"""Preserve chapter review evidence and the explicit one-chapter approval gate."""
import hashlib,json,shutil,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=Path(tempfile.gettempdir())/'d-number-browser';out=ROOT/'research/d_number-evidence';out.mkdir(exist_ok=True)
for p in src.glob('*.png'):shutil.copy2(p,out/p.name)
shutil.copy2(src/'browser-review.json',out/'browser-review.json')
paths=['research/d_number.en.md','research/d_number-problems.en.md','research/d_number-review.en.md','research/d_number-source-audit.md','research/d_number-quality-audit.md','dist/chapters/d_number.html','dist/chapters/d_number.js','dist/chapters/d_number.css']
(out/'artifact-hashes.json').write_text(json.dumps({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
p=ROOT/'research/chapter-gate.json';g=json.loads(p.read_text());g.update(currentTopicId='d_number',state='awaiting_user_approval',approvedTopicId='d_invariants',nextTopicId=None,proposedNextTopicId='a_recurrence',lastCompletedReview='Deep English number-theory chapter completed: four genuinely read university courses, 40 fully worked problems, 70 complete examination rules, four original diagrams, and independently verified exact residue laboratory.',nextReview='Await explicit approval of d_number before promoting it and beginning a_recurrence.',activeWork='Number theory review draft delivered; no later chapter has been started.');p.write_text(json.dumps(g,indent=2)+'\n')
p=ROOT/'WEEKLY_DELIVERY.md';head=p.read_text(encoding='utf-8').split('## Current chapter handoff')[0]
p.write_text(head+'''## Current chapter handoff

2026-10-02: The student explicitly approved d_invariants and authorized the next chapter. Invariants is now ready in the chapter index; its reproducible builder preserves that approved status.

The sole new chapter is d_number, Discrete Mathematics Chapter 8, Week 2: Divisibility, Modular Arithmetic, and Number Theory. The English review draft teaches signed divisibility and division, gcd/lcm and prime factors, extended Euclid and integer equations, modular units and full linear fibers, ordinary and generalized CRT, totient and safe power reduction, prime-power boundaries, divisor functions and factorial valuations, exact quadratic root classifications, primality reasoning, additive cycles, and mathematical RSA correctness. MIT, Berkeley, CMU, and Cambridge are four genuinely read principal courses selected through a documented eight-candidate comparison. The chapter includes 40 fully explained problems, 70 full-sentence examination rules, four original vector figures, native mathematical limits and indices, and an exact residue-map laboratory.

Study page: dist/chapters/d_number.html. Source comparison: dist/reviews/d_number-sources.html. Actual reading scopes: research/d_number-source-audit.md. Mathematical and visual evidence: research/d_number-quality-audit.md, research/d_number-finite-check.json, and research/d_number-evidence. No deferred Iranian examination questions were opened or classified.

The gate is awaiting_user_approval. d_number remains draft until explicit approval. The proposed next chapter is a_recurrence, following the Week 2 subject sequence; it has not been started. Previous chapter and library-review evidence remain preserved.
''',encoding='utf-8')
print('Number theory evidence saved; explicit student approval is required before the next chapter.')
