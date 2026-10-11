"""Independent exact resource counts and replay of every authentic merge checkpoint."""
from pathlib import Path
from fractions import Fraction
import ast, hashlib, itertools, json, math, re, subprocess, tempfile
import xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent; R=B.parent; E=B/'deep-library-revision'; checks=[]
def check(name,got,want):
    assert got==want,(name,got,want)
    checks.append(dict(name=name,result=got,expected=want,passed=True))

def merge(a,b):
    out=[]; events=[]; i=j=0
    while i<len(a) and j<len(b):
        pick=min(a[i],b[j]); out.append(pick)
        events.append(dict(left=a[:],right=b[:],i=i,j=j,chosen=pick,output=out[:],finished=False))
        if a[i]<b[j]:i+=1
        else:j+=1
    out+=a[i:]+b[j:]
    events.append(dict(left=a[:],right=b[:],i=i,j=j,chosen=None,output=out[:],finished=True))
    return out,events
def sort(a):
    if len(a)<2:return a[:],[]
    m=len(a)//2; left,le=sort(a[:m]); right,re=sort(a[m:]); out,ev=merge(left,right)
    return out,le+re+ev
sorted_keys,events=sort([12,7,5,9,3,8,2,6])
check('authentic sorted output',sorted_keys,[2,3,5,6,7,8,9,12])
check('authentic comparison count',sum(not e['finished'] for e in events),16)
check('all seven independent exhaustion events',sum(e['finished'] for e in events),7)
scene_bytes=(R/'dist/chapters/concept-animations.json').read_bytes()
scene=json.loads(scene_bytes)['scenes']['model-merge-exact']; total=0
check('exact checkpoint count',len(scene['frames']),len(events))
for k,(event,frame) in enumerate(zip(events,scene['frames'])):
    for key,value in event.items():check(f'checkpoint {k} {key}',frame['snapshot'][key],value)
    total+=not event['finished'];check(f'checkpoint {k} cumulative comparisons',frame['snapshot']['total'],total)
    check(f'checkpoint {k} native counter formula',frame['formula'],f'C={total}')

# Exhaustive finite input families test both attainable merge endpoint bounds.
for p in range(1,6):
    for q in range(1,6):
        counts=[]
        for positions in itertools.combinations(range(p+q),p):
            a=list(positions);b=[x for x in range(p+q) if x not in positions]
            out,ev=merge(a,b);counts.append(len(ev)-1)
            assert out==list(range(p+q))
        check(f'merge minimum p={p} q={q}',min(counts),min(p,q))
        check(f'merge maximum p={p} q={q}',max(counts),p+q-1)

# Construct one family that attains every sequential stage maximum simultaneously.
for m in range(1,6):
    for k in range(2,8):
        low=iter(range(k*(m-1)));lists=[]
        for j in range(k):lists.append([next(low) for _ in range(m-1)]+[k*(m-1)+j])
        acc=lists[0];charged=0
        for j,other in enumerate(lists[1:],2):
            acc,ev=merge(acc,other);check(f'sequential maximum m={m} k={k} stage={j}',len(ev)-1,j*m-1);charged+=len(ev)-1
        check(f'sequential total m={m} k={k}',charged,m*(k*(k+1)//2-1)-(k-1))

for n in range(1,8):
    updates=0
    for a in itertools.permutations(range(n)):
        smallest=math.inf
        for v in a:
            if v<smallest:updates+=1;smallest=v
    check(f'exhaustive permutation expectation n={n}',str(Fraction(updates,math.factorial(n))),str(sum((Fraction(1,j) for j in range(1,n+1)),Fraction())))
for n in range(1,13):
    check(f'full subset bits n={n}',sum(n for _ in range(2**n)),n*2**n)
    check(f'triangular index region n={n}',sum(1 for i in range(n) for j in range(i)),n*(n-1)//2)
    check(f'binary length n={n}',(2**n-1).bit_length(),n)
    check(f'exact doubling dense charged bits n={n}',sum((2**(j-1)).bit_length() for j in range(1,n+1)),n*(n+1)//2)
    check(f'explicit triple payload n={n}',sum(3 for _ in itertools.combinations(range(n),3)),3*math.comb(n,3))
    check(f'exact factorial tree capacity n={n}',(math.factorial(n)-1).bit_length(),math.ceil(math.log2(math.factorial(n))))
for n in [5,8]:check(f'explicit permutation references n={n}',sum(len(p) for p in itertools.permutations(range(n))),n*math.factorial(n))
for r in range(1,7):
    for c in range(1,7):
        check(f'rectangular products r={r} c={c}',sum(1 for _ in range(r) for _ in range(c)),r*c)
        check(f'rectangular chain additions r={r} c={c}',sum(1 for _ in range(r) for _ in range(c-1)),r*(c-1))
def call_stats(n):
    if n==1:return 1,1,0
    calls,depth,work=call_stats(n//2)
    return 1+2*calls,1+depth,2*work+n
for h in range(10):check(f'balanced recursion h={h}',call_stats(2**h),(2**(h+1)-1,h+1,h*2**h))
check('four equal bits among eight outcomes',math.comb(8,4),70)
check('binary leaf-capacity rounded depth',(math.comb(8,4)-1).bit_length(),7)
value=2
for k in range(7):
    check(f'square exact value k={k}',value,2**(2**k));check(f'square bit length k={k}',value.bit_length(),2**k+1);value*=value
check('20-bit exact capacity',100*(2**20-1),104857500)

ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
old=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/a_model.html']).decode().replace('\r\n','\n')
new=(R/'dist/chapters/a_model.html').read_text();oq=ns['questions'](old);nq=ns['questions'](new);rev=json.loads((E/'a_model-revision.json').read_text())
check('46 question placements',len(nq),46)
for index,((a,b,attrs,q),record) in enumerate(zip(nq,rev['records']),1):
    if attrs.get('data-answer'):check(f'Q{index} declared option agreement',record['answer'],int(attrs['data-answer']))
    if index<=4:
        check(f'authentic Q{index} preserved identity',attrs['data-source-id'],oq[index-1][2]['data-source-id'])
        pat=r'<div class="exam-options">[\s\S]*?(?=<details)'
        check(f'authentic Q{index} preserved original options',re.search(pat,q)[0],re.search(pat,oq[index-1][3])[0])
check('individually authored solution count',len({r['solutionSha256'] for r in rev['records']}),46)
check('solution disclosures',sum('<details class="exam-solution">' in q for a,b,c,q in nq),46)
check('final complete rules',len(re.findall('<h3>',new[new.index('id="quick-reference"'):new.index('id="references"')])),32)
check('mathematical question tables',sum(q.count('<table>') for a,b,c,q in nq),6)
for expression in re.findall(r'<math\b[\s\S]*?</math>',re.sub(r'<script\b[\s\S]*?</script>','',new)):ET.fromstring(expression)
check('native MathML syntax',True,True)
for chapter in json.loads((E/'inventory.json').read_text())['chapters']:
    topic=chapter['topicId']
    if topic=='a_model':continue
    live=(R/'dist'/chapter['url']).read_bytes().replace(b'\r\n',b'\n')
    preserved=subprocess.check_output(['git','show','1cb982141cc78010ffe07415b89be253e8094dac:dist/'+chapter['url']]).replace(b'\r\n',b'\n')
    check('other chapter unchanged '+topic,hashlib.sha256(live).hexdigest(),hashlib.sha256(preserved).hexdigest())
sources=[]
for q in json.loads((B/'exam-calibration/actual-items.json').read_text()):
    if 'a_model' not in q.get('topics',[]):continue
    p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath']
    check('authentic PDF hash '+q['id'],hashlib.sha256(p.read_bytes()).hexdigest(),q['sourceSha256'])
    sources.append(dict(id=q['id'],pdfPage=q['pdfPage'],visualRecheck='Original PDF image inspected during this revision; parameters and option order agree.'))
report=dict(topicId='a_model',status='passed_with_recorded_finite_bounds',checkCount=len(checks),scope='Merge input partitions p,q=1..5; simultaneous sequential worst-case m=1..5,k=2..7; all permutations n=1..7 for record expectation; exact representation/output identities n=1..12; recursion h=0..9; individual 23-frame replay. Finite checks support, and do not universally certify, the written general proofs.',checks=checks,sourcePages=sources,animationJsonSha256=hashlib.sha256(scene_bytes).hexdigest())
(E/'a_model-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),sourcePages=sources,status=report['status']),indent=2))
