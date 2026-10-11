'use strict';
(()=>{
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function law(s){
 for(const k of['n','r','N','K','limit'])if(s[k]!==undefined&&(!Number.isInteger(s[k])||s[k]<0))throw Error('Count parameters must be nonnegative integers.');
 if(!Number.isFinite(s.p)||s.p<0||s.p>1)throw Error('The success probability must lie between zero and one.');
 if(!Number.isInteger(s.limit)||s.limit<1||s.limit>12)throw Error('Use a display limit from one through twelve.');
 if(['binomial','hypergeometric'].includes(s.kind)&&(!Number.isInteger(s.n)||s.n<0||s.n>12))throw Error('Use a sample or trial count from zero through twelve.');
 let masses,tail=0,mean,variance;
 const choose=(n,k)=>{if(k<0||k>n)return 0;let v=1;for(let j=1;j<=k;j++)v*= (n-j+1)/j;return v;};
 if(s.kind==='binomial'){
  masses=Array.from({length:s.n+1},(_,k)=>({x:k,p:choose(s.n,k)*s.p**k*(1-s.p)**(s.n-k)}));mean=s.n*s.p;variance=mean*(1-s.p);
 }else if(s.kind==='geometric'){
  if(s.p===0)throw Error('Finite geometric waiting needs a positive success probability.');
  masses=Array.from({length:s.limit},(_,k)=>({x:k+1,p:s.p*(1-s.p)**k}));tail=(1-s.p)**s.limit;mean=1/s.p;variance=(1-s.p)/s.p**2;
 }else if(s.kind==='negative-binomial'){
  if(s.p===0||!Number.isInteger(s.r)||s.r<1||s.r>6)throw Error('Use positive success probability and a success target from one through six.');
  masses=Array.from({length:s.limit+1},(_,f)=>({x:f+s.r,p:choose(f+s.r-1,s.r-1)*s.p**s.r*(1-s.p)**f}));tail=Math.max(0,1-masses.reduce((t,a)=>t+a.p,0));mean=s.r/s.p;variance=s.r*(1-s.p)/s.p**2;
 }else if(s.kind==='hypergeometric'){
  if(!Number.isInteger(s.N)||s.N<1||s.N>30||!Number.isInteger(s.K)||s.K<0||s.K>s.N||s.n>s.N)throw Error('Use population one through thirty, marks zero through N and sample size no larger than N.');
  const lo=Math.max(0,s.n-s.N+s.K),hi=Math.min(s.n,s.K);
  masses=Array.from({length:hi-lo+1},(_,i)=>({x:i+lo,p:choose(s.K,i+lo)*choose(s.N-s.K,s.n-i-lo)/choose(s.N,s.n)}));mean=s.n*s.K/s.N;variance=s.N===1?0:s.n*(s.K/s.N)*(1-s.K/s.N)*(s.N-s.n)/(s.N-1);
 }else if(s.kind==='poisson'){
  if(!Number.isFinite(s.lambda)||s.lambda<0||s.lambda>8)throw Error('Use a Poisson parameter from zero through eight.');
  masses=[{x:0,p:Math.exp(-s.lambda)}];for(let k=1;k<=s.limit;k++)masses.push({x:k,p:masses[k-1].p*s.lambda/k});
  tail=Math.max(0,1-masses.reduce((t,a)=>t+a.p,0));mean=variance=s.lambda;
 }else throw Error('Select a supported count or waiting-time law.');
 return{masses,tail,mean,variance};
}
function mount(host,m){
 const c=document.createElement('div');c.className='sd-controls';c.innerHTML='<button data-reset>Restart</button><button data-prev>Previous</button><button data-play>Play</button><button data-next>Next</button><label>Speed<select data-speed></select></label><label>Step<input type="range" data-seek min="0" value="0"></label>';host.querySelector('.sd-stage').before(c);
 for(const cls of['sd-caption','sd-formula','sd-print'])if(!host.querySelector('.'+cls)){const e=document.createElement('div');e.className=cls;host.append(e);}
 return AdvancedSimulations.mount(host,m,{topic:'s_distributions',prefix:'sd',retainDrawing:true});
}
if(typeof module!=='undefined')module.exports={law};if(typeof document==='undefined')return;
async function boot(){
 const data=await(await fetch('s_distributions-models.json')).json();globalThis.DistributionPlayers=[];
 for(const h of document.querySelectorAll('[data-sd-model]')){const m=data.models.find(m=>m.id===h.dataset.sdModel);if(!m)throw Error('Missing distribution model '+h.dataset.sdModel);DistributionPlayers.push(mount(h,m));}
 const form=document.querySelector('#sd-form'),out=document.querySelector('#sd-output'),error=document.querySelector('#sd-error');
 form.addEventListener('submit',e=>{e.preventDefault();try{
  const spec={kind:form.elements.kind.value};for(const k of['n','r','N','K','limit','p','lambda']){const value=form.elements[k].value.trim();if(!value)throw Error('Every parameter field must contain a value.');spec[k]=Number(value);}
  const z=law(spec),w=620/z.masses.length,tx=(x,y,t)=>'<text x="'+x+'" y="'+y+'" class="sd-math" text-anchor="middle">'+esc(t)+'</text>';
  const svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-label="Editable exact law, fixed probability scale zero through one"><path d="M65 280H710M65 85V280" stroke="#658899" fill="none"/>'+z.masses.map((a,i)=>'<rect x="'+(70+i*w)+'" y="'+(280-190*a.p)+'" width="'+(w-10)+'" height="'+190*a.p+'" fill="#8cb9ad"/>'+tx(70+i*w+(w-10)/2,307,a.x)).join('')+'</svg>';
  out.innerHTML='<h3>Your '+esc(spec.kind)+' law</h3><div class="sd-stage">'+svg+'</div><p>Displayed probabilities use a fixed vertical scale from zero through one. The omitted tail remains part of the law and is not renormalized.</p><pre>'+esc(JSON.stringify({...z,inputs:spec},null,2))+'</pre>';globalThis.DistributionLab={spec,result:z};error.textContent='';
 }catch(ex){error.textContent=ex.message;}});
 form.dispatchEvent(new Event('submit',{cancelable:true}));
}
boot().catch(e=>{document.querySelector('#sd-error').textContent=e.message;throw e;});
})();
