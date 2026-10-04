"""Exact matrix checkpoints with persistent row identities and geometric motion."""
from common import node,frame,scene,check
from gauss_exact import solve,reduce,matrix,multiply,identity,mattex
from fractions import Fraction as F

def cells(a,ids=None,x=140,y=100,gap=115,rowgap=75,prefix='m',w=85):
 ids=ids or list(range(len(a)))
 return [node(prefix+str(ids[i])+'-'+str(j),str(v),x+j*gap,y+i*rowgap,w=w,h=50,size=23,tone='done' if str(v)=='0' else 'plain') for i,row in enumerate(a) for j,v in enumerate(row)]

def reduction(id,title,description,invariant,a,n=None):
 n=len(a[0])-1 if n is None else n
 r,p,e,steps=reduce(a,n);frames=[]
 for index,s in enumerate(steps):
  check(id+' exact transform '+str(index),multiply(matrix(s['transform']),matrix(a))==matrix(s['matrix']))
  nodes=cells(s['matrix'],s['ids'],gap=100 if len(a[0])>5 else 115,x=80 if len(a[0])>5 else 140)
  nodes+=[node('rhs','Last column: load',570,325,w=255,h=28,size=19)]
  cap=s['op']+'. Every displayed entry is an exact field value. The stored invertible transform maps the original complete augmented array to this checkpoint, preserving all original solutions.'
  frames.append(frame(nodes,cap,{'Operation':s['op'],'Coefficient pivots found':len(s['pivots']),'Unknowns':n},formula=r'M=TM_0',snapshot=dict(kind='rational-reduction',input=[[str(v) for v in row] for row in a],n=n,**s)))
 scene(id,title,description,invariant,frames,code=['Search the current coefficient column.','Swap a nonzero candidate into the active row.','Normalize its nonzero pivot.','Clear other rows with synchronized operations.','Classify zero coefficient rows and free coordinates.'])

reduction('gauss-swap','Move an equation into a legal pivot position','Persistent cell identities move with their full row during an actual row exchange. Later values change by exact reversible operations.','The original system has three unknowns. Coefficient column searches exclude the load column.',[[0,2,1,1],[1,-1,1,2],[2,1,-1,0]])
reduction('gauss-skip','A zero early column stays a free coordinate','The active row does not advance when no eligible coefficient pivot exists. Later columns still determine coordinates.','The first coefficient column is zero; the load column is not a variable.',[[0,1,2,3],[0,2,4,6],[0,0,1,1]])
reduction('gauss-affine','Two free coordinates survive all reversible operations','Trace a rectangular array to its independent equations and see exactly which restrictions disappear as redundancies.','Four real unknowns and two independent coefficient equations give an affine plane when compatible.',[[1,-1,1,3,2],[2,-1,1,2,4],[4,-3,3,8,8]])
reduction('gauss-inconsistent','A transformed row becomes an impossibility certificate','The last row loses every coefficient but keeps a nonzero load. Its stored row combination proves a contradiction in original coordinates.','The right side is transformed together with coefficients; a coefficient-zero nonzero-load row ends the solve.',[[1,1,1,1,4],[2,3,-2,-3,1],[1,0,5,6,1]])
reduction('gauss-inverse','The right block records the inverse transform','Reduce a two by two coefficient block and watch both identity-load columns undergo exactly the same operations.','Search only the first two columns. Reaching the identity on the left identifies the inverse on the right.',[[2,1,1,0],[1,1,0,1]],n=2)

frames=[]
for stage,second in [('Original equations',[(-.5,5),(2.5,-1)]),('Subtract four times row one',[(-.5,2),(2.5,2)])]:
 def point(id,p):return node(id,'',300+65*p[0],235-43*p[1],kind='point',w=0,h=0)
 nodes=[point('a',(-2,-1)),point('b',(3,4)),point('c',second[0]),point('d',second[1]),node('solution','(1, 2)',365,149,kind='point',labelDx=40,labelDy=-12),node('first','x − y = −1',170,320,w=245,h=28,size=21),node('second','4x + 2y = 8' if stage=='Original equations' else '6y = 12',540,320,w=235,h=28,size=21)]
 # Both endpoint pairs have the fixed solution as their midpoint, so the
 # interpolated straight line also retains the exact intersection throughout.
 frames.append(frame(nodes,'The second line changes from an oblique equation to the horizontal eliminated equation. Both pass through the same solution point, while the unchanged first line preserves the common intersection.',{'Phase':stage,'Common solution':'(1,2)'},formula=r'x-y=-1,\quad4x+2y=8\quad\Rightarrow\quad6y=12',edges=[{'from':'a','to':'b'},{'from':'c','to':'d','tone':'active'}],snapshot=dict(kind='geometry',first=[[1,-1,-1]],second=[4,2,8] if stage=='Original equations' else [0,6,12],solution=[1,2])))
scene('gauss-geometry','Elimination preserves an intersection, not each line','The second line physically rotates to its eliminated horizontal form. The common solution remains fixed.','Both equations and their exact eliminated combination are plotted using the same coordinate map.',frames)

frames=[]
for alpha in [1,0,-2,3]:
 a=[[1,0,1,-5],[0,alpha,1,1],[0,0,alpha+2,alpha*alpha-4]]
 state='unique solution' if alpha not in [0,-2] else 'inconsistent' if alpha==0 else 'one free coordinate'
 frames.append(frame(cells(a)+[node('branch','α = '+str(alpha),380,325,w=250,h=32,size=22)],'Substitute this parameter into the undivided triangular array. Inspect the vanished pivots and their remaining loads before permitting any division; the outcome differs across the exceptional values.',{'Parameter':alpha,'Classification':state},formula=r'(\alpha+2)z=\alpha^2-4',snapshot=dict(kind='parameter',alpha=alpha,input=a,classify=state)))
scene('gauss-parameters','Branch before dividing by a parameter','The coefficient and load entries change together as the parameter moves between ordinary and exceptional values.','The array is derived using parameter-independent row additions; its zero pivots must be inspected before cancellation.',frames)

frames=[];a=matrix([[2,1,1],[4,-6,0],[-2,7,2]]);u=matrix(a);l=identity(3)
for k in [-1,0,1]:
 if k>=0:
  for i in range(k+1,3):
   l[i][k]=u[i][k]/u[k][k]
   for j in range(k,3):u[i][j]-=l[i][k]*u[k][j]
 check('gauss LU stage '+str(k),multiply(l,u)==a)
 nodes=cells(u,x=100,gap=100,prefix='u',w=72)+cells(l,x=460,gap=100,prefix='l',w=72)
 nodes +=[node('uhead','Current U',200,40,w=200,h=28,size=22),node('lhead','Stored L',560,40,w=200,h=28,size=22)]
 frames.append(frame(nodes,'Subtract the newly stored multiplier times the pivot row from each lower row. The multiplier record reconstructs the original coefficient matrix at every displayed factorization checkpoint.',{'Stages completed':k+1,'Factor identity':'L U = A'},formula=r'A=LU',snapshot=dict(kind='lu',input=[[str(v) for v in row] for row in a],L=[[str(v) for v in row] for row in l],U=[[str(v) for v in row] for row in u])))
scene('gauss-lu','Multipliers reconstruct the original matrix','The left array becomes upper triangular while the right array fills with the actual elimination multipliers.','No exchanges are needed for this exact matrix; L has a fixed unit diagonal.',frames)

frames=[];a=matrix([[4,2,0],[2,1,1],[1,3,1]]);u=matrix(a);l=identity(3);p=identity(3);ids=[0,1,2]
def save_plu(phase):
 check('gauss PLU '+phase,multiply(l,u)==multiply(p,a))
 nodes=cells(u,ids,x=100,gap=100,prefix='u',w=72)+cells(l,ids,x=460,gap=100,prefix='l',w=72)
 nodes +=[node('uhead','Working U',200,40,w=200,h=28,size=22),node('lhead','Earlier L columns',560,40,w=255,h=28,size=21)]
 frames.append(frame(nodes,'The active arrays change while the exact product L U equals the permuted original matrix P A. During the later exchange, previously stored multiplier entries move with their equation rows.',{'Phase':phase,'Recorded row order':str(ids)},formula=r'PA=LU',snapshot=dict(kind='plu',phase=phase,input=[[str(v) for v in row] for row in a],L=[[str(v) for v in row] for row in l],U=[[str(v) for v in row] for row in u],P=[[str(v) for v in row] for row in p])))
save_plu('original')
for i in [1,2]:
 l[i][0]=u[i][0]/u[0][0]
 for j in range(3):u[i][j]-=l[i][0]*u[0][j]
save_plu('first column eliminated')
u[1],u[2]=u[2],u[1];p[1],p[2]=p[2],p[1];l[1][:1],l[2][:1]=l[2][:1],l[1][:1];ids[1],ids[2]=ids[2],ids[1]
save_plu('later row exchange and earlier multiplier exchange')
save_plu('finished: final multiplier is zero')
scene('gauss-plu','A later pivot exchange moves stored multipliers','Persistent row identities move in both arrays; the multiplier exchange is visible rather than merely stated.','Only already completed columns of L are exchanged. P records the corresponding equation permutation.',frames)

frames=[]
for phase,a in [('Original binary equations',[[1,1,0,1],[0,1,1,0],[1,0,1,1]]),('Remove dependent third equation',[[1,1,0,1],[0,1,1,0],[0,0,0,0]]),('Clear second pivot above',[[1,0,1,1],[0,1,1,0],[0,0,0,0]])]:
 frames.append(frame(cells(a), 'All displayed additions are modulo two, so adding the first two equations to the third removes it. The surviving free coordinate has two choices and produces exactly two solutions.',{'Phase':phase,'Field':'two elements','Solutions':'(1,0,0); (0,1,1)'},formula=r'x=1+z,\quad y=z\quad(\bmod\,2)',snapshot=dict(kind='binary',matrix=a,solutions=[[1,0,0],[0,1,1]])))
scene('gauss-binary','The coefficient field changes the pivot pattern','Exact binary additions make a real-independent equation redundant in the two-element field.','Every coefficient, load and operation is interpreted modulo two. The ordinary rational laboratory is a different model.',frames)

frames=[]
for phase,x in [('Transformed coordinates y',[5,2]),('Apply Q to recover x',[1,2])]:
 nodes=[node('vector','('+str(x[0])+', '+str(x[1])+')',170+70*x[0],250-60*x[1],kind='point',labelDy=-10,labelDx=20,size=23),node('formula','x = Qy',370,310,w=260,h=35,size=23)]
 frames.append(frame(nodes,'The displayed coordinate vector moves when the invertible column transformation is undone. The transformed system uses y, while original-system substitution must use the recovered vector x.',{'Phase':phase,'First coordinate':x[0],'Second coordinate':x[1]},formula=r'Q=\begin{bmatrix}1&-2\\0&1\end{bmatrix},\quad x=Qy',snapshot=dict(kind='coordinate',phase=phase,vector=x,Q=[[1,-2],[0,1]],original=[[1,2],[0,1]],load=[5,2])))
scene('gauss-coordinate','Column operations require a variable coordinate map','The exact vector moves from the transformed coordinates back to the original variables.','The new coefficient block A Q is the identity. The original solution is Q y, not y.',frames)

frames=[]
for phase,a,answer in [('Unpivoted input',[['1/10000',1,1],[1,1,2]],None),('Rounded unpivoted lower row',[['1/10000',1,1],[0,-10000,-10000]],[0,1]),('Exchange equations',[[1,1,2],['1/10000',1,1]],None),('Rounded pivoted lower row',[[1,1,2],[0,1,1]],[1,1])]:
 frames.append(frame(cells(a), 'Use the explicitly declared three-significant-digit decimal model. Rounding changes the lower equation; exchanging rows first changes the multiplier and produces a much more accurate answer for this example.',{'Phase':phase,'Rounded answer':str(answer) if answer else 'not yet computed','Exact answer':'(10000/9999, 9998/9999)'},formula=r'x_{\mathrm{exact}}=\frac{10000}{9999},\quad y_{\mathrm{exact}}=\frac{9998}{9999}',snapshot=dict(kind='rounding',phase=phase,matrix=a,answer=answer)))
scene('gauss-rounding','Tiny-pivot rounding versus a row exchange','Changing matrix entries shows the actual rounded lower system, with both coefficient and load affected.','Round after every scalar operation to three significant decimal digits; exact fractions remain the independent reference.',frames)
