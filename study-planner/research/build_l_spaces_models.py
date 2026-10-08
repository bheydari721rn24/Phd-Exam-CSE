from pathlib import Path
from html import escape as e
from itertools import product
import json,sys,ast
import sympy as S
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
models=[];groups={}
def tx(x,y,s,math=False,anchor='start'):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="vs-{"math"if math else"label"}">{e(str(s))}</text>'
def line(a,b,c='#8a9b9c',arrow=False):return f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{c}" stroke-width="3"'+(' marker-end="url(#vs-arrow)"'if arrow and a!=b else'')+'/>'
def rect(x,y,w,h,c='#e6efea'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{c}" stroke="#b0c4c5"/>'
def svg(s,h=560):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {h}" role="img" data-visual-type="plot"><defs><marker id="vs-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 1 L 9 5 L 0 9" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs>{s}</svg>'
def mat(A,x=65,y=115,w=92,h=70,hot=(),id='cell'):
 A=S.Matrix(A);out=''
 for i in range(A.rows):
  for j in range(A.cols):
   xx=x+j*w;yy=y+i*h;out+=f'<g data-entity="{id}-{i}-{j}">'+rect(xx,yy,w-10,h-10,'#f4dfb8'if(i,j)in hot else'#e6efea')+tx(xx+(w-10)/2,yy+(h-10)/2+8,A[i,j],True,'middle')+'</g>'
 return out
def texmat(A):return r'\begin{bmatrix}'+r'\\'.join('&'.join(str(v)for v in row)for row in S.Matrix(A).tolist())+r'\end{bmatrix}'
def model(id,title,kind,invariant,group,guide):
 m=dict(id=id,title=title,kind=kind,invariant=invariant,code=guide,frames=[]);models.append(m);groups.setdefault(group,[]).append(id);return m
def frame(m,state,drawing,operation,why,formula,checks):
 state=json.loads(json.dumps(state,default=str));prev=m['frames'][-1]['snapshot']if m['frames']else None
 changes=[dict(field=k,before=prev.get(k),after=v)for k,v in state.items()if prev and prev.get(k)!=v]
 m['frames'].append(dict(snapshot=state,svg=drawing,caption=why,formulaHtml=mathml.render(formula,True),teaching=dict(operation=operation,why=why,checks=[dict(mathHtml=mathml.render(a),result=str(b).lower())for a,b in checks],changes=changes,currentState=state,initial=prev is None,reading=m['invariant'],guide=m['code'],activeLine=min(len(m['frames']),len(m['code'])-1),mode=m['kind'])))
P=lambda v:(455+float(v[0])*60+float(v[2])*25,315-float(v[1])*36+float(v[2])*18)
def axes3():
 s=tx(35,32,'Fixed oblique projection of three-dimensional coordinates')
 for k,l in enumerate(['x','y','z']):
  a=[0,0,0];b=[0,0,0];a[k]=-3;b[k]=3;s+=line(P(a),P(b))+tx(P(b)[0]+14,P(b)[1]+8,l,True)
 return s
def plane(b1,b2,col='#cbded5',id='plane',offset=(0,0,0)):
 b1=S.Matrix(b1);b2=S.Matrix(b2);o=S.Matrix(offset);pts=[P(o+a*b1+b*b2)for a,b in[(-1,-1),(1,-1),(1,1),(-1,1)]]
 return f'<g data-entity="{id}"><polygon points="'+ ' '.join(f'{x},{y}'for x,y in pts)+f'" fill="{col}" fill-opacity=".55" stroke="#518a78" stroke-width="2"/></g>'
def point3(v,label,id='point',col='#9b673d'):
 x,y=P(v);return f'<g data-entity="{id}"><circle cx="{x}" cy="{y}" r="7" fill="{col}"/>'+tx(x+13,y-14,label,True)+'</g>'
def vec2(v,label,id,col='#3c728d',origin=(0,0)):
 Q=lambda t:(400+float(t[0])*45,355-float(t[1])*36);a=Q(origin);b=Q(S.Matrix(origin)+S.Matrix(v));return f'<g data-entity="{id}">'+line(a,b,col,True)+tx(b[0]+14,b[1]-14,label,True)+'</g>'
def axes2():return line((100,355),(850,355))+line((400,80),(400,465))+tx(870,365,'x',True)+tx(414,80,'y',True)

m=model('closure-plane','Homogeneous closure uses the actual plane','plane-geometry','The plane is x + 2y − z = 0. A fixed oblique camera is used; a visual overlap is not a proof of equality.','closure',['Check zero.','Add two plane vectors.','Multiply by a scalar.','Substitute into the defining equation.'])
for v,label in[([0,0,0],'zero'),([1,0,1],'u'),([-2,1,0],'v'),([-1,1,1],'u + v'),([2,0,2],'2u')]:
 s=axes3()+plane([1,0,1],[-2,1,0])+point3(v,label)+tx(65,485,f'Point {tuple(v)}: x + 2y − z = {v[0]+2*v[1]-v[2]}',True)
 frame(m,dict(vector=v,residual=v[0]+2*v[1]-v[2]),svg(s),'Verify '+label,'Each listed vector satisfies the homogeneous constraint; the proof in the lesson handles arbitrary scalars.',r'x+2y-z=0',[(r'x+2y-z=0',v[0]+2*v[1]-v[2]==0)])
m=model('affine-failure','A translated plane fails the zero and addition tests','plane-geometry','The affine set x + 2y − z = 3 is not a vector subspace under ordinary operations.','closure',['Inspect one allowed point.','Add it to itself.','Test the zero vector.'])
for v,label in[([1,1,0],'u in the set'),([2,2,0],'u + u outside'),([0,0,0],'zero outside')]:
 res=v[0]+2*v[1]-v[2];s=axes3()+plane([1,0,1],[-2,1,0],offset=[1,1,0])+point3(v,label)+tx(65,485,f'Actual constraint value = {res}; required value = 3',True)
 frame(m,dict(vector=v,value=res),svg(s),'Test membership','The translated patch has the same direction as the homogeneous plane but a different offset.',r'x+2y-z='+str(res),[(r'\text{point belongs to the affine set}',res==3)])
m=model('union-failure','Two axes: a union is different from a sum','vector-geometry','The union contains only points on either axis; the sum contains every pair of coordinates.','intersection',['Choose a point on each axis.','Add the two points.','Check both original sets.'])
for v,lab in[([2,0],'u'),([0,2],'v'),([2,2],'u + v')]:
 s=axes2()+vec2([3,0],'U','U')+vec2([0,3],'W','W','#9b673d')+vec2(v,lab,'target','#8e4d58')+tx(65,495,f'Target {tuple(v)} lies in the union: {v[0]==0 or v[1]==0}')
 frame(m,dict(vector=v,inUnion=v[0]==0 or v[1]==0),svg(s),'Add vectors from different members','Both coordinates nonzero exclude the sum from both axes, although it belongs to U + W.',r'U\cup W\ne U+W',[(r'\text{target belongs to the union}',v[0]==0 or v[1]==0)])
m=model('redundant-parameters','Three named parameters, only two image directions','matrix-column-selection','The map (a,b,c) ↦ (a+b,2a+2b,c) has repeated first two columns.','span',['Write the parameter map as columns.','Recognize the duplicate direction.','Keep columns 1 and 3.'])
A=S.Matrix([[1,1,0],[2,2,0],[0,0,1]])
for hot in[[(i,0)for i in range(3)],[(i,1)for i in range(3)],[(i,j)for i in range(3)for j in[0,2]]]:
 s=tx(35,32,m['title'])+mat(A,85,120,100,75,hot)+tx(520,160,'Column 2 equals column 1.')+tx(520,225,'Column 3 adds a new direction.')+tx(65,450,'Image basis: (1,2,0), (0,0,1); dimension = 2',True)
 frame(m,dict(matrix=A.tolist(),selected=hot,rank=2),svg(s),'Inspect the highlighted generators','Counting parameter names would overestimate dimension. Count independent output directions instead.',r'\operatorname{rank}A=2',[(r'A_1=A_2',A[:,0]==A[:,1]),(r'\operatorname{rank}A=2',A.rank()==2)])
m=model('basis-filter','Keep independent directions, then solve the actual target','vector-geometry','Generators e1, e2, (2,3) span a plane. The third generator is redundant. Target is (5,7).','span',['Keep e1.','Add independent e2.','Reject 2e1 + 3e2.','Express (5,7) in the retained basis.'])
for k in range(4):
 s=axes2()+vec2([1,0],'e1','e1')
 if k>=1:s+=vec2([0,1],'e2','e2','#9b673d')
 if k>=2:s+=vec2([2,3],'2e1 + 3e2','redundant','#9691a0')
 if k>=3:s+=vec2([5,7],'(5,7)','target','#8e4d58')
 s+=tx(65,505,'Rank = '+str(1 if k==0 else 2)+'; target coefficients in the basis are (5,7).',True)
 frame(m,dict(step=k,rank=1 if k==0 else 2),svg(s),'Scan the next generator or target','A new name is not a new independent direction. Once the two axes are retained, the target has unique basis coordinates.',r'(5,7)=5e_1+7e_2',[(r'(2,3)=2e_1+3e_2',True)])
m=model('parameter-span','Exceptional values change the number of directions','vector-geometry','Columns are (1,t) and (t,1). The coordinate scale is fixed across t = −1, 0, 1.','parameter',['Set t to minus one.','Compare with t equal zero.','Set t to one.','Check determinant before dividing.'])
for t in[-1,0,1]:
 A=S.Matrix([[1,t],[t,1]]);s=axes2()+vec2([1,t],'u','u')+vec2([t,1],'v','v','#9b673d')+tx(65,490,f't = {t}; determinant = {1-t*t}; rank = {A.rank()}',True)
 frame(m,dict(t=t,matrix=A.tolist(),rank=A.rank()),svg(s),'Change the actual parameter','The exceptional cases are not approximations: the columns become equal or opposite exactly at the endpoints.',r'\det A=1-t^2',[(r'\operatorname{rank}A=2',A.rank()==2)])
A0=S.Matrix([[1,2,0,3],[2,4,1,4],[3,6,2,5]]);A=A0.copy();E=S.eye(3)
m=model('pivot-main','Row reduction selects original columns and solves the kernel','matrix-row-reduction','Every row operation preserves column relations. The basis vectors come from the original matrix, not the reduced columns.','computation',['Keep the original matrix.','Clear entries below the first pivot.','Clear the second pivot column.','Read pivot indices 1 and 3.','Solve two free variables for the null space.'])
ops=[('Read original input',None),('R2 becomes R2 minus 2R1',(1,0,-2)),('R3 becomes R3 minus 3R1',(2,0,-3)),('R3 becomes R3 minus 2R2',(2,1,-2))]
for k,(label,op)in enumerate(ops):
 if op:
  i,j,c=op;A[i,:]+=c*A[j,:];E[i,:]+=c*E[j,:]
 s=tx(35,32,label)+tx(65,90,'Working matrix')+mat(A,65,115,95,70,[(op[0],j)for j in range(4)]if op else[])+tx(540,90,'Original pivot columns')+mat(A0[:,[0,2]],540,115,100,70,id='original')+tx(65,430,'Final kernel basis: (−2,1,0,0), (−3,0,2,1)',True)+tx(65,485,'Column basis: (1,2,3), (0,1,2)',True)
 frame(m,dict(matrix=A.tolist(),rowOperator=E.tolist(),original=A0.tolist(),rank=2),svg(s),label,'The independently tracked row operator E verifies the exact equality E A_original = A_current.',texmat(A),[(r'EA_0=A',E*A0==A),(r'\operatorname{rank}A=2',A.rank()==2)])
m=model('exchange-main','Exchange one old basis vector with a genuine new direction','vector-geometry','The drawing restricts Question 24 to the e1,e2 plane; the unchanged third direction e3 is perpendicular to the drawing. Replacing e3 by w would lose that direction.','exchange',['Start with the two in-plane basis directions; retain e3.','Insert w = 2e1 − e2.','Remove e1 and retain w, e2; keep e3 unchanged.'])
for k in range(3):
 s=axes2()+vec2([0,1],'e2','e2','#9b673d')
 if k<2:s+=vec2([1,0],'e1','e1')
 if k>0:s+=vec2([2,-1],'w','w','#8e4d58')
 s+=tx(65,505,'After exchange: e1 = (w + e2)/2; the span is unchanged.',True)
 frame(m,dict(step=k,retained=['w','e2']if k==2 else['e1','e2']),svg(s),'Exchange a nonzero-coefficient member','The replacement coefficient must be nonzero. The displayed reconstruction proves the missing axis is still spanned.',r'e_1=\frac12(w+e_2)',[(r'\det[w\ e_2]=2',S.Matrix([[2,0],[-1,1]]).det()==2)])
m=model('coordinates-main','One vector, two ordered coordinate systems','vector-geometry','B = ((1,1),(1,−1)); C = ((2,0),(1,1)); the physical vector (3,1) never changes.','coordinates',['Read v = (3,1).','Express v = 2b1 + b2.','Express v = c1 + c2.'])
for k in range(3):
 s=axes2()+vec2([3,1],'v','target','#8e4d58')
 if k==1:s+=vec2([2,2],'2b1','component1')+vec2([1,-1],'b2','component2','#9b673d',origin=[2,2])
 if k==2:s+=vec2([2,0],'c1','component1')+vec2([1,1],'c2','component2','#9b673d',origin=[2,0])
 s+=tx(65,490,['Fixed physical vector v = (3,1)','B-coordinates = (2,1)','C-coordinates = (1,1)'][k],True)
 frame(m,dict(step=k,vector=[3,1],Bcoordinates=[2,1],Ccoordinates=[1,1]),svg(s),'Change the coordinate description','The component arrows remain joined head-to-tail. Coordinates depend on the ordered basis, while the represented vector is fixed.',r'[v]_B=(2,1),\quad[v]_C=(1,1)',[(r'2(1,1)+(1,-1)=(3,1)',True),(r'(2,0)+(1,1)=(3,1)',True)])
m=model('polynomial-main','Triangular polynomial coordinates build the actual polynomial','polynomial-plot','The target is 2 + 3x + 4x². Contributions are −1, −(1+x), and 4(1+x+x²). Axes and plot scale stay fixed.','polynomial',['Use the ordered polynomial basis.','Add the first contribution.','Add the second contribution.','Add the final contribution and compare coefficients.'])
x=S.symbols('x');polys=[-S.Integer(1),-2-x,2+3*x+4*x*x]
for k,p in enumerate(polys):
 pts=[(480+float(t)*160,380-float(p.subs(x,t))*15)for t in[S.Rational(i,20)for i in range(-20,21)]]
 s=tx(35,32,m['title'])+line((280,380),(700,380))+line((480,80),(480,445))+tx(720,390,'x',True)+tx(490,80,'p(x)',True)+f'<g data-entity="polynomial"><polyline points="'+ ' '.join(f'{a},{b}'for a,b in pts)+'" fill="none" stroke="#518a78" stroke-width="3"/></g>'+tx(65,490,'Partial polynomial: '+str(p),True)
 frame(m,dict(step=k,coefficients=[str(S.expand(p).coeff(x,j))for j in range(3)]),svg(s),'Add one actual basis contribution','This graph shows partial sums, not an interpolation from arbitrary samples. The coefficient identity supplies the proof.',r'-1-(1+x)+4(1+x+x^2)=2+3x+4x^2',[(r'\text{target reached}',S.expand(p)==2+3*x+4*x*x)])
m=model('symmetric-trace','Symmetry ties pairs; trace removes one diagonal freedom','matrix-symmetry-constraint','Order four is used, matching the authentic MSc question. Six off-diagonal coordinates and three diagonal differences remain independent.','matrix',['Identify four diagonal slots.','Tie each off-diagonal pair.','Impose one trace equation.','Build diagonal-difference basis elements.'])
for k in range(4):
 A=S.zeros(4)
 if k==0:A=S.eye(4)
 elif k==1:A[0,1]=A[1,0]=1
 elif k==2:A=S.diag(1,2,3,-6)
 else:A=S.diag(0,1,0,-1)
 s=tx(35,32,m['title'])+mat(A,65,105,95,70,[(i,j)for i in range(4)for j in range(4)if A[i,j]!=0])+tx(530,150,'Symmetric coordinates: 4 + 6 = 10',True)+tx(530,215,'Independent trace constraint: 1',True)+tx(530,280,'Kernel dimension: 10 − 1 = 9',True)+tx(65,475,f'Displayed symmetric matrix trace = {S.trace(A)}',True)
 why=['The identity matrix shows trace is a nonzero functional; it is outside the trace-zero kernel.','One off-diagonal symmetric pair contributes one independent direction and has zero trace.','The last diagonal entry is forced by the first three; it is not an extra free coordinate.','This is a diagonal-difference basis element, independent from the six off-diagonal directions.'][k]
 frame(m,dict(step=k,matrix=A.tolist(),trace=str(S.trace(A)),dimension=9),svg(s),'Inspect a symmetry or trace direction',why,r'\dim W=\frac{4(4+1)}2-1=9',[(r'A^T=A',A.T==A),(r'\operatorname{tr}A=0',S.trace(A)==0)])
m=model('symmetric-split','Symmetric and skew parts reconstruct the supplied matrix','matrix-decomposition','This decomposition assumes the field has characteristic different from two. The displayed real matrix satisfies that condition.','matrix',['Read A.','Compute (A + transpose A)/2.','Compute (A − transpose A)/2.'])
A=S.Matrix([[1,4],[-2,3]]);parts=[A,(A+A.T)/2,(A-A.T)/2]
for k,N in enumerate(parts):
 s=tx(35,32,m['title'])+mat(N,100,120,110,80)+tx(470,170,['Original matrix','Symmetric component S','Skew component K'][k])+tx(65,420,'S + K = A, and the intersection is {0}.',True)
 frame(m,dict(step=k,matrix=N.tolist()),svg(s),'Compute the labelled component','Division by two is essential. Over characteristic two this proof and its conclusion must be reconsidered.',texmat(N),[(r'S+K=A',parts[1]+parts[2]==A),(r'S^T=S',parts[1].T==parts[1]),(r'K^T=-K',parts[2].T==-parts[2])])
m=model('intersection-main','Two coordinate planes share a line, so decompositions vary','plane-geometry','U is the xy-plane and W is the xz-plane. Explicit specialization of Question 48: a = b = c = 1. Their shared x-axis is the source of nonuniqueness.','intersection',['Read the two planes.','Choose a decomposition of (1,1,1).','Move an intersection vector from one component to the other.'])
for t in[-1,0,1]:
 u=S.Matrix([t,1,0]);w=S.Matrix([1-t,0,1]);s=axes3()+plane([2,0,0],[0,2,0],id='U')+plane([2,0,0],[0,0,2],col='#cbdde9',id='W')+point3(u,'u','u')+point3(w,'w','w','#3c728d')+point3([1,1,1],'target','target','#8e4d58')+tx(65,485,f'u = {tuple(u)}, w = {tuple(w)}; u + w = (1,1,1)',True)
 frame(m,dict(t=t,u=list(u),w=list(w),target=[1,1,1]),svg(s),'Shift the shared-axis component','The total vector is fixed while the two valid components change. Therefore this sum is not direct.',r'\dim(U+W)=2+2-1=3',[(r'u+w=(1,1,1)',u+w==S.Matrix([1,1,1]))])
m=model('three-lines','Pairwise trivial intersections do not imply a three-way direct sum','vector-geometry','The three real lines are span(e1), span(e2), and span(e1+e2). Every pair meets only at zero.','direct',['Choose e1 from the first line.','Add e2 from the second line.','Subtract e1 + e2 from the third line.'])
for k in range(3):
 s=axes2()+vec2([1,0],'e1','u')
 if k>=1:s+=vec2([0,1],'e2','v','#9b673d',origin=[1,0])
 if k>=2:s+=vec2([-1,-1],'−(e1+e2)','w','#8e4d58',origin=[1,1])
 s+=tx(65,495,'Nonzero components can sum to zero: e1 + e2 − (e1+e2) = 0.',True)
 frame(m,dict(step=k,components=[[1,0],[0,1],[-1,-1]][:k+1]),svg(s),'Follow the actual head-to-tail components','At the third step the path returns to zero. This is a nontrivial dependence across three subspaces.',r'e_1+e_2-(e_1+e_2)=0',[(r'\text{three components sum to zero}',k==2)])
m=model('direct-oblique','A complement gives unique components without orthogonality','vector-geometry','U = span((1,0)), W = span((1,2)); target (5,6) = (2,0) + (3,6).','direct',['Keep the target fixed.','Take its W component (3,6).','Add its U component (2,0).'])
for k in range(3):
 s=axes2()+vec2([5,6],'target','target','#8e4d58')
 if k>=1:s+=vec2([3,6],'w','w','#3c728d')
 if k>=2:s+=vec2([2,0],'u','u','#9b673d',origin=[3,6])
 s+=tx(65,505,'W coefficient = 3; U coefficient = 2. The two lines are not perpendicular.',True)
 frame(m,dict(step=k,target=[5,6],u=[2,0],w=[3,6]),svg(s),'Construct the oblique decomposition','Independence gives uniqueness. Orthogonality is a stronger additional property, not part of a direct-sum definition.',r'(5,6)=2(1,0)+3(1,2)',[(r'\det[(1,0)\ (1,2)]=2',True)])
m=model('quotient-main','A coset is an entire parallel line of representatives','quotient-geometry','U = span((1,1,0)). The actual coset in Question 59 has quotient coordinates (1,4); representative coordinates are not quotient coordinates.','quotient',['Choose representative (2,3,4).','Add one vector from U.','Subtract a vector from U.'])
for t in[0,1,-1]:
 v=[2+t,3+t,4];s=axes3()+line(P([-1,0,4]),P([4,5,4]),'#518a78')+point3(v,'representative')+tx(65,485,f'Representative = {tuple(v)}; invariant quotient coordinates = (1,4)',True)
 frame(m,dict(t=t,representative=v,quotientCoordinates=[1,4]),svg(s),'Change representative within one coset','Adding (t,t,0) leaves y minus x and z unchanged. A coset is a quotient vector, not a chosen single point.',r'(y-x,z)=(1,4)',[(r'y-x=1',v[1]-v[0]==1),(r'z=4',v[2]==4)])
m=model('finite-basis','Count an ordered basis in the finite field, not by real geometry','finite-field-table','All arithmetic is in F2. Seven nonzero vectors are listed; after one independent choice there are six, then four choices.','field',['Choose any nonzero first vector.','Exclude its two-element span for the second choice.','Exclude the four-element plane for the third choice.'])
vectors=list(product([0,1],repeat=3));selected=[(1,0,0),(0,1,0),(0,0,1)]
for k in range(3):
 span={tuple(sum(c*v[j]for c,v in zip(cs,selected[:k]))%2 for j in range(3))for cs in product([0,1],repeat=k)}
 s=tx(35,32,m['title'])
 for i,v in enumerate(vectors):
  xx=65+(i%4)*225;yy=120+(i//4)*100;s+=f'<g data-entity="vector-{i}">'+rect(xx,yy,200,75,'#d4d7d9'if v in span else'#e6efea')+tx(xx+100,yy+45,str(v),True,'middle')+'</g>'
 s+=tx(65,400,f'Already chosen: {k}; excluded span size = {len(span)}; next choices = {8-len(span)}',True)+tx(65,465,'Ordered bases = 7 × 6 × 4 = 168; unordered bases = 168/6 = 28.',True)
 frame(m,dict(chosen=k,excluded=[list(v)for v in sorted(span)],choices=8-len(span)),svg(s),'Exclude the span of preceding choices','The grey cells are exactly the vectors that would make the next choice dependent. This is a finite-field table, not a real point plot.',r'(2^3-1)(2^3-2)(2^3-2^2)=168',[(r'\text{excluded span size}=2^k',len(span)==2**k)])
m=model('finite-lines','Three one-dimensional subspaces cover F2 squared','finite-field-table','Over F2 each line has just zero and one nonzero vector. A finite union can cover a finite vector space.','field',['List the first line.','List the second line.','Include the diagonal line.'])
vs=[(0,0),(1,0),(0,1),(1,1)]
for k in range(3):
 s=tx(35,32,m['title'])
 for i,v in enumerate(vs):
  xx=65+i*225;s+=rect(xx,160,200,85,'#f4dfb8'if v==vs[k+1]or v==(0,0)else'#e6efea')+tx(xx+100,210,str(v),True,'middle')
 s+=tx(65,365,'Highlighted line = { (0,0), '+str(vs[k+1])+' }',True)+tx(65,435,'The three proper lines together contain all four vectors.',True)
 frame(m,dict(line=[vs[0],vs[k+1]],field=2),svg(s),'Select one finite-field line','Do not import the theorem about a finite union of proper subspaces over an infinite field into F2.',r'\mathbb F_2^2=L_1\cup L_2\cup L_3',[(r'\text{each line has two vectors}',True)])
m=model('plane-course','A reconstructed course plane: two generators and one constraint','plane-geometry','The course problem is reconstructed with coefficients 2x − y + 4z = 0. These are the actual coefficients of Question 72.','polynomial',['Choose (1,2,0).','Choose (0,4,1).','Add the two generators.'])
for v in[[1,2,0],[0,4,1],[1,6,1]]:
 # Scale the visible patch to keep all labels inside a fixed view. Coordinates still use the same camera.
 s=axes3()+plane([S.Rational(1,2),1,0],[0,2,S.Rational(1,2)])+point3(v,'actual vector')+tx(65,500,f'Vector {tuple(v)}: 2x − y + 4z = 0',True)
 frame(m,dict(vector=v),svg(s,600),'Substitute one generator or its sum','The two generators are independent because their x and z coordinates force both coefficients to zero.',r'2x-y+4z=0',[(r'2x-y+4z=0',2*v[0]-v[1]+4*v[2]==0)])
m=model('measurement-main','Measurements leave a one-dimensional ambiguity','plane-geometry','Measurements are x1 + x2 = 4 and x2 + x3 = 7. The homogeneous ambiguity direction is (−1,1,−1).','coordinates',['Solve using x2 as a free parameter.','Change the free parameter.','Verify both measurements remain fixed.'])
for t in[2,3,4]:
 v=[4-t,t,7-t];s=axes3()+line(P([3,1,6]),P([-1,5,2]),'#518a78')+point3(v,'solution')+tx(65,505,f'x = {tuple(v)}; measurements = (4,7)',True)
 frame(m,dict(t=t,vector=v,measurements=[v[0]+v[1],v[1]+v[2]]),svg(s,600),'Move along the null-space direction','The solution set is an affine line. Its direction is a vector space, while this nonzero right-hand-side solution set is not.',r'x=(4-t,t,7-t)',[(r'x_1+x_2=4',v[0]+v[1]==4),(r'x_2+x_3=7',v[1]+v[2]==7)])
m=model('projection-main','Orthogonal basis projection shortens or preserves length','vector-geometry','Explicit two-dimensional specialization: U is the horizontal axis and x = (2,3). The general m-dimensional proof remains in the solution.','direct',['Read x = (2,3).','Take its horizontal projection (2,0).','Separate the orthogonal residual (0,3).'])
for k in range(3):
 s=axes2()+vec2([2,3],'x','x','#8e4d58')
 if k>=1:s+=vec2([2,0],'Px','projection','#3c728d')
 if k>=2:s+=vec2([0,3],'residual','residual','#9b673d',origin=[2,0])+line((490,343),(502,343))+line((502,343),(502,355))
 s+=tx(65,495,'Squared lengths: 13 = 4 + 9; projected length 2 is below √13.',True)
 frame(m,dict(step=k,vector=[2,3],projection=[2,0],residual=[0,3]),svg(s),'Construct the orthogonal decomposition','The residual is perpendicular to U. The authentic question reverses the universally valid norm inequality.',r'\|x\|_2^2=\|Px\|_2^2+\|x-Px\|_2^2=13',[(r'13=4+9',True)])
m=model('intersection-parameter','A moving plane changes the intersection dimension at zero','plane-geometry','The fixed plane is z = 0; the moving plane is z = t(x+y). Each plane always has dimension two.','parameter',['Use generators (1,0,t), (0,1,t).','At t = 0 the planes coincide.','At nonzero t only the line (a,−a,0) is shared.'])
for t in[-1,0,1]:
 BU=S.Matrix([[1,0],[0,1],[0,0]]);BW=S.Matrix([[1,0],[0,1],[t,t]]);d=4-BU.row_join(BW).rank()
 s=axes3()+plane([1,0,0],[0,1,0],id='fixed')+plane([1,0,t],[0,1,t],col='#cbdde9',id='moving')+line(P([-2,2,0]),P([2,-2,0]),'#8e4d58')+tx(65,480,f't = {t}; intersection dimension = {d}; sum dimension = {4-d}',True)+tx(65,530,'Red line is the entire intersection only when t is nonzero.')
 frame(m,dict(t=t,fixed=BU.tolist(),moving=BW.tolist(),intersectionDimension=d,sumDimension=4-d),svg(s,590),'Set the parameter and solve both constraints','At zero the whole plane is shared. Dividing by t before separating that case would discard the dimension jump.',r'\dim(U\cap W_t)='+str(d),[(r'\dim U=\dim W_t=2',BU.rank()==BW.rank()==2)])
m=model('matrix-balances','Four free entries force the remaining row and column balances','matrix-constraint-coupling','These are the actual four basis directions for Question 43, followed by their combination with coefficients 1,2,3,4.','matrix',['Choose one top-left free entry.','Balance its row and column by two negative entries.','Correct the last corner once.','Combine the four independent directions.'])
basis=[]
for i in range(2):
 for j in range(2):
  A=S.zeros(3);A[i,j]=A[2,2]=1;A[i,2]=A[2,j]=-1;basis.append(A)
for k,A in enumerate(basis+[sum(((j+1)*A for j,A in enumerate(basis)),S.zeros(3))]):
 s=tx(35,32,m['title'])+mat(A,70,110,100,80,[(i,j)for i in range(3)for j in range(3)if A[i,j]!=0])+tx(510,150,'Every row sum = 0',True)+tx(510,220,'Every column sum = 0',True)+tx(510,290,'Four independent free coordinates',True)+tx(65,440,'Basis direction '+str(k+1)if k<4 else'Combination: B1 + 2B2 + 3B3 + 4B4',True)
 frame(m,dict(step=k,matrix=A.tolist(),rowSums=list(A*S.ones(3,1)),columnSums=list(S.ones(1,3)*A)),svg(s),'Balance the indicated coordinate','The top-left four entries isolate the coefficients. The shared corner satisfies both last equations; counting all six equations as independent would be wrong.',texmat(A),[(r'A\mathbf1=0',A*S.ones(3,1)==S.zeros(3,1)),(r'\mathbf1^TA=0',S.ones(1,3)*A==S.zeros(1,3))])
data=dict(topicId='l_spaces',models=models,groups=groups)
(R/'dist/chapters/l_spaces-models.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
(B/'l_spaces-evidence/models.json').write_text(json.dumps(dict(status='built_pending_browser_review',models=len(models),frames=sum(len(m['frames'])for m in models),ids=[m['id']for m in models]),indent=2)+'\n')
print(len(models),'models;',sum(len(m['frames'])for m in models),'exact checkpoints')
