"""Revise every answer, repair the independently discovered counterexample error,
and remove unrelated generic question animations. Preserve the current lesson."""
from pathlib import Path
from html import escape
import hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
from conditional_problem_figures import get as problem_figure
from teaching_prose_spacing import fix as clean_prose
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';BASE='1e5e749'
sys.path.insert(0,str(R/'research/exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;mathml.SYMBOLS.update(Pr='Pr',epsilon='ε',downarrow='↓')
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',mathml.markdown_math(s,md))
parts=re.split(r'^### (SC\d+)\s*$',(E/'s_conditional-answer-expansions.md').read_text(encoding='utf8'),flags=re.M);answers={parts[i]:parts[i+1].strip()for i in range(1,len(parts),2)};assert len(answers)==56
qs=json.loads((R/'research/s_conditional-questions.json').read_text(encoding='utf8'));qmap={q['id']:q for q in qs};q=qmap['SC33'];q['stem']=r'On eight equal atoms, let $A=B=\{1,2,3,4\}$ and $C=\{1,5,6,7\}$. Check the full triple product and a failed pair condition.';q['solution']=answers['SC33'];q['result']=['1/8','1/2']
(R/'research/s_conditional-questions.json').write_text(json.dumps(qs,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
page=subprocess.check_output(['git','show',BASE+':dist/chapters/s_conditional.html'],cwd=R).decode('utf8').replace('\r\n','\n')
def sections(s):
 for m in re.finditer(r'<section class="exam-question"[^>]*>',s):
  depth=1
  for token in re.finditer(r'<section\b[^>]*>|</section>',s[m.end():]):
   depth+=-1 if token[0]=='</section>'else 1
   if depth==0:
    end=m.end()+token.end();yield m.start(),end,s[m.start():end];break
  else:raise ValueError('Unclosed question')
rows=list(sections(page));assert len(rows)==60
authids=['Phd_CS_1404_Q68','Phd_CS_1404_Q69','Phd_CS_1404_Q70','MS_CE_1405_Q35'];actual=json.loads((R/'research/exam-calibration/actual-items.json').read_text(encoding='utf8'));amap={q['id']:q for q in actual if q['id']in authids}
audit=[];edits=[]
for n,(a,z,old)in enumerate(rows,1):
 id=re.search(r'data-source-id="([^"]+)"',old)[1]
 if id in qmap:
  q=qmap[id];solution=answers[id]
  if id!='SC33':solution+='\n\n**Result, interpretation and additional check.** '+q['solution']
  prefix=old[:old.index('<details')];prefix=re.sub(r'<p>([\s\S]*)</p>\s*$',lambda m:render(q['stem']),prefix,count=1)if False else prefix
  tag=re.match(r'<section[^>]*>',old)[0];prefix=tag+'<h3>Question '+str(n)+'. '+escape(q['title'])+'</h3><p class="exam-label">Original/course-derived mathematical problem · individually revised answer</p><p class="exam-provenance">'+escape(q['origin'])+'</p>'+render(q['stem'])
 else:
  q=amap[id];prefix=old[:old.index('<details')];solution=q['solution']
  if id=='Phd_CS_1404_Q68':solution+='\n\n'+r'The zero-event and exactly-one cases are disjoint and exhaustive for this target. The exactly-one patterns each require all other events to fail. The formula therefore uses mutual independence of the complete family, including complements, rather than pairwise information. At $n=2$ direct enumeration gives three of four equally likely event patterns. The stated $n\ge2$ domain also avoids ambiguous endpoint powers in the factored display.'
  if id=='Phd_CS_1404_Q69':solution+='\n\nThe information is the event of no boys, including a family with zero children. Its positive-count joint mass is one sixth and its total mass is two thirds. Reversing the requested direction would instead divide the joint by the positive-count marginal one half and give one third, explaining the tempting first option. The joint event is the same; the denominator changes.'
  if id=='Phd_CS_1404_Q70':solution+='\n\nFor the complemented-indicator construction, let $H_A$ count the first player\'s heads and let $T_B=20-H_B$ count the second player\'s tails. Equality $H_A=H_B$ is exactly $H_A+T_B=20$. Each of the combined45indicators is fair and mutually independent. Choosing which20are one gives the coefficient in option1. This independently proves the finite-sum identity rather than merely quoting its name.'
  if id=='MS_CE_1405_Q35':solution+='\n\nThe latent second toss can be defined even for a coin that is never physically retossed; revealing it only after a first head leaves the observed experiment unchanged. The four independent contribution indicators thus each have success probability one quarter. A failure includes both a first-tail case and a first-head/second-tail case, totaling three quarters. These are the precise events behind the two factors in the binomial count.'
 visual=problem_figure(id)
 if id=='SC16':visual+='<p>This urn walkthrough uses the same initial four red and three blue objects and the exact RBR path.</p><div class="concept-animation" data-scenes="conditional-urn"></div>'
 if id=='SC49':visual='<p>The bridge walkthrough below uses this exact five-edge network. Its finite edge states explain the general conditioned formula; the written polynomial remains the proof for arbitrary success rates.</p><div class="concept-animation" data-scenes="conditional-bridge"></div>'
 if id=='SC54':visual='<p>The strip walkthrough specializes the parameters to y = 1/2 and several positive strip widths. Its target is X at most 1/4. The symbolic derivation above applies to all parameters in the stated domain.</p><div class="concept-animation" data-scenes="conditional-strip"></div>'
 edits.append((a,z,prefix+'<details class="exam-solution"><summary>Read the complete construction, calculation and checks</summary>'+render(solution)+visual+'</details></section>'))
 audit.append({'id':id,'solutionWords':len(solution.split()),'solutionSha256':hashlib.sha256(solution.encode()).hexdigest(),'newDerivation':id in answers,'authentic':id in amap})
for a,z,value in reversed(edits):page=page[:a]+value+page[z:]
new=r'The full-family equation alone does not establish mutual independence. On eight equally weighted outcomes, take $A=B=\{1,2,3,4\}$ and $C=\{1,5,6,7\}$. All three marginals are $1/2$, and the triple intersection is the singleton $\{1\}$ with mass $1/8=(1/2)^3$. But $P(A\cap B)=1/2\ne1/4$. Thus the triple equation holds while a required pair equation fails. Checking both properties of a counterexample is essential.'
page,n=re.subn(r'<p>To see the reverse logical failure,[\s\S]*?</p>',lambda m:render(new),page,count=1);assert n==1
source=R/'research/s_conditional.en.md';s=source.read_text(encoding='utf8');s,n=re.subn(r'To see the reverse logical failure,[\s\S]*?(?=\n\n### Independent coordinate blocks)',lambda m:new,s,count=1);assert n==1 or new in s;source.write_text(s,encoding='utf8')
# Re-render original formula labels as one mathematical row, retaining matrices.
def formula(m):
 raw=m[0];label=re.search(r'aria-label="([^"]*)"',raw)
 if not label:return raw
 from html import unescape
 return mathml.render(unescape(label[1]),'display="block"'in raw)
page=re.sub(r'<math\b[\s\S]*?</math>',formula,page)
page=re.sub(r'(?<!<span class="pr-inline">)<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',page)
page=page.replace('</head>','<link rel="stylesheet" href="l_projection.css"><style>.pr-inline{vertical-align:middle}.conditional-answer-notice{padding:1rem 1.5rem;border:1px solid #c6dcd8;background:#f1f7f4;border-radius:10px;margin:1.2rem 0}</style></head>',1)
page=page.replace('<article','<aside class="conditional-answer-notice"><strong>Individual revision · 15October2026.</strong> All60answers reviewed;56 original/course problem answers now include additional explicit constructions. The triple-only independence example has been repaired. Unrelated question animations have been replaced by mathematically matched figures and mechanisms. This edition remains a review draft.</aside><article',1)
page=page.replace('Mass-proportional regions, bars, distributions or reliability edges expose the conditioning model.','Read the specified probability mass, information event and observation protocol before interpreting a probability diagram.')
page=page.replace('Record indices, logical boundaries, time coordinates and electrical polarity have distinct meanings.','Schematic cards use exact printed weights; equal card sizes do not assert equal probabilities. Reliability edges represent primitive components, and continuous diagrams use the stated density and dimension.')
page=clean_prose(page);(R/'dist/chapters/s_conditional.html').write_text(page,encoding='utf8')
record={'state':'answer_revision_in_progress_visual_review_pending','questions':audit,'baseline':BASE,'criticalCorrection':'SC33 and the lesson used C={1,5} with marginal1/4, for which the advertised triple factorization was false:1/8 !=1/16. Replaced C by{1,5,6,7}, making all marginals1/2 and the triple exactly1/8 while AB remains1/2.','removedWrongQuestionVisuals':True,'studentApproved':False};(E/'s_conditional-answer-revision.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8');print({'answers':len(audit),'newOriginalDerivations':56,'totalSolutionWords':sum(r['solutionWords']for r in audit)})
