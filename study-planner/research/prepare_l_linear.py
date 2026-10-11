"""Generate typed pipelines, exact operator checkpoints and compact geometric models."""
from pathlib import Path
from html import escape
import json,hashlib,sys,math,copy
import sympy as S
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_linear-evidence'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
models=[];groups={};specs=[]
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def rows(A):return [[str(z)for z in row]for row in S.Matrix(A).tolist()]
def tex(A):return S.latex(S.Matrix(A),mat_delim='',mat_str='pmatrix')
def mh(t):return mathml.render(t,True)
def tx(x,y,s,cls='prose',anchor='start'):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="lt-{cls}">{escape(str(s))}</text>'
def svg(body):return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" data-visual-type="plot"><defs><marker id="lt-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 1L9 5L0 9" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs>'+body+'</svg>'
def line(x1,y1,x2,y2,color='#315d72',arrow=False):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2"'+(' marker-end="url(#lt-arrow)"'if arrow else'')+'/>'
def frame(snapshot,drawing,formula,action,why):
 return dict(label=action,snapshot=snapshot,svg=drawing,formulaHtml=mh(formula),caption=why,teaching=dict(operation=action,why=why,currentState=snapshot,checks=[dict(mathHtml=mh(formula),result='true')],reading='Follow physical vectors and labelled coordinate spaces separately. Checkpoints contain computed values, not interpolated arithmetic.'))
def model(id,title,kind,invariant,frames,group=None):
 guide=['Read the stated spaces and field.','Identify the current operation.','Check the exact coordinates or matrix entries.','Verify the endpoint against the original map.']
 for i,f in enumerate(frames):
  f['index']=i;f['teaching'].update(initial=i==0,guide=guide,activeLine=min(i,3),mode=kind)
  prev=frames[i-1]['snapshot']if i else{}
  f['teaching']['changes']=[dict(field=k,before=prev.get(k),after=v)for k,v in f['snapshot'].items()if prev.get(k)!=v]
  f['teaching']['reading']=invariant
 m=dict(id=id,title=title,kind=kind,invariant=invariant,code=guide,frames=frames);models.append(m)
 if group:groups.setdefault(group,[]).append(id)
 return m
def pipeline(id,title,A,P,Q,x,group=None):
 A,P,Q,x=map(S.Matrix,(A,P,Q,x));v=P*x;y=A*v;c=Q.inv()*y;M=Q.inv()*A*P
 values=[x,v,y,c];labels=['Input coefficients','Physical input','Physical output','Output coefficients'];ops=['P synthesis','A physical map','Q inverse analysis'];frames=[]
 for stage in range(4):
  body=tx(24,30,'A typed coordinate pipeline · every box has a distinct role')
  for j,z in enumerate(values):
   left=20+j*190;body+=f'<g data-entity="box-{j}"><rect x="{left}" y="92" width="150" height="130" rx="8" fill="'+('#e7f0e9'if j<=stage else'#f3f5f4')+'" stroke="#91aca8"/>'+tx(left+75,119,labels[j],anchor='middle')
   for k,a in enumerate(z):
    body+=tx(left+75,156+k*23,str(a)if j<=stage else'?',cls='math',anchor='middle')
   body+='</g>'
   if j<3:body+=line(left+150,184,left+190,184,arrow=True)+tx(left+170,72,ops[j],anchor='middle')
  body+=tx(24,283,'Read right to left in Q inverse × A × P; this diagram reads left to right.')
  body+=tx(24,321,'The physical output equals Q × final output coefficients.')
  formulas=[r'[v]_B='+tex(x),r'v=P[v]_B='+tex(v),r'T(v)=Av='+tex(y),r'[T(v)]_C=Q^{-1}AP[v]_B='+tex(c)]
  snap=dict(A=rows(A),P=rows(P),Q=rows(Q),input=rows(x),physicalInput=rows(v),physicalOutput=rows(y),output=rows(c),stage=stage,representation=rows(M))
  frames.append(frame(snap,svg(body),formulas[stage],['Read input coefficients',*ops][stage],'Synthesis constructs the physical input, the operator acts on it, and inverse synthesis extracts output coefficients. Each arrow names its coordinate operation.'))
 specs.append(dict(id=id,kind='pipeline',A=rows(A),P=rows(P),Q=rows(Q),input=rows(x),expectedMatrix=rows(M),expectedOutput=rows(c)))
 return model(id,title,'typed-coordinate-pipeline','All numerical values are exact rationals. P and Q are standard synthesis matrices. The last box contains coefficients, not the physical output.',frames,group)
def geometry(id,title,matrices,kind,group,notes):
 frames=[];base=S.Matrix([1,1]);points=[(-2,-2),(2,-2),(2,2),(-2,2)];scale=30;cx=270;cy=190
 def pt(v):return (float(cx+scale*v[0]),float(cy-scale*v[1]))
 def segment(u,v,color='#d4dedb',entity=None):
  x1,y1=pt(u);x2,y2=pt(v)
  return ('<g data-entity="'+entity+'">'if entity else'')+line(x1,y1,x2,y2,color)+('</g>'if entity else'')
 for i,(A,description)in enumerate(matrices):
  A=S.Matrix(A);body=tx(24,30,title)
  body+=segment(S.Matrix([-3,0]),S.Matrix([3,0]),'#8f9e9d')+segment(S.Matrix([0,-3]),S.Matrix([0,3]),'#8f9e9d')
  body+=tx(401,195,'x','math')+tx(280,68,'y','math')
  # Rotation uses an actual SVG angle transform, so in-flight movement remains rotation.
  angle=(i*90/(len(matrices)-1))if kind=='angle-rotation'else None
  if angle is not None:
   body+=f'<g data-entity="rotating-grid" transform="rotate({-angle} {cx} {cy})">'
   for k in range(-2,3):
    body+=segment(S.Matrix([k,-2]),S.Matrix([k,2]))+segment(S.Matrix([-2,k]),S.Matrix([2,k]))
   ps=' '.join(f'{a},{b}'for a,b in[pt(S.Matrix(p))for p in points])
   body+=f'<polygon points="{ps}" fill="#c9ddd3" fill-opacity=".4" stroke="#588a76" stroke-width="2"/>'
   x2,y2=pt(base);body+=line(cx,cy,x2,y2,'#9e6741',True)+'</g>'
  else:
   for k in range(-2,3):
    body+=segment(A*S.Matrix([k,-2]),A*S.Matrix([k,2]),entity='grid-v'+str(k))+segment(A*S.Matrix([-2,k]),A*S.Matrix([2,k]),entity='grid-h'+str(k))
   ps=' '.join(f'{a},{b}'for a,b in[pt(A*S.Matrix(p))for p in points])
   body+=f'<g data-entity="unit-polygon"><polygon points="{ps}" fill="#c9ddd3" fill-opacity=".4" stroke="#588a76" stroke-width="2"/></g>'
   x2,y2=pt(A*base)
   zero=A*base==S.zeros(2,1)
   body+='<g'+(''if kind=='discrete-reflection'else' data-entity="vector"')+'>'+((f'<circle cx="{cx}" cy="{cy}" r="5" fill="#9e6741"/>')if zero else line(cx,cy,x2,y2,'#9e6741',True))+'</g>'
  body+=tx(490,100,'Physical input: (1, 1)','math')+tx(490,140,'Output: '+str(tuple(round(float(a),3)for a in A*base)),'math')
  body+=tx(490,183,'Rank: '+str(A.rank()),'math')+tx(490,226,description)
  body+=tx(24,330,notes)
  snapshot=dict(matrix=rows(A),input=rows(base),output=rows(A*base),step=i)
  if angle is not None:snapshot['angleDegrees']=angle
  frames.append(frame(snapshot,svg(body),r'A='+tex(A),description,notes+' The labelled output is the current exact checkpoint; controls expose each stage.'))
 specs.append(dict(id=id,kind=kind,matrices=[rows(S.Matrix(A))for A,_ in matrices]))
 return model(id,title,kind,notes,frames,group)
I=S.eye(2)
geometry('scale','Uniform scaling',[(a*I,'Factor '+str(a))for a in [1,S.Rational(5,4),S.Rational(3,2),S.Rational(7,4),2]],'uniform-scale','geometry','Both components scale together; this is the Cartesian form of radial doubling.')
angles=[S.pi*k/16 for k in range(9)]
geometry('rotation','Rotation follows the angle',[(S.Matrix([[S.cos(t),-S.sin(t)],[S.sin(t),S.cos(t)]]),'Angle '+str(k*90/8)+' degrees')for k,t in enumerate(angles)],'angle-rotation','transforms','A rotating SVG group interpolates the angle; length and area remain unchanged.')
geometry('reflection','Reflection is a discrete orientation switch',[(I,'Before reflection'),(S.diag(1,-1),'After reflection')],'discrete-reflection','transforms','Endpoints are identity and horizontal reflection; no invertible connecting path is claimed.')
geometry('shear','Horizontal shear',[(S.Matrix([[1,s],[0,1]]),'Shear coefficient '+str(s))for s in [0,S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),1]],'linear-shear','transforms','Horizontal displacement is s times the original vertical component; area stays fixed.')
geometry('oblique','Projection along a diagonal direction',[(S.Matrix([[1,-t],[0,1-t]]),'Elimination fraction '+str(t))for t in [0,S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),1]],'oblique-collapse','projection','Intermediate maps approach P; only the final map is the stated projection.')
geometry('orthogonal','Projection with perpendicular residual',[(S.diag(1,1-t),'Vertical removal '+str(t))for t in [0,S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),1]],'orthogonal-collapse','projection','Only the final map is projection; its discarded direction is perpendicular to the image.')
geometry('nilpotent-plane','A planar nilpotent power',[(I,'Power zero'),(S.Matrix([[0,1],[0,0]]),'Power one'),(S.zeros(2),'Power two')],'operator-powers','powers','These are discrete powers of one operator, not a continuous path of powers.')
pipeline('basis-images','Reconstructing the basis-image map',[[-1,2],[1,-1]],[[1,2],[1,1]],I,[1,2],'coordinates')
pipeline('two-bases','Independent domain and codomain bases',[[1,2],[0,1]],[[1,0],[1,1]],[[1,1],[0,1]],[2,-1],'coordinates')
pipeline('basis-transition','A physical identity with changing coordinates',I,[[1,1],[1,-1]],[[2,1],[0,1]],[2,1],'passive')
pipeline('similarity','The same physical operator in a skewed common basis',[[2,1],[3,-2]],[[1,-2],[-2,5]],[[1,-2],[-2,5]],[1,1],'passive')
def flow(id,title,steps,group,scope):
 frames=[]
 for j,(labels,values,formula,action)in enumerate(steps):
  assert len(labels)==len(values)<=4
  n=len(labels);w=150;gap=(700-n*w)/(n-1)if n>1 else 0
  body=tx(24,30,title)
  for k,(label,value)in enumerate(zip(labels,values)):
   x=30+k*(w+gap)
   body+=f'<g data-entity="state-{k}"><rect x="{x}" y="95" width="{w}" height="128" rx="8" fill="#e6efea" stroke="#91aca8"/>'+tx(x+w/2,124,label,anchor='middle')
   vals=value if isinstance(value,list)else[value]
   for ii,a in enumerate(vals):body+=tx(x+w/2,160+ii*23,a,'math','middle')
   body+='</g>'
   if k<n-1:body+=line(x+w,185,x+w+gap,185,arrow=True)
  body+=tx(24,282,action)+tx(24,325,scope)
  frames.append(frame(dict(step=j,labels=labels,values=values),svg(body),formula,action,scope))
 return model(id,title,'exact-coefficient-flow',scope,frames,group)
flow('prescriptions','The input relation constrains output labels',[
 (['First image','Second image','Forced third'],['(1, 0)','(0, 1)','?'],r'T(e_1+e_2)=T(e_1)+T(e_2)','Read the dependent input list'),
 (['First image','Second image','Forced third'],['(1, 0)','(0, 1)','(1, 1)'],r'T(e_1+e_2)=(1,1)^T','The proposed (2, 2) violates this forced sum')],'coordinates','The third input is the sum of the first two; the relation is part of the specification.')
flow('rank-normal','Adapted bases reveal the lost directions',[
 (['Domain basis','Image basis'],[['u1, u2','k1, k2'],['T(u1), T(u2)']],r'\dim V=4','Extend the kernel basis'),
 (['Domain basis','Image basis'],[['u1, u2','k1, k2'],['2 independent','2 zero images']],r'\operatorname{rank}T=2','The added basis images are independent')],'rank-nullity','This is a rank-two map with a two-dimensional kernel, expressed in adapted bases.')
flow('bridge','Composition with intermediate reexpression',[
 (['Input','C coordinates','E coordinates','Final output'],['(1, 2)','(3, 2)','?','?'],r'R=\begin{pmatrix}1&1\\0&1\end{pmatrix}','First map produced C coordinates'),
 (['Input','C coordinates','E coordinates','Final output'],['(1, 2)','(3, 2)','(5, 2)','?'],r'R(3,2)^T=(5,2)^T','Convert the same intermediate vector'),
 (['Input','C coordinates','E coordinates','Final output'],['(1, 2)','(3, 2)','(5, 2)','(5, 7)'],r'\begin{pmatrix}1&0\\1&1\end{pmatrix}(5,2)^T=(5,7)^T','Apply the outer map in its expected basis')],'composition','The intermediate change is passive; applying the outer matrix without it gives the wrong result.')
H=S.Matrix([[1,1],[0,1]]);K=S.Matrix([[1,0],[1,1]])
flow('shears','Both orders retain their intermediate vectors',[
 (['First order','Reverse order'],[['e1 = (1, 0)','H first'],['e1 = (1, 0)','K first']],r'H e_1=(1,0)^T','Read the two operations'),
 (['First order','Reverse order'],[['(1, 0)','after H'],['(1, 1)','after K']],r'K e_1=(1,1)^T','Inspect the intermediate states'),
 (['First order','Reverse order'],[['(1, 1)','after K'],['(2, 1)','after H']],r'KH e_1\ne HK e_1','The final vectors differ')],'composition','Horizontal and vertical shears do not commute.')
flow('derivative-bases','Differentiation needs output-basis analysis',[
 (['Input polynomial','Physical derivative','Output coefficients'],['1 + x + x²','?','?'],r'D(1+x+x^2)=1+2x','Choose the third input basis vector'),
 (['Input polynomial','Physical derivative','Output coefficients'],['1 + x + x²','1 + 2x','(-1, 2)'],r'1+2x=-1+2(1+x)','Analyze in output basis (1, 1 + x)')],'polynomials','The coefficient column (-1, 2) is not the monomial coefficient column (1, 2).')
flow('characteristic-two','Derivative coefficients modulo two',[
 (['Domain basis','Derivative images'],[['1, x, x²','x³, x⁴'],['0, 1, 0','x², 0']],r'D(x^k)=k x^{k-1}','Differentiate each basis vector'),
 (['Kernel basis','Image basis'],[['1, x², x⁴'],['1, x²']],r'3+2=5','Count independent zero and nonzero directions')],'polynomials','The field is F2; even coefficients vanish and extra kernel directions appear.')
flow('evaluation','Sampling versus polynomial coefficients',[
 (['Polynomial','Value at 0','Value at 1','Value at 2'],['1 + x²','?','?','?'],r'p(x)=1+x^2','Start with the polynomial'),
 (['Polynomial','Value at 0','Value at 1','Value at 2'],['1 + x²','1','2','5'],r'E(p)=(1,2,5)^T','Evaluate at distinct nodes')],'polynomials','Three distinct measurements determine a degree-at-most-two polynomial.')
flow('compression','A fixed mask deletes a basis component',[
 (['Physical input','Coefficients','Masked','Reconstruction'],['(3, 1)','(2, 1)','?','?'],r'W=\begin{pmatrix}1&1\\1&-1\end{pmatrix}','Convert without losing information'),
 (['Physical input','Coefficients','Masked','Reconstruction'],['(3, 1)','(2, 1)','(2, 0)','(2, 2)'],r'W\operatorname{diag}(1,0)W^{-1}(3,1)^T=(2,2)^T','Discard only the second coordinate')],'compression','This fixed mask projects onto the retained first basis direction.')
flow('transpose','Transpose permutes matrix-entry identities',[
 (['Original rows','Transposed rows'],[['1, 2','3, 4'],['?','?']],r'X=\begin{pmatrix}1&2\\3&4\end{pmatrix}','Read the four matrix units'),
 (['Original rows','Transposed rows'],[['1, 2','3, 4'],['1, 3','2, 4']],r'X^T=\begin{pmatrix}1&3\\2&4\end{pmatrix}','Exchange off-diagonal entry roles')],'matrix-operators','Storage rows do not change identity; only the operator assigns new output positions.')
flow('trace','Trace extracts a scalar from matrix space',[
 (['Diagonal','Off diagonal','Trace output'],[['2, -1, 4'],['Arbitrary'],['?']],r'\operatorname{tr}X=x_{11}+x_{22}+x_{33}','Read the diagonal contributions'),
 (['Diagonal','Off diagonal','Trace output'],[['2, -1, 4'],['Arbitrary'],['5']],r'2-1+4=5','Sum only the diagonal entries')],'matrix-operators','Trace is one independent linear measurement; off-diagonal entries belong to its kernel.')
flow('sylvester','Solve independent matrix-unit equations',[
 (['Differences','Output rows','Input rows'],[['1, -1','3, 1'],['2, 4','6, 8'],['?','?']],r'(a_i-b_j)x_{ij}=c_{ij}','Read the four nonzero multipliers'),
 (['Differences','Output rows','Input rows'],[['1, -1','3, 1'],['2, 4','6, 8'],['2, -4','2, 8']],r'X=\begin{pmatrix}2&-4\\2&8\end{pmatrix}','Divide entrywise and substitute')],'matrix-operators','A diagonal Sylvester operator acts separately on each matrix-unit coordinate.')
flow('commutator','Zero multipliers create consistency conditions',[
 (['Differences','Allowed output','Input freedom'],[['0, -1','1, 0'],['0, a','b, 0'],['u, -a','b, v']],r'AX-XA=\begin{pmatrix}0&a\\b&0\end{pmatrix}','Separate free diagonal and constrained off-diagonal entries'),
 (['Kernel','Image','Dimensions'],['Diagonal','Off diagonal',['nullity 2','rank 2']],r'2+2=4','Count operator dimensions')],'matrix-operators','The diagonal entries of the output must vanish; both input diagonal entries remain free.')
flow('nilpotent','A three-dimensional shift loses one layer per power',[
 (['Original','Power one','Power two','Power three'],['(1, 2, 3)','?','?','?'],r'T(x,y,z)=(0,x,y)','Read the original vector'),
 (['Original','Power one','Power two','Power three'],['(1, 2, 3)','(0, 1, 2)','?','?'],r'T(1,2,3)=(0,1,2)','Apply the first shift'),
 (['Original','Power one','Power two','Power three'],['(1, 2, 3)','(0, 1, 2)','(0, 0, 1)','?'],r'T^2(1,2,3)=(0,0,1)','Apply the same map again'),
 (['Original','Power one','Power two','Power three'],['(1, 2, 3)','(0, 1, 2)','(0, 0, 1)','(0, 0, 0)'],r'T^3=0','The final layer is lost')],'powers','These are discrete applications; the ranks are two, one, and zero.')
def fibers():
 frames=[]
 for t in [-2,-1,0,1,2]:
  x=S.Matrix([3+t,-t]);body=tx(24,30,'Different inputs have the same attained output')
  # Original coordinates at a smaller scale keep all listed witnesses within the viewport.
  cx,cy,sc=255,180,24
  body+=line(cx-120,cy,cx+160,cy,'#9baba8')+line(cx,cy+90,cx,cy-90,'#9baba8')
  body+=line(cx+sc,cy-2*sc,cx+5*sc,cy+2*sc,'#668e82')
  xx,yy=cx+sc*float(x[0]),cy-sc*float(x[1])
  body+=f'<g data-entity="fiber-witness"><circle cx="{xx}" cy="{yy}" r="6" fill="#9e6741"/></g>'
  body+=tx(490,100,'Input: '+str(tuple(x)),'math')+tx(490,150,'Output: (3, 0)','math')+tx(490,200,'Direction: (1, −1)','math')
  body+=tx(24,320,'All shown inputs lie on x + y = 3; the symbolic proof covers every real t.')
  frames.append(frame(dict(t=t,input=rows(x),output=[[3],[0]]),svg(body),r'T(3+t,-t)=(3,0)', 'Move along the kernel direction','Adding a kernel vector changes the input without changing the attained output.'))
 model('fiber-sum','An affine fiber parallel to the kernel','kernel-fiber','T(x,y) = (x + y, 0). Only outputs on the horizontal axis are attainable.',frames,'fibers')
fibers()
flow('product-collapse','An attained subspace is killed by the outer map',[
 (['Original input','After inner map','After outer map'],['(2, 3)','(2, 0)','?'],r'T=\operatorname{diag}(1,0)','The inner map keeps the first axis'),
 (['Original input','After inner map','After outer map'],['(2, 3)','(2, 0)','(0, 0)'],r'ST=0','The outer map kills that entire attained axis')],None,'Each factor has rank one; their product has rank zero because image meets kernel.')
qs=json.loads((B/'l_linear-questions.json').read_text())
for q in qs:
 if q['title'].startswith('Exact coordinate pipeline'):
  i=int(q['title'].split()[-1])-1;c=json.loads((E/'question-certificates.json').read_text())[i];id='question-pipeline-'+str(i+1)
  pipeline(id,q['title'],c['A'],c['P'],c['Q'],c['input']);q['modelId']=id
save(B/'l_linear-questions.json',qs)
auth=json.loads((B/'l_spaces-authentic.json').read_text())
flow('symmetric-trace','The authentic four-by-four dimension calculation',[
 (['Symmetric entries','Trace measurement','Remaining freedom'],[['4 diagonal','6 off diagonal'],['One nonzero','linear constraint'],['?']],r'\dim \operatorname{Sym}_4=10','Count independent symmetric entries'),
 (['Symmetric entries','Trace measurement','Remaining freedom'],[['4 diagonal','6 off diagonal'],['One nonzero','linear constraint'],['3 diagonal','6 off diagonal','Total 9']],r'\dim\ker(\operatorname{tr}|_{\operatorname{Sym}_4})=10-1=9','Apply rank–nullity to the trace functional')],None,'This model uses exactly the real four-by-four symmetric space in the authentic question.')
for q in auth:
 q['title']='Explicit linear-map revisit: '+q['title'];q['origin']='Authentic archive revisit; not a new distinct examination item'
 q['modelId']='symmetric-trace'if q['questionNumber']==41 else'orthogonal'
 path=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/q['repoPath']
 assert hashlib.sha256(path.read_bytes()).hexdigest()==q['sourceSha256']
save(B/'l_linear-authentic.json',auth)
save(R/'dist/chapters/l_linear-models.json',dict(topicId='l_linear',models=models,groups=groups))
save(E/'model-specs.json',specs)
save(E/'problem-visual-decisions.json',[dict(id=q['id'],modelId=q.get('modelId'),decision='Data-matched walkthrough accompanies this solution.'if q.get('modelId')else'The complete algebraic proof or counterexample is clearer than an additional moving diagram.')for q in qs+auth])
print(len(models),'models;',sum(len(m['frames'])for m in models),'checkpoints')
