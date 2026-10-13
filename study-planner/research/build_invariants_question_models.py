"""Build exact transition traces, mass trees and constructor/count models."""
from pathlib import Path
import json, sys, html, math
from fractions import Fraction
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True});S={}
def native(s):return mathml.render(str(s),False)
def prose(s):return mathml.markdown_math(s,md).strip().removeprefix('<p>').removesuffix('</p>')
def frame(kind,formula,caption,why,**data):
 formula=formula.replace('flatAcc(',r'\operatorname{flatAcc}(').replace('flatten(',r'\operatorname{flatten}(')
 return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**data),caption=caption,captionMathHtml=prose(caption),formula=formula,formulaHtml=mathml.render(formula,True).replace('<mo>‖</mo>','<mo stretchy="false">‖</mo>'),metrics={},line=0,teaching=dict(operation=caption,operationHtml=prose(caption),why=why,whyHtml=prose(why),currentState=data,changes=[],checks=[],initial=False,activeLine=0))
def scene(name,title,description,frames,guide):
 id='invariants-question-'+name
 for i,f in enumerate(frames):
  t=f['teaching'];t.update(initial=i==0,activeLine=0 if i==0 else 2 if i==len(frames)-1 else 1,guide=guide)
  f['line']=t['activeLine']
  if i:
   old=frames[i-1]['teaching']['currentState'];new=t['currentState'];t['changes']=[dict(field=k,before=old.get(k),after=v) for k,v in new.items()if old.get(k)!=v]
 s=dict(id=id,title=title,description=description,descriptionHtml='<p>'+prose(description)+'</p>',invariant=description,visual=dict(type='enumeration',claim=description),code=guide,frames=frames,useAuthoredTeachingChanges=True)
 if len(frames)>12:s['printFrameIndices']=[0,1,len(frames)//2,len(frames)-1]
 S[id]=s
def rowsframe(headings,rows,formula,caption,why,active=-1):
 visible=rows[-7:]
 import re
 cell=lambda v:native(v[1:])if str(v).startswith('$')else native(v)if re.fullmatch(r'[-0-9, ]+',str(v))else html.escape(str(v))
 f=frame('table',formula,caption,why,headings=headings,rows=rows,rowsHtml=[[cell(v)for v in row]for row in visible],active=len(visible)-1)
 f['teaching']['currentState']={'Displayed checkpoint':len(rows)-1}
 return f
def trace(name,title,description,headings,rows,formula,why):
 scene(name,title,description,[rowsframe(headings,rows[:i+1],formula,'Inspect checkpoint '+str(i)+' and the actual old-to-new values.',why,i)for i in range(len(rows))],['Read the initial state and the permitted update.','Calculate the next state using old values.','Use the exact final condition and count the displayed transitions.'])
def state_scene(name,title,nodes,edges,sets,formula,description):
 scene(name,title,description,[frame('state-graph',formula,cap,why,nodes=nodes,edges=edges,highlight=selected,unsafe=unsafe)for cap,why,selected,unsafe in sets],['Identify the initial and candidate states.','Follow only actual directed edges or apply the declared closure step.','Separate a reachable witness from a failing proposed certificate.'])
state_scene('true-not-closed','Reachable safety versus inductive closure',list(range(4)),[[0,1],[2,3]],[('The initial state is zero.','Initialization checks only membership of the initial state.',[0],[]),('Reachable states are zero and one.','The second edge has an unreachable source; it is not an execution from zero.',[0,1],[]),('The candidate also contains state two.','Its edge to excluded three violates global preservation, even though actual reachable safety holds.',[0,1,2],[3]),('Strengthen the certificate to zero and one.','The only outgoing edge of this smaller initialized set stays inside it.',[0,1],[])],r'R=\{0,1\},\quad P=\{0,1,2\}', 'Every displayed edge is the stated transition. Green and red identify the current certificate and excluded destination, not a change to reachability.')
nodes=list(range(6));edges=[[0,1],[1,2],[2,3],[4,2],[5,5]]
layers=[([0],'Initial forward layer'),([0,1],'First forward successor'),([0,1,2],'Second forward successor'),([0,1,2,3],'The reachable set stabilizes')]
state_scene('forward-six','Exact forward reachability and shortest unsafe path',nodes,edges,[(cap,'Follow the chain from zero; neither four nor five has a reachable predecessor.',selected,[3]if 3 in selected else[])for selected,cap in layers],r'R=\{0,1,2,3\}', 'This is the six-state graph of Challenge 1. The self-loop at five is unreachable from zero.')
state_scene('backward-six','Greatest safe closure by backward deletion',nodes,edges,[(cap,'Remove any current state with an outgoing edge leaving the current safe candidate.',selected,[x for x in nodes if x not in selected])for selected,cap in [([0,1,2,4,5],'Start from the permitted region'),([0,1,4,5],'Delete two, whose successor is unsafe'),([0,5],'Delete one and four'),([5],'Delete zero; safe closure stabilizes')]],r'K=\{5\}', 'Backward deletion computes universal safety inside the given region; it does not compute forward reachability.')

def mass(name,title,nodes,edges):
 leaves=[v for v,d in nodes if not any(e[0]==v for e in edges)];weights={v:Fraction(1,2**d)for v,d in nodes};total=sum(weights[v]for v in leaves)
 fs=[]
 for k in range(len(leaves)+1):
  processed=leaves[:k];subtotal=sum((weights[v]for v in processed),Fraction())
  value=str(subtotal.numerator)if subtotal.denominator==1 else rf'\frac{{{subtotal.numerator}}}{{{subtotal.denominator}}}'
  caption='No leaf allocation has been collected yet.'if k==0 else 'Include leaf $'+str(leaves[k-1])+'$; the displayed sum now includes exactly '+str(k)+' leaves.'
  f=frame('mass-tree',r'\alpha='+value,caption, 'Each displayed leaf has its exact depth weight. Missing children discard mass rather than creating new leaf allocations.',nodes=nodes,edges=edges,leaves=leaves,selected=processed,weights={str(v):str(weights[v])for v in leaves},fullSum=str(total));f['teaching']['currentState']={'Collected leaves':k,'Uncollected leaves':len(leaves)-k};fs.append(f)
 scene(name,title,'The drawing specifies every vertex and child of this finite tree; root depth is zero. Leaf labels show exact rational allocations.',fs,['Give the root unit mass.','Halve along each actual child edge.','Sum actual leaves and identify missing-child loss.'])
mass('mass-full','Full binary tree: all root mass reaches its leaves',[(0,0),(1,1),(2,1),(3,2),(4,2)],[[0,1],[0,2],[2,3],[2,4]])
mass('mass-unary','A unary root loses half its mass',[(0,0),(1,1)],[[0,1]])
mass('mass-irregular','Exact missing-child deficit in the irregular tree',[(0,0),(1,1),(2,1),(3,2),(4,3),(5,3)],[[0,1],[0,2],[2,3],[3,4],[3,5]])

for n in[5,8]:
 trace('weighted-'+str(n),'A conserved weighted sum and a decreasing counter',f'The actual numerical input is n={n}. Every row is one complete loop-head state.', ['step','first counter','second counter','conserved value','remaining steps'],[[f'${t}',f'${n-t}',f'${n+1+2*t}',f'${3*n+1}',f'${n-t}']for t in range(n+1)],rf'2a+b=3({n})+1={3*n+1}', 'The first counter loses one and the second gains two. The weighted sum stays constant, while the natural first counter counts remaining work.')
 a,b=30*n,18*n;rr=[];t=0
 while True:
  rr.append([f'${t}',f'${a}',f'${b}',f'${math.gcd(a,b)}'])
  if b==0:break
  a,b=b,a%b;t+=1
 trace('euclid-'+str(n),'Euclidean states preserve divisors and lower the remainder','Rows are simultaneous old-to-new remainder transitions; the stopped second coordinate is zero.', ['step','first argument','second argument','preserved gcd'],rr,rf'\gcd(a,b)=6({n})={6*n}', 'The gcd remains unchanged. Only the new remainder, rather than both arguments, is guaranteed smaller than the old second argument.')
 x=y=n;rr=[];t=0
 while True:
  rr.append([f'${t}',f'${x}',f'${y}',f'${(n+1)*x+y}'])
  if x==y==0:break
  if x:x-=1;y+=n
  else:y-=1
  t+=1
 trace('two-counter-'+str(n),'Prepaid future work in a two-phase transition',f'This is the full n={n} execution, not a normalized growing or shrinking bar.', ['step','primary','secondary','remaining exact rank'],rr,rf'\rho=({n}+1)x+y,\quad T={t}', 'Each primary step creates n secondary steps; its weight pays for those and itself. The displayed rank loses exactly one at both kinds of transition.')
 s=0;rr=[]
 for t in range(n+1):
  rr.append([f'${t}',f'${t+2}',f'${s}',f'${n-t}'])
  s+=t+2
 trace('arithmetic-'+str(n),'Addition then increment: exact loop-head checkpoints',f'Initial index is two, and exactly {n} body executions are permitted.', ['completed bodies','next old index','accumulated sum','remaining bodies'],rr,rf's=\frac{{t(t+3)}}2,\quad s_{{final}}={n*(n+3)//2}', 'The current index has not yet been added at the loop head. Reversing assignment order shifts every accumulated term.')
 trace('ternary-'+str(n),'Ternary recursion: levels, leaves and total calls',f'All three-child call-tree leaves have depth {n}. Rows aggregate actual complete levels; individual thousands of calls are not drawn.', ['depth','calls on level','cumulative calls'],[[f'${k}',f'${3**k}',f'${(3**(k+1)-1)//2}']for k in range(n+1)],rf'C=\frac{{3^{{{n}+1}}-1}}2={(3**(n+1)-1)//2}', 'One root call produces three children per nonbase call. A level count and a cumulative count measure different objects; stack depth is only one active branch.')
 trace('mixed-'+str(n),'Mixed parent arities determine edges and leaves','This is aggregate accounting for the stated tree counts; it does not assert a unique tree shape or height.', ['vertex type','vertices','children each','edge contribution'],[['binary',f'${n}','$2',f'${2*n}'],['ternary',f'${n}','$3',f'${3*n}'],['leaf',f'${3*n+1}','$0','$0']],rf'E=5({n})={5*n},\quad L=3({n})+1={3*n+1}', 'Sum actual parent outdegrees for the edge count, then subtract internal vertices and use the root correction in the tree identity.')
 trace('period-'+str(n),'Full parity periods and the two-entry boundary','The cycle is specified to begin odd, odd, even at index one. Every row accounts for a complete block or the final fragment.', ['block','index range','odd terms','running odd count'],[[str(k),f'${3*k-2},{3*k}', '$2',f'${2*k}']for k in range(1,n)]+[['last fragment',f'${3*n-2},{3*n-1}','$2',f'${2*n}']],rf'N_{{odd}}=2({n})={2*n}', 'The final two entries are both odd and must be counted. This block calculation relies on the established phase, not on an assumed equal parity split.')
 trace('affine-'+str(n),'Affine difference: growth and an actual conserved ratio','The root input is fixed. Four exact updates show the raw difference changing, while the ratio stays constant.', ['step','first value','second value','difference','conserved ratio'],[[f'${t}',f'${(n+1)*2**t-1}',f'${2**t}',f'${n*2**t-1}',f'${n+1}']for t in range(5)],rf'a_t-b_t=({n})2^t-1', 'Both the shifted first value and the second value double, preserving their ratio. Their raw difference is not conserved.')

for n in[6,7]:
 fs=[];a=list(range(1,n+1));out=[]
 for t in range((n+1)//2+1):
  source=n-1-2*t;caption='Check the initial source before the first write.'if t==0 else'All required copies are complete; the negative source returns without access.'if source<0 else'The preceding copy is complete; the next source is two positions to its left.'
  f=frame('copy-array',rf'n_t={n}-1-2t,\quad i_t=t',caption,'The negative source guard is tested before access. Consecutive destination slots keep all copied values without gaps.',source=a,output=out.copy(),nextSource=source);f['teaching']['currentState']={'Completed copies':len(out),'Next source index':source,'Next destination index':len(out)};fs.append(f)
  if source>=0:out.append(a[source])
 scene('copy-'+str(n),'Reverse-stride source and contiguous destination','Array labels are concrete values. Source index markers and output order come from the actual copying algorithm.',fs,['Check the signed source guard.','Copy the current source to the next destination.','Decrease source by two and increase destination by one.'])

trace('prefix','Exact prefix sum with a negative input','The immutable input is four, minus seven, five; sum and rank have distinct roles.', ['next index','processed sum','remaining index rank'],[['$0','$0','$3'],['$1','$4','$2'],['$2','$-3','$1'],['$3','$2','$0']],r's=\sum_{j=0}^{i-1}a_j', 'The sum may decrease. Its exact prefix specification proves the result; the nonnegative remaining index rank proves termination.')
for n in[13,32]:
 e=n;r=1;b=2;rr=[];t=squares=extra=0
 while True:
  exact_power=lambda v:('$'+str(v))if v<100000 else r'$2^{'+str(v.bit_length()-1)+'}'
  rr.append([f'${t}',f'${e}',exact_power(r),exact_power(b),f'${squares+extra}'])
  if e==0:break
  if e%2:r*=b;extra+=1
  b*=b;squares+=1;e//=2;t+=1
 trace('power-'+str(n),'Binary powering with the final square counted',f'Base two and exponent {n}; every row is a loop head, including the final unused squared base.', ['completed bodies','exponent','accumulator','base','executed products'],rr,rf'rb^e=2^{{{n}}},\quad M={squares+extra}', 'Multiply the accumulator by the old base only for an odd exponent. The unconditional square counts even at the final iteration.')

trace('parity-authentic','The full consecutive-pair residue cycle','The source indices sixteen and seventeen are both odd. The exact pair state returns after three steps.', ['phase','first residue','second residue','next residue'],[['$0','$1','$1','$0'],['$1','$1','$0','$1'],['$2','$0','$1','$1'],['$3','$1','$1','$0']],r'(u,v)\mapsto(v,u+v\bmod2)', 'A deterministic return of the full pair state proves periodicity. Its phase places even terms at indices divisible by three.')
trace('horner','Backwards polynomial suffix checkpoints','Ascending coefficients are one, minus two, three, four; the evaluation input is two.', ['next index','current value','remaining bodies'],[['$3','$0','$4'],['$2','$4','$3'],['$1','$11','$2'],['$0','$20','$1'],['$-1','$41','$0']],r'value=\sum_{j=i+1}^{3}a_j2^{j-i-1}', 'Multiplying the old suffix by two shifts its powers, then the next coefficient enters at degree zero. At index minus one the whole polynomial is complete.')
trace('population-max','All guards in the maximum population witness','Use the add-one-blue/add-two-reds move five times from twelve blue and seven red.', ['step','blue','red','difference','population'],[[f'${t}',f'${12+t}',f'${7+2*t}',f'${5-t}',f'${19+3*t}']for t in range(6)],r'T=5,\quad P_{max}=34', 'The difference loses one per step and stays nonnegative. The population gains three, attaining the proved upper bound at equal counts.')
trace('population-min','All removal guards in the minimum population witness','Remove two blues and one red five times; the final state still has two of each.', ['step','blue','red','difference','population'],[[f'${t}',f'${12-2*t}',f'${7-t}',f'${5-t}',f'${19-3*t}']for t in range(6)],r'T=5,\quad P_{min}=4', 'Before each removal, both required token counts are available and blue exceeds red. The final equal counts disable every further move.')
trace('flat-acc','Right-first evaluation, left-to-right returned leaves','The source tree has leaves two, five, seven in that order, and the original shared suffix is nine, ten.', ['processed leaf','new prefix','unchanged shared suffix'],[['none','empty','9, 10'],['$7','7','9, 10'],['$5','5, 7','9, 10'],['$2','2, 5, 7','9, 10']],r'flatAcc(T,A)=flatten(T)\Vert A', 'Right-first evaluation builds the suffix first. Prepending the left leaves then returns their original left-to-right order, without copying the original suffix.')
trace('ackermann','Two fixed recursive conventions give different values','The standard first row grows linearly; the alternative positive-input first row doubles.', ['second input','standard first row','alternative first row'],[[f'${n}',f'${n+2}',f'${0 if n==0 else 2**n}']for n in range(6)],r'A(1,5)=7,\quad B(1,5)=32', 'Fix base equations before comparing named functions. Totality uses smaller lexicographic pairs and legal natural-valued intermediate outputs.')
scene('split-order','Greater block, pivot, smaller block: descending output','The concrete input has distinct values four, one, three, two, five and pivot three. Pure call evaluation order does not alter the prescribed joined block order.',[frame('split-order',r'R\Vert[m]\Vert L',cap,'Every greater-block value exceeds the pivot, and every smaller-block value is below it. Recursive hypotheses order both blocks; concatenation checks the cross-block comparisons.',stage=k,source=[4,1,3,2,5],greater=[4,5]if k<2 else[5,4],less=[1,2]if k<2 else[2,1],output=[]if k<3 else[5,4,3,2,1])for k,cap in enumerate(['Read the complete input before partitioning.','Partition around the actual median three.','Recursive calls return descending child blocks.','Join the greater block, median and smaller block in that order.'])],['Identify the actual pivot and partition all other values.','Apply the specification to both strictly shorter recursive inputs.','Verify occurrence preservation and both joined inequalities.'])
scene('modular-orbit','Five exact states in the modular move orbit','Coordinates are residues modulo five. The only move adds one to the first and two to the second, reducing both modulo five.',[frame('modular-grid',r'y-2x\equiv0\pmod5', 'Process the next actual residue pair; the coordinate wrap follows modulo five.', 'All highlighted visited states lie in the zero residue class. The red target three, four has a different residue and never joins this orbit.',step=t,visited=[[k%5,2*k%5]for k in range(t+1)],target=[3,4])for t in range(6)],['Start at the displayed origin.','Add the exact vector and reduce both coordinates modulo five.','Use the invariant for impossibility and the complete orbit for attainability.'])
trace('lattice-witness','An actual signed-generator path to the first target','Both forward and reverse generators are permitted on all integer pairs. This displayed path reaches five, zero.', ['step','first coordinate','second coordinate','conserved residue'],[['$0','$0','$0','$0'],['$1','$2','$1','$0'],['$2','$4','$2','$0'],['$3','$5','$0','$0']],r'x+3y\equiv0\pmod5', 'The first two steps add the first generator; the final step subtracts the second. Each update preserves the same residue and is a permitted move.')
rr=[];i,j=2,3;t=0
while True:
 rr.append([f'${t}',f'${i}',f'${j}',f'${4*i+j}'])
 if i==j==0:break
 if j:j-=1
 else:i-=1;j=3
 t+=1
trace('bounded-reset','A unit-decreasing rank despite secondary resets','This representative uses reset bound three and initial counters two, three. The general formula in the proof has an arbitrary declared bound.', ['step','primary','secondary','exact remaining rank'],rr,r'\rho=4i+j,\quad T=11', 'A secondary decrement lowers the rank by one. At a reset, primary weight four pays for the new three secondary steps plus the reset itself.')
trace('laurent','Ten exponent choices retain a residue modulo four','Each row chooses how many of the ten factors contribute exponent three; the other factors contribute minus one.', ['positive choices','negative choices','exponent','coefficient multiplicity'],[[f'${k}',f'${10-k}',f'${4*k-10}',f'${math.comb(10,k)}']for k in range(11)],r'e=4k-10,\quad e\equiv2\pmod4', 'The exponent combines all ten factor choices. Its coefficient counts which factors supplied the positive term, a separate quantity from whether that exponent occurs.')
trace('full-nineteen','Nineteen leaves: internal vertices, edges and all vertices','These are exact aggregate counts for a finite full binary tree; its particular shape is not specified.', ['quantity','exact count'],[['leaves','$19'],['internal vertices','$18'],['all vertices','$37'],['edges','$36']],r'L=I+1,\quad E=2I=V-1', 'Fullness gives two child edges per internal vertex. The finite tree relation then identifies leaves; vertices and edges differ by one.')
state_scene('integer-certificate','The unreachable integer predecessor that breaks closure',[-1,0,1,2],[[0,2],[1,3]],[('Only zero is initial.','The full domain is all integers; the drawing is a declared four-value excerpt.',[0],[]),('The next reached value is two.','Further actual reached values continue as nonnegative evens, outside this finite excerpt.',[0,2],[]),('Minus one satisfies the proposed non-one predicate.','Its successor one violates global closure but is not reached from zero.',[-1,0,2],[1])],r'x\mapsto x+2,\quad P(x):x\ne1', 'Only the displayed two edges are drawn from the infinite integer system. This is a counterexample excerpt, not a finite-state replacement for the full process.')
trace('mixed-challenge','Three internal arities in the concrete counting challenge','Four binary, three ternary and two unary internal vertices give an exact aggregate; the proof separately uses the tree edge relation.', ['vertex type','vertices','arity','edge contribution'],[['binary','$4','$2','$8'],['ternary','$3','$3','$9'],['unary','$2','$1','$2'],['leaf','$11','$0','$0']],r'E=19,\quad V=20,\quad L=11', 'Unary vertices add an edge and an internal vertex but no net leaf. Sum parent degrees before subtracting the internal count.')
flat=S['invariants-question-flat-acc'];flat['frames']=[]
for k,acc in enumerate([[9,10],[7,9,10],[5,7,9,10],[2,5,7,9,10]]):
 caption='The initial accumulator is the unchanged shared suffix.'if k==0 else'Prepend the evaluated leaf $'+str([7,5,2][k-1])+'$ to the previously constructed suffix.'
 f=frame('flat-tree',r'flatAcc(T,A)=flatten(T)\Vert A',caption,'Right-first evaluation makes the suffix first; left leaves are then prepended. Existing suffix cells are shared, and only one new cons is allocated per processed leaf.',nodes=[[0,0],[1,1],[2,1],[3,2],[4,2]],edges=[[0,1],[0,2],[2,3],[2,4]],leaves=[1,3,4],labels={'1':2,'3':5,'4':7},selected=[4,3,1][:k],accumulator=acc,stage=k);f['teaching']['currentState']={'Processed leaves':k,'New cons cells':k,'Shared original suffix cells':2};flat['frames'].append(f)
for k,f in enumerate(flat['frames']):f['teaching'].update(initial=k==0,activeLine=0 if k==0 else 2 if k==3 else 1,guide=flat['code']);f['line']=f['teaching']['activeLine']

all=json.loads((R/'dist/chapters/concept-animations.json').read_text(encoding='utf-8'));all['scenes'].update(S)
(R/'dist/chapters/concept-animations.json').write_text(json.dumps(all,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(E/'d_invariants-models.json').write_text(json.dumps(dict(models=len(S),uniqueFrames=sum(len(v['frames'])for v in S.values()),sceneIds=list(S),state='constructed_pending_independent_mathematics_and_rendering'),indent=2)+'\n',encoding='utf-8')
print({'models':len(S),'frames':sum(len(v['frames'])for v in S.values())})
