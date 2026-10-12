function countingFormula(g,f,x,y,w,h){
 nativeFormula(g,f,x,y,w,h);
 const body=g.lastElementChild.firstElementChild,math=body.querySelector('math');
 body.style.display='flex';body.style.alignItems='center';body.style.justifyContent='center';body.style.height='100%';body.style.overflowY='hidden';
 if(math){math.style.margin='0';math.style.fontSize='18px';math.style.lineHeight='1.15';}
}
function countingQuestion(p,g,f){
 const s=f.snapshot;
 if(s.kind==='stars'){
  text(g,380,35,`Encoding ${s.index} of ${s.total}: five units, two separators`,21);
  s.tokens.forEach((v,i)=>{const x=110+i*90;if(v==='|')path(g,`M${x} 100V173`,C.amber,5);else dot(g,x,136,14,C.blue);text(g,x,205,i,16);});
  text(g,380,245,'Slot numbers describe the encoding; coordinates are named.',18);
  countingFormula(g,{formulaHtml:f.formulaHtml},55,270,650,82);return;
 }
 if(s.kind==='parity'){
  text(g,380,30,'Exact parity rows after imposing c at least one',21);
  ['b','largest j','row count','included so far'].forEach((h,i)=>text(g,110+i*175,72,h,18));
  s.counts.forEach((v,i)=>{const y=110+i*34;if(i===s.active)rect(g,40,y-22,680,32,'#fff0cc','none');[i,s.upper[i],v,i<=s.active?s.counts.slice(0,i+1).reduce((a,b)=>a+b,0):'pending'].forEach((v,j)=>text(g,110+j*175,y,String(v),18));});
  countingFormula(g,{formulaHtml:f.formulaHtml},35,290,690,60);return;
 }
 if(s.kind==='onto'){
  text(g,380,32,'Inclusion–exclusion: signed terms, not disjoint events',20);
  s.terms.forEach((v,i)=>{const x=45+i*143;const h=Math.abs(v)/4096*125;rect(g,x,225-h,105,h||2,i<=s.stage?(v<0?'#ecd6dc':'#cee9df'):'#edf3f6','none');text(g,x+52.5,243,s.labels[i],15);text(g,x+52.5,72,String(v),18);});
  countingFormula(g,{formulaHtml:f.formulaHtml},40,270,680,84);return;
 }
 if(s.kind==='dp'){
  text(g,380,30,'No adjacent ones: exact prefix-count recurrence',21);
  s.values.forEach((v,i)=>{const x=36+i*78;rect(g,x,75,67,43,i<=s.n?'#d9ebe5':'#edf3f6');text(g,x+33.5,99,i<=s.n?v:'?',18);text(g,x+33.5,145,i,16);});
  text(g,380,186,`Complete words at length ${s.examplesLength}${s.n>5?' (reference)':''}`,18);
  s.words.forEach((v,i)=>text(g,100+(i%5)*140,224+Math.floor(i/5)*28,v||'empty',18));
  countingFormula(g,{formulaHtml:f.formulaHtml},45,303,670,53);return;
 }
 if(s.kind==='pairing'){
  text(g,380,30,`Pairing ${s.index} of 105: each label has one partner`,21);
  const pos=Array.from({length:8},(_,i)=>[380+220*Math.cos(-Math.PI/2+i*Math.PI/4),171+90*Math.sin(-Math.PI/2+i*Math.PI/4)]);
  s.pairs.forEach(([a,b])=>{const [x,y]=pos[a-1],[X,Y]=pos[b-1],d=Math.hypot(X-x,Y-y),dx=(X-x)/d*21,dy=(Y-y)/d*21;path(g,`M${x+dx} ${y+dy}L${X-dx} ${Y-dy}`,C.blue,2.4);});
  pos.forEach(([x,y],i)=>{dot(g,x,y,21,'#e5f1f5');text(g,x,y+6,i+1,18);});
  countingFormula(g,{formulaHtml:f.formulaHtml},45,303,670,53);return;
 }
 if(s.kind==='report'){
  text(g,380,30,'Eight ordered words, four reports with unequal fibers',21);
  s.words.forEach((v,i)=>{const x=65+(i%4)*170,y=80+Math.floor(i/4)*83;rect(g,x,y,120,50,v.split('1').length-1===s.k?'#cee8df':'#eef4f7');text(g,x+60,y+29,v,21);});
  text(g,380,262,`The report with ${s.k} ones combines ${s.counts[s.k]} words.`,20);
  countingFormula(g,{formulaHtml:f.formulaHtml},55,288,650,65);return;
 }
 throw Error('Unknown counting question contract: '+s.kind);
}
