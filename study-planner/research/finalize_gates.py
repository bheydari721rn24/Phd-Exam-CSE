"""Finalize the reviewed gate chapter and its single-chapter approval handoff."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
p = ROOT / 'research/g_gates.en.md'
s = p.read_text(encoding='utf-8')
s = s.replace('CS 61C teaching staff; source attribution names John Wawrzynek and Lisa Yan', 'CS 61C teaching staff')
s = s.replace('x="382" y="165"', 'x="300" y="184"')
p.write_text(s, encoding='utf-8')

gate_path = ROOT / 'research/chapter-gate.json'
gate = json.loads(gate_path.read_text(encoding='utf-8'))
assert gate['currentTopicId'] == 'g_gates'
gate.update(state='awaiting_user_approval', nextTopicId=None,
    lastCompletedReview='2026-10-02: Completed g_gates source, mathematical, laboratory, typography, mobile and sampled A4 print audits. Four reviewed core university courses; 36 worked problems; 60 complete examination rules.',
    nextReview='Await explicit student approval of g_gates before promoting this draft or beginning any following chapter. Archived Iranian examinations remain deferred.')
gate_path.write_text(json.dumps(gate, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

p = ROOT / 'WEEKLY_DELIVERY.md'
s = p.read_text(encoding='utf-8')
heading = '## Current chapter handoff'
assert heading in s
s = s.split(heading)[0] + heading + '''

As of 2026-10-02, the student explicitly approved `g_boolean`, now `ready`. The current chapter `g_gates` (Logic Gates and Function Implementation, Logic Circuits Chapter 3) is a completed English **review draft** at `dist/chapters/g_gates.html`, linked in the chapter library. The declared eight-university pool selected four genuinely reviewed core courses from MIT, Cambridge, Stanford and UC San Diego; Berkeley provides an additional written cross-check. Actual reading ranges, selection rationale, inaccessible candidates, document hashes and corrected source issues are recorded in `research/g_gates-source-audit.md` and `research/g_gates-source-manifest.json`.

The main lesson teaches stable semantics, complete gate constructions and their proofs, netlists, CMOS switching, noise margins, physical cost models and timed hazards. It contains 36 worked problems with transfer lessons, five connected summary paragraphs, 60 complete-sentence examination rules, an eight-step solving procedure, three original static diagrams, and a two-mode interactive laboratory. Independent checks passed 3525 mathematical assertions and 5547 laboratory assertions. Browser checks covered six truth-table states, five delay states, three invalid inputs, local code/math fonts, all problem headings, and zero page overflow at 390px. A 42-page A4 QA print was sampled visually, including the corrected CMOS label placement. Exact scope and remaining uncertainty are in `research/g_gates-quality-audit.md`.

Iranian archived examinations remain deferred to the final month. The gate is `awaiting_user_approval`: do not promote g_gates or start a following chapter until explicit student approval. There is no writing timetable or scheduled production deadline; prepare one complete chapter at a time, then await approval. The local QA PDF is an inspection artifact, not a promised standalone publication.
'''
p.write_text(s, encoding='utf-8')
