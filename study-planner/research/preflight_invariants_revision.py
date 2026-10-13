from pathlib import Path
import sys,re
B=Path(__file__).parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
errors=[];count=0
for p in (B/'deep-library-revision').glob('d_invariants-*.md'):
 for m in re.finditer(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',p.read_text(encoding='utf-8')):
  count+=1
  try:mathml.render(m[1]or m[2],bool(m[1]))
  except Exception as ex:errors.append((p.name,repr(m[1]or m[2]),str(ex)))
print({'formulas':count,'errors':errors});assert not errors
