"""Independently evaluate the printed numerical substitution equations."""
from pathlib import Path
import re,math,json,ast
B=Path(__file__).parent; E=B/'deep-library-revision'; s=(E/'d_relations-solutions.md').read_text()
checked=[]
for equation in re.findall(r'\$([^$\n]+)\$',s):
 if '=' not in equation: continue
 lhs,rhs=equation.rsplit('=',1)
 lhs=lhs.split('=')[-1]
 if not re.fullmatch(r'\d+',rhs): continue
 if re.search(r'[A-Za-z]',lhs.replace(r'\binom','').replace(r'\cdot','')): continue
 expression=re.sub(r'\\binom\{\(?([0-9]+)\)?\}\{([0-9]+)\}',r'comb(\1,\2)',lhs)
 expression=re.sub(r'\\binom([0-9])([0-9])',r'comb(\1,\2)',expression)
 expression=expression.replace(r'\cdot','*').replace('^','**').replace('{','(').replace('}',')')
 expression=re.sub(r'(?<=[0-9)])(?=\()', '*',expression)
 expression=re.sub(r'(?<=\))(?=[0-9])', '*',expression)
 tree=ast.parse(expression,mode='eval')
 assert all(isinstance(n,(ast.Expression,ast.BinOp,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.Constant,ast.Call,ast.Name,ast.Load)) for n in ast.walk(tree)),expression
 assert all(n.id=='comb' for n in ast.walk(tree) if isinstance(n,ast.Name))
 actual=eval(compile(tree,'<printed numerical equation>','eval'),{'__builtins__':{},'comb':math.comb})
 assert actual==int(rhs),(equation,actual)
 checked.append(equation)
assert len(checked)>=60,len(checked)
report=dict(status='passed',equationsChecked=len(checked),equations=checked,scope='Printed fully numerical equalities in the 45 rewritten solutions; symbolic theorems are checked separately.')
(E/'d_relations-printed-numerics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print({'printedNumericEqualitiesChecked':len(checked)})
