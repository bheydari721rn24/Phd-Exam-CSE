function invariantsQuestion(p,g,f){
 const tx=(...args)=>{const t=text(...args);t.style.setProperty('font-size',String(args[4]??17)+'px','important');t.style.setProperty('font-family','"Source Sans 3"','important');return t;};
 const mt=(x,y,value,size=17)=>{const t=tx(g,x,y,value,size);t.style.setProperty('font-family','"STIX Two Math"','important');return t;};
 const s=f.snapshot,tip='invariants-arrow-'+p.scene.id+'-'+p.index;
 const defs=E('defs'),marker=E('marker',{id:tip,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'});marker.append(E('path',{d:'M0 0L7 3L0 6Z',fill:C.blue}));defs.append(marker);g.append(defs);
 function circle(x,y,label,fill='white',r=16){g.append(E('circle',{cx:x,cy:y,r,fill,stroke:C.ink,'stroke-width':1.4}));mt(x,y+5,label,17);}
 function arrow(A,B,r=16,curve=0){
  let start,end,d;
  if(A[0]===B[0]&&A[1]===B[1]){const v=r/Math.sqrt(2);start=[A[0]-v,A[1]-v];end=[A[0]+v,A[1]-v];d=`M${start}C${A[0]-35} ${A[1]-48} ${A[0]+35} ${A[1]-48} ${end}`;}
  else{const M=[(A[0]+B[0])/2,(A[1]+B[1])/2+curve],da=Math.hypot(M[0]-A[0],M[1]-A[1]),db=Math.hypot(B[0]-M[0],B[1]-M[1]);start=[A[0]+r*(M[0]-A[0])/da,A[1]+r*(M[1]-A[1])/da];end=[B[0]-r*(B[0]-M[0])/db,B[1]-r*(B[1]-M[1])/db];d=`M${start}Q${M} ${end}`;}
  const q=path(g,d,C.blue,1.5);q.setAttribute('marker-end','url(#'+tip+')');q.dataset.invariantsStart=start.join(',');q.dataset.invariantsEnd=end.join(',');
 }
 tx(g,380,22,p.scene.title,18);
 const formula=()=>vectorNative(g,f.formulaHtml,25,297,710,55);
 function cells(values,y,start=55,width=650,selected=-1){const step=width/Math.max(values.length,1);values.forEach((v,i)=>{rect(g,start+i*step,y,step-8,40,i===selected?'#fff0cb':'#edf5f8','#91aeba');mt(start+i*step+(step-8)/2,y+26,v,21);});}
 if(s.kind==='table'){
  const records=s.rowsHtml;booleanTable(g,records,s.headings,35,67,690,205,s.active);tx(g,380,283,s.rows.length>7?'Seven recent rows are shown; earlier checkpoints remain available with Previous.':'Columns retain the named quantities; each row is an exact checkpoint or aggregate.',14);formula();return;
 }
 if(s.kind==='state-graph'){
  const positions=s.nodes.map((_,i)=>[110+(i%3)*270,95+120*Math.floor(i/3)]);
  s.edges.forEach(([a,b])=>arrow(positions[a],positions[b],16,a===2&&b===3?-14:0));
  s.nodes.forEach((label,i)=>circle(...positions[i],label,s.unsafe.includes(label)?'#f8dedc':s.highlight.includes(label)?'#d7eadf':'white'));
  tx(g,380,269,'Green: retained or reached in this step. Red: currently excluded or unsafe.',14);formula();return;
 }
 if(s.kind==='mass-tree'||s.kind==='flat-tree'){
  const children=new Map(s.nodes.map(([id])=>[id,[]]));s.edges.forEach(([a,b])=>children.get(a).push(b));const points=new Map();let leaf=0;
  function place(id,depth){const kids=children.get(id);let x;if(kids.length){const positions=kids.map(k=>place(k,depth+1));x=positions.reduce((a,b)=>a+b,0)/positions.length;}else{x=leaf++;}points.set(id,[x,depth]);return x;}
  place(0,0);const count=Math.max(leaf,2);for(const [id,[x,d]]of points)points.set(id,[leaf===1?380:120+x*520/(count-1),62+d*55]);
  s.edges.forEach(([a,b])=>arrow(points.get(a),points.get(b),15));
  s.nodes.forEach(([id,d])=>{const [x,y]=points.get(id);circle(x,y,s.kind==='flat-tree'?(s.labels[String(id)]??'N'):id,s.selected.includes(id)?'#d7eadf':'white',15);if(s.kind==='mass-tree'&&s.leaves.includes(id)){const parts=s.weights[String(id)].split('/'),value=parts.length===2?'<mfrac><mn>'+parts[0]+'</mn><mn>'+parts[1]+'</mn></mfrac>':'<mn>'+parts[0]+'</mn>';vectorNative(g,'<math xmlns="http://www.w3.org/1998/Math/MathML">'+value+'</math>',x-25,y+20,50,34);}});
  if(s.kind==='flat-tree'){tx(g,380,214,'Current accumulator; the original two-value suffix is shared',16);const a=Array(5-s.accumulator.length).fill('').concat(s.accumulator);cells(a,230);}
  formula();return;
 }
 if(s.kind==='copy-array'){
  tx(g,380,60,'Immutable source array',16);cells(s.source,78,55,650,s.nextSource);s.source.forEach((_,i)=>mt(55+i*650/s.source.length+(650/s.source.length-8)/2,144,i,14));
  tx(g,380,186,'Completed contiguous destination prefix',16);const count=Math.ceil(s.source.length/2),output=Array.from({length:count},(_,i)=>s.output[i]??'');cells(output,204,55,650);output.forEach((_,i)=>mt(55+i*650/count+(650/count-8)/2,266,i,14));
  tx(g,380,282,s.nextSource<0?'Negative source: return before attempting an array access.':'Yellow marks the next valid source index; previous copies remain in order.',14);formula();return;
 }
 if(s.kind==='split-order'){
  tx(g,380,59,'Original input',16);cells(s.source,70);
  if(s.stage>0){tx(g,190,139,'Greater block',16);tx(g,380,139,'Median',16);tx(g,575,139,'Smaller block',16);cells(s.greater,150,70,240);cells([3],150,340,80);cells(s.less,150,455,240);}
  if(s.stage===3){tx(g,380,221,'Returned descending permutation',16);cells(s.output,233);}
  formula();return;
 }
 if(s.kind==='modular-grid'){
  tx(g,540,90,'Five-coordinate residue grid',16);tx(g,540,124,'Green: visited orbit',16);tx(g,540,158,'Red: excluded target',16);tx(g,540,192,'The next wrap is exact modulo five.',14);
  for(let x=0;x<5;x++)for(let y=0;y<5;y++){const X=135+55*x,Y=260-45*y,visited=s.visited.some(v=>v[0]===x&&v[1]===y),bad=s.target[0]===x&&s.target[1]===y;circle(X,Y,'',visited?'#d7eadf':bad?'#f8dedc':'white',8);}
  for(let k=0;k<5;k++){mt(135+55*k,283,k,14);mt(111,265-45*k,k,14);}mt(390,283,'x',16);mt(111,55,'y',16);
  const current=s.visited.at(-1),X=135+55*current[0],Y=260-45*current[1];g.append(E('circle',{cx:X,cy:Y,r:12,fill:'none',stroke:C.blue,'stroke-width':2}));formula();return;
 }
 throw Error('Unreviewed invariants visual kind: '+s.kind);
}
