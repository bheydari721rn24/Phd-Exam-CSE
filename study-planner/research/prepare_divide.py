"""Record explicit approval of recurrence and activate only divide-and-conquer."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'research'
p=R/'chapter-gate.json';g=json.loads(p.read_text())
assert g['currentTopicId']=='a_recurrence' and g['state']=='awaiting_user_approval'
g.update(currentTopicId='a_divide',state='in_progress',approvedTopicId='a_recurrence',
 sourceAuditPath='research/a_divide-source-audit.md',qualityAuditPath='research/a_divide-quality-audit.md',
 activeWork='Writing and auditing the single authorized divide-and-conquer chapter.',
 nextReview='Complete and deliver a_divide, then wait for explicit student approval.',proposedNextTopicId=None)
p.write_text(json.dumps(g,indent=2)+'\n')
p=ROOT/'dist/lessons.json';rows=json.loads(p.read_text())
for w in rows:
 for c in w['chapters']:
  if c['topicId']=='a_recurrence':c['status']='ready'
p.write_text(json.dumps(rows,indent=2)+'\n')
for relative in ['dist/chapters/a_recurrence.html','research/build_recurrence_chapter.py']:
 p=ROOT/relative;t=p.read_text(encoding='utf-8').replace('Review draft · four principal university courses','Student-approved chapter · four principal university courses')
 if p.suffix=='.py':t=t.replace("'status':'draft'","'status':'ready'")
 p.write_text(t,encoding='utf-8')
p=R/'a_recurrence.en.md';t=p.read_text(encoding='utf-8').replace("This remains a review draft awaiting the student's explicit approval.","The student explicitly approved this chapter; it is now part of the finished library.")
p.write_text(t,encoding='utf-8')
p=R/'verify_a_recurrence_en.py';t=p.read_text().replace("'Review draft' in page","'Student-approved chapter' in page").replace("c['topicId']=='a_recurrence')['status']=='draft'","c['topicId']=='a_recurrence')['status']=='ready'")
p.write_text(t)
print('Recurrence approved; only a_divide is in progress.')
