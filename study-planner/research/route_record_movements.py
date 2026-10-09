from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text(encoding='utf-8')
a="}${tx(start+j*w+(w-10)/2,y+38,format(v),'sim-number')}${tx(start+j*w+(w-10)/2,y+88,j,'sim-number')}</g>"
b="}${tx(start+j*w+(w-10)/2,y+38,format(v),'sim-number')}</g>${tx(start+j*w+(w-10)/2,y+88,j,'sim-number sim-slot-index')}"
assert a in s;s=s.replace(a,b)
s=s.replace("pairs=[],affected=[],flows=[],view=", "pairs=[],affected=[],flows=[],recordRoutes=[],hiddenAnnotations=[],view=")
s=s.replace("pairs=[];affected=[];flows=[];", "pairs=[];affected=[];flows=[];recordRoutes=[];hiddenAnnotations=[];")
start="  function setGeometry(t){transition=t;"
replace="""  function setGeometry(t){transition=t;const horizontal=Math.max(0,Math.min(1,(t-.25)/.5)),lift=t<.25?t/.25:t>.75?(1-t)/.25:1;
   for(const n of hiddenAnnotations)n.style.visibility=t<1?'hidden':'';
"""
assert start in s;s=s.replace(start,replace)
s=s.replace("p.a[j]+(p.b[j]-p.a[j++])*t", "p.a[j]+(p.b[j]-p.a[j++])*(p.route?horizontal:t)")
s=s.replace("for(const n of affected)n.style.opacity=", "for(const r of recordRoutes){if(t===1){if(r.base)r.node.setAttribute('transform',r.base);else r.node.removeAttribute('transform');}else{const base=r.node.getAttribute('transform')??r.base;r.node.setAttribute('transform',(base||'')+' translate(0 '+(r.lane*lift)+')');}}for(const n of affected)n.style.opacity=")
# Each geometry update restores a fresh base transform first, avoiding accumulation
# when a route has only direct x/y attributes and no transform interpolation.
s=s.replace("const base=r.node.getAttribute('transform')??r.base;", "const base=r.transformPair?r.node.getAttribute('transform'):r.base;")
marker="  function dependencyFlows(svg,before){"
code="""  function recordMovementRoutes(svg,before){
   if(!(['a_sort','a_select'].includes(topic)||model.kind==='concept:bars')||model.kind==='heap')return;
   const old=new Map([...before.querySelectorAll('[data-entity]')].map(n=>[n.dataset.entity,n])),translation=n=>{const q=n.getAttribute('transform');if(!q)return [0,0];const match=q.match(/^translate\\(\\s*(-?[\\d.]+)[ ,]+(-?[\\d.]+)\\s*\\)$/);return match?[+match[1],+match[2]]:null;};
   for(const g of svg.querySelectorAll('[data-entity]')){const a=old.get(g.dataset.entity),r=g.querySelector(':scope>rect'),oldRect=a?.querySelector(':scope>rect');if(!a||!r||!oldRect)continue;const A=translation(a),B=translation(g);if(!A||!B)continue;const dims=n=>['x','y','width','height'].map(k=>Number(n.getAttribute(k)));const [x,y,w,h]=dims(r),[ox,oy,ow,oh]=dims(oldRect),dx=x+B[0]-ox-A[0];if(Math.abs(dx)<2||Math.abs(y+B[1]-oy-A[1])>.1||w!==ow||h!==oh)continue;
    const related=pairs.filter(p=>p.node===g||g.contains(p.node));if(!related.length)continue;const lane=-Math.sign(dx)*(h+10),route={node:g,base:g.getAttribute('transform')??'',lane,transformPair:related.some(p=>p.node===g&&p.attr==='transform')};related.forEach(p=>p.route=true);recordRoutes.push(route);
    const corridor={x:Math.min(x+B[0],ox+A[0]),y:y+B[1]+Math.min(0,lane),w:Math.abs(dx)+w,h:h+Math.abs(lane)};
    for(const t of svg.querySelectorAll('text')){if(t.closest('[data-entity]')||t.closest('defs'))continue;const b=DiagramLayout.box(svg,t);if(Math.min(b.x+b.w,corridor.x+corridor.w)>Math.max(b.x,corridor.x)&&Math.min(b.y+b.h,corridor.y+corridor.h)>Math.max(b.y,corridor.y))hiddenAnnotations.push(t);}
   }
  }
"""
assert marker in s;s=s.replace(marker,code+marker)
s=s.replace("pairs=pairGeometry(before,svg,model);dependencyFlows(svg,before);", "pairs=pairGeometry(before,svg,model);recordMovementRoutes(svg,before);dependencyFlows(svg,before);")
s=s.replace("get dependencyFlows(){return flows.length;}", "get recordRoutes(){return recordRoutes.length;},get dependencyFlows(){return flows.length;}")
s=s.replace("'Highlighted objects are changing. Displayed numbers describe the target checkpoint; motion does not assert intermediate arithmetic values.'", "recordRoutes.length?'Records lift, travel in separate lanes, and settle into their target slots. Displayed values describe the target checkpoint; slot labels reappear after the movement.':'Highlighted objects are changing. Displayed numbers describe the target checkpoint; motion does not assert intermediate arithmetic values.'")
p.write_text(s,encoding='utf-8');print('Record transfers use lift / travel / settle paths; indices remain slot labels.')
