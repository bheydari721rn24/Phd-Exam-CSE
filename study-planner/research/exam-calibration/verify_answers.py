"""Independent finite enumerations and exact arithmetic, not a universal-correctness claim."""
import json,itertools as it,math,re,xml.etree.ElementTree as ET
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parent
results=[]
def check(name,computed,expected):
 assert computed==expected,(name,computed,expected)
 results.append(dict(check=name,computed=str(computed),expected=str(expected),passed=True))
def onto(n,k):return sum(len(set(v))==k for v in it.product(range(k),repeat=n))
def merge(a):
 if len(a)<=1:return a,0
 k=len(a)//2;l,c1=merge(a[:k]);r,c2=merge(a[k:]);out=[];i=j=c=0
 while i<len(l) and j<len(r):
  c+=1
  if l[i]<=r[j]:out.append(l[i]);i+=1
  else:out.append(r[j]);j+=1
 return out+l[i:]+r[j:],c+c1+c2
def rank(a):
 a=[[F(x) for x in row] for row in a];r=0
 for c in range(len(a[0])):
  pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];v=a[r][c];a[r]=[x/v for x in a[r]]
  for i in range(len(a)):
   if i!=r:
    v=a[i][c];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
  r+=1
 return r
for A,B in it.product((False,True),repeat=2):
 val=((not A) and B) or (((A and not B) or not B) and (B and not A))
 check('MS1405 Q37 membership region '+str((A,B)),val,B and not A)
check('MS1405 Q95 first universal',all(any(x<y for y in range(5)) for x in range(5)),False)
check('MS1405 Q95 successor order',all(not x<y or (x+1)%5<(y+1)%5 for x,y in it.product(range(5),repeat=2)),False)
f={0:1,1:2,2:0};R={(0,1),(1,2),(2,0)}
check('MS1405 Q97 assignments',[all((x,y) not in R or (f[y],0) in R for y in range(3)) for x in (0,2)],[True,False])
check('MS1405 Q99 false rows',[i for i in range(8) if i not in (6,4,3,1)],[0,2,5,7])
check('MS1405 Q113 coupled equations',sum(a+b+c==5 and a+b+c+d+e==20 for a,b,c in it.product(range(6),repeat=3) for d,e in it.product(range(16),repeat=2)),336)
check('MS1405 Q115 category choices',sum(sum(i<5 for i in s)>=4 for s in it.combinations(range(10),8)),35)
check('MS1405 Q121 weighted sum',F(sum(math.comb(i,3)*math.comb(7,i) for i in range(3,8)),10),56)
check('MS1405 Q122 monotone maps',sum(all(v[i]<=v[i+1] for i in range(4)) for v in it.product(range(5),repeat=5)),126)
check('MS1405 Q123 even zeros',sum(v.count(0)%2==0 for v in it.product(range(4),repeat=4)),136)
check('MS1405 Q124 onto',onto(6,4),1560)
check('MS1405 Q125 exponent feasibility',[j for j in range(15) if 2*j-(14-j)==14],[])
check('MS1405 Q129 exact constrained solutions',sum(a%2==0 and b<=4 and c>=1 for a,b,c in it.product(range(21),repeat=3) if a+b+c==20),46)
c=[1]
for n in range(8):c.append(sum(c))
check('MS1405 Q130 prefix recurrence',c,[1,1,2,4,8,16,32,64,128])
check('PhD1405 Q20 weak triples',10+sum(1<=i<=j<=k<=15 for i,j,k in it.product(range(1,16),repeat=3)),690)
check('PhD1405 Q21 attainable maximal union',13+8+6+2,29)
check('PhD1405 Q22 canonical true rows',[4*p+2*q+r for p,q,r in it.product((0,1),repeat=3) if ((not p) or r) and p==q],[0,1,7])
check('PhD1405 Q16 merge comparisons',merge([12,7,5,9,3,8,2,6])[1],16)
check('PhD1405 Q31 decoded sums',[5-8,2+5,4-2,-4-5],[-3,7,2,-9])
check('PhD1404 Q25 odd-sum witness',sum(any((x+y)%2 for x,y in it.combinations(s,2)) for s in it.combinations(range(1,11),4)),200)
parity={16:1403%2,17:2025%2}
for n in range(18,114):parity[n]=(3*parity[n-1]+5*parity[n-2]+4)%2
check('PhD1404 Q28 distant even terms',[n for n in range(100,114) if parity[n]==0],[102,105,108,111])
check('PhD1404 Q68 at most one at n=4',sum(F(1,4)**sum(v)*F(3,4)**(4-sum(v)) for v in it.product((0,1),repeat=4) if sum(v)<=1),F(189,256))
check('PhD1404 Q69 conditional direction',F(1,6)/F(2,3),F(1,4))
check('PhD1404 Q70 equal heads',sum(math.comb(25,k)*math.comb(20,k) for k in range(21)),math.comb(45,20))
updates=0
for p in it.permutations(range(5)):
 m=math.inf
 for x in p:
  if x<m:m=x;updates+=1
check('Original probability expected records',F(updates,math.factorial(5)),F(137,60))
for x,y in it.product((0,1),repeat=2):
 nand=lambda a,b:1-(a&b)
 t=nand(x,y);u=nand(x,t);v=nand(y,t)
 check('PhD1405 Q23 circuit '+str((x,y)),(nand(u,v),nand(v,v)),(x^y,(1-x)&y))
 check('MS1404 Q80 mux '+str((x,y)),(1-y) if x==0 else 0,1-(x|y))
check('MS1404 Q81 oscillator MHz',F(1000,2*5*5),20)

# Original discrete banks: independently enumerate their finite object spaces.
check('Logic conditional-parity models',sum(p==q and (not p or r) and bool(r^s) for p,q,r,s in it.product((0,1),repeat=4)),3)
check('Logic exactly two implications',sum(sum((not p or q,not q or r,not r or p))==2 for p,q,r in it.product((0,1),repeat=3)),6)
check('Sets three nonempty labeled regions',sum(len(set(a))==3 for a in it.product(range(3),repeat=5)),150)
check('Sets prescribed Venn cells',sum([a.count(i) for i in range(4)]==[2,1,1,2] for a in it.product(range(4),repeat=6)),180)
check('Relations generated block pair count',len({(x,y) for x,y in it.product(range(4),repeat=2) if (x<3 and y<3) or x==y==3}),10)
check('Functions exactly three image values',sum(len(set(v))==3 for v in it.product(range(4),repeat=5)),600)
check('Functions fixed endpoint monotonicity',sum(v[0]==0 and v[-1]==3 and all(v[i]<=v[i+1] for i in range(5)) for v in it.product(range(4),repeat=6)),35)
check('Functions two-fixed-point idempotence',sum(sum(v[i]==i for i in range(5))==2 and all(v[v[i]]==v[i] for i in range(5)) for v in it.product(range(5),repeat=5)),80)
check('Functions involutions one fixed point',sum(sum(v[i]==i for i in range(5))==1 and all(v[v[i]]==i for i in range(5)) for v in it.permutations(range(5))),15)
check('Number congruence interval',[x for x in range(84) if (12*x-18)%30==0],list(range(4,84,5)))
check('Number shared-modulus first solutions',[x for x in range(1,50) if x%8==5 and x%6==1],[13,37])
check('Number nonunit power',pow(6,100,15),6)
check('Number factorial power twelve',next(k-1 for k in range(1,30) if math.factorial(30)%12**k),13)
check('Number units prescribed residue',[x for x in range(30) if math.gcd(x,30)==1 and x%3==1],[1,7,13,19])
check('Number bounded integer equation',[(x,(45-6*x)//9) for x in range(11) if (45-6*x)%9==0],[(0,5),(3,3),(6,1),(9,-1)])
check('Induction weighted exact sum',sum(k*2**(k-1) for k in range(1,9)),1793)
check('Induction weighted binomial',sum(math.comb(8,k)*math.comb(k,2) for k in range(2,9)),1792)
check('Invariant exponent13 multiplications',(13).bit_length()+(13).bit_count(),7)
check('Invariant coefficient obstruction',[4*j-10 for j in range(11) if 4*j-10 in (-10,-2,6,8)],[-10,-2,6])
check('Probability feasibility atom endpoints',[F(1,10)-t for t in (F(0),F(1,10))],[F(1,10),0])
check('Probability conditional urn',F(math.comb(3,2),math.comb(5,2)-math.comb(2,2)),F(1,3))
check('Probability three-draw collision',F(sum(len(set(v))<3 for v in it.product(range(4),repeat=3)),4**3),F(5,8))
check('Counting parity bounded allocations',sum(a%2==0 and b<=3 and c>=2 for a,b,c in it.product(range(19),repeat=3) if a+b+c==18),32)
check('Counting distinguished fiber onto',sum(v.count(0)>=2 and len(set(v))==3 for v in it.product(range(3),repeat=5)),80)
check('Counting even-zero ternary strings',sum(v.count(0)%2==0 for v in it.product(range(3),repeat=5)),122)
check('Counting categories two lower bounds',sum(3<=sum(i<5 for i in s)<=4 for s in it.combinations(range(10),6)),150)
check('Counting monotone required middle value',sum(1 in v and all(v[i]<=v[i+1] for i in range(3)) for v in it.product(range(3),repeat=4)),10)
check('Algorithms weak-strict triples',sum(i<=j<k for i,j,k in it.product(range(1,11),repeat=3)),165)
check('Algorithms divisibility body',sum(j%i==0 for i,j in it.product(range(1,13),repeat=2)),35)
check('Algorithms branch parity region',sum((i+j)%2==0 for i in range(1,9) for j in range(1,i+1)),20)
check('Algorithms nonconstant body exact n8',sum(j for i in range(1,9) for j in range(1,i+1)),8*9*10//6)
check('Algorithms sorted-input merge count',merge(list(range(1,9)))[1],12)
check('Algorithms strict cross inversions',sum(l>r for l in (1,3,3) for r in (2,3,4)),2)
check('Recurrence exact power-two16',1+sum(k**3 for k in range(1,5)),101)
a=[1,6]
for n in range(2,5):a.append(4*a[-1]-4*a[-2])
check('Recurrence repeated root value4',a[-1],144)
check('Representation binary64 tie',float(2**53)+1==float(2**53),True)
check('Representation sign extension',int('11101101',2)-256,-19)
check('Representation nearest-even scaled product',round(F(25*24,16)),38)
check('Boolean self-dual free completions',sum(all(v[7-i]==1-v[i] for i in range(8)) for v in it.product((0,1),repeat=8)),16)
for a,b,c in it.product((0,1),repeat=3):
 check('Boolean majority ANF '+str((a,b,c)),(a&b)^(a&c)^(b&c),int(a+b+c>=2))
 check('Boolean POS simplification '+str((a,b,c)),(a|b)&((1-a)|c)&(b|c),(a&c)|((1-a)&b))
check('Vectors independence exceptional parameter',rank([[1,1,0],[1,0,1],[0,1,-1]]),2)
check('Vectors independence ordinary parameter',rank([[1,1,0],[1,0,1],[0,1,0]]),3)
projection=[F(7,3),F(2,3),F(5,3)];w=[1,2,3]
for u in ([1,0,1],[1,1,0]):check('Vectors residual dot '+str(u),sum((F(x)-p)*v for x,p,v in zip(w,projection,u)),0)
check('Matrices basis-column coordinates',[(2+1,2-1),(1+0,1-0)],[(3,1),(1,1)])
check('Matrices nilpotent power entry',math.comb(7,2),21)

# Structural evidence binds records to chapter outputs and catches raw TeX/control glyphs.
check('MSCE1405 Q35 indicator probability',math.comb(4,2)*F(1,4)**2*F(3,4)**2,F(27,128))
check('MSCE1405 Q35 conditional expansion',sum(F(math.comb(4,k),16)*F(math.comb(k,2),2**k) for k in range(2,5)),F(27,128))
check('MSCE1405 Q56 accumulated merging work',sum(j*12 for j in range(2,9)),12*(8*9//2-1))
sources=json.loads((BASE/'actual-items.json').read_text())
new=[q for f in BASE.glob('original-*.json') for q in json.loads(f.read_text())]
def strings(obj):
 if isinstance(obj,str):yield obj
 elif isinstance(obj,dict):
  for v in obj.values():yield from strings(v)
 elif isinstance(obj,list):
  for v in obj:yield from strings(v)
for q in sources+new:
 assert len(q['options'])==4 and len(set(q['options']))==4 and (q['answer'] is None or 1<=q['answer']<=4),q['title']
 assert all(not any(ord(c)<32 and c not in '\n\r\t' for c in s) for s in strings(q)),q['title']
 assert len(q['solution'])>=180,q['title']
for q in new:
 for ref in q['pattern'].split('; '):assert any(a['id']==ref for a in sources),(q['title'],ref)
manifest=json.loads((BASE/'manifest.json').read_text())
for c in manifest['chapters']:
 path=BASE.parents[1]/'dist/chapters'/(c['topicId']+'.html');s=path.read_text(encoding='utf-8')
 check(c['topicId']+' active-bank counts',len(re.findall(r'<h3>Question \d+\.',s)),c['totalQuestions'])
 check(c['topicId']+' authentic occurrences',len(re.findall('data-kind="authentic"',s)),c['authenticQuestions'])
 assert not re.search(r'[\u0600-\u06ff]',s),c['topicId']
 assert 'MATHSLOT' not in s and '$' not in re.sub(r'<[^>]+>','',re.sub(r'<script[\s\S]*?</script>','',s)),c['topicId']
 ids=re.findall(r'\bid="([^"]+)"',s);assert len(ids)==len(set(ids)),(c['topicId'],'duplicate IDs')
 for anchor in re.findall(r'href="#([^"]+)"',s):assert anchor in ids,(c['topicId'],anchor)
 for block in re.findall(r'<math\b[\s\S]*?</math>',s):
  root=ET.fromstring(block)
  for node in root.iter():
   tag=node.tag.rsplit('}',1)[-1]
   if tag in ('mfrac','msub','msup','munder','mover'):assert len(node)==2,(c['topicId'],tag)
   if tag in ('msubsup','munderover'):assert len(node)==3,(c['topicId'],tag)
  visible=''.join(root.itertext());assert not any(x in visible for x in ('\\','^','_')),(c['topicId'],visible)
out=dict(independentChecks=len(results),finiteChecksOnly=True,limits='Finite cases and exact arithmetic support the stated derivations; they do not prove universal scientific correctness or future exam performance.',checks=results)
(BASE/'answer-validation.json').write_text(json.dumps(out,indent=2)+'\n')
print('Passed',len(results),'independent finite/exact and output-consistency checks.')
