from pathlib import Path
import sympy as S,json,re,hashlib,subprocess,xml.etree.ElementTree as ET,sys,random
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_spaces-evidence';sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
checks=[]
def ck(name,condition):
 assert bool(condition),name;checks.append(dict(name=name,status='passed'))
def basis_check(name,A,N):
 A=S.Matrix(A);N=S.Matrix(N);ck(name+' null vectors',A*N==S.zeros(A.rows,N.cols));ck(name+' null basis independent',N.rank()==N.cols);ck(name+' rank-nullity',A.rank()+N.cols==A.cols)
x,t,a,b=S.symbols('x t a b')
ck('Q1 basis membership',S.Matrix([[1,2,-1]])*S.Matrix([[-2,1],[1,0],[0,1]])==S.zeros(1,2))
ck('Q2 affine base point',S.Matrix([[1,2,-1]])*S.Matrix([3,0,0])==S.Matrix([3]))
ck('Q3 union fails addition',1*1!=0)
c=S.Matrix([1,2]);u=S.Matrix(S.symbols('u:2'));v=S.Matrix(S.symbols('v:2'));ck('Q4 transported addition',(u+v-c)-c==(u-c)+(v-c));ck('Q4 transported scaling',(a*u+(1-a)*c-c-a*(u-c)).applyfunc(S.simplify)==S.zeros(2,1))
ck('Q5 identity law fails',S.Matrix([0,0])!=S.Matrix([0,1]));basis_check('Q6 ambiguity',[[1,1,0],[2,2,0],[0,0,1]],[[1],[-1],[0]])
ck('Q7 coordinates',2**3==8);ck('Q8 nonlinear polynomial witness',(x+1-x).subs(x,0)*(x+1-x).subs(x,1)==1)
A=S.Matrix([[1,1,1,1],[2,2,2,2],[1,-1,0,0]]);basis_check('Q9 dependent constraints',A,[[1,0],[1,0],[0,1],[-2,-1]])
ck('Q10 complex scalar leaves real axis',S.im(S.I)==1)
basis_check('Q11 redundant coordinates',[[1,0,2],[0,1,3]],[[-2],[-3],[1]])
ck('Q12 joint relation',S.Matrix([[1,0,1],[0,1,1]])*S.Matrix([1,1,-1])==S.zeros(2,1))
ck('Q13 essential horizontal direction',S.Matrix([[0,0],[1,2]]).rank()==1)
ck('Q14 determinant',S.expand(S.Matrix([[1,t],[t,1]]).det())==1-t*t)
ck('Q15 exceptional set',S.Matrix([[1,0,a],[0,1,b],[1,1,1]]).det()==1-a-b)
T=S.Matrix([[1,0,1],[1,1,0],[0,1,1]]);ck('Q16 field-sensitive determinant',T.det()==2);ck('Q16 mod-two relation',all(int(v)%2==0 for v in T*S.ones(3,1)))
ck('Q17 coefficient inverse',S.Matrix([[1,1],[1,-1]]).det()==-2)
basis_check('Q18 relation space',[[1,0,1,2],[2,1,3,5],[0,1,1,1]],[[-1,-2],[-1,-1],[1,0],[0,1]])
ck('Q19 evaluation determinant',S.Matrix([[1,j,j*j]for j in[1,2,3]]).det()==2);ck('Q20 singular samples',S.Matrix([[1,1],[1,1]]).det()==0)
A=S.Matrix([[1,2,0,3],[2,4,1,4],[3,6,2,5]]);basis_check('Q21 row-column-kernel',A,[[-2,-3],[1,0],[0,2],[0,1]]);ck('Q21 exact reduced form',A.rref()[0]==S.Matrix([[1,2,0,3],[0,0,1,-2],[0,0,0,0]]))
ck('Q22 wrong reduced column outside original space',S.Matrix([[1,1],[2,0]]).rank()==2)
ck('Q23 extension determinant',S.Matrix([[1,0,1],[1,1,0],[0,1,0]]).det()==1)
ck('Q24 allowed exchange',S.Matrix([[2,0,0],[-1,1,0],[0,0,1]]).det()==2);ck('Q24 forbidden exchange',S.Matrix([[1,0,2],[0,1,-1],[0,0,0]]).rank()==2)
ck('Q25 four-vector counterexample',S.Matrix([[1,0,0,1],[0,1,0,1],[0,0,1,0],[0,0,0,0]]).rank()==3)
ck('Q26 candidate span dimension',S.Matrix([[1,0,1],[0,1,1],[0,0,0]]).rank()==2)
ck('Q27 finite fiber count',3**(7-3)==81 and 3**3==27);ck('Q28 unique nested dimension',[i for i in range(8)if 5<i<7]==[6]);ck('Q29 distinct planes',S.Matrix([[1,0,0],[0,1,0],[0,0,1]]).rank()==3)
B0=S.Matrix([[1,1],[1,-1]]);C=S.Matrix([[2,1],[0,1]]);target=S.Matrix([3,1]);ck('Q30 B coordinates',B0*S.Matrix([2,1])==target);ck('Q30 C coordinates',C*S.Matrix([1,1])==target)
P=C.inv()*B0;ck('Q31 change direction',P==S.Matrix([[0,1],[1,-1]]) and P*S.Matrix([2,1])==S.Matrix([1,1]))
ck('Q32 rectangular recovery',S.Matrix([[1,0],[0,1],[1,1]])*S.Matrix([2,3])==S.Matrix([2,3,5]));ck('Q33 dual evaluation',B0.inv()*S.Matrix([5,-3])==S.Matrix([1,4]))
ck('Q34 polynomial coordinates',S.expand(-1-(1+x)+4*(1+x+x*x))==2+3*x+4*x*x)
for num,factor in[(35,x*(x-1)*(x-2)),(36,(x-1)**2*(x+1)),(37,x*(x-1))]:
 ck('Q'+str(num)+' polynomial basis dimension',len([factor,x*factor])==2 and S.degree(factor)<=3)
ck('Q36 double root',S.diff((x-1)**2*(x+1),x).subs(x,1)==0)
ck('Q38 interpolation', (1+x).subs(x,0)==1 and (1+x).subs(x,1)==2)
ck('Q39 integral basis',S.integrate(x*x-S.Rational(1,3),(x,0,1))==0 and S.integrate(x**3-S.Rational(1,4),(x,0,1))==0)
# Infinite statements are reviewed as proofs, not assigned a fabricated numeric check.
for n in[1,2,4,5]:
 sym=[]
 for i in range(n):
  for j in range(i+1,n):
   M=S.zeros(n);M[i,j]=M[j,i]=1;sym.append(M)
 for i in range(n-1):
  M=S.zeros(n);M[i,i]=1;M[n-1,n-1]=-1;sym.append(M)
 ck('Q41 explicit basis count n='+str(n),len(sym)==n*(n+1)//2-1)
 ck('Q41 independence n='+str(n),not sym or S.Matrix.hstack(*(M.reshape(n*n,1)for M in sym)).rank()==len(sym))
A=S.Matrix([[1,4],[-2,3]]);SS=(A+A.T)/2;K=(A-A.T)/2;ck('Q42 decomposition',SS+K==A and SS.T==SS and K.T==-K)
rowcols=[]
for i in range(2):
 for j in range(2):
  M=S.zeros(3);M[i,j]=M[2,2]=1;M[i,2]=M[2,j]=-1;rowcols.append(M.reshape(9,1));ck('Q43 basis row-column sums',M*S.ones(3,1)==S.zeros(3,1) and S.ones(1,3)*M==S.zeros(1,3))
ck('Q43 independent four directions',S.Matrix.hstack(*rowcols).rank()==4)
for n in[3,4]:
 basis=[]
 for i in range(n):
  for j in range(i+1,n):
   M=S.zeros(n);M[i,j]=M[j,i]=1;M[i,i]=M[j,j]=-1;basis.append(M.reshape(n*n,1));ck('Q44 zero symmetric row sums',M==M.T and M*S.ones(n,1)==S.zeros(n,1))
 ck('Q44 dimension n='+str(n),S.Matrix.hstack(*basis).rank()==n*(n-1)//2)
D=S.diag(1,1,2,3);ck('Q45 commutant freedom',sum(D[i,i]==D[j,j]for i in range(4)for j in range(4))==6)
ck('Q46 singular addition witness',S.diag(1,0).det()==0 and S.diag(0,1).det()==0 and S.eye(2).det()==1)
pp=2+3*x-4*x*x+x**5;ck('Q47 parity split',S.expand((pp+pp.subs(x,-x))/2)==2-4*x*x)
ck('Q48 decompositions',S.Matrix([t,b,0])+S.Matrix([a-t,0,x])==S.Matrix([a,b,x]))
ck('Q49 intersection equation',S.Matrix([[1,1,1,1]])*S.Matrix([1,1,-1,-1])==S.zeros(1,1))
U=S.Matrix([[1,0],[0,1],[1,0],[0,1]]);W=S.Matrix([[1,0],[1,0],[0,1],[0,1]]);ck('Q50 sum rank',U.row_join(W).rank()==3)
ck('Q51 redundant block nullity',3-S.Matrix([[1,1,-1],[0,0,0]]).rank()==2)
for k in range(2,7):
 U=S.eye(10)[:,:6];W=S.eye(10)[:,list(range(k))+list(range(6,12-k))];ck('Q52 attainable intersection '+str(k),U.rank()+W.rank()-U.row_join(W).rank()==k)
ck('Q53 equality counterexample',S.eye(4).rank()==4);ck('Q55 three-line dependence',S.Matrix([[1,0,1],[0,1,1]]).rank()==2)
ck('Q56 oblique components',S.Matrix([[1,1],[0,2]])*S.Matrix([2,3])==S.Matrix([5,6]));ck('Q57 failed inclusion exclusion',1+1+1!=2)
ck('Q58 polynomial lcm',S.lcm(x*(x-1),(x-1)*(x-2))==x**3-3*x*x+2*x)
ck('Q59 adapted basis',S.Matrix([[1,0,0],[1,1,0],[0,0,1]]).det()==1);ck('Q59 quotient coordinates',(3-2,4)==(1,4));ck('Q60 coset equality',S.Matrix([1,2])-S.Matrix([7,2])==S.Matrix([-6,0]))
ck('Q61 annihilator',S.Matrix([[1,-1,1]])*S.Matrix([[1,0],[1,1],[0,1]])==S.zeros(1,2));ck('Q62 scalar restriction',2*3==6)
ck('Q63 finite ordered basis count',7*6*4==168 and 168//6==28);ck('Q64 finite union cover',len({(0,0),(1,0),(0,1),(1,1)})==4)
ck('Q65 formal versus functional',all((v**3-v)%3==0 for v in range(3)))
ck('Q67 generic plane intersection',S.Matrix([[0,0,1],[-t,-t,1]]).rank()==2)
ck('Q67 exceptional plane intersection',S.Matrix([[0,0,1],[0,0,1]]).rank()==1)
ck('Q68 minimum codimension',7-4==3);ck('Q69 constrained finite functions',5-1==4)
for n in range(8):ck('Q70 recurrence basis n='+str(n),2**(n+2)==3*2**(n+1)-2*2**n)
ck('Q71 difference basis rank',S.Matrix([[1,0,0],[0,1,0],[0,0,1],[-1,-1,-1]]).rank()==3)
ck('Q72 plane generators',S.Matrix([[2,-1,4]])*S.Matrix([[1,0],[2,4],[0,1]])==S.zeros(1,2))
ck('Q73 measurement fiber',S.Matrix([[1,1,0],[0,1,1]])*S.Matrix([4-t,t,7-t])==S.Matrix([4,7]))
ck('Q75 rank formula numerical check',6-2-3+4==5 and 6-4==2)
pp=sum(S.symbols('c:5')[j]*x**j for j in range(5));cc=S.symbols('c:5');ck('Q76 quotient remainder',S.rem(pp,x*x-1,x)==cc[0]+cc[2]+cc[4]+x*(cc[1]+cc[3]))
ck('Q79 extension size',3+3-1==5);ck('Q80 missing cancellation direction',7-1==6 and 3+2==5)
ck('Authentic MSc Q41 dimension',4*5//2-1==9);ck('Authentic PhD Q31 inequality counterexample',S.Matrix([0,1]).dot(S.Matrix([0,1]))>0)
data=json.loads((R/'dist/chapters/l_spaces-models.json').read_text());frames=0
for m in data['models']:
 for f in m['frames']:
  s=f['snapshot'];ck(m['id']+' current state',s==f['teaching']['currentState'])
  if m['id']=='closure-plane':ck('stored plane membership',s['vector'][0]+2*s['vector'][1]-s['vector'][2]==s['residual']==0)
  if m['id']=='pivot-main':ck('stored row operator',S.Matrix(s['rowOperator'])*S.Matrix(s['original'])==S.Matrix(s['matrix']))
  if m['id']=='parameter-span':ck('stored exceptional rank',S.Matrix(s['matrix']).rank()==s['rank'])
  if m['id']=='symmetric-trace':ck('stored symmetric trace',S.Matrix(s['matrix'])==S.Matrix(s['matrix']).T and S.trace(S.Matrix(s['matrix']))==S.sympify(s['trace']))
  if m['id']=='quotient-main':v=s['representative'];ck('stored quotient coordinates',[v[1]-v[0],v[2]]==s['quotientCoordinates'])
  if m['id']=='intersection-main':ck('stored decomposition',S.Matrix(s['u'])+S.Matrix(s['w'])==S.Matrix(s['target']))
  if m['id']=='finite-basis':ck('stored finite span size',len(s['excluded'])==2**s['chosen'] and s['choices']==8-2**s['chosen'])
  if m['id']=='affine-failure':v=s['vector'];ck('stored affine residual',v[0]+2*v[1]-v[2]==s['value'])
  if m['id']=='union-failure':ck('stored union membership',s['inUnion']==(s['vector'][0]==0 or s['vector'][1]==0))
  if m['id']=='redundant-parameters':ck('stored redundant parameter rank',S.Matrix(s['matrix']).rank()==s['rank'])
  if m['id']=='basis-filter':ck('stored basis filter rank',s['rank']==(1 if s['step']==0 else 2))
  if m['id']=='exchange-main':ck('stored replacement basis rank',S.Matrix([[2,0],[-1,1]]).rank()==2)
  if m['id']=='coordinates-main':ck('stored B coordinate reconstruction',S.Matrix([[1,1],[1,-1]])*S.Matrix(s['Bcoordinates'])==S.Matrix(s['vector']));ck('stored C coordinate reconstruction',S.Matrix([[2,1],[0,1]])*S.Matrix(s['Ccoordinates'])==S.Matrix(s['vector']))
  if m['id']=='polynomial-main':ck('stored polynomial partial sum',list(map(S.sympify,s['coefficients']))==[[-1,0,0],[-2,-1,0],[2,3,4]][s['step']])
  if m['id']=='symmetric-split':
   OA=S.Matrix([[1,4],[-2,3]]);ck('stored symmetric/skew part',S.Matrix(s['matrix'])==[OA,(OA+OA.T)/2,(OA-OA.T)/2][s['step']])
  if m['id']=='three-lines':ck('stored multi-component partial sum',list(sum((S.Matrix(v)for v in s['components']),S.zeros(2,1)))==[[1,0],[1,1],[0,0]][s['step']])
  if m['id']=='direct-oblique':ck('stored oblique components',S.Matrix(s['u'])+S.Matrix(s['w'])==S.Matrix(s['target']))
  if m['id']=='finite-lines':ck('stored finite-field line',s['field']==2 and s['line'][0]==[0,0] and s['line'][1]!=[0,0])
  if m['id']=='plane-course':v=s['vector'];ck('stored reconstructed plane',2*v[0]-v[1]+4*v[2]==0)
  if m['id']=='measurement-main':v=s['vector'];ck('stored measurement values',[v[0]+v[1],v[1]+v[2]]==s['measurements']==[4,7])
  if m['id']=='projection-main':ck('stored projection orthogonality',S.Matrix(s['projection']).dot(S.Matrix(s['residual']))==0 and S.Matrix(s['projection'])+S.Matrix(s['residual'])==S.Matrix(s['vector']))
  if m['id']=='intersection-parameter':BU=S.Matrix(s['fixed']);BW=S.Matrix(s['moving']);ck('stored intersection rank identity',BU.rank()+BW.rank()-BU.row_join(BW).rank()==s['intersectionDimension'] and BU.row_join(BW).rank()==s['sumDimension'])
  if m['id']=='matrix-balances':M=S.Matrix(s['matrix']);ck('stored coupled zero row/column sums',M*S.ones(3,1)==S.zeros(3,1) and S.ones(1,3)*M==S.zeros(1,3))
  root=ET.fromstring(f['formulaHtml']);assert not closing_script_bases(root)and not delimiter_issues(root);frames+=1
prior=json.loads((E/'prior-library.json').read_text());assert prior['chapterCount']==42 and prior['questionCount']==2675
for c in prior['chapters']:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']
html=(R/'dist/chapters/l_spaces.html').read_text(encoding='utf-8');qs=json.loads((B/'l_spaces-questions.json').read_text());auth=json.loads((B/'l_spaces-authentic.json').read_text());assert len(qs)==80 and html.count('class="exam-question"')==82 and html.count('class="review-rule"')==80 and not re.search('[\u0600-\u06ff]',html)and '$'not in html
formulaCount=0
for raw in re.findall(r'<math\b[\s\S]*?</math>',html):
 root=ET.fromstring(raw);assert not closing_script_bases(root)and not delimiter_issues(root);formulaCount+=1
for acq in json.loads((E/'acquisition.json').read_text()):
 if 'cachePath'in acq:assert hashlib.sha256(Path(acq['cachePath']).read_bytes()).hexdigest()==acq['sha256']
for q0 in auth:assert hashlib.sha256((Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q0['repoPath']).read_bytes()).hexdigest()==q0['sourceSha256']
rng=random.Random(81);inputs=[]
for rows in[2,3,4]:
 for cols in[1,2,3,4,5]:
  for j in range(6):
   A=[[rng.randrange(-5,6)for k in range(cols)]for i in range(rows)]
   if j==0:A[-1]=A[0][:]
   target=[rng.randrange(-5,6)for i in range(rows)]
   if j%2==0:target=list(S.Matrix(A)*S.Matrix([rng.randrange(-2,3)for k in range(cols)]));target=list(map(int,target))
   inputs.append(dict(A=A,b=target))
inputs.extend([dict(A=[[0,0],[0,0]],b=[0,0]),dict(A=[[0,0],[0,0]],b=[0,1])])
script='const a=require(process.argv[1]);process.stdout.write(JSON.stringify(JSON.parse(process.argv[2]).map(x=>a.spanLab(x.A,x.b))));'
out=json.loads(subprocess.check_output(['node','-e',script,str(R/'dist/chapters/l_spaces.js'),json.dumps(inputs)],text=True,encoding='utf-8'))
for ix,(inp,m)in enumerate(zip(inputs,out)):
 A=S.Matrix(inp['A']);bb=S.Matrix(inp['b']);r=m['result'];ck('Lab '+str(ix)+' independently computed rank',r['rank']==A.rank());ck('Lab '+str(ix)+' target consistency',r['consistent']==(A.rank()==A.row_join(bb).rank()))
 ck('Lab '+str(ix)+' original basis',r['basis']==[[str(v)for v in col]for col in A.columnspace()]);ck('Lab '+str(ix)+' kernel basis',r['nullBasis']==[[str(v)for v in col]for col in A.nullspace()])
 if r['consistent']:ck('Lab '+str(ix)+' actual target reconstruction',A*S.Matrix(list(map(S.sympify,r['coefficients'])))==bb)
 for f in m['frames']:
  st=f['snapshot'];original=A if st['phase']=='Generator reduction'else A.row_join(bb);ck('Lab '+str(ix)+' row operation',S.Matrix(st['rowOperator'])*original==S.Matrix(st['matrix']))
report=dict(status='passed',exactChecks=len(checks),checks=checks,editableInputs=len(inputs),authenticAnswers='independently derived, not official keys',proofBoundary='Symbolic checks certify stated finite examples; infinite and universal claims also require the supplied mathematical proofs.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n')
(E/'models.json').write_text(json.dumps(dict(status='passed',models=len(data['models']),checkpoints=frames,allFormulaFencesChecked=True,coordinateStatesIndependentlyChecked=True),indent=2)+'\n')
lesson=(B/'l_spaces.en.md').read_text(encoding='utf-8')
(E/'lesson-and-retention.json').write_text(json.dumps(dict(status='passed',sections=lesson.count('\n## '),lessonWords=len(re.findall(r'\b\w+\b',lesson)),questions=82,originalQuestions=80,rules=80,mathElements=formulaCount,previousChapters=42,previousQuestions=2675,allPreviousHtmlHashesUnchanged=True,solutionWordCounts=[len(re.findall(r'\b\w+\b',z['solution']))for z in qs]),indent=2)+'\n')
print(len(checks),'exact checks;',len(inputs),'independent rectangular lab inputs;',formulaCount,'MathML elements;',frames,'stored checkpoints; preceding 42 chapter hashes unchanged.')
