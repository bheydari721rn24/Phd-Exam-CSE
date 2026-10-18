# Rank chapter: written-source revalidation, 18 October 2026

## What was actually read

Four official PDFs were freshly downloaded, fingerprinted, and their stated scopes read in this task. Download success is recorded separately from reading. No whole-course or worldwide exhaustive reading claim is made. The complete current `l_rank.en.md` lesson was read and reconciled with the selected sources; the problem bank and browser inspection are separate work.

| University and course | Pages actually reread, one-based PDF numbering | Teaching contribution |
| --- | --- | --- |
| MIT 18.700, Fall 2013, David Vogan, Gaussian Elimination | 13–20 | Row transformations, preserved kernel/row space, transformed column space, rank equality, canonical RREF bases and tall left inverse |
| Oxford M1 Linear Algebra I, 2022, Andrew Wathen as course lecturer | 42–51, 57–61, 68–69 | Exchange and dimension, basis extension, dimension formula, rank–nullity proof, one-sided inverses, restriction bound and rank factorization |
| Stanford EE263, Autumn 2007–08, Stephen Boyd, Lecture 3 | 1–19, slide labels 3–1 through 3–19 | Null-space ambiguity, attainable measurements, injection/surjection, inverse direction, dual bases and dimension interpretation |
| UC Berkeley Math 54, Spring 2018, Alexander Paulin, Rank and Nullity | Both handwritten pages, rendered and visually read | Exact four-by-five matrix, original pivot-column extraction, independent kernel directions and rank–nullity count |

The mathematical ranking remains chapter-specific: Oxford for proofs; MIT for row-operation and inverse precision; Berkeley for the concrete exact example; Stanford for interpretation. All four contribute different components. The fifth CMU comparison in the previous audit was not freshly reread here and remains explicitly historical.

## Fingerprints and access

All four requests succeeded on this run. The Oxford web reader itself returned an internal error, but the direct official HTTP download succeeded and yielded a valid 78-page PDF. Thus Oxford reading is based on the downloaded official document, not a search snippet.

| Document | SHA-256 |
| --- | --- |
| MIT | `7e6f2c9a2a3681d95c1ab2a41ba23fff43fdc339cffaf93c809c3898ec5985a3` |
| Oxford | `b7b49ddc40a68cd3d4376143178d259140a0fa01f5098c7df295d6ef85cf69ba` |
| Stanford | `a38713dbed8b74cd3f50491b9e476072a586727a5d0c7e8f6e991231b1f66e3f` |
| Berkeley | `2282a237bbdd0b9d9f0030cf91ec2a66c442c3bc1d00c95f40605338e139d76b` |

## Corrections that must not be imported from sources

1. **MIT PDF p. 13:** The prose says to multiply a row with leading entry 3 by −1/3; its own diagram correctly uses +1/3. The positive reciprocal is required. The original rendered page was inspected.
2. **MIT PDF p. 18:** The third displayed supposed two-dimensional RREF row-basis matrix has rows `(0,1,0)` and `(0,0,0)`, hence rank one. For its stated yz plane the second row must be `(0,0,1)`. The original page was visually inspected and both ranks independently checked. The current rank lesson does not reproduce the faulty display.
3. **MIT PDF p. 19:** An injective tall matrix requires a pivot in every **column**, not every row. The printed p. 20 construction itself uses the correct rank-n condition. The current lesson already states this correctly.
4. **Oxford PDF p. 50, Proposition 135 proof:** The extending vector is written as belonging to an undefined U minus the current span. It should be chosen in V minus that span. The current lesson uses the actual finite-dimensional domain.
5. **Oxford PDF p. 50, Corollary 137 proof:** Deleting a dependent spanning vector preserves spanning; it need not immediately leave an independent set. For instance, from `{e1,e2,e1+e2,e1+2e2}`, removing the last vector leaves a dependent spanning set. Preserved spanning alone contradicts minimality, so the theorem remains valid without the unnecessary false step. The current lesson's repeated deletion construction is correct.
6. **Stanford slide 3–8:** Lack of a finite basis must not be rephrased as lack of any basis. Infinite-dimensional spaces can have infinite bases. The lesson remains finite-dimensional and does not import the overcompressed parenthesis.
7. **Stanford slide 3–19:** Dimension conservation is interpreted in a kernel-adapted basis. It does not say that each original coordinate is independently retained or deleted. The current lesson's `(1,1)` measurement example makes that distinction correctly.

Additional small Oxford notation slips, such as a k−n versus m−n zero-block label and w labels at the end of the rank–nullity independence proof, do not change the corresponding theorem after dimensions and objects are made explicit. Infinite sequence examples are boundary context, not a claim to teach infinite-dimensional algebra in this chapter.

## Independent exact cross-checks

The Berkeley matrix was transcribed again from the original handwritten first page. Its RREF has pivot columns 1, 3 and 5 and rank 3. Both original kernel directions `(-2,1,0,0,0)` and `(-1,0,-1,1,0)` are annihilated, independent, and span a two-dimensional kernel. These results agree with the current lesson and the handwritten second page.

The main lesson's rank inequalities, finite-field fiber count, rank-one update branch, finite-dimensional one-sided inverse restriction, Schur-complement hypothesis and real-versus-complex Gram distinction were checked against their stated hypotheses. No new error in the main lesson was identified by this bounded source reconciliation. This is not a completion certificate for the bank, simulations, typography or browser behavior.

## Official written references

- David Vogan, MIT 18.700, Fall 2013, [Gaussian Elimination](https://ocw.mit.edu/courses/18-700-linear-algebra-fall-2013/b144082f6883d02faeec26d7f708c63e_MIT18_700F13_gauss.pdf).
- University of Oxford, M1 Linear Algebra I, 2022, Andrew Wathen as course lecturer, [Lecture Notes](https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1). A separate note author is not inferred.
- Stephen Boyd, Stanford EE263, Autumn 2007–08, [Lecture 3: Linear Algebra Review](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg.pdf).
- Alexander Paulin, UC Berkeley Math 54, Spring 2018, [Rank and Nullity](https://math.berkeley.edu/~apaulin/Rank%20and%20Nullity.pdf).

Private source PDFs, extracted text and rendered source images remain outside the repository in the Temp research cache. The companion JSON records exact paths, scopes, hashes and limits. No source files, gates, counts, question banks, or deployed pages were changed by this research task.
