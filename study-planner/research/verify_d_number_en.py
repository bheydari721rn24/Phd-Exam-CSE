"""Independent finite error detectors for the actual algorithms and worked results."""
import itertools,json,math,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];base=ROOT/'research'
main=(base/'d_number.en.md').read_text(encoding='utf-8');problems=(base/'d_number-problems.en.md').read_text(encoding='utf-8');review=(base/'d_number-review.en.md').read_text(encoding='utf-8')
env={}
for code in re.findall(r'```python\n(.*?)\n```',main,re.S):exec(code,env)
egcdcases=0
for a,b in itertools.product(range(-100,101),repeat=2):
 g,s,t=env['egcd'](a,b);assert g==math.gcd(a,b) and s*a+t*b==g;egcdcases+=1
powercases=0
for a,e,m in itertools.product(range(-15,16),range(40),range(1,31)):
 assert env['modpow'](a,e,m)==pow(a,e,m);powercases+=1
# The actual JavaScript is exercised against an independently enumerated Python oracle.
js="""const {analyze,egcd}=require('./dist/chapters/d_number.js');let rows=[];
for(let m=1;m<=30;m++)for(let a=-15;a<=15;a++)for(let b=-15;b<=15;b++){let r=analyze(a,b,m);rows.push([a,b,m,r.g,r.s,r.t,r.solutions,r.image,r.kernel]);}
let rejected=0;for(const xs of [[1.5,2,3],[1,2,0],[1,2,61],[10001,2,3],[1,Infinity,3]]){try{analyze(...xs)}catch(e){rejected++}}if(rejected!==5)throw Error('boundary rejection');process.stdout.write(JSON.stringify(rows));"""
out=subprocess.run(['node','-e',js],cwd=ROOT,check=True,capture_output=True,text=True)
labrows=json.loads(out.stdout)
for a,b,m,g,s,t,solutions,image,kernel in labrows:
 ys=[a*x%m for x in range(m)]
 assert g==math.gcd(a,m) and a*s+m*t==g
 assert solutions==[x for x in range(m) if a*x%m==b%m]
 assert image==sorted(set(ys)) and kernel==[x for x in range(m) if ys[x]==0]
# Independent generalized-CRT construction and brute-force oracle, including modulus one.
crtcases=0
for m,n in itertools.product(range(1,13),repeat=2):
 g,s,t=env['egcd'](m,n);period=math.lcm(m,n)
 for a,b in itertools.product(range(m),range(n)):
  roots=[x for x in range(period) if x%m==a and x%n==b]
  if (b-a)%g:assert roots==[]
  else:
   x=(a+m*((s*((b-a)//g))%(n//g)))%period;assert roots==[x]
  crtcases+=1
assert 4*252-5*198==18
assert [(x,y) for x in range(8) for y in range(12) if 14*x+9*y==100]==[(2,8)]
assert [x for x in range(100) if 14*x%100==30]==[45,95]
assert [x for x in range(35) if 6*x%14==8 and 4*x%10==6]==[34]
assert [x for x in range(60) if x%4==1 and x%6==3 and x%10==9]==[9]
assert [pow(a,e,m) for a,e,m in [(7,222,40),(2,100,12),(12,100,175),(6,50,200),(3,3**20,100)]]==[9,4,51,176,3]
assert [x for x in range(35) if x*x%35==1]==[1,6,29,34]
assert [x for x in range(72) if x*x%72==0]==list(range(0,72,12))
assert [x for x in range(16) if x*x%16==1]==[1,7,9,15]
ds=[d for d in range(1,361) if 360%d==0];assert (len(ds),sum(ds))==(24,1170)
assert sum(math.gcd(x,360)==1 for x in range(360))==96
assert pow(2,340,341)==1 and 341==11*31 and 30031==59*509
assert pow(pow(5,3,55),27,55)==5
assert all(pow(pow(x,3,55),27,55)==x for x in range(55))
assert math.comb(10,6)==210
fact=math.factorial(100);valuations={}
for p in [2,3,5]:
 n=fact;c=0
 while n%p==0:n//=p;c+=1
 valuations[p]=c
assert valuations=={2:97,3:48,5:24}
# General finite theorem checks use enumeration, not a mirrored formula.
totientcases=0
for n in range(2,101):
 units=[a for a in range(n) if math.gcd(a,n)==1]
 for a in units:assert pow(a,len(units),n)==1;totientcases+=1
coincases=0
for a,b in itertools.product(range(2,15),repeat=2):
 if math.gcd(a,b)!=1:continue
 f=a*b-a-b;reachable={a*x+b*y for x in range(3*b+1) for y in range(3*a+1)}
 assert f not in reachable and all(n in reachable for n in range(f+1,f+1+a));coincases+=1
rootcases=0
for n in range(1,301):
 remainder=n;factors=[]
 for p in range(2,n+1):
  if remainder%p:continue
  e=0
  while remainder%p==0:remainder//=p;e+=1
  factors.append((p,e))
 expected_zero=math.prod(p**(e//2) for p,e in factors)
 expected_one=math.prod((1 if e==1 else 2 if e==2 else 4) if p==2 else 2 for p,e in factors)
 assert sum(x*x%n==0 for x in range(n))==expected_zero
 assert sum(x*x%n==1%n for x in range(n))==expected_one;rootcases+=1
assert re.findall(r'### Problem (\d+)\.',problems)==list(map(str,range(1,41))) and problems.count('**Solution.**')==40
assert re.findall(r'^(\d+)\. ',review,re.M)==list(map(str,range(1,71)))
page=(ROOT/'dist/chapters/d_number.html').read_text(encoding='utf-8')
from check_site_en import MathCoverage
c=MathCoverage();c.feed(page);assert not c.unstyled,c.unstyled
assert page.count('<figure ')==4 and page.count('<h2 ')==12 and page.count('<munderover>')>=1
assert not re.search(r'[\u0600-\u06ff]|\$|\\\\|<!--',page)
assert '^' not in re.sub(r'<pre>.*?</pre>','',page,flags=re.S)
assert 'Student-approved chapter' in page
report={'extendedEuclidSignedPairs':egcdcases,'modularPowerInputs':powercases,'laboratoryMapsComparedWithIndependentEnumeration':len(labrows),'generalizedCRTSystems':crtcases,'EulerUnitCases':totientcases,'coprimeCoinPairs':coincases,'quadraticRootCountModuli':rootcases,'workedProblems':40,'completeExaminationRules':70,'figures':4,'limits':'Finite checks detect errors; general results rely on the written proofs. Iranian examination archives remain deferred.'}
(base/'d_number-finite-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
