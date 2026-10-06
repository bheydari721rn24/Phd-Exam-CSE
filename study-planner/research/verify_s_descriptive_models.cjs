const assert=require('node:assert/strict'),fs=require('node:fs');
const S=require('../dist/chapters/s_descriptive.js');
let seed=60406,cases=0;const rand=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;};
const eq=(a,b)=>assert.ok(a===b||Math.abs(a-b)<1e-8*Math.max(1,Math.abs(a),Math.abs(b)),`${a} differs from ${b}`);
const total=a=>a.reduce((x,y)=>x+y,0);
const direct=a=>{const n=a.length,mean=total(a)/n,m2=total(a.map(x=>(x-mean)**2));return {n,mean,m2,v:m2/n};};
function qref(a,p){const b=a.slice().sort((a,b)=>a-b),h=(b.length-1)*p,l=Math.floor(h),u=Math.ceil(h);return (1-(h-l))*b[l]+(h-l)*b[u];}
for(let t=0;t<120;t++){
 const a=Array.from({length:1+rand()%12},()=>rand()%41-20),z=direct(a),stream=S.stream(a),variance=S.variance(a);for(const key of ['mean','m2','v']){eq(stream.result[key],z[key]);eq(variance.result[key],z[key]);}
 const k=rand()%9-4,b=rand()%21-10,tr=S.affine(a,k,b).result;eq(tr.mean,k*z.mean+b);eq(tr.v,k*k*z.v);
 const box=S.box(a).result;eq(box.q1,qref(a,.25));eq(box.median,qref(a,.5));eq(box.q3,qref(a,.75));assert.deepEqual(box.outliers,a.filter(v=>v<box.lower||v>box.upper));
 for(const p of [0,.25,.5,.75,1])eq(S.quant(a,p),qref(a,p));
 const h=S.histogram(a,[-21,-10,0,10,21]).result;assert.deepEqual(h.counts,[-21,-10,0,10].map((lo,j)=>a.filter(x=>x>=lo&&(x<[-10,0,10,21][j]||j===3&&x===21)).length));eq(h.area,1);
 const ecdf=S.ecdf(a).result;for(const row of ecdf){eq(row.before,a.filter(x=>x<row.value).length/a.length);eq(row.after,a.filter(x=>x<=row.value).length/a.length);}
 const v=Array.from({length:a.length},()=>rand()%41-20),V=direct(v),c=total(a.map((x,i)=>(x-z.mean)*(v[i]-V.mean))),corr=S.correlation(a,v).result;eq(corr.cross,c);if(z.m2&&V.m2)eq(corr.r,c/Math.sqrt(z.m2*V.m2));else assert.equal(corr.r,null);
 const merge=S.pooling(a,v).result,U=direct([...a,...v]);eq(merge.mean,U.mean);eq(merge.m2,U.m2);eq(merge.within+merge.between,U.m2);
 const width=1+rand()%12,ma=S.smoothing(a,width).result;ma.forEach((r,i)=>{const window=a.slice(Math.max(0,i-width+1),i+1);eq(r,total(window)/window.length);});
 const lambda=(1+rand()%10)/10,ewma=S.smoothing(a,lambda,true).result;ewma.forEach((r,i)=>eq(r,total(a.slice(0,i+1).map((x,j)=>lambda*(1-lambda)**(i-j)*x))));
 const loss=S.center(a,'loss',true),sort=a.slice().sort((a,b)=>a-b),lower=sort[Math.ceil(a.length/2)-1],upper=sort[Math.floor(a.length/2)];assert.deepEqual(loss.result.minimizer,[lower,upper]);eq(loss.result.minimum,total(a.map(v=>Math.abs(v-(lower+upper)/2))));
 cases+=12;
}
assert.deepEqual(S.histogram([0,1,1,2,3,4],[0,1,2,4]).result.counts,[1,2,3]);
const b=S.box([1,2,3,4,5,6,7,20]).result;assert.deepEqual([b.q1,b.median,b.q3,b.lower,b.upper],[2.75,4.5,6.25,-2.5,11.5]);assert.deepEqual(b.whiskers,[1,7]);assert.deepEqual(b.outliers,[20]);
eq(S.correlation([-1,0,1],[1,0,1]).result.r,0);assert.equal(S.correlation([2,2,2],[1,3,8]).result.r,null);assert.deepEqual(S.smoothing([2,4,10],.5,true).result,[1,2.5,6.25]);
const data=S.fixtures();assert.equal(data.models.length,28);assert.equal(new Set(data.models.map(m=>m.id)).size,28);let checkpoints=0;
for(const m of data.models){assert.ok(m.frames.length>1);for(const f of m.frames){assert.ok(f.teaching.operation&&f.teaching.why&&f.svg.includes('data-visual-type="plot"'));assert.ok(!f.svg.includes('<rect'));assert.deepEqual(f.snapshot,f.teaching.currentState);assert.ok(f.teaching.checks.every(c=>c.mathHtml.includes('<math')));checkpoints++;}}
fs.writeFileSync('dist/chapters/s_descriptive-models.json',JSON.stringify(data,null,2)+'\n');
fs.writeFileSync('research/s_descriptive-evidence/models.json',JSON.stringify({status:'passed',seed:60406,randomizedAlgorithmComparisons:cases,models:28,storedCheckpoints:checkpoints,contracts:['histogram endpoints and area','ECDF left limits and ties','quantile interpolation','variance and Welford','affine invariance','type-7 box fences and observed whiskers','within/between decomposition','paired correlation degeneracy','moving-average startup','EWMA expansion and initialization','absolute-loss minimizer interval'],limits:'Finite seeded verification, not a universal proof or browser-layout check.'},null,2)+'\n');console.log(cases+' finite model comparisons passed; '+checkpoints+' checkpoints.');
