"""Reconstruct all answers while preserving the current full teaching chapter."""
from pathlib import Path
from html import escape,unescape
import hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
from bayes_problem_figures import get as problem_figure
from teaching_prose_spacing import fix
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';BASE='9b7d401'
sys.path.insert(0,str(R/'research/exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;mathml.SYMBOLS.update(epsilon='ε',partial='∂',Longleftrightarrow='⇔',Longrightarrow='⇒')
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',mathml.markdown_math(s,md))
parts=re.split(r'^### (SB\d+)\s*$',(E/'s_bayes-answer-expansions.md').read_text(encoding='utf8'),flags=re.M);answers={parts[i]:parts[i+1].strip()for i in range(1,len(parts),2)};assert len(answers)==63
qs=json.loads((R/'research/s_bayes-questions.json').read_text(encoding='utf8'));qmap={q['id']:q for q in qs}
qmap['SB33']['stem']=r'A population has exact family-size proportions $(1/2,1/3,1/6)$ at sizes one, two, and three; its family count is a positive multiple of six. Select a child uniformly from all children in this population. Find the selected child\'s family-size distribution.'
qmap['SB36']['stem']=r'Two coins have the same heavy weight and eight coins have the same distinct light weight. An unordered pair is selected uniformly without replacement. Given that its two coins have equal weights, what is the probability both are heavy?'
(R/'research/s_bayes-questions.json').write_text(json.dumps(qs,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
page=subprocess.check_output(['git','show',BASE+':dist/chapters/s_bayes.html'],cwd=R).decode('utf8').replace('\r\n','\n')
def sections(s):
 for m in re.finditer(r'<section class="exam-question"[^>]*>',s):
  depth=1
  for t in re.finditer(r'<section\b[^>]*>|</section>',s[m.end():]):
   depth+=-1 if t[0]=='</section>'else 1
   if depth==0:
    z=m.end()+t.end();yield m.start(),z,s[m.start():z];break
  else:raise ValueError('Unclosed question')
rows=list(sections(page));assert len(rows)==65
actual=json.loads((R/'research/exam-calibration/actual-items.json').read_text(encoding='utf8'));amap={q['id']:q for q in actual}
audit=[];edits=[]
for n,(a,z,old)in enumerate(rows,1):
 id=re.search(r'data-source-id="([^"]+)"',old)[1]
 if id in qmap:
  q=qmap[id];solution=answers[id]+'\n\n**Result and interpretation.** '+q['solution'];tag=re.match(r'<section[^>]*>',old)[0]
  prefix=tag+'<h3>Question '+str(n)+'. '+escape(q['title'])+'</h3><p class="exam-label">Original/course-derived mathematical problem · individually reconstructed solution</p><p class="exam-provenance">'+escape(q['origin'])+'</p>'+render(q['stem'])
 else:
  q=amap[id];prefix=old[:old.index('<details')];solution=q['solution']
  if id=='Phd_CS_1404_Q69':solution+='\n\n'+r'**An independent posterior calculation.** The normalized posterior is $P(N=n\mid G)=(3/4)4^{-n}$ for every $n\ge0$. Its zero-size mass is $3/4$, so its positive-size tail is $1-3/4=1/4$. This separates the empty-family boundary from the positive-size geometric tail. The reverse conditional uses the same joint mass $1/6$ but divides by $P(N\ge1)=1/2$, giving $1/3$. That explains option1without changing the question\'s conditioning direction.'
  else:solution+='\n\n'+r'**Why the per-coin indicators are independent.** Pre-generate two independent fair tosses for every coin and reveal its second toss only after a first head. The second-round contribution of coin i is the indicator of its own HH pair. Different coins depend on disjoint independent pairs, so their indicators are mutually independent. The three equally likely pair outcomes other than HH contribute zero, explaining the factor $3/4$. Conditioning on the first-round eligibility count provides a separate derivation and is expanded into a posterior question in SB10.'
 visual=problem_figure(id)
 if id=='SB01':visual+='<p>The walkthrough uses these exact three priors and likelihoods. Its final normalized state is the requested posterior.</p><div class="concept-animation" data-scenes="bayes-normalize"></div>'
 if id=='SB11':visual+='<p>The following positive/negative walkthrough uses these exact detector rates and both conditioning denominators.</p><div class="concept-animation" data-scenes="bayes-frequencies"></div>'
 if id=='SB21':visual+='<p>Compare the n =2states. These walkthroughs use the stated prior1/10and likelihoods4/5and1/5, distinguishing independent observations from copies.</p><div class="concept-animation" data-scenes="bayes-repeat,bayes-copy"></div>'
 if id=='SB23':visual+='<p>Advance to the n =3state to obtain this question\'s posterior and prediction. Earlier states explain how the same fixed coin is updated.</p><div class="concept-animation" data-scenes="bayes-predict"></div>'
 edits.append((a,z,prefix+'<details class="exam-solution"><summary>Read the complete construction, calculation and checks</summary>'+render(solution)+visual+'</details></section>'))
 audit.append(dict(id=id,solutionWords=len(solution.split()),solutionSha256=hashlib.sha256(solution.encode()).hexdigest(),newDerivation=id in answers,authentic=id in['Phd_CS_1404_Q69','MS_CE_1405_Q35'],problemFigure=bool(problem_figure(id))))
for a,z,s in reversed(edits):page=page[:a]+s+page[z:]
def formula(m):
 raw=m[0];label=re.search(r'aria-label="([^"]*)"',raw)
 return mathml.render(unescape(label[1]),'display="block"'in raw)if label else raw
page=re.sub(r'<math\b[\s\S]*?</math>',formula,page)
page=re.sub(r'(?<!<span class="pr-inline">)<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',page)
# Remove the old automatic numeric-text wrapper, which split the MIT course identifier.
page=re.sub(r'<span class="math-inline">([^<>]*)</span>',r'\1',page)
page=page.replace('</head>','<link rel="stylesheet" href="l_projection.css"><style>.bayes-revision-notice{padding:1rem 1.5rem;border:1px solid #c6dcd8;background:#f1f7f4;border-radius:10px;margin:1.2rem 0}.pr-static svg{font-family:"Source Sans 3",sans-serif}</style></head>',1)
page=page.replace('<article','<aside class="bayes-revision-notice"><strong>Individual revision · 17 October2026.</strong> All65worked answers individually reviewed;63original/course answers now include explicit new constructions. Population sampling and equal-weight assumptions are specified. Question figures use their actual inputs. This revised edition is a review draft; earlier approval of a previous edition remains historical.</aside><article',1)
page=page.replace('Student-approved chapter ·','Revised edition · review draft ·',1)
old='Selecting a child uniformly across a population weights family sizes by the number of children. Selecting a family uniformly first does not create this size bias.'
new='For fixed population family proportions, selecting a child uniformly weights family sizes by their number of children. The size-biased limiting distribution requires a finite positive mean. A ratio of expected counts need not equal the expected ratio in a small random finite population. Selecting a family uniformly first defines a different protocol.'
page=page.replace('<p>'+old+'</p>',render(new))
old_population='If the family-size prior is'
population_start=page.index(old_population)
population_end=page.index('</p>',population_start)
page=page[:population_start]+render(r'If the family proportions are fixed as $\pi_n$, uniform child selection gives weights proportional to $n\pi_n$, provided the total child count is positive. For a limiting population law, the normalization requires a finite positive mean. In a small random finite population, the expected ratio of random counts need not equal the ratio of their expectations. Specify the population model before applying this transformation.').removeprefix('<p>').removesuffix('</p>\n')+page[population_end:]
p=R/'research/s_bayes-review.en.md';s=p.read_text(encoding='utf8').replace(old,new);p.write_text(s,encoding='utf8')
page=page.replace('Mass-proportional regions, bars, distributions or reliability edges expose the conditioning model.','Inspect the hidden states, actual report mechanism and printed probability masses before interpreting each display.')
page=page.replace('Record indices, logical boundaries, time coordinates and electrical polarity have distinct meanings.','Equal-sized cards are schematic; their printed numbers specify exact probabilities. Density curves represent mass per parameter unit, while posterior-risk panels represent costs.')
page=fix(page);(R/'dist/chapters/s_bayes.html').write_text(page,encoding='utf8')
record=dict(state='answer_revision_in_progress_visual_review_pending',baseline=BASE,questions=audit,questionFigures=sum(q['problemFigure']for q in audit),allOriginalAnswersExpanded=63,totalSolutionWords=sum(q['solutionWords']for q in audit),studentApproved=False,modelClarifications=['SB33 exact finite population proportions; no ratio-of-expectations substitution for a random finite population','SB36 two distinct common coin weights','SB29 stopping/count posterior coincidence and different evidence rates','SB54 observationally identical structural models with different interventions','SB55 numerical rounding distinguished from mathematical certainty'])
(E/'s_bayes-answer-revision.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8');print({k:v for k,v in record.items()if k not in['questions','modelClarifications']})
