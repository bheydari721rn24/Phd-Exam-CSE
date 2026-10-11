'use strict';
(()=>{
const clone=x=>JSON.parse(JSON.stringify(x)),esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const sum=a=>a.reduce((t,v)=>t+v,0),num=x=>Math.abs(x)<1e-12?'0':String(Number(x.toFixed(5)));
function evaluate(spec){
 const s=clone(spec);if(!['moments','joint'].includes(s.kind))throw Error('Select moments or joint moments.');
 if(!Array.isArray(s.points)||s.points.length<1||s.points.length>9)throw Error('Use one through nine atoms.');
 for(const p of s.points)if(!Number.isFinite(p.x)||Math.abs(p.x)>20||!Number.isFinite(p.p)||p.p<0||p.p>1||s.kind==='joint'&&(!Number.isFinite(p.y)||Math.abs(p.y)>20))throw Error('Values must be finite between -20 and 20; probabilities must lie between zero and one.');
 if(Math.abs(sum(s.points.map(p=>p.p))-1)>1e-10)throw Error('Probabilities must sum to one.');
 if(s.center!==undefined&&(!Number.isFinite(s.center)||Math.abs(s.center)>20))throw Error('The center must lie between -20 and 20.');
 const a=s.points,mean=sum(a.map(p=>p.p*p.x)),second=sum(a.map(p=>p.p*p.x*p.x)),variance=sum(a.map(p=>p.p*(p.x-mean)**2)),center=s.center??mean;
 let base,terms,result;
 if(s.kind==='moments'){
  terms=a.map(p=>p.p*(p.x-center)**2);base={kind:s.kind,points:a,mean,second,variance,center,terms};result={mean,second,variance,center,squaredError:sum(terms)};
 }else{
  const meanY=sum(a.map(p=>p.p*p.y)),varY=sum(a.map(p=>p.p*(p.y-meanY)**2)),mixed=sum(a.map(p=>p.p*p.x*p.y));terms=a.map(p=>p.p*(p.x-mean)*(p.y-meanY));base={kind:s.kind,points:a,meanX:mean,meanY,varX:variance,varY,terms};result={meanX:mean,meanY,varX:variance,varY,covariance:sum(terms),mixed,correlation:variance>0&&varY>0?sum(terms)/Math.sqrt(variance*varY):null};
 }
 let accumulated=0;const states=[{...base,cursor:-1,accumulated,action:'Choose the declared center',why:'The law is fixed; partial sums are not the full moment.'}];
 a.forEach((p,i)=>{accumulated+=terms[i];states.push({...base,cursor:i,accumulated,action:'Add atom '+i,why:s.kind==='moments'?'Weight its squared displacement and add it to the ledger.':'Weight the product of its two centered coordinates and add the signed contribution.'});});
 return{spec:s,states,result};
}
const tx=(x,y,t,cls='sv-prose',anchor='start')=>'<text x="'+x+'" y="'+y+'" class="'+cls+'" text-anchor="'+anchor+'">'+esc(t)+'</text>';
const line=(x1,y1,x2,y2,gold=false)=>'<line x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'" stroke="'+(gold?'#b98634':'#7195a5')+'" stroke-width="1.5"/>';
function drawing(z){
 let out='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" aria-label="'+esc(z.action)+'">',a=z.points;
 if(z.kind==='moments'){
  const top=Math.max(...a.map(p=>p.p),.01),w=620/a.length;out+=tx(70,40,'Probability mass · vertical scale follows current maximum')+line(70,260,700,260);
  a.forEach((p,i)=>{const x=80+i*w,h=170*p.p/top;out+='<rect x="'+x+'" y="'+(260-h)+'" width="'+(w-20)+'" height="'+h+'" fill="'+(i<=z.cursor?'#8cb9ad':'#b9d2dd')+'" stroke="#537688"/>'+tx(x+(w-20)/2,285,num(p.x),'sv-math','middle');});
  out+=tx(70,320,'Weighted squared displacement so far: '+num(z.accumulated),'sv-math')+tx(70,345,'Center '+num(z.center)+' · population mean '+num(z.mean),'sv-math');
  if(z.cursor>=0){const p=a[z.cursor];out+=tx(70,65,'Atom '+num(p.x)+' · probability '+num(p.p)+' · weighted square '+num(z.terms[z.cursor]),'sv-math');}
 }else{
  const lo=Math.min(...a.map(p=>p.x))-1,hi=Math.max(...a.map(p=>p.x))+1,low=Math.min(...a.map(p=>p.y))-1,high=Math.max(...a.map(p=>p.y))+1,X=v=>75+330*(v-lo)/(hi-lo),Y=v=>260-175*(v-low)/(high-low);
  out+=tx(70,40,'Joint outcomes · marker area follows probability')+line(65,270,425,270)+line(65,75,65,270)+line(X(z.meanX),75,X(z.meanX),270,true)+line(65,Y(z.meanY),425,Y(z.meanY),true);
  if(z.cursor>=0){const p=a[z.cursor],x=Math.min(X(p.x),X(z.meanX)),y=Math.min(Y(p.y),Y(z.meanY));out+='<rect x="'+x+'" y="'+y+'" width="'+Math.abs(X(p.x)-X(z.meanX))+'" height="'+Math.abs(Y(p.y)-Y(z.meanY))+'" fill="'+(z.terms[z.cursor]>=0?'#cee5d8':'#efd8cb')+'" opacity=".7"/>';}
  const combined=new Map();a.forEach((p,i)=>{const key=p.x+','+p.y,old=combined.get(key)||{x:p.x,y:p.y,p:0,current:false};old.p+=p.p;old.current||=i===z.cursor;combined.set(key,old);});
  for(const p of combined.values())if(p.p>0)out+='<circle cx="'+X(p.x)+'" cy="'+Y(p.y)+'" r="'+(23*Math.sqrt(p.p))+'" fill="'+(p.current?'#b98634':'#578c9d')+'" stroke="#315b6f"><title>'+esc('Joint value ('+num(p.x)+', '+num(p.y)+'), combined probability '+num(p.p))+'</title></circle>';
  for(const v of new Set([Math.min(...a.map(p=>p.x)),Math.max(...a.map(p=>p.x))]))out+=tx(X(v),286,num(v),'sv-math','middle');
  for(const v of new Set([Math.min(...a.map(p=>p.y)),Math.max(...a.map(p=>p.y))]))out+=tx(53,Y(v)+5,num(v),'sv-math','end');
  out+=tx(245,299,'X coordinate','sv-prose','middle')+tx(32,65,'Y','sv-math')+tx(470,78,'Centered contribution ledger')+line(475,180,715,180);
  const top=Math.max(...z.terms.map(Math.abs),.01),w=230/a.length;
  z.terms.forEach((t,i)=>{if(i<=z.cursor){const h=65*Math.abs(t)/top;out+='<rect x="'+(480+i*w)+'" y="'+(t>=0?180-h:180)+'" width="'+Math.max(5,w-8)+'" height="'+h+'" fill="'+(t>=0?'#8cb9ad':'#dbad95')+'"/>';}});
  out+=tx(470,280,'Sum '+num(z.accumulated),'sv-math')+tx(70,335,'Means ('+num(z.meanX)+', '+num(z.meanY)+') · gold lines mark the centers','sv-math');
 }
 return out+'</svg>';
}
function makeModel(id,title,spec){
 const ev=evaluate(spec);return{id,title,spec:ev.spec,result:ev.result,invariant:'The declared normalized finite law determines these moments. Partial accumulation is labeled, and a finite model is not a universal proof.',frames:ev.states.map((z,i)=>({label:z.action,caption:z.why,index:i,duration:1000,svg:drawing(z),formula:'',snapshot:{inputs:ev.spec,state:z,result:i===ev.states.length-1?ev.result:null},teaching:{currentState:z.action,operation:z.action,why:z.why,reading:'Inspect actual values, probability weights and centered contributions in the exact state.',checks:[{mathHtml:'This is the completed result, not a partial accumulator',result:String(i===ev.states.length-1)}]}}))};
}
if(typeof module!=='undefined')module.exports={evaluate,drawing,makeModel};if(typeof document==='undefined')return;
function mount(host,m){
 const c=document.createElement('div');c.className='sv-controls';c.innerHTML='<button data-reset>Restart</button><button data-prev>Previous</button><button data-play>Play</button><button data-next>Next</button><label>Speed<select data-speed></select></label><label>Step<input type="range" data-seek min="0" value="0"></label>';host.querySelector('.sv-stage').before(c);
 for(const cls of['sv-caption','sv-formula','sv-print'])if(!host.querySelector('.'+cls)){const e=document.createElement('div');e.className=cls;host.append(e);}
 return AdvancedSimulations.mount(host,m,{topic:'s_variance',prefix:'sv',retainDrawing:true});
}
async function boot(){
 const data=await(await fetch('s_variance-models.json')).json();globalThis.VariancePlayers=[];
 for(const h of document.querySelectorAll('[data-sv-model]')){const m=data.models.find(m=>m.id===h.dataset.svModel);if(!m)throw Error('Missing finite probability model');VariancePlayers.push(mount(h,m));}
 const f=document.querySelector('#sv-form'),out=document.querySelector('#sv-output'),error=document.querySelector('#sv-error');let active;
 f.addEventListener('submit',e=>{e.preventDefault();try{
  const keys=['x','p',...(f.elements.kind.value==='joint'?['y']:[])],a={};for(const key of keys){const ps=f.elements[key].value.split(',');if(ps.some(v=>!v.trim()))throw Error('Every atom entry must be present.');a[key]=ps.map(Number);}
  if(keys.some(k=>a[k].length!==a.x.length))throw Error('All columns must have the same atom count.');
  const spec={kind:f.elements.kind.value,points:a.x.map((x,i)=>({x,p:a.p[i],...(a.y?{y:a.y[i]}:{})}))};if(f.elements.kind.value==='moments'&&f.elements.center.value.trim())spec.center=Number(f.elements.center.value);
  const m=makeModel('editable-variance','Your finite '+spec.kind+' law',spec);active?.dispose();out.innerHTML='<section class="sv-model"><h3>'+esc(m.title)+'</h3><div class="sv-stage"></div></section><h3>Computed moments</h3><pre>'+esc(JSON.stringify(m.result,null,2))+'</pre>';active=mount(out.firstChild,m);globalThis.VarianceLab=active;error.textContent='';
 }catch(ex){error.textContent=ex.message;}});
 f.dispatchEvent(new Event('submit',{cancelable:true}));
}
boot().catch(e=>{document.querySelector('#sv-error').textContent=e.message;throw e;});
})();
