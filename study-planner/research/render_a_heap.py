"""Render only the new heap review draft using native mathematical typography."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import json,re,sys,ast
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(ldots='…',log='log',Longrightarrow='⟹',Sigma='Σ',psi='ψ',phi='φ',Phi='Φ')
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):
 s=s.replace(r"\mathbin{\&}",r"\&").replace(r"\bigl", "").replace(r"\bigr", "")
 return normalize_scripts(normalize_math(mathml.markdown_math(s,md)))
models=json.loads((R/'dist/chapters/a_heap-models.json').read_text(encoding='utf-8'))
for m in models['models']:
 for f in m['frames']:
  f['formulaHtml']=text('$'+f['formula']+'$')if f.get('formula')else ''
by={m['id']:m for m in models['models']}
def trace(id):
 m=by[id];return '<section class="hp-model" data-hp-model="'+e(id)+'" tabindex="0" aria-label="'+e(m['title'])+'"><h3>'+e(m['title'])+'</h3><p>'+e(m['invariant'])+'</p><div class="hp-stage">'+m['frames'][0]['svg']+'</div><div class="hp-print"></div></section>'
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
qs=json.loads((B/'a_heap-questions.json').read_text(encoding='utf-8'));auth=json.loads((B/'a_heap-authentic.json').read_text(encoding='utf-8'))
bank='<h3 id="authentic-questions">Authenticated MSc and doctoral examination bridges</h3>'+''.join(item(q,i,True)for i,q in enumerate(auth,1))+'<h3 id="original-questions">Original and reconstructed formula/concept problems</h3>'+''.join(item(q,i+len(auth))for i,q in enumerate(qs,1))
rules=[]
for block in (B/'a_heap-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>'if m else text(block))
lab='<section class="lab"><form id="hp-form"><label>Operation<select name="operation"><option>build</option><option>insert</option><option>extract</option><option>change</option><option>delete</option><option>sort</option><option>multiway</option><option>topk</option><option>frontier</option><option>binomial</option><option>fibonacci</option></select></label><label>Orientation<select name="orientation"><option>min</option><option>max</option></select></label><label>Input keys<input name="keys" value="9,4,7,1,0,3,2"></label><label>Arity<select name="arity"><option>2</option><option>3</option><option>4</option></select></label><label>New key<input name="value" value="1"></label><label>Target zero-based position<input name="index" value="0"></label><label>Rank or retained count<input name="k" value="3"></label><button type="submit">Build the exact heap trace</button></form><p id="hp-error" role="alert"></p><p>The compact editable laboratory accepts one through fifteen integer keys between minus 999 and 999, including duplicates; insertion accepts at most fourteen initial keys. Insert, extraction, key change, deletion and frontier selection require an already heap-ordered input. Build repairs arbitrary input. Sort uses a max heap for ascending output. Top-k uses a retained min heap. Binomial insertion uses canonical equal-rank carries. Fibonacci replays the stated four-record first-loss/second-loss case; its controls do not promise an arbitrary Fibonacci implementation. Stable E identifiers refer to original input positions, so E0, E1 and E2 correspond to A, B and C in the tie example. Every trace starts paused; invalid input preserves the previous valid trace.</p><div id="hp-output"></div></section>'

source=(B/'a_heap.en.md').read_text(encoding='utf-8').split('\n',1)[1].replace('<!-- INCLUDE: problems -->',bank).replace('<!-- INCLUDE: review -->',''.join(rules)).replace('<!-- LAB: heap -->',lab)
for k,ids in models['groups'].items():source=source.replace('<!-- SIM: '+k+' -->',''.join(trace(i)for i in ids))
body=text(source);anchors=['sources','interface','shape','order','upward','downward','construction','counters','indexed','aggregate','heapsort','counting','multiway','applications','binomial','potential','fibonacci','degree-proof','alternatives','exam-reasoning','summary','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--'not in body and '$'not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='Heaps and Priority Queues: Exact Structure, Repair Proofs, and Amortized Design';nav=' '.join('<a href="#'+k+'">'+k.replace('-',' ').capitalize()+'</a>'for k in anchors)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+''' · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="teaching-transitions.css"><link rel="stylesheet" href="a_heap.css"><link rel="stylesheet" href="advanced-simulations.css?player-behavior-2"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-4">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Data Structures and Algorithms · Week 4</p><h1>'''+title+'''</h1><p>Review draft · four core written university courses plus a fifth reviewed course · 82 worked problems · 80 final reasoning rules · 21 specialized exact heap models</p><p><a href="../reviews/a_heap-quality.html">Scientific and visual audit</a></p></header><nav class="toc" aria-label="Chapter contents">'''+nav+'''</nav><article class="lesson">'''+body+'''</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="advanced-simulations.js?player-behavior-2"></script><script src="math-layout.js?v=79"></script><script src="diagram-layout.js"></script><script src="teaching-transitions.js?v=library-unified-1"></script><script src="a_heap.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/a_heap.html').write_text(page,encoding='utf-8')
(R/'dist/chapters/a_heap-models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'a_heap-{suffix}.md'
 if p.exists():(R/f'dist/reviews/a_heap-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Heap and priority queue chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/a_heap.css"></head><body><main class="chapter"><p><a href="../chapters/a_heap.html">Heap and priority queue chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js?v=79"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';weeks=json.loads(p.read_text(encoding='utf-8'));w=next((w for w in weeks if w['week']==4),None)
if w is None:
 w=dict(week=4,title='Week 4 chapter library',description='Source-reviewed chapters are added sequentially under your standing authorization. Completed drafts remain available for student review.',chapters=[]);weeks.append(w)
w['title']='Week 4 chapter library'
w['description']='Source-reviewed chapters are added sequentially under your standing authorization. Completed drafts remain available for student review.'
w['chapters']=[c for c in w['chapters']if c['topicId']!='a_heap']+[dict(topicId='a_heap',title=title,status='draft',statusLabel='New chapter available for review',revisionState='new_chapter_draft',url='chapters/a_heap.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/a_heap-sources.html',qualityAuditUrl='reviews/a_heap-quality.html',animationCount=21,animationWalkthroughCount=21,animationReviewState='review_draft',visualRevisionState='review_draft')]
p.write_text(json.dumps(weeks,indent=2)+'\n',encoding='utf-8')
print('Rendered only a_heap: 82 worked problems, 80 final rules, 21 specialized exact heap models.')
