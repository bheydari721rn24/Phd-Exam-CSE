function parseList(raw){const a=String(raw).split(',').map(x=>x.trim());if(!a.length||a.some(x=>!/^[-+]?\d+$/.test(x)))throw Error('Enter comma-separated integers with no empty entries.');return a.map(Number);}
function evaluate(mode,values,m=5,n=6,mask=0){
 if(mode==='occupancy'){
  if(!Array.isArray(values)||!values.length||values.length>8||values.some(x=>!Number.isInteger(x)||x<0||x>40)||values.reduce((a,b)=>a+b,0)>40)throw Error('Use one to eight occupancies, each a nonnegative integer, with total at most forty.');
  const total=values.reduce((a,b)=>a+b,0),pairs=values.reduce((s,x)=>s+x*(x-1)/2,0);return{count:pairs,total,max:Math.max(...values),min:Math.min(...values),ceil:Math.ceil(total/values.length),floor:Math.floor(total/values.length),values};
 }
 if(mode==='prefix'||mode==='sequence'){
  const limit=mode==='prefix'?12:9;if(!Array.isArray(values)||!values.length||values.length>limit||values.some(x=>!Number.isInteger(x)||x<-20||x>20))throw Error(`Use one to ${limit} integers from −20 to 20.`);
 }
 if(mode==='prefix'){
  if(!Number.isInteger(m)||m<1||m>12)throw Error('Use an integer modulus from one to twelve.');
  const sums=[0],res=[0],first=new Map([[0,0]]);let witness=null,count=0;
  for(let j=0;j<values.length;j++){sums.push(sums.at(-1)+values[j]);res.push(((sums.at(-1)%m)+m)%m);const r=res.at(-1);if(witness===null&&first.has(r))witness=[first.get(r),j+1];if(!first.has(r))first.set(r,j+1);}
  for(let i=0;i<sums.length;i++)for(let j=i+1;j<sums.length;j++)if(res[i]===res[j])count++;
  return{count,sums,res,witness,values,modulus:m};
 }
 if(mode==='sequence'){
  const inc=[],dec=[],predI=[],predD=[];
  values.forEach((v,j)=>{let a=-1,b=-1;for(let i=0;i<j;i++){if(values[i]<v&&(a<0||inc[i]>inc[a]))a=i;if(values[i]>v&&(b<0||dec[i]>dec[b]))b=i;}inc.push(a<0?1:inc[a]+1);dec.push(b<0?1:dec[b]+1);predI.push(a);predD.push(b);});
  const lis=Math.max(...inc),lds=Math.max(...dec);let end=inc.indexOf(lis),path=[];while(end>=0){path.unshift(end);end=predI[end];}
  // Different reference: enumerate every index subset and compare actual adjacent values.
  let bruteI=0,bruteD=0;for(let mask=1;mask<2**values.length;mask++){const a=values.filter((_,i)=>(mask>>i)&1);if(a.every((v,i)=>!i||a[i-1]<v))bruteI=Math.max(bruteI,a.length);if(a.every((v,i)=>!i||a[i-1]>v))bruteD=Math.max(bruteD,a.length);}
  if(lis!==bruteI||lds!==bruteD)throw Error('Sequence recurrence and exhaustive reference disagree.');return{count:lis,lis,lds,inc,dec,predI,predD,path,distinct:new Set(values).size===values.length,values};
 }
 if(mode==='graph'){
  if(!Number.isInteger(n)||![5,6].includes(n)||!Number.isInteger(mask)||mask<0||mask>=2**(n*(n-1)/2))throw Error('Use five or six vertices and a legal nonnegative integer edge-color mask.');
  const edges=[],color=Array.from({length:n},()=>Array(n).fill(0));let k=0;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){let c=(mask>>k++)&1;color[i][j]=color[j][i]=c;edges.push([i,j,c]);}
  const triangles=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let k=j+1;k<n;k++)if(color[i][j]===color[i][k]&&color[i][j]===color[j][k])triangles.push([i,j,k,color[i][j]]);
  return{count:triangles.length,edges,triangles,n,mask};
 }
 throw Error('Select a supported laboratory.');
}
const tx=(x,y,s,size=16,cl='')=>`<text x="${x}" y="${y}" text-anchor="middle" font-size="${size}" ${cl?`class="${cl}"`:''}>${esc(s)}</text>`;
const ln=(x,y,u,v,c='#7da0ad',w=1.5)=>`<path d="M${x},${y} L${u},${v}" fill="none" stroke="${c}" stroke-width="${w}"/>`;
const dot=(x,y,s,fill='#c4e8d8')=>`<circle cx="${x}" cy="${y}" r="17" fill="${fill}" stroke="#7297a9"/>`+tx(x,y+6,s,17,'math-label');
function paint(z,mode){
 let d=tx(380,28,{occupancy:'Actual fibers and equal-label pair counts',prefix:'Indexed prefixes and the actual divisible block',sequence:'Strict ending-length dependencies; green path is a LIS',graph:'Actual complete graph; highlighted edges certify one triangle'}[mode],19);
 if(mode==='occupancy'){
  const w=680/z.values.length;z.values.forEach((v,i)=>{let x=40+i*w;d+=`<rect x="${x}" y="75" width="${w-8}" height="210" rx="5" fill="#eef5f8" stroke="#7297a9"/>`+tx(x+w/2,58,'bin '+(i+1),14);for(let j=0;j<v;j++)d+=`<circle cx="${x+14+(j%3)*(w-25)/3}" cy="${96+Math.floor(j/3)*13}" r="4" fill="#398b71"/>`;d+=tx(x+w/2,315,v+' objects',13)+tx(x+w/2,343,(v*(v-1)/2)+' pairs',13);});
 }else if(mode==='prefix'){
  const w=650/(z.values.length+1);z.res.forEach((r,i)=>{let x=55+i*w;d+=tx(x,77,'S'+i,14,'math-label')+dot(x,120,r,z.witness?.includes(i)?'#ffd894':'#c4e8d8');if(i){if(z.witness&&i>z.witness[0]&&i<=z.witness[1])d+=`<rect x="${x-20}" y="200" width="40" height="44" rx="5" fill="#ffe5b3"/>`;d+=tx(x,230,z.values[i-1],20,'math-label');}});
  if(z.witness){const[a,b]=z.witness;d+=ln(55+a*w,160,55+b*w,160,'#c5835d',3)+tx(380,300,`positions ${a+1}–${b}; sum ${z.sums[b]-z.sums[a]}`,20);}
  else d+=tx(380,300,'No nonempty divisible block exists in this input.',18);
 }else if(mode==='sequence'){
  const w=650/Math.max(z.values.length-1,1);const P=z.values.map((v,i)=>[55+i*w,80+(20-v)*4]);
  z.values.forEach((v,j)=>{for(const i of [z.predI[j],z.predD[j]])if(i>=0)d+=ln(...P[i],...P[j],z.path.includes(i)&&z.path.includes(j)&&z.predI[j]===i?'#45836b':'#bac9cf',2);});
  z.values.forEach((v,j)=>d+=dot(...P[j],v,z.path.includes(j)?'#ffd894':'#c4e8d8')+tx(P[j][0],300,`(${z.inc[j]},${z.dec[j]})`,16,'math-label'));
  d+=tx(380,347,`LIS ${z.lis}; LDS ${z.lds}; distinct values: ${z.distinct}`,18);
 }else{
  const P=Array.from({length:z.n},(_,j)=>[380+140*Math.cos(-Math.PI/2+2*Math.PI*j/z.n),200+140*Math.sin(-Math.PI/2+2*Math.PI*j/z.n)]),t=z.triangles[0];
  z.edges.forEach(([i,j,c])=>d+=ln(...P[i],...P[j],c?'#be735e':'#5d8aa6',t&&t.slice(0,3).includes(i)&&t.slice(0,3).includes(j)?5:1.5));P.forEach((p,i)=>d+=dot(...p,i+1));
  d+=tx(380,385,t?`Witness vertices ${t.slice(0,3).map(x=>x+1).join(', ')}; ${z.count} monochromatic triangles`:'No monochromatic triangle: a verified five-vertex counterexample.',17);
 }
 return '<svg viewBox="0 0 760 410" role="img" aria-label="'+esc(mode)+' laboratory"><title>'+esc(mode)+' exact witness</title>'+d+'</svg>';
}
const form=document.querySelector('#pigeonhole-form'),out=document.querySelector('#pigeonhole-output');
function calculate(ev){ev?.preventDefault();try{
 const f=new FormData(form),mode=f.get('mode');const z=evaluate(mode,mode==='graph'?[]:parseList(f.get('values')),Number(f.get('m')),Number(f.get('n')),Number(f.get('mask')));
 out.dataset.count=z.count;let detail=mode==='occupancy'?`The total is ${z.total}. The actual maximum is ${z.max}; the universal maximum lower bound is ${z.ceil}. The actual minimum is ${z.min}; the universal minimum upper bound is ${z.floor}.`:mode==='prefix'?`Exactly ${z.count} nonempty contiguous ${z.count===1?'block has':'blocks have'} a sum divisible by ${z.modulus}. Prefix positions include zero.`:mode==='sequence'?`The dynamic program and exhaustive index-subset enumeration agree: the LIS length is ${z.lis} and the LDS length is ${z.lds}. ${z.distinct?'The distinct-value theorem applies.':'Duplicates are present; the purely strict distinct-value theorem is not applicable.'}`:`There are ${z.count} monochromatic triangles among all vertex triples. The edge mask encodes pairs in increasing lexicographic order, with bit one red and bit zero blue.`;
 out.innerHTML=`<h3>Exact result: ${math(z.count)}</h3><p>${esc(detail)}</p><div class="pigeonhole-lab-diagram">${paint(z,mode)}</div>`;window.MathLayout?.schedule();
 }catch(e){delete out.dataset.count;out.textContent=e.message;}}
if(form){form.onsubmit=calculate;form.elements.mode.onchange=()=>{const mode=form.elements.mode.value;for(const key of ['values','m','n','mask'])form.elements[key].closest('label').hidden=key==='values'?mode==='graph':key==='m'?mode!=='prefix':mode!=='graph';form.elements.values.value={occupancy:'4,4,3,3,3',prefix:'3,4,2,7,1',sequence:'5,1,4,2,3',graph:''}[mode];calculate();};form.elements.mode.dispatchEvent(new Event('change'));}
window.PigeonholeLab={evaluate,parseList,paint,calculate};
