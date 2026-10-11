"""Repair exact finite shape equations without regenerating unrelated scenes."""
from pathlib import Path
import json,sys
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text())
for key in ['induction-triangular','induction-square']:
    for f in d['scenes'][key]['frames']:
        n=f['snapshot']['n'];square=key.endswith('square')
        formula=(('+'.join(map(str,range(1,2*n,2)))+f'={n}^2')if square else('+'.join(map(str,range(1,n+1)))+rf'=\frac{{{n}({n}+1)}}2'))if n else('S_0=0'if square else'T_0=0')
        f['formula']=formula
        f['formulaHtml']='<div class="formula-block">'+mathml.render(formula,True)+'</div>'
        f['line']=0 if n==0 else 1
        f['teaching']['activeLine']=f['line'];f['teaching']['operation']=d['scenes'][key]['code'][f['line']]
for i,f in enumerate(d['scenes']['induction-gap']['frames']):
    f['line']=0 if i==0 else 1;f['teaching']['activeLine']=f['line'];f['teaching']['operation']=d['scenes']['induction-gap']['code'][f['line']]
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Exact finite sums and active induction-step labels repaired.')
