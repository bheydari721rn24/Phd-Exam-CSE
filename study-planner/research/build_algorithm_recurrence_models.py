from pathlib import Path
from fractions import Fraction
import json,math,html,sys,re
from markdown_it import MarkdownIt
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True});S={}
def prose(s):return mathml.markdown_math(s,md).strip().removeprefix('<p>').removesuffix('</p>')
def frame(kind,formula,caption,why,**data):return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**data),caption=caption,captionMathHtml=prose(caption),formula=formula,formulaHtml=mathml.render(formula,True),metrics={},line=0,teaching=dict(operation=caption,operationHtml=prose(caption),why=why,whyHtml=prose(why),currentState={},initial=False,activeLine=0,changes=[],checks=[]))
def scene(name,title,description,frames,guide=None):
 guide=guide or ['Read the input, base and measured quantity.','Apply the stated child map and the exact local toll.','Sum the complete admitted contributions and restore the original variable.']
 for i,f in enumerate(frames):
  f['line']=0 if i==0 else 2 if i==len(frames)-1 else 1;f['teaching'].update(initial=i==0,activeLine=f['line'],guide=guide,currentState={'Checkpoint':i,'Total checkpoints':len(frames)})
  if i:f['teaching']['changes']=[dict(field='Checkpoint',before=i-1,after=i)]
 id='algorithm-recurrence-question-'+name;S[id]=dict(id=id,title=title,description=description,descriptionHtml='<p>'+prose(description)+'</p>',invariant=description,visual=dict(type='enumeration',claim=description),code=guide,frames=frames,useAuthoredTeachingChanges=True)
def table(name,title,heads,rows,formulas,why,description):
 fs=[]
 for i in range(len(rows)):
  cell=lambda v:mathml.render(str(v)[1:]if str(v).startswith('$')else str(v),False)if str(v).startswith('$')or re.fullmatch(r'-?\d+(?:/\d+)?',str(v))else html.escape(str(v))
  fs.append(frame('table',formulas[i]if isinstance(formulas,list)else formulas,'Read the exact recurrence checkpoint at index $'+str(i)+'$.',why,headings=heads,rows=rows[:i+1],rowsHtml=[[cell(v)for v in r]for r in rows[max(0,i-6):i+1]],active=min(i,6)))
 scene(name,title,description,fs)
def recurrence(name,title,a,toll,h,seed,formula,description,original=None):
 values=[seed];rows=[[0,'base','base',seed]]
 for k in range(1,h+1):values.append(a*values[-1]+toll(k));rows.append([k,a*values[k-1],toll(k),values[k]])
 table(name,title,['index','propagated','local toll','total'],rows,formula,'The previous value is multiplied exactly once by the stated coefficient; the new toll is then added. The seed is retained.',description)
 S['algorithm-recurrence-question-'+name]['audit']=dict(mechanism='first-order',a=a,seed=seed,values=values,tolls=[toll(k)for k in range(1,h+1)],originalVariable=original)
def levels(name,title,a,b,h,toll,seed,formula,description,logLabels=False,terminalSize=1):
 N=terminalSize*b**h;rows=[];running=0;fs=[]
 for j in range(h+1):
  nodes=a**j;size=N//b**j;local=seed if j==h else toll(size);aggregate=nodes*local;running+=aggregate
  rows.append([j,nodes,size,local,aggregate,running]);fs.append(frame('level-work',formula,'Reveal depth $'+str(j)+'$: its contribution is $'+str(aggregate)+'$.','The diagram contains the root and its first split, explicitly labeled. The ledger counts the complete level by exact multiplicity and includes the terminal contribution.',a=a,b=b,N=N,h=h,level=j,rows=rows.copy(),labelsAreLogSizes=logLabels))
 scene(name,title,description,fs);S['algorithm-recurrence-question-'+name]['audit']=dict(mechanism='levels',a=a,b=b,h=h,N=N,seed=seed,rows=rows)
def chain(name,title,values,tolls,formula,description):
 fs=[];total=0
 for i,n in enumerate(values):
  local=tolls[i];total+=local;fs.append(frame('chain',formula,'Inspect chain state $'+str(n)+'$, adding local cost $'+str(local)+'$.','One executed child creates one next state. The displayed window is marked; earlier and later windows are available through checkpoints.',values=values,tolls=tolls,index=i,total=total,windowStart=max(0,min(i-2,len(values)-5))))
 scene(name,title,description,fs);S['algorithm-recurrence-question-'+name]['audit']=dict(mechanism='chain',values=values,tolls=tolls)

prefix=[1];rows=[]
for n in range(7):
 if n:prefix.append(sum(prefix))
 rows.append([n,prefix[n],sum(prefix)])
table('prefix','Authentic prefix terms and their accumulated sums',['index','term','prefix sum'],rows,r'C(x)=\frac{1-x}{1-2x}','The next term is the previous prefix. At index zero and one the terms are both one, so a universal doubling rule would be false.','Every displayed value is an exact checkpoint; the formal-series proof supplies the general result.')

def unequal(name,quadratic=False):
 nodes=[dict(id=0,parent=None,x=380,y=72,size=Fraction(64),depth=0)];front=[0];fs=[]
 for depth in range(5):
  costs=[n['size']**(2 if quadratic else 1)for n in nodes if n['depth']==depth];formula=(r'\sum_{v\text{ at depth }j}|v|^2=64^2(5/8)^j'if quadratic else r'\sum_{v\text{ at depth }j}|v|=64')
  fs.append(frame('unequal',formula,'Inspect exact depth $'+str(depth)+'$ of the illustrative unperturbed tree.','The displayed branches are the first two depths. The complete frontier is counted in the ledger; these checkpoints precede the fixed base and are not a claim that unequal branches have equal terminal depth.',quadratic=quadratic,depth=depth,shown=[dict(id=n['id'],parent=n['parent'],size=str(n['size']),depth=n['depth'])for n in nodes if n['depth']<=2],frontier=[str(n['size'])for n in nodes if n['depth']==depth],total=str(sum(costs)),root=64))
  if depth<4:
   for pid in front:
    for ratio in[Fraction(1,4),Fraction(3,4)]:nodes.append(dict(id=len(nodes),parent=pid,size=nodes[pid]['size']*ratio,depth=depth+1))
   front=[n['id']for n in nodes if n['depth']==depth+1]
 scene(name,'Unequal squared-size mass'if quadratic else'Unequal conserved linear mass','The exact one-quarter and three-quarter real-size tree is illustrative. Its frontier arithmetic is complete at every shown depth, while only seven diagram nodes are drawn.',fs)
unequal('unequal');unequal('quadratic',True)
chain('polylog','One chain: squared logarithmic tolls',[64,32,16,8,4,2,1],[36,25,16,9,4,1,1],r'T(64)=1+\sum_{r=1}^{6}r^2=92','The concrete chain uses base-two logarithms and a unit base; the authentic question asks for order, so this is an illustrative exact input.')
levels('sqrt','Square-root recurrence: complete transformed level costs',2,2,5,lambda m:m,1,r'T(2^{32})=192',r'The labeled node values are logarithmic sizes, not original input sizes. The exact original grid has input $2^{32}$ and base input two.',True)
scene('pivot','A sample median and the permitted rank interval','Distinct keys and the sample median guarantee three sampled keys on either side at input sixteen. The unsampled keys can all be placed on one side.',[frame('pivot',r'm=2\sqrt{16}+1=9','Reveal the median and its six forced sample neighbors.','The global rank can range from four through thirteen; an unsampled item has no forced side until its value is specified.',stage=i,n=16,m=9,left=4,right=13)for i in range(4)])
rows=[[k,2**k,k*(k+1)//2,2**(k*(k+1)//2)]for k in range(5)]
table('product','Changing multipliers and exact triangular exponents',['index','multiplier','exponent','exact value'],rows,r'T_n=2^{n(n+1)/2}','Each multiplier is 2 to the current index. The resulting product exponent is the finite triangular sum.','The exact values and exponent checkpoints are shown independently; the display does not compress an exponent into a loose growth class.')
scene('parity','The anchored three-state parity cycle','The cycle phase is anchored at indices sixteen and seventeen, then checked on every requested index.',[frame('parity',r'p_n\equiv p_{n-1}+p_{n-2}\pmod2','Inspect the parity at original index $'+str(n)+'$.','Even terms align with multiples of three; the initial pair fixes this phase.',index=n,residue=0 if n%3==0 else 1,step=i,requested=list(range(100,114)))for i,n in enumerate([16,17,18,19,20,21]+list(range(100,114)))])
levels('balanced32','Input thirty-two with leaf cost three',2,2,5,lambda size:size,3,r'T(32)=160+96=256','All five internal levels and the entire leaf contribution are counted. The root and its first children illustrate the split; the ledger counts every node.')
chain('cubes16','The exact cubic-logarithm chain at sixteen',[16,8,4,2,1],[64,27,8,1,1],r'T(16)=64+27+8+1+1=101','This full chain is the exact stated input, with the final unit base separate from the unit toll at input two.')
levels('four-sqrt','Four children after logarithmic transformation',4,2,3,lambda size:size,1,r'S(16)=16+32+64+64=176',r'The displayed original input is $2^{16}$, with base input at most four and unit cost. The transformed base is at logarithmic size two.',True,2)
prefix=[1];rows=[]
for n in range(6):
 if n:prefix.append(3*sum(prefix))
 rows.append([n,prefix[n],sum(prefix)])
table('prefix-three','A multiplier-three prefix recurrence',['index','term','prefix sum'],rows,r'a_5=3\cdot4^4=768','The first term is three; all later transitions multiply terms by four. The prefix is four to the index.','Every original prefix and term checkpoint is exact; the first exceptional transition is retained.')
rows=[[n,1+2*n,2**n,(1+2*n)*2**n]for n in range(5)]
table('repeated-root','Normalize the repeated characteristic root',['index','normalized','scale','term'],rows,r'a_n=(1+2n)2^n','The normalized sequence has constant difference two. Two initial conditions determine its intercept and slope.','The four-step recurrence is checked by a separately displayed affine normalization, not by a generic growth curve.')
chain('odd-squares','Odd tolls add an exact square',[4,3,2,1,0],[7,5,3,1,0],r'T(4)=7+5+3+1=16','This is the complete decrement chain at input four, including the zero seed.')
scene('fib','Fibonacci dependencies: state graph and executed call count','Each arrow is a mathematical dependency between distinct states. Green states are evaluated once under memoization. The naive call count is recorded separately, not represented as a duplicated DAG edge.',[frame('fib',rf'C_{{{k}}}=2F_{{{k+1}}}-1','Evaluate distinct Fibonacci state $'+str(k)+'$.','The state graph contains overlapping dependencies. Memoization does not execute every path as a new call.',evaluated=k,n=7)for k in range(8)])
for n in [5,8]:
 recurrence('affine-'+str(n),'Shifted affine recurrence, index '+str(n),2,lambda k:3,n,0,r'T_n=3(2^n-1)','Exact propagated values and local tolls retain the shifted seed.')
 levels('balanced-'+str(n),'Complete balanced levels, depth '+str(n),2,2,n,lambda s:s,1,r'T(2^n)=(n+1)2^n','The transformed index is recursion depth; every aggregate includes exact multiplicity and the base.')
 levels('leaf-'+str(n),'Four-child level amplification, depth '+str(n),4,2,n,lambda s:s,1,r'U_n=2\cdot4^n-2^n','Increasing level work and complete unit leaves explain the exact finite correction.')
 chain('chain-'+str(n),'A single halving chain, depth '+str(n),[2**k for k in range(n,-1,-1)],[2**k if k else 1 for k in range(n,-1,-1)],r'U_n=2^{n+1}-1','Every chain input and actual toll is exact. The window advances without skipping undisplayed checkpoints.')
 recurrence('squares-seed-'+str(n),'Squared index toll with unit seed',1,lambda k:k*k,n,1,r'U_n=1+\frac{n(n+1)(2n+1)}6','The index ledger is complete; conversion to logarithmic input is stated in the question solution.')
 recurrence('squares-zero-'+str(n),'Squared original-input toll with zero seed',1,lambda k:k*k,n,0,r'T_n=\frac{n(n+1)(2n+1)}6','This index is the original integer input. The zero seed differs from the unit-seed family.')
 recurrence('weighted-index-'+str(n),'Two-child weighted index toll',2,lambda k:k,n,0,r'U_n=2^{n+1}-n-2','The finite weighted sum retains its nonzero tail correction and zero seed.')
 levels('ternary-'+str(n),'Two children with one-third input size',2,3,n,lambda s:1,0,r'T(3^n)=2^n-1','Child count two and shrink factor three are displayed separately. Leaves have zero cost in this abstract problem.')
 levels('double-log-'+str(n),'Double-logarithmic depth restored to input',2,2,n,lambda s:s,1,r'T(2^{2^n})=(n+1)2^n','Node labels are logarithmic sizes. The original input is double exponential, and the base original input is two.',True)
values=[100]
while values[-1]>1:values.append(values[-1]-math.isqrt(values[-1])-(math.isqrt(values[-1])**2!=values[-1]))
chain('slow','Ceiling-square-root decrement at one hundred',values,[1]*(len(values)-1)+[0],r'h(100)=16','Every integer child uses the actual ceiling. A zero terminal cost is chosen for the illustrative depth count; the original order permits any bounded base cost.')
scene('reuse','Executed half-size chain with a reused reference','Blue solid arrows execute the first child; the dashed reference denotes reuse of its identical result and adds no second recursive computation.',[frame('reuse',r'T(32)=1+32+16+8+4+2=63','Reveal executed chain depth $'+str(i)+'$.','The second request is a reference to the same state. It is not a distinct child with the same size.',index=i,values=[32,16,8,4,2,1],tolls=[32,16,8,4,2,1],logToll=False)for i in range(6)])
levels('challenge1','Five quarter-size children',5,4,5,lambda s:2*s,1,r'T(4^5)=19933','Complete aggregate level costs and leaf contribution are counted; the diagram illustrates only the first two depths.')
levels('challenge2','Critical fourth-root toll',3,81,4,lambda s:round(s**.25)*10,1,r'T(81^4)=3321','The critical exponent is one-quarter. Exact fourth roots are integers on this grid.')
for k in[1,2]:
 rows=[];v=Fraction(1,2)
 for h in range(1,9):
  if h>1:v+=Fraction(1,h**k)
  rows.append([h,str(Fraction(0)if h==1 else Fraction(1,h**k)),str(v),str(2**h*v)])
 table('harmonic-'+str(k),'Critical reciprocal log power '+str(k),['depth','new term','normalized sum','total'],rows,r'T_k(2^h)=2^h\left(\frac12+\sum_{r=2}^h\frac1{r^k}\right)','The stated base is at depth one. The harmonic case diverges slowly; the squared reciprocal sum is bounded.','These are exact rational mathematical costs, not asserted integer operation counts.')
rows=[];v=1
for h in range(6):
 N=2**h;f=0 if h==0 else N**(2 if h%2 else 3)
 if h:v=2*v+f
 rows.append([h,N,f,v])
table('challenge4','Alternating positive polynomial tolls',['depth','input','root toll','total'],rows,r'T(N)\in\Theta(N^3)','At odd depths, the previous even-depth cubic toll dominates the current quadratic root toll.','Exact grid values demonstrate failure of the regularity ratio; the upper and lower proof supplies the general classification.')
scene('challenge5','Two halves and three thirds: squared-size weights','The root is six. Two children have size three and three children have size two, yielding child square sum thirty against root square thirty-six.',[frame('weighted',r'2(3^2)+3(2^2)=30=\frac56\cdot36','Reveal one of the five weighted branches.','The remaining one-sixth quadratic slack determines induction constant six. These are unperturbed real-size children.',stage=i,children=[3,3,2,2,2])for i in range(6)])
nodes=[]
def merge(n,parent=None,depth=0):
 id=len(nodes);nodes.append(dict(id=id,parent=parent,size=n,depth=depth,cost=n-1 if n>1 else 0))
 if n>1:merge(n//2,id,depth+1);merge((n+1)//2,id,depth+1)
merge(13);maxdepth=max(n['depth']for n in nodes)
scene('challenge6','The complete rounded merge tree at thirteen','Every one of the twenty-five nodes is drawn. Blue shading identifies the current depth. The depth summary distinguishes size tolls from worst-case comparisons.',[frame('merge-tree',r'A(13)=49,\quad C(13)=37','Reveal all nodes at actual depth $'+str(d)+'$.','Singleton leaves have zero cost. A size-two internal node can lie one level below its neighboring singleton leaves.',nodes=nodes,depth=d,levels=[dict(depth=j,sizeToll=sum(n['size']if n['size']>1 else 0 for n in nodes if n['depth']==j),comparisons=sum(n['cost']for n in nodes if n['depth']==j))for j in range(maxdepth+1)])for d in range(maxdepth+1)])
values=[1];rows=[[0,1,1,1]]
for n in range(1,6):values.append(n*values[-1]+math.factorial(n));rows.append([n,math.factorial(n),n+1,values[-1]])
table('challenge7','Factorial normalization with a nonzero toll',['index','factorial','normalized','total'],rows,r'T_n=(n+1)n!','Division by the nonzero factorial converts the variable coefficient to a unit-step additive recurrence.','Every exact value and normalizer is declared; the extra factor n+1 is retained.')
scene('challenge8','Four equally likely larger-child outcomes','The rank distribution is complete for input four. Each outcome has probability one-quarter; it is not replaced by a fictitious fractional child.',[frame('expectation',r'\mathbb E[J^2]=13/2\ne25/4=(\mathbb E[J])^2','Reveal '+str(i)+' of the four rank outcomes.','The quadratic mean is obtained by averaging actual squared costs. Squaring the mean discards the variance.',inspected=i,ranks=[0,1,2,3],sizes=[3,2,2,3])for i in range(5)])
rows=[[n,n*(n+1)//2,n*n,Fraction(n*n,2),Fraction(n,2)]for n in range(7)]
table('challenge9','Exponent differences determine tight classes',['index','exact exponent','candidate 1','candidate 2','gap to second'],rows,r'\frac{T_n}{2^{n^2/2}}=2^{n/2}','The second exponent differs by a growing linear term, so the original exponential ratio is unbounded.','Only exponents are tabulated to avoid huge unreadable integers; the formulas retain the exact exponential values.')
rows=[];U=V=1
for h in range(6):
 if h:U+=h;V=2*V+h
 rows.append([h,2**h,U,V])
table('challenge10','Reused chain versus executed binary calls',['depth','input','reused work','unreused work'],rows,r'U_h=1+\frac{h(h+1)}2,\quad V_h=3\cdot2^h-h-2','The same logarithmic local toll is accumulated once per depth in the reused chain, but amplified by two children in the unreused tree.','Both exact bases are one; identity of state, not merely equal size, authorizes the reference edge.')
p=R/'dist/chapters/concept-animations.json';data=json.loads(p.read_text());data['scenes'].update(S);p.write_text(json.dumps(data,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf8')
(E/'a_recurrence-models.json').write_text(json.dumps(dict(topicId='a_recurrence',models=len(S),frames=sum(len(s['frames'])for s in S.values()),ids=list(S),state='exact_models_pending_independent_and_rendered_checks'),indent=2)+'\n',encoding='utf8');print({'models':len(S),'frames':sum(len(s['frames'])for s in S.values())})
