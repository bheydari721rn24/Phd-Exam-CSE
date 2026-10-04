"""Exact original Bayes models; each visible state carries its rational snapshot."""
from fractions import Fraction as F
from math import factorial
from common import node,frame,scene,check

def mass_nodes(values,heading,y=145):
    # Segments share a fixed probability axis; labels remain in separate rows.
    nodes=[node('heading',heading,380,40,w=620,h=38,size=20)]
    left=90
    for i,v in enumerate(values):
        w=580*float(v)
        nodes.append(node('mass'+str(i),'',left+w/2,y,w=max(w,1),h=54,tone='done' if i==0 else 'active' if i==1 else 'plain'))
        nodes.append(node('label'+str(i),f'H{i+1}: {v}',140+i*235,245,w=215,h=46,size=21))
        left+=w
    return nodes

priors=[F(1,2),F(1,3),F(1,6)];likelihoods=[F(1,10),F(1,5),F(3,5)]
weights=[p*l for p,l in zip(priors,likelihoods)];z=sum(weights);post=[w/z for w in weights]
frames=[]
for k in range(4):
    retained=[weights[i] if i<k else F(0) for i in range(3)]
    nodes=[node('H'+str(i),f'H{i+1}: prior {p}',140+i*235,65,w=205) for i,p in enumerate(priors)]+[node('mass'+str(i),f'joint {retained[i]}',140+i*235,210,w=205,tone='done' if i<k else 'plain') for i in range(3)]
    frames.append(frame(nodes,'Include the next disjoint source contribution without double-counting any observation. The accumulated evidence grows by that source prior times its alert likelihood.',{'Included sources':k,'Evidence accumulated':str(sum(retained))},formula=r'P(E)=\sum_i P(H_i)P(E\mid H_i)',snapshot={'included':k,'weights':list(map(str,retained)),'evidence':str(sum(retained))}))
scene('bayes-partition','Accumulate the disjoint evidence masses','Three sources contribute separate pieces of the same alert event.','Only the three specified disjoint source classes contribute; uninspected terms are not declared impossible.',frames)

frames=[]
for values,heading in [(priors,'Original prior mass'),(weights,'Retained joint mass on the original unit axis'),(post,'Normalize retained mass to one'),(post,'Posterior: all three normalized components sum to one')]:
    frames.append(frame(mass_nodes(values,heading),'The segment widths display exact probability masses on one shared axis. Evidence weighting removes different fractions of each source, then one common normalization expands the retained evidence to unit mass.',{'Evidence probability':str(z),'Displayed total':str(sum(values))},formula=r'r_i=\frac{\pi_iL_i}{\sum_j\pi_jL_j}',snapshot={'values':list(map(str,values)),'heading':heading}))
scene('bayes-normalize','Prior, retained mass, posterior','Probability-width segments demonstrate what weighting and normalization actually change.','The fixed source likelihoods are one tenth, one fifth and three fifths; every posterior uses the same evidence denominator.',frames)

frames=[]
for positive in [False,True]:
    for stage in ['population','retained','normalized']:
        values=[F(1,100),F(99,100)] if stage=='population' else ([F(9,1000),F(99,2000)] if positive else [F(1,1000),F(1881,2000)])
        den=sum(values)
        if stage=='normalized':values=[v/den for v in values]
        label='Positive' if positive else 'Negative'
        nodes=mass_nodes(values,f'{label} report: {stage}')
        frames.append(frame(nodes,'Retain the target and background counts compatible with this report. The selected population is then renormalized; its class proportions are different from the original prevalence.',{'Report':label,'Stage':stage,'Target count':18 if positive else 2,'Background count':99 if positive else 1881},snapshot={'positive':positive,'stage':stage,'values':list(map(str,values))}))
scene('bayes-frequencies','Positive and negative selected populations','The synthetic detector represents two thousand weighted cases.','Target prevalence is one hundredth; positive rates are nine tenths and one twentieth. Counts are exact scaled model weights, not a random sample guarantee.',frames)

frames=[]
for p in [F(1,100),F(1,20),F(1,10),F(1,4),F(1,2),F(3,4)]:
    r=4*p/(1+3*p)
    frames.append(frame(mass_nodes([r,1-r],f'Prior varies; likelihood ratio remains four'),'Move the prior while holding the two observation likelihoods fixed. The posterior increases continuously with prevalence, but the evidence model itself does not change.',{'Prior':str(p),'Posterior':str(r),'Likelihood ratio':4},formula=r'g(p)=\frac{4p}{1+3p}',snapshot={'p':str(p),'posterior':str(r)}))
scene('bayes-sensitivity','Base-rate sensitivity at fixed rates','Increasing prevalence shifts the posterior probability segments.','Target and background observation probabilities are four fifths and one fifth. All shown priors are interior rational values.',frames)

frames=[]
for n in range(6):
    odds=F(4**n,9);r=odds/(1+odds)
    frames.append(frame(mass_nodes([r,1-r],f'{n} independent positive reports'),'Each new independent report under the same fixed class multiplies the prior odds by four. The probability segments approach one without making a finite posterior equal to one.',{'Reports':n,'Posterior odds':str(odds),'Posterior':str(r)},formula=r'O_n=\frac{4^n}{9}',snapshot={'n':n,'odds':str(odds),'posterior':str(r)}))
scene('bayes-repeat','Independent positives multiply odds','The exact independent-report model follows one shared latent class.','Prior target probability is one tenth; class-specific positive rates are four fifths and one fifth. Conditional independence is assumed, not inferred from repetition.',frames)

frames=[]
for n in range(4):
    independent=F(1,10) if n==0 else F(4**n,9+4**n)
    duplicate=F(1,10) if n==0 else F(4,13)
    nodes=[node('title',f'{n} displayed reports',380,40,w=590,size=21),node('ind',f'independent: {independent}',190,120,w=295),node('dup',f'copied: {duplicate}',570,120,w=285),node('ind-point','',90+250*float(independent),240,w=16,h=40,tone='done'),node('dup-point','',430+250*float(duplicate),240,w=16,h=40,tone='warning'),node('ind-axis','probability axis: 0 to 1',210,310,w=300,size=19),node('dup-axis','probability axis: 0 to 1',550,310,w=300,size=19)]
    frames.append(frame(nodes,'Compare new measurements with repeated display of the same measurement. In the copied branch the second and later messages add no likelihood information after the original report.',{'Independent posterior':str(independent),'Copied-report posterior':str(duplicate)},snapshot={'n':n,'independent':str(independent),'duplicate':str(duplicate)}))
scene('bayes-copy','Repeated evidence versus repeated text','Two probability markers diverge when messages carry different information.','The first report has the same detector model in both branches; only the conditional dependence of later reports differs.',frames)

frames=[]
for n in range(5):
    w0=F(1,2)**n;w1=F(9,10)**n;r=w1/(w0+w1);predict=(1-r)*F(1,2)+r*F(9,10)
    nodes=mass_nodes([r,1-r],f'{n} heads: posterior biased-coin weight')
    nodes.append(node('predict',f'next head: {predict}',380,315,w=570,size=22))
    frames.append(frame(nodes,'Update which fixed coin was selected, then average both next-head rates under those posterior weights. The most probable coin alone does not determine the predictive distribution.',{'Heads':n,'Biased posterior':str(r),'Next-head probability':str(predict)},snapshot={'n':n,'biased':str(r),'predictive':str(predict)}))
scene('bayes-predict','Infer a fixed coin, then predict a toss','Posterior type weights and next-head probabilities are separately displayed.','A fair coin and a nine-tenths-head coin have equal priors and are selected once. Tosses are independent conditional on that fixed identity.',frames)

frames=[]
for q in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
    r=1/(1+q)
    nodes=[node('door1',f'prize 1\nlikelihood {q}',145,80,w=230,h=64),node('door2','prize 2\nlikelihood 1',380,80,w=220,h=64),node('door3','prize 3\nlikelihood 0',615,80,w=220,h=64,tone='warning'),node('stay',f'stay: {1-r}',220,230,w=300,tone='plain'),node('switch',f'switch: {r}',560,230,w=300,tone='done')]
    frames.append(frame(nodes,'Vary the informed host tie-breaking probability while keeping the prize prior uniform. The specific report that door three is opened reweights prize locations by different reporting likelihoods.',{'Host tie-breaking q':str(q),'Switch posterior':str(r),'Unconditional switch':str(F(2,3))},formula=r'P(\text{prize 2}\mid\text{open 3})=\frac{1}{1+q}',snapshot={'q':str(q),'switch':str(r)}))
scene('bayes-host','The host protocol changes a specific-report posterior','Three door hypotheses respond to asymmetric report likelihoods.','Door one was initially chosen; the knowledgeable host always opens an empty unchosen door. q is the probability of opening door three when door one hides the prize.',frames)

frames=[]
for cfn in [F(1),F(2),F(4),F(9),F(20)]:
    r=F(2,13);threshold=1/(1+cfn);target=1-r;background=cfn*r
    nodes=[node('post',f'posterior fixed: {r}',380,50,w=590),node('target',f'target risk: {target}',200,150,w=320,tone='done' if target<=background else 'plain'),node('background',f'background risk: {background}',560,150,w=320,tone='done' if background<=target else 'plain'),node('threshold',f'target threshold: {threshold}',380,275,w=600)]
    frames.append(frame(nodes,'Increase the false-negative cost while preserving the same posterior probability. The action changes only when its conditional risk crosses the competing action risk.',{'False-positive cost':1,'False-negative cost':str(cfn),'Optimal action':'target' if target<background else 'background' if target>background else 'tie'},snapshot={'cfn':str(cfn),'threshold':str(threshold),'targetRisk':str(target),'backgroundRisk':str(background)}))
scene('bayes-loss','Costs change decisions, not posterior beliefs','Two posterior risks cross as one error cost varies.','Posterior target probability stays two thirteenths, false-positive cost is one, and correct decisions have zero cost.',frames)

frames=[]
for h,t in [(0,0),(1,0),(2,0),(2,1),(2,2),(3,2)]:
    norm=F(factorial(h)*factorial(t),factorial(h+t+1));nodes=[]
    for j in range(11):
        x=F(j,10);density=x**h*(1-x)**t/norm
        nodes.append(node('p'+str(j),'',90+j*58,285-65*float(density),kind='point',w=14,h=14))
    nodes += [node('title',f'heads {h}, tails {t}',380,35,w=600,h=35),node('axis','parameter from zero to one',380,320,w=410,h=30,size=18),node('origin','',90,285,kind='point'),node('x-end','',670,285,kind='point'),node('y-end','',90,70,kind='point'),node('zero','0',90,315,w=30,h=24,size=16),node('one','1',670,315,w=30,h=24,size=16)]
    nodes += [node('density'+str(j),str(j),60,285-65*j,w=26,h=24,size=16) for j in range(4)]
    edges=[{'from':'p'+str(j),'to':'p'+str(j+1),'tone':'active'} for j in range(10)]+[{'from':'origin','to':'x-end'},{'from':'origin','to':'y-end'}]
    frames.append(frame(nodes,'Apply the next stated toss outcome to the continuous coin-rate likelihood and renormalize its density. Points show exact density samples, while probability requires an interval integral.',{'Heads':h,'Tails':t,'Likelihood integral':str(norm),'Next-head predictive':str(F(h+1,h+t+2))},formula=r'\pi(\theta\mid h,t)=\frac{\theta^h(1-\theta)^t}{I(h,t)}',edges=edges,snapshot={'h':h,'t':t,'integral':str(norm),'densities':[str(F(j,10)**h*(1-F(j,10))**t/norm) for j in range(11)]}))
scene('bayes-density','Likelihood weighting reshapes a parameter density','Exact sampled density heights evolve after specified coin outcomes.','The prior is uniform on the unit interval. The display samples eleven density values; it does not replace the exact normalization integral or claim area accuracy from straight segments.',frames)
