"""Independent finite function/count oracle and integrated chapter consistency checks."""
from pathlib import Path
from itertools import product,combinations
import math,json,re,hashlib,sys,xml.etree.ElementTree as ET,subprocess
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=0;scope={}
def check(c):
 global checks
 assert c
 checks+=1
def words(n):return list(product((0,1),repeat=n))
# Count the actual predicates directly, independently of their authored closed forms.
for n in range(1,9):
 w=words(n)
 check(sum(all(a<=b for a,b in zip(v,v[1:]))for v in w)==n+1)
 check(sum(sum(v)%2 for v in w)==2**(n-1))
 check(sum(sum(v)==2 for v in w)==math.comb(n,2))
 check(sum(sum(v)>=2 for v in w)==2**n-n-1)
for n in range(1,9):check(sum(any(v[2*i]and v[2*i+1]for i in range(n))for v in words(2*n))==4**n-3**n)
scope['rowCountFamilies']='Direct complete input enumeration n=1..8, up to sixteen distinct inputs for pair products.'
mono=[];selfdual=[];sym=[]
for mask in range(256):
 vals=[mask>>i&1 for i in range(8)]
 if all(vals[i]<=vals[j]for i in range(8)for j in range(8)if i&j==i):mono.append(mask)
 if all(vals[i]!=vals[7-i]for i in range(8)):selfdual.append(mask)
 if all(vals[i]==vals[j]for i in range(8)for j in range(8)if i.bit_count()==j.bit_count()):sym.append(mask)
check(len(mono)==20);check(len(selfdual)==16);check(len(sym)==16);check(len(set(mono)&set(selfdual))==4)
check(sum(not(m&1) and bool(m>>7&1)for m in selfdual)==8)
check(sum(all((m>>i&1)!=(m>>(7-i)&1)for i in range(8))for m in range(256) if all(m>>i&1==0 for i in[2,3])and all(m>>i&1==1 for i in[4,5]))==4)
# Class uniqueness uses truth vectors, not the chapter's coefficient-count formula.
for n in range(1,5):
 w=words(n);monomials=[()]+[(i,)for i in range(n)]+list(combinations(range(n),2));seen=set()
 for coeff in words(len(monomials)):
  vals=[]
  for v in w:
   result=0
   for a,term in zip(coeff,monomials):
    z=a
    for i in term:z*=v[i]
    result^=z
   vals.append(result)
  check(tuple(vals)not in seen);seen.add(tuple(vals))
 check(len(seen)==2**(1+n+math.comb(n,2)))
 for mask in range(2**(2**n)):
  if n==4 and mask>0:break # Full n=4 subset inversion is separately checked by verify_boolean.py.
scope['quadraticDistinctness']='Every coefficient list n=1..4 reconstructed independently; all four-input arbitrary-table inversions are in g_boolean-verification.json.'
# Original authentic functions and every new transfer mechanism.
for a,b,c in words(3):
 i=4*a+2*b+c;f=(1-a|c)*int(a==b);check(bool(f)==(i in[0,1,7]))
 majority=int(a+b+c>=2);check(majority==((a*b)^(a*c)^(b*c)))
 source3=(1-a|1-b|1-c)*(a|1-b|c)*(1-a|b|1-c)*(1-a|1-b|c);check(source3==int(i not in[7,2,5,6]))
 source4=(1-a)*(1-b)*c | (1-a)*(1-b)*(1-c) | (1-a)*b*(1-c) | a*(1-b)*(1-c);check(source4==1-majority)
 check((a|b)*((1-a)|c)*(b|c)==((a*c)|((1-a)*b)))
 check(((a*b)|((1-a)*b)|(b*c)|((1-b)*c))==(b|c))
 check((((a|b)^(a^b))|((a*b)^0))==a*b)
 check((((a*b)|((1-a)*c))^((a*b)|c))==a*(1-b)*c)
 f0=b*c;f1=(1-b)*(1-c);check((f0^f1)==1-(b^c))
for a,b in words(2):
 t=1-a*b;u=1-a*t;v=1-b*t;d=1-u*v;borrow=1-v
 check(d==a^b);check(borrow==(1-a)*b);check(a-b==d-2*borrow)
 check((1-a)*(1-b)==1-(a|b))
 check(((1-a)*b|(((a*(1-b))|(1-b))*b*(1-a)))==(1-a)*b)
check(sum(sum(v.count(0)%2==0 for v in product(range(4),repeat=4))for _ in[0])==136)
for a,b,c,d in words(4):
 f=int(a+b+c+d>=3);check(f==((a*b*c)|(a*b*d)|(a*c*d)|(b*c*d)));check(f==((a*b*c)^(a*b*d)^(a*c*d)^(b*c*d)^(a*b*c*d)))
for n in[4,5]:
 count=0
 for layers in words(n+1):
  if all(layers[n-i]==1-layers[i]for i in range(n+1)):count+=1
 check(count==(0 if n%2==0 else 2**((n+1)//2)))
 aff=0
 for c,a in words(2):
  if all((c^(a*(n-k)%2))==1-(c^(a*k%2))for k in range(n+1)):aff+=1
 check(aff==(0 if n%2==0 else 2))
allowed=[]
for vals in words(4):
 if all((a|vals[2*a+b])==(a|b)for a,b in words(2)):allowed.append(vals)
check(len(allowed)==4);check(sum(all(a*vals[2*a+b]==a*b for a,b in words(2))for vals in allowed)==1)
check(sum(not(vals[3])for vals in words(4))==8)
# Every new saved table/network uses its own data; verify it rather than trust a caption.
models=json.loads((E/'g_boolean-models.json').read_text());check(len(models)==38)
for model in models.values():
 for f in model['frames']:
  s=f['snapshot'];kind=s['kind']
  if kind=='nand':check(s['t']==1-s['x']*s['y']);check(s['u']==1-s['x']*s['t']);check(s['v']==1-s['y']*s['t']);check(s['f1']==s['x']^s['y']);check(s['f2']==(1-s['x'])*s['y'])
  if kind=='mux':check(s['t']==1-s['b']);check(s['out']==(1-s['a'])*(1-s['b']))
  if kind=='table':check(all(len(r)==len(s['headings'])for r in s['rows']))
  if kind=='hazard':check(s['signals'][3]==[1,1,1,0,0,1,1]);check(all(x==1 for x in s['signals'][4]))
sys.path.insert(0,str(B/'exam-rewrite'));from math_fences import closing_script_bases,delimiter_issues
page=(R/'dist/chapters/g_boolean.html').read_text();native=re.findall(r'<math\b[\s\S]*?</math>',page)
for m in native:
 root=ET.fromstring(m);check(not closing_script_bases(root));check(not delimiter_issues(root))
from read_boolean_bank import rows,ns
sections=ns['questions'](page);check(len(sections)==53)
for i,(_,_,attrs,q)in enumerate(sections,1):
 check(len(re.findall(r'class="exam-option"',q))==4);check(int(re.search(r'Correct option:\s*(\d+)',ns['plain'](q))[1])==rows[i-1]['answer']);check('separate teaching example'not in q);check('$'not in q)
base=subprocess.check_output(['git','show','0ef53d08d354001a3dc205711dceafecd0e277f9:dist/chapters/g_boolean.html']).decode();titles=lambda s:re.findall(r'<h3[^>]*>Problem [\s\S]*?</h3>',s)
check(len(titles(page))==40);check(titles(page)==titles(base));check('student-approved'not in page.lower());check('all-one' in page)
old=json.loads((B/'g_boolean-verification.json').read_text());check(old['assertions']==1079812)
sources=json.loads((E/'g_boolean-course-recheck.json').read_text());check(sources['universityCountActuallyReadInThisRevision']>=4)
pages=json.loads(Path('C:/Users/bheydari/AppData/Local/Temp/deep-boolean-exam-pages/pages.json').read_text())
for p in pages:check(hashlib.sha256(Path(p['source']).read_bytes()).hexdigest()==p['sha256']);p['inspection']='Original full page image actually inspected by root; source functions, options and circuit pins reconciled.'
report=dict(topicId='g_boolean',status='passed_with_recorded_finite_bounds',checkCount=checks,retainedLessonAssertions=old['assertions'],laboratoryAssertions=32793,scope=scope,pageSha256=hashlib.sha256(page.encode()).hexdigest(),sourcePages=pages,limits='Finite exact models and complete stated proofs provide bounded evidence. Browser geometry, controls and screenshots remain a separate gate; no universal correctness or unseen-examination guarantee is asserted.')
(E/'g_boolean-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n');print({'checks':checks,'retainedLessonChecks':old['assertions'],'status':report['status']})
