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
from combin_math_layout import wrap
mathml.wrap_display=wrap
figures={}
b=label(350,30,'Specify priority before simplifying',23)
for k,t in enumerate(['E=0 → G₁=G₀=0','E=1, R₁=1 → G₁=1, G₀=0','E=1, R₁=0 → G₀=R₀']):b+=box(90,85+95*k,520,65,t)
figures['contract']=fig('combin-contract','Three exhaustive priority cases',410,b,'Figure 1. The three mutually exclusive cases cover every input. Simultaneous requests belong to the second case and cannot assert both grants.')
b=label(350,30,'A directed acyclic network shares r',23)
for x,y,w,h,t in [(35,100,170,60,'p = AB'),(35,235,170,60,'q = C + D'),(265,167,170,60,'r = pq'),(495,100,170,60,'Y = r + E'),(495,235,170,60,'Z = r ⊕ H')]:b+=box(x,y,w,h,t)
for coords in [(205,130,265,197),(205,265,265,197),(435,197,495,130),(435,197,495,265)]:b+=line(*coords)
b+=label(350,355,'Rank: inputs 0; p,q 1; r 2; Y,Z 3',21)
figures['dag']=fig('combin-dag','Shared-net dependency graph',390,b,'Figure 2. Arrows represent dependency, not execution order in a source file. The same internal r drives both observed outputs.')
b=label(350,30,'Factor common products under a declared library',22)
b+=box(90,85,520,65,'adf + aef + bdf + bef + cdf + cef + g')
b+=line(350,150,350,205)+box(90,205,520,65,'(a + b + c)(d + e)f + g')
b+=label(350,325,'Wide-gate cost: 7 → 4; two-input mapping differs',20)
figures['sharing']=fig('combin-sharing','Factoring with explicit fan-in assumptions',370,b,'Figure 3. The two forms are functionally equal. Gate count and depth depend on whether wide gates are available, so literal savings alone cannot certify mapped cost.')
b=label(350,30,'Read each residual pair in C=0, C=1 order',22)
for k,(s,p,t) in enumerate([('00','01','C'),('01','11','1'),('10','01','C'),('11','01','C')]):
 y=105+60*k;b+=label(130,y,'AB='+s,21)+label(350,y,'output pair '+p,21)+label(585,y,'D'+str(k)+'='+t,21)
b+=label(350,375,'F = Σm(1,2,3,5,7) = C + A̅B',22)
figures['cofactor']=fig('combin-cofactor','Cofactor table becomes mux wiring',415,b,'Figure 4. Each data function is determined by two original truth rows. Select-bit order controls which pin receives each function.')
b=label(350,30,'Eight addresses; two independent output columns',22)
words=['00','10','10','01','10','01','01','11']
for i,w in enumerate(words):
 x=60+160*(i%4);y=90+110*(i//4);b+=box(x,y,135,75,format(i,'03b')+' → '+w)
b+=label(350,345,'Word order: odd parity, then majority; 16 stored bits',20)
figures['rom']=fig('combin-rom','Explicit multi-output ROM contents',385,b,'Figure 5. The address sequence retains ABC significance and each word retains parity/majority order. A shared row decoder feeds separate output columns.')
b=label(350,30,'Two complemented products feed a final NAND',22)
b+=box(40,100,240,60,'p = (AB)̅')+box(40,245,240,60,'q = (AC)̅')+box(390,172,260,60,'Y = (pq)̅')
b+=line(280,130,390,202)+line(280,275,390,202)
b+=label(350,370,'Y = AB + AC = A(B + C)',23)
figures['polarity']=fig('combin-polarity','A verified three-NAND mapping',410,b,'Figure 6. Each block names its complemented internal signal. This mapping uses three two-input NAND gates without free primary-input complements.')
b=label(350,30,'Every output discrepancy contributes to the miter',22)
b+=box(40,100,260,60,'reference F₀, F₁')+box(400,100,260,60,'candidate G₀, G₁')
b+=box(110,240,210,60,'e₀ = F₀ ⊕ G₀')+box(380,240,210,60,'e₁ = F₁ ⊕ G₁')
b+=line(170,160,215,240)+line(530,160,485,240)+label(350,365,'M = e₀ + e₁; care equivalence requires CM = 0',21)
figures['miter']=fig('combin-miter','Complete multi-output comparison',410,b,'Figure 7. Equivalence means no allowed input makes any corresponding output differ. A passing comparison of only one output is insufficient.')
b=label(350,30,'Timing recurrences use different extrema',22)
for k,(t,lo,hi) in enumerate([('primary',0,0),('p = AB',1,3),('q = p + C',2,7),('Y = qD',1,9)]):
 y=95+65*k;b+=label(140,y,t,22)+label(365,y,'earliest '+str(lo),21)+label(580,y,'latest '+str(hi),21)
b+=label(350,395,'Bounds are structural; a masked transition may not occur',20)
figures['timing']=fig('combin-timing','Contamination and propagation bounds',435,b,'Figure 8. Gate intervals are (1,3), (2,4), (1,2). The fastest structural route enters at D, while the longest route enters at A or B.')
figures={k:v.replace('conditional-diagram','combin-diagram') for k,v in figures.items()}
for k,v in figures.items():
 marker='combin-arrow-'+k
 v=v.replace('<path ',f'<path marker-end="url(#{marker})" ')
 pos=v.index('>')+1
 # Definitions belong inside the SVG, not the outer figure.
 pos=v.index('>',v.index('<svg'))+1
 v=v[:pos]+f'<defs><marker id="{marker}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#447986"/></marker></defs>'+v[pos:]
 figures[k]=v
questions=json.loads((BASE/'g_combin-questions.json').read_text());auth=json.loads((BASE/'g_combin-authentic.json').read_text())
for q in auth:q['questionNumber']=q['qNumber']
bank='<h3 id="authentic-questions">Authentic netlist and cofactor-design revisits</h3>'+''.join(item(q,i,True).replace('Authentic examination · checked English translation','Authentic bridge revisit · checked English adaptation') for i,q in enumerate(auth,1))
bank=bank.replace('<strong>Correct option: None.</strong>', '<strong>Convention-sensitive tutorial; no unqualified single answer.</strong>')
bank+='<h3 id="original-questions">Original and course-inspired mathematical/conceptual problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,3))
rules=[]
for block in (BASE/'g_combin-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab="""<section class="lab" id="combin-lab"><form id="combin-form"><label>Circuit family<select name="mode"><option value="shared">Shared multi-output circuit</option><option value="priority">Priority controller</option><option value="nand">Three-NAND mapping of A(B+C)</option></select></label><label>Candidate<select name="variant"><option value="correct">Correct implementation</option><option value="faulty">Faulty implementation</option></select></label><div class="bit-inputs"><label>A<select name="a"><option>0</option><option selected>1</option></select></label><label>B<select name="b"><option>0</option><option selected>1</option></select></label><label>C<select name="c"><option selected>0</option><option>1</option></select></label><label>D<select name="d"><option>0</option><option selected>1</option></select></label></div><button type="submit">Recompute complete table and restart trace</button></form><div id="combin-output" aria-live="polite"></div><section class="concept-animation" id="combin-player" data-loaded="true"></section></section>"""
source=(BASE/'g_combin.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:combin -->',lab)
for k,v in figures.items():source=source.replace('<!-- FIGURE:'+k+' -->',v)
body=text(source)
anchors=['sources','contract','netlists','structure','cofactors','mapping','hdl','verification','timing','case-studies','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='Combinational Circuit Design'
nav=' '.join('<a href="#'+a+'">'+a.capitalize()+'</a>' for a in anchors)
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="g_combin.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Digital Logic · Week 2</p><h1>{title}</h1><p>Review draft · five reviewed university courses · 82 worked problems · 80 examination rules · 14 concept simulations</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="g_combin.js"></script><script src="exam-calibration.js"></script></body></html>'
(ROOT/'dist/chapters/g_combin.html').write_text(page,encoding='utf-8')
for part,name in [('source-audit','sources'),('quality-audit','quality')]:
 audit=text((BASE/f'g_combin-{part}.md').read_text())
 (ROOT/f'dist/reviews/g_combin-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Combinational circuit design chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/g_combin.html">← Combinational circuit design chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());w=next(w for w in lessons if w['week']==2)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='g_combin']+[dict(topicId='g_combin',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/g_combin.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/g_combin-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
p=ROOT/'dist/course-audit-week1.en.json';data=json.loads(p.read_text());reviewed=json.loads((BASE/'g_combin-reviewed-courses.json').read_text());ids={c['id'] for c in reviewed}
data['courses']=[c for c in data['courses'] if c['id'] not in ids]+reviewed;data['reviewedAt']='2026-10-04';p.write_text(json.dumps(data,indent=2)+'\n')
from build_concept_animations import build_data,install_animations
build_data();install_animations()
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built sole combinational-design draft: 82 worked tasks, 80 rules, eight figures, fourteen models and an editable verification lab.')
