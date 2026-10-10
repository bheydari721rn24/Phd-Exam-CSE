"""Render only the new arithmetic review draft using native mathematical typography."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import json,re,sys,ast
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(ldots='…',log='log',Longrightarrow='⟹')
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):return normalize_scripts(normalize_math(mathml.markdown_math(s,md)))
models=json.loads((R/'dist/chapters/g_arithmetic-models.json').read_text(encoding='utf-8'))
for m in models['models']:
 for f in m['frames']:
  f['formulaHtml']=text('$'+f['formula']+'$')if f.get('formula')else ''
by={m['id']:m for m in models['models']}
def trace(id):
 m=by[id];return '<section class="ar-model" data-ar-model="'+e(id)+'" tabindex="0" aria-label="'+e(m['title'])+'"><h3>'+e(m['title'])+'</h3><p>'+e(m['invariant'])+'</p><div class="ar-stage">'+m['frames'][0]['svg']+'</div><div class="ar-print"></div></section>'
def item(q,n,auth=False):
 provenance=e(q.get('origin',''));options='';answer=''
 if auth:
  url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
  provenance='<a href="'+e(url)+'">'+e(q['booklet'].replace('_',' '))+' · Q'+str(q['questionNumber'])+' · PDF page '+str(q['pdfPage'])+'</a>. Revisited authenticated bridge; independently derived answer, not an official key.'
  options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(s)+'</div></div>'for i,s in enumerate(q['options'],1))+'</div>'
  answer='<p><strong>Correct option: '+str(q['answer'])+'.</strong></p>'
 visual=trace(q['modelId'])if q.get('modelId')else''
 if visual and not q.get('visualQualification'):visual='<p class="visual-scope">Companion visualization: the diagram title specifies its sample operands and width. Follow the written solution for the stated problem parameters; this sample illustrates the reasoning pattern.</p>'+visual
 if visual and not q.get('visualQualification'):visual='<p class="visual-scope">Companion visualization: the diagram title specifies its sample operands and width. Follow the written solution for the stated problem parameters; this sample illustrates the reasoning pattern.</p>'+visual
 if q.get('visualQualification'):visual='<p class="visual-scope">'+e(q['visualQualification'])+'</p>'+visual
 return '<section class="exam-question" data-source-id="'+e(q['id'])+'" data-kind="'+('authentic'if auth else'original')+'"><h3>Question '+str(n)+'. '+e(q['title'])+'</h3><p class="exam-label">'+('Authentic examination · checked English adaptation'if auth else'Original or reconstructed problem · mathematical and conceptual reasoning')+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])+options+'<details class="exam-solution"><summary>Read the complete solution and reasoning</summary>'+answer+text(q['solution'])+visual+'</details></section>'
qs=json.loads((B/'g_arithmetic-questions.json').read_text(encoding='utf-8'));auth=json.loads((B/'g_arithmetic-authentic.json').read_text(encoding='utf-8'))
bank='<h3 id="authentic-questions">Authenticated doctoral examination bridges</h3>'+''.join(item(q,i,True)for i,q in enumerate(auth,1))+'<h3 id="original-questions">Original and reconstructed formula/concept problems</h3>'+''.join(item(q,i+len(auth))for i,q in enumerate(qs,1))
rules=[]
for block in (B/'g_arithmetic-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>'if m else text(block))
lab='''<section class="lab"><form id="ar-form"><label>Operation<select name="operation">'''+''.join('<option value="'+x+'"'+(' selected'if x=='ripple'else'')+'>'+x.capitalize()+'</option>'for x in ['full','ripple','prefix','select','subtract','compare','bcd','csa','multiply','division','booth','nand'])+'''</select></label><label>Word width (one through eight)<input name="n" type="number" min="1" max="8" value="4"></label><label>Unsigned word A<input name="a" type="number" min="0" value="11"></label><label>Unsigned word B / positive divisor<input name="b" type="number" min="0" value="5"></label><label>Incoming carry (zero or one)<input name="c" type="number" min="0" max="1" value="0"></label><label>Third word for carry-save only<input name="z" type="number" min="0" value="6"></label><button type="submit">Build the exact arithmetic trace</button></form><p id="ar-error" role="alert"></p><p>All word inputs must fit the selected unsigned width. Full-adder and NAND inputs are single bits; use width one and third word zero. BCD uses valid digits zero through nine at width four. Carry-select uses width eight with the fixed four/four split. Division requires a positive divisor. Subtraction sets complement mode and initial carry one internally. The third word is used only by carry-save; all other operations ignore it after width validation. Every trace starts paused; invalid input preserves the previous valid trace. These models explain exact logical dependencies and integer identities, not physical gate timing.</p><div id="ar-output"></div></section>'''
source=(B/'g_arithmetic.en.md').read_text(encoding='utf-8').split('\n',1)[1].replace('<!-- INCLUDE: problems -->',bank).replace('<!-- INCLUDE: review -->',''.join(rules)).replace('<!-- LAB: arithmetic -->',lab)
for k,ids in models['groups'].items():source=source.replace('<!-- SIM: '+k+' -->',''.join(trace(i)for i in ids))
body=text(source);anchors=['sources','contract','half','full','ripple','timing','propagate','expansion','groups','prefix','select','skip','borrow','addsub','overflow','extension','equality','signed-compare','bcd','csa','multiply','signed-multiply','division','alu','hdl','summary','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--'not in body and '$'not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='Adders, Comparators, and Arithmetic Circuits';nav=' '.join('<a href="#'+k+'">'+k.replace('-',' ').capitalize()+'</a>'for k in anchors)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+title+''' · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="teaching-transitions.css"><link rel="stylesheet" href="g_arithmetic.css"><link rel="stylesheet" href="advanced-simulations.css?player-behavior-2"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Digital Logic · Week 3</p><h1>'''+title+'''</h1><p>Review draft · four reviewed written university courses · 82 worked problems · 80 final reasoning rules · 15 circuit/process models</p><p><a href="../reviews/g_arithmetic-quality.html">Scientific and visual audit</a></p></header><nav class="toc" aria-label="Chapter contents">'''+nav+'''</nav><article class="lesson">'''+body+'''</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="advanced-simulations.js?player-behavior-2"></script><script src="math-layout.js?v=79"></script><script src="diagram-layout.js"></script><script src="teaching-transitions.js?v=library-unified-1"></script><script src="g_arithmetic.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/g_arithmetic.html').write_text(page,encoding='utf-8')
(R/'dist/chapters/g_arithmetic-models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'g_arithmetic-{suffix}.md'
 if p.exists():(R/f'dist/reviews/g_arithmetic-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Arithmetic chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/g_arithmetic.css"></head><body><main class="chapter"><p><a href="../chapters/g_arithmetic.html">Arithmetic chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js?v=79"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';weeks=json.loads(p.read_text(encoding='utf-8'));w=next(w for w in weeks if w['week']==3)
w['chapters']=[c for c in w['chapters']if c['topicId']!='g_arithmetic']+[dict(topicId='g_arithmetic',title=title,status='draft',statusLabel='New chapter available for review',revisionState='new_chapter_draft',url='chapters/g_arithmetic.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/g_arithmetic-sources.html',qualityAuditUrl='reviews/g_arithmetic-quality.html',animationCount=15,animationWalkthroughCount=15,animationReviewState='review_draft',visualRevisionState='review_draft')]
p.write_text(json.dumps(weeks,indent=2)+'\n',encoding='utf-8')
print('Rendered only g_arithmetic: 82 worked problems, 80 final rules, 15 stored circuit/process models.')
