function algorithmRecurrenceQuestion(p,g,f){
 const s=f.snapshot;
 if(s.kind==='table')return invariantsQuestion(p,g,f);
 const tx=(x,y,v,size=16,color=C.ink)=>{const t=text(g,x,y,v,size,'middle',color);t.style.setProperty('font-size',size+'px','important');t.style.setProperty('font-family','"Source Sans 3"','important');return t;};
 const mt=(x,y,v,size=17,color=C.ink)=>{const t=tx(x,y,v,size,color);t.style.setProperty('font-family','"STIX Two Math"','important');return t;};
 const tip='recurrence-tip-'+p.scene.id+'-'+p.index,defs=E('defs'),marker=E('marker',{id:tip,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'});marker.append(E('path',{d:'M0 0L7 3L0 6Z',fill:C.blue}));defs.append(marker);g.append(defs);
 const box=(x,y,v,fill='white',w=74,h=28)=>{rect(g,x-w/2,y-h/2,w,h,fill,'#91aeba');mt(x,y+6,v,17);return{x,y,w,h};};
 const edge=(A,B,dashed=false)=>{const dx=B.x-A.x,dy=B.y-A.y,L=Math.hypot(dx,dy);if(!L)return;const a=Math.min((A.w/2)/Math.abs(dx||1e-20),(A.h/2)/Math.abs(dy||1e-20)),b=Math.min((B.w/2)/Math.abs(dx||1e-20),(B.h/2)/Math.abs(dy||1e-20)),P=[A.x+a*dx,A.y+a*dy],Q=[B.x-b*dx,B.y-b*dy],e=path(g,`M${P}L${Q}`,C.blue,1.5);e.setAttribute('marker-end','url(#'+tip+')');if(dashed)e.setAttribute('stroke-dasharray','4 4');e.dataset.recurrencePorts=P.concat(Q).join(',');};
 const circle=(x,y,v,fill='white',r=17)=>{g.append(E('circle',{cx:x,cy:y,r,fill,stroke:C.blue,'stroke-width':1.4}));mt(x,y+6,v,18);return{x,y,w:2*r,h:2*r};};
 const formula=()=>vectorNative(g,f.formulaHtml,20,304,720,48);
 tx(380,22,p.scene.title,17);
 if(s.kind==='level-work'){
  tx(380,44,s.labelsAreLogSizes?'Illustrative first split; labels are logarithmic sizes':'Illustrative first split; complete levels are counted below',14);
  const A={x:380,y:70,w:86,h:28},kids=Array.from({length:s.a},(_,i)=>({x:s.a===1?380:90+i*580/(s.a-1),y:124,w:86,h:28}));kids.forEach(B=>edge(A,B));box(A.x,A.y,s.N,s.level===0?'#fff0cb':'white',86);kids.forEach(B=>box(B.x,B.y,s.N/s.b,s.level===1?'#fff0cb':'white',86));
  const rows=s.rows.slice(-4),heads=['depth','nodes','size','local toll','level cost','sum'];heads.forEach((v,i)=>tx(67+i*125,163,v,13));
  rows.forEach((r,j)=>r.forEach((v,i)=>{rect(g,12+i*125,173+j*25,113,24,j===rows.length-1?'#e0eee8':'#f0f5f7','#ccd8de');mt(68+i*125,190+j*25,v,String(v).length>8?13:16);}));
  tx(380,287,`Complete depth ${s.level} of ${s.h}; earlier rows remain in Previous.`,14);formula();return;
 }
 if(s.kind==='chain'){
  const start=s.windowStart,visible=s.values.slice(start,start+5),positions=visible.map((_,j)=>({x:90+j*145,y:130,w:90,h:38}));positions.slice(1).forEach((B,j)=>edge(positions[j],B));positions.forEach((P,j)=>box(P.x,P.y,visible[j],start+j===s.index?'#fff0cb':'white',90,38));
  visible.forEach((_,j)=>{tx(positions[j].x,89,'state '+(start+j),14);mt(positions[j].x,193,s.tolls[start+j],17);});tx(380,64,`Shown states ${start}–${start+visible.length-1} of ${s.values.length-1}`,14);tx(380,221,'Local costs, including the separately declared base',15);tx(380,261,'Accumulated cost through the highlighted state',15);mt(380,288,s.total,20);formula();return;
 }
 if(s.kind==='unequal'){
  const P=[{x:380,y:65},{x:230,y:118},{x:530,y:118},{x:125,y:171},{x:300,y:171},{x:480,y:171},{x:650,y:171}].map(v=>({...v,w:64,h:28}));s.shown.slice(1).forEach(n=>edge(P[n.parent],P[n.id]));s.shown.forEach(n=>box(P[n.id].x,P[n.id].y,n.size,n.depth===s.depth?'#fff0cb':'white',64));
  tx(380,213,'Only the first two depths are drawn; the full frontier is counted.',14);tx(225,244,'Complete depth');mt(530,244,s.depth,20);tx(225,276,s.quadratic?'Sum of squared sizes':'Sum of sizes');mt(530,276,s.total,20);formula();return;
 }
 if(s.kind==='pivot'){
  tx(380,63,'Nine sampled keys; median is the fifth ordered sample key',15);
  for(let i=0;i<9;i++){const x=86+i*75;rect(g,x-30,87,60,41,s.stage>=1&&i===4?'#fff0cb':s.stage>=2?(i<4?'#deedf5':i>4?'#e0eee8':'#fff0cb'):'white','#91aeba');mt(x,113,i+1,20);}
  tx(380,165,'Permitted global ranks among sixteen distinct keys',15);
  const X=r=>72+(r-1)*41;path(g,`M${X(1)} 218H${X(16)}`,C.blue,1.5);
  for(let r=1;r<=16;r++){g.append(E('circle',{cx:X(r),cy:218,r:8,fill:s.stage>=3&&r>=s.left&&r<=s.right?'#b9ddcb':'#eef3f6',stroke:'#91aeba'}));mt(X(r),252,r,14);}
  tx(380,286,'Green ranks are possible; they are not all realized by one input.',14);formula();return;
 }
 if(s.kind==='parity'){
  const P=[{x:190,y:115,w:90,h:38},{x:380,y:115,w:90,h:38},{x:570,y:115,w:90,h:38}];edge(P[0],P[1]);edge(P[1],P[2]);
  const q=path(g,'M570 96C570 53 190 53 190 96',C.blue,1.5);q.setAttribute('marker-end','url(#'+tip+')');q.dataset.recurrenceCurvePorts='570,96,190,96';['(1,1)','(1,0)','(0,1)'].forEach((v,i)=>box(P[i].x,P[i].y,v,(s.index-16)%3===i?'#fff0cb':'white',90,38));
  tx(380,163,'Anchored at indices sixteen and seventeen: both odd',15);
  s.requested.forEach((n,i)=>{const x=71+i*47;rect(g,x-20,198,40,36,n===s.index?'#fff0cb':n%3===0?'#d7eadf':'white','#91aeba');mt(x,222,n,15);});
  tx(380,270,'Green indices are even; yellow is the inspected requested index.',14);formula();return;
 }
 if(s.kind==='fib'){
  const P=Array.from({length:8},(_,i)=>({x:65+90*i,y:175,w:34,h:34}));
  for(let k=2;k<=7;k++){
   // Adjacent dependency clips to the circular ports rather than rectangle corners.
   const e=path(g,`M${P[k].x-17} 175H${P[k-1].x+17}`,C.blue,1.4);e.setAttribute('marker-end','url(#'+tip+')');
   const v=17/Math.sqrt(2),A=[P[k].x-v,175-v],B=[P[k-2].x+v,175-v],q=path(g,`M${A}C${A[0]-30} 87 ${B[0]+30} 87 ${B}`,C.blue,1.2);q.setAttribute('marker-end','url(#'+tip+')');q.dataset.recurrenceCurvePorts=A.concat(B).join(',');
  }
  P.forEach((v,k)=>circle(v.x,v.y,k,k<=s.evaluated?'#d7eadf':'white'));tx(380,64,'Dependency edges point toward the required smaller states',15);tx(380,221,'Each state is evaluated once with memoization',15);tx(380,276,'The formula below counts naive calls separately',15);formula();return;
 }
 if(s.kind==='reuse'){
  const P=s.values.map((_,i)=>({x:65+125*i,y:132,w:86,h:38}));P.slice(1).forEach((v,i)=>edge(P[i],v));P.forEach((v,i)=>box(v.x,v.y,s.values[i],i<=s.index?'#d7eadf':'white',86,38));
  const q=path(g,'M65 113C65 61 190 61 190 113',C.blue,1.3);q.setAttribute('marker-end','url(#'+tip+')');q.setAttribute('stroke-dasharray','4 4');q.dataset.recurrenceCurvePorts='65,113,190,113';tx(380,61,'Dashed: second request reuses the first child result',14);
  P.forEach((v,i)=>mt(v.x,208,s.tolls[i],18));tx(380,245,'Local cost at each actually executed state',15);tx(380,281,'Six executed states; the reused request is not a new child.',14);formula();return;
 }
 if(s.kind==='weighted'){
  const A={x:380,y:72,w:70,h:30},P=s.children.map((_,i)=>({x:92+i*144,y:165,w:70,h:30}));P.forEach(v=>edge(A,v));box(380,72,6,'white',70,30);P.forEach((v,i)=>{box(v.x,v.y,s.children[i],i<s.stage?'#d7eadf':'white',70,30);mt(v.x,225,s.children[i]**2,19);});tx(380,119,'Two halves; three thirds',15);tx(380,267,'Each lower value is that child size squared.',15);formula();return;
 }
 if(s.kind==='expectation'){
  tx(380,64,'Uniform pivot ranks and their actual larger-child sizes',15);
  for(let i=0;i<4;i++){const x=135+i*163;rect(g,x-62,90,124,112,i<s.inspected?'#dcecf3':'white','#91aeba');tx(x,114,'rank',14);mt(x,140,s.ranks[i],19);tx(x,166,'child size',14);mt(x,190,s.sizes[i],22);mt(x,235,'1/4',18);}
  tx(380,278,'Each outcome has probability one-quarter.',15);formula();return;
 }
 if(s.kind==='merge-tree'){
  const kids=new Map(s.nodes.map(n=>[n.id,[]]));s.nodes.filter(n=>n.parent!==null).forEach(n=>kids.get(n.parent).push(n.id));const P=new Map();let next=0;
  const place=id=>{const list=kids.get(id),x=list.length?list.map(place).reduce((a,b)=>a+b,0)/list.length:next++;P.set(id,{x:48+x*55,y:63+s.nodes[id].depth*44,w:32,h:24});return x;};place(0);
  s.nodes.filter(n=>n.parent!==null).forEach(n=>edge(P.get(n.parent),P.get(n.id)));s.nodes.forEach(n=>{const v=P.get(n.id);box(v.x,v.y,n.size,n.depth===s.depth?'#dcecf3':'white',32,24);});
  tx(380,280,`Depth ${s.depth}: size toll ${s.levels[s.depth].sizeToll}; comparisons ${s.levels[s.depth].comparisons}`,15);formula();return;
 }
 throw Error('Unsupported recurrence model '+s.kind);
}
