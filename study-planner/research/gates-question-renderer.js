function gatesQuestion(p,g,f){
 const s=f.snapshot,head=v=>text(g,380,30,v,19),formula=()=>vectorNative(g,f.formulaHtml,25,298,710,55);
 const mt=(x,y,v,size=17)=>{const t=text(g,x,y,v,size);t.setAttribute('font-family','STIX Two Math');const q=String(v).match(/^Q(\d+)$/),voltage=String(v).match(/^V(OL|IL|IH|OH)=(.*)$/);if(q||voltage){t.replaceChildren();const base=E('tspan'),sub=E('tspan',{'baseline-shift':'sub','font-size':size*.72});base.textContent=q?'Q':'V';sub.textContent=q?q[1]:voltage[1];t.append(base,sub);if(voltage){const tail=E('tspan',{'baseline-shift':'baseline'});tail.textContent='='+voltage[2];t.append(tail);}}};
 const nand=(x,y,label,inputs=2)=>{path(g,`M${x} ${y}h25a25 25 0 0 1 0 50h-25Z`,C.ink,1.5);g.append(E('circle',{cx:x+55,cy:y+25,r:5,fill:'white',stroke:C.ink,'stroke-width':1.5}));mt(x+24,y+30,label);};
 const nor=(x,y,label)=>{path(g,`M${x} ${y}Q${x+20} ${y+25} ${x} ${y+50}Q${x+43} ${y+54} ${x+60} ${y+25}Q${x+43} ${y-4} ${x} ${y}`,C.ink,1.5);g.append(E('circle',{cx:x+65,cy:y+25,r:5,fill:'white',stroke:C.ink,'stroke-width':1.5}));mt(x+34,y+30,label);};
 if(s.kind==='nand'||s.kind==='mux')return booleanQuestion(p,g,f);
 if(s.kind==='table'){head(p.scene.title);booleanTable(g,s.stage===0?[]:s.rowsHtml,s.headings,35,69,690,185,s.stage===2?-1:0);if(s.stage===0)text(g,380,158,'The declared resources and exact parameters determine the calculation.',16);text(g,380,282,s.stage===2?'Final quantities are checked; count, depth and timing retain their distinct units.':'Advance to derive the exact layers, components or operation counts.',15);formula();return;}
 if(s.kind==='ring'){
  head(`${s.n} delayed inverters · checkpoint ${s.time} ns`);const dx=620/s.n,w=Math.min(52,dx-24),cy=133;
  for(let i=0;i<s.n;i++){const x=70+i*dx;path(g,`M${x} ${cy-26}L${x+w} ${cy}L${x} ${cy+26}Z`,C.ink,1.5);g.append(E('circle',{cx:x+w+5,cy,r:5,fill:'white',stroke:C.ink,'stroke-width':1.5}));mt(x+20,95,`Q${i+1}`);mt(x+w+15,177,s.q[i]);if(i<s.n-1)path(g,`M${x+w+10} ${cy}H${70+(i+1)*dx}`,C.blue,1.5);}
  const end=70+(s.n-1)*dx+w+10;path(g,`M${end} ${cy}H712V227H45V${cy}H70`,C.blue,1.5);text(g,380,215,'Closed feedback path: every inversion takes its declared delay.',16);
  const x0=190,x1=650,y0=262;path(g,`M${x0} ${y0}H${x1}`,C.ink,1);const t=190+460*(s.time/s.T);dot(g,t,y0,4,C.green);text(g,190,284,'0',14);text(g,420,284,'opposite edge',14);text(g,650,284,`${s.T} ns: full cycle`,14);formula();return;
 }
 if(s.kind==='positive-and'){
  head(`Positive AND at x=${s.x}, y=${s.y}`);nand(195,117,'t');nand(470,117,'F');path(g,'M100 130H195M100 154H195M255 142H420V130H470M420 142V154H470M530 142H665',C.blue,1.5);dot(g,420,142,3);mt(100,112,`x=${s.x}`);mt(100,180,`y=${s.y}`);mt(335,122,s.stage>=1?`t=${s.t}`:'t pending');mt(620,122,s.stage>=2?`F=${s.out}`:'F pending');text(g,380,246,'Both pins of the second NAND receive the same connected net.',17);formula();return;
 }
 if(s.kind==='majority'){
  head(`Three-input majority at ${s.x}${s.y}${s.z}`);const ys=[70,150,230],pairs=[[s.x,s.y],[s.x,s.z],[s.y,s.z]],names=['u','v','w'];ys.forEach((y,i)=>{nor(215,y,names[i]);mt(117,y+17,`${['x','x','y'][i]}=${pairs[i][0]}`);mt(117,y+45,`${['y','z','z'][i]}=${pairs[i][1]}`);path(g,`M150 ${y+13}H${215+8}M150 ${y+37}H${215+8}`,C.blue,1.5);mt(340,y+8,s.stage>=1?`${names[i]}=${s[names[i]]}`:'pending');});
  nor(545,150,'F');path(g,'M285 95H450V160H551.4M285 175H555M285 255H470V190H551.4M615 175H705',C.blue,1.5);mt(672,150,s.stage>=2?`F=${s.out}`:'F pending');formula();return;
 }
 if(s.kind==='wave'){
  head(`Declared low interval [${s.lo}, ${s.hi}) ns`);const names=['a','ab','not-a · c','original Y','bridged Y'],left=160,right=690,min=s.times[0],max=s.times.at(-1),xx=t=>left+(right-left)*(t-min)/(max-min);
  s.times.forEach(t=>text(g,xx(t),65,t,14));text(g,725,65,'ns',14);
  names.forEach((name,j)=>{const y=91+j*35;text(g,140,y+5,name,15,'end');if(j>0&&s.stage===0||j===3&&s.stage<2||j===4&&s.stage<3)return;let d=`M${xx(s.times[0])} ${y+(s.signals[j][0]?0:17)}`;for(let i=1;i<s.times.length;i++)d+=`H${xx(s.times[i])}V${y+(s.signals[j][i]?0:17)}`;path(g,d,j===4?C.green:j===3?C.red:C.blue,2);});text(g,380,283,'Stable b=c=1; consensus bc stays high under this single-input contract.',15);formula();return;
 }
 if(s.kind==='arrival'){
  head('Structural late arrival at the final AND');const b=(x,y,w,v)=>{rect(g,x,y,w,52,'#edf5f8','#91aeba');text(g,x+w/2,y+32,v,17);};b(100,75,110,'3 ns');b(100,210,110,'2 ns');b(295,210,110,'4 ns');b(550,144,115,'AND: 1 ns');path(g,'M50 101H100M50 236H100M210 101H470V157H550M210 236H295M405 236H490V183H550M665 170H720',C.blue,1.6);text(g,330,83,s.stage>=1?'upper: 3 ns':'upper branch',16);text(g,485,262,s.stage>=1?'lower: 6 ns':'lower branch',16);text(g,645,117,s.stage>=2?'output: 7 ns':'output pending',16);formula();return;
 }
 if(s.kind==='sizing'){
  head(`Illustrative switching cases at width scale ${s.s}`);text(g,650,59,'time units',15);
  s.cases.forEach((r,i)=>{const y=100+i*92,unit=80;text(g,98,y+29,`case ${i+1}`,17);rect(g,160,y,r[0]*unit,37,'#d6e4eb','#789eaf');rect(g,160+r[0]*unit,y,r[1]*unit,37,'#cae9dd','#73a994');text(g,580,y+24,`${(r[0]+r[1]).toFixed(3).replace(/0+$/,'').replace(/\.$/,'')} total`,17);text(g,335,y+62,`internal ${r[0]} + fixed-load ${r[1].toFixed(3)}`,16);if(i===s.maxCase)text(g,683,y+24,'maximum',15,'middle',C.red);});text(g,380,280,'Gray: internal contribution · green: external contribution divided by scale.',15);formula();return;
 }
 if(s.kind==='rc'){
  head('Normalized first-order charging model');const x=110,y=257,w=560,h=170;path(g,`M${x} ${y}H${x+w}M${x} ${y}V${y-h}`,C.ink,1.4);text(g,82,y-h,1,14);text(g,82,y,0,14);text(g,380,282,'horizontal axis: t / (RC)',16);text(g,95,63,'v / V',15);
  if(s.stage>=1){let d='';for(let i=0;i<=100;i++){const t=3*i/100;d+=(i?'L':'M')+(x+w*t/3)+' '+(y-h*(1-Math.exp(-t)));}path(g,d,C.blue,2);const yy=y-h*s.q;path(g,`M${x} ${yy}H${x+w}`,C.red,1.2,{'stroke-dasharray':'4 4'});text(g,705,yy+5,'3/4',16);if(s.stage>=2){const xx=x+w*s.cross/3;path(g,`M${xx} ${y}V${yy}`,C.green,1.3,{'stroke-dasharray':'4 4'});dot(g,xx,yy,4,C.green);mt(570,223,'crossing: ln 4',15);}}formula();return;
 }
 if(s.kind==='noise'){
  head('Guaranteed driver levels and receiver acceptance');const top=82,bottom=246,scale=s.voh+.4,yy=v=>bottom-(bottom-top)*v/scale;
  const levels=[['VOL',s.vol,180],['VIL',s.vil,320],['VIH',s.vih,465],['VOH',s.voh,610]];levels.forEach(([name,v,x])=>{path(g,`M${x} ${bottom}V${top}`,C.ink,1);dot(g,x,yy(v),4,C.blue);mt(x,yy(v)-15,`${name}=${v}`);});
  if(s.stage>=1){path(g,`M230 ${yy(s.vol)}H270V${yy(s.vil)}H300`,C.green,2);text(g,250,273,`low margin: ${(s.vil-s.vol).toFixed(1)} V`,16);}
  if(s.stage>=2){path(g,`M485 ${yy(s.vih)}H535V${yy(s.voh)}H595`,C.green,2);text(g,550,273,`high margin: ${(s.voh-s.vih).toFixed(1)} V`,16);}formula();return;
 }
 if(s.kind==='cmos'){
  const bits=s.inputs||[s.x,s.y],n=bits.length,names=['x','y','z'],xs=n===3?[215,385,555]:[245,515],ys=n===3?[178,212,246]:[188,234];head(`Complementary NAND: stable input ${bits.join('')}`);
  const mos=(x,y,name,on,pmos)=>{path(g,`M${x} ${y-12}V${y+12}M${x-8} ${y-10}V${y+10}M${x-35} ${y}H${x-8}`,on&&s.stage>=1?C.green:C.ink,1.7);if(pmos)g.append(E('circle',{cx:x-15,cy:y,r:4,fill:'white',stroke:C.ink}));text(g,x+43,y+5,name,15);};
  text(g,380,60,'VDD',16);path(g,`M${xs[0]} 68H${xs.at(-1)}`,C.blue,1.5);xs.forEach((x,i)=>{path(g,`M${x} 68V98M${x} 122V151`,C.blue,1.5);mos(x,110,'pMOS '+names[i],!bits[i],true);mt(x-55,115,bits[i]);});path(g,`M${xs[0]} 151H${xs.at(-1)}M380 151V${ys[0]-12}M380 151H680`,C.blue,1.5);dot(g,380,151,3);
  ys.forEach((y,i)=>{mos(380,y,'nMOS '+names[i],bits[i],false);mt(325,y+5,bits[i]);if(i<n-1)path(g,`M380 ${y+12}V${ys[i+1]-12}`,C.blue,1.5);});path(g,`M380 ${ys.at(-1)+12}V274M368 274H392M373 279H387M377 284H383`,C.blue,1.5);text(g,654,131,s.stage>=2?`F=${s.out}`:'F pending',17);text(g,130,194,s.stage>=1?`pullup: ${s.up?'on':'off'}`:'pullup pending',16);text(g,130,241,s.stage>=1?`pulldown: ${s.down?'on':'off'}`:'pulldown pending',16);formula();return;
 }
 throw Error('Unknown gates mechanism '+s.kind);
}
