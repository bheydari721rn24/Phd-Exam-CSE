"""Original exact conditional models, not decorative motion or copied lectures."""
from common import node,frame,scene,check
from fractions import Fraction as F
from itertools import product

def rows(labels,tones=None):
    return [node(str(i),label,150+(i%2)*450,80+(i//2)*170,w=245,h=78,tone=(tones or {}).get(i,'plain'),size=23) for i,label in enumerate(labels)]

frames=[]
for phase,labels,tones,cap in [
    ('Original weights',['atom 1: 1/10','atom 2: 2/10','atom 3: 3/10','atom 4: 4/10'],{},'Begin with unequal atom weights. Every original atom contributes its own mass, so counting atoms alone would not calculate a probability.'),
    ('Retain B',['atom 1: 1/10','atom 2: 2/10','excluded from B','excluded from B'],{0:'active',1:'active'},'The information event retains atoms one and two. Their combined mass is three tenths; the other original atoms are incompatible with the observation.'),
    ('Renormalize',['atom 1: 1/3','atom 2: 2/3','conditional mass 0','conditional mass 0'],{0:'done',1:'done'},'Divide every retained atom mass by three tenths. The relative ratio one to two remains unchanged, while the new total mass becomes one.'),
    ('Target within B',['A and B: 1/3','B without A: 2/3','conditional mass 0','conditional mass 0'],{0:'active',1:'done'},'The target A contains atom one among the retained outcomes. Its conditional probability is therefore one third, not one half.')]:
    masses=[F(1,10),F(2,10),F(3,10),F(4,10)] if phase=='Original weights' else [F(1,3),F(2,3),F(0),F(0)] if phase in ['Renormalize','Target within B'] else [F(1,10),F(2,10),F(0),F(0)]
    nodes=rows(labels,tones)
    if phase!='Original weights':
        for i,n in enumerate(nodes):
            n['x']=220+i*320 if i<2 else 220+(i-2)*320
            n['y']=130 if i<2 else 280
    frames.append(frame(nodes,cap,{'Phase':phase,'Original information mass':'3/10','Conditional target':'1/3'},formula=r'P(A\mid B)=\frac{1/10}{3/10}=\frac13',snapshot={'phase':phase,'masses':list(map(str,masses))}))
scene('conditional-atoms','Unequal atoms: retain, normalize, select','Conditioning changes the mass scale, not the relative weights of retained outcomes.','The original atom probabilities are $(1,2,3,4)/10$, and $B$ retains the first two.',frames)

frames=[]
for labels,cap,value in [
    (['00: mass 1/4','01: mass 1/4','10: mass 1/4','11: mass 1/4'],'The full two-bit sample space has four equal atoms. The target equality event depends on both coordinates, not just the last observed coordinate.',F(1)),
    (['00 excluded','01 excluded','10: A holds','11: A holds'],'Observe the first bit equal to one. The surviving prefix event A has probability one half and retains two possible second-bit outcomes.',F(1,2)),
    (['00 excluded','01 excluded','10 excluded','11: A and B'],'Observe the second bit equal to one as well. The full prefix contains just state eleven, so the equality target is now certain.',F(1,4)),
    (['Full history: 1','B alone: 1/2','correct joint: 1/4','wrong joint: 1/8'],'Compare the final factors under different information. Keeping both previous observations gives one; deleting the first observation gives one half and halves the joint answer.',F(1,4))]:
    frames.append(frame(rows(labels),cap,{'Prefix mass':str(value),'Correct triple':'1/4','Abbreviated product':'1/8'},formula=r'P(A\cap B\cap C)=\frac12\cdot\frac12\cdot1=\frac14',snapshot={'prefix':str(value)}))
scene('conditional-history','A chain factor must keep the complete history','The equality event gives a minimal counterexample to dropping the first observation.','The two bits are independent and fair; $A$ fixes the first bit and $B$ the second to one.',frames)

frames=[];mass=F(1);r,b=4,3;removed=[]
for k,color in enumerate([None,'red','blue','red']):
    if color:
        factor=F(r if color=='red' else b,r+b);mass*=factor
        if color=='red':r-=1
        else:b-=1
    if color:removed.append([0,4,1][k-1])
    nodes=[node('ball'+str(i),('R'+str(i+1)) if i<4 else ('B'+str(i-3)),70+i*100 if i not in removed else 220+removed.index(i)*160,90 if i not in removed else 255,w=70,h=54,tone='done' if i in removed else 'plain') for i in range(7)]
    nodes+=[node('remaining','Remaining urn',380,35,w=240,h=30,size=20),node('drawn','Observed color prefix',380,330,w=270,h=30,size=20)]
    frames.append(frame(nodes,'Move one representative object of the observed color into the prefix row. This movement records color counts; the displayed probability sums all equivalent labeled choices of that color.',{'Draws completed':k,'Red remaining':r,'Blue remaining':b,'Remaining total':r+b,'Prefix mass':str(mass)},formula=r'P(RBR)=\frac47\cdot\frac36\cdot\frac35=\frac6{35}',snapshot={'red':r,'blue':b,'draws':k,'mass':str(mass)}))
check('conditional RBR exact',mass==F(6,35))
scene('conditional-urn','Without replacement: remaining counts and path mass','The ordered red-blue-red example tracks the entire urn state after each draw.','Every draw is uniform among the remaining distinct objects. The original urn has four red and three blue objects.',frames)

frames=[]
for labels,cap in [
    (['type 1 weight: 1/2','type 2 weight: 1/2','success rate: 9/10','success rate: 1/10'],'Two types are initially equally likely. The checks are independent within a known type, with the displayed type-specific success rates.'),
    (['type 1 joint: 9/20','type 2 joint: 1/20','first success: 1/2','rate within type fixed'],'First success weights the type-one branch nine times as strongly as the type-two branch. Add these joint masses to obtain the observation denominator.'),
    (['type 1 given pass: 9/10','type 2 given pass: 1/10','second joint: 41/100','second given first: 41/50'],'Renormalize the type weights after the observation. Conditional independence keeps the rates fixed inside types, but their new mixture changes the next-check probability.')]:
    frames.append(frame(rows(labels),cap,{'First-check marginal':'1/2','Second-check marginal':'1/2','Joint success':'41/100','Second given first':'41/50'},formula=r'P(B\mid A)=\frac{41/100}{1/2}=\frac{41}{50}',snapshot={'joint':'41/100','marginal':'1/2'}))
scene('conditional-mixture','Independent within types, dependent after mixing','A shared hidden type changes the joint law even though the within-type checks factor.','Types have equal prior weight; within-type rates are $9/10$ and $1/10$.',frames)

frames=[]
for mode,retained,cap in [
    ('Original',[True]*4,'Start with four equally likely bit pairs. The independent success marginals each equal one half and their joint mass equals one quarter.'),
    ('Equal bits',[True,False,False,True],'Condition on equal bits and retain only zero-zero and one-one. Each marginal stays one half, but joint success becomes one half and independence fails.'),
    ('At least one',[False,True,True,True],'Condition instead on at least one success. Three pairs remain, giving success marginals two thirds and joint one third, below the independent product.')]:
    pairs=list(product([0,1],repeat=2));total=sum(retained);a=F(sum(keep*x for keep,(x,y) in zip(retained,pairs)),total);b=F(sum(keep*y for keep,(x,y) in zip(retained,pairs)),total);joint=F(sum(keep*x*y for keep,(x,y) in zip(retained,pairs)),total)
    nodes=rows([f'{x}{y}: '+(str(F(1,total)) if keep else 'excluded') for (x,y),keep in zip(pairs,retained)],{i:'active' for i,keep in enumerate(retained) if keep})
    frames.append(frame(nodes,cap,{'Selection':mode,'A marginal':str(a),'B marginal':str(b),'Joint':str(joint),'Product':str(a*b)},formula=r'P(A\cap B\mid C)\ne P(A\mid C)P(B\mid C)' if mode!='Original' else r'P(A\cap B)=P(A)P(B)',snapshot={'retained':retained,'a':str(a),'b':str(b),'joint':str(joint)},counterexample=mode!='Original'))
scene('conditional-selection','Selection changes independence','Changing the information event changes both the retained states and their probability relationships.','The original coordinates are independent fair bits; each new view explicitly conditions on its stated selection event.',frames)

frames=[]
for mode,weights,cap in [
    ('Within strata',None,'Compare success rates inside each separate stratum. Method A exceeds method B by one tenth in both easy and hard cases.'),
    ('Actual allocation',(F(1,10),F(9,10)),'Give method A mostly hard cases and method B mostly easy cases. Their aggregate rates reverse because each method uses a different mixture.'),
    ('Common allocation',(F(1,2),F(1,2)),'Use the same mixture for both methods. The positive within-stratum difference is preserved by common weighted addition, so the reversal disappears.')]:
    rates=(F(9,10),F(2,5),F(4,5),F(3,10));ra=weights[0]*rates[0]+(1-weights[0])*rates[1] if weights else None;rb=weights[1]*rates[2]+(1-weights[1])*rates[3] if weights else None
    frames.append(frame(rows(['A easy: 9/10','B easy: 4/5','A hard: 2/5','B hard: 3/10']),cap,{'View':mode,'A aggregate':str(ra) if ra is not None else 'separate strata','B aggregate':str(rb) if rb is not None else 'separate strata','A easy weight':str(weights[0]) if weights else 'not aggregated','B easy weight':str(weights[1]) if weights else 'not aggregated'},formula=r'P(S\mid A)=\frac9{20}<\frac34=P(S\mid B)' if mode=='Actual allocation' else r'\frac9{10}>\frac45,\quad\frac25>\frac3{10}',snapshot={'weights':list(map(str,weights)) if weights else [],'a':str(ra),'b':str(rb)}))
scene('conditional-simpson','Simpson reversal: rates and case weights','Exact rates are compared before and after the methods receive different case mixtures.','Within each stratum A is better; a common mixture preserves that order.',frames)

frames=[]
for mode,likelihoods,cap in [
    ('At least one reports',[F(0),F(1),F(1),F(1)],'A monitor reports whenever at least one sensor is active. Three states produce the message with equal likelihood, so the both-active probability is one third.'),
    ('A chosen sensor reports',[F(0),F(1,2),F(1,2),F(1)],'Choose one sensor uniformly and report only if it is active. Single-active states now produce the message only half as often as the both-active state.'),
    ('Renormalized chosen report',[F(0),F(1,2),F(1,2),F(1)],'Normalize the reporting-weighted masses for the chosen-sensor protocol. Both-active now has conditional probability one half, despite the message remaining truthful.')]:
    mass=sum(likelihoods,F(0))/4;post=[v/4/mass for v in likelihoods]
    frames.append(frame(rows([f'{x}{y}: report {v}\nposterior {post[i]}' for i,((x,y),v) in enumerate(zip(product([0,1],repeat=2),likelihoods))]),cap,{'Protocol':mode,'Message mass':str(mass),'Both given report':str(post[-1])},formula=rf'P(11\mid M)={post[-1]}',snapshot={'likelihoods':list(map(str,likelihoods)),'posteriors':list(map(str,post))}))
scene('conditional-report','Truthful reports can assign different state weights','The monitor procedure is part of the sample space, not an optional interpretation.','The original states have equal mass $1/4$; the displayed report likelihoods define each protocol.',frames)

def connected(bits):
    adj={i:[] for i in range(4)}
    for bit,(a,b) in zip(bits,[(0,1),(1,3),(0,2),(2,3),(1,2)]):
        if bit:adj[a].append(b);adj[b].append(a)
    seen={0};todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return 3 in seen
frames=[];wins=0
for k,bits in enumerate(product([0,1],repeat=5),1):
    works=connected(bits);wins+=works
    nodes=[node('s','source',80,180,w=110),node('u','upper',380,60,w=100),node('l','lower',380,300,w=100),node('t','destination',680,180,w=135)]
    edges=[{'from':a,'to':b,'tone':'active' if bit else 'warning','dashed':not bit} for bit,(a,b) in zip(bits,[('s','u'),('u','t'),('s','l'),('l','t'),('u','l')])]
    frames.append(frame(nodes,'Inspect this exact five-edge configuration: solid gold edges work and dashed red edges fail. Determine whether a working path joins source and destination before adding its atom mass.',{'Edge bits in stated order':''.join(map(str,bits)),'Connected':works,'Configurations inspected':k,'Working configurations so far':wins,'Each configuration mass':'1/32'},formula=r'R(1/2)=\frac{16}{32}=\frac12',edges=edges,snapshot={'bits':list(bits),'connected':works,'wins':wins,'inspected':k}))
check('bridge sixteen working configurations',wins==16)
scene('conditional-bridge','Bridge reliability: all 32 exact edge states','Five fair independent edge states are enumerated; solid gold means working and dashed red means failed.','Edge order is source-upper, upper-destination, source-lower, lower-destination, upper-lower. Each atom has mass $1/32$.',frames)

frames=[]
for epsilon in [F(1,4),F(1,8),F(1,16),F(1,32)]:
    y=F(1,2);mass=2*y*epsilon+epsilon**2;target=y*epsilon;ratio=target/mass
    nodes=[node('strip',f'strip width {epsilon}',200,100,w=270),node('den',f'strip mass {mass}',560,100,w=245),node('target',f'target mass {target}',200,260,w=270),node('ratio',f'conditional {ratio}',560,260,w=245)]
    frames.append(frame(nodes,'Shrink a positive-width strip around the fixed interior observation. Its target mass and total mass both shrink, while their ratio approaches one half without dividing by a null line.',{'Fixed y':'1/2','Strip width':str(epsilon),'Conditional ratio':str(ratio),'Limit':'1/2'},formula=r'\frac{y\varepsilon}{2y\varepsilon+\varepsilon^2}=\frac{y}{2y+\varepsilon}',snapshot={'epsilon':str(epsilon),'mass':str(mass),'target':str(target),'ratio':str(ratio)}))
scene('conditional-strip','A positive strip approaches a continuous observation','The joint density is two on the triangle zero less than X less than Y less than one.',r'For fixed $y=1/2$, the target is $X\le y/2$ and the strip is $y\le Y\le y+\varepsilon$. Every checkpoint has positive strip mass.',frames)
