/* Exact arithmetic in the documented, safely bounded laboratory. */
(function(){
'use strict';
function egcd(a,b){
 let r0=Math.abs(a),r1=Math.abs(b),s0=1,s1=0,t0=0,t1=1;
 while(r1!==0){const q=Math.floor(r0/r1);[r0,r1]=[r1,r0-q*r1];[s0,s1]=[s1,s0-q*s1];[t0,t1]=[t1,t0-q*t1];}
 return [r0,a<0?-s0:s0,b<0?-t0:t0];
}
const mod=(a,m)=>((a%m)+m)%m;
function analyze(a,b,m){
 if(![a,b,m].every(Number.isSafeInteger)||Math.abs(a)>10000||Math.abs(b)>10000||m<1||m>60)throw new RangeError('Use integer coefficients from −10000 through 10000 and a modulus from 1 through 60.');
 const [g,s,t]=egcd(a,m),target=mod(b,m),solutions=[];
 if(a*s+m*t!==g)throw new Error('The internal Bézout certificate failed exact substitution.');
 if(b%g===0){const reduced=m/g,x0=mod(s*(b/g),reduced);for(let k=0;k<g;k++)solutions.push(x0+k*reduced);}
 const map=Array.from({length:m},(_,x)=>mod(a*x,m));
 return {a,b,m,g,s,t,target,solutions,map,kernel:map.flatMap((y,x)=>y===0?[x]:[]),image:[...new Set(map)].sort((x,y)=>x-y),inverse:g===1?mod(s,m):null};
}
if(typeof module!=='undefined')module.exports={egcd,analyze};
if(typeof document==='undefined')return;
const presets={unit:[5,7,12],many:[8,4,12],none:[8,6,12],zero:[0,0,6],negative:[-3,1,7]};
const inputs=['a','b','m'].map(k=>document.getElementById('number-'+k)),out=document.getElementById('number-output'),form=document.getElementById('number-form');
const math=s=>'<span class="math-inline">'+s+'</span>';
function render(){
 inputs.forEach(i=>i.setCustomValidity(''));
 if(!form.checkValidity()){form.reportValidity();return;}
 let r;try{r=analyze(...inputs.map(i=>Number(i.value)));}catch(e){inputs[0].setCustomValidity(e.message);form.reportValidity();return;}
 out.dataset.count=String(r.solutions.length);out.dataset.gcd=String(r.g);out.dataset.inverse=r.inverse===null?'none':String(r.inverse);
 const rows=[['Bézout certificate',math(r.s+' × ('+r.a+') + '+r.t+' × '+r.m+' = '+r.g)],['Normalized target',math(r.target)],['Unit coefficient',r.inverse===null?'No; division by this coefficient is not valid at the original modulus.':'Yes; its inverse is '+math(r.inverse)+'.'],['Solvability',r.solutions.length?'The gcd divides the target. There are exactly '+math(r.g)+' solutions.':'The gcd does not divide the target. There are no solutions.'],['Canonical solutions',math(r.solutions.length?r.solutions.join(', '):'∅')],['Kernel',math('{'+r.kernel.join(', ')+'}')],['Image',math('{'+r.image.join(', ')+'}')]];
 out.innerHTML='<dl>'+rows.map(([k,v])=>'<dt>'+k+'</dt><dd>'+v+'</dd>').join('')+'</dl><p>Each cell shows '+math('x → ax mod m')+'. Green cells satisfy the target congruence.</p><div class="map-grid">'+r.map.map((y,x)=>'<div class="map-cell'+(y===r.target?' solution':'')+'">'+x+' → '+y+'</div>').join('')+'</div>';
}
form.addEventListener('submit',e=>{e.preventDefault();render();});inputs.forEach(i=>i.addEventListener('change',render));
document.querySelectorAll('[data-preset]').forEach(button=>button.addEventListener('click',()=>{presets[button.dataset.preset].forEach((v,i)=>inputs[i].value=v);render();}));
render();
})();
