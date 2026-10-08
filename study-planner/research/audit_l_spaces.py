from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_spaces-evidence'
mat=json.loads((E/'mathematics.json').read_text());browser=json.loads((E/'browser.json').read_text());lesson=json.loads((E/'lesson-and-retention.json').read_text());models=json.loads((E/'models.json').read_text())
assert all(x['status']=='passed'for x in[mat,browser,lesson,models])
assert browser['geometry']['models']==models['models']and browser['geometry']['frames']==models['checkpoints']
s=f'''# Vector Spaces, Subspaces, Bases, and Dimension: Quality Audit

## Written chapter and problem bank

The English review draft has 29 teaching sections and {lesson['lessonWords']} counted lesson words before the appended bank and final rules. Its central proofs include the subspace test, finite-basis exchange, uniqueness of basis size, basis extension/extraction, the two-subspace dimension formula, direct-sum uniqueness, quotient dimension and restriction of scalars. The discussion separates fields, operations, finite versus infinite dimension, affine fibers and vector subspaces.

There are 82 complete worked problems: 80 original or independently reconstructed items, plus two original-PDF-checked authentic examination adaptations. The original solutions contain between {min(lesson['solutionWordCounts'])} and {max(lesson['solutionWordCounts'])} counted words each, with actual equations, constructions or counterexamples. Counts and length are descriptions, not automatic measures of quality. All 80 final rules were written independently as complete retrieval statements with hypotheses and explicit checks or counterexamples, rather than extracted as vague sentence fragments. The summary and final rules complement the full teaching text.

## Source and scope review

The source audit documents four genuinely read written courses from Oxford, ETH Zurich, MIT and Stanford, along with CMU/Harvard comparisons and a separately identified Berkeley access screen. Reading boundaries, document hashes and discovered source corrections are recorded. It does not call a title or access check a full reading. Extensions such as quotient coordinates and finite-field basis counts are independently derived with explicit assumptions. The candidate pool is bounded and does not claim worldwide exhaustive inspection.

## Mathematical verification

{mat['exactChecks']} exact comparisons passed. These include concrete basis membership and independence, kernel directions, polynomial identities, parameter exceptions, finite-field counts, structured matrix freedoms, quotient coordinates, adapted-basis dimension checks, and the authentic answer calculations. Universal and infinite-dimensional statements require their supplied proofs; they are not falsely certified by a few numerical samples.

The new exact-rational rectangular generator laboratory was independently compared with SymPy on {mat['editableInputs']} deterministic/random inputs of 2–4 rows and 1–5 columns. The comparison checked ranks, original pivot-column bases, nullspace bases, consistent/inconsistent targets and reconstructed target coefficients. Every intermediate row operation was verified through an independently tracked row operator against the original generator or augmented matrix. Exact arithmetic uses integer ratios, never a floating-point rank threshold. Internal verification failure rejects a result.

## Visual teaching and problem-specific diagrams

There are {models['models']} distinct models with {models['checkpoints']} stored mathematical checkpoints. These include homogeneous and affine planes, union-versus-sum failure, redundant parameter directions, incremental basis selection, parameter-dependent rank, original pivot columns, exchange, coordinate changes, polynomial contributions, symmetric trace constraints, symmetric/skew decomposition, coupled row/column balances, intersecting planes, three-space dependence, an oblique complement, quotient representatives, finite-field tables, sensor ambiguity and an orthogonal projection. Applicable questions embed their actual model or an explicitly labelled specialization. The quotient example uses the question's actual coset and coordinates; the exchange model states that its drawing is restricted to the first two basis directions while the third is retained.

Plane drawings use one fixed oblique camera and explicitly say they are projections; apparent screen overlap is not used as a proof of equality. Geometry interpolates actual endpoints and polygon coordinates, keeping linked paths attached. Matrix arithmetic uses discrete exact checkpoints and changed-entry highlighting. Controls begin paused and provide previous/next, play/pause, restart, speed and seeking; reduced-motion and print behavior were checked. A transition preview explicitly identifies numeric checks as describing the target checkpoint.

## Browser, fonts and formula layout

Real Edge desktop and 390-pixel mobile checks passed without runtime errors or page overflow. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono loaded. Native MathML separates mathematical symbols from prose. All {lesson['mathElements']} static mathematical expressions passed delimiter and script-base inspection: no isolated closing fence is the base of an exponent or subscript, and displayed fences have nonzero dimensions. No link underline was observed.

All {models['checkpoints']} stored diagram states passed text-bound, collision and minimum label-padding checks. Real animation time was frozen by pause and advanced by resume. Reduced motion suppressed animation; print exposed stored checkpoints. Seven valid laboratory inputs included zero rank, dependence, rectangular shape, inconsistent targets and a dense integer matrix producing rational intermediate values. Six invalid inputs retained the preceding valid result. The full matrix also appears as native MathML beneath the SVG value grid.

The chapter link is present in both Week 3 and the library. The local library now has 43 chapters and 2,757 worked questions. All 42 preceding HTML hashes and 2,675 preceding questions remain unchanged. Determinants version 80 has been approved; this new chapter remains a review draft.

## Remaining limits and approval

This is a carefully reviewed finite chapter, not a guarantee of literal perfection or of performance on every future unseen examination. The two authentic questions calibrate the specific scope and are not claimed to exhaust the archive. Their options were visually checked in the original order and answers are independently derived, not official keys. Infinite-dimensional material marks the boundary of the finite theory rather than claiming a full functional-analysis course. No learner diagnostic test was administered. A following chapter requires explicit approval of this draft.

## Evidence records

- acquisition.json and reading.json: downloaded document fingerprints, true reading locations and source corrections.
- mathematics.json: exact comparisons and independent laboratory checks.
- models.json and question-visual-decisions.json: model inventory and question-level representation decisions.
- browser.json and rendered screenshots: actual fonts, diagrams, interactions, print and mobile.
- prior-library.json and lesson-and-retention.json: unchanged preceding pages and content counts.
- l_spaces-authentic.json: pinned original PDF provenance, option order, file hashes and independent solutions.
'''
(B/'l_spaces-quality-audit.md').write_text(s,encoding='utf-8')
g=json.loads((B/'chapter-gate.json').read_text());g.update(sourceAudit='research/l_spaces-source-audit.md',qualityAudit='research/l_spaces-quality-audit.md',nextReview='Finish publication of the reviewed l_spaces draft, then await explicit approval.',activeWork='l_spaces passed exact arithmetic, written scope, font, mathematical delimiter, animation, print, mobile and retention checks. Preparing private publication.',publicationState='prepared_for_publication',reviewEvidence=['research/l_spaces-evidence/'+x+'.json'for x in['reading','mathematics','models','browser','lesson-and-retention']])
(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
print('Wrote evidence-based chapter quality audit and updated the active gate without starting another chapter.')
