"""Independent finite checks for instructional results, not a universal proof."""
import itertools,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'research/d_relations.en.md').read_text(encoding='utf-8')
code=re.search(r'```python\n(.*?)\n```',source,re.S).group(1)
env={};exec(code,env);warshall=env['transitive_closure']
def compose(s,r):return {(a,c) for a,b in r for x,c in s if b==x}
def reach(r,n,identity=False):
 result=set()
 for start in range(n):
  seen={start} if identity else set();todo=[b for a,b in r if a==start];seen.update(todo)
  while todo:
   a=todo.pop()
   for x,b in r:
    if x==a and b not in seen:seen.add(b);todo.append(b)
  result.update((start,b) for b in seen)
 return result
def matrix(r,n):return [[(i,j) in r for j in range(n)] for i in range(n)]
def pairs(m):return {(i,j) for i,row in enumerate(m) for j,b in enumerate(row) if b}
counts={'reflexive':0,'symmetric':0,'antisymmetric':0,'asymmetric':0,'equivalence':0,'total_order':0}
for n in range(4):
 coords=list(itertools.product(range(n),repeat=2))
 for bits in range(1<<len(coords)):
  r={p for i,p in enumerate(coords) if bits&(1<<i)};ident={(i,i) for i in range(n)}
  positive=reach(r,n);star=reach(r,n,True)
  assert pairs(warshall(matrix(r,n)))==positive
  assert pairs(warshall(matrix(r,n),include_zero_length=True))==star
  power=ident;unions=set()
  for k in range(1,n+1):power=compose(r,power);unions|=power
  assert unions==positive
  ref=ident<=r;sym=all((b,a) in r for a,b in r);anti=all(a==b or (b,a) not in r for a,b in r);trans=compose(r,r)<=r
  cyclic=all((c,a) in r for a,b in r for x,c in r if b==x)
  euclidean=all((b,c) in r for a,b in r for x,c in r if a==x)
  assert (ref and sym and trans)==(ref and cyclic)==(ref and euclidean)
  assert all((b,a) not in r for a,b in r)==(anti and not (r&ident))
  assert (ref and trans and anti)==(ref and trans and all(not ((a,b) in positive and (b,a) in positive) for a,b in coords if a!=b))
  if n==3:
   for key,value in [('reflexive',ref),('symmetric',sym),('antisymmetric',anti),('asymmetric',all((b,a) not in r for a,b in r)),('equivalence',ref and sym and trans),('total_order',ref and anti and trans and all((a,b) in r or (b,a) in r for a,b in coords))]:counts[key]+=int(value)
assert counts=={'reflexive':64,'symmetric':64,'antisymmetric':216,'asymmetric':27,'equivalence':5,'total_order':6},counts
# Independently confirm the exact illustrative closure stages and wrong-order failure.
cycle={(0,1),(1,2),(2,0)};d=matrix(cycle,4);stage_new=[]
for k in range(4):
 old=[r[:] for r in d];d=[[old[i][j] or old[i][k] and old[k][j] for j in range(4)] for i in range(4)];stage_new.append(sorted(pairs(d)-pairs(old)))
assert stage_new==[[(2,1)],[(0,2),(2,2)],[(0,0),(1,0),(1,1)],[]]
wrong={(0,2),(2,3),(3,1)};d=matrix(wrong,4)
for i in range(4):
 for j in range(4):
  for k in range(4):d[i][j]=d[i][j] or d[i][k] and d[k][j]
assert (0,1) in reach(wrong,4) and not d[0][1]
# Divisor covers and scheduling witnesses are computed from relation definitions.
div=[1,2,3,4,6,12];cov={(a,b) for a in div for b in div if a!=b and b%a==0 and not any(c!=a and c!=b and c%a==0 and b%c==0 for c in div)}
assert cov=={(1,2),(1,3),(2,4),(2,6),(3,6),(4,12),(6,12)}
tasks={(0,2),(0,3),(1,3),(2,4),(3,4),(3,5)};ordered=reach(tasks,6)
chains=[(0,2,4),(1,3,5)];assert all((c[i],c[i+1]) in ordered for c in chains for i in range(len(c)-1))
assert (2,3) not in ordered and (3,2) not in ordered
assert sorted(v for c in chains for v in c)==list(range(6))
problems=(ROOT/'research/d_relations-problems.en.md').read_text(encoding='utf-8');review=(ROOT/'research/d_relations-review.en.md').read_text(encoding='utf-8')
assert re.findall(r'### Problem (\d+)\.',problems)==list(map(str,range(1,47)))
assert problems.count('**Solution.**')==46
assert re.findall(r'^(\d+)\. ',review,re.M)==list(map(str,range(1,73)))
page=(ROOT/'dist/chapters/d_relations.html').read_text(encoding='utf-8');assert page.count('<figure ')==4 and page.count('<h2 ')==12
assert not re.search(r'[\u0600-\u06ff]|\$|\\bar|<!-- INCLUDE',page)
assert 'Student-approved chapter' in page
assert '^' not in page
assert all('include_zero_length' in text for text in re.findall(r'>[^<]*_[^<]*<',page)), 'Unrendered mathematical underscore'
result={'finiteRelationsChecked':sum(1<<(n*n) for n in range(4)),'propertiesAndAlternativeAxioms':True,'countsForThreeElements':counts,'cycleStages':stage_new,'wrongLoopCounterexample':True,'divisorCoversAndTaskChains':True,'workedProblems':46,'completeReviewRules':72,'figures':4}
(ROOT/'research/d_relations-finite-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
