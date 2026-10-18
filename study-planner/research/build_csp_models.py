"""Declared finite inputs and exact support/queue snapshots; no generic fake animation."""
from pathlib import Path
from copy import deepcopy
import json,shutil
from csp_exact import CSP,instance,ac3,brute_force
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'i_csp-evidence';E.mkdir(exist_ok=True)
tmp=Path('C:/Users/bheydari/AppData/Local/Temp')
for folder,names in [('phd-csp-peer-20261018',['i_csp-written-source-review.md','i_csp-written-source-review.json','independent-checks.json','acquisition-final.json']),('phd-csp-exams-20261018',['i_csp-authentic-research.json','i_csp-authentic-research.en.md'])]:
 for name in names:shutil.copyfile(tmp/folder/name,E/name)
shutil.copyfile(tmp/'phd-csp-sources-20261018/stanford-acquisition.json',E/'stanford-acquisition.json')
models=[]
def add(id,title,domains,rules,assumption=None,mode='ac',queue=None,legend=None):
 c=instance(domains,rules);D=deepcopy(c.initial)
 prefix=[]
 if assumption:
  x,a=assumption;before=deepcopy(D);D[x]=[a]
  prefix=[dict(kind='assumption',why=f'Assume {x}={a} in this branch. Later failure is conditional on this decision.',arc=None,domains=deepcopy(D),queue=[],removed=[],supports=[],before=before,pairChecks=0)]
  if queue is None:queue=[(z,x)for z in c.neighbors[x]]
 if mode=='fc':
  events=prefix;checks=0
  for z,x in queue:
   before=deepcopy(D);supports=[];removed=[]
   for b in list(D[z]):
    checks+=1;ok=(b,D[x][0])in c.relations[z,x]
    supports.append(dict(tail=b,head=D[x][0]if ok else None))
    if not ok:D[z].remove(b);removed.append(b)
   events.append(dict(kind='forward-check',why='One-layer forward checking filters only a neighbor of the assigned variable. It does not requeue other arcs.',arc=[z,x],domains=deepcopy(D),queue=[],removed=removed,supports=supports,before=before,pairChecks=checks))
  events.append(dict(kind='one-layer-end',why='Forward checking stops here: compare the unchanged distant domain with the MAC case.',arc=None,domains=deepcopy(D),queue=[],removed=[],supports=[],before=None,pairChecks=checks))
 else:
  ok,D,events=ac3(c,D,queue);events=prefix+events
 m=dict(id=id,title=title,variables=list(c.variables),domains=c.initial,constraints=[dict(x=x,y=y,allowed=[list(p)for p in sorted(c.relations[x,y])],label=c.labels[x,y])for x in c.variables for y in c.neighbors[x]if c.variables.index(x)<c.variables.index(y)],frames=events,mode=mode,legend=legend or '',solutions=brute_force(c))
 models.append(m);return m
eq=lambda a,b:a==b
ne=lambda a,b:a!=b
lt=lambda a,b:a<b
add('sum-four','Sum support: X+Y=4',{'X':[1,2,3,4,5],'Y':[1,2]},[('X','Y',lambda a,b:a+b==4,'X + Y = 4')])
for d in [3,4]:add('strict-'+str(d),'Strict chain on '+str(d)+' values',{x:list(range(1,d+1))for x in 'ABC'},[('A','B',lt,'A < B'),('B','C',lt,'B < C')])
add('holes','Extensional table with unsupported values',{'X':[1,2,3],'Y':[3,4,5,6]},[('X','Y',lambda a,b:(a,b)in{(1,3),(1,5),(3,3),(3,6)},'Four allowed pairs')])
add('mit-colors','Three-color triangle with a fixed domain',{'A':[1,2,3],'B':[1,2],'C':[2]},[('A','B',ne,'A != B'),('A','C',ne,'A != C'),('B','C',ne,'B != C')],legend='Color codes: 1=red; 2=green; 3=blue.')
for n in [3,4]:
 vars='ABCD'[:n];add('cycle-'+str(n),str(n)+'-cycle: local support versus global parity',{x:[0,1]for x in vars},[(vars[i],vars[(i+1)%n],ne,'Different colors')for i in range(n)])
chain={x:[0,1]for x in 'ABC'};rules=[('A','B',eq,'A = B'),('B','C',eq,'B = C')]
add('chain-fc','Forward checking after A=0',chain,rules,('A',0),mode='fc')
add('chain-mac','MAC after A=0',chain,rules,('A',0))
rollback={x:[0,1]for x in 'XYZ'};rr=[('X','Y',lambda a,b:a<=b,'X <= Y'),('Y','Z',eq,'Y = Z'),('X','Z',ne,'X != Z')]
m=add('rollback','A failed branch, complete restoration, then a valid sibling',rollback,rr,('X',1));good=add('rollback-zero','Restored sibling X=0',rollback,rr,('X',0))
m['frames']+=[dict(kind='restore',why='Restore ALL parent domains before changing the assumption. A sibling must not inherit the failed branch.',arc=None,domains=deepcopy(rollback),queue=[],removed=[],supports=[],before=None,pairChecks=0)]+good['frames']
add('conjunction','Equality and inequality conjoined',{'X':[0,1],'Y':[0,1]},[('X','Y',eq,'Equality AND inequality'),('X','Y',ne,'Equality AND inequality')])
add('asymmetric','Reverse direction uses a transposed relation',{'X':[1,2,3],'Y':[1,2,3]},[('X','Y',lt,'X < Y')])
add('star','A tree can fail in the backward sweep',{'H':[1,2,3],'U':[1],'V':[2],'W':[3]},[('H',x,ne,'H != '+x)for x in 'UVW'],queue=[('H',x)for x in 'UVW'])
add('tree','Three-color path: supports before witness construction',{x:[1,2,3]for x in 'ABC'},[('A','B',ne,'A != B'),('B','C',ne,'B != C')],queue=[('B','C'),('A','B')])
add('triangle-cutset','Condition A=1; the remaining edge has two completions',{'A':[1],'B':[1,2,3],'C':[1,2,3]},[('A','B',ne,'A != B'),('A','C',ne,'A != C'),('B','C',ne,'B != C')],legend='A is the supplied one-variable cutset. Its fixed value prunes boundary neighbors before the residual edge is solved.')
clique=[(x,y,ne,x+' != '+y)for i,x in enumerate('ABCD')for y in 'ABCD'[i+1:]]
add('k4-root','K4 is arc consistent with three colors, but has no solution',{x:[1,2,3]for x in 'ABCD'},clique)
add('k4-cutset','A=1,B=2: the residual edge fails',{'A':[1],'B':[2],'C':[1,2,3],'D':[1,2,3]},clique,legend='Cutset {A,B} satisfies its internal edge. Boundary filtering leaves C and D both equal to3, contradicting C != D.')
add('hall-pairwise','Pairwise AC misses the Hall-set consequence',{'X':[1,2],'Y':[1,2],'Z':[1,2,3]},[(x,y,ne,x+' != '+y)for x,y in [('X','Y'),('X','Z'),('Y','Z')]])
add('hall-impossible','Every pair supported; three distinct values impossible',{x:[1,2]for x in 'XYZ'},[(x,y,ne,x+' != '+y)for x,y in [('X','Y'),('X','Z'),('Y','Z')]])
add('path-consistency','Equal, equal, different: AC alone misses contradiction',rollback,[('X','Y',eq,'X = Y'),('Y','Z',eq,'Y = Z'),('X','Z',ne,'X != Z')])
add('lcv','LCV value-loss counterexample',{'X':[0,1],'Y':[1,2,3,4],'Z':[1,2,3,4]},[('X','Y',lambda a,b:b==1 if a==0 else b in[2,3,4],'0: Y=1; 1: Y in 2,3,4'),('X','Z',lambda a,b:True if a==0 else b in[2,3,4],'0: any Z; 1: Z in 2,3,4')],legend='X code 0 represents a; X code 1 represents b. The initial AC trace leaves both candidates; IC12 computes their separate LCV scores.')
scope=[('X',y,lambda a,b:(a,b)in{(0,0),(1,0),(1,1)},'Allowed: 00,10,11')for y in 'YZ']+[('Y','Z',ne,'Y != Z')]
add('scope-root','Root is arc consistent and has two solutions',rollback,scope)
add('scope-fail','Only branch X=0 fails',rollback,scope,('X',0))
add('auth-numeric','Original1404Q75: node filtering, then exact AC',{'X':[1,2,3],'Y':[1,2,3,4],'Z':[1,2],'W':[2,3]},[('X','Y',ne,'X != Y'),('Z','W',eq,'Z = W'),('X','W',lambda a,b:a+b<=4,'X + W <= 4')],legend='Unary preprocessing has already removed Z=3. The original domain before that step was {1,2,3}.')
edges=['AB','AC','AD','AE','BC','BE','CD','DE']
add('auth-map','Original map: explicit three-color teaching case',{'A':[1,2,3],'B':[1,2,3],'C':[1,2,3],'D':[2],'E':[1]},[(x,y,ne,x+' != '+y)for x,y in edges],legend='Teaching palette only: 1=red, 2=yellow, 3=green. The printed item does not state palette size. D and E are assigned; residual degree ignores their vertices.')
out=dict(models=models,contract='Integer-coded finite binary tables; one conjoined relation per pair; full root AC before incremental MAC. Snapshots are exact execution states, not interpolated algorithm claims.')
(B/'i_csp-models.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print({'models':len(models),'modelFrames':sum(len(m['frames'])for m in models)})
