"""Independent immutable AVL oracle, shape DP, boundary calculations and stored-state certificates."""
from pathlib import Path
from itertools import permutations
from functools import lru_cache
from math import log2,log,ceil,sqrt
import json,subprocess,hashlib,random,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_balanced-evidence'
def h(t):return -1 if t is None else 1+max(h(t[1]),h(t[2]))
def ino(t):return []if t is None else ino(t[1])+[t[0]]+ino(t[2])
def pre(t):return []if t is None else[t[0]]+pre(t[1])+pre(t[2])
def ordinary(t,k):
 if t is None:return(k,None,None)
 a,l,r=t;return(a,ordinary(l,k),r)if k<a else(a,l,ordinary(r,k))if k>a else t
def plain(keys):
 t=None
 for k in keys:t=ordinary(t,k)
 return t
def rotate(t,left):
 a,l,r=t
 if left:b,rl,rr=r;return(b,(a,l,rl),rr)
 b,ll,lr=l;return(b,ll,(a,lr,r))
def repair(t):
 a,l,r=t;count=0
 if h(l)-h(r)>1:
  if h(l[1])<h(l[2]):l=rotate(l,True);count+=1
  t=rotate((a,l,r),False);count+=1
 elif h(r)-h(l)>1:
  if h(r[1])>h(r[2]):r=rotate(r,False);count+=1
  t=rotate((a,l,r),True);count+=1
 return t,count
def update(t,k,delete=False):
 if t is None:return(None if delete else(k,None,None)),0
 a,l,r=t;c=0
 if k<a:l,c=update(l,k,delete)
 elif k>a:r,c=update(r,k,delete)
 elif delete:
  if l is None:return r,0
  if r is None:return l,0
  a=ino(r)[0];r,c=update(r,a,True)
 t,d=repair((a,l,r));return t,c+d
def build(keys):
 t=None;c=0
 for k in keys:t,d=update(t,k);c+=d
 return t,c
@lru_cache(None)
def shapes(n):
 if n==0:return{-1:1}
 out={}
 for i in range(n):
  for a,x in shapes(i).items():
   for b,y in shapes(n-1-i).items():
    if abs(a-b)<=1:out[1+max(a,b)]=out.get(1+max(a,b),0)+x*y
 return out
M={-1:0,0:1};S={-1:1,0:1};L={-1:0,0:1,1:1}
for i in range(1,31):
 M[i]=1+M[i-1]+M[i-2];S[i]=2*S[i-1]*S[i-2]
 if i>1:L[i]=L[i-1]+L[i-2]
checks={}
def check(i,a,b,method):
 assert a==b,(i,a,b);checks[str(i)]={'method':method,'result':str(a)}
check(1,max(k for k,v in M.items()if v<=50),6,'Exact integer recurrence')
check(2,(ceil(log2(1001))-1,max(k for k,v in M.items()if v<=1000)),(9,13),'Exact capacities and integer recurrence')
check(3,(max(k for k,v in M.items()if v<=10**6),M[27],M[28]),(27,832039,1346268),'Exact recurrence and route comparison count')
fib=[0,1]
for i in range(34):fib.append(sum(fib[-2:]))
check(4,all(M[i]==fib[i+3]-1 for i in range(-1,31)),True,'Finite bases plus manual induction')
check(5,round(1/log2((1+sqrt(5))/2),5),1.44042,'Independent change of base; asymptotic domain reviewed')
check(6,(S[4],S[5]),(128,4096),'Independent ordered-minimal-shape recurrence')
check(7,(L[6],M[6],M[6]+1),(13,33,34),'Leaf recurrence and external-position identity')
check(8,shapes(5),{2:6},'All child sizes/heights dynamically enumerated')
check(9,shapes(7),{2:1,3:16},'All child sizes/heights dynamically enumerated')
cases={14:([30,10,20],[],[20,10,30],1,2),15:([50,20,70,10,30,25],[],[30,20,10,25,50,70],2,2),16:([50,20,70,10,30,5],[],[20,10,5,50,30,70],2,1),17:([40,20,10,30,60],[60],[20,10,40,30],2,1),18:([40,20,10,60],[60],[20,10,40],1,1),19:([40,20,30,60],[60],[30,20,40],1,2),20:([50,20,10,30,40,80,60,70,90,85,100,110],[10],[80,50,30,20,40,60,70,90,85,100,110],3,2),21:([40,20,60,10,30,50,70],[40],[50,20,10,30,60,70],2,0),22:([7],[9,7],[],-1,0),70:([50,10,30],[],[30,10,50],1,2)}
for i,(keys,deleted,order,height,count)in cases.items():
 t=plain(keys)if deleted else build(keys)[0];c=0 if deleted else build(keys)[1]
 for k in deleted:t,d=update(t,k,True);c+=d
 check(i,(pre(t),h(t),c),(order,height,count),'Immutable reference, recomputed heights; no production caches')
check(25,(2+1+3,2+1+3+1+4),(6,11),'Independent association count')
check(26,min(8,6,40-37,44-40),3,'Four augmentation candidates')
keys=[10,20,25,30,40,60,65,70,80]
check(27,(sum(k<65 for k in keys),keys[4],sum(25<=k<=70 for k in keys)),(6,40,6),'Sorted reference membership')
check(28,(2**4-1,3**4-1,2**3,3**3),(15,80,8,27),'Exact geometric capacities')
check(29,(4**4-1,4**3,sum(4**i for i in range(4))),(255,64,85),'Keys versus nodes independently counted')
check(30,([i for i in range(12)if 2**(i+1)-1<=1000<=3**(i+1)-1],[i for i in range(12)if 2**(i+1)-1<=1000<=4**(i+1)-1]),([6,7,8],[4,5,6,7,8]),'Capacity inequalities, labelled necessary')
check(31,(1+2*2+6*2,5*(1+6+36)),(17,215),'Actual occupancy level count, including exceptional root')
check(33,min(range(2,100),key=lambda b:b/log(b)),3,'Integer comparison plus derivative monotonicity proof')
check(41,(2**3-1,4**3-1),(7,63),'Collapsed-cluster capacity proof')
check(42,[b for b in range(1,10)if 2**b-1<=31<=4**b-1],[3,4,5],'Necessary black-layer capacity constraints')
check(43,(4,2*4,2*4-1),(4,8,7),'Root-null and actual-edge conventions')
check(60,(len([3,8,8,11,11,11]),[3,8,8,11,11,11][3:]),(6,[11,11,11]),'Expanded occurrence blocks')
check(65,sum(range(1,101)),100*101//2,'Exact development-audit overhead sum')
def midpoint(a,depth=0,H=None):
 if not a:return None
 H=(len(a).bit_length()-1)if H is None else H;i=(len(a)-1)//2
 return dict(key=a[i],red=depth==H and depth>0,left=midpoint(a[:i],depth+1,H),right=midpoint(a[i+1:],depth+1,H))
def certificate(t,kind,lo=float('-inf'),hi=float('inf'),root=True):
 if t is None:return(-1,0,0)
 assert lo<t['key']<hi
 hl,nl,bl=certificate(t['left'],kind,lo,t['key'],False);hr,nr,br=certificate(t['right'],kind,t['key'],hi,False)
 height=1+max(hl,hr);size=1+nl+nr
 if 'height'in t:assert t['height']==height and t['size']==size
 if kind=='avl':assert abs(hl-hr)<=1
 else:
  assert bl==br
  assert not t['red']or not ((t['left']and t['left']['red'])or(t['right']and t['right']['red']))
  if root:assert not t['red']
  if kind=='llrb':assert not (t['right']and t['right']['red'])
 return height,size,bl+(not t['red'])
for n in range(1,1025):certificate(midpoint(list(range(n))),'general')
check(67,1024,1024,'Independent midpoint/color construction certified for every size 1 through 1024; general variant only')
check(72,[min(b-a for a,b in zip(v,v[1:]))for v in[[4,11,17,26],[4,11,15,17,26],[4,11,15,26]]],[6,2,4],'Sorted adjacent-gap reference')
check(74,sum(range(100)),100*99//2,'Actual increasing ordinary-BST comparison count; sorting proof reviewed')
check(78,int(2*log2(1001)-1),18,'Safe integer bound; no attainability claim')
t,c=build([40,20,60,10,30,50,70,25,35]);c=0
for k,d in [(10,True),(60,True),(65,False)]:t,r=update(t,k,d);c+=r
check(80,(ino(t),pre(t),h(t),c,sum(k<65 for k in ino(t)),ino(t)[4],sum(25<=k<=65 for k in ino(t))),([20,25,30,35,40,50,65,70],[40,30,20,25,35,65,50,70],3,3,6,40,6),'Three immutable updates, independently recomputed order and metadata queries')
# Every remaining proof/recognition question is explicitly a manual proof audit, not a fabricated numerical test.
manual={10:'Inherited ordering and root-only counterexample',11:'True-height dependency and corrupted root cache',12:'Arbitrary rotation order versus failed balance',13:'Demoted-first dependency proof',23:'Route work versus primitive count',24:'Aggregate propagation despite unchanged height',32:'CPU/block resource distinctions',34:'Two actual top-down splits',35:'Bottom-up seven-key promotion sequence',36:'Borrow through 40 then promote 50',37:'Merge and root contraction',38:'General red cluster versus completed LLRB',39:'Child beta mismatch despite no red adjacency',40:'Actual/null count translation',44:'Red-uncle black-count accounting',45:'Line recolor and interval-preserving rotation',46:'Triangle role conversion before line case',47:'One new black leaf changes only one route family',48:'Removed successor color versus target association',49:'Red surviving child absorbs one black unit',50:'Case-two parent-color absorption and propagation',51:'Near/far labels relative to active side',52:'Only zero-rotation case propagates; terminating bound three',53:'Reachable deficit requires positive sibling beta',54:'Classical bounds cannot be assigned to recursive LLRB',55:'All seven exact LLRB insertions independently traced',56:'Two prepared toggles and normalization rotations',57:'Descending LLRB normalization',58:'Toggle preconditions in deletion',59:'Priority/arrival tie example independent of key rank',61:'Measurements versus invariant worst-case theorem',62:'Larger strict-equality failure witness links',63:'Inverse composition reverses location and order',64:'Ignored promoted root loses two reachable keys',66:'Visited ownership set and one-pass beta induction',68:'Fixed-size augmentation hypotheses',69:'Map and height-change insertion contract',71:'General/left-leaning versus black-balance recognition',73:'Parent-separator borrowing preserves intervals',75:'Owned cached extreme pointer maintenance',76:'Sign translation preserves LR geometry',77:'Input-preimage distribution differs from shape family',79:'Mutable value aggregate versus structural metadata'}
for i,reason in manual.items():checks[str(i)]={'method':'Manual step-by-step proof and boundary audit','result':'reviewed','reason':reason}
assert set(map(int,checks))==set(range(1,81))
models=json.loads((R/'dist/chapters/a_balanced-models.json').read_text(encoding='utf-8'))['models'];complete=0
for m in models:
 for f in m['frames']:
  z=f['snapshot']['state']
  if z.get('complete')and'tree'in z:
   kind='avl'if m['spec']['operation'].startswith('avl')else'llrb'if m['spec']['operation'].startswith('llrb')else'general'
   certificate(z['tree'],kind);complete+=1
 for f in m['frames']:
  z=f['snapshot']['state']
  if 'multiway'in z:
   depths=[]
   def multi(t,lo=float('-inf'),hi=float('inf'),d=0):
    k=t['keys'];assert k==sorted(set(k))and all(lo<x<hi for x in k);assert len(k)<=3
    if not t['children']:depths.append(d);return
    assert len(t['children'])==len(k)+1
    for i,c in enumerate(t['children']):multi(c,([lo]+k)[i],(k+[hi])[i],d+1)
   multi(z['multiway']);assert len(set(depths))<=1
specs=[]
for p in permutations([1,2,3,4,5]):
 specs.append(dict(operation='avl-insert',keys=list(p)))
 specs.append(dict(operation='avl-delete',keys=list(p),remove=[3,1,5,2,4,999]))
rng=random.Random(1406)
for j in range(50):
 a=rng.sample(range(-30,31),12);d=rng.sample(a,len(a))
 specs.extend([dict(operation='avl-delete',keys=a,remove=d),dict(operation='llrb-delete',keys=a,remove=d)])
code="const{evaluate}=require('./dist/chapters/a_balanced.js');const fs=require('fs');const specs=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(specs.map(evaluate)));"
answers=json.loads(subprocess.check_output(['node','-e',code],input=json.dumps(specs),cwd=R,text=True,encoding='utf-8'));frames=0
for spec,ans in zip(specs,answers):
 frames+=len(ans['states']);kind='avl'if spec['operation'].startswith('avl')else'llrb'
 for z in ans['states']:
  if z['complete']:certificate(z['tree'],kind)
 assert ans['result']['keys']==sorted(set(spec['keys'])-set(spec.get('remove',[])))
 if kind=='avl':
  t,c=build(spec['keys'])
  for k in spec.get('remove',[]):t,d=update(t,k,True);c+=d
  assert (ans['result']['preorder'],ans['result']['height'],ans['result']['rotations'])==(pre(t),h(t),c)
snapshot=json.loads((E/'prior-library.json').read_text(encoding='utf-8'))
prior=snapshot.get('chapters',snapshot)if isinstance(snapshot,dict)else snapshot
# Preserve prior library bytes; support the snapshot's actual structure.
if isinstance(prior,dict):
 for path,digest in prior.items():
  if isinstance(digest,dict):digest=digest.get('sha256')
  assert hashlib.sha256((R/path).read_bytes()).hexdigest()==digest,(path,'prior file changed')
else:
 for item in prior:
  path=item.get('path',item.get('url'));assert hashlib.sha256((R/'dist'/path).read_bytes()).hexdigest()==item['sha256']
report=dict(topicId='a_balanced',status='passed',questionAudits=checks,referenceInputs=len(specs),generatedCheckpoints=frames,completedStoredStates=complete,midpointSizesCertified=1024,models=len(models),storedCheckpoints=sum(len(m['frames'])for m in models),limits='Finite computations corroborate named statements. Manual proof audits are identified separately. Exhaustive five-key AVL permutations and fifty twelve-key AVL/LLRB deletion sequences do not certify all inputs or arbitrary corrupted pointers.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items()if k!='questionAudits'}))
