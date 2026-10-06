"""Teaching views: semantic regions, visible inputs to decisions and compact digit buckets."""
from html import escape as e
import sys,re,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'exam-rewrite'))
import mathml

PALETTE={'plain':'#eef4f8','compare':'#fff0c9','done':'#d5ede7','pivot':'#e7ddf6','less':'#d5ede7','equal':'#e7ddf6','unknown':'#fff0c9','greater':'#dce8f8','consumed':'#e1e5e8'}
GUIDES={
 'selection':['Inspect one suffix key against the current minimum.','Update the minimum index only after a strict improvement.','Exchange the minimum with the first unfinished slot.','Grow the final prefix; repeat on the remaining suffix.'],
 'insertion':['Save the next record and expose its array hole.','Compare its predecessor with the saved key.','Shift a strictly larger predecessor into the hole.','Place the saved record; the sorted prefix grows.'],
 'shell':['Select a gap and an interleaved insertion chain.','Save one record and compare the gap predecessor.','Shift larger predecessors by the current gap.','Insert the record; finish this gap before the next gap.'],
 'bubble':['Compare the next adjacent pair.','Exchange the pair only if it is inverted.','Complete the pass; its maximum enters the final suffix.','Stop after a pass with no exchanges.'],
 'merge':['Read the two already sorted runs and create an output buffer.','Compare the next unconsumed heads.','Copy the smaller head; a tie chooses the left run.','Copy any remainder without key comparisons.','Copy the completed run back into the main array.'],
 'quick':['Keep the pivot at the last slot of the current range.','Compare one unknown key with the pivot.','Extend the less region or the scanned greater-or-equal region.','Place the pivot at its final index.','Sort the two children, excluding the pivot.'],
 'three':['Maintain less, equal, unknown and greater regions.','Compare the first unknown key with the pivot value.','Extend its appropriate region; a right exchange leaves a new unknown key.','Exclude the complete equal block from recursive calls.'],
 'cmu':['Move the middle-position pivot to the front.','Compare the first unknown key with the pivot.','Accept a small key or exchange a larger key to the right region.','Place the pivot, then recurse on the two children.'],
 'hoare':['Scan from both ends until the keys stop on their pivot comparisons.','Exchange the stopped keys while the scan positions have not crossed.','Return a split boundary after the scans cross.','The split is not necessarily the position of the pivot record.'],
 'heap':['Choose the larger child of the current parent.','Compare the parent with that child.','Exchange and continue downward only if the parent is smaller.','Move the maximum into the final suffix; shrink the heap before repairing it.'],
 'counting':['Count each original key occurrence.','Accumulate counts into exclusive block ends.','Scan original records from right to left.','Decrease the corresponding end and copy the record into that output slot.'],
 'radix':['Read the current digit of the monotonically shifted key.','Append records to digit buckets in their current order.','Concatenate FIFO buckets in increasing digit order.','Advance to the next digit; earlier lower-digit order is preserved within ties.'],
 'bucket':['Distribute each key into its range bucket.','Sort each bucket internally by insertion.','Concatenate the ordered buckets.'],
 'inversions':['Inspect an earlier and a later record.','An earlier strictly larger key witnesses one inversion.','Count the pair without changing the input order.']}

def regions(f):
 n=len(f['rows'][0]['cells']) if f['rows'] else 0;lo,hi=f.get('range',[0,n]);b=f.get('boundaries',[]);kind=f.get('kind');out=[]
 if kind=='three' and len(b)==3:
  lt,i,gt=b;out=[(lo,lt,'less','< pivot'),(lt,i,'equal','= pivot'),(i,gt,'unknown','unknown'),(gt,hi,'greater','> pivot')]
 elif kind=='quick' and len(b)==3:
  left,scan,p=b;out=[(lo,left,'less','< pivot'),(left,scan,'greater','≥ pivot'),(scan,p,'unknown','unknown'),(p,hi,'pivot','pivot')]
 elif kind=='cmu' and len(b)==2:
  left,right=b;out=[(lo,lo+1,'pivot','pivot'),(lo+1,left,'less','≤ pivot'),(left,right,'unknown','unknown'),(right,hi,'greater','> pivot')]
 elif kind=='hoare' and b:
  split=b[0] if len(b)==1 else b[1] if b[0]>=b[1] else None
  out=[(lo,split,'less','≤ pivot'),(split,hi,'greater','≥ pivot')] if split is not None else [(lo,b[0],'less','≤ pivot'),(b[0],b[1],'unknown','unknown'),(b[1],hi,'greater','≥ pivot')]
 elif kind=='heap' and f.get('layout')=='heap':out=[(0,f.get('heapSize',0),'unknown','heap storage'),(f.get('heapSize',0),n,'done','final suffix')]
 elif f.get('prefix',0):out=[(0,f['prefix'],'done','sorted prefix')]
 elif f.get('suffix',n+1)<n:out=[(f['suffix'],n,'done','final suffix')]
 return [dict(lo=a,hi=b,role=role,label=label) for a,b,role,label in out if a is not None and b is not None and 0<=a<=b<=n]

def explain(f,m):
 kind=m['kind'];caption=f['caption'];op=f.get('operation')
 if not op:
  z=caption.lower();op='move' if any(x in z for x in ['shift','swap','exchange','emit','copy','place','insert']) else 'finish' if 'final checkpoint' in z else 'prepare'
 rs=regions(f);f['regions']=rs
 result=f.get('testResult');test=mathml.render(f['test']) if f.get('test') else ''
 reason=f.get('reason','')
 if not reason:
  if kind=='insertion':reason='The held record is outside the array while its hole moves left. Strict shifts retain the earlier order of equal keys.'
  elif kind=='merge':reason='Gray source records were consumed; amber marks the next head. The source runs are copies, so emitting into Output does not delete their reference cells.'
  elif kind=='heap':reason='The tree shows the live storage prefix. Heap order can be temporarily violated during construction or repair. The green array suffix is final and is never included in a later repair.'
  elif kind in ['quick','cmu','three','hoare']:reason='Colored regions are labeled by their key relation. Empty intervals are valid. Read the exact boundaries below; a split and a final pivot index have different contracts.'
  elif kind=='counting':reason='A cumulative end is a one-past-the-end slot. Decrease it before placement, and scan right-to-left to preserve equal-key record order.'
  elif kind=='radix':reason='Bucket order is increasing digit order; within a bucket, records keep arrival order. Letters reveal whether equal-digit stability is preserved.'
  elif kind=='bucket':reason='Equal-width ranges determine bucket membership. Records inside a bucket still need sorting; concentration can cause quadratic local work.'
  else:reason='Only keys participate in comparisons. Record letters retain their original identities through every movement.'
 guide=GUIDES.get(kind,[]);line=1
 if kind in ['insertion','shell']:line=2 if op=='compare' else 3 if 'Shift' in caption else 4 if 'Insert' in caption else 1
 elif kind=='merge':line=2 if op=='compare' else 4 if 'remaining' in caption else 5 if 'back' in caption else 3 if 'Emit' in caption else 1
 elif kind in ['quick','cmu']:line=2 if op=='compare' else 4 if 'final position' in caption or 'reaches' in caption else 3 if 'Classify' in caption or 'scan:' in caption else 1
 elif kind=='three':line=2 if op=='compare' else 4 if 'no further' in caption else 3 if 'Ternary' in caption else 1
 elif kind=='heap':line=1 if 'two children' in caption else 2 if op=='compare' else 4 if 'Maximum' in caption else 3
 elif kind=='counting':line=1 if 'Count an' in caption else 2 if 'Prefix' in caption or 'Cumulative' in caption else 4 if 'scatter' in caption else 3
 elif kind in ['radix','bucket']:line=2 if op=='distribute' and kind=='radix' or 'Insertion-sort' in caption else 3 if 'Concatenate' in caption else 1
 elif kind=='selection':line=1 if op=='compare' else 3 if 'Place' in caption else 2
 elif kind=='hoare':line=3 if 'Return split' in caption else 2 if 'Exchange' in caption else 1
 elif kind=='bubble':line=1 if op=='compare' else 2 if 'Swap' in caption else 3 if 'Largest' in caption else 4
 return dict(operation=op,testHtml=test,decision=('True' if result else 'False') if result is not None else '',why=reason,guide=guide,activeLine=line,regions=rs)

def svg(f):
 if f['layout']=='heap':
  return heap_svg(f)
 rows=f['rows'];N=max((len(r['cells']) for r in rows),default=0);width=max(900,194+N*70);height=160+len(rows)*140;s=[]
 def cell(r,x,y,fill,entity,sub,w=60,h=64,slot=None):
  label='hole' if r is None else str(r['key']);s.append(f'<g data-entity="{e(entity)}"><rect data-box="" x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#7b98aa"/><text data-contained="" class="sort-key" text-anchor="middle" x="{x+w/2}" y="{y+27}">{e(label)}</text><text data-contained="" class="sort-id" text-anchor="middle" x="{x+w/2}" y="{y+49}">{e(str(sub))}</text></g>')
  if slot is not None:s.append(f'<text class="sort-index" text-anchor="middle" x="{x+w/2}" y="{y+h+24}">{e(str(slot))}</text>')
 if f['layout']=='buckets':
  for i,r in enumerate(rows[0]['cells']):cell(r,156+i*70,84,PALETTE['compare'] if r and r['id']==f.get('distributedId') else PALETTE['plain'],'reference-'+r['id'],r['id'],slot='slot '+str(i))
  s.append('<text class="sort-label" x="24" y="115">Current input</text><text class="sort-pointer" x="24" y="56">FIFO arrival order within a bucket: top to bottom</text>');cols=min(5,len(rows)-1);cardW=(width-48-(cols-1)*16)/cols;top=205;target=None
  for start in range(1,len(rows),cols):
   chunk=rows[start:start+cols];depth=max(1,max(len(r['cells']) for r in chunk));cardH=70+depth*74
   for col,row in enumerate(chunk):
    x=24+col*(cardW+16);idx=start-1+col;s.append(f'<rect data-card="" x="{x}" y="{top}" width="{cardW}" height="{cardH}" rx="12" fill="{PALETTE["compare"] if idx==f.get("bucketIndex") else "#f7fafc"}" stroke="#a8becb"/><text class="sort-label" x="{x+14}" y="{top+29}">{e(row["name"])}</text>')
    for j,r in enumerate(row['cells']):
     cell(r,x+(cardW-60)/2,top+49+j*74,PALETTE['plain'],r['id'],r['id'])
     if r['id']==f.get('distributedId') and idx==f.get('bucketIndex'):target=(x+cardW-6,x+(cardW-60)/2+60,top+49+j*74+32)
    if not row['cells']:s.append(f'<text class="sort-id" x="{x+14}" y="{top+77}">empty</text>')
   top+=cardH+22
  height=top+20
  if target:
   r=f['distributedId'];i=next(i for i,x in enumerate(rows[0]['cells']) if x['id']==r);x1=216+70*i;lane,x2,y2=target;route=f'M {x1} 116 L {x1+5} 116 L {x1+5} 190 L {lane} 190 L {lane} {y2} L {x2} {y2}';s.append(f'<path data-edge="" data-source-entity="reference-{r}" data-target-entity="{r}" d="{route}" fill="none" stroke="#426e91" stroke-width="2" marker-end="url(#sort-arrow)"/>')
 else:
  for ri,row in enumerate(rows):
   y=116+ri*140;s.append(f'<text class="sort-label" x="24" y="{y+31}">{e(row["name"])}</text>')
   for i,r in enumerate(row['cells']):
    fill=PALETTE['plain']
    if ri==0:
     for region in f.get('regions',[]):
      if region['lo']<=i<region['hi']:fill=PALETTE[region['role']]
     if i in f.get('active',[]):fill=PALETTE['compare']
     if i==f.get('pivot'):fill=PALETTE['pivot']
    if row.get('numeric'):fill='#dce8f8'
    if row.get('role') in ['left','right']:
     head=f.get('pointers',{}).get(row['role'],0);fill=PALETTE['consumed'] if i<head else PALETTE['compare'] if i==head else PALETTE['plain']
    prefix='counter-' if row.get('numeric') else row.get('role','')+'-' if row.get('role') else ''
    entity=prefix+(r['id'] if r else f'hole-{ri}-{i}');sub='' if row.get('numeric') else r['id'] if r else ''
    cell(r,156+i*70,y,fill,entity,sub,slot=('key '+r['id'] if row.get('numeric') else 'slot '+str(i)))
   if ri==0:
    for region in f.get('regions',[]):
     a,b=region['lo'],region['hi']
     if b>a:s.append(f'<rect x="{156+a*70}" y="96" width="{(b-a)*70-10}" height="7" rx="3" fill="{ {"less":"#287d6b","equal":"#8057aa","greater":"#476d9e","unknown":"#b3832c","pivot":"#8057aa","done":"#287d6b"}[region["role"]]}"/>')
   # A visible head marker is above the consumed/reference run, never in the transfer lane.
   if f['layout']=='merge' and row.get('role') in ['left','right']:
    head=f.get('pointers',{}).get(row['role'],0)
    if head<len(row['cells']):s.append(f'<text class="sort-pointer" text-anchor="middle" x="{186+head*70}" y="{y-24}">head {head}</text><path d="M {186+head*70} {y-17} L {186+head*70} {y}" stroke="#a57425" marker-end="url(#sort-arrow)"/>')
   if ri==0 and f.get('pointers') and f['layout']!='merge':
    names={}
    for name,index in f['pointers'].items():
     if 0<=index<len(row['cells']):names.setdefault(index,[]).append(name)
    for i,labels in names.items():s.append(f'<text class="sort-pointer" x="{186+i*70}" y="{y-35}" text-anchor="middle">{e("/".join(labels))}</text>')
  if f.get('transfer'):
   t=f['transfer'];ri=0 if t['row']=='left' else 1;x1=216+t['index']*70;y1=116+ri*140+32;x2=186+t['dest']*70;y2=116+2*140;lane=width-18;corridor=116+ri*140+106
   route=f'M {x1} {y1} L {x1+5} {y1} L {x1+5} {corridor} L {lane} {corridor} L {lane} {y2-18} L {x2} {y2-18} L {x2} {y2}' if ri==0 else f'M {x1} {y1} L {x1+5} {y1} L {x1+5} {corridor} L {x2} {corridor} L {x2} {y2}'
   r=rows[ri]['cells'][t['index']];s.append(f'<path data-edge="" data-source-entity="{t["row"]}-{r["id"]}" data-target-entity="output-{r["id"]}" d="{route}" stroke="#426e91" stroke-width="2" fill="none" marker-end="url(#sort-arrow)"/>')
  if f.get('outputActive') is not None:
   k=f['outputActive'];r=rows[2]['cells'][k];i=next(i for i,x in enumerate(rows[0]['cells']) if x['id']==r['id']);x1=216+70*i;x2=186+70*k;route=f'M {x1} 148 L {x1+5} 148 L {x1+5} 222 L {width-18} 222 L {width-18} 378 L {x2} 378 L {x2} 396';s.append(f'<path data-edge="" data-source-entity="reference-{r["id"]}" data-target-entity="{r["id"]}" d="{route}" fill="none" stroke="#426e91" stroke-width="2" marker-end="url(#sort-arrow)"/>')
  if f.get('inversion'):
   i,j=f['inversion'];x1=186+i*70;x2=186+j*70;s.append(f'<path data-edge="" d="M {x1} 116 L {x1} 75 L {x2} 75 L {x2} 116" stroke="#426e91" stroke-width="2" fill="none" marker-end="url(#sort-arrow)"/>')
 top='<text class="sort-meta" x="24" y="30">'+e(' · '.join(k+' '+str(v) for k,v in f['metrics'].items()))+'</text>'
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{e(f["caption"])}"><defs><marker id="sort-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 1 L 9 5 L 0 9" fill="none" stroke="#426e91" stroke-width="1.5"/></marker></defs>{top}'+re.sub(r'<text[^>]*></text>','',''.join(s))+'</svg>'

def heap_svg(f):
 A=f['rows'][0]['cells'];end=f.get('heapSize',len(A)) or 0;width=max(900,194+len(A)*70);pos={};s=[]
 for i in range(end):
  d=math.floor(math.log2(i+1));k=i-(2**d-1);pos[i]=(width*(k+.5)/2**d,110+90*d)
 for i,(x,y) in pos.items():
  if not i:continue
  px,py=pos[(i-1)//2];dx=x-px;dy=y-py;length=math.hypot(dx,dy);s.append(f'<path data-edge="" d="M {px+dx*29/length} {py+dy*29/length} L {x-dx*29/length} {y-dy*29/length}" stroke="#678ba3" stroke-width="1.8" fill="none"/>')
 for i,(x,y) in pos.items():
  r=A[i];color=PALETTE['compare'] if i in f.get('active',[]) else PALETTE['plain'];s.append(f'<g data-entity="{r["id"]}"><circle data-box="" cx="{x}" cy="{y}" r="29" fill="{color}" stroke="#7b98aa"/><text data-contained="" class="sort-key" x="{x}" y="{y-2}" text-anchor="middle">{r["key"]}</text><text data-contained="" class="sort-id" x="{x}" y="{y+17}" text-anchor="middle">{r["id"]}</text></g><text class="sort-index" x="{x}" y="{y+46}" text-anchor="middle">slot {i}</text>')
 for i,r in enumerate(A):
  x=156+70*i;color=PALETTE['done'] if i>=end else PALETTE['plain'];s.append(f'<g data-entity="array-{r["id"]}"><rect data-box="" x="{x}" y="465" width="60" height="64" rx="10" fill="{color}" stroke="#7b98aa"/><text data-contained="" class="sort-key" x="{x+30}" y="492" text-anchor="middle">{r["key"]}</text><text data-contained="" class="sort-id" x="{x+30}" y="514" text-anchor="middle">{r["id"]}</text></g><text class="sort-index" x="{x+30}" y="553" text-anchor="middle">slot {i}</text>')
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 590" role="img" aria-label="{e(f["caption"])}"><text class="sort-meta" x="24" y="30">Heap storage prefix: {end} slots; final suffix [{end}, {len(A)})</text><text class="sort-label" x="24" y="496">Array / suffix</text>'+''.join(s)+'</svg>'
