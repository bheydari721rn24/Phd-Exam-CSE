"use strict";
(() => {
 const ids=["angle","shear","x","y"];
 const controls=Object.fromEntries(ids.map(id=>[id,document.getElementById(`matrix-${id}`)]));
 const svg=document.getElementById("matrix-canvas"),result=document.getElementById("matrix-result");
 if(!svg||!result)return;
 const mul=(a,b)=>[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]];
 const mv=(a,v)=>[a[0][0]*v[0]+a[0][1]*v[1],a[1][0]*v[0]+a[1][1]*v[1]];
 const fmt=n=>(Math.abs(n)<1e-10?0:n).toFixed(3).replace(/\.?0+$/,"");
 const mathMatrix=a=>`<math class="lab-math"><mrow><mo>[</mo><mtable>${a.map(row=>`<mtr>${row.map(v=>`<mtd><mn>${fmt(v)}</mn></mtd>`).join("")}</mtr>`).join("")}</mtable><mo>]</mo></mrow></math>`;
 function update(){
  const theta=Number(controls.angle.value)*Math.PI/180,s=Number(controls.shear.value)/100;
  const x=[Number(controls.x.value)/100,Number(controls.y.value)/100];
  const R=[[Math.cos(theta),-Math.sin(theta)],[Math.sin(theta),Math.cos(theta)]],S=[[1,s],[0,1]];
  const RS=mul(R,S),SR=mul(S,R),a=mv(RS,x),b=mv(SR,x);
  const comm=RS.map((row,i)=>row.map((v,j)=>v-SR[i][j]));
  const gap=(a[0]-b[0])**2+(a[1]-b[1])**2;
  const commute=comm.every(row=>row.every(v=>Math.abs(v)<1e-10));
  for(const id of ids)document.getElementById(`matrix-${id}-value`).textContent=id==="angle"?`${controls.angle.value}°`:fmt(Number(controls[id].value)/100);
  const corners=[[0,0],[1,0],[1,1],[0,1]];
  const polys=[corners,corners.map(v=>mv(RS,v)),corners.map(v=>mv(SR,v))];
  const extent=Math.max(2,...[...polys.flat(),x,a,b].flat().map(Math.abs))*1.2;
  const scale=260/extent,point=v=>[320+scale*v[0],320-scale*v[1]];
  const pstr=v=>point(v).join(",");
  let drawing="";
  const step=extent>4?2:1;
  for(let k=-Math.floor(extent/step);k<=Math.floor(extent/step);k++){
   const coordinate=k*step,px=point([coordinate,0])[0],py=point([0,coordinate])[1];
   drawing+=`<path d="M${px}35V605M35 ${py}H605" stroke="#e5edf2"/>`;
   if(k!==0)drawing+=`<text x="${px}" y="341" text-anchor="middle">${coordinate}</text><text x="299" y="${py+6}" text-anchor="end">${coordinate}</text>`;
  }
  drawing+='<path d="M35 320H605M320 35V605" stroke="#768a98" stroke-width="1.7"/><text x="600" y="345">x</text><text x="336" y="45">y</text>';
  const colors=["#899da9","#286c91","#ba7a2d"];
  polys.forEach((poly,i)=>drawing+=`<polygon points="${poly.map(pstr).join(" ")}" fill="${colors[i]}" fill-opacity="${i?'.1':'0'}" stroke="${colors[i]}" stroke-width="${i?3:2}" ${i?'':'stroke-dasharray="6 5"'}/>`);
  [x,a,b].forEach((v,i)=>{const p=point(v);drawing+=`<path d="M320 320L${p[0]} ${p[1]}" stroke="${colors[i]}" stroke-width="3"/><circle cx="${p[0]}" cy="${p[1]}" r="6" fill="${colors[i]}"/>`;});
  svg.innerHTML=drawing;
  result.dataset.commute=String(commute);result.dataset.gap=String(gap);
  result.dataset.rs=JSON.stringify(RS);result.dataset.sr=JSON.stringify(SR);result.dataset.first=JSON.stringify(a);result.dataset.second=JSON.stringify(b);result.dataset.scale=String(scale);
  result.innerHTML=`<p>Grey: input and original square. <span class="lab-blue">Blue: shear first, then rotation.</span> <span class="lab-amber">Amber: rotation first, then shear.</span></p>
   <div class="lab-comparison"><div><p class="lab-blue">Rotation after shear: <span class="lab-math">RS</span></p>${mathMatrix(RS)}<p>Output: <span class="lab-math">(${a.map(fmt).join(", ")})</span></p></div><div><p class="lab-amber">Shear after rotation: <span class="lab-math">SR</span></p>${mathMatrix(SR)}<p>Output: <span class="lab-math">(${b.map(fmt).join(", ")})</span></p></div></div>
   <p>Commutator <span class="lab-math">RS−SR</span>: ${mathMatrix(comm)}</p><p>Squared distance between the two outputs: <span class="lab-math">${fmt(gap)}</span>.</p><p>${commute?"The two matrices commute at this parameter setting.":gap<1e-10?"The matrices differ, but agree on this particular input.":"The matrices differ and produce different outputs on this input."}</p>`;
 }
 ids.forEach(id=>controls[id].addEventListener("input",update));update();
})();
