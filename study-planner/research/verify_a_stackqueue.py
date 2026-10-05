"""Independent finite checks against simple specifications; not an unseen-exam guarantee."""
import itertools,json,math,hashlib,random,re
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from pathlib import Path
from sq_engine import evaluate
B=Path(__file__).resolve().parent;R=B.parent;counts={};fixtures=[]
def checked(k):counts[k]=counts.get(k,0)+1
def histories(n,h):
 out=[]
 def rec(p,d,S,O,peak):
  if p==d==n:out.append((tuple(O),peak));return
  if p<n and len(S)<h:rec(p+1,d,S+[p+1],O,max(peak,len(S)+1))
  if S:rec(p,d+1,S[:-1],O+[S[-1]],peak)
 rec(0,0,[],[],0);return out
for n in range(1,8):
 possible={x:peak for x,peak in histories(n,n)}
 assert len(possible)==math.comb(2*n,n)//(n+1)
 for h in range(n+1):assert evaluate('catalan',dict(n=n,h=h))['result']['count']==len(histories(n,h));checked('boundedCatalan')
 for p in itertools.permutations(range(1,n+1)):
  z=evaluate('permutation',dict(target=list(p)))['result'];avoid=not any(p[i]>p[k]>p[j] for i in range(n) for j in range(i+1,n) for k in range(j+1,n))
  assert z['valid']==(p in possible)==avoid,(n,p,z)
  if z['valid']:assert z['peak']==possible[p]
  checked('permutation312AndMinimumCapacity')
for C in range(1,6):
 for initial in range(C):
  for bits in itertools.product('ED',repeat=8):
   q=[];ops=[];expected=[];ok=True
   for j,o in enumerate(bits):
    if o=='E':
     if len(q)==C:ok=False;break
     q.append(j);ops.append('E:'+str(j))
    else:
     if not q:ok=False;break
     expected.append(q.pop(0));ops.append('D')
   if not ok:continue
   z=evaluate('ring',dict(C=C,f=initial,ops=ops))['result'];assert z['values']==q and z['output']==expected and z['f']==(initial+len(expected))%C
   checked('ringAllFrontOffsets')
for n in range(1,7):
 for A in itertools.product(range(3),repeat=n):
  for equal in [False,True]:
   ans=[next((j for j in range(i+1,n) if A[j]>=A[i] if equal),None) if equal else next((j for j in range(i+1,n) if A[j]>A[i]),None) for i in range(n)]
   assert evaluate('monostack',dict(values=list(A),equal=equal))['result']['answers']==ans;checked('nextGreaterDuplicates')
  best=max(min(A[i:j+1])*(j-i+1) for i in range(n) for j in range(i,n))
  assert evaluate('histogram',dict(values=list(A)))['result']['best']==best;checked('histogramAllIntervals')
  for k in range(1,n+1):assert evaluate('window',dict(values=list(A),k=k))['result']['answers']==[max(A[j:j+k]) for j in range(n-k+1)];checked('windowBruteForce')
for n in range(1,41):
 for k in range(1,13):
  j=0
  for m in range(2,n+1):j=(j+k)%m
  assert evaluate('josephus',dict(n=n,k=k))['result']['survivor']==j+1;checked('josephusRecurrence')
for p in itertools.permutations([1,2,3,4,5]):assert evaluate('sort',dict(values=list(p)))['result']['S']==sorted(p,reverse=True);checked('auxiliaryStackSorting')
for n in range(0,13):
 z=evaluate('recursive',dict(values=list(range(n))))['result'];assert z['S']==list(range(n)) and z['count']==n and z['cost']==2*n;checked('recursiveRestoration')
 for copy in [False,True]:
  z=evaluate('restore',dict(values=list(range(n)),copy=copy))['result'];assert z['S']==list(range(n)) and z['cost']==(5 if copy else 4)*n
  if copy:assert z['C']==list(range(n))
  checked('iterativeRestorationAndCopy')
rng=random.Random(1406)
for i in range(180):
 q=[];ops=[];e=d=0
 for j in range(16):
  if not q or len(q)<8 and rng.random()<.55:x=rng.randrange(-20,21);q.append(x);ops.append('E:'+str(x));e+=1
  elif rng.random()<.25:ops.append('F')
  else:q.pop(0);ops.append('D');d+=1
 z=evaluate('two',dict(ops=ops))['result'];assert z['queue']==q and z['cost']==e+2*z['t']+d and z['cost']<=3*e+d;checked('twoStackCostAndFIFO')
 if i<40:fixtures.append(dict(mode='two',params=dict(ops=[[o[:1],int(o[2:])] if o.startswith('E:') else [o] for o in ops]),expected=z))
for C in range(1,13):
 ops=['E:'+str(j) for j in range(C)]+['D']*C
 z=evaluate('ring',dict(C=C,ops=ops))['result'];fixtures.append(dict(mode='ring',params=dict(C=C,ops=[['E',j] for j in range(C)]+[['D']]*C),expected=z))
for tokens in ['18 6 3 / - 4 *','5 2 / 7 3 / + 6 *','7 3 /','-3 5 - 2 /']:
 z=evaluate('postfix',dict(tokens=tokens.split()))['result'];assert z['valid'];fixtures.append(dict(mode='postfix',params=dict(tokens=tokens.split()),expected=dict(value=z['value'])))
for target in [[3,2,1,5,4],[3,1,2],[1],[2,1],[1,3,2],[4,2,3,1]]:
 z=evaluate('permutation',dict(target=target))['result'];fixtures.append(dict(mode='permutation',params=dict(target=target),expected=z))
for values,k in [([1,3,-1,-3,5,3,6,7],3),([5,5,4,5],3),([1],1),([-2,-3],2)]:fixtures.append(dict(mode='window',params=dict(values=values,k=k),expected=dict(maxima=evaluate('window',dict(values=values,k=k))['result']['answers'])))
models=json.loads((R/'dist/chapters/a_stackqueue-models.json').read_text(encoding='utf-8'))
for m in models['models']:assert evaluate(m['kind'],m['params'])['result']==m['result'];checked('publishedModelRecomputation')
baseline=json.loads((B/'a_stackqueue-retention-baseline.json').read_text(encoding='utf-8'))
print('BASELINE KEYS',list(baseline)[:5])
for key,value in baseline.items():
 p=R/key if (R/key).exists() else R/'dist/chapters'/key
 assert hashlib.sha256(p.read_bytes()).hexdigest()==value;checked('approvedChapterRetention')
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[];self.classes=[];self.words=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if 'href' in a or 'src' in a:self.links.append(a.get('href') or a.get('src'))
  self.classes.extend(a.get('class','').split())
 def handle_data(self,s):self.words.extend(s.split())
page=R/'dist/chapters/a_stackqueue.html';soup=Page();soup.feed(page.read_text(encoding='utf-8'));ids=soup.ids
for u in soup.links:
 a=urlsplit(u)
 if a.scheme:continue
 if not a.path and a.fragment:assert a.fragment in ids,u
 if a.path:assert (page.parent/unquote(a.path)).resolve().exists(),u
 checked('localLinksAndAssets')
assert soup.classes.count('exam-question')==84 and soup.classes.count('review-rule')==80
report=dict(topicId='a_stackqueue',state='passed',checks=counts,renderedWordCount=len(soup.words),finiteVerificationOnly=True,limits='Finite enumeration and independent oracles supplement the stated proofs; they do not certify unseen exam performance.',models=len(models['models']),frames=sum(len(m['frames']) for m in models['models']))
(B/'a_stackqueue-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
(B/'a_stackqueue-lab-fixtures.json').write_text(json.dumps(fixtures,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
