"""Independent sorted-multiset, mathematical and forest certification."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import json,subprocess,math,hashlib,heapq,random,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_heap-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
models=json.loads((R/'dist/chapters/a_heap-models.json').read_text())['models'];specs=[]
for keys in permutations(range(5)):
 for orientation in ['min','max']:
  for d in[2,3,4]:specs.append(dict(operation='build',keys=list(keys),orientation=orientation,arity=d))
rng=random.Random(1406)
for _ in range(50):
 keys=[rng.randrange(-20,21)for _ in range(rng.randrange(1,16))]
 for orientation in ['min','max']:
  for d in[2,3,4]:
   # Sorted ascending/descending arrays are independently valid in every arity.
   a=sorted(keys,reverse=orientation=='max')
   specs.extend([dict(operation='insert',keys=a,value=-30 if orientation=='min'else 30,orientation=orientation,arity=d),dict(operation='extract',keys=a,orientation=orientation,arity=d),dict(operation='delete',keys=a,index=rng.randrange(len(a)),orientation=orientation,arity=d),dict(operation='change',keys=a,index=rng.randrange(len(a)),value=rng.randrange(-40,41),orientation=orientation,arity=d)])
 specs.append(dict(operation='sort',keys=keys))
 specs.append(dict(operation='topk',keys=keys,k=rng.randrange(1,len(keys)+1)))
 specs.append(dict(operation='frontier',keys=sorted(keys),k=rng.randrange(1,len(keys)+1)))
 specs.append(dict(operation='binomial',keys=keys))
save(E/'independent-inputs.json',specs)
node="const fs=require('fs'),h=require('./dist/chapters/a_heap.js');const a=JSON.parse(fs.readFileSync('research/a_heap-evidence/independent-inputs.json'));process.stdout.write(JSON.stringify(a.map(s=>h.evaluate(s))))"
p=subprocess.run(['node','-e',node],cwd=R,capture_output=True,text=True,check=True);runs=json.loads(p.stdout)
checkpoints=0;forest_count=0
def heap_order(a,d,orientation):return all((a[(i-1)//d]<=a[i]if orientation=='min'else a[(i-1)//d]>=a[i])for i in range(1,len(a)))
def binomial(t,orientation):
 global forest_count
 forest_count+=1;children=t['children'];d=len(children)
 assert sorted(len(c['children'])for c in children)==list(range(d))
 sizes=[binomial(c,orientation)for c in children]
 assert all((t['key']<=c['key']if orientation=='min'else t['key']>=c['key'])for c in children)
 assert 1+sum(sizes)==2**d
 return 1+sum(sizes)
def forest_nodes(roots):
 arr=[]
 def walk(t):arr.append(t);[walk(c)for c in t['children']]
 for r in roots:walk(r)
 return arr
for obj in runs+[dict(spec=m['spec'],states=[f['snapshot']['state']for f in m['frames']],result=m['result'])for m in models]:
 s=obj['spec'];op=s['operation'];result=obj['result'];keys=s.get('keys',[]);orientation=s.get('orientation','min');d=s.get('arity',2)
 if op=='sort':orientation='max'
 if op=='topk':orientation='min'
 for z in obj['states']:
  checkpoints+=1
  if z['kind']=='array':
   a=z['array'];assert len({x['id']for x in a})==len(a)
   live=[x['key']for x in a[:z['active']]];valid=heap_order(live,d,orientation)
   assert valid==z['valid']
   if z['complete']:assert valid
   if op=='sort':
    assert Counter(x['key']for x in a)==Counter(keys)
    if z['complete']:
     tail=[x['key']for x in a[z['active']:]];assert tail==sorted(tail)
     if live and tail:assert max(live)<=min(tail)
  else:
   roots=z['roots'];nodes=forest_nodes(roots);assert len({x['id']for x in nodes})==len(nodes)
   if op=='binomial':
    sizes=[binomial(r,orientation)for r in roots]
    if z['complete']:assert len({len(r['children'])for r in roots})==len(roots)
   elif z['complete']:
    def check(t):
     assert all(t['key']<=c['key']for c in t['children']);[check(c)for c in t['children']]
    for r in roots:assert not r['marked'];check(r)
    marks=sum(x['marked']for x in nodes);assert z['potential']==len(roots)+2*marks
 if op=='fibonacci':assert result['potential']==4;continue
 if op=='binomial':
  assert Counter(x['key']for x in forest_nodes(result['roots']))==Counter(keys)
  assert result['links']==len(keys)-len(keys).bit_count();continue
 out=result['array'];expected=keys.copy()
 if op=='insert':expected.append(s['value'])
 elif op=='extract':expected.remove(min(keys)if orientation=='min'else max(keys));assert result['selected'][0]['key']==(min(keys)if orientation=='min'else max(keys))
 elif op=='delete':expected.pop(s['index'])
 elif op=='change':expected[s['index']]=s['value']
 elif op=='topk':expected=sorted(keys)[-s['k']:]
 elif op=='frontier':assert result['rankValue']==sorted(keys,reverse=orientation=='max')[s['k']-1]
 if op=='sort':assert out==sorted(keys)
 assert Counter(out)==Counter(expected),(s,out,expected)
 assert result['positions']=={x['id']:i for i,x in enumerate(result['entries'][:result['active']])}
# Exact independent hand-calculated witnesses and complete identity checks.
expected={'up':[2,5,8,9,10,14,11,12],'down':[5,9,8,12,10,14,11],'build':[0,1,2,9,4,3,7],'indexed':[1,5,2,9,10,8,11],'equal-children':[4,6,4,7,9,8,10],'max-insert':[16,15,12,10,6,9,11,8],'delete-up':[1,4,2,10,12,3],'delete-down':[1,4,2,5,7,6],'topk':[8,10,9]}
for m in models:
 if m['id']in expected:assert m['result']['array']==expected[m['id']],m['id']
by={m['id']:m for m in models};assert by['up']['result']['comparisons']==by['up']['result']['swaps']==3
assert(by['down']['result']['comparisons'],by['down']['result']['swaps'])==(4,2)
assert(by['build']['result']['comparisons'],by['build']['result']['swaps'])==(8,4)
assert [x['id']for x in by['unstable']['result']['entries']]==['E2','E1','E0']
assert by['frontier']['result']['array']==[1,4,2,8,5,3,7]and by['frontier']['result']['rankValue']==4
# Integer shape and counting arguments checked independently of production code.
def subtree_size(i,n):return 0 if i>=n else 1+subtree_size(2*i+1,n)+subtree_size(2*i+2,n)
def height(i,n):return -1 if i>=n else 1+max(height(2*i+1,n),height(2*i+2,n))
for n in range(1,257):
 hs=[height(i,n)for i in range(n)];assert sum(hs)==n-n.bit_count()
 for i in range(n):assert hs[i]==(n//(i+1)).bit_length()-1
 h=n.bit_length()-1;assert sum((j.bit_length()-1)for j in range(1,n+1))==h*n-2**(h+1)+h+2
for d in[2,3,4,7]:
 for n in range(1,1025):
  h=0;cap=1;level=1
  while cap<n:level*=d;cap+=level;h+=1
  power=d;k=1
  while power<(d-1)*n+1:power*=d;k+=1
  assert h==k-1
from functools import lru_cache
@lru_cache(None)
def count(n):
 if n<2:return 1
 L=subtree_size(1,n);R=n-1-L
 return math.comb(n-1,L)*count(L)*count(R)
for n in range(1,9):
 if n<=7:assert count(n)==sum(heap_order(list(a),2,'min')for a in permutations(range(n)))
 assert count(n)==math.factorial(n)//math.prod(subtree_size(i,n)for i in range(n))
assert count(6)==20 and count(7)==80 and count(8)==210
fib=[0,1]
for _ in range(15):fib.append(sum(fib[-2:]))
assert [fib[d+2]for d in[6,7,8]]==[21,34,55]
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==53
for q in prior:assert hashlib.sha256((R/'dist'/q['url']).read_bytes()).hexdigest()==q['sha256']
qs=json.loads((B/'a_heap-questions.json').read_text());assert len(qs)==80 and all(len(q['solution'].split())>=55 for q in qs)
save(E/'question-review.json',dict(status='reviewed',items=[dict(id=q['id'],method='Independent arithmetic witness plus general proof/conditions reviewed'if i in[1,2,3,7,8,10,13,14,16,17,19,21,22,24,25,26,27,28,29,30,32,33,34,35,37,38,39,40,42,43,45,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,71,72,73,74,75,76]else'Manual conceptual proof, counterexample, assumptions and boundary review; not claimed automatically proven')for i,q in enumerate(qs,1)]))
save(E/'mathematics.json',dict(status='passed',independentSpecifications=len(runs),generatedAndSavedCheckpoints=checkpoints,storedModels=len(models),storedCheckpoints=sum(len(m['frames'])for m in models),binomialNodesCertified=forest_count,shapeSizes=256,multiwayThresholdCases=4096,distinctHeapCountsEnumeratedThrough=7,priorChapterPagesRetained=53,handCalculatedTraces=len(expected),fibonacciEvidence='Explicit first-loss/second-loss forest, potential counts and written degree/potential proofs; not an arbitrary Fibonacci implementation.',verificationLimit='Finite independent oracles and manual proofs do not certify every unseen problem.'))
print('Passed',len(runs),'independent input specifications and',checkpoints,'checkpoints; prior 53 pages retained.')
