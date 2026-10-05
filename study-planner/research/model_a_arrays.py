"""Concept-specific memory geometry with exact checkpoint states."""
from pathlib import Path
from html import escape as e
import sys,json,math
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.wrap_display=lambda value:value
from mathml import render
models=[];groups={}
def tx(x,y,t,size=16,cl='',box=None):
 attrs=f' dominant-baseline="middle" data-label-for="{e(box)}"' if box else ''
 return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" class="{cl}"{attrs}>{e(str(t))}</text>'
def rounded(points,r=6):
 out=f'M{points[0][0]},{points[0][1]}'
 for a,b,c in zip(points,points[1:],points[2:]):
  la=math.dist(a,b);lc=math.dist(b,c);rr=min(r,la/2,lc/2)
  if not la or not lc:continue
  p=(b[0]+(a[0]-b[0])*rr/la,b[1]+(a[1]-b[1])*rr/la)
  q=(b[0]+(c[0]-b[0])*rr/lc,b[1]+(c[1]-b[1])*rr/lc)
  out+=f' L{p[0]},{p[1]} Q{b[0]},{b[1]} {q[0]},{q[1]}'
 return out+f' L{points[-1][0]},{points[-1][1]}'
def edge(points,source,target,kind='forward'):
 colors=dict(forward='#557e91',backward='#b17d55',pointer='#7a739d')
 a,b=points[0],points[-1]
 return f'<path class="diagram-edge" data-arrow="true" data-source="{e(source)}" data-target="{e(target)}" data-points="{json.dumps(points)}" data-start="{a[0]},{a[1]}" data-end="{b[0]},{b[1]}" d="{rounded(points)}" stroke="{colors[kind]}" stroke-width="1.6" stroke-linejoin="round" fill="none" marker-end="url(#arrow-{kind})"/>'
def path(x,y,u,v,color='#537f91',curve=False,source='',target=''):
 # Matrix adjacency uses exact boundary ports too; no oversized stroke-scaled marker.
 return edge([(x,y),(u,v)],source,target,'backward' if color=='#b57952' else 'forward')
def svg(body,height=410):
 defs=''.join(f'<marker id="arrow-{k}" markerUnits="userSpaceOnUse" markerWidth="7" markerHeight="6" viewBox="0 0 7 6" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="{c}"/></marker>' for k,c in [('forward','#557e91'),('backward','#b17d55'),('pointer','#7a739d')])
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {height}" role="img"><defs>'+defs+'</defs>'+body+'</svg>'
def array(values,y=100,label='Buffer',offset=0,highlight=None):
 body=tx(380,y-30,label,18);w=650/max(len(values),1)
 for i,v in enumerate(values):
  x=55+i*w
  box='slot-'+label.replace(' ','-')+'-'+str(i)
  body+=f'<rect data-box="{e(box)}" x="{x}" y="{y}" width="{w-4}" height="52" fill="{"#ffe0a7" if i==highlight else "#e9f3f5"}" stroke="#6e97a7"/>'+tx(x+(w-4)/2,y+83,i,13,'math-label')
  if v is not None:
   key=str(v).split(':')[0];labelv=str(v).split(':')[-1]
   body+=f'<g data-entity="{e(key)}">'+tx(x+(w-4)/2,y+26,labelv,17,'math-label',box)+'</g>'
 return body
def linked(nodes,links,cursors=None,back=False,sentinel=None,dy=0):
 n=len(nodes);xs={k:65+i*min(105,630/max(n-1,1)) for i,k in enumerate(nodes)};body='';top=175+dy;bottom=top+50
 def connect(a,b,backward=False):
  x,u=xs[a],xs[b];kind='backward' if backward else 'forward'
  if a==b:
   y=top+37 if backward else top+13;lane=bottom+30 if backward else top-30;end=(x+16,bottom if backward else top)
   points=[(x+36,y),(x+60,y),(x+60,lane),(x+16,lane),end]
  elif abs(nodes.index(a)-nodes.index(b))==1:
   sign=1 if u>x else -1;y=top+37 if backward else top+13
   points=[(x+sign*36,y),(u-sign*36,y)]
  else:
   lane=bottom+30 if backward else top-30;y=bottom if backward else top
   points=[(x+16,y),(x+16,lane),(u-16,lane),(u-16,y)]
  return edge(points,'node-'+a,'node-'+b,kind)
 for a,b in links.items():
  if b is not None and b in xs:
   body+=connect(a,b)
   if back:body+=connect(b,a,True)
  elif b is None:
   x=xs[a];key='null-'+a;ny=top+76
   body+=edge([(x,bottom),(x,ny)],'node-'+a,key)
   body+=f'<rect data-box="{key}" x="{x-47}" y="{ny}" width="94" height="30" rx="6" fill="#fff" stroke="#c4d3db"/>'+tx(x,ny+15,'next = null',12,'pointer-label',key)
 for k in nodes:
  x=xs[k];key='node-'+k;body+=f'<g data-entity="{key}"><rect data-box="{key}" x="{x-36}" y="{top}" width="72" height="50" rx="8" fill="{"#ffe0a7" if k==sentinel else "#d2e8e3"}" stroke="#528276"/>'+tx(x,top+25,k,17,'math-label',key)+'</g>'
 for j,(name,k) in enumerate((cursors or {}).items()):
  cx=180 if j==0 else 580;cy=57+dy;key='cursor-'+name
  body+=f'<rect data-box="{e(key)}" x="{cx-76}" y="{cy}" width="152" height="38" rx="7" fill="#fff" stroke="#bcb6ce"/>'+tx(cx,cy+19,name+(' = null' if k is None else ''),14,'pointer-label',key)
  if k is not None:
   x=xs[k]+(-10 if j==0 else 10);lane=115+dy+20*j
   body+=f'<g data-entity="{e(key)}">'+edge([(cx,cy+38),(cx,lane),(x,lane),(x,top)],key,'node-'+k,'pointer')+'</g>'
 return body
def add(group,id,title,invariant,frames,kind):
 z=dict(id=id,title=title,invariant=invariant,assumptions='Exclusive access; word-sized slots and pointers; finite illustrative state. Exact counting convention appears in each caption.',kind=kind,frames=[])
 import re
 for body,caption,formula,state in frames:
  formula=re.sub(r'\\mathrm\{([^}]*)\}',lambda m:r'\text{'+m[1].replace('\\ ',' ')+'}' if '\\ ' in m[1] else m[0],formula)
  z['frames'].append(dict(svg=svg(body,480 if id=='merge' else 410),caption=caption,formulaHtml=render(formula,True),state=state))
 models.append(z);groups.setdefault(group,[]).append(id)
# Direct-address geometry versus a chain walk.
f=[]
for i in range(5):
 f.append((array(['A','B','C','D','E'],65,'Rank four: direct arithmetic stays one operation',highlight=4)+linked(['A','B','C','D','E'],dict(A='B',B='C',C='D',D='E',E=None),{'cursor':'ABCDE'[i]},dy=115),f'List cursor has followed {i} links; array rank four is reached by base plus four slot strides.',f'B+4b;\quad \mathrm{{links}}={i}',dict(rank=4,links=i)))
add('access','address','Direct rank access versus successor traversal','The list cursor is at the node reached by the stated number of links; array indices do not traverse nodes.',f,'address and chain')
# Array shift traces preserve source-identity labels.
old=['A:2','B:4','C:6','D:8','E:10',None];v=old[:];f=[(array(v),'Original live length five; insertion rank two, one spare slot.','n=5,\ i=2',dict(values=v[:],writes=0))]
for t,j in enumerate(range(5,2,-1),1):
 v[j]=v[j-1];f.append((array(v,highlight=j),f'Copy old slot {j-1} to {j}; backward order leaves all unread sources intact.',f'\mathrm{{shifts}}={t}',dict(values=v[:],writes=t)))
v[2]='X:9';f.append((array(v,highlight=2),'Write the new value. All original identities remain in their original relative order.','\mathrm{shifts}=3,\quad \mathrm{writes}=4',dict(values=v[:],writes=4)))
add('shifts','insert','Stable insertion: backward source copies','The completed right suffix contains the displaced old suffix; unprocessed sources remain available.',f,'array shift')
v=old[:];f=[]
for j in range(2,5):
 v[j+1]=v[j];f.append((array(v,highlight=j+1),f'Counterexample: forward copy from {j} reads a value already overwritten on later steps.','\mathrm{wrong\ direction}',dict(values=v[:])))
add('shifts','bad-insert','Counterexample: an increasing insertion loop','This deliberately incorrect trace exposes lost source values; it is not a valid stable insertion.',f,'counterexample array overwrite')
v=['A:2','X:9','B:4','C:6','D:8','E:10'];f=[]
for t,j in enumerate(range(1,5),1):
 v[j]=v[j+1];f.append((array(v,highlight=j),f'Delete rank one: copy source {j+1} left to {j}.',f'\mathrm{{shifts}}={t}',dict(values=v[:],live=6)))
v[-1]=None;f.append((array(v),'Logical length is five. Clearing the old last slot is shown separately from four shifts.','n=5,\quad \mathrm{shifts}=4',dict(values=v[:],live=5)))
add('shifts','delete','Stable deletion: forward copies','The completed left prefix is the original sequence with the victim omitted.',f,'array deletion')
# Growth: two actual buffers, then one.
f=[];src=['A:2','B:4','C:6','D:8'];dst=[None]*8
for k in range(5):
 if k:dst[k-1]=src[k-1]
 f.append((array(src,90,'Old buffer: capacity four')+array(dst,245,'New buffer: capacity eight'),f'{k} of four live slots copied; both buffers coexist.',f'\mathrm{{copied}}={k},\quad \mathrm{{peak\ slots}}=12',dict(old=src[:],new=dst[:],copies=k)))
dst[4]='X:9';f.append((array(dst,170,'New backing buffer replaces old storage'),'Publish the new backing buffer and append 9; saved old-buffer addresses no longer remain valid.','n=5,\ C=8',dict(new=dst[:],copies=4)))
add('growth','resize','Geometric growth moves actual slots into a new buffer','Each copied old slot has an equal value in the new buffer before the old storage is released.',f,'two-buffer relocation')
f=[]
for m in [1,2,3,4,5,8,9,12,16]:
 C=1;gcopy=0
 while C<m:gcopy+=C;C*=2
 acopy=m*(m-1)//2
 body=tx(380,40,'Cumulative copying: additive +1 versus doubling',19)
 for y,c,lab,col in [(130,gcopy,'doubling','#6b9d8e'),(240,acopy,'additive +1','#b88b64')]:body+=tx(115,y,lab,16)+f'<rect x="215" y="{y-27}" width="{c*3}" height="37" fill="{col}"/>'+tx(680,y,c,17,'math-label')
 f.append((body,f'After {m} appends, doubling has copied {gcopy} slots; additive growth by one has copied {acopy}.',f'm={m};\quad G={gcopy};\quad A={acopy}',dict(m=m,geometric=gcopy,additive=acopy)))
add('growth','growth-contrast','Geometric sums versus arithmetic sums','Bars display actual cumulative old-slot copies; new-value writes are excluded from both.',f,'cumulative-cost plot')
# Threshold traces with occupancy actual slots.
for policy in ['quarter','half']:
 C=8;n=8;f=[]
 ops=['append','delete','append','delete'] if policy=='half' else ['delete']*6+['append']*4
 for t,op in enumerate(['start']+ops):
  copied=0
  if op=='append':
   if n==C:copied=n;C*=2
   n+=1
  elif op=='delete':
   n-=1
   if C>2 and n==C//(4 if policy=='quarter' else 2):copied=n;C//=2
  phi=2*n-C if n>=C/2 else C/2-n
  f.append((array([f'v{i}:{i}' if i<n else None for i in range(C)],140,f'{policy}-full shrink: {op}'),f'Length {n}, capacity {C}; this update copied {copied} slots. '+('Counterexample: opposite resizes can occur on consecutive updates.' if policy=='half' else 'The gap between thresholds separates opposite resizes.'),f'n={n},\ C={C},\ \mathrm{{copies}}={copied}',dict(n=n,C=C,operation=op,copies=copied,potential=phi)))
 add('shrink',policy+'-shrink',('Hysteresis: quarter-full contraction' if policy=='quarter' else 'Counterexample: half-full thrashing'),'Live occupied slots are exactly n; capacity transitions follow the explicitly named policy.',f,'occupancy threshold')
# SLL updates.
links=dict(A='B',B='C',C=None,X=None);f=[]
for label,update in [('Original chain; X is allocated but detached.',{}),('Initialize X.next to the old successor B.',{'X':'B'}),('Publish X through A.next.',{'A':'X'}),('Remove B by bypassing it from predecessor X.',{'X':'C'}),('Detached B can now be released; chain remains A→X→C.',{'B':None})]:
 links.update(update);f.append((linked(['A','X','B','C'],links,{'predecessor':'A'}),label,'\mathrm{known\ predecessor}',dict(links=links.copy())))
add('singly','sll-insert-delete','Insertion and removal through a known predecessor','The old successor is saved before publishing X; only detached nodes may be released.',f,'singly linked heap')
f=[]
for tail in ['E','D','C','B']:
 nodes=list('ABCDE'[:'ABCDE'.index(tail)+1]);links={a:(nodes[j+1] if j+1<len(nodes) else None) for j,a in enumerate(nodes)}
 for j,p in enumerate(nodes[:-1]):f.append((linked(nodes,links,{'tail':tail,'search':p}),f'Find predecessor of current tail {tail}; search has followed {j} links. Tail does not expose a predecessor field.',f'\mathrm{{searched}}={j}',dict(nodes=nodes,tail=tail,search=p)))
add('singly','tail-search','Repeated singly linked tail removal exposes new searches','Only forward links are stored; the predecessor must be reached from the current head.',f,'predecessor-search paths')
# DLL genuine bidirectional topology; insertion complete checkpoints.
f=[]
for nodes,links,cap in [(['S','A','B','C'],dict(S='A',A='B',B='C',C='S'),'Circular doubly linked sentinel with three data nodes.'),(['S','A','X','B','C'],dict(S='A',A='X',X='B',B='C',C='S'),'X inserted between A and B: four pointer fields establish two adjacencies.'),(['S','A','X','C'],dict(S='A',A='X',X='C',C='S'),'Known B unlinked: reconnect X and C in both directions.'),(['S'],dict(S='S'),'All real nodes removed: sentinel next and prev both point to itself.')]:
 f.append((linked(nodes,links,back=True,sentinel='S'),cap,'x.\mathrm{next}.\mathrm{prev}=x',dict(nodes=nodes,links=links)))
add('doubly','dll','Circular doubly linked adjacency and empty sentinel','Blue forward and amber backward arrows describe inverse adjacency; S is not a data node.',f,'bidirectional circular topology')
f=[]
for k in range(3):
 left= ['S','A','B','C','D'] if k<2 else ['S','A','D'];right=['T','X','Y'] if k<2 else ['T','X','B','C','Y']
 lp={a:left[(i+1)%len(left)] for i,a in enumerate(left)};rp={a:right[(i+1)%len(right)] for i,a in enumerate(right)}
 body=linked(left,lp,back=True,sentinel='S')+linked(right,rp,back=True,sentinel='T',dy=140)
 f.append((body,['Identify the source range B through C and destination gap X,Y.','Save all six boundary neighbors before the mutation; internal B,C links remain.','Close A,D and connect X,B and C,Y; the range has moved.'][k],f'\mathrm{{boundary\ writes}}={0 if k<2 else 6}',dict(source=left,destination=right)))
add('doubly','splice','Range splice: unchanged interior, changed boundaries','Source and destination are disjoint lists; the range length is supplied as two.',f,'two-list range splice')
# Reversal edges flip while node identities remain fixed in memory.
nodes=list('ABCD');links={a:(nodes[i+1] if i+1<len(nodes) else None) for i,a in enumerate(nodes)};prev=None;cur='A';f=[]
for k in range(5):
 f.append((linked(nodes,links,{'prev':prev,'cur':cur}),f'{k} nodes reversed; the untouched suffix remains reachable through cur.','\mathrm{next\ writes}='+str(k),dict(links=links.copy(),prev=prev,cur=cur,writes=k)))
 if cur is not None:nxt=links[cur];links[cur]=prev;prev=cur;cur=nxt
add('reverse','reverse','Iterative reversal flips links without reallocating nodes','Reversed prefix and untouched suffix are disjoint and cover the original node set.',f,'reversal heap and cursors')
# Cycle diagrams: nodes positioned along actual path and a visible return arc.
mu=3;lam=4;nodes=[str(i) for i in range(mu+lam)];links={a:str(i+1) if i+1<len(nodes) else str(mu) for i,a in enumerate(nodes)}
def advance(i,step=1):
 for _ in range(step):i=int(links[str(i)])
 return i
slow=fast=0;f=[]
for t in range(5):
 f.append((linked(nodes,links,{'slow':str(slow),'fast':str(fast)}),f'After {t} full iterations: slow={slow}, fast={fast}. '+('Positive collision found.' if t==4 else 'Initial equality at iteration zero is ignored.' if t==0 else 'Advance one and two links before comparing.'),f't={t},\quad \mu=3,\ \lambda=4',dict(t=t,slow=slow,fast=fast,mu=mu,lam=lam)))
 slow=advance(slow);fast=advance(fast,2)
add('cycle','floyd','Floyd detection: one-link and two-link paths','Cursor positions follow actual successors; equality is tested after complete iterations.',f,'cycle graph with two cursors')
head=0;meet=4;f=[]
for t in range(4):
 f.append((linked(nodes,links,{'from head':str(head),'from meeting':str(meet)}),f'Reset phase after {t} one-link steps; '+('both cursors identify cycle entry.' if t==3 else 'advance at equal speed.'),f'\mathrm{{reset\ steps}}={t}',dict(t=t,head=head,meet=meet)))
 head=advance(head);meet=advance(meet)
add('cycle','entry','Reset phase locates the cycle entry','The meeting time was divisible by cycle length; this reset proof uses fast speed two.',f,'entry alignment')
# Traversal contrast uses accumulators and moving pointer, not decorative generic simulation.
f=[];cost=0
for i in range(6):
 cost+=i;body=linked(list('ABCDEF'),dict(A='B',B='C',C='D',D='E',E='F',F=None),{'requested rank':list('ABCDEF')[i]})+tx(380,325,f'Independent get calls: {cost} links; retained cursor: {i} links',18)
 f.append((body,f'Visited ranks zero through {i}. Restarting at head pays a triangular sum.',f'\sum_{{j=0}}^{i}j={cost}',dict(rank=i,restartCost=cost,cursorCost=i)))
add('traversal','scan-cost','Two traversal strategies on the same list','Both visit identical logical positions; the restart strategy repeats physical paths.',f,'traversal cost accumulation')
# Merge uses three actual sequence buffers for readability; IDs move to output.
L=['L1:2','L2:4','L3:7'];Q=['R1:1','R2:4','R3:8'];out=[];f=[];comp=0
while L or Q:
 f.append((array(L+[None]*(3-len(L)),75,'Remaining left chain values')+array(Q+[None]*(3-len(Q)),225,'Remaining right chain values')+array(out+[None]*(6-len(out)),375,'Merged node order'),f'Output contains {len(out)} selected nodes; {comp} head comparisons. Equal keys choose left.',f'\mathrm{{comparisons}}={comp}',dict(left=L[:],right=Q[:],output=out[:],comparisons=comp)))
 if L and Q:comp+=1
 if not Q or (L and int(L[0].split(':')[1])<=int(Q[0].split(':')[1])):out.append(L.pop(0))
 else:out.append(Q.pop(0))
f.append((array(out,170,'Final stable merged order'),'All six nodes selected; five comparisons, then an unexamined suffix attachment.','\mathrm{comparisons}=5',dict(output=out[:],comparisons=comp)))
add('mergecompact','merge','Stable merge moves identities into output order','Left-on-equality preserves the original left-then-right order of equal keys; input nodes are disjoint.',f,'two-input merge')
v=['A:-2','B:5','C:0','D:-1','E:8','F:-3','G:4'];w=0;f=[]
for r in range(len(v)):
 source=v[r]
 if int(source.split(':')[1])>=0:v[w]=source;w+=1
 f.append((array(v,140,highlight=r)+tx(380,280,f'read={r}; retained prefix length={w}',18),f'After testing old rank {r}, keep exactly the nonnegative values in the first {w} slots.',f'w={w}\le r+1={r+1}',dict(values=v[:],read=r,write=w)))
add('mergecompact','compact','Stable compaction: read and write cursors','All future unread positions retain their original values because write never leads read.',f,'compaction overwrite geometry')
nodes=list('ABCDE');f=[]
for links,cap in [(dict(A='B',B='C',C='D',D='E',E=None),'Save C as new head and B as new tail.'),(dict(A='B',B='C',C='D',D='E',E='A'),'Temporarily connect old tail E to old head A.'),(dict(A='B',B=None,C='D',D='E',E='A'),'Cut B.next. The acyclic result begins C and ends B.')]:
 f.append((linked(nodes,links,{'new head':'C','new tail':'B'}),cap,'k=2,\quad n=5',dict(links=links)))
add('rotation','rotate','Left rotation joins one boundary and cuts another','The saved new head remains available throughout the temporary cycle.',f,'rotation topology')
# Orthogonal sparse nodes are physical coordinate intersections, with separate colored chains.
f=[];entries=[(0,1,10),(0,2,14),(2,1,15),(2,2,21)]
for k in range(5):
 body=tx(380,30,'Right links organize rows; down links organize columns',19)
 for i in range(3):body+=tx(85,110+i*80,'row '+str(i),15)
 for j in range(4):body+=tx(210+j*120,64,'col '+str(j),15)
 for i,j,v in entries[:k]:
  x=210+j*120;y=110+i*80;key=f'entry-{i}-{j}';body+=f'<g data-entity="e{i}{j}"><rect data-box="{key}" x="{x-26}" y="{y-22}" width="52" height="42" rx="5" fill="#d2e8e3" stroke="#528276"/>'+tx(x,y-1,v,18,'math-label',key)+'</g>'
 for i in [0,2]:
  row=[(j,v) for a,j,v in entries[:k] if a==i]
  if len(row)==2:body+=path(210+row[0][0]*120+26,110+i*80,210+row[1][0]*120-26,110+i*80,source=f'entry-{i}-{row[0][0]}',target=f'entry-{i}-{row[1][0]}')
 for j in [1,2]:
  col=[(i,v) for i,b,v in entries[:k] if b==j]
  if len(col)==2:body+=path(210+j*120,110+col[0][0]*80+20,210+j*120,110+col[1][0]*80-22,'#b57952',source=f'entry-{col[0][0]}-{j}',target=f'entry-{col[1][0]}-{j}')
 f.append((body,f'{k} nonzero entries placed. Each added node belongs to a row chain and a column chain.','\operatorname{nnz}(C)=2\cdot2=4',dict(entries=entries[:k])))
add('sparse','orthogonal','Sparse outer product and two independent adjacency directions','Coordinates come from nonzero factor pairs; rows and columns have independent successor relations.',f,'orthogonal matrix schematic')
out=dict(chapter='a_arrays',models=models,groups=groups,scope='Finite exact illustrations accompany general proofs; no finite trace substitutes for a theorem.')
(R/'dist/chapters/a_arrays-models.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(len(models),'models;',sum(len(m['frames']) for m in models),'checkpoints')
