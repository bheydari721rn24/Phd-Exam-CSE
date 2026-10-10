### 1. A locally correct but globally invalid tree

Root 20 has left child 10 and right child 30. Node 10 has right child 25. Every other link is null. Decide whether this is a strict BST, give a failed search witness, and repair it without changing the keys.

#### Solution

The 10-to-25 edge is locally ordered, but every node below root 20's left link must be below 20. The key 25 violates that ancestor bound. Searching for 25 compares with 20 and 30, then reaches null at 30's left link, despite the stored occurrence. Move the node 25 from 10.right to 30.left. Its new allowed interval is $(20,30)$, so every bound holds. The repaired inorder is 10,20,25,30. A child-only validator would miss the original failure; interval validation rejects 25 in $(10,20)$.

### 2. Sharp height bounds for a nonpower size

For a strict BST with 1000 distinct keys, find the sharp minimum and maximum edge heights, the number of null links, and the largest possible successful-search comparison count.

#### Solution

The capacity of height $h$ is $2^{h+1}-1$. Since 511 is too small and 1023 is sufficient, the minimum height is 9, attained by direct midpoint construction. A chain attains height 999. There are exactly 1001 null links because $2n-(n-1)=n+1$. The deepest stored key in the chain needs 1000 three-way comparisons. A failed query can also compare with all 1000 stored keys before the final null test. The capacity argument bounds height from below; it does not say every 1000-node tree has height 9.

### 3. Complete insertion trace and exact cost

Insert 40,20,70,10,30,60,80,25,65 into an empty unique-key BST. Give all three depth-first traversals, the height, and the exact total number of insertion comparisons.

#### Solution

The root is 40, with children 20 and 70. Node 20 has 10 and 30; 30 has left child 25. Node 70 has 60 and 80; 60 has right child 65. Preorder is 40,20,10,30,25,70,60,65,80. Inorder is 10,20,25,30,40,60,65,70,80. Postorder is 10,25,30,20,65,60,80,70,40. Final depths in insertion order are 0,1,1,2,2,2,2,3,3, so insertion comparisons sum to 16 and height is 3. Each absent insertion compares with its existing ancestors; it does not compare with its newly allocated node.

### 4. Failed search and bracketing

In the tree of Question 3, search for 27. Give the comparison path, null-gap depth, floor, ceiling, strict rank and inclusive rank.

#### Solution

The visited keys are 40,20,30,25, after which the search takes 25.right to null. Four actual comparator calls are made and the terminal gap has depth 4. The largest encountered key below 27 is 25 and the smallest above is 30, so floor and ceiling are 25 and 30. Exactly 10,20,25 are smaller: strict rank is 3. Since 27 is absent, inclusive rank is also 3. Reusing the insertion position as a one-based rank would incorrectly give 4.

### 5. Repeated key versus repeated node

Insert the pairs (8,A),(4,B),(12,C),(8,D),(4,E) under replacement-value semantics. Give size, inorder associations and the total comparisons. Contrast counted-occurrence semantics.

#### Solution

The first pair creates the root without a key comparison. The next two each compare once with 8. Replacing 8 compares once; replacing 4 compares with 8 then 4, using two. Total comparisons are 5. Distinct-node size is 3 and inorder associations are (4,E),(8,D),(12,C). Under counted-node multiset semantics, the same shape has multiplicities 2,2,1 and mass 5; values require a separate policy, such as one shared value or a collection per key. Adding a new equal-key node would be a third design and would not obey the strict unique-node invariant.

### 6. Minimum with a nonnull right child

A subtree rooted at 30 has left child 20; node 20 has no left child and has right child 25. Explain delete-min and determine the surviving subtree.

#### Solution

The minimum is 20 because its left link is null. Its right child 25 is not a contradiction: only smaller descendants are excluded. Delete-min returns 20.right, so 30.left becomes 25. The resulting subtree has root 30 and left child 25, with size 2. Setting 30.left to null would lose a valid surviving key. If parent links are maintained, 25.parent becomes 30 before the allocation for 20 is released.

### 7. A successor that requires climbing

Use Question 3's tree. Find successors of 25,30,65,80 with parent pointers, specifying each upward or downward route.

#### Solution

Node 25 has no right child and is the left child of 30, so its successor is 30. Node 30 has no right child; climb to 20 from its right child, then to 40 from its left child, yielding 40. Node 65 similarly climbs from 60's right side to 70's left side, yielding 70. Node 80 climbs from 70's right side and then 40's right side to null, so no successor exists. Stopping at any ancestor with a nonempty right subtree would incorrectly return 20 for the 30 query.

### 8. Two-child deletion with a deep successor

Start with Question 3's tree and delete 40 using successor association copying. Give the successor, the final links, preorder, size and height.

#### Solution

The successor is the minimum of the right subtree, namely 60. It has a surviving right child 65. Copy (60,value-of-60) to the root object, then remove the old node 60 by setting 70.left to 65. The root's left subtree stays rooted at 20; its right subtree stays rooted at 70. Preorder becomes 60,20,10,30,25,70,65,80. There are 8 nodes, height 3, and inorder is the original sorted list with only 40 removed. Copying the key without its value would preserve order but corrupt the dictionary association. Discarding 65 would remove an unintended second key.

### 9. Immediate-right successor and a self-cycle trap

Insert 40,20,60,70, then delete root 40 by physically transplanting its successor. Give correct final links and explain why blindly assigning successor.right to the old right root can create a cycle.

#### Solution

The successor is the immediate right child 60. The new root is that existing node, with left child 20 and its original right child 70. Its parent becomes null, and 20.parent becomes 60. The old root object 40 is removed. The old right root is already 60; assigning 60.right to that pointer would set 60.right to itself. A deep-successor transplant first extracts a different node and can reconnect the remaining right root, but the immediate-child case must retain the successor's existing right link. Association-copy deletion avoids this identity change while still deleting the correct key.

### 10. Successor versus predecessor deletion

In Question 3's tree, delete 40 using predecessor replacement instead. Compare the resulting inorder and preorder with Question 8.

#### Solution

The predecessor is the maximum of the left subtree, 30. It has left child 25 and no right child. Copy its association to the root and replace 20.right by 25. Preorder is 30,20,10,25,70,60,65,80. Inorder remains 10,20,25,30,60,65,70,80, identical to the successor-deletion result's inorder. The shapes and identities differ, but both remove exactly 40 and preserve the map on other keys. An exam that prescribes successor replacement must use that convention when asking for an exact final shape.

### 11. Root replacement and absent deletion

Insert 9,5,3. Delete 9, then delete 8, then delete 3, then delete 5. Give the root after each operation and identify every size change.

#### Solution

The initial tree is a left chain of size 3. Deleting 9 returns its child 5 as the new root, size 2; parent 5 must become null. Deleting absent 8 follows 5.right to null and changes neither root nor size. Deleting leaf 3 sets 5.left to null, size 1. Deleting the remaining root returns null, size 0. The header object may remain allocated throughout; its root field changes. A helper whose returned root is ignored fails at the first and final operations.

### 12. Traversal accounting and workspace

A perfect tree has edge height 6. How many actual-node visits and recursive calls occur in a full binary inorder traversal that calls both children even when null? Compare recursive and breadth-first auxiliary storage.

#### Solution

There are $2^7-1=127$ actual nodes and 128 null positions. Actual processing occurs 127 times, while all recursive calls total $127+128=255$. The maximum chain of actual active recursive calls is 7; a null call can add one further frame depending on implementation. Breadth-first traversal has a level of 64 nodes and therefore linear-width queue storage. The output array, if retained, contains 127 keys under either method. Neither a logarithmic height nor a constant action per visit makes the complete traversal logarithmic in time.

### 13. Iterative inorder states

For insertions 8,4,12,2,6,10,14, list the stack just before each of the first four inorder emissions. Explain the amortized scan bound.

#### Solution

Writing the stack from bottom to top, before emitting 2 it is [8,4,2]. After removing 2, before emitting 4 it is [8,4]. Then descend into 4's right subtree, giving [8,6] before emitting 6. Before emitting 8 it is [8]. Each actual node enters and leaves the stack exactly once, so all seven emissions use linear aggregate work. One emission may include a long left descent; constant amortized cost is a statement about the full sequence, not every individual step. The maximum retained stack here has three actual nodes.

### 14. BST preorder reconstruction

Reconstruct a strict BST from preorder 50,30,20,40,35,80,70,90. Give postorder and explain the bounds assigned to 35.

#### Solution

Root 50 splits keys below and above 50. Its left root is 30, with left child 20 and right root 40; 40 has left child 35. Its right root is 80 with children 70 and 90. Postorder is 20,35,40,30,70,90,80,50. The key 35 inherits $(30,50)$ on entering 30's right subtree and then $(30,40)$ on entering 40's left subtree. Keeping only the immediate upper bound would discard the necessary lower bound. All eight tokens are consumed, so the parser certifies the supplied preorder as well as constructing its tree.

### 15. Invalid preorder despite plausible adjacent comparisons

Determine whether 20,10,5,30,15 can be the preorder of a strict BST. Identify the first unconsumed key in an interval parser and prove impossibility.

#### Solution

The parser builds root 20 and its left subtree rooted at 10 with left child 5. The next token 30 ends all left-subtree slots and starts root 20's right subtree. Key 15 is then outside that subtree's lower bound 20; it fits no remaining slot and is unconsumed. Any preorder visits the whole left subtree before the right subtree. Once 30, greater than 20, appears in the right block, the smaller key 15 cannot return to the left block. Repeated insertion of these numbers still creates a valid BST, but its preorder is different; insertion success is not preorder validity.

### 16. Arbitrary-tree reconstruction and an ambiguity witness

Given inorder 1,2,3,4,5 and preorder 3,2,1,5,4, find the tree. Would the preorder alone determine an arbitrary binary tree? Would it determine a strict BST?

#### Solution

Root 3 splits inorder into [1,2] and [4,5]. The left preorder block [2,1] makes root 2 with left child 1; the right block [5,4] makes root 5 with left child 4. The supplied preorder alone does not identify an arbitrary tree: even the smaller example [3,2] permits 2 as either child. Under strict BST order, side placement is fixed by comparisons, and the supplied five-key preorder uniquely gives the reconstructed tree. Distinct keys are essential; repeated labels without identities can make a traversal pair ambiguous.

### 17. Level order versus an insertion sequence

Could 20,10,30,25,5 be the level-order traversal of a strict BST? Contrast this claim with using the same list as an ordinary insertion order.

#### Solution

After root 20 and its two children 10,30, depth-two nodes belonging to 10 must precede those belonging to 30. Key 25 belongs below 30 while key 5 belongs below 10, so the claimed level order is invalid. The interval-slot queue skips 10's slots to place 25 under 30; once those earlier slots are skipped, 5 cannot occupy them. Ordinary insertion nevertheless creates a valid tree with 5 as 10.left and 25 as 30.left. Its actual level order is 20,10,30,5,25. Reconstructing by insertion without comparing the resulting traversal would fail to validate the assertion.

### 18. Strict rank, inclusive rank and zero-based select

Use Question 3's tree. Calculate strict rank of 30, strict rank of 31, inclusive rank of 30, and select at ranks 0,3,8. State the subtree quantities used when selecting rank 6.

#### Solution

The sorted list is 10,20,25,30,40,60,65,70,80. Therefore strict rank of 30 is 3; strict rank of absent 31 is 4; inclusive rank of 30 is 4. Select(0), select(3) and select(8) return 10,30,80. For rank 6, root 40 has left size 4, so descend right with residual $6-4-1=1$. At 70 the left size is 2, so descend left without changing that residual. At 60 its left size is 0, so descend right with residual 0 and return 65. Counts identify complete rank blocks; no inorder scan is needed.

### 19. Inclusive range counts with absent endpoints

For Question 3's keys, find counts in [25,70], [26,69], [5,9], [80,80] and [90,10]. Derive each using strict rank rather than enumeration alone.

#### Solution

For [25,70], ranks are 2 and 7 and 70 is present, giving $7-2+1=6$. For [26,69], strict ranks are 3 and 7 and 69 is absent, giving 4. For [5,9], both ranks are zero, giving zero. For [80,80], ranks cancel but membership contributes one. The reversed interval [90,10] is explicitly empty under our interface; do not evaluate the normal formula and report a negative count. The membership correction belongs only to the inclusive upper endpoint because subtracting strict rank already retains the lower endpoint when it is present.

### 20. A sorted tree with invalid augmentation

A root 8 has leaf children 4 and 12. Its stored size is 3, but the left leaf's stored size is incorrectly 2. Explain the result of select(1), and why checking only the root's stored size against the number of nodes is insufficient.

#### Solution

Select sees left size 2 and descends left with residual rank 1. At leaf 4, left size is zero, so it descends right with residual 0 and reaches null instead of returning 8. Inorder remains 4,8,12, so sortedness cannot detect the metadata error. The root's size happens to equal the real total 3, but its local equation $3=1+2+1$ is false. A complete augmentation validator checks every node's equation and the null size zero. It must also reject the left leaf's claim that it contains two nodes.

### 21. Weighted prefix sums

Keys 2,5,9,12 carry weights 7,-3,10,4. Build any correctly augmented BST. Find the sum for [5,12], the strict prefix sum at 9, and the effect of changing key 5's weight to 8.

#### Solution

The strict prefix at 9 includes keys 2 and 5 and equals 4. The strict prefix at 12 is 14; at 5 it is 7. The inclusive range sum is $14-7+4=11$. Updating key 5 changes its weight by 11, so every subtree sum whose subtree contains that node increases by 11, while all other subtree sums remain unchanged. The interval [5,12] then sums to 22. Negative weights do not invalidate subtraction; the BST is ordered by keys, not by subtree sums. A rank structure using size alone cannot answer these sum queries without another scan.

### 22. Counted multiset rank blocks

Store keys 3,8,11 with counts 2,3,1 in a counted-node BST. Find mass, strict occurrence rank of 8, inclusive occurrence rank of 8, select at ranks 1,2,4,5, and the median occurrences.

#### Solution

The expanded sorted sequence is 3,3,8,8,8,11, so mass is 6. Strict occurrence rank of 8 is 2 and inclusive rank is $2+3=5$. Select gives 3,8,8,11 at ranks 1,2,4,5. Both central ranks 2 and 3 return 8, so either lower or upper median convention gives 8. A unique-key dictionary would have size 3 and strict distinct-key rank of 8 equal to 1; substituting that size into the occurrence formula loses multiplicity. Every stored node's count must stay positive.

### 23. Count transfer in two-child multiset deletion

Root key 8 has count 1, left key 3 has count 2, and right key 11 has count 4. Delete one occurrence of 8 using successor replacement. Determine the correct count transfers and show the error in deleting only one successor occurrence.

#### Solution

Removing 8 is structural because its count is one. Transfer successor key 11 and its full count 4 to the root, then remove the old node 11 completely. The left key 3 keeps count 2. New mass is 6, exactly original mass 7 minus one. If only one occurrence is removed from the old successor node, the root retains count 4 while another node 11 retains count 3: strict node order is broken and mass becomes 9 rather than 6. Association transfer and occurrence deletion must be distinguished. A helper that removes a whole successor node is needed in this case.

### 24. Exact path-length averages

Compute internal path length, external path length and uniform successful and uniform-gap unsuccessful comparator averages for Question 3's tree.

#### Solution

The actual depths sum to $I=16$ and $n=9$. Therefore $E=I+2n=34$. Successful search costs depth plus one, so its uniform mean is $(16+9)/9=25/9$. There are ten null gaps, making the uniform-gap failed-search mean $34/10=17/5$. These conditional means differ because unsuccessful searches run to null while successful searches stop at the matching actual key. They cannot be combined into one unconditional average without the probability of success and the within-family query distributions.

### 25. Nonuniform gap probabilities

For root 10 with right child 20, successful key probabilities are 0.1 and 0.2. The three null-gap probabilities, from smallest to largest, are 0.4,0.2,0.1. Find the unconditional comparison expectation and the conditional successful mean.

#### Solution

The successful costs are 1 and 2. The left root gap has depth 1; the two gaps below 20 have depth 2. The total probabilities sum to one. The unconditional expectation is $0.1\cdot1+0.2\cdot2+0.4\cdot1+0.2\cdot2+0.1\cdot2=1.5$. Success probability is 0.3, and its conditional expectation is $(0.1+0.4)/0.3=5/3$. Uniform-gap averaging would give $5/3$ for the failed family, but its actual conditional average is $1.0/0.7=10/7$. The shape alone does not determine a query-weighted expectation.

### 26. Perfect-tree depth sums

Derive internal path length and uniform successful cost for a perfect tree of edge height $h$, then evaluate at $h=3$.

#### Solution

At depth $j$ there are $2^j$ nodes, so $I=\sum_{j=0}^h j2^j=(h-1)2^{h+1}+2$. The finite-sum identity follows by subtracting twice the sum shifted one index, or by differentiating the finite geometric polynomial. With $n=2^{h+1}-1$, the successful mean is $((h-1)2^{h+1}+2+n)/n$. At height 3, $n=15$, $I=34$, and the mean is $49/15$. Every null gap is at depth 4, so the failed mean is exactly 4 and $E=64=34+30$ verifies the external identity.

### 27. A chain is expensive on average too

For a chain of $n$ distinct keys, derive internal path length and uniform successful and uniform-gap unsuccessful means. Evaluate at $n=5$.

#### Solution

Actual depths are 0 through $n-1$, regardless of the left/right direction pattern, so $I=n(n-1)/2$. Successful mean is $(I+n)/n=(n+1)/2$. External mean is $(I+2n)/(n+1)=n(n+3)/(2(n+1))$. For five keys these are 3 and $10/3$, with $I=10$ and $E=20$. A chain does not become logarithmic merely because queries are uniformly spread over its stored keys. Random queries on a fixed worst-case tree and random insertion order are different probability models.
