# Balanced Search Trees: Exact Heights, Repair Proofs, and Ordered Updates

## Written courses, prerequisites and reading route

Four core written courses were read and selected for complementary coverage: CMU 15-122, MIT 6.006, Princeton COS226 and Stanford CS166. Berkeley CS61B provides an additional comparison of multiway repair. The [source audit](../reviews/a_balanced-sources.html) records actual reading, candidate selection and corrections. The exposition, proofs, numerical examples and implementations below are independently written.

This chapter assumes the strict BST ordering invariant, traversal, deletion and subtree-size machinery of the preceding chapter. Its goal is to make the height guarantee survive arbitrary valid updates. Read the teaching sections before the questions. Use the full summary to reconstruct the argument, and the final rules to check hypotheses and exam traps. Models start paused and separate exact algorithm checkpoints from geometric interpolation. A moving key token represents an association, not the identity of a particular memory allocation.

## 1. What balance guarantees, and what it does not

A search visits one root-to-key or root-to-null route. Constant work per visited node gives cost proportional to route length. Keeping height logarithmic therefore protects worst-case search, insertion, deletion, predecessor and successor against adversarial input orders. Sorted input is harmless to a correctly maintained AVL or red-black structure; it is disastrous to an ordinary insertion-only chain.

Balance is a property of every completed state and a theorem about its size. It is not the visual claim that a tree looks symmetric. A root with equal child heights may hide a severe violation lower down. A low height does not alone verify either BST ordering or correct cached fields. Moreover, a logarithmic worst-case upper bound does not say that a root hit takes logarithmic actual time. Search at the root still takes one key comparison.

Throughout, keys are distinct and have a stable total order. An existing-key insertion replaces its associated value. Empty height is minus one; a singleton has height zero. A primitive rotation is one left or one right rotation. A double rotation contains two primitives. Completed states must be owned, acyclic trees with consistent parent links if parent links are stored. Key comparison, scalar metadata and pointer reassignment are treated as constant-cost operations; long strings or unbounded exact arithmetic need their own cost accounting.

## 2. AVL heights and local certificates

Define the true height and balance factor by

$$h(\varnothing)=-1,\qquad h(v)=1+\max(h(v_L),h(v_R)),\qquad B(v)=h(v_L)-h(v_R).$$

An AVL tree is a strict BST for which every node has balance factor minus one, zero or one. The sign convention matters: positive means left-heavy here. A textbook using right minus left reverses signs but not geometry. Stored height must equal true height. Reading a cached value costs constant time only after this agreement has been established and maintained.

For a bottom-up certificate, recursively obtain the two true child heights, test their difference, compare the stored height to their maximum plus one, and return that true height. Combine this with inherited strict key intervals and a visited-address set when malformed pointers are possible. Each node is processed once, so certification takes linear time. Computing a fresh recursive height separately at each node revisits descendants and can take quadratic time on a chain. Production updates use the maintained local cache; the full certificate is an audit tool.

Sources: CMU Lecture 16, PDF pages 2–13; MIT Lecture 6, PDF pages 2–4.

## 3. The exact minimum-node recurrence

Let $M_{h}$ be the fewest actual key nodes in an AVL tree of edge height h. The bases are $M_{-1}$=0 and $M_{0}$=1. A height-h root must have a height-(h−1) child. To minimize the other child while retaining balance, give it height h−2. Both subtrees can be chosen minimally, so this is an achievable equality:

$$M_h=1+M_{h-1}+M_{h-2}\quad(h\ge1).$$

This proves both directions. Any valid tree has at least those child sizes; attaching two minimal subtrees gives a valid witness. The first values, indexed from height minus one, are 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232 and 376. A perfect tree gives the opposite size bound:

$$M_h\le n\le2^{h+1}-1.$$

With $F_{0}$=0 and $F_{1}$=1, induction gives the exact identity

$$M_h=F_{h+3}-1.$$

The base cases are $F_{2}$−1=0 and $F_{3}$−1=1. Adding one to the recurrence makes the Fibonacci shift immediate. Do not substitute an index taken from a different height convention. For n=1000, $M_{13}$=986 and $M_{14}$=1596, so the greatest possible AVL height is 13. The minimum possible binary height is 9 because $2^{10}$−1=1023 can hold 1000 nodes. Exact maximum-height questions should compare recurrence values, not round a logarithmic approximation.

<!-- SIM: minimum -->

## 4. Logarithmic height, constants and extremal shapes

The weaker recurrence inequality $M_{h}$≥2$M_{h-2}$+1 already proves exponential growth in h and therefore logarithmic height. For the sharp leading constant, solve the Fibonacci characteristic equation x²=x+1. Its roots are $\phi$=(1+sqrt(5))/2 and $\psi$=(1−sqrt(5))/2, giving

$$M_h+1=\frac{\phi^{h+3}-\psi^{h+3}}{\sqrt5}.$$

The second exponential has absolute value below one. Taking logarithms shows maximum height equals $\log_{\phi}$(n) plus a bounded additive term. Changing log bases yields leading coefficient 1/$\log_{2}$($\phi$), approximately 1.44042. This is an asymptotic coefficient, not the exact height for a small n. An elementary induction also gives $F_{j}$≥$\phi^{j-2}$ for j≥2, and hence the safe bound h≤$\log_{\phi}$(n+1)−1 for a nonempty height-h AVL tree. The recurrence remains the best integer test.

Minimum-node shapes are not unique. Let $S_{h}$ count ordered shapes attaining $M_{h}$. Then $S_{-1}$=$S_{0}$=1 and $S_{h}$=2$S_{h-1}$$S_{h-2}$ for h≥1: choose the side of the taller child and independently choose the two minimal shapes. The first counts are 2, 4, 16, 128 and 4096 at heights one through five. Sorted keys assign one unique BST labelling to any ordered shape. This shape count is distinct from the number of insertion orders that create a particular tree after rebalancing.

For all AVL shapes on n keys, refine the count by height. Let A(n,h) count ordered AVL shapes; the empty case is A(0,−1)=1. Sum products A(i,a)A(n−1−i,b) over all left sizes i and heights satisfying |a−b|≤1 and max(a,b)+1=h. This dynamic recurrence avoids falsely counting all Catalan shapes as balanced. It also supplies independent small-size checks for examination questions.

Every integer size between $M_{h}$ and $2^{h+1}$−1 is attainable at fixed height h. Induct on h: use child heights h−1/h−2 to obtain a contiguous size interval from $M_{h}$ through 1+capacity(h−1)+capacity(h−2), and child heights h−1/h−1 for a second interval from 1+2$M_{h-1}$ through full capacity(h). Sums of integer intervals contain every integer between their endpoints. The intervals overlap or touch because $M_{j}$≤$2^{j}$ for j≥0, proved directly from the minimum recurrence. Their union has no gap. This establishes the size witnesses used in exact maximum-height questions; merely satisfying an unproved necessary inequality would not have established existence.

Sources: MIT Lecture 6, PDF page 3, with the Fibonacci index independently corrected; CMU Lecture 16 for the local invariant. The counting extensions are independently derived.

## 5. A rotation preserves order before it repairs balance

For a right rotation, write the original subtree as z with left child y. Let A=y.left, C=y.right and D=z.right. All keys satisfy A<y<C<z<D. The result has root y, left subtree A, and right child z whose left subtree is C and right subtree D. The inorder sequence is unchanged. No subtree is lost, copied or attached twice. A left rotation is its mirror and structural inverse.

```python
def rotate_right(z):
    y = z.left
    middle = y.right
    z.left = middle
    y.right = z
    refresh(z)           # Demoted node first.
    refresh(y)           # Promoted node depends on z.
    return y
```

The returned root must replace the caller's old child link or the global root. If parent pointers exist, update the old parent, the promoted node, the demoted node and the transferred middle subtree. Refresh every cached field from actual children, in dependency order. A rotation is constant work with fixed-size metadata.

The structural primitive does not promise to make every input balanced. Right-rotating the perfect tree with keys 10,20,30 at 20 makes a root 10 with a right chain of length two, violating AVL. The correct contract promises content/order preservation and metadata correctness; balance additionally requires the case hypotheses below. Intermediate steps of a double rotation may themselves be unbalanced. This is why a generic rotation and a specialized repair must have different contracts.

## 6. AVL insertion: the lowest violation

Insert by ordinary BST search, attach a new height-zero leaf, and return upward. Each affected ancestor's subtree height increases by at most one. Nodes outside this route retain exactly the same child subtrees. At the first upward node z with absolute balance two, both child subtrees are already AVL. Assume z is left-heavy. Its left child y is either left-heavy or right-heavy; at this first insertion violation y cannot be balanced. If y became balanced after a new key was attached, its larger child height before the insertion already equalled its new maximum, so y's height would not have increased.

The names LL, LR, RR and RL describe the two route directions from z, not the names of the required primitive rotations.

| Lowest violation | Heavy child | Repair |
|---|---|---|
| B(z)=2 | B(y)=1 | LL: right rotation at z. |
| B(z)=2 | B(y)=−1 | LR: left rotation at y, then right rotation at z. |
| B(z)=−2 | B(y)=−1 | RR: left rotation at z. |
| B(z)=−2 | B(y)=1 | RL: right rotation at y, then left rotation at z. |

Sequences 30,20,10 and 10,20,30 use one primitive each. Sequences 30,10,20 and 10,30,20 use two. All finish with root 20 and children 10 and 30. Looking only at the final inserted key and the root is insufficient after deletion or in a nonroot repair: inspect the actual child balance.

<!-- SIM: insertion -->

## 7. Why one insertion repair site suffices

For the LL case, let the unchanged short subtree at z have height t. Before insertion, z's left subtree had height t+1 and z had height t+2. After insertion, y's left subtree has height t+1, while y's right and z's right subtrees each have height t. Rotating right gives demoted z height t+1 and new root y height t+2. All local balances are valid and the repaired subtree has exactly its pre-insertion height.

For LR, write y.right=w. The outer subtrees y.left and z.right have height t. The two children of w have heights at most t, differ by at most one and have maximum t. The double rotation gives root w, children y and z, each of height t+1, and total height t+2. The order intervals still occur as A<y<B<w<C<z<D. Both local child balances remain at most one, including the small case where w was the inserted leaf and t=−1.

The mirror proofs establish RR and RL. Since the old subtree height is restored, no higher ancestor gains a new height difference and no additional repair site is needed. Standard AVL insertion therefore uses at most two primitive rotations in total, although it can refresh logarithmically many ancestors and perform logarithmically many comparisons. Several primitive rotations and several repair sites are different claims. Existing-key replacement changes no structural height, though a value-dependent aggregate may still need refresh.

## 8. AVL deletion begins at the physical removal

Delete using the strict BST procedure. A two-child target is replaced by its inorder successor association, and the successor is physically removed from its old location. Repair begins on the route from that physical removal back to the root, not merely at the target whose key was overwritten. Replacing only a key while failing to replace its value breaks dictionary semantics; freeing a still-linked successor breaks ownership.

A removed child subtree's height decreases by at most one after a valid recursive repair. At an affected node, the remaining heavy child has balance −1, zero or one. Unlike insertion, zero is possible and important. With B(z)=2 and y=z.left, a right rotation is used when B(y)≥0; LR is used when B(y)<0. Mirror these inequalities for right-heavy z. Thus an insertion-only helper using a strict outer-height test may choose the wrong operation for deletion.

Deletion of an absent key changes no associations or heights. A singleton deletion returns an empty tree. A one-child removal returns its surviving child. These are structural outcomes, not special exceptions to the height definition. Continue returning the repaired root and freshly computed metadata through every recursive caller.

## 9. Deletion's balanced-heavy-child case and cascading repair

Assume deletion has shortened z.right from height t+1 to t, while y=z.left remains height t+2. The old z height was t+3. If B(y)=0, both y children have height t+1. A right rotation gives demoted z height t+2 and promoted y height t+3. Its balance is −1 and z's balance is 1. The subtree retains its old height, so height propagation stops at this site.

If B(y)=1, y.left has height t+1 and y.right has height t. A right rotation gives both the demoted z and its left peer height t+1, promoted y height t+2, and zero balances. The repaired subtree is one level shorter than before deletion, so the parent must be revisited. If B(y)=−1, the LR double rotation similarly gives height t+2 and can continue the decrease upward. The mirror cases have the same stop/continue consequences.

| B(z) after removal | Heavy-child balance | Primitives | Height relative to pre-deletion subtree |
|---|---|---|---|
| 2 | 1 | Right at z | Decreases by one. |
| 2 | 0 | Right at z | Unchanged; stop height propagation. |
| 2 | −1 | Left at y, right at z | Decreases by one. |
| −2 | −1 | Left at z | Decreases by one. |
| −2 | 0 | Left at z | Unchanged; stop height propagation. |
| −2 | 1 | Right at y, left at z | Decreases by one. |

For a zero-child witness, use root 40, left subtree 20 with children 10,30, and right leaf 60. Deleting 60 triggers a right rotation; the result is root 20 with left 10 and right 40 whose left is 30. Its total height remains two. For a cascading witness, begin with root 50; its left subtree is root 20 with left 10 and right 30 with right 40; its right subtree is root 80 with left 60 with right 70 and right 90 with left 85 and right 100 with right 110. All twelve nodes initially satisfy AVL. Deleting 10 causes a left rotation at 20, followed by a left rotation at 50. This actual two-site example is traced below and independently checked.

<!-- SIM: deletion -->

## 10. Complete AVL update implementation and proof

The following independently written reference uses cached edge heights. Each node has key, value, left, right and height fields, with a new node initially having height zero. Optional size or sum fields belong in refresh as well. Parent pointers are omitted deliberately; adding them requires the assignments established in Section 5.

```python
def height(t):
    return -1 if t is None else t.height

def refresh(t):
    t.height = 1 + max(height(t.left), height(t.right))

def balance(t):
    return height(t.left) - height(t.right)

def rotate_left(z):
    y = z.right
    z.right = y.left
    y.left = z
    refresh(z)
    refresh(y)
    return y

def repair(t):
    refresh(t)
    if balance(t) == 2:
        if balance(t.left) < 0:
            t.left = rotate_left(t.left)
        return rotate_right(t)
    if balance(t) == -2:
        if balance(t.right) > 0:
            t.right = rotate_right(t.right)
        return rotate_left(t)
    return t

def insert(t, key, value):
    if t is None:
        return Node(key, value)
    if key < t.key:
        t.left = insert(t.left, key, value)
    elif key > t.key:
        t.right = insert(t.right, key, value)
    else:
        t.value = value
    return repair(t)

def delete(t, key):
    if t is None:
        return None
    if key < t.key:
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        if t.left is None:
            return t.right
        if t.right is None:
            return t.left
        s = t.right
        while s.left is not None:
            s = s.left
        t.key, t.value = s.key, s.value
        t.right = delete(t.right, s.key)
    return repair(t)
```

The repair precondition is stronger than having two arbitrary AVL children: before one local update the whole subtree was AVL, and one child's height has changed by at most one. The magnitude can consequently be at most two. Calling repair on an arbitrary corrupted tree with balance four is outside this contract; the equality tests deliberately do not conceal that violation.

Induct on recursive subtree size. The empty and surviving-child returns preserve contents and balance. A recursive update returns an ordered AVL child with the required content change and height change at most one. Search intervals preserve strict order, including the successor substitution. The local case proofs restore balance and true metadata; rotations preserve the association set. The returned root is attached by the caller. This establishes the update postcondition and the height-change bound together. Complexity is logarithmic because a search/successor route and a return route each have logarithmic length, and each local repair uses at most two constant-time primitives. A deletion may repair logarithmically many sites; it is not a constant-rotation algorithm in the worst case.

Sources: CMU Lecture 16 for insertion contracts and pointer reasoning; MIT Lecture 6 for geometric cases. Deletion implementation and its zero-child/cascade proof are independent extensions.

## 11. Augmentation survives rotations when it is locally recomputable

Subtree size satisfies size(v)=1+size(v.left)+size(v.right), with empty size zero. Rotations do not change the promoted subtree's overall contents, but they change the demoted node's contents. Refresh the demoted node first, then the promoted one. Rank and select from the previous chapter now have worst-case logarithmic routes. Range reporting still costs O(log n+k) for k outputs; balancing does not make printing k results constant-time.

A fixed-size aggregate computed in constant time from a node and its children's aggregates can be refreshed along update routes and at rotation sites without changing the logarithmic update bound. Examples include count, sum, minimum, maximum and an argmax priority with a specified tie rule. A field storing every global rank is different: inserting a new minimum can change all n ranks. A field storing a sorted list of an entire subtree is also not constant-size or constant-time to combine.

For closest pairs on a line, cache subtree minimum, maximum and smallest adjacent gap with its witness pair. At v, candidates are the left child's best pair, the right child's best pair, (max(left),v.key), and (v.key,min(right)); omit candidates involving an empty subtree. Every cross-cut closest pair must be one of these two boundary pairs because keys are ordered. With fewer than two keys use an explicit no-pair sentinel, not gap zero. Querying the root's cached witness is constant time while insertion/deletion remain logarithmic. This is a meaningful conceptual application of the augmentation theorem.

Source: Stanford Lecture 7, PDF pages 38–65. The formulas and new numerical examples are independently derived.

## 12. Multiway search trees and exact height bounds

A node containing k sorted keys has k+1 ordered child intervals if it is internal. A 2–3 node stores one or two keys; a 2–3–4 node stores one, two or three. All actual leaves are at the same depth. Do not confuse a node's key count with its potential child count or the binary node count of an encoding.

For a nonempty 2–3 tree of edge height H, every level has between the corresponding all-two and all-three branching capacities. Therefore

$$2^{H+1}-1\le n\le3^{H+1}-1.$$

For a 2–3–4 tree replace the upper base three with four. The equality examples fill every node with the minimum or maximum key capacity, and the geometric sums count keys, not merely leaves. A one-node tree has height zero and may contain multiple keys. With n=1000, the 2–3 height lies between 6 and 8: $3^{6}$−1<1000≤$3^{7}$−1 and $2^{9}$−1≤1000<$2^{10}$−1. These are necessary bounds; a requested exact construction must still satisfy uniform leaf depth and local capacities.

For a B-tree of minimum degree b≥2, nonroot nodes have b−1 through 2b−1 keys, while a nonempty root has one through 2b−1. For H≥1 the minimum root has one key and two children; level j≥1 contributes at least 2$b^{j-1}$(b−1) keys. Summing gives

$$2b^H-1\le n\le(2b)^{H+1}-1.$$

At H=0 the minimum is one key, consistent with the same formula. This minimum-degree convention differs from an 'order' defined as maximum children. State the convention before substituting a branching factor.

Linear scanning of a b-sized node uses O(b) comparisons per level; binary search uses O(log b). Updating packed key arrays or splitting a node can still cost O(b). Thus comparisons for lookup can be O(log n) while insertion movement has bound O(b $log_{b}$ n). If each node is one disk block and transfer cost dominates, block accesses are O(1+$log_{b}$ n); within-block work remains a separate resource. Minimizing the symbolic scalar b/ln(b) over integer b≥2 gives b=3 by comparing the two neighbors of e. It does not establish the fastest practical implementation, where different constants, node capacity and cache transfers dominate.

Sources: Princeton slides, PDF pages 4–12; Stanford Lecture 6, PDF pages 21–52, with the discrete minimization corrected.

## 13. Splitting, borrowing, merging and root exceptions

Bottom-up 2–3 insertion first inserts into a leaf. A temporary three-key node [a,b,c] splits into [a] and [c], with b promoted. The original four interval subtrees are divided in order. If promotion overflows the parent, repeat. Splitting the root alone increases the uniform leaf depth by one. No newly inserted key is pushed into a fresh deeper singleton while other leaves remain shallower.

Top-down 2–3–4 insertion instead splits a full three-key child before descending into it; its parent has already been made nonfull. A full root is split first. The descended leaf consequently has room. This top-down variant and the bottom-up 2–3 variant need not produce identical valid shapes. For increasing keys 10 through 70 by tens, top-down 2–3–4 insertion ends with root [20,40] and leaves [10], [30], [50,60,70]. The model shows the actual split before 60 enters the right leaf.

For deletion in minimum-degree-two multiway trees, ensure that a descended nonroot child has at least two keys. If a neighboring sibling has spare capacity, move the separating parent key into the child, move the sibling boundary key up to the parent, and transfer the corresponding boundary subtree. Directly moving a nonadjacent sibling key breaks intervals. If both adjacent candidates have only one key, merge a child, separator and sibling into a three-key node. A parent may thereby lose a key; the invariant established earlier makes that safe, except that an emptied root is replaced by its only child and the overall height decreases.

For an internal target, if its predecessor-side child has at least two keys, replace by the predecessor and recursively remove it; otherwise use a sufficiently large successor-side child. If both have one key, merge them with the separator and recurse into that combined child. Returning through valid local transformations preserves every association except the target, the interval order, capacity bounds and uniform leaf depth. A key absent from the tree can still cause top-down restructuring if search and repair are interleaved; membership checking first is needed if a no-structural-change contract is desired for absent deletion.

<!-- SIM: multiway -->

Source: Berkeley Lecture 27 for top-down repair; Princeton for bottom-up 2–3 promotion; Stanford for minimum-degree capacity and the correspondence.

## 14. General red-black trees and a precise black-height convention

In the general node-colored variant, actual nodes are red or black, the nonempty root is black, red nodes have no red children, and every route from a node to a null child has the same black-node count. Null children are black sentinels conceptually. To avoid an off-by-one ambiguity in numerical questions, define $\beta$(null)=0 and let $\beta$(v) include v itself if v is black, but exclude the final null. The two child $\beta$ values must agree, and $\beta$(v) is that common value plus one for a black v, or unchanged for a red v.

This is a translated convention, not the CLRS-style count that excludes v and includes the final sentinel. For a black root their numerical values agree; at a red node or a null they may differ. State which objects are counted before comparing paths. Colors protect complexity; ordinary key search still ignores them.

A valid general red-black tree can have a red right child or two red children of a black node. Neither alone is a general red-black violation. Collapsing each black node with its red children yields a one-, two- or three-key multiway node. No red-red adjacency limits the cluster to those sizes. Equal black height makes the resulting 2–3–4 leaves uniform in depth. Conversely, a two-key node has two possible binary red encodings; a three-key node uses its middle key black with its two outer keys red. Thus general red-black encoding is not a unique 2–3 left-leaning correspondence.

<!-- SIM: encoding -->

Sources: Stanford Lectures 6–7. This $\beta$ convention and its exact bounds below are defined and proved here.

## 15. Red-black height, path ratio and counting bounds

With a black root and $\beta$(root)=b, collapsing red clusters produces exactly b black layers. Each cluster has one through three keys. Hence

$$2^b-1\le n\le4^b-1.$$

On any root-to-null route there are b black actual nodes and at most b red actual nodes. If d is the number of visited actual nodes, b≤d≤2b. The number of traversed child links from the root to the terminal null is also d, whereas edge height to the deepest actual node is at most 2b−1. Consequently

$$h\le2b-1\le2\log_2(n+1)-1.$$

This safe universal bound is sufficient for logarithmic routes and handles n=1 correctly. It is a necessary bound, not a guarantee that every integer meeting it is achievable for a fixed n and color pattern. Ratios of longest to shortest root-null paths are at most two. Ratios of actual root-leaf lengths cannot be inferred by dropping the null endpoint without adjusting the subtraction, especially when the shortest actual-leaf edge length is zero.

For n=31, the size bounds imply 3≤b≤5: 4²−1=15 cannot hold 31, while 2⁶−1=63 needs too many. A perfect all-black 31-key tree realizes b=5. The bounds do not count how many colored trees exist. Certification must verify strict inherited order, no red-red adjacency and equal child $\beta$ recursively; root-black is checked separately. An all-black chain fails equal black height despite having no adjacent red nodes.

## 16. Classical red-black insertion: red uncle and black uncle

Insert a new red leaf at the BST null position. This preserves the black count of that route, because the new actual node contributes zero. Its only possible internal color violation is a red parent. A new root is blackened. Otherwise a red parent has a black grandparent g; choose the mirror of the following cases when the parent is g.right.

If the uncle is red, blacken both parent and uncle and redden g. Both routes through g keep the same local black contribution, but g may now violate its own parent's color. Continue at g. If g is the root, blacken it and stop; all paths gain a black equally. This case uses no rotation and may repeat logarithmically many levels.

If the uncle is black or null and the new/active node is the parent's right child, left-rotate the parent to convert the triangle to a line. Relabel the active parent/child roles after that operation. Then blacken the new parent, redden g, and right-rotate g. The transformed subtree preserves ordering and has the same black count as before insertion. It has no red-red link at its new top, so no further repair is needed.

The line case uses one primitive; triangle plus line uses two. Earlier red-uncle propagation uses zero. Classical red-black insertion therefore uses at most two primitive rotations overall and O(log n) recolor work. This bound is attached to this algorithm, not every left-leaning implementation. The invariant in the loop is that at most the active node and its parent have a red-red link, while all child subtrees have consistent black height.

<!-- SIM: classical -->

## 17. Classical red-black deletion and the missing-black ledger

If a two-child target is replaced by its successor association, the color removed is the successor's original color, not the target's original color. Track the surviving replacement child x and its parent, including a sentinel x when necessary. Removing a red node creates no black deficit. Removing a black node with a red replacement is repaired by blackening that replacement. Otherwise a missing black unit must be transported or absorbed.

'Double black' is a proof ledger: the active route carries one missing black unit, so counting that virtual unit makes both parent routes agree. It is not a third persistent node color. At every loop step, all ordinary subtrees satisfy the completed color invariants; only the active route has the deficit. If x is the root, discard the extra ledger unit because all remaining routes are affected equally.

Assume x is p.left and sibling w is p.right. Near means w.left, toward x; far means w.right. The right-active mirror reverses all directions.

| Case | Condition | Action and consequence |
|---|---|---|
| 1 | w is red | Blacken w, redden p, left-rotate p; recompute w=x.parent.right. This converts to a black-sibling case. |
| 2 | w is black and both children are black/null | Redden w and move the deficit to p. If p was red, blacken it and stop; if black, continue upward. |
| 3 | w is black, far child black, near child red | Blacken near, redden w, right-rotate w; recompute w. The new sibling has a red far child. |
| 4 | w is black with red far child | Give w p's old color; blacken p and the far child; left-rotate p. The deficit is absorbed; stop. |

Case 2 shortens the sibling's ordinary black count by one and transfers the virtual missing unit to the parent. Cases 3 and 4 redistribute a black unit while preserving subtree intervals and the counts of every unaffected branch. Case 1 is a color/geometry conversion, not deficit removal; recomputing w is essential after the rotation. A sibling cannot be a null sentinel in a reachable nonroot deficit case arising from a formerly valid tree: the active side's pre-removal black contribution would require a positive corresponding sibling contribution.

Only case 2 can continue upward, and it performs no rotation. Once case 1 occurs its now-red parent cannot propagate beyond the subsequent black-sibling repair. Case 3 is immediately followed by case 4, which stops. There can therefore be at most one rotation from each of cases 1,3,4, for a maximum of three primitives in the classical algorithm. Recolor propagation and search may still be logarithmic. A full implementation must maintain sentinel-parent information, returned root/parent links and every aggregate. The executable laboratory below implements the separately specified LLRB deletion variant rather than pretending these two algorithms are identical.

## 18. The stricter 2–3 left-leaning variant

A completed 2–3 LLRB tree is a strict BST with a black root, no red right links, no red-red adjacency and equal black height. A two-key multiway node [a,b] is represented by black b with red left child a. A persistent black node with two red children would be a four-node and is disallowed in this completed 2–3 variant, even though it is valid in the general variant. Temporary color violations are permitted during an update and must be repaired before return.

A color is stored in the child as the color of its incoming link; a root has a conventional black incoming color. A colored left rotation at h with red right child x preserves the old incoming color on x and makes h red. A right rotation is mirrored. A color flip toggles h and both nonnull children. Toggle is needed for deletion; a helper that always assigns parent red/children black only handles one insertion direction.

For insertion, recurse exactly as in a BST and create the new leaf red. Then, in this specified order, fix a sole right-red child with a left rotation, fix two successive left-red links with a right rotation, and split two red children with a color flip. Refresh size and other aggregates; finally blacken the global root. These transformations preserve black balance and correspond to promoting a temporary multiway overflow. At most constant local work is done per visited ancestor, so the total is logarithmic, but this recursive LLRB algorithm is not assigned the classical two-rotation guarantee.

<!-- SIM: llrb-insert -->

Source: Princeton slides, PDF pages 14–38, and the full public RedBlackBST.java listing. The executable code is an independent implementation of the same stated variant.

## 19. LLRB deletion: move a red resource before descending

Before deleting an existing key, redden the root if both children are black; the final root is blackened again if nonempty. This prepares a top-down resource and can temporarily violate root-black only. Check membership first so absent deletion preserves the completed state.

For left descent, if h.left and h.left.left are both black, call moveRedLeft: toggle h and both children; if the sibling's left child is red, right-rotate h.right, left-rotate h, then toggle again. This borrows from the neighboring multiway node or merges two minimal nodes, ensuring the descended side is not a minimal two-node. The right descent uses moveRedRight: toggle, and if h.left.left is red, right-rotate h and toggle again. The asymmetry is deliberate because completed red links lean left.

Before deleting on the right/equality side, right-rotate h when its left link is red. If the target is then h and has no right child, return null. Otherwise prepare the right descent as above. For a two-child equality target, copy the successor's complete association and remove the minimum from the prepared right subtree. At a minimum with no left child the returned tree is null: under this variant's descent invariant there cannot be a surviving right subtree that should have been kept. This statement would be false for an arbitrary ordinary BST.

On return, apply the same LLRB normalization order and recompute metadata. The local borrow/merge interpretation preserves key intervals, uniform black routes and the one intended association removal. Every descent consumes one actual route level after constant transformations, so the cost is logarithmic. Bounds of two insertion or three deletion rotations from the classical algorithm are not reused here. The model records all actual rotations and flips so this distinction can be inspected rather than memorized.

<!-- SIM: llrb-delete -->

## 20. Exam reasoning: select the invariant before the formula

For an AVL maximum-height question, compute the minimum-node recurrence and bracket n between consecutive thresholds. For an AVL rotation question, find the lowest violation, read the heavy child's balance, and distinguish insertion from deletion's zero case. Track the physical successor removal if the target has two children. Count primitive rotations separately from repair sites, comparisons and metadata refreshes.

For a red-black validity question, first identify the variant, then check inherited ordering, root color, red-red adjacency and equal black routes. Add the left-leaning condition only when it is part of the problem. For black-height arithmetic, explicitly state whether the starting node and null endpoint contribute. For multiway height or capacity, identify minimum degree versus maximum children and count keys per node rather than assuming one key each.

For data-structure selection, distinguish priority order from key order. A balanced tree with subtree sizes supports median keys; an argmax aggregate supports maximum mutable priority. One field does not automatically maintain the other. A minimum pointer can make finding the minimum constant-time but needs maintenance during updates. A hash-table lookup assumption does not replace a deterministic height proof. A proof that average update time is logarithmic is not a proof that every update is logarithmic.

## 21. Complete summary

Balance protects root-to-null routes under arbitrary valid updates. AVL requires strict BST order, true cached heights and child-height difference at most one at every node. The exact minimum size is $F_{h+3}$−1 under empty height minus one. Standard AVL insertion repairs one lowest site with at most two primitives, because the repaired subtree regains its old height. AVL deletion starts at the physical removed position; a balanced heavy child needs one rotation and stops height loss, while other repair cases may propagate upward.

Rotations preserve inorder associations but do not universally preserve balance. Returned roots, parent links and dependency-ordered metadata updates are part of correctness. Locally recomputable fixed-size aggregates preserve logarithmic maintenance; global ranks do not. Reporting k entries still requires output-sensitive work.

Multiway trees keep all leaves at one depth by splitting, borrowing and merging ordered intervals. Root split and empty-root replacement are the only global height changes in those procedures. General red-black trees encode 2–3–4 nodes; with $\beta$ counting actual black nodes including a black root and excluding null, size lies between $2^{\beta}$−1 and $4^{\beta}$−1, and actual height is at most 2 $\beta$−1. Classical insertion/deletion use at most two/three primitives respectively, while recolors and routes may be logarithmic.

The completed 2–3 LLRB variant instead encodes each two-key node by a left red link and excludes persistent four-nodes. Its ordered local normalization and top-down deletion resource transfers are specified separately. Neither colors alone nor an attractive drawing certifies order, balanced paths, ownership or cached values. Exact finite audits support the proofs and reveal bugs, but do not guarantee a score or correctness for every unseen input outside the declared contract.

## 22. Fully worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 23. Final reasoning rules and examination traps

<!-- INCLUDE: review -->

## 24. Editable balanced-tree laboratory

<!-- LAB: balanced -->

## References

1. Frank Pfenning, CMU 15-122, Fall 2026, [Lecture 16: AVL Trees](https://www.cs.cmu.edu/~15122/handouts/lectures/16-avl.pdf). AVL definitions, pointer contracts, insertion and exercise analysis; all 29 PDF pages reviewed.
2. Erik Demaine and Srini Devadas, MIT 6.006, Fall 2011, [Lecture 6: Balanced Binary Search Trees](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/83cdd705cd418d10d9769b741e34a2b8_MIT6_006F11_lec06.pdf). Edge-height convention, minimum-node recurrence, geometric insertion cases and operation comparisons; all eight PDF pages reviewed, with the stated index correction.
3. Robert Sedgewick and Kevin Wayne, Princeton COS226 Spring 2023 archive, [§3.3 written slides](https://www.cs.princeton.edu/courses/archive/spring23/cos226/lectures/33BalancedSearchTrees.pdf), [booksite](https://algs4.cs.princeton.edu/33balanced/) and [public RedBlackBST.java listing](https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html). Forty-five PDF pages, all written booksite sections and the public listing reviewed; 2–3 LLRB variant stated explicitly.
4. Keith Schwarz, Stanford CS166, Spring 2026, [Balanced Trees Part I](https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/06/Condensed%20Slides.pdf) and [Part II](https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/07/Condensed%20Slides.pdf). All 58 and 66 PDF pages reviewed; multiway cost models, general red-black correspondence and augmentation. The discrete optimization correction is recorded in the source audit.
5. Jonathan Richard Shewchuk, Berkeley CS61B, Spring 2014, [Lecture 27: 2–3–4 Trees](https://people.eecs.berkeley.edu/~jrs/61b/lec/27). All 195 lines of official text reviewed through the web reader; top-down split/borrow/fusion comparison. Native retrieval failure is disclosed.
6. Original Iranian MSc and doctoral archive pages are cited individually beside their checked English adaptations. Their independently derived answers are not described as official keys. Independent proofs, new numerical cases and executable laboratories extend the sources where the source notes leave a derivation or boundary case unresolved.
