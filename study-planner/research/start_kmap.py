import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
for name in ['library-approval.json','animation-approval.json']:
 p=BASE/name;d=json.loads(p.read_text())
 if 'p_arrays' not in d['approvedTopics']:d['approvedTopics'].append('p_arrays')
 d.setdefault('approvalByTopic',{})['p_arrays']={'version':64,'date':'2026-10-04','approval':'User explicitly approved arrays and indexing and authorized the next chapter.'}
 p.write_text(json.dumps(d,indent=2)+'\n')
p=BASE/'chapter-gate.json';d=json.loads(p.read_text());d.update(currentTopicId='g_kmap',state='in_progress',approvedTopicId='p_arrays',nextTopicId=None,proposedNextTopicId=None,activeWork='Author and verify only Minterms, Maxterms, and Logic Minimization.',reviewScope='Only g_kmap is being authored; all approved chapters are preserved.',sourceAudit='research/g_kmap-source-audit.md',qualityAudit='research/g_kmap-quality-audit.md',sourceAuditPath='research/g_kmap-source-audit.md',qualityAuditPath='research/g_kmap-quality-audit.md');p.write_text(json.dumps(d,indent=2)+'\n')
p=BASE/'verify_concept_animations.py';t=p.read_text();t=t.replace('1498','1581').replace('1,498','1,581');p.write_text(t)
print('Arrays approval recorded. Only g_kmap is in progress.')
