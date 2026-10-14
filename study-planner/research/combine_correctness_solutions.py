from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision'
old=(E/'a_correct-solutions.md').read_text(encoding='utf8');parts=re.split(r'^### Solution (\d+)\s*$',old,flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
for name in['1-4','17-28','29-41','42-54']:
 parts=re.split(r'^### Solution (\d+)\s*$',(E/f'a_correct-solutions-{name}.md').read_text(encoding='utf8'),flags=re.M)
 answers.update({int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)})
assert set(answers)==set(range(1,55))
text='# Correctness solution rewrite — complete answer manuscript\n\nAll 54 answer drafts are present. This is an answer manuscript, not a completed chapter audit: deeper instruction, final rules, subject-specific models and rendered checks still need integration and verification.\n\n'+'\n\n'.join(f'### Solution {n}\n\n'+answers[n]for n in range(1,55))+'\n'
(E/'a_correct-solutions.md').write_text(text,encoding='utf8')
original=json.loads((E/'a_correct-original-recheck.json').read_text())
for item in original:item.update(visualReconciled=True,reviewedAt='2026-10-14',reviewScope='Question and all four original alternatives inspected on the rendered source page; independent English derivation; not an official key.')
(E/'a_correct-original-recheck.json').write_text(json.dumps(original,indent=2)+'\n')
print({'answers':len(answers),'words':sum(len(s.split())for s in answers.values()),'minimumWords':min(len(s.split())for s in answers.values()),'sha256':hashlib.sha256(text.encode()).hexdigest()})
