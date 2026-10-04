### Definitions and representation

1. Declare the variable order before reading decimal indices; in order A,B,C,D the index is $8A+4B+2C+D$.

2. A minterm contains every variable exactly once and is true on exactly its indexed row; complement the literals whose row bits are zero.

3. A maxterm contains every variable exactly once and is false on exactly its indexed row; complement the literals whose row bits are one.

4. The identity $M_i=\overline{m_i}$ links the same index, not the complemented index; test the formula at row i to check polarity.

5. Canonical SOP uses the one-set, and canonical POS uses the zero-set. Complement the index set only within the declared $2^n$-row universe.

6. A semantically equivalent SOP is not a correct response to a question specifically asking for canonical POS; check syntax and truth behavior separately.

7. General DNF/SOP and CNF/POS may omit variables within a component; canonical forms may not omit them.

8. Changing the variable order permutes every row’s bits before converting to decimal. It does not merely reorder the printed list of existing indices.

9. To expand a missing product variable X, multiply by $X+\overline X$ and distribute; each missing variable doubles the represented rows.

10. To expand a missing sum variable X, use $(P+X)(P+\overline X)=P$; this Boolean identity is not ordinary numerical algebra.

11. A product with r fixed coordinates among n variables has r literals and covers $2^{n-r}$ rows, provided its literal assignments are consistent.

12. A contradictory product such as $A\overline A$ is zero, not a useful cube with a negative number of free dimensions.

13. An empty OR is zero and an empty AND is one. Constant functions must respect these two different identities.

14. There are $\binom nk2^{n-k}$ cube patterns with k free coordinates and $3^n$ cube patterns in total, before function-specific validity checks.

15. The number of Boolean functions is $2^{2^n}$, not $3^n$; truth-table output choices and cube syntax count different objects.

### Map geometry and group validity

16. Use Gray order 00,01,11,10 for a two-bit map axis so adjacent labels—including the cyclic endpoints—differ in one bit.

17. Decimal minterm numbering remains ordinary binary even though the printed K-map cells are arranged in Gray order.

18. Horizontal and vertical wrap-around represents valid single-bit adjacency; opposite edges are neighbors in the Boolean geometry.

19. The four corners of a four-variable map can form one four-cell cube; derive its fixed coordinates instead of drawing four unrelated groups.

20. Diagonal contact does not imply adjacency. Rows differing in two bits cannot combine into a two-cell implicant.

21. Power-of-two cardinality is necessary but insufficient for a group; every assignment of its free coordinates must be present.

22. A three-cell or bent incomplete group is not one product. Replace it by valid cubes or prove that omitted cells are permitted before expanding.

23. A one-group may contain required ones and DC rows but no specified zero; a zero-group has the dual restriction.

24. For SOP, keep each fixed bit as its satisfied literal. For POS, reverse its polarity so the sum vanishes on the grouped zero rows.

25. Overlap is legal in Boolean covers; ORing a row twice still produces one and does not count it numerically twice.

26. A group’s product is derived from constant coordinates, not from the location of its center, its numerical label average or the number of visible rectangles.

27. Five-variable planes can merge only corresponding compatible groups; the plane variable disappears only when both of its values are covered.

28. Plane indices depend on bit significance. An MSB plane variable splits consecutive halves; an LSB plane variable splits alternating indices.

29. Six-variable plane adjacency must also follow Gray geometry; arbitrary nearby drawings do not license group merging.

30. A cube with more cells has fewer literals, but choosing it greedily can make the complete cover more expensive.

### Prime covers and proofs of optimality

31. A prime implicant is maximal by inclusion among valid cubes, not necessarily a cube of maximum size among every prime.

32. A prime is essential only when it uniquely covers at least one required row in the complete prime chart.

33. Prime status does not force selection. Nonessential primes may be absent from every particular optimum or appear in different tied optima.

34. Under monotone two-level term/literal cost, expanding a valid product to a prime cannot worsen its cost; this justifies restricting exact search to primes.

35. The prime-restriction proof does not establish optimality for arbitrary technology costs or for a particular guessed collection of primes.

36. Irredundancy means no selected term can be removed from that cover; it does not mean no smaller different cover exists.

37. A complete optimality certificate needs both a lower bound and an achieving cover, or a complete exact search with its candidate universe justified.

38. If p obligations are pairwise unable to share any candidate, at least p candidates are required; these witnesses provide a packing lower bound.

39. If every candidate covers at most r obligations, at least $\lceil |O|/r\rceil$ candidates are necessary, but overlap can make this bound unattainable.

40. Essential primes give a lower bound because their unique-owner witnesses cannot be covered by another prime.

41. A function can have no essential prime and still have a minimum cover; cyclic charts are a standard example.

42. A function can have several optimum SOP expressions, so do not claim uniqueness without solving the complete chart or proving forced choices.

43. Delete obligations already covered by a selected compulsory candidate before comparing residual coverage; keep the selected cost separately.

44. Candidate dominance requires coverage superset and no greater cost under the actual objective; coverage alone is insufficient for weighted minimization.

45. If candidate-choice set S(u) is contained in S(v), requirement v is redundant because satisfying u guarantees v. Deleting u reverses the argument incorrectly.

46. Textbook charts may transpose rows and columns. Identify whether a line represents a candidate or an obligation before applying dominance.

47. Removing equal-cost duplicate-coverage candidates preserves an optimum value but can erase alternative optimum expressions; retain or reconstruct them when all answers are requested.

48. A secondary essential after discretionary pruning is conditional on that pruning and need not be essential in the original prime chart.

49. Petrick selection variables represent candidate inclusion, not input signal values. Their truth assignment describes a cover.

50. A Petrick clause is the OR of all owners of one required obligation; the AND of all clauses enforces complete coverage.

51. Use Boolean idempotence and absorption when multiplying Petrick’s formula. Superset selections are unnecessary under positive monotone costs.

52. Minimize number of selected candidates first and literal weight second when using the chapter’s lexicographic convention; do not compare only term count after a tie.

### Don’t-cares and exact tabulation

53. O, Z and D must be disjoint and exhaust the input universe. A row cannot simultaneously be required one and optional.

54. Don’t-care means permission to choose an output under a contract; it is not a third Boolean output value of the realized circuit.

55. Two valid DC realizations can disagree on optional rows. Compare them only on care rows when testing the incomplete specification.

56. DC rows participate in QM generation because they can enlarge useful cubes, but do not become required columns in the final covering chart.

57. A DC-only cube may be an intermediate merging object; if it covers no required row, selecting it cannot help the ordinary functional cover.

58. With no required one rows, the constant-zero SOP is optimal under the expression model; optional rows alone force no product term.

59. With no required zero rows, the constant-one POS is optimal under the dual expression model.

60. To minimize POS, swap O and Z while preserving D, solve an SOP for the complement, then apply De Morgan to every selected product.

61. A DC assignment used in an SOP optimum need not match the completion used in an independently optimized POS; both can satisfy the original contract.

62. QM merges require identical dash-position masks and exactly one differing fixed bit; unequal masks cannot be ignored to invent a child.

63. A legal merge doubles the cube’s cell count and removes one literal; verify both facts to detect accidental multi-bit elimination.

64. Mark every participating parent as combined, even when its child duplicates an existing child; otherwise a nonprime may be reported as prime.

65. Deduplicate equal child cubes by pattern, not merely by one pair of parent indices; several different parent pairs can generate the same cube.

66. QM generation finds primes, but exact cover selection is a separate phase. Producing the complete prime list does not finish a cyclic minimization.

67. The completeness proof splits any valid cube into valid halves and inducts on free dimensions; it is stronger than testing a few sample merges.

68. Exact cube enumeration and cover selection can be exponential. A systematic algorithm is not automatically a polynomial-time algorithm.

### Hazards, gate models and diagnostic checks

69. A static-one hazard is a possible 1–0–1 excursion during an input change whose two settled outputs should both be one.

70. In the two-level SOP single-input-change model, every relevant adjacent one pair needs a common selected product to remove arbitrary-delay static-one risk.

71. Hazard-constrained covering must cover edge obligations as well as vertex obligations; a complete truth-table cover can still miss a transition bridge.

72. The consensus term in $AB+\overline A C+BC$ is algebraically redundant but may be necessary for a hazard-free physical realization.

73. Static-zero POS has the dual consensus-sum repair. Do not use a one-group SOP argument without reversing the appropriate polarity and transition condition.

74. A selected DC completion can introduce additional realized-one edges. Check all transitions required by the external contract, not only the original O–O pairs.

75. Single-input static-hazard freedom does not guarantee multilevel dynamic-hazard freedom or safety under simultaneous input changes.

76. A delay calculation must state initial settled values, input-change direction, every gate delay, and transport versus inertial interpretation.

77. NAND–NAND implements a SOP and NOR–NOR implements a POS, but inverter availability, fan-in and tied-input conventions must be stated before gate-count claims.

78. A minimum SOP is not automatically a minimum multilevel circuit. Factoring, XOR gates and technology mapping change the permitted implementation space.

79. Multi-output PLA cost can count distinct products, output connections or both. Shared cubes must avoid the zero-set of every output they feed.

80. Before accepting an examination answer, check variable order, requested representation, care-row correctness, complete-cover cost and any transition constraints. If the question omits a cost convention, state the ambiguity rather than inventing certainty.
