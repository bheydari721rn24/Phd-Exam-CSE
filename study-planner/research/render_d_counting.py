"""Render only the new counting chapter and its audit pages."""
from pathlib import Path
from html import escape as e
import ast,json,re,sys,hashlib,xml.etree.ElementTree as ET
from markdown_it import MarkdownIt
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
sys.path.insert(0,str(BASE/'exam-rewrite'))
import mathml
mathml.SYMBOLS['ell']='ℓ'
from mathml import render,width,markdown_math
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
# Obtain pure helpers without executing another chapter's rebuild.
for filename,names in [('build_correct_chapter.py',('scope_preserving_display',)),('exam-calibration/build.py',('prep','text')),('build_conditional_chapter.py',('item',))]:
    for f in ast.parse((BASE/filename).read_text(encoding='utf-8')).body:
        if isinstance(f,ast.FunctionDef) and f.name in names:exec(compile(ast.Module(body=[f],type_ignores=[]),filename,'exec'))
mathml.wrap_display=scope_preserving_display
models=json.loads((ROOT/'dist/chapters/d_counting-models.json').read_text())
by_id={m['id']:m for m in models['models']}
def trace(id):
    m=by_id[id];f=m['frames'][0]
    return f'''<section class="counting-model" data-counting-model="{id}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p class="counting-invariant"><strong>Model invariant.</strong> {e(m['invariant'])}</p><div class="counting-stage">{f['svg']}</div><p class="counting-caption" aria-live="polite">{e(f['caption'])}</p><div class="counting-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2200">Slow</option><option value="1400" selected>Normal</option><option value="850">Fast</option></select></label><label>Checkpoint<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} checkpoint"></label></div><p class="counting-progress" data-progress>Checkpoint 1 of {len(m['frames'])}</p><div class="formula-block counting-formula">{f['formulaHtml']}</div><p class="counting-error" hidden></p><div class="counting-print-trace"></div></section>'''
groups={'tree':['dc-tree'],'fibers':['dc-fibers','dc-nonuniform'],'selection':['dc-selection'],'word':['dc-word'],'gaps':['dc-gaps'],'circle':['dc-circle','dc-periodic'],'stars':['dc-stars','dc-lower'],'groups':['dc-groups','dc-empty'],'pascal':['dc-pascal'],'path':['dc-path','dc-reflection']}
questions=json.loads((BASE/'d_counting-questions.json').read_text())
all_actual=json.loads((BASE/'exam-calibration/actual-items.json').read_text())
ids=['MS_CS_1405_Q113','MS_CS_1405_Q115','MS_CS_1405_Q120','MS_CS_1405_Q121','MS_CS_1405_Q122','MS_CS_1405_Q123','MS_CS_1405_Q129','Phd_CS_1405_Q20']
auth=[dict(next(q for q in all_actual if q['id']==id)) for id in ids]
auth[0]['options']=list(auth[0]['options']);auth[0]['options'][0]='37'
# Correct the previously mistyped archive option; the derived answer is unchanged.
next(q for q in all_actual if q['id']==ids[0])['options'][0]='37'
(BASE/'exam-calibration/actual-items.json').write_text(json.dumps(all_actual,indent=2)+'\n')
(BASE/'d_counting-authentic.json').write_text(json.dumps(auth,indent=2)+'\n')
bank='<h3 id="authentic-questions">Authentic examination revisits</h3>'+''.join(item(q,i,True).replace('Authentic examination · checked English translation','Authentic examination revisit · checked English adaptation') for i,q in enumerate(auth,1))
bank+='<h3 id="original-questions">Original and course-inspired problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,9))
rules=[]
for block in (BASE/'d_counting-review.en.md').read_text().split('\n\n'):
    m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
    rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="counting-lab"><form id="counting-form"><label>Model<select name="mode"><option value="subset">Distinct subsets</option><option value="gap">Nonadjacent selected positions</option><option value="composition">Identical tokens in labeled boxes</option><option value="necklace">Fixed-weight binary rotation classes</option></select></label><label>n: positions or tokens<input name="n" type="number" min="1" max="8" step="1" value="6" required></label><label>k: selected positions or boxes<input name="k" type="number" min="0" max="8" step="1" value="3" required></label><button type="submit">Enumerate and compare</button></form><div id="counting-output" aria-live="polite"></div><p>Enumeration is restricted to small finite inputs: n from one to eight, k from zero to eight; allocation mode permits one to four labeled boxes. It verifies those inputs, while the lesson supplies general proofs. Rotation mode keeps reflection distinct.</p></section>'''
source=(BASE/'d_counting.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:counting -->',lab)
for key,model_ids in groups.items():source=source.replace('<!-- SIM:'+key+' -->',''.join(trace(id) for id in model_ids))
body=text(source)
anchors=['sources','models','selections','inventory','arrangements','allocations','identities','paths','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body and '\x00' not in body
assert body.count('class="exam-question"')==88 and body.count('class="review-rule"')==80,(body.count('class="exam-question"'),body.count('class="review-rule"'))
title='Permutations, Combinations, and Counting'
nav=' '.join('<a href="#'+a+'">'+a.capitalize()+'</a>' for a in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="d_counting.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Week 3</p><h1>{title}</h1><p>Review draft · four reviewed university courses · 88 worked problems · 80 examination rules · 15 dedicated concept traces</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="math-layout.js"></script><script src="d_counting.js"></script><script src="exam-calibration.js"></script></body></html>'''
(ROOT/'dist/chapters/d_counting.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
    p=BASE/f'd_counting-{suffix}.md'
    if p.exists():(ROOT/f'dist/reviews/d_counting-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Counting chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/d_counting.html">← Counting chapter</a></p><article class="lesson">'+text(p.read_text())+'</article></main><script src="../chapters/math-layout.js"></script></body></html>',encoding='utf-8')

p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());ledger=json.loads((BASE/'library-approval.json').read_text());approved=set(ledger['approvedTopics'])
for w in lessons:
    for c in w['chapters']:
        if c['topicId'] not in approved:continue
        c.update(status='ready',statusLabel='Student-approved chapter',revisionState='exam_grounded_approved',visualRevisionState='student_approved',animationReviewState='student_approved')
        if c['topicId']=='g_combin':c['approvedVersion']=67
        file=ROOT/'dist'/c['url'];s=file.read_text(encoding='utf-8');s=s.replace('Review draft ·','Student-approved chapter ·')
        # Approval changes the visible state, retaining the reviewed lesson and formulas.
        s=s.replace('Current revision awaits approval','Visual and mathematical revision approved').replace('All 31 chapters have a revised visual and mathematical layer. Earlier approval statements below describe previous versions.','The student approved the visual and mathematical revision of these 31 chapters in Site version 67.')
        if c['topicId']=='s_counting':
            def correct_source_option(match):
                q=match.group()
                if not re.match(r'<section[^>]*data-source-id="MS_CS_1405_Q113"',q):return q
                q,n=re.subn(r'(<b>1\.</b><div><p>)32(</p>)',r'\g<1>37\2',q,count=1)
                assert n==1 or '<b>1.</b><div><p>37</p>' in q
                return q
            s=re.sub(r'<section class="exam-question"[\s\S]*?</section>',correct_source_option,s)
        file.write_text(s,encoding='utf-8')
week=next((w for w in lessons if w['week']==3),None)
if week is None:week=dict(week=3,title='Week 3 chapter library',description='Each chapter is published as a source-reviewed draft and requires explicit approval before the next chapter begins.',chapters=[]);lessons.append(week)
week['chapters']=[c for c in week['chapters'] if c['topicId']!='d_counting']+[dict(topicId='d_counting',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/d_counting.html',questionCount=88,authenticQuestionCount=8,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/d_counting-sources.html',qualityAuditUrl='reviews/d_counting-quality.html',animationCount=15,animationWalkthroughCount=15,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
# Update historical library review banners only; do not rerender approved prose.
for p in [ROOT/'dist/library-review.html',ROOT/'dist/subject-visual-review.html',ROOT/'dist/animation-review.html']:
    if p.exists():
        s=p.read_text();s=s.replace('Current revision awaits approval','Visual and mathematical revision approved').replace('All 31 chapters have a revised visual and mathematical layer. Earlier approval statements below describe previous versions.','The student approved the visual and mathematical revision of these 31 chapters in Site version 67.')
        s=s.replace('awaiting_user_approval','student_approved').replace('Awaiting student approval','Student-approved in version 67')
        p.write_text(s)
p=ROOT/'dist/evidence/subject-visual-review/review.json';p.write_text((BASE/'subject-visual-review.json').read_text())
# Four actual read-course records; download failures and web text access stay explicit.
downloads=json.loads((BASE/'d_counting-source-downloads.json').read_text());docs={d['key']:d for d in downloads}
specs=[('mit','MIT','6.042J Mathematics for Computer Science, Spring 2015; Lehman, Leighton and Meyer','Sections 14.1–14.7 and 14.10; PDF pages 560–581 and 596–600 with section boundaries respected','Bijection, constant-fiber and multinomial proof backbone',['mit']),('berkeley','UC Berkeley','CS70 Summer 2019; instructors James Hulett and Elizabeth Yang','Notes 12 and 12.5, all nine pages','Four selection models, nonuniform fibers, casework and symmetry',['berkeley','berkeley-advanced']),('stanford','Stanford','CS109 Spring 2020; Lisa Yan, based on Sahami and Piech','Lecture Notes 1 and 2, all eleven pages','Constrained selection, allocation transformations and role identities',['stanford-basic','stanford']),('cmu','Carnegie Mellon','15-251 Fall 2010; Anupam Gupta and Danny Sleator','Lectures 7 and 8, all 27 original PDF pages through web text reader','Choice trees, repeated words, polynomial choices and double counting',['cmu','cmu-advanced'])]
courses=[]
for key,university,course,scope,role,keys in specs:
    source_docs=[]
    for k in keys:
        doc=dict(url=docs[k]['url'],readingScope=scope)
        if 'sha256' in docs[k]:doc['sha256']=docs[k]['sha256']
        if k=='mit':doc['sha256']=hashlib.sha256(Path('C:/Users/bheydari/AppData/Local/Temp/phd-invariants-sources/mit.pdf').read_bytes()).hexdigest();doc['access']='Read existing original cached PDF after current download timeout'
        if key=='cmu':doc['access']='Original web PDF text read; native request refused; no local checksum claimed'
        source_docs.append(doc)
    courses.append(dict(id=key+'-discrete-counting-written',subject='discrete',university=university,course=course,url=source_docs[0]['url'],evidence=source_docs[0]['url'],topics=['d_counting'],advantage=role,limit='Bounded eight-candidate comparison; not exhaustive worldwide ranking',access='Official public written material',reviewed=True,reviewScope=scope,selectionRole=role,sourceDocuments=source_docs))
(BASE/'d_counting-reviewed-courses.json').write_text(json.dumps(courses,indent=2)+'\n')
p=ROOT/'dist/course-audit-week1.en.json';data=json.loads(p.read_text());ids={c['id'] for c in courses};data['courses']=[c for c in data['courses'] if c['id'] not in ids]+courses;data['reviewedAt']='2026-10-05';p.write_text(json.dumps(data,indent=2)+'\n')
print('Rendered one counting draft: 88 worked tasks, 80 rules, 15 traces / 76 checkpoints; 31 prior chapters approved.')
