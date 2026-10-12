from pathlib import Path
from fractions import Fraction as F
import copy,json,sys
B=Path(__file__).parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
original_render=mathml.render
mathml.render=lambda *args,**kwargs:original_render(*args,**kwargs).replace('<mo>-</mo>','<mo>−</mo>')
def matrix(a):return r'\begin{pmatrix}'+(chr(92)*2).join('&'.join(map(str,row)) for row in a)+r'\end{pmatrix}'
def state(kind,formula,caption,**s):return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**s),caption=caption,captionHtml='<p>'+caption+'</p>',metrics={},formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True)+'</div>',line=0,teaching=dict(operation=caption.split('.')[0],why=caption,currentState=dict(kind=kind,**s),initial=False,activeLine=0,changes=[],checks=[],reading='This model uses the named matrices, dimensions, actual operation and exact checkpoints. Native formulas explain the arithmetic. A coordinate-plane plot has equal axis scales. An algebraic board is explicitly labeled; it does not pretend to be a spatial picture of a higher-dimensional vector.'))
def scene(name,title,description,frames):
 frames[0]['teaching']['initial']=True
 return dict(id='matrices-question-'+name,title=title,description=description,descriptionHtml='<p>'+description+'</p>',invariant=description,visual=dict(type='enumeration',claim=description),code=['Construct the actual operation; verify dimensions and the stated defining identities'],frames=frames)
sc={}
frames=[]
for stage in range(4):
 formulas=[r'J=qq^T,\quad Jq=5q',r'\sum_i z_i=0\ \Rightarrow\ Jz=0',r'(I+J)q=6q,\quad (I+J)z=z',r'\det(I+J)=6\cdot1^4=6']
 captions=['The all-ones matrix reads the coordinate sum and repeats that sum into every output coordinate.','The displayed sum-zero input is (1,-1,0,0,0); J annihilates it.','Adding identity keeps the sum-zero directions and increases the all-equal scale by one.','In an adapted basis the actual five diagonal scales are 6,1,1,1,1; multiply these, not the original displayed diagonal.']
 frames.append(state('allones',formulas[stage],captions[stage],stage=stage,n=5,scales=[6,1,1,1,1],leftMath=mathml.render(matrix([[1]*5 for _ in range(5)]),True),rightMath=mathml.render(matrix([[6 if i==j==0 else 1 if i==j else 0 for j in range(5)] for i in range(5)]),True)))
sc['allones']=scene('allones','Question 6: all-ones action and adapted diagonal scales','An algebraic board uses the actual size-five all-ones map, its all-equal line and its four-dimensional sum-zero complement. It is not a spatial five-dimensional picture.',frames)
frames=[]
for stage,point in enumerate([[1,1],[6,1],[1,1]]):
 f=[r'x=(1,1),\quad S=\begin{pmatrix}1&5\\0&1\end{pmatrix}',r'Sx=(6,1)',r'S^{-1}Sx=(1,1),\quad S^{-1}=\begin{pmatrix}1&-5\\0&1\end{pmatrix}'][stage]
 frames.append(state('shear',f,['Read the input before applying the size-five shear.','Shear adds five times the unchanged vertical coordinate to the horizontal coordinate.','The inverse subtracts exactly that contribution and restores the input.'][stage],stage=stage,point=point,n=5))
sc['shear']=scene('shear','Question 10: forward shear and its inverse','Actual parameter five maps (1,1) to (6,1), then back to (1,1). The grid and unit-square image use equal coordinate scales; the area stays one.',frames)
frames=[]
for row in range(6):
 p=[(j+1)%5 for j in range(5)] if row<5 else list(range(5));P=[[int(i==p[j]) for j in range(5)] for i in range(5)];DP=[[(i+1)*P[i][j] for j in range(5)] for i in range(5)];trace=sum(DP[i][i] for i in range(5))
 frames.append(state('fixed',rf'\operatorname{{tr}}(DP)=\sum_{{i=1}}^5 iP_{{ii}}={trace}',f'Inspect diagonal coordinate {row+1}.' if row<5 else 'Counterexample variant: identity permutation fixes all five coordinates, changing the weighted trace from zero to 15.',row=row,P=P,DP=DP,trace=trace,leftMath=mathml.render(matrix(P),True),rightMath=mathml.render(matrix(DP),True)))
sc['fixed']=scene('fixed','Question 14: weighted fixed-coordinate trace','The exact size-five permutation and its weighted product are shown. The first five checkpoints verify zero diagonal terms; the final deliberately changed identity permutation demonstrates the missing-hypothesis failure.',frames)
for exponent in [5,10]:
 frames=[]
 for k in range(exponent+1):
  value=k*(k-1)//2;M=[[1,k,value],[0,1,k],[0,0,1]]
  frames.append(state('power',rf'(I+N)^{{{k}}}=I+{k}N+{value}N^2,\quad t_{{{k}}}={value}',f'At power {k}, choose two distinct chronological N slots. There are {value} pairs. '+('No two-step contribution exists yet.' if k<2 else f'The newest slot adds {k-1} pairs to the previous count.'),k=k,value=value,matrixMath=mathml.render(matrix(M),True)))
 name='power' if exponent==5 else 'power10';sc[name]=scene(name,f'Nilpotent power through exponent {exponent}','The coordinate chain is 3 to 2 to 1. A triangular pair diagram enumerates distinct slot pairs i<j; its count is the exact upper-right coefficient, not a squared one-step count.',frames)
U=[[1,0],[0,1],[0,0],[0,0],[0,0]];V=[[0,0,1,0,0],[0,0,0,1,0]];UV=[[0]*5 for _ in range(5)];UV[0][2]=UV[1][3]=1
frames=[]
for stage,f in enumerate([r'V:\mathbb R^5\to\mathbb R^2\ \text{is onto}',r'U:\mathbb R^2\to\mathbb R^5\ \text{is injective}',r'\operatorname{rank}(UV)=2,\quad\dim\ker(UV)=3',r'(UV)^2=0,\quad VU=0_{2\times2}']):
 frames.append(state('rank',f,['V reads the third and fourth coordinates, reaching all two-coordinate outputs.','U embeds those two values into the first two coordinates without loss.','The complete five-coordinate output is (x3,x4,0,0,0); its image has dimension two.','Reverse composition reads zeros from an embedded output. A second forward product also vanishes, although the first product has rank two.'][stage],stage=stage,n=5,leftMath=mathml.render(matrix(U),True),rightMath=mathml.render(matrix(V),True),productMath=mathml.render(matrix(UV),True)))
sc['rank']=scene('rank','Question 26: full-rank rectangular composition','A typed map chain and the actual size-five embedding/reader show why UV has rank two, while VU can be zero. Native matrices and named spaces replace a misleading spatial five-dimensional drawing.',frames)
frames=[]
for stage,(point,formula) in enumerate([([1,-1],r'b_2=(1,-1)'),([2,-5],r'Tb_2=(2,-5)'),([2,-5],r'c_1+c_2=2,\quad c_1-c_2=-5'),([2,-5],r'c_1=-\frac32,\quad c_2=\frac72')]):
 frames.append(state('basis',formula,['Read the actual second basis vector in standard coordinates.','The diagonal map scales the horizontal coordinate by two and the vertical by five.','Solve the coordinate reconstruction equations; the image is not yet a basis-coordinate list.','Reconstruction -3/2 b1 + 7/2 b2 equals (2,-5); this verifies the requested new-matrix entry.'][stage],stage=stage,point=point))
sc['basis']=scene('basis','Question 30: actual image, then basis coefficients','Equal-scale plane geometry tracks b2 and its transformed image. The algebraic reconstruction yields the first-row second-column entry -3/2 and explicitly distinguishes physical coordinates from basis coefficients.',frames)
for name,lower in [('block',2),('blockidentity',1)]:
 frames=[]
 for stage in range(4):
  formula=[rf'M=\begin{{pmatrix}}I_5&2I_5\\0&{lower}I_5\end{{pmatrix}}',rf'(x,y)\mapsto(x+2y,{lower}y)',rf'y=\frac{{v}}{{{lower}}},\quad x=u-2y',rf'M^{{-1}}=\begin{{pmatrix}}I_5&-\frac{{2}}{{{lower}}}I_5\\0&\frac{{1}}{{{lower}}}I_5\end{{pmatrix}}'][stage]
  frames.append(state('block',formula,['Declare both five-coordinate blocks and choose coupling 2I5 as one valid actual matrix.','For the sample x=e1,y=e1, the forward map gives u=3e1 and v equal to the displayed lower scaling.','Recover the lower input first; then subtract its coupling from the upper output.','Both ordered products give identity. The upper-right inverse coupling includes the undoing of the lower diagonal action.'][stage],stage=stage,lower=lower,n=5,det=lower**5))
 sc[name]=scene(name,'Block map and its ordered inverse: lower scale '+str(lower),'Two five-coordinate groups remain distinct. The sample x=y=e1 gives explicit forward and backward values, while the formulas prove the full inverse for all inputs. Coupling needs no separate inverse.',frames)
frames=[]
AA=[[1,1],[0,0]];G=[[1,1],[1,1]]
for x in [[1,0],[0,1],[1,-1],[2,-2]]:
 out=[x[0]+x[1],0];norm=out[0]**2;frames.append(state('gram',rf'x={tuple(x)},\quad Ax={tuple(out)},\quad x^TA^TAx={norm}',f'Input {tuple(x)} maps to {tuple(out)}. Its squared output length is {norm}. Zero output is equivalent to zero Gram action for this real matrix.',x=x,out=out,norm=norm,leftMath=mathml.render(matrix(AA),True),rightMath=mathml.render(matrix(G),True)))
sc['gram']=scene('gram','Question 42: real Gram kernel and a lost direction','The actual rank-one real matrix sends (x1,x2) to (x1+x2,0). Equal-scale input/output geometry and its exact Gram matrix show the nonnegative squared-norm identity and kernel direction.',frames)
A=[[1,2,0],[0,-1,3]];BT=[[2,1,-2],[0,4,1]];terms=[[A[i][j]*BT[i][j] for j in range(3)] for i in range(2)]
frames=[]
for stage in range(3):
 formula=[r'\operatorname{tr}(AB)=(2+2+0)+(0-4+3)=3',r'\operatorname{tr}(BA)=(2+0)+(2-4)+(0+3)=3',r'AB=\begin{pmatrix}4&8\\-7&-1\end{pmatrix},\quad\operatorname{tr}(AB)=3'][stage]
 frames.append(state('trace',formula,['Group the same six entry products by the two A rows.','Regroup those identical products by the three B rows; no product is added or lost.','Check the concrete two-by-two product. Trace equality does not assert equality with the three-by-three reverse product.'][stage],stage=stage,terms=terms))
sc['trace']=scene('trace','Question 44: six products, two trace groupings','A rectangular two-by-three/three-by-two example uses the actual same six scalar pair products. Row and column regrouping proves trace equality; the bank also supplies the identity/embedding determinant counterexample.',frames)
for d in [3,4]:
 frames=[]
 for a in [-F(1,2),-F(1,d-1),F(0),F(1,2),F(1)]:
  line=1+(d-1)*a;other=1-a
  frames.append(state('positivity',rf'a={a},\quad\lambda_{{\text{{line}}}}={line},\quad\lambda_{{\text{{sum-zero}}}}={other}',f'Dimension {d}: the all-equal coefficient is {line}; the sum-zero coefficient is {other}. Strict positivity requires both positive. A zero coefficient exposes a nonzero null subspace.',a=str(a),dimension=d,parallel=float(line),perpendicular=float(other),valid=line>0 and other>0))
 sc['positivity'+str(d)]=scene('positivity'+str(d),f'Structured positivity in dimension {d}','Signed coefficients of two orthogonal subspaces are tested separately. A coefficient-zero boundary is semidefinite, not strictly definite. This is a coefficient plot, not a spatial depiction of the full vector space.',frames)
p=R/'dist/chapters/concept-animations.json';data=json.loads(p.read_text());source=copy.deepcopy(data['scenes']['vectors-question-source']);source.update(id='matrices-question-source',title='Original PhD Q31: literal source sum and normalized projection');sc['source']=source;data['scenes'].update({s['id']:s for s in sc.values()});p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print({k:len(v['frames']) for k,v in sc.items()})
