from pathlib import Path
from fractions import Fraction as F
import copy,json,sys
B=Path(__file__).parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
def tex(x):
 x=F(x);return str(x.numerator) if x.denominator==1 else ('-' if x<0 else '')+rf'\frac{{{abs(x.numerator)}}}{{{x.denominator}}}'
def vec(v):return '('+','.join(map(tex,v))+')'
def frame(snapshot,formula,caption):return dict(nodes=[],edges=[],snapshot=copy.deepcopy(snapshot),caption=caption,captionHtml='<p>'+caption+'</p>',metrics={},formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True)+'</div>',line=0,teaching=dict(operation='Follow the declared exact geometric or algebraic operation',why=caption,currentState=copy.deepcopy(snapshot),initial=False,activeLine=0,changes=[],checks=[],reading='Blue is the given input; green is the verified construction. The source-formula comparison uses purple. Geometry uses equal coordinate scales where a spatial plane is shown. An algebraic board or objective plot is explicitly labeled as such. Transit is between exact checkpoints, not a new exact theorem.'))
def scene(id,title,description,frames):
 frames[0]['teaching']['initial']=True
 return dict(id='vectors-question-'+id,title=title,description=description,descriptionHtml='<p>'+description+'</p>',invariant='Every checkpoint uses the displayed source hypothesis, exact arithmetic and named geometry. A literal source ambiguity is distinguished from an added normalized interpretation.',visual=dict(type='enumeration',claim=description),code=['State the geometry; construct the candidate; verify the exact defining conditions'],frames=frames)
models={};frames=[]
for scale,x in [(F(1),[1,1]),(F(2),[1,1]),(F(2),[0,1]),(F(1,2),[1,1])]:
 source=[scale*scale*x[0],F(0)];foot=[F(x[0]),F(0)];state=dict(kind='source',scale=float(scale),x=x,source=list(map(float,source)),foot=list(map(float,foot)),idempotent=scale==1)
 formula=rf'P_s=\operatorname{{diag}}({tex(scale*scale)},0),\quad P_sx={vec(source)},\quad P_Ux={vec(foot)}'
 plain=lambda v:'('+', '.join(map(str,v))+')'
 frames.append(frame(state,formula,f'Use generator u=({scale},0), so the source sum multiplies the first coordinate by {scale*scale}. Input x={plain(x)}. The purple ring marks source output {plain(source)}, whereas dividing by the squared generator norm gives actual foot {plain(foot)}. '+('Unit normalization makes the two maps agree and gives idempotence.' if scale==1 else 'The nonunit source map is not idempotent. The displayed operator is not silently called an orthogonal projection.')))
models['source']=scene('source','Question 3: literal source sum versus normalized projection','The target subspace is the x-axis. Four exact cases distinguish a unit basis, a nonunit basis and a perpendicular input. Green uses the denominator required for true projection; purple uses the literal source formula.',frames)
frames=[]
for a in [F(-3,4),F(-1,2),F(-1,4),F(0),F(3,4),F(1),F(5,4)]:
 l=1+2*a;t=1-a;state=dict(kind='positivity',a=str(a),parallel=float(l),perpendicular=float(t),valid=l>0 and t>0)
 frames.append(frame(state,rf"a={tex(a)},\quad\lambda_{{\text{{line}}}}={tex(l)},\quad\lambda_{{\text{{plane}}}}={tex(t)}",f"Parameter a={a}. Unit all-equal coefficient {l}; sum-zero coefficient {t}. "+("Both positive: strict positive definiteness." if l>0 and t>0 else "A zero coefficient gives a nonzero null direction: semidefinite boundary, not strict positivity." if l==0 or t==0 else "A negative coefficient supplies a direction disproving positive definiteness.")))
models['positivity']=scene('positivity','Question 4: exact positivity boundaries','Bar heights share the same signed coefficient scale. A horizontal zero marker denotes a zero coefficient. The all-equal component is normalized; its coefficient is 1+2a, while the sum-zero plane coefficient is 1-a.',frames)
for num,u,v,w,rhs,c,r in [(37,[1,0,1],[1,1,0],[1,2,3],[4,3],[F(5,3),F(2,3)],[F(-4,3),F(4,3),F(4,3)]),(45,[1,1,0],[1,0,1],[0,1,1],[1,1],[F(1,3),F(1,3)],[F(-2,3),F(2,3),F(2,3)])]:
 frames=[];p=[c[0]*u[i]+c[1]*v[i] for i in range(3)];system=rf'\begin{{pmatrix}}2&1\\1&2\end{{pmatrix}}\begin{{pmatrix}}c_1\\c_2\end{{pmatrix}}=\begin{{pmatrix}}{rhs[0]}\\{rhs[1]}\end{{pmatrix}}'
 steps=[rf'G=B^TB,\quad B^Tw={vec(rhs)}',rf'3c_1={2*rhs[0]-rhs[1]}',rf'c_1={tex(c[0])},\quad c_2={tex(c[1])}',rf'p=c_1u+c_2v={vec(p)}',rf'r=w-p={vec(r)}',r'u^Tr=v^Tr=0']
 captions=['Compute every generator dot product; the off-diagonal one couples the coefficients.','Twice the first equation minus the second eliminates c2.','Solve the remaining scalar equation and substitute into the second equation.','Reconstruct the actual vector from both generators.','Subtract from the original target to obtain the full residual.','Verify both residual inner products are zero and the foot belongs to the span; these certify the unique nearest point.']
 for stage,(formula,caption) in enumerate(zip(steps,captions)):
  state=dict(kind='gram',stage=stage,question=num,inputMath=[mathml.render(vec(x)) for x in [u,v,w]],systemMath=mathml.render(system,True),coefficients=[str(q) for q in c],foot=[str(q) for q in p],residual=[str(q) for q in r],rhs=rhs)
  frames.append(frame(state,formula,caption))
 models['gram'+str(num)]=scene('gram'+str(num),f'Question {num}: coupled Gram construction','An algebraic board shows the exact three-dimensional input vectors and coupled two-coefficient system. It is not a two-dimensional spatial projection of 3D coordinates; the final vector and residual are verified algebraically.',frames)
frames=[]
for c in [[0,0],[1,0],[2,0],[2,1]]:
 state=dict(kind='coordinates',c=c,partial=[c[0]+c[1],c[0]-c[1]],target=[3,1])
 frames.append(frame(state,rf'q={c[0]}b_1+{c[1]}b_2={vec(state["partial"])},\quad\Vert q\Vert^2={2*(c[0]**2+c[1]**2)}',f'Current basis coefficients are {c}. Add {c[0]} copies of b1=(1,1), then {c[1]} copies of b2=(1,-1), head to tail. The partial vector is {state["partial"]}; the fixed target is (3,1). The final coordinates (2,1) have physical squared norm ten because the basis Gram matrix is 2I.'))
models['coordinates']=scene('coordinates','Question 41: coordinates and physical geometry','Both plot axes use one common unit scale. The second component begins at the first component endpoint. The amber fixed target is reached only at the final coefficient pair; coordinate-square sum differs from physical squared norm.',frames)
frames=[]
for y in [F(0),F(1,6),F(1,3),F(1,2),F(2,3),F(5,6),F(1),F(4,3)]:
 f=2*(1-y)**2+y*y;state=dict(kind='minimum',y=float(y),value=float(f),vector=[str(1-y),str(y),str(1-y)],minimum=F(y)==F(2,3))
 frames.append(frame(state,rf'y={tex(y)},\quad F(y)={tex(f)},\quad x={vec([1-y,y,1-y])}',f'Feasible candidate (1-y,y,1-y) at y={y}. Its exact squared norm is {f}. The curve is F(y)=3(y-2/3)^2+2/3, and the moving point is this objective value, not a spatial drawing of the 3D vector. '+('The square vanishes and the unique minimum 2/3 is attained.' if y==F(2,3) else 'The nonnegative extra square explains its excess above the exact minimum.')))
models['minimum']=scene('minimum','Question 46: a feasible line and its exact objective','The horizontal axis is the scalar parameter y; the vertical axis is squared norm F(y). A stable candidate point moves along the verified parabola. Every checkpoint also names the corresponding feasible 3D vector.',frames)
frames=[]
rows=[([1,1],[1,1],[],r'w_1=v_1=(1,1)','Read the first input; there is no retained basis yet.'),([1,1],[1,1],[[2**-.5,2**-.5]],r'q_1=\frac{(1,1)}{\sqrt2}','Normalize the nonzero residual and retain the first unit direction.'),([2,2],[2,2],[[2**-.5,2**-.5]],r'v_2=2v_1','Read the second input; it already belongs to the retained span.'),([2,2],[0,0],[[2**-.5,2**-.5]],r'w_2=v_2-\langle q_1,v_2\rangle q_1=0','Subtract its complete projection. Skip the zero residual instead of dividing by zero.'),([0,0],[0,0],[[2**-.5,2**-.5]],r'w_3=0','The explicit zero input is also skipped. Skipping does not terminate the algorithm.'),([1,-1],[1,-1],[[2**-.5,2**-.5]],r'\langle q_1,v_4\rangle=0','The fourth input is perpendicular to the retained direction and remains nonzero.'),([1,-1],[1,-1],[[2**-.5,2**-.5],[2**-.5,-2**-.5]],r'q_2=\frac{(1,-1)}{\sqrt2}','Normalize and retain the second direction; both have unit norm and zero cross product.'),([1,-1],[1,-1],[[2**-.5,2**-.5],[2**-.5,-2**-.5]],r'Q^TQ=I_2','The final two vectors are an orthonormal basis for all four inputs. Two redundant inputs were skipped.')]
for i,(v,w,q,formula,caption) in enumerate(rows):frames.append(frame(dict(kind='orthogonalize',stage=i,input=v,residual=w,basis=q,inputIndex=0 if i<2 else 1 if i<4 else 2 if i==4 else 3),formula,caption))
models['gram-schmidt']=scene('gram-schmidt','Tutorial 22: Gram–Schmidt with dependent and zero inputs','Four real planar inputs are processed in order. Each checkpoint shows the current input, residual and retained unit directions. A zero residual is skipped; later independent input still adds a direction.',frames)
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text());d['scenes'].update({s['id']:s for s in models.values()})
for f in d['scenes']['projection']['frames']:
 for k,v in list(f.get('metrics',{}).items()):
  if isinstance(v,str) and 'Fraction(' in v:
   import re
   v=re.sub(r'Fraction\(([-\d]+), (\d+)\)',r'\1/\2',v);f['metrics'][k]=v
   if f.get('teaching',{}).get('currentState',{}).get('counters'):f['teaching']['currentState']['counters'][k]=v
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print({k:len(v['frames']) for k,v in models.items()})
