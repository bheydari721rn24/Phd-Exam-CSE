function discreteNumberQuestion(p,g,f){
 const s=f.snapshot;
 if(s.kind==='table')return invariantsQuestion(p,g,f);
 const tx=(x,y,v,size=17,color=C.ink)=>{const t=text(g,x,y,v,size,'middle',color);t.style.setProperty('font-size',size+'px','important');t.style.setProperty('font-family','"Source Sans 3"','important');return t;};
 const mt=(x,y,v,size=17,color=C.ink)=>{const t=tx(x,y,v,size,color);t.style.setProperty('font-family','"STIX Two Math"','important');return t;};
 const formula=()=>vectorNative(g,f.formulaHtml,20,295,720,56);
 const cell=(x,y,w,h,v,fill='white',size=17)=>{rect(g,x,y,w,h,fill,'#9eb5c0');mt(x+w/2,y+h/2+size*.32,v,size);};
 tx(380,18,p.scene.title,17);
 if(s.kind==='residue-grid'){
  const cols=Math.min(12,s.values.length),rows=Math.ceil(s.values.length/cols),w=660/cols,h=Math.min(44,192/rows);
  s.values.forEach((v,i)=>{const known=i<s.inspected,ok=s.accepted.includes(v);cell(50+(i%cols)*w,65+Math.floor(i/cols)*h,w-6,h-5,s.labels[i],known?(ok?'#d7eadf':'#f4dfe3'):'#f1f5f7',s.labels[i].length>6?13:17);});
  tx(380,279,`${s.inspected} inspected; ${s.values.slice(0,s.inspected).filter(v=>s.accepted.includes(v)).length} admitted in the displayed domain`,15);formula();return;
 }
 if(s.kind==='exponent-grid'){
  tx(380,53,'Selection j; exponent 3j−15; number of factor choices',16);
  s.exponents.forEach((v,i)=>{const x=55+(i%8)*83,y=80+Math.floor(i/8)*91;rect(g,x,y,73,76,i===s.j?'#fff0cb':'#eef5f7','#9eb5c0');mt(x+36.5,y+20,i,15);mt(x+36.5,y+44,v,20);mt(x+36.5,y+65,s.coefficients[i],14);});
  tx(380,279,'Target exponent fourteen is absent from the entire lattice.',15);formula();return;
 }
 if(s.kind==='crt-grid'){
  const d=(a,b)=>b?d(b,a%b):a,G=d(s.m,s.n),r=s.target[0]%G,cols=Array.from({length:s.m/G},(_,i)=>r+G*i),allRows=Array.from({length:s.n/G},(_,i)=>r+G*i),first=allRows.length>6&&s.inspected>1&&s.inspected<s.period?allRows.length-5:0,rows=allRows.length>6?allRows.slice(first,first+5):allRows,w=Math.min(83,620/cols.length),h=Math.min(45,192/rows.length),X=(760-cols.length*w)/2,Y=77;
  tx(380,45,`Shared residue ${r} mod ${G}; columns mod ${s.m}; rows mod ${s.n}`,14);
  cols.forEach((v,j)=>mt(X+j*w+w/2,Y-12,v,14));rows.forEach((v,i)=>mt(X-23,Y+i*h+h*.65,v,14));
  rows.forEach((b,i)=>cols.forEach((a,j)=>{const hit=s.pairs.find(q=>q[0]===a&&q[1]===b),target=a===s.target[0]&&b===s.target[1],seen=hit&&hit[2]<s.inspected;cell(X+j*w,Y+i*h,w-3,h-3,seen?hit[2]:'·',target?'#fff0cb':seen?'#dcecf3':'#f5f7f8',17);}));
  tx(380,283,allRows.length>6?`Rows ${first+1}–${first+rows.length} of ${allRows.length}; other windows remain in previous checkpoints.`:`Each occupied cell contains its unique x modulo ${s.period}.`,13);formula();return;
 }
 if(s.kind==='prime-grid'){
  // Half-coordinate compression makes a large square grid legible; odd cells are excluded by the written parity proof.
  const xs=s.square?Array.from({length:Math.floor(s.maxI/2)+1},(_,i)=>2*i):Array.from({length:s.maxI+1},(_,i)=>i),ys=s.square?Array.from({length:Math.floor(s.maxJ/2)+1},(_,i)=>2*i):Array.from({length:s.maxJ+1},(_,i)=>i),w=Math.min(65,600/xs.length),h=Math.min(52,168/ys.length),X=(760-xs.length*w)/2,Y=88;
  tx(380,44,s.square?'Even-exponent pairs; each has two five-coordinate lifts.':'Columns: two-exponent. Rows: three-exponent. One divisor per cell.',13);
  xs.forEach((v,i)=>mt(X+i*w+w/2,Y-15,v,13));ys.forEach((v,i)=>mt(X-22,Y+i*h+h*.65,v,13));
  ys.forEach((j,r)=>xs.forEach((i,c)=>{const index=s.coords.findIndex(q=>q[0]===i&&q[1]===j),seen=index<s.inspected;rect(g,X+c*w,Y+r*h,w-4,h-4,seen?'#b9ddcb':'#f0f5f7','#9eb5c0');}));
  tx(380,280,s.square?'Green: inspected even pairs. Odd exponent pairs are excluded.':'Green: inspected pairs. Zero-exponent row and column are included.',15);formula();return;
 }
 const tip='discrete-number-tip-'+p.scene.id+'-'+p.index;const defs=E('defs'),marker=E('marker',{id:tip,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'});marker.append(E('path',{d:'M0 0L7 3L0 6Z',fill:C.blue}));defs.append(marker);g.append(defs);
 const arrow=(a,b,r=16)=>{const dx=b[0]-a[0],dy=b[1]-a[1],L=Math.hypot(dx,dy),A=[a[0]+r*dx/L,a[1]+r*dy/L],B=[b[0]-r*dx/L,b[1]-r*dy/L],q=path(g,`M${A}L${B}`,C.blue,1.5);q.setAttribute('marker-end','url(#'+tip+')');q.dataset.numberPorts=A.concat(B).join(',');};
 if(s.kind==='power-orbit'){
  const coords=s.values.map((_,i)=>{const row=Math.floor(i/3),col=i%3;return[150+(row%2?2-col:col)*230,85+row*77];});
  for(let i=1;i<coords.length;i++)arrow(coords[i-1],coords[i]);
  coords.forEach(([x,y],i)=>{g.append(E('circle',{cx:x,cy:y,r:16,fill:i===s.active?'#fff0cb':i<s.active?'#d7eadf':'white',stroke:C.blue,'stroke-width':1.4}));mt(x,y+6,s.values[i],18);const labelX=i>0&&i%3===0?x+(x>380?37:-37):x;mt(labelX,y-25,'k='+i,14);});
  tx(380,281,'Each arrow multiplies by the fixed base; exponent zero is included.',15);formula();return;
 }
 if(s.kind==='integer-line'){
  const X=x=>120+(x+3)*28,Y=y=>240-(y+5)*15;
  path(g,'M100 165H680',C.blue,1);path(g,'M204 270V65',C.blue,1);mt(687,170,'x',17);mt(204,57,'y',17);
  const a=s.points[0],b=s.points[s.points.length-1];path(g,`M${X(a[0])} ${Y(a[1])}L${X(b[0])} ${Y(b[1])}`,C.blue,1.5);
  s.points.forEach(([x,y],i)=>{const u=X(x),v=Y(y);g.append(E('circle',{cx:u,cy:v,r:8,fill:i===s.active?'#ffe1a3':s.accepted.includes(i)?'#d7eadf':'#f4dfe3',stroke:C.blue,'stroke-width':1.2}));mt(u,v-15,'('+x+','+y+')',14);});
  tx(380,281,'Green points satisfy the x bounds; a negative y can be allowed.',15);formula();return;
 }
 if(s.kind==='prime-vectors'){
  const names=['first operand','second operand','gcd minima','lcm maxima'];['object','two-exponent','three-exponent'].forEach((v,i)=>tx(150+i*235,65,v,16));
  s.vectors.forEach((v,i)=>{if(i===s.active)rect(g,35,87+i*44,690,39,'#fff0cb','none');tx(150,113+i*44,names[i],17);mt(385,113+i*44,v[0],21);mt(620,113+i*44,v[1],21);});formula();return;
 }
 throw Error('Unknown discrete number model '+s.kind);
}
