"""Build only Bayes, retaining approved library content and typography."""
import ast,html,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from markdown_it import MarkdownIt
from math_typography import normalize_math,normalize_scripts
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
sys.path.insert(0,str(BASE/'exam-rewrite'))
import mathml
from mathml import render,width,markdown_math
md=MarkdownIt('commonmark',{'html':True}).enable('table')
for filename,names in [('build_correct_chapter.py',('scope_preserving_display',)),('exam-calibration/build.py',('prep','text')),('build_conditional_chapter.py',('chapter_wrap','e','label','box','line','fig','item'))]:
    for f in ast.parse((BASE/filename).read_text(encoding='utf-8')).body:
        if isinstance(f,ast.FunctionDef) and f.name in names:exec(compile(ast.Module(body=[f],type_ignores=[]),filename,'exec'))
mathml.wrap_display=chapter_wrap
figures={}
b=label(350,32,'Evidence is the sum of three disjoint source pieces')
for i,(p,l,w) in enumerate([('1/2','1/10','3/60'),('1/3','1/5','4/60'),('1/6','3/5','6/60')]):
    x=20+i*230;b+=box(x,75,210,60,'prior '+p)+box(x,180,210,60,'likelihood '+l)+box(x,285,210,60,'joint '+w,'#bee4d0')+line(x+105,135,x+105,180)+line(x+105,240,x+105,285)
b+=label(350,405,'Add joint masses: evidence = 13/60')
figures['partition']=fig('bayes-partition','Disjoint source weighting',445,b,'Figure 1. Each column follows one source. Priors multiply conditional report likelihoods; the resulting disjoint joint masses add to the common denominator.')
b=label(350,32,'Original prior → retained joint mass → posterior')
for y,values,total in [(85,[.5,1/3,1/6],'1'),(205,[.05,1/15,.1],'13/60'),(325,[3/13,4/13,6/13],'1')]:
    x=70
    for v,c in zip(values,['#bee4d0','#ffda87','#dae8f2']):b+=f'<rect x="{x}" y="{y}" width="{560*v}" height="40" fill="{c}" stroke="#4f7986"/>';x+=560*v
    b+=label(350,y+78,'total '+total)
figures['normalization']=fig('bayes-normalization','Mass weighting on one common probability axis',450,b,'Figure 2. Every row uses the same unit-length axis. Weighting retains only alert mass. Dividing by thirteen sixtieths changes the retained mass to a unit posterior distribution, while preserving ratios among its source pieces.')
b=label(350,30,'Two thousand synthetic weighted cases')
for x,y,s,c in [(55,80,'target +: 18','#bee4d0'),(365,80,'background +: 99','#ffda87'),(55,185,'target −: 2','#ffda87'),(365,185,'background −: 1881','#dae8f2')]:b+=box(x,y,275,65,s,c)
b+=label(350,315,'Positive target fraction: 18/117 = 2/13')+label(350,368,'Negative target fraction: 2/1883')
figures['frequencies']=fig('bayes-frequencies','Natural-frequency positive and negative evidence cells',410,b,'Figure 3. The conditioning denominator uses a report row. The class-specific likelihood denominators instead use class columns. Those denominators answer different questions.')
b=label(350,30,'Likelihood ratio four with initial prior odds 1/9')
for i,(n,o,p) in enumerate([(0,'1/9','1/10'),(1,'4/9','4/13'),(2,'16/9','16/25'),(3,'64/9','64/73')]):
    x=30+i*170;b+=box(x,90,140,65,'n = '+str(n))+box(x,195,140,65,o,'#ffda87')+box(x,300,140,65,p,'#bee4d0')
    if i<3:b+=line(x+140,122,x+170,122)
b+=label(350,420,'Rows show report count, posterior odds, posterior probability',20)
figures['odds']=fig('bayes-odds','Independent report odds and probability',455,b,'Figure 4. Each report multiplies odds by four. Probability requires a separate conversion, dividing odds by one plus odds. The same arithmetic is not valid for copied measurements.')
b=label(350,30,'Observed report: the host opens empty door 3')
for i,s in enumerate(['prize 1','prize 2','prize 3']):b+=box(30+i*230,75,210,65,s)
for i,s in enumerate(['likelihood q','likelihood 1','likelihood 0']):b+=box(30+i*230,190,210,65,s,'#ffda87');b+=line(135+i*230,140,135+i*230,190)
b+=label(350,325,'Uniform prize priors → switch posterior 1/(1 + q)')+label(350,385,'The specific report and host policy are both part of the evidence',20)
figures['protocol']=fig('bayes-protocol','Informed host reporting likelihoods',420,b,'Figure 5. When the initial choice hides the prize, the host has a choice and uses the specified tie-breaking probability. In the other two states the report is either forced or impossible.')
b='<path d="M90,315 L620,315 M90,315 L90,55" stroke="#4f7986" stroke-width="2" fill="none"/>'
points=[(90+530*j/100,315-240*(4*(j/100)/(1+3*j/100))) for j in range(101)]
b+='<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#2b7a68" stroke-width="4"/>'
b+='<path d="M90,315 L620,75" stroke="#a2aab2" stroke-dasharray="5 5" fill="none"/>'
b+=label(350,30,'Posterior response for likelihood ratio four',23)+label(350,378,'prior probability p',23)+label(90,347,'0',18)+label(620,347,'1',18)+label(62,78,'1',18)+label(220,110,'posterior',22)+label(510,280,'unchanged prior',20)
figures['sensitivity']=fig('bayes-sensitivity','Posterior sensitivity curve on a unit probability square',410,b,'Figure 6. Both axes range from zero to one. The green curve is four p divided by one plus three p. The dashed diagonal represents uninformative evidence. The algebraic derivative, not the plotted sample alone, proves monotonicity and concavity.')
b='<path d="M90,315 L620,315 M90,315 L90,55" stroke="#4f7986" stroke-width="2" fill="none"/>'
for h,t,col in [(0,0,'#a2aab2'),(1,0,'#b78221'),(2,1,'#2b7a68')]:
    norm=1 if h==0 else .5 if h==1 else 1/12
    pts=[(90+530*j/100,315-105*((j/100)**h*(1-j/100)**t/norm)) for j in range(101)]
    b+='<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+'" fill="none" stroke="'+col+'" stroke-width="3"/>'
b+=label(350,30,'Uniform prior, one head, and two heads plus one tail')+label(90,347,'0',18)+label(620,347,'1',18)+label(62,315,'0',18)+label(62,105,'2',18)+label(350,387,'parameter θ; vertical axis is density',22)
b+=label(260,85,'one head: 2θ',21)+label(220,150,'HHT: 12θ²(1 − θ)',20)
figures['density']=fig('bayes-density','Normalized posterior densities on the unit interval',425,b,'Figure 7. The horizontal coordinate is coin rate and density uses a common scale of 105 drawing units per density unit. Gray is the uniform prior, amber the one-head posterior, and green the HHT posterior. Every curve integrates to one; density heights are not probabilities of parameter points.')
questions=json.loads((BASE/'s_bayes-questions.json').read_text());actual=json.loads((BASE/'exam-calibration/actual-items.json').read_text())
auth=[next(q for q in actual if q['id']==id) for id in ['Phd_CS_1404_Q69','MS_CE_1405_Q35']]
bank='<h3 id="authentic-questions">Authentic examination revisits</h3>'+''.join(item(q,i,True) for i,q in enumerate(auth,1))
bank+='<h3 id="original-questions">Original and course-derived problems</h3>'+''.join(item(q,i) for i,q in enumerate(questions,3))
parts=[]
for block in (BASE/'s_bayes-review.en.md').read_text().split('\n\n'):
    m=re.fullmatch(r'(\d+)\. ([\s\S]+)',block)
    parts.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>' if m else text(block))
lab='''<section class="lab" id="bayes-lab"><form id="bayes-form"><label>Prior target probability (integer fraction)<input name="prior" value="1/100" required></label><label>Observation likelihood in target class<input name="target" value="9/10" required></label><label>Observation likelihood in background class<input name="background" value="1/20" required></label><label>Number of displayed reports<input name="reports" type="number" min="0" max="20" step="1" value="1" required></label><label>Report dependence model<select name="mode"><option value="independent">Independent measurements</option><option value="duplicate">Copies of one measurement</option></select></label><button type="submit">Compute the exact posterior and evidence</button></form><div class="lab-actions"><button type="button" data-bayes-preset="default">Rare-class positive</button><button type="button" data-bayes-preset="negative">Rare-class negative</button><button type="button" data-bayes-preset="independent">Two independent positives</button><button type="button" data-bayes-preset="duplicate">One positive copied twice</button><button type="button" data-bayes-preset="impossible">Impossible report</button></div><div id="bayes-output" aria-live="polite"></div><p>Probability inputs must be integers or fractions with numerator and denominator at most 100,000, a positive denominator, and value between zero and one. Repetition count is an integer from zero to twenty. All products and normalization use exact integer fractions. With zero reports the evidence is the whole sample space; with copied reports, every positive report count uses only the first measurement.</p></section>'''
source=(BASE/'s_bayes.en.md').read_text().split('\n',1)[1].replace('<!-- INCLUDE:problems -->',bank).replace('<!-- INCLUDE:review -->',''.join(parts)).replace('<!-- LAB:bayes -->',lab)
for key,value in figures.items():source=source.replace(f'<!-- FIGURE:{key} -->',value)
body=text(source)
anchors=['sources','partitions','bayes','frequencies','odds','repeated','protocols','sensitivity','decisions','continuous','implementation','problems','review','laboratory','references']
it=iter(anchors);body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{next(it)}">{m[1]}</h2>',body)
assert '<!--' not in body and '$' not in body
assert body.count('class="exam-question"')==65 and body.count('class="review-rule"')==80
title="Bayes' Rule, Base Rates, and Evidence"
nav=' '.join('<a href="#'+a+'">'+a.replace('-',' ').capitalize()+'</a>' for a in anchors)
page=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Doctoral CSE 1406</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="exam-calibration.css"><link rel="stylesheet" href="s_bayes.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#week-2">← Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Probability and Statistics · Week 2</p><h1>{html.escape(title)}</h1><p>Review draft · five reviewed university courses · 65 worked problems · 80 examination rules · 10 exact simulations</p></header><nav class="toc" aria-label="Chapter contents">{nav}</nav><article class="lesson">{body}</article><p class="top-link"><a href="../index.html#library">← Chapter library</a></p></main><script src="s_bayes.js"></script><script src="exam-calibration.js"></script></body></html>'
(ROOT/'dist/chapters/s_bayes.html').write_text(page,encoding='utf-8')
for part,name in [('source-audit','sources'),('quality-audit','quality')]:
    audit=text((BASE/f's_bayes-{part}.md').read_text())
    (ROOT/f'dist/reviews/s_bayes-{name}.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bayes chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/s_bayes.html">← Bayes chapter</a></p><article class="lesson">'+audit+'</article></main></body></html>',encoding='utf-8')
p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text());w=next(w for w in lessons if w['week']==2)
w['chapters']=[c for c in w['chapters'] if c['topicId']!='s_bayes']+[dict(topicId='s_bayes',title=title,status='draft',statusLabel='New chapter awaiting review',revisionState='new_chapter_draft',url='chapters/s_bayes.html',questionCount=65,authenticQuestionCount=2,originalQuestionCount=63,examNotesCount=80,sourceAuditUrl='reviews/s_bayes-sources.html')]
p.write_text(json.dumps(lessons,indent=2)+'\n')
from build_concept_animations import build_data,install_animations
build_data();install_animations()
from preserve_library_approval import preserve_approval
preserve_approval()
print('Built s_bayes: 65 problems, 80 rules, seven figures, ten exact simulations and a rational laboratory.')
