"""Independent bounded enumeration plus source, preservation, and native-math audits."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,itertools,json,math,re,subprocess,tempfile,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='fd28529bf422d3cee6d1ae1ff828eba078fe8f3f';checks=[]
def check(label,test):
 assert test,label;checks.append(dict(name=label,passed=True))
C=math.comb
def binom(n,k):return C(n,k) if 0<=k<=n else 0
for n in range(0,11):
 triples=[(x,y,n-x-y) for x in range(n+1) for y in range(n-x+1)]
 check(f'positive residual shift {n}',len(triples)==C(n+2,2))
 check(f'bounded coordinate {n}',sum(x<=2 for x,y,z in triples)==(1 if n==0 else 3*n))
 even=[(x,y,2*n-x-y) for x in range(2*n+1) for y in range(2*n-x+1) if x%2==0]
 check(f'even coordinate {n}',len(even)==(n+1)**2)
 four=sum(1 for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1))
 check(f'four-type vectors {n}',four==C(n+3,3))
 check(f'marked subset identity {n}',sum(binom(n,k)*binom(k,3) for k in range(n+1))==binom(n,3)*2**max(0,n-3))
for n in range(1,9):
 words=list(itertools.product(range(4),repeat=n))
 check(f'even word filter {n}',sum(w.count(0)%2==0 for w in words)==(4**n+2**n)//2)
 check(f'three-bin surjections {n}',sum(len(set(w))==3 for w in itertools.product(range(3),repeat=n))==3**n-3*2**n+3)
 states=list(itertools.product([0,1],repeat=n));count=sum(all(not(w[i] and w[i+1]) for i in range(n-1)) for w in states)
 check(f'nonadjacent fixed-weight sum {n}',count==sum(binom(n-j+1,j) for j in range((n+1)//2+1)))
 perms=list(itertools.permutations(range(n)));der=sum(all(x!=i for i,x in enumerate(p)) for p in perms)
 exact=F(math.factorial(n))*sum((F((-1)**j,math.factorial(j)) for j in range(n+1)),F(0))
 check(f'derangement enumeration {n}',der==exact)
 for j in range(n+1):
  both=sum(w.count(2)==j for w in itertools.product([0,1,2],repeat=n))
  check(f'exact common membership {n},{j}',both==C(n,j)*2**(n-j))
for n in range(3,9):
 count=sum(sum(x<n for x in ss)>=3 for ss in itertools.combinations(range(2*n),5))
 check(f'red-majority swap {n}',count==C(2*n,5)//2)
check('authentic coupled totals',C(7,2)*16==336)
check('authentic eight-subset categories',sum(sum(x<5 for x in ss)>=4 for ss in itertools.combinations(range(10),8))==35)
check('authentic parity lower-bound cap',sum(a%2==0 and b<=4 and 40-a-b>=1 for a in range(41) for b in range(41-a))==96)
check('integrated parity cap',sum(a%2==0 and b<=3 and 18-a-b>=2 for a in range(19) for b in range(19-a))==32)
check('six-to-four surjection',sum(len(set(w))==4 for w in itertools.product(range(4),repeat=6))==1560)
check('restricted first onto fiber',sum(len(set(w))==3 and w.count(0)>=2 for w in itertools.product(range(3),repeat=5))==80)
check('integrated bounded positives',sum(sum(v)==12 for v in itertools.product(range(1,6),repeat=4))==85)
check('sorted required symbol',sum(2 in w for w in itertools.combinations_with_replacement([1,2,3],4))==10)
check('mixed parity subset',sum(any((a+b)%2 for a,b in itertools.combinations(s,2)) for s in itertools.combinations(range(1,11),4))==200)
check('integrated two category lower bounds',sum(3<=sum(x<5 for x in s)<=4 for s in itertools.combinations(range(10),6))==150)
check('equal toss convolution',sum(C(8,k)*C(5,k) for k in range(6))==1287)
check('coefficient impossible congruence',not any(3*j-14==14 for j in range(15)))
def matchings(xs):
 if not xs:yield ();return
 for j in range(1,len(xs)):
  for rest in matchings(xs[1:j]+xs[j+1:]):yield ((xs[0],xs[j]),)+rest
for n in range(6):
 allpairs=list(matchings(list(range(2*n))))
 check(f'pairing recurrence {n}',len(allpairs)==math.factorial(2*n)//(2**n*math.factorial(n)))
 check(f'pairing identity unique {n}',len(set(allpairs))==len(allpairs))
for n in range(1,5):
 # A person label 2i or 2i+1 belongs to couple i.
 count=sum(all(abs(p.index(2*i)-p.index(2*i+1))==1 for i in range(n)) for p in itertools.permutations(range(2*n)))
 check(f'adjacent couples direct {n}',count==2**n*math.factorial(n))
scenes=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes']
states=[f['snapshot']['tuple'] for f in scenes['counting-question-stars']['frames']]
check('all 21 exact stars-and-bars states',len(states)==21 and len(set(map(tuple,states)))==21 and all(sum(s)==5 for s in states))
for id in ['parity','onto','dp','pairing','report']:
 for i,f in enumerate(scenes['counting-question-'+id]['frames']):
  s=f['snapshot']
  if id=='parity':check(f'parity state {i}',s['prefix']==sum(s['counts'][:i+1]) and len(s['aValues'])==s['counts'][i])
  if id=='onto':check(f'onto state {i}',s['prefix']==sum(s['terms'][:i+1]) and sum(s['terms'])==1560)
  if id=='dp':check(f'dp state {i}',len(s['words'])==s['values'][min(i,5)] and (i<2 or s['values'][i]==s['values'][i-1]+s['values'][i-2]))
  if id=='pairing':check(f'pairing state {i}',sorted(sum(s['pairs'],[]))==list(range(1,9)))
  if id=='report':check(f'report state {i}',sum(w.count('1')==s['k'] for w in s['words'])==s['counts'][s['k']])
ns={};t=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in t.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
page=(R/'dist/chapters/s_counting.html').read_text();old=subprocess.check_output(['git','show',BASE+':dist/chapters/s_counting.html']).decode();qs=ns['questions'](page);oq=ns['questions'](old);rev=json.loads((E/'s_counting-revision.json').read_text())
check('preserve 77 placements',len(qs)==len(oq)==77)
for i,(row,(_,_,a,q),(_,_,oa,o)) in enumerate(zip(rev['records'],qs,oq),1):
 oldkey=int(oa['data-answer']) if oa.get('data-answer') else int(re.search(r'Correct option:\s*(\d+)',ns['plain'](o))[1])
 check(f'answer preserved {i}',row['answer']==int(a['data-answer'])==(4 if a.get('data-source-id')=='MS_CS_1405_Q129' else oldkey))
 check(f'complete mathematical response {i}',row['words']>=100 and '<math' in q[q.index('<details'):])
 if i<=15:check(f'authentic option order and content {i}',re.search(r'<div class="exam-options">[\s\S]*?</div></div></div>',q)[0]==re.search(r'<div class="exam-options">[\s\S]*?</div></div></div>',o)[0])
for m in re.findall(r'<math\b[\s\S]*?</math>',page):
 e=ET.fromstring(m)
 for c in e.iter():
  if c.tag.split('}')[-1] in ['msup','msub','msubsup']:check('script on intended base',list(c)[0].text not in [')',']','}'])
check('no abstract old answer template','Step 1 — model and conditions.' not in ''.join(q[3] for q in qs))
check('no unrelated repeated question aid','question-concept-aid' not in ''.join(q[3] for q in qs))
inv=json.loads((E/'inventory.json').read_text())
for c in inv['chapters']:
 if c['topicId']=='s_counting':continue
 p='dist/'+c['url'];check('other chapter preserved '+c['topicId'],subprocess.check_output(['git','show',BASE+':'+p]).replace(b'\r\n',b'\n')==(R/p).read_bytes().replace(b'\r\n',b'\n'))
act={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
for _,_,attrs,q in qs[:15]:
 item=act[attrs['data-source-id']];p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/item['repoPath'];check('authentic PDF hash '+item['id'],hashlib.sha256(p.read_bytes()).hexdigest()==item['sourceSha256'])
report=dict(topicId='s_counting',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='Finite enumerations have their explicit bounds above; mathematical proofs supply general statements. No universal performance or global course completeness is certified.')
(E/'s_counting-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'checks':len(checks),'status':report['status']})
