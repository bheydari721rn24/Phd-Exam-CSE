from pathlib import Path
from itertools import combinations
from xml.etree import ElementTree as ET
import re,json,hashlib,subprocess,sys
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=0
def ck(v,label=''):
 global checks
 assert v,label;checks+=1
def summary(a):return[sum(a),max(sum(a[:j])for j in range(1,len(a)+1)),max(sum(a[i:])for i in range(len(a))),max(sum(a[i:j])for i in range(len(a))for j in range(i+1,len(a)+1))]
scenes={k:s for k,s in json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'].items()if k.startswith('divide-question-')};ck(len(scenes)==64)
for key,s in scenes.items():
 for frame in s['frames']:
  ET.fromstring(frame['formulaHtml']);d=frame['snapshot'];k=d['kind']
  if k=='merge':
   ck(d['output']==sorted(d['left'][:d['i']]+d['right'][:d['j']]),key);ck(d['charge']==sum(x>y for x in d['left']for y in d['right'][:d['j']]),key);ck(d['comparisons']<=len(d['left'])+len(d['right'])-1,key)
  elif k=='summary':
   a=d['input'];m=d['split'];ck(d['left']==summary(a[:m])and d['right']==summary(a[m:])and d['combined']==summary(a),key);w=min((-sum(a[i:j]),i,j)for i in range(len(a))for j in range(i+1,len(a)+1));ck(d['witness']==list(w[1:]),key)
  elif k=='radix':
   h,l,u,v=d['parts'];z2,z0,zs,z1=d['products'];ck(z2==h*u and z0==l*v and zs==(h+l)*(u+v)and z1==h*v+l*u);ck(abs(d['x']*d['y'])==z2*d['base']**2+z1*d['base']+z0)
  elif k=='blocks':ck(d['products']==[65,35,-2,8,24,22,-30]and d['outputs']==[19,22,43,50])
  elif k=='geometry':
   p=d['points'];dist=lambda i,j:(p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2
   ck(min(dist(i,j)for i,j in combinations(range(3),2))==5);ck(min(dist(i,j)for i,j in combinations(range(3,6),2))==5);ck(d['best']>=min(dist(i,j)for i,j in combinations(range(6),2)));ck(d['order']==sorted(range(6),key=lambda i:(p[i][1],i)))
  elif k=='butterfly':
   ck(d['output']==[sum(v*pow(4,j*i,17)for j,v in enumerate([1,2,0,0]))%17 for i in range(4)]);ck(pow(4,2,17)==16 and pow(4,4,17)==1)
  elif k=='convolution':
   a=d['inputA'];b=d['inputB'];coeff=[sum(a[i]*b[k-i]for i in range(len(a))if 0<=k-i<len(b))for k in range(len(a)+len(b)-1)];ck(d['values']==coeff);ck(d['accum']==[sum(coeff[i]for i in range(d['stage'])if i%d['N']==j)for j in range(d['N'])])
  elif k=='groups':
   gs=d['groups'];flat=sum(gs,[]);ck(len(flat)==len(set(flat)));ck(sorted(sorted(g)[2]for g in gs)[len(gs)//2]==0);ck(sum(v<0 for v in flat)==3*d['t']+2);ck(d['smaller']==sum(v<0 for g in gs[:d['stage']]for v in g))
  elif k=='search':ck(0<=d['lo']<=d['hi']<=d['N']);ck(d['inspections']==d['calls']-(d['mid']is None));ck(d['mid'] is None if d['lo']==d['hi']else d['mid']==(d['lo']+d['hi'])//2)
  elif k=='levels':
   j=d['depth'];ck(d['count']==d['a']**j and d['size']*d['b']**j==d['N']);measure=d['measure']
   if measure=='merge':ck(d['value']==d['h']*d['N']-d['N']+1)
   if measure=='leaves':ck(d['value']==d['a']**d['h'] and d['local']==(1 if j==d['h']else 0))
   if measure=='fft':ck(d['value']==d['h']*d['N']//2 and d['local']*d['count']==(d['N']//2 if j<d['h']else 0))
  elif k=='table':ck(all(len(r)==len(d['headings'])for r in d['rows']))
  else:raise AssertionError(k)
page=(R/'dist/chapters/a_divide.html').read_text();base=subprocess.check_output(['git','show','0cf6fb27e8d200bd1c49f2e22f6689dc84308e3b:dist/chapters/a_divide.html']).decode().replace('\r\n','\n')
from space_number_prose import fix
base=fix(base);tutorials=lambda p:re.findall(r'<h3[^>]*>Tutorial [\s\S]*?(?=<h3|<h2)',p)
ck(len(tutorials(page))==48);ck(tutorials(page)==tutorials(base),'All complete tutorials must remain unchanged')
sourceLesson=lambda p:p[p.index('<h2 id="design">'):p.index('<h2 id="proof-tutorials">')]
# Original lesson is retained before the newly added bridge; only one local scene identifier is replaced.
old=sourceLesson(base).replace('data-scenes="merge-recursion,merge"','data-scenes="merge-recursion,divide-question-q3"');new=sourceLesson(page).split('<h2 id="mathematical-bridge">')[0];withoutSvg=lambda p:re.sub(r'<svg\b[\s\S]*?</svg>','[separately audited diagram]',p);ck(withoutSvg(new)==withoutSvg(old),'Full original lesson and methods retained; six diagrams receive separate typography and port repairs')
maths=re.findall(r'<math\b[\s\S]*?</math>',page)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import delimiter_issues,closing_script_bases
for m in maths:
 root=ET.fromstring(m);ck(not delimiter_issues(root)and not closing_script_bases(root),'Math delimiters')
ck(len(re.findall(r'data-deep-index="\d+"',page))==46);ck(len(re.findall(r'<h3>Decision \d+\.',page))==40);ck(len(re.findall(r'<h3>Challenge \d+\.',page))==10)
(E/'a_divide-mathematical-checks.json').write_text(json.dumps(dict(topicId='a_divide',status='passed',assertions=checks,newModels=len(scenes),newModelFrames=sum(len(s['frames'])for s in scenes.values()),nativeExpressions=len(maths),fullOriginalTutorialsRetained=48,fullOriginalLessonRetained=True,pageSha256=hashlib.sha256(page.encode()).hexdigest(),scope='Every new frame, exact numerical examples, full lesson/tutorial retention and document mathematics; browser audit is separate. Answer and synthesis proofs have separate finite-oracle evidence.'),indent=2)+'\n');print(checks,'assertions;',len(maths),'document expressions')
