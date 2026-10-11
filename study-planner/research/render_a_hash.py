"""Render only the new heap review draft using native mathematical typography."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import json,re,sys,ast
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(ell='ℓ',gcd='gcd',exp='exp',ln='ln',Pr='Pr',ldots='…',log='log',Longrightarrow='⟹',Sigma='Σ',psi='ψ',phi='φ',Phi='Φ')
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):
 s=s.replace(r"\mathbin{\&}",r"\&").replace(r"\bigl", "").replace(r"\bigr", "")
 return normalize_scripts(normalize_math(mathml.markdown_math(s,md)))
models=json.loads((R/'dist/chapters/a_hash-models.json').read_text(encoding='utf-8'))
for m in models['models']:
 for f in m['frames']:
  f['formulaHtml']=text('$'+f['formula']+'$')if f.get('formula')else ''
by={m['id']:m for m in models['models']}
def trace(id):
 m=by[id];return '<section class="hs-model" data-hs-model="'+e(id)+'" tabindex="0" aria-label="'+e(m['title'])+'"><h3>'+e(m['title'])+'</h3><p>'+e(m['invariant'])+'</p><div class="hs-stage">'+m['frames'][0]['svg']+'</div><div class="hs-print"></div></section>'
def item(q,n,auth=False):
 provenance=e(q.get('origin',''));options='';answer=''
 if auth:
  url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
  provenance='<a href="'+e(url)+'">'+e(q['booklet'].replace('_',' '))+' · Q'+str(q['questionNumber'])+' · PDF page '+str(q['pdfPage'])+'</a>. Revisited original examination bridge; independently derived answer, not an official key.'
  options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(s)+'</div></div>'for i,s in enumerate(q['options'],1))+'</div>'
  answer='<p><strong>'+e(q.get('answerLabel','Correct option:'))+' '+str(q['answer'])+'.</strong></p>'
 visual=trace(q['modelId'])if q.get('modelId')else''
 if visual and not q.get('visualQualification'):visual='<p class="visual-scope">Companion visualization: the diagram title specifies its sample inputs and index range. Follow the written solution for the stated problem parameters; this sample illustrates the reasoning pattern.</p>'+visual
 if q.get('visualQualification'):visual='<p class="visual-scope">'+e(q['visualQualification'])+'</p>'+visual
 return '<section class="exam-question" data-source-id="'+e(q['id'])+'" data-kind="'+('authentic'if auth else'original')+'"><h3>Question '+str(n)+'. '+e(q['title'])+'</h3><p class="exam-label">'+('Authentic examination · checked English adaptation'if auth else'Original or reconstructed problem · mathematical and conceptual reasoning')+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])+options+'<details class="exam-solution"><summary>Read the complete solution and reasoning</summary>'+answer+text(q['solution'])+visual+'</details></section>'
qs=json.loads((B/'a_hash-questions.json').read_text(encoding='utf-8'));auth=json.loads((B/'a_hash-authentic.json').read_text(encoding='utf-8'))
bank='<h3 id="authentic-questions">Authenticated MSc and doctoral examination bridges</h3>'+''.join(item(q,i,True)for i,q in enumerate(auth,1))+'<h3 id="original-questions">Original and reconstructed formula/concept problems</h3>'+''.join(item(q,i+len(auth))for i,q in enumerate(qs,1))
rules=[]
for block in (B/'a_hash-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>'if m else text(block))
lab='<section class="lab"><form id="hs-form"><label>Operation<select name="operation"><option>open</option><option>chain</option><option>shift</option><option>rebuild</option><option>perfect</option><option>cuckoo</option><option>bloom</option><option>horner</option><option>robin</option></select></label><label>Capacity<input name="capacity" value="11"></label><label>Integer keys or character codes<input name="keys" value="10,21,32,43,9"></label><label>Probe policy<select name="policy"><option>linear</option><option>square</option><option>alternating</option><option>triangular</option><option>double</option></select></label><label>Fixed secondary step<input name="step" value="4"></label><label>After building<select name="command"><option>get</option><option>put</option><option>delete</option><option>none</option></select></label><label>Command target<input name="target" value="54"></label><label>New capacity for rebuilding<input name="newCapacity" value="13"></label><label>Polynomial base<input name="base" value="5"></label><label>Bloom bit-function count<input name="hashes" value="3"></label><button type="submit">Build the exact hashing trace</button></form><p id="hs-error" role="alert"></p><p>The compact laboratory accepts capacities two through thirteen and at most sixteen integer inputs between minus 999 and 999. Chaining uses at most eight inputs and eight buckets. Perfect placement requires distinct keys, at most three keys per bucket and four occupied buckets for readable second-level arrays. Rebuilding uses linear probing and enough new slots for every distinct key. Backward shifting requires a present deletion target and linear probing. Cuckoo placement uses distinct keys and declared candidate functions; bounded relocation failure is labeled. Robin Hood placement requires enough slots. Polynomial inputs are character codes; Bloom inputs use the explicit deterministic bit functions printed in the checkpoint. These mechanism samples do not simulate random hashing distributions. A probe route can exhaust before the physical table fills. Every trace starts paused, and invalid input preserves the preceding valid trace.</p><div id="hs-output"></div></section>'

source=(B/'a_hash.en.md').read_text(encoding='utf-8').split('\n',1)[1].replace('<!-- INCLUDE: problems -->',bank).replace('<!-- INCLUDE: review -->',''.join(rules)).replace('<!-- LAB: hash -->',lab)
for k,ids in models['groups'].items():source=source.replace('<!-- SIM: '+k+' -->',''.join(trace(i)for i in ids))
body=text(source);anchors=['sources', 'contract', 'arithmetic', 'chaining', 'occupancy', 'birthday', 'universal', 'lookup', 'linear', 'tombstones', 'shifting', 'quadratic', 'double', 'ideal-probing', 'models', 'rebuilding', 'perfect', 'advanced', 'applications', 'exam-reasoning', 'summary', 'problems', 'review', 'laboratory', 'references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--'not in body and '$'not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='Hash Tables: Exact Probes, Collision Mathematics, and Correct Updates';nav=' '.join('<a href="#'+k+'">'+k.replace('-',' ').capitalize()+'</a>'for k in anchors)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+''' · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="teaching-transitions.css"><link rel="stylesheet" href="a_hash.css"><link rel="stylesheet" href="advanced-simulations.css?player-behavior-2"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-4">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Data Structures and Algorithms · Week 4</p><h1>'''+title+'''</h1><p>Review draft · four core written university courses plus two reviewed comparisons · 82 worked problems · 80 final reasoning rules · 21 specialized exact hashing models</p><p><a href="../reviews/a_hash-quality.html">Scientific and visual audit</a></p></header><nav class="toc" aria-label="Chapter contents">'''+nav+'''</nav><article class="lesson">'''+body+'''</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="advanced-simulations.js?player-behavior-2"></script><script src="math-layout.js?v=79"></script><script src="diagram-layout.js"></script><script src="teaching-transitions.js?v=library-unified-1"></script><script src="a_hash.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/a_hash.html').write_text(page,encoding='utf-8')
(R/'dist/chapters/a_hash-models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'a_hash-{suffix}.md'
 if p.exists():(R/f'dist/reviews/a_hash-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hashing chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/a_hash.css"></head><body><main class="chapter"><p><a href="../chapters/a_hash.html">Hashing chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js?v=79"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';weeks=json.loads(p.read_text(encoding='utf-8'));w=next((w for w in weeks if w['week']==4),None)
if w is None:
 w=dict(week=4,title='Week 4 chapter library',description='Source-reviewed chapters are added sequentially under your standing authorization. Completed drafts remain available for student review.',chapters=[]);weeks.append(w)
w['title']='Week 4 chapter library'
w['description']='Source-reviewed chapters are added sequentially under your standing authorization. Completed drafts remain available for student review.'
w['chapters']=[c for c in w['chapters']if c['topicId']!='a_hash']+[dict(topicId='a_hash',title=title,status='draft',statusLabel='New chapter available for review',revisionState='new_chapter_draft',url='chapters/a_hash.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/a_hash-sources.html',qualityAuditUrl='reviews/a_hash-quality.html',animationCount=21,animationWalkthroughCount=21,animationReviewState='review_draft',visualRevisionState='review_draft')]
p.write_text(json.dumps(weeks,indent=2)+'\n',encoding='utf-8')
print('Rendered only a_hash: 82 worked problems, 80 final rules, 21 specialized exact hashing models.')
