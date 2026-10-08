from pathlib import Path
from html import escape as e
from fractions import Fraction as F
from itertools import product
import json,sys,ast
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.SYMBOLS.update(gamma='γ',varnothing='∅')
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
models=[];groups={}
def tx(x,y,s,math=False,anchor='start'):return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="ag-{"math"if math else"label"}">{e(str(s))}</text>'
def rect(x,y,w,h,c='#e6efea'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{c}" stroke="#a2b9b4"/>'
def box(x,y,w,h,lines,hot=False,id=''):
 return f'<g data-entity="{id}">'+rect(x,y,w,h,'#f3deb7'if hot else'#e6efea')+''.join(tx(x+w/2,y+32+i*30,t,math=(' = 'in t or t.startswith(('EU','P('))),anchor='middle')for i,t in enumerate(lines))+'</g>'
def arrow(x1,y1,x2,y2,col='#47768a'):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="2.5" marker-end="url(#ag-arrow)"/>'
def svg(s,h=540):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {h}" role="img" data-visual-type="agent-model"><defs><marker id="ag-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,1 L9,5 L0,9" fill="none" stroke="context-stroke" stroke-width="1.4"/></marker></defs>{s}</svg>'
def model(id,title,kind,invariant,group,guide):
 m=dict(id=id,title=title,kind=kind,invariant=invariant,code=guide,frames=[]);models.append(m);groups.setdefault(group,[]).append(id);return m
def frame(m,state,drawing,op,why,formula,checks):
 state=json.loads(json.dumps(state,default=str));prev=m['frames'][-1]['snapshot']if m['frames']else None
 changes=[dict(field=k,before=prev.get(k),after=v)for k,v in state.items()if prev and prev.get(k)!=v]
 m['frames'].append(dict(snapshot=state,svg=drawing,caption=why,formulaHtml=mathml.render(formula,True),teaching=dict(operation=op,why=why,checks=[dict(mathHtml=mathml.render(a),result=str(b).lower())for a,b in checks],changes=changes,currentState=state,initial=prev is None,reading=m['invariant'],guide=m['code'],activeLine=min(len(m['frames']),len(m['code'])-1),mode=m['kind'])))
def tex(v):v=F(v);return str(v.numerator)if v.denominator==1 else r'\frac{'+str(v.numerator)+'}{'+str(v.denominator)+'}'
def bars(labels,values,hot=-1,title='Expected utility',scale=20):
 s=tx(40,35,title)+f'<line x1="360" y1="90" x2="360" y2="435" stroke="#90a6a5"/>'
 for i,(label,v)in enumerate(zip(labels,values)):
  y=115+i*85;v=float(v);w=abs(v)*scale;x=360 if v>=0 else 360-w
  s+=f'<g data-entity="bar-{i}">'+rect(x,y,max(w,1),40,'#f3deb7'if i==hot else'#bfd5d0')+tx(50,y+27,label)+tx(max(380,x+w+20),y+27,str(values[i]),True)+'</g>'
 return svg(s)

m=model('loop-main','Percept, internal update, action and next state','agent-loop','The selected action affects the next physical state; the percept already received is not rewritten.','loop',['Observe s_t.','Update internal state.','Choose a_t.','Apply the action to obtain s_(t+1).'])
for k in range(4):
 s=tx(40,35,'One control cycle: the physical world and the internal model are distinct')+box(70,130,240,100,['World state','s = (L, 1, 0)'],k==0,'world')+box(380,130,240,100,['Local percept','o = (L, dirty)'],k==1,'percept')+box(690,130,240,100,['Internal update','left dirt = 1'],k==2,'memory')+box(380,340,240,100,['Selected action','Clean'],k==3,'action')+arrow(310,180,380,180)+arrow(620,180,690,180)+f'<path d="M810,230 V390 H620" fill="none" stroke="#47768a" stroke-width="2.5" marker-end="url(#ag-arrow)"/>'+f'<path d="M380,390 H190 V230" fill="none" stroke="#47768a" stroke-width="2.5" marker-end="url(#ag-arrow)"/>'+tx(85,490,'After execution: next world state = (L, 0, 0); observe again.')
 frame(m,dict(phase=k,physical=['L',1,0],nextPhysical=['L',0,0]),svg(s),'Follow cycle phase '+str(k+1),'Memory describes the world but is not itself the physical world.',r'T((L,1,0),\text{Clean})=(L,0,0)',[(r'2\cdot2^2=8',True)])
m=model('risk-main','Expected utility and the realized outcome','utility-bars','The risky action has expectation 26/5; its negative branch remains possible.','utility',['Write every payoff and probability.','Multiply then add.','Compare the expectation with safe.'])
for k in range(3):frame(m,dict(stage=k,safe=4,risky='26/5'),bars(['Safe expectation','Risky expectation','Possible risky loss'],[F(4),F(26,5),F(-2)],k,scale=55),'Compare expectation and realization','A lower realized result does not retrospectively alter the available-information optimum.',r'\frac35\,10+\frac25(-2)=\frac{26}5>4',[(r'\frac{26}5-4=\frac65',F(26,5)-4==F(6,5))])
m=model('threshold-main','The exact probability threshold','probability-threshold','A = (12, −4), B = (5, 5); the threshold is 9/16, not 1/2.','utility',['Compute EU(A)=16p−4.','Compute EU(B)=5.','Locate the sign of 16p−9.'])
for p in[F(0),F(1,2),F(9,16),F(3,4),F(1)]:
 x=100+800*float(p);cut=100+800*9/16;s=tx(40,35,'Probability axis: action changes only at the derived utility threshold')+rect(100,165,450,54,'#dbe8ed')+rect(550,165,350,54,'#e4e9d5')+f'<line x1="100" y1="192" x2="900" y2="192" stroke="#607b83"/>'+tx(100,250,'0',True)+tx(900,250,'1',True,'middle')+tx(cut,125,'9/16: tie',True,'middle')+f'<line x1="{cut}" y1="137" x2="{cut}" y2="220" stroke="#9b673d" stroke-width="2"/>'+f'<g data-entity="probability"><circle cx="{x}" cy="192" r="9" fill="#325d74"/>'+tx(x,295,'p = '+str(p),True,'middle')+'</g>'+tx(100,365,'EU(A) = '+str(16*p-4)+'; EU(B) = 5',True)+tx(100,420,'Best: '+('A and B'if p==F(9,16)else'A'if p>F(9,16)else'B'))
 frame(m,dict(prior=str(p),A=str(16*p-4),B='5'),svg(s),'Change the actual prior','The pointer moves along a fixed probability axis; the numerical checkpoint is exact.',r'EU(A)-EU(B)=16p-9',[(tex(16*p-9)+r'='+tex(16*p-4-5),True)])
m=model('alias-main','Identical percept, incompatible history-dependent optima','history-aliasing','Both histories end with the same sensor symbol, but the uniquely correct actions differ.','aliasing',['Retain the histories.','Compare their last percepts.','Compare their optimal-action sets.'])
for k in range(3):
 s=tx(40,35,'An information conflict, not a missing search algorithm')+box(60,120,260,110,['History h1','key was collected'],k==0,'h1')+box(60,310,260,110,['History h2','key was not collected'],k==1,'h2')+box(420,215,220,100,['Same percept','at door X'],k==2,'shared')+box(760,120,180,110,['Best action','Open'],k==0,'open')+box(760,310,180,110,['Best action','Find key'],k==1,'find')+arrow(320,175,420,235)+arrow(320,365,420,295)+arrow(640,235,760,175)+arrow(640,295,760,365)+tx(60,490,'One current-percept-only output cannot implement both distinct unique optima.')
 frame(m,dict(stage=k,optima=['Open','Find key']),svg(s),'Expose the aliased histories','Store a key bit or obtain another observation; changing the rule alone cannot recover omitted information.',r'\{\text{Open}\}\cap\{\text{Find key}\}=\varnothing',[(r'\text{the two required actions are equal}',False)])
m=model('common-action','Hidden states can share the same best action','payoff-table','Partial observability does not force a loss when every hidden state has the same maximizing action.','aliasing',['Read both hidden states.','Compare A and B in each.','Intersect maximizing sets.'])
for k in range(3):
 s=tx(40,35,'One ambiguous observation, one common optimal action')+box(80,130,330,130,['Hidden H: A = 5, B = 1','Hidden L: A = 5, B = 1'],k<2,'payoffs')+box(590,130,300,130,['M(H) = {A}','M(L) = {A}'],k==2,'intersection')+arrow(410,195,590,195)+tx(85,350,'For every p in [0, 1], EU(A) = 5 and EU(B) = 1.',True)
 frame(m,dict(stage=k,commonAction='A'),svg(s),'Find the common maximizer','State uncertainty remains, but it does not change this decision.',r'5p+5(1-p)=5',[(r'5>1',True)])
m=model('posterior-main','Bayes update: joint mass before normalization','belief-bars','Prior H=3/10; positive likelihoods are 4/5 and 1/5. Normalize joint mass, not likelihood alone.','belief',['Read the prior.','Multiply by signal likelihood.','Normalize positive mass.','Check the negative branch.'])
for label,p,prob in[('Prior',F(3,10),F(1)),('After positive',F(12,19),F(19,50)),('After negative',F(3,31),F(31,50))]:
 s=tx(40,35,label+': posterior H mass on a unit probability bar')+rect(90,155,800*float(p),90,'#b6d4d0')+rect(90+800*float(p),155,800*float(1-p),90,'#e9d6b3')+tx(90,300,'P(H) = '+str(p)+'; P(L) = '+str(1-p),True)+tx(90,355,'Branch probability = '+str(prob),True)+tx(90,420,'H and L are the complete mutually exclusive hidden-state alternatives.')
 frame(m,dict(branch=label,posteriorH=str(p),branchProbability=str(prob)),svg(s),'Condition on '+label.lower(),'The bar lengths represent exact probabilities; numerical values use rational arithmetic.',r'P(H)='+tex(p)+r',\quad P(L)='+tex(1-p),[(tex(p)+'+'+tex(1-p)+'=1',p+(1-p)==1)])
m=model('voi-main','A signal-contingent decision tree','information-tree','Compare each signal branch after optimizing its action; then average and subtract sensing cost.','belief',['Compute prior utility.','Choose A after positive.','Choose B after negative.','Average and subtract cost.'])
for k in range(4):
 s=tx(40,35,'Actual model: prior 3/10; positive likelihoods 4/5 and 1/5')+box(60,215,230,100,['Buy signal','cost = 1/4'],k==0,'sensor')+box(450,100,200,100,['Positive','P = 19/50'],k==1,'positive')+box(450,330,200,100,['Negative','P = 31/50'],k==2,'negative')+box(790,100,160,100,['Choose A','EU = 116/19'],k==1,'A')+box(790,330,160,100,['Choose B','EU = 5'],k==2,'B')+arrow(290,240,450,150)+arrow(290,290,450,380)+arrow(650,150,790,150)+arrow(650,380,790,380)+tx(60,490,'Prior best = 5; free-signal value = 271/50; net = 517/100.',True)
 frame(m,dict(stage=k,priorValue='5',signalValue='271/50',netValue='517/100'),svg(s),'Evaluate signal policy phase '+str(k+1),'Each leaf is a conditional optimized utility, not an unweighted payoff.',r'\frac{19}{50}\frac{116}{19}+\frac{31}{50}5-\frac14=\frac{517}{100}',[(r'\frac{517}{100}-5=\frac{17}{100}',True)])
def vacuumdraw(state,title='Known physical vacuum state'):
 x,l,r=state;s=tx(40,35,title)+box(80,130,350,230,['Room L','Dirty'if l else'Clean'],False,'room-L')+box(570,130,350,230,['Room R','Dirty'if r else'Clean'],False,'room-R')
 for xx,dirty in[(255,l),(745,r)]:
  if dirty:s+=''.join(f'<circle cx="{xx-45+i*30}" cy="225" r="7" fill="#a47850"/>'for i in range(4))
 xx=255 if x=='L'else 745;s+=f'<g data-entity="robot"><circle cx="{xx}" cy="295" r="27" fill="#376b83"/>'+tx(xx,302,'R',anchor='middle')+'</g>'+tx(80,420,'Physical state = '+str(tuple(state)),True)+tx(80,470,'Only current-room dirt is observed; other dirt needs memory or belief.')
 return svg(s)
m=model('vacuum-main','Two local cleans and one necessary move','vacuum-motion','Reliable actions, unit cost and no dirt recurrence: the shown three-action plan is optimal.','vacuum',['Read (L,1,1).','Clean left.','Move right.','Clean right.'])
for i,s in enumerate([['L',1,1],['L',0,1],['R',0,1],['R',0,0]]):frame(m,dict(position=s[0],leftDirt=s[1],rightDirt=s[2],cost=i),vacuumdraw(s),['Initial state','Clean','Right','Clean'][i],'Two initially dirty rooms require two local cleans and one connecting move.',r'g='+str(i),[(r'\text{both rooms are clean}',s[1]+s[2]==0)])
m=model('sensorless-main','Belief propagation without a sensor','vacuum-belief-set','Right, Clean, Left, Clean reduces all eight states to one goal state; no observation is invented.','vacuum',['Begin with eight states.','Right merges locations.','Clean removes right dirt.','Left moves all possibilities.','Clean removes left dirt.'])
belief=list(product(['L','R'],[0,1],[0,1]));actions=['Initial','Right','Clean','Left','Clean']
for k,a in enumerate(actions):
 if k:
  nxt=[]
  for x,l,r in belief:
   if a=='Right':x='R'
   elif a=='Left':x='L'
   elif x=='L':l=0
   else:r=0
   nxt.append((x,l,r))
  belief=sorted(set(nxt))
 s=tx(40,35,'Sensorless belief after '+a+'; support size = '+str(len(belief)))
 for i,(x,l,r)in enumerate(belief):s+=box(55+(i%4)*240,120+(i//4)*145,210,100,[f'Robot: {x}',f'dL = {l}; dR = {r}'],False,'state-'+str(i))
 s+=tx(55,455,'These are possible physical states, not independent simulated worlds.')
 frame(m,dict(action=a,belief=[list(z)for z in belief],size=len(belief)),svg(s),'Propagate '+a,'Set images merge duplicate successors. No observations are used in this model.',r'|B|='+str(len(belief)),[(r'\text{every possible state is a clean goal}',all(l==r==0 for x,l,r in belief))])
m=model('key-main','A key bit repairs an invalid state abstraction','state-legality-graph','At the same position X, Open has different legality depending on key possession.','abstraction',['Inspect key absent.','Inspect key present.','Retain the distinguishing bit.'])
for k in[0,1]:
 s=tx(40,35,'Physical location is identical; legal actions are not')+box(80,170,290,130,['At door X','Key bit = '+str(k)],True,'door')+box(680,170,240,130,['Goal room','Open succeeds'if k else'Open unavailable'],False,'goal')
 if k:s+=arrow(370,235,680,235)
 else:s+=f'<line x1="405" y1="210" x2="455" y2="260" stroke="#a35361" stroke-width="4"/><line x1="405" y1="260" x2="455" y2="210" stroke="#a35361" stroke-width="4"/>'+tx(490,245,'No legal edge')
 s+=tx(80,400,'State must retain (position, key), not position alone.')
 frame(m,dict(position='X',key=k,openLegal=bool(k)),svg(s),'Check Open legality','A missing key is a missing precondition, not a different arrow label on the same exact abstract edge.',r'|\{0,1\}|=2',[(r'\text{Open is legal}',bool(k))])
m=model('graph-main','Different paths produce different search nodes','state-versus-node','Two paths can end at the same goal state but have different parent records and costs.','graph',['Read both paths.','Compute action count.','Compute path cost.'])
for k in range(3):
 s=tx(40,35,'One start and one goal, two path records')+box(70,210,160,100,['Start S'],False,'S')+box(400,90,160,100,['A1','cost so far 100'],k==0,'A1')+box(330,340,160,100,['B1','cost so far 1'],k==1,'B1')+box(580,340,160,100,['B2','cost so far 2'],k==1,'B2')+box(790,210,160,100,['Goal G'],k==2,'G')+arrow(230,235,400,140)+arrow(560,140,790,235)+arrow(230,285,330,390)+arrow(490,390,580,390)+arrow(740,390,790,285)+tx(70,495,'A: depth 2, cost 200. B: depth 3, cost 3.',True)
 frame(m,dict(stage=k,depths=[2,3],costs=[200,3]),svg(s),'Separate state identity from path bookkeeping','Goal state equality does not imply equal search-node path cost.',r'2<3,\qquad200>3',[(r'100+100=200',True),(r'1+1+1=3',True)])
m=model('cycle-main','A self-loop generates infinitely many prefixes','state-cycle','There are two states but a distinct goal path for every number of self-loop repetitions.','graph',['Repeat the self-loop k times.','Take the goal edge.','Compare state count and path count.'])
for k in range(4):
 s=tx(40,35,'Finite graph; arbitrarily long action history')+box(160,200,200,100,['State X','loop count = '+str(k)],True,'X')+box(690,200,200,100,['State G'],False,'G')+arrow(360,250,690,250)+f'<path d="M210,200 V110 H310 V200" fill="none" stroke="#47768a" stroke-width="2.5" marker-end="url(#ag-arrow)"/>'+tx(450,230,'goal action')+tx(160,420,'Path: '+('Loop, '*k)+'Goal')
 frame(m,dict(loops=k,depth=k+1,states=2),svg(s),'Choose '+str(k)+' self-loop repetitions','The search node remembers a path prefix; the physical vertex X is the same after every loop.',r'd=k+1',[(str(k)+'+1='+str(k+1),True)])
m=model('horizon-main','Discounted return changes the preferred action','discount-bars','A pays 6 then −10; B pays 1 then 8. Compare full two-step returns, not the first reward alone.','utility',['Weight the later reward.','Sum each return.','Compare with the exact tie 5/18.'])
for g in[F(0),F(1,4),F(5,18),F(1,2),F(1)]:frame(m,dict(discount=str(g),A=str(6-10*g),B=str(1+8*g)),bars(['A: 6 − 10 gamma','B: 1 + 8 gamma'],[6-10*g,1+8*g],title='Discount gamma = '+str(g),scale=30),'Change the discount','Future outcomes use the same stated discount in both alternatives.',r'G_A-G_B=5-18\gamma',[(tex(6-10*g-(1+8*g))+'='+tex(5-18*g),True)])
m=model('takeaway-main','An inductive winning policy executed on actual counters','counter-game','Normal play: remove one or two; the player taking the last wins. Agent leaves multiples of three.','graph',['Start at 14.','Remove the remainder modulo three.','After an opponent move, restore a multiple of three.'])
seq=[14,12,11,9,7,6,5,3,1,0]
for i,n in enumerate(seq):
 s=tx(40,35,'One legal play: '+('initial state'if not i else('Agent'if i%2 else'Opponent')+' removed '+str(seq[i-1]-n)))
 for j in range(14):s+=f'<g data-entity="counter-{j}"><circle cx="{95+(j%7)*130}" cy="{165+(j//7)*140}" r="30" fill="{"#4b8491"if j<n else"#edf1ef"}" stroke="#96afb1"/>'+tx(95+(j%7)*130,172+(j//7)*140,str(j+1),True,'middle')+'</g>'
 s+=tx(55,440,'Counters left = '+str(n)+'; agent acts on odd-numbered transitions.',True)
 frame(m,dict(counters=n,lastRemoval=seq[i-1]-n if i else 0,turn=i),svg(s),'Execute the stated move','The exact count is discrete; removed counters fade rather than pretending to split continuously.',r'n='+str(n),[(r'\text{last removal is legal}',i==0 or seq[i-1]-n in[1,2])])
m=model('peas-main','PEAS keeps sensing and acting separate','task-specification','A delivery task needs a measurable score, environment, control channels and observation channels.','loop',['State the outcome score.','Identify the environment.','List actuators.','List sensors.'])
for k in range(4):
 s=tx(40,35,'Delivery robot task specification')
 for i,(h,ls)in enumerate([('Performance',['Deliveries, delay','energy, collisions']),('Environment',['Corridors, doors','people, packages']),('Actuators',['Drive, stop','load command']),('Sensors',['Position, obstacle range','battery, package status'])]):s+=box(60+(i%2)*470,105+(i//2)*190,410,145,[h,*ls],i==k,'peas-'+str(i))
 frame(m,dict(component=k),svg(s),'Inspect PEAS component '+str(k+1),'A motor command is not a sensor reading, and an outcome score is not an actuator.',r'J=10D-2L-E-100C',[(r'10(3)-2(2)-4-100(0)=22',True)])
m=model('learning-main','Learning changes a component, not just a data counter','learning-architecture','Performance, feedback, updating and exploration have distinct roles; they can be implemented in one program.','loop',['Act using the current policy.','Evaluate task feedback.','Update a relevant component.','Choose informative experience when worthwhile.'])
for k in range(4):
 s=tx(40,35,'Functional learning-agent decomposition')+box(70,120,300,100,['Performance element','chooses an action'],k==0,'performance')+box(630,120,300,100,['Critic','evaluates task feedback'],k==1,'critic')+box(630,350,300,100,['Learning element','updates model or policy'],k==2,'learning')+box(70,350,300,100,['Exploration mechanism','selects useful experience'],k==3,'explore')+arrow(370,170,630,170)+arrow(780,220,780,350)+arrow(630,400,370,400)+arrow(220,350,220,220)
 frame(m,dict(component=k),svg(s),'Inspect learning role '+str(k+1),'Data quantity alone does not choose the target, prior assumptions or feedback type.',r'\text{net exploration gain}\le2-5=-3',[(r'2-5=-3',True)])
m=model('regret-main','Regret compares against the best in each state','regret-table','Payoffs A=(10,0), B=(6,5), C=(0,8); statewise best values are 10 and 8.','utility',['Find the best payoff per state.','Subtract each action payoff.','Take maximum regret per action.'])
for k in range(3):
 s=tx(40,35,'Statewise regret, not subtraction from one global maximum')
 for i,(name,values)in enumerate([('A',[0,8]),('B',[4,3]),('C',[10,0])]):s+=box(65+i*310,140,270,160,[name,'Regrets: '+str(values),'Maximum: '+str(max(values))],i==k,'regret-'+name)
 s+=tx(70,410,'Minimax regret chooses B because 4 is the smallest maximum.',True)
 frame(m,dict(action=['A','B','C'][k],regrets=[[0,8],[4,3],[10,0]][k]),svg(s),'Compute one action regret','Each column uses its own best available payoff.',r'\min\{8,4,10\}=4',[(r'10-6=4',True),(r'8-5=3',True)])
data=dict(topicId='i_agents',models=models,groups=groups)
(R/'dist/chapters/i_agents-models.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
(B/'i_agents-evidence/models.json').write_text(json.dumps(dict(models=len(models),checkpoints=sum(len(m['frames'])for m in models),inventory=[dict(id=m['id'],kind=m['kind'],checkpoints=len(m['frames']))for m in models]),indent=2)+'\n',encoding='utf-8')
print(len(models),'models,',sum(len(m['frames'])for m in models),'checkpoints')
