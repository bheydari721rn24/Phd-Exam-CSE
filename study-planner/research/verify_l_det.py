from pathlib import Path
import sympy as S,json,re,hashlib,subprocess,xml.etree.ElementTree as ET,sys,random
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_det-evidence';sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
checks=[]
def ck(n,a,b):
 assert S.simplify(a-b)==0,(n,a,b);checks.append(dict(name=n,result=str(a),status='passed'))
A=S.Matrix([[1,-3,2],[0,7,1],[-5,1,3]]);ck('Q1 minor',A.minor_submatrix(1,2).det(),-14);ck('Q1 determinant',A.det(),105)
K=S.Matrix([[0,1,0,1],[1,1,2,3],[1,0,3,1],[0,2,3,1]]);ck('Q2 elimination',K.det(),-2)
M=S.Matrix([[2,4,2],[3,2,1],[2,0,1]]);ck('Q3 sparse',M.det(),-8);ck('Q4 parity product',-A[0,2]*A[1,1]*A[2,0],70)
ck('Q5 counterexample',S.Matrix([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]]).det(),-1)
ck('Q6 scaling',2**5*-3,-96);ck('Q6 inverse',S.Rational(1,9),S.Rational(1,(-3)**2));ck('Q7 ledger',S.Rational(-48,-3),16)
ck('Q8 row mixing',S.Matrix([[1,1,0],[1,-1,0],[0,0,2]]).det(),-4)
ck('Q10 zero initial pivot',S.Matrix([[0,2,1],[3,0,4],[1,5,0]]).det(),23);ck('Q11 anti-diagonal',S.Matrix([[0,0,0,2],[0,0,3,0],[0,5,0,0],[7,0,0,0]]).det(),210)
ck('Q14 sensitivity',M.cofactor(2,0),0);h,k=S.symbols('h k');ck('Q15 cross term',S.Matrix([[2+h,1],[3,4+k]]).det(),5+4*h+2*k+h*k)
N=S.Matrix([[2,1],[3,4]]);ck('Q16 inverse identity',(N*N.adjugate())[0,0],5);ck('Q16 off-diagonal',(N*N.adjugate())[0,1],0)
ck('Q20 scaling adjugate',3**4*2**3,648);ck('Q21 x',N.inv()[0,:].dot(S.Matrix([5,6])),S.Rational(14,5));ck('Q21 y',N.inv()[1,:].dot(S.Matrix([5,6])),S.Rational(-3,5))
t=S.symbols('t');ck('Q24 family',S.Matrix([[t,1],[t*t,t]]).det(),0)
u=S.Matrix([1,2,-1]);v=S.Matrix([2,-1,3]);ck('Q25 update',(S.eye(3)+t*u*v.T).det(),1-3*t);ck('Q26 singular update',S.diag(1,2,12).det(),24)
ck('Q28 Schur',S.Matrix([[2,0,1],[0,3,2],[4,5,6]]).det(),4);ck('Q29 swap blocks',S.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]).det(),1)
b=S.Matrix([[1,1],[0,1]]);c=S.diag(1,2);ee=S.Matrix([[0,0],[1,0]]);d=S.eye(2);full=b.row_join(c).col_join(ee.row_join(d));ck('Q30 actual block',full.det(),3);ck('Q30 invalid expression',(b*d-ee*c).det(),2)
ck('Q31 Vandermonde',S.Matrix([[x**j for j in range(3)]for x in [1,3,2]]).det(),-2)
for n in range(1,13):
 tri=S.zeros(n)
 for i in range(n):
  tri[i,i]=1
  if i:tri[i,i-1]=tri[i-1,i]=1
 ck('Q33 recurrence order '+str(n),tri.det(),[1,1,0,-1,-1,0][n%6])
for n in range(1,10):
 lap=S.zeros(n)
 for i in range(n):
  lap[i,i]=2
  if i:lap[i,i-1]=lap[i-1,i]=-1
 ck('Q34 Laplacian '+str(n),lap.det(),n+1)
ck('Q35 variable bands',S.Matrix([[2,1,0,0],[4,3,2,0],[0,1,4,3],[0,0,2,5]]).det(),8)
ck('Q36 area',S.Matrix([[2,-1],[1,3]]).det(),7);ck('Q37 translated triangle',S.Matrix([[3,1],[1,4]]).det(),11)
U=S.Matrix([[1,0],[0,2],[1,1]]);ck('Q38 Gram',(U.T*U).det(),9)
X=S.Matrix([[1,2,0],[0,1,3]]);Y=S.Matrix([[2,1],[1,0],[0,1]]);ck('Q39 rectangular product',(X*Y).det(),11)
u=S.Matrix([S.Rational(3,5),S.Rational(4,5)]);H=S.eye(2)-2*u*u.T;ck('Q42 reflection',H.det(),-1);ck('Q42 entry',H[0,0],S.Rational(7,25))
ck('Q46 interval polynomial',S.Matrix([[2,t],[t,3]]).det(),6-t*t);ck('Q48 defective',S.Matrix([[2,1,0],[0,2,1],[0,0,2]]).det(),8)
ck('Q51 derivative',S.diff(S.Matrix([[t,1],[0,t]]).det(),t),2*t)
U=S.Matrix([[1,0],[0,1],[1,1]]);V=S.Matrix([[1,2,0],[0,1,3]]);ck('Q54 smaller update',(S.eye(2)+V*U).det(),4);ck('Q54 larger update',(S.eye(3)+U*V).det(),4)
ck('Q55 row-sum family',((t-3)*S.eye(4)+S.ones(4)/4).det(),(t-2)*(t-3)**3)
ck('Q57 commutator',S.Matrix([[0,1],[-1,0]]).det(),1);ck('Q60 bilinear',(S.Matrix([1,S.I]).T*S.Matrix([1,S.I]))[0,0],0);ck('Q60 Hermitian',(S.Matrix([1,S.I]).H*S.Matrix([1,S.I]))[0,0],2)
ck('Q62 low-rank update',(S.diag(0,0,3,4)+t*S.ones(4)).det(),0);ck('Q63 repair',(S.diag(0,2,3,4)+5*S.ones(4)).det(),120)
ck('Q67 singular family',S.Matrix([[1,2],[2,t]]).det(),t-4);ck('Q68 product',S.Rational(1,2)*(-3)**2*2,9)
ck('Q70 Schur boundary',S.Matrix([[t,0,1],[0,2,0],[1,0,3]]).det(),6*t-2);ck('Q73 LU',-2*3*-4*5,120)
ck('Q75 positivity determinant',((1-t)*S.eye(3)+t*S.ones(3)).det(),(1-t)**2*(1+2*t));ck('Q76 polynomial',(1+2*t)*(1-t)*(1+3*t),1+4*t+t*t-6*t**3)
ck('Q80 mixed',((t-1)*S.eye(3)+S.ones(3)).det(),(t-1)**2*(t+2))
ck('Authentic PhD Q32 determinant',((1-t)*S.eye(3)+t*S.ones(3)).det(),(1-t)**2*(1+2*t));ck('Authentic MSc Q44',S.Matrix([[1,1,0],[0,2,2],[0,0,3]]).det(),6)
# Recompute every saved mathematical model state independently of its drawing.
data=json.loads((R/'dist/chapters/l_det-models.json').read_text());total=0
for m in data['models']:
 for f in m['frames']:
  s=f['snapshot'];assert f['teaching']['currentState']==s
  if 'matrix'in s:
   A=S.Matrix(s['matrix'])
   if m['kind']=='permutation-term-grid':
    p=s['permutation'];inv=sum(p[i]>p[j]for i in range(3)for j in range(i+1,3));assert inv==s['inversions'];ck(m['id']+' term',(-1)**inv*S.prod(A[i,p[i]]for i in range(3)),S.sympify(s['term']))
   elif m['kind']=='cofactor-deletion':ck(m['id']+' cofactor',A.cofactor(s['row'],s['column']),S.sympify(s['cofactor']))
   elif m['kind']=='adjugate-product-grid':ck(m['id']+' product entry',(A*S.Matrix(s['adjugate']))[s['i'],s['j']],S.sympify(s['entry']))
   elif m['kind']=='rank-one-selected-column-expansion':ck(m['id']+' one-column term',A.det(),S.sympify(s['term']))
   elif m['kind']=='gram-minor-area':ck(m['id']+' squared minor',S.Matrix(s['minor']).det()**2,S.sympify(s['contribution']))
   else:ck(m['id']+' determinant',A.det(),S.sympify(s.get('determinant',s.get('numerator'))))
   if m['kind']=='row-operation-matrix-ledger':ck(m['id']+' ledger',A.det(),s['factor']*S.Matrix(s['original']).det())
  elif m['kind']=='oriented-triangle-translation':
   p0,p1,p2=[S.Matrix(p)for p in s['vertices']];D=(p1-p0).row_join(p2-p0).det();ck(m['id']+' edge determinant',D,11);ck(m['id']+' area',abs(D)/2,S.sympify(s['area']))
  elif m['kind']in['diagonal-subspace-volume','quadratic-form-direction-factors']:ck(m['id']+' factors',S.sympify(s['line'])*S.sympify(s['plane'])**2,S.sympify(s['determinant']))
  elif m['kind']=='continuant-recurrence-plot':
   ds=list(map(S.sympify,s['prefix']));assert ds[:2]==[1,1][:len(ds)];assert all(ds[i]==ds[i-1]-ds[i-2]for i in range(2,len(ds)))
  root=ET.fromstring(f['formulaHtml']);assert not closing_script_bases(root)and not delimiter_issues(root);total+=1
prior=json.loads((E/'prior-library.json').read_text());assert prior['chapterCount']==41 and prior['questionCount']==2593
for c in prior['chapters']:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']
html=(R/'dist/chapters/l_det.html').read_text(encoding='utf-8');qs=json.loads((B/'l_det-questions.json').read_text());auth=json.loads((B/'l_det-authentic.json').read_text());assert len(qs)==80 and html.count('class="exam-question"')==82 and html.count('class="review-rule"')==80 and not re.search('[\u0600-\u06ff]',html)and '$'not in html
formulaCount=0
for raw in re.findall(r'<math\b[\s\S]*?</math>',html):
 root=ET.fromstring(raw);assert not closing_script_bases(root)and not delimiter_issues(root);formulaCount+=1
for a in json.loads((E/'acquisition.json').read_text()):
 if 'cachePath'in a:assert hashlib.sha256(Path(a['cachePath']).read_bytes()).hexdigest()==a['sha256']
for q in auth:
 path=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q['repoPath'];assert hashlib.sha256(path.read_bytes()).hexdigest()==q['sourceSha256']
# Editable exact rational engine, independently compared with SymPy on random integer inputs.
rng=random.Random(79);inputs=[[[0,1],[1,0]],[[1,2],[2,4]],[[0,1,0,1],[1,1,2,3],[1,0,3,1],[0,2,3,1]]]+[[[rng.randrange(-5,6)for _ in range(n)]for _ in range(n)]for n in[2,3,4]for j in range(12)]
script="const a=require(process.argv[1]);const xs=JSON.parse(process.argv[2]);process.stdout.write(JSON.stringify(xs.map(x=>a.elimination(x))));"
out=json.loads(subprocess.check_output(['node','-e',script,str(R/'dist/chapters/l_det.js'),json.dumps(inputs)],text=True,encoding='utf-8'))
for A,m in zip(inputs,out):
 expected=S.Matrix(A).det();assert S.sympify(m['result']['determinant'])==expected
 for f in m['frames']:
  s=f['snapshot'];ck('Editable exact frame',S.Matrix(s['matrix']).det(),S.sympify(s['factor'])*expected)
for name,obj in [('mathematics',dict(status='passed',exactChecks=len(checks),checks=checks,editableInputs=len(inputs),authenticAnswers='independently derived, not official keys')),('models',dict(status='passed',models=len(data['models']),checkpoints=total,independentlyRecomputedStates=total)),('lesson-and-retention',dict(status='passed',sections=(B/'l_det.en.md').read_text(encoding='utf-8').count('\n## '),lessonWords=len(re.findall(r'\b\w+\b',(B/'l_det.en.md').read_text(encoding='utf-8'))),questions=82,originalQuestions=80,rules=80,mathElements=formulaCount,previousChapters=41,previousQuestions=2593,allPreviousHtmlHashesUnchanged=True,solutionWordCounts=[len(re.findall(r'\b\w+\b',x['solution']))for x in qs]))]:
 (E/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
print(len(checks),'exact checks;',total,'model checkpoints;',formulaCount,'MathML expressions; 41 previous chapters unchanged.')
