from pathlib import Path
import sys,re,json,math
from itertools import product
from xml.etree import ElementTree as ET
B=Path(__file__).parent; E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
from markdown_it import MarkdownIt
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True});checks=0;formulas=0
def ck(x):
 global checks
 assert x;checks+=1
for f in E.glob('a_divide-*.md'):
 text=mathml.markdown_math(f.read_text(),md)
 for m in re.findall(r'<math\b[\s\S]*?</math>',text):ET.fromstring(m);formulas+=1
# Independent exhaustive order-sensitive summary associativity including the identity.
def summary(a):
 if not a:return(0,-math.inf,-math.inf,-math.inf)
 return(sum(a),max(sum(a[:j])for j in range(1,len(a)+1)),max(sum(a[i:])for i in range(len(a))),max(sum(a[i:j])for i in range(len(a))for j in range(i+1,len(a)+1)))
def join(L,R):
 s,p,u,b=L;t,q,v,c=R;return(s+t,max(p,s+q),max(v,t+u),max(b,c,u+q))
for n in range(0,7):
 for a in product([-2,0,3],repeat=n):
  for i in range(n+1):
   for j in range(i,n+1):
    L,R,Q=map(summary,[a[:i],a[i:j],a[j:]])
    ck(join(join(L,R),Q)==join(L,join(R,Q))==summary(a))
ck(summary([3,-6,5,-5,1,6,-2])==(2,4,5,7));ck(summary([6,-2,3,-6,5,-5,1])==(2,7,2,7))
def best(a):return min(((-sum(a[i:j]),i,j)for i in range(len(a))for j in range(i+1,len(a)+1)))
ck(best([3,-6,5,-5,1,6,-2])==(-7,2,6));ck(best([6,-2,3,-6,5,-5,1])==(-7,0,3))
# Both radix identities, including signed operands and odd widths.
for x in range(-140,141):
 for y in range(-70,71):
  h,l=divmod(abs(x),10);u,v=divmod(abs(y),10);s=(h+l)*(u+v)-h*u-l*v;d=h*u+l*v-(h-l)*(u-v)
  ck(s==d);ck((h*u*100+s*10+l*v)*(-1 if(x<0) != (y<0)else 1)==x*y)
# Noncommutative 2x2-block Strassen, over small deterministic matrix instances.
def add(A,B):return[[x+y for x,y in zip(a,b)]for a,b in zip(A,B)]
def neg(A):return[[-x for x in r]for r in A]
def sub(A,B):return add(A,neg(B))
def mul(A,B):return[[sum(A[i][k]*B[k][j]for k in range(len(B)))for j in range(len(B[0]))]for i in range(len(A))]
for q in range(40):
 A,B0,C,D,E0,F,G,H=[[[((q+v*7+i*3+j*11)%13)-6 for j in range(2)]for i in range(2)]for v in range(8)]
 M1=mul(add(A,D),add(E0,H));M2=mul(add(C,D),E0);M3=mul(A,sub(F,H));M4=mul(D,sub(G,E0));M5=mul(add(A,B0),H);M6=mul(sub(C,A),add(E0,F));M7=mul(sub(B0,D),add(G,H))
 ck(add(sub(add(M1,M4),M5),M7)==add(mul(A,E0),mul(B0,G)));ck(add(M3,M5)==add(mul(A,F),mul(B0,H)));ck(add(M2,M4)==add(mul(C,E0),mul(D,G)));ck(add(add(sub(M1,M2),M3),M6)==add(mul(C,F),mul(D,H)))
ck(416%17==8 and 8*13%17==2);ck(pow(22,2,97)==96 and pow(22,4,97)==1)
(E/'a_divide-synthesis-checks.json').write_text(json.dumps(dict(status='passed',scope='New mathematical constructions and transfer examples; finite exhaustive checks supplement stated proofs, not a full chapter or browser audit',assertions=checks,parsedMathExpressions=formulas),indent=2)+'\n');print(checks,'assertions;',formulas,'expressions')
