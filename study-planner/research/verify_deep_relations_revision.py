from pathlib import Path
from itertools import product,combinations,permutations
from functools import lru_cache
import math,json,re,sys,subprocess,hashlib,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';count=0
def check(v):
 global count
 assert v;count+=1
# Reuse the retained independent set/path checks, excluding obsolete UI assertions.
old=(B/'verify_d_relations_en.py').read_text();env={'__file__':str(B/'verify_d_relations_en.py')};exec(old[:old.index('page=(ROOT/')],env)
for n in range(4):
 coords=list(product(range(n),repeat=2));stats=dict(refsym=0,strictsym=0,anti=0,diagonly=0,symserial=0)
 for bits in range(1<<(n*n)):
  pairs={p for i,p in enumerate(coords)if bits>>i&1};ref=all((i,i)in pairs for i in range(n));sym=all((j,i)in pairs for i,j in pairs);anti=all(i==j or(j,i)not in pairs for i,j in pairs);irref=all((i,i)not in pairs for i in range(n));serial=all(any(a==i for a,b in pairs)for i in range(n))
  stats['refsym']+=ref and sym;stats['strictsym']+=sym and irref;stats['anti']+=anti;stats['diagonly']+=sym and anti;stats['symserial']+=sym and serial
 check(stats['refsym']==2**(n*(n-1)//2));check(stats['strictsym']==2**(n*(n-1)//2));check(stats['anti']==2**n*3**(n*(n-1)//2));check(stats['diagonly']==2**n);check(stats['symserial']==sum((-1)**j*math.comb(n,j)*2**((n-j)*(n-j+1)//2)for j in range(n+1)))
 if n==3:check(stats['symserial']==45)
# Enumerate labelled partitions directly to check the profile and equivalence counts.
def partitions(items):
 if not items:yield[];return
 x,*rest=items
 for p in partitions(rest):
  yield [[x]]+[b[:]for b in p]
  for i in range(len(p)):
   q=[b[:]for b in p];q[i].append(x);yield q
for n in range(1,7):
 ps=list(partitions(list(range(n))))
 for p in ps:check(sum(len(b)**2 for b in p)-n==2*sum(math.comb(len(b),2)for b in p))
 if n==6:check(sum(sorted(map(len,p))==[1,1,2,2]for p in ps)==45)
check(sum(sorted(map(len,p))==[3,4]for p in partitions(list(range(7))))==35)
check(sum(sorted(map(len,p))==[4,4]for p in partitions(list(range(8))))==35)
# Independent ideal subset recursion, different from the authored row-length DP.
values=[d for d in range(1,73)if 72%d==0];pred=[sum(1<<i for i,x in enumerate(values)if x!=y and y%x==0)for y in values];full=(1<<len(values))-1
@lru_cache(None)
def ways(mask):
 if mask==full:return 1
 return sum(ways(mask|(1<<i))for i in range(len(values))if not(mask>>i&1)and pred[i]&mask==pred[i])
check(len(values)==12);check(ways(0)==462)
cov={(a,b)for a,b in product(values,repeat=2)if a!=b and b%a==0 and not any(c not in[a,b]and c%a==0 and b%c==0 for c in values)}
check(len(cov)==17);check(sum(b%a==0 for a,b in product(values,repeat=2))==60)
check(all(b%a==0 for a,b in zip([1,2,4,8,24,72],[2,4,8,24,72])))
check(sum(all(v%u==0 for u,v in zip(p,p[1:]))for p in permutations(values,6)if p[0]==1 and p[-1]==72)==10)
models=json.loads((E/'d_relations-models.json').read_text());check(len(models)==40)
for model in models.values():
 for frame in model['frames']:
  s=frame['snapshot'];kind=s['kind']
  if kind=='matrices':
   for m in s['matrices']:check(len(m['values'])==len(m['rowLabels']));check(all(len(r)==len(m['colLabels'])for r in m['values']));check(all(len(r)==len(m['colLabels'])for r in m['html']))
   if 'chain-closure-'in model['id']and s['stage']==len(s['matrices'][0]['values']):
    M=s['matrices'][0]['values'];check(all(v==int(i<j)for i,row in enumerate(M)for j,v in enumerate(row)))
   if 'reflexive-symmetric-'in model['id']or'irreflexive-symmetric-'in model['id']:
    M=s['matrices'][0]['values'];check(all(M[i][j]==M[j][i]for i in range(len(M))for j in range(len(M))));check(all(M[i][i]==int('irreflexive'not in model['id'])for i in range(len(M))))
  if kind=='hasse':
   labs=s['labels'];expected={(i,j)for i,a in enumerate(labs)for j,b in enumerate(labs)if a!=b and b%a==0 and not any(c not in[a,b]and c%a==0 and b%c==0 for c in labs)};check(set(map(tuple,s['covers']))<=expected)
   if s['stage']==2:check(set(map(tuple,s['covers']))==expected)
   for a,b in s['covers']:check(s['positions'][b][1]<s['positions'][a][1])
   if 'height'in model['id']:check(all((a,b)in expected for a,b in zip(s['highlight'],s['highlight'][1:])))
  if kind=='table':check(all(len(r)==len(s['headings'])for r in s['rows']));check(all(len(r)==len(s['headings'])for r in s['rowsHtml']))
  if kind=='refinement':check(s['mapping']==[0,0,1])
  if kind=='lex'and s['stage']:
   a,b=s['before'];m,n=s['after'];check(m>=0 and n>=0);check((m==a-1 and a>0 and n==b*b+1)or(m==a and b>=2 and n==b-2))
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/d_relations.html').read_text()
for source in [page]+[f['formulaHtml']for m in models.values()for f in m['frames']]+[v for m in models.values()for f in m['frames']for mat in f['snapshot'].get('matrices',[])for row in mat['html']for v in row]:
 for native in re.findall(r'<math\b[\s\S]*?</math>',source):
  root=ET.fromstring(native);check(not closing_script_bases(root));check(not delimiter_issues(root));check(not re.search(r'\\[A-Za-z]',''.join(root.itertext())));check(chr(92) not in ''.join(root.itertext()))
from read_relations_bank import ns,rows
sections=ns['questions'](page);check(len(sections)==45)
for i,(_,_,attrs,q)in enumerate(sections):check(q.count('class="exam-option"')==4);check(int(re.search(r'Correct option:\s*(\d+)',ns['plain'](q))[1])==rows[i]['answer']);check('$'not in q);check('separate teaching example'not in q)
base=subprocess.check_output(['git','show','9628d13bd1f5417e4144c95b1be84e18782294bc:dist/chapters/d_relations.html']).decode();titles=lambda s:re.findall(r'<h3[^>]*>Tutorial [\s\S]*?</h3>',s);check(len(titles(page))==46);check(titles(page)==titles(base));check('student-approved'not in page.lower())
check(json.loads((E/'d_relations-course-recheck.json').read_text())['universityCountActuallyReadInThisRevision']==4)
for r in rows[:3]:check(hashlib.sha256((Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/r['canonical']['repoPath']).read_bytes()).hexdigest()==r['canonical']['sourceSha256'])
report=dict(topicId='d_relations',status='passed_with_recorded_finite_bounds',checkCount=count,retainedFiniteRelationsChecked=531,laboratoryAllFourVertexRelations=65536,models=40,uniqueModelFrames=sum(len(m['frames'])for m in models.values()),independentIdealSubsetsVisited=ways.cache_info().currsize,linearExtensions=ways(0),pageSha256=hashlib.sha256(page.encode()).hexdigest(),scope='Retained all relations on carriers of sizes 0–3; independent labelled partition enumeration through size eight for selected profiles; independent twelve-divisor ideal subset DP; all saved matrix/cover states; every lexicographic branch call; all native formulas; authentic original file hashes.',limits='Finite declared objects and stated general proofs; not universal correctness or examination performance. Actual browser rendering and controls are a separate gate.')
(E/'d_relations-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(report)
