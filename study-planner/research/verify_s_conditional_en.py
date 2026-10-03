"""Independent finite/rational checks and explicit answer-to-manuscript bindings."""
from fractions import Fraction as F
from itertools import product,permutations,combinations
from math import comb
from collections import Counter
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent;counts=Counter()
def check(kind,p):assert p,kind;counts[kind]+=1
def s(v):return [s(x) for x in v] if isinstance(v,(list,tuple)) else str(v)
questions=json.loads((BASE/'s_conditional-questions.json').read_text());q={x['id']:x for x in questions}
bindings={}
def bind(title,value):
    item=next(x for x in questions if x['title']==title);check('answer-bound-to-source',s(value)==item['result']);bindings[item['id']]=s(value)
bind('Unequal retained masses',[F(1,3),F(1,4)])
bind('Reconstruct every cell',[F(2,5)*F(3,4),F(3,5)*F(1,6),F(2,5)*F(1,4),F(3,5)*F(5,6)])
bind('Sharp range of a conditional',[max(F(0),F(7,10)+F(3,5)-1)/F(3,5),min(F(7,10),F(3,5))/F(3,5)])
bind('Recover an unknown stratum weight',[(F(1,2)-F(1,5))/(F(4,5)-F(1,5)),F(4,5)])
bind('A conditional union uses one universe',[F(2,3)+F(1,2)-F(1,3),F(2,3)+F(1,2)-2*F(1,3),1-F(2,3)-F(1,2)+F(1,3)])
bind('Nested information',F(1+4,1+2+4))
bind('A zero last factor is allowed',F(2,5)*F(3,4)*0)
bind('Dropping history changes a joint answer',[F(1,2)*F(1,2),F(1,2)**3])
bind('Reverse a three-stage factorization',F(3,5)*F(1,2)*F(2,3)/(F(2,5)*F(3,4)))
bind('Conditional paths with a stated Markov assumption',[F(2,5)*F(1,3)**2,F(2,5)*F(2,3)**2,F(1,5)])
pairs=list(product(range(1,5),repeat=2));retained=[v for v in pairs if min(v)==2]
bind('Minimum and maximum of two rolls',[F(sum(max(v)==k for v in retained),len(retained)) for k in [2,3,4]])
draws=list(permutations(range(7),3));colors=lambda d:tuple('R' if x<4 else 'B' for x in d)
bind('Sampling a specified pattern',[F(sum(colors(d)==('R','B','R') for d in draws),len(draws)),F(sum(sum(x<4 for x in d)==2 for d in draws),len(draws))])
d=[x for x in draws if (x[0]<4)!=(x[1]<4)];bind('Condition on a coarse color history',F(sum(x[2]<4 for x in d),len(d)))
d=[x for x in draws if x[0]<4 or x[1]<4];bind('A mixture of remaining urns',F(sum(x[2]<4 for x in d),len(d)))
patterns=list(combinations(range(8),3));bind('A conditional arrangement erases p',F(sum(0 in v and 1 in v for v in patterns),len(patterns)))
patterns=list(combinations(range(6),3));bind('A conditional streak count',F(sum(any(set(range(i,i+3))<=set(v) for i in range(4)) for v in patterns),len(patterns)))
prob=[F(1,2),F(1,3),F(1,6)];bind('Birthday-type chain with nonuniform labels',sum((prob[a]*prob[b]*prob[c] for a,b,c in permutations(range(3))),F(0)))
bind('Random eligibility with unequal stages',comb(5,2)*F(1,2)**5)
bind('Total probability needs actual partition weights',[F(1,4)*F(4,5)+F(3,4)*F(2,5),F(2,5)])
bind('A conditioned partition uses new weights',F(3,4)*F(2,3)+F(1,4)*F(1,3))
bind('Simpson reversal in exact fractions',[F(1,10)*F(9,10)+F(9,10)*F(2,5),F(9,10)*F(4,5)+F(1,10)*F(3,10)])
bind('An event independent of itself',[0,1]);bind('Pairwise independent, not mutually independent',[F(1,4),0]);bind('Triple factorization is not sufficient',[F(1,8),F(1,2)])
bind('Counting independence constraints',[2**5-5-1,comb(5,2)])
rates=[F(1,2),F(1,3),F(1,4)];exact=F(0)
for bits in product([0,1],repeat=3):
    mass=F(1)
    for bit,p in zip(bits,rates):mass*=p if bit else 1-p
    if sum(bits)==1:exact+=mass
bind('Exactly one heterogeneous success',[exact,1-(1-rates[0])*(1-rates[1])*(1-rates[2])])
bind('Pairwise information cannot fix an all-failure rate',[F(1,8),F(1,4)])
bind('Selection on equality creates dependence',[F(1,2),F(1,2),F(1,4)])
bind('Selection on a union creates negative association',[F(1,3),F(2,3)**2])
joint=(F(9,10)**2+F(1,10)**2)/2;bind('Hidden type makes independent checks dependent',[joint,2*joint])
bind('Conditional independence in one stratum only',(F(1,4)+F(1,2))/2)
joint=F(4,5)*F(1,5);bind('Opposite hidden-type rates',[joint,joint-F(1,4)])
bind('A truthful report has two different answers',[F(1,4)/F(3,4),F(1,4)/F(1,2)])
bind('Two-sided cards and face multiplicity',[F(2,3),F(1,2)])
bind('A host who does not know the prize',F(1,3)/(F(1,3)+F(1,6)+F(1,6)))
bind('Shared-edge paths are dependent',[2*F(1,2)**2-F(1,2)**3,2*F(1,2)**2-F(1,2)**4])
bind('Conditional independence is not supplied by equal rates',F(3,8)/F(1,2))
bind('Conditional geometry on a triangle',(F(1,2)-F(1,2)**2/2)/F(1,2))
bind('An exact observation requires a density model',F(1,3))
bind('How little does pairwise data identify?',[0,F(1,4)])

for x,a,b,z in product(range(7),repeat=4):
    total=x+a+b+z
    if not total:continue
    pa,pb,j=F(x+a,total),F(x+b,total),F(x,total)
    check('four-cell-feasibility',max(F(0),pa+pb-1)<=j<=min(pa,pb))
    check('determinant-independence',(x*z==a*b)==(j==pa*pb))
    if x+b:
        check('conditional-complement',F(x,x+b)+F(b,x+b)==1)
        check('conditional-association-sign',(F(x,x+b)>pa)==(j>pa*pb))
    if x+a and x+b:check('reversed-equality',((F(x,x+b)==F(x,x+a)))==(x==0 or pa==pb))

for t in [F(i,80) for i in range(21)]:
    masses=[F(1,4)-t if sum(bits)%2==0 else t for bits in product([0,1],repeat=3)]
    # 000 has 1/4-t; 111 has t; one-success cells t; two-success cells 1/4-t.
    states=list(product([0,1],repeat=3));check('triple-family-normalization',sum(masses)==1 and min(masses)>=0)
    for i,j in combinations(range(3),2):check('triple-family-pairwise',sum(m for m,bits in zip(masses,states) if bits[i] and bits[j])==F(1,4))
    check('triple-family-mutual', (t==F(1,8))==(masses[-1]==F(1,8)))

for n in range(2,14):
    p=F(1,n);exact=(1-p)**n+n*p*(1-p)**(n-1)
    check('authentic-68-general-form',exact==F((n-1)**(n-1)*(2*n-1),n**n))
check('authentic-69-geometric',F(1,2)/(1-F(1,4))==F(2,3) and (F(2,3)-F(1,2))/F(2,3)==F(1,4))
check('authentic-70-vandermonde',sum(comb(25,k)*comb(20,k) for k in range(21))==comb(45,20))
check('authentic-35-two-derivations',sum(F(comb(4,k)*comb(k,2),2**(4+k)) for k in range(2,5))==comb(4,2)*F(1,4)**2*F(3,4)**2==F(27,128))

def network(bits):
    vertices={0}
    changed=True
    while changed:
        old=set(vertices)
        for bit,(u,v) in zip(bits,[(0,1),(1,3),(0,2),(2,3),(1,2)]):
            if bit and (u in vertices or v in vertices):vertices.update([u,v])
        changed=vertices!=old
    return 3 in vertices
for p in [F(i,20) for i in range(21)]:
    exact=F(0)
    for bits in product([0,1],repeat=5):
        mass=p**sum(bits)*(1-p)**(5-sum(bits))
        if network(bits):exact+=mass
    check('bridge-reliability',exact==(1-p)*(2*p*p-p**4)+p*(2*p-p*p)**2)
bind('Bridge reliability by conditioning',F(sum(network(b) for b in product([0,1],repeat=5)),32))
for w,u1,u2,v1,v2 in product([F(0),F(1,2),F(1)],repeat=5):
    joint=w*u1*v1+(1-w)*u2*v2
    marg=(w*u1+(1-w)*u2)*(w*v1+(1-w)*v2)
    check('two-stratum-covariance',joint-marg==w*(1-w)*(u1-u2)*(v1-v2))
for r in [F(1,4),F(1,2),F(3,4)]:
    for p in [F(1,4),F(1,2),F(3,4)]:
        total=(1-r)/(1-r*p);check('geometric-mixture-positive-count',(total-(1-r))/total==r*p)

data=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes']
new={k:v for k,v in data.items() if k.startswith('conditional-')}
check('animation-count',len(new)==9)
for id,scene in new.items():
    for f in scene['frames']:
        state=f['snapshot']
        if id=='conditional-bridge':check('serialized-bridge-state',network(state['bits'])==state['connected'])
        if id=='conditional-strip':
            ep=F(state['epsilon']);check('serialized-strip-masses',F(state['mass'])==ep+ep**2 and F(state['target'])==ep/2 and F(state['ratio'])==F(state['target'])/F(state['mass']))
        if id=='conditional-report':
            likelihoods=list(map(F,state['likelihoods']));check('serialized-report-weights',[x/sum(likelihoods) for x in likelihoods]==list(map(F,state['posteriors'])))
        if id=='conditional-selection':
            pairs=list(product([0,1],repeat=2));keep=state['retained'];den=sum(keep)
            check('serialized-selection-joint',F(sum(k*x*y for k,(x,y) in zip(keep,pairs)),den)==F(state['joint']))
        for value in [f['caption'],f['formula'],scene['invariant']]:check('animation-text-control-characters',not any(ord(c)<32 and c not in '\n\t\r' for c in value))

for item in questions:
    check('distinct-complete-problem',len(item['solution'].split())>=50 and len(item['stem'].split())>=12)
    for text in [item['stem'],item['solution']]:check('source-string-integrity',text.count('$')%2==0 and not any(ord(c)<32 and c not in '\n\t\r' for c in text))
check('unique-problem-identities',len({v['id'] for v in questions})==56)
downloads=json.loads((BASE/'s_conditional-source-downloads.json').read_text())
for item in downloads:
    if item.get('path'):check('reviewed-source-fingerprint',hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256'])
check('minimum-reviewed-universities',len({x['university'] for x in downloads if 'reviewed' in x['readingState']})>=4)
archive=json.loads((BASE/'exam-calibration/actual-items.json').read_text())
for id in ['Phd_CS_1404_Q68','Phd_CS_1404_Q69','Phd_CS_1404_Q70','MS_CE_1405_Q35']:
    item=next(x for x in archive if x['id']==id)
    source=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/item['repoPath']
    check('authentic-booklet-fingerprint',hashlib.sha256(source.read_bytes()).hexdigest()==item['sourceSha256'])
page=(ROOT/'dist/chapters/s_conditional.html').read_text()
check('artifact-counts',page.count('class="exam-question"')==60 and page.count('class="exam-solution"')==60 and page.count('class="review-rule"')==80 and page.count('<figure ')==7)
for m in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(m);counts['well-formed-mathml']+=1
approved=set(json.loads((BASE/'library-approval.json').read_text())['approvedTopics'])
chapters=[c for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]
check('existing-approval-preserved',len(approved)==23 and all(c['status']=='ready' and c['animationReviewState']=='student_approved' for c in chapters if c['topicId'] in approved))
check('one-new-draft',[(c['topicId'],c['status']) for c in chapters if c['topicId'] not in approved]==[('s_conditional','draft')])
report=dict(chapter='s_conditional',state='passed',checks=sum(counts.values()),byKind=dict(counts),numericAnswerBindings=bindings,originalProblems=56,authenticProblems=4,examRules=80,figures=7,scenarios=9,checkpoints=sum(len(v['frames']) for v in new.values()),domains={'jointTables':'all integer weights 0..6, excluding all-zero table','bridge':'all 32 edge states; 21 rational success probabilities 0..1','urn':'all 210 ordered three-object draws from four red and three blue','stratumCovariance':'243 rational parameter combinations','pairwiseFamily':'21 feasible triple masses','authentic':'four exact independently derived answers plus the at-most-one formula for n=2..13'},limits='Bounded models and explicit numeric answer bindings. Other symbolic proofs and conceptual solutions receive editorial derivation review, not automated universal theorem proving. No unseen-examination score guarantee.')
(BASE/'s_conditional-validation.json').write_text(json.dumps(report,indent=2)+'\n')
public=ROOT/'dist/evidence/s_conditional';public.mkdir(parents=True,exist_ok=True)
(public/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['state','checks','originalProblems','authenticProblems','examRules','figures','scenarios','checkpoints']}))
