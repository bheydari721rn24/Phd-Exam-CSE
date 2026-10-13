"""Independent brute-force oracles, certificates, canonical originals and actual model values."""
from pathlib import Path
import ast, hashlib, itertools, json, math, re, subprocess, sys, xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=0
def check(ok,label=''):
 global checks
 assert ok,label;checks+=1
def factors(n):
 out=[];p=2
 while p*p<=n:
  if n%p==0:
   e=0
   while n%p==0:n//=p;e+=1
   out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return out
def egcd(a,b):
 r,u,v=abs(a),1 if a>0 else -1 if a<0 else 0,0;s,w,z=abs(b),0,1 if b>0 else -1 if b<0 else 0
 while s:
  check(r==u*a+v*b and s==w*a+z*b)
  q=r//s;r,s,u,w,v,z=s,r-q*s,w,u-q*w,z,v-q*z
 return r,u,v
for a in range(-40,41):
 for b in range(-40,41):
  d,u,v=egcd(a,b);check(d==math.gcd(a,b) and u*a+v*b==d)
linearCases=0
for m in range(1,41):
 for a in range(-m,m+1):
  d=math.gcd(a,m)
  for b in range(-m,m+1):
   actual=[x for x in range(m)if(a*x-b)%m==0];check(len(actual)==(d if b%d==0 else 0));linearCases+=1
  for z in range(-2*m,2*m+1):check((a*z)%m==0 if z%(m//d)==0 else(a*z)%m!=0)
crtCases=0
for m in range(1,17):
 for n in range(1,17):
  d=math.gcd(m,n);L=math.lcm(m,n)
  for r in range(m):
   for s in range(n):
    actual=[x for x in range(L)if x%m==r and x%n==s];check(len(actual)==(1 if(r-s)%d==0 else 0));crtCases+=1
    if actual:check(all((actual[0]+k*L)%m==r and(actual[0]+k*L)%n==s for k in [-2,-1,0,1,2]))
tripleCases=0
for ms in itertools.product(range(1,9),repeat=3):
 L=math.lcm(*ms);coords={tuple(x%m for m in ms)for x in range(L)}
 for rs in itertools.product(*(range(m)for m in ms)):
  compatible=all((rs[i]-rs[j])%math.gcd(ms[i],ms[j])==0 for i in range(3)for j in range(i));check((rs in coords)==compatible);tripleCases+=1
rootCases=0
for m in range(1,301):
 fs=factors(m)
 for k in range(1,6):
  D=math.prod(p**math.ceil(e/k)for p,e in fs);actual=[x for x in range(m)if pow(x,k,m)==0];check(actual==list(range(0,m,D)));rootCases+=1
 roots=[x for x in range(m)if x*x%m==1%m];expected=math.prod((1 if e==1 else 2 if e==2 else 4)if p==2 else 2 for p,e in fs);check(len(roots)==expected)
 for a in range(min(m,31)):
  v=1%m;seq=[]
  for k in range(72):seq.append(v);v=v*a%m
  if math.gcd(a,m)==1:
   period=next(k for k in range(1,m+1)if pow(a,k,m)==1%m);check(all(seq[k]==seq[k%period]for k in range(len(seq))))
  else:
   unitMod=math.prod(p**e for p,e in fs if a%p);zeroMod=m//unitMod
   T=0
   for p,e in fs:
    if a%p:continue
    if a==0:T=max(T,1);continue
    q=a;v=0
    while q%p==0:q//=p;v+=1
    T=max(T,math.ceil(e/v))
   period=1 if unitMod==1 else next(k for k in range(1,unitMod+1)if pow(a,k,unitMod)==1)
   check(all(seq[k]%zeroMod==0 for k in range(T,len(seq))))
   check(all(seq[k]==seq[k+period]for k in range(T,len(seq)-period)))
for n in range(101):
 N=math.factorial(n);v=0
 while N%2==0:N//=2;v+=1
 check(v==n-n.bit_count())
for n in range(1,10):
 check(sum((6*x-12)%(6*n)==0 for x in range(6*n))==6)
 if n>=2:check(next(x for x in range(n*(n+1))if x%n==1 and x%(n+1)==2)==n*n+1)
 check(sum(math.gcd(x,27*2**n)==1 for x in range(27*2**n))==18*2**(n-1))
 check(math.gcd(2**n*3**(n+2),2**(n+1)*3**n)==6**n)
 check(pow(3,4*n+1,10)==3)
 # Factor-exponent counts use a direct list of prime products rather than the closed formula.
 ds={2**i*3**j for i in range(n+1)for j in range(3)};check(len(ds)==3*(n+1))
 sq={2**i*3**j*5**k for i in range(0,2*n+1,2)for j in range(0,2*n+2,2)for k in[0,2]};check(len(sq)==2*(n+1)**2)
check([x for x in range(84)if(12*x-18)%30==0]==list(range(4,84,5)))
check([x for x in range(24)if x%8==5 and x%6==1]==[13])
check(pow(6,100,15)==6 and pow(6,8,15)==6 and pow(6,0,15)==1)
check([x for x in range(30)if math.gcd(x,30)==1 and x%3==1]==[1,7,13,19])
check([(x,(45-6*x)//9)for x in range(11)if(45-6*x)%9==0]==[(0,5),(3,3),(6,1),(9,-1)])
check(sum((6*x-8)%14==0 for x in range(101))==14)
check(next(x for x in range(36)if x%12==5 and x%18==11)==29)
check([x for x in range(-100,101)if(18*x-30)%42==0 and(10*x-20)%30==0]==[-94,-73,-52,-31,-10,11,32,53,74,95])
check([x for x in range(501)if x%4==1 and x%6==3 and x%10==9]==list(range(9,501,60)))
check(pow(18,60,1000)==376 and pow(2,2**20,72)==16)
check([x for x in range(360)if x*x%360==1]==[1,19,71,89,91,109,161,179,181,199,251,269,271,289,341,359])
check([x for x in range(2160)if x**3%2160==0]==list(range(0,2160,60)))
check(math.comb(30,12)%2==1)
check(all(pow(pow(x,3,55),27,55)==x for x in range(55)))
check(sum(a%2==0 and b<=4 and 40-a-b>=1 for a in range(41)for b in range(41-a))==96)
check(math.comb(15,9)==5005)
data=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'];models={k:s for k,s in data.items()if k.startswith('discrete-number-question-')}
check(len(models)==41)
for id,s in models.items():
 for f in s['frames']:
  ET.fromstring(f['formulaHtml']);snap=f['snapshot'];kind=snap['kind']
  if kind=='residue-grid':check(0<=snap['inspected']<=len(snap['values']) and set(snap['accepted'])<=set(snap['values']))
  if kind=='crt-grid':check(snap['pairs']==[[x%snap['m'],x%snap['n'],x]for x in range(math.lcm(snap['m'],snap['n']))])
  if kind=='prime-grid':check(snap['valid']==[[i,j]for i,j in snap['coords']if not snap['square']or i%2==j%2==0])
  if kind=='power-orbit':check(snap['values']==[pow(snap['a'],k,snap['m'])for k in range(len(snap['values']))])
  if kind=='table':check(len(snap['rowsHtml'])<=7 and all(len(r)==len(snap['headings'])for r in snap['rows']))
  if kind=='exponent-grid':check(snap['exponents']==[3*j-15 for j in range(16)]and snap['coefficients']==[math.comb(15,j)for j in range(16)]and 14 not in snap['exponents'])
page=(R/'dist/chapters/d_number.html').read_text();base=subprocess.check_output(['git','show','77f4b6dd3bbabb32ac75667b0a2f83f6f8518306:dist/chapters/d_number.html']).decode();tutorial=lambda t:re.findall(r'<h3[^>]*>Tutorial [\s\S]*?(?=<h3|<h2)',t)
base=base.replace('<span class="math-inline">B</span>ézout','Bézout')
check(tutorial(page)==tutorial(base)and len(tutorial(page))==40,'all forty full tutorials retained except explicit Bezout word-font repair')
for m in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(m);check(True)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
for m in re.findall(r'<math\b[\s\S]*?</math>',page):root=ET.fromstring(m);check(not delimiter_issues(root) and not closing_script_bases(root))
from read_discrete_number_bank import rows
check(len(rows)==47)
canon={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
for id in ['MS_CS_1405_Q38','MS_CS_1405_Q125','MS_CS_1405_Q129','Phd_CS_1404_Q25','Phd_CS_1404_Q28']:
 q=canon[id];p=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/q['repoPath'];check(hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSha256'])
check(canon['MS_CS_1405_Q129']['answer']==4 and 'a+b+c=40'in canon['MS_CS_1405_Q129']['stem'])
revision=json.loads((E/'d_number-revision.json').read_text());check(all(r['words']>=120 for r in revision['records']))
report=dict(topicId='d_number',status='passed_independent_finite_oracles',checks=checks,linearCongruenceInputTriples=linearCases,twoModulusTargetSystems=crtCases,threeModulusTargetSystems=tripleCases,powerZeroRootSystems=rootCases,models=len(models),frames=sum(len(s['frames'])for s in models.values()),retainedTutorials=40,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='Explicit finite domains and authored general proofs support the recorded statements. No literal universal zero-error or unseen-question guarantee is asserted.')
(E/'d_number-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(report)
