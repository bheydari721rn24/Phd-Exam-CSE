"""Reproducible chapter, separately authored questions, figures and audits."""
import ast,html,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
sys.path.insert(0,str(BASE/'exam-rewrite'))
import mathml
from mathml import markdown_math,render,width
md=MarkdownIt('commonmark',{'html':True}).enable('table')
# Only pure helpers are extracted; importing the overlay would rebuild other chapters.
tree=ast.parse((BASE/'exam-calibration/build.py').read_text(encoding='utf-8'))
for fn in tree.body:
    if isinstance(fn,ast.FunctionDef) and fn.name in ('compact_display','prep','text'):
        exec(compile(ast.Module(body=[fn],type_ignores=[]),'<shared native math layout>','exec'))
def scope_preserving_display(value):
    # Keep each complete equation together; its container handles narrow screens.
    # Actual matrix/case tables in the input retain their intended rows.
    return value
mathml.wrap_display=scope_preserving_display
base_render=mathml.render
def precise_render(s,display=False):
    # Multi-letter program variables are upright mathematical identifiers.
    s=re.sub(r'(?<![A-Za-z\\])(?:lo|hi|mid|lt|gt|parent)(?![A-Za-z])',lambda m:r'\mathrm{'+m.group()+'}',s)
    value=base_render(s,display)
    return value if display else '<span class="math-inline">'+value+'</span>'
mathml.render=precise_render
def e(s):return html.escape(str(s))
def label(x,y,s,size=24):return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}">{e(s)}</text>'
def rect(x,y,w,h,fill='#e6f0f4'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#83a6b0"/>'
def box(x,y,w,h,s):return rect(x,y,w,h)+label(x+w/2,y+h/2+8,s)
def arrow(x,y,a,b):
    return f'<path d="M{x},{y} L{a},{b}" stroke="#447986" stroke-width="2.5" fill="none"/>'+f'<circle cx="{a}" cy="{b}" r="4" fill="#447986"/>'
def fig(key,title,height,body,caption):
    return f'<figure class="logic-diagram correctness-diagram"><svg viewBox="0 0 700 {height}" role="img" aria-labelledby="correct-{key}"><title id="correct-{key}">{e(title)}</title>{body}</svg><figcaption>{e(caption)}</figcaption></figure>'
figures={}
b=box(210,25,280,50,'State and contract')
for x,s in [(20,'Preserved result'),(245,'Safe operations'),(470,'Strict progress')]:
    b+=arrow(350,75,x+105,125)+box(x,130,210,65,s)
b+=label(350,242,'All three obligations support the complete algorithm claim',23)
figures['obligations']=fig('obligations','Separate correctness, safety and termination obligations',275,b,'Figure 1. The postcondition, safe execution and a well-founded progress argument are separate proof obligations. A preserved result relation alone does not rule out an infinite loop or an unsafe access.')
b=label(350,35,'Lower bound: target 3 in [1, 3, 3, 3, 8, 9]',25)
for index,value in enumerate([1,3,3,3,8,9]):
    x=60+index*95;b+=rect(x,70,85,65,'#dcebdd' if index==0 else '#e5edf8')+label(x+42.5,111,str(value),29)+label(x+42.5,165,'index '+str(index),20)
b+=label(105,213,'Below target',22)+label(438,213,'At least target',22)
b+=label(350,265,'Exit: both boundaries are 1; unresolved width is 0',24)
figures['interval']=fig('interval','Classified regions at lower-bound termination',305,b,'Figure 2. The final left region contains only the one below-target value. The right region contains every duplicate three and every larger value. Coincident boundaries certify the first eligible index, rather than an arbitrary matching index.')
b=label(350,35,'Insert key 2 into prefix [1, 4, 2]',26)
for x,s in [(50,'1'),(250,'hole'),(450,'4')]:b+=box(x,90,160,70,s)
b+=box(250,220,160,60,'saved key 2')+arrow(330,220,330,170)
b+=label(350,330,'Ignore the hole: remaining records + saved key preserve the bag',22)
figures['hole']=fig('hole','Insertion-sort saved-key conservation during a shift',365,b,'Figure 3. The physical middle cell still contains a stale four after the shift. Treat it as a logical hole; the other records together with the saved two preserve the original prefix multiset. Restoring the saved key fills that hole.')
b=label(350,35,'Four regions before classifying the scan position',25)
for x,w,s,fill in [(20,150,'less','#dcebdd'),(175,150,'equal','#e5edf8'),(330,180,'unknown','#fff1d8'),(515,165,'greater','#eddfe9')]:
    b+=rect(x,80,w,70,fill)+label(x+w/2,123,s,25)
for x,s in [(20,'0'),(175,'lt'),(330,'i'),(515,'gt'),(680,'n')]:b+=label(x,184,s,24)
b+=label(350,232,'Greater branch: shrink gt; incoming value stays unknown',23)
b+=label(350,279,'Variant: unknown length decreases by one in every branch',23)
figures['partition']=fig('partition','Three-way partition regions and progress',315,b,'Figure 4. Boundaries describe half-open slices. A swap from the right unknown boundary does not classify the incoming scan value; the scan boundary remains in place until that value is inspected.')
b=label(350,35,'An attaining path and a universal path bound',25)
for x,s in [(60,'Root s'),(290,'a'),(520,'b')]:b+=box(x,95,120,65,s)
b+=arrow(180,127,290,127)+arrow(410,127,520,127)+label(235,94,'weight 4',21)+label(465,94,'weight −3',21)
b+=label(350,216,'Parent path gives an attainable distance of 1 to b',24)
b+=label(350,265,'All edge inequalities bound every competing path',24)
figures['certificate']=fig('certificate','Feasibility and optimality components of a path certificate',305,b,'Figure 5. The two displayed parent edges give a path of weight one. Verification also checks every other graph edge and checks that all parent chains end at the root. A path witness alone would not exclude a cheaper competing path.')

questions=json.loads((BASE/'a_correct-questions.json').read_text())
assert len(questions)==50
actual=json.loads((BASE/'exam-calibration/actual-items.json').read_text())
ids=['Phd_CE_1405_Q9','MS_CS_1393_Q167','Phd_CE_1405_Q3','Phd_CS_1405_Q20']
auth=[next(q for q in actual if q['id']==i) for i in ids]
assert all(q['translationStatus']=='checked against rendered source page' and q['answer'] is not None for q in auth)
def item(q,n,authentic=False):
    if authentic:
        from urllib.parse import quote
        url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
        provenance=f'<a href="{e(url)}">{e(q["booklet"].replace("_"," "))} · Q{q["questionNumber"]} · PDF page {q["pdfPage"]}</a>. Independently derived solution; not an official key.'
        kind='Authentic examination · English translation'
    else:
        provenance=e(q['origin']);kind='Original/course-derived problem · author-assessed '+q['difficulty'].lower()
    options=''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(o)+'</div></div>' for i,o in enumerate(q['options'],1))
    solution=text(q['solution']) if authentic else '<ol class="solution-steps">'+''.join('<li>'+text(step)+'</li>' for step in re.split(r'(?<=[.!?])\s+(?=[A-Z])',q['solution']))+'</ol>'
    return '<section class="exam-question" data-source-id="'+e(q['id'])+'" data-kind="'+('authentic' if authentic else 'original')+'" data-answer="'+str(q['answer'])+'"><h3>Question '+str(n)+'. '+e(q['title'])+'</h3><p class="exam-label">'+e(kind)+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])+'<div class="exam-options">'+options+'</div><details class="exam-solution"><summary>Read the complete solution and option analysis</summary><p><strong>Correct option: '+str(q['answer'])+'.</strong></p>'+solution+'</details></section>'
bank='<h3 id="authentic-questions">Authentic examination questions</h3>'
bank+=''.join(item(q,i,True) for i,q in enumerate(auth,1))
bank+='<h3 id="original-questions">Original and course-derived questions</h3>'
bank+=''.join(item(q,i) for i,q in enumerate(questions,5))
source=(BASE/'a_correct.en.md').read_text(encoding='utf-8').replace('48 original','50 original')
review_source=(BASE/'a_correct-review.en.md').read_text(encoding='utf-8')
review_source=re.sub(r'^### [A-E]\. ', '### ',review_source,flags=re.M)
review_html=[]
for paragraph in review_source.split('\n\n'):
    rules=re.findall(r'^(\d+)\. (.*)$',paragraph,re.M)
    if rules:
        review_html.extend('<section class="review-rule"><h4>Rule '+n+'</h4>'+text(content)+'</section>' for n,content in rules)
    else:review_html.append(text(paragraph))
source=source.replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(review_html))
for key,value in figures.items():source=source.replace(f'<!-- FIGURE:{key} -->',value)
lab='''<section class="lab" id="search-lab"><form id="search-form"><label>Sorted integer array<input id="search-array" value="1,3,3,3,8,9" placeholder="Leave empty for an empty array"></label><label>Target<input id="search-target" type="number" min="-999" max="999" step="1" value="3" required></label><label>Update rule<select id="search-mode"><option value="correct">Correct: discard the midpoint on the below-target branch</option><option value="faulty">Faulty: keep the midpoint on the below-target branch</option></select></label><button type="submit">Show the proof checkpoints</button></form><div class="lab-actions"><button type="button" data-search-preset="duplicates">Duplicates</button><button type="button" data-search-preset="empty">Empty input</button><button type="button" data-search-preset="stall">Minimal nontermination witness</button></div><div id="search-output" aria-live="polite"></div><p>Use zero through 24 sorted integers between negative 999 and 999. The target uses the same range. A repeated nonempty interval is reported as a stalling counterexample; the demonstration stops safely after detecting that repetition.</p></section>'''
source=source.replace('<!-- LAB:search -->',lab)
body=text(source)
anchors=['sources','contracts','backward','invariants','search','sorting','partition','arithmetic','certificates','problems','review','laboratory','references']
it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body,re.findall(r'.{0,90}(?:<!--|[$]).{0,90}',body)
assert len(re.findall(r'<section class="exam-question"',body))==54
review_source=(BASE/'a_correct-review.en.md').read_text()
assert len(re.findall(r'^\d+\. ',review_source,re.M))==74
title='Invariants, Correctness Certificates, and Method Comparison'
nav=' '.join(f'<a href="#{a}">{a.capitalize()}</a>' for a in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><meta name="description" content="Four reviewed university courses; deep algorithm proofs, 54 fully worked mathematical and conceptual questions, 74 complete notes, five original figures and a binary-search proof laboratory."><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="a_correct.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Algorithms · Week 2</p><h1>{title}</h1><p>Review draft · four reviewed universities · 54 worked questions · 74 complete examination notes</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="a_correct.js"></script><script src="exam-calibration.js"></script></body></html>'''
(ROOT/'dist/chapters/a_correct.html').write_text(page,encoding='utf-8')
for part,filename in [('source-audit','sources'),('quality-audit','quality')]:
    content=text((BASE/f'a_correct-{part}.md').read_text(encoding='utf-8'))
    out=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Algorithm correctness: {filename} audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/a_correct.html">← Algorithm correctness chapter</a></p><article class="lesson">{content}</article></main></body></html>'
    (ROOT/f'dist/reviews/a_correct-{filename}.html').write_text(out,encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());week=next(w for w in lessons if w['week']==2)
week['chapters']=[c for c in week['chapters'] if c['topicId']!='a_correct']+[dict(topicId='a_correct',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/a_correct.html',questionCount=54,authenticQuestionCount=4,originalQuestionCount=50,examNotesCount=74,sourceAuditUrl='reviews/a_correct-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+chr(10),encoding='utf-8')
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built a_correct: 54 worked questions, 74 notes, five original diagrams and native MathML.')
