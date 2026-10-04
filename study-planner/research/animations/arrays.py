"""Exact array transformations: stable object slots and moving value tokens."""
from common import node,frame,scene
from copy import deepcopy

def slots(a,y=85,prefix='a'):
 return [node(prefix+str(i),str(v),75+110*i,y,w=90,h=48,size=22) for i,v in enumerate(a)]
def checkpoint(a,i,caption,formula='',**snap):
 x=75+110*max(0,min(i,len(a)-1))
 ns=slots(a)+[node('cursor',f'i = {i}',x,190,w=115,h=50,tone='active',size=22)]
 return frame(ns,caption,{'processed':i},formula,snapshot=dict(values=deepcopy(a),index=i,**snap))
def add(id,title,description,invariant,frames):
 return scene('arr-'+id,title,description,invariant,frames)

a=[2,4,6,8,10,12]
fs=[]
for i in [0,2,5,6]:
 ns=slots(a)+[node('pointer','one-past' if i==6 else f'p → a[{i}]',75+110*i if i<6 else 695,190,w=120,h=50,tone='active',size=20)]
 fs.append(frame(ns,'The pointer selects '+('the exclusive end after six elements. It can be formed but there is no element here to read.' if i==6 else f'live element {i}, whose value is {a[i]}. Its index is within the stated six-element object.'),{'element index':i},snapshot=dict(index=i,values=a)))
add('boundary','Element positions and the exclusive end','Advance a pointer within one six-element object, then stop at its legal one-past boundary.','Elements are 0 through 5; endpoint 6 is a position, not an element.',fs)

for order in ['row','column']:
 coords=[(i,j) for i in range(3) for j in range(4)] if order=='row' else [(i,j) for j in range(4) for i in range(3)]
 fs=[]
 for t,(i,j) in enumerate(coords):
  ns=[node(f'cell{r}{c}',f'{r},{c}: {4*r+c}',115+165*c,65+75*r,w=135,h=48,size=20,tone='active' if (r,c)==(i,j) else 'plain') for r in range(3) for c in range(4)]
  ns.append(node('pointer',f'offset {4*i+j}',115+165*j,300,w=130,h=46,size=21,tone='active'))
  fs.append(frame(ns,f'Traversal step {t+1} selects coordinate ({i},{j}). In this row-major backing array, its physical element offset is {4*i+j}; the loop order does not change that representation.',{'visited':t+1},r'o=4i+j',snapshot=dict(order=order,step=t,coord=[i,j],offset=4*i+j)))
 add(order,'Traverse '+order+' first in a row-major matrix','Compare two loop orders over the same 3-by-4 storage. Read the physical offsets as the selection moves.','The matrix representation remains row-major in both traces; only visit order changes.',fs)

a=[3,-2,5,1,-4];p=[0];fs=[]
for i in range(6):
 ns=slots(a,y=65)+slots(p+['—']*(6-len(p)),y=165,prefix='p')
 ns.append(node('transfer',f'P[{i}] = {p[-1]}',75+110*i,275,w=125,h=50,size=21,tone='active'))
 fs.append(frame(ns,f'After processing {i} original values, the verified prefix is {p}. The unfilled positions are marked with a dash rather than a fabricated numeric value.',{'processed':i},r'P[i]=\sum_{k=0}^{i-1}A[k]',snapshot=dict(index=i,input=a,prefix=p[:])))
 if i<5:p.append(p[-1]+a[i])
add('prefix','Build the boundary prefix array','Five values produce six prefix boundaries; the transfer token advances one filled boundary at a time.','P[0] is zero and every completed P[i] sums the first i original values.',fs)

for name,s,d,order in [('bad',0,1,'forward'),('right',0,1,'reverse'),('left',1,0,'forward')]:
 a=[2,4,6,8,10,12];original=a[:];fs=[checkpoint(a,0,'Begin with the original six-element sequence. No destination write has occurred, so every source value still has its original value.',source=s,destination=d,step=-1)]
 for t in (range(4) if order=='forward' else range(3,-1,-1)):
  value=a[s+t];a[d+t]=value
  f=checkpoint(a,d+t,f'Read current source index {s+t} with value {value}, then write destination index {d+t}. '+('Forward rightward overlap can reread an overwritten value, so this trace is a deliberate counterexample.' if name=='bad' else 'The chosen direction keeps every still unread source value original.'),source=s,destination=d,step=t,value=value)
  f['nodes'].append(node('source-token',str(value),75+110*(s+t),275,w=80,h=44,size=22,tone='done'))
  fs.append(f)
 add('copy-'+name,{'bad':'Counterexample: rightward forward copy','right':'Correct rightward reverse move','left':'Correct leftward forward move'}[name],'Follow four writes in one shared array. Source and target refer to overlapping regions.','The desired target is the original source segment; final-source equality alone is insufficient.',fs)

a=[3,6,9,12,'—','—'];fs=[checkpoint(a,4,'The logical length is four and allocated capacity is six. Two spare slots exist but are not part of the original sequence.',length=4)]
for src in [3,2]:
 a[src+1]=a[src]
 fs.append(checkpoint(a,src+1,f'Move original index {src} to position {src+1}. Descending shifts keep the earlier unread values intact before the insertion.',length=4))
a[2]=7;fs.append(checkpoint(a,2,'Write the inserted value seven at index two, then increase the logical length to five. The remaining spare slot is still outside the sequence.',length=5))
add('insert','Insert with descending shifts','Insert seven at logical index two of a four-value sequence with spare capacity.','The moved suffix retains original order and every write remains within allocated capacity.',fs)

a=[0,1,2,3,4,5];fs=[checkpoint(a,0,'Start a complete reversal of six entries. Neither end has been placed in its final reversed position yet.',done=0)]
for t in range(3):
 a[t],a[5-t]=a[5-t],a[t]
 fs.append(checkpoint(a,t,f'Swap pair ({t},{5-t}). The first and last {t+1} entries now match the reversed original; the remaining middle stays untouched.',done=t+1))
add('reverse','Pair swaps fix both ends','Reverse a six-value sequence by three disjoint endpoint swaps.','After t swaps, t positions at each end have their final values.',fs)

a=[0,1,2,3,4,5];fs=[checkpoint(a,0,'Split the original sequence into the first two entries and the final four entries before any reversal.',stage=0)]
for stage,(l,r) in enumerate([(0,2),(2,6),(0,6)],1):
 a[l:r]=a[l:r][::-1]
 fs.append(checkpoint(a,l,f'Reverse segment [{l}:{r}) at stage {stage}. '+('The complete result is now the original suffix followed by the original prefix.' if stage==3 else 'This is an intermediate state, not yet the rotated result.'),stage=stage))
add('rotate','Three reversals rotate left','Rotate six entries left by two with exact intermediate block states.','Reverse(X), reverse(Y), then reverse the whole concatenation produces YX.',fs)

fs=[]
for stage,(aa,bb,inner) in enumerate([('A → outer 1','B not created','row 0: [2]'),('A → outer 1','B → outer 2','shared row 0: [2]'),('A → outer 1','B → outer 2','shared row 0: [2,7]')]):
 ns=[node('a',aa,180,60,w=260,h=55,size=22),node('b',bb,580,60,w=270,h=55,size=22),node('inner',inner,380,185,w=340,h=55,size=22),node('token','reference' if stage<2 else 'append 7',180 if stage==0 else 580 if stage==1 else 380,290,w=180,h=50,tone='active',size=22)]
 fs.append(frame(ns,['Begin with one outer list containing an inner row. The second outer list and its copied slot reference do not exist yet.','A slice creates a second outer list but copies the inner row reference. Both first slots now designate the same inner object.','Append seven through the second outer list’s row reference. The first outer list sees the same changed inner row because its identity is shared.'][stage],snapshot=dict(stage=stage,row=[2] if stage<2 else [2,7])))
add('sharing','An outer copy retains inner identities','Move a reference token to a new outer list, then mutate the shared row.','Outer identity differs; the selected inner identity remains shared.',fs)

fs=[];old=[2,4,6];new=['—']*6
for t in range(5):
 if 1<=t<=3:new[t-1]=old[t-1]
 ns=slots(old,y=65)+slots(new,y=165,prefix='new')
 ns.append(node('token','allocate' if t==0 else 'release old' if t==4 else f'copy {old[t-1]}',75+110*max(0,t-1),285,w=140,h=48,tone='active',size=21))
 if t==4:
  for n in ns:
   if n['id'].startswith('a'):n['label']='released';n['tone']='muted'
 fs.append(frame(ns,f'Expansion checkpoint {t}: '+('a distinct six-slot block is reserved while the three-slot original remains live.' if t==0 else 'release the old storage only after all three live values have been copied; the owner must use the new block.' if t==4 else f'copy original element {t-1} into the matching new position; no old value is overwritten.'),{'copied':min(t,3),'peak slots':9},snapshot=dict(step=t,new=new[:],oldLive=t<4)))
add('growth','Expansion uses two backing objects','Copy three live values into a new six-slot block before releasing the old storage.','Length stays three while capacity grows; peak backing storage is nine slots.',fs)

fs=[]
for i,j in [(0,0),(1,0),(1,1),(2,0),(2,1),(2,2)]:
 ns=[]
 for r in range(3):
  for c in range(r+1):
   ns.append(node(f'cell{r}{c}',f'{r},{c}',170+165*c,65+75*r,w=120,h=48,size=22,tone='active' if (r,c)==(i,j) else 'plain'))
 off=i*(i+1)//2+j;ns.append(node('token',f'offset {off}',75+110*off,300,w=120,h=46,size=21,tone='active'))
 fs.append(frame(ns,f'Select lower-triangle position ({i},{j}). Its {i} earlier rows occupy {i*(i+1)//2} entries, so adding column {j} gives packed offset {off}.',formula=r'o=i(i+1)/2+j',snapshot=dict(i=i,j=j,offset=off)))
add('packed','Lower-triangle packing by rows','Trace all six positions of a three-row packed lower triangle including its diagonal.','Only j≤i is stored; row starts are triangular counts.',fs)

fs=[]
for t in range(4):
 physical=(5+t)%7
 ns=[node('slot'+str(i),str(i),65+100*i,90,w=80,h=48,size=22,tone='active' if i==physical else 'plain') for i in range(7)]
 ns.append(node('cursor',f'logical {t}',65+100*physical,235,w=120,h=50,tone='active',size=21))
 fs.append(frame(ns,f'Logical offset {t} from head five maps to physical slot {physical} modulo seven. The wrap does not change the logical encounter order.',formula=r'p=(5+t)\bmod7',snapshot=dict(t=t,physical=physical)))
add('ring','Logical order wraps around storage','Visit a length-four circular sequence with head five and capacity seven.','Capacity is positive and logical offsets remain below the current length.',fs)

fs=[];target=['—']*6
for o in range(6):
 i,j=divmod(o,3);dest=j*2+i
 for phase in ['read','write']:
  if phase=='write':target[dest]=o
  ns=slots([0,1,2,3,4,5],65)+slots(target,165,prefix='b')
  ns.append(node('value',str(o),75+110*(o if phase=='read' else dest),265 if phase=='read' else 320,w=85,h=40,size=22,tone='active'))
  fs.append(frame(ns,f'{phase.capitalize()} original value {o}: source coordinate ({i},{j}) maps to transpose coordinate ({j},{i}), whose destination offset is {dest}. '+('The destination slot remains unfilled until the write checkpoint.' if phase=='read' else 'This destination is now filled while all original source values remain unchanged.'),formula=r'iC+j\mapsto jR+i',snapshot=dict(source=o,i=i,j=j,destination=dest,phase=phase,target=target[:])))
add('transpose','Rectangular transpose changes strides','The source and destination rows are distinct objects with widths three and two. Each checkpoint explains one source-to-destination correspondence.','The complete mapping is a bijection of six positions; source values are unchanged.',fs)

a=[3,5,9,10];fs=[checkpoint(a,3,'Begin an original-neighbor difference transform. The first entry will remain unchanged while the later entries are processed from right to left.',step=-1)]
for i in [3,2,1]:
 a[i]-=a[i-1]
 fs.append(checkpoint(a,i,f'Write difference at index {i} using its still original lower predecessor. The descending order prevents an earlier difference from being reused as source data.',step=i))
add('difference','Descending differences preserve neighbors','Compute adjacent original differences without a second array.','Each lower predecessor remains original when the current entry is updated.',fs)

a=[5,2,7,4,6,9];w=0;fs=[checkpoint(a,0,'Begin stable compaction retaining only even original entries. Both the read boundary and the logical output length begin at zero.',read=0,write=0)]
for r,v in enumerate([5,2,7,4,6,9]):
 if v%2==0:a[w]=v;w+=1
 fs.append(checkpoint(a,r,f'Read original index {r} with value {v}; '+(f'append it to the retained prefix, whose length becomes {w}.' if v%2==0 else f'discard it while retained length stays {w}.')+' The write boundary never exceeds the read boundary.',read=r+1,write=w))
add('compact','Stable compaction does not damage unread values','Retain even values with a moving read cursor and a nondecreasing write boundary.','A[0:w) contains precisely the retained original values from the processed prefix.',fs)

fs=[];text='aaaaab';pattern='aaab';comparisons=0
for start in range(len(text)-len(pattern)+1):
 for j in range(len(pattern)):
  comparisons+=1;equal=text[start+j]==pattern[j]
  ns=slots(list(text),65)+[node('p'+str(k),v,75+110*(start+k),165,w=90,h=48,size=22,tone='active' if k==j else 'plain') for k,v in enumerate(pattern)]
  ns.append(node('compare','equal' if equal else 'mismatch',75+110*(start+j),280,w=115,h=46,size=21,tone='done' if equal else 'warning'))
  fs.append(frame(ns,f'Candidate start {start}, pattern offset {j}: compare text character {text[start+j]} with pattern character {pattern[j]}. '+('This position agrees; continue until the whole pattern agrees or a later comparison fails.' if equal else 'This mismatch rejects the current candidate and restarts at the next permitted start.'),{'comparisons':comparisons},snapshot=dict(start=start,j=j,equal=equal,comparisons=comparisons)))
  if not equal:break
add('search','Bounded naive matching with exact comparisons','Compare a four-character pattern at every permitted start in six-character text, keeping the final candidate included.','A candidate start is between zero and n−m inclusive; reads remain within the stated lengths.',fs)
