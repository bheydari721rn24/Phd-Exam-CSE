function divideQuestion(p,g,f){
 const s=f.snapshot;if(s.kind==='table')return invariantsQuestion(p,g,f);
 const tx=(x,y,v,size=15,color=C.ink)=>{const t=text(g,x,y,v,size,'middle',color);t.style.setProperty('font-size',size+'px','important');t.style.setProperty('font-family','"Source Sans 3"','important');return t;};
 const mt=(x,y,v,size=18)=>{const t=tx(x,y,v,size);t.style.setProperty('font-family','"STIX Two Math"','important');return t;};
 const tip='divide-tip-'+p.scene.id+'-'+p.index,defs=E('defs'),marker=E('marker',{id:tip,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'});marker.append(E('path',{d:'M0 0L7 3L0 6Z',fill:C.blue}));defs.append(marker);g.append(defs);
 const box=(x,y,v,w=70,h=32,fill='white')=>{rect(g,x-w/2,y-h/2,w,h,fill,'#91aeba');mt(x,y+6,v,String(v).length>12?13:18);return{x,y,w,h};};
 const edge=(A,B)=>{const dx=B.x-A.x,dy=B.y-A.y;if(!dx&&!dy)return;const a=Math.min(A.w/2/Math.abs(dx||1e-20),A.h/2/Math.abs(dy||1e-20)),b=Math.min(B.w/2/Math.abs(dx||1e-20),B.h/2/Math.abs(dy||1e-20)),P=[A.x+a*dx,A.y+a*dy],Q=[B.x-b*dx,B.y-b*dy],e=path(g,`M${P}L${Q}`,C.blue,1.4);e.setAttribute('marker-end','url(#'+tip+')');e.dataset.dividePorts=P.concat(Q).join(',');};
 const formula=()=>vectorNative(g,f.formulaHtml,22,306,716,48);
 const row=(a,y,highlight=-1,offset=0)=>{const width=Math.min(68,620/Math.max(a.length,1));const start=380-width*(a.length-1)/2;return a.map((v,i)=>box(start+i*width,y,v,width-8,32,i===highlight?'#fff0cb':i<offset?'#e0eee8':'white'));};
 tx(380,24,p.scene.title,17);
 if(s.kind==='merge'){
  tx(380,54,'Sorted left run; next head is yellow',14);row(s.left,81,s.i,s.i);tx(380,123,'Sorted right run; next head is yellow',14);row(s.right,150,s.j,s.j);tx(380,192,'Consumed output in stable order',14);row(s.output,219);
  tx(205,269,'Current merge comparisons: '+s.comparisons,14);tx(558,269,'Strict cross inversions: '+s.charge,14);if(s.totalComparisons!==undefined)tx(380,293,'All merges so far: '+s.totalComparisons+' comparisons',14);formula();return;
 }
 if(s.kind==='summary'){
  tx(380,55,'Input; green cells form the declared best witness',14);const P=row(s.input,83);P.forEach((v,i)=>{if(i>=s.witness[0]&&i<s.witness[1]){const el=g.querySelectorAll('rect')[i];el.setAttribute('fill','#d7eadf');}});const cut=(P[s.split-1].x+P[s.split].x)/2;path(g,`M${cut} 61V107`,'#ad664c',2);
  const names=['total','prefix','suffix','best'];tx(80,132,'interval',14);names.forEach((v,i)=>tx(250+i*135,132,v,14));['left','right','combined'].forEach((v,j)=>{tx(80,170+j*45,v,15);[s.left,s.right,s.combined][j].forEach((n,i)=>box(250+i*135,164+j*45,i<s.reveal?n:'?',102,30,j===2?'#e0eee8':'white'));});formula();return;
 }
 if(s.kind==='radix'){
  tx(380,55,`Operands ${s.x} and ${s.y}; low width ${s.m}`,15);s.parts.forEach((v,i)=>box(155+i*150,90,v,94));['x high','x low','y high','y low'].forEach((v,i)=>tx(155+i*150,126,v,14));
  ['high product','low product','sum product','mixed term'].forEach((v,i)=>{tx(155+i*150,174,v,14);box(155+i*150,207,i<s.stage?s.products[i]:'?',94,38,i===3?'#fff0cb':'white');});tx(380,274,`Radix shifts: ${s.base} and ${s.base*s.base}; restore operand sign.`,15);formula();return;
 }
 if(s.kind==='blocks'){
  tx(380,54,'Seven scalar blocks; negative values preserve cancellation',14);s.products.forEach((v,i)=>{tx(80+i*100,83,'M'+(i+1),14);box(80+i*100,112,i<s.stage?v:'?',78);});
  tx(380,165,'Output blocks match the independently computed dot products',14);s.outputs.forEach((v,i)=>box(308+(i%2)*145,202+Math.floor(i/2)*53,s.stage===8?v:'?',114,40,'#e0eee8'));formula();return;
 }
 if(s.kind==='geometry'){
  const X=x=>380+x*72,Y=y=>264-y*40,delta=Math.sqrt(5);rect(g,X(-delta),65,2*delta*72,215,'#eef5f8','#ccd8de');path(g,'M380 65V280','#a26c54',1.5);tx(110,64,'Left identities',14);tx(650,64,'Right identities',14);
  // Within-half cells have an explicit owner; the divider never recolors a point.
  for(let x=-2;x<=2;x++)path(g,`M${X(x*delta/2)} 65V280`,'#cfdee6',1);
  for(let y=0;y<=4;y++)path(g,`M${X(-delta)} ${Y(y)}H${X(delta)}`,'#cfdee6',1);
  if(s.active.length){const A=s.points[s.active[0]],B=s.points[s.active[1]];path(g,`M${X(A[0])} ${Y(A[1])}L${X(B[0])} ${Y(B[1])}`,'#a76842',2.3);}
  s.points.forEach((q,i)=>{g.append(E('circle',{cx:X(q[0]),cy:Y(q[1]),r:6,fill:q[2]==='L'?'#2b6782':'#397a58',stroke:'white','stroke-width':1}));tx(X(q[0])+24,Y(q[1])-10,String(i),14);});tx(380,295,'Strip bound uses initial delta; identities survive tied coordinates.',14);formula();return;
 }
 if(s.kind==='butterfly'){
  const labels=['E₀=1','O₀=2','E₁=1','O₁=2'],A=labels.map((_,i)=>({x:122,y:75+i*54,w:100,h:32})),B=[0,2,1,3].map((v,i)=>({x:640,y:75+i*54,w:112,h:32,index:v}));
  for(let k=0;k<2;k++){const mid={x:378,y:102+k*108,w:92,h:42};if(s.stage>=1){edge(A[k*2],mid);edge(A[k*2+1],mid);}if(s.stage>=2){edge(mid,B[k*2]);edge(mid,B[k*2+1]);}box(mid.x,mid.y,'w='+s.twiddle[k],92,42,'#fff0cb');tx(485,85+k*108,'plus',13);tx(485,140+k*108,'minus',13);}
  A.forEach((v,i)=>box(v.x,v.y,labels[i],100));B.forEach(v=>box(v.x,v.y,s.stage>=3?'Y'+'₀₁₂₃'[v.index]+'='+s.output[v.index]:'Y'+'₀₁₂₃'[v.index],112));tx(380,288,'Inverse root 13; inverse length 13 modulo 17',14);formula();return;
 }
 if(s.kind==='convolution'){
  tx(380,54,'Linear coefficient indices and values',14);const A=row(s.values,86,s.stage<s.values.length?s.stage:-1);A.forEach((v,i)=>mt(v.x,119,i,14));tx(380,160,`Destination length ${s.N}; arrows show index modulo length`,14);const B=row(s.accum,224);B.forEach((v,i)=>mt(v.x,260,i,14));
  for(let i=0;i<s.stage;i++)edge(A[i],B[i%s.N]);tx(380,294,s.modulus?'Arithmetic modulus '+s.modulus+' is a separate value-recovery issue.':'No modulus is applied to these exact integer sums.',14);formula();return;
 }
 if(s.kind==='groups'){
  const start=s.windowStart,gs=s.groups.slice(start,start+5);tx(380,53,`Shown groups ${start+1}–${start+gs.length} of ${s.groups.length}`,14);
  gs.forEach((a,i)=>{tx(100+i*140,78,'group '+(start+i+1),13);a.forEach((v,j)=>box(100+i*140,105+j*32,v,85,27,start+i<s.stage&&v<0?'#d7eadf':v===0?'#fff0cb':'white'));});tx(380,286,'Certified negatives through checkpoint: '+s.smaller,15);formula();return;
 }
 if(s.kind==='search'){
  const width=600,x=80+width*s.lo/s.N,right=80+width*s.hi/s.N;tx(380,60,'Half-open interval endpoints; numbers are indices',15);path(g,'M80 130H680',C.blue,1.5);path(g,`M${x} 107V151`,'#a26c54',2);path(g,`M${right} 107V151`,'#397a58',2);mt(x,175,s.lo,18);mt(right,204,s.hi,18);
  box(380,244,s.mid===null?'empty':'key '+(s.mid+1),150,36,s.mid===null?'#fff0cb':'white');tx(205,290,'Calls: '+s.calls,15);tx(560,290,'Inspected keys: '+s.inspections,15);formula();return;
 }
 if(s.kind==='levels'){
  const A={x:380,y:80,w:88,h:30},K=Array.from({length:s.a},(_,i)=>({x:s.a===1?380:78+i*604/(s.a-1),y:146,w:72,h:30}));K.forEach(B=>edge(A,B));box(380,80,s.N,88,30);K.forEach(B=>box(B.x,B.y,s.N/s.b,72,30));tx(380,48,'Illustrative first split; full depth counts appear below',14);
  const labels=['depth','nodes','size','local toll'];[s.depth,s.count,s.size,s.local].forEach((v,i)=>{tx(118+i*175,212,labels[i],14);box(118+i*175,244,v,142,36);});tx(380,292,s.measure==='leaves'?'At terminal depth the node count is the complete leaf count.':'Each depth ledger represents every node, not only drawn nodes.',14);formula();return;
 }
 throw Error('Unsupported divide model '+s.kind);
}
