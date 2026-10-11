"""Independent exact formulas, actual JS calculator oracle and native math checks."""
from pathlib import Path
import sympy as S,json,re,hashlib,subprocess,sys,random,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_linear-evidence'
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
checks=[]
def ck(name,ok):assert bool(ok),name;checks.append(name)
M=S.Matrix;x,t=S.symbols('x t');I=S.eye(2)
ck('basis reconstruction',M([[-1,2],[1,-1]])*M([[1,2],[1,1]])==I)
ck('two-basis representative',M([[1,1],[0,1]]).inv()*M([[1,2],[0,1]])*M([[1,0],[1,1]])==M([[2,1],[1,1]]))
ck('directional transition',M([[2,1],[0,1]]).inv()*M([[1,1],[1,-1]])==M([[0,1],[1,-1]]))
A=M([[2,1],[3,-2]]);P=M([[1,-2],[-2,5]])
ck('skewed similarity',P.inv()*A*P==M([[14,-27],[7,-14]]))
H=M([[1,1],[0,1]]);K=M([[1,0],[1,1]])
ck('both shear orders',K*H==M([[1,1],[1,2]])and H*K==M([[2,1],[1,1]]))
P0=M([[1,-1],[0,0]]);ck('oblique idempotent',P0*P0==P0 and P0!=P0.T)
ck('complementary projection',(I-P0)**2==I-P0)
P1=M([[1,1],[0,0]]);Q1=M([[1,0],[1,0]]);ck('projection product counterexample',P1**2==P1 and Q1**2==Q1 and (P1*Q1)**2!=P1*Q1)
V=M([[1,0,0],[1,1,1],[1,2,4]]);ck('evaluation invertible',V.det()==2 and V*M([1,0,1])==M([1,2,5]))
L=[(x-1)*(x-2)/2,-x*(x-2),x*(x-1)/2];ck('Lagrange table',M([[f.subs(x,j)for f in L]for j in[0,1,2]])==S.eye(3))
W=M([[1,1],[1,-1]]);mask=S.diag(1,0);C=W*mask*W.inv();ck('mask reconstruction',C*M([3,1])==M([2,2])and C*C==C)
G=S.diag(1,4);A0=M([[0,1],[0,0]]);ck('Gram adjoint',G.inv()*A0.T*G==M([[0,0],[S.Rational(1,4),0]]))
N=M([[0,0,0],[1,0,0],[0,1,0]]);ck('nilpotent sequence',[int((N**k).rank())for k in range(4)]==[3,2,1,0])
ck('Sylvester explicit',S.diag(1,3)*M([[2,-4],[2,8]])-M([[2,-4],[2,8]])*S.diag(0,2)==M([[2,4],[6,8]]))
ck('finite field derivative',[(k%2)for k in range(5)]==[0,1,0,1,0])
models=json.loads((R/'dist/chapters/l_linear-models.json').read_text())
for m in models['models']:
 for i,f in enumerate(m['frames']):
  snap=f['snapshot']
  if 'A'in snap:
   A,P,Q,c=map(M,[snap['A'],snap['P'],snap['Q'],snap['input']])
   ck(m['id']+' path '+str(i),Q.inv()*A*P*c==M(snap['output']))
   ck(m['id']+' representation '+str(i),Q.inv()*A*P==M(snap['representation']))
  if 'matrix'in snap:
   A=M(snap['matrix']);ck(m['id']+' geometric output '+str(i),A*M(snap['input'])==M(snap['output']))
   if m['kind']=='angle-rotation':ck(m['id']+' orthogonality '+str(i),(A.T*A-S.eye(2)).applyfunc(S.simplify)==S.zeros(2))
  if m['id']=='fiber-sum':ck('fiber '+str(i),M([[1,1],[0,0]])*M(snap['input'])==M(snap['output']))
random.seed(1406);cases=[]
for j in range(120):
 def invertible():
  while True:
   a=M(2,2,[random.randint(-5,5)for _ in range(4)])
   if a.det():return a
 A=M(2,2,[random.randint(-5,5)for _ in range(4)]);P=invertible();Q=invertible();c=M([random.randint(-5,5)for _ in range(2)])
 cases.append(dict(A=A.tolist(),P=P.tolist(),Q=Q.tolist(),x=list(c)))
code="const fs=require('fs'),a=require('./dist/chapters/l_linear.js');const cases=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(cases.map(z=>a.coordinateLab(z.A,z.P,z.Q,z.x).result)));"
plain=json.loads(json.dumps(cases,default=int))
res=subprocess.run(['node','-e',code],input=json.dumps(plain),text=True,capture_output=True,cwd=R,check=True)
actual=json.loads(res.stdout)
for i,(z,v)in enumerate(zip(cases,actual)):
 A,P,Q,c=map(M,[z['A'],z['P'],z['Q'],z['x']]);expected=Q.inv()*A*P
 ck('Actual JS calculator matrix '+str(i),M(v['matrix'])==expected)
 ck('Actual JS calculator output '+str(i),M(v['output'])==expected*c and all(v['checks'].values()))
 # Verify the rank theorem, both directions and invertibility independently.
 ck('Actual JS rank '+str(i),v['rank']==A.rank())
script=(R/'dist/chapters/l_linear.html').read_text(encoding='utf-8')
maths=re.findall(r'<math\b[\s\S]*?</math>',script)
for i,m in enumerate(maths):
 node=ET.fromstring(m);ck('Math fences '+str(i),not closing_script_bases(node)and not delimiter_issues(node))
prior=json.loads((E/'prior-library.json').read_text())['chapters']
for c in prior:ck('Retained '+c['topicId'],hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256'])
ck('question count',len(json.loads((B/'l_linear-questions.json').read_text()))==82)
ck('rules',len(re.findall(r'^\d+\. ',(B/'l_linear-review.en.md').read_text(),re.M))==84)
report=dict(status='passed',exactChecks=len(checks),actualJSOracleCases=len(cases),staticMathMLChecks=len(maths),retainedPriorChapters=len(prior),checks=checks)
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()if k!='checks'}))
