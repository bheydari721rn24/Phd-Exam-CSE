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
