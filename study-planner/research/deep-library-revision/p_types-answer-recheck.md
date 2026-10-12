# Independent recheck of the generated p_types answers

Date: 12 October 2026. Scope: `research/write_types_answers.py` and all 45 sections of `research/deep-library-revision/p_types-solutions.md`. The generated manuscript already existed, so the writer was not rerun against the filesystem. Its AST was executed after removing only the output write and print calls; the reconstructed string exactly matched the existing manuscript. No shared source or generated answer file was edited.

Reviewed manuscript SHA-256, computed from its UTF-8 text with normalized reading newlines: `4e858c5f44b03f70f49694c43506756a20785c9162d8f7cc65f2d599577e63e2`.

The entire 79,422-character manuscript was read in four nontruncated ranges: 0–20,000, 20,000–40,000, 40,000–60,000 and the remainder. References to line numbers below identify the reviewed snapshot, not a claim that later regenerated versions retain the same lines.

## Correction 1: Q1 names the wrong option for unsigned carry

**Location:** generated Q1, line 18; writer string `A[1]`.

Current sentence:

> Unsigned carry and signed overflow answer different questions: option 1 has an unsigned carry although its signed result is valid; option 2 can overflow neither interpretation.

The first part is numerically wrong. Option 1's four-bit operands are `0101` and `1000`: unsigned 5+8=13, below16. It has no unsigned carry. Option 3's operands are `0100` and `1110`: unsigned 4+14=18=16+2, so it does have a carry, while the signed interpretation is 4+(-2)=2 and does not overflow. The solution table's signed calculations are already correct.

**Exact replacement:**

> Unsigned carry and signed overflow answer different questions: option 3 has an unsigned carry although its signed result is valid; option 2 has neither unsigned carry nor signed overflow.

This correction does not change the correct answer, option4.

## Correction 2: Q20–23 must classify negation after integer promotion

**Location:** shared writer family starting at20; generated lines401,419,437,455 in the reviewed snapshot.

Current passage:

> In a signed C arithmetic type of this stated width, that negation is undefined, not a guarantee that the value stays negative.

The representation endpoint proof is correct, but this language-level statement can conflate the stored source type with the type in which unary minus evaluates. In particular, an eight-bit signed source with value -128 promotes to the declared int32 before unary minus. Its negation is int128 and is defined. Only a subsequent conversion back into an eight-bit signed destination raises the separate out-of-range signed-integer conversion question. Two's-complement object representation does not itself mandate the result of that C17 conversion; the implementation supplies the documented result or signal.

By contrast, `-INT_MIN` has int operands after promotion and its mathematical result is not representable in int, so that negation is undefined. A sufficiently wide type cast **before** the operation can make the negation valid; casting after an already overflowing operation cannot repair it.

**Replace the current paragraph beginning “Negating the minimum...” with:**

> Negating the representation minimum has mathematical result 2^(n−1), which exceeds that representation's positive endpoint. In C, first determine the type after integer promotion. If unary minus evaluates in a signed type whose minimum is this value, as in `-INT_MIN`, the unrepresentable result gives undefined behavior. A narrow signed source may instead promote to a wider int: with an eight-bit two's-complement signed char having range[-128,127] and the declared int32 model, `signed char s=-128;` followed by `-s` yields the defined int value128. Converting that result back to an eight-bit signed type is a separate out-of-range signed conversion with implementation-defined handling, not the same operation as signed arithmetic overflow. A sufficiently wide cast before negation can change the arithmetic domain; a cast after an operation that already overflowed cannot repair it. The two's-complement premise establishes the representation endpoints but does not eliminate promotion or conversion rules.

Apply this one shared-proof repair to all four generated answers. Their existing range formulas and correct options remain unchanged.

Rule pointers for this correction are integer promotion in6.3.1.1, signed-destination conversion in6.3.1.3 and unrepresentable evaluated results in6.5, as freshly consulted in the official [WG14 N1570 C11 committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf). This source is not the published C17 standard.

## Results of the remaining checks

No further concrete mathematical or C-semantics error was identified in the remaining answers. In particular:

- Q4 and Q44 correctly promote narrow unsigned objects before complement and distinguish their later destination residues.
- Q6 and Q45 correctly separate conditional common typing from selected-branch evaluation and later comparison conversions.
- Q8's signed-addition guard is evaluated before addition and is representable under the stated sign conditions.
- Q9's binary64 midpoint and the a+3 extension use the correct significand parity and explicitly exclude excess intermediate precision.
- Q24–27 now explicitly state the minimum-layout policy needed for their sizes and calculate both internal and extension-example tail padding correctly.
- Q28–31 preserve the pointed-to row type after parameter adjustment, while separately labeling the eight-byte-pointer ABI used in the example.
- Q32–35's quotient/remainder ceiling expression avoids adding7 at a near-maximum unsigned value; the final quotient increment fits. Narrow-source promotion does not invalidate this safe formula.
- Q40–43 use truncation toward zero, remainder−1 and the correct positive int32 parameter endpoint715827882; both minimum/-1 and minimum%-1 are classified undefined.
- No actual shift expression appears in the generated 45 answers. Mathematical powers of two in the representation proofs are not C shift expressions and must not later be translated blindly into `1 << width` by a simulator.

The answer keys need no numerical changes. The two concrete corrections above should be applied in the writer and the manuscript regenerated before this answer-level audit is considered closed. The report does not verify browser rendering or claim infallibility of the complete chapter.
