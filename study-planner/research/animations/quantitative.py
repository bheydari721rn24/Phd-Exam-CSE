"""Exact finite mathematical models; geometric positions are display coordinates."""
from common import *
from fractions import Fraction as F
from itertools import product,combinations
from math import comb,sqrt,log2

def lattice():
    frames=[];seen=[]
    for i in range(1,6):
        for j in range(1,i+1):
            seen.append((i,j))
            nodes=[node(f'{a}-{b}',f'{a},{b}',130+b*80,35+a*51,w=60,h=38,tone='active' if (a,b)==(i,j) else 'done' if (a,b) in seen else 'plain',size=18) for a in range(1,6) for b in range(1,a+1)]
            frames.append(frame(nodes,'Visit exactly one feasible index pair in the triangular iteration region. Each row contributes its own length rather than the full outer bound.',{'Outer index':i,'Inner index':j,'Visited pairs':len(seen),'Row length':i},formula=rf'\sum_{{i=1}}^{{5}}i=15',snapshot={'i':i,'j':j,'count':len(seen)}))
    check('triangle exact count',len(seen)==15)
    scene('loop-triangle','Triangular loops: exact iteration lattice','Every cell is one loop-body execution. The unvisited region is visible, so dependent loop limits cannot be replaced by a rectangular product.','The feasible indices satisfy $1\le j\le i\le5$. Each pair is visited exactly once.',frames,['for i = 1,...,5','    for j = 1,...,i','        execute body once'])
    frames=[]
    for k,x in enumerate([1,2,4,8,16]):
        frames.append(frame([node('x',f'x = {x}',90+k*130,130,tone='active'),node('bound','bound = 17',380,270,w=190)],'Double the positive loop variable after one constant-cost visit. The next value determines whether the guard can still succeed.',{'Visit':k+1,'Value':x,'Next value':2*x,'Guard x < 17':True},formula=rf'x=2^{{{k}}}',line=1))
    scene('loop-doubling','Multiplicative progress: count levels, not increments','The example uses exact positive integers; fixed-width overflow would invalidate this termination argument.','The visited values are powers of two strictly below the bound.',frames,['x = 1','while x < 17: visit; x = 2*x'])

def cost_models():
    frames=[];carry=0;out=[]
    for k in range(4):
        a=(7>>k)&1;b=(3>>k)&1;s=a+b+carry;out.append(s%2);carry=s//2
        nodes=[node('a'+str(j),(7>>j)&1,210+(3-j)*100,80,tone='active' if j==k else 'plain') for j in range(4)]+[node('b'+str(j),(3>>j)&1,210+(3-j)*100,155,tone='active' if j==k else 'plain') for j in range(4)]+[node('o'+str(j),v,210+(3-j)*100,250,tone='done') for j,v in enumerate(out)]
        frames.append(frame(nodes,'Propagate the carry from the current low-order bit toward the next higher bit. A bit operation is a different cost unit from a whole-word instruction.',{'Processed bits':k+1,'Carry out':carry,'Word additions':1,'Bit stages so far':k+1},line=1,snapshot={'bits':out[:],'carry':carry}))
    check('ripple exact result',sum(b<<k for k,b in enumerate(out))+carry*16==10)
    scene('word-bit-cost','Word operations versus bit-level carry work','A four-bit ripple model illustrates cost accounting; it is not a claim about the physical implementation of a processor adder.','Seven plus three equals ten. A word-RAM instruction and bit-stage work are counted separately.',frames,['add two bounded words as one RAM instruction','or charge each ripple bit stage in a bit model'])
    frames=[]
    for k in range(1,7):
        n=2**k;frames.append(frame([node('bits',f'{k+1} bits',170,100,w=190),node('value',str(n),550,100,w=190),node('work',f'{n} visits',550,260,w=210)],'Increase the numeric parameter by doubling it. An algorithm visiting every value up to this parameter has work exponential in its binary encoding length.',{'Numeric parameter':n,'Encoding length':n.bit_length(),'Enumerated values':n},formula=rf'N=2^{{{k}}}',edges=[{'from':'bits','to':'value','directed':True},{'from':'value','to':'work','directed':True}]))
    scene('encoding-length','Numeric value versus encoding length','This distinction explains pseudo-polynomial bounds. The table records exact positive-integer binary lengths including the leading one.','For this family, $N=2^k$ has $k+1$ binary digits.',frames)
    frames=[]
    for n in [1,2,4,8,16,32]:
        f=3*n+7;g=n;frames.append(frame([node('f',f'3n+7 = {f}',200,100,w=225),node('g',f'n = {n}',560,100,w=185),node('ratio',f'ratio = {F(f,g)}',380,260,w=240,tone='done' if n>=7 else 'warning')],'Evaluate the growth ratio at a concrete input size. The symbolic bound below, rather than these finitely many observations alone, proves the eventual comparison.',{'n':n,'Exact ratio':str(F(f,g)),'Upper bound 4n holds':f<=4*n},formula=r'n\ge7\Rightarrow 3n+7\le4n',counterexample=n<7))
    scene('growth-threshold','Asymptotic bounds: constants and a valid threshold','Finite observations illustrate the threshold. The displayed inequality supplies the all-input argument for the chosen upper bound.','For $n\ge7$, $3n\le3n+7\le4n$, hence the function is $\Theta(n)$.',frames)

def probability():
    atoms=list(product([0,1],repeat=3));frames=[]
    for i,a in enumerate(atoms):
        nodes=[node('a'+str(j),''.join(map(str,b)),110+(j%4)*180,90+(j//4)*110,w=100,tone='active' if j==i else 'done' if j<i else 'plain') for j,b in enumerate(atoms)]
        frames.append(frame(nodes,'Expose one equally likely elementary outcome of three independent fair trials. Events are sets of these outcomes, and their masses add without counting an outcome twice.',{'Atom probability':'1/8','Outcomes exposed':i+1,'Exposed mass':str(F(i+1,8))},formula=rf'P(\Omega)={F(8,8)}'))
    scene('probability-atoms','Sample spaces: disjoint atoms and probability mass','The model assumes three independent fair binary trials. Unequal atoms would require their own explicit weights.','Eight disjoint atoms each have probability $1/8$; their union has total probability one.',frames)
    A={a for a in atoms if a[0]==1};B={a for a in atoms if sum(a)>=2};seen=set();frames=[]
    for title,event in [('A',A),('B',B),('Intersection',A&B),('Union',A|B)]:
        nodes=[node('a'+str(j),''.join(map(str,b)),110+(j%4)*180,90+(j//4)*110,w=100,tone='active' if b in event else 'plain') for j,b in enumerate(atoms)]
        frames.append(frame(nodes,'Select the '+title.lower()+' event from the same fixed atoms. Shared atoms belong to the intersection and must be subtracted once in the union calculation.',{'Event':title,'Selected atoms':len(event),'Probability':str(F(len(event),8))},formula=r'P(A\cup B)=P(A)+P(B)-P(A\cap B)'))
    check('prob union exact',F(len(A|B),8)==F(len(A),8)+F(len(B),8)-F(len(A&B),8))
    scene('probability-union','Inclusion–exclusion: overlapping event mass','The event A fixes the first trial to one; B requires at least two ones. Every view uses the same sample space.','Union mass counts shared atoms once, not twice.',frames)
    frames=[];mass=F(0)
    for k in range(1,7):
        mass+=F(1,2**k);nodes=[node('t'+str(j),str(F(1,2**j)),75+j*90,100,w=82,tone='active' if j==k else 'done') for j in range(1,k+1)]
        frames.append(frame(nodes,'Add the next disjoint geometric-probability atom to an increasing event sequence. The finite remainder quantifies the mass not yet included.',{'Included atoms':k,'Included mass':str(mass),'Remaining mass':str(1-mass)},formula=rf'P(A_{{{k}}})=1-2^{{-{k}}}'))
    scene('probability-limit','Continuity from below: mass approaching a limit','The six checkpoints illustrate an infinite disjoint construction. The exact geometric formula proves convergence; a finite animation does not prove countable additivity.','The increasing events have mass $1-2^{-k}$ and limiting mass one.',frames)
    frames=[];pairs=list(product([0,1],repeat=2))
    for a,b in pairs:
        z=a^b;frames.append(frame([node('x',f'X = {a}',170,100),node('y',f'Y = {b}',590,100),node('z',f'Z = {z}',380,250,tone='active')],'Observe one of four equally likely pairs and compute its parity. Any two variables are independent, but the third is determined by the first two.',{'Atom mass':'1/4','X':a,'Y':b,'Z = X xor Y':z},formula=r'P(X=0,Y=0,Z=0)=1/4\ne1/8',edges=[{'from':'x','to':'z'},{'from':'y','to':'z'}],counterexample=True))
    for i,j in [(0,1),(0,2),(1,2)]:check('pairwise parity independence',all(sum((a,b,a^b)[i]==u and (a,b,a^b)[j]==v for a,b in pairs)==1 for u,v in pairs))
    scene('pairwise-independence','Pairwise independence does not imply mutual independence','The example is an exact four-outcome probability model. A parity constraint persists even though all two-variable marginals factor.','Each pair is independent; the triple intersection can fail product factorization.',frames)
    draws=list(combinations(range(5),2));frames=[]
    for k,d in enumerate(draws):
        good=sum(i<3 for i in d)==1;nodes=[node('ball'+str(i),'R' if i<3 else 'B',100+i*130,100,tone='active' if i in d else 'plain') for i in range(5)]
        frames.append(frame(nodes,'Inspect one unordered draw of two distinct balls without replacement. Exactly one red ball is a successful outcome, and every unordered pair has the same probability.',{'Draw':k+1,'Success':good,'All pairs':10,'Successful pairs':6},formula=r'P(\text{one red})=\frac{\binom31\binom21}{\binom52}=\frac35',counterexample=False))
    check('hypergeometric count',sum(sum(i<3 for i in d)==1 for d in draws)==6)
    scene('draw-without-replacement','Counting probabilities without replacement','Three red and two blue labeled balls are sampled uniformly as unordered pairs. Replacement or ordered sampling requires a changed denominator.','The favorable unordered pairs number six out of ten.',frames)

def vectors():
    def pt(id,x,y,tone='plain'):return node(id,id+' = ('+str(x)+','+str(y)+')',300+65*x,245-65*y,kind='point',geometry=True,tone=tone,size=18)
    frames=[];u=(2,0);v=(1,1)
    for title,points,eds,formula in [('First vector',[pt('O',0,0),pt('u',*u)],[('O','u')],r'u=(2,0)'),('Translate the second vector',[pt('O',0,0),pt('u',*u),pt('v',3,1)],[('O','u'),('u','v')],r'u+v=(3,1)'),('Equivalent diagonal',[pt('O',0,0),pt('u',*u),pt('v',3,1)],[('O','v')],r'(2,0)+(1,1)=(3,1)')]:
        frames.append(frame(points,'Construct '+title.lower()+' by translating a directed vector without changing its components. The endpoint of the chained displacement equals the componentwise sum.',{'u':str(u),'v':str(v),'Sum':'(3,1)'},formula=formula,edges=[dict(from_=a,to=b) for a,b in []]))
        frames[-1]['edges']=[{'from':a,'to':b,'directed':True} for a,b in eds]
    scene('vector-addition','Vector addition: translated arrows and the sum','The coordinate scale is fixed and identical on both axes. Translation moves a free vector without changing its length or direction.','Componentwise addition and head-to-tail geometric addition agree.',frames)
    a=(2,1);b=(1,2);dot=4;bb=5;t=F(dot,bb);p=(t,t*2);r=(F(2)-p[0],F(1)-p[1]);check('projection residual orthogonal',r[0]*b[0]+r[1]*b[1]==0)
    frames=[]
    for i,(title,pts) in enumerate([('Original vectors',[pt('O',0,0),pt('a',*a),pt('b',*b)]),('Projected point',[pt('O',0,0),pt('a',*a),pt('b',*b),pt('p',*p)]),('Orthogonal residual',[pt('O',0,0),pt('a',*a),pt('b',*b),pt('p',*p)])]):
        eds=[{'from':'O','to':'b','directed':True},{'from':'O','to':'a','directed':True}]+([{'from':'O','to':'p','directed':True}] if i else [])+([{'from':'p','to':'a','directed':True,'tone':'active'}] if i==2 else [])
        frames.append(frame(pts,'Display the '+title.lower()+' using one fixed Euclidean coordinate system. Subtracting the projection isolates a residual whose dot product with the projection direction is exactly zero.',{'Coefficient':str(t),'Projection':str(p),'Residual':str(r),'Residual dot b':0},formula=r'p=\frac{a\cdot b}{b\cdot b}b=\frac45(1,2)',edges=eds))
    scene('projection','Projection: parallel component and orthogonal residual','Projection is onto the nonzero vector (1,2) under the Euclidean inner product. A different inner product changes the formula.','The residual is orthogonal to the projection direction and $a=p+r$.',frames)
    frames=[]
    u=(1,1);v=(2,0);q=(1,-1);check('Gram Schmidt dot',sum(x*y for x,y in zip(u,q))==0)
    for i,val in enumerate([v,(1,1),q]):
        nodes=[pt('O',0,0),pt('u',*u),pt('v',*val)]
        if i==1:nodes[-1].update(labelDy=50,labelDx=80)
        frames.append(frame(nodes,'Separate the second input vector into its component along the first vector and its remaining independent direction. Normalize only after the orthogonal residual has been obtained.',{'Stage':['input','parallel component','orthogonal residual'][i],'Dot of final residual with u':0},formula=[r'v=(2,0)',r'\operatorname{proj}_u v=(1,1)',r'v-\operatorname{proj}_u v=(1,-1)'][i],edges=[{'from':'O','to':'u','directed':True},{'from':'O','to':'v','directed':True,'tone':'active'}]))
    scene('gram-schmidt','Gram–Schmidt: subtract before normalizing','The geometric example is two-dimensional. A zero residual signals dependence and cannot be normalized.','Subtracting the parallel component produces an orthogonal residual; normalization preserves orthogonality.',frames)
    frames=[]
    for origin in [(0,0),(1,0),(1,1)]:
        points=[pt('O',*origin),pt('P',2,1),pt('Q',3,2)];points[0]['labelDy']=50
        frames.append(frame(points,'Move the chosen coordinate origin while keeping the physical points fixed. Their position vectors change, but the displacement from P to Q remains the same.',{'Origin':str(origin),'P relative to origin':str((2-origin[0],1-origin[1])),'Q minus P':'(1,1)'},edges=[{'from':'O','to':'P','directed':True},{'from':'P','to':'Q','directed':True}]))
    scene('affine-origin','Affine points: origin-dependent coordinates and invariant displacement','The plane displays fixed physical points. Moving the origin changes coordinates rather than translating these points.','Point differences are translation-invariant vectors.',frames)

def matrices():
    A=[[1,2],[3,4]];B=[[2,0],[1,2]];frames=[];C=[[0,0],[0,0]]
    for i,j,k in product(range(2),repeat=3):
        C[i][j]+=A[i][k]*B[k][j]
        nodes=[node('a'+str(r)+str(c),A[r][c],90+c*85,75+r*85,tone='active' if (r,c)==(i,k) else 'plain') for r,c in product(range(2),repeat=2)]+[node('b'+str(r)+str(c),B[r][c],340+c*85,75+r*85,tone='active' if (r,c)==(k,j) else 'plain') for r,c in product(range(2),repeat=2)]+[node('c'+str(r)+str(c),C[r][c],590+c*85,75+r*85,tone='done' if (r,c)==(i,j) else 'plain') for r,c in product(range(2),repeat=2)]
        frames.append(frame(nodes,'Multiply the highlighted row entry by the matching column entry and add the product to exactly one output cell. The shared inner index is summed; the output indices remain fixed.',{'Output row':i+1,'Output column':j+1,'Inner index':k+1,'Partial output':C[i][j]},formula=rf'C_{{{i+1}{j+1}}}=\sum_{{k=1}}^2 A_{{{i+1}k}}B_{{k{j+1}}}',snapshot={'C':[r[:] for r in C],'i':i,'j':j,'k':k}))
    check('matrix multiplication exact',C==[[4,4],[10,8]])
    scene('matrix-product','Matrix multiplication: row–column accumulation','The matrices have compatible two-by-two shapes. Matrix multiplication is ordered and differs from entrywise multiplication.','An output entry is a dot product over the shared inner dimension.',frames)
    frames=[]
    for k in range(5):
        nodes=[node('e'+str(i)+str(j),A[i][j],150+j*100 if q>=k else 460+i*100,90+i*100 if q>=k else 90+j*100,tone='active' if q==k-1 else 'plain') for q,(i,j) in enumerate(product(range(2),repeat=2))]
        frames.append(frame(nodes,'Move each labeled matrix entry into its transposed position without changing its value. The old row index becomes the new column index, and the old column index becomes the new row index.',{'Entries moved':k,'Original shape':'2 by 2','Transposed shape':'2 by 2'},formula=r'(A^T)_{ji}=A_{ij}'))
    scene('matrix-transpose','Transpose: preserve identity while exchanging indices','Each entry keeps its identity as it moves from the left matrix to the right matrix. Rectangular matrices exchange their dimensions too.','Transposition exchanges row and column roles without multiplying or conjugating entries.',frames)
    # Elementary row operations are simultaneous within a row and preserve solutions.
    states=[[[F(1),F(2),F(5)],[F(3),F(4),F(11)]],[[F(1),F(2),F(5)],[F(0),F(-2),F(-4)]],[[F(1),F(2),F(5)],[F(0),F(1),F(2)]],[[F(1),F(0),F(1)],[F(0),F(1),F(2)]]];frames=[]
    for k,M in enumerate(states):
        check('row operation known solution',all(row[0]*1+row[1]*2==row[2] for row in M))
        nodes=[node('m'+str(i)+str(j),str(M[i][j]),230+j*150,100+i*110,w=110,tone='active' if k and i==(0 if k==3 else 1) else 'plain') for i,j in product(range(2),range(3))]
        frames.append(frame(nodes,'Apply the '+['initial augmented-system display','row replacement using the unchanged first row','nonzero row scaling','elimination above the second pivot'][k]+'. Every transformed equation has the same solution pair as the original system.',{'Operation':['initial','R2 <- R2 - 3 R1','R2 <- -R2 / 2','R1 <- R1 - 2 R2'][k],'Solution x':1,'Solution y':2},formula=r'(x,y)=(1,2)',snapshot={'matrix':[[str(x) for x in r] for r in M]}))
    scene('row-elimination','Elimination: equivalent equations and exact fractions','Rows represent equations, and elementary invertible row operations preserve the complete solution set. Floating-point pivoting is a separate numerical concern.','Each displayed augmented system is equivalent to the initial system.',frames)
    frames=[];points=[(0,0),(1,0),(0,1)];origin=(310,230)
    def geom(ps):return [node('v'+str(i),['O','e1','e2'][i],origin[0]+85*x,origin[1]-85*y,kind='point',geometry=True,size=20) for i,(x,y) in enumerate(ps)]
    rotate=lambda p:(-p[1],p[0]);shear=lambda p:(p[0]+p[1],p[1])
    for name,ps,motion in [('original',points,None),('rotate then shear: rotation',[rotate(p) for p in points],{'kind':'rotation','cx':310,'cy':230,'angle':-3.141592653589793/2}),('rotate then shear: shear',[shear(rotate(p)) for p in points],None),('reset original',points,None),('shear then rotate: shear',[shear(p) for p in points],None),('shear then rotate: rotation',[rotate(shear(p)) for p in points],{'kind':'rotation','cx':310,'cy':230,'angle':-3.141592653589793/2})]:
        frames.append(frame(geom(ps),'Apply '+name+' to the same labeled basis points. Composition acts from right to left, so reversing the two operations can produce different final coordinates.',{'Stage':name,'First basis image':str(ps[1]),'Second basis image':str(ps[2])},edges=[{'from':'v0','to':'v1','directed':True},{'from':'v0','to':'v2','directed':True}],**({'motion':motion} if motion else {})))
    check('composition noncommutative',shear(rotate((1,0)))!=rotate(shear((1,0))))
    scene('matrix-composition','Ordered composition: rotation and shear do not commute','The rotation uses an exact quarter-turn endpoint and an analytic circular interpolation. Shear uses its linear continuous path; the reset is explicitly identified.','The same basis vectors distinguish the two ordered compositions.',frames)

def residues():
    frames=[]
    for k in range(6):
        x=2+3*k;ok=x%5==3
        nodes=[node('candidate',str(x),110+k*105,100,tone='done' if ok else 'warning'),node('first','mod 3: 2',220,260,w=210),node('second',f'mod 5: {x%5}',540,260,w=210,tone='done' if ok else 'warning')]
        frames.append(frame(nodes,'Keep the first congruence satisfied while moving through its arithmetic progression. Check the second congruence on each candidate; successful candidates repeat modulo the combined coprime modulus.',{'Candidate':x,'First remainder':2,'Second remainder':x%5,'Both constraints':ok},formula=r'x\equiv2\pmod3,\quad x\equiv3\pmod5',counterexample=not ok))
    check('CRT representative',8%3==2 and 8%5==3)
    scene('crt-intersection','Chinese remainder theorem: intersection of residue progressions','The moduli three and five are coprime. The successful representative is eight, and all solutions differ by fifteen.','Candidates preserve the first congruence; both congruences select one residue modulo fifteen.',frames)
    frames=[]
    for t in range(-2,3):
        x=1+3*t;y=1-2*t;check('Diophantine family',4*x+6*y==10)
        frames.append(frame([node('x',f'x = {x}',200,110,w=180),node('y',f'y = {y}',560,110,w=180),node('sum',str(4*x+6*y),380,280,tone='done')],'Move along the integer solution family by the homogeneous step. Increasing x by three and decreasing y by two leaves the equation unchanged.',{'Parameter t':t,'Left side':4*x+6*y,'Required right side':10},formula=r'(x,y)=(1+3t,1-2t)',edges=[{'from':'x','to':'sum'},{'from':'y','to':'sum'}]))
    scene('integer-family','Linear Diophantine equations: all integer solutions','The gcd of four and six is two and divides ten. The parameter step uses coefficients divided by this gcd.','Every displayed pair solves $4x+6y=10$; the complete family uses integer $t$.',frames)

lattice();cost_models();probability();vectors();matrices();residues()
