"""Save the completed single-chapter handoff without shell string interpolation."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'WEEKLY_DELIVERY.md'
text=path.read_text(encoding='utf-8').split('## Current chapter handoff')[0]
text+='''## Current chapter handoff

As of 2026-10-02, the student explicitly approved `l_matrices`, now `ready`. The next chapter, `p_types` (Data Types, Conversions, and Operators, Programming Fundamentals Chapter 1), is a completed English **review draft** in `dist/chapters/p_types.html`, linked from the chapter library. Its source and quality audits are `research/p_types-source-audit.md` and `research/p_types-quality-audit.md`. Four core written courses from four universities were selected after a bounded seven-offering survey; a fifth university course adds a Python comparison. The chapter has 36 fully explained problems, 50 complete-sentence examination rules, a seven-step expression method, two original diagrams, semantic fractions/indices, separate locally bundled code/math fonts and a five-mode laboratory. Mobile and 39-page print QA passed, along with 453,032 exact/model assertions and eleven browser laboratory states. C examples were not compiled; specification checks and independent models are distinguished from compiler execution. The gate is `awaiting_user_approval`; do not promote this chapter to `ready` or start `p_flow` until explicit student approval. Archived Iranian entrance-exam papers remain deferred.
'''
assert not any(ord(c)<32 and c not in '\n\t' for c in text)
path.write_text(text,encoding='utf-8')
print('Saved completed p_types handoff; l_matrices approved; next chapter requires approval.')
