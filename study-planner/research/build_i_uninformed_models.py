from pathlib import Path
from html import escape as e
import json,subprocess,sys,ast,math
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.SYMBOLS.update(varepsilon='ε',infty='∞',nRightarrow='⇏')
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef) and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
# Reuse the approved motion controls, not the preceding subject's mathematical model.
p=R/'dist/chapters/i_uninformed.js';s=p.read_text(encoding='utf-8');old=(R/'dist/chapters/i_agents.js').read_text(encoding='utf-8')
mount=old[old.index('function mount(host,m)'):old.index('const api=')].replace('ag-','us-').replace('probability-threshold|belief-bars|vacuum-motion|decision-belief','search-graph|search-count|cost-contour|grid-path|bidirectional-layers')
if '/* PLAYER_MOUNT */' in s:s=s.replace('/* PLAYER_MOUNT */',mount);p.write_text(s,encoding='utf-8')
css=(R/'dist/chapters/i_agents.css').read_text().replace('ag-','us-').replace('#ag-','#us-')
css+='\n#us-form textarea{width:100%;min-height:160px;font:15px/1.6 "JetBrains Mono",monospace;padding:12px;border:1px solid #b9cbd6;border-radius:8px}#us-form select{font:inherit;padding:10px}.us-label{font-size:18px}.us-stage svg .us-math{font-family:"STIX Two Math",serif!important}.us-model details{max-width:100%}\n'
(R/'dist/chapters/i_uninformed.css').write_text(css,encoding='utf-8')
specs=[];groups={}
def graph(id,title,edges,alg='bfs',limit=4,group=None,start='S',goal='G',positions=None):
 nodes=list(dict.fromkeys([start,goal]+[v for edge in edges for v in edge[:2]]));specs.append(dict(id=id,title=title,graph=dict(nodes=nodes,edges=edges,start=start,goal=goal),algorithm=alg,limit=limit,positions=positions));
 if group:groups.setdefault(group,[]).append(id)
main=[['S','A',1],['S','B',1],['A','C',1],['A','D',1],['B','D',1],['B','G',1],['D','G',1]]
pos=dict(S=[90,220],A=[330,130],B=[330,315],C=[590,100],D=[590,255],G=[850,315])
graph('bfs-main','BFS: FIFO frontier and discovery on insertion',main,group='bfs',positions=pos)
graph('dfs-main','DFS: reverse pushes preserve written successor order',main,'dfs',group='dfs',positions=pos)
triangle=dict(S=[100,230],A=[470,120],G=[850,230])
graph('weighted-bfs','BFS minimizes edge count, not arbitrary cost',[['S','G',9],['S','A',1],['A','G',1]],positions=triangle)
weighted=[['S','A',4],['S','B',1],['B','A',1],['A','G',2],['B','G',8]]
graph('ucs-main','UCS: strict relaxation and stale records',weighted,'ucs',group='ucs',positions=dict(S=[90,220],A=[460,120],B=[330,320],G=[850,220]))
graph('early-goal','Generate an expensive goal; select the cheaper goal later',[['S','G',10],['S','A',1],['A','G',1]],'ucs',positions=triangle)
graph('zero-cycle','A zero-cost cycle with strict improvement',[['S','A',0],['A','S',0],['A','G',2]],'ucs',positions=triangle)
chain=[['S','A',1],['A','G',1]]
graph('dls-main','DLS: the goal at the boundary is accepted',chain,'dls',2,'dls',positions=triangle)
graph('dls-cutoff','DLS: a depth-one cutoff is not failure',chain,'dls',1,'dls',positions=triangle)
graph('depth-alias-main','Depth budget: revisit X by the shallower path',[['S','A',1],['A','B',1],['B','X',1],['X','G',1],['S','X',1]],'dls',3,'depth-alias',positions=dict(S=[80,220],A=[290,120],B=[500,120],X=[710,220],G=[910,320]))
graph('ids-main','IDS: fresh path checks at every increasing limit',[['S','A',1],['A','B',1],['B','G',1]],'ids',3,'ids',positions=dict(S=[100,220],A=[350,220],B=[600,220],G=[850,220]))
graph('segment-main','Dictionary segmentation: indices and word edges',[['0','1',1],['0','2',1],['1','2',1],['1','3',1],['2','4',1],['3','4',1]],'bfs',group='segmentation',start='0',goal='4',positions={'0':[80,220],'1':[300,120],'2':[520,220],'3':[740,120],'4':[910,300]})
graph('key-main','Room plus key bit: distinct states must remain distinct',[['S','X0',1],['S','K',1],['K','X1',1],['X1','G',1]],positions=dict(S=[90,220],X0=[370,120],K=[370,320],X1=[640,320],G=[880,220]))
graph('finite-cycle-failure','Finite graph: exhaust a cycle without a goal',[['S','A',0],['A','S',0]],'bfs',positions=triangle)
graph('costly-dls','DLS can return an expensive route within its bound',[['S','A',10],['A','B',10],['B','G',10],['S','X',1],['X','G',1]],'dls',3,positions=dict(S=[80,220],A=[300,120],B=[540,120],G=[850,220],X=[400,320]))
script="const fs=require('fs'),a=require('./dist/chapters/i_uninformed.js');const specs=JSON.parse(fs.readFileSync(0,'utf8'));process.stdout.write(JSON.stringify(specs.map(s=>a.makeModel(s.id,s.title,a.run(s.graph,s.algorithm,s.limit,240),s.positions))));"
models=json.loads(subprocess.check_output(['node','-e',script],input=json.dumps(specs).encode(),cwd=R))
def tx(x,y,s,anchor='start',is_math=False):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="us-{"math"if is_math else"label"}">{e(str(s))}</text>'
def rect(x,y,w,h,c='#e6efea'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c}" stroke="#9db6be"/>'
def svg(s):return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 640" role="img">'+s+'</svg>'
def model(id,title,kind,invariant,group=None):
 m=dict(id=id,title=title,kind=kind,invariant=invariant,code=['Identify the counted object or path.','Apply the declared formula or invariant.','Check the boundary case.','Interpret the result under the stated assumptions.'],frames=[]);models.append(m)
 if group:groups.setdefault(group,[]).append(id)
 return m
def frame(m,state,s,op,why,formula):
 prev=m['frames'][-1]['snapshot'] if m['frames'] else None;f=dict(snapshot=state,svg=svg(s),caption=why,formulaHtml=mathml.render(formula,True),teaching=dict(operation=op,why=why,checks=[dict(mathHtml=mathml.render(formula),result='independently checked in chapter audit')],changes=[dict(field=k,before=prev.get(k),after=v)for k,v in state.items() if prev and prev.get(k)!=v],currentState=state,initial=prev is None,reading=m['invariant'],guide=m['code'],activeLine=min(3,len(m['frames'])),mode=m['kind']));m['frames'].append(f)
def bars(m,rows,formula,description,state):
 maximum=max(v for _,v in rows);s=tx(35,35,m['title'])+tx(35,88,'Exact quantities; bar lengths share the same linear scale within this checkpoint.')
 for i,(label,v)in enumerate(rows):
  y=140+105*i;w=620*v/maximum;s+=tx(40,y+26,label)+f'<g data-entity="bar-{i}">'+rect(300,y,w,45,'#c4dcd5')+'</g>'+tx(310,y+78,str(v),is_math=True)
 frame(m,state,s,'Compute exact counts',description,formula)
m=model('counts-main','Full trees and repeated IDS visits','search-count','Roots are counted on every iteration. These are exhaustive traversals, not average goal positions.','counts')
for b,d in [(3,6),(2,4),(10,5),(3,4),(6,8)]:
 N=sum(b**i for i in range(d+1));I=sum((d-i+1)*b**i for i in range(d+1));bars(m,[('One traversal',N),('IDS selections',I),('Last layer',b**d)],r'N='+str(N)+r',\quad I='+str(I),f'Explicit specialization b={b}, d={d}. Select the checkpoint matching the problem; the 96-byte memory question multiplies the last-layer value by 96.',dict(b=b,d=d,nodes=N,ids=I,leaves=b**d))
m=model('counts-chain','Unary IDS: triangular repeated work','search-count','For b=1 there is no exponential last layer. Every root visit is included.')
for d in [1,3,8]:bars(m,[('Single traversal',d+1),('IDS selections',(d+1)*(d+2)//2)],r'I_1('+str(d)+r')=\frac{('+str(d)+r'+1)('+str(d)+r'+2)}2',f'Unary chain through depth {d}; the overhead grows with d.',dict(d=d,single=d+1,ids=(d+1)*(d+2)//2))
m=model('counts-bfs','BFS can generate beyond the goal depth','search-count','Full binary tree, unique shallowest goal last at depth 3, goal test on removal.')
for k in [0,1,3,7]:
 s=tx(35,35,'Depth 3: processed nonglobal goals before the last goal')+tx(35,92,'Each non-goal at depth 3 generates two depth-4 children.')
 for i in range(8):s+=rect(40+116*i,160,95,70,'#e9d7b5' if i==7 else '#c1d7d3' if i<k else '#edf3f3')+tx(87+116*i,201,'G'if i==7 else str(i+1),'middle',True)
 s+=tx(40,320,'Nodes through depth 3: 15; additional generated children: '+str(2*k))+tx(40,380,'Queue size before selecting the goal: '+str(8+k))+tx(40,450,'Final count at k=7: 29 generated nodes; 15 entries waiting before goal removal.')
 frame(m,dict(processedDepth3=k,generated=15+2*k,queue=8+k),s,'Process a nonglobal goal-depth node','The final checkpoint is the requested worst-position goal case.',r'15+2\cdot'+str(k)+'='+str(15+2*k))
m=model('counts-dfs','Eager DFS stores siblings along one active branch','search-count','Full four-ary tree, maximum depth 7. This is a frontier bound, not the memory for a global visited set.')
for depth in range(8):bars(m,[('Pending frontier',1+3*depth),('Active depth',max(0,depth))],r'F=1+(4-1)\cdot'+str(depth)+'='+str(1+3*depth),f'After descending {depth} levels, the frontier contains the next node plus three pending siblings per level.',dict(depth=depth,frontier=1+3*depth))
m=model('negative-edge','Why a negative suffix invalidates UCS stopping','search-graph','This is a deliberately invalid UCS input, shown as a counterexample. The editable UCS laboratory rejects negative edges.')
for k in range(3):
 s=tx(35,35,'S → G costs 2; S → A costs 5; A → G costs −10')+rect(60,140,260,115)+tx(190,185,'Early goal removal','middle')+tx(190,225,'cost = 2','middle',True)+rect(620,140,310,115,'#e9d8b5')+tx(775,185,'True best route: S → A → G','middle')+tx(775,225,'cost = −5','middle',True)+tx(60,355,['The goal enters the queue at cost 2.','UCS selects cost 2 before the prefix of cost 5.','The unseen negative suffix makes the later complete path cheaper.'][k])+tx(60,440,'No negative cycle is required for this stopping-rule counterexample.')
 frame(m,dict(stage=k,returned=2,optimum=-5),s,'Inspect the negative suffix','A prefix no longer lower-bounds every extension when an edge can be negative.',r'5+(-10)=-5<2')
m=model('starvation-main','Infinitely many prefixes remain below the goal cost','cost-contour','A finite animation shows prefixes only. The geometric-series proof establishes the infinite counterexample.','starvation')
for k in range(1,7):
 x=100+800*(1-2**(-k));s=tx(35,35,'The goal waits at cost 1; chain prefixes approach 1 from below.')+f'<line x1="100" y1="245" x2="900" y2="245" stroke="#63828c" stroke-width="2"/>'+tx(100,300,'0','middle',True)+tx(900,300,'1: goal','middle',True)+f'<g data-entity="cost-pointer"><circle cx="{x}" cy="245" r="10" fill="#387184"/></g>'+tx(50,390,f'Prefix k={k}: cost = {2**k-1}/{2**k}; another cheaper prefix remains.')+tx(50,460,'Every edge is positive, but no common positive lower bound exists.')
 frame(m,dict(k=k,numerator=2**k-1,denominator=2**k),s,'Advance one cheaper prefix','No finite number of selected prefixes permits the goal to become minimum cost.',r'g_k=1-2^{-'+str(k)+r'}<1')
m=model('dfs-infinite','DFS can remain on an acyclic infinite branch','search-graph','The displayed prefix is finite; the proof assumes that the first branch continues forever with distinct states.')
for k in range(1,5):
 s=tx(35,35,'The first child extends an infinite chain; the second child is a goal.')+tx(55,165,'S → A1 → A2 → A3 → A4 → ···',is_math=True)+tx(55,260,'The sibling G remains pending at every shown depth.')+f'<g data-entity="depth-cursor"><circle cx="{95+160*k}" cy="190" r="9" fill="#387184"/></g>'+tx(55,390,'Current depth: '+str(k)+'. No state repeats, so cycle checking rejects nothing.')
 frame(m,dict(prefixDepth=k,goalPending=True),s,'Descend along the first branch','Cycle avoidance alone does not establish completeness on an infinite acyclic tree.',r'\text{distinct states}\nRightarrow\text{finite branch}')
m=model('cost-bound','Selected-depth and generated-depth bounds differ','search-count','Each edge costs at least 3/2 and the optimal goal costs 10.')
bars(m,[('Selected depth bound',6),('Generated depth bound',7)],r'\left\lfloor\frac{10}{3/2}\right\rfloor=6', 'A selected node within the optimal-cost contour can have depth at most 6; expanding it can generate depth-7 children.',dict(selectedDepth=6,generatedDepth=7))
m=model('diamonds-main','Reconverging paths versus distinct states','search-count','Each gadget doubles the number of histories and then merges them into one state.')
for k in [1,2,4,8]:bars(m,[('Start-to-end paths',2**k),('Distinct gadget states',1+3*k)],r'\text{paths}=2^{'+str(k)+'}='+str(2**k),f'{k} diamonds produce {2**k} histories but only {1+3*k} states in this explicit gadget construction.',dict(gadgets=k,paths=2**k,states=1+3*k))
m=model('bidir-main','Bidirectional BFS: balanced depth layers','bidirectional-layers','This is an ideal regular-tree growth illustration, not a stopping certificate for arbitrary weighted graphs.','bidirectional')
for k in range(5):
 s=tx(35,35,'Depth-eight solution: expand forward and backward complete layers')
 for i in range(9):s+=rect(40+105*i,180,90,80,'#bcd6d1' if i<=k else '#e9d8b5' if i>=8-k else '#edf3f3')+tx(85+105*i,226,str(i),'middle',True)
 s+=tx(40,355,'Forward depth '+str(k)+'; backward depth '+str(k)+'. At 4 they meet in the middle.')+tx(40,420,'For b=10: one last layer = 100000000; two balanced layers = 20000.')
 frame(m,dict(forwardDepth=k,backwardDepth=k),s,'Advance complete layers','Directed backward search must use predecessor edges, not outgoing edges from the goal.',r'2\cdot10^4=20000')
m=model('grid-main','Monotone grid paths: choose four right moves among seven','grid-path','Only right and up moves are permitted. Every route has exactly seven steps.')
path=[(0,0),(1,0),(2,0),(2,1),(3,1),(3,2),(4,2),(4,3)]
for k,(x,y) in enumerate(path):
 s=tx(35,35,'A 4-by-3 monotone route; one of 35 equally deep paths')
 for i in range(5):
  for j in range(4):s+=rect(120+150*i,120+90*(3-j),100,70,'#d4e4de')+tx(170+150*i,148+90*(3-j),f'{i},{j}','middle',True)
 for (a,b),(c,d) in zip(path[:k],path[1:k+1]):s+=f'<line x1="{170+150*a}" y1="{174+90*(3-b)}" x2="{170+150*c}" y2="{174+90*(3-d)}" stroke="#b47a36" stroke-width="4"/>'
 s+=f'<g data-entity="grid-pointer"><circle cx="{170+150*x}" cy="{174+90*(3-y)}" r="9" fill="#345e78"/></g>'+tx(80,545,'Coordinates denote states; the moving point follows the displayed legal route.')
 frame(m,dict(step=k,state=[x,y],totalPaths=35),s,'Take one legal move','Permuting the four right and three up moves counts all paths.',r'\binom74=35,\quad d=7')
data=dict(topicId='i_uninformed',models=models,groups=groups)
(R/'dist/chapters/i_uninformed-models.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
# Visuals in these two problems must match the failure/weighted scenario, not just the algorithm name.
qpath=B/'i_uninformed-questions.json';qs=json.loads(qpath.read_text());qs[40]['modelId']='finite-cycle-failure';qs[50]['modelId']='costly-dls';qpath.write_text(json.dumps(qs,indent=2)+'\n',encoding='utf-8')
print('Built',len(models),'subject-specific models and',sum(len(m['frames'])for m in models),'checkpoints.')
