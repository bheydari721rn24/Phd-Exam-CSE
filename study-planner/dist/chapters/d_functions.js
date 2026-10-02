"use strict";
function analyzeFiniteFunction(values, targetSize, selected = []) {
  if (!Number.isInteger(targetSize) || targetSize < 0 || !Array.isArray(values)) throw new Error("Invalid function type.");
  const fibers = Array.from({length:targetSize}, () => []);
  values.forEach((target, input) => {
    if (!Number.isInteger(target) || target < 0 || target >= targetSize) throw new Error("An output is outside the codomain.");
    fibers[target].push(input);
  });
  if (!Array.isArray(selected) || selected.some(x => !Number.isInteger(x) || x < 0 || x >= values.length)) throw new Error("Invalid selected subset.");
  const image = [...new Set(selected.map(x => values[x]))].sort((a,b)=>a-b);
  const saturation = values.map((v,i)=>image.includes(v)?i:null).filter(x=>x!==null);
  const injective = fibers.every(f=>f.length<=1), surjective= fibers.every(f=>f.length>=1);
  const missed = fibers.map((f,i)=>f.length===0?i:null).filter(x=>x!==null);
  const collision = fibers.find(f=>f.length>1)?.slice(0,2) || null;
  return {fibers,injective,surjective,missed,collision,image,saturation,inverse:injective&&surjective?fibers.map(f=>f[0]):null};
}
if (typeof module !== "undefined" && module.exports) module.exports={analyzeFiniteFunction};
if (typeof document !== "undefined") {
  let values=[0,1,0,1], targetSize=3, selected=new Set([0]);
  const setText=a=>"{"+a.join(", ")+"}";
  const targetText=a=>setText(a.map(x=>"b"+x));
  const math=s=>'<span class="math-inline">'+s.replace(/b(\d+)/g,'b<sub>$1</sub>')+'</span>';
  function render() {
    document.getElementById("target-size").value=String(targetSize);
    document.getElementById("function-input").innerHTML='<table><thead><tr><th>Input</th><th>Output</th><th>In subset S</th></tr></thead><tbody>'+values.map((v,i)=>'<tr><td>'+math(String(i))+'</td><td><select class="output-choice" data-input="'+i+'" aria-label="Output for input '+i+'">'+Array.from({length:targetSize},(_,j)=>'<option value="'+j+'"'+(j===v?' selected':'')+'>b'+j+'</option>').join('')+'</select></td><td><input type="checkbox" data-select="'+i+'" aria-label="Include input '+i+' in S"'+(selected.has(i)?' checked':'')+'></td></tr>').join('')+'</tbody></table>';
    const r=analyzeFiniteFunction(values,targetSize,[...selected]);
    const inv=r.inverse===null?'No true inverse exists.':math('f<sup>−1</sup> = '+setText(r.inverse.map((v,i)=>'(b'+i+', '+v+')')));
    document.getElementById("function-output").innerHTML='<p><strong>'+ (r.injective&&r.surjective?'Bijective':r.injective?'Injective; not onto':r.surjective?'Onto; not injective':'Neither injective nor onto')+'</strong></p><table><thead><tr><th>Target</th><th>Fiber of inputs</th></tr></thead><tbody>'+r.fibers.map((f,i)=>'<tr'+(r.image.includes(i)?' class="selected-fiber"':'')+'><td>'+math('b'+i)+'</td><td>'+math(setText(f))+'</td></tr>').join('')+'</tbody></table><dl><dt>Collision witness</dt><dd>'+(r.collision?math(setText(r.collision))+' have the same output.':'No two distinct inputs collide.')+'</dd><dt>Missed targets</dt><dd>'+math(targetText(r.missed))+'</dd><dt>Selected subset</dt><dd>'+math('S = '+setText([...selected].sort((a,b)=>a-b)))+'</dd><dt>Direct image</dt><dd>'+math('f[S] = '+targetText(r.image))+'</dd><dt>Saturation</dt><dd>'+math('f<sup>−1</sup>[f[S]] = '+setText(r.saturation))+'</dd><dt>True inverse</dt><dd>'+inv+'</dd></dl>';
    document.querySelectorAll('[data-input]').forEach(x=>x.addEventListener('change',()=>{values[Number(x.dataset.input)]=Number(x.value);render();}));
    document.querySelectorAll('[data-select]').forEach(x=>x.addEventListener('change',()=>{const i=Number(x.dataset.select);x.checked?selected.add(i):selected.delete(i);render();}));
  }
  document.getElementById('target-size').addEventListener('change',e=>{targetSize=Number(e.target.value);values=values.map(x=>Math.min(x,targetSize-1));render();});
  for (const [name,n,v] of [['bijection',4,[0,1,2,3]],['onto',3,[0,1,2,0]],['injection',5,[0,1,2,3]]]) document.getElementById('preset-'+name).addEventListener('click',()=>{targetSize=n;values=v.slice();selected=new Set([0]);render();});
  render();
}
