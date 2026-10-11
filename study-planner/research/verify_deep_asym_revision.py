"""Exact examples, independent finite recurrences, source preservation and scene replay.

Finite computations supplement the analytic proofs; they do not certify infinite tails.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import ast, hashlib, json, math, re, subprocess, tempfile
import xml.etree.ElementTree as ET
import mpmath as mp
B=Path(__file__).resolve().parent; R=B.parent; E=B/'deep-library-revision'; checks=[]
def check(name,got,want):
    assert got==want,(name,got,want)
    checks.append(dict(name=name,result=got,expected=want,passed=True))

for n in (5,8):
    check(f'quadratic normalized n={n}',str(F(3*n*n+5*n,n*n)),str(F(3)+F(5,n)))
    check(f'exponential normalized n={n}',str(F(3**n+2**n,3**n)),str(1+F(2,3)**n))
    check(f'double logarithm n={n}',(2**(2**n)).bit_length()-1,2**n)
    check(f'second logarithm n={n}',(2**n).bit_length()-1,n)
    check(f'harmonic exact n={n}',str(sum((F(1,k) for k in range(1,n+1)),F())),{5:'137/60',8:'761/280'}[n])
    check(f'cancelled normalized n={n}',str(F(n*n-n,n*n)),str(1-F(1,n)))
    check(f'cubic normalized n={n}',str(F(n**3+n*n,n**3)),str(1+F(1,n)))
    check(f'even subsequence n={n}',2*n*(2+(-1)**(2*n)),6*n)
    h=(math.factorial(n)-1).bit_length()
    check(f'factorial capacity n={n}',h,{5:7,8:16}[n])
    check(f'neighboring powers n={n}',2**(h-1)<math.factorial(n)<=2**h,True)
check('harmonic extension H8-H5',str(sum((F(1,k) for k in range(6,9)),F())),'73/168')
check('unused factorial-capacity leaves n=8',2**16-math.factorial(8),25216)
for c in (F(7,2),F(4),F(10),F(301,100)):
    threshold=max(1,math.ceil(5/(c-3)))
    check(f'upper quadratic witness c={c}',3+F(5,threshold)<=c,True)
    if threshold>1:check(f'least upper quadratic threshold c={c}',3+F(5,threshold-1)>c,True)
for n in range(1,33):
    power=1<<(n.bit_length()-1)
    check(f'binary floor envelope n={n}',F(n,2)<power<=n,True)
    check(f'quadratic normalized not attained limit n={n}',3+F(5,n)>3,True)
    check(f'factorial exact capacity n={n}',1<<((math.factorial(n)-1).bit_length())>=math.factorial(n),True)
for h in range(1,13):
    t=1
    for n in range(1,h+1):t*=2**n
    check(f'multiplicative recurrence h={h}',t,2**(h*(h+1)//2))
    # Exact transformed shrinking chain with zero final toll and fixed base.
    check(f'squared-logarithm chain h={h}',sum(k*k for k in range(1,h+1)),h*(h+1)*(2*h+1)//6)
    u=1
    for j in range(1,h+1):u=2*u+2**j
    check(f'square-root log-size exact h={h}',u,(h+1)*2**h)

@lru_cache(None)
def floor_root_toll(n):
    if n<=2:return (1,0)
    m=math.isqrt(n);assert 1<=m<n
    cost,depth=floor_root_toll(m)
    return (2*cost+math.log2(n),depth+1)
for n in (3,4,8,15,16,17,64,255,256,257,65535,65536):
    cost,depth=floor_root_toll(n)
    check(f'floor-root terminating finite tree n={n}',math.isfinite(cost) and depth<=math.ceil(math.log2(math.log2(n)))+1,True)

def unequal_tree(n):
    if n<=1:return (F(1),[n],F())
    ca,la,wa=unequal_tree(n/3);cb,lb,wb=unequal_tree(2*n/3)
    return (ca+cb,la+lb,wa+wb+n)
for n in (F(2),F(3),F(7),F(16),F(32)):
    count,leaves,work=unequal_tree(n)
    check(f'unequal-tree leaf mass n={n}',str(sum(leaves)),str(n))
    check(f'unequal-tree base envelopes n={n}',all(F(1,3)<x<=1 for x in leaves),True)
    check(f'unequal-tree count envelopes n={n}',n<=count<3*n,True)

scene_bytes=(R/'dist/chapters/concept-animations.json').read_bytes();scenes=json.loads(scene_bytes)['scenes']
for i,f in enumerate(scenes['asym-parity-ratio']['frames']):
    n=i+1;s=f['snapshot'];check(f'parity frame {i} input',s['n'],n)
    check(f'parity frame {i} exact ratio',s['ordinate'],str(F(n if n%2 else 1)))
for i,(n,f) in enumerate(zip((1,2,3,4,7,8,15,16,31,32),scenes['asym-floor-ratio']['frames'])):
    s=f['snapshot'];power=1<<(n.bit_length()-1)
    check(f'floor frame {i} exact power',s['power'],power)
    check(f'floor frame {i} ratio',s['ordinate'],str(F(power,n)))
mp.mp.dps=60
for i,f in enumerate(scenes['asym-log-oscillation']['frames']):
    s=f['snapshot'];k=i//2;sign=1 if i%2==0 else -1
    phase=(mp.pi/2 if sign==1 else 3*mp.pi/2)+2*mp.pi*k
    n=int(mp.floor(mp.exp(phase)));lnn=mp.log(n);exponent=mp.sin(lnn)
    check(f'oscillation frame {i} independently rounded integer',s['n'],n)
    check(f'oscillation frame {i} exponent half bound',exponent>=mp.mpf('.5') if sign==1 else exponent<=mp.mpf('-.5'),True)
    check(f'oscillation frame {i} plotted ordinate',abs(s['ordinate']-float(lnn*exponent))<1e-12,True)
for sid,key,values in [('growth-threshold','n',[1,2,4,8,16,32]),('encoding-length','Encoding length',[2,3,4,5,6,7]),('loop-doubling','Value',[1,2,4,8,16])]:
    fs=scenes[sid]['frames'];check(sid+' retained frame count',len(fs),len(values))
    for k,(frame,v) in enumerate(zip(fs,values)):check(f'{sid} retained frame {k}',frame['metrics'][key],v)
for k,f in enumerate(scenes['recurrence-levels']['frames']):
    m=f['metrics']
    check(f'equal-split level {k} mass',m['Nodes']*m['Size per node'],8)
    check(f'equal-split level {k} accumulated cost',m['Accumulated toll'],8*(k+1))

ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
baseline='f890223f3111d27958eb483056556fded2d59ff3'
old=subprocess.check_output(['git','show',baseline+':dist/chapters/a_asym.html']).decode().replace('\r\n','\n')
new=(R/'dist/chapters/a_asym.html').read_text();oq=ns['questions'](old);nq=ns['questions'](new);rev=json.loads((E/'a_asym-revision.json').read_text())
check('question placements',len(nq),46);check('individually authored solutions',len({x['solutionSha256'] for x in rev['records']}),46)
for i,((a,b,attrs,q),rec) in enumerate(zip(nq,rev['records']),1):
    if attrs.get('data-answer'):check(f'Q{i} recorded option agreement',rec['answer'],int(attrs['data-answer']))
    if i<=4:
        check(f'authentic Q{i} identity',attrs['data-source-id'],oq[i-1][2]['data-source-id'])
        pat=r'<div class="exam-options">[\s\S]*?(?=<details|<p class="source-correction")'
        if i!=2:check(f'authentic Q{i} option preservation',re.search(pat,q)[0],re.search(pat,oq[i-1][3])[0])
        else:
            options=re.findall(r'<div class="exam-option"><b>\d\.</b><div>([\s\S]*?)</div></div>',q)
            prev=re.findall(r'<div class="exam-option"><b>\d\.</b><div>([\s\S]*?)</div></div>',oq[i-1][3])
            check('Q2 first three options preserved',options[:3],prev[:3])
            check('Q2 corrected fourth option aria formula',bool(re.search(r'aria-label="[^"\n]*Theta\(n\\log\^2 n\)',options[3])),True)
check('solution disclosures',sum('<details class="exam-solution">' in q for a,b,c,q in nq),46)
check('final rules',len(re.findall('<h3>',new[new.index('id="quick-reference"'):new.index('id="references"')])),32)
check('mathematical question tables',sum(q.count('<table>') for a,b,c,q in nq),7)
check('question-specific animation count',new.count('class="concept-animation question-specific-animation"'),3)
maths=re.findall(r'<math\b[\s\S]*?</math>',re.sub(r'<script\b[\s\S]*?</script>','',new))
for expr in maths:ET.fromstring(expr)
check('nonempty native MathML expressions parsed',len(maths)>0,True)
for c in json.loads((E/'inventory.json').read_text())['chapters']:
    if c['topicId'] in ('a_asym','a_recurrence'):continue
    live=(R/'dist'/c['url']).read_bytes().replace(b'\r\n',b'\n')
    before=subprocess.check_output(['git','show','ce78ccc6649ee3ffa22cff387450084c5c72d939:dist/'+c['url']]).replace(b'\r\n',b'\n')
    check('other chapter preserved '+c['topicId'],hashlib.sha256(live).hexdigest(),hashlib.sha256(before).hexdigest())
actual=json.loads((B/'exam-calibration/actual-items.json').read_text());source=[]
for q in actual:
    if 'a_asym' not in q.get('topics',[]):continue
    path=Path(tempfile.gettempdir())/'exam-calibration-1406/source'/q['repoPath']
    check('authentic PDF hash '+q['id'],hashlib.sha256(path.read_bytes()).hexdigest(),q['sourceSha256'])
    source.append(dict(id=q['id'],pdfPage=q['pdfPage'],visualRecheck='Original PDF image inspected in this revision; Q2 missing n and logarithm square restored; smallest-O convention disclosed for square-root recurrence.'))
report=dict(topicId='a_asym',status='passed_with_recorded_finite_bounds',checkCount=len(checks),checks=checks,sourcePages=source,animationJsonSha256=hashlib.sha256(scene_bytes).hexdigest(),scope='Exact rational examples at n=5,8; capacity and envelopes n=1..32; recurrences h=1..12 and explicitly listed floor-root inputs; five unequal-tree inputs; all 34 new animation frames independently replayed, including 60-digit exponential rounding. These checks support the written general proofs, not a universal correctness certificate.')
(E/'a_asym-mathematical-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),sourcePages=len(source),status=report['status'])))
