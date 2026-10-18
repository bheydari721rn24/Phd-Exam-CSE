"""Exact independent checks for the twenty-four current replacement solutions only."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,re,sys
import sympy as S
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
count=0
def check(v,msg=''):
 global count
 assert v,msg
 count+=1
x=S.symbols('x');check(S.expand(2*(3*x-2)+5)==6*x+1);check(S.expand(3*(2*x+5)-2)==6*x+13)
check(2*(3*4-2)+5==25);check([n for n in range(-100,101)if 17<=3*(2*n+1)-4<=41]==list(range(3,8)))
state=1
for k in range(31):
 check(state==4*2**k-3)
 state=2*state+3
for n in range(4097):
 current=n;calls=0
 while current:
  current//=2;calls+=1;check(current==n//(2**calls))
 check(calls==n.bit_length())
check(83 .bit_length()==7);check(S.expand(-2*(3*x-1)+7)==9-6*x);check(3*0-1==-1)
for n in range(100):check(sum(2*k+1 for k in range(n))==n*n)
check(2*((2*3)+1)==14);check((2*3+1)+(2*(2*3+1)+1)==22)
for p in range(-25,26):
 v=Fraction(p,2)
 if v in [1,2]:continue
 inner=1/(v-2);outer=1/(inner+1);check(outer==(v-2)/(v-1))
caller=7
for _ in range(13):
 parameter=caller;parameter+=4;check(caller==7 and parameter==11)
def recursive(n,depth=1):
 if not n:return 0,1,depth
 value,calls,peak=recursive(n-1,depth+1);return n+value,1+calls,peak
for n in range(40):
 value,calls,depth=recursive(n);check(value==n*(n+1)//2 and calls==depth==n+1)
for bits in range(2,13):
 U=2**(bits-1)-1
 for L in [-U,-U-1]:
  lower=-((-L)//2);upper=(U-1)//2
  for v in range(L,U+1):check((lower<=v<=upper)==(L<=2*v<=U and L<=2*v+1<=U))
L,U=-(2**31),2**31-1;check(-((-L)//2)==-1073741824 and (U-1)//2==1073741823)
check((12+1)+4==17)
outer=5;inner=2;inner+=3;result=inner;outer+=result;check((outer,result)==(10,5))
sf=sg=0;returns=[]
for name in ['f','g','f','g']:
 if name=='f':sf+=1;returns.append(sf)
 else:sg+=2;returns.append(sg)
check(returns==[1,2,2,4]and(sf,sg)==(2,4))
saved=1;returns=[]
for d in [2,3,-1]:local=1+d;saved+=local;returns.append(saved)
check(returns==[4,8,8])
def stateful(n,state):
 if not n:return state[0]
 state[0]+=1;returned=stateful(n-1,state);return returned+n
for n in range(20):
 for prior in range(10):
  state=[prior];value=stateful(n,state);check(value==prior+n+n*(n+1)//2 and state[0]==prior+n)
for u in range(-20,21):
 for v in range(-20,21):
  objects=[u,v];objects[0]+=2;objects[1]*=3;check(objects==[u+2,3*v])
for u in range(-200,201):
 obj=[u];p=q=obj;p[0]+=2;q[0]*=3;check(obj[0]==3*u+6);check(obj[0]-(3*u+2)==4)
path=E/'p_functions-answer-rewrites.en.md';text=path.read_text(encoding='utf8');ids=re.findall(r'^## (PF\d+)',text,re.M);check(ids==['PF'+str(n).zfill(2)for n in range(1,25)])
formulas=re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',text)
for block,inline in formulas:mathml.render(block or inline,bool(block));check(True)
report=dict(date='2026-10-18',state='partial_review_manuscript_checked_not_integrated',rewrittenAnswers=ids,assertions=count,nativeFormulaChecks=len(formulas),inputSha256=hashlib.sha256(path.read_bytes()).hexdigest(),limits='Exact mathematical integers/rationals, finite representability models and semantic call activations. No C compiler/ABI execution is claimed. Only these twenty-four blocks checked; whole-chapter review remains incomplete.')
(E/'p_functions-review-start-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print(report)
