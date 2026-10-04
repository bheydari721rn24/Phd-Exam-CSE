"""Single-chapter renderer with native math, original figures and a real lab."""
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
b=label(350,30,'Input and output are different ambient spaces')
b+=box(25,85,285,65,'input: Fⁿ')+box(390,85,285,65,'output: Fᵐ')+line(310,117,390,117)+label(350,100,'A',23)
b+=box(25,205,285,65,'kernel: dimension n − r')+box(390,205,285,65,'image: dimension r')
b+=label(350,350,'rank ≤ min(m, n)',25)
figures['spaces']=fig('rank-spaces','Domain and output dimensions',390,b,'Figure 1. The kernel is a set of input vectors, while the image is a set of output vectors. Rank–nullity counts domain dimensions; left nullity uses the output dimension separately.')
b=label(350,30,'Original pivot indices select original columns',23)
for j,txt in enumerate(['a₁','a₂ = 2a₁','a₃','a₄ = a₁ + a₃','a₅']):
 b+=box(10+140*j,95,120,65,txt,'#bee4d0' if j in [0,2,4] else '#e6f0f4')
b+=box(70,230,560,65,'column basis: a₁, a₃, a₅')+label(350,350,'Reduced columns locate indices; original columns give vectors',21)
figures['pivots']=fig('rank-pivots','Independent and dependent original columns',390,b,'Figure 2. In the Berkeley four-by-five example, columns two and four add no output direction. Green original columns form a basis, and the same dependency coefficients survive reduction.')
b=label(350,30,'Two different loads give parallel, disjoint fibers',23)+line(60,315,650,315)+line(130,345,130,65)
b+='<path d="M130,180 L400,315" stroke="#287f68" stroke-width="3"/><path d="M130,90 L580,315" stroke="#b17616" stroke-width="3"/>'
b+=label(375,155,'x + y = 3',23)+label(535,235,'x + y = 5',23)+label(520,85,'common direction (1, −1)',22)
figures['fibers']=fig('rank-fibers','Parallel solution fibers in the input plane',380,b,'Figure 3. Every shown point belongs to a nonempty fiber of the same map. The output values differ, so the fibers cannot intersect. Their direction spaces are the same kernel line.')
b=label(350,30,'Four spaces, two separate decompositions',24)
for x,y,t,c in [(30,95,'row space: r','#bee4d0'),(365,95,'kernel: n − r','#ffda87'),(30,240,'column space: r','#bee4d0'),(365,240,'left kernel: m − r','#ffda87')]:b+=box(x,y,305,65,t,c)
b+=label(350,195,'orthogonal pair inside Rⁿ',22)+label(350,345,'orthogonal pair inside Rᵐ',22)
figures['four']=fig('rank-four','Four real fundamental spaces',390,b,'Figure 4. Each row shows a pair of complementary subspaces in its own ambient Euclidean space. Do not add a column-space vector to a kernel vector when their ambient dimensions differ.')
b=label(350,30,'The identity acts on the space named by its subscript',22)
b+=box(30,100,260,65,'L A = Iₙ: left inverse')+box(410,100,260,65,'A R = Iₘ: right inverse')
b+=box(30,240,260,65,'injective; r = n')+box(410,240,260,65,'onto; r = m')
b+=label(350,360,'Both conditions coincide for finite square matrices',22)
figures['inverse']=fig('rank-inverse','Inverse directions and rank conditions',405,b,'Figure 5. The order of multiplication determines which coordinates are recovered. A genuinely rectangular matrix can satisfy one of these full-rank conditions without satisfying the other.')
b=label(350,30,'Rank factorization of a three-by-three matrix',23)
b+=box(20,115,190,70,'x: 3 coordinates')+box(255,115,190,70,'F x: 2 coordinates')+box(490,115,190,70,'C F x: 3 coordinates')
b+=line(210,150,255,150)+line(445,150,490,150)+label(350,285,'C has two independent columns; F has two independent rows',21)+label(350,350,'The minimal bottleneck dimension equals rank',24)
figures['factor']=fig('rank-factor','Exact factorization through the image dimension',390,b,'Figure 6. The product recovers every output through two intermediate coordinates. Three output entries do not mean three independent output directions.')
b=label(350,30,'Apply A only to the image reached by B',24)
b+=box(35,95,300,65,'image of B: dimension s')+box(365,95,300,65,'intersection with ker A: k')
b+=box(125,245,450,65,'rank of A B = s − k')
b+=label(350,365,'Intermediate alignment decides which directions are lost',21)
figures['composition']=fig('rank-composition','Exact composition rank by a restricted kernel',410,b,'Figure 7. The killed part is an intersection in the common intermediate space. Knowing factor ranks bounds this dimension but does not usually determine it.')
figures={k:v.replace('conditional-diagram','rank-diagram') for k,v in figures.items()}
questions=json.loads((BASE/'l_rank-questions.json').read_text());auth=json.loads((BASE/'l_rank-authentic.json').read_text())
bank='<h3 id="authentic-questions">Authentic archive revisits</h3>'+''.join(item(q,i,True) for i,q in enumerate(auth,1))
bank+='<h3 id="original-questions">Original and written-course problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,3))
rules=[]
for block in (BASE/'l_rank-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="rank-lab"><form id="rank-form"><label>Coefficient matrix: one row per line; every column is an input coordinate<textarea name="matrix" spellcheck="false" required>1 2 0 1 0
0 0 1 1 0
1 2 0 1 1
-1 -2 0 -1 0</textarea></label><button type="submit">Compute all four spaces</button></form><div class="lab-actions">'''+''.join(f'<button type="button" data-rank-preset="{k}">{v}</button>' for k,v in [('pivot','Nonconsecutive pivots'),('tall','Injective tall map'),('wide','Surjective wide map'),('zero','Zero map'),('fractions','Exact fractions'),('exceptional','Exceptional rank one')])+'''</div><div class="rank-step-controls"><button type="button" data-rank-step="back">Previous operation</button><button type="button" data-rank-step="next">Next operation</button><button type="button" data-rank-step="reset">Return to original</button></div><div id="rank-output" aria-live="polite"></div><p>Accepts one to five rows and one to five columns of equal length. Use integers or exact fractions with numerator and denominator magnitude at most 100,000 and nonzero denominators. This is a coefficient matrix: no final load column is assumed. All arithmetic uses exact integer fractions.</p></section>'''
source=(BASE/'l_rank.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:rank -->',lab)
for k,v in figures.items():source=source.replace('<!-- FIGURE:'+k+' -->',v)
body=text(source)
anchors=['sources','spaces','reduction','nullity','solutions','inverses','factorization','inequalities','parameters','structures','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==90 and body.count('class="review-rule"')==80
title='Rank, Invertibility, and Solution Sets'
nav=' '.join('<a href="#'+a+'">'+a.capitalize()+'</a>' for a in anchors)
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="l_rank.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Linear Algebra · Week 2</p><h1>{title}</h1><p>Review draft · five reviewed university courses · 90 worked problems · 80 examination rules · 12 concept simulations</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="l_rank.js"></script><script src="exam-calibration.js"></script></body></html>'
(ROOT/'dist/chapters/l_rank.html').write_text(page,encoding='utf-8')
for part,name in [('source-audit','sources'),('quality-audit','quality')]:
 audit=text((BASE/f'l_rank-{part}.md').read_text())
 (ROOT/f'dist/reviews/l_rank-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rank chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/l_rank.html">← Rank chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());w=next(w for w in lessons if w['week']==2)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='l_rank']+[dict(topicId='l_rank',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/l_rank.html',questionCount=90,authenticQuestionCount=2,originalQuestionCount=88,examNotesCount=80,sourceAuditUrl='reviews/l_rank-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
register=ROOT/'dist/course-audit-week1.en.json';data=json.loads(register.read_text());reviewed=json.loads((BASE/'l_rank-reviewed-courses.json').read_text());ids={c['id'] for c in reviewed}
data['courses']=[c for c in data['courses'] if c['id'] not in ids]+reviewed;data['reviewedAt']='2026-10-04';register.write_text(json.dumps(data,indent=2)+'\n')
from build_concept_animations import build_data,install_animations
build_data();install_animations()
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built one rank draft: 90 worked questions, 80 rules, seven figures, twelve simulations.')
