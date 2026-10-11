/* Exact rational generator-span laboratory; fixed-coordinate subject models. */
(() => {
'use strict';
const esc=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;};
class Q {constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error('Zero divisor.');if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}add(b){return new Q(this.n*b.d+b.n*this.d,this.d*b.d);}neg(){return new Q(-this.n,this.d);}sub(b){return this.add(b.neg());}mul(b){return new Q(this.n*b.n,this.d*b.d);}div(b){return new Q(this.n*b.d,this.d*b.n);}toString(){return String(this.n)+(this.d===1n?'':'/'+this.d);}}
const q=x=>new Q(x),zero=q(0),one=q(1),cp=A=>A.map(r=>r.map(v=>new Q(v.n,v.d))),values=A=>A.map(r=>r.map(String));
const eq=(a,b)=>a.n===b.n&&a.d===b.d;
const multiply=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,a,k)=>s.add(a.mul(B[k][j])),zero)));
const same=(A,B)=>A.length===B.length&&A.every((r,i)=>r.every((a,j)=>eq(a,B[i][j])));
const mathNum=x=>{const a=String(x).split('/');const mn=s=>s.startsWith('-')?'<mrow><mo>−</mo><mn>'+s.slice(1)+'</mn></mrow>':'<mn>'+esc(s)+'</mn>';return a.length===2?'<mfrac>'+mn(a[0])+mn(a[1])+'</mfrac>':mn(a[0]);};
const matrixMath=A=>'<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mrow><mo>[</mo><mtable>'+A.map(r=>'<mtr>'+r.map(v=>'<mtd>'+mathNum(v)+'</mtd>').join('')+'</mtr>').join('')+'</mtable><mo>]</mo></mrow></math>';
const tx=(x,y,s,cls='label',anchor='start')=>`<text x="${x}" y="${y}" text-anchor="${anchor}" class="lt-${cls}">${esc(s)}</text>`;
function cellLabel(x,y,v){const parts=String(v).split('/');if(parts.length===1)return tx(x+38.5,y+37,String(v).replace('-','−'),'math','middle');const tiny=(s,dy)=>{let z=tx(x+38.5,y+dy,s.replace('-','−'),'math','middle').replace('<text','<text style="font-size:18px"');if(s.length>6)z=z.replace('<text','<text textLength="59" lengthAdjust="spacingAndGlyphs"');return z;};return tiny(parts[0],22)+`<line x1="${x+9}" y1="${y+29}" x2="${x+68}" y2="${y+29}" stroke="#304c61" stroke-width="1.2"/>`+tiny(parts[1],47);}
function grid(A,hot=-1){let s='';A.forEach((r,i)=>r.forEach((v,j)=>{const x=65+j*87,y=115+i*70;s+=`<g data-entity="cell-${i}-${j}"><rect x="${x}" y="${y}" width="77" height="58" rx="7" fill="${i===hot?'#f3deb7':'#e6efea'}" stroke="#b0c4c5"/>`+cellLabel(x,y,v)+'</g>';}));return s;}
function reduce(input,keepSteps=true){const A=cp(input),rows=A.length,cols=A[0].length,E=Array.from({length:rows},(_,i)=>Array.from({length:rows},(_,j)=>q(i===j?1:0))),pivots=[],steps=[];const save=(operation,hot=-1)=>{if(keepSteps)steps.push({A:cp(A),E:cp(E),operation,hot,verified:same(multiply(E,input),A)});};save('Read the original matrix');let r=0;
for(let c=0;c<cols&&r<rows;c++){let p=r;while(p<rows&&!A[p][c].n)p++;if(p===rows)continue;if(p!==r){[A[r],A[p]]=[A[p],A[r]];[E[r],E[p]]=[E[p],E[r]];save('Swap rows '+(r+1)+' and '+(p+1),r);}const d=A[r][c];if(!eq(d,one)){A[r]=A[r].map(v=>v.div(d));E[r]=E[r].map(v=>v.div(d));save('Divide row '+(r+1)+' by '+d,r);}for(let i=0;i<rows;i++){if(i===r||!A[i][c].n)continue;const a=A[i][c];A[i]=A[i].map((v,j)=>v.sub(a.mul(A[r][j])));E[i]=E[i].map((v,j)=>v.sub(a.mul(E[r][j])));save('R'+(i+1)+' becomes R'+(i+1)+' minus ('+a+') R'+(r+1),i);}pivots.push(c);r++;}return {A,E,pivots,steps};}

function inverse(A){const rr=reduce(A);if(rr.pivots.length!==A.length)throw Error('Both synthesis matrices must be invertible.');return rr.E;}
function coordinateLab(A,P,Q0,x){
 A=A.map(r=>r.map(q));P=P.map(r=>r.map(q));Q0=Q0.map(r=>r.map(q));x=x.map(z=>[q(z)]);
 const Pi=inverse(P),Qi=inverse(Q0),M=multiply(multiply(Qi,A),P),v=multiply(P,x),y=multiply(A,v),c=multiply(Qi,y);
 const checks={pathsAgree:same(multiply(M,x),c),outputReconstruction:same(multiply(Q0,c),y),inputReconstruction:same(multiply(Pi,v),x)};
 if(!Object.values(checks).every(Boolean))throw Error('The independent exact checks failed.');
 const result={matrix:values(M),physicalInput:values(v),physicalOutput:values(y),output:values(c),rank:reduce(A,false).pivots.length,checks};
 const labels=['Input coefficients','Physical input','Physical output','Output coefficients'],vectors=[x,v,y,c],operations=['P synthesis','A physical map','Q inverse analysis'],frames=[];
 for(let stage=0;stage<4;stage++){
  let body=tx(24,30,'Your exact coordinate pipeline');
  for(let j=0;j<4;j++){const left=20+190*j;body+='<g data-entity="box-'+j+'"><rect x="'+left+'" y="92" width="150" height="130" rx="8" fill="'+(j<=stage?'#e7f0e9':'#f3f5f4')+'" stroke="#91aca8"/>'+tx(left+75,119,labels[j],'label','middle');vectors[j].forEach((r,k)=>{body+=tx(left+75,156+k*23,j<=stage?String(r[0]).replace('-','−'):'?','math','middle');});body+='</g>';if(j<3)body+='<line x1="'+(left+150)+'" y1="184" x2="'+(left+190)+'" y2="184" stroke="#315d72" stroke-width="2" marker-end="url(#lt-lab-arrow)"/>'+tx(left+170,72,operations[j],'label','middle');}
  body+=tx(24,285,'Both paths use exact rational arithmetic; each basis is checked invertible.')+tx(24,325,'All independently checked equations pass.');
  const snapshot={stage,...result};frames.push({snapshot,svg:'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" data-visual-type="plot"><defs><marker id="lt-lab-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 1L9 5L0 9" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs>'+body+'</svg>',caption:'The boxes distinguish coefficients and physical vectors at both ends.',formulaHtml:matrixMath(values(vectors[stage])),teaching:{operation:stage?operations[stage-1]:'Read input coefficients',why:'A direct representation-matrix path is checked against synthesis, physical action and analysis.',checks:Object.entries(checks).map(([mathHtml,ok])=>({mathHtml,result:String(ok)})),currentState:snapshot,initial:stage===0,reading:'Inputs are bounded integers; inverses and outputs use exact reduced fractions.',guide:['Read coefficients','Synthesize input','Apply operator','Analyze output'],activeLine:stage,mode:'typed-coordinate-pipeline'}});
 }
 return{id:'editable',title:'Your operator and two bases',kind:'typed-coordinate-pipeline',invariant:'The same physical output is recovered by two exact rational paths.',code:['Read input coefficients','Multiply by P','Multiply by A','Multiply by inverse Q'],frames,result};
}
const api={coordinateLab};if(typeof module!=='undefined'){module.exports=api;return;}globalThis.LinearCoordinateModels=api;
const mount=(host,m)=>AdvancedSimulations.mount(host,m,{topic:'l_linear',prefix:'lt'});
const controls=()=>'<div class="lt-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2600">Slow</option><option value="1800" selected>Normal</option><option value="1300">Fast</option></select></label><label>Step<input type="range" data-seek min="0" value="0" aria-label="Coordinate checkpoint"></label></div><div class="lt-stage"></div><p class="lt-caption"></p><p data-progress></p><div class="lt-formula formula-block"></div><div class="lt-print"></div>';
async function boot(){
 const data=await(await fetch('l_linear-models.json')).json();globalThis.LinearPlayers=[];
 for(const host of document.querySelectorAll('[data-lt-model]')){const m=data.models.find(z=>z.id===host.dataset.ltModel);if(!m)throw Error('Missing linear transformation model.');LinearPlayers.push(mount(host,m));}
 const form=document.querySelector('#lt-form'),out=document.querySelector('#lt-output'),err=document.querySelector('#lt-error');let player=null;
 const bounded=s=>/^[-+]?\d+$/.test(s)&&Math.abs(Number(s))<=10;
 const matrix=s=>{const a=s.trim().split(';').map(r=>r.split(',').map(z=>z.trim()));if(a.length!==2||a.some(r=>r.length!==2)||!a.flat().every(bounded))throw Error('Enter two rows of two integers from −10 through 10.');return a.map(r=>r.map(Number));};
 form.addEventListener('submit',e=>{e.preventDefault();try{
  const A=matrix(form.elements.matrix.value),P=matrix(form.elements.inputBasis.value),Q0=matrix(form.elements.outputBasis.value),x=form.elements.vector.value.trim().split(',').map(z=>z.trim());
  if(x.length!==2||!x.every(bounded))throw Error('Enter two integer input coefficients from −10 through 10.');
  const m=coordinateLab(A,P,Q0,x.map(Number));player?.dispose();out.innerHTML='<section class="lt-model" tabindex="0"><h3>'+esc(m.title)+'</h3><p>'+esc(m.invariant)+'</p>'+controls()+'</section><section class="lab-results"><h3>Exact representation matrix</h3>'+matrixMath(m.result.matrix)+'<p>Exact output coefficients:</p>'+matrixMath(m.result.output)+'<p>Rank '+m.result.rank+'. Kernel dimension '+(2-m.result.rank)+'. Both coordinate paths and reconstructions pass.</p></section>';
  player=mount(out.firstChild,m);globalThis.LinearLab=player;err.textContent='';
 }catch(error){err.textContent=error.message;}});
}
boot().catch(error=>{const p=document.createElement('p');p.setAttribute('role','alert');p.textContent='The coordinate laboratory could not initialize: '+error.message;document.querySelector('.lesson').prepend(p);throw error;});
})();
