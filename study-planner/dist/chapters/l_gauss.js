/* Exact rational row-operation laboratory; no numerical rank tolerance. */
(() => {
  document.querySelectorAll('.gauss-diagram').forEach(figure=>{const button=document.createElement('button');button.type='button';button.className='gauss-figure-toggle';button.textContent='Enlarge figure';button.setAttribute('aria-expanded','false');button.addEventListener('click',()=>{const expanded=figure.classList.toggle('expanded');button.textContent=expanded?'Fit complete figure':'Enlarge figure';button.setAttribute('aria-expanded',String(expanded))});figure.prepend(button)});
  const form=document.getElementById('gauss-form'),output=document.getElementById('gauss-output');
  if(!form||!output)return;
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
  const f=(n,d=1n)=>{n=BigInt(n);d=BigInt(d);if(!d)throw Error('A denominator cannot be zero.');if(d<0n){n=-n;d=-d}const g=gcd(n,d);return {n:n/g,d:d/g}};
  const add=(a,b)=>f(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>f(-a.n,a.d),sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>f(a.n*b.n,a.d*b.d),div=(a,b)=>f(a.n*b.d,a.d*b.n);
  const str=a=>a.d===1n?String(a.n):`${a.n}/${a.d}`,zero=a=>a.n===0n;
  const read=s=>{if(!/^[+-]?\d+(?:\/[+-]?\d+)?$/.test(s))throw Error('Use integers or fractions, with no decimal points.');const [n,d='1']=s.split('/');if(BigInt(n)>100000n||BigInt(n)<-100000n||BigInt(d)>100000n||BigInt(d)<-100000n)throw Error('Input numerator and denominator magnitude must not exceed 100,000.');return f(n,d)};
  const math=a=>a.d===1n?`<mn>${a.n<0n?-a.n:a.n}</mn>`:`<mfrac><mn>${a.n<0n?-a.n:a.n}</mn><mn>${a.d}</mn></mfrac>`;
  const atom=a=>`<mrow>${a.n<0n?'<mo>−</mo>':''}${math(a)}</mrow>`;
  const matrixHTML=a=>`<math xmlns="http://www.w3.org/1998/Math/MathML" display="block" aria-label="Exact matrix"><mrow><mo>[</mo><mtable columnspacing=".65em" rowspacing=".35em">${a.map(row=>`<mtr>${row.map(x=>`<mtd>${atom(x)}</mtd>`).join('')}</mtr>`).join('')}</mtable><mo>]</mo></mrow></math>`;
  const vectorHTML=a=>matrixHTML(a.map(x=>[x]));
  let trace=[],position=0,summary='';
  const render=()=>{if(!trace.length)return;const s=trace[position];output.innerHTML=`<p class="lab-phase">Step ${position+1} of ${trace.length}: ${s.op}</p><div class="gauss-matrix" aria-label="Current augmented matrix">${matrixHTML(s.a)}</div><details><summary>Exact row transformation at this step</summary><div class="gauss-matrix">${matrixHTML(s.e)}</div><p>Multiplying this matrix by the original augmented array gives the current array exactly.</p></details>${summary}`;output.dataset.step=String(position);document.querySelector('[data-gauss-step=back]').disabled=position===0;document.querySelector('[data-gauss-step=next]').disabled=position===trace.length-1};
  function compute(){
    try{
      const rows=form.elements.matrix.value.trim().split(/\n+/).map(s=>s.trim().split(/[\s,]+/));
      if(rows.length<1||rows.length>4||rows[0].length<2||rows[0].length>5||rows.some(r=>r.length!==rows[0].length))throw Error('Enter one to four rows of equal length, with one to four coefficient columns and a final load column.');
      let a=rows.map(r=>r.map(read));const original=a.map(r=>r.map(str)),m=a.length,n=a[0].length-1,e=Array.from({length:m},(_,i)=>Array.from({length:m},(_,j)=>f(i===j?1:0))),p=[];trace=[];
      const save=op=>trace.push({op,a:a.map(r=>r.slice()),e:e.map(r=>r.slice())});
      save('Original augmented system');let r=0;
      for(let c=0;c<n&&r<m;c++){
        const j=a.findIndex((row,i)=>i>=r&&!zero(row[c]));
        if(j<0){save(`Skip coefficient column ${c+1}; it has no available pivot`);continue}
        if(j!==r){[a[j],a[r]]=[a[r],a[j]];[e[j],e[r]]=[e[r],e[j]];save(`Swap rows ${j+1} and ${r+1}`)}
        const pivot=a[r][c];if(str(pivot)!=='1'){a[r]=a[r].map(x=>div(x,pivot));e[r]=e[r].map(x=>div(x,pivot));save(`Divide row ${r+1} by ${str(pivot)}`)}p.push(c);
        for(let i=0;i<m;i++)if(i!==r&&!zero(a[i][c])){const v=a[i][c];a[i]=a[i].map((x,j)=>sub(x,mul(v,a[r][j])));e[i]=e[i].map((x,j)=>sub(x,mul(v,e[r][j])));save(`Row ${i+1} minus (${str(v)}) times row ${r+1}`)}r++;
      }
      save('Coefficient RREF and consistency classification');const bad=a.findIndex(row=>row.slice(0,n).every(zero)&&!zero(row[n]));
      const basis=[],x=Array.from({length:n},()=>f(0));
      let state;
      if(bad>=0){state='inconsistent';summary=`<section class="lab-result"><h4>No solution</h4><p>A coefficient-zero row has load ${str(a[bad][n])}. The following original-equation row combination gives zero coefficients and that nonzero load:</p>${matrixHTML([e[bad]])}<p>This proves inconsistency before any free-variable assignment.</p></section>`}
      else{
        for(let i=0;i<p.length;i++)x[p[i]]=a[i][n];
        for(let c=0;c<n;c++)if(!p.includes(c)){const v=Array.from({length:n},()=>f(0));v[c]=f(1);for(let i=0;i<p.length;i++)v[p[i]]=neg(a[i][c]);basis.push(v)}
        state=basis.length?'affine':'unique';summary=`<section class="lab-result"><h4>${basis.length?'Complete affine solution':'Unique solution'}</h4><p>Coefficient pivot columns: ${p.map(c=>c+1).join(', ')||'none'}. Free coordinates: ${basis.length}. A particular solution is:</p>${vectorHTML(x)}${basis.length?'<p>Add any real scalar multiple of each independent homogeneous direction below:</p>'+basis.map(vectorHTML).join(''):''}<p>Substitution checks the particular vector and every homogeneous direction. Assigning all free coordinates recovers every solution.</p></section>`;
      }
      output.dataset.valid='true';output.dataset.state=state;output.dataset.particular=bad>=0?'none':x.map(str).join(',');output.dataset.free=String(basis.length);output.dataset.trace=JSON.stringify(trace.map(s=>({matrix:s.a.map(r=>r.map(str)),transform:s.e.map(r=>r.map(str)),op:s.op})));output.dataset.input=JSON.stringify(original);output.dataset.basis=JSON.stringify(basis.map(v=>v.map(str)));position=0;render();
    }catch(err){trace=[];position=0;output.dataset.valid='false';output.dataset.state='invalid';delete output.dataset.trace;delete output.dataset.input;output.textContent=err.message;document.querySelectorAll('[data-gauss-step]').forEach(b=>b.disabled=true)}
  }
  const presets={unique:'0 2 1 1\n1 -1 1 2\n2 1 -1 0',free:'0 1 2 3\n0 2 4 6\n0 0 1 1',affine:'1 0 2 -1 3\n0 1 -1 4 -1\n0 0 0 0 0',inconsistent:'1 2 -1 1\n2 4 -2 3',fractions:'1/2 1/3 1/6 1\n1 -1 2 0\n3/2 2/3 7/6 2',zero:'0 0 0\n0 0 0'};
  document.querySelectorAll('[data-gauss-preset]').forEach(b=>b.addEventListener('click',()=>{form.elements.matrix.value=presets[b.dataset.gaussPreset];document.querySelectorAll('[data-gauss-step]').forEach(b=>b.disabled=false);compute()}));
  document.querySelectorAll('[data-gauss-step]').forEach(b=>b.addEventListener('click',()=>{position=b.dataset.gaussStep==='next'?Math.min(position+1,trace.length-1):b.dataset.gaussStep==='back'?Math.max(position-1,0):0;render()}));
  form.addEventListener('submit',e=>{e.preventDefault();compute()});form.addEventListener('input',compute);compute();
})();
