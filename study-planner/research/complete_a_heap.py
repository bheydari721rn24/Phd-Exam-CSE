from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_heap-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
m=json.loads((E/'mathematics.json').read_text());v=json.loads((E/'browser.json').read_text())
assert m['status']==v['status']=='passed' and not v['geometry']['issues'] and not v['treeConnections']['issues']
assert v['counts']['questions']==82 and v['counts']['rules']==80
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==53
for q in prior:
 p=R/'dist'/q['url'];assert hashlib.sha256(p.read_bytes()).hexdigest()==q['sha256'];assert p.read_text(encoding='utf-8').count('class="exam-question"')==q['questions']
chapters=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']]
assert len(chapters)==54 and sum(c['questionCount']for c in chapters)==3657
save(E/'retention.json',dict(status='passed',unchangedChapterPages=53,unchangedQuestionCounts=53,libraryCards=54))
save(E/'lesson-and-retention.json',dict(status='quality_review_complete',teachingSections=20,totalSections=25,workedQuestions=82,finalRules=80,universitiesRead=5,coreUniversities=4,models=21,checkpoints=359,priorPagesRetained=53,studentApproved=False))
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='a_heap'
g['completedReviewDrafts']=[q for q in g.get('completedReviewDrafts',[])if q['topicId']!='a_heap']+[dict(topicId='a_heap',state='quality_review_complete',studentApproved=False,url='chapters/a_heap.html',qualityAudit='research/a_heap-quality-audit.md',evidence=['research/a_heap-evidence/'+p+'.json'for p in ['reading','mathematics','browser']],publicationState='pending_upload')]
g.update(currentTopicId='a_hash',state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate accessible written hashing courses and author the next chapter under standing continuous authorization.',reviewScope='Hash functions, collision resolution, exact probe traces, load factors, expected analysis, deletion invariants and resizing.',sourceAuditPath='research/a_hash-source-audit.md',sourceAudit='research/a_hash-source-audit.md',qualityAuditPath='research/a_hash-quality-audit.md',qualityAudit='research/a_hash-quality-audit.md',lastCompletedReview='a_heap: 82 worked solutions, 80 final rules, five read universities, 21 models / 359 checkpoints; 2120 independent inputs / 24992 checked checkpoints.',nextReview='Complete a_hash audits before advancing.',reviewEvidence=['research/a_heap-evidence/'+p+'.json'for p in ['reading','mathematics','browser']])
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Heap and priority-queue review draft\n\nCompleted a_heap: 82 fully worked questions, 80 final rules, five genuinely read universities, 21 specialized models / 359 checkpoints. Independent verification passed 2120 inputs / 24992 checkpoints; real Edge passed all checkpoint geometry, 1864 arrow endpoints, movement/pause/resume, editable boundaries, MathML, fonts, mobile and print. All 53 preceding pages remain unchanged. Library: 54 chapters / 3657 worked questions. Publication is tracked separately; no student approval is inferred. Authoring proceeds to a_hash under standing continuous authorization.\n')
N=B/'a_hash-evidence';N.mkdir(exist_ok=True)
save(N/'prior-library.json',dict(chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in chapters]))
pending=B/'a_balanced-publication-pending.json'
if pending.exists():
 x=json.loads(pending.read_text());x['reason']='Reconciliation succeeded and the newest saved version was still BST version 87. The legitimate balanced retry failed before archive upload at the backend files request; no saved version or deployment was returned.';save(pending,x);g['pendingPriorPublication']=x;save(B/'chapter-gate.json',g)
print('Heap review completed; next active topic a_hash.')
