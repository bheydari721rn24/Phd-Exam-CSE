const fs=require('fs'),vm=require('vm'),path=require('path');
const context={window:{},document:{getElementById:()=>null}};
vm.createContext(context);vm.runInContext(fs.readFileSync(path.join(__dirname,'../dist/chapters/g_number-lab.js'),'utf8'),context);
const model=context.window.numberWordModel;
let cases=0;
const assert=(ok)=>{if(!ok)throw Error('Independent laboratory arithmetic mismatch');};
for(let n=2;n<=8;n++){
 const M=1<<n,top=M/2,signed=u=>u>=top?u-M:u;
 for(let a=0;a<M;a++)for(let b=0;b<M;b++)for(const op of ['add','sub']){
  const r=model(n,BigInt(a),BigInt(b),op),exact=op==='add'?a+b:a-b,sExact=op==='add'?signed(a)+signed(b):signed(a)-signed(b);
  const retained=((exact%M)+M)%M;
  assert(Number(r.word)===retained && Number(r.signedResult)===signed(retained));
  assert(r.overflow===String(sExact< -top || sExact>=top));
  assert(Number(r.carry)===(op==='add'?Number(exact>=M):Number(a>=b)));
  assert(r.gray===(a^(a>>1)).toString(2).padStart(n,'0'));cases++;
 }
}
for(const [n,a,b,op] of [[16,65535n,1n,'add'],[16,32767n,1n,'add'],[16,0n,32768n,'sub'],[16,32768n,65535n,'sub']]){const r=model(n,a,b,op);assert(r.trace.length===16);cases++;}
console.log(JSON.stringify({laboratoryCases:cases,exhaustiveWidths:[2,3,4,5,6,7,8],additionalWidth16Cases:4}));
