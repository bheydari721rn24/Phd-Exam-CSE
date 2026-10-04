# Logic minimization: source selection and reading audit

## Selection method and bounded pool

Nine university candidates were discovered or screened: MIT, Cambridge, Stanford, Cornell, Columbia, Berkeley, CMU, Michigan and Illinois. Five accessible written courses were actually read. Four primary courses supply complementary foundations; Columbia is necessary as a fifth source for exact cyclic covering and dominance. Comparative scores below are editorial judgments, not objective worldwide rankings. Course dates are explicitly identified, including archived Stanford material. No claim is made that every course worldwide has been read.

## Actual reading and contributions

### MIT — 6.004 Computation Structures, Spring 2017; Chris Terman

Lecture 4 written annotations, slides 1–4 and 10–20 in depth; slides 21–29 screened for implementation context. Primary: specification, SOP, implicants, care sets and hazard coverage. Written access / boundary coverage / semantic depth / exercise value: 5 / 4 / 4 / 3.

[Official written source](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/). Acquisition hashes are recorded in the evidence file.

### Cambridge — Digital Electronics, 2025–26; Ian J. Wassell

Combined slides 21–43 and Examples Paper 1, all three pages; POS slide 34 and exercise page 2 visually checked. Primary: canonical polarity, Gray maps, POS, don’t-cares and tabular simplification. Written access / boundary coverage / semantic depth / exercise value: 5 / 5 / 4 / 5.

[Official written source](https://www.cl.cam.ac.uk/teaching/2526/DigElec/combined_25.pdf). Acquisition hashes are recorded in the evidence file.

### Stanford — EE108A, Winter 2008; Philip Levis; reader author William J. Dally, 2002–2006

Reader Chapter 6, PDF pages 83–105, all text and exercise families read. Primary: cubes, essential primes, nonunique covers, greedy counterexample and delay hazards. Written access / boundary coverage / semantic depth / exercise value: 5 / 5 / 5 / 5.

[Official written source](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf). Acquisition hashes are recorded in the evidence file.

### Cornell — ECE2300 / ENGRD2300, Fall 2026; Christopher Batten

T03 Boolean Algebra, all 26 pages; revision 2026-09-08. Primary: algebra-to-map connection, stepwise grouping and abstraction. Written access / boundary coverage / semantic depth / exercise value: 5 / 4 / 4 / 4.

[Official written source](https://www.csl.cornell.edu/courses/ece2300/handouts/ece2300-T03-bool-algebra.pdf). Acquisition hashes are recorded in the evidence file.

### Columbia — CSEE E6861, 2016; Steven Nowick

Handout 5, Quine–McCluskey, all 15 pages; three exact covering examples. Selected fifth complement: chart dominance, secondary essentials and Petrick’s method. Written access / boundary coverage / semantic depth / exercise value: 5 / 5 / 5 / 5.

[Official written source](https://www.cs.columbia.edu/~cs6861/handouts/quine-mccluskey-handout.pdf). Acquisition hashes are recorded in the evidence file.

## Alternatives and access limits

Berkeley CS150 Spring 1998 lecture outline was screened; its body was not comprehensively read. CMU 18-240 Fall 1996 course index was screened but usable lecture bodies were not retrieved. Michigan EECS270 Spring 2023 homework index was found, but no full lecture body was read. Illinois ECE462 Fall 2020 index exposes QM and Petrick lectures, but bodies were not read because the selected Columbia text provides an explicit exact-cover treatment. These four alternatives are not counted as reviewed courses.

## Reconciliation and corrections

MIT’s “cannot expand any selected term” argument establishes prime status, not global cover optimality. This chapter proves the prime restriction under its stated cost, then solves the chart exactly. Stanford explicitly acknowledges that greedy covering can be nonminimum. The lesson distinguishes irredundancy, prime status, minimum term count and minimum literal count.

Stanford’s prime-number example includes index 1; modern mathematical primality excludes 1. Our prime-detector tasks use 2,3,5,7,11,13. The reader’s “conjunctive (sum-of-products)” figure caption is inconsistent with standard CNF/DNF terminology. The chapter uses canonical DNF for the minterm sum and canonical CNF for the maxterm product. The decimal example refers to three primes while listing four; independent enumeration controls our counts. Stanford’s OR(bit-pattern) maxterm convention differs from ordinary index numbering; the chapter consistently defines M_i as zero at input i.

Columbia places implicants in columns and minterms in rows; Cambridge uses the transpose. Our charts put primes in rows and ON minterms in columns. Dominance is therefore taught by explicit set inclusion, not memorized “delete the dominating row” wording. Cost must be no larger before replacing a candidate. Equal-cost dominance can discard alternative optimal covers; it preserves an optimal value, not necessarily every optimum. Secondary essentials depend on earlier pruning choices and are not necessarily essential in the original chart.

Don’t-care cells are permission to choose outputs under an external input contract. Pure DC cubes may be generated as intermediate QM objects, but do not become required coverage obligations. The hazard treatment is confined to two-level SOP/POS and single-input changes with stable other inputs. It does not promise immunity to all dynamic or multiple-input hazards. Care-set equivalence is weaker than equality on all Boolean rows.

## Questions, figures and archive provenance

All figures and animations are original. Relevant course exercise families—threshold voters, canonical polarity, prime/Fibonacci detectors, BCD, all minimum covers, chart reduction, tabular merging and hazards—are represented by independently worded extensions. The chapter does not republish complete copyrighted course problem sheets or Cornell figures. Source PDFs are cached privately; no originals enter the public artifact.

Three authentic questions are revisited: MSc CS 1405 Q99, PhD CS 1405 Q22, and MSc CE 1405 Q78. Each was checked against its rendered original PDF page at the pinned archive commit. This revisit corrects a prior shortened transcription of Q78 option 4: the original has five products, including both complemented-B/complemented-C and complemented-A/complemented-C. Its extra term violates specified zero row 4. Earlier approved banks are preserved; this chapter records the corrected original explicitly. Q78 is a convention-sensitive tutorial with no unqualified single correct answer. It is excluded from single-answer scoring; the chapter adds an explicitly costed original hazard problem. Answers are independently derived, not official keys. These are revisits, not newly unique archive items.

## Coverage boundary

The chapter covers canonical forms, indexing, cubes, Gray maps through six-variable layout, exact SOP/POS, DC contracts, QM, chart dominance, Petrick, proofs of minimality, hazard-constrained covering and multi-output sharing. Timing claims state a gate-delay model. Technology mapping, large-scale heuristic synthesis, sequential minimization and transistor-level effects are separate topics. Exhaustive small-instance tests and provenance checks support the authored artifact; they cannot certify every possible unseen examination question.
