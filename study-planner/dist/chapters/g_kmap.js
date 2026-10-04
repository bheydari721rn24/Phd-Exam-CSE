"use strict";
(()=>{
 const gray=[0,1,3,2];
 function members(pattern){let a=[];for(let i=0;i<16;i++)if([...pattern].every((v,j)=>v==="-"||Number(v)===((i>>(3-j))&1)))a.push(i);return a;}
 function solve(on,dc,mode){
  const required=mode==="POS"?Array.from({length:16},(_,i)=>i).filter(i=>!on.includes(i)&&!dc.includes(i)):on.slice();
  const allowed=new Set([...required,...dc]);let valid=[];
  for(let k=0;k<81;k++){let z=k,p="";for(let j=0;j<4;j++){p="01-"[z%3]+p;z=Math.floor(z/3);}const rows=members(p);if(rows.every(i=>allowed.has(i))&&rows.some(i=>required.includes(i)))valid.push({pattern:p,rows,literals:[...p].filter(x=>x!=="-").length});}
  const primes=valid.filter(a=>!valid.some(b=>a.rows.length<b.rows.length&&a.rows.every(x=>b.rows.includes(x)))).sort((a,b)=>a.pattern<b.pattern?-1:a.pattern>b.pattern?1:0);
  let covers=[],best=required.length?[Infinity,Infinity]:[0,0];
  if(!required.length)covers=[[]];else for(let mask=1;mask<2**primes.length;mask++){
   let selected=[],rows=new Set(),lit=0;for(let j=0;j<primes.length;j++)if(mask&2**j){selected.push(primes[j].pattern);lit+=primes[j].literals;primes[j].rows.forEach(x=>rows.add(x));}
   const cost=[selected.length,lit];if(cost[0]>best[0]||(cost[0]===best[0]&&cost[1]>best[1]))continue;
   if(required.every(x=>rows.has(x))){if(cost[0]<best[0]||cost[1]<best[1]){best=cost;covers=[];}covers.push(selected);}
  }
  covers.sort((a,b)=>a.join("|")<b.join("|")?-1:a.join("|")>b.join("|")?1:0);
  return {on:on.slice(),dc:dc.slice(),mode,required:required.sort((a,b)=>a-b),primes,covers,cost:best};
 }
 function formula(cover,pos){if(!cover.length)return pos?"1":"0";return cover.map(c=>{let a=[];[...c].forEach((b,j)=>{if(b!=="-")a.push("ABCD"[j]+((pos?b==="1":b==="0")?"\u0305":""));});return a.length?(pos?"("+a.join(" + ")+")":a.join("")):(pos?"0":"1");}).join(pos?" · ":" + ");}
 window.KmapLab={solve,members,formula};
 addEventListener("DOMContentLoaded",()=>{
  const form=document.getElementById("kmap-form"),host=document.getElementById("kmap-player"),out=document.getElementById("kmap-output");let player;
  const node=(id,label,x,y,w=105,h=38,tone="plain",size=20)=>({id,label:String(label),x,y,w,h,tone,size,kind:"card"});
  function parse(raw){if(!raw.trim())return [];if(!/^\d+(\s*,\s*\d+)*$/.test(raw.trim()))throw Error();const a=raw.split(",").map(Number);if(a.some(x=>!Number.isSafeInteger(x)||x<0||x>15)||new Set(a).size!==a.length)throw Error();return a.sort((a,b)=>a-b);}
  function run(e){e?.preventDefault();let on,dc;
   try{on=parse(form.elements.on.value);dc=parse(form.elements.dc.value);if(on.some(x=>dc.includes(x)))throw Error();}catch{player?.pause();host.hidden=true;out.dataset.valid="false";out.textContent="Enter distinct comma-separated indices from 0 to 15. Empty sets are allowed; one and don’t-care sets must not overlap.";return;}
   const data=solve(on,dc,form.elements.mode.value),cover=data.covers[0],frames=[],states=[];let seen=new Set();
   for(let k=0;k<=cover.length;k++){
    if(k)members(cover[k-1]).forEach(x=>seen.add(x));const nodes=[];
    for(let j=0;j<4;j++)nodes.push(node("col"+j,gray[j].toString(2).padStart(2,"0"),180+120*j,40,75,34,"plain",18));
    for(let r=0;r<4;r++){nodes.push(node("row"+r,gray[r].toString(2).padStart(2,"0"),70,90+55*r,70,38,"plain",18));for(let c=0;c<4;c++){let i=4*gray[r]+gray[c],v=on.includes(i)?"1":dc.includes(i)?"X":"0";nodes.push(node("m"+i,i+": "+v,180+120*c,90+55*r,105,38,seen.has(i)?"done":"plain"));}}
    nodes.push(node("token",k?cover[k-1]:"start",180+120*(k%4),320,115,38,"active"));
    const state={selected:cover.slice(0,k),covered:[...seen].sort((a,b)=>a-b),requiredCovered:data.required.filter(i=>seen.has(i)),step:k};states.push(state);
    const caption=k?"Select cube "+cover[k-1]+". The accumulated union covers required "+(data.mode==="SOP"?"one":"zero")+" rows "+JSON.stringify(state.requiredCovered)+". Optional cells are permitted, while every forbidden care row remains excluded.":"Start with the exact fixed specification and no selected candidates. Required rows are obligations; optional cells may assist a group but never require coverage.";
    frames.push({nodes,caption,captionHtml:"<p>"+caption+"</p>",metrics:{Selected:k,Covered:state.requiredCovered.length},metricLabels:{Selected:"Selected candidates",Covered:"Covered obligations"},formula:"",line:0,edges:[],snapshot:state});
   }
   if(frames.length===1){frames.push({...frames[0],caption:"There are no required obligations in this representation. The empty cover realizes the appropriate constant and has zero terms and zero literals.",captionHtml:"<p>There are no required obligations. The empty cover realizes the appropriate constant with zero terms and literals.</p>"});states.push(states[0]);}
   const scene={id:"kmap-custom-"+data.mode,title:"Exact "+data.mode+" cover",descriptionHtml:"<p>All valid four-input cubes and every lexicographic optimum are computed from the stated care sets.</p>",invariantHtml:"<p>Each selected cube avoids forbidden rows. SOP covers required ones; POS covers required zeros through the complement. This laboratory does not certify hazard constraints.</p>",frames,code:[]};
   host.hidden=false;if(player){player.pause();player.scenes=[scene];player.scene=scene;player.index=0;player.choice.options[0].textContent=scene.title;player.choice.value=0;player.show(0,false);}else player=ConceptAnimations.mount(host,[scene]);
   out.dataset.valid="true";out.dataset.result=JSON.stringify(data);out.dataset.states=JSON.stringify(states);
   out.replaceChildren();const add=(tag,s)=>{const x=document.createElement(tag);x.textContent=s;out.append(x);return x;};
   add("p","Exact optimum: "+data.cost[0]+" candidates and "+data.cost[1]+" literals; "+data.covers.length+" tied optimum expressions.");
   data.covers.forEach(c=>{const p=add("p","F = "+formula(c,data.mode==="POS"));p.style.fontFamily='"STIX Two Math", serif';});
   const table=document.createElement("table");const h=table.insertRow();["Prime cube","Required rows covered","Literals"].forEach(s=>{const th=document.createElement("th");th.textContent=s;h.append(th);});data.primes.forEach(p=>{const tr=table.insertRow();[p.pattern,p.rows.filter(i=>data.required.includes(i)).join(", "),p.literals].forEach(s=>tr.insertCell().textContent=s);});out.append(table);
   add("p","Trace starts paused and shows the first optimum. All tied results appear above. Gray axes are AB and CD; DC completion may differ between SOP and POS.");
  }
  form.addEventListener("submit",run);form.addEventListener("input",run);form.addEventListener("change",run);run();
  document.querySelectorAll(".kmap-diagram").forEach(fig=>{const b=document.createElement("button");b.type="button";b.className="kmap-figure-toggle";b.textContent="Enlarge diagram";b.setAttribute("aria-expanded","false");b.addEventListener("click",()=>{const open=fig.classList.toggle("expanded");b.textContent=open?"Fit diagram to page":"Enlarge diagram";b.setAttribute("aria-expanded",String(open));});fig.prepend(b);});
 });
})();
