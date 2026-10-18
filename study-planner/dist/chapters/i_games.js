(() => {
  'use strict';
  const payload=JSON.parse(document.getElementById('games-model-data').textContent);
  const models=new Map(payload.models.map(m=>[m.id,m]));
  const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  let serial=0;
  function diagram(model,frame,uid){
    const lookup=new Map(model.nodes.map(n=>[n.id,n]));
    const colors={MAX:['#edf3fa','#426586'],MIN:['#faf0ef','#925653'],CHANCE:['#eaf5f2','#397a70'],LEAF:['#f4f5f6','#82918f']};
    let content=`<defs><marker id="arrow-${uid}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L7,3.5 L0,7 Z" fill="#879a98"/></marker></defs>`;
    for(const edge of model.edges){
      const a=lookup.get(edge.from),b=lookup.get(edge.to),pruned=frame.nodes[b.id].status==='pruned';
      const y1=a.y+62,y2=b.y;
      content+=`<path class="game-edge" data-from="${a.id}" data-to="${b.id}" d="M${a.x},${y1} C${a.x},${y1+16} ${b.x},${y2-16} ${b.x},${y2}" fill="none" stroke="${pruned?'#bcc4c2':'#879a98'}" stroke-width="1.6" ${pruned?'stroke-dasharray="4 4"':''} marker-end="url(#arrow-${uid})"/>`;
      if(edge.probability!==null)content+=`<text class="probability" x="${(a.x+b.x)/2+7}" y="${(y1+y2)/2+4}" fill="#226b61" font-size="13">${esc(edge.probability)}</text>`;
    }
    for(const n of model.nodes){
      const state=frame.nodes[n.id],isLeaf=n.kind==='LEAF',active=frame.active===n.id,pruned=state.status==='pruned';
      const [fill,border]=colors[n.kind];
      const value=state.score??(isLeaf?n.input:'?');
      const heading=n.label?(isLeaf?n.label:n.kind+' · '+n.label):(isLeaf?'Input':n.kind);
      const flag=pruned?'not evaluated':state.flag??(isLeaf?'not evaluated':'not searched');
      const shortFlag=flag==='upper bound'?'upper bound':flag==='lower bound'?'lower bound':flag==='working score'?'working':flag;
      content+=`<g class="game-node" data-node="${n.id}" data-state="${state.status}" data-flag="${esc(state.flag??'')}" opacity="${pruned?'.63':'1'}"><title>${esc(heading+'; '+value+'; '+flag)}</title><rect class="node-box" x="${n.x-35}" y="${n.y}" width="70" height="62" rx="7" fill="${pruned?'#f5f6f5':fill}" stroke="${active?'#1c6c73':border}" stroke-width="${active?'2.5':'1.2'}"/><text class="node-heading" x="${n.x}" y="${n.y+16}" text-anchor="middle" fill="#24464d" font-size="10.5">${esc(heading)}</text><text class="value" x="${n.x}" y="${n.y+38}" text-anchor="middle" fill="${pruned?'#7b8583':'#163a42'}">${esc(value)}</text><text class="node-flag" x="${n.x}" y="${n.y+54}" text-anchor="middle" fill="#536e70" font-size="9">${esc(shortFlag)}</text></g>`;
    }
    return `<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc(model.title+'. '+frame.caption)}" viewBox="0 0 ${model.width} ${model.height}" width="${model.width}" height="${model.height}">${content}</svg>`;
  }
  const players=[];
  document.querySelectorAll('.game-player').forEach(host=>{
    const ids=host.dataset.models.split(','),uid=++serial;
    let id=ids[0],index=0,timer=null;
    const seek=host.querySelector('[data-seek]'),play=host.querySelector('[data-play]'),stage=host.querySelector('.game-stage');
    const overview=document.createElement('button');overview.type='button';overview.className='game-overview';overview.setAttribute('aria-label','Pan the readable tree using its complete overview');stage.before(overview);
    const overviewHint=document.createElement('p');overviewHint.className='game-overview-hint';overviewHint.textContent='Overview of the complete tree. The readable view follows the active node. Select an overview position, use its left/right keys, or scroll the main view to inspect another branch.';overview.after(overviewHint);
    function paintOverview(){
      const m=models.get(id),lookup=new Map(m.nodes.map(n=>[n.id,n]));
      const f=m.frames[index],edges=m.edges.map(e=>{const a=lookup.get(e.from),b=lookup.get(e.to);return`<path d="M${a.x},${a.y+31} L${b.x},${b.y+31}" fill="none" stroke="#9eb4b0" stroke-width="3"/>`;}).join('');
      overview.innerHTML=`<svg viewBox="0 0 ${m.width} ${m.height}" aria-hidden="true">${edges}${m.nodes.map(n=>`<circle cx="${n.x}" cy="${n.y+31}" r="${f.active===n.id?12:7}" fill="${f.active===n.id?'#174d63':n.kind==='MIN'?'#bc827c':n.kind==='CHANCE'?'#6ca798':'#7c9eb6'}"/>`).join('')}<rect x="${stage.scrollLeft+2}" y="2" width="${Math.max(0,Math.min(stage.clientWidth,m.width-stage.scrollLeft)-4)}" height="${m.height-4}" fill="none" stroke="#2b7974" stroke-width="4" stroke-dasharray="9 6"/></svg>`;
    }
    function centerActive(){const m=models.get(id),f=m.frames[index],n=m.nodes.find(n=>n.id===f.active)||m.nodes[0];if(stage.clientWidth>0)stage.scrollLeft=Math.max(0,n.x-stage.clientWidth/2);paintOverview();}
    overview.addEventListener('click',event=>{const r=overview.getBoundingClientRect(),m=models.get(id);stage.scrollLeft=Math.max(0,(event.clientX-r.left)/r.width*m.width-stage.clientWidth/2);paintOverview();});
    overview.addEventListener('keydown',event=>{if(event.key==='ArrowLeft'||event.key==='ArrowRight'){event.preventDefault();stage.scrollLeft+=(event.key==='ArrowLeft'?-1:1)*stage.clientWidth*.65;paintOverview();}});
    stage.addEventListener('scroll',paintOverview,{passive:true});
    new ResizeObserver(centerActive).observe(stage);
    function pause(){if(timer!==null)clearInterval(timer);timer=null;play.textContent='Play';play.setAttribute('aria-pressed','false');}
    function paint(){
      const model=models.get(id),f=model.frames[index];
      host.dataset.currentModel=id;host.dataset.checkpoint=String(index);
      seek.max=String(model.frames.length-1);seek.value=String(index);
      stage.innerHTML=diagram(model,f,uid);
      centerActive();
      const windowLabel={incoming:'incoming call window',current:'current tightened window',classification:'original call window for return classification'};
      host.querySelector('.game-counter').textContent=`Checkpoint ${index+1} of ${model.frames.length} · evaluated leaves: ${f.evaluatedLeaves}${f.window?' · '+windowLabel[f.windowRole]+': ('+f.window.join(', ')+')':''}`;
      host.querySelector('.game-caption').textContent=f.caption;
      host.querySelector('.game-why').textContent=f.why;
      host.querySelector('[data-prev]').disabled=index===0;
      host.querySelector('[data-next]').disabled=index===model.frames.length-1;
      if(index===model.frames.length-1)pause();
    }
    host.querySelector('[data-first]').addEventListener('click',()=>{pause();index=0;paint();});
    host.querySelector('[data-prev]').addEventListener('click',()=>{pause();index=Math.max(0,index-1);paint();});
    host.querySelector('[data-next]').addEventListener('click',()=>{pause();index=Math.min(models.get(id).frames.length-1,index+1);paint();});
    seek.addEventListener('input',()=>{pause();index=Number(seek.value);paint();});
    play.addEventListener('click',()=>{
      if(timer!==null){pause();return;}
      if(index===models.get(id).frames.length-1)index=0;
      play.textContent='Pause';play.setAttribute('aria-pressed','true');
      timer=setInterval(()=>{index=Math.min(models.get(id).frames.length-1,index+1);paint();},Number(host.querySelector('[data-speed]').value));
      paint();
    });
    host.querySelector('[data-speed]').addEventListener('change',pause);
    const select=host.querySelector('[data-case]');if(select)select.addEventListener('change',()=>{pause();id=select.value;index=0;paint();});
    host.querySelector('.game-final-print').innerHTML=ids.map((key,i)=>{const m=models.get(key),f=m.frames.at(-1);return'<p>'+esc(m.title)+'</p>'+diagram(m,f,uid+'-print-'+i)+'<p>'+esc(f.caption+' '+f.why)+'</p>';}).join('');
    players.push({host,pause,paint,models:ids,get model(){return id;},get checkpoint(){return index;}});
    paint();
  });
  document.querySelectorAll('.game-uct').forEach(host=>{
    const range=host.querySelector('[data-uct-c]');
    function paint(){
      const c=Number(range.value),rows=[{name:'A',mean:16/20,n:20},{name:'B',mean:3/5,n:5}].map(r=>({...r,bonus:c*Math.sqrt(Math.log(100)/r.n)}));
      const best=rows[0].mean+rows[0].bonus>=rows[1].mean+rows[1].bonus?'A':'B';
      host.dataset.selected=best;host.dataset.coefficient=String(c);
      host.querySelector('.uct-stage').innerHTML=rows.map(r=>`<div class="uct-row ${r.name===best?'selected':''}"><strong>${r.name}</strong><div class="uct-bar" aria-label="${r.name}: mean ${r.mean}, exploration bonus ${r.bonus.toFixed(5)}"><div class="uct-mean" style="width:${r.mean/3*100}%"></div><div class="uct-bonus" style="width:${r.bonus/3*100}%"></div></div><span class="uct-number">${(r.mean+r.bonus).toFixed(5)}</span></div>`).join('');
      host.querySelector('.uct-caption').textContent=`C = ${c.toFixed(1)}. Blue: empirical mean; gold: exploration bonus. Among these listed candidates, the next simulation favors ${best}. A greatest-visits final rule favors A (20 versus 5 visits). UCB is a selection score and may exceed 1; it is not a win probability.`;
    }
    range.addEventListener('input',paint);paint();
  });
  document.querySelectorAll('.game-chance-bounds').forEach(host=>{
    let step=0;const button=host.querySelector('button');
    const captions=['Processed outcomes contribute S = 3.2 with probability 0.6. The unknown mass is 0.4.','The unknown contribution lies in [0.4 × (−2), 0.4 × 8] = [−0.8, 3.2].','Adding S gives an expected-value interval [2.4, 6.4].','The upper endpoint 6.4 is below incumbent 7, so MAX rejects the candidate without evaluating the remainder. Against incumbent 6 the interval would be inconclusive.'];
    function paint(){
      host.dataset.step=String(step);const x=v=>45+v*66;
      host.querySelector('.bounds-stage').innerHTML=`<svg viewBox="0 0 620 150" role="img" aria-label="${esc(captions[step])}"><line x1="45" y1="91" x2="573" y2="91" stroke="#9aafaa"/>${[0,2,4,6,8].map(v=>`<line x1="${x(v)}" y1="87" x2="${x(v)}" y2="96" stroke="#829b96"/><text class="math-text" x="${x(v)}" y="118" text-anchor="middle">${v}</text>`).join('')}${step>=2?`<rect x="${x(2.4)}" y="47" width="${x(6.4)-x(2.4)}" height="25" rx="4" fill="#b5d9d0"/><text class="math-text" x="${x(2.4)}" y="37" text-anchor="middle">2.4</text><text class="math-text" x="${x(6.4)}" y="37" text-anchor="middle">6.4</text>`:`<text x="45" y="53">${step===0?'Known partial sum 3.2; probability mass remains.':'Bound the missing weighted contribution before adding it.'}</text>`}${step===3?`<line x1="${x(7)}" y1="27" x2="${x(7)}" y2="95" stroke="#9c6b4f" stroke-width="2"/><text x="${x(7)}" y="17" text-anchor="middle">incumbent 7</text>`:''}</svg>`;
      host.querySelector('.bounds-caption').textContent=captions[step];button.textContent=step===3?'Restart calculation':'Next calculation';
    }
    button.addEventListener('click',()=>{step=(step+1)%4;paint();});paint();
  });
  let printState=null;
  addEventListener('beforeprint',()=>{
    players.forEach(p=>p.pause());
    if(printState===null)printState=[...document.querySelectorAll('.exam-solution')].map(d=>[d,d.open]);
    document.querySelectorAll('.exam-solution').forEach(d=>d.open=true);
  },true);
  addEventListener('afterprint',()=>queueMicrotask(()=>{if(printState!==null){printState.forEach(([d,open])=>d.open=open);printState=null;}}));
  addEventListener('pagehide',()=>players.forEach(p=>p.pause()));
  document.addEventListener('visibilitychange',()=>{if(document.hidden)players.forEach(p=>p.pause());});
  window.__gamesTeaching={players,models,diagram};
})();
