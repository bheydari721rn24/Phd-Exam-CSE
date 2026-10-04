"""Rank concepts with exact snapshots and genuine coordinate movement."""
from common import node,frame,scene,check
from gauss_exact import reduce,mattex,matrix,multiply
from fractions import Fraction as F
import sympy as S

A=[[1,2,0,1,0],[0,0,1,1,0],[1,2,0,1,1],[-1,-2,0,-1,0]]
r,p,e,steps=reduce(A,5);frames=[]
for s in steps:
 nodes=[node(f'row{rid}c{j}',v,115+120*j,65+70*i,w=80,h=45,size=22,tone='active' if j in s['pivots'] else 'plain') for i,(rid,row) in enumerate(zip(s['ids'],s['matrix'])) for j,v in enumerate(row)]
 frames.append(frame(nodes,s['op']+'. The same invertible transform acts on all five columns. Dependency coefficients and the kernel are preserved, while the original pivot columns must be taken from the unreduced matrix.',{'Pivots found':len(s['pivots']),'Input coordinates':5,'Final rank':3},formula=r'Ax=0\quad\Longleftrightarrow\quad EAx=0',snapshot=dict(kind='rank-reduction',input=A,**s)))
scene('rank-pivots','Locate independent columns without replacing their coordinates','Equation cells move with their complete rows during reduction. The final pivot indices select original output vectors.','Each checkpoint is an exact invertible left transformation; the final matrix has rank three and nullity two.',frames)

def point(id,x,y,panel=0):
 return node(id,'',180+panel*390+55*x,190-45*y,kind='point',w=0,h=0)
frames=[]
for a in [S.Rational(0),S.Rational(1,2),S.Rational(1)]:
 v=[1-a,a];E=[[1-a,-a],[a,1-a]]
 frames.append(frame([point('origin',0,0),point('tip',*v),node('legend','Column-space direction',530,80,w=320,h=42,size=22)],'An invertible output transformation moves the image line from the first axis toward the second. The nonzero direction moves continuously, so its dimension stays one although the actual column space changes.',{'Parameter':str(a),'Rank':1,'Kernel dimension':0},formula=r'\operatorname{Col}(EA)=E\operatorname{Col}(A)',edges=[{'from':'origin','to':'tip'}],snapshot=dict(kind='column-transform',E=[[str(x) for x in row] for row in E],A=[[1],[0]],v=list(map(str,v)))))
scene('rank-column-transform','Same rank, a different column-space line','A nonzero output direction moves under a reversible change of output coordinates.','The determinant of E is (1−t)²+t², positive along the full interpolation interval; image position moves but rank remains one.',frames)

frames=[]
for t in [-1,0,1,2,3]:
 x=[3-t,t]
 frames.append(frame([point('input',*x),point('fiber-a',4,-1),point('fiber-b',0,3),node('inputlabel','Input: ('+str(x[0])+', '+str(x[1])+')',220,320,w=320,h=35,size=21),node('output','Measured sum: 3',570,190,w=285,h=60,size=23)],'The input point moves along the drawn compatible line while the measured sum stays three. One independent kernel direction changes the input without changing its output, demonstrating a fiber rather than a unique point.',{'Free parameter':t,'First coordinate':x[0],'Second coordinate':x[1],'Output':3},formula=r'x=(3,0)^T+t(-1,1)^T',edges=[{'from':'fiber-a','to':'fiber-b'}],snapshot=dict(kind='fiber',A=[[1,1]],x=x,b=[3])))
scene('rank-fibers','Different inputs with the same attainable output','The point moves along a line of solutions; its measured value is fixed.','All interpolated inputs retain coordinate sum three because the path direction is a kernel vector.',frames)

frames=[]
for t in [F(0),F(1,2),F(1)]:
 M=[[F(1),F(0)],[F(0),1-t]]
 nodes=[point(f'p{i}',x,float((1-t)*y),1) for i,(x,y) in enumerate([(-1,-1),(-1,1),(0,-1),(0,1),(1,-1),(1,1)])]
 nodes+=[node('title','Outputs of six distinct inputs',380,35,w=440,h=35,size=23),node('rank','Exact rank '+str(2 if t!=1 else 1),190,300,w=240,h=45,size=22)]
 frames.append(frame(nodes,'The second output coordinate contracts continuously to zero. Rank stays two at every nonsingular stage and becomes one only at the final collapse; the newly lost direction is the second input axis.',{'Parameter':str(t),'Rank':2 if t!=1 else 1,'Nullity':0 if t!=1 else 1},formula=r'A_t=\begin{bmatrix}1&0\\0&1-t\end{bmatrix}',snapshot=dict(kind='rank-map',matrix=[[str(v) for v in row] for row in M],inputs=[[-1,-1],[-1,1],[0,-1],[0,1],[1,-1],[1,1]],outputs=[[str(x),str((1-t)*y)] for x,y in [(-1,-1),(-1,1),(0,-1),(0,1),(1,-1),(1,1)]])))
scene('rank-collapse','A two-dimensional image collapses to a line','Six actual outputs move under an exact diagonal map until pairs become indistinguishable.','Exact rank is integer-valued and drops only at t=1; it is not continuously interpolated.',frames)

frames=[]
for v in [[1,0],[1,1],[0,1]]:
 nodes=[point('bo',0,0),point('bt',*v),point('ao',0,0,1),point('at',v[0],0,1),node('bl','Image of B',180,320,w=220,h=35,size=21),node('al','Image of A B',570,320,w=250,h=35,size=21)]
 frames.append(frame(nodes,'The first map reaches one intermediate direction. The second map keeps only its first coordinate; once the reached direction lies entirely in the second-axis kernel, the composition loses that direction completely.',{'Rank B':1,'Intersection dimension':int(v[0]==0),'Rank A B':int(v[0]!=0)},formula=r'\operatorname{rank}(AB)=\operatorname{rank}B-\dim(\operatorname{Col}B\cap\ker A)',edges=[{'from':'bo','to':'bt'},{'from':'ao','to':'at','tone':'active'}],snapshot=dict(kind='composition',A=[[1,0],[0,0]],B=[[v[0]],[v[1]]],AB=[[v[0]],[0]])))
scene('rank-composition','The intersection that determines product rank','The intermediate line rotates toward a killed direction while its projected output shrinks to zero.','Both checkpoints and interpolated segments keep B nonzero; the product rank falls only when its first coordinate vanishes.',frames)

frames=[]
for t in [F(0),F(1,2),F(1)]:
 inputs=[[-1,-1],[-1,1],[1,-1],[1,1]]
 nodes=[point(f'c{i}',float((1-t)*x),float((1-t)*y),1) for i,(x,y) in enumerate(inputs)]
 nodes+=[node('formula','A + B = (1 − t) I',230,80,w=330,h=45,size=22),node('dimension','Rank '+str(2 if t!=1 else 0),230,280,w=220,h=45,size=22)]
 frames.append(frame(nodes,'Two-dimensional output freedom remains while the scalar is nonzero. At complete cancellation every input output reaches the origin, so the sum has rank zero despite the nonzero individual factor ranks.',{'t':str(t),'Sum rank':2 if t!=1 else 0},formula=r'A=I,\quad B=-tI,\quad A+B=(1-t)I',snapshot=dict(kind='rank-map',matrix=[[str(1-t),'0'],['0',str(1-t)]],inputs=inputs,outputs=[[str((1-t)*x),str((1-t)*y)] for x,y in inputs])))
scene('rank-cancellation','Rank of a sum can collapse completely','Four output points genuinely contract to a common zero output under cancellation.','The shared input map is I−tI; individual ranks do not add under cancellation.',frames)

frames=[]
for t in [0,1,2,1]:
 a=[[1,1,1],[1,t,1],[1,1,t]];rank=S.Matrix(a).rank()
 nodes=[node(f'v{i}{j}',v,160+180*j,80+80*i,w=110,h=50,size=24,tone='active' if i==j and i>0 else 'plain') for i,row in enumerate(a) for j,v in enumerate(row)]
 frames.append(frame(nodes,'The two independent diagonal differences both vanish at the same exceptional parameter value. Inspect the undivided equations: rank drops directly from three to one, with no rank-two branch to insert.',{'t':t,'Rank':rank,'Nullity':3-rank},formula=r'R_2-R_1=(0,t-1,0),\quad R_3-R_1=(0,0,t-1)',snapshot=dict(kind='parameter-rank',t=t,matrix=a,rank=rank)))
scene('rank-parameters','One parameter removes two restrictions at once','The actual parameter entries and both rank counts update at each branch.','All branch statements come from row subtraction before division; t=1 is treated separately.',frames)

frames=[]
C=S.Matrix([[1,1],[2,0],[0,1]]);Fmat=S.Matrix([[1,2,0],[0,0,1]])
for x in [[1,0,0],[0,1,0],[0,0,1],[1,-1,2]]:
 z=Fmat*S.Matrix(x);y=C*z
 nodes=[node('x','x: '+', '.join(map(str,x)),150,85,w=260,h=55,size=21),node('z','F x: '+', '.join(map(str,z)),380,180,w=260,h=55,size=21),node('y','C F x: '+', '.join(map(str,y)),610,275,w=260,h=55,size=21)]
 frames.append(frame(nodes,'The three input coordinates pass through exactly two independent intermediate coordinates, then produce a three-coordinate output. The second input column duplicates twice the first direction, while the third supplies the other independent output direction.',{'Input dimension':3,'Bottleneck dimension':2,'Rank':2},formula=r'A=CF',edges=[{'from':'x','to':'z'},{'from':'z','to':'y'}],snapshot=dict(kind='factorization',C=[list(row) for row in [[1,1],[2,0],[0,1]]],F=[[1,2,0],[0,0,1]],x=x,z=list(map(int,z)),y=list(map(int,y)))))
scene('rank-factorization','Two coordinates suffice to reproduce every column','Exact values flow through a rank factorization with a minimal intermediate space.','C has independent columns and F has independent rows; every shown output is C(Fx).',frames)

frames=[]
for t in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
 x=[1+2*t,1-t]
 nodes=[point('input',float(x[0]),float(x[1])),point('image',3,0),point('origin',0,0),node('legend','P(x,y) = (x + 2y, 0)',535,80,w=350,h=45,size=22)]
 frames.append(frame(nodes,'The point moves to its projected image along the kernel direction rather than along a perpendicular. Its image stays fixed, and the final point is fixed by a second application of the same idempotent map.',{'t':str(t),'Input':','.join(map(str,x)),'Image':'3,0'},formula=r'P=\begin{bmatrix}1&2\\0&0\end{bmatrix},\quad P^2=P',edges=[{'from':'origin','to':'image','tone':'active'},{'from':'input','to':'image','dashed':True}],snapshot=dict(kind='projection',P=[[1,2],[0,0]],x=list(map(str,x)),y=[3,0])))
scene('rank-projection','An oblique projection does not move perpendicularly','The actual input moves along a null direction toward a fixed image point.','The path stays in the same fiber throughout interpolation; idempotence is not a claim of symmetry.',frames)

frames=[]
for t in [F(0),F(1,2),F(1)]:
 a=[[1-t,0],[-2*t,1]];inputs=[[1,0],[0,1],[1,2]]
 outs=[[a[0][0]*x,a[1][0]*x+y] for x,y in inputs]
 nodes=[point(f'u{i}',float(x),float(y),1) for i,(x,y) in enumerate(outs)]
 nodes+=[node('legend','Update: I − t (1,2)ᵀ (1,0)',230,65,w=405,h=45,size=22),node('parameter','t = '+str(t),230,300,w=210,h=45,size=22)]
 frames.append(frame(nodes,'The rank-one change moves the three displayed outputs. At the exceptional scalar value the input direction (1,2) reaches zero and becomes the entire one-dimensional kernel of the updated square map.',{'t':str(t),'Rank':2 if t!=1 else 1},formula=r'1+v^Tu=1-t',snapshot=dict(kind='rank-map',matrix=[[str(v) for v in row] for row in a],inputs=inputs,outputs=[[str(v) for v in row] for row in outs])))
scene('rank-update','A rank-one update destroys exactly one direction','Actual output points move under a parameterized outer-product update.','The determinant is 1−t; at t=1 the kernel is the nonzero direction (1,2), so rank drops by one.',frames)

frames=[]
for t in [1,2,3,4]:
 b=[1,2,t];a=[[1,0],[0,1],[1,1]]
 nodes=[node('b0','b₁ = 1',150,85,w=190,h=55,size=24),node('b1','b₂ = 2',380,85,w=190,h=55,size=24),node('b2','b₃ = '+str(t),610,85,w=190,h=55,size=24),node('w','−b₁ − b₂ + b₃ = '+str(t-3),380,210,w=470,h=65,size=24,tone='done' if t==3 else 'warning')]
 frames.append(frame(nodes,'Changing only the third load crosses the exact compatibility condition. The independent left-kernel combination cancels all coefficient columns; a nonzero remaining load proves that no input can fit the three equations simultaneously.',{'Coefficient rank':2,'Augmented rank':2 if t==3 else 3,'Witness value':t-3},formula=r'y=(-1,-1,1)^T,\quad y^TA=0',snapshot=dict(kind='witness',A=a,b=b,y=[-1,-1,1],value=t-3)))
scene('rank-witness','A load must satisfy every independent output restriction','The exact load and cancellation value update, distinguishing a compatible fiber from an impossibility certificate.','The same left-null vector annihilates every coefficient column for all shown loads.',frames)

frames=[]
for k in [0,1,2,3,4]:
 a=S.zeros(4)
 for j in range(1,4):a[j-1,j]=1
 power=a**k
 nodes=[]
 for j in range(4):
  active=j>=k
  nodes.append(node('basis'+str(j),'e'+str(j+1)+' → '+('e'+str(j-k+1) if active else '0'),125+160*j,100+45*min(k,j+1),w=145,h=50,size=22,tone='active' if active else 'done'))
 frames.append(frame(nodes,'Successive powers shift surviving basis directions toward the killed endpoint. Each additional application removes one independent image direction until every basis input has zero output and the kernel is the whole domain.',{'Power':k,'Rank':max(0,4-k),'Nullity':min(4,k)},formula=r'Ae_1=0,\quad Ae_j=e_{j-1}',snapshot=dict(kind='power-rank',A=[list(map(int,a.row(i))) for i in range(4)],power=k,result=[list(map(int,power.row(i))) for i in range(4)])))
scene('rank-powers','Successive powers enlarge the kernel','Persistent input identities move through the nilpotent chain and eventually become zero outputs.','Each label gives original input followed by its actual output basis vector or zero; exact matrix powers are recorded at every checkpoint.',frames)
