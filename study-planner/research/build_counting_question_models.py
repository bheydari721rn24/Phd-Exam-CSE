from pathlib import Path
import copy,itertools,json,math,sys
B=Path(__file__).parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
def frame(state,formula,caption):
 return dict(nodes=[],edges=[],snapshot=copy.deepcopy(state),caption=caption,captionHtml='<p>'+caption+'</p>',metrics={},formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True)+'</div>',line=0,teaching=dict(operation='Construct and check the displayed exact combinatorial state',why=caption,currentState=copy.deepcopy(state),initial=False,activeLine=0,checks=[],changes=[],reading='Read the exact objects, reversible encoding and running count. These are exhaustive or explicitly selected exact checkpoints, not sampled experimental evidence.'))
def scene(kind,title,description,frames):
 frames[0]['teaching']['initial']=True
 return dict(id='counting-question-'+kind,title=title,description=description,descriptionHtml='<p>'+description+'</p>',invariant='The displayed construction preserves the stated object labels, constraints and outcome definition.',visual=dict(type='enumeration',claim=description),code=['Build the declared outcome; apply its exact constraint; recover its unique encoding'],frames=frames)
models={};frames=[]
for i,(a,b) in enumerate(itertools.combinations(range(7),2)):
 tuple_=[a,b-a-1,6-b];tokens=['|' if j in (a,b) else '*' for j in range(7)]
 state=dict(kind='stars',bars=[a,b],tokens=tokens,tuple=tuple_,index=i+1,total=21)
 frames.append(frame(state,rf'(x_1,x_2,x_3)=({tuple_[0]},{tuple_[1]},{tuple_[2]}),\quad N=\binom72=21',f'Encoding {i+1} of 21. The two distinct separator slots are {a} and {b} (zero-based). Count stars in each named segment to recover {tuple_}. Five stars remain in every row; adjacent bars mean an empty coordinate. The separate pair totaling 15 always has 16 choices.'))
models['stars']=scene('stars','Question 1: all 21 triple encodings','Two movable separator positions enumerate every nonnegative triple totaling five exactly once. Slot numbers identify the encoding; bars are separators, not objects being distributed.',frames)
frames=[];counts=[20,20,19,19,18]
for b in range(5):
 upper=(39-b)//2;state=dict(kind='parity',active=b,counts=counts,upper=[19,19,18,18,17],prefix=sum(counts[:b+1]),aValues=list(range(0,2*upper+1,2)))
 frames.append(frame(state,rf'b={b},\quad 0\le j\le {upper},\quad c={40-b}-2j,\quad \text{{prefix}}={sum(counts[:b+1])}',f'Fix b={b}. The original lower bound c>=1 gives 2j+c=40-b, so j runs inclusively from zero through {upper}. Each of the {counts[b]} even a values produces exactly one c. Accumulating these disjoint b rows reaches 96.'))
models['parity']=scene('parity','Question 9: parity and lower-bound ledger','Each row fixes b, lists the even a values and determines c. The count changes at floor endpoints; all five rows together give the exact answer 96.',frames)
frames=[];terms=[4096,-2916,384,-4,0]
for j in range(5):
 state=dict(kind='onto',stage=j,terms=terms,prefix=sum(terms[:j+1]),labels=['all maps','one missing','two missing','three missing','four missing'])
 frames.append(frame(state,rf'\sum_{{i=0}}^{{{j}}}(-1)^i\binom4i(4-i)^6={state["prefix"]}',f'Include missing-set size {j}. Its signed contribution is {terms[j]}, counting all selected missing-target sets. The partial total is {state["prefix"]}. Intermediate totals are inclusion-exclusion approximations, not counts of a separately defined event. After all intersections the onto count is 1560.'))
models['onto']=scene('onto','Question 7: every missing-target correction','Signed contributions use the exact map counts for four named targets. The restored intersections explain why subtracting only singleton exclusions is inadequate.',frames)
frames=[];values=[1,2,3,5,8,13,21,34,55]
for n in range(9):
 words=[''.join(map(str,w)) for w in itertools.product([0,1],repeat=min(n,5)) if all(not(w[i]==w[i+1]==1) for i in range(len(w)-1))]
 state=dict(kind='dp',n=n,values=values,words=words,examplesLength=min(n,5))
 formula=rf'T_{n}={values[n]}' if n<2 else rf'T_{n}=T_{{{n-1}}}+T_{{{n-2}}}={values[n-1]}+{values[n-2]}={values[n]}'
 frames.append(frame(state,formula,f'Length {n} has {values[n]} admissible words. '+('The empty word has one construction.' if n==0 else 'At length one the direct words are 0 and 1.' if n==1 else 'Deleting prefix 0 leaves length n-1; deleting forced prefix 10 leaves length n-2. These branches are disjoint.')+(' The word examples below are the complete length-five set, retained as a reference rather than claimed to enumerate this larger length.' if n>5 else ' Every word at this length is listed below.')))
models['dp']=scene('dp','Question 40: prefix recurrence and explicit words','The recurrence grows from its exact two seeds. All words are listed through length five; later checkpoints show computed recurrence counts with an explicitly labeled length-five reference.',frames)
def pairings(xs):
 if not xs:yield [];return
 for j in range(1,len(xs)):
  for rest in pairings(xs[1:j]+xs[j+1:]):yield [(xs[0],xs[j])]+rest
allpairs=list(pairings(list(range(1,9))));frames=[]
for i in [0,1,2,14,44,74,104]:
 pairs=allpairs[i];state=dict(kind='pairing',pairs=pairs,index=i+1,total=105)
 frames.append(frame(state,r'M_4=7\cdot5\cdot3\cdot1=105',f'Exact pairing {i+1} of 105 in smallest-remaining-label enumeration: '+', '.join(f'{a}-{b}' for a,b in pairs)+'. At each stage the smallest unpaired label chooses one partner. The branch factors are 7,5,3,1. Seven selected checkpoints illustrate distinct outcomes; the independent verification enumerates all 105.'))
models['pairing']=scene('pairing','Question 71: pairs as actual edges','Eight labeled vertices and four connecting edges represent one real pairing. Edges terminate at vertex boundaries. Crossing edges do not change pair membership; the collection has no order.',frames)
frames=[];words=[''.join(map(str,w)) for w in itertools.product([0,1],repeat=3)]
for k in range(4):
 state=dict(kind='report',k=k,words=words,counts=[1,3,3,1])
 frames.append(frame(state,rf'P(K={k})=\frac{{{math.comb(3,k)}}}8',f'The highlighted words have exactly {k} ones. There are {math.comb(3,k)} preimages of this multiset report, each of mass 1/8. Summaries with counts 0,1,2,3 therefore have probabilities 1/8,3/8,3/8,1/8.'))
models['report']=scene('report','Question 77: all ordered preimages of a multiset','The eight equiprobable words stay visible. Highlighting a count identifies the detailed outcomes merged into that report and its exact induced probability.',frames)
p=R/'dist/chapters/concept-animations.json';data=json.loads(p.read_text());data['scenes'].update({s['id']:s for s in models.values()});p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print({k:len(v['frames']) for k,v in models.items()})
