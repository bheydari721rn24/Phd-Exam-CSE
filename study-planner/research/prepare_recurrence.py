"""Promote the approved number-theory chapter and activate one successor."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'dist/lessons.json';rows=json.loads(p.read_text())
for week in rows:
 for c in week['chapters']:
  if c['topicId']=='d_number':c['status']='ready'
p.write_text(json.dumps(rows,indent=2)+'\n')
for rel in ['dist/chapters/d_number.html','research/build_discrete_number.py','research/d_number.en.md']:
 p=ROOT/rel;s=p.read_text(encoding='utf-8').replace('Review draft · four principal','Student-approved chapter · four principal').replace('This remains a review draft until the student explicitly approves it.','This chapter has been approved by the student.')
 if rel.endswith('.py'):s=s.replace("'status':'draft'","'status':'ready'")
 p.write_text(s,encoding='utf-8')
p=ROOT/'research/verify_d_number_en.py';p.write_text(p.read_text().replace("'Review draft' in page","'Student-approved chapter' in page"))
p=ROOT/'research/chapter-gate.json';g=json.loads(p.read_text());g.update(currentTopicId='a_recurrence',state='in_progress',approvedTopicId='d_number',proposedNextTopicId=None,sourceAuditPath='research/a_recurrence-source-audit.md',qualityAuditPath='research/a_recurrence-quality-audit.md',activeWork='Writing and auditing the single authorized algorithmic-recurrences chapter.',nextReview='Complete and deliver a_recurrence, then wait for explicit student approval.');p.write_text(json.dumps(g,indent=2)+'\n')
print('Number theory approved; only algorithmic recurrences are active.')
