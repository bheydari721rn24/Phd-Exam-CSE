"""Independent exact and symbolic audit of the rank chapter."""
import json,re,hashlib,random,subprocess,xml.etree.ElementTree as ET
from collections import Counter
from itertools import product
from pathlib import Path
import sympy as S
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent;counts=Counter()
def check(label,c):
 assert c,label
 counts[label]+=1
def mat(a):return S.Matrix([[S.sympify(str(v)) for v in row] for row in a])
qs=json.loads((BASE/'l_rank-questions.json').read_text());auth=json.loads((BASE/'l_rank-authentic.json').read_text())
check('unique-complete-question-bank',len(qs)==88 and len({q['id'] for q in qs})==88 and len(auth)==2)
for q in qs:
 check('complete-english-solution',len(q['solution'].split())>=42 and len(q['stem'].split())>=8)
 check('controlled-source-text',not any(ord(c)<32 and c not in '\n\r\t' for c in q['stem']+q['solution']))
 check('balanced-math-delimiters',q['stem'].count('$')%2==0 and q['solution'].count('$')%2==0)
 c=q.get('certificate')
 if c:
  A=mat(c['input']);R,p=A.rref();r=A.rank()
  check('independent-reduction',R==mat(c['rref']) and p==tuple(c['pivots']) and r==c['rank'])
  for key,M,expected in [('null',A,A.cols-r),('left',A.T,A.rows-r)]:
   vs=[mat([[x] for x in v]) for v in c[key]]
   check('annihilated-directions',all(M*v==S.zeros(M.rows,1) for v in vs))
   check('complete-independent-space',len(vs)==expected and (not vs or S.Matrix.hstack(*vs).rank()==expected))
  C=A[:,list(p)] if p else S.zeros(A.rows,0)
  check('original-column-basis',C.rank()==r and C.row_join(A).rank()==r)

# Parameter families and explicit exceptional branches.
s,t,d,c=S.symbols('s t d c')
family=S.Matrix([[1,1,1],[1,1+s,1],[1,1,1+t]])
check('two-parameter-minor',S.expand(family.det())==s*t)
for ss,tt in product([-2,0,3],repeat=2):
 check('all-parameter-strata',family.subs({s:ss,t:tt}).rank()==1+(ss!=0)+(tt!=0))
load=S.Matrix(S.symbols('b1:4'));T=S.Matrix([[1,0,0],[-1,1,0],[-1,0,1]])
check('load-transform',T*family==S.Matrix([[1,1,1],[0,s,0],[0,0,t]]))
schur=S.Matrix([[2,1,3],[0,1,1],[2,2,t]])
check('schur-determinant',S.expand(schur.det())==2*(t-4))
for v in [-1,0,4,7]:check('schur-branch',schur.subs(t,v).rank()==(2 if v==4 else 3))
for n in [2,3,4,5]:
 for dd,cc in product([-2,-1,0,1,2],repeat=2):
  M=(dd-cc)*S.eye(n)+cc*S.ones(n)
  check('constant-off-diagonal-strata',M.rank()==int(dd+(n-1)*cc!=0)+(n-1)*int(dd-cc!=0))
check('complex-transpose-counterexample',(S.Matrix([1,S.I]).T*S.Matrix([1,S.I]))==S.zeros(1))
check('hermitian-gram',S.Matrix([1,S.I]).conjugate().T*S.Matrix([1,S.I])==S.Matrix([2]))
L0=S.Matrix([[1,0,0],[0,1,0]]);At=S.Matrix([[1,0],[0,1],[1,1]])
check('left-inverse-family',(L0+S.Matrix([[-s,-s,s],[-t,-t,t]]))*At==S.eye(2))
Aw=S.Matrix([[1,0,1],[0,1,1]]);R0=S.Matrix([[1,0],[0,1],[0,0]])
check('right-inverse-family',Aw*(R0+S.Matrix([-1,-1,1])*S.Matrix([[s,t]]))==S.eye(2))
P=S.Matrix([[1,2],[0,0]])
check('oblique-projection',P*P==P and P.rank()==S.trace(P)==1 and P!=P.T)
update=S.eye(3)+S.Matrix([1,2,0])*S.Matrix([[-1,0,0]])
check('update-exception',update.rank()==2 and update*S.Matrix([1,2,0])==S.zeros(3,1))
check('update-regular',(S.eye(3)+S.Matrix([1,2,0])*S.Matrix([[1,0,0]])).rank()==3)
ox=S.Matrix([[1,2,-1,0],[2,1,0,3],[0,1,1,1]])
check('oxford-membership-certificate',ox*S.Matrix([8,-1,6,-5])==S.zeros(3,1) and ox.rank()==3)

# Independent rectangular random tests close shape and empty-kernel risks.
random.seed(1406)
for _ in range(50):
 m,n,p=[random.randint(1,5) for _ in range(3)]
 A=S.Matrix(m,n,lambda i,j:random.randint(-2,2));B=S.Matrix(n,p,lambda i,j:random.randint(-2,2))
 ra,rb,rab=A.rank(),B.rank(),(A*B).rank()
 check('sylvester-and-upper',max(0,ra+rb-n)<=rab<=min(ra,rb))
 U=S.Matrix.hstack(*B.columnspace()) if rb else S.zeros(n,0)
 K=S.Matrix.hstack(*A.nullspace()) if n-ra else S.zeros(n,0)
 intersection=rb+n-ra-U.row_join(K).rank()
 check('restriction-formula',rab==rb-intersection)
 C=S.Matrix(m,n,lambda i,j:random.randint(-2,2))
 check('sum-inequalities',abs(ra-C.rank())<=(A+C).rank()<=ra+C.rank())
 check('gram-rank',(A.T*A).rank()==ra)
 check('four-space-dimensions',len(A.nullspace())==n-ra and len(A.T.nullspace())==m-ra)
 M=S.Matrix.hstack(*A.columnspace()) if ra else S.zeros(m,0)
 N=S.Matrix.hstack(*C.columnspace()) if C.rank() else S.zeros(m,0)
 intersection2=ra+C.rank()-M.row_join(N).rank()
 check('sum-intersection-dimension',0<=intersection2<=min(ra,C.rank()))

# Enumerate a finite field independently instead of calling rational RREF.
for a,b,c,d in product(range(2),repeat=4):
 arr=[[a,b],[c,d]]
 image={tuple(sum(row[j]*x[j] for j in range(2))%2 for row in arr) for x in product(range(2),repeat=2)}
 null=[x for x in product(range(2),repeat=2) if all(sum(row[j]*x[j] for j in range(2))%2==0 for row in arr)]
 check('finite-field-dimension-count',len(image)*len(null)==4)
 for bvec in product(range(2),repeat=2):
  solutions=[x for x in product(range(2),repeat=2) if tuple(sum(row[j]*x[j] for j in range(2))%2 for row in arr)==bvec]
  check('finite-field-fiber-count',len(solutions) in (0,len(null)))

data=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes']
for id,scene in data.items():
 if not id.startswith('rank-'):continue
 for f in scene['frames']:
  q=f['snapshot'];kind=q['kind']
  if kind=='rank-reduction':
   check('animated-exact-transform',mat(q['transform'])*mat(q['input'])==mat(q['matrix']) and mat(q['transform']).det()!=0)
  if kind=='column-transform':
   check('animated-image-transform',mat(q['E'])*mat(q['A'])==mat([[v] for v in q['v']]) and mat(q['E']).det()!=0)
  if kind=='fiber':check('animated-fixed-fiber',mat(q['A'])*S.Matrix(q['x'])==S.Matrix(q['b']))
  if kind in ('fiber','projection'):
   pos=next(n for n in f['nodes'] if n['id']=='input')
   x=list(map(S.Rational,q['x']))
   check('moving-point-coordinate-binding',abs(pos['x']-float(180+55*x[0]))<1e-9 and abs(pos['y']-float(190-45*x[1]))<1e-9)
  if kind=='rank-map':
   M=mat(q['matrix']);X=mat(q['inputs']).T;Y=mat(q['outputs']).T
   check('animated-actual-map',M*X==Y)
   check('animated-rank-count',M.rank()==f['metrics'].get('Rank',f['metrics'].get('Sum rank')))
  if kind=='composition':
   A,B=mat(q['A']),mat(q['B']);check('animated-composition',A*B==mat(q['AB']) and (A*B).rank()==f['metrics']['Rank A B'])
  if kind=='parameter-rank':check('animated-parameter-branch',mat(q['matrix']).rank()==q['rank'])
  if kind=='factorization':check('animated-factor-values',mat(q['F'])*S.Matrix(q['x'])==S.Matrix(q['z']) and mat(q['C'])*S.Matrix(q['z'])==S.Matrix(q['y']))
  if kind=='projection':check('animated-projection-fiber',mat(q['P'])*mat([[x] for x in q['x']])==S.Matrix(q['y']))
  if kind=='witness':check('animated-compatibility-witness',S.Matrix([q['y']])*mat(q['A'])==S.zeros(1,2) and (S.Matrix([q['y']])*S.Matrix(q['b']))[0]==q['value'])
  if kind=='power-rank':check('animated-power',mat(q['A'])**q['power']==mat(q['result']) and mat(q['result']).rank()==f['metrics']['Rank'])

page=(ROOT/'dist/chapters/l_rank.html').read_text()
check('question-rule-figure-counts',page.count('class="exam-question"')==90 and page.count('class="review-rule"')==80 and page.count('<figure class="logic-diagram rank-diagram"')==7)
for m in re.findall(r'<math\b[\s\S]*?</math>',page):check('well-formed-native-math',ET.fromstring(m).tag.endswith('math'))
check('no-raw-tex-or-persian',not re.search(r'[\u0600-\u06ff]|\$\$|\\begin\{',re.sub(r'aria-label="[^"]*"','',page)))
approved=json.loads((BASE/'library-approval.json').read_text())['approvedTopics']
check('preserved-approval-bank',len(approved)==26 and sum((ROOT/f'dist/chapters/{id}.html').read_text().count('class="exam-question"') for id in approved)==1317)
for id in approved:
 old=subprocess.check_output(['git','show','f616b10ec71352ae6dd390d0f4b7e103c557cf9c:dist/chapters/'+id+'.html'],cwd=ROOT).decode()
 new=(ROOT/f'dist/chapters/{id}.html').read_text()
 pattern=r'<section class="exam-question"[\s\S]*?</section>'
 check('unchanged-approved-question-content',re.findall(pattern,old)==re.findall(pattern,new))
for u in range(21):
 t=S.Rational(u,20)
 E=S.Matrix([[1-t,-t],[t,1-t]])
 check('interpolated-output-transform-invertible',E.det()>0)
 x=S.Matrix([1+2*t,1-t])
 check('interpolated-oblique-fiber',P*x==S.Matrix([3,0]))
 x=S.Matrix([4-t,-1+t])
 check('interpolated-solution-fiber',sum(x)==3)
for q in auth:
 path=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q['repoPath']
 check('authentic-archive-fingerprint',hashlib.sha256(path.read_bytes()).hexdigest()==q['sourceSHA'])
result=dict(state='passed',chapter='l_rank',checks=sum(counts.values()),groups=dict(counts),limits='Exact and finite checked inputs plus explicit mathematical proofs; not universal unseen-score or worldwide-course guarantees.')
(BASE/'l_rank-validation.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'dist/evidence/l_rank/validation.json').write_text(json.dumps(result,indent=2)+'\n')
print('Passed',result['checks'],'independent rank chapter checks.')
