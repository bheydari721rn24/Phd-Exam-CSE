function typesQuestion(p,g,f){
 const s=f.snapshot,head=v=>text(g,380,30,v,20),formula=()=>vectorNative(g,f.formulaHtml,25,278,710,76);
 const box=(x,y,w,h,line,fill='#f2f7fa')=>{rect(g,x,y,w,h,fill,'#b5cbd3');text(g,x+w/2,y+h/2+6,line,18);};
 if(s.kind==='adder'){
  head('Four-bit hardware: signed result and unsigned carry');
  const labels=['first operand','second operand','stored low bits'];
  s.bits.forEach((bits,r)=>{text(g,80,90+r*55,labels[r],17,'start');[...bits].forEach((v,j)=>box(275+j*58,60+r*55,48,40,v,j===0?'#f7eddc':'#f2f7fa'));});
  text(g,380,248,`Signed sum ${s.total}; overflow ${s.overflow?'YES':'NO'}; carry out ${s.carryout}`,18);formula();return;
 }
 if(s.kind==='pipeline'||s.kind==='chop'){
  head(s.kind==='chop'?'Exact-real decimal operation checkpoints':'Typed value and destination checkpoints');
  const xs=[30,285,540];s.rows.forEach(([label,value],i)=>{const r=i<3?0:1,x=i<3?xs[i]:160+(i-3)*300,y=70+r*105;rect(g,x,y,190,65,i===s.active?'#dceee4':'#f4f8fa','#a8c1ca');text(g,x+95,y+22,label,15);text(g,x+95,y+49,value,19);});
  arrow(g,220,102,285,102,C.blue);arrow(g,475,102,540,102,C.blue);
  if(s.kind==='pipeline'&&s.rows[0][0]==='unsigned8 source'){
   path(g,'M635 135V155H255V175',C.blue,1.8);path(g,'M635 155H555V175',C.green,1.8);
  }else{path(g,'M635 135V155H255V175',C.blue,1.8);arrow(g,350,207,460,207,C.blue);}formula();return;
 }
 if(s.kind==='decimal'){
  head('Exact intermediate → rounded value at each tree node');
  s.rows.forEach(([label,exact,rounded],i)=>{const x=i<2?45:410,y=65+(i%2)*100;rect(g,x,y,300,77,i===s.stage?'#dceee4':'#f3f8fa','#acc5ce');text(g,x+150,y+22,label,16);text(g,x+150,y+54,exact+' → '+rounded,20);});
  arrow(g,195,142,195,165,C.blue);arrow(g,560,142,560,165,C.green);formula();return;
 }
 if(s.kind==='casts'){
  head('Division operands determine what a later cast receives');
  s.rows.forEach((row,i)=>{const y=65+i*67;rect(g,40,y,680,57,i===s.stage?'#dceee4':'#f4f8fa','#bdd0d6');text(g,62,y+33,row[0],18,'start');text(g,310,y+33,row[1]+'; '+row[2],15,'start');});formula();return;
 }
 if(s.kind==='short'){
  head('Reachability separates skipped from undefined');
  box(55,88,220,75,s.stage===0?'input: x = 0':'x != 0 : false','#e5f0f7');box(475,88,220,75,s.stage===3?'10/0 : undefined':s.stage===0?'right operand pending':'10/x : not evaluated',s.stage===3?'#eed8df':'#eef2f4');
  if(s.stage===3)arrow(g,275,125,475,125,C.amber);else if(s.stage>=1){path(g,'M165 163V220H475',C.green,2);box(475,195,220,60,s.stage===2?'logical result: 0':'division bypassed','#dceee4');}
  text(g,380,65,s.stage===3?'Changed operator: bitwise AND':'Original operator: logical AND',17);formula();return;
 }
 if(s.kind==='wrap'){
  head('Two different arithmetic domains');box(40,80,300,100,'unsigned32','#e4f0e9');box(420,80,300,100,'signed32','#f3e2e7');
  text(g,190,210,s.stage>=1?'exact 2³² → residue 0':'UINT_MAX + 1u',19);text(g,570,210,s.stage>=2?'exact 2³¹ → undefined':'INT_MAX + 1',19);text(g,380,250,s.stage===0?'First identify each operand type.':s.stage===1?'Only the unsigned lane has completed its operation.':'The signed lane stops before any numeric C output.',17);formula();return;
 }
 if(s.kind==='macro'){
  head('Token substitution, then the actual parse tree');
  if(s.stage===3){box(130,80,500,70,'((i++) * (i++))','#f3e2e7');text(g,380,200,'Unsequenced modifications: no predicted result.',19);formula();return;}
  if(s.stage===0){box(80,80,600,70,'SQR(1+2) → 1+2*1+2');text(g,380,210,'Substitute tokens before constructing the parse tree.',19);formula();return;}
  const done=s.stage===2;const nodes=[[380,65,done?'5':'+'],[220,125,done?'3':'+'],[540,125,'2'],[100,190,'1'],[330,190,done?'2':'*'],[285,245,'2'],[395,245,'1']];nodes.forEach(([x,y,v])=>{box(x-26,y-18,52,36,v);});
  arrow(g,354,76,244,107,C.blue);arrow(g,406,76,516,107,C.blue);arrow(g,194,138,124,172,C.blue);arrow(g,244,143,308,172,C.blue);arrow(g,310,208,293,227,C.blue);arrow(g,350,208,380,227,C.blue);
  text(g,560,208,done?'2 × 1 = 2; then add':'Grouped multiplication first',18);formula();return;
 }
 if(s.kind==='bits'){
  head(s.signed?'Signed positional weights: an asymmetric range':'Unsigned weights and maximum');
  if(s.signed&&s.stage===3){box(60,75,640,65,'signed char −128 promotes to int32 before unary minus');box(180,170,400,55,'int negation: 128 is representable','#dceee4');text(g,380,255,'−INT_MIN instead overflows its evaluated int domain.',18);formula();return;}
  const width=s.weights.length,dx=62,start=380-width*dx/2;s.weights.forEach((w,i)=>{box(start+i*dx,95,52,52,s.stage===0?'?':s.bits[i],w<0?'#f7e6d5':'#edf5f8');text(g,start+i*dx+26,182,w,18);});text(g,380,230,s.stage===0?'Read the weights before selecting an extremal pattern.':s.stage===1?'Construct the requested extremal pattern.':'Each bit contributes its displayed positional weight.',18);formula();return;
 }
 if(s.kind==='register'){
  head('Exact total, discarded carry and stored residue');box(50,85,200,76,s.stage===0?'inputs: 255 and 6':'255 + 6 = 261');box(300,85,190,76,s.stage>=1?'carry: 1 × 256':'carry: not computed','#f7eddc');box(540,85,170,76,s.stage>=2?'stored: 5':'store pending','#dceee4');if(s.stage>=1)arrow(g,250,124,300,124,C.blue);if(s.stage>=2)arrow(g,490,124,540,124,C.green);text(g,380,220,s.stage===3?'C lane: promoted int261, then byte conversion5.':'Hardware lane: exact sum precedes reduction.',18);formula();return;
 }
 if(s.kind==='layout'){
  head(`Minimum ABI: n=${s.n}, second offset=${s.offset}, size=${s.size}`);const start=70,dx=38;
  for(let i=0;i<s.size;i++){const pad=i>=s.n&&i<s.offset;rect(g,start+i*dx,115,dx-3,65,pad?'#f7e5c9':i<s.n?'#e1eff8':'#dceee4','#b3c5cd');text(g,start+i*dx+(dx-3)/2,153,i,16);}
  text(g,start+s.n*dx/2,90,'first member',17);text(g,start+(s.offset+2)*dx,90,'second member',17);text(g,380,235,s.n===s.offset?'No internal padding is required at this aligned boundary.':'Amber bytes are padding; every other byte belongs to a member.',17);formula();return;
 }
 if(s.kind==='array'){
  head('Five rows × six elements × four bytes');
  for(let i=0;i<5;i++)for(let j=0;j<6;j++){const active=s.stage===1?i===0:s.stage===2?i===4&&j===5:false;rect(g,55+j*59,70+i*33,55,29,active?'#e7d5ad':'#e3f0f7','#b6cbd5');text(g,82+j*59,90+i*33,4*(6*i+j),14);}
  text(g,535,110,'row stride: 24 bytes',18);text(g,535,160,'whole object: 120 bytes',18);text(g,535,210,s.stage===3?'parameter pointer: 8 bytes':'last element ends at byte119',17);formula();return;
 }
 if(s.kind==='packed'){
  head(`Packed flags: ${s.n} bits in ${s.size} whole bytes`);
  for(let row=0;row<s.size;row++)for(let bit=0;bit<8;bit++){const i=row*8+bit;rect(g,165+bit*53,78+row*53,46,43,i<s.n?'#dceee4':'#f0e9dc','#b9cdd5');text(g,188+bit*53,106+row*53,i<s.n?i+1:'·',17);}
  text(g,380,260,'Dots mark unused bits inside the final allocated byte.',17);formula();return;
 }
 if(s.kind==='float'){
  head(s.base===32?'Actual p=5 neighbors near32':'Binary64 neighbors at a local origin a=2⁵³');const vals=[-3,-2,-1,0,2,4],x=v=>310+60*v;
  path(g,'M100 155H630','#8faab8',1.8);vals.forEach(v=>{dot(g,x(v),155,4,C.blue);text(g,x(v),197,s.base===32?s.base+v:v===0?'a':`a${v>0?'+':''}${v}`,17);});
  const binary64=s.base!==32,midpoint=s.stage===2&&binary64||s.stage===3&&!binary64?3:1;
  if(s.stage>=1){dot(g,x(midpoint),155,6,C.amber);text(g,x(midpoint),120,'exact midpoint',15);}
  const rounding=binary64?s.stage>=1: s.stage>=2;
  if(rounding){const chosen=midpoint===1?0:4;const ring=E('circle',{cx:x(chosen),cy:155,r:12,fill:'none',stroke:C.green,'stroke-width':3});g.append(ring);text(g,380,250,binary64?`Chosen neighbor: a+${chosen}; its retained significand is even.`:`Chosen neighbor: ${32+chosen}; retained significand ${(32+chosen)/2} is even.`,17);}else text(g,380,250,s.stage===0?'Spacing changes from1 to2 at this boundary.':'The intermediate odd integer has no exact representation.',17);formula();return;
 }
 if(s.kind==='division'){
  head('Negative quotient: truncation is not floor');
  if(s.stage===3){box(95,75,240,75,'INT_MIN / −1');box(430,75,240,75,'undefined','#f3e2e7');arrow(g,335,112,430,112,C.amber);text(g,380,220,'Mathematical quotient 2³¹ does not fit int32.',19);formula();return;}
  path(g,'M110 145H650','#9ab1bd',1.5);[[-6,210],[-5,530]].forEach(([v,x])=>{dot(g,x,145,4,C.blue);text(g,x,188,v,20);});dot(g,423.333,145,6,C.amber);text(g,423.333,115,'−16/3',19);
  if(s.stage>=1){text(g,210,227,'floor: −6',18);text(g,530,227,'truncate: −5',18);}else text(g,380,230,'First locate the exact real quotient.',18);formula();return;
 }
 throw Error('Unknown typed mechanism: '+s.kind);
}
