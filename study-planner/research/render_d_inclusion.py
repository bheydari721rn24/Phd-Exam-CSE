"""Render the sole new chapter without rerendering approved chapters."""
from pathlib import Path
from html import escape as e
import ast,json,re,sys,hashlib,xml.etree.ElementTree as ET
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.SYMBOLS.update(ell='ℓ',supseteq='⊇')
from mathml import render,width,markdown_math
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
for filename,names in [('build_correct_chapter.py',('scope_preserving_display',)),('exam-calibration/build.py',('prep','text')),('build_conditional_chapter.py',('item',))]:
 for f in ast.parse((B/filename).read_text(encoding='utf-8')).body:
  if isinstance(f,ast.FunctionDef) and f.name in names:exec(compile(ast.Module(body=[f],type_ignores=[]),filename,'exec'))
mathml.wrap_display=scope_preserving_display
data=json.loads((R/'dist/chapters/d_inclusion-models.json').read_text());by={m['id']:m for m in data['models']}
def trace(id):
 m=by[id];f=m['frames'][0]
 return f'''<section class="inclusion-model" data-inclusion-model="{id}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p class="inclusion-invariant"><strong>Model invariant.</strong> {e(m['invariant'])}</p><div class="inclusion-stage">{f['svg']}</div><p class="inclusion-caption" aria-live="polite">{e(f['caption'])}</p><div class="inclusion-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2200">Slow</option><option value="1400" selected>Normal</option><option value="850">Fast</option></select></label><label>Checkpoint<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} checkpoint"></label></div><p class="inclusion-progress" data-progress>Checkpoint 1 of {len(m['frames'])}</p><div class="formula-block inclusion-formula">{f['formulaHtml']}</div><p class="inclusion-error" hidden></p><div class="inclusion-print-trace"></div></section>'''
q=json.loads((B/'d_inclusion-questions.json').read_text());actual=json.loads((B/'d_inclusion-authentic.json').read_text())
bank='<h3 id="authentic-questions">Authentic examination revisits</h3>'+''.join(item(x,i,True).replace('Authentic examination · checked English translation','Authentic examination revisit · checked English adaptation') for i,x in enumerate(actual,1))
bank+='<h3 id="original-questions">Original and independently reconstructed course problems</h3>'+''.join(item(x,i) for i,x in enumerate(q,3))
rules=[]
for block in (B/'d_inclusion-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="inclusion-lab"><form id="inclusion-form"><label>Exact model<select name="mode"><option value="sets">Three-set atoms and signed intersections</option><option value="maps">Onto maps with actual assignments</option><option value="permutations">Forbidden diagonal assignments</option><option value="caps">Equal-cap identical-token allocations</option></select></label><label><span>n: objects, inputs, labels or tokens</span><input name="n" type="number" min="0" max="8" step="1" value="4" required></label><label><span>m: outputs, forbidden positions or boxes</span><input name="m" type="number" min="0" max="4" step="1" value="3" required></label><label>Cap per box<input name="cap" type="number" min="0" max="5" step="1" value="2" required></label><label class="atom-input">Set mode: eight exact atoms in mask order<input name="atoms" type="text" value="1,4,4,3,4,2,1,1"></label><button type="submit">Enumerate and audit</button></form><div id="inclusion-output" aria-live="polite"></div><p>Map enumeration permits zero to eight inputs and zero to four outputs, with at most 65,536 unrestricted maps. Permutations permit zero to eight labels; the forbidden-position count cannot exceed the label count. Allocations permit zero to eight identical tokens and one to four labeled boxes, with caps zero to five. Set mode uses eight nonnegative integer atom sizes up to fifty each. Only the first 24 qualifying objects are drawn when the result is larger; every object contributes to the exact count.</p></section>'''
source=(B/'d_inclusion.en.md').read_text().split('\n',1)[1].replace(r'\mathbin{\mathrm{xor}}',r'\mathrm{xor}').replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:inclusion -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM:'+k+' -->',''.join(trace(id) for id in ids))
body=text(source)
anchors=['sources','atoms','theorem','multiplicity','bounds','maps','derangements','rook','allocations','arithmetic','probability','computation','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body and '\x00' not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='Inclusion-Exclusion: Overlap, Exact Multiplicity, and Forbidden Configurations'
nav=' '.join('<a href="#'+k+'">'+k.capitalize()+'</a>' for k in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="d_inclusion.css"><link rel="stylesheet" href="advanced-simulations.css?v=library-unified-1"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Week 3</p><h1>{title}</h1><p>Review draft · four primary university courses and one reviewed complementary course · 82 worked problems · 80 examination rules · 13 dedicated concept traces</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="advanced-simulations.js?v=library-unified-1"></script><script src="diagram-layout.js?v=library-ports-3"></script><script src="math-layout.js"></script><script src="d_inclusion.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/d_inclusion.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'd_inclusion-{suffix}.md'
 if p.exists():(R/f'dist/reviews/d_inclusion-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Inclusion-exclusion chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="advanced-simulations.css?v=library-unified-1"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/d_inclusion.html">Inclusion-exclusion chapter</a></p><article class="lesson">'+text(p.read_text())+'</article></main><script src="../chapters/math-layout.js"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';a=json.loads(p.read_text());w=next(w for w in a if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='d_inclusion']+[dict(topicId='d_inclusion',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/d_inclusion.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/d_inclusion-sources.html',qualityAuditUrl='reviews/d_inclusion-quality.html',animationCount=13,animationWalkthroughCount=13,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')];p.write_text(json.dumps(a,indent=2)+'\n')
downloads={x['key']:x for x in json.loads((B/'d_inclusion-downloads.json').read_text())};specs=[('mit','MIT','6.042J Mathematics for Computer Science, Spring 2015; Lehman, Leighton and Meyer','§14.9, physical PDF pages 590–596, respecting section boundaries','Adjacency intersections, inclusive and exclusive overlap, and totient'),('oxford','Oxford','Discrete Mathematics, Michaelmas 2010; Andrew D. Ker','§3.3–3.4, physical pages 47–50','Position-dependent digits, derangements and strict endpoints'),('cornell','Cornell','CS2800 course text A Course in Discrete Structures; Rafael Pass and Wei-Lung Dustin Tseng','§4.4, physical pages 74–76','Multiplicity proof, onto maps and complement counting'),('cmu','Carnegie Mellon','21-301 Combinatorics, Fall 2018; Michael Tait','§2.5, physical pages 20–24','Complement, empty-intersection convention and assignment applications'),('berkeley','UC Berkeley','EECS70 Spring 2020, Note 14; individual authorship not named in the note','§4.3, physical pages 10–11, before exercises','Complementary weighted-event interpretation and union bounds')]
courses=[]
for key,uni,course,scope,role in specs:
 d=downloads[key];doc=dict(url=d['url'],readingScope=scope)
 if 'sha256' in d:doc['sha256']=d['sha256'];doc['access']='Original cached PDF read'
 else:doc['access']='Official original PDF section read through web text reader after native download timeout; no local checksum claimed'
 courses.append(dict(id=key+'-inclusion-written',subject='discrete',university=uni,course=course,url=d['url'],evidence=d['url'],topics=['d_inclusion'],advantage=role,limit='Bounded eight-candidate evaluation, not worldwide exhaustive ranking',access='Official public written text',reviewed=True,reviewScope=scope,selectionRole=role,sourceDocuments=[doc]))
(B/'d_inclusion-reviewed-courses.json').write_text(json.dumps(courses,indent=2)+'\n')
p=R/'dist/course-audit-week1.en.json';a=json.loads(p.read_text());ids={c['id'] for c in courses};a['courses']=[c for c in a['courses'] if c['id'] not in ids]+courses;a['reviewedAt']='2026-10-05';p.write_text(json.dumps(a,indent=2)+'\n')
print('Rendered one inclusion-exclusion draft, 82 solved tasks, 80 full rules, 13 exact displays.')
