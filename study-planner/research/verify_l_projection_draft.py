"""Verify the actual written examples; a passed draft check is not full chapter approval."""
from pathlib import Path
import json,sympy as S
B=Path(__file__).resolve().parent;E=B/'l_projection-evidence';checks=[]
def ck(name,ok):assert bool(ok),name;checks.append(name)
M=S.Matrix;I=S.eye(3)
C=M([[1,0],[0,1],[1,1]]);b=M([1,2,0]);P=C*(C.T*C).inv()*C.T;p=P*b;r=b-p
ck('Plane formula',P==S.Rational(1,3)*M([[2,-1,1],[-1,2,1],[1,1,2]]))
ck('Plane membership and residual',p==M([0,1,1])and r==M([1,1,-1])and C.T*r==S.zeros(2,1))
ck('Plane squared distance and split',r.dot(r)==3 and b.dot(b)==p.dot(p)+r.dot(r))
t=S.symbols('t',real=True);A=C.row_join(C[:,0]+C[:,1]);c=M([-t,1-t,t]);n=M([-1,-1,1])
ck('Dependent coefficient family',A*c==p and A*n==S.zeros(3,1))
q=c.subs(t,S.Rational(1,3));ck('Minimum-norm coefficients',q.dot(n)==0 and q.dot(q)==S.Rational(2,3))
G=S.diag(1,4);u=M([1,1]);W=u*(u.T*G*u).inv()*u.T*G;x=M([2,0]);p=W*x;r=x-p
ck('Weighted projector',W==M([[1,4],[1,4]])/5 and W*W==W and W.T*G==G*W)
ck('Weighted residual',p==M([S.Rational(2,5)]*2)and u.T*G*r==S.zeros(1,1))
ck('Weighted energy split',(r.T*G*r)[0]==S.Rational(16,5)and(x.T*G*x)[0]==(p.T*G*p)[0]+(r.T*G*r)[0])
u=M([1,S.I]);H=u*(u.H*u).inv()*u.H;x=M([1,0]);r=x-H*x
ck('Complex projector',H.H==H and H*H==H and u.H*r==S.zeros(1,1))
n=M([1,2,-1]);x=M([2,0,1]);p=x-n*(n.dot(x)-3)/n.dot(n)
ck('Affine hyperplane',p==M([S.Rational(7,3),S.Rational(2,3),S.Rational(2,3)])and n.dot(p)==3 and(x-p).dot(x-p)==S.Rational(2,3))
D=M([[1,1,0],[0,1,1]]);d=M([1,2]);p=D.T*(D*D.T).inv()*d
ck('Affine system closest point',p==M([0,1,1])and D*p==d and M([-1,1,-1]).dot(p)==0)
P=M([[1,0],[0,0]]);Q=M([[1,1],[1,1]])/2;T=P*Q
ck('Noncommuting product',T.T!=T and T*T!=T and all(T**k==S.Rational(1,2)**k*M([[1,1],[0,0]])for k in range(1,10)))
ck('Trace is not intersection dimension',S.trace(P*Q)==S.Rational(1,2)and M.hstack(*P.columnspace(),*Q.columnspace()).rank()==2)
e=S.symbols('epsilon',nonzero=True,real=True);A=M([[1,1],[0,e]]);x=M([0,1])
ck('Fixed-rank projector versus limiting rank',S.simplify(A*(A.T*A).inv()*A.T)==S.eye(2)and A.inv()*x==M([-1/e,1/e]))
report=dict(status='draft_examples_passed',completedChapter=False,checks=checks,note='Only the currently written examples are certified. Full source comparison, worked bank, models, final rules and browser QA remain pending.')
(E/'draft-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print('Passed '+str(len(checks))+' independent draft-example certificates; chapter remains incomplete.')
