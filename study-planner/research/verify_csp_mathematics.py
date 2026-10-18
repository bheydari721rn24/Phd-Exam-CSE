"""Independent finite oracles test the code extracted from the actual teaching page."""
from pathlib import Path
from itertools import product,permutations
from collections import Counter
from html import unescape
import hashlib,json,re,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];B=R/'research';sys.path.insert(0,str(B/'exam-rewrite'))
from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/i_csp.html').read_text(encoding='utf8')
code=unescape(re.search(r'<pre><code class="language-python">([\s\S]*?)</code>',page)[1]);ns={};exec(compile(code,'printed-csp.py','exec'),ns)
assert code.strip()==(B/'csp_exact.py').read_text(encoding='utf8').strip(),'Printed algorithm differs from source'
CSP,ac3,solve=ns['CSP'],ns['ac3'],ns['solve'];count=0
def check(value,message=''):
 global count
 assert value,message
 count+=1
vs=['A','B','C'];pairs=list(product([0,1],repeat=2));edges=[('A','B'),('A','C'),('B','C')]
tables=[{p for i,p in enumerate(pairs)if mask>>i&1}for mask in range(16)]
def canonical(solutions,variables):return sorted(tuple(s[v]for v in variables)for s in solutions)
for selected in product(tables,repeat=3):
 c=CSP({v:[0,1]for v in vs},[dict(x=x,y=y,allowed=[list(p)for p in t])for(x,y),t in zip(edges,selected)])
 expected=[t for t in product([0,1],repeat=3)if all((t[vs.index(x)],t[vs.index(y)])in r for(x,y),r in zip(edges,selected))]
 ok,D,_=ac3(c,record=False)
 check(all(all(t[i]in D[v]for i,v in enumerate(vs))for t in expected),'Propagation lost a solution')
 check(ok or not expected,'Failure on a satisfiable input')
 if ok:check(all(any((a,b)in c.relations[x,y]for b in D[y])for x,y in c.arcs()for a in D[x]),'Claimed fixed point lacks support')
 for mode in ['plain','fc','mac']:
  check(canonical(solve(c,mode),vs)==expected,'Solver mismatch '+mode)
  first=solve(c,mode,False);check(bool(first)==bool(expected)and(len(first)<=1)and all(tuple(s[v]for v in vs)in expected for s in first),'First-solution mode incorrect')
exhaustive=count
for domains,n in [({'X':[]},0),({'X':[1,2,3]},3),({},1)]:
 c=CSP(domains,[])
 for mode in ['plain','fc','mac']:check(len(solve(c,mode))==n)
c=CSP({'X':[0,1],'Y':[0,1]},[dict(x='X',y='Y',allowed=[[0,0],[1,1]]),dict(x='Y',y='X',allowed=[[0,1],[1,0]])]);check(not solve(c),'Reversed duplicate constraints not conjoined')
models=json.loads((B/'i_csp-models.json').read_text(encoding='utf8'))['models'];model_checks=0
for m in models:
 c=CSP(m['domains'],m['constraints'])
 expected=[dict(zip(c.variables,t))for t in product(*(m['domains'][v]for v in c.variables))if all((t[c.variables.index(r['x'])],t[c.variables.index(r['y'])])in{tuple(p)for p in r['allowed']}for r in m['constraints'])]
 check(canonical(m['solutions'],c.variables)==canonical(expected,c.variables),m['id']+' solution list')
 for f in m['frames']:
  if not f.get('before')or not f['supports']:continue
  x,y=f['arc'];table=c.relations[x,y];before=f['before'];unsupported=[]
  for s in f['supports']:
   a=s['tail'];w=s['head'];candidates=[b for b in before[y]if(a,b)in table]
   check((w is None and not candidates)or(w in candidates),m['id']+' invalid witness');model_checks+=1
   if not candidates:unsupported.append(a)
  check(unsupported==f['removed']);check(f['domains'][x]==[a for a in before[x]if a not in unsupported]);check(all(f['domains'][v]==before[v]for v in c.variables if v!=x))
  check(all(tuple(a)in c.relations for a in f['queue']))
lookup={m['id']:m for m in models}
check([f['arc']for f in lookup['strict-3']['frames']if f['kind']=='revise']==[['A','B'],['B','A'],['B','C'],['C','B'],['A','B']])
for id,n in [('sum-four',2),('strict-4',4),('holes',4),('mit-colors',1),('cycle-3',0),('cycle-4',2),('rollback',1),('lcv',13),('auth-numeric',6),('auth-map',1),('scope-root',2)]:check(len(lookup[id]['solutions'])==n,id)
c=CSP(lookup['auth-numeric']['domains'],lookup['auth-numeric']['constraints']);closures=[];revisions=[]
for q in permutations(c.arcs()):
 ok,D,events=ac3(c,queue=q);check(ok and D=={'X':[1,2],'Y':[1,2,3,4],'Z':[2],'W':[2]});revisions.append(sum(f['kind']=='revise'for f in events));check(max(Counter(tuple(f['arc'])for f in events if f['kind']=='revise').values())<=4)
queen_solutions=[t for t in product(range(1,5),repeat=4)if all(t[i]!=t[j]and abs(t[i]-t[j])!=j-i for i in range(4)for j in range(i+1,4))];check(queen_solutions==[(2,4,1,3),(3,1,4,2)])
queencost=[]
for r in range(1,5):
 t=(r,1,3,4);queencost.append(sum(t[i]==t[j]or abs(t[i]-t[j])==j-i for i in range(4)for j in range(i+1,4)))
check(queencost==[4,2,2,2])
for d in range(2,5):
 for k in range(3,7):
  actual=sum(all(t[i]!=t[(i+1)%k]for i in range(k))for t in product(range(d),repeat=k));check(actual==(d-1)**k+(-1)**k*(d-1))
check(3**5==243 and 120*243==29160 and 4**5==1024 and sum(3**k for k in range(6))==364)
for m in models:
 if m['id']in ['chain-fc','chain-mac','rollback','rollback-zero','star','tree']:continue
 c=CSP(m['domains'],m['constraints']);ok,D,frames=ac3(c);freq=Counter(tuple(f['arc'])for f in frames if f['kind']=='revise');check(all(n<=max(map(len,c.initial.values()),default=0)for n in freq.values()),'Arc processed too often')
maths=re.findall(r'<math\b[\s\S]*?</math>',page)
for s in maths:
 root=ET.fromstring(s);check(not closing_script_bases(root));check(not delimiter_issues(root))
 for x in root.iter():
  tag=x.tag.split('}')[-1]
  if tag in ['msub','msup','munder','mover','mfrac']:check(len(x)==2)
  if tag in ['msubsup','munderover']:check(len(x)==3)
check(len(re.findall(r'class="exam-question',page))==54);check(not re.search('[\u0600-\u06ff]',page));check('MATHSLOT'not in page and '<!-- CSP:'not in page)
report={'date':'2026-10-18','status':'passed','assertions':count,'exhaustiveSystems':4096,'exhaustiveAssertions':exhaustive,'modelWitnessChecks':model_checks,'numericQueueOrders':len(revisions),'numericRevisionRange':[min(revisions),max(revisions)],'nativeMathExpressions':len(maths),'printedCodeSha256':hashlib.sha256(code.encode()).hexdigest(),'queenScores':queencost,'inputSha256':{p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in ['research/csp_exact.py','research/i_csp.en.md','research/i_csp-problems.en.md','research/i_csp-review.en.md','research/i_csp-models.json','dist/chapters/i_csp.html']},'limits':'All4096 three-variable Boolean binary-table systems and stated finite numeric cases; general correctness also relies on the displayed proofs. Not a universal correctness or exam-performance guarantee.'}
(B/'i_csp-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print(report)
