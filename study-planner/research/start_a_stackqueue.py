from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,a):p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
g=read(B/'chapter-gate.json')
assert g['currentTopicId']=='a_arrays' and g['state']=='awaiting_user_approval'
baseline={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'dist/chapters').glob('*.html')}
save(B/'a_stackqueue-retention-baseline.json',baseline)
for name in ['library-approval.json','animation-approval.json']:
 p=B/name;a=read(p)
 if 'a_arrays' not in a['approvedTopics']:a['approvedTopics'].append('a_arrays')
 a.setdefault('approvalByTopic',{})['a_arrays']={'date':'2026-10-05','approval':'Explicit user approval of the whole-library visual revision and authorization to write the next chapter.','onlinePublication':'Separate from approval; currently unconfirmed.'}
 a['libraryVisualQuestionRevisionApproval']={'date':'2026-10-05','chapters':35,'problems':2085,'state':'student_approved'};save(p,a)
p=B/'library-visual-question-review/manifest.json';a=read(p);a.update(state='student_approved',approval='Explicit user approval before starting a_stackqueue.');save(p,a)
p=R/'dist/lessons.json';a=read(p)
for w in a:
 for c in w['chapters']:
  c.update(visualRevisionState='student_approved',animationReviewState='student_approved')
  if c['topicId']=='a_arrays':c.update(status='ready',statusLabel='Student-approved chapter',revisionState='exam_grounded_approved')
save(p,a)
g.update(currentTopicId='a_stackqueue',state='in_progress',approvedTopicId='a_arrays',activeWork='Write only Stacks, Queues, and Applications; preserve all 35 prior chapter bodies and visual models.',reviewScope='Only a_stackqueue; the 35-chapter visual revision is explicitly approved.',nextReview='Deliver a complete chapter draft and wait for explicit approval.',sourceAuditPath='research/a_stackqueue-source-audit.md',qualityAuditPath='research/a_stackqueue-quality-audit.md',reviewEvidence=[])
save(B/'chapter-gate.json',g)
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Active chapter: Stacks, Queues, and Applications\n\n5 October 2026: The user explicitly approved the whole-library visual revision and requested the next chapter. The sole active chapter is a_stackqueue. Preserve the 35 existing chapter HTML files byte for byte, including their 2,085 complete problem bodies and reviewed animations. The next chapter remains a draft until explicit approval. Publication remains a separate verification step.\n')
print('Approved prior library; started only a_stackqueue.')
