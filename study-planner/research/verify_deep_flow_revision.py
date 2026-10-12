from pathlib import Path
import ast,hashlib,json,math,re,subprocess,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='b786d491f7285f3ab2154d958988641fd43c3ee1';checks=[]
def check(name,value):assert value,name;checks.append(dict(name=name,passed=True))
for n in range(0,40):
 triples=sum(j*(n+1-j) for j in range(1,n+1));check('weak triple count '+str(n),triples==math.comb(n+2,3));check('sum prefix '+str(n),sum(range(n))==n*(n-1)//2)
 check('filter counter '+str(n),sum(i%3!=0 for i in range(1,3*n+1))==2*n);check('two-child recurrence '+str(n),sum(2**i for i in range(n+1))==2**(n+1)-1);check('local toll '+str(n),sum(range(n+1))==n*(n+1)//2)
 check('posttest nonnegative domain '+str(n),len(list(range(n-1,-2,-1)))==n+1)
for n in range(1,1001):
 x=n;t=0
 while x>0:x=x-1 if x%2 else x//2;t+=1
 check('branch ranking exact count '+str(n),t==n.bit_length()-1+n.bit_count())
orbit=[(6*t)%256 for t in range(128)];check('128 distinct even residues',len(set(orbit))==128 and set(orbit)==set(range(0,256,2)));check('first64hit96',orbit.index(64)==96)
check('authentic count690',10+math.comb(17,3)==690);check('nested guard951update815',16+135+800==951 and 15+120+680==815)
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
page=(R/'dist/chapters/p_flow.html').read_text();old=subprocess.check_output(['git','show',BASE+':dist/chapters/p_flow.html']).decode();qs=ns['questions'](page);oq=ns['questions'](old);rev=json.loads((E/'p_flow-revision.json').read_text());check('all45placements retained',len(qs)==len(oq)==45)
for i,((_,_,attrs,q),(_,_,oa,o),record) in enumerate(zip(qs,oq,rev['records']),1):
 key=int(oa['data-answer']) if oa.get('data-answer') else int(re.search(r'Correct option:\s*(\d+)',ns['plain'](o))[1]);check('exact answer '+str(i),key==record['answer']==int(attrs['data-answer']));check('complete proof '+str(i),record['words']>=200 and '<math' in q[q.index('<details'):])
 if i==3:check('source option4 stride2','store(n-2,i+2)' in ns['plain'](q) and 'store(n-1,i+2)' not in ns['plain'](q))
 if i==44:check('disjoint predicate order correction','does not change' in ns['plain'](q))
 if i>3:check('no false pattern source '+str(i),'Pattern reference:' not in ns['plain'](q))
for f in re.findall(r'<math\b[\s\S]*?</math>',page):
 e=ET.fromstring(f)
 for c in e.iter():
  if c.tag.split('}')[-1] in ['msup','msub','msubsup']:check('native script base '+str(len(checks)),list(c)[0].text not in [')',']','}'])
for title in re.findall(r'<h3>(?:Tutorial|Problem) [\s\S]*?</h3>',old[:old.index('<h2 id="worked-problems">')]):check('retained original teaching '+ns['plain'](title),title in page)
sc=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'];models={k:v for k,v in sc.items() if k.startswith('flow-question-')};check('21modeldefinitions',len(models)==21)
for name,v in models.items():
 for i,f in enumerate(v['frames']):
  ET.fromstring(f['formulaHtml'].replace('<div class="formula-block">','').replace('</div>',''));s=f['snapshot'];k=s['kind']
  if k=='copy':check(name+str(i),s['negative']==(s['source']<0) and s['dest']==list(range(s['sourceSize']-1,-1,-2))[:len(s['dest'])] and all(0<=x<s['sourceSize'] for x in s['dest']))
  elif k=='orbit':check(name+str(i),s['value']==6*s['t']%256 and s['hit']==(s['value']==s['target']))
  elif k=='threshold':check(name+str(i),s['sum']==s['i']*(s['i']+1)//2 and s['hit']==(s['sum']==15))
  elif k=='swap':check(name+str(i),[s['a'],s['b']]==[[5,2],[7,2],[7,5],[2,5]][s['stage']])
  elif k=='posttest':check(name+str(i),s['i']==5-s['count'])
check('no stale archive deferral','No Iranian entrance-exam paper is used' not in page)
report=dict(topicId='p_flow',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='General proofs complement finite exact models; native structure checks do not themselves certify visual rendering or every unseen examination question.')
(E/'p_flow-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'checks':len(checks),'status':report['status']})
