from pathlib import Path
import json,re
B=Path(__file__).resolve().parent
questions=[]
for block in (B/'a_select-problems.en.txt').read_text(encoding='utf-8').split('@@ ')[1:]:
 head,body=block.split('\n',1);parts=head.split('|');number,title,origin=parts[:3];stem,solution=body.split('---SOLUTION---\n')
 q=dict(id='a_select_Q'+number,title=title,origin=origin,stem=stem.strip(),solution=solution.strip(),difficulty='Medium–Hard')
 if len(parts)>3:q['modelId']=parts[3]
 questions.append(q)
assert len(questions)==86
links={13:'problem-frequency-lower',14:'problem-range-upper',31:'problem-tournament-bye',33:'problem-replacement',39:'problem-quadratic',60:'problem-two-empty',64:'problem-top-k',71:'problem-weight-gap',75:'problem-heavy-weight',49:'problem-deterministic',46:'groups-example',54:'problem-two-groups'}
for n,id in links.items():questions[n-1]['modelId']=id
(B/'a_select-questions.json').write_text(json.dumps(questions,indent=2)+'\n',encoding='utf-8')
sort=json.loads((B/'a_sort-authentic.json').read_text(encoding='utf-8'))
password=next(q for q in json.loads((B/'d_pigeonhole-authentic.json').read_text(encoding='utf-8')) if q['id']=='MS_CS_1405_Q116')
sample=next(q for q in sort if q['id']=='MS_CE_1405_Q59')
sample['title']='Authentic revisit: sample pivot guarantee for sorting'
sample['solution']+='\n\n**Selection contrast.** This original question asks about quicksort, so both strict children are sorted. A single-rank selector would follow only one child and would need a separate recurrence. A sample median is not the global median and is not the median-of-medians construction.'
split=next(q for q in json.loads((B/'exam-calibration/actual-items.json').read_text(encoding='utf-8')) if q['id']=='Phd_CE_1405_Q9')
split.update(title='Authentic revisit: descending recursive median sort',booklet='Phd_CE_1405',pdfPage=3,questionNumber=9,stem=r'For distinct keys, SplitSort chooses the median $m$, recursively applies itself to $R=\{x:x>m\}$ and $L=\{x:x<m\}$, and returns `SplitSort(R), m, SplitSort(L)` concatenated in that order. What is the final output order?',options=['Descending up to the median, then ascending','Approximately random','Ascending','Descending'],answer=4,solution='Use strong induction on the number of keys. Empty and singleton arrays are already in descending order. Assume both smaller recursive outputs are descending. Every key in $R$ is greater than $m$, and every key in $L$ is smaller than $m$. Therefore concatenating the descending $R$ output, then $m$, then the descending $L$ output creates a fully descending array. The answer is printed option 4. The selected median affects balance, while the concatenation direction determines the output order. This algorithm sorts both children; it is not quickselect, which follows only the rank-containing child. Options 1 and 2 contradict the inductive block order, while option 3 would require reversing the concatenation direction.',sourceCommit='bdadf6e2c9cadc4772ae137a96a3da753c7cfd08',repoPath='Exams/Phd/CE/1405/Q707A-phd1405-[www.konkur.in].pdf',sourceSha256='34d7e4f8f1d347be2ede1be4ff027efc2e17680c3aedf633a13857f27955b75a')
for q in [password,split,sample]:q['translationStatus']='Original full PDF page rendered and rechecked on 2026-10-06; printed options preserved';q['answerProvenance']='Independently derived; not an official key'
(B/'a_select-authentic.json').write_text(json.dumps([password,split,sample],indent=2)+'\n',encoding='utf-8')
print('Prepared 86 original/reconstructed and 3 authentic questions.')
