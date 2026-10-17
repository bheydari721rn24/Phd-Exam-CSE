# Gaussian elimination: original examination recheck, 17 October 2026

## Source provenance and visual scope

Both original examination PDFs were available in the desktop repository. Their current bytes were independently compared with both the SHA-256 recorded in `research/l_gauss-authentic.json` and the exact Git blobs at archive commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. All comparisons match.

| Placement | Original archive path | Exact PDF SHA-256 | Original page inspected |
|---|---|---|---|
| PhD CS 1404 Q33 | `Exams/Phd/CS/1404/Q892A-PHD1404-[www.konkur.in].pdf` | `928e51b55059b3094583f9c190e260b405ec775da05f6c7679675e332a8a6f40` | PDF page 8, also printed page 8; the header identifies Computer Science and Bioinformatics, code 2247, booklet 892A. |
| MS CS 1405 Q113 | `Exams/MS/CS/1405/Q257A-Arshad1405-[www.konkur.in].pdf` | `198f75f9f9d195adc5c09ab14d17029e63a3cd11030d62cffcdfcb5df7627527` | PDF page 25, also printed page 25; Computer Science, code 1209, booklet 257A. |

Both complete pages were rendered at 1.7 scale and visually inspected. Q113's alternatives were additionally rendered at 4 scale with PDF-coordinate crop `[390,135,565,270]` to distinguish the original Persian digits precisely. Image paths, hashes, scale factors and clip coordinates are recorded in the adjacent JSON. Temporary images are outside the checkout at `C:/Users/bheydari/AppData/Local/Temp/phd-gauss-authentic-recheck-20261017-agent`; this record does not redistribute full booklets.

## PhD CS 1404 Q33: translation and constructive answer verified

The original states that L and U are respectively lower and upper triangular, gives `LU = [[3,-2,4],[0,5,1],[6,2,3]]`, and asks which displayed column vector can be the first column of L. It does **not** impose a unit diagonal on L. The current translated stem, matrix and all four alternatives match the original: `(-1,0,2)`, `(1,0,-2)`, `(-1,0,-2)`, `(1,2,0)`, in that numbered order.

Because U is upper triangular, its first column is `(u11,0,0)`. Thus the first column of A equals `u11` times the first column of L. Since A's first column is `(3,0,6)`, any candidate must have zero middle coordinate, nonzero first coordinate and third coordinate twice its first. Only alternative 3 qualifies.

This necessity test is supplemented by an existence certificate. Take

- `L = [[-1,0,0],[0,1,0],[-2,6/5,1]]`;
- `U = [[-3,2,-4],[0,5,1],[0,0,-31/5]]`.

Exact matrix multiplication gives the original A. These triangular factors therefore realize alternative 3. The scaling is legitimate: start from unit-lower Doolittle factors and multiply L's first column by -1 while dividing U's first row by -1. A convention imposed by a solver must not be mistaken for a restriction in the question. The answer remains an independent derivation, not an asserted official key.

## MS CS 1405 Q113: genuine distractor transcription error

The translated equations and nonnegative-integer domain match the original: `x1+x2+x3=5` and `x1+x2+x3+x4+x5=20`. Alternatives 2–4 also match. **Original alternative 1 is 37 (Persian ۳۷), not the Gaussian bank's 32.** This difference is clear in the high-resolution original crop.

Subtracting the first equality from the second gives `x4+x5=15`. For the first group, choosing x1 from 0 through 5 leaves respectively 6,5,4,3,2,1 choices for `(x2,x3)`, giving 21 triples. For the second group, choosing x4 from 0 through 15 forces x5, giving 16 pairs. Every admissible five-tuple has one unique triple/pair decomposition. Consequently the count is `21*16=336`, alternative 4.

An additional independent finite enumeration loops over x1,x2,x3,x4 from 0 through 20, sets `x5=20-x1-x2-x3-x4`, and accepts exactly the nonnegative vectors satisfying the first equality. It finds 336 vectors. The source's additive distractor is therefore meaningful: `21+16=37`. The other distractors evaluate to `C(24,4)+C(7,2)=10647` and `C(24,4)*C(7,2)=223146`; neither enforces the coupled constraints through a unique object decomposition.

## Attribution drift and required propagation

The canonical `research/exam-calibration/actual-items.json` already records Q113 alternative 1 as 37, with a 12 October source correction. `research/d_counting-authentic.json` also has 37. The separate Gaussian placement retained the stale value 32 while its `translationStatus` still claimed a rendered-source check. This is a copied-record drift, not a change in the examination source. Update the Gaussian bank and rendered question without rerunning an old builder that would discard subsequent chapter revisions. Its existing explanation about erroneously adding the two group counts correctly describes 37 once the option is repaired.

`research/author_gauss_problems.py` currently obtains this MS item from the corrected canonical bank, so its import source is already correct; rerunning the entire generator is unnecessary and potentially destructive to later edits. PhD Q33 inherits common booklet metadata from a same-page Q30 template, but the Q33 stem/options have now been independently verified directly on their own original item.

Both are authentic examination placements; the counting item is explicitly a revisit. Neither is an original question authored for this chapter, a newly discovered placement in this recheck, or an official-answer-key claim. This subtask modified only its recheck reports. No full-archive examination coverage or whole-chapter completion is claimed.
