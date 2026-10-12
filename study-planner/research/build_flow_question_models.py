from pathlib import Path
import json,math,sys,re
B=Path(__file__).parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
def state(kind,formula,caption,**data):
 return dict(nodes=[],edges=[],snapshot=dict(kind=kind,**data),caption=caption,captionHtml='<p>'+caption+'</p>',formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True).replace('<mo>-</mo>','<mo>−</mo>')+'</div>',line=0,metrics={},teaching=dict(operation=caption.split('.')[0],why=caption,currentState=data,initial=False,activeLine=0,changes=[],checks=[],reading='Read the named control checkpoint and actual data together. An event count is attached to its own operation. A skipped update has no invented side effect, and an undefined expression has no numeric C output.'))
S={}
def scene(name,title,description,frames):
 frames[0]['teaching']['initial']=True;S['flow-question-'+name]=dict(id='flow-question-'+name,title=title,description=description,descriptionHtml='<p>'+description+'</p>',invariant=description,visual=dict(type='enumeration',claim=description),code=['Trace the actual control edge and state; verify the named count, invariant and domain'],frames=frames)
scene('triples','Original PhD Q20: dependent bounds and shifted triples','The actual upper bound is fifteen. Middle-index rows aggregate their exact allowed source pairs rather than drawing a misleading independent15×15×15 cube.',[state('triples',r'\sum_{j=1}^{15}j(16-j)=680,\quad10+680=690',f'Checkpoint {k+1}: '+['read the weakly ordered index domain','count pairs with each fixed middle index','map to distinct shifted triples','add the initialized accumulator separately'][k],stage=k,rows=[[j,j,16-j,j*(16-j)] for j in range(1,16)]) for k in range(4)])
scene('split','Original SplitSort: the greater block comes first','A representative distinct input[5,1,4,2,3] uses actual input pivot3. Sorting-permutation semantics require an input order statistic, not an average that adds an extra value.',[state('split',r'(5,4)\Vert(3)\Vert(2,1)=(5,4,3,2,1)',cap,stage=i) for i,cap in enumerate(['Partition the actual input around member3: greater[5,4], smaller[1,2].','Recursively return the descending greater block[5,4].','Recursively return the descending smaller block[2,1].','Join greater, pivot, smaller; the whole result is descending and preserves the five original values.'])])
for n,name in [(6,'copy-source'),(10,'copy10')]:
 frames=[state('copy',rf'n_0={n},\quad i_0=0',f'Initial call: source index {n}, destination index0; no copy has occurred yet.',sourceSize=n+1,source=n,dest=[],negative=False,offset=0,stride=1)];dest=[]
 for t,src in enumerate(range(n,-1,-2)):
  dest.append(src);frames.append(state('copy',rf'n_t={n}-2\cdot{t}={src},\quad i_t={t}',f'Read source index {src}, then write that value into dense destination index {t}. The source is still nonnegative at this call.',sourceSize=n+1,source=src,dest=list(dest),negative=False,offset=0,stride=1))
 frames.append(state('copy',rf'n_{{{len(dest)}}}={n}-2\cdot{len(dest)}={n-2*len(dest)}<0',f'Base call source {n-2*len(dest)}: the guard returns before any array read. There were {len(dest)} writes and {len(dest)+1} total calls.',sourceSize=n+1,source=n-2*len(dest),dest=list(dest),negative=True,offset=0,stride=1))
 if name=='copy-source':
  for offset,stride in [(1,1),(0,2),(1,2)]:
   frames.append(state('copy',rf'\text{{Destination at copy }}t={stride}t+{offset}',f'Changed source option: destination positions {offset}, {stride+offset}, {2*stride+offset}. Source stride remains two; this variant changes destination offset or density.',sourceSize=n+1,source=0,dest=list(dest),negative=False,offset=offset,stride=stride,variant=True))
 scene(name,'Reverse-stride array reads and destination positions','Array cells display source indices as symbolic payloads so the preserved element identity is visible. The specific source-size example is declared; the original algorithm question remains general.',frames)
scene('dangling','Actual outer-false path and statement ownership','The else belongs to the inner if. An unvisited inner condition is distinct from a condition that ran and returnedfalse.',[state('dangling',r'a=0,\quad b=1,\quad x=0',cap,stage=i) for i,cap in enumerate(['Parse the outer if owning the entire inner if/else.','Evaluate outer a=0: false; the inner guard is not evaluated.','Skip both assignments and retain initialized x=0.'])])
for mode,n,name in [('odd',6,'filter-odd'),('third',15,'filter-third'),('sum',5,'sum-before')]:
 start=0 if mode=='sum' else 1;frames=[state('trace',rf'i={start},\quad s=0','Initial guard checkpoint: no body entries, accumulator operations or index updates have occurred.',rows=[],values=[['body entries',0],['updates completed',0],['accumulator',0]],phase='guard',exit=False)];total=0;rows=[];entries=0;updates=0
 for i in range(0 if mode=='sum' else 1,n if mode=='sum' else n+1):
  entries+=1;accept=mode=='sum' or (i%2==1 if mode=='odd' else i%3!=0);total+=i if mode in ['odd','sum'] and accept else 1 if accept else 0
  rows.append([i,'add '+str(i) if mode in ['odd','sum'] and accept else 'increment s' if accept else 'continue',total]);frames.append(state('trace',rf'i={i},\quad s={total}',f'Body checkpoint at i={i}: '+('perform the counted accumulator action.' if accept else 'continue skips the accumulator but reaches the for update.')+' The header update has not yet completed for this entry.',rows=list(rows[-5:]),values=[['body entries',entries],['updates completed',updates],['accumulator',total]],phase='body' if accept else 'continue',exit=False))
  updates+=1
 final_i=n if mode=='sum' else n+1;frames.append(state('trace',rf'i={final_i},\quad s={total}',f'The last index update completed and the final guard failed. Entries {entries}, updates {updates}, guard tests {entries+1}.',rows=list(rows[-5:]),values=[['body entries',entries],['updates completed',updates],['accumulator',total]],phase='exit',exit=True))
 scene(name,'Actual accumulator and continuation checkpoints','A compact history table shows the actual current entry and the distinct event counters. Native formulas describe this checkpoint, not an invariant asserted at every intermediate instruction.',frames)
scene('switch','Original switch entry2, fallthrough and break','Dispatch is one entry jump. The subsequent labels are reached by ordinary execution, not independent condition tests.',[state('switch',rf'x={x}',cap,stage=i,x=x) for i,(x,cap) in enumerate([(0,'Dispatch to case2; case1 is not entered.'),(2,'Add two at case2, then fall through to case3.'),(6,'Add four at case3, obtaining six.'),(6,'Break exits before default; x remains six.')])])
for target,name in [(1,'orbit-unreachable'),(64,'orbit-target')]:
 ticks=[0,1,2,32,64,96,128];frames=[]
 for t in ticks:
  value=(6*t)%256;extension=target==64 and t>96;frames.append(state('orbit',rf'6\cdot{t}\bmod256={value}',('Counterfactual full-orbit extension after the target-stopping loop ended: ' if extension else '')+f'after {t} updates the residue is {value}. '+('Target one is outside the even subgroup.' if target==1 else 'The first target64 hit is96; period128 is a separately analyzed return tozero.'),t=t,value=value,target=target,period=128,hit=target==value,extension=extension))
 scene(name,'Modulo256 orbit: target '+str(target),'The128 points are actual reachable even residues, ordered by update time around the orbit. Their position is not ordinary numeric magnitude; each selected checkpoint prints its exact residue.',frames)
scene('postfix','A failed postfix guard still updates its object','Each row records the old compared value, the resulting stored value and whether the body count changed.',[state('postfix',rf'x={old+1},\quad c={min(old+1,3)}',f'Guard compares old x={old}; its result is {old<3}. Stored x becomes {old+1}; '+('the body increments c.' if old<3 else 'the body is skipped, so c stays3.'),stage=old,rows=[[x,x+1,'true' if x<3 else 'false',min(x+1,3)] for x in range(old+1)]) for old in range(4)])
v=S['flow-question-postfix'];v['frames'].insert(0,state('postfix',r'x=0,\quad c=0','Initial objects are both zero; the first postfix guard has not yet executed.',stage=-1,rows=[]));v['frames'][0]['teaching']['initial']=True;v['frames'][1]['teaching']['initial']=False
frames=[state('trace',r'i=j=0','Initial left-guard checkpoint: both counters are zero.',rows=[],values=[['i',0],['j',0],['body entries',0]],phase='left guard',exit=False)];history=[]
for t in range(5):
 history.append([t,t+1,'right ++j']);frames.append(state('trace',rf'i={t},\quad j={t+1}',f'At left guard i={t}<5, evaluate ++j and obtain {t+1}>0. The body has not yet incremented i.',rows=list(history[-5:]),values=[['i',t],['j',t+1],['body entries',t]],phase='right guard',exit=False))
 history.append([t+1,t+1,'body ++i']);frames.append(state('trace',rf'i=j={t+1}',f'The body restores equality at the next left-guard checkpoint: i=j={t+1}.',rows=list(history[-5:]),values=[['i',t+1],['j',t+1],['body entries',t+1]],phase='body completed',exit=False))
frames.append(state('trace',r'i=j=5','Final left guard is false, so ++j is not evaluated. Both objects remainfive.',rows=list(history[-5:]),values=[['i',5],['j',5],['body entries',5]],phase='exit: right skipped',exit=True))
scene('stateful','Left and right guard effects, then body restoration','Original n=5 conditional evaluation shows a temporary i/j difference inside the guard, then restoration by the body; the final left-only false test skips the second increment.',frames)
seq=[13,12,6,3,2,1,0];frames=[]
for i,v in enumerate(seq):frames.append(state('ranking',rf'n={v},\quad\operatorname{{popcount}}(n)={v.bit_count()}',f'Current positive ranking value {v}.' if v else 'Zero guard exits. Three halvings and three odd subtractions made six transitions.',stage=i,sequence=seq,n=v,pop=v.bit_count(),bitLength=v.bit_length()))
scene('ranking','Both branches decrease n, but not every popcount','The actual13 trajectory is shown. Halving preserves population count, so it is not misrepresented as a strictly decreasing measure at each transition.',frames)
frames=[state('nested',r'c=0','Initial counter zero; neither loop initializer has established an index value yet.',i=None,j=None,total=0,broke=False)];total=0
for i in range(1,4):
 for j in range(1,4):
  broke=j==3
  if not broke:total+=1
  frames.append(state('nested',rf'i={i},\quad j={j},\quad c={total}',f'Outer entry {i}, inner entry {j}: '+('break exits only the inner loop before increment.' if broke else 'increment the counter.'),i=i,j=j,total=total,broke=broke))
scene('nested','Break targets the inner loop, leaving outer work active','Three outer entries each make two increments, while their third inner entry breaks. The enclosing frames and transfer destination are explicit.',frames)
frames=[state('threshold',r'S_0=0,\quad H=15','Initial empty sum is zero; threshold15 is positive.',i=0,sum=0,threshold=15,hit=False,history=[0])];total=0
for i in range(1,6):
 total+=i;frames.append(state('threshold',rf'S_{{{i}}}={total},\quad H=15',f'After addition {i}, sum is {total}. '+('It first reaches15, so break precedes the next index update.' if i==5 else 'The threshold is not yet reached.'),i=i,sum=total,threshold=15,hit=i==5,history=[k*(k+1)//2 for k in range(i+1)]))
scene('threshold','First positive threshold at an after-addition checkpoint','The actual n=5 threshold15 grows through1,3,6,10,15. The first qualifying test is shown before any invented further update.',frames)
scene('binary-tree','Total binary calls versus an active single stack path','A complete depth-three representative tree has15calls and at mostfour active frames in sequential traversal. The original n=5 bank count63 is separately labeled.',[state('binary',r'C(3)=1+2+4+8=15,\quad C(5)=63',cap,stage=i,depth=3) for i,cap in enumerate(['Count the representative root invocation.','Count both children at depthone.','Count four depth-two invocations.','Include all eight zero-parameter leaves; current stack remains one path, not the whole historical tree.'])])
scene('toll','One-child recursion with actual local operation tolls','The original n=5 path performs5,4,3,2,1local operations; onechild does not imply constant per-call work. A_t counts the first t descending tolls; W(5)=15 is the full-work value.',[state('toll',rf'A_{{{i+1}}}={sum(range(5-i,6))}',f'Account for parameter {5-i}: local toll {5-i}; accumulated accounted work A_{i+1}={sum(range(5-i,6))}.',stage=i,tolls=[5,4,3,2,1],total=sum(range(5-i,6))) for i in range(5)])
scene('swap','Read the state left by the preceding assignment','For original n=5, the intermediate sum7 is representable. A separate INT_MAX+2 case would stop as undefined before any invented swapped output.',[state('swap',rf'a={a},\quad b={b}',cap,stage=i,rows=[[5,2],[7,2],[7,5],[2,5]],a=a,b=b) for i,(a,b,cap) in enumerate([(5,2,'Read original objects a=5,b=2.'),(7,2,'First assignment sums original values: a becomes7.'),(7,5,'Second reads updated a=7 and old b=2: b becomes5.'),(2,5,'Third reads both updated values: a becomes2, completing the swap.')])])
scene('posttest','A signed decrement precedes its first guard','The actual n=5 posttest path goes4,3,2,1,0,−1. The final negative guard result is signed, not an unsigned wrap.',[state('posttest',r'i=5,\quad t=0','Initial state has i=5 and no preliminary guard; the body is entered next.',i=5,count=0,stage=-1,history=[])]+[state('posttest',rf'i={v},\quad t={t}',f'Body execution {t} decrements to {v}; trailing guard i>=0 is {v>=0}.',i=v,count=t,stage=t-1,history=list(range(4,v-1,-1))) for t,v in enumerate(range(4,-2,-1),1)])
scenarios=[(8,False),(8,True),(9,False),(9,True)];frames=[]
for stop,first in scenarios:
 rows=[];total=0;final=11
 for i in range(1,11):
  if first and i==stop:rows.append([i,'break',total]);final=i;break
  if i%3==0:rows.append([i,'continue',total]);continue
  if i==stop:rows.append([i,'break',total]);final=i;break
  total+=i;rows.append([i,'add',total])
 frames.append(state('priorities',rf's={total},\quad i={final}',f'Break target {stop}, '+('break-first' if first else 'continue-first')+f': final(s,i)=({total},{final}). Target8 has disjoint predicates; target9 creates genuine priority overlap.',rows=rows,stop=stop,first=first,sum=total,index=final))
scene('priorities','Original disjoint tests and overlapping break9 extension','The two original break8 traces yield the same final pair. Only the declared changed break9 target creates the different numerical results.',frames)
forms=[r'1\le i\le j\le k\le15',r'\sum_{j=1}^{15}j(16-j)=680',r'(i,j,k)\mapsto(i,j+1,k+2)',r'10+680=690']
for f,form in zip(S['flow-question-triples']['frames'],forms):f['formula']=form;f['formulaHtml']='<div class="formula-block">'+mathml.render(form,True).replace('<mo>-</mo>','<mo>−</mo>')+'</div>'
def prose(text):
 text=re.sub(r'\b(upper bound|independent|step|call|depth|target|input|output|count|parameter|has|gives|plus|initial|through|size|source|remain|case|at|to|of|with|break|pivot|stride|position|index|times|sum|calls|leaves)(?=\d)',r'\1 ',text)
 text=re.sub(r'(?<=\d)(?=(?:calls|increments|local|of|reachable)\b)',' ',text)
 return text.replace('at mostfour','at most four').replace('remainfive','remain five').replace('tozero','to zero')
for model in S.values():
 model['title']=prose(model['title']);model['description']=prose(model['description']);model['descriptionHtml']='<p>'+model['description']+'</p>';model['invariant']=prose(model['invariant'])
 for f in model['frames']:f['caption']=prose(f['caption']);f['captionHtml']='<p>'+f['caption']+'</p>';f['teaching']['why']=f['caption'];f['teaching']['operation']=prose(f['teaching']['operation'])
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text());d['scenes'].update(S);p.write_text(json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n')
(B/'deep-library-revision/p_flow-models.json').write_text(json.dumps({k:dict(kind=v['frames'][0]['snapshot']['kind'],frames=len(v['frames'])) for k,v in S.items()},indent=2)+'\n')
print({'models':len(S),'checkpoints':sum(len(v['frames']) for v in S.values())})
