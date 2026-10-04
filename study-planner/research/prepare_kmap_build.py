from pathlib import Path
import re
B=Path(__file__).resolve().parent;R=B.parent
p=B/'build_concept_animations.py';s=p.read_text();s=s.replace('functions,arrays\n','functions,arrays,kmap\n');p.write_text(s)
p=B/'animations/catalog.py';s=p.read_text()
if "'g_kmap':" not in s:s=s.rstrip()[:-1]+",\n'g_kmap':{'geometry':['km-gray','km-corners'],'covers':['km-chart','km-cycle','km-greedy','km-petrick'],'care-sets':['km-dc','km-pos'],'tabulation':['km-merge','km-qm'],'implementation':['km-hazard-cover','km-hazard-time','km-sharing']}\n}\n"
p.write_text(s)
p=B/'qa_animations_browser.py';s=p.read_text().replace('scene.id.startsWith("arrays-custom-")','scene.id.startsWith("arrays-custom-")||scene.id.startsWith("kmap-custom-")');p.write_text(s)
s=(B/'build_arrays_chapter.py').read_text();s=s[:s.index('figures={}')]+'''figures={}
def mapfig(key,title,on,dc=(),active=(),caption=''):
 b=label(350,30,title,23);gray=[0,1,3,2]
 for j,v in enumerate(gray):b+=label(165+130*j,80,format(v,'02b'),20)
 for r,v in enumerate(gray):
  b+=label(65,130+60*r,format(v,'02b'),20)
  for c,w in enumerate(gray):
   i=4*v+w;value='1' if i in on else 'X' if i in dc else '0'
   color='#c5e7d9' if i in active else '#edf3f6'
   b+=f'<rect x="{110+130*c}" y="{105+60*r}" width="110" height="46" rx="6" fill="{color}" stroke="#96b7c7"/>'+label(165+130*c,135+60*r,str(i)+': '+value,21)
 b+=label(350,385,'Rows AB; columns CD; each axis uses 00, 01, 11, 10',19)
 return fig('kmap-'+key,title,420,b,caption)
b=label(350,30,'The same row gives opposite literal polarity',23)
b+=box(180,80,340,55,'ABCD = 1010; index = 10')
b+=box(40,200,280,65,'minterm: A B̅ C D̅')+box(380,200,280,65,'maxterm: A̅ + B + C̅ + D')
b+=label(350,350,'At row 1010: the minterm is 1; the maxterm is 0',21)
figures['polarity']=fig('kmap-polarity','Indexed minterm and maxterm polarity',400,b,'Figure 1. Every minterm literal is satisfied by its indexed row; every maxterm literal is false there. Overbars use the dedicated mathematical font.')
figures['gray']=mapfig('gray','Gray geometry does not change binary indices',[0,2,8,10],caption='Figure 2. Cell labels show decimal index and output. Moving to a neighboring row or column changes one bit, including cyclic edge wrapping.')
figures['corners']=mapfig('corners','Four corners: B = 0 and D = 0',[0,2,8,10],active=[0,2,8,10],caption='Figure 3. The green corner cells jointly free A and C. Their exact cube is -0-0; no specified zero belongs to the group.')
b=label(350,30,'A prime chart exposes unique ownership',23)
for j,m in enumerate([2,3,5,7]):b+=label(260+110*j,90,str(m),22)
for r,c in enumerate(['01-','1-1','-11']):
 b+=label(95,150+65*r,c,23)
 from kmap_model import cells
 for j,m in enumerate([2,3,5,7]):b+=box(215+110*j,120+65*r,90,45,'×' if m in cells(c) else '·')
b+=label(350,370,'Rows 2 and 5 force 01- and 1-1; -11 is nonessential',20)
figures['chart']=fig('kmap-chart','Essential-prime witnesses in a complete chart',410,b,'Figure 4. Candidate rows are products; columns are required one indices. A single mark in a column is a proof of unique ownership, not a heuristic.')
figures['pos']=mapfig('pos','POS groups zero rows of majority',[i for i in range(16) if sum(map(int,format(i>>1,'03b')))>=2],active=[0,1,2,3,4,5,8,9],caption='Figure 5. This four-input view replicates three-input majority across free D. Highlighted zeros are complement obligations; POS factors reverse their fixed-bit polarity.')
b=label(350,30,'QM generations preserve the exact allowed rows',22)
b+=box(110,80,480,50,'0000    0010    1000    1010')
b+=box(110,185,480,50,'00-0    10-0    -000    -010')
b+=box(230,290,240,50,'-0-0')+line(350,130,350,185)+line(350,235,350,290)
b+=label(350,390,'Different parent pairs produce the same final cube',20)
figures['qm']=fig('kmap-qm','Complete tabular merge levels',430,b,'Figure 6. Every dash removes one fixed literal. The two possible parent pairings yield one deduplicated four-cell cube; all contributing parents are marked.')
b=label(350,30,'One input transition; two different path delays',22)
for r,(name,segments) in enumerate([('A',[(0,0,6,0)]),('AB',[(0,1,1,1),(1,0,6,0)]),('not A C',[(0,0,4,0),(4,1,6,1)]),('F',[(0,1,2,1),(2,0,5,0),(5,1,6,1)])]):
 y=90+75*r;b+=label(75,y+10,name,19)
 for a,v,z,w in segments:b+=line(155+75*a,y-20*v,155+75*z,y-20*w)
 for j in range(len(segments)-1):x=155+75*segments[j][2];b+=line(x,y-20*segments[j][3],x,y-20*segments[j+1][1])
for t in range(7):b+=label(155+75*t,395,str(t),19)
b+=label(350,435,'Transport delay: F is low from time 2 until time 5',20)
figures['hazard']=fig('kmap-hazard','Exact static-one transport trace',475,b,'Figure 7. After A falls at time zero, AB falls at one and the slow complemented product rises at four. The OR adds one delay unit to each event.')
figures={k:v.replace('conditional-diagram','kmap-diagram') for k,v in figures.items()}
'''+s[s.index('questions=json.loads'):]
s=s.replace('p_arrays','g_kmap').replace('arrays-','kmap-').replace('LAB:arrays','LAB:kmap').replace('FIGURE:arrays','FIGURE:kmap')
start=s.index("lab='''");end=s.index('source=(BASE/',start)
s=s[:start]+'''lab="""<section class="lab" id="kmap-lab"><form id="kmap-form"><label>Representation<select name="mode"><option value="SOP">Minimum SOP</option><option value="POS">Minimum POS</option></select></label><label>Required one indices, comma-separated; empty is allowed<input name="on" type="text" value="0,2,3,4,5,7"></label><label>Don’t-care indices, comma-separated; empty is allowed<input name="dc" type="text" value=""></label><button type="submit">Compute every optimum and restart trace</button></form><div id="kmap-output" aria-live="polite"></div><section class="concept-animation" id="kmap-player" data-loaded="true"></section></section>"""
'''+s[end:]
s=s.replace("anchors=['sources','representation','layouts','c-semantics','traversals','mutation','python','strings','growth','packed','problems','review','laboratory','references']","anchors=['sources','canonical','geometry','covers','care-sets','tabulation','implementation','problems','review','laboratory','references']")
s=s.replace("title='Arrays and Indexing'","title='Minterms, Maxterms, and Logic Minimization'")
s=s.replace('==83','==84').replace('83 worked problems','84 worked problems').replace('18 concept simulations','14 concept simulations').replace('six reviewed university courses','five reviewed university courses').replace('Programming Fundamentals · Week 2','Digital Logic · Week 2')
s=s.replace('enumerate(questions,3)','enumerate(questions,4)')
s=s.replace('Authentic array-reasoning bridge revisits','Authentic canonical-form and hazard revisits').replace("'arrays chapter audit'","'logic minimization chapter audit'")
s=s.replace("q['questionNumber']=q['qNumber']","q['questionNumber']=q['qNumber']")
s=s.replace("bank+='<h3", "bank=bank.replace('<strong>Correct option: None.</strong>', '<strong>Convention-sensitive tutorial; no unqualified single answer.</strong>')\nbank+='<h3")
s=s.replace('g_kmap.css','g_kmap.css').replace('g_kmap.js','g_kmap.js')
s=s.replace('questionCount=83,authenticQuestionCount=2,originalQuestionCount=81','questionCount=84,authenticQuestionCount=3,originalQuestionCount=81')
s=s.replace('← Arrays chapter','← Logic minimization chapter').replace('Arrays chapter audit','Logic minimization chapter audit')
s=s[:s.index("print('Built sole")]+"print('Built sole logic-minimization draft: 84 fully solved tasks, 80 rules, seven diagrams, fourteen exact models and a custom cover lab.')\n"
s=s.replace('mathml.wrap_display=chapter_wrap','mathml.wrap_display=chapter_wrap\nfrom kmap_math_layout import wrap\nmathml.wrap_display=wrap')
(B/'build_kmap_chapter.py').write_text(s,encoding='utf-8')
(R/'dist/chapters/g_kmap.css').write_text((R/'dist/chapters/p_arrays.css').read_text().replace('arrays','kmap')+'\n#kmap-output table{width:100%;font-family:"STIX Two Math",serif} #kmap-output{overflow:auto} #kmap-output p{overflow-wrap:anywhere}\n',encoding='utf-8')
print('Prepared renderer and fourteen exact concept models.')
