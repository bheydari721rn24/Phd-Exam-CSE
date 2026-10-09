from pathlib import Path
from itertools import product
import json,math,subprocess,hashlib,re,sys,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'p_recursion-evidence';checks=0
def ck(x,msg=''):
 global checks;checks+=1;assert x,msg
cases=[];expect=[]
def add(spec,result,calls,depth,ops):cases.append(spec);expect.append((result,dict(calls=calls,depth=depth,ops=ops)))
fib=[0,1]
for n in range(2,15):fib.append(sum(fib[-2:]))
for n in range(9):
 add(dict(operation='factorial',n=n),math.factorial(n),n+1,n+1,n)
 add(dict(operation='memo',n=n),fib[n],1 if n<=1 else 2*n-1,max(1,n),max(0,n-1))
 add(dict(operation='stride',n=n),list(range(n-1,-1,-2)),(n+1)//2+1,(n+1)//2+1,(n+1)//2)
for n in range(6):add(dict(operation='fib',n=n),fib[n],2*fib[n+1]-1,max(1,n),fib[n+1]-1)
for x in range(200):
 d=len(str(x));add(dict(operation='digits',value=x),sum(map(int,str(x))),d,d,d-1)
for a in range(18):
 for b in range(18):
  x,y=a,b;count=1
  while y:x,y=y,x%y;count+=1
  add(dict(operation='gcd',a=a,b=b),math.gcd(a,b),count,count,count-1)
for a in range(4):
 for e in range(14):
  d=max(1,e.bit_length());m=0 if e==0 else e.bit_length()-1+e.bit_count()-1
  add(dict(operation='power',a=a,exponent=e),a**e,d,d,m)
for n in range(7):
 for values in product('ab',repeat=n):
  s=''.join(values);ops=0
  for i in range(n//2):
   ops+=1
   if s[i]!=s[-1-i]:break
  calls=ops+(1 if s==s[::-1]else 0)
  add(dict(operation='palindrome',text=s),s==s[::-1],calls,calls,ops)
for n in range(9):
 a=list(range(0,2*n,2))
 for target in range(-1,2*n+1):
  l,r=0,n;ops=0
  while l<r:
   m=(l+r)//2;ops+=1
   if a[m]==target:break
   if target<a[m]:r=m
   else:l=m+1
  calls=ops+(target not in a)
  add(dict(operation='binary',array=a,target=target),target in a,calls,calls,ops)
for n in range(5):
 outs=[list(q)for q in product([0,1],repeat=n)]
 expected=[[i for i,b in enumerate(row)if b]for row in outs]
 add(dict(operation='subsets',n=n),expected,2**(n+1)-1,n+1,0)
 add(dict(operation='hanoi',n=n),[[],[],list(range(n,0,-1))],2**(n+1)-1,n+1,2**n-1)
script="const fs=require('fs'),a=require('./dist/chapters/p_recursion.js');process.stdout.write(JSON.stringify(JSON.parse(fs.readFileSync(0,'utf8')).map((s,i)=>{const m=a.makeModel('test-'+i,'Independent check',s);return {result:m.result,counts:m.counts,frames:m.frames.map(f=>({stack:f.snapshot.stack,pegs:f.snapshot.pegs,phase:f.snapshot.phase,checks:f.teaching.checks}))};})));"
actual=json.loads(subprocess.check_output(['node','-e',script],input=json.dumps(cases).encode(),cwd=R))
for spec,a,(value,counts)in zip(cases,actual,expect):
 ck(a['result']==value,(spec,a['result'],value));ck(a['counts']==counts,(spec,a['counts'],counts))
 for f in a['frames']:
  ck(all(x['result']for x in f['checks']),spec)
  if f.get('pegs'):
   for p in f['pegs']:ck(all(p[i]>p[i+1]for i in range(len(p)-1)),spec)
# Independent identities for the symbolic examples and boundary formulae.
for n in range(1,30):
 ck(sum(range(1,n+1))==n*(n+1)//2)
 for k in range(1,6):ck(len(range(n,0,-k))==math.ceil(n/k))
for n in range(8):
 ck(sum(math.perm(n,d)for d in range(n+1))==sum(math.factorial(n)//math.factorial(k)for k in range(n+1)))
 ck(sum(sum(row)for row in product([0,1],repeat=n))==(n*2**(n-1)if n else 0))
ck(math.factorial(5)//4==30);ck(sum(math.perm(5,d)for d in range(6))==326)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/p_recursion.html').read_text(encoding='utf-8');maths=re.findall(r'<math\b[^>]*>[\s\S]*?</math>',page)
for s in maths:
 root=ET.fromstring(s);ck(not closing_script_bases(root),s);ck(not delimiter_issues(root),s)
ck(not re.search('[\u0600-\u06ff]',page));ck('$'not in page and 'MATHSLOT'not in page and '<!--'not in page)
ck(page.count('class="exam-question"')==81);ck(page.count('class="review-rule"')==80)
qs=json.loads((B/'p_recursion-questions.json').read_text());ck(all(len(q['solution'].split())>=50 for q in qs));ck(len({q['id']for q in qs})==80)
models=json.loads((R/'dist/chapters/p_recursion-models.json').read_text())['models'];ids={m['id']for m in models};ck(all(q.get('modelId')in ids for q in qs if q.get('modelId')))
for m in models:
 for f in m['frames']:ck(not delimiter_issues(ET.fromstring(f['formulaHtml'])));ck(all(x['result']for x in f['teaching']['checks']))
prior=json.loads((E/'prior-library.json').read_text());oldq=0
corrections={x['path']:x for x in json.loads((E/'source-corrections.json').read_text())['records']}
for c in prior['chapters']:
 path='dist/'+c['url'];actualSha=hashlib.sha256((R/path).read_bytes()).hexdigest()
 if path in corrections:
  ck(corrections[path]['beforeSha256']==c['sha256']);ck(actualSha==corrections[path]['afterSha256'])
  original=subprocess.check_output(['git','show',prior['sourceCommit']+':'+path],cwd=R).decode('utf-8').replace('\r\n','\n');updated=(R/path).read_text(encoding='utf-8')
  def outside(s):
   marker='data-source-id="MS_CS_1393_Q167"';i=s.index(marker);a=s.rfind('<section',0,i);j=s.find('data-source-id=',i+len(marker));b=s.rfind('<section',a,j)if j>=0 else len(s);return s[:a],s[b:]
  ck(outside(original)==outside(updated),path+' changed outside Q167')
 else:ck(actualSha==c['sha256'],c['url'])
 ck((R/path).read_text(encoding='utf-8').count('class="exam-question"')==c['questions']);oldq+=c['questions']
cs=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']];ck(len(cs)==47);ck(sum(c['questionCount']for c in cs)==3082);ck(next(c for c in cs if c['topicId']=='p_strings')['status']=='ready')
result=dict(status='passed',exactChecks=checks,independentAlgorithmRuns=len(cases),mathInstances=len(maths),priorChapterCount=46,priorQuestionCount=oldq,chapterCount=len(cs),questionCount=3082,scope='Independent iterative/Python oracles over bounded recursive executions and exact symbolic identities; no universal unseen-exam accuracy claim.')
(E/'mathematics.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');(E/'lesson-and-retention.json').write_text(json.dumps(dict(priorUnchangedPages=40,priorPagesWithOnlyCheckedQ167Correction=6,priorChapters=46,priorQuestions=3001,sections=30,lessonWords=len((B/'p_recursion.en.md').read_text().split()),questions=81,rules=80),indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
