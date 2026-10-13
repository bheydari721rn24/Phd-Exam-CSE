"""Independent recurrence iteration, exact fractions, rounding and document checks."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import ast,hashlib,json,math,re,subprocess,sys,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=0
def check(v,label=''):
 global checks
 assert v,label;checks+=1
# Independent loops start from the recurrence, not the authored closed-form generator.
families=[(2,lambda n:3,0,lambda n:3*(2**n-1)),(2,lambda n:2**n,1,lambda n:(n+1)*2**n),(4,lambda n:2**n,1,lambda n:2*4**n-2**n),(1,lambda n:2**n,1,lambda n:2**(n+1)-1),(1,lambda n:n*n,1,lambda n:1+n*(n+1)*(2*n+1)//6),(1,lambda n:n*n,0,lambda n:n*(n+1)*(2*n+1)//6),(2,lambda n:n,0,lambda n:2**(n+1)-n-2),(2,lambda n:1,0,lambda n:2**n-1),(2,lambda n:2**n,1,lambda n:(n+1)*2**n)]
for a,toll,seed,closed in families:
 value=seed;check(value==closed(0))
 for n in range(1,81):value=a*value+toll(n);check(value==closed(n),(a,n))
# The exact sums are separately counted through level nodes.
for a in range(1,7):
 for b in range(2,7):
  for q in range(5):
   for h in range(9):
    for c in [1,3,20]:
     u=c
     for k in range(1,h+1):u=a*u+(b**k)**q
     tree=a**h*c+sum(a**j*(b**(h-j))**q for j in range(h));check(u==tree)
prefix=[1];triple=[1]
for n in range(1,31):
 prefix.append(sum(prefix));triple.append(3*sum(triple));check(prefix[n]==2**(n-1));check(triple[n]==3*4**(n-1))
v=[1,6]
for n in range(2,41):v.append(4*v[-1]-4*v[-2]);check(v[n]==(1+2*n)*2**n)
u=1
for n in range(1,41):u*=2**n;check(u==2**(n*(n+1)//2))
u=1
for n in range(1,31):u=n*u+math.factorial(n);check(u==(n+1)*math.factorial(n))
p=[1,1]
for n in range(18,114):p.append((p[-1]+p[-2])%2)
check([n for n in range(100,114)if p[n-16]==0]==[102,105,108,111])
F=[0,1];calls=[1,1]
for n in range(2,40):F.append(F[-1]+F[-2]);calls.append(calls[-1]+calls[-2]+1);check(calls[n]==2*(F[n]+F[n-1])-1)
# Every rounded merge input in a non-power-of-two range is compared to its actual children.
A=[0,0];C=[0,0]
for n in range(2,2001):
 A.append(A[n//2]+A[(n+1)//2]+n);C.append(C[n//2]+C[(n+1)//2]+n-1);L=n.bit_length()-1;H=(n-1).bit_length();check(A[n]==n*L+2*n-2**(L+1));check(C[n]==n*H-2**H+1);check(A[n]-C[n]==n-1)
# Potential inequalities and full integer paths, including square boundaries.
steps=[0,0]
for n in range(2,10001):
 d=math.isqrt(n)+(math.isqrt(n)**2!=n);child=n-d;check(0<=child<n);drop=d/(math.sqrt(n)+math.sqrt(child));check(.5-1e-12<=drop<2);steps.append(steps[child]+1);check((math.sqrt(n)-1)/2<steps[n]<=2*math.sqrt(n))
check(steps[100]==16)
# Square-root integer paths are checked against exact transformed error bounds.
for n in range(4,4001):
 x=n;m=math.log2(n);j=0
 while x>=4:
  check(m/(2**j)-2<=math.log2(x)+1e-12<=m/(2**j)+1e-12);x=math.isqrt(x);j+=1
# Conditional expected sizes use actual uniform rank lists.
for n in range(2,501):
 sizes=[max(r,n-1-r)for r in range(n)];mean=Fraction(sum(sizes),n);check(mean<=Fraction(3*n,4))
 if n%2==0:check(mean==Fraction(3*n-2,4))
 else:m=n//2;check(mean==Fraction(3*m*m+2*m,2*m+1))
check(Fraction(sum(j*j for j in [3,2,2,3]),4)==Fraction(13,2))
check(Fraction(sum([3,2,2,3]),4)**2==Fraction(25,4))
# Transfer examples use exact algebraic arithmetic.
check(9*5**5-8*4**5==19933);check((10*4+1)*3**4==3321)
check(16*(Fraction(1,2)+sum((Fraction(1,r)for r in range(2,5)),Fraction()))==Fraction(76,3))
check(16*(Fraction(1,2)+sum((Fraction(1,r*r)for r in range(2,5)),Fraction()))==Fraction(133,9))
v=1;seq=[v]
for h in range(1,6):v=2*v+(2**h)**(2 if h%2 else 3);seq.append(v)
check(seq==[1,6,76,216,4528,10080]);check(A[13]==49 and C[13]==37)
check(1+5*6//2==16 and 3*2**5-5-2==89)
# Every new model carries exact snapshots, and frame equations must parse with balanced fences.
models={k:s for k,s in json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'].items()if k.startswith('algorithm-recurrence-question-')};check(len(models)==46)
for id,s in models.items():
 for f in s['frames']:
  ET.fromstring(f['formulaHtml']);d=f['snapshot'];kind=d['kind']
  if kind=='table':check(all(len(r)==len(d['headings'])for r in d['rows'])and len(d['rowsHtml'])<=7)
  if kind=='level-work':
   running=0
   for j,nodes,size,local,aggregate,total in d['rows']:
    check(nodes==d['a']**j and size*d['b']**j==d['N']);check(nodes*local==aggregate);running+=aggregate;check(total==running)
  if kind=='unequal':check(sum((Fraction(n)**(2 if d['quadratic']else 1)for n in d['frontier']),Fraction())==Fraction(d['total']))
  if kind=='chain':
   check(d['total']==sum(d['tolls'][:d['index']+1]));check(len(d['values'])==len(d['tolls']))
   if id.endswith('-slow'):check(all(a-math.isqrt(a)-(math.isqrt(a)**2!=a)==b for a,b in zip(d['values'],d['values'][1:])))
  if kind=='merge-tree':
   ns=d['nodes'];check(len(ns)==25 and sum(n['cost']for n in ns)==37);check(sum(n['size']if n['size']>1 else 0 for n in ns)==49)
   for n in ns:
    kids=[v for v in ns if v['parent']==n['id']];check(not kids if n['size']==1 else sorted(v['size']for v in kids)==[n['size']//2,(n['size']+1)//2])
  if kind=='expectation':check(d['sizes']==[max(r,3-r)for r in d['ranks']])
 audit=s.get('audit',{})
 if audit.get('mechanism')=='first-order':
  v=audit['seed'];check(audit['values'][0]==v)
  for k,toll in enumerate(audit['tolls'],1):v=audit['a']*v+toll;check(audit['values'][k]==v)
page=(R/'dist/chapters/a_recurrence.html').read_text();base=subprocess.check_output(['git','show','86f1b64def331f48c7f9bfd1a05cdc463e99faa1:dist/chapters/a_recurrence.html']).decode().replace('\r\n','\n');tutorial=lambda t:re.findall(r'<h3[^>]*>Tutorial [\s\S]*?(?=<h3|<h2)',t)
def normalized_math_markup(s):
 def normalize(m):
  root=ET.fromstring(m[0])
  for p in root.iter():
   for c in list(p):
    if c.tag.split('}')[-1]=='mspace'and c.get('width')=='.14em':p.remove(c)
  return ET.tostring(root,encoding='unicode')
 return re.sub(r'<math\b[\s\S]*?</math>',normalize,s)
check([normalized_math_markup(v)for v in tutorial(page)]==[normalized_math_markup(v)for v in tutorial(base)]and len(tutorial(page))==40,'retained full tutorials; named-function spacing is the sole MathML typography repair')
check(page.count('data-deep-index=')==53 and page.count('<summary>Read the complete derivation')==53)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
mathblocks=re.findall(r'<math\b[\s\S]*?</math>',page)
for block in mathblocks:
 root=ET.fromstring(block);check(not closing_script_bases(root)and not delimiter_issues(root),block[:150])
sources=json.loads((E/'a_recurrence-course-recheck.json').read_text());check(sources['universityCountActuallyReadInThisRevision']==5)
for src in sources['sources']:
 if src.get('sha256'):
  ds=next(v for v in json.loads((E/'a_recurrence-source-recheck-downloads.json').read_text())if v.get('sha256')==src['sha256']);p=Path(ds['path'])if 'path'in ds else None
  if p and p.exists():check(hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256'])
original=json.loads((E/'a_recurrence-original-recheck.json').read_text());check(len(original)==7 and all(v['state'].startswith('original_image_actually')for v in original))
q=next(q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())if q['id']=='MS_CE_1405_Q58');check(q['options']==[r'$O(\log n\log\log n)$',r'$O(n\log n\log\log n)$',r'$O(n\log\log n)$',r'$O(\log\log n)$'])
parts=re.split(r'^### Solution (\d+)\s*$',(E/'a_recurrence-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)};check(len(answers)==53 and min(len(v.split())for v in answers.values())>=160)
from read_algorithm_recurrence_bank import rows
for f in range(9):
 start=16+4*f;_,_,_,closed=families[f]
 for j,n in enumerate([5,8]):r=rows[start+j-1];choice=r['options'][r['answer']-1];check(choice=='$'+str(closed(n))+'$',(start+j,choice,closed(n)))
record=dict(status='passed',checks=checks,topicId='a_recurrence',newModels=len(models),uniqueModelFrames=sum(len(s['frames'])for s in models.values()),nativeMathExpressions=len(mathblocks),roundedMergeIntegerInputs=1999,slowShrinkIntegerInputs=9999,expectedRankDistributions=499,questionCount=53,retainedTutorials=40,sourceUniversitiesActuallyRead=5,originalItemsActuallyViewed=7,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='Independent finite recurrence oracles, symbolic derivations and actual source/image reconciliation. No outside peer review, exhaustive nonlinear-recurrence coverage or universal examination guarantee is claimed.')
(E/'a_recurrence-mathematical-checks.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8');print(record)
