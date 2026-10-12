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
  let camera={scale:48,ox:120,oy:300};
  const point = v => [camera.ox+v[0]*camera.scale,camera.oy-v[1]*camera.scale];
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
    const pts=[[0,0],fixed,projection,trial,b],xs=pts.map(p=>p[0]),ys=pts.map(p=>p[1]);
    const loX=Math.min(-1,...xs),hiX=Math.max(4,...xs),loY=Math.min(-1,...ys),hiY=Math.max(3,...ys);
    camera.scale=Math.min(430/(hiX-loX),280/(hiY-loY));
    camera.ox=55-loX*camera.scale;camera.oy=350+loY*camera.scale;
    const origin=point([0,0]);
    let axes=`<path d="M30 ${origin[1]}H525M${origin[0]} 370V25" stroke="#d1e0e7" fill="none"/><text x="${origin[0]-14}" y="${origin[1]+22}">0</text>`;
    if(valid){
      const bounds=[(30-camera.ox)/camera.scale,(525-camera.ox)/camera.scale,(camera.oy-370)/camera.scale,(camera.oy-25)/camera.scale],cuts=[];
      if(Math.abs(unit[0])>1e-12)for(const x of bounds.slice(0,2)){const k=x/unit[0],y=k*unit[1];if(y>=bounds[2]-1e-9&&y<=bounds[3]+1e-9)cuts.push(k);}
      if(Math.abs(unit[1])>1e-12)for(const y of bounds.slice(2)){const k=y/unit[1],x=k*unit[0];if(x>=bounds[0]-1e-9&&x<=bounds[1]+1e-9)cuts.push(k);}
      if(cuts.length>=2){const a=point(unit.map(v=>v*Math.min(...cuts))),z=point(unit.map(v=>v*Math.max(...cuts)));axes+=`<path d="M${a}L${z}" fill="none" stroke="#b4c9d5" stroke-dasharray="5 4"/>`;}
    }
    const target=point(fixed),trialPoint=point(trial);
    drawing.innerHTML=axes+arrow([0,0],fixed,"#286c91")+arrow([0,0],projection,"#487962")+arrow(projection,fixed,"#a0612e")+arrow([0,0],trial,"#805da0",true)+`<circle data-candidate-point cx="${trialPoint[0]}" cy="${trialPoint[1]}" r="4" fill="#805da0"/><text x="${Math.min(410,target[0]+9)}" y="${Math.max(25,target[1]-12)}">x = (3, 2)</text><text x="280" y="407" text-anchor="middle" font-size="13">Equal axis scale · 1 unit = ${camera.scale.toFixed(1)} diagram pixels</text>`;
    result.dataset.candidateVisible=String(trialPoint[0]>=30&&trialPoint[0]<=525&&trialPoint[1]>=25&&trialPoint[1]<=370);
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
