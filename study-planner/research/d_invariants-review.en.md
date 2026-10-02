### The complete reasoning chain

An invariant proof starts with an explicit state model, proves initialization and preservation under every enabled transition, and uses induction to conclude that every reachable state satisfies the assertion. Safety follows only when that assertion excludes the forbidden states. Equality of invariant values does not itself supply a path to a target.

A termination proof assigns relevant states or calls a value in a well-founded order and proves strict descent. Partial correctness identifies the result if execution finishes; termination ensures it finishes when each ranked step itself terminates. Total correctness needs both arguments. A terminal state can still be an unintended deadlock.

Structural induction follows finite-data constructors. Each base constructor supplies a base case, and each recursive constructor supplies hypotheses for its components. The strongest useful hypothesis often includes arbitrary accumulators and unchanged parameters so it applies to the arguments actually passed. Correctness, well-definedness, termination, evaluation order, output order, and complexity remain separate obligations.

### Choose the method from the question

| Question pattern | Productive starting point | Completion criterion | Common trap |
|---|---|---|---|
| A target seems impossible | Compute each move's change to counts, parity, or weighted sums. | Prove preservation and compare initial and target values. | Treat equal invariant values as proof of reachability. |
| A true assertion fails closure | Inspect whether the bad predecessor is reachable. | Strengthen with a proved bound or relation. | Label an unreachable bad edge a reachable violation. |
| A loop should return a value | Describe its processed prefix and remaining work. | Prove setup, body safety, preservation, and the exit consequence. | Lose the relationship between output and original input. |
| A counter can reset | Identify primary progress before secondary work. | Use lexicographic descent or a justified bounded weighted rank. | Assume one large constant covers arbitrary resets. |
| A recursive parameter changes | Describe the helper for an arbitrary parameter. | Quantify that parameter before using induction. | Assume only the top-level empty accumulator case. |
| A tree routine uses both children | Write one case for each constructor. | Apply both child hypotheses to actual call arguments. | Confuse external empty positions with data leaves. |
| A numerical bound will not close | Compute the slack consumed by the next term. | Prove a bound that carries sufficient slack. | Add a positive term to a bound already at the target. |
| A finite proposed rank fails | Inspect the bad edge and detect reachable cycles independently. | Supply another rank or a concrete cycle. | Infer nontermination from one failed certificate. |

### State modeling and invariant rules

1. Specify the state set, initial states, and exact transition relation before choosing an assertion. A proof about a different move set does not answer the problem.
2. Include the control location when assertions differ between program points. Numeric variables alone may not identify the next permitted operation.
3. Distinguish immutable inputs from overwritten variables. Equations about original input need a fixed name or justified snapshot.
4. Count path length by transitions. A finite execution has one more state occurrence than transitions.
5. Reachability is existential over finite prefixes. A reachable goal may be avoided by another legal execution.
6. The reachable set is the least closed set containing the initial states. Every initialized closed certificate contains it.
7. Initialization and preservation are independent obligations. A preserved predicate that fails initially proves nothing about actual executions.
8. A reachable-state property may fail closure at an unreachable predecessor. Check the scope of a reported counterexample.
9. Preservation checks every outgoing edge from every candidate state, including unreachable candidate states.
10. Safety needs an initialized closed assertion implying the desired property. Exact equality with reachability is unnecessary.
11. Strengthening can supply the information needed by induction, but every added clause still needs initialization and preservation.
12. Intersection and union preserve transition closure. Complement can fail because an incoming edge becomes an escape from the complement.
13. Weakening can destroy inductiveness by admitting extra predecessors with unsafe successors. Logical implication alone does not transfer closure.
14. Strengthening is not a ritual. Compute the change before claiming that a candidate is too weak.
15. Finite successful examples suggest patterns but cannot replace the universally quantified preservation calculation.
16. Removing states with unsafe successors constructs the largest safe closed subset of a finite graph. Forward reachability constructs a different, least closed set.

### Conservation and puzzle rules

17. Compute a derived quantity's change under every move type. Conservation, weak monotonicity, and strict monotonicity are different classifications.
18. A linear conserved weighting must annihilate every move vector. Matching one transition is insufficient.
19. Modular preservation requires every change to be divisible by the chosen modulus. Exact conservation is stronger than necessary.
20. Over a composite modulus, nonzero residues need not be invertible. Check a pivot before using field-style modular division.
21. Different conserved values exclude reachability. Equal values require further constraints or a constructive witness.
22. A constructive converse must respect direction and guards. Intermediate negative coordinates invalidate a path in a nonnegative state domain.
23. Check every permitted orientation in a tile-weight argument. A weighting for horizontal dominoes alone says nothing about vertical ones.
24. Area divisibility can miss coloring obstructions. Weighted counts retain information that total area discards.
25. Flipping a fixed even number of coins preserves head parity because the count change is even. It does not conserve the count itself.
26. State-dependent additions may require a previously proved parity invariant to classify their effect. Do not assume the needed parity without proof.
27. Adjacent swaps flip inversion parity only for distinct entries. Swapping equal entries changes no permutation ordering.
28. A three-cycle preserves parity through two swaps. Its inversion count may stay constant, so parity preservation is not strict progress.
29. On an even-width sliding puzzle, combine numbered-tile inversion parity with blank-row parity to handle vertical moves.
30. On an odd-width puzzle, a vertical move crosses an even number of numbered entries, so inversion parity alone is preserved.
31. A weakly decreasing geometric quantity can exclude a target without proving termination. The marked-union perimeter illustrates that distinction.
32. Sequentializing simultaneous growth is justified only when enabling conditions remain valid. Permanent marks make the two-neighbor argument work.

### Loop and termination rules

33. Place the invariant at a definite control point. A loop-head assertion may legitimately fail halfway through a body before being restored.
34. Derive a loop invariant by replacing completed work with a processed prefix. Keep its exact relationship to original input.
35. Prove body safety, including valid indices and defined arithmetic. An output equality does not justify an invalid access.
36. Use both the invariant and the false guard at exit. One supplies information the other may lack.
37. Check zero iterations explicitly. Empty arrays, zero exponents, and initially false guards expose missing setup assumptions.
38. Sequential assignments use values left by preceding statements. A simultaneous-update proof needs parallel assignment or saved old values.
39. Partial correctness constrains terminating executions. An infinite routine can satisfy it vacuously.
40. Total correctness adds termination for every permitted input and choice. Preservation alone does not provide it.
41. A natural rank must stay nonnegative and strictly decrease on every relevant enabled transition. Both conditions matter.
42. Weak descent permits an infinite plateau. A constant-rank self-loop is an immediate counterexample.
43. Strict descent in unrestricted integers permits an infinite negative sequence. The lower-bound argument cannot be omitted.
44. Strict descent among positive reals can converge without reaching a base case. Positivity is not well-foundedness.
45. A uniform positive decrease plus a lower bound gives a step bound. Merely having some positive decrease at each step does not.
46. A rank bounds only its ranked transitions. A nonterminating computation inside one body iteration defeats total correctness of the outer loop.
47. Lexicographic descent permits secondary resets when the primary coordinate drops. The sum of coordinates may increase.
48. Fixed-dimension natural tuples are well-founded under the stated lexicographic priority. Unrestricted integer coordinates need another argument.
49. A scalar weighted replacement requires a justified reset bound. Choose its weight from that bound and calculate the maximum increase.
50. Every execution can be finite while lengths from one fixed start are unbounded. Arbitrary reset choices produce this distinction.
51. Termination can end in deadlock. Add a terminal-state or progress characterization when a successful answer is required.
52. Fairness is an execution assumption. A continuously enabled exit does not force an unrestricted scheduler to take it.

### Recursive and structural rules

53. State a recursive routine's domain first. A written base case does not imply that every call stays in that domain.
54. Prove each recursive dependency smaller in a well-founded order. A visually simpler argument is not a strict comparison.
55. Include termination and result correctness jointly when a proof relies on returned values from smaller calls.
56. Use integer quotient and remainder for natural-number recursion. Real division can destroy domain closure and descent.
57. Supply base cases for every residue reached by a decrement. Removing two list entries needs both empty and singleton cases.
58. Multiple smaller calls can terminate while having exponential cost. Inefficiency and nontermination are different diagnoses.
59. Reuse the recursive result when the intended algorithm makes one subcall. Duplicating it changes the recursion tree even if the answer is unchanged.
60. Structural induction has one obligation per constructor and one hypothesis per recursive component. Omitting a constructor leaves the theorem unproved.
61. The least generated-set convention covers finite constructions. Infinite lazy objects are not automatically included in a finite-list proof.
62. Keep unchanged parameters universally quantified inside the induction predicate so it covers changed accumulators and environments.
63. Induction on one argument can prove a two-argument theorem with the other arbitrary. Pair induction needs a justified smaller-pair relation.
64. Determine whether an accumulator represents a prefix, suffix, or numeric offset before choosing its specification.
65. Prove concatenation associativity before using it. Regrouping is valid, but reordering would require false list commutativity.
66. Returned-value equality is symmetric in a proof. The underlying evaluation step still has a direction and is not reversible execution.
67. Tail recursion has no pending operation after the call. Constant stack space additionally needs actual tail-call elimination.
68. Linked-list cons and tail costs differ from Python slicing and concatenation. A translation preserves complexity only if its primitive costs match the model.
69. Declare whether a tree leaf carries data, is a nonempty terminal node, or denotes an external empty position. Counts depend on that convention.
70. Declare the height base convention before using a power-of-two bound. Empty height zero and data-leaf height zero produce different exponents.
71. Evaluation order differs from output order. Right-first helper evaluation can still construct left-to-right leaf output.
72. For ambiguous constructions, prove independence of derivation before defining an object-level function. A derivation-tree function has another domain.
73. Generator soundness proves generated objects have the property. Completeness separately proves every qualifying object can be generated.
74. Mutual recursion needs a joint hypothesis or a justified phase ranking. Using the other routine's unproved correctness is circular.
75. Nested recursion may increase a secondary argument while lowering a primary one. Also prove the inner output lies in the outer call's domain.
76. Fix an Ackermann variant's exact equations before comparing values. Similar names do not make differing base cases interchangeable.
77. Pure expression substitution supports structural evaluation proofs. Side effects and bindings change the hypotheses and may invalidate the result.
78. Value preservation proves a simplifier's soundness. It does not show that the simplifier recognizes every opportunity or returns an optimal expression.
79. Reachable cycles decide universal termination exactly in finite graphs. Failure of one supplied rank is only failure of that certificate.
80. Finite exhaustive checks detect errors within their declared scope. General claims still need proofs, with source and examination boundaries visible.

### A reusable complete-solution template

Write the domain, initial state, permitted steps, and required conclusion. Define the assertion or rank with its quantifiers and codomain. Prove initialization or every base case. For each transition or constructor, name old values, check guards and recursive-call domains, and calculate the new assertion using proved hypotheses. Conclude by the appropriate induction principle. For an output claim, combine the assertion with the actual exit condition. For total correctness, add well-founded progress and termination of each ranked step. For attainability, distinguish an obstruction from a valid constructive path. Finally, check zero, empty, boundary, duplicate, and representation cases before claiming completeness.
