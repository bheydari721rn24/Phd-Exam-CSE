import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
for name in ['library-approval.json','animation-approval.json']:
 p=BASE/name;d=json.loads(p.read_text())
 if 'p_functions' not in d['approvedTopics']:d['approvedTopics'].append('p_functions')
 d.setdefault('approvalByTopic',{})['p_functions']={'version':63,'date':'2026-10-04','approval':'User explicitly approved functions, scope and parameter passing and authorized the next chapter.'}
 p.write_text(json.dumps(d,indent=2)+'\n')
p=BASE/'chapter-gate.json';d=json.loads(p.read_text());d.update(currentTopicId='p_arrays',state='in_progress',approvedTopicId='p_functions',nextTopicId=None,proposedNextTopicId=None,activeWork='Author and verify only Arrays and Indexing.',reviewScope='Only p_arrays is being authored; all approved chapters are preserved.',sourceAudit='research/p_arrays-source-audit.md',qualityAudit='research/p_arrays-quality-audit.md',sourceAuditPath='research/p_arrays-source-audit.md',qualityAuditPath='research/p_arrays-quality-audit.md');p.write_text(json.dumps(d,indent=2)+'\n')
p=BASE/'verify_concept_animations.py';t=p.read_text();t=t.replace('1407','1498').replace('1,407','1,498');p.write_text(t)
print('Functions approval recorded. Only p_arrays is in progress.')
