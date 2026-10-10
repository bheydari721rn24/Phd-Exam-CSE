# Complete end-of-chapter reasoning rules

1. Establish that the representation is a finite rooted tree before applying structural induction. Cycles and shared child ownership require separate identity checks; key comparisons alone do not certify a valid tree.

2. State the comparator contract before searching. Its order must stay stable and transitive; mutable keys or overflow in an integer difference can invalidate otherwise correct pointer algorithms.

3. A strict BST compares each node with every key in each descendant subtree. Checking only its immediate children misses ancestor-bound violations such as a large grandchild below a smaller root's left link.

4. Preserve both inherited interval bounds when descending. A left turn changes the upper bound and a right turn changes the lower bound; earlier ancestor bounds remain active.

5. Represent an absent interval bound explicitly. An extreme legal integer cannot serve as an exclusive bound beyond every legal key, and weakening strict comparisons admits unwanted duplicate nodes.

6. Declare the duplicate policy before applying formulas. A replacement dictionary, a counted multiset and separate duplicate nodes have different size changes, rank blocks and structural deletion requirements.

7. With edge height, an empty subtree has height minus one and a leaf has height zero. Convert a course's node-count height by subtracting one before comparing exact results.

8. Write path-time bounds as $O(h+1)$ under edge height. A singleton still requires a comparator call even though its height is zero, and an empty operation still has a null test.

9. For a nonempty n-node binary tree, minimum edge height is $\lceil\log_2(n+1)\rceil-1$ and maximum is $n-1$. Neither follows from root symmetry alone; the lower bound uses level capacity.

10. A finite n-node binary tree has n+1 null child positions. These external search gaps are not stored key nodes and must not be confused with actual leaves.

11. Count one comparator call per actual visited node only when the model uses a three-way comparator. Equality-plus-less-than source code can use more primitive comparisons on the same route.

12. Successful search at actual depth d uses d+1 comparator calls. Failed search ending at external depth g uses g calls because the final null test compares no stored key.

13. Search exclusion is justified by the whole-subtree invariant. A smaller query discards the root and its entire right subtree; correctness requires both matching-result soundness and missing-result completeness.

14. An absent-key insertion makes the failed search's null position an actual node. Its final depth equals the previous comparator count, while a subsequent successful lookup adds one comparison.

15. Inserting an existing key in a replacement dictionary changes its value rather than its node count. Adding size unconditionally on a replacement corrupts every later augmented query.

16. Assign every returned subtree root to its owning link. This includes the dictionary root, because empty insertion and root deletion change which object that outer field references.

17. Preserve exact map associations during deletion. Copying a successor's key without its value can maintain sortedness while returning the wrong value for a surviving key.

18. The minimum has no left child but can have a right child. Delete-min must return that right subtree so surviving larger keys are retained.

19. Floor and ceiling include an equal stored query. Strict predecessor and successor exclude it; an exact endpoint can therefore change the result by one entire key.

20. A missing query's floor and ceiling lie on its comparison path when they exist. Keep improving candidates while descending; returning the last visited node need not give either neighbor.

21. If a node has a right child, its successor is the minimum of that right subtree. That successor can have a right child even though it cannot have a left child.

22. Without a right subtree, climb until first reaching an ancestor from its left side. An ancestor reached from the right has a smaller key and cannot be the successor.

23. Mirror the successor rule to obtain predecessor. Merely stopping at any ancestor with a nonempty child subtree ignores the side from which the climb arrives.

24. Deleting an absent key must preserve content and size. A route to null is a successful absence diagnosis, not permission to remove a neighboring entry.

25. One-child deletion substitutes the entire child subtree into the former owning link. Its keys already obey all inherited bounds, which proves order preservation without reinserting them.

26. When maintaining parent pointers, repair the replacement child's parent and the root's null parent. Correct child order does not imply correct back-links.

27. In two-child successor deletion, remove the old successor occurrence after transferring its association. Leaving both occurrences violates strict node order and removes the wrong number of keys.

28. Handle an immediate-right-child successor separately in physical transplantation. Assigning its right link to the old right root would create a self-cycle because those objects are identical.

29. Association copying and physical transplantation have different identity effects. Specify which node objects and external references survive rather than inferring identity from the surviving key set.

30. Plain search plus successor removal follows a bounded downward route and costs $O(h+1)$. Counting the two path lengths as a product incorrectly invents a quadratic-height bound.

31. Predecessor replacement also preserves order for unique keys. An exact-shape question can nevertheless prescribe one method, so different valid deletion conventions need not produce the same preorder.

32. Release allocations only after preserving every pointer still needed. Clearing a local copied pointer does not clear the caller's owning field, and reading a released node's children is invalid.

33. Inorder is sorted only under an ordering invariant. Arbitrary binary-tree traversal follows the same visit rule without promising any numeric monotonicity.

34. For distinct keys in a finite binary tree, strictly increasing inorder is equivalent to global BST order. It does not certify ownership, parent pointers, stored sizes or expected content.

35. A full traversal visits n actual nodes in linear time even when height is logarithmic. Balanced search does not turn complete enumeration into a logarithmic operation.

36. Recursive traversal with two child calls per actual node makes exactly 2n+1 calls including nulls. Keep actual visits, calls and language stack frames as separate counts.

37. Streaming depth-first traversal retains unfinished ancestors in $O(h+1)$ space. Materializing its complete output additionally uses linear storage regardless of the recursion method.

38. Breadth-first queue storage depends on maximum level width, not only height. A perfect shallow tree can still require a queue containing a linear number of nodes.

39. In an iterative inorder scan every node is pushed and popped once. One next operation can be expensive while the whole retained-state scan remains linear in aggregate.

40. Preorder alone does not determine an arbitrary binary tree. Distinct-key inorder plus preorder or postorder determines it by locating each recursively chosen root's inorder position.

41. For a strict BST, a valid preorder alone suffices because inorder is already the sorted key order. This conclusion needs distinct node keys and the declared strict invariant.

42. A bounds-based preorder parser must consume the complete input. Returning a partial tree while leaving an invalid token unconsumed is construction without validation.

43. Parse postorder backward by root, right subtree, left subtree. Reusing forward preorder's child order changes the traversal contract and can reconstruct the wrong structure.

44. Repeated insertion can turn any distinct list into a valid BST without proving that list was its claimed preorder or level order. Validate the resulting traversal or use an interval parser.

45. Linear level-order reconstruction needs a breadth-first queue of allowed child slots. Once an earlier slot is skipped as empty, a later token cannot return to fill it.

46. State whether rank counts strict or inclusive predecessors. Their values differ by stored-query membership under unique keys, and by its multiplicity under counted occurrences.

47. Zero-based select requires an index below the total size. The insertion rank of a query above the maximum equals n and is a valid count but an invalid select index.

48. Select subtracts the entire left block plus the root before entering the right child. Omitting that root changes the residual index and returns the wrong successor key.

49. Stored subtree sizes must be refreshed along every changed ancestor route. Sorted keys can coexist with incorrect metadata, so rank and select need their own augmentation certificate.

50. Inclusive count on a nonreversed interval is $r(b)-r(a)+\mathbf{1}_{b\in T}$. The upper membership correction retains an equal upper endpoint; lower inclusion is already handled by subtracting strict rank.

51. Reject reversed intervals or explicitly return empty before applying normal range formulas. Algebraically subtracting their endpoint ranks can produce a negative number that is not a count.

52. Range reporting costs $O(h+m+1)$ for m results because boundary routes remain even with no output. An empty range in a chain can still require a linear descent.

53. Subtree sums support weighted prefix and interval queries by adding whole excluded blocks. Negative weights are permitted because the tree is ordered by keys, not by the weights.

54. A weight replacement preserves key order but changes aggregate sums. Refresh affected ancestors even when no pointer or key is modified.

55. A counted multiset stores mass as left mass plus count plus right mass. Distinct-node size and total occurrence mass answer different questions and cannot be substituted interchangeably.

56. Multiset select returns a node across its complete occurrence block. For count c, that block has c consecutive ranks, not one rank followed immediately by the right subtree.

57. Removing one occurrence from a count above one leaves the node intact. Structural deletion begins only when the last occurrence of that distinct key is removed.

58. During multiset two-child deletion, transfer the successor's complete count and remove its old node completely. Removing just one successor occurrence can duplicate both its key and its mass.

59. The external path identity $E=I+2n$ uses actual-node depths and null-gap depths. In that extended-tree accounting an actual stored leaf still contributes to I.

60. Uniform successful cost is $(I+n)/n$ only when queries are uniform over actual keys. Nonuniform successful probabilities require a weighted sum of individual depths plus one.

61. Uniform failed-gap cost is $E/(n+1)$ only when gaps are equally probable. Uniform numerical queries generally assign unequal probabilities to differently sized key intervals.

62. Combine successful and failed costs with their jointly normalized probabilities. Adding two separately conditional means without success/failure weights does not produce an unconditional expectation.

63. A fixed tree's producing insertion orders are exactly the ancestor-before-descendant permutations. Child subtrees can interleave arbitrarily because their comparisons never cross the root split.

64. The producing-order recurrence multiplies child counts by $\binom{n-1}{l}$. Treating each child as one contiguous block omits valid interleavings.

65. The hook formula $W(T)=n!/\prod_vs(v)$ counts a specified labeled distinct-key BST. Under uniform insertion permutations its shape probability is the reciprocal subtree-size product.

66. Catalan numbers count ordered shapes, not insertion permutations. A fixed sorted key set labels each shape uniquely, while several permutations may produce the same branching shape.

67. Chain directions may change at every level. There are $2^{n-1}$ chain shapes and producing orders on n distinct keys, not merely the increasing and decreasing permutations.

68. Uniform permutations and uniform Catalan shapes induce different probability distributions. Specify the model before reporting any average depth, average height or probability of a shape.

69. For random distinct-key insertion, a rank j is an ancestor of i exactly when it appears first in the sorted interval between them. That interval-first criterion gives the exact ancestor probability.

70. Linearity of expectation sums ancestor indicators without requiring independence. Do not assume independence for other tree events merely because a depth proof did not need it.

71. Under uniform permutations, expected fixed-rank depth is $H_i+H_{n+1-i}-2$. Add one for successful comparator cost and keep harmonic numbers indexed by the actual rank endpoints.

72. Expected internal path length is $2(n+1)H_n-4n$ in the random-permutation model. It also equals expected total absent-key insertion comparisons because later insertions leave existing depths unchanged.

73. Expected maximum depth cannot be inferred by taking the maximum of expected depths. Random-BST logarithmic height is a separate probability theorem; a mean-depth calculation alone does not prove it.

74. Direct midpoint construction from sorted distinct entries is linear because every node is allocated once. Ordinary midpoint-first dictionary insertion follows search routes and generally uses n log n work instead.

75. Sorted input to a plain BST creates a chain and quadratic total insertion comparisons. Its final inorder pass remains linear; the construction phase determines tree sorting's worst-case cost.

76. An LCA descent assumes both queried keys are present. Without membership, a stopping node is merely an interval split point and need not be an ancestor of actual queried entries.

77. A rotation preserves inorder by keeping the ordered blocks A, x, B, y, C in the same order. It also needs outer-root, parent-link and augmentation repairs to be a correct update.

78. Recompute the rotation's lower node before its new upper node. The upper aggregate depends on the lower node's new children, so reversing that order can leave stale metadata.

79. Morris traversal temporarily mutates child links and must restore every thread. Constant auxiliary storage does not make it appropriate for uncoordinated concurrent readers or early exit without cleanup.

80. A complete audit checks order, content, associations, ownership, outer-root links, optional parents, aggregate equations and cost conventions separately. Independent finite tests supplement the proofs but cannot guarantee correctness on every unseen question or workload.
