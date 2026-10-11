# Written-course selection: amortized analysis

## Scope and selection rule

This is a documented, bounded comparison of accessible written courses from eight universities. It is not an enumeration of every course ever taught. A course inventory is not evidence that its lecture was read. Four core courses were selected after reading their entire relevant lectures; a fifth university provides an independent comparison. Video recordings were not used. The chapter is an original synthesis, not a reproduction of the source slides or exercise collections.

| University and course | Instructor | Reading evidence | Selection and contribution |
| --- | --- | --- | --- |
| MIT, 6.046J, Spring 2012, Lecture 11 | Dana Moshkovitz and Bruce Tidor | All nine PDF pages, including the license page, read through official OCW PDF text; native download timed out. Lecture 10 was screened but not counted as fully read. | Core: stack, geometric growth, accounting, expansion and contraction. |
| Carnegie Mellon, 15-451/651, Spring 2024, Lecture 6 | Daniel Anderson and David Woodruff, verified on course homepage | All eleven PDF pages, including four exercise prompts, read through official university PDF text; native connection was refused. | Core: exact cost contracts, initial potential, failed potential guesses, shrink timing. |
| Princeton, COS423, Spring 2013, Amortized Analysis | Kevin Wayne, printed on slide 1 | All 49 native PDF pages read. SHA-256 d8262485a004de4dfe3234097aebaafbc2ed556f615f86468ba15e7f54e05441. | Core: counter, multipop, sparse initialization, aggregate/accounting/potential comparison. |
| Stanford, CS166, Spring 2026, Lecture 9 | Keith Schwarz, verified on archived course homepage | All 79 native condensed slide pages read. SHA-256 8293ac5c51d8dc55e9c7939382b3937e15b173aeacf6ad530d324336b990094c. | Core: two-stack queue, latency versus throughput, dynamic arrays, right-spine B-tree extension. |
| ETH Zurich, Data Structures and Algorithms, Spring 2022, Lecture 8 | Felix Friedrich, verified on course homepage | All 57 native handout pages screened/read, including amortization pages 14–29 and move-to-front pages 34–45. SHA-256 20219690daab13ba36ddbf27277dbffdd4d8dd9e359820e5327159dc5ff324f4. | Additional reviewed comparison: finite-counter endpoints, state-relative potential, competitive analysis. |
| Cambridge, Algorithms 1/2, 2023/24 | Course inventory names Damon Wischik and Frank Stajano | Public inventory screened. A guessed Algorithm2/alg2.pdf URL returned 404. No amortization lecture is counted as read in this chapter. | Candidate for later expansion; not counted toward four-course requirement. |
| Berkeley, CS170 archived inventories | Not attributed without lecture evidence | Public inventories screened; no relevant complete written lecture read in this chapter. | Not counted as a reviewed course. |
| Oxford, Algorithms, 2019/20 | Andreas Galanis, inventory attribution | Public syllabus includes amortised analysis; no complete relevant lecture read. | Not counted as a reviewed course. |

No numerical ranking based on invented scores was used. The four core selections complement one another: MIT covers resizing, CMU exposes proof assumptions, Princeton supplies exact counter/stack development, and Stanford adds queue and tree mechanisms. ETH strengthens endpoint and competitive reasoning. This is an evidence-based choice within the recorded pool, not a claim of globally optimal selection.

## Corrections and harmonization

1. MIT's single POP must not be confused with a linear MULTIPOP. The new-minus-old potential difference is written explicitly rather than copying a repeated new-size term.
2. CMU's initial capacity-one, size-zero potential is minus one for the expression two times size minus capacity; the printed minus-one-half value is inconsistent with that expression. The chapter uses a nonnegative clipped potential for insert-only tables.
3. CMU tests quarter occupancy before removal. This chapter's main algorithm tests after removal. Both are legitimate policies, but their states and exact charges differ. They are not mixed in one proof.
4. Princeton's insert-only page 39 labels a copying-only model, while subsequent pages also charge the new-element write. This chapter distinguishes those models. Its exact growth sum stops strictly before the final element count; an unused power of two is not included.
5. Princeton's multipop removes exactly the requested number only when enough records exist; this chapter uses a bounded removal contract and counts call overhead explicitly when requested.
6. Princeton's sparse-initialization technique is a word-RAM technique. Uninitialized C/C++ values cannot be read portably merely because the mathematical model permits arbitrary machine words.
7. Stanford slide 45 says the amortized charges never overestimate work, whereas the displayed inequality makes them an upper bound that must not underestimate total work. The chapter uses the displayed inequality with the correct wording.
8. Stanford slide 75 names the number of right-spine nodes, but its argument counts keys moved off that spine. The chapter gives a charging argument instead of equating unspecified big-O and Theta terms. Variable branching factor, pointer traversal, and allocation must be accounted for.
9. ETH's finite counter stops before overflow in its example. At an actual modulo wrap, no zero bit becomes one. The wrap charge is zero in the bit-flip model, and the exact finite-width sum differs from an unbounded counter.
10. All sources are reconciled using explicit cost units, initial state, legal operations, resize timing and endpoint potential. Expected collision costs are separated from deterministic rebuilding costs.

## References

- MIT. Dana Moshkovitz and Bruce Tidor. 6.046J Design and Analysis of Algorithms, Spring 2012, Lecture 11. https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/83b82d45beb3776da72b7f3e1b3f42df_MIT6_046JS12_lec11.pdf
- Carnegie Mellon University. Daniel Anderson and David Woodruff. 15-451/651 Algorithm Design and Analysis, Spring 2024, Lecture 6. https://www.cs.cmu.edu/~15451-s24/lectures/lecture06-amortized.pdf
- Princeton University. Kevin Wayne. COS423, Spring 2013, Amortized Analysis. https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/AmortizedAnalysis.pdf
- Stanford University. Keith Schwarz. CS166 Advanced Data Structures, Spring 2026, Lecture 9. https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/09/Condensed%20Slides.pdf
- ETH Zurich. Felix Friedrich. Data Structures and Algorithms, Spring 2022, Lecture 8, English handout. https://lec.inf.ethz.ch/DA/2022/slides/daLecture8.en.handout.pdf
