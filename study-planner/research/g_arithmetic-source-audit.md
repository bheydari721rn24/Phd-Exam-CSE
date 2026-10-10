# Arithmetic circuits: written-source selection and reconciliation

## Selection boundary

The search concerns free, public written teaching about fixed-width adders, carry acceleration, subtraction, comparison, BCD correction, carry-save compression, and integer multiplication/division. It does not establish that every course worldwide has been discovered. An inaccessible course cannot be ranked as if its complete notes had been read. Eight university candidates were investigated; four accessible courses supplied the core synthesis. Selection is based on the passages relevant to this chapter, not a universal ranking of universities.

| University / course | Written material actually inspected | Role and reason for selection | Limitation |
| --- | --- | --- | --- |
| MIT, 6.004 Computation Structures, Chris Terman, Spring 2017 | [Arithmetic lecture annotations](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c8/c8s1/), arithmetic paragraphs through the final carry-save/pipeline discussion | Carry-select, hierarchical carry acceleration, signed partial products, hardware reuse and throughput tradeoffs; strongest architectural complement | Read through the web text. The attempted local PDF download failed; no PDF hash is claimed. |
| Stanford, EE108A, Philip Levis, Winter 2008; reader by William J. Dally | [Reader](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf), PDF pages 147–149, 189–218, 229–232; exercises 209–211 reread | Strongest continuous derivation from bit weights to complete datapaths, saturation, population counting, division and group carry | Contains typographical errors and incomplete comparison conditions; corrected below. HDL examples are instructional, not synthesized measurements. |
| Berkeley, CS150, Randy H. Katz, Fall 2000 | [Arithmetic slides](https://people.eecs.berkeley.edu/~randy/Courses/CS150.F00/Lectures/09-Arith.pdf), all nine PDF pages / 51 slides; figures on PDF pages 4 and 7 visually inspected; [HW10/11](https://people.eecs.berkeley.edu/~randy/Courses/CS150.F00/HWs/HW10_11.pdf), all three PDF pages | Detailed CLA, carry-select, ALU polarity, BCD and multiplier diagrams; exercise patterns connect flags to multiword arithmetic | Legacy PDF text has a shifted font encoding. Decoded text was checked against rendered diagrams. Component counts depend on architecture. |
| ETH Zurich, Digital Design and Computer Architecture, Onur Mutlu, Spring 2020 | [Lecture 5 written slides](https://safari.ethz.ch/digitaltechnik/spring2020/lib/exe/fetch.php?media=onur-digitaldesign-2020-lecture5-combinational-logic-ii-afterlecture.pdf), PDF pages 37–66, 71–72, 81–84; diagrams on PDF pages 48–49 and 82–83 visually inspected | Independent full-adder SOP, ripple/CLA block diagrams and comparator Karnaugh-map formulations; useful check on Boolean functions | Some later slides are supplementary material explicitly marked outside delivered lecture coverage. Their written content was read; lecture delivery is not inferred. |

## Candidates investigated but not adopted as read core texts

Cornell CS3410 Spring 2017 and Spring 2011 arithmetic notes timed out. Cornell ECE2300's combinational handout returned HTTP 421. Washington CSE370's attempted adder download returned an HTML page rather than the intended PDF. CMU 18-240's historical index was accessible, but the candidate arithmetic text was not retrieved as a usable complete document. Imperial CO501's attempted written page timed out. These retrieval outcomes are recorded in the download logs. None is counted among the four actually reviewed courses. They may be reconsidered if accessible copies become available.

## Scientific reconciliation

1. An unsigned carry and a signed overflow are different predicates. The signed formula is proved from the two's-complement range and checked independently over every input pair for tested widths.
2. Stanford PDF page 200 uses a subtraction sign as a comparison explanation without the overflow correction. Signed comparison requires the result sign XOR signed overflow; unsigned comparison uses the no-borrow convention. The lesson supplies a counterexample.
3. Stanford PDF page 198's four-bit positive-overflow example contains an inconsistent negative decimal value. Four-bit `0100 + 0100` is the bit pattern `1000`, which represents −8, not −7. Berkeley's slide 15 likewise has an inconsistent decimal overflow annotation. The bit arithmetic governs the correction.
4. Stanford Exercise 10–10 prints saturation bounds with an inconsistent exponent. For an n-bit two's-complement output the bounds are −2^(n−1) and 2^(n−1)−1. These bounds are derived rather than copied.
5. Stanford's group-propagate notation near PDF page 231 is inconsistent with its upper-group indices. This chapter defines inclusive high/low intervals explicitly and uses one associative ordered composition throughout.
6. XOR propagate and OR propagate both give a valid carry equation when paired with AND generate. Only XOR propagate can directly form the sum by XOR with carry. Every formula names the chosen convention.
7. A delay claim requires gate delays, allowed fan-in, loading assumptions and the relevant source arrival time. No lecture's simplified timing model is presented as a measured device delay. Logical snapshots are not event-driven electrical simulation.
8. A carry-save carry row has one-column-higher weight. The local identity is X+Y+Z=S+2C when C is unshifted. A final carry-propagate stage is still required.
9. A BCD correction predicate assumes both input digits are valid. Invalid codes are not silently treated as valid decimal numbers or safe don't-cares.

## Authenticated examination provenance

The original PDF pages 6 and 8 of the 1405 Computer Engineering doctoral booklet were rendered and checked for questions 23 and 31. The source is repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`, path `Exams/Phd/CE/1405/Q707A-phd1405-[www.konkur.in].pdf`, SHA-256 `34d7e4f8f1d347be2ede1be4ff027efc2e17680c3aedf633a13857f27955b75a`. English stems are checked adaptations. Answers and derivations are independent, not an official answer key. Reusing an authenticated bridge from a preceding chapter is identified explicitly and does not create a new unique archive item.

## Reproducible evidence

The local download manifests record original URLs, document lengths and hashes for successful downloads. Reading scopes above describe inspected passages rather than merely listing downloaded files. The lesson and problem solutions are original synthesis; course-inspired problems are reconstructed and labeled, not falsely presented as verbatim university examinations. Unseen examination performance and literal 100% completeness cannot be certified by a finite audit.
