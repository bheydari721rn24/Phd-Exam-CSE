"""Independent enumeration and mathematics of the rewritten functions chapter."""
from pathlib import Path
import itertools,math,json,re,sys,subprocess,hashlib,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=0
def check(v):
 global checks
 assert v;checks+=1
def onto(m,n):return sum((-1)**j*math.comb(n,j)*(n-j)**m for j in range(n+1))
def partitions(n,k):
 if n==k==0:return 1
 if n==0 or k==0:return 0
 return partitions(n-1,k-1)+k*partitions(n-1,k)
enumerated=0
for m in range(6):
 for n in range(6):
  tuples=list(itertools.product(range(n),repeat=m));enumerated+=len(tuples);check(len(tuples)==n**m)
  injective=sum(len(set(v))==m for v in tuples);surjective=sum(set(v)==set(range(n))for v in tuples)
  check(injective==(math.factorial(n)//math.factorial(n-m)if m<=n else 0));check(surjective==onto(m,n))
  for k in range(min(m,n)+1):check(sum(len(set(v))==k for v in tuples)==math.comb(n,k)*math.factorial(k)*partitions(m,k))
  for v in tuples:
   fibers=[[i for i,x in enumerate(v)if x==j]for j in range(n)]
   if m<=3 and n<=3:
    powers=[set(i for i in range(m)if mask>>i&1)for mask in range(2**m)];targets=[set(i for i in range(n)if mask>>i&1)for mask in range(2**n)]
    image=lambda S:{v[i]for i in S};pre=lambda T:{i for i,x in enumerate(v)if x in T}
    for X in powers:
     check(X<=pre(image(X)));check(pre(image(pre(image(X))))==pre(image(X)))
     for Y in powers:check(image(X|Y)==image(X)|image(Y));check(image(X&Y)<=image(X)&image(Y));check(image(X)-image(Y)<=image(X-Y))
    for T in targets:
     check(image(pre(T))==T&set(v))
     for U in targets:check(pre(T|U)==pre(T)|pre(U));check(pre(T&U)==pre(T)&pre(U));check(pre(T-U)==pre(T)-pre(U))
    for g in itertools.product(range(m),repeat=n):
     left=all(g[v[i]]==i for i in range(m));right=all(v[g[j]]==j for j in range(n))
     if left:check(len(set(v))==m and set(g)==set(range(m)))
     if right:check(set(v)==set(range(n))and len(set(g))==n)
  if m==n and m>0:check(sum(all(v[v[i]]==v[i]for i in range(m))for v in tuples)==sum(math.comb(m,k)*k**(m-k)for k in range(1,m+1)))

# Enumerate actual output tuples instead of reproducing stars-and-bars constructions.
for m,n,expected,ends in[(5,5,126,False),(6,4,35,True),(5,3,21,False),(8,3,45,False),(8,5,210,True)]:
 count=0;by_image={}
 for v in itertools.product(range(1,n+1),repeat=m):
  if all(v[i]<=v[i+1]for i in range(m-1))and(not ends or(v[0]==1 and v[-1]==n)):
   count+=1;by_image[len(set(v))]=by_image.get(len(set(v)),0)+1
 check(count==expected)
 if m==8 and n==5:check(by_image=={2:7,3:63,4:105,5:35})
for n in[5,8]:
 allperm=list(itertools.permutations(range(n)));fixed_two=0;two_pairs=0;one_cycle=0;involutions=0;two_fixed=0
 for v in allperm:
  fixed=[i for i in range(n)if v[i]==i];square=all(v[v[i]]==i for i in range(n));fixed_two+=int(v[0]==0 and v[1]==1)
  if square:
   involutions+=1;two_pairs+=int(len(fixed)==n-4);two_fixed+=int(len(fixed)==2)
  seen=set();x=0
  while x not in seen:seen.add(x);x=v[x]
  one_cycle+=int(len(seen)==n)
 check(fixed_two==math.factorial(n-2));check(two_pairs==3*math.comb(n,4));check(one_cycle==math.factorial(n-1))
 if n==8:check(involutions==764 and two_fixed==420)
 for m in[3]:check(sum(len(set(v))==m for v in itertools.product(range(n+3),repeat=m))==(n+3)*(n+2)*(n+1))
 check(sum(all(v[v[i]]==v[i]for i in range(n))and set(v)=={0,1}for v in itertools.product([0,1],repeat=n))==2**(n-2))
 check(sum(all((g[j]//n)==j for j in range(3))for g in itertools.product(range(3*n),repeat=3))==n**3)
check(onto(6,4)==1560);check(onto(5,3)*4==600)
check(sum(v.count(0)==3 for v in itertools.product(range(3),repeat=7))==560)
check(sum(set(v)=={0,1,2}and max(v.count(j)for j in range(3))<=3 for v in itertools.product(range(3),repeat=6))==450)
for n,expected in[(3,12),(4,48)]:check(sum(all(g[f[i]]==i for i in range(2))for f in itertools.product(range(n),repeat=2)for g in itertools.product(range(2),repeat=n))==expected)
g=[0,1,1,2,2,2];check(sum(len({g[x]for x in v})==3 for v in itertools.product(range(6),repeat=3))==36);check(sum(len({g[x]for x in v})==3 for v in itertools.product(range(6),repeat=4))==432)
affine=[]
for a in range(6):
 for b in range(6):
  well_defined=all((a*x+b)%6==(a*(x+4*t)+b)%6 for x in range(4)for t in range(-8,9));check(well_defined==((4*a)%6==0))
  if well_defined:affine.append(tuple((a*x+b)%6 for x in range(4)))
check(len(set(affine))==12)
def power(v,k):
 out=list(range(len(v)))
 for _ in range(k):out=[v[x]for x in out]
 return out
v=[1,2,2,4,3,4,5];check(power(v,2)==[2,2,2,3,4,3,4])
for k in range(1,13):w=power(v,k);check(all(w[w[i]]==w[i]for i in range(7))==(k>=2 and k%2==0))
v=[1,2,0,4,5,6,3];check(power(v,12)==list(range(7)));check(sum(i==x for i,x in enumerate(power(v,6)))==3)
data=json.loads((R/'dist/chapters/concept-animations.json').read_text());models={k:v for k,v in data['scenes'].items()if k.startswith('functions-question-')};check(len(models)==39)
for model in models.values():
 for f in model['frames']:
  s=f['snapshot']
  if s['kind']in['map','endofunction','subsets']:check(len(s['values'])==len(s['source']));check(all(0<=x<len(s['target'])for x in s['values']))
  if s['kind']=='sequence':check(all(a<=b for a,b in zip(s['values'],s['values'][1:])));check(sum(s['counts'])==len(s['values']))
  if s['kind']=='sections':check(all(s['selected'][j]in s['fibers'][j]for j in range(3)))
  if s['kind']=='composition':check(all(0<=x<len(s['middle'])for x in s['inner']));check(all(0<=x<len(s['target'])for x in s['outer']))
page=(R/'dist/chapters/d_functions.html').read_text(encoding='utf-8');sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
for src in[page]+[model['descriptionHtml']for model in models.values()]+[markup for model in models.values()for f in model['frames']for markup in[f['formulaHtml'],f.get('captionMathHtml',''),f['teaching'].get('operationHtml',''),f['teaching'].get('whyHtml','')]]:
 for native in re.findall(r'<math\b[\s\S]*?</math>',src):
  root=ET.fromstring(native);check(not closing_script_bases(root));check(not delimiter_issues(root));check(chr(92)not in ''.join(root.itertext()))
for model in models.values():
 for f in model['frames']:check('join(str('not in f['caption']);check('sorted(set('not in f['caption']);check('\ue000'not in f.get('captionMathHtml',''))
from read_functions_bank import ns,rows
entries=ns['questions'](page);check(len(entries)==47)
for i,(_,_,attrs,q)in enumerate(entries):check(q.count('class="exam-option"')==4);check(int(re.search(r'Correct option:\s*(\d+)',ns['plain'](q))[1])==rows[i]['answer']);check('$'not in q);check('separate teaching example'not in q)
base=subprocess.check_output(['git','show','162799857108eb67965f6d2a54526a9da82bb3e7:dist/chapters/d_functions.html']).decode();titles=lambda s:re.findall(r'<h3[^>]*>Tutorial [\s\S]*?</h3>',s);check(len(titles(page))==42);check(titles(page)==titles(base));check('student-approved'not in page.lower())
check(json.loads((E/'d_functions-course-recheck.json').read_text())['universityCountActuallyReadInThisRevision']>=4)
for row in rows[:5]:check(hashlib.sha256((Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/row['canonical']['repoPath']).read_bytes()).hexdigest()==row['canonical']['sourceSha256'])
report=dict(status='passed_with_recorded_finite_bounds',topicId='d_functions',checkCount=checks,smallMapsEnumerated=enumerated,models=len(models),uniqueModelFrames=sum(len(v['frames'])for v in models.values()),pageSha256=hashlib.sha256(page.encode()).hexdigest(),scope='All total maps for sizes 0 through 5; selected exact monotone tuples through 8 inputs, all permutations through 8 points, actual inverse pairs, affine quotient representatives, weighted composites, native formulas and original source hashes.',limits='Finite enumerations cross-check the stated general proofs; neither implies literal perfection or unseen examination performance.')
(E/'d_functions-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(report)
