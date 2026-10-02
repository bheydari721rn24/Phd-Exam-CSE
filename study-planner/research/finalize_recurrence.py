"""Retain actual QA evidence and the single-chapter approval handoff."""
import hashlib,json,shutil,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'research'
qa=Path(tempfile.gettempdir())/'a-recurrence-browser'
report=json.loads((qa/'browser-review.json').read_text());assert len(report)==1
row=report[0];assert row['topicId']=='a_recurrence' and len(row['figures'])==4
assert row['mobile']['document']==390 and not row['mobile']['formulaOverflow']
assert all(not f['outside'] and not f['overlap'] for f in row['figures'])
assert row['printStyle']['diagramOverflow']==0
evidence=R/'a_recurrence-evidence';evidence.mkdir(exist_ok=True)
for p in [qa/'browser-review.json',*qa.glob('*.png')]:shutil.copy2(p,evidence/p.name)
gatepath=R/'chapter-gate.json';gate=json.loads(gatepath.read_text())
assert gate['currentTopicId']=='a_recurrence' and gate['approvedTopicId']=='d_number'
gate.update(state='awaiting_user_approval',proposedNextTopicId='a_divide',nextTopicId=None,
 lastCompletedReview='Deep English recurrence chapter: four genuinely read principal universities plus Cornell and MIT theorem supplements, 40 fully worked problems, 80 complete rules, four original diagrams, native MathML, and independently verified arbitrary-precision laboratory.',
 nextReview='Wait for explicit student approval of a_recurrence; only then promote it and begin a_divide.',
 activeWork='Delivered a_recurrence review draft; waiting for explicit student approval.')
gatepath.write_text(json.dumps(gate,indent=2)+'\n')
p=ROOT/'WEEKLY_DELIVERY.md';t=p.read_text(encoding='utf-8')
t=t.split('## Current chapter handoff')[0]+'''## Current chapter handoff

2026-10-02: The student explicitly approved d_number and authorized the next chapter. Number theory is ready in the chapter index; its reproducible builder preserves that approved status.

The sole new chapter is a_recurrence, Week 2 Algorithms: Algorithmic Recurrences and Solution Theorems. The English review draft teaches recurrence modeling, exact and asymptotic sums, first-order normalization, elementary characteristic roots, complete recursion trees, substitution and slack, master cases and critical real logarithmic powers, exact balanced rounding, unequal mass and the unperturbed Akra–Bazzi theorem with proof, transformed arguments, and work/span/storage/expectation distinctions. Eight university candidates were documented; MIT, Stanford, CMU, and Princeton are four genuinely read principal courses, with read Cornell and MIT theorem supplements. There are forty fully explained problems, eighty full-sentence rules, four original vector diagrams, native mathematical limits and indices, and an exact arbitrary-precision recurrence-level laboratory.

Study page: dist/chapters/a_recurrence.html. Source comparison: dist/reviews/a_recurrence-sources.html. Actual reading scopes: research/a_recurrence-source-audit.md. Mathematical and visual evidence: research/a_recurrence-quality-audit.md, research/a_recurrence-math-checks.json, and research/a_recurrence-evidence. No deferred Iranian examination questions were opened or classified.

The gate is awaiting_user_approval. a_recurrence remains draft until explicit approval. The proposed next chapter is a_divide, following the Week 2 subject sequence; it has not been started. Previous chapter and library-review evidence remain preserved.
'''
p.write_text(t,encoding='utf-8')
paths=[R/name for name in ['a_recurrence.en.md','a_recurrence-problems.en.md','a_recurrence-review.en.md','a_recurrence-source-audit.md','a_recurrence-quality-audit.md','a_recurrence-math-checks.json','a_recurrence-source-downloads.json','build_recurrence_chapter.py','verify_a_recurrence_en.py','qa_recurrence_browser.py','chapter-gate.json']]
paths += [ROOT/'dist/chapters'/name for name in ['a_recurrence.html','a_recurrence.js','a_recurrence.css']]
paths += [ROOT/'dist/reviews/a_recurrence-sources.html',ROOT/'dist/lessons.json',ROOT/'WEEKLY_DELIVERY.md',*evidence.glob('*.png'),evidence/'browser-review.json']
manifest={str(p.relative_to(ROOT)).replace('\\','/'):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in paths}
(evidence/'artifact-hashes.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Retained actual screenshots and measurements; a_recurrence is awaiting explicit approval.')
