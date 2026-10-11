"""Exact independent sums, states, tree enumerations, sources and preservation."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import ast,hashlib,itertools as it,json,math,re,subprocess,tempfile
import xml.etree.ElementTree as ET
import fitz,sympy as sp
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';checks=[]
def check(name,got,want):
    assert got==want,(name,got,want)
    checks.append(dict(name=name,result=got,expected=want,passed=True))
n,x=sp.symbols('n x',integer=True,positive=True)
G=n*(n+1)*(2*n+1)/6;W=(n-1)*2**n+1
check('weighted successor identity',str(sp.simplify(W.subs(n,n+1)-W-(n+1)*2**n)),'0')
check('square successor identity',str(sp.factor(G.subs(n,n+1)-G-(n+1)**2)),'0')
check('telescoping successor identity',str(sp.factor((n+1)/(n+2)-n/(n+1)-1/((n+1)*(n+2)))),'0')
check('strengthened reciprocal-square slack',str(sp.factor(1/n-1/(n+1)-1/(n+1)**2)),str(1/(n*(n+1)**2)))
check('Hanoi transformed recurrence',str(sp.simplify(2*(2**(n-1)-1)+1-(2**n-1))),'0')
check('square inequality minimal tail seed',[2**j>j*j for j in range(1,6)],[True,False,False,False,True])
for k in range(1,13):
    check(f'exact weighted sum n={k}',sum(j*2**(j-1)for j in range(1,k+1)),(k-1)*2**k+1)
    check(f'exact square sum n={k}',sum(j*j for j in range(1,k+1)),k*(k+1)*(2*k+1)//6)
    check(f'exact telescope n={k}',str(sum((F(1,j*(j+1))for j in range(1,k+1)),F())),str(F(k,k+1)))
    check(f'one-mark binomial sum n={k}',sum(j*math.comb(k,j)for j in range(k+1)),k*2**(k-1))
    if k>=2:check(f'square-mark binomial sum n={k}',sum(j*j*math.comb(k,j)for j in range(k+1)),k*(k+1)*2**(k-2))
    for r in range(k+1):check(f'marked-r identity N={k} r={r}',sum(math.comb(k,j)*math.comb(j,r)for j in range(r,k+1)),math.comb(k,r)*2**(k-r))
check('authentic weighted interval result',F(sum(math.comb(i,3)*math.comb(7,i)for i in range(3,8)),10),F(56))
for b,c in [(0,1),(0,2),(2,1),(-1,2),(3,0)]:
    a=[c]
    for j in range(1,13):a.append(b+sum(a))
    check(f'prefix seed and domain b={b} c={c}',a,[c]+[(b+c)*2**(j-1)for j in range(1,13)])
    series=sp.series((c+(b-c)*x)/(1-2*x),x,0,8).removeO().expand()
    check(f'formal coefficients b={b} c={c}',[int(series.coeff(x,j))for j in range(8)],a[:8])
state=(1,1);cycle=[]
for j in range(3):cycle.append(state);state=(state[1],sum(state)%2)
check('parity state cycle',cycle,[(1,1),(1,0),(0,1)]);check('state return',state,(1,1))
seq={16:1403,17:2025}
for j in range(18,114):seq[j]=3*seq[j-1]+5*seq[j-2]+4
check('authentic parity recurrence actual large integers',[j for j in range(100,114)if seq[j]%2==0],[102,105,108,111])
check('inclusive multiple count',113//3-99//3,4)
check('divisibility claimed domain',all((5**(2*j)-1)%8==0 for j in range(25)),True)
check('divisibility false alternatives',[(5-1)%8,(25-1)%16,(1+1)%3],[4,8,2])
check('induction discovery illustration Euler polynomial',all(sp.isprime(j*j-j+41)for j in range(41)),True)
check('Euler failure at 41',41*41-41+41,41*41)
second=[2,3]
for j in range(2,13):second.append(2*second[-1]-second[-2])
check('two-seed recurrence',[v for v in second],list(range(2,15)))
for provided in [[3],[3,4],[3,4,5],[3,4,5,6]]:
    reached=set(provided)
    for j in range(3,51):
        if j in reached:reached.add(j+4)
    check('step-four exact reachability bases='+str(provided),[j for j in range(3,51)if j in reached],[j for j in range(3,51)if j%4 in{b%4 for b in provided}])
check('step-two even reachability',[2*j for j in range(20)],list(range(0,40,2)))
@lru_cache(None)
def full_trees(m,I):
    if I==0:return(None,)
    out=[]
    for sizes in it.product(range(I),repeat=m):
        if sum(sizes)!=I-1:continue
        out.extend(it.product(*(full_trees(m,j)for j in sizes)))
    return tuple(out)
def stats(t):
    if t is None:return(0,1,1,0)
    rows=[stats(c)for c in t]
    return(1+sum(r[0]for r in rows),sum(r[1]for r in rows),1+sum(r[2]for r in rows),1+max(r[3]for r in rows))
def mass(t):return F(1)if t is None else sum((mass(c)/2 for c in t),F())
for m in [2,3]:
    for I in range(6 if m==2 else 5):
        trees=full_trees(m,I)
        check(f'all full {m}-ary counts internal={I}',all(stats(t)[:3]==(I,(m-1)*I+1,m*I+1)for t in trees),True)
        if m==2:
            check(f'all binary full leaf masses internal={I}',all(mass(t)==1 for t in trees),True)
            if I:check(f'all binary heights internal={I}',all(math.ceil(math.log2(I+1))<=stats(t)[3]<=I for t in trees),True)
check('two shapes same size different heights',{stats(t)[3]for t in full_trees(2,3)},{2,3})
@lru_cache(None)
def binary_nodes(N):
    if N==0:return(None,)
    return tuple((a,b)for left in range(N)for a in binary_nodes(left)for b in binary_nodes(N-1-left))
def raw_mass(t):
    if t==(None,None):return F(1)
    return sum((raw_mass(c)/2 for c in t if c is not None),F())
def raw_full(t):return t==(None,None)or all(c is not None and raw_full(c)for c in t)
for N in range(1,8):
    trees=binary_nodes(N)
    check(f'all binary shapes leaf bound nodes={N}',all(raw_mass(t)<=1 for t in trees),True)
    check(f'finite equality iff full nodes={N}',all((raw_mass(t)==1)==raw_full(t)for t in trees),True)
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[z for z in tree.body if isinstance(z,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
old=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/d_induction.html']).decode().replace('\r\n','\n');new=(R/'dist/chapters/d_induction.html').read_text();oq=ns['questions'](old);nq=ns['questions'](new)
check('46 retained question placements',len(nq),46)
rev=json.loads((E/'d_induction-revision.json').read_text())
for index,((a,b,attrs,q),record)in enumerate(zip(nq,rev['records']),1):
    if attrs.get('data-answer'):check(f'Q{index} independently derived option',record['answer'],int(attrs['data-answer']))
    if index<=4:
        check(f'authentic Q{index} identity',attrs['data-source-id'],oq[index-1][2]['data-source-id'])
        pat=r'<div class="exam-options">[\s\S]*?(?=<details)'
        check(f'authentic Q{index} original options',re.search(pat,q)[0],re.search(pat,oq[index-1][3])[0])
check('complete disclosures',sum('<details class="exam-solution">'in q for a,b,c,q in nq),46)
check('46 individually authored answers',len({q['solutionSha256']for q in rev['records']}),46)
check('unrelated generic aids removed',sum('question-concept-aid'in q for a,b,c,q in nq),0)
check('exact question animation present','question-specific-animation'in nq[-1][3],True)
check('thirty final rules',len(re.findall('<h3>',new[new.index('id="quick-reference"'):new.index('id="references"')])),30)
for m in re.findall(r'<math\b[\s\S]*?</math>',re.sub(r'<script\b[\s\S]*?</script>','',new)):ET.fromstring(m)
check('all MathML XML parses',True,True)
for chapter in json.loads((E/'inventory.json').read_text())['chapters']:
    if chapter['topicId']in['d_logic','d_sets','d_proof','d_functions','d_induction']:continue
    value=(R/'dist'/chapter['url']).read_text().replace('\r\n','\n')
    check('unchanged pending chapter '+chapter['topicId'],hashlib.sha256(value.encode()).hexdigest(),chapter['canonicalLFsha256'])
for topic in ['d_logic','d_sets','d_proof','d_functions']:
    published=subprocess.check_output(['git','show','f1719660997f115d6d93614316628141aa6a09ca:dist/chapters/'+topic+'.html']).replace(b'\r\n',b'\n')
    live=(R/'dist/chapters'/ (topic+'.html')).read_bytes().replace(b'\r\n',b'\n')
    check('previous checked or source-corrected page preserved '+topic,hashlib.sha256(live).hexdigest(),hashlib.sha256(published).hexdigest())
out=Path(tempfile.gettempdir())/'deep-induction-source-pages';out.mkdir(exist_ok=True);pages=[]
for q in json.loads((B/'exam-calibration/actual-items.json').read_text()):
    if 'd_induction'not in q.get('topics',[]):continue
    p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];check('PDF hash '+q['id'],hashlib.sha256(p.read_bytes()).hexdigest(),q['sourceSha256'])
    d=fitz.open(p);target=out/(q['id']+'.png');d[q['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(target);d.close();pages.append(dict(id=q['id'],pdfPage=q['pdfPage'],image=str(target),visualRecheck='pending'))
report=dict(topicId='d_induction',status='passed_finite_checks_pending_visual_recheck',checkCount=len(checks),scope='Exact sums and marked identities n=1..12; full binary trees I=0..5 and full ternary I=0..4; all binary shapes N=1..7; original parity recurrence evaluated through 113; step-four reachability 3..50; symbolic successor identities. General proofs are independently written and are not universally certified by finite tests.',checks=checks,sourcePages=pages)
(E/'d_induction-mathematical-checks.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(dict(checks=len(checks),status=report['status'],sourcePages=pages),indent=2))
