"""Render the projection teaching draft without changing preceding chapters."""
from pathlib import Path
from html import escape
import json,re,sys
from projection_problem_figures import coefficients,polynomial
from teaching_prose_spacing import fix as clean_prose
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];B=R/'research';D=R/'dist/chapters'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
mathml.SYMBOLS.update(Pi='Π',ll='≪')
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):
 s=s.replace(r'P_{\rm new}',r'P_{\text{new}}').replace(r'P_{\rm wrong}',r'P_{\text{wrong}}')
 return re.sub(r'<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',mathml.markdown_math(s,md))
def model(title,spec):
 return '<section class="pr-model" tabindex="0" data-pr-spec="'+escape(json.dumps(spec),quote=True)+'"><h3>'+escape(title)+'</h3><div class="pr-controls"><button type="button" data-reset>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play>Play</button><button type="button" data-next>Next</button><label>Checkpoint<input type="range" data-seek min="0" value="0" aria-label="Projection checkpoint"></label></div><div class="pr-stage"></div><p class="pr-caption"></p><p class="pr-why"></p><p class="pr-progress" aria-live="polite"></p><div class="pr-formula"></div><div class="pr-print"></div></section>'
base=(B/'l_projection.en.md').read_text(encoding='utf8')
base=base.split('## Draft completion boundary')[0].split('\n',1)[1]
base=base.replace('Authoring draft: the sections below have been written, but the complete problem bank, final examination rules, models, source comparison and independent review are still pending. This draft is not yet a library chapter.','Review draft. This chapter has a source-specific comparison, complete worked bank, final examination decisions and compact geometric laboratories. Its recorded audits describe the checks performed; student approval is separate.')
base=base.replace('The working synthesis uses','The core synthesis uses').replace('Exact reading ranges, conventions and the pending comparison are in the source audit.','Exact reading ranges, conventions and the completed bounded comparison are in the source audit.').replace('Oxford M1 Linear Algebra I','Oxford M1 Linear Algebra I (metric and adjoint foundations)')
sections=re.split(r'(?=^## )',base,flags=re.M)
lesson_models={3:('Closest point and its perpendicular residual',dict(kind='projection',u=[2,1],b=[1,3])),9:('An oblique idempotent is not a closest-point map',dict(kind='oblique',t=2,b=[0,1])),13:('Weighted projection: coordinate angles can mislead',dict(kind='projection',u=[1,1],b=[2,-1],w=[1,4])),15:('A two-dimensional affine analogue',dict(kind='affine',n=[1,2],d=3,b=[3,1])),17:('Finite alternating projection cycles',dict(kind='alternating',angle=45,b=[1,0]))}
lesson=''
for section in sections:
 lesson+=text(section)
 m=re.match(r'## (\d+)\.',section)
 if m and int(m[1])in lesson_models:
  title,spec=lesson_models[int(m[1])];lesson+=model(title,spec)
lesson+=text((B/'l_projection-extensions.en.md').read_text(encoding='utf8'))
lesson+=model('Reflection fixes the line and reverses the residual',dict(kind='reflection',u=[1,-1],b=[3,0]))
raw=(B/'l_projection-worked-bank.en.md').read_text(encoding='utf8').split('## Problem 1.',1)[1].split('## Current completion boundary')[0]
raw='## Problem 1.'+raw+'\n'+(B/'l_projection-more-problems.en.md').read_text(encoding='utf8')
bank=[]
visual={1:dict(kind='plane',b=[2,1,0]),4:dict(kind='projection',u=[1,1],b=[2,-1],w=[1,4]),7:dict(kind='alternating',angle=45,b=[1,0]),10:dict(kind='oblique',t=2,b=[0,1]),17:dict(kind='reflection',u=[1,-1],b=[3,0]),18:dict(kind='alternating',angle=60,b=[1,0]),25:dict(kind='affine',n=[1,1],d=1,b=[0,0],w=[1,4])}
for n,title,body in re.findall(r'^## Problem (\d+)\. (.+)\n([\s\S]*?)(?=^## Problem |\Z)',raw,re.M):
 stem,answer=body.strip().removeprefix('**Question.** ').split('**Solution.** ',1)
 # Q25's figure explicitly compares the ordinary coordinate analogue: the weighted
 # answer is separately illustrated by the actual weighted generator model in Q4.
 extra=model('Finite geometry for this problem',visual[int(n)])if int(n)in visual else ''
 if n=='2':extra+=coefficients().replace('class="pr-model"','class="pr-model pr-static"')
 if n=='34':extra+=polynomial().replace('class="pr-model"','class="pr-model pr-static"')
 origin='Original problem; independently derived solution.'
 if n=='13':origin='Berkeley Math54 projection example, independently explained and checked.'
 if n in ['29','30','31','32']:origin='MIT18.06SC Session2.3 exercise reconstruction; independently derived explanation. See exact exercise numbers in the question.'
 bank.append(dict(id='projection-'+n,title=title,stem=stem,solution=answer,origin=origin))
 lesson+='<section class="exam-question" id="problem-'+n+'" data-source-id="projection-'+n+'"><h3>Problem '+n+'. '+escape(title)+'</h3><p class="exam-provenance">'+origin+'</p>'+text(stem)+'<details class="exam-solution"><summary>Read the complete solution and independent checks</summary>'+text(answer)+extra+'</details></section>'
assert len(bank)==50
(B/'l_projection-questions.json').write_text(json.dumps(bank,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
# Retain authentic provenance without pretending these revisits are distinct new questions.
auth=json.loads((B/'l_orthogonality-authentic.json').read_text(encoding='utf8'))
lesson+='<h2 id="archive">Authentic examination revisits and a matrix-space extension</h2><p>These two archive questions were also used in the orthogonality chapter. They are explicit revisits, not newly discovered distinct examination items. The PhD item tests this chapter directly; the MSc item is followed by an additional projection derivation. Answers are independently derived, not an official key.</p>'
from urllib.parse import quote
for q in auth:
 url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
 solution=q['solution']
 if q['id']=='MS_CS_1405_Q41':solution+='\n\n'+r'For a real symmetric matrix $X$, the closest trace-zero symmetric matrix under the Frobenius product is $X-\operatorname{tr}(X)I/4$. It is feasible because its trace is zero. The residual is the scalar matrix $\operatorname{tr}(X)I/4$, perpendicular to every trace-zero symmetric matrix since its Frobenius product with $Y$ is $\operatorname{tr}(X)\operatorname{tr}(Y)/4=0$. This proves optimality and uniqueness by the same squared-distance theorem. For $X=\operatorname{diag}(1,2,3,4)$, subtract $5I/2$, giving diagonal $(-3/2,-1/2,1/2,3/2)$. The squared residual norm is $4(5/2)^2=25$. Removing the entire diagonal instead discards additional feasible trace-zero directions and is not the closest point in general.'
 lesson+='<section class="exam-question" id="'+q['id']+'"><h3>'+escape(q['booklet'])+' · Question '+str(q['questionNumber'])+'</h3><p><a href="'+escape(url)+'">Original booklet · PDF page '+str(q['pdfPage'])+'</a></p>'+text(q['stem'])+'<ol>'+''.join('<li>'+text(o)+'</li>'for o in q['options'])+'</ol><details class="exam-solution"><summary>Read the independently derived complete answer</summary><p>Correct option: '+str(q['answer'])+'.</p>'+text(solution)+'</details></section>'
review=(B/'l_projection-review.en.md').read_text(encoding='utf8')
for block in review.split('\n\n'):
 m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
 lesson+=('<section class="review-rule"><h4>Decision '+m[1]+'</h4>'+text(m[2])+'</section>')if m else text(block)
lesson+='<h2 id="laboratory">Editable geometry laboratory</h2><p>Choose an angle, input coordinates and a positive vertical weight. Every run begins paused. Coordinate arrows are drawn in an ordinary coordinate plane; when the weight differs from one, the perpendicularity certificate uses the declared weighted product. The display rounds decimals to four places; it does not assert exact decimal arithmetic.</p><form id="pr-explorer"><label>Line angle in degrees<input name="angle" type="number" min="0" max="90" step="1" value="30"></label><label>Input x coordinate<input name="x" type="number" min="-5" max="5" step="0.25" value="1"></label><label>Input y coordinate<input name="y" type="number" min="-5" max="5" step="0.25" value="3"></label><label>Vertical metric weight<input name="weight" type="number" min="1" max="5" step="0.25" value="1"></label><button type="submit">Build my projection walkthrough</button></form><p id="pr-error" role="alert"></p><div id="pr-explorer-output"></div>'
refs=(B/'l_projection-source-audit.md').read_text(encoding='utf8').split('## Written references\n',1)[1].split('\n## ',1)[0]
lesson+=text('## References\n\n'+refs)
lesson=lesson.replace('<h3>Problem 1.','<h2 id="questions">Fifty worked mathematical and conceptual problems</h2><h3>Problem 1.',1)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Orthogonal Projections and Projection Matrices · Doctoral CSE1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="l_projection.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#library">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Linear Algebra · New chapter review draft</p><h1>Orthogonal Projections and Projection Matrices</h1><p>Four core university courses · 25 teaching sections · 50 fully worked problems plus two authentic examination revisits · 50 final decisions · compact geometric walkthroughs</p><p class="pr-subtitle">Source comparison and independent checks: <a href="../reviews/l_projection-sources.html">source audit</a> · <a href="../reviews/l_projection-quality.html">quality and coverage audit</a></p></header><nav class="toc"><a href="#questions">Worked problems</a> · <a href="#archive">Authentic examinations</a> · <a href="#summary">Summary and final decisions</a> · <a href="#laboratory">Editable geometry</a> · <button id="show-solutions" type="button">Open all solutions</button></nav><article class="lesson">'''+lesson+'''</article></main><script src="l_projection.js"></script><script>document.getElementById('show-solutions').onclick=()=>document.querySelectorAll('.exam-solution').forEach(d=>d.open=true);addEventListener('beforeprint',()=>document.querySelectorAll('.exam-solution').forEach(d=>d.open=true));</script></body></html>'''
page=page.replace('<h2>Summary:','<h2 id="summary">Summary:',1)
assert '$'not in page and '<!--'not in page
page=clean_prose(page);(D/'l_projection.html').write_text(page,encoding='utf8')
for suffix,label in [('source-audit','sources'),('quality-audit','quality')]:
 p=B/f'l_projection-{suffix}.md'
 if p.exists():(R/f'dist/reviews/l_projection-{label}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Projection chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p><a href="../chapters/l_projection.html">Projection chapter</a></p><article class="lesson">'+text(p.read_text(encoding='utf8'))+'</article></main></body></html>',encoding='utf8')
print({'originalOrCourseProblems':len(bank),'authenticRevisits':len(auth),'words':len(re.sub('<[^>]+>',' ',page).split()),'math':page.count('<math '),'models':page.count('data-pr-spec=')})
