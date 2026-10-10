### 28. Two–three tree capacities

A 2–3 tree has edge height three. Find its minimum/maximum key counts and corresponding actual leaf counts.

#### Solution

For minimum capacity all nodes are two-nodes, containing one key and branching twice. The four levels contribute 1+2+4+8=**15 keys** and the bottom level has **8 leaves**. For maximum capacity all are three-nodes, containing two keys and branching three times. The levels contribute 2(1+3+9+27)=**80 keys** and **27 leaves**. These sums agree with $2^{3+1}$−1 and $3^{3+1}$−1. Counting only leaves would omit internal keys; assuming each node contains one key would undercount the full three-node tree. Every extremal leaf has exactly depth three.

### 29. Two–three–four tree capacities

Repeat Question 28 for a 2–3–4 tree of height three. Explain why a binary node count is not the same as its multiway node count.

#### Solution

Minimum capacity is unchanged: one key per two-node gives **15 keys** and eight leaves. Maximum capacity uses three keys per four-node: 3(1+4+16+64)=**255 keys**, with **64 actual leaves**. There are 1+4+16+64=85 multiway nodes in this maximum tree. Its red-black encoding has one actual binary node per key and hence 255 actual binary nodes. Collapsing red clusters changes node grouping, not the key set. Uniform leaf depth is measured in multiway edges; binary paths may contain additional red edges.

### 30. Necessary height bounds for a thousand multiway keys

Compute the necessary edge-height intervals for n=1000 in 2–3 and 2–3–4 trees.

#### Solution

The lower key bound $2^{H+1}$−1≤1000 gives H≤8. For 2–3 maximum capacity, $3^{H+1}$−1≥1000 requires H≥6 because $3^{6}$−1=728 and $3^{7}$−1=2186. Thus **6≤H≤8**. For 2–3–4 maximum capacity, $4^{4}$−1=255 and $4^{5}$−1=1023, so **4≤H≤8**. These are necessary integer bounds obtained by capacity; the problem does not specify a particular update-produced shape. Constructions and legal occupancy, if requested, require an additional argument rather than a bare interval formula.

### 31. B-tree root exceptions

A B-tree has minimum degree three and edge height two. Find its minimum and maximum key counts, including the root exception.

#### Solution

The minimum root has one key and two children. Level one then has two nodes with two keys each; level two has six nodes with two keys each. Total minimum is 1+4+12=**17**, matching 2·3²−1. The maximum root has five keys and six children, every internal node has six children and every node five keys. Total maximum is 5(1+6+36)=**215**, matching 6³−1. Applying the nonroot minimum of two keys to the root would incorrectly give a larger lower bound. 'Minimum degree three' means capacity two through five keys, not exactly three children per node.

### 32. CPU comparisons and block transfers

For a B-tree with minimum degree b=32, describe lookup cost under linear node scanning, binary node search and one-node-per-block storage.

#### Solution

The root-to-leaf route has O(1+$log_{32}$ n) node visits. Linear scanning performs at most a constant multiple of 32 comparisons per node, giving O(32(1+$log_{32}$ n)). Binary searching the sorted node keys performs O($log_{2}$ 32) comparisons per node, so the asymptotic comparison cost is O(log n) for growing n. If one node occupies one transfer block and the root is not assumed cached, block accesses are O(1+$log_{32}$ n). Insertion can still move O(32) packed entries per split; reducing comparison count does not remove those movements. These costs measure different resources and cannot be exchanged without stating the cost model.

### 33. The integer fanout optimization trap

Minimize f(b)=b/ln(b) over integers b≥2. Show why flooring the continuous optimum is insufficient.

#### Solution

Differentiate to obtain f'(b)=(ln b−1)/(ln b)². The function decreases below e and increases above e. Hence the integer minimum must be at two or three. Their values are 2/ln2≈2.88539 and 3/ln3≈2.73072, so **b=3** is smaller; f(4)=4/ln4≈2.88539 and subsequent values increase. Merely taking floor(e)=2 misses the neighboring candidate. This optimizes the given symbolic factor only. It does not prove a universal implementation choice because big-O coefficients, cache costs, key movement and memory layout can change the practical objective.

### 34. Top-down splitting on increasing keys

Insert 10,20,30,40,50,60,70 into an empty top-down 2–3–4 tree. Give the final root/leaf boxes and split events.

#### Solution

The first three keys fill root [10,20,30]. Before inserting 40, split that root, promoting 20 and leaving leaves [10] and [30]; then append 40 to the right leaf. Inserting 50 fills it to [30,40,50]. Before descending for 60, split that full leaf, promoting 40 into the root. The root becomes **[20,40]** with leaves **[10]**, **[30]** and **[50]**. Add 60 and then 70 to the last leaf, which finishes as **[50,60,70]**. There are two splits. The final full leaf is legal and need not be split until an operation actually descends into it.

### 35. Bottom-up promotion is a different variant

Insert the same seven increasing keys into an empty bottom-up 2–3 tree. Compare the final structure with Question 34.

#### Solution

After 10,20 the root is the two-key box [10,20]. Adding 30 makes a temporary [10,20,30], promoting 20 with leaves [10],[30]. Adding 40 fills the right leaf to [30,40]. Adding 50 overflows it, promotes 40 and leaves root [20,40] with leaves [10],[30],[50]. Adding 60 fills the last leaf. Adding 70 promotes 60; the temporary root [20,40,60] then splits. The final root is **[40]**, children **[20]** and **[60]**, and leaves **[10],[30],[50],[70]**, with height two. The top-down 2–3–4 result has height one and allows the three-key leaf. Both are valid for their declared variants; expecting identical shapes is an error.

### 36. Borrow through the separator

In a 2–3–4 tree, parent [20,40] has leaf children [10], [30] and [50,60]. Before deleting 30, borrow from the adjacent right sibling. Give every updated box.

#### Solution

The middle child has only one key, while its right sibling has two. Move the separating parent key **40** down to the middle child, and the sibling's smallest key **50** up to the parent. Parent becomes **[20,50]**, middle child **[30,40]**, right sibling **[60]**, and left child stays [10]. Now removing 30 leaves middle **[40]** without emptying a nonroot node. In an internal-node version, the right sibling's leftmost child subtree would move to the middle node's new right boundary. Moving 60 directly into the middle child without the parent exchange would violate the parent interval.

### 37. Merge and shrink the root

An initial 2–3–4 tree has root [20] and leaf children [10],[30]. Delete 10 using a prepared top-down descent.

#### Solution

Both the target-side leaf and its only adjacent sibling contain one key, so neither can lend. Merge [10], separator 20 and [30] into **[10,20,30]**. The old root becomes empty and is replaced by that merged leaf. Deleting 10 then leaves **[20,30]**, a one-node tree of height zero. The original height was one. Every remaining leaf moved up equally, preserving uniform depth. An empty nonroot node would be invalid, but the emptied root has a specific replacement rule. Its exceptional treatment is part of correctness, not an arbitrary deletion shortcut.

### 38. A general red-black tree that LLRB rejects

Color root 40 black and its children 20,60 red. All grandchildren are null. Check the general red-black and completed 2–3 LLRB invariants, and compute $\beta$(root).

#### Solution

Strict order holds, the root is black and neither red child has a red child. Every root-null route contains only the black root, so **$\beta$=1**. Thus it is **valid general red-black**. Collapsing the red children yields one three-key 2–3–4 node [20,40,60]. It is **not a completed 2–3 LLRB tree**, because the right red link is forbidden and the two red children form a persistent four-node. The same colors can therefore be accepted or rejected depending on the explicitly stated variant. A transient insertion checkpoint may allow them before its normalization finishes.

### 39. A black chain is not balanced

Consider black root 20 with black left child 10 and no right child. Which red-black invariant fails? Does the absence of red nodes certify anything useful?

#### Solution

The root is black and there are no red-red links. Strict BST ordering also holds. However the route through 10 contains two actual black nodes, while the root's right-null route contains one. Equivalently $\beta$(left)=1 and $\beta$(right)=0 disagree at the root. Hence equal black height fails and the tree is **invalid red-black**. The absence of red nodes only makes the red-adjacency condition vacuous; it does not prove route balance. It is a valid two-node AVL shape, because the child edge heights differ by one. The two invariants impose different conditions.

### 40. Translate black-height conventions

Compare this chapter's $\beta$ with a count that excludes the starting node and includes the final black null sentinel. Find the difference for a black actual node, a red actual node and a null start.

#### Solution

Let the alternative count be c(v). For a black actual starting node, excluding that black subtracts one while including the terminal null adds one, so **c(v)=$\beta$(v)**. For a red actual start, exclusion subtracts zero but the null adds one, so **c(v)=$\beta$(v)+1**. At a null start, the usual excluded-start path has count zero, and this chapter's $\beta$(null)=0, so both are zero. The separate null base must be stated rather than obtained by treating a null start as an ordinary red/black actual node. This translation explains why formulas can agree at a black root yet differ inside a tree.

### 41. Black-height size bounds

A general red-black tree has $\beta$(root)=3. Find minimum/maximum possible numbers of actual key nodes and justify both equality structures.

#### Solution

There are three black layers after collapsing red clusters. Minimum capacity uses one-key clusters with branching two, giving **2³−1=7** actual keys: a perfect all-black seven-node tree. Maximum capacity uses three-key clusters with branching four at every layer, giving **4³−1=63** actual keys. Each cluster is represented by a black middle key and red outer children; the red children have black roots of the next clusters or null endpoints. Both structures have three actual black nodes on every root-null route and no red-red edge. Binary height may differ because maximum clusters add red edges.

### 42. Infer possible black heights from size

A valid general red-black tree has 31 keys. Infer the necessary $\beta$(root) interval using only size bounds. Give a witness for its upper endpoint.

#### Solution

From 31≤$4^{b}$−1, b must be at least three, since b=2 holds at most 15. From $2^{b}$−1≤31, b must be at most five, since b=6 needs at least 63. Thus the necessary interval is **3≤b≤5**. A perfect all-black tree with 31 keys has five actual black layers and realizes b=5. The inequalities are necessary; they do not specify a particular colored tree or count its encodings. A construction for another endpoint must be given if requested, rather than inferred solely from an interval bound.

### 43. Root-null path lengths and actual heights

A general red-black tree has $\beta$(root)=4. Bound root-null link length and actual edge height. Explain why subtracting null changes a ratio argument.

#### Solution

Every root-null route contains four black actual nodes and at most four red actual nodes, so it visits **four through eight actual nodes** and traverses the same **four through eight child links to null**. The deepest actual edge height is at most **seven**, because the route with eight actual nodes has seven edges before its terminal null. The ratio of root-null route lengths is at most two. Actual root-to-leaf edge lengths subtract one, so simply keeping the same ratio can fail at small depths; a singleton has actual height zero. A counting convention must stay fixed throughout the comparison.

### 44. Recoloring a red-uncle insertion

Let black root 40 have red children 20,60. Insert 10 as a red child of 20 using the classical algorithm. Describe repair and final colors.

#### Solution

Insertion adds no black node to the route but creates red 20 with red child 10. The uncle 60 is red, so blacken **20 and 60** and redden **40**. The active node becomes 40. Since it is the root, blacken it and stop. Final colors are black 40, black 20, black 60, red 10; the other child links are null. Beta(root) is now two on every route. There are **zero primitive rotations** and three assignments in the red-uncle transformation plus the root blackening. Recolors can change the common black count uniformly at the root without violating the equal-path condition.

### 45. Black-uncle line insertion

Starting with black 30 and red left child 20, insert red 10 using the classical algorithm. Give repair, colors and primitive count.

#### Solution

The initial tree is valid because the red 20 contributes no additional black node. New red 10 creates a red-red left-left line at black grandparent 30; the uncle is null and hence black. Blacken 20, redden 30 and right-rotate 30. Final root is **20 black**, with **10 red** and **30 red** children. There is **one primitive rotation**. The root-to-null black count remains one and red nodes have no red children. This general red-black result is not completed 2–3 LLRB, since it has two red children and a right red link; a different declared algorithm may normalize it differently.

### 46. Black-uncle triangle insertion

Starting with black 30 and red left child 10, insert red 20 using the classical algorithm. Give both primitives and final colors.

#### Solution

The new 20 is the right child of red 10, forming a left-right triangle below black 30 with a black/null uncle. Left-rotate **10**, which converts the active geometry into a left-left line with 20 above 10. Update the active roles; then blacken **20**, redden **30** and right-rotate **30**. Final root is **20 black**, children **10 red** and **30 red**, with **two primitives**. Skipping the triangle conversion leaves the wrong intervals or unresolved red adjacency. Black balance is preserved by the paired recolor/line rotation, not by assigning colors independently of the topology.

### 47. Why a new classical node is red

Explain why inserting a black leaf below a nonroot null position generally breaks a valid red-black tree, whereas inserting red preserves path black counts before repair.

#### Solution

At the original null position, no actual black node is counted. Replacing it by a black actual leaf adds one black unit to routes through that position but not to sibling routes. The nearest common ancestor therefore receives unequal child black counts. A red actual leaf instead contributes zero and its two null endpoints preserve the prior count, so the only possible new internal violation is a red parent with a red child. This isolates insertion repair to color adjacency and root blackening. The empty-tree case is exceptional: the new root is blackened uniformly because there is no competing old route.

### 48. Deletion uses the physically removed color

A black target has two children. Its inorder successor is a red leaf. Classical deletion copies the successor association into the target and removes that red leaf. Is a missing-black repair required?

#### Solution

The target position remains in the tree with its original black color; only its association changes. The physically removed successor position was **red**, so its removal subtracts no black unit from any route. Hence **no missing-black repair is required**. The BST successor copy must include the full value, and size/other aggregates still need updates. If the successor had been black, a deficit could arise even when the target itself was red. Tracking target color instead of removed-position color confuses association semantics with color topology and chooses the wrong repair branch.

### 49. A red replacement absorbs a black deficit

A removed black node has one surviving red child. Explain the classical repair and why no rotation is needed.

#### Solution

Attach the surviving red child in the removed node's position and **blacken it**. Every route that previously passed through the black removed node and then the red child now passes through the replacement black child, retaining the same number of actual black units. Its child subtrees were already black-height-consistent and contain no red-red adjacency because the replacement was red before the operation. No primitive rotation is required. Parent links and aggregates must still be updated. The conclusion uses the formerly valid tree and a one-child physical removal; it is not a general permission to blacken an arbitrary red node without checking path counts.

### 50. Case two: absorb or propagate

In classical missing-black deletion, the active node is a left child; its sibling and both nephews are black. Compare the outcomes when the parent is red and when it is black.

#### Solution

Reddening the black sibling removes one ordinary black unit from that side, allowing the missing unit to move to the parent. If the parent is **red**, blacken it: that adds the required black unit to both of its child routes, and the deficit is absorbed. If the parent is **black**, it cannot gain another persistent black color; keep a single virtual deficit at that parent and continue upward. This case performs **zero rotations** in either outcome. A red parent stops propagation, while a black parent may repeat the case higher up. The virtual 'double black' is a counting ledger, not a node field with a third stable color.

### 51. Near and far nephews must be relative to the active side

In a classical deletion step the active deficit is p.right and sibling w=p.left. Identify near/far nephews and the mirror of the final absorption rotation.

#### Solution

The near nephew is **w.right**, because it is toward the active right side; the far nephew is **w.left**. If w is black with a red far nephew, give w the old parent color, blacken p and **w.left**, and **right-rotate p**. The mirror would be left rotation when the deficit is the left child. A memorized instruction to blacken 'the right nephew' is incorrect without stating which side is active. Recompute the sibling after any preceding conversion rotation. This positional definition preserves the correct interval decomposition and black-count redistribution.

### 52. The classical three-rotation deletion bound

Prove the at-most-three primitive rotation bound for the declared classical deletion algorithm. Why can case two repeat without violating it?

#### Solution

A red-sibling conversion in case one uses one primitive and yields a black sibling under a now-red parent. If case two follows, that red parent absorbs the deficit and stops; it cannot propagate beyond that conversion. Otherwise case three may use one sibling rotation, immediately followed by case four's one parent rotation, which absorbs the deficit and stops. Without case one, only the latter two can occur. Case two under a black parent may repeat upward, but performs no rotation at all. Thus at most **one case-one, one case-three and one case-four primitive**, total **three**, occur. Recolor assignments and route steps can still be logarithmic. This proof does not apply to recursive LLRB deletion.

### 53. The sibling cannot be null in a reachable deficit step

For a nonroot classical missing-black step obtained from a formerly valid tree, show why its sibling must be an actual node rather than null.

#### Solution

Before the physical black removal or deficit propagation, the active-side route contributed the sibling's equal black count. A genuine missing-black unit means the old active-side count was at least one more than its present ordinary count, hence at least one. A null sibling has this chapter's $\beta$ zero and cannot match that positive old contribution. The same invariant is preserved when case two moves the deficit to a parent. Therefore a reachable nonroot deficit has an actual sibling. This reasoning relies on a valid pre-update tree and exactly one deficit; arbitrary corrupted inputs may violate it and need explicit rejection rather than unsafe nephew dereferences.

### 54. Variant-specific rotation bounds

An implementation recursively normalizes an LLRB tree at every ancestor. May it claim the classical insertion bound of two total rotations and deletion bound of three? State a justified bound instead.

#### Solution

No. The constant classical bounds come from its specific propagation and terminating repair cases. Recursive LLRB normalization performs constant local work at each visited ancestor, and top-down resource transfers can rotate at more than one level. Its generally justified bound here is **O(log n) primitive work and total time**, not the classical constants. Exact traces may use fewer rotations, but a small observed count is not a universal theorem. Algorithms implementing the same ordered dictionary can maintain related invariants by different schedules. Every claimed bound must name the schedule and its proof, especially when an examination asks for rotations rather than only asymptotic update time.
