"""Independent exact-cost oracles, not tests that copy the simulator's implementation."""
from pathlib import Path
import json,subprocess,itertools,math,hashlib,tempfile,re
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'a_amortized-evidence'
inputs=[];expected=[]
def add(spec,cost,predicate=None):inputs.append(spec);expected.append((cost,predicate))
for w in range(2,7):
 for start in range(2**w):
  for N in [0,1,2,3,7,16,32]:
   cost=sum(((start+i)%(2**w)^((start+i+1)%(2**w))).bit_count()for i in range(N))
   add(dict(kind='counter',width=w,start=start,count=N),cost,dict(value=(start+N)%2**w))
for r in [1.5,2,3]:
 for N in range(33):
  C=1;cost=N
  for n in range(N):
   if n==C:cost+=n;C=math.ceil(r*C)
  add(dict(kind='growth',count=N,factor=r),cost,dict(capacity=C))
for N in range(10):
 for bits in itertools.product([0,1],repeat=N):
  n=0;C=2;cost=0;ops=[]
  for bit in bits:
   if bit:
    ops.append(dict(type='append'));cost+=1
    if n==C:cost+=n;C*=2
    n+=1
   else:
    ops.append(dict(type='pop'));cost+=1
    if n:
     n-=1
     if C>2 and n<=C/4:cost+=n;C//=2
  add(dict(kind='shrink',size=0,capacity=2,operations=ops),cost,dict(capacity=C,records=n))
for N in range(9):
 for bits in itertools.product([0,1],repeat=N):
  enqueues=0;dequeues=0;transfers=0;out=0;pending=0;ops=[];fifo=[];returned=None
  for bit in bits:
   if bit:
    enqueues+=1;pending+=1;fifo.append(enqueues);ops.append(dict(type='enqueue',value=enqueues))
   else:
    ops.append(dict(type='dequeue'));dequeues+=1
    if out==0:transfers+=pending;out=pending;pending=0
    if out:out-=1;returned=fifo.pop(0)
  add(dict(kind='queue',operations=ops),enqueues+2*transfers+dequeues,dict(fifo=fifo,returned=returned))
for N in range(8):
 for values in itertools.product(range(3),repeat=N):
  for equal in [False,True]:
   # Final survivors are exactly suffix records not dominated by a later greater (or equal) value.
   survivors=[i for i,v in enumerate(values)if not any(x>=v if equal else x>v for x in values[i+1:])]
   pops=N-len(survivors)
   add(dict(kind='monotonic',values=list(values),equal=equal),N+pops,dict(stack=survivors))
for N in range(17):
 cost=N+sum((N//2**j)*2**j for j in range(1,N.bit_length()))
 add(dict(kind='blocks',count=N),cost,dict(blockSizes=[2**j for j in range(N.bit_length())if N>>j&1]))
for N in range(8):
 for bits in itertools.product([0,1],repeat=N):
  size=0;cost=0;ops=[]
  for b in bits:
   if b:size+=1;cost+=1;ops.append(dict(type='push',value=1))
   else:r=min(size,3);size-=r;cost+=r;ops.append(dict(type='multipop',k=3))
  add(dict(kind='multipop',operations=ops),cost,dict(stackLength=size))
add(dict(kind='migration'),8,dict(boundary=4,size=8))
cache=Path(tempfile.gettempdir())/'a-amortized-inputs.json';cache.write_text(json.dumps(inputs),encoding='utf-8')
output=Path(tempfile.gettempdir())/'a-amortized-results.json'
node="""const h=require('./dist/chapters/a_amortized.js'),fs=require('fs'),inputs=JSON.parse(fs.readFileSync(process.argv[1]));let checkpoints=0;const results=inputs.map(s=>{const e=h.evaluate(s);checkpoints+=e.states.length;for(const z of e.states){if(z.complete&&Math.abs(z.actual-z.charges-z.initialPotential+z.potential)>1e-8)throw Error('telescoping');if(z.complete&&['growth','shrink'].includes(s.kind)&&z.charge!==undefined&&z.charge>(s.kind==='growth'?1+(s.factor||2)/((s.factor||2)-1):3)+1e-8)throw Error('charge bound');}return e.result;});fs.writeFileSync(process.argv[2],JSON.stringify({results,checkpoints}));"""
subprocess.run(['node','-e',node,str(cache),str(output)],cwd=R,check=True)
data=json.loads(output.read_text());checks=0
for s,z,(cost,exp)in zip(inputs,data['results'],expected):
 assert z['actual']==cost,(s,z,cost)
 for k,v in (exp or{}).items():
  actual=([r['value']for r in reversed(z['output'])]+[r['value']for r in z['input']])if k=='fifo'else z.get('returned',{}).get('value')if k=='returned'else len(z['records'])if k=='records'else len(z['stack'])if k=='stackLength'else [len(x)for x in z['blocks']if x]if k=='blockSizes'else z[k]
  assert actual==v,(s,k,actual,v);checks+=1
 if s['kind']=='monotonic'and s['values']:assert z['comparisons']<=2*len(s['values'])-2
prior=json.loads((E/'prior-library.json').read_text())['chapters']
for c in prior:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']
html=(R/'dist/chapters/a_amortized.html').read_text(encoding='utf-8')
assert html.count('class="exam-question"')==87 and html.count('class="review-rule"')==80
assert '<!--'not in html and '$'not in html
report=dict(status='passed',independentInputs=len(inputs),checkedCheckpoints=data['checkpoints'],contractChecks=checks,unchangedChapterPages=len(prior),costModels=['finite-width XOR bit flips','capacity-event sums','all append/pop prefixes through length nine','FIFO transfer count through length eight','suffix-dominance certificate through length seven','binary level output-write counts','bounded record conservation','incremental copy deadline'],limits='Finite spaces establish mechanism consistency; derivations are also reviewed in the chapter. They do not certify all future questions or all production runtimes.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
