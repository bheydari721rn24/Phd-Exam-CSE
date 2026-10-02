"""Independent finite checks of the chapter's worked calculations and actual code."""
import functools,itertools,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
main=(base/'d_invariants.en.md').read_text(encoding='utf-8');problems=(base/'d_invariants-problems.en.md').read_text(encoding='utf-8');review=(base/'d_invariants-review.en.md').read_text(encoding='utf-8')
env={}
for s in (main,problems):
 for code in re.findall(r'```python\n(.*?)\n```',s,re.S):exec(code,env)
lists=[list(xs) for n in range(5) for xs in itertools.product(range(-2,3),repeat=n)]
for xs in lists:assert env['prefix_sum'](xs)==sum(xs)
power_cases=0
for a,n in itertools.product(range(-3,4),range(70)):
 assert env['power'](a,n)==a**n;power_cases+=1
merge_cases=0
sorted_lists=[xs for xs in lists if xs==sorted(xs)]
for left,right in itertools.product(sorted_lists,repeat=2):
 assert env['merge'](left,right)==sorted(left+right);merge_cases+=1
# Integer-halving counts; verify the nonpower-of-two counterexample explicitly.
for n in range(10000):
 q=n;steps=0
 while q:q//=2;steps+=1
 assert steps==n.bit_length()
assert 3 .bit_length()==2
# Coin witness, checking each selected count and the population at every operation.
h,t=98,4
def flip(h,t,heads):
 assert h>=heads and t>=10-heads
 return h+10-2*heads,t-10+2*heads
h,t=flip(h,t,9);assert (h,t)==(90,12)
t+=h+1
for _ in range(9):h,t=flip(h,t,0)
assert (h,t)==(180,13)
h,t=flip(h,t,3);h,t=flip(h,t,1);assert (h,t)==(192,1)
# Every small full permutation and every consecutive triple checks inversion cases.
def inv(xs):return sum(a>b for i,a in enumerate(xs) for b in xs[i+1:])
rotations=0
for n in range(3,7):
 for xs in itertools.permutations(range(n)):
  for i in range(n-2):
   part=xs[i:i+3];k=part.index(min(part));part=part[k:]+part[:k];out=xs[:i]+part+xs[i+3:]
   assert inv(out)-inv(xs) in (0,-2);assert k==0 or out<xs;rotations+=1
# Legal sliding-puzzle edges, with independently calculated inversion and row parity.
slide_cases=0
for xs in itertools.permutations(range(6)):
 blank=xs.index(0);before=inv([x for x in xs if x])%2
 for target in [blank-1,blank+1,blank-3,blank+3]:
  if not 0<=target<6:continue
  if abs(target-blank)==1 and target//3!=blank//3:continue
  out=list(xs);out[blank],out[target]=out[target],out[blank];assert inv([x for x in out if x])%2==before;slide_cases+=1
for blank in range(16):
 xs=list(range(1,16));xs.insert(blank,0);p=(inv([x for x in xs if x])+blank//4)%2
 for target in [blank-1,blank+1,blank-4,blank+4]:
  if not 0<=target<16:continue
  if abs(target-blank)==1 and target//4!=blank//4:continue
  out=xs.copy();out[blank],out[target]=out[target],out[blank];assert (inv([x for x in out if x])+target//4)%2==p;slide_cases+=1
# Normal and misere game values from exact legal-move dynamic programming.
def game(misere):
 @functools.lru_cache(None)
 def wins(piles):
  if not any(piles):return misere
  return any(not wins(piles[:i]+(q,)+piles[i+1:]) for i,p in enumerate(piles) for q in range(p))
 return wins
normal,misere=game(False),game(True);nim_cases=0
for piles in itertools.product(range(6),repeat=4):
 z=functools.reduce(lambda a,b:a^b,piles,0);large=sum(p>1 for p in piles);ones=sum(p==1 for p in piles)
 assert normal(piles)==bool(z)
 expected=ones%2==0 if not large else bool(z)
 assert misere(piles)==expected;nim_cases+=1
# Perimeter change for every enabled single-cell addition on a 3x3 board.
def perimeter(mask):
 ans=0
 for i in range(9):
  if mask>>i&1:
   x,y=divmod(i,3)
   for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    a,b=x+dx,y+dy
    ans+=not(0<=a<3 and 0<=b<3 and mask>>(3*a+b)&1)
 return ans
growth=0
for mask in range(512):
 for i in range(9):
  if mask>>i&1:continue
  x,y=divmod(i,3);neighbors=[3*a+b for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if 0<=a<3 and 0<=b<3]
  k=sum(mask>>j&1 for j in neighbors)
  if k>=2:assert perimeter(mask|1<<i)-perimeter(mask)==4-2*k;growth+=1
# Bridge invariant with every short admissible trace and several initial occupancies.
bridge_edges=0
for cap in range(1,5):
 for c0 in range(cap+1):
  a0,b0=2,1;threshold=a0-b0+3*(cap-c0);front={(a0,b0,c0)}
  for _ in range(9):
   new=set()
   for a,b,c in front:
    assert 0<=c<=cap and a-b-3*c>=a0-b0-3*c0
    if a-b<threshold:new.add((a+3,b,c+1));bridge_edges+=1
    if c>0:new.add((a,b+2,c-1));bridge_edges+=1
   front=new
# Structural identities over all small list triples and accumulators.
small=[list(x) for n in range(4) for x in itertools.product(range(2),repeat=n)]
structural=0
for x,y,z in itertools.product(small,repeat=3):
 assert (x+y)+z==x+(y+z);assert len(x+y)==len(x)+len(y)
 assert list(reversed(x+y))==list(reversed(y))+list(reversed(x));structural+=1
for xs,acc in itertools.product(small,repeat=2):
 result=acc.copy()
 for x in xs:result.insert(0,x)
 assert result==xs[::-1]+acc
# Guarded population process: each legal change lowers difference exactly one.
population=0
for b,r in itertools.product(range(25),repeat=2):
 if b<=r:continue
 for db,dr in [(0,1),(-1,0),(1,2),(-2,-1)]:
  if b+db<0 or r+dr<0:continue
  assert (b+db)-(r+dr)==b-r-1 and b+db>=r+dr;population+=1
assert 19+3*5==34
assert re.findall(r'### Problem (\d+)\.',problems)==list(map(str,range(1,50))) and problems.count('**Solution.**')==49
assert re.findall(r'^(\d+)\. ',review,re.M)==list(map(str,range(1,81)))
page=(ROOT/'dist/chapters/d_invariants.html').read_text(encoding='utf-8')
from check_site_en import MathCoverage
c=MathCoverage();c.feed(page);assert not c.unstyled,c.unstyled
assert page.count('<figure ')==4 and page.count('<h2 ')==14 and page.count('<munderover>')>=2
assert not re.search(r'[\u0600-\u06ff]|\$|\\\\|<!--',page)
assert '^' not in re.sub(r'<pre>.*?</pre>','',page,flags=re.S)
assert 'awaiting your approval' in page
report={'prefixSumInputs':len(lists),'powerInputs':power_cases,'mergePairs':merge_cases,'halvingInputs':10000,'tripleRotations':rotations,'slidingMoves':slide_cases,'nimPositionsPerVariant':nim_cases,'growthTransitions':growth,'bridgeTransitions':bridge_edges,'listTriples':structural,'populationTransitions':population,'workedProblems':49,'examinationRules':80,'figures':4,'limits':'These are finite independent error detectors. General statements are proved in the manuscript; no deferred Iranian examination archives were used.'}
(base/'d_invariants-finite-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
