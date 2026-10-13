"""Evaluate numeric end equalities in the new manuscripts independently."""
from pathlib import Path
import re, ast, json
B=Path(__file__).parent;E=B/'deep-library-revision';checked=[]
def group(s,i):
 if s[i]!='{':return s[i],i+1
 depth=1;j=i+1
 while depth:
  if s[j]=='{':depth+=1
  elif s[j]=='}':depth-=1
  j+=1
 return s[i+1:j-1],j
def convert(s):
 while r'\frac'in s:
  i=s.index(r'\frac');a,j=group(s,i+5);b,k=group(s,j);s=s[:i]+'(('+convert(a)+')/('+convert(b)+'))'+s[k:]
 s=s.replace(r'\cdot','*').replace('^','**').replace('{','(').replace('}',')').replace('−','-')
 s=re.sub(r'(?<=[0-9)])(?=\()', '*',s);s=re.sub(r'(?<=\))(?=[0-9])','*',s)
 return s
for p in[E/'d_invariants-solutions.md',E/'d_invariants-method-instruction.md',E/'d_invariants-transfer-challenges.md']:
 for equation in re.findall(r'\$([^$\n]+)\$',p.read_text(encoding='utf-8')):
  if '='not in equation:continue
  lhs,rhs=equation.rsplit('=',1);lhs=lhs.split('=')[-1]
  if not re.fullmatch(r'-?\d+',rhs.strip()):continue
  if re.search('[A-Za-z]',lhs.replace(r'\frac','').replace(r'\cdot','')):continue
  expr=convert(lhs);tree=ast.parse(expr,mode='eval');allowed=(ast.Expression,ast.BinOp,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.Constant,ast.UnaryOp,ast.USub)
  assert all(isinstance(n,allowed)for n in ast.walk(tree)),expr
  value=eval(compile(tree,'<numeric end equality>','eval'),{'__builtins__':{}});assert value==int(rhs),(p.name,equation,value)
  checked.append(dict(file=p.name,equation=equation))
assert len(checked)>=20,len(checked)
(E/'d_invariants-printed-numerics.json').write_text(json.dumps(dict(status='passed',equationsChecked=len(checked),equations=checked,scope='Fully numeric final equalities in the three new manuscripts. Symbolic statements and conceptual proofs require separate review.'),indent=2)+'\n',encoding='utf-8');print({'numericEqualitiesChecked':len(checked)})
