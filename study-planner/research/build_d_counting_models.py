"""Exact counting-specific diagrams and traces; no legacy chapter rebuild."""
from pathlib import Path
from itertools import combinations,permutations,product
from math import comb,factorial
from html import escape
import json,sys
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
sys.path.insert(0,str(BASE/'exam-rewrite'))
from mathml import render
MODELS=[]
def txt(x,y,s,size=20,color='#233142',anchor='middle'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{color}">{escape(str(s))}</text>'
def edge(x,y,u,v,color='#9bb8c5',wide=2):return f'<path d="M{x},{y} L{u},{v}" stroke="{color}" stroke-width="{wide}" fill="none"/>'
def token(x,y,s,id,color='#e2edf2',radius=22):
    return f'<g data-entity="{id}"><circle cx="{x}" cy="{y}" r="{radius}" fill="{color}" stroke="#557f90"/>{txt(x,y+7,s)}</g>'
def strip(values,y=125,active=(),prefix='v',step=70,start=80):
    return ''.join(token(start+i*step,y,v,prefix+str(i),'#ffdb8d' if i in active else '#e2edf2')+txt(start+i*step,y+49,'slot '+str(i+1),14) for i,v in enumerate(values))
def svg(title,body):
    return f'<svg viewBox="0 0 760 400" role="img" aria-label="{escape(title,quote=True)}"><title>{escape(title)}</title>{body}</svg>'
def model(id,title,kind,invariant,frames):
    assert len(frames)>=2
    for f in frames:
        assert len(f['caption'].split())>=12,(id,f['caption'])
        f['formulaHtml']=render(f.pop('formula'),True)
        f['svg']=svg(title,f.pop('drawing'))
    MODELS.append(dict(id=id,title=title,kind=kind,invariant=invariant,frames=frames))
def f(body,caption,formula,state):return dict(drawing=body,caption=caption,formula=formula,state=state)

# Real branching tree, with prefix-dependent numbers of leaves.
frames=[]
for active in range(5):
    b=txt(380,28,'Choose a weak pair: first i, then j at least i')+token(55,185,'root','root')
    for i in range(1,5):
        yy=100+(i-1)*80;b+=edge(77,185,215,yy,'#b98219' if active==i else '#9bb8c5')+token(235,yy,i,'i'+str(i),'#ffdb8d' if active==i else '#e2edf2')
        for j in range(i,5):
            xx=400+(j-i)*88;leaf_y=yy+((j-i)-(4-i)/2)*23
            b+=edge(257,yy,xx-20,leaf_y)+token(xx,leaf_y,f'{i},{j}','p'+str(i)+str(j),'#bde3d0' if active==i else '#e2edf2',20)
        b+=txt(715,yy+5,str(5-i)+' leaves',16)
    frames.append(f(b,'Inspect each first-value branch. Its permitted second values run from the first value through four, so branch sizes differ.',r'4+3+2+1=10',dict(active=active,n=4,count=10)))
model('dc-tree','Variable branching in a weakly ordered pair','choice-tree','Every legal ordered pair occurs at one leaf; branch counts are 4, 3, 2, and 1.',frames)

frames=[]
for pair in combinations('ABCD',2):
    a,b=pair;body=txt(380,35,'Erase ordering only after checking every fiber')
    body+=strip([a,b],95,prefix='a',start=120)+strip([b,a],195,prefix='b',start=120)
    body+=edge(220,95,430,145)+edge(220,195,430,145)+token(500,145,''.join(pair),'set',radius=35)
    body+=txt(500,225,'one unordered two-subset')+txt(380,340,'Two ordered preimages for every subset')
    frames.append(f(body,'Both orders map to the same two-subset, and no other distinct-symbol ordered pair maps to that subset. This fiber size is uniform.',r'P(4,2)/2!=12/2=6',dict(pair=list(pair),fiber=2,count=6)))
model('dc-fibers','Uniform ordering fibers','fiber-map','Each two-subset of four distinct symbols has exactly two ordered representations.',frames)
frames=[]
for word in ['AAA','AAB','ABB','BBB']:
    pre=sorted(set(''.join(p) for p in permutations(word)));body=txt(380,35,'Repeated values make order-forgetting fibers unequal')
    for j,p in enumerate(pre):body+=txt(150,105+75*j,p,28)+edge(215,98+75*j,470,170)
    body+=token(550,170,word,'multiset',radius=42)+txt(550,252,str(len(pre))+' ordered preimages')
    body+=txt(380,360,'Fibers: 1, 3, 3, 1; total eight words, four multisets')
    frames.append(f(body,'The displayed multiset has exactly these ordered representations. Equal copies erase some permutations, so dividing every fiber by the same factorial fails.',r'\binom{2+3-1}{3}=4',dict(word=word,preimages=pre,fiber=len(pre),count=4)))
model('dc-nonuniform','Nonuniform repeated-value fibers','fiber-map','All eight binary length-three words are partitioned into fibers of sizes 1, 3, 3, and 1.',frames)

frames=[]
for j in [4,5]:
    b=txt(380,35,'Select eight questions; at least four from the first five')
    for i in range(10):b+=token(75+(i%5)*143,110+(i//5)*125,i+1,'q'+str(i),'#ffdb8d' if (i<j if i<5 else i-5<8-j) else '#edf1f4')
    count=comb(5,j)*comb(5,8-j);b+=txt(380,325,str(j)+' from first group; '+str(8-j)+' from second; '+str(count)+' choices')
    frames.append(f(b,'Classify the committee by its exact first-group count. The two feasible category counts are disjoint and together enforce the original at-least restriction.',rf'\binom5{{{j}}}\binom5{{{8-j}}}={count}',dict(first=j,second=8-j,count=count)))
model('dc-selection','Disjoint category counts','category-selection','A selected set has exactly one first-group size; total is 25 plus 10.',frames)

frames=[]
word='ABABC'
for t in range(6):
    used=word[:t];remaining={s:word.count(s)-used.count(s) for s in 'ABC'}
    b=txt(380,30,'Fixed inventory A,A,B,B,C; each symbol choice consumes one copy')+strip(list(word),125,active=range(t),start=170)
    for j,s in enumerate('ABC'):b+=txt(180+200*j,260,s+' remaining: '+str(remaining[s]),23)
    b+=txt(380,345,'Prefix '+(used or '(empty)')+'; completed length '+str(t))
    frames.append(f(b,'The highlighted prefix consumes precisely its symbol multiplicities. Fixed-content completion counts use the remaining inventory, rather than an unlimited alphabet or labeled identical copies.',rf'\frac{{{5-t}!}}{{{remaining["A"]}!{remaining["B"]}!{remaining["C"]}!}}',dict(prefix=used,remaining=remaining,total=5-t)))
model('dc-word','Fixed-content inventory consumption','inventory-strip','At every prefix, used plus remaining multiplicity equals the original inventory for each symbol.',frames)

frames=[]
a=[1,4,6];compressed=[1,3,4]
for t in range(4):
    vals=[compressed[i] if i<t else a[i] for i in range(3)]
    b=txt(380,35,'Compress forbidden interior gaps one selected position at a time')
    for i in range(1,9):b+=token(80+(i-1)*85,105,i,'slot'+str(i),'#bde3d0' if i in a else '#edf1f4')
    for i,v in enumerate(vals):b+=token(80+(v-1)*85,240,i+1,'selected'+str(i),'#ffdb8d')
    b+=txt(380,330,'Original positions 1,4,6; compressed positions 1,3,4')
    frames.append(f(b,'Subtract the number of earlier selected positions from each index. The final positions form an ordinary subset, and adding those offsets reconstructs the separated original positions.',r'b_i=a_i-(i-1),\qquad \binom{8-3+1}{3}=20',dict(original=a,compressed=compressed,processed=t,displayed=vals)))
model('dc-gaps','Position compression for nonadjacent ones','gap-compression','The offset for selected index i is i minus one; final compressed positions are strictly increasing.',frames)

import math
def ring(values,rotation=0):
    b='';n=len(values)
    for i,v in enumerate(values):
        theta=2*math.pi*(i+rotation)/n-math.pi/2;x=380+135*math.cos(theta);y=205+135*math.sin(theta)
        b+=token(round(x,2),round(y,2),v,'bead'+str(i),'#ffdb8d' if v in ('A','1') else '#d8e9f1',25)
    return b
frames=[]
for r in range(4):
    vals='ABCD';b=txt(380,30,'Distinct identities: all four starting seats yield different words')+ring(vals,r)+txt(380,205,'one circular order',18)+txt(380,385,'Reference-seat word: '+vals[-r:]+vals[:-r] if r else 'Reference-seat word: ABCD')
    frames.append(f(b,'Rotate the four distinct identities without changing their clockwise neighbors. Every starting position gives a different linear representative of the same oriented circular arrangement.',r'4!/4=3!=6',dict(word=vals,rotation=r,orbit=4,count=6)))
model('dc-circle','Distinct rotations preserve clockwise order','rotation-orbit','A distinct-symbol circular order has exactly n distinct starting-seat representations.',frames)
frames=[]
for w in ['AABB','ABAB']:
    orbit=sorted(set(w[r:]+w[:r] for r in range(4)))
    for r in range(4):
        b=txt(380,30,'Periodic and nonperiodic words have different rotation orbit sizes')+ring(w,r)+txt(380,204,'orbit size '+str(len(orbit)),19)+txt(380,385,'Distinct seat words: '+', '.join(orbit),18)
        frames.append(f(b,'This rotation preserves the circular color pattern. Compare the number of distinct seat words across patterns before attempting division by the number of seats.',r'(6+0+2+0)/4=2',dict(word=w,rotation=r,orbit=orbit,count=2)))
model('dc-periodic','A periodic word has fewer distinct rotations','rotation-orbit','AABB has orbit size four; ABAB has orbit size two; together they account for all six weight-two words.',frames)

def starbar(values,progress):
    seq=[]
    for i,v in enumerate(values):
        seq+=['*']*v
        if i<len(values)-1:seq+=['|']
    b=txt(380,30,'Bars preserve labeled box boundaries, including an empty box')
    for i,s in enumerate(seq):
        x=140+i*75
        if s=='|':b+=f'<g data-entity="mark{i}">'+edge(x,75,x,140,'#b98219',7)+'</g>'
        else:b+=token(x,106,'','mark'+str(i),'#ffdb8d' if i<progress else '#dceaf1',16)
    cursor=0
    for j,v in enumerate(values):
        x=115+j*240;b+=f'<rect x="{x-80}" y="205" width="160" height="125" rx="8" fill="#f2f7fa" stroke="#93b4c1"/>'+txt(x,355,'box '+str(j+1),19)
        for i in range(v):
            if cursor+i<progress:b+=token(x-40+i*35,262,'','object'+str(j)+'-'+str(i),'#bde3d0',13)
        cursor+=v+1
    return b
frames=[]
for t in range(8):
    b=starbar([2,0,3],t)
    frames.append(f(b,'Read stars between consecutive bars into the corresponding labeled box. Consecutive bars preserve a zero occupancy rather than removing or merging that box.',r'\binom{5+3-1}{3-1}=21',dict(values=[2,0,3],processed=t,count=21)))
model('dc-stars','Stars and bars reconstructs an occupancy vector','star-bar-bijection','Five identical stars and two bars reconstruct the three labeled occupancies 2,0,3.',frames)
frames=[]
for t in [0,1,2]:
    v=[3,2,4] if t==0 else [1,1,4];b=txt(380,30,'Consume compulsory lower-bound units before counting the residual')
    for j,(x,l) in enumerate(zip([3,2,4],[2,1,0])):
        xx=145+j*235;b+=txt(xx,75,'box '+str(j+1),21)
        for i in range(x):
            if t==1 and i<l:continue
            y=150 if t!=1 else 180
            xpos=xx-50+i*34 if t!=1 else xx-30+(i-l)*34
            b+=token(xpos,y,'','s'+str(j)+'-'+str(i),'#ffdb8d' if i<l else '#bde3d0',14)
        b+=txt(xx,235,'lower bound '+str(l),18)+txt(xx,305,'residual '+str(x-l) if t else 'original '+str(x),20)
    frames.append(f(b,'The amber tokens are compulsory. Removing the fixed lower-bound inventory leaves nonnegative residual coordinates, and adding it back reconstructs the original allocation uniquely.',r'y_1=x_1-2,\quad y_2=x_2-1,\quad y_3=x_3',dict(original=[3,2,4],lower=[2,1,0],residual=[1,1,4],phase=t)))
model('dc-lower','Lower-bound translation retains an inverse','allocation-shift','Each coordinate equals its compulsory lower bound plus a nonnegative residual.',frames)

frames=[]
groups=['AB','CD','EF']
for perm in permutations(groups):
    b=txt(380,30,'Group labels change representations; internal order is already erased')
    for j,g in enumerate(perm):
        x=145+j*235;b+=f'<rect x="{x-80}" y="105" width="160" height="175" fill="#edf5f8" stroke="#8cb0bf"/>'+txt(x,85,'label '+str(j+1))
        for i,v in enumerate(g):b+=token(x-32+i*64,185,v,'person'+v,'#bde3d0')
    b+=txt(380,345,'All six labelings represent the same three nonempty groups')
    frames.append(f(b,'Permuting the three nonempty group labels changes the labeled assignment but preserves its unlabeled partition. Every such partition therefore has exactly six labelings.',r'6!/((2!)^3 3!)=15',dict(groups=list(perm),fiber=6,count=15)))
model('dc-groups','Unlabeled nonempty groups have constant label fibers','group-partition','The three disjoint nonempty sets are different contents, so all six label assignments are distinct.',frames)
frames=[]
for phase,g in enumerate([['AB','',''],['A','B','']]):
    b=txt(380,30,'Empty boxes produce different numbers of distinct labelings')
    for j,s in enumerate(g):
        x=145+j*235;b+=f'<rect x="{x-80}" y="100" width="160" height="175" fill="#edf5f8" stroke="#8cb0bf"/>'+txt(x,82,'box '+str(j+1))
        for i,v in enumerate(s):b+=token(x-32+i*64,180,v,'person'+v,'#ffdb8d')
        if not s:b+=txt(x,195,'empty',20)
    fiber=3 if phase==0 else 6;b+=txt(380,335,'Distinct labeled assignments for this partition: '+str(fiber))
    frames.append(f(b,'Compare partitions with both objects together and with the objects separated. The empty-box symmetries differ, so their numbers of distinct labeled representations are unequal.',r'3+6=9,\quad \text{unlabeled outcomes}=2',dict(groups=g,fiber=fiber,count=2)))
model('dc-empty','An empty-box symmetry breaks division','group-partition','The together partition has three labeled realizations; the separated partition has six.',frames)

frames=[]
for r in range(6):
    b=txt(380,28,'Every Pascal entry counts subsets, not merely an arithmetic pattern')
    for n in range(6):
        for k in range(n+1):
            x=380+(k-n/2)*100;y=80+n*51
            if n==r and n>0:
                if k>0:b+=edge(x-50,y-51,x,y,'#b98219')
                if k<n:b+=edge(x+50,y-51,x,y,'#2d8c67')
            b+=token(x,y,comb(n,k),f'p{n}-{k}','#ffdb8d' if n==r else '#e2edf2',20)
    frames.append(f(b,'Inspect one row of subset counts. Each interior entry partitions selections into those including a distinguished element and those excluding it, giving the two parent contributions.',r'\binom nk=\binom{n-1}{k-1}+\binom{n-1}{k}',dict(row=r,values=[comb(r,k) for k in range(r+1)])))
model('dc-pascal','Pascal parents represent disjoint subset cases','pascal-triangle','Interior values equal their two parent counts; boundary subset counts are one.',frames)

def pathdrawing(word,processed,diagonal=False):
    b=txt(380,30,'A step word and a grid path encode the same ordered choices')
    for x in range(5):
        for y in range(5):b+=f'<circle cx="{150+x*75}" cy="{335-y*65}" r="3" fill="#99b7c4"/>'
    if diagonal:b+=edge(150,335,450,75,'#93adb8',2)
    x=y=0
    for i,s in enumerate(word[:processed]):
        u,v=x+(s=='R'),y+(s=='U');b+=edge(150+x*75,335-y*65,150+u*75,335-v*65,'#b98219',6);x,y=u,v
    b+=token(150+x*75,335-y*65,'','cursor','#ffdb8d',10)
    for i,s in enumerate(word):b+=txt(550+(i%4)*42,105+(i//4)*58,s,25,'#b98219' if i<processed else '#55798b')
    b+=txt(625,260,'prefix '+str(processed),19)+txt(625,315,'point '+str((x,y)),19)
    return b
frames=[];w='RRURURUU'
for t in range(9):
    b=pathdrawing(w,t)
    frames.append(f(b,'Advance exactly one unit step along the word prefix. Right and up multiplicities determine the endpoint; the order of those steps determines the path itself.',r'\binom{4+4}{4}=70',dict(word=w,processed=t,right=w[:t].count('R'),up=w[:t].count('U'),count=70)))
model('dc-path','Step words move along a lattice path','lattice-path','Each processed R changes x by one; each processed U changes y by one.',frames)
frames=[];bad='URRRUU';first=1;reflected='RRRRUU'
for t in [0,1,2]:
    w=bad if t<2 else reflected;b=pathdrawing(w,6,True)+txt(380,385,'Original first crossing: U; reflected prefix: R',20)
    if t==1:b+=edge(150,335,150,270,'#a64b65',9)+token(150,270,'','crossing','#efbfd0',12)
    frames.append(f(b,'The bad path first crosses above the diagonal on its initial up step. Reflect precisely that first-crossing prefix, changing the endpoint and preserving an invertible correspondence.',r'\binom63-\binom62=20-15=5',dict(original=bad,firstCrossing=first,reflected=reflected,phase=t,endpoint=[w.count('R'),w.count('U')],count=5)))
model('dc-reflection','Reflect the first boundary-crossing prefix','lattice-path','The transformed bad path has four right and two up steps; the inverse reflects its first opposite crossing.',frames)

assert len(MODELS)==15
# Explain the actual inspected transition instead of repeating a generic caption.
for m in MODELS:
    for i,frame in enumerate(m['frames']):
        s=frame['state'];id=m['id'];lead=''
        if id=='dc-tree':lead=('Overview: all ten leaves are visible.' if s['active']==0 else f'First value {s["active"]}: {5-s["active"]} legal second values are highlighted.')
        elif id=='dc-fibers':lead='Current unordered subset: '+', '.join(s['pair'])+'.'
        elif id=='dc-nonuniform':lead=f'Current multiset {s["word"]}: exactly {s["fiber"]} ordered words map to it.'
        elif id=='dc-selection':lead=f'Current case selects {s["first"]} first-group and {s["second"]} second-group questions, with {s["count"]} choices.'
        elif id=='dc-word':lead=f'Prefix {s["prefix"] or "empty"}: {s["total"]} positions remain, with inventory '+', '.join(a+'='+str(v) for a,v in s['remaining'].items())+'.'
        elif id=='dc-gaps':lead=f'{s["processed"]} index shifts have been applied; the lower row currently displays '+', '.join(map(str,s['displayed']))+'.'
        elif id in ('dc-circle','dc-periodic'):lead=f'Rotation by {s["rotation"]} seats; this pattern has '+str(s['orbit'] if isinstance(s['orbit'],int) else len(s['orbit']))+' distinct rotation representatives.'
        elif id=='dc-stars':lead=f'{s["processed"]} symbols of the star–bar encoding have been scanned. The middle box remains empty because its two boundaries are consecutive.'
        elif id=='dc-lower':lead=['Original occupancies are 3,2,4; amber units mark the fixed lower bounds 2,1,0.','Remove the compulsory units. Only the residual occupancies 1,1,4 remain visible.','Restore the compulsory units to recover the original occupancies 3,2,4.'][s['phase']]
        elif id=='dc-groups':lead='Current labeled contents: '+', '.join('label '+str(j+1)+' holds '+g for j,g in enumerate(s['groups']))+'.'
        elif id=='dc-empty':lead=f'This occupancy pattern has {s["fiber"]} distinct labelings, compared with '+('six for the separated pattern.' if s['fiber']==3 else 'three for the together pattern.')
        elif id=='dc-pascal':lead=f'Row {s["row"]} is highlighted; its subset counts are '+', '.join(map(str,s['values']))+'.'
        elif id=='dc-path':lead=f'The first {s["processed"]} steps reach point ({s["right"]},{s["up"]}); the moving marker records the actual grid endpoint.'
        elif id=='dc-reflection':lead=['The original bad path begins U and reaches its first above-diagonal crossing immediately.','Select only the first-crossing prefix U; do not reflect the entire path.','Replace that prefix U with R. The transformed path ends at (4,2), not (3,3).'][s['phase']]
        frame['caption']=lead+' '+frame['caption']
out=dict(topicId='d_counting',models=MODELS,frameCount=sum(len(m['frames']) for m in MODELS),schema='dedicated-counting-traces-v1')
(ROOT/'dist/chapters/d_counting-models.json').write_text(json.dumps(out,separators=(',',':'))+'\n',encoding='utf-8')
(BASE/'d_counting-model-audit.json').write_text(json.dumps(dict(models=len(MODELS),checkpoints=out['frameCount'],families=sorted(set(m['kind'] for m in MODELS)),invariants=[dict(id=m['id'],invariant=m['invariant']) for m in MODELS]),indent=2)+'\n')
print('Built',len(MODELS),'counting-specific traces;',out['frameCount'],'semantic checkpoints.')
