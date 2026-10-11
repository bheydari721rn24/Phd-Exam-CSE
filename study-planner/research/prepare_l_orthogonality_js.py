from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
base=(R/'dist/chapters/l_spaces.js').read_text(encoding='utf-8')
prefix=base[:base.index('function spanLab')].replace('vs-','og-')
tail=r'''
const trans=A=>A[0].map((_,j)=>A.map(r=>r[j]));
const eye=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>q(i===j?1:0)));
const zeros=(n,m)=>Array.from({length:n},()=>Array.from({length:m},()=>q(0)));
const subtract=(A,B)=>A.map((r,i)=>r.map((a,j)=>a.sub(B[i][j])));
function inverse(A){const z=reduce(A,false);if(z.pivots.length!==A.length)throw Error('The retained basis Gram matrix is singular.');return z.E;}
function projectionLab(raw,vector,weights){
 if(raw.length<2||raw.length>4||raw[0].length<1||raw[0].length>4||raw.some(r=>r.length!==raw[0].length)||vector.length!==raw.length||weights.length!==raw.length)throw Error('Use two through four rows and one through four generator columns.');
 if(!raw.flat().concat(vector).every(z=>Number.isInteger(z)&&Math.abs(z)<=10)||!weights.every(z=>Number.isInteger(z)&&z>=1&&z<=10))throw Error('Generator/target entries must be integers from minus ten through ten; weights are positive integers through ten.');
 const A=raw.map(r=>r.map(q)),x=vector.map(z=>[q(z)]),G=weights.map((w,i)=>weights.map((_,j)=>q(i===j?w:0))),pivots=reduce(A,false).pivots,C=A.map(r=>pivots.map(j=>r[j])),rank=pivots.length,n=A.length;
 const gram=rank?multiply(multiply(trans(C),G),C):[],coef=rank?multiply(multiply(inverse(gram),trans(C)),multiply(G,x)):[],P=rank?multiply(multiply(multiply(C,inverse(gram)),trans(C)),G):zeros(n,n);
 const p=multiply(P,x),r=subtract(x,p),d=multiply(multiply(trans(r),G),r)[0][0],norm=multiply(multiply(trans(x),G),x)[0][0],pnorm=multiply(multiply(trans(p),G),p)[0][0];
 const checks={idempotent:same(multiply(P,P),P),metricSelfAdjoint:same(multiply(trans(P),G),multiply(G,P)),membership:rank?same(multiply(C,coef),p):same(p,zeros(n,1)),residualPerpendicular:rank?same(multiply(multiply(trans(C),G),r),zeros(rank,1)):true,pythagoras:eq(norm,pnorm.add(d))};
 if(!Object.values(checks).every(Boolean))throw Error('An exact independent certificate failed.');
 const result={rank,pivotColumns:pivots,projector:values(P),projection:values(p),residual:values(r),squaredDistance:String(d),coefficients:values(coef),checks};
 const frames=[],vec=[x,p,r],labels=['Input','Projected part','Residual'];
 for(let stage=0;stage<4;stage++){
  let body=tx(24,30,'Your exact perpendicular decomposition');
  for(let j=0;j<3;j++){const left=30+240*j;body+='<rect x="'+left+'" y="90" width="205" height="175" rx="8" fill="#edf2ee" stroke="#a0b3a7"/>'+tx(left+102,120,labels[j],'label','middle');for(let k=0;k<n;k++){const val=j===0||stage>=j?String(vec[j][k][0]).replace('-','−'):'?';body+=tx(left+102,158+k*25,val,'math','middle');}}
  body+=tx(24,302,'Retained generator columns: '+(pivots.length?pivots.map(z=>z+1).join(', '):'none; zero subspace'));
  body+=tx(24,336,'All membership, metric, idempotence and distance certificates pass.');
  const snap={stage,...result};
  frames.push({label:['Read input','Reveal projection','Reveal residual','Check squared distance'][stage],snapshot:snap,svg:'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" data-visual-type="plot">'+body+'</svg>',formulaHtml:stage===3?matrixMath([[String(d)]]):matrixMath(values(vec[Math.min(stage,2)])),caption:'Each column shows an actual coordinate vector. The metric is diagonal with the entered positive weights.',teaching:{operation:['Read input','Reveal projection','Reveal residual','Check squared distance'][stage],why:'Retaining independent original columns avoids a singular generator Gram inverse. Exact rational identities certify the result.',checks:Object.entries(checks).map(([mathHtml,ok])=>({mathHtml,result:String(ok)})),currentState:snap,initial:stage===0,reading:'Coordinate panels do not depict angles. Numerical values are exact reduced rational numbers.',guide:['Select a column basis','Solve its Gram system','Form the physical projection','Verify residual and distance'],activeLine:stage,mode:'exact-weighted-projection'}});
 }
 return{id:'editable',title:'Your weighted subspace',kind:'exact-weighted-projection',invariant:'The unique physical closest point is computed exactly even for dependent generators.',code:['Select independent columns','Solve the retained Gram equations','Form projection and residual','Check metric identities'],frames,result};
}
const api={projectionLab};if(typeof module!=='undefined'){module.exports=api;return;}globalThis.OrthogonalityModels=api;
const mount=(host,m)=>AdvancedSimulations.mount(host,m,{topic:'l_orthogonality',prefix:'og'});
const controls=()=>'<div class="og-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2600">Slow</option><option value="1800" selected>Normal</option><option value="1300">Fast</option></select></label><label>Step<input type="range" data-seek min="0" value="0" aria-label="Projection checkpoint"></label></div><div class="og-stage"></div><p class="og-caption"></p><p data-progress></p><div class="og-formula formula-block"></div><div class="og-print"></div>';
async function boot(){
 const data=await(await fetch('l_orthogonality-models.json')).json();globalThis.OrthogonalityPlayers=[];
 for(const host of document.querySelectorAll('[data-og-model]')){const m=data.models.find(z=>z.id===host.dataset.ogModel);if(!m)throw Error('Missing orthogonality model.');OrthogonalityPlayers.push(mount(host,m));}
 const form=document.querySelector('#og-form'),out=document.querySelector('#og-output'),err=document.querySelector('#og-error');let player=null;
 const list=s=>{const parts=s.trim().split(',').map(z=>z.trim());if(!parts.every(z=>/^[-+]?\d+$/.test(z)))throw Error('Enter comma-separated integers, not decimals or empty entries.');return parts.map(Number);};
 form.addEventListener('submit',e=>{e.preventDefault();try{
  const A=form.elements.matrix.value.trim().split(';').map(list),x=list(form.elements.vector.value),w=list(form.elements.weights.value),m=projectionLab(A,x,w);
  player?.dispose();out.innerHTML='<section class="og-model" tabindex="0"><h3>'+esc(m.title)+'</h3><p>'+esc(m.invariant)+'</p>'+controls()+'</section><section class="lab-results"><h3>Exact projection matrix</h3>'+matrixMath(m.result.projector)+'<p>Exact projected vector:</p>'+matrixMath(m.result.projection)+'<p>Exact perpendicular residual:</p>'+matrixMath(m.result.residual)+'<p>Exact squared distance:</p>'+matrixMath([[m.result.squaredDistance]])+'<p>Rank '+m.result.rank+'. Original independent columns: '+(m.result.pivotColumns.length?m.result.pivotColumns.map(j=>j+1).join(', '):'none')+'. All five independent certificates pass.</p></section>';
  player=mount(out.firstChild,m);globalThis.OrthogonalityLab=player;err.textContent='';
 }catch(error){err.textContent=error.message;}});
}
boot().catch(error=>{const p=document.createElement('p');p.setAttribute('role','alert');p.textContent='The orthogonality laboratory could not initialize: '+error.message;document.querySelector('.lesson').prepend(p);throw error;});
})();
'''
(R/'dist/chapters/l_orthogonality.js').write_text(prefix+tail,encoding='utf-8')
