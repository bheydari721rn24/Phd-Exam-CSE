"""Independent finite models and symbolic identities, not universal certification."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,itertools,json,math,re,subprocess,tempfile,xml.etree.ElementTree as ET
import sympy as sp
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';BASE='016619372dc5e5930c6a9b0ed9d2e37b6dd04a2f';checks=[]
def check(name,condition):
 assert condition,name;checks.append(dict(name=name,passed=True))
for n in range(1,21):
 atoms=[1,n-1,1,2];check(f'uniform four cells n={n}',sum(atoms)==n+3 and F(sum(atoms[:3]),n+3)==F(n+1,n+3))
 a,b=F(1,n),F(1,n+1);cells=[a*b,a*(1-b),b*(1-a),(1-a)*(1-b)]
 check(f'independent exclusive law n={n}',sum(cells)==1 and sum(cells[1:3])==F(2*n-1,n*(n+1)))
 check(f'disjoint realization n={n}',F(n,n+1)+F(1,n+1)==1)
 prior=F(1,n);joint=[prior*F(2,3),prior*F(1,3),(1-prior)*F(1,3),(1-prior)*F(2,3)]
 check(f'posterior column n={n}',sum(joint)==1 and joint[0]/(joint[0]+joint[2])==F(2,n+1))
 check(f'geometric tail endpoint n={n}',F(1,2**(n-1))-F(1,2**n)==F(1,2**n))
 check(f'normalized ternary tail n={n}',F(1,3**(n-1))-F(1,3**n)==F(2,3**n))
for n in range(2,9):
 p=F(1,n);exact=sum(p**sum(s)*(1-p)**(n-sum(s)) for s in itertools.product([0,1],repeat=n) if sum(s)<=1)
 check(f'at most one exact product patterns n={n}',exact==F((n-1)**(n-1)*(2*n-1),n**n))
for n in range(1,7):
 patterns=list(itertools.product(range(4),repeat=n));check(f'retoss exactly one n={n}',F(sum(s.count(0)==1 for s in patterns),4**n)==F(n*3**(n-1),4**n))
for n in range(1,6):
 states=list(itertools.product([0,1],repeat=n));weights=[F(1,3)**sum(s)*F(2,3)**(n-sum(s)) for s in states];mean=sum(w*sum(s) for s,w in zip(states,weights));second=sum(w*sum(s)**2 for s,w in zip(states,weights))
 check(f'count moment expansion n={n}',sum(weights)==1 and second-mean**2==F(2*n,9))
for a in range(1,11):
 for b in range(1,8):check(f'equal count bijection {a},{b}',sum(math.comb(a,k)*math.comb(b,k) for k in range(min(a,b)+1))==math.comb(a+b,b))
check('authentic unequal toss count',sum(math.comb(25,k)*math.comb(20,k) for k in range(21))==math.comb(45,20))
patterns=list(itertools.product(range(4),repeat=4));check('authentic retoss two',F(sum(s.count(0)==2 for s in patterns),256)==F(27,128))
orders=list(itertools.permutations(range(5)));record_total=sum(sum(x==min(s[:i+1]) for i,x in enumerate(s)) for s in orders)
check('exact five-key record enumeration',record_total==274 and F(record_total,len(orders))==F(137,60))
n=sp.symbols('n',positive=True,integer=True);check('indicator variance symbolic',sp.simplify(n/sp.Integer(3)+n*(n-1)/9-n**2/9-2*n/9)==0)
t=sp.symbols('t');allcells=[t,sp.Rational(3,10)-t,sp.Rational(1,5)-t,sp.Rational(1,10)-t]+[sp.Rational(1,10)+t]*3+[sp.Rational(1,10)-t]
check('three-event atom symbolic normalization',sp.simplify(sum(allcells)-1)==0)
labels=['111','110','101','011','100','010','001','000']
for i,marg in enumerate([sp.Rational(3,5),sp.Rational(1,2),sp.Rational(2,5)]):check(f'three-event marginal {i}',sp.simplify(sum(q for label,q in zip(labels,allcells) if label[i]=='1')-marg)==0)
for a,b,marg in [(0,1,sp.Rational(3,10)),(0,2,sp.Rational(1,5)),(1,2,sp.Rational(1,10))]:check(f'three-event pair {a},{b}',sp.simplify(sum(q for label,q in zip(labels,allcells) if label[a]==label[b]=='1')-marg)==0)
scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes']
for id in ['axioms-question-atoms39','axioms-question-atoms47']:
 for i,f in enumerate(scenes[id]['frames']):
  s=f['snapshot'];masses=list(map(F,s['masses']));check(f'{id} candidate {i}',sum(masses)==1 and s['valid']==all(x>=0 for x in masses))
  expected=[F(3,5),F(1,2),F(2,5)] if id.endswith('39') else [F(1,2)]*3
  check(f'{id} marginals {i}',[sum(q for label,q in zip(labels,masses) if label[j]=='1') for j in range(3)]==expected)
for i,f in enumerate(scenes['axioms-question-urn']['frames']):
 s=f['snapshot'];weights=list(map(F,s['weights']));check(f'conditional urn weights {i}',sum(weights)==(F(9,10) if i==1 else 1) and sum(s['target'])==3 and sum(s['kept'])==9)
 if i>=2:check(f'conditional urn target {i}',sum(w for w,k in zip(weights,s['target']) if k)==F(1,3))
for i,f in enumerate(scenes['axioms-question-report']['frames']):
 s=f['snapshot'];check(f'coarsening fibers {i}',[len(x) for x in s['sequences']]==[1,3,3,1] and len(set(sum(s['sequences'],[])))==8)
draws=list(itertools.product(range(4),repeat=3));cats=[sum(len(set(s))==k for s in draws) for k in [3,2,1]];check('collision exact partition',cats==[24,36,4])
check('collision bound gap',sum(sum(s[a]==s[b] for a,b in [(0,1),(0,2),(1,2)]) for s in draws)==48 and sum(len(set(s))<3 for s in draws)==40)
tree=ast.parse((B/'deep_revision_inventory.py').read_text());ns={};exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
page=(R/'dist/chapters/s_axioms.html').read_text();qs=ns['questions'](page);old=ns['questions'](subprocess.check_output(['git','show',BASE+':dist/chapters/s_axioms.html']).decode());rev=json.loads((E/'s_axioms-revision.json').read_text())
check('preserve 48 placements',len(qs)==len(old)==48)
for record,(_,_,attrs,q),(_,_,oldattrs,oldq) in zip(rev['records'],qs,old):
 check('answer agreement '+str(record['index']),record['answer']==int(attrs['data-answer']))
 if record['index']<=6:check('authentic options preserved '+str(record['index']),re.search(r'<div class="exam-options">[\s\S]*?</div></div>',q)[0]==re.search(r'<div class="exam-options">[\s\S]*?</div></div>',oldq)[0])
for i,formulahtml in enumerate(re.findall(r'<math\b[\s\S]*?</math>',page)):ET.fromstring(formulahtml)
check('all native mathematics XML parse',bool(re.search(r'<math\b',page)))
check('no old abstract answer template','Step 1 — model and conditions.' not in ''.join(q[3] for q in qs))
inventory=json.loads((E/'inventory.json').read_text())
chapters=inventory['chapters'] if isinstance(inventory,dict) else inventory
for c in chapters:
 if c['topicId']=='s_axioms':continue
 path='dist/'+c['url'];before=subprocess.check_output(['git','show',BASE+':'+path]);after=(R/path).read_bytes();check('preserve other chapter '+c['topicId'],before.replace(b'\r\n',b'\n')==after.replace(b'\r\n',b'\n'))
source=json.loads((E/'s_axioms-course-recheck.json').read_text());actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
for q in source['sourcePages']:
 path=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/actual[q['id']]['repoPath'];check('original archive hash '+q['id'],hashlib.sha256(path.read_bytes()).hexdigest()==q['sourceSha256'])
report=dict(topicId='s_axioms',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='Exact finite witnesses and symbolic identities complement analytic arguments; not universal correctness or future-performance certification.')
(E/'s_axioms-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(checks=len(checks),status=report['status'])))
