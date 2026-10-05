from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];p=ROOT/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
s=s.replace('["E","NOT",["E_n"],150,40]','["E","NOT",["E_n"],150,65]')
s=s.replace('s.outputs.join(" and ")}`,20);return;}','s.outputs.join(" and ")}`,20);g.querySelectorAll(`path[data-net="${s.product}"]`).forEach(e=>e.setAttribute("stroke",C.amber));return;}')
# Remove ambiguous raw-TeX fallback even in a model without a numerical snapshot.
s=s.replace('derivation(p,g,f);\n}', 'derivationExact(p,g,f);\n}')
p.write_text(s,encoding='utf-8')
p=ROOT/'research/qa_subject_visuals.py';s=p.read_text(encoding='utf-8')
a='const b=t.getBBox();if(b.x<0'
b='const local=t.getBBox(),matrix=p.canvas.getScreenCTM().inverse().multiply(t.getScreenCTM()),corners=[[local.x,local.y],[local.x+local.width,local.y],[local.x,local.y+local.height],[local.x+local.width,local.y+local.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(matrix)),b={x:Math.min(...corners.map(a=>a.x)),y:Math.min(...corners.map(a=>a.y)),width:Math.max(...corners.map(a=>a.x))-Math.min(...corners.map(a=>a.x)),height:Math.max(...corners.map(a=>a.y))-Math.min(...corners.map(a=>a.y))};if(b.x<-.5'
assert a in s;s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
