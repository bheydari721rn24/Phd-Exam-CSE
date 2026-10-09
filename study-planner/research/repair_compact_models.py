from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'dist/chapters/a_sort.js';s=p.read_text();s=s.replace("??model.frames[0].teaching.why","??model.frames[0].teaching?.why??'Each comparison selects a branch of the decision tree. Every leaf represents one possible strict input order; the maximum root-to-leaf depth bounds worst-case comparisons.'");p.write_text(s,encoding='utf-8')
p=R/'dist/chapters/advanced-simulations.js';s=p.read_text();old="const exactView=(i,reference=false)=>normalize(renderFrame?renderFrame(model.frames[i],i):reference||retainDrawing?model.frames[i].svg??model.frames[i].html:drawing(model,model.frames[i]).svg,id+'-'+i+'-'+(reference?'reference':'focus'));"
new="""const exactCache=new Map();
  const exactView=(i,reference=false)=>{const key=i+'-'+reference;if(exactCache.has(key))return exactCache.get(key).cloneNode(true);const svg=normalize(renderFrame?renderFrame(model.frames[i],i):reference||retainDrawing?model.frames[i].svg??model.frames[i].html:drawing(model,model.frames[i]).svg,id+'-'+i+'-'+(reference?'reference':'focus'));if(svg.tagName.toLowerCase()==='svg'){const measuring=el('div',undefined,'sim-stage');measuring.style.cssText='position:fixed;left:-10000px;top:0;width:760px;visibility:hidden';measuring.append(svg);host.append(measuring);fit(svg);svg.remove();measuring.remove();}exactCache.set(key,svg.cloneNode(true));return svg;};"""
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf-8')
print('Complete sorting initialization and measured identical before/after/print drawings.')
