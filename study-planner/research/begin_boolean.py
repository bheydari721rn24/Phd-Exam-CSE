from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/chapter-gate.json'; d=json.loads(p.read_text(encoding='utf-8'))
assert d['currentTopicId']=='g_number' and d['state']=='awaiting_user_approval'
p=ROOT/'research/build_number_chapter.py'; s=p.read_text(encoding='utf-8').replace('Review draft · six','Approved chapter · six').replace("status='draft'","status='ready'"); p.write_text(s,encoding='utf-8')
p=ROOT/'research/g_number-review.en.md';s=p.read_text(encoding='utf-8').replace('This is a completed **review draft**. Promotion to the approved library and work on the next chapter require the student\'s explicit approval. No pre-study test is required.','This chapter was explicitly approved by the student on 2026-10-02. It is now an approved chapter. No pre-study test is required.');p.write_text(s,encoding='utf-8')
p=ROOT/'research/g_number-quality-audit.md';s=p.read_text(encoding='utf-8');p.write_text(s+'\n\n2026-10-02: Student explicitly approved g_number and authorized g_boolean. g_number is now ready.\n',encoding='utf-8')
d.update(currentTopicId='g_boolean',state='in_progress',sourceAuditPath='research/g_boolean-source-audit.md',qualityAuditPath='research/g_boolean-quality-audit.md',lastCompletedReview='2026-10-02: Student approved g_number and authorized Boolean algebra.',nextReview='Complete and audit only g_boolean, then await explicit approval. Iranian examination archives remain deferred.')
(ROOT/'research/chapter-gate.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print('Approved number chapter; Boolean chapter in progress.')
