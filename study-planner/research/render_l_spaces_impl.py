"""Render only the active review draft; preceding approved chapter files are read-only here."""
from pathlib import Path
from html import escape as e
import json,re,sys,ast
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(star='⋆',odot='⊙',varnothing='∅',subsetneq='⊊',setminus='∖');mathml.SYMBOLS.update(Phi='Φ',inf='inf',downarrow='↓',uparrow='↑')
mathml.SYMBOLS.update(gamma=chr(947));mathml.SYMBOLS.update(Pr='Pr',Vert='‖',ell='ℓ')
oldbase=mathml.Parser.base
def base(self):
 self.skip()
 if self.s.startswith(r'\widetilde',self.i):
  self.i+=len(r'\widetilde');return '<mover>'+self.group()+'<mo>~</mo></mover>'
 marker=r'\begin{cases}'
 if self.s.startswith(marker,self.i):
  self.i+=len(marker);stop=self.s.index(r'\end{cases}',self.i);s=self.s[self.i:stop];self.i=stop+len(r'\end{cases}')
  return '<mrow><mo>{</mo><mtable columnalign="left left">'+''.join('<mtr>'+''.join('<mtd>'+mathml.Parser(c).seq()+'</mtd>' for c in row.split('&'))+'</mtr>' for row in s.split(r'\\'))+'</mtable></mrow>'
 value=oldbase(self)
 value=re.sub(r'<mi>(Var|Cov|med|sign)</mi>',r'<mi mathvariant="normal">\1</mi>',value)
 return value.replace('<mo>-</mo>','<mo>−</mo>')
mathml.Parser.base=base
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef) and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
from math_typography import normalize_math,normalize_scripts
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):
 s=s.replace(r'\bigl','').replace(r'\bigr','').replace(r'\mathbin{\oplus}',r'\oplus ')
 s=re.sub(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',lambda m:m[0].replace('Var(',r'\operatorname{Var}(').replace('Cov(',r'\operatorname{Cov}(').replace('med(',r'\operatorname{med}(').replace('med_i',r'\operatorname{med}_i').replace('sign(',r'\operatorname{sign}('),s)
 return normalize_scripts(normalize_math(mathml.markdown_math(s,md)))
data=json.loads((R/'dist/chapters/l_spaces-models.json').read_text(encoding='utf-8'));by={m['id']:m for m in data['models']}
def trace(id):
 m=by[id];f=m['frames'][0]
 return f'''<section class="vs-model" data-vs-model="{e(id)}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p>{e(m['invariant'])}</p><div class="vs-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2600">Slow</option><option value="1800" selected>Normal</option><option value="1300">Fast</option></select></label><label>Step<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} step"></label></div><div class="vs-stage">{f['svg']}</div><p class="vs-caption">{e(f['caption'])}</p><p data-progress>Step 1 of {len(m['frames'])}</p><div class="vs-formula formula-block">{f['formulaHtml']}</div><div class="vs-print"></div></section>'''
def item(q,n,auth=False):
 title=q['title'];provenance=e(q.get('origin',''));options='';answer=''
 if auth:
  from urllib.parse import quote
  url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
  provenance=f'<a href="{e(url)}">{e(q["booklet"].replace("_"," "))} · Q{q["questionNumber"]} · PDF page {q["pdfPage"]}</a>. Independently derived answer; not an official key.'
  options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(s)+'</div></div>' for i,s in enumerate(q['options'],1))+'</div>'
  answer='<p><strong>Correct option: '+str(q['answer'])+'.</strong></p>'
 visual=(trace(q['modelId']) if q.get('modelId') else '')+''.join(trace(id) for id in q.get('additionalModelIds',[]))
 if q.get('modelId')=='bin-three-third':visual='<p class="visual-scope">Worked specialization: n = 3 and success probability 1/3. The symbolic argument above applies to all stated n; the diagram does not replace that proof.</p>'+visual
 return '<section class="exam-question" data-source-id="'+e(q['id'])+'" data-kind="'+('authentic' if auth else 'original')+'"><h3>Question '+str(n)+'. '+e(title)+'</h3><p class="exam-label">'+('Authentic examination · checked English adaptation' if auth else 'Original or independently reconstructed course problem · Foundational checks and Medium–Hard synthesis')+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])+options+'<details class="exam-solution"><summary>Read the complete solution and reasoning</summary>'+answer+text(q['solution'])+visual+'</details></section>'
qs=json.loads((B/'l_spaces-questions.json').read_text());auth=json.loads((B/'l_spaces-authentic.json').read_text())
bank='<h3 id="authentic-questions">Authentic examinations: structured dimension and basis-defined projection</h3>'+''.join(item(q,i,True) for i,q in enumerate(auth,1))+'<h3 id="original-questions">Original and reconstructed mathematical/conceptual problems</h3>'+''.join(item(q,i) for i,q in enumerate(qs,1))
rules=[]
for block in (B/'l_spaces-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='<section class="lab"><form id="vs-form"><label>Generator matrix<input name="matrix" value="1,2,0,3;2,4,1,4;3,6,2,5"></label><label>Target vector<input name="target" value="1,3,5"></label><button type="submit">Compute bases, dependencies and membership</button></form><p id="vs-error" role="alert"></p><p>Enter generators as columns: separate columns with commas and rows with semicolons. Use 2–4 rows, 1–5 columns and integer entries from −20 to 20. The target has one entry per row. Exact rational arithmetic handles every row operation, including fractions. The original generators are retained; an independently tracked row operator checks every intermediate matrix. Invalid input preserves the previous result. Every walkthrough starts paused.</p><div id="vs-output"></div></section>'
source=(B/'l_spaces.en.md').read_text(encoding='utf-8').split('\n',1)[1].replace('<!-- INCLUDE: problems -->',bank).replace('<!-- INCLUDE: review -->',''.join(rules)).replace('<!-- LAB: spaces -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM: '+k+' -->',''.join(trace(id) for id in ids))
body=text(source);anchors=['sources', 'axioms', 'consequences', 'subspace', 'constraints', 'span', 'independence', 'basis', 'exchange', 'dimension', 'computation', 'functions', 'interpolation', 'matrix-spaces', 'sum-intersection', 'dimension-formula', 'direct-sums', 'complements', 'coordinate-change', 'quotients', 'fields', 'parameters', 'infinite-boundaries', 'workflow', 'summary', 'problems', 'review', 'laboratory', 'references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='Vector Spaces, Subspaces, Bases, and Dimension';nav=' '.join('<a href="#'+k+'">'+({'ecdf':'ECDF','qq-time':'Q–Q and time','bessel':'Bessel correction','association':'Paired association'}.get(k,k.replace('-',' ').capitalize()))+'</a>' for k in anchors)
modelCount=len(data['models']);frameCount=sum(len(m['frames']) for m in data['models'])
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="teaching-transitions.css"><link rel="stylesheet" href="l_spaces.css"><link rel="stylesheet" href="advanced-simulations.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Linear Algebra · Week 3</p><h1>{title}</h1><p>Review draft · four core written courses from four universities · 82 worked problems · 80 examination rules · {modelCount} exact-state models / {frameCount} stored checkpoints</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="math-layout.js?v=79"></script><script src="diagram-layout.js"></script><script src="teaching-transitions.js"></script><script src="advanced-simulations.js"></script><script src="l_spaces.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/l_spaces.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'l_spaces-{suffix}.md'
 if p.exists():(R/f'dist/reviews/l_spaces-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Vector spaces chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/l_spaces.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/l_spaces.html">Vector spaces chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js?v=79"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';all=json.loads(p.read_text());w=next(w for w in all if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='l_spaces']+[dict(topicId='l_spaces',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/l_spaces.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/l_spaces-sources.html',qualityAuditUrl='reviews/l_spaces-quality.html',animationCount=modelCount,animationWalkthroughCount=modelCount,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')]
p.write_text(json.dumps(all,indent=2)+'\n',encoding='utf-8')
print(f'Rendered only l_spaces: 82 questions, 80 rules, {modelCount} models, {frameCount} checkpoints.')
