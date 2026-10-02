from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/chapter-gate.json';d=json.loads(p.read_text(encoding='utf-8'))
assert d['currentTopicId']=='g_boolean' and d['state']=='awaiting_user_approval'
p=ROOT/'research/build_boolean_chapter.py';s=p.read_text(encoding='utf-8').replace('Review draft · four','Approved chapter · four').replace("status='draft'","status='ready'");p.write_text(s,encoding='utf-8')
p=ROOT/'research/g_boolean-review.en.md';s=p.read_text(encoding='utf-8');s+='\n\nThe student explicitly approved this chapter on 2026-10-02. It is now in the approved library.\n';p.write_text(s,encoding='utf-8')
p=ROOT/'research/g_boolean-quality-audit.md';s=p.read_text(encoding='utf-8');p.write_text(s+'\n\n2026-10-02: Student explicitly approved g_boolean and authorized g_gates. Boolean algebra is now ready.\n',encoding='utf-8')
d.update(currentTopicId='g_gates',state='in_progress',sourceAuditPath='research/g_gates-source-audit.md',qualityAuditPath='research/g_gates-quality-audit.md',lastCompletedReview='2026-10-02: Student approved g_boolean and authorized logic gates.',nextReview='Complete and audit only g_gates; then await explicit student approval. Archived Iranian exams remain deferred.')
(ROOT/'research/chapter-gate.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print('Boolean chapter approved; gate chapter in progress.')
