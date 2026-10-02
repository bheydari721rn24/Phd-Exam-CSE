const assert=require('node:assert/strict');
const lab=require('../dist/chapters/g_boolean-lab.js');let checks=0;
function check(c){assert(c);checks++;}
function expression(mask,n){const vars=['x','y','z'].slice(0,n),terms=[];for(let i=0;i<(1<<n);i++)if(mask>>i&1)terms.push('('+vars.map((v,j)=>(i>>(n-1-j)&1)?v:'!'+v).join('&')+')');return terms.join('|')||'0';}
for(let m=0;m<256;m++){
 const expr=expression(m,3);
 for(const variable of ['x','y','z']){
  const r=lab.analyze(expr,'!('+expr+')',variable);check(!r.equivalent);
  for(let i=0;i<8;i++){check(r.rows[i].a===(m>>i&1));check(r.rows[i].b===1-(m>>i&1));check(r.rows[i].mismatch===1);}
  const index=['x','y','z'].indexOf(variable),stride=1<<(2-index),zeroIndices=[...Array(8).keys()].filter(i=>!(i&stride));
  let positive=true,negative=true;
  for(let j=0;j<4;j++){
   const zero=m>>zeroIndices[j]&1,one=m>>(zeroIndices[j]|stride)&1,c=r.cofactors[j];
   check(c.zero===zero&&c.one===one);check(c.difference===(zero!==one?1:0));check(c.universal===Math.min(zero,one));check(c.existential===Math.max(zero,one));positive&&=zero<=one;negative&&=one<=zero;
  }
  check(r.positive===positive&&r.negative===negative&&r.independent===(positive&&negative));
 }
}
for(let m=0;m<16;m++)for(let n=0;n<16;n++){
 const r=lab.analyze(expression(m,2),expression(n,2),'z');check(r.equivalent===(m===n));
 const first=[...Array(4).keys()].find(i=>(m>>i&1)!==(n>>i&1));check(first===undefined?r.counterexample===null:r.counterexample.join('')===(first.toString(2).padStart(2,'0')+'0'));
}
for(const bad of ['', 'xy','x&&y','x||y','x+', 'x &','x(', '(x','x)','2','a','window','x;','!','x y', 'x'.repeat(301)]){assert.throws(()=>lab.parse(bad));checks++;}
assert.throws(()=>lab.analyze('x','x','a'));checks++;
for(let x=0;x<2;x++)for(let y=0;y<2;y++)for(let z=0;z<2;z++){check(lab.evaluate(lab.parse('x | y ^ z & !x'),{x,y,z})===(x|(y^(z&(1-x)))));}
console.log(JSON.stringify({assertions:checks,allThreeInputFunctions:256,allTwoInputComparisons:256,rejectedSyntax:17}));
