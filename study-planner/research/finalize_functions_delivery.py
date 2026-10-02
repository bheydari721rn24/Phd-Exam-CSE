"""Preserve exact review evidence and the one-chapter handoff."""
import hashlib,json,shutil,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=Path(tempfile.gettempdir())/'d-functions-browser';out=ROOT/'research/d_functions-evidence';out.mkdir(exist_ok=True)
for p in src.glob('*.png'):shutil.copy2(p,out/p.name)
shutil.copy2(src/'browser-review.json',out/'browser-review.json')
paths=['research/d_functions.en.md','research/d_functions-problems.en.md','research/d_functions-review.en.md','research/d_functions-source-audit.md','dist/chapters/d_functions.html','dist/chapters/d_functions.js','dist/chapters/d_functions.css']
(out/'artifact-hashes.json').write_text(json.dumps({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
p=ROOT/'research/chapter-gate.json';g=json.loads(p.read_text());g.update(currentTopicId='d_functions',state='awaiting_user_approval',approvedTopicId='d_relations',nextTopicId=None,proposedNextTopicId='d_invariants',lastCompletedReview='Deep English functions chapter completed: four genuinely read principal university courses, two supplements, 42 worked problems, 72 complete examination rules, four original figures, and audited fiber laboratory.',nextReview='Await explicit approval of d_functions before promoting it and beginning d_invariants.',activeWork='Functions review draft delivered; no later chapter has been started.');p.write_text(json.dumps(g,indent=2)+'\n')
p=ROOT/'WEEKLY_DELIVERY.md';head=p.read_text(encoding='utf-8').split('## Current chapter handoff')[0]
p.write_text(head+'''## Current chapter handoff

2026-10-02: The student explicitly approved d_relations and authorized the next chapter. Relations is now ready in the chapter index and its reproducible builder preserves that approved status.

The sole new chapter is d_functions, Discrete Mathematics Chapter 6, Week 2. Its English review draft teaches exact typed definitions, fibers, partial functions, composition, cancellation, true and one-sided inverses, image/preimage calculus, quotient factorization, finite function counting, function spaces, and cardinality constructions. Four principal written university courses from Oxford, Stanford, Cambridge, and MIT were genuinely read and compared; CMU and Cornell supplement exercises and inverse checks. It contains 42 fully explained worked problems, 72 complete examination rules, four original vector diagrams, semantic mathematical indices and a MathML summation, and a finite-function/fiber laboratory.

Study page: dist/chapters/d_functions.html. Source comparison: dist/reviews/d_functions-sources.html. The selection and exercise ledger is research/d_functions-source-audit.md. Quality results and explicit limits are in research/d_functions-quality-audit.md, with independent finite reports and exact screenshot evidence. No archived Iranian exam questions were opened or classified.

The gate is awaiting_user_approval. d_functions remains draft until explicit approval. The proposed next chapter is d_invariants; it has not been started. The previous sixteen-chapter final-review ledger remains preserved and approved.
''',encoding='utf-8')
print('Functions evidence saved; gate awaits explicit student approval.')
