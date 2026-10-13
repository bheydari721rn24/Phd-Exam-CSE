function functionsQuestion(p,g,f){
 const tx=(...args)=>{const t=text(...args);t.style.setProperty('font-size',String(args[4]??17)+'px','important');t.style.setProperty('font-family','"Source Sans 3"','important');return t;};
 const s=f.snapshot,mt=(x,y,v,size=17)=>{const t=tx(g,x,y,v,size);t.style.setProperty('font-family','STIX Two Math','important');return t;};
 const formula=()=>vectorNative(g,f.formulaHtml,25,298,710,55),head=()=>tx(g,380,22,p.scene.title,18);
 const tip='functions-arrow-'+p.scene.id+'-'+p.index;
 function definitions(){const d=E('defs'),m=E('marker',{id:tip,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'});m.append(E('path',{d:'M0 0L7 3L0 6Z',fill:C.blue}));d.append(m);g.append(d);}
 function dotAt(A,label,fill='white',r=16){g.append(E('circle',{cx:A[0],cy:A[1],r,fill,stroke:C.ink,'stroke-width':1.4}));mt(A[0],A[1]+5,label,17);}
 function wire(A,B,r=16,bend=0,color=C.blue,targetRadius=r){
  let d,start,end;
  if(A===B||A[0]===B[0]&&A[1]===B[1]){const h=r/Math.sqrt(2);start=[A[0]-h,A[1]-h];end=[A[0]+h,A[1]-h];d=`M${start}C${A[0]-37} ${A[1]-49} ${A[0]+37} ${A[1]-49} ${end}`;}
  else{const c=[(A[0]+B[0])/2,(A[1]+B[1])/2+bend],u=Math.hypot(c[0]-A[0],c[1]-A[1]),v=Math.hypot(B[0]-c[0],B[1]-c[1]);start=[A[0]+r*(c[0]-A[0])/u,A[1]+r*(c[1]-A[1])/u];end=[B[0]-targetRadius*(B[0]-c[0])/v,B[1]-targetRadius*(B[1]-c[1])/v];d=`M${start}Q${c} ${end}`;}
  const q=path(g,d,color,1.5);q.setAttribute('marker-end','url(#'+tip+')');q.dataset.functionStart=start.join(',');q.dataset.functionEnd=end.join(',');
 }
 const column=(n,x)=>Array.from({length:n},(_,i)=>[x,n===1?170:(n>5?75:90)+i*(n>5?175:155)/(n-1)]);
 if(s.kind==='table'){
  head();booleanTable(g,s.rowsHtml,s.headings,35,68,690,203,s.active);tx(g,380,284,p.scene.id==='functions-question-quantified-cycle'?'One means true, zero means false. Check all three rows for each fixed input.':'Each row counts the specified object; labels and constraints remain fixed.',14);formula();return;
 }
 if(s.kind==='sequence'){
  head();const n=s.values.length,w=Math.min(90,680/n),start=380-n*w/2;
  s.values.forEach((v,i)=>{rect(g,start+i*w,97,w-6,58,s.endpointFixed&&(i===0||i===n-1)?'#d7eadf':'#edf5f8','#91aeba');mt(start+i*w+(w-6)/2,134,v,23);mt(start+i*w+(w-6)/2,180,i+1,15);});
  tx(g,380,75,'Function values in increasing input order',16);tx(g,380,203,'Input positions are shown below; repeated outputs are permitted.',14);
  const html='<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mi>c</mi><mo>=</mo><mo>(</mo>'+s.counts.map((n,i)=>(i?'<mo>,</mo>':'')+'<mn>'+n+'</mn>').join('')+'<mo>)</mo></mrow></math>';vectorNative(g,html,55,227,650,46);formula();return;
 }
 if(s.kind==='map'||s.kind==='subsets'){
  head();definitions();const A=column(s.source.length,170),n=s.target.length,B=n<=7?column(n,585):Array.from({length:n},(_,i)=>[475+83*(i%3),91+52*Math.floor(i/3)]);
  const ra=s.source.length>5?12:16,rb=n>5&&n<=7?12:16;tx(g,170,50,'Domain',16);tx(g,585,50,'Codomain',16);
  s.values.forEach((j,i)=>{if(s.kind==='subsets'||i<s.stage)wire(A[i],B[j],ra,0,s.selected?.includes(i)?C.green:C.blue,rb);});
  A.forEach((a,i)=>dotAt(a,s.source[i],s.selected?.includes(i)?'#d7eadf':'white',ra));B.forEach((b,j)=>dotAt(b,s.target[j],s.targetSelected?.includes(j)?'#d7eadf':'white',rb));
  tx(g,380,287,s.kind==='subsets'?'Green marks the selected input or target subset.':'One arrow per processed input; unprocessed inputs have not yet been assigned.',14);formula();return;
 }
 if(s.kind==='endofunction'){
  head();definitions();const n=s.values.length;let points;
  if(s.cycleGroups){points=[];s.cycleGroups.forEach((group,j)=>group.forEach((i,k)=>points[i]=[230+305*j+77*Math.cos(2*Math.PI*k/group.length-Math.PI/2),170+77*Math.sin(2*Math.PI*k/group.length-Math.PI/2)]));}
  else if(s.cyclic)points=Array.from({length:n},(_,i)=>[380+145*Math.cos(2*Math.PI*i/n-Math.PI/2),170+88*Math.sin(2*Math.PI*i/n-Math.PI/2)]);
  else points=Array.from({length:n},(_,i)=>[110+180*(i%4),n<=4?170:100+130*Math.floor(i/4)]);
  s.values.forEach((j,i)=>wire(points[i],points[j],16,i!==j&&points[i][1]===points[j][1]?-65:0));points.forEach((a,i)=>dotAt(a,i,s.fixed?.includes(i)?'#d7eadf':'white'));
  tx(g,380,285,s.cyclic?'Every arrow is an actual successor; rotations retain the same values.':'Each vertex has exactly one outgoing assignment. Green marks fixed points when specified.',14);formula();return;
 }
 if(s.kind==='sections'){
  head();definitions();const A=[[90,85],[90,160],[90,235]];
  s.fibers.forEach((fiber,i)=>{const y=A[i][1],w=Math.min(58,440/fiber.length),x=276;
   rect(g,249,y-28,461,57,'#f3f7fa','#bed0d8');dotAt(A[i],String.fromCharCode(97+i));
   fiber.forEach((v,j)=>{const X=x+j*w;rect(g,X,y-19,w-7,38,s.selected[i]===v?'#d7eadf':'white','#bed0d8');mt(X+(w-7)/2,y+6,v,17);});
   const index=fiber.indexOf(s.selected[i]),xEnd=x+index*w+(w-7)/2;const q=path(g,`M${A[i][0]} ${y-16}V${y-35}H${xEnd}V${y-19}`,C.blue,1.5);q.setAttribute('marker-end','url(#'+tip+')');
  });tx(g,380,285,'Each reverse arrow chooses one member of its own displayed fiber.',14);formula();return;
 }
 if(s.kind==='composition'){
  head();definitions();const A=column(s.source.length,112),B=column(s.middle.length,380),D=column(s.target.length,649),rb=s.middle.length>5?12:16;mt(112,50,'A',16);mt(380,50,'B',16);tx(g,649,50,'Target',16);tx(g,246,70,'inner map',14);tx(g,514,70,'outer map',14);
  s.inner.forEach((j,i)=>wire(A[i],B[j],16,0,C.blue,rb));s.outer.forEach((j,i)=>wire(B[i],D[j],rb,0,C.blue,16));A.forEach((a,i)=>dotAt(a,s.source[i]));B.forEach((a,i)=>dotAt(a,s.middle[i],s.inner.includes(i)?'#d7eadf':'white',rb));D.forEach((a,i)=>dotAt(a,s.target[i]));
  tx(g,380,285,'Follow the inner arrow first, then the outer arrow at its actual middle value.',14);formula();return;
 }
 if(s.kind==='parabola'){
  head();definitions();const x=v=>100+90*(v+1),y=v=>260-20*(v-3);
  path(g,'M85 66V260M100 270H672',C.ink,1.2);mt(75,55,'y',16);mt(690,276,'x',16);
  [3,7,12].forEach(v=>{path(g,`M80 ${y(v)}H90`,C.ink,1);mt(65,y(v)+5,v,15);});[-1,0,2,4,5].forEach(v=>{path(g,`M${x(v)} 266V274`,C.ink,1);mt(x(v),292,v,15);});
  path(g,`M${x(-1)} ${y(12)}Q${x(.5)} ${y(3)} ${x(2)} ${y(3)}`,C.blue,2);path(g,`M${x(2)} ${y(3)}Q${x(3.5)} ${y(3)} ${x(5)} ${y(12)}`,s.stage?'#a9bac3':C.blue,2);
  if(s.stage===0){path(g,`M${x(0)} ${y(7)}H${x(4)}`,'#b58132',1.3);dotAt([x(0),y(7)],'', '#fff0ce',5);dotAt([x(4),y(7)],'','#fff0ce',5);tx(g,380,65,'Inputs 0 and 4 both produce output 7.',15);}
  else tx(g,380,65,'Blue retains the left branch; vertical values range from three to twelve.',15);
  formula();return;
 }
 throw Error('Unknown exact function drawing '+s.kind);
}
