"""Render only the functions chapter; preserve all accepted chapter banks."""
import ast,html,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
sys.path.insert(0,str(BASE/'exam-rewrite'))
import mathml
from mathml import render,width,markdown_math
md=MarkdownIt('commonmark',{'html':True}).enable('table')
for filename,names in [('build_correct_chapter.py',('scope_preserving_display',)),('exam-calibration/build.py',('prep','text')),('build_conditional_chapter.py',('chapter_wrap','e','label','box','line','fig','item'))]:
 for f in ast.parse((BASE/filename).read_text()).body:
  if isinstance(f,ast.FunctionDef) and f.name in names:exec(compile(ast.Module(body=[f],type_ignores=[]),filename,'exec'))
mathml.wrap_display=chapter_wrap
from kmap_math_layout import wrap
mathml.wrap_display=wrap
figures={}
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
questions=json.loads((BASE/'g_kmap-questions.json').read_text());auth=json.loads((BASE/'g_kmap-authentic.json').read_text())
for q in auth:q['questionNumber']=q['qNumber']
bank='<h3 id="authentic-questions">Authentic canonical-form and hazard revisits</h3>'+''.join(item(q,i,True).replace('Authentic examination · checked English translation','Authentic bridge revisit · checked English adaptation') for i,q in enumerate(auth,1))
bank=bank.replace('<strong>Correct option: None.</strong>', '<strong>Convention-sensitive tutorial; no unqualified single answer.</strong>')
bank+='<h3 id="original-questions">Original and course-inspired mathematical/conceptual problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,4))
rules=[]
for block in (BASE/'g_kmap-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab="""<section class="lab" id="kmap-lab"><form id="kmap-form"><label>Representation<select name="mode"><option value="SOP">Minimum SOP</option><option value="POS">Minimum POS</option></select></label><label>Required one indices, comma-separated; empty is allowed<input name="on" type="text" value="0,2,3,4,5,7"></label><label>Don’t-care indices, comma-separated; empty is allowed<input name="dc" type="text" value=""></label><button type="submit">Compute every optimum and restart trace</button></form><div id="kmap-output" aria-live="polite"></div><section class="concept-animation" id="kmap-player" data-loaded="true"></section></section>"""
source=(BASE/'g_kmap.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:kmap -->',lab)
for k,v in figures.items():source=source.replace('<!-- FIGURE:'+k+' -->',v)
body=text(source)
anchors=['sources','canonical','geometry','covers','care-sets','tabulation','implementation','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==84 and body.count('class="review-rule"')==80
title='Minterms, Maxterms, and Logic Minimization'
nav=' '.join('<a href="#'+a+'">'+a.capitalize()+'</a>' for a in anchors)
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="g_kmap.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Digital Logic · Week 2</p><h1>{title}</h1><p>Review draft · five reviewed university courses · 84 worked problems · 80 examination rules · 14 concept simulations</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="g_kmap.js"></script><script src="exam-calibration.js"></script></body></html>'
(ROOT/'dist/chapters/g_kmap.html').write_text(page,encoding='utf-8')
for part,name in [('source-audit','sources'),('quality-audit','quality')]:
 audit=text((BASE/f'g_kmap-{part}.md').read_text())
 (ROOT/f'dist/reviews/g_kmap-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Logic minimization chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/g_kmap.html">← Logic minimization chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());w=next(w for w in lessons if w['week']==2)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='g_kmap']+[dict(topicId='g_kmap',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/g_kmap.html',questionCount=84,authenticQuestionCount=3,originalQuestionCount=81,examNotesCount=80,sourceAuditUrl='reviews/g_kmap-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
p=ROOT/'dist/course-audit-week1.en.json';data=json.loads(p.read_text());reviewed=json.loads((BASE/'g_kmap-reviewed-courses.json').read_text());ids={c['id'] for c in reviewed}
data['courses']=[c for c in data['courses'] if c['id'] not in ids]+reviewed;data['reviewedAt']='2026-10-04';p.write_text(json.dumps(data,indent=2)+'\n')
from build_concept_animations import build_data,install_animations
build_data();install_animations()
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built sole logic-minimization draft: 84 fully solved tasks, 80 rules, seven diagrams, fourteen exact models and a custom cover lab.')
