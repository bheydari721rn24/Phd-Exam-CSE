## 14. Connected summary and sixty examination rules

### The chapter in five connected ideas

A gate implements a Boolean function only within a physical contract. The settled truth table defines the final output, while voltage thresholds and delay bounds define when that output is valid. Positive and negative logic describe interpretations of the same voltage behavior. Active-low names describe assertion conventions and must be translated into explicit complements before deriving an equation.

A circuit is easier to reason about as a named, directed graph than as an unlabeled picture. Local equations preserve bubbles and complement scope. Topological substitution proves the function of an acyclic circuit. Sharing a result changes physical gate count and loading without necessarily changing the expanded Boolean formula. Loops, multiple drivers, and floating nodes require additional analysis rather than an invented Boolean operation.

Restricted-library mapping rests on constructive identities and resource assumptions. NAND and NOR are complete because each can construct NOT, AND, and OR. Other libraries can be ruled out by monotonicity, affineness, or preservation of a corner input. Constant-one availability changes the XOR/AND completeness result. A gate-count construction provides an upper bound; claiming a minimum requires a lower-bound proof for the exact permitted library.

Static complementary CMOS connects switch conduction to function. Series and parallel networks implement AND and OR conduction conditions. The output is the complement of pulldown conduction, and pullup must conduct exactly when pulldown does not. This gives NAND, NOR, AOI, and OAI topologies and explains the polarity restriction of a single stage using uncomplemented controls. Real capacitance, finite drive, and leakage remain beyond a pure truth table.

Timing and hazards are properties of an implementation and an input trajectory. Maximum path bounds describe safe settling; minimum path bounds describe earliest possible disturbance. Reconvergence can produce a transient even when endpoints have the same Boolean output. Consensus terms can bridge single-input transitions under a two-level hazard model. Simultaneous-input functional hazards, arbitrary multilevel changes, and analog effects need stronger specifications than static algebraic equivalence.

### Rules 1–10: semantics and signal interpretation

1. Read a gate's entire truth table before identifying its function; several functions agree on the all-zero row.
2. Apply an input bubble before the gate operation and an output bubble after it, keeping parentheses around every complemented compound expression.
3. Treat an n-input NAND as one complemented n-input AND, not as repeated binary NAND.
4. Treat an n-input NOR as one complemented n-input OR, not as repeated binary NOR.
5. An n-input XOR computes odd parity; it is an exactly-one detector only when there are two inputs.
6. A standard n-input XNOR computes even parity, whereas a binary XNOR tree with odd n computes odd parity.
7. Tying both NAND or NOR inputs to the same signal makes an inverter; tying both XOR inputs makes zero.
8. Zero controls AND and one controls OR; their opposite values are neutral, so use these facts before expanding a full equation.
9. A floating input is not a permitted substitute for a tied constant, and high impedance is not a Boolean zero.
10. Translate active-low assertion predicates explicitly; an electrical AND can implement an OR of active-low asserted events.

### Rules 11–20: graph reading and polarity

11. A wire branch copies one signal to several receivers and does not compute an OR or duplicate a gate.
12. Follow the stated crossing-dot convention; a wrong connection changes the function before any algebra begins.
13. Write one equation per named internal net, then substitute in topological order to avoid losing nested complements.
14. An acyclic composition of combinational gates is combinational; the proof is induction over the graph order.
15. Do not apply the acyclic arrival-time algorithm to a feedback loop without an additional state or equilibrium model.
16. A primary input that appears in an internal gate may still cancel from the final function; test semantic support after simplification.
17. A bubble pushed across an AND/OR changes the gate type and complements every input, not just one selected pin.
18. Redrawing a gate with its De Morgan-equivalent symbol does not add a physical inverter or delay.
19. Canceling complements on one branch does not authorize changing the signal level on every branch of a shared net.
20. Two ordinary push-pull outputs tied together do not implement a Boolean OR; their differing levels can create electrical contention.

### Rules 21–30: completeness and mapping

21. To prove a library complete, construct NOT, AND, and OR and explain whether constant outputs can also be generated.
22. NAND alone and NOR alone are complete under ordinary tied-input and fanout permissions; write the constructive identities rather than relying on the word “universal.”
23. AND and OR preserve monotonicity under composition, so neither adding more stages nor adding constants gives them a NOT operation.
24. XOR, NOT, and constants preserve affineness and cannot create the product term of AND.
25. XOR and AND without an external one preserve the all-zero vector and therefore are not a complete library.
26. Adding constant one to XOR and AND enables NOT, changing the completeness conclusion.
27. Of the sixteen binary gates, only NAND and NOR are single-gate universal bases without external constants under the stated standard composition rules.
28. A NAND-NAND SOP or NOR-NOR POS mapping must include unavailable literal complements, output polarity, and single-term exceptions in its cost.
29. A textbook “two-level” label may exclude input inversions; a physical delay sum includes every traversed cell.
30. Replacing a large NAND/NOR by binary gates requires intermediate polarity recovery; a naive chain is generally a different function.

### Rules 31–40: cost and CMOS

31. Count a shared subexpression as one gate instance even when its expression is written in several places.
32. Count physical input pins separately from distinct logical variables; a tied-input inverter loads two pins.
33. Equal gate count does not imply equal depth, equal load, or equal delay.
34. A factored expression can save area while adding levels; compare a common cost model before calling either implementation better.
35. A presented gate construction proves a cost upper bound; a minimum claim also needs an argument excluding all cheaper permitted circuits.
36. In static complementary CMOS, the output is the complement of the pulldown conduction predicate, not the predicate itself.
37. Complementary pullup and pulldown must cover every stable input exactly once; both-on is contention and both-off is floating.
38. To dualize a series-parallel pulldown, swap series and parallel recursively and replace each nMOS with a same-control pMOS.
39. The one-stage inverting restriction assumes uncomplemented control signals and the stated static topology; do not generalize it to all CMOS implementations.
40. Static CMOS has no ideal settled supply path through complementary switches, but real leakage and switching currents prevent a literal zero-power claim.

### Rules 41–50: timing

41. Propagation delay is a latest-validity bound; contamination delay is an earliest-disturbance bound.
42. When no contamination bound is given, use zero for a conservative early-change assumption.
43. The interval between contamination and propagation bounds need not contain just one clean output transition.
44. Sum upper delay bounds along paths and take the maximum for a structural settling budget.
45. Sum lower delay bounds and take the minimum for a conservative earliest possible output disturbance.
46. Include primary-input arrival times; a later input change can determine the final output settling time.
47. Use output-falling delay after a rising input at an inverter, and output-rising delay after a falling input.
48. A longest structural path may be unsensitizable under a particular side-input assignment; a conservative bound is not a promised observed transition.
49. A fixed transport model preserves a pulse's width while translating its edges; an inertial model requires an explicit rejection rule.
50. RC ln 2 is a midpoint estimate in a lumped first-order model, not a characterized worst-case delay for every gate.

### Rules 51–60: hazards, verification, and implementation

51. Equal stable endpoint outputs do not prove a transition has no glitch; analyze the intermediate event times.
52. A static-one hazard falls briefly from a required one, and a static-zero hazard rises briefly from a required zero.
53. A dynamic hazard makes multiple output transitions when the settled trajectory requires one.
54. An SOP consensus product can hold the output high during a bridged single-input transition while preserving the stable function.
55. The dual POS consensus sum can hold the output low under its corresponding stable side inputs.
56. Standard adjacency-cover hazard protection assumes one changing primary input, settled other inputs, and a suitable two-level gate model.
57. Covering one transition does not prove every remapped multilevel circuit hazard-free; inspect the actual implementation.
58. Multiple-input functional hazards can pass through input vectors whose correct Boolean outputs differ from the endpoints; static algebra cannot erase those required responses.
59. For a stuck-at test, first force the correct internal value opposite to the fault, then remove side-input values that mask the difference at an output.
60. Exhaustive Boolean verification establishes the tested stable truth table; timing, physical compatibility, and synthesis preservation of hazard terms remain separate checks.

### An eight-step procedure for a difficult circuit question

1. State the available gate library, constants, tied-input permission, output polarity, signal conventions, and timing model.
2. Name every net and identify its unique driver, branches, and gate input bubbles.
3. Derive the exact local equations and combine them before making any simplifying assumption.
4. Verify the stable function against its specification, using truth tables, cofactors, or a proved identity.
5. Construct the required gate mapping with explicit polarity recovery and all unavailable literal inversions.
6. Count gates, input pins, depth, and transistor assumptions separately; prove a lower bound if minimum cost is requested.
7. Propagate early and late arrival bounds, then inspect sensitization and reconvergent transition paths when relevant.
8. Give the final answer with its boundary conditions, identify a counterexample to each rejected shortcut, and distinguish a guaranteed result from a modeled estimate.

## 15. References and chapter boundary

1. **Massachusetts Institute of Technology.** Chris Terman, *6.004 Computation Structures*, Spring 2017. [Chapter 3: CMOS, annotated teaching text](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c3/c3s1/). Reviewed sections: complementary switch networks, static gates, timing bounds, and lenient behavior.
2. **University of Cambridge.** Ian J. Wassell, *Digital Electronics*, 2020–21. [Course materials](https://www.cl.cam.ac.uk/teaching/2021/DigElec/materials.html); [Introduction](https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_intro_20_1.pdf); [Multilevel Logic and Hazards](https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_haz_20.pdf), PDF pages 1–9; [Transistors and CMOS](https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/dev_trans_20.pdf), PDF pages 10–17; [Examples Paper](https://www.cl.cam.ac.uk/teaching/2021/DigElec/examples_20.pdf), selected gate, voter, and hazard exercise types.
3. **Stanford University.** William J. Dally, *EE108 Class Notes*, copyright 2002–2006, distributed in *EE108A Digital Systems I*, Winter 2008, with Philip Levis. [Course reader](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf). Reviewed pages: 39–42, 58–65, 67–76, 79, 83–85, and 100–101; selected exercises on pages 45 and 66. [Course schedule](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/schedule.html).
4. **University of California, San Diego.** C. K. Cheng, *CSE 140: Components and Design Techniques for Digital Systems*, Spring 2022. [Lecture 6: Universal Gates](https://cseweb.ucsd.edu/classes/sp22/cse140-a/slides/lec6UniversalSet.pdf), PDF pages 1–25; [Lecture 1: Introduction](https://cseweb.ucsd.edu/classes/sp22/cse140-a/slides/lec1Introduction.pdf), relevant gate and cost slides on pages 46–62; [Syllabus](https://cseweb.ucsd.edu/classes/sp22/cse140-a/syllabus.html).
5. **University of California, Berkeley.** CS 61C teaching staff, *CS 61C Course Notes*, [Logic Gates](https://notes.cs61c.org/content/sds-combinational-logic/). Reviewed teaching body: primitive truth tables, universal subsets, and multi-input parity conventions. The linked notes are retained at their original source; no source prose or artwork is reproduced here.

This chapter teaches the declared gate-level boundary in depth. It does not replace later minimization, arithmetic, sequential, or advanced VLSI chapters. Course-derived questions represent the reviewed in-scope reasoning types; they are not a claim that every university exercise has been reproduced. Archived Iranian entrance examinations remain reserved for joint work in the final month.

The mathematical checks verify the listed finite truth tables, mappings, CMOS conduction predicates, and illustrative timing calculations. They do not certify a real fabricated circuit, every possible waveform, or performance on unseen examination questions. The source register documents the bounded search, access failures, qualifications, and remaining uncertainty. This is a completed review draft; promotion and work on the next chapter require the student's explicit approval.
