### 1. Exact thresholds rather than a rounded logarithm

Find the largest possible AVL edge height for 50 distinct keys. Give the two thresholds that certify it.

#### Solution

Start with $M_{-1}$=0 and $M_{0}$=1. Applying $M_{h}$=1+$M_{h-1}$+$M_{h-2}$ gives $M_{5}$=20, $M_{6}$=33 and $M_{7}$=54. Fifty keys can reach height six but cannot reach seven, since 50<54. The upper capacity at height six is 127, so a minimal height-six shape can be filled further while preserving that height; alternatively an independently enumerated valid construction supplies the witness. Thus the maximum is **six**. The leading constant 1.44042 is useful asymptotically but does not establish this exact integer result.

### 2. A thousand keys and both extremal heights

Determine the minimum and maximum possible edge heights of an AVL tree with exactly 1000 nodes.

#### Solution

A binary tree of height eight holds at most 511 keys, while height nine holds at most 1023. A recursive midpoint construction on 1000 sorted keys is AVL and has height nine, attaining the lower bound. For the upper bound, $M_{13}$=$F_{16}$−1=986 and $M_{14}$=$F_{17}$−1=1596. Hence no height above 13 is possible. Filling suitable available positions of a minimal height-13 AVL shape yields 1000 nodes without increasing height or breaking balance; the shape-count recurrence also certifies attainable sizes. The height interval is therefore **9 through 13**, inclusive. Both bounds count actual nodes with empty height minus one.

### 3. A million-key height calculation

An AVL tree has one million keys. Find its greatest possible height and the maximum number of actual key comparisons on a search route of that height.

#### Solution

The relevant Fibonacci values are $F_{30}$=832040 and $F_{31}$=1346269. Therefore $M_{27}$=832039 and $M_{28}$=1346268. One million lies between them, so the maximum edge height is **27**. A deepest actual node lies after 27 edges and requires **28** key comparisons including the root. An unsuccessful search through a deepest missing child also compares 28 actual nodes; the null sentinel adds no key comparison. Confusing height with comparisons produces an off-by-one error. Logarithmic height is a worst-case upper guarantee, not a claim that every query costs 28.

### 4. Prove the Fibonacci shift

Under empty height minus one, prove $M_{h}$=$F_{h+3}$−1. Translate the result to a convention using empty height zero and singleton height one.

#### Solution

For h=−1, $F_{2}$−1=0; for h=0, $F_{3}$−1=1. If the identity holds at the two smaller heights, then 1+$M_{h-1}$+$M_{h-2}$=$F_{h+2}$+$F_{h+1}$−1=$F_{h+3}$−1. This completes induction. In the shifted convention H=h+1, replace h by H−1 to obtain $F_{H+2}$−1. The shapes and key counts have not changed; only the height index changes. Reusing the old h+3 subscript with the new height variable would overcount even a singleton. Base cases are part of the proof, not optional notation.

### 5. The logarithmic constant has a domain

Derive the AVL leading height coefficient relative to log base two and explain why floor(1.44042 $log_{2}$ n) is not an exact maximum-height formula.

#### Solution

Writing $M_{h}$+1=$F_{h+3}$, the Fibonacci characteristic roots give growth proportional to $\phi^{h+3}$, up to a bounded smaller-root term. Taking logs gives h=$\log_{\phi}$ n+O(1) at the extremal thresholds. The change-of-base coefficient is 1/$\log_{2}$ $\phi$, approximately **1.44042**. The hidden additive term depends on the shift and the factor sqrt(5); the small oscillating term and integer threshold matter as well. At n=1 the approximate formula floors to zero, but its accidental success there is not a proof. For n=2 it floors to one; again use $M_{h}$ thresholds to establish an exact result. Asymptotic equivalence preserves leading growth, not every integer answer.

### 6. Count the sparsest AVL shapes

How many ordered AVL shapes have the minimum number of nodes at edge height four? How many have the minimum at height five?

#### Solution

At every internal extremal root, child heights are h−1 and h−2 and can be assigned to either side. Thus $S_{h}$=2$S_{h-1}$$S_{h-2}$, with $S_{-1}$=$S_{0}$=1. Compute $S_{1}$=2, $S_{2}$=4, $S_{3}$=16, $S_{4}$=128 and $S_{5}$=4096. The required counts are **128** and **4096**. Their node counts are $M_{4}$=12 and $M_{5}$=20. These are ordered shapes, so a left/right reflection is counted separately unless identical; distinct child heights prevent identity at an extremal internal root. A fixed increasing key set labels each shape uniquely. This does not count generating insertion permutations after rebalancing.

### 7. Leaves in a minimum-node AVL tree

Find the number of actual leaves in a minimum-node AVL shape of height six. Explain why this number is independent of its left/right orientation choices.

#### Solution

Let $L_{h}$ count leaves in the extremal shape. The bases are $L_{-1}$=0, $L_{0}$=1 and $L_{1}$=1: the two-node minimal shape has only one actual leaf. For h≥2 both child subtrees are nonempty and $L_{h}$=$L_{h-1}$+$L_{h-2}$. The sequence at heights zero through six is 1,1,2,3,5,8,13. Thus there are **13 leaves** among $M_{6}$=33 nodes. Orientation changes which side each smaller tree occupies, but does not change their leaf counts, so induction establishes independence. Null search gaps would instead number 34 and must not be confused with the actual leaves.

### 8. All AVL shapes on five keys

Count all ordered AVL shapes on five distinct keys. Give their root split sizes and heights.

#### Solution

The root has four remaining nodes. Splits 0/4 and 4/0 are invalid because an empty child has height minus one while a four-node AVL child has height two. Splits 1/3 and 3/1 are valid: the singleton has height zero and the unique balanced three-node subtree height one, contributing one shape each. Split 2/2 is also valid; each two-node child has two orientations and height one, contributing 2×2=4. Summing gives **six** shapes, all of height two. The root key is determined by the left size, so these are also the six labelled BSTs on any fixed increasing five-key set.

### 9. Seven keys: perfect is not the only balanced shape

Count all ordered AVL shapes on seven keys and partition the answer by edge height.

#### Solution

A height-two tree with seven nodes must be perfect, contributing one shape. Height three has minimum $M_{3}$=7, so every such tree is extremal and contributes $S_{3}$=16. A height above three needs at least $M_{4}$=12 and is impossible. Hence the total is **17**, partitioned as one height-two and sixteen height-three shapes. A root that splits 3/3 contributes the perfect shape; the extremal height-three roots split 4/2 or 2/4 with the valid smaller child shapes. Counting all $C_{7}$ Catalan shapes would ignore the balance requirement.

### 10. Root balance misses a lower violation

Construct a strict BST whose root has balance factor zero but which is not AVL. Give true heights and an offending node.

#### Solution

Use root 40. Its left branch is 20 with left 10 with left 5; its right branch is 60 with right 70 with right 80. Each root child has height two, so B(40)=0 and root height is three. Node 20 has left height one and empty right height minus one, giving B(20)=2; node 60 has the mirror violation −2. Inorder is 5,10,20,40,60,70,80, so ordering is valid. This witness separates strict BST order, the root-only height test and the recursive AVL certificate. Every node's balance is required.

### 11. Cached height corruption

In a perfect seven-key AVL tree, the root cache incorrectly says height one, while its two child caches correctly say one. Can a cache-only balance test certify the representation? Give the correct linear audit.

#### Solution

The root's child difference is zero, so testing only cached balance would accept that local check even though the root's true height is two. A parent relying on the false root cache could then choose an incorrect repair. The audit recursively obtains true child heights, tests their difference and verifies stored height equals one plus their maximum; it returns the true value upward. The root mismatch is detected at the final return. Combining inherited key intervals, metadata and ownership checks certifies the representation in linear time. Accepting an apparently balanced cache is not equivalent to proving the cache represents the actual tree.

### 12. The rotation contract counterexample

Right-rotate the perfect three-key tree with root 20 and children 10,30. Does ordering survive? Does AVL balance survive? Identify the missing contract condition.

#### Solution

The result is root 10, with right child 20 whose right child is 30. Inorder remains 10,20,30, so the BST ordering and content conditions survive. True heights are zero at 30, one at 20 and two at 10; B(10)=−2. The result is **not AVL**. Having two valid AVL children before an arbitrary rotation does not suffice for an AVL postcondition. A specialized right-repair must additionally constrain the root imbalance and the heavy-child configuration. A structural primitive instead promises ordering/content preservation and correct refresh, while the repair proof supplies balance.

### 13. Why refresh order matters

Let z=30 have left child y=20 with left 10 and no other children. Right-rotate z. Compute both final heights and explain a promoted-first refresh bug.

#### Solution

After rewiring, z=30 has no children, so its new height is zero. Promoted y=20 has children 10 and 30, each height zero, so its new height is one. Before the rotation z's cached height was two. If y is refreshed first, it reads that stale two from its new right child z and stores height three, even though the final tree height is one. Refreshing z first and y second obeys the actual dependency. The same ordering is required for size, sum or closest-pair aggregates that depend on child metadata.

### 14. Four insertion cases, one final shape

For sequences (30,20,10), (10,20,30), (30,10,20) and (10,30,20), identify the repair site, primitive rotations and final preorder.

#### Solution

In the first sequence, 30 becomes left-heavy with left-heavy child 20: right-rotate 30, one primitive. In the second, 10 becomes right-heavy with right-heavy child 20: left-rotate 10, one. In the third, 30 has right-heavy left child 10: left-rotate 10 then right-rotate 30, two. In the fourth, 10 has left-heavy right child 30: right-rotate 30 then left-rotate 10, two. Every final preorder is **20,10,30**, with root height one and all balances zero. The route names LL/RR/LR/RL identify geometry; their required rotation directions are not identical to those names.

### 15. A double rotation with a real middle subtree

Start with AVL root 50, children 20 and 70, and 20's children 10 and 30. Insert 25. Determine the lowest violation, final links, height and primitive count.

#### Solution

The new leaf 25 attaches as 30.left. Node 30 has balance one and height one; node 20 has left height zero and right height one, so is valid with balance −1 and height two. Node 50 now has left height two and right height zero, giving balance two. This is LR: left-rotate 20, then right-rotate 50. The new root is 30; its left child is 20 with children 10,25, and right child is 50 with right 70. Preorder is **30,20,10,25,50,70**, height two, with **two primitives**. Transferring the middle subtree 25 correctly distinguishes the repair from merely swapping three keys.

### 16. One insertion can expose several apparent violations

In the pre-insertion tree from Question 15, insert 5 instead. Explain why fixing the lowest violation removes any need for a higher insertion repair.

#### Solution

The new 5 attaches below 10. Node 10 becomes height one; node 20 now has child heights one and zero and remains valid. Root 50 gets child heights two and zero, so it is the lowest violation, with left-heavy child 20. Right-rotate 50. The result is root 20, with left 10 whose left is 5, and right 50 with children 30,70. Its height is two, equal to the original root's height. If this subtree had an ancestor, that ancestor would receive the same height as before insertion. It can require metadata refresh but cannot require another balance repair from this insertion. The final preorder is **20,10,5,50,30,70**.

### 17. Deletion with a balanced heavy child

Given root 40, left 20 with children 10,30, and right leaf 60, delete 60. State the primitive count, final preorder and whether height propagation continues.

#### Solution

The old tree height is two. After removing 60, B(40)=1−(−1)=2 and B(20)=0. The correct repair is one right rotation at 40. The new root is 20, with left 10 and right 40 whose left child is 30. Preorder is **20,10,40,30**; height remains two. The demoted 40 has balance one and height one, and promoted 20 has balance −1. Since the repaired subtree keeps its pre-deletion height, no height decrease propagates to an ancestor. This is deletion's equality case; a strict insertion-only outer comparison is unsuitable.

### 18. Deletion with an outer-heavy child

Given root 40, left 20 with left 10, and right leaf 60, delete 60. Compare the outcome with Question 17.

#### Solution

Before deletion the root height is two and its left child's balance is one. Deleting 60 gives B(40)=2, so right-rotate 40. The result is root 20 with children 10,40, preorder **20,10,40**, height one and zero local balances. There is **one primitive**, as in Question 17, but now the subtree height decreases from two to one. An ancestor must therefore be reconsidered. Equal rotation counts do not imply equal height propagation; the heavy child's pre-repair balance determines the difference.

### 19. Deletion with an inner-heavy child

Given root 40, left 20 with right 30, and right leaf 60, delete 60. Explain why one right rotation fails.

#### Solution

After deleting 60 the root is left-heavy by two, but its heavy child 20 is right-heavy by one. A single right rotation would make 20 the root with right 40 whose left is 30; that root still has a right subtree of height one and empty left, so balance is −2. Instead left-rotate 20, then right-rotate 40. The final preorder is **30,20,40**, with height one and all balances zero. The correct count is **two primitives**, and the repaired subtree loses one height level relative to the original. Child geometry, not a memorized single-rotation direction, resolves the case.

### 20. A two-site deletion cascade

Use the twelve-key initial BST insertion order 50,20,10,30,40,80,60,70,90,85,100,110. It describes an already AVL initial shape, not a sequence that must be rebalanced while loading. Delete 10 and determine all repair sites, final preorder and height change.

#### Solution

The initial root height is four; its child heights are two at 20 and three at 80. Removing leaf 10 makes 20 right-heavy by two, with right-heavy child 30. Left-rotate 20, producing a height-one subtree rooted at 30 with children 20,40. This subtree is shorter than the original left subtree. Root 50 then has left height one and right height three, so is right-heavy by two. Child 80 has balance −1, so left-rotate 50. Final preorder is **80,50,30,20,40,60,70,90,85,100,110**. Height is three and there are **two primitive rotations at two distinct sites**. Loading this stated diagram through an AVL insertion algorithm could change its shape; the question explicitly fixes the initial links.

### 21. Two-child deletion tracks the removed successor

Start with the perfect seven-node tree 40,20,60,10,30,50,70. Delete 40 using successor substitution. Give the association removed, physical removal point, final preorder and rotation count.

#### Solution

The target association is key 40. Its successor is 50, the left leaf of 60. Copy the full 50 association into the root, then remove the old leaf 50 from 60.left. Node 60 now has balance −1 and height one; the root still has two height-one children, so no repair rotation is needed. Final preorder is **50,20,10,30,60,70**, with **zero rotations**. The deleted association is 40, while the physically freed/relinked position belonged to 50. The repair route follows that physical position through 60 to the root. Key/value semantics and memory identity are separate.

### 22. Absent deletion and singleton deletion

For a singleton AVL tree containing 7, perform delete(9), then delete(7). State roots, sizes, heights and whether any rotation occurs.

#### Solution

The first search compares with 7 and reaches a null right child. No association is removed, so the root stays 7, size stays one and height stays zero. The second deletion removes the root, returning its null child; size becomes zero and height becomes minus one. Neither operation requires a rotation. A null root is a valid completed empty tree, not an error state. The first operation has constant actual cost in this one-node example even though a general worst-case bound is logarithmic in growing n.

### 23. Primitive rotations are not operation time

A standard AVL insertion performs a double rotation at a depth-eight subtree in a height-twelve tree. Is the whole insertion constant-time? Explain the cost components.

#### Solution

The local repair contains **two constant-time primitives**. Before reaching it, the insertion must search a root-to-null route that can contain thirteen actual nodes. Returning upward refreshes height and any relevant aggregate along that route. Restoring the repaired subtree's old height prevents another rotation site, but does not undo the search or necessarily eliminate aggregate updates above it. Thus the general insertion remains **O(log n)**, with a constant rotation count. A pointer to the insertion position could change the search resource, but metadata propagation and the explicitly supplied interface must still be analyzed. Local work and total operation work are different quantities.

### 24. Stop height propagation, continue aggregate propagation

After the balanced-heavy-child deletion in Question 17, the subtree has unchanged height but one fewer key. If size and sum are cached above it, may the update stop completely?

#### Solution

No. The unchanged height means the ancestor's AVL balance cannot newly change from this deletion, so height-based rebalancing can stop. Nevertheless the subtree size decreases by one and its sum decreases by the deleted key 60. Every ancestor whose subtree contains that position must refresh those fields. Stopping the entire return process would leave stale rank/select and range-sum answers despite a valid AVL shape. An implementation can maintain separate flags for structural height change and aggregate change, or simply return and refresh all ancestors. The latter still takes logarithmic time. A balance propagation optimization is not a semantic no-change certificate.

### 25. Rotation updates for rank augmentation

Before a left rotation at x with right child y, let sizes of A=x.left, B=y.left and C=y.right be 2,3 and 4. Compute the final sizes of x and y.

#### Solution

Before rotation, y owns 1+3+4=8 nodes and x owns 1+2+8=11. After rotation, x owns A, its own association and B, so size(x)=2+1+3=**6**. Promoted y owns the new x subtree, itself and C, so size(y)=6+1+4=**11**. The promoted total equals the original total because rotation preserves all associations. Refresh x before y so y sees six rather than x's old eleven. A select route uses these subtree counts, not the heights or a globally stored rank. The computation is constant work per rotation with fixed-size counts.

### 26. Closest-pair augmentation with a cross-boundary winner

At node key 40, left-subtree minimum/maximum are 5/37 and its best gap is 8. The right minimum/maximum are 44/100 and its best gap is 6. Compute the combined best gap and witness category.

#### Solution

The internal candidates have gaps eight and six. The two boundary candidates are (37,40), gap three, and (40,44), gap four. The minimum is therefore **three**, witnessed by **37 and 40**. A pair spanning both child subtrees has distance at least 44−37=7 and cannot beat the adjacent boundary pair; more generally closest pairs in an ordered set are adjacent in sorted order. Combined minimum and maximum are 5 and 100. Store the witness with a deterministic tie rule when equal gaps occur. A null child contributes no candidate, and a singleton returns no pair rather than a false zero gap.

### 27. Count versus rank and output-sensitive work

A balanced subtree-size tree holds 10,20,25,30,40,60,65,70,80. Compute strict rank(65), zero-based select(4), inclusive count [25,70] and the reporting cost for that interval.

#### Solution

Six keys are smaller than 65, so strict rank is **six**. Zero-based position four is the fifth sorted key, **40**. The interval contains 25,30,40,60,65,70, hence count **six**. Algebraically rank(70)−rank(25)+1=7−2+1=6 because 70 is present; if it were absent the upper presence term would be zero. Rank/select and range count each follow logarithmic routes with correct size fields. Reporting all six associations costs O(log n+6), and reporting an interval containing k keys requires Omega(k) output work. Balance changes route length, not the cost of emitting the requested results.
