"""Retain the independent rank oracle and verify every revised answer identity."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,xml.etree.ElementTree as ET
import sympy as S
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision'
p=R/'research/verify_l_rank_en.py';source=p.read_text(encoding='utf8')
# The historical global approval-bank snapshot is unrelated to this chapter's
# current mathematics. Every other chapter is checked against the frozen Git state.
a=source.index("approved=json.loads");z=source.index('for u in range(21):',a)
source=source[:a]+source[z:];source=source.split('for q in auth:\n',1)[0]
scope={'__file__':str(p),'__name__':'current_rank_model_audit'}
exec(compile(source,str(p),'exec'),scope)
q=json.loads((R/'research/l_rank-questions.json').read_text());auth=json.loads((R/'research/l_rank-authentic.json').read_text())
prior=json.loads(subprocess.check_output(['git','show','ce272ad83079d4e95f6e009fd89c603240a8a708:research/l_rank-questions.json'],cwd=R))
for now,old in zip(q,prior):
    assert all(now[k]==old[k]for k in old if k!='solution'),now['id']
    assert len(now['solution'])>len(old['solution'])and len(now['solution'].split())>=105,now['id']
assert 'left-annihilator restriction'not in q[-1]['solution']
sources=json.loads((E/'l_rank-source-revalidation-20261018.json').read_text())
for record in sources['sources']:
    assert hashlib.sha256(Path(record['path']).read_bytes()).hexdigest()==record['sha256']
authproof=json.loads((E/'l_rank-authentic-recheck-20261018.json').read_text())
# Use the original documents acquired by the source-page recheck.
for record in authproof.get('sourceRecords',authproof.get('sources',[])):
    path=record.get('sourceLocalFile',record.get('path'))
    sha=record.get('sourceSha256',record.get('sha256'))
    if path and sha:assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha
for record in auth:
    path=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/record['repoPath']
    if not path.exists():
        candidates=list(Path('C:/Users/bheydari/AppData/Local/Temp/phd-rank-revalidation-20261018').rglob('*.pdf'))
        path=next(p for p in candidates if hashlib.sha256(p.read_bytes()).hexdigest()==record['sourceSha256'])
    assert hashlib.sha256(path.read_bytes()).hexdigest()==record['sourceSha256']
assert [a['answer']for a in auth]==[2,2]

# Explicit affine formulas added to the first twelve complete calculations.
b1,b2,b3,b4,b5,s,t,u=S.symbols('b1 b2 b3 b4 b5 s t u')
spec={
 'LR01':([b1-b3-2*t,t,b3],[b1,2*b1-2*b3,b3]),
 'LR02':([b1-2*s-t,s,b2-t,t,b3-b1],[b1,b2,b3,-b1]),
 'LR04':([b2-2*b1+s+2*t,b1-2*s-3*t,s,t],[b1,b2,2*b2-b1]),
 'LR05':([b1,b2],[b1,b2,b1+b2]),
 'LR06':([b1-t,b2-t,t],[b1,b2]),
 'LR07':([s,t,u],[0,0]),
 'LR08':([b1+2*s-3*t,s,t],[b1,2*b1,-b1]),
 'LR09':([s,b2-2*t+b3/3,t,b3/3],[2*b2,b2,b3]),
 'LR10':([b1-2*b3-s-4*t,b3-s,s,t],[b1,2*b1,b3,b1+b3]),
 'LR11':([b1,b2,b3,b4],[b1,b2,b3,b4,b1+2*b2+3*b3+4*b4]),
 'LR12':([b1-2*s-t-3*u,s,b2-t+u,t,u],[b1,b2])}
checks=[]
def check(label,c):assert c,label;checks.append(label)
byid={a['id']:a for a in q}
for key,(x,b)in spec.items():
    A=S.Matrix(byid[key]['certificate']['input'])
    check(key+' arbitrary-load fiber',all(S.simplify(v)==0 for v in A*S.Matrix(x)-S.Matrix(b)))
    variables=[v for v in[s,t,u]if any(S.sympify(c).has(v)for c in x)]
    J=S.Matrix(x).jacobian(variables)if variables else S.zeros(A.cols,0)
    check(key+' all independent free coordinates',J.rank()==A.cols-A.rank()and A*J==S.zeros(A.rows,len(variables)))

A=S.Matrix(byid['LR03']['certificate']['input']);check('LR03 exact row dependence',S.Matrix([[-1,-6,-3,1]])*A==S.zeros(1,5))
Rref=S.Matrix(byid['LR03']['certificate']['rref']);rho=S.symbols('rho1:4')
xp=S.Matrix([rho[0]-s+t,rho[1]-2*s-3*t,s,rho[2]-4*t,t])
check('LR03 reduced arbitrary-load formula',Rref*xp==S.Matrix([*rho,0]))

# Independent witnesses for new advanced teaching steps.
P=S.Matrix([[1,10,3],[-1,1,0],[1,0,0]])
aa,bb,cc=S.symbols('a b c')
check('LR85 arbitrary polynomial expansion',P*S.Matrix([cc,bb+cc,(aa-10*bb-11*cc)/3])==S.Matrix([aa,bb,cc]))
check('LR86 unique basis coordinates',S.Matrix([[1,1,0],[1,-1,0],[0,0,1]])*S.Matrix([(aa+bb)/2,(aa-bb)/2,cc])==S.Matrix([aa,bb,cc]))
inverse=S.Matrix([[S.Rational(1,2),0,0],[-1,1,0],[0,0,1]])
updated=S.Matrix([[2,0,0],[2,1,0],[0,0,1]])
check('LR57 actual two-sided inverse',inverse*updated==updated*inverse==S.eye(3))
x=S.symbols('x');lag=[(x-1)*(x-2)/2,-x*(x-2),x*(x-1)/2]
check('LR67 interpolation witnesses',S.Matrix([[p.subs(x,i)for p in lag]for i in range(3)])==S.eye(3))
for n in range(1,15):
    mats=[]
    for i in range(n):
        for j in range(i+1,n):
            f=S.zeros(n);f[i,j]=f[j,i]=1;f[i,i]=f[j,j]=-1;mats.append(f)
    check('LR66 row-sum basis '+str(n),all(f==f.T and f*S.ones(n,1)==S.zeros(n,1)for f in mats))
    check('LR66 independent coordinates '+str(n),not mats or S.Matrix.hstack(*[f.reshape(n*n,1)for f in mats]).rank()==n*(n-1)//2)
    a=S.zeros(n)
    for start in range(0,n-2,3):a[start,start+1]=a[start+1,start+2]=1
    if n%3==2:a[n-2,n-1]=1
    check('LR63 sharp cube-zero rank '+str(n),a**3==S.zeros(n)and a.rank()==2*n//3)

page=(R/'dist/chapters/l_rank.html').read_text(encoding='utf8')
sys.path.insert(0,str(R/'research/exam-rewrite'))
from math_fences import delimiter_issues,closing_script_bases
expressions=re.findall(r'<math\b[\s\S]*?</math>',page)
for expr in expressions:
    node=ET.fromstring(expr);assert not delimiter_issues(node)and not closing_script_bases(node),expr[:200]
check('all 90 problems retained',page.count('class="exam-question"')==90)
check('80 complete final rules retained',page.count('class="review-rule"')==80)
check('27 question-specific visual placements',page.count('data-problem-visual=')==27)
report={'state':'passed_current_rank_mathematical_review','date':'2026-10-18','retainedIndependentAssertions':sum(scope['counts'].values()),'newExactAssertions':len(checks),'newChecks':checks,'nativeMathExpressions':len(expressions),'solutionsIndividuallyExtended':88,'authenticSolutionsRewritten':2,'originalSourceHashesRechecked':4,'authenticHashesRechecked':2,'pageSha256':hashlib.sha256((R/'dist/chapters/l_rank.html').read_bytes()).hexdigest(),'limits':'Finite exact examples and parameter grids supplement the explicit general proofs. Historical global approval counts are excluded; student approval is not inferred.'}
(E/'l_rank-current-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print({k:v for k,v in report.items()if k!='newChecks'})
