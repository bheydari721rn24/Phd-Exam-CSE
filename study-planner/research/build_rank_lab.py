from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
t=(ROOT/'dist/chapters/l_gauss.js').read_text()
start=t.index('  const gcd=');end=t.index('  let trace=')
helpers=t[start:end]
prefix="""/* Exact four-space laboratory with rational arithmetic. */
(() => {
document.querySelectorAll('.rank-diagram').forEach(figure=>{const button=document.createElement('button');button.type='button';button.className='rank-figure-toggle';button.textContent='Enlarge figure';button.setAttribute('aria-expanded','false');button.addEventListener('click',()=>{const expanded=figure.classList.toggle('expanded');button.textContent=expanded?'Fit complete figure':'Enlarge figure';button.setAttribute('aria-expanded',String(expanded))});figure.prepend(button)});
const form=document.getElementById('rank-form'),output=document.getElementById('rank-output');if(!form||!output)return;
"""
rest=r'''
const clone=a=>a.map(r=>r.slice());
const transpose=a=>a[0].map((_,j)=>a.map(r=>r[j]));
function reduction(input){
 const a=clone(input),m=a.length,n=a[0].length,p=[],trace=[{op:'Original coefficient matrix',a:clone(a)}];let r=0;
 const save=op=>trace.push({op,a:clone(a)});
 for(let c=0;c<n&&r<m;c++){
  let k=a.findIndex((row,i)=>i>=r&&!zero(row[c]));if(k<0)continue;
  if(k!==r){[a[k],a[r]]=[a[r],a[k]];save('Exchange rows '+(k+1)+' and '+(r+1))}
  const pivot=a[r][c];if(str(pivot)!=='1'){a[r]=a[r].map(v=>div(v,pivot));save('Divide row '+(r+1)+' by '+str(pivot))}
  p.push(c);
  for(let i=0;i<m;i++)if(i!==r&&!zero(a[i][c])){const q=a[i][c];a[i]=a[i].map((v,j)=>sub(v,mul(q,a[r][j])));save('Clear row '+(i+1)+' using pivot row '+(r+1))}
  r++;
 }
 const basis=[];
 for(let j=0;j<n;j++)if(!p.includes(j)){const v=Array.from({length:n},()=>f(0));v[j]=f(1);p.forEach((c,i)=>v[c]=neg(a[i][j]));basis.push(v)}
 save('Reduced row echelon form');
 return {a,p,basis,trace};
}
const encode=a=>a.map(r=>r.map(str));
let trace=[],position=0,summary='';
const list=(basis,ambient)=>basis.length?basis.map(vectorHTML).join(''):'<p>The empty list is the basis of the zero subspace in '+ambient+' coordinates.</p>';
function show(){
 const step=trace[position];output.innerHTML='<p class="lab-phase">Operation '+(position+1)+' of '+trace.length+': '+step.op+'</p><div class="rank-matrix">'+matrixHTML(step.a)+'</div>'+summary;
 output.dataset.step=String(position);
 document.querySelector('[data-rank-step=back]').disabled=position===0;
 document.querySelector('[data-rank-step=next]').disabled=position===trace.length-1;
}
function compute(){
 try{
  const raw=form.elements.matrix.value.trim();if(!raw)throw Error('Enter at least one coefficient row.');
  const rows=raw.split(/\n+/).map(r=>r.trim().split(/[\s,]+/));
  if(rows.length>5||rows[0].length>5||rows.some(r=>r.length!==rows[0].length))throw Error('Use one to five rows and one to five columns, with equal row lengths.');
  const a=rows.map(r=>r.map(read)),m=a.length,n=a[0].length,red=reduction(a),left=reduction(transpose(a));
  const cols=red.p.map(j=>a.map(row=>row[j])),rb=red.a.slice(0,red.p.length);
  const dot=(row,v)=>row.reduce((s,x,i)=>add(s,mul(x,v[i])),f(0));
  if(red.p.length!==left.p.length||red.basis.some(v=>a.some(row=>!zero(dot(row,v))))||left.basis.some(v=>transpose(a).some(row=>!zero(dot(row,v)))))throw Error('An internal exact certificate failed.');
  const r=red.p.length;
  summary='<section class="lab-result"><h4>Rank '+r+'; input dimension '+n+'; output dimension '+m+'</h4><p>Original pivot columns: '+(red.p.map(x=>x+1).join(', ')||'none')+'. Nullity '+(n-r)+'; left nullity '+(m-r)+'.</p><h4>Column-space basis: '+m+' output coordinates</h4>'+list(cols,m)+'<h4>Row-space basis: '+n+' input coordinates</h4>'+list(rb,n)+'<h4>Kernel basis: '+n+' input coordinates</h4>'+list(red.basis,n)+'<h4>Left-kernel basis: '+m+' output coordinates</h4>'+list(left.basis,m)+'<p>Every kernel direction gives zero under A, and every left-kernel direction gives zero under its transpose. Their independent free-coordinate patterns and dimensions certify completeness. A load is attainable exactly when every displayed left-kernel vector has zero dot product with it.</p></section>';
  trace=red.trace;position=0;
  Object.assign(output.dataset,{valid:'true',input:JSON.stringify(encode(a)),rank:String(r),pivots:JSON.stringify(red.p),rref:JSON.stringify(encode(red.a)),column:JSON.stringify(encode(cols)),row:JSON.stringify(encode(rb)),null:JSON.stringify(encode(red.basis)),left:JSON.stringify(encode(left.basis)),trace:JSON.stringify(trace.map(s=>({op:s.op,a:encode(s.a)})))});
  show();
 }catch(e){trace=[];output.dataset.valid='false';output.textContent=e.message;document.querySelectorAll('[data-rank-step]').forEach(b=>b.disabled=true)}
}
form.addEventListener('submit',e=>{e.preventDefault();compute()});form.addEventListener('input',compute);
const presets={pivot:'1 2 0 1 0\n0 0 1 1 0\n1 2 0 1 1\n-1 -2 0 -1 0',tall:'1 0\n0 1\n1 1',wide:'1 0 1\n0 1 1',zero:'0 0 0\n0 0 0',fractions:'1/2 1/3 1\n1 2/3 2',exceptional:'1 1 1\n1 1 1\n1 1 1'};
document.querySelectorAll('[data-rank-preset]').forEach(b=>b.addEventListener('click',()=>{form.elements.matrix.value=presets[b.dataset.rankPreset];compute()}));
document.querySelectorAll('[data-rank-step]').forEach(b=>b.addEventListener('click',()=>{if(!trace.length)return;position=b.dataset.rankStep==='reset'?0:Math.max(0,Math.min(trace.length-1,position+(b.dataset.rankStep==='next'?1:-1)));show()}));
compute();
})();
'''
(ROOT/'dist/chapters/l_rank.js').write_text(prefix+helpers+rest,encoding='utf-8')
css=(ROOT/'dist/chapters/l_gauss.css').read_text().replace('gauss','rank')
(ROOT/'dist/chapters/l_rank.css').write_text(css,encoding='utf-8')
print('Exact four-space rational laboratory written.')
