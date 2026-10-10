### 55. A joint ancestor probability

Under uniform permutations of keys 1 through 6, find the probability that 2 is an ancestor of 5. Are the ancestor indicators for keys 2 and 3 independent?

#### Solution

Key 2 is an ancestor of 5 exactly when it appears first among 2,3,4,5, so its probability is $1/4$. Key 3 is an ancestor of 5 exactly when it is first among 3,4,5, with probability $1/3$. Both events hold exactly when 2 precedes 3, which precedes 4 and 5 within those four keys. There are two such relative orders, differing only in the order of 4 and 5, out of 24, giving joint probability $1/12$. Here that equals the product, so these particular two nested-interval indicators are independent. This calculation does not justify assuming independence for arbitrary tree events; for example the incompatible events “2 is ancestor of 5” and “5 is ancestor of 2” cannot both hold. Linearity of expectation needs no such assumption.

### 56. Root-rank distribution and a weighted shape

For uniform insertion permutations of five distinct ranks, find the probability that the root has rank 3. Conditional on that root, find the probability that both two-key children increase along their right edges.

#### Solution

Each key is equally likely to be inserted first, so root rank 3 has probability $1/5$. Conditional on this event, each two-key subtree has either local order with probability one half. Relative orders in the disjoint left and right key sets are independent under a uniform permutation, so both right-oriented chains occur with conditional probability one fourth. The joint shape probability is $1/20$. Its subtree-size product is $5\cdot2\cdot2=20$, agreeing with the hook formula. Interleaving the two local sequences accounts for six producing full permutations, $6/120=1/20$.

### 57. Conditional expected subtree sizes

For a random-permutation BST on $n$ distinct keys, find the expected left-subtree size and the probability that exactly $k$ keys are in the left subtree. Does equality of expected left and right sizes prove that the root is balanced in every realization?

#### Solution

The root rank is uniform from 1 through $n$, so left size is uniform over 0 through $n-1$. Its probability at each $k$ in that range is $1/n$, and its expectation is $(n-1)/2$. The right-size expectation is the same by symmetry. Yet root rank 1 gives an empty left subtree and all $n-1$ keys on the right, with positive probability $1/n$. Equality of averages is not a pointwise balance condition. Even root-level equal sizes would not establish height balance deeper in the tree.

### 58. Insertion orders subject to an extra precedence

For the perfect seven-key tree in Question 28, count producing insertion orders with key 1 preceding key 7. Explain the symmetry used rather than dividing automatically.

#### Solution

The full count is 80. Exchanging the entire left and right subtrees by mapping each rank $k$ to $8-k$ preserves the shape and its ancestor-before-descendant constraints, but exchanges labels 1 and 7. It pairs every producing order with 1 before 7 to a producing order with 7 before 1. The two events partition the orders since distinct keys cannot tie, so each count is 40. A nonsymmetric shape may lack this bijection; an arbitrary extra precedence cannot always be enforced by halving the total.

### 59. An adjacent pair and its parent

In a strict BST, let a leaf $x$ have parent $p$. Prove that $p$ is either the predecessor or successor of $x$. Would the statement hold if $x$ were not a leaf?

#### Solution

If $x$ is a left leaf, it has no right subtree and is reached from the left side of its parent. The successor-climb rule therefore stops immediately at $p$. If it is a right leaf, the predecessor rule similarly returns $p$. For a nonleaf this can fail: root 20, left child 10 with right child 15 makes 10's successor equal to 15, not 20; 10's predecessor may be absent or another descendant. The leaf hypothesis removes the possible nearer descendant on the relevant side.

### 60. The two external gaps adjacent to a leaf

In a strict BST a leaf key is at depth $d$. Find the failed-search comparator cost in its two null-child gaps, and compare their contribution with its successful cost.

#### Solution

Each null child is at external depth $d+1$, so a failed query in either gap visits exactly the root-to-leaf route and uses $d+1$ comparisons. A successful lookup of that leaf also uses $d+1$ comparisons and stops at the leaf rather than testing a null child. The gap intervals may have different query probabilities, so equality of these individual costs does not imply equal weighted contributions. If the node is not a leaf, one or both neighboring gaps can lie deeper inside a child subtree.

### 61. Counting nodes from leaves and one-child nodes

A finite nonempty binary tree has $n_0$ actual leaves, $n_1$ one-child nodes and $n_2$ two-child nodes. Derive a relation between $n_0$ and $n_2$ and determine total nodes when $n_0=9$ and $n_1=6$.

#### Solution

The child-edge count is $n_1+2n_2=n-1$, while $n=n_0+n_1+n_2$. Subtracting yields $n_0=n_2+1$, independent of the one-child count. Thus nine leaves imply eight two-child nodes, and total nodes are $9+6+8=23$. This concerns actual leaves, not the $n+1=24$ null gaps. For an empty tree the nonempty edge equation and the leaf relation do not apply unchanged. The identities need no BST order, so they also audit a BST's structural counts.

### 62. Dyadic leaf mass and null gaps

For the chain of three actual nodes at depths 0,1,2, compute actual-leaf mass $\sum2^{-d}$ and null-gap mass. Generalize the null-gap identity to every finite binary tree.

#### Solution

The only actual leaf has mass $2^{-2}=1/4$. The four null gaps have depths 1,2,3,3, so their mass is $1/2+1/4+1/8+1/8=1$. For a general finite tree, give the root mass one and split each actual node's mass equally between its two child positions. Actual children continue splitting; null gaps receive the mass permanently. Every finite branch terminates, so all mass reaches null gaps and their sum is exactly one. Actual leaves occupy only some of these structural allocations, making their sum at most one. The two kinds of leaves must not be conflated.

### 63. Catalan recurrence from root decomposition

Compute $C_4$ from the root-size recurrence and explain each contribution. What would the recurrence count if left and right children were not distinguished?

#### Solution

With $C_0=1,C_1=1,C_2=2,C_3=5$, the four contributions for left sizes 0,1,2,3 are $1\cdot5$, $1\cdot2$, $2\cdot1$, $5\cdot1$, totaling 14. The recurrence treats the ordered pair of child shapes as distinct, appropriate because a BST's left and right links have different meanings. If children were unordered, mirror pairs could collapse and symmetric pairs would need separate handling; the same Catalan recurrence would not count that new class. A fixed sorted key set labels each of the 14 ordered shapes uniquely.

### 64. Maximum height conditional on the root

A BST has seven distinct keys and root rank 4. Determine the maximum possible height and give an attaining insertion order. Is the minimum-height tree forced?

#### Solution

There are three smaller keys and three larger keys. Either child can be a three-node chain of height 2, making whole-tree height 3. No child can contain more than three nodes, so height 3 is the maximum with this fixed root. Order 4,1,2,3,5,6,7 attains it. Median-first at only the root does not force a perfect height-two tree; the rest of each subtree's insertion order matters. The perfect tree is attained by 4,2,1,3,6,5,7 and has height 2.

### 65. Sorted construction with duplicate compression

A sorted array is 1,1,1,3,5,5,8,8. Design a linear-time counted-BST construction and identify distinct-node size, mass and minimum possible edge height.

#### Solution

Scan adjacent equal keys into pairs (1,3),(3,1),(5,2),(8,2), costing linear time in array length. Build midpoint subtrees directly from the four distinct pairs and compute each node's mass from its count and child masses. There are four distinct nodes and mass eight. The minimum height for four nodes is $\lceil\log_2(5)\rceil-1=2$. Treating all eight occurrences as strictly ordered node keys would violate the unique-key invariant. Computing median by occurrence rank still uses mass eight, not the distinct-node count four.

### 66. Rank validation is not pointer validation

If every stored node's keys appear sorted in a separately supplied array and that array's rank/select operations are consistent, does this validate the BST's child pointers? Give a failure and state the actual checks needed.

#### Solution

No. The array could contain the correct set while a tree link omits a node, duplicates ownership of a subtree or creates a cycle. Array rank/select consistency validates that array's indexing, not reachability or ordering of the actual pointer graph. Traverse the actual owned graph with identity tracking to reject cycles and shared children, then check ancestor intervals, parent back-links and local augmentation equations. Comparing reached keys with the expected dictionary validates content separately. A specification must name the object it certifies rather than infer graph correctness from an unrelated representation.

### 67. Cost of naive interval-independent validation

A validator computes the maximum key of each node's entire left subtree by a fresh traversal before recursively checking both children. Analyze a left chain of $n$ keys and give a linear replacement.

#### Solution

At the root it traverses $n-1$ nodes, then at the next node $n-2$, continuing to zero. These scans alone sum to $n(n-1)/2$, making worst-case time quadratic. An interval validator passes ancestor bounds once and examines each actual node once. Alternatively a postorder helper returns each subtree's minimum, maximum and validity so those aggregates are reused rather than rescanned; that also takes linear time. A correct criterion can still have a poor implementation cost when its subresults are repeatedly recomputed.

### 68. Recovering an insertion order from a fixed shape

For any strict BST, show that its preorder is a producing insertion order. Is its inorder always a producing insertion order for the same shape?

#### Solution

Preorder places every ancestor before its descendants. The sufficiency theorem for producing orders therefore shows that ordinary insertion of that preorder reconstructs exactly the tree. Inorder lists keys increasingly, so ordinary insertion creates a right chain. It reproduces the original shape only when the original tree is that right chain, including the empty and singleton boundaries. Postorder puts descendants before the root and generally fails the necessary root-first condition. The statement concerns reconstruction through insertion without rotations or balancing.

### 69. All course-pattern contracts in one implementation

Reconstruct the CMU-style iterative insertion task with keys 18,9,27,6,12,24,30 and then replacement of key 12's value. State the trailing-parent invariant and all outer-root cases.

#### Solution

Maintain current pointer v and its last nonnull parent p. Before each iteration, v is the only subtree that can contain the key, and p is its parent when p exists. A matching key changes only its value and returns. At null, allocate the new node and attach it to p on the side determined by the last comparator; if p is null, update the dictionary root. The seven distinct insertions create a perfect height-two tree, and replacement leaves node count seven. This is an original reconstruction of the lecture's iterative-insertion pattern; the values and solution are independently chosen. Augmentation additionally requires storing the ancestor route and refreshing it backward.

### 70. Berkeley-style bracketing with exact endpoints

Reconstruct a nearest-neighbor exercise for stored keys 6,14,19,31. Find floor and ceiling at queries 5,14,20,40 and state each missing-bound result.

#### Solution

At 5, floor is absent and ceiling is 6. At exact stored key 14, both floor and ceiling are 14; strict predecessor and successor would instead be 6 and 19. At 20, floor is 19 and ceiling is 31. At 40, floor is 31 and ceiling is absent. The candidate search must represent absence explicitly instead of returning a numerical sentinel. This is an original reconstruction of Berkeley's bracketing-query pattern. Equality must be handled before continuing a strict neighbor descent, or the exact-endpoint semantics change.

### 71. Princeton-style augmentation certification

Give a complete recursive check of subtree-size consistency and explain whether it proves BST order. Then estimate the cost of checking rank(select(j)) for every stored rank by repeated path queries.

#### Solution

For null return actual size zero and validity true. For a node recursively obtain both actual child sizes and validity flags; return their sum plus one, and require its stored size to equal that sum. This bottom-up computation is linear and validates all size fields. It says nothing about key inequalities, so combine it with a separate interval check. Repeated rank and select checks across $n$ ranks cost $O(n(h+1))$, potentially quadratic on a chain; they can be useful additional diagnostics but are not the most efficient size certificate. This is an original reconstruction of the booksite's metadata-certification pattern.

### 72. Stanford-style null and lifetime diagnosis

Design an interface for maximum on an empty or nonempty BST that permits the smallest signed integer as a real key. Explain why returning that extreme as an absence sentinel is ambiguous.

#### Solution

Return an optional entry or a pair `(found, entry)` rather than a legal key alone. On empty input set found false; otherwise follow right links to an actual node and return found true with its association. A singleton whose key is the smallest signed integer then returns that key unambiguously. Throwing an exception or stating a nonempty precondition are also coherent interfaces, but they impose different caller obligations. This is an original reconstruction of Stanford's empty-tree diagnostic pattern. If an entry pointer is returned, its validity after later deletion must be part of the ownership contract.

### 73. MIT-style inclusive rank in a schedule

Reservations are 5,15,25,35,45. A scheduling API reports how many times are at most a query. Find its results at 25,26,4 and relate them to this chapter's strict rank.

#### Solution

The inclusive counts are 3,3,0. Strict ranks are respectively 2,3,0. Add the stored-query membership indicator to strict rank, giving the correct inclusive values. For a query above every reservation the count is five, which is a valid count but not a valid zero-based select index. This is an original reconstruction of MIT's scheduling-rank pattern. Rank's definition must be specified before using a course's formula; equality is exactly where the two conventions differ.

### 74. A weighted-search root choice

Three ordered keys have successful-query probabilities 0.8,0.1,0.1 and no failed queries. Compare a median-root tree with a minimum-root tree whose right child is the largest key and whose left descendant there is the middle key.

#### Solution

The median-root tree has costs 2,1,2 for the ordered keys, so weighted expectation is $0.8\cdot2+0.1\cdot1+0.1\cdot2=1.9$. The specified minimum-root tree has costs 1,3,2 and expectation $0.8+0.3+0.2=1.3$. Its height is worse, yet its probability-weighted expected query cost is better. Balancing optimizes worst-case path length, not every weighted workload. This comparison is not a proof of global optimality among all possible trees; it establishes the stated pairwise claim using the explicit probabilities.

### 75. Building a range iterator

Design a sorted iterator reporting keys in inclusive interval [a,b] without materializing every key first. State setup time, aggregate emission time and workspace.

#### Solution

Use a stack descent to the first key at least a: at a node at least a, push it and go left; at a smaller node, go right without pushing it. Then repeatedly pop the next key, stop if it exceeds b, and push the left spine of its right subtree. The setup follows one route, costing $O(h+1)$. Complete emission of m matching entries costs $O(h+m+1)$ in aggregate because route edges are shared rather than restarted. Workspace is $O(h+1)$. A single next step can still descend a long spine; the aggregate bound does not grant every emission constant worst-case cost.

### 76. Mixed-direction chain null-depth distribution

For any chain of $n\ge1$ nodes, determine the multiset of null-gap depths and derive the external sum directly. Does the direction pattern affect it?

#### Solution

Each of the first $n-1$ actual nodes has one missing child, giving gap depths 1,2,...,$n-1$. The terminal actual leaf has two missing children, each at depth n. Thus $E=n(n-1)/2+2n=n(n+3)/2$. Left/right directions change which sorted gap occupies each depth, but not this multiset or its sum. A query distribution over numeric intervals can still make the direction pattern relevant, because those intervals may receive different probabilities. Uniform gaps disregard that distinction.

### 77. Can a deletion increase edge height?

For association-copy successor deletion in a plain strict BST, can the tree's edge height increase? Can its stored root key change? Justify both answers, including root and singleton cases.

#### Solution

Height cannot increase. Zero/one-child deletion removes an actual node and possibly shortens descendant routes. Two-child deletion keeps the target position, copies an association, and removes a successor with at most one child, again creating no longer route. The root key can change when the root itself is deleted; Question 8 changes it from 40 to 60. A one-child root deletion can change the root object too, and singleton deletion yields empty height minus one. This proof applies to plain deletion without balancing rotations; a repair algorithm can change intermediate heights differently while maintaining its own invariant.

### 78. Failed-search insertion equivalence

For an absent key q in a strict BST, show that its failed-search comparison count equals its depth after insertion. Compare the cost of a subsequent successful lookup and discuss equal-key insertion.

#### Solution

Failed search visits the ancestors of the terminal null position, so if that position has depth g there are exactly g comparator calls. Insertion replaces it by the new node at depth g and does not move its ancestors. A later successful lookup adds comparison with the new node, using g+1 calls. Equal-key insertion does not reach a null position; it stops at a node of depth d and uses d+1 calls while leaving depth unchanged. Confusing these cases creates an off-by-one in total construction work and replacement costs.

### 79. Merge two ordered BST inventories

Given two strict BSTs with total $n$ distinct-node entries and possibly overlapping keys, design a linear-time construction of a balanced union dictionary with an explicit overlapping-value rule. Can ordinary insertion of the merged sorted list preserve that bound?

#### Solution

Traverse each input inorder to obtain sorted entries, merge the two sorted streams and resolve equal keys under a declared rule, for example choosing the second dictionary's value. Direct midpoint construction on the merged distinct list allocates each result node once, giving total $\Theta(n)$ time and linear materialized workspace. Ordinary insertion of the merged increasing list instead produces a right chain and uses quadratic comparisons in its length. Streaming construction can reduce materialization only with additional counting and iterator design; it is not implied by simply merging streams.

### 80. Full contract audit after a compound update

Insert 40,20,70,10,30,60,80,25,65, replace key 30's value, delete 40 by successor copying, then insert 50. Give final preorder, size, internal path sum, strict rank of 65 and select(4). List the contracts this result checks.

#### Solution

Replacement changes no key or size. Deleting 40 yields root association 60, with 70.left=65; inserting 50 descends through 60,20,30 and attaches as 30.right. Final preorder is 60,20,10,30,25,50,70,65,80. Size is 9. Depths are 0; two nodes at depth 1; four at depth 2; two at depth 3, so $I=0+2+8+6=16$. Sorted keys are 10,20,25,30,50,60,65,70,80, giving strict rank(65)=6 and select(4)=50. Audit global bounds, exact content, retained values, root assignment, child ownership, parent links if present, size equations and rank conventions separately. A sorted inorder alone does not prove the other contracts.
