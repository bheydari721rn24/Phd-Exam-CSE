"""Derive the established native-math renderer without modifying prior chapters."""
from pathlib import Path
import re
B=Path(__file__).resolve().parent;R=B.parent
s=(B/'render_s_variance.py').read_text(encoding='utf-8')
s=s.replace('s_variance','s_distributions').replace('sv-','sd-').replace('data-sv','data-sd').replace('sv-form','sd-form').replace('sv-error','sd-error').replace('sv-output','sd-output')
s=s.replace("mathml.SYMBOLS.update(ell=", "mathml.SYMBOLS.update(Lambda='Λ',Gamma='Γ',ell=")
s=s.replace('Phd-Exsd-CSE','Phd-Exam-CSE').replace('exsd-','exam-').replace('diagr sd-','diagram-')
s=s.replace('Two previously used items are explicitly identified as revisited in the audit.','This previously delivered item is revisited with a deeper named-law interpretation; the audit records its original PDF check.')
start=s.index("lab='<section");end=s.index('\nsource=',start)
lab='''<section class="lab"><form id="sd-form"><label>Law<select name="kind"><option value="binomial">Binomial count</option><option value="geometric">Positive geometric wait</option><option value="negative-binomial">Total-trial negative-binomial wait</option><option value="hypergeometric">Hypergeometric count</option><option value="poisson">Poisson count</option></select></label><label>Fixed trials or sample n<input name="n" value="6"></label><label>Success probability p<input name="p" value="0.3333333333333333"></label><label>Required successes r<input name="r" value="2"></label><label>Population N<input name="N" value="10"></label><label>Marked objects K<input name="K" value="4"></label><label>Poisson expected count<input name="lambda" value="1"></label><label>Infinite-law display limit<input name="limit" value="8"></label><button type="submit">Calculate the law</button></form><p id="sd-error" role="alert"></p><p>Counts n are bounded by twelve, population N by thirty, success target r by six and Poisson parameter by eight. The display limit is one through twelve: geometric waits show that many positive trial positions; negative-binomial waits show failure counts zero through that limit, shifted by r; Poisson counts show zero through the limit. Irrelevant parameters do not change the selected experiment. Displayed prefixes retain their omitted probability and use a fixed vertical scale from zero through one. Invalid input preserves the preceding valid result. The calculator uses floating-point probabilities; it does not infer whether an observed experiment satisfies the selected model.</p><div id="sd-output"></div></section>'''
s=s[:start]+'lab='+repr(lab)+'\n'+s[end:]
s=s.replace("anchors=['sources'", "anchors=['sources'",1)
start=s.index(";anchors=");end=s.index(";it=iter(anchors)",start)
anchors=['sources','contracts','bernoulli','binomial','factorial-moments','modes','conditioning','thinning','heterogeneous','geometric','memorylessness','censoring','races','negative-binomial','negative-pgfs','hypergeometric','finite-moments','finite-waits','poisson','splitting','approximation','latent','numerics-and-uniform','summary','problems','review','laboratory','references']
s=s[:start]+";anchors="+repr(anchors)+s[end:]
s=s.replace("==87","==88").replace("==80","==84")
s=s.replace('Variance, Covariance, and Second-Moment Reasoning','Discrete Distributions: Counts, Waiting Times, and Exact Model Selection')
s=s.replace('four core written university courses plus two reviewed comparisons · 87 worked problems · 80 final reasoning rules · 23 subject-specific second-moment models','four core written university courses plus Stanford comparison · 88 worked problems · 84 final reasoning rules · 26 mechanism-specific models')
s=s.replace('Variance and covariance chapter','Discrete distributions chapter').replace('Variance and covariance chapter audit','Discrete distributions chapter audit')
s=s.replace('questionCount=87','questionCount=88').replace('originalQuestionCount=84','originalQuestionCount=85').replace('examNotesCount=80','examNotesCount=84').replace('animationCount=23','animationCount=26').replace('animationWalkthroughCount=23','animationWalkthroughCount=26')
s=s.replace('87 worked problems, 80 final rules, 23 subject-specific second-moment models','88 worked problems, 84 final rules, 26 mechanism-specific models')
# Correct the derivative name embedded in diagram- and exam- class names.
s=s.replace('exsd-','exam-').replace('diagrsd-','diagram-').replace('Phd-Exsd-CSE','Phd-Exam-CSE')
(B/'render_s_distributions.py').write_text(s,encoding='utf-8')
css=(R/'dist/chapters/s_variance.css').read_text(encoding='utf-8').replace('sv-','sd-').replace('#sv-','#sd-')
css=css.replace('#sd-form',' #sd-form')
css+='\n.sd-stage svg text{font-size:16px}.sd-stage svg .sd-math{font-family:"STIX Two Math",serif}.sd-stage svg .sd-prose{font-family:"Source Sans 3",sans-serif}.sd-model{max-width:100%}#sd-form{grid-template-columns:repeat(auto-fit,minmax(180px,1fr))}.sd-stage{max-width:760px;margin-inline:auto}.sd-model svg{height:auto;max-width:100%}\n'
(R/'dist/chapters/s_distributions.css').write_text(css,encoding='utf-8')
print('Prepared the isolated discrete-distribution renderer and compact styles.')
