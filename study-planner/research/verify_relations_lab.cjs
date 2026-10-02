"use strict";
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'..');
const source=fs.readFileSync(path.join(root,'dist/chapters/d_relations.js'),'utf8');
const prefix=source.slice(0,source.indexOf('let input,stage'))+'})();';
const ctx={window:{}};vm.createContext(ctx);vm.runInContext(prefix,ctx);
const {closure,equivalence,properties}=ctx.window.relationModel;
const n=4;
function graphSearch(m,identity=false){
 return m.map((_,start)=>{const seen=new Set(identity?[start]:[]),todo=[];
  for(let v=0;v<n;v++)if(m[start][v]){seen.add(v);todo.push(v);}
  while(todo.length){const u=todo.pop();for(let v=0;v<n;v++)if(m[u][v]&&!seen.has(v)){seen.add(v);todo.push(v);}}
  return Array.from({length:n},(_,v)=>seen.has(v));
 });
}
const plain=x=>JSON.parse(JSON.stringify(x));
for(let bits=0;bits<65536;bits++){
 const m=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>Boolean(bits&(1<<(n*i+j)))));
 const plus=graphSearch(m),star=graphSearch(m,true),undirected=m.map((r,i)=>r.map((v,j)=>v||m[j][i]));
 assert.deepStrictEqual(plain(closure(m)),plus);
 assert.deepStrictEqual(plain(closure(m,true)),star);
 assert.deepStrictEqual(plain(equivalence(m)),graphSearch(undirected,true));
 const pairs=[];for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(m[i][j])pairs.push([i,j]);
 const has=(i,j)=>m[i][j];
 const expected=[Array.from({length:n},(_,i)=>has(i,i)).every(Boolean),!pairs.some(([i,j])=>i===j),pairs.every(([i,j])=>has(j,i)),pairs.every(([i,j])=>i===j||!has(j,i)),pairs.every(([i,j])=>!has(j,i)),pairs.every(([i,j])=>pairs.filter(([a])=>a===j).every(([,k])=>has(i,k))),Array.from({length:n},(_,i)=>pairs.some(([a])=>a===i)).every(Boolean)];
 const actual=plain(properties(m));assert.deepStrictEqual(actual.map(p=>p.holds),expected);
 for(const p of actual.filter(p=>!p.holds)){
  const w=p.witness;
  if(p.label==='Transitive')assert(has(w[0],w[1])&&has(w[1],w[2])&&!has(w[0],w[2]));
  if(p.label==='Antisymmetric')assert(w[0]!==w[1]&&has(w[0],w[1])&&has(w[1],w[0]));
  if(p.label==='Asymmetric')assert(has(w[0],w[1])&&has(w[1],w[0]));
  if(p.label==='Symmetric')assert(has(w[0],w[1])&&!has(w[1],w[0]));
  if(p.label==='Reflexive')assert(!has(w,w));
  if(p.label==='Irreflexive')assert(has(w,w));
  if(p.label==='Serial')assert(!pairs.some(([i])=>i===w));
 }
}
const result={relations:65536,carrierSize:4,checks:['positive closure vs independent graph search','zero-length closure vs graph search','equivalence closure vs undirected components','seven properties vs pair-set definitions','every emitted failure witness validated']};
fs.writeFileSync(path.join(root,'research/d_relations-lab-check.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify(result));
