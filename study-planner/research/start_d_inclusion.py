from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent
def load(p):return json.loads(p.read_text())
def save(p,a):p.write_text(json.dumps(a,indent=2)+'\n')
g=load(B/'chapter-gate.json')
assert g['currentTopicId']=='d_counting' and g['state']=='awaiting_user_approval'
for name in ['library-approval.json','animation-approval.json']:
 p=B/name;a=load(p)
 if 'd_counting' not in a['approvedTopics']:a['approvedTopics'].append('d_counting')
 a.setdefault('approvalByTopic',{})['d_counting']={'version':68,'date':'2026-10-05','approval':'User explicitly approved the counting chapter and authorized the next sole chapter.'}
 a['approvedSiteVersion']=68;a['approvedSourceSHA']='310897fdc44f3f304bb279995f715bdfa246944a';save(p,a)
g.update(currentTopicId='d_inclusion',state='in_progress',approvedTopicId='d_counting',activeWork='Author only the next inclusion-exclusion chapter, preserving all 32 approved chapters.',sourceAuditPath='research/d_inclusion-source-audit.md',qualityAuditPath='research/d_inclusion-quality-audit.md',nextReview='Finish, independently audit and deliver this sole draft before requesting approval.',reviewScope='Only d_inclusion; all 32 previous chapters explicitly approved.',reviewEvidence=[])
save(B/'chapter-gate.json',g)
p=R/'dist/lessons.json';a=load(p)
for w in a:
 for c in w['chapters']:
  if c['topicId']=='d_counting':c.update(status='ready',statusLabel='Student-approved chapter',revisionState='exam_grounded_approved',visualRevisionState='student_approved',animationReviewState='student_approved',approvedVersion=68)
save(p,a)
p=R/'dist/chapters/d_counting.html';p.write_text(p.read_text().replace('Review draft ·','Student-approved chapter ·'))
with (R/'WEEKLY_DELIVERY.md').open('a') as f:f.write('\n\n## Active chapter: inclusion-exclusion, October 5, 2026\n\nThe user explicitly approved d_counting in Site version 68 and authorized only the next chapter d_inclusion. All 32 existing chapters remain approved. Work continuously on this chapter until its complete review draft is delivered, then wait for explicit approval. Preserve all existing questions, formulas, visuals and study progress.\n')
print('Recorded counting approval and started only d_inclusion.')
