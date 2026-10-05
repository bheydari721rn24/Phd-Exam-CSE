"""Inclusion-specific SVG state models, each with its own mathematical contract."""
from pathlib import Path
from itertools import permutations,product,combinations
from math import comb,factorial
from html import escape
import json,sys
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.SYMBOLS.update(supseteq='⊇',varnothing='∅')
from mathml import render
M=[]
def text(x,y,s,size=19,anchor='middle',color='#253d50',math=False):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}"'+(' class="math-label"' if math else '')+'>'+escape(str(s))+'</text>'
def rect(x,y,w,h,fill='#e9f2f7',stroke='#7395a8'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}"/>'
def line(x,y,u,v,color='#7c9aab',width=2):return f'<path d="M{x},{y} L{u},{v}" fill="none" stroke="{color}" stroke-width="{width}"/>'
def token(x,y,s,id,fill='#c4e8d8',radius=18):return f'<g data-entity="{id}"><circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="#598799"/>'+text(x,y+6,s,17,math=True)+'</g>'
def frame(d,caption,formula,state):return dict(drawing=d,caption=caption,formula=formula,state=state)
def model(id,title,family,invariant,frames):
 for f in frames:
  assert len(f['caption'].split())>=13
  f['svg']=f'<svg viewBox="0 0 760 400" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'+f.pop('drawing')+'</svg>'
  f['formulaHtml']=render(f.pop('formula'),True)
 M.append(dict(id=id,title=title,kind=family,invariant=invariant,frames=frames))

# Region geometry really represents each membership mask.
atoms=[22,22,18,8,15,6,5,4];points={0:(625,315),1:(245,140),2:(485,140),3:(365,90),4:(365,335),5:(280,225),6:(450,225),7:(365,180)}
frames=[]
for r in [0,1,2,3]:
 d=text(380,27,'Exact membership regions: count only the selected multiplicity')
 for x,y,name in [(300,150,'A'),(430,150,'B'),(365,245,'C')]:d+=f'<circle cx="{x}" cy="{y}" r="110" fill="none" stroke="#6e95a9" stroke-width="2"/>'
 d+=text(230,75,'A',20,math=True)+text(500,75,'B',20,math=True)+text(365,380,'C',20,math=True)
 for mask,(x,y) in points.items():d+=token(x,y,atoms[mask],f'atom{mask}','#ffd894' if mask.bit_count()==r else '#e9f2f7')
 count=sum(a for mask,a in enumerate(atoms) if mask.bit_count()==r)
 d+=text(650,100,'Selected count')+text(650,135,count,28,math=True)+text(650,175,f'exactly {r} events',16)
 frames.append(frame(d,f'Highlight every disjoint region with exactly {r} memberships. Add its own size, not the inclusive intersections that also contain other regions.',rf'N_{{{r}}}={count}',dict(atoms=atoms,r=r,count=count)))
model('di-atoms','Three-set exact regions','venn-atoms','Eight disjoint atoms total 100; circles represent the membership mask of every displayed region.',frames)

frames=[];running=0
for j in range(0,5):
 if j:running+=(-1)**(j+1)*comb(4,j)
 d=text(380,28,'One object in four events: cancel its repeated representations')+line(90,220,700,220)
 for k in range(1,5):
  val=(-1)**(k+1)*comb(4,k);h=abs(val)*18;y=220-h if val>0 else 220
  d+=rect(100+(k-1)*140,y,70,h,'#c4e8d8' if k<=j and val>0 else '#ffd7c2' if k<=j else '#eff3f6')+text(135+(k-1)*140,350,f'order {k}',16)+text(135+(k-1)*140,375,f'{val:+d} copies',16)
 if j:d+=token(135+(j-1)*140,75,'x','object')
 d+=text(380,115,f'After order {j}: net coefficient {running}',20)
 frames.append(frame(d,'The bars count how many specified intersections contain the same object. Each order changes its net coefficient; only the full alternating sum leaves one copy.',rf'\sum_{{k=1}}^{{{j}}}(-1)^{{k+1}}\binom4k={running}',dict(r=4,j=j,coefficient=running)))
model('di-cancel','Per-object binomial cancellation','signed-multiplicity-bars','The coefficient after j orders is the signed binomial partial sum for one object in four events.',frames)

frames=[];G=[20,10,9,4,8,3,2,1];a=G[:]
for step in range(4):
 if step:
  bit=step-1
  for mask in range(8):
   if not mask&(1<<bit):a[mask]-=a[mask|(1<<bit)]
 d=text(380,28,'Inclusive table becomes exact atoms by deleting extra memberships')
 for mask,v in enumerate(a):
  x=90+(mask%4)*175;y=105+(mask//4)*145
  d+=rect(x-55,y-34,110,70,'#c4e8d8' if step==3 else '#e9f2f7')+text(x,y-46,format(mask,'03b'),18,math=True)+text(x,y+11,v,27,math=True)
  if step and not mask&(1<<(step-1)):d+=text(x,y+67,'superset subtracted',13)
 d+=text(380,365,'Start: inclusive counts' if step==0 else f'Completed bit {step-1}; processed absence constraints enforced',18)
 frames.append(frame(d,'Each subtraction removes outcomes with an additional membership at the current bit. Entries containing that bit remain available as the superset values for this stage.',r'F(J)=\sum_{K\supseteq J}(-1)^{|K|-|J|}G(K)',dict(step=step,counts=a[:])))
model('di-atom-transform','Bitwise exact-atom reconstruction','subset-table-transform','Each stage excludes one more outside bit; the final nonnegative vector reconstructs the original inclusive table.',frames)

frames=[];S=[50,70,40,10,1];N=[None]*5
for r in range(4,-1,-1):
 N[r]=S[r]-sum(comb(t,r)*N[t] for t in range(r+1,5))
 d=text(380,28,'Solve the intersection-sum system from the largest multiplicity')
 for k in range(5):
  x=80+k*145;d+=text(x,90,f'S{k} = {S[k]}',20,math=True)+line(x,110,x,210)+rect(x-48,220,96,62,'#ffd894' if k==r else '#c4e8d8' if N[k] is not None else '#eff3f6')+text(x,260,'?' if N[k] is None else N[k],25,math=True)+text(x,310,f'N{k}',20,math=True)
 d+=text(380,365,f'New exact count N{r} = {N[r]}; higher counts already known',19)
 frames.append(frame(d,'Use the current equation only after all higher multiplicities have been recovered. Subtract their binomial-weighted contributions to obtain the one remaining exact count.',rf'N_{{{r}}}=S_{{{r}}}-\sum_{{t={r+1}}}^4\binom t{{{r}}}N_t={N[r]}',dict(S=S,r=r,N=N[:])))
model('di-inverse','Descending multiplicity inversion','triangular-inversion','The known higher counts contribute binomial multiples; after five steps the counts sum to 50.',frames)

frames=[]
for k,T in enumerate([0,150,90,105],0):
 d=text(380,28,'Bonferroni: bound direction follows the truncation parity')+line(100,185,700,185,width=3)
 for val in [0,50,90,105,150,200]:x=100+val*3;d+=line(x,180,x,193)+text(x,220,val,16,math=True)
 if k:d+=token(100+T*3,145,str(T),'bound','#ffd894')
 lo=90 if k>=2 else 0;hi=105 if k==3 else 150 if k else 200
 d+=rect(100+lo*3,250,(hi-lo)*3,30,'#c4e8d8')+text(380,320,f'Certified union interval: [{lo}, {hi}]')
 frames.append(frame(d,'Add the next intersection order and retain the certified bounds. Even truncations bound from below and odd truncations from above; unknown orders prevent an exact claim.',rf'T_{{{k}}}={T}',dict(k=k,S=[200,150,60,15],T=T,lower=lo,upper=hi)))
model('di-bounds','Alternating certified bounds','interval-bounds','Orders one and three give upper bounds; order two gives a lower bound. The current interval never asserts an unproved attainable endpoint.',frames)

frames=[];digits=[1,2,3,1];colors=['#c4e8d8','#ffd894','#c9ddf4']
for omit in [[],[3],[2,3],[1,2,3]]:
 d=text(380,28,'Missing output labels shrink the choices for every input')
 for i in range(4):d+=token(95,100+i*70,i+1,'input'+str(i))+text(55,105+i*70,'input',14)
 for j in range(1,4):
  y=110+(j-1)*95;d+=rect(530,y-25,140,50,'#f5c9c3' if j in omit else '#c4e8d8')+text(600,y+6,f'label {j}',20,math=True)
  if j not in omit:
   for i in range(4):d+=line(115,100+i*70,530,y,'#b7cbd5',1)
 d+=text(380,365,f'Excluded labels: {omit}; unrestricted surviving maps: {(3-len(omit))**4}',19)
 frames.append(frame(d,'Removing a specified output label removes it from every input alphabet. Remaining arrows show all permitted choices, not one selected map or an assumption that every remaining label is used.',rf'|A_I|=(3-|I|)^4={(3-len(omit))**4}',dict(n=4,m=3,omitted=omit,count=(3-len(omit))**4)))
model('di-missing','Surjections through missing-label events','function-choice-bipartite','A specified omission set leaves exactly (3-|I|)^4 functions; the outputs remain labeled.',frames)

frames=[]
for p in [(0,1,2,3),(1,0,3,2),(1,2,3,0),(0,2,3,1)]:
 fixed=[i for i,x in enumerate(p) if i==x];d=text(380,28,'A permutation has one arrow at every input and every output')
 for i in range(4):
  x=145+i*150;d+=token(x,110,i+1,'in'+str(i),radius=21)+token(x,295,i+1,'out'+str(i),radius=21)+text(x,70,'position',14)+text(x,345,'label',14)
 for i,v in enumerate(p):d+=line(145+i*150,131,145+v*150,273,'#b05b55' if i==v else '#3b927b',3)
 d+=text(380,385,'Fixed positions: '+str([i+1 for i in fixed])+'; derangement: '+str(not fixed),18)
 frames.append(frame(d,'Follow each actual assignment arrow. A vertical self-label assignment is fixed and fails a full derangement restriction; cycles of length two or more move every participating label.',r'\pi(i)\ne i\quad\text{for every }i',dict(permutation=list(p),fixed=fixed,derangement=not fixed)))
model('di-derange','Actual permutation arrows and fixed points','permutation-arrows','Every frame is a bijection; fixed-point status comes from its exact assignments, not from color alone.',frames)

frames=[]
for forced in [[],[0],[0,2],[0,1,2],[0,1,2,3]]:
 d=text(380,28,'A specified fixed-point intersection permits other fixed points')
 for i in range(4):
  x=145+i*150;d+=token(x,100,i+1,'top'+str(i))+token(x,260,i+1,'bottom'+str(i))
  if i in forced:d+=line(x,120,x,240,'#b47c27',3)
  else:
   for j in range(4):
    if j not in forced:d+=line(x,120,145+j*150,240,'#bdd0da',1)
 d+=text(380,335,f'Forced fixed positions: {[i+1 for i in forced]}')+text(380,375,f'{factorial(4-len(forced))} completions of the remaining bijection')
 frames.append(frame(d,'Fix the specified positions and remove their labels from all other choices. The remaining assignments may have additional fixed points; this is an inclusive intersection, not an exact fixed set.',rf'|A_I|=(4-|I|)!={factorial(4-len(forced))}',dict(n=4,forced=forced,count=factorial(4-len(forced)))))
model('di-fixed-intersection','Fixed-point intersections versus exact fixed sets','forced-bijection','Forced positions and labels are removed together; remaining completions count all bijections, including further fixed points.',frames)

board=[(0,0),(0,1),(1,0)];frames=[]
for selected in [[],[(0,0)],[(0,1)],[(0,0),(0,1)],[(0,1),(1,0)]]:
 valid=len({r for r,c in selected})==len(selected) and len({c for r,c in selected})==len(selected)
 d=text(380,28,'Forbidden cells: only nonattacking selections have an intersection')
 for r in range(4):
  for c in range(4):
   x=190+c*73;y=75+r*65;d+=rect(x,y,65,56,'#f6d0c4' if (r,c) in board else '#f4f8fb')
   if (r,c) not in selected:d+=text(x+32,y+35,f'{r+1},{c+1}',15,math=True)
 for i,(r,c) in enumerate(selected):d+=token(222+c*73,103+r*65,'R','rook'+str(i),'#ffd894',18)
 count=factorial(4-len(selected)) if valid else 0;d+=text(630,125,'Compatible' if valid else 'Row conflict',19)+text(630,165,f'{count} completions',20,math=True)
 frames.append(frame(d,'Place the selected forbidden assignments as rooks. Shared rows or columns force contradictory assignments and have zero completions; nonattacking selections leave a smaller unconstrained permutation.',rf'|A_I|={count}',dict(n=4,selected=[list(p) for p in selected],compatible=valid,count=count)))
model('di-rooks','Forbidden-cell intersections on a real board','rook-board','Each selected cell is a forced assignment; repeated row or column means an empty event intersection.',frames)

frames=[]
for selected in [[],[0],[1],[2],[0,1]]:
 thresholds=[3,4,5];shift=sum(thresholds[i] for i in selected);res=5-shift;count=comb(res+2,2) if res>=0 else 0
 d=text(380,28,'Upper violations translate into residual token counts')
 for i,cap in enumerate([2,3,4]):
  x=80+i*230;d+=rect(x,110,165,135,'#ffd894' if i in selected else '#e9f2f7')+text(x+82,95,f'box {i+1}',18)+text(x+82,145,f'cap {cap}',18,math=True)
  for j in range(thresholds[i]):d+=token(x+25+j*27,205,j+1,'box'+str(i)+'t'+str(j),'#f5ca90' if i in selected else '#c4e8d8',11)
 d+=text(380,295,f'Violation threshold sum = {shift}; residual total = {res}',20)+text(380,345,f'{count} nonnegative residual vectors',21)
 frames.append(frame(d,'Every selected violation commits its first forbidden occupancy, cap plus one. Subtract those committed tokens; a negative remaining budget proves that intersection empty rather than using a negative binomial argument.',rf'H_3(5-{shift})={count}',dict(total=5,caps=[2,3,4],selected=selected,shift=shift,residual=res,count=count)))
model('di-caps','Cap-plus-one shifts for unequal boxes','occupancy-shift','Committed thresholds are 3, 4 and 5; residual stars-and-bars counts are zero for a negative budget.',frames)

frames=[]
for selected in [[4],[6],[4,6]]:
 div=1
 from math import lcm
 for k in selected:div=lcm(div,k)
 vals=[x for x in range(1,25) if x%div==0];d=text(380,28,'Divisibility intersections use the least common multiple')
 for x in range(1,25):
  cx=80+(x-1)%8*85;cy=115+(x-1)//8*83;d+=token(cx,cy,x,'number'+str(x),'#ffd894' if x in vals else '#e9f2f7',23)
 d+=text(380,350,f'Selected divisors {selected}; lcm = {div}; qualifying values {vals}',19)
 frames.append(frame(d,'Intersect the selected divisor properties on the same integer universe. The highlighted values are exactly multiples of their least common multiple; shared prime factors are never multiplied twice.',rf'|A_I|=\lfloor24/{div}\rfloor={len(vals)}',dict(L=1,H=24,divisors=selected,lcm=div,values=vals)))
model('di-sieve','Arithmetic sieve with actual multiples','integer-sieve','The highlighted integers satisfy every selected divisor condition; the intersection denominator is the lcm.',frames)

frames=[]
for stage in range(3):
 d=text(380,28,'Nonuniform weights stay attached to their exact regions')
 labels=['outside','only A','only B','both'];weights=[1,2,3,4]
 for i,(label,w) in enumerate(zip(labels,weights)):
  x=80+i*175;d+=text(x+55,90,label,18)+rect(x,110,110,170)
  for j in range(w):d+=token(x+30+(j%2)*50,150+(j//2)*65,'1/10','w'+str(i)+'_'+str(j),radius=20)
 d+=text(380,330,['P(A) = 6/10; P(B) = 7/10','Union: 6/10 + 7/10 - 4/10 = 9/10','Condition on B: preserve weights and normalize by 7/10'][stage],19)
 frames.append(frame(d,'Each token has the same tenth-unit weight, but regions contain different total masses. Select the union or conditioning region without pretending the four region labels are equally likely.',[r'P(A)=6/10,\;P(B)=7/10',r'P(A\cup B)=9/10',r'P(A\mid B)=4/7'][stage],dict(weights=weights,stage=stage,union='9/10',conditional='4/7')))
model('di-weights','Weighted union and conditional normalization','probability-mass-regions','Ten tenth-unit masses total one; union and conditional weights come from exact region masses.',frames)

# Incompatible edges contrasted with an actual concatenating path.
frames=[]
for edges in [[],[(0,1)],[(0,1),(1,2)],[(0,1),(0,2)],[(0,1),(1,0)]]:
 indeg=[0]*4;out=[0]*4
 for u,v in edges:out[u]+=1;indeg[v]+=1
 compatible=max(indeg+out)<=1 and not ((0,1) in edges and (1,0) in edges)
 d=text(380,28,'Directed adjacency: paths contract, forks and cycles do not')
 for i in range(4):d+=token(150+i*150,175,i+1,'vertex'+str(i),radius=26)
 for u,v in edges:
  x=150+u*150;y=150+v*150;d+=line(x,135,y,135,'#7d9da8',3)+f'<path d="M{y-9 if y>x else y+9},129 L{y},135 L{y-9 if y>x else y+9},141" fill="none" stroke="#7d9da8" stroke-width="2"/>'
 count=factorial(4-len(edges)) if compatible else 0;d+=text(380,290,'Compatible path blocks' if compatible else 'Incompatible linear constraints',21)+text(380,340,f'{count} arrangements',23,math=True)
 frames.append(frame(d,'Check actual predecessor and successor requirements before contracting edges. A directed path can form one block; a fork assigns two successors and a directed cycle cannot occur in a linear row.',rf'|A_I|={count}',dict(n=4,edges=[list(e) for e in edges],compatible=compatible,count=count)))
model('di-adjacency','Adjacency path compatibility','directed-block-graph','Linear arrangements permit path components with at most one predecessor and successor; cycles are excluded.',frames)

groups={'atoms':['di-atoms'],'cancellation':['di-cancel'],'inversion':['di-inverse'],'bounds':['di-bounds'],'onto':['di-missing'],'derangements':['di-derange','di-fixed-intersection'],'rook':['di-rooks','di-adjacency'],'caps':['di-caps'],'sieve':['di-sieve'],'weights':['di-weights'],'transform':['di-atom-transform']}
(R/'dist/chapters/d_inclusion-models.json').write_text(json.dumps(dict(topicId='d_inclusion',models=M,groups=groups),indent=2)+'\n')
(B/'d_inclusion-model-audit.json').write_text(json.dumps(dict(topicId='d_inclusion',state='constructed_pending_independent_checks',models=len(M),checkpoints=sum(len(m['frames']) for m in M),contracts=[dict(id=m['id'],family=m['kind'],invariant=m['invariant'],checkpoints=len(m['frames'])) for m in M]),indent=2)+'\n')
print('Built',len(M),'independent subject displays and',sum(len(m['frames']) for m in M),'checkpoints.')
