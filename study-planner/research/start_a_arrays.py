from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,a):p.write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8')
g=load(B/'chapter-gate.json')
assert g['currentTopicId']=='d_pigeonhole' and g['state']=='awaiting_user_approval'
for name in ['library-approval.json','animation-approval.json']:
 p=B/name;a=load(p)
 if 'd_pigeonhole' not in a['approvedTopics']:a['approvedTopics'].append('d_pigeonhole')
 a.setdefault('approvalByTopic',{})['d_pigeonhole']={'date':'2026-10-05','sourceSHA':'bb29506e6c92cf3b52c62b504ef7ea4c5dab13cf','version':None,'approval':'User explicitly approved the delivered chapter and formula-layout correction and requested the next sole chapter. Online publication remains separately unconfirmed.'};save(p,a)
g.update(currentTopicId='a_arrays',state='in_progress',approvedTopicId='d_pigeonhole',activeWork='Write only arrays, linked lists, and operation costs; preserve 34 approved chapters.',sourceAuditPath='research/a_arrays-source-audit.md',qualityAuditPath='research/a_arrays-quality-audit.md',nextReview='Finish and audit this single chapter; deliver a draft for explicit approval.',reviewScope='Only a_arrays; 34 preceding chapters are approved.',reviewEvidence=[]);save(B/'chapter-gate.json',g)
p=R/'dist/lessons.json';a=load(p)
for w in a:
 for c in w['chapters']:
  if c['topicId']=='d_pigeonhole':c.update(status='ready',statusLabel='Student-approved chapter',revisionState='exam_grounded_approved',visualRevisionState='student_approved',animationReviewState='student_approved')
save(p,a)
p=R/'dist/chapters/d_pigeonhole.html';p.write_text(p.read_text(encoding='utf-8').replace('Review draft ·','Student-approved chapter ·'),encoding='utf-8')
with (R/'WEEKLY_DELIVERY.md').open('a',encoding='utf-8') as f:f.write('\n\n## Active chapter: arrays and linked lists, October 5, 2026\n\nThe user explicitly approved d_pigeonhole and its formula correction and authorized the next sole chapter a_arrays. Approval applies to the delivered local source; online publication is separate and currently unconfirmed. Preserve all 34 approved chapters and 1,999 questions. Write a deep English lesson, at least four genuinely reviewed university courses, a large mathematical/conceptual solved bank, concrete examination rules, and subject-specific pointer and storage animations. The a_arrays chapter stays draft until explicit approval.\n')
print('Approved d_pigeonhole and started only a_arrays.')
