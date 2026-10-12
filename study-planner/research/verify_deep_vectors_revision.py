from pathlib import Path
import ast,hashlib,itertools,json,re,subprocess,tempfile,xml.etree.ElementTree as ET
from fractions import Fraction as F
import sympy as S
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='3838bc4653b34ac78dc5f73f82c6b6302b7afe92';checks=[]
def check(label,value):assert value,label;checks.append(dict(name=label,passed=True))
for n in range(1,10):
 basis=[]
 for i in range(n):
  for j in range(i+1,n):
   m=S.zeros(n);m[i,j]=m[j,i]=1;basis.append(m)
 for i in range(n-1):
  m=S.zeros(n);m[i,i]=1;m[n-1,n-1]=-1;basis.append(m)
 check(f'trace basis properties {n}',all(m==m.T and S.trace(m)==0 for m in basis) and len(basis)==n*(n+1)//2-1)
 check(f'trace basis rank {n}',(S.Matrix.hstack(*[S.Matrix(n*n,1,list(m)) for m in basis]).rank() if basis else 0)==len(basis))
 u=S.eye(3*n)[:,:2*n];v=S.eye(3*n)[:,n:];check(f'sum witness dimension {n}',u.rank()==v.rank()==2*n and u.row_join(v).rank()==3*n)
 A=S.zeros(n+3,n+1)
 for i in range(n-1):A[i,i]=1
 check(f'rectangular witness {n}',A.rank()==n-1 and len(A.nullspace())==2 and len(A.T.nullspace())==4)
 for x in [5,8,n]:
  w=S.Matrix([x,1,2]);d=S.Matrix([1,1,0]);p=w.dot(d)/d.dot(d)*d;r=w-p
  check(f'projection and residual {n},{x}',d.dot(r)==0 and p.dot(p)==S.Rational((x+1)**2,2) and r.dot(r)==S.Rational((x-1)**2,2)+4 and w.dot(w)==p.dot(p)+r.dot(r))
  c=S.Matrix([(S.Rational(x)+2)/2,(S.Rational(x)-2)/2]);M=S.Matrix([[1,1],[1,-1]]);check(f'coordinates and metric {n},{x}',M*c==S.Matrix([x,2]) and (c.T*M.T*M*c)[0]==x*x+4)
 kernel=[S.eye(n+1)[:,i]-S.eye(n+1)[:,n] for i in range(n)];check(f'coordinate sum kernel {n}',S.Matrix.hstack(*kernel).rank()==n and all(sum(v)==0 for v in kernel))
N=S.symbols('n',real=True);w=S.Matrix([N,1,2]);d=S.Matrix([1,1,0]);p=(N+1)/2*d;r=w-p
check('symbolic projection split',S.expand(w.dot(w)-p.dot(p)-r.dot(r))==0)
a,s,z1,z2=S.symbols('a s z1 z2',real=True);A=(1-a)*S.eye(3)+a*S.ones(3);x=S.Matrix([s+z1,s+z2,s-z1-z2])
check('structured quadratic form identity',S.expand((x.T*A*x)[0]-3*(1+2*a)*s*s-(1-a)*(z1*z1+z2*z2+(z1+z2)**2))==0)
for aa in [S.Rational(-3,4),S.Rational(-1,2),S.Rational(-1,4),0,S.Rational(3,4),1,S.Rational(5,4)]:
 M=A.subs(a,aa);check(f'positivity exact eigenvalues {aa}',sorted([(val,mult) for val,mult in M.eigenvals().items()])==sorted({1-aa:2,1+2*aa:1}.items()) if aa!=0 else M==S.eye(3))
P=S.diag(4,0);check('literal nonunit source failure',P*P!=P and P*S.Matrix([0,1])==S.zeros(2,1))
Q=S.Matrix([[1,2],[0,0]]);check('oblique idempotent noncontraction',Q*Q==Q and (Q*S.Matrix([0,1])).norm()==2)
for u,v,w,expected in [(S.Matrix([1,0,1]),S.Matrix([1,1,0]),S.Matrix([1,2,3]),S.Matrix([S.Rational(7,3),S.Rational(2,3),S.Rational(5,3)])),(S.Matrix([1,1,0]),S.Matrix([1,0,1]),S.Matrix([0,1,1]),S.Matrix([S.Rational(2,3),S.Rational(1,3),S.Rational(1,3)]))]:
 M=u.row_join(v);p=M*(M.T*M).inv()*M.T*w;r=w-p;check('exact coupled projection '+str(list(w)),p==expected and M.T*r==S.zeros(2,1) and w.dot(w)==p.dot(p)+r.dot(r))
normal=S.Matrix([2,-1,2]);X=S.Matrix([1,2,3]);foot=X-(normal.dot(X)-4)/normal.dot(normal)*normal
check('plane foot and distance',foot==S.Matrix([S.Rational(5,9),S.Rational(20,9),S.Rational(23,9)]) and normal.dot(foot)==4 and (X-foot).dot(X-foot)==S.Rational(4,9))
M=S.Matrix([[1,1,0],[1,0,1],[0,1,a]]);check('parameter independence witness',M.det()==-a-1 and M.subs(a,-1).rank()==2)
u=S.Matrix([1,S.I]);v=S.Matrix([S.I,1]);check('complex conjugate convention',(S.conjugate(u).T*v)[0]==0 and (S.conjugate(u).T*u)[0]==2 and (u.T*u)[0]==0)
check('complex projection numerator',(S.conjugate(u).T*(S.I*u))[0]/2==S.I)
y=S.symbols('y',real=True);check('affine objective complete square',S.expand(2*(1-y)**2+y*y-3*(y-S.Rational(2,3))**2-S.Rational(2,3))==0)
t=S.symbols('t',real=True);check('polynomial corrected parity',S.integrate(t**3*(t*t-S.Rational(1,3)),(t,-1,1))==0 and S.integrate((t*t-S.Rational(1,3))**2,(t,-1,1))==S.Rational(8,45))
for v in [[1,2,3],[2,-1,3],[-1,1,0]]:
 u=S.Matrix([1,1,0]);x=S.Matrix(v);check('cross perpendicularity '+str(v),u.dot(u.cross(x))==x.dot(u.cross(x))==0)
scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes']
for id in ['source','positivity','gram37','gram45','coordinates','minimum']:
 for i,f in enumerate(scenes['vectors-question-'+id]['frames']):
  s=f['snapshot']
  if id=='source':check(f'source comparison {i}',s['source']==[s['scale']**2*s['x'][0],0] and s['foot']==[s['x'][0],0] and s['idempotent']==(s['scale']==1))
  if id=='positivity':aa=F(s['a']);check(f'coefficient signs {i}',s['parallel']==float(1+2*aa) and s['perpendicular']==float(1-aa) and s['valid']==(-F(1,2)<aa<1))
  if id=='coordinates':c=s['c'];check(f'head-to-tail basis {i}',s['partial']==[c[0]+c[1],c[0]-c[1]])
  if id=='minimum':
   yy=s['y'];v=list(map(F,s['vector']));check(f'objective checkpoint {i}',abs(s['value']-(2*(1-yy)**2+yy*yy))<1e-12 and v[0]+v[1]==v[1]+v[2]==1)
  if id.startswith('gram'):check(f'Gram exact state {id},{i}',len(s['coefficients'])==2 and len(s['foot'])==len(s['residual'])==3)
gs=scenes['vectors-question-gram-schmidt']['frames']
check('Gram Schmidt exact eight checkpoints',len(gs)==8)
for i,f in enumerate(gs):
 st=f['snapshot'];basis=st['basis'];check(f'Gram Schmidt unit directions {i}',all(abs(sum(x*x for x in q)-1)<1e-12 for q in basis) and all(abs(sum(x*y for x,y in zip(q,p)))<1e-12 for j,q in enumerate(basis) for p in basis[j+1:]))
 check(f'Gram Schmidt retained dimension {i}',len(basis)==[0,1,1,1,1,1,2,2][i])
check('Gram Schmidt dependent subtraction',gs[3]['snapshot']['residual']==[0,0] and gs[3]['snapshot']['input']==[2,2])
check('Gram Schmidt zero skip and later continuation',gs[4]['snapshot']['residual']==[0,0] and gs[5]['snapshot']['input']==[1,-1] and len(gs[-1]['snapshot']['basis'])==2)
check('no implementation representation in source captions',all('Fraction(' not in f['caption'] for f in scenes['vectors-question-source']['frames']))
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
page=(R/'dist/chapters/l_vectors.html').read_text();old=subprocess.check_output(['git','show',BASE+':dist/chapters/l_vectors.html']).decode();qs=ns['questions'](page);oq=ns['questions'](old);rev=json.loads((E/'l_vectors-revision.json').read_text());check('preserve all 46 placements',len(qs)==len(oq)==46)
for i,(record,(_,_,attrs,q),(_,_,oldattrs,o)) in enumerate(zip(rev['records'],qs,oq),1):
 check(f'complete mathematical response {i}',record['words']>=100 and '<math' in q[q.index('<details'):])
 if i==3:check('source ambiguity no fabricated unique key',record['answer'] is None and attrs.get('data-source-ambiguous')=='true' and 'data-answer' not in attrs and 'An orthogonal basis' in ns['plain'](q))
 else:
  oldkey=int(oldattrs['data-answer']) if oldattrs.get('data-answer') else int(re.search(r'Correct option:\s*(\d+)',ns['plain'](o))[1]);check(f'answer preserved {i}',record['answer']==int(attrs['data-answer'])==oldkey)
 if i<=4:check(f'authentic options preserved {i}',re.search(r'<div class="exam-options">[\s\S]*?</div></div></div>',q)[0]==re.search(r'<div class="exam-options">[\s\S]*?</div></div></div>',o)[0])
for formula in re.findall(r'<math\b[\s\S]*?</math>',page):
 e=ET.fromstring(formula)
 for c in e.iter():
  if c.tag.split('}')[-1] in ['msup','msub','msubsup']:check('native script base',list(c)[0].text not in [')',']','}'])
for c in json.loads((E/'inventory.json').read_text())['chapters']:
 if c['topicId']=='l_vectors':continue
 path='dist/'+c['url'];before=subprocess.check_output(['git','show',BASE+':'+path]).decode().replace('\r\n','\n');after=(R/path).read_text()
 if c['topicId'] in ['l_matrices','l_linear','l_spaces','l_orthogonality']:
  def mask(s):
   for a,b,attrs,q in reversed(ns['questions'](s)):
    if attrs.get('data-source-id')=='Phd_CS_1404_Q31':s=s[:a]+'SOURCE_Q31'+s[b:]
   return s
  check('preserve related chapter outside corrected source '+c['topicId'],mask(before)==mask(after))
 else:check('preserve other chapter '+c['topicId'],before==after)
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
check('canonical source ambiguity',actual['Phd_CS_1404_Q31']['answer'] is None and actual['Phd_CS_1404_Q31']['intendedAnswer']==3)
for _,_,attrs,q in qs[:4]:
 item=actual[attrs['data-source-id']];path=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/item['repoPath'];check('original PDF hash '+item['id'],hashlib.sha256(path.read_bytes()).hexdigest()==item['sourceSha256'])
report=dict(topicId='l_vectors',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='Finite exact witnesses and symbolic identities complement general proofs. The authentic Q31 literal source has no asserted unique key; no universal completeness or future-performance certification.')
(E/'l_vectors-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'checks':len(checks),'status':report['status']})
