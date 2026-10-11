"""Independent dictionary contracts, exact combinatorics and route invariants."""
from pathlib import Path
from itertools import permutations,product
from fractions import Fraction as F
from collections import Counter
import json,subprocess,math,random,hashlib,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_hash-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
rng=random.Random(1406);specs=[]
for keys in permutations([0,1,5,6,10]):
 specs.append(dict(operation='open',capacity=7,keys=list(keys),commands=[dict(type='get',key=k)for k in[0,10,17,99]]))
 specs.append(dict(operation='shift',capacity=7,keys=list(keys),commands=[dict(type='delete',key=keys[2])]))
for policy,capacity in [('linear',7),('square',7),('alternating',7),('triangular',8),('double',12)]:
 for _ in range(100):
  keys=[rng.randrange(-20,21)for _ in range(5)];cmd=[dict(type=rng.choice(['get','put','delete']),key=rng.randrange(-20,21))for _ in range(15)]
  specs.append(dict(operation='open',capacity=capacity,policy=policy,step=rng.choice([0,1,4,8,-5]),keys=keys,commands=cmd))
for _ in range(100):
 keys=rng.sample(range(-30,31),6)
 specs.append(dict(operation='chain',capacity=5,keys=keys,commands=[dict(type='get',key=keys[0]),dict(type='delete',key=keys[2])]))
 specs.append(dict(operation='rebuild',capacity=7,newCapacity=13,keys=keys))
 specs.append(dict(operation='robin',capacity=7,keys=keys))
 specs.append(dict(operation='bloom',capacity=13,keys=keys,hashes=3,commands=[dict(type='get',key=keys[0])]))
for keys in permutations([0,1,4,5]):specs.append(dict(operation='cuckoo',capacity=3,keys=list(keys)))
specs.extend([dict(operation='perfect',capacity=6,keys=[0,6,12,2,3,9]),dict(operation='perfect',capacity=5,keys=[-10,999,0,5]),dict(operation='horner',capacity=13,base=-5,keys=[-999,999,0,1])])
save(E/'independent-inputs.json',specs)
node="const fs=require('fs'),h=require('./dist/chapters/a_hash.js'),a=JSON.parse(fs.readFileSync('research/a_hash-evidence/independent-inputs.json'));process.stdout.write(JSON.stringify(a.map(s=>h.evaluate(s))))"
p=subprocess.run(['node','-e',node],cwd=R,capture_output=True,text=True,check=True);runs=json.loads(p.stdout)
models=json.loads((R/'dist/chapters/a_hash-models.json').read_text())['models']
def route(k,s):
 m=s['capacity'];policy=s.get('policy','linear');offsets=[]
 for i in range(m):
  if policy=='linear':d=i
  elif policy=='square':d=i*i
  elif policy=='alternating':d=0 if i==0 else (-1 if i%2==0 else 1)*((i+1)//2)**2
  elif policy=='triangular':d=i*(i+1)//2
  else:d=i*(1+k%7 if s.get('keyStep')else s.get('step',1))
  offsets.append((k+d)%m)
 return offsets
checkpoints=0;dictionary_checks=0
for obj in runs+[dict(spec=m['spec'],states=[f['snapshot']['state']for f in m['frames']],result=m['result'])for m in models]:
 s=obj['spec'];op=s['operation'];r=obj['result'];keys=s['keys'];m=s['capacity'];abstract={}
 commands=[dict(type='put',key=k)for k in keys]+s.get('commands',[])
 completed=[z for z in obj['states']if z['complete']]
 if op in ['chain','open']:
  assert len(completed)==len(commands)
  for c,z in zip(commands,completed):
   k=c['key'];status=z['answer']['status']
   if c['type']=='put':
    if k in abstract:assert status=='updated'
    elif op=='chain' or s['policy'] in ['linear','triangular'] and len(abstract)<m:assert status=='inserted'
    if status in ['inserted','updated']:abstract[k]=c.get('value',k)
    else:assert status=='route_exhausted'
   elif c['type']=='delete':
    assert status==('deleted'if k in abstract else'absent');abstract.pop(k,None)
   else:assert status==('found'if k in abstract else'absent')
   actual=[v['key']for b in z['buckets']for v in b]if op=='chain'else[v['key']for v in z['slots']if isinstance(v,dict)]
   assert Counter(actual)==Counter(abstract.keys()),(s,c,z);dictionary_checks+=1
 for z in obj['states']:
  checkpoints+=1
  if op in ['chain','perfect']:
   assert all(v['key']%z['capacity']==i for i,b in enumerate(z['buckets'])for v in b)
  elif op in ['open','shift','rebuild','robin']:
   live=[v for v in z['slots']if isinstance(v,dict)];assert len({v['key']for v in live})==len(live);assert len({v['id']for v in live})==len(live)
   if z['complete']:
    for at,v in enumerate(z['slots']):
     if not isinstance(v,dict):continue
     ctx=dict(s,capacity=z['capacity'],policy='linear'if op in ['shift','rebuild','robin']else s['policy'])
     rr=route(v['key'],ctx);assert at in rr
     assert all(z['slots'][i]is not None for i in rr[:rr.index(at)]),(s,z,v)
  elif op=='cuckoo':
   for side,a in enumerate([z['slots'],z['extra'].get('right',[])]):
    for i,v in enumerate(a):
     if v:assert i==(v['key']%m if side==0 else(v['key']//m)%m)
 if op=='shift':assert Counter(r['liveKeys'])==Counter(k for k in set(keys)if k!=s['commands'][0]['key'])
 if op=='rebuild':assert Counter(r['liveKeys'])==Counter(set(keys));assert r['moves']==len(set(keys))
 if op=='robin':assert Counter(r['liveKeys'])==Counter(set(keys))
 if op=='perfect':
  assert Counter(r['liveKeys'])==Counter(keys)
  for q in r['answer']['second']:
   assert len(set(q['targets']))==len(q['keys']);assert q['targets']==[((q['a']*(k+999)+q['b'])%q['prime'])%q['size']for k in q['keys']]
  assert r['answer']['squaredSpace']==sum(len(b)**2 for b in r['buckets'])
 if op=='bloom':
  expected=[0]*m
  for k in keys:
   for i in range(s['hashes']):expected[(k*(i+1)+i*i)%m]=1
  assert r['slots']==expected
  for k in keys:assert all(expected[(k*(i+1)+i*i)%m]for i in range(s['hashes']))
 if op=='horner':
  expected=sum(k*s['base']**(len(keys)-i-1)for i,k in enumerate(keys))%m
  assert r['answer']['hash']==expected
 if op=='cuckoo'and r['answer']['status']=='inserted':assert Counter(r['liveKeys'])==Counter(keys)
# Independently enumerate finite probability spaces rather than reuse animation code.
probabilities=[]
for m in range(2,7):
 for n in range(1,5):
  placements=list(product(range(m),repeat=n));occupied=sum(len(set(a))for a in placements);pairs=sum(sum(a[i]==a[j]for i in range(n)for j in range(i))for a in placements);squares=sum(sum(a.count(j)**2 for j in range(m))for a in placements)
  assert F(occupied,len(placements))==m*(1-F(m-1,m)**n)
  assert F(pairs,len(placements))==F(n*(n-1),2*m)
  assert F(squares,len(placements))==n+F(n*(n-1),m)
  nocoll=sum(len(set(a))==n for a in placements)
  expected=math.prod(F(m-i,m)for i in range(n))if n<=m else F(0)
  assert F(nocoll,len(placements))==expected;probabilities.append(dict(capacity=m,keys=n,outcomes=len(placements)))
permutations_checked=0
for m in range(2,8):
 for n in range(m):
  total=0;ct=0
  for rr in permutations(range(m)):
   ct+=1;total+=next(i+1 for i,v in enumerate(rr)if v>=n)
  assert F(total,ct)==F(m+1,m-n+1);permutations_checked+=ct
universal=[]
for p in[3,5,7,11]:
 for m in range(2,p+1):
  for x,y in[(0,1),(0,p-1),(1,p-1)]:
   count=sum(((a*x+b)%p)%m==((a*y+b)%p)%m for a in range(1,p)for b in range(p))
   assert F(count,p*(p-1))<=F(1,m);universal.append(dict(prime=p,capacity=m,x=x,y=y,collisions=count))
restricted=sum(((a*0+b)%7)%2==((a*2+b)%7)%2 for a in[1,2]for b in[0,1,2]);assert restricted==6
for m in range(2,25):
 for step in range(-m,m+1):assert len({(i*step)%m for i in range(m)})==m//math.gcd(step,m)
for m in[2,4,8,16,32,64]:assert len({i*(i+1)//2%m for i in range(m)})==m
for p in[3,7,11,19,23]:assert len({(0 if i==0 else(1 if i%2 else-1)*((i+1)//2)**2)%p for i in range(p)})==p
by={x['id']:x for x in models}
assert [v['key']if isinstance(v,dict)else v for v in by['linear']['result']['slots']]==[21,32,43,None,None,None,None,None,None,9,10]
assert by['linear']['result']['probes']==16
assert by['double']['result']['route']==[10,5]
assert by['perfect']['result']['answer']['squaredSpace']==14
assert by['square-failure']['result']['answer']['status']=='route_exhausted'
assert by['double-failure']['result']['answer']['distinctVisited']==3
assert by['update']['result']['slots'][1]['value']==99
assert len(by['update']['result']['liveKeys'])==4
assert sorted(by['all-markers']['result']['liveKeys'])==[9,10]
assert by['cuckoo-failure']['result']['answer']['status']=='needs_rebuild'
assert F(9,4)*(F(1,9)+F(1,8)+F(1,7)+F(1,6))==F(275,224)
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==54
for c in prior:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']
page=(R/'dist/chapters/a_hash.html').read_text(encoding='utf-8');assert page.count('class="exam-question"')==82 and page.count('class="review-rule"')==80 and '<!--'not in page
save(E/'mathematics.json',dict(status='passed',independentInputs=len(runs),checkpoints=checkpoints,dictionaryOperationChecks=dictionary_checks,placementSpaces=probabilities,idealProbePermutationOutcomes=permutations_checked,universalFamilyPairCases=len(universal),universalParametersRestrictedCounterexample=restricted,routeCoverage='gcd cycles, triangular powers of two, signed-square primes',handTraces='wraparound, marker updates/reuse, route failure, perfect allocation, double-hash query, cuckoo obstruction',priorChapterPagesUnchanged=54,limits='Finite enumerations test implementation and small-space formulas; universal statements additionally depend on the explicit written proofs. No official MS65 unique key or unseen-exam guarantee asserted.'))
print('Passed',len(runs),'independent inputs;',checkpoints,'checkpoints;',dictionary_checks,'dictionary operation contracts;',permutations_checked,'ideal-route permutation outcomes.')
