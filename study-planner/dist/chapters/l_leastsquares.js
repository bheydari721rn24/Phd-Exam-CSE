"use strict";
(async()=>{
 const db=window.LS_MODEL_DATA??await fetch('l_leastsquares-models.json').then(r=>{if(!r.ok)throw Error('Least-squares model data unavailable');return r.json();});
 const NS='http://www.w3.org/2000/svg',MNS='http://www.w3.org/1998/Math/MathML';
 const svg=(tag,attrs={})=>{const n=document.createElementNS(NS,tag);for(const[k,v]of Object.entries(attrs))n.setAttribute(k,v);return n;};
 const node=(tag,s,cls)=>{const n=document.createElement(tag);if(s!==undefined)n.textContent=s;if(cls)n.className=cls;return n;};
 const text=(s,x,y,label,math=false,anchor='start')=>{const t=svg('text',{x,y,'text-anchor':anchor,class:math?'ls-math':'ls-prose'});t.textContent=label;s.append(t);return t;};
 const line=(s,x1,y1,x2,y2,color='#8baca4',dash=false)=>s.append(svg('line',{x1,y1,x2,y2,stroke:color,'stroke-width':2,...(s._plotClip?{'clip-path':'url(#'+s._plotClip+')'}:{}),...(dash?{'stroke-dasharray':'5 4'}:{})}));
 const dot=(s,x,y,color='#17636a',open=false)=>s.append(svg('circle',{cx:x,cy:y,r:5,fill:open?'white':color,stroke:color,'stroke-width':2,...(s._plotClip?{'clip-path':'url(#'+s._plotClip+')'}:{})}));
 const fmt=x=>Number.isInteger(x)?String(x):String(Number(x.toFixed(4)));
 function axes(s,xmin,xmax,ymin,ymax,width=300){
  const X=x=>62+width*(x-xmin)/(xmax-xmin),Y=y=>265-205*(y-ymin)/(ymax-ymin);
  line(s,62,265,62+width,265);line(s,62,265,62,60);
  text(s,62,288,fmt(xmin),true,'middle');text(s,62+width,288,fmt(xmax),true,'middle');text(s,56,269,fmt(ymin),true,'end');text(s,56,66,fmt(ymax),true,'end');const id='ls-clip-'+Math.random().toString(36).slice(2),defs=svg('defs'),clip=svg('clipPath',{id});clip.append(svg('rect',{x:62,y:60,width,height:205}));defs.append(clip);s.append(defs);s._plotClip=id;return{X,Y};
 }
 function legend(s,entries){entries.forEach(([label,value],i)=>{const y=82+i*49;text(s,410,y,label);text(s,410,y+23,value,true);});}
 function draw(f){
  const s=svg('svg',{viewBox:'0 0 760 330',role:'img','aria-label':f.title});s.append(svg('title'));s.firstChild.textContent=f.title;
  if(f.kind==='fit'){
   const minT=Math.min(...f.t),maxT=Math.max(...f.t),ends=[f.c+f.d*minT,f.c+f.d*maxT];let lo=Math.min(0,...f.y,...ends)-.5,hi=Math.max(...f.y,...ends)+.5;if(hi-lo<1)hi=lo+1;
   const {X,Y}=axes(s,minT-.3,maxT+.3,lo,hi);line(s,X(minT),Y(ends[0]),X(maxT),Y(ends[1]),'#17636a');
   f.t.forEach((t,i)=>{const fit=f.c+f.d*t;line(s,X(t),Y(f.y[i]),X(t),Y(fit),f.omit===i?'#a04d51':'#bc9665',true);dot(s,X(t),Y(f.y[i]),'#253e59',f.omit===i);dot(s,X(t),Y(fit),'#17636a');});
   text(s,210,316,'Input t; vertical response errors',false,'middle');legend(s,[['Intercept c',f.exactC],['Slope d',f.exactD],['Declared squared error',f.sse],['Residuals in input order',f.residual.join(', ')]]);
  }else if(f.kind==='coefficients'){
   const {X,Y}=axes(s,-1,5,-2,4,205),a=f.a;
   const pts=[-1,5].map(x=>[x,(f.rhs-a[0]*x)/a[1]]);line(s,X(pts[0][0]),Y(pts[0][1]),X(pts[1][0]),Y(pts[1][1]),'#17636a');dot(s,X(f.point[0]),Y(f.point[1]));
   if(f.target){dot(s,X(f.target[0]),Y(f.target[1]),'#a04d51');line(s,X(f.point[0]),Y(f.point[1]),X(f.target[0]),Y(f.target[1]),'#bc9665',true);}
   text(s,210,316,'Coefficient space: x₁ horizontal, x₂ vertical',false,'middle');legend(s,[['Moving coefficient pair',f.pointExact.join(', ')],['Constraint / identical-fit line',a[0]+'x₁ + '+a[1]+'x₂ = '+f.rhs],['Squared observation error',f.sse]]);
  }else if(f.kind==='ridge'){
   const val=x=>(3-x)**2+f.lam*x*x,ymax=Math.max(10,val(3.3)),{X,Y}=axes(s,0,3.3,0,ymax);
   const pts=Array.from({length:101},(_,i)=>{const x=3.3*i/100;return X(x)+','+Y(val(x));}).join(' ');s.append(svg('polyline',{points:pts,fill:'none',stroke:'#17636a','stroke-width':2.5}));dot(s,X(f.x),Y(val(f.x)));text(s,210,316,'Coefficient x; complete loss on vertical axis',false,'middle');legend(s,[['Penalty λ / optimal x',f.lambdaExact+' / '+f.xExact],['Residual squared',f.residualSSE],['Penalty contribution',f.penalty],['Complete objective minimum',f.sse]]);
  }else if(f.kind==='ridge-identity'){
   const val=a=>25*(1-a)**2+25*f.lam*a*a,ymax=Math.max(28,val(1.1)),{X,Y}=axes(s,0,1.1,0,ymax),pts=Array.from({length:101},(_,i)=>{const a=1.1*i/100;return X(a)+','+Y(val(a));}).join(' ');s.append(svg('polyline',{points:pts,fill:'none',stroke:'#17636a','stroke-width':2.5}));dot(s,X(f.alpha),Y(val(f.alpha)));text(s,210,316,'Scale α in x = α(3,4); vertical complete loss',false,'middle');legend(s,[['Penalty λ',f.lambdaExact],['Optimal coefficient pair',f.xExact.join(', ')],['Residual / penalty terms',f.residualSSE+' / '+f.penalty],['Complete objective minimum',f.sse]]);
  }else if(f.kind==='vectors'){
   const {X,Y}=axes(s,-6,9,-3,7.25);line(s,X(0),Y(-3),X(0),Y(7.25),'#c5d5d0');line(s,X(-6),Y(0),X(9),Y(0),'#c5d5d0');
   // Arrowheads are attached at the real endpoint, with orientation from the vector.
   const defs=svg('defs');s.append(defs);['#17636a','#a04d51'].forEach((c,i)=>{const id='ls-arrow-'+Math.random().toString(36).slice(2);const marker=svg('marker',{id,viewBox:'0 0 10 10',refX:9,refY:5,markerWidth:5,markerHeight:5,orient:'auto'});marker.append(svg('path',{d:'M0 0L10 5L0 10Z',fill:c}));defs.append(marker);const v=f.vectors[i];s.append(svg('line',{x1:X(0),y1:Y(0),x2:X(v[0]),y2:Y(v[1]),stroke:c,'stroke-width':2.5,'marker-end':'url(#'+id+')'}));});
   text(s,210,316,'Observation coordinates; numeric axes',false,'middle');legend(s,f.vectors.map((v,i)=>[f.labels[i],v.map(fmt).join(', ')]).concat([['Invariant minimum squared distance',f.sse]]));
  }else if(f.kind==='sensitivity'){
   const lim=Math.max(2,...f.x.map(Math.abs))+1,{X,Y}=axes(s,-lim,lim,-lim,lim,205);line(s,X(-lim),Y(1+lim),X(lim),Y(1-lim),'#17636a');dot(s,X(1),Y(0),'#a04d51');dot(s,X(f.x[0]),Y(f.x[1]));text(s,210,316,'Coefficient space; axis scale changes explicitly',false,'middle');legend(s,[['Column separation ε',f.epsilon],['Old → new coefficients','(1,0) → ('+f.xExact.join(', ')+')'],['Observation change norm',f.delta],['Residual squared remains',f.sse]]);
  }else if(f.kind==='noise'){
   const {X,Y}=axes(s,-1.5,1.5,-1.5,1.5);line(s,X(0),Y(-1.5),X(0),Y(1.5),'#c5d5d0');line(s,X(-1.5),Y(0),X(1.5),Y(0),'#c5d5d0');[[1,0],[0,1],[0,-1],[-1,0]].forEach(p=>dot(s,X(p[0]),Y(p[1]),'#a8c4ba'));dot(s,X(f.point[0]),Y(f.point[1]));text(s,210,316,'M horizontal; first residual D vertical',false,'middle');legend(s,[['Current errors ε₁, ε₂',f.errors.join(', ')],['Coefficient error M',fmt(f.point[0])],['First residual D',fmt(f.point[1])],['Probability of each support point','1/4']]);
  }
  return s;
 }
 class Player{
  constructor(host,frames){this.host=host;this.frames=frames;this.index=0;this.timer=null;this.buttons={};this.stage=host.querySelector('.ls-stage');this.caption=host.querySelector('.ls-caption');this.why=host.querySelector('.ls-why');this.seek=host.querySelector('[data-seek]');this.seek.max=frames.length-1;
   ['reset','prev','play','next'].forEach(k=>this.buttons[k]=host.querySelector('[data-'+k+']'));this.buttons.reset.onclick=()=>{this.pause();this.show(0);};this.buttons.prev.onclick=()=>{this.pause();this.show(this.index-1);};this.buttons.next.onclick=()=>{this.pause();this.show(this.index+1);};this.buttons.play.onclick=()=>this.timer?this.pause():this.play();this.seek.oninput=()=>{this.pause();this.show(Number(this.seek.value));};this.show(0);
  }
  pause(){clearInterval(this.timer);this.timer=null;this.buttons.play.textContent='Play';this.buttons.play.setAttribute('aria-pressed','false');}
  play(){if(this.index===this.frames.length-1)this.show(0);this.buttons.play.textContent='Pause';this.buttons.play.setAttribute('aria-pressed','true');this.timer=setInterval(()=>{this.show(this.index+1);if(this.index===this.frames.length-1)this.pause();},1300);}
  show(k){this.index=Math.max(0,Math.min(k,this.frames.length-1));const f=this.frames[this.index];this.stage.replaceChildren(draw(f));this.caption.textContent=f.title+' · checkpoint '+(this.index+1)+' of '+this.frames.length;this.why.textContent=f.why;this.seek.value=this.index;this.buttons.prev.disabled=this.index===0;this.buttons.next.disabled=this.index===this.frames.length-1;this.host.dataset.step=this.index;}
  print(){const out=this.host.querySelector('.ls-print');out.replaceChildren();for(const f of this.frames){const fig=node('figure');fig.append(draw(f),node('figcaption',f.title+'. '+f.why));out.append(fig);}}
 }
 const players=[...document.querySelectorAll('[data-ls-model]')].map(h=>new Player(h,db[h.dataset.lsModel]));window.LeastSquaresPlayers=players;
 addEventListener('beforeprint',()=>players.forEach(p=>{p.pause();p.print();}));document.addEventListener('visibilitychange',()=>{if(document.hidden)players.forEach(p=>p.pause());});
 const gcd=(a,b)=>b?gcd(b,a%b):a,F=(a,b=1n)=>{if(b<0n){a=-a;b=-b;}const g=gcd(a<0n?-a:a,b);return[a/g,b/g];},add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>{if(!b[0])throw Error('The effective design is rank deficient.');return F(a[0]*b[1],a[1]*b[0]);},neg=a=>[-a[0],a[1]],show=a=>a[1]===1n?String(a[0]):a[0]+'/'+a[1],num=a=>Number(a[0])/Number(a[1]),sum=a=>a.reduce(add,F(0n));
 const form=document.getElementById('ls-explorer');const explorer=players.find(p=>p.host.id==='ls-editable-player');
 function update(){
  const error=document.getElementById('ls-error');error.textContent='';
  try{
   const y=[0,1,2].map(i=>Number(form.elements['y'+i].value)),w=[0,1,2].map(i=>Number(form.elements['w'+i].value));if(y.some(x=>!Number.isInteger(x)||x< -10||x>10)||w.some(x=>!Number.isInteger(x)||x<1||x>9))throw Error('Use integer responses from −10 to 10 and positive integer weights from 1 to 9.');
   const ys=y.map(x=>F(BigInt(x))),ws=w.map(x=>F(BigInt(x))),ts=[1,2,3].map(x=>F(BigInt(x))),s=sum(ws),st=sum(ws.map((v,i)=>mul(v,ts[i]))),st2=sum(ws.map((v,i)=>mul(v,mul(ts[i],ts[i])))),sy=sum(ws.map((v,i)=>mul(v,ys[i]))),sty=sum(ws.map((v,i)=>mul(v,mul(ts[i],ys[i]))));
   let c,d;if(form.elements.model.value==='constant'){c=div(sy,s);d=F(0n);}else{const det=add(mul(s,st2),neg(mul(st,st)));c=div(add(mul(st2,sy),neg(mul(st,sty))),det);d=div(add(mul(s,sty),neg(mul(st,sy))),det);}
   const residual=ys.map((v,i)=>add(v,neg(add(c,mul(d,ts[i]))))),sse=sum(residual.map((v,i)=>mul(ws[i],mul(v,v)))),normal0=sum(residual.map((v,i)=>mul(ws[i],v))),normal1=sum(residual.map((v,i)=>mul(ws[i],mul(ts[i],v))));
   const f={kind:'fit',t:[1,2,3],y,w,c:num(c),d:num(d),exactC:show(c),exactD:show(d),sse:show(sse),residual:residual.map(show),title:'Your exact weighted fit',why:'Integer inputs are solved with exact rational arithmetic. The certificate below uses the same weights and responses as the graph.'};explorer.pause();explorer.frames=[f];explorer.seek.max=0;explorer.show(0);
   const out=document.getElementById('ls-exact-output');out.replaceChildren();Object.assign(out.dataset,{c:show(c),d:show(d),sse:show(sse),normal0:show(normal0),normal1:show(normal1),valid:'true'});
   [['Intercept',c],['Slope',d],['Weighted squared error',sse],['Weighted residual sum',normal0],['Weighted time-residual sum',normal1]].forEach(([label,value])=>{const p=node('p',label+': '),m=document.createElementNS(MNS,'math');m.setAttribute('aria-label',show(value));const n=x=>{const v=document.createElementNS(MNS,'mn');v.textContent=x;return v;};if(value[1]===1n)m.append(n(value[0]));else{const frac=document.createElementNS(MNS,'mfrac');frac.append(n(value[0]),n(value[1]));m.append(frac);}p.append(m);out.append(p);});
   out.append(node('p',form.elements.model.value==='constant'?'Only the constant-column product must vanish. The time product is displayed for comparison and need not be zero.':'Both weighted products vanish because the two sampled design columns are independent.'));
  }catch(e){error.textContent=e.message;document.getElementById('ls-exact-output').dataset.valid='false';}
 }
 form.addEventListener('submit',e=>{e.preventDefault();update();});update();
})().catch(e=>{console.error(e);document.querySelectorAll('.ls-stage:empty').forEach(h=>h.textContent='The animation data could not load. The complete written derivation remains available.');});
