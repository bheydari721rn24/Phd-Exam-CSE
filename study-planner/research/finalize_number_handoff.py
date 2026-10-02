from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/chapter-gate.json';gate=json.loads(p.read_text(encoding='utf-8'))
assert gate['currentTopicId']=='g_number','Historical helper cannot overwrite a later chapter gate.'
gate.update(state='awaiting_user_approval',lastCompletedReview='2026-10-02: Student approved p_flow, now ready. g_number completed as English review draft: six genuinely reviewed written university sources, 36 solved problems, 60 rules, two diagrams, fixed-width laboratory, 823880 independent mathematical assertions, 174756 laboratory states, mobile fonts/indices and 46-page print reviewed.',nextReview='Await explicit approval of g_number before promotion or starting any next chapter. Archived Iranian examination papers remain deferred.')
p.write_text(json.dumps(gate,indent=2)+'\n',encoding='utf-8')
p=ROOT/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8').split('## Current chapter handoff')[0]
s+='''## Current chapter handoff

As of 2026-10-02, the student explicitly approved `p_flow`, now `ready`. The current chapter `g_number` (Number Bases and Binary Encoding, Logic Circuits Chapter 1) is a completed English **review draft** at `dist/chapters/g_number.html`, linked from the library. Source and quality audits are `research/g_number-source-audit.md` and `research/g_number-quality-audit.md`. A bounded eight-offering survey selected four complementary core courses from MIT, UC Berkeley, Stanford and Cornell; CMU arithmetic and Princeton Gray-code reading are two further university supplements. Actual sections read, access failures, byte hashes and corrections are documented. The chapter includes 36 fully worked problems, 60 complete-sentence examination rules, five explanatory summary paragraphs, an eight-step solving method, two original diagrams, locally bundled prose/heading/math/code fonts, semantic indices and stacked fractions/sigma limits, and a fixed-width arithmetic/Gray laboratory. Independent verification passed 823880 mathematical assertions and 174756 laboratory cases, nine interactive browser states plus four invalid-input checks, a zero-overflow 390-pixel mobile view, and sampled visual review of a 46-page A4 print. These bounded checks are not universal correctness or exam-performance guarantees. Archived Iranian papers remain deferred. The gate is `awaiting_user_approval`: do not promote g_number or begin any following chapter before explicit student approval.
'''
p.write_text(s,encoding='utf-8')
p=ROOT/'research/mirror_flow.py';s=p.read_text(encoding='utf-8').replace('Add deep English control-flow chapter and approve scalar types','Add deep English number representation chapter and approve control flow');p.write_text(s,encoding='utf-8')
print('Recorded the completed g_number draft and one-chapter approval gate.')
