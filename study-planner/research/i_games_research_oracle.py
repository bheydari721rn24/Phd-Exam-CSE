"""Independent finite-game research checks, not an authored or delivered chapter."""
from pathlib import Path
from fractions import Fraction
from itertools import product
import json,math
R=Path(__file__).resolve().parents[1]

def tree(values,depth,branching=(2,2),level=0):
    if depth==0:return values[0]
    b=branching[level%2];size=len(values)//b
    return ('max'if level%2==0 else'min',tuple(tree(values[i*size:(i+1)*size],depth-1,branching,level+1)for i in range(b)))

def exhaustive(node):
    if not isinstance(node,tuple):return node
    kind,children=node
    if kind=='chance':
        assert all(p>=0 for p,_ in children)and sum(p for p,_ in children)==1
        return sum(p*exhaustive(child)for p,child in children)
    values=[exhaustive(c)for c in children]
    return max(values)if kind=='max'else min(values)

def bounded(node,alpha=-math.inf,beta=math.inf,visits=None):
    if visits is None:visits=[]
    if not isinstance(node,tuple):visits.append(node);return node
    kind,children=node
    if kind not in ['max','min']:raise ValueError('Chance nodes require probability-weighted bounds; ordinary alpha-beta is not used here.')
    value=-math.inf if kind=='max'else math.inf
    for child in children:
        v=bounded(child,alpha,beta,visits)
        if kind=='max':value=max(value,v);alpha=max(alpha,value)
        else:value=min(value,v);beta=min(beta,value)
        if alpha>=beta:break
    return value

checks=0;trees=0;window_checks=0
for depth in range(1,4):
    for values in product([-1,0,1],repeat=2**depth):
        node=tree(values,depth);exact=exhaustive(node);visits=[]
        assert bounded(node,visits=visits)==exact and len(visits)<=len(values)
        checks+=1;trees+=1
        for alpha,beta in [(-2,-1),(-1,0),(0,1),(1,2),(-1,1)]:
            result=bounded(node,alpha,beta)
            if result<=alpha:assert exact<=result
            elif result>=beta:assert exact>=result
            else:assert result==exact
            checks+=1;window_checks+=1

# Exact depth-two and alternating-branch counts under ideal equality ordering.
counts=[]
for b in range(2,5):
    for depth in range(1,7):
        node=tree([0]*(b**depth),depth,(b,b));seen=[];bounded(node,visits=seen)
        expected=b**((depth+1)//2)+b**(depth//2)-1
        assert len(seen)==expected;checks+=1
        counts.append({'branching':b,'depth':depth,'allLeaves':b**depth,'observedLeaves':len(seen),'bestCaseFormula':expected})
for n,m,k in product(range(2,4),range(2,4),range(1,4)):
    node=tree([0]*((n*m)**k),2*k,(n,m));seen=[];bounded(node,visits=seen)
    assert len(seen)==n**k+m**k-1;checks+=1

# An equality cutoff returns a bound, not necessarily an exact tied child value.
first=('min',(5,5));second=('min',(5,0))
assert exhaustive(first)==5 and exhaustive(second)==0 and bounded(second,alpha=5)==5
checks+=1

# Strictly increasing nonlinear score changes can reverse expected-value choice.
a=2;b=('chance',((Fraction(1,2),0),(Fraction(1,2),3)))
assert exhaustive(a)>exhaustive(b)
cube=('chance',((Fraction(1,2),0),(Fraction(1,2),27)))
assert 8<exhaustive(cube);checks+=2
for scale,offset in product(range(1,4),range(-2,3)):
    changed=('chance',tuple((p,scale*v+offset)for p,v in b[1]))
    assert scale*a+offset>exhaustive(changed);checks+=1

report={'state':'passed_preliminary_mathematical_research_not_a_chapter','date':'2026-10-17','exhaustiveSmallTrees':trees,'narrowWindowCertificates':window_checks,'assertions':checks,'uniformBestCaseCounts':counts,'equalityCutoffExample':{'rootIncumbent':5,'candidateReturnedUpperBound':5,'candidateExactValue':0,'lesson':'A returned equality bound does not prove that a second root move is optimal.'},'chanceUtilityExample':{'deterministic':'2','lotteryExpected':'3/2','cubedDeterministic':'8','cubedLotteryExpected':'27/2'},'limits':'These finite tests support preparation of exact teaching models. They are not a four-course synthesis, a general proof of every bound, an authored problem bank, or a completed i_games chapter. No new chapter is counted.'}
(R/'research/i_games-preliminary-mathematics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print({k:v for k,v in report.items()if k not in ['uniformBestCaseCounts','limits']})
