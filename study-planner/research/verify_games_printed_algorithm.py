"""Check the actual printed search implementation against exhaustive backups."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib, json, math, re

R=Path(__file__).resolve().parents[1]
source=(R/'research/i_games.en.md').read_text(encoding='utf8')
code=re.search(r'```python\n([\s\S]*?)```',source)[1]
class State:
    def __init__(self,t):
        self.terminal=not isinstance(t,tuple)
        self.utility=Fraction(t) if self.terminal else None
        self.kind='LEAF' if self.terminal else t[0]
        self.children=[] if self.terminal else [State(c) for c in t[1]]
def make(values,depth,level=0):
    if not depth:return values[0]
    n=len(values)//2
    return ('MAX' if level%2==0 else 'MIN',
            (make(values[:n],depth-1,level+1),make(values[n:],depth-1,level+1)))
def truth(t):
    if not isinstance(t,tuple):return Fraction(t)
    return (max if t[0]=='MAX' else min)(truth(c) for c in t[1])
ns={'evaluate':lambda s:Fraction(0),'ordered_children':lambda s:iter(s.children),
    'ordered_actions':lambda s:enumerate(s.children)}
exec(compile(code,'actual_printed_chapter_code','exec'),ns)
trees=windows=action_checks=0
for depth in range(1,4):
    for values in product([-1,0,1],repeat=2**depth):
        t=make(values,depth);state=State(t);exact=truth(t)
        assert ns['alphabeta'](state,depth)==exact
        action,score=ns['choose_max_action'](state,depth)
        assert score==exact and truth(t[1][action])==exact
        trees+=1;action_checks+=1
        for alpha,beta in [(-2,-1),(-1,0),(0,1),(1,2),(-1,1)]:
            result=ns['alphabeta'](state,depth,alpha,beta)
            assert (exact<=result if result<=alpha else exact>=result if result>=beta else exact==result)
            windows+=1
nonalternating=[('MAX',(('MAX',(2,9)),)),('MIN',(('MIN',(-4,8)),)),
                ('MAX',(('MAX',(-2,3)),('MIN',(4,-1))))]
for t in nonalternating:assert ns['alphabeta'](State(t),5)==truth(t)
report={'state':'passed_printed_algorithm_exhaustive_checks','date':'2026-10-18',
        'orderedTrees':trees,'narrowWindowContracts':windows,'optimalActionChecks':action_checks,
        'consecutiveSamePlayerCases':len(nonalternating),
        'assertions':trees+windows+action_checks+len(nonalternating),
        'printedCodeSha256':hashlib.sha256(code.encode()).hexdigest(),
        'limits':'All ordered binary trees of depths 1–3 over leaf values -1,0,1 and five windows; finite evidence, not a universal proof. The text supplies the recursive correctness argument.'}
(R/'research/i_games-printed-code-exhaustive.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(report)
