from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
import json,subprocess,re,hashlib,sys,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'i_agents-evidence';checks=0
def ck(x):
 global checks
 assert x;checks+=1
# Independent branch enumeration: optimize complete signal policies without using
# the JavaScript engine's posterior-first implementation.
cases=[];expected=[]
for p,h,l in product([F(0),F(1,4),F(3,10),F(1,2),F(3,4),F(1)],[F(0),F(1,5),F(1,2),F(4,5),F(1)],[F(0),F(1,5),F(1,2),F(4,5),F(1)]):
 for U in[[[12,-4],[5,5]],[[-7,-3],[-2,-8]],[[0,0],[0,0]],[[1,-100],[0,0]]]:
  c=F(1,4);prior=[p*r[0]+(1-p)*r[1]for r in U];base=max(prior)
  # Every possible signal-conditioned action pair is enumerated directly.
  totals=[p*(h*U[a][0]+(1-h)*U[b][0])+(1-p)*(l*U[a][1]+(1-l)*U[b][1])for a,b in product(range(2),repeat=2)]
  post=max(totals);perf=p*max(r[0]for r in U)+(1-p)*max(r[1]for r in U)
  cases.append([str(p),str(h),str(l),U,str(c)]);expected.append(dict(priorValue=str(base),afterValue=str(post),evsi=str(post-base),vpi=str(perf-base),netValue=str(post-c),netGain=str(post-base-c)))
cases.append(['9999/10000','7777/10000','3333/10000',[[10000,-10000],[-9999,9999]],'9999/10000'])
p,h,l,c=map(F,[cases[-1][0],cases[-1][1],cases[-1][2],cases[-1][4]]);U=cases[-1][3];base=max(p*r[0]+(1-p)*r[1]for r in U);post=max(p*(h*U[a][0]+(1-h)*U[b][0])+(1-p)*(l*U[a][1]+(1-l)*U[b][1])for a,b in product(range(2),repeat=2));perf=p*max(r[0]for r in U)+(1-p)*max(r[1]for r in U);expected.append(dict(priorValue=str(base),afterValue=str(post),evsi=str(post-base),vpi=str(perf-base),netValue=str(post-c),netGain=str(post-base-c)))
script="const fs=require('fs'),m=require('./dist/chapters/i_agents.js');const cases=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(cases.map(x=>m.calc(...x))));"
res=subprocess.run(['node','-e',script],input=json.dumps(cases),cwd=R,text=True,capture_output=True);assert res.returncode==0,res.stderr;actual=json.loads(res.stdout)
for a,b in zip(actual,expected):
 for k,v in b.items():ck(a[k]==v)
 ck(all(a['checks'].values()))
 for sig in a['signals']:
  if F(sig['prob'])==0:ck(sig['posterior']is None and sig['utilities']is None)
  else:ck(0<=F(sig['posterior'])<=1)
# Mathematical and combinatorial checks independent of the rendered bank.
ck(2**12==4096);ck(3**6==729);ck(3**7==2187);ck(4**5==1024);ck(2*4**3==128);ck(2*2**6*2**2==512)
ck(6*len(list(combinations(range(6),2)))==90);ck(4*15==60);ck(4*3*16==192);ck(6*16==96)
for n in range(1,12):
 for k in range(n+1):ck((n-k)*len(list(combinations(range(n),k)))==n*len(list(combinations(range(n-1),k))))
for p in[F(i,100)for i in range(101)]:ck((16*p-4>=5)==(p>=F(9,16)));ck((9-8*p>=4)==(p<=F(5,8)))
ck(F(19,50)*F(116,19)+F(31,50)*5==F(271,50));ck(F(271,50)-F(1,4)==F(517,100));ck(F(21,50)-F(1,4)==F(17,100));ck(F(21,50)-F(1,2)==F(-2,25))
belief=set(product('LR',[0,1],[0,1]));sizes=[len(belief)]
for a in['Right','Clean','Left','Clean']:
 nxt=set()
 for x,l,r in belief:
  if a=='Right':x='R'
  elif a=='Left':x='L'
  elif x=='L':l=0
  else:r=0
  nxt.add((x,l,r))
 belief=nxt;sizes.append(len(belief))
ck(sizes==[8,4,2,2,1]and belief=={('L',0,0)})
# Independently solve the takeaway game by dynamic programming.
winning=[False]
for n in range(1,101):winning.append(any(not winning[n-k]for k in[1,2]if k<=n));ck(winning[n]==(n%3!=0))
ck(F(1,2)*0+F(1,2)*10<40**.5);ck(F(9,1000)/F(108,1000)==F(1,12));ck(F(3,5)*16-9>16*F(1,100))
qs=json.loads((B/'i_agents-questions.json').read_text());auth=json.loads((B/'i_agents-authentic.json').read_text());ck(len(qs)==80 and len(auth)==2)
ck(all(len(q['solution'].split())>=55 for q in qs));ck(len({q['id']for q in qs+auth})==82)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/i_agents.html').read_text();maths=re.findall(r'<math\b[^>]*>[\s\S]*?</math>',page)
for s in maths:
 root=ET.fromstring(s);ck(not closing_script_bases(root));ck(not delimiter_issues(root))
ck(not re.search('[\u0600-\u06ff]',page));ck('MATHSLOT'not in page and '$'not in page and '<!--'not in page)
ck(page.count('class="exam-question"')==82);ck(page.count('class="review-rule"')==80)
models=json.loads((R/'dist/chapters/i_agents-models.json').read_text());ids={m['id']for m in models['models']};ck(all(q.get('modelId')in ids for q in qs if q.get('modelId')))
for m in models['models']:
 for f in m['frames']:
  ck(f['snapshot']==f['teaching']['currentState']);ck(bool(f['teaching']['checks']))
  for s in[f['formulaHtml']]+[c['mathHtml']for c in f['teaching']['checks']]:ck(not delimiter_issues(ET.fromstring(s)))
prior=json.loads((E/'prior-library.json').read_text());oldq=0
for c in prior['chapters']:ck(hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']);oldq+=c['questions']
lessons=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in lessons for c in w['chapters']];ck(len(cs)==44);ck(sum(c['questionCount']for c in cs)==2839);ck(next(c for c in cs if c['topicId']=='l_spaces')['status']=='ready')
result=dict(status='passed',exactChecks=checks,independentlyComparedLabInputs=len(cases),mathInstances=len(maths),priorChapterCount=len(prior['chapters']),priorQuestionCount=oldq,chapterCount=len(cs),questionCount=sum(c['questionCount']for c in cs),scope='Exact finite-model checks and independent policy enumeration; not a proof about all unseen examinations.')
(E/'mathematics.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');(E/'lesson-and-retention.json').write_text(json.dumps(dict(priorPagesUnchanged=True,priorChapters=43,priorQuestions=2757,sections=len(re.findall(r'^## ',(B/'i_agents.en.md').read_text(),re.M)),lessonWords=len((B/'i_agents.en.md').read_text().split()),questions=82,rules=80),indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
