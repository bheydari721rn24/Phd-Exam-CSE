/* Sequential, paused teaching traces. Editable laboratories compute their own states. */
(() => {
 'use strict';
 const esc=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'), players=[];
 function finish(svg){if(svg)window.DiagramLayout?.finish(svg,{arrows:false,labels:true});}
 function player(el,model){
  const q=s=>el.querySelector(s),api=TeachingTransitions.raw({host:el,model,stage:q('.sq-stage'),caption:q('.sq-caption'),formula:q('.sq-formula'),seek:q('[data-seek]'),progress:q('[data-progress]'),play:q('[data-play]'),speed:q('[data-speed]'),prev:q('[data-prev]'),next:q('[data-next]'),reset:q('[data-reset]'),printRoot:q('.sq-print-trace')});players.push(api);return api;
 }
 function formula(metrics){return '<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow>'+Object.entries(metrics).map(([k,v])=>`<mtext>${esc(k)}</mtext><mo>=</mo><mn>${esc(v)}</mn><mspace width="1em"/>`).join('')+'</mrow></math>';}
 function picture(f){
  let y=38,body='',serial=0;
  const tx=(x,y,s,size=16,key='')=>`<text x="${x}" y="${y}" font-size="${size}" text-anchor="middle" dominant-baseline="middle"${key?` data-label-for="${key}"`:''}>${esc(s)}</text>`;
  const box=(x,y,w,h,v,key)=>`<rect data-box="${key}" x="${x}" y="${y}" width="${w}" height="${h}" rx="7" fill="#e5f0f2" stroke="#7393a1"/>`+tx(x+w/2,y+h/2,v,18,key);
  if(f.storage){const C=f.storage.length;body+=tx(380,28,`Physical capacity ${C}; front ${f.front}; count ${f.count}; next insertion ${(f.front+f.count)%C}`,17);for(let j=0;j<C;j++){const a=-Math.PI/2+2*Math.PI*j/C,r=C>1?174:0,x=380+r*Math.cos(a),z=300+r*Math.sin(a);body+=box(x-31,z-24,62,48,f.storage[j]===null?'empty':f.storage[j],'slot-'+j)+tx(380+(r+72)*Math.cos(a),300+(r+72)*Math.sin(a),'slot '+j,14);}if(C>1)body+=tx(380,300,'Count '+f.count,21);y=646;}
  const stacks=f.rows.filter(x=>x.style==='stack');if(stacks.length){const start=y,depth=Math.max(1,...stacks.map(x=>x.values.length)),bottom=start+52+depth*57;stacks.forEach((row,c)=>{const x=(c+.5)*760/stacks.length;body+=tx(x,start,row.name,16);if(!row.values.length)body+=tx(x,start+75,'empty');row.values.forEach((v,j)=>{const key='b'+serial++;body+=box(x-54,bottom-(j+1)*57,108,48,v,key);});if(row.values.length)body+=tx(x+88,bottom-row.values.length*57+24,'top',14);});y=bottom+54;}
  for(const row of f.rows.filter(x=>x.style!=='stack')){body+=tx(380,y,row.name,16);y+=35;if(!row.values.length){body+=tx(380,y+25,'empty');y+=78;}else for(let a=0;a<row.values.length;a+=10){const v=row.values.slice(a,a+10),w=Math.min(58,620/v.length),start=(760-v.length*(w+10)+10)/2;v.forEach((x,j)=>{const key='b'+serial++;body+=box(start+j*(w+10),y,w,48,x,key);});y+=78;}}
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 ${y+26}" role="img"><title>${esc(f.caption)}</title>${body}</svg>`;
 }
 function evaluate(mode,p){
  const frames=[],row=(name,values,style='row')=>({name,values:[...values],style});
  const frame=(caption,rows,metrics={},extra={})=>{const f={caption,rows:structuredClone(rows),...structuredClone(extra),formulaHtml:formula(metrics)};f.svg=picture(f);frames.push(f);};let result;
  if(mode==='ring'){
   const C=p.C,A=Array(C).fill(null),q=[],out=[];let f=0;
   const add=c=>frame(c,[row('Logical FIFO order',q),row('Removed',out)],{front:f,count:q.length,rear:(f+q.length)%C},{storage:A,front:f,count:q.length});add('Empty count-based ring; all physical slots are usable.');
   for(const op of p.ops){if(op[0]==='E'){if(q.length===C)throw Error('Overflow: the history exceeds the physical capacity.');A[(f+q.length)%C]=op[1];q.push(op[1]);}else{if(!q.length)throw Error('Underflow: removal from an empty queue.');out.push(q.shift());A[f]=null;f=(f+1)%C;}add(op[0]==='E'?`Enqueue ${op[1]}.`:'Dequeue oldest item; advance front modulo capacity.');}result={values:q,output:out,f,n:q.length,r:(f+q.length)%C,storage:A};
  }else if(mode==='two'){
   const I=[],O=[],out=[];let e=0,d=0,t=0;
   const add=(c,logical=O.slice().reverse().concat(I))=>frame(c,[row('Input bottom to top',I,'stack'),row('Output bottom to top',O,'stack'),row('Logical queue',logical),row('Removed',out)],{enqueues:e,moved:t,dequeues:d,cost:e+2*t+d,potential:2*I.length});add('Initially empty; stack push/pop count starts at zero.');
   for(const op of p.ops){if(op[0]==='E'){if(I.length+O.length===12)throw Error('At most 12 live items fit this teaching display.');I.push(op[1]);e++;add(`Enqueue ${op[1]} into input.`);}else{if(!I.length&&!O.length)throw Error('Underflow.');if(!O.length){const logical=[...I];while(I.length){O.push(I.pop());t++;add('Internal transfer: complete it before a public observation.',logical);}add('Transfer complete; output top is oldest.');}if(op[0]==='F'){add('Observe oldest value '+O.at(-1)+' without removal.');}else{out.push(O.pop());d++;add('Remove output top.');}}}result={I,O,output:out,e,d,t,cost:e+2*t+d,queue:O.slice().reverse().concat(I)};
  }else if(mode==='postfix'){
   const S=[];let operations=0;const gcd=(a,b)=>{a=a<0n?-a:a;while(b){[a,b]=[b,a%b];}return a;};
   const rat=(a,b=1n)=>{if(!b)throw Error('Division by zero.');if(b<0n){a=-a;b=-b;}const g=gcd(a,b);a/=g;b/=g;if(a.toString().replace('-','').length>30||b.toString().length>30)throw Error('Exact result exceeds the 30-digit laboratory bound.');return [a,b];},str=([a,b])=>b===1n?String(a):`${a}/${b}`;
   const add=c=>frame(c,[row('Operands bottom to top',S.map(str),'stack')],{binaryOperations:operations});add('Exact rational arithmetic; right operand is popped first.');
   for(const tok of p.tokens){if(/^-?\d+$/.test(tok)){S.push(rat(BigInt(tok)));add('Push operand '+tok);}else{if(S.length<2)throw Error('Operator needs two available operands.');const [c,d]=S.pop(),[a,b]=S.pop();S.push(tok==='+'?rat(a*d+c*b,b*d):tok==='-'?rat(a*d-c*b,b*d):tok==='*'?rat(a*c,b*d):rat(a*d,b*c));operations++;add(`Apply ${tok}; retain exact reduced result.`);}}if(S.length!==1)throw Error('A complete expression must leave exactly one result.');result={value:str(S[0]),operations};
  }else if(mode==='permutation'){
   const target=p.target,S=[],out=[];let a=1,peak=0,valid=true;const add=c=>frame(c,[row('Pending bottom to top',S,'stack'),row('Unused increasing inputs',Array.from({length:target.length-a+1},(_,i)=>a+i)),row('Output',out),row('Target',target)],{peak});add('Forced greedy simulation starts with unused input 1.');
   for(const x of target){while((!S.length||S.at(-1)!==x)&&a<=target.length){S.push(a++);peak=Math.max(peak,S.length);add('Forced push before output '+x);}if(S.at(-1)!==x){valid=false;add('Impossible: requested value is covered by another top.');break;}out.push(S.pop());add('Pop requested value '+x);}result={valid,peak,output:out};
  }else if(mode==='window'){
   const A=p.values,k=p.k,D=[],out=[];const add=c=>frame(c,[row('Input values',A),row('Candidate indices front to rear',D),row('Candidate values',D.map(j=>A[j])),row('Completed window maxima',out)],{window:k});add('Candidate indices increase; values strictly decrease under newest-equal tie policy.');
   for(let i=0;i<A.length;i++){while(D.length&&D[0]<=i-k){D.shift();add('Expire an index outside the current window.');}while(D.length&&A[D.at(-1)]<=A[i]){D.pop();add('Remove a dominated rear candidate.');}D.push(i);if(i>=k-1)out.push(A[D[0]]);add('Insert index '+i+'; front gives a maximum for each complete window.');}result={maxima:out};
  }return {id:'editable',title:'Computed '+mode+' laboratory',kind:mode,frames,result};
 }
 function editable(model){return `<section class="sq-model" data-sq-model="editable" tabindex="0"><h3>${esc(model.title)}</h3><p class="sq-invariant">Inputs are validated before this complete trace replaces the previous valid run. Each checkpoint is independently computed.</p><div class="sq-stage"></div><p class="sq-caption" aria-live="polite"></p><div class="sq-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2400">Slow</option><option value="1600" selected>Normal</option><option value="950">Fast</option></select></label><label>Checkpoint<input type="range" data-seek min="0" max="${model.frames.length-1}" value="0"></label></div><p data-progress></p><div class="formula-block sq-formula"></div><div class="sq-print-trace"></div></section>`;}
 function read(form){
  const mode=form.mode.value,int=(s,name)=>{if(!/^-?\d+$/.test(s.trim()))throw Error(name+' must be an integer.');const x=Number(s);if(!Number.isSafeInteger(x)||Math.abs(x)>99)throw Error(name+' must be between −99 and 99.');return x;},list=(s,name)=>s.split(',').map(x=>int(x,name));let p;
  if(mode==='ring'||mode==='two'){const pieces=form.ops.value.split(',');if(pieces.length>20)throw Error('At most 20 operations.');const ops=pieces.map(s=>{s=s.trim();if(s==='D'||mode==='two'&&s==='F')return [s];if(!/^E:-?\d+$/.test(s))throw Error('Use E:integer, D, or (for two stacks) F, separated by commas.');return ['E',int(s.slice(2),'Value')];});const C=Number(form.capacity.value);if(!Number.isInteger(C)||C<1||C>12)throw Error('Capacity must be 1–12.');p={ops,C};}
  else if(mode==='postfix'){const tokens=form.tokens.value.trim().split(/\s+/);if(tokens.length>24)throw Error('At most 24 tokens.');tokens.forEach(t=>{if(!['+','-','*','/'].includes(t))int(t,'Operand');});p={tokens};}
  else if(mode==='permutation'){const target=list(form.target.value,'Label');if(target.length>8||target.length<1||target.slice().sort((a,b)=>a-b).some((x,i)=>x!==i+1))throw Error('Use each label from 1 to n exactly once; n must be 1–8.');p={target};}
  else{const values=list(form.values.value,'Value'),k=Number(form.window.value);if(values.length>12||!Number.isInteger(k)||k<1||k>values.length)throw Error('Use 1–12 values and an integer width fitting the input.');p={values,k};}return evaluate(mode,p);
 }
 function fitInline(){for(const m of document.querySelectorAll('.lesson p math')){m.classList.remove('sq-wide-math');if(m.getBoundingClientRect().width>m.parentElement.clientWidth-1)m.classList.add('sq-wide-math');}}
 window.addEventListener('resize',fitInline);
 async function init(){
  try{const response=await fetch('a_stackqueue-models.json');if(!response.ok)throw Error('Could not load checkpoint data.');const data=await response.json(),models=new Map(data.models.map(x=>[x.id,x]));for(const el of document.querySelectorAll('[data-sq-model]'))player(el,models.get(el.dataset.sqModel));
   const form=document.getElementById('sq-form'),output=document.getElementById('sq-output'),error=document.getElementById('sq-lab-error');let active;
   const fields=()=>{for(const el of form.querySelectorAll('[data-modes]'))el.hidden=!el.dataset.modes.split(' ').includes(form.mode.value);};form.mode.onchange=fields;fields();
   form.onsubmit=ev=>{ev.preventDefault();try{const model=read(form);if(active){active.pause();players.splice(players.indexOf(active),1);}output.innerHTML=editable(model);active=player(output.firstElementChild,model);output.dataset.result=JSON.stringify(model.result);error.textContent='';}catch(e){error.textContent=e.message;}};
   form.requestSubmit();window.StackQueueChapter={players,evaluate,read};fitInline();document.documentElement.dataset.sqLoaded='true';
  }catch(e){document.documentElement.dataset.sqLoaded='error';const p=document.createElement('p');p.textContent='Interactive models unavailable: '+e.message;document.querySelector('.hero').append(p);}
 }
 window.addEventListener('beforeprint',()=>{for(const p of players){p.pause();p.print();}});window.addEventListener('afterprint',()=>{for(const p of players)p.clearPrint();});
 document.fonts.ready.then(init);
})();
