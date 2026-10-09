1. **Factorial: value, calls, edges, and depth.** For decrement-to-zero factorial, the value is $n!$, calls and depth are $n+1$, and recursive edges and multiplications are $n$. State whether the root and base are included.

2. **Changing the factorial base.** Changing the base from zero to one can remove one invocation and multiplication without changing factorial's value. Never transplant exact counts without checking the guard.

3. **A nonreachable base.** A base case must be reachable from every admitted input. Parity and domain preservation matter when decrement steps skip values.

4. **Fixed-step call count.** For a positive step k and a nonpositive stopping guard, positive input n needs $\lceil n/k\rceil$ recursive edges and one more invocation.

5. **An index increases while the measure decreases.** Termination can be proved by remaining work even when a parameter increases. A one-past endpoint is a stopping state, not an array element.

6. **Lexicographic progress.** A reset of one coordinate does not invalidate termination when a higher-priority coordinate decreases. Encode or prove the lexicographic order explicitly.

7. **Partial correctness without termination.** Correctness of a returned result and existence of a return are different proof obligations. Total correctness requires both.

8. **A sum proof with an empty interval.** An interval sum proof needs bounds, an empty-case identity, a decreasing length, and representable intermediate arithmetic.

9. **Returned value versus emitted output.** Track printed output and returned values separately. Their ordering and counts depend on different instructions.

10. **One saved local per frame.** Same-named automatic locals in different recursive invocations are distinct objects. Shared storage must be identified separately.

11. **Post-decrement destroys progress.** A postfix decrement as the only call argument passes the old value. Separate the child's argument from the parent's later local state.

12. **Pre-decrement changes the continuation.** Pre-decrement and subtraction can pass the same child value while leaving different parent state for the return phase.

13. **Unsigned underflow at the boundary.** Guard small unsigned arguments before subtracting a stride. Mathematical negativity is not how unsigned C represents the boundary.

14. **Operand order and pure results.** Unspecified call order can coexist with a fixed pure result. Do not invent an output order or confuse it with undefined behavior.

15. **Short-circuit avoids a child.** Short-circuit evaluation can stop recursion before the theoretical deepest base. Separate worst-case counts from the actual input trace.

16. **A missing returned result.** A recursive call's return does not implicitly return from its caller. Every value-producing path needs the specified return.

17. **Static state survives calls.** Static state is shared and persistent. Include relevant state in a contract and do not memoize a history-dependent function as if it were pure.

18. **Pointer aliasing across frames.** Pointer parameters are copied by value while their pointees can remain shared. Trace identities of objects, not just parameter names.

19. **Digit sum with a one-digit base.** Digit-recursion counts depend on whether the base is one digit or zero. Give zero separately before applying a logarithm.

20. **Changing the numeral base.** Halving or base-b division is logarithmic only when the divisor exceeds one and integer rounding and the stopping guard are specified.

21. **Euclid's trace and invariant.** Euclid decreases the positive second argument. Count remainder operations separately from the terminal invocation.

22. **Euclid with the smaller argument first.** Use the measure the algorithm actually decreases. Optional input normalization can change exact calls without changing the mathematical result.

23. **Palindrome's worst-case formula.** With a length-at-most-one base, matching palindrome calls are one more than endpoint-pair comparisons. Exclude the string terminator from content length.

24. **Repeated slicing changes time.** Argument construction is part of recursive work. Replacing slices by interval bounds changes cost even if the recurrence's logical problem sizes look identical.

25. **Binary search's unsuccessful path.** Unsuccessful binary search includes an empty final invocation. Its count differs from successful search even with the same comparison depth.

26. **Binary search loses strict shrinkage.** Binary search must remove the midpoint after an unsuccessful comparison. A retained one-element interval is a direct nontermination witness.

27. **Successful search has no failure base.** State whether a count is an actual trace, a best case, or a worst case. Success can stop before any empty base is called.

28. **Fast power: exact multiplication count.** Fast-power exact costs depend on the exponent's bit pattern and the exponent-one base. Popcount alone or logarithm alone misses part of the work.

29. **Fast power with a zero-only base.** A mathematically harmless base change can alter exact operation counts. Derive them from the implemented operations.

30. **Duplicated power calls.** Calling an identical subproblem twice duplicates its computation unless reuse is explicitly established. Algebraic identity is not execution identity.

31. **A full binary call tree.** For a finite full binary call tree, internal calls equal leaves minus one. Balance is unnecessary; exactly two children is essential.

32. **Three-child recursion.** For a complete b-ary recursion of k edges, leaves are $b^k$ and calls are $(b^{k+1}-1)/(b-1)$; sequential depth is k+1.

33. **Fibonacci's exact call count.** Solve Fibonacci call counts with their constant term and bases. The returned Fibonacci value is not the number of calls.

34. **Fibonacci leaves and additions.** Naive Fibonacci additions are counted by internal call nodes; leaves return directly and do not add.

35. **Fibonacci depth is not its tree size.** An exponential call tree can have linear depth. Sequential space follows live paths and retained data, not cumulative calls.

36. **Fibonacci indexing across sources.** Normalize sequence indexing and base values before combining sources. Identical recurrence syntax does not fix identical initial values.

37. **Sharper exponential growth.** Distinguish a valid upper bound from a tight asymptotic characterization. Recursive branching alone does not select the exact exponential base.

38. **Cold memoization counts.** Cold memo Fibonacci distinguishes requests, misses, hits, additions, and stored entries. They are related but not identical counts.

39. **A warm cache changes the formula.** Memoized exact counts depend on initial cache contents. Always identify cold, partially populated, or warm state.

40. **A cache key loses essential state.** A memoization key must distinguish every state component affecting the result. Similar control location does not imply equivalent subproblems.

41. **Memoization and printed side effects.** Caching a value can suppress effects. State what behavior must be preserved before claiming a memoized implementation is equivalent.

42. **Arbitrary-precision Fibonacci cost.** Count operations and the cost of their operands separately. Linear arithmetic-operation counts can correspond to quadratic bit work.

43. **One child with a linear local loop.** The number of recursive calls is not the total running time when local work depends on input size.

44. **Sequential balanced split.** Balanced sequential recursion can have linear calls, logarithmic depth, and n log n work. Derive each requested quantity separately.

45. **Live variable-size arrays on a halving path.** Variable frame sizes must be summed along simultaneous live paths. Depth multiplied by the largest frame is often only a loose bound.

46. **Live arrays on a decrement path.** Linear recursion depth does not guarantee linear auxiliary memory when frames retain input-sized objects.

47. **Tail-recursive factorial contract.** An accumulator needs a generalized contract and invariant. Merely adding an extra parameter is not a correctness proof.

48. **Tail-call elimination is optional.** Tail position permits a transformation; it does not guarantee that C performs it. Claim constant storage only under a verified implementation or explicit loop.

49. **A continuation needs a phase.** An explicit stack must encode pending work and saved intermediate values, not merely a list of nodes to visit.

50. **Push order reverses visit order.** With a LIFO stack, push siblings in reverse of the intended visitation order. The base-action contract still matters.

51. **Mutual parity recursion.** For mutual recursion, prove a shared decreasing measure across the complete call cycle, and establish all base contracts together.

52. **Tree size and null calls.** A binary-tree traversal making both null-child calls has 2N+1 invocations. Count null calls explicitly and require an actual finite tree.

53. **A DAG can repeat structural occurrences.** Distinguish unique objects from repeated structural occurrences when recursion follows shared pointers.

54. **Hanoi's physical moves.** Hanoi's move count is $2^n-1$ for three pegs. Base invocations and physical moves are distinct objects.

55. **Hanoi's calls with a zero base.** Zero-base Hanoi has $2^{n+1}-1$ invocations and depth n+1. Removing zero calls changes exact invocation counts, not the puzzle's move requirement.

56. **Hanoi's one-disk base.** Hanoi's one-base and zero-base implementations have different call counts. Always check their admitted zero-input behavior.

57. **Hanoi legality is an inductive invariant.** For Hanoi, prove peg-state legality before counting moves. Size-order preservation is part of the subproblem contract.

58. **Hanoi timing with explicit units.** Invert the requested quantity with correct units. Physical-action counts should not be replaced by implementation call counts.

59. **All subsets: outputs and invocations.** Binary decisions over n positions produce $2^n$ complete choices and $2^{n+1}-1$ calls without pruning.

60. **The empty input has one subset.** The empty combinatorial object is often one valid answer, not absence of an answer. State its output policy explicitly.

61. **Total emitted subset elements.** Include output size in enumeration complexity. The cost of emitting a complete result may grow with its length.

62. **Undoing an included element.** Backtracking must restore the state promised to the caller. Correct leaf counts can coexist with corrupted outputs.

63. **Negative numbers invalidate a pruning rule.** Every pruning rule needs a proof under the data domain. A rule sound for nonnegative values can fail with negative values.

64. **A remaining-sum upper bound.** Prune when a proved completion bound excludes the target. State the bound, inequality, and domain rather than merely labelling a branch impossible.

65. **Retain success or restore everything?.** Backtracking restoration policy follows the output contract. Retaining one solution and enumerating all solutions require different success handling.

66. **Path marks versus global visited marks.** Current-path cycle prevention and global visited-state reuse are different algorithms with different output and cost contracts.

67. **Permutations: leaf count.** Permutation leaves are factorial for distinct positions, while output materialization adds a length factor.

68. **Permutations: all prefix calls.** Count every prefix level in permutation recursion. A leaf-only factorial count does not give total invocations.

69. **Duplicate values in permutation generation.** Repeated values and distinct positions define different permutation contracts. Deduplication must be implemented rather than assumed.

70. **Partition recurrence classes.** Derive counting recurrences by disjoint exhaustive classes and bijections. Unordered partitions are not ordered compositions.

71. **Partition bases meet at (0,0).** When base conditions overlap, evaluate their joint state explicitly. Empty constructions commonly require priority over failure guards.

72. **A small partition calculation.** Use a small independently listed instance to detect recurrence and base errors, while retaining the general proof.

73. **Koch replacement geometry.** Recursive geometry combines branch counts with length scaling. Distinguish final primitives, construction calls, and physical lengths.

74. **Floating-point accumulator reassociation.** Recursive-to-iterative transformations need arithmetic-model checks. Mathematical associativity is not a floating-point equivalence guarantee.

75. **Termination does not guarantee available stack.** Separate mathematical termination, arithmetic representability, and finite implementation resources. Each requires its own justification.

76. **Minimum signed integer and absolute value.** Domain normalization can overflow before recursive progress starts. Treat the minimum signed value explicitly.

77. **Restore a swap even after failure.** Restoration proofs compose across recursive levels. Each child must satisfy its own restoration contract before the parent's undo is sufficient.

78. **Nested calls are not parallel children.** Nested argument evaluation and recursive child branches are different structures. Determine when each body starts and finishes.

79. **A corrected reverse-stride contract.** For reverse-stride recursion, derive source and destination indices as functions of the copy count. Mathematical negative sentinels require compatible implementation types.

80. **A complete recursion audit.** Validate the language semantics and child progress before deriving a recurrence. A halving branch cannot justify logarithmic depth when another live path decreases by one.
