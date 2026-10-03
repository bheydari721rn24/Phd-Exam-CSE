"""Exact state transitions for algorithm animations; no prerecorded video."""
import math,itertools
from collections import Counter
from fractions import Fraction
from common import *

def insertion(values,id='insertion',unstable=False):
    records=list(enumerate(values));arr=records[:];frames=[];shifts=0
    def snap(caption,line,i=0,j=None,saved=None):
        nodes=[node('cell'+str(k),str(k),90+92*k,170,w=58,h=34,tone='muted',size=18) for k in range(len(arr))]
        for k,item in enumerate(arr):
            if item is not None:nodes.append(node('record'+str(item[0]),str(item[1])+' · '+chr(97+item[0]),90+92*k,100,tone='done' if k<i else 'plain'))
        if saved is not None:nodes+=[node('record'+str(saved[0]),str(saved[1])+' · '+chr(97+saved[0]),380,270,tone='active'),node('hole','hole',90+92*(j+1),100,tone='active')]
        else:
            if i<len(arr):
                for n in nodes:
                    if n['id']=='record'+str(arr[i][0]):n['tone']='active'
        logical=[x for x in arr if x is not None]+([saved] if saved is not None else [])
        check(id+' full record preservation',Counter(logical)==Counter(records))
        frames.append(frame(nodes,caption,{'Pass':i,'Scan':j if j is not None else '—','Shifts':shifts},line=line,snapshot={'array':arr,'saved':saved,'input':records}))
    snap('Begin with tagged records; equal keys can be distinguished by their original letters.',0)
    for i in range(1,len(arr)):
        saved=arr[i];arr[i]=None;j=i-1
        snap('Save the next key outside the array. Its old position is now the logical hole.',1,i,j,saved)
        while j>=0 and (arr[j][1]>=saved[1] if unstable else arr[j][1]>saved[1]):
            snap('Compare the saved key with the predecessor. A shift is required by this comparison rule.',2,i,j,saved)
            arr[j+1]=arr[j];arr[j]=None;j-=1;shifts+=1
            snap('Move the predecessor record into the hole. The hole moves one position left; the saved record stays outside.',3,i,j,saved)
        arr[j+1]=saved
        check(id+' sorted prefix',all(arr[k][1]<=arr[k+1][1] for k in range(i)))
        snap('Fill the hole with the saved record. The expanded prefix is sorted and its complete multiset is restored.',4,i+1)
    stable=arr==sorted(records,key=lambda r:r[1]);check(id+' intended stability',stable!=unstable)
    frames[-1].update(counterexample=unstable,status='Sorted keys, but equal-key records changed order: this is a stability counterexample.' if unstable else 'Sorted keys, preserved records and original equal-key order all hold.')
    return scene(id,'Insertion sort: saved key and moving hole'+(' — unstable tie rule' if unstable else ''),'Follow tagged records through each comparison and shift. Letters identify original records, not additional sorting keys.',r'The non-hole records plus the saved key preserve the input multiset. The completed prefix is sorted.',frames,['for each next record:','save the record; create a logical hole','shift while predecessor '+('>=' if unstable else '>')+' saved key','shift predecessor; move hole left','restore saved key into the hole'])

def merge(left,right,id='merge'):
    a=[('L'+str(i),v) for i,v in enumerate(left)];b=[('R'+str(i),v) for i,v in enumerate(right)];out=[];i=j=0;frames=[];comparisons=0
    def snap(caption,line,active=()):
        nodes=[node(k,str(v)+' · '+k,100+90*t,80,tone='active' if k in active else 'muted' if t<i else 'plain') for t,(k,v) in enumerate(a)]
        nodes +=[node(k,str(v)+' · '+k,100+90*t,180,tone='active' if k in active else 'muted' if t<j else 'plain') for t,(k,v) in enumerate(b)]
        emitted={k:t for t,(k,v) in enumerate(out)}
        for n in nodes:
            if n['id'] in emitted:n.update(x=90+92*emitted[n['id']],y=290,tone='done')
        check(id+' sorted output prefix',all(out[t][1]<=out[t+1][1] for t in range(len(out)-1)))
        check(id+' conservation',Counter(out+a[i:]+b[j:])==Counter(a+b))
        frames.append(frame(nodes,caption,{'Left cursor':i,'Right cursor':j,'Comparisons':comparisons,'Emitted':len(out)},line=line,snapshot={'left':a,'right':b,'output':out,'i':i,'j':j}))
    snap('Two sorted input lists are ready. The bottom row will contain their stable merged output.',0)
    while i<len(a) and j<len(b):
        comparisons+=1;snap('Compare the two current heads. Equal values choose the left head to preserve cross-half stability.',1,(a[i][0],b[j][0]))
        if a[i][1]<=b[j][1]:out.append(a[i]);i+=1
        else:out.append(b[j]);j+=1
        snap('Move the chosen complete record to the output. Only that input cursor advances.',2)
    while i<len(a) or j<len(b):
        if i<len(a):out.append(a[i]);i+=1
        else:out.append(b[j]);j+=1
        snap('One list is exhausted. Append the next remaining record without comparing a nonexistent head.',3)
    check(id+' final merge',out==sorted(a+b,key=lambda r:r[1]))
    return scene(id,'Stable merge: two heads and the exhausted tail','The top two rows are the original lists. A record moves to the output rather than being silently replaced.',r'The output prefix is sorted. Output plus unconsumed input suffixes preserves every original record.',frames,['initialize two cursors and empty output','compare heads while both exist','emit smaller head; take left on equality','append the remaining sorted tail'])

def sorting_extra(kind,values):
    arr=list(enumerate(values));frames=[]
    def snap(caption,line,active=()):
        nodes=[node('r'+str(r),str(v)+' · '+chr(97+r),90+92*i,110,tone='active' if i in active else 'plain') for i,(r,v) in enumerate(arr)]
        check(kind+' record preservation',Counter(arr)==Counter(enumerate(values)))
        frames.append(frame(nodes,caption,{'Current keys':', '.join(str(v) for r,v in arr)},line=line,snapshot={'array':arr}))
    snap('The input records start in their original positions. Each following comparison or swap is shown separately.',0)
    if kind=='selection':
        for i in range(len(arr)-1):
            m=i
            for j in range(i+1,len(arr)):
                snap('Inspect the next candidate against the current minimum of the unprocessed suffix.',1,(m,j))
                if arr[j][1]<arr[m][1]:m=j
            arr[i],arr[m]=arr[m],arr[i];snap('Move the suffix minimum to its final prefix position by a complete-record swap.',2,(i,m))
    else:
        for end in range(len(arr)-1,0,-1):
            for j in range(end):
                snap('Compare adjacent records in the current unsorted prefix before deciding whether to exchange them.',1,(j,j+1))
                if arr[j][1]>arr[j+1][1]:arr[j],arr[j+1]=arr[j+1],arr[j];snap('Exchange an inverted adjacent pair. Equal keys are left in their original order.',2,(j,j+1))
            snap('This pass has moved the largest remaining key to the right boundary.',3,(end,))
    check(kind+' sorted result',[v for r,v in arr]==sorted(values))
    snap('Every prefix or suffix obligation is now complete, and the final keys are nondecreasing.',3)
    return scene(kind,kind.capitalize()+' sort: exact comparisons and record swaps','This additional construction helps compare operation counts and preservation claims across sorting methods.',r'Every swap preserves record identities. The finalized region satisfies the algorithm-specific ordering invariant.',frames,['begin with the input array','inspect the relevant candidates','swap only under the stated comparison rule','finalize the pass boundary'])

def binary(a,target,id='lower-bound',faulty=False):
    lo=0;hi=len(a);frames=[];steps=0
    def snap(caption,line,mid=None,stall=False):
        nodes=[node('v'+str(i),v,90+92*i,110,tone='done' if i<lo or i>=hi else 'active' if i==mid else 'plain') for i,v in enumerate(a)]
        nodes+=[node('lo','lo = '+str(lo),100+lo*72,250,w=110,tone='active'),node('hi','hi = '+str(hi),100+hi*72,310,w=110,tone='active')]
        invariant=all(x<target for x in a[:lo]) and all(x>=target for x in a[hi:]);check(id+' classification',invariant)
        frames.append(frame(nodes,caption,{'Target':target,'Lower':lo,'Upper':hi,'Width':hi-lo,'Bodies':steps},line=line,counterexample=stall,snapshot={'array':a,'target':target,'lo':lo,'hi':hi},status='Classification holds, but the nonempty interval repeats; strict progress fails.' if stall else 'Both classified regions satisfy their inequalities at this checkpoint.'))
    snap('Initialize a half-open interval containing the entire array. Classified outer regions are initially empty.',0)
    while lo<hi:
        mid=(lo+hi)//2;snap('Inspect the floor midpoint. Sortedness will justify discarding a whole side from this one value.',1,mid);old=(lo,hi);steps+=1
        if a[mid]<target:lo=mid if faulty else mid+1
        else:hi=mid
        if old==(lo,hi):snap('The faulty update keeps the same one-element interval. This exact state will repeat forever.',2,mid,True);break
        check(id+' strict progress',hi-lo<old[1]-old[0]);snap('Update the appropriate boundary. The unresolved interval strictly shrinks and classifications remain valid.',2)
    if lo==hi:snap('The unresolved interval is empty. The coincident boundaries identify the first eligible position.',3)
    return scene(id,'Lower bound: '+('minimal stalling counterexample' if faulty else 'duplicate-aware interval elimination'),'Green records have been classified. Boundary cards expose the exact interval and its decreasing width.',r'All valid indices below $lo$ have value below the target; all at or above $hi$ have value at least the target.',frames,['lo = 0; hi = n','mid = lo + (hi-lo)//2; inspect A[mid]','if below target: lo = '+('mid (FAULT)' if faulty else 'mid+1')+'; else: hi = mid','return lo when lo == hi'])

def partition(values,pivot,id='partition3',faulty=False):
    records=list(enumerate(values));arr=records[:];lt=i=0;gt=len(arr);frames=[]
    def snap(caption,line,broken=False):
        nodes=[node('r'+str(r),str(v)+' · '+chr(97+r),90+92*k,110,tone='done' if k<lt or k>=gt else 'active' if k==i and k<gt else 'plain') for k,(r,v) in enumerate(arr)]
        valid=all(v<pivot for r,v in arr[:lt]) and all(v==pivot for r,v in arr[lt:i]) and all(v>pivot for r,v in arr[gt:])
        if not broken:check(id+' region invariant',valid)
        check(id+' record multiset',Counter(arr)==Counter(records))
        nodes +=cards_region(lt,i,gt)
        frames.append(frame(nodes,caption,{'Pivot':pivot,'Less end':lt,'Scan':i,'Greater start':gt,'Unknown width':max(0,gt-i)},line=line,counterexample=broken,status='The equal region contains an unclassified non-equal value; this variant is incorrect.' if broken else 'All classified regions and the full record multiset are preserved.',snapshot={'array':arr,'lt':lt,'i':i,'gt':gt,'pivot':pivot}))
    snap('Initialize the less and equal regions as empty; every input record starts in the unknown region.',0)
    while i<gt:
        snap('Inspect the scan record and compare it with the pivot before selecting a branch.',1)
        if arr[i][1]<pivot:arr[lt],arr[i]=arr[i],arr[lt];lt+=1;i+=1
        elif arr[i][1]>pivot:
            gt-=1;arr[i],arr[gt]=arr[gt],arr[i]
            if faulty:i+=1
        else:i+=1
        broken=not(all(v==pivot for r,v in arr[lt:i]))
        snap('After a greater-side swap, the incoming record still needs inspection; advancing the scan can violate the equal-region claim.' if faulty else 'Classify exactly one unknown record. A greater-side swap keeps the scan in place to inspect the incoming value.',2,broken)
        if broken:break
    if not faulty:snap('No unknown records remain. Region membership is established, but sorting within the outer regions is not promised.',3)
    return scene(id,'Three-way partition'+(' — skipped-record counterexample' if faulty else ' — four moving regions'),'Records keep their identity during swaps. Boundary values identify less, equal, unknown and greater slices.',r'The unknown region is $[i,gt)$. Its length decreases by one in each correct body; swaps preserve the record multiset.',frames,['lt = i = 0; gt = n','inspect A[i]','less: swap and advance; equal: advance; greater: shrink gt and swap','stop when i == gt'])
def cards_region(lt,i,gt):
    return [node('lt','lt = '+str(lt),150,250,w=130),node('i','i = '+str(i),380,250,w=130,tone='active'),node('gt','gt = '+str(gt),610,250,w=130)]

def euclid(A,B,id='euclid'):
    a,b=A,B;x0,y0,x1,y1=1,0,0,1;frames=[]
    def snap(caption,line):
        check(id+' gcd preservation',math.gcd(a,b)==math.gcd(A,B));check(id+' Bezout rows',a==A*x0+B*y0 and b==A*x1+B*y1)
        nodes=cards([f'a = {a}',f'b = {b}',f'gcd = {math.gcd(a,b)}',f'({x0}, {y0})',f'({x1}, {y1})'])
        frames.append(frame(nodes,caption,{'Original inputs':f'{A}, {B}','Remainder':b,'Coefficient rows':f'({x0},{y0}); ({x1},{y1})'},formula=rf'{a}={A}\cdot({x0})+{B}\cdot({y0})',line=line,snapshot={'a':a,'b':b,'A':A,'B':B,'x0':x0,'y0':y0,'x1':x1,'y1':y1}))
    snap('Start with the original operands and coefficient rows that reconstruct each operand exactly.',0)
    while b:
        q=a//b;a,b=b,a%b;x0,x1=x1,x0-q*x1;y0,y1=y1,y0-q*y1;snap('Use the old divisor and remainder simultaneously. The same row operation updates the Bézout coefficients.',1)
    snap('The remainder is zero. The first row gives both the gcd and an exact Bézout certificate.',2)
    return scene(id,'Euclid and extended Euclid: simultaneous remainder updates','The first three cards show operands and gcd; the lower cards track coefficients of the immutable inputs.',r'The gcd is unchanged. Each operand remains an integer linear combination of the original inputs.',frames,['a=A; b=B; initialize coefficient rows','q=a//b; (a,b)=(b,a-q*b); update both rows','return a and its coefficient row'])

def division(X,Y,id='division'):
    q=0;r=X;frames=[]
    def snap(caption,line):
        check(id+' conservation',X==q*Y+r and r>=0)
        nodes=[node('unit'+str(k),str(k+1),60+(k%9)*80,75+(k//9)*80,w=58,h=38,tone='done' if k<q*Y else 'active',size=18) for k in range(X)]
        nodes +=[node('q','q = '+str(q),150,280,w=130),node('r','r = '+str(r),380,280,w=130,tone='active'),node('Y','Y = '+str(Y),610,280,w=130)]
        frames.append(frame(nodes,caption,{'Dividend':X,'Divisor':Y,'Quotient':q,'Remainder':r},formula=rf'{X}={q}\cdot{Y}+{r}',line=line,snapshot={'X':X,'Y':Y,'q':q,'r':r}))
    snap('Initially the entire dividend is unallocated remainder; the quotient counts no removed groups yet.',0)
    while r>=Y:r-=Y;q+=1;snap('Remove one full positive-divisor group from the remainder and add one to the quotient.',1)
    snap('The remainder is now smaller than the positive divisor, establishing the unique division result.',2)
    return scene(id,'Division: quotient groups and conserved remainder','Each step subtracts exactly one group. The live identity connects the evolving state to the original dividend.',r'$X=qY+r$ and $r\ge0$ hold throughout. The positive divisor makes the remainder decrease strictly.',frames,['q=0; r=X','while r>=Y: r-=Y; q+=1','return q,r when 0<=r<Y'])

def power(x,y,M=None,id='power'):
    r,b,e=(1,x,y) if M is None else (1%M,x%M,y);frames=[]
    def snap(caption,line):
        check(id+' conserved power',r*b**e==x**y if M is None else r*pow(b,e,M)%M==pow(x,y,M))
        frames.append(frame(cards([f'r = {r}',f'b = {b}',f'e = {e}']),caption,{'Original base':x,'Original exponent':y,'Modulus':M or 'exact integers'},formula=rf'{r}\cdot {b}^{{{e}}}'+(rf'\equiv {pow(x,y,M)}\pmod{{{M}}}' if M is not None else rf'={x}^{{{y}}}'),line=line,snapshot={'r':r,'b':b,'e':e,'x':x,'y':y,'M':M}))
    snap('Initialize the accumulator, evolving base and remaining exponent from the immutable input contract.',0)
    while e:
        old=e;rb=r*b if e%2 else r;r=rb if M is None else rb%M;b=b*b if M is None else b*b%M;e//=2
        snap('The old exponent was '+('odd, so multiply the accumulator by the old base; ' if old%2 else 'even, so keep the accumulator; ')+'then square the base and halve the exponent.',1)
    snap('The remaining exponent is zero. The accumulator is the requested value in the stated arithmetic model.',2)
    return scene(id,'Exponentiation by squaring'+(' modulo '+str(M) if M else ' over exact integers'),'Each animation checkpoint is after a complete body, so the power invariant is valid at every displayed state.',r'The accumulator times the evolving base raised to the remaining exponent equals the original power, or is congruent modulo the stated modulus.',frames,['r=1; b=x; e=y (normalize for a modulus)','if e is odd: r*=b; then b*=b; e//=2','return r when e=0'])

def recursion_tree(n=8,id='recursion-tree',unequal=False):
    frames=[];nodes=[];edges=[];work=0;queue=[('root',n,380,65,0,760)]
    while queue:
        name,size,x,y,depth,span=queue.pop(0);nodes.append(node(name,str(size),x,y,w=62,tone='active'));work+=size
        if size>1:
            left=size//4 if unequal else size//2;left=max(1,left);right=size-left
            for k,child in enumerate((left,right)):
                childname=name+str(k);cx=x+(-1 if k==0 else 1)*span/4;queue.append((childname,child,cx,y+65,depth+1,span/2));edges.append(dict(from_=name,to=childname))
        validedges=[{'from':e['from_'],'to':e['to'],'directed':True} for e in edges if e['to'] in {a['id'] for a in nodes}]
        frames.append(frame(nodes,'Expand this exact subproblem and charge its own size once. Child sizes sum to their parent before rounding-free split work is counted.',{'Expanded node':name,'Node size':size,'Accumulated toll':work},line=1,edges=validedges,snapshot={'nodeSize':size,'work':work}))
        for a in nodes:a['tone']='done'
    check(id+' leaf count',sum(a['label']=='1' for a in nodes)==n)
    return scene(id,'Exact recursion tree'+(' with unequal children' if unequal else ' with equal children'),'The example charges size at every node, including a unit leaf. Node expansion order is a visualization order, not a parallel runtime claim.',r'Every split preserves total child size and strictly decreases positive non-leaf sizes. The total charge is the sum of the displayed node tolls.',frames,['T(1)=1','T(n)=T(left)+T(right)+n'])

def merge_recursion(values,id='merge-recursion'):
    frames=[];nodes=[];edges=[];result={}
    def visit(a,name,x,y,span):
        nodes.append(node(name,', '.join(map(str,a)) or 'empty',x,y,w=max(65,min(220,35*len(a))),tone='active'))
        frames.append(frame(nodes,'Enter a recursive call with this exact subsequence. Children must be smaller unless this is a base case.',{'Active length':len(a),'Active call':name},line=0,edges=edges))
        if len(a)<=1:out=a[:]
        else:
            m=len(a)//2;l=name+'L';r=name+'R'
            edges.append({'from':name,'to':l,'directed':True});left=visit(a[:m],l,x-span/4,y+80,span/2)
            edges.append({'from':name,'to':r,'directed':True});right=visit(a[m:],r,x+span/4,y+80,span/2);out=sorted(left+right)
        check('merge recursion preservation',Counter(out)==Counter(a))
        for nd in nodes:
            if nd['id']==name:nd.update(label=', '.join(map(str,out)) or 'empty',tone='done')
        frames.append(frame(nodes,'Return a sorted sequence with exactly the same multiset. The child contracts and merge lemma justify this parent result.',{'Returned length':len(out),'Returned call':name},line=2,edges=edges))
        return out
    visit(values,'root',380,55,760)
    return scene(id,'Merge sort: recursive calls and return contracts','The tree shows when subproblems are entered and when their complete sorting contracts are returned. Use the stable-merge animation for the individual merge emissions.',r'Each returned sequence is sorted and preserves its call input. Non-base child lengths are strictly smaller.',frames,['enter call; if length<=1, return','split into two smaller calls','merge the sorted children; return'])

def max_subarray():
    a=[4,-6,8,-2,3,-9,5];frames=[]
    def summary(x):return (sum(x),max(sum(x[:k]) for k in range(1,len(x)+1)),max(sum(x[k:]) for k in range(len(x))),max(sum(x[i:j]) for i in range(len(x)) for j in range(i+1,len(x)+1)))
    left=summary(a[:3]);right=summary(a[3:]);combined=(left[0]+right[0],max(left[1],left[0]+right[1]),max(right[2],right[0]+left[2]),max(left[3],right[3],left[2]+right[1]))
    check('maximum subarray exact combine',combined==summary(a))
    for k,title in enumerate(['total','prefix','suffix','best']):
        nodes=array_nodes(a,start=65,gap=103,tones={i:'active' if k==3 and 2<=i<5 else 'plain' for i in range(7)})
        nodes+=[node('left','Left: '+str(left[k]),180,240,w=170),node('right','Right: '+str(right[k]),580,240,w=170),node('parent','Parent: '+str(combined[k]),380,310,w=190,tone='done')]
        frames.append(frame(nodes,'Combine the '+title+' component using the two adjacent summaries. For the best component, compare both internal answers with the crossing suffix-plus-prefix answer.',{'Component':title,'Left summary':str(left),'Right summary':str(right),'Parent summary':str(combined)},line=k,edges=[{'from':'left','to':'parent'},{'from':'right','to':'parent'}]))
    return scene('max-subarray','Maximum subarray: four sufficient summary components','The chosen convention requires a nonempty interval; an all-negative input would not return an empty interval of sum zero.',r'The adjacent summaries contain total, best nonempty prefix, best nonempty suffix and best nonempty subarray.',frames,['total = left.total + right.total','prefix = max(left.prefix, left.total+right.prefix)','suffix = max(right.suffix, right.total+left.suffix)','best = max(left.best, right.best, left.suffix+right.prefix)'])

def karatsuba():
    steps=[('Split both inputs using the same base-ten low-part width.',[3,7,2,4],''),('Compute the high product from the two high parts.',[3,2,6],r'z_2=3\cdot2=6'),('Compute the low product from the two low parts.',[7,4,28],r'z_0=7\cdot4=28'),('Compute the signed difference product; both differences are negative in this example.',[-4,-2,8],r'z_d=(-4)(-2)=8'),('Recover the mixed coefficient from the three products, retaining their exact signs.',[6,28,8,26],r'6+28-8=26'),('Reconstruct the full product using shifts by the stated low-part width.',[600,260,28,888],r'37\cdot24=600+260+28=888')]
    check('Karatsuba reconstruction',37*24==6*100+26*10+28)
    frames=[frame(cards(vals),caption,{'Base':10,'Low-part width':1,'Recursive products':min(i,3)},formula=f,line=min(i,3)) for i,(caption,vals,f) in enumerate(steps)]
    return scene('karatsuba','Karatsuba: signed differences and exact reconstruction','Follow the shared split, three products and reconstruction. This is exact scalar integer arithmetic; the recursive size proof remains in the text.',r'The common low-part width determines every shift. Signed intermediate products are preserved without taking absolute values.',frames,['split x and y at the same width','compute high, low and difference products','mixed = high + low - difference','combine shifted coefficients'])

def strassen():
    A=[[1,2],[3,4]];B=[[5,6],[7,8]];P=[-2,24,35,8,65,-30,-22];frames=[]
    formulas=[r'P_1=1(6-8)=-2',r'P_2=(1+2)8=24',r'P_3=(3+4)5=35',r'P_4=4(7-5)=8',r'P_5=(1+4)(5+8)=65',r'P_6=(2-4)(7+8)=-30',r'P_7=(1-3)(5+6)=-22']
    for k in range(7):
        nodes=[node('p'+str(i),'P'+str(i+1)+' = '+str(P[i]),130+(i%4)*165,100+(i//4)*95,w=140,tone='active' if i==k else 'done') for i in range(k+1)]
        frames.append(frame(nodes,'Compute this one Strassen product from its explicitly defined ordered factors. Retain the sign for later recombination.',{'Products computed':k+1,'Ordinary products replaced':8},formula=formulas[k],line=0))
    C=[[P[4]+P[3]-P[1]+P[5],P[0]+P[1]],[P[2]+P[3],P[0]+P[4]-P[2]-P[6]]]
    check('Strassen ordered reconstruction',C==[[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)])
    frames.append(frame(cards([f'C11 = {C[0][0]}',f'C12 = {C[0][1]}',f'C21 = {C[1][0]}',f'C22 = {C[1][1]}']),'Recombine the seven saved products into four output entries. Direct multiplication gives the same result.',{'Output rows':str(C),'Products':7},line=1))
    return scene('strassen','Strassen: seven products with fixed signs','The scalar two-by-two example makes each product and recombination visible. For blocks, operand order and dimension compatibility remain essential.',r'Use one fixed product convention throughout; do not mix recombination formulas from a different convention.',frames,['compute the seven defined products','recombine them into four compatible output blocks'])

insertion([4,2,3,1,3,2]);insertion([2,1,2,2],id='insertion-unstable',unstable=True)
merge([1,4,7],[2,4,8]);sorting_extra('selection',[4,2,3,1]);sorting_extra('bubble',[4,2,3,1])
binary([1,3,3,3,8,9],3);binary([2],3,id='search-stall',faulty=True)
partition([3,1,2,3,0],2);partition([3,1],2,id='partition-skip',faulty=True)
euclid(84,30);division(17,3);power(3,13);power(5,9,12,id='modular-power')
recursion_tree();merge_recursion([4,1,3,2]);max_subarray();karatsuba();strassen()
