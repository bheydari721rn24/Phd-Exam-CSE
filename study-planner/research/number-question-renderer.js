function numberQuestion(p,g,f){
 const s=f.snapshot,head=v=>text(g,380,30,v,20),formula=()=>vectorNative(g,f.formulaHtml,25,283,710,70);
 const box=(x,y,w,h,v,fill='#eef5f8',size=18)=>{rect(g,x,y,w,h,fill,'#abc4cf');text(g,x+w/2,y+h/2+6,v,size);};
 if(s.kind==='adder'){
  head(`${s.w}-bit ripple addition: bit 0 at the left`);const dx=650/s.w,cw=Math.min(70,dx-38);
  s.rows.forEach(([i,a,b,cin,r,cout],j)=>{const x=52+j*dx,done=j<s.completed;box(x,75,cw,32,a,'#edf4f8',18);box(x,115,cw,32,b,'#f3f0e6',18);rect(g,x,162,cw,48,done?'#dceee4':'#f1f4f6','#aac3cf');text(g,x+cw/2,191,'FA'+i,16);path(g,`M${x+cw/3} 107H${x-8}V154H${x+cw/3}V162M${x+2*cw/3} 147V162`,C.blue,1.3);path(g,`M${x+cw/2} 210V225`,done?C.green:'#b5c6ce',1.4);box(x,225,cw,37,done?r:'·',done?'#dceee4':'#f1f4f6',19);
   if(j<s.w-1){arrow(g,x+cw,186,x+dx,186,done?C.green:'#b5c6ce');text(g,x+cw+(dx-cw)/2,150,done?cout:'·',15);}
  });
  text(g,380,60,s.completed===s.w?`stored ${s.stored}; signed ${s.signedResult}; carry ${s.carry}; overflow ${s.overflow}`:'A row above B; FA has two bit inputs and the routed incoming carry.',13);
  text(g,31,190,'0',15);arrow(g,34,186,52,186,C.blue);text(g,380,279,'Dots mark result positions whose local operation is still pending.',13);formula();return;
 }
 if(s.kind==='quant'){
  head('Exact target → raw index → neighbor decision → decoded output');
  box(62,76,240,48,'target '+s.target);box(460,76,240,48,'unit '+s.unit);arrow(g,302,100,460,100,C.blue);
  box(245,151,270,43,s.stage>=1?'raw target '+s.scaled:'raw target: pending');
  if(s.stage>=2){box(65,219,220,43,`${s.low} → ${s.lowReal}`,s.stage===3&&s.chosen===s.low?'#dceee4':'#edf5f8');box(475,219,220,43,`${s.high} → ${s.highReal}`,s.stage===3&&s.chosen===s.high?'#dceee4':'#edf5f8');arrow(g,290,194,190,219,C.blue);arrow(g,470,194,580,219,C.blue);}
  else text(g,380,239,'Neighbors are not yet compared.',17);formula();return;
 }
 if(s.kind==='round-tree'){
  head('Two actual decimal addition trees; round at each node');
  ['left','right'].forEach((key,k)=>{const x=42+k*375;box(x,58,330,35,k?'a + (b + c)':'(a + b) + c');s[key].forEach(([op,exact,rounded],i)=>{const y=120+i*77;box(x,y,330,50,s.stage>i?`${op}: ${exact} → ${rounded}`:'next addition pending',s.stage>i?'#dceee4':'#f0f4f6',16);if(i===0)arrow(g,x+165,y+50,x+165,y+77,C.blue);});});formula();return;
 }
 if(s.kind==='fields'){
  head('Declared normal fields: each has its own decoder');box(35,65,105,50,'sign '+s.sign);box(177,65,230,50,'exponent '+s.exponent);box(445,65,280,50,'fraction '+s.fraction);
  box(177,172,230,47,s.stage>=1?`${s.E} − ${s.bias} = ${s.e}`:'bias step pending',s.stage>=1?'#dceee4':'#edf5f8');box(445,172,280,47,s.stage>=2?'1.1010₂ = '+s.m:'leading bit pending',s.stage>=2?'#dceee4':'#edf5f8');arrow(g,292,115,292,172,C.blue);arrow(g,585,115,585,172,C.blue);formula();return;
 }
 if(s.kind==='extension'){
  head('Original cells and added sign cells remain distinguishable');bits(g,s.old,175,83,50,s.old.length,'original six-bit word');
  if(s.stage>=1){bits(g,s.new,125,195,50,s.new.length,'extended eight-bit word');rect(g,125,185,98,62,'none',C.amber);arrow(g,200,125,150,195,C.amber);}
  else text(g,380,220,'New sign positions have not been introduced.',18);formula();return;
 }
 if(s.kind==='denominator'){
  head('Reduced denominator determines exact binary termination');numberTable(g,s.rows.slice(0,s.stage===0?0:4),['fraction','factorization','decision'],50,85,660,180,s.stage===2?2:-1);if(s.stage===0)text(g,380,179,'All four reduced fractions are inputs; factorization follows.',18);formula();return;
 }
 if(s.kind==='bytes'){
  head('Increasing byte addresses run left to right');text(g,380,63,'Hex values 12,34,56,78 keep their internal bit order.',17);const row=(values,y,label)=>{text(g,105,y+29,label,17);values.forEach((v,i)=>{const x=225+i*105,active=s.stage===3||s.stage===1&&label==='little'&&i===0||s.stage===2&&label==='big'&&i===0;box(x,y,75,47,v,active?'#dceee4':'#edf5f8');text(g,x+37,y-10,'addr+'+i,15);});};row(s.le,106,'little');row(s.be,207,'big');formula();return;
 }
 if(s.kind==='bias'){
  head('Normal stored field and complete bias subtraction');box(55,90,210,55,'E = '+s.stored);box(290,90,210,55,s.stage>=1?'K = '+s.bias:'bias pending');box(535,90,180,55,s.stage===2?'e = '+s.decoded:'decode pending',s.stage===2?'#dceee4':'#edf5f8');arrow(g,265,118,290,118,C.blue);arrow(g,500,118,535,118,C.blue);text(g,380,220,'Stored exponent00010 is normal in the declared five-bit field.',17);formula();return;
 }
 if(s.kind==='scale'){
  head('Integer code and real unit are separate objects');box(250,75,260,50,'stored integer97');
  if(s.stage>=1){box(75,170,225,50,'integer part:3 × 32');box(455,170,225,50,'remainder:1');arrow(g,280,125,190,170,C.blue);arrow(g,480,125,565,170,C.green);}else text(g,380,215,'The unit1/32 is external format metadata.',18);formula();return;
 }
 if(s.kind==='decode'){
  head('One unchanged word with two mathematical decoders');bits(g,s.word,200,84,64,5,'the original five bits');box(85,197,250,47,s.stage>=1?'unsigned29':'unsigned: pending');box(420,197,250,47,s.stage>=2?'signed−3':'signed: pending',s.stage>=2?'#dceee4':'#edf5f8');formula();return;
 }
 if(s.kind==='zeros'){
  head('Two distinct words, one numerical zero');bits(g,s.positive,75,95,45,5,'top-zero branch');bits(g,s.negative,440,95,45,5,'top-one branch');box(85,205,210,42,s.stage>=1?'0 → 0':'decode pending');box(450,205,210,42,s.stage>=2?'31 − 31 → 0':'decode pending',s.stage>=2?'#dceee4':'#edf5f8');formula();return;
 }
 if(s.kind==='fraction-sum'){
  head('Exactly five retained positions; no unstated infinite tail');for(let i=0;i<5;i++){const x=60+i*138;box(x,86,105,58,i<s.count?'1':'pending',i<s.count?'#dceee4':'#eef4f7',18);text(g,x+52,175,'weight 1/'+(2**(i+1)),17);}text(g,380,240,'included '+s.count+' of 5 positions; remaining-to-one '+(s.denominator-s.numerator)+'/'+s.denominator,18);formula();return;
 }
 if(s.kind==='spacing'){
  head('Local precision grid and unequal boundary-side gaps');const x=[70,155,260,365,465,570,675];s.values.forEach((v,i)=>{dot(g,x[i],154,7,i===1?C.amber:C.blue);text(g,x[i],190,v,19);if(i)arrow(g,x[i-1]+7,154,x[i]-7,154,C.blue);});text(g,207,112,'gap2',17);if(s.stage>=2){text(g,110,231,'previous gap1',17);text(g,625,231,'next-binade gap4',17);}text(g,420,110,'…',19);formula();return;
 }
 if(s.kind==='hex'){
  head('Five groups retain the declared format width');s.groups.forEach((v,i)=>{const x=42+i*142;box(x,75,120,40,'hex '+i);if(s.stage>=1){bits(g,v,x,175,29,4,'four bits');arrow(g,x+60,115,x+60,175,C.blue);}});formula();return;
 }
 if(s.kind==='division'||s.kind==='fraction-conversion'){
  head(s.kind==='division'?'Quotient decreases; remainders need reversal':'Residual fraction advances; digits keep extraction order');numberTable(g,s.rows,s.kind==='division'?['old quotient','new quotient','remainder']:['twice residual','emitted digit','new residual'],50,77,660,173);text(g,380,268,(s.kind==='division'?'low-to-high extracted digits: ':'fraction digits: ')+(s.bits||'none yet'),17);formula();return;
 }
 if(s.kind==='multi-decode'){
  head('The decoder supplies signedness and scale');bits(g,s.word,175,61,48,8,'unchanged word 11101001');numberTable(g,s.stage?s.rows.slice(0,s.stage===2?5:4):[],['declared decoder','exact value'],150,140,460,132);formula();return;
 }
 if(s.kind==='bcd'){
  head('Digit subtotals use decimal carry from the previous digit');numberTable(g,s.rows.slice(0,Math.max(0,s.stage)),['place','a','b','cin','sum','+6','digit','cout'],25,90,710,120);if(s.stage===3){box(175,230,410,40,'0001 0111 0101 → decimal 175','#dceee4');}formula();return;
 }
 if(s.kind==='gray'){
  head('Decode the label before arithmetic, then re-encode');box(50,77,300,47,'input Gray '+s.gray);box(415,77,300,47,s.stage>=1?'binary '+s.binary+' =19':'prefix XOR pending');arrow(g,350,100,415,100,C.blue);box(50,200,300,47,s.stage>=2?'incremented binary '+s.newBinary:'index increment pending');box(415,200,300,47,s.stage>=3?'output Gray '+s.newGray:'Gray encoding pending',s.stage>=3?'#dceee4':'#eef5f8');arrow(g,565,124,200,200,C.blue);arrow(g,350,224,415,224,C.green);formula();return;
 }
 if(s.kind==='hamming'){
  head('Position order 1→7 and syndrome order high→low');const word=s.stage===2||s.stage===3?s.received:s.word;for(let i=0;i<7;i++){const x=66+i*89,isParity=[0,1,3].includes(i);text(g,x+30,75,'pos '+(i+1),16);box(x,93,61,45,s.stage===0&&isParity?'p':word[i],(s.stage===2||s.stage===3)&&i===5?'#f7e5c8':isParity?'#e5eff7':'#dceee4',20);}
  if(s.stage>=3){s.checks.forEach((v,i)=>{box(55+i*239,191,222,55,'check '+(1<<i)+': '+v.join(','),'#eef5f8',16);text(g,165+i*239,270,'XOR = '+s.syndrome[i],17);});}formula();return;
 }
 if(s.kind==='secded'){
  head('Two actual errors are not a single-error correction request');const v=s.stage===0?'00000000':s.stage===3?s.naive:s.received;bits(g,v,124,85,63,8,s.stage===3?'counterfactual wrong correction':'actual extended word');box(70,214,270,48,s.stage===3?'counterfactual S0, P1':s.stage>=2?'syndrome3, parity0':'checks pending');box(405,214,290,48,s.stage===3?'wrong data; original decision refuses':s.stage>=2?'detect; do not correct':'action pending','#dceee4',s.stage===3?14:17);formula();return;
 }
 throw Error('Unknown number representation mechanism: '+s.kind);
 function bits(g,word,x,y,dx,n,label){text(g,x+dx*n/2,y-14,label,16);[...word].forEach((b,i)=>box(x+i*dx,y,dx-4,45,b,'#eef5f8',19));}
}
function numberTable(g,rows,headings,x,y,w,h,activeIndex=rows.length-1){
 const node=E('foreignObject',{x,y,width:w,height:h}),div=document.createElementNS('http://www.w3.org/1999/xhtml','div');div.style.cssText="font:14px 'Source Sans 3',sans-serif;width:100%;height:100%;overflow:auto";
 const table=document.createElement('table');table.style.cssText='display:table;width:100%;table-layout:fixed;border-collapse:collapse;margin:0;font-size:14px;line-height:1.25';
 const tr=document.createElement('tr');headings.forEach(v=>{const c=document.createElement('th');c.textContent=v;c.style.cssText='padding:3px 7px;text-align:left;font-size:14px;line-height:1.25;background:#edf4f8';tr.append(c);});table.append(tr);
 rows.forEach((r,i)=>{const tr=document.createElement('tr');r.forEach(v=>{const c=document.createElement('td');c.textContent=v;c.style.cssText='padding:1px 7px;text-align:left;font-size:14px;line-height:1.25;border-bottom:2px solid white;background:'+(i===activeIndex?'#e0eee7':'#f5f8fa');tr.append(c);});table.append(tr);});div.append(table);node.append(div);g.append(node);
}
