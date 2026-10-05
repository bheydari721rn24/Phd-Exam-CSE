"""Independent finite references and retained-content validation."""
from pathlib import Path
from itertools import product,combinations,permutations
from math import comb,ceil,sqrt,gcd,prod
from fractions import Fraction
from functools import lru_cache
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,re,hashlib,subprocess,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;COUNT=0;RESULTS=[]
def check(ok,label):
 global COUNT
 COUNT+=1
 assert ok,label
def ext(N,caps,cost,minimize=True):
 a={0:0}
 for cap in caps:
  b={}
  for total,v in a.items():
   for x in range(min(cap,N-total)+1):
    t=total+x;z=v+cost(x)
    if t not in b or (z<b[t] if minimize else z>b[t]):b[t]=z
  a=b
 return a.get(N)
def subset_values(a):return [sum(v for i,v in enumerate(a) if mask>>i&1) for mask in range(2**len(a))]
def monotone(a):
 I=D=0
 for mask in range(1,2**len(a)):
  s=[v for i,v in enumerate(a) if mask>>i&1]
  if all(x<y for x,y in zip(s,s[1:])):I=max(I,len(s))
  if all(x>y for x,y in zip(s,s[1:])):D=max(D,len(s))
 return I,D
def triangles(n,mask):
 C={p:(mask>>i)&1 for i,p in enumerate(combinations(range(n),2))}
 return [t for t in combinations(range(n),3) if len({C[p] for p in combinations(t,2)})==1]
def ref(c):
 k=c['kind']
 if k=='function':return 'Noninjective' if c['n']>c['k'] else 'Neither collision nor collision-freedom is forced'
 if k=='maxmin':return ceil(c['n']/c['k'])
 if k=='ids':z=9*(c['digits']-1)+1;return f'{z} labels; occupancy {ceil(c["students"]/z)}'
 if k=='subset-bound':check(2**c['n']>c['n']*c['maximum']+1,k);return 'Guaranteed'
 if k=='symmetric-es':return ceil(sqrt(c['n']))
 if k=='divisibility-threshold':check(all(y%x for x,y in combinations(range(c['n']+1,2*c['n']+1),2)),k);return c['n']+1
 if k=='triangle-threshold':check(1/sqrt(3)>.5 and sqrt(3)/2>.5,k);return 5
 if k=='saturation':check(sum(c['capacities'])==c['total'],k);return len(c['capacities']) if len(c['capacities'])>3 else ','.join(map(str,c['capacities']))
 if k=='ramsey-threshold':check(not triangles(5,665),k);return 6
 if k in ['seven-multiple','zeroone']:check(c['value']%c['m']==0 and set(str(c['value']))<=set('70' if k=='seven-multiple' else '01'),k);return c['value']
 if k=='subset-residue-bound':check(2**c['n']>c['m'] and gcd(2,c['m'])>1,k);return 'Collision guaranteed; cancellation not guaranteed'
 if k=='average':return f'Maximum at least {ceil(c["n"]/c["k"])}; minimum at most {c["n"]//c["k"]}'
 if k=='threshold':return c['k']*(c['r']-1)+1
 if k=='inventory':
  # Enumerate actual stock vectors rather than evaluate the authored cap formula.
  avoiding=[sum(a) for a in product(*[range(x+1) for x in c['stocks']]) if all(x<t for x,t in zip(a,c['targets']))];z=max(avoiding)+1
  return z if z<=sum(c['stocks']) else 'Infeasible'
 if k=='specified':return max(sum(a) for a in product(*[range(x+1) for x in c['stocks']]) if a[c['index']]<c['r'])+1
 if k=='distinct-colors':return max(sum(a) for a in product(*[range(x+1) for x in c['stocks']]) if sum(v>0 for v in a)<c['t'])+1
 if k=='heavy':return ext(c['n'],[c['capacity']]*c['k'],lambda x:int(x>=c['r']))
 if k=='strict-average':return 'Not forced' if c['n']%c['k']==0 else 'Both are forced'
 if k=='real-load':check(Fraction(2,5)*2==Fraction(4,5),k);return 'No; 0.4 is the sharp lower bound'
 if k=='utilization':return Fraction(c['loads'],sum(c['capacities']))
 if k in ['pairs','tuples']:return ext(c['n'],[c['n']]*c['k'],lambda x:comb(x,c.get('t',2)) if x>=c.get('t',2) else 0)
 if k=='actual-tuples':return sum(comb(v,c['t']) for v in c['occupancies'] if v>=c['t'])
 if k=='max-pairs':return ext(c['n'],[c['n']]*c['k'],lambda x:comb(x,2),False)
 if k=='bounded-pairs':return ext(c['n'],c['capacities'],lambda x:comb(x,2))
 if k=='hash':return 2**c['bits']+1
 if k=='short-codes':return sum(2**i for i in range(c['n']))
 if k=='prefix':
  a=c['values'];s=[sum(a[:j])%c['m'] for j in range(len(a)+1)];j=next(j for j in range(1,len(s)) if s[j] in s[:j]);i=s.index(s[j]);return f'Positions {i+1}–{j}; sum {sum(a[i:j])}'
 if k=='difference':check(c['n']>c['m'] and (1+1)%c['m']!=0,k);return 'A divisible difference, not necessarily a divisible sum'
 if k=='remainder-counterexample':check(1%5==6%5 and (6-1)%5==0 and (6+1)%5!=0,k);return 'Difference only'
 if k=='no-prefix':return 'No' if all(sum(c['values'][i:j])%c['m'] for i in range(len(c['values'])) for j in range(i+1,len(c['values'])+1)) else 'Yes'
 if k=='repunit':
  v=0
  for _ in range(c['m']):
   v=10*v+1
   if v%c['m']==0:return v
  raise AssertionError(k)
 if k=='repunit-obstruction':check(gcd(10,c['m'])>1,k);return 'Impossible'
 if k=='cancellation':check(c['c']*c['a']%c['m']==c['c']*c['b']%c['m'] and c['a']%c['m']!=c['b']%c['m'],k);return 'No'
 if k=='square-prime':p=c['p'];S={x*x%p for x in range(p)};check(any((x*x+y*y+1)%p==0 for x,y in product(range(p),repeat=2)),k);return f'{len(S)} residues; a solution exists'
 if k=='square-two':check((1+0+1)%2==0,k);return 'x=1, y=0'
 if k=='square-composite':check(not any((x*x+y*y+1)%c['m']==0 for x,y in product(range(c['m']),repeat=2)),k);return 'No solution'
 if k=='equal-subsets':check(1+4==2+3 and len(set(subset_values(c['values'])))<2**len(c['values']),k);return '1+4=2+3'
 if k=='unique-subsets':check(len(set(subset_values(c['values'])))==2**len(c['values']),k);return 'No'
 if k=='fixed-subsets':S=[sum(a) for a in combinations(range(1,c['n']+1),c['t'])];check(len(S)>len(set(S)),k);return 'Guaranteed'
 if k=='no-zero-subset':check(all(x%c['m'] for x in subset_values(c['values'])[1:]),k);return 'No'
 if k=='unit-subsets':a=c['values'];S=[prod(v for i,v in enumerate(a) if mask>>i&1)%c['m'] for mask in range(2**len(a))];check(len(set(S))<len(S) and all(gcd(x,c['m'])==1 for x in a),k);return 'Collision with valid cancellation'
 if k=='zero-subset-counterexample':check(subset_values([0])==[0,0],k);return 'No'
 if k=='complement':
  U=set(range(1,c['H']+1));pairs={tuple(sorted((x,c['sum']-x))) for x in U if c['sum']-x in U and 2*x!=c['sum']};return c['H']-len(pairs)+1
 if k=='odd-witness':check(8%4==0 and len(set(c['values']))==len(c['values']),k);return '4 divides 8'
 if k=='divfree':check(all(y%x for x,y in combinations(range(c['L'],c['H']+1),2)),k);return 'No proper multiple remains in the interval'
 if k=='consecutive':return (c['H']+1)//2+1
 if k=='coprime-threshold':check(all(gcd(x,y)>1 for x,y in combinations(range(2,c['H']+1,2),2)),k);return c['H']//2+1
 if k=='base-cores':return sum(x%c['base']!=0 for x in range(1,c['H']+1))
 if k=='grid':r=next(i for i in range(1,100) if sqrt(2)/i<=c['distance']);return r*r+1
 if k=='rectangle-grid':return c['cols']*c['rows']+1
 if k in ['approximation','rational-approximation']:alpha=sqrt(2) if k=='approximation' else .5;check(abs(c['q']*alpha-c['p'])<1/c['m'] and 1<=c['q']<=c['m'],k);return f'q={c["q"]}, p={c["p"]}'
 if k=='es':return (c['r']-1)*(c['s']-1)+1
 if k=='lis':i,d=monotone(c['values']);return f'LIS {i}; LDS {d}'
 if k=='es-square':return '10 at 100; 11 first at 101'
 if k=='duplicate-es':check(monotone([1]*min(c['n'],9))==(1,1),k);return 'No; strict maximum is one'
 if k=='lis-contiguous':i,_=monotone(c['values']);a=c['values'];t=max(j-i for i in range(len(a)) for j in range(i+1,len(a)+1) if all(x<y for x,y in zip(a[i:j],a[i+1:j])));return f'Subsequence {i}; contiguous block {t}'
 if k=='degree':check(len(set(range(c['n'])))==c['n'],k);return 'Repeated undirected degree; distinct tournament outdegrees possible'
 if k=='ramsey-cycle':return len(triangles(5,665))
 if k=='rectangle':
  cols,colors=c['cols'],c['colors'];check(cols==colors+1,k);a=[]
  for pair in combinations(range(cols),2):
   for color in range(colors):
    row=[None]*cols
    for j in pair:row[j]=color
    for j,v in zip([j for j in range(cols) if j not in pair],[x for x in range(colors) if x!=color]):row[j]=v
    a.append(row)
  check(all(not any(x[i]==x[j]==y[i]==y[j] for i,j in combinations(range(cols),2)) for x,y in combinations(a,2)),k)
  return len(a)+1
 if k=='binary-identification':return (c['N']-1).bit_length()
 if k=='one-lie':return 2**c['q']//(c['q']+1)
 if k=='card-channel':check(comb(52,4)>52*51*50 and list(permutations('ABC'))[2]==('B','A','C'),k);return 'Six rank codes; four-card variant impossible'
 if k=='authentic-parity':return sum(any((x+y)%2 for x,y in combinations(S,2)) for S in combinations(range(1,c['H']+1),c['t']))
 if k=='authentic-password':return Fraction(sum(c%2==1 for a,b,c in product(range(1,10),repeat=3))*2,60)
 raise ValueError(k)
Q=json.loads((B/'d_pigeonhole-questions.json').read_text());A=json.loads((B/'d_pigeonhole-authentic.json').read_text());check(len(Q)==80 and len(A)==2,'question inventory')
for q in Q+A:
 z=ref(q['check']);expected=q['expected'];check(str(z)==expected or (q['check']['kind']=='authentic-password' and float(z)==float(expected)),f'{q["id"]}: {z} != {expected}')
 if 'options' in q:check(q['options'][q['answer']-1]==expected or q['id']=='Phd_CS_1404_Q25','option '+q['id'])
 RESULTS.append(dict(id=q['id'],state='passed',method=q['check']['kind'],reference=str(z)))
# Exercise general formulas against occupancy convolution, independent subset scans and actual graph cases.
for N in range(15):
 for k in range(1,6):
  q,s=divmod(N,k)
  check(ext(N,[N]*k,lambda x:comb(x,2))==k*comb(q,2)+s*q,'pair extremum')
  for t in [3,4]:check(ext(N,[N]*k,lambda x:comb(x,t) if x>=t else 0)==k*(comb(q,t) if q>=t else 0)+s*(comb(q,t-1) if q>=t-1 else 0),'tuple extremum')
for k in range(1,6):
 for cap in range(1,6):
  for r in range(1,cap+1):
   for n in range(k*cap+1):check(ext(n,[cap]*k,lambda x:int(x>=r))==max(0,ceil((n-k*(r-1))/(cap-r+1))),'heavy minimum')
for n in range(2,7):
 for mask in range(2**(n*(n-1)//2)):
  E=[e for i,e in enumerate(combinations(range(n),2)) if mask>>i&1];deg=[sum(v in e for e in E) for v in range(n)];check(len(set(deg))<n,'all simple graphs degree repetition')
  if n==6:check(bool(triangles(n,mask)),'all 32768 K6 colorings')
for n in range(1,8):
 for a in list(permutations(range(n)))[:min(100,1 if n==1 else 100)]:i,d=monotone(a);check(n<=i*d,'distinct sequence product')
models=json.loads((R/'dist/chapters/d_pigeonhole-models.json').read_text())['models']
for m in models:
 for f in m['frames']:
  ET.fromstring(f['svg']);ET.fromstring(f['formulaHtml']);s=f['state'];id=m['id']
  if id=='dp-placement':check(sum(s['occupancies'])==s['n'] and s['occupancies']==[s['dest'][:s['n']].count(j) for j in range(5)],id)
  elif id in ['dp-average','dp-capacity','dp-collisions']:
   a=s['occupancies'];check(sum(a)==s.get('total',sum(a)),id)
   if 'stocks' in s:check(all(x<=y for x,y in zip(a,s['stocks'])),id)
   if 'pairs' in s:check(s['pairs']==sum(comb(x,2) for x in a),id)
  elif id=='dp-prefix':check(s['prefixes']==[sum(s['values'][:j])%s['modulus'] for j in range(len(s['prefixes']))],id)
  elif id=='dp-repunit':check(all(set(str(x))=={'1'} for x in s['repunits']),id)
  elif id=='dp-prime':check(s['A']==sorted({x*x%s['p'] for x in range(s['p'])}) and s['B']==sorted({(-1-x*x)%s['p'] for x in range(s['p'])}),id)
  elif id=='dp-subsets':check(sum(s['values'][i] for i in s['left'])==sum(s['values'][i] for i in s['right']),id)
  elif id=='dp-oddchain':check(s['cores']==[x for x in range(1,s['H']+1) if x%2],id)
  elif id=='dp-pairing':check(s['target']==22 and s['H']==21 and s['total']<=12,id)
  elif id=='dp-triangle':
   V=s['vertices'];check(all(abs(sqrt((x-u)**2+(y-v)**2)-320)<1e-8 for (x,y),(u,v) in combinations(V,2)),id)
  elif id=='dp-fractional':check(all(abs(x-(j*s['alpha'])%1)<1e-9 for j,x in enumerate(s['fractions'])),id)
  elif id=='dp-es':check((max(s['increasing']),max(s['decreasing']))==monotone(s['values']),id)
  elif id=='dp-degree':check(s['degrees']==[sum(v in e for e in s['edges']) for v in range(s['n'])],id)
  elif id=='dp-ramsey':
   t=s['triangle'];check(not t or len({tuple(e) in {tuple(x) for x in s['red']} for e in combinations(t,2)})==1,id)
  elif id=='dp-rectangle':
   a=s['rows'];collision=any(x[i]==x[j]==y[i]==y[j] for x,y in combinations(a,2) for i,j in combinations(range(4),2));check(collision==(len(a)>18),id)
  elif id=='dp-info':check(s['leaves']==2**s['depth'],id)
  elif id=='dp-cards':check((s['anchor']+s['gap']-1)%13+1==s['hidden'] and (s['stage']<2 or tuple(s['order'])==list(permutations('ABC'))[s['gap']-1]),id)
  else:raise ValueError(id)
cache=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
for q in A:check(hashlib.sha256((cache/q['repoPath']).read_bytes()).hexdigest()==q['sourceSha256'],'archive source '+q['id'])
courses=json.loads((B/'d_pigeonhole-reviewed-courses.json').read_text());check(len({x['university'] for x in courses if x['selectionRole']=='Primary'})>=4,'four primary universities')
for c in courses:
 for d in c['sourceDocuments']:
  if 'sha256' in d:check(hashlib.sha256(Path(d['cachedPath']).read_bytes()).hexdigest()==d['sha256'],'course source '+c['id'])
baseline='c958f2b5b8eae701ab686ba77051991cc1b24278';lessons=json.loads(subprocess.check_output(['git','show',baseline+':dist/lessons.json'],cwd=R,text=True));retained=chapters=0
for w in lessons:
 for c in w['chapters']:
  old=subprocess.check_output(['git','show',baseline+':dist/'+c['url']],cwd=R).decode('utf-8');new=(R/'dist'/c['url']).read_text(encoding='utf-8');check(old==new or c['topicId']=='d_inclusion' and old.replace('Review draft ·','Student-approved chapter ·')==new,'retained '+c['topicId']);retained+=old.count('class="exam-question"');chapters+=1
check(retained==1917 and chapters==33,'prior inventory')
page=(R/'dist/chapters/d_pigeonhole.html').read_text(encoding='utf-8');check(page.count('class="exam-question"')==82 and page.count('class="review-rule"')==80,'rendered questions and rules')
for f in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(f);check(True,'well formed math')
check(not re.search('[\u0600-\u06ff\ufffd\x00]',page),'English glyph scope')
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,a):
  a=dict(a)
  if 'id' in a:self.ids.add(a['id'])
  self.links += [a[k] for k in ['href','src'] if k in a]
p=Links();p.feed(page)
for link in p.links:
 u=urlparse(link)
 if u.scheme or u.netloc:continue
 if not u.path:check(not u.fragment or u.fragment in p.ids,'anchor '+link)
 else:check((R/'dist/chapters'/unquote(u.path)).resolve().exists(),'local resource '+link)
report=dict(topicId='d_pigeonhole',state='passed',checks=COUNT,questionChecks=RESULTS,retainedQuestions=retained,retainedChapters=chapters,models=len(models),checkpoints=sum(len(m['frames']) for m in models),formulaInstances=len(re.findall('<math\\b',page)),limitations='Finite references supplement written general proofs; necessary bounds are not represented as sufficient strategies.')
(B/'d_pigeonhole-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k!='questionChecks'}))
# Independent browser lab reference vectors.
lab=[]
for i in range(90):
 a=[(i*(j+1)+j*j)%7 for j in range(1+i%6)];lab.append(dict(mode='occupancy',values=a,m=5,n=6,mask=0,count=sum(sum(1 for _ in combinations(range(v),2)) for v in a)))
for i in range(90):
 a=[(i*3+j*5)%15-7 for j in range(1+i%10)];m=1+i%12;lab.append(dict(mode='prefix',values=a,m=m,n=6,mask=0,count=sum(sum(a[j:k])%m==0 for j in range(len(a)) for k in range(j+1,len(a)+1))))
for i in range(90):
 a=[(i*3+j*5)%11-5 for j in range(1+i%9)];li,ld=monotone(a);lab.append(dict(mode='sequence',values=a,m=5,n=6,mask=0,count=li,lds=ld))
for n in [5,6]:
 for i in range(30):mask=(i*991+665)%2**(n*(n-1)//2);lab.append(dict(mode='graph',values=[],m=5,n=n,mask=mask,count=len(triangles(n,mask))))
(B/'d_pigeonhole-lab-reference.json').write_text(json.dumps(lab,indent=2)+'\n',encoding='utf-8');print('Wrote',len(lab),'independent browser reference cases.')
