"""Apply the final quantitative and checkpoint interpretation corrections."""
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'dist/chapters/semantic-diagrams.js'
s=P.read_text(encoding='utf-8')
old='const all=p.scene.frames.map(choose),points='
new='const all=p.scene.frames.map(choose),points='
assert old in s
# Connected samples are never presented as an exact continuous response curve.
s=s.replace('text(g,380,345,`Axes: x from 0 to ${maxX}; y from 0 to ${Number(maxY.toFixed(3))}`,17);', '''if(id==="bayes-copy"){const copied=p.scene.frames.slice(0,p.index+1).map(r=>[num(r.snapshot.n),num(r.snapshot.duplicate)]);path(g,copied.map((a,i)=>`${i?"L":"M"}${at(a)}`).join(" "),C.blue,3);copied.forEach(a=>{const [X,Y]=at(a);rect(g,X-4,Y-4,8,8,C.blue);});text(g,490,48,"Green: independent; blue: copied",17);}text(g,380,345,`Saved samples joined for orientation; x 0–${maxX}, y 0–${Number(maxY.toFixed(3))}`,17);''')
s=s.replace('const all=records.map(n=>num(n.label.split(" · ")[0])),max=', 'const selected=p.scene.id==="max-subarray"?({total:[0,7],prefix:[0,5],suffix:[6,7],best:[2,5]}[f.metrics.Component]):null;const all=records.map(n=>num(n.label.split(" · ")[0])),max=')
s=s.replace('54,h,tone(n),"none");text(g,a.x', '54,h,selected?(+n.id.slice(1)>=selected[0]&&+n.id.slice(1)<selected[1]?C.green:"#dbe5eb"):tone(n),"none");text(g,a.x')
s=s.replace('const s=f.snapshot;if(s&&"lt" in s)', 'if(selected)text(g,380,35,`${f.metrics.Component}: highlighted indices [${selected[0]}, ${selected[1]})`,21);const s=f.snapshot;if(s&&"lt" in s)')
P.write_text(s,encoding='utf-8')
p=P.parent/'concept-animation.js';s=p.read_text(encoding='utf-8')
s=s.replace('this.busy=false;if(after)after();','this.busy=false;this.status.textContent=f.status||"This saved state illustrates the stated model; the chapter supplies its general argument.";if(window.MathLayout)MathLayout.schedule();if(after)after();')
s=s.replace('this.busy=true;const begin=performance.now();','this.busy=true;this.status.textContent="Moving drawings interpolate between saved checkpoints; they do not introduce extra mathematical or electrical states.";const begin=performance.now();')
p.write_text(s,encoding='utf-8')
