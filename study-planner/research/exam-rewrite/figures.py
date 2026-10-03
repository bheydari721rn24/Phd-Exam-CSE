"""Exact numerical vector illustrations supporting the revised solving methods."""
import html,json
from pathlib import Path
BASE=Path(__file__).parent;OUT=BASE/'figures';OUT.mkdir(exist_ok=True)
def text(x,y,s,size=23,anchor='middle',color='#25394b'):
 return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" font-family="STIX Two Math">{html.escape(str(s))}</text>'
def box(x,y,w,h,s,fill='#e8f0f5',size=23):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#91abba"/>'+text(x+w/2,y+h/2+8,s,size)
def line(x,y,a,b,arrow=True,color='#6589a0'):
 return f'<line x1="{x}" y1="{y}" x2="{a}" y2="{b}" stroke="{color}" stroke-width="2"'+(' marker-end="url(#exam-arrow)"' if arrow else '')+'/>'
def figure(topic,title,h,body,caption):
 # Every page receives at most one new figure, so this marker id is unambiguous.
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 {h}" role="img" aria-label="{html.escape(title)}"><title>{html.escape(title)}</title><defs><marker id="exam-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#6589a0"/></marker></defs>'+text(350,31,title,24)+body+'</svg>'
 (OUT/(topic+'.svg')).write_text(svg,encoding='utf-8')
 return '<figure class="logic-diagram exam-figure">'+svg+'<figcaption>'+html.escape(caption)+'</figcaption></figure>'
figures={}
b=''
for x,y,label,color in [(260,165,'A','#cee2ec'),(400,165,'B','#d5e8db'),(330,280,'C','#eee0cd')]:
 b+=f'<circle cx="{x}" cy="{y}" r="105" fill="{color}" fill-opacity=".38" stroke="#8babbc"/>'
for x,y,s in [(180,140,20),(480,140,18),(330,355,15),(330,110,12),(250,245,10),(410,245,7),(330,205,8),(610,365,10)]:b+=text(x,y,s,27)
b+=text(205,67,'A',22)+text(455,67,'B',22)+text(330,392,'C',22)+text(610,330,'Outside',20)
figures['d_sets']=figure('d_sets','Three-set data resolved into disjoint regions',425,b,'Numerical region diagram for the revised three-group question: A has 50 objects, B 45 and C 40. Inclusive pair intersections are 20, 18 and 15; the triple has 8. The single-only regions total 53, pair-only regions 29, triple 8 and outside 10. Every inclusive intersection includes the central eight.')
b=text(270,78,'B absent',22)+text(490,78,'B present',22)+text(80,145,'A absent',20)+text(80,255,'A present',20)
for x,y,v in [(170,100,'.10'),(390,100,'.30'),(170,210,'.40'),(390,210,'.20')]:b+=box(x,y,200,85,v,size=30)
b+=text(350,340,'Exactly one: .40 + .30 = .70',25)
figures['s_axioms']=figure('s_axioms','Four nonnegative masses define the event model',380,b,'With P(A)=0.60, P(B)=0.50 and intersection 0.20, the four cells are disjoint and sum to one. The off-diagonal cells are exactly-one membership; all cells except the upper-left form the union. No independence assumption is used.')
b=''
for i in range(5):b+=box(120+i*100,125,42,55,'0',size=28)
for i in range(6):
 x=91+i*100;b+=f'<line x1="{x}" x2="{x}" y1="105" y2="190" stroke="#b3c7d2" stroke-dasharray="4 5"/>'
 if i in (0,2,5):b+=text(x,160,'1',30,color='#98564f')
b+=text(350,255,'Five zeros create six available gaps',25)+text(350,307,'Choose three distinct gaps: 20 strings',25)
figures['s_counting']=figure('s_counting','Three isolated ones in an eight-bit string',345,b,'Five ordered zeros create six gaps, including both ends. Place at most one of the three indistinguishable ones in each selected gap. Choosing three gaps gives 20 strings; the pictured choice is one example, not an additional multiplicity factor.')
b=line(90,325,490,325,False)+line(90,325,90,75,False)
b+=line(90,325,200,105,False,color='#9cadb7')
b+=line(90,325,300,255)+line(90,325,160,185)+line(160,185,300,255,False,color='#a57265')
for x,y,c in [(90,325,'#506f88'),(160,185,'#44775a'),(300,255,'#447da0')]:b+=f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>'
b+=text(355,250,'v = (3, 1)',23)+text(250,170,'p = (1, 2)',23)+text(130,85,'Line: y = 2x',22)+text(350,380,'Residual v − p = (2, −1); squared distance = 5',23)
figures['l_vectors']=figure('l_vectors','Projection and perpendicular residual in actual coordinates',415,b,'The gray line is the span of (1,2). The projection of (3,1) is (1,2), and the connecting residual (2,-1) is perpendicular to the direction. Equal horizontal and vertical scales preserve the right-angle geometry. Distance is the square root of five, not the coefficient one or squared distance five.')
b=''
for i,(label,cost) in enumerate([('Left association: (AB)C','5,000 + 2,500 = 7,500'),('Right association: A(BC)','25,000 + 50,000 = 75,000')]):
 y=80+i*120;b+=box(30,y,295,70,label,size=21)+box(345,y,325,70,cost,fill='#e0ede5',size=23)
b+=text(350,355,'Shapes: A 10×100, B 100×5, C 5×50',24)
figures['l_matrices']=figure('l_matrices','Same matrix-chain result, different scalar-operation costs',395,b,'Both associations produce a 10 by 50 matrix in exact arithmetic. The left intermediate is 10 by 5; the right intermediate is 100 by 50. Each cost multiplies the three dimensions of the corresponding ordinary matrix product. Factor order is preserved.')
b=''
bits='11110110';weights=[-128,64,32,16,8,4,2,1]
for i,(bit,w) in enumerate(zip(bits,weights)):
 x=35+i*80;b+=box(x,100,70,55,bit,size=29)+text(x+35,207,str(w),23)
b+=text(350,270,'Two’s-complement weights sum to −10',26)+text(350,320,'Unsigned interpretation of the same bits: 246',23)
figures['g_number']=figure('g_number','One word, two precise numeric interpretations',355,b,'The most significant signed weight is negative 128; all other weights stay positive. For 11110110 the selected signed weights add to -10, while unsigned weights add to 246. A representation contract must be chosen before arithmetic or comparison.')
b=''
for y,label in [(90,'ab'),(160,'¬a · c'),(230,'F')]:b+=text(65,y+12,label,24)
for t in range(9):
 x=130+60*t;b+=f'<line x1="{x}" x2="{x}" y1="65" y2="290" stroke="#d9e3e8"/>'+text(x,355,t,19)
b+=f'<rect x="310" y="218" width="180" height="52" fill="#f1ded8"/>'
paths=[[(130,90),(250,90),(250,115),(610,115)],[(130,185),(430,185),(430,160),(610,160)],[(130,230),(310,230),(310,255),(490,255),(490,230),(610,230)]]
for pts in paths:b+='<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="none" stroke="#346c91" stroke-width="3"/>'
b+=text(400,315,'Low width: 3 ns',23)+text(635,355,'ns',19)
figures['g_gates']=figure('g_gates','A static-one hazard under the stated transport delays',395,b,'During a falling selector transition, the ab path falls at two nanoseconds and the other term rises at five. A one-nanosecond OR transport delay shifts the low pulse to three through six nanoseconds, retaining width three. The steady-state Boolean function is one on both sides of the transition.')
b=''
pos={(i,j):(120+120*i,345-90*j-30*i) for i in range(4) for j in range(3)}
for (i,j),(x,y) in pos.items():
 for ni,nj in [(i+1,j),(i,j+1)]:
  if (ni,nj) in pos:
   a,z=pos[(ni,nj)];b+=line(x,y,a,z,False)
for (i,j),(x,y) in pos.items():
 b+=f'<circle cx="{x}" cy="{y}" r="20" fill="#e2edf3" stroke="#7c9dad"/>'+text(x,y+7,2**i*3**j,22)
b+=text(350,408,'12 divisors · 17 cover edges · chain length 6',23)
figures['d_relations']=figure('d_relations','Divisibility of 72 as an exponent-grid Hasse diagram',445,b,'Every vertex is 2 to the i times 3 to the j, with i from zero through three and j zero through two. Upward edges increment one exponent, giving nine plus eight covers. Transitive comparisons are represented by paths, not extra drawn edges. A longest chain has six vertices and five edges.')
b=text(140,70,'Inputs',23)+text(470,70,'Outputs in the same set',22)
for i,target in [(1,1),(2,2),(3,1),(4,2)]:b+=line(165,90+70*(i-1),435,90+70*(target-1))
for i in range(1,5):
 y=90+70*(i-1)
 for x in (140,460):
  b+=f'<circle cx="{x}" cy="{y}" r="22" fill="'+('#e0ede5' if i<=2 else '#eef1f3')+'" stroke="#8facbd"/>'+text(x,y+8,i,25)
 if i<=2:b+=text(555,y+8,'Fixed image point',20)
b+=text(350,365,'Every image point is fixed: applying f twice changes nothing',22)
figures['d_functions']=figure('d_functions','A two-image idempotent function on four labeled points',405,b,'The function maps 1 to 1, 2 to 2, 3 to 1 and 4 to 2. Its image is {1,2}, and both image points are fixed, so the function is idempotent. Once the two image points are chosen, each of the two other inputs has two independent output choices.')
b=''
for row in range(2):
 for col in range(7):
  k=row*7+col;x=70+92*col;y=115+105*row
  b+=f'<circle cx="{x}" cy="{y}" r="24" fill="'+('#d6e9dd' if k in (6,13) else '#edf1f4')+'" stroke="#8ba9b9"/>'+text(x,y+8,k,24)
b+=text(350,300,'Solutions modulo 14: 6 and 13',25)+text(350,350,'One residue modulo 7: x = 6 + 7t',25)
figures['d_number']=figure('d_number','Solve 6x ≡ 8 modulo 14 by reducing the gcd',390,b,'The common gcd is two, so divide the coefficient, target and modulus by two. The reduced inverse gives x equal to six modulo seven; lifting produces six and thirteen modulo fourteen. Two residue solutions per full period are distinct from counting an arbitrary bounded interval.')
b=''
for y,label in [(75,'Depth 0: 1 node × 8 × 3 = 24'),(140,'Depth 1: 2 nodes × 4 × 2 = 16'),(205,'Depth 2: 4 nodes × 2 × 1 = 8'),(270,'Leaves: 8 nodes × base cost 1 = 8')]:b+=box(60,y,580,48,label,size=24)
b+=text(350,370,'Total at n = 8: 24 + 16 + 8 + 8 = 56',25)
figures['a_recurrence']=figure('a_recurrence','Critical logarithmic toll counted one complete level at a time',410,b,'This numerical tree uses T(n)=2T(n/2)+n log base two n with T(1)=1. The root and two smaller internal levels contribute 24,16,8; the eight leaves contribute eight. The arithmetic level sequence yields an extra logarithmic factor in the general total.')
b=''
for i,value in enumerate([4,13,22,15]):
 y=80+i*65;b+=box(30,y,250,45,f'Degree {i}: {value}',size=23)
for i,label in enumerate(['Index 0: 4 + 22 = 26','Index 1: 13 + 15 = 28']):b+=box(415,125+i*125,250,60,label,size=21)
for i in range(4):b+=line(280,102+i*65,415,155+(i%2)*125)
b+=text(350,390,'Linear length is 4; cyclic length 2 aliases degrees',23)
figures['a_divide']=figure('a_divide','Insufficient convolution padding folds coefficients together',430,b,'The exact product coefficients 4,13,22,15 have length four. Reducing modulo x squared minus one combines degrees zero and two, and degrees one and three, producing 26,28. Truncating the high-degree terms would not compute the same cyclic convolution.')
(BASE/'figures.json').write_text(json.dumps(figures,indent=2),encoding='utf-8')
print('Created',len(figures),'numerically specified vector figures.')
