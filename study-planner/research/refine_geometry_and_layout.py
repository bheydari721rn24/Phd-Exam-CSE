from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'dist/chapters/math-layout.js';s=p.read_text();s=s.replace('limit=box.clientWidth-40','limit=box.clientWidth-48');p.write_text(s,encoding='utf-8')
p=ROOT/'dist/chapters/semantic-diagrams.js';s=p.read_text(encoding='utf-8')
old=':gauss?300:300,oy=rank?190:gauss?235:245,k=rank?55:gauss?50:65;'
new=':gauss?300:(p.scene.axes?.cx??300),oy=rank?190:gauss?235:(p.scene.axes?.cy??245),k=rank?55:gauss?50:(p.scene.axes?.scale??65);'
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf-8')
