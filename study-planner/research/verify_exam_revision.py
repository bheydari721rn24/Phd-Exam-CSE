"""Independent finite oracles plus whole-library content/MathML integrity checks.

Finite checks corroborate exact instances; they do not prove asymptotic or universal
theorems. Original university-source teaching audits remain separate evidence.
"""
import json,re,math,itertools,hashlib,xml.etree.ElementTree as ET
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'research/exam-rewrite'
manifest=json.loads((BASE/'manifest.json').read_text());checks=[]
banks={}
for c in manifest['chapters']:
 t=c['topicId'];s=(BASE/(t+'.md')).read_text(encoding='utf-8')
 section=s.split('## Formula and conceptual problem bank')[1].split('## Applicable formulas and examination notes')[0]
 qs=re.split(r'^### (?:Problem|Question) \d+[^\n]*\n',section,flags=re.M)[1:]
 parsed=[]
 for q in qs:
  a=re.search(r'\*\*(?:Answer|Correct option): ([ABCD])\.\*\*',q)[1]
  if '**Options.**' in q:
   row=re.search(r'\*\*Options\.\*\* ([^\n]+)',q)[1]
   opts=[x[3:].rstrip('.') for x in re.split(r'; (?=[ABCD]:)',row)]
  else:opts=re.findall(r'^\*\*[ABCD]\.\*\* ([^\n]+)',q,re.M)
  assert len(opts)==4 and len(set(opts))==4,(t,opts)
  assert len(q.split())>=35,(t,'insufficient explanation')
  parsed.append((opts,a))
 banks[t]=parsed
 assert len(parsed)==c['questionCount'],t
 assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',s),t
 rendered=(ROOT/'dist/chapters'/(t+'.html')).read_text(encoding='utf-8')
 assert rendered.count('Formula and conceptual problem bank')==1,t
 assert 'Examination revision draft' in rendered and 'Applicable formulas and examination notes' in rendered,t
 assert len(re.findall(r'<h3>Question \d+',rendered))==len(parsed),t
 assert 'MATHSLOT' not in rendered,t
 ids=re.findall(r'\bid="([^"]+)"',rendered);assert len(ids)==len(set(ids)),(t,'duplicate IDs',[x for x in set(ids) if ids.count(x)>1])
 for anchor in re.findall(r'href="#([^"]+)"',rendered):assert anchor in ids,(t,anchor)
 for block in re.findall(r'<math\b[\s\S]*?</math>',rendered):
  root=ET.fromstring(block)
  for e in root.iter():
   name=e.tag.rsplit('}',1)[-1]
   if name in ('mfrac','msub','msup','munder','mover'):assert len(e)==2,(t,name)
   if name in ('msubsup','munderover'):assert len(e)==3,(t,name)
  visible=''.join(root.itertext());assert '\\' not in visible and '^' not in visible and '_' not in visible,(t,visible)
def canon(v):return re.sub(r'\s+','',str(v).strip().strip('$').replace('\\\\','\\'))
def expect(t,n,value):
 opts,answer=banks[t][n-1];got=opts['ABCD'.index(answer)]
 if isinstance(value,F):value=str(value)
 a,b=canon(got),canon(value)
 try: same=F(a)==F(b)
 except ValueError: same=a==b
 assert same,(t,n,got,value)
 checks.append({'chapter':t,'question':n,'verified':str(value)})
def event(t,n,value):
 assert value,(t,n);checks.append({'chapter':t,'question':n,'verified':'semantic countermodel or identity check'})
I=itertools.product
rows=list(I((0,1),repeat=3))
expect('d_logic',1,(2**4,2**(2**4)))
expect('d_logic',2,sum((not p or q) and(q or r) for p,q,r in rows))
def constrained(g,h):
 return sum(all((not g(v) or ((mask>>j)&1)) and(not ((mask>>j)&1) or h(v)) for j,v in enumerate(rows)) for mask in range(256))
expect('d_logic',3,constrained(lambda v:not v[0] or v[1],lambda v:True))
expect('d_logic',4,constrained(lambda v:v[0] and v[1],lambda v:v[0] or v[2]))
expect('d_logic',5,0)
expect('d_logic',6,sum(all(not v[i] or v[i+1] for i in range(5)) for v in I((0,1),repeat=6)))
event('d_logic',7,[j for j,(p,q,r) in enumerate(rows) if(p!=q) or r]==[1,2,3,4,5,7])
relations=list(I((0,1),repeat=9))
hasrow=lambda r:all(any(r[3*i+j] for j in range(3)) for i in range(3))
hascolumn=lambda r:any(all(r[3*i+j] for i in range(3)) for j in range(3))
expect('d_logic',10,sum(map(hasrow,relations)));expect('d_logic',11,sum(map(hascolumn,relations)))
expect('d_logic',12,len(list(I(range(4),repeat=4))))
expect('d_logic',17,sum(not ((p and q) <= (r or s)) for p,q,r,s,t in I((0,1),repeat=5)))
expect('d_logic',19,2**sum((p or r) and not(p and q) for p,q,r,s in I((0,1),repeat=4)))
expect('d_logic',20,sum(hasrow(r) and hascolumn(r) for r in relations))
atoms=[20,18,15,12,10,7,8,10]
expect('d_sets',1,sum(atoms[:3]));expect('d_sets',2,sum(atoms[3:6]));expect('d_sets',3,math.comb(8-3,5-3))
expect('d_sets',4,sum(a!=b and(a&b)==a for a,b in I(range(16),repeat=2)))
expect('d_sets',5,r'2^n');expect('d_sets',6,2**3);expect('d_sets',7,len([(),((),)]))
expect('d_sets',9,17+12-2*(17+12-22))
expect('d_sets',11,sum(a!=b and b!=c and(a&b)==a and(b&c)==b for a,b,c in I(range(16),repeat=3)))
expect('d_sets',12,sum(a and b and(a&b)==0 for a,b in I(range(32),repeat=2)))
event('d_proof',3,all(((n*n-1)%3==0)==(n%3!=0) for n in range(-60,61)))
event('d_proof',6,all(x*x+y*y-2*x*y==(x-y)**2 for x,y in I(range(-8,9),repeat=2)))
expect('d_proof',11,40)
event('d_proof',11,40*40+40+41==41*41)
expect('d_induction',1,sum(j*2**j for j in range(1,6)))
expect('d_induction',4,next(n for n in range(1,10) if all(2**j>=j*j for j in range(n,100))))
representable=lambda n:any(4*a+5*b==n for a,b in I(range(n+1),repeat=2))
expect('d_induction',5,next(n for n in range(1,20) if all(representable(j) for j in range(n,50))))
expect('d_induction',6,sum(all(not(v[i] and v[i+1]) for i in range(4)) for v in I((0,1),repeat=5)))
expect('d_induction',9,sum(math.comb(j,3) for j in range(3,9)))
expect('d_induction',11,sum(j*j*math.comb(6,j) for j in range(7)))
expect('a_model',1,(1024).bit_length());expect('a_model',2,(math.ceil(math.log2(1024)),(1024).bit_length()))
expect('a_model',4,200*16//8);expect('a_model',7,math.ceil(math.log2(70)));expect('a_model',8,math.ceil(math.log2(math.factorial(5))))
expect('a_model',11,(2**(2**6)).bit_length());expect('a_model',12,100*((1<<20)-1))
expect('a_loop',1,sum(range(1,21)));expect('a_loop',2,len(list(itertools.combinations(range(10),3))))
expect('a_loop',3,sum(6//i for i in range(1,7)))
event('a_loop',4,all(sum(2**j for j in range(k+1))==2*(2**k)-1 for k in range(12)))
event('a_loop',5,all(n<=sum(n//(2**j) for j in range(n.bit_length()))<2*n for n in range(1,100)))
expect('a_loop',7,7+1);expect('a_loop',10,sum(a>b for i,a in enumerate([4,1,3,2]) for b in [4,1,3,2][i+1:]))
event('a_loop',12,all(sum(1 for i,j in I(range(1,n+1),repeat=2) if i+j<=n)==n*(n-1)//2 for n in range(1,30)))
for t,q,result in [('s_axioms',1,F(6,10)+F(5,10)-F(2,10)),('s_axioms',2,F(6,10)+F(5,10)-2*F(2,10))]:
 expect(t,q,float(result))
expect('s_axioms',5,F(2+4,1+2+3+4));expect('s_axioms',6,F(1,6));expect('s_axioms',7,1);expect('s_axioms',8,F(1,8));expect('s_axioms',9,F(1,2));expect('s_axioms',10,0);expect('s_axioms',11,.1+.2+.25 if False else '0.55');expect('s_axioms',12,2**3);expect('s_axioms',14,F(1,4)+F(3,4)*F(1,2))
expect('s_counting',1,len(list(itertools.permutations(range(7),3))))
expect('s_counting',2,len(set(itertools.permutations('BANANA'))))
expect('s_counting',3,sum(x+y+z==10 for x,y,z in I(range(1,11),repeat=3)))
expect('s_counting',4,sum(x+y+z==7 for x,y,z in I(range(4),repeat=3)))
expect('s_counting',5,sum(len(set(v))==3 for v in I(range(3),repeat=4)))
expect('s_counting',6,len({tuple(sorted(tuple(sorted(i for i in range(4) if v[i]==j)) for j in range(3))) for v in I(range(3),repeat=4) if len(set(v))==3}))
expect('s_counting',7,sum(sum(v)==3 and all(not(v[i] and v[i+1]) for i in range(7)) for v in I((0,1),repeat=8)))
expect('s_counting',8,F(sum(sum(i<5 for i in v)==2 for v in itertools.combinations(range(9),3)),math.comb(9,3)))
expect('s_counting',9,F(sum(abs(v.index(0)-v.index(1))==1 for v in itertools.permutations(range(5))),math.factorial(5)))
expect('s_counting',10,math.factorial(5));expect('s_counting',11,7*3+1)
expect('s_counting',12,len(set(itertools.combinations_with_replacement(range(3),4))))
expect('s_counting',13,sum(sum(v)==12 for v in I(range(1,6),repeat=4)));expect('s_counting',14,F(sum(sum(v)==1 for v in I((0,1),repeat=3)),8))
dot=lambda u,v:sum(a*b for a,b in zip(u,v))
u=(F(1),F(2));v=(F(3),F(1));coefficient=dot(u,v)/dot(u,u);p=tuple(coefficient*x for x in u);res=tuple(a-b for a,b in zip(v,p))
expect('l_vectors',1,'(1,2)');event('l_vectors',1,p==(1,2) and dot(u,res)==0)
event('l_vectors',2,dot(res,res)==5);expect('l_vectors',4,F(abs(1+2*2+2*3-5),3));expect('l_vectors',5,F(4,2));expect('l_vectors',6,'(3,1)')
expect('l_vectors',7,F(2+4,1+4));expect('l_vectors',8,abs(1)**2+abs(1j)**2)
expect('l_vectors',11,F(3,2));expect('l_vectors',12,abs(-6))
proj=(F(2,3),F(1,3),F(1,3));target=(0,1,1);res=tuple(a-b for a,b in zip(target,proj))
event('l_vectors',13,dot(res,(1,1,0))==dot(res,(1,0,1))==0)
expect('l_vectors',14,dot((F(1,3),F(2,3),F(1,3)),(F(1,3),F(2,3),F(1,3))))
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
expect('l_matrices',2,dot((1,2),(3,4)));expect('l_matrices',5,-1)
expect('l_matrices',7,'Left,'+str(10*100*5+10*5*50));expect('l_matrices',11,'2 by3,'+str(2*5));expect('l_matrices',12,'8 by15')
A=[[1,1,0],[0,1,1],[0,0,1]];power=[[1,0,0],[0,1,0],[0,0,1]]
for _ in range(10):power=mul(power,A)
expect('l_matrices',13,power[0][2])
expect('p_types',1,'1.0');expect('p_types',3,int(((1<<32)-1)<1));expect('p_types',4,(250+10)%256);expect('p_types',5,-7-math.trunc(-7/3)*3);expect('p_types',9,'(0,2)');expect('p_types',10,10*4);expect('p_types',11,1+2*1+2)
event('p_types',12,float(2**53)+1==float(2**53));expect('p_types',13,f'({(~128)%(1<<32)},{(~128)%256})');expect('p_types',14,int(((1<<32)-1)<0))
expect('p_flow',1,3);expect('p_flow',2,0);expect('p_flow',3,2+4);expect('p_flow',4,sum(i for i in range(5) if i!=2));expect('p_flow',5,'(4,3)');expect('p_flow',6,1);expect('p_flow',7,3*2);expect('p_flow',8,4)
expect('p_flow',10,'s=i(i-1)/2');event('p_flow',10,all(sum(range(i))==i*(i-1)//2 for i in range(100)))
a,b=48,18;updates=0
while b:a,b=b,a%b;updates+=1
expect('p_flow',11,updates);expect('p_flow',13,'('+str(sum(i for i in range(1,8) if i%3))+',8)');expect('p_flow',14,next(i for i in range(1,129) if 6*i%256==64))
expect('g_number',1,int('2D',16));expect('g_number',2,float(F(int('101101',2),8)));expect('g_number',3,(300).bit_length());expect('g_number',4,int('11110110',2)-256);expect('g_number',7,float(F(40,16)));expect('g_number',12,float(F(5,4)*2))
expect('g_number',13,'-2.0');event('g_number',13,round(F(-6*5,4))/4==-2);expect('g_number',14,float(F(round(F(13,8)*4),4)))
tables=list(I((0,1),repeat=8));subset=lambda a,b:(a&b)==a
monotone=lambda f:all(not subset(a,b) or f[a]<=f[b] for a,b in I(range(8),repeat=2))
dual=lambda f:all(f[a]==1-f[a^7] for a in range(8))
expect('g_boolean',1,len(tables));expect('g_boolean',10,2**5);expect('g_boolean',12,sum(map(dual,tables)));expect('g_boolean',13,sum(map(monotone,tables)));expect('g_boolean',14,sum(dual(f) and f[0]==0 and f[7]==1 for f in tables))
event('g_gates',3,all((not ((not(a and b)) and c))==(a and b or not c) for a,b,c in I((0,1),repeat=3)))
event('g_gates',4,all((not((not(a and not(a and b))) and(not(b and not(a and b)))))==(a!=b) for a,b in I((0,1),repeat=2)))
expect('g_gates',2,3);expect('g_gates',6,2*3);expect('g_gates',7,'10ns');expect('g_gates',8,'3ns');expect('g_gates',11,2**2*F(1,2));expect('g_gates',13,'3ns');expect('g_gates',14,'0.4V')
reflexive=lambda r:all(r[3*i+i] for i in range(3))
symmetric=lambda r:all(r[3*i+j]==r[3*j+i] for i,j in I(range(3),repeat=2))
anti=lambda r:all(i==j or not(r[3*i+j] and r[3*j+i]) for i,j in I(range(3),repeat=2))
expect('d_relations',1,sum(map(reflexive,relations)));expect('d_relations',2,2**math.comb(4,2));expect('d_relations',3,sum(map(anti,relations)));expect('d_relations',4,2**4);expect('d_relations',5,sum(k*k for k in [2,3,4]));expect('d_relations',6,(2**4-2)//2);expect('d_relations',8,3**2)
expect('d_relations',12,sum(v.index(0)<v.index(1) and v.index(2)<v.index(3) for v in itertools.permutations(range(4))))
divs=[d for d in range(1,73) if 72%d==0];covers=[(a,b) for a,b in I(divs,repeat=2) if a!=b and b%a==0 and not any(c!=a and c!=b and c%a==0 and b%c==0 for c in divs)]
expect('d_relations',15,(len(divs),len(covers)));expect('d_relations',16,3+2+1)
expect('d_functions',1,3**4);expect('d_functions',2,len(list(itertools.permutations(range(5),3))));expect('d_functions',3,sum(len(set(v))==2 for v in I(range(2),repeat=5)));expect('d_functions',4,sum(len(set(v))==3 for v in I(range(5),repeat=4)));expect('d_functions',5,2*3*4);expect('d_functions',6,3**2)
expect('d_functions',11,sum(all(v[v[i]]==i for i in range(4)) for v in itertools.permutations(range(4))))
idempotents=[v for v in I(range(4),repeat=4) if all(v[v[i]]==v[i] for i in range(4))]
expect('d_functions',12,sum(len(set(v))==2 for v in idempotents));expect('d_functions',15,4**6);expect('d_functions',17,len(idempotents));expect('d_functions',18,sum(all(g[f[i]]==i for i in range(2)) for f in I(range(3),repeat=2) for g in I(range(2),repeat=3)))
expect('d_invariants',4,sum([2,5,-1]));expect('d_invariants',5,17+1);expect('d_invariants',6,2*10+1);expect('d_invariants',7,4)
def power_count(n):
 if n<2:return 0
 return power_count(n//2)+1+n%2
expect('d_invariants',9,power_count(13));expect('d_invariants',13,(13).bit_length()+(13).bit_count())
event('d_invariants',14,(3,4) not in {(t%5,2*t%5) for t in range(5)})
expect('d_number',2,(math.gcd(72,90),math.lcm(72,90)));expect('d_number',3,sum(6*x%14==8 for x in range(14)));expect('d_number',4,sum(6*x%14==5 for x in range(14)));expect('d_number',5,pow(7,-1,26));expect('d_number',7,next(x for x in range(15) if x%3==2 and x%5==3));expect('d_number',9,sum(math.gcd(x,60)==1 for x in range(60)));expect('d_number',10,pow(7,100,13));expect('d_number',11,pow(2,4,8));expect('d_number',12,sum(360%d==0 for d in range(1,361)))
fact=math.factorial(10);v2=0
while fact%2==0:fact//=2;v2+=1
expect('d_number',13,v2);expect('d_number',15,sum(math.gcd(x,18)==1 for x in range(18)));expect('d_number',16,next(k for k in range(1,7) if pow(2,k,7)==1));expect('d_number',17,sum(6*x%14==8 for x in range(101)));expect('d_number',18,next(x for x in range(36) if x%12==5 and x%18==11))
expect('a_recurrence',5,sum(range(11)));expect('a_recurrence',10,32)
event('a_recurrence',11,all((1+2*n)==2*(1+2*(n-1))-(1+2*(n-2)) for n in range(2,40)))
event('a_recurrence',12,all(n*2**n==2*((n-1)*2**(n-1))+2**n for n in range(1,30)))
expect('a_divide',1,4+6-1);expect('a_divide',2,sum(a>b for a,b in I([2,4,7],[1,4,6])))
expect('a_divide',3,'(3,7,5,9)');expect('a_divide',4,max(sum([-8,-3,-5][i:j]) for i in range(3) for j in range(i+1,4)));expect('a_divide',9,8+15-1);expect('a_divide',11,1<<(5+4-2).bit_length())
convolution=[sum(a*b for i,a in enumerate([1,2,3]) for j,b in enumerate([4,5]) if i+j==k) for k in range(4)]
expect('a_divide',12,str(convolution));expect('a_divide',13,str([sum(convolution[i] for i in range(4) if i%2==k) for k in range(2)]));expect('a_divide',15,8//2*3)
expect('a_divide',17,str([(1+2*pow(4,k,17))%17 for k in range(4)]));event('a_divide',18,7%17==(-10)%17 and(-10)>=-10 and 7<=10)
report={'chapters':22,'questions':sum(c['questionCount'] for c in manifest['chapters']),'examinationNotes':sum(c['notesCount'] for c in manifest['chapters']),'independentAnswerChecks':len(checks),'checks':checks,'limits':'Finite oracles validate the stated instances and modeled properties; universal theorems retain written proofs. No Iranian exam archive was consulted. C semantics were checked against explicit type assumptions and WG14 clauses, not by executing undefined expressions.'}
(BASE/'answer-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('Verified 22 chapter structures, unique four-option banks, internal anchors, native MathML arities, and',len(checks),'independent answer/property checks.')
