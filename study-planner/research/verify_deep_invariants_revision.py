"""Independent finite algorithms cross-check the new proofs and actual models."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import itertools, math, json, re, hashlib, subprocess, sys, xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=0
def check(b):
 global checks;assert b;checks+=1
for encoded in range(1<<16):
 adjacency=[(encoded>>(4*i))&15 for i in range(4)];reachable=[]
 for source in range(4):
  reached=1<<source;front=reached
  while front:
   following=0
   for v in range(4):
    if front>>v&1:following|=adjacency[v]
   front=following&~reached;reached|=front
  reachable.append(reached)
 for Q in range(16):
  K=Q
  while True:
   nextK=sum(1<<i for i in range(4)if K>>i&1 and adjacency[i]&~K==0)
   if nextK==K:break
   K=nextK
  oracle=sum(1<<i for i in range(4)if reachable[i]&~Q==0)
  check(K==oracle)
for n in range(101):
 a,b=n,n+1;t=0
 while a:
  check(2*a+b==3*n+1);a,b=a-1,b+2;t+=1
 check(t==n and b==3*n+1)
 a,b=30*n,18*n
 if n:
  while b:
   check(math.gcd(a,b)==6*n);old=b;a,b=b,a%b;check(b<old)
  check(a==6*n)
 x=y=n;t=0
 while x or y:
  old=(n+1)*x+y
  if x:x-=1;y+=n
  else:y-=1
  check((n+1)*x+y==old-1 and x>=0 and y>=0);t+=1
 check(t==n*n+2*n)
 check(sum(range(2,n+2))==n*(n+3)//2)
 check(sum(3**i for i in range(n+1))==(3**(n+1)-1)//2)
 if n:check(sum(k%3!=0 for k in range(1,3*n))==2*n)
 a,b=n,1
 for t in range(8):
  check(a-b==n*2**t-1 and Fraction(a+1,b)==n+1);a,b=2*a+1,2*b
for n in range(1025):
 e=n;r=1;base=2;products=0
 while e:
  check(r*base**e==2**n)
  if e%2:r*=base;products+=1
  base*=base;products+=1;e//=2
 check(r==2**n and products==(n.bit_length()+n.bit_count()if n else 0))
@lru_cache(None)
def trees(n):
 if n==0:return(None,)
 return tuple((L,U)for k in range(n)for L in trees(k)for U in trees(n-1-k))
def stats(T,d=0):
 if T is None:return 0,0,Fraction(),Fraction()
 L,U=T
 if L is None and U is None:return 1,0,Fraction(1,2**d),Fraction()
 l,i,w,loss=stats(L,d+1);ll,ii,ww,loss2=stats(U,d+1)
 return l+ll,i+ii+1,w+ww,loss+loss2+(Fraction(1,2**(d+1))if(L is None)!=(U is None)else 0)
treeCount=0
for n in range(1,9):
 for T in trees(n):
  l,i,w,loss=stats(T);check(l+i==n and w+loss==1 and w<=1);treeCount+=1
counts={16:1403,17:2025}
for n in range(18,114):counts[n]=3*counts[n-1]+5*counts[n-2]+4
check([n for n in range(100,114)if counts[n]%2==0]==[102,105,108,111])
finals=[]
for choices in itertools.product([(0,1),(-1,0),(1,2),(-2,-1)],repeat=5):
 b,r=12,7
 for db,dr in choices:check(b>r and b+db>=0 and r+dr>=0);b+=db;r+=dr
 check(b==r);finals.append(b+r)
check(len(finals)==1024 and min(finals)==4 and max(finals)==34 and set(finals)==set(range(4,35,2)))
for x in range(-20,21):
 for y in range(-20,21):check(((x+3*y)%5==0)==((2*x+y)%5==0 and(-x+2*y)%5==0))
check(sum([1,-2*2,3*2**2,4*2**3])==41)
check([(1,2),(2,4),(3,1),(4,3),(0,0)]==[((t)%5,(2*t)%5)for t in range(1,6)])
data=json.loads((R/'dist/chapters/concept-animations.json').read_text(encoding='utf-8'))['scenes'];models={k:v for k,v in data.items()if k.startswith('invariants-question-')}
for id,m in models.items():
 for f in m['frames']:
  ET.fromstring('<root>'+f['formulaHtml']+'</root>');check('\\'not in ''.join(ET.fromstring('<root>'+f['formulaHtml']+'</root>').itertext()))
  s=f['snapshot'];check(s['kind']in['table','state-graph','mass-tree','copy-array','split-order','modular-grid','flat-tree'])
  if s['kind']=='table':check(len(s['rowsHtml'])<=7 and all(len(row)==len(s['headings'])for row in s['rows']))
  if s['kind']=='copy-array':check(s['output']==s['source'][::-2][:len(s['output'])] and s['nextSource']==len(s['source'])-1-2*len(s['output']))
  if s['kind']=='mass-tree':
   levels=dict(s['nodes']);check(all(levels[b]==levels[a]+1 for a,b in s['edges']));check(Fraction(s['fullSum'])==sum(Fraction(1,2**levels[x])for x in s['leaves']))
  if s['kind']=='modular-grid':check(s['visited']==[[i%5,2*i%5]for i in range(s['step']+1)])
page=(R/'dist/chapters/d_invariants.html').read_text(encoding='utf-8');base=subprocess.check_output(['git','show','01015cc80d725c367957cace974050c90f96b64b:dist/chapters/d_invariants.html']).decode()
titles=lambda s:re.findall(r'<h3[^>]*>(Tutorial [\s\S]*?)</h3>',s)
check(titles(page)==titles(base)and len(titles(page))==49)
check(len(re.findall('data-deep-index=',page))==46)
for raw in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(raw);check('\\'not in ''.join(ET.fromstring(raw).itertext()))
report=dict(status='passed_with_recorded_finite_bounds',topicId='d_invariants',checkCount=checks,allFourVertexGraphs=65536,safeRegionCases=65536*16,binaryTreeShapes=treeCount,poweringExponents=1025,guardedPopulationPaths=1024,models=len(models),uniqueModelFrames=sum(len(m['frames'])for m in models.values()),pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='These finite computations cross-check the written proofs and declared models. They do not imply universal perfection or future examination outcomes.')
(E/'d_invariants-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(report)
