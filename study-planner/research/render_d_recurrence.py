"""Render only the new arithmetic review draft using native mathematical typography."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import json,re,sys,ast
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(ldots='…',log='log',Longrightarrow='⟹',Sigma='Σ',psi='ψ')
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):
 s=s.replace(r"\mathbin{\&}",r"\&").replace(r"\bigl", "").replace(r"\bigr", "")
 return normalize_scripts(normalize_math(mathml.markdown_math(s,md)))
models=json.loads((R/'dist/chapters/d_recurrence-models.json').read_text(encoding='utf-8'))
for m in models['models']:
 for f in m['frames']:
  f['formulaHtml']=text('$'+f['formula']+'$')if f.get('formula')else ''
by={m['id']:m for m in models['models']}
def trace(id):
 m=by[id];return '<section class="rc-model" data-rc-model="'+e(id)+'" tabindex="0" aria-label="'+e(m['title'])+'"><h3>'+e(m['title'])+'</h3><p>'+e(m['invariant'])+'</p><div class="rc-stage">'+m['frames'][0]['svg']+'</div><div class="rc-print"></div></section>'
def item(q,n,auth=False):
 provenance=e(q.get('origin',''));options='';answer=''
 if auth:
  url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
  provenance='<a href="'+e(url)+'">'+e(q['booklet'].replace('_',' '))+' · Q'+str(q['questionNumber'])+' · PDF page '+str(q['pdfPage'])+'</a>. Revisited original examination bridge; independently derived answer, not an official key.'
  options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(s)+'</div></div>'for i,s in enumerate(q['options'],1))+'</div>'
  answer='<p><strong>Correct option: '+str(q['answer'])+'.</strong></p>'
 visual=trace(q['modelId'])if q.get('modelId')else''
 if visual and not q.get('visualQualification'):visual='<p class="visual-scope">Companion visualization: the diagram title specifies its sample inputs and index range. Follow the written solution for the stated problem parameters; this sample illustrates the reasoning pattern.</p>'+visual
 if q.get('visualQualification'):visual='<p class="visual-scope">'+e(q['visualQualification'])+'</p>'+visual
 return '<section class="exam-question" data-source-id="'+e(q['id'])+'" data-kind="'+('authentic'if auth else'original')+'"><h3>Question '+str(n)+'. '+e(q['title'])+'</h3><p class="exam-label">'+('Authentic examination · checked English adaptation'if auth else'Original or reconstructed problem · mathematical and conceptual reasoning')+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])+options+'<details class="exam-solution"><summary>Read the complete solution and reasoning</summary>'+answer+text(q['solution'])+visual+'</details></section>'
qs=json.loads((B/'d_recurrence-questions.json').read_text(encoding='utf-8'));auth=json.loads((B/'d_recurrence-authentic.json').read_text(encoding='utf-8'))
bank='<h3 id="authentic-questions">Authenticated MSc and doctoral examination bridges</h3>'+''.join(item(q,i,True)for i,q in enumerate(auth,1))+'<h3 id="original-questions">Original and reconstructed formula/concept problems</h3>'+''.join(item(q,i+len(auth))for i,q in enumerate(qs,1))
rules=[]
for block in (B/'d_recurrence-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>'if m else text(block))
lab='<section class="lab"><form id="rc-form"><label>Model<select name="operation"><option>unrolling</option><option>differences</option><option>boundary</option><option>tiling</option><option>resonance</option><option>automaton</option><option>derangements</option><option>partitions</option><option>ferrers</option><option>catalan</option><option>modular</option><option>matrix</option></select></label><label>Target index / size<input name="n" type="number" min="1" max="8" value="5"></label><label>First-order multiplier<input name="p" type="number" min="-4" max="4" value="2"></label><label>First-order starting value<input name="a0" type="number" min="-10" max="10" value="0"></label><label>Modulus<input name="modulus" type="number" min="2" max="8" value="3"></label><button type="submit">Build an exact trace</button></form><p id="rc-error" role="alert"></p><p>All indices are integers from one through eight. Full Dyck-path enumeration is limited to four pairs. Exact three-part Ferrers diagrams require a total of at least three. The multiplier and starting value affect only first-order unrolling; the modulus affects only the Fibonacci residue model. Other model equations and boundaries are explicitly fixed in their titles and descriptions. Every trace starts paused, and invalid input preserves the previous valid trace. Enumeration checkpoints represent different objects, rather than time evolution of one object.</p><div id="rc-output"></div></section>'
source=(B/'d_recurrence.en.md').read_text(encoding='utf-8').split('\n',1)[1].replace('<!-- INCLUDE: problems -->',bank).replace('<!-- INCLUDE: review -->',''.join(rules)).replace('<!-- LAB: recurrence -->',lab)
for k,ids in models['groups'].items():source=source.replace('<!-- SIM: '+k+' -->',''.join(trace(i)for i in ids))
body=text(source);anchors=['sources', 'domain', 'classification', 'unrolling', 'variable', 'uniqueness', 'characteristic', 'distinct', 'repeated', 'completeness', 'zero', 'complex', 'fibonacci', 'forcing', 'resonance', 'mixed', 'counting', 'patterns', 'derangements', 'set-partitions', 'integer-partitions', 'catalan', 'prefix', 'generating', 'matrix', 'modular', 'verification', 'summary', 'problems', 'review', 'laboratory', 'references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--'not in body and '$'not in body
assert body.count('class="exam-question"')==83 and body.count('class="review-rule"')==80
title='Recurrence Relations: Exact Solutions, Counting Models, and Boundary Conditions';nav=' '.join('<a href="#'+k+'">'+k.replace('-',' ').capitalize()+'</a>'for k in anchors)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+''' · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="teaching-transitions.css"><link rel="stylesheet" href="d_recurrence.css"><link rel="stylesheet" href="advanced-simulations.css?player-behavior-2"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-4">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Week 4</p><h1>'''+title+'''</h1><p>Review draft · four reviewed written university courses · 83 worked problems · 80 final reasoning rules · 14 distinct mathematical models</p><p><a href="../reviews/d_recurrence-quality.html">Scientific and visual audit</a></p></header><nav class="toc" aria-label="Chapter contents">'''+nav+'''</nav><article class="lesson">'''+body+'''</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="advanced-simulations.js?player-behavior-2"></script><script src="math-layout.js?v=79"></script><script src="diagram-layout.js"></script><script src="teaching-transitions.js?v=library-unified-1"></script><script src="d_recurrence.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/d_recurrence.html').write_text(page,encoding='utf-8')
(R/'dist/chapters/d_recurrence-models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'd_recurrence-{suffix}.md'
 if p.exists():(R/f'dist/reviews/d_recurrence-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Recurrence chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/d_recurrence.css"></head><body><main class="chapter"><p><a href="../chapters/d_recurrence.html">Recurrence chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js?v=79"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';weeks=json.loads(p.read_text(encoding='utf-8'));w=next((w for w in weeks if w['week']==4),None)
if w is None:
 w=dict(week=4,title='Week 4 chapter library',description='Source-reviewed chapters are added sequentially under your standing authorization. Completed drafts remain available for student review.',chapters=[]);weeks.append(w)
w['title']='Week 4 chapter library'
w['description']='Source-reviewed chapters are added sequentially under your standing authorization. Completed drafts remain available for student review.'
w['chapters']=[c for c in w['chapters']if c['topicId']!='d_recurrence']+[dict(topicId='d_recurrence',title=title,status='draft',statusLabel='New chapter available for review',revisionState='new_chapter_draft',url='chapters/d_recurrence.html',questionCount=83,authenticQuestionCount=3,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/d_recurrence-sources.html',qualityAuditUrl='reviews/d_recurrence-quality.html',animationCount=14,animationWalkthroughCount=14,animationReviewState='review_draft',visualRevisionState='review_draft')]
p.write_text(json.dumps(weeks,indent=2)+'\n',encoding='utf-8')
print('Rendered only d_recurrence: 83 worked problems, 80 final rules, 14 distinct mathematical models.')
