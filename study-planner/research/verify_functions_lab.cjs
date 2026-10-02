const assert=require('node:assert/strict');
const fs=require('node:fs');
const {analyzeFiniteFunction}=require('../dist/chapters/d_functions.js');
let cases=0, subsets=0;
function tuples(m,n,p=[]){if(m===0)return [p];return Array.from({length:n},(_,j)=>tuples(m-1,n,[...p,j])).flat();}
for(let m=0;m<=4;m++)for(let n=0;n<=5;n++)for(const f of tuples(m,n)){
  for(let bits=0;bits<(1<<m);bits++){
    const selected=Array.from({length:m},(_,i)=>i).filter(i=>bits>>i&1);
    const r=analyzeFiniteFunction(f,n,selected);
    const image=Array.from({length:n},(_,j)=>j).filter(j=>selected.some(i=>f[i]===j));
    const sat=Array.from({length:m},(_,i)=>i).filter(i=>image.includes(f[i]));
    assert.deepEqual(r.image,image);assert.deepEqual(r.saturation,sat);
    assert.equal(r.injective,!f.some((v,i)=>f.slice(0,i).includes(v)));
    assert.equal(r.surjective,Array.from({length:n},(_,j)=>j).every(j=>f.includes(j)));
    assert.deepEqual(r.missed,Array.from({length:n},(_,j)=>j).filter(j=>!f.includes(j)));
    if(r.collision){assert.notEqual(...r.collision);assert.equal(f[r.collision[0]],f[r.collision[1]]);}
    if(r.inverse!==null){assert.deepEqual(r.inverse,Array.from({length:n},(_,j)=>f.indexOf(j)));}
    subsets++;
  }cases++;
}
for(const args of [[[0],0],[[5],5],[[-1],3],[[1.1],3],[[], -1],[[0],1,[1]]])assert.throws(()=>analyzeFiniteFunction(...args));
const r=analyzeFiniteFunction([0,1,0,1],3,[0]);assert.deepEqual(r.saturation,[0,2]);
const report={finiteFunctionsChecked:cases,selectedSubsetCases:subsets,invalidInputsRejected:true,defaultSaturation:[0,2]};
fs.writeFileSync(require('node:path').join(__dirname,'d_functions-lab-check.json'),JSON.stringify(report,null,2)+'\n');console.log(report);
