"""Exact map, covering, merge, and single-input hazard teaching checkpoints."""
from common import node,frame,scene
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from kmap_model import cells,primes,optimum,essentials,qm,cost
G=[0,1,3,2]
def grid(on,dc=(),selected=(),n=4):
 rows=G if n==4 else [0,1];ns=[]
 for r,b in enumerate(rows):
  ns.append(node('row'+str(r),format(b,'02b' if n==4 else '01b'),70,90+55*r,w=70,h=38,size=19))
  for c,d in enumerate(G):
   m=(b<<2)|d;v='1' if m in on else 'X' if m in dc else '0'
   ns.append(node('m'+str(m),str(m)+': '+v,180+120*c,90+55*r,w=105,h=38,size=21,tone='done' if m in selected else 'plain'))
 for c,d in enumerate(G):ns.append(node('col'+str(c),format(d,'02b'),180+120*c,40,w=75,h=34,size=18))
 return ns
def add(id,title,description,invariant,fs):return scene('km-'+id,title,description,invariant,fs)
fs=[]
for t,c in enumerate(G+[0]):
 ns=grid([0,2,8,10])+[node('token','CD='+format(c,'02b'),180+120*G.index(c),320,w=110,h=38,tone='active',size=20)]
 fs.append(frame(ns,f'Column label {format(c,"02b")} is selected. Consecutive Gray labels, including the last-to-first wrap, change exactly one input coordinate; minterm indices remain ordinary binary.',snapshot=dict(label=c,step=t)))
add('gray','Gray traversal and wrapping','Follow 00 → 01 → 11 → 10 → 00 across a fixed four-input map.','Each consecutive Gray transition changes one coordinate; decimal index meaning is unchanged.',fs)
def covering(id,title,n,on,dc,cover,description):
 fs=[];seen=set()
 for k in range(len(cover)+1):
  c=cover[k-1] if k else '';seen|=set(cells(c)) if c else set()
  ns=grid(on,dc,seen,n)+[node('token',c or 'start',180+120*(k%4),320,w=110,h=38,tone='active',size=20)]
  fs.append(frame(ns,('Begin with the complete fixed specification. Required one rows remain uncovered, and optional cells do not create extra obligations.' if not k else f'Select cube {c}. Its cells contain no specified zero; the accumulated union covers {sorted(seen&set(on))}. Every group follows fixed-coordinate semantics, including any wrap-around.'),{'selected terms':k,'covered required rows':len(seen&set(on))},snapshot=dict(n=n,on=on,dc=dc,cover=cover[:k],covered=sorted(seen),requiredCovered=sorted(seen&set(on)))))
 add(id,title,description,'Every selected cube is contained in ON ∪ DC and has at least one ON cell; the snapshot stores the exact union.',fs)
covering('corners','The four corners form one cube',4,[0,2,8,10],[],['-0-0'],'Merge four wrapping corners by freeing A and C while B and D stay zero.')
covering('cycle','Two-level optimum without essentials',3,[0,2,3,4,5,7],[],['-00','01-','1-1'],'Select one three-prime optimum of a six-cycle; each selected pair has exact coverage.')
covering('greedy','A locally plausible nonminimum cover',3,[0,2,3,4,5,7],[],['-00','-11','0-0','1-1'],'Watch the first two choices leave incompatible residual rows; four terms finish a cover when three suffice.')
covering('dc','Optional cells assist but do not demand coverage',4,[1,5],[8,9,10,11],['0-01'],'Cover required rows 1 and 5; the remote DC-only block need not be covered.')
covering('hazard-cover','Cover required one-edges, not only vertices',3,[2,3,5,7],[],['01-','1-1','-11'],'The third product BC is logically redundant but provides a stable bridge for A changes with B=C=1.')
fs=[]
for c in ['01-0','11-0','-1-0']:
 ns=[node('parent0','01-0',180,100,w=180),node('parent1','11-0',540,100,w=180),node('token',c,180 if c=='01-0' else 540 if c=='11-0' else 360,260,w=180,tone='active')]
 fs.append(frame(ns,f'Pattern {c} denotes exactly the rows {sorted(cells(c))}. The two parents share the same free-bit mask and differ only in A, so their union removes that one fixed coordinate.',snapshot=dict(pattern=c,rows=sorted(cells(c)))))
add('merge','A legal equal-mask QM merge','Compare the two half-cubes, then replace their differing A bit with a dash.','The child is exactly the union of the two parents, not an approximate numerical interval.',fs)
ps,lev=qm(4,[0,2,8,10]);fs=[]
for k,patterns in enumerate(lev):
 ns=[node('cube'+str(i),c,130+170*(i%4),80+90*(i//4),w=140,h=55,tone='done' if k==len(lev)-1 else 'plain') for i,c in enumerate(patterns)]
 ns.append(node('token','level '+str(k),130+170*min(k,3),300,w=130,h=38,tone='active'))
 fs.append(frame(ns,f'Generation {k} contains exactly {patterns}. Legal merges preserve the allowed row set, increase free dimensions by one, and deduplicate child patterns reached through different parent pairs.',snapshot=dict(level=k,patterns=patterns,on=[0,2,8,10])))
add('qm','All merge generations for a wrapping cube','Construct the complete prime `-0-0` from four minterms through every intermediate legal pair.','Every generation is deduplicated; terminal uncombined patterns are prime candidates.',fs)
fs=[]
for k,z in enumerate([0,1,2,4]):
 ns=grid([3,5,6,7],selected=[z],n=3)+[node('token','zero '+str(z),180+120*G.index(z%4),320,w=110,h=38,tone='active')]
 fs.append(frame(ns,f'Selected row {z} is a specified zero of majority. POS groups these zero obligations through the complement; fixed-zero coordinates become positive literals in the final sum factor.',snapshot=dict(zero=z,zeroSet=[0,1,2,4])))
add('pos','POS begins with zero rows','Select majority zero rows before constructing complement cubes and De Morgan sum factors.','The POS obligation set is Z, not O; canonical maxterm polarity is reversed.',fs)
fs=[]
for k,c in enumerate(['01-','1-1','-11']):
 owners={str(m):sorted(p for p,s in primes(3,[2,3,5,7]).items() if m in s) for m in [2,3,5,7]}
 ns=[node('r'+str(m),str(m)+': '+','.join(owners[str(m)]),380,70+65*j,w=560,h=42,size=20,tone='done' if c in owners[str(m)] else 'plain') for j,m in enumerate([2,3,5,7])]
 ns.append(node('token',c,130+240*k,320,w=125,h=38,tone='active'))
 fs.append(frame(ns,f'Candidate {c} is highlighted in the exact ownership chart. Rows 2 and 5 have unique owners and force two primes; row 7 has multiple owners and cannot force the consensus cube alone.',snapshot=dict(candidate=c,owners=owners,essentials=['01-','1-1'])))
add('chart','Unique ownership proves essentials','Highlight each of three multiplexer primes against the four required rows.','Essential status is defined in the complete chart, before discretionary pruning.',fs)
fs=[]
for k,s in enumerate([[],['P','Q'],['P','R'],['Q','R']]):
 clauses=[['P','Q'],['Q','R'],['P','R']];sat=[bool(set(s)&set(c)) for c in clauses];w={'P':2,'Q':3,'R':5}
 ns=[node('c'+str(j),'+'.join(c),140+240*j,110,w=205,h=55,tone='done' if sat[j] else 'plain') for j,c in enumerate(clauses)]
 ns+=[node('choice','select '+(''.join(s) or 'none'),380,220,w=300),node('token','cost '+str((len(s),sum(w[x] for x in s))),140+180*k,315,w=140,h=38,tone='active',size=19)]
 fs.append(frame(ns,f'The selection {s} satisfies clause values {sat}. All three pair selections cover the chart, but the secondary literal weights make PQ strictly less expensive than PR or QR.',snapshot=dict(selection=s,satisfied=sat,cost=[len(s),sum(w[x] for x in s)])))
add('petrick','Selection clauses and a literal-cost tie break','Compare PQ, PR and QR as actual covers of a three-clause selection problem.','The selection Boolean variables are not circuit inputs; cost is computed on chosen candidates.',fs)
fs=[]
for t in [0,1,2,3,4,5]:
 vals={'A':0,'AB':int(t<1),'not A':int(t>=3),'not A C':int(t>=4),'F':int(t<2 or t>=5)}
 ns=[node(key,val,110+135*j,110,w=115,h=60,size=22) for j,(key,val) in enumerate(vals.items())]+[node('labels',', '.join(vals),380,220,w=650,h=45,size=19),node('token','time '+str(t),90+110*t,315,w=110,h=38,tone='active')]
 fs.append(frame(ns,f'At transport time {t}, the settled input transition has propagated to the displayed signals. AB falls at one, the slow complement product rises at four, and F is low only from time two until five.',snapshot=dict(time=t,signals=vals,delay=[3,1,1])))
add('hazard-time','Transport-delay hazard with exact events','Advance through the gate events of a falling A with B=C=1 and delays 3,1,1.','The output low interval is [2,5); a consensus BC remains one and prevents the gap.',fs)
fs=[]
for k,p in enumerate(['AB','AC','BC']):
 ns=[node('p'+str(j),x,180+200*j,100,w=130,h=50,tone='active' if x==p else 'plain') for j,x in enumerate(['AB','AC','BC'])]
 ns+=[node('F','F: AB + AC',220,230,w=280),node('G','G: AB + BC',540,230,w=280),node('token',p,180+200*k,320,w=120,h=38,tone='active')]
 fs.append(frame(ns,f'Distinct product {p} is selected. AB feeds both output sums, while AC feeds only F and BC only G; three products require four product-to-output connections.',snapshot=dict(product=p,outputs=['F','G'] if p=='AB' else ['F'] if p=='AC' else ['G'])))
add('sharing','PLA products and output connections differ','Track one shared product and two output-specific products.','A shared product must be valid for every output it feeds; product count differs from connection count.',fs)
fs=[]
for k,selected in enumerate([[0,1,2,3],[16,17,18,19],[0,1,2,3,16,17,18,19]]):
 ns=[]
 for r,base in enumerate([0,16]):
  ns.append(node('plane'+str(r),'A='+str(r),75,100+120*r,w=85,h=40,size=20))
  for j,d in enumerate(G):
   m=base+d;ns.append(node('m'+str(m),str(m),200+130*j,100+120*r,w=105,h=45,tone='done' if m in selected else 'plain'))
 ns.append(node('token',['000--','100--','-00--'][k],180+200*k,320,w=140,h=38,tone='active'))
 fs.append(frame(ns,f'Plane selection {k} contains rows {selected}. Matching four-cell groups in A=0 and A=1 planes merge to -00--, so the final product retains only complemented B and C.',snapshot=dict(n=5,pattern=['000--','100--','-00--'][k],rows=selected)))
add('planes','Matching groups across a fifth-input plane','Combine corresponding groups when A is the most significant plane variable.','Variable order is A,B,C,D,E; plane indices differ by 16, not by one.',fs)
