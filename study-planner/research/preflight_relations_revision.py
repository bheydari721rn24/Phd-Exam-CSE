from pathlib import Path
import sys,re,json
B=Path(__file__).parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
bad=[];total=0
for p in (B/'deep-library-revision').glob('d_relations-*.md'):
 for m in re.finditer(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',p.read_text()):
  f=m[1]or m[2];total+=1
  try:mathml.render(f,bool(m[1]))
  except Exception as e:bad.append(dict(file=p.name,formula=f,error=str(e)))
print(json.dumps(dict(formulas=total,errors=bad),indent=2));assert not bad
