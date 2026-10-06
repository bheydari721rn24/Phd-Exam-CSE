from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];B=R/'research'
questions=[]
for block in (B/'s_descriptive-problems.en.txt').read_text(encoding='utf-8').split('@@ ')[1:]:
 header,body=block.split('\n',1);parts=header.split('|');stem,solution=body.split('---SOLUTION---',1)
 q=dict(id='s-descriptive-original-'+parts[0],title=parts[1],origin=parts[2],stem=stem.strip(),solution=solution.strip())
 if len(parts)>3 and parts[0]!='35':q['modelId']=parts[3]
 questions.append(q)
assert len(questions)==80
(B/'s_descriptive-questions.json').write_text(json.dumps(questions,indent=2)+'\n',encoding='utf-8')
manifest=json.loads((B/'exam-calibration/archive-manifest.json').read_text())
auth=[dict(id='s-descriptive-phd-cs-1405-q58',title='Discrete variance and the squared-value term',booklet='PhD CS 1405',questionNumber=58,pdfPage=15,repoPath='Exams/Phd/CS/1405/Q693A-phd1405-[www.konkur.in].pdf',stem=r'Let $X$ take values $x_1,\ldots,x_k$ with $P(X=x_i)=P_i$, and let $\mu=E[X]$. Which expression is its variance? This authentic population-moment question is a bridge from mass-weighted descriptive variance, not a Bessel-corrected sample-variance question.',options=[r'$\sum_{i=1}^k x_iP_i-\mu^2$',r'$\sum_{i=1}^k x_iP_i^2-\mu$',r'$\sum_{i=1}^k x_i^2P_i-\mu^2$',r'$\sum_{i=1}^k x_iP_i-\mu$'],answer=3,solution=r'''The probability weights satisfy $P_i\ge0$ and $\sum_iP_i=1$. First calculate $\mu=\sum_i x_iP_i$. Then expand the squared deviation:

$$Var(X)=\sum_iP_i(x_i-\mu)^2=\sum_iP_ix_i^2-2\mu\sum_iP_ix_i+\mu^2\sum_iP_i=\sum_iP_ix_i^2-\mu^2.$$

Therefore option 3 is correct. The first and fourth alternatives replace the second moment by a first moment; the fourth is identically zero because its first term is the mean. The second squares the probabilities instead of the observed values and also subtracts a first-power mean. The units must be squared measurement units. There is no $n-1$ correction here: the supplied probabilities define the complete law, and the expression is a population variance. For the special case $P_i=f_i/n$, the same identity describes the empirical distribution's variance.'''),
dict(id='s-descriptive-ms-ce-1405-q36',title='Normal search-cost standardization',booklet='MS CE 1405',questionNumber=36,pdfPage=8,repoPath='Exams/MS/CE/1405/Q135A-Arshad1405-[www.konkur.in].pdf',stem=r'An algorithm searches among $n$ entries. Its average number of steps is $\log_2 n$. For $n=1024$, suppose the number of steps follows the stated normal model with variance 4. What is the probability that the number of steps is at most 12? Here $\Phi$ is the standard normal CDF.',options=[r'$\Phi(1)$',r'$\Phi(-1)$',r'$2\Phi(1)-1$',r'$1-2\Phi(-1)$'],answer=1,solution=r'''First distinguish variance from SD. The mean is $\log_2(1024)=10$, the variance is 4, and the SD is $\sqrt4=2$. Under the explicitly supplied normal model, standardize the threshold:

$$P(X\le12)=P\left(\frac{X-10}{2}\le\frac{12-10}{2}\right)=\Phi(1).$$

Thus option 1 is correct. Option 2 reverses the threshold sign. Options 3 and 4 are equal by $\Phi(-1)=1-\Phi(1)$, but both describe a two-sided one-SD interval, not the requested one-sided event. Dividing by variance 4 rather than SD 2 gives the wrong standardized threshold. The result uses the question's normal assumption; a mean and variance alone would not determine this probability. Step counts are discrete in reality, while this question supplies a continuous normal model. No unstated continuity correction is inserted into that model.''')]
for q in auth:
 q['sourceCommit']=manifest['commit'];q['pdfSha256']=next(f['sha256'] for f in manifest['files'] if f['repoPath']==q['repoPath']);q['answerStatus']='independently_derived_not_official';q['verification']='Original PDF page visually checked; printed option order preserved.'
(B/'s_descriptive-authentic.json').write_text(json.dumps(auth,indent=2)+'\n',encoding='utf-8')
css=(R/'dist/chapters/a_select.css').read_text().replace('select-','stat-').replace('#select','#stat')
css+='\n.stat-math{font-family:"STIX Two Math",serif!important;font-size:17px}.stat-model svg .stat-label{font-size:17px}.stat-model svg{isolation:isolate}.stat-stage polygon{pointer-events:none}\n'
(R/'dist/chapters/s_descriptive.css').write_text(css,encoding='utf-8')
s=(B/'render_a_select.py').read_text(encoding='utf-8').replace('a_select','s_descriptive').replace('select-','stat-').replace('#select','#stat').replace('data-select','data-stat')
s=s.replace("mathml.SYMBOLS.update(Pr=", "mathml.SYMBOLS.update(Phi='Φ',inf='inf')\nmathml.SYMBOLS.update(Pr=")
s=s.replace('def text(s):return', "def text(s):\n s=s.replace(r'\\bigl','').replace(r'\\bigr','')\n return")
s=s.replace(" s=s.replace(r'\\bigl','').replace(r'\\bigr','')", " s=s.replace(r'\\bigl','').replace(r'\\bigr','')\n s=re.sub(r'\\$\\$([\\s\\S]*?)\\$\\$|\\$([^$\\n]+)\\$',lambda m:m[0].replace('Var(',r'\\operatorname{Var}(').replace('Cov(',r'\\operatorname{Cov}(').replace('med(',r'\\operatorname{med}(').replace('med_i',r'\\operatorname{med}_i').replace('sign(',r'\\operatorname{sign}('),s)")
s=s.replace(" return oldbase(self).replace", " value=oldbase(self)\n value=re.sub(r'<mi>(Var|Cov|med|sign)</mi>',r'<mi mathvariant=\"normal\">\\1</mi>',value)\n return value.replace")
s=s.replace(" self.skip();marker=", " self.skip()\n if self.s.startswith(r'\\widetilde',self.i):\n  self.i+=len(r'\\widetilde');return '<mover>'+self.group()+'<mo>~</mo></mover>'\n marker=")
s=s.replace('Authentic searching bridge and sorting/selection revisits','Authentic population-moment and normal-standardization bridges')
start=s.index("lab='''");stop=s.index("source=",start)
s=s[:start]+'''lab=\"\"\"<section class="lab"><form id="stat-form"><label>Exact model<select name="kind"><option value="histogram">Density histogram</option><option value="ecdf">Empirical CDF</option><option value="mean">Squared loss and mean</option><option value="median">Absolute loss and median</option><option value="quantiles">Quantile conventions</option><option value="variance">Residuals and variance</option><option value="affine">Affine transformation</option><option value="box">Type-7 boxplot</option><option value="pooling">Pool two groups</option><option value="stream">Welford stream</option><option value="correlation">Paired correlation</option><option value="qq">Two-sample Q–Q</option><option value="ma">Trailing moving average</option><option value="ewma">EWMA, initial value zero</option></select></label><label>Values / first group<input name="values" value="0,1,1,2,3,4" aria-describedby="stat-limits"></label><label>Scale / window / lambda<input name="parameter" value="3" aria-describedby="stat-limits"></label><label>Bin edges / second group / translation<input name="other" value="0,1,2,4" aria-describedby="stat-limits"></label><button type="submit">Compute the exact teaching trace</button></form><p id="stat-error" role="alert"></p><p id="stat-limits">Enter 1–12 finite values per list between −999 and 999. Histogram mode needs strictly increasing edges covering every observation. Pooling and Q–Q accept unequal group sizes; correlation needs equal lengths and labels constant-column correlation undefined. Affine mode uses the numeric scale (−20 to 20) and exactly one translation in the second field. Moving average uses integer window 1–12 and shorter windows at startup. EWMA uses lambda greater than zero and at most one, with initial value zero. Other modes ignore unused fields. Boxplots use type 7 and strict 1.5-IQR fences. Invalid submissions preserve the previous model. The displayed arithmetic uses finite precision; exact rational examples are checked separately.</p><div id="stat-output"></div></section>\"\"\"
''' +s[stop:]
s=s.replace('<!-- LAB:selection -->','<!-- LAB:statistics -->')
start=s.index("anchors=[");stop=s.index(';it=iter(anchors)',start)
anchors=['sources','units','histograms','ecdf','mean','quantiles','variance','bessel','affine','robust','shape','bounds','grouped','pooling','stream','association','qq-time','summary','problems','review','laboratory','references']
s=s[:start]+'anchors='+repr(anchors)+s[stop:]
s=s.replace('==89','==82').replace('89 worked','82 worked').replace('89 questions','82 questions').replace('89,authenticQuestionCount=3,originalQuestionCount=86','82,authenticQuestionCount=2,originalQuestionCount=80')
s=s.replace('Searching, Selection, and Order Statistics','Descriptive Statistics and Exploratory Data Analysis').replace('Data Structures and Algorithms','Probability and Statistics').replace('Selection chapter audit','Descriptive statistics chapter audit').replace('Searching and selection chapter','Descriptive statistics chapter')
s=s.replace("k.replace('-',' ').capitalize()", "({'ecdf':'ECDF','qq-time':'Q–Q and time','bessel':'Bessel correction','association':'Paired association'}.get(k,k.replace('-',' ').capitalize()))")
(B/'render_s_descriptive.py').write_text(s,encoding='utf-8')
print('Prepared 80 original solved questions, two checked authentic questions, styles and active-chapter renderer.')
