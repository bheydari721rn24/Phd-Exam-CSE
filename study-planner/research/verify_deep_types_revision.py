from pathlib import Path
import ast,hashlib,json,re,subprocess,tempfile,xml.etree.ElementTree as ET
from decimal import Decimal,localcontext,ROUND_HALF_EVEN
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='44c760435cb24a1f7eaafac9bfb15905c818e305';checks=[]
def check(label,value):assert value,label;checks.append(dict(name=label,passed=True))
for n in range(1,65):
 w=n+3;M=2**w;check('unsigned geometric range '+str(n),sum(2**j for j in range(w))==M-1);check('register residue '+str(n),(M-1+n+1)%M==n and n<M)
 check('signed endpoints '+str(n),-2**(n-1)+(2**(n-1)-1)==-1)
 off=4*((n+3)//4);check('minimum record '+str(n),off>=n and off%4==0 and off-n<4 and (off+4)%4==0)
 count=n*(n+1);check('array last-byte reconstruction '+str(n),4*((n-1)*(n+1)+n)+3==4*count-1)
 q,r=divmod(n,8);size=q+int(r!=0);check('packing minimality '+str(n),8*size>=n and 8*(size-1)<n)
 p=n;check('consecutive endpoint binade '+str(n),2**(p-p+1)==2 and (2**p+1)%2==1)
 a=-(3*n+1);q=-n;r=a-3*q;check('truncating quotient identity '+str(n),r==-1 and abs(r)<3 and abs(a)//3==n)
for x in range(256):check('promoted complement destinations '+str(x),(-x-1)%256==255-x and (-x-1)%(2**32)==2**32-x-1)
with localcontext() as c:
 c.prec=5;c.rounding=ROUND_HALF_EVEN;a=Decimal('341.27');b=Decimal('81.316');d=Decimal('12.417');left=(a+b)+d;right=a+(b+d);check('authentic decimal operation trees',left==Decimal('435.01') and right==Decimal('435.00') and left-right==Decimal('.01'))
check('uint16 intermediate square',65535**2==4294836225 and 65535**2>2**31-1)
check('int32 safe parameter ceiling',3*715827882+1==2**31-1 and 3*715827883+1>2**31-1)
check('representable final invalid intermediate',2*1073741824>2**31-1 and -(2*1073741824)==-2**31)
check('two binary64 midpoint parities',(2**52)%2==0 and (2**52+1)%2==1 and (2**52+2)%2==0)
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
page=(R/'dist/chapters/p_types.html').read_text();old=subprocess.check_output(['git','show',BASE+':dist/chapters/p_types.html']).decode();qs=ns['questions'](page);oq=ns['questions'](old);rev=json.loads((E/'p_types-revision.json').read_text());check('all45 question placements retained',len(qs)==len(oq)==45)
for i,((_,_,attrs,q),(_,_,oa,o),record) in enumerate(zip(qs,oq,rev['records']),1):
 key=int(oa['data-answer']) if oa.get('data-answer') else int(re.search(r'Correct option:\s*(\d+)',ns['plain'](o))[1]);check('unchanged exact answer '+str(i),key==record['answer']==int(attrs['data-answer']))
 check('full mathematical answer '+str(i),record['words']>=200 and '<math' in q[q.index('<details'):])
 if 24<=i<=27:check('minimum ABI explicit '+str(i),'no discretionary padding' in ns['plain'](q))
 if 40<=i<=43:check('every evaluated intermediate required '+str(i),'every evaluated intermediate' in ns['plain'](q))
 if i>=4:check('no false source calibration '+str(i),'Pattern reference:' not in ns['plain'](q))
check('Q1 carry repaired','option 3 has an unsigned carry' in ns['plain'](qs[0][3]))
for i in range(20,24):check('promotion before negation '+str(i),'signed char negative128' in ns['plain'](qs[i-1][3]))
for formula in re.findall(r'<math\b[\s\S]*?</math>',page):
 e=ET.fromstring(formula)
 for c in e.iter():
  tag=c.tag.split('}')[-1]
  if tag in ['msup','msub','msubsup']:check('script base '+str(len(checks)),list(c)[0].text not in [')',']','}'])
check('native nonempty formulas',page.count('<math')>=850)
oldlesson=old[old.index('<h2 id="values">'):old.index('<h2 id="worked-problems">')];newlesson=page[page.index('<h2 id="values">'):page.index('<h2 id="mathematical-bridge">')]
for title in re.findall(r'<h3>Tutorial [\s\S]*?</h3>',oldlesson):check('retained tutorial '+ns['plain'](title),title in newlesson)
check('retained tutorial count',len(re.findall(r'<h3>Tutorial ',newlesson))==36)
sc=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes'];models={k:v for k,v in sc.items() if k.startswith('types-question-')};check('21 distinct scoped models',len(models)==21)
for name,v in models.items():
 for i,f in enumerate(v['frames']):
  ET.fromstring(f['formulaHtml'].replace('<div class="formula-block">','').replace('</div>',''));s=f['snapshot'];k=s['kind']
  if k=='adder':check(name+str(i),(s['a']+s['b']==s['total']) and s['overflow']==(s['carryin']!=s['carryout']) and s['bits'][2]==format(s['total']%16,'04b'))
  elif k=='layout':check(name+str(i),s['offset']==4*((s['n']+3)//4) and s['size']==s['offset']+4)
  elif k=='packed':check(name+str(i),s['size']==(s['n']+7)//8)
check('no literal perfection claim in rewritten exposition','100% accuracy' not in (E/'p_types-method-instruction.md').read_text())
report=dict(topicId='p_types',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,pageSha256=hashlib.sha256(page.encode()).hexdigest(),limits='Finite exact arithmetic checks complement recorded general proofs and independent source review; they do not certify all unseen questions or all worldwide courses.')
(E/'p_types-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'checks':len(checks),'status':report['status']})
