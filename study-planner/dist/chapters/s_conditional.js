"use strict";
(() => {
  const form=document.getElementById("table-form"),out=document.getElementById("table-output");
  if(!form||!out)return;
  const keys=["both","aonly","bonly","neither"];
  const gcd=(a,b)=>{while(b){[a,b]=[b,a%b];}return a;};
  const ratio=(a,b)=>{if(!b)return "undefined";const d=gcd(a,b);return b/d===1?String(a/d):`${a/d}/${b/d}`;};
  function calculate(){
    const v=keys.map(k=>Number(form.elements[k].value));
    if(!form.checkValidity()||v.some(x=>!Number.isInteger(x)||x<0||x>100000)||v.reduce((a,b)=>a+b,0)===0){out.replaceChildren();const p=document.createElement("p");p.className="error";p.textContent="Enter four nonnegative integer weights with a positive total. Each weight must be at most 100,000.";out.append(p);out.dataset.valid="false";return;}
    const [x,a,b,z]=v,total=x+a+b+z;
    const values={a:ratio(x+a,total),b:ratio(x+b,total),joint:ratio(x,total),forward:ratio(x,x+b),reverse:ratio(x,x+a),independent:String(x*z===a*b)};
    Object.assign(out.dataset,{valid:"true",...values});out.replaceChildren();
    const dl=document.createElement("dl");
    for(const [label,value] of [["Probability of A",values.a],["Probability of B",values.b],["Probability of both events",values.joint],["Probability of A given B",values.forward],["Probability of B given A",values.reverse],["Exact independence test",values.independent==="true"?"independent":"dependent"]]){
      const dt=document.createElement("dt"),dd=document.createElement("dd");dt.textContent=label;dd.textContent=value;if(label!=="Exact independence test"&&value!=="undefined")dd.className="math-inline";dl.append(dt,dd);
    }
    out.append(dl);const p=document.createElement("p");p.textContent=(!x&&!b)?"B has zero mass, so conditioning on B is undefined. The product definition of independence still applies.":values.independent==="true"?"The intersection mass equals the product of the marginal masses. This equality uses exact integer weights.":"The intersection mass differs from the product of the marginal masses. Equal or similar individual rates would not change this result.";out.append(p);
  }
  form.addEventListener("submit",e=>{e.preventDefault();calculate();});
  form.addEventListener("input",calculate);
  const presets={independent:[1,2,3,6],associated:[3,1,1,5],disjoint:[0,2,3,5],zero:[0,3,0,5]};
  document.querySelectorAll("[data-table-preset]").forEach(button=>button.addEventListener("click",()=>{presets[button.dataset.tablePreset].forEach((x,i)=>form.elements[keys[i]].value=x);calculate();}));
  calculate();
})();
