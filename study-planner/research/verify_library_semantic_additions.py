"""Independent finite witnesses for findings from the final semantic review.

General proofs remain in the chapters; these regressions target their exact
empty-domain and finite-code boundary risks rather than claim universal QA.
"""
from itertools import product,combinations
from functools import reduce
from operator import xor
from pathlib import Path
import json

checks=0
for n in range(5):
    for a in product((False,True),repeat=n):
        for b in (False,True):
            pairs=[(all(a) and b,all(x and b for x in a)),
                   (all(a) or b,all(x or b for x in a)),
                   (any(a) and b,any(x and b for x in a)),
                   (any(a) or b,any(x or b for x in a))]
            for i,(left,right) in enumerate(pairs):
                if n or i in (1,2):
                    assert left==right,(n,a,b,i)
                else:
                    assert (left!=right)==((i==0 and not b) or (i==3 and b))
                checks+=1
        for c in product((False,True),repeat=n):
            assert all(x and y for x,y in zip(a,c))==(all(a) and all(c))
            assert any(x or y for x,y in zip(a,c))==(any(a) or any(c))
            checks+=2
a=(True,False);c=(False,True)
assert all(x or y for x,y in zip(a,c)) and not(all(a) or all(c))
assert any(a) and any(c) and not any(x and y for x,y in zip(a,c))

words=[]
for bits in product((0,1),repeat=7):
    syndrome=reduce(xor,(i for i,v in enumerate(bits,1) if v),0)
    if syndrome==0:words.append(bits)
assert len(words)==16
extended=[w+(sum(w)%2,) for w in words]
distance=lambda x,y:sum(a!=b for a,b in zip(x,y))
assert min(distance(a,b) for a,b in combinations(words,2))==3
assert min(distance(a,b) for a,b in combinations(extended,2))==4
for a,b in combinations(words,2):
    w=distance(a,b)
    assert distance(a+(sum(a)%2,),b+(sum(b)%2,))==w+w%2
    checks+=1

for x,y,z,w in product((0,1),repeat=4):
    sop=(x and y and z) or (x and y and w) or (x and z and w) or (y and z and w)
    pos=(x or y) and (x or z) and (x or w) and (y or z) and (y or w) and (z or w)
    dual=(x or y or z) and (x or y or w) and (x or z or w) and (y or z or w)
    assert bool(sop)==bool(pos)==(x+y+z+w>=3)
    assert bool(dual)==(x+y+z+w>=2)
    checks+=1
out={'status':'passed','finiteCases':checks,'quantifierDomainSizes':[0,1,2,3,4],
     'hammingCodewords':16,'originalDistance':3,'extendedDistance':4,
     'voterRows':16,'scope':'Finite regressions plus general proofs in manuscripts; not a proof of the entire library.'}
Path('research/library-semantic-additions-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
