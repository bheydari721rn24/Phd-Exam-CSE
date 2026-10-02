const assert=require('node:assert/strict');
const {gate,rows,hazard}=require('../dist/chapters/g_gates-lab.js');
let count=0;function check(a,b){assert.deepEqual(a,b);count++;}
for(const name of ['AND','OR','NAND','NOR','XOR','XNOR'])for(let n=2;n<=4;n++){
 const table=rows(name,n);check(table.length,2**n);
 for(let i=0;i<2**n;i++){
  const bits=Array.from({length:n},(_,j)=>(i>>(n-1-j))&1),sum=bits.reduce((a,b)=>a+b,0);
  const oracle={AND:sum===n?1:0,OR:sum>0?1:0,NAND:sum===n?0:1,NOR:sum>0?0:1,XOR:sum%2,XNOR:1-sum%2};
  check(table[i].bits,bits);check(table[i].multi,oracle[name]);
 }
}
// Independent event batching oracle for exact transport OR response.
for(let a=0;a<=5;a++)for(let b=0;b<=5;b++)for(let c=0;c<=5;c++)for(let d=0;d<=5;d++){
 const batches=new Map();for(const [t,p,v]of [[b,0,0],[a+c,1,1]]){if(!batches.has(t))batches.set(t,[]);batches.get(t).push([p,v]);}
 const state=[1,0];let out=1,events=[];
 for(const [t,batch]of [...batches].sort((u,v)=>u[0]-v[0])){
  batch.forEach(([p,v])=>state[p]=v);const next=state[0]|state[1];if(next!==out){events.push([t+d,next]);out=next;}
 }
 const r=hazard(a,b,c,d);check(r.fall,events.length?events[0][0]:null);check(r.rise,events.length?events[1][0]:null);check(r.width,events.length?events[1][0]-events[0][0]:0);check(r.protected,1);
}
for(const args of [[-1,1,1,1],[1,21,1,1],[NaN,1,1,1],[Infinity,1,1,1]]){assert.throws(()=>hazard(...args));count++;}
for(const args of [['INVALID',[0,1]],['AND',[0,2]],['OR',[]]]){assert.throws(()=>gate(...args));count++;}
check(hazard(3,1,1,2).width,3);check(hazard(.5,1,.75,2).width,.25);
console.log(JSON.stringify({assertions:count,transportCases:1296,gateRows:168}));
