"""Question-specific states and witnesses, with distinct array, tree, graph and interval views."""
from pathlib import Path
from fractions import Fraction
from math import comb
import copy,json,sys
from markdown_it import MarkdownIt
from read_correctness_bank import rows
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'research/exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True});S={}
def prose(s):return mathml.markdown_math(s,md).strip().removeprefix('<p>').removesuffix('</p>')
def frame(kind,caption,why,formula,**data):return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**copy.deepcopy(data)),caption=caption,captionMathHtml=prose(caption),formula=formula,formulaHtml=mathml.render(formula,True),metrics={},line=0,teaching=dict(operation=caption,operationHtml=prose(caption),why=why,whyHtml=prose(why),currentState={},changes=[],checks=[]))
def scene(n,description,fs):
 key='correctness-question-q'+str(n);guide=['Read the precise input, premises, and representation.','Apply one stated transition or inspect one witness.','Check the invariant, result, and missing obligation.']
 for i,f in enumerate(fs):
  f['line']=0 if i==0 else 2 if i==len(fs)-1 else 1;f['teaching'].update(initial=i==0,activeLine=f['line'],guide=guide,currentState={'Checkpoint':i,'Checkpoints':len(fs)})
  if i:f['teaching']['changes']=[{'field':'Checkpoint','before':i-1,'after':i}]
 S[key]=dict(id=key,title=rows[n-1]['title'].split('. ',1)[1],description=description,descriptionHtml='<p>'+prose(description)+'</p>',invariant=description,visual=dict(type='enumeration',claim=description),code=guide,frames=fs,useAuthoredTeachingChanges=True)
def ledger(n,description,steps):
 scene(n,description,[frame('ledger',caption,why,formula,labels=labels,values=values)for caption,why,formula,labels,values in steps])
def flow(n,description,steps):
 scene(n,description,[frame('flow',caption,why,formula,boxes=boxes)for caption,why,formula,boxes in steps])
def arrays(n,description,steps):
 scene(n,description,[frame('arrays',caption,why,formula,rows=data)for caption,why,formula,data in steps])
flow(1,'Illustrative witness for the general distinct-key question: input values 1 through 5, with actual pivot 3. Blocks preserve their original values.',[("Partition by an input median.","Every greater key belongs on the left of the descending join.",r'm=3',[{'label':'Greater child','value':'4, 5'},{'label':'Pivot','value':'3'},{'label':'Smaller child','value':'1, 2'}]),("Each child returns a descending permutation.","Strong induction supplies order and conservation, not merely a sorted-looking array.",r'5>4>3>2>1',[{'label':'Greater output','value':'5, 4'},{'label':'Pivot','value':'3'},{'label':'Smaller output','value':'2, 1'}])])
for n,N in[(2,6),(51,10)]:
 a=list(range(N));out=[];steps=[]
 for k in range((N+1)//2+1):
  source=N-1-2*k;steps.append(('Inspect the next recursive call.'if source>=0 else'Return before any negative-index access.','Source falls by two; destination advances by one. Empty output cells are unwritten, not copied zeros.',r'n=N-1-2k,\quad i=k',[{'label':'Source values; yellow is the next source','values':a,'active':source,'indices':True},{'label':'Destination prefix; dash means unwritten','values':out+['—']*((N+1)//2-len(out)),'active':k if source>=0 else-1,'indices':True}]))
  if source>=0:out.append(a[source])
 arrays(n,('A declared N=6 teaching witness for the general recursive question.'if n==2 else'The exact N=10 index trace. Source values are illustrative indices; the copied positions are the question data.'),steps)
def tree(n,description,variants):
 fs=[]
 for name,nodes,edges,mass,why in variants:fs.append(frame('tree',name,why,r'\alpha='+mass,nodes=nodes,treeEdges=edges))
 scene(n,description,fs)
full=[{'id':'r','x':380,'y':78,'value':'1','label':'root'},{'id':'l','x':235,'y':186,'value':'1/2','label':'leaf'},{'id':'q','x':525,'y':186,'value':'1/2','label':'leaf'}]
tree(3,'Two finite witnesses test the universal alternatives; each node receives half its parent budget.',[('A full two-leaf tree attains mass one.',full,[['r','l'],['r','q']],'1','Both child budgets are retained.'),('A missing child leaves half the root budget unused.',full[:2],[['r','l']],r'\frac12','The root has one leaf child, refuting always-equal mass.')])
for n,m,c0 in[(4,15,10),(50,4,7)]:
 total=0;steps=[]
 for i in range(1,m+1):
  add=comb(m-i+2,2);total+=add;steps.append((f'Complete all inner visits for outer index {i}.','This checkpoint aggregates every j,k visit for this fixed i; it is not a claim to animate only one inner increment.',r'C=c_0+\binom{n+2}{3}'if i==m else r'C=c_0+\text{completed visits}',['outer i','inner visits','total visits','accumulator'],[i,add,total,c0+total]))
 ledger(n,('Exact upper bound 15 and initial value 10; fifteen grouped checkpoints represent all 680 increments.'if n==4 else'Declared n=4, initial value 7 teaching witness for the symbolic general formula. All twenty triples are counted.'),steps)
flow(5,'Exact successful preimages under x := x+3; the rejected final-value candidates are explained in the written solution.',[("Move initial values through the assignment.","Old x must be shifted before testing the final square.",r'(x+3)^2=25',[{'label':'Initial values','value':'2, −8'},{'label':'Add three','value':'5, −5'},{'label':'Final squares','value':'25, 25'}])])
ledger(6,'Exact state trace for the derived original input x=4; old y is irrelevant.',[("Initial requirement.","Initial y is unconstrained because it will be overwritten.",r'x_0=4',['x','y'],[4,'any']),('Execute x := x+1.','The second statement sees updated x.',r'x=5',['x','y'],[5,'any']),('Execute y := 2x.','Use current x=5.',r'y=10',['x','y'],[5,10]),('Execute x := y−3.','The final target is met.',r'x=7',['x','y'],[7,10])])
ledger(7,'The exact pair (5,8), evaluated under two different assignment semantics.',[("Start from one old-state snapshot.","Both implementations start with the same input.",r'(x_0,y_0)=(5,8)',['sim x','sim y','seq x','seq y'],[5,8,5,8]),('Complete both transformers.','The sequential sum reads updated x; the simultaneous sum reads old x.',r'(y,x+y)\ne(y,2y)',['sim x','sim y','seq x','seq y'],[8,13,8,16])])
scene(8,'Finite boundary witnesses for the proved full integer condition; the diagram is not an exhaustive domain proof.',[frame('numberline','Evaluate guarded outputs around the excluded region.','Only initial x≤−3 or x≥1 achieves final value at least three.',r'x\le-3\lor x\ge1',inputs=list(range(-4,4)),outputs=[-x if x<0 else x+2 for x in range(-4,4)],valid=[x<=-3 or x>=1 for x in range(-4,4)])])
flow(9,'The valid consequence directions. The implementation C is unspecified; no stronger result is invented.',[('Strengthen the admitted inputs; weaken the promised outputs.','The new precondition implies the old precondition; the old postcondition implies the new postcondition.',r'P^{\prime}\Rightarrow P,\quad Q\Rightarrow Q^{\prime}',[{'label':'New input restriction','value':'x ≥ 2'},{'label':'Proved command','value':'C'},{'label':'Weaker result','value':'r ≥ 0'}])])
arrays(10,'Two declared valid-index witnesses distinguish aliasing from nonaliasing; initial unused cells are 9.',[("Use distinct cells i=0, j=1.","The second write preserves the first cell.",r'i\ne j',[{'label':'After A[i]=1 then A[j]=2','values':[1,2,9],'active':1,'indices':True}]),('Use the same cell i=j=0.','The second write overwrites the first result; one cell cannot equal both one and two.',r'A[0]=2\ne1',[{'label':'Aliasing final state','values':[2,9,9],'active':0,'indices':True}])])
ledger(11,'Reachable equal pairs and an explicitly unreachable counter-witness admitted by the weak annotation.',[('Initial reachable state.','Both nonnegativity and equality hold.',r'x=y',['x','y','reachable'],[0,0,'yes']),('One reachable transition.','Both coordinates increase.',r'x=y',['x','y','reachable'],[1,1,'yes']),('Test the weak predicate on an admitted state.','This state is not claimed reachable; it refutes the implication from x≥0 to x=y.',r'x\ge0\not\Rightarrow x=y',['x','y','reachable'],[1,0,'no'])])
ledger(12,'Zero is the sole reachable state; one is a separate annotation witness, not a reachable state.',[('Reachable zero maps to zero.','The reachable set stays at zero.',r'0\mapsto0',['before','after','reachable before'],[0,0,'yes']),('An admitted positive witness maps below zero.','The annotation is not inductive over all its states.',r'1\mapsto-1',['before','after','reachable before'],[1,-1,'no'])])
ledger(13,'Verification conditions for the stipulated false guard; the body never runs.',[('Check the chosen False annotation.','Initialization fails even though preservation and exit are vacuous.',r'\text{True}\not\Rightarrow\text{False}',['initialization','preservation','exit'],['fails','vacuous','vacuous']),('Replace the annotation by True.','The unchanged command now has valid obligations and immediate termination.',r'\text{True}\Rightarrow\text{True}',['initialization','preservation','exit'],['valid','vacuous','valid'])])
ledger(14,'Declared n=8 witness for the general exact formula; each body subtracts at most three.',[(f'After {k} bodies.','The clamp preserves nonnegativity; the first zero ends the loop.',r'x_k=\max(0,8-3k)',['bodies','x','guard'],[k,max(0,8-3*k),'true' if 8-3*k>0 else 'false'])for k in range(4)])
ledger(15,'A finite prefix of an infinite exact-real execution, not a claim to draw infinity.',[(f'After {k} exact divisions.','Every displayed value is positive; the general proof establishes this at every finite checkpoint.',r'x_k=2^{-k}>0',['bodies','exact x','guard'],[k,str(Fraction(1,2**k)),'true'])for k in range(7)])
ledger(16,'Declared finite choice B=4 illustrates lexicographic descent; the proof permits arbitrarily larger finite choices.',[('Initial pair.','The first coordinate will decrease at the reset.',r'(1,0)',['first','second','steps'],[1,0,0])]+[(f'Reset and then decrement: checkpoint {5-b}.','The pair is lexicographically smaller at each move; B is a fixed finite choice in this trace.',r'(0,'+str(b)+')',['first','second','steps'],[0,b,5-b])for b in range(4,-1,-1)])
def search(n,a,t,upper=False,fault=False):
 lo=0;hi=len(a);fs=[];count=0
 while True:
  mid=(lo+hi)//2 if lo<hi else None
  formula=r'0\le lo\le hi\le n'
  fs.append(frame('search','Inspect the unresolved interval.'if mid is not None else'Return the meeting boundary.','Equality follows the declared threshold. Sortedness is required for regional exclusion.'if not fault else'The below-target update keeps the midpoint and can leave a singleton unchanged.',formula,values=a,lo=lo,hi=hi,mid=mid,target=t,upper=upper,iterations=count))
  if mid is None:break
  previous=(lo,hi)
  if a[mid]<t or upper and a[mid]==t:lo=mid if fault else mid+1
  else:hi=mid
  count+=1
  if previous==(lo,hi):
   fs.append(frame('search','The same singleton state repeats forever.','This is a repeated-state counterexample; strict width descent fails.',r'V^{\prime}=V=1',values=a,lo=lo,hi=hi,mid=mid,target=t,upper=upper,iterations=count));break
 scene(n,'Exact '+('upper-bound'if upper else'lower-bound')+' trace for input '+str(a)+' and target '+str(t)+'.',fs)
search(17,[1,3,3,3,8,9],3);search(18,list(range(31)),31);search(19,[2],3,fault=True);search(20,[4,1,3],3);search(21,[1,2,2,2,5],2)
S['correctness-question-q21']['description']+=' This player shows lower bound 1; its paired upper-bound proof and separate upper trace are available in the comparison frames.'
# Add the exact upper-bound trace to the same player's selectable checkpoint sequence.
lower21=copy.deepcopy(S['correctness-question-q21']['frames']);search(21,[1,2,2,2,5],2,upper=True);upper21=S['correctness-question-q21']['frames'];scene(21,'First lower-bound trace, then upper-bound trace for the exact same duplicate block; the mode label distinguishes them.',lower21+upper21)
ledger(22,'Exact even and odd width witnesses support the general floor bound; symbolic proof appears in the solution.',[(f'Width L={L}.','The two branches remove the inspected midpoint and retain different even-length sizes.',r'\max(L_{\text{left}},L_{\text{right}})=\lfloor L/2\rfloor',['old width','hi branch','lo branch','maximum'],[L,L//2,L-L//2-1,L//2])for L in[1,2,3,4,5,6]])
a=[4,2,3,1];steps=[];shifts=0
for i in range(1,4):
 key=a[i];j=i-1
 while j>=0 and a[j]>key:
  a[j+1]=a[j];j-=1;shifts+=1;steps.append(('Shift a larger prefix key into the hole.','Ignore the newly vacated hole and retain the saved key separately.',r'\text{shifts}='+str(shifts),[{'label':f'Physical array; hole={j+1}, saved={key}','values':a.copy(),'hole':j+1,'active':j+2,'indices':True}]))
 a[j+1]=key;steps.append(('Place the saved key and close the hole.','The physical array is now a permutation; only the processed prefix is promised sorted.',r'\text{shifts}='+str(shifts),[{'label':'After placement; total shifts shown below','values':a.copy(),'active':j+1,'indices':True}]))
arrays(23,'Exact insertion trace of [4,2,3,1]. The hole is excluded from logical conservation until placement.',steps)
arrays(24,'The exact [1,4,2] insertion checkpoint; the saved 2 is outside the physical array during the shift.',[('Save the final key.','The final position is the logical hole.',r'\text{saved}=2',[{'label':'Physical array before the shift','values':[1,4,2],'hole':2,'indices':True}]),('Shift 4 to the right.','Exclude index one and include saved 2 when checking the original multiset.',r'\{1,4\}\uplus\{2\}=\{1,4,2\}',[{'label':'Physical duplicates; logical hole at index 1','values':[1,4,4],'hole':1,'indices':True}]),('Restore the saved key.','Closing the hole restores the physical permutation.',r'1\le2\le4',[{'label':'Final physical array','values':[1,2,4],'active':1,'indices':True}])])
arrays(25,'Exact equal-key record witness; a,b identify original records.',[('Original equal records.','Stability concerns identity order, not only key values.',r'2=2',[{'label':'Before inclusive shifting','values':['2a','2b'],'indices':True}]),('Greater-or-equal shifting crosses an equal record.','The keys remain ordered, but b now precedes a.',r'\text{sorted}\not\Rightarrow\text{stable}',[{'label':'After insertion with ≥','values':['2b','2a'],'indices':True}])])
l=[1,4,7];r=[2,3,8];i=j=c=0;o=[];fs=[]
while i<len(l)and j<len(r):
 fs.append(frame('merge','Compare two valid heads.','Consumed values appear exactly once in output; the pointers mark the next heads.',r'C='+str(c),left=l,right=r,i=i,j=j,output=o.copy(),comparisons=c,charge=0));c+=1
 if l[i]<=r[j]:o.append(l[i]);i+=1
 else:o.append(r[j]);j+=1
fs.append(frame('merge','Copy the remaining 8 without another head comparison.','The left run is exhausted and the right suffix is sorted.',r'C=5',left=l,right=r,i=i,j=j,output=o+r[j:],comparisons=c,charge=0));scene(26,'Exact two-run merge; only comparisons between two valid heads count.',fs)
arrays(27,'Declared [3,1] counterexample to sortedness-only checking.',[('Input requires order and conservation.','The original multiset is {3,1}.',r'\{3,1\}',[{'label':'Input','values':[3,1],'indices':True}]),('Zeroing passes an order check but loses the input.','The result is nondecreasing; its multiset is wrong.',r'\{0,0\}\ne\{3,1\}',[{'label':'Faulty output accepted by order-only checker','values':[0,0],'indices':True}])])
flow(28,'A finite displayed prefix of the empty-input recursion failure; every next child still has size zero.',[('The size-one base condition never applies.','The next call repeats the same zero-size problem.',r'n=0\mapsto0\mapsto0',[{'label':'Admitted empty input','value':'n=0'},{'label':'First recursive child','value':'n=0'},{'label':'Same unresolved child','value':'n=0'}])])
def part(n,a,p,fault=False):
 a=a.copy();lt=i=0;gt=len(a);fs=[];count=0
 while True:
  fs.append(frame('partition','Inspect the four half-open regions.'if i<gt else'Read the returned equal-block boundaries.','The current position stays unknown after a right swap.'if not fault else'The faulty right branch skips the incoming unknown value.',r'V=gt-i='+str(gt-i),values=a.copy(),lt=lt,i=i,gt=gt,pivot=p,iterations=count))
  if i==gt:break
  if a[i]<p:a[lt],a[i]=a[i],a[lt];lt+=1;i+=1
  elif a[i]==p:i+=1
  else:gt-=1;a[i],a[gt]=a[gt],a[i];i+=int(fault)
  count+=1
 scene(n,('Faulty'if fault else'Correct')+' exact partition trace for input '+str(fs[0]['snapshot']['values'])+' with pivot '+str(p)+'.',fs)
part(29,[3,1,2,3,0],2);part(30,[3,1],2,True);part(31,[2,0,1,2,1],1)
arrays(32,'The exact tagged [3a,3b,1c] pivot-two witness. Record identity is retained in labels.',[('Original identity order.','The two equal-3 records begin a before b.',r'3=3',[{'label':'Input records','values':['3a','3b','1c'],'indices':True}]),('The first right swap reverses the equal records.','The final greater-key region retains this new order.',r'\text{permutation}\not\Rightarrow\text{stable}',[{'label':'Final partition; smaller block is [0,1)','values':['1c','3b','3a'],'indices':True}])])
ledger(33,'Exact repeated subtraction for X=47, Y=6.',[(f'After {q} subtractions.','The remainder is nonnegative; exit is allowed exactly below the positive divisor.',r'47=6q+r',['q','r','guard'],[q,47-6*q,'true' if 47-6*q>=6 else 'false'])for q in range(8)])
ledger(34,'Declared X=47, zero-divisor counterexample under exact integer semantics.',[(f'After {q} bodies.','The remainder never changes, so the guard stays true.',r'47=q\cdot0+47',['q','r','guard'],[q,47,'true'])for q in range(4)])
ledger(35,'The exact defective sequential Euclid transition compared with the correct next pair.',[('Initial pair.','Both variants start with 21 and 15.',r'\gcd(21,15)=3',['a','b'],[21,15]),('Overwrite a before calculating the remainder.','The needed old 21 is lost.',r'a=15',['a','b'],[15,15]),('Calculate the wrong remainder.','The routine exits with 15 rather than the true gcd 3.',r'15\bmod15=0',['a','b'],[15,0])])
a,b=34,21;steps=[]
while True:
 steps.append(('Inspect the current Euclidean pair.','The common-divisor set is conserved; a positive old b bounds the new remainder.',r'\gcd(a,b)=1',['a','b','bodies'],[a,b,len(steps)]))
 if b==0:break
 a,b=b,a%b
ledger(36,'Exact Euclidean trace from (34,21), including the final transition to b=0.',steps)
for n,A,B in[(37,3,13),(38,2,45)]:
 r=1;b=A;e=B;c=sq=0;steps=[]
 while True:
  steps.append(('Inspect a complete fast-power checkpoint.','The odd branch consumes one set bit; this code squares on every body, including the last.',r'rb^e='+str(A)+'^{'+str(B)+'}', ['r','b','e','acc products','squares'],[str(r),str(b),e,c,sq]))
  if e==0:break
  if e%2:r*=b;c+=1
  b*=b;e//=2;sq+=1
 ledger(n,'Exact base/exponent ('+str(A)+','+str(B)+') under unbounded integer arithmetic. Large values use exact decimal strings in the ledger.',steps)
ledger(39,'Exact (base,exponent)=(2,1) counterexample to the reversed square/odd-product order.',[('Initial state.','The correct target is two.',r'2^1=2',['r','b','e'],[1,2,1]),('Square the base too early.','The odd product will now read four instead of two.',r'b=4',['r','b','e'],[1,4,1]),('Finish the faulty body.','Termination succeeds but the numerical answer is wrong.',r'4\ne2',['r','b','e'],[4,4,0])])
ledger(40,'Exact M=1, exponent-zero normalization boundary; the loop does not execute.',[('Literal-one initialization.','Congruence alone does not imply the canonical output range.',r'1\notin[0,1)',['modulus','exponent','accumulator'],[1,0,1]),('Normalize the identity before the loop.','The canonical zero residue is now returned.',r'1\bmod1=0',['modulus','exponent','accumulator'],[1,0,0])])
flow(41,'Exact stipulated unsigned-eight-bit product compared with exact multiplication; real C promotions require separate analysis.',[('Follow the prematurely wrapped path.','Reducing modulo 251 cannot recover the missing product bits.',r'40000\bmod256=64',[{'label':'Exact product','value':'40000'},{'label':'8-bit stored product','value':'64'},{'label':'Then mod 251','value':'64'}]),('Follow the intended exact path.','The two output residues differ.',r'40000\bmod251=91',[{'label':'Exact product','value':'40000'},{'label':'Divide by 251','value':'159 · 251 + 91'},{'label':'Canonical residue','value':'91'}])])
arrays(42,'Exact input keys and two index-certificate candidates. Original positions identify equal records.',[('Check the stable certificate.','Index one supplies key one; equal-key indices zero then two preserve order.',r'c=[1,0,2]',[{'label':'Input keys at original indices','values':[5,1,5],'indices':True},{'label':'Output original-index certificate','values':[1,0,2],'indices':True}]),('Check the unstable alternative.','The same keys are output, but equal-key record identities reverse.',r'2>0',[{'label':'Sorted output keys','values':[1,5,5],'indices':True},{'label':'Rejected stability certificate','values':[1,2,0],'active':1,'indices':True}])])
flow(43,'The exact meeting value seventeen; feasibility and the universal lower bound play different roles.',[('Meet the lower and upper bounds.','This proves the value, not uniqueness of a solution.',r'17\le\text{OPT}\le17',[{'label':'Universal lower bound','value':'17'},{'label':'Optimal value','value':'17'},{'label':'Feasible witness cost','value':'17'}])])
for n,weights,distances,flags,description in[(44,[2,3,4],[0,2,5],[True,True,False],'Exact triangle; the direct edge to b violates the proposed distance.'),(45,[5,0,0],[0,0,0],[True,True,True],'Exact parent-cycle witness; all local inequalities pass but no zero-cost root path attains a or b.'),(46,[4,-3,5],[0,4,1],[True,True,True],'Exact negative-edge certificate; source-rooted attaining paths and all edge checks agree.'),(47,[2,-5,1],[0,2,-3],[True,True,False],'One illustrative finite labeling of the negative-total cycle. The summed contradiction proves that every finite labeling fails some edge.')]:
 nodes=[{'id':'s','x':145,'y':82,'value':distances[0],'label':'s'},{'id':'a','x':570,'y':82,'value':distances[1],'label':'a'},{'id':'b','x':570,'y':223,'value':distances[2],'label':'b'}]
 edges=([['s','a',weights[0],flags[0]],['a','b',weights[1],flags[1]],['b','a',weights[2],flags[2]] ]if n==45 else [['s','a',weights[0],flags[0]],['a','b',weights[1],flags[1]],['b','s',weights[2],flags[2]]]if n==47 else[['s','a',weights[0],flags[0]],['a','b',weights[1],flags[1]],['s','b',weights[2],flags[2]]])
 fs=[frame('graph','Inspect every displayed weighted edge.','Labels inside vertices are proposed distances; edge labels are costs. Red marks a failed local inequality, not an invalid graph edge.',r'\sum_{\text{cycle}}w=-2'if n==47 else r'd(v)\le d(u)+w(u,v)',nodes=nodes,graphEdges=edges,parentCycle=n==45,edgeFocus=k)for k in range(3)];scene(n,description,fs)
scene(48,'Exact half-open scheduling counterexample. Blue long interval conflicts with the three green compatible intervals.',[frame('intervals','Earliest start chooses the long interval.','The resulting one-interval schedule is feasible but not maximum-cardinality.',r'1<3',intervals=[[0,10],[1,2],[2,3],[3,4]],selected=[0]),frame('intervals','Choose all three short intervals.','Touching half-open endpoints are compatible, giving an attaining schedule of size three.',r'\text{OPT}=3',intervals=[[0,10],[1,2],[2,3],[3,4]],selected=[1,2,3])])
nodes=[{'id':'r','x':170,'y':57,'value':'1','label':'root'},{'id':'l','x':74,'y':123,'value':'1/2','label':'leaf'},{'id':'a','x':333,'y':123,'value':'1/2','label':'internal'},{'id':'q','x':247,'y':193,'value':'1/4','label':'leaf'},{'id':'b','x':492,'y':193,'value':'1/4','label':'internal'},{'id':'z','x':440,'y':263,'value':'1/8','label':'leaf'},{'id':'missing','x':646,'y':263,'value':'1/8','label':'missing','missing':True}]
tree(49,'A realizing finite tree for the complete depth list 1,2,3. The missing sibling is a budget, not an extra leaf.',[('Add only the three actual leaf budgets.',nodes,[['r','l'],['r','a'],['a','q'],['a','b'],['b','z'],['b','missing']],r'\frac78','The missing-child budget 1/8 explains the deficit and refutes fullness.')])
ledger(52,'Declared n=4 witness for the general odd-sum invariant, with every complete checkpoint shown.',[(f'After {k-1} additions.','The value relation and the index bound are both required to infer the final square.',r's=(k-1)^2',['k','s','guard','variant'],[k,(k-1)**2,'true'if k<=4 else'false',5-k])for k in range(1,6)])
scene(53,'Declared parent input [3,1] counterexample to sortedness-only child contracts. Left input [3] and right input [1] each return [0]. Both child results feed the merge.',[frame('tree','Merge two sorted child outputs that have lost their inputs.','Both dependency arrows converge on the parent output. Order alone did not preserve either original record.',r'\text{sorted}\not\Rightarrow\text{permutation}',nodes=[{'id':'left','x':235,'y':100,'label':'left child','value':'0'},{'id':'right','x':525,'y':100,'label':'right child','value':'0'},{'id':'output','x':380,'y':235,'label':'merge output','value':'0, 0'}],treeEdges=[['left','output'],['right','output']])])
arrays(54,'Exact all-negative singleton counterexample; the artificial zero candidate is explicitly outside the input.',[('Scan the admitted input.','Initialization best=0 introduces a value not present in the array.',r'\max(0,-2)=0',[{'label':'Input; best begins at zero','values':[-2],'active':0,'indices':True}]),('Return zero instead of the only input value.','A corrected nonempty-prefix initialization would return −2.',r'0\ne\max\{-2\}=-2',[{'label':'Correct attaining maximum','values':[-2],'active':0,'indices':True}])])
assert len(S)==54
db=R/'dist/chapters/concept-animations.json';data=json.loads(db.read_text(encoding='utf8'));container=data['scenes']if'scenes'in data else data;container.update(S);db.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(R/'research/deep-library-revision/a_correct-models.json').write_text(json.dumps({'topicId':'a_correct','models':S},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'models':len(S),'frames':sum(len(s['frames'])for s in S.values()),'kinds':sorted({f['snapshot']['kind']for s in S.values()for f in s['frames']})})
