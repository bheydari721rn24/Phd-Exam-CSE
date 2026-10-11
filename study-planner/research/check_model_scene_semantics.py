from pathlib import Path
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/concept-animations.json';raw=p.read_bytes();d=json.loads(raw)['scenes'];checks=[]
def check(name,ok):
    assert ok,name
    checks.append(name)
input_records=d['insertion']['frames'][0]['snapshot']['input']
for k,f in enumerate(d['insertion']['frames']):
    s=f['snapshot'];live=[tuple(v) for v in s['array'] if v is not None]
    if s['saved'] is not None:live.append(tuple(s['saved']))
    check(f'insertion {k}: exact tagged multiset including saved key',Counter(live)==Counter(map(tuple,input_records)))
    if s['saved'] is None:
        prefix=s['array'][:f['metrics']['Pass']]
        check(f'insertion {k}: completed prefix sorted',prefix==sorted(prefix,key=lambda v:v[1]))
check('insertion final stable sorted records',d['insertion']['frames'][-1]['snapshot']['array']==sorted(input_records,key=lambda v:v[1]))
dist=[0,2,3,6];parent=[None,0,1,2];edges=[(0,1,2),(0,2,5),(1,2,1),(2,3,3),(1,3,7)]
for f,(u,v,w) in zip(d['shortest-path-certificate']['frames'],edges):
    check(f'certificate edge {u}->{v}',f['metrics']['Edge']==f'{u} to {v}' and f['metrics']['Weight']==w and f['metrics']['Edge inequality']==f'{dist[v]} <= {dist[u]+w}' and dist[v]<=dist[u]+w)
    check(f'certificate parent at {v}',f['metrics']['Parent of destination']==parent[v])
for u,v,w in edges:
    if parent[v]==u:check(f'rooted attaining edge {u}->{v}',dist[v]==dist[u]+w)
for f in d['encoding-length']['frames']:
    n=f['metrics']['Numeric parameter'];check(f'encoding n={n}',n.bit_length()==f['metrics']['Encoding length'])
a,b,carry,out=7,3,0,[]
for i,f in enumerate(d['word-bit-cost']['frames']):
    z=((a>>i)&1)+((b>>i)&1)+carry;out.append(z%2);carry=z//2
    check(f'ripple column {i}',f['snapshot']==dict(bits=out,carry=carry))
check('ripple exact result',sum(v*2**i for i,v in enumerate(out))==10 and carry==0)
report=dict(topicId='a_model',status='passed',checkCount=len(checks),checks=checks,animationJsonSha256=hashlib.sha256(raw).hexdigest(),exactMergeReplay='a_model-mathematical-checks.json contains independent replay of every field at all 23 merge checkpoints.',scope='Every saved insertion, path-certificate, encoding and bit-carry state checked against its exact displayed example. General mathematical arguments remain in the chapter.')
(R/'research/deep-library-revision/a_model-scene-semantics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),status='passed')))
