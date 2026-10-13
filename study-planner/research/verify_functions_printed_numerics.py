"""Evaluate fully numerical equations in the actual authored answer manuscript."""
from pathlib import Path
import re,math,json,ast
B=Path(__file__).parent;E=B/'deep-library-revision';s=(E/'d_functions-solutions.md').read_text(encoding='utf-8');checked=[]
def postfix_factorials(s):
 while '!' in s:
  z=s.index('!');a=z-1
  if s[a]==')':
   depth=1;a-=1
   while depth:
    if s[a]==')':depth+=1
    elif s[a]=='(':depth-=1
    a-=1
   a+=1
  else:
   while a>=0 and s[a].isdigit():a-=1
   a+=1
  s=s[:a]+'factorial('+s[a:z]+')'+s[z+1:]
 return s
for equation in re.findall(r'\$([^$\n]+)\$',s):
 if '='not in equation:continue
 lhs,rhs=equation.rsplit('=',1);lhs=lhs.split('=')[-1]
 if not re.fullmatch(r'\d+',rhs):continue
 if re.search(r'[A-Za-z]',lhs.replace(r'\binom','').replace(r'\cdot','')):continue
 expr=re.sub(r'\\binom\{([^{}]+)\}\{([^{}]+)\}',r'comb(\1,\2)',lhs);expr=re.sub(r'\\binom([0-9])([0-9])',r'comb(\1,\2)',expr)
 expr=expr.replace(r'\cdot','*').replace('^','**').replace('{','(').replace('}',')').replace('−','-');expr=postfix_factorials(expr)
 expr=re.sub(r'(?<=[0-9)])(?=\()', '*',expr);expr=re.sub(r'(?<=\))(?=[0-9]|comb|factorial)','*',expr)
 expr=re.sub(r'(?<=[0-9])(?=comb|factorial)','*',expr)
 tree=ast.parse(expr,mode='eval');allowed=(ast.Expression,ast.BinOp,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.Constant,ast.Call,ast.Name,ast.Load,ast.UnaryOp,ast.USub)
 assert all(isinstance(n,allowed)for n in ast.walk(tree)),expr
 assert all(n.id in['comb','factorial']for n in ast.walk(tree)if isinstance(n,ast.Name))
 value=eval(compile(tree,'<printed equation>','eval'),{'__builtins__':{},'comb':math.comb,'factorial':math.factorial});assert value==int(rhs),(equation,value)
 checked.append(equation)
assert len(checked)>=60,len(checked)
report=dict(status='passed',equationsChecked=len(checked),equations=checked,scope='The final equality in fully numerical inline chains in the 47 answer manuscript; symbolic and display proofs are checked independently.')
(E/'d_functions-printed-numerics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print({'checkedPrintedNumerics':len(checked)})
