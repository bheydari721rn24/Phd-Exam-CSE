/* Original finite recurrence model. BigInt preserves exact polynomial tolls. */
(function () {
  "use strict";
  const limits = {a:[1,6], b:[2,6], q:[0,4], h:[0,8], base:[1,20]};
  function analyze(parameters) {
    for (const [key,[low,high]] of Object.entries(limits)) {
      if (!Number.isInteger(parameters[key]) || parameters[key] < low || parameters[key] > high)
        throw new RangeError("Use integers within the displayed parameter limits.");
    }
    const {a,b,q,h,base} = parameters;
    const A=BigInt(a), B=BigInt(b), Q=BigInt(q), H=BigInt(h);
    const n=B**H, leaves=A**H;
    let bottomUp=BigInt(base);
    for (let r=1;r<=h;r++) bottomUp=A*bottomUp+(B**BigInt(r))**Q;
    const rows=[];
    let levelSum=0n;
    for (let j=0;j<h;j++) {
      const nodes=A**BigInt(j),size=B**BigInt(h-j),toll=size**Q,total=nodes*toll;
      rows.push({depth:j,nodes:String(nodes),size:String(size),toll:String(toll),total:String(total),terminal:false});
      levelSum+=total;
    }
    const terminal=leaves*BigInt(base);
    rows.push({depth:h,nodes:String(leaves),size:"1",toll:String(base),total:String(terminal),terminal:true});
    levelSum+=terminal;
    if (levelSum!==bottomUp) throw new Error("Independent cost computations disagree.");
    const denominator=B**Q;
    const status=A<denominator?"root":A===denominator?"balanced":"leaves";
    return {n:String(n),leaves:String(leaves),total:String(bottomUp),levelTotal:String(levelSum),
      terminal:String(terminal),ratioNumerator:String(A),ratioDenominator:String(denominator),status,rows};
  }
  if (typeof module!=="undefined" && module.exports) module.exports={analyze};
  if (typeof document==="undefined") return;
  const form=document.getElementById("recurrence-form"), output=document.getElementById("recurrence-output");
  if (!form || !output) return;
  const presets={leaves:[4,2,1,4,1],balanced:[2,2,1,4,1],root:[2,2,2,4,1],chain:[1,2,0,6,1],base:[2,2,1,4,5]};
  const keys=["a","b","q","h","base"];
  const math=value=>'<span class="math-inline">'+value+"</span>";
  function render(event) {
    if (event) event.preventDefault();
    if (!form.reportValidity()) return;
    const parameters=Object.fromEntries(keys.map(key=>[key,Number(document.getElementById("recurrence-"+key).value)]));
    try {
      const result=analyze(parameters);
      Object.assign(output.dataset,{total:result.total,levelTotal:result.levelTotal,status:result.status,height:String(parameters.h)});
      const interpretation={root:"Internal level costs decrease geometrically; the polynomial root toll determines the asymptotic order.",balanced:"All internal levels have equal cost. The number of internal levels produces a logarithmic factor.",leaves:"Internal level costs increase geometrically toward the leaves. Positive terminal costs have the critical leaf exponent."}[result.status];
      output.innerHTML='<dl><dt>Input size</dt><dd>'+math(result.n)+'</dd><dt>Bottom-up cost</dt><dd>'+math(result.total)+'</dd><dt>Independent level sum</dt><dd>'+math(result.levelTotal)+'</dd><dt>Terminal leaf contribution</dt><dd>'+math(result.terminal)+'</dd><dt>Internal level ratio</dt><dd>'+math(result.ratioNumerator+" / "+result.ratioDenominator)+'</dd></dl><p>'+interpretation+' This interpretation uses the proven polynomial-toll family; a single finite total is not an asymptotic proof.</p><div class="lab-table-scroll"><table><thead><tr><th>Depth</th><th>Kind</th><th>Node count</th><th>Node size</th><th>Cost per node</th><th>Level cost</th></tr></thead><tbody>'+result.rows.map(row=>'<tr class="'+(row.terminal?"terminal":"internal")+'"><td>'+math(row.depth)+'</td><td>'+(row.terminal?"Terminal":"Internal")+'</td><td>'+math(row.nodes)+'</td><td>'+math(row.size)+'</td><td>'+math(row.toll)+'</td><td>'+math(row.total)+'</td></tr>').join("")+'</tbody></table></div><p>Exact agreement verified. The terminal row uses the base cost rather than the internal toll.</p>';
    } catch (error) {
      output.textContent=error.message;
      for (const key of Object.keys(output.dataset)) delete output.dataset[key];
    }
  }
  form.addEventListener("submit",render);
  form.addEventListener("change",render);
  document.querySelectorAll("[data-preset]").forEach(button=>button.addEventListener("click",()=>{
    presets[button.dataset.preset].forEach((value,index)=>{document.getElementById("recurrence-"+keys[index]).value=value;});
    render();
  }));
  render();
})();
