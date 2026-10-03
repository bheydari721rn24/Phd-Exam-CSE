"""Independent finite models, invariant checks, counterexamples and artifact bindings."""
import collections,itertools,json,math,re
from fractions import Fraction
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
counts=collections.Counter()
def checked(kind,p):
    assert p,kind
    counts[kind]+=1
def lower(a,t,faulty=False):
    lo,hi=0,len(a);midpoints=[]
    while lo<hi:
        if list(a)==sorted(a):checked('search checkpoint',0<=lo<=hi<=len(a) and all(x<t for x in a[:lo]) and all(x>=t for x in a[hi:]))
        mid=(lo+hi)//2;midpoints.append(mid);old=(lo,hi)
        if a[mid]<t:lo=mid if faulty else mid+1
        else:hi=mid
        if (lo,hi)==old:return None,midpoints
        checked('search progress',hi-lo<old[1]-old[0] and hi-lo<=(old[1]-old[0])//2)
    if list(a)==sorted(a):checked('search exit',all(x<t for x in a[:lo]) and all(x>=t for x in a[lo:]))
    return lo,midpoints
for n in range(8):
    for a in itertools.combinations_with_replacement(range(-2,3),n):
        for t in range(-3,4):
            result,trace=lower(a,t);expected=next((i for i,x in enumerate(a) if x>=t),n)
            checked('search output',result==expected)
            checked('search bound',len(trace)<=(n.bit_length() if n else 0))
checked('faulty search witness',lower([2],3,True)[0] is None)
checked('unsorted witness',lower([4,1,3],3)[0]==2)

def insertion(a,unstable=False):
    b=list(enumerate(a));shifts=0
    for i in range(1,len(b)):
        key=b[i];j=i-1;original=collections.Counter(b[:i+1])
        while j>=0 and (b[j][1]>=key[1] if unstable else b[j][1]>key[1]):
            b[j+1]=b[j];j-=1;shifts+=1
            logical=b[:j+1]+b[j+2:i+1]+[key]
            checked('saved-key conservation',collections.Counter(logical)==original)
        b[j+1]=key
        checked('sorted prefix',all(b[k][1]<=b[k+1][1] for k in range(i)))
    return b,shifts
def partition(a,p,faulty=False):
    b=list(a);lt=i=0;gt=len(b);steps=0
    while i<gt:
        checked('partition regions',0<=lt<=i<=gt<=len(b) and all(x<p for x in b[:lt]) and all(x==p for x in b[lt:i]) and all(x>p for x in b[gt:]))
        old=gt-i
        if b[i]<p:b[lt],b[i]=b[i],b[lt];lt+=1;i+=1
        elif b[i]>p:
            gt-=1;b[i],b[gt]=b[gt],b[i]
            if faulty:i+=1
        else:i+=1
        steps+=1
        if not faulty:checked('partition exact progress',gt-i==old-1)
    return b,lt,gt,steps
for n in range(7):
    for a in itertools.product(range(3),repeat=n):
        b,shifts=insertion(a)
        checked('stable sorting',b==sorted(enumerate(a),key=lambda x:x[1]))
        checked('shift inversion identity',shifts==sum(a[i]>a[j] for i in range(n) for j in range(i+1,n)))
        for p in range(3):
            b,lt,gt,steps=partition(a,p)
            checked('partition output',collections.Counter(b)==collections.Counter(a) and all(x<p for x in b[:lt]) and all(x==p for x in b[lt:gt]) and all(x>p for x in b[gt:]) and steps==n)
checked('unstable insertion witness',[i for i,x in insertion([2,2],True)[0]]==[1,0])
b,lt,gt,_=partition([3,1],2,True)
checked('faulty partition witness',any(x!=2 for x in b[lt:gt]))

for X in range(120):
    for Y in range(1,25):
        q=0;r=X;steps=0
        while r>=Y:
            checked('division invariant',X==q*Y+r and q>=0 and r>=0)
            old=r;r-=Y;q+=1;steps+=1
            checked('division progress',0<=r<old)
        checked('division result',(q,r)==divmod(X,Y) and steps==X//Y)
for A in range(80):
    for B in range(80):
        a,b=A,B
        while b:
            checked('gcd invariant',math.gcd(a,b)==math.gcd(A,B))
            old=b;a,b=b,a%b
            checked('gcd progress',0<=b<old)
        checked('gcd result',a==math.gcd(A,B))
def power(x,y,M=None):
    r,b,e=(1,x,y) if M is None else (1%M,x%M,y);odd=squares=0;states=[]
    while e>0:
        checked('power invariant',r*b**e==x**y if M is None else (r*pow(b,e,M)-pow(x,y,M))%M==0)
        if e%2:r=r*b if M is None else r*b%M;odd+=1
        b=b*b if M is None else b*b%M;e//=2;squares+=1;states.append((r,b,e))
    checked('power result',r==x**y if M is None else r==pow(x,y,M))
    checked('power counts',odd==y.bit_count() and squares==y.bit_length())
    return r,states,odd,squares
for x in range(-5,6):
    for y in range(41):power(x,y)
for M in range(1,32):
    for x in range(17):
        for y in range(25):power(x,y,M)
for a in range(256):
    for b in range(256):checked('pre-multiplication overflow test',(a*b>255)==(b!=0 and a>255//b))

# Backward conditions are compared with independent forward execution on finite inputs.
for x in range(-30,31):
    checked('quadratic weakest precondition',((x+3)**2==25)==(x in (-8,2)))
    final=-(x) if x<0 else x+2
    checked('conditional weakest precondition',(final>=3)==(x<=-3 or x>=1))
for a in itertools.product(range(3),repeat=3):
    for i,j in itertools.product(range(3),repeat=2):
        b=list(a);b[i]=1;b[j]=2
        checked('array alias condition',(b[i]==1 and b[j]==2)==(i!=j))

# Exhaustive three-vertex nonnegative graphs, with brute simple-path optimal values.
edges=[(u,v) for u in range(3) for v in range(3) if u!=v]
def certificate(edge,d,parent):
    if d[0]!=0:return False
    if any(d[v]>d[u]+w for (u,v),w in edge.items()):return False
    for v in (1,2):
        seen=set();cur=v
        while cur!=0:
            if cur in seen or cur not in parent:return False
            seen.add(cur);p=parent[cur]
            if (p,cur) not in edge or d[cur]!=d[p]+edge[p,cur]:return False
            cur=p
    return True
for weights in itertools.product([None,0,2],repeat=6):
    edge={uv:w for uv,w in zip(edges,weights) if w is not None}
    optimum=[0,math.inf,math.inf]
    for v in (1,2):
        for middle in [(),(3-v,)]:
            path=(0,)+middle+(v,)
            if all(uv in edge for uv in zip(path,path[1:])):optimum[v]=min(optimum[v],sum(edge[uv] for uv in zip(path,path[1:])))
    accepted=False
    for a,b in itertools.product(range(5),repeat=2):
        d=[0,a,b]
        for p1,p2 in itertools.product(range(3),repeat=2):
            if certificate(edge,d,{1:p1,2:p2}):
                accepted=True;checked('certificate soundness',d==optimum)
    checked('certificate completeness on bounded graphs',accepted==all(x<math.inf for x in optimum))
checked('parent cycle counterexample',not certificate({(0,1):5,(1,2):0,(2,1):0},[0,0,0],{1:2,2:1}))
checked('negative-edge certificate',certificate({(0,1):4,(0,2):5,(1,2):-3},[0,4,1],{1:0,2:1}))

# Calculated answers are bound to their stored alternative, not just hard-coded answer letters.
qs={q['id']:q for q in json.loads((BASE/'a_correct-questions.json').read_text())}
bindings={
 'AC01':(sorted(x for x in range(-20,21) if (x+3)**2==25),[-8,2],r'$x=2$ or $x=-8$'),
 'AC02':([x for x in range(-10,11) if 2*(x+1)-3==7],[4],r'$x=4$'),
 'AC13':(lower([1,3,3,3,8,9],3),(1,[3,1,0]),r'Midpoints $(3,1,0)$; result one'),
 'AC14':(max(len(lower(list(range(31)),t)[1]) for t in range(-1,33)),5,'Five'),
 'AC19':(insertion([4,2,3,1])[1],5,'Five'),
 'AC25':(partition([3,1,2,3,0],2)[1:3],(2,3),r'$(2,3)$'),
 'AC29':(divmod(47,6),(7,5),r'$(7,5)$ and seven'),
 'AC33':(power(3,13)[1][1],(3,81,3),r'$(3,81,3)$'),
 'AC34':(power(2,45)[2:],(4,6),'Four and six'),
 'AC37':((((200*200)%256)%251,(200*200)%251),(64,91),'Wrapped result 64; exact result 91'),
 'AC45':(sum(Fraction(1,2**d) for d in [1,2,3]),Fraction(7,8),r'$7/8$; it does not prove fullness'),
 'AC47':(list(range(9,-1,-2)),[9,7,5,3,1],'Source one; length five'),
}
for id,(value,expected,alternative) in bindings.items():
    checked('numeric question binding',value==expected and qs[id]['options'][qs[id]['answer']-1]==alternative)
checked('authentic count calculation',10+sum(1 for i in range(1,16) for j in range(i,16) for k in range(j,16))==690)
for n in range(31):checked('exact dependent-loop formula',sum(1 for i in range(1,n+1) for j in range(i,n+1) for k in range(j,n+1))==math.comb(n+2,3))
for n in range(51):checked('odd-sum formula',sum(2*k-1 for k in range(1,n+1))==n*n)
page=(ROOT/'dist/chapters/a_correct.html').read_text(encoding='utf-8')
checked('artifact problem count',page.count('<section class="exam-question"')==54 and page.count('<details class="exam-solution"')==54)
checked('artifact note count',page.count('<section class="review-rule"')==74)
checked('artifact diagrams',page.count('<svg ')==5)
checked('approval state',all(c['status']=='ready' for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters'] if c['topicId']!='a_correct'))
for q in qs.values():
    checked('question structure',len(q['options'])==4 and len(set(q['options']))==4 and len(q['solution'].split())>=40)
    for value in [q['stem'],q['solution']]+q['options']:
        checked('source text integrity',value.count('$')%2==0 and not any(ord(c)<32 and c not in '\n\t\r' for c in value))
report=dict(chapter='a_correct',checks=sum(counts.values()),byKind=dict(counts),numericAnswerBindings=list(bindings),domains={'search':'sorted arrays length 0..7, values -2..2, targets -3..3','sortingPartition':'all arrays length 0..6 over 0..2; pivots 0..2','division':'dividend 0..119, divisor 1..24','gcd':'both operands 0..79','exactPower':'base -5..5, exponent 0..40','modularPower':'modulus 1..31, base 0..16, exponent 0..24','overflow':'all pairs of eight-bit unsigned operand values','certificates':'729 three-vertex directed graphs; absent/zero/two edge weights; exhaustive bounded labels and parent candidates'},limits='Finite models do not prove unbounded theorems; other alternatives and symbolic claims received editorial derivation review, not independent automated universal proof.')
(BASE/'a_correct-validation.json').write_text(json.dumps(report,indent=2)+chr(10),encoding='utf-8')
public=ROOT/'dist/evidence/a_correct';public.mkdir(exist_ok=True,parents=True)
(public/'validation.json').write_text(json.dumps(report,indent=2)+chr(10),encoding='utf-8')
print(json.dumps(report,indent=2))
