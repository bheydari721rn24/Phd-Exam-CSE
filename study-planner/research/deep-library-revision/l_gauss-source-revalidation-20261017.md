# Gaussian elimination: bounded source revalidation, 17 October 2026

## What was actually reread

This source subtask independently reread three university sources. The parent task reported a fresh complete reading of MIT's 21-page Gaussian elimination handout; that reading was not repeated by this reviewer. The combined project evidence must preserve that distinction. This record does not declare the individual chapter review complete.

| University | Written source and exact fresh scope | Method and acquisition |
|---|---|---|
| Oxford | M1 Linear Algebra I, `lecture_notes22.pdf`: printed pages 3–8 and 16–20, corresponding to PDF pages 4–9 and 17–21 | Complete extracted text of the eleven pages was read. Original rendered printed pages 6 and 18 were additionally inspected to verify the newly detected source errors. Local official-site download: 495,950 bytes; 78 PDF pages. |
| UC Berkeley | Alexander Paulin, Systems of Linear Equations and Row Reduction: all seven handwritten PDF pages | Every page was rendered and visually read individually, including the two introductory solves, the five-variable reduction and classification diagrams. Local official-site download: 4,991,758 bytes. |
| Stanford | CME108/MATH114: all three Gaussian-elimination HTML parts, all three LU parts and all five Permuted-LU parts | All eleven instructional HTML text and mathematical bodies were freshly read. Local official-site downloads recovered all eleven historical document hashes exactly. External linked media or separate image assets were not independently reviewed. |

All thirteen downloaded documents match the corresponding historical SHA-256 and byte counts in `dist/evidence/l_gauss/sources.json`. The accompanying JSON records every exact URL and verified hash. Original PDFs and rendering caches were moved outside the checkout to `C:/Users/bheydari/AppData/Local/Temp/phd-gauss-source-revalidation-20261017-agent`; they are not public redistribution deliverables. Instructor metadata is inherited from the earlier audit rather than newly established here.

The web reader could not open the Oxford URL and timed out on three Berkeley screenshot requests. Local official-site downloads subsequently succeeded. Berkeley's complete seven-page visual review therefore uses the local rendered originals, not an inference from an inaccessible web result.

## Newly detected errors and qualifications

### Oxford Example 7(b), printed page 6: the displayed subtraction has wrong signs

Immediately before its final arrow, the first two augmented rows are `[1,1,1,1 | 4]` and `[0,1,-4,-5 | -7]`. The stated operation subtracts the second row from the first. Its correct result is `[1,0,5,6 | 11]`; the source instead displays `[1,0,-5,-6 | -11]`. This is an arithmetic error, separately from the previously documented failure to clear the augmented last-column pivot. The existing contradiction row still proves inconsistency, so the classification is unaffected. A copied row-operation animation must use the correct arithmetic, not merely arrive at the same classification.

### Oxford Proposition 44(b), printed page 18: consistency is required

The coefficient condition alone does not imply a unique solution. The augmented RREF `[[1 | 0], [0 | 1]]` has nonzero coefficient rows forming `I_1`, but its last equation is impossible. The correct general criterion is `rank(A) = rank([A|b]) = n`. Equivalently, require both absence of a contradictory augmented row and a pivot in every coefficient column. The proof below the source proposition implicitly assumes matching coefficient/augmented nonzero-row counts; that assumption needs to appear in the statement too.

### Stanford Gaussian Part 1: the motivating backward-substitution formula reverses a sign

For `-8v - 2w = -12`, the source prints the expression `(-12 + 2w)/8` but claims the resulting value is 1 at `w=2`. That expression actually gives -1. The correct expression is `(12 - 2w)/8`, which gives 1. Deriving the numerator from the original equation prevents reproducing this transcription error.

### Stanford Permuted-LU Part 5: conjugation needs the active-row condition

A later elimination permutation fixes the already completed pivot coordinates. Under that condition, conjugating a completed Gauss transform preserves the appropriate strictly lower multiplier structure. An arbitrary row swap need not do so: with `G = [[1,0],[2,1]]` and the two-coordinate swap `P`, the conjugate `PGP^-1 = [[1,2],[0,1]]` is upper triangular. The chapter should state the restriction when explaining why previous multiplier columns are swapped. One intermediate equality in the source also drops the earlier factor `P_1`; retain that factor throughout the derivation.

These findings add to, rather than replace, the historical audit's triangular-side reversal, missing target-row subtraction, inverse-exponent typo, ambiguity in in-place multiplier updates, and other recorded corrections.

## Source-specific conceptual improvements to retain in the chapter

1. **Oxford: preserve complete necessity and sufficiency.** A displayed candidate is not yet a complete solution set. Derive the constraints, assign independent parameters only to free coefficient variables, prove every constructed vector satisfies all equations, and show every solution arises. State consistency before uniqueness. For Example 8, branch before dividing by the parameter: determinant `alpha(alpha+2)`, a unique solution for `alpha != 0,-2`, inconsistency at 0, and a one-parameter family at -2. Independent exact ranks are respectively `(2,3)` and `(2,2)` for the coefficient/augmented matrices in the exceptional cases.
2. **Oxford: distinguish coefficient elimination from full augmented RREF.** A contradiction is enough to stop a solve, but it does not make every displayed matrix a full RREF. A normalized augmented pivot must also be cleared above. Existence follows by induction on the smaller bottom-right block; the uniqueness proof needs its own argument, rather than borrowing a deferred source theorem.
3. **Berkeley: synchronize geometry with actual equations.** Its first example is the intersection of `x-y=-1` and `4x+2y=8` at `(1,2)`. Its second gives the line `(5/2-8t,t-1/2,t)` from two planes. Draw those actual examples with equal coordinate scales when metric geometry is implied, and show why replacing one equation preserves the common intersection even though the individual line/plane changes.
4. **Berkeley: keep nonconsecutive pivots visible.** The five-variable example has pivots in columns 1,3,5 and free variables in columns 2,4. Its complete solution is `(s+5t-9,s,4-4t,t,3)`. In an accompanying diagram, label the augmented load separately: it is neither a free variable nor another coefficient unknown. The zero/one/infinitely-many classification assumes an infinite scalar field; over a finite field a consistent free-variable family has a finite cardinality.
5. **Stanford: separate a factorization from a solve.** Factor the coefficient matrix once, then apply the recorded permutation and two triangular solves to each new load. State the convention `PA=LU`, so the solve order is `Ly=Pb`, `Ux=y`. Explain nonzero diagonal requirements and explicit simultaneous row swaps; sequential assignment without a temporary row would overwrite data.
6. **Stanford: derive exact operations and stability claims locally.** Count the declared loops rather than importing the source's inconsistent general flop-table row. Preserve completed multipliers when pivoting, update only the trailing coefficient block, and never infer exact singularity solely from a small floating-point pivot. The three-digit example should distinguish exact rational elimination, rounding at each declared arithmetic operation, residual size and forward error. Partial pivoting helps that example without becoming a universal error guarantee.

## Boundaries

This is a revalidation of a bounded five-course historical candidate pool, not an exhaustive comparison of all world courses. Restricted Stanford HW2 was not accessed, and references to exercises in unavailable books were not counted as fully read questions. No new instructor attribution or full-course homework coverage is claimed. The exact independent checks and acquisition evidence are in the adjacent JSON file. The chapter's overall semantic, answer, animation and browser review remains the parent task's separate responsibility.
