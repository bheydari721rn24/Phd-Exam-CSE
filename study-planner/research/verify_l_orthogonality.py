"""Independent symbolic examples, actual JS oracle and native formula fences."""
from pathlib import Path
import json,re,random,subprocess,hashlib,sys,xml.etree.ElementTree as ET,sympy as S
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_orthogonality-evidence';checks=[]
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
def ck(name,ok):assert bool(ok),name;checks.append(name)
M=S.Matrix;t=S.symbols('t');I=S.eye(2)
G=M([[2,t],[t,3]])
ck('two-by-two positivity determinant',G.det()==6-t*t)
u=M([3,-1]);v=M([1,3]);x=M([1,2])
ck('Berkeley coordinates',u.dot(v)==0 and u/10+7*v/10==x)
u1=M([1,-1,1]);u2=M([-1,0,1]);x=M([1,2,3]);p=S.Rational(2,3)*u1+u2;r=x-p
ck('Berkeley projection',p==M([-S.Rational(1,3),-S.Rational(2,3),S.Rational(5,3)])and u1.dot(r)==u2.dot(r)==0 and r.dot(r)==S.Rational(32,3))
polys=[1,t,t*t-S.Rational(1,3)]
ck('polynomial orthogonal Gram',M([[S.integrate(a*b,(t,-1,1))for b in polys]for a in polys])==S.diag(2,S.Rational(2,3),S.Rational(8,45)))
ck('odd projection source correction',all(S.integrate(t**3*f,(t,-1,1))==0 for f in [1,t*t]))
ck('cubic residual',S.integrate((t**3-S.Rational(3,5)*t)**2,(t,-1,1))==S.Rational(8,175))
p4=S.Rational(6,7)*t*t-S.Rational(3,35)
ck('fourth-power projection',all(S.integrate((t**4-p4)*f,(t,-1,1))==0 for f in [1,t*t]))
ck('fourth-power residual',S.integrate((t**4-p4)**2,(t,-1,1))==S.Rational(128,11025))
mit=[M([1,-1,0,0]),M([S.Rational(1,2),S.Rational(1,2),-1,0]),M([S.Rational(1,3),S.Rational(1,3),S.Rational(1,3),-1])]
ck('MIT orthogonal hyperplane basis',all(a.dot(b)==0 for i,a in enumerate(mit)for j,b in enumerate(mit)if i!=j)and all(sum(a)==0 for a in mit)and M.hstack(*mit).rank()==3)
H=M([[S.Rational(3,5),S.Rational(4,5)],[S.Rational(4,5),-S.Rational(3,5)]])
ck('Householder target',H*M([3,4])==M([5,0])and H.T*H==I)
N=M([[S.Rational(1,2),S.Rational(1,2)],[0,0]])
ck('alternating line powers',all(N**k==S.Rational(1,2)**k*M([[1,1],[0,0]])for k in range(1,8)))
z=M([1,S.I]);P=z*z.H/(z.H*z)[0];r=M([1,0])-P*M([1,0])
ck('complex conjugation',P.H==P and P*P==P and(z.H*r)[0]==0)
models=json.loads((R/'dist/chapters/l_orthogonality-models.json').read_text())
for model in models['models']:
 for i,f in enumerate(model['frames']):
  q=f['snapshot'];tag=model['id']+' frame'+str(i)
  if 'P'in q:
   A,G,x,p,r,P=map(M,[q['A'],q['G'],q['input'],q['projection'],q['residual'],q['P']])
   ck(tag+' membership',A.row_join(p).rank()==A.rank())
   ck(tag+' exact split',x==p+r and P*x==p)
   ck(tag+' residual',A.T*G*r==S.zeros(A.cols,1))
   ck(tag+' projector',P*P==P and P.T*G==G*P)
   ck(tag+' distance',(r.T*G*r)[0]==S.Rational(q['distanceSquared']))
   ck(tag+' norm split',(x.T*G*x)[0]==(p.T*G*p)[0]+(r.T*G*r)[0])
  if model['id']=='reflection':
   H,x,y=map(M,[q['H'],q['input'],q['output']])
   ck(tag+' orthogonality',(H.T*H-I).applyfunc(S.simplify)==S.zeros(2))
   ck(tag+' reflected output',(H*x-y).applyfunc(S.simplify)==S.zeros(2,1))
  if model['id']=='qr':
   Q,RR=map(M,[q['Q'],q['R']]);ck(tag+' orthonormal columns',Q.T*Q==S.eye(3))
   ck(tag+' reconstruction',Q*RR[:,q['columnNumber']-1]==M(q['reconstructed']))
  if model['id']=='gram':
   accepted=[M(u)for u in q['accepted']]
   ck(tag+' accepted perpendicularity',all(a.dot(b)==0 for j,a in enumerate(accepted)for b in accepted[j+1:]))
   ck(tag+' accepted nonzero',all(u.dot(u)>0 for u in accepted))
   if q['phase'].startswith('Normalize'):ck(tag+' unit output',S.simplify(M(q['residual']).dot(M(q['residual'])))==1)
random.seed(1406);cases=[]
for i in range(120):
 n=random.randint(2,4);k=random.randint(1,4);A=M(n,k,[random.randint(-4,4)for _ in range(n*k)])
 if i%5==0:A=S.zeros(n,k)
 if i%5==1 and k>1:A[:,1]=2*A[:,0]
 x=M([random.randint(-4,4)for _ in range(n)]);w=[random.randint(1,5)for _ in range(n)]
 cases.append(dict(A=A.tolist(),x=list(x),weights=w))
plain=json.loads(json.dumps(cases,default=int))
code="const fs=require('fs'),a=require('./dist/chapters/l_orthogonality.js');const z=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(z.map(c=>a.projectionLab(c.A,c.x,c.weights).result)));"
res=subprocess.run(['node','-e',code],input=json.dumps(plain),text=True,capture_output=True,cwd=R,check=True);actual=json.loads(res.stdout)
for i,(c,out)in enumerate(zip(cases,actual)):
 A,x=M(c['A']),M(c['x']);G=S.diag(*c['weights']);C=M.hstack(*A.columnspace())if A.rank()else S.zeros(A.rows,0)
 expected=C*(C.T*G*C).inv()*C.T*G if C.cols else S.zeros(A.rows)
 P=M(out['projector']);p=M(out['projection']);r=M(out['residual'])
 ck('Actual JavaScript projector '+str(i),P==expected)
 ck('Actual JavaScript output '+str(i),p==P*x and r==x-p)
 ck('Actual JavaScript norm '+str(i),S.Rational(out['squaredDistance'])==(r.T*G*r)[0])
 ck('Actual JavaScript certificates '+str(i),all(out['checks'].values())and out['rank']==A.rank())
page=(R/'dist/chapters/l_orthogonality.html').read_text(encoding='utf-8')
maths=re.findall(r'<math\b[\s\S]*?</math>',page)
for i,m in enumerate(maths):
 node=ET.fromstring(m);ck('Math fences '+str(i),not closing_script_bases(node)and not delimiter_issues(node))
for c in json.loads((E/'prior-library.json').read_text())['chapters']:
 ck('Retained '+c['topicId'],hashlib.sha256((R/'dist'/c['url']).read_bytes().replace(b'\r\n',b'\n')).hexdigest()==c['canonicalLFsha256'])
ck('authored bank',len(json.loads((B/'l_orthogonality-questions.json').read_text()))==82)
ck('final rules',len(re.findall(r'^\d+\. ',(B/'l_orthogonality-review.en.md').read_text(),re.M))==84)
report=dict(status='passed',exactChecks=len(checks),actualJSOracleCases=120,staticMathMLChecks=len(maths),retainedPriorChapters=59,checks=checks)
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()if k!='checks'}))
