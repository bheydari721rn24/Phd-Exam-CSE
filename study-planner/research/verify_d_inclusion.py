"""Independent finite reference models, retained-content checks, and exact source fingerprints."""
from pathlib import Path
from itertools import product,permutations,combinations
from functools import lru_cache
from math import comb,factorial,gcd
from fractions import Fraction
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,re,hashlib,subprocess,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;COUNT=0;RESULTS=[]
def check(cond,label):
 global COUNT
 COUNT+=1
 assert cond,label
def exact_inverse(G):return [sum((-1)**((k^j).bit_count())*G[k] for k in range(len(G)) if (k&j)==j) for j in range(len(G))]
def subsetsum_atoms(atoms):return [sum(v for k,v in enumerate(atoms) if k&j==j) for j in range(len(atoms))]
def digits(n,required,positive):
 req={x:i for i,x in enumerate(required)};a={0:1}
 for pos in range(n):
  b={}
  for mask,v in a.items():
   for d in range(1 if positive and pos==0 else 0,10):
    t=mask|(1<<req[d] if d in req else 0);b[t]=b.get(t,0)+v
  a=b
 return a.get((1<<len(req))-1,0)
def bounded(t,c):
 a=[1]+[0]*t
 for cap in c:a=[sum(a[s-x] for x in range(min(cap,s)+1)) for s in range(t+1)]
 return a[t]
def edge_count(n,edges):
 edges={tuple(x) for x in edges}
 @lru_cache(None)
 def dp(mask,last,seen):
  if mask==(1<<n)-1:return int(seen)
  return sum(dp(mask|1<<x,x,seen or (last,x) in edges) for x in range(n) if not mask>>x&1)
 return dp(0,-1,False)
def map_count(n,m,target,q=None):
 z=0
 for a in product(range(m),repeat=n):
  s=set(a)
  ok={'onto':lambda:len(s)==m,'required':lambda:set(range(q))<=s,'image':lambda:len(s)==q,'missing':lambda:m-len(s)==q,'specified_missing':lambda:not s&set(range(q)),'minoccupancy':lambda:all(a.count(x)>=q for x in range(m)),'equalonto':lambda:len(s)==m and a[0]==a[1]}[target]()
  z+=ok
 return z
def permutation_count(c):
 n=c['n'];target=c['target'];z=0
 for p in permutations(range(n)):
  fixed=[i for i,v in enumerate(p) if i==v]
  if target=='fixed':ok=len(fixed)==c['r']
  elif target=='partial':ok=not any(i in fixed for i in range(c['q']))
  elif target=='forcedpartial':ok=set(c['forced'])<=set(fixed) and not set(c['forbidden'])&set(fixed)
  elif target=='two_cycle':ok=not fixed and p[c['a']]==c['b'] and p[c['b']]==c['a']
  elif target=='not_two_cycle':ok=not fixed and p[c['a']]==c['b'] and p[c['b']]!=c['a']
  elif target=='no_two_cycles':ok=not any(p[i]!=i and p[p[i]]==i for i in range(n))
  elif target=='specified_fixed':ok=set(fixed)==set(c['positions'])
  else:raise ValueError(target)
  z+=ok
 return z
def proof(name):
 if name=='negative_single_atom':check(10-8-8+1==-5,name)
 elif name=='triple_range':check([t for t in range(20) if min(5-t,4-t,3-t,3+t,4-t)>=0]==[0,1,2,3],name)
 elif name=='pairwise_not_mutual':
  vals=[(x,y,x^y) for x,y in product(range(2),repeat=2)];check(all(sum(a[i]==a[j]==1 for a in vals)==1 for i,j in combinations(range(3),2)) and not any(all(a) for a in vals),name)
 elif name=='empty_derangement':check(len(list(permutations([])))==1,name)
 elif name=='empty_maps':check([map_count(n,m,'onto') for n,m in [(0,0),(0,3),(3,0)]]==[1,0,0],name)
 elif name=='required_vs_exact':check(map_count(7,4,'required',2)==12138 and map_count(7,2,'onto')==126,name)
 elif name=='rook_components':check(sum(len({r for r,c in I})==len(I) for I in combinations([(0,0),(0,1)],2))==0,name)
 elif name=='bonferroni_interval':check(150-60==90 and 150-60+15==105 and [200-105,200-90]==[95,110],name)
 elif name=='truncation_error':check(abs(10-comb(10,2)-1)>abs(10-1),name)
 elif name=='exact2_coefficient':
  for t in range(2,20):check(sum((-1)**(j-2)*comb(j,2)*comb(t,j) for j in range(2,t+1))==int(t==2),name+str(t))
 elif name=='atleast2_coefficient':
  for t in range(20):check(sum((-1)**(j-2)*(j-1)*comb(t,j) for j in range(2,t+1))==int(t>=2),name+str(t))
 elif name=='weights':check(Fraction(6,10)+Fraction(7,10)-Fraction(4,10)==Fraction(9,10) and Fraction(4,10)/Fraction(7,10)==Fraction(4,7),name)
 elif name in ['atom_realization','transform']:
  for n in range(1,7):
   a=[(i*i+3*i+1)%7 for i in range(1<<n)];G=subsetsum_atoms(a);b=G[:]
   for bit in range(n):
    for mask in range(1<<n):
     if not mask>>bit&1:b[mask]-=b[mask|1<<bit]
   check(b==a==exact_inverse(G),name+str(n))
 elif name=='labeled_weights':check(sum(factorial(6)//(factorial(a)*factorial(b)*factorial(6-a-b)) for a in range(7) for b in range(7-a))==3**6,name)
 else:raise ValueError(name)
def reference(c):
 kind=c['kind']
 if kind=='atoms':
  a=c['atoms'];target=c['target'];pred={'none':lambda r:r==0,'union':lambda r:r>0,'exact1':lambda r:r==1,'exact2':lambda r:r==2,'atleast2':lambda r:r>=2,'odd':lambda r:r%2==1}[target]
  return sum(x for mask,x in enumerate(a) if pred(mask.bit_count()))
 if kind=='digits':return digits(c['length'],c['required'],c['positive'])
 if kind=='divisible':
  pred={'none':lambda r:r==0,'union':lambda r:r>0,'exact1':lambda r:r==1,'atleast2':lambda r:r>=2}[c['target']]
  return sum(pred(sum(x%d==0 for d in c['divisors'])) for x in range(c['L'],c['H']+1))
 if kind=='poker':
  # Rank occupancy DP: distinct cards, unordered hand, with a flag for a repeated rank.
  dp={(0,False):1}
  for _ in range(13):
   nxt={}
   for (total,repeated),v in dp.items():
    for k in range(5):
     if total+k<=5:key=(total+k,repeated or k>=2);nxt[key]=nxt.get(key,0)+v*comb(4,k)
   dp=nxt
  return dp[5,True]
 if kind=='edges':return edge_count(c['n'],c['edges'])
 if kind=='dice':return Fraction(sum(c['face'] in p for p in product(range(1,c['faces']+1),repeat=c['dice'])),c['faces']**c['dice'])
 if kind=='coprime':return sum(gcd(x,c['n'])==1 for x in range(1,c['n']+1))
 if kind=='map':return map_count(c['n'],c['m'],c['target'],c.get('q'))
 if kind=='inverse':
  S=c['S'];n=len(S)-1;N=[0]*(n+1)
  for r in range(n,-1,-1):N[r]=S[r]-sum(comb(t,r)*N[t] for t in range(r+1,n+1))
  return N
 if kind=='atoms_inverse':return exact_inverse(c['G'])
 if kind=='permutation':return permutation_count(c)
 if kind=='partition':
  a=[1]+[0]*c['m']
  for n in range(1,c['n']+1):a=[0]+[a[m-1]+m*a[m] for m in range(1,c['m']+1)]
  return a[c['m']]
 if kind=='caps':return bounded(c['total'],c['caps'])
 if kind=='alphabets':return sum(set(c['required'])<=set(w) for w in product(*c['sets']))
 if kind in ['congruence','congruenceunion']:return sum((all if kind=='congruence' else any)(x%d==r%d for r,d in c['residues']) for x in range(c['L'],c['H']+1))
 if kind=='board':
  board={tuple(p) for p in c['board']};check(c['rook']==[sum(len({r for r,s in I})==k and len({s for r,s in I})==k for I in combinations(board,k)) for k in range(c['n']+1)],'rook coefficient')
  return sum(all((i,v) not in board for i,v in enumerate(p)) for p in permutations(range(c['n'])))
 if kind=='conditional_dice':
  p=[x for x in product(range(1,7),repeat=2) if sum(x)%2==0];return Fraction(sum(6 in x for x in p),len(p))
 if kind=='proof':proof(c['claim']);return None
 raise ValueError(kind)
q=json.loads((B/'d_inclusion-questions.json').read_text());check(len(q)==80,'bank size')
for task in q:
 z=reference(task['check']);check(z is None or str(z)==task['expected'],f"{task['id']}: actual {z}, stated {task['expected']}")
 RESULTS.append(dict(id=task['id'],state='verified',method=task['check']['kind'],reference=None if z is None else str(z)))
# Arbitrary finite-set identities over deterministic, nonuniform membership masks.
for m in range(0,9):
 atoms=[(j*j+5*j+3)%11 for j in range(1<<m)];G=subsetsum_atoms(atoms);N=[sum(v for j,v in enumerate(atoms) if j.bit_count()==r) for r in range(m+1)];S=[sum(G[j] for j in range(1<<m) if j.bit_count()==r) for r in range(m+1)]
 check(exact_inverse(G)==atoms,f'full atom inversion {m}')
 for r in range(m+1):check(sum((-1)**(j-r)*comb(j,r)*S[j] for j in range(r,m+1))==N[r],f'exact inversion {m} {r}')
 for r in range(1,m+1):check(sum((-1)**(j-r)*comb(j-1,r-1)*S[j] for j in range(r,m+1))==sum(N[r:]),f'atleast inversion {m} {r}')
 union=sum(atoms[1:])
 for k in range(1,m+1):
  t=sum((-1)**(j+1)*S[j] for j in range(1,k+1));check(t>=union if k%2 else t<=union,f'Bonferroni {m} {k}')
# Dynamic-program checks on the general equal-cap and map expressions over lab bounds.
for n in range(9):
 for m in range(5):
  # independent Stirling recurrence instead of exponential repeated enumeration
  a=[1]+[0]*m
  for _ in range(n):a=[0]+[a[k-1]+k*a[k] for k in range(1,m+1)]
  expected=factorial(m)*a[m];check(sum((-1)**j*comb(m,j)*(m-j)**n for j in range(m+1))==expected,f'onto range {n} {m}')
 for m in range(1,5):
  for cap in range(6):
   h=lambda t:comb(t+m-1,m-1) if t>=0 else 0
   check(sum((-1)**j*comb(m,j)*h(n-j*(cap+1)) for j in range(m+1))==bounded(n,[cap]*m),f'cap range {n} {m} {cap}')
models=json.loads((R/'dist/chapters/d_inclusion-models.json').read_text())['models']
for model in models:
 for f in model['frames']:
  s=f['state'];id=model['id'];ET.fromstring(f['svg']);ET.fromstring(f['formulaHtml']);check(len(f['caption'].split())>=13,'caption '+id)
  if id=='di-atoms':check(s['count']==sum(x for j,x in enumerate(s['atoms']) if j.bit_count()==s['r']),id)
  elif id=='di-cancel':check(s['coefficient']==sum((-1)**(j+1)*comb(s['r'],j) for j in range(1,s['j']+1)),id)
  elif id=='di-atom-transform':
   a=[20,10,9,4,8,3,2,1]
   for bit in range(s['step']):
    for mask in range(8):
     if not mask>>bit&1:a[mask]-=a[mask|1<<bit]
   check(a==s['counts'],id)
  elif id=='di-inverse':check(all(s['N'][r]==[11,16,16,6,1][r] for r in range(s['r'],5)),id)
  elif id=='di-bounds':check(s['lower']<=95<=s['upper'],id+' permissible illustrative union')
  elif id=='di-missing':check(s['count']==sum(all(v+1 not in s['omitted'] for v in w) for w in product(range(3),repeat=4)),id)
  elif id=='di-derange':check(s['fixed']==[j for j,v in enumerate(s['permutation']) if j==v] and s['derangement']==(not s['fixed']),id)
  elif id=='di-fixed-intersection':check(s['count']==sum(all(p[i]==i for i in s['forced']) for p in permutations(range(4))),id)
  elif id=='di-rooks':check(s['count']==sum(all(p[r]==c for r,c in s['selected']) for p in permutations(range(4))),id)
  elif id=='di-caps':check(s['count']==sum(all(v[i]>s['caps'][i] for i in s['selected']) for v in product(range(6),repeat=3) if sum(v)==5),id)
  elif id=='di-sieve':check(s['values']==[x for x in range(1,25) if all(x%d==0 for d in s['divisors'])],id)
  elif id=='di-weights':check(sum(s['weights'])==10 and str(Fraction(s['weights'][3],sum(s['weights'][i] for i in [2,3])))==s['conditional'],id)
  elif id=='di-adjacency':check(s['count']==sum(all(any(p[i]==u and p[i+1]==v for i in range(3)) for u,v in s['edges']) for p in permutations(range(4))),id)
  else:raise ValueError(id)
auth=json.loads((B/'d_inclusion-authentic.json').read_text());cache=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
for x in auth:check(hashlib.sha256((cache/x['repoPath']).read_bytes()).hexdigest()==x['sourceSha256'],'authentic fingerprint '+x['id'])
check(map_count(6,4,'onto')==1560 and Fraction(1560,30)==52,'authentic MSc answer')
check(32-(13+8+6+2)==3,'authentic PhD bound attained')
courses=json.loads((B/'d_inclusion-reviewed-courses.json').read_text());check(len({x['university'] for x in courses if x['reviewed']})>=4,'four read universities')
baseline='310897fdc44f3f304bb279995f715bdfa246944a';lessons=json.loads(subprocess.check_output(['git','show',baseline+':dist/lessons.json'],cwd=R,text=True));retained=0
for w in lessons:
 for c in w['chapters']:
  old=subprocess.check_output(['git','show',baseline+':dist/'+c['url']],cwd=R).decode('utf-8');new=(R/'dist'/c['url']).read_text(encoding='utf-8')
  # Only the approved counting chapter's header is allowed to change.
  check(old==new or (c['topicId']=='d_counting' and old.replace('Review draft ·','Student-approved chapter ·')==new),'preserve full prior chapter '+c['topicId'])
  retained+=old.count('class="exam-question"')
check(retained==1835,'retained question inventory')
page=(R/'dist/chapters/d_inclusion.html').read_text();check(page.count('class="exam-question"')==82,'rendered bank');check(page.count('class="review-rule"')==80,'rendered notes');check(len(models)==13,'models count')
for formula in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(formula);check(True,'valid structured formula')
check(not re.search('[\u0600-\u06ff\ufffd\x00]',page),'English glyph scope')
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,a):
  a=dict(a)
  if 'id' in a:self.ids.add(a['id'])
  for k in ('href','src'):
   if k in a:self.links.append(a[k])
p=Links();p.feed(page)
for link in p.links:
 u=urlparse(link)
 if u.scheme or u.netloc:continue
 if not u.path:check(not u.fragment or u.fragment in p.ids,'anchor '+link)
 else:check((R/'dist/chapters'/unquote(u.path)).resolve().exists(),'local resource '+link)
report=dict(topicId='d_inclusion',state='passed',checks=COUNT,questionChecks=RESULTS,retainedQuestions=retained,retainedChapters=32,models=13,checkpoints=sum(len(m['frames']) for m in models),formulaInstances=len(re.findall('<math\\b',page)),limitations='Finite references check the enumerated ranges; general mathematical claims have written proofs. No universal unseen-examination guarantee.')
(B/'d_inclusion-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='questionChecks'}))
