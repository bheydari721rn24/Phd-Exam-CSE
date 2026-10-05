"""Render only the active chapter. Never rerender preceding approved chapters."""
from pathlib import Path
from html import escape as e
import json,re,sys,ast,xml.etree.ElementTree as ET
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(Vert='‖',circ='∘',Phi='Φ',ell='ℓ')
oldbase=mathml.Parser.base
def base(self):
 self.skip();marker=r'\begin{cases}'
 if self.s.startswith(marker,self.i):
  self.i+=len(marker);stop=self.s.index(r'\end{cases}',self.i);s=self.s[self.i:stop];self.i=stop+len(r'\end{cases}')
  return '<mrow><mo>{</mo><mtable columnalign="left left">'+''.join('<mtr>'+''.join('<mtd>'+mathml.Parser(c).seq()+'</mtd>' for c in row.split('&'))+'</mtr>' for row in s.split(r'\\'))+'</mtable></mrow>'
 return oldbase(self)
mathml.Parser.base=base
from mathml import render,width,markdown_math
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef) and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
def text(s):return normalize_scripts(normalize_math(markdown_math(s,md)))
data=json.loads((R/'dist/chapters/a_stackqueue-models.json').read_text(encoding='utf-8'));by={m['id']:m for m in data['models']}
def trace(id,scope='Exact stated inputs and derived checkpoints'):
 m=by[id];f=m['frames'][0]
 return f'''<section class="sq-model" data-sq-model="{e(id)}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p class="sq-scope">{e(scope)}</p><p class="sq-invariant"><strong>Invariant and scope.</strong> {e(m['invariant'])}</p><div class="sq-stage">{f['svg']}</div><p class="sq-caption" aria-live="polite">{e(f['caption'])}</p><div class="sq-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2400">Slow</option><option value="1600" selected>Normal</option><option value="950">Fast</option></select></label><label>Checkpoint<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} checkpoint"></label></div><p class="sq-progress" data-progress>Checkpoint 1 of {len(m['frames'])}</p><div class="formula-block sq-formula">{f['formulaHtml']}</div><p class="sq-error" hidden></p><div class="sq-print-trace"></div></section>'''
def item(q,n,auth=False):
 provenance=e(q['origin']) if not auth else ''
 title=q['title'];options='';answer=''
 if auth:
  from urllib.parse import quote
  url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
  provenance=f'<a href="{e(url)}">{e(q["booklet"].replace("_"," "))} · Q{q["questionNumber"]} · PDF page {q["pdfPage"]}</a>. Independently derived answer; not an official key.'
  title=q['booklet'].replace('_',' ')+' Q'+str(q['questionNumber'])+' — '+title
  options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(s)+'</div></div>' for i,s in enumerate(q['options'],1))+'</div>'
  answer='<p><strong>Correct option: '+str(q['answer'])+'.</strong></p>'
 model=trace(q['modelId'],q.get('visualScope','Exact question inputs; the state trace illustrates the written derivation.')) if q.get('modelId') else ''
 return '<section class="exam-question" data-source-id="'+e(q['id'])+'" data-kind="'+('authentic' if auth else 'original')+'"><h3>Question '+str(n)+'. '+e(title)+'</h3><p class="exam-label">'+('Authentic examination · checked English adaptation' if auth else 'Original or independently reconstructed course problem · Medium–Hard')+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])+options+'<details class="exam-solution"><summary>Read the complete solution and reasoning</summary>'+answer+text(q['solution'])+model+'</details></section>'
qs=json.loads((B/'a_stackqueue-questions.json').read_text(encoding='utf-8'));a=json.loads((B/'a_stackqueue-authentic.json').read_text(encoding='utf-8'))
bank='<h3 id="authentic-questions">Authentic MSc and PhD questions</h3>'+''.join(item(q,i,True) for i,q in enumerate(a,1))+'<h3 id="original-questions">Original and course-derived mathematical/conceptual questions</h3>'+''.join(item(q,i) for i,q in enumerate(qs,len(a)+1))
rules=[]
for block in (B/'a_stackqueue-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="sq-lab"><form id="sq-form"><label>Laboratory<select name="mode"><option value="ring">Circular queue</option><option value="two">Queue from two stacks</option><option value="postfix">Exact postfix evaluation</option><option value="permutation">Stack-output permutation</option><option value="window">Sliding-window maximum</option></select></label><label data-modes="ring">Physical capacity<input name="capacity" type="number" value="7" min="1" max="12"></label><label data-modes="ring two">Operation history<input name="ops" type="text" value="E:4,E:7,E:9,D,E:2,D" aria-describedby="sq-limits"></label><label data-modes="postfix">Space-separated tokens<input name="tokens" type="text" value="18 6 3 / - 4 *"></label><label data-modes="permutation">Target permutation<input name="target" type="text" value="3,2,1,5,4"></label><label data-modes="window">Input values<input name="values" type="text" value="1,3,-1,-3,5,3,6,7"></label><label data-modes="window">Window width<input name="window" type="number" value="3" min="1" max="12"></label><button type="submit">Compute and inspect all checkpoints</button></form><p id="sq-lab-error" role="alert"></p><p id="sq-limits">Ring capacity: 1–12. Histories: at most 20 operations with integer values from −99 to 99; two-stack live length at most 12. Postfix: at most 24 tokens, integer operands −99 to 99, binary + − * /, exact rational results within the displayed arithmetic bound. Permutations: 1–8 distinct labels. Window inputs: 1–12 integers −99 to 99 and a width that fits the input. Invalid input retains the last valid trace.</p><div id="sq-output"></div></section>'''
source=(B/'a_stackqueue.en.md').read_text(encoding='utf-8').split('\n',1)[1]
source=source.replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:stackqueue -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM:'+k+' -->',''.join(trace(id) for id in ids))
body=text(source);anchors=['sources','interface','array-stack','linked','ring','resizing','two-stacks','clients','permutations','catalan','brackets','expressions','conversion','aggregates','monotone-stacks','windows','worklists','summary','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--' not in body and '$' not in body, [(x,body[max(0,body.index(x)-90):body.index(x)+150]) for x in ['<!--','$'] if x in body]
assert body.count('class="exam-question"')==84 and body.count('class="review-rule"')==80
title='Stacks, Queues, and Applications'
model_count=len(data['models']);lesson_count=sum(len(v) for v in data['groups'].values());problem_count=model_count-lesson_count
nav=' '.join('<a href="#'+k+'">'+k.replace('-',' ').capitalize()+'</a>' for k in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="a_stackqueue.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Data Structures and Algorithms · Week 3</p><h1>{title}</h1><p>Review draft · four primary university courses · 84 worked problems · 80 examination rules · {lesson_count} lesson models and {problem_count} problem models</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="math-layout.js"></script><script src="diagram-layout.js"></script><script src="a_stackqueue.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/a_stackqueue.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'a_stackqueue-{suffix}.md'
 if p.exists():(R/f'dist/reviews/a_stackqueue-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Stacks and Queues audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/a_stackqueue.html">Stacks and Queues chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';a=json.loads(p.read_text(encoding='utf-8'));w=next(w for w in a if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='a_stackqueue']+[dict(topicId='a_stackqueue',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/a_stackqueue.html',questionCount=84,authenticQuestionCount=3,originalQuestionCount=81,examNotesCount=80,sourceAuditUrl='reviews/a_stackqueue-sources.html',qualityAuditUrl='reviews/a_stackqueue-quality.html',animationCount=model_count,animationWalkthroughCount=model_count,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')];p.write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8')
print(f'Rendered only a_stackqueue: 84 problems, 80 rules, {model_count} models.')
