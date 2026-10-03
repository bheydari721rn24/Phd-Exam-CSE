"""Finite semantics, proof constructions, set maps and graph transitions."""
import itertools,math
from common import *

def boolean(kind,title,formula,left,right,arity=2):
    frames=[]
    for values in itertools.product([0,1],repeat=arity):
        L=int(left(*values));R=int(right(*values));check(kind+' Boolean equivalence',L==R)
        nodes=[node('v'+str(i),chr(112+i)+' = '+str(v),110,70+i*85,w=125,tone='active') for i,v in enumerate(values)]
        nodes+=[node('left','Left = ?',375,100,w=180),node('right','Right = ?',375,240,w=180),node('equal','Check both',625,170,w=160)]
        edges=[{'from':'v'+str(i),'to':side,'directed':True} for i in range(arity) for side in ('left','right')]+[{'from':side,'to':'equal','directed':True} for side in ('left','right')]
        frames.append(frame(nodes,'Select this valuation and send its input bits to both expressions. Evaluation must use the same valuation on both sides.',{'Inputs':str(values),'Rows completed':len(frames)//2},formula=formula,line=0,edges=edges))
        nodes[-3]['label']='Left = '+str(L);nodes[-2]['label']='Right = '+str(R);nodes[-1].update(label='Equal',tone='done')
        frames.append(frame(nodes,'Evaluate both sides independently. Their equal outputs establish this truth-table row; the full finite table establishes the displayed Boolean identity.',{'Left output':L,'Right output':R},formula=formula,line=1,edges=edges,snapshot={'inputs':values,'left':L,'right':R}))
    return scene(kind,title,'Each input valuation is inspected and evaluated. The diagram shows expression dependencies rather than electrical propagation delay.',r'Both expressions receive exactly the same input valuation. All rows are checked, not sampled.',frames,['choose the next complete input valuation','evaluate both expressions and compare outputs'])

boolean('implication','Implication: the only false valuation',r'(p\Rightarrow q)\equiv(\neg p\lor q)',lambda p,q:not p or q,lambda p,q:not(p and not q))
boolean('de-morgan','De Morgan: complementing a composite expression',r'\neg(p\land q)\equiv\neg p\lor\neg q',lambda p,q:not(p and q),lambda p,q:not p or not q)
boolean('absorption','Absorption: why the extra product contributes nothing',r'p\lor(p\land q)\equiv p',lambda p,q:p or p and q,lambda p,q:p)
boolean('xor','XOR and parity: equal versus unequal inputs',r'p\oplus q\equiv(p\land\neg q)\lor(\neg p\land q)',lambda p,q:p!=q,lambda p,q:(p and not q)or(not p and q))
boolean('shannon','Shannon decomposition: select the correct cofactor',r'pq\lor\neg p\,r',lambda p,q,r:(p and q)or(not p and r),lambda p,q,r:q if p else r,3)
boolean('selectors','Minterms: one selected row per input assignment',r'pq\lor p\neg q\equiv p',lambda p,q:p and q or p and not q,lambda p,q:p)
boolean('nand-only','NAND completeness: composing an AND function',r'\neg\neg(pq)\equiv pq',lambda p,q:not(not(p and q)),lambda p,q:p and q)
boolean('consensus','Consensus: a redundant term removes a hazard without changing the truth table',r'pq\lor\neg p\,r\lor qr\equiv pq\lor\neg p\,r',lambda p,q,r:(p and q)or(not p and r)or(q and r),lambda p,q,r:(p and q)or(not p and r),3)

def quantifiers(order=False):
    frames=[];D=range(3)
    for outer in D:
        nodes=[node('x'+str(x),x,150,80+100*x,tone='active' if x==outer and not order else 'plain') for x in D]
        nodes+=[node('y'+str(y),y,600,80+100*y,tone='active' if y==outer and order else 'plain') for y in D]
        if order:
            edges=[{'from':'x'+str(x),'to':'y'+str(outer),'tone':'done' if x==outer else 'warning','directed':True} for x in D]
            caption='Try one fixed candidate for the existential outer quantifier. It fails for each different universally required input.'
            metrics={'Fixed candidate':outer,'Successful inputs':1,'Required inputs':3};broken=True
        else:
            edges=[{'from':'x'+str(x),'to':'y'+str(x),'tone':'active' if x==outer else 'plain','directed':True} for x in range(outer+1)]
            caption='For this universally chosen input, choose its equal value as a witness. The witness may depend on the input.'
            metrics={'Current input':outer,'Chosen witness':outer,'Inputs certified':outer+1};broken=False
        frames.append(frame(nodes,caption,metrics,formula=r'\exists y\,\forall x:\ y=x' if order else r'\forall x\,\exists y:\ y=x',edges=edges,counterexample=broken,status='Every fixed candidate is refuted by a different input in this domain.' if order else 'This input has a valid witness; all three inputs are eventually covered.'))
    return scene('quantifier-fixed' if order else 'quantifier-dependent','Quantifier order: '+('one fixed witness fails' if order else 'input-dependent witnesses succeed'),'The explicit domain is the three integers zero, one and two. This finite example illustrates the scope difference, not a claim about every possible predicate.',r'An outer existential witness must serve every universally required input; an inner existential witness may depend on the preceding input.',frames,['select the outer-quantifier value','inspect every required inner value'])
quantifiers();quantifiers(True)

def set_operation(kind):
    U=set(range(1,9));A={1,2,3,4};B={3,4,5,6}
    result={'union':A|B,'intersection':A&B,'difference':A-B,'symmetric':A^B,'complement':U-A,'set-demorgan':U-(A|B)}[kind]
    formula={'union':r'A\cup B','intersection':r'A\cap B','difference':r'A\setminus B','symmetric':r'A\triangle B','complement':r'A^c','set-demorgan':r'(A\cup B)^c=A^c\cap B^c'}[kind]
    frames=[];seen=[]
    for value in sorted(U):
        seen.append(value);nodes=[]
        for x in sorted(U):
            category=0 if x in A-B else 1 if x in A&B else 2 if x in B-A else 3
            base=[(140,95),(380,95),(620,95),(380,240)][category];within=sorted([k for k in U if (0 if k in A-B else 1 if k in A&B else 2 if k in B-A else 3)==category]).index(x)
            nodes.append(node('e'+str(x),x,base[0]+(within-.5)*68,base[1],w=56,tone='active' if x==value else 'done' if x in seen and x in result else 'muted' if x in seen else 'plain'))
        nodes +=[node('Aonly','A only',140,155,w=130,h=35,size=20),node('both','Both',380,155,w=120,h=35,size=20),node('Bonly','B only',620,155,w=130,h=35,size=20),node('outside','Neither',380,300,w=135,h=35,size=20)]
        selected=sorted(result.intersection(seen));check('set '+kind+' membership',all(x in U for x in selected))
        frames.append(frame(nodes,'Inspect the highlighted universe element, apply the membership rule, and retain it precisely when the requested operation includes it.',{'Inspected element':value,'In first set':str(value in A),'In second set':str(value in B),'Result so far':str(selected)},formula=formula,snapshot={'U':sorted(U),'A':sorted(A),'B':sorted(B),'result':selected,'inspected':seen[:]}))
    return scene('set-'+kind,kind.replace('-',' ').capitalize()+': classify every universe element','Positions separate the four disjoint membership regions. Green elements have been inspected and selected; muted elements have been inspected and excluded.',r'The four regions partition the explicit universe. Complements are taken relative to that same universe.',frames,['inspect one universe element','apply the exact operation membership condition'])
for k in ['union','intersection','difference','symmetric','complement','set-demorgan']:set_operation(k)

def selections(kind):
    universe=range(4);outcomes=list(itertools.permutations(universe,2)) if kind=='ordered' else list(itertools.combinations(universe,2)) if kind=='unordered' else list(itertools.combinations_with_replacement(universe,2))
    expected=12 if kind=='ordered' else 6 if kind=='unordered' else 10;check(kind+' selection count',len(outcomes)==expected);frames=[]
    for i,pair in enumerate(outcomes):
        nodes=array_nodes(list(universe),tones={x:'active' for x in pair},start=160,gap=145)
        nodes +=[node('first',pair[0],285,270,w=90,tone='done'),node('second',pair[1],475,270,w=90,tone='done')]
        frames.append(frame(nodes,'Construct the next '+('ordered pair without replacement' if kind=='ordered' else 'unordered pair without replacement' if kind=='unordered' else 'unordered pair with repetition')+'. The convention determines whether reversing or repeating values creates another outcome.',{'Outcome number':i+1,'Total outcomes':len(outcomes),'Current pair':str(pair)},snapshot={'outcomes':outcomes,'current':pair}))
    return scene('selection-'+kind,'Selections: '+kind+' pairs','The example chooses two entries from four labeled values. Every admitted outcome appears exactly once.',r'Ordered selections distinguish reversed positions; unordered selections use canonical nondecreasing representatives.',frames,['choose an admitted pair','count each distinct outcome exactly once'])
for k in ['ordered','unordered','repeated']:selections(k)

def powerset():
    frames=[];U=[1,2,3]
    for mask in range(8):
        subset=[v for i,v in enumerate(U) if mask>>i&1];nodes=array_nodes(U,start=220,gap=160,tones={i:'done' if mask>>i&1 else 'muted' for i in range(3)})
        frames.append(frame(nodes,'Choose one membership bit independently for each universe element. This mask identifies exactly one subset, including the empty subset.',{'Mask':format(mask,'03b'),'Subset':str(subset),'Subsets counted':mask+1},formula=r'|\mathcal P(U)|=2^3=8',snapshot={'mask':mask,'subset':subset}))
    return scene('powerset','Power set: independent membership choices','Each universe element has an include/exclude decision. The subsets are objects in a new set, not copies of the original elements.',r'One complete membership bit vector corresponds to exactly one subset.',frames,['choose a complete membership mask','materialize the corresponding subset'])
powerset()

def product():
    frames=[]
    for i,(a,b) in enumerate(itertools.product([1,2,3],[4,5])):
        nodes=[node('a'+str(x),x,160,80+85*(x-1),tone='active' if x==a else 'plain') for x in [1,2,3]]+[node('b'+str(y),y,560,110+110*(y-4),tone='active' if y==b else 'plain') for y in [4,5]]
        frames.append(frame(nodes,'Pair this first-coordinate choice with this second-coordinate choice. Coordinates keep their types and their order.',{'Pair':f'({a}, {b})','Pairs counted':i+1,'Total pairs':6},edges=[{'from':'a'+str(a),'to':'b'+str(b),'directed':True,'tone':'active'}]))
    return scene('cartesian','Cartesian product: two typed coordinates','The left and right sets occupy different columns. Reversing their roles would construct a different product.',r'Each output pair chooses exactly one element from each factor, with coordinate order preserved.',frames,['choose a left coordinate','choose a right coordinate and emit the ordered pair'])
product()

def induction(kind):
    frames=[]
    for n in range(0,7):
        if kind=='triangular':coordinates=[(i,j) for i in range(1,n+1) for j in range(i)];formula=rf'1+\cdots+{n}=\frac{{{n}({n}+1)}}2' if n else r'T_0=0';total=n*(n+1)//2
        else:coordinates=[(i,j) for i in range(n) for j in range(n)];formula=rf'1+3+\cdots+{2*n-1}={n}^2' if n else r'S_0=0';total=n*n
        check('induction '+kind+' exact shape count',len(coordinates)==total)
        nodes=[node('tile'+str(i)+'_'+str(j),'',160+j*55,45+i*43,w=36,h=32,tone='active' if i==(n if kind=='triangular' else n-1) or kind=='square' and j==n-1 else 'done') for i,j in coordinates]
        frames.append(frame(nodes,'Add the next '+('triangular row' if kind=='triangular' else 'odd-sized square border')+'. The new contribution transforms the established size into the next claimed size.',{'Parameter':n,'Total tiles':total,'Added tiles':n if kind=='triangular' else max(0,2*n-1)},formula=formula,snapshot={'n':n,'count':total}))
    return scene('induction-'+kind,'Induction: '+('triangular sums' if kind=='triangular' else 'odd sums form squares'),'The colored tiles display the constructive step. The animation checks finitely many instances; the quantified induction proof remains in the lesson.',r'The established smaller shape plus the new row or border equals the next claimed count.',frames,['establish the base shape','add the next row or border','identify the next closed-form total'])
induction('triangular');induction('square')

def induction_gap():
    frames=[];proved=set()
    for n in range(0,8,2):
        proved.add(n);nodes=array_nodes(range(8),start=50,gap=94,tones={i:'done' if i in proved else 'warning' if i%2 else 'plain' for i in range(8)})
        frames.append(frame(nodes,'A step of two from the zero base reaches only even indices. The odd chain needs its own base and cannot be silently assumed.',{'Established indices':str(sorted(proved)),'Uncovered odd indices':'1, 3, 5, 7'},counterexample=True,status='This proof scheme leaves the odd-index chain unestablished.'))
    return scene('induction-gap','Induction with a two-step rule: the missing odd base','One base and a step of two do not cover every nonnegative integer. Green marks only claims justified by this scheme.',r'Each valid two-step implication stays within one residue class; another residue class requires another base.',frames,['establish index zero','apply the two-step implication to an established index'])
induction_gap()

def strong_coins():
    known={8:[3,5],9:[3,3,3],10:[5,5]};frames=[]
    for n in range(8,21):
        if n not in known:known[n]=known[n-3]+[3]
        check('strong coin witness',sum(known[n])==n)
        nodes=array_nodes(known[n],start=90,gap=85,tones={i:'active' if i==len(known[n])-1 else 'done' for i in range(len(known[n]))})
        frames.append(frame(nodes,'Use an explicit base witness or add one three-unit coin to the already established value three smaller. The dependency is on an earlier claim.',{'Value':n,'Dependency':n-3 if n>10 else 'base case','Coin values':str(known[n])},formula=rf'{n}='+ '+'.join(map(str,known[n])),snapshot={'n':n,'coins':known[n]}))
    return scene('strong-coins','Strong induction: three and five-unit coin witnesses','Three consecutive bases cover every residue class modulo three. The text proves the general claim for every integer at least eight.',r'The listed coin values sum exactly to the current claim, and non-base claims depend on a smaller established value.',frames,['verify bases 8,9,10','use the established claim for n-3','append one coin of value 3'])
strong_coins()

def proof_chain(id,title,steps,invariant):
    frames=[]
    for i,(claim,formula,caption) in enumerate(steps):
        nodes=[node('assumption','Assumptions',150,75,w=195),node('claim',claim,510,75,w=295,h=80,size=21),node('step','Derived step '+str(i+1),380,255,w=210,tone='done' if i==len(steps)-1 else 'active')]
        frames.append(frame(nodes,caption,{'Derivation step':i+1,'Total steps':len(steps)},formula=formula,line=i,edges=[{'from':'assumption','to':'claim','directed':True},{'from':'claim','to':'step','directed':True}]))
    return scene(id,title,'Follow the dependency of each justified claim. This is a proof construction, not a numerical experiment offered as a universal proof.',invariant,frames,[s[0] for s in steps])
proof_chain('direct-even','Direct proof: an even integer has an even square',[
 ('n = 2k',r'n=2k','Unpack the definition of evenness by choosing an integer witness for the original assumption.'),
 ('Square the expression',r'n^2=4k^2','Substitute the witness into the square and expand in exact integer arithmetic.'),
 ('Exhibit an integer witness',r'n^2=2(2k^2)','The remaining coefficient is an integer, so this is exactly the required evenness definition.')],r'Every transformation follows from the original evenness witness and exact integer algebra.')
proof_chain('contrapositive','Contrapositive: proving the equivalent direction',[
 ('If n is even',r'\neg Q\Rightarrow\neg P','To prove that an odd square requires an odd input, take the equivalent contrapositive direction.'),
 ('Its square is even',r'n=2k\Rightarrow n^2=2(2k^2)','The even-input witness forces an even square, refuting the possibility of an odd square on that branch.'),
 ('Original implication follows',r'P\Rightarrow Q','The contrapositive is logically equivalent to the original implication; the converse is a different claim.')],r'The contrapositive changes both predicates by negation and reverses their order.')
proof_chain('sqrt-contradiction','Contradiction: a supposed reduced rational square root',[
 ('Assume a reduced fraction',r'\gcd(p,q)=1','Assume positive coprime integers represent the square root of two, so the fraction is in lowest terms.'),
 ('The numerator is even',r'p^2=2q^2\Rightarrow p=2k','Squaring the assumed equality forces the numerator square even, hence its integer numerator even.'),
 ('The denominator is even',r'q^2=2k^2\Rightarrow q=2j','Substitution of the even numerator forces the denominator even by the same parity argument.'),
 ('Common factor contradicts reduction',r'2\mid p\land2\mid q','Both integers now share factor two, contradicting the original lowest-terms assumption.')],r'Keep the reduced-fraction assumption throughout; the final shared divisor contradicts that specific assumption.')
proof_chain('weakest-precondition','Backward verification: transform the required final state',[
 ('Required final value',r'x=7','Begin with the required value after the entire sequence, before choosing any initial condition.'),
 ('Undo x = y - 3',r'y-3=7\Rightarrow y=10','Substitute the final assignment expression into the desired value and solve for its previous state.'),
 ('Undo y = 2x',r'2x=10\Rightarrow x=5','The preceding multiplication must establish the required intermediate value of the overwritten variable.'),
 ('Undo x = x + 1',r'x+1=5\Rightarrow x=4','The first increment determines the initial value. Forward execution from four reaches the required result.')],r'Substitute backward in reverse execution order, always referring to the state before the assignment being removed.')

def reachability(reflexive=False):
    N=4;R={(0,1),(1,2),(2,3)};frames=[]
    if reflexive:R|={(i,i) for i in range(N)}
    for k in range(N+1):
        new=set()
        if k:
            pivot=k-1
            for i in range(N):
                for j in range(N):
                    if (i,pivot) in R and (pivot,j) in R:new.add((i,j))
            R|=new
        nodes=[node('v'+str(i),i,120+170*i,65,w=55,tone='active' if k and i==k-1 else 'plain') for i in range(N)]
        nodes +=[node('m'+str(i)+str(j),int((i,j) in R),265+65*j,170+43*i,w=44,h=32,tone='active' if (i,j) in new else 'done' if (i,j) in R else 'muted') for i in range(N) for j in range(N)]
        edges=[{'from':'v'+str(i),'to':'v'+str(j),'directed':True,'tone':'active' if (i,j) in new else 'plain'} for i,j in R]
        frames.append(frame(nodes,'Admit '+('no intermediate vertex yet' if k==0 else 'vertex '+str(k-1)+' as an additional intermediate')+'. Add precisely the paths formed by joining two already admitted subpaths.',{'Admitted intermediates':k,'Reachable pairs':len(R),'Reflexive convention':str(reflexive)},edges=edges,snapshot={'relation':sorted(R),'admitted':k,'reflexive':reflexive}))
    expected={(i,j) for i in range(N) for j in range(N) if i<j or reflexive and i==j};check('reachability final closure',R==expected)
    return scene('reflexive-closure' if reflexive else 'transitive-closure','Reachability: '+('reflexive transitive' if reflexive else 'positive-length transitive')+' closure','The upper graph and lower adjacency matrix update together. This chain has no positive-length cycles; reflexive paths are a separate convention.',r'After processing a pivot, every added pair has a path whose intermediate vertices are among the processed pivots.',frames,['initialize the given directed edges','for each pivot k: add i→j when i→k and k→j exist'])
reachability();reachability(True)

def equivalence():
    frames=[]
    for upto in range(1,7):
        nodes=[]
        for v in range(1,7):
            processed=v<=upto;x=(230 if v%2 else 530) if processed else 80+110*(v-1);y=(95+70*((v-1)//2)) if processed else 310
            nodes.append(node('e'+str(v),v,x,y,w=65,tone='active' if v==upto else 'done' if processed else 'plain'))
        frames.append(frame(nodes,'Move the inspected integer into its remainder class modulo two. Equivalent values share exactly one block of the partition.',{'Inspected value':upto,'Remainder':upto%2,'Odd block':str([x for x in range(1,upto+1) if x%2]),'Even block':str([x for x in range(1,upto+1) if not x%2])},snapshot={'upto':upto}))
    return scene('equivalence-classes','Equivalence classes: building a disjoint partition','The equivalence relation is equality of remainder modulo two on the explicit set of six integers.',r'Each element belongs to one class; two elements are equivalent exactly when their class labels agree.',frames,['inspect one element','place it in its unique remainder class'])
equivalence()

def hasse():
    positions={1:(380,285),2:(210,170),3:(550,170),6:(380,55)};covers=[(1,2),(1,3),(2,6),(3,6)];frames=[]
    for k in range(1,5):
        nodes=[node(str(v),v,*positions[v],w=65,tone='active' if v in covers[k-1] else 'plain') for v in positions]
        frames.append(frame(nodes,'Add the next cover of the divisibility order. The omitted transitive edge from one to six is implied by an upward path.',{'Cover edges shown':k,'Meet of 2 and 3':1,'Join of 2 and 3':6},edges=[{'from':str(a),'to':str(b),'directed':True,'tone':'active' if i==k-1 else 'plain'} for i,(a,b) in enumerate(covers[:k])]))
    return scene('hasse','Hasse diagram: covers, meet and join','Upward paths represent divisibility among the positive divisors of six. Reflexive and transitive edges are suppressed in the Hasse drawing.',r'A cover has no intermediate distinct element in this order. Common upper and lower bounds are determined by upward reachability.',frames,['identify the divisibility relation','remove reflexive and implied transitive edges','read common lower and upper bounds'])
hasse()

def topological():
    edges={(0,1),(0,2),(1,3),(2,3)};done=[];remaining=set(range(4));frames=[]
    while remaining:
        available=sorted(v for v in remaining if not any(b==v and a in remaining for a,b in edges));check('topological available source',bool(available));v=available[0]
        nodes=[node('v'+str(x),x,130+165*x,100,tone='active' if x in available else 'plain') for x in remaining]+[node('v'+str(x),x,130+165*i,270,tone='done') for i,x in enumerate(done)]
        frames.append(frame(nodes,'Choose a currently zero-indegree vertex. Previously emitted vertices have already satisfied every prerequisite of remaining vertices.',{'Available vertices':str(available),'Next vertex':v,'Output prefix':str(done)},edges=[{'from':'v'+str(a),'to':'v'+str(b),'directed':True} for a,b in edges if a in remaining and b in remaining]))
        done.append(v);remaining.remove(v)
    check('topological order certificate',all(done.index(a)<done.index(b) for a,b in edges))
    frames.append(frame([node('v'+str(x),x,130+165*i,270,tone='done') for i,x in enumerate(done)],'Every vertex has been emitted. Each original directed edge points from an earlier output position to a later one.',{'Final order':str(done)},snapshot={'order':done,'edges':sorted(edges)}))
    return scene('topological','Topological scheduling: remove only satisfied prerequisites','The upper row contains remaining vertices; the lower row is the growing valid schedule.',r'Every emitted vertex has no remaining predecessor. A directed cycle would prevent completion.',frames,['find vertices with no remaining incoming edge','emit one available vertex and remove its outgoing constraints'])
topological()

def functions(mode):
    frames=[];mapping=[0,0,1]
    for k in range(3):
        nodes=[node('a'+str(i),chr(97+i),140,80+i*95,w=65,tone='active' if i==k else 'plain') for i in range(3)]+[node('b'+str(i),i,595,125+i*120,w=65,tone='active' if i==mapping[k] else 'plain') for i in range(2)]
        edges=[{'from':'a'+str(i),'to':'b'+str(mapping[i]),'directed':True,'tone':'active' if i==k else 'plain'} for i in range(k+1)]
        caption='Follow the selected source to its unique output. Distinct sources can share an output, so totality does not imply injectivity.' if mode=='fibers' else 'Inspect whether this source belongs to the preimage of output zero. A preimage contains sources, not output values.'
        metrics={'Source':chr(97+k),'Output':mapping[k],'Fiber of zero':'a, b','Surjective':'true','Injective':'false'}
        frames.append(frame(nodes,caption,metrics,edges=edges,snapshot={'mapping':mapping,'source':k}))
    return scene('function-'+mode,'Functions: '+('fibers, collisions and coverage' if mode=='fibers' else 'images and preimage membership'),'The declared domain has three values and the codomain has two. Every source has exactly one outgoing arrow.',r'Fibers partition the domain. Surjectivity asks that every codomain value have a nonempty fiber; injectivity asks each fiber have at most one element.',frames,['inspect one source','follow its single output arrow','collect sources with the selected output'])
functions('fibers');functions('preimages')

def inverse_choices():
    frames=[]
    for choice in [0,1]:
        nodes=[node('a'+str(i),chr(97+i),155,80+i*95,w=65,tone='done' if i in (choice,2) else 'plain') for i in range(3)]+[node('b'+str(i),i,600,125+i*120,w=65,tone='active') for i in range(2)]
        edges=[{'from':'b0','to':'a'+str(choice),'directed':True,'tone':'active'},{'from':'b1','to':'a2','directed':True,'tone':'active'}]
        frames.append(frame(nodes,'Choose one representative from each nonempty fiber. Composing the original surjection after this section returns the codomain input.',{'Representative for zero':chr(97+choice),'Representative for one':'c','Valid sections':2},formula=r'f\circ s=\operatorname{id}',edges=edges))
    return scene('right-inverse','Right inverses: two valid sections of one surjection','Reverse arrows choose representatives; they do not turn a noninjective function into a two-sided inverse.',r'A section selects one source in each fiber. The two-sided inverse additionally requires injectivity.',frames,['choose one representative of each fiber','verify f(section(y)) = y for both codomain inputs'])
inverse_choices()

def composition():
    frames=[];f=[0,1,0];g=[1,0]
    for k in range(3):
        nodes=[node('a'+str(i),i,100,80+95*i,w=60,tone='active' if i==k else 'plain') for i in range(3)]+[node('b'+str(i),i,380,125+120*i,w=60,tone='active' if i==f[k] else 'plain') for i in range(2)]+[node('c'+str(i),i,660,125+120*i,w=60,tone='done' if i==g[f[k]] else 'plain') for i in range(2)]
        frames.append(frame(nodes,'Apply the first function before the second. The intermediate codomain must be a valid input domain for the second function.',{'Input':k,'Intermediate':f[k],'Composed output':g[f[k]]},formula=rf'(g\circ f)({k})={g[f[k]]}',edges=[{'from':'a'+str(k),'to':'b'+str(f[k]),'directed':True,'tone':'active'},{'from':'b'+str(f[k]),'to':'c'+str(g[f[k]]),'directed':True,'tone':'active'}]))
    return scene('function-composition','Composition: typed paths through the intermediate set','Follow only one source at a time; the highlighted two-edge path determines its composed image.',r'Composition applies the rightmost function first, and the intermediate value must have the declared type.',frames,['evaluate f at the input','evaluate g at the intermediate result'])
composition()

def finite_functions():
    frames=[];surj=0
    for bits in itertools.product(range(2),repeat=3):
        surj+=len(set(bits))==2
        nodes=[node('a'+str(i),chr(97+i),140,80+95*i,w=65) for i in range(3)]+[node('b'+str(i),i,610,125+120*i,w=65,tone='done' if i in bits else 'muted') for i in range(2)]
        frames.append(frame(nodes,'Choose one output for every source. Distinct complete assignments define distinct total functions; surjectivity requires both outputs to be hit.',{'Assignment':str(bits),'Functions counted':len(frames)+1,'Surjections counted':surj},edges=[{'from':'a'+str(i),'to':'b'+str(bits[i]),'directed':True} for i in range(3)],snapshot={'mapping':bits,'surjective':len(set(bits))==2}))
    check('finite function count',len(frames)==8 and surj==6)
    return scene('function-count','Counting functions: total maps versus surjections','The example has a three-element domain and two-element codomain. All eight maps appear; the two constant maps are not surjective.',r'Each source independently chooses one output. Surjections are filtered by codomain coverage.',frames,['choose a complete output assignment','inspect whether every codomain value is hit'])
finite_functions()
