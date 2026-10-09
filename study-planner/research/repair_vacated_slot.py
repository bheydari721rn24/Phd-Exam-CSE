from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text(encoding='utf-8')
marker="for(const n of affected)n.style.opacity="
code="""// Empty-slot markers appear only after the traveling record vacates the slot.
   if(recordRoutes.length){const svg=stage.querySelector('svg'),records=[...svg.querySelectorAll('[data-entity]>rect')].filter(r=>!r.parentElement.dataset.entity.startsWith('hole-')).map(r=>DiagramLayout.box(svg,r));for(const g of svg.querySelectorAll('[data-entity^="hole-"]')){const r=g.querySelector('rect');if(!r)continue;const b=DiagramLayout.box(svg,r),covered=records.some(a=>Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x)>1&&Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y)>1);g.style.visibility=t<1&&covered?'hidden':'';}}
   """
assert marker in s;s=s.replace(marker,code+marker);p.write_text(s,encoding='utf-8')
p=R/'research/qa_record_routes.py';s=p.read_text(encoding='utf-8');s=s.replace('if(!p.recordRoutes)continue;','if(!p.motionPairs)continue;');s=s.replace("svg.querySelectorAll('[data-entity]>rect')].map","svg.querySelectorAll('[data-entity]>rect')].filter(r=>getComputedStyle(r).visibility!=='hidden').map");p.write_text(s,encoding='utf-8')
