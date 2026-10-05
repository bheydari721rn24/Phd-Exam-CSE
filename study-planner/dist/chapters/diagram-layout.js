/* Shared geometric finish for subject-specific diagrams, never model-state data. */
"use strict";
(() => {
const NS='http://www.w3.org/2000/svg';let serial=0;
const box=(svg,e)=>{const b=e.getBBox(),m=svg.getScreenCTM().inverse().multiply(e.getScreenCTM()),p=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));return {x:Math.min(...p.map(q=>q.x)),y:Math.min(...p.map(q=>q.y)),w:Math.max(...p.map(q=>q.x))-Math.min(...p.map(q=>q.x)),h:Math.max(...p.map(q=>q.y))-Math.min(...p.map(q=>q.y))};};
const gap=(a,b)=>Math.hypot(Math.max(a.x-b.x-b.w,b.x-a.x-a.w,0),Math.max(a.y-b.y-b.h,b.y-a.y-a.h,0));
function move(svg,e,dx,dy){const m=svg.getScreenCTM().inverse().multiply(e.getScreenCTM()),q=m.inverse(),o=new DOMPoint(0,0).matrixTransform(q),d=new DOMPoint(dx,dy).matrixTransform(q),x=+(e.getAttribute('x')||0),y=+(e.getAttribute('y')||0);e.setAttribute('x',x+d.x-o.x);e.setAttribute('y',y+d.y-o.y);for(const s of e.querySelectorAll('tspan'))if(s.hasAttribute('x'))s.setAttribute('x',+s.getAttribute('x')+d.x-o.x);}
function boundary(b,x,y,tx,ty){const cx=b.x+b.w/2,cy=b.y+b.h/2,dx=tx-cx,dy=ty-cy;if(b.kind==='circle'){const r=b.w/2,len=Math.hypot(dx,dy)||1;return [cx+r*dx/len,cy+r*dy/len];}const k=1/Math.max(Math.abs(dx)/(b.w/2),Math.abs(dy)/(b.h/2),1e-8);return [cx+dx*k,cy+dy*k];}
function local(svg,e,point){return new DOMPoint(...point).matrixTransform(svg.getScreenCTM().inverse().multiply(e.getScreenCTM()).inverse());}
function marker(svg,color){let d=svg.querySelector('defs[data-layout]');if(!d){d=document.createElementNS(NS,'defs');d.dataset.layout='true';svg.prepend(d);}let m=[...d.querySelectorAll('marker')].find(m=>m.dataset.color===color);if(m)return 'url(#'+m.id+')';const id='layout-tip-'+(++serial);m=document.createElementNS(NS,'marker');m.dataset.color=color;Object.entries({id,markerWidth:7,markerHeight:6,refX:7,refY:3,orient:'auto',markerUnits:'userSpaceOnUse'}).forEach(([k,v])=>m.setAttribute(k,v));const p=document.createElementNS(NS,'path');p.setAttribute('d','M0 0L7 3L0 6Z');p.setAttribute('fill',color);m.append(p);d.append(m);return 'url(#'+id+')';}
function finish(svg,{arrows=true,labels=true}={}){
 if(!svg?.isConnected||!svg.getScreenCTM())return;svg.dataset.layoutRevision='ports-padding-3';
 const shapes=[...svg.querySelectorAll('rect,circle')].filter(e=>!e.closest('defs')&&e.getAttribute('fill')!=='none').map((e,i)=>({e,...box(svg,e),kind:e.tagName==='circle'?'circle':'rect',id:e.dataset.layoutBox||'box'+i})).filter(b=>b.w>=28&&b.h>=25&&b.w*b.h<100000);
 shapes.forEach(b=>{b.e.dataset.layoutBox=b.id;});
 const texts=[...svg.querySelectorAll('text')].filter(t=>!t.closest('defs')&&t.textContent.trim());
 if(labels)for(const t of texts){t.style.fontFamily=/[A-Za-z]{4}/.test(t.textContent)?'Source Sans 3, sans-serif':'STIX Two Math, serif';let a=box(svg,t),cx=a.x+a.w/2,cy=a.y+a.h/2;
  const own=shapes.filter(b=>cx>b.x+.1&&cx<b.x+b.w-.1&&cy>b.y-4&&cy<b.y+b.h+4).sort((a,b)=>a.w*a.h-b.w*b.h)[0];
  if(own){t.dataset.layoutLabelFor=own.id;let fs=parseFloat(getComputedStyle(t).fontSize),availW=own.w-16,availH=own.h-12;if(own.kind==='circle'){availW=Math.sqrt(Math.max(0,(own.w/2-5)**2-Math.min(a.h/2,own.h/2-6)**2))*2;}
   if(a.w>availW||a.h>availH){const target=fs*Math.min(availW/a.w,availH/a.h);t.style.fontSize=Math.max(12,target)+'px';a=box(svg,t);}
   // Preserve intentionally separate lines in the same table cell or card.
   const siblings=texts.filter(u=>u!==t).map(u=>box(svg,u)).filter(b=>b.x+b.w/2>own.x&&b.x+b.w/2<own.x+own.w&&b.y+b.h/2>own.y&&b.y+b.h/2<own.y+own.h);
   if(!siblings.length)move(svg,t,own.x+own.w/2-a.x-a.w/2,own.y+own.h/2-a.y-a.h/2);
   else {let dx=a.x<own.x+8?own.x+8-a.x:a.x+a.w>own.x+own.w-8?own.x+own.w-8-a.x-a.w:0,dy=a.y<own.y+6?own.y+6-a.y:a.y+a.h>own.y+own.h-6?own.y+own.h-6-a.y-a.h:0;move(svg,t,dx,dy);}
  }else{delete t.dataset.layoutLabelFor;for(const b of shapes){a=box(svg,t);if(gap(a,b)<12){const options=[[b.x-14-a.x-a.w,0],[b.x+b.w+14-a.x,0],[0,b.y-14-a.y-a.h],[0,b.y+b.h+14-a.y]];options.sort((a,b)=>Math.hypot(...a)-Math.hypot(...b));const [dx,dy]=options.find(([dx,dy])=>a.x+dx>=8&&a.x+a.w+dx<=svg.viewBox.baseVal.width-8&&a.y+dy>=8&&a.y+a.h+dy<=svg.viewBox.baseVal.height-8)||[0,0];move(svg,t,dx,dy);}}
  }
  const b=box(svg,t),v=svg.viewBox.baseVal;move(svg,t,b.x<8?8-b.x:b.x+b.w>v.width-8?v.width-8-b.x-b.w:0,b.y<6?6-b.y:b.y+b.h>v.height-6?v.height-6-b.y-b.h:0);
 }
 // External explanatory labels must not collide with each other. Node/value
 // labels keep their owning shape; only the outside annotation is displaced.
 if(labels){for(let pass=0;pass<6;pass++){let changed=false;for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){const a=box(svg,texts[i]),b=box(svg,texts[j]);if(Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)>1){const t=!texts[j].dataset.layoutLabelFor?texts[j]:!texts[i].dataset.layoutLabelFor?texts[i]:null;if(!t)continue;const own=box(svg,t),other=t===texts[j]?a:b;move(svg,t,0,other.y+other.h+12-own.y);changed=true;}}if(!changed)break;}const bottom=Math.max(svg.viewBox.baseVal.height,...texts.map(t=>{const b=box(svg,t);return b.y+b.h+16;}));if(bottom>svg.viewBox.baseVal.height)svg.setAttribute('viewBox',`0 0 ${svg.viewBox.baseVal.width} ${Math.ceil(bottom)}`);}
 const ports=(x,y)=>shapes.map(b=>({b,d:gap({x,y,w:0,h:0},b)})).filter(q=>q.d<14).sort((a,b)=>a.d-b.d||a.b.w*a.b.h-b.b.w*b.b.h)[0]?.b;
 // Legacy tree/map drawings store straight connectors without endpoint metadata.
 // Infer only links between two distinct filled nodes; axes and cell separators
 // are never converted into directed edges or treated as node connections.
 for(const p of svg.querySelectorAll('path:not([data-layout-arrow])')){if(p.closest('defs')||!/^M[-\d.,\s]+L[-\d.,\s]+$/.test(p.getAttribute('d')||''))continue;const length=p.getTotalLength();if(!length)continue;const m=svg.getScreenCTM().inverse().multiply(p.getScreenCTM()),s=p.getPointAtLength(0).matrixTransform(m),e=p.getPointAtLength(length).matrixTransform(m),a=shapes.find(b=>b.id===p.dataset.layoutSource)||ports(s.x,s.y),b=shapes.find(b=>b.id===p.dataset.layoutTarget)||ports(e.x,e.y);if(!a||!b||a.id===b.id)continue;const A=boundary(a,s.x,s.y,b.x+b.w/2,b.y+b.h/2),B=boundary(b,e.x,e.y,a.x+a.w/2,a.y+a.h/2);p.dataset.layoutSource=a.id;p.dataset.layoutTarget=b.id;p.dataset.start=A.join(',');p.dataset.end=B.join(',');const L=local(svg,p,A),K=local(svg,p,B);p.setAttribute('d',`M${L.x},${L.y}L${K.x},${K.y}`);p.setAttribute('stroke-width','1.6');p.setAttribute('stroke-linecap','round');}
 if(arrows){
  for(const p of svg.querySelectorAll('path[data-layout-arrow]')){const q=JSON.parse(p.dataset.layoutArrow);let [a,b]=q.map(v=>v.slice());const source=ports(...a),target=ports(...b);
   // Coordinate axes and geometric vectors retain their exact mathematical endpoints.
   if(!['geometry','plot','waveform'].includes(svg.dataset.visualType)){if(source)a=boundary(source,...a,...b);if(target)b=boundary(target,...b,...a);}
   p.setAttribute('d',`M${a}L${b}`);p.setAttribute('stroke-width','1.6');p.setAttribute('stroke-linecap','round');p.setAttribute('marker-end',marker(svg,p.getAttribute('stroke')||'#557e91'));p.dataset.start=a.join(',');p.dataset.end=b.join(',');if(source)p.dataset.layoutSource=source.id;if(target)p.dataset.layoutTarget=target.id;
  }
 }
}
function audit(svg){const issues=[],shapes=new Map([...svg.querySelectorAll('[data-layout-box]')].map(e=>[e.dataset.layoutBox,{...box(svg,e),kind:e.tagName==='circle'?'circle':'rect'}]));
 for(const t of svg.querySelectorAll('text')){if(t.closest('defs'))continue;const a=box(svg,t),b=shapes.get(t.dataset.layoutLabelFor);if(b&&b.kind==='rect'){const padding=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(padding[0],padding[1])<7.5||Math.min(padding[2],padding[3])<5.5)issues.push({kind:'padding',text:t.textContent,padding});}const v=svg.viewBox.baseVal;if(a.x<-.5||a.y<-.5||a.x+a.w>v.width+.5||a.y+a.h>v.height+.5)issues.push({kind:'bounds',text:t.textContent});}
 const ts=[...svg.querySelectorAll('text')].filter(t=>!t.closest('defs'));for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){const a=box(svg,ts[i]),b=box(svg,ts[j]);if(Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)>1.5&&Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)>1.5)issues.push({kind:'text-overlap',texts:[ts[i].textContent,ts[j].textContent]});}
 for(const p of svg.querySelectorAll('path[data-layout-source],path[data-layout-target]'))for(const [which,key] of [['start','layoutSource'],['end','layoutTarget']]){const b=shapes.get(p.dataset[key]);if(!b)continue;const m=svg.getScreenCTM().inverse().multiply(p.getScreenCTM()),v=p.getPointAtLength(which==='start'?0:p.getTotalLength()).matrixTransform(m),x=v.x,y=v.y,d=b.kind==='circle'?Math.abs(Math.hypot(x-b.x-b.w/2,y-b.y-b.h/2)-b.w/2):Math.min(Math.abs(x-b.x),Math.abs(x-b.x-b.w),Math.abs(y-b.y),Math.abs(y-b.y-b.h));if(d>.6)issues.push({kind:'detached',which,d});}
 return issues;
}
window.DiagramLayout={finish,audit,box};
})();
