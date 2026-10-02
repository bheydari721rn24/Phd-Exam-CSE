# g_number source selection and coverage audit

Date: 2026-10-02. Topic: Number Bases and Binary Encoding, Logic Circuits Chapter 1.

## Selection boundary and evidence standard

Eight named university offerings/resource families were screened. Six supplied actually read written instructional material; four form the complementary core, and two are supplements. This is a bounded accessible-source comparison. It does not mean that every worldwide course or every lecture within a selected offering was read. A catalogue entry, search snippet, video, or unavailable note does not count as a substantive written course reading. No video is required. Archived Iranian MSc/PhD papers were neither read nor used.

Selection order: in-scope written coverage, mathematical explanations, assumption clarity, useful instructional questions, and marginal coverage beyond already chosen courses. A university's prestige alone is not a selection criterion.

## Candidate evaluation

| Candidate | Review actually performed | Decision and reason |
|---|---|---|
| MIT 6.004 Spring 2017, Chris Terman | Chapter 1 annotated written instruction: fixed-length codes, binary/hex, signed integers, complement, Hamming distance, parity and bounded correction; worksheet landing page screened only | Core: strongest bridge from representation to capacity and code reliability. Entropy and Huffman sections were screened for scope but are not claimed as taught exhaustively. |
| Berkeley CS61C living teaching-team notes | Written bodies of Binary, Decimal, Hex and Integer Representations, including explanations and quick checks | Core: the most useful accessible comparison of unsigned, sign-magnitude, ones' complement, two's complement and bias. Correct the incomplete ones' complement addition description. |
| Stanford CS107 Winter 2020, Jerry Cain and Lisa Yan | Lecture 2 PDF pages 8–50, 53–84, 109–114; representation, base conversion, negation, range, extension and truncation | Core: progressive conversion and boundary examples. Machine-size tables and signed narrowing shortcuts must be qualified. |
| Cornell CS3410 Fall 2024, Adrian Sampson and Giulia Guidi | Official Switches and Numbers written teaching body; Real Numbers in Binary and Fixed-Point Numbers sections of Floating Point | Core: exact conversion procedures and fixed-point scale metadata. Read via browser because local TLS trust failed; no successful local hash is invented. |
| CMU 15-213/14-513/15-513 Spring 2025 teaching team | January 16 PDF pages 7–10, 19, 21–35 and 39–64; modular arithmetic, width conversion, multiplication and shift rounding | Selected supplement: useful intermediate-width and negative-rounding coverage beyond the core. Excluded byte-order pages and machine-specific C assumptions from this chapter. |
| Princeton Algorithms, Sedgewick and Wayne | Combinatorial Search PDF pages 35–37 visually inspected: reflection, enumeration and encoder applications | Selected supplement: adds the Gray construction and practical adjacency perspective. Local text extraction was corrupt, so original images were used; no false clean-extraction claim. |
| Cambridge Digital Electronics 2020–21, Ian Wassell | Official materials index screened; gate/Boolean, minimization, adders and sequential lecture boundaries | Not selected for this chapter: accessible index emphasizes later gate/sequential instruction; no substantive lecture-body reading is counted here. Useful candidate for later chapters. |
| ETH Zurich Digital Circuits | Official course catalogue and notes URL screened; direct notes landing access returned HTTP 403 | Not selected: teaching body not accessible in this run. Catalogue descriptions do not count as actual reading. |

Four cores are selected for complementary roles, not a claim that they outrank every course universally. Supplements are included because arithmetic edge cases and Gray adjacency add real material. Six sources are not treated as six fully read complete courses.

## Exact primary URLs and reading record

- MIT annotated instruction: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s1/ . Author and offering verified on the primary page. Worksheet landing: https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s3/ ; linked worksheet not counted as read.
- Berkeley radix: https://notes.cs61c.org/content/number-rep/binary-decimal-hex/ . Integer representations: https://notes.cs61c.org/content/number-rep/integer-representations/ . Living notes attributed to the course teaching team, without inventing a sole author or edition year.
- Stanford: https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/lectures/2/Lecture2.pdf . Local cached original, 115 PDF pages; specified sections read in the current turn. Title slide credits Jerry Cain and Lisa Yan and acknowledges prior contributors.
- Cornell: https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/numbers.html and https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/float.html . Offering overview https://www.cs.cornell.edu/courses/cs3410/2024fa/ identifies Sampson and Guidi. Local downloads refused by certificate verification; primary web text was read. No certificate bypass used.
- CMU: https://www.cs.cmu.edu/afs/cs/academic/class/15213-s25/www/lectures/02-bits-bytes-ints.pdf . Local original fetched successfully, 69 PDF pages. Page numbering is PDF-page numbering where printed slide numbers differ; course-team attribution used because sole slide author was not verified.
- Princeton: https://algs4.cs.princeton.edu/lectures/keynote/67CombinatorialSearch.pdf . Three relevant pages rendered and visually read; Gray construction, Java subset-transition pattern, encoder/Hanoi/ring applications. Year not inferred from search crawl metadata.
- Cambridge index: https://www.cl.cam.ac.uk/teaching/2021/DigElec/materials.html . Index only.
- ETH notes URL: https://iis-students.ee.ethz.ch/lectures/digital-circuits/ . HTTP 403.

Source-byte hashes and access results are stored in `g_number-source-manifest.json`. University files remain reference originals in a temporary source cache and are not republished wholesale.

The cached primary WG14 N1570 C11 committee draft (https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), §§6.5 paragraph 5 and 6.5.7, was checked for retained C17 expression and shift rules. It is an additional specification reference, not a seventh university course and not mislabeled as the published C17 standard.

## Reconciliation decisions that matter scientifically

1. Berkeley's ones' complement example without final carry is valid but insufficient to describe general addition. The manuscript derives end-around carry modulo 2^n-1 and supplies a carry example and range caveat.
2. Leading-one zero in sign-magnitude or ones' complement is numerical zero, not a strictly negative integer. Counts and decoder wording account for the two representations of zero.
3. Cornell and Stanford shorthand that ordinary binary addition always gives the correct signed answer is restricted to the residue, with exact signed range checked independently.
4. Stanford complement-plus-one negation of the minimum produces the same word; the exact positive opposite is not representable. The exception is proved, not omitted.
5. Stanford/CMU numeric conversion claims assume a platform. The manuscript gives abstract extension/truncation contracts and separates C17 signed narrowing, promotions, signed overflow and negative shifts. A word model is not compiler execution.
6. CMU's E9 + D5 displayed unsigned decimal values contain an inconsistent 223 label; E9 is 233. That data was not copied; the chapter uses independently checked examples.
7. CMU's signed/unsigned adder equivalence applies at the bit level. An overflowing C17 signed expression does not acquire defined modular semantics from the diagram.
8. Cornell's general statement that float behaves identically on all hardware/languages is not adopted. Fixed-point sections are used; full declared IEEE format instruction is deferred.
9. Gray adjacency is proved for the declared reflected cycle, and explicitly distinguished from error-detecting distance and from physical synchronization guarantees.
10. BCD correction, excess-three, the declared Aiken table, exact rational termination, Hamming construction and SECDED boundaries are independently derived extensions. They are not falsely presented as content found in all four core courses.

## Coverage matrix

| Chapter section | Required microtopics | Course contribution / original work |
|---|---|---|
| Positional notation | legal digits, weights, uniqueness, capacity, inclusive intervals, zero digit count, interpretation versus bits | MIT/Berkeley/Stanford/Cornell; original uniqueness and format contrast |
| Integer conversion | Horner invariant, division invariant/termination, internal zeros, power-of-two grouping, fractional padding, unknown bases | Berkeley/Stanford/Cornell; original proofs and constraints |
| Rational fractions | multiplication invariant, termination iff denominator divides radix power, shortest length, repeating remainder cycle, prefix/block formula, dual expansions, rounding error | Cornell foundation; original exact derivations and examples |
| Signed forms | unsigned, sign-magnitude, ones' complement, two's complement, bias, ranges, zero count, negation exception, radix complements | Four cores plus CMU; original modular reconciliation |
| Arithmetic | exact/residue, carry, signed addition/subtraction overflow, carry XOR proof, no-borrow convention, minimum subtraction, product width/overflow, division and signed comparisons | MIT/Stanford/CMU; original proofs and boundary distinctions |
| Widths/shifts | widening in all signed encodings, narrowing criterion using retained sign, widening order, logical/arithmetic shifts, floor versus truncation, rotate/language boundaries | Stanford/CMU; original sign-magnitude contrast and exact-width checks |
| Fixed point | full format declaration, range/resolution, encoding, ties, clipping, negative quantization, scale alignment, product rescaling, intermediate range, propagated errors | Cornell scale model; independently derived accuracy and arithmetic |
| Decimal codes | 8421 legal nibbles/capacity, add-six proof with both carry cases, multi-digit carries, excess-three, Aiken table/weight ambiguity, nines/tens complements | MIT BCD capacity; original declared tables, proofs, problems |
| Gray | reflection/bijection, encode/decode XOR, adjacency and wrap proofs, encoder/skipped position limits, arithmetic, minimum-distance distinction | Princeton supplement; original conversion/adjacency derivations |
| Error control | distance, detection/correction iff bounds, parity odd/even errors, Hamming (7,4), syndrome ordering, miscorrection, SECDED assumptions, parity-bit count | MIT distance foundation; original complete Hamming construction and finite code checks |
| Problems/review | 36 complete solutions, course-pattern labels, 60 complete-sentence rules, eight-step method, clear coverage limitations | Independently written teaching and problems |

## Exercise boundary and attribution

Read lecture checks and worked-example patterns were screened for relevance. Problems 1–2 and 13 use Stanford representation/negation patterns; 2 uses Cornell conversion; 5 uses MIT capacity; 11 uses Berkeley decoder comparison; 20 uses Stanford/CMU widths; 23 uses CMU shift rounding; 31 uses Princeton Gray instruction; 33 uses MIT distance/parity. Wording, data and solutions are independent. No claim is made that every exercise in every entire course is reproduced, and no deferred archived Iranian question is included. Course exercises in later circuits, compression, Java algorithms or C applications are not silently counted as taught here.

## Explicit scope limits

IEEE formats, character encodings and endianness belong to the later programming representation chapter; gate-level arithmetic/code-converter design and sequential counters belong to their logic chapters; Huffman compression and full coding theory are beyond this numerical chapter. The finite checks recorded separately are evidence about specified models and cases, not proof of universal examination performance.
