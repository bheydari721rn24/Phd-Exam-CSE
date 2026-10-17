"""Independent checks for the LG13--LG25 solution manuscript, not a chapter gate."""
from pathlib import Path
from collections import Counter
from itertools import product
import hashlib, json, re, sys, xml.etree.ElementTree as ET
import sympy as S
from markdown_it import MarkdownIt

R = Path(__file__).resolve().parents[1]
P = R / 'research/deep-library-revision/l_gauss-answer-expansions.en.md'
counts = Counter()
def check(condition, kind):
    assert bool(condition), kind
    counts[kind] += 1

a, t, s = S.symbols('a t s', real=True)
A = S.Matrix([[1,0,1],[2,a,3],[-1,-a,a]])
b = S.Matrix([-5,-9,a*a])
x = S.Matrix([-a-3,3/a-1,a-2])
check((A*x-b).applyfunc(S.simplify)==S.zeros(3,1), 'LG13 generic residual')
check(A.subs(a,0).rank()<A.subs(a,0).row_join(b.subs(a,0)).rank(), 'LG13 zero contradiction')
xm = S.Matrix([-5-t,(t-1)/2,t])
check((A.subs(a,-2)*xm-b.subs(a,-2)).applyfunc(S.simplify)==S.zeros(3,1), 'LG13 minus two affine family')
check(A.subs(a,-2).nullspace()==[S.Matrix([-1,S.Rational(1,2),1])], 'LG13 complete one-direction family')

families = [
 ('LG14', S.Matrix([[1,1,1],[1,a,1],[1,1,a]]), S.Matrix([1,2,2]), S.Matrix([1-2/(a-1),1/(a-1),1/(a-1)]), {1:None}),
 ('LG15', S.Matrix([[1,1],[1,a]]), S.Matrix([1,a]), S.Matrix([0,1]), {1:S.Matrix([1-t,t])}),
 ('LG16', S.Matrix([[a,1],[a,a]]), S.Matrix([1,a]), S.Matrix([0,1]), {0:S.Matrix([t,1]),1:S.Matrix([1-t,t])}),
 ('LG17', S.Matrix([[1,1,0],[0,a-1,0],[0,0,a+1]]), S.Matrix([2,a*a-1,a-1]), S.Matrix([1-a,a+1,(a-1)/(a+1)]), {1:S.Matrix([2-t,t,0]),-1:None}),
]
grid = [S.Rational(i,j) for i in range(-6,7) for j in [1,2,3]]
for name,A,b,x,branches in families:
    check((A*x-b).applyfunc(S.simplify)==S.zeros(A.rows,1), name+' generic symbolic residual')
    for value in branches:
        aa,bb=A.subs(a,value),b.subs(a,value);sol=branches[value]
        if sol is None:
            check(aa.rank()<aa.row_join(bb).rank(),name+' exceptional incompatibility')
        else:
            check((aa*sol-bb).applyfunc(S.simplify)==S.zeros(A.rows,1),name+' exceptional residual')
            check(aa.cols-aa.rank()==1 and sol.diff(t)!=S.zeros(A.cols,1),name+' exceptional completeness')
    for value in grid:
        if value in branches: continue
        aa,bb=A.subs(a,value),b.subs(a,value)
        check(aa.det()!=0 and aa.inv()*bb==x.subs(a,value),name+' independent rational-grid solve')

A=S.Matrix([[1,2,-1],[2,4,-2],[3,6,-3]])
for v in product(range(-2,3),repeat=3):
    b=S.Matrix(v);compatible=(v[1]==2*v[0] and v[2]==3*v[0])
    check((A.rank()==A.row_join(b).rank())==compatible,'LG18 all small load classifications')
    if compatible:
        xx=S.Matrix([v[0]-2*s+t,s,t])
        check((A*xx-b)==S.zeros(3,1),'LG18 symbolic complete family')
for w in [S.Matrix([-2,1,0]),S.Matrix([-3,0,1])]:
    check(w.T*A==S.zeros(1,3),'LG18 left-null basis')
A=S.Matrix([[1,2,-1],[2,4,-2]]);w=S.Matrix([-2,1]);b=S.Matrix([1,3])
check(w.T*A==S.zeros(1,3) and (w.T*b)[0]==1,'LG19 exact impossibility certificate')
A=S.Matrix([[1,0],[0,1],[1,1]]);w=S.Matrix([-1,-1,1])
check(w.T*A==S.zeros(1,2),'LG20 left-null certificate')
for v in product(range(-2,3),repeat=3):
    b=S.Matrix(v);compatible=v[2]==v[0]+v[1]
    check((A.rank()==A.row_join(b).rank())==compatible,'LG20 all small load classifications')
    if compatible:check(A*S.Matrix(v[:2])==b and A.rank()==2,'LG20 unique compatible solution')
check([v for v in product(range(2),repeat=2) if sum(v)%2==0]==[(0,0),(1,1)],'LG21 full binary enumeration')
xp=S.Matrix([2,-1,0]);v=S.Matrix([1,2,-1]);xx=xp-S.Rational(1,2)*v
check(xx==S.Matrix([S.Rational(3,2),-2,S.Rational(1,2)]) and sum(xx)==0,'LG22 supplementary condition')
xx=S.Matrix([a,11-4*a-7*s,s,a-3+2*s])
A=S.Matrix([[1,0,2,-1],[0,1,-1,4]])
check(A*xx==S.Matrix([3,-1]),'LG23 inverse parameter map residual')
check(S.Matrix([[-2,1],[1,0]]).det()==-1,'LG23 invertible parameter map')
A=S.Matrix([[1,1],[1,2]]);e1=S.Matrix([[1,1],[0,1]]);e2=S.Matrix([[1,1],[0,2]])
check(A.rref()[0]==e1.rref()[0]==e2.rref()[0]==S.eye(2),'LG24 canonical completion')
check(e1!=e2 and e1.det()!=0 and e2.det()!=0,'LG24 distinct echelon witnesses')
for m,n in [(2,3),(3,4),(4,3),(3,3)]:
    for seed in range(12):
        A=S.Matrix(m,n,lambda i,j: ((seed+3)*(i+2)+(seed+1)*(j+1)**2+i*j)%7-3)
        _,pivots=A.rref()
        for j in range(n+1):
            check(A[:,:j].rank()==sum(p<j for p in pivots),'LG25 independent prefix-rank invariant')

text=P.read_text(encoding='utf8')
check(re.findall(r'^## (LG\d+)$',text,re.M)==['LG'+str(i) for i in range(13,26)],'thirteen exact existing identities')
sys.path.insert(0,str(R/'research/exam-rewrite'))
import mathml
from math_fences import delimiter_issues, closing_script_bases
mathml.wrap_display=lambda s:s
rendered=mathml.markdown_math(text,MarkdownIt('commonmark',{'html':True}).enable('table'))
expressions=re.findall(r'<math\b[\s\S]*?</math>',rendered)
for expression in expressions:
    node=ET.fromstring(expression)
    check(not delimiter_issues(node) and not closing_script_bases(node),'native mathematical expression structure')
report={'state':'passed_expanded_answer_manuscript_checks','date':'2026-10-17','ids':['LG'+str(i) for i in range(13,26)],'assertions':sum(counts.values()),'byKind':dict(counts),'nativeMathExpressions':len(expressions),'words':len(text.split()),'sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'integratedIntoChapter':False,'individualChapterReviewComplete':False,'limits':'Exact and bounded checks supplement the written proofs. Four-course revalidation, remaining answer expansions, integration and final presentation audit are pending; no library completion count changes.'}
(P.parent/'l_gauss-expanded-answer-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items() if k not in ['byKind','limits']})
