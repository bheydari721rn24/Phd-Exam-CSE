/* Exact, independently rendered inclusion traces and bounded enumeration laboratory. */
"use strict";
(() => {
const reduced=matchMedia('(prefers-reduced-motion: reduce)'),esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const choose=(n,k)=>{if(k<0||k>n)return 0;let r=1;for(let j=1;j<=Math.min(k,n-k);j++)r=r*(n-Math.min(k,n-k)+j)/j;return r;};
const math=n=>`<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>${n}</mn></math>`;
const states=[];
function mount(host,model){
 const q=s=>host.querySelector(s),api=TeachingTransitions.raw({host,model,stage:q('.inclusion-stage'),caption:q('.inclusion-caption'),formula:q('.inclusion-formula'),seek:q('[data-seek]'),progress:q('[data-progress]'),play:q('[data-play]'),speed:q('[data-speed]'),prev:q('[data-prev]'),next:q('[data-next]'),reset:q('[data-reset]'),printRoot:q('.inclusion-print-trace')});states.push(api.pause);
}
fetch('d_inclusion-models.json').then(r=>{if(!r.ok)throw Error('Trace data unavailable');return r.json();}).then(data=>{for(const m of data.models){const host=document.querySelector(`[data-inclusion-model="${m.id}"]`);if(host)mount(host,m);}document.documentElement.dataset.inclusionLoaded='true';}).catch(e=>{document.querySelectorAll('.inclusion-error').forEach(x=>{x.hidden=false;x.textContent='The trace could not load. Its static diagram and lesson remain available; reload to retry.';});console.error(e);});
addEventListener('beforeprint',()=>states.forEach(stop));addEventListener('pagehide',()=>states.forEach(stop));reduced.addEventListener('change',()=>states.forEach(stop));

function maps(n,m){const out=[];function go(a){if(a.length===n){out.push(a.slice());return;}for(let x=0;x<m;x++)go([...a,x]);}go([]);return out;}
function permutations(n){const out=[];function go(a,remaining){if(!remaining.length){out.push(a);return;}for(const x of remaining)go([...a,x],remaining.filter(y=>y!==x));}go([],Array.from({length:n},(_,i)=>i));return out;}
function allocations(n,m){const out=[];function go(a,left){if(a.length===m-1){out.push([...a,left]);return;}for(let x=0;x<=left;x++)go([...a,x],left-x);}go([],n);return out;}
function factorial(n){let z=1;for(let i=2;i<=n;i++)z*=i;return z;}
function atomTable(atoms){const G=atoms.map((_,mask)=>atoms.reduce((s,v,i)=>s+((i&mask)===mask?v:0),0));const N=Array(4).fill(0);atoms.forEach((v,i)=>N[i.toString(2).replace(/0/g,'').length]+=v);let signed=G[0];for(let mask=1;mask<8;mask++)signed+=(-1)**mask.toString(2).replace(/0/g,'').length*G[mask];return{G,N,none:signed,union:G[0]-signed};}
function evaluate(mode,n,m,cap,atoms){
 if(mode==='sets'){
  if(!Array.isArray(atoms)||atoms.length!==8||atoms.some(x=>!Number.isInteger(x)||x<0||x>50))throw Error('Enter exactly eight integer atom counts from 0 to 50, separated by commas.');
  const table=atomTable(atoms);if(table.none!==atoms[0])throw Error('Atom complement and signed sum disagree');return{count:table.union,items:atoms,table};
 }
 if(!Number.isInteger(n)||n<0||n>8||!Number.isInteger(m)||m<0||m>4)throw Error('Enter integer n from 0 to 8 and m from 0 to 4.');
 let items,expected;
 if(mode==='maps'){
  items=maps(n,m).filter(a=>new Set(a).size===m);expected=0;for(let j=0;j<=m;j++)expected+=(-1)**j*choose(m,j)*(m-j)**n;
 }else if(mode==='permutations'){
  if(m>n)throw Error('The forbidden-position count m cannot exceed n.');items=permutations(n).filter(a=>a.slice(0,m).every((v,i)=>v!==i));expected=0;for(let j=0;j<=m;j++)expected+=(-1)**j*choose(m,j)*factorial(n-j);
 }else if(mode==='caps'){
  if(m<1)throw Error('Allocation mode requires one to four labeled boxes.');if(!Number.isInteger(cap)||cap<0||cap>5)throw Error('The cap must be an integer from 0 to 5.');items=allocations(n,m).filter(a=>a.every(x=>x<=cap));expected=0;for(let j=0;j<=m;j++){let left=n-j*(cap+1);expected+=(-1)**j*choose(m,j)*(left<0?0:choose(left+m-1,m-1));}
 }else throw Error('Select a supported exact model.');
 if(items.length!==expected)throw Error('Independent enumeration and formula disagree');return{count:items.length,items};
}
const tx=(x,y,s,size=16,cl='')=>`<text x="${x}" y="${y}" text-anchor="middle" font-size="${size}" ${cl?`class="${cl}"`:''}>${esc(s)}</text>`;
const ln=(x,y,u,v,c='#7da0ad',w=1.5)=>`<path d="M${x},${y} L${u},${v}" fill="none" stroke="${c}" stroke-width="${w}"/>`;
function paint(result,mode,n,m,cap){
 if(mode==='sets'){
  let b='<svg viewBox="0 0 760 540" role="img" aria-label="Exact three-set atoms and inclusive intersection table"><title>Exact regions and inclusive counts</title>'+tx(380,30,'Each mask specifies an exact membership region',21);
  b+=tx(130,75,'Mask',18)+tx(330,75,'Exact atom',18)+tx(570,75,'Inclusive intersection',18);
  for(let mask=0;mask<8;mask++){let y=115+mask*43;b+=tx(130,y,mask.toString(2).padStart(3,'0'),19,'math-label')+tx(330,y,result.items[mask],21,'math-label')+tx(570,y,result.table.G[mask],21,'math-label');}
  b+=tx(380,485,`Union ${result.count}; outside ${result.table.none}; total ${result.table.G[0]}`,20)+tx(380,525,'For mask 000, the inclusive count is the whole universe.',16);return b+'</svg>';
 }
 const shown=result.items.slice(0,24),columns=2,row=mode==='permutations'?300:mode==='maps'?240:200,h=60+Math.ceil(shown.length/2)*row;
 let b=`<svg viewBox="0 0 760 ${Math.max(h,150)}" role="img" aria-label="Actual ${esc(mode)} outcomes"><title>First ${shown.length} qualifying objects</title>`;
 if(!shown.length)b+=tx(380,95,'No qualifying object exists for these inputs.',21);
 shown.forEach((a,i)=>{const x=20+(i%columns)*380,y=35+Math.floor(i/columns)*row;b+=tx(x+170,y,`Object ${i+1}`,16);
  if(mode==='maps'){
   if(n===0)b+=tx(x+170,y+85,'Empty function',19);
   for(let j=0;j<n;j++){let xx=x+35+j*35;b+=`<circle cx="${xx}" cy="${y+55}" r="11" fill="#c4e8d8"/>`+tx(xx,y+30,j+1,14,'math-label');const dest=x+70+a[j]*70;b+=ln(xx,y+66,dest,y+136);}
   for(let j=0;j<m;j++){let xx=x+70+j*70;b+=`<rect x="${xx-20}" y="${y+140}" width="40" height="32" fill="#ffd894" stroke="#7395a8"/>`+tx(xx,y+163,j+1,17,'math-label');}
   b+=tx(x+170,y+204,'Every labeled output is used.',15);
  }else if(mode==='permutations'){
   if(n===0)b+=tx(x+170,y+70,'Empty permutation',19);
   for(let rr=0;rr<n;rr++)for(let cc=0;cc<n;cc++){let xx=x+45+cc*25,yy=y+37+rr*25;b+=`<rect x="${xx}" y="${yy}" width="23" height="23" fill="${rr===cc&&rr<m?'#f6d0c4':'#f2f7fa'}" stroke="#a5bcc7"/>`;if(a[rr]===cc)b+=`<circle cx="${xx+11.5}" cy="${yy+11.5}" r="7" fill="#27775f"/>`;}
   for(let j=0;j<n;j++)b+=tx(x+56+j*25,y+29,j+1,13,'math-label')+tx(x+27,y+55+j*25,j+1,13,'math-label');b+=tx(x+170,y+266,'Green cells: actual assignments; red: forbidden.',13);
  }else{
   for(let j=0;j<m;j++){const xx=x+18+j*80;b+=`<rect x="${xx}" y="${y+45}" width="70" height="85" rx="5" fill="#e9f2f7" stroke="#7395a8"/>`+tx(xx+35,y+32,`box ${j+1}`,14);for(let k=0;k<a[j];k++)b+=`<circle cx="${xx+16+(k%3)*19}" cy="${y+62+Math.floor(k/3)*28}" r="7" fill="#27775f"/>`;b+=tx(xx+35,y+156,`${a[j]} ≤ ${cap}`,15,'math-label');}
  }
 });return b+'</svg>';
}
const form=document.querySelector('#inclusion-form'),out=document.querySelector('#inclusion-output');
function calculate(e){e?.preventDefault();const f=new FormData(form),mode=f.get('mode'),n=Number(f.get('n')),m=Number(f.get('m')),cap=Number(f.get('cap'));try{
 const raw=String(f.get('atoms')).split(',').map(x=>x.trim());if(mode==='sets'&&raw.some(x=>!/^\d+$/.test(x)))throw Error('Each exact atom must be a nonnegative integer.');const atoms=raw.map(Number),result=evaluate(mode,n,m,cap,atoms);
 out.dataset.count=result.count;out.innerHTML=`<h3>Exact count: ${math(result.count)}</h3><p>${mode==='sets'?'Union count from exact regions agrees with the complete signed intersection sum.':'Every qualifying object was independently enumerated and compared with its inclusion-exclusion expression.'} ${mode!=='sets'&&result.count>24?'The diagram shows the first 24 objects; all objects contribute to the count.':''}</p><div class="inclusion-lab-diagram">${paint(result,mode,n,m,cap)}</div>`;window.MathLayout?.schedule();
 }catch(error){delete out.dataset.count;out.textContent=error.message;}
}
if(form){form.onsubmit=calculate;form.querySelector('[name=mode]').onchange=()=>{const mode=form.elements.mode.value;for(const key of ['n','m','cap'])form.elements[key].closest('label').hidden=mode==='sets'||(key==='cap'&&mode!=='caps');form.elements.atoms.closest('label').hidden=mode!=='sets';calculate();};form.elements.mode.dispatchEvent(new Event('change'));}
window.InclusionLab={evaluate,maps,permutations,allocations,factorial,atomTable,calculate};

})();
