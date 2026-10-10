"""Independent integer/search oracles and retention checks for exact routing models."""
from pathlib import Path
import itertools,json,subprocess,hashlib,re
import xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'g_mux-evidence'
cases=[]
def add(s,expected):cases.append(dict(spec=s,expected=expected))
for n in range(1,4):
 N=2**n
 for d in itertools.product([0,1],repeat=N):
  for a in range(N):
   for op in['mux','tree']:add(dict(operation=op,n=n,address=a,data=list(d)),dict(output=d[a],address=a))
 for a,e,pol in itertools.product(range(N),[0,1],['high','low']):
  logical=[int(e==1 and i==a)for i in range(N)];pins=logical if pol=='high'else[1-x for x in logical]
  for op in['decoder','demux']:add(dict(operation=op,n=n,address=a,enable=e,residual=e,polarity=pol),dict(logical=logical,pins=pins,enabled=e))
 for r in range(2**N):
  present=[i for i in range(N)if (r//(2**i))%2]
  for order in['low','high']:
   winner=(min(present)if order=='low'else max(present))if present else None
   add(dict(operation='priority',n=n,requests=r,order=order),dict(winner=winner,code=winner if winner is not None else 0,valid=int(bool(present)),grants=[int(i==winner)for i in range(N)]))
  for p in range(N):
   winner=next(((p+j)%N for j in range(N)if (p+j)%N in present),None)
   add(dict(operation='rotate',n=n,requests=r,pointer=p),dict(winner=winner,code=winner if winner is not None else 0,valid=int(bool(present))))
for a,z in itertools.product(range(4),[0,1]):add(dict(operation='shannon',n=2,address=a,residual=z),dict(output=int(2*a+z in[0,2,6,7])))
for a,b,sel in itertools.product([0,1],[0,1],range(4)):
 carry=int(a+b+1>=2);summ=(a+b+1)%2;t=int(summ!=carry);d=[1-carry,carry,t,1-t]
 add(dict(operation='integrated',n=2,a=a,b=b,address=sel),dict(carry=carry,sum=summ,t=t,data=d,output=d[sel]))
for a,b in itertools.product([0,1],repeat=2):add(dict(operation='cascade',n=1,a=a,b=b),dict(output=int(not(a or b)),t=int(not b)))
for a,e in itertools.product(range(8),[0,1]):add(dict(operation='banks',n=3,address=a,enable=e),dict(bank=a//4,local=a%4,logical=[int(e and i==a)for i in range(8)]))
geom=['abcdef','bc','abdeg','abcdg','bcfg','acdfg','acdefg','abc','abcdefg','abcdfg']
for a,pol in itertools.product(range(16),['high','low']):
 lit=''.join(str(int(c in(geom[a]if a<10 else'')))for c in'abcdefg')
 add(dict(operation='display',n=4,address=a,polarity=pol),dict(lit=lit,pattern=lit if pol=='high'else''.join(str(1-int(c))for c in lit),valid=int(a<10)))
for a in range(16):add(dict(operation='rom',n=4,address=a,data=[3*i for i in range(16)]),dict(row=a//4,column=a%4,output=3*a))
for data,en in itertools.product(itertools.product([0,1],repeat=2),repeat=2):
 owners=[i for i in range(2)if en[i]];v=[data[i]for i in owners];value='Z'if not owners else ('CONFLICT'if len(set(v))>1 else v[0])
 add(dict(operation='bus',n=1,data=list(data),enables=list(en)),dict(value=value,owners=owners,singleOwner=len(owners)==1,contractViolation=len(owners)>1))
fixture=E/'reference-cases.json';fixture.write_text(json.dumps(cases),encoding='utf-8')
js="const fs=require('fs'),{makeModel}=require('./dist/chapters/g_mux.js');const qs=JSON.parse(fs.readFileSync('./research/g_mux-evidence/reference-cases.json'));let states=0;for(let i=0;i<qs.length;i++){const q=qs[i],m=makeModel('qa','independent QA',q.spec);for(const[k,v]of Object.entries(q.expected))if(JSON.stringify(m.result[k])!==JSON.stringify(v))throw Error(JSON.stringify({i,k,v,actual:m.result[k]}));for(const f of m.frames){states++;if(!f.teaching.why||!f.svg.includes('<svg'))throw Error('Invalid checkpoint');}if(JSON.stringify(m.frames.at(-1).snapshot.result)!==JSON.stringify(m.result))throw Error('Final result mismatch');}process.stdout.write(JSON.stringify({cases:qs.length,states}));"
result=json.loads(subprocess.check_output(['node','-e',js],cwd=R,text=True,encoding='utf-8'))
# Independently re-enumerate both authenticated answers and selected derived cofactor exercises.
q82=[8*a+4*b+2*c+d for a,b,c,d in itertools.product([0,1],repeat=4)if ([int(a+b==0),int(a+b>0),int(a*b==0),a*b][2*c+d])]
assert q82==[0,2,5,6,9,10,13,15]
assert [4*a+2*b+c for a,b,c in itertools.product([0,1],repeat=3)if ((not c)and(a!=b))or(c and a)]==[2,4,5,7]
assert [4*a+2*b+c for a,b,c in itertools.product([0,1],repeat=3)if ([c,not c,1,0][2*a+b])]==[1,2,4,5]
prior=json.loads((E/'prior-library.json').read_text(encoding='utf-8'))['chapters']
for c in prior:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256'],c['topicId']
page=(R/'dist/chapters/g_mux.html').read_text(encoding='utf-8')
assert page.count('class="exam-question"')==82 and page.count('class="review-rule"')==80
assert not re.search('[\u0600-\u06ff]',page)and '$'not in page
sys_path=B/'exam-rewrite';import sys;sys.path.insert(0,str(sys_path))
from math_fences import delimiter_issues,closing_script_bases
issues=[]
maths=re.findall(r'<math\b.*?</math>',page,re.S)
for m in maths:
 root=ET.fromstring(m)
 issues.extend(delimiter_issues(root))
 issues.extend(closing_script_bases(root))
assert not issues,issues
result.update(status='passed',retainedPages=len(prior),questions=82,rules=80,mathExpressions=len(maths),authenticAnswers='Both independently rederived; Q82 enumerated over all sixteen inputs',limitations='Bounded logical cases; no analog, HDL compilation, arbitrary four-valued simulation, or unseen-exam guarantee.')
(E/'mathematics.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
