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
b=label(350,30,'One caller waits; helper invocations are sequential',22)
b+=box(35,85,275,65,'combine: first pending')+box(390,85,275,65,'affine(2) → 7')+line(310,117,390,117)
b+=box(35,220,275,65,'combine: first = 7')+box(390,220,275,65,'affine(7) → 22')+line(310,252,390,252)
b+=label(350,350,'combine returns 7 + 22 = 29',23)
figures['frames']=fig('functions-frames','Sequential nested helper frames',390,b,'Figure 1. combine remains active while each helper executes. The first helper ends before the second starts; total invocations and maximum active depth therefore differ.')
b=label(350,30,'Three separate quantities in one scalar call',23)
b+=box(20,100,200,65,'caller a = 4')+box(250,100,200,65,'parameter x = 4')+box(480,100,200,65,'local x = 7')
b+=line(220,132,250,132)+line(450,132,480,132)+box(215,245,270,65,'returned result = 14')
b+=label(350,370,'Caller a stays 4; only the copied parameter changes',22)
figures['copy']=fig('functions-copy','Copy state and returned result',410,b,'Figure 2. A value is transferred to a new parameter object. Adding three changes only that parameter; returning twice its value supplies fourteen to a different caller destination.')
b=label(350,30,'Lexical environment is not the active call tree',22)
b+=box(30,100,280,65,'file object x = 10')+box(390,100,280,65,'caller local x = 3')
b+=box(175,250,350,65,'read_x selects file object')
b+=line(350,250,170,165)+label(350,375,'read_x() + caller x = 13',23)
figures['scope']=fig('functions-scope','Lexical lookup and caller continuation',410,b,'Figure 3. The separately defined helper resolves its free name at file scope. Its caller contributes another value only after the helper returns to the caller continuation.')
b=label(350,30,'Two copied pointers; one shared target',23)
b+=box(30,90,250,65,'parameter p → a')+box(420,90,250,65,'parameter q → a')
b+=box(225,240,250,65,'a: 4 → 6 → 18')+line(155,155,350,240)+line(545,155,350,240)
b+=label(350,380,'The second statement reads the first statement’s update',21)
figures['alias']=fig('functions-alias','Alias-mediated sequential composition',415,b,'Figure 4. Adding two and then tripling act on one target. Distinct targets would have a different two-coordinate result, so object identity must be established before calculation.')
b=label(350,30,'Two permitted alternatives from the same initial state',21)
b+=box(25,95,300,65,'left call 1; right call 2')+box(375,95,300,65,'right call 1; left call 2')
b+=box(25,235,300,65,'difference = −1')+box(375,235,300,65,'difference = 1')
b+=line(175,160,175,235)+line(525,160,525,235)+label(350,370,'counter ends at 2 in both branches',23)
figures['orders']=fig('functions-orders','C17 indeterminately sequenced helper bodies',405,b,'Figure 5. Each next body completes before the other starts, but the language permits either order. These defined alternatives must not be confused with directly unsequenced argument increments.')
b=label(350,30,'Modular reasoning across a function boundary',23)
b+=box(30,90,280,65,'caller proves precondition')+box(390,90,280,65,'callee assumes it')+line(310,122,390,122)
b+=box(30,245,280,65,'caller uses postcondition')+box(390,245,280,65,'callee proves each return')+line(390,277,310,277)
b+=label(350,375,'Frame conditions and termination are separate obligations',21)
figures['contracts']=fig('functions-contracts','Caller and callee proof obligations',410,b,'Figure 6. The caller establishes valid inputs; the callee establishes the promised result. Effects and termination need explicit guarantees before this proof can justify replacing a call.')
b=label(350,30,'A shared object survives a local rebinding',23)
b+=box(20,90,250,65,'caller data → original')+box(430,90,250,65,'local values → new')
b+=box(20,255,250,65,'original list: [2, 7]')+box(430,255,250,65,'new list: [99]')
b+=line(145,155,145,255)+line(555,155,555,255)+label(350,385,'Mutation affected the original; rebinding selected another object',20)
figures['sharing']=fig('functions-sharing','Python object mutation versus name rebinding',420,b,'Figure 7. append changes the original list while caller and parameter share it. A later local assignment selects a new object without redirecting the caller name.')
figures={k:v.replace('conditional-diagram','functions-diagram') for k,v in figures.items()}
questions=json.loads((BASE/'p_functions-questions.json').read_text());auth=json.loads((BASE/'p_functions-authentic.json').read_text())
for q in auth:q['questionNumber']=q['qNumber']
bank='<h3 id="authentic-questions">Authentic call-semantics bridge revisits</h3>'+''.join(item(q,i,True).replace('Authentic examination · checked English translation','Authentic bridge revisit · checked English adaptation') for i,q in enumerate(auth,1))
bank+='<h3 id="original-questions">Original and course-inspired mathematical/conceptual problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,3))
rules=[]
for block in (BASE/'p_functions-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="functions-lab"><form id="functions-form"><label>Exact model<select name="mode"><option value="copy">Scalar copy: local add three, return twice</option><option value="pointer">Pointer: write twice the target plus three</option><option value="alias">Aliases: add two, then triple the same target</option><option value="static">Three calls: fresh local and persistent saved state</option><option value="nested">Nested body: two sequential affine calls</option></select></label><label>Initial caller integer: -20 through 20<input name="input" type="text" inputmode="numeric" value="4" required></label><button type="submit">Restart exact trace</button></form><p id="functions-output" aria-live="polite"></p><section class="concept-animation" id="functions-player" data-loaded="true"></section><p>Static model: each of three calls resets fresh to zero, increments it, adds the input to saved (initially zero), and returns 10 × fresh + saved. Negative inputs are valid for every listed nonrecursive model. Laboratory transitions are integer-exact and begin paused.</p></section>'''
source=(BASE/'p_functions.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:functions -->',lab)
for k,v in figures.items():source=source.replace('<!-- FIGURE:'+k+' -->',v)
body=text(source)
anchors=['sources','interfaces','frames','values','scope','pointers','order','contracts','callbacks','python','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==91 and body.count('class="review-rule"')==80
title='Functions, Variable Scope, and Parameter Passing'
nav=' '.join('<a href="#'+a+'">'+a.capitalize()+'</a>' for a in anchors)
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="p_functions.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Programming Fundamentals · Week 2</p><h1>{title}</h1><p>Review draft · six reviewed university courses · 91 worked problems · 80 examination rules · 12 concept simulations</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="p_functions.js"></script><script src="exam-calibration.js"></script></body></html>'
(ROOT/'dist/chapters/p_functions.html').write_text(page,encoding='utf-8')
for part,name in [('source-audit','sources'),('quality-audit','quality')]:
 audit=text((BASE/f'p_functions-{part}.md').read_text())
 (ROOT/f'dist/reviews/p_functions-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Functions chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/p_functions.html">← Functions chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());w=next(w for w in lessons if w['week']==2)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='p_functions']+[dict(topicId='p_functions',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/p_functions.html',questionCount=91,authenticQuestionCount=2,originalQuestionCount=89,examNotesCount=80,sourceAuditUrl='reviews/p_functions-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
p=ROOT/'dist/course-audit-week1.en.json';data=json.loads(p.read_text());reviewed=json.loads((BASE/'p_functions-reviewed-courses.json').read_text());ids={c['id'] for c in reviewed}
data['courses']=[c for c in data['courses'] if c['id'] not in ids]+reviewed;data['reviewedAt']='2026-10-04';p.write_text(json.dumps(data,indent=2)+'\n')
from build_concept_animations import build_data,install_animations
build_data();install_animations()
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built sole functions draft: 91 worked questions, 80 rules, seven figures, twelve models and adjustable trace lab.')
