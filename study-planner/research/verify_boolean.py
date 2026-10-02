"""Independent truth-vector oracle, no chapter parser or laboratory imports."""
from itertools import product
from pathlib import Path
import json
count=0
def check(condition):
 global count
 assert condition
 count+=1
bits=list(product((0,1),repeat=3))
for x,y,z in bits:
 check(x*(y|z)==((x*y)|(x*z)))
 check((x|(y*z))==((x|y)*(x|z)))
 check((x|(x*y))==x)
 check((x|((1-x)*y))==(x|y))
 check(((x*y)|((1-x)*z)|(y*z))==((x*y)|((1-x)*z)))
 check(((x|y)*((1-x)|z)*(y|z))==((x|y)*((1-x)|z)))
 check(1-(x|y)==(1-x)*(1-y))
 check(1-(x*y)==((1-x)|(1-y)))
 check((x*(y^z))==((x*y)^(x*z)))
 check((x|y)==(x^y^(x*y)))
 check(((x|y)==(x^y))==(x*y==0))
 check((((1-x)*y)|(x*z))==((x|y)*((1-x)|z)))
# All three-input functions: restrictions, Shannon, support, quantification, duality.
for mask in range(256):
 vals=[(mask>>i)&1 for i in range(8)]
 dual=[1-vals[7-i] for i in range(8)]
 check([1-dual[7-i] for i in range(8)]==vals)
 check(sum(vals)==4 if vals==dual else True)
 for v in range(3):
  other=[j for j in range(3) if j!=v]
  rising=falling=changed=False
  for b in product((0,1),repeat=2):
   assignment=[0]*3
   for j,a in zip(other,b):assignment[j]=a
   i=sum(a<<(2-j) for j,a in enumerate(assignment));zero=vals[i];assignment[v]=1;k=sum(a<<(2-j) for j,a in enumerate(assignment));one=vals[k]
   rising|=zero<one;falling|=one<zero;changed|=zero!=one
   universal=zero&one;existential=zero|one
   for x,value in ((0,zero),(1,one)):
    check(((1-x)*zero)|(x*one)==value)
    check(((x|zero)*((1-x)|one))==value)
    check(universal<=value<=existential)
    check(((value^zero)==(x*(zero^one))))
   check((1-zero)^(1-one)==zero^one)
  check(changed==(rising or falling))
# Every two-input function pair, every cofactor context: product and OR differences.
for fm,gm in product(range(16),repeat=2):
 f=[fm>>i&1 for i in range(4)];g=[gm>>i&1 for i in range(4)]
 for v in (0,1):
  stride=2 if v==0 else 1
  for base in range(4):
   if base&stride:continue
   f0,f1=f[base],f[base|stride];g0,g1=g[base],g[base|stride];d=f0^f1;e=g0^g1
   check(((f0*g0)^(f1*g1))==((f0*e)^(g0*d)^(d*e)))
   check(((f0|g0)^(f1|g1))==(((1-f0)*e)^((1-g0)*d)^(d*e)))
# All four-input truth tables: independent subset inversion and reconstruction.
for mask in range(65536):
 values=[mask>>i&1 for i in range(16)]
 coefficients=[]
 for s in range(16):
  a=0
  for t in range(16):
   if t&s==t:a^=values[t]
  coefficients.append(a)
 for s in range(16):
  value=0
  for t,a in enumerate(coefficients):
   if t&s==t:value^=a
  check(value==values[s])
# Worked-problem equations, tested on every applicable assignment.
for x,y,z,w in product((0,1),repeat=4):
 pairs=[
  ((x*y)|x|(z*(x|y)),x|(y*z)),
  ((x|((1-x)*y))*(x|((1-x)*z)),x|(y*z)),
  (1-((x|(1-y))*(z|w)),((1-x)*y)|((1-z)*(1-w))),
  (((1-x)*y*z)|(x*(1-y)*z)|(x*y*(1-z))|(x*y*z),(x*y)|(x*z)|(y*z)),
  ((x|y)*(x|(1-y))*((1-x)|z),x*z),
  ((x*y)|(x*(1-y))|(z*(1-z)),x),
  (((x*y)|(x*z)|(y*z)),(x*y)^(x*z)^(y*z)),
  ((x|y)*(1-(x*y)),x^y),
  ((x|y)^ (x^y),x*y),
  ((x*y)|(x*z)|(x*(1-y)*(1-z))|(1-x),1),
 ]
 for a,b in pairs:check(a==b)
check([int(((1-x)*y)|z) for x,y,z in bits]==[0,1,1,1,0,1,0,1])
check([1^x^(x*y) for x,y in product((0,1),repeat=2)]==[1,1,0,1])
check([(x,y,z) for x,y,z in bits if x==1 and y!=z]==[(1,0,1),(1,1,0)])
check(sum(all(((m>>i)&1)!=((m>>(7-i))&1) for i in range(8)) for m in range(256))==16)
result={'assertions':count,'allFourInputANFTables':65536,'allThreeInputFunctions':256,'allTwoInputFunctionPairs':256,'scope':'Finite independent checks. Universal identities are proved in prose; this is not a universal accuracy guarantee.'}
(Path(__file__).parent/'g_boolean-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
