"""Render only the active chapter. Never rerender preceding approved chapters."""
from pathlib import Path
from html import escape as e
import json,re,sys,ast,xml.etree.ElementTree as ET
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(Pr='Pr',Vert='‖',circ='∘',Phi='Φ',ell='ℓ')
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
data=json.loads((R/'dist/chapters/a_sort-models.json').read_text(encoding='utf-8'));by={m['id']:m for m in data['models']}
def trace(id,scope='Exact stated inputs and derived checkpoints'):
 m=by[id];f=m['frames'][0]
 return f'''<section class="sort-model" data-sort-model="{e(id)}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p class="sort-scope">{e(scope)}</p><p class="sort-invariant"><strong>Invariant and scope.</strong> {e(m['invariant'])}</p><div class="sort-stage">{f['svg']}</div><p class="sort-caption" aria-live="polite">{e(f['caption'])}</p><div class="sort-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2400">Slow</option><option value="1600" selected>Normal</option><option value="950">Fast</option></select></label><label>Checkpoint<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} checkpoint"></label></div><p class="sort-progress" data-progress>Checkpoint 1 of {len(m['frames'])}</p><div class="formula-block sort-formula">{f['formulaHtml']}</div><p class="sort-error" hidden></p><div class="sort-print-trace"></div></section>'''
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
qs=json.loads((B/'a_sort-questions.json').read_text(encoding='utf-8'));a=json.loads((B/'a_sort-authentic.json').read_text(encoding='utf-8'))
bank='<h3 id="authentic-questions">Authentic MSc and PhD questions</h3>'+''.join(item(q,i,True) for i,q in enumerate(a,1))+'<h3 id="original-questions">Original and course-derived mathematical/conceptual questions</h3>'+''.join(item(q,i) for i,q in enumerate(qs,len(a)+1))
rules=[]
for block in (B/'a_sort-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='<section class="lab" id="sort-lab"><form id="sort-form"><label>Algorithm<select name="kind"><option value="insertion">Stable insertion</option><option value="selection">Selection</option><option value="bubble">Early-exit bubble</option><option value="merge">Stable top-down merge</option><option value="quick">Strict Lomuto quicksort</option><option value="three">Three-way quicksort</option><option value="heap">Floyd heapsort</option><option value="counting">Stable counting</option><option value="radix">Stable LSD radix</option><option value="bucket">Bucket with local insertion</option></select></label><label>Integer keys<input name="values" value="4,1,3,1,2" aria-describedby="sort-limits"></label><label>Radix base / bucket count<input name="base" type="number" min="2" max="10" value="5"></label><button type="submit">Compute the complete trace</button></form><p id="sort-lab-error" role="alert"></p><p id="sort-limits">Enter 1–10 integers from −999 to 999. Counting intervals may contain at most 24 keys. Radix uses a monotone shift of the minimum key, and a base from 2 to 10. Bucket keys must be integer percentages from 0 to 99. The displayed comparison convention is specified in the lesson; radix/counting distribution uses no key comparisons. An invalid submission preserves the last valid trace.</p><div id="sort-output"></div></section>'
source=(B/'a_sort.en.md').read_text(encoding='utf-8').split('\n',1)[1]
source=source.replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:sorting -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM:'+k+' -->',''.join(trace(id) for id in ids))
body=text(source);anchors=['sources','contract','costs','selection','insertion','bubble-shell','merge-counts','merge-extensions','partition','random-quick','duplicates','heap','lower-bound','counting','radix','bucket-strings','hybrids','summary','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--' not in body and '$' not in body, [(x,body[max(0,body.index(x)-90):body.index(x)+150]) for x in ['<!--','$'] if x in body]
assert body.count('class="exam-question"')==88 and body.count('class="review-rule"')==80
title='Comparison and Non-comparison Sorting'
model_count=len(data['models']);lesson_count=sum(len(v) for v in data['groups'].values());problem_count=model_count-lesson_count
nav=' '.join('<a href="#'+k+'">'+k.replace('-',' ').capitalize()+'</a>' for k in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="a_sort.css"><link rel="stylesheet" href="advanced-simulations.css?v=library-unified-1"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Data Structures and Algorithms · Week 3</p><h1>{title}</h1><p>Review draft · four primary and one complementary university courses · 88 worked problems · 80 examination rules · {lesson_count} lesson models and {problem_count} problem models</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="advanced-simulations.js?v=library-unified-1"></script><script src="diagram-layout.js?v=library-ports-3"></script><script src="math-layout.js"></script><script src="a_sort.js?v=library-unified-1"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/a_sort.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'a_sort-{suffix}.md'
 if p.exists():(R/f'dist/reviews/a_sort-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sorting audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="advanced-simulations.css?v=library-unified-1"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/a_sort.html">Sorting chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';a=json.loads(p.read_text(encoding='utf-8'));w=next(w for w in a if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='a_sort']+[dict(topicId='a_sort',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/a_sort.html',questionCount=88,authenticQuestionCount=2,originalQuestionCount=86,examNotesCount=80,sourceAuditUrl='reviews/a_sort-sources.html',qualityAuditUrl='reviews/a_sort-quality.html',animationCount=model_count,animationWalkthroughCount=model_count,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')];p.write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8')
print(f'Rendered only a_sort: 88 problems, 80 rules, {model_count} models.')
