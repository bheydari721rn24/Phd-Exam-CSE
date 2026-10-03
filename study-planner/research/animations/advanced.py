"""Additional geometric, transform, counting and certification walkthroughs."""
from common import *
from fractions import Fraction as F
from itertools import product
from math import comb
import cmath

def stars_bars():
    outcomes=[(a,b,4-a-b) for a in range(5) for b in range(5-a)];frames=[]
    for a,b,c in outcomes:
        seq=['*']*a+['|']+['*']*b+['|']+['*']*c
        frames.append(frame([node('s'+str(i),v,115+i*100,110,w=66,tone='active' if v=='|' else 'done') for i,v in enumerate(seq)],'Place two separating bars among four identical stars to encode a weak composition. Empty groups are valid, and the ordered group sizes are recovered uniquely from the bar positions.',{'First group':a,'Second group':b,'Third group':c,'Total':4,'All encodings':15},formula=r'\binom{4+3-1}{3-1}=15'))
    check('stars bars count',len(outcomes)==comb(6,2))
    scene('stars-bars','Stars and bars: empty groups and a bijective encoding','The objects are identical, the three groups are labeled, and zero occupancy is allowed. These assumptions determine the counting formula.','Four stars and two bars correspond bijectively to three nonnegative parts summing to four.',frames)
    frames=[]
    for mask in range(4):
        u=(1,2,3);sub=tuple(x for j,x in enumerate(u) if mask>>j&1);image=tuple(x%2 for x in sub)
        frames.append(frame([node('source',str(sub),220,100,w=310),node('image',str(sorted(set(image))),550,260,w=240)],'Take the image of the selected subset under reduction modulo two. Distinct inputs can enter the same fiber, so an image set discards repeated output values.',{'Selected subset':str(sub),'Image set':str(sorted(set(image)))},edges=[{'from':'source','to':'image','directed':True}]))
    scene('image-collapse','Set images: fiber collisions discard multiplicity','The finite function maps one, two and three to their parity. Compare this with the preimage animation, which collects every input in a target fiber.','A set image retains values, not the multiplicities of their preimages.',frames)

def norms_cross():
    frames=[]
    for p,label,val in [(1,'one-norm',7),(2,'Euclidean norm',5),('inf','infinity norm',4)]:
        frames.append(frame([node('x','3',220,100,tone='active'),node('y','4',540,100,tone='active'),node('norm',str(val),380,270,w=190,tone='done')],'Apply the '+label+' to the same vector with components three and four. Different norm definitions give different values even though the vector has not moved.',{'Vector':'(3,4)','Norm':label,'Result':val},formula={'one-norm':r'\|x\|_1=|3|+|4|=7','Euclidean norm':r'\|x\|_2=\sqrt{3^2+4^2}=5','infinity norm':r'\|x\|_\infty=\max(3,4)=4'}[label]))
    scene('vector-norms','Three norms of one vector','The vector is fixed. The formulas distinguish coordinate sum, Euclidean length and largest absolute coordinate.','Each norm uses its own definition; values from different norms are not interchangeable.',frames)
    frames=[]
    for order,sign in [('u then v',1),('v then u',-1),('u then u',0)]:
        nodes=[node('O','O',270,270,kind='point'),node('u','u=(2,0,0)',400,270,kind='point',size=18),node('v','v=(0,3,0)',270,75,kind='point',size=18),node('normal','normal '+str(6*sign),560,90,w=240,tone='warning' if sign<0 else 'done')]
        frames.append(frame(nodes,'Use the ordered '+order+' pair in the cross-product rule. The normal reverses when operands are exchanged and vanishes for a repeated vector.',{'Operand order':order,'Signed z component':6*sign,'Parallelogram area':abs(6*sign)},formula=rf'\text{{signed normal component}}={6*sign}',edges=[{'from':'O','to':'u','directed':True},{'from':'O','to':'v','directed':True}]))
    scene('cross-orientation','Cross product: orientation, area and degeneracy','The drawing is the xy plane; the labeled scalar is the perpendicular z component, not a falsely projected three-dimensional arrow.','The magnitude gives area, while operand order determines orientation.',frames)
    frames=[]
    for k in range(4):
        vals=[1,2,3,4];partial=sum(v*v for v in vals[:k+1]);nodes=[node('e'+str(i),v,240+(i%2)*220,95+(i//2)*110,tone='active' if i==k else 'done' if i<k else 'plain') for i,v in enumerate(vals)]
        frames.append(frame(nodes,'Add the square of the next matrix entry to the Frobenius-norm total. Diagonal trace and total entry-square mass are different matrix summaries.',{'Entries processed':k+1,'Square sum':partial,'Final trace':5},formula=rf'\|A\|_F^2={partial}'))
    scene('matrix-summaries','Trace versus Frobenius entry-square accumulation','The matrix entries are one, two, three and four in row-major order. Its trace is five, while its squared Frobenius norm is thirty.','The trace sums diagonal entries; the Frobenius norm squares and sums every entry.',frames)

def recurrences():
    frames=[]
    for level in range(4):
        count=2**level;size=8//count;toll=count*size
        nodes=[node('node'+str(i),str(size),380+(i-(count-1)/2)*(650/count),90,w=min(90,590/count),tone='active') for i in range(count)]
        nodes +=[node('level',f'{count} x {size} = {toll}',380,255,w=280,tone='done')]
        frames.append(frame(nodes,'Inspect one complete level of the equal-split recurrence tree. The number of subproblems doubles while each size halves, leaving the exact level work unchanged.',{'Level':level,'Nodes':count,'Size per node':size,'Level toll':toll,'Accumulated toll':8*(level+1)},formula=rf'2^{{{level}}}\cdot\frac{{8}}{{2^{{{level}}}}}=8'))
    scene('recurrence-levels','Critical recurrence: equal work at each level','For T(n)=2T(n/2)+n with n=8 and T(1)=1, the three internal levels and leaf level each contribute eight.','The exact example totals thirty-two; the level count creates the logarithmic factor.',frames)
    frames=[]
    for n in [3,5,7,9,11]:
        l=n//2;r=n-l;check('rounded split conserved',l+r==n and 0<l<n and 0<r<n)
        frames.append(frame([node('parent',str(n),380,80,w=130),node('left',str(l),210,240,w=130),node('right',str(r),550,240,w=130)],'Split an odd-size problem using floor and ceiling halves. The children differ by one, preserve the total input size, and remain strictly smaller than the non-base parent.',{'Parent size':n,'Floor half':l,'Ceiling half':r,'Child size sum':l+r},formula=rf'\lfloor{n}/2\rfloor+\lceil{n}/2\rceil={n}',edges=[{'from':'parent','to':'left','directed':True},{'from':'parent','to':'right','directed':True}]))
    scene('rounded-splits','Rounding: odd parents and unequal half sizes','The display tracks the exact integer subproblem sizes rather than silently replacing them by fractions.','Both children decrease, and their sizes sum to the parent size.',frames)

def fft():
    vals=[1,2,3,4];even=[4,-2];odd=[6,-2];X=[10,-2+2j,-2,-2-2j]
    ref=[sum(vals[k]*cmath.exp(-2j*cmath.pi*k*j/4) for k in range(4)) for j in range(4)]
    check('DFT4 exact convention',all(abs(a-b)<1e-10 for a,b in zip(X,ref)))
    frames=[]
    for stage in range(4):
        ns=[node('a'+str(i),str(v),95,65+i*85,w=90,tone='active' if stage==0 else 'plain') for i,v in enumerate(vals)]
        if stage>=1:ns +=[node('e'+str(i),str(v),330,80+i*160,w=125,tone='active' if stage==1 else 'done') for i,v in enumerate(even)]+[node('o'+str(i),str(v),490,80+i*160,w=125,tone='active' if stage==1 else 'done') for i,v in enumerate(odd)]
        if stage>=2:ns +=[node('x'+str(i),str(X[i]).replace('j','i'),660,65+i*85,w=170,tone='active') for i in range(4)]
        ed=[]
        if stage>=1:ed=[{'from':'a'+str(i),'to':('e' if i%2==0 else 'o')+str(j),'directed':True} for i in range(4) for j in range(2)]
        if stage>=2:ed +=[{'from':prefix+str(i%2),'to':'x'+str(i),'directed':True} for i in range(4) for prefix in ['e','o']]
        frames.append(frame(ns,'Perform '+['the ordered input display','the two length-two transforms on even and odd indices','the root-weighted butterfly recombination','the final transform verification'][stage]+'. The forward transform uses a negative complex exponential, fixing every twiddle sign.',{'Stage':stage,'Forward convention':'negative exponent','Twiddle for k=1':'-i'},formula=r'X_k=E_k+\omega_4^k O_k,\quad X_{k+2}=E_k-\omega_4^k O_k',edges=ed))
    scene('fft-butterfly','Four-point FFT: splitting and signed butterflies','The exact endpoints use integer real and imaginary parts. Butterfly arrows denote dependencies; the figure does not imply that crossing wires are connected.','Even and odd transforms combine with the same explicitly stated forward-transform convention.',frames)

def geometry():
    points=[(-2,0),(-1,2),(1,1),(2,3),(0,2)];frames=[];best=None;bestpair=None
    for i,j in [(0,1),(2,3),(1,4),(4,2),(1,2)]:
        d=sum((points[i][k]-points[j][k])**2 for k in range(2))
        if best is None or d<best:best=d;bestpair=(i,j)
        nodes=[node('p'+str(k),'P'+str(k),380+65*x,280-65*y,kind='point',tone='active' if k in [i,j] else 'plain',size=20) for k,(x,y) in enumerate(points)]
        frames.append(frame(nodes,'Inspect the next explicitly chosen candidate pair and compare its squared Euclidean distance with the best value saved so far. A valid closest-pair algorithm must justify why uninspected pairs can be excluded.',{'Candidate pair':str((i,j)),'Squared distance':d,'Best squared distance':best,'Saved best pair':str(bestpair)},formula=rf'd^2={d}',edges=[{'from':'p'+str(i),'to':'p'+str(j),'tone':'active'}]))
    allbest=min(sum((points[i][k]-points[j][k])**2 for k in range(2)) for i in range(5) for j in range(i+1,5));check('geometry witness minimum',best==allbest)
    scene('closest-pair','Closest pair: candidate distances and a retained witness','The scene displays selected candidates for one five-point instance; the chapter text supplies the strip-packing exclusion proof. It is not a simulation of every implementation optimization.','Squared distance comparisons avoid unnecessary square roots and preserve the chosen minimum.',frames)

def certificates():
    frames=[];edges=[(0,1,2),(0,2,5),(1,2,1),(2,3,3),(1,3,7)];dist=[0,2,3,6];parent=[None,0,1,2]
    for k,(u,v,w) in enumerate(edges):
        ns=[node('v'+str(i),f'{i}: d={dist[i]}',95+i*185,100,w=150,tone='active' if i in [u,v] else 'plain') for i in range(4)]
        check('distance certificate edge',dist[v]<=dist[u]+w)
        frames.append(frame(ns,'Check the displayed directed edge against the candidate distance labels. Every edge inequality prevents an unexplained shorter path, while tight rooted parent paths witness that the claimed distances are attainable.',{'Edge':f'{u} to {v}','Weight':w,'Edge inequality':f'{dist[v]} <= {dist[u]+w}','Parent of destination':parent[v]},formula=rf'd_{{{v}}}\le d_{{{u}}}+{w}',edges=[{'from':'v'+str(u),'to':'v'+str(v),'directed':True,'tone':'active'}]))
    check('parent rooted witness',all(parent[v] is not None and dist[v]==dist[parent[v]]+next(w for u,t,w in edges if u==parent[v] and t==v) for v in range(1,4)))
    scene('shortest-path-certificate','Shortest paths: local inequalities and rooted witnesses','The certificate is for a directed graph with nonnegative weights. Feasible labels alone do not prove equality with shortest distances; rooted tight paths supply the second half.','Edge inequalities lower-bound path costs, and rooted tight parent paths attain each claimed distance.',frames)

stars_bars();norms_cross();recurrences();fft();geometry();certificates()
