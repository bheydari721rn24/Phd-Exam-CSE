/* Labeled, decision-led teaching player. Every transition is tied to saved algorithm state. */
(() => {
 'use strict';
 const esc=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),players=[];
 function player(el,model){
  let i=0,timer=null;const stage=el.querySelector('.sort-stage'),seek=el.querySelector('[data-seek]'),play=el.querySelector('[data-play]');
  const panel=document.createElement('div');panel.className='sort-teaching';stage.before(panel);
  const controls=el.querySelector('.sort-controls');stage.before(controls);
  const pause=()=>{clearTimeout(timer);timer=null;stage.getAnimations({subtree:true}).forEach(a=>a.pause());play.textContent='Play';play.setAttribute('aria-pressed','false');};
  function copyAlong(path,target,svg){
   const dot=document.createElementNS('http://www.w3.org/2000/svg','circle');dot.setAttribute('r','4');dot.setAttribute('fill','#426e91');dot.dataset.flowToken='true';svg.append(dot);const length=path.getTotalLength(),steps=Math.max(2,Math.ceil(length/10)),keys=[];
   for(let k=0;k<=steps;k++){const p=path.getPointAtLength(length*k/steps);keys.push({transform:`translate(${p.x}px,${p.y}px)`,offset:k/steps});}
   const a=dot.animate(keys,{duration:1050,easing:'linear',fill:'forwards'});a.finished.then(()=>dot.remove()).catch(()=>dot.remove());
   for(const text of target.querySelectorAll('text'))text.animate([{opacity:0,offset:0},{opacity:0,offset:.85},{opacity:1,offset:1}],{duration:1050});
  }
  function move(node,before,after,svg,copy=false){
   const dx=before.x-after.x,dy=before.y-after.y;if(!dx&&!dy)return;
   const lane=Math.abs(dy)<8?(dx<0?-42:42):0;
   const keys=[{transform:`translate(${dx}px,${dy}px)`,opacity:copy?.6:1},{transform:`translate(${dx/2}px,${dy/2+lane}px)`,opacity:1},{transform:'translate(0,0)',opacity:1}];
   // Heap edges connect fixed positions. Move record labels rather than the position circles.
   const targets=model.kind==='heap'?[...node.querySelectorAll('text')]:[node];
   for(const target of targets)target.animate(keys,{duration:850,easing:'cubic-bezier(.42,0,.2,1)'});
  }
  function draw(index,animate=false){
   stage.getAnimations({subtree:true}).forEach(a=>a.cancel());const old=new Map([...stage.querySelectorAll('[data-entity]')].map(x=>[x.dataset.entity,x.getBBox()]));
   i=Math.max(0,Math.min(model.frames.length-1,index));const f=model.frames[i];stage.innerHTML=f.svg;const svg=stage.querySelector('svg');
   if(animate&&!reduced.matches){const copied=new Set();
    for(const path of svg.querySelectorAll('[data-source-entity]')){const source=old.get(path.dataset.sourceEntity),target=svg.querySelector('[data-entity="'+path.dataset.targetEntity+'"]');if(source&&target){copyAlong(path,target,svg);copied.add(path.dataset.targetEntity);}}
    const destination=f.distributedId||(f.outputActive!==undefined?f.rows.find(r=>r.name==='Output')?.cells[f.outputActive]?.id:null);
    if(destination){const source=old.get('reference-'+destination),target=svg.querySelector('[data-entity="'+destination+'"]');if(source&&target){move(target,source,target.getBBox(),svg,true);copied.add(destination);}}
    for(const node of svg.querySelectorAll('[data-entity]')){if(copied.has(node.dataset.entity))continue;const before=old.get(node.dataset.entity);if(before)move(node,before,node.getBBox(),svg);}
   }
   el.querySelector('.sort-caption').textContent=f.caption;el.querySelector('.sort-formula').innerHTML=f.formulaHtml;
   const t=f.teaching||{operation:'checkpoint',why:f.caption,guide:[],regions:[]};
   const interval=r=>'<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>[</mo><mn>'+r.lo+'</mn><mo>,</mo><mn>'+r.hi+'</mn><mo>)</mo></mrow></math>';
   const regionLabel=r=>/^[<>=≤≥] pivot$/.test(r.label)?'<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>'+esc(r.label[0])+'</mo><mtext>pivot</mtext></mrow></math>':esc(r.label);
   panel.innerHTML='<div class="sort-decision"><strong>'+esc(t.operation.replaceAll('-',' '))+'</strong>'+(t.testHtml?'<span>'+t.testHtml+'<b class="sort-truth">'+esc(t.decision)+'</b></span>':'')+'</div><p>'+esc(t.why)+'</p>'+(t.regions?.length?'<ul class="sort-regions">'+t.regions.map(r=>'<li data-role="'+r.role+'"><strong>'+regionLabel(r)+'</strong> '+interval(r)+'</li>').join('')+'</ul>':'')+(t.guide?.length?'<details class="sort-guide"'+(el.dataset.guideOpen==='true'?' open':'')+'><summary>Algorithm steps and current operation</summary><ol>'+t.guide.map((s,j)=>'<li'+(j+1===t.activeLine?' class="current" aria-current="step"':'')+'>'+esc(s)+'</li>').join('')+'</ol></details>':'');
   const guide=panel.querySelector('details');if(guide)guide.ontoggle=()=>el.dataset.guideOpen=String(guide.open);
   let summary=el.querySelector('.sort-mobile-state');if(!summary){summary=document.createElement('div');summary.className='sort-mobile-state';stage.after(summary);}
   summary.innerHTML='<p>Current state; pan the full-size diagram for labels.</p>'+f.rows.map(r=>'<p><strong>'+esc(r.name)+':</strong> '+esc(r.cells.length?r.cells.map(x=>x?x.key+'['+x.id+']':'hole').join(', '):'empty')+'</p>').join('');
   seek.value=i;el.querySelector('[data-prev]').disabled=i===0;el.querySelector('[data-next]').disabled=i===model.frames.length-1;el.querySelector('[data-progress]').textContent=`Step ${i+1} of ${model.frames.length}`;el.dataset.checkpoint=i;el.dataset.operation=t.operation;window.MathLayout?.schedule?.();
  }
  const step=d=>{pause();draw(i+d,true);};function tick(){if(i===model.frames.length-1){pause();return;}draw(i+1,true);timer=setTimeout(tick,Math.max(1250,Number(el.querySelector('[data-speed]').value)));}
  el.querySelector('[data-reset]').onclick=()=>{pause();draw(0);};el.querySelector('[data-prev]').onclick=()=>step(-1);el.querySelector('[data-next]').onclick=()=>step(1);play.onclick=()=>{if(timer){pause();return;}if(i===model.frames.length-1)draw(0);stage.getAnimations({subtree:true}).forEach(a=>a.play());play.textContent='Pause';play.setAttribute('aria-pressed','true');timer=setTimeout(tick,Math.max(1250,Number(el.querySelector('[data-speed]').value)));};seek.oninput=()=>{pause();draw(Number(seek.value));};
  el.addEventListener('keydown',ev=>{if(ev.target!==el)return;const actions={ArrowRight:()=>step(1),ArrowLeft:()=>step(-1),Home:()=>{pause();draw(0);},End:()=>{pause();draw(model.frames.length-1);},' ':()=>play.click()};if(actions[ev.key]){ev.preventDefault();actions[ev.key]();}});
  const api={model,draw,pause,print(){el.querySelector('.sort-print-trace').innerHTML=model.frames.map((f,j)=>`<figure>${f.svg}<figcaption>Step ${j+1}. ${esc(f.caption)}${f.teaching?'<p>'+esc(f.teaching.why)+'</p>':''}</figcaption><div class="formula-block">${f.formulaHtml}</div></figure>`).join('');},clearPrint(){el.querySelector('.sort-print-trace').innerHTML='';}};players.push(api);draw(0);el.dataset.ready='true';return api;
 }
