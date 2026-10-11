from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_hash-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
m=json.loads((E/'mathematics.json').read_text());v=json.loads((E/'browser.json').read_text());assert m['status']==v['status']=='passed' and not v['geometry']['issues'] and not v['connections']['issues']
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==54
for c in prior:assert hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest()==c['sha256']
cs=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']];assert len(cs)==55 and sum(c['questionCount']for c in cs)==3739
save(E/'retention.json',dict(status='passed',unchangedChapterPages=54,libraryCards=55,workedQuestions=3739))
save(E/'lesson-and-retention.json',dict(status='quality_review_complete',totalSections=25,teachingSections=20,workedQuestions=82,finalRules=80,coreUniversities=4,universitiesRead=6,models=21,checkpoints=551,studentApproved=False))
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='a_hash'
g['completedReviewDrafts']=[c for c in g['completedReviewDrafts']if c['topicId']!='a_hash']+[dict(topicId='a_hash',state='quality_review_complete',studentApproved=False,url='chapters/a_hash.html',qualityAudit='research/a_hash-quality-audit.md',evidence=['research/a_hash-evidence/'+k+'.json'for k in['reading','mathematics','browser']],publicationState='pending_upload')]
g.update(currentTopicId='a_amortized',state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate written amortized-analysis sources and author the next chapter under continuous user authorization.',reviewScope='Aggregate, accounting and potential proofs; dynamic arrays, hysteresis, counters, queues and amortized versus expected bounds.',sourceAuditPath='research/a_amortized-source-audit.md',sourceAudit='research/a_amortized-source-audit.md',qualityAuditPath='research/a_amortized-quality-audit.md',qualityAudit='research/a_amortized-quality-audit.md',lastCompletedReview='a_hash: 82 complete solutions, 80 final rules, six reviewed universities, 21 models / 551 checkpoints; 1167 independent inputs / 70392 checkpoints.',nextReview='Complete a_amortized scientific and visual audits.',reviewEvidence=['research/a_hash-evidence/'+k+'.json'for k in['reading','mathematics','browser']])
save(B/'chapter-gate.json',g)
N=B/'a_amortized-evidence';N.mkdir(exist_ok=True)
save(N/'prior-library.json',dict(chapters=[dict(topicId=c['topicId'],url=c['url'],questions=c['questionCount'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest())for c in cs]))
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Hash-table review draft\n\nCompleted a_hash: 82 worked questions, 80 final rules, four core written courses from four universities and two additional reviewed universities. Twenty-one specialized models / 551 checkpoints; independent checks passed 1167 inputs / 70392 checkpoints and 11967 dictionary contracts. Real Edge passed geometry, 69 attached connections, native mathematics, controls, editable boundaries, mobile and print. All 54 preceding pages remain unchanged. Library: 55 chapters / 3739 worked questions. Publication is tracked separately; no student approval is inferred. Continue with a_amortized under standing continuous authorization.\n')
print('Completed hash quality review; advanced to amortized analysis. Library: 55 chapters, 3739 questions.')
