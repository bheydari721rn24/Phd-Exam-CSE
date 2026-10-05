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
data=json.loads((R/'dist/chapters/d_pigeonhole-models.json').read_text());by={m['id']:m for m in data['models']}
def trace(id):
 m=by[id];f=m['frames'][0]
 return f'''<section class="pigeonhole-model" data-pigeonhole-model="{id}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p class="pigeonhole-invariant"><strong>Model invariant.</strong> {e(m['invariant'])}</p><div class="pigeonhole-stage">{f['svg']}</div><p class="pigeonhole-caption" aria-live="polite">{e(f['caption'])}</p><div class="pigeonhole-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2200">Slow</option><option value="1400" selected>Normal</option><option value="850">Fast</option></select></label><label>Checkpoint<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} checkpoint"></label></div><p class="pigeonhole-progress" data-progress>Checkpoint 1 of {len(m['frames'])}</p><div class="formula-block pigeonhole-formula">{f['formulaHtml']}</div><p class="pigeonhole-error" hidden></p><div class="pigeonhole-print-trace"></div></section>'''
q=json.loads((B/'d_pigeonhole-questions.json').read_text());actual=json.loads((B/'d_pigeonhole-authentic.json').read_text())
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
for block in (B/'d_pigeonhole-review.en.md').read_text().split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='<section class="lab" id="pigeonhole-lab"><form id="pigeonhole-form"><label>Exact laboratory<select name="mode"><option value="occupancy">Occupancy and collision pairs</option><option value="prefix">Divisible contiguous blocks</option><option value="sequence">Strict monotone subsequences</option><option value="graph">Two-color complete graphs</option></select></label><label>Comma-separated integer values<input name="values" type="text" value="4,4,3,3,3" required></label><label>Positive modulus<input name="m" type="number" min="1" max="12" value="5"></label><label>Vertices<select name="n"><option value="5">Five</option><option value="6" selected>Six</option></select></label><label>Edge-color mask<input name="mask" type="number" min="0" max="32767" value="0"></label><button type="submit">Compute and draw the witness</button></form><div id="pigeonhole-output" aria-live="polite"></div><p>Occupancy mode permits one to eight bins and at most forty total objects. Prefix mode permits one to twelve values from −20 to 20 and modulus one to twelve. Sequence mode permits one to nine integer values from −20 to 20; duplicates are explicitly identified, and exhaustive index-subset enumeration checks the dynamic program. Graph mode permits five or six vertices and a legal integer bit mask: ten bits for five vertices, fifteen for six. Bits follow unordered edges in increasing lexicographic order. Blue is zero, red is one. A five-cycle counterexample uses five vertices and mask 665.</p></section>'
source=(B/'d_pigeonhole.en.md').read_text().split('\n',1)[1].replace(r'\mathbin{\mathrm{xor}}',r'\mathrm{xor}').replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:pigeonhole -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM:'+k+' -->',''.join(trace(id) for id in ids))
body=text(source)
anchors=['sources','assignment','average','capacity','collisions','residues','subsets','chains','geometry','subsequences','graphs','information','summary','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body and '\x00' not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='The Pigeonhole Principle: Sharp Guarantees, Hidden Classes, and Constructive Witnesses'
nav=' '.join('<a href="#'+k+'">'+k.capitalize()+'</a>' for k in anchors)
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="d_pigeonhole.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Discrete Mathematics · Week 3</p><h1>{title}</h1><p>Review draft · five primary written courses from four universities and a sixth complementary course · 82 worked problems · 80 examination rules · 18 dedicated concept traces</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="math-layout.js"></script><script src="d_pigeonhole.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/d_pigeonhole.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'd_pigeonhole-{suffix}.md'
 if p.exists():(R/f'dist/reviews/d_pigeonhole-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Inclusion-exclusion chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/d_pigeonhole.html">Inclusion-exclusion chapter</a></p><article class="lesson">'+text(p.read_text())+'</article></main><script src="../chapters/math-layout.js"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';a=json.loads(p.read_text());w=next(w for w in a if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='d_pigeonhole']+[dict(topicId='d_pigeonhole',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/d_pigeonhole.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/d_pigeonhole-sources.html',qualityAuditUrl='reviews/d_pigeonhole-quality.html',animationCount=18,animationWalkthroughCount=18,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')];p.write_text(json.dumps(a,indent=2)+'\n')
