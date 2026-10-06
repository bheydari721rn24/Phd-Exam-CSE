from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,a):p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
g=read(B/'chapter-gate.json')
assert g['currentTopicId']=='a_stackqueue' and g['state']=='awaiting_user_approval'
save(B/'a_sort-retention-baseline.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'dist/chapters').glob('*.html')})
for name in ['library-approval.json','animation-approval.json']:
 p=B/name;a=read(p)
 if 'a_stackqueue' not in a['approvedTopics']:a['approvedTopics'].append('a_stackqueue')
 a.setdefault('approvalByTopic',{})['a_stackqueue']={'date':'2026-10-06','approval':'Explicit user approval and authorization to write the next chapter.','onlinePublication':'Separate from student approval.'};save(p,a)
p=R/'dist/lessons.json';a=read(p)
for w in a:
 for c in w['chapters']:
  if c['topicId']=='a_stackqueue':c.update(status='ready',statusLabel='Student-approved chapter',revisionState='exam_grounded_approved',visualRevisionState='student_approved',animationReviewState='student_approved')
save(p,a)
g.update(currentTopicId='a_sort',state='in_progress',approvedTopicId='a_stackqueue',activeWork='Write only Comparison and Non-comparison Sorting; preserve all 36 previous chapter HTML files byte for byte.',reviewScope='Only a_sort.',nextReview='Deliver the complete review draft and await explicit user approval.',sourceAuditPath='research/a_sort-source-audit.md',qualityAuditPath='research/a_sort-quality-audit.md',reviewEvidence=[])
save(B/'chapter-gate.json',g)
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Active chapter: Comparison and Non-comparison Sorting\n\n6 October 2026: The user explicitly approved a_stackqueue and requested the next chapter. Only a_sort is active. Preserve the 36 previous chapter HTML files and their 2,169 question bodies. Source comparison, complete solutions, algorithm-specific models, formula layout, and mathematical/browser verification are required before delivery. The new chapter remains a draft until explicit approval.\n')
print('Started only a_sort; 36 approved HTML files retained.')
