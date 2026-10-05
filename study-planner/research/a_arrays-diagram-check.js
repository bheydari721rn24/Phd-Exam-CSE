window.checkDiagram=svg=>{
 const bad=[],boxes=new Map([...svg.querySelectorAll('rect[data-box]')].map(r=>[r.dataset.box,r.getBBox()]));
 const onEdge=(p,b)=>{const [x,y]=p,t=.6;return x>=b.x-t&&x<=b.x+b.width+t&&y>=b.y-t&&y<=b.y+b.height+t&&Math.min(Math.abs(x-b.x),Math.abs(x-b.x-b.width),Math.abs(y-b.y),Math.abs(y-b.y-b.height))<t;};
 for(const p of svg.querySelectorAll('[data-arrow]'))for(const [name,key] of [['start','source'],['end','target']]){const b=boxes.get(p.dataset[key]);if(!b||!onEdge(p.dataset[name].split(',').map(Number),b))bad.push({arrow:p.dataset.source+' → '+p.dataset.target,end:name,problem:'detached endpoint'});}
 for(const t of svg.querySelectorAll('text')){const a=t.getBBox(),own=boxes.get(t.dataset.labelFor);
  if(own){const pad=[a.x-own.x,own.x+own.width-a.x-a.width,a.y-own.y,own.y+own.height-a.y-a.height];if(Math.min(pad[0],pad[1])<7.8||Math.min(pad[2],pad[3])<5.8)bad.push({text:t.textContent,pad,problem:'inside padding'});}
  for(const [key,b] of boxes){if(key===t.dataset.labelFor)continue;const dx=Math.max(b.x-a.x-a.width,a.x-b.x-b.width,0),dy=Math.max(b.y-a.y-a.height,a.y-b.y-b.height,0),gap=Math.hypot(dx,dy);if(gap<13.8)bad.push({text:t.textContent,box:key,gap,problem:'outside clearance'});}
 }
 return bad;
};
