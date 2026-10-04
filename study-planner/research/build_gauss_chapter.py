"""Build the sole Gaussian draft, preserving approved library content."""
import ast,html,json,re,sys,hashlib,tempfile,xml.etree.ElementTree as ET
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
b=label(350,30,'Same intersection before and after elimination',22)
cx,cy,sx,sy=250,280,85,55
b+=line(80,cy,610,cy)+line(cx,335,cx,55)
for pts,col,dash in [([(-1,0),(3,4)],'#527fa2',''),([(0,4),(2.5,-1)],'#b17616',''),([(-1,2),(3,2)],'#287f68',' stroke-dasharray="6 4"')]:
 b+='<polyline points="'+' '.join(f'{cx+sx*x},{cy-sy*y}' for x,y in pts)+'" fill="none" stroke="'+col+'" stroke-width="3"'+dash+'/>'
b+=f'<circle cx="{cx+sx}" cy="{cy-2*sy}" r="6" fill="#a43e61"/>'
b+=label(390,150,'(1, 2)',22)+label(505,75,'x − y = −1',21)+label(515,240,'6y = 12',21)+label(405,355,'4x + 2y = 8',21)+label(590,305,'x',21)+label(230,70,'y',21)
figures['geometry']=fig('gauss-geometry','Two original lines and their eliminated equation',390,b,'Figure 1. Blue and amber are the original equations. The dashed green eliminated equation and the unchanged blue line retain the same red intersection. Coordinate scales are fixed within the figure.')
b=label(350,30,'Every complete row operation has an inverse')
b+=box(35,90,270,65,'original array M₀')+box(395,90,270,65,'current array M')+line(305,122,395,122)+label(350,105,'T',23)
b+=box(35,230,270,65,'identity I')+box(395,230,270,65,'recorded transform T')+line(305,262,395,262)+label(350,245,'same',19)
b+=label(350,350,'M = T M₀; reverse with T⁻¹',25)
figures['certificate']=fig('gauss-certificate','Synchronized exact matrix transformation',385,b,'Figure 2. The same operations applied to an identity array record the entire invertible left transform. Multiplying that record by the original augmented array must reproduce the current array exactly.')
b=label(350,30,'Coefficients 1–4; last column is a load',23)
arr=[[1,2,0,-1,3],[0,0,1,3,-2],[0,0,0,0,0]]
for i,row in enumerate(arr):
 for j,v in enumerate(row):
  x=110+120*j;y=100+75*i
  b+=label(x,y,str(v),26)
  if (i,j) in [(0,0),(1,2)]:b+=f'<circle cx="{x}" cy="{y-8}" r="24" fill="none" stroke="#2b8068" stroke-width="3"/>'
b+=line(530,55,530,265)
for x,t in [(110,'pivot'),(230,'free'),(350,'pivot'),(470,'free'),(590,'load')]:b+=label(x,300,t,22)
figures['pivots']=fig('gauss-pivots','Nonconsecutive coefficient pivot columns',340,b,'Figure 3. Circled leading ones identify coefficient columns one and three. Columns two and four are free; the last column is never an additional unknown.')
b=label(350,30,'Affine solution set: x + y = 3',24)+line(90,300,620,300)+line(150,320,150,60)
b+='<path d="M150,120 L510,300" stroke="#377e83" stroke-width="3"/><path d="M510,300 L390,240" stroke="#b17616" stroke-width="4"/>'
b+='<circle cx="510" cy="300" r="7" fill="#a44061"/><circle cx="390" cy="240" r="7" fill="#287f68"/>'
b+=label(530,340,'xₚ = (3, 0)',22)+label(375,210,'xₚ + v = (2, 1)',21)+label(360,85,'v = (−1, 1)',23)+label(110,125,'3',21)+label(160,340,'0',21)+label(590,325,'x',21)+label(125,65,'y',21)
figures['affine']=fig('gauss-affine','A particular point and one homogeneous direction',380,b,'Figure 4. The shown line is a two-dimensional illustration with one free coordinate. Adding any real multiple of the homogeneous direction to the particular point gives every point on the line; higher-dimensional families follow the same algebra.')
b=label(350,30,'A load mismatch survives coefficient cancellation',22)
b+=box(60,85,580,60,'row 1: x + 2y − z = 1')+box(60,185,580,60,'row 2: 2x + 4y − 2z = 3')+label(350,285,'row 2 − 2 × row 1 → 0 = 1',24)+label(350,345,'w = (−2, 1):  wᵀA = 0,  wᵀb = 1',22)
figures['contradiction']=fig('gauss-contradiction','An original-equation inconsistency witness',385,b,'Figure 5. Combining equations with the displayed row weights cancels every coefficient but leaves a nonzero load. The witness refutes every possible unknown vector, not just a guessed solution.')
b=box(80,35,540,60,'inspect α and α + 2 before division')
for x,t,c in [(20,'α = 0','#efbfd0'),(250,'α = −2','#ffda87'),(480,'α ≠ 0, −2','#bee4d0')]:
 b+=box(x,155,200,60,t,c)+line(350,95,x+100,155)
for x,t in [(20,'contradiction'),(250,'one free coordinate'),(480,'unique solution')]:b+=box(x,275,200,60,t)
figures['branches']=fig('gauss-branches','Exceptional values from undivided equations',375,b,'Figure 6. This tree classifies the specific three-variable Oxford comparison family, not every parameter system. The two exceptional values have different load compatibility and therefore different outcomes.')
b=label(350,30,'A stage-two row exchange must move earlier L entries',22)
for y,left,right in [(90,'old row 2: 1/2','old row 3: 1/4'),(245,'new row 2: 1/4','new row 3: 1/2')]:
 b+=box(30,y,280,65,left)+box(390,y,280,65,right)
b+=line(170,155,530,245)+line(530,155,170,245)+label(350,365,'Exchange completed columns only; verify P A = L U',22)
figures['plu']=fig('gauss-plu','Persistent earlier multiplier bookkeeping',400,b,'Figure 7. In the chapter example, row three supplies the second pivot and moves above row two. Its earlier first-column multiplier moves with it. The unit diagonal of L is retained, and its unfilled later columns are not exchanged.')
figures={k:v.replace('conditional-diagram','gauss-diagram') for k,v in figures.items()}
questions=json.loads((BASE/'l_gauss-questions.json').read_text())
actual=json.loads((BASE/'l_gauss-authentic.json').read_text())
bank='<h3 id="authentic-questions">Authentic examination questions and an explicit revisit</h3>'+''.join(item(q,i,True) for i,q in enumerate(actual,1))
bank+='<h3 id="original-questions">Original and course-derived mathematical problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,3))
rules=[]
for block in (BASE/'l_gauss-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="gauss-lab"><form id="gauss-form"><label>Augmented matrix: one equation per line, last entry is its load<textarea name="matrix" spellcheck="false" required>0 2 1 1
1 -1 1 2
2 1 -1 0</textarea></label><button type="submit">Compute exact elimination</button></form><div class="lab-actions">'''+''.join(f'<button type="button" data-gauss-preset="{k}">{v}</button>' for k,v in [('unique','Unique with a swap'),('free','Skipped early column'),('affine','Two free coordinates'),('inconsistent','Contradiction'),('fractions','Rational coefficients'),('zero','Zero equations')])+'''</div><div class="gauss-step-controls"><button type="button" data-gauss-step="back">Previous operation</button><button type="button" data-gauss-step="next">Next operation</button><button type="button" data-gauss-step="reset">Return to original</button></div><div id="gauss-output" aria-live="polite"></div><p>Accepts one to four rows, one to four coefficient columns and one final load column. All rows must have equal length. Inputs are integers or fractions with numerator and denominator magnitude at most 100,000 and a nonzero denominator. All subsequent arithmetic uses exact integer fractions. Zero-load identity rows are allowed; a zero coefficient row with nonzero load proves inconsistency.</p></section>'''
source=(BASE/'l_gauss.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:gauss -->',lab)
for key,value in figures.items():source=source.replace(f'<!-- FIGURE:{key} -->',value)
body=text(source)
anchors=['sources','geometry','operations','elimination','solutions','canonical','parameters','factorization','inverses','numerics','fields','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==71 and body.count('class="review-rule"')==80
title='Gaussian Elimination and Linear Systems'
nav=' '.join('<a href="#'+a+'">'+a.capitalize()+'</a>' for a in anchors)
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="l_gauss.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Linear Algebra · Week 2</p><h1>{title}</h1><p>Review draft · five reviewed university courses · 71 worked problems · 80 examination rules · 12 exact simulations</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="l_gauss.js"></script><script src="exam-calibration.js"></script></body></html>'
(ROOT/'dist/chapters/l_gauss.html').write_text(page,encoding='utf-8')
for part,name in [('source-audit','sources'),('quality-audit','quality')]:
 audit=text((BASE/f'l_gauss-{part}.md').read_text())
 (ROOT/f'dist/reviews/l_gauss-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Gaussian elimination audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/l_gauss.html">← Gaussian elimination chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());w=next(w for w in lessons if w['week']==2)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='l_gauss']+[dict(topicId='l_gauss',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/l_gauss.html',questionCount=71,authenticQuestionCount=2,originalQuestionCount=69,examNotesCount=80,sourceAuditUrl='reviews/l_gauss-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
register=ROOT/'dist/course-audit-week1.en.json';data=json.loads(register.read_text())
reviewed=json.loads((BASE/'l_gauss-reviewed-courses.json').read_text());ids={c['id'] for c in reviewed}
data['courses']=[c for c in data['courses'] if c['id'] not in ids]+reviewed
data['reviewedAt']='2026-10-04';data['scope']='Chapter-specific course entries across the authored weeks; each entry states its actual reading boundary.'
register.write_text(json.dumps(data,indent=2)+'\n')
cache=Path(tempfile.gettempdir())/'phd-gauss-sources'
records=[]
for path in cache.glob('*acquisition.json'):records+=json.loads(path.read_text())
records={r['id']:r for r in records if 'sha256' in r}
for n,u in [('stanford-plu3','permuted_lu16.html'),('stanford-plu4','permuted_lu32.html'),('stanford-plu5','permuted_lu64.html')]:
 data=(cache/(n+'.html')).read_bytes();records[n]=dict(id=n,url='https://web.stanford.edu/class/math114/decks/linear_systems/'+u,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),pages=None)
for record in records.values():record.pop('cache',None)
evidence=ROOT/'dist/evidence/l_gauss';evidence.mkdir(parents=True,exist_ok=True)
(evidence/'sources.json').write_text(json.dumps(dict(candidateCourses=5,primaryUniversities=['MIT','Oxford','Stanford','UC Berkeley'],additionalUniversity='CMU',reviewedScope={'mit':'all 21 PDF pages','oxford':'printed 3–7,16–20; adjoining printed 8 inspected','berkeley':'all seven handwritten pages, visually read','cmu':'all nine pages of Days 1,2,8','stanford':'all eleven linked Gaussian/LU/Permuted-LU bodies'},documents=list(records.values()),limits='Bounded five-course accessible written pool; no whole-world or inaccessible-homework claim.'),indent=2)+'\n')
from build_concept_animations import build_data,install_animations
build_data();install_animations()
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built Gaussian draft: 71 fully worked tasks, 80 complete rules, seven original figures, twelve simulations.')
