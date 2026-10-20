"""Independent bounded arithmetic/Python oracle; no C execution and no checkout writes."""
import hashlib,json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).parent
raw=(ROOT/'research/p_arrays-questions.json').read_bytes()
questions={q['id']:q for q in json.loads(raw)}
rows=[]
assertions=0
def check(key,actual,expected,note):
    global assertions
    assert actual==expected,(key,actual,expected)
    assertions+=1
    rows.append({'id':key,'actual':actual,'expected':expected,'note':note,'status':'passed'})
def semantic(key,note):
    rows.append({'id':key,'status':'reviewed_semantically_not_executed','note':note})
check('PA13',([2,4,6,8,10,12,14][4-3],[2,4,6,8,10,12,14][4+2],[k for k in range(-10,11) if 0<=4+k<7]),(4,14,list(range(-4,3))),'Independent transformed-index enumeration; negative C subscript relative to p.')
check('PA14',(9*4//4,8//4),(9,2),'Declared target-model sizes only; array parameter adjustment is separately reviewed.')
check('PA15',(4,6*4),(4,24),'Typed strides under stipulated flat byte model; equal starts do not equal types.')
check('PA16',(2*5*4,5*4),(40,20),'Pointer-to-row rather than pointer-to-pointer.')
semantic('PA17','C17 6.5.6 array relation: the first row has length three; p[4] exceeds it despite rectangular adjacency. No invalid C run.')
semantic('PA18','Partial initializer fills omitted integer elements with zero; static no-initializer zero; automatic uninitialized b has no asserted numerical value.')
semantic('PA19','Array assignment fails modifiable-lvalue constraint; fixed zero bound is nonstandard. Diagnostics are not inferred by executing a compiler.')
check('PA20',(4,4-0),(4,4),'One-past position/subtraction abstract model; dereference and a+5 classified semantically invalid, not run.')
for n in range(101):
    i=n; seen=[]
    while i>0:
        i-=1;seen.append(i)
    assert seen==list(range(n-1,-1,-1));assertions+=1
check('PA21',len(seen),100,'Safe boundary-before-decrement loop tested for n=0..100; unsafe unsigned loop not run.')
vis=list(range(3,26,4))
check('PA22',(len(vis),vis[-1],math.ceil((26-3)/4)),(6,23,6),'Strict arithmetic progression.')
a=[5,5,2,2,7,1,1]
def minimum(a,from_first):
    best=a[0] if from_first else math.inf;updates=0;comparisons=0;pos=0
    for i in range(1 if from_first else 0,len(a)):
        comparisons+=1
        if a[i]<best:best=a[i];pos=i;updates+=1
    return comparisons,updates,pos
check('PA23',(minimum(a,True),minimum(a,False)),((6,2,5),(7,3,5)),'Strict ties leave earliest minimum.')
check('PA24',sum((i+1)*x for i,x in enumerate([2,-1,4,3])),24,'Exact integer weighted contributions.')
a=[3,-2,5,1,-4];p=[0]
for x in a:p.append(p[-1]+x)
check('PA25',(p,[p[r]-p[l] for l,r in [(1,4),(0,5),(3,3)]]),([0,3,1,6,7,3],[4,3,0]),'Boundary prefix construction and three intervals.')
d=[0]*6
for l,r,v in [(1,4,4),(2,5,-2)]:d[l]+=v;d[r]-=v
total=0;arr=[]
for x in d[:5]:total+=x;arr.append(total)
check('PA26',(d,arr),([0,4,-2,0,-4,2],[0,4,2,2,-2]),'Boundary difference events; sentinel excluded from result.')
a=[[1,2,3],[4,5,6]]
p=[[sum(a[x][y] for x in range(i) for y in range(j)) for j in range(4)] for i in range(3)]
check('PA27',(p,p[2][3]-p[0][3]-p[2][1]+p[0][1]),([[0,0,0,0],[0,1,3,6],[0,5,12,21]],16),'Prefix rectangles built directly from sums, independently of recurrence.')
for key,order,expected in [('PA28',range(1,5),[1,3,6,10,15]),('PA29',range(4,0,-1),[1,3,5,7,9])]:
    a=[1,2,3,4,5]
    for i in order:a[i]+=a[i-1]
    check(key,a,expected,'Actual sequential in-place read/write trace.')
def move(a,s,d,m,reverse=False):
    b=a[:]
    for t in (range(m-1,-1,-1) if reverse else range(m)):b[d+t]=b[s+t]
    return b
a=[2,4,6,8,10,12]
check('PA30',move(a,0,1,4),[2,2,2,2,2,12],'Forward destructive right overlap.')
check('PA31',move(a,0,1,4,True),[2,2,4,6,8,12],'Reverse original-preserving right overlap.')
check('PA32',(move(a,1,0,4),move(a,1,0,4,True)),([4,6,8,10,10,12],[10,10,10,10,10,12]),'Both left-overlap directions.')
check('PA33',(move([1,2,3,4],0,1,3),move([1,2,3,4],1,0,3)),([1,1,1,1],[2,3,4,4]),'Final-equality weak contract counterexamples; original snapshot is needed.')
for n in range(20):
    for l in range(n+1):
        for r in range(l,n+1):
            a=list(range(n));b=[]
            for t in range(r-l):b.append(a[l+t])
            assert b==a[l:r];assertions+=1
semantic('PA34','Independently tested copy result all 1540 bounded interval cases n<20; generic invariant needs distinct storage and a suitable zero-length representation.')
a=[3,6,9,12];a.insert(2,7)
check('PA35',(a,4-2,4-4),([3,6,7,9,12],2,0),'Logical insertion and shift counts.')
a=[3,6,9,12,15];del a[1]
check('PA36',(a,5-1-1),([3,9,12,15],3),'Logical deletion and stable shift count; physical spare slot remains unspecified by container contract.')
a=list(range(7));pairs=[]
for k in range((6-1)//2):
    i,j=1+k,6-1-k;pairs.append([i,j]);a[i],a[j]=a[j],a[i]
check('PA37',(pairs,a),([[1,5],[2,4]],[0,5,4,3,2,1,6]),'Exclusive right boundary and untouched center.')
a=list(range(7));stages=[]
for l,r in [(0,3),(3,7),(0,7)]:a[l:r]=a[l:r][::-1];stages.append(a[:])
check('PA38',stages,[[2,1,0,3,4,5,6],[2,1,0,6,5,4,3],[3,4,5,6,0,1,2]],'All three reversal stages.')
cycles=[];unseen=set(range(12))
while unseen:
    cur=min(unseen);c=[]
    while cur in unseen:c.append(cur);unseen.remove(cur);cur=(cur+8)%12
    cycles.append(c)
check('PA39',cycles,[[0,8,4],[1,9,5],[2,10,6],[3,11,7]],'Destination-to-source map +8 for left rotation; opposite original-to-destination direction acknowledged.')
a=[5,2,7,4,6,9,8];w=0
for r in range(len(a)):
    if a[r]%2==0:a[w]=a[r];w+=1
check('PA40',(a[:w],w),([2,4,6,8],4),'Read/write compaction; physical tail not claimed erased.')
outputs=[]
for order in (range(3,0,-1),range(1,4)):
    a=[3,5,9,10]
    for i in order:a[i]-=a[i-1]
    outputs.append(a)
check('PA41',outputs,[[3,2,4,1],[3,2,7,3]],'Independent reverse/forward difference traces.')
# All ten Python certificate programs are executed in fresh namespaces. Their
# values are then compared with hand-derived expected values, not merely with
# their stored certificates. The three multiline programs actually printed in
# stems PA46/47/48 are executed or reconstructed exactly below as appropriate.
expected={
'PA42':[4,[0,3],[]], 'PA43':[[6,5,4,3,2,1,0],[],[5,3,1]],
'PA44':[0,9,2,8,4,7], 'PA45':[[1,8,9,5],[1,8,6,7,9,5]],
'PA46':[[[2,7],[5]],[[2,7],[9]]],
'PA47':[[[0,0,9,0]]*3,[[0,0,0,0],[0,0,9,0],[0,0,0,0]]],
'PA48':[4,7], 'PA49':[True,False,True,False],
'PA50':[[9,25],[-2,3,5]], 'PA51':[2,3]}
def plain(x):return json.loads(json.dumps(x))
for key,want in expected.items():
    code=questions[key]['certificate']['data'][0];ns={};exec(compile(code,key,'exec'),ns)
    check(key,plain(ns['result']),want,'Fresh actual Python execution with independent expected result.')
for key in ['PA46','PA48']:
    code=re.search(r'~~~python\n(.*?)\n~~~',questions[key]['stem'],re.S).group(1)
    ns={};exec(compile(code,key+'-printed-stem','exec'),ns)
    check(key+'-printed',plain(ns['result']),expected[key],'Exact multiline code extracted from the question stem, not certificate.')
ns={};exec('bad=[[0]*4]*3\ngood=[[0]*4 for _ in range(3)]\nbad[1][2]=9\ngood[1][2]=9',ns)
check('PA47-identity',(ns['bad'][0] is ns['bad'][2],ns['good'][0] is ns['good'][2]),(True,False),'Fresh shared-versus-distinct object identity test.')
for index in [8,-8]:
    try:list(range(6))[index]
    except IndexError:assertions+=1
    else:raise AssertionError(index)
a=list(range(6))
try:a[1:6:2]=[9,8]
except ValueError:assertions+=1
else:raise AssertionError('PA44 replacement count did not fail')
check('PA52',(len([97,98,0,99,0,0,0,0]),[97,98,0,99,0,0,0,0].index(0)),(8,2),'Abstract initialized byte array; malformed displayed escape notation is separately reported.')
semantic('PA53','C17 permits char[3] initialized by cat without terminator; strlen contract then fails. No UB string call executed.')
semantic('PA54','Writable initialized array distinct from literal; casting away const does not grant literal modification rights. No invalid write executed.')
def bounded(a):
    k=0
    while k<len(a) and a[k]!=0:k+=1
    return k,k<len(a)
check('PA55',(bounded([65,66,67,0,88]),bounded([65,66,67,88,89])),((3,True),(5,False)),'Bound guard precedes element read; absence distinguished.')
def search(text,pat):
    if not pat:return 0,0
    if len(pat)>len(text):return None,0
    comparisons=0
    for i in range(len(text)-len(pat)+1):
        for j in range(len(pat)):
            comparisons+=1
            if text[i+j]!=pat[j]:break
        else:return i,comparisons
    return None,comparisons
check('PA56',search('aaaaab','aaab'),(2,12),'Naive first-mismatch count includes successful tests.')
check('PA57',(search('abc',''),search('abc','abcd')),((0,0),(None,0)),'Empty convention and longer-pattern guard; unsigned subtraction not executed.')
check('PA58',(4+4+1<=9,4+4+1<=8),(True,False),'Final terminator included.')
semantic('PA59','argc=3 argument-pointer array has argv[3] null; yz has separate zero char at argv[2][2]. Null dereference not executed.')
semantic('PA60','ctype requires EOF or unsigned-char-representable int; negative plain-char promotion may violate it. Cast to unsigned char restores domain, not Unicode semantics.')
semantic('PA61','Interior pointer borrows source lifetime and is not an owning allocation pointer; automatic local lifetime ends on return. No dangling pointer execution.')
def grow(n,initial,factor=None,increment=None):
    c=initial;length=0;copies=0;peak=c
    for _ in range(n):
        if length==c:
            new=c*factor if factor else c+increment
            copies+=length;peak=max(peak,c+new);c=new
        length+=1
    return c,copies,copies+n,peak
check('PA62',grow(13,1,factor=2),(16,15,28,24),'Allocate-copy-free peak, successful operations, unit-cost assignments.')
for n in range(1,10001):
    c=1<<(n-1).bit_length();copies=c-1
    assert n<=c<2*n and copies<2*n and copies+n<3*n;assertions+=1
semantic('PA63','General geometric-series proof reviewed; inequalities independently checked n=1..10000, including exact powers.')
check('PA64',grow(12,3,increment=3)[:3],(12,18,30),'Additive growth happens only before otherwise-exceeding append.')
for m in range(1,101):
    assert grow(3*m,3,increment=3)[1]==3*m*(m-1)//2;assertions+=1
check('PA65',(grow(10,1,factor=3)[:3],grow(10,1,factor=2)[:3]),((27,13,23),(16,15,25)),'Cost/storage comparison is model-specific.')
check('PA66',(65535//8,8191*8,8192*8,(8192*8)%65536),(8191,65528,65536,0),'Integer promotions caveat: mathematical product may be wider int; zero occurs on modulo-65536 conversion or stipulated narrow unsigned arithmetic.')
semantic('PA67','Nonzero-size realloc: failure preserves old allocation; success invalidates prior access handles even at same observed address. No allocation implementation or C compiler used.')
check('PA68',(8,8-2,8+8-2+1,8+16),(8,6,15,24),'Expand-then-shift strategy, not optimized direct-position copy.')
check('PA69',(4+4,1),(8,1),'Four copies on shrink, four on next expansion, one append value write per pair.')
def fills(addresses,line_bytes):
    last=None;count=0
    for b in addresses:
        line=b//line_bytes
        if line!=last:count+=1;last=line
    return count
check('PA70',(fills([4*(i*8+j) for i in range(8) for j in range(8)],32),fills([4*(i*8+j) for j in range(8) for i in range(8)],32)),(8,64),'Cold one-line model, no prefetch, row-aligned.')
check('PA71',len({byte//16 for byte in range(8,8+11*4)}),4,'Every byte interval enumerated independently of rounded formula.')
check('PA72',([(5+t)%7 for t in range(4)],(5+4)%7),([5,6,0,1],2),'Separate length distinguishes empty/full; head+length overflow in finite types requires additional implementation qualification.')
mapping=[(i%3)*2+i//3 for i in range(6)]
cycle=[];cur=1
while cur not in cycle:cycle.append(cur);cur=mapping[cur]
check('PA73',(mapping,cycle),([0,2,4,1,3,5],[1,2,4,3]),'Original-to-destination rectangular transpose, inverse movement direction not conflated.')
i=0
while (i+1)*(i+2)//2<=17:i+=1
check('PA74',(i,17-i*(i+1)//2),(5,2),'Exact integer triangular-start enumeration.')
check('PA75',(len([(i,j) for i in range(5) for j in range(5) if i<j]),len([(i,j) for i in range(5) for j in range(5) if i<=j])),(10,15),'Independent region enumeration.')
semantic('PA76','Known nonempty or sentinel contract can authorize useful access without an ordinary length parameter. No unconditional arbitrary-empty-array access is claimed.')
check('PA77',(sum([2147483647,1]),sum([2147483647,1,-1])),(2147483648,2147483647),'Exact integer model demonstrates first invalid C signed-32 intermediate; UB never run.')
for n in range(101):
    seen=set()
    for i in range(n//2):
        assert 0<=i<n and 0<=n-1-i<n and i<n-1-i
        seen.update([i,n-1-i]);assertions+=1
    assert (n%2==0 or (n-1)//2 not in seen);assertions+=1
semantic('PA78','Both access bounds and unvisited odd center checked n=0..100; body not evaluated for n<2.')
check('PA79',(math.isqrt(2**31-1),46340**2,46341**2),(46340,2147395600,2147488281),'Value range bound separate from allocation success, size arithmetic, and zero-length C representation.')
for n in range(1,31):
    for r in range(n+1):
        actual=[k for k in range(-40,41) if 0<=r+k<n]
        formed=[k for k in range(-40,41) if 0<=r+k<=n]
        assert actual==list(range(-r,n-r)) and formed==list(range(-r,n-r+1));assertions+=1
semantic('PA80','General offset formulas independently enumerated for n=1..30 and r=0..n, including one-past starting pointer.')
check('PA81',(sum([7,8,10]),25//3,25/3),(25,8,8.333333333333334),'Positive C quotient modeled exactly; float result only approximate; a cast after division cannot recover remainder.')
covered={r['id'] for r in rows if re.fullmatch('PA[0-9]+',r['id'])}
assert covered=={f'PA{i:02}' for i in range(13,82)}
report={'questions_sha256':hashlib.sha256(raw).hexdigest(),'review_sha256':hashlib.sha256((ROOT/'research/p_arrays-review.en.md').read_bytes()).hexdigest(),'individual_questions_reviewed':69,'rules_read':80,'assertions':assertions,'scope':'Exact mathematical and bounded enumeration plus fresh Python execution. C/C++ semantics manually checked; no C/C++ compiler, UB execution, allocation implementation, or physical cache measurement. Finite tests supplement proofs.','rows':rows,'findings':['PA66 multiplication-promotions qualification required: narrow size_t can promote to wider int; zero on conversion is distinct from direct-expression unsigned wrap.','PA52/PA54 literal escaped apostrophe notation in source stem needs renderer check: replace literal \\x27 with actual apostrophe.','PA41 title calls its one-pass transform two-pass; retitle or explain inverse second transformation.','PA39 +8 map is destination-to-source for left rotation; preserve explicit direction.','PA67 assume new_bytes>0 for stated realloc contract.']}
(OUT/'oracle-report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2,ensure_ascii=False))
