"""Exact question-specific vector figures; no unrelated borrowed scene inputs."""
from html import escape
import re
def text(x,y,s,math=False):return f'<text x="{x}" y="{y}" class="'+('pr-math'if math else'pr-prose')+'">'+escape(s)+'</text>'
def figure(title,body,caption):return '<figure class="pr-model pr-static"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 330" role="img" aria-label="'+escape(title)+'">'+text(20,32,title)+body+'</svg><figcaption>'+escape(re.sub(r'Problem\s*\d+:','This problem:',caption))+'</figcaption></figure>'
def cells(title,labels,caption):
 body=''
 for i,(name,value,note)in enumerate(labels):
  col=i%4;row=i//4;x=20+185*col;y=58+126*row
  body+=f'<rect x="{x}" y="{y}" width="168" height="108" rx="7" fill="#eef5f1" stroke="#bed3ca"/>'+text(x+14,y+25,name)+text(x+14,y+54,value,True)+text(x+14,y+83,note)
 return figure(title,body,caption)
def table(values,title='The exact four-cell probability model'):
 names=['Both events','A only','B only','Neither'];caption='These formal candidate cells include a negative entry, so they cannot define a probability measure.'if'negative'in title else'The four boxes are disjoint probability masses in the stated measure. Their sizes are schematic; the printed values give the exact mass. Conditional probabilities use a row or column sum as denominator.';return cells(title,[(n,v,'Candidate cell'if'negative'in title else'Disjoint joint cell')for n,v in zip(names,values)],caption)
def network(kind):
 if kind=='shared':
  nodes=[(45,165,'Source'),(260,165,'Junction'),(650,165,'Destination')];edges=[(0,1,'E: p',0),(1,2,'F: p',-65),(1,2,'G: p',65)]
  body=''
  # Parallel edges use curved paths, with their endpoints on the same junction ports.
  body+='<path d="M67 165H238" stroke="#17636a" stroke-width="2.5" fill="none"/>'+text(138,143,'E: p',True)
  for offset,label in[(-100,'F: p'),(100,'G: p')]:body+=f'<path d="M282 165 Q455 {165+offset} 628 165" stroke="#17636a" stroke-width="2.5" fill="none"/>'+text(435,100 if offset<0 else 245,label,True)
  for x,y,label in nodes:body+=f'<circle cx="{x}" cy="{y}" r="22" fill="#e8f1ed" stroke="#8eada0"/>'+text(x-18 if x>50 else 20,235,label)
  return figure('Three primitive edges; two paths share E',body,'Problem48: every successful route requires E. The two alternative path events are EF and EG. Parallel curves show distinct primitive edges between the same junctions; there is no assumption that the derived paths are independent.')
 if kind=='parallel':
  body='';source=(55,175);dest=(690,175)
  for i in range(8):
   y=64+30*i;body+=f'<path d="M73 175L365 {y}L672 175" stroke="#a0b8ac" stroke-width="1.5" fill="none"/><circle cx="365" cy="{y}" r="5" fill="#17636a"/>'
  for x,y in[source,dest]:body+=f'<circle cx="{x}" cy="{y}" r="18" fill="#e8f1ed" stroke="#8eada0"/>'
  body+=text(24,315,'Source')+text(630,315,'Destination')+text(424,42,'Eight disjoint two-edge blocks')
  return figure('Sixteen independent edges in eight two-hop routes',body,'Problem50: each middle dot is a distinct vertex and each route has two primitive edges. All edges have working rate p. Lines meet only at the common terminal vertices; crossings away from a dot do not create additional vertices.')
def geometry(kind):
 # Unit coordinates map to a true equal-scale square.
 def points(a):return' '.join(f'{65+220*x},{286-220*y}'for x,y in a)
 base='<path d="M65 66V286H285" stroke="#7a9b8b" fill="none"/><rect x="65" y="66" width="220" height="220" fill="none" stroke="#c4d4cc"/>'
 if kind=='area':
  base+='<polygon points="'+points([(0,0),(1,0),(0,1)])+'" fill="#e2ece8"/><polygon points="'+points([(0,0),(.5,0),(.5,.5),(0,1)])+'" fill="#a9d2c1"/>'
  labels=['Information triangle area: 1/2','Green target area: 3/8','Conditional ratio: 3/4'];title='Uniform-square conditioning uses area';caption='Problem52: the retained triangle is x + y at most 1. The green portion has x at most 1/2. Both axes run from zero to one on the same scale; the vertical boundary is a genuine half-unit slice.'
 elif kind=='fiber':
  base+='<polygon points="'+points([(0,0),(0,1),(1,1)])+'" fill="#e2ece8"/><polyline points="'+points([(0,.6),(.6,.6)])+'" stroke="#536b9c" stroke-width="4"/><polyline points="'+points([(0,.6),(.2,.6)])+'" stroke="#17636a" stroke-width="7"/>'
  labels=['Illustrated interior y = 3/5','Fiber length: 3/5','Target length: 1/5; ratio 1/3'];title='A conditional-density fiber, not an event ratio';caption='Problem53: this illustration specializes to y = 3/5 and x at most y/3. The joint density is two on 0 < x < y < 1. The horizontal line has zero two-dimensional event probability; its normalized one-dimensional density is a specified conditional version.'
 else:
  base+='<polygon points="'+points([(0,0),(0,1),(1,1)])+'" fill="#edf2f0"/><polygon points="'+points([(0,.5),(.5,.5),(.75,.75),(0,.75)])+'" fill="#ccdfd5"/><polygon points="'+points([(0,.5),(.25,.5),(.25,.75),(0,.75)])+'" fill="#74b59d"/>'
  labels=['Illustrated y = 1/2; width = 1/4','Strip mass: 5/16','Target mass: 1/8; ratio 2/5'];title='A positive-width strip has a defined denominator';caption='Problem54: shaded masses include joint density two. The darker target is x at most 1/4 within the strip from y = 1/2 to y = 3/4. Its ratio is 2/5 at this positive width, approaching one half only when the width tends to zero.'
 base+=text(48,305,'0',True)+text(276,305,'1',True)+text(40,78,'1',True)
 for i,s in enumerate(labels):base+=text(335,95+i*53,s,True)
 return figure(title,base,caption)
def get(id):
 tables={'SC02':['3/10','1/10','1/10','1/2'],'SC03':['3/10','−1/10','3/10','1/2'],'SC05':['2/5','1/10','1/10','2/5'],'SC08':['1/3','1/3','1/6','1/6'],'SC39':['41/100','9/100','9/100','41/100'],'SC40':['3/8','1/8','1/8','3/8'],'SC42':['4/25','17/50','17/50','4/25'],'SC51':['3/8','1/8','1/8','3/8']}
 if id in tables:return table(tables[id],('An impossible table: a negative cell'if id=='SC03'else'The exact four-cell probability model'))
 if id=='SC18':return cells('Different retained histories leave different urns',[('RR','Weight 1/3','Next red: 2/5'),('RB','Weight 1/3','Next red: 3/5'),('BR','Weight 1/3','Next red: 3/5')],'Problem18: the conditional history weights sum to one. Each row of the mixture uses the actual remaining inventory; averaging those three rates gives 8/15.')
 if id=='SC33':return cells('Eight equal atoms: the repaired triple-only example',[(str(i),'Mass 1/8',('AB and C'if i==1 else'AB only'if i<=4 else'C only'if i<=7 else'Neither'))for i in range(1,9)],'Problem33: A and B coincide on atoms1through4; C contains atoms1,5,6,7. All three marginals are one half and the triple mass is one eighth. The AB intersection is one half, so mutual independence fails.')
 if id in['SC32','SC36']:return cells('Four parity states: every pair is fair and independent',[(v,'Mass 1/4','A, B, C indicators')for v in['000','011','101','110']],'The parity construction has these four equally likely triples. Each coordinate pair realizes all four binary combinations, but the full three-coordinate law is not the eight-state independent law.')
 if id=='SC37':return cells('Conditioning fair bits on equality',[('00','Weight 1/2','Retained'),('01','Weight0','Excluded'),('10','Weight0','Excluded'),('11','Weight1/2','Retained')],'Problem37: the conditional joint success mass is one half, although each conditional success marginal is also one half. The product of those marginals is only one quarter.')
 if id=='SC38':return cells('Conditioning fair bits on at least one success',[('00','Weight0','Excluded'),('01','Weight1/3','Retained'),('10','Weight1/3','Retained'),('11','Weight1/3','Retained')],'Problem38: exactly three original equal states survive. Each conditional marginal is two thirds and the joint one third, demonstrating selection-induced negative association.')
 if id=='SC55':return cells('Every feasible pairwise-independent three-event law',[(v,('t'if v.count('1')%2 else'1/4 − t'),'0 ≤ t ≤1/4')for v in['000','001','010','011','100','101','110','111']],'Problem55: the complete eight-cell table is parameterized by the triple mass t. Every pair intersection is one quarter throughout this interval. Mutual independence selects t =1/8.')
 if id=='SC44':return cells('The reporting protocol changes retained state weights',[('State 00','Prior 1/4','No report'),('State 01','Prior 1/4','Likelihood 1/2'),('State 10','Prior 1/4','Likelihood 1/2'),('State 11','Prior 1/4','Likelihood 1')],'Problem44, random-sensor protocol: multiply the prior by the shown message likelihood and normalize. The posterior weights are0,1/4,1/4,1/2. The event-only protocol instead gives three equal retained weights.')
 if id=='SC45':return cells('The six card-face outcomes, each originally mass1/6',[('RR: face1','Shows red','Other face red'),('RR: face2','Shows red','Other face red'),('RB: red face','Shows red','Other face blue'),('RB: blue face','Shows blue','Excluded'),('BB: face1','Shows blue','Excluded'),('BB: face2','Shows blue','Excluded')],'Problem45: the observed red face retains three equally likely card-face outcomes, two on RR. Distinguish a displayed face from an unordered card name.')
 if id=='SC46':return cells('A named reveal under the informed-host protocol',[('Prize door1','Prior 1/3','Reveal rate t'),('Prize door2','Prior 1/3','Reveal rate1'),('Prize door3','Prior 1/3','Reveal rate0')],'Problem46: multiply each prior by its rate of revealing door3. Only the second retained state wins by switching to door2, giving1/(1+t) after normalization.')
 if id=='SC47':return cells('An empty reveal under the uninformed-host protocol',[('Prize door1','Joint mass1/3','Posterior1/2'),('Prize door2','Joint mass1/6','Posterior1/4'),('Prize door3','Joint mass1/6','Posterior1/4')],'Problem47: the three joint masses total2/3. The final two cases win by switching, so their conditional weights add to one half.')
 if id=='SC48':return network('shared')
 if id=='SC50':return network('parallel')
 if id in['SC52','SC53','SC54']:return geometry({'SC52':'area','SC53':'fiber','SC54':'strip'}[id])
 return''
