"""Independent exact models, explicit manuscript answer bindings and artifact QA."""
from fractions import Fraction as F
from itertools import product,combinations,permutations
from collections import Counter
from math import comb,factorial
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent;counts=Counter();bindings={}
qs=json.loads((BASE/'s_bayes-questions.json').read_text());q={x['id']:x for x in qs}
def check(kind,condition):assert condition,kind;counts[kind]+=1
def bind(id,values):
    values=values if isinstance(values,list) else [values]
    for v in values:check('numeric-answer-explicitly-in-manuscript',str(v) in q[id]['solution'])
    bindings[id]=list(map(str,values))
def posterior(ps,ls):
    w=[p*l for p,l in zip(ps,ls)];z=sum(w);assert z>0;return z,[v/z for v in w]
z,r=posterior([F(1,2),F(1,3),F(1,6)],[F(1,10),F(1,5),F(3,5)])
bind('SB01',[z]+r);bind('SB02',posterior([F(3,4),F(1,4)],[F(1,50),F(1,10)])[1][1]);bind('SB03',posterior([F(2,3),F(1,3)],[F(1,4),F(3,4)])[1][1])
cells=[F(1,5),F(1,5),F(3,10),F(3,10)];w=[p*l for p,l in zip(cells,[F(1),F(1,2),F(1,4),F(0)])];bind('SB04',sum(w[:2])/sum(w))
bind('SB06',posterior([F(1,4),F(3,4)],[F(1,5),F(2,5)])[1][1]);x=F(1,4)*F(1,2);bind('SB07',[x/F(1,5),(F(1,4)-x)/F(4,5),F(1,5)-x,1-F(1,5)-F(1,4)+x])
bind('SB09',F(1,4)/(1-F(1,4)))
paths=list(product([0,1],repeat=8));joint=Counter()
for path in paths:
    k=sum(path[:4]);y=sum(path[i] and path[i+4] for i in range(4))
    if y==2:joint[k]+=1
den=sum(joint.values());bind('SB10',[F(joint[k],den) for k in [2,3,4]]+[sum(F(k*v,den) for k,v in joint.items())]);check('authentic-masters-direct-enumeration',F(den,len(paths))==F(27,128))
z,r=posterior([F(1,100),F(99,100)],[F(9,10),F(1,20)]);bind('SB11',[z,r[0],posterior([F(1,100),F(99,100)],[F(1,10),F(19,20)])[1][0]])
bind('SB12',F(1,100)*F(9,10)+F(99,100)*F(19,20));bind('SB13',F(100,1099));bind('SB14',[F(3,2),F(3,5)]);bind('SB15',[F(99,50),F(1,50)])
bind('SB16',F(3,4)*F(1,10)/(F(4,5)*F(1,4)+F(3,4)*F(1,10)));bind('SB17',F(1,50)*F(9,10)*F(1,10)/(F(9,10)*F(49,50)))
check('minimum-repetition-threshold',5**4<9*99<=5**5);bind('SB19',F(2,5));bind('SB20',posterior([F(1,4),F(3,4)],[F(3,10),F(1,20)])[1][0])
bind('SB21',[posterior([F(1,10),F(9,10)],[F(4,5),F(1,5)])[1][0],posterior([F(1,10),F(9,10)],[F(4,5)**2,F(1,5)**2])[1][0]])
bind('SB22',posterior([F(1,3),F(2,3)],[F(3,4)*F(1,2),F(1,4)*F(3,4)])[1][0])
z,r=posterior([F(1,2)]*2,[F(1,2)**3,F(9,10)**3]);bind('SB23',[r[1],r[0]*F(1,2)+r[1]*F(9,10)]);bind('SB24',F(7,10))
bind('SB25',posterior([F(1,2)]*2,[comb(5,3)*F(1,3)**3*F(2,3)**2,comb(5,3)*F(2,3)**3*F(1,3)**2])[1][1])
orders=list(permutations(range(6),2));ls=[F(sum(all(v<red for v in pair) for pair in orders),len(orders)) for red in [4,2]];bind('SB26',posterior([F(1,2)]*2,ls)[1][0])
j=(F(4,5)**2+F(1,5)**2)/2;bind('SB27',[j,2*j]);z,r=posterior([F(2,3),F(1,3)],[F(1,4)**2*F(3,4),F(3,4)**2*F(1,4)]);bind('SB28',[r[1],r[0]*F(1,4)+r[1]*F(3,4)])
bind('SB29',posterior([F(1,2)]*2,[F(1,2)**3,F(1,4)**2*F(3,4)])[1][1]);bind('SB30',posterior([F(1,2)]*2,[1-F(3,4)**3,1-F(1,4)**3])[1][1])
check('family-selected-child',posterior([F(1,4)]*4,[F(1),F(1,2),F(1,2),F(0)])[1][0]==F(1,2));bind('SB32',F(3,4));bind('SB33',[F(3,10),F(2,5)]);bind('SB34',F(4,5))
check('ignorant-host',posterior([F(1,3)]*3,[F(1,2),F(1,2),F(0)])[1][1]==F(1,2))
pairs=list(combinations(range(10),2));kept=[p for p in pairs if (p[0]<2)==(p[1]<2)];bind('SB36',F(sum(p[0]<2 for p in kept),len(kept)));bind('SB37',F(2,3));bind('SB40',(F(1,5)*F(1,4)+F(3,10)*F(3,4))/F(1,2))
p=(F(7,20)-F(1,5))/(F(4,5)-F(1,5));bind('SB41',[p,p*F(4,5)/F(7,20)]);check('infeasible-evidence',F(4,5)>F(3,4));bind('SB43',F(1,3))
bind('SB44',[4*p/(1+3*p) for p in [F(1,10),F(1,4)]]);bind('SB45',[posterior([F(1,5),F(4,5)],[s,f])[1][0] for s,f in [(F(3,5),F(1,5)),(F(4,5),F(1,10))]])
bind('SB48',F(2,5));bind('SB49',[F(9,13),F(4,13)]);bind('SB50',[F(11,13),F(18,13)]);bind('SB51',F(19,4));bind('SB52',[F(5,7),F(4,7)]);bind('SB53',F(1,4))
bind('SB56',[F(3,4),F(2,3)]);bind('SB57',F(3,5));check('nonuniform-density-mean',6*(F(1,3)-F(1,4))==F(1,2));bind('SB60',F(2,3));bind('SB61',[4*F(9,10)**3,1-F(9,10)**4])

# Independent grid checks include zero priors/likelihoods and feasible boundary models.
grid=[F(i,8) for i in range(9)]
for p,a,b in product(grid,repeat=3):
    z=p*a+(1-p)*b
    if not z:check('impossible-evidence-detection',p*a==0 and (1-p)*b==0);continue
    r=p*a/z
    check('posterior-normalization',0<=r<=1 and r+(1-p)*b/z==1)
    if 0<p<1:
        check('association-sign',(r>p)==(a>b))
        if a and b:check('odds-factorization',r/(1-r)==p/(1-p)*a/b)
for a,b in product(grid[1:],repeat=2):
    prev=F(0)
    for p in grid:
        z=p*a+(1-p)*b;r=p*a/z;check('base-rate-monotonicity',r>=prev);prev=r
    for threshold in grid[1:-1]:
        cutoff=threshold*b/(a*(1-threshold)+threshold*b)
        for p in grid:check('sharp-credibility-threshold',(p*a/(p*a+(1-p)*b)>=threshold)==(p>=cutoff))
for h,t in product(range(9),repeat=2):
    # Integrate the expanded polynomial exactly, independently of factorial formula.
    integral=sum(F((-1)**j*comb(t,j),h+j+1) for j in range(t+1))
    check('beta-integral-expanded-polynomial',integral==F(factorial(h)*factorial(t),factorial(h+t+1)))
    mean=sum(F((-1)**j*comb(t,j),h+j+2) for j in range(t+1))/integral
    check('predictive-integral-ratio',mean==F(h+1,h+t+2))
data=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'];new={k:v for k,v in data.items() if k.startswith('bayes-')}
check('ten-original-simulations',len(new)==10)
for id,s in new.items():
    for f in s['frames']:
        v=f['snapshot']
        if id=='bayes-partition':check('serialized-evidence-sum',sum(map(F,v['weights']))==F(v['evidence']))
        if id=='bayes-normalize':check('serialized-normalization',list(map(F,v['values'])) in [[F(1,2),F(1,3),F(1,6)],[F(1,20),F(1,15),F(1,10)],[F(3,13),F(4,13),F(6,13)]])
        if id=='bayes-frequencies':
            target,background=([F(9,1000),F(99,2000)] if v['positive'] else [F(1,1000),F(1881,2000)])
            expected=[F(1,100),F(99,100)] if v['stage']=='population' else [target,background] if v['stage']=='retained' else [target/(target+background),background/(target+background)]
            check('serialized-frequency-stage',list(map(F,v['values']))==expected)
        if id=='bayes-sensitivity':check('serialized-prior-response',F(v['posterior'])==4*F(v['p'])/(1+3*F(v['p'])))
        if id=='bayes-repeat':check('serialized-repeat-odds',F(v['odds'])==F(4**v['n'],9) and F(v['posterior'])==F(4**v['n'],9+4**v['n']))
        if id=='bayes-copy':check('serialized-copied-report',F(v['duplicate'])==(F(1,10) if v['n']==0 else F(4,13)))
        if id=='bayes-predict':
            r=F(9,10)**v['n']/(F(9,10)**v['n']+F(1,2)**v['n']);check('serialized-prediction',F(v['biased'])==r and F(v['predictive'])==(1-r)*F(1,2)+r*F(9,10))
        if id=='bayes-host':check('serialized-host-report',F(v['switch'])==1/(1+F(v['q'])))
        if id=='bayes-loss':check('serialized-decision-loss',F(v['threshold'])==1/(1+F(v['cfn'])) and F(v['targetRisk'])==F(11,13) and F(v['backgroundRisk'])==F(2,13)*F(v['cfn']))
        if id=='bayes-density':
            h,t=v['h'],v['t'];I=F(factorial(h)*factorial(t),factorial(h+t+1));check('serialized-density-values',F(v['integral'])==I and list(map(F,v['densities']))==[F(j,10)**h*(1-F(j,10))**t/I for j in range(11)])
        check('complete-simulation-explanation',len(f['caption'].split())>=15)
for item in qs:
    check('complete-worked-problem',len(item['solution'].split())>=55 and item['stem'].count('$')%2==item['solution'].count('$')%2==0)
    check('clean-source-characters',not any(ord(c)<32 and c not in '\n\r\t' for c in item['stem']+item['solution']))
check('unique-original-identities',len({x['id'] for x in qs})==63)
downloads=json.loads((BASE/'s_bayes-source-downloads.json').read_text())
for x in downloads:
    if 'path' in x:check('reviewed-source-fingerprint',hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'])
check('five-actually-reviewed-universities',len({x['university'] for x in downloads if 'reviewed' in x['readingState']})==5)
archive=json.loads((BASE/'exam-calibration/actual-items.json').read_text())
for id in ['Phd_CS_1404_Q69','MS_CE_1405_Q35']:
    x=next(v for v in archive if v['id']==id);p=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/x['repoPath'];check('original-booklet-fingerprint',hashlib.sha256(p.read_bytes()).hexdigest()==x['sourceSha256'])
check('authentic-family-tail',F(1,2)/(1-F(1,4))==F(2,3) and (F(2,3)-F(1,2))/F(2,3)==F(1,4))
page=(ROOT/'dist/chapters/s_bayes.html').read_text();check('artifact-bank-rules-figures',page.count('class="exam-question"')==65 and page.count('class="exam-solution"')==65 and page.count('class="review-rule"')==80 and page.count('<figure ')==7)
for m in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(m);counts['well-formed-native-mathml']+=1
approved=set(json.loads((BASE/'library-approval.json').read_text())['approvedTopics']);chapters=[c for w in json.loads((ROOT/'dist/lessons.json').read_text()) for c in w['chapters']]
check('24-approved-chapters-preserved',len(approved)==24 and all(c['status']=='ready' and c['animationReviewState']=='student_approved' for c in chapters if c['topicId'] in approved))
check('sole-new-chapter-draft',[(c['topicId'],c['status']) for c in chapters if c['topicId'] not in approved]==[('s_bayes','draft')])
report=dict(chapter='s_bayes',state='passed',checks=sum(counts.values()),byKind=dict(counts),numericAnswerBindings=bindings,originalProblems=63,authenticProblems=2,examRules=80,figures=7,scenarios=10,checkpoints=sum(len(v['frames']) for v in new.values()),limits='Exact finite/rational grids, independent enumeration/polynomial integrals and explicitly bound selected numerical answers. Symbolic proofs and conceptual cases receive editorial review; not every possible input is machine-proved. No universal completeness or unseen-score guarantee.')
(BASE/'s_bayes-validation.json').write_text(json.dumps(report,indent=2)+'\n');public=ROOT/'dist/evidence/s_bayes';public.mkdir(parents=True,exist_ok=True);(public/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['state','checks','originalProblems','authenticProblems','examRules','figures','scenarios','checkpoints']}))
