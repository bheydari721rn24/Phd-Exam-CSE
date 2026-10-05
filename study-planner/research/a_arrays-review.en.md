# Examination rules: formulas, conditions, and counterexamples

1. **Separate interface from representation.** If a question states only “sequence,” no physical access cost follows. A rank lookup in an array is constant; the same interface on a singly linked list needs traversal. Name the storage model before selecting a complexity.

2. **Separate length from capacity.** Use $0\le n\le C$. A length-8 capacity-16 array has eight valid retrieval ranks and nine insertion positions, not sixteen live elements. Spare slots are storage, not members of the sequence.

3. **Respect the lower bound in addresses.** For slot size b and lower bound L, address is $B+b(i-L)$. With L=−3 and i=5 the offset is 8b. Multiplying the declared index directly by b is wrong unless L=0.

4. **Distinguish a slot from its payload object.** Copying n pointers is $\Theta(n)$ even if the referenced objects are large. Deep-copying objects instead costs their total copied size; never transfer the word-copy theorem without its premise.

5. **Count insertion shifts exactly.** With spare capacity, stable insertion at rank i shifts $n-i$ old slots and adds one new-value write. At i=n it shifts zero; at i=0 it shifts n. These endpoint checks expose an erroneous off-by-one formula.

6. **Count deletion shifts exactly.** Stable deletion at rank i shifts $n-i-1$ old slots. Deleting the last live rank shifts zero. Clearing a vacated reference slot is a separate write and must follow the requested counting convention.

7. **Copy overlapping rightward ranges backward.** If destinations overlap unread sources to their right, a descending source loop preserves old values. Inserting into `[3,5,7]` with an ascending loop propagates 5 and loses 7.

8. **Copy overlapping leftward ranges forward.** A left shift reads from a larger rank than it writes. Its ascending loop preserves the unread suffix. Applying the insertion direction to deletion can overwrite an unread source.

9. **Order is part of deletion's contract.** Swap-with-last permits constant-time deletion at a known array index only for an unordered collection. It cannot implement stable sequence deletion, because it changes relative order.

10. **Update n between operations.** An insertion into length 17 makes length 18 before the following deletion. Using 17 again undercounts the latter shift loop. A multistep question requires a state trace.

11. **Repeated front insertion is quadratic.** With ample capacity, m insertions from empty shift $m(m-1)/2$ slots. No resizing theorem removes these shifts; geometric growth adds only a lower-order linear term.

12. **Repeated insertion at one rank reverses the new block.** Inserting x1, then x2, at the same rank puts x2 before x1. If k values are inserted into original length n at fixed i, shifts total $k(n-i)+k(k-1)/2$.

13. **Uniform insertion is an average over n+1 positions.** Expected shifts are n/2 only when those positions are equally likely. A distribution favoring the front raises the expectation; this is not amortized analysis.

14. **Uniform deletion averages over n live ranks.** For n>0, expected shifts are $(n-1)/2$. The n+1 insertion denominator does not apply. Worst-case deletion still shifts n−1 elements.

15. **Use the final doubling capacity to sum copies.** From capacity one, m≥1 appends finish at $C=2^{\lceil\log_2m\rceil}$ and copy C−1 old slots. For m=13, C=16 and copies=15; assuming m−1 copies would be wrong.

16. **State whether copies count reads and writes.** A resize moving C slots costs C copies but may cost 2C accesses. For 13 appends, 15 copies plus 13 appended writes give 28 writes, not 43 unless reads are also charged.

17. **The last append need not be the worst.** In 100 capacity-one doubling appends, append 65 costs 65 writes and append 100 costs one. Find growth-triggering positions rather than using the final length as every operation's cost.

18. **Geometric growth requires a fixed factor above one.** For exact factor g>1, copies are $(C_{final}-C_0)/(g-1)$. A factor depending on n and approaching one requires a new summation; the denominator is not a universal constant.

19. **Rounding changes exact counts.** With $C'=\lceil1.5C\rceil$, actual capacities must be traced. A continuous geometric sum can justify an asymptotic bound but may give the wrong integer copy count.

20. **Additive growth has an arithmetic sum.** Initial capacity h and growth h give q=$\lceil m/h\rceil-1$ expansions and $hq(q+1)/2$ copies. With h=10 and m=101, q=10 and copies=550.

21. **Sublinear increments require a scale argument.** Increasing capacity by about $\sqrt C$ creates only about $\sqrt C$ spare positions after C copies. Total copying to N is $\Theta(N^{3/2})$, not linear; the growth increment is not a fixed fraction.

22. **Amortized cost is deterministic sequence accounting.** Doubling gives constant amortized append cost for every append sequence under the model. No distribution on keys is needed. A worst individual append remains linear.

23. **Include the initial potential.** For $\Phi=2n-C$ at empty capacity one, $\Phi_0=-1$. Shift it by one or isolate the first operation; do not claim an initial value of zero in the telescoping identity.

24. **Potential is bookkeeping.** Actual cost equals amortized cost minus potential change. A decrease in potential pays for a resize; it does not imply the machine executes fewer copies on that operation.

25. **Separate middle shifts from capacity overhead.** Dynamic-array insertion at rank i costs its stable shifts plus any resize work. An amortized constant expansion overhead does not make arbitrary insertion constant.

26. **Half-full shrinking can thrash.** Grow a full C buffer, delete once to half of 2C, shrink, then append again. The state repeats with linear copies per pair. This is an adversarial counterexample, not a rare-input argument.

27. **Quarter-full shrinking leaves hysteresis.** Shrinking at n=C/4 to capacity C/2 leaves the new buffer half full. Many ordinary updates separate opposite resize events. The threshold gap is the mechanism behind the amortized proof.

28. **Use the correct potential branch.** For doubling with quarter shrinking, dense states use $2n-C$ and sparse states use $C/2-n$. At n=C/2 both equal zero; a one-branch formula alone does not pay for both growth and contraction.

29. **Contraction copies live slots.** Shrinking from capacity 64 at length 16 copies sixteen values, not sixty-four. With one deletion counted, actual cost is 17 and amortized cost is 2 in the specified potential model.

30. **Minimum capacity is a boundary case.** A capacity-one structure must not shrink to zero and make later doubling stay zero. Keep a positive minimum and treat its bounded work separately.

31. **Peak memory includes both buffers.** Separate-allocation doubling of a full C buffer uses 3Cb slot bytes while copying. Final storage uses only 2Cb. A peak-allocation question cannot use the final figure.

32. **Use the correct slack denominator.** After doubling and appending, unused slots are C−1 out of 2C allocated. The unused fraction is $(C-1)/(2C)$, whereas slack relative to live values is $(C-1)/(C+1)$.

33. **Buffer movement invalidates physical addresses.** Preserved logical rank does not preserve an old pointer into the released buffer. A saved index must be resolved again and may itself change meaning after middle mutations.

34. **Fusing copy and shift changes exact work.** A resize insertion can copy each old value directly to its final position, using n+1 writes. Copying unchanged ranks and then shifting uses n+(n−i)+1; name the implementation.

35. **Allocation assumptions must be explicit.** Slot copying may be linear, while allocator initialization or a destructor has a different cost. The simple model excludes those costs unless the problem supplies them.

36. **A singly linked rank needs a path.** Rank i needs i successor traversals from head. The time including payload access is $\Theta(i+1)$, so rank zero is constant rather than “zero time.”

37. **A known predecessor removes search.** Inserting after p needs two link writes once p is supplied. Inserting at arbitrary rank i must first locate the predecessor. Do not answer the easier handle problem when the question supplies an index.

38. **Initialize the new successor before publishing the node.** For P→Q, do X.next=Q before P.next=X. Reversing these statements without a saved Q handle produces X.next=X and a self-cycle.

39. **Tail caching accelerates append, not tail removal.** A singly linked tail pointer gives the last node but no predecessor. For n>1, preserving identity while removing the tail still requires linear search.

40. **A second-last cache is not a complete remedy.** One deletion consumes that cached predecessor. Repeated deletion needs predecessors of newly exposed nodes, which are not available from two endpoint handles alone.

41. **Cached size is an invariant.** It must equal the number of reachable real nodes. A stale value can reject a valid last rank or permit invalid access, making the defect behavioral rather than merely slow.

42. **State the empty-tail convention.** With a head sentinel, empty tail may be the sentinel or null. Both work if used consistently. A released last node must never remain cached as tail.

43. **Sentinel values are not sequence elements.** A sentinel simplifies boundary links but is excluded from n and from predicate tests over data. A list with n real nodes and one sentinel allocates n+1 nodes.

44. **Save a victim's successor while it is alive.** Reading next after freeing a node is invalid even if memory bits look unchanged. Detach, release, and advance through a saved successor handle.

45. **The node-only trick changes identity.** Copying a successor payload and deleting that successor can mimic a value-sequence deletion only under restrictive contracts. It cannot delete a tail or preserve external identity handles.

46. **Doubly linked adjacency has two equations.** Completed updates must restore x.next.prev=x and x.prev.next=x. A correct forward scan alone cannot expose a broken backward link.

47. **Count required and optional pointer writes separately.** DLL insertion uses four link writes; unlink uses two neighbor writes. Clearing a removed node's fields adds two, and updating size adds metadata work.

48. **Circular empty lists are self-linked.** The sentinel satisfies S.next=S.prev=S. After deleting a singleton, both sentinel links must return to S; leaving one attached to the victim breaks the invariant.

49. **Circular traversal stops at identity.** A scan terminates on the sentinel, not null. In an empty list the first cursor equals the sentinel and no data value should be processed.

50. **Known endpoints make range rewiring constant.** Moving a DLL range needs six boundary writes, independent of its length. Determining unknown range length for cached sizes still takes traversal; total cost may be linear.

51. **Same-list splice needs a destination precondition.** A destination inside the moved range is not an ordinary external insertion gap. Reject it or define a no-op; blindly applying cross-list links may form a disconnected cycle.

52. **Intermediate states and publication differ.** Four DLL insertion writes can temporarily break bidirectional consistency. Exclusive access permits this; concurrent readers require a synchronization design beyond the sequential proof.

53. **Iterative reversal preserves two disjoint regions.** The reversed prefix and untouched suffix together contain every original node. Saving nxt before changing cur.next is what preserves the untouched region.

54. **Count the reversal's null write.** The original head's next is changed to null. Reversing n nodes therefore writes n next fields, not n−1, even though only n−1 links initially joined real nodes.

55. **Cached tail changes under reversal.** Save the old head as the new tail for a nonempty list; new head is the final prev handle. Size remains unchanged. Empty input preserves the chosen empty convention.

56. **Reverse printing is not pointer reversal.** A recursive routine can print values in reverse without writing links, but ordinary recursion uses linear stack space. Short source code does not imply constant auxiliary memory.

57. **Floyd compares after moving.** Initial equal head handles do not prove a cycle. Guard fast and fast.next before the two-step move, then compare identities after a complete iteration.

58. **Compute the first positive meeting multiple.** With speeds one and two, meeting time is $\lambda\max(1,\lceil\mu/\lambda\rceil)$. A pure seven-cycle meets after seven iterations, not zero.

59. **Meeting offset subtracts the prefix.** At t iterations, slow's offset from entry is $(t-\mu)\bmod\lambda$. For μ=13, λ=5, t=15 gives offset 2. Using t modulo λ would incorrectly report entry.

60. **Reset works because t is divisible by λ.** After resetting one cursor to head, μ simultaneous one-link steps bring both to entry. The proof uses the modular meeting condition, not a visual coincidence.

61. **Measure a positive cycle lap.** Starting a length cursor at the meeting node requires at least one advance. A self-cycle has length one; testing equality before movement would return zero incorrectly.

62. **A different fast speed changes the congruence.** Speed r gives $(r-1)t\equiv0\pmod\lambda$ and period $\lambda/\gcd(r-1,\lambda)$. This may detect a cycle without validating the usual entry-reset phase.

63. **Count Floyd's phases independently.** Standard detection uses 3t successor advances; reset uses 2μ; length measurement uses λ. Their sum excludes extra guard reads unless the cost model charges them separately.

64. **Repeated list get calls hide a quadratic sum.** Visiting get(0),…,get(n−1) from head follows $n(n-1)/2$ links. Keeping one cursor makes a full scan linear; cached size does not create random access.

65. **Key comparisons do not count midpoint traversal.** Binary search on a list may use logarithmic comparisons and linear or worse pointer work. Global-head midpoint lookup can give $\Theta(n\log n)$ for a search above every key.

66. **The kth-from-end convention matters.** With k=1 meaning last, the answer's rank is n−k. The gap method follows n lead links and n−k lag links, counting tail-to-null; k=0 is not valid under this convention.

67. **Specify which even middle is wanted.** Slow=head, fast=head, and the usual two-link guard returns rank floor(n/2), the second middle for even n. Different initialization may return the first.

68. **Stable merge chooses left on equal keys.** This preserves equal-key order relative to the concatenated left-then-right input. Sorted values alone do not establish stability of labeled objects.

69. **Merge comparison bounds require positive inputs.** For lengths m,n>0, head comparisons range from min(m,n) to m+n−1. If one list is empty, zero comparisons suffice; blindly applying m+n−1 is wrong.

70. **Destructive merge requires disjoint nodes.** Shared tails can cause a node to be selected twice and links to cycle. Sortedness and acyclicity of each separate input do not establish disjoint ownership.

71. **Compaction's write cursor never leads read.** After processing r old positions, w survivors satisfy w≤r. That inequality prevents overwriting unread input. Assigning all survivors gives k writes; skipping self-assignments changes the count.

72. **Normalize rotations and handle empty input first.** For n>0, replace k by k mod n. If the result is zero, do nothing. Computing modulo n for n=0 is invalid.

73. **A rotation needs both connection and cut.** Connecting old tail to old head creates a temporary cycle; breaking the new tail's successor restores acyclicity. Save the new head before the cut or it becomes unreachable.

74. **Intersection means shared objects.** Equal numeric suffixes allocated separately do not intersect. The two-switch method compares handles and assumes acyclic immutable topology during its run.

75. **Round node storage to alignment.** For payload d, p pointers of w bytes, and alignment a, node size is $a\lceil(d+pw)/a\rceil$ before headers. With d=13,w=8,a=8, SLL and DLL sizes are 24 and 32.

76. **Block-span arithmetic includes starting offset.** Reading n>0 consecutive slots from offset r in an L-slot block touches $\lceil(r+n)/L\rceil$ blocks. Twelve slots from offset five in a sixteen-slot block touch two blocks, not one.

77. **Locality depends on placement.** A linked list can occupy one block per node or use a compact pool. The RAM bound alone cannot predict cache misses; count blocks under an explicit placement and initial-cache model.

78. **Outer-product support needs the algebraic domain.** Over reals, nnz(abᵀ)=nnz(a)nnz(b). Modulo six, 2·3=0 is a counterexample. Treat the field assumption as part of the formula.

79. **Factorization and a general matrix interface differ.** Two factors store one outer product compactly, but arbitrary addition can yield rank two. Orthogonal row/column links answer a general traversal requirement that one circular successor chain does not.

80. **Select a structure from the supplied operation arguments.** Rank-heavy workloads favor direct indexing; handle-heavy deletion favors DLLs. If an option says O(1), check whether searching, range length, payload copying, allocation, and ownership are excluded explicitly. A correct local pointer count is not always the cost of the whole requested operation.
