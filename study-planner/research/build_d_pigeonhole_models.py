"""Subject-specific witnesses; shared transport does not define their geometry."""
from pathlib import Path
from itertools import combinations
from math import comb,cos,sin,pi,sqrt
from html import escape
import json,sys
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.SYMBOLS.update(Longrightarrow='⇒')
from mathml import render
M=[]
def text(x,y,s,size=18,anchor='middle',color='#253d50',math=False):
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}"'+(' class="math-label"' if math else '')+'>'+escape(str(s))+'</text>'
def rect(x,y,w,h,fill='#e9f2f7',stroke='#7395a8'):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}"/>'
def line(x,y,u,v,color='#7c9aab',width=2):return f'<path d="M{x},{y} L{u},{v}" fill="none" stroke="{color}" stroke-width="{width}"/>'
def token(x,y,s,id,fill='#c4e8d8',radius=17):return f'<g data-entity="{id}"><circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="#598799"/>'+text(x,y+6,s,16,math=True)+'</g>'
def arrow(x,y,u,v,color='#7298a6'):
 dx=u-x;dy=v-y;h=sqrt(dx*dx+dy*dy);dx/=h;dy/=h
 a=x+24*dx;b=y+24*dy;tipx=u-24*dx;tipy=v-24*dy;backx=tipx-9*dx;backy=tipy-9*dy
 return line(a,b,tipx,tipy,color)+f'<polygon points="{tipx},{tipy} {backx-4*dy},{backy+4*dx} {backx+4*dy},{backy-4*dx}" fill="{color}"/>'
def frame(d,caption,formula,state):return dict(drawing=d,caption=caption,formula=formula,state=state)
def model(id,title,family,invariant,frames):
 for f in frames:
  assert len(f['caption'].split())>=13
  f['svg']=f'<svg viewBox="0 0 760 400" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'+f.pop('drawing')+'</svg>'
  f['formulaHtml']=render(f.pop('formula'),True)
 M.append(dict(id=id,title=title,kind=family,invariant=invariant,frames=frames))

# Distinct requests move from the unassigned row into actual fibers.
frames=[];dest=[0,1,2,3,4,0,1]
for n in range(8):
 d=text(380,28,'Seven indexed requests; five available server labels');used=[0]*5
 for i in range(5):d+=rect(55+140*i,145,115,180)+text(112+140*i,125,'server '+str(i+1),16)
 for i in range(7):
  if i<n:j=dest[i];x=90+140*j+(used[j]%2)*43;y=180+(used[j]//2)*47;used[j]+=1
  else:x=125+85*i;y=75
  d+=token(x,y,i+1,'request'+str(i))
 d+=text(380,365,f'Assigned {n}; occupancies {used}; first repeat at request 6',17)
 frames.append(frame(d,'Each request has one server label. Follow the same numbered object into its fiber; a repeated label keeps the two requests distinct.',rf'\sum_{{i=1}}^5 x_i={n}',dict(n=n,dest=dest,occupancies=used)))
model('dp-placement','Total assignment into actual fibers','object-to-bin-map','Assigned objects occur once each; bin sizes sum to the assigned total.',frames)

frames=[]
for vals in [[11,0,0,0,0],[7,1,1,1,1],[5,2,2,1,1],[3,2,2,2,2]]:
 d=text(380,28,'Integer occupancies balance around the same fixed mean')
 for i,v in enumerate(vals):
  x=80+i*140;d+=rect(x,315-v*19,75,v*19,'#c4e8d8')+text(x+37,345,'bin '+str(i+1),16)+text(x+37,295-v*19,v,20,math=True)
 d+=line(60,315-2.2*19,700,315-2.2*19,'#c98361')+text(620,205,'mean = 11/5',16)
 frames.append(frame(d,'The total stays eleven while transfers reduce the maximum. The mean line is nonintegral, so some integer bin lies above it and some below.',r'\max_i x_i\ge3,\quad\min_i x_i\le2',dict(occupancies=vals,total=11)))
model('dp-average','A fixed mean and integer rounding','occupancy-bars','Every checkpoint totals eleven; the final maximum is three and minimum two.',frames)

frames=[]
for vals in [[0,0,0],[2,3,3],[2,4,3],[2,3,9],[2,4,9]]:
 d=text(380,28,'Finite stock: distinguish any-color and specified-blue targets')
 for i,(v,cap,name) in enumerate(zip(vals,[2,7,9],['red','blue','green'])):
  x=90+225*i;d+=rect(x,75,165,245)+text(x+82,55,name+' stock '+str(cap),16)
  for j in range(cap):d+=token(x+37+(j%3)*45,115+(j//3)*67,j+1,'stock'+str(i)+'_'+str(j),'#ffd894' if j<v else '#eff4f7')
  d+=text(x+82,350,'selected '+str(v),17)
 total=sum(vals);d+=text(380,385,f'Total {total}; any four: {max(vals)>=4}; blue four: {vals[1]>=4}',17)
 frames.append(frame(d,'The numbered stock items show feasible avoidance directly. Eight draws can avoid every four-fold color; fourteen can still avoid four blue despite a large green count.',rf'N={total},\quad x_2={vals[1]}',dict(stocks=[2,7,9],occupancies=vals)))
model('dp-capacity','Inventory avoidance and a specified target','finite-stock-selection','No occupancy exceeds its stock; selected items remain distinct physical objects.',frames)

frames=[]
for vals in [[5,1,0],[4,1,1],[3,2,1],[2,2,2]]:
 d=text(380,28,'A transfer removes actual equal-label pairs');P=sum(comb(v,2) for v in vals)
 for i,v in enumerate(vals):
  cx=150+230*i;d+=rect(cx-80,70,160,235)+text(cx,335,'fiber '+str(i+1),17);points=[(cx-43+(j%2)*85,110+(j//2)*70) for j in range(v)]
  for a,b in combinations(points,2):d+=line(*a,*b,'#caa36f',1)
  for j,(x,y) in enumerate(points):d+=token(x,y,j+1,'pair'+str(i)+'_'+str(j))
  d+=text(cx,365,str(comb(v,2))+' pairs',18)
 frames.append(frame(d,'Every connecting segment is an unordered pair within one fiber. Compare their total during balancing; cross-fiber object pairs are intentionally absent.',rf'P=\sum_i\binom{{x_i}}2={P}',dict(occupancies=vals,pairs=P)))
model('dp-collisions','Visible pair contributions and exchange','within-fiber-complete-graphs','Each drawn segment joins two objects of one fiber; total segments equal the pair count.',frames)

values=[3,4,2,7,1];pref=[0]
for v in values:pref.append((pref[-1]+v)%5)
frames=[]
for j in range(1,7):
 d=text(380,28,'Prefix residues include the empty prefix at index zero')
 for i in range(6):
  x=100+110*i;d+=text(x,90,'S'+str(i),19,math=True)
  if i<j:d+=token(x,145,pref[i],'prefix'+str(i),'#ffd894' if j==6 and i in [2,5] else '#c4e8d8',23)
  if i: d+=rect(x-35,235,70,55,'#ffd894' if j==6 and i>=3 else '#e9f2f7')+text(x,270,values[i-1],22,math=True)
 if j==6:d+=line(320,180,650,180,'#c78355',3)+text(480,212,'same remainder 2',17)
 d+=text(380,340,'Block positions 3–5: 2 + 7 + 1 = 10' if j==6 else 'Read the next prefix and retain its earliest label position',18)
 frames.append(frame(d,'Each prefix gets a remainder label. The last state links prefix indices two and five and highlights only the intervening three input values.',r'S_5-S_2=10\equiv0\pmod5' if j==6 else rf'j={j-1}',dict(values=values,modulus=5,prefixes=pref[:j],complete=j==6)))
model('dp-prefix','Construct the contiguous divisible block','prefix-index-strip','Prefixes are canonical remainders; equal prefixes delimit a nonempty ordered block.',frames)

frames=[];rep=[1,11,111,1111]
for k in range(1,5):
 d=text(380,28,'Repunit recurrence modulo six; subtraction preserves the modulus')
 for j in range(k):
  x=120+170*j;d+=rect(x-55,95,110,110)+text(x,135,rep[j],21,math=True)+text(x,180,'remainder '+str(rep[j]%6),15)
 if k==4:d+=line(120,230,630,230,'#c78355',3)+text(380,275,'1111 − 1 = 1110 = 6 × 185',23,math=True)
 d+=text(380,340,'Trailing zeros cannot be canceled modulo six',18)
 frames.append(frame(d,'Track each repunit by its actual remainder. The repeated label at lengths one and four produces a zero-one multiple; it does not produce an all-ones multiple here.',r'R_{j+1}\equiv10R_j+1\pmod6',dict(repunits=rep[:k],modulus=6)))
model('dp-repunit','Decimal difference with trailing zeros','modular-recurrence','All displayed repunits have their computed remainders; the positive difference is divisible by six.',frames)

frames=[];p=7;A={x*x%p for x in range(p)};C={(-1-y*y)%p for y in range(p)}
for stage in range(3):
 d=text(380,28,'Two four-element square images in seven residue labels')
 for j in range(7):
  x=80+100*j;d+=text(x,75,j,21,math=True)+rect(x-35,95,70,170)
  if j in A:d+=token(x,140,'A','sqA'+str(j))
  if stage>=1 and j in C:d+=token(x,220,'B','sqB'+str(j),'#ffd894')
 d+=text(380,315,'A = square residues; B = −1 − square residues',18)
 if stage==2:d+=text(380,365,'Shared residue 4: x = 2, y = 3; 4 + 9 ≡ −1',20,math=True)
 frames.append(frame(d,'The colors retain which image a residue comes from. Four labels from each origin cannot stay disjoint inside seven available labels; the intersection supplies a congruence witness.',r'|A|+|B|=8>7',dict(p=p,A=sorted(A),B=sorted(C),stage=stage)))
model('dp-prime','Overlapping modular images','two-origin-residue-cells','Both images have four elements; shared residues encode the stated square-sum relation.',frames)

frames=[];subsets=[[0,1,3],[0,2,3],[0,1],[2]];vals=[1,2,3,4]
for stage in range(3):
 left,right=([0,1,3],[0,2,3]) if stage==0 else ([0,1],[2]) if stage==1 else ([0,3],[1,2])
 # Stage zero is a candidate pair that must fail: sums seven and eight.
 d=text(380,28,'Check equal sums before canceling common indices')
 for row,S,name in [(0,left,'left subset'),(1,right,'right subset')]:
  y=130+125*row;d+=text(90,y,name,16)
  for j in S:d+=token(235+105*j,y,vals[j],('left' if row==0 else 'right')+str(j),'#ffd894' if j in set(left)&set(right) else '#c4e8d8',24)
  d+=text(685,y,'sum '+str(sum(vals[j] for j in S)),17)
 eq=sum(vals[j] for j in left)==sum(vals[j] for j in right)
 d+=text(380,345,['Unequal candidate: cancellation cannot manufacture equality','Equal disjoint sums: 1 + 2 = 3','A second witness: 1 + 4 = 2 + 3'][stage],19)
 frames.append(frame(d,'The drawing preserves index identities and recalculates both sums. Reject unequal candidates; an equal collision can then have common indices removed without changing the equality.',rf'\sum_{{i\in U}}a_i={sum(vals[j] for j in left)},\quad\sum_{{i\in V}}a_i={sum(vals[j] for j in right)}',dict(values=vals,left=left,right=right,equal=eq)))
# Add a real cancellation pair: {1,2,4} and {3,4} both seven; delete common index 4.
f=frames[0];left=[0,1,3];right=[2,3];d=text(380,28,'Equal sums share index 4: remove it from both sides')
for row,S in enumerate([left,right]):
 for j in S:d+=token(215+110*j,130+125*row,vals[j],('left' if row==0 else 'right')+str(j),'#ffd894' if j==3 else '#c4e8d8',24)
 d+=text(680,130+125*row,'sum 7',18)
d+=text(380,345,'7 − 4 = 7 − 4; residual sums remain 3',20,math=True)
frames[0]=frame(d,'Two distinct index subsets sum to seven and share the value at index four. Remove that same indexed object from both sides to preserve equality and obtain disjoint witnesses.',r'1+2+4=3+4\;\Longrightarrow\;1+2=3',dict(values=vals,left=left,right=right,equal=True))
model('dp-subsets','Equal subset sums and common-index cancellation','indexed-subset-cancellation','Displayed sums are checked from selected indices; deleting the common part preserves equality.',frames)

frames=[];cores=[1,3,5,7,9,11]
for stage in range(4):
 d=text(380,28,'Odd cores partition 1 through 12 into actual divisibility chains')
 for row,core in enumerate(cores):
  y=75+45*row;d+=text(70,y,'core '+str(core),15);x=170;v=core;j=0
  while v<=12:
   if j:d+=line(x-95,y-5,x-23,y-5)
   active=stage>=1 and v in [4,8] or stage>=2 and v in [6,12] or stage>=3 and v in [5,10]
   d+=token(x,y-5,v,'chain'+str(v),'#ffd894' if active else '#c4e8d8',17);x+=115;v*=2;j+=1
 d+=text(380,370,'Equal cores supply powers-of-two quotients',18)
 frames.append(frame(d,'Each integer appears once in the row of its odd part. Highlight two selected nodes in the same row; the connecting chain shows the smaller divides the larger.',r'x=2^a b,\quad y=2^c b',dict(H=12,base=2,cores=cores,stage=stage)))
model('dp-oddchain','Odd-part divisibility chains','multiplicative-chain-graph','Every integer has a unique odd core and successive nodes differ by a factor two.',frames)

frames=[]
for n in [10,11,12]:
 d=text(380,28,'Complement pairs summing to 22, with a singleton fixed point')
 for j in range(10):
  x=85+(j%5)*145;y=120+(j//5)*120;a=j+1;b=22-a
  d+=line(x-20,y,x+35,y)+token(x-20,y,a,'low'+str(j),'#ffd894')+token(x+35,y,b,'high'+str(j),'#ffd894' if n==12 and j==0 else '#e9f2f7')
 d+=token(380,340,11,'fixed',' #ffd894'.strip() if n>=11 else '#e9f2f7')+text(520,347,'11 cannot pair with itself',16)
 frames.append(frame(d,'Distinct selections choose at most one member per two-element complement pair and may additionally choose eleven. The twelfth selection completes an actual pair, rather than doubling the singleton.',rf'N={n},\quad a+b=22',dict(H=21,target=22,total=n)))
model('dp-pairing','Complement matching and its fixed point','involution-pair-matching','Ten disjoint pairs and one singleton cover all twenty-one values.',frames)

frames=[];points=[(200,295),(520,295),(360,18+277),(360,110),(300,190)]
# Equilateral triangle has screen vertices (200,300),(520,300),(360,22.872).
V=[(200,300),(520,300),(360,300-160*sqrt(3))];mid=[((V[i][0]+V[(i+1)%3][0])/2,(V[i][1]+V[(i+1)%3][1])/2) for i in range(3)]
for stage in range(3):
 d=text(380,385,'Four cells of side 1/2; five points force one repeated cell',17)
 d+='<polygon points="'+' '.join(f'{x},{y}' for x,y in V)+'" fill="#f0f7fa" stroke="#6f95aa" stroke-width="2"/>'
 for a,b in combinations(mid,2):d+=line(*a,*b,'#7298a6')
 if stage==0:P=V+[(360,300-160*sqrt(3)/3)]
 else:P=[(230,280),(265,285),(485,280),(360,75),(360,225)]
 for j,(x,y) in enumerate(P[:4 if stage==1 else len(P)]):d+=token(x,y,j+1,'point'+str(j),'#ffd894' if stage==2 and j<2 else '#c4e8d8',13)
 if stage==2:d+=line(*P[0],*P[1],'#c78355',3)
 caption='Three vertices and the centroid avoid distance one-half, giving the four-point lower-bound certificate.' if stage==0 else 'Assign each point to one half-size triangular cell, choosing a fixed cell on shared boundaries; the repeated-cell pair meets the diameter bound.'
 frames.append(frame(d,caption,r'd\le1/2' if stage else r'd_{\min}=1/\sqrt3>1/2',dict(stage=stage,vertices=V,points=P[:4 if stage==1 else len(P)])))
model('dp-triangle','Triangle cells and the sharp four-point obstruction','triangular-partition','The four midpoint cells have side one-half; displayed points retain their true geometric coordinates.',frames)

frames=[];fractions=[(j*sqrt(2))%1 for j in range(6)]
for n in range(1,7):
 d=text(380,28,'Fractional parts of j times √2, in five half-open intervals')
 for j in range(5):d+=rect(75+122*j,115,122,150,'#edf5f7')+text(75+122*j,95,f'{j}/5',16,math=True)
 d+=text(685,95,'1',16,math=True)
 for j,f in enumerate(fractions[:n]):d+=token(75+610*f,155+(j%3)*40,j,'fraction'+str(j),'#ffd894' if n==6 and j in [0,5] else '#c4e8d8',13)
 if n==6:d+=text(380,315,'q = 5, p = 7; |5√2 − 7| ≈ 0.0711 < 0.2',20,math=True)
 frames.append(frame(d,'Horizontal position is the actual fractional part, not an ordinal bin number. Two prefixes sharing a half-open interval produce an integer difference and a strict approximation bound.',r'|q\alpha-p|<1/5',dict(alpha=sqrt(2),fractions=fractions[:n],m=5)))
model('dp-fractional','Dirichlet witness on the fractional unit interval','fractional-coordinate-strip','Coordinates are fractional multiples; intervals have width one-fifth and distinct endpoint ownership.',frames)

frames=[];values=[5,1,4,2,3];L=[];D=[]
for j,v in enumerate(values):L.append(1+max([L[i] for i in range(j) if values[i]<v] or [0]));D.append(1+max([D[i] for i in range(j) if values[i]>v] or [0]))
for n in range(1,6):
 d=text(380,28,'Directed predecessors extend ending-length labels')
 for j in range(n):
  x=90+j*145;y=270-values[j]*27
  for i in range(j):d+=arrow(90+i*145,270-values[i]*27,x,y,'#83ab96' if values[i]<values[j] else '#d3aa7b')
 for j in range(n):
  x=90+j*145;y=270-values[j]*27
  d+=token(x,y,values[j],'seq'+str(j),radius=23)+text(x,325,f'({L[j]}, {D[j]})',19,math=True)
 d+=text(380,375,'Green: increasing extension; amber: decreasing extension',17)
 frames.append(frame(d,'Every arrow comes from an earlier index and compares actual values. Each ending-length label is computed from eligible predecessors, so different positions receive different ordered labels.',rf'\mathrm{{LIS}}={max(L[:n])},\quad\mathrm{{LDS}}={max(D[:n])}',dict(values=values[:n],increasing=L[:n],decreasing=D[:n])))
model('dp-es','Actual sequence dependency graph','ending-length-dag','Every displayed label equals its strict predecessor recurrence; arrows respect index order.',frames)

def graph_drawing(n,edges,highlight=(),title=''):
 P=[(380+145*cos(-pi/2+2*pi*j/n),195+145*sin(-pi/2+2*pi*j/n)) for j in range(n)]
 d=text(380,28,title,18)
 for i,j,color in edges:d+=line(*P[i],*P[j],color,4 if (i,j) in highlight else 2)
 deg=[0]*n
 for i,j,c in edges:deg[i]+=1;deg[j]+=1
 for j,(x,y) in enumerate(P):d+=token(x,y,j+1,'vertex'+str(j),radius=21)
 return d,P,deg
frames=[]
for edges in [[],[(0,1),(1,2)],[(0,j) for j in range(1,5)],list(combinations(range(5),2))]:
 d,P,degs=graph_drawing(5,[(i,j,'#6a9cae') for i,j in edges],title='Simple undirected degrees: 0 and 4 cannot coexist')
 d+=text(380,375,'degrees '+str(degs)+'; repeat: '+str(len(set(degs))<5),18)
 frames.append(frame(d,'Read degrees from actual drawn incident edges. An isolated vertex excludes a universal vertex, leaving too few usable labels for five distinct vertices.',r'|\{\mathrm{deg}(v):v\in V\}|\le4',dict(n=5,edges=edges,degrees=degs)))
model('dp-degree','Degree labels from actual edges','simple-undirected-graph','Degree equals the number of incident neighbors; the two extreme labels never coexist.',frames)

frames=[]
for stage in range(3):
 red={(0,1),(0,2),(0,3)}
 if stage==1:red.add((1,2))
 if stage==2:red|={(0,4),(0,5)}
 edges=[(i,j,'#c47964' if (i,j) in red else '#638fac') for i,j in combinations(range(6),2)]
 tri=[0,1,2] if stage==1 else [1,2,3] if stage==2 else []
 d,P,degs=graph_drawing(6,edges,highlight=list(combinations(tri,2)),title='A same-color star requires a second triangle argument')
 d+=text(380,375,['Three red star edges identified','A red endpoint edge closes a red triangle','All three endpoint edges blue close a blue triangle'][stage],17)
 frames.append(frame(d,'Inspect actual edge colors, then follow one of the two proof branches. A star is not yet a triangle; the endpoint edges determine which triangle can be certified.',r'R(3,3)=6',dict(n=6,red=sorted(red),triangle=tri)))
model('dp-ramsey','Two explicit Ramsey proof branches','edge-colored-complete-graph','Each unordered vertex pair has one color; the selected triangle has three equal-color edges.',frames)

frames=[];rows=[]
for pair in combinations(range(4),2):
 for color in range(3):
  row=[None]*4
  for j in pair:row[j]=color
  for j,c in zip([j for j in range(4) if j not in pair],[c for c in range(3) if c!=color]):row[j]=c
  rows.append(row)
for n in [1,6,12,18,19]:
 a=(rows+[rows[0]])[:n];d=text(380,28,'Pair + color certificates: eighteen avoiding rows, then a repeat')
 for panel in range(2):
  for j in range(4):d+=text(112+panel*350+j*54,53,'col '+str(j+1),13)
 for i,row in enumerate(a):
  x=65+(i//10)*350;y=65+(i%10)*29
  d+=text(x,y+18,i+1,14)
  for j,c in enumerate(row):
   d+=rect(x+25+j*54,y,45,24,['#c4836e','#76a1b6','#8eb897'][c])
   if n==19 and i in [0,18] and j in [0,1]:d+=f'<rect x="{x+25+j*54}" y="{y}" width="45" height="24" rx="5" fill="none" stroke="#2f5d52" stroke-width="3"/>'
  cert=next((j,k,c) for j,k in combinations(range(4),2) for c in range(3) if row[j]==row[k]==c)
  d+=text(x+275,y+18,f'({cert[0]+1},{cert[1]+1};{cert[2]+1})',14,math=True)
 d+=text(380,380,'The nineteenth row repeats the first row’s pair-color certificate',16)
 frames.append(frame(d,'Each avoiding row has exactly one same-color pair and a unique certificate. After all eighteen certificates are used, the next row creates a repeated pair and color.',rf'N={n},\quad\binom42\cdot3=18',dict(rows=a,cols=4,colors=3)))
model('dp-rectangle','Actual colored rows and repeated certificates','colored-matrix-certificate','Each of the first eighteen rows has one distinct pair-color certificate; row nineteen repeats it.',frames)

frames=[]
for depth in [0,1,2,3]:
 d=text(380,28,'A truthful binary decision tree separates possibilities at leaves')
 for level in range(depth+1):
  for j in range(2**level):
   x=60+(j+.5)*640/(2**level);y=70+85*level
   if level:
    px=60+(j//2+.5)*640/(2**(level-1));d+=line(px,y-85,x,y)
   d+=token(x,y,format(j,'0'+str(max(1,level))+'b'),'decision'+str(level)+'_'+str(j),radius=17)
 d+=text(380,375,f'Depth {depth}: at most {2**depth} distinguishable leaves',18)
 frames.append(frame(d,'Each edge contributes one answer bit to the transcript. Count complete root-to-leaf words, not internal nodes; identifying more possibilities needs a larger leaf set.',rf'M\le2^{{{depth}}}={2**depth}',dict(depth=depth,leaves=2**depth)))
model('dp-info','Answer transcripts as actual tree paths','binary-decision-tree','At depth q the full tree has two to q leaves, each with one distinct transcript.',frames)

frames=[];ranks=[1,4,7,10,13];gap=3
for stage in range(4):
 d=text(380,28,'Same-suit rank anchor and a six-permutation gap code')
 for j in range(13):
  a=-pi/2+2*pi*j/13;x=210+125*cos(a);y=205+125*sin(a)
  d+=token(x,y,j+1,'rank'+str(j+1),'#ffd894' if j+1 in [1,4] else '#eef4f7',14)
 d+=text(210,205,'suit cycle',17)+text(545,100,'anchor rank 1 → hidden rank 4',17)
 cards=['A','B','C'];order=['B','A','C'] if stage>=2 else cards
 for i,c in enumerate(order):
  d+=rect(430+95*i,160,75,115)
  if stage>=1:d+=text(468+95*i,223,c,25)
 d+=text(565,310,'code 3: B, A, C' if stage>=2 else 'Agree on total order A < B < C' if stage==1 else 'First select the same-suit pair',17)
 if stage==3:d+=text(565,345,'Decoded hidden card: rank 4',17)
 d+=text(380,380,'Six permutations encode gaps 1–6; suit and anchor supply the rest',16)
 frames.append(frame(d,'Keep the same-suit pair separate from the three permutation cards. Their ordered identities encode one gap; adding it cyclically to the anchor rank recovers the hidden card.',r'3!=6,\quad1+3=4',dict(anchor=1,hidden=4,gap=gap,order=order,stage=stage)))
model('dp-cards','Cyclic card-rank decoding','rank-cycle-permutation-code','Lexicographic permutation rank three is B,A,C; its gap advances rank one to four in the anchor suit.',frames)

groups={'assignment':['dp-placement'],'average':['dp-average'],'capacity':['dp-capacity'],'collisions':['dp-collisions'],'residues':['dp-prefix','dp-repunit','dp-prime'],'subsets':['dp-subsets'],'chains':['dp-pairing','dp-oddchain'],'geometry':['dp-triangle','dp-fractional'],'subsequences':['dp-es'],'graphs':['dp-degree','dp-ramsey','dp-rectangle'],'information':['dp-info','dp-cards']}
(R/'dist/chapters/d_pigeonhole-models.json').write_text(json.dumps(dict(topicId='d_pigeonhole',models=M,groups=groups),indent=2)+'\n',encoding='utf-8')
(B/'d_pigeonhole-model-audit.json').write_text(json.dumps(dict(topicId='d_pigeonhole',state='pending_independent_checks',models=len(M),checkpoints=sum(len(m['frames']) for m in M),contracts=[dict(id=m['id'],family=m['kind'],invariant=m['invariant'],checkpoints=len(m['frames'])) for m in M]),indent=2)+'\n',encoding='utf-8')
print('Built',len(M),'subject-specific models and',sum(len(m['frames']) for m in M),'checkpoints.')
