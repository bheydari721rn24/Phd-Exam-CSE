from pathlib import Path
import hashlib,json,re,sys
import sympy as s
from xml.etree import ElementTree as ET
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'research/exam-rewrite'));import mathml
mathml.wrap_display=lambda x:x;checks=[]
def ck(label,value):assert value,label;checks.append(label)
A=s.Matrix([[1,0],[0,1],[1,1]]);b=s.Matrix([2,1,0]);P=A*(A.T*A).inv()*A.T;ck('Plane matrix',P==s.Matrix([[2,-1,1],[-1,2,1],[1,1,2]])/3);ck('Plane point and residual',P*b==s.Matrix([1,0,1])and((s.eye(3)-P)*b).dot((s.eye(3)-P)*b)==3)
A=s.Matrix([[1,2],[2,4],[0,0]]);b=s.Matrix([2,1,3]);ck('Dependent minimum norm',A.pinv()*b==s.Matrix([s.Rational(4,25),s.Rational(8,25)]));r=b-A*A.pinv()*b;ck('Dependent residual energy',r.dot(r)==s.Rational(54,5))
u=s.Matrix([1,2]);B=u*u.T;a=s.symbols('a',real=True);ck('Scale equation',B*B==5*B and s.solve(5*a*a-a,a)==[0,s.Rational(1,5)])
u=s.Matrix([1,1]);W=s.diag(1,4);P=u*(u.T*W*u).inv()*u.T*W;b=s.Matrix([2,-1]);p=P*b;r=b-p;ck('Weighted point',p==s.Matrix([-s.Rational(2,5),-s.Rational(2,5)]));ck('Weighted geometry',P.T*W==W*P and P*P==P and(u.T*W*r)[0]==0);ck('Weighted energy',(p.T*W*p)[0]==s.Rational(4,5)and(r.T*W*r)[0]==s.Rational(36,5))
n=s.Matrix([1,2,-1]);b=s.Matrix([3,1,0]);p=b-n*(n.dot(b)-3)/n.dot(n);ck('Affine plane',p==s.Matrix([s.Rational(8,3),s.Rational(1,3),s.Rational(1,3)])and n.dot(p)==3 and(b-p).dot(b-p)==s.Rational(2,3))
P=s.diag(1,1,0);Q=s.diag(0,1,1);ck('Commuting ranges',P*Q==s.diag(0,1,0)and P+Q-P*Q==s.eye(3));ck('Plain sum fails',(P+Q)**2!=P+Q)
P=s.diag(1,0);Q=s.ones(2)/2;M=P*Q;ck('Noncommuting trace',M*M==M/2 and P*Q!=Q*P and s.trace(M)==s.Rational(1,2));ck('Frobenius distance',sum(x*x for x in(P-Q))==1)
u=s.Matrix([1,s.I]);b=s.Matrix([1,1]);P=u*(u.conjugate().T*u).inv()*u.conjugate().T;p=P*b;r=b-p;ck('Complex projection',p==s.Matrix([(1-s.I)/2,(1+s.I)/2])and u.dot(u)==0);ck('Complex orthogonality',s.simplify((u.conjugate().T*r)[0])==0 and s.simplify((p.conjugate().T*p)[0])==1 and s.simplify((r.conjugate().T*r)[0])==1)
for t in[-s.Rational(1,2),s.Rational(1,2)]:
 P=s.Matrix([[1,0,0],[0,s.Rational(1,2),t],[0,t,s.Rational(1,2)]]);ck('Diagonal candidate '+str(t),P.T==P and P*P==P and P.rank()==2)
t=s.symbols('t',real=True);E=s.Matrix([[1,t],[0,0]]);ck('Oblique idempotence',E*E==E);ck('Oblique squared singular values',(E*E.T).eigenvals()=={t*t+1:1,0:1})
text=(R/'research/l_projection-worked-bank.en.md').read_text(encoding='utf8');md=MarkdownIt('commonmark',{'html':True});page=mathml.markdown_math(text,md);parsed=0
for value in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(value);parsed+=1
report={'status':'passed_exact_draft_problem_checks','completedChapter':False,'problemsWritten':10,'manuscriptWords':len(text.split()),'checks':checks,'nativeExpressionsParsed':parsed,'sha256':hashlib.sha256(text.encode()).hexdigest(),'remaining':'Full source selection, further bank questions, final decisions, figures/models, integration and rendered review; the draft is not counted as a finished technical note.'}
(R/'research/l_projection-evidence/worked-bank-mathematics.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
