from pathlib import Path
import ast,hashlib,json,re,subprocess,tempfile,xml.etree.ElementTree as ET
import sympy as S
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='a28dc770d47ecedeee37be63820d05ee4c2d7665';checks=[]
def check(label,value):assert value,label;checks.append(dict(name=label,passed=True))
for n in [1,2,3,5,8]:
 J=S.ones(n);check('allones action '+str(n),J*J==n*J);check('allones determinant '+str(n),(S.eye(n)+J).det()==n+1);check('allones inverse '+str(n),(S.eye(n)+J)*(S.eye(n)-J/(n+1))==S.eye(n));check('scalar product determinant '+str(n),(6*S.eye(n)).det()==6**n)
 if n>=2:
  P=S.zeros(n)
  for j in range(n):P[(j+1)%n,j]=1
  check('weighted derangement trace '+str(n),S.trace(S.diag(*range(1,n+1))*P)==0)
 if n>=2:
  U=S.eye(n)[:,:2];V=U.T;check('rank two standard witness '+str(n),(U*V).rank()==2 and len((U*V).nullspace())==n-2)
 if n>=4:
  V=S.zeros(2,n);V[0,2]=V[1,3]=1;check('rank two squarezero reverse '+str(n),(U*V).rank()==2 and (U*V)**2==S.zeros(n) and V*U==S.zeros(2))
 for c in [S.zeros(n),S.eye(n),S.ones(n)]:
  M=S.eye(n).row_join(c).col_join(S.zeros(n).row_join(2*S.eye(n)));inv=S.eye(n).row_join(-c/2).col_join(S.zeros(n).row_join(S.eye(n)/2));check('ordered block determinant inverse '+str(n)+str(c[0,0]),M.det()==2**n and M*inv==inv*M==S.eye(2*n))
t=S.symbols('t');shear=S.Matrix([[1,t],[0,1]]);inv=S.Matrix([[1,-t],[0,1]]);check('symbolic shear two sided',shear*inv==inv*shear==S.eye(2))
N=S.Matrix([[0,1,0],[0,0,1],[0,0,0]])
for k in range(11):check('nilpotent power '+str(k),(S.eye(3)+N)**k==S.Matrix([[1,k,k*(k-1)//2],[0,1,k],[0,0,1]]))
Bmat=S.Matrix([[1,1],[1,-1]]);n=S.symbols('n');T=S.diag(2,n);check('symbolic coordinate similarity',Bmat.inv()*T*Bmat==S.Matrix([[n+2,2-n],[2-n,n+2]])/2)
T=S.Matrix([[2,1],[1,0]]);check('specific coordinate columns',Bmat.inv()*T*Bmat==T and T*Bmat[:,0]==S.Matrix([3,1]) and T*Bmat[:,1]==S.Matrix([1,1]))
M=S.Matrix([[1,1,1],[0,1,1],[1,0,2]]);check('nontriangular coincidence',M.det()==2 and M[0,0]*M[1,1]*M[2,2]==2 and M[0,1]!=0 and M[2,0]!=0)
A=S.Matrix([[1,1],[0,1]]);B2=S.diag(2,3);M=A*B2*A.inv();candidates=[A*B2.inv()*A.inv(),A.inv()*B2.inv()*A,A.inv()*B2.inv()*A.inv(),A*B2.inv()*A];check('inverse order numeric alternatives',[M*x==S.eye(2) for x in candidates]==[True,False,False,False]);check('inverse alternatives exact entries',[x[0,1] for x in candidates]==[S.Rational(-1,6),S.Rational(1,6),S.Rational(-5,6),S.Rational(5,6)])
A=S.Matrix([[1,0,0],[0,1,0]]);B2=A.T;check('rectangular trace determinant',(A*B2)==S.eye(2) and B2*A==S.diag(1,1,0) and S.trace(A*B2)==S.trace(B2*A)==2 and (A*B2).det()==1 and (B2*A).det()==0)
check('lattice counts and distractors',sum(6-i for i in range(6))==21 and 21*16==336 and S.binomial(24,4)+21==10647 and S.binomial(24,4)*21==223146)
a=S.symbols('a',real=True);x1,x2,x3,s=S.symbols('x1 x2 x3 s',real=True);x=S.Matrix([s+x1,s+x2,s+x3,s-x1-x2-x3]);M=(1-a)*S.eye(4)+a*S.ones(4);check('four dimensional positivity decomposition',S.expand((x.T*M*x)[0]-4*(1+3*a)*s*s-(1-a)*(x1*x1+x2*x2+x3*x3+(x1+x2+x3)**2))==0)
scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes']
for name,scene in scenes.items():
 if not name.startswith('matrices-question-'):continue
 for i,f in enumerate(scene['frames']):
  st=f['snapshot'];kind=st['kind']
  expected={'allones':{'leftMath':(5,5),'rightMath':(5,5)},'fixed':{'leftMath':(5,5),'rightMath':(5,5)},'rank':{'leftMath':(5,2),'rightMath':(2,5),'productMath':(5,5)},'power':{'matrixMath':(3,3)},'gram':{'leftMath':(2,2),'rightMath':(2,2)}}.get(kind,{})
  for field,(rows,columns) in expected.items():
   xml=ET.fromstring(st[field]);table=next(c for c in xml.iter() if c.tag.split('}')[-1]=='mtable');check(name+' native shape '+field+str(i),len(table)==rows and all(len(row)==columns for row in table))
  if kind=='power':check(name+str(i),st['value']==st['k']*(st['k']-1)//2)
  if kind=='fixed':check(name+str(i),st['DP']==[[(r+1)*st['P'][r][c] for c in range(5)] for r in range(5)] and st['trace']==sum(st['DP'][r][r] for r in range(5)))
  if kind=='gram':check(name+str(i),st['out']==[sum(st['x']),0] and st['norm']==sum(st['x'])**2)
  if kind=='positivity':aa=S.Rational(st['a']);d=st['dimension'];check(name+str(i),st['parallel']==float(1+(d-1)*aa) and st['perpendicular']==float(1-aa) and st['valid']==(-S.Rational(1,d-1)<aa<1))
  if kind=='trace':check(name+str(i),st['terms']==[[2,2,0],[0,-4,3]])
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
page=(R/'dist/chapters/l_matrices.html').read_text();old=subprocess.check_output(['git','show',BASE+':dist/chapters/l_matrices.html']).decode();qs=ns['questions'](page);oq=ns['questions'](old);rev=json.loads((E/'l_matrices-revision.json').read_text());check('47 placements preserved',len(qs)==len(oq)==47)
for i,(record,(_,_,attrs,q),(_,_,oa,o)) in enumerate(zip(rev['records'],qs,oq),1):
 check('complete mathematical response '+str(i),record['words']>=150 and '<math' in q[q.index('<details'):])
 if i==4:check('literal ambiguity preserved',record['answer'] is None and 'data-answer' not in attrs and attrs.get('data-source-ambiguous')=='true')
 else:
  key=int(oa['data-answer']) if oa.get('data-answer') else int(re.search(r'Correct option:\s*(\d+)',ns['plain'](o))[1]);check('answer preserved '+str(i),key==record['answer']==int(attrs['data-answer']))
 if i==2:check('fresh authentic option 37',ns['plain'](q[q.index('<div class="exam-options">'):]).startswith('1. 37'))
 if i==9:check('triangular guarantee not false necessity','guarantees the diagonal-product' in ns['plain'](q) and 'directly only' not in ns['plain'](q))
 if i==33:check('same ordered basis qualification','same new ordered basis' in ns['plain'](q))
for formula in re.findall(r'<math\b[\s\S]*?</math>',page):
 e=ET.fromstring(formula)
 for c in e.iter():
  if c.tag.split('}')[-1] in ['msup','msub','msubsup']:check('native script base',list(c)[0].text not in [')',']','}'])
for c in json.loads((E/'inventory.json').read_text())['chapters']:
 if c['topicId']=='l_matrices':continue
 path='dist/'+c['url'];before=subprocess.check_output(['git','show',BASE+':'+path]).decode().replace('\r\n','\n');after=(R/path).read_text()
 if c['topicId']=='l_gauss':
  def mask(s):
   for a,b,attrs,q in reversed(ns['questions'](s)):
    if attrs.get('data-source-id')=='MS_CS_1405_Q113':s=s[:a]+'SOURCE_Q113'+s[b:]
   return s
  check('Gaussian chapter source-only correction',mask(before)==mask(after))
 else:check('preserve other chapter '+c['topicId'],before==after)
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())};check('canonical original option 37',actual['MS_CS_1405_Q113']['options'][0]=='37')
for _,_,attrs,q in qs[:5]:
 item=actual[attrs['data-source-id']];p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/item['repoPath'];check('original PDF '+item['id'],hashlib.sha256(p.read_bytes()).hexdigest()==item['sourceSha256'])
report=dict(topicId='l_matrices',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='General derivations are complemented by exact symbolic and finite witnesses. Q31 has no fabricated unique literal key. No universal correctness or future-performance guarantee.')
(E/'l_matrices-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'checks':len(checks),'status':report['status']})
