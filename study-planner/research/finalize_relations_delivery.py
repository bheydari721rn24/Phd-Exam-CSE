"""Save audit evidence and the explicit one-chapter review handoff."""
import hashlib,json,shutil,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=Path(tempfile.gettempdir())/'d-relations-browser';out=ROOT/'research/d_relations-evidence';out.mkdir(exist_ok=True)
for p in src.glob('*.png'):shutil.copy2(p,out/p.name)
shutil.copy2(src/'browser-review.json',out/'browser-review.json')
paths=['research/d_relations.en.md','research/d_relations-problems.en.md','research/d_relations-review.en.md','research/d_relations-source-audit.md','dist/chapters/d_relations.html','dist/chapters/d_relations.js','dist/chapters/d_relations.css']
(out/'artifact-hashes.json').write_text(json.dumps({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},indent=2)+'\n',encoding='utf-8')
gate=ROOT/'research/chapter-gate.json';g=json.loads(gate.read_text(encoding='utf-8'))
g.update(currentTopicId='d_relations',state='awaiting_user_approval',nextTopicId=None,lastCompletedReview='Relations chapter written and audited: four principal courses plus Cornell; 46 worked problems, 72 exam rules, four figures, and independently checked closure laboratory.',nextReview='Await explicit student approval of d_relations before promoting it and starting d_functions.',activeWork='Relations review draft completed; no further chapter started.',qualityAuditPath='research/d_relations-quality-audit.md',sourceAuditPath='research/d_relations-source-audit.md',proposedNextTopicId='d_functions',approvedLibraryReview=True)
gate.write_text(json.dumps(g,indent=2)+'\n',encoding='utf-8')
delivery=ROOT/'WEEKLY_DELIVERY.md';text=delivery.read_text(encoding='utf-8');head=text.split('## Current chapter handoff')[0]
delivery.write_text(head+'''## Current chapter handoff

2026-10-02: The student explicitly approved the final revision of the sixteen existing chapters and requested the next chapter. The next scheduled boundary is d_relations (Relations, equivalence, and partial orders), Discrete Mathematics Chapter 5 in Week 2.

The new English chapter has now been written and audited. It synthesizes four genuinely reviewed principal courses from MIT, Stanford, Cambridge, and Oxford, with Cornell as a focused fifth source. It contains 46 fully explained worked problems, 72 complete examination rules, four original vector figures, full proofs, a decision table, and a relation/Warshall laboratory. Source comparisons and corrections are documented in research/d_relations-source-audit.md. Mathematical and presentation checks are documented in research/d_relations-quality-audit.md; exact finite results and browser evidence accompany it.

Study-facing draft: dist/chapters/d_relations.html. Source audit: dist/reviews/d_relations-sources.html. The chapter index lists this chapter under Week 2 as draft. Gate: awaiting_user_approval. Await explicit approval of this chapter before promoting it and beginning d_functions. No archived Iranian examination questions were inspected. No production schedule or universal-correctness guarantee is introduced.

The earlier sixteen-chapter final review remains complete and approved. Its ledger and report are preserved in research/library-review.json, research/LIBRARY_FINAL_REVIEW.en.md, and dist/library-review.html.
''',encoding='utf-8')
print('Saved exact chapter evidence and one-chapter approval gate')
