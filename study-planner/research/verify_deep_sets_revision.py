"""Independent finite checks and source/preservation evidence for the sets revision."""
from pathlib import Path
import ast,hashlib,itertools as it,json,math,re,subprocess,tempfile
import xml.etree.ElementTree as ET
import fitz
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';checks=[]
def check(name,got,want):
 assert got==want,(name,got,want)
 checks.append(dict(name=name,result=got,expected=want,passed=True))
def power(A):
 a=list(A);return{frozenset(a[i]for i in range(len(a))if mask>>i&1)for mask in range(1<<len(a))}
empty=frozenset();one=frozenset([empty]);two=frozenset([empty,one]);S=frozenset([empty,one,two])
for name,A in[('Q3 S1',two),('Q3 S2',S)]:
 check(name+' union',frozenset().union(*A),one if A==two else two)
 check(name+' transitivity',all(x<=A for x in A),True)
check('Q10 union proper',frozenset().union(*S)<S,True)
check('Q10 power proper',S<power(S),True)
check('Q4 parity subsets',sum(any((x+y)%2 for x,y in it.combinations(a,2))for a in it.combinations(range(1,11),4)),200)
check('Q4 positive parity count',sum(math.comb(5,j)*math.comb(5,4-j)for j in range(1,4)),200)
for n in range(5):
 U=frozenset(range(n));subs=power(U);pairs=list(it.product(subs,repeat=2));triples=list(it.product(subs,repeat=3))
 check(f'contained pairs n={n}',sum(a<=b for a,b in pairs),3**n)
 check(f'proper-contained pairs n={n}',sum(a<b for a,b in pairs),3**n-2**n)
 check(f'covering pairs n={n}',sum(a|b==U for a,b in pairs),3**n)
 check(f'disjoint pairs n={n}',sum(not a&b for a,b in pairs),3**n)
 check(f'complementary pairs n={n}',sum(not a&b and a|b==U for a,b in pairs),2**n)
 check(f'nonempty proper subsets n={n}',sum(bool(a)and a<U for a in subs),2**n-2 if n else 0)
 check(f'nested triples n={n}',sum(a<=b<=c for a,b,c in triples),4**n)
 check(f'strict triples n={n}',sum(a<b<c for a,b,c in triples),4**n-2*3**n+2**n)
 check(f'nonempty disjoint pairs n={n}',sum(bool(a)and bool(b)and not a&b for a,b in pairs),3**n-2*2**n+1)
 check(f'pairwise-disjoint triples n={n}',sum(not(a&b or a&c or b&c)for a,b,c in triples),4**n)
 check(f'disjoint covers n={n}',sum(not(a&b or a&c or b&c)and a|b|c==U for a,b,c in triples),3**n)
 check(f'empty triple intersection n={n}',sum(not a&b&c for a,b,c in triples),7**n)
 check(f'nonempty disjoint triples n={n}',sum(bool(a)and bool(b)and bool(c)and not(a&b or a&c or b&c)for a,b,c in triples),4**n-3*3**n+3*2**n-1)
 check(f'nonempty disjoint covers n={n}',sum(bool(a)and bool(b)and bool(c)and not(a&b or a&c or b&c)and a|b|c==U for a,b,c in triples),3**n-3*2**n+3 if n else 0)
 cover={frozenset([a,b])for a,b in pairs if a|b==U}
 check(f'unordered covering pairs n={n}',len(cover),(3**n+1)//2)
 check(f'unordered complements n={n}',len({frozenset([a,b])for a,b in pairs if not a&b and a|b==U}),2**(n-1)if n else 1)
 for D in subs:
  check(f'fixed symmetric difference n={n} D={sorted(D)}',sum(a^b==D for a,b in pairs),2**n)
  check(f'fixed intersection n={n} I={sorted(D)}',sum(a&b==D for a,b in pairs),3**(n-len(D)))
 check(f'power intersection n={n}',all(power(a)&power(b)==power(a&b)for a,b in pairs),True)
 check(f'power union equality criterion n={n}',all((power(a)|power(b)==power(a|b))==(a<=b or b<=a)for a,b in pairs),True)
 check(f'power difference count n={n}',all(len(power(a)-power(b))==2**len(a)-2**len(a&b)for a,b in pairs),True)
check('Q5 atoms total',sum([10,8,7,6,5,4,4,16]),60)
check('Q5 recovered single/pair sizes',[10+6+5+4,8+6+4+4,7+5+4+4,6+4,5+4,4+4],[25,22,20,10,9,8])
check('Q5 exactly two',6+5+4,15)
check('Q6 nonempty strict regions direct',sum(len(set(x))==3 for x in it.product(range(3),repeat=5)),150)
check('Q7 explicit power difference',len(power({1,2,3,4})-power({1,2,5})),12)
check('Q8 intersection equation',(11+9-12)//2,4)
check('Q9 fixed cover choices',2**3-1,7)
check('Q11 population enumeration',sum([x.count(j)for j in range(4)]==[2,1,1,2]for x in it.product(range(4),repeat=6)),180)
check('Q45 positive region sum',sum(math.comb(4,b)*math.comb(4-b,c)*2**(4-b-c)for b in range(1,4)for c in range(1,5-b)),110)
check('Q46 direct five-object pairs',sum(bool(a)and bool(b)and not a&b for a,b in it.product(power(range(5)),repeat=2)),180)
for a,b,c in it.product([False,True],repeat=3):
 check(f'Q1 simplification {a}{b}',((not a and b)or(((a and not b)or not b)and(b and not a))),b and not a)
 check(f'lab distributivity {a}{b}{c}',a and(b or c),(a and b)or(a and c))
check('false XOR distribution witness',(True!=(True and False))!=((True!=True)and(True!=False)),True)
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
old=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/d_sets.html']).decode().replace('\r\n','\n')
new=(R/'dist/chapters/d_sets.html').read_text();oq=ns['questions'](old);nq=ns['questions'](new)
check('46 question placements retained',len(nq),46)
for i in range(4):
 check(f'authentic Q{i+1} identity',nq[i][2]['data-source-id'],oq[i][2]['data-source-id'])
 check(f'authentic Q{i+1} answer order',nq[i][2]['data-answer'],oq[i][2]['data-answer'])
 pattern=r'<div class="exam-options">[\s\S]*?(?=<details)'
 check(f'authentic Q{i+1} original options retained',re.search(pattern,nq[i][3])[0],re.search(pattern,oq[i][3])[0])
rev=json.loads((E/'d_sets-revision.json').read_text())
for index,((a,b,attrs,q),record)in enumerate(zip(nq,rev['records']),1):
 if attrs.get('data-answer'):check(f'Q{index} independently rederived option',record['answer'],int(attrs['data-answer']))
check('complete disclosures',sum('<details class="exam-solution">'in q for a,b,c,q in nq),46)
check('unrelated question animations removed',sum('question-concept-aid'in q for a,b,c,q in nq),0)
content=re.sub(r'<script\b[\s\S]*?</script>','',new)
for m in re.findall(r'<math\b[\s\S]*?</math>',content):ET.fromstring(m)
check('all MathML XML parses',True,True)
check('new final-rule count',len(re.findall('<h3>',new[new.index('id="quick-reference"'):new.index('id="laboratory"')])),20)
inventory=json.loads((E/'inventory.json').read_text())
for c in inventory['chapters']:
 if c['topicId']in['d_logic','d_sets']:continue
 value=(R/'dist'/c['url']).read_text().replace('\r\n','\n')
 check('other chapter unchanged '+c['topicId'],hashlib.sha256(value.encode()).hexdigest(),c['canonicalLFsha256'])
check('logic published content preserved',hashlib.sha256((R/'dist/chapters/d_logic.html').read_bytes().replace(b'\r\n',b'\n')).hexdigest(),hashlib.sha256(subprocess.check_output(['git','show','d9e951a662f1b881b5164b797cc5735ae9bc19c5:dist/chapters/d_logic.html']).replace(b'\r\n',b'\n')).hexdigest())
out=Path(tempfile.gettempdir())/'deep-sets-source-pages';out.mkdir(exist_ok=True);pages=[]
for q in json.loads((B/'exam-calibration/actual-items.json').read_text()):
 if'd_sets'not in q.get('topics',[]):continue
 p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];check('PDF hash '+q['id'],hashlib.sha256(p.read_bytes()).hexdigest(),q['sourceSha256'])
 doc=fitz.open(p);target=out/(q['id']+'.png');doc[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(target);doc.close()
 pages.append(dict(id=q['id'],pdfPage=q['pdfPage'],image=str(target),visualRecheck='pending'))
report=dict(topicId='d_sets',status='passed_finite_checks_pending_visual_recheck',checkCount=len(checks),scope='Exact enumeration n=0..4; fixed-set families enumerate all fixed subsets in that range. General formulas are proved in the authored solutions, not certified universally by these finite tests.',checks=checks,sourcePages=pages)
(E/'d_sets-mathematical-checks.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(dict(checks=len(checks),status=report['status'],sourcePages=pages),indent=2))
