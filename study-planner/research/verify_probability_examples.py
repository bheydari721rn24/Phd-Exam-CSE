"""Independently enumerate finite event laws using exact rational arithmetic."""
from fractions import Fraction as F
from itertools import product

checks = 0
for weights in ((F(1,4),)*4, (F(1,10),F(2,10),F(3,10),F(4,10)), (F(1,2),F(1,2),F(0),F(0))):
    def prob(mask):
        return sum((weights[i] for i in range(4) if mask & (1 << i)), F(0))
    for a, b in product(range(16), repeat=2):
        pa, pb, q = prob(a), prob(b), prob(a & b)
        assert prob(a | b) == pa + pb - q
        assert prob(a ^ b) == pa + pb - 2*q
        assert prob(a & (15 ^ b)) == pa - q
        assert max(F(0),pa+pb-1) <= q <= min(pa,pb)
        assert abs(pa-pb) <= prob(a^b) <= min(pa+pb,2-pa-pb)
        assert abs(pa-pb) <= prob(a^b)
        assert prob(a|b) <= pa+pb
        checks += 1

# Independently enumerate eight membership cells for the three-event example.
atoms = [(0,0,0,F(5,100)),(1,0,0,F(10,100)),(0,1,0,F(15,100)),(0,0,1,F(20,100)),(1,1,0,F(10,100)),(1,0,1,F(15,100)),(0,1,1,F(5,100)),(1,1,1,F(20,100))]
p = lambda predicate: sum((w for a,b,c,w in atoms if predicate(a,b,c)), F(0))
assert p(lambda a,b,c: True) == 1
assert [p(lambda a,b,c,i=i:(a,b,c)[i]) for i in range(3)] == [F(55,100),F(50,100),F(60,100)]
assert p(lambda a,b,c: a or b or c) == F(95,100)
assert p(lambda a,b,c: a+b+c==1) == F(45,100)
assert p(lambda a,b,c: a+b+c==2) == F(30,100)
assert p(lambda a,b,c: a+b+c>=2) == F(50,100)
for a,b,c in product(range(16), repeat=3):
    # Uniform four-point law checks every triple of subsets of that space.
    pop = lambda x: F(x.bit_count(),4)
    assert pop(a|b|c) == pop(a)+pop(b)+pop(c)-pop(a&b)-pop(a&c)-pop(b&c)+pop(a&b&c)
    checks += 1

# Every feasible integer-percent overlap constructs a nonnegative law.
for a,b in product(range(101),repeat=2):
    for q in (max(0,a+b-100),min(a,b)):
        masses = [q,a-q,b-q,100-a-b+q]
        assert min(masses)>=0 and sum(masses)==100
        checks += 1
assert F(7,10)+F(6,10)-F(2,10)>1
assert [F(25,100),F(40,100),F(20,100),F(15,100)] == [F(1,4),F(65,100)-F(1,4),F(45,100)-F(1,4),1-F(65,100)-F(45,100)+F(1,4)]
for n in range(1,120):
    assert sum((F(1,k*(k+1)) for k in range(1,n+1)),F(0)) == 1-F(1,n+1)
assert F(2,9)/(1-F(1,9)) == F(1,4)
assert F(2,3)/(1-F(1,3)) == 1
assert 1-F(1,2)*F(1,2)*F(1,2) == F(7,8)
assert F(1,2**10)<=F(1,1000)<F(1,2**9)
print(f"Passed {checks:,} exact finite-model and feasibility checks; countable theorems retain separate written proofs.")
