# Divisibility and number theory: source selection and reading audit

Review date: 2026-10-02. Chapter: d_number, Discrete Mathematics Chapter 8, Week 2. This is a documented bounded comparison of eight university-course candidates. Selection is based on this chapter's mathematical coverage, proof clarity, explicit assumptions, algorithm derivations, and usable written materials. It does not assert that all worldwide courses were discovered or that this ranking is globally optimal.

## Candidate-by-candidate comparison

| Candidate and instructor | Actual review level | Chapter-specific strengths and limitations | Decision |
| --- | --- | --- | --- |
| MIT 6.042J, Mathematics for Computer Science, Spring 2015; Lehman, Leighton, Meyer textbook | Genuinely read PDF pages 253–260 and 272–282 of the official 2015 text: divisibility, signed remainders, jug invariant, gcd, extended-Euclid setup, congruence, remainder arithmetic, inverse and cancellation proofs | Clear exact certificates and proof dependencies. Historical narrative and historical computational assertions are outside the synthesis. Gcd zero-pair convention requires an explicit extension. | Principal course: mathematical and algorithmic spine. |
| UC Berkeley CS 70, Spring 2022; Satish Rao, Koushik Sen | Genuinely read Note 6 pages 1–11, including every algorithm and exercise statement; Note 7 pages 2 and 4 specifically for RSA's algebra and CRT proof | Strong extended-Euclid derivation, modular-power correctness exercise, and CRT coordinate interpretation. Note 6's bare exponent-zero return is normalized for modulus one. Security and implementation recommendations are not adopted. | Principal course: algorithms and coordinate reasoning. |
| CMU MFCS 15-151, Fall 2022; Klaus Sutner | Genuinely read all 72 modular-arithmetic slides, with the extracted middle pages read again to avoid truncation; original cancellation page visually inspected | Broadest compact coverage: valuations, divisor lattice, exact fiber counts, Wilson, additive rotations, and generalized CRT. Slides sometimes state results or leave proofs as exercises; the new chapter supplies its own proofs. | Principal course: advanced boundaries and applications. |
| Cambridge Part IA Discrete Mathematics, 2022–23; Marcelo Fiore | Genuinely read PDF pages 123–143 and 151–182, including modular tables, inverse/linear-combination equivalence, common-divisor characterization, Euclid, and coefficient tracing | Most explicit domain and algebraic-structure distinctions. Some proof slides are intentionally blank for classroom completion. The new chapter fills these with independent proofs and handles signed/zero inputs beyond positive-input code. | Principal course: domains, structures, proof completeness. |
| Oxford Discrete Mathematics; Andrew D. Ker notes and 2024–25 course syllabus | Syllabus and official note availability screened; the new chapter's number-theory passages were not fully read from this course | Very strong curricular fit: gcd, CRT, Fermat/Euler, arithmetic functions. It remains a viable future supplementary source. Previously cached notes are not counted as a fresh complete number-theory review. | Unselected candidate; not counted toward four. |
| Cornell CS 2800, Spring 2017 / Fall 2015 | Official lecture descriptions and accessible modular-number explanations screened, including quotient versus congruence and well-defined operations | Useful conceptual perspective, but a full chain through generalized CRT and prime-power boundaries was not established in this screening. Course pages use MIT MCS readings, so they are not treated as independent full textbook coverage. | Unselected candidate; not counted toward four. |
| Stanford CS 103, Spring 2017 | Official problem-set modular-arithmetic entry and course description screened | Strong foundational proof course; a standalone full written number-theory progression was not verified in this comparison. No lecture-completeness claim is made. | Unselected candidate; not counted toward four. |
| ETH Zurich Number Theory I, Fall 2024; Emmanuel Kowalski | Official lecture-note introduction and stated course scope screened | Rich algebraic and analytic course, broader and more advanced than the bounded discrete-mathematics chapter. The complete notes were not read. | Unselected candidate; not counted toward four. |

The four principal courses cover complementary requirements. Four is the minimum, not a ceiling. Additional primary courses should be reviewed if a documented gap or future student question requires them. A candidate page is not promoted to “read” merely because a PDF download exists.

## Reconciliation and independent additions

1. Mathematical remainder uses a positive modulus and a nonnegative interval, even for a negative dividend. Language-dependent signed remainders are kept separate.
2. The greatest positive numerical gcd definition fails at two zeros; the chapter explicitly introduces the computational/divisibility-order convention.
3. Cambridge positive-input Euclid is extended to signed and zero inputs in the independently authored code; its proof follows exact coefficient identities.
4. CMU's cancellation rule is proved by dividing the modulus by the gcd; the original-modulus fiber count is retained rather than silently discarding solutions.
5. Berkeley modular exponentiation is made canonical at exponent zero and modulus one. Loop iterations, arithmetic operations, and bit costs are distinguished.
6. CMU's generalized CRT statement receives a full two-modulus construction and a prime-power proof of pairwise sufficiency for many moduli.
7. Euler reduction is restricted to units. Prime-power valuations, transient power tails, and safe nested-exponent reasoning are taught independently with boundary counterexamples.
8. RSA correctness is proved separately for zero and nonzero coordinates at each prime; no security guarantee or outdated parameter advice is inferred from the course example.
9. The coin threshold, divisor count/sum derivations, factorial valuations, and additional quadratic boundary problems are original elementary extensions supported by the established divisibility/CRT machinery; they are not described as quotations from the reviewed course passages.

## Selected course exercise ledger

| Actual read source | New worked problem | Adaptation and full solution |
| --- | --- | --- |
| Berkeley Note 6 p. 8: inverse exercise for twelve modulo thirty-five | Problem 4 | Independently worded problem and explicit quotient/substitution certificate. |
| Berkeley Note 6 p. 3: prove modular exponentiation | Problem 27 | Iterative invariant proof, exact exponent-thirteen counts, and corrected modulus-one boundary. |
| CMU valuation and divisor-lattice exercises, slides 15–19 | Problem 9 | Different numeric inputs, complete factor-coordinate reasoning and common-divisor list. |
| CMU cancellation exercise, slide 38 | Problem 11 | Explicit many-solution example; complete reduced-modulus derivation. |
| CMU generalized CRT, slide 69 | Problem 16 | New overlapping moduli; constructive compatibility proof and correct lcm period. |
| CMU polynomial parity demonstration, slides 21–24 | Problem 34 | Generalized to any finite integer-coefficient degree; counterexample over rationals. |
| CMU Wilson theorem, slide 48 | Problem 36 | Independent proof completion and converse comparison. |
| CMU rotation exercise, slides 56–59 | Problem 37 | New step/modulus pair, all cycles enumerated and completeness proved. |
| Berkeley Note 7 p. 4: CRT proof of RSA recovery | Problem 38 | Original nonunit message showing why a direct Euler proof is insufficient. |

The remaining worked questions are labeled original and synthesize the chapter's methods. The bank is deliberately broad but does not reproduce every problem in any course's entire exercise collection. MIT and Cambridge contribute the actual lesson derivations and domain checks even when a question is an original application.

## Primary links

- [MIT 2015 official course readings](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/pages/readings/).
- [Berkeley course and instructors](https://www.sp22.eecs70.org/), [Note 6](https://www.sp22.eecs70.org/assets/pdf/notes/n6.pdf), [Note 7](https://www.sp22.eecs70.org/assets/pdf/notes/n7.pdf).
- [CMU MFCS course listing](https://www.cs.cmu.edu/~sutner/mfcs.html), [modular slides](https://www.cs.cmu.edu/~sutner/pdf/60-modari.pdf).
- [Cambridge course materials](https://www.cl.cam.ac.uk/teaching/2223/DiscMath/materials.html), [written notes](https://www.cl.cam.ac.uk/teaching/2223/DiscMath/DiscMathProofsNumbersSetsNotes.pdf).
- [Oxford course syllabus](https://www.cs.ox.ac.uk/teaching/courses/2024-2025/discretemaths/index.html), [Ker notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf).
- [Cornell GCD and modular numbers](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec31-gcd.html), [modular operations](https://www.cs.cornell.edu/courses/cs2800/2015fa/lectures/lec25-modular.html).
- [Stanford problem-set entry](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/handouts/100%20Problem%20Set%201.pdf).
- [ETH Number Theory I notes](https://people.math.ethz.ch/~kowalski/number-theory.pdf).

Reference PDFs remain in temporary reference storage. Their downloaded metadata and hashes are recorded separately; the published lesson is newly authored prose and original figures. No archived Iranian examination PDF was opened, mined, classified, or solved. Literal zero-error guarantees and exhaustive worldwide coverage cannot be certified; identified mathematical and presentation errors are corrected before delivery and the residual boundaries remain explicit.
