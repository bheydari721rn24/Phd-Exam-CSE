from pathlib import Path
from collections import deque
from fractions import Fraction
import json,subprocess,re,hashlib,sys,random,xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'i_uninformed-evidence';checks=0
def ck(x):
 global checks
 assert x;checks+=1
rng=random.Random(1406);cases=[];expected=[]
# Independent Bellman-Ford and FIFO oracles do not import the JS engine.
for trial in range(360):
 n=rng.randint(2,7);nodes=[chr(65+i)for i in range(n)];edges=[[u,v,rng.randint(0,9)]for u in nodes for v in nodes if rng.random()<.20];s,g=nodes[0],nodes[-1];dist={v:float('inf')for v in nodes};dist[s]=0
 for _ in range(n-1):
  for u,v,c in edges:dist[v]=min(dist[v],dist[u]+c)
 depth={s:0};q=deque([s])
 while q:
  u=q.popleft()
  for a,v,c in edges:
   if a==u and v not in depth:depth[v]=depth[u]+1;q.append(v)
 for alg in ['bfs','dfs','ucs','dls','ids']:
  cases.append(dict(graph=dict(nodes=nodes,edges=edges,start=s,goal=g),alg=alg,limit=n,cap=20000));expected.append((alg,dist[g],depth.get(g),edges))
script="const fs=require('fs'),a=require('./dist/chapters/i_uninformed.js');process.stdout.write(JSON.stringify(JSON.parse(fs.readFileSync(0,'utf8')).map(x=>a.run(x.graph,x.alg,x.limit,x.cap).result)));"
out=subprocess.check_output(['node','-e',script],input=json.dumps(cases).encode(),cwd=R);actual=json.loads(out)
for a,(alg,cost,depth,edges) in zip(actual,expected):
 ck((a['termination']=='success')==(depth is not None))
 if depth is not None:
  ck(bool(a['path']))
  ck(a['depth']==len(a['path'])-1);ck(all(any(u==x and v==y for u,v,c in edges)for x,y in zip(a['path'],a['path'][1:])))
  if alg=='ucs':ck(a['cost']==cost)
  if alg in ['bfs','ids']:ck(a['depth']==depth)
# Exact formulas include b=1 separately and distinguish generated/selected bounds.
for b in range(1,12):
 for d in range(10):
  N=sum(b**i for i in range(d+1));I=sum((d-i+1)*b**i for i in range(d+1));ck(I==sum(sum(b**i for i in range(L+1))for L in range(d+1)))
  if b>1:ck(N==(b**(d+1)-1)//(b-1));ck(I==(b**(d+2)-(d+2)*b+d+1)//(b-1)**2)
  else:ck(I==(d+1)*(d+2)//2)
ck(6**8*96==161243136);ck(sum((5-i)*2**i for i in range(5))==57);ck(sum((6-i)*10**i for i in range(6))==123456)
ck(sum(3**i for i in range(7))==1093);ck(1+3*7==22);ck(sum(2**i for i in range(4))+2*(8-1)==29)
qs=json.loads((B/'i_uninformed-questions.json').read_text());auth=json.loads((B/'i_uninformed-authentic.json').read_text());ck(len(qs)==80 and len(auth)==1);ck(all(len(q['solution'].split())>=55 for q in qs));ck(len({q['id']for q in qs+auth})==81)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/i_uninformed.html').read_text(encoding='utf-8');maths=re.findall(r'<math\b[^>]*>[\s\S]*?</math>',page)
for s in maths:
 root=ET.fromstring(s);ck(not closing_script_bases(root));ck(not delimiter_issues(root))
ck(not re.search('[\u0600-\u06ff]',page));ck('MATHSLOT'not in page and '$'not in page and '<!--'not in page);ck(page.count('class="exam-question"')==81);ck(page.count('class="review-rule"')==80)
data=json.loads((R/'dist/chapters/i_uninformed-models.json').read_text());ids={m['id']for m in data['models']};ck(all(q.get('modelId')in ids for q in qs+auth if q.get('modelId')))
for m in data['models']:
 for f in m['frames']:
  ck(f['snapshot']==f['teaching']['currentState']);ck(bool(f['teaching']['checks']))
  for s in [f['formulaHtml']]+[c['mathHtml']for c in f['teaching']['checks']]:ck(not delimiter_issues(ET.fromstring(s)))
by={m['id']:m for m in data['models']};ck(by['ucs-main']['result']['cost']==4);ck(by['ucs-main']['result']['stale']==1);ck(by['depth-alias-main']['result']['path']==['S','X','G']);ck(by['dls-cutoff']['result']['termination']=='cutoff');ck(by['ids-main']['result']['selected']==10 and by['ids-main']['result']['expanded']==6);ck(by['costly-dls']['result']['cost']==30)
prior=json.loads((E/'prior-library.json').read_text());oldq=0
for c in prior['chapters']:ck(hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']);oldq+=c['questions']
lessons=json.loads((R/'dist/lessons.json').read_text());cs=[c for w in lessons for c in w['chapters']];ck(len(cs)==45);ck(sum(c['questionCount']for c in cs)==2920);ck(next(c for c in cs if c['topicId']=='i_agents')['status']=='ready')
result=dict(status='passed',exactChecks=checks,independentlyComparedSearchRuns=len(cases),randomGraphs=360,mathInstances=len(maths),priorChapterCount=len(prior['chapters']),priorQuestionCount=oldq,chapterCount=len(cs),questionCount=sum(c['questionCount']for c in cs),scope='Independent finite-graph reachability, depth and cost oracles; exact count identities and delimiters. Not universal unseen-exam certification.')
(E/'mathematics.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');(E/'lesson-and-retention.json').write_text(json.dumps(dict(priorPagesUnchanged=True,priorChapters=44,priorQuestions=2839,sections=len(re.findall(r'^## ',(B/'i_uninformed.en.md').read_text(),re.M)),lessonWords=len((B/'i_uninformed.en.md').read_text().split()),questions=81,rules=80),indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
