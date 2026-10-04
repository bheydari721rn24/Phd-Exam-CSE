import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
for name in ['library-approval.json','animation-approval.json']:
 p=BASE/name;d=json.loads(p.read_text())
 if 'l_rank' not in d['approvedTopics']:d['approvedTopics'].append('l_rank')
 d.setdefault('approvalByTopic',{})['l_rank']={'version':62,'date':'2026-10-04','approval':'User explicitly approved rank, invertibility and solution sets and authorized the next chapter.'}
 p.write_text(json.dumps(d,indent=2)+'\n')
p=BASE/'chapter-gate.json';d=json.loads(p.read_text());d.update(currentTopicId='p_functions',state='in_progress',approvedTopicId='l_rank',nextTopicId=None,proposedNextTopicId=None,activeWork='Author and verify only Functions, Variable Scope, and Parameter Passing.',reviewScope='Only p_functions is being authored; all approved chapters are preserved.',sourceAudit='research/p_functions-source-audit.md',qualityAudit='research/p_functions-quality-audit.md');p.write_text(json.dumps(d,indent=2)+'\n')
p=BASE/'verify_concept_animations.py';t=p.read_text();t=t.replace('1317','1407').replace('1,317','1,407');p.write_text(t)
print('Rank approval recorded. Only p_functions is in progress.')
