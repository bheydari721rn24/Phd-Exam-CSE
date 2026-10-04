import json
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
cache=Path('C:/Users/bheydari/AppData/Local/Temp/phd-functions-sources')
docs=json.loads((cache/'acquisition.json').read_text())
specs=[
 ('cambridge','Cambridge','Programming in C, Michaelmas 2017–18; Neel Krishnaswami','All 19 slides; selected emphasis pp. 2–8,14–19','Primary: C interfaces, storage/linkage and macro contrast',[5,5,4,4]),
 ('berkeley13','UC Berkeley','CS61A, Composing Programs; John DeNero','§1.3 all; §1.6.3–1.6.4 all; §2.4.2 sequence sharing and mutation','Primary: environment identity, lexical parents and closures',[5,4,5,4]),
 ('harvard4','Harvard','CS50x 2025; David J. Malan','Lecture 1 Functions; Lecture 4 Swapping including both pointer/value examples','Primary: direct caller/callee target comparison',[5,4,4,3]),
 ('cmu','CMU','15-122 Fall 2026; Frank Pfenning, Iliano Cervesato','pp. 19–39 read; pp. 1–10 introductory example context','Primary: modular specifications and proof obligations',[5,4,5,5]),
 ('stanford','Stanford','CS106B, Winter 2016; course teaching staff','Functions and Pass by Reference, both pages','Selected supplemental comparison: true C++ references',[5,3,3,3]),
 ('mit','MIT','6.0001, Fall 2016; Ana Bell, Eric Grimson, John Guttag','Lecture 4 slides 3–35 read','Selected supplemental comparison: return, scope, decomposition',[5,4,4,3])]
records=[]
for key,uni,course,scope,role,scores in specs:
 doc=next(d for d in docs if d['id']==key)
 linked=[d for d in docs if d['id'].startswith('berkeley')] if key=='berkeley13' else [d for d in docs if d['id'].startswith('harvard')] if key=='harvard4' else [doc]
 records.append(dict(id=key+'-functions-written',subject='programming',university=uni,course=course,url=doc['url'],evidence=doc['url'],topics=['p_functions'],advantage=role+'; '+scope,limit='Bounded written chapter scope; no claim of global exhaustiveness. See source audit for language reconciliation.',access='Official publicly accessible written text',reviewed=True,reviewScope=scope,selectionRole=role,selectionScores=dict(zip(['writtenAccess','boundaryCoverage','semanticDepth','exerciseValue'],scores)),sourceDocuments=linked))
(BASE/'p_functions-reviewed-courses.json').write_text(json.dumps(records,indent=2)+'\n')
pub=ROOT/'dist/evidence/p_functions';pub.mkdir(parents=True,exist_ok=True)
(pub/'sources.json').write_text(json.dumps(dict(state='reviewed',courses=records,documents=docs,readingDate='2026-10-04',scope='Six reviewed courses, four primary universities and two supplemental comparisons; hashes identify the actually acquired documents.'),indent=2)+'\n')
print('Recorded six examined course candidates and fingerprinted written portions.')
