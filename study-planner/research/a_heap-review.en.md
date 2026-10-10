# Final reasoning rules

1. A priority queue is an interface; a binary heap is one implementation with complete shape and parent-child order.

2. In a min queue, a numerically smaller priority is served first. Reverse primary comparisons for a max queue.

3. Duplicate priorities are allowed. Live record identifiers must remain distinct if operations use handles.

4. FIFO ties require arrival metadata in the comparator; choosing the left child on equality is insufficient.

5. A comparator must remain consistent while records are stored. External mutation requires an explicit repair operation.

6. A nonempty complete binary tree has edge height $\lfloor\log_2 n\rfloor$, with a singleton at height zero.

7. Never evaluate the logarithm of zero to compute empty-heap height; use the declared empty convention instead.

8. A zero-based nonroot index has parent $\lfloor(i-1)/2\rfloor$ and potential children $2i+1,2i+2$.

9. A one-based nonroot index has parent $\lfloor i/2\rfloor$ and potential children $2i,2i+1$.

10. Every child access must be bounded by active size, not allocated capacity.

11. In a dense complete shape, a missing left child implies a missing right child.

12. Binary leaf count is $\lceil n/2\rceil$; the zero-based first leaf is $\lfloor n/2\rfloor$.

13. A nonempty complete binary tree has one single-child node exactly when its size is even.

14. Zero-based depth is $\lfloor\log_2(i+1)\rfloor$. One-based binary addresses encode structural left/right routes.

15. Heap order compares ancestors with descendants, and imposes no sibling or BST interval order.

16. A heap's inorder traversal is generally unsorted. Do not use a BST branch decision for heap membership.

17. The root is extreme by transitivity along every route, not because the entire array is sorted.

18. For distinct keys, the second extreme is among existing root children. Handle a lone child without a sibling access.

19. A distinct key of rank $k$ can have depth at most $k-1$; shallow depth alone does not determine rank.

20. An opposite extreme has a leaf representative. With duplicates, it can also have internal occurrences.

21. Without extra metadata, scanning the opposite extreme among independent leaf candidates is linear worst-case work.

22. Insert at the unique next complete position, then repair upward; selecting a convenient empty pointer position is not enough.

23. Sift-up stops at the root or the first parent relation that is legal under the full comparator.

24. A one-edge upward exception alone is insufficient for a general repair proof; account for the displaced parent's new children.

25. A strengthened grandparent condition or an equivalent hole invariant supplies the missing upward proof obligation.

26. Extract the root by saving its record, moving the final active record, shrinking size, and repairing the remaining prefix.

27. Extracting a singleton performs no repair and must clear its handle mapping without accessing an empty root.

28. Sift-down must promote the best existing child; choosing merely a child better than the parent can leave a sibling violation.

29. Equality may stop a numerical repair, but a changed arrival/identity tie field can still change comparator order.

30. A two-child repair level uses up to two priority comparisons; a one-child level uses only one.

31. A terminal failed priority comparison is real work even when no exchange follows.

32. Keep loop tests, priority comparisons, array assignments, record exchanges and initial root replacement in separate counters.

33. Sift-down's subtree proof assumes its child subtrees are already heaps; state the enclosing-parent obligation separately.

34. Bottom-up construction visits internal indices in decreasing order so child-subtree preconditions hold.

35. A size-$n$ node at zero-based index $i$ has subtree height $\lfloor\log_2(n/(i+1))\rfloor$.

36. Nodes with subtree height at least $j$ number $\lfloor n/2^j\rfloor$, including incomplete final levels.

37. The total downward height budget is $n-s_2(n)$, where $s_2$ counts binary set bits.

38. Bottom-up build uses at most $n-s_2(n)$ repair exchanges and at most twice that height budget comparisons under the chapter's code.

39. The safe comparison bound charges available heights, not twice the number of exchanges actually performed.

40. A valid already ordered heap can require zero construction exchanges and a linear number of certification/build comparisons.

41. Repeated insertion has a logarithmic-per-item worst case; it is a different builder from linear bottom-up heapification.

42. Different correct builders may produce different heap arrays from the same input multiset.

43. Heap construction has a linear comparison lower bound because its root identifies an extreme; it does not reveal a full sorted order.

44. A stable handle identifies a record, not its current array position. Every exchange must update both inverse entries.

45. Min-heap decrease-key repairs upward and increase-key repairs downward; max orientation reverses those directions.

46. Known-position deletion moves the final record and selects repair direction by its new parent relation.

47. If a replacement precedes its parent, it is already legal above the old entry's children; one upward repair suffices.

48. Deleting the final position needs no repair. Deleting an unknown identifier needs a separately priced lookup.

49. Direct identifier arrays give constant worst-case lookup within a bounded universe; hash lookup needs its expected-cost assumptions.

50. Array resizing can make one heap operation linear actual time even when storage cost is constant amortized.

51. Geometric growth has linear aggregate copy cost. Shrink hysteresis prevents alternating large copies near a threshold.

52. Comparison-model insertion and extraction cannot both have universal constant amortized bounds because together they would sort in linear work.

53. Ascending in-place heapsort uses a max heap in the active prefix and ascending final maxima in the suffix.

54. Shrink the active prefix before sortdown repair; extracted suffix entries are no longer tree nodes.

55. Standard early-stop heapsort has logarithmic-per-item worst-case work but can be linear when all priorities are equal.

56. Ordinary heapsort is unstable because root-last movements can reverse equal identities even without equal-key repair exchanges.

57. Constant auxiliary heapsort space applies to the iterative in-place implementation, not a separately allocated queue or recursive call stack.

58. Distinct-key heap counts use $H(n)=\binom{n-1}{L}H(L)H(R)$ with subtree sizes fixed by complete filling.

59. The left subtree receives the earliest last-level positions; do not split remaining nodes into equal halves blindly.

60. A uniform permutation is heap-ordered with probability $H(n)/n!$. This is not the probability distribution of a builder's outputs.

61. The product formula divides $n!$ by the product of actual subtree sizes. Duplicate counting requires a separate multiset argument.

62. A zero-based $d$-ary parent is $\lfloor(i-1)/d\rfloor$; children are $di+1$ through $di+d$, clipped by active size.

63. Exact $d$-ary height is $\lceil\log_d((d-1)n+1)\rceil-1$ for $n\ge1,d\ge2$; verify power boundaries with integer capacities.

64. Greater arity reduces height but increases child-selection work. Operation mix and machine costs determine the useful arity.

65. Retaining the largest $k$ stream entries uses a min heap of retained candidates so the root exposes the weakest survivor.

66. Nonmutating rank selection from an existing heap uses a second frontier queue and costs $O(k\log(k+1))$ under this algorithm.

67. Repeated extraction from the original heap costs $O(k\log n)$ and changes it. Do not claim those operations preserve the source.

68. Threshold pruning can decide whether at least $k$ keys qualify in $O(k+1)$ work; that decision does not itself select an exact rank.

69. A sorted-stream merge needs one unconsumed head per nonempty list; sequential accumulated merging has a different cost.

70. Two-heap median maintenance needs both size balance and cross-order between the lower and upper halves.

71. A rank-$j$ binomial tree has size $2^j$, root degree $j$, height $j$, and depth populations $\binom{j}{r}$.

72. Canonical binomial forest ranks are size's set-bit positions; equal ranks may coexist only during an explicitly unconsolidated step.

73. Canonical meld link count is $s_2(n)+s_2(m)-s_2(n+m)$. A three-tree carry must retain one tree and link the other two.

74. Singleton insertions from empty make exactly $N-s_2(N)$ binomial links; constant amortized linking assumes a carry-only implementation.

75. Amortized charges telescope with an initial-potential term. Nonempty initial states cannot silently discard that term.

76. Never cancel an unspecified big-O coefficient with a unit potential drop; normalize primitive work or scale the potential.

77. Fibonacci first-child loss marks a nonroot, second loss cuts it, and promoted or newly linked nodes clear their marks.

78. Ordinary Fibonacci decrease-key is constant amortized, extraction logarithmic amortized; cascades or lazy-root scans can be linear actual work.

79. Fibonacci degree-$d$ subtrees contain at least $F_{d+2}$ nodes. This bounds degree of every node, not global tree height.

80. A data structure choice must satisfy the entire requested interface, tie policy, lookup assumptions and latency requirement; a fast isolated operation is insufficient.
