from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/chapter-gate.json';gate=json.loads(p.read_text(encoding='utf-8'))
assert gate['currentTopicId']=='g_boolean','Historical helper cannot overwrite a later chapter gate.'
gate.update(state='awaiting_user_approval',lastCompletedReview='2026-10-02: Student approved g_number, now ready. g_boolean completed as an English review draft: four reviewed core courses plus two university cross-checks, 40 worked problems, 60 rules, two diagrams, exact truth-table/cofactor lab, 1079812 independent mathematical assertions, 32793 lab assertions, mobile font/index QA and sampled 41-page print reviewed.',nextReview='Await explicit g_boolean approval before promotion or beginning g_gates. Iranian archived examinations remain deferred.')
p.write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
p=ROOT/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8').split('## Current chapter handoff')[0]
s+='''## Current chapter handoff

As of 2026-10-02, the student explicitly approved `g_number`, now `ready`. The current chapter `g_boolean` (Boolean Algebra and Truth Tables, Logic Circuits Chapter 2) is a completed English **review draft** at `dist/chapters/g_boolean.html`, linked in the chapter library. The bounded eight-university pool selected four genuinely reviewed core courses from MIT, Cambridge, Stanford and Carnegie Mellon; Berkeley and Cornell written teaching bodies are two further cross-checks. Exact reading ranges, request hashes, failed access and independently corrected source issues are documented in `research/g_boolean-source-audit.md` and `research/g_boolean-source-manifest.json`. The lesson contains deep main teaching and proofs, 40 worked problems with transfer lessons, five connected summary paragraphs, 60 full-sentence examination rules, an eight-step solving method, two original diagrams and a truth-table/cofactor laboratory. Independent checks passed 1079812 mathematical assertions and 32793 laboratory assertions; browser checks covered seven valid states, four invalid cases, local code/math fonts, semantic indices and limits, and zero page overflow at390px. A41-page A4 print was sampled visually. Scope limits and remaining uncertainty are stated in `research/g_boolean-quality-audit.md`. Archived Iranian examination papers remain deferred. The gate is `awaiting_user_approval`: do not promote g_boolean or start g_gates until explicit student approval.
'''
p.write_text(s,encoding='utf-8')
print('Recorded g_boolean review draft; next chapter requires explicit approval.')
