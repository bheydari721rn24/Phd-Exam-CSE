"""Build exact decomposition-specific models; numerical snapshots never interpolate."""
from pathlib import Path
from html import escape
import json,sys,math,hashlib,re,sympy as S
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_orthogonality-evidence'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
models=[];groups={};specs=[]
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def rows(A):return[[str(z)for z in row]for row in S.Matrix(A).tolist()]
def tex(A):return S.latex(S.Matrix(A),mat_delim='',mat_str='pmatrix')
def mh(t):
 t=re.sub(r'\\\|(.+?)\\\|',lambda m:r'{\Vert '+m[1]+r'\Vert}',t)
 return mathml.render(t,True)
def tx(x,y,s,cls='prose',anchor='start'):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="og-{cls}">{escape(str(s))}</text>'
def line(a,b,color='#315d72',arrow=False):return f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" stroke-width="2"'+(' marker-end="url(#og-arrow)"'if arrow else'')+'/>'
def svg(body):return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 360" role="img" data-visual-type="plot"><defs><marker id="og-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 1L9 5L0 9" fill="none" stroke="context-stroke" stroke-width="1.5"/></marker></defs>'+body+'</svg>'
def frame(snap,drawing,formula,action,why):
 return dict(label=action,snapshot=snap,svg=drawing,formulaHtml=mh(formula),caption=why,teaching=dict(operation=action+' at this checkpoint',why=why,currentState=snap,checks=[dict(mathHtml=mh(formula),result='true')]))
def model(id,title,kind,invariant,frames,guide,group=None):
 for i,f in enumerate(frames):
  prev=frames[i-1]['snapshot']if i else{}
  f['teaching'].update(initial=i==0,reading=invariant,guide=guide,activeLine=min(i,len(guide)-1),mode=kind,changes=[dict(field=k,before=prev.get(k),after=v)for k,v in f['snapshot'].items()if prev.get(k)!=v])
 m=dict(id=id,title=title,kind=kind,invariant=invariant,code=guide,frames=frames);models.append(m)
 if group:groups.setdefault(group,[]).append(id)
 return m
def vstr(v):return '('+', '.join(str(z)for z in v)+')'
def projection(id,title,A,x,G=None,group=None):
 A,x=S.Matrix(A),S.Matrix(x);G=S.eye(A.rows)if G is None else S.Matrix(G);piv=list(A.rref()[1]);C=A[:,piv]
 P=S.zeros(A.rows)if not piv else C*(C.T*G*C).inv()*C.T*G
 p=P*x;r=x-p;dist=(r.T*G*r)[0];frames=[];isplane=A.rows==2
 def drawing(stage):
  body=tx(24,30,title)
  if isplane:
   scale=95/max(1,*[abs(float(v))for v in list(x)+list(p)+list(r)]);cx=240;cy=194
   def pt(v):return(float(cx+scale*v[0]),float(cy-scale*v[1]))
   body+=line((70,cy),(425,cy),'#bdc9c3')+line((cx,64),(cx,294),'#bdc9c3')
   if C.cols==1:
    u=C[:,0];u=u/S.sqrt((u.T*u)[0]);body+=line(pt(-S.Rational(110)/scale*u),pt(S.Rational(110)/scale*u),'#779782')
   for name,v,start,col,available in [('input',x,S.zeros(2,1),'#315d72',True),('projection',p,S.zeros(2,1),'#547d51',stage>=1),('residual',r,p,'#ad784a',stage>=2)]:
    if not available:continue
    a,b=pt(start),pt(start+v)
    body+='<g data-entity="'+name+'">'+(f'<circle cx="{a[0]}" cy="{a[1]}" r="4" fill="{col}"/>'if v==S.zeros(2,1)else line(a,b,col,True))+'</g>'
   body+=tx(480,105,'Input '+vstr(x),'math')+tx(480,148,'Projection '+(vstr(p)if stage>=1 else'?'),'math')+tx(480,191,'Residual '+(vstr(r)if stage>=2 else'?'),'math')
   body+=tx(480,238,'Squared distance '+(str(dist)if stage>=3 else'?'),'math')
   body+=tx(24,318,'Blue: input. Green: subspace component. Brown: residual from its tip.')
  else:
   # Component bars represent n-dimensional coordinates; no planar angle is claimed.
   vectors=[x,p,r];labels=['Input','Projected part','Residual'];colors=['#315d72','#547d51','#ad784a']
   bound=max(1,*[abs(float(v))for z in vectors for v in z]);scale=45/bound
   for j,(v,label,col)in enumerate(zip(vectors,labels,colors)):
    left=30+240*j;body+=tx(left+102,72,label,anchor='middle')
    body+=f'<rect x="{left}" y="91" width="205" height="175" rx="8" fill="#f0f4f1" stroke="#a8bbb0"/>'
    zero=left+101;body+=line((zero,108),(zero,250),'#a3b3ab')
    for k,z in enumerate(v):
     y=124+33*k;avail=j==0 or stage>=j
     body+=tx(left+12,y+5,'x'+str(k+1).translate(str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')),'math')
     if avail:
      endpoint=float(z)*scale;body+=f'<g data-entity="bar-{j}-{k}">'+line((zero,y),(zero+endpoint,y),col)+'</g>'
      body+=tx(left+191,y+5,str(z),'math','end')
     else:body+=tx(left+191,y+5,'?','math','end')
   body+=tx(24,310,'Coordinate bars preserve signs and magnitudes; they do not depict spatial angles.')
   body+=tx(24,339,'Squared distance '+(str(dist)if stage>=3 else'?'),'math')
  return svg(body)
 for stage in range(4):
  formula=[r'x='+tex(x),r'p=Px='+tex(p),r'r=x-p='+tex(r),r'r^TGr='+S.latex(dist)][stage]
  snap=dict(stage=stage,A=rows(A),G=rows(G),input=rows(x),projection=rows(p),residual=rows(r),P=rows(P),distanceSquared=str(dist),pivotColumns=piv)
  frames.append(frame(snap,drawing(stage),formula,['Read target and generators','Find the subspace component','Expose the perpendicular residual','Verify the squared distance'][stage],'The projected vector is in the original column span and the residual has zero product against that basis in the declared metric.'))
 specs.append(dict(id=id,kind='projection',A=rows(A),G=rows(G),input=rows(x),P=rows(P)))
 return model(id,title,'perpendicular-decomposition','Exact checkpoint values use the stated metric. Motion reveals components; the proof uses membership and zero residual products.',frames,['Read the target','Project onto a retained column basis','Subtract from the original target','Check membership, perpendicularity and distance'],group)
projection('line','Euclidean line: a nonunit generator',[[2],[1]],[1,3],group='line')
projection('weighted','Weighted line: perpendicularity depends on G',[[1],[1]],[2,0],S.diag(1,4),'weighted')
projection('auth-projection','Projection contracts length',[[1],[0]],[0,1],group='authentic')
projection('metric','Weighted orthogonality in the same physical plane',[[1],[1]],[4,-1],S.diag(1,4),'metric')
for z in json.loads((E/'question-certificates.json').read_text()):
 projection(z['modelId'],'Exact subspace case '+z['modelId'].split('-')[1],z['A'],z['x'],z['G'])
def oblique():
 frames=[];x=S.Matrix([0,1]);p=S.Matrix([2,0]);r=x-p
 for i in range(3):
  cx=220;cy=205;scale=55
  def pt(v):return(float(cx+scale*v[0]),float(cy-scale*v[1]))
  body=tx(24,30,'Oblique projection follows a nonperpendicular kernel')
  body+=line((65,cy),(415,cy),'#779782')+line(pt(-S.Matrix([-2,1])),pt(S.Matrix([-2,1])),'#beaa8c')
  body+=line(pt(S.zeros(2,1)),pt(x),'#315d72',True)
  if i>=1:body+='<g data-entity="oblique-output">'+line(pt(S.zeros(2,1)),pt(p),'#547d51',True)+'</g>'
  if i>=2:body+=line(pt(p),pt(x),'#ad784a',True)
  body+=tx(480,100,'Input length: 1','math')+tx(480,145,'Output length: '+('2'if i else'?'),'math')+tx(480,190,'Kernel: span((-2, 1))','math')+tx(24,315,'The residual follows the kernel, not the Euclidean normal.')
  frames.append(frame(dict(stage=i,input=rows(x),projection=rows(p),residual=rows(r)),svg(body),r'P='+tex([[1,2],[0,0]]),'Reveal '+['input','output','kernel residual'][i],'Idempotence holds, but symmetry and Euclidean norm contraction fail.'))
 model('oblique','Idempotence does not imply perpendicularity','oblique-projection','Compare the oblique residual direction with the vertical Euclidean normal; exact lengths show expansion.',frames,['Read the vertical input','Apply the idempotent','Inspect the discarded kernel direction'],'oblique')
oblique()
# Gram–Schmidt: exact coordinate subtraction and prefix-specific checks.
A=S.Matrix([[1,1,0],[1,0,1],[0,1,1]]);accepted=[];frames=[]
for k in range(3):
 raw=A[:,k];v=raw
 phases=[('Read column',v,None)]
 for j,u in enumerate(accepted):
  coef=(u.T*raw)[0]/(u.T*u)[0];v=v-coef*u;phases.append(('Remove component '+str(j+1),v,coef))
 phases.extend([('Accept perpendicular residual',v,None),('Normalize accepted residual',v/S.sqrt(v.dot(v)),None)])
 for action,current,coef in phases:
  body=tx(24,30,'Gram–Schmidt: residual coordinates after each subtraction')
  final=action.startswith(('Accept','Normalize'))
  labels=['Current input','Unit output'if action.startswith('Normalize')else'Current residual','Accepted count'];values=[list(raw),list(current),[len(accepted)+int(final)]]
  for col,(label,val)in enumerate(zip(labels,values)):
   left=30+240*col;body+=f'<rect x="{left}" y="90" width="205" height="160" rx="8" fill="#edf2ee" stroke="#a0b3a7"/>'+tx(left+102,120,label,anchor='middle')
   for j,z in enumerate(val):body+=tx(left+102,159+26*j,str(z).replace('sqrt(3)','√3').replace('sqrt(2)','√2').replace('sqrt(6)','√6'),'math','middle')
  body+=tx(24,292,action+' for input column '+str(k+1))+tx(24,332,'Acceptance requires a nonzero residual perpendicular to all earlier outputs.')
  snap=dict(columnNumber=k+1,phase=action,raw=rows(raw),residual=rows(current),accepted=[rows(u)for u in accepted+([v]if final else[])],coefficient=str(coef)if coef is not None else None)
  symbol='q'if action.startswith('Normalize')else'v'
  formula=symbol+'='+tex(current)+r',\qquad \|'+symbol+r'\|^2='+S.latex((current.T*current)[0])
  why='Divide the nonzero accepted residual by its positive length. The resulting vector has unit length and remains perpendicular to earlier outputs.'if action.startswith('Normalize')else'Acceptance follows after every earlier component is removed and the nonzero residual is checked.'if action.startswith('Accept')else'Each removal uses the exact product and squared length of an earlier perpendicular output.'
  frames.append(frame(snap,svg(body),formula,action,why))
 accepted.append(v)
model('gram','Gram–Schmidt: subtracting every earlier component','gram-schmidt-residual','Coordinate columns show exact three-dimensional states. Orthogonality is certified algebraically; no planar angle is claimed.',frames,['Read an input column','Subtract earlier components','Accept the nonzero perpendicular residual','Divide by its positive length'],'gram')
# QR reconstruction highlights the actual triangular dependency pattern.
Q=S.Matrix([[1,0,0],[0,1,0],[0,0,S.Rational(3,5)],[0,0,S.Rational(4,5)]])
RR=S.Matrix([[1,1,1],[0,1,0],[0,0,5]]);frames=[]
for j in range(3):
 body=tx(24,30,'Reduced QR reconstructs column '+str(j+1))
 for k in range(3):
  left=30+240*k;body+=f'<rect x="{left}" y="90" width="205" height="145" rx="8" fill="#edf2ee" stroke="#a0b3a7"/>'+tx(left+102,122,'Basis contribution '+str(k+1),'prose','middle')
  for a,z in enumerate(Q[:,k]*RR[k,j]):body+=tx(left+102,153+20*a,str(z),'math','middle')
 body+=tx(24,283,'Later basis directions have zero coefficients in earlier input columns.')
 body+=tx(24,328,'R column: '+vstr(RR[:,j]),'math')
 snap=dict(columnNumber=j+1,Q=rows(Q),R=rows(RR),reconstructed=rows(Q*RR[:,j]))
 frames.append(frame(snap,svg(body),r'a_{'+str(j+1)+r'}=Q r_{'+str(j+1)+r'}='+tex(Q*RR[:,j]),'Reconstruct column '+str(j+1),'All three physical contributions sum to the original input column. The zero pattern is triangular.'))
model('qr','Reduced QR: exact column contributions','qr-column-reconstruction','Q is four by three; the diagram shows its actual four-component vectors and triangular coefficient pattern.',frames,['Read a column of R','Scale the columns of Q','Sum to recover the original input column'],'qr')
# Odd/even function projection uses curves rather than a generic state-flow chart.
t=S.symbols('t');frames=[]
for j,poly in enumerate([t**3,S.Integer(0),t**3]):
 body=tx(24,30,'Odd cubic versus an even approximation subspace')
 body+=line((55,195),(410,195),'#b8c8bd')+line((230,82),(230,290),'#b8c8bd')
 for name,f,col in [('target',t**3,'#315d72')]+([('projection'if j==1 else'residual',poly,'#547d51')]if j else[]):
  points=' '.join(str(round(230+150*z,3))+','+str(round(195-80*float(f.subs(t,z)),3))for z in [i/50 for i in range(-50,51)])
  body+='<g data-entity="'+name+'"><polyline points="'+points+'" fill="none" stroke="'+col+'" stroke-width="2"/></g>'
 body+=tx(480,108,'Target: t³','math')+tx(480,151,'Subspace: span(1, t²)','math')+tx(480,194,['Blue: target','Green: zero projection','Green: cubic residual'][j])
 body+=tx(480,238,'Squared error: 2/7','math')+tx(24,329,['Read the odd target','Its even-space projection is zero','The residual is the original cubic'][j])
 frames.append(frame(dict(stage=j,target='t³',projection='0',residual='t³',distanceSquared='2/7'),svg(body),r'\int_{-1}^{1}t^3\,dt=\int_{-1}^{1}t^5\,dt=0',['Target','Zero projection','Residual'][j],'The first and last curves describe target and residual, not a nonzero projected polynomial.'))
model('polynomial','Parity decides the even-space projection','function-parity','A finite polynomial projection is determined by zero odd integrals. This is not an infinite Fourier-convergence illustration.',frames,['Read parity','Check both generator products','Identify projection and residual'],'polynomial')
# Reflection movement rotates the reflecting normal; each frame remains orthogonal.
frames=[];x=S.Matrix([2,0]);cx=250;cy=190
for k in range(9):
 angle=S.pi*k/32;v=S.Matrix([S.cos(angle),S.sin(angle)]);H=S.eye(2)-2*v*v.T;y=S.simplify(H*x)
 body=tx(24,30,'Householder reflection: the normal rotates, length stays fixed')
 body+=line((cx-130,cy),(cx+130,cy),'#bdc9c3')+line((cx,cy-115),(cx,cy+115),'#bdc9c3')
 # Reflector line rotates by the normal angle; the reflected output rotates twice.
 degree=float(angle*180/S.pi)
 body+=f'<g data-entity="reflector" transform="rotate({-degree} {cx} {cy})">'+line((cx,cy-100),(cx,cy+100),'#779782')+'</g>'
 body+=f'<g data-entity="reflected-vector" transform="rotate({-2*degree} {cx} {cy})">'+line((cx,cy),(cx-90,cy),'#547d51',True)+'</g>'
 body+=line((cx,cy),(cx+90,cy),'#315d72',True)+tx(475,105,'Input: (2, 0)','math')+tx(475,151,'Output length: 2','math')+tx(475,195,'Normal angle: '+str(round(degree,3)),'math')+tx(475,239,'det(H) = −1','math')
 body+=tx(24,325,'The output rotates through twice the normal-angle change; it is not a projector.')
 snap=dict(normalAngleDegrees=degree,H=rows(H),input=rows(x),output=rows(y))
 frames.append(frame(snap,svg(body),r'H='+tex(H),'Normal angle '+str(round(degree,3)),'Actual SVG rotations preserve vector length throughout in-flight movement. The endpoint operator remains a reflection.'))
model('reflection','Householder family with norm-preserving motion','householder-normal-rotation','The normal rotates from zero to forty-five degrees; every checkpoint and intermediate motion preserves output length.',frames,['Read the reflecting normal','Rotate the normal','Follow the doubled reflected-vector angle'],'reflection')
# Authentic revisit provenance remains intact, rather than counted as a new unique question.
auth=json.loads((B/'l_linear-authentic.json').read_text())
for z in auth:
 z['title']=z['title'].replace('Explicit linear-map revisit:','Explicit orthogonality revisit:')
 z.pop('additionalModelIds',None)
 z['modelId']='auth-projection'if z['id']=='Phd_CS_1404_Q31'else None
 if z['modelId']is None:z.pop('modelId')
 if z['id']=='MS_CS_1405_Q41':
  z['solution']+=r' Under the Frobenius product, trace is the product with $I$. The trace-zero subspace is its perpendicular complement inside the ten-dimensional symmetric space. Thus exactly one nonzero normal direction is removed. The projector is $X-\operatorname{tr}(X)I/4$, which is distinct from entrywise removal of the whole diagonal.'
 p=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/z['repoPath']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==z['sourceSha256']
save(B/'l_orthogonality-authentic.json',auth)
save(R/'dist/chapters/l_orthogonality-models.json',dict(models=models,groups=groups))
save(E/'model-specs.json',specs)
print(str(len(models))+' models / '+str(sum(len(m['frames'])for m in models))+' exact checkpoints')
