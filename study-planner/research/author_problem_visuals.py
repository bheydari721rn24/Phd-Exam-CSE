"""Problem-specific visual additions from explicit question data, never random examples."""
from pathlib import Path
from fractions import Fraction as F
import json,re,html,math,itertools,sys,collections
R=Path(__file__).resolve().parents[1];O=R/'research/library-visual-question-review';D=R/'dist/chapters'
sys.path.insert(0,str(R/'research/exam-rewrite'));import mathml
from problem_circuits import circuit_models,word_model,arrival_model
from problem_traces import programming
rows=json.loads((O/'input.json').read_text()); sources={}
def norm(s):return re.sub(r'^Question \d+\.\s*','',s).strip()
for p in (R/'research').glob('*-questions.json'):
 try: qs=json.loads(p.read_text())
 except Exception:continue
 if isinstance(qs,list):
  for q in qs:
   if isinstance(q,dict) and 'title' in q:sources[(p.name.split('-questions')[0],q['title'])]=q
def esc(s):return html.escape(str(s),quote=True)
def tx(x,y,s,size=19,anchor='middle',cls=''):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" class="{cls}">{esc(s)}</text>'
def rect(x,y,w,h,fill='#edf5f8',id=''):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="#91adb9"'+(f' data-box="{id}"' if id else '')+'/>'
def line(x,y,X,Y,color='#557e91',arrow=False):
 return f'<path d="M{x},{y}L{X},{Y}" fill="none" stroke="{color}" stroke-width="1.6"'+(' marker-end="url(#problem-tip)"' if arrow else '')+'/>'
def svg(body,title,height=360):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {height}" role="img" aria-label="{esc(title)}"><title>{esc(title)}</title><defs><marker id="problem-tip" markerWidth="7" markerHeight="6" refX="7" refY="3" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0L7 3L0 6Z" fill="#557e91"/></marker></defs>{body}</svg>'
def frame(body,caption,**data):return dict(html=body,caption=caption,**data)
def model(kind,frames,reading,scope):return dict(kind=kind,frames=frames,reading=reading,scope=scope)
def matrix_picture(A,active=None,augmented=False):
 h=max(360,len(A)*54+140);cols=max(map(len,A));w=min(100,600/cols);x=(760-cols*w)/2;y=90;s=''
 for i,row in enumerate(A):
  for j,v in enumerate(row):
   s+=rect(x+j*w,y+i*54,w,54,'#ffecd1' if active and (i,j) in active else '#edf5f8');label=str(v);cx=x+(j+.5)*w;cy=y+i*54
   if re.fullmatch(r'-?\d+/\d+',label):
    a,b=label.split('/');s+=tx(cx,cy+20,a,16)+line(cx-15,cy+26,cx+15,cy+26)+tx(cx,cy+44,b,16)
   else:s+=tx(cx,cy+33,v,21)
 if augmented:s+=f'<path d="M{x+(cols-1)*w} {y-6}V{y+len(A)*54+6}" stroke="#557e91" stroke-width="3"/>'
 s+=tx(380,48,('Coefficients | right-hand side; ' if augmented else '')+f'{len(A)} rows × {cols} columns',20,cls='prose-label')
 return svg(s,'Exact matrix entries',h)
def gauss(A,maxcols):
 a=[[F(v) for v in row] for row in A];augmented=maxcols==len(a[0])-1; frames=[frame(matrix_picture(a,augmented=augmented),'Original matrix. Row positions are equations; column positions retain their original coordinate meaning.',matrix=[[str(v) for v in row] for row in a])]; r=0
 def save(caption,active):frames.append(frame(matrix_picture(a,active,augmented),caption,matrix=[[str(v) for v in row] for row in a]))
 for c in range(maxcols):
  pivot=next((k for k in range(r,len(a)) if a[k][c]),None)
  if pivot is None:continue
  if pivot!=r:a[r],a[pivot]=a[pivot],a[r];save(f'Swap rows {r+1} and {pivot+1}. The solution set is unchanged.',[(r,j) for j in range(len(a[0]))]+[(pivot,j) for j in range(len(a[0]))])
  v=a[r][c]
  if v!=1:a[r]=[x/v for x in a[r]];save(f'Divide row {r+1} by the nonzero pivot {v}. Apply the operation to the entire row.',[(r,j) for j in range(len(a[0]))])
  for k in range(len(a)):
   if k!=r and a[k][c]:v=a[k][c];a[k]=[x-v*y for x,y in zip(a[k],a[r])];save(f'Row {k+1} ← row {k+1} − ({v}) × row {r+1}. Only this row is replaced.',[(k,j) for j in range(len(a[0]))])
  r+=1
  if r==len(a):break
 return frames,[[str(v) for v in row] for row in a]
def strip(vals,active=None,title='Indexed storage'):
 w=min(74,650/max(1,len(vals)));x=(760-w*len(vals))/2;s=tx(380,44,title,21,cls='prose-label')
 for i,v in enumerate(vals):s+=rect(x+i*w,120,w,60,'#ffecd1' if i==active else '#edf5f8')+tx(x+(i+.5)*w,157,v,20)+tx(x+(i+.5)*w,215,i,17)
 s+=tx(380,280,'Indices remain fixed; values occupy the displayed slots.',18,cls='prose-label')
 return svg(s,title)
def relation(pairs,title):
 values=sorted(set(itertools.chain.from_iterable(pairs)));n=len(values);pos={v:(380+230*math.cos(-math.pi/2+2*math.pi*i/n),170+110*math.sin(-math.pi/2+2*math.pi*i/n)) for i,v in enumerate(values)};s=''
 for a,b in pairs:
  x,y=pos[a];X,Y=pos[b];r=25
  if a==b:s+=f'<path d="M{x-17.68} {y-17.68}C{x-55} {y-65} {x+55} {y-65} {x+17.68} {y-17.68}" fill="none" stroke="#557e91" stroke-width="1.6" marker-end="url(#problem-tip)"/>'
  else:
   dx=X-x;dy=Y-y;d=math.hypot(dx,dy);ax=x+r*dx/d;ay=y+r*dy/d;bx=X-r*dx/d;by=Y-r*dy/d
   if (b,a) in pairs:
    # Equal and opposite curves keep both relation directions visible.
    cx=(x+X)/2-16*dy/d;cy=(y+Y)/2+16*dx/d
    s+=f'<path d="M{ax} {ay}Q{cx} {cy} {bx} {by}" fill="none" stroke="#557e91" stroke-width="1.6" marker-end="url(#problem-tip)"/>'
   else:s+=line(ax,ay,bx,by,arrow=True)
 for v,(x,y) in pos.items():s+=f'<circle cx="{x}" cy="{y}" r="25" fill="#edf5f8" stroke="#557e91"/>'+tx(x,y+7,v,20)
 return svg(s+tx(380,330,'An arrow a → b means the ordered pair (a, b).',18,cls='prose-label'),title)
def kmap(data):
 n=data['n'];on=set(data['on']);dc=set(data.get('dc',[]));gray=[0,1,3,2];covers=data.get('covers') or [[]];selected=covers[0];frames=[]
 for k in range(len(selected)+1):
  s='';panels=2 if n==5 else 1;nr=2 if n==3 else 4;cell=52;x0=110 if panels==2 else 250
  for panel in range(panels):
   x=x0+panel*350;y=92;s+=tx(x+104,42,f'A = {panel}' if panels==2 else f'{n}-variable Gray map',20,cls='prose-label')
   for j,v in enumerate(gray):s+=tx(x+(j+.5)*cell,77,format(v,'02b'),17)
   for i in range(nr):
    rv=i if nr==2 else gray[i];s+=tx(x-27,y+(i+.5)*cell+6,format(rv,'01b' if nr==2 else '02b'),17)
    for j,cv in enumerate(gray):
     index=panel*16+rv*4+cv;bits=format(index,f'0{n}b');covered=any(all(a=='-' or a==b for a,b in zip(c,bits)) for c in selected[:k]);val='X' if index in dc else str(int(index in on));s+=rect(x+j*cell,y+i*cell,cell,cell,'#ffe7b9' if covered else '#e0f0e7' if index in on else '#fff')+tx(x+(j+.5)*cell,y+(i+.5)*cell+7,val,22)+tx(x+j*cell+8,y+i*cell+14,index,11,anchor='start')
  s+=tx(380,340,'Selected cubes: '+(', '.join(selected[:k]) or 'none yet'),17,cls='prose-label')
  frames.append(frame(svg(s,'Question-specific Karnaugh map'),('Original ON/DC specification. Gray adjacency wraps across opposite boundaries.' if k==0 else f'Include cube {selected[k-1]}. Highlighting denotes '+('covered zero obligations for POS.' if data.get('pos') else 'covered one obligations for SOP.')),on=sorted(on),dc=sorted(dc),selected=selected[:k]))
 return model('karnaugh-map',frames,'Match the decimal minterm index to its Gray-ordered cell. Inspect each selected cube and compare its fixed bits with the solution.','A selected optimal cover is shown; all alternative optimal covers remain in the written solution. X denotes a genuine don’t-care, never a mandatory one.')
def mux(data,stem):
 remaining=data['remaining'];free='ABC'[remaining];select=''.join(v for i,v in enumerate('ABC') if i!=remaining);m=re.search(r'select order is \$?([ABC]{2})',stem)
 if m:select=m[1]
 tuple_=data['data'];on=set(data['on']);frames=[]
 for row in range(8):
  bits=format(row,'03b');address=int(''.join(bits['ABC'.index(c)] for c in select),2);out=int(row in on)
  residual=tuple_[address].replace(' ','');computed=int(residual) if residual in ['0','1'] else 1-int(bits[remaining]) if 'overline' in residual else int(bits[remaining]);assert computed==out,(row,select,tuple_)
  s=tx(380,38,f'Input ABC = {bits}; selected address {address:02b}',21,cls='prose-label')
  s+=f'<path d="M330 70L455 100V280L330 310Z" fill="#edf5f8" stroke="#557e91" stroke-width="1.5"/>'+tx(390,190,'4:1 MUX',20,cls='prose-label')
  for i,v in enumerate(tuple_):
   label=v.replace('\\overline ', 'NOT ').replace('\\overline','NOT ');y=112+i*52;s+=tx(140,y+6,f'D{i} = {label}',19,cls='prose-label')+line(230,y,330,y,'#b17d55' if i==address else '#91adb9')
  s+=line(455,190,620,190)+tx(660,197,f'F = {out}',23)+line(375,330,375,296)+tx(510,330,f'Select {select} = '+''.join(bits['ABC'.index(c)] for c in select),18,cls='prose-label')
  frames.append(frame(svg(s,'Exact four-input multiplexer connections'),f'For ABC={bits}, address {address:02b} selects D{address}; evaluate its residual function at {free}={bits[remaining]} to obtain {out}.',row=row,output=out))
 return model('multiplexer',frames,'Follow the selected data wire, then substitute the residual input. Select-bit order is explicit and matches this question.','Each step is a separate settled input valuation, not an electrical timing model.')
def truth_model(data,kind):
 if kind=='miter':n=4;values=[[i,*v,int(v[0]!=v[1])] for i,v in enumerate(data['values'])];headers=['ABCD','F','G','F XOR G'];title='Equivalence miter';captions=['Compare the same input in both functions. Highlighted discrepancies reject equivalence.']*len(values)
 else:n=data['n'];values=[[i,*list(v)] for i,v in enumerate(data['words'])];headers=['Input']+[f'Output {j}' for j in range(len(values[0])-1)];title='Multi-output contract';captions=['Read all specified outputs for this input, rather than checking only one pin.']*len(values)
 frames=[];h=max(360,len(values)*33+140);dx=600/len(headers)
 for active in range(len(values)):
  s=tx(380,30,title,22,cls='prose-label')
  for j,v in enumerate(headers):s+=tx(90+(j+.5)*dx,67,v,19,cls='prose-label')
  for i,row in enumerate(values):
   for j,v in enumerate(row):s+=rect(90+j*dx,82+i*33,dx,33,'#ffe7b9' if active==i else '#fff')+tx(90+(j+.5)*dx,104+i*33,format(v,f'0{n}b') if j==0 else v,17)
  frames.append(frame(svg(s,title,h),f'Input {format(active,f"0{n}b")}. '+captions[active],values=values,active=active))
 return model('truth-contract',frames,'Use one complete input valuation per row. Read every output before deciding equivalence or contract satisfaction.','Settled truth values only; no propagation delay is inferred.')
def arrays_move(data):
 original,src,dst,count,direction,expected=data;a=original[:];frames=[frame(strip(a,title='Original array'),'Original storage, before any write.',values=a[:])]
 for t in (range(count) if direction=='forward' else range(count-1,-1,-1)):
  value=a[src+t];a[dst+t]=value;frames.append(frame(strip(a,dst+t,'Actual in-place movement'),f'Read A[{src+t}] = {value}, then write A[{dst+t}] = {value}. Later reads use this current storage, not an implicit snapshot.',values=a[:],source=src+t,destination=dst+t))
 assert a==expected,(a,expected)
 return model('array-copy',frames,'Inspect the source before each destination write. Compare the final values with the original-value contract in the solution.','This is the specified traversal direction; a failing forward copy is deliberately displayed, not silently repaired.')
def numeric_tuples(formulas):
 result=[]
 for f in formulas:
  m=re.fullmatch(r'\(?\s*(-?\d+(?:/\d+)?(?:\s*,\s*-?\d+(?:/\d+)?){1,15})\s*\)?',f)
  if m:
   try:result.append([F(v.strip()) for v in m[1].split(',')])
   except ValueError:pass
 return result
def probability_model(q,topic):
 tuples=numeric_tuples(q['formulas']);text=q['text'].lower()
 if topic=='s_bayes' and ('prior' in text) and ('likelihood' in text) and len(tuples)>=2:
  priors,likelihood=tuples[:2]
  if len(priors)!=len(likelihood) or sum(priors)!=1 or not all(0<=v<=1 for v in priors+likelihood):return
  joint=[a*b for a,b in zip(priors,likelihood)];total=sum(joint)
  if total==0:return
  vectors=[priors,joint,[v/total for v in joint]];names=['Prior stratum masses','Observation masses: prior × likelihood','Posterior after dividing by the evidence mass'];frames=[]
  for vals,name in zip(vectors,names):
   s=tx(380,36,name,21,cls='prose-label')+line(65,270,710,270)
   for i,v in enumerate(vals):x=90+i*580/len(vals);w=min(100,420/len(vals));height=180*float(v);s+=rect(x,270-height,w,height,'#bddfcd')+tx(x+w/2,250-height,str(v),21)+tx(x+w/2,310,f'H{i+1}',19)
   frames.append(frame(svg(s,name),name+'. Evidence mass = '+str(total)+'.',values=[str(v) for v in vals]))
  return model('bayesian-masses',frames,'Track one hypothesis through prior mass, retained observation mass and normalized posterior. Relative evidence weights determine the final bars.','The explicit probability vectors in this question are used. Bars share a fixed unit-probability vertical scale.')
def formula_inspection(q):
 sol=re.search(r'<details class="exam-solution"[\s\S]*?</details>',q['html'])
 if not sol:return
 displays=re.findall(r'<math\b[^>]*display="block"[^>]*>[\s\S]*?</math>',sol[0]); seen=[]
 for f in displays:
  if f not in seen:seen.append(f)
 if len(seen)<2:return
 frames=[frame('<div class="problem-exact-formula">'+f+'</div>',f'Inspect displayed expression {i+1} in the written derivation. Read its assumptions and preceding justification in the solution.') for i,f in enumerate(seen)]
 return model('mathematical-derivation',frames,'Inspect the exact displayed mathematical objects in their written order. The surrounding proof supplies each justification; unrelated objects are not asserted equal.','This is a paced inspection of the actual solution formulas, not a new proof or invented state transition.')
def relation_model(q):
 f=next((f for f in q['formulas'] if re.match(r'R(?:_\d)?=\\\{\(',f)),None)
 if not f:return
 pairs=[tuple(map(int,m)) for m in re.findall(r'\((-?\d+),(-?\d+)\)',f)]
 if not pairs or len(set(itertools.chain.from_iterable(pairs)))>9:return
 return model('directed-relation',[frame(relation(pairs,'The relation specified in this question'),'Only the explicitly specified ordered pairs are drawn.',pairs=pairs)],'Follow the arrow direction when composing the relation. A path witnesses a composition; reversing an arrow changes the relation.','The given relation is shown, not an assumed reflexive or transitive closure.')
def matrix_formula(q):
 forms=[f for f in q['formulas'] if '\\begin{bmatrix}' in f or '\\begin{pmatrix}' in f]
 frames=[]
 for f in forms:
  m=re.search(r'\\begin\{[bp]matrix\}([\s\S]*?)\\end\{[bp]matrix\}',f)
  if not m:continue
  A=[row.split('&') for row in m[1].split('\\\\')]
  if len(A)>8 or max(map(len,A))>8:continue
  if all(re.fullmatch(r'-?\d+(?:/\d+)?',v.strip()) for row in A for v in row):frames.append(frame(matrix_picture(A),'Matrix exactly as displayed in this question; row and column order are retained.',matrix=A))
 if not frames:return
 return model('matrix-objects',frames,'Read dimensions before multiplying or comparing these matrices. Display order follows the question and solution; distinct matrices are not asserted equal.','Exact displayed numeric objects only; any transformation claim comes from the accompanying written reasoning.')
def array_objects(q):
 vals=[]
 for f in q['formulas']:
  m=re.search(r'\[\s*(-?\d+(?:\s*,\s*-?\d+){2,19})\s*\]',f)
  if m:
   a=list(map(int,m[1].split(',')))
   if a not in vals:vals.append(a)
 if not vals:return
 return model('indexed-objects',[frame(strip(v,title='Array explicitly given in the question or derivation'),'Read each indexed value in the specified array.',values=v) for v in vals],'Match each value to its index. Different arrays are separately labeled objects from the written problem; the solution specifies any operation connecting them.','No inferred operation, sorted order or implicit copy is added.')

def canonical_rows(q):
 stem=q['html'].split('<details')[0].split('<ol class="exam-options"')[0]
 if not re.search(r'true exactly on rows',stem):return
 match=next((f for f in q['formulas'] if re.fullmatch(r'[01]{3}(?:,[01]{3}){1,7}',f)),None)
 if not match:return
 on=set(int(v,2) for v in match.split(','));frames=[]
 for active in range(8):
  body=tx(380,30,'Specified true rows and canonical maxterms',21,cls='prose-label')
  for i in range(8):
   bits=format(i,'03b');y=65+i*36;clause=' ∨ '.join(('¬' if b=='1' else '')+v for v,b in zip('ABC',bits))
   body+=rect(95,y,570,36,'#ffe7b9' if i==active else '#e0f0e7' if i in on else '#fff')+tx(165,y+24,bits,19)+tx(270,y+24,'F = '+str(int(i in on)),18)+tx(455,y+24,'no maxterm' if i in on else clause,18)
  frames.append(frame(svg(body,'Question-specific canonical CNF table',410),f'Row {active:03b} is '+('true: it supplies no canonical maxterm.' if active in on else 'false: include the clause whose every literal is false on this row.'),trueRows=sorted(on),active=active))
 return model('canonical-truth-rows',frames,'A canonical CNF is indexed by false rows. Compare a row bit with the polarity of its maxterm literal, then take the conjunction of all required maxterms.','The question’s three-variable true-row set is used. Positional labels ABC follow its listed row order; canonical expansion is distinct from minimization.')
def atoms_picture(atoms,target):
 n=int(math.log2(len(atoms)));frames=[]
 predicates={'union':lambda i:i!=0,'none':lambda i:i==0,'exact1':lambda i:i.bit_count()==1,'exact2':lambda i:i.bit_count()==2,'atleast2':lambda i:i.bit_count()>=2,'odd':lambda i:i.bit_count()%2==1}
 choose=predicates.get(target,lambda i:True);total=sum(v for i,v in enumerate(atoms) if choose(i))
 for active in [None,*range(len(atoms))]:
  body=tx(380,35,f'Disjoint membership atoms; target = {target}',21,cls='prose-label')
  for i,v in enumerate(atoms):
   x=70+(i%4)*158;y=80+(i//4)*115;body+=rect(x,y,145,90,'#ffe7b9' if i==active else '#d8ece1' if choose(i) else '#eef2f4')+tx(x+72,y+31,format(i,f'0{n}b'),23)+tx(x+72,y+66,'mass '+str(v),19,cls='prose-label')
  body+=tx(380,335,'Target sum = '+str(total),21,cls='prose-label');frames.append(frame(svg(body,'Disjoint event membership table'),f'Bit i records membership in event i; the zero mask is outside every event. Selected atoms contribute {total} in total.',atoms=atoms,target=target,total=total))
 return model('disjoint-event-atoms',frames,'Use disjoint atoms to avoid double counting inclusive overlaps. A highlighted mask records exactly which events occur.','Membership bit positions follow the chapter bit-mask convention; rectangle areas are not proportional to masses.')
def inclusion_model(cert):
 kind=cert.get('kind')
 if kind=='atoms':return atoms_picture(cert['atoms'],cert['target'])
 if kind=='divisible':
  ds=cert['divisors'];a=[0]*(2**len(ds))
  for v in range(cert['L'],cert['H']+1):a[sum(1<<i for i,d in enumerate(ds) if v%d==0)]+=1
  return atoms_picture(a,cert['target'])
 if kind=='edges':return model('adjacency-constraints',[frame(relation(cert['edges'],'Directed block requirements'),'Each arrow requires consecutive order, not merely coexistence.',edges=cert['edges'])],'Check whether required arrows form compatible chains or conflicting successors before contracting blocks.','Arrows are adjacency constraints in permutations, not an arbitrary transitive relation.')
 if kind=='board':
  n=cert['n'];w=min(55,280/n);x=(760-n*w)/2;s=tx(380,35,'Forbidden assignment board',23,cls='prose-label')
  for i in range(n):
   s+=tx(x-25,85+(i+.5)*w, i,17)
   for j in range(n):s+=rect(x+j*w,85+i*w,w,w,'#efd4d7' if [i,j] in cert['board'] else '#fff')+tx(x+(j+.5)*w,85+(i+.5)*w+6,'×' if [i,j] in cert['board'] else '',22)
  for j in range(n):s+=tx(x+(j+.5)*w,65,j,17)
  return model('forbidden-board',[frame(svg(s,'The specified forbidden board',max(360,120+n*w)), 'A permutation places one rook in every row and column; marked cells are forbidden.',board=cert['board'])],'Count compatible forbidden placements using nonattacking rooks. Shared rows or columns prevent treating components as independent.','Exact specified board. A marked cell is forbidden, not a chosen rook.')
def occupancy(vals,title):
 maxv=max([1,*vals]);w=min(85,570/len(vals));x=(760-len(vals)*w)/2;s=tx(380,35,title,21,cls='prose-label')+line(55,285,705,285)
 for i,v in enumerate(vals):h=180*v/maxv;s+=rect(x+i*w+6,285-h,w-12,h,'#bddfcd')+tx(x+(i+.5)*w,267-h,v,20)+tx(x+(i+.5)*w,320,f'bin {i+1}',16,cls='prose-label')
 return svg(s,title)
def pigeon_model(cert):
 kind=cert.get('kind');vals=cert.get('occupancies') or cert.get('capacities') or cert.get('stocks')
 if vals and len(vals)<=20:return model('bin-occupancies',[frame(occupancy(vals,'Specified occupancies, capacities or inventories'),'The displayed vector is the one explicitly specified in the question. Identify whether it denotes loads, capacity limits or available stock before applying an inequality.',values=vals)],'Compare the exact per-bin constraints with the target. Capacity and actual occupancy are distinct quantities.','Fixed-scale bars compare the specified values; they do not claim this vector is an extremal allocation unless the proof establishes it.')
 if kind in ['pairs','tuples','maxmin','average','strict-average'] and cert['k']<=16:
  n,k=cert['n'],cert['k'];q,r=divmod(n,k);vals=[q+(i<r) for i in range(k)]
  return model('balanced-bin-witness',[frame(occupancy(vals,f'Balanced allocation: {n} objects into {k} bins'),f'One feasible balanced vector: {r} bins have {q+1}, the others have {q}. This witness helps check sharpness; the written proof establishes the general bound.',values=vals)],'Check the total and the floor/ceiling occupancies. The existence of this example is separate from the proof that another distribution cannot improve the claimed extremum.','This is an explicitly labeled construction, not a display of every possible allocation.')
 if kind in ['lis','lis-contiguous']:
  vals=cert['values'];inc=[];dec=[];frames=[]
  for i,v in enumerate(vals):
   inc.append(1+max([inc[j] for j in range(i) if vals[j]<v],default=0));dec.append(1+max([dec[j] for j in range(i) if vals[j]>v],default=0))
   frames.append(frame(strip(vals,i,'Monotone ending-length labels'),f'At index {i}, the increasing ending length is {inc[-1]} and decreasing ending length is {dec[-1]}. Only earlier eligible values enter the maxima.',increasing=inc[:],decreasing=dec[:]))
  return model('monotone-subsequence',frames,'Use ending-length labels, not contiguous runs. Each predecessor must have an earlier index and the required strict value comparison.','The exact sequence from the question is used; equal values never form a strict extension.')
 if kind in ['prefix','no-prefix']:
  a=cert['values'];m=cert['m'];p=[0]
  for v in a:p.append((p[-1]+v)%m)
  return model('prefix-residues',[frame(strip(p,title=f'Prefix sums modulo {m}, including prefix zero'),'Equal prefix residues identify a divisible segment by subtraction; do not add their values.',values=p)],'Prefix zero is an object too. A collision at indices i<j corresponds to the original slice [i,j).','The displayed prefixes are computed from the actual question sequence.')
def symmetric_space(q):
 if 'symmetric' not in q['text'].lower() or 'trace zero' not in q['text'].lower():return
 m=next((re.fullmatch(r'n=(\d+)',f) for f in q['formulas'] if re.fullmatch(r'n=(\d+)',f)),None);n=int(m[1]) if m else 4
 if n>8:return
 A=[[f'a{min(i,j)+1},{max(i,j)+1}' for j in range(n)] for i in range(n)]
 return model('symmetric-coordinate-chart',[frame(matrix_picture(A),'Mirrored cells carry the same parameter. Only the upper triangle and diagonal are independent before imposing trace zero.')],'Count one parameter for each mirrored pair, then impose the single independent diagonal-sum equation.','The numeric size is the question’s n when specified; otherwise a labeled four-by-four illustration of the general symmetry constraint.')
def growth_picture(cert):
 kind=cert['kind'];m=cert['m'];c=cert.get('c0',1 if kind=='doubling' else cert.get('h',1));g=cert.get('g',2);caps=[c];copied=0;frames=[]
 while c<m:
  copied+=c;c=c+cert['h'] if kind=='additive' else c*g;caps.append(c)
 for i in range(len(caps)):
  visible=caps[:i+1];s=tx(380,35,f'Append target {m}; capacity at each allocation',21,cls='prose-label')+line(60,285,710,285);maxc=max(caps)
  for j,v in enumerate(visible):x=80+j*610/len(caps);h=190*v/maxc;s+=rect(x,285-h,min(60,450/len(caps)),h,'#bddfcd')+tx(x+min(60,450/len(caps))/2,265-h,v,18)
  cost=sum(caps[:i]);s+=tx(380,325,f'Old-slot copies so far: {cost}',20,cls='prose-label');frames.append(frame(svg(s,'Exact capacity and copy accounting'),f'Allocation {i}: capacity {caps[i]}. Prior full buffers contributed {cost} old-slot copies. New-element writes are separate.',capacities=visible,copies=cost))
 assert frames[-1]['copies']==copied
 return model('capacity-growth-accounting',frames,'Follow actual capacity jumps. The copied old slots form the sum of earlier full capacities; the last capacity need not equal the append count.','The exact question parameters are used; allocation time and new-value writes are excluded from the displayed copy counter.')
def make(q,topic):
 # Alternatives are not given input data. Restrict extracted objects to the
 # statement and the worked derivation before inspecting mathematical labels.
 original=q;q=dict(q);body=q['html'];stmt=body.split('<details')[0];stmt=re.split(r'<(?:ol|div) class="exam-options"',stmt)[0];sol=re.search(r'<details[\s\S]*?</details>',body)
 q['formulas']=[html.unescape(f) for f in re.findall(r'<math\b[^>]*aria-label="([^"]*)"',stmt+(sol[0] if sol else ''))]
 raw=sources.get((topic,norm(q['title'])),{});cert=raw.get('certificate') or raw.get('check') or {};kind=cert.get('kind');data=cert.get('data',{})
 if topic in ['d_logic','g_boolean']:
  p=canonical_rows(q)
  if p:return p
 if topic in ['l_gauss','l_rank'] and cert.get('input'):
  n=len(cert['input'][0])-(topic=='l_gauss');frames,result=gauss(cert['input'],n);expected=cert.get('rref')
  if expected:assert result==[[str(F(v)) for v in row] for row in expected],q['title']
  return model('exact-row-reduction',frames,'Follow the highlighted row through each legal operation. Coefficient pivots and any augmented column keep their original meanings.','Exact rational arithmetic. The row-operation sequence may differ from the written solution but its reduced matrix is independently checked against the chapter certificate.')
 if topic=='g_kmap' and kind=='cover':return kmap(data)
 if topic=='g_combin' and kind=='cofactor':return mux(data,raw['stem'])
 if topic=='g_combin' and kind=='miter':return circuit_models((tx,line,svg,frame,model),data)
 if topic=='g_combin' and kind=='word':return word_model((tx,line,svg,frame,model),data)
 if topic=='g_combin' and kind=='tree':return arrival_model((tx,line,svg,frame,model),data)
 if topic=='g_combin' and kind=='contract':return truth_model(data,kind)
 if topic=='p_arrays' and kind=='move':return arrays_move(data)
 if topic in ['p_functions','p_arrays']:
  p=programming((strip,frame,model),topic,cert,raw)
  if p:return p
 if topic=='a_arrays' and kind in ['growth','doubling','additive','growthcompound']:return growth_picture(cert)
 if topic=='d_inclusion':
  p=inclusion_model(cert)
  if p:return p
 if topic=='d_pigeonhole':
  p=pigeon_model(cert)
  if p:return p
 if topic in ['l_vectors','l_matrices']:
  p=symmetric_space(q)
  if p:return p
 if topic.startswith('s_'):
  p=probability_model(q,topic)
  if p:return p
 if topic in ['d_logic','d_relations','d_functions','d_invariants','d_proof']:
  p=relation_model(q)
  if p:return p
 if topic in ['a_model','a_loop','a_correct','a_divide','p_types','p_flow','p_functions','p_arrays','a_arrays']:
  p=array_objects(q)
  if p:return p
 p=matrix_formula(q)
 if p:return p
 return formula_inspection(q)
def run():
 results=[];models={};counts=collections.Counter()
 for row in rows:
  qs=[]
  for q in row['questions']:
   m=make(q,row['topicId']);reason='Complete symbolic or conceptual reasoning; no numeric/geometric state is inferred from unstated data.'
   if m:models[q['id']]=m;counts[m['kind']]+=1;reason=m['reading']
   elif q['existingFigures']:reason='Existing question-specific visual retained and included in the chapter browser audit.'
   qs.append(dict(id=q['id'],number=q['number'],title=q['title'],visual=m['kind'] if m else 'retained' if q['existingFigures'] else 'written-reasoning',reviewReason=reason,frameCount=len(m['frames']) if m else 0))
  results.append(dict(topicId=row['topicId'],questionCount=len(qs),questions=qs))
 (O/'problem-models.json').write_text(json.dumps(models,ensure_ascii=True,separators=(',',':'))+'\n')
 (O/'problem-review.json').write_text(json.dumps(dict(state='implementation_pending_browser_review',chapters=results,counts=dict(counts)),indent=2)+'\n')
 (D/'problem-visual-models.json').write_text(json.dumps(models,ensure_ascii=True,separators=(',',':'))+'\n')
 print(dict(reviewed=sum(len(r['questions']) for r in results),visualProblems=len(models),frames=sum(len(m['frames']) for m in models.values()),kinds=dict(counts)))
if __name__=='__main__':run()
