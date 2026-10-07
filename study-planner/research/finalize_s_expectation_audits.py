from pathlib import Path
import json,hashlib,re
B=Path(__file__).resolve().parent;R=B.parent;E=B/'s_expectation-evidence'
a=json.loads((E/'acquisition.json').read_text());core=[x for x in a if x['university']!='stanford']
reading=dict(status='completed',coreUniversities=['Oxford','MIT','UC Berkeley','Carnegie Mellon'],coreScopes=core,additionalLecture=dict(university='Cornell',course='CS2800 Fall 2017 Lecture 9',url='https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec09-expect.html',scope='Complete accessible official lecture text',provenance='Read via official web text; no downloaded-file hash claimed'),excludedCandidate=dict(university='Stanford',reason='Locally acquired advertised Moments PDF instead contains Random Variables & Binomial. Web-reader content and local bytes disagree; excluded from expectation reading count.',sha256=next(x['sha256']for x in a if x['university']=='stanford')),sourceCorrections=['Oxford loop-sum leading coefficient is 1/2 on ln n.','CMU perfectly dependent average has original variance, not original standard deviation.'],figureInspection=['MIT center-of-mass figure, Berkeley expectation and occupancy figures, original PhD Q72 page 16, original MSc Q121 page 26, and excluded Stanford PDF pages were inspected.'])
(E/'reading.json').write_text(json.dumps(reading,indent=2)+'\n')
models=json.loads((E/'models.json').read_text());math=json.loads((E/'mathematics.json').read_text());browser=json.loads((E/'browser.json').read_text());ret=json.loads((E/'lesson-and-retention.json').read_text())
assert all(x['status']=='passed'for x in [models,math,browser,ret])
quality=f'''# Expectation: final quality and coverage audit

## Delivered scope

The scheduled Week 3 topic s_expectation is an English review draft with {ret['sections']} sections and {ret['lessonWords']} lesson words, excluding the separately inserted solved bank and review notes. The bank has 80 independently written course-family/original questions and two original-PDF-checked authentic examination adaptations. All 82 have complete solutions. The 80 final notes state a trigger or rule, a condition or warning, and a worked calibration; they are complete sentences rather than compressed fragments.

Four actually reread written courses from four universities form the core synthesis. Cornell provides a fifth university lecture check. Stanford's mismatched local acquisition is explicitly excluded. Sources and all reference explanations are English. The chapter evaluates a documented accessible pool; it does not claim every existing course was reviewed or every copyrighted course exercise reproduced.

## Mathematical and semantic audit

{math['exactChecks']} independent mathematical checks passed, including rational weighted means and moments; exhaustive permutations, sample subsets, allocations, runs, overlapping windows, graph edges and triangles; geometric caps; hidden-parameter mixtures; compound payoffs; and both authentic answers. Every question's full solution was read during the final semantic review. Infinite-support examples distinguish finite, extended and undefined means. Infinite signed algebra carries integrability conditions. Linearity is separated from independence, and dependent product and random-length counterexamples are explicit.

Models have {models['models']} distinct stored instances and {models['checkpoints']} checkpoints. Their snapshots were recomputed against their corresponding arithmetic, exact record prefixes, occupancy counts, layer sums and direct loss formulas. Concrete diagrams are labelled as realizations or numeric calculations; symbolic proofs are not replaced by those diagrams. Per-question visual decisions identify where an actual numeric diagram is useful and where a complete symbolic proof or finite table is clearer.

## Typography and real browser evidence

Real Microsoft Edge rendered all {models['checkpoints']} checkpoints. Layout checks found no stored-frame geometry, text-bound or enclosed-label padding errors. Permutation arrows end at the box boundaries; graph edges meet circle boundaries. The actual screenshots were inspected. The moving scanner was paused during its transition, remained frozen, and resumed; previous, next, seek and reset worked. Reduced-motion mode created no active movement. Printable checkpoint sequences were visible under print styling.

The browser confirmed Source Sans 3 prose, Newsreader headings, STIX Two Math mathematics, and JetBrains Mono code. It found {browser['counts']['math']} native MathML nodes, {browser['nativeMath']['fractions']} fraction structures and {browser['nativeMath']['scripts']} script/limit structures; none was invisible. No link was underlined. The 390-pixel viewport had no page overflow; large exact diagrams use local horizontal scrolling. Seven editable modes passed ten numerical/boundary fixtures, including height-eight tails, zero-success finite caps and zero-ball allocation. Nine invalid-input cases preserved the preceding model and displayed an explanatory error. No runtime error occurred.

## Preservation and workflow

All 40 preceding chapter HTML files match their captured SHA-256 values. Their 2,511 complete problems remain retained; the library now has 41 chapters and 2,593 complete problems. The previous discrete-variable chapter was marked approved only after the student's explicit approval. This new chapter remains a draft awaiting explicit approval after verified publication. No subsequent chapter has started.

## Remaining limits

The audits check stated models and reviewed statements; they are not a proof of literal universal correctness or a promise of answering every unseen examination question. Full covariance theory, continuous and conditional expectation, convergence theorem proofs and inference remain separate scheduled chapters. The examination pages inspected here do not constitute an exhaustive classification of the scanned archive. Floating-point diagrams use rounded labels; rational checks and exact symbolic reasoning are separately recorded. The finite laboratory is not a random sampling guarantee or a substitute for a theorem.

Evidence: reading.json, acquisition.json, mathematics.json, models.json, browser.json, lesson-and-retention.json and question-visual-decisions.json in research/s_expectation-evidence. Source provenance and immutable examination links appear in the chapter and source audit. Publication status will be recorded from the actual hosting response and exact source commit, rather than predicted.
'''
(B/'s_expectation-quality-audit.md').write_text(quality,encoding='utf-8')
print('Source reading evidence and final quality audit written after passed checks.')
