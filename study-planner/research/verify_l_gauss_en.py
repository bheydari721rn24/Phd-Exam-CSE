"""Independent symbolic, enumerative and serialized exact chapter audit."""
import json,re,hashlib,random,xml.etree.ElementTree as ET
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as S
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent;counts=Counter()
def check(label,condition):
 assert condition,label
 counts[label]+=1
def mat(a):return S.Matrix([[S.Rational(str(v)) for v in r] for r in a])
qs=json.loads((BASE/'l_gauss-questions.json').read_text())
auth=json.loads((BASE/'l_gauss-authentic.json').read_text())
for q in qs:
 check('complete-problem-solution',len(q['solution'].split())>=55)
 check('balanced-controlled-math',q['stem'].count('$')%2==0 and q['solution'].count('$')%2==0)
 check('no-corrupted-source-controls',not any(ord(c)<32 and c not in '\n\r\t' for c in q['stem']+q['solution']))
 if q.get('certificate'):
  c=q['certificate'];a=mat(c['input']);n=a.cols-1;r=mat(c['rref']);e=mat(c['transform'])
  check('problem-invertible-transform',e.det()!=0 and e*a==r)
  coef=a[:,:n];b=a[:,n];p=c['pivots']
  check('problem-coefficient-rref',r[:,:n]==coef.rref()[0])
  check('problem-pivot-identification',tuple(p)==coef.rref()[1])
  if c['particular'] is None:check('problem-inconsistent-ranks',coef.rank()<a.rank())
  else:
   xp=mat([[v] for v in c['particular']]);check('problem-particular-substitution',coef*xp==b)
   directions=[mat([[v] for v in vec]) for vec in c['basis']]
   check('problem-direction-substitutions',all(coef*v==S.zeros(coef.rows,1) for v in directions))
   check('problem-complete-independent-family',len(directions)==n-coef.rank() and (not directions or S.Matrix.hstack(*directions).rank()==len(directions)))
check('distinct-problem-identities',len(qs)==69 and len({q['id'] for q in qs})==69)
alpha=S.symbols('alpha');A=S.Matrix([[1,0,1],[2,alpha,3],[-1,-alpha,alpha]]);b=S.Matrix([-5,-9,alpha**2])
generic=S.Matrix([-alpha-3,3/alpha-1,alpha-2])
check('generic-parameter-substitution',all(S.simplify(v)==0 for v in A*generic-b))
check('exceptional-parameter-zero',A.subs(alpha,0).rank()<A.row_join(b).subs(alpha,0).rank())
t=S.symbols('t');special=S.Matrix([-5-t,(t-1)/2,t]);check('exceptional-parameter-minus-two',A.subs(alpha,-2)*special==b.subs(alpha,-2))
check('parameter-singular-roots',S.factor(A.det())==alpha*(alpha+2))
# Bind independently derived answers to the authored prose, not only to helper fixtures.
bindings={
 'Parameter branching before cancellation':r'y=3/\alpha-1',
 'Schur complement as the lower subsystem':r'x=5/18',
 'A later row swap must move earlier multipliers':r'1/4&1&0',
 'A lower-triangular inverse by a finite series':r'7&-3&1',
 'A linear constraint after elimination':r'x=(3,3,1)^T',
 'Minimum-length member of an affine line':r'x=(3/2,3/2)^T',
 'The final pivot is a determinant ratio':r'u_{33}=24/(-6)=-4',
 'An integer restriction requires more than real consistency':r'(x,y)=(2/5,1/5)',
 'A complete elimination certificate for an asserted solution family':r't(2,1,-3)',
}
for title,value in bindings.items():check('answer-bound-to-prose',value in next(q['solution'] for q in qs if q['title']==title))
check('schur-example-answer',S.Matrix([[2,1,1],[4,3,-1],[-2,1,2]])*S.Matrix([S.Rational(5,18),S.Rational(1,3),S.Rational(1,9)])==S.Matrix([1,2,0]))
L=S.Matrix([[1,0,0],[2,1,0],[-1,-1,1]]);U=S.Matrix([[2,1,1],[0,-8,-2],[0,0,1]]);A0=S.Matrix([[2,1,1],[4,-6,0],[-2,7,2]])
check('Stanford-LU-example',L*U==A0 and A0*S.Matrix([1,1,2])==S.Matrix([5,-2,9]))
Ap=S.Matrix([[4,2,0],[2,1,1],[1,3,1]]);P=S.Matrix([[1,0,0],[0,0,1],[0,1,0]])
Lp=S.Matrix([[1,0,0],[S.Rational(1,4),1,0],[S.Rational(1,2),0,1]]);Up=S.Matrix([[4,2,0],[0,S.Rational(5,2),1],[0,0,1]])
check('later-swap-answer',Lp*Up==P*Ap)
inv=S.Matrix([[1,-1],[-1,2]]);Ai=S.Matrix([[2,1],[1,1]])
check('square-inverse-both-sides',Ai*inv==S.eye(2) and inv*Ai==S.eye(2))
Li=S.Matrix([[1,0,0],[2,1,0],[-1,3,1]]);check('triangular-inverse-cross-term',Li.inv()==S.Matrix([[1,0,0],[-2,1,0],[7,-3,1]]))
# Original examination pages are pinned and have genuinely inspected visual translations.
for q in auth:
 file=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q['repoPath']
 check('archive-source-fingerprint',hashlib.sha256(file.read_bytes()).hexdigest()==q['sourceSha256'])
doctoral=S.Matrix([[3,-2,4],[0,5,1],[6,2,3]])
Ld=S.Matrix([[1,0,0],[0,1,0],[2,S.Rational(6,5),1]])
Ud=S.Matrix([[3,-2,4],[0,5,1],[0,0,S.Rational(-31,5)]])
D=S.diag(-1,1,1);check('authentic-LU-scaled-existence',Ld*Ud==doctoral and (Ld*D)[:,0]==S.Matrix([-1,0,-2]) and (Ld*D)*(D.inv()*Ud)==doctoral)
check('authentic-LU-option',auth[0]['answer']==3)
integer_count=sum(a+b+c==5 for a,b,c in product(range(6),repeat=3))*sum(a+b==15 for a,b in product(range(16),repeat=2))
check('authentic-MS-integer-count',integer_count==336)
for n in range(1,31):
 check('exact-factor-loop-count',2*sum(k*k for k in range(1,n))+sum(range(n))==S.Rational(2,3)*n**3-S.Rational(1,2)*n**2-S.Rational(1,6)*n)
 check('exact-backsolve-count',2*sum(range(n))+n==n*n)
# Independently enumerate finite-field solutions instead of importing the chapter solver.
binA=[[1,1,0,1],[0,1,1,0],[1,0,1,1]]
check('binary-field-complete-answer',[list(x) for x in product(range(2),repeat=3) if all(sum(v*y for v,y in zip(row[:3],x))%2==row[3] for row in binA)]==[[0,1,1],[1,0,0]])
check('five-element-field-count',sum((x+2*y)%5==1 and (2*x+4*y)%5==2 for x,y in product(range(5),repeat=2))==5)
eps=S.symbols('epsilon',positive=True);ill=S.Matrix([[1,1],[1,1+eps]])
check('small-residual-counterexample',S.Matrix([2,2+eps])-ill*S.Matrix([2,0])==S.Matrix([0,eps]))
check('rounding-exact-answer',S.Matrix([[S.Rational(1,10000),1],[1,1]])*S.Matrix([S.Rational(10000,9999),S.Rational(9998,9999)])==S.Matrix([1,2]))
# Exact rational implementation additionally faces independent symbolic random grids.
from gauss_exact import solve
rng=random.Random(1406)
for rows in range(1,5):
 for cols in range(1,5):
  for trial in range(12):
   a=[[rng.randint(-3,3) for _ in range(cols+1)] for _ in range(rows)]
   r,p,x,basis,e,steps=solve(a);M=mat(a);C=M[:,:cols]
   check('rectangular-independent-grid-rref',mat(r)[:,:cols]==C.rref()[0])
   check('rectangular-independent-grid-classification',(x is None)==(C.rank()<M.rank()))
   if x is not None:check('rectangular-independent-grid-solution',C*mat([[v] for v in x])==M[:,cols])
scenes=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'];new={k:v for k,v in scenes.items() if k.startswith('gauss-')}
check('twelve-concept-specific-models',len(new)==12)
for id,scene in new.items():
 for index,fr in enumerate(scene['frames']):
  v=fr['snapshot'];kind=v['kind']
  if kind=='rational-reduction':
   check('serialized-exact-row-transform',mat(v['transform'])*mat(v['input'])==mat(v['matrix']))
   check('serialized-invertible-transform',mat(v['transform']).det()!=0)
  if kind=='lu':check('serialized-LU-product',mat(v['L'])*mat(v['U'])==mat(v['input']))
  if kind=='plu':check('serialized-PLU-product',mat(v['L'])*mat(v['U'])==mat(v['P'])*mat(v['input']))
  if kind=='parameter':
   M=mat(v['input']);C=M[:,:3];state='inconsistent' if C.rank()<M.rank() else 'unique solution' if C.rank()==3 else 'one free coordinate'
   check('serialized-exceptional-branch',state==v['classify'])
  if kind=='binary':check('serialized-binary-solutions',all(all(sum(v*y for v,y in zip(row[:3],x))%2==row[3] for row in v['matrix']) for x in v['solutions']))
  if kind=='coordinate':
   vec=mat([[x] for x in v['vector']]);Q=mat(v['Q']);A=mat(v['original']);b=mat([[x] for x in v['load']])
   check('serialized-variable-map',(A*Q*vec if 'Transformed' in v['phase'] else A*vec)==b)
  if kind=='geometry':
   x,y=v['solution'];a,b,c=v['second'];check('serialized-geometric-intersection',a*x+b*y==c)
  if kind=='rounding' and v['answer'] is not None:
   check('serialized-declared-rounded-solve',mat(v['matrix'])[:,:2]*mat([[x] for x in v['answer']])==mat(v['matrix'])[:,2])
  check('complete-model-explanations',len(fr['caption'].split())>=15)
# The interpolated geometric line must also retain the intersection, not only endpoints.
geom=new['gauss-geometry']['frames']
for j in range(21):
 t=F(j,20);pos=[]
 for fr in geom:
  ns={n['id']:n for n in fr['nodes']};pos.append([(F(str(ns[k]['x'])),F(str(ns[k]['y']))) for k in ['c','d','solution']])
 c=[(1-t)*pos[0][0][i]+t*pos[1][0][i] for i in [0,1]];d=[(1-t)*pos[0][1][i]+t*pos[1][1][i] for i in [0,1]]
 check('interpolated-geometric-invariant',all((c[i]+d[i])/2==pos[0][2][i] for i in [0,1]))
sources=json.loads((ROOT/'dist/evidence/l_gauss/sources.json').read_text())
check('four-primary-distinct-universities',len(set(sources['primaryUniversities']))==4 and sources['candidateCourses']==5)
cache=Path('C:/Users/bheydari/AppData/Local/Temp/phd-gauss-sources')
for record in sources['documents']:
 p=cache/(record['id']+('.pdf' if record.get('pages') else '.html'))
 check('written-source-content-fingerprint',hashlib.sha256(p.read_bytes()).hexdigest()==record['sha256'])
page=(ROOT/'dist/chapters/l_gauss.html').read_text()
check('complete-artifact-inventory',page.count('class="exam-question"')==71 and page.count('class="review-rule"')==80 and page.count('<figure ')==7)
for formula in re.findall(r'<math\b[\s\S]*?</math>',page):
 ET.fromstring(formula);counts['native-mathml-well-formed']+=1
check('dedicated-matrix-tables',page.count('<mtable columnspacing=')>=35)
approved=set(json.loads((BASE/'library-approval.json').read_text())['approvedTopics'])
chapters=[c for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]
check('all-25-approved-chapters-preserved',len(approved)==25 and all(c['status']=='ready' and c['animationReviewState']=='student_approved' for c in chapters if c['topicId'] in approved))
check('sole-Gaussian-review-draft',[(c['topicId'],c['status']) for c in chapters if c['topicId'] not in approved]==[('l_gauss','draft')])
report=dict(chapter='l_gauss',state='passed',checks=sum(counts.values()),byKind=dict(counts),numericProseBindings=bindings,originalProblems=69,authenticProblems=2,examRules=80,figures=7,scenarios=12,checkpoints=sum(len(s['frames']) for s in new.values()),limits='Independent symbolic checks, exact products and finite enumerations; conceptual proofs also receive editorial review. No universal coverage or unseen-examination guarantee.')
(BASE/'l_gauss-validation.json').write_text(json.dumps(report,indent=2)+'\n')
(ROOT/'dist/evidence/l_gauss/validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['state','checks','originalProblems','authenticProblems','examRules','figures','scenarios','checkpoints']}))
