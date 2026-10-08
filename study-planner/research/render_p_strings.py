"""Render only the active review draft; preceding approved chapter files are read-only here."""
from pathlib import Path
from html import escape as e
import json,re,sys,ast
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(Sigma=chr(931),varepsilon=chr(949))
mathml.SYMBOLS.update(Longrightarrow='⟹',varepsilon='ε');mathml.SYMBOLS.update(star='⋆',odot='⊙',varnothing='∅',subsetneq='⊊',setminus='∖');mathml.SYMBOLS.update(Phi='Φ',inf='inf',downarrow='↓',uparrow='↑')
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
data=json.loads((R/'dist/chapters/p_strings-models.json').read_text(encoding='utf-8'));by={m['id']:m for m in data['models']}
def trace(id):
 m=by[id];f=m['frames'][0]
 return f'''<section class="st-model" data-st-model="{e(id)}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p>{e(m['invariant'])}</p><div class="st-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2600">Slow</option><option value="1800" selected>Normal</option><option value="1300">Fast</option></select></label><label>Step<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} step"></label></div><div class="st-stage">{f['svg']}</div><p class="st-caption">{e(f['caption'])}</p><p data-progress>Step 1 of {len(m['frames'])}</p><div class="st-formula formula-block">{f['formulaHtml']}</div><div class="st-print"></div></section>'''
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
qs=json.loads((B/'p_strings-questions.json').read_text());auth=json.loads((B/'p_strings-authentic.json').read_text())
bank='<h3 id="authentic-questions">Authentic examination: abstract-string counting bridge</h3>'+''.join(item(q,i,True) for i,q in enumerate(auth,1))+'<h3 id="original-questions">Original and reconstructed mathematical/conceptual problems</h3>'+''.join(item(q,i) for i,q in enumerate(qs,1))
rules=[]
for block in (B/'p_strings-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='<section class="lab"><form id="st-form"><label>Operation<select name="operation"><option value="copy">Whole-string copy</option><option value="ncpy">Bounded padded copy</option><option value="append" selected>Append selected content</option><option value="compare">Bounded unsigned comparison</option><option value="match">Find all overlapping matches</option><option value="scan">Scan source extent</option><option value="move">Move bytes inside destination</option><option value="insert">Insert first source byte</option><option value="delete">Delete content interval</option><option value="reverse">Reverse destination content</option><option value="compact">Remove first source byte</option><option value="tokens">Split on first source byte</option></select></label><label>Source / pattern / selected byte<input name="source" value="XY"></label><label>Initial destination / text<input name="destination" value="orbit"></label><label>Destination capacity<input name="capacity" type="number" min="1" max="16" value="10"></label><label>Copy, append or comparison limit<input name="limit" type="number" min="0" max="16" value="16"></label><label>Insertion or deletion position<input name="position" type="number" min="0" max="15" value="2"></label><label>Deleted content count<input name="remove" type="number" min="0" max="15" value="1"></label><label>Move source offset<input name="from" type="number" min="0" max="15" value="0"></label><label>Move destination offset<input name="to" type="number" min="0" max="15" value="1"></label><label>Move byte count<input name="count" type="number" min="0" max="16" value="3"></label><button type="submit">Build and inspect the byte trace</button></form><p id="st-error" role="alert"></p><p>Use at most fifteen entered printable ASCII bytes; \\0 inserts an embedded zero. A final source zero is added automatically. Destination capacity is between one and sixteen bytes. Only the selected operation\'s parameters apply. All traces start paused. Invalid inputs preserve the preceding valid result. Scan examines the displayed source extent; capacity controls the destination object. The laboratory\'s zero-filled unused destination cells are initialized model data, never a claim that automatic C arrays initialize themselves.</p><div id="st-output"></div></section>'
source=(B/'p_strings.en.md').read_text(encoding='utf-8').split('\n',1)[1].replace('<!-- INCLUDE: problems -->',bank).replace('<!-- INCLUDE: review -->',''.join(rules)).replace('<!-- LAB: strings -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM: '+k+' -->',''.join(trace(id) for id in ids))
body=text(source);anchors=['sources','representation','nulls','initialization','extent','scan','copy','bounded-copy','append','ownership','overlap','compare','spans','match','reverse','compact','tokens','input','formatting','unicode','tables','buffers','counting','summary','problems','review','laboratory','references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==81 and body.count('class="review-rule"')==80
title='Strings and Terminators: Representation, Contracts, and Algorithms in C17';nav=' '.join('<a href="#'+k+'">'+({'ecdf':'ECDF','qq-time':'Q–Q and time','bessel':'Bessel correction','association':'Paired association'}.get(k,k.replace('-',' ').capitalize()))+'</a>' for k in anchors)
modelCount=len(data['models']);frameCount=sum(len(m['frames']) for m in data['models'])
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="teaching-transitions.css"><link rel="stylesheet" href="p_strings.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Programming · Week 3</p><h1>{title}</h1><p>Review draft · four core written courses from four universities · 81 worked problems · 80 examination rules · {modelCount} byte-memory models / {frameCount} stored checkpoints</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="math-layout.js?v=79"></script><script src="diagram-layout.js"></script><script src="teaching-transitions.js"></script><script src="p_strings.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/p_strings.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'p_strings-{suffix}.md'
 if p.exists():(R/f'dist/reviews/p_strings-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Strings and terminators chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/p_strings.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/p_strings.html">Strings and terminators chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js?v=79"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';all=json.loads(p.read_text());w=next(w for w in all if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='p_strings']+[dict(topicId='p_strings',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/p_strings.html',questionCount=81,authenticQuestionCount=1,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/p_strings-sources.html',qualityAuditUrl='reviews/p_strings-quality.html',animationCount=modelCount,animationWalkthroughCount=modelCount,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')]
p.write_text(json.dumps(all,indent=2)+'\n',encoding='utf-8')
print(f'Rendered only p_strings: 81 questions, 80 rules, {modelCount} models, {frameCount} checkpoints.')
