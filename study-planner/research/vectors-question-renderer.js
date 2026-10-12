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
