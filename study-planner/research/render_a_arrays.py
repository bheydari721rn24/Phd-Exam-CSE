"""Render the sole new chapter without rerendering approved chapters."""
from pathlib import Path
from html import escape as e
import ast,json,re,sys,hashlib,xml.etree.ElementTree as ET
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.SYMBOLS.update(ell='ℓ',supseteq='⊇',Phi='Φ')
original_base=mathml.Parser.base
def chapter_base(self):
 self.skip()
 marker=r'\begin{cases}'
 if self.s.startswith(marker,self.i):
  self.i+=len(marker);stop=self.s.index(r'\end{cases}',self.i);content=self.s[self.i:stop];self.i=stop+len(r'\end{cases}')
  rows=[row.split('&') for row in content.split(r'\\')]
  return '<mrow><mo>{</mo><mtable columnalign="left left">'+''.join('<mtr>'+''.join('<mtd>'+mathml.Parser(cell).seq()+'</mtd>' for cell in row)+'</mtr>' for row in rows)+'</mtable></mrow>'
 return original_base(self)
mathml.Parser.base=chapter_base
from mathml import render,width,markdown_math
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
for filename,names in [('build_correct_chapter.py',('scope_preserving_display',)),('exam-calibration/build.py',('prep','text')),('build_conditional_chapter.py',('item',))]:
 for f in ast.parse((B/filename).read_text(encoding='utf-8')).body:
  if isinstance(f,ast.FunctionDef) and f.name in names:exec(compile(ast.Module(body=[f],type_ignores=[]),filename,'exec'))
mathml.wrap_display=scope_preserving_display
data=json.loads((R/'dist/chapters/a_arrays-models.json').read_text());by={m['id']:m for m in data['models']}
def trace(id):
 m=by[id];f=m['frames'][0]
 return f'''<section class="arrays-model" data-arrays-model="{id}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p class="arrays-invariant"><strong>Model invariant.</strong> {e(m['invariant'])}</p><div class="arrays-stage">{f['svg']}</div><p class="arrays-caption" aria-live="polite">{e(f['caption'])}</p><div class="arrays-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2200">Slow</option><option value="1400" selected>Normal</option><option value="850">Fast</option></select></label><label>Checkpoint<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} checkpoint"></label></div><p class="arrays-progress" data-progress>Checkpoint 1 of {len(m['frames'])}</p><div class="formula-block arrays-formula">{f['formulaHtml']}</div><p class="arrays-error" hidden></p><div class="arrays-print-trace"></div></section>'''
q=json.loads((B/'a_arrays-questions.json').read_text());actual=json.loads((B/'a_arrays-authentic.json').read_text())
old_item=item
def item(q,n,authentic=False):
 h=old_item(q,n,authentic)
 if not authentic and q.get('options'):
  opts='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(v)+'</div></div>' for i,v in enumerate(q['options'],1))+'</div>'
  h=h.replace('<details class="exam-solution">',opts+'<details class="exam-solution">',1).replace('<summary>Read the complete derivation and reasoning</summary>','<summary>Read the complete derivation and reasoning</summary><p><strong>Correct option: '+str(q['answer'])+'.</strong></p>',1)
 return h
bank='<h3 id="authentic-questions">Authentic examination questions and conceptual bridges</h3>'+''.join(item(x,i,True).replace('Authentic examination · checked English translation','Authentic examination revisit · checked English adaptation') for i,x in enumerate(actual,1))
bank+='<h3 id="original-questions">Original and independently reconstructed course problems</h3>'+''.join(item(x,i) for i,x in enumerate(q,3))
rules=[]
for block in (B/'a_arrays-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='<section class="lab" id="arrays-lab"><form id="arrays-form"><label>Exact laboratory<select name="mode"><option value="growth">Geometric capacity growth</option><option value="shift">Stable array insertion</option><option value="reverse">Linked-list reversal</option><option value="floyd">Floyd cycle and entry</option></select></label><label data-modes="growth">Append count<input name="m" type="number" value="13" min="1" max="64"></label><label data-modes="growth">Initial capacity<input name="c0" type="number" value="1" min="1" max="16"></label><label data-modes="growth">Growth factor<input name="g" type="number" value="2" min="2" max="4"></label><label data-modes="shift">Array values<input name="values" type="text" value="2,4,6,8,10"></label><label data-modes="shift">Insertion rank<input name="index" type="number" value="2" min="0" max="8"></label><label data-modes="shift">New value<input name="value" type="number" value="9" min="-99" max="99"></label><label data-modes="reverse">Real nodes<input name="n" type="number" value="5" min="0" max="7"></label><label data-modes="floyd">Prefix links<input name="mu" type="number" value="3" min="0" max="5"></label><label data-modes="floyd">Cycle links<input name="lam" type="number" value="4" min="1" max="5"></label><button type="submit">Recompute the complete trace</button></form><p id="arrays-lab-error" class="arrays-lab-error" role="alert"></p><div id="arrays-output"></div><p>Growth permits 1–64 appends, initial capacity 1–16, and integer factor 2–4. Insertion permits 1–8 original values from −99 to 99 and any legal insertion rank. Reversal permits 0–7 nodes. Cycle mode permits prefix length 0–5 and cycle length 1–5. Counts exclude allocation and guard reads; cycle comparisons follow complete one-versus-two iterations. An invalid input leaves the last valid trace intact and displays an explanation.</p></section>'
source=(B/'a_arrays.en.md').read_text().split('\n',1)[1].replace(r'\mathbin{\mathrm{xor}}',r'\mathrm{xor}').replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:arrays -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM:'+k+' -->',''.join(trace(id) for id in ids))
body=text(source)
anchors=['sources','model','shifts','growth','amortization','singly','doubly','reverse','cycles','traversal','transformations','memory','sparse','summary','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body and '\x00' not in body
assert body.count('class="exam-question"')==86 and body.count('class="review-rule"')==80
title='Arrays, Linked Lists, and Operation Costs'
nav=' '.join('<a href="#'+k+'">'+k.capitalize()+'</a>' for k in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="a_arrays.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Data Structures and Algorithms · Week 3</p><h1>{title}</h1><p>Review draft · four primary university courses and two complementary courses · 86 worked problems · 80 examination rules · 20 dedicated concept traces</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="math-layout.js"></script><script src="a_arrays.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/a_arrays.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'a_arrays-{suffix}.md'
 if p.exists():(R/f'dist/reviews/a_arrays-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Arrays and linked lists audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/a_arrays.html">Arrays and linked lists chapter</a></p><article class="lesson">'+text(p.read_text())+'</article></main><script src="../chapters/math-layout.js"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';a=json.loads(p.read_text());w=next(w for w in a if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='a_arrays']+[dict(topicId='a_arrays',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/a_arrays.html',questionCount=86,authenticQuestionCount=2,originalQuestionCount=84,examNotesCount=80,sourceAuditUrl='reviews/a_arrays-sources.html',qualityAuditUrl='reviews/a_arrays-quality.html',animationCount=20,animationWalkthroughCount=20,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')];p.write_text(json.dumps(a,indent=2)+'\n')
