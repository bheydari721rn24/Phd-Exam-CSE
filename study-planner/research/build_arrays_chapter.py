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
figures={}
b=label(350,30,'Six live elements, seven logical boundaries',23)
for i,v in enumerate([2,4,6,8,10,12]):
 b+=box(20+100*i,110,90,60,str(v))+label(65+100*i,205,'i = '+str(i),21)
b+=label(650,140,'end',22)+label(350,290,'0 ≤ i < 6 permits reads; boundary 6 is one-past',22)
figures['boundaries']=fig('arrays-boundaries','Element indices and exclusive end',340,b,'Figure 1. Values occupy indices zero through five. The exclusive endpoint is a valid boundary but contains no readable element.')
b=label(350,30,'Row-major strides: four elements per row',23)
for i in range(3):
 for j in range(4):b+=box(25+165*j,70+75*i,150,55,str(i)+','+str(j)+' → '+str(4*i+j))
b+=label(350,335,'Inverse: row = floor(offset / 4); column = offset mod 4',20)
figures['layouts']=fig('arrays-layouts','Dense layout and inverse map',380,b,'Figure 2. The row index skips complete rows; the column index advances within one row. Quotient and remainder uniquely undo the map.')
b=label(350,30,'Prefix values belong to boundaries',23)
for i,v in enumerate([0,3,1,6,7,3]):b+=box(20+110*i,100,100,55,str(v))+label(70+110*i,200,'P['+str(i)+']',21)
b+=label(350,285,'Sum A[1:4) = P[4] − P[1] = 7 − 3 = 4',22)
figures['prefix']=fig('arrays-prefix','Prefix boundaries and cancellation',330,b,'Figure 3. The five-element input [3, −2, 5, 1, −4] has six prefix boundaries. A half-open query subtracts two prefix values.')
b=label(350,30,'Rightward overlap: preserve the original source',22)
b+=box(30,90,280,65,'forward → [1,1,1,1]')+box(390,90,280,65,'reverse → [1,1,2,3]')
b+=box(150,225,400,65,'original source segment: [1,2,3]')
b+=label(350,360,'Copy high indices first when destination is to the right',21)
figures['overlap']=fig('arrays-overlap','Overlap counterexample and safe direction',400,b,'Figure 4. Both moves begin with [1,2,3,4] and target positions one through three. Only reverse copying preserves the original source values.')
b=label(350,30,'New outer list, shared inner row',23)
b+=box(30,90,270,60,'A: outer object 1')+box(400,90,270,60,'B: outer object 2')
b+=box(200,240,300,65,'one shared row: [2,7]')+line(165,150,300,240)+line(535,150,400,240)
b+=label(350,370,'An outer slice copies references, not inner objects',22)
figures['sharing']=fig('arrays-sharing','Nested row sharing',410,b,'Figure 5. An append through either copied outer reference changes the same inner row. Rebinding one outer slot has a different effect.')
b=label(350,30,'Expansion: length 3, capacity 3 → 6',23)
b+=box(30,95,270,65,'old: [2,4,6]')+box(390,95,280,65,'new: [2,4,6,_,_,_]')+line(300,127,390,127)
b+=box(150,240,400,65,'peak storage: 3 + 6 = 9 slots')
b+=label(350,370,'Release old storage only after copying all live entries',21)
figures['growth']=fig('arrays-growth','Distinct backing objects during growth',410,b,'Figure 6. Logical length remains three while capacity doubles. Two allocations coexist during the copy, so peak storage differs from final capacity.')
b=label(350,30,'Lower triangle: row starts are triangular counts',22)
for i in range(3):
 for j in range(i+1):b+=box(50+180*j,90+75*i,150,55,str(i)+','+str(j)+' → '+str(i*(i+1)//2+j))
b+=label(350,350,'offset = i(i + 1)/2 + j, with 0 ≤ j ≤ i',22)
figures['packed']=fig('arrays-packed','Packed lower-triangle positions',395,b,'Figure 7. Each earlier row contributes its length. Adding the within-row index gives a unique offset; upper-triangle coordinates are outside this domain.')
figures={k:v.replace('conditional-diagram','arrays-diagram') for k,v in figures.items()}
questions=json.loads((BASE/'p_arrays-questions.json').read_text());auth=json.loads((BASE/'p_arrays-authentic.json').read_text())
for q in auth:q['questionNumber']=q['qNumber']
bank='<h3 id="authentic-questions">Authentic array-reasoning bridge revisits</h3>'+''.join(item(q,i,True).replace('Authentic examination · checked English translation','Authentic bridge revisit · checked English adaptation') for i,q in enumerate(auth,1))
bank+='<h3 id="original-questions">Original and course-inspired mathematical/conceptual problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,3))
rules=[]
for block in (BASE/'p_arrays-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="arrays-lab"><form id="arrays-form"><label>Exact transformation<select name="mode"><option value="prefix">Prefix boundaries</option><option value="right">Overlap-safe rightward move</option><option value="bad">Counterexample: forward rightward move</option><option value="reverse">Pair-swap reversal</option><option value="difference">Original-neighbor differences</option><option value="compact">Stable compaction: retain even values</option></select></label><label>One to six comma-separated integers, each from minus twenty through twenty<input name="input" type="text" value="2,4,6,8,10,12" required></label><button type="submit">Restart exact trace</button></form><p id="arrays-output" aria-live="polite"></p><section class="concept-animation" id="arrays-player" data-loaded="true"></section><p>Rightward copy moves the original first n−1 values one slot right. The counterexample changes loop direction only. Reversal swaps symmetric pairs; differences preserve the first entry; compaction keeps only its stated logical prefix. Every checkpoint begins paused.</p></section>'''
source=(BASE/'p_arrays.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:arrays -->',lab)
for k,v in figures.items():source=source.replace('<!-- FIGURE:'+k+' -->',v)
body=text(source)
anchors=['sources','representation','layouts','c-semantics','traversals','mutation','python','strings','growth','packed','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==83 and body.count('class="review-rule"')==80
title='Arrays and Indexing'
nav=' '.join('<a href="#'+a+'">'+a.capitalize()+'</a>' for a in anchors)
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="p_arrays.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Programming Fundamentals · Week 2</p><h1>{title}</h1><p>Review draft · six reviewed university courses · 83 worked problems · 80 examination rules · 18 concept simulations</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="p_arrays.js"></script><script src="exam-calibration.js"></script></body></html>'
(ROOT/'dist/chapters/p_arrays.html').write_text(page,encoding='utf-8')
for part,name in [('source-audit','sources'),('quality-audit','quality')]:
 audit=text((BASE/f'p_arrays-{part}.md').read_text())
 (ROOT/f'dist/reviews/p_arrays-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Arrays chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/p_arrays.html">← Arrays chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());w=next(w for w in lessons if w['week']==2)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='p_arrays']+[dict(topicId='p_arrays',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/p_arrays.html',questionCount=83,authenticQuestionCount=2,originalQuestionCount=81,examNotesCount=80,sourceAuditUrl='reviews/p_arrays-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
p=ROOT/'dist/course-audit-week1.en.json';data=json.loads(p.read_text());reviewed=json.loads((BASE/'p_arrays-reviewed-courses.json').read_text());ids={c['id'] for c in reviewed}
data['courses']=[c for c in data['courses'] if c['id'] not in ids]+reviewed;data['reviewedAt']='2026-10-04';p.write_text(json.dumps(data,indent=2)+'\n')
from build_concept_animations import build_data,install_animations
build_data();install_animations()
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built sole arrays draft: 83 worked questions, 80 rules, seven figures, eighteen models and adjustable trace lab.')
