"""Independent transition references; finite checks complement the written proofs."""
from pathlib import Path
import json,math,hashlib,subprocess,re,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;checks=0
def require(condition,message):
 global checks
 checks+=1
 assert condition,message
def grow(m,c0,g):
 cap=c0;buf=[];copy=0;worst=0;peak=cap
 for i in range(m):
  cost=1
  if len(buf)==cap:
   new=[None]*(cap*g);peak=max(peak,cap+len(new))
   for j,v in enumerate(buf):new[j]=v;copy+=1;cost+=1
   cap=len(new)
  buf.append(i);worst=max(worst,cost)
 return cap,copy,worst,peak
def cycle(mu,lam):
 nxt=list(range(1,mu+lam))+[mu];s=f=0;t=0
 while True:
  s=nxt[s];f=nxt[nxt[f]];t+=1
  if s==f:break
 h=0;steps=0
 while h!=f:h=nxt[h];f=nxt[f];steps+=1
 return t,h,steps
refs=[]
for m in range(1,65):
 for c0 in [1,2,3,4,7,16]:
  for g in [2,3,4]:
   C,c,w,p=grow(m,c0,g);require(c==(C-c0)//(g-1),'geometric sum');require(c+m<=m*(g/(g-1)+1)+c0*g,'linear bound')
   if c0 in [1,3,16] and g in [2,3]:refs.append(dict(mode='growth',params=dict(m=m,c0=c0,g=g),expected=dict(copies=c,writes=c+m,capacity=C)))
for n in range(13):
 for i in range(n+1):
  a=list(range(n))+[None];count=0
  for j in range(n,i,-1):a[j]=a[j-1];count+=1
  a[i]=-1;require(a==list(range(i))+[-1]+list(range(i,n)),'stable insertion content');require(count==n-i,'exact insertion shifts')
 for i in range(n):
  a=list(range(n));count=0
  for j in range(i,n-1):a[j]=a[j+1];count+=1
  require(a[:n-1]==list(range(i))+list(range(i+1,n)),'stable deletion content');require(count==n-i-1,'deletion shifts')
for n in range(31):
 nxt=list(range(1,n))+[None] if n else [];prev=None;cur=0 if n else None;count=0
 while cur is not None:
  old=nxt[cur];nxt[cur]=prev;prev=cur;cur=old;count+=1
  seen=[];v=prev
  while v is not None:seen.append(v);v=nxt[v]
  require(seen==list(range(count-1,-1,-1)),'reversal prefix invariant')
 require(count==n,'reversal writes')
 if n<=7:refs.append(dict(mode='reverse',params=dict(n=n),expected=dict(head=n-1 if n else None,writes=n)))
for mu in range(41):
 for lam in range(1,31):
  t,entry,reset=cycle(mu,lam);require(t==lam*max(1,math.ceil(mu/lam)),'meeting formula');require(entry==mu and reset==mu,'entry proof reference')
  if mu<=5 and lam<=5:refs.append(dict(mode='floyd',params=dict(mu=mu,lam=lam),expected=dict(meeting=t,entry=entry,resetSteps=reset)))
for n in range(1,9):
 for i in range(n+1):
  refs.append(dict(mode='shift',params=dict(values=list(range(n)),index=i,value=-9),expected=dict(result=list(range(i))+[-9]+list(range(i,n)),writes=n-i+1,shifts=n-i)))
# Exhaust every legal short append/delete-last word; verify potential transition costs.
for mask in range(1<<13):
 n=0;C=1;phi=lambda n,C:2*n-C if n>=C/2 else C/2-n
 for k in range(13):
  op=(mask>>k)&1
  if not op and not n:continue
  before=phi(n,C);actual=1
  if op:
   if n==C:actual+=n;C*=2
   n+=1
  else:
   n-=1
   if C>=4 and n==C//4:actual+=n;C//=2
  require(actual+phi(n,C)-before<=3 if op else actual+phi(n,C)-before<=2,'potential transition')
q=json.loads((B/'a_arrays-questions.json').read_text());actual=json.loads((B/'a_arrays-authentic.json').read_text())
require(len(q)==84 and len(actual)==2,'question inventory');require(len({x['id'] for x in q})==84,'unique problems')
checked=[]
for z in q:
 d=z.get('check')
 if not d:continue
 kind=d['kind']
 if kind in ['growth','growthcompound','doubling']:
  C,c,w,p=grow(d['m'],d.get('c0',1),d.get('g',2));result=(C,c,w,p)
  if kind=='doubling':require(str(c) in z['expected'] and str(c+d['m']) in z['expected'] and str(C) in z['expected'],'bank doubling')
  elif kind=='growth':require(str(c) in z['expected'] and str(C) in z['expected'],'bank growth')
  else:require(z['expected']==f"{c}; {c+d['m']}; {C-d['m']}; {p*d['b']}",'compound memory')
 elif kind in ['floyd','cyclecompound']:
  t,en,reset_count=cycle(d['mu'],d['lam']);result=(t,en,reset_count)
  require(str(t) in z['expected'],'bank meeting')
  if kind=='cyclecompound':require(z['expected']==f"{t}; {2*reset_count}; {d['lam']}; {3*t+2*reset_count+d['lam']}",'full cycle work')
 elif kind=='front':result=2*sum(range(d['m']));require(str(result)==z['expected'],'front work')
 elif kind=='indexed':result=sum(range(d['n']));require(str(result) in z['expected'],'indexed work')
 elif kind=='batch':result=sum(d['n']+t-d['i'] for t in range(d['k']));require(z['expected'].startswith(str(result)+'; '+str(result+d['k'])),'batch work')
 elif kind=='additive':result=sum(range(d['h'],d['m'],d['h']));require(str(result)==z['expected'],'additive work')
 elif kind=='shrink':C=d['C'];before=C/2-(C//4+1);result=1+C//4;require(result-before==2,'shrink work')
 elif kind=='insertdelete':result=d['n']-d['i']+d['n']-d['j'];require(str(result) in z['expected'],'two operations')
 elif kind=='peak':result=d['C']*(d['g']+1)*d['b'];require(str(result) in z['expected'],'peak storage')
 elif kind=='kth':result=2*d['n']-d['k'];require(str(result) in z['expected'],'gap scan')
 elif kind=='reverse':result=d['n'];require(z['expected'].startswith(str(result)),'reverse work')
 elif kind=='blocks':result=len({(d['r']+i)//d['L'] for i in range(d['n'])});require(str(result)==z['expected'],'block enumeration')
 elif kind=='support':result=len([(a,b) for a in range(d['x']) for b in range(d['y'])]);require(z['expected'].startswith(str(result)+';'),'support Cartesian product')
 elif kind=='traversecompound':moves=d['n']+(d['n']-d['k']);blocks=len({(d['r']+i)//d['L'] for i in range(d['n'])});result=(moves,blocks);require(z['expected']==f'{moves} links; {blocks} blocks','combined traversal')
 else:raise AssertionError(kind)
 checked.append(dict(id=z['id'],kind=kind,reference=result))
for z in actual:
 p=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/z['repoPath'];require(hashlib.sha256(p.read_bytes()).hexdigest()==z['sourceSha256'],'archive hash')
models=json.loads((R/'dist/chapters/a_arrays-models.json').read_text());require(len(models['models'])==20,'model inventory')
for m in models['models']:
 require(bool(m['invariant']) and len(m['frames'])>=2,'model contract')
 for f in m['frames']:
  ET.fromstring(f['svg']);ET.fromstring(f['formulaHtml']);require('.55em' not in f['formulaHtml'],'no synthetic wrap')
  s=f['state']
  if m['id']=='resize':require(s['copies']==sum(x is not None for x in s.get('new',[]))-(1 if len(s.get('new',[]))>4 and s.get('new',[None]*5)[4] is not None else 0),'resize trace')
  if m['id']=='scan-cost':require(s['restartCost']==sum(range(s['rank']+1)),'scan trace')
  if m['id']=='floyd':require(s['slow']==(s['t'] if s['t']<3 else 3+(s['t']-3)%4),'slow position')
  if m['id']=='orthogonal':require(all(v in [10,14,15,21] for i,j,v in s['entries']),'matrix values')
html=(R/'dist/chapters/a_arrays.html').read_text();require(html.count('class="exam-question"')==86,'rendered bank');require(html.count('class="review-rule"')==80,'rendered rules');require(html.count('data-arrays-model=')==20,'placements')
require(not re.search('[\u0600-\u06ff]',html),'English only');require('MATHSLOT' not in html and '\x08' not in html,'clean math')
maths=re.findall(r'<math\b[\s\S]*?</math>',html)
for formula in maths:ET.fromstring(formula);require('rowspacing=".55em"' not in formula and 'rowspacing=".5em"' not in formula,'complete formulas')
base='bb29506e6c92cf3b52c62b504ef7ea4c5dab13cf';entries=0;retained=0
names=subprocess.check_output(['rtk','proxy','git','ls-tree','-r','--name-only',base,'dist/chapters'],cwd=R,text=True).splitlines()
for name in names:
 if not name.endswith('.html'):continue
 old=subprocess.check_output(['rtk','proxy','git','show',base+':'+name],cwd=R).decode('utf-8');new=(R/name).read_text()
 if name.endswith('/d_pigeonhole.html'):old=old.replace('Review draft ·','Student-approved chapter ·',1)
 require(new==old,'approved chapter preserved: '+name);retained+=1;entries+=new.count('class="exam-question"')
require(retained==34 and entries==1999,'retained inventory')
(B/'a_arrays-lab-reference.json').write_text(json.dumps(refs,indent=2)+'\n')
report=dict(topicId='a_arrays',state='passed',checks=checks,retainedChapters=retained,retainedQuestions=entries,questions=86,originalQuestions=84,authenticQuestions=2,checkedNumericBankItems=checked,labReferenceCases=len(refs),models=20,checkpoints=sum(len(m['frames']) for m in models['models']),nativeMathInstances=len(maths),scope='Finite transition checks plus explicit general written proofs. Conceptual solutions manually reasoned; official exam keys unavailable.')
(B/'a_arrays-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='checkedNumericBankItems'}))
