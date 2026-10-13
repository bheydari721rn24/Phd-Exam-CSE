from pathlib import Path
import sys,json,math,copy,html
from itertools import product
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;S={};md=MarkdownIt('commonmark',{'html':True})
def frame(kind,formula,caption,**v):
 return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**v),caption=caption,captionHtml='<p>'+caption+'</p>',formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True).replace('<mo>-</mo>','<mo>−</mo>')+'</div>',line=0,metrics={},teaching=dict(operation=caption,why=caption,currentState=v,initial=False,activeLine=0,changes=[],checks=[],reading='Inspect named pins, exact dimensions and the stated time model. Pending means not yet derived, not an unknown physical voltage.'))
def scene(name,title,description,frames):
 frames[0]['teaching']['initial']=True;S['gates-question-'+name]=dict(id='gates-question-'+name,title=title,description=description,descriptionHtml=mathml.markdown_math(description,md),invariant=description,visual=dict(type='enumeration',claim=description),code=['Establish the netlist and contract; derive intermediate states; compute the requested output and check its scope.'],frames=frames)
def table(name,title,description,headings,rows,formula):
 rendered=[[mathml.render(str(v)[1:],False)if str(v).startswith('$')else html.escape(str(v))for v in r]for r in rows]
 scene(name,title,description,[frame('table',formula,cap,headings=headings,rows=rows,rowsHtml=rendered,stage=i)for i,cap in enumerate(['Read the exact cost or resource model and all column definitions.','Derive the intermediate quantities shown in the complete table.','Compare the requested result with the separate scope and count quantities.'])])
old=json.loads((E/'g_boolean-models.json').read_text())
for name in ['nand','mux']:
 src=copy.deepcopy(old['boolean-question-'+name]);scene(name,src['title'],src['description'],src['frames'])
scene('nand-01','The specified input 01 through the source network','Only the requested x=0,y=1 assignment is evaluated; the difference and borrow pins retain their source connections.',copy.deepcopy(old['boolean-question-nand']['frames'][4:8]))
for n,tau in [(5,5),(5,2),(7,2)]:
 T=2*n*tau;frames=[]
 for k in range(2*n+1):
  time=k*tau;q=[int(((time-i*tau)%T)<n*tau)^(i%2)for i in range(n)]
  frames.append(frame('ring',rf'T=2\cdot{n}\cdot{tau}={T}\,\mathrm{{ns}},\quad f=\frac{{1000}}{{{T}}}\,\mathrm{{MHz}}',f'Established-regime checkpoint at {time} ns; outputs include each stage’s delayed inversion.',n=n,tau=tau,time=time,T=T,q=q))
 scene(f'ring-{n}-{tau}',f'{n}-stage ring with {tau} ns per stage','This is an established ordinary equal-delay regime, not a startup simulation. Outputs satisfy delayed inversion, not simultaneous inversion around a cycle.',frames)
scene('sizing-cases','Resizing can change the maximizing case','Illustrative symbolic cases D1=0.5+4/s and D2=3+1/s are not transistor measurements from the authentic question. Both retain internal contributions while their external contributions divide by s.',[frame('sizing',rf'D_{{\max}}({s})=\max(0.5+4/{s},3+1/{s})',cap,s=s,cases=[[.5,4/s],[3,1/s]],maxCase=0 if .5+4/s>=3+1/s else 1)for s,cap in [(1,'At scale one, case 1 is the maximum: 4.5 versus 4.'),(1.2,'At scale 1.2 both cases equal; this is the crossover.'),(2,'At scale two, case 2 is the maximum: 3.5 versus 2.5.'),(5,'At scale five, the maximum meets target 3.2; all cases are checked.')]])
frames=[]
for x,y in product((0,1),repeat=2):
 t=1-x*y;out=x*y
 frames.extend(frame('positive-and',r't=\neg(xy),\quad F=\neg(tt)=xy',cap,x=x,y=y,t=t,out=out,stage=i)for i,cap in enumerate(['Apply the current two primary inputs.','Evaluate the first NAND on the complete product.','The second NAND receives the first output at both pins and restores positive polarity.']))
scene('positive-and','Two connected NANDs produce positive AND','All four complete valuations use the actual tied-input net. Logical checkpoints are not characterized gate delays.',frames)
frames=[]
for x,y,z in product((0,1),repeat=3):
 u=1-(x|y);v=1-(x|z);w=1-(y|z);out=1-(u|v|w)
 frames.extend(frame('majority',r'F=\neg(\neg(x+y)+\neg(x+z)+\neg(y+z))',cap,x=x,y=y,z=z,u=u,v=v,w=w,out=out,stage=i)for i,cap in enumerate(['Apply the current three-input valuation.','Derive the three complemented pair sums.','The final three-input NOR restores the product of the original sums.']))
scene('majority','Three binary NORs and one ternary NOR','This direct POS construction permits the named three-input final gate. The diagrams trace all eight original valuations.',frames)
for name,rise,old,new in [('hazard-rise',True,2,7),('hazard-fall',False,2,5)]:
 times=sorted(set([-1,0,old,old+1,new,new+1,new+2]));sig=[]
 sig.append([int(t>=0)if rise else int(t<0)for t in times]);sig.append([int(t>=new)if rise else int(t<old)for t in times]);sig.append([int(t<old)if rise else int(t>=new)for t in times]);sig.append([int(not(old+1<=t<new+1))for t in times]);sig.append([1]*len(times))
 scene(name,'Exact rising-input hazard'if rise else'Exact falling-input hazard',f'Stable b=c=1. The old product falls at {old} ns and the new one rises at {new} ns. Equal one-nanosecond transport shifts both output edges by one. A stable bc bridge is compared separately.',[frame('wave',rf'Y=0\quad\mathrm{{on}}\quad[{old+1},{new+1})\,\mathrm{{ns}}',cap,stage=i,times=times,signals=sig,lo=old+1,hi=new+1)for i,cap in enumerate(['Establish the declared primary change.','The old and new products hand off with an uncovered interval.','Translate each OR edge under its stated transport delay.','Compare the bridged output under the same single-input stable context.'])])
scene('arrival','Serial delays and reconvergent arrival','The upper branch takes 3 ns, the lower branch 2+4 ns and the final AND 1 ns. This is the problem’s structural latest-arrival bound.',[frame('arrival',r'L_F=\max(3,2+4)+1=7\,\mathrm{ns}',cap,stage=i)for i,cap in enumerate(['Read the two separate branches and the final gate.','Add the two lower serial delays: their branch arrives at 6 ns.','Compare parallel branch arrivals, then add the final one nanosecond.'])])
table('power','Factor-by-factor dynamic power ratio','The activity convention stays fixed; capacitance does not change. Voltage is squared, while frequency and activity are linear factors.',['factor','new/old','role'],[['activity','$1/2','charging events'],['capacitance','$1','fixed'],['voltage squared','$0.8^2=0.64','quadratic'],['frequency','$2','linear'],['product','$0.64','power ratio']],r'P_1/P_0=(1/2)\cdot1\cdot(0.8)^2\cdot2=0.64')
scene('rc-charge','Threshold crossing on the normalized charge curve','The first-order resistor-capacitor model starts at zero and tends to V. The horizontal axis is t/(RC), so physical time is recovered by multiplication by RC.',[frame('rc',r't/(RC)=-\ln(1-3/4)=\ln4',cap,stage=i,q=.75,cross=math.log(4))for i,cap in enumerate(['Establish the zero initial condition and normalized axis.','Read the rising exponential curve and the requested three-quarter threshold.','Intersect the threshold with the curve at ln(4); this is not a midpoint estimate.'])])
for name,voh,vih,vil,vol in [('noise',4.2,3,.9,.3),('noise-bottleneck',2.4,2,.7,.2)]:
 scene(name,'Driver/receiver guaranteed-level margins','The scale connects receiver acceptance limits with driver guaranteed output limits. The unspecified voltage zone is not a valid third Boolean value.',[frame('noise',rf'NM_H={voh}-{vih}={voh-vih:.1f}\,\mathrm{{V}},\quad NM_L={vil}-{vol}={vil-vol:.1f}\,\mathrm{{V}}',cap,stage=i,voh=voh,vih=vih,vil=vil,vol=vol)for i,cap in enumerate(['Read the driver and receiver guaranteed limits.','Subtract the two low-side limits in receiver-minus-driver order.','Subtract the high-side limits in driver-minus-receiver order; compare both margins.'])])
for n in [5,8]:
 for kind in ['and-tree','mux-tree']:
  rows=[[k,'$'+str(2**(n-k)),'$'+str(2**(n-k)), '$'+str(sum(2**(n-j)for j in range(1,k+1)))]for k in range(1,n+1)]
  table(f'{kind}-{n}',f'Exact {2**n}-input '+('AND reduction'if kind=='and-tree'else'selection tree'),'Each row is a collapsed complete layer, not one depicted cell. Balanced depth and total cell count remain separate.',['layer','outputs','cells at layer','cumulative cells'],rows,rf'G=2^{n}-1={2**n-1},\quad d={n}')
 table(f'nand-and-{n}',f'{n} independent positive AND outputs','Each module contains the two NAND cells shown in the positive-AND model. No inter-module sharing or free complemented input is allowed.',['modules processed','NANDs added','cumulative NANDs'],[[k,'$2','$'+str(2*k)]for k in range(1,n+1)],rf'G=2\cdot{n}={2*n}')
 table(f'xor-chain-{n}',f'{n} serial XOR operations priced in NANDs','There are n+1 leaves and n binary XOR modules. Each module has the source XOR’s four-NAND subnetwork, with no sharing across modules.',['XOR units processed','NANDs per unit','cumulative NANDs'],[[k,'$4','$'+str(4*k)]for k in range(1,n+1)],rf'G=4\cdot{n}={4*n}')
 rows=[[k,'$'+str(2*k),'$'+str(2*k+3)]for k in range(n)]
 table(f'ripple-{n}',f'{n}-bit carry and sum arrival comparison','Row k is the sum block fed by carry Ck. The table gives arrival times, not logical carry bits. Cn is a separate final output.',['sum index k','L(Ck)','L(Sk)'],rows+[['final carry','$'+str(2*n),'not a sum']],rf'L_{{S_{{{n-1}}}}}=2({n}-1)+3={2*n+1},\quad L_{{C_{{{n}}}}}={2*n}')
 table(f'scaling-{n}',f'Internal/external delay at width scale {n}','The specified internal contribution stays one; the fixed external-load contribution divides by the width scale. This model does not scale the next stage.',['component','initial','after sizing'],[['internal','$1','$1'],['fixed load','$1',rf'$\frac{{1}}{{{n}}}'],['total','$2',rf'$\frac{{{n+1}}}{{{n}}}']],rf'D({n})=1+1/{n}=\frac{{{n+1}}}{{{n}}}')
 table(f'consensus-{n}',f'Literal occurrences in {n} independent bridged outputs','Every output uses ab + not-a c + bc. The three two-literal terms have six occurrences, regardless of how physical cells are subsequently mapped.',['outputs processed','literals per output','total occurrences'],[[k,'$6','$'+str(6*k)]for k in range(1,n+1)],rf'\ell=6\cdot{n}={6*n}')
frames=[]
for x,y in product((0,1),repeat=2):
 frames.extend(frame('cmos',r'D=xy,\quad U=(\neg x)+(\neg y)=\neg D',cap,x=x,y=y,down=x*y,up=1-x*y,out=1-x*y,stage=i)for i,cap in enumerate(['Apply stable ideal-switch inputs.','Determine the series nMOS and parallel pMOS conduction predicates.','Exactly one network connects the output to a supply; the resulting function is NAND.']))
scene('cmos','Connected complementary two-input CMOS NAND','Source/drain switch channels are drawn explicitly. The nMOS branch is series and the pMOS branches parallel. This is a stable ideal-switch model, not transistor waveforms or leakage certification.',frames)
frames=[]
for bits in product((0,1),repeat=3):
 d=math.prod(bits)
 frames.extend(frame('cmos',r'D=xyz,\quad U=(\neg x)+(\neg y)+(\neg z)=\neg D',cap,inputs=list(bits),down=d,up=1-d,out=1-d,stage=i)for i,cap in enumerate(['Read the source question’s three-input NAND topology.','Determine series nMOS and parallel pMOS conduction for this stable assignment.','Identify the guaranteed ideal output; sizing affects RC parameters, not this Boolean function.']))
scene('cmos-3','Three-input NAND topology from the sizing question','All eight stable valuations use three series nMOS and three parallel pMOS switches. Widths and capacitances are not numerically supplied, so no physical delay measurement is invented.',frames)
(E/'g_gates-models.json').write_text(json.dumps(S,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');p=R/'dist/chapters/concept-animations.json';all=json.loads(p.read_text());all['scenes'].update(S);p.write_text(json.dumps(all,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8');print({'models':len(S),'frames':sum(len(v['frames'])for v in S.values())})
