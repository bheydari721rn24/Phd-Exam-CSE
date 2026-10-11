"""Independent exact models, symbolic identities, source and preservation checks."""
from pathlib import Path
import ast, hashlib, itertools as it, json, math, re, subprocess, tempfile
import xml.etree.ElementTree as ET
import fitz
import sympy as sp
B=Path(__file__).resolve().parent; R=B.parent; E=B/'deep-library-revision'; checks=[]
def check(name, got, want):
    assert got==want,(name,got,want)
    checks.append(dict(name=name,result=got,expected=want,passed=True))
empty=frozenset(); s=frozenset([empty]); t=frozenset([empty,s])
for A in [empty,t,frozenset([empty,s,t]),frozenset([s])]:
    trans=all(x in A for y in A for x in y)
    check('union equivalence '+str(A),frozenset().union(*A)<=A,trans)
    check('power-set equivalence '+str(A),all(y<=A for y in A),trans)
for bits in it.product([False,True],repeat=3):
    H,I,T=bits
    check('categorical universal entailment '+str(bits), not((not I or not T)and(not H or T))or(not H or not I),True)
for size in range(4):
    for model in it.product(list(it.product([False,True],repeat=3)),repeat=size):
        premise=any(H and I for H,I,T in model)and all(not H or T for H,I,T in model)
        assert not premise or any(T and I for H,I,T in model)
    check('categorical existential entailment all models size='+str(size),True,True)
check('order-preserving shift counterexample',all(i+1<j+1 for i,j in it.product(range(-20,21),repeat=2)if i<j)and 0+1!=0,True)
for size in range(6):
    preserving=[p for p in it.permutations(range(size))if all(p[i]<p[j]for i in range(size)for j in range(i+1,size))]
    check('finite ordered self-map identity size='+str(size),preserving,[tuple(range(size))])
for n in range(-60,61):
    assert (n*n%6==0)==(n%6==0)
check('six square equivalence integers -60..60',True,True)
check('modulus four invalid converse',(2*2%4==0,2%4==0),(True,False))
for a in [-3,-1,0,1,2]:
    c=a*a-1;d=a-1
    if c:
        x=sp.Rational(d,c)
        check('parameter existence a='+str(a),str(sp.simplify(c*x-d)),'0')
    else: check('parameter singular classification a='+str(a),'all'if d==0 else'none','all'if a==1 else'none')
check('counterexample pair classification',[x>0 and y>0 and(x+y)%2==0 and not(x%2==0 and y%2==0)for x,y in [(2,4),(1,2),(3,5),(0,2)]],[False,False,True,False])
check('quantifier witness y=x+1',all(x+1>x for x in range(-20,21)),True)
check('equality refutes reversed strict quantifiers',all(not y>y for y in range(-20,21)),True)
x,y,c=sp.symbols('x y c',real=True)
check('sum-ten completion identity',str(sp.simplify(x*(10-x)-(25-(x-5)**2))),'0')
check('positive-domain lower-bound identity',str(sp.simplify(x+1/x-2-(x-1)**2/x)),'0')
check('negative-domain upper-bound identity',str(sp.simplify(x+1/x+2-(x+1)**2/x)),'0')
check('prime-polynomial construction',str(sp.expand((c-1)**2+(c-1)+c-c*c)),'0')
check('Q47 explicit composite',40*40+40+41,41*41)
check('Q47 alternatives prime',[bool(sp.isprime(n*n+n+41))for n in [0,1,2,40]],[True,True,True,False])
check('zero cancellation boundary',(1-1)*(1+1)==1*(1-1)and 1+1!=1,True)
for n in range(1,9):
    check(f'square divisibility input count n={n}',sum(x*x%6==0 for x in range(1,6*n+1)),n)
    check(f'exclusive divisibility count n={n}',sum((x%2==0 or x%3==0)and x%6!=0 for x in range(1,6*n+1)),3*n)
    check(f'universal inequality failures n={n}',sum(x>y for x,y in it.product(range(1,n+1),repeat=2)),n*(n-1)//2)
    check(f'odd-square input residues n={n}',sum(x*x%2 for x in range(2*n)),n)
    N=n+4
    triples=[(a,b,N-a-b)for a in range(1,N)for b in range(1,N)if N-a-b>0]
    check(f'positive fixed-total triples n={n}',len(triples),math.comb(n+3,2))
    check(f'nonnegative fixed-total triples n={n}',sum(a+b<=N for a,b in it.product(range(N+1),repeat=2)),math.comb(n+6,2))
    if n<=4:
        occupied=list(it.product(range(4),repeat=n))
        check(f'largest capped occupancy n={n}',max(map(sum,occupied)),3*n)
        vals=range(1,2*n+1)
        nonforcing=[z for k in range(2*n+1)for z in it.combinations(vals,k)if not any(a+b==2*n+1 for a,b in it.combinations(z,2))]
        check(f'largest pair-avoiding subset n={n}',max(map(len,nonforcing)),n)
        check(f'extremal pair-avoiding subset count n={n}',sum(len(z)==n for z in nonforcing),2**n)
        assignments=list(it.product([0,1],repeat=2*n))
        good=[a for a in assignments if all(not a[2*i]or a[2*i+1]for i in range(n))and any(not a[2*i]for i in range(n))]
        check(f'implication-model exact count n={n}',len(good),3**n-1)
        check(f'false-antecedent binomial partition n={n}',sum(math.comb(n,j)*2**j for j in range(1,n+1)),len(good))
for m in range(1,25):
    factor=math.prod(int(p)**math.ceil(e/2)for p,e in sp.factorint(m).items())
    check('general square divisor m='+str(m),all((x*x%m==0)==(x%factor==0)for x in range(-50,51)),True)
check('shared-antecedent model count',sum((not p or q)and(not p or r)and not p for p,q,r in it.product([0,1],repeat=3)),4)
check('explosion premise models',sum(p and not p for p in [False,True]),0)
check('quantifier-order equality countermodel', (all(any(a==b for b in [0,1])for a in [0,1]),any(all(a==b for a in [0,1])for b in [0,1])),(True,False))
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[z for z in tree.body if isinstance(z,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
old=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/d_proof.html']).decode().replace('\r\n','\n')
new=(R/'dist/chapters/d_proof.html').read_text(); oq=ns['questions'](old);nq=ns['questions'](new)
check('48 question placements retained',len(nq),48)
rev=json.loads((E/'d_proof-revision.json').read_text())
for i,((a,b,attrs,q),record)in enumerate(zip(nq,rev['records']),1):
    if attrs.get('data-answer'):check(f'Q{i} independently derived option',record['answer'],int(attrs['data-answer']))
    if i<=6:
        check(f'authentic Q{i} identity',attrs['data-source-id'],oq[i-1][2]['data-source-id'])
        pattern=r'<div class="exam-options">[\s\S]*?(?=<details)'
        check(f'authentic Q{i} option order retained',re.search(pattern,q)[0],re.search(pattern,oq[i-1][3])[0])
check('48 full solution disclosures',sum('<details class="exam-solution">'in q for a,b,c,q in nq),48)
check('unrelated question visual aids removed',sum('question-concept-aid'in q for a,b,c,q in nq),0)
check('48 individual authored answers',len({r['solutionSha256']for r in rev['records']}),48)
for m in re.findall(r'<math\b[\s\S]*?</math>',re.sub(r'<script\b[\s\S]*?</script>','',new)):ET.fromstring(m)
check('all native MathML XML parses',True,True)
check('eighteen final rules',len(re.findall('<h3>',new[new.index('id="quick-reference"'):new.index('id="references"')])),18)
check('old final-month deferral removed','intentionally deferred to the final month'in new,False)
inventory=json.loads((E/'inventory.json').read_text())
for chapter in inventory['chapters']:
    if chapter['topicId']in['d_logic','d_sets','d_proof','d_functions']:continue
    value=(R/'dist'/chapter['url']).read_text().replace('\r\n','\n')
    check('unchanged pending chapter '+chapter['topicId'],hashlib.sha256(value.encode()).hexdigest(),chapter['canonicalLFsha256'])
functions_old=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/d_functions.html']).decode().replace('\r\n','\n')
functions_new=(R/'dist/chapters/d_functions.html').read_text()
def outside_q19(page):
    a,b,attrs,q=next(q for q in ns['questions'](page)if q[2].get('data-source-id')=='Phd_CS_1405_Q19')
    return page[:a]+page[b:]
check('functions outside confirmed source correction unchanged',hashlib.sha256(outside_q19(functions_new).encode()).hexdigest(),hashlib.sha256(outside_q19(functions_old).encode()).hexdigest())
for topic,sha in [('d_logic','d9e951a662f1b881b5164b797cc5735ae9bc19c5'),('d_sets','51bf6393736c974144090d16c5aac4648bd1dd60')]:
    live=(R/f'dist/chapters/{topic}.html').read_bytes().replace(b'\r\n',b'\n')
    published=subprocess.check_output(['git','show',sha+f':dist/chapters/{topic}.html']).replace(b'\r\n',b'\n')
    check('previous published chapter preserved '+topic,hashlib.sha256(live).hexdigest(),hashlib.sha256(published).hexdigest())
out=Path(tempfile.gettempdir())/'deep-proof-source-pages';out.mkdir(exist_ok=True);pages=[]
for q in json.loads((B/'exam-calibration/actual-items.json').read_text()):
    if 'd_proof'not in q.get('topics',[]):continue
    p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath']
    check('PDF source hash '+q['id'],hashlib.sha256(p.read_bytes()).hexdigest(),q['sourceSha256'])
    doc=fitz.open(p);target=out/(q['id']+'.png');doc[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(target);doc.close()
    pages.append(dict(id=q['id'],pdfPage=q['pdfPage'],image=str(target),visualRecheck='pending'))
report=dict(topicId='d_proof',status='passed_finite_checks_pending_visual_recheck',checkCount=len(checks),scope='Exact finite enumerations: families n=1..8; subset, capacity and Boolean model enumerations n=1..4; integer divisibility -60..60; general moduli 1..24 on -50..50. Symbolic identities and independently written general proofs complement, but are not universally certified by, the finite checks.',checks=checks,sourcePages=pages)
(E/'d_proof-mathematical-checks.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(dict(checks=len(checks),status=report['status'],sourcePages=pages),indent=2))
