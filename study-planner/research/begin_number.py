from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/build_flow_chapter.py';s=p.read_text(encoding='utf-8').replace('Review draft · five','Approved chapter · five').replace("status='draft'","status='ready'");p.write_text(s,encoding='utf-8')
p=ROOT/'research/p_flow-review.en.md';s=p.read_text(encoding='utf-8').replace("**Status:** English review draft, awaiting the student's explicit approval before promotion and before the next chapter begins.","**Status:** Approved English chapter. The student explicitly approved promotion and continuation on 2026-10-02.");p.write_text(s,encoding='utf-8')
p=ROOT/'research/p_flow-quality-audit.md';s=p.read_text(encoding='utf-8');s+='\n\nApproval update, 2026-10-02: The student approved p_flow and authorized g_number. The validation record above describes the pre-approval review; p_flow is now ready.\n';p.write_text(s,encoding='utf-8')
p=ROOT/'research/chapter-gate.json';d=json.loads(p.read_text(encoding='utf-8'));d.update(currentTopicId='g_number',state='in_progress',sourceAuditPath='research/g_number-source-audit.md',qualityAuditPath='research/g_number-quality-audit.md',lastCompletedReview='2026-10-02: Student explicitly approved p_flow; promotion to ready and g_number authorized.',nextReview='Complete and audit only g_number; then await approval.');p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
p=ROOT/'research/finalize_flow_handoff.py';s=p.read_text(encoding='utf-8').replace("assert gate['currentTopicId']=='p_flow'","assert gate['currentTopicId']=='p_flow', 'Historical helper cannot overwrite a later chapter gate.'");p.write_text(s,encoding='utf-8')
print('Promoted approved flow chapter; activated number representation chapter.')
