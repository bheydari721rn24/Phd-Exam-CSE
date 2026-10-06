/* Exact, inspectable teaching transitions shared by concept-specific drawings. */
"use strict";
(() => {
 const NS='http://www.w3.org/2000/svg',reduced=matchMedia('(prefers-reduced-motion: reduce)'),players=[];
 const element=(tag,text,cls)=>{const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;};
 const state=f=>({...f.snapshot??f.state??(f.rows?Object.fromEntries(f.rows.map(r=>[r.name,r.values??r.cells])):Object.fromEntries((f.nodes||[]).map(n=>[n.id,n.label]))),...(f.metrics?{counters:f.metrics}:{})});
 function difference(a,b,path=''){
  if(JSON.stringify(a)===JSON.stringify(b))return [];
  if(a&&b&&typeof a==='object'&&typeof b==='object'&&Array.isArray(a)===Array.isArray(b))return [...new Set([...Object.keys(a),...Object.keys(b)])].flatMap(k=>difference(a[k],b[k],Array.isArray(b)?`${path}[${k}]`:path?`${path}.${k}`:k));
  return [{field:path||'state',before:a??null,after:b??null}];
 }
 function value(v){
  const e=element('span',undefined,'teaching-value');
  if(v===null||v===undefined){e.textContent='not present';return e;}
  if(typeof v==='object'){e.textContent=JSON.stringify(v);return e;}
  const math=document.createElementNS('http://www.w3.org/1998/Math/MathML','math'),n=document.createElementNS(math.namespaceURI,/^-?\d+(\.\d+)?$/.test(String(v))?'mn':'mtext');n.textContent=String(v);math.append(n);e.append(math);return e;
 }
 function metadata(model,f,i){
  if(f.teaching)return f.teaching;
  return {operation:f.caption,why:f.caption,reading:model.teachingPolicy?.reading||model.description||model.reading||'Inspect the exact input, operation and resulting state.',guide:model.code||model.teachingPolicy?.guide||[],activeLine:f.line,checks:[],changes:i?difference(state(model.frames[i-1]),state(f)):[],currentState:state(f),initial:i===0,scope:model.invariant||model.scope||'',counterexample:!!f.counterexample};
 }
 function panel(host,before){
  const root=element('section',undefined,'teaching-panel');root.setAttribute('aria-label','Explanation of the current transition');before.before(root);let guideOpen=false,stateOpen=false;
  return {root,show(model,f,i){
   const t=metadata(model,f,i);root.replaceChildren();root.dataset.operation=t.operation;root.dataset.mode=t.mode||model.kind||'exact-state';
   const heading=element('div',undefined,'teaching-operation');heading.append(element('span',i===0?'Initial checkpoint':'Current operation','teaching-eyebrow'),element('p',t.operation),document.createTextNode(' '));root.append(heading);
   if(t.checks?.length){const tests=element('div',undefined,'teaching-tests');tests.setAttribute('aria-label','Exact checks at this checkpoint');for(const c of t.checks){const row=element('div',undefined,'teaching-test');const math=element('span');math.innerHTML=c.mathHtml;row.append(math,element('span',c.result,'teaching-result'));tests.append(row);}root.append(tests);}
   const why=t.why.startsWith(t.operation)?t.why.slice(t.operation.length).trim():t.why;if(why)root.append(element('p',why,'teaching-why'));root.dataset.explanation=t.why;
   if(t.changes?.length){const details=element('details',undefined,'teaching-changes');details.open=stateOpen;details.append(element('summary',`Before and after: ${t.changes.length} changed ${t.changes.length===1?'field':'fields'}`));const wrap=element('div',undefined,'teaching-table-wrap'),table=element('table'),head=element('tr');for(const text of ['State field','Before','After'])head.append(element('th',text));table.append(head);for(const c of t.changes){const row=element('tr');row.append(element('th',c.field,'teaching-field'));for(const v of [c.before,c.after]){const cell=element('td');cell.append(value(v));row.append(cell);}table.append(row);}wrap.append(table);details.append(wrap);details.ontoggle=()=>stateOpen=details.open;root.append(details);}
   else root.append(element('p',t.initial?'This is the first displayed checkpoint. Its exact state includes the operation described above.':'No recorded state field changes in this checkpoint; inspect the stated test, case or dependency.','teaching-state-note'));
   if(t.reading||t.guide?.length){const details=element('details',undefined,'teaching-guide');details.open=guideOpen;details.append(element('summary','How to read this model and follow its steps'));if(t.reading)details.append(element('p',t.reading));if(t.guide?.length){const list=element('ol');for(const [j,line] of t.guide.entries()){const item=element('li',line);if(j===t.activeLine){item.className='current';item.setAttribute('aria-current','step');}list.append(item);}details.append(list);}details.ontoggle=()=>guideOpen=details.open;root.append(details);}
   if(t.counterexample)root.append(element('p','Counterexample: the stated failure belongs to this deliberately incorrect variant.','teaching-counterexample'));
   const summary=element('details',undefined,'teaching-snapshot');summary.append(element('summary','Exact current state'));const code=element('pre',JSON.stringify(t.currentState,null,2),'teaching-state');summary.append(code);root.append(summary);
  }};
 }
 function transformedBox(node,svg){const b=node.getBBox(),m=svg.getScreenCTM().inverse().multiply(node.getScreenCTM()),a=new DOMPoint(b.x,b.y).matrixTransform(m),c=new DOMPoint(b.x+b.width,b.y+b.height).matrixTransform(m);return {x:(a.x+c.x)/2,y:(a.y+c.y)/2,w:Math.abs(c.x-a.x),h:Math.abs(c.y-a.y)};}
 function snapshot(stage){const svg=stage.querySelector('svg');return svg?new Map([...stage.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,{box:transformedBox(n,svg),text:n.textContent}])):new Map();}
 function motion(stage,old,model){
  if(reduced.matches)return [];const svg=stage.querySelector('svg');if(!svg)return [];
  const animations=[];
  // Fixed slot labels, gates and linked-object bodies do not travel. Each model keeps its own topology.
  const linked=/linked|topology|chain|splice|heap|cycle|predecessor|reversal/.test(model.kind||'');
  for(const n of stage.querySelectorAll('[data-entity]')){
   const id=n.dataset.entity,p=old.get(id);if(!p||/^slot|^cell|^node-|^cursor-|^ptr|^edge/.test(id)||n.querySelector('[data-arrow]'))continue;
   const b=transformedBox(n,svg),dx=p.box.x-b.x,dy=p.box.y-b.y;
   if(Math.hypot(dx,dy)<.1||p.text!==n.textContent||linked)continue;
   const lane=Math.abs(dy)<4?(dx<0?-Math.max(32,b.h):Math.max(32,b.h)):0;
   animations.push(n.animate([{transform:`translate(${dx}px,${dy}px)`},{transform:`translate(${dx/2}px,${dy/2+lane}px)`},{transform:'translate(0,0)'}],{duration:1000,easing:'cubic-bezier(.42,0,.2,1)'}));
  }
  // Rewiring is a discrete operation: show the complete new attached wire, then trace it.
  for(const path of stage.querySelectorAll('path[data-arrow]')){const len=path.getTotalLength();if(!len||!Number.isFinite(len))continue;animations.push(path.animate([{strokeDasharray:String(len),strokeDashoffset:String(len)},{strokeDasharray:String(len),strokeDashoffset:'0'}],{duration:900,easing:'linear'}));}
  return animations;
 }
 function raw(o){
  const {host,model,stage,caption,formula,seek,progress,play,speed,prev,next,reset,printRoot}=o;let i=0,timer=null,running=false;const explain=panel(host,stage);
  const stop=()=>{clearTimeout(timer);timer=null;running=false;stage.getAnimations({subtree:true}).forEach(a=>{const t=a.currentTime;a.pause();if(t!==null)a.currentTime=t;});if(play){play.textContent='Play';play.setAttribute('aria-pressed','false');}host.dataset.running='false';};
  function draw(n,animate=false){
   const old=snapshot(stage);stage.getAnimations({subtree:true}).forEach(a=>a.cancel());i=Math.max(0,Math.min(model.frames.length-1,n));const f=model.frames[i];stage.innerHTML=f.svg||f.html;
   for(const svg of stage.querySelectorAll('svg')){window.DiagramLayout?.finish(svg,{arrows:false});svg.setAttribute('aria-label',f.caption);}
   if(animate)motion(stage,old,model);explain.show(model,f,i);
   if(caption)caption.textContent=f.caption;if(formula)formula.innerHTML=f.formulaHtml||'';if(seek){seek.value=i;seek.max=model.frames.length-1;seek.setAttribute('aria-valuetext',`Step ${i+1} of ${model.frames.length}`);}if(progress)progress.textContent=`Step ${i+1} of ${model.frames.length}`;if(prev)prev.disabled=i===0;if(next)next.disabled=i===model.frames.length-1;host.dataset.checkpoint=i;host.dataset.frame=i;host.dataset.ready='true';window.MathLayout?.schedule();
  }
  function delay(){const s=Number(speed?.value)||1500;return s<=2?Math.max(1250,1800/s):Math.max(1250,s);}
  function tick(){if(!running)return;if(i===model.frames.length-1){stop();return;}draw(i+1,true);timer=setTimeout(tick,delay());}
  function start(){players.forEach(p=>{if(p!==api)p.pause();});const unfinished=stage.getAnimations({subtree:true}).some(a=>a.playState==='paused'&&Number(a.currentTime)<a.effect.getComputedTiming().endTime);if(i===model.frames.length-1&&!unfinished)draw(0);running=true;host.dataset.running='true';stage.getAnimations({subtree:true}).forEach(a=>reduced.matches?a.finish():a.play());if(play){play.textContent='Pause';play.setAttribute('aria-pressed','true');}timer=setTimeout(tick,delay());}
  if(reset)reset.onclick=()=>{stop();draw(0);};if(prev)prev.onclick=()=>{stop();draw(i-1,true);};if(next)next.onclick=()=>{stop();draw(i+1,true);};if(play)play.onclick=()=>running?stop():start();if(seek)seek.oninput=()=>{stop();draw(Number(seek.value));};if(speed)speed.onchange=()=>{if(running){clearTimeout(timer);timer=setTimeout(tick,delay());}};
  host.addEventListener('keydown',e=>{if(e.target.matches('input,select,button,summary')||!['ArrowLeft','ArrowRight','Home','End',' '].includes(e.key))return;e.preventDefault();if(e.key===' '){running?stop():start();return;}stop();draw(e.key==='Home'?0:e.key==='End'?model.frames.length-1:i+(e.key==='ArrowRight'?1:-1),!['Home','End'].includes(e.key));});
  function print(){stop();if(!printRoot)return;printRoot.replaceChildren();for(const [j,f] of model.frames.entries()){const figure=element('figure');figure.innerHTML=f.svg||f.html;figure.append(element('figcaption',`Step ${j+1}. ${f.caption}`));if(f.formulaHtml){const math=element('div');math.innerHTML=f.formulaHtml;figure.append(math);}printRoot.append(figure);for(const svg of figure.querySelectorAll('svg'))window.DiagramLayout?.finish(svg,{arrows:false});}}
  const api={host,model,draw,show:n=>{stop();draw(n);},pause:stop,print,clearPrint:()=>printRoot?.replaceChildren(),get index(){return i;},get running(){return running;},teaching:explain};players.push(api);draw(0);return api;
 }
 function register(p){players.push(p);return p;}
 addEventListener('beforeprint',()=>players.forEach(p=>p.print?.()??p.pause()));addEventListener('afterprint',()=>players.forEach(p=>p.clearPrint?.()));document.addEventListener('visibilitychange',()=>{if(document.hidden)players.forEach(p=>p.pause());});addEventListener('pagehide',()=>players.forEach(p=>p.pause()));reduced.addEventListener('change',()=>players.forEach(p=>p.pause()));
 window.TeachingTransitions={panel,metadata,difference,state,raw,motion,snapshot,register,players};
})();
