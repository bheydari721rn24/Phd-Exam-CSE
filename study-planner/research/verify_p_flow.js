'use strict';
const assert = require('node:assert/strict');
const {traceFlow} = require('../dist/chapters/p_flow-lab.js');
let cases = 0;
for (const mode of ['for','while','do','bug','break']) {
  for (let n = 0; n <= 12; n++) for (let a = 0; a <= 12; a++) {
    const t = traceFlow(mode,n,a); assert(t.valid);
    let values = Array.from({length:Math.max(0,n-a)},(_,k)=>a+k);
    let expectedStatus = 'normal', expectedI = Math.max(a,n);
    if (mode === 'do' && values.length === 0) {values=[a]; expectedI=a+1;}
    if (mode === 'break' && values.includes(3)) {
      values=values.filter(x=>x<3); expectedStatus='break'; expectedI=3;
    }
    if (mode === 'bug') {
      const stuck=values.find(x=>x%2===0);
      if (stuck!==undefined) {values=values.filter(x=>x<stuck); expectedStatus='cycle'; expectedI=stuck;}
    }
    const accumulated=mode==='for'?values.filter(x=>x%2):values;
    assert.equal(t.sum,accumulated.reduce((s,x)=>s+x,0),`${mode},${n},${a}`);
    assert.equal(t.i,expectedI); assert.equal(t.status,expectedStatus);
    const expectedEntries=values.length+(expectedStatus==='break'||expectedStatus==='cycle'?1:0);
    assert.equal(t.entries,expectedEntries);
    assert.equal(t.updates,values.length);
    assert.equal(t.tests,mode==='do'?values.length:expectedEntries+(expectedStatus==='normal'?1:0));
    assert(t.rows.every(row=>row.i>=0 && row.i<=13 && row.sum>=0 && row.sum<=90));
    cases++;
  }
}
for(const input of [['for',1.5,0],['for',0,-1],['for',13,0],['for',0,NaN],['other',1,1]]) {
  assert.equal(traceFlow(...input).valid,false);cases++;
}
console.log(`${cases} execution-model cases passed: five modes, all 169 input pairs each, independent closed-form results, transfer counts, cycles and invalid inputs.`);
