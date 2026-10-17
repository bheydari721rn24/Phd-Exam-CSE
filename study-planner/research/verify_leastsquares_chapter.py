"""Independent exact matrix models, counterexamples and current-page mathematics."""
from pathlib import Path
from itertools import product
import json,re,sys,hashlib,xml.etree.ElementTree as ET
import sympy as S
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'l_leastsquares-evidence';E.mkdir(exist_ok=True)
q={x['id']:x for x in json.loads((B/'l_leastsquares-questions.json').read_text(encoding='utf8'))};checks=[]
def ck(name,ok):
 assert bool(ok),name
 checks.append(name)
def equal(a,b):return S.simplify(a-b)==S.zeros(*a.shape)if isinstance(a,S.MatrixBase)else S.simplify(a-b)==0
def fit(A,b,W=None):
 W=S.eye(A.rows)if W is None else W
 x=(A.T*W*A).inv()*A.T*W*b;r=b-A*x
 ck('normal product',equal(A.T*W*r,S.zeros(A.cols,1)))
 return S.simplify(x),S.simplify(r),S.simplify((r.T*W*r)[0])
def matrix_stem(id):
 s=re.search(r'\\begin\{bmatrix\}(.+?)\\end\{bmatrix\}',q[id]['stem'])[1]
 return S.Matrix([[S.Rational(x)for x in row.split('&')]for row in s.split('\\\\')])
A=S.Matrix([[1,1],[1,2],[1,3]]);b=S.Matrix([1,2,2]);x,r,e=fit(A,b)
ck('LS01 coefficients',equal(x,S.Matrix([S.Rational(2,3),S.Rational(1,2)])));ck('LS01 error',e==S.Rational(1,6))
for id,bv,xv,err in [('LS02',[4,1,2],[3,2],11),('LS03',[3,5,7,-3],[10,-6,2],4),('LS09',[1,2,4],[S.Rational(4,3),S.Rational(7,3)],S.Rational(1,3))]:
 AA=matrix_stem(id);xx,rr,ee=fit(AA,S.Matrix(bv));ck(id+' actual stem matrix solution',equal(xx,S.Matrix(xv)));ck(id+' error',ee==err)
t=S.Matrix([-1,0,1]);Ac=S.ones(3,1).row_join(t);xx,rr,ee=fit(Ac,S.Matrix([0,1,3]));ck('LS04 centered fit',list(xx)==[S.Rational(4,3),S.Rational(3,2)]and ee==S.Rational(1,6))
xx,rr,ee=fit(S.Matrix([1,2,3]),b);ck('LS05 origin error',xx[0]==S.Rational(11,14)and ee==S.Rational(5,14)and sum(rr)!=0)
u=S.Matrix([1,2,0]);Ar=u.row_join(2*u);bb=S.Matrix([3,1,2]);xm=Ar.pinv()*bb;ck('LS07 minimum norm',list(xm)==[S.Rational(1,5),S.Rational(2,5)]);ck('LS07 error',((bb-Ar*xm).T*(bb-Ar*xm))[0]==9)
ck('LS06 minimum norm',list(S.Matrix([[1,2]]).pinv()*S.Matrix([4]))==[S.Rational(4,5),S.Rational(8,5)])
Ao=S.Matrix([[1,1],[1,-1],[0,2]]);xx,rr,ee=fit(Ao,S.Matrix([1,2,3]));ck('LS10 normalized divisions',list(xx)==[S.Rational(3,2),S.Rational(5,6)]and ee==S.Rational(16,3))
v=S.Matrix([3,4]);normal=v+5*S.Matrix([1,0]);H=S.eye(2)-2*normal*normal.T/(normal.dot(normal));ck('LS11 reflector',H*v==S.Matrix([-5,0])and H.T*H==S.eye(2));ck('LS11 response',H*S.Matrix([1,2])==S.Matrix([-S.Rational(11,5),S.Rational(2,5)]))
xx,rr,ee=fit(matrix_stem('LS12'),S.Matrix([5,6,7]));ck('LS12 triangular answer',list(xx)==[S.Rational(3,2),2]and ee==49)
T=S.Matrix([[1,2],[0,1]]);ck('LS13 basis change',list(T.inv()*x)==[-S.Rational(1,3),S.Rational(1,2)])
Ap=S.Matrix([[1,-1,1],[1,0,0],[1,0,0],[1,1,1]]);xx,rr,ee=fit(Ap,S.Matrix([1,0,2,3]));ck('LS14 duplicate-input fit',list(xx)==[1,1,1]and ee==2)
xx,rr,ee=fit(S.ones(3,1),S.Matrix([0,2,4]),S.diag(1,1,2));ck('LS16 weighted fit',xx[0]==S.Rational(5,2)and ee==11)
xx,rr,ee=fit(S.Matrix([[1,0],[1,1],[1,2]]),S.Matrix([0,1,0]),S.diag(1,2,1));ck('LS17 weighted fit',list(xx)==[S.Rational(1,2),0]and ee==1 and sum(rr)!=0)
W=S.Matrix([[2,1],[1,2]]);aa=S.Matrix([1,0]);xx,rr,ee=fit(aa,S.Matrix([0,1]),W);PW=aa*(aa.T*W*aa).inv()*aa.T*W;ck('LS18 weighted geometry',xx[0]==S.Rational(1,2)and ee==S.Rational(3,2)and PW!=PW.T and PW.T*W==W*PW)
z,lam=S.symbols('z lam',positive=True);ck('LS20 unbounded signed loss',S.expand(z*z-(1-z)**2)==2*z-1)
ck('LS21 constrained identity',S.expand((3-z)**2+(1-z)**2-2*(z-2)**2)==2)
ck('LS23 restoring constraint',S.Matrix([[1,1],[1,-1]]).det()!=0)
ck('LS24 ridge terms',S.Rational(3,2)**2+2**2==S.Rational(25,4))
ridge=(S.Matrix([[1,1],[1,1]])+lam*S.eye(2)).inv()*S.Matrix([2,2]);ck('LS25 ridge path',all(S.simplify(v-2/(2+lam))==0 for v in ridge))
ck('LS26 common kernels trivial',S.Matrix([[1,1],[0,1]]).rank()==2)
ck('LS27 common kernels nontrivial',S.Matrix([[1,0],[1,0]]).rank()==1)
P=Ac*(Ac.T*Ac).inv()*Ac.T;ck('LS29 leverage',list(P.diagonal())==[S.Rational(5,6),S.Rational(1,3),S.Rational(5,6)])
bb=S.Matrix([0,1,0]);xx,rr,ee=fit(Ac,bb)
for i in range(3):
 idx=[j for j in range(3)if j!=i];xd,rd,ed=fit(Ac[idx,:],bb[idx,:]);deleted=bb[i]-(Ac[i,:]*xd)[0];ck('LS29 direct deletion '+str(i),deleted==rr[i]/(1-P[i,i])==[-2,1,-2][i])
Ad=S.Matrix([[1,0],[0,1],[0,1]]);Pd=Ad*Ad.pinv();ck('LS30 deletion loses rank',Pd[0,0]==1 and Ad[1:,:].rank()==1)
u=S.Matrix([-S.Rational(1,3),S.Rational(2,3),-S.Rational(1,3)]);bb=S.Matrix([1,0,3]);ck('LS33 added feature gain',u.dot(bb)**2/u.dot(u)==S.Rational(8,3))
ep=S.symbols('ep',nonzero=True,real=True);Ae=S.Matrix([[1,1],[0,ep],[0,0]]);delta=S.Rational(1,100);xx,rr,ee=fit(Ae,S.Matrix([1,delta,1]));ck('LS35 exact sensitivity',equal(xx,S.Matrix([1-delta/ep,delta/ep]))and ee==1)
a=S.symbols('a',real=True);ck('LS36 variance identity',S.expand(a*a+(1-a)**2-2*(a-S.Rational(1,2))**2)==S.Rational(1,2));ck('LS37 heteroscedastic variance',S.expand(a*a+9*(1-a)**2-10*(a-S.Rational(9,10))**2)==S.Rational(9,10))
outcomes=[((u+v)/2,(u-v)/2)for u,v in product([-1,1],repeat=2)];ck('LS40 dependent zero covariance',sum(m*d for m,d in outcomes)==0 and sum(m==0 and d==0 for m,d in outcomes)==0)
AA=S.Matrix([1,S.I]);bb=S.Matrix([1,1]);xc=(AA.H*AA).inv()*AA.H*bb;rc=bb-AA*xc;ck('LS42 complex fit',xc[0]==(1-S.I)/2 and S.simplify((rc.H*rc)[0])==1 and (AA.T*AA)[0]==0)
AA=S.Matrix([1,1]);BB=S.Matrix([[1,2],[3,0]]);XX=AA.pinv()*BB;RR=BB-AA*XX;ck('LS43 multiresponse',XX==S.Matrix([[2,1]])and sum(v*v for v in RR)==4)
AA=S.Matrix([[1,0],[0,1],[1,1]]);bb=S.Matrix([2-z,-1-z,1+z]);xx,rr,ee=fit(AA,bb);ck('LS44 inverse construction',xx==S.Matrix([2,-1])and S.expand(ee)==3*z*z)
ck('LS46 original-error comparison',S.Rational(2,5)**2+(2-S.Rational(2,5))**2==S.Rational(68,25))
ck('LS47 wrong certificate',S.Matrix([-1,1]).dot(S.Matrix([1,1]))==0 and S.Matrix([-1,1]).dot(S.Matrix([1,0]))!=0)
ck('LS48 mean versus median',2*3**2+(9-3)**2==54 and 2*abs(0)+abs(9)==9)
ck('LS49 coordinate-dependent minimum norm',list(S.Matrix([[2,1]]).pinv())==[S.Rational(2,5),S.Rational(1,5)])
eps=S.symbols('eps',real=True);exact=eps/(1+eps*eps);ck('LS50 first-order residual term',S.diff(exact,eps).subs(eps,0)==1)
# General identities are checked across declared exact finite domains.
for vals in product([-2,0,3],repeat=3):
 for weights in [(1,1,1),(1,2,3),(9,1,4)]:
  bb=S.Matrix(vals);WW=S.diag(*weights);xx,rr,ee=fit(A,bb,WW)
  for zz in [S.Matrix([1,0]),S.Matrix([0,1]),S.Matrix([-2,3])]:
   new=bb-A*(xx+zz);ck('weighted global excess identity',equal((new.T*WW*new)[0]-ee,(zz.T*A.T*WW*A*zz)[0]))
for pval in [S.Rational(1,4),1,4]:
 for bv in [S.Matrix([1,2,2]),S.Matrix([-3,0,4])]:
  G=A.T*A;xx=(G+pval*S.eye(2)).inv()*A.T*bv;rr=bv-A*xx;ck('general ridge stationarity',A.T*rr==pval*xx)
models=json.loads((R/'dist/chapters/l_leastsquares-models.json').read_text())
for id,frames in models.items():
 for k,f in enumerate(frames):
  if f['kind']=='fit':
   ts=list(map(S.Rational,map(str,f['t'])));ys=list(map(S.Rational,map(str,f['y'])));ws=list(map(S.Rational,map(str,f['w'])));c=S.Rational(f['exactC']);d=S.Rational(f['exactD']);res=[y-c-d*t for y,t in zip(ys,ts)];keep=[i for i in range(len(ts))if i!=f.get('omit')]
   ck(id+' actual plotted error '+str(k),sum(ws[i]*res[i]**2 for i in keep)==S.Rational(f['sse']))
   ck(id+' actual plotted residual '+str(k),res==list(map(S.Rational,f['residual'])))
  elif f['kind']=='ridge':
   l=S.Rational(f['lambdaExact']);x=S.Rational(f['xExact']);ck('ridge checkpoint '+str(k),x==3/(1+l)and S.Rational(f['sse'])==(3-x)**2+l*x*x)
  elif f['kind']=='ridge-identity':
   l=S.Rational(f['lambdaExact']);alpha=S.Rational(f['alphaExact']);ck('two-coordinate ridge checkpoint '+str(k),alpha==1/(1+l)and list(map(S.Rational,f['xExact']))==[3*alpha,4*alpha]and S.Rational(f['sse'])==25*(1-alpha)**2+25*l*alpha*alpha)
  elif f['kind']=='coefficients':ck(id+' feasible actual point '+str(k),sum(S.Rational(a)*S.Rational(x)for a,x in zip(f['a'],f['pointExact']))==f['rhs'])
  elif f['kind']=='sensitivity':ck('sensitivity checkpoint '+str(k),S.Rational(f['xExact'][1])==S.Rational(f['delta'])/S.Rational(f['epsilon'])and sum(map(S.Rational,f['xExact']))==1)
page=(R/'dist/chapters/l_leastsquares.html').read_text(encoding='utf8');sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
maths=re.findall(r'<math\b[\s\S]*?</math>',page)
for i,m in enumerate(maths):
 root=ET.fromstring(m);ck('delimiter and scripts '+str(i),not delimiter_issues(root)and not closing_script_bases(root))
ck('all worked answers present',page.count('class="exam-question"')==51 and page.count('class="exam-solution"')==51)
ck('sixty complete final decisions',page.count('class="review-rule"')==60)
visible=re.sub(r'<(?:script|style)\b[\s\S]*?</(?:script|style)>','',page);ck('no raw TeX or slots',not re.search(r'\$|MATHSLOT',visible))
ck('all question statements and solutions written',len(q)==50 and all(len(x['solution'].split())>=75 for x in q.values()))
report=dict(status='passed_independent_mathematical_checks',checks=len(checks),assertions=checks,nativeExpressions=len(maths),workedEntries=51,finalDecisions=60,distinctModelFamilies=len(models),modelCheckpoints=sum(map(len,models.values())),documentSha256=hashlib.sha256((R/'dist/chapters/l_leastsquares.html').read_bytes()).hexdigest(),normalizedTextSha256=hashlib.sha256(page.encode()).hexdigest(),limits='Exact matrix models, symbolic identities and finite grids test the recorded cases; editorial proofs and source comparison remain separate evidence. Not universal correctness or unseen performance certification.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in report.items()if k not in ['assertions','limits']})
