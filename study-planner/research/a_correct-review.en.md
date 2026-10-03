### A. What the contract actually claims

1. A precondition defines the admitted initial states. A counterexample outside that domain does not refute the stated contract, although it may reveal an unnecessarily narrow domain.
2. A postcondition must describe the required function, not merely a convenient property of its result. Sortedness alone accepts an empty or constant replacement array.
3. Partial correctness quantifies over normally terminating executions. It does not establish that an execution exists which terminates, or that an implementation is safe.
4. Total correctness adds termination for every admitted input. This chapter also checks safety explicitly, rather than allowing errors to escape a normal-termination specification.
5. An impossible precondition makes a partial-correctness triple vacuous. Check consistency before treating a successful logical derivation as a useful algorithm guarantee.
6. Immutable input snapshots distinguish original operands from evolving program variables. A power invariant uses original $x,y$ and changing $r,b,e$.
7. Sortedness and multiset preservation are independent obligations. Stability and frame conditions are additional obligations when records and external memory matter.
8. A multiset records multiplicities. Set equality does not detect loss of a duplicate input record.
9. Mathematical exact integers, unsigned wrapping integers, signed machine integers and floating-point values have different semantics. Every formula is conditional on its declared model.
10. Signed C overflow is not ordinary modulo arithmetic. A modular proof must not be used to justify a signed-overflowing implementation.

### B. Backward algebra and proof obligations

11. For a pure defined assignment, substitute the old expression into the postcondition: $\operatorname{wp}(x:=E,Q)=Q[E/x]$. Do not assume the final variable value was already true initially.
12. For sequential commands, perform substitution in reverse execution order. Forward-order substitution can mix values from different checkpoints.
13. Simultaneous assignment evaluates all right sides in the same old state. Sequential assignment permits later right sides to observe earlier writes.
14. Backward substitution must avoid variable capture. Rename a bound variable when replacement would accidentally bind a formerly free occurrence.
15. A conditional proof covers the true branch under the guard and the false branch under its negation. An omitted else branch still contributes a `skip` obligation.
16. A stronger precondition implies the known precondition; a known postcondition implies a weaker replacement postcondition. Reversing either implication is unsound.
17. For array writes, equality of indices determines whether one write overwrites another. Valid indices do not imply distinct indices.
18. A loop proof checks initialization, body preservation and the exit implication. These establish partial functional correctness, not termination by themselves.
19. Guard evaluation and every access must be defined. A logically true invariant can still allow an invalid index or division by zero.
20. Verification conditions depend on the chosen annotation. A failed condition can indicate a bad annotation rather than a bad program.
21. A property of reachable states need not be inductive over all states satisfying that property. Add relationships that exclude unreachable spurious states when necessary.
22. Preservation without initialization gives no guarantee about reachable executions. A false initial invariant is not repaired by a vacuous preservation implication.
23. The negation of an invariant need not be invariant. A transition may enter the invariant region from outside it even though it never leaves that region from inside.

### C. Termination, exact counts and boundaries

24. A nonnegative integer variant must decrease strictly at every executed body. Merely staying nonnegative or nonincreasing is insufficient.
25. A strictly decreasing nonnegative real can have infinitely many steps. Exact halving of a positive real is the standard counterexample.
26. A lexicographic pair can decrease while its second coordinate increases, provided its first coordinate decreases. Componentwise ordering is a different relation.
27. A well-founded proof establishes finiteness of each execution. It does not necessarily supply a uniform numeric bound under arbitrarily large nondeterministic resets.
28. A variant supplies an upper bound when each decrease is at least one. An exact state formula or a fixed decrease can yield a sharper exact count.
29. Recursive termination needs every invoked child's measure to be smaller. Correctness of base cases does not prevent a same-size recursive cycle.
30. Empty input often needs its own base case. “Stop at size one” is insufficient for a recursion that may receive size zero.
31. The number of guard evaluations can differ from the number of body executions by one. State which quantity an exact-count question asks for.
32. A counterexample should identify an admitted input, a failing state transition and the specific obligation that fails. A large random input is less informative than a minimal witness.

### D. Searching, sorting and partitioning

33. Half-open lower bound searches $[lo,hi)$ with $0\le lo\le hi\le n$. The upper boundary may equal the array length without being a valid access index.
34. The lower-bound left classification is strictly below the target; its right classification is at least the target. These clauses determine the duplicate convention.
35. At a true guard, the floor midpoint satisfies $lo\le mid<hi$. This is the safety fact used before reading the midpoint element.
36. A below-target midpoint requires `lo=mid+1`. Keeping `lo=mid` can preserve classification while causing a one-element interval to repeat forever.
37. An eligible midpoint requires `hi=mid`, not `mid-1`, in this half-open implementation. Changing boundary conventions requires a fresh proof.
38. Sortedness justifies classifying the discarded region from a single midpoint comparison. Termination and valid indices do not establish correctness on unsorted input.
39. The maximum lower-bound body count is $\lfloor\log_2 n\rfloor+1$ for positive $n$, and zero for empty input. This count belongs to the displayed floor-midpoint implementation.
40. Upper bound replaces the classification by at most the target on the left and strictly greater on the right. Subtracting lower bound from upper bound counts target occurrences in a sorted array.
41. A safer midpoint formula avoids adding the endpoints, but its type must still represent the endpoints and their difference. Mathematical absence of overflow is not an automatic machine guarantee.
42. Insertion sort temporarily stores the key outside the array. Exclude the logical hole before asserting multiset preservation during shifts.
43. The strict greater-than insertion comparison preserves equal-key order. A greater-than-or-equal comparison can preserve sorting and multiplicity while breaking stability.
44. Insertion shifts correspond to strict inversions. Equal-key pairs do not require shifts in the stable implementation.
45. Merge correctness requires sorted output and preservation of both input multisets. It also requires an explicit exhausted-input case before reading a head.
46. Taking the left record on an equal-key merge preserves cross-half stability when both children are themselves stable.
47. A merge of nonempty lists of lengths $p,q$ uses at most $p+q-1$ head comparisons in the standard implementation, because one list becomes exhausted before the final tail copy.
48. Merge-sort induction needs smaller child sizes, complete child contracts and a merge lemma. The runtime recurrence proves none of these functional claims on its own.
49. In three-way partition, the unknown region is $[i,gt)$ and its length decreases exactly once per body. Therefore the displayed procedure executes exactly $n$ bodies.
50. After swapping a greater-than-pivot value with the unknown region's last element, keep the scan index unchanged. The incoming value still needs classification.
51. A less-than-pivot swap may exchange with an equal-region value. The special case $lt=i$ is a harmless self-swap with both boundaries advancing.
52. Three-way partition establishes three regions and preserves the record multiset. It does not establish stability or sorted outer regions.
53. Ordered-key proofs assume comparison trichotomy. Unordered floating-point NaNs require a separately specified comparison policy.

### E. Arithmetic and certificates

54. Repeated subtraction uses $X=qY+r$ with nonnegative quotient and remainder. The positive-divisor hypothesis supplies strict decrease and the usual remainder convention.
55. Conservation alone survives divisor zero. The zero-divisor loop demonstrates why a preserved identity cannot replace a termination proof.
56. Euclid preserves the gcd because common divisors are unchanged by replacing a dividend by its remainder. The positive current divisor supplies the strictly smaller remainder.
57. Euclid's operands must be updated using old values. Sequentially overwriting the dividend first usually returns the old divisor instead of the gcd.
58. If $(0,0)$ is admitted, define its gcd convention explicitly. Avoid importing a positive-input proof into an unspecified edge case.
59. Exponentiation maintains $rb^e=x^y$ at the guard checkpoint. Odd updates multiply by the old base, and even updates leave the accumulator unchanged.
60. Exponent zero executes no bodies. The chosen value is one in the exact implementation; a modular implementation must normalize it to $1\bmod M$.
61. For positive exponent $y$, the displayed power loop has bit-length many bodies and population-count many accumulator multiplications. It includes a final square that an optimized implementation may omit; this unused intermediate can overflow even when the final answer is representable.
62. Modular correctness uses congruence plus canonical output range. Congruence alone does not require returning the normalized residue.
63. Reduction after a narrow intermediate overflow can change the answer for a modulus different from the machine range. Prove the multiplication implementation as well as the modular identity.
64. An overflow check for nonnegative multiplication can compare an operand with a maximum-value quotient before multiplying, while handling a zero divisor in the check separately.
65. A sorting certificate needs ordered keys and a bijection to original records. An index list with a duplicate entry is not a permutation certificate.
66. A feasible minimization witness gives an upper bound on the optimum. A universal lower bound proves optimality only when it meets the witness value.
67. Shortest-path parent equalities establish path values only when every parent chain reaches the root. Local equalities can hold on a disconnected zero-weight parent cycle.
68. Edge inequalities give a lower bound on every path's weight after summation. Combined with an attaining parent path, they establish shortest-path optimality.
69. Negative edges do not invalidate the certificate proof. A reachable negative cycle contradicts finite edge inequalities when the cycle's inequalities are summed.
70. Unreachable vertices need separate reachability and infinity conventions. They are excluded from the finite-distance certificate model in this chapter.
71. Structural induction suits recursive tree properties, including conserved leaf mass. Missing child branches explain why a universal bound need not be an equality.
72. A feasibility invariant is insufficient to prove a greedy choice optimal. Supply an exchange, dominance or matching-bound argument for the specific objective.
73. Dynamic-programming correctness requires a recurrence covering all legal choices and an acyclic dependency order. A table of plausible values is not a proof.
74. Finite exhaustive tests can decisively refute a claim and verify a bounded domain. They cannot establish an unbounded theorem or guarantee every unseen examination answer.

### A complete procedure for a new examination problem

Read the input domain and arithmetic model first. Identify the requested quantity: output, correctness, safety, termination, stability or cost. Write the state at the checkpoint and an invariant connecting it to the original input. Verify initialization, each branch and the exit implication. If termination is relevant, give a well-founded decreasing measure. For an exact count, derive the number of transitions rather than quoting a complexity class. Check empty, singleton, duplicate, zero and exceptional-parameter cases permitted by the problem. Finally, refute distractors with either the derived formula or a concrete admitted counterexample. This procedure supports reasoning across implementations; it is not a promise that every unfamiliar problem will yield to a memorized template.
