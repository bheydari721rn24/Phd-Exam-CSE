"""Precisely specified sorting variants; semantic checkpoints and original SVG geometry."""
from copy import deepcopy
from html import escape
from math import floor,log2,ceil
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'exam-rewrite'))
import mathml

def records(values):return [dict(key=x,id=chr(97+i)) for i,x in enumerate(values)]
def trace(kind,params,capture=True):
 A=records(params.get('values',[]));initial=deepcopy(A);n=len(A);frames=[];C=W=S=0;extra={}
 def frame(caption,rows=None,active=None,**kw):
  if capture:frames.append(dict(layout=kw.pop('layout','array'),rows=deepcopy(rows or [dict(name='Array',cells=A)]),active=list(active or []),metrics=dict(comparisons=C,writes=W,swaps=S),caption=caption,**kw))
 def swap(i,j):
  nonlocal W,S
  if i!=j:A[i],A[j]=A[j],A[i];W+=2;S+=1
 frame('Initial records. Letters identify original occurrences; comparisons use keys only.')
 if kind=='selection':
  for i in range(n-1):
   m=i
   for j in range(i+1,n):
    C+=1
    if A[j]['key']<A[m]['key']:m=j
    frame(f'Scan index {j}; the minimum of the inspected suffix is at {m}.',active=[m,j],prefix=i,pointers=dict(i=i,min=m,j=j))
   swap(i,m);frame(f'Place the suffix minimum at {i}; the final prefix grows.',active=[i,m],prefix=i+1)
 elif kind in ['insertion','shell']:
  gaps=[1] if kind=='insertion' else params.get('gaps',[4,2,1])
  shifts=0
  for gap in gaps:
   if gap<1 or gap>max(n,1):continue
   for i in range(gap,n):
    x=A[i];A[i]=None;j=i
    def rs():return [dict(name='Array',cells=A),dict(name='Held key',cells=[x])]
    frame(f'Gap {gap}: hold original record {x["id"]}; slot {j} is the hole.',rs(),[j],gap=gap,prefix=i if gap==1 else 0)
    while j>=gap:
     C+=1;frame(f'Compare predecessor at {j-gap} with held key {x["key"]}.',rs(),[j-gap],gap=gap)
     if A[j-gap]['key']<=x['key']:break
     A[j]=A[j-gap];A[j-gap]=None;j-=gap;W+=1;shifts+=1
     frame(f'Shift the larger record right by gap {gap}; the hole moves to {j}.',rs(),[j],gap=gap)
    A[j]=x;W+=1;frame(f'Insert held record at {j}. Equal existing records stay before it.',active=[j],gap=gap,prefix=i+1 if gap==1 else 0)
  extra.update(shifts=shifts,gaps=gaps)
 elif kind=='bubble':
  passes=0
  for end in range(n-1,0,-1):
   moved=False;passes+=1
   for j in range(end):
    C+=1;frame(f'Pass {passes}: compare adjacent keys at {j} and {j+1}.',active=[j,j+1],suffix=end+1)
    if A[j]['key']>A[j+1]['key']:swap(j,j+1);moved=True;frame('Swap this inverted adjacent pair; exactly one strict inversion disappears.',active=[j,j+1],suffix=end+1)
   frame(f'Largest remaining key is final at {end}.',suffix=end)
   if not moved:frame('No swap in the complete pass: the remaining prefix is already sorted.');break
  extra['passes']=passes
 elif kind=='merge':
  merges=[];skip=params.get('skip',False)
  def rec(lo,hi):
   nonlocal C,W
   if hi-lo<=1:return
   mid=params.get('split',(lo+hi)//2) if params.get('mergeOnly') else (lo+hi)//2
   if not params.get('mergeOnly'):rec(lo,mid);rec(mid,hi)
   if skip:
    C+=1
    if A[mid-1]['key']<=A[mid]['key']:frame(f'Boundary test succeeds for [{lo},{hi}); skip the merge.');return
   L=deepcopy(A[lo:mid]);R=deepcopy(A[mid:hi]);out=[];i=j=0;c0=C
   def rs():return [dict(name='Left run',cells=L,role='left'),dict(name='Right run',cells=R,role='right'),dict(name='Output',cells=out+[None]*(hi-lo-len(out)),role='output')]
   frame(f'Merge [{lo},{mid}) and [{mid},{hi}); consumed heads are shown by pointers.',rs(),layout='merge',pointers=dict(left=i,right=j))
   while i<len(L) and j<len(R):
    C+=1
    if L[i]['key']<=R[j]['key']:out.append(L[i]);i+=1;side='left'
    else:out.append(R[j]);j+=1;side='right'
    W+=1;frame(f'Emit from {side}; equality chooses left, preserving stability.',rs(),layout='merge',pointers=dict(left=i,right=j),transfer=dict(row=side,index=(i-1 if side=='left' else j-1),dest=len(out)-1))
   while i<len(L):out.append(L[i]);i+=1;W+=1;frame('Copy the remaining left head without a key comparison.',rs(),layout='merge',pointers=dict(left=i,right=j))
   while j<len(R):out.append(R[j]);j+=1;W+=1;frame('Copy the remaining right head without a key comparison.',rs(),layout='merge',pointers=dict(left=i,right=j))
   A[lo:hi]=out;W+=hi-lo;merges.append(dict(lo=lo,mid=mid,hi=hi,comparisons=C-c0))
   frame(f'Copy the merged run back. This merge used {C-c0} comparisons.',active=list(range(lo,hi)),range=[lo,hi])
  rec(0,n);extra['merges']=merges
 elif kind=='hoare':
  splits=[]
  def rec(lo,hi):
   nonlocal C
   if hi-lo<=1:return
   p=A[lo]['key'];i=lo-1;j=hi
   while True:
    i+=1;C+=1
    while A[i]['key']<p:i+=1;C+=1
    j-=1;C+=1
    while A[j]['key']>p:j-=1;C+=1
    frame(f'Hoare scans stop at i={i}, j={j}, pivot value {p}; equality stops either scan.',active=[i,j],range=[lo,hi],boundaries=[i,j+1],pivotValue=p)
    if i>=j:break
    swap(i,j);frame('Exchange the two out-of-side keys. Both scans advance before testing again.',active=[i,j])
   splits.append(dict(lo=lo,hi=hi,split=j+1));frame(f'Return split {j+1}; this is not a final pivot index.',range=[lo,hi],boundaries=[j+1],pivotValue=p)
   if not params.get('partitionOnly'):rec(lo,j+1);rec(j+1,hi)
  rec(0,n);extra['splits']=splits
 elif kind in ['quick','three','cmu']:
  partitions=[];depth=0
  def rec(lo,hi,lev):
   nonlocal C,depth
   depth=max(depth,lev)
   if hi-lo<=1:return
   if kind=='quick':
    pi=hi-1 if params.get('pivot','last')=='last' else lo;swap(pi,hi-1);p=A[hi-1]['key'];b=lo
    frame(f'Lomuto partition [{lo},{hi}); last key {p} is the pivot.',range=[lo,hi],pivot=hi-1,boundaries=[b,lo,hi-1],pivotValue=p)
    for j in range(lo,hi-1):
     C+=1
     if A[j]['key']<p:swap(b,j);b+=1
     frame(f'Classify index {j}; [{lo},{b}) is strictly below {p}.',active=[j],range=[lo,hi],pivot=hi-1,boundaries=[b,j+1,hi-1],pivotValue=p)
    swap(b,hi-1);partitions.append(dict(lo=lo,hi=hi,pivot=b));frame(f'Pivot reaches final position {b}; children exclude it.',pivot=b,range=[lo,hi]);rec(lo,b,lev+1);rec(b+1,hi,lev+1)
   elif kind=='cmu':
    pi=(lo+hi)//2;swap(lo,pi);p=A[lo]['key'];left=lo+1;right=hi
    while left<right:
     C+=1
     if A[left]['key']<=p:left+=1
     else:swap(left,right-1);right-=1
     frame(f'CMU scan: [{lo+1},{left}) <= {p}; [{right},{hi}) > {p}.',pivot=lo,range=[lo,hi],boundaries=[left,right],pivotValue=p)
    swap(lo,left-1);partitions.append(dict(lo=lo,hi=hi,pivot=left-1));frame(f'CMU pivot {p} reaches index {left-1}.',pivot=left-1);rec(lo,left-1,lev+1);rec(left,hi,lev+1)
   else:
    p=A[lo]['key'];lt=lo;i=lo+1;gt=hi
    frame(f'Three-way partition [{lo},{hi}); pivot value {p}; equal region initially contains one record.',range=[lo,hi],boundaries=[lt,i,gt],pivotValue=p)
    while i<gt:
     C+=1;cmp=(A[i]['key']>p)-(A[i]['key']<p)
     if cmp<0:swap(lt,i);lt+=1;i+=1
     elif cmp>0:gt-=1;swap(i,gt)
     else:i+=1
     frame(f'Ternary comparison: less [{lo},{lt}), equal [{lt},{i}), unknown [{i},{gt}), greater [{gt},{hi}).',range=[lo,hi],boundaries=[lt,i,gt],pivotValue=p)
    partitions.append(dict(lo=lo,hi=hi,equal=[lt,gt]));frame('The complete equal block needs no further recursion.',range=[lo,hi],boundaries=[lt,gt,gt],pivotValue=p);rec(lo,lt,lev+1);rec(gt,hi,lev+1)
  rec(0,n,0);extra.update(partitions=partitions,recursionDepth=depth)
 elif kind=='heap':
  size=n;buildC=0
  def sink(i,end):
   nonlocal C
   while 2*i+1<end:
    j=2*i+1
    if j+1<end:C+=1;j=j+1 if A[j+1]['key']>A[j]['key'] else j
    C+=1;frame(f'Choose larger child {j}; compare it with parent {i}.',layout='heap',heapSize=end,active=[i,j])
    if A[i]['key']>=A[j]['key']:break
    swap(i,j);frame('Exchange parent and larger child; only the lower subtree may still violate heap order.',layout='heap',heapSize=end,active=[i,j]);i=j
  for i in range(n//2-1,-1,-1):sink(i,n);frame(f'Floyd construction: subtree rooted at {i} now satisfies heap order.',layout='heap',heapSize=n,active=[i])
  buildC=C
  for end in range(n-1,0,-1):
   swap(0,end);frame(f'Maximum is final at index {end}; the heap shrinks to {end}.',layout='heap',heapSize=end,active=[0,end]);sink(0,end)
  extra['buildComparisons']=buildC
 elif kind=='counting':
  low=params.get('low',min(params.get('values',[0])) if n else 0);K=params.get('K',(max(params['values'])-low+1) if n else 1)
  counts=[0]*K
  for r in A:counts[r['key']-low]+=1;frame('Count an original occurrence; payload and identity remain attached.',[dict(name='Input',cells=A),dict(name='Counts',cells=[dict(key=x,id=str(i+low)) for i,x in enumerate(counts)],numeric=True)],layout='counting')
  for k in range(1,K):counts[k]+=counts[k-1]
  ends=counts[:];out=[None]*n
  frame('Cumulative counts give exclusive ends of each key block.',[dict(name='Input',cells=A),dict(name='Ends',cells=[dict(key=x,id=str(i+low)) for i,x in enumerate(counts)],numeric=True),dict(name='Output',cells=out)],layout='counting')
  for r in reversed(A):
   k=r['key']-low;counts[k]-=1;out[counts[k]]=r;W+=1
   frame(f'Right-to-left scatter: record {r["id"]} goes to index {counts[k]}.',[dict(name='Input',cells=A,role='reference'),dict(name='Ends',cells=[dict(key=x,id=str(i+low)) for i,x in enumerate(counts)],numeric=True),dict(name='Output',cells=out)],layout='counting',outputActive=counts[k])
  A=out;extra.update(cumulative=ends,K=K,low=low)
 elif kind in ['radix','bucket']:
  low=params.get('low',min(params.get('values',[0])) if n else 0) if kind=='radix' else 0
  B=params.get('base',10);exp=1;digitPasses=[]
  maximum=max([r['key']-low for r in A],default=0)
  passes=max(1,params.get('digits',0)) if 'digits' in params else 1
  if 'digits' not in params:
   z=maximum
   while z>=B:z//=B;passes+=1
  if kind=='bucket':passes=1;B=params.get('buckets',5)
  for t in range(passes):
   bins=[[] for _ in range(B)];ref=deepcopy(A)
   def rs():return [dict(name='Input reference',cells=ref,role='reference')]+[dict(name=f'Bucket {i}',cells=bs) for i,bs in enumerate(bins)]
   for r in A:
    k=((r['key']-low)//exp)%B if kind=='radix' else floor(r['key']*B/100)
    bins[k].append(r);W+=1;frame(f'Pass {t+1}: append original record {r["id"]} to FIFO bucket {k}.',rs(),layout='buckets',base=B,digit=t+1)
   if kind=='bucket':
    for k,bs in enumerate(bins):
     for i in range(1,len(bs)):
      j=i
      while j>0:
       C+=1
       if bs[j-1]['key']<=bs[j]['key']:break
       bs[j-1],bs[j]=bs[j],bs[j-1];j-=1;W+=2;S+=1
       frame(f'Insertion-sort bucket {k}; its local ordering must be established.',rs(),layout='buckets',base=B)
   A=[r for bs in bins for r in bs];W+=n;digitPasses.append([r['key'] for r in A]);frame(f'Concatenate buckets in increasing index order after pass {t+1}.',digit=t+1);exp*=B
  extra.update(passes=digitPasses,base=B,low=low)
 elif kind=='inversions':
  pairs=[]
  for i in range(n):
   for j in range(i+1,n):
    if A[i]['key']>A[j]['key']:pairs.append([i,j]);frame(f'Strict inversion ({i},{j}): earlier key {A[i]["key"]} exceeds later key {A[j]["key"]}.',active=[i,j],inversion=[i,j])
  extra['pairs']=pairs
 else:raise ValueError(kind)
 frame('Final checkpoint. All counts refer only to this specified implementation.',layout='heap' if kind=='heap' else 'array',heapSize=0 if kind=='heap' else None,prefix=n if kind!='inversions' and not params.get('partitionOnly') else 0)
 return dict(kind=kind,params=params,initial=initial,frames=frames,result=dict(keys=[r['key'] for r in A],ids=[r['id'] for r in A],comparisons=C,writes=W,swaps=S,**extra))

def svg(f):
 rows=f['rows'];N=max((len(r['cells']) for r in rows),default=0);width=max(860,156+N*70+38);height=110+len(rows)*112
 colors=dict(normal='#eff4f5',active='#f4debb',final='#d3ebe5',pivot='#d9d4f0')
 s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(f["caption"])}"><defs><marker id="sort-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 9 5 L 0 9" fill="none" stroke="#577686" stroke-width="1.5"/></marker></defs>']
 s.append('<text class="sort-meta" x="24" y="28">'+escape(' · '.join(k+' '+str(v) for k,v in f['metrics'].items()))+'</text>')
 def cell(r,x,y,fill,entity,sub=None):
  if r is None:label='hole';sub='' if sub is None else sub
  else:label=str(r['key']);sub=r['id'] if sub is None else sub
  s.append(f'<g data-entity="{escape(entity)}"><rect data-box="" x="{x}" y="{y}" width="60" height="64" rx="12" fill="{fill}" stroke="#9fb8bd"/><text data-contained="" x="{x+30}" y="{y+27}" text-anchor="middle" class="sort-key">{escape(label)}</text><text data-contained="" x="{x+30}" y="{y+49}" text-anchor="middle" class="sort-id">{escape(str(sub))}</text></g>')
 if f['layout']=='heap' and rows:
  height=540;s[0]=s[0].replace(f'{110+len(rows)*112}',str(height));A=rows[0]['cells'];end=f.get('heapSize',len(A)) or 0
  positions={}
  for i in range(end):
   dep=floor(log2(i+1));first=2**dep-1;k=i-first;positions[i]=(width*(k+.5)/2**dep,95+dep*90)
  for i,(x,y) in positions.items():
   if i:
    xp,yp=positions[(i-1)//2];dx=x-xp;dy=y-yp;dist=(dx*dx+dy*dy)**.5;st=(xp+dx/dist*29,yp+dy/dist*29);en=(x-dx/dist*29,y-dy/dist*29)
    s.append(f'<path data-edge="" d="M {st[0]} {st[1]} L {en[0]} {en[1]}" fill="none" stroke="#819ea9" stroke-width="1.6"/>')
  for i,(x,y) in positions.items():
   r=A[i];fill=colors['active'] if i in f.get('active',[]) else colors['normal']
   s.append(f'<g data-entity="{r["id"]}"><circle data-box="" cx="{x}" cy="{y}" r="29" fill="{fill}" stroke="#829fa7"/><text data-contained="" class="sort-key" x="{x}" y="{y-2}" text-anchor="middle">{r["key"]}</text><text data-contained="" class="sort-id" x="{x}" y="{y+17}" text-anchor="middle">{i}: {r["id"]}</text></g>')
  s.append('<text x="24" y="475" class="sort-label">Array / suffix</text>')
  for i,r in enumerate(A):cell(r,156+i*70,449,colors['final'] if i>=end else colors['normal'],'array-'+r['id'],str(i)+' · '+r['id'])
 else:
  for ri,row in enumerate(rows):
   y=74+ri*112;s.append(f'<text x="24" y="{y+31}" class="sort-label">{escape(row["name"])}</text>')
   for i,r in enumerate(row['cells']):
    fill=colors['normal']
    if ri==0:
     if i<f.get('prefix',0) or i>=f.get('suffix',N+1):fill=colors['final']
     if i in f.get('active',[]):fill=colors['active']
     if i==f.get('pivot'):fill=colors['pivot']
    if row.get('numeric'):fill='#e2e9f1'
    if f['layout']=='merge' and row.get('role') in ['left','right']:
     head=f.get('pointers',{}).get(row['role'],0)
     fill='#e0e5e7' if i<head else colors['active'] if i==head else colors['normal']
    entity=(row.get('role','')+'-' if row.get('role') else '')+(r['id'] if r else f'hole-{ri}-{i}')
    cell(r,156+i*70,y,fill,entity,((str(i)+' · '+r['id'] if r else str(i)) if not row.get('numeric') else r['id']))
   if ri==0 and f.get('boundaries'):
    bounds=f['boundaries'];lo,hi=f.get('range',[0,N]);points=sorted(set([lo,hi]+bounds))
    for k,(a,b) in enumerate(zip(points,points[1:])):
     if b>a:s.append(f'<rect x="{156+a*70}" y="{y-16}" width="{(b-a)*70-10}" height="6" rx="3" fill="{["#60a496","#a28cc5","#d8b271","#7094b9"][k%4]}"/>')
    s.append(f'<text class="sort-index" x="156" y="{y+87}">boundaries: '+escape(', '.join(str(b) for b in bounds))+f'; pivot value: {f.get("pivotValue","–")}</text>')
   elif f['layout']!='merge':s.append(f'<text class="sort-index" x="156" y="{y+87}">slot index · original record identity</text>')
  if f.get('inversion'):
   i,j=f['inversion'];x1=186+i*70;x2=186+j*70
   s.append(f'<path data-edge="" d="M {x1} 74 L {x1} 46 L {x2} 46 L {x2} 74" fill="none" stroke="#577686" stroke-width="1.7" marker-end="url(#sort-arrow)"/>')
  if f.get('transfer'):
   t=f['transfer'];ri=0 if t['row']=='left' else 1;x1=186+t['index']*70;y1=74+ri*112+64;x2=186+t['dest']*70;y2=74+2*112
   # Route outside the intervening row when transferring from the first run.
   lane=width-17 if ri==0 else None
   route=f'M {x1} {y1} L {x1} {y1+18} L {lane} {y1+18} L {lane} {y2-18} L {x2} {y2-18} L {x2} {y2}' if ri==0 else f'M {x1} {y1} L {x1} {y1+18} L {x2} {y1+18} L {x2} {y2}'
   s.append(f'<path data-edge="" d="{route}" fill="none" stroke="#577686" stroke-width="1.6" marker-end="url(#sort-arrow)"/>')
 s.append('</svg>');return ''.join(s)

def decorate(model,id,title,invariant):
 model.update(id=id,title=title,invariant=invariant)
 for f in model['frames']:
  f['svg']=svg(f);f['formulaHtml']=mathml.render(r'C='+str(f['metrics']['comparisons'])+r',\quad W='+str(f['metrics']['writes'])+r',\quad S='+str(f['metrics']['swaps']),True)
 return model
