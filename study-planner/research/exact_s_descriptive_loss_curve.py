"""Make L1 knots and quadratic SVG curves exact, without changing numerical states."""
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/s_descriptive.js';s=p.read_text(encoding='utf-8')
old="let pts=[];for(let k=0;k<=160;k++){const u=r[0]+k*(r[1]-r[0])/160;pts.push(x(u)+','+y(loss(u)));}"
new="let curve;if(absolute){const knots=[r[0],...new Set(sorted),r[1]];curve=`<polyline points=\"${knots.map(u=>x(u)+','+y(loss(u))).join(' ')}\" fill=\"none\" stroke=\"#527f99\" stroke-width=\"3\"/>`;}else{const y0=y(loss(r[0])),controlY=y0-240*a.length*(r[0]-mean)*(r[1]-r[0])/maxLoss;curve=`<path d=\"M ${x(r[0])} ${y0} Q 500 ${controlY} ${x(r[1])} ${y(loss(r[1]))}\" fill=\"none\" stroke=\"#527f99\" stroke-width=\"3\"/>`;}"
assert old in s;s=s.replace(old,new)
old="+`<polyline points=\"${pts.join(' ')}\" fill=\"none\" stroke=\"#527f99\" stroke-width=\"3\"/>`"
assert old in s;s=s.replace(old,'+curve')
p.write_text(s,encoding='utf-8')
