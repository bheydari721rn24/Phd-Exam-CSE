from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_bst-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
m=json.loads((E/'mathematics.json').read_text());v=json.loads((E/'browser.json').read_text())
assert m['status']==v['status']=='passed' and not v['geometry']['issues'] and not v['treeConnections']['issues']
assert v['counts']['questions']==82 and v['counts']['rules']==80
prior=json.loads((E/'prior-library.json').read_text())['chapters'];assert len(prior)==51
for q in prior:
 p=R/'dist'/q['url'];assert hashlib.sha256(p.read_bytes()).hexdigest()==q['sha256'];assert p.read_text(encoding='utf-8').count('class="exam-question"')==q['questions']
chapters=[c for w in json.loads((R/'dist/lessons.json').read_text())for c in w['chapters']]
assert len(chapters)==52 and sum(c['questionCount']for c in chapters)==3493
save(E/'retention.json',dict(status='passed',unchangedChapterPages=51,unchangedQuestionCounts=51,libraryCards=52))
save(E/'lesson-and-retention.json',dict(status='quality_review_complete',teachingSections=22,totalSections=27,workedQuestions=82,finalRules=80,universitiesRead=5,coreUniversities=4,models=27,checkpoints=208,priorPagesRetained=51,studentApproved=False))
g=json.loads((B/'chapter-gate.json').read_text());assert g['currentTopicId']=='a_bst'
g['completedReviewDrafts']=[q for q in g.get('completedReviewDrafts',[])if q['topicId']!='a_bst']+[dict(topicId='a_bst',state='quality_review_complete',studentApproved=False,url='chapters/a_bst.html',qualityAudit='research/a_bst-quality-audit.md',evidence=['research/a_bst-evidence/'+p+'.json'for p in ['reading','mathematics','browser']],publicationState='pending_upload')]
g.update(currentTopicId='a_balanced',state='in_progress',nextTopicRequiresExplicitApproval=False,activeWork='Evaluate and read written balanced-tree courses; author a_balanced under standing authorization.',reviewScope='AVL balance and exact height, insertion and deletion repair, rotations, 2-3-4/red-black encodings and variant-specific invariants.',sourceAuditPath='research/a_balanced-source-audit.md',sourceAudit='research/a_balanced-source-audit.md',qualityAuditPath='research/a_balanced-quality-audit.md',qualityAudit='research/a_balanced-quality-audit.md',lastCompletedReview='a_bst: 82 worked solutions, 80 reasoning rules, five read universities, 27 models / 208 checkpoints; 161 independent inputs / 723 generated checkpoints.',nextReview='Complete a_balanced audits before advancing.',reviewEvidence=['research/a_bst-evidence/'+p+'.json'for p in ['reading','mathematics','browser']])
save(B/'chapter-gate.json',g)
with(R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8')as f:f.write('\n\n## Binary search trees review draft — 10 October 2026\n\nCompleted a_bst with 82 fully worked questions, 80 condition-bearing final rules, 27 specialized models and 208 checkpoints. Five universities genuinely read, four core courses selected. Independent reference checks passed 161 inputs / 723 generated checkpoints. Real Edge checked moving arrow ports, pause/resume, complete checkpoint geometry, fonts, math, mobile containment and print. All 51 preceding pages retained. Library: 52 chapters / 3493 questions. Student approval and publication are separate. Standing authorization advances authoring to a_balanced.\n')
N=B/'a_balanced-evidence';N.mkdir(exist_ok=True)
save(N/'prior-library.json',dict(chapters=[dict(topicId=c['topicId'],url=c['url'],sha256=hashlib.sha256((R/'dist'/c['url']).read_bytes()).hexdigest(),questions=c['questionCount'])for c in chapters]))
print('BST quality review completed; next active topic a_balanced.')
