"""Independent exhaustive experiment oracles, not a replay of the visual evaluator."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from math import comb,exp,factorial,isclose
import json,re,hashlib,subprocess,xml.etree.ElementTree as ET
import sympy as S
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_distributions-evidence'
report=dict(status='in_progress',enumeratedExperiments=0,checkpointChecks=0)
def eq(a,b):assert isclose(float(a),float(b),abs_tol=2e-10,rel_tol=1e-9),(a,b)
def moments(law):
 law=list(law)
 mean=sum(k*p for k,p in law);second=sum(k*k*p for k,p in law);return mean,second-mean*mean
for n in range(9):
 for p in [F(0),F(1,5),F(1,2),F(4,5),F(1)]:
  values={k:F(0)for k in range(n+1)}
  for path in product([0,1],repeat=n):
   k=sum(path);values[k]+=p**k*(1-p)**(n-k)
  for k,mass in values.items():eq(mass,comb(n,k)*p**k*(1-p)**(n-k))
  mu,v=moments(values.items());eq(mu,n*p);eq(v,n*p*(1-p));report['enumeratedExperiments']+=1
for N in range(1,10):
 for K in range(N+1):
  for n in range(N+1):
   values=[sum(i<K for i in sample)for sample in combinations(range(N),n)]
   counts={k:F(values.count(k),len(values))for k in set(values)}
   lo=max(0,n-N+K);hi=min(n,K);assert set(counts)==set(range(lo,hi+1))
   for k,p in counts.items():eq(p,F(comb(K,k)*comb(N-K,n-k),comb(N,n)))
   mu,v=moments(counts.items());eq(mu,F(n*K,N));eq(v,0 if N==1 else n*F(K,N)*(1-F(K,N))*F(N-n,N-1));report['enumeratedExperiments']+=1
for N in range(1,10):
 for K in range(1,N+1):
  for r in range(1,K+1):
   positions=[a[r-1]for a in combinations(range(1,N+1),K)]
   mu=sum(positions)/len(positions);v=sum(x*x for x in positions)/len(positions)-mu*mu
   eq(mu,F(r*(N+1),K+1));eq(v,F(r*(K-r+1)*(N+1)*(N-K),(K+1)**2*(K+2)))
   for t in range(r,N-K+r+1):eq(F(positions.count(t),len(positions)),F(comb(t-1,r-1)*comb(N-t,K-r),comb(N,K)))
   report['enumeratedExperiments']+=1
data=json.loads((R/'dist/chapters/s_distributions-models.json').read_text(encoding='utf-8'))
for m in data['models']:
 for f in m['frames']:
  ET.fromstring(f['svg']);z=f['snapshot']['state'];s=m['spec'];report['checkpointChecks']+=1
  if z['kind']=='flow':
   eq(sum(z['source']),1);assert 0<=sum(z['destination'])<=1+1e-9
   t=z['step'];n=t-1
   if s['kind']=='independent':
    expected=[0]*(n+1)
    for path in product([0,1],repeat=n):
     probability=1
     for i,b in enumerate(path):probability*=s['probabilities'][i]if b else 1-s['probabilities'][i]
     expected[sum(path)]+=probability
   else:
    expected=[comb(s['K'],k)*comb(s['N']-s['K'],n-k)/comb(s['N'],n)if 0<=k<=s['K']and 0<=n-k<=s['N']-s['K']else 0 for k in range(n+1)]
   for k,p in enumerate(expected):eq(z['source'][k],p)
   if z.get('from')is not None:eq(z['transferred'],z['source'][z['from']]*z['branchProbability'])
  elif z['kind']=='wait':
   r=s['r'];t=z['step'];p=s['p'];oracle=[0]*(r+1)
   for path in product([0,1],repeat=t):
    k=sum(path);oracle[min(k,r)]+=p**k*(1-p)**(t-k)
   for a,b in zip(z['mass'],oracle):eq(a,b)
   eq(sum(z['mass']),1)
   eq(z['newFinish'],comb(t-1,r-1)*p**r*(1-p)**(t-r)if t>=r else 0)
  elif z['kind']=='subsets':
   allsets=list(combinations(range(1,z['N']+1),z['K']))[:z['processed']]
   for t,count in enumerate(z['counts']):assert count==sum(a[z['r']-1]==t for a in allsets)
  elif z['kind']=='classification':
   if z.get('poisson'):
    a=z['step']/3;b=2*z['step']/3
    for i,j,p in z['law']:eq(p,exp(-a)*a**i/factorial(i)*exp(-b)*b**j/factorial(j))
    eq(sum(p for i,j,p in z['law'])+z['tail'],1)
   else:
    expected={}
    for path in product([0,1,2],repeat=z['step']):
     a=path.count(0);b=path.count(1);p=(.25)**(a+path.count(2))*.5**b;expected[(a,b)]=expected.get((a,b),0)+p
    for i,j,p in z['law']:eq(p,expected[(i,j)])
    eq(sum(p for i,j,p in z['law']),1)
  elif z['kind']=='transform':
   assert 0<=sum(z['destination'])<=1+1e-9
   if f is m['frames'][-1]:
    oracle={'censored':[0,.5,.25,.125,.125],'truncated':[0,8/15,4/15,2/15,1/15],'failure-code':[1/16,.5,.25,.125,1/16]}[s['kind']]
    for a,b in zip(z['destination'],oracle):eq(a,b)
  elif z['kind']=='uniform':assert z['y']==[z['a']*x+z['b']for x in z['x']]
  elif s['kind']=='poisson':
   for k,p in z['law']:eq(p,exp(-s['lam'])*s['lam']**k/factorial(k))
  elif s['kind']=='geometric-failures':
   for k,p in z['law']:eq(p,s['p']*(1-s['p'])**k)
  elif s['kind']=='approximation':
   n=z['n'];a=dict(z['law']);b=dict(z['comparison'])
   tvprefix=sum(abs(a[k]-b[k])for k in a)/2
   # Full TV differs from its visible prefix. A rigorous *upper* certificate
   # adds both omitted tails, never normalizes the displayed atoms.
   upper=tvprefix+((1-sum(a.values()))+(1-sum(b.values())))/2
   assert upper<=z['bound']+2e-6,(n,upper,z['bound'])
qs=json.loads((B/'s_distributions-questions.json').read_text(encoding='utf-8'));assert len(qs)==85
ids={m['id']for m in data['models']}
for q in qs:
 assert q.get('modelId',next(iter(ids)))in ids,q['id']
 assert len(q['solution'])>=300
 for field in ['stem','solution']:
  for formula in re.findall(r'\$([^$]+)\$',q[field]):
   assert not re.search(r'[A-Za-z](?:cdot|cap|mid|epsilon|sqrt)|(?:le|ge)sqrt|lambdamu',formula),(q['id'],formula)
auth=json.loads((B/'s_distributions-authentic.json').read_text(encoding='utf-8'))
root=Path(r'C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
for q in auth:
 assert hashlib.sha256((root/q['repoPath']).read_bytes()).hexdigest()==q['sourceSha256']
 assert q['revisited']and q['answerStatus']=='independently_derived_not_official'
eq(comb(4,2)*F(1,4)**2*F(3,4)**2,F(27,128))
eq(F(1,6)/F(2,3),F(1,4))
checks=[
 ('third binomial moment',sum(k**3*F(comb(7,k))*F(2,5)**k*F(3,5)**(7-k)for k in range(8)),F(182,5)),
 ('truncated binomial variance',F(16,3)-F(32,15)**2,F(176,225)),
 ('mixed-binomial zero',((F(3,4)**6+F(1,4)**6)/2),F(365,4096)),
 ('strict geometric interval',F(3,4)**2-F(3,4)**6,F(1575,4096)),
 ('negative wait by five',1-F(3,4)**5-5*F(1,4)*F(3,4)**4,F(47,128)),
 ('finite count by six',F(comb(4,3)*comb(8,3)+comb(4,4)*comb(8,2),comb(12,6)),F(3,11)),
 ('multinomial category count',30*F(1,4)*F(1,2)**2*F(1,4)**2,F(15,128)),
 ('success budget',F(2,3)**3*(1+3*F(1,3)),F(16,27)),
 ('conditional allocation',4*F(2,5)*F(3,5)**3,F(216,625))]
for name,a,b in checks:eq(a,b)
report['namedAnswerChecks']=[n for n,_,_ in checks]
cases=[]
for kind in ['binomial','geometric','negative-binomial','hypergeometric','poisson']:
 for n in range(7):
  for p in [.2,.5,1]:
   cases.append(dict(kind=kind,n=n,p=p,r=max(1,n),N=8,K=n,lambdaValue=n/2,limit=12))
js=r"""let s='';process.stdin.on('data',c=>s+=c);process.stdin.on('end',()=>{const a=JSON.parse(s),m=require('./dist/chapters/s_distributions.js');process.stdout.write(JSON.stringify(a.map(z=>m.law({...z,lambda:z.lambdaValue}))));});"""
outputs=json.loads(subprocess.check_output(['node','-e',js],input=json.dumps(cases).encode(),cwd=R))
for s,a in zip(cases,outputs):
 kind=s['kind'];n=s['n'];p=s['p'];r=s['r'];mu,v=moments((z['x'],z['p'])for z in a['masses'])
 eq(sum(z['p']for z in a['masses'])+a['tail'],1)
 if kind=='binomial':eq(mu,n*p);eq(v,n*p*(1-p))
 elif kind=='hypergeometric':eq(mu,n*n/8);eq(v,n*(n/8)*(1-n/8)*(8-n)/7)
 elif kind=='geometric':
  for z in a['masses']:eq(z['p'],p*(1-p)**(z['x']-1))
 elif kind=='negative-binomial':
  for z in a['masses']:eq(z['p'],comb(z['x']-1,r-1)*p**r*(1-p)**(z['x']-r))
 else:
  for z in a['masses']:eq(z['p'],exp(-n/2)*(n/2)**z['x']/factorial(z['x']))
report['editableIndependentCases']=len(cases)
page=(R/'dist/chapters/s_distributions.html').read_text(encoding='utf-8')
assert page.count('class="exam-question"')==88 and page.count('class="review-rule"')==84
assert not re.search(r'[\u0600-\u06ff]',page)
assert 'Phd-Exsd'not in page and 'exsd-'not in page
sys_path=B/'exam-rewrite'
import sys
sys.path.insert(0,str(sys_path))
from math_fences import delimiter_issues,closing_script_bases
mathCount=0
for m in re.findall(r'<math\b[\s\S]*?</math>',page):
 x=ET.fromstring(m);assert not delimiter_issues(x),(x.get('aria-label'),'delimiter');assert not closing_script_bases(x);mathCount+=1
report['staticMathMLChecks']=mathCount
baseline=json.loads((E/'prior-library.json').read_text(encoding='utf-8'))
assert isinstance(baseline,list)or isinstance(baseline,dict)
report['status']='passed'
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
