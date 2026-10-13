from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext,ROUND_HALF_EVEN
import ast,hashlib,json,re,subprocess,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def signed(u,w):return u-(1<<w) if u>=(1<<(w-1)) else u
for w in range(1,8):
 M=1<<w
 for a in range(M):
  for b in range(M):
   exact=signed(a,w)+signed(b,w);r=(a+b)%M;c=0;cin=0
   for i in range(w):
    if i==w-1:cin=c
    c=(((a>>i)&1)+((b>>i)&1)+c)//2
   v=not -M//2<=exact<M//2
   check(f'carry/overflow:w{w},a{a},b{b}',c==int(a+b>=M) and bool(cin^c)==v and signed(r,w)==exact-(cin-c)*M)
 for a in range(M):
  for m in range(1,w):
   t=signed(a,w);new=signed(a%(1<<m),m);bit=(a>>(m-1))&1;discard=a>>m
   criterion=discard==(1<<(w-m))-1 if bit else discard==0
   check(f'narrow:w{w},u{a},to{m}',(new==t)==criterion)
for a in range(10):
 for b in range(10):
  for cin in [0,1]:
   t=a+b+cin;low=t%16;binaryCarry=t//16;correct=binaryCarry or low>9;r=t+6 if correct else t
   check(f'BCD:{a}+{b}+{cin}',r%16==t%10 and int(bool(correct))==t//10)
for w in range(1,11):
 gray=[i^(i>>1) for i in range(1<<w)];check(f'Gray bijection{w}',len(set(gray))==1<<w)
 for i,g in enumerate(gray):
  n=g;b=0
  while n:b^=n;n>>=1
  check(f'Gray prefix{w}:{i}',b==i and (g^gray[(i+1)%len(gray)]).bit_count()==1)
def synd(v):return [sum(v[j-1] for j in range(1,8) if j&(1<<k))%2 for k in range(3)]
for data in range(16):
 v=[0]*7
 for j,bit in zip([3,5,6,7],format(data,'04b')):v[j-1]=int(bit)
 for pos,k in [(1,0),(2,1),(4,2)]:v[pos-1]=sum(v[j-1] for j in range(1,8) if j&(1<<k))%2
 check(f'Hamming parity{data}',synd(v)==[0,0,0])
 for j in range(1,8):
  r=v.copy();r[j-1]^=1;s=synd(r);index=s[0]+2*s[1]+4*s[2];r[index-1]^=1;check(f'Hamming repair{data}:{j}',index==j and r==v)
 for a in range(8):
  for b in range(a+1,8):
   r=v+[sum(v)%2];r[a]^=1;r[b]^=1;check(f'SECDED double{data}:{a},{b}',sum(r)%2==0 and synd(r[:7])!=[0,0,0])
with localcontext() as ctx:
 ctx.prec=30
 def round5(x):return x.quantize(Decimal(1).scaleb(x.adjusted()-4),rounding=ROUND_HALF_EVEN)
 a,b,c=map(Decimal,['341.27','81.316','12.417']);A=round5(round5(a+b)+c);C=round5(a+round5(b+c));check('original decimal nodes',A==Decimal('435.01') and C==Decimal('435.00') and A-C==Decimal('.01'))
for n in range(4,40):check(f'normal field domain{n}',1<=n-3<(1<<n)-1 and (n-3)-((1<<(n-1))-1)==n-2-(1<<(n-1)))
for n in range(1,40):
 check(f'fixed unit{n}',F(3*(1<<n)+1,1<<n)==3+F(1,1<<n))
 check(f'finite ones{n}',sum((F(1,1<<i) for i in range(1,n+1)),F(0))==1-F(1,1<<n))
 check(f'hex capacity{n}',16**n==2**(4*n))
 if n>=3:check(f'negative word{n}',signed((1<<n)-3,n)==-3)
 if n>=2:check(f'maximum sum{n}',signed((1<<n)-2,n)==-2)
check('unsigned exact product nearest-even',round(F(600,16))==38 and F(38,16)-F(600,256)==F(1,32))
check('signed product nearest-even',round(F(-30,4))==-8 and F(-8,4)==-2)
check('unsigned quarter tie',round(F(13,2))==6)
check('transfer1 incompatible radix',2*8+3==19 and (8+3)**2==8**2+6*8+9 and 9>=8)
check('transfer2 base-six digits',F(2,36)+F(3,216)==F(5,72) and F(5,72)*216==15)
check('transfer2 binary period',all(pow(2,k,9)!=1 for k in range(1,6)) and pow(2,6,9)==1 and F(35,63*8)==F(5,72))
check('transfer3 signed endpoint and zero',22+25==47 and 47%32+47//32==16 and 16-31==-15 and 16+15==31)
check('transfer4 width pipelines',signed(180,8)==-76 and signed(90%16,4)==-6 and signed((10+10)%16,4)==4)
check('transfer5 negative shift',227>>3==28 and -29//8==-4 and int(F(-29,8))==-3 and (-29+7)//8==-3)
check('transfer6 format',F(1023,64)<20<=F(2047,64) and (1<<4)<12+4+1 and (1<<5)>=12+5+1 and format(3884,'012b')=='111100101100' and F(3884-4096,64)==F(-53,16))
triples=[a+b+c for a in range(10) for b in range(10) for c in [0,1]]
check('transfer7 counted correction families',sum(t>=10 for t in triples)==100 and sum(t>=16 for t in triples)==16 and 48+57+1==106)
check('transfer8 Gray sum',19^(19>>1)==26 and 22^(22>>1)==29 and 9^(9>>1)==13 and 41^(41>>1)==61)
check('transfer9 same syndrome distinct parity',synd([int(x) for x in '1100110'])==[0,0,0] and synd([int(x) for x in '1100111'])==[1,1,1] and sum(map(int,'11001110'))%2==1 and sum(map(int,'11001111'))%2==0)
check('transfer10 false valid correction',synd([int(x) for x in '1101000'])==[1,1,1] and sum(map(int,'11010000'))%2==1 and synd([int(x) for x in '1101001'])==[0,0,0] and sum(map(int,'11010010'))%2==0)
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'helpers','exec'),ns)
page=(R/'dist/chapters/g_number.html').read_text();rev=json.loads((E/'g_number-revision.json').read_text());questions=ns['questions'](page);check('45completeentries',len(questions)==45)
for i,(_,_,attrs,q) in enumerate(questions,1):
 key=int(re.search(r'Correct option:\s*(\d+)',ns['plain'](q))[1]);check('answer record'+str(i),key==rev['records'][i-1]['answer']==int(attrs['data-answer']))
 check('full written proof'+str(i),rev['records'][i-1]['words']>=200 and '<math' in q[q.index('<details'):])
 if i>3:check('authored provenance'+str(i),'Pattern reference:' not in ns['plain'](q))
for i,math in enumerate(re.findall(r'<math\b[\s\S]*?</math>',page)):
 e=ET.fromstring(math)
 depth=0
 for mo in (x for x in e.iter() if x.tag.split('}')[-1]=='mo'):
  if mo.text in ['(','[','{']:depth+=1
  elif mo.text in [')',']','}']:depth-=1;check('nonnegative delimiter depth'+str(i),depth>=0)
 check('closed mathematical delimiters'+str(i),depth==0)
 for x in e.iter():
  if x.tag.split('}')[-1] in ['msup','msub','msubsup']:check('native script'+str(i),list(x)[0].text not in [')',']','}'])
models=json.loads((E/'g_number-models.json').read_text());check('28distinctmodels',len(models)==28)
for name,model in models.items():
 for i,f in enumerate(model['frames']):
  ET.fromstring(f['formulaHtml'].replace('<div class="formula-block">','').replace('</div>',''));s=f['snapshot'];kind=s['kind']
  if kind=='adder':check(name+str(i),s['stored']==(s['a']+s['b'])%(1<<s['w']) and s['signedResult']==signed(s['stored'],s['w']) and s['overflow']==int(not -(1<<(s['w']-1))<=s['exact']<(1<<(s['w']-1))))
  elif kind=='quant':
   if s['mode']=='nearest-even':check(name+str(i),round(F(s['scaled']))==s['chosen'])
   check(name+str(i)+'decoded',F(s['lowReal'])==s['low']*F(s['unit']) and F(s['highReal'])==s['high']*F(s['unit']) and F(s['error'])==s['chosen']*F(s['unit'])-F(s['target']))
  elif kind=='hamming' and s['stage']:
   word=s['received'] if s['stage'] in [2,3] else s['word'];check(name+str(i),synd([int(x) for x in word])==s['syndrome'])
old=subprocess.check_output(['git','show',rev['baselineCommit']+':dist/chapters/g_number.html']).decode();stop=old.index('<h2 id="worked-problems">')
for title in re.findall(r'<h3>Problem [\s\S]*?</h3>',old[:stop]):check('retained tutorial'+ns['plain'](title),title in page)
check('no stale archive deferral','Archived Iranian entrance-exam questions remain reserved' not in page)
report=dict(topicId='g_number',status='passed_with_recorded_finite_bounds',reviewer='root',checkCount=len(checks),pageSha256=hashlib.sha256(page.encode()).hexdigest(),scopes=['All signed/unsigned adder input pairs through7 bits','All narrower signed targets through7 bits','All BCD input digit/carry triples','Every reflected Gray index through10 bits','All Hamming data/single errors and SECDED double-error pairs','Exact canonical decimal and fixed-point calculations','Every question key/complete solution/native math and named model arithmetic'],limits='These finite checks complement the written general derivations. The interrupted independent research tasks are not claimed completed peer audits. Rendered inspection remains a separate gate.')
(E/'g_number-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'checks':len(checks),'status':report['status']})
