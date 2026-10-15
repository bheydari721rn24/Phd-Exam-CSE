"""Independent exact calculations, bounded operator cases and rendered formula checks."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,xml.etree.ElementTree as ET
import sympy as s
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'l_projection-evidence';checks=[]
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
M=s.Matrix;F=s.Rational;I=s.eye
def ck(label,value):
 assert bool(value),label
 checks.append(label)
 if len(checks)%100==0:print('Verified',len(checks),label,flush=True)
def P(C,G=None):
 G=I(C.rows)if G is None else G
 return C*(C.T*G*C).inv()*C.T*G
def energy(x,G=None):return s.simplify((x.T*(I(x.rows)if G is None else G)*x)[0])
# The first ten already have an independent dedicated exact bank oracle.
subprocess.run([sys.executable,str(B/'verify_projection_worked_bank.py')],cwd=R,check=True,capture_output=True)
b=M([1,1,1]);p=M([1,0,0]);ck('Q11 incomplete certificate',p.dot(b-p)==0 and M([0,1,0]).dot(b-p)==1 and energy(b-p)==2)
n=M([1,2,2]);A=I(3)-n*n.T/9;b=M([3,0,0]);ck('Q12 kernel projection',A*b==M([F(8,3),-F(2,3),-F(2,3)])and energy(b-A*b)==1)
v=M([2,1,2]);w=M([-2,2,1]);b=M([4,8,1]);p=2*v+w;ck('Q13 unnormalized basis',v.dot(w)==0 and p==M([2,4,5])and energy(b-p)==36 and energy(p)==45)
P0=M([[F(1,2),F(1,2),0],[F(1,2),F(1,2),0],[0,0,0]]);P1=P0+s.diag(0,0,1);ck('Q14 two realizations',P0*P0==P0 and P1*P1==P1 and P0.rank()==1 and P1.rank()==2)
u=M([0,2,2]);old=s.diag(1,0,0);new=old+u*u.T/8;ck('Q15 rank update',new==M([[1,0,0],[0,F(1,2),F(1,2)],[0,F(1,2),F(1,2)]])and new*new==new)
B0=M([[1,1],[0,1]]);C=s.diag(1,0);EE=B0.inv()*C*B0;G=B0.T*B0;ck('Q16 metric coordinates',EE==M([[1,1],[0,0]])and EE.T*G==G*EE and EE*M([-1,1])==s.zeros(2,1))
H=M([[0,-1],[-1,0]]);ck('Q17 reflection',H*H==I(2)and H.det()==-1 and H*M([3,0])==M([0,-3]))
ck('Q18 integer cycle count',F(1,4)**4>F(1,1000)and F(1,4)**5<=F(1,1000))
c,t=s.symbols('c t',real=True);A=s.diag(1,0);Q=M([[c*c,c*t],[c*t,t*t]]);K=A*Q-Q*A;ck('Q19 commutator',K==M([[0,c*t],[-c*t,0]])and sum(a*a for a in K)==2*c*c*t*t)
A=s.diag(1,1,0);Q=P(M([[1,0],[0,1],[0,1]]));ck('Q20 plane overlap',s.trace(A*Q)==F(3,2)and sum(x*x for x in A-Q)==1 and M.hstack(*A.columnspace(),*Q.columnspace()).rank()==3)
a,b=s.symbols('a b');A=M([[1,2],[0,0]]);inv=(I(2)-A)/a+A/(a+b);ck('Q21 polynomial inverse',A**7-3*A*A+2*I(2)==2*(I(2)-A)and(inv*(a*I(2)+b*A)-I(2)).applyfunc(s.simplify)==s.zeros(2))
A=s.diag(1,1,1,0,0);ck('Q22 shifted determinants',(I(5)+2*A).det()==27 and(2*I(5)-A).det()==4)
D=M([[1,1,0],[0,1,1]]);d=M([1,2]);b=M([1,0,0]);p=b-D.T*(D*D.T).inv()*(D*b-d);ck('Q23 affine correction',p==M([F(1,3),F(2,3),F(4,3)])and D*p==d and energy(b-p)==F(8,3))
D=M([[1,1],[2,2]]);ck('Q24 constraint consistency',D.rank()==D.row_join(M([1,2])).rank()==1 and D.row_join(M([1,3])).rank()==2)
p=M([F(4,5),F(1,5)]);G=s.diag(1,4);ck('Q25 weighted affine',energy(p,G)==F(4,5)and(M([[1,1]])*p)[0]==1 and(M([1,-1]).T*G*p)[0]==0)
ck('Q26 null cost direction',energy(M([0,7]),s.diag(1,0))==0 and energy(M([1,7]),s.diag(1,0))==1)
a=s.symbols('a',real=True);A=M([[1,a],[0,0]]);G=M([[1,a],[a,a*a+1]]);ck('Q27 oblique metric',G.det()==1 and A.T*G==G*A)
for sign in[-1,1]:
 A=M([[F(1,4),sign*s.sqrt(3)/4],[sign*s.sqrt(3)/4,F(3,4)]]);ck('Q28 sharp entry '+str(sign),A*A==A and A.rank()==1)
A=M([[1,-1],[1,1],[1,2]]);b=M([7,7,21]);coef=(A.T*A).inv()*A.T*b;p=A*coef;r=b-p;ck('Q29 fitted coefficients',coef==M([9,4])and p==M([5,13,17]));ck('Q30 error and repeat',r==M([2,-6,4])and A.T*r==s.zeros(2,1)and energy(r)==56 and P(A)*p==p and P(A)*r==s.zeros(3,1))
A=M([[1,1]]);ck('Q31 nonminimum rowspace',A*M([1,0])==M([1])and M([[1,1],[1,0]]).det()!=0 and A.pinv()*M([1])==M([F(1,2),F(1,2)]))
A=M([[1,-2],[1,-1],[1,0],[1,1],[1,2]]);b=M([4,2,-1,0,0]);coef=(A.T*A).inv()*A.T*b;p=A*coef;ck('Q32 symmetric times',coef==M([1,-1])and p==M([3,2,1,0,-1])and energy(b-p)==6)
Q=M.hstack(M([1,1,0])/s.sqrt(2),M([1,-1,2])/s.sqrt(6));b=M([0,0,1]);p=Q*Q.T*b;ck('Q33 QR complement',p==M([F(1,3),-F(1,3),F(2,3)])and energy(b-p)==F(1,3))
t=s.symbols('t',real=True);ck('Q34 polynomial error',s.integrate((t*t-F(1,3))**2,(t,-1,1))==F(8,45))
u=M([1,s.I]);G=s.diag(2,1);b=M([1,1]);A=u*(u.H*G*u).inv()*u.H*G;p=A*b;r=b-p;ck('Q35 weighted complex',p==M([(2-s.I)/3,(1+2*s.I)/3])and s.simplify((r.H*G*r)[0])==F(4,3)and A.H*G==G*A)
ck('Q36 endpoint distances',energy((I(3)-s.diag(1,1,0))*M([0,0,1]))==1)
A=s.ones(2)/2;ck('Q37 mixed distance',energy((I(2)-A)*M([1,1]))==0 and A[0,1]==F(1,2))
b=M([3,4]);x=M([1,4]);ck('Q38 penalty minimum',energy(x-b)+2*energy(s.diag(1,0)*x)==6)
ck('Q39 nonunique finite nearest points',energy(M([-1,0]))==energy(M([1,0]))==1)
A=s.diag(1,0);Q=s.ones(2)/2;N=A+Q-A*Q;ck('Q40 false sum formula',N==M([[1,0],[F(1,2),F(1,2)]])and N*N!=N)
A=M([[1,1],[0,0]]);b=M([0,1]);ck('Q41 single-vector energy fails',energy(A*b)+energy((I(2)-A)*b)==3)
Q=M([[1,0],[1,0]]);A=s.diag(1,0);ck('Q42 oblique trace counterexample',s.trace(A*Q)==1 and A.columnspace()!=Q.columnspace())
A=s.diag(1,1,0,0,0,0);Q=s.diag(1,1,1,1,0,0);ck('Q43 nested difference',(Q-A)**2==Q-A and(Q-A).rank()==2 and s.trace(A-Q)==-2)
t=s.symbols('t',nonzero=True);A=M([[1,1],[0,t]]);ck('Q44 changing rank',s.simplify(A*P(I(2))-A)==s.zeros(2)and A.inv()*M([0,1])==M([-1/t,1/t]))
ck('Q45 Bessel feasibility',25-(4+9+1)==11 and 16+9+4>25)
u=M([1,0]);v=M([F(3,5),F(4,5)]);A=u*u.T;Q=v*v.T;ck('Q46 rank-one distance',sum(z*z for z in A-Q)==2*(1-u.dot(v)**2))
for m in range(1,9):
 u=s.ones(m,1);b=M(list(range(1,m+1)));A=u*u.T/m;p=A*b;ck('Q47 centered exact '+str(m),energy(b-p)==F(m*(m*m-1),12));ck('Q48 centering idempotent '+str(m),(I(m)-A)**2==I(m)-A and(I(m)-A).rank()==m-1)
A=M([[1,0],[1,1],[0,1]]);b=M([0,0,1]);p=P(A)*b;ck('Q49 original basis',p==M([-F(1,3),F(1,3),F(2,3)])and energy(b-p)==F(1,3))
G=M([[2,1],[1,2]]);u=M([1,-1]);b=M([2,0]);A=P(u,G);p=A*b;r=b-p;ck('Q50 metric synthesis',p==u and r==M([1,1])and energy(p,G)==2 and energy(r,G)==6)
# Independent exact projector identities on a bounded rational collection.
vectors=[M([i,j])for i in range(-2,3)for j in range(-2,3)if(i,j)!=(0,0)]
for i,u in enumerate(vectors):
 A=P(u)
 for j,v in enumerate(vectors):
  Q=P(v);ck('bounded trace and metric '+str(i)+'-'+str(j),s.trace(A*Q)==sum(z*z for z in A*Q)and sum(z*z for z in A-Q)==2-2*s.trace(A*Q))
page=(R/'dist/chapters/l_projection.html').read_text(encoding='utf8');maths=re.findall(r'<math\b[\s\S]*?</math>',page)
for i,m in enumerate(maths):
 root=ET.fromstring(m);ck('native formula fences '+str(i),not delimiter_issues(root)and not closing_script_bases(root))
ck('bank and final decisions',page.count('class="exam-question"')==52 and page.count('class="review-rule"')==50)
ck('no unfinished markup',not re.search(r'\$|MATHSLOT|<!--[\s\S]*?-->',page))
specs=[json.loads(__import__('html').unescape(v))for v in re.findall(r'data-pr-spec="([^"]+)"',page)]
code="const p=require('./dist/chapters/l_projection.js'),z=JSON.parse(require('fs').readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(z.map(s=>p.frames(s))));"
out=json.loads(subprocess.run(['node','-e',code],input=json.dumps(specs),text=True,capture_output=True,cwd=R,check=True).stdout)
for i,frames in enumerate(out):
 for j,f in enumerate(frames):ck('actual JS finite model '+str(i)+'-'+str(j),f['certificate'])
report={'status':'passed_exact_mathematical_and_document_checks','originalOrReconstructedProblems':50,'authenticRevisits':2,'finalDecisions':50,'nativeMathExpressions':len(maths),'modelPlacements':len(specs),'finiteCheckpoints':sum(map(len,out)),'checks':checks,'normalizedTextSha256':hashlib.sha256(page.encode()).hexdigest(),'documentSha256':hashlib.sha256((R/'dist/chapters/l_projection.html').read_bytes()).hexdigest(),'limitations':'Exact checks cover explicit examples and bounded rational cases; proofs were separately reasoned through. No claim of exhaustive worldwide course review or perfect unseen-examination performance.'}
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print({k:v for k,v in report.items()if k!='checks'}|{'assertions':len(checks)})
