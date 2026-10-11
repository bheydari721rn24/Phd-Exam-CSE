"""Verify every retained fixed induction scene against its mathematical state."""
from pathlib import Path
import ast,hashlib,json,math
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text())['scenes'];checks=[]
def check(key,i,condition):
    assert condition,(key,i)
    checks.append(dict(scene=key,checkpoint=i,passed=True))
for key in ['induction-triangular','induction-square']:
    for i,f in enumerate(d[key]['frames']):
        n=f['snapshot']['n'];square=key.endswith('square');total=n*n if square else n*(n+1)//2;inc=max(0,2*n-1)if square else n
        active=sum(x['tone']=='active'for x in f['nodes'])
        exact='+'.join(map(str,range(1,2*n,2)if square else range(1,n+1)))
        check(key,i,f['snapshot']['count']==f['metrics']['Total tiles']==len(f['nodes'])==total and f['metrics']['Added tiles']==active==inc and (f['formula'].startswith(exact+'=')if n else f['formula'].endswith('=0')))
known={}
for i,f in enumerate(d['strong-coins']['frames']):
    s=f['snapshot'];n=s['n'];coins=s['coins'];dep=f['metrics']['Dependency']
    check('strong-coins',i,all(c in[3,5]for c in coins)and sum(coins)==n and[ int(x['label'])for x in f['nodes']]==coins and(dep=='base case'if n<=10 else dep==n-3 and coins==known[n-3]+[3]))
    known[n]=coins
old=None
for i,f in enumerate(d['euclid']['frames']):
    s=f['snapshot'];a,b,A,Bb,x0,y0,x1,y1=[s[k]for k in['a','b','A','B','x0','y0','x1','y1']]
    valid=a==A*x0+Bb*y0 and b==A*x1+Bb*y1 and math.gcd(a,b)==6 and(A,Bb)==(84,30)
    if old and old['b']:
        q=old['a']//old['b'];valid=valid and(a,b)==(old['b'],old['a']%old['b'])and(x0,y0,x1,y1)==(old['x1'],old['y1'],old['x0']-q*old['x1'],old['y0']-q*old['y1'])
    elif old:valid=valid and s==old
    check('euclid',i,valid);old=s
for i,f in enumerate(d['induction-gap']['frames']):
    established=ast.literal_eval(f['metrics']['Established indices']);want=list(range(0,2*i+1,2))
    check('induction-gap',i,established==want and all(x['tone']==('done'if int(x['label'])in want else'warning'if int(x['label'])%2 else'plain')for x in f['nodes']))
report=dict(status='passed',checkpoints=len(checks),sourceSha256=hashlib.sha256(p.read_bytes()).hexdigest(),scope='Five fixed scenarios, all 36 exact checkpoints. Exact counts, highlighted increments, residue reachability, 3/5 coin dependencies, gcd and both coefficient rows checked; not certification of arbitrary inputs.',checks=checks)
(E/'d_induction-scene-semantics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(status='passed',checkpoints=len(checks))))
