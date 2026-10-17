"""Assemble a full English chapter with strict native mathematics and local assets."""
from pathlib import Path
from html import escape
from markdown_it import MarkdownIt
import json,re,sys
from teaching_prose_spacing import fix
R=Path(__file__).resolve().parents[1];B=R/'research';D=R/'dist/chapters'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
mathml.SYMBOLS.update(varepsilon='ε',Sigma='Σ',Longrightarrow='⇒')
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',mathml.markdown_math(s,md))
def model(id,title,editable=False):
 return '<section class="ls-model" data-ls-model="'+id+'"'+(' id="ls-editable-player"'if editable else'')+'><h3>'+escape(title)+'</h3><div class="ls-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play aria-pressed="false">Play</button><button type="button" data-next>Next</button><label>Checkpoint <input type="range" data-seek min="0" value="0" aria-label="'+escape(title)+' checkpoint"></label></div><div class="ls-stage"></div><p class="ls-caption" aria-live="polite"></p><p class="ls-why"></p><div class="ls-print"></div></section>'
raw=(B/'l_leastsquares.en.md').read_text(encoding='utf8').split('\n',1)[1]
lesson='';models={6:('line','Vertical response errors and the fitted line'),9:('householder','One reflector, then a triangular fit'),11:('deficient','Move through nonunique coefficient descriptions'),12:('weighted-constant','Weights change the selected constant'),13:('constraint','Search only along the feasible line'),14:('ridge','The complete regularized objective'),15:('leverage','Delete one observation and predict it'),17:('sensitivity','A small data change and large coefficient changes'),19:('discrete-noise','A discrete dependence counterexample')}
for part in re.split(r'(?=^## )',raw,flags=re.M):
 lesson+=render(part);m=re.match(r'## (\d+)\.',part)
 if m and int(m[1])in models:
  id,title=models[int(m[1])];lesson+=model(id,title)
qs=[];bank=(B/'l_leastsquares-problems.en.md').read_text(encoding='utf8')
lesson+=render(bank.split('## Problem 1.')[0]);visual={1:'line',6:'deficient',11:'householder',16:'weighted-constant',17:'weighted-line',21:'constraint',24:'ridge-identity',29:'leverage',35:'sensitivity',40:'discrete-noise'}
for n,title,body in re.findall(r'^## Problem (\d+)\. (.+)\n([\s\S]*?)(?=^## Problem |\Z)',bank,re.M):
 stem,answer=body.strip().removeprefix('**Question.** ').split('**Solution.** ',1);id='LS'+n.zfill(2)
 origin={1:'Course reconstruction: MIT18.06SC Session2.3 worked line fit; independently derived explanation.',2:'Course reconstruction: Berkeley Math54 Least-Squares Problems, page2; independently derived explanation.',3:'Course reconstruction: Berkeley Math54 Least-Squares Problems, pages3–4; independently derived explanation.',15:'Course-derived conceptual extension: ETH Linear Algebra PartII Example6.1.4; independently derived obstruction.'}.get(int(n),'Original mathematical/conceptual problem; independently derived solution.')
 qs.append(dict(id=id,title=title,stem=stem,solution=answer,origin=origin))
 lesson+='<section class="exam-question" id="problem-'+n+'" data-source-id="'+id+'"><h3>Problem '+n+'. '+escape(title)+'</h3><p class="exam-provenance">'+escape(origin)+'</p>'+render(stem)+'<details class="exam-solution"><summary>Read the complete mathematical construction and checks</summary>'+render(answer)+(model(visual[int(n)],'Walk through this problem\'s actual model')if int(n)in visual else'')+'</details></section>'
assert len(qs)==50
(B/'l_leastsquares-questions.json').write_text(json.dumps(qs,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
lesson+='<section id="authentic"><h2>Authentic doctoral examination revisit</h2><p>The following projection question also appears in earlier chapters. It is explicitly reused here as a least-squares optimality certificate, not counted as a newly discovered distinct archive item. The English adaptation retains the original option order; its answer is independently derived.</p>'
q=next(x for x in json.loads((B/'l_orthogonality-authentic.json').read_text(encoding='utf8'))if x['id']=='Phd_CS_1404_Q31')
lesson+='<section class="exam-question" data-source-id="'+q['id']+'"><h3>Authentic revisit: PhD CS1404, Question31</h3>'+render(q['stem'])+'<ol>'+''.join('<li>'+render(x)+'</li>'for x in q['options'])+'</ol><details class="exam-solution"><summary>Read the complete proof and least-squares connection</summary>'+render(q['solution']+r' **Least-squares connection.** Form the design $Q=[u_1\ \cdots\ u_n]$. Its independent orthonormal columns give coefficient vector $Q^Tx$, fitted vector $QQ^Tx=Px$, and residual $(I-P)x$. The Pythagorean identity proves global closest-point optimality and the correct contraction inequality. This is the same theorem used to solve a QR-transformed fit; it does not claim that the fitted norm exceeds the data norm.')+'</details></section></section>'
review=(B/'l_leastsquares-review.en.md').read_text(encoding='utf8')
for section in re.split(r'(?=^\d+\. )',review,flags=re.M):
 if re.match(r'^\d+\. ',section):lesson+='<section class="review-rule">'+render(section)+'</section>'
 else:lesson+=render(section)
lesson+='<section id="laboratory"><h2>Exact weighted-fitting laboratory</h2><p>Time inputs are fixed at1,2,3. Choose integer responses and positive integer weights. The laboratory solves with exact fractions and reports the normal-equation products. It teaches the declared model; no test answer is requested.</p><form id="ls-explorer"><div class="ls-inputs">'
for i,y in enumerate([1,2,2]):
 lesson+='<label>Response at time '+str(i+1)+'<input name="y'+str(i)+'" type="number" min="-10" max="10" step="1" value="'+str(y)+'" required></label><label>Weight at time '+str(i+1)+'<input name="w'+str(i)+'" type="number" min="1" max="9" step="1" value="1" required></label>'
lesson+='</div><label>Features <select name="model"><option value="line">Intercept and slope</option><option value="constant">Constant only</option></select></label><button type="submit">Compute the exact fit</button></form><p id="ls-error" role="alert"></p>'+model('line','Explore your own declared fitting model',True)+'<section id="ls-exact-output" aria-live="polite"></section></section>'
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Least Squares: Fitting, Computation and Estimation</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="l_projection.css"><link rel="stylesheet" href="l_leastsquares.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#library">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Linear algebra · completed author-review draft</p><h1>Least Squares</h1><p>Fitting, identifiability, computation and estimation</p><p>22teaching sections · 50worked mathematical/course problems · one explicit authentic examination revisit · 60final decisions</p><p><a href="../reviews/l_leastsquares-sources.html">Source comparison and actual reading</a> · <a href="../reviews/l_leastsquares-quality.html">Coverage and verification</a></p></header><article class="lesson">'''+lesson+'''</article></main><script src="l_leastsquares.js"></script><script>addEventListener('beforeprint',()=>document.querySelectorAll('.exam-solution').forEach(d=>d.open=true));</script></body></html>'''
(D/'l_leastsquares.html').write_text(fix(page),encoding='utf8')
print({'questions':len(qs)+1,'finalRules':page.count('class="review-rule"'),'models':page.count('data-ls-model=')})
