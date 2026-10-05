from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
base=(R/'dist/chapters/d_pigeonhole.js').read_text(encoding='utf-8').split('function parseList')[0]
base=base.replace('pigeonhole','arrays').replace('d_arrays-models.json','a_arrays-models.json')
base=base.replace("fetch('a_arrays-models.json')", "fetch('a_arrays-models.json?v=ports-2')")
base=base.replace('Exact, independently rendered arrays traces and bounded enumeration laboratory.','Array storage and actual linked topology; exact editable laboratories.')
base=base.replace('const old=new Map([...stage.querySelectorAll', 'const old=new Map([...stage.querySelectorAll')
base=base.replace('return[e.dataset.entity,{x:b.x+b.width/2,y:b.y+b.height/2}];','return[e.dataset.entity,{x:b.x+b.width/2,y:b.y+b.height/2,path:e.querySelector("[data-arrow]")?.getAttribute("d")}];')
old_motion="if(motion&&!reduced.matches){for(const e of stage.querySelectorAll('[data-entity]')){const p=old.get(e.dataset.entity);if(p){const b=e.getBBox(),dx=p.x-b.x-b.width/2,dy=p.y-b.y-b.height/2;if(Math.abs(dx)+Math.abs(dy)>1)e.animate([{transform:`translate(${dx}px,${dy}px)`},{transform:'translate(0,0)'}],{duration:450,easing:'ease-in-out'});}}}"
new_motion=r'''if(motion&&!reduced.matches){let movedNodes=false;const pointerPaths=[];
  for(const e of stage.querySelectorAll('[data-entity]')){const p=old.get(e.dataset.entity);if(!p)continue;const line=e.querySelector('[data-arrow]');if(line&&p.path){pointerPaths.push([line,p.path]);continue;}const b=e.getBBox(),dx=p.x-b.x-b.width/2,dy=p.y-b.y-b.height/2;if(Math.abs(dx)+Math.abs(dy)>1){e.animate([{transform:`translate(${dx}px,${dy}px)`},{transform:'translate(0,0)'}],{duration:450,easing:'ease-in-out'});if(e.querySelector('rect[data-box]'))movedNodes=true;}}
  if(movedNodes){const svg=stage.querySelector('svg'),start=performance.now(),bind=()=>{if(!svg.isConnected)return;const screen=svg.getBoundingClientRect(),view=svg.viewBox.baseVal,boxes=new Map([...svg.querySelectorAll('[data-box]')].map(r=>{const b=r.getBoundingClientRect();return[r.dataset.box,[(b.left-screen.left)*view.width/screen.width-Number(r.getAttribute('x')),(b.top-screen.top)*view.height/screen.height-Number(r.getAttribute('y'))]];}));for(const line of svg.querySelectorAll('[data-arrow]')){const pts=JSON.parse(line.dataset.points),ds=boxes.get(line.dataset.source)||[0,0],dt=boxes.get(line.dataset.target)||[0,0];pts.forEach((p,i)=>{const delta=i===pts.length-1?dt:i===0?ds:pts.length===4?(i===1?ds:dt):i<=2?ds:dt;p[0]+=delta[0];p[1]+=delta[1];});line.setAttribute('d',route(pts));}if(performance.now()-start<480)requestAnimationFrame(bind);};bind();}
  else for(const [line,before] of pointerPaths){const after=line.getAttribute('d');if(before!==after)line.animate([{d:`path("${before}")`},{d:`path("${after}")`}],{duration:450,easing:'ease-in-out'});}
 }'''
assert old_motion in base
base=base.replace(old_motion,new_motion)
lab=r'''
function evaluate(mode,params){
 const int=(v,a,b,name)=>{if(!Number.isInteger(v)||v<a||v>b)throw Error(`${name} must be an integer from ${a} to ${b}.`);return v;};
 if(mode==='growth'){
  const m=int(params.m,1,64,'Appends'),c0=int(params.c0,1,16,'Initial capacity'),g=int(params.g,2,4,'Growth factor');let C=c0,n=0,copies=0,states=[{n,C,copies,last:0}];
  for(let t=0;t<m;t++){let last=0;if(n===C){last=n;copies+=n;C*=g;}n++;states.push({n,C,copies,last});}
  return{mode,m,c0,g,copies,writes:copies+m,capacity:C,states};
 }
 if(mode==='shift'){
  const a=params.values;if(!Array.isArray(a)||a.length<1||a.length>8||a.some(v=>!Number.isInteger(v)||Math.abs(v)>99))throw Error('Use one to eight integers from −99 to 99.');
  const i=int(params.index,0,a.length,'Insertion rank'),x=int(params.value,-99,99,'New value');let v=a.map((x,j)=>({id:'v'+j,value:x}));v.push(null);let states=[{values:v.map(x=>x&&{...x}),writes:0,caption:'Original array plus one spare slot.'}];let writes=0;
  for(let j=a.length;j>i;j--){v[j]={...v[j-1]};writes++;states.push({values:v.map(x=>x&&{...x}),writes,caption:`Copy source ${j-1} backward to ${j}.`});}
  v[i]={id:'new',value:x};writes++;states.push({values:v.map(x=>x&&{...x}),writes,caption:'Write the new value at the supplied rank.'});return{mode,index:i,result:v.map(x=>x.value),writes,shifts:writes-1,states};
 }
 if(mode==='reverse'){
  const n=int(params.n,0,7,'Node count');let next=Array.from({length:n},(_,i)=>i+1<n?i+1:null),prev=null,cur=n?0:null,states=[];let writes=0;
  while(true){states.push({next:[...next],prev,cur,writes});if(cur===null)break;let saved=next[cur];next[cur]=prev;prev=cur;cur=saved;writes++;}
  return{mode,n,head:prev,writes,states};
 }
 if(mode==='floyd'){
  const mu=int(params.mu,0,5,'Prefix length'),lam=int(params.lam,1,5,'Cycle length');let next=Array.from({length:mu+lam},(_,i)=>i+1<mu+lam?i+1:mu),s=0,f=0,t=0,states=[{s,f,t,phase:'detect'}];
  do{s=next[s];f=next[next[f]];t++;states.push({s,f,t,phase:'detect'});}while(s!==f);
  const meeting=t;let h=0,r=0;states.push({s:h,f,t:r,phase:'reset'});while(h!==f){h=next[h];f=next[f];r++;states.push({s:h,f,t:r,phase:'reset'});}
  return{mode,mu,lam,meeting,entry:h,resetSteps:r,states,next};
 }
 throw Error('Choose a supported laboratory.');
}
const tx=(x,y,t,size=16,box='',cl='')=>`<text x="${x}" y="${y}" text-anchor="middle" font-size="${size}" class="${cl}" ${box?`dominant-baseline="middle" data-label-for="${esc(box)}"`:''}>${esc(t)}</text>`;
function route(points,r=6){let d=`M${points[0]}`;for(let j=1;j<points.length-1;j++){const a=points[j-1],b=points[j],c=points[j+1],la=Math.hypot(a[0]-b[0],a[1]-b[1]),lc=Math.hypot(c[0]-b[0],c[1]-b[1]),q=Math.min(r,la/2,lc/2);if(!la||!lc)continue;const p=[b[0]+(a[0]-b[0])*q/la,b[1]+(a[1]-b[1])*q/la],v=[b[0]+(c[0]-b[0])*q/lc,b[1]+(c[1]-b[1])*q/lc];d+=` L${p} Q${b} ${v}`;}return d+` L${points.at(-1)}`;}
function arrow(points,source,target,kind='forward'){return`<path data-arrow="true" data-source="${esc(source)}" data-target="${esc(target)}" data-points="${esc(JSON.stringify(points))}" data-start="${points[0]}" data-end="${points.at(-1)}" d="${route(points)}" fill="none" stroke="${kind==='pointer'?'#7a739d':'#557e91'}" stroke-width="1.6" stroke-linejoin="round" marker-end="url(#lab-${kind})"/>`;}
function picture(z,f){
 let d='';
 if(z.mode==='growth'){
  const width=600;d+=tx(380,50,`Length ${f.n}, capacity ${f.C}`,19)+`<rect x="80" y="110" width="${width}" height="60" fill="#e9f3f5" stroke="#648c9f"/><rect x="80" y="110" width="${width*f.n/f.C}" height="60" fill="#89bbab"/>`;
  d+=tx(380,215,`${f.n} live slots; ${f.C-f.n} unused slots`,18)+tx(380,270,`${f.copies} cumulative copied slots`,18)+tx(380,325,`This append copied ${f.last} slots`,17);
 }else if(z.mode==='shift'){
  let w=650/f.values.length;f.values.forEach((v,i)=>{let x=55+i*w,key='array-'+i;d+=`<rect data-box="${key}" x="${x}" y="135" width="${w-5}" height="60" fill="#e9f3f5" stroke="#6c93a2"/>`+tx(x+(w-5)/2,227,i,14);if(v)d+=`<g data-entity="${v.id}">${tx(x+(w-5)/2,165,v.value,20,key)}</g>`;});d+=tx(380,65,`${f.writes} element writes`,19);
 }else{
  const next=z.mode==='reverse'?f.next:z.next,n=next.length,w=n>1?620/(n-1):0,x=i=>65+i*w,half=n>8?28:36,top=175,bottom=225;
  next.forEach((b,a)=>{let points;if(b===null){const key='null-'+a,ny=251;d+=arrow([[x(a),bottom],[x(a),ny]],'node-'+a,key)+`<rect data-box="${key}" x="${x(a)-47}" y="${ny}" width="94" height="30" rx="6" fill="#fff" stroke="#c4d3db"/>`+tx(x(a),ny+15,'next = null',12,key,'pointer-label');return;}
   if(a===b)points=[[x(a)+half,188],[x(a)+half+24,188],[x(a)+half+24,145],[x(a)+16,145],[x(a)+16,top]];
   else if(Math.abs(a-b)===1){const sign=b>a?1:-1;points=[[x(a)+sign*half,188],[x(b)-sign*half,188]];}
   else points=[[x(a)+16,top],[x(a)+16,145],[x(b)-16,145],[x(b)-16,top]];
   d+=arrow(points,'node-'+a,'node-'+b);
  });
  next.forEach((_,i)=>{const key='node-'+i;d+=`<g data-entity="${key}"><rect data-box="${key}" x="${x(i)-half}" y="${top}" width="${half*2}" height="50" rx="8" fill="#cfe5df" stroke="#659484"/>${tx(x(i),top+25,i,18,key)}</g>`;});
  const cursors=z.mode==='reverse'?{prev:f.prev,cur:f.cur}:{slow:f.s,fast:f.f};Object.entries(cursors).forEach(([name,i],j)=>{const cx=j?580:180,cy=57,key='cursor-'+name;d+=`<rect data-box="${key}" x="${cx-76}" y="${cy}" width="152" height="38" rx="7" fill="#fff" stroke="#bcb6ce"/>`+tx(cx,cy+19,name+(i===null?' = null':''),14,key,'pointer-label');if(i!==null){const u=x(i)+(j?10:-10),lane=115+j*20;d+=`<g data-entity="${key}">`+arrow([[cx,cy+38],[cx,lane],[u,lane],[u,top]],key,'node-'+i,'pointer')+'</g>';}});
  if(!n)d+=tx(380,200,'Empty list: no live nodes',18);
  d+=tx(380,335,z.mode==='reverse'?`${f.writes} rewritten successor fields`:`${f.phase}: ${f.t} complete iterations`,18);
 }
 return`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 410" role="img"><defs>${['forward','pointer'].map(k=>`<marker id="lab-${k}" markerUnits="userSpaceOnUse" markerWidth="7" markerHeight="6" viewBox="0 0 7 6" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="${k==='pointer'?'#7a739d':'#557e91'}"/></marker>`).join('')}</defs>${d}</svg>`;
}
const formula=f=>`<math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>${esc(f)}</mtext></math>`;
const labHost=document.querySelector('#arrays-output');
function labModel(z){
 let title={growth:'Recomputed geometric growth',shift:'Recomputed stable insertion',reverse:'Recomputed linked-list reversal',floyd:'Recomputed Floyd detection and entry'}[z.mode];
 return{id:'editable',title,invariant:'Displayed values, links and cursors are recomputed from the selected input. The complete trace starts paused.',frames:z.states.map(f=>({svg:picture(z,f),caption:f.caption||(z.mode==='growth'?`After ${f.n} appends, capacity ${f.C}; this update copies ${f.last}.`:z.mode==='reverse'?`Reversed prefix contains ${f.writes} nodes; cur identifies the untouched suffix.`:`${f.phase} phase after ${f.t} complete iterations; cursor identities shown above.`),formulaHtml:formula(z.mode==='growth'?`n = ${f.n}; C = ${f.C}; copies = ${f.copies}`:z.mode==='shift'?`writes = ${f.writes}`:z.mode==='reverse'?`next writes = ${f.writes}`:`steps = ${f.t}`)}))};
}
function hostHtml(m){return`<section class="arrays-model" data-arrays-model="editable" tabindex="0"><h3>${esc(m.title)}</h3><p class="arrays-invariant">${esc(m.invariant)}</p><div class="arrays-stage"></div><p class="arrays-caption" aria-live="polite"></p><div class="arrays-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2200">Slow</option><option value="1400" selected>Normal</option><option value="850">Fast</option></select></label><label>Checkpoint<input data-seek type="range" min="0" max="${m.frames.length-1}" value="0"></label></div><p class="arrays-progress" data-progress></p><div class="formula-block arrays-formula"></div><div class="arrays-print-trace"></div></section>`;}
const form=document.querySelector('#arrays-form');
function fields(){const mode=form.mode.value;form.querySelectorAll('[data-modes]').forEach(x=>{x.hidden=!x.dataset.modes.split(' ').includes(mode);});}
function run(event){event?.preventDefault();states.forEach(stop=>stop());try{
 const raw=form.values.value.trim().split(',').map(x=>x.trim());if(form.mode.value==='shift'&&raw.some(x=>!/^[-+]?\d+$/.test(x)))throw Error('Use comma-separated integers with no empty values.');
 const z=evaluate(form.mode.value,{m:Number(form.m.value),c0:Number(form.c0.value),g:Number(form.g.value),values:raw.map(Number),index:Number(form.index.value),value:Number(form.value.value),n:Number(form.n.value),mu:Number(form.mu.value),lam:Number(form.lam.value)}),m=labModel(z);
 labHost.innerHTML=hostHtml(m);mount(labHost.firstElementChild,m);labHost.dataset.result=JSON.stringify(z);document.querySelector('#arrays-lab-error').textContent='';
 }catch(error){document.querySelector('#arrays-lab-error').textContent=error.message;}}
form.addEventListener('submit',run);form.mode.addEventListener('change',()=>{fields();run();});fields();run();
window.ArrayLab={evaluate,picture,labModel};
})();
'''
(R/'dist/chapters/a_arrays.js').write_text(base+lab,encoding='utf-8')
css=(R/'dist/chapters/d_pigeonhole.css').read_text(encoding='utf-8').replace('pigeonhole','arrays')
css+='\n#arrays-form [hidden]{display:none!important}#arrays-form input{box-sizing:border-box}#arrays-form input[name=values]{width:250px}.arrays-lab-error{color:#8d3851}.arrays-stage svg text,.arrays-print-trace svg text{font-weight:400}.arrays-stage [data-entity] text,.arrays-print-trace [data-entity] text{font-family:"STIX Two Math",serif}.arrays-print-trace svg{max-width:100%}\n'
css+='\n.arrays-stage,.arrays-print-trace figure{padding:12px 0}.arrays-controls label{display:inline-flex;align-items:center;gap:8px}.arrays-stage .pointer-label,.arrays-print-trace .pointer-label{font-family:"Source Sans 3",sans-serif!important}.arrays-stage svg,.arrays-print-trace svg{overflow:visible}.arrays-caption{padding-top:12px}.arrays-model{padding:26px}.arrays-controls{gap:12px}@media(max-width:650px){.arrays-model{padding:16px}}\n'
(R/'dist/chapters/a_arrays.css').write_text(css,encoding='utf-8')
s=(B/'render_d_pigeonhole.py').read_text(encoding='utf-8')
s=s.replace('d_pigeonhole','a_arrays').replace('pigeonhole','arrays').replace('==82','==86').replace('enumerate(q,3)','enumerate(q,3)')
start=s.index("lab='<section")
end=s.index("\nsource=",start)
labhtml='''<section class="lab" id="arrays-lab"><form id="arrays-form"><label>Exact laboratory<select name="mode"><option value="growth">Geometric capacity growth</option><option value="shift">Stable array insertion</option><option value="reverse">Linked-list reversal</option><option value="floyd">Floyd cycle and entry</option></select></label><label data-modes="growth">Append count<input name="m" type="number" value="13" min="1" max="64"></label><label data-modes="growth">Initial capacity<input name="c0" type="number" value="1" min="1" max="16"></label><label data-modes="growth">Growth factor<input name="g" type="number" value="2" min="2" max="4"></label><label data-modes="shift">Array values<input name="values" type="text" value="2,4,6,8,10"></label><label data-modes="shift">Insertion rank<input name="index" type="number" value="2" min="0" max="8"></label><label data-modes="shift">New value<input name="value" type="number" value="9" min="-99" max="99"></label><label data-modes="reverse">Real nodes<input name="n" type="number" value="5" min="0" max="7"></label><label data-modes="floyd">Prefix links<input name="mu" type="number" value="3" min="0" max="5"></label><label data-modes="floyd">Cycle links<input name="lam" type="number" value="4" min="1" max="5"></label><button type="submit">Recompute the complete trace</button></form><p id="arrays-lab-error" class="arrays-lab-error" role="alert"></p><div id="arrays-output"></div><p>Growth permits 1–64 appends, initial capacity 1–16, and integer factor 2–4. Insertion permits 1–8 original values from −99 to 99 and any legal insertion rank. Reversal permits 0–7 nodes. Cycle mode permits prefix length 0–5 and cycle length 1–5. Counts exclude allocation and guard reads; cycle comparisons follow complete one-versus-two iterations. An invalid input leaves the last valid trace intact and displays an explanation.</p></section>'''
s=s[:start]+'lab='+repr(labhtml)+s[end:]
a=s.index("anchors=[");z=s.index(';it=iter(anchors)',a)
s=s[:a]+"anchors=['sources','model','shifts','growth','amortization','singly','doubly','reverse','cycles','traversal','transformations','memory','sparse','summary','problems','review','laboratory','references']"+s[z:]
s=s.replace('The Pigeonhole Principle: Sharp Guarantees, Hidden Classes, and Constructive Witnesses','Arrays, Linked Lists, and Operation Costs')
s=s.replace('Discrete Mathematics · Week 3','Data Structures and Algorithms · Week 3').replace('five primary written courses from four universities and a sixth complementary course · 82 worked problems · 80 examination rules · 18 dedicated concept traces','four primary university courses and two complementary courses · 86 worked problems · 80 examination rules · 20 dedicated concept traces')
s=s.replace('questionCount=82','questionCount=86').replace('originalQuestionCount=80','originalQuestionCount=84').replace('animationCount=18','animationCount=20').replace('animationWalkthroughCount=18','animationWalkthroughCount=20')
s=s.replace('Inclusion-exclusion chapter audit','Arrays and linked lists audit').replace('Inclusion-exclusion chapter','Arrays and linked lists chapter')
s=s.replace("mathml.SYMBOLS.update(ell='ℓ',supseteq='⊇')","mathml.SYMBOLS.update(ell='ℓ',supseteq='⊇',Phi='Φ')\noriginal_base=mathml.Parser.base\ndef chapter_base(self):\n self.skip()\n marker=r'\\begin{cases}'\n if self.s.startswith(marker,self.i):\n  self.i+=len(marker);stop=self.s.index(r'\\end{cases}',self.i);content=self.s[self.i:stop];self.i=stop+len(r'\\end{cases}')\n  rows=[row.split('&') for row in content.split(r'\\\\')]\n  return '<mrow><mo>{</mo><mtable columnalign=\"left left\">'+''.join('<mtr>'+''.join('<mtd>'+mathml.Parser(cell).seq()+'</mtd>' for cell in row)+'</mtr>' for row in rows)+'</mtable></mrow>'\n return original_base(self)\nmathml.Parser.base=chapter_base")
s=s.replace("body.count('class=\"exam-question\"')==86","body.count('class=\"exam-question\"')==86")
s=s.replace('href="a_arrays.css"','href="a_arrays.css?v=ports-2"').replace('src="a_arrays.js"','src="a_arrays.js?v=ports-2"')
(B/'render_a_arrays.py').write_text(s,encoding='utf-8')
print('prepared chapter player, four labs, CSS, and isolated renderer')
