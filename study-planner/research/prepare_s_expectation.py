from pathlib import Path
import json,re,subprocess,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_expectation-evidence'
qs=[];rules=[]
for block in (B/'s_expectation-problems.en.txt').read_text(encoding='utf-8').split('@@ ')[1:]:
 header,body=block.split('\n',1);parts=header.split('|');stem,sol=body.split('---SOLUTION---',1);q=dict(id='s-expectation-original-'+parts[0],title=parts[1],origin=parts[2],stem=stem.strip(),solution=sol.strip())
 if len(parts)>3:q['modelId']=parts[3]
 if parts[0]=='9':q['additionalModelIds']=['central-four']
 if parts[0]=='38':q['additionalModelIds']=['tail-second']
 if parts[0]=='36':q['modelId']='graph-five'
 if parts[0]=='35':q['modelId']='window-eight'
 qs.append(q)
 note=sol.split('**Transfer rule.**')[1].strip();calibration=sol.strip().split('\n\n')[0]
 # The review is a complete condition-bearing retrieval note with a worked calibration,
 # not a fragment or a second copy of the entire solved exercise.
 pieces=re.split(r'(?<=[.!?])\s+(?=[A-Z])',calibration);worked=' '.join(pieces[:2])
 rules.append(str(len(qs))+'. **'+q['title']+'.** '+note+' **Worked check.** '+worked)
assert len(qs)==80
(B/'s_expectation-questions.json').write_text(json.dumps(qs,indent=2)+'\n')
(B/'s_expectation-review.en.md').write_text('\n\n'.join(rules)+'\n',encoding='utf-8')
original=json.loads((B/'exam-calibration/actual-items.json').read_text());a=next(x for x in original if x['id']=='Phd_CS_1404_Q72').copy();a.update(modelId='record-five',pdfSha256=a['sourceSha256'],answerStatus='independently_derived_not_official',verification='Original PDF page 16 visually inspected in this chapter turn; printed option order preserved. Five-value trace is a labelled realization, not the complete symbolic proof.');a['solution']+='\n\n**Visualization scope.** The attached five-element array is one numerical realization. The indicator proof above applies to every stated n.'
m=next(x for x in original if x['id']=='MS_CS_1405_Q121').copy();m.update(pdfSha256=m['sourceSha256'],answerStatus='independently_derived_not_official',verification='Original PDF page 26 visually inspected in this chapter turn; printed option order preserved.')
m['solution']+='\n\n**Expectation route.** Introduce an independently defined count $B\\sim Bin(7,1/2)$. This is a solving device, not an extra premise in the printed question. The number of successful unordered triples is $\\binom B3$. Summing its 35 triple indicators gives $E[\\binom B3]=35/8$. On the other hand, its PMF gives $E[\\binom B3]=2^{-7}\\sum_{i=3}^7\\binom i3\\binom7i$. Therefore the printed sum is $2^7(35/8)=560$, and $A=56$. This provides a factorial-moment proof of the same answer.'
(B/'s_expectation-authentic.json').write_text(json.dumps([a,m],indent=2)+'\n')
data=json.loads(subprocess.check_output(['node','-e','process.stdout.write(JSON.stringify(require(process.argv[1]).fixtures()))',str(R/'dist/chapters/s_expectation.js')],text=True,encoding='utf-8'))
(R/'dist/chapters/s_expectation-models.json').write_text(json.dumps(data,indent=2)+'\n')
css=(R/'dist/chapters/s_discrete.css').read_text(encoding='utf-8').replace('disc-','exp-').replace('#disc','#exp')
(R/'dist/chapters/s_expectation.css').write_text(css,encoding='utf-8')
old=(B/'render_s_discrete.py').read_text(encoding='utf-8').replace('s_discrete','s_expectation').replace('disc-','exp-').replace('data-disc','data-exp').replace('Discrete Random Variables and Common Distributions','Expectation, Linearity, Indicators, and Moments').replace('Discrete random variables chapter','Expectation chapter').replace('Discrete random variables','Expectation')
old=old.replace('==83','==82').replace('questionCount=83','questionCount=82').replace('authenticQuestionCount=3','authenticQuestionCount=2').replace('83 questions','82 questions').replace('83 worked problems','82 worked problems').replace('four core university courses and one bounded additional review','four core university courses and one additional lecture check').replace('Medium–Hard','Foundational checks and Medium–Hard synthesis')
old=old.replace('Authentic examination questions: count models and conditioning','Authentic examination: indicator expectation and algorithm cost')
start=old.index('lab=');end=old.index('\nsource=',start)
lab='<section class="lab"><form id="exp-form"><label>Mode<select name="kind"><option value="mean">Signed weighted mean</option><option value="square">Squared value mean</option><option value="absolute">Absolute value mean</option><option value="loss">Expected squared loss</option><option value="tails">Integer tail-sum mean</option><option value="cap">Capped executed trials</option><option value="bins">Uniform-bin occupancy</option></select></label><label>Original values<input name="values" value="-2,1,4"></label><label>Probability masses<input name="masses" value="0.2,0.5,0.3"></label><label>Cap / number of balls<input name="cap" value="3"></label><label>Success probability / number of bins<input name="prob" value="0.25"></label><button type="submit">Compute and inspect every step</button></form><p id="exp-error" role="alert"></p><p>Finite-law modes use 1–5 values between −100 and 100, and equally long nonnegative masses summing to one. Duplicate values remain valid original contributions. Tail mode requires integer values from 0 to 8. Capped trials use an integer cap from 1 to 10 and success probability from 0 to 1, including a finite cap with zero success probability. Occupancy uses 0–8 balls and 1–3 uniform bins. Cap and occupancy modes ignore the value law after list syntax validation. Invalid input preserves the preceding result. Floating-point displays are rounded; rational and enumeration audits are separate evidence. Every animation starts paused.</p><div id="exp-output"></div></section>'
old=old[:start]+'lab='+repr(lab)+old[end:]
old=old.replace('<!-- LAB: discrete -->','<!-- LAB: expectation -->')
start=old.index('anchors=');end=old.index(';it=iter(anchors)',start)
anchors=['sources','mean','existence','outcomes','lotus','linearity','products','indicators','permutations','records','occupancy','sampling','patterns','tails','waiting','classical','moments','loss','bounds','partition','random-sums','infinite-sums','computation','workflow','summary','problems','review','laboratory','references']
old=old[:start]+'anchors='+repr(anchors)+old[end:]
(B/'render_s_expectation.py').write_text(old,encoding='utf-8')
decisions=[]
for q in qs:
 decisions.append(dict(questionId=q['id'],models=([q['modelId']]if q.get('modelId')else[])+q.get('additionalModelIds',[]),decision='Exact numeric process/plot clarifies the stated data.'if q.get('modelId')else'The complete symbolic or finite-table reasoning is the primary representation; no unrelated animation is attached.'))
(E/'question-visual-decisions.json').write_text(json.dumps(decisions,indent=2)+'\n')
print('Prepared 80 independently written solutions, 80 complete review notes, authentic Q72,',len(data['models']),'concept models and',sum(len(m['frames'])for m in data['models']),'checkpoints.')
