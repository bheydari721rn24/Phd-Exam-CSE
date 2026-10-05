from pathlib import Path
import json,sys,math,html
from sq_engine import evaluate
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));from mathml import render
e=lambda x:html.escape(str(x),quote=True)
def tx(x,y,s,size=16,key=None):return f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="middle" font-size="{size}"'+(f' data-label-for="{e(key)}"' if key else '')+'>'+e(s)+'</text>'
def box(x,y,w,h,value,key,fill='#e5f0f2',entity=None):
 return f'<g'+(f' data-entity="{e(entity)}"' if entity else '')+f'><rect data-box="{e(key)}" x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="#7393a1" stroke-width="1.3"/>'+tx(x+w/2,y+h/2,value,18,key)+'</g>'
def arrow(x1,y1,x2,y2,id,route=None):
 d=route or f'M{x1},{y1} L{x2},{y2}'
 return f'<path d="{d}" data-layout-arrow="{e(json.dumps([[x1,y1],[x2,y2]]))}" data-connection="{id}" fill="none" stroke="#5b7d8d" stroke-width="1.5" marker-end="url(#sq-tip)"/>'
def picture(f,mode):
 parts=[];Y=44
 if 'storage' in f:
  C=f['C'];cx=380;cy=300;rad=174 if C>1 else 0
  parts.append(tx(380,28,f'Physical ring: capacity {C}, front {f["f"]}, count {f["n"]}, next insertion {f["r"]}',17))
  for i,x in enumerate(f['storage']):
   a=-math.pi/2+2*math.pi*i/C;X=cx+rad*math.cos(a);yy=cy+rad*math.sin(a);key=f'physical-{i}'
   parts.append(box(X-31,yy-24,62,48,'empty' if x is None else x,key,'#cde5db' if i==f['f'] and f['n'] else '#e5f0f2'))
   parts.append(tx(cx+(rad+72)*math.cos(a),cy+(rad+72)*math.sin(a),'slot '+str(i),14))
  if C>1:parts.append(tx(380,300,'Count '+str(f['n']),21))
  parts.append(tx(380,590,'Green occupied slot is front; unused slots are explicitly empty.',16));Y=646
 if 'shared' in f:
  z=f['shared'];values=z['L']+[None]*(z['C']-len(z['L'])-len(z['R']))+z['R'][::-1]
  f=dict(f,rows=[dict(name='Shared physical slots: left grows right, right grows left',values=values,style='indexed')]+f['rows'])
  parts.append(tx(380,Y,f'Left top {len(z["L"])-1}; right top {z["C"]-len(z["R"])}; free {z["C"]-len(z["L"])-len(z["R"])}',17));Y+=48
 if 'nodes' in f:
  v=f['nodes'];parts.append(tx(380,Y,'Live linked '+('deque' if f['bidirectional'] else 'queue')+'; endpoint handles name actual nodes',17));Y+=52
  if not v:parts.append(tx(380,Y+26,'Empty: head = tail = null',19));Y+=105
  else:
   w=min(96,620/max(1,len(v)));gap=(650-len(v)*w)/max(1,len(v)-1);xs=[55+i*(w+gap) for i in range(len(v))]
   for i,x in enumerate(v):parts.append(box(xs[i],Y,w,58,x,'node-'+str(i)))
   for i in range(len(v)-1):
    parts.append(arrow(xs[i]+w,Y+20,xs[i+1],Y+20,'next-'+str(i)))
    if f['bidirectional']:parts.append(arrow(xs[i+1],Y+42,xs[i]+w,Y+42,'prev-'+str(i)))
   parts.append(tx(xs[0]+w/2,Y-29,'head / front',14));parts.append(tx(xs[-1]+w/2,Y+90,'tail / rear',14));Y+=150
 if 'grid' in f:
  n=f['n'];w=55;start=155;parts.append(tx(380,28,f'Legal-history lattice: {n} pairs, capacity {f["h"]}',19));Y=76
  for j in range(n+1):parts.append(tx(start+j*w+24,Y-24,'d='+str(j),14))
  for i,row in enumerate(f['grid']):
   parts.append(tx(start-50,Y+i*w+24,'p='+str(i),14))
   for j,x in enumerate(row):
    legal=j<=i and i-j<=f['h'];parts.append(box(start+j*w,Y+i*w,48,48,x if legal else '—',f'cell-{i}-{j}','#cde5db' if i==f['p'] and j==f['d'] else '#e8f0f3' if legal else '#f1f1f1'))
  Y+=(n+1)*w+48
 if f.get('bars'):
  A=f['bars'];parts.append(tx(380,Y,'Histogram: unit-width nonnegative bars',17));Y+=35;baseline=Y+150;scale=145/max(1,max(A));w=600/len(A)
  for i,x in enumerate(A):parts.append(f'<rect x="{80+i*w}" y="{baseline-x*scale}" width="{w-7}" height="{x*scale}" fill="#9ec7b9" stroke="#527f70"/>');parts.append(tx(80+i*w+(w-7)/2,baseline+23,str(i),14))
  z=f.get('rect')
  if z:parts.append(f'<rect x="{80+z["left"]*w}" y="{baseline-z["height"]*scale}" width="{(z["right"]-z["left"]+1)*w-7}" height="{z["height"]*scale}" fill="none" stroke="#9b6a31" stroke-width="3"/>')
  Y=baseline+72
 if f.get('tree'):
  xy={'A':(380,Y+30),'B':(215,Y+115),'C':(545,Y+115),'D':(215,Y+200),'E':(545,Y+200)}
  for a,b in [('A','B'),('A','C'),('B','D'),('C','E')]:
   x1,y1=xy[a];x2,y2=xy[b];dx=x2-x1;dy=y2-y1;l=math.hypot(dx,dy);parts.append(arrow(x1+dx*27/l,y1+dy*27/l,x2-dx*27/l,y2-dy*27/l,a+b))
  for id,(x,y) in xy.items():parts.append(f'<circle cx="{x}" cy="{y}" r="27" fill="#e5f0f2" stroke="#7393a1"/>'+tx(x,y,id,18))
  Y+=250
 stacks=[r for r in f['rows'] if r['style']=='stack'];rows=[r for r in f['rows'] if r['style']!='stack']
 if stacks:
  maxn=max(1,max(len(r['values']) for r in stacks));height=maxn*57+76;column=680/len(stacks)
  for c,row in enumerate(stacks):
   cx=40+column*(c+.5);parts.append(tx(cx,Y,row['name'],16));bottom=Y+height-20
   for i,v in enumerate(row['values']):
    key=f'stack-{c}-{i}';entity=f'scalar-{v}' if sum(r['values'].count(v) for r in stacks)==1 else key
    parts.append(box(cx-54,bottom-(i+1)*57,108,49,v,key,'#cde5db' if i==len(row['values'])-1 else '#e5f0f2',entity))
   if not row['values']:parts.append(tx(cx,bottom-30,'empty',17))
   else:
    top=bottom-len(row['values'])*57;parts.append(tx(cx+89,top+24,'top',14));parts.append(arrow(cx+71,top+24,cx+54,top+24,'top-'+str(c)))
  Y+=height+40
 for r,row in enumerate(rows):
  parts.append(tx(380,Y,row['name'],16));Y+=30;v=row['values']
  if not v:parts.append(tx(380,Y+23,'empty',17));Y+=65;continue
  for start in range(0,len(v),10):
   seg=v[start:start+10];w=min(94,660/max(1,len(seg)));left=(760-len(seg)*w)/2
   for j,x in enumerate(seg):
    i=start+j;key=f'row-{r}-{i}';parts.append(box(left+j*w,Y,w-8,48,'empty' if x is None else x,key,'#ecd9b8' if f.get('at')==i and r==0 else '#e5f0f2'))
    if row['style']=='indexed':parts.append(tx(left+j*w+(w-8)/2,Y+74,str(i),14))
   Y+=109 if row['style']=='indexed' else 67
  Y+=19
 metrics=[]
 for k in ['n','cost','potential','peak','copies','best','added','removed']:
  if k in f:metrics.append(k+' = '+str(f[k]))
 if metrics:parts.append(tx(380,Y,'; '.join(metrics[:4]),17));Y+=38
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {Y+25}" role="img"><title>{e(mode+": "+f["caption"])}</title><defs><marker id="sq-tip" markerUnits="userSpaceOnUse" markerWidth="7" markerHeight="6" viewBox="0 0 7 6" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#5b7d8d"/></marker></defs>'+''.join(parts)+'</svg>'

contracts={
 'queue-restore':'Two FIFO transfers restore the queue; running sum covers exactly the values moved in the first pass.',
 'sortedness':'The original container remains untouched; consecutive pops of its preserving copy are tested in the declared orientation.',
'recursive':'Distinct pending continuation values restore the original stack on return; call depth and total work differ.',
'aggregate':'Completed public queue fold is output top-to-bottom followed by input bottom-to-top; partial transfers are internal.',
'sort':'Temporary stack is nondecreasing bottom-to-top after each completed insertion; final reversal sets output orientation.',
'order':'Same operation history and occupancy; LIFO and FIFO remove different identities.',
'shared':'Live stacks occupy disjoint intervals; leftTop + 1 <= rightTop.',
'linked':'Head is oldest, tail is newest; both handles are null in an empty non-sentinel queue.',
'deque':'Forward and backward links agree; endpoints are directly accessible.',
'ring':'Logical rank j occupies (front+j) mod capacity; count distinguishes full and empty.',
'resize':'Only logical-order copies are published; old physical order is not treated as FIFO order.',
'two':'Public queue = reverse(output) concatenated with input; partial transfer is an internal checkpoint, not a completed public operation.',
'two-bad':'Explicit counterexample: transfer into a nonempty output stack violates FIFO.',
'restore':'A transfer reverses stack orientation; the restoration pass restores the source.',
'qstack':'Queue front is newest simulated stack item after each completed expensive push.',
'permutation':'Increasing input is pushed only as needed; output must match the requested prefix.',
'catalan':'DP counts histories whose every prefix height lies from zero to capacity.',
'brackets':'Stack contains unmatched opening types; a closer must match its current top.',
'postfix':'Value stack represents completed subexpressions; pop right before left; use exact rational arithmetic.',
'infix':'Output is a postfix prefix; operator stack obeys precedence and incoming associativity.',
'extrema':'Each auxiliary entry is the maximum of its data-stack prefix; duplicate maxima remain represented.',
'monostack':'Candidates are unresolved indices; each removed index receives its first qualifying position.',
'histogram':'Popped height spans from leftBlocking+1 to rightExclusive-1; best area never decreases.',
'window':'Candidates are live indices in increasing order and values in decreasing order; front is window maximum.',
'dominated':'An appended identity removes larger rear values; each created identity can be deleted at most once.',
'josephus':'Rotate k-1 survivors modulo current length, then remove the kth identity.',
'worklist':'The same adjacency order is inspected with FIFO layers and LIFO preorder.'}
models=[];groups={}
def add(id,title,mode,params):
 z=evaluate(mode,params)
 for f in z['frames']:
  f['svg']=picture(f,mode);formula=r'\mathrm{checkpoint}'
  pairs=[r'\mathrm{'+k+'}='+str(f[k]) for k in ['n','cost','potential','peak','copies','best'] if k in f]
  if pairs:formula=r',\quad '.join(pairs)
  f['formulaHtml']=render(formula)
 m=dict(id=id,title=title,kind=mode,invariant=contracts[mode],assumptions='Sequential bounded model; word-sized slots unless exact rational expression arithmetic is stated. Diagram scalar identities are stable where values are distinct; duplicated data use explicit positions/indices and do not imply ambiguous moving identities.',params=params,frames=z['frames'],result=z['result']);models.append(m);return id
specs=[('order','LIFO and FIFO in the same history','order',dict(ops=['E:4','E:7','E:9','D','E:2','D','D'])),('shared','Two stacks sharing an array','shared',dict(C=10,left=[1,2],right=[8,9],ops=['L:3','R:7','L:4','R:6'])),('linked','Singleton queue and doubly linked deque','linked',dict(ops=['E:4','E:7','D','D','E:2'])),('linked','Deque forward and backward links','deque',dict(values=[2,5,8],ops=['DF','ER:11','DR','EF:1'])),('ring','Ring wrap with front and count','ring',dict(C=7,f=5,values=[10,20,30,40],ops=['E:50','D','D','E:60'])),('resize','Wrapped storage copied in logical order','resize',dict(C=5,f=3,values=[10,20,30,40,50],newC=10)),('two','Two stacks with inspection inside transfer','two',dict(ops=['E:1','E:2','E:3','D','E:4','F','D','D','D'])),('two','Why transferring early fails','two-bad',dict()),('restore','Preserving stack copy and double reversal','restore',dict(values=[3,8,2],copy=True)),('permutation','Forced stack-permutation realization','permutation',dict(target=[3,2,1,5,4])),('permutation','The 312 obstruction','permutation',dict(target=[3,1,2])),('catalan','Bounded-height legal-history lattice','catalan',dict(n=4,h=2)),('brackets','Correct nested bracket matching','brackets',dict(tokens=list('{[()]([])}'))),('postfix','Exact operand order and arithmetic','postfix',dict(tokens='18 6 3 / - 4 *'.split())),('infix','Left-associative subtraction','infix',dict(tokens='a - b - c'.split())),('infix','Right-associative exponentiation','infix',dict(tokens='a ^ b ^ c'.split())),('extrema','Duplicate maximum restoration','extrema',dict(values=[5,7,7,3],pops=3)),('monostack','Next strictly greater positions','monostack',dict(values=[2,1,2,4,3])),('histogram','Rectangle boundaries and widths','histogram',dict(values=[2,1,5,6,2,3])),('window','Expire and dominate sliding-window candidates','window',dict(values=[1,3,-1,-3,5,3,6,7],k=3)),('josephus','Cyclic rotations and Josephus removal','josephus',dict(n=7,k=3))]
specs.extend([('restore','Recursive restoration continuations','recursive',dict(values=[9,4,7])),('restore','A stack built from FIFO rotations','qstack',dict(values=[1,2,3,4],pops=2)),('extrema','Noncommutative aggregate directions','aggregate',dict()),('restore','Insertion sorting with an auxiliary stack','sort',dict(values=[3,1,4,2]))])
for i,(group,title,mode,p) in enumerate(specs,1):groups.setdefault(group,[]).append(add('concept-'+str(i),title,mode,p))
for name in ['a_stackqueue-authentic.json','a_stackqueue-questions.json']:
 a=json.loads((B/name).read_text(encoding='utf-8'))
 for q in a:
  if q['id']=='SQ_30':q['visual']=dict(mode='recursive',params=dict(values=[1,2,3,4,5,6,7,8,9]));q['visualScope']='Concrete values chosen to illustrate the stated size n=9; values do not affect the primitive count.'
  if q['id']=='SQ_31':q['visual']=dict(mode='sortedness',params=dict(values=[2,2,5]))
  if q['id']=='SQ_32':q['visual']=dict(mode='sort',params=dict(values=[3,1,4,2]));q['visualScope']='Separate concrete teaching example for the general algorithm; not supplied problem data.'
  if q['id']=='SQ_33':q['visual']=dict(mode='queue-restore',params=dict(values=[4,-2,9,4]));q.pop('visualScope',None)
  if q['id'] in ['SQ_27','SQ_29']:q['visualScope']='Separate concrete teaching example for the general n-item algorithm; not supplied problem data.'
  if q['id']=='SQ_04':q['visualScope']='Constructed payload values illustrate the question’s exact capacity and top positions; payload values were not supplied in the question.'
  if q['id']=='SQ_51':q['visualScope']='Exact subtraction trace; the right-associative exponentiation trace is separately embedded in the conversion lesson.'
  if q['id']=='SQ_61':q['visualScope']='Exact greater-or-equal variant; the written solution separately compares strictly greater answers.'
  if q['id']=='SQ_66':q['visualScope']='Exact newest-equal trace; the written solution separately derives oldest-equal argmax identities.'
  if q['id']=='SQ_23':q['visualScope']='Values 1,2,3 stand for the question labels A,B,C; the model deliberately demonstrates the invalid transfer.'
  if q['title']=='Associative but noncommutative aggregate':q['visual']=dict(mode='aggregate',params=dict())
  if 'visual' in q:q['modelId']=add('problem-'+q['id'],('Algorithm teaching example: ' if q.get('visualScope') else 'Exact problem trace: ')+q['title'],q['visual']['mode'],q['visual']['params'])
 (B/name).write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
out=dict(topicId='a_stackqueue',models=models,groups=groups)
(R/'dist/chapters/a_stackqueue-models.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'{len(models)} models; {sum(len(m["frames"]) for m in models)} exact frames; {len(specs)} lesson placements.')
