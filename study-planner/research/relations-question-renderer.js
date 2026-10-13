function relationsQuestion(p,g,f){
 const s=f.snapshot,head=v=>text(g,380,30,v,19),formula=()=>vectorNative(g,f.formulaHtml,25,298,710,55);
 const mt=(x,y,v,size=17)=>{const t=text(g,x,y,v,size);t.setAttribute('font-family','STIX Two Math');return t;};
 if(s.kind==='table'){
  head(p.scene.title);booleanTable(g,s.stage===0?[]:s.rowsHtml,s.headings,35,69,690,185,s.stage===2?-1:0);if(s.stage===0)text(g,380,156,'Read the exact carrier, block sizes and the object being counted.',16);
  text(g,380,283,s.stage===2?'The result counts the stated object; competing quantities remain distinct.':'Each row derives a block, independent choice or witness contribution.',15);formula();return;
 }
 if(s.kind==='matrices'){
  head(p.scene.title);const slot=710/s.matrices.length;
  s.matrices.forEach((m,index)=>{
   const rows=m.values.length,cols=m.values[0].length,dx=Math.min(45,(slot-70)/cols),dy=Math.min(38,182/rows),center=25+(index+.5)*slot,x=center-cols*dx/2+10,y=82;
   text(g,center,55,m.label,15);m.colLabels.forEach((v,j)=>mt(x+(j+.5)*dx,76,v,15));m.rowLabels.forEach((v,i)=>mt(x-21,y+(i+.5)*dy+5,v,15));
   m.html.forEach((row,i)=>row.forEach((v,j)=>{rect(g,x+j*dx,y+i*dy,dx,dy,typeof m.values[i][j]==='number'&&m.values[i][j]>0?'#d7eadf':'#f3f7fa','#bed0d8');vectorNative(g,v,x+j*dx+1,y+i*dy+1,dx-2,dy-2);const fo=g.lastElementChild,body=fo.firstElementChild,math=body.querySelector('math');body.style.padding='0';if(math)math.style.fontSize=(cols>=8?14:16)+'px';}));
  });text(g,380,285,'Rows are sources; columns are targets. Symbols mark choices, not a third truth value.',14);formula();return;
 }
 if(s.kind==='hasse'){
  head(p.scene.title);const r=16,marked=new Set(s.highlight||[]),line=(a,b,color)=>{const A=s.positions[a],B=s.positions[b],dx=B[0]-A[0],dy=B[1]-A[1],d=Math.hypot(dx,dy);path(g,`M${A[0]+r*dx/d} ${A[1]+r*dy/d}L${B[0]-r*dx/d} ${B[1]-r*dy/d}`,color,1.8);};
  if(s.stage>0)s.covers.forEach(([a,b])=>line(a,b,marked.has(a)&&marked.has(b)?C.green:C.blue));
  s.positions.forEach(([x,y],i)=>{g.append(E('circle',{cx:x,cy:y,r,fill:marked.has(i)?'#d7eadf':'white',stroke:marked.has(i)?C.green:C.ink,'stroke-width':1.5}));mt(x,y+5,s.labels[i],17);});
  text(g,380,285,'Greater elements are above. Lines are covers; upward paths encode other comparisons.',14);formula();return;
 }
 if(s.kind==='refinement'){
  head('Containing-block map on the stated example');const ly=[81,157,233],ry=[116,228];
  s.left.forEach((v,i)=>{rect(g,60,ly[i]-25,200,50,'#edf5f8','#91aeba');mt(160,ly[i]+6,v,20);});s.right.forEach((v,i)=>{rect(g,510,ry[i]-25,190,50,'#edf5f8','#91aeba');mt(605,ry[i]+6,v,20);});
  if(s.stage>=1)s.mapping.forEach((j,i)=>arrow(g,260,ly[i],510,ry[j],C.blue));
  text(g,155,54,'R-classes',16);text(g,610,54,'S-classes',16);text(g,380,281,'Three refined source blocks map onto two coarser target blocks.',16);formula();return;
 }
 if(s.kind==='lex'){
  head('One legal lexicographically decreasing recursion branch');rect(g,55,91,270,114,'#edf5f8','#91aeba');rect(g,435,91,270,114,'#d7eadf','#91aeba');text(g,190,78,s.stage?'preceding arguments':'initial arguments',16);text(g,570,78,'current arguments',16);vectorNative(g,s.beforeHtml,70,124,240,50);vectorNative(g,s.afterHtml,450,124,240,50);if(s.stage)arrow(g,325,148,435,148,C.blue);text(g,380,248,s.stage&&s.after[0]<s.before[0]?'The first coordinate decreases; the second may increase.':s.stage?'The first coordinate is fixed; the second decreases by two.':'The finite illustration starts at the explicitly declared pair (2,3).',16);formula();return;
 }
 throw Error('Unknown relation geometry '+s.kind);
}
