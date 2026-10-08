from pathlib import Path
from itertools import product
from fractions import Fraction
import json,subprocess,re,hashlib,sys,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'p_strings-evidence';checks=0;cases=[];expected=[]
def ck(x,message=''):
 global checks
 assert x,message;checks+=1
def case(s,dst=None,result=None):cases.append(s);expected.append((dst,result))
strings=[''.join(a)for n in range(5)for a in product('ab',repeat=n)]
for s in strings:
 b=list(s.encode())+[0]
 for cap in range(1,7):
  init=[120]*cap
  case(dict(operation='copy',source=s,capacity=cap),b+[120]*(cap-len(b)) if len(b)<=cap else None,dict(status='complete'if len(b)<=cap else'rejected'))
  for k in range(7):case(dict(operation='ncpy',source=s,capacity=cap,limit=k),([*s.encode(),*([0]*max(0,k-len(s)))][:k]+[120]*(cap-k))if k<=cap else None,dict(status='complete'if k<=cap else'rejected'))
 for op,out in [('reverse',s[::-1]),('compact',s.replace('a',''))]:
  if op=='reverse':final=list(out.encode())+[0]
  else:final=b.copy();final[:len(out)+1]=list(out.encode())+[0]
  case(dict(operation=op,source='a',destination=s,capacity=len(b)),final,dict(length=len(out)))
 for p in range(len(s)+1):
  if len(s)<5:case(dict(operation='insert',source='X',destination=s,capacity=len(s)+2,position=p),list((s[:p]+'X'+s[p:]).encode())+[0],dict(length=len(s)+1))
  for r in range(len(s)-p+1):
   final=b.copy();out=s[:p]+s[p+r:];final[:len(out)+1]=list(out.encode())+[0]
   case(dict(operation='delete',source='',destination=s,capacity=len(b),position=p,remove=r),final,dict(length=len(out)))
 for t in strings:
  for k in [0,1,3,6]:
   left=s[:k];right=t[:k];sign=(left>right)-(left<right)
   case(dict(operation='compare',source=s,destination=t,capacity=len(t)+1,limit=k),None,dict(sign=sign))
  for all_ in [False,True]:
   matches=([0]if s==''else[i for i in range(max(0,len(t)-len(s)+1))if t.startswith(s,i)])
   if not all_:matches=matches[:1]
   case(dict(operation='match',source=s,destination=t,capacity=len(t)+1,all=all_),None,dict(matches=matches))
  for k in [0,1,3,6]:
   cap=7;take=s[:k];ok=len(t)+len(take)<cap;out=t+take;init=list(t.encode())+[0]*(cap-len(t));final=init.copy();final[len(t):len(out)+1]=list(take.encode())+[0]
   case(dict(operation='append',source=s,destination=t,capacity=cap,limit=k),final if ok else None,dict(status='complete'if ok else'rejected'))
# All short same-object memory movements, independently using saved original bytes.
for cap in range(1,8):
 original=[97+i for i in range(cap-1)]+[0]
 for source in range(cap+1):
  for target in range(cap+1):
   for count in range(min(cap-source,cap-target)+1):
    final=original.copy();final[target:target+count]=original[source:source+count]
    case(dict(operation='move',source='',destination=original[:-1],capacity=cap,**{'from':source,'to':target,'count':count}),final,dict(status='complete'))
script="const fs=require('fs'),a=require('./dist/chapters/p_strings.js');process.stdout.write(JSON.stringify(JSON.parse(fs.readFileSync(0,'utf8')).map(x=>{const r=a.run(x);return {result:r.result,final:r.frames.at(-1).snapshot.destination};})));"
actual=json.loads(subprocess.check_output(['node','-e',script],input=json.dumps(cases).encode(),cwd=R))
for i,(a,(dst,result))in enumerate(zip(actual,expected)):
 if dst is not None:ck(a['final']==dst,(i,cases[i],a,dst))
 for k,v in result.items():ck(a['result'].get(k)==v,(i,cases[i],a,k,v))
# Independently enumerate storage/value counts, expected scans, exact comparison maxima.
for C in range(1,7):
 for q in range(1,4):
  arrays=list(product(range(q+1),repeat=C));terminated=[a for a in arrays if 0 in a]
  ck(len(terminated)==(q+1)**C-q**C)
  values={a[:a.index(0)]for a in terminated};ck(len(values)==sum(q**j for j in range(C)))
  for j in range(C):ck(sum(a.index(0)==j for a in terminated)==q**j*(q+1)**(C-j-1))
for n in range(1,60):
 ck(max(m*(n-m+1)for m in range(1,n+1))==((n+1)**2)//4)
 ck(sum(n-k+1 for k in range(n+1))==(n+1)*(n+2)//2)
 for k in range(1,10):ck(sum(j*3+4+1 for j in range(k))==3*k*(k-1)//2+3*k+2*k)
ck(sum(1 for a in product(range(4),repeat=4)if a.count(0)%2==0)==136)
ck(sum(3**j for j in range(5))==121);ck(15*3**4==1215);ck(3**2*4**3==576)
qs=json.loads((B/'p_strings-questions.json').read_text());auth=json.loads((B/'p_strings-authentic.json').read_text());ck(len(qs)==80 and len(auth)==1);ck(all(len(q['solution'].split())>=60 for q in qs));ck(len({q['id']for q in qs+auth})==81)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/p_strings.html').read_text(encoding='utf-8');maths=re.findall(r'<math\b[^>]*>[\s\S]*?</math>',page)
for s in maths:
 root=ET.fromstring(s);ck(not closing_script_bases(root),s);ck(not delimiter_issues(root),s)
ck(not re.search('[\u0600-\u06ff]',page));ck('MATHSLOT'not in page and '$'not in page and '<!--'not in page);ck(page.count('class="exam-question"')==81);ck(page.count('class="review-rule"')==80)
data=json.loads((R/'dist/chapters/p_strings-models.json').read_text());ids={m['id']for m in data['models']};ck(all(q.get('modelId')in ids for q in qs+auth if q.get('modelId')))
for m in data['models']:
 for f in m['frames']:
  ck(bool(f['teaching']['checks']));ck(not delimiter_issues(ET.fromstring(f['formulaHtml'])))
by={m['id']:m for m in data['models']};ck(by['match-worst']['result']['comparisons']==20);ck(by['compact-main']['result']['length']==3);ck(by['match-overlap']['result']['matches']==[0,1,2]);ck(by['scan-missing']['result']['status']=='missing terminator')
prior=json.loads((E/'prior-library.json').read_text());oldq=0
for c in prior['chapters']:ck(hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']);oldq+=c['questions']
lessons=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in lessons for c in w['chapters']];ck(len(cs)==46);ck(sum(c['questionCount']for c in cs)==3001);ck(next(c for c in cs if c['topicId']=='i_uninformed')['status']=='ready')
result=dict(status='passed',exactChecks=checks,independentByteOperationRuns=len(cases),shortAlphabetStrings=len(strings),mathInstances=len(maths),priorChapterCount=len(prior['chapters']),priorQuestionCount=oldq,chapterCount=len(cs),questionCount=sum(c['questionCount']for c in cs),scope='Independent finite byte-array oracles and exact enumerations; not execution of arbitrary C or universal unseen-exam certification.')
(E/'mathematics.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');(E/'lesson-and-retention.json').write_text(json.dumps(dict(priorPagesUnchanged=True,priorChapters=45,priorQuestions=2920,sections=28,lessonWords=len((B/'p_strings.en.md').read_text().split()),questions=81,rules=80),indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
