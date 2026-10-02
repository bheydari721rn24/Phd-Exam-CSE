"""Independent finite checks of the actual manuscript and laboratory implementations."""
import cmath,itertools,json,math,random,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
source=(base/'a_divide.en.md').read_text(encoding='utf-8')
fence=chr(96)*3
env={}
for block in re.findall(fence+r'python\n(.*?)'+fence,source,re.S):exec(compile(block,'<actual manuscript code>','exec'),env)
result={}
count=0
for n in range(8):
 for a in itertools.product(range(-2,3),repeat=n):
  s,c=env['sort_and_count'](a)
  assert s==sorted(a)
  assert c==sum(a[i]>a[j] for i in range(n) for j in range(i+1,n))
  for target in [-3,0,3]:
   assert env['lower_bound'](s,target)==next((i for i,v in enumerate(s) if v>=target),len(s))
  count+=1
result['mergeInversionAndLowerBoundArrays']=count
arrays=[a for n in range(2,7) for a in itertools.product([-1,0,1],repeat=n)]
def direct_summary(a):
 return (sum(a),max(sum(a[:i]) for i in range(1,len(a)+1)),max(sum(a[i:]) for i in range(len(a))),max(sum(a[i:j]) for i in range(len(a)) for j in range(i+1,len(a)+1)))
records=[]
for a in arrays:
 expected=direct_summary(a)
 assert env['subarray_summary'](a)==expected
 witness=max(((sum(a[i:j]),-i,-j) for i in range(len(a)) for j in range(i+1,len(a)+1)))
 for split in range(1,len(a)):
  assert env['join_summary'](direct_summary(a[:split]),direct_summary(a[split:]))==expected
  records.append({'a':a,'split':split,'values':expected,'witness':[witness[0],-witness[1],-witness[2]]})
js=r'''const fs=require("fs"),lab=require("./dist/chapters/a_divide.js"),rows=JSON.parse(fs.readFileSync(0,"utf8"));for(const r of rows){const t=lab.analyze(r.a,r.split);if(JSON.stringify(t.combined)!==JSON.stringify(r.values)||JSON.stringify([t.witness.value,t.witness.start,t.witness.end])!==JSON.stringify(r.witness))throw Error("summary mismatch");}for(const s of ["1,,2","1,","1.5,2","1e2,3","NaN,2",""]){let rejected=false;try{lab.parse(s);}catch(e){rejected=true;}if(!rejected)throw Error("bad parser accepted");}for(const a of [[1],[1,100],[1,-100],Array(17).fill(1)]){let rejected=false;try{lab.analyze(a,1);}catch(e){rejected=true;}if(!rejected)throw Error("bad array accepted");}console.log(rows.length);'''
p=subprocess.run(['rtk','proxy','node','-e',js],input=json.dumps(records),text=True,capture_output=True,cwd=ROOT,check=True)
result['summaryArrays']=len(arrays);result['actualJavaScriptSplitWitnessChecks']=int(p.stdout.strip())
try:env['subarray_summary']([]);raise AssertionError('empty input accepted')
except ValueError:pass
checks=0
for x in range(-128,129):
 for y in range(-128,129):
  assert env['karatsuba'](x,y)==x*y;checks+=1
rng=random.Random(1406)
for bits in range(1,513):
 radius=1<<max(1,bits-1)
 x=(1<<bits)+rng.randrange(-radius,radius)
 y=rng.getrandbits(bits+1)
 for sx in [-1,1]:
  assert env['karatsuba'](sx*x,y)==sx*x*y;checks+=1
result['signedOddWidthKaratsubaProducts']=checks
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def ma(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def ms(a,b):return tuple(tuple(a[i][j]-b[i][j] for j in range(2)) for i in range(2))
for _ in range(300):
 blocks=[tuple(tuple(rng.randrange(-5,6) for _ in range(2)) for _ in range(2)) for _ in range(8)]
 A,B,C,D,E,F,G,H=blocks
 expected=(ma(mm(A,E),mm(B,G)),ma(mm(A,F),mm(B,H)),ma(mm(C,E),mm(D,G)),ma(mm(C,F),mm(D,H)))
 assert env['strassen_blocks'](*blocks,ma,ms,mm)==expected
result['noncommutingMatrixBlockChecks']=300
grid=list(itertools.product(range(3),repeat=2))
cases=[list(c) for n in range(2,10) for c in itertools.combinations(grid,n)]
cases += [list(c) for n in range(2,8) for c in itertools.combinations_with_replacement(grid[:4],n)]
cases += [[(rng.randrange(-7,8),rng.randrange(-7,8)) for _ in range(rng.randrange(2,33))] for _ in range(1000)]
for points in cases:
 expected=min((a[0]-b[0])**2+(a[1]-b[1])**2 for i,a in enumerate(points) for b in points[i+1:])
 d,ids=env['closest_pair'](points);a,b=(points[i] for i in ids)
 assert ids[0]!=ids[1] and d==expected==(a[0]-b[0])**2+(a[1]-b[1])**2
assert env['closest_pair']([]) is None and env['closest_pair']([(1,1)]) is None
result['closestPairSetsAndMultisets']=len(cases)
count=0;max_error=0.0
for n in [1,2,4,8,16,32]:
 for _ in range(30):
  a=[complex(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(n)]
  got=env['fft'](a)
  direct=[sum(a[k]*cmath.exp(2j*math.pi*j*k/n) for k in range(n)) for j in range(n)]
  err=max(abs(x-y) for x,y in zip(got,direct));max_error=max(max_error,err)
  assert err<1e-9
  assert max(abs(x-y) for x,y in zip(env['fft'](got,True),a))<1e-9;count+=1
for a in [[],[1,2,3]]:
 try:env['fft'](a);raise AssertionError('invalid transform accepted')
 except ValueError:pass
result['floatingFFTDirectAndInverseChecks']=count;result['floatingFFTMaxObservedError']=max_error
def nt(a,inverse=False):
 n=len(a);root=pow(2,-1,17) if inverse else 2
 out=[sum(a[k]*pow(root,j*k,17) for k in range(n))%17 for j in range(n)]
 return [v*pow(n,-1,17)%17 for v in out] if inverse else out
polys=list(itertools.product(range(3),repeat=3))
for a in polys:
 for b in polys:
  aa=list(a)+[0]*5;bb=list(b)+[0]*5
  A,B=nt(aa),nt(bb);got=nt([x*y%17 for x,y in zip(A,B)],True)
  direct=[sum(a[i]*b[j] for i in range(3) for j in range(3) if i+j==r)%17 for r in range(8)]
  assert got==direct
result['exactModularConvolutions']=len(polys)**2
assert env['sort_and_count']([2,4,7,1,4,6])[1]==5
assert env['subarray_summary']([4,-6,8,-2,3,-9,5])==(3,7,5,9)
assert env['karatsuba'](123,45)==5535 and env['karatsuba'](-37,25)==-925
html=(ROOT/'dist/chapters/a_divide.html').read_text(encoding='utf-8')
assert len(re.findall(r'<h3>Problem \d+ ',html))==48
review=(base/'a_divide-review.en.md').read_text(encoding='utf-8')
assert re.findall(r'^(\d+)\. \*\*',review,re.M)==list(map(str,range(1,89)))
assert html.count('<figure ')==5 and html.count('<math ')==12
assert 'English review draft' in html
assert not re.search(r'[\u0600-\u06ff]',html)
rows=json.loads((ROOT/'dist/lessons.json').read_text())
chapters={c['topicId']:c for w in rows for c in w['chapters']}
assert chapters['a_recurrence']['status']=='ready' and chapters['a_divide']['status']=='draft'
result['limits']='Finite independent checks supplement the stated proofs; they do not establish universal completeness, a floating-point error guarantee or performance on unseen questions.'
(base/'a_divide-math-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
