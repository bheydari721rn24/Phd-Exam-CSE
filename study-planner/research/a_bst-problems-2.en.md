### 28. Counting orders for a seven-node perfect shape

For root 4, children 2 and 6, and leaves 1,3,5,7, count insertion permutations producing exactly this tree. Give its probability under uniform permutations.

#### Solution

Root 4 must be first. Each three-node child shape has two valid local orders because its root must precede its two leaves. Interleave the left and right triples in $\binom{6}{3}=20$ ways. Therefore $W=20\cdot2\cdot2=80$. Equivalently, the subtree-size product is $7\cdot3\cdot3=63$, so $W=7!/63=80$. Uniform permutations assign probability $80/5040=1/63$. Uniform Catalan shapes would give probability $1/C_7=1/429$, a different model.

### 29. An asymmetric hook-product calculation

Insert 5,2,1,4,3,8,7,9. Find the number of insertion orders producing the same final tree and its probability.

#### Solution

The root has a four-node left subtree and a three-node right subtree. Left root 2 has leaf 1 and right root 4 with left leaf 3, so its local count is $\binom{3}{1}=3$. Right root 8 has leaves 7,9, giving count 2. Interleaving the two child sequences after 5 gives $\binom{7}{4}\cdot3\cdot2=210$. Subtree sizes multiply to $8\cdot4\cdot2\cdot3=192$, confirming $8!/192=210$. The probability is $1/192$. Requiring an entire child block to precede the other would omit most valid interleavings.

### 30. All random three-key trees

Enumerate the six insertion permutations of keys 1,2,3, group them by resulting shape, and find expected height and expected internal path length.

#### Solution

Orders 2,1,3 and 2,3,1 produce the balanced tree of height 1 and internal sum 2. Each of 1,2,3; 1,3,2; 3,1,2; 3,2,1 produces a different chain of height 2 and internal sum 3. Thus expected height is $(2\cdot1+4\cdot2)/6=5/3$, and expected internal sum is $(2\cdot2+4\cdot3)/6=8/3$. The five possible shapes are not equally likely. Uniformly choosing those shapes would instead yield height $9/5$ and internal sum $14/5$.

### 31. Chains with changing directions

For four keys, count all insertion permutations yielding a chain, list them, and find their probability. Explain why only counting sorted orders is wrong.

#### Solution

The first inserted key must be either the minimum or maximum of the remaining set; otherwise it would have nonempty children on both sides. Repeat that choice until one key remains. This gives $2^3=8$ orders: 1,2,3,4; 1,2,4,3; 1,4,2,3; 1,4,3,2; 4,1,2,3; 4,1,3,2; 4,3,1,2; 4,3,2,1. Each creates a different left/right chain shape. The probability is $8/24=1/3$. Increasing and decreasing orders count only two of these eight possibilities.

### 32. Catalan counts versus permutation counts

Find the number of strict BST shapes on five fixed distinct keys and compare it with the number of insertion permutations. Why is division of these two totals not a probability for each shape?

#### Solution

The number of shapes is $C_5=\binom{10}{5}/6=42$, while insertion permutations number $5!=120$. The ratio $120/42$ is an average multiplicity of producing orders, not the multiplicity of every shape; indeed it is not an integer. A chain has multiplicity one, while a more branching shape has several valid descendant interleavings. For any specified shape use $W(T)=5!/\prod_vs(v)$ and its probability $1/\prod_vs(v)$. Catalan enumeration counts ordered left/right shapes, so mirroring a nonsymmetric tree generally produces a different shape.

### 33. Fixed-rank expected depth

Under uniform insertion permutations of seven distinct keys, find expected depths of ranks 1 and 4 and their expected successful comparator counts.

#### Solution

Using $H_7=363/140$, rank 1 has expected depth $H_1+H_7-2=223/140$. Rank 4 has $2H_4-2=2(25/12)-2=13/6$. Add one to convert depths to successful comparator counts: $363/140$ and $19/6$. The middle rank is expected to be deeper than an extreme even though a balanced deterministic tree would place a central key at the root. Root rank is uniform in the random-permutation model, so the deterministic median-first construction is not that distribution.

### 34. Expected insertion work

Insert ten distinct keys in uniform random order. Find the exact expected total insertion comparisons, the expected uniform successful-search cost in the final tree, and their relationship.

#### Solution

The insertion cost of each key equals its final depth because later insertions do not move existing nodes. Therefore total cost is internal path length. With $H_{10}=7381/2520$, its expectation is $22H_{10}-40=30791/1260$. Adding ten and dividing by ten yields successful mean $43391/12600$. A new key's insertion cost excludes comparison with itself, whereas a later successful search includes that final comparison. This is why the two quantities differ by one per stored key when averaged.

### 35. Expected failed search under a specified gap model

For a uniformly random five-key insertion permutation, then a uniformly selected one of its six null gaps, find expected failed-search comparisons. Would uniformly choosing a real number between the smallest and largest keys give the same model?

#### Solution

The expected internal path sum is $12H_5-20=37/5$. Adding $2n=10$ gives expected external sum $87/5$, then dividing by six gives $29/10$. Equivalently, $2H_5-10/6=29/10$. A real-number query gives gap probabilities proportional to interval lengths and excludes the outer gaps when restricted between the endpoints. It therefore need not give the same expectation. Both randomness stages are stated here; choosing a uniform permutation alone does not specify the query distribution.

### 36. Why expected depth does not prove expected height

Suppose every fixed rank in a random BST has expected depth at most $2\ln n$. Is it valid to conclude expected height is at most $2\ln n$ by taking a maximum? Give a concrete probabilistic counterexample to that inference.

#### Solution

No. In general the expected maximum is at least the maximum of expectations, with the inequality in the wrong direction for the proposed bound. As a counterexample, choose one of $n$ positions uniformly and set its value to $n$, all others to zero. Each fixed position has expectation 1, while the maximum is always $n$. This example is about the logical inference, not a model of tree depths. Random BST height has a logarithmic theorem, but it needs a separate argument controlling unusually long routes and their dependence.

### 37. Direct construction versus ordinary insertion

For sorted keys 1 through 15, choose midpoint roots recursively. Give the first seven preorder keys, exact ordinary insertion comparisons in that order, and the direct-construction operation count up to asymptotic order.

#### Solution

The preorder begins 8,4,2,1,3,6,5. The final tree is perfect of height 3. Ordinary absent-key insertion comparisons equal final depth sum $I=34$, because no existing node is moved. Direct construction allocates each of the 15 nodes and assigns each of 14 nonnull child links once; it therefore costs linear time. For growing perfect sizes, depth sum is $\Theta(n\log n)$ while allocation and link assignment stay $\Theta(n)$. The same resulting shape does not imply the same construction cost.

### 38. Median-first does not require a perfect tree

Construct a minimum-height BST from sorted keys 1 through 10 using the lower midpoint of each half. Give root, height and subtree sizes at the root. Explain why it is not perfect.

#### Solution

The lower midpoint key is 5, leaving four keys on the left and five on the right. Applying the same rule recursively gives height 3, since capacity 7 at height 2 is insufficient while capacity 15 at height 3 suffices. The root's left and right sizes are 4 and 5. A perfect height-three tree has 15 nodes, not ten; minimum height only requires that no deeper route is necessary, not that every possible position is occupied. Stored sizes and heights must still be computed from the actual allocated children.

### 39. Range-reporting complexity with no output

In a right chain of keys 1 through $n$, report keys in $[n+1,n+2]$. How many actual nodes are visited? Does zero output contradict an output-sensitive bound?

#### Solution

Every current key is below the lower endpoint, so the algorithm descends right through all $n$ nodes and then reaches null. It emits no keys but uses $n$ actual-node comparisons. Height is $n-1$, so $O(h+m+1)$ becomes $O(n)$ when $m=0$, fully consistent with the observed work. Claiming $O(m)$ would incorrectly predict zero work. A balanced tree would reduce the boundary route to logarithmic length but would still need to locate the empty interval.

### 40. LCA versus an interval split point

In Question 3's tree, find LCAs of stored pairs (25,10), (25,65) and (60,65). What would the same descent return for absent pair (26,28), and what can it legitimately mean?

#### Solution

For 25 and 10, both are below 40 and straddle 20, so LCA is 20. For 25 and 65 they split at 40. For 60 and 65, descent reaches node 60 itself, an ancestor of 65, so LCA is 60. Queries 26 and 28 descend through 40,20,30,25 and reach null because neither stored key lies in that interval. More generally an absent pair can still straddle an existing node, but that node is only a range split point. Membership checks are required to promise an LCA of actual nodes.

### 41. A rotation with augmentation

Root 20 has left leaf 10 and right child 40; node 40 has leaves 30,50. Perform one left rotation at 20. Give all changed links, the new sizes of 20 and 40, and the inorder sequence.

#### Solution

Node 40 becomes the root. Set 20.right to 30 and 40.left to 20; 20.left stays 10 and 40.right stays 50. The old root link must now point to 40. Node 20 has subtree size 3 and 40 has subtree size 5. Recompute 20 first because 40's new size uses 20's updated size. Inorder remains 10,20,30,40,50. With parent links, 40.parent becomes null, 20.parent becomes 40 and 30.parent becomes 20. The operation preserves order but is not by itself proof of a global AVL invariant.

### 42. A mirror preserves shape size but reverses order

Swap left and right child links at every node of a strict BST with distinct keys. Is the result a standard BST? What traversal retrieves increasing order afterward?

#### Solution

The mirror has every original smaller subtree on the right and larger subtree on the left, so it is a reverse BST under the original comparator. Ordinary inorder now produces decreasing order. Reverse inorder, visiting right, root, left, restores increasing output. A singleton is both standard and reverse because it has no inequalities between different nodes; any nontrivial tree fails standard order after mirroring. The operation visits each actual node once, so it is linear, and a recursive implementation uses height-proportional workspace.

### 43. Two swapped keys

An otherwise correct distinct-key BST has inorder 1,7,3,4,5,6,2,8 after exactly two key fields were swapped. Locate the keys and show the repair. What if the swapped positions were adjacent?

#### Solution

The descents are 7 greater than 3 and 6 greater than 2. The first descent's left value and the last descent's right value are the misplaced keys, 7 and 2. Swapping them yields 1,2,3,4,5,6,7,8. If the swapped positions are adjacent, there is only one descent and its two values are swapped back. This diagnostic assumes exactly two distinct keys were exchanged; arbitrary corruption can create more descents or imitate this pattern without satisfying the promise. Values associated with keys must be moved consistently when repairing a dictionary.

### 44. Exact comparator versus language-expression counts

Search for 65 in Question 3's tree with code that tests equality, then less-than if unequal. Count three-way comparator calls in the mathematical model and primitive Boolean comparisons in that code.

#### Solution

The path is 40,70,60,65. The comparator model uses four calls, each giving less, equal or greater. The language code performs equality and less-than at the first three nodes, then equality only at 65, for seven primitive comparisons. A different branch ordering or comparator API gives a different primitive count. The path bound is still linear in the number of visited nodes when each comparison has constant cost. For long strings, comparator work can itself depend on common-prefix lengths, which should be multiplied or summed rather than ignored.

### 45. Integer-sentinel validation bug

An integer BST validator starts with exclusive lower bound INT_MIN and exclusive upper bound INT_MAX. Give valid trees it rejects and a correct representation of the initial interval.

#### Solution

A singleton containing either INT_MIN or INT_MAX is a valid strict BST, yet one of the exclusive sentinel tests fails. No legal integer can serve as an exclusive bound beyond the entire integer domain. Use an absent-bound flag, an optional bound, or a wider type only if it can genuinely represent values beyond all legal keys. The root interval is mathematically unbounded; the implementation must encode that fact. Replacing strict comparisons by nonstrict ones to admit endpoints introduces another error by admitting duplicate keys under a unique-node policy.

### 46. Comparator overflow

A signed 32-bit comparator returns the sign of $a-b$. Analyze inputs $a=2^{31}-1$ and $b=-1$, and replace this implementation safely.

#### Solution

The mathematical difference is $2^{31}$, beyond the signed 32-bit positive maximum. In a wrapping implementation its sign can become negative; in a language with undefined signed overflow the program is not even defined. Either outcome fails the ordering contract. Compute `(a > b) - (a < b)` instead; both relational tests are legal and the result lies in -1,0,1. Widening before subtraction also works only if the widened type is guaranteed to contain the entire difference range. A wrong comparator can cause search to discard the subtree containing the actual key.

### 47. Root field and caller-visible mutation

Why does `put(root,k,v)` without assigning its returned pointer sometimes appear to work on a nonempty tree but fail on an empty one? Give a caller-visible correction.

#### Solution

On a nonempty tree, a helper can mutate existing nodes reached through the copied root pointer, so some insertions appear to succeed even if the return value is ignored. With an empty root, it allocates a new node but only its local pointer changes; the caller still stores null. Deleting a one-child root has the same caller-link issue. Always assign `root = put(root,k,v)` and `root = erase(root,k)`, or explicitly pass a mutable reference to the root field. Mutation of a referenced object and mutation of the variable holding its address are different operations.

### 48. Height recursion with one missing child

Diagnose a height function that returns zero when both children are null and otherwise calls height on both children without a null base case. Give the smallest nonempty counterexample and the corrected recurrence.

#### Solution

A root with just one child reaches the nonleaf branch and calls height on its null missing child, which is then dereferenced. An empty initial tree fails immediately too. Set height(null) to minus one, then return one plus the maximum child height for every nonnull node. This yields zero on leaves without a special leaf condition and correctly handles one-child nodes. A full traversal computes heights in linear time; returning a cached root height is constant only when every update maintains those cached fields.

### 49. Iterator aggregate cost

A parent-pointer inorder iterator scans a chain of 100 keys from its minimum through exhaustion. Can a next operation cost 99 upward edges? Can the whole scan cost quadratic time?

#### Solution

In a right chain, the last key's next operation climbs 99 edges to reach the root and then null. Earlier steps move to the immediate right child. Each edge is traversed at most once downward and once upward during a continuous full scan, so total work is linear, not quadratic. In a left chain, finding the initial minimum descends the whole chain, then successive ancestors are reached one edge at a time. Resetting to the root for every successor query is another algorithm and can repeat routes; the aggregate bound assumes iterator state or parent links are retained.

### 50. Search-path inequalities

Could the visited-key sequence 50,20,40,30,35 occur when searching for 34 in a strict BST? Give the successive allowed intervals and final decision.

#### Solution

Yes. Starting unbounded, query 34 goes left at 50, right at 20, left at 40, then right at 30. The node intervals are successively unrestricted, below 50, $(20,50)$, $(20,40)$ and $(30,40)$. Key 35 lies inside the final interval and sends the query left. A null left link would certify absence after five comparisons. Every turn preserves all prior lower and upper bounds. The visited sequence is not monotone, so monotonicity of consecutive visited values is not a correct search-path criterion.

### 51. Impossible search-path sequence

Could 50,20,40,10 be the visited-key sequence when searching for 34? Prove your conclusion using bounds.

#### Solution

After visiting 20, the query is greater than 20, so every subsequently visited node must be in 20's right subtree and have key above 20. After visiting 40, the search goes left but retains the lower bound 20, so the next node must lie in $(20,40)$. Key 10 violates that inherited interval. No strict BST can realize the claimed path under a correct search, even though 10 is less than its immediate predecessor 40. This is the same ancestor-bound issue as global validation, applied to a query trace.

### 52. Scheduling conflicts require only adjacent stored times

Existing reservation times are 10,20,35,50. A new time is allowed only if its distance from every existing time is at least 8. Decide queries 27,28,43,58 and prove the nearest-neighbor criterion.

#### Solution

The predecessor and successor of 27 are 20,35; distances 7 and 8 reject it. For 28 the distances are 8 and 7, also rejecting it. For 43 neighbors 35,50 give distances 8 and 7, rejecting it. For 58 only predecessor 50 exists and distance 8 permits it. Every earlier stored time is no closer than the predecessor, and every later stored time is no closer than the successor. Thus checking those two bounds is sufficient, with an inclusive distance threshold as stated. If the rule instead forbade distance equal to 8, the final decision would change.

### 53. Two simultaneous orderings

Entries have unique identifier keys and independent mutable priorities. Explain why one plain BST ordered by identifier cannot find maximum priority in path time. Design augmentation that supports it and identifier-rank median.

#### Solution

Priority values need not follow identifier order, so descending the right spine finds the maximum identifier, not maximum priority. Store subtree size and a subtree argmax-priority entry at each node; the argmax is chosen from the node and its two child aggregates with a declared tie rule. The root aggregate gives maximum priority in constant time, while rank/select use size along a path. A priority update finds the identifier and refreshes aggregates back to the root. Balance is still needed for logarithmic worst-case update routes; a plain chain can require linear time despite correct augmentation.

### 54. Safe postorder release

A node has two child allocations. Why is `delete v; free(v.left); free(v.right)` invalid? Give a safe alternative and state which external reference must be cleared.

#### Solution

Deleting v releases the allocation containing its child fields, so reading v.left or v.right afterward dereferences freed memory. Recursively release both children while v is still alive, then delete v and clear the caller's owning pointer. Alternatively save both child pointers before deletion, but the ownership model must ensure that deleting v does not already destroy them. Clearing a local copied pointer alone leaves the caller's root dangling; use returned null or a reference to its pointer field. Postorder specifies when storage is released, not just when a key is printed.
