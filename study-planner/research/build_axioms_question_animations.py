from pathlib import Path
from fractions import Fraction as F
import copy,itertools,json,sys
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
def formula(q):
 q=F(q);return str(q.numerator) if q.denominator==1 else ('-' if q<0 else '')+rf'\frac{{{abs(q.numerator)}}}{{{q.denominator}}}'
def native(q):return mathml.render(formula(q))
def frame(state,claim,caption,initial):
 return dict(nodes=[],edges=[],snapshot=copy.deepcopy(state),caption=caption,captionHtml='<p>'+caption+'</p>',metrics={},formula=claim,formulaHtml='<div class="formula-block">'+mathml.render(claim,True)+'</div>',line=0,teaching=dict(operation='Inspect the exact outcome partition and probability law',why=caption,currentState=copy.deepcopy(state),initial=initial,activeLine=0,checks=[],changes=[],reading='Outcome cards are not area-scaled. Fractions give exact masses. Bar heights use the declared exact counting scale.'))
def scene(id,title,description,frames):return dict(id=id,title=title,description=description,descriptionHtml='<p>'+description+'</p>',invariant='Displayed masses and counts belong to the declared experiment. Negative candidate masses are explicitly marked impossible, never presented as probabilities.',visual=dict(type='enumeration',claim='A question-specific exact atomic law, conditional pair space or count partition.'),code=['Build the exact partition; check all masses; select and normalize the target'],frames=frames)
scenes={}
for num,ts in [(39,[F(0),F(1,40),F(1,20),F(3,40),F(1,10),F(1,8)]),(47,[F(0),F(1,10),F(3,20),F(1,5),F(1,4),F(3,10),F(2,5)])]:
 frames=[]
 for t in ts:
  masses=([t,F(3,10)-t,F(1,5)-t,F(1,10)-t]+[F(1,10)+t]*3+[F(1,10)-t] if num==39 else [t]+[F(3,10)-t]*3+[t-F(1,10)]*3+[F(2,5)-t])
  valid=all(q>=0 for q in masses);state=dict(question=num,t=str(t),masses=[str(q) for q in masses],massMath=[native(q) for q in masses],valid=valid,total=str(sum(masses)))
  caption=f'Candidate triple mass t={t}. All eight exact membership masses sum to one. '+('Every mass is nonnegative, so these atoms construct a valid law with the stated marginals and pair intersections.' if valid else 'At least one mass is negative, so this candidate cannot define a probability law; the red cells identify the contradiction.')
  frames.append(frame(state,rf't={formula(t)},\quad\sum_{{s}}p_s=1',caption,not frames))
 id=f'axioms-question-atoms{num}';scenes[id]=scene(id,f'Question {num}: exact eight-cell feasibility','Three membership bits specify whether A, B and C occur. Changing only the triple parameter recovers every cell. The final valid endpoints and explicit invalid candidates expose the sharp interval.',frames)
balls=['R1','R2','R3','B1','B2'];pairs=list(itertools.combinations(balls,2));frames=[]
for stage in range(4):
 kept=[not all(x.startswith('B') for x in pair) for pair in pairs];target=[all(x.startswith('R') for x in pair) for pair in pairs]
 weights=[F(1,10) if stage==0 else (F(1,10) if stage==1 else F(1,9)) if k else F(0) for k in kept]
 state=dict(stage=stage,pairs=[list(x) for x in pairs],kept=kept,target=target,weights=[str(q) for q in weights],massMath=[native(q) for q in weights])
 caption=['Ten unordered labeled pairs each have original mass 1/10. Three are red-red, six mixed and one blue-blue.','The observation excludes only the blue-blue pair. Its original mass is 1/10, so the conditioning event has mass 9/10. The surviving original masses shown here are not yet renormalized.','Divide every surviving original mass 1/10 by the same positive denominator 9/10. All nine conditional masses now sum to one.','The target consists of the three red-red pairs, each with conditional mass 1/9. Add their disjoint masses to obtain 1/3.'][stage]
 frames.append(frame(state,r'P(RR\mid\text{at least one red})=\frac{3/10}{9/10}=\frac13',caption,stage==0))
scenes['axioms-question-urn']=scene('axioms-question-urn','Question 41: all ten labeled pairs and conditioning','No random sampling is approximated here: every unordered two-ball subset is enumerated exactly. Gray excludes a pair, blue retains a mixed pair and green marks the red-red target.',frames)
frames=[];sequences=[''.join(x) for x in itertools.product('HT',repeat=3)];counts=[1,3,3,1]
for k in range(4):
 state=dict(active=k,counts=counts,sequences=[[s for s in sequences if s.count('H')==j] for j in range(4)],masses=[native(F(q,8)) for q in counts])
 frames.append(frame(state,rf'P(K={k})={formula(F(counts[k],8))}',f'The active head count is {k}; its detailed preimages are '+', '.join(state['sequences'][k])+f'. There are {counts[k]} such sequences, each of mass 1/8. The four group sizes remain 1,3,3,1; the reported values are not uniform.',k==0))
scenes['axioms-question-report']=scene('axioms-question-report','Question 43: the induced head-count distribution','Four bars show exact preimage counts on a fixed common scale. Highlighting each group identifies its ordered sequences; adding the final two groups gives the target probability.',frames)
frames=[]
for stage in range(3):
 state=dict(stage=stage,counts=[24,36,4],total=64,repeat=40,boundCount=48,overcount=8)
 caption=['The 64 ordered outcomes partition into 24 all-distinct, 36 exactly-one-pair and four all-equal outcomes.','Repetition includes the second and third categories once: 36+4=40, hence probability 40/64=5/8.','Summing three pair-equality counts includes 36 single-pair outcomes once and four all-equal outcomes three times: 36+12=48. The union bound is 48/64=3/4; its excess is 8/64.'][stage]
 frames.append(frame(state,[r'24+36+4=64',r'P(\text{repeat})=\frac{40}{64}=\frac58',r'P(\text{repeat})\le\frac{48}{64}=\frac34'][stage],caption,stage==0))
scenes['axioms-question-collision']=scene('axioms-question-collision','Question 45: exact collision categories and overcount','Bar heights show actual ordered-outcome counts, not the number of category names. The pair-equality bound counts each all-equal outcome three times; the union counts it once.',frames)
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text());d['scenes'].update(scenes);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:len(v['frames']) for k,v in scenes.items()}))
