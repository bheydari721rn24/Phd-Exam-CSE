from pathlib import Path
from itertools import permutations,product,combinations_with_replacement
from fractions import Fraction as F
import json,subprocess,math,re,hashlib,sys
B=Path(__file__).resolve().parent;R=B.parent;E=B/'d_recurrence-evidence'
checks=[];count=0
def check(label,ok):
 assert ok,label
 checks.append(label)
def recurrence(coeff,bases,N=20,force=lambda n:0):
 a=list(map(F,bases));k=len(coeff)
 for n in range(k,N+1):a.append(sum(F(coeff[j])*a[n-j-1]for j in range(k))+force(n))
 return a
def verify_formula(label,coeff,bases,fn,force=lambda n:0):
 a=recurrence(coeff,bases,24,force);check(label,all(a[n]==fn(n)for n in range(len(a))))
verify_formula('Q17: distinct roots',[5,-6],[2,5],lambda n:2**n+3**n)
verify_formula('Q18: one-based boundary shift',[3,-2],[0,1],lambda n:2**n-1)
verify_formula('Q20: averaging with one-based observations',[F(1,2),F(1,2)],[100000,300000],lambda n:F(700000,3)-F(400000,3)*F(-1,2)**n)
verify_formula('Q25: double root',[4,-4],[1,6],lambda n:(1+2*n)*2**n)
verify_formula('Q26: triple root',[6,-12,8],[1,8,36],lambda n:(n+1)**2*2**n)
verify_formula('Q27: mixed repeated and simple modes',[5,-7,3],[4,12,32],lambda n:1+2*n+3**(n+1))
verify_formula('Q32: minimal-polynomial expanded coefficients',[8,-21,18],[1,5,22],lambda n:2**n+n*3**n)
verify_formula('Q33: constant double resonance',[2,-1],[0,1],lambda n:F(n*(n+1),2),lambda n:1)
verify_formula('Q34: exponential double resonance',[4,-4],[0,0],lambda n:F(n*(n-1),2)*2**n,lambda n:2**n)
verify_formula('Q35: polynomial simple resonance',[3,-2],[0,0],lambda n:3*2**n-3-F(n*n+5*n,2),lambda n:n)
verify_formula('Q36: polynomial-exponential forcing',[2],[0],lambda n:(3*n-6)*3**n+6*2**n,lambda n:n*3**n)
verify_formula('Q37: mixed forcing',[2],[0],lambda n:7*2**n+3**(n+1)-5*n-10,lambda n:3**n+5*n)
verify_formula('Q38: third-order rational amplitudes',[2,5,-6],[0,7,-3],lambda n:F(25+6*3**n-31*(-2)**n,15))
verify_formula('Q10: first-order resonance',[3],[4],lambda n:(4+2*n)*3**n,lambda n:2*3**n)
verify_formula('Q11: nonresonant formula',[2],[1],lambda n:F(5**(n+1)-2**(n+1),3),lambda n:5**n)
verify_formula('Q13: alternating particular',[ -1],[0],lambda n:F(n,2)+F(1-(-1)**n,4),lambda n:n)
verify_formula('Q67: double-pole coefficients',[6,-9],[1,6],lambda n:(n+1)*3**n)
verify_formula('Q68: generating forced coefficients',[2],[0],lambda n:3**(n+1)-3*2**n,lambda n:3**n)
verify_formula('Q48: weighted two-state scalar recurrence',[1,6],[1,1],lambda n:F(3**(n+1)+2*(-2)**n,5))
for t in [-3,-1,0,1,2,5]:
 a=recurrence([1+t,-t],[0,1]);check('Q78 parameter collision '+str(t),all(v==sum(t**j for j in range(n))for n,v in enumerate(a)))
check('Q3 backward boundary',7*2**7-3==893)
check('Q15 reset',6*3**8-1==39365)
check('Q16 periodic coefficients',all((F(9*6**m-4,5)*2+1)==F(18*6**m-3,5)for m in range(8)))
check('Q21 nearest-integer Binet inequality',1/math.sqrt(5)<.5)
check('Q31 infinitely many oscillatory zeros',all((3*n)%4==2 for n in range(2,50,4)))
specs=[]
for n in range(1,9):
 for op in['differences','boundary','tiling','resonance','automaton','derangements','partitions','matrix']:specs.append(dict(operation=op,n=n))
 for p in range(-4,5):
  for a0 in range(-10,11):specs.append(dict(operation='unrolling',n=n,p=p,a0=a0))
 for m in range(2,9):specs.append(dict(operation='modular',n=n,modulus=m))
 if n>=3:specs.append(dict(operation='ferrers',n=n))
 if n>=3:specs.append(dict(operation='conjugate',n=n))
 if n<=4:specs.append(dict(operation='catalan',n=n))
specs.append(dict(operation='reflection',n=6))
js="const {makeModel}=require('./dist/chapters/d_recurrence.js');const a="+json.dumps(specs)+";process.stdout.write(JSON.stringify(a.map((s,i)=>makeModel('check-'+i,'reference check',s))));"
p=E/'model-cases.json';p.write_text(json.dumps(specs),encoding='utf-8')
js="const fs=require('fs'),{makeModel}=require('./dist/chapters/d_recurrence.js');const a=JSON.parse(fs.readFileSync('./research/d_recurrence-evidence/model-cases.json','utf8'));process.stdout.write(JSON.stringify(a.map((s,i)=>makeModel('check-'+i,'reference check',s))));"
models=json.loads(subprocess.check_output(['node','-e',js],cwd=R,text=True,encoding='utf-8'))
bruteD={n:sum(all(i!=v for i,v in enumerate(p))for p in permutations(range(n)))for n in range(9)}
def blocks(n):
 counts=[0]*(n+1)
 def visit(word,k):
  if len(word)==n:counts[k]+=1;return
  for x in range(k+1):visit(word+[x],max(k,x+1))
 if n==0:return[1]
 visit([0],1);return counts
stirling={n:blocks(n)for n in range(9)}
for m in models:
 s=m['spec'];n=s['n'];r=m['result'];op=s['operation'];count+=1
 assert all(f['snapshot']['step']==i+1 for i,f in enumerate(m['frames']))
 assert m['frames'][-1]['snapshot']['result']==r
 assert all('undefined'not in f['svg']and 'NaN'not in f['svg']for f in m['frames'])
 if op=='unrolling':
  a=s['a0']
  for j in range(1,n+1):a=s['p']*a+j
  assert a==r['value']
 elif op=='differences':
  for j,row in enumerate(r['rows']):assert all(v==((i+1)**2 if j==0 else 2*i+3 if j==1 else 2 if j==2 else 0)for i,v in enumerate(row))
 elif op=='boundary':assert r['values']==[4,5]+[6*2**(i-2)for i in range(2,n+1)]if n>=2 else r['values']==[4,5]
 elif op=='tiling':
  a,b=1,1
  for j in range(2,n+1):a,b=b,a+b
  assert r['count']==b
  seen=set()
  for z in m['frames'][1:]:
   cells=[]
   for t in z['snapshot']['state']['tiles']:cells +=[(c,row)for c in range(t['c'],t['c']+t['w'])for row in range(t['row'],t['row']+t['h'])]
   assert len(cells)==2*n and len(set(cells))==2*n and set(cells)==set(product(range(n),range(2)))
   key=json.dumps(z['snapshot']['state']['tiles'],sort_keys=True);assert key not in seen;seen.add(key)
 elif op=='resonance':
  a=recurrence([4,-4],[0,0],n,lambda j:2**j);assert list(map(F,r['values']))==a
 elif op=='automaton':
  words=[x for x in product(range(3),repeat=n)if all(not(x[i]==x[i-1]and x[i]in[0,1])for i in range(1,n))];assert r['total']==len(words)and r['u']==sum(x[-1]==0 for x in words)and r['v']==sum(x[-1]==2 for x in words)
 elif op=='derangements':assert r['values']==[bruteD[j]for j in range(n+1)]
 elif op=='partitions':assert all(r['rows'][j][:j+1]==stirling[j]for j in range(n+1))and r['bell']==sum(stirling[n])
 elif op=='ferrers':
  t=[list(reversed(x))for x in combinations_with_replacement(range(1,n+1),3)if sum(x)==n];assert r['count']==len(t)and {tuple(x['snapshot']['state']['parts'])for x in m['frames']}=={tuple(x)for x in t}
 elif op=='catalan':
  assert r['count']==math.comb(2*n,n)//(n+1)
  for f in m['frames'][1:]:
   z=f['snapshot']['state'];path=z['path'];h=0;returns=[]
   for j,c in enumerate(path):h+=1 if c=='U'else-1;assert h>=0;returns +=[j+1]if h==0 else[]
   assert h==0 and returns[0]==z['split']
 elif op=='modular':
  a,b=0,1;seen={};states=[]
  while(a,b)not in seen:seen[(a,b)]=len(states);states.append((a,b));a,b=b,(a+b)%s['modulus']
  assert r['period']==len(states)and r['returnTo']==seen[(a,b)]==0 and r['residue']==states[n%len(states)][0]
 elif op=='conjugate':
  assert sum(r['original'])==sum(r['transposed'])==n
  assert [sum(x>i for x in r['transposed'])for i in range(max(r['transposed']))]==r['original']
 elif op=='reflection':
  assert r['original'].count('U')==r['original'].count('D')==6 and r['transformed'].count('U')==7 and r['transformed'].count('D')==5
 else:assert r['a']==2**n+3**n and r['b']==2**(n-1)+3**(n-1)
images=set();bad=0
for word in product('UD',repeat=12):
 if word.count('U')!=6:continue
 h=0;first=None
 for j,c in enumerate(word):
  h+=1 if c=='U'else-1
  if h<0 and first is None:first=j+1
 if first is None:continue
 bad+=1;image=tuple('D'if c=='U'else'U'for c in word[:first])+word[first:];assert image.count('U')==7 and image not in images;images.add(image)
check('Q62 full reflection bijection on all bad six-pair paths',bad==len(images)==math.comb(12,7)==792)
check('Q49 D8 independent permutation enumeration',bruteD[8]==14833)
check('Q52 and Q53 independent restricted-growth partition enumeration',stirling[6][3]==90 and stirling[7][3]==301)
check('Q54 B6 independent set partitions',sum(stirling[6])==203)
check('Q55 exact singleton partitions',5*(1+3)==20)
check('Q57 exact integer parts',len([x for x in combinations_with_replacement(range(1,8),3)if sum(x)==7])==4)
check('Q58 bounded parts',sum(x+2*y+3*z==6 for x,y,z in product(range(7),repeat=3))==7)
check('Q61 Q62 Q64 Catalan values',math.comb(10,5)//6==42 and math.comb(12,6)//7==132 and 16*14==224)
check('Q44 colored compositions',2**7+3*2**2==140)
check('Q75 inclusive modular interval',len([i for i in range(50,71)if i%3==0])==7)
check('Authentic doctoral parity interval',len([i for i in range(100,114)if i%3==0])==4)
check('Authentic prefix initial exception',all(sum([1]+[2**(j-1)for j in range(1,n+1)])==2**n for n in range(15)))
prior=json.loads((E/'prior-library.json').read_text());print(type(prior).__name__)
if isinstance(prior,dict):print(list(prior)[:8])
out=dict(status='passed',independentlyReferencedModelCases=count,checkedModelCheckpoints=sum(len(m['frames'])for m in models),formulaAndBoundaryChecks=checks,method='Python Fraction recurrences, direct products and word/permutation/set-partition/tiling enumerations independently compared with JavaScript models. General proofs manually reviewed in lesson and complete solutions.',limits='Finite cases do not replace proofs or guarantee unseen exam performance.')
(E/'mathematics.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items()if k not in['formulaAndBoundaryChecks']}))
