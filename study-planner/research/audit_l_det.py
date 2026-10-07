from pathlib import Path
import json,hashlib,shutil,datetime
B=Path(__file__).resolve().parent;R=B.parent;E=B/'l_det-evidence';C=Path('C:/Users/bheydari/AppData/Local/Temp/l-det-sources');C.mkdir(exist_ok=True)
acq=json.loads((E/'acquisition.json').read_text());reading=json.loads((E/'reading.json').read_text())
rows=[]
for a in acq:
 if 'cachePath'in a:rows.append('| '+a['id']+' | '+str(a['pages'])+' | `'+a['sha256']+'` |')
audit='''# Determinants source-selection and reading audit

## Selected written university courses

Selection used chapter coverage, proof quality, identifiable course provenance, examples, geometry, and scientific consistency. Four distinct universities contribute genuinely inspected written course content. Inspection is scoped to determinant-relevant pages, not every page of every full course.

| Priority | University / instructor / course | Inspected scope | Contribution and limits |
|---|---|---|---|
| 1 | Oxford / Richard Earl / M1 Linear Algebra II, Hilary 2026 | PDF pages 5–21 | Definitions, multilinearity, uniqueness, operations, multiplicativity, permutation matrices, structured examples, adjugate, Cramer, basis-invariant linear maps. Page 16 printed indexing mistakes are corrected independently. |
| 2 | Cambridge / Stephen J. Cowley / Mathematical Tripos IA Vectors and Matrices, Michaelmas 2010 | PDF pages 74–84, determinant paragraph on 89, Appendix B on 148 | Signed geometry, permutation sign, transpose and product proofs, cofactors, inverse, computational cost. Read-only reference; source text, diagrams, and pages are not redistributed. |
| 3 | MIT / Gilbert Strang / 18.06SC Linear Algebra, Fall 2011 | Instructional pages 1–3 of sessions 2.5 and 2.6; 1–4 of session 2.7 | Properties, geometric intuition, cofactor explanation, Cramer, volume and tridiagonal recurrence. Printed formula and index errors are explicitly corrected. |
| 4 | UC Berkeley / Alexander Paulin / Math 54, Spring 2018 | All four scanned Determinants pages, visually read | Deletion/minor computation, checkerboard signs, row-operation algorithm and a complete four-by-four elimination example. Compact notes alone would not supply the whole chapter's depth. |

These sources complement rather than simply repeat one another. Original proofs cover additional structured identities and boundary cases after their prerequisites are taught. The chapter is not a stitched copy of source prose.

## Candidate pool and exclusions

Harvard Math 21b (Oliver Knill, Spring 2023), both determinant pages, was reviewed but not selected as a core. The printed Leibniz formula on page 1 includes an extra factor (-1)^(n+1); testing the identity matrix of even order exposes the error. The triple-product parenthesis is also unclosed. These defects were visually confirmed and were not transferred into the lesson.

CMU 21-241 Summer I 2014 (William Gunther) was screened through its calendar and advertised determinant PDF. That PDF actually contains linear-map notes, so the mismatched link does not count as a reviewed determinant course. The ETH-hosted module 110PMA207 notes have uncertain institutional course provenance; hosting alone does not make them an ETH course. Stanford SUMO notes are student-organization material rather than an identified instructor course. Their locations/provenance were screened, not represented as full course readings. This finite accessible pool does not support a claim to have evaluated every university course worldwide.

## Corrections and independent validation

1. Oxford PDF page 16 prints a11 a22 a23 in an identity-permutation term and repeats a23 in the displayed position (3,2). The correct identity term is a11 a22 a33 and the correct entry is a32. The general Leibniz definition, independent enumeration, and the earlier source formula all confirm the repair.
2. Oxford PDF page 7 correctly excludes Sarrus at n >= 4. Text extraction looked like n > 4; visual inspection prevented a false source-error allegation.
3. MIT cofactor summary page 1 prints a11 a23 a33 where the negative permutation term requires a11 a23 a32. It was visually checked against the displayed selected pattern and corrected.
4. MIT Cramer summary page 1 uses Cj1 instead of C1j for a diagonal product and includes an extra A in the final inverse statement. The lesson derives both adjugate identities with explicit indices and verifies products independently.
5. Physical area and volume are always absolute determinants. A signed-area expression is never presented as universally nonnegative.
6. Proofs do not divide by a zero pivot or extend an inverse formula to a singular matrix. Characteristic-two exceptions, order-one adjugates, singular rank cases, strict positivity boundaries, and rectangular dimensions are stated explicitly.

## Coverage mapping

| Chapter sections | Primary course anchors | Independent extension or correction |
|---|---|---|
| 2–7: definition, geometry, permutations, axioms, multilinearity and ledger | Oxford definitions and permutation section; Cambridge 3.7; MIT 2.5–2.6; Berkeley pages 1–4 | Characteristic-two caveat, simultaneous-row examples, explicit determinant ledger |
| 8–12: products, singularity, cofactors, adjugate and Cramer | Oxford 1.1–1.2; Cambridge 3.7.6 and 4.1–4.2; MIT 2.5–2.7; Berkeley page 4 | Rank of adjugate, order-one exception, consistency counterexample, corrected indices |
| 13–17: parameter and structured determinants | Oxford examples 23–24; MIT 2.6 tridiagonal recurrence; Cambridge permutation/operation framework | Schur proof, inversion-free rank-one identity, complete Vandermonde proof, singular parameter ranks |
| 18–22: Gram, special maps, positivity and derivatives | Cambridge geometry/orthogonality; Oxford linear-map determinants; MIT volume | Original Cauchy–Binet proof, complex conjugation distinction, proved positivity bridge, Jacobi/cofactor sensitivity |
| 23–27: computation, solutions and final retrieval rules | Cambridge elimination and Appendix B; Berkeley elimination; all four conceptual anchors | Exact-rational editable lab, 80 original solutions, 80 explicit condition-bearing checks, two authentic adaptations |

## Original examination pages

The repository is pinned to commit bdadf6e2c9cadc4772ae137a96a3da753c7cfd08. PhD CS 1404 Q32 (PDF page 8) and MSc CS 1405 Q44 (PDF page 10) were visually inspected from their original PDFs. All options remain in printed order. The first calibrates a determinant-versus-positivity trap; the second uses a triangular characteristic determinant. The additional determinant-six conclusion for Q44 is explicitly labelled as a derived extension, not a modification of the question. Answers are independently derived, not official answer keys. PDF hashes and checked adaptations are in l_det-authentic.json.

## Source fingerprints

Course PDFs are cached outside the repository and are not part of the published site. Recorded hashes identify the inspected snapshots, not the permanent availability of remote URLs.

| Source ID | PDF pages | SHA-256 |
|---|---:|---|
'''+ '\n'.join(rows)+'''

## References

- University of Oxford — Richard Earl, M1 Linear Algebra II, Hilary 2026: [Official notes](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=61510).
- University of Cambridge — Stephen J. Cowley, IA Vectors and Matrices, Michaelmas 2010: [Official notes](https://www.damtp.cam.ac.uk/user/sjc1/teaching/VandM/notes.pdf).
- MIT — Gilbert Strang, 18.06SC, Fall 2011: [Properties](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/5dd3f8ec0a398fd74264fef3fd591f81_MIT18_06SCF11_Ses2.5sum.pdf), [Cofactors](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/cc79f04d92ee282758780bac2ec5e403_MIT18_06SCF11_Ses2.6sum.pdf), [Cramer and volume](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/f6e46da0d783d8f9c0a25c407c76166a_MIT18_06SCF11_Ses2.7sum.pdf).
- UC Berkeley — Alexander Paulin, Math 54, Spring 2018: [Official determinant notes](https://math.berkeley.edu/~apaulin/Determinants.pdf).
- Harvard — Oliver Knill, Math 21b, Spring 2023, rejected core candidate: [Determinants](https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture14.pdf).
- CMU — William Gunther, 21-241 Summer I 2014, mismatched calendar candidate: [Calendar](https://www.math.cmu.edu/~wgunther/241/m14/index.html).
- ETH-hosted — Lorenz Halbeisen, module 110PMA207, unverified institutional provenance: [Notes](https://people.math.ethz.ch/~halorenz/4students/linalg/linalgln.pdf).
- Stanford SUMO — student organization, not counted as an instructor course: [Notes](https://sumo.stanford.edu/pdfs/LinearAlgebraNotes.pdf).
'''
(B/'l_det-source-audit.md').write_text(audit,encoding='utf-8')
math=json.loads((E/'mathematics.json').read_text());model=json.loads((E/'models.json').read_text());browser=json.loads((E/'browser.json').read_text());ret=json.loads((E/'lesson-and-retention.json').read_text());assert browser['status']=='passed'
quality=f'''# Determinants chapter quality audit

## Delivery scope

This English review draft contains {ret['sections']} teaching sections, {ret['lessonWords']} lesson words before its appended question bank and final rules, 82 fully worked questions (80 independently authored/reconstructed and two authentic original-PDF-checked adaptations), and 80 rewritten final retrieval rules. Each final rule includes a complete condition or numeric calibration; it does not rely on fragments such as “the first value.” Solutions range from {min(ret['solutionWordCounts'])} to {max(ret['solutionWordCounts'])} counted words. Length is evidence of written content, not an automatic quality guarantee.

## Mathematical checks

{math['exactChecks']} exact comparisons passed, including numeric determinants, parameter polynomial identities, Schur-complement counterexamples, Gram and Cauchy–Binet examples, recurrence initial conditions, singular updates, genuine exam consequences, and every saved model state. The editable exact-rational engine was independently compared with SymPy on {math['editableInputs']} deterministic/random matrices of orders two through four, including swaps and singular cases. Its intermediate matrices preserve the stated determinant ledger. The proof and condition review covers exceptional divisions, field characteristic, empty minors, sign conventions and dimension restrictions.

## Concept-specific visuals

There are {model['models']} different models and {model['checkpoints']} independently recomputed checkpoints: oriented parallelograms, shears, selected permutation terms, deleted-row/column cofactors, row elimination with a ledger, adjugate products, Cramer columns, invariant-direction collapse, block elimination, single-column update terms, Vandermonde nodes, determinant recurrences and projected Gram minors. Applicable worked solutions embed the corresponding exact data model. Question-by-question visual decisions are recorded; pure symbolic arguments do not receive unrelated generic animations.

Geometry interpolates actual endpoints and polygon coordinates, keeping edges attached throughout a transition. A transition-preview label states that numerical checks refer to the target checkpoint. Arithmetic operations retain discrete exact matrix checkpoints and animate the changed text/highlighting rather than inventing a continuous row operation. Controls provide previous/next, play/pause, restart, speed, step seeking and keyboard navigation. Models begin paused. Reduced-motion mode suppresses animation, and print mode exposes every checkpoint.

## Browser and typography checks

The chapter passed real Edge desktop and mobile checks. Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono load successfully. Native MathML renders formulas and inline symbols, with {ret['mathElements']} static expressions inspected for balanced fences and complete script bases. No bare closing delimiter is a standalone exponent/subscript base; rendered fences have nonzero dimensions. No links have an underline. All {model['checkpoints']} stored diagram states passed text bounds and six-unit minimum label-padding checks. Controls paused/froze and resumed real animations; reduced motion and print were verified. Six valid editable inputs and six invalid inputs were checked; invalid input preserves the previous result. No runtime error or mobile page overflow was observed. The new chapter is present in both the library and Week 3.

## Retention and editorial review

All 41 preceding chapter HTML hashes remain identical to the starting snapshot, preserving all 2,593 preceding worked questions. The new card is a draft. Previous approval of s_expectation is recorded as version 79. No following chapter has been started. Native-math checks address the user's recurring delimiter and index concerns directly. Source selection and original booklet provenance are documented separately.

## Practical limits

The source pool is bounded and accessible; it is not every university course in existence. Authentic questions here are two relevant calibrations, not an exhaustive classification of the whole examination archive. Printed course errors were corrected, not treated as authoritative. Finite arithmetic and browser checks support the inspected result but do not establish literal 100% perfection or guarantee answers to every unseen question. No diagnostic test has been administered to the learner, and this draft remains subject to explicit approval.

## Evidence

- acquisition.json and reading.json: source fingerprints and actual reading scope.
- mathematics.json: exact comparison records, including the editable engine.
- models.json: independently recomputed checkpoint inventory.
- browser.json and the chapter's rendered screenshots: layout, fonts, controls, print and mobile.
- prior-library.json and lesson-and-retention.json: preceding content preservation.
- l_det-authentic.json: immutable PDF paths, hashes, option order and independent solutions.
'''
(B/'l_det-quality-audit.md').write_text(quality,encoding='utf-8')
# Keep third-party source-page screenshots in the external reading cache, not the source repository.
external=C/'reading-images';external.mkdir(exist_ok=True)
prefixes=('berkeley-','oxford-','harvard-','mit-','cambridge-','ms-','phd-')
for p in E.glob('*.png'):
 if p.name.startswith(prefixes):
  assert p.resolve().is_relative_to(E.resolve());dest=external/p.name;assert dest.resolve().is_relative_to(external.resolve());shutil.move(str(p),str(dest))
g=json.loads((B/'chapter-gate.json').read_text());g.update(sourceAudit='research/l_det-source-audit.md',qualityAudit='research/l_det-quality-audit.md',nextReview='Complete only the l_det review draft and publication; then await explicit approval.',reviewEvidence=['research/l_det-evidence/'+n+'.json'for n in['reading','mathematics','models','browser','lesson-and-retention']],activeWork='Only l_det is in progress. Previous s_expectation approved; all 41 prior HTML files retained.');(B/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
print('Wrote source and quality audits; cached reference screenshots remain outside the repository.')
