"""Independent exhaustive finite checks supplement the mathematical proofs."""
import itertools,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=(ROOT/'research/d_functions.en.md').read_text(encoding='utf-8')
code=re.search(r'```python\n(.*?)\n```',src,re.S).group(1);env={};exec(code,env);analyze=env['analyze_function']
def maps(m,n):return itertools.product(range(n),repeat=m)
def subsets(n):return [set(i for i in range(n) if bits>>i&1) for bits in range(1<<n)]
def im(f,s):return {f[x] for x in s}
def pre(f,t):return {x for x,v in enumerate(f) if v in t}
S={(0,0):1}
def stirling(m,n):
 if (m,n) in S:return S[m,n]
 if m==0 or n==0 or n>m:return 0
 S[m,n]=stirling(m-1,n-1)+n*stirling(m-1,n);return S[m,n]
checked=0;identities=0;count_rows=[];inverse_checks=0
for m in range(5):
 for n in range(5):
  counts=[0,0,0];ranks={k:0 for k in range(min(m,n)+1)}
  for f in maps(m,n):
   checked+=1;a=set(range(m));b=set(range(n));image=set(f)
   inj=len(image)==m;sur=image==b
   fibers,ci,cs,inv=analyze(f,n)
   assert (ci,cs)==(inj,sur)
   assert fibers==[[i for i,v in enumerate(f) if v==j] for j in range(n)]
   assert inv==([f.index(j) for j in range(n)] if inj and sur else None)
   counts[0]+=inj;counts[1]+=sur;counts[2]+=inj and sur;ranks[len(image)]+=1
   ins=subsets(m);outs=subsets(n)
   assert all(im(f,pre(f,t))==t&image for t in outs)
   assert all(s<=pre(f,im(f,s)) for s in ins)
   assert all(pre(f,im(f,pre(f,im(f,s))))==pre(f,im(f,s)) for s in ins)
   eq_inter=True;eq_diff=True
   for x,y in itertools.product(ins,repeat=2):
    assert im(f,x|y)==im(f,x)|im(f,y)
    assert im(f,x&y)<=im(f,x)&im(f,y)
    assert im(f,x)-im(f,y)<=im(f,x-y)
    eq_inter&=im(f,x&y)==im(f,x)&im(f,y)
    eq_diff&=im(f,x-y)==im(f,x)-im(f,y);identities+=1
   assert eq_inter==inj and eq_diff==inj
   for x,y in itertools.product(outs,repeat=2):
    assert pre(f,x|y)==pre(f,x)|pre(f,y)
    assert pre(f,x&y)==pre(f,x)&pre(f,y)
    assert pre(f,x-y)==pre(f,x)-pre(f,y)
   assert all(pre(f,b-t)==a-pre(f,t) for t in outs)
   assert sum(s==pre(f,im(f,s)) for s in ins)==2**len(image)
   # Enumerate actual inverse candidates on small carriers; count all, including empties.
   if m<=3 and n<=3:
    left=right=0
    for g in maps(n,m):
     left+=all(g[f[i]]==i for i in range(m))
     right+=all(f[g[j]]==j for j in range(n));inverse_checks+=1
    expected_left=(m**(n-m) if inj and m>0 else int(m==n==0))
    expected_right=(math.prod(len(z) for z in fibers) if sur else 0)
    assert left==expected_left and right==expected_right
  onto=sum((-1)**j*math.comb(n,j)*(n-j)**m for j in range(n+1))
  injection=math.factorial(n)//math.factorial(n-m) if m<=n else 0
  assert counts==[injection,onto,math.factorial(m) if m==n else 0]
  assert onto==math.factorial(n)*stirling(m,n)
  assert ranks=={k:math.comb(n,k)*math.factorial(k)*stirling(m,k) for k in ranks}
  count_rows.append({'m':m,'n':n,'injections':counts[0],'surjections':counts[1],'bijections':counts[2]})
for args in [([0],0),([True],1),([-1],2),([2],2),([],True),([], -1)]:
 try:analyze(*args)
 except ValueError:pass
 else:raise AssertionError(('Invalid input accepted',args))
# Check the chapter's nonbijective-factor example and all small composite implications.
composition_checks=0
for m,n,k in itertools.product(range(4),repeat=3):
 for f in maps(m,n):
  for g in maps(n,k):
   c=tuple(g[x] for x in f);fi=len(set(f))==m;gs=set(g)==set(range(k));ci=len(set(c))==m;cs=set(c)==set(range(k))
   assert not ci or fi;assert not cs or gs
   assert ci==(fi and len({g[x] for x in set(f)})==len(set(f)))
   assert cs==({g[x] for x in set(f)}==set(range(k)));composition_checks+=1
assert tuple([0,1,0][x] for x in [0,1])==(0,1)
assert 3**4-3*2**4+3==36 and 3*(2**4-2)==42
assert sum(math.comb(3,k)*k**(3-k) for k in range(1,4))==10
seen={}
for x,y in itertools.product(range(12),repeat=2):
 z=2**x*(2*y+1)-1;assert z not in seen;seen[z]=(x,y)
for z in range(10000):
 u=z+1;x=0
 while u%2==0:u//=2;x+=1
 y=(u-1)//2;assert 2**x*(2*y+1)-1==z
def sb(a):return 2*a if (a+1)&a==0 else a-1
assert len({sb(x) for x in range(1000)})==1000
for b in range(1000):
 a=b//2 if b%2==0 and (((b+2)//2)&((b+2)//2-1))==0 else b+1
 assert sb(a)==b
p=(ROOT/'research/d_functions-problems.en.md').read_text(encoding='utf-8');r=(ROOT/'research/d_functions-review.en.md').read_text(encoding='utf-8')
assert re.findall(r'### Problem (\d+)\.',p)==list(map(str,range(1,43))) and p.count('**Solution.**')==42
assert re.findall(r'^(\d+)\. ',r,re.M)==list(map(str,range(1,73)))
page=(ROOT/'dist/chapters/d_functions.html').read_text(encoding='utf-8')
from check_site_en import MathCoverage
for topic in ('d_functions',):
 coverage=MathCoverage();coverage.feed((ROOT/f'dist/chapters/{topic}.html').read_text(encoding='utf-8'))
 assert not coverage.unstyled,(topic,coverage.unstyled)
assert page.count('<figure ')==4 and page.count('<h2 ')==13 and '<munderover>' in page
assert not re.search(r'[\u0600-\u06ff]|\$|\\binom|<!--',page)
assert 'Student-approved chapter' in page
assert '^' not in page
outside_code=re.sub(r'<pre>.*?</pre>','',page,flags=re.S)
assert not re.search(r'>[^<]*_[^<]*<',outside_code)
report={'finiteFunctionsChecked':checked,'inputSubsetPairsChecked':identities,'inverseCandidatesChecked':inverse_checks,'compositePairsChecked':composition_checks,'finiteCounts':count_rows,'pairingTargetsDecoded':10000,'workedProblems':42,'examinationRules':72,'figures':4,'newChapterMathCoverageChecked':True,'limitations':'Finite checks are independent error detectors, not proofs for arbitrary or infinite sets.'}
(ROOT/'research/d_functions-finite-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='finiteCounts'}))
