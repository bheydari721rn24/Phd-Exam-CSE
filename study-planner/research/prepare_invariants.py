"""Record the student's approval and activate exactly one successor chapter."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'dist/lessons.json';rows=json.loads(p.read_text())
for week in rows:
 for chapter in week['chapters']:
  if chapter['topicId']=='d_functions':chapter['status']='ready'
p.write_text(json.dumps(rows,indent=2)+'\n')
for rel in ['dist/chapters/d_functions.html','research/build_functions_chapter.py','research/d_functions.en.md']:
 p=ROOT/rel;s=p.read_text(encoding='utf-8').replace('Review draft awaiting your approval','Student-approved chapter').replace('This is a review draft awaiting student approval.','This chapter has been approved by the student.')
 if rel.endswith('.py'):s=s.replace("'status':'draft'","'status':'ready'")
 p.write_text(s,encoding='utf-8')
p=ROOT/'research/verify_d_functions_en.py';p.write_text(p.read_text().replace("'awaiting your approval' in page","'Student-approved chapter' in page"))
p=ROOT/'research/chapter-gate.json';g=json.loads(p.read_text());g.update(currentTopicId='d_invariants',state='in_progress',approvedTopicId='d_functions',proposedNextTopicId=None,sourceAuditPath='research/d_invariants-source-audit.md',qualityAuditPath='research/d_invariants-quality-audit.md',activeWork='Writing and auditing the single authorized chapter on invariants and recursive reasoning.',nextReview='Complete and deliver d_invariants, then wait for explicit student approval.');p.write_text(json.dumps(g,indent=2)+'\n')
print('Functions approval recorded; only d_invariants is active.')
