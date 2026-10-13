from pathlib import Path
from itertools import product
import math,json,re,sys,subprocess,hashlib,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';count=0
def check(v):
 global count
 assert v;count+=1
N=lambda a,b:1-a*b
for x,y,z in product((0,1),repeat=3):
 t=N(x,y);u=N(x,t);v=N(y,t);check(N(u,v)==x^y);check(N(v,v)==(1-x)*y);check(N(N(t,t),z)==1-x*y*z)
 check(N(t,t)==x*y);check(1-((1-(x|y))|(1-(x|z))|(1-(y|z)))==int(x+y+z>=2));check(x*y*z+(1-x|1-y|1-z)==1)
for a,b,c,d in product((0,1),repeat=4):
 check(((a*b*c)|(a*b*d)|(a*c*d)|(b*c*d))==int(a+b+c+d>=3));check((a|b)*(a|c)*(a|d)*(b|c)*(b|d)*(c|d)==int(a+b+c+d>=3))
bits=list(product((0,1),repeat=3));target=[1-math.prod(v)for v in bits];possible=set()
for i,j in product(range(3),repeat=2):
 first=[N(v[i],v[j])for v in bits]
 for k,l in product(range(4),repeat=2):possible.add(tuple(N((list(v)+[t])[k],(list(v)+[t])[l])for v,t in zip(bits,first)))
check(tuple(target)not in possible)
for n in range(1,9):
 check(sum(2**(n-k)for k in range(1,n+1))==2**n-1);check(sum(2 for _ in range(n))==2*n);check(sum(4 for _ in range(n))==4*n);check(max([2*(k-1)+3 for k in range(1,n+1)]+[2*n])==2*n+1)
for s in [1.1,1.2,2,5,8,100]:
 cases=[(.5,4),(3,1),(2,.2)];old=max(i+l for i,l in cases);new=max(i+l/s for i,l in cases);check(old/s<new<old)
check(max(.5+4,3+1)==4.5);check(max(.5+4/2,3+1/2)==3.5);check(abs(.5+4/1.2-3-1/1.2)<1e-12);check(max(.5+4/5,3+1/5)==3.2)
check(2000*5+3000*(4+6)==40000);check(1000*10+1500*(8+6)==31000);check(22000+18000/2==31000)
for q in [.01,.2,.5,.75,.99]:
 t=-math.log(1-q);check(abs(1-math.exp(-t)-q)<1e-12);t=-math.log(q);check(abs(math.exp(-t)-q)<1e-12)
check(abs(.5*.8**2*2-.64)<1e-12);check(abs((4.2-3)-1.2)<1e-12);check(abs((.9-.3)-.6)<1e-12);check(abs(min(2.4-2,.7-.2)-.4)<1e-12)
models=json.loads((E/'g_gates-models.json').read_text());check(len(models)==32)
for model in models.values():
 for f in model['frames']:
  s=f['snapshot'];k=s['kind']
  if k=='nand':check(s['t']==N(s['x'],s['y']));check(s['u']==N(s['x'],s['t']));check(s['v']==N(s['y'],s['t']));check(s['f1']==s['x']^s['y']);check(s['f2']==(1-s['x'])*s['y'])
  if k=='mux':check(s['out']==(1-s['a'])*(1-s['b']))
  if k=='positive-and':check(s['t']==N(s['x'],s['y']));check(s['out']==s['x']*s['y'])
  if k=='majority':check(s['u']==1-(s['x']|s['y']));check(s['v']==1-(s['x']|s['z']));check(s['w']==1-(s['y']|s['z']));check(s['out']==int(s['x']+s['y']+s['z']>=2))
  if k=='cmos':v=s.get('inputs',[s.get('x'),s.get('y')]);check(s['down']==math.prod(v));check(s['up']==1-s['down']);check(s['out']==s['up'])
  if k=='ring':
   n,tau,T,t=s['n'],s['tau'],s['T'],s['time'];check(T==2*n*tau);prev=[int(((t-tau-i*tau)%T)<n*tau)^(i%2)for i in range(n)]
   for i,q in enumerate(s['q']):check(q==1-prev[(i-1)%n])
   check(s['q']==[int(((t+T-i*tau)%T)<n*tau)^(i%2)for i in range(n)])
  if k=='sizing':check(s['maxCase']==max(range(2),key=lambda i:sum(s['cases'][i])))
  if k=='wave':check(s['signals'][3]==[int(not(s['lo']<=t<s['hi']))for t in s['times']]);check(all(v==1 for v in s['signals'][4]));check(s['hi']-s['lo']in[3,5])
  if k=='table':check(all(len(r)==len(s['headings'])for r in s['rows']));check(all(len(r)==len(s['headings'])for r in s['rowsHtml']))
  if k=='rc':check(abs(1-math.exp(-s['cross'])-s['q'])<1e-12)
  for m in re.findall(r'<math\b[\s\S]*?</math>',f['formulaHtml']):ET.fromstring(m)
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/g_gates.html').read_text()
for m in re.findall(r'<math\b[\s\S]*?</math>',page):
 root=ET.fromstring(m);check(not closing_script_bases(root));check(not delimiter_issues(root));check(not re.search(r'\\[A-Za-z]', ''.join(root.itertext())))
from read_gates_bank import ns,rows
qs=ns['questions'](page);check(len(qs)==46)
for i,(_,_,a,q)in enumerate(qs):check(q.count('class="exam-option"')==4);check(int(re.search(r'Correct option:\s*(\d+)',ns['plain'](q))[1])==rows[i]['answer']);check('$'not in q);check('separate teaching example'not in q)
base=subprocess.check_output(['git','show','6dc081117f8724d4eb940e959073eb30e3577727:dist/chapters/g_gates.html']).decode();titles=lambda s:re.findall(r'<h3[^>]*>Problem [\s\S]*?</h3>',s)
check(len(titles(page))==36);check(titles(page)==titles(base));check('student-approved'not in page.lower())
src=json.loads((E/'g_gates-course-recheck.json').read_text());check(src['universityCountActuallyReadInThisRevision']==4)
pdf=Path(r'C:/Users/bheydari/Desktop/Phd-Exam-CSE/Exams/MS/CE/1404/Daftarche-Soalat-Konkur-Arshad-Computer-1404 (konkurcomputer.ir).pdf');check(hashlib.sha256(pdf.read_bytes()).hexdigest()=='909e4efaaad96f4d39e526104bc9dc6de6d52be11fd7716e583476b0e62ff654')
old=json.loads((B/'g_gates-verification.json').read_text());report=dict(topicId='g_gates',status='passed_with_recorded_finite_bounds',checkCount=count,retainedLessonAssertions=old['assertions'],pageSha256=hashlib.sha256(page.encode()).hexdigest(),models=len(models),frames=sum(len(m['frames'])for m in models.values()),sourceReview='g_gates-course-recheck.json',scope='All eight three-input states; all sixteen four-input voter states; all two-NAND topologies on three primaries; listed width scales and RC identities; every saved model state; complete native mathematics and retained tutorial titles.',limits='Finite logical and specified timing/RC models, not physical circuit certification or universal examination performance.')
(E/'g_gates-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
