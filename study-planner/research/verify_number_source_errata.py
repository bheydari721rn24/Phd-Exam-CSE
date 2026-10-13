from pathlib import Path
import json, itertools, math, ast, re, hashlib, xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';checks=[]
def check(label,p):assert p,label;checks.append(label)
matches=[(a,b,40-a-b)for a in range(41)for b in range(41-a)if a%2==0 and b<=4 and 40-a-b>=1]
check('independent direct enumeration: total40 gives96',len(matches)==96)
check('actual complete row counts',[sum(b==i for a,b,c in matches)for i in range(5)]==[20,20,19,19,18])
check('ratio six belongs only to fourth interval',len(matches)/16==6)
# Construct the entire Laurent polynomial using exact exponent convolution.
coeff={0:1}
for _ in range(15):
 nxt={}
 for e,c in coeff.items():
  for delta in [2,-1]:nxt[e+delta]=nxt.get(e+delta,0)+c
 coeff=nxt
check('independent Laurent coefficient x14 of fifteenth power',coeff.get(14,0)==0)
check('independent example x12 coefficient',coeff[12]==5005)
canon={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
for id in ['MS_CS_1405_Q125','MS_CS_1405_Q129']:
 q=canon[id];p=Path('C:/Users/bheydari/Desktop/Phd-Exam-CSE')/q['repoPath'];check('original PDF unchanged '+id,hashlib.sha256(p.read_bytes()).hexdigest()==q['sourceSha256'])
for n in ['s_counting','d_counting','d_number']:
 page=(R/f'dist/chapters/{n}.html').read_text()
 for m in re.findall(r'<math\b[\s\S]*?</math>',page):ET.fromstring(m)
 check(n+' native mathematics is well-formed',True)
check('canonical total and answer corrected','a+b+c=40' in canon['MS_CS_1405_Q129']['stem'] and canon['MS_CS_1405_Q129']['answer']==4)
check('canonical exponent corrected','^{15}' in canon['MS_CS_1405_Q125']['stem'])
for p in [B/'exam-calibration/author_actual.py',B/'write_counting_answers.py',B/'write_discrete_number_answers.py',B/'build_counting_question_models.py']:ast.parse(p.read_text());check('producer syntax '+p.name,True)
frames=json.loads((R/'dist/chapters/concept-animations.json').read_text())['scenes']['counting-question-parity']['frames']
for i,f in enumerate(frames):
 s=f['snapshot'];check('model exact row '+str(i),s['counts']==[20,20,19,19,18] and s['upper']==[19,19,18,18,17] and s['prefix']==sum(s['counts'][:i+1]) and s['aValues']==list(range(0,2*s['upper'][i]+1,2)))
report=dict(status='passed_independent_arithmetic_and_corrected_producers',checks=len(checks),labels=checks,sourceFaithfulness='Root visually reread the original full pages and enlarged Q125/Q129 crops. Previous transcription and its old finite checks are superseded.',exactResult=96,coefficient=0)
(E/'number-source-errata-math.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(report)
