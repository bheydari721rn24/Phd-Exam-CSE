function correctnessQuestion(p,g,f){
 const s=f.snapshot;
 const tx=(x,y,v,size=15,color=C.ink)=>{const t=text(g,x,y,v,size,'middle',color);t.style.setProperty('font-size',size+'px','important');t.style.setProperty('font-family','"Source Sans 3"','important');return t;};
 const mt=(x,y,v,size=18)=>{const t=tx(x,y,v,size);t.style.setProperty('font-family','"STIX Two Math"','important');return t;};
 const tip='correctness-tip-'+p.scene.id+'-'+p.index,defs=E('defs');for(const[color,suffix]of [[C.blue,''],[C.red,'-red']]){const marker=E('marker',{id:tip+suffix,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'});marker.append(E('path',{d:'M0 0L7 3L0 6Z',fill:color}));defs.append(marker);}g.append(defs);
 const box=(x,y,v,w=82,h=36,fill='white',size=18)=>{rect(g,x-w/2,y-h/2,w,h,fill,'#91aeba');mt(x,y+6,v,size);return{x,y,w,h};};
 const edge=(A,B,color=C.blue,shift=0)=>{const dx=B.x-A.x,dy=B.y-A.y;if(!dx&&!dy)return;const a=Math.min(A.w/2/Math.abs(dx||1e-20),A.h/2/Math.abs(dy||1e-20)),b=Math.min(B.w/2/Math.abs(dx||1e-20),B.h/2/Math.abs(dy||1e-20)),P=[A.x+a*dx,A.y+a*dy],Q=[B.x-b*dx,B.y-b*dy];if(!dx){P[0]+=shift;Q[0]+=shift;}const route=shift?`M${P}C${P[0]},${P[1]+(Q[1]-P[1])/3} ${Q[0]},${Q[1]-(Q[1]-P[1])/3} ${Q}`:`M${P}L${Q}`;const line=path(g,route,color,1.5);line.setAttribute('marker-end','url(#'+tip+(color===C.red?'-red':'')+')');line.dataset.correctnessPorts=P.concat(Q).join(',');return{P,Q};};
 const row=(a,y,{active=-1,hole=-1,indices=false,colors=[]}={})=>{if(!a.length){tx(380,y+5,'Empty prefix',15);return[];}const width=Math.min(72,650/a.length),start=380-width*(a.length-1)/2;return a.map((v,i)=>{const b=box(start+i*width,y,hole===i?'hole':v,width-7,36,hole===i?'#fbe8e6':colors[i]||(i===active?'#fff0cb':'white'),hole===i?15:18);if(colors.length&&i===active)path(g,`M${b.x-b.w/2+2} ${y-16}H${b.x+b.w/2-2}V${y+16}H${b.x-b.w/2+2}Z`,C.amber,2);if(indices)mt(b.x,y+44,i,14);return b;});};
 const formula=()=>vectorNative(g,f.formulaHtml,22,306,716,48);
 tx(380,24,p.scene.title,17);
 if(s.kind==='merge'){
  tx(380,53,'Left sorted run; yellow is the next head',14);row(s.left,84,{active:s.i});tx(380,128,'Right sorted run; yellow is the next head',14);row(s.right,159,{active:s.j});tx(380,204,'Emitted output, followed by the final tail when exhausted',14);row(s.output,234);tx(380,283,'Head comparisons completed: '+s.comparisons,15);formula();return;
 }
 if(s.kind==='ledger'){
  const cols=s.values.length<=3?s.values.length:3,w=210,start=380-w*(cols-1)/2;
  s.values.forEach((v,i)=>{const x=start+(i%cols)*w,y=112+Math.floor(i/cols)*108;tx(x,y-33,s.labels[i],14);box(x,y,v,w-22,48,i===s.values.length-1?'#eef5f2':'white',String(v).length>17?15:20);});formula();return;
 }
 if(s.kind==='flow'){
  const boxes=s.boxes.map((v,i)=>({x:135+i*245,y:160,w:190,h:66}));for(let i=0;i<boxes.length-1;i++)edge(boxes[i],boxes[i+1]);boxes.forEach((b,i)=>{tx(b.x,106,s.boxes[i].label,14);box(b.x,b.y,s.boxes[i].value,b.w,b.h,i===1?'#edf5f8':'white',String(s.boxes[i].value).length>17?16:20);});tx(380,257,'Read the stated direction and exact role of each block.',14);formula();return;
 }
 if(s.kind==='arrays'){
  s.rows.forEach((v,i)=>{tx(380,66+i*111,v.label,14);row(v.values,105+i*111,v);});formula();return;
 }
 if(s.kind==='numberline'){
  tx(380,59,'Initial integer witnesses; green columns meet the target',14);const width=80,start=380-width*(s.inputs.length-1)/2;s.inputs.forEach((v,i)=>{const x=start+i*width,A=box(x,106,v,60,36,s.valid[i]?'#d7eadf':'#fbe8e6'),B=box(x,218,s.outputs[i],60,36,s.valid[i]?'#d7eadf':'#fbe8e6');edge(A,B);});tx(380,269,'Top: old x · Bottom: guarded final x',15);formula();return;
 }
 if(s.kind==='tree'||s.kind==='graph'){
  const ns=new Map(s.nodes.map(v=>[v.id,{...v,w:s.kind==='graph'?108:86,h:42}]));const es=s.kind==='tree'?s.treeEdges:s.graphEdges;
  es.forEach((v,i)=>{const A=ns.get(v[0]),B=ns.get(v[1]),reverse=es.some(e=>e[0]===v[1]&&e[1]===v[0]);const shift=reverse?(v[0]==='a'?-21:21):0,line=edge(A,B,s.kind==='graph'&&v[3]===false?C.red:C.blue,shift);if(s.kind==='graph'){const x=(line.P[0]+line.Q[0])/2,y=(line.P[1]+line.Q[1])/2;mt(x+(A.x===B.x?(shift<0?-25:25):0),y+(A.y===B.y?-15:0),v[2],17);}});
  s.nodes.forEach(v=>{const b=ns.get(v.id);rect(g,b.x-b.w/2,b.y-b.h/2,b.w,b.h,v.missing?'#f8ece7':'#edf5f8','#91aeba');tx(b.x,b.y-5,v.label,12);mt(b.x,b.y+14,s.kind==='graph'?'d='+v.value:v.value,17);});
  if(s.parentCycle)tx(265,253,'Parent pointers cycle a ↔ b; they never reach s.',14);formula();return;
 }
 if(s.kind==='search'){
  const N=s.values.length,X=v=>80+600*v/Math.max(1,N);tx(380,59,(s.upper?'Upper bound > ':'Lower bound ≥ ')+s.target,15);rect(g,80,95,600,40,'#f7fafb','#91aeba');if(s.lo)rect(g,80,95,X(s.lo)-80,40,'#dceee4','#91aeba');if(s.hi<N)rect(g,X(s.hi),95,680-X(s.hi),40,'#f5edda','#91aeba');
  if(N<=9)s.values.forEach((v,i)=>{if(s.mid===i)rect(g,X(i)+2,98,600/N-4,34,'#ffe7af','#c99831');mt(X(i+.5),121,v,18);});else if(s.mid!==null)dot(g,X(s.mid+.5),115,7,C.amber);
  if(s.lo===s.hi){path(g,`M${X(s.lo)} 88V150`,C.blue,2);mt(X(s.lo),181,'lo=hi='+s.lo,16);}else{path(g,`M${X(s.lo)} 88V150`,C.green,2);path(g,`M${X(s.hi)} 88V150`,C.amber,2);mt(X(s.lo),170,'lo='+s.lo,16);mt(X(s.hi),207,'hi='+s.hi,16);}tx(380,246,s.mid===null?'No midpoint: the unresolved interval is empty.':'mid='+s.mid+'; inspected value='+s.values[s.mid],15);tx(380,281,'Unresolved width '+(s.hi-s.lo)+' · completed bodies '+s.iterations,15);formula();return;
 }
 if(s.kind==='partition'){
  tx(380,61,'Green < pivot · gold = pivot · white unknown · blue > pivot',14);const colors=s.values.map((_,j)=>j<s.lt?'#dceee4':j<s.i?'#fff0cb':j>=s.gt?'#daeaf4':'white');row(s.values,121,{active:s.i<s.gt?s.i:-1,indices:true,colors});
  ['lt','i','gt','pivot'].forEach((v,k)=>{tx(155+k*150,214,v,14);box(155+k*150,246,s[v],86,34,k===1?'#fff0cb':'white');});formula();return;
 }
 if(s.kind==='intervals'){
  tx(380,55,'Horizontal position is time; touching half-open ends are compatible',14);const X=t=>92+t*58;path(g,'M92 79H672','#91aeba',1);for(let i=0;i<=10;i++)mt(X(i),74,i,13);
  s.intervals.forEach((v,i)=>{const x=X(v[0]),w=X(v[1])-x,y=112+i*43;rect(g,x,y,w,26,s.selected.includes(i)?'#d5e9df':'#edf3f6','#91aeba');mt(x+w/2,y+18,'['+v[0]+','+v[1]+')',i===0?17:13);});formula();return;
 }
 throw Error('Unsupported correctness model '+s.kind);
}
