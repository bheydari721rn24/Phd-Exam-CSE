"use strict";
(() => {
  const form=document.getElementById("bayes-form"),out=document.getElementById("bayes-output");
  if(!form||!out)return;
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const F=(a,b=1n)=>{const d=gcd(a,b);return [a/d,b/d];};
  const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
  const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const pow=(a,n)=>F(a[0]**BigInt(n),a[1]**BigInt(n));
  const show=a=>a[1]===1n?String(a[0]):`${a[0]}/${a[1]}`;
  function parse(s){
    if(!/^\s*\d+(?:\s*\/\s*\d+)?\s*$/.test(s))throw Error("Use an integer or an integer fraction.");
    const parts=s.trim().split("/").map(x=>BigInt(x.trim())),a=parts[0],b=parts[1]??1n;
    if(b===0n||a>b||a>100000n||b>100000n)throw Error("Each probability must lie between zero and one, with a positive denominator and entries at most 100,000.");
    return F(a,b);
  }
  const math=value=>{const ns="http://www.w3.org/1998/Math/MathML",m=document.createElementNS(ns,"math");m.setAttribute("aria-label",show(value));
    const number=n=>{const x=document.createElementNS(ns,"mn");x.textContent=String(n);return x;};
    if(value[1]===1n)m.append(number(value[0]));else{const f=document.createElementNS(ns,"mfrac");f.append(number(value[0]),number(value[1]));m.append(f);}return m;};
  function calculate(){
    out.replaceChildren();out.dataset.valid="false";out.dataset.posterior="undefined";out.dataset.evidence="undefined";
    try{
      const p=parse(form.elements.prior.value),a=parse(form.elements.target.value),b=parse(form.elements.background.value);
      const n=Number(form.elements.reports.value),mode=form.elements.mode.value;
      if(!form.checkValidity()||!Number.isInteger(n)||n<0||n>20||!["independent","duplicate"].includes(mode))throw Error("Use an integer report count from zero to twenty and choose a report model.");
      const effective=mode==="duplicate"&&n>0?1:n;
      const w1=mul(p,pow(a,effective)),w0=mul(F(p[1]-p[0],p[1]),pow(b,effective)),z=add(w1,w0);
      out.dataset.evidence=show(z);
      if(z[0]===0n)throw Error("The specified report has zero probability in this model. Its posterior is undefined; choose a compatible observation or revise the model.");
      const r=F(w1[0]*z[1],w1[1]*z[0]);
      Object.assign(out.dataset,{valid:"true",posterior:show(r),evidence:show(z),effective:String(effective)});
      const dl=document.createElement("dl");
      for(const [label,value] of [["Target joint evidence mass",w1],["Background joint evidence mass",w0],["Total evidence probability",z],["Posterior target probability",r],["Posterior background probability",F(r[1]-r[0],r[1])]]){
        const dt=document.createElement("dt"),dd=document.createElement("dd");dt.textContent=label;dd.append(math(value));dl.append(dt,dd);
      }
      out.append(dl);const info=document.createElement("p");info.textContent=n===0?"No report was observed, so evidence probability is one and the posterior equals the prior.":mode==="duplicate"?"All displayed reports copy the first measurement. Later copies add no evidence; one likelihood factor is used.":`${n} reports are independent conditional on the same fixed class. The class likelihoods are raised to this report count.`;out.append(info);
    }catch(error){const message=document.createElement("p");message.className="error";message.textContent=error.message;out.append(message);}
  }
  const presets={default:["1/100","9/10","1/20",1,"independent"],negative:["1/100","1/10","19/20",1,"independent"],independent:["1/10","4/5","1/5",2,"independent"],duplicate:["1/10","4/5","1/5",2,"duplicate"],impossible:["1/2","0","0",1,"independent"]};
  document.querySelectorAll("[data-bayes-preset]").forEach(button=>button.addEventListener("click",()=>{["prior","target","background","reports","mode"].forEach((key,i)=>form.elements[key].value=presets[button.dataset.bayesPreset][i]);calculate();}));
  form.addEventListener("submit",event=>{event.preventDefault();calculate();});form.addEventListener("input",calculate);form.addEventListener("change",calculate);calculate();
})();
