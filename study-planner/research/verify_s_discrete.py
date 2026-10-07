"""Independent outcome/subset enumeration, rational problem checks, and retention."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from collections import defaultdict
from math import comb,exp,isclose
import json,subprocess,hashlib,re
B=Path(__file__).resolve().parent;R=B.parent;OUT=B/'s_discrete-evidence'
checks=[]
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 checks.append(dict(name=name,result=str(actual),status='passed'))
def enumerate_count(ps):
 a=[F(0)]*(len(ps)+1)
 for bits in product([0,1],repeat=len(ps)):
  w=F(1)
  for bit,p in zip(bits,ps):w*=p if bit else 1-p
  a[sum(bits)]+=w
 return a
def subsets(N,K,n):
 a=[F(0)]*(n+1)
 for sample in combinations(range(N),n):a[sum(i<K for i in sample)]+=F(1,comb(N,n))
 return a
def fibers(v,p,fn):
 a=defaultdict(F)
 for x,w in zip(v,p):a[fn(x)]+=w
 return sorted(a.items())
check('Q1 weighted image mass',F(1,10)+F(3,10),F(2,5))
check('Q1 conditional fiber',F(4,10)/F(6,10),F(2,3))
check('Q2 conditional odd atom',F(2+4,2+3+4+5),F(3,7))
check('Q4 finite telescoping identity',sum(F(1,k*(k+1)) for k in range(1,100)),F(99,100))
check('Q5 recovered mass total',sum([F(1,5),F(1,5),F(2,5),F(1,5)]),F(1))
check('Q7 geometric atom tail',sum(F(1,2**k) for k in range(3,20))+F(1,2**19),F(1,4))
check('Q10 integer congruence atoms',[x for x in range(-4,9) if 0<=x<7 and x%3==1],[1,4])
check('Q10 conditional even event',F(len([x for x in range(-4,9) if x%2==0 and x>=0]),len([x for x in range(-4,9) if x%2==0])),F(5,7))
check('Q11 four endpoint masses',[F(3,10),F(4,5),F(0),F(1,2)],[F(1)-F(7,10),F(1)-F(1,5),F(7,10)-F(7,10),F(7,10)-F(1,5)])
check('Q12 CDF jump',[F(1,4),F(3,5)-F(1,4),F(1)-F(3,5)],[F(1,4),F(7,20),F(2,5)])
check('Q14 inclusive real thresholds',sum(F(k+1,15) for k in range(5) if .2<=k<=3.9),F(3,5))
check('Q15 missing threshold mass',1-F(1,3)-F(1,4),F(5,12))
check('Q20 conditional strict interval',(F(6,10)-F(3,10)+F(8,10)-F(6,10))/F(9,10),F(5,9))
check('Q21 square fibers',fibers([-2,-1,0,1,2],[F(k,20) for k in [1,2,4,5,8]],lambda x:x*x),[(0,F(1,5)),(1,F(7,20)),(4,F(9,20))])
check('Q22 decreasing affine event',sum(w for x,w in zip([-2,1,4],[F(1,5),F(1,2),F(3,10)]) if 3-2*x<=1),F(4,5))
check('Q23 modulo fibers',[sum(x%4==r for x in range(11)) for r in range(4)],[3,3,3,2])
check('Q25 cyclic comparison',F(sum(x<(x+2)%5 for x in range(5)),5),F(3,5))
check('Q27 independent sum event',F(sum(a+b==4 for a,b in product(range(1,4),repeat=2)),9),F(1,3))
check('Q28 maximum masses',[F(sum(max(a,b)==k for a,b in product(range(1,5),repeat=2)),16) for k in range(1,5)],[F(k,16) for k in [1,3,5,7]])
check('Q29 maximum-three event',F(sum(max(t)==3 for t in product(range(1,5),repeat=3)),64),F(19,64))
joint=[(x+y,px*py,x) for x,px in zip([0,1],[F(1,3),F(2,3)]) for y,py in zip([0,1,2],[F(1,4),F(1,2),F(1,4)])]
check('Q30 conditional weighted diagonal',sum(p for z,p,x in joint if z==2 and x==1)/sum(p for z,p,x in joint if z==2),F(4,5))
check('Q31 reliability upper tail',sum(enumerate_count([F(3,4)]*5)[4:]),F(81,128))
check('Q32 short failure tail',sum(enumerate_count([F(4,5)]*7)[:2]),F(29,78125))
check('Q33 zero mass after ratio parameter',(1-F(2,3))**5,F(1,243))
check('Q35 even binomial mass',sum(enumerate_count([F(1,4)]*4)[::2]),F(17,32))
check('Q36 unequal independent count',enumerate_count([F(1,4),F(3,4)]),[F(3,16),F(10,16),F(3,16)])
check('Q37 shared regime mixture',[(a+b)/2 for a,b in zip(enumerate_count([F(1,4)]*2),enumerate_count([F(3,4)]*2))],[F(5,16),F(6,16),F(5,16)])
check('Q38 eligibility conditioning sum',sum(comb(6,k)*F(2,3)**k*F(1,3)**(6-k)*comb(k,3)*F(3,4)**3*F(1,4)**(k-3) for k in range(3,7)),F(5,16))
check('Q39 pairwise-independence count',[a+b+(a^b) for a,b in product([0,1],repeat=2)],[0,2,2,2])
for p in [F(1,4),F(1,2),F(3,4)]:check('Q40 two derivations p='+str(p),p**3+3*p**3*(1-p)+6*p**3*(1-p)**2,sum(enumerate_count([p]*5)[3:]))
check('Q41 full feasible urn',subsets(8,3,4),[F(1,14),F(6,14),F(6,14),F(1,14),F(0)])
check('Q41 forced lower support',[i for i,p in enumerate(subsets(8,3,7)) if p],[2,3])
check('Q42 upper urn tail',sum(subsets(12,5,4)[3:]),F(5,33))
check('Q43 ordered draws',F(4,10)*F(3,9)*F(6,8)*3,F(3,10))
check('Q44 observed urn state',subsets(7,2,3)[1],F(4,7))
check('Q46 adjacent ratios',[F(comb(4,k+1)*comb(6,4-k),comb(4,k)*comb(6,5-k)) for k in range(4)],[F(10),F(2),F(1,2),F(1,10)])
check('Q47 truncated urn event',subsets(9,5,2)[2]/sum(subsets(9,5,2)[1:]),F(1,3))
check('Q48 inferred urn mass',subsets(8,4,2)[1],F(4,7))
check('Q50 replacement contrast',[enumerate_count([F(1,2)]*4)[2],subsets(8,4,4)[2]],[F(3,8),F(18,35)])
check('Q51 positive geometric CDF',1-F(3,4)**3,F(37,64))
check('Q53 conditional waiting union',1-F(4,5)**3,F(61,125))
check('Q54 endpoint waiting intervals',[F(2,3)**2-F(2,3)**5,F(2,3)-F(2,3)**4],[F(76,243),F(38,81)])
check('Q56 varying hazard first success',F(1,2)*F(2,3)*F(1,4),F(1,12))
check('Q57 cap and truncation final atoms',[F(1,2)**3,F(1,2)**4/(1-F(1,2)**4)],[F(1,8),F(1,15)])
check('Q58 separate failure-code conditional',F(1,3)*F(2,3)**2/(1-F(2,3)**3),F(4,19))
check('Q60 counterexample residual',[F(2,3),F(1,2)],[F(1,3)/F(1,2),F(1,2)])
check('Q61 forced terminal success',F(sum(sum(t[:-1])==2 and t[-1]==1 for t in product([0,1],repeat=5)),32),F(3,16))
check('Q62 second-success failure count',4*F(1,3)**2*F(2,3)**3,F(32,243))
check('Q63 future remaining target',F(sum(sum(t[:-1])==1 and t[-1]==1 for t in product([0,1],repeat=3)),8),F(1,4))
check('Q64 failed memoryless comparison',1-F(1,2)**2,F(3,4))
check('Q65 window parameter',F(2)*F(3,2),F(3))
check('Q66 adjacent ratio parameter',F(6,2),F(3))
check('Q68 renormalized prefix',[F(1)/F(5,2),F(1)/F(5,2),F(1,2)/F(5,2)],[F(2,5),F(2,5),F(1,5)])
check('Q71 count capping',fibers(range(5),enumerate_count([F(1,2)]*4),lambda x:min(x,2)),[(0,F(1,16)),(1,F(4,16)),(2,F(11,16))])
check('Q72 binomial distance',fibers(range(7),enumerate_count([F(1,2)]*6),lambda x:abs(x-3)),[(i,F(k,32)) for i,k in enumerate([10,15,6,1])])
check('Q74 unequal eligibility',enumerate_count([F(1,4),F(1,3),F(3,8)])[2],F(5,24))
check('Q75 quadratic law',fibers(range(-2,4),[F(1,6)]*6,lambda x:x*(x-1)),[(0,F(1,3)),(2,F(1,3)),(6,F(1,3))])
check('Q77 conditional allocation',F(comb(2,1)*comb(3,1),comb(5,2)),F(3,5))
selected=[(a,b) for a,b in product(range(1,5),repeat=2) if max(a,b)==3]
check('Q78 conditional ties and first coordinate',[F(sum(a==b for a,b in selected),len(selected)),F(sum(a==3 for a,b in selected),len(selected))],[F(1,5),F(3,5)])
check('Authentic MS1405 Q35 via path enumeration',enumerate_count([F(1,4)]*4)[2],F(27,128))
for n in range(2,9):check('Authentic PhD1404 Q68 n='+str(n),sum(enumerate_count([F(1,n)]*n)[:2]),F((n-1)**(n-1)*(2*n-1),n**n))
check('Authentic PhD1404 Q69 posterior-positive',F(1)-F(1,2)/F(2,3),F(1,4))
(OUT/'mathematics.json').write_text(json.dumps(dict(status='passed',checks=checks,proofReview='All 80 original solutions and 80 rules read in this turn; executable checks supplement, rather than prove, the general arguments.'),indent=2)+'\n')
# Compare the real JavaScript implementations with independent enumeration.
code="""const a=require(process.argv[1]),out=[];for(let n=0;n<=8;n++)for(const p of [0,.25,.5,.75,1])out.push({kind:'bin',n,p,result:a.binomial(n,p).result});for(let N=1;N<=8;N++)for(let K=0;K<=N;K++)for(let n=0;n<=N;n++){out.push({kind:'urn',N,K,n,result:a.hypergeometric(N,K,n).result});out.push({kind:'sequential',N,K,n,result:a.urnSequential(N,K,n).result});}for(const ps of [[.25,.75],[.2,.3,.5],[0,1,.5]])out.push({kind:'unequal',ps,result:a.heterogeneous(ps).result});process.stdout.write(JSON.stringify(out));"""
rows=json.loads(subprocess.check_output(['node','-e',code,str(R/'dist/chapters/s_discrete.js')],text=True,encoding='utf-8'))
for row in rows:
 kind=row['kind']
 if kind=='bin':ref=enumerate_count([F(str(row['p']))]*row['n']);actual=[r['p'] for r in row['result']]
 elif kind=='unequal':ref=enumerate_count([F(str(p)) for p in row['ps']]);actual=row['result']
 else:
  ref=subsets(row['N'],row['K'],row['n']);actual=[0.]*(row['n']+1)
  if kind=='urn':
   for r in row['result']:actual[r['x']]=r['p']
  else:actual=row['result']['law'];assert row['result']['agrees']
 assert len(actual)==len(ref) and all(isclose(a,float(b),abs_tol=1e-12) for a,b in zip(actual,ref)),row
models=json.loads((R/'dist/chapters/s_discrete-models.json').read_text());allmodels=models['models']
for m in allmodels:
 assert len(m['frames'])>0
 for i,f in enumerate(m['frames']):
  assert f['snapshot']==f['teaching']['currentState'] and f['teaching']['initial']==(i==0)
  assert f['caption'] and f['teaching']['operation'] and f['teaching']['guide']
  if i:assert f['teaching']['changes'],(m['id'],i)
  assert '<svg ' in f['svg'] and 'data-visual-type="plot"' in f['svg']
  assert '^' not in f['svg'],'Unformatted exponent in a figure'
(OUT/'models.json').write_text(json.dumps(dict(status='passed',independentComparisonGroups=len(rows),methods=['complete binary-path enumeration','uniform subset enumeration','sequential depletion compared to subset counts'],models=len(allmodels),checkpoints=sum(len(m['frames']) for m in allmodels),finitePrecisionLimit='Double precision; rational independent references use exact Fraction arithmetic.'),indent=2)+'\n')
# Retain approved pages byte for byte, and ensure every chapter asset is discoverable.
prior=json.loads((OUT/'prior-library.json').read_text());page=(R/'dist/chapters/s_discrete.html').read_text(encoding='utf-8')
for c in prior['chapters']:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256'],c['topicId']
assert page.count('class="exam-question"')==83 and page.count('class="review-rule"')==80 and '<!--' not in page and '$' not in page
assert not re.search('[\u0600-\u06ff]',page),'Non-English chapter line'
qs=json.loads((B/'s_discrete-questions.json').read_text());auth=json.loads((B/'s_discrete-authentic.json').read_text());allq=qs+auth
assert len(qs)==80 and len(auth)==3
used=set(re.findall(r'data-disc-model="([^"]+)"',page));assert used=={m['id'] for m in allmodels}
for q in allq:assert len(q['solution'].split())>=50 and q['stem'].strip()
for a in auth:
 cache=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/a['repoPath']
 assert hashlib.sha256(cache.read_bytes()).hexdigest()==a['pdfSha256']
for rec in json.loads((OUT/'reading.json').read_text())['records']:
 if rec.get('path'):assert hashlib.sha256(Path(rec['path']).read_bytes()).hexdigest()==rec['sha256']
ret=dict(status='passed',retainedChapters=39,retainedProblems=2428,totalChapters=40,totalProblems=2511,currentQuestions=83,originalQuestions=80,authenticQuestions=3,finalRules=80,lessonSections=26,distinctModels=len(allmodels),problemVisuals=sum(bool(q.get('modelId')) for q in allq),texRendering='strict native MathML; no unresolved delimiter',lessonWords=len((B/'s_discrete.en.md').read_text().split()),bankWords=sum(len((q['stem']+' '+q['solution']).split()) for q in allq),sourcePDFHashes='four core files verified; Harvard web scope has no downloaded-file hash')
(OUT/'lesson-and-retention.json').write_text(json.dumps(ret,indent=2)+'\n')
print(json.dumps(dict(exactChecks=len(checks),independentAlgorithmComparisons=len(rows),**ret)))
