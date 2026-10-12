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
