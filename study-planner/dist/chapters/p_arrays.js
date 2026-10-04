"use strict";
addEventListener("DOMContentLoaded",()=>{
 const form=document.getElementById("arrays-form"),host=document.getElementById("arrays-player"),out=document.getElementById("arrays-output");let player;
 const node=(id,v,x,y,w=88)=>({id,label:String(v),x,y,w,h:48,tone:id==="token"?"active":"plain",kind:"card",size:21});
 function build(mode,input){
  let a=input.slice(),prefix=[0],write=0,states=[];
  const put=(i,caption,extra={})=>states.push({values:a.slice(),prefix:prefix.slice(),write,index:i,caption,...extra});
  put(0,"Begin with the complete original sequence. No destination write or compaction has occurred; the prefix boundary at zero is initialized to zero.");
  if(mode==="prefix")for(let i=0;i<a.length;i++){prefix.push(prefix.at(-1)+a[i]);put(i,"Read original input index "+i+" and add it to the previous prefix value. Store the sum at the next exclusive boundary.",{token:prefix.at(-1),from:i,to:i+1});}
  if(mode==="right"||mode==="bad"){
   let indices=Array.from({length:a.length-1},(_,i)=>i);if(mode==="right")indices.reverse();
   for(const i of indices){const v=a[i];a[i+1]=v;put(i,"Read current source index "+i+" and write its value to index "+(i+1)+". "+(mode==="right"?"Descending order preserves every unread original source value.":"Ascending order can reread an overwritten value. This deliberately faulty procedure is a counterexample."),{token:v,from:i,to:i+1});}
  }
  if(mode==="reverse")for(let i=0;i<Math.floor(a.length/2);i++){const j=a.length-1-i;[a[i],a[j]]=[a[j],a[i]];put(i,"Exchange indices "+i+" and "+j+" as one pair-swap checkpoint. Both completed ends now match their final reversed original values.",{token:a[j],from:i,to:j});}
  if(mode==="difference")for(let i=a.length-1;i>0;i--){a[i]-=a[i-1];put(i,"Subtract the still original predecessor at index "+(i-1)+" from index "+i+". Descending order leaves every lower source value unmodified.",{token:a[i],from:i-1,to:i});}
  if(mode==="compact")for(let i=0;i<a.length;i++){const v=input[i];if(v%2===0){a[write]=v;write++;}put(i,"Read original value "+v+" at index "+i+". "+(v%2===0?"Retain it at the next output position; the prefix keeps encounter order.":"Discard it and keep the output boundary unchanged; unused trailing slots are not part of the result."),{token:v,from:i,to:v%2===0?write-1:i});}
  if(states.length===1)put(0,"This one-element input needs no write for the selected operation. Its original value is already the complete required result.");
  const frames=states.map((s,i)=>{
   const nodes=s.values.map((v,k)=>node("a"+k,v,65+100*k,65));
   if(mode==="prefix")for(let k=0;k<=a.length;k++)nodes.push(node("p"+k,k<s.prefix.length?s.prefix[k]:"—",65+100*k,165));
   else nodes.push(node("extent",mode==="compact"?"Retained length = "+s.write:"Length = "+a.length,350,170,300));
   nodes.push(node("token",i===0?"start":s.token??"unchanged",65+100*(s.to??s.index),280,105));
   return {nodes,caption:s.caption,captionHtml:"<p>"+s.caption+"</p>",metrics:{Checkpoint:i+1,Length:a.length},metricLabels:{Checkpoint:"Checkpoint",Length:"Length"},formula:"",line:0,edges:[],snapshot:{mode,input:input.slice(),...s}};
  });
  return {id:"arrays-custom-"+mode,title:form.elements.mode.selectedOptions[0].textContent,descriptionHtml:"<p>Exact bounded integer transformations with explicit original input and visible logical boundaries.</p>",invariantHtml:"<p>Values and write order follow the selected contract. A faulty forward move is deliberately labeled a counterexample; trailing compacted storage is not logical output.</p>",frames,code:[]};
 }
 function run(e){e?.preventDefault();const raw=form.elements.input.value.trim();
  if(!/^-?\d+(\s*,\s*-?\d+){0,5}$/.test(raw)){invalid();return;}
  const a=raw.split(",").map(Number);if(a.some(x=>!Number.isSafeInteger(x)||x< -20||x>20)){invalid();return;}
  const scene=build(form.elements.mode.value,a);host.hidden=false;
  if(player){player.pause();player.scenes=[scene];player.scene=scene;player.index=0;player.choice.options[0].textContent=scene.title;player.choice.value=0;player.show(0,false);}else player=ConceptAnimations.mount(host,[scene]);
  out.dataset.valid="true";out.dataset.states=JSON.stringify(scene.frames.map(f=>f.snapshot));out.textContent="Trace begins paused. Inspect each exact write with Next step, or use playback and the checkpoint slider.";
 }
 function invalid(){player?.pause();host.hidden=true;out.dataset.valid="false";out.textContent="Enter one to six comma-separated integers, each from −20 through 20.";}
 form.addEventListener("submit",run);form.addEventListener("input",run);form.addEventListener("change",run);run();
 document.querySelectorAll(".arrays-diagram").forEach(fig=>{const b=document.createElement("button");b.type="button";b.className="arrays-figure-toggle";b.textContent="Enlarge diagram";b.setAttribute("aria-expanded","false");b.addEventListener("click",()=>{const open=fig.classList.toggle("expanded");b.textContent=open?"Fit diagram to page":"Enlarge diagram";b.setAttribute("aria-expanded",String(open));});fig.prepend(b);});
});
