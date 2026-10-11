from pathlib import Path
import sys,re,ast
B=Path(__file__).resolve().parent;R=B.parent
source=(B/'deep_revision_inventory.py').read_text();ns={}
tree=ast.parse(source)
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'inventory helpers','exec'),ns)
topic=sys.argv[1];s=(R/'dist/chapters'/ (topic+'.html')).read_text(encoding='utf-8');qs=ns['questions'](s)
if '--options' in sys.argv:
 for n,(a,b,attrs,q)in enumerate(qs,1):
  part=q[q.find('<div class="exam-options">'):q.find('<details')]
  print(str(n)+': '+ns['plain'](part))
 sys.exit()
if len(sys.argv)>2:
 lo=int(sys.argv[2]);hi=int(sys.argv[3])
 for n,(a,b,attrs,q)in enumerate(qs,1):
  if lo<=n<=hi:
   q=re.split(r'<(?:section|div)\b[^>]*class="[^"]*(?:problem-visual|solution-visual|concept-model|question-concept-aid)',q)[0]
   print(ns['plain'](q)+'\n')
else:
 print(s[qs[0][0]:qs[0][0]+5000]);print((B/'d_logic-en-quality-audit.md').read_text()[:6700]);print([p.name for p in (R/'dist').glob('*.js')])
