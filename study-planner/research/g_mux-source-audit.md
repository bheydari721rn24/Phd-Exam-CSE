# Written-source selection and reading audit: g_mux

## Selection boundary

Four core courses from four universities were actually read for the chapter boundary. The comparison uses the documented accessible source pool, with chapter-specific inspection and relevance screening. It is not a worldwide exhaustive search or a ranking of universities. A more recent course is not automatically more useful than a complete older written treatment; the selection prioritizes scope, derivation quality, independent contracts, and accessible exercise patterns.

| Candidate | Actual inspected material / relevance | Decision |
|---|---|---|
| Stanford EE108A, Philip Levis; W. J. Dally reader | PDF 119–146 and 150–162; code conversion, binary and one-hot selection, tree counts, encoders, priority, ROM, PLA/PAL, exercises | Core: broadest written block-design treatment, with explicit corrections |
| MIT 6.004, Chris Terman, Spring 2017 | Lecture 4 written multiplexer, function-lookup and ROM annotations; web-text lines 697–759 | Core: independent function-realization and lookup structure |
| Cambridge Digital Electronics, Ian J. Wassell, 2025–26 | PDF 64–76; three-page Examples Paper 1; source diagrams 66,68,75 rendered | Core: implementation polarity, programmable arrays, bus ownership and threshold exercise pattern |
| ETH Zurich Digital Design and Computer Architecture, Onur Mutlu, Spring 2020 | Lecture 5 PDF 37–43; diagrams 39 and 43 rendered | Core: independent decoder/MUX contract and hierarchy derivation; introductory rather than priority coverage |
| Berkeley CS150, R. H. Katz, Fall 2005, combinational-logic lecture | Cached lecture inspected by chapter-keyword and scope screening; principally Boolean synthesis rather than comprehensive routing/priority treatment | Supplemental candidate, not counted as a reviewed core course |
| Cornell ECE2300, Christopher Batten | Accessible cached combinational-logic material has a MUX primitive passage; chapter scope screened, not a claimed current complete reading | Candidate; current four cover the selected boundary more broadly |
| Carnegie Mellon, University of Washington, Imperial College | Prior candidate acquisition had unavailable, mismatched HTML, or timed-out written artifacts; no usable current chapter text claimed | Excluded from actual-read count; availability is not a scientific ranking |

## Read evidence and exact source hashes

Stanford reader: 232 pages; SHA256 `e1be9e7e4780d5fd8baa4ce7afa7a959e1d50c60d80d6c0fc2f551afd0d617b6`. PDF 127–129 was reread after an output truncation. Relevant decoder/selector/priority diagrams on 130,138,144 were inspected. The ROM organization on 150–154 was read directly during this chapter's work. Exercise patterns are reconstructed with independent solutions rather than copying the entire exercise collection.

Cambridge notes: 190 pages; SHA256 `e4790943453a7562a3f93a51180e4db72819fe48131aca7b5231ac4631c37c2e`. Every page 64–76 was extracted and read; formulas whose complements vanished in extraction were checked in the rendered page 66. The course materials page identifies the 2025–26 course and its notes. The chapter does not claim a reading of all 190 pages.

ETH Lecture 5: 87 pages; SHA256 `3e84c2da3cd6caa79f14f1dacb9b192ca78c8292e5fe3fbcef490d703f849083`. Pages 37–43 were reread, including the 4:1 MUX gate/block exercise. Later arithmetic and sequential material is outside this chapter's source claim.

MIT public annotations were read through the official web page, not downloaded as an authenticated local PDF. No invented file hash or full-course reading claim is made. The lecture's lookup argument is independently derived through Shannon expansion in the lesson.

## Source discrepancies and normalization

- Stanford's prose about arbitrary n-variable lookup occasionally confuses n data inputs with the required 2^n inputs. The lesson states both select and data counts explicitly and proves them.
- Stanford's example treats one as prime. The mathematical prime convention excludes one; that example is not copied as a correct prime lookup.
- Priority suppression requires complemented outranking requests. The reader's HDL and the independent grant proof resolve prose that omits a complement.
- Cambridge page 66 extraction loses overbars. The rendered cofactor example is `(not z, not z, 0, 1)` under selectors x,y, and agrees with the independent eight-row truth table.
- Cambridge page 68's “system 1” sentence does not agree with interpreting x,y,z as the displayed S2,S1,S0 ordering. Our circuit declares MSB-first order and uses equality to assign indices rather than inheriting that ambiguous sentence.
- A PLA product can omit variables, so it need not be a complete minterm. The lesson uses cube terminology and states the PAL architecture assumptions.
- A one-hot OR selector outside its legal domain and tied push-pull drivers are different contracts. No Boolean superposition is used to excuse electrical contention.

## Original-examination evidence

MSc Computer Engineering 1404, booklet 335C, PDF page 19 was newly rendered and inspected. Original PDF SHA256: `909e4efaaad96f4d39e526104bc9dc6de6d52be11fd7716e583476b0e62ff654`; repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. Question 80 has the two cascaded selector topology and NOR choice four. Question 82 has a full adder with carry-in one, an XOR, two inversions, and S1=c/S0=d; its first option is independently verified over all sixteen inputs. Answers are independent derivations, not an official key.

Question 80 is a deliberately revisited archive bridge, not a new unique question. Question 82 is newly checked for this chapter. No uninspected doctoral selector question is invented to satisfy an archive quota. The bank combines these two authentic items with 80 original or clearly named reconstructed patterns, from foundational counterexamples through multi-stage mathematical reasoning.

## Exact references

1. Stanford University — Philip Levis, EE108A Winter 2008; William J. Dally, EE108 Class Notes, Chapters 7–8. [Reader](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf).
2. Massachusetts Institute of Technology — Chris Terman, 6.004 Computation Structures, Spring 2017, Lecture 4. [Written annotations](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/).
3. University of Cambridge — Ian J. Wassell, Digital Electronics, 2025–26. [Materials](https://www.cl.cam.ac.uk/teaching/2526/DigElec/materials.html), [notes](https://www.cl.cam.ac.uk/teaching/2526/DigElec/combined_25.pdf), [Examples Paper 1](https://www.cl.cam.ac.uk/teaching/2526/DigElec/examples_25_1.pdf).
4. ETH Zurich — Onur Mutlu, Digital Design and Computer Architecture, Spring 2020, Lecture 5. [Slides](https://safari.ethz.ch/digitaltechnik/spring2020/lib/exe/fetch.php?media=onur-digitaldesign-2020-lecture5-combinational-logic-ii-afterlecture.pdf).

The references identify actual material used. The audited synthesis remains a review draft until student approval; finite evidence cannot guarantee every unseen examination outcome.
