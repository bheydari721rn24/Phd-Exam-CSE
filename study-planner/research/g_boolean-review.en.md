## 14. Consolidated summary, examination rules, and solving method

### The main ideas in connected form

Boolean algebra begins with a declared binary domain and exact operator definitions. An expression is a recipe, while a function is the complete mapping it produces. Fixing the input order makes a truth table a definitive specification. For every fully specified scalar function, full row selectors construct a valid expression. This is a proof of representability, not a proof of minimal implementation cost.

Algebraic identities preserve the output on every allowed assignment. Both distributive laws, absorption, combining, De Morgan, and consensus follow from the binary definitions. Complementation and duality are distinct operations on an expression. Ordinary arithmetic cancellation is generally invalid for AND and OR because those operations can conceal information. XOR has different rules and allows cancellation; its interaction with AND leads to algebraic normal form.

Cofactors expose what remains after fixing one input. Shannon decomposition reconnects the zero and one slices exactly, in either SOP or POS form. Equal cofactors mean an input is irrelevant, unequal cofactors establish essential dependence, their XOR measures context-dependent change, their AND expresses universal elimination, and their OR expresses existential elimination. Containment of the two cofactors determines unateness. These interpretations explain the formulas rather than leave them as disconnected symbols.

Verification converts a claim into a witness problem. XOR of two scalar outputs marks mismatches; OR of the coordinate mismatches checks a vector output. A care function restricts the assignments that must be preserved. A single satisfying mismatch assignment refutes full equivalence. Recursive restriction is complete because every split covers both values of the selected input, though its worst-case cost remains exponential.

The chapter concerns exact binary steady-state functions. Physical delays, hazards, unspecified analog levels, HDL unknowns, and programming side effects require additional models. Functional equivalence is the algebraic conclusion; stronger conclusions must be justified separately. The worked problems and laboratory support deriving answers on unfamiliar examples within this scope.

### Sixty complete-sentence examination rules

#### Domain and specification

1. Declare whether a plus sign means OR, integer addition, or addition modulo two before applying any algebraic rule.
2. Inclusive OR accepts the both-one case, whereas two-input XOR excludes it; translate "at least one" and "exactly one" differently.
3. Fix the input order and its most significant position before identifying binary row numbers or reading an output vector.
4. A fully specified n-input scalar function needs one output for each of its 2<sup>n</sup> assignments, including the single empty assignment when n=0.
5. Conflicting outputs on one input row make a specification inconsistent; an omitted output instead leaves a completion choice if the omission is intentional.
6. Define signal polarity in words before writing its literal, especially for inhibits, vetoes, active-low conditions, and permission signals.
7. The phrase "only if" states a necessary condition and generally specifies containment rather than equality.
8. Distinguish literal occurrences, distinct variables, and essential support; all three counts can differ for the same written expression.
9. A function has a unique truth table under a fixed order, but may have many equivalent expressions and implementations.
10. Count scalar functions as 2<sup>2<sup>n</sup></sup>; count unconstrained k-output functions as 2<sup>k·2<sup>n</sup></sup>.

#### Laws and complement scope

11. AND and OR are idempotent, so repeating a requirement does not change its output; XOR instead cancels an identical pair.
12. Remove products containing both polarities of an input as zero, and replace sum terms containing both polarities as one.
13. Use both distributive laws: x(y+z)=xy+xz and x+yz=(x+y)(x+z), with no appeal to real-number arithmetic.
14. Absorption removes xy from x+xy, because all assignments satisfying the smaller product already satisfy x.
15. Combining complementary literals with a shared context removes that input: xy+xy′=x and (x+y)(x+y′)=x.
16. Covering gives x+x′y=x+y; dropping the entire x′y term without retaining y is generally wrong.
17. Consensus removes yz from xy+x′z+yz, provided the complement pair and remaining factors match the theorem exactly.
18. Consensus can be applied to compound Boolean subfunctions, but each compound complement must retain its original scope.
19. Deliberate OR duplication can form several combining pairs; explain the use of idempotence rather than cancel duplicates arithmetically.
20. NAND and NOR are commutative but not associative, so a sequence of those operations cannot be regrouped as AND or OR can.
21. A complement on a whole parenthesized expression must be processed at that expression's top operator before moving inward.
22. De Morgan exchanges AND and OR and complements each operand; double complements disappear only after their scope has been tracked.
23. A dual swaps AND/OR and zero/one, while keeping variable names and existing literal complements unchanged.
24. The dual, output complement, and all-input-inverted function are three different transformations; their relation is E<sup>d</sup>(x)=[E(x′)]′.
25. Self-duality requires opposite outputs on every complementary input pair; balancedness alone is not sufficient.

#### Simplification and XOR

26. Specify whether an optimization targets literal count, term count, proof clarity, gate cost, or delay; these objectives need not select the same expression.
27. Search for constants, absorption, complementary pairs, and consensus before expanding every factor.
28. An SOP term t is redundant in t+H exactly when tH′=0; collective coverage by several terms is sufficient.
29. A POS factor s is redundant in sH exactly when H≤s, which reverses the containment direction used for an SOP term.
30. OR and AND cannot generally be cancelled from both sides of an equality; construct a hiding-operand counterexample before accepting such a step.
31. A simplification proved under an assumption is conditional; verify whether that assumption covers the entire specification.
32. Express two-input XOR as x′y+xy′ and XNOR as xy+x′y′ to connect parity and equality to the basic algebra.
33. XOR with a fixed operand is reversible, so x⊕y=x⊕z legitimately implies y=z.
34. A many-input XOR measures odd parity, while its complement measures even parity; neither normally means that all inputs are equal.
35. AND distributes over XOR, but the OR-style distributive identity with XOR does not generally hold.
36. OR of two subfunctions equals their XOR exactly when the subfunctions never overlap, meaning their AND is identically zero.
37. Algebraic normal form uses XOR of square-free products and has unique coefficients; an OR-based SOP obeys a different coefficient logic.
38. OR can be translated into the Boolean ring as x⊕y⊕xy, and complement as 1⊕x.
39. For two-input ANF, the xy coefficient is the XOR of all four truth-table outputs, with the other coefficients obtained from the corresponding lower-order rows.
40. An affine Boolean function has degree at most one in its ANF; a short expression containing nonlinear products is not automatically affine.

#### Selectors, cofactors, and advanced reasoning

41. A full product selector uses an uncomplemented literal for a one-valued input; a sum that vanishes on that same row uses the opposite polarity.
42. A consistent product fixing r distinct inputs covers 2<sup>n−r</sup> assignments, after duplicates and contradictions have been handled.
43. A dash omitting an input literal in a product describes a free input position, whereas an unspecified output row describes a specification choice.
44. A cofactor is generally a function of the remaining inputs; restricting one variable is not the same operation as evaluating every variable.
45. Restrictions on distinct variables commute, and restriction commutes with every truth-functional operation when the same assignment is used.
46. Shannon SOP attaches the zero cofactor to x′ and the one cofactor to x; its POS form attaches them to x and x′ respectively.
47. An input is irrelevant exactly when its zero and one cofactors are identical as functions; occurrence of its name in a formula proves nothing by itself.
48. Boolean difference is the XOR of the two cofactors and describes output change under a toggle, with all other inputs held fixed.
49. The zero-cofactor product rule includes the extra difference-product term de; importing a two-term calculus rule can give a false answer.
50. Existential elimination ORs the cofactors, universal elimination ANDs them, and both outputs remain functions until all inputs have been eliminated.
51. Universal and existential elimination give the tightest respective lower and upper bounds independent of the removed variable.
52. Quantifiers of the same kind commute over distinct inputs; mixed quantifiers require an explicit dependency analysis and need not commute.
53. Positive unateness means f₀≤f₁ and negative unateness means f₁≤f₀; equal cofactors satisfy both and indicate independence.
54. Opposite polarities in a redundant written cover do not prove semantic binateness; use the cofactor containment test.
55. A syntactically unate SOP is a tautology exactly when it contains a constant-one term, because otherwise one assignment falsifies every used literal polarity.

#### Verification and model limits

56. Full scalar equivalence requires the mismatch miter f⊕g to vanish on every assignment; one satisfying row is an explicit counterexample.
57. For multiple outputs, OR the coordinate mismatch indicators; XOR aggregation can cancel two simultaneous errors and return a false success.
58. Care-restricted equivalence requires C(f⊕g)=0; don't-care rows permit alternative binary completions and are not a third algebraic value.
59. A primary input stuck at zero is detected only when its healthy value is one and its Boolean difference is one; use the opposite excitation value for stuck-at-one.
60. Functional equality does not prove equal delay, absence of hazards, analog safety, or programming side-effect preservation; every such conclusion needs its own model.

### An eight-step method for unfamiliar questions

1. **Specify the domain.** State the input meanings, order, output count, operator meanings, and any care-set or other assumptions.
2. **Parse the expression.** Identify the top operator and each complement scope; add parentheses wherever a convention could be ambiguous.
3. **Choose a representation.** Use a table for small specifications, algebra for an identity, cofactors for dependence, or an on-set for coverage.
4. **Remove immediate redundancies.** Apply constants, idempotence, contradictions, absorption, and complementary-pair combining before a large expansion.
5. **Name every substantive step.** Justify the relevant theorem or case split and retain conditional assumptions throughout the derivation.
6. **Produce a certificate.** Give a general proof for an identity, a mismatch assignment for a refutation, or the two cofactors for a dependence claim.
7. **Check by another route.** Compare a truth table, case argument, cofactor calculation, or count with the first derivation to expose a shared indexing or scope error.
8. **State what the conclusion covers.** Distinguish full from care-restricted equivalence, syntactic from semantic properties, and functional from physical claims.

### Review status and remaining uncertainty

The student approved this English chapter on 2026-10-02. The mathematical derivations, independent finite checks, parser tests, font checks, and sampled print inspection provide specific evidence. They do not establish literal universal correctness or guarantee answers to every unseen examination question. Later gate, minimization, and timing chapters supply their own material. No archived Iranian exam has been mined for this chapter, and no pre-study test is requested.

## 15. References and exact reading locations

1. **Massachusetts Institute of Technology.** Chris Terman. *6.004 Computation Structures*, Spring 2017. [Chapter 4: Annotated Slides](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/). Written annotations reviewed for functional specification, SOP construction, Boolean reduction, care conditions, and the distinction between functional redundancy and implementation behavior. The [worksheet landing page](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s3/) was screened; its linked exercise file is not counted as a reviewed problem source.
2. **University of Cambridge.** Ian Wassell. *Digital Electronics*, 2020–21. [Logic Gates and Boolean Algebra](https://www.cl.cam.ac.uk/teaching/2021/DigElec/slides/comb_log_bool_20.pdf), PDF pages 1–14, with algebra on pages 8–12. [Examples Paper](https://www.cl.cam.ac.uk/teaching/2021/DigElec/examples_20.pdf), pages 1–2 for identity, expression-reduction, and voter-specification patterns. Gate-only construction and map exercises are reserved for later chapters. [Course materials](https://www.cl.cam.ac.uk/teaching/2021/DigElec/materials.html) identifies the offering and instructor.
3. **Stanford University.** William J. Dally and Philip Levis. *EE108A: Digital Systems I*, Winter 2008. [Lecture 1](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/lectures/01-introduction-w08.pdf), PDF pages 8–16, including memoryless functions, acyclic composition, majority, operator conventions, laws, and verification. Page 14 contains mislabeled headings; the identities in this chapter are classified by their definitions. The teaching content is not represented as a complete independent axiomatization. [Offering schedule](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/schedule.html).
4. **Carnegie Mellon University.** Rob A. Rutenbar. *18-760: VLSI CAD*, Fall 2001. [Lecture 1: Advanced Boolean Algebra](https://course.ece.cmu.edu/~ee760/760docs/lec01.pdf), PDF pages 4–24 for restriction, difference, quantification, and containment; pages 30–39 for cube representation and recursive tautology checking. [Homework 1](https://course.ece.cmu.edu/~ee760/760docs/hw1v1.pdf), items 1–5, PDF pages 1–3, reviewed for cofactor identities, POS Shannon, grouped-input representation, and unate complements. Statements and derivations here are independent; source qualifications and detected notation issues are in the audit. [Course description](https://course.ece.cmu.edu/~ee760/760class.html).
5. **University of California, Berkeley.** John Wawrzynek, with edits by Lisa Yan; CS61C course teaching team. [Boolean Algebra](https://notes.cs61c.org/content/sds-combinational-logic/boolean-algebra/) and [Canonical Form, CL Design](https://notes.cs61c.org/content/sds-combinational-logic/cl-design/), living written course notes. Teaching bodies reviewed for operator definitions, algebra, full-row construction, majority, and equality comparison. Course text and artwork are linked for attribution, not copied into this chapter. The historical PDF link returned HTML during local retrieval and is not counted as a reviewed PDF.
6. **Cornell University.** Adrian Sampson and Giulia Guidi; CS3410 teaching team. *Computer System Organization and Programming*, Fall 2024. [Gates & Logic](https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/logic.html), Truth Tables, Logic Notation, and Universal Gates and a Recipe for Building Anything. The in-scope XNOR and selector exercise patterns were reviewed; the later arithmetic construction is not taught here. [Offering overview](https://www.cs.cornell.edu/courses/cs3410/2024fa/).

The bounded source pool and its access evidence are recorded in the project research files. Additional ANF, self-duality, counting, model-boundary, and verification derivations are original instructional extensions with independent checks. The references specify actual reviewed locations rather than imply that every lecture or problem in each complete course was analyzed.


The student explicitly approved this chapter on 2026-10-02. It is now in the approved library.
