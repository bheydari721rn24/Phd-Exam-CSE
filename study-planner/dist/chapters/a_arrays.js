/* Array storage and actual linked topology; exact editable laboratories. */
"use strict";
(() => {
const reduced=matchMedia('(prefers-reduced-motion: reduce)'),esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const choose=(n,k)=>{if(k<0||k>n)return 0;let r=1;for(let j=1;j<=Math.min(k,n-k);j++)r=r*(n-Math.min(k,n-k)+j)/j;return r;};
const math=n=>`<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>${n}</mn></math>`;
const states=[];
function mount(host,model){
 const q=s=>host.querySelector(s),api=TeachingTransitions.raw({host,model,stage:q('.arrays-stage'),caption:q('.arrays-caption'),formula:q('.arrays-formula'),seek:q('[data-seek]'),progress:q('[data-progress]'),play:q('[data-play]'),speed:q('[data-speed]'),prev:q('[data-prev]'),next:q('[data-next]'),reset:q('[data-reset]'),printRoot:q('.arrays-print-trace')});states.push(api.pause);
}
fetch('a_arrays-models.json?v=ports-2').then(r=>{if(!r.ok)throw Error('Trace data unavailable');return r.json();}).then(data=>{for(const m of data.models){const host=document.querySelector(`[data-arrays-model="${m.id}"]`);if(host)mount(host,m);}document.documentElement.dataset.arraysLoaded='true';}).catch(e=>{document.querySelectorAll('.arrays-error').forEach(x=>{x.hidden=false;x.textContent='The trace could not load. Its static diagram and lesson remain available; reload to retry.';});console.error(e);});
addEventListener('beforeprint',()=>states.forEach(stop));addEventListener('pagehide',()=>states.forEach(stop));reduced.addEventListener('change',()=>states.forEach(stop));


function evaluate(mode,params){
 const int=(v,a,b,name)=>{if(!Number.isInteger(v)||v<a||v>b)throw Error(`${name} must be an integer from ${a} to ${b}.`);return v;};
 if(mode==='growth'){
  const m=int(params.m,1,64,'Appends'),c0=int(params.c0,1,16,'Initial capacity'),g=int(params.g,2,4,'Growth factor');let C=c0,n=0,copies=0,states=[{n,C,copies,last:0}];
  for(let t=0;t<m;t++){let last=0;if(n===C){last=n;copies+=n;C*=g;}n++;states.push({n,C,copies,last});}
  return{mode,m,c0,g,copies,writes:copies+m,capacity:C,states};
 }
 if(mode==='shift'){
  const a=params.values;if(!Array.isArray(a)||a.length<1||a.length>8||a.some(v=>!Number.isInteger(v)||Math.abs(v)>99))throw Error('Use one to eight integers from −99 to 99.');
  const i=int(params.index,0,a.length,'Insertion rank'),x=int(params.value,-99,99,'New value');let v=a.map((x,j)=>({id:'v'+j,value:x}));v.push(null);let states=[{values:v.map(x=>x&&{...x}),writes:0,caption:'Original array plus one spare slot.'}];let writes=0;
  for(let j=a.length;j>i;j--){v[j]={...v[j-1]};writes++;states.push({values:v.map(x=>x&&{...x}),writes,caption:`Copy source ${j-1} backward to ${j}.`});}
  v[i]={id:'new',value:x};writes++;states.push({values:v.map(x=>x&&{...x}),writes,caption:'Write the new value at the supplied rank.'});return{mode,index:i,result:v.map(x=>x.value),writes,shifts:writes-1,states};
 }
 if(mode==='reverse'){
  const n=int(params.n,0,7,'Node count');let next=Array.from({length:n},(_,i)=>i+1<n?i+1:null),prev=null,cur=n?0:null,states=[];let writes=0;
  while(true){states.push({next:[...next],prev,cur,writes});if(cur===null)break;let saved=next[cur];next[cur]=prev;prev=cur;cur=saved;writes++;}
  return{mode,n,head:prev,writes,states};
 }
 if(mode==='floyd'){
  const mu=int(params.mu,0,5,'Prefix length'),lam=int(params.lam,1,5,'Cycle length');let next=Array.from({length:mu+lam},(_,i)=>i+1<mu+lam?i+1:mu),s=0,f=0,t=0,states=[{s,f,t,phase:'detect'}];
  do{s=next[s];f=next[next[f]];t++;states.push({s,f,t,phase:'detect'});}while(s!==f);
  const meeting=t;let h=0,r=0;states.push({s:h,f,t:r,phase:'reset'});while(h!==f){h=next[h];f=next[f];r++;states.push({s:h,f,t:r,phase:'reset'});}
  return{mode,mu,lam,meeting,entry:h,resetSteps:r,states,next};
 }
 throw Error('Choose a supported laboratory.');
}
const tx=(x,y,t,size=16,box='',cl='')=>`<text x="${x}" y="${y}" text-anchor="middle" font-size="${size}" class="${cl}" ${box?`dominant-baseline="middle" data-label-for="${esc(box)}"`:''}>${esc(t)}</text>`;
function route(points,r=6){let d=`M${points[0]}`;for(let j=1;j<points.length-1;j++){const a=points[j-1],b=points[j],c=points[j+1],la=Math.hypot(a[0]-b[0],a[1]-b[1]),lc=Math.hypot(c[0]-b[0],c[1]-b[1]),q=Math.min(r,la/2,lc/2);if(!la||!lc)continue;const p=[b[0]+(a[0]-b[0])*q/la,b[1]+(a[1]-b[1])*q/la],v=[b[0]+(c[0]-b[0])*q/lc,b[1]+(c[1]-b[1])*q/lc];d+=` L${p} Q${b} ${v}`;}return d+` L${points.at(-1)}`;}
function arrow(points,source,target,kind='forward'){return`<path data-arrow="true" data-source="${esc(source)}" data-target="${esc(target)}" data-points="${esc(JSON.stringify(points))}" data-start="${points[0]}" data-end="${points.at(-1)}" d="${route(points)}" fill="none" stroke="${kind==='pointer'?'#7a739d':'#557e91'}" stroke-width="1.6" stroke-linejoin="round" marker-end="url(#lab-${kind})"/>`;}
function picture(z,f){
 let d='';
 if(z.mode==='growth'){
  const width=600;d+=tx(380,50,`Length ${f.n}, capacity ${f.C}`,19)+`<rect x="80" y="110" width="${width}" height="60" fill="#e9f3f5" stroke="#648c9f"/><rect x="80" y="110" width="${width*f.n/f.C}" height="60" fill="#89bbab"/>`;
  d+=tx(380,215,`${f.n} live slots; ${f.C-f.n} unused slots`,18)+tx(380,270,`${f.copies} cumulative copied slots`,18)+tx(380,325,`This append copied ${f.last} slots`,17);
 }else if(z.mode==='shift'){
  let w=650/f.values.length;f.values.forEach((v,i)=>{let x=55+i*w,key='array-'+i;d+=`<rect data-box="${key}" x="${x}" y="135" width="${w-5}" height="60" fill="#e9f3f5" stroke="#6c93a2"/>`+tx(x+(w-5)/2,227,i,14);if(v)d+=`<g data-entity="${v.id}">${tx(x+(w-5)/2,165,v.value,20,key)}</g>`;});d+=tx(380,65,`${f.writes} element writes`,19);
 }else{
  const next=z.mode==='reverse'?f.next:z.next,n=next.length,w=n>1?620/(n-1):0,x=i=>65+i*w,half=n>8?28:36,top=175,bottom=225;
  next.forEach((b,a)=>{let points;if(b===null){const key='null-'+a,ny=251;d+=arrow([[x(a),bottom],[x(a),ny]],'node-'+a,key)+`<rect data-box="${key}" x="${x(a)-47}" y="${ny}" width="94" height="30" rx="6" fill="#fff" stroke="#c4d3db"/>`+tx(x(a),ny+15,'next = null',12,key,'pointer-label');return;}
   if(a===b)points=[[x(a)+half,188],[x(a)+half+24,188],[x(a)+half+24,145],[x(a)+16,145],[x(a)+16,top]];
   else if(Math.abs(a-b)===1){const sign=b>a?1:-1;points=[[x(a)+sign*half,188],[x(b)-sign*half,188]];}
   else points=[[x(a)+16,top],[x(a)+16,145],[x(b)-16,145],[x(b)-16,top]];
   d+=arrow(points,'node-'+a,'node-'+b);
  });
  next.forEach((_,i)=>{const key='node-'+i;d+=`<g data-entity="${key}"><rect data-box="${key}" x="${x(i)-half}" y="${top}" width="${half*2}" height="50" rx="8" fill="#cfe5df" stroke="#659484"/>${tx(x(i),top+25,i,18,key)}</g>`;});
  const cursors=z.mode==='reverse'?{prev:f.prev,cur:f.cur}:{slow:f.s,fast:f.f};Object.entries(cursors).forEach(([name,i],j)=>{const cx=j?580:180,cy=57,key='cursor-'+name;d+=`<rect data-box="${key}" x="${cx-76}" y="${cy}" width="152" height="38" rx="7" fill="#fff" stroke="#bcb6ce"/>`+tx(cx,cy+19,name+(i===null?' = null':''),14,key,'pointer-label');if(i!==null){const u=x(i)+(j?10:-10),lane=115+j*20;d+=`<g data-entity="${key}">`+arrow([[cx,cy+38],[cx,lane],[u,lane],[u,top]],key,'node-'+i,'pointer')+'</g>';}});
  if(!n)d+=tx(380,200,'Empty list: no live nodes',18);
  d+=tx(380,335,z.mode==='reverse'?`${f.writes} rewritten successor fields`:`${f.phase}: ${f.t} complete iterations`,18);
 }
 return`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 410" role="img"><defs>${['forward','pointer'].map(k=>`<marker id="lab-${k}" markerUnits="userSpaceOnUse" markerWidth="7" markerHeight="6" viewBox="0 0 7 6" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="${k==='pointer'?'#7a739d':'#557e91'}"/></marker>`).join('')}</defs>${d}</svg>`;
}
const formula=f=>`<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>${esc(f)}</mtext></math>`;
const labHost=document.querySelector('#arrays-output');
function labModel(z){
 let title={growth:'Recomputed geometric growth',shift:'Recomputed stable insertion',reverse:'Recomputed linked-list reversal',floyd:'Recomputed Floyd detection and entry'}[z.mode];
 return{id:'editable',title,invariant:'Displayed values, links and cursors are recomputed from the selected input. The complete trace starts paused.',frames:z.states.map(f=>({svg:picture(z,f),caption:f.caption||(z.mode==='growth'?`After ${f.n} appends, capacity ${f.C}; this update copies ${f.last}.`:z.mode==='reverse'?`Reversed prefix contains ${f.writes} nodes; cur identifies the untouched suffix.`:`${f.phase} phase after ${f.t} complete iterations; cursor identities shown above.`),formulaHtml:formula(z.mode==='growth'?`n = ${f.n}; C = ${f.C}; copies = ${f.copies}`:z.mode==='shift'?`writes = ${f.writes}`:z.mode==='reverse'?`next writes = ${f.writes}`:`steps = ${f.t}`)}))};
}
function hostHtml(m){return`<section class="arrays-model" data-arrays-model="editable" tabindex="0"><h3>${esc(m.title)}</h3><p class="arrays-invariant">${esc(m.invariant)}</p><div class="arrays-stage"></div><p class="arrays-caption" aria-live="polite"></p><div class="arrays-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2200">Slow</option><option value="1400" selected>Normal</option><option value="850">Fast</option></select></label><label>Checkpoint<input data-seek type="range" min="0" max="${m.frames.length-1}" value="0"></label></div><p class="arrays-progress" data-progress></p><div class="formula-block arrays-formula"></div><div class="arrays-print-trace"></div></section>`;}
const form=document.querySelector('#arrays-form');
function fields(){const mode=form.mode.value;form.querySelectorAll('[data-modes]').forEach(x=>{x.hidden=!x.dataset.modes.split(' ').includes(mode);});}
function run(event){event?.preventDefault();states.forEach(stop=>stop());try{
 const raw=form.values.value.trim().split(',').map(x=>x.trim());if(form.mode.value==='shift'&&raw.some(x=>!/^[-+]?\d+$/.test(x)))throw Error('Use comma-separated integers with no empty values.');
 const z=evaluate(form.mode.value,{m:Number(form.m.value),c0:Number(form.c0.value),g:Number(form.g.value),values:raw.map(Number),index:Number(form.index.value),value:Number(form.value.value),n:Number(form.n.value),mu:Number(form.mu.value),lam:Number(form.lam.value)}),m=labModel(z);
 labHost.innerHTML=hostHtml(m);mount(labHost.firstElementChild,m);labHost.dataset.result=JSON.stringify(z);document.querySelector('#arrays-lab-error').textContent='';
 }catch(error){document.querySelector('#arrays-lab-error').textContent=error.message;}}
form.addEventListener('submit',run);form.mode.addEventListener('change',()=>{fields();run();});fields();run();
window.ArrayLab={evaluate,picture,labModel};
})();
