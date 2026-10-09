from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/advanced-simulations.js';s=p.read_text()
s=s.replace('function pairGeometry(before,after){','function pairGeometry(before,after,model){')
s=s.replace("const add=(a,b)=>{if(!a||!b||a.tagName!==b.tagName)return;","const add=(a,b)=>{if(!a||!b||a.tagName!==b.tagName)return;if(model.kind==='heap'&&!['text','tspan'].includes(b.tagName.toLowerCase()))return;")
s=s.replace('pairs=pairGeometry(before,svg);','pairs=pairGeometry(before,svg,model);')
s=s.replace("el('h4',t.operation??f.caption,'sim-operation')","el('h4',!t.operation||t.operation.length<24?f.caption:t.operation,'sim-operation')")
s=s.replace("el('p',t.why??f.caption,'sim-why')","el('p',t.why??f.caption,'sim-why')")
# Shared construction must preserve metadata without fabricating intermediate mathematical states.
s=s.replace("const signature=g=>", "const signature=g=>")
p.write_text(s,encoding='utf-8')
print('Heap slot bodies remain fixed; informative saved captions label short operation names.')
