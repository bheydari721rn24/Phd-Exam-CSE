"""Independent finite oracles for exact mathematical and executable claims."""
import json,re,subprocess,itertools
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'research'
main=(R/'a_recurrence.en.md').read_text(encoding='utf-8')
bank=(R/'a_recurrence-problems.en.md').read_text(encoding='utf-8')
review=(R/'a_recurrence-review.en.md').read_text(encoding='utf-8')
assert [int(n) for n in re.findall(r'^### Problem (\d+)\.',bank,re.M)]==list(range(1,41))
assert len(re.findall(r'\*\*Solution\.\*\*',bank))==40
assert [int(n) for n in re.findall(r'^(\d+)\. ',review,re.M)]==list(range(1,81))
for t in (main,bank,review):
 for line in t.splitlines():assert line.count('$')%2==0,line
 assert not re.search(r'[\u0600-\u06ff]',t)
page=(ROOT/'dist/chapters/a_recurrence.html').read_text()
assert page.count('<figure ')==4 and page.count('<math ')==4
assert '<!--' not in page and '$' not in page
assert 'Review draft' in page and '<sup>' in page and '<sub>' in page
from check_site_en import MathCoverage
coverage=MathCoverage();coverage.feed(page)
assert not coverage.unstyled,coverage.unstyled

# Actual copied lesson function, validated against independently enumerated trees.
fence=chr(96)*3
code=re.search(fence+r'python\n(.*?)'+fence,main,re.S).group(1);namespace={}
exec(compile(code,'lesson-python','exec'),namespace)
def enumerate_tree(a,b,q,h,base):
 frontier=[b**h];cost=0
 for _ in range(h):
  cost+=sum(size**q for size in frontier)
  frontier=[size//b for size in frontier for _ in range(a)]
 return cost+len(frontier)*base
cases=[];expected=[]
for a,b,q,h,base in itertools.product(range(1,5),range(2,5),range(4),range(6),[1,3,5]):
 case=dict(a=a,b=b,q=q,h=h,base=base);value=enumerate_tree(**case)
 assert namespace['ideal_cost'](**case)==value
 cases.append(case);expected.append(value)
# Precision regression includes a cost above Number.MAX_SAFE_INTEGER.
for case in [dict(a=6,b=6,q=4,h=8,base=20),dict(a=1,b=2,q=0,h=0,base=7)]:
 value=namespace['ideal_cost'](**case);cases.append(case);expected.append(value)
node="const fs=require('fs');const {analyze}=require('./dist/chapters/a_recurrence.js');const cases=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(cases.map(c=>analyze(c))))"
run=subprocess.run(['node','-e',node],cwd=ROOT,input=json.dumps(cases),text=True,capture_output=True,check=True)
results=json.loads(run.stdout)
for case,want,result in zip(cases,expected,results):
 assert int(result['total'])==int(result['levelTotal'])==want
 assert int(result['terminal'])==case['a']**case['h']*case['base']
 assert len(result['rows'])==case['h']+1
 assert result['rows'][-1]['terminal'] and result['rows'][-1]['size']=='1'
assert max(expected)>2**53
for bad in [dict(a=0,b=2,q=1,h=4,base=1),dict(a=True,b=2,q=1,h=4,base=1),dict(a=2,b=1,q=1,h=4,base=1),dict(a=2,b=2,q=1,h=9,base=1)]:
 try:namespace['ideal_cost'](**bad)
 except ValueError:pass
 else:raise AssertionError(bad)

# Rounded merge counts: direct dynamic recurrence vs a closed form.
cost=[0,0]
for n in range(2,1025):
 cost.append(cost[n//2]+cost[(n+1)//2]+n-1)
 h=(n-1).bit_length();assert cost[n]==n*h-2**h+1
assert cost[5]==8 and cost[8]==17
# Zero, repeated-root, cancellation and forcing examples.
u,v=F(1),10;sequence=[4,6];cancel=[4,4];repeated=[1,4];forced=3
for n in range(1,61):
 u=F(n,n+1)*u+1;assert u==F(n+2,2)
 v=(2*v+3 if n==1 else 5 if n==2 else 2*v+1)
 if n>=2:assert v==6*2**(n-2)-1
 forced=2*forced+2**n;assert forced==(n+3)*2**n
 if n>=2:
  sequence.append(3*sequence[-1]-2*sequence[-2]);assert sequence[n]==2+2**(n+1)
  cancel.append(3*cancel[-1]-2*cancel[-2]);assert cancel[n]==4
  repeated.append(4*repeated[-1]-4*repeated[-2]);assert repeated[n]==(n+1)*2**n
# Harmonic critical toll and polynomial logarithmic toll, exact rational oracles.
t=F(2);harmonic=F(1);log_cost=1
for h in range(2,129):
 n=2**h;t=2*t+F(n,h);harmonic+=F(1,h);assert t/n==harmonic
for h in range(1,61):
 n=2**h;log_cost=2*log_cost+n*h;assert log_cost==n*(1+F(h*(h+1),2))
# Floor composition and stopping, without floating logarithms.
for b in range(2,7):
 for n in range(1,257):
  size=n;depth=0
  while size>=b:
   size//=b;depth+=1;assert size==n//(b**depth)
  assert b**depth<=n<b**(depth+1)
# Child progress with ceiling plus offset.
for n in range(5,2049):assert (n+1)//2+1<n and ((n+1)//2+1)-3<=F(n-3,2)
# Actual dyadic alternating-toll counterexample to omitted regularity.
value=1
for h in range(1,19):
 n=2**h;toll=n**(2 if h%2==0 else 3);value=2*value+toll
 if h%2==0:assert F(value,toll)>=F(n,4)
# Characteristic weighted equations and the six-constant quadratic bound.
assert 2*F(1,4)+3*F(1,6)==1
assert 2*F(1,4)+3*F(1,9)==F(5,6)
assert 6*F(5,6)+1==6 and F(1,5)+F(7,10)==F(9,10)
fib=[0,1];calls=[1,1]
for n in range(2,61):
 fib.append(fib[-1]+fib[-2]);calls.append(calls[-1]+calls[-2]+1)
 assert calls[n]==2*(fib[n]+fib[n-1])-1
rows=json.loads((ROOT/'dist/lessons.json').read_text())
flat=[c for w in rows for c in w['chapters']]
assert next(c for c in flat if c['topicId']=='d_number')['status']=='ready'
assert next(c for c in flat if c['topicId']=='a_recurrence')['status']=='draft'
report={'laboratoryOracleCases':len(cases),'arbitraryPrecisionVerified':True,'mergeInputsVerified':1024,
 'workedProblems':40,'reviewRules':80,'figures':4,'mathmlDisplays':4,
 'oracles':['explicit recursive-node enumeration','rounded merge dynamic recurrence','first-order rational recurrence','characteristic roots and resonance','harmonic critical normalization','floor stopping','ceiling progress','regularity counterexample','weighted child equations','Fibonacci dependency count'],
 'limits':'Finite checks support the stated general proofs; they do not certify every possible unseen recurrence.'}
(R/'a_recurrence-math-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
