"""Independent finite checks for the chapter's declared Boolean and bound models."""
from itertools import product
from pathlib import Path
import math,json
COUNT=0
def check(value):
 global COUNT
 assert value
 COUNT+=1
N=lambda a,b:1-(a&b)
R=lambda a,b:1-(a|b)
for x,y in product((0,1),repeat=2):
 check(N(N(x,x),N(y,y))==(x|y))
 check(N(N(x,y),N(x,y))==(x&y))
 check(R(R(x,x),R(y,y))==(x&y))
 t=N(x,y);check(N(N(x,t),N(y,t))==(x^y))
 check((x|y)==((x&y)^x^y))
for x,y,z,s,w in product((0,1),repeat=5):
 check(N(N(x,y),z)==((x&y)|(1-z)))
 check(N(N(N(x,y),N(x,y)),z)==1-(x&y&z))
 check(((1-s)&x)|(s&y)| (x&y)==(((1-s)&x)|(s&y)))
 check((s|x)&((1-s)|y)&(x|y)==((s|x)&((1-s)|y)))
 check(N(N(N(s,s),x),N(s,y))==(((1-s)&x)|(s&y)))
 check(R(R(x,R(y,y)),R(z,w))==((x|(1-y))&(z|w)))
 check(N(x,y)|R(y,z)==N(x,y))
 check(((x&y&z)|(x&y&w)|(x&z&w)|(y&z&w))==int(x+y+z+w>=3))
 check(((x|y)&(x|z)&(x|w)&(y|z)&(y|w)&(z|w))==int(x+y+z+w>=3))
 # Pullup/pulldown conduction for NAND, NOR, AOI21, and OAI21.
 for d,u in [(x&y,(1-x)|(1-y)),(x|y,(1-x)&(1-y)),((x&y)|z,((1-x)|(1-y))&(1-z)),((x|y)&z,((1-x)&(1-y))|(1-z))]:
  check(d+u==1)
# All three-input truth tables: independently synthesize row selectors with a
# binary NAND library, including constants generated from an available input.
def inv(x):return N(x,x)
def and_chain(items):
 v=items[0]
 for x in items[1:]:v=inv(N(v,x))
 return v
def or_chain(items):
 v=items[0]
 for x in items[1:]:v=N(inv(v),inv(x))
 return v
for mask in range(256):
 for row in range(8):
  bits=[(row>>(2-i))&1 for i in range(3)]
  terms=[]
  for selector in range(8):
   if (mask>>selector)&1:
    terms.append(and_chain([bits[i] if (selector>>(2-i))&1 else inv(bits[i]) for i in range(3)]))
  actual=or_chain(terms) if terms else inv(N(bits[0],inv(bits[0])))
  check(actual==((mask>>row)&1))
# Binary XNOR tree parity for multiple shapes and sizes.
def xnor(a,b):return 1-(a^b)
def tree(bits):
 if len(bits)==1:return bits[0]
 k=len(bits)//2
 return xnor(tree(bits[:k]),tree(bits[k:]))
for n in range(2,9):
 for bits in product((0,1),repeat=n):
  p=sum(bits)%2;fold=bits[0]
  for b in bits[1:]:fold=xnor(fold,b)
  check(fold==(p^((n-1)%2)));check(tree(bits)==fold)
# Closure on binary truth-table masks: every gate is evaluated as a primitive
# operation over independently enumerated vectors, with no external constants.
universal=[]
for gate in range(16):
 pool={12,10};changed=True
 while changed:
  previous=set(pool)
  for a,b in product(previous,repeat=2):
   out=0
   for row in range(4):
    av=(a>>row)&1;bv=(b>>row)&1
    out|=((gate>>(2*av+bv))&1)<<row
   pool.add(out)
  changed=pool!=previous
 check(len(pool)<=16)
 if len(pool)==16:universal.append(gate)
check(universal==[1,7]) # NOR mask 0001; NAND mask 0111.
# Hand calculations, checked against direct path enumeration.
late_paths=[2+3+2,0+3+2,0+5+2,1+5+2]
early_paths=[1+.5,1+.5,2+.5,2+.5]
check(max(late_paths)==8);check(min(early_paths)==1.5)
check(2+3==5);check(4+5==9)
check(abs((.8-.35)-.45)<1e-12);check(abs((2.7-2)-.7)<1e-12)
check(abs(2000*30e-15*math.log(2)*1e12-41.58883083359672)<1e-9)
check(1+2==3 and 3+1+2==6 and (3+1)-1==3)
out={'assertions':COUNT,'allThreeInputNandSyntheses':256,'singleBinaryUniversalMasks':universal,'xnorLeafCounts':[2,8],'models':'Stable Boolean, ideal complementary switches, supplied fixed timing bounds. No physical circuit certification.'}
p=Path(__file__).with_name('g_gates-verification.json');p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
