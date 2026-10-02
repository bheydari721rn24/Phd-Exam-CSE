"""Preserve exact review evidence and the one-chapter approval handoff."""
import hashlib,json,shutil,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=Path(tempfile.gettempdir())/'d-invariants-browser';out=ROOT/'research/d_invariants-evidence';out.mkdir(exist_ok=True)
for p in src.glob('*.png'):shutil.copy2(p,out/p.name)
shutil.copy2(src/'browser-review.json',out/'browser-review.json')
paths=['research/d_invariants.en.md','research/d_invariants-problems.en.md','research/d_invariants-review.en.md','research/d_invariants-source-audit.md','research/d_invariants-quality-audit.md','dist/chapters/d_invariants.html','dist/chapters/d_invariants.js','dist/chapters/d_invariants.css']
(out/'artifact-hashes.json').write_text(json.dumps({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
p=ROOT/'research/chapter-gate.json';g=json.loads(p.read_text());g.update(currentTopicId='d_invariants',state='awaiting_user_approval',approvedTopicId='d_functions',nextTopicId=None,proposedNextTopicId='d_number',lastCompletedReview='Deep English invariants chapter completed: four genuinely read principal university courses, three supplements, 49 fully worked problems, 80 complete examination rules, four original figures, and independently audited finite-state laboratory.',nextReview='Await explicit approval of d_invariants before promoting it and beginning d_number.',activeWork='Invariants review draft delivered; no later chapter has been started.');p.write_text(json.dumps(g,indent=2)+'\n')
p=ROOT/'WEEKLY_DELIVERY.md';head=p.read_text(encoding='utf-8').split('## Current chapter handoff')[0]
p.write_text(head+'''## Current chapter handoff

2026-10-02: The student explicitly approved d_functions and authorized the next chapter. Functions is now ready in the chapter index and its reproducible builder preserves that approved status.

The sole new chapter is d_invariants, Discrete Mathematics Chapter 7, Week 2. Its English review draft teaches reachable-state semantics, inductive certificates, conservation and impossibility, loop contracts, termination ranks, recursive and structural proofs, generalized accumulators, mutual recursion, substitution, and exact finite-state checking. MIT, Stanford, CMU, and Cambridge supply four genuinely read principal courses; Cornell, Berkeley, and Princeton provide supplements. It contains 49 completely explained worked problems, 80 full-sentence examination rules, four original vector figures, semantic mathematical indices and native MathML limits, and an editable finite-state laboratory.

Study page: dist/chapters/d_invariants.html. Source comparison: dist/reviews/d_invariants-sources.html. Reading scopes and selected exercise mappings: research/d_invariants-source-audit.md. Review evidence and explicit coverage limits: research/d_invariants-quality-audit.md and research/d_invariants-evidence. Independent mathematical and laboratory reports are retained. No archived Iranian examination questions were opened or classified.

The gate is awaiting_user_approval. d_invariants remains draft until explicit approval. The proposed next chapter is d_number; it has not been started. The previous sixteen-chapter library review remains preserved and approved.
''',encoding='utf-8')
print('Invariants evidence saved; gate awaits explicit student approval.')
