from pathlib import Path
import itertools,json,hashlib,math,re,xml.etree.ElementTree as ET
from a_sort_engine import trace
B=Path(__file__).parent;R=B.parent
checks=0
def check(condition,context):
 global checks
 assert condition,context;checks+=1
for n in range(7):
 for a in itertools.permutations(range(n)):
  I=sum(a[i]>a[j] for i in range(n) for j in range(i+1,n));r=sum(a[i]<min(a[:i]) for i in range(1,n))
  for kind in ['insertion','selection','bubble','merge','quick','three','cmu','heap','hoare']:
   z=trace(kind,dict(values=list(a)),False)['result'];check(z['keys']==list(range(n)),(kind,a,z))
   if kind=='insertion':check((z['shifts'],z['comparisons'],z['writes'])==(I,I+max(0,n-1)-r,I+max(0,n-1)),(kind,a,z,I,r))
   if kind=='selection':check(z['comparisons']==n*(n-1)//2 and z['swaps']<=max(0,n-1),(kind,a,z))
   if kind=='bubble':check(z['swaps']==I,(kind,a,z,I))
  if n:
   z=trace('merge',dict(values=list(a)),False)['result'];h=math.ceil(math.log2(n));check(z['comparisons']<=n*h-2**h+1,(a,z))
for n in range(6):
 for a in itertools.product(range(3),repeat=n):
  expected=sorted(zip(a,[chr(97+i) for i in range(n)]),key=lambda t:t[0])
  for kind in ['insertion','bubble','merge','counting','radix','bucket']:
   p=dict(values=list(a),base=3,buckets=3);z=trace(kind,p,False)['result'];check(list(zip(z['keys'],z['ids']))==expected,(kind,a,z))
  for kind in ['quick','three','cmu','heap','hoare']:check(trace(kind,dict(values=list(a)),False)['result']['keys']==sorted(a),(kind,a))
for n in range(1,17):
 a=list(range(n));check(trace('merge',dict(values=a,skip=True),False)['result']['comparisons']==n-1,('skip',n))
 if n>1:check(trace('quick',dict(values=[1]*n),False)['result']['comparisons']==n*(n-1)//2,('quick-equal',n));check(trace('three',dict(values=[1]*n),False)['result']['comparisons']==n-1,('three-equal',n))
 check(trace('heap',dict(values=a),False)['result']['buildComparisons']<2*n,('floyd-bound',n))
for Bv in range(2,11):
 for a in [[-999,-1,0,999,-999],[0],[1,2,1],[Bv**3-1,0,Bv**3]]:
  z=trace('radix',dict(values=a,base=Bv),False)['result'];check(z['keys']==sorted(a),('radix',Bv,a));M=max(a)-min(a);d=1
  while M>=Bv:M//=Bv;d+=1
  check(len(z['passes'])==d,('digits',Bv,a,z))
z=trace('merge',dict(values=[12,7,5,9,3,8,2,6]),False)['result'];check(z['comparisons']==16,('authentic',z))
auth=json.loads((B/'a_sort-authentic.json').read_text());check(auth[0]['answer']==1 and auth[0]['options']==['16','14','12','10'],auth[0])
check(trace('cmu',dict(values=[1,3,5,7,6,4,2]),False)['result']['comparisons']==21,'CMU worst')
models=json.loads((R/'dist/chapters/a_sort-models.json').read_text())['models'];frames=0
for m in models:
 if m['kind']=='decision':continue
 check(m['result']==trace(m['kind'],m['params'],False)['result'],m['id'])
 for f in m['frames']:
  ET.fromstring(f['svg']);ET.fromstring(f['formulaHtml']);frames+=1
  # Original records are conserved across live storage, excluding immutable reference/copies.
  if m['kind']=='insertion':
   ids=[r['id'] for row in f['rows'] for r in row['cells'] if r];check(len(ids)==len(set(ids))==len(m['initial']),(m['id'],f['caption'],ids))
html=(R/'dist/chapters/a_sort.html').read_text();check(html.count('class="exam-question"')==88 and html.count('class="review-rule"')==80,'chapter counts')
check('$' not in html and '<!--' not in html,'unrendered marker')
for formula in re.findall(r'<math\b.*?</math>',html,re.S):ET.fromstring(formula)
baseline=json.loads((B/'a_sort-retention-baseline.json').read_text());correction=json.loads((B/'a_sort-provenance-correction.json').read_text())
cor={x['file']:x for x in correction}
prior_question_count=0
for name,old in baseline.items():
 p=R/'dist/chapters'/name;actual=hashlib.sha256(p.read_bytes()).hexdigest();expected=cor[name]['afterSha256'] if name in cor else old
 check(actual==expected,('retention',name,actual,expected));prior_question_count+=p.read_text(encoding='utf-8').count('class="exam-question"')
check(prior_question_count==2169,('prior questions',prior_question_count))
fixtures=[]
for kind in ['insertion','selection','bubble','merge','quick','three','heap','counting','radix','bucket']:
 for vals in [[4,1,3,1,2],[5,4,3,2,1],[2,2,2,2],[1],[3,1,2,3,0,1]]:
  p=dict(values=vals,base=5,buckets=5);fixtures.append(dict(kind=kind,params=p,expected=trace(kind,p,False)['result']))
for vals in [[-3,2,-1,2,-3],[-9,0,7,-9]]:
 for kind in ['counting','radix']:fixtures.append(dict(kind=kind,params=dict(values=vals,base=3),expected=trace(kind,dict(values=vals,base=3),False)['result']))
(B/'a_sort-lab-fixtures.json').write_text(json.dumps(fixtures,indent=2)+'\n')
report=dict(state='passed',checks=checks,modelCount=len(models),parsedFrames=frames,questions=88,rules=80,fixtures=len(fixtures),priorChapters=len(baseline),priorQuestions=prior_question_count,documentedOptionCorrections=list(cor),scope='Finite exhaustive permutations through length 6; ternary multisets through length 5; exact authentic count and algorithm-specific identities. This is not a proof of all possible executions.')
(B/'a_sort-mathematical-audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
