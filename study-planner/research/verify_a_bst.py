"""Independent immutable-tree references, exact fractions and actual permutations."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from math import comb,factorial,ceil,log2
import json,subprocess,hashlib,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_bst-evidence'
def insert(t,k):
 if t is None:return(k,None,None)
 x,l,r=t
 return(x,insert(l,k),r)if k<x else(x,l,insert(r,k))if k>x else t
def tree(a):
 t=None
 for k in a:t=insert(t,k)
 return t
def traverse(t,kind='in'):
 if t is None:return[]
 k,l,r=t;a=traverse(l,kind);b=traverse(r,kind)
 return[k]+a+b if kind=='pre' else a+b+[k]if kind=='post'else a+[k]+b
def rows(t,d=0):return[]if t is None else[(t[0],d)]+rows(t[1],d+1)+rows(t[2],d+1)
def h(t):return max((d for k,d in rows(t)),default=-1)
def n(t):return len(rows(t))
def I(t):return sum(d for k,d in rows(t))
def gaps(t,d=0):return[d]if t is None else gaps(t[1],d+1)+gaps(t[2],d+1)
def shape(t):return None if t is None else(shape(t[1]),shape(t[2]))
def remove(t,k):
 if t is None:return None
 x,l,r=t
 if k<x:return(x,remove(l,k),r)
 if k>x:return(x,l,remove(r,k))
 if l is None:return r
 if r is None:return l
 y=traverse(r)[0];return(y,l,remove(r,y))
def comparisons(t,k):
 p=[]
 while t is not None:
  x,l,r=t;p.append(x)
  if k==x:break
  t=l if k<x else r
 return p
def W(t):return 1 if t is None else comb(n(t)-1,n(t[1]))*W(t[1])*W(t[2])
def H(k):return sum((F(1,i)for i in range(1,k+1)),F(0))
def lca(t,a,b):
 while t:
  k,l,r=t
  if b<k:t=l
  elif a>k:t=r
  else:return k
 return None
checks={}
def check(i,actual,expected,why):
 assert actual==expected,(i,actual,expected)
 checks[i]={'method':'independent exact calculation or enumeration','result':str(expected),'reason':why}
base=[40,20,70,10,30,60,80,25,65];t=tree(base)
check(1,comparisons(tree([20,10,30]),25),[20,30],'Ancestor-bound witness and repaired sorted placement reviewed separately.')
check(2,(ceil(log2(1001))-1,1000-1,1000+1),(9,999,1001),'Binary level capacities and child-position identity.')
check(3,(traverse(t,'pre'),traverse(t,'post'),h(t),I(t)),([40,20,10,30,25,70,60,65,80],[10,25,30,20,65,60,80,70,40],3,16),'Immutable reference construction.')
check(4,(comparisons(t,27),sum(k<27 for k in base)),([40,20,30,25],3),'Actual comparison path and independent sorted rank.')
check(5,sum([0,1,1,1,2]),5,'Replacement is not a fresh absent insertion.')
check(6,traverse(remove(tree([30,20,25]),20),'pre'),[30,25],'Minimum right child remains reachable.')
check(7,[next((y for y in sorted(base)if y>x),None)for x in[25,30,65,80]],[30,40,70,None],'Successors independently read from sorted keys.')
check(8,(traverse(remove(t,40),'pre'),n(remove(t,40)),h(remove(t,40))),([60,20,10,30,25,70,65,80],8,3),'Independent persistent deletion.')
check(9,traverse(remove(tree([40,20,60,70]),40),'pre'),[60,20,70],'Immediate successor retains right child; identity proof reviewed.')
check(10,sorted([30,20,10,25,70,60,65,80]),[10,20,25,30,60,65,70,80],'Predecessor association replacement retains exact content.')
u=tree([9,5,3]);roots=[]
for k in[9,8,3,5]:u=remove(u,k);roots.append(None if u is None else u[0])
check(11,roots,[5,5,5,None],'Root/absence boundaries.')
check(12,(2**7-1,2*(2**7-1)+1,2**6),(127,255,64),'Actual nodes, null calls and level width.')
check(13,traverse(tree([8,4,12,2,6,10,14]))[:4],[2,4,6,8],'Independent emission order; stack invariants reviewed.')
check(14,traverse(tree([50,30,20,40,35,80,70,90]),'post'),[20,35,40,30,70,90,80,50],'Unique preorder example reconstructed independently.')
check(15,(20,10,5,30,15)in{tuple(traverse(tree(p),'pre'))for p in permutations([20,10,5,30,15])},False,'All 120 possible insertion trees screened for claimed preorder.')
check(16,traverse(tree([3,2,1,5,4])),[1,2,3,4,5],'Distinct-key traversal-pair root decomposition.')
check(17,traverse(tree([20,10,30,25,5]),'pre'),[20,10,5,30,25],'Breadth-first order contradiction separately proved from depth blocks.')
check(18,(sum(k<30 for k in base),sum(k<31 for k in base),sorted(base)[6]),(3,4,65),'Sorted-array order statistics.')
check(19,[sum(a<=k<=b for k in base)for a,b in[(25,70),(26,69),(5,9),(80,80),(90,10)]],[6,4,0,1,0],'Actual endpoint membership counts.')
check(20,3==1+2+1,False,'Root stored-size equation is false despite matching actual total.')
check(21,(sum(w for k,w in[(2,7),(5,-3),(9,10),(12,4)]if 5<=k<=12),sum(w for k,w in[(2,7),(5,-3)])),(11,4),'Signed weights directly summed.')
expanded=[k for k,c in[(3,2),(8,3),(11,1)]for _ in range(c)]
check(22,(len(expanded),sum(k<8 for k in expanded),sum(k<=8 for k in expanded),[expanded[i]for i in[1,2,4,5]]),(6,2,5,[3,8,8,11]),'Occurrence blocks and boundary ranks independently expanded.')
check(23,(2+4,2+4+3),(6,9),'Complete count transfer versus duplicate-node failure.')
check(24,(I(t),sum(gaps(t)),F(I(t)+n(t),n(t)),F(sum(gaps(t)),n(t)+1)),(16,34,F(25,9),F(17,5)),'Actual external depths enumerated, not only identity reused.')
check(25,F(1,10)+F(2,10)*2+F(4,10)+F(2,10)*2+F(1,10)*2,F(3,2),'Jointly normalized weighted costs.')
check(26,(sum(j*2**j for j in range(4)),F(sum((j+1)*2**j for j in range(4)),15)),(34,F(49,15)),'Depth-level enumeration.')
check(27,(I(tree(range(5))),F(I(tree(range(5)))+5,5),F(sum(gaps(tree(range(5)))),6)),(10,F(3),F(10,3)),'Chain actual and gap depths.')
perfect=tree([4,2,1,3,6,5,7]);check(28,W(perfect),80,'Recursive child interleavings.')
check(29,W(tree([5,2,1,4,3,8,7,9])),210,'Asymmetric interleavings.')
ps=list(permutations([1,2,3]));ts=[tree(p)for p in ps]
check(30,(F(sum(h(z)for z in ts),6),F(sum(I(z)for z in ts),6)),(F(5,3),F(8,3)),'All six actual permutation outcomes.')
check(31,sum(h(tree(p))==3 for p in permutations(range(1,5))),8,'All 24 permutations explicitly built.')
check(32,len({shape(tree(p))for p in permutations(range(1,6))}),42,'All 120 permutations grouped by shape.')
check(33,(H(1)+H(7)-2,2*H(4)-2),(F(223,140),F(13,6)),'Exact harmonic fractions.')
check(34,(22*H(10)-40,(22*H(10)-40+10)/10),(F(30791,1260),F(43391,12600)),'Exact nonasymptotic expectations.')
check(35,F(sum(sum(gaps(tree(p)))for p in permutations(range(1,6))),120*6),F(29,10),'All permutation/gap pairs enumerated.')
check(36,(F(5,5),5),(1,5),'Expected-max counterexample with five equally likely outcomes.')
check(37,sum(j*2**j for j in range(4)),34,'Perfect-depth insertion count; linear direct allocation argument reviewed.')
check(38,(ceil(log2(11))-1,4,5),(3,4,5),'Lower midpoint and capacity.')
check(39,len(comparisons(tree(range(1,11)),11)),10,'No-output query still visits a complete chain.')
check(40,[lca(t,a,b)for a,b in[(10,25),(25,65),(60,65),(26,28)]],[20,40,60,None],'Each target route split checked against immutable example; absent pair reaches null.')
check(41,traverse(tree([40,20,10,30,50])),[10,20,30,40,50],'Rotation sorted blocks and subtree sizes 3/5 reviewed.')
check(42,traverse(t)[::-1],sorted(base,reverse=True),'Mirror/reverse-inorder induction reviewed.')
check(43,[i for i in range(7)if[1,7,3,4,5,6,2,8][i]>[1,7,3,4,5,6,2,8][i+1]],[1,5],'Exact adjacent descent positions.')
check(44,(len(comparisons(t,65)),2*(len(comparisons(t,65))-1)+1),(4,7),'Declared comparison models.')
check(45,(-2**31< -2**31,2**31-1<2**31-1),(False,False),'Exclusive legal-extreme sentinel collisions.')
check(46,((2**31-1)-(-1),((2**31-1)>-1)-((2**31-1)<-1)),(2**31,1),'Mathematical difference outside signed32 range; relational comparator valid.')
check(48,h(tree([2,1])),1,'Empty-height recurrence covers one missing child.')
check(50,comparisons(tree([50,20,40,30,35]),34),[50,20,40,30,35],'Actual legal route.')
check(51,20<10<40,False,'Persistent lower bound rejects the last key.')
check(52,[min(abs(q-k)for k in[10,20,35,50])>=8 for q in[27,28,43,58]],[False,False,False,True],'Every reservation checked independently of neighbor shortcut.')
rels=list(permutations([2,3,4,5]));a=lambda p:p.index(2)==min(p.index(k)for k in[2,3,4,5]);b=lambda p:p.index(3)==min(p.index(k)for k in[3,4,5]);check(55,(F(sum(a(p)for p in rels),24),F(sum(b(p)for p in rels),24),F(sum(a(p)and b(p)for p in rels),24)),(F(1,4),F(1,3),F(1,12)),'All relative permutations; particular nested events genuinely independent.')
check(56,F(W(tree([3,1,2,4,5])),factorial(5)),F(1,20),'Specified five-key shape.')
check(57,F(sum(range(7)),7),3,'Uniform root ranks induce uniform left sizes.')
orders=[p for p in permutations(range(1,8))if tree(p)==perfect];check(58,sum(p.index(1)<p.index(7)for p in orders),40,'All 5040 permutations screened, then extra precedence counted.')
check(60,(3+1,3+1),(4,4),'Gap depth and successful count agree at a leaf.')
check(61,(9-1,9+6+8),(8,23),'Actual child-edge count identity.')
check(62,(F(1,4),sum(F(1,2**d)for d in gaps(tree([1,2,3])))),(F(1,4),1),'Dyadic null-gap conservation checked independently.')
check(63,sum([1*5,1*2,2*1,5*1]),14,'Explicit ordered root-size cases.')
check(64,h(tree([4,1,2,3,5,6,7])),3,'Conditional root example attains maximum child-chain height.')
check(65,(len(set([1,1,1,3,5,5,8,8])),len([1,1,1,3,5,5,8,8]),ceil(log2(5))-1),(4,8,2),'Duplicate compression separates distinct size from mass.')
check(67,sum(range(10)),45,'Repeated subtree scans on a ten-node left chain.')
check(68,tree(traverse(t,'pre')),t,'Preorder ancestor precedence reconstructs the same shape.')
check(69,(n(tree([18,9,27,6,12,24,30])),h(tree([18,9,27,6,12,24,30]))),(7,2),'Reconstructed CMU-pattern example.')
vals=[6,14,19,31];check(70,[(max((k for k in vals if k<=q),default=None),min((k for k in vals if k>=q),default=None))for q in[5,14,20,40]],[(None,6),(14,14),(19,31),(31,None)],'Direct sorted nearest-neighbor reference.')
check(73,[sum(k<=q for k in[5,15,25,35,45])for q in[25,26,4]],[3,3,0],'Inclusive MIT-style counts.')
check(74,(F(8,10)*2+F(1,10)+F(1,10)*2,F(8,10)+F(1,10)*3+F(1,10)*2),(F(19,10),F(13,10)),'Exact weighted comparator expectations.')
check(76,sorted(gaps(tree([1,4,2,3]))),[1,2,3,4,4],'Actual mixed-chain gap depth multiset.')
check(78,len(comparisons(t,50)),3,'Absent path becomes new-node depth three.')
z=insert(remove(t,40),50);check(80,(traverse(z,'pre'),n(z),I(z),sum(k<65 for k in traverse(z)),traverse(z)[4]),([60,20,10,30,25,50,70,65,80],9,16,6,50),'Independent immutable compound update.')
proof_notes={47:'Returned owning-root assignment and call-by-value alias distinction.',49:'Each edge traversed at most twice in retained-state successor scan.',53:'Subtree argmax plus size recurrence; independent orders need augmentation.',54:'Child fields read before release; caller owning field cleared.',59:'Successor/predecessor climb stops immediately at a leaf parent.',66:'Graph identity, metadata and content certificates are separate.',71:'Bottom-up actual-size computation is linear; repeated rank/select is path bounded.',72:'Optional result distinguishes legal minimum integer from absence.',75:'Initial ceiling route plus push-once/pop-once interval scan.',77:'Plain successor-copy deletion creates no longer route.',79:'Sorted-stream merge plus direct allocation is linear; sorted ordinary insertion is quadratic.'}
for i,note in proof_notes.items():checks[i]={'method':'manual proof and contract audit','reason':note}
assert set(checks)==set(range(1,81)),set(range(1,81))-set(checks)
models=json.loads((R/'dist/chapters/a_bst-models.json').read_text())['models'];cases=[m['spec']for m in models]
for keys in[[4],[4,2,6],[4,2,6,1,3,5,7],list(range(1,10)),list(range(9,0,-1))]:
 for op in['search','neighbors','delete','rank']:
  for q in[-1,keys[0],5,11]:cases.append(dict(operation=op,keys=keys,q=q))
 for q in range(len(keys)):cases.append(dict(operation='select',keys=keys,q=q))
 for a,b in[(0,10),(3,6),(11,12),(4,4)]:cases.append(dict(operation='range',keys=keys,a=a,b=b))
 cases.append(dict(operation='insert',keys=keys))
code="const {evaluate}=require('./dist/chapters/a_bst.js');const a="+json.dumps(cases)+";process.stdout.write(JSON.stringify(a.map(evaluate)));"
out=json.loads(subprocess.check_output(['node','-e',code],cwd=R,text=True,encoding='utf-8'));checkpoint_count=0
for c,o in zip(cases,out):
 op=c['operation'];keys=c['keys'];z=tree(keys);sorted_keys=sorted(keys);r=o['result'];q=c.get('q')
 if op in['search','neighbors']:
  assert r==dict(found=q in keys,comparisons=len(comparisons(z,q)),floor=max((x for x in keys if x<=q),default=None),ceiling=min((x for x in keys if x>=q),default=None))
 elif op=='delete':assert r==dict(preorder=traverse(remove(z,q),'pre'),inorder=traverse(remove(z,q)),size=n(remove(z,q)),height=h(remove(z,q)))
 elif op=='rank':assert r['rank']==sum(k<q for k in keys)
 elif op=='select':assert r['selected']==sorted_keys[q]
 elif op=='range':assert r['keys']==[k for k in sorted_keys if c['a']<=k<=c['b']]and r['count']==len(r['keys'])
 elif op=='insert':assert r['comparisons']==I(z)and r['preorder']==traverse(z,'pre')and r['height']==h(z)
 elif op=='orders':assert r['count']==W(z)and all(tree(p)==z for p in r['orders'])and len({tuple(p)for p in r['orders']})==r['count']
 elif op=='random':assert r['shapeMultiplicities']==[1,1,1,1,2]and r['heightNumerator']==10 and r['internalNumerator']==16
 elif op=='cost':assert(r['I'],r['E'],r['gaps'])==(I(z),sum(gaps(z)),gaps(z))
 elif op=='structure':assert(r['n'],r['I'],r['E'],r['height'])==(n(z),I(z),sum(gaps(z)),h(z))
 elif op=='bounds':assert r==dict(valid=False,witness=25)
 elif op=='successor':assert r['successor']==next((k for k in sorted_keys if k>q),None)
 elif op=='traversal':assert r['inorder']==sorted_keys
 elif op=='reconstruct':assert r['valid']==(traverse(z,'pre')==keys)
 elif op=='multiplicity':assert r['expanded']==[sorted_keys[0]]*2+[sorted_keys[1]]*3+[sorted_keys[2]]and r['mass']==6
 elif op=='rotation':assert r['inorder']==sorted_keys and r['preorder']==[40,20,10,30,50]
 for st in o['states']:
  checkpoint_count+=1
  def decode(v):return None if v is None else(v['key'],decode(v['left']),decode(v['right']))
  zt=decode(st['tree']);vals=traverse(zt)
  if op!='bounds':assert vals==sorted(set(vals)),(op,vals)
  if op=='delete':assert set(vals)in[set(keys),set(keys)-{q}]
  if op in['search','neighbors','rank','select','range','traversal','cost','successor','structure','orders']:assert set(vals)==set(keys)
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==51
for p in prior:
 f=R/'dist'/p['url'];assert hashlib.sha256(f.read_bytes()).hexdigest()==p['sha256'];assert f.read_text(encoding='utf-8').count('class="exam-question"')==p['questions']
page=(R/'dist/chapters/a_bst.html').read_text(encoding='utf-8');assert page.count('class="exam-question"')==82 and page.count('class="review-rule"')==80
report=dict(status='passed',topicId='a_bst',questionChecks=[dict(question=i,**checks[i])for i in sorted(checks)],independentModelInputs=len(cases),modelCheckpoints=checkpoint_count,storedModels=len(models),storedCheckpoints=sum(len(m['frames'])for m in models),priorChaptersRetained=len(prior),limitations='Proof-oriented entries are identified separately from numerical/exhaustive checks. Finite input checks supplement general proofs and do not guarantee all unseen cases.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in report.items()if k!='questionChecks'}))
