from pathlib import Path
from html import escape as e
import json,sys,math,ast
import sympy as S
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
models=[];groups={}
def tx(x,y,s,math=False,anchor='start'):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="det-{("math"if math else"label")}">{e(str(s))}</text>'
def ln(x,y,u,v,c='#77939a'):return f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="{c}" stroke-width="2"/>'
def rect(x,y,w,h,c='#e6efea'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{c}" stroke="#b0c4c5"/>'
def svg(s,h=480):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {h}" role="img" data-visual-type="plot">{s}</svg>'
def mat(A,x=65,y=110,w=82,h=64,hot=(),id='cell'):
 A=S.Matrix(A);out=''
 for i in range(A.rows):
  for j in range(A.cols):
   xx=x+j*w;yy=y+i*h;out+=f'<g data-entity="{id}-{i}-{j}">'+rect(xx,yy,w-10,h-10,'#f4dfb8'if(i,j)in hot else'#e6efea')+tx(xx+(w-10)/2,yy+(h-10)/2+8,A[i,j],True,'middle')+'</g>'
 return out
def texmat(A):return r'\begin{bmatrix}'+r'\\'.join('&'.join(str(v)for v in row)for row in S.Matrix(A).tolist())+r'\end{bmatrix}'
def model(id,title,kind,invariant,group):
 m=dict(id=id,title=title,kind=kind,invariant=invariant,code=['Read the actual supplied state.','Check the displayed condition before acting.','Apply the specified mathematical operation.','Retain its exact value and stated interpretation.'],frames=[]);models.append(m);groups.setdefault(group,[]).append(id);return m
def frame(m,state,drawing,operation,why,formula,checks=None):
 state=json.loads(json.dumps(state,default=str));prev=m['frames'][-1]['snapshot']if m['frames']else None
 changes=[dict(field=k,before=prev.get(k),after=v)for k,v in state.items()if prev and prev.get(k)!=v]
 m['frames'].append(dict(snapshot=state,svg=drawing,caption=why,formulaHtml=mathml.render(formula,True),teaching=dict(operation=operation,why=why,checks=[dict(mathHtml=mathml.render(a),result=str(b).lower())for a,b in(checks or[])],changes=changes,currentState=state,initial=prev is None,reading=m['invariant'],guide=m['code'],activeLine=0 if prev is None else 2,mode=m['kind'])))
def area(id,title,values,group):
 m=model(id,title,'oriented-parallelogram','Axes and scale stay fixed. Edge identities persist; signed determinant and physical area are different quantities.',group);ox,oy,sc=410,365,58
 for A in values:
  A=S.Matrix(A);u=A[:,0];v=A[:,1];d=A.det();P=lambda x,y:(ox+float(x)*sc,oy-float(y)*sc);o=P(0,0);a=P(*u);b=P(*v);c=P(*(u+v));s=tx(35,32,title)+ln(95,oy,840,oy)+ln(ox,90,ox,430)
  s+=f'<g data-entity="parallelogram"><polygon points="{o[0]},{o[1]} {a[0]},{a[1]} {c[0]},{c[1]} {b[0]},{b[1]}" fill="#dcebe3" stroke="#518a78" stroke-width="2"/></g>'
  for key,pt,col in [('u',a,'#9b673d'),('v',b,'#3c728d')]:
   s+=f'<g data-entity="edge-{key}">'+ln(*o,*pt,col)+f'<circle cx="{pt[0]}" cy="{pt[1]}" r="6" fill="{col}"/>'+tx(pt[0]+12,pt[1]-12,key,True)+'</g>'
  s+=tx(60,480,f'Columns u = {tuple(u)}, v = {tuple(v)}',True)+tx(60,530,f'Signed area = {d}; physical area = {abs(d)}',True)
  frame(m,dict(matrix=A.tolist(),determinant=str(d),physicalArea=str(abs(d))),svg(s,580),'Change the actual column pair','Follow the ordered edge vectors. The same coordinate scale is used in every checkpoint.',r'\det A='+str(d),[(r'\det A\ne0',d!=0)])
 return m
area('geometry-main','Oriented area: reversal and collapse',[[[2,-1],[1,3]],[[-1,2],[3,1]],[[2,4],[1,2]]],'geometry')
area('shear-main','A shear changes slant while preserving area',[[[1,t],[0,1]]for t in[0,1,2,3]],'geometry')
A=S.Matrix([[1,-3,2],[0,7,1],[-5,1,3]])
from itertools import permutations
m=model('permutation-main','Every selected term uses each row and column exactly once','permutation-term-grid','Fixed matrix entries are highlighted according to a real permutation. Accumulated contributions include both parity and numeric entry signs.','permutations');acc=0
for p in permutations(range(3)):
 inv=sum(p[i]>p[j]for i in range(3)for j in range(i+1,3));prod=S.prod(A[i,p[i]]for i in range(3));term=(-1)**inv*prod;acc+=term
 s=tx(35,32,m['title'])+mat(A,90,120,110,80,[(i,p[i])for i in range(3)])
 for i,j in enumerate(p):s+=tx(565,155+i*70,f'Row {i+1} selects column {j+1}')
 s+=tx(65,425,f'Inversions = {inv}; product = {prod}; signed contribution = {term}',True)+tx(65,475,f'Accumulated determinant terms = {acc}',True)
 frame(m,dict(matrix=A.tolist(),permutation=list(p),inversions=inv,product=str(prod),term=str(term),accumulator=str(acc)),svg(s,530),'Select one bijective pattern','The highlighted entries form one legitimate term. A zero factor kills a term without changing its parity.',r'(-1)^{'+str(inv)+r'}('+str(prod)+r')='+str(term),[(r'\text{distinct selected columns}',len(set(p))==3)])
for id,A,row,group in [('cofactor-main',[[1,-3,2],[0,7,1],[-5,1,3]],0,'cofactors'),('cofactor-sparse',[[2,4,2],[3,2,1],[2,0,1]],2,'cofactors')]:
 A=S.Matrix(A);m=model(id,'Cofactor deletion: keep the sign and the surviving submatrix','cofactor-deletion','The selected row is fixed. Gold identifies the deleted row/column; the smaller matrix contains only surviving entries.','cofactors');total=0
 for j in range(A.cols):
  N=A.minor_submatrix(row,j);co=(-1)**(row+j)*N.det();term=A[row,j]*co;total+=term
  s=tx(35,32,m['title'])+mat(A,70,105,105,80,[(i,k)for i in range(3)for k in range(3)if i==row or k==j])+mat(N,550,130,105,80,id='minor')+tx(555,100,'Surviving minor matrix')+tx(65,420,f'Entry ({row+1},{j+1}) = {A[row,j]}; cofactor = {co}; term = {term}',True)+tx(65,475,f'Partial expansion = {total}',True)
  frame(m,dict(matrix=A.tolist(),row=row,column=j,minor=N.tolist(),cofactor=str(co),term=str(term),accumulator=str(total)),svg(s,530),'Delete the indicated row and column','Compute the smaller determinant, then apply its checkerboard sign before multiplying by the selected entry.',str(A[row,j])+r'\cdot('+str(co)+')='+str(term),[(r'(-1)^{i+j}',(-1)**(row+j))])
orig=S.Matrix([[0,1,0,1],[1,1,2,3],[1,0,3,1],[0,2,3,1]]);A=orig.copy();m=model('eliminate-main','Row elimination with a determinant correction ledger','row-operation-matrix-ledger','The matrix is the original Berkeley worked example. Row replacements preserve determinant; a swap changes the tracked sign.','elimination');factor=1
ops=[('Initial matrix',None),('Swap rows 1 and 2',('swap',0,1)),('R3 becomes R3 minus R1',('add',2,0,-1)),('R3 becomes R3 plus R2',('add',2,1,1)),('R4 becomes R4 minus twice R2',('add',3,1,-2)),('R4 becomes R4 minus three times R3',('add',3,2,-3))]
for label,op in ops:
 if op:
  if op[0]=='swap':A.row_swap(op[1],op[2]);factor=-factor
  else:A[op[1],:]=A[op[1],:]+op[3]*A[op[2],:]
 hot=[(op[1],j)for j in range(4)]if op else[];s=tx(35,32,label)+mat(A,90,105,100,75,hot)+tx(560,145,'Exact determinant ledger')+tx(560,210,f'det(current) = {factor} × det(original)',True)+tx(560,275,f'det(current) = {A.det()}',True)+tx(560,340,'No row has been normalized.')
 frame(m,dict(matrix=A.tolist(),factor=factor,original=orig.tolist(),determinant=str(A.det()),originalDeterminant=str(orig.det())),svg(s,470),label,'Only the highlighted row changes; the ledger remains valid at the exact current matrix.',r'\det A=\frac{'+str(A.det())+'}{'+str(factor)+'}=-2',[(r'\det M=k\det A',A.det()==factor*orig.det())])
A=S.Matrix([[2,1],[3,4]]);C=A.cofactor_matrix();adj=A.adjugate();m=model('adjugate-main','Transpose the cofactor matrix before multiplication','adjugate-product-grid','Rows of signed cofactors become columns of the adjugate. Product entries are exact row-column scalar products.','cramer')
for i,j in[(0,0),(0,1),(1,0),(1,1)]:
 result=sum(A[i,k]*adj[k,j]for k in range(2));s=tx(35,32,m['title'])+tx(65,85,'Original matrix')+mat(A,65,110,100,75,[(i,k)for k in range(2)])+tx(340,85,'Transposed cofactors')+mat(adj,340,110,100,75,[(k,j)for k in range(2)],id='adj')+tx(665,85,'Product')+mat(A*adj,665,110,100,75,[(i,j)],id='product')+tx(65,365,f'Product entry ({i+1},{j+1}) = {result}',True)+tx(65,420,'Diagonal entries equal det(A); off-diagonal entries cancel.')
 frame(m,dict(matrix=A.tolist(),adjugate=adj.tolist(),i=i,j=j,entry=str(result)),svg(s,470),'Compute one selected row-column product','The selected row of A meets the selected column of the transposed cofactor matrix.',r'A\operatorname{adj}A=5I_2',[(r'\text{selected product entry}',result)])
m=model('cramer-main','Column replacement changes one coordinate numerator','cramer-column-replacement','Each numerator replaces exactly one original column by the supplied right-hand side. The denominator remains det(A) = 5.','cramer');b=S.Matrix([5,6])
for j in[0,1]:
 N=A.copy();N[:,j]=b;val=N.det()/A.det();s=tx(35,32,m['title'])+tx(65,85,'Original coefficient matrix')+mat(A,65,110,100,75)+tx(470,85,f'Replace column {j+1} by b = (5,6)')+mat(N,470,110,100,75,[(i,j)for i in range(2)],id='replacement')+tx(65,375,f'Numerator = {N.det()}; denominator = {A.det()}; coordinate = {val}',True)
 frame(m,dict(matrix=N.tolist(),coefficient=A.tolist(),b=list(b),column=j,numerator=str(N.det()),denominator=str(A.det()),coordinate=str(val)),svg(s,440),'Replace one coefficient column','The untouched coefficient column retains its position. A signed ratio supplies the corresponding coordinate.',r'x_{'+str(j+1)+r'}=\frac{'+str(N.det())+'}{5}='+str(val),[(r'\det A\ne0',A.det()!=0)])
def cube(s1,s2):
 # Orthogonal invariant directions scaled independently; the scale never auto-fits.
 p=lambda x,y,z:(440+float(x)*68+float(z)*35,335-float(y)*48+float(z)*20)
 pts={tuple(v):p(v[0]*s1,v[1]*s2,v[2]*s2)for v in __import__('itertools').product([0,1],repeat=3)};out=''
 for k,v in pts.items():
  for axis in range(3):
   if k[axis]==0:
    other=list(k);other[axis]=1;out+=f'<g data-entity="cube-{k}-{axis}">'+ln(*v,*pts[tuple(other)],'#4d8276')+'</g>'
 return out
for id,params,kind in [('parameter-main',[-3,-2,0,1,2],'diagonal-subspace-volume'),('positivity-main',[-1,S.Rational(-1,2),0,S.Rational(1,2),1,S.Rational(3,2)],'quadratic-form-direction-factors')]:
 m=model(id,'Constant line and sum-zero plane: separate the two factors',kind,'One invariant direction is the constant line; two orthogonal directions span the sum-zero plane. The illustration is in that adapted basis, not the original columns.','parameter'if id=='parameter-main'else'positivity')
 for t in params:
  l=t+2 if id=='parameter-main'else 1+2*t;r=t-1 if id=='parameter-main'else 1-t;det=l*r*r
  s=tx(35,32,m['title'])+cube(l,r)+tx(65,95,f'Parameter = {t}',True)+tx(65,145,f'Constant-line factor = {l}',True)+tx(65,195,f'Sum-zero-plane factor = {r}',True)+tx(65,460,f'Determinant = {l} × ({r})² = {det}',True)+tx(65,505,'Positive definiteness needs both factors positive.'if id=='positivity-main'else'Zero factors collapse the corresponding invariant directions.')
  frame(m,dict(parameter=str(t),line=str(l),plane=str(r),determinant=str(det),positive=bool(l>0 and r>0)),svg(s,560),'Change the parameter and inspect each invariant direction','The line and plane may collapse at different parameters. A squared plane factor hides its sign in the determinant.',str(l)+r'\cdot('+str(r)+r')^2='+str(det),[(r'\text{line factor}>0',l>0),(r'\text{plane factor}>0',r>0)])
A=S.Matrix([[2,0,1],[0,3,2],[4,5,6]]);m=model('block-main','Block elimination: the Schur scalar appears after subtraction','partitioned-block-elimination','Gold marks the lower-left block being cleared; the matrix partition and multiplication order remain explicit.','blocks')
for k in[0,1,2]:
 M=A.copy()
 if k>=1:M[2,:]-=2*M[0,:]
 if k>=2:M[2,:]-=S.Rational(5,3)*M[1,:]
 s=tx(35,32,m['title'])+mat(M,95,110,110,80,[(2,j)for j in range(3)])+ln(310,103,310,355,'#9b673d')+ln(90,265,420,265,'#9b673d')+tx(510,165,'Pivot block: diagonal (2,3)')+tx(510,225,'Its determinant is 6.')+tx(510,285,f'Current bottom-right entry = {M[2,2]}',True)+tx(65,435,'After both replacements, the Schur complement is 2/3.')
 frame(m,dict(matrix=M.tolist(),step=k,determinant=str(M.det()),schur=str(M[2,2])),svg(s,490),'Clear one part of the lower-left block','Both row replacements preserve the full determinant. The bottom-right entry is a Schur complement only after the block is fully cleared.',r'\det M=4',[(r'\det M=4',M.det()==4)])
u=S.Matrix([1,2,-1]);v=S.Matrix([2,-1,3]);I=S.eye(3);m=model('update-main','Rank-one multilinearity: only single update columns survive','rank-one-selected-column-expansion','Each term changes one identity column to v_j u. Terms changing two columns vanish because those columns are proportional.','update');acc=S.Integer(1)
for j in range(3):
 N=I.copy();N[:,j]=v[j]*u;term=N.det();acc+=term;s=tx(35,32,m['title'])+mat(N,85,110,115,80,[(i,j)for i in range(3)])+tx(530,145,f'Select update column {j+1}',True)+tx(530,210,f'This determinant term = {term}',True)+tx(530,275,f'Identity plus processed terms = {acc}',True)+tx(65,445,'Full determinant: 1 + 2 − 2 − 3 = −2',True)
 frame(m,dict(matrix=N.tolist(),u=list(u),v=list(v),column=j,term=str(term),accumulator=str(acc)),svg(s,500),'Include one single-column update term','No two updated columns can contribute a nonzero term. The accumulator is a determinant expansion, not a determinant of an intermediate update.',r'\det(I+uv^T)=1+v^Tu=-2',[(r'\text{selected term}=u_jv_j',term==u[j]*v[j])])
m=model('vandermonde-main','Ordered interpolation nodes: signed differences and duplicate rows','node-to-power-matrix','Node positions follow the actual supplied ordered values. A duplicate node creates a duplicate row, not a missing interpolation coefficient.','vandermonde')
for nodes in[[1,3,2],[1,2,3],[1,2,2]]:
 A=S.Matrix([[x**j for j in range(3)]for x in nodes]);s=tx(35,32,m['title'])+mat(A,460,105,110,80)
 for i,x in enumerate(nodes):s+=rect(65,105+i*80,220,60)+tx(175,143+i*80,f'Node {i+1}: {x}',True,'middle')+ln(285,135+i*80,450,135+i*80)
 factors=[nodes[j]-nodes[i]for i in range(3)for j in range(i+1,3)];s+=tx(65,415,'Ordered differences = '+str(factors),True)+tx(65,465,'Determinant = '+str(A.det()),True)
 frame(m,dict(nodes=nodes,matrix=A.tolist(),factors=factors,determinant=str(A.det())),svg(s,520),'Change a supplied node or its row order','Columns remain powers zero, one, and two. Coincident nodes duplicate the full row and annihilate the determinant.',r'\det V='+str(A.det()),[(r'\text{distinct nodes}',len(set(nodes))==3)])
m=model('recurrence-main','Tridiagonal recurrence: compute the next scalar from two stored states','continuant-recurrence-plot','Horizontal positions are matrix orders 0 through 8; the vertical axis is the determinant on a fixed scale. D0 = 1 is retained as a real recurrence state.','recurrence');ds=[S.Integer(1),S.Integer(1)]
for n in range(2,9):ds.append(ds[-1]-ds[-2])
for n in range(9):
 s=tx(35,32,m['title'])+ln(110,240,880,240)
 for i in range(9):
  x=130+i*88;s+=tx(x,345,'n='+str(i),True,'middle')
  if i<=n:s+=f'<g data-entity="D-{i}"><circle cx="{x}" cy="{240-int(ds[i])*90}" r="8" fill="#4e8277"/>'+tx(x,240-int(ds[i])*90-18,ds[i],True,'middle')+'</g>'
 s+=tx(65,410,'D(n) = D(n−1) − D(n−2); no division by a prior determinant.',True)
 frame(m,dict(n=n,prefix=[str(x)for x in ds[:n+1]],determinant=str(ds[n])),svg(s,470),'Append one matrix order','The recurrence uses the last two exact scalar states, including zeros. Six-step repetition comes from recurrence-state repetition.',r'D_{'+str(n)+'}='+str(ds[n]),[(r'\text{initial or recurrence-consistent state}',True)])
U=S.Matrix([[1,0],[0,2],[1,1]]);m=model('gram-main','Embedded area: the three signed minors contribute squares','gram-minor-area','Three coordinate-plane projections have signed two-by-two minors. Their squared sum, not their signed sum, is the Gram determinant.','gram');acc=0
for k,(i,j)in enumerate([(0,1),(0,2),(1,2)]):
 N=U[[i,j],:];d=N.det();acc+=d*d;s=tx(35,32,m['title'])+mat(U,65,110,100,75,[(r,c)for r in[i,j]for c in range(2)])+tx(420,85,f'Projection rows {i+1} and {j+1}')+mat(N,420,110,100,75,id='projection')+tx(65,405,f'Signed projected minor = {d}; squared contribution = {d*d}',True)+tx(65,460,f'Squared area accumulator = {acc}; full area = 3',True)
 frame(m,dict(matrix=U.tolist(),subset=[i,j],minor=N.tolist(),contribution=str(d*d),accumulator=str(acc),gramDeterminant=str((U.T*U).det())),svg(s,520),'Select a coordinate-plane minor','Its sign is squared for Gram volume; the rectangular original matrix has no ordinary determinant.',str(d)+'^2='+str(d*d),[(r'\text{Gram determinant}=9',(U.T*U).det()==9)])
m=model('triangle-main','Translate vertices into edges before measuring triangle area','oriented-triangle-translation','These are the actual vertices from Question 37. Translation subtracts the base vertex; it preserves both edge differences and unsigned triangle area.','problem-only')
for shift in [(0,0),(-1,-2)]:
 vertices=[(x+shift[0],y+shift[1])for x,y in[(1,2),(4,3),(2,6)]];P=lambda t:(190+t[0]*95,660-t[1]*85);pts=[P(t)for t in vertices]
 s=tx(35,32,m['title'])+ln(105,660,845,660)+ln(190,85,190,710)+f'<g data-entity="triangle"><polygon points="'+ ' '.join(f'{x},{y}'for x,y in pts)+'" fill="#dcebe3" stroke="#4c8275" stroke-width="2"/></g>'
 for i,(pt,vertex)in enumerate(zip(pts,vertices)):s+=f'<g data-entity="vertex-{i}"><circle cx="{pt[0]}" cy="{pt[1]}" r="6" fill="#9b673d"/>'+tx(pt[0]+15,pt[1]-12,str(vertex),True)+'</g>'
 s+=tx(65,765,'Edge columns = (3,1), (1,4); determinant = 11; triangle area = 11/2',True)
 frame(m,dict(vertices=vertices,shift=shift,edgeMatrix=[[3,1],[1,4]],twiceArea='11',area='11/2'),svg(s,820),'Subtract the base vertex'if shift!=(0,0)else'Read the original vertices','Translation changes absolute positions but leaves the two edge differences and area unchanged.',r'\text{Area}=\frac{|11|}{2}=\frac{11}{2}',[(r'\text{edge determinant}=11',True)])
m=model('reflection-main','A reflection negates its normal and preserves the tangent','reflection-vector-geometry','The unit normal and its perpendicular tangent are actual vectors from Question 42. The displayed operator is identity first and then the exact reflection.','problem-only')
u=S.Matrix([S.Rational(3,5),S.Rational(4,5)]);w=S.Matrix([S.Rational(-4,5),S.Rational(3,5)]);H=S.eye(2)-2*u*u.T
for A in[S.eye(2),H]:
 s=tx(35,32,m['title'])+ln(120,335,860,335)+ln(480,90,480,545)
 for id,vec,col in[('normal',A*u,'#9b673d'),('tangent',A*w,'#3c728d')]:
  x=480+float(vec[0])*190;y=335-float(vec[1])*190;s+=f'<g data-entity="{id}">'+ln(480,335,x,y,col)+f'<circle cx="{x}" cy="{y}" r="7" fill="{col}"/>'+tx(x+12,y-12,id)+'</g>'
 s+=tx(65,605,'Normal eigenvalue −1; tangent eigenvalue +1; reflection determinant −1',True)
 frame(m,dict(matrix=A.tolist(),normal=list(A*u),tangent=list(A*w),determinant=str(A.det())),svg(s,660),'Apply the reflection'if A==H else'Inspect the original directions','The perpendicular direction remains fixed, while the unit normal reverses. The transition is a preview between the exact endpoint operators.',r'\det A='+str(A.det()),[(r'\text{tangent remains fixed}',A*w==w)])
(R/'dist/chapters/l_det-models.json').write_text(json.dumps(dict(topicId='l_det',groups=groups,models=models),indent=2)+'\n')
print(len(models),'different concept models,',sum(len(m['frames'])for m in models),'exact checkpoints')
