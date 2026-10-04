"""Independent finite reference checks; never execute undefined C examples."""
import json,re,hashlib,subprocess,math,itertools
from pathlib import Path
import sympy as S
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent;checks=[]
def check(name,b):
 assert b,name
 checks.append(name)
Q=json.loads((BASE/'p_functions-questions.json').read_text())
check('89 distinct original/course problem ids',len(Q)==89 and len({q['id'] for q in Q})==89)
check('Distinct titles',len({q['title'] for q in Q})==89)
for q in Q:
 check(q['id']+' complete explanation',len(q['solution'].split())>=45)
 c=q['certificate'];kind=c['kind'];d=c['data']
 if kind=='python':
  ns={};exec(compile(d['code'],q['id'],'exec'),ns)
  check(q['id']+' actual Python execution',ns['answer']==d['answer'])
 if kind=='affine':
  a,b,c,e,x,y=d
  check(q['id']+' independently composed affine result',c*(a*x+b)+e==y)
 if kind=='range':check(q['id']+' solution interval',[x for x in range(-30,31) if 17<=3*(2*x+1)-4<=41]==list(range(d[0],d[1]+1)))
 if kind=='iterate':
  a,b,x,k,expected=d
  result=x
  for _ in range(k):result=a*result+b
  check(q['id']+' iterative and closed form',result==expected==a**k*x+b*sum(a**j for j in range(k)))
 if kind=='halves':
  x,out=d;result=[]
  while x:x//=2;result.append(x)
  check(q['id']+' exact half sequence',result==out)
 if kind=='odd-sum':check(q['id']+' odd summation',sum(2*k+1 for k in range(d))==d*d)
 if kind=='triangular':
  check(q['id']+' triangular induction instance',sum(range(d+1))==d*(d+1)//2)
 if kind=='geometric':check(q['id']+' geometric series',sum(2**k for k in range(d))==2**d-1)
 if kind=='qr':
  n,v,qv,r=d;check(q['id']+' exact division identity',divmod(n,v)==(qv,r) and n==qv*v+r and 0<=r<v)
 if kind=='signed-qr':
  n,v,qv,r=d;check(q['id']+' signed truncation model',math.trunc(n/v)==qv and n==qv*v+r and r<0)
 if kind=='safe-affine':
  lo,hi,x0,x1=d
  check(q['id']+' safe endpoints',all(lo<=2*x<=hi and lo<=2*x+1<=hi for x in [x0,x1]))
  check(q['id']+' immediate unsafe neighbors',2*(x0-1)<lo and 2*(x1+1)+1>hi)
 if kind=='safe-composite':
  lo,hi=-2**31,2**31-1;x0,x1=d
  check(q['id']+' safe composition endpoints',all(lo<=x+3<=hi and lo<=2*(x+3)<=hi for x in [x0,x1]))
  check(q['id']+' unsafe outer neighbors',2*(x0-1+3)<lo and 2*(x1+1+3)>hi)
 if kind=='alias-affine':
  u,v,alias,expected=d
  objects=[u] if alias else [u,v];p=0;qidx=0 if alias else 1
  objects[p]+=2;objects[qidx]*=3
  check(q['id']+' independent object-identity model',[objects[p],objects[qidx]]==expected)
 if kind=='static':
  state,inc,expected=d;actual=[]
  for x in inc:state+=x;actual.append(state)
  check(q['id']+' persistent state',actual==expected)
 if kind=='orders':
  results=[]
  for order in [(0,1),(1,0)]:
   vals=[0,0];counter=0
   for i in order:counter+=1;vals[i]=counter
   results.append(vals[0]-vals[1])
  check(q['id']+' permitted orders',sorted(results)==d[0] and counter==d[1])
 if kind=='tetrahedral':check(q['id']+' returned counter sum',sum(sum(range(k+1)) for k in range(1,d+1))==d*(d+1)*(d+2)//6)

# Domain and mathematical relations checked symbolically, not by repeating
# the author construction functions.
x=S.symbols('x')
check('Composition domain excludes both denominator roots',S.solve(x-2,x)==[2] and S.solve(1/(x-2)+1,x)==[1])
for n in range(101):
 total=0
 for k in range(1,n+1):
  check(f'triangular {n},{k} guard invariant',total==(k-1)*k//2)
  total+=k
 check(f'triangular {n} final safe result',total==n*(n+1)//2 and total<=5050)
for n in range(1,80):
 expected=[n-1-2*t for t in range((n+1)//2)]
 def store(a,i,b):
  if a<0:return
  b[i]=a;store(a-2,i+1,b)
 out=[None]*((n+1)//2);store(n-1,0,out)
 check(f'authentic reverse stride {n}',out==expected)

data=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'];new={k:v for k,v in data.items() if k.startswith('fn-')}
check('12 concept models',len(new)==12)
expected_values={
 'fn-copy':[4,4,14,14],'fn-pointer':['&a','&a','*p = 11','void return'],
 'fn-alias':[4,6,18],'fn-nested':[2,7,7,22,29],
 'fn-static':[v for k in range(1,4) for v in [k,10+k,10+k]],
 'fn-lookup':['lookup x',10,13],'fn-orders':[0,1,-1,0,1,1],
 'fn-closure':['function','function',7,7],'fn-default':['[]','[2]','[2,5]','two snapshots'],'fn-output':[0,4,3,3]}
for id,scene in new.items():
 for i,f in enumerate(scene['frames']):
  snap=f['snapshot']
  if id in expected_values:
   check(id+f' checkpoint {i} exact value',snap['value']==expected_values[id][i])
   token=next(n for n in f['nodes'] if n['id']=='value')
   check(id+f' checkpoint {i} numeric visual matches',token['label']==str(snap['value']) and token['x']==snap['x'])
  if id=='fn-recursion':
   d=snap['depth'];expected=3-d if snap['kind']=='descent' else (3-d)*(4-d)//2
   check(id+f' checkpoint {i} frame count',len(f['nodes'])==d+2)
   check(id+f' checkpoint {i} recursive value',snap['value']==expected)
   check(id+f' checkpoint {i} moving stack token',f['nodes'][-1]['y']==65+70*d)
  if id=='fn-sharing':
   old,newobj=[('[2]','Not created'),('[2,7]','Not created'),('[2,7]','[99]'),('[2,7]','[99]')][i]
   check(id+f' checkpoint {i} separate objects',snap['old']==old and snap['new']==newobj)
  check(id+f' checkpoint {i} readable caption',len(f['caption'].split())>=14)
check('Copy model has actual position transfer',new['fn-copy']['frames'][0]['nodes'][-1]['x']!=new['fn-copy']['frames'][1]['nodes'][-1]['x'])

auth=json.loads((BASE/'p_functions-authentic.json').read_text())
for q in auth:
 p=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q['repoPath']
 check(q['id']+' original PDF hash',hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSHA'])
 check(q['id']+' pinned archive and explicit revisit',q['sourceCommit']=='bdadf6e2c9cadc4772ae137a96a3da753c7cfd08' and 'revisit' in q['provenance'].lower())
check('MSc correct stride option',auth[0]['answer']==1 and 'decrease source n by two' in auth[0]['options'][0])
check('PhD descending block order option',auth[1]['answer']==4 and auth[1]['options'][3]=='Descending.')
approved=json.loads((BASE/'library-approval.json').read_text())['approvedTopics']
check('27 approved chapters',len(approved)==27)
opening='a53e3941a114564855623adf021d5abafd5408e3'
total=0
for id in approved:
 live=(ROOT/f'dist/chapters/{id}.html').read_text(encoding='utf-8')
 before=subprocess.check_output(['git','show',opening+':dist/chapters/'+id+'.html'],cwd=ROOT).decode('utf-8')
 extract=lambda s:re.findall(r'<section class="exam-question"[\s\S]*?</section>',s)
 check(id+' approved solved question content preserved',extract(live)==extract(before))
 total+=len(extract(live))
check('1407 approved entries preserved',total==1407)
page=(ROOT/'dist/chapters/p_functions.html').read_text()
check('91 solved questions, 80 rules, 7 figures',page.count('class="exam-question"')==91 and page.count('class="review-rule"')==80 and page.count('<figure')==7)
check('English chapter with no raw TeX delimiters',not re.search('[\u0600-\u06ff]',page) and '$' not in page)
check('Four primary plus two supplemental universities',len({c['university'] for c in json.loads((BASE/'p_functions-reviewed-courses.json').read_text())})==6)
result=dict(state='passed',checks=len(checks),questionCount=91,ruleCount=80,modelCount=len(new),checkpoints=sum(len(s['frames']) for s in new.values()),approvedQuestionsPreserved=total,pythonExecutions=sum(q['certificate']['kind']=='python' for q in Q),limitations='Finite independent exact-state and executable Python checks plus written language-rule reasoning. No local C/C++ compiler; no compiled or universal performance certification.',details=checks)
(BASE/'p_functions-validation.json').write_text(json.dumps(result,indent=2)+'\n')
pub=ROOT/'dist/evidence/p_functions';pub.mkdir(exist_ok=True);(pub/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items() if k!='details'})
