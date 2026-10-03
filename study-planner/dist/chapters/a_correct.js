"use strict";
(() => {
  const form=document.getElementById("search-form"), out=document.getElementById("search-output");
  const input=document.getElementById("search-array"), target=document.getElementById("search-target"), mode=document.getElementById("search-mode");
  function fail(message){out.dataset.valid="false";out.dataset.status="invalid";out.textContent=message;input.setCustomValidity(message);}
  function run(){
    input.setCustomValidity("");out.dataset.valid="false";
    const raw=input.value.trim();
    if(raw && !/^-?\d+(?:(?:\s*,\s*|\s+)-?\d+)*$/.test(raw)){fail("Separate integer entries with commas or spaces; do not leave missing entries.");return;}
    const a=raw?raw.split(/\s*,\s*|\s+/).map(Number):[], t=Number(target.value);
    if(a.length>24 || a.some(x=>!Number.isInteger(x)||Math.abs(x)>999)){fail("Use at most 24 integers, each between negative 999 and 999.");return;}
    if(a.some((x,i)=>i>0&&a[i-1]>x)){fail("The lower-bound proof requires a sorted, nondecreasing array.");return;}
    if(target.value===""||!Number.isInteger(t)||Math.abs(t)>999){out.dataset.status="invalid";out.textContent="Use an integer target between negative 999 and 999.";return;}
    let lo=0,hi=a.length,stalled=false;const rows=[];
    function invariant(){return 0<=lo&&lo<=hi&&hi<=a.length&&a.slice(0,lo).every(x=>x<t)&&a.slice(hi).every(x=>x>=t);}
    while(lo<hi){
      const mid=lo+Math.floor((hi-lo)/2), oldLo=lo,oldHi=hi;
      rows.push({lo,hi,mid,value:a[mid],width:hi-lo,ok:invariant()});
      if(a[mid]<t)lo=mode.value==="faulty"?mid:mid+1;else hi=mid;
      if(lo===oldLo&&hi===oldHi){stalled=true;break;}
      if(rows.length>32)throw Error("Unexpected bounded demonstration length");
    }
    rows.push({lo,hi,mid:null,value:null,width:hi-lo,ok:invariant()});
    const expected=a.findIndex(x=>x>=t),answer=expected<0?a.length:expected;
    out.replaceChildren();const p=document.createElement("p");
    p.className=stalled?"counterexample":"certificate-ok";
    p.textContent=stalled?"Counterexample: the nonempty interval repeats. Classification is preserved, but strict progress fails.":`Terminated at index ${lo}. Independent linear scan returns ${answer}. Both classifications hold and the unresolved region is empty.`;
    out.append(p);const regions=document.createElement("p");regions.textContent=`Below-target region: [${a.slice(0,lo).join(", ")}]. Unresolved region: [${a.slice(lo,hi).join(", ")}]. At-least-target region: [${a.slice(hi).join(", ")}].`;out.append(regions);
    const table=document.createElement("table"),head=document.createElement("thead"),tr=document.createElement("tr");
    ["Checkpoint","Lower","Upper","Midpoint","Value","Width","Invariant"].forEach(s=>{const th=document.createElement("th");th.textContent=s;tr.append(th);});head.append(tr);table.append(head);
    const body=document.createElement("tbody");rows.forEach((r,i)=>{const row=document.createElement("tr");[i,r.lo,r.hi,r.mid??"—",r.value??"—",r.width,r.ok?"Holds":"Fails"].forEach(x=>{const td=document.createElement("td");td.textContent=x;row.append(td);});body.append(row);});table.append(body);out.append(table);
    out.dataset.valid="true";out.dataset.status=stalled?"stalled":"terminated";out.dataset.result=String(lo);out.dataset.expected=String(answer);out.dataset.invariant=String(rows.every(x=>x.ok));out.dataset.steps=String(rows.length-1);
  }
  form.addEventListener("submit",event=>{event.preventDefault();run();});
  [input,target,mode].forEach(el=>el.addEventListener("change",run));
  document.querySelectorAll("[data-search-preset]").forEach(button=>button.addEventListener("click",()=>{
    const p=button.dataset.searchPreset;input.value=p==="empty"?"":p==="stall"?"2":"1,3,3,3,8,9";target.value="3";mode.value=p==="stall"?"faulty":"correct";run();
  }));run();
})();
