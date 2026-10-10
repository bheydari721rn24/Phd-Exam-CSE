1. Define height before using a threshold. This chapter counts edges, gives an empty tree height minus one and a singleton height zero; a node-height convention shifts every Fibonacci index by one.

2. The AVL condition is recursive: every actual node must have child-height difference at most one. A root with equal child heights can hide violations lower down.

3. Strict inherited key order, ownership, balance and metadata agreement are separate certificates. Passing one does not prove the others, even when the drawing appears symmetric.

4. Positive balance means left-heavy only under the left-minus-right convention. Translate signs in an examination before selecting a repair table.

5. The exact minimum-node bases are $M_{-1}$=0 and $M_{0}$=1. Omitting the empty base corrupts the first nontrivial recurrence and its shifted closed form.

6. Minimum size at height h satisfies $M_{h}$=1+$M_{h-1}$+$M_{h-2}$. The equality is achievable by attaching minimal child shapes with those two heights.

7. With $F_{0}$=0 and $F_{1}$=1, the edge-height identity is $M_{h}$=$F_{h+3}$−1. Check the empty and singleton cases before copying a formula from another source.

8. A maximum AVL height for fixed n is established by consecutive minimum thresholds and an attainable-size argument. A necessary bound alone is not an existence proof.

9. Fixed-height AVL sizes have no gaps between the minimum and full binary capacity. The two child-height choices yield overlapping integer-sum intervals, as proved in the lesson.

10. Maximum binary capacity at edge height h is $2^{h+1}$−1. The minimum possible height for n keys comes from this capacity, while the greatest AVL height comes from the minimum recurrence.

11. The constant 1.44042 multiplies log base two in an asymptotic AVL height estimate. Its additive term and integer thresholds prevent treating the rounded estimate as an exact small-n answer.

12. A height-h minimum-node AVL shape has two independently oriented smaller extremal subtrees. Count those shapes with $S_{h}$=2$S_{h-1}$$S_{h-2}$, rather than a Catalan formula.

13. Counting all AVL shapes requires tracking both size and height. Sum child-count products only for height pairs differing by at most one.

14. A fixed ordered shape has one strict BST labelling by a fixed increasing key set. This does not imply that all shapes are equally likely under a balancing insertion algorithm.

15. Actual leaves and null search gaps are different objects. A minimum height-six AVL tree has thirteen actual leaves and thirty-four null gaps.

16. A rotation's unconditional purpose is preserving the inorder association sequence through a local link transformation. It does not unconditionally preserve AVL balance.

17. Save and transfer the middle subtree during a rotation. Swapping pivot keys without preserving its interval and association values is not the specified pointer operation.

18. Attach the rotation's returned root to the caller or global root. Retaining the demoted root can disconnect the promoted association and its remaining subtree.

19. Refresh the demoted node before the promoted node. The new parent's metadata depends on the new child and must not read its old height or size.

20. Parent pointers need assignments at the old parent, both pivots and the transferred middle subtree. A correct child-link drawing alone does not certify parent-link consistency.

21. The local AVL repair contract assumes one child changed height by at most one from a formerly valid subtree. Two arbitrary AVL children do not limit the new root imbalance to magnitude two.

22. LL/LR/RR/RL names describe route geometry, not primitive rotation names. An LL insertion repair uses a right rotation, and RR uses a left rotation.

23. At the lowest insertion imbalance, the growing heavy child cannot have balance zero. If it had become equally tall on both sides, its maximum height would not have increased.

24. A standard AVL insertion has one repair site and at most two primitive rotations. Its repaired subtree recovers its pre-insertion height, so higher ancestors do not acquire a new imbalance.

25. A double rotation includes two primitives and may have an unbalanced intermediate checkpoint. The completed double repair, rather than each individual intermediate tree, carries the AVL postcondition.

26. Existing-key dictionary replacement changes no structural height. Value-dependent aggregates may nevertheless need ancestor refresh and must not be dismissed as unchanged.

27. An insertion's constant rotation count does not make the whole operation constant-time. The search and metadata return routes still have logarithmic worst-case length.

28. Two-child deletion begins its height repair at the physically removed successor position. The overwritten target association and freed/relinked position are different semantic objects.

29. Deletion allows a balanced heavy child at the first imbalance. For a left-heavy root, heavy-child balance zero belongs to the single-right-rotation branch.

30. In deletion's zero-heavy-child case the repaired subtree retains its pre-deletion height. Height loss stops, although size, sum and other changed aggregates still propagate.

31. Deletion with an outer-heavy child uses one primitive and loses one subtree height level. Revisit the parent because another imbalance can arise there.

32. Deletion with an inner-heavy child uses two primitives and also can lose one level. The child balance chooses this case; the deleted key's comparison is insufficient.

33. AVL deletion can repair several ancestor sites and use logarithmically many primitives. Do not transfer the constant insertion rotation bound to deletion.

34. A strict outer-height test valid for an insertion-only helper is unsuitable for deletion equality. Some tiny equality cases happen to survive a double rotation, but a general counterexample still invalidates the helper.

35. Absent-key AVL deletion preserves associations, size and height. A singleton's successful deletion returns null and gives completed height minus one.

36. Copy the successor's full key/value association. Copying only its key preserves apparent key order but breaks the dictionary's value mapping.

37. Full certification is linear and is not part of a logarithmic production update. Running it after every insertion makes the total n-insertion audit workload quadratic.

38. Subtree-size refresh after rotation uses the new children. The promoted total equals the old rotated-subtree total, but the demoted subtotal usually changes.

39. Strict rank counts keys smaller than the query, including absent queries. Zero-based select uses a valid index from zero through size minus one and is not the same operation.

40. Inclusive range count is rank(upper) minus rank(lower), plus the presence indicator of the upper endpoint. This formula assumes correctly maintained structural sizes and ordered distinct keys.

41. Range reporting requires output-sensitive work O(log n+k). A logarithmic route guarantee does not eliminate the time to emit k associations.

42. Fixed-size metadata preserves logarithmic update complexity only if recomputation from the node and its children is constant-time in the declared cost model.

43. Global ranks can change at every old entry after inserting a new minimum. Store local subtree counts rather than claiming constant-time maintenance of every global rank.

44. Sorted vectors of whole subtree contents do not satisfy the fixed-size augmentation hypothesis. They can require linear movement during a large-node refresh.

45. Closest-pair metadata needs child minima/maxima and best internal pairs. Only adjacent cross-boundary pairs with the root can beat the children's internal candidates.

46. A subtree with fewer than two keys has no closest pair. Use an explicit no-pair sentinel; assigning a zero gap would invent an impossible winning pair.

47. Priority argmax and key median use different order information. A balanced key tree needs separate size and priority-witness aggregates, with an explicit tie rule.

48. Key order is not an arrival/list-position tie order. Stable position labels or another specified representation must support the intended maximum-priority tie semantics.

49. Counted multisets use occurrence mass for selection and rank blocks. Structural size still counts distinct key nodes and cannot substitute for that mass.

50. Removing one occurrence from a positive multiplicity does not change height. Its mass aggregate changes along the route even without a node removal or rotation.

51. A k-key internal multiway node has k+1 ordered child intervals. Count key slots and child slots separately before deriving capacity.

52. A 2–3 tree permits one or two keys per node and uniform actual-leaf depth. Its height-H key bounds are $2^{H+1}$−1 and $3^{H+1}$−1.

53. A 2–3–4 tree permits one through three keys per node. Its maximum height-H key capacity is $4^{H+1}$−1, while its minimum stays the all-two-node bound.

54. Minimum-degree b means nonroot key capacity b−1 through 2b−1 in this chapter. Another author's maximum-child order convention must be translated before using the same letter.

55. A B-tree root has a smaller minimum occupancy than other nodes. Its minimum height-H total is 2$b^{H}$−1, not the total obtained by imposing the nonroot minimum at the root.

56. Multiway CPU work and block transfers are different resources. Binary node search can reduce comparisons without removing packed-entry movement or disk reads.

57. The continuous minimizer of b/ln(b) is e; compare integer neighbors rather than flooring it automatically. The stated scalar objective favors three, not a universal practical fanout.

58. Bottom-up 2–3 insertion promotes an overflow's middle key and may repeat upward. Only splitting its root raises every leaf depth together.

59. Top-down 2–3–4 insertion splits a full child before descending, under a nonfull parent. A legal full leaf need not be split until encountered by the next relevant descent.

60. Different top-down and bottom-up variants can produce different valid shapes from the same keys. Compare invariants and declared schedules rather than requiring shape identity.

61. Multiway borrowing must pass through the parent separator and transfer the proper boundary subtree. A direct nonadjacent sibling-key move can break interval order.

62. Merging joins a minimal child, separator and sibling. Replacing an emptied root by its sole child decreases all surviving leaf depths equally.

63. Top-down deletion can restructure even while searching for an absent key. Check membership first when the interface promises no structural change on absent deletion.

64. General red-black trees permit right-red links and black nodes with two red children. Those conditions alone are not violations unless the stricter LLRB variant is specified.

65. Beta here counts actual black nodes including a black starting node and excluding null. Child $\beta$ values must agree; the null base is zero.

66. Translate a black-height convention at both endpoints. A count excluding a red start and including its final sentinel is one greater than $\beta$ at that red node.

67. Collapsing red children into their black parent gives a 2–3–4 cluster. No red-red edge limits cluster size, and equal black paths give uniform multiway depth.

68. With a black root and $\beta$ b, actual key count lies between $2^{b}$−1 and $4^{b}$−1. These necessary bounds do not by themselves count colored trees or prove every proposed extremum achievable.

69. Root-null routes visit between b and 2b actual nodes. Their terminal-null link length agrees with that count, while actual edge height subtracts one.

70. In classical insertion, a red new leaf preserves black path counts and may create only red adjacency internally. A new black nonroot leaf would add an unmatched black unit.

71. A classical red-uncle insertion recolors and can propagate upward without rotations. Root blackening changes all root-null routes equally.

72. A black-uncle triangle must first become a line before the final recolor/rotation. Classical insertion uses at most two primitives, with its proof tied to that schedule.

73. Classical deletion tracks the original color of the physically removed position. A red successor removal does not create a black deficit merely because the target was black.

74. A surviving red replacement can absorb a removed black unit by being blackened. No rotation is required under the valid one-child removal hypotheses.

75. Double black is a virtual deficit ledger, not a persistent third color. It identifies the one route that still needs a black unit while ordinary subtrees remain valid.

76. Near/far nephews are relative to the active deficit side. Mirror both recolors and rotation directions when the active node changes from left to right.

77. Classical deletion's only upward-propagating case uses no rotation. Red-sibling conversion, near-nephew conversion and final absorption yield at most three primitives overall.

78. Completed 2–3 LLRB adds no right-red link and no persistent four-node. Its colored rotations and toggling flips implement a distinct normalization schedule with logarithmic total primitive work.

79. LLRB deletion prepares a red resource before descending into a minimal child. The terminal-minimum null return depends on this invariant and is not valid for arbitrary ordinary BST deletion.

80. Independent finite checks and clear source reconciliation strengthen a proof-based chapter. They do not certify literal universal infallibility, an exact examination rank or performance on every unseen question outside the stated contracts.
