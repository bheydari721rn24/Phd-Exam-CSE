"""Exact-arithmetic audit of numerical answers and algebraic edge cases."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import re
checks=0
def eq(actual,expected):
 global checks
 assert actual==expected,(actual,expected)
 checks+=1
def mat(rows): return tuple(tuple(F(x) for x in row) for row in rows)
def mul(a,b):
 assert len(a[0])==len(b)
 return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))) for i in range(len(a)))
def add(a,b): return tuple(tuple(x+y for x,y in zip(ar,br)) for ar,br in zip(a,b))
def scale(t,a): return tuple(tuple(t*x for x in row) for row in a)
def transpose(a): return tuple(zip(*a))
def eye(n): return mat([[int(i==j) for j in range(n)] for i in range(n)])
def trace(a): return sum(a[i][i] for i in range(len(a)))
def norm2(a): return sum(x*x for row in a for x in row)
def power(a,k):
 result=eye(len(a))
 for _ in range(k): result=mul(result,a)
 return result
def inverse2(a):
 det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 if not det:return None
 return scale(1/det,mat([[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]))

A=mat([[1,-1,2],[0,3,1]]); B=mat([[2,0],[1,4],[-1,2]])
eq(mul(A,B),mat([[-1,0],[2,14]]))
terms=[mul(tuple((row[k],) for row in A),(B[k],)) for k in range(3)]
eq(add(add(terms[0],terms[1]),terms[2]),mul(A,B))
X=mat([[1,2],[3,0]]); Y=mat([[2,-1],[-1,2]])
eq(add(X,scale(2,Y)),mat([[5,0],[1,4]]));eq(add(scale(3,X),scale(-1,Y)),mat([[1,7],[10,-2]]))
eq(mul(mat([[2,1],[-1,3],[0,4]]),mat([[3],[-2]])),mat([[4],[-9],[-8]]))
eq(mul(mat([[2,-1],[1,3]]),mat([[1,0],[4,-2]])),mat([[-2,2],[13,-6]]))
eq(mul(mat([[3,2,5],[1,4,2]]),mat([[2,3],[5,4],[1,2]])),mat([[21,27],[24,23]]))
R=mat([[0,-1],[1,0]]);S=mat([[1,1],[0,1]])
eq(mul(R,S),mat([[0,-1],[1,1]]));eq(mul(S,R),mat([[1,-1],[1,0]]))
eq(mul(mul(R,S),mat([[1],[1]])),mat([[-1],[2]]));eq(mul(mul(S,R),mat([[1],[1]])),mat([[0],[1]]))
D=mat([[1,0],[0,0]]);lost=mat([[0,0],[1,0]])
eq(mul(D,lost),mat([[0,0],[0,0]]));assert lost!=mat([[0,0],[0,0]])
embed=mat([[1,0],[0,1],[0,0]]);reader=transpose(embed)
eq(mul(reader,embed),eye(2));eq(mul(embed,reader),mat([[1,0,0],[0,1,0],[0,0,0]]))
eq(mul(mul(S,mat([[1,1],[1,1]])),mat([[2,0],[0,3]])),mat([[4,6],[2,3]]))
eq(transpose(mul(mat([[1,2,0],[-1,3,4]]),mat([[2],[1],[-1]]))),mat([[4,-3]]))
z=(1,1j);eq(sum(x*x for x in z),0);eq(sum(x.conjugate()*x for x in z),2)
H=mat([[2,2],[2,4]]);K=mat([[0,3],[-3,0]]);A=add(H,K)
eq(A,mat([[2,5],[-1,4]]));eq(mul(mul(mat([[1,2]]),A),mat([[1],[2]])),mat([[26]]))
eq(norm2(A),46);eq(norm2(H),28);eq(norm2(K),18)
T=mat([[1,-1],[0,2],[1,0]]);eq(mul(transpose(T),T),mat([[2,-1],[-1,5]]))
Q=mat([[1,0],[0,0],[0,1]]);eq(mul(transpose(Q),Q),eye(2));eq(mul(Q,transpose(Q)),mat([[1,0,0],[0,0,0],[0,0,1]]))
for t in (F(-2),F(0),F(1),F(3,2),F(2)):
 a=mat([[1,t],[2,3]]);inv=inverse2(a)
 if t==F(3,2):eq(inv,None);eq(mul(a,mat([[-3],[2]])),mat([[0],[0]]))
 else:eq(mul(a,inv),eye(2));eq(mul(inv,a),eye(2))
eq(inverse2(mul(S,mat([[2,0],[0,3]]))),mat([[F(1,2),F(-1,2)],[0,F(1,3)]]))
cycle=mat([[0,0,1],[1,0,0],[0,1,0]]);eq(power(cycle,3),eye(3));assert power(cycle,2)!=eye(3)
tri1=mat([[2,1,4],[0,3,-2],[0,0,5]]);tri2=mat([[1,2,0],[0,-1,3],[0,0,2]])
eq(mul(tri1,tri2),mat([[2,3,11],[0,-3,5],[0,0,10]]))
AA=mat([[1,2,0],[0,-1,3]]);BB=mat([[2,0],[1,4],[-2,1]])
eq(mul(AA,BB),mat([[4,8],[-7,-1]]));eq(trace(mul(AA,BB)),3);eq(trace(mul(BB,AA)),3)
E12=mat([[0,1],[0,0]]);E21=mat([[0,0],[1,0]]);E11=mat([[1,0],[0,0]])
eq(trace(mul(mul(E12,E21),E11)),1);eq(trace(mul(mul(E12,E11),E21)),0)
PP=scale(F(1,5),mat([[1,2],[2,4]]));eq(mul(PP,PP),PP)
for k in range(1,8):eq(power(add(eye(2),PP),k),add(eye(2),scale(2**k-1,PP)))
for a,b,c in product(range(-2,3),repeat=3):
 u=mat([[1,a,b],[0,1,c],[0,0,1]]);v=mat([[1,-a,a*c-b],[0,1,-c],[0,0,1]])
 eq(mul(u,v),eye(3));eq(mul(v,u),eye(3))
for e in (F(-1),F(0),F(1,10),F(2)):
 A=mat([[2,0],[0,1]]);B=eye(2);E=mat([[0,e],[0,0]]);Fmat=mat([[0,0],[e,0]])
 error=add(mul(add(A,E),add(B,Fmat)),scale(-1,mul(A,B)))
 eq(error,mat([[e*e,e],[e,0]]));eq(norm2(error),e**4+2*e**2)
G=mat([[0,1,0],[1,0,1],[0,1,0]])
eq(power(G,2),mat([[1,0,1],[0,2,0],[1,0,1]]))
for length in range(5):
 count=[[0]*3 for _ in range(3)]
 for path in product(range(3),repeat=length+1):
  if all(G[path[k]][path[k+1]] for k in range(length)): count[path[0]][path[-1]]+=1
 eq(power(G,length),mat(count))
pool=[mat([row[:2],row[2:]]) for row in product((-1,0,1),repeat=4)]
for A,B in product(pool,repeat=2):
 eq(transpose(mul(A,B)),mul(transpose(B),transpose(A)))
 eq(trace(mul(A,B)),trace(mul(B,A)))
 C=pool[(int(sum(x for row in A for x in row))+int(sum(x for row in B for x in row)))%len(pool)]
 eq(mul(mul(A,B),C),mul(A,mul(B,C)))
 eq(mul(A,add(B,C)),add(mul(A,B),mul(A,C)))
eq((10*100*5+10*5*50,10*5*99+10*50*4),(7500,6950))
eq((100*5*50+10*100*50,100*50*4+10*50*99),(75000,69500))
root=Path(__file__).resolve().parents[1]
manuscript='\n'.join((root/'research'/name).read_text(encoding='utf-8') for name in ('l_matrices.en.md','l_matrices-problems.en.md','l_matrices-review.en.md'))
eq(len(re.findall(r'^### Problem ',manuscript,re.M)),36)
review=manuscript.split('## 13. Consolidation:',1)[1].split('## 14. References',1)[0]
eq(len(re.findall(r'^\d+\. \*\*',review,re.M)),50)
eq(len({c['university'] for c in json.loads((root/'research/l_matrices-reviewed-courses.json').read_text())}),5)
print(f'Matrix audit passed: {checks} exact checks; 36 solutions; 50 complete-sentence rules; five reviewed universities. Finite checks support the written proofs, not universal guarantees.')
