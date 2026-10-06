"use strict";
(() => {
  const angle = document.getElementById("vector-angle");
  const length = document.getElementById("vector-length");
  const candidate = document.getElementById("vector-candidate");
  const drawing = document.getElementById("l_vectors-figure-3-vector-drawing");
  const result = document.getElementById("vector-result");
  const fixed = [3, 2];
  const clean = n => Math.abs(n) < 1e-10 ? 0 : n;
  const fmt = n => clean(n).toFixed(3);
  const point = v => [120+v[0]*48, 300-v[1]*48];
  const arrow = (a,b,color,dashed=false) => {
    const [ax,ay]=point(a), [bx,by]=point(b);
    return `<path d="M${ax} ${ay} L${bx} ${by}" fill="none" stroke="${color}" stroke-width="3" ${dashed?'stroke-dasharray="5 4"':''} marker-end="url(#l_vectors-figure-3-lab-arrow)"/>`;
  };
  function update() {
    const degrees=Number(angle.value), size=Number(length.value)/100;
    const t=Number(candidate.value)/100, radians=degrees*Math.PI/180;
    const unit=[Math.cos(radians),Math.sin(radians)];
    const b=unit.map(v=>size*v), valid=size!==0;
    const scalar=valid ? fixed[0]*unit[0]+fixed[1]*unit[1] : null;
    const coefficient=valid ? scalar/size : null;
    const projection=valid ? unit.map(v=>scalar*v) : [0,0];
    const residual=fixed.map((v,i)=>v-projection[i]);
    const trial=b.map(v=>t*v);
    const minimum=residual.reduce((a,v)=>a+v*v,0);
    const actual=fixed.reduce((a,v,i)=>a+(v-trial[i])**2,0);
    const excess=valid ? (t-coefficient)**2*size**2 : 0;
    result.dataset.valid=String(valid);
    result.dataset.minimum=String(minimum);
    result.dataset.actual=String(actual);
    result.dataset.excess=String(excess);
    result.dataset.orthogonality=String(b[0]*residual[0]+b[1]*residual[1]);
    document.getElementById("angle-label").textContent=`${degrees}°`;
    document.getElementById("length-label").textContent=size.toFixed(2);
    document.getElementById("candidate-label").textContent=t.toFixed(2);
    let axes='<path d="M24 300 H536 M120 390 V25" stroke="#d1e0e7" fill="none"/><text x="106" y="322">0</text>';
    if(valid) axes+=arrow(unit.map(v=>-2*v),unit.map(v=>8*v),"#b4c9d5",true);
    drawing.innerHTML=axes+arrow([0,0],fixed,"#286c91")+arrow([0,0],projection,"#487962")+arrow(projection,fixed,"#a0612e")+arrow([0,0],trial,"#805da0",true)+`<circle cx="${point(trial)[0]}" cy="${point(trial)[1]}" r="4" fill="#805da0"/><text x="${point(fixed)[0]+9}" y="${point(fixed)[1]-9}">x = (3, 2)</text>`;
    const line = (name,value) => `<p>${name}: <span class="lab-math">${value}</span></p>`;
    result.innerHTML=(valid
      ? line("Projection coefficient",fmt(coefficient))+line("Signed scalar component",fmt(scalar))
      : '<p><strong>Zero direction.</strong> The span is the zero subspace. Projection is zero; a direction angle and quotient-based coefficient are undefined. Every coefficient gives the same candidate point.</p>')
      +line("Projected vector",`(${projection.map(fmt).join(", ")})`)
      +line("Residual",`(${residual.map(fmt).join(", ")})`)
      +line("Minimum squared distance",fmt(minimum))
      +line("Candidate squared distance",`${fmt(actual)} = ${fmt(minimum)} + ${fmt(excess)}`)
      +line("Residual–direction inner product",fmt(Number(result.dataset.orthogonality)));
  }
  [angle,length,candidate].forEach(control=>control.addEventListener("input",update));
  update();
})();
