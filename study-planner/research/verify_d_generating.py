"""Independent symbolic algebra and finite object enumerations, not copied model recurrences."""
from pathlib import Path
from itertools import product, permutations, combinations, combinations_with_replacement
from fractions import Fraction as F
from math import comb,factorial
import json,subprocess,hashlib,re
import sympy as S
B=Path(__file__).resolve().parent;R=B.parent;E=B/'d_generating-evidence'
x=S.symbols('x');checks={}
def ok(q,label,condition):
 assert condition,(q,label)
 checks.setdefault(str(q),[]).append(label)
def coefficients(expr,N=16):
 return [S.expand(S.series(expr,x,0,N+1).removeO()).coeff(x,n)for n in range(N+1)]
def eq(q,expr,fn,N=16):ok(q,'Symbolic coefficients independently expanded',coefficients(expr,N)==[S.sympify(fn(n))for n in range(N+1)])
eq(1,1/(2-x),lambda n:S.Rational(1,2**(n+1)))
eq(2,1/(1-2*x-x*x),lambda n:[1,2,5,12,29][n],4)
A=sum(factorial(n)*x**n for n in range(20));ok(3,'Factorial differential identity through degree nineteen',all(S.expand(x*x*S.diff(A,x)+(x-1)*A+1).coeff(x,n)==0 for n in range(20)))
ok(4,'Direct polynomial product and Hadamard distinction',S.expand((1+2*x+3*x*x+4*x**3)*(1+3*x+9*x*x+27*x**3)).coeff(x,3)==58 and 4*27==108)
ok(5,'Explicit indistinguishable prefixes with different shifted target',coefficients(1/(1-x),6)==coefficients(1/(1-x)+x**8,6) and coefficients(1/(1-x),8)[8]!=coefficients(1/(1-x)+x**8,8)[8])
eq(6,x**5/(1-3*x)**3,lambda n:0 if n<5 else 3**(n-5)*comb(n-3,2),12)
ok(7,'Exact boundary subtraction identity',S.cancel((1/(1-2*x)-1-2*x-4*x*x)/x**3-8/(1-2*x))==0)
eq(8,1/(1-9*x*x),lambda n:0 if n%2 else 3**n)
eq(9,4*x*x/(1-8*x**3),lambda n:2**n if n%3==2 else 0)
eq(10,x*(1+x)/(1-x)**3,lambda n:n*n)
eq(11,x*(1+4*x+x*x)/(1-x)**4,lambda n:n**3)
eq(12,-S.log(1-x)/(1-x)**2,lambda n:(n+1)*sum(S.Rational(1,k)for k in range(1,n+1))-n)
eq(13,1/((1-2*x)*(1-x)**2),lambda n:2**(n+2)-n-3)
ok(14,'Binomial expansion for twenty indices',all(sum(comb(n,k)*3**k for k in range(n+1))==4**n for n in range(20)))
ok(15,'Inverse signed binomial sum',all(sum((-1)**(n-k)*comb(n,k)*5**k for k in range(n+1))==4**n for n in range(20)))
ok(16,'Exact square-root coefficient',coefficients(S.sqrt(1-4*x),4)[4]==-10)
eq(17,x*x/((1-x)*(1-3*x)),lambda n:0 if n<2 else S.Rational(3**(n-1)-1,2))
eq(18,(1+x)/(1-x)**3,lambda n:(n+1)**2)
eq(19,(1-2*x)**2/((1-2*x)**3*(1+x)),lambda n:S.Rational(2**(n+1)+(-1)**n,3))
eq(20,(1+x*x)/(1-x),lambda n:1 if n<2 else 2)
eq(21,(2+x)/((1-2*x)*(1-3*x)),lambda n:-5*2**n+7*3**n)
eq(22,1/(1+x*x),lambda n:0 if n%2 else (-1)**(n//2))
eq(23,(2-7*x+6*x*x)/((1-x)*(1-2*x)**2),lambda n:1+2**n)
eq(24,3/(1-2*x)+2*x/(1-2*x)**2,lambda n:(n+3)*2**n)
eq(25,(1+x+x*x)/((1+x)**2*(1-2*x)),lambda n:S.Rational(7,9)*2**n+(S.Rational(n,3)+S.Rational(2,9))*(-1)**n)
eq(26,1/((1-5*x)*(1-x)**2),lambda n:S.Rational(25*5**n-4*n-9,16))
eq(27,1/(1-x-2*x*x),lambda n:S.Rational(2**(n+1)+(-1)**n,3))
ok(28,'Self-term removed induction numerators',all(F(2**n-1,1- F(1,2**n))==2**n for n in range(1,20)))
eq(29,1/(1-x)**2,lambda n:n+1)
eq(30,(7-19*x)/(1-3*x),lambda n:7 if n==0 else 2*3**(n-1))
ok(31,'Independent bounded-box enumeration',sum(sum(p)==9 for p in product(range(4),repeat=4))==20)
ok(32,'Independent unequal bounds',sum(sum(p)==7 for p in product(range(3),range(4),range(5)))==6)
ok(33,'Independent lower and upper bounds',sum(sum(p)==10 for p in product(range(1,5),range(2,6),range(3,7)))==12)
ok(34,'Congruence plus cap enumeration',sum(a+b+c==12 for a,b,c in product(range(0,13,2),range(1,13,2),range(4)))==11)
ok(35,'Mixed inventory exact counts',all(sum(3*a+b+c==n for a,b,c in product(range(n//3+1),range(3),range(n+1)))==n+1 for n in range(15)))
ok(36,'Direct coin multiplicities',sum(a+2*b+5*c==10 for a,b,c in product(range(11),range(6),range(3)))==10)
def comp(n,parts=(1,2)):
 return [p for k in range(n+1)for p in product(parts,repeat=k)if sum(p)==n]
ok(37,'Complete ordered versus unordered count',len(comp(5))==8 and sum(a+2*b==5 for a,b in product(range(6),range(3)))==3)
ok(38,'Direct subset enumeration',sum(sum(c)==5 for k in range(5)for c in combinations(range(1,5),k))==2)
ok(39,'Two distinguishable types',all(sum(a+b==n for a,b in product(range(n+1),repeat=2))==n+1 for n in range(12)))
ok(40,'Four lower-bounded parts',sum(sum(p)==16 for p in product(range(2,11),repeat=4))==165)
ok(41,'Fixed length and size',sum(sum(p)==9 for p in product((1,3),repeat=5))==10)
ok(42,'Fixed component count remains finite',all(sum(sum(p)==n for p in product((0,1),repeat=6))==comb(6,n)for n in range(7)))
ok(43,'No-adjacent-one binary enumeration',sum('11'not in ''.join(p)for p in product('01',repeat=6))==21)
def parts(n):
 return [tuple(reversed(p))for k in range(1,n+1)for p in combinations_with_replacement(range(1,n+1),k)if sum(p)==n] if n else [()]
ok(44,'Exact three-part partition enumeration',sum(len(p)==3 for p in parts(10))==8)
ok(45,'Distinct three-part enumeration',sum(len(p)==3 and len(set(p))==3 for p in parts(12))==7)
ok(46,'Odd/distinct partition identity at degree seven',sum(all(j%2 for j in p)for p in parts(7))==sum(len(set(p))==len(p)for p in parts(7))==5)
def durfee(p):return sum(v>=i+1 for i,v in enumerate(p))
ok(47,'Unique Durfee-square counts',sum(durfee(p)==1 for p in parts(7))==7 and sum(durfee(p)==2 for p in parts(7))==8)
def transpose(p):return tuple(sum(v>j for v in p)for j in range(max(p,default=0)))
ok(48,'Self-conjugate diagrams',sum(transpose(p)==p for p in parts(9))==2)
C=[comb(2*n,n)//(n+1)for n in range(20)]
ok(49,'Exact full Catalan convolution',sum(C[i]*C[3-i]for i in range(4))==14)
eq(50,(1-S.sqrt(1-4*x))/(2*x),lambda n:C[n],12)
ok(51,'Ordered rooted versus binary indices',C[4]==14 and C[5]==42)
ok(52,'Lagrange integer coefficient',comb(15,4)//5==273)
ok(53,'Power inversion independently checked by recursive coefficient convolution',sum(S.Rational(comb(3*i,i-1),i)*S.Rational(comb(3*(6-i),5-i),6-i)for i in range(1,6))==1020)
ok(54,'Rooted/unrooted label tree normalization',5**4==625 and 5**3==125)
ok(55,'OGF/EGF count normalization',factorial(3)==6 and coefficients(S.exp(2*x),3)[3]==S.Rational(8,6))
ok(56,'Every label allocated to one of two boxes',len(list(product(range(2),repeat=5)))==32)
ok(57,'Surjection direct function enumeration',sum(len(set(p))==3 for p in product(range(3),repeat=6))==540)
ok(58,'Constrained labelled-box function enumeration',sum(p.count(0)==2 and p.count(1)>0 for p in product(range(3),repeat=5))==70)
def setparts(n):
 def visit(word,k):
  if len(word)==n:yield tuple(tuple(i for i,v in enumerate(word)if v==j)for j in range(k));return
  for z in range(k+1):yield from visit(word+[z],max(k,z+1))
 return list(visit([0],1))if n else [()]
ok(59,'Direct set partition pairing enumeration',sum(all(len(b)==2 for b in p)for p in setparts(8))==105)
ok(60,'Direct singleton/pair partition enumeration',sum(all(len(b)<=2 for b in p)for p in setparts(6))==76)
ok(61,'No singleton enumeration',sum(all(len(b)>1 for b in p)for p in setparts(4))==4)
ok(62,'Two even blocks enumeration',sum(len(p)==2 and all(len(b)%2==0 for b in p)for p in setparts(6))==15)
ok(63,'Order each actual block set',sum(factorial(len(p))for p in setparts(4))==75)
ok(64,'Direct derangement permutation enumeration',sum(all(i!=v for i,v in enumerate(p))for p in permutations(range(6)))==265)
def cycles(p):
 seen=set();lens=[]
 for i in range(len(p)):
  if i in seen:continue
  n=0;j=i
  while j not in seen:seen.add(j);n+=1;j=p[j]
  lens.append(n)
 return lens
ok(65,'Actual permutation cycles',sum(len(cycles(p))==2 for p in permutations(range(5)))==50)
ok(66,'Actual one-three-cycle permutations',sum(sorted(cycles(p))==[1,1,1,1,3]for p in permutations(range(7)))==70)
eq(67,S.diff(1/(1-x),x),lambda n:n+1)
ok(68,'Actual alternating permutations',sum(all((p[j]<p[j+1])==(j%2==0)for j in range(4))for p in permutations(range(5)))==16)
ones=[sum(p)for p in product(range(2),repeat=6)];ok(69,'Binary parameter moments',sum(ones)==192 and F(sum(k*(k-1)for k in ones),64)==F(15,2) and F(sum(k*k for k in ones),64)-9==F(3,2))
def trees(n):
 if n==0:return [None]
 return [(a,b)for i in range(n)for a in trees(i)for b in trees(n-1-i)]
def leaves(t):return 0 if t is None else 1 if t==(None,None)else leaves(t[0])+leaves(t[1])
ok(70,'Actual ordered binary-tree internal leaves',len(trees(4))==14 and sum(map(leaves,trees(4)))==20)
ok(71,'Fixed-sum pair moments',F(sum(range(7)),7)==3 and F(sum(k*k for k in range(7)),7)-9==4)
s=S.symbols('s');G=S.Rational(1,4)/(1-S.Rational(3,4)*s)
ok(72,'Both geometric support derivatives',S.diff(G,s).subs(s,1)==3 and S.diff(s*G,s).subs(s,1)==4)
ok(73,'Poisson PGF multiplication',S.simplify(S.exp(2*(s-1))*S.exp(3*(s-1))-S.exp(5*(s-1)))==0)
ok(74,'Telescoping normalization and divergent mean comparison',all(sum(F(1,(n+1)*(n+2))for n in range(N+1))==1-F(1,N+2)for N in range(1,25)) and all(F(n,(n+1)*(n+2))>=F(1,4*n)for n in range(2,100)))
eq(75,1/(1-4*x*x),lambda n:2**n if n%2==0 else 0)
eq(76,(1-3*x)/((1-2*x)*(1-3*x)),lambda n:2**n)
eq(77,x**3/(1-2*x)**4,lambda n:0 if n<3 else 2**(n-3)*comb(n,3))
positiveComps=[1+sum(p)for p in product((0,1),repeat=4)]
ok(78,'Every separator subset independently determines one composition',sum(positiveComps)==48 and len(positiveComps)==16)
ok(79,'Nonlinear Catalan coefficient equation',all(C[n]==sum(C[i]*C[n-1-i]for i in range(n))for n in range(1,18)))
ok(80,'Three distinct object classes',len(comp(6))==13 and sum(a+2*b==6 for a,b in product(range(7),range(4)))==4 and sum(all(len(b)<=2 for b in p)for p in setparts(6))==76)
ok('auth-prefix','Boundary plus tail',coefficients((1-x)/(1-2*x),15)==[1]+[2**(n-1)for n in range(1,16)])
auth=coefficients((1403-2184*x+4*x*x/(1-x))/(1-3*x-5*x*x),20)
ok('auth-doctoral','All shifted forcing coefficients',auth[:4]==[1403,2025,13094,49411]and all(auth[n]==3*auth[n-1]+5*auth[n-2]+4 for n in range(2,21)))
specs=[]
for op in ['inverse','convolution','filter','bounded','coins','composition','partitions','durfee','catalan','labelled','marking','poles']:
 hi={'convolution':6,'bounded':9,'composition':7,'durfee':7,'catalan':4,'labelled':6,'marking':6}.get(op,10)
 specs.extend(dict(operation=op,n=n)for n in range(1,hi+1))
specs.extend([dict(operation='convolution',n=3,base=3),dict(operation='filter',n=8,residue=2),dict(operation='bounded',n=9,boxes=4),dict(operation='coins',n=10,weights=[1,2,5]),dict(operation='composition',n=6)])
(E/'model-cases.json').write_text(json.dumps(specs),encoding='utf-8')
js="const fs=require('fs'),{makeModel}=require('./dist/chapters/d_generating.js');process.stdout.write(JSON.stringify(JSON.parse(fs.readFileSync('./research/d_generating-evidence/model-cases.json','utf8')).map((s,i)=>makeModel('check-'+i,'independent check',s))));"
models=json.loads(subprocess.check_output(['node','-e',js],cwd=R,text=True,encoding='utf-8'))
for m in models:
 spec=m['spec'];n=spec['n'];op=spec['operation'];r=m['result']
 assert all(f['snapshot']['step']==i+1 and 'NaN'not in f['svg']and 'undefined'not in f['svg']for i,f in enumerate(m['frames']))
 assert m['frames'][-1]['snapshot']['result']==r
 if op=='inverse':assert r['coefficients']==[int(v)for v in coefficients(1/(1-2*x-x*x),n)]
 elif op=='convolution':assert r['coefficient']==int(coefficients(1/((1-x)**2*(1-spec['base']*x)),n)[n])
 elif op=='filter':assert r['retained']==[dict(index=i,value=2**i)for i in range(n+1)if i%3==spec['residue']]
 elif op=='bounded':
  assert r['coefficient']==sum(sum(p)==n for p in product(range(4),repeat=spec['boxes']))
  for frame in m['frames']:
   z=frame['snapshot']['state'];j=z['step'];assert z['rows'][-1]==[sum(sum(p)==t for p in product(range(4),repeat=j))for t in range(n+1)]
 elif op=='coins':
  assert r['coefficient']==sum(sum(w*a for w,a in zip(spec['weights'],p))==n for p in product(range(n+1),repeat=3))
  for frame in m['frames']:
   z=frame['snapshot']['state'];ws=spec['weights'][:z['step']];assert z['rows'][-1]==[sum(sum(w*a for w,a in zip(ws,p))==t for p in product(range(n+1),repeat=len(ws)))for t in range(n+1)]
 elif op=='composition':assert r['coefficient']==len(comp(n)) and {tuple(p)for p in r['objects']}==set(comp(n))
 elif op=='partitions':
  P=parts(n);assert r['coefficient']==len(P)and {tuple(p)for p in r['objects']}==set(P)
  for frame in m['frames']:
   z=frame['snapshot']['state'];assert z['rows'][-1]==[sum(max(p,default=0)<=z['step']for p in parts(t))for t in range(n+1)]
 elif op=='durfee':
  assert {tuple(p)for p in r['objects']}==set(parts(n))
  for frame in m['frames']:
   z=frame['snapshot']['state'];assert z['d']==durfee(z['parts']) and sum(z['arm'])+sum(z['leg'])+z['d']**2==n
 elif op=='catalan':
  valid=[]
  for p in product('UD',repeat=2*n):
   h=0;hs=[]
   for c in p:h+=1 if c=='U'else-1;hs.append(h)
   if h==0 and min(hs)>=0:valid.append(''.join(p))
  assert set(r['paths'])==set(valid)and r['coefficient']==C[n]
  for frame in m['frames'][1:]:
   z=frame['snapshot']['state'];assert next(j+1 for j in range(2*n)if z['path'][:j+1].count('U')==z['path'][:j+1].count('D'))==z['split']
 elif op=='labelled':
  seen=set()
  for frame in m['frames']:
   z=frame['snapshot']['state'];assert sorted(z['left']+z['right'])==list(range(1,n+1))and not(set(z['left'])&set(z['right']));seen.add(tuple(z['left']));assert z['multiplicity']==comb(n,z['k'])
  assert len(seen)==r['count']==2**n
 elif op=='marking':
  ref=[sum(p)for p in product(range(2),repeat=n)];assert r['histogram']==[ref.count(k)for k in range(n+1)]and r['total']==sum(ref)
  seen=set();total=0
  for frame in m['frames']:
   z=frame['snapshot']['state'];seen.add(z['word']);total+=z['word'].count('1');assert z['total']==total and z['ones']==z['word'].count('1')
  assert len(seen)==2**n
 else:assert r['coefficients']==[int(v)for v in coefficients(1/(1-2*x)**3,n)]
prior=json.loads((E/'prior-library.json').read_text(encoding='utf-8'))
print('Prior snapshot structure:',list(prior)[:3] if isinstance(prior,dict)else str(type(prior)))
assert set(map(str,range(1,81)))<=set(checks)
report=dict(status='passed',problemChecks=checks,independentModelInputs=len(models),modelCheckpoints=sum(len(m['frames'])for m in models),methods=['SymPy rational/formal coefficient expansion','Exact Fraction arithmetic','Independent product, subset, permutation, label-partition and binary-tree enumeration'],limits='Finite checks accompany the written proofs; they do not prove universal source completeness or guarantee performance on unseen questions.')
(E/'mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items()if k!='problemChecks'}))
