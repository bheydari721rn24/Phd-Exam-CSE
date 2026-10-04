import json
from pathlib import Path
B=Path(__file__).resolve().parent
for name in ['library-approval.json','animation-approval.json']:
 p=B/name;d=json.loads(p.read_text())
 if 'g_kmap' not in d['approvedTopics']:d['approvedTopics'].append('g_kmap')
 d.setdefault('approvalByTopic',{})['g_kmap']={'version':65,'date':'2026-10-04','approval':'User explicitly approved logic minimization and authorized the next chapter.'}
 p.write_text(json.dumps(d,indent=2)+'\n')
p=B/'chapter-gate.json';d=json.loads(p.read_text());d.update(currentTopicId='g_combin',state='in_progress',approvedTopicId='g_kmap',nextTopicId=None,proposedNextTopicId=None,activeWork='Author and verify only Combinational Circuit Design.',reviewScope='Only g_combin is being authored; all approved chapters are preserved.',sourceAudit='research/g_combin-source-audit.md',qualityAudit='research/g_combin-quality-audit.md',sourceAuditPath='research/g_combin-source-audit.md',qualityAuditPath='research/g_combin-quality-audit.md');p.write_text(json.dumps(d,indent=2)+'\n')
p=B/'verify_concept_animations.py';t=p.read_text();p.write_text(t.replace('1581','1665').replace('1,581','1,665'))
print('Logic minimization approval recorded; combinational design in progress.')
