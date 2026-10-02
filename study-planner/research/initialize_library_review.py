from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/build_gates_chapter.py';s=p.read_text(encoding='utf-8').replace('Review draft · four core','Student-approved chapter · four core').replace("status='draft'","status='ready'");p.write_text(s,encoding='utf-8')
p=ROOT/'research/g_gates-review.en.md';s=p.read_text(encoding='utf-8');s=s.replace('This chapter remains a review draft until explicit student approval.','The student approved this chapter on 2026-10-02.');p.write_text(s,encoding='utf-8')
p=ROOT/'research/g_gates-quality-audit.md';s=p.read_text(encoding='utf-8');s+='\n2026-10-02: Student explicitly approved g_gates and requested a comprehensive revision of all existing chapters. No new chapter is authorized during this revision.\n';p.write_text(s,encoding='utf-8')
p=ROOT/'research/chapter-gate.json';g=json.loads(p.read_text(encoding='utf-8'));assert g['currentTopicId']=='g_gates';g.update(state='library_review_in_progress',approvedTopicId='g_gates',activeWork='Review all 16 existing chapters; no new chapter.',revisionTracker='research/library-review.json',lastCompletedReview='2026-10-02: Student approved g_gates and authorized comprehensive library revision.',nextReview='Complete the existing-library revision. Do not begin a new chapter during this task.');p.write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
p=ROOT/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8');s=s.split('## Current chapter handoff')[0]+'''## Current chapter handoff

2026-10-02: The student explicitly approved g_gates and requested a prolonged, detailed final revision of all 16 existing chapters. The active task is the existing-library revision, recorded in research/library-review.json. Review teaching prose, assumptions, derivations, every worked solution and end rule; inspect mathematical notation, all figures and interactive models. Correct identified errors and keep the actual semantic-reading coverage separate from automated checks. Previously approved chapters remain available. No new chapter begins during this revision. Archived Iranian examinations remain deferred.

The library revision is not complete while any chapter has pending semantic review, source issues or unresolved visual findings. Do not claim token-by-token review or universal perfection from automated inventory, finite tests or sampled screenshots.
''';p.write_text(s,encoding='utf-8')
