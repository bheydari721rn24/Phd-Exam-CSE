/* Exact, independently rendered counting traces and bounded enumeration laboratory. */
"use strict";
(() => {
const reduced=matchMedia('(prefers-reduced-motion: reduce)'),esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const choose=(n,k)=>{if(k<0||k>n)return 0;let r=1;for(let j=1;j<=Math.min(k,n-k);j++)r=r*(n-Math.min(k,n-k)+j)/j;return r;};
const math=n=>`<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>${n}</mn></math>`;
const states=[];
function mount(host,model){
 const stage=host.querySelector('.counting-stage'),caption=host.querySelector('.counting-caption'),formula=host.querySelector('.counting-formula'),seek=host.querySelector('[data-seek]'),progress=host.querySelector('[data-progress]'),play=host.querySelector('[data-play]'),speed=host.querySelector('[data-speed]');
 let index=0,timer=null;
 const stop=()=>{clearInterval(timer);timer=null;play.textContent='Play';};
 function draw(motion=true){
  const old=new Map([...stage.querySelectorAll('[data-entity]')].map(e=>{const b=e.getBBox();return[e.dataset.entity,{x:b.x+b.width/2,y:b.y+b.height/2}];}));
  const f=model.frames[index];stage.innerHTML=f.svg;caption.textContent=f.caption;formula.innerHTML=f.formulaHtml;seek.value=index;progress.textContent=`Checkpoint ${index+1} of ${model.frames.length}`;
  host.querySelector('[data-prev]').disabled=index===0;host.querySelector('[data-next]').disabled=index===model.frames.length-1;
  if(motion&&!reduced.matches){for(const e of stage.querySelectorAll('[data-entity]')){const p=old.get(e.dataset.entity);if(p){const b=e.getBBox(),dx=p.x-b.x-b.width/2,dy=p.y-b.y-b.height/2;if(Math.abs(dx)+Math.abs(dy)>1)e.animate([{transform:`translate(${dx}px,${dy}px)`},{transform:'translate(0,0)'}],{duration:450,easing:'ease-in-out'});}}}
  window.MathLayout?.schedule();
 }
 function start(){stop();if(index===model.frames.length-1)index=0;play.textContent='Pause';draw();timer=setInterval(()=>{if(index===model.frames.length-1){stop();return;}index++;draw();if(index===model.frames.length-1)stop();},Number(speed.value));}
 host.querySelector('[data-prev]').onclick=()=>{stop();index=Math.max(0,index-1);draw();};host.querySelector('[data-next]').onclick=()=>{stop();index=Math.min(model.frames.length-1,index+1);draw();};
 host.querySelector('[data-reset]').onclick=()=>{stop();index=0;draw();};play.onclick=()=>timer?stop():start();seek.oninput=()=>{stop();index=Number(seek.value);draw();};speed.onchange=()=>{if(timer)start();};
 host.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight'].includes(e.key)||e.target.matches('input,select'))return;e.preventDefault();stop();index=Math.max(0,Math.min(model.frames.length-1,index+(e.key==='ArrowRight'?1:-1)));draw();});
 host.querySelector('.counting-print-trace').innerHTML=model.frames.map((f,i)=>`<figure><p>Checkpoint ${i+1} of ${model.frames.length}</p>${f.svg}<figcaption>${esc(f.caption)}</figcaption><div class="formula-block">${f.formulaHtml}</div></figure>`).join('');
 states.push(stop);draw(false);
}
fetch('d_counting-models.json').then(r=>{if(!r.ok)throw Error('Trace data unavailable');return r.json();}).then(data=>{for(const m of data.models){const host=document.querySelector(`[data-counting-model="${m.id}"]`);if(host)mount(host,m);}document.documentElement.dataset.countingLoaded='true';}).catch(e=>{document.querySelectorAll('.counting-error').forEach(x=>{x.hidden=false;x.textContent='The trace could not load. Its static diagram and lesson remain available; reload to retry.';});console.error(e);});
addEventListener('beforeprint',()=>states.forEach(stop));addEventListener('pagehide',()=>states.forEach(stop));reduced.addEventListener('change',()=>states.forEach(stop));

function subsets(n,k){const out=[];function visit(a,next){if(a.length===k){out.push(a.slice());return;}for(let i=next;i<=n;i++)visit([...a,i],i+1);}if(k>=0&&k<=n)visit([],1);return out;}
function allocations(n,m){const out=[];function visit(a,left){if(a.length===m-1){out.push([...a,left]);return;}for(let i=0;i<=left;i++)visit([...a,i],left-i);}visit([],n);return out;}
function words(n){const out=[];for(let mask=0;mask<2**n;mask++)out.push(mask.toString(2).padStart(n,'0'));return out;}
function rotate(w,r){return w.slice(r)+w.slice(0,r);}
function canonical(w){return [...w].map((_,i)=>rotate(w,i)).sort()[0];}
function paintGrid(items,mode,n){
 const shown=items.slice(0,48),w=760,rowH=70,columns=mode==='composition'?3:2,h=45+Math.ceil(shown.length/columns)*rowH;
 let b=`<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Enumerated ${esc(mode)} objects"><title>Exact enumeration; first ${shown.length} outcomes</title>`;
 for(let j=0;j<shown.length;j++){let x=30+(j%columns)*(w/columns),y=50+Math.floor(j/columns)*rowH;const v=shown[j];
  if(mode==='composition'){for(let i=0;i<v.length;i++){b+=`<rect x="${x+i*68}" y="${y-26}" width="60" height="38" rx="5" fill="#edf5f8" stroke="#83a5b5"/><text x="${x+i*68+30}" y="${y}" text-anchor="middle">${v[i]}</text>`;}b+=`<text x="${x}" y="${y+27}" font-size="13">ordered box occupancies</text>`;}
  else if(mode==='necklace'){for(let i=0;i<v.length;i++)b+=`<circle cx="${x+12+i*28}" cy="${y-6}" r="10" fill="${v[i]==='1'?'#ffdb8d':'#dceaf1'}" stroke="#557f90"/>`;b+=`<text x="${x}" y="${y+26}" font-size="14">rotation representative ${v}</text>`;}
  else {for(let i=1;i<=n;i++)b+=`<circle cx="${x+12+(i-1)*29}" cy="${y-6}" r="10" fill="${v.includes(i)?'#bde3d0':'#edf1f4'}" stroke="#557f90"/><text x="${x+12+(i-1)*29}" y="${y+21}" text-anchor="middle" font-size="13">${i}</text>`;}
 }
 return b+'</svg>';
}
const form=document.querySelector('#counting-form'),out=document.querySelector('#counting-output');
function calculate(e){e?.preventDefault();const f=new FormData(form),mode=f.get('mode'),n=Number(f.get('n')),k=Number(f.get('k'));
 if(!Number.isInteger(n)||!Number.isInteger(k)||n<1||n>8||k<0||k>8){out.textContent='Enter integer n from 1 to 8 and k from 0 to 8.';return;}
 let items=[],formula='',expected;
 if(mode==='subset'){items=subsets(n,k);expected=choose(n,k);formula='Unordered distinct k-subsets of n labeled positions.';}
 else if(mode==='gap'){items=subsets(n,k).filter(a=>a.every((v,i)=>i===0||v>a[i-1]+1));expected=k===0?1:(n>=2*k-1?choose(n-k+1,k):0);formula='Exactly k selected positions, with no adjacent selected pair.';}
 else if(mode==='composition'){if(k<1||k>4){out.textContent='For allocations, k is the number of labeled boxes and must be from 1 to 4.';return;}items=allocations(n,k);expected=choose(n+k-1,k-1);formula='n identical tokens in k labeled boxes, allowing empty boxes.';}
 else {items=[...new Set(words(n).filter(w=>[...w].filter(x=>x==='1').length===k).map(canonical))].sort();let fix=0;for(let r=0;r<n;r++)fix+=words(n).filter(w=>[...w].filter(x=>x==='1').length===k&&rotate(w,r)===w).length;expected=fix/n;formula='Binary n-seat rotation classes with exactly k ones; reflection remains distinct.';}
 if(items.length!==expected)throw Error('Enumeration disagrees with its independent formula');
 const label=mode==='composition'?'composition':mode==='necklace'?'necklace':'subset';out.innerHTML=`<h3>Exact count: ${math(items.length)}</h3><p>${esc(formula)}</p><p>Independent enumeration agrees with the corresponding ${mode==='necklace'?'fixed-word average':'closed counting formula'}. ${items.length>48?'The display shows the first 48 outcomes; the count includes every enumerated outcome.':'Every outcome is shown below.'}</p><div class="counting-lab-diagram">${paintGrid(items,label,n)}</div>`;out.dataset.count=items.length;window.MathLayout?.schedule();
}
if(form){form.onsubmit=calculate;form.querySelector('[name=mode]').onchange=calculate;calculate();}
window.CountingLab={choose,subsets,allocations,words,canonical,calculate};
})();
