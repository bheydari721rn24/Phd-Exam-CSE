/* Subject-specific diagrams. Geometry encodes the actual saved state; color is secondary. */
"use strict";
(() => {
const NS="http://www.w3.org/2000/svg", C={ink:"#28495b",blue:"#277d9f",green:"#268466",red:"#b4425f",amber:"#bc831c",pale:"#e9f3f7"};
const E=(tag,a={})=>{const e=document.createElementNS(NS,tag);Object.entries(a).forEach(([k,v])=>e.setAttribute(k,v));return e;};
function text(g,x,y,s,size=18,anchor="middle",color=C.ink){const t=E("text",{x,y,"font-size":size,"text-anchor":anchor,fill:color});String(s).split("\n").forEach((line,i)=>{const a=E("tspan",{x,dy:i?size*1.25:0});a.textContent=line;t.append(a);});g.append(t);return t;}
function path(g,d,color=C.ink,width=2,extra={}){const e=E("path",{d,fill:"none",stroke:color,"stroke-width":width,...extra});g.append(e);return e;}
function rect(g,x,y,w,h,fill=C.pale,stroke=C.ink){g.append(E("rect",{x,y,width:w,height:h,fill,stroke,"stroke-width":1}));}
function dot(g,x,y,r=5,fill=C.blue){g.append(E("circle",{cx:x,cy:y,r,fill}));}
function arrow(g,x,y,X,Y,color=C.blue){return path(g,`M${x} ${y}L${X} ${Y}`,color,1.6,{'data-layout-arrow':JSON.stringify([[x,y],[X,Y]])});}
const num=v=>{if(typeof v==="number")return v;if(v===true)return 1;if(v===false)return 0;const s=String(v),m=s.match(/^(-?\d+(?:\.\d+)?)\/(-?\d+(?:\.\d+)?)$/);return m?+m[1]/+m[2]:Number(s);};
const tone=n=>n.tone==="active"?C.amber:n.tone==="warning"?C.red:n.tone==="done"?C.green:C.blue;
function strip(g,x,y,values,{cell=64,labels=true,active=-1,title="",tones=[]}={}){if(title)text(g,x,y-23,title,18,"start");values.forEach((v,i)=>{rect(g,x+i*cell,y,cell,46,i===active?"#ffe0a1":"#f4f9fb");text(g,x+(i+.5)*cell,y+29,typeof v==="object"?v.value??v.join(" · "):v,20,"middle",tones[i]||C.ink);if(labels)text(g,x+(i+.5)*cell,y+68,i,15);});}
function matrix(g,M,x,y,label,mark=[]){if(!M?.length||!Array.isArray(M[0]))return;const rows=M.length,cols=M[0].length,dx=Math.min(66,270/cols),dy=Math.min(48,210/rows);text(g,x+cols*dx/2,y-24,label,20);path(g,`M${x+7} ${y-10}h-12v${rows*dy+6}h12M${x+cols*dx-7} ${y-10}h12v${rows*dy+6}h-12`);M.forEach((r,i)=>r.forEach((v,j)=>{if(mark.some(p=>p[0]===i&&p[1]===j))rect(g,x+j*dx+2,y+i*dy-5,dx-4,dy-2,"#ffe0a1","none");text(g,x+(j+.5)*dx,y+i*dy+25,v,21);}));return {w:cols*dx,h:rows*dy};}
function axes(g,{x=90,y=295,w=590,h=235,xlabel="x",ylabel="y"}={}){arrow(g,x,y,x+w,y,C.ink);arrow(g,x,y,x,y-h,C.ink);text(g,x+w/2,y+38,xlabel,17);text(g,x-6,y-h-15,ylabel,18);return {x,y,w,h};}
function bars(p,g,f,pos){
 const a=f.snapshot?.array,records=f.nodes.filter(n=>/^(r|record)\d+$/.test(n.id)),n=a?.length||records.length;
 if(p.scene.id==='max-subarray'){const selected=({total:[0,7],prefix:[0,5],suffix:[6,7],best:[2,5]}[f.metrics.Component]);text(g,380,40,`${f.metrics.Component}: selected indices [${selected[0]}, ${selected[1]})`,21);records.forEach((r,i)=>{rect(g,55+i*88,120,78,60,i>=selected[0]&&i<selected[1]?'#cce9dc':'#edf5f8');text(g,94+i*88,158,r.label.split(' · ')[0],23);text(g,94+i*88,209,i,16);});text(g,380,290,'The four summary components use different allowed index ranges.',20);return;}
 for(let i=0;i<n;i++){rect(g,49+92*i,75,82,60,'#fafcfd','#b9cbd4');text(g,90+92*i,206,i,16);}
 text(g,380,34,'Fixed array slots; the lower labels are indices',20);
 for(const r of records){const q=pos.get(r.id)||r,held=r.y>200,y=held?q.y:q.y-5,group=E('g',{'data-record':r.id,transform:`translate(${q.x} ${y})`});rect(group,-41,-25,82,54,r.tone==='active'?'#ffe0a1':r.tone==='done'?'#cce9dc':'#edf5f8');const [key,tag]=r.label.split(' · ');text(group,0,-2,key,23);if(tag)text(group,0,19,tag,14);g.append(group);p.nodes.set(r.id,group);}
 if(f.snapshot?.saved){text(g,610,255,'Saved record outside storage',18);text(g,610,285,'The hole is not a second copy.',17);}
 const h=f.nodes.find(n=>n.id==='hole');if(h){const q=pos.get(h.id)||h;path(g,`M${q.x-30} 99h60`,C.amber,2,{'stroke-dasharray':'5 4'});text(g,q.x,130,'hole',16);}
 if(f.snapshot&&'lt' in f.snapshot){const z=f.snapshot;[[0,z.lt,'< pivot'],[z.lt,z.i,'= pivot'],[z.i,z.gt,'unknown'],[z.gt,n,'> pivot']].forEach(([lo,hi,label],j)=>{text(g,115+j*175,245,label,18);text(g,115+j*175,277,`[${lo}, ${hi})`,18);path(g,`M${60+j*175} 299h110`,[C.green,C.blue,C.amber,C.green][j],4);});}
}

function search(p,g,f){const s=f.snapshot,a=s.array.map(v=>Array.isArray(v)?v[1]:v),cell=Math.min(82,620/a.length),x=65;strip(g,x,130,a,{cell,title:`Sorted input; target = ${s.target}`});const lo=x+s.lo*cell,hi=x+s.hi*cell;path(g,`M${lo} 110V100H${hi}V110`,C.amber,4);text(g,Math.max(145,Math.min(615,(lo+hi)/2)),78,`Unresolved interval [${s.lo}, ${s.hi})`,21);text(g,190,270,"Earlier indices: value < target",18);text(g,560,270,"Later indices: value ≥ target",18);text(g,380,315,`Width = ${s.hi-s.lo}; coincident boundaries denote an empty interval`,18);}
function venn(p,g,f){const s=f.snapshot;rect(g,35,35,690,290,"#fff","#718f9e");text(g,58,62,"U",20);g.append(E("ellipse",{cx:285,cy:165,rx:155,ry:110,fill:"#e8f3f8",stroke:C.blue}));g.append(E("ellipse",{cx:475,cy:165,rx:155,ry:110,fill:"#f0f8ed","fill-opacity":.65,stroke:C.green}));text(g,210,85,"A",23);text(g,550,85,"B",23);const groups=[s.U.filter(v=>s.A.includes(v)&&!s.B.includes(v)),s.U.filter(v=>s.A.includes(v)&&s.B.includes(v)),s.U.filter(v=>!s.A.includes(v)&&s.B.includes(v)),s.U.filter(v=>!s.A.includes(v)&&!s.B.includes(v))];groups.forEach((vs,j)=>vs.forEach((v,i)=>{const x=[230,380,530,670][j],y=140+i*62;dot(g,x,y,22,s.result.includes(v)?C.green:s.inspected.includes(v)?"#dae3e7":C.blue);text(g,x,y+7,v,21,"middle",s.result.includes(v)||!s.inspected.includes(v)?"white":C.ink);}));text(g,380,348,`Selected elements after this inspection: {${s.result.join(", ")}}`,18);}
function truth(p,g,f){
 const rows=[...new Map(p.scene.frames.filter(x=>x.snapshot?.inputs).map(r=>[JSON.stringify(r.snapshot.inputs),r])).values()],arity=rows[0]?.snapshot.inputs.length||2,inputs=f.snapshot?.inputs||[];
 const cols=arity+2,dx=Math.min(110,580/cols),x=(760-cols*dx)/2,y=66,h=Math.min(42,235/rows.length);
 [...Array(arity)].map((_,i)=>String.fromCharCode(112+i)).concat(['Left','Right']).forEach((v,i)=>text(g,x+(i+.5)*dx,y-20,v,20));
 rows.forEach((r,k)=>{const active=JSON.stringify(r.snapshot.inputs)===JSON.stringify(inputs);rect(g,x,y+k*h,cols*dx,h,active?'#ffe0a1':'#fff','#bed0d8');[...r.snapshot.inputs,r.snapshot.left,r.snapshot.right].forEach((v,i)=>text(g,x+(i+.5)*dx,y+k*h+h/2+7,v,19));});
 text(g,380,335,'One row per complete valuation; both expressions receive the same inputs.',18);
}

function graph(p,g,f,pos){const nodes=f.nodes.filter(n=>!/^m\d\d$/.test(n.id)),ids=new Map(nodes.map(n=>[n.id,pos.get(n.id)||n]));const map=/function|quantifier|cartesian|right-inverse|image-collapse/.test(p.scene.id);if(map){const xs=[...new Set(nodes.map(n=>n.x))].sort((a,b)=>a-b);if(xs.length<=3)xs.forEach((x,i)=>{g.append(E("ellipse",{cx:x,cy:173,rx:64,ry:150,fill:"#f4f9fb",stroke:"#c4d8e1"}));text(g,x,345,`${["Domain","Middle set","Codomain"][xs.length===2&&i===1?2:i]}`,16);});}
 for(const e of f.edges||[]){const a=ids.get(e.from),b=ids.get(e.to);if(!a||!b)continue;const color=e.tone==="warning"?C.red:e.tone==="active"?C.amber:C.blue;if(e.from===e.to){path(g,`M${a.x-12} ${a.y-18}C${a.x-50} ${a.y-70} ${a.x+50} ${a.y-70} ${a.x+12} ${a.y-18}`,color);continue;}const d=Math.hypot(b.x-a.x,b.y-a.y)||1,x=a.x+(b.x-a.x)*23/d,y=a.y+(b.y-a.y)*23/d,X=b.x-(b.x-a.x)*25/d,Y=b.y-(b.y-a.y)*25/d;if(e.directed)arrow(g,x,y,X,Y,color);else path(g,`M${x} ${y}L${X} ${Y}`,color,2.5);}
 nodes.forEach(n=>{const a=pos.get(n.id)||n;if(n.label.length<10){dot(g,a.x,a.y,22,tone(n));text(g,a.x,a.y+7,n.label,20,"middle","#fff");}else {dot(g,a.x,a.y,7,tone(n));text(g,a.x,a.y-18,n.label,17);}});
 const s=f.snapshot;if(s?.relation){const M=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>+s.relation.some(([a,b])=>a===i&&b===j)));matrix(g,M,245,155,"Reachability matrix");}
}
function geometry(p,g,f,pos){let ox=300,oy=245;const O=f.nodes.find(n=>["O","v0"].includes(n.id));if(O&&p.scene.id!=="affine-origin"){ox=O.x;oy=O.y;}for(let x=ox%65;x<720;x+=65)path(g,`M${x} 32V322`,"#e0ebef",1);for(let y=oy%65;y<323;y+=65)path(g,`M35 ${y}H725`,"#e0ebef",1);arrow(g,35,oy,723,oy,C.ink);arrow(g,ox,323,ox,25,C.ink);text(g,738,oy+5,"x",18);text(g,ox+15,20,"y",18);for(const e of f.edges||[]){const a=pos.get(e.from),b=pos.get(e.to);if(a&&b)arrow(g,a.x,a.y,b.x,b.y,e.tone==="active"?C.amber:C.blue);}for(const n of f.nodes){const a=pos.get(n.id)||n;dot(g,a.x,a.y,5,tone(n));text(g,a.x+(n.labelDx||0),a.y+(n.labelDy||-18),n.label,17);}
 if(p.scene.id==="projection"&&f.nodes.some(n=>n.id==="p")){const a=pos.get("p"),b=pos.get("a"),o=pos.get("O"),dir=pos.get("b"),ux=(dir.x-o.x)/Math.hypot(dir.x-o.x,dir.y-o.y),uy=(dir.y-o.y)/Math.hypot(dir.x-o.x,dir.y-o.y),vx=(b.x-a.x)/Math.hypot(b.x-a.x,b.y-a.y),vy=(b.y-a.y)/Math.hypot(b.x-a.x,b.y-a.y);path(g,`M${a.x+ux*12} ${a.y+uy*12}l${vx*12} ${vy*12}l${-ux*12} ${-uy*12}`,C.green);}
}
function matrices(p,g,f,pos){const s=f.snapshot||{},id=p.scene.id;let groups=[];if(id==="matrix-summaries")groups=[["A: trace 5; squared Frobenius norm 30",[[1,2],[3,4]]]];else if(id==="matrix-product")groups=[["A",[[1,2],[3,4]]],["B",[[2,0],[1,2]]],["C",s.C]];else if(s.matrix)groups=[["Current matrix",s.matrix]];else if(s.L&&s.U)groups=[["L",s.L],["U",s.U],...(s.P?[["P",s.P]]:[])];else {for(const k of ["A","B","AB","C","F","E","P","Q","result","input"])if(Array.isArray(s[k]?.[0]))groups.push([k,s[k]]);}
 if(groups.length){groups=groups.slice(0,3);groups.forEach(([name,M],i)=>{const mark=id==="matrix-summaries"?[[Math.floor(p.index/2),p.index%2]]:id==="matrix-product"?(i===0?[[s.i,s.k]]:i===1?[[s.k,s.j]]:[[s.i,s.j]]):(s.pivots||[]).map((c,r)=>[r,c]);matrix(g,M,groups.length===1?200:35+i*245,85,name,mark);});if(id==='matrix-product'){
 const A=[[1,2],[3,4]],B=[[2,0],[1,2]],left=A[s.i][s.k],right=B[s.k][s.j],after=num(s.C[s.i][s.j]),before=after-left*right;
 text(g,380,285,`Accumulate C[${s.i},${s.j}]: ${before} + (${left} × ${right}) = ${after}`,23);
 text(g,380,330,`A[${s.i},${s.k}] and B[${s.k},${s.j}] share inner index ${s.k}.`,19);
 }if(s.op)text(g,380,330,s.op,21);if(s.x)text(g,380,330,`Input coordinates: (${s.x.join(", ")})`,20);return;}
 const ns=f.nodes.filter(n=>/^[a-z]\d\d$/.test(n.id));if(ns.length){const prefixes=[...new Set(ns.map(n=>n.id[0]))];prefixes.forEach(prefix=>{const group=ns.filter(n=>n.id[0]===prefix),xs=group.map(n=>(pos.get(n.id)||n).x),ys=group.map(n=>(pos.get(n.id)||n).y),left=Math.min(...xs)-40,right=Math.max(...xs)+40,top=Math.min(...ys)-28,bottom=Math.max(...ys)+30;path(g,`M${left+8} ${top}H${left}V${bottom}H${left+8}M${right-8} ${top}H${right}V${bottom}H${right-8}`);group.forEach(n=>{const a=pos.get(n.id)||n;if(n.tone==="active")rect(g,a.x-30,a.y-25,60,48,"#ffe0a1","none");text(g,a.x,a.y+7,n.label,22);});});return;}
 derivationExact(p,g,f);
}
function tiles(p,g,f){const s=f.snapshot;if(p.scene.id==="strong-coins"){s.coins.forEach((v,i)=>{dot(g,75+i*80,165,30,i===s.coins.length-1?C.amber:C.green);text(g,75+i*80,173,v,25,"middle","white");});text(g,380,280,`${s.coins.join(" + ")} = ${s.n}`,26);return;}f.nodes.forEach(n=>{rect(g,n.x-18,n.y-16,36,32,n.tone==="active"?"#ffe0a1":"#cce9dc",C.green);});text(g,570,135,`n = ${s.n}`,25);text(g,570,180,`${s.count} unit tiles`,23);}
function arrayMemory(p,g,f,pos){const s=f.snapshot||{},id=p.scene.id;let a=s.values||s.input||s.new||s.prefix;if(id==="arr-row"||id==="arr-column"){const M=Array.from({length:3},(_,i)=>Array.from({length:4},(_,j)=>`${i},${j}`));matrix(g,M,60,95,"Logical 3 × 4 array",[s.coord]);strip(g,375,120,Array.from({length:12},(_,i)=>i),{cell:26,active:s.offset,title:"Physical offsets: row-major storage"});text(g,535,260,`(${s.coord}) → offset ${s.offset}`,22);return;}
 if(id==="arr-transpose"){matrix(g,s.source,55,92,"Source",[[s.i,s.j]]);matrix(g,s.destination,415,92,"Destination",[[s.j,s.i]]);arrow(g,320,170,400,170);text(g,380,320,`(${s.i},${s.j}) → (${s.j},${s.i})`,23);return;}
 if(id==="arr-ring"){const r=105,cx=250,cy=180;for(let i=0;i<5;i++){const a=-Math.PI/2+i*2*Math.PI/5,x=cx+r*Math.cos(a),y=cy+r*Math.sin(a);dot(g,x,y,25,i===s.physical?C.amber:C.blue);text(g,x,y+7,i,21,"middle","white");}text(g,555,140,`Logical index: ${s.t}`,22);text(g,555,185,`Physical index: ${s.physical}`,22);text(g,555,245,"The address wraps;\nlogical order does not.",18);return;}
 if(id==="arr-packed"){const M=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>j<=i?i*(i+1)/2+j:"—"));matrix(g,M,160,80,"Packed lower triangle",[[s.i,s.j]]);text(g,550,180,`Offset ${s.offset}`,24);return;}
 if(a&&Array.isArray(a)&&!Array.isArray(a[0])){const cell=Math.min(83,630/a.length);strip(g,55,125,a,{cell,active:s.index??s.read??-1,title:id.includes("prefix")?"Prefix boundaries":"Contiguous indexed storage"});if(s.source!==undefined&&s.destination!==undefined){arrow(g,55+(s.source+.5)*cell,245,55+(s.destination+.5)*cell,245,C.amber);text(g,380,285,"Read source before writing destination",20);}if(s.write!==undefined)text(g,380,300,`Read boundary ${s.read}; write boundary ${s.write}`,21);if(s.length!==undefined)text(g,380,300,`Logical length = ${s.length}`,21);return;}
 const ns=f.nodes.filter(n=>/^r\d|^a\d|^b\d|^old|^new|^cell/.test(n.id));if(ns.length){ns.forEach(n=>{const a=pos.get(n.id)||n;rect(g,a.x-30,a.y-24,60,48,n.tone==="active"?"#ffe0a1":"#f3f9fb");text(g,a.x,a.y+7,n.label,19);text(g,a.x,a.y+44,n.id,14);});return;}memory(p,g,f,pos);
}
function memory(p,g,f,pos){const s=f.snapshot||{};if(p.scene.id==="fn-recursion"){const depth=s.depth;rect(g,75,35,380,300,"#f8fbfd");text(g,265,23,"Active call stack",20);for(let k=0;k<=depth;k++){rect(g,95,55+k*65,340,55,k===depth?"#ffe0a1":"#e5eff5");text(g,265,89+k*65,`frame ${k}: n = ${3-k}`,21);}const token=f.nodes.find(n=>n.id==="token"),a=pos.get("token")||token;arrow(g,455,a.y,520,a.y,C.amber);text(g,600,a.y+7,token.label,19);return;}
 const labels=[s.caller,s.callee,s.shared].filter(v=>v!==undefined);if(labels.length){rect(g,30,48,300,130,"#eff5f9");rect(g,430,48,300,130,"#f0f8f3");text(g,180,30,"Caller frame",20);text(g,580,30,"Callee frame",20);wrapped(g,180,92,s.caller,30);wrapped(g,580,92,s.callee,30);if(s.shared!==undefined&&s.shared!==null&&!/No shared/.test(String(s.shared))){rect(g,215,245,330,80,"#fff4dd");wrapped(g,380,275,s.shared,33);if(!/ended|Not entered/.test(s.callee)){arrow(g,580,178,500,245,C.green);text(g,680,215,"reference",15);}arrow(g,180,178,260,245,C.blue);}const a=pos.get("value")||pos.get("token")||{x:s.x||380,y:210};dot(g,a.x,210,18,C.amber);text(g,a.x,216,s.value,17);return;}
 const vars=f.nodes.filter(n=>["x","y","sum","value","guard","rhs"].includes(n.id));vars.forEach((n,i)=>{const x=70+i*200;path(g,`M${x} 105h170v65H${x}z`);text(g,x+85,142,n.label,20);text(g,x+85,83,n.id,17);});if(!vars.length)derivationExact(p,g,f);else text(g,380,280,`Current statement: ${(p.scene.code||[])[f.line]||"observe the store"}`,20);}
function wrapped(g,x,y,s,width=32){const words=String(s).split(" "),lines=[];let a="";for(const w of words){if((a+" "+w).length>width){lines.push(a);a=w;}else a+=(a?" ":"")+w;}if(a)lines.push(a);text(g,x,y,lines.join("\n"),18);}
function derivation(p,g,f){const steps=p.scene.frames.slice(0,p.index+1);text(g,380,30,"Justified transformations",22);steps.slice(-5).forEach((s,i)=>{const y=72+i*54;const label=s.nodes.find(n=>n.id==="claim")?.label||s.formula||s.nodes.map(n=>n.label).join("; ");path(g,`M80 ${y+16}H675`,i===Math.min(4,steps.length-1)?C.amber:"#c6d9e3",2);wrapped(g,380,y,label,65);if(i)arrow(g,52,y-32,52,y-3,C.green);});}
function numeric(p,g,f){const s=f.snapshot||{},id=p.scene.id;if(id==="division"){for(let i=0;i<s.X;i++){const group=Math.floor(i/s.Y),x=70+(i%s.Y)*30+group*95,y=115;dot(g,x,y,10,i<s.q*s.Y?C.green:C.amber);}text(g,380,225,`${s.X} = ${s.q} × ${s.Y} + ${s.r}`,28);text(g,380,280,`${s.q} complete groups; ${s.r} units remain`,22);return;}if(id==="euclid"){const rows=p.scene.frames.slice(0,p.index+1).map(x=>x.snapshot);rows.forEach((r,i)=>{const y=55+i*48;text(g,160,y,`(${r.a}, ${r.b})`,23);if(i)arrow(g,65,y-30,65,y-5,C.green);text(g,455,y,`${r.a} = ${r.A}(${r.x0}) + ${r.B}(${r.y0})`,21);});return;}
 if(["power","modular-power"].includes(id)){strip(g,80,135,[s.r,s.b,s.e],{cell:190,labels:false,title:"Accumulator          Evolving base          Remaining exponent"});text(g,380,255,`Original problem: ${s.x} to power ${s.y}${s.M?` modulo ${s.M}`:""}`,23);return;}
 const bits=f.nodes.find(n=>["bits","binary","gray"].includes(n.id))?.label||f.metrics.Binary||f.metrics.Codeword;if(bits&&/^[01]{3,}/.test(bits)){strip(g,85,140,bits.split(""),{cell:70,title:"Bits in most-significant-first order"});text(g,380,280,f.formula||p.scene.title,21);return;}if(id==="hamming-code"){strip(g,45,120,f.nodes.map(n=>n.label),{cell:92,title:"Hamming positions 1–7",labels:false});f.nodes.forEach((n,i)=>text(g,91+i*92,212,`position ${i+1}`,16,"middle",tone(n)));return;}derivationExact(p,g,f);
}
function probability(p,g,f){const s=f.snapshot||{},id=p.scene.id;
 if(id==="conditional-strip"){const a=axes(g,{x:100,y:305,w:230,h:230,xlabel:"X",ylabel:"Y"}),e=num(s.epsilon);path(g,`M100 75L330 305H100Z`,C.blue);const xmax=Math.min(1,e);g.append(E("polygon",{points:`100,305 ${100+230*xmax},305 ${100+230*xmax},${75+230*xmax} 100,75`,fill:"#c6e8da"}));text(g,510,130,`Retained width ε = ${s.epsilon}`,22);text(g,510,185,`Information mass = ${s.mass}`,21);text(g,510,240,`Conditional ratio = ${s.ratio}`,21);return;}
 if(id==="conditional-bridge"){const pts=[[90,180],[325,70],[325,285],[635,180]],edges=[[0,1],[1,3],[0,2],[2,3],[1,2]];edges.forEach(([a,b],i)=>{path(g,`M${pts[a]}L${pts[b]}`,s.bits[i]?C.green:"#c5d0d7",s.bits[i]?5:2,{"stroke-dasharray":s.bits[i]?"none":"6 6"});text(g,(pts[a][0]+pts[b][0])/2+(i===4?30:0),(pts[a][1]+pts[b][1])/2-12,`e${i+1}`,18);});pts.forEach(([x,y],i)=>{dot(g,x,y,12,C.blue);text(g,x,y+35,["s","u","v","t"][i],22);});text(g,535,330,s.connected?"A live path connects s to t":"No live path connects s to t",19);return;}
 if(id==="bayes-density"){const {x,y,w,h}=axes(g,{x:80,y:300,w:570,h:220,xlabel:"θ",ylabel:"density"}),values=s.densities.map(num),scale=Math.max(1,...p.scene.frames.flatMap(a=>a.snapshot.densities.map(num)));path(g,values.map((v,i)=>`${i?"L":"M"}${x+w*i/(values.length-1)} ${y-h*v/scale}`).join(" "),C.green,3);text(g,380,345,`Beta(${num(s.h)+1}, ${num(s.t)+1}); density scale 0–${scale.toFixed(2)}`,18);return;}
 if(["bayes-sensitivity","bayes-repeat","bayes-copy","bayes-predict","bayes-host","bayes-loss","probability-limit","growth-threshold","encoding-length","loop-doubling"].includes(id)){plot(p,g,f);return;}
 let values=s.values||s.weights||s.posteriors||s.masses||s.joint||s.marginal||s.likelihoods;
 if(Array.isArray(values?.[0]))values=values.flat();if(values&&typeof values==="object"&&!Array.isArray(values))values=Object.values(values);
 if(!values){const ns=f.nodes.filter(n=>/^a\d|^t\d/.test(n.id));if(ns.length){const max=id==="probability-limit"?1:ns.length;ns.forEach((n,i)=>{const v=id==="probability-limit"?num(n.label):1/max;rect(g,80+i*(600/max),115,(600/max)-2,150,n.tone==="active"?"#ffe0a1":n.tone==="done"?"#cce9dc":"#eef5f8");text(g,80+(i+.5)*(600/max),190,n.label,20);});text(g,380,305,"Area represents probability mass, not outcome multiplicity.",20);return;}const balls=f.nodes.filter(n=>/^ball/.test(n.id));if(balls.length){balls.forEach((n,i)=>{dot(g,100+i*135,160,30,n.label==="R"?C.red:C.blue);text(g,100+i*135,168,n.label,24,"middle","white");if(n.tone==="active")g.append(E("circle",{cx:100+i*135,cy:160,r:40,fill:"none",stroke:C.amber,"stroke-width":4}));});return;}values=Object.values(f.metrics).map(num).filter(Number.isFinite).slice(0,5);}
 values=values.map(num).filter(Number.isFinite);const max=Math.max(1,...values),dx=Math.min(100,580/Math.max(1,values.length));axes(g,{x:85,y:290,w:580,h:220,xlabel:"category",ylabel:"mass / rate"});values.forEach((v,i)=>{rect(g,115+i*dx,290-200*v/max,dx*.6,200*v/max,i===p.index?"#f3cd78":"#7bb6c7","none");text(g,115+i*dx+dx*.3,280-200*v/max,Number(v.toFixed(4)),17);text(g,115+i*dx+dx*.3,320,i+1,16);});text(g,380,352,s.heading||"Categories follow the order stated in the exact checkpoint below.",17);
}
function plot(p,g,f){if(p.scene.id.startsWith("asym-"))return asymPlot(p,g,f);const id=p.scene.id,choose=s=>id==="growth-threshold"?[num(s.metrics.n),num(s.metrics["Exact ratio"])]:id==="encoding-length"?[num(s.metrics["Encoding length"]),num(s.metrics["Numeric parameter"])]:id==="loop-doubling"?[num(s.metrics.Visit),num(s.metrics.Value)]:id==="probability-limit"?[num(s.metrics["Included atoms"]),num(s.metrics["Included mass"])]:id==="bayes-sensitivity"?[num(s.snapshot.p),num(s.snapshot.posterior)]:id==="bayes-loss"?[num(s.snapshot.cfn),num(s.snapshot.threshold)]:id==="bayes-host"?[num(s.snapshot.q),num(s.snapshot.switch)]:[num(s.snapshot.n),num(s.snapshot.posterior??s.snapshot.independent??s.snapshot.predictive)];const all=p.scene.frames.map(choose),points=all.slice(0,p.index+1),maxX=Math.max(1,...all.map(a=>a[0])),maxY=Math.max(1,...all.map(a=>a[1]));const {x,y,w,h}=axes(g,{xlabel:/sensitivity|host/.test(id)?"p / q":id==="bayes-loss"?"false-negative cost":"step / size",ylabel:/growth/.test(id)?"ratio":/encoding/.test(id)?"value":"result"});const at=([a,b])=>[x+w*a/maxX,y-h*b/maxY];path(g,points.map((a,i)=>`${i?"L":"M"}${at(a)}`).join(" "),C.green,3);points.forEach((a,i)=>{const [X,Y]=at(a);dot(g,X,Y,5,i===points.length-1?C.amber:C.green);});if(id==="bayes-copy"){const copied=p.scene.frames.slice(0,p.index+1).map(r=>[num(r.snapshot.n),num(r.snapshot.duplicate)]);path(g,copied.map((a,i)=>`${i?"L":"M"}${at(a)}`).join(" "),C.blue,3);copied.forEach(a=>{const [X,Y]=at(a);rect(g,X-4,Y-4,8,8,C.blue);});text(g,490,48,"Green: independent; blue: copied",17);}text(g,380,345,`Saved samples joined for orientation; x 0–${maxX}, y 0–${Number(maxY.toFixed(3))}`,17);}
function tree(p,g,f,pos){if(p.scene.id==="recurrence-levels"){const n=+f.metrics.Nodes,depth=+f.metrics.Level;for(let d=0;d<=depth;d++){const count=2**d;for(let i=0;i<count;i++){const x=70+(i+.5)*620/count,y=45+70*d;if(d){const px=70+(Math.floor(i/2)+.5)*620/(count/2);path(g,`M${px} ${y-50}L${x} ${y-18}`,"#83a5b5");}dot(g,x,y,18,d===depth?C.amber:C.blue);text(g,x,y+6,8/count,18,"middle","white");}}text(g,380,340,`Level ${depth}: ${n} nodes × ${8/n} units = 8 units of work`,20);return;}
 graph(p,g,f,pos);
}
function gridEnumeration(p,g,f){const id=p.scene.id,s=f.snapshot||{};if(id.startsWith("number-question-"))return numberQuestion(p,g,f);if(id.startsWith("flow-question-"))return flowQuestion(p,g,f);if(id.startsWith("types-question-"))return typesQuestion(p,g,f);if(id.startsWith("matrices-question-"))return matricesQuestion(p,g,f);if(id.startsWith("vectors-question-"))return vectorsQuestion(p,g,f);if(id.startsWith("counting-question-"))return countingQuestion(p,g,f);if(id.startsWith("axioms-question-"))return axiomsQuestion(p,g,f);if(id.startsWith("loop-question-"))return loopQuestion(p,g,f);if(id==="loop-triangle"){for(let i=1;i<=5;i++)for(let j=1;j<=i;j++){rect(g,115+j*55,35+i*45,45,35,i===s.i&&j===s.j?"#ffe0a1":"#d1e8f1");text(g,137+j*55,59+i*45,`${i},${j}`,16);}text(g,565,150,`Body visits: ${s.count}`,24);return;}if(id==="powerset"){strip(g,170,115,[1,2,3],{cell:130,labels:false,title:"Independent inclusion decisions"});[1,2,3].forEach((v,i)=>text(g,235+i*130,225,s.subset.includes(v)?"include":"exclude",21,"middle",s.subset.includes(v)?C.green:C.red));text(g,380,310,`Mask ${s.mask.toString(2).padStart(3,"0")} → {${s.subset}}`,23);return;}if(id.startsWith("selection-")){const vs=s.outcomes;vs.forEach((v,i)=>{const x=90+(i%6)*112,y=100+Math.floor(i/6)*100;dot(g,x,y,32,String(v)===String(s.current)?C.amber:C.blue);text(g,x,y+7,`(${v})`,19,"middle","white");});text(g,380,330,`${vs.length} distinct admitted outcomes`,22);return;}if(id==="stars-bars"){f.nodes.forEach(n=>{if(n.label==="|")path(g,`M${n.x} 80V185`,C.amber,5);else dot(g,n.x,135,14,C.blue);});text(g,380,285,`Labeled group sizes: ${f.metrics["First group"]}, ${f.metrics["Second group"]}, ${f.metrics["Third group"]}`,24);return;}graph(p,g,f,new Map(f.nodes.map(n=>[n.id,n])));}
function kmap(p,g,f){const s=f.snapshot,id=p.scene.id;let n=s.n||4,on=s.on||[],dc=s.dc||[],cover=s.cover||[];if(id==="km-pos")on=s.zeroSet||[];if(s.rows)on=s.rows;if(id==="km-gray"){strip(g,170,140,["00","01","11","10"],{cell:100,active:s.step%4,labels:false,title:"Cyclic Gray order: one bit changes per neighbor"});return;}if(["km-chart","km-petrick","km-qm"].includes(id)){const patterns=s.patterns||Object.keys(s.owners||{});if(patterns.length){patterns.forEach((v,i)=>text(g,175+(i%4)*140,90+Math.floor(i/4)*65,v,25));text(g,380,320,`Exact tabulation stage: ${s.level??s.cost??s.candidate}`,21);return;}}
 const gray=[0,1,3,2],cells=n===3?2:4,x=200,y=85,size=50;text(g,300,37,n===3?"Rows: A; columns: BC":"Rows: AB; columns: CD",20);for(let i=0;i<cells;i++){text(g,x-28,y+i*size+32,n===3?i:gray[i].toString(2).padStart(2,"0"),18);for(let j=0;j<4;j++){if(!i)text(g,x+j*size+25,y-12,gray[j].toString(2).padStart(2,"0"),18);const v=(n===3?i:gray[i])*4+gray[j];rect(g,x+j*size,y+i*size,size,size,on.includes(v)?"#cce9dc":dc.includes(v)?"#ffe0a1":"#fff");text(g,x+j*size+25,y+i*size+20,v,13);text(g,x+j*size+25,y+i*size+42,on.includes(v)?1:dc.includes(v)?"X":0,22);}}
 const patterns=cover.map(v=>typeof v==="string"?v:v.pattern).filter(Boolean);patterns.forEach((pat,k)=>{for(let i=0;i<cells;i++)for(let j=0;j<4;j++){const v=(n===3?i:gray[i])*4+gray[j],bits=v.toString(2).padStart(n,"0");if([...pat].every((b,i)=>b==="-"||b===bits[i]))g.append(E("rect",{x:x+j*size+4+k*2,y:y+i*size+4+k*2,width:size-8-k*4,height:size-8-k*4,rx:9,fill:"none",stroke:[C.green,C.blue,C.amber,C.red][k%4],"stroke-width":3}));}});text(g,570,135,"Groups wrap across\nopposite edges.\nEach group represents\na Boolean cube.",18);text(g,380,335,patterns.length?`Selected cubes: ${patterns.join(", ")}`:s.pattern?`Cube under inspection: ${s.pattern}`:"Read decimal indices and Boolean obligations separately.",19);}
function waveform(p,g,f){const history=p.scene.frames,keys=p.scene.id==="km-hazard-time"?Object.keys(f.snapshot.signals):["x","notx","a","b","f"],times=history.map(a=>num(a.snapshot?.time??a.metrics.Time)),min=Math.min(...times),max=Math.max(...times),x=t=>120+(t-min)*560/(max-min||1);keys.forEach((key,i)=>{const y=62+i*52;const value=a=>a.snapshot?.signals?.[key]??a.snapshot?.[key]??(key==="f"?1:0);text(g,80,y+12,key,19);const points=[];history.slice(0,p.index+1).forEach((a,j)=>{if(j)points.push([x(times[j]),y+22-22*value(history[j-1])]);points.push([x(times[j]),y+22-22*value(a)]);});path(g,points.map((a,i)=>`${i?"L":"M"}${a}`).join(" "),key==="f"?C.green:C.blue,3);});const current=num(f.snapshot?.time??f.metrics.Time);path(g,`M${x(current)} 35V320`,C.amber,2,{"stroke-dasharray":"4 4"});times.forEach(t=>text(g,x(t),345,t,15));text(g,715,345,"time",15);}
// Conventional distinctive-shape logic symbols. Inputs connect at declared ports.
function gate(g,kind,x,y,name,value,w=66){const h=46,k=kind.replace(/NAND/,"AND").replace(/NOR/,"OR").replace(/XNOR/,"XOR"),inverted=["NAND","NOR","XNOR","NOT"].includes(kind);let d;if(k==="AND")d=`M${x} ${y-h/2}H${x+w/2}A${w/2} ${h/2} 0 0 1 ${x+w/2} ${y+h/2}H${x}Z`;else if(k==="OR"||k==="XOR")d=`M${x} ${y-h/2}Q${x+45} ${y-h/2} ${x+w} ${y}Q${x+45} ${y+h/2} ${x} ${y+h/2}Q${x+20} ${y} ${x} ${y-h/2}Z`;else if(k==="NOT")d=`M${x} ${y-h/2}L${x+w} ${y}L${x} ${y+h/2}Z`;else d=`M${x} ${y-h/2}h${w}v${h}h-${w}Z`;path(g,d,C.ink,2,{fill:"white"});if(k==="XOR")path(g,`M${x-7} ${y-h/2}Q${x+13} ${y} ${x-7} ${y+h/2}`);if(inverted)g.append(E("circle",{cx:x+w+5,cy:y,r:5,fill:"white",stroke:C.ink,"stroke-width":2}));text(g,x+w/2,y-36,name,17);if(!["AND","OR","XOR","NOT"].includes(k))text(g,x+w/2,y+5,k,14);const out=[x+w+(inverted?10:0),y];text(g,out[0]+12,y-13,value??"?",18,"start",value===null||value==="?"?C.ink:value?C.green:C.red);return {inputs:k==="NOT"?[[x,y]]:[[x,y-12],[x,y+12]],out};}
function circuit(p,g,f){const id=p.scene.id,s=f.snapshot||{},m=f.metrics;const row=s.row??0,a=(row>>2)&1,b=(row>>1)&1,c=row&1;let nets={},pins={};function input(name,value,x=45,y=80){text(g,x,y-13,`${name} = ${value}`,18,"start");pins[name]=[x,y];nets[name]=value;return name;}function G(name,kind,ins,x,y,override){const vals=ins.map(n=>nets[n]);let v=kind==="NOT"?1-vals[0]:kind==="AND"?+(vals.every(Boolean)):kind==="OR"?+(vals.some(Boolean)):kind==="XOR"?+(vals[0]!==vals[1]):kind==="NAND"?1-(+(vals.every(Boolean))):kind==="NOR"?1-(+(vals.some(Boolean))):0;if(override!==undefined)v=override;const q=gate(g,kind,x,y,name,v);ins.forEach((n,i)=>{const from=pins[n],to=q.inputs[Math.min(i,q.inputs.length-1)],bend=x-22-i*12;path(g,`M${from}H${bend}V${to[1]}H${to[0]}`,nets[n]?C.green:"#889da9",2.5);dot(g,from[0],from[1],3,nets[n]?C.green:C.ink);});nets[name]=v;pins[name]=q.out;return name;}function out(name,y){const from=pins[name];path(g,`M${from}H700`,nets[name]?C.green:C.red,3);text(g,710,y??from[1],name,19,"start");}
 if(id==="comb-dag"){input("A",1,40,55);input("B",1,40,95);input("C",0,40,220);input("D",1,40,265);input("E",0,410,45);input("H",1,410,315);G("p","AND",["A","B"],170,90);G("q","OR",["C","D"],170,245);G("r","AND",["p","q"],325,170);G("Y","OR",["r","E"],565,95);G("Z","XOR",["r","H"],565,260);out("Y");out("Z");return;}
 if(id==="nand-mapping"){input("A",+m.A,40,90);input("B",+m.B,40,250);G("n","NAND",["A","B"],250,170);G("Y","NAND",["n","n"],500,170);out("Y");return;}
 if(["static-hazard","hazard-consensus"].includes(id)){input("x",s.x??+p.scene.frames[p.index].metrics["Time"]<0,40,70);input("y",1,40,135);input("z",1,40,290);G("nx","NOT",["x"],130,220,s.notx??(p.index>=3?1:0));G("a","AND",["x","y"],295,90,s.a);G("b","AND",["nx","z"],295,250,s.b);G("F","OR",["a","b"],530,170,id==="hazard-consensus"?1:s.f);if(id==="hazard-consensus"){G("c","AND",["y","z"],330,320,1);const from=pins.c;path(g,`M${from}H485V185H530`,C.green,3);text(g,590,320,"Stable consensus path yz",17);}out("F");text(g,390,35,"Fixed y = z = 1; transport-delay events",17);return;}
 if(id==="comb-priority"){const r1=(s.row>>1)&1,r0=s.row&1;input("r1",r1,55,95);input("r0",r0,55,245);G("nr1","NOT",["r1"],185,210);G("g0","AND",["nr1","r0"],480,245);path(g,"M55 95H680",r1?C.green:C.ink,3);text(g,685,83,`g1 = ${s.g1}`,19);out("g0");return;}
 if(id==="comb-falsepath"){input("A",s.a,45,95);input("B",1,45,270);G("nA","NOT",["A"],180,190);G("q","AND",["A","nA"],375,125);G("Y","OR",["q","B"],570,220);out("Y");text(g,380,340,"Reconvergent A and ¬A never make q = 1 at stable inputs.",18);return;}
 input("A",a,45,55);input("B",b,45,150);input("C",c,45,295);
 if(id==="comb-nand"){G("p","NAND",["A","B"],240,100);G("q","NAND",["A","C"],240,255);G("Y","NAND",["p","q"],510,180);out("Y");return;}
 if(id==="comb-miter"){G("bc","OR",["B","C"],170,245);G("F","AND",["A","bc"],350,100);G("ab","AND",["A","B"],350,265);G("G","OR",["ab","C"],480,265);G("M","XOR",["F","G"],620,175);text(g,380,340,"A high miter output witnesses a functional mismatch.",18);return;}
 if(id==="comb-fault"){G("t","AND",["A","B"],245,100,s.fault?0:s.t);G("Y","OR",["t","C"],520,195);out("Y");text(g,380,340,s.fault?"Fault injected: internal t is stuck at 0":"Fault-free network",20);return;}
 if(id==="comb-interval"){G("p","AND",["A","B"],190,90);G("q","OR",["p","C"],350,175);input("D",1,400,290);G("Y","AND",["q","D"],570,230);out("Y");text(g,380,340,`Arrival interval at step ${s.step}: [${s.lo}, ${s.hi}]`,20);return;}
 if(id==="comb-cofactor"){g.replaceChildren();mux(g,s);return;}
 if(id==="comb-active-low"||id==="comb-rom"){g.replaceChildren();decoder(g,s,id);return;}
 if(id==="comb-feedback"||id==="comb-latch"){g.replaceChildren();feedback(g,s,id);return;}
 if(id==="comb-arrival"){g.replaceChildren();arrival(g,s);return;}
 throw Error(`Circuit ${id} requires a declared topology`);
}
function mux(g,s){const x=360,y=72,w=110,h=220;path(g,`M${x} ${y}L${x+w} ${y+35}V${y+h-35}L${x} ${y+h}Z`,C.ink,2,{fill:"#f4f9fb"});const names=["C","1","C","C"],sel=s.select;names.forEach((v,i)=>{const Y=105+i*47;path(g,`M155 ${Y}H360`,i===sel?C.amber:C.ink,i===sel?4:2);text(g,135,Y+5,v,23);text(g,380,Y+5,`D${i}`,18);});path(g,"M415 292V325H250",C.blue);text(g,220,330,`AB = ${sel.toString(2).padStart(2,"0")}`,20);path(g,"M470 182H665",C.green,3);text(g,670,188,"F",24);text(g,565,75,"4:1 multiplexer",21);text(g,570,260,`Selected cofactor: ${s.pair}`,19);}
function decoder(g,s,id){if(id==="comb-active-low"){rect(g,290,70,160,220,"white");text(g,370,118,"2:4 decoder",20);[["EN",s.en,220],["r1",s.r1,155],["r0",s.r0,190]].forEach(([n,v,y])=>{path(g,`M90 ${y}H290`,v?C.green:C.ink);text(g,140,y-15,`${n} = ${v}`,19);});s.outputs.forEach((v,i)=>{g.append(E("circle",{cx:455,cy:115+i*45,r:5,fill:"white",stroke:C.ink}));path(g,`M460 ${115+i*45}H640`,v?C.ink:C.green,3);text(g,680,121+i*45,`Y${i} = ${v}`,20);});text(g,380,335,"Bubbles denote active-low outputs; EN is active high.",19);return;}
 const row=s.row;rect(g,185,40,125,275,"#f6fafc");text(g,247,25,"3:8 decoder",19);for(let i=0;i<8;i++){const y=65+i*31;path(g,`M310 ${y}H580`,i===row?C.amber:"#cedce2",i===row?4:1);text(g,330,y-7,`m${i}`,14);if(i.toString(2).split("1").length%2===0)dot(g,455,y,4,C.blue);if(i.toString(2).split("1").length-1>=2)dot(g,550,y,4,C.green);}path(g,"M455 55V305",C.blue,2);path(g,"M550 55V305",C.green,2);text(g,455,340,`Parity = ${s.p}`,20);text(g,605,340,`Majority = ${s.m}`,20);text(g,83,175,`ABC\n${row.toString(2).padStart(3,"0")}`,24);arrow(g,130,170,185,170);}
function feedback(g,s,id){if(id==="comb-latch"){rect(g,320,95,125,140,"white");text(g,380,158,"D latch",22);path(g,"M95 135H320");text(g,150,118,`D = ${s.d}`,21);path(g,"M95 205H320");text(g,150,190,`EN = ${s.en}`,21);path(g,"M445 160H650",s.y?C.green:C.ink,3);text(g,665,166,`Q = ${s.y}`,22);text(g,380,300,s.en?"Transparent: Q follows D":"Hold: Q retains the previously established state",20);return;}
 const odd=s.case===0||String(s.case).includes("invert"),q=gate(g,odd?"NOT":"AND",340,175,"feedback",null);path(g,`M${q.out}H570V285H250V175H340`,C.blue,3);text(g,380,65,`Feedback constraint: ${s.case}`,22);text(g,380,335,`Stable solutions: ${JSON.stringify(s.solutions)}`,20);}
function arrival(g,s){const balanced=String(s.case).includes("balanced"),times=s.times;[70,130,235,295].forEach((y,i)=>{path(g,`M45 ${y}H180`);text(g,85,y-15,`x${i+1}`,18);});if(balanced){const a=gate(g,"AND",180,100,"pair 1",null),b=gate(g,"AND",180,265,"pair 2",null),o=gate(g,"AND",440,185,"root",null);path(g,`M${a.out}H390V173H440M${b.out}H390V197H440`);}else{const a=gate(g,"AND",180,100,"first",null),b=gate(g,"AND",330,190,"second",null),c=gate(g,"AND",480,280,"third",null);path(g,`M${a.out}H290V178H330M45 235H285V202H330M${b.out}H440V268H480M45 295H480`);}text(g,380,340,`${s.case}: arrival times ${times}`,20);}
function cmos(p,g,f){const a=+f.metrics.A,b=+f.metrics.B;path(g,"M190 40H565",C.ink,3);text(g,380,25,"VDD",23);const transistor=(name,x,y,pmos,on)=>{path(g,`M${x} ${y-23}V${y-12}M${x} ${y+12}V${y+23}M${x} ${y-12}h-8V${y+12}h8M${x-19} ${y-16}V${y+16}`,on?C.green:C.ink,3);path(g,`M${x-45} ${y}H${x-20}`);if(pmos)g.append(E("circle",{cx:x-24,cy:y,r:4,fill:"white",stroke:C.ink}));text(g,x+31,y+7,name,20,"start");text(g,x-47,y-14,name.slice(-1),18);};transistor("pA",240,98,true,!a);transistor("pB",500,98,true,!b);path(g,"M240 40V75M500 40V75M240 121V155H500V121M370 155V170",C.ink,2);dot(g,370,155,4);path(g,"M370 155H660",f.metrics.Output?C.green:C.red,3);text(g,650,142,`Y = ${f.metrics.Output}`,23);transistor("nA",370,193,false,!!a);transistor("nB",370,262,false,!!b);path(g,"M370 216V239M370 285V312M350 312H390M357 318H383M363 324H377",C.ink,2);text(g,175,245,"Parallel pMOS pull-up",18);text(g,575,245,"Series nMOS pull-down",18);text(g,380,353,`A = ${a}, B = ${b}: conducting channels are green`,19);}
function nativeFormula(g,f,x,y,w=650,h=60){const node=E("foreignObject",{x,y,width:w,height:h}),body=document.createElementNS("http://www.w3.org/1999/xhtml","div");body.style.cssText="font:18px 'STIX Two Math',serif;text-align:center;overflow:auto;padding:3px";const template=document.createElement("template");template.innerHTML=f.formulaHtml||"";const math=template.content.querySelector("math");if(math)body.append(math);else body.textContent=f.nodes.find(n=>n.id==="claim")?.label||f.nodes.filter(n=>n.id!=="token").map(n=>n.label).join("; ");node.append(body);g.append(node);}
function derivationExact(p,g,f){text(g,380,32,"Justified derivation",23);const history=p.scene.frames.slice(Math.max(0,p.index-3),p.index+1);history.forEach((r,i)=>{const y=60+i*70;nativeFormula(g,r,75,y,610,65);if(i)arrow(g,45,y-20,45,y+10,C.green);});}
function network(g,inputs,devices,outputs,known=null){const ports={},values={},used=[],boxes=devices.map(([name,kind,ins,x,y])=>[x,y-23,x+66+(["NAND","NOR","NOT","XNOR"].includes(kind)?10:0),y+23]);inputs.forEach(([name,value,x,y])=>{ports[name]=[x,y];values[name]=value;text(g,x,y-14,`${name} = ${value}`,17,"start");});devices.forEach(([name,kind,ins,x,y,forced])=>{const a=ins.map(k=>values[k]);if(a.some(v=>v===undefined))throw Error(`Undefined input at ${name}`);let v=kind==="NOT"?1-a[0]:kind==="BUF"?a[0]:kind==="AND"?+a.every(Boolean):kind==="OR"?+a.some(Boolean):kind==="NAND"?1-(+a.every(Boolean)):kind==="NOR"?1-(+a.some(Boolean)):kind==="XOR"?a.reduce((n,b)=>n^b,0):0;if(forced!==undefined)v=forced;const symbol=gate(g,kind,x,y,name,known&&!known.has(name)?"?":v);const inputPorts=ins.length>2?ins.map((_,i)=>[x,y-16+i*32/(ins.length-1)]):symbol.inputs;
 ins.forEach((source,i)=>{const from=ports[source],to=inputPorts[Math.min(i,inputPorts.length-1)],bend=x-18-i*14,color=known&&!known.has(source)&&!inputs.some(a=>a[0]===source)?"#c1cbd1":values[source]?C.green:"#8199a6";const wire=path(g,orthogonalRoute(from,to,boxes,used,source),color,2.5);wire.dataset.net=source;const coordinates=[...wire.getAttribute("d").matchAll(/[ML](-?[0-9.]+),(-?[0-9.]+)/g)].map(m=>[+m[1],+m[2]]);for(let k=1;k<coordinates.length;k++)used.push({a:coordinates[k-1],b:coordinates[k],net:source});if(["OR","NOR","XOR"].includes(kind))path(g,`M${to}h12`,color,2.5);dot(g,from[0],from[1],3,color);});ports[name]=symbol.out;values[name]=v;
 const proof=E("g",{"data-gate":name,"data-kind":kind,"data-inputs":ins.join(","),"data-value":v});g.append(proof);
 });outputs.forEach(name=>{const from=ports[name];path(g,`M${from}H710`,known&&!known.has(name)?"#c1cbd1":values[name]?C.green:C.red,3);text(g,744,from[1]-12,name,18,"end");});g.dataset.netValues=JSON.stringify(values);}
function circuitExact(p,g,f){const id=p.scene.id,s=f.snapshot||{},custom=id.startsWith("combin-custom-"),r=s.row??0;let a=r>>2&1,b=r>>1&1,c=r&1;
 if(custom){[a,b,c]=s.bits;const mode=s.mode;if(mode==="priority"){network(g,[["E",a,25,35],["R1",b,25,115],["R0",c,25,295]],[["not R1","NOT",["R1"],125,205],["G1","AND",["E","R1"],410,65],["allow R0","AND",["not R1","R0"],265,245],["G0","AND",["E","allow R0"],470,210],["request","OR",["R1","R0"],155,315],["V","AND",["E","request"],595,300]],["G1","G0","V"],new Set(["not R1","allow R0","request",...["G1","G0","V"].slice(0,p.index+1)]));text(g,380,350,"Reference network: six gates; V = E(R1 + R0).",18);return;}if(mode==="nand"){network(g,[["A",a,30,45],["B",b,30,140],["C",c,30,290]],[["p","NAND",["A","B"],240,95],["q","NAND",["A","C"],240,255],["Y","NAND",["p","q"],540,180]],["Y"],new Set(["p","q","Y"].slice(0,p.index+1)));return;}network(g,[["A",a,35,55],["B",b,35,105],["C",c,35,215],["D",s.bits[3],35,285]],[["p","AND",["A","B"],170,95],["q","OR",["C","D"],170,250],["Y","AND",["p","q"],405,125],["Z","OR",["p","C"],570,265]],["Y","Z"],new Set(["p","q","Y","Y","Z"].slice(0,p.index+1)));return;}
 if(id==="comb-nand"){network(g,[["A",a,30,45],["B",b,30,140],["C",c,30,290]],[["p","NAND",["A","B"],240,95],["q","NAND",["A","C"],240,255],["Y","NAND",["p","q"],540,180]],["Y"]);return;}
 if(id==="nand-mapping"){network(g,[["A",+f.metrics.A,40,85],["B",+f.metrics.B,40,260]],[["n","NAND",["A","B"],250,170],["Y","NAND",["n","n"],515,170]],["Y"]);return;}
 if(id==="comb-miter"){network(g,[["A",a,30,35],["B",b,30,155],["C",c,30,315]],[["B+C","OR",["B","C"],160,225],["F","AND",["A","B+C"],330,90],["AB","AND",["A","B"],325,275],["G","OR",["AB","C"],480,265],["M","XOR",["F","G"],620,165]],["M"]);return;}
 if(id==="comb-interval"){network(g,[["A",1,30,40],["B",1,30,115],["C",0,30,265],["D",1,415,315]],[["p","AND",["A","B"],180,90],["q","OR",["p","C"],350,200],["Y","AND",["q","D"],580,265]],["Y"]);text(g,400,35,`Step ${s.step}: arrival interval [${s.lo}, ${s.hi}]`,20);text(g,380,350,"Gate delay intervals: p (1,3), q (2,4), Y (1,2).",19);return;}
 if(id==="comb-priority"||id==="comb-active-low"){if(id==="comb-active-low"){a=s.en;b=s.r1;c=s.r0;}const ins=[["E",a,30,40],["R1",b,30,105],["R0",c,30,300]],dev=[["not R1","NOT",["R1"],155,220],["G1","AND",["E","R1"],390,80],["allow R0","AND",["not R1","R0"],305,265],["G0","AND",["E","allow R0"],485,225]];if(id==="comb-active-low"){ins[0]=["E_n",1-a,30,40];dev.unshift(["E","NOT",["E_n"],150,65]);dev.push(["G1_n","NOT",["G1"],610,80],["G0_n","NOT",["G0"],610,225]);network(g,ins,dev,["G1_n","G0_n"]);text(g,380,350,`Observed active-low enable E_n = ${1-a}; E = ¬E_n`,19);}else {network(g,ins,dev,["G1","G0"]);text(g,380,350,"Enable guards both grants; R1 suppresses R0.",19);}return;}
 if(id==="comb-falsepath"){network(g,[["A",s.a,45,75]],[["not A","NOT",["A"],190,240],["Y","AND",["A","not A"],465,175]],["Y"]);text(g,380,330,"Settled Y = A ∧ ¬A = 0; this is not a glitch-free timing claim.",18);return;}
 if(id==="comb-fault"){network(g,[["A",a,30,50],["B",b,30,115],["C",c,30,295]],[["AB","AND",["A","B"],190,90],["correct","OR",["AB","C"],415,105],["faulty AB","BUF",["AB"],345,250,0],["faulty","OR",["faulty AB","C"],585,260]],["correct","faulty"]);text(g,380,345,`Stuck-at-0 on AB: correct ${s.y}, faulty ${s.fault}; detection ${s.y^s.fault}`,19);return;}
 if(id==="comb-feedback"){const kind=s.case===0?"BUF":s.case===1?"NOT":"AND",q=gate(g,kind,330,175,"Q",null);path(g,`M${q.out}H535V280H230V${s.case===2?163:175}H330`,C.blue,3);if(s.case===2){path(g,"M100 205H270V187H330");text(g,115,190,"0",23);}text(g,380,65,["Q = Q","Q = ¬Q","Q = Q ∧ 0"][s.case],24);text(g,380,335,`Boolean fixed points: {${s.solutions.join(", ")}}`,21);return;}
 if(id==="comb-arrival"){arrival(g,{...s,case:s.case===0?"balanced":s.case===1?"chain":"early subtree"});text(g,80,45,"Early inputs: 0",16);text(g,115,320,"Late input x4: 10",16);return;}
 if(id==="static-hazard"||id==="hazard-consensus"){const old=[[-1,1,0,1,0,1],[0,0,0,1,0,1],[1,0,0,0,0,1],[2,0,1,0,0,0],[3,0,1,0,1,0],[4,0,1,0,1,1]][p.index],x=s.x??old[1],nx=s.notx??old[2],aa=s.a??old[3],bb=s.b??old[4],ff=s.f??old[5];const dev=[["not x","NOT",["x"],150,205,nx],["xy","AND",["x","y"],300,95,aa],["not x z","AND",["not x","z"],300,255,bb]];if(id==="hazard-consensus")dev.push(["yz","AND",["y","z"],400,320,1]);dev.push(["F","OR",["xy","not x z",...(id==="hazard-consensus"?["yz"]:[])],575,175,id==="hazard-consensus"?1:ff]);network(g,[["x",x,30,55],["y",1,30,125],["z",1,30,290]],dev,["F"]);text(g,420,30,`Time ${s.time??old[0]}; transport-delay state`,18);return;}
 if(id==="comb-dag"){network(g,[["A",1,30,55],["B",1,30,105],["C",0,30,215],["D",1,30,275],["E",0,405,40],["H",1,405,320]],[["p","AND",["A","B"],170,95],["q","OR",["C","D"],170,245],["r","AND",["p","q"],330,175],["Y","OR",["r","E"],570,100],["Z","XOR",["r","H"],570,260]],["Y","Z"],new Set(["p","q","r","Y","Z"].slice(0,s.step)));return;}
 circuit(p,g,f);
}
function geometryExact(p,g,f,pos){const id=p.scene.id,s=f.snapshot||{};
 if(id==="vector-norms"){const ox=130,oy=290,k=45;axes(g,{x:ox,y:oy,w:320,h:235});arrow(g,ox,oy,ox+3*k,oy-4*k);path(g,`M${ox} ${oy}h${3*k}v${-4*k}`,C.amber,3);text(g,560,110,f.metrics.Norm,23);text(g,560,165,`Value = ${f.metrics.Result}`,25);text(g,560,230,"Fixed vector (3,4)",22);return;}
 if(id==="integer-family"){const pts=p.scene.frames.map(r=>[num(r.nodes.find(n=>n.id==="x").label.split("=")[1]),num(r.nodes.find(n=>n.id==="y").label.split("=")[1])]),ox=355,oy=220,k=27;arrow(g,55,oy,700,oy,C.ink);arrow(g,ox,330,ox,35,C.ink);path(g,pts.map((a,i)=>`${i?"L":"M"}${ox+k*a[0]} ${oy-k*a[1]}`).join(" "),C.blue);pts.forEach((a,i)=>{dot(g,ox+k*a[0],oy-k*a[1],i===p.index?8:4,i===p.index?C.amber:C.blue);});text(g,380,350,"Integer points on 4x + 6y = 10; x increases by 3 as y decreases by 2.",18);return;}
 const rank=id.startsWith("rank-"),gauss=id==="gauss-geometry",ox=rank?(s.kind==="rank-map"?570:180):gauss?300:(p.scene.axes?.cx??300),oy=rank?190:gauss?235:(p.scene.axes?.cy??245),k=rank?55:gauss?50:(p.scene.axes?.scale??65);
 for(let x=ox%k;x<725;x+=k)path(g,`M${x} 30V315`,"#e5edf1",1);for(let y=oy%k;y<316;y+=k)path(g,`M35 ${y}H725`,"#e5edf1",1);arrow(g,35,oy,725,oy,C.ink);arrow(g,ox,315,ox,25,C.ink);text(g,738,oy+6,"x",18);text(g,ox+15,22,"y",18);
 const transform=a=>rank?{x:a.x,y:190+(a.y-190)*55/45}:gauss?{x:300+(a.x-300)*50/65,y:235+(a.y-235)*50/43}:a;
 for(const e of f.edges||[]){const a=pos.get(e.from),b=pos.get(e.to);if(!a||!b)continue;const A=transform(a),B=transform(b);if(e.directed)arrow(g,A.x,A.y,B.x,B.y,e.tone==="active"?C.amber:C.blue);else path(g,`M${A.x} ${A.y}L${B.x} ${B.y}`,e.tone==="active"?C.amber:C.blue,3);}
 f.nodes.forEach(n=>{if(n.kind!=="point"){text(g,n.x,n.y,n.label,18);return;}const a=transform(pos.get(n.id)||n);dot(g,a.x,a.y,n.id==="solution"||n.id==="input"?7:4,tone(n));if(n.label)text(g,a.x+(n.labelDx||0),a.y+(n.labelDy||-16),n.label,17);});
 if(rank&&s.kind==="rank-map")text(g,280,160,`Image of ${s.inputs.length} inputs`,21);
}
function arrayExact(p,g,f,pos){const s=f.snapshot||{},id=p.scene.id;
 if(id==="model-merge-exact"){
  text(g,380,38,s.stage,21);
  strip(g,90,100,s.left,{cell:58,active:s.finished?-1:s.i,title:"Left input: fronts before this event",tones:s.left.map((_,i)=>i<s.i?"#8d9fac":C.ink)});
  strip(g,425,100,s.right,{cell:58,active:s.finished?-1:s.j,title:"Right input: fronts before this event",tones:s.right.map((_,i)=>i<s.j?"#8d9fac":C.ink)});
  strip(g,90,250,s.output,{cell:65,labels:false,title:s.finished?"Complete merge output, including the copied tail":"Output after the highlighted comparison",active:s.finished?-1:s.output.length-1});
  text(g,380,215,s.finished?"No additional key comparison for tail copies":`Compare ${s.left[s.i]} with ${s.right[s.j]}; emit ${s.chosen}`,19);
  return;
 }
 if(id==="arr-ring"){const r=112,cx=235,cy=185;for(let i=0;i<7;i++){const a=-Math.PI/2+i*2*Math.PI/7,x=cx+r*Math.cos(a),y=cy+r*Math.sin(a);dot(g,x,y,23,i===s.physical?C.amber:C.blue);text(g,x,y+7,i,20,"middle","white");}text(g,540,140,`Logical offset = ${s.t}`,22);text(g,540,190,`Physical slot = ${s.physical}`,22);text(g,540,255,"(head 5 + offset) mod 7",22);return;}
 if(id==="arr-transpose"){const source=[[0,1,2],[3,4,5]],dest=[s.target.slice(0,2),s.target.slice(2,4),s.target.slice(4,6)];matrix(g,source,80,95,"Source 2 × 3",[[s.i,s.j]]);matrix(g,dest,480,95,"Transpose 3 × 2",[[s.j,s.i]]);arrow(g,300,160,440,160);text(g,380,315,`${s.phase}: source offset ${s.source} → destination offset ${s.destination}`,20);return;}
 if(id==="arr-packed"){const M=Array.from({length:3},(_,i)=>Array.from({length:3},(_,j)=>j<=i?i*(i+1)/2+j:"—"));matrix(g,M,125,85,"Three-row packed lower triangle",[[s.i,s.j]]);text(g,550,170,`Offset ${s.offset}`,24);return;}
 if(id==="arr-sharing"||id==="fn-sharing"){const old=s.row||(typeof s.old==="string"?JSON.parse(s.old):s.old),newObject=typeof s.new==="string"&&s.new.startsWith("[")?JSON.parse(s.new):s.new;rect(g,70,65,230,52,"#eef6fb");rect(g,450,65,240,52,"#f1f8ef");text(g,185,98,"Caller reference",21);text(g,570,98,"Copied/local reference",21);strip(g,150,225,old,{cell:70,title:"Original inner object"});arrow(g,185,117,185,225,C.blue);if(id==="fn-sharing"&&s.stage>=2){strip(g,490,225,newObject,{cell:70,title:"New object"});arrow(g,570,117,525,225,C.green);}else arrow(g,570,117,220,225,C.green);text(g,380,330,"Reference identity determines which mutation is shared.",19);return;}
 if(id==="arr-growth"){strip(g,60,75,s.oldLive?[2,4,6]:["released","released","released"],{cell:s.oldLive?100:130,title:"Old allocation"});strip(g,60,225,s.new,{cell:100,title:"New allocation: capacity 6; logical length 3"});if(s.step>0&&s.step<4)arrow(g,110+(s.step-1)*100,145,110+(s.step-1)*100,220,C.amber);return;}
 if(id==="arr-prefix"){strip(g,60,85,s.input,{cell:90,title:"Input cells"});strip(g,60,225,s.prefix,{cell:90,active:s.index,title:"Prefix boundaries: one more than input length"});return;}
 arrayMemory(p,g,f,pos);
}








/* NUMBER QUESTION RENDERER */
function numberQuestion(p,g,f){
 const s=f.snapshot,head=v=>text(g,380,30,v,20),formula=()=>vectorNative(g,f.formulaHtml,25,283,710,70);
 const box=(x,y,w,h,v,fill='#eef5f8',size=18)=>{rect(g,x,y,w,h,fill,'#abc4cf');text(g,x+w/2,y+h/2+6,v,size);};
 if(s.kind==='adder'){
  head(`${s.w}-bit ripple addition: bit 0 at the left`);const dx=650/s.w,cw=Math.min(70,dx-38);
  s.rows.forEach(([i,a,b,cin,r,cout],j)=>{const x=52+j*dx,done=j<s.completed;box(x,75,cw,32,a,'#edf4f8',18);box(x,115,cw,32,b,'#f3f0e6',18);rect(g,x,162,cw,48,done?'#dceee4':'#f1f4f6','#aac3cf');text(g,x+cw/2,191,'FA'+i,16);path(g,`M${x+cw/3} 107H${x-8}V154H${x+cw/3}V162M${x+2*cw/3} 147V162`,C.blue,1.3);path(g,`M${x+cw/2} 210V225`,done?C.green:'#b5c6ce',1.4);box(x,225,cw,37,done?r:'·',done?'#dceee4':'#f1f4f6',19);
   if(j<s.w-1){arrow(g,x+cw,186,x+dx,186,done?C.green:'#b5c6ce');text(g,x+cw+(dx-cw)/2,150,done?cout:'·',15);}
  });
  text(g,380,60,s.completed===s.w?`stored ${s.stored}; signed ${s.signedResult}; carry ${s.carry}; overflow ${s.overflow}`:'A row above B; FA has two bit inputs and the routed incoming carry.',13);
  text(g,31,190,'0',15);arrow(g,34,186,52,186,C.blue);text(g,380,279,'Dots mark result positions whose local operation is still pending.',13);formula();return;
 }
 if(s.kind==='quant'){
  head('Exact target → raw index → neighbor decision → decoded output');
  box(62,76,240,48,'target '+s.target);box(460,76,240,48,'unit '+s.unit);arrow(g,302,100,460,100,C.blue);
  box(245,151,270,43,s.stage>=1?'raw target '+s.scaled:'raw target: pending');
  if(s.stage>=2){box(65,219,220,43,`${s.low} → ${s.lowReal}`,s.stage===3&&s.chosen===s.low?'#dceee4':'#edf5f8');box(475,219,220,43,`${s.high} → ${s.highReal}`,s.stage===3&&s.chosen===s.high?'#dceee4':'#edf5f8');arrow(g,290,194,190,219,C.blue);arrow(g,470,194,580,219,C.blue);}
  else text(g,380,239,'Neighbors are not yet compared.',17);formula();return;
 }
 if(s.kind==='round-tree'){
  head('Two actual decimal addition trees; round at each node');
  ['left','right'].forEach((key,k)=>{const x=42+k*375;box(x,58,330,35,k?'a + (b + c)':'(a + b) + c');s[key].forEach(([op,exact,rounded],i)=>{const y=120+i*77;box(x,y,330,50,s.stage>i?`${op}: ${exact} → ${rounded}`:'next addition pending',s.stage>i?'#dceee4':'#f0f4f6',16);if(i===0)arrow(g,x+165,y+50,x+165,y+77,C.blue);});});formula();return;
 }
 if(s.kind==='fields'){
  head('Declared normal fields: each has its own decoder');box(35,65,105,50,'sign '+s.sign);box(177,65,230,50,'exponent '+s.exponent);box(445,65,280,50,'fraction '+s.fraction);
  box(177,172,230,47,s.stage>=1?`${s.E} − ${s.bias} = ${s.e}`:'bias step pending',s.stage>=1?'#dceee4':'#edf5f8');box(445,172,280,47,s.stage>=2?'1.1010₂ = '+s.m:'leading bit pending',s.stage>=2?'#dceee4':'#edf5f8');arrow(g,292,115,292,172,C.blue);arrow(g,585,115,585,172,C.blue);formula();return;
 }
 if(s.kind==='extension'){
  head('Original cells and added sign cells remain distinguishable');bits(g,s.old,175,83,50,s.old.length,'original six-bit word');
  if(s.stage>=1){bits(g,s.new,125,195,50,s.new.length,'extended eight-bit word');rect(g,125,185,98,62,'none',C.amber);arrow(g,200,125,150,195,C.amber);}
  else text(g,380,220,'New sign positions have not been introduced.',18);formula();return;
 }
 if(s.kind==='denominator'){
  head('Reduced denominator determines exact binary termination');numberTable(g,s.rows.slice(0,s.stage===0?0:4),['fraction','factorization','decision'],50,85,660,180,s.stage===2?2:-1);if(s.stage===0)text(g,380,179,'All four reduced fractions are inputs; factorization follows.',18);formula();return;
 }
 if(s.kind==='bytes'){
  head('Increasing byte addresses run left to right');text(g,380,63,'Hex values 12,34,56,78 keep their internal bit order.',17);const row=(values,y,label)=>{text(g,105,y+29,label,17);values.forEach((v,i)=>{const x=225+i*105,active=s.stage===3||s.stage===1&&label==='little'&&i===0||s.stage===2&&label==='big'&&i===0;box(x,y,75,47,v,active?'#dceee4':'#edf5f8');text(g,x+37,y-10,'addr+'+i,15);});};row(s.le,106,'little');row(s.be,207,'big');formula();return;
 }
 if(s.kind==='bias'){
  head('Normal stored field and complete bias subtraction');box(55,90,210,55,'E = '+s.stored);box(290,90,210,55,s.stage>=1?'K = '+s.bias:'bias pending');box(535,90,180,55,s.stage===2?'e = '+s.decoded:'decode pending',s.stage===2?'#dceee4':'#edf5f8');arrow(g,265,118,290,118,C.blue);arrow(g,500,118,535,118,C.blue);text(g,380,220,'Stored exponent00010 is normal in the declared five-bit field.',17);formula();return;
 }
 if(s.kind==='scale'){
  head('Integer code and real unit are separate objects');box(250,75,260,50,'stored integer97');
  if(s.stage>=1){box(75,170,225,50,'integer part:3 × 32');box(455,170,225,50,'remainder:1');arrow(g,280,125,190,170,C.blue);arrow(g,480,125,565,170,C.green);}else text(g,380,215,'The unit1/32 is external format metadata.',18);formula();return;
 }
 if(s.kind==='decode'){
  head('One unchanged word with two mathematical decoders');bits(g,s.word,200,84,64,5,'the original five bits');box(85,197,250,47,s.stage>=1?'unsigned29':'unsigned: pending');box(420,197,250,47,s.stage>=2?'signed−3':'signed: pending',s.stage>=2?'#dceee4':'#edf5f8');formula();return;
 }
 if(s.kind==='zeros'){
  head('Two distinct words, one numerical zero');bits(g,s.positive,75,95,45,5,'top-zero branch');bits(g,s.negative,440,95,45,5,'top-one branch');box(85,205,210,42,s.stage>=1?'0 → 0':'decode pending');box(450,205,210,42,s.stage>=2?'31 − 31 → 0':'decode pending',s.stage>=2?'#dceee4':'#edf5f8');formula();return;
 }
 if(s.kind==='fraction-sum'){
  head('Exactly five retained positions; no unstated infinite tail');for(let i=0;i<5;i++){const x=60+i*138;box(x,86,105,58,i<s.count?'1':'pending',i<s.count?'#dceee4':'#eef4f7',18);text(g,x+52,175,'weight 1/'+(2**(i+1)),17);}text(g,380,240,'included '+s.count+' of 5 positions; remaining-to-one '+(s.denominator-s.numerator)+'/'+s.denominator,18);formula();return;
 }
 if(s.kind==='spacing'){
  head('Local precision grid and unequal boundary-side gaps');const x=[70,155,260,365,465,570,675];s.values.forEach((v,i)=>{dot(g,x[i],154,7,i===1?C.amber:C.blue);text(g,x[i],190,v,19);if(i)arrow(g,x[i-1]+7,154,x[i]-7,154,C.blue);});text(g,207,112,'gap2',17);if(s.stage>=2){text(g,110,231,'previous gap1',17);text(g,625,231,'next-binade gap4',17);}text(g,420,110,'…',19);formula();return;
 }
 if(s.kind==='hex'){
  head('Five groups retain the declared format width');s.groups.forEach((v,i)=>{const x=42+i*142;box(x,75,120,40,'hex '+i);if(s.stage>=1){bits(g,v,x,175,29,4,'four bits');arrow(g,x+60,115,x+60,175,C.blue);}});formula();return;
 }
 if(s.kind==='division'||s.kind==='fraction-conversion'){
  head(s.kind==='division'?'Quotient decreases; remainders need reversal':'Residual fraction advances; digits keep extraction order');numberTable(g,s.rows,s.kind==='division'?['old quotient','new quotient','remainder']:['twice residual','emitted digit','new residual'],50,77,660,173);text(g,380,268,(s.kind==='division'?'low-to-high extracted digits: ':'fraction digits: ')+(s.bits||'none yet'),17);formula();return;
 }
 if(s.kind==='multi-decode'){
  head('The decoder supplies signedness and scale');bits(g,s.word,175,61,48,8,'unchanged word 11101001');numberTable(g,s.stage?s.rows.slice(0,s.stage===2?5:4):[],['declared decoder','exact value'],150,140,460,132);formula();return;
 }
 if(s.kind==='bcd'){
  head('Digit subtotals use decimal carry from the previous digit');numberTable(g,s.rows.slice(0,Math.max(0,s.stage)),['place','a','b','cin','sum','+6','digit','cout'],25,90,710,120);if(s.stage===3){box(175,230,410,40,'0001 0111 0101 → decimal 175','#dceee4');}formula();return;
 }
 if(s.kind==='gray'){
  head('Decode the label before arithmetic, then re-encode');box(50,77,300,47,'input Gray '+s.gray);box(415,77,300,47,s.stage>=1?'binary '+s.binary+' =19':'prefix XOR pending');arrow(g,350,100,415,100,C.blue);box(50,200,300,47,s.stage>=2?'incremented binary '+s.newBinary:'index increment pending');box(415,200,300,47,s.stage>=3?'output Gray '+s.newGray:'Gray encoding pending',s.stage>=3?'#dceee4':'#eef5f8');arrow(g,565,124,200,200,C.blue);arrow(g,350,224,415,224,C.green);formula();return;
 }
 if(s.kind==='hamming'){
  head('Position order 1→7 and syndrome order high→low');const word=s.stage===2||s.stage===3?s.received:s.word;for(let i=0;i<7;i++){const x=66+i*89,isParity=[0,1,3].includes(i);text(g,x+30,75,'pos '+(i+1),16);box(x,93,61,45,s.stage===0&&isParity?'p':word[i],(s.stage===2||s.stage===3)&&i===5?'#f7e5c8':isParity?'#e5eff7':'#dceee4',20);}
  if(s.stage>=3){s.checks.forEach((v,i)=>{box(55+i*239,191,222,55,'check '+(1<<i)+': '+v.join(','),'#eef5f8',16);text(g,165+i*239,270,'XOR = '+s.syndrome[i],17);});}formula();return;
 }
 if(s.kind==='secded'){
  head('Two actual errors are not a single-error correction request');const v=s.stage===0?'00000000':s.stage===3?s.naive:s.received;bits(g,v,124,85,63,8,s.stage===3?'counterfactual wrong correction':'actual extended word');box(70,214,270,48,s.stage===3?'counterfactual S0, P1':s.stage>=2?'syndrome3, parity0':'checks pending');box(405,214,290,48,s.stage===3?'wrong data; original decision refuses':s.stage>=2?'detect; do not correct':'action pending','#dceee4',s.stage===3?14:17);formula();return;
 }
 throw Error('Unknown number representation mechanism: '+s.kind);
 function bits(g,word,x,y,dx,n,label){text(g,x+dx*n/2,y-14,label,16);[...word].forEach((b,i)=>box(x+i*dx,y,dx-4,45,b,'#eef5f8',19));}
}
function numberTable(g,rows,headings,x,y,w,h,activeIndex=rows.length-1){
 const node=E('foreignObject',{x,y,width:w,height:h}),div=document.createElementNS('http://www.w3.org/1999/xhtml','div');div.style.cssText="font:14px 'Source Sans 3',sans-serif;width:100%;height:100%;overflow:auto";
 const table=document.createElement('table');table.style.cssText='display:table;width:100%;table-layout:fixed;border-collapse:collapse;margin:0;font-size:14px;line-height:1.25';
 const tr=document.createElement('tr');headings.forEach(v=>{const c=document.createElement('th');c.textContent=v;c.style.cssText='padding:3px 7px;text-align:left;font-size:14px;line-height:1.25;background:#edf4f8';tr.append(c);});table.append(tr);
 rows.forEach((r,i)=>{const tr=document.createElement('tr');r.forEach(v=>{const c=document.createElement('td');c.textContent=v;c.style.cssText='padding:1px 7px;text-align:left;font-size:14px;line-height:1.25;border-bottom:2px solid white;background:'+(i===activeIndex?'#e0eee7':'#f5f8fa');tr.append(c);});table.append(tr);});div.append(table);node.append(div);g.append(node);
}

/* END NUMBER QUESTION RENDERER */
function flowQuestion(p,g,f){
 const s=f.snapshot,head=v=>text(g,380,30,v,20),formula=()=>vectorNative(g,f.formulaHtml,25,283,710,70);
 const box=(x,y,w,h,value,fill='#f3f8fa',size=18)=>{rect(g,x,y,w,h,fill,'#afc5cf');text(g,x+w/2,y+h/2+6,value,size);};
 if(s.kind==='triples'){
  head('Actual middle index j: j choices × (16−j) choices');
  if(s.stage===2){box(75,105,250,60,'weak triple (2,2,4)');box(450,105,250,60,'shifted triple (2,3,6)','#dceee4');arrow(g,325,135,450,135,C.blue);text(g,380,230,'The inverse subtracts 0, 1, 2 and reconstructs every weak triple.',17);formula();return;}
  if(s.stage===3){box(60,108,170,70,'initial: 10');box(295,108,170,70,'writes: 680');box(530,108,170,70,'final: 690','#dceee4');arrow(g,230,143,295,143,C.blue);arrow(g,465,143,530,143,C.green);text(g,380,230,'Count 680 increments, then add the separate initial value 10.',17);formula();return;}
  s.rows.forEach(([j,a,b,n],i)=>{const x=45+i*44;rect(g,x,215-n*1.8,32,n*1.8,'#dceae2','#b0c6be');text(g,x+16,245,j,16);if(s.stage>=1)text(g,x+16,198-n*1.8,n,14);});
  text(g,380,65,s.stage===0?'i≤j≤k≤15: bounds depend on the current middle index.':s.stage===1?'Each bar counts one disjoint fixed-j group.':s.stage===2?'Shifted triples(i,j+1,k+2) choose3of17.':'680increments plus initial10 gives690.',17);formula();return;
 }
 if(s.kind==='split'){
  head('Greater block, pivot, smaller block: actual element identities');
  box(250,55,260,43,'input[5,1,4,2,3]');box(65,145,210,45,s.stage>=1?'R output[5,4]':'R input[5,4]',s.stage>=1?'#dceee4':'#f3f8fa');box(330,145,100,45,'pivot3','#f7eddc');box(485,145,210,45,s.stage>=2?'L output[2,1]':'L input[1,2]',s.stage>=2?'#dceee4':'#f3f8fa');
  arrow(g,295,98,175,145,C.blue);arrow(g,380,98,380,145,C.amber);arrow(g,465,98,590,145,C.green);
  if(s.stage===3){box(215,232,330,40,'join[5,4,3,2,1]','#dceee4');arrow(g,170,190,245,232,C.blue);arrow(g,380,190,380,232,C.amber);arrow(g,590,190,515,232,C.green);}formula();return;
 }
 if(s.kind==='copy'){
  head(s.variant?'Original alternatives: output offset and stride':'Actual array source read and destination write');const dx=48,start=70;
  text(g,380,66,`source has ${s.sourceSize} cells; read only if its index is nonnegative`,17);
  for(let i=0;i<s.sourceSize;i++){const active=i===s.source;rect(g,start+i*dx,86,dx-4,45,active?'#f7e3bd':'#edf4f8','#b0c5cd');text(g,start+i*dx+(dx-4)/2,115,`v${i}`,17);}
  const size=Math.max(4,s.dest.length?s.offset+s.stride*(s.dest.length-1)+1:4);for(let i=0;i<size;i++){const t=(i-s.offset)/s.stride,v=Number.isInteger(t)&&t>=0&&t<s.dest.length?'v'+s.dest[t]:'·';box(start+i*dx,188,dx-4,45,v,v==='·'?'#f1eee6':'#dceee4',17);}
  text(g,380,165,'Destination dots are unwritten, not numeric zero.',17);
  if(s.negative)text(g,380,258,'Negative guard returns: no source read occurs.',17);
  else if(s.dest.length&&!s.variant){const src=start+s.source*dx+22,dst=start+(s.dest.length-1)*dx+22;arrow(g,src,131,dst,188,C.blue);}
  formula();return;
 }
 if(s.kind==='dangling'){
  head('Statement ownership and the actual outer-false path');box(275,55,210,45,'outer if(a)','#e5f0f7');box(70,145,230,45,s.stage?'inner not evaluated':'inner if(b)');box(505,145,210,45,s.stage===2?'final x=0':'outer false: skip','#dceee4');
  arrow(g,300,100,210,145,s.stage?'#b8cad2':C.blue);arrow(g,460,100,610,145,s.stage?C.green:'#b8cad2');box(35,232,125,40,'x=1');box(210,232,125,40,'else x=2');arrow(g,150,190,98,232,'#b8cad2');arrow(g,220,190,270,232,'#b8cad2');formula();return;
 }
 if(s.kind==='trace'){
  const guard=s.values[0][0]==='i';head(guard?'Actual short-circuit guard and restoration checkpoints':'Actual loop checkpoint and separate event counts');box(210,53,340,40,'phase: '+s.phase,s.exit?'#dceee4':'#e5f0f7',17);
  const headings=guard?['i','j','operation']:['index','action','sum'];flowHistoryTable(g,s.rows,headings);
  s.values.forEach(([label,value],i)=>box(490,115+i*53,240,39,`${label}: ${value}`,'#f3f8fa',16));formula();return;
 }
 if(s.kind==='switch'){
  head('One dispatch jump, then sequential fallthrough');const ys=[57,110,163,216],labels=['case1: x+=1','case2: x+=2','case3: x+=4; break','default: x=9'];ys.forEach((y,i)=>box(65,y,260,40,labels[i],i===1&&s.stage===0||i===2&&s.stage>=1&&s.stage<=2?'#dceee4':'#f4f7f9',17));
  box(495,95,220,43,'control value2');box(495,187,220,45,'current x='+s.x,s.stage===3?'#dceee4':'#e5f0f7');arrow(g,495,116,325,130,C.blue);if(s.stage>=1)arrow(g,195,150,195,163,C.green);if(s.stage===3)arrow(g,325,183,495,208,C.amber);text(g,550,260,'Default is not reached.',17);formula();return;
 }
 if(s.kind==='orbit'){
  head(s.extension?'Counterfactual full-cycle extension after termination':`Actual modulo256 orbit: target ${s.target}, update ${s.t}`);const center=[230,163],radius=95;
  for(let t=0;t<128;t++){const a=-Math.PI/2+2*Math.PI*t/128;dot(g,center[0]+radius*Math.cos(a),center[1]+radius*Math.sin(a),t===s.t%128?6:2,t===s.t%128?C.amber:'#a8c5d0');}
  text(g,230,150,'128 reachable',17);text(g,230,177,'even residues',17);box(425,80,285,48,'actual residue: '+s.value,s.hit?'#dceee4':'#edf5f8');box(425,158,285,48,s.target===1?'odd target: unreachable':s.hit?'target 64 reached':'first target 64 hit: 96',s.hit?'#dceee4':'#f8efdf',17);text(g,555,250,'Position represents update order.',17);formula();return;
 }
 if(s.kind==='postfix'){
  head('Guard old value, stored new value and body counter');const cols=[95,270,430,590],heads=['old x','stored x','guard result','c'];cols.forEach((x,i)=>text(g,x,90,heads[i],17));
  s.rows.forEach((row,i)=>{const y=130+i*34;rect(g,45,y-22,670,30,i===s.rows.length-1?'#dceee4':'#f4f8fa','none');row.forEach((v,j)=>text(g,cols[j],y,v,18));});if(s.stage<0)text(g,380,190,'No guard or body has executed yet.',19);formula();return;
 }
 if(s.kind==='ranking'){
  head('Actual13trajectory: n strictly decreases on both branches');s.sequence.forEach((v,i)=>{const x=50+i*95;box(x,93,70,48,v,i===s.stage?'#dceee4':'#f2f7fa',20);if(i<6)arrow(g,x+70,117,x+95,117,C.blue);});box(160,192,440,45,`current n=${s.n}; bit length=${s.bitLength}; ones=${s.pop}`,'#edf5f8',18);formula();return;
 }
 if(s.kind==='nested'){
  head('The inner break leaves the outer frame active');rect(g,70,65,630,195,'#f5f9fa','#a7c4cf');text(g,385,98,s.i===null?'outer index: not initialized yet':'outer loop: i='+s.i,18);rect(g,120,130,370,68,s.broke?'#f7e9d2':'#e4eff6','#a6c1cc');text(g,305,169,s.j===null?'inner index: not initialized yet':'inner loop: j='+s.j,18);box(525,145,145,50,'counter '+s.total,'#dceee4',17);
  if(s.broke){path(g,'M490 164H510V230H380',C.amber,1.8);text(g,290,247,'after inner loop; outer remains active',16);}formula();return;
 }
 if(s.kind==='threshold'){
  head('Positive prefix sums and the first qualifying body');const scale=v=>250-v*9;path(g,'M80 250H650M80 250V70','#9fb8c3',1.2);s.history.forEach((v,i)=>{const x=95+i*100;dot(g,x,scale(v),i===s.i?6:4,i===s.i?C.amber:C.blue);text(g,x,scale(v)-15,v,17);if(i)path(g,`M${95+(i-1)*100} ${scale(s.history[i-1])}L${x} ${scale(v)}`,C.blue,1.5);});path(g,'M80 115H655',C.green,1.5);text(g,650,100,'H=15',16);formula();return;
 }
 if(s.kind==='binary'){
  head('Depth-three representative: whole tree versus one active path');
  for(let d=0;d<=s.stage;d++){const nodes=2**d;for(let j=0;j<nodes;j++){const x=45+(j+.5)*440/nodes,y=65+d*52;if(d){const px=45+(Math.floor(j/2)+.5)*440/(nodes/2);path(g,`M${px} ${y-45}L${x} ${y-7}`,'#afc7d1',1.3);}dot(g,x,y,7,j===0?C.green:C.blue);text(g,x,y+26,3-d,15);}}
  text(g,600,85,'active path',17);for(let d=0;d<=s.stage;d++)box(535,110+d*38,145,30,'frame k='+(3-d),'#e3f0e9',15);formula();return;
 }
 if(s.kind==='toll'){
  head('One child per call, with a changing local work toll');s.tolls.forEach((v,i)=>{const x=75+i*130;box(x,75,85,43,'k='+v,i===s.stage?'#dceee4':'#f3f8fa',18);if(i<4)arrow(g,x+85,97,x+130,97,C.blue);for(let j=0;j<v;j++)rect(g,x+25,140+j*20,35,15,i<=s.stage?'#dceee4':'#e7edf1','none');});text(g,380,262,'Accounted local work: '+s.total,18);formula();return;
 }
 if(s.kind==='swap'){
  head('Each full expression reads the newly established state');text(g,240,80,'a',20);text(g,475,80,'b',20);s.rows.slice(0,s.stage+1).forEach(([a,b],i)=>{const y=110+i*38;box(165,y,150,30,a,i===s.stage?'#dceee4':'#f3f8fa',18);box(400,y,150,30,b,i===s.stage?'#dceee4':'#f3f8fa',18);text(g,635,y+21,i===0?'initial':'after statement'+i,15);});formula();return;
 }
 if(s.kind==='posttest'){
  head('Body first, then trailing guard');box(65,76,280,55,'decrement body');box(445,76,245,55,s.stage<0?'guard not yet evaluated':s.i>=0?'guard true':'guard false',s.i<0?'#dceee4':'#edf5f8');if(s.stage>=0)arrow(g,345,104,445,104,C.blue);s.history.forEach((v,i)=>box(50+i*110,200,75,45,v,i===s.history.length-1?'#dceee4':'#f3f8fa',20));formula();return;
 }
 if(s.kind==='priorities'){
  head(`Break at ${s.stop}; ${s.first?'break':'continue'} test first`);s.rows.forEach(([i,action,sum],r)=>{const x=45+(r%5)*140,y=85+Math.floor(r/5)*105;rect(g,x,y,125,78,action==='break'?'#f6e2c4':action==='continue'?'#e7edf3':'#e0eee7','#b0c5cf');text(g,x+62,y+23,'i='+i,17);text(g,x+62,y+48,action,16);text(g,x+62,y+68,'s='+sum,16);});formula();return;
 }
 throw Error('Unknown control-flow mechanism: '+s.kind);
}
function flowHistoryTable(g,rows,headings){
 const node=E('foreignObject',{x:50,y:105,width:415,height:173}),div=document.createElementNS('http://www.w3.org/1999/xhtml','div');
 div.style.cssText="font:14px 'Source Sans 3',sans-serif;width:100%;height:100%;overflow:auto";
 const table=document.createElement('table');table.style.cssText='display:table;width:100%;table-layout:fixed;border-collapse:collapse;margin:0;font-size:14px;line-height:1.25';
 const tr=document.createElement('tr');for(const v of headings){const cell=document.createElement('th');cell.textContent=v;cell.style.cssText='padding:5px 8px;text-align:left;font-size:14px;line-height:1.25;background:#edf4f8';tr.append(cell);}table.append(tr);
 rows.forEach((row,i)=>{const tr=document.createElement('tr');row.forEach(v=>{const cell=document.createElement('td');cell.textContent=String(v);cell.style.cssText='padding:3px 8px;font-size:14px;line-height:1.25;text-align:left;background:'+(i===rows.length-1?'#e0eee7':'#f5f8fa')+';border-bottom:2px solid white';tr.append(cell);});table.append(tr);});div.append(table);node.append(div);g.append(node);
}

function typesQuestion(p,g,f){
 const s=f.snapshot,head=v=>text(g,380,30,v,20),formula=()=>vectorNative(g,f.formulaHtml,25,278,710,76);
 const box=(x,y,w,h,line,fill='#f2f7fa')=>{rect(g,x,y,w,h,fill,'#b5cbd3');text(g,x+w/2,y+h/2+6,line,18);};
 if(s.kind==='adder'){
  head('Four-bit hardware: signed result and unsigned carry');
  const labels=['first operand','second operand','stored low bits'];
  s.bits.forEach((bits,r)=>{text(g,80,90+r*55,labels[r],17,'start');[...bits].forEach((v,j)=>box(275+j*58,60+r*55,48,40,v,j===0?'#f7eddc':'#f2f7fa'));});
  text(g,380,248,`Signed sum ${s.total}; overflow ${s.overflow?'YES':'NO'}; carry out ${s.carryout}`,18);formula();return;
 }
 if(s.kind==='pipeline'||s.kind==='chop'){
  head(s.kind==='chop'?'Exact-real decimal operation checkpoints':'Typed value and destination checkpoints');
  const xs=[30,285,540];s.rows.forEach(([label,value],i)=>{const r=i<3?0:1,x=i<3?xs[i]:160+(i-3)*300,y=70+r*105;rect(g,x,y,190,65,i===s.active?'#dceee4':'#f4f8fa','#a8c1ca');text(g,x+95,y+22,label,15);text(g,x+95,y+49,value,19);});
  arrow(g,220,102,285,102,C.blue);arrow(g,475,102,540,102,C.blue);
  if(s.kind==='pipeline'&&s.rows[0][0]==='unsigned8 source'){
   path(g,'M635 135V155H255V175',C.blue,1.8);path(g,'M635 155H555V175',C.green,1.8);
  }else{path(g,'M635 135V155H255V175',C.blue,1.8);arrow(g,350,207,460,207,C.blue);}formula();return;
 }
 if(s.kind==='decimal'){
  head('Exact intermediate → rounded value at each tree node');
  s.rows.forEach(([label,exact,rounded],i)=>{const x=i<2?45:410,y=65+(i%2)*100;rect(g,x,y,300,77,i===s.stage?'#dceee4':'#f3f8fa','#acc5ce');text(g,x+150,y+22,label,16);text(g,x+150,y+54,exact+' → '+rounded,20);});
  arrow(g,195,142,195,165,C.blue);arrow(g,560,142,560,165,C.green);formula();return;
 }
 if(s.kind==='casts'){
  head('Division operands determine what a later cast receives');
  s.rows.forEach((row,i)=>{const y=65+i*67;rect(g,40,y,680,57,i===s.stage?'#dceee4':'#f4f8fa','#bdd0d6');text(g,62,y+33,row[0],18,'start');text(g,310,y+33,row[1]+'; '+row[2],15,'start');});formula();return;
 }
 if(s.kind==='short'){
  head('Reachability separates skipped from undefined');
  box(55,88,220,75,s.stage===0?'input: x = 0':'x != 0 : false','#e5f0f7');box(475,88,220,75,s.stage===3?'10/0 : undefined':s.stage===0?'right operand pending':'10/x : not evaluated',s.stage===3?'#eed8df':'#eef2f4');
  if(s.stage===3)arrow(g,275,125,475,125,C.amber);else if(s.stage>=1){path(g,'M165 163V220H475',C.green,2);box(475,195,220,60,s.stage===2?'logical result: 0':'division bypassed','#dceee4');}
  text(g,380,65,s.stage===3?'Changed operator: bitwise AND':'Original operator: logical AND',17);formula();return;
 }
 if(s.kind==='wrap'){
  head('Two different arithmetic domains');box(40,80,300,100,'unsigned32','#e4f0e9');box(420,80,300,100,'signed32','#f3e2e7');
  text(g,190,210,s.stage>=1?'exact 2³² → residue 0':'UINT_MAX + 1u',19);text(g,570,210,s.stage>=2?'exact 2³¹ → undefined':'INT_MAX + 1',19);text(g,380,250,s.stage===0?'First identify each operand type.':s.stage===1?'Only the unsigned lane has completed its operation.':'The signed lane stops before any numeric C output.',17);formula();return;
 }
 if(s.kind==='macro'){
  head('Token substitution, then the actual parse tree');
  if(s.stage===3){box(130,80,500,70,'((i++) * (i++))','#f3e2e7');text(g,380,200,'Unsequenced modifications: no predicted result.',19);formula();return;}
  if(s.stage===0){box(80,80,600,70,'SQR(1+2) → 1+2*1+2');text(g,380,210,'Substitute tokens before constructing the parse tree.',19);formula();return;}
  const done=s.stage===2;const nodes=[[380,65,done?'5':'+'],[220,125,done?'3':'+'],[540,125,'2'],[100,190,'1'],[330,190,done?'2':'*'],[285,245,'2'],[395,245,'1']];nodes.forEach(([x,y,v])=>{box(x-26,y-18,52,36,v);});
  arrow(g,354,76,244,107,C.blue);arrow(g,406,76,516,107,C.blue);arrow(g,194,138,124,172,C.blue);arrow(g,244,143,308,172,C.blue);arrow(g,310,208,293,227,C.blue);arrow(g,350,208,380,227,C.blue);
  text(g,560,208,done?'2 × 1 = 2; then add':'Grouped multiplication first',18);formula();return;
 }
 if(s.kind==='bits'){
  head(s.signed?'Signed positional weights: an asymmetric range':'Unsigned weights and maximum');
  if(s.signed&&s.stage===3){box(60,75,640,65,'signed char −128 promotes to int32 before unary minus');box(180,170,400,55,'int negation: 128 is representable','#dceee4');text(g,380,255,'−INT_MIN instead overflows its evaluated int domain.',18);formula();return;}
  const width=s.weights.length,dx=62,start=380-width*dx/2;s.weights.forEach((w,i)=>{box(start+i*dx,95,52,52,s.stage===0?'?':s.bits[i],w<0?'#f7e6d5':'#edf5f8');text(g,start+i*dx+26,182,w,18);});text(g,380,230,s.stage===0?'Read the weights before selecting an extremal pattern.':s.stage===1?'Construct the requested extremal pattern.':'Each bit contributes its displayed positional weight.',18);formula();return;
 }
 if(s.kind==='register'){
  head('Exact total, discarded carry and stored residue');box(50,85,200,76,s.stage===0?'inputs: 255 and 6':'255 + 6 = 261');box(300,85,190,76,s.stage>=1?'carry: 1 × 256':'carry: not computed','#f7eddc');box(540,85,170,76,s.stage>=2?'stored: 5':'store pending','#dceee4');if(s.stage>=1)arrow(g,250,124,300,124,C.blue);if(s.stage>=2)arrow(g,490,124,540,124,C.green);text(g,380,220,s.stage===3?'C lane: promoted int261, then byte conversion5.':'Hardware lane: exact sum precedes reduction.',18);formula();return;
 }
 if(s.kind==='layout'){
  head(`Minimum ABI: n=${s.n}, second offset=${s.offset}, size=${s.size}`);const start=70,dx=38;
  for(let i=0;i<s.size;i++){const pad=i>=s.n&&i<s.offset;rect(g,start+i*dx,115,dx-3,65,pad?'#f7e5c9':i<s.n?'#e1eff8':'#dceee4','#b3c5cd');text(g,start+i*dx+(dx-3)/2,153,i,16);}
  text(g,start+s.n*dx/2,90,'first member',17);text(g,start+(s.offset+2)*dx,90,'second member',17);text(g,380,235,s.n===s.offset?'No internal padding is required at this aligned boundary.':'Amber bytes are padding; every other byte belongs to a member.',17);formula();return;
 }
 if(s.kind==='array'){
  head('Five rows × six elements × four bytes');
  for(let i=0;i<5;i++)for(let j=0;j<6;j++){const active=s.stage===1?i===0:s.stage===2?i===4&&j===5:false;rect(g,55+j*59,70+i*33,55,29,active?'#e7d5ad':'#e3f0f7','#b6cbd5');text(g,82+j*59,90+i*33,4*(6*i+j),14);}
  text(g,535,110,'row stride: 24 bytes',18);text(g,535,160,'whole object: 120 bytes',18);text(g,535,210,s.stage===3?'parameter pointer: 8 bytes':'last element ends at byte119',17);formula();return;
 }
 if(s.kind==='packed'){
  head(`Packed flags: ${s.n} bits in ${s.size} whole bytes`);
  for(let row=0;row<s.size;row++)for(let bit=0;bit<8;bit++){const i=row*8+bit;rect(g,165+bit*53,78+row*53,46,43,i<s.n?'#dceee4':'#f0e9dc','#b9cdd5');text(g,188+bit*53,106+row*53,i<s.n?i+1:'·',17);}
  text(g,380,260,'Dots mark unused bits inside the final allocated byte.',17);formula();return;
 }
 if(s.kind==='float'){
  head(s.base===32?'Actual p=5 neighbors near32':'Binary64 neighbors at a local origin a=2⁵³');const vals=[-3,-2,-1,0,2,4],x=v=>310+60*v;
  path(g,'M100 155H630','#8faab8',1.8);vals.forEach(v=>{dot(g,x(v),155,4,C.blue);text(g,x(v),197,s.base===32?s.base+v:v===0?'a':`a${v>0?'+':''}${v}`,17);});
  const binary64=s.base!==32,midpoint=s.stage===2&&binary64||s.stage===3&&!binary64?3:1;
  if(s.stage>=1){dot(g,x(midpoint),155,6,C.amber);text(g,x(midpoint),120,'exact midpoint',15);}
  const rounding=binary64?s.stage>=1: s.stage>=2;
  if(rounding){const chosen=midpoint===1?0:4;const ring=E('circle',{cx:x(chosen),cy:155,r:12,fill:'none',stroke:C.green,'stroke-width':3});g.append(ring);text(g,380,250,binary64?`Chosen neighbor: a+${chosen}; its retained significand is even.`:`Chosen neighbor: ${32+chosen}; retained significand ${(32+chosen)/2} is even.`,17);}else text(g,380,250,s.stage===0?'Spacing changes from1 to2 at this boundary.':'The intermediate odd integer has no exact representation.',17);formula();return;
 }
 if(s.kind==='division'){
  head('Negative quotient: truncation is not floor');
  if(s.stage===3){box(95,75,240,75,'INT_MIN / −1');box(430,75,240,75,'undefined','#f3e2e7');arrow(g,335,112,430,112,C.amber);text(g,380,220,'Mathematical quotient 2³¹ does not fit int32.',19);formula();return;}
  path(g,'M110 145H650','#9ab1bd',1.5);[[-6,210],[-5,530]].forEach(([v,x])=>{dot(g,x,145,4,C.blue);text(g,x,188,v,20);});dot(g,423.333,145,6,C.amber);text(g,423.333,115,'−16/3',19);
  if(s.stage>=1){text(g,210,227,'floor: −6',18);text(g,530,227,'truncate: −5',18);}else text(g,380,230,'First locate the exact real quotient.',18);formula();return;
 }
 throw Error('Unknown typed mechanism: '+s.kind);
}

function matricesQuestion(p,g,f){
 const s=f.snapshot;
 if(s.kind==='source')return vectorsQuestion(p,g,f);
 if(s.kind==='positivity'){
  text(g,380,30,`Dimension ${s.dimension}: strict positivity of both components`,20);path(g,'M95 195H665','#9eb4bf',1.5);
  [s.parallel,s.perpendicular].forEach((v,i)=>{const x=180+i*310,y=v>0?195-v*30:195;if(v===0)path(g,`M${x} 195h130`,C.amber,3);else rect(g,x,y,130,Math.abs(v)*30,v>0?'#cfe8dd':'#eed5dc','none');text(g,x+65,65,['all-equal line','sum-zero subspace'][i],18);text(g,x+65,252,`coefficient = ${v}`,18);});vectorNative(g,f.formulaHtml,25,265,710,90);return;
 }
 if(s.kind==='allones'||s.kind==='fixed'){
  text(g,380,30,s.kind==='allones'?'All-ones action, then the adapted-basis scales':'Permutation, weighted product, and fixed coordinates',20);
  text(g,200,65,s.kind==='allones'?'J in standard coordinates':'P: actual permutation',18);text(g,570,65,s.kind==='allones'?'I + J in the adapted basis':'DP: weighted rows',18);
  vectorNative(g,s.leftMath,45,80,310,165);vectorNative(g,s.rightMath,410,80,310,165);
  text(g,380,268,s.kind==='allones'?'The complement is unchanged by J and kept by I.':s.row===5?'Changed hypothesis: all five coordinates are now fixed.':`Checked coordinate ${s.row+1}: weighted diagonal entry is zero.`,18);vectorNative(g,f.formulaHtml,20,285,720,68);return;
 }
 if(s.kind==='shear'){
  text(g,380,30,'Forward shear and exact inverse on a common plane',20);const xy=v=>[90+40*v[0],220-40*v[1]];
  path(g,'M50 220H385M90 250V70','#9eb4bf',1);for(let i=0;i<=6;i++)text(g,90+i*40,243,i,15);
  const corners=s.stage===1?[[0,0],[1,0],[6,1],[5,1]]:[[0,0],[1,0],[1,1],[0,1]];path(g,'M'+corners.map(v=>xy(v).join(' ')).join('L')+'Z','#a7c8d5',1.5);
  vectorEntityArrow(g,'shear-point',xy([0,0]),xy(s.point),C.blue);text(g,450,115,'Input: (1, 1)',18,'start');text(g,450,160,'Forward: (6, 1)',18,'start');text(g,450,205,'Restored: (1, 1)',18,'start');vectorNative(g,f.formulaHtml,25,265,710,90);return;
 }
 if(s.kind==='power'){
  text(g,380,30,`Power ${s.k}: chronological two-step paths`,20);
  const pos=[[90,110],[225,110],[360,110]];['e1','e2','e3'].forEach((v,i)=>{dot(g,...pos[i],4,C.blue);text(g,pos[i][0],80,v,18);});arrow(g,355,110,230,110,C.green);arrow(g,220,110,95,110,C.green);text(g,225,145,'N moves left; I holds a coordinate.',16);
  vectorNative(g,s.matrixMath,65,160,320,105);
  text(g,580,70,'Two distinct N slots: i < j',17);for(let j=2;j<=s.k;j++)for(let i=1;i<j;i++){const node=E('g',{'data-entity':`slot-pair-${i}-${j}`});dot(node,460+j*18,90+i*15,4,j===s.k?C.amber:C.blue);g.append(node);}text(g,580,260,`Exact pair count: ${s.value}`,18);vectorNative(g,f.formulaHtml,15,282,730,70);return;
 }
 if(s.kind==='rank'){
  text(g,380,30,'Typed maps: onto intermediate space, then injective embedding',19);
  [['R⁵',40],['R²',300],['R⁵',560]].forEach(([v,x])=>{rect(g,x,62,160,48,'#f4f8fa','#b5cbd3');text(g,x+80,93,v,20);});arrow(g,200,86,300,86,C.blue);arrow(g,460,86,560,86,C.green);text(g,250,65,'V',18);text(g,510,65,'U',18);
  vectorNative(g,s.leftMath,25,126,220,135);vectorNative(g,s.rightMath,265,126,230,135);vectorNative(g,s.productMath,515,115,225,165);text(g,135,275,'U: embed axes 1 and 2',15);text(g,380,275,'V: read axes 3 and 4',15);text(g,628,295,'UV: rank 2',15);vectorNative(g,f.formulaHtml,15,300,730,55);return;
 }
 if(s.kind==='basis'){
  text(g,380,30,'Actual basis image and the coefficient reconstruction',20);const xy=v=>[185+26*v[0],90-26*v[1]];path(g,'M65 90H350M185 55V260','#9eb4bf',1);
  vectorEntityArrow(g,'basis-image',xy([0,0]),xy(s.point),C.blue);vectorEntityArrow(g,'original-basis-2',xy([0,0]),xy([1,-1]),'#b4c4ca');
  text(g,425,110,'Standard image: (2, -5)',18,'start');text(g,425,158,'Basis coordinates: (-3/2, 7/2)',18,'start');text(g,425,208,'Convert output coordinates too.',18,'start');vectorNative(g,f.formulaHtml,25,265,710,90);return;
 }
 if(s.kind==='block'){
  text(g,380,30,'Ordered block action and backward recovery',20);
  const values=s.stage===0?['x = e1','y = e1']:s.stage===1?['u = 3e1',`v = ${s.lower}e1`]:['x = u - 2y = e1',`y = v / ${s.lower} = e1`];
  [0,1].forEach(i=>{rect(g,90+i*370,88,230,105,'#f2f7fa','#aac3cc');text(g,205+i*370,117,'5-coordinate group '+(i+1),17);text(g,205+i*370,158,values[i],18);});
  if(s.stage===1)arrow(g,460,140,320,140,C.amber);text(g,380,230,`Determinant: ${s.lower}⁵ = ${s.det}; coupling has no inverse requirement.`,17);vectorNative(g,f.formulaHtml,20,260,720,95);return;
 }
 if(s.kind==='gram'){
  text(g,380,30,'Real kernel direction and squared output norm',20);vectorNative(g,s.leftMath,35,62,300,90);vectorNative(g,s.rightMath,425,62,300,90);text(g,185,55,'A',18);text(g,575,55,'AᵀA',18);
  const xy=v=>[170+28*v[0],220-28*v[1]];path(g,'M75 220H275M170 165V275','#9eb4bf',1);vectorEntityArrow(g,'kernel-input',xy([0,0]),xy(s.x),C.blue);text(g,500,208,`Output: (${s.out})`,18);text(g,500,245,`Squared length: ${s.norm}`,18);vectorNative(g,f.formulaHtml,25,282,710,70);return;
 }
 if(s.kind==='trace'){
  text(g,380,30,'Same six scalar terms, regrouped without loss',20);
  for(let i=0;i<2;i++)for(let j=0;j<3;j++){const x=190+j*130,y=95+i*72;rect(g,x,y,105,54,s.stage===0?(i?'#e4f1ea':'#e5f0f7'):s.stage===1?['#e5f0f7','#e4f1ea','#f7eddc'][j]:'#f3f8fa','#bbced5');text(g,x+52,y+34,s.terms[i][j],22);}
  text(g,380,265,s.stage===0?'Two row sums: 4 and -1.':s.stage===1?'Three column sums: 2, -2, 3.':'Both groupings total three.',18);vectorNative(g,f.formulaHtml,15,280,730,75);return;
 }
 throw Error('Unknown matrix question geometry: '+s.kind);
}

function vectorNative(g,html,x,y,w,h){countingFormula(g,{formulaHtml:html},x,y,w,h);const math=g.lastElementChild.querySelector('math');if(math)math.style.mathStyle='compact';}
function vectorEntityArrow(g,id,a,b,color){const node=E('g',{'data-entity':id});if(Math.hypot(a[0]-b[0],a[1]-b[1])>.1)arrow(node,...a,...b,color);else dot(node,a[0],a[1],3,color);g.append(node);}
function vectorsQuestion(p,g,f){
 const s=f.snapshot;
 if(s.kind==='orthogonalize'){
  text(g,380,30,'Exact Gram–Schmidt: subtract, skip, or normalize',20);
  const xy=v=>[120+48*v[0],205-48*v[1]];path(g,'M65 205H350M120 260V65','#9eb4bf',1);
  vectorEntityArrow(g,'gs-input-'+s.inputIndex,xy([0,0]),xy(s.input),C.blue);
  s.basis.forEach((q,i)=>vectorEntityArrow(g,'gs-unit-'+i,xy([0,0]),xy(q),i?C.green:'#9566a7'));
  text(g,420,95,`Current input ${s.inputIndex+1}: (${s.input})`,18,'start');text(g,420,145,`Residual: (${s.residual})`,18,'start');text(g,420,195,`Retained unit directions: ${s.basis.length}`,18,'start');text(g,420,240,'Zero residual is skipped.',18,'start');
  vectorNative(g,f.formulaHtml,35,273,690,80);return;
 }
 if(s.kind==='source'){
  text(g,380,30,'Literal source map and the correctly normalized foot',20);
  const xy=v=>[85+55*v[0],230-55*v[1]];
  path(g,'M55 230H365M85 255V95','#9eb4bf',1);
  [0,1,2,3,4,5].forEach(i=>{path(g,`M${85+i*55} 225V235`,'#9eb4bf',1);text(g,85+i*55,250,i,15);});
  vectorEntityArrow(g,'correct-foot-vector',xy([0,0]),xy(s.foot),C.green);vectorEntityArrow(g,'given-vector',xy([0,0]),xy(s.x),C.blue);
  const sourceMark=E('g',{'data-entity':'source-output'}),sourcePoint=xy(s.source);sourceMark.append(E('circle',{cx:sourcePoint[0],cy:sourcePoint[1],r:6,fill:'none',stroke:'#9566a7','stroke-width':2}));g.append(sourceMark);
  text(g,455,105,'Blue: given input x',18,'start');text(g,455,145,'Purple ring: source output',18,'start');text(g,455,185,'Green: actual foot',18,'start');text(g,455,225,`Basis length: ${s.scale}`,18,'start');
  vectorNative(g,f.formulaHtml,25,250,710,105);return;
 }
 if(s.kind==='positivity'){
  text(g,380,30,'Two orthogonal components test strict positivity',21);
  path(g,'M95 200H665','#9eb4bf',1.5);
  [s.parallel,s.perpendicular].forEach((v,i)=>{const x=180+i*310,y=v>0?200-v*32:200,h=Math.abs(v)*32;if(v===0)path(g,`M${x} 200h130`,C.amber,3);else rect(g,x,y,130,h,v>0?'#cfe8dd':'#eed5dc','none');text(g,x+65,80,['all-equal line','sum-zero plane'][i],18);text(g,x+65,255,`coefficient = ${v}`,18);});
  vectorNative(g,f.formulaHtml,35,265,690,90);return;
 }
 if(s.kind==='gram'){
  text(g,380,30,`Question ${s.question}: exact inputs and coupled equations`,20);
  ['u','v','target w'].forEach((v,i)=>{text(g,130+i*250,75,v,18);vectorNative(g,s.inputMath[i],25+i*250,90,210,50);});
  vectorNative(g,s.systemMath,100,150,560,95);
  text(g,380,267,'Current justified deduction',18);
  vectorNative(g,f.formulaHtml,35,278,690,75);return;
 }
 if(s.kind==='coordinates'){
  text(g,380,30,'The same vector has basis coordinates and physical length',20);
  const xy=v=>[110+48*v[0],215-48*v[1]],mid=[s.c[0],s.c[0]];
  path(g,'M60 215H355M110 268V55','#9eb4bf',1);
  vectorEntityArrow(g,'basis-component-1',xy([0,0]),xy(mid),C.blue);vectorEntityArrow(g,'basis-component-2',xy(mid),xy(s.partial),C.green);
  const target=xy(s.target);dot(g,...target,5,C.amber);
  text(g,425,100,'Blue: first basis component',18,'start');text(g,425,145,'Green: second, head to tail',18,'start');text(g,425,190,'Amber: fixed target (3, 1)',18,'start');text(g,425,235,`Coordinates so far: (${s.c})`,18,'start');
  vectorNative(g,f.formulaHtml,35,283,690,70);return;
 }
 if(s.kind==='minimum'){
  text(g,380,30,'Objective on the feasible line: F(y) = squared norm',20);
  const xy=(t,v)=>[95+400*t,220-70*v];path(g,'M95 55V220H690','#9eb4bf',1.5);
  [0,1,2].forEach(v=>{path(g,`M90 ${220-70*v}h10`,'#9eb4bf',1);text(g,72,226-70*v,v,16);});
  const curve=Array.from({length:81},(_,i)=>{const y=i/60;return xy(y,3*(y-2/3)**2+2/3);});path(g,'M'+curve.map(v=>v.join(' ')).join('L'),C.blue,2.2);
  [0,1/3,2/3,1,4/3].forEach(t=>{const x=95+400*t;path(g,`M${x} 216V224`,'#9eb4bf',1);text(g,x,250,['0','1/3','2/3','1','4/3'][Math.round(t*3)],16);});
  const mark=E('g',{'data-entity':'feasible-candidate'}),point=xy(s.y,s.value);dot(mark,...point,6,s.minimum?C.green:C.amber);g.append(mark);
  vectorNative(g,f.formulaHtml,25,255,710,100);return;
 }
 throw Error('Unknown vector question contract: '+s.kind);
}

function countingFormula(g,f,x,y,w,h){
 nativeFormula(g,f,x,y,w,h);
 const body=g.lastElementChild.firstElementChild,math=body.querySelector('math');
 body.style.display='flex';body.style.alignItems='center';body.style.justifyContent='center';body.style.height='100%';body.style.overflowY='hidden';
 if(math){math.style.margin='0';math.style.fontSize='18px';math.style.lineHeight='1.15';}
}
function countingQuestion(p,g,f){
 const s=f.snapshot;
 if(s.kind==='stars'){
  text(g,380,35,`Encoding ${s.index} of ${s.total}: five units, two separators`,21);
  s.tokens.forEach((v,i)=>{const x=110+i*90;if(v==='|')path(g,`M${x} 100V173`,C.amber,5);else dot(g,x,136,14,C.blue);text(g,x,205,i,16);});
  text(g,380,245,'Slot numbers describe the encoding; coordinates are named.',18);
  countingFormula(g,{formulaHtml:f.formulaHtml},55,270,650,82);return;
 }
 if(s.kind==='parity'){
  text(g,380,30,'Exact parity rows after imposing c at least one',21);
  ['b','largest j','row count','included so far'].forEach((h,i)=>text(g,110+i*175,72,h,18));
  s.counts.forEach((v,i)=>{const y=110+i*34;if(i===s.active)rect(g,40,y-22,680,32,'#fff0cc','none');[i,s.upper[i],v,i<=s.active?s.counts.slice(0,i+1).reduce((a,b)=>a+b,0):'pending'].forEach((v,j)=>text(g,110+j*175,y,String(v),18));});
  countingFormula(g,{formulaHtml:f.formulaHtml},35,290,690,60);return;
 }
 if(s.kind==='onto'){
  text(g,380,32,'Inclusion–exclusion: signed terms, not disjoint events',20);
  s.terms.forEach((v,i)=>{const x=45+i*143;const h=Math.abs(v)/4096*125;rect(g,x,225-h,105,h||2,i<=s.stage?(v<0?'#ecd6dc':'#cee9df'):'#edf3f6','none');text(g,x+52.5,243,s.labels[i],15);text(g,x+52.5,72,String(v),18);});
  countingFormula(g,{formulaHtml:f.formulaHtml},40,270,680,84);return;
 }
 if(s.kind==='dp'){
  text(g,380,30,'No adjacent ones: exact prefix-count recurrence',21);
  s.values.forEach((v,i)=>{const x=36+i*78;rect(g,x,75,67,43,i<=s.n?'#d9ebe5':'#edf3f6');text(g,x+33.5,99,i<=s.n?v:'?',18);text(g,x+33.5,145,i,16);});
  text(g,380,186,`Complete words at length ${s.examplesLength}${s.n>5?' (reference)':''}`,18);
  s.words.forEach((v,i)=>text(g,100+(i%5)*140,224+Math.floor(i/5)*28,v||'empty',18));
  countingFormula(g,{formulaHtml:f.formulaHtml},45,303,670,53);return;
 }
 if(s.kind==='pairing'){
  text(g,380,30,`Pairing ${s.index} of 105: each label has one partner`,21);
  const pos=Array.from({length:8},(_,i)=>[380+220*Math.cos(-Math.PI/2+i*Math.PI/4),171+90*Math.sin(-Math.PI/2+i*Math.PI/4)]);
  s.pairs.forEach(([a,b])=>{const [x,y]=pos[a-1],[X,Y]=pos[b-1],d=Math.hypot(X-x,Y-y),dx=(X-x)/d*21,dy=(Y-y)/d*21;path(g,`M${x+dx} ${y+dy}L${X-dx} ${Y-dy}`,C.blue,2.4);});
  pos.forEach(([x,y],i)=>{dot(g,x,y,21,'#e5f1f5');text(g,x,y+6,i+1,18);});
  countingFormula(g,{formulaHtml:f.formulaHtml},45,303,670,53);return;
 }
 if(s.kind==='report'){
  text(g,380,30,'Eight ordered words, four reports with unequal fibers',21);
  s.words.forEach((v,i)=>{const x=65+(i%4)*170,y=80+Math.floor(i/4)*83;rect(g,x,y,120,50,v.split('1').length-1===s.k?'#cee8df':'#eef4f7');text(g,x+60,y+29,v,21);});
  text(g,380,262,`The report with ${s.k} ones combines ${s.counts[s.k]} words.`,20);
  countingFormula(g,{formulaHtml:f.formulaHtml},55,288,650,65);return;
 }
 throw Error('Unknown counting question contract: '+s.kind);
}

function axiomsQuestion(p,g,f){
 const s=f.snapshot,id=p.scene.id;
 if(id.includes("atoms")){
  text(g,380,24,`Triple mass t = ${s.t}; binary labels identify A, B and C membership`,18);
  ["111","110","101","011","100","010","001","000"].forEach((label,i)=>{
   const x=50+(i%4)*175,y=80+Math.floor(i/4)*125,q=num(s.masses[i]);
   rect(g,x,y,135,75,q<0?"#f4d3dc":q===0?"#f1f4f6":"#d9ecdf",q<0?C.red:C.ink);
   text(g,x+67.5,y-20,label,19);nativeFormula(g,{formulaHtml:s.massMath[i]},x+10,y+18,115,45);
  });
  text(g,380,313,s.valid?"All masses are nonnegative: a valid atomic law":"Negative mass: this candidate law is impossible",19,"middle",s.valid?C.green:C.red);
  text(g,380,338,"The total is one; nonnegativity must also be checked.",17);return;
 }
 if(id==="axioms-question-urn"){
  text(g,380,28,["Original ten equally likely pairs","Condition: at least one red","Renormalize the nine retained pairs","Target: three red-red pairs"][s.stage],20);
  s.pairs.forEach((pair,i)=>{const x=45+(i%5)*137,y=80+Math.floor(i/5)*122,kept=s.stage===0||s.kept[i];
   rect(g,x,y,115,78,!kept?"#f1f4f6":s.target[i]?"#d1e8d9":"#dcebf5");
   text(g,x+57.5,y-20,pair.join(", "),18);nativeFormula(g,{formulaHtml:s.massMath[i]},x+7,y+20,101,45);
  });text(g,380,337,s.stage===0?"Original mass per pair: 1/10":s.stage===1?"Retained original mass: 9/10; normalize next":"Conditional target: 3 of 9 retained pairs",18);return;
 }
 const report=id==="axioms-question-report",counts=s.counts;
 text(g,380,28,report?"Eight equally likely sequences; group sizes 1, 3, 3, 1":"64 equally likely ordered outcomes; count each category exactly",18);
 path(g,"M75 270H705",C.ink,2);
 counts.forEach((q,i)=>{const x=report?105+155*i:125+190*i,h=report?45*q:4*q,w=report?95:110;
  rect(g,x,270-h,w,h,report?(i===s.active?"#f4d795":"#bad4e3"):(s.stage>0&&i>0?"#b7dac5":"#bad4e3"));
  text(g,x+w/2,256-h,q,21);text(g,x+w/2,301,report?`K=${i}`:["All distinct","One repeated pair","All equal"][i],17);
 });text(g,380,338,report?`Active K=${s.active}; probability ${s.counts[s.active]}/8`:["24+36+4 = 64 outcomes","Exact repetition: 36+4 = 40 outcomes","Pair-equality bound: 36+3×4 = 48 counts"][s.stage],18);
}

function loopQuestion(p,g,f){
 const s=f.snapshot,id=p.scene.id;
 if(id==="loop-question-minimum"){
  text(g,380,34,"One comparison per key; assignments only on a true test",18);
  s.values.forEach((v,j)=>{const x=100+j*72;rect(g,x,80,58,55,j+1===s.i?"#ffe1a2":j+1<s.i?"#cce6d7":"#eef3f6");text(g,x+29,115,v,24);text(g,x+29,159,j+1,17);});
  text(g,380,197,`Position ${s.i}: compare ${s.key} with ${s.before}`,19);
  text(g,380,238,s.update?"True: assign this key as the new minimum":"False: preserve the established minimum",20,"middle",s.update?C.green:C.red);
  text(g,380,282,`Minimum now ${s.after}; comparisons ${s.comparisons}; updates ${s.updates}`,20);
  text(g,380,335,"The initial minimum is positive infinity; no array entry is skipped.",17);return;
 }
 const parity=id==="loop-question-parity";
 text(g,380,22,parity?"Rows: i; columns: j; keep i+j even inside j ≤ i":`Fixed i=${s.i}; rows: j; columns: k; keep i*j*k ≤ ${s.n}`,18);
 for(let row=1;row<=8;row++){
  text(g,130,79+(row-1)*28,row,17);
  for(let col=1;col<=8;col++){
   const valid=parity?col<=row: s.i*row*col<=s.n;
   const visited=!parity||row<=s.i,keep=valid&&(!parity||(row+col)%2===0);
   const x=165+(col-1)*52,y=60+(row-1)*28;
   rect(g,x,y,43,26,visited&&keep?"#b5d9c3":visited&&valid?"#f1d6dd":"#f3f5f7",parity&&row===s.i?C.amber:"#bdcfd8");
   if(visited&&valid&&!keep)text(g,x+21.5,y+19,"×",17,"middle",C.red);
  }
 }
 for(let col=1;col<=8;col++)text(g,186.5+(col-1)*52,312,col,17);
 text(g,380,338,parity?`Active row ${s.i}: ${s.rowCount} bodies; cumulative ${s.total}`:`Layer i=${s.i}: ${s.layerCount} triples; cumulative ${s.total}`,18);
}

function asymPlot(p,g,f){
 const id=p.scene.id,logarithmic=id==="asym-log-oscillation",floor=id==="asym-floor-ratio";
 const all=p.scene.frames.map(f=>f.snapshot),seen=all.slice(0,p.index+1),current=f.snapshot;
 const maxX=logarithmic?24:floor?32:16,maxY=floor?1:16;
 const at=s=>[75+590*(logarithmic?s.logn:s.n)/maxX,logarithmic?175-5*s.ordinate:285-220*num(s.ordinate)/maxY];
 arrow(g,75,logarithmic?175:285,680,logarithmic?175:285,C.ink);arrow(g,75,295,75,45,C.ink);
 text(g,380,32,logarithmic?"Vertical: ln(ratio); horizontal: ln(n)":"Vertical: ratio to n; horizontal: integer n",18);
 const ticks=logarithmic?[-20,-10,0,10,20]:floor?[.5,1]:[1,8,16];
 for(const r of ticks){const y=logarithmic?175-5*r:285-220*r/maxY;path(g,`M70 ${y}H680`,r===0?C.ink:"#d2dfe6",1,{"stroke-dasharray":r===0?"none":"4 4"});text(g,55,y+6,r,16);}
 for(const x of logarithmic?[0,6,12,18,24]:floor?[0,8,16,24,32]:[0,4,8,12,16]){const X=75+590*x/maxX;text(g,X,315,x,16);}
 for(let i=0;i<seen.length;i++){const s=seen[i],[x,y]=at(s);dot(g,x,y,i===seen.length-1?7:4,logarithmic?s.sign>0?C.green:C.red:floor?C.blue:s.n%2?C.red:C.green);}
 text(g,380,345,logarithmic?`Current integer n = ${current.n}; no continuous interpolation`:floor?`Exact ratio ${current.ordinate}; every point stays in (1/2, 1]`:`Current ratio ${current.ordinate}; green even inputs, red odd inputs`,17);
}
function probabilityExact(p,g,f,pos){const s=f.snapshot||{},id=p.scene.id;
 if(id==="conditional-strip"){const x=80,y=305,k=240,e=num(s.epsilon);axes(g,{x,y,w:k,h:k,xlabel:"X",ylabel:"Y"});g.append(E("polygon",{points:`${x},${y} ${x},${y-k} ${x+k},${y-k}`,fill:"#f0f6fa",stroke:C.blue}));const Y0=y-k*.5,Y1=y-k*(.5+e);g.append(E("polygon",{points:`${x},${Y0} ${x+k*.5},${Y0} ${x+k*(.5+e)},${Y1} ${x},${Y1}`,fill:"#ffe0a1",stroke:C.amber}));rect(g,x,Y1,k*.25,k*e,"#bde3ce",C.green);text(g,525,95,"Joint density: 2 on 0 < X < Y < 1",20);text(g,525,150,`Observation: 1/2 ≤ Y ≤ 1/2 + ${s.epsilon}`,19);text(g,525,210,`Target: X ≤ 1/4; mass ${s.target}`,20);text(g,525,265,`Strip mass ${s.mass}; ratio ${s.ratio}`,20);text(g,525,320,"Green / amber mass → 1/2",21);return;}
 if(["bayes-normalize","bayes-frequencies","bayes-partition","conditional-atoms"].includes(id)){const values=s.values||s.weights||s.masses;let left=80;values.forEach((v,i)=>{const w=600*num(v);rect(g,left,130,w,80,["#a9d7e1","#bde3ce","#f4d59c","#e4cddd"][i]);text(g,135+i*160,255,`${id==="conditional-atoms"?"atom":"H"}${i+1}: ${v}`,20);left+=w;});path(g,"M80 220H680",C.ink);text(g,80,240,"0",16);text(g,680,240,"1",16);text(g,380,60,s.heading||s.phase||(id==="bayes-frequencies"?`${s.positive?"Positive":"Negative"} report: ${s.stage}`:`Included sources: ${s.included}`),22);return;}
 if(id==="conditional-mixture"){const rows=[[.5,.5],[.45,.05],[.9,.1]][p.index];strip(g,70,70,["type 1","type 2"],{cell:210,labels:false,title:"Hidden type weights"});rows.forEach((v,i)=>{rect(g,130+i*260,300-110*v,80,110*v,["#8bc5d3","#bde3ce"][i]);text(g,170+i*260,280-110*v,v,22);});text(g,595,155,p.index===2?"Next success: 41/50":"Fixed success rates:\n9/10 and 1/10",21);text(g,380,330,["Equal prior type weights","Joint masses after a success","Posterior type weights after normalization"][p.index],21);return;}
 if(id==="conditional-selection"){const total=s.retained.filter(Boolean).length;["00","01","10","11"].forEach((v,i)=>{const x=130+(i%2)*170,y=100+Math.floor(i/2)*130;rect(g,x,y,150,90,s.retained[i]?"#cce9dc":"#f0f1f3");text(g,x+75,y+32,v,24);text(g,x+75,y+68,s.retained[i]?`mass 1/${total}`:"excluded",20);});text(g,590,140,`P(A) = ${s.a}`,22);text(g,590,190,`P(B) = ${s.b}`,22);text(g,590,240,`P(A ∩ B) = ${s.joint}`,22);return;}
 if(id==="conditional-history"){const prefix=p.index===0?"":p.index===1?"1":"11",points={root:[90,175],"0":[285,75],"1":[285,275],"00":[580,40],"01":[580,110],"10":[580,235],"11":[580,310]};for(const [n,[x,y]] of Object.entries(points)){if(n!=="root"){const parent=n.length===1?"root":n[0],[X,Y]=points[parent];arrow(g,X,Y,x,y,prefix&&n.startsWith(prefix)?C.amber:C.blue);}dot(g,x,y,17,C.blue);text(g,x,y+6,n==="root"?"Ω":n,18,"middle","white");}text(g,380,355,`Observed prefix mass ${s.prefix}; keep the complete conditioning history.`,18);return;}
 if(id==="conditional-simpson"){const values=s.weights.length?[num(s.a),num(s.b)]:[.9,.8,.4,.3],labels=s.weights.length?["A aggregate","B aggregate"]:["A easy","B easy","A hard","B hard"];probabilityBars(g,values,labels);text(g,380,345,s.weights.length?`Easy-case weights: A ${s.weights[0]}, B ${s.weights[1]}`:"Compare each method within the same stratum.",19);return;}
 if(id==="pairwise-independence"){const vals=[f.metrics.X,f.metrics.Y,f.metrics["Z = X xor Y"]];strip(g,95,115,vals,{cell:175,labels:false,title:"One atom: X           Y           Z = X XOR Y"});text(g,380,270,"Only 000, 011, 101 and 110 are possible; each has mass 1/4.",20);return;}
 if(id==="conditional-urn"||id==="draw-without-replacement"){const balls=f.nodes.filter(n=>/^ball/.test(n.id));balls.forEach(n=>{const q=pos.get(n.id)||n;dot(g,q.x,q.y,23,n.label[0]==="R"?C.red:C.blue);text(g,q.x,q.y+7,n.label,20,"middle","white");if(n.tone==="active")g.append(E("circle",{cx:q.x,cy:q.y,r:30,fill:"none",stroke:C.amber,"stroke-width":3}));});if(id==="conditional-urn")text(g,380,345,`Remaining R = ${s.red}, B = ${s.blue}; prefix mass ${s.mass}`,20);return;}
 probability(p,g,f,pos);
}
function probabilityBars(g,values,labels){path(g,"M65 290H710");values.forEach((v,i)=>{const x=90+i*600/values.length,w=Math.min(80,420/values.length);rect(g,x,290-190*v,w,190*v,i%2?"#a9d7e1":"#bde3ce");text(g,x+w/2,278-190*v,v,20);text(g,x+w/2,325,labels[i],17);});}
function numericExact(p,g,f,pos){const s=f.snapshot||{},id=p.scene.id;
 if(id==="comb-word"||id==="finite-representation"){const w=s.w||4,x=s.x??+f.metrics["Unsigned interpretation"];strip(g,100,100,x.toString(2).padStart(w,"0").split(""),{cell:75,labels:false,title:`Word width: ${w}; most-significant bit on the left`});text(g,250,235,`Unsigned: ${x}`,23);text(g,530,235,`Signed: ${s.signed??f.metrics["Signed interpretation"]}`,23);if(s.inv!==undefined)text(g,380,305,`Bitwise NOT = ${s.inv}; logical NOT = 0`,22);return;}
 if(id==="word-bit-cost"){["a","b","o"].forEach((prefix,k)=>{const ns=f.nodes.filter(n=>n.id.startsWith(prefix)).sort((a,b)=>a.x-b.x);strip(g,160,55+k*85,ns.map(n=>n.label),{cell:85,labels:false,title:["First operand","Second operand","Sum bits produced so far"][k]});});text(g,640,260,`Carry ${s.carry}`,21);return;}
 if(id==="float-rounding"){const exact=+f.metrics["Exact integer"],rounded=+f.metrics["Binary32 result"],x=n=>110+120*(n-16777216);path(g,"M90 175H690");for(const n of [16777216,16777218,16777220]){path(g,`M${x(n)} 160V190`);text(g,x(n),220,n,20);}dot(g,x(exact),135,6,C.amber);arrow(g,x(exact),145,x(rounded),175,C.green);text(g,380,300,`Exact ${exact} → binary32 ${rounded}; ties choose an even significand.`,18);return;}
 if(["euclid","division","power","modular-power","gray-code","hamming-code"].includes(id))numeric(p,g,f,pos);else derivationExact(p,g,f);
}
function draw(p,nodes,edges,positions){let type=p.scene.visual?.type;if(!type){type=p.scene.id.startsWith("functions-custom-")?"memory":p.scene.id.startsWith("arrays-custom-")?"array":p.scene.id.startsWith("kmap-custom-")?"kmap":p.scene.id.startsWith("combin-custom-")?"circuit":null;if(type)p.scene.visual={type,claim:"Exact state of the chapter's adjustable subject-specific model."};}if(!type)throw Error(`No reviewed visual contract for ${p.scene.id}`);p.grid.replaceChildren();p.links.replaceChildren();p.nodeLayer.replaceChildren();p.nodes.clear();const g=p.nodeLayer;delete g.dataset.netValues;legend(p,type);const f=p.scene.frames[p.index];g.dataset.visualType=type;const functions={bars:mergeExact,search,venn,truth,graph:graphExact,geometry:geometryExact,matrices,tiles,array:arrayExact,memory:memoryExact,derivation:derivationExact,numeric:numericExact,probability:probabilityExact,plot,tree,enumeration:gridEnumeration,kmap:kmapExact,waveform,circuit:circuitExact,cmos};if(!functions[type])throw Error(`Unknown visual type ${type}`);functions[type](p,g,f,positions);p.canvas.dataset.visualType=type;p.canvas.dataset.visualContract=p.scene.visual.claim;window.DiagramLayout?.finish(p.canvas);}
function memoryExact(p,g,f,pos){const id=p.scene.id,s=f.snapshot||{};if(id==="fn-sharing"){arrayExact(p,g,f,pos);return;}if(id.startsWith("functions-custom-")){memory(p,g,{...f,snapshot:{...s,caller:`a = ${s.caller}`,callee:s.callee===null?"Invocation not active":String(s.callee),shared:s.shared===null?"No shared object":`Shared target = ${s.shared}`}},pos);return;}
 if(id.startsWith("branch-")){const input=f.metrics.Input,active=p.index;path(g,"M100 60H240V100");text(g,170,42,`Input x = ${input}`,22);const diamond=(x,y,label)=>{path(g,`M${x} ${y-30}L${x+90} ${y}L${x} ${y+30}L${x-90} ${y}Z`,C.ink,2,{fill:active===0?"#ffe0a1":"#f5fafc"});text(g,x,y+6,label,22);};diamond(240,130,"x < 0");diamond(240,250,"x = 0");path(g,"M240 160V220");text(g,268,196,"no",17);arrow(g,330,130,510,130,input<0?C.green:C.ink);text(g,600,136,"negative",22);arrow(g,330,250,510,250,input===0?C.green:C.ink);text(g,600,256,"zero",22);arrow(g,240,280,240,320,input>0?C.green:C.ink);text(g,240,348,"positive",22);return;}
 if(id==="short-circuit"){const x=+f.metrics.x;rect(g,60,100,250,75,"#eef7fb");text(g,185,145,`Guard x ≠ 0: ${!!x}`,23);arrow(g,310,140,450,140,x?C.green:C.red);rect(g,450,100,260,75,x?"#d3e9dc":"#f3e1e7");text(g,580,145,x?"Evaluate 10/x > 1":"Do not evaluate division",20);text(g,380,270,x?"True left operand permits evaluation of the right operand.":"False left operand bypasses the partial operation.",20);return;}
 if(id==="wraparound-loop"){const n=+f.metrics.Counter;for(let i=0;i<8;i++){const a=2*Math.PI*i/8-Math.PI/2,x=270+105*Math.cos(a),y=180+105*Math.sin(a);dot(g,x,y,20,i===n?C.amber:C.blue);text(g,x,y+7,i,19,"middle","white");}text(g,555,140,"x ← (x + 1) mod 8",24);text(g,555,220,n===0&&p.index>0?"The initial state repeats.":"The state follows a cycle.",21);return;}
 memory(p,g,f,pos);
}
function kmapExact(p,g,f){const s=f.snapshot||{},id=p.scene.id;
 if(id==="km-chart"){const columns=Object.keys(s.owners),patterns=[...new Set(Object.values(s.owners).flat())],x=220,y=90,w=75,h=60;columns.forEach((v,j)=>text(g,x+(j+.5)*w,y-20,`m${v}`,20));patterns.forEach((v,i)=>{text(g,130,y+i*h+35,v,22);columns.forEach((col,j)=>{rect(g,x+j*w,y+i*h,w,h,v===s.candidate?"#fff0ca":"#fff");if(s.owners[col].includes(v))text(g,x+(j+.5)*w,y+i*h+38,"×",25,"middle",s.essentials.includes(v)?C.green:C.blue);});});text(g,380,320,`Essential prime cubes: ${s.essentials.join(", ")}`,22);return;}
 if(id==="km-petrick"){const clauses=[["P","Q"],["P","R"],["Q","R"]];clauses.forEach((c,i)=>{text(g,220,100+i*70,`(${c.join(" + ")})`,27);text(g,515,100+i*70,s.satisfied[i]?"satisfied":"unsatisfied",22,"middle",s.satisfied[i]?C.green:C.red);});text(g,380,315,`Selection {${s.selection}}; cost = ${s.cost[0]} products, ${s.cost[1]} literals`,22);return;}
 if(id==="km-sharing"){const dev=[["AB","AND",["A","B"],210,70],["AC","AND",["A","C"],210,185],["BC","AND",["B","C"],210,290],["F","OR",["AB","AC"],545,110],["G","OR",["AB","BC"],545,245]];network(g,[["A",1,30,40],["B",1,30,155],["C",1,30,290]],dev,["F","G"]);text(g,380,350,`Selected product ${s.product} feeds ${s.outputs.join(" and ")}`,20);g.querySelectorAll(`path[data-net="${s.product}"]`).forEach(e=>e.setAttribute("stroke",C.amber));return;}
 if(id==="km-planes"){const gray=[0,1,3,2];[0,1].forEach((a,panel)=>{const x=110+panel*370; text(g,x+100,45,`Plane A = ${a}`,22);for(let r=0;r<4;r++)for(let j=0;j<4;j++){const v=a*16+gray[r]*4+gray[j];rect(g,x+j*46,70+r*46,46,46,s.rows.includes(v)?"#cce9dc":"#fff");text(g,x+j*46+23,99+r*46,v,19);}text(g,x+100,292,"BC / DE in cyclic Gray order",16);});text(g,380,345,`Cube ${s.pattern}; matching plane cells differ only in A.`,22);return;}
 kmap(p,g,f);
}
function staticDiagram(name){const g=E("svg",{xmlns:NS,viewBox:"0 0 760 360",role:"img","data-schematic":name});
 if(name==="gate-symbols"){["AND","OR","NOR","NAND","XOR","XNOR"].forEach((kind,i)=>{const x=55+(i%3)*240,y=85+Math.floor(i/3)*175,q=gate(g,kind,x,y,kind,"?");q.inputs.forEach(([X,Y])=>path(g,`M${X-25} ${Y}H${X}`));path(g,`M${q.out}h30`);text(g,x+35,y+66,["xy","x + y","¬(x + y)","¬(xy)","x ⊕ y","¬(x ⊕ y)"][i],23);});}
 else if(name==="nand-mux")network(g,[["s",1,30,55],["d0",0,30,145],["d1",1,30,300]],[["not s","NAND",["s","s"],165,65],["p","NAND",["not s","d0"],350,140],["q","NAND",["s","d1"],350,280],["F","NAND",["p","q"],590,210]],["F"]);
 else if(name==="half-subtractor")network(g,[["x",1,30,55],["y",0,30,290]],[["t","NAND",["x","y"],160,170],["u","NAND",["x","t"],330,80],["v","NAND",["y","t"],330,270],["F1","NAND",["u","v"],550,100],["F2","NAND",["v","v"],550,270]],["F1","F2"]);
 else if(name==="factored")network(g,[["a",1,25,35],["b",0,25,78],["c",1,25,121],["d",0,25,164],["e",1,25,207],["f",1,25,250],["g",0,25,305]],[["a+b+c","OR",["a","b","c"],190,90],["d+e","OR",["d","e"],190,215],["product","AND",["a+b+c","d+e","f"],405,170],["F","OR",["product","g"],610,245]],["F"]);
 else if(name==="multi-miter")network(g,[["F0",0,30,55],["G0",0,30,120],["F1",1,30,215],["G1",1,30,285]],[["e0","XOR",["F0","G0"],265,100],["e1","XOR",["F1","G1"],265,255],["M","OR",["e0","e1"],570,175]],["M"]);
 else throw Error(`Unknown static schematic ${name}`);return g;}
function graphExact(p,g,f,pos){const id=p.scene.id,s=f.snapshot||{};
 if(id==="shortest-path-certificate"){const points=[[90,185],[285,65],[465,270],[650,180]],dist=[0,2,3,6],es=[[0,1,2],[0,2,5],[1,2,1],[2,3,3],[1,3,7]],current=f.metrics.Edge;es.forEach(([a,b,w])=>{const A=points[a],B=points[b],d=Math.hypot(B[0]-A[0],B[1]-A[1]),X=A[0]+(B[0]-A[0])*24/d,Y=A[1]+(B[1]-A[1])*24/d,x=B[0]-(B[0]-A[0])*26/d,y=B[1]-(B[1]-A[1])*26/d;arrow(g,X,Y,x,y,current===`${a} to ${b}`?C.amber:C.blue);text(g,(A[0]+B[0])/2+12,(A[1]+B[1])/2-12,`w=${w}`,18);});points.forEach(([x,y],i)=>{dot(g,x,y,23,C.blue);text(g,x,y+7,i,21,"middle","white");text(g,x,y+49,`d${i} = ${dist[i]}`,20);});text(g,380,345,"Tight parent edges: 0 → 1 → 2 → 3; every graph inequality is checked.",18);return;}
 if(id==="transitive-closure"||id==="reflexive-closure"){const xs=[110,290,470,650],y=95,r=22;const tip=(pathEl)=>{const existing=g.querySelector("[id=relation-tip-"+p.index+"]");if(existing){pathEl.setAttribute("marker-end","url(#relation-tip-"+p.index+")");return;}const defs=E("defs"),m=E("marker",{id:"relation-tip-"+p.index,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:"auto",markerUnits:"userSpaceOnUse"});m.append(E("path",{d:"M0 0L7 3L0 6Z",fill:C.blue}));defs.append(m);g.append(defs);pathEl.setAttribute("marker-end","url(#relation-tip-"+p.index+")");};
  s.relation.forEach(([a,b])=>{let d;if(a===b){const t=r/Math.sqrt(2);d=`M${xs[a]-t} ${y-t}C${xs[a]-52} ${y-75} ${xs[a]+52} ${y-75} ${xs[a]+t} ${y-t}`;}else{const left=a<b,x=xs[a]+(left?r:-r),X=xs[b]+(left?-r:r),lane=left?y-30-9*(b-a):y+30+9*(a-b);d=`M${x} ${y}Q${(x+X)/2} ${lane} ${X} ${y}`;}tip(path(g,d,C.blue,1.6));});xs.forEach((x,i)=>{dot(g,x,y,r,i===s.admitted-1?C.amber:C.blue);text(g,x,y+7,i,21,"middle","white");});matrix(g,Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>+s.relation.some(([a,b])=>a===i&&b===j))),245,180,"Reachability matrix");return;}
 if(id==="image-collapse"){const selected=f.metrics["Selected subset"].match(/\d+/g)?.map(Number)||[];[1,2,3].forEach((v,i)=>{dot(g,150,80+i*95,22,selected.includes(v)?C.amber:C.blue);text(g,150,87+i*95,v,22,"middle","white");if(selected.includes(v))arrow(g,173,80+i*95,550,110+(v%2)*120,C.green);});[0,1].forEach((v,i)=>{dot(g,570,110+i*120,23,C.green);text(g,570,117+i*120,v,22,"middle","white");});text(g,150,335,"Selected inputs",21);text(g,570,335,"Distinct parity outputs",21);return;}
 graph(p,g,f,pos);
}
function mergeExact(p,g,f,pos){if(p.scene.id!=="merge"){bars(p,g,f,pos);return;}text(g,510,78,"Left sorted run",21);text(g,510,178,"Right sorted run",21);text(g,380,345,"Stable output: equal keys from the left run precede equal keys from the right.",18);f.nodes.forEach(n=>{const a=pos.get(n.id)||n,v=E("g",{"data-record":n.id,transform:`translate(${a.x} ${a.y})`});rect(v,-41,-24,82,48,n.tone==="active"?"#ffe0a1":n.tone==="done"?"#cce9dc":"#edf6fa");text(v,0,7,n.label,19);g.append(v);p.nodes.set(n.id,v);});}
function legend(p,type){if(!p.legend||p.legend.dataset.visualType===type)return;p.legend.dataset.visualType=type;p.legend.replaceChildren();const entries=type==="circuit"?[[C.green,"Logic 1"],["#8199a6","Logic 0"],["#c1cbd1","Not evaluated yet"]]:type==="cmos"?[[C.green,"Conducting channel"],[C.ink,"Off channel"]]:type==="kmap"?[["#cce9dc","Specified one"],["#ffe0a1","Don't-care cell"],[C.blue,"Colored outlines mark selected cubes"]]:type==="probability"||type==="plot"?[[C.blue,"Probability categories or observations"],[C.green,"Retained mass or quantitative curve"]]:type==="geometry"?[[C.blue,"Labeled geometric object"],[C.amber,"Highlighted vector or point"]]:type==="waveform"?[[C.blue,"Binary signal trace"],[C.green,"Output trace"],[C.amber,"Current time"]]:[[C.blue,"Available object or state"],[C.amber,"Currently inspected"],[C.green,"Processed or established"]];for(const [color,label] of entries){const span=document.createElement("span");span.style.setProperty("--tone",color);span.textContent=label;p.legend.append(span);}}
const routeCache=new Map();
function orthogonalRoute(from,to,boxes,used=[],net=""){const key=JSON.stringify([from,to,boxes,used,net]);if(routeCache.has(key))return routeCache.get(key);const xs=[...new Set([from[0],to[0],from[0]+12,to[0]-14,...boxes.flatMap(b=>[b[0]-14,b[2]+14])].filter(x=>x>=15&&x<=740))].sort((a,b)=>a-b),ys=[...new Set([from[1],to[1],20,340,...boxes.flatMap(b=>[b[1]-13,b[3]+13])].filter(y=>y>=15&&y<=345))].sort((a,b)=>a-b),points=xs.flatMap(x=>ys.map(y=>[x,y])),same=(a,b)=>a[0]===b[0]&&a[1]===b[1],inside=p=>boxes.some(b=>p[0]>b[0]&&p[0]<b[2]&&p[1]>b[1]&&p[1]<b[3]),blocked=(a,c)=>boxes.some(b=>a[1]===c[1]?a[1]>b[1]&&a[1]<b[3]&&Math.max(a[0],c[0])>b[0]&&Math.min(a[0],c[0])<b[2]:a[0]>=b[0]&&a[0]<=b[2]&&Math.max(a[1],c[1])>b[1]&&Math.min(a[1],c[1])<b[3]),start=points.findIndex(p=>same(p,from)),end=points.findIndex(p=>same(p,to));
 if(start<0||end<0)throw Error("A circuit port lies outside the declared routing grid");const dist=new Map(),prev=new Map(),open=[{i:start,d:0,dir:-1,key:start+":-1"}];dist.set(start+":-1",0);let final;
 while(open.length){open.sort((a,b)=>a.d-b.d);const q=open.shift();if(q.d!==dist.get(q.key))continue;if(q.i===end){final=q.key;break;}const ix=Math.floor(q.i/ys.length),iy=q.i%ys.length;for(const [dx,dy,dir] of [[1,0,0],[-1,0,0],[0,1,1],[0,-1,1]]){const X=ix+dx,Y=iy+dy;if(X<0||X>=xs.length||Y<0||Y>=ys.length)continue;const i=X*ys.length+Y,a=points[q.i],b=points[i];if((q.i===start&&dx!==1)||(i===end&&dx!==1)||inside(b)||blocked(a,b)||used.some(u=>u.net!==net&&(a[1]===b[1]&&u.a[1]===u.b[1]&&a[1]===u.a[1]?Math.max(Math.min(a[0],b[0]),Math.min(u.a[0],u.b[0]))<Math.min(Math.max(a[0],b[0]),Math.max(u.a[0],u.b[0])):a[0]===b[0]&&u.a[0]===u.b[0]&&a[0]===u.a[0]?Math.max(Math.min(a[1],b[1]),Math.min(u.a[1],u.b[1]))<Math.min(Math.max(a[1],b[1]),Math.max(u.a[1],u.b[1])):false)))continue;const value=q.d+Math.abs(a[0]-b[0])+Math.abs(a[1]-b[1])+(q.dir!==-1&&q.dir!==dir?24:0),k=i+":"+dir;if(value<(dist.get(k)??Infinity)){dist.set(k,value);prev.set(k,q.key);open.push({i,d:value,dir,key:k});}}}
 if(!final)throw Error("Cannot route a wire without crossing a gate body");const route=[];while(final){route.push(points[+final.split(":")[0]]);final=prev.get(final);}route.reverse();const d=route.map((p,i)=>`${i?"L":"M"}${p}`).join(" ");routeCache.set(key,d);return d;}
function animateDependencies(p){
 const id=p.scene.id,s=p.scene.frames[p.index].snapshot||{},known=id==='comb-dag'?['p','q','r','Y','Z'].slice(0,s.step):id.startsWith('combin-custom-')?null:[];
 if(!known?.length)return;
 const selected=known.at(-1),paths=[...p.canvas.querySelectorAll('path[data-net]')].filter(path=>path.dataset.net===selected);
 for(const route of paths){const length=route.getTotalLength(),dot=E('circle',{r:4,fill:'#bc831c','data-flow-token':'true'}),frames=[];p.canvas.append(dot);for(let i=0;i<=50;i++){const point=route.getPointAtLength(length*i/50);frames.push({transform:`translate(${point.x}px,${point.y}px)`,offset:i/50});}const motion=dot.animate(frames,{duration:1050,easing:'linear',fill:'forwards'});motion.finished.then(()=>dot.remove()).catch(()=>dot.remove());}
}
window.SemanticDiagrams={draw,staticDiagram,animateDependencies};
})();
