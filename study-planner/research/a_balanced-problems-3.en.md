### 55. Exact LLRB insertion trace on seven keys

Insert 10,20,30,40,50,60,70 by the declared recursive 2–3 LLRB algorithm. Find the final preorder, $\beta$, total primitive rotations and color-flip operations.

#### Solution

Insert 10 as the blackened root. Insert 20 with a red link and rotate left at 10. Insert 30 and split the two red children by a color flip. Insert 40 and rotate left at 30. Insert 50, flip at 40 and rotate left at 20. Insert 60 and rotate left at 50. Insert 70, flip at 60 and then at 40; finally blacken the root. Final preorder is **40,20,10,30,60,50,70**; all seven nodes are black, so **$\beta$=3**. There are **four primitive rotations** and **four color-flip operations** across the seven insertions. Root blackening is not a three-node flip. Per-sequence totals are different from a theorem about one classical insertion.

### 56. LLRB deletion of the minimum

From the final LLRB tree in Question 55, delete 10. Identify the resulting preorder and surviving colors; explain the resource transfer before left descent.

#### Solution

Initially every node is black. Temporarily redden root 40. The minimal left child requires moveRedLeft at 40, whose toggle makes 20 and 60 red while 40 becomes black. Within 20, another prepared left descent toggles 20 and its leaf children. Remove red minimum 10; normalization at 20 left-rotates the sole red right link to 30. On returning to 40, normalization also rotates the sole right-red link to 60. The result is root **60 black**, left **40 red** whose children are **30 black** with left **20 red**, and **50 black**; right is **70 black**. Preorder is **60,40,30,20,50,70**, with $\beta$ two. The question counts deletion work separately from the already completed construction; missing a top-down toggle gives the wrong color trace.

### 57. Descending input is not a linear chain

Insert 70,60,50,40,30,20,10 into the declared LLRB algorithm. What is the final shape? Why does an ordinary BST comparison not predict it?

#### Solution

Successive red-link normalizations repeatedly split local overflow and reorient links. The final preorder is **40,20,10,30,60,50,70**, all nodes black and $\beta$ three. The insertion sequence has **four primitive rotations** and **four color flips**. An ordinary BST would instead be a left chain of height six because it never rotates; applying that result to a balanced algorithm ignores the algorithm's central update step. Increasing and decreasing orders happen to have the same final perfect seven-key shape here, but this example does not prove mirror symmetry of every LLRB update trace, whose completed red links lean left.

### 58. Why color flips must toggle for deletion

An insertion helper always assigns parent red and both children black. Is this an adequate implementation of the color flip used in moveRedLeft during deletion?

#### Solution

No. In a prepared deletion step the parent can be **red** with two **black** children. The resource transfer must change it to black with two red children, merging a minimal cluster or enabling a borrow. Assigning parent red/children black leaves exactly the original colors and fails to prepare the descended two-node. A toggle handles both insertion's black-parent/red-children direction and deletion's red-parent/black-children direction under their stated preconditions. It requires two actual children; blindly toggling a null child is a pointer error. The result may be transiently non-LLRB, and normalization plus final root blackening completes the update.

### 59. Equal key priorities require a defined tie order

A key-ordered balanced tree contains entries (key,priority,arrival label)=(20,8,5),(10,8,2),(30,7,1). A maximum-priority deletion uses earliest arrival as the tie rule. Which entry is removed, and what must argmax metadata compare?

#### Solution

Priority eight is maximal and is shared by keys 20 and 10. Their arrival labels are five and two, so the earliest is **key 10**. The aggregate compares first by greater priority and then by smaller arrival label; key order is only the BST routing order and is not the tie rule. A root argmax must recompute this total selection rule from its own entry and both child witnesses. After a priority change, refresh its ancestor route; rotations likewise refresh demoted/promoted nodes. Using 'leftmost key' as a substitute for earliest arrival would accidentally work for this data but fails after changing key 10's arrival label to nine, when key 20 should win.

### 60. Multiplicities and rotation-safe selection

A counted-key AVL tree has root 8 with multiplicity two, left key 3 with multiplicity one, and right key 11 with multiplicity three. Compute the expanded zero-based rank blocks and total mass. What changes when key 11 loses one occurrence?

#### Solution

Expanded sorted keys are **3,8,8,11,11,11**. Key 3 occupies rank zero, key 8 ranks one through two and key 11 ranks three through five. Total occurrence mass is **six** although there are only three structural nodes. Removing one 11 occurrence leaves multiplicity two and total mass five; no node disappears and no height changes, so no AVL rotation is required. Mass fields along the route still change, and the 11 block becomes ranks three through four. Selection must use occurrence mass and local multiplicity, not structural size. A rotation moves the entire counted association; it must not split equal keys into separate order intervals.

### 61. A misleading average-cost claim

An implementation reports mean update time proportional to log n on one workload. Does that establish an AVL or red-black worst-case guarantee? Describe the missing evidence.

#### Solution

It does not. Measurements sample a finite workload and combine algorithmic work with system effects. An ordinary BST under random permutations may show logarithmic average routes while retaining a linear adversarial chain. A worst-case balanced guarantee needs a maintained recursive invariant, a size-to-height proof, and a proof that each valid update restores the invariant at bounded route cost. Independent malformed-state certificates and update traces help catch implementation errors but do not replace those arguments. A doubling experiment is evidence about the tested implementation/workload, not a theorem about every insertion order. Separate expected-input, randomized-algorithm and deterministic worst-case claims.

### 62. A deletion bug caused by a strict outer test

A left-heavy deletion repair uses a single right rotation only when h(y.left)>h(y.right), otherwise choosing LR. Apply it to Question 17 and diagnose the error.

#### Solution

After deleting 60, heavy child 20 has children 10 and 30, both height zero. The strict comparison is false, so the helper chooses an unnecessary double rotation rather than the proved one-rotation equality case. In this tiny example the double result happens to remain balanced; it does not establish the helper's general correctness. A failure witness has initial BST order 80,40,20,10,60,70,100,90, an already AVL shape. Delete 90. Child 40 then has equally tall children 20 and 60. Incorrect LR at 80 makes demoted 40 have left subtree 20 of height one and empty right subtree, so B(40)=2 remains invalid. The correct test is **B(y)≥0 for a single right rotation**, with LR only when B(y)<0. An insertion-only proof excludes equality, but deletion permits it; recheck the contract before reusing its strict test.

### 63. Single inverses versus double mirrors

Why are left and right single rotations structural inverses, while an LR repair and an RL repair are not generally inverse operations on the same tree?

#### Solution

A right rotation at z promotes its left child y and transfers y.right into z.left. A subsequent left rotation at that promoted y reconnects those exact three subtrees and restores z as root. Thus the inverse uses the newly promoted root and the opposite primitive. An LR repair is the composition left-at-child then right-at-root. Its inverse must reverse that exact sequence at the corresponding transformed locations, not simply apply the mirror repair's fixed root/child pattern. LR and RL are geometric mirrors for opposite imbalance configurations; they do not generally satisfy inverse-domain hypotheses on each other's output. Track node roles and intervals to prove inverses rather than swapping labels.

### 64. Nonroot repair must return its new root

Suppose a recursive AVL insertion rotates a subtree rooted at 30 to root 20 but its caller ignores the returned pointer and keeps the old child link to 30. What content becomes unreachable?

#### Solution

In the LL three-key case, right rotation makes 20 the subtree root with children 10 and 30. The demoted 30 no longer points back to 20. If the caller retains its link to 30, the subtree associations **10 and 20** are unreachable from that caller, even though they still exist in allocated memory. A local drawing of the rotated nodes can look correct while the actual global tree loses contents. Assign the returned root to the caller's old left/right link, or replace the global root if this was the whole tree. Parent pointers and caches also need updating. A rotation's return value is part of its semantic contract.

### 65. Full certification changes update complexity

After every AVL insertion an implementation runs a complete O(n) ownership/order/height certificate. What is the resulting cost of n successive insertions, even if each update alone is logarithmic?

#### Solution

At the jth completed state the full certificate visits j nodes. Total certification work is sum j from one through n, equal to **n(n+1)/2=Theta(n²)**. The balanced updates themselves sum to O(n log n), which is dominated by the audits. Thus the combined instrumented workload is quadratic despite a correct logarithmic production algorithm. Full certification is valuable for development and selected validation; it should not be silently included in a claimed logarithmic operation implementation. An audit flag or separate verification pass makes the distinction explicit. Correctness checking is real work and needs its own complexity accounting.

### 66. A linear red-black certificate

Give a one-pass general red-black validation algorithm returning $\beta$. Include ordering, malformed sharing and the root check.

#### Solution

Traverse with inherited open key bounds and a visited-address set. A null returns $\beta$ zero. Reject an address visited twice, a key outside its bounds or a red node with a red actual child. Recursively obtain the left and right $\beta$ values; reject if they differ. Otherwise return the common value plus one when the current node is black. Check a nonempty global root is black. Each address is processed once and each local step uses constant work, so the certificate is **O(n)** time and O(n) visited-set memory, plus stack space. For LLRB, additionally reject red right links. The general checker must not impose that stricter condition without naming the variant.

### 67. Linear construction from sorted keys

Construct a valid general red-black tree from a sorted array in linear time, without inserting n keys individually. Explain the color rule and its root exception.

#### Solution

Build the near-complete BST recursively using midpoint splits, each node once. Its null depths differ by at most one; actual leaves occur at the deepest level H or the preceding level. Color actual nodes at deepest level **red** and all shallower nodes **black**, except that a singleton root stays black. A deepest red node has only null children. A longest route has H black actual nodes followed by a red node; a shorter route has H black actual nodes before null, so equal black count holds. Strict ordering follows sorted midpoint intervals. The construction is **Theta(n)** and yields a general red-black tree, but may have right-red links and therefore does not automatically produce completed 2–3 LLRB. The exact midpoint rule and uniform-depth property are part of the proof.

### 68. Repair only changes constant local metadata

During an AVL rotation, a proposed aggregate stores a sorted vector of every subtree key. Is the standard constant-time augmentation theorem applicable? Contrast subtree sum.

#### Solution

The vector has length proportional to subtree size. Combining or rebuilding it at a large rotated node can require linear movement, so it is neither fixed-size nor constant-time to recompute from children. The standard theorem's hypotheses therefore fail, and logarithmic update time is not established by that theorem. A scalar subtree sum, in a declared constant-word arithmetic model, is computed as sum(left)+key+sum(right) with fixed storage and constant local work. Its refresh preserves O(log n) update cost. With unbounded exact integers, bit complexity must be counted separately. Naming a value 'metadata' does not grant constant-time maintenance.

### 69. Course-pattern reconstruction: insertion contracts

Inspired by CMU Lecture 16's contract exercises, strengthen an AVL insertion specification enough to justify a parent's local repair. Use newly chosen interface wording rather than copying an exercise.

#### Solution

Require an owned ordered AVL input with correct cached fields and a comparable key. Guarantee an owned ordered AVL output whose association map is the old map updated at that key, with no loss or duplication of other entries. Guarantee the output height is either the original height or original height plus one for an absent insertion; existing-key replacement leaves height unchanged. This height-change clause, together with the unchanged opposite child, limits the parent's new balance to magnitude two. The local case proof then justifies repair. Merely promising 'output is AVL' leaves the parent unable to deduce a bounded height change from the contract alone. Value-dependent aggregates need their own preservation/update clause.

### 70. Course-pattern reconstruction: a failed single inner repair

Inspired by CMU's inner-case exercise, use newly chosen keys 50,10,30 to show that a single right rotation is insufficient after inserting 30.

#### Solution

Before insertion, root 50 has left 10 and no right child and is AVL. New 30 attaches as 10.right, making the root balance two and child balance minus one. A single right rotation at 50 yields root 10 with right 50 whose left is 30; 10's left is empty and right height one, so B(10)=−2. The correct LR composition is left at 10 then right at 50, yielding root **30**, children **10,50** and height one. The independently chosen numerical witness preserves the course's reasoning pattern while showing all true heights. A rotation preserving order can still fail the balance goal.

### 71. Course-pattern reconstruction: invariant recognition

Inspired by Princeton §3.3 certification exercises, compare two strict three-key colored shapes: (A) black 20 with red children 10,30; (B) black 30 with black left 20 whose left 10 is red and no right child. Classify both variants.

#### Solution

Shape A has equal $\beta$ one, a black root and no red-red edge, so it is valid **general red-black** but invalid completed **2–3 LLRB** because of the right-red link and persistent four-node. Shape B has no red right link and no red-red edge, but the root's left $\beta$ is one and right $\beta$ zero, so it is invalid **both** variants. These checks show that passing color orientation alone does not prove black balance, and rejecting a general red right link alone would impose the wrong variant. The shape data and full reasoning are independently authored.

### 72. Course-pattern reconstruction: dynamic nearest neighbors

Inspired by Stanford CS166 augmentation, maintain closest points for the changing sorted set 4,11,17,26. Insert 15, then delete 17. Determine the root's best gap/witness after each operation and the required maintenance route.

#### Solution

Initially adjacent gaps are seven, six and nine; the best is **six**, pair **11,17**. Inserting 15 yields sorted 4,11,15,17,26 with gaps seven, four, two and nine, so the best is **two**, pair **15,17**. Deleting 17 yields 4,11,15,26 with gaps seven, four and eleven, so the best becomes **four**, pair **11,15**. Maintain subtree minimum, maximum and best adjacent pair. Refresh the search/physical-removal ancestor route and all rotated nodes in dependency order. The root query is constant-time only because update work maintained its exact witness; a stale minimum gap from the removed pair would be incorrect.

### 73. Course-pattern reconstruction: safe multiway descent

Inspired by Berkeley's top-down explanation, parent [30] has leaves [10] and [40,50]. Prepare descent to delete 10. Show the borrow and result.

#### Solution

The left leaf has one key and the adjacent right leaf has two, so borrow through separator 30. Move **30** into the left leaf and move right sibling minimum **40** into the parent. Before deletion the boxes are parent **[40]**, left **[10,30]**, right **[50]**. Removing 10 then leaves left **[30]**, preserving nonroot minimum capacity and uniform depth. No root shrink is needed. A direct move of 50 to the left would place it above the parent separator and break ordered intervals. In an internal-node version the sibling's leftmost interval child moves with the separator exchange. The new keys and solution reconstruct the pattern independently.

### 74. Worst-case sorted insertions and sorting cost

Compare inserting n increasing distinct keys into an ordinary BST and a maintained AVL tree, then inorder traversal to sort.

#### Solution

The ordinary BST becomes a chain. Insertion j compares j−1 old nodes, giving total n(n−1)/2=**Theta(n²)**, followed by linear traversal. AVL bounds each route by O(log j), so insertion totals **O(n log n)** and traversal **Theta(n)**. In a comparison model, sorting arbitrary permutations also has an Omega(n log n) worst-case lower bound, so AVL-based comparison sorting has **Theta(n log n)** worst-case complexity. This does not say every single insertion takes Theta(log n), nor does it contradict linear construction from an already sorted array whose order information is supplied. The input/knowledge assumptions differ.

### 75. Minimum caching and ownership of the extreme key

An AVL dictionary keeps a pointer to its minimum node. Explain find-min cost and the maintenance after deleting that minimum, including the empty case.

#### Solution

Reading the cached minimum pointer is **O(1)**. Inserting a smaller key replaces it; replacing a value at the same minimum key must retain correct association semantics. When the minimum is deleted, find or already retain its next surviving successor and update the cache during the logarithmic update. If the dictionary becomes empty, set the pointer to null; leaving it at a freed node is a use-after-free bug. A rotation preserves inorder minimum association but may move its allocation position or representation depending on implementation. The maintained pointer guarantee depends on the concrete deletion/ownership strategy, not on height balance alone.

### 76. Reversed sign conventions in an examination

A problem defines balance as right height minus left height. A node reports balance −2 and its left child reports +1. Which repair is required under that convention?

#### Solution

The root's −2 means its **left** subtree is taller by two. The left child's +1 means that child's **right** subtree is taller by one. Therefore the geometry is **left-right**, requiring **left rotation at the left child followed by right rotation at the root**, two primitives. Translate the signs before selecting a table row: under this chapter's left-minus-right convention the same values would be root +2 and left child −1. The rotation directions depend on topology, which remains unchanged by renaming the sign. Copying a balance table without translating its definition reverses the diagnosis.

### 77. Exact-height enumeration is not an insertion distribution

There are 17 AVL shapes on seven keys. May they be treated as equally likely outcomes of a uniform random AVL insertion permutation? Explain what must be counted instead.

#### Solution

No. A uniform permutation gives each of the 7!=5040 insertion orders equal probability. The balancing algorithm maps each order to a completed shape, and different shapes can have different numbers of preimages. Shape count 17 does not establish a uniform distribution on those outputs. To find a shape's probability for a specified insertion algorithm, enumerate or derive the number of orders that map to it and divide by 5040. The map itself differs from ordinary BST insertion because rotations change the shape. A Catalan or AVL shape count measures a combinatorial family; an update-produced probability needs both the algorithm and its input distribution.

### 78. A safe red-black upper bound is not an exact extremum

For n=1000, compute the integer upper height bound from h≤2 $log_{2}$(n+1)−1. Does that establish an achievable exact maximum?

#### Solution

The numerical quantity is 2 $log_{2}$(1001)−1≈18.93445, so integer height satisfies **h≤18**. This is a valid consequence of the general theorem under this chapter's actual-node $\beta$ convention. It is not an existence proof for a 1000-key tree of height 18 and does not specify a particular colored structure. The sharper route/black-layer feasibility constraints or a construction may reduce an exact extremum. In contrast, the AVL minimum recurrence together with the proved no-gap attainable-size lemma establishes an exact maximum. Label necessary bounds and exact achievable results differently.

### 79. Balanced-tree range sums after a priority update

A balanced key tree caches subtree size, key sum and maximum mutable priority. A priority change affects key 25 but no key order or multiplicity. Which fields may change, and does it require an AVL rotation?

#### Solution

Key order, node count, subtree size, key sum and true heights do not change because no structural key update occurs. The **maximum-priority witness** may change at key 25 and along every ancestor whose previous or new maximum depends on it. Refresh that aggregate on the ancestor route with the declared tie rule. No AVL rotation is needed merely for this value change. If the sum field instead sums values or priorities, that field changes too; its definition matters. A balanced shape can still return wrong priority answers when value-dependent metadata is stale. The update has O(log n) route cost without a structural repair.

### 80. Compound final audit with both update types

Construct AVL by inserting 40,20,60,10,30,50,70,25,35. Then delete 10, delete 60 by successor substitution, and insert 65. Determine final inorder, true height, strict rank(65), zero-based select(4) and inclusive count [25,65]. Audit the final balance.

#### Solution

The initial tree is root 40 with left 20 (left 10, right 30 with children 25,35) and right 60 with children 50,70. Deleting 10 exposes a right-heavy 20 with balanced heavy child 30, so one left rotation gives left root 30 with left 20 whose right is 25, and right 35. Deleting 60 replaces it by 70 and removes the old right leaf, leaving 70 with left 50. Insert 65 into that subtree as 50.right; LR at 70 yields right root 65 with children 50,70. Final inorder is **20,25,30,35,40,50,65,70**, and preorder **40,30,20,25,35,65,50,70**. Root height is **three**. Six keys are below 65, so rank is **six**; select(4)=**40**. The inclusive interval contains 25,30,35,40,50,65, count **six**. True child heights verify every balance magnitude is at most one. The one single and one double repair use **three primitives total** during these three updates, independently of construction work.
