"""Render only the active review draft; preceding approved chapter files are read-only here."""
from pathlib import Path
from html import escape as e
import json,re,sys,ast
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));sys.path.insert(0,str(B))
import mathml
mathml.SYMBOLS.update(Phi='Φ',inf='inf')
mathml.SYMBOLS.update(Pr='Pr',Vert='‖',ell='ℓ')
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
 s=s.replace(r'\bigl','').replace(r'\bigr','')
 s=re.sub(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',lambda m:m[0].replace('Var(',r'\operatorname{Var}(').replace('Cov(',r'\operatorname{Cov}(').replace('med(',r'\operatorname{med}(').replace('med_i',r'\operatorname{med}_i').replace('sign(',r'\operatorname{sign}('),s)
 return normalize_scripts(normalize_math(mathml.markdown_math(s,md)))
data=json.loads((R/'dist/chapters/s_descriptive-models.json').read_text(encoding='utf-8'));by={m['id']:m for m in data['models']}
def trace(id):
 m=by[id];f=m['frames'][0]
 return f'''<section class="stat-model" data-stat-model="{e(id)}" tabindex="0" aria-label="{e(m['title'])}"><h3>{e(m['title'])}</h3><p>{e(m['invariant'])}</p><div class="stat-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev disabled>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Speed<select data-speed><option value="2600">Slow</option><option value="1800" selected>Normal</option><option value="1300">Fast</option></select></label><label>Step<input type="range" data-seek min="0" max="{len(m['frames'])-1}" value="0" aria-label="{e(m['title'])} step"></label></div><div class="stat-stage">{f['svg']}</div><p class="stat-caption">{e(f['caption'])}</p><p data-progress>Step 1 of {len(m['frames'])}</p><div class="stat-formula formula-block">{f['formulaHtml']}</div><div class="stat-print"></div></section>'''
def item(q,n,auth=False):
 title=q['title'];provenance=e(q.get('origin',''));options='';answer=''
 if auth:
  from urllib.parse import quote
  url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
  provenance=f'<a href="{e(url)}">{e(q["booklet"].replace("_"," "))} · Q{q["questionNumber"]} · PDF page {q["pdfPage"]}</a>. Independently derived answer; not an official key.'
  options='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(s)+'</div></div>' for i,s in enumerate(q['options'],1))+'</div>'
  answer='<p><strong>Correct option: '+str(q['answer'])+'.</strong></p>'
 visual=trace(q['modelId']) if q.get('modelId') else ''
 return '<section class="exam-question" data-source-id="'+e(q['id'])+'" data-kind="'+('authentic' if auth else 'original')+'"><h3>Question '+str(n)+'. '+e(title)+'</h3><p class="exam-label">'+('Authentic examination · checked English adaptation' if auth else 'Original or independently reconstructed course problem · Medium–Hard')+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])+options+'<details class="exam-solution"><summary>Read the complete solution and reasoning</summary>'+answer+text(q['solution'])+visual+'</details></section>'
qs=json.loads((B/'s_descriptive-questions.json').read_text());auth=json.loads((B/'s_descriptive-authentic.json').read_text())
bank='<h3 id="authentic-questions">Authentic population-moment and normal-standardization bridges</h3>'+''.join(item(q,i,True) for i,q in enumerate(auth,1))+'<h3 id="original-questions">Original and reconstructed mathematical/conceptual problems</h3>'+''.join(item(q,i) for i,q in enumerate(qs,len(auth)+1))
rules=[]
for block in (B/'s_descriptive-review.en.md').read_text(encoding='utf-8').split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block);rules.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab="""<section class="lab"><form id="stat-form"><label>Exact model<select name="kind"><option value="histogram">Density histogram</option><option value="ecdf">Empirical CDF</option><option value="mean">Squared loss and mean</option><option value="median">Absolute loss and median</option><option value="quantiles">Quantile conventions</option><option value="variance">Residuals and variance</option><option value="affine">Affine transformation</option><option value="box">Type-7 boxplot</option><option value="pooling">Pool two groups</option><option value="stream">Welford stream</option><option value="correlation">Paired correlation</option><option value="qq">Two-sample Q–Q</option><option value="ma">Trailing moving average</option><option value="ewma">EWMA, initial value zero</option></select></label><label>Values / first group<input name="values" value="0,1,1,2,3,4" aria-describedby="stat-limits"></label><label>Scale / window / lambda<input name="parameter" value="3" aria-describedby="stat-limits"></label><label>Bin edges / second group / translation<input name="other" value="0,1,2,4" aria-describedby="stat-limits"></label><button type="submit">Compute the exact teaching trace</button></form><p id="stat-error" role="alert"></p><p id="stat-limits">Enter 1–12 finite values per list between −999 and 999. Histogram mode needs strictly increasing edges covering every observation. Pooling and Q–Q accept unequal group sizes; correlation needs equal lengths and labels constant-column correlation undefined. Affine mode uses the numeric scale (−20 to 20) and exactly one translation in the second field. Moving average uses integer window 1–12 and shorter windows at startup. EWMA uses lambda greater than zero and at most one, with initial value zero. Other modes ignore unused fields. Boxplots use type 7 and strict 1.5-IQR fences. Invalid submissions preserve the previous model. The displayed arithmetic uses finite precision; exact rational examples are checked separately.</p><div id="stat-output"></div></section>"""
source=(B/'s_descriptive.en.md').read_text(encoding='utf-8').split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(rules)).replace('<!-- LAB:statistics -->',lab)
for k,ids in data['groups'].items():source=source.replace('<!-- SIM:'+k+' -->',''.join(trace(id) for id in ids))
body=text(source);anchors=['sources', 'units', 'histograms', 'ecdf', 'mean', 'quantiles', 'variance', 'bessel', 'affine', 'robust', 'shape', 'bounds', 'grouped', 'pooling', 'stream', 'association', 'qq-time', 'summary', 'problems', 'review', 'laboratory', 'references'];it=iter(anchors)
body=re.sub(r'<h2>(.*?)</h2>',lambda m:'<h2 id="'+next(it)+'">'+m[1]+'</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==82 and body.count('class="review-rule"')==80
title='Descriptive Statistics and Exploratory Data Analysis';nav=' '.join('<a href="#'+k+'">'+({'ecdf':'ECDF','qq-time':'Q–Q and time','bessel':'Bessel correction','association':'Paired association'}.get(k,k.replace('-',' ').capitalize()))+'</a>' for k in anchors)
modelCount=len(data['models']);frameCount=sum(len(m['frames']) for m in data['models'])
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="teaching-transitions.css"><link rel="stylesheet" href="s_descriptive.css"><link rel="stylesheet" href="advanced-simulations.css?v=library-unified-1"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-3">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Probability and Statistics · Week 3</p><h1>{title}</h1><p>Review draft · five reviewed university courses · 82 worked problems · 80 examination rules · {modelCount} exact-state models / {frameCount} stored checkpoints</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">Chapter library</a></p></main><script src="advanced-simulations.js?v=library-unified-1"></script><script src="math-layout.js"></script><script src="diagram-layout.js"></script><script src="teaching-transitions.js?v=library-unified-1"></script><script src="s_descriptive.js"></script><script src="exam-calibration.js"></script></body></html>'''
(R/'dist/chapters/s_descriptive.html').write_text(page,encoding='utf-8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f's_descriptive-{suffix}.md'
 if p.exists():(R/f'dist/reviews/s_descriptive-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Descriptive statistics chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/s_descriptive.css"><link rel="stylesheet" href="advanced-simulations.css?v=library-unified-1"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/s_descriptive.html">Descriptive statistics chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf-8'))+'</article></main><script src="../chapters/math-layout.js"></script></body></html>',encoding='utf-8')
p=R/'dist/lessons.json';all=json.loads(p.read_text());w=next(w for w in all if w['week']==3)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='s_descriptive']+[dict(topicId='s_descriptive',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/s_descriptive.html',questionCount=82,authenticQuestionCount=2,originalQuestionCount=80,examNotesCount=80,sourceAuditUrl='reviews/s_descriptive-sources.html',qualityAuditUrl='reviews/s_descriptive-quality.html',animationCount=modelCount,animationWalkthroughCount=modelCount,animationReviewState='awaiting_user_approval',visualRevisionState='awaiting_user_approval')]
p.write_text(json.dumps(all,indent=2)+'\n',encoding='utf-8')
print(f'Rendered only s_descriptive: 82 questions, 80 rules, {modelCount} models, {frameCount} checkpoints.')
