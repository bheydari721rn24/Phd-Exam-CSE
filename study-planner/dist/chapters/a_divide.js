(function(){
"use strict";
function join(l,r){return [l[0]+r[0],Math.max(l[1],l[0]+r[1]),Math.max(r[2],r[0]+l[2]),Math.max(l[3],r[3],l[2]+r[1])];}
function summary(a,lo=0,hi=a.length){
 if(hi-lo===1){const v=a[lo];return [v,v,v,v];}
 const m=lo+Math.floor((hi-lo)/2);
 return join(summary(a,lo,m),summary(a,m,hi));
}
function enumerate(a){
 let total=0,prefix=-Infinity,suffix=-Infinity;
 for(let i=0;i<a.length;i++){total+=a[i];prefix=Math.max(prefix,total);}
 let s=0;for(let i=a.length-1;i>=0;i--){s+=a[i];suffix=Math.max(suffix,s);}
 let best=null;
 for(let i=0;i<a.length;i++){
  let value=0;
  for(let j=i;j<a.length;j++){
   value+=a[j];
   if(best===null||value>best.value||(value===best.value&&(i<best.start||(i===best.start&&j+1<best.end))))best={value,start:i,end:j+1};
  }
 }
 return {values:[total,prefix,suffix,best.value],witness:best};
}
function analyze(a,split){
 if(!Array.isArray(a)||a.length<2||a.length>16||a.some(v=>!Number.isInteger(v)||Math.abs(v)>99))throw new Error("Enter two through sixteen integers between −99 and 99.");
 if(!Number.isInteger(split)||split<1||split>=a.length)throw new Error("Choose a split leaving both halves nonempty.");
 const left=summary(a,0,split),right=summary(a,split),combined=join(left,right),whole=summary(a),direct=enumerate(a);
 if(combined.some((v,i)=>v!==whole[i]||v!==direct.values[i]))throw new Error("Independent computations disagree.");
 return {left,right,combined,cross:left[2]+right[1],witness:direct.witness};
}
function parse(value){
 const s=value.trim();
 if(!/^[+-]?\d+(?:(?:\s*,\s*|\s+)[+-]?\d+)*$/.test(s))throw new Error("Use integers separated by commas or spaces; omit empty entries.");
 return s.split(/[\s,]+/).map(Number);
}
if(typeof module!=="undefined")module.exports={join,summary,enumerate,analyze,parse};
if(typeof document==="undefined")return;
const form=document.getElementById("subarray-form"),input=document.getElementById("subarray-input"),split=document.getElementById("subarray-split"),out=document.getElementById("subarray-output");
const presets={crossing:[[4,-6,8,-2,3,-9,5],3],negative:[[-7,-2,-5],1],left:[[8,1,-20,2,1],2],ties:[[2,-2,2],1]};
const math=v=>'<span class="math-inline">'+String(v).replace(/-/g,"−")+'</span>';
function render(){
 input.setCustomValidity("");split.setCustomValidity("");
 try{
  const a=parse(input.value);split.max=String(a.length-1);
  if(!form.checkValidity()){out.dataset.verified="false";out.textContent="Correct the required integer inputs before calculating.";return;}
  const result=analyze(a,Number(split.value));
  out.dataset.best=String(result.combined[3]);out.dataset.start=String(result.witness.start);out.dataset.end=String(result.witness.end);out.dataset.verified="true";
  out.innerHTML='<table><thead><tr><th>Segment</th><th>Total</th><th>Prefix</th><th>Suffix</th><th>Best</th></tr></thead><tbody>'+["left","right","combined"].map(k=>'<tr><th>'+({left:"Left child",right:"Right child",combined:"Parent result"}[k])+'</th>'+result[k].map(v=>'<td>'+math(v)+'</td>').join("")+'</tr>').join("")+'</tbody></table><p>Crossing candidate: '+math(result.left[2])+' + '+math(result.right[1])+' = '+math(result.cross)+'.</p><p>Best interval: '+math('['+result.witness.start+', '+result.witness.end+')')+'; items '+math(a.slice(result.witness.start,result.witness.end).join(", "))+'; sum '+math(result.witness.value)+'.</p><p class="verified">Verified: the joined summary, full recursive summary and independent interval enumeration agree in every component.</p>';
 }catch(e){input.setCustomValidity(e.message);out.dataset.verified="false";out.textContent=e.message;}
}
form.addEventListener("submit",e=>{e.preventDefault();render();form.reportValidity();});
form.addEventListener("change",render);
document.querySelectorAll("[data-preset]").forEach(b=>b.addEventListener("click",()=>{const [a,m]=presets[b.dataset.preset];input.value=a.join(", ");split.value=String(m);render();}));
render();
})();
