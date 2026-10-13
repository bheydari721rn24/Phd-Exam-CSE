from pathlib import Path
import sys
B=Path(__file__).parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
p=B.parent/'dist/chapters/g_gates.html';s=p.read_text()
for v in [r'R_1=2\,\mathrm{k\Omega}',r'R_2=1\,\mathrm{k\Omega}']:
 s=s.replace(mathml.render(v,False),mathml.render(v.replace(r'\mathrm{k\Omega}',r'\mathrm{k}\Omega'),False))
p.write_text(s,encoding='utf-8');p=B/'finish_gates_visuals.py';s=p.read_text().replace(r'\mathrm{k\Omega}',r'\mathrm{k}\Omega');p.write_text(s,encoding='utf-8')
