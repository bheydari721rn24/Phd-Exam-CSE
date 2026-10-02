/* Independent graph oracles: transitive closure and topological deletion. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {analyzeSystem} = require('../dist/chapters/d_invariants.js');
let cases = 0, rankCases = 0;
for (let mask = 0; mask < 512; mask++) {
  const adj = Array.from({length:3},(_,s)=>Array.from({length:3},(_,t)=>!!(mask & (1 << (s*3+t)))));
  const trans = adj.map(row=>row.slice());
  for (let k=0;k<3;k++)for(let s=0;s<3;s++)for(let t=0;t<3;t++)trans[s][t] ||= trans[s][k] && trans[k][t];
  for (let init=0;init<8;init++) for (let pred=0;pred<8;pred++) {
    const initial=[0,1,2].filter(s=>init>>s&1),property=[0,1,2].map(s=>!!(pred>>s&1));
    const reached=[0,1,2].filter(t=>initial.includes(t)||initial.some(s=>trans[s][t]));
    const indeg=Array(3).fill(0);for(const s of reached)for(const t of reached)if(adj[s][t])indeg[t]++;
    const ready=reached.filter(s=>indeg[s]===0);let removed=0;
    for(let head=0;head<ready.length;head++){const s=ready[head];removed++;for(const t of reached)if(adj[s][t]&&--indeg[t]===0)ready.push(t);}
    const r=analyzeSystem(adj,initial,property,[2,1,0]);
    assert.deepEqual(r.reachable,reached);assert.equal(r.initialized,initial.every(s=>property[s]));
    const bad=[];for(let s=0;s<3;s++)for(let t=0;t<3;t++)if(adj[s][t]&&property[s]&&!property[t])bad.push([s,t]);
    assert.deepEqual(r.closureViolations,bad);assert.equal(r.safe,reached.every(s=>property[s]));
    assert.equal(r.terminates,removed===reached.length);
    if(r.unsafePath){assert(initial.includes(r.unsafePath[0]));assert(!property[r.unsafePath.at(-1)]);for(let i=1;i<r.unsafePath.length;i++)assert(adj[r.unsafePath[i-1]][r.unsafePath[i]]);}
    if(r.cycle){assert.equal(r.cycle[0],r.cycle.at(-1));assert(r.cycle.every(s=>reached.includes(s)));for(let i=1;i<r.cycle.length;i++)assert(adj[r.cycle[i-1]][r.cycle[i]]);}
    cases++;
  }
  for(let vals=0;vals<64;vals++){
    const ranks=[vals&3,(vals>>2)&3,(vals>>4)&3];const r=analyzeSystem(adj,[0],[true,true,true],ranks);
    const bad=[];for(const s of r.reachable)for(let t=0;t<3;t++)if(adj[s][t]&&ranks[t]>=ranks[s])bad.push([s,t]);
    assert.deepEqual(r.rankViolations,bad);if(!bad.length)assert(r.terminates);rankCases++;
  }
}
for(const args of [[[[true,false]],[0],[true],[0]],[[[true]],[1],[true],[0]],[[[true]],[0],[true],[-1]],[[[true]],[0],[true],[0.5]]])assert.throws(()=>analyzeSystem(...args));
const report={graphInitialPredicateCases:cases,rankAssignmentCases:rankCases,independentOracles:'Floyd transitive closure and topological vertex deletion',witnessesChecked:true};
fs.writeFileSync(path.join(__dirname,'d_invariants-lab-check.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
