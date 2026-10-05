from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
a='const ports={},values={};inputs.forEach'
b='const ports={},values={},boxes=devices.map(([name,kind,ins,x,y])=>[x,y-23,x+66+(["NAND","NOR","NOT","XNOR"].includes(kind)?10:0),y+23]);inputs.forEach'
assert a in s;s=s.replace(a,b)
a='path(g,`M${from}H${bend}V${to[1]}H${to[0]}`,color,2.5);'
b='const wire=path(g,orthogonalRoute(from,to,boxes),color,2.5);wire.dataset.net=source;'
assert a in s;s=s.replace(a,b)
a='M${x-8} ${y-12}V${y+12}M${x-19}'
b='M${x} ${y-12}h-8V${y+12}h8M${x-19}'
assert a in s;s=s.replace(a,b)
p.write_text(s,encoding='utf-8')
