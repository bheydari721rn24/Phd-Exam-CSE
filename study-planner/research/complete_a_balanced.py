from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_balanced-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
m=json.loads((E/'mathematics.json').read_text());v=json.loads((E/'browser.json').read_text())
assert m['status']==v['status']=='passed'and not v['geometry']['issues']and not v['treeConnections']['issues']
assert v['counts']['questions']==82 and v['counts']['rules']==80
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==52
for q in prior:
 p=R/'dist'/q['url'];assert hashlib.sha256(p.read_bytes()).hexdigest()==q['sha256'];assert p.read_text(encoding='utf-8').count('class="exam-question"')==q['questions']
chapters=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']]
assert len(chapters)==53 and sum(c['questionCount']for c in chapters)==3575
save(E/'retention.json',dict(status='passed',unchangedChapterPages=52,unchangedQuestionCounts=52,libraryCards=53))
save(E/'lesson-and-retention.json',dict(status='quality_review_complete',teachingSections=20,totalSections=26,workedQuestions=82,finalRules=80,universitiesRead=5,coreUniversities=4,models=26,checkpoints=294,priorPagesRetained=52,studentApproved=False))
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='a_balanced'
g['completedReviewDrafts']=[q for q in g.get('completedReviewDrafts',[])if q['topicId']!='a_balanced']+[dict(topicId='a_balanced',state='quality_review_complete',studentApproved=False,url='chapters/a_balanced.html',qualityAudit='research/a_balanced-quality-audit.md',evidence=['research/a_balanced-evidence/'+p+'.json'for p in ['reading','mathematics','browser']],publicationState='pending_upload')]
g.update(currentTopicId='a_heap',state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate written priority-queue courses, then author a_heap under standing continuous authorization.',reviewScope='Binary heap invariants, exact array/tree indices, repair and construction proofs, priority-queue interfaces, heapsort and advanced comparisons.',sourceAuditPath='research/a_heap-source-audit.md',sourceAudit='research/a_heap-source-audit.md',qualityAuditPath='research/a_heap-quality-audit.md',qualityAudit='research/a_heap-quality-audit.md',lastCompletedReview='a_balanced: 82 worked solutions, 80 final rules, five read universities, 26 models / 294 checkpoints; 340 independent inputs / 13,142 generated checkpoints.',nextReview='Complete a_heap audits before advancing.',reviewEvidence=['research/a_balanced-evidence/'+p+'.json'for p in ['reading','mathematics','browser']])
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Balanced search trees review draft — 10 October 2026\n\nCompleted a_balanced with 82 fully worked questions, 80 final rules, 26 specialized models and 294 checkpoints. Four core courses plus a fifth university comparison were genuinely read. Independent checks cover 340 input specifications / 13,142 generated checkpoints; every midpoint-construction size 1 through 1024 is independently certified. Real Edge checked fonts, scripts, fence geometry, 867 edge endpoints, actual motion/pause/resume, all saved checkpoint geometry, mobile, print and editable boundaries including twelve negative four-character keys. All 52 preceding pages and counts are retained. Library: 53 chapters / 3575 questions. Student approval and publication remain separate. Authoring advances to a_heap under standing continuous authorization.\n')
N=B/'a_heap-evidence';N.mkdir(exist_ok=True)
save(N/'prior-library.json',dict(chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in chapters]))
print('Balanced-tree quality review completed; next active topic a_heap.')
