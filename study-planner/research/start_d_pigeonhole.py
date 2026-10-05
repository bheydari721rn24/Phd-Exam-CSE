from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
def load(p):return json.loads(p.read_text())
def save(p,a):p.write_text(json.dumps(a,indent=2)+'\n')
g=load(B/'chapter-gate.json')
assert g['currentTopicId']=='d_inclusion' and g['state']=='awaiting_user_approval'
for name in ['library-approval.json','animation-approval.json']:
 p=B/name;a=load(p)
 if 'd_inclusion' not in a['approvedTopics']:a['approvedTopics'].append('d_inclusion')
 a.setdefault('approvalByTopic',{})['d_inclusion']={'version':69,'date':'2026-10-05','approval':'User explicitly approved the inclusion-exclusion chapter and authorized the next sole chapter.'}
 a['approvedSiteVersion']=69;a['approvedSourceSHA']='c958f2b5b8eae701ab686ba77051991cc1b24278';save(p,a)
g.update(currentTopicId='d_pigeonhole',state='in_progress',approvedTopicId='d_inclusion',activeWork='Author only the next pigeonhole chapter, preserving all 33 approved chapters.',sourceAuditPath='research/d_pigeonhole-source-audit.md',qualityAuditPath='research/d_pigeonhole-quality-audit.md',nextReview='Finish, independently audit and deliver this sole draft before requesting approval.',reviewScope='Only d_pigeonhole; all 33 previous chapters explicitly approved.',reviewEvidence=[])
save(B/'chapter-gate.json',g)
p=R/'dist/lessons.json';a=load(p)
for w in a:
 for c in w['chapters']:
  if c['topicId']=='d_inclusion':c.update(status='ready',statusLabel='Student-approved chapter',revisionState='exam_grounded_approved',visualRevisionState='student_approved',animationReviewState='student_approved',approvedVersion=69)
save(p,a)
p=R/'dist/chapters/d_inclusion.html';p.write_text(p.read_text().replace('Review draft ·','Student-approved chapter ·'))
with (R/'WEEKLY_DELIVERY.md').open('a') as f:f.write('\n\n## Active chapter: pigeonhole principle, October 5, 2026\n\nThe user explicitly approved d_inclusion in Site version 69 and authorized only the next chapter d_pigeonhole. All 33 existing chapters remain approved. Work continuously on this chapter until its complete review draft is delivered, then wait for explicit approval. Preserve all existing questions, formulas, visuals and study progress.\n')
print('Recorded inclusion-exclusion approval and started only d_pigeonhole.')
