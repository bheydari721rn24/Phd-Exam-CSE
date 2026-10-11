from pathlib import Path
from fractions import Fraction
import ast,hashlib,itertools,json,math,re,subprocess,tempfile
import xml.etree.ElementTree as ET
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';checks=[]
def check(name,got,want):
    assert got==want,(name,got,want)
    checks.append(dict(name=name,result=got,expected=want,passed=True))
check('authentic fifteen-value ordered triples',10+sum(1 for i in range(1,16) for j in range(i,16) for k in range(j,16)),690)
check('one-strict triples n=10',sum(i<=j<k for i,j,k in itertools.product(range(1,11),repeat=3)),165)
check('divisibility branches n=12',sum(j%i==0 for i in range(1,13) for j in range(1,13)),35)
check('harmonic exact n=5',str(sum((Fraction(1,i) for i in range(1,6)),Fraction())),'137/60')
for n in range(0,25):
    triangle=sum(1 for i in range(1,n+1) for j in range(1,i+1))
    check(f'triangular bodies n={n}',triangle,n*(n+1)//2)
    check(f'inner guards n={n}',sum(i+1 for i in range(1,n+1)),n*(n+3)//2)
    check(f'doubled-row bodies n={n}',sum(len(range(1,2*i+1)) for i in range(1,n+1)),n*(n+1))
    check(f'squared-row bodies n={n}',sum(len(range(1,i*i+1)) for i in range(1,n+1)),n*(n+1)*(2*n+1)//6)
    check(f'weighted triangle n={n}',sum(j for i in range(1,n+1) for j in range(1,i+1)),n*(n+1)*(n+2)//6)
    check(f'filtered parity n={n}',sum((i+j)%2==0 for i in range(1,n+1) for j in range(1,i+1)),(n+1)**2//4)
    check(f'sum-constrained triangle n={n}',sum(i+j<=n for i,j in itertools.product(range(1,n+1),repeat=2)),n*(n-1)//2)
    check(f'residue successes n={n}',sum(i%3!=0 for i in range(1,3*n+1)),2*n)
    check(f'divisor reversed count n={n}',sum(i%j==0 for i,j in itertools.product(range(1,n+1),repeat=2)),sum(n//j for j in range(1,n+1)))
    if n:
        d=sum(n//j for j in range(1,n+1));h=sum((Fraction(1,j) for j in range(1,n+1)),Fraction())
        check(f'divisor harmonic envelope n={n}',n*h/2<=d<=n*h,True)
        reverse=0
        for i in range(1,n+1):
            v=i
            while v<=n:reverse+=1;v*=2
        check(f'reverse doubling binary identity n={n}',reverse,2*n-n.bit_count())
        outer=1;weighted=0;visits=0
        while outer<=n:visits+=1;weighted+=outer;outer*=2
        check(f'doubling visits n={n}',visits,n.bit_length())
        check(f'doubling weighted work n={n}',weighted,(1<<n.bit_length())-1)
for n in range(1,13):
    weak=[(i,j,k) for i,j,k in itertools.product(range(1,n+1),repeat=3) if i<=j<=k]
    strict=[v for v in weak if v[0]<v[1]<v[2]]
    shifted={(i,j+1,k+2) for i,j,k in weak}
    check(f'weak-triple bijection n={n}',sorted(shifted),list(itertools.combinations(range(1,n+3),3)))
    check(f'equality difference n={n}',len(weak)-len(strict),n*n)
    count=0
    for i in range(n):
        v=1<<i
        while v<=(1<<n):count+=1;v*=2
    check(f'correlated exponent rows n={n}',count,n*(n+3)//2)
for bound in (0,1,2,3,4,5,15,16,17,255,256,257,65535,65536,65537):
    count=0;v=2
    while v<=bound:count+=1;v*=v
    # Exact integer exponent comparison avoids nested floating logarithms.
    expected=0 if bound<2 else (bound.bit_length()-1).bit_length()
    check(f'inclusive squaring endpoint bound={bound}',count,expected)
for n in (5,8):
    check(f'exponential rows n={n}',sum(1<<i for i in range(n+1)),{5:63,8:511}[n])
    a=list(range(1,2*n,2));b=list(range(2,2*n+1,2));i=j=count=0
    while i<n and j<n:
        count+=1
        if a[i]<b[j]:i+=1
        else:j+=1
    check(f'attained equal-merge maximum n={n}',count,2*n-1)
for n in (1,2,4,8,16,64):
    exact=sum(i*j*k<=n for i,j,k in itertools.product(range(1,n+1),repeat=3))
    floor=sum(n//(i*j) for i in range(1,n+1) for j in range(1,n//i+1))
    check(f'product region exact enumeration n={n}',exact,floor)
    h=sum((Fraction(1,j) for j in range(1,n+1)),Fraction());check(f'product region upper envelope n={n}',exact<=n*h*h,True)

raw=(R/'dist/chapters/concept-animations.json').read_bytes();scenes=json.loads(raw)['scenes']
total=0
for k,f in enumerate(scenes['loop-question-parity']['frames'],1):
    row=sum((k+j)%2==0 for j in range(1,k+1));total+=row
    check(f'parity frame {k}',f['snapshot'],dict(n=8,i=k,rowCount=row,total=total))
smallest=None;updates=0;values=[8,3,7,2,6,1,5,4]
for k,(key,f) in enumerate(zip(values,scenes['loop-question-minimum']['frames']),1):
    before=smallest;changed=before is None or key<before
    if changed:smallest=key;updates+=1
    check(f'minimum frame {k}',f['snapshot'],dict(values=values,i=k,key=key,before='positive infinity' if before is None else before,after=smallest,update=changed,updates=updates,comparisons=k))
total=0
for i,f in enumerate(scenes['loop-question-product']['frames'],1):
    rows=[sum(i*j*k<=8 for k in range(1,9)) for j in range(1,9)];count=sum(rows);total+=count
    check(f'product layer {i}',f['snapshot'],dict(n=8,i=i,rowCounts=rows,layerCount=count,total=total))
check('complete product animation count',total,sum(i*j*k<=8 for i,j,k in itertools.product(range(1,9),repeat=3)))
expected=[dict(i=i,j=j,count=k) for k,(i,j) in enumerate(((i,j) for i in range(1,6) for j in range(1,i+1)),1)]
check('retained triangular trace', [f['snapshot'] for f in scenes['loop-triangle']['frames']],expected)
for sid in ('model-merge-exact','loop-doubling','word-bit-cost','lower-bound','search-stall'):
    before=json.loads(subprocess.check_output(['git','show','7980ac1f52ab9fdc95ba81d17bbaabb8c28f8cf0:dist/chapters/concept-animations.json']))['scenes'][sid]
    check('previous bounded trace retained '+sid,scenes[sid],before)

ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
old=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/a_loop.html']).decode().replace('\r\n','\n')
new=(R/'dist/chapters/a_loop.html').read_text();oq=ns['questions'](old);nq=ns['questions'](new);rev=json.loads((E/'a_loop-revision.json').read_text())
check('individually authored solutions',len({x['solutionSha256'] for x in rev['records']}),46);check('question placements',len(nq),46)
for i,((a,b,attrs,q),rec) in enumerate(zip(nq,rev['records']),1):
    if attrs.get('data-answer'):check(f'Q{i} option agreement',rec['answer'],int(attrs['data-answer']))
    if i<=4:
        check(f'authentic Q{i} identity',attrs['data-source-id'],oq[i-1][2]['data-source-id'])
        pat=r'<div class="exam-options">[\s\S]*?(?=<details)';check(f'authentic Q{i} original options',re.search(pat,q)[0],re.search(pat,oq[i-1][3])[0])
check('solution disclosures',sum('<details class="exam-solution">' in q for a,b,c,q in nq),46)
check('final rules',len(re.findall('<h3>',new[new.index('id="quick-reference"'):new.index('id="references"')])),32)
check('question tables',sum(q.count('<table>') for a,b,c,q in nq),7)
for expr in re.findall(r'<math\b[\s\S]*?</math>',re.sub(r'<script\b[\s\S]*?</script>','',new)):ET.fromstring(expr)
check('nonempty native mathematics parsed','<math' in new,True)
for c in json.loads((E/'inventory.json').read_text())['chapters']:
    if c['topicId']=='a_loop':continue
    live=(R/'dist'/c['url']).read_bytes().replace(b'\r\n',b'\n');before=subprocess.check_output(['git','show','7980ac1f52ab9fdc95ba81d17bbaabb8c28f8cf0:dist/'+c['url']]).replace(b'\r\n',b'\n')
    check('other chapter preserved '+c['topicId'],hashlib.sha256(live).hexdigest(),hashlib.sha256(before).hexdigest())
source=[]
for q in json.loads((B/'exam-calibration/actual-items.json').read_text()):
    if 'a_loop' not in q.get('topics',[]):continue
    p=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath'];check('authentic PDF hash '+q['id'],hashlib.sha256(p.read_bytes()).hexdigest(),q['sourceSha256']);source.append(dict(id=q['id'],pdfPage=q['pdfPage'],visualRecheck='Original rendered PDF inspected; weak triple loop initialization was also inspected in a magnified PDF clip.'))
report=dict(topicId='a_loop',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,sourcePages=source,animationJsonSha256=hashlib.sha256(raw).hexdigest(),scope='Exact frequency families n=0..24; weak-triple bijections n=1..12; explicit squaring endpoints; product enumeration at six listed bounds; all 24 new question frames replayed. Previously checked merge/bit/doubling/search states are preserved. Finite checks supplement the analytic identities and bounds, not a universal certificate.')
(E/'a_loop-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),sourcePages=len(source),status=report['status'])))
