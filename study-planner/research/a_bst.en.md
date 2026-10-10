# Binary Search Trees: Correctness, Ordered Queries, and Exact Costs

## Written courses and how to use this chapter

This chapter combines genuinely reviewed written materials from CMU 15-122, Princeton COS226, Berkeley CS61B and MIT 6.006, with Stanford CS106B as an additional implementation reference. The [source audit](../reviews/a_bst-sources.html) identifies authors, reading scopes, selection decisions and disagreements. The derivations and worked examples here are original. In particular, a familiar algorithm is not accepted merely because several courses present it: its hypotheses, result and boundary cases are established below.

Read the full lesson before attempting its question bank. The last sections contain a complete summary and a separate bank of reasoning rules. The interactive models are explanatory tools: each starts paused, and each checkpoint states the operation, its reason and the invariant being preserved. Visual tokens identify key associations, not allocation identities. During geometric replay the arrows follow the displayed token positions; structural rewiring belongs to the exact target checkpoint, and intermediate movement does not claim an additional valid BST state. Use Before and Compare to inspect the precise previous and target trees. AVL and red-black repair, heaps, hashing and amortized trees belong to subsequent chapters; the present chapter establishes the machinery those subjects depend on.

## 1. Ordered dictionaries and representation assumptions

A dictionary associates a key with a value. A set stores only membership. An ordered dictionary additionally supports queries about the order: the smallest key, nearest key below a query, the number of smaller keys, and all keys in an interval. A binary search tree is one possible implementation, not the definition of that abstract interface.

We assume a finite rooted binary tree. Each actual node owns at most one left child and at most one right child, the two subtrees are disjoint, and no child pointer creates a cycle. A null child represents an empty subtree. Shared children or cycles invalidate the ordinary structural induction even if some individual comparisons look correct. Parent pointers are optional; if present, the root's parent is null and each child points back to its actual parent.

Keys belong to a stable total order. The comparator must be consistent, transitive and antisymmetric in sign, and equality must identify the dictionary's key equivalence classes. Changing a stored key in place can destroy order without changing a single pointer. A comparator that subtracts bounded integers can overflow; compare relationally instead. NaN-like incomparable values require a declared ordering policy before they can be ordinary ordered keys.

Our default dictionary contains one node per distinct key. Inserting an existing key replaces its value and leaves its position unchanged. A successful lookup returns an entry, not merely a value whose nullness might also mean absence. This distinction matters when null is itself a legal stored value. Later we extend the dictionary to a multiset using positive counts in the existing nodes.

## 2. Depth, height, size and null gaps

The depth of the root is zero and increases by one on each child edge. A node's height is the largest number of edges from that node to a descendant. Define the empty-tree height to be minus one, making the recursive equations uniform:

$$s(\varnothing)=0,\qquad s(v)=1+s(v.left)+s(v.right).$$

$$h(\varnothing)=-1,\qquad h(v)=1+\max(h(v.left),h(v.right)).$$

A leaf therefore has height zero. Some courses use the number of vertices on a path, so their nonempty height is ours plus one. Whenever an operation follows a single path, write its bound as $O(h+1)$ with our convention; writing $O(h)$ for a singleton or empty tree can conceal the boundary.

For a nonempty tree with $n$ nodes, at depth $j$ there are at most $2^j$ nodes. Thus $n\le 2^{h+1}-1$, giving the sharp minimum height $\lceil\log_2(n+1)\rceil-1$. A chain has height $n-1$, the sharp maximum. Having a full root or a roughly symmetric drawing does not establish a height bound for every subtree.

Every actual node has two child positions, so there are $2n$ positions and $n-1$ nonnull child edges. Exactly $n+1$ positions are null. Their external depths are one more than their actual parents' depths. These are search gaps, including the interval before the minimum and after the maximum. They are not additional stored keys.

<!-- SIM: structure -->

## 3. The global ordering invariant

For every node $v$, every key in its left subtree is strictly less than $v.key$, and every key in its right subtree is strictly greater. This quantifies over entire subtrees, not just immediate children. For example, root 20, left child 10 and that child's right child 25 satisfy both parent-child comparisons, yet 25 violates the root's left-subtree bound. Searching for 25 goes right from 20 and misses it.

Equivalently, each recursive subtree carries an open allowed interval $(lo,hi)$. Its root must lie inside that interval. The left subtree receives $(lo,v.key)$; the right receives $(v.key,hi)$. Ancestor bounds persist when descending. An absent bound is represented explicitly, not by the smallest or largest legal integer: either of those integers may be an actual key.

**Interval proof.** At the root no finite bounds are required. If every descendant satisfies its inherited interval, the left descendants are below their ancestor's key and the right descendants are above it, proving global order. Conversely, global order imposes each ancestor inequality, so every node lies in the intersection of those inequalities, exactly its inherited interval. This equivalence assumes the representation is a finite tree; the ordering check alone need not diagnose every memory-ownership error.

```python
def valid(v, lo=None, hi=None):
    if v is None:
        return True
    if lo is not None and not lo < v.key:
        return False
    if hi is not None and not v.key < hi:
        return False
    return valid(v.left, lo, v.key) and valid(v.right, v.key, hi)
```

This integer-key example uses None only for absent bounds. A generic comparator version substitutes comparator signs. Checking each node once takes $\Theta(n)$ time in the worst case and $O(h+1)$ recursive workspace. Recomputing the minimum and maximum of every subtree instead can take quadratic time on a chain.

<!-- SIM: bounds -->

## 4. Search: exclusion, termination and completeness

At a node of key $k$, compare query $q$ with $k$. Equality returns the entry. If $q<k$, neither the node nor its right subtree can contain $q$; descend left. If $q>k$, descend right symmetrically. A null subtree proves absence.

The loop invariant has two parts: every still-possible occurrence is in the current subtree, and every discarded node or subtree has been excluded by a justified comparison. Initially the current subtree is the whole tree. Each unequal comparison preserves the possible occurrence in the chosen child. A finite descent terminates because depth increases and the tree is finite. Equality gives a genuine match; reaching null means the complete remaining candidate set is empty. This proves both directions of correctness: return a node if and only if its key is present.

```python
def find(root, q):
    v = root
    while v is not None:
        if q == v.key:
            return v
        v = v.left if q < v.key else v.right
    return None
```

Our mathematical cost model counts one three-way comparator call per actual visited node. The illustrative Python expression may implement equality and less-than separately; primitive language comparisons are a different count. A found key at depth $d$ uses $d+1$ comparator calls. A failed query terminating at a null gap of depth $g$ uses $g$ calls: the final null test is not a comparison with a key. Iterative search uses constant auxiliary workspace.

<!-- SIM: search -->

## 5. Insertion and the returned-subtree contract

Absent-key insertion follows its failed-search path and replaces the terminal null link by a fresh node. The legal interval at that null link proves the new key is below every upper bound and above every lower bound. Existing-key insertion changes only the value. The distinction determines whether size increases.

In recursive code the helper returns the root of the updated subtree. Every caller must reconnect that returned root, including the outermost dictionary root. This is not optional bookkeeping: inserting into an empty tree changes its root from null to an actual node.

```python
def size(v):
    return 0 if v is None else v.size

def refresh(v):
    v.size = 1 + size(v.left) + size(v.right)
    return v

def put(v, key, value):
    if v is None:
        return Node(key, value)  # left/right=None, size=1
    if key < v.key:
        v.left = put(v.left, key, value)
    elif v.key < key:
        v.right = put(v.right, key, value)
    else:
        v.value = value
    return refresh(v)

root = put(root, key, value)
```

**Inductive contract.** Given an ordered subtree whose keys lie in $(lo,hi)$ and a new key inside that interval, put returns an ordered subtree in the same interval with exactly the old key set union the inserted key. Existing other associations remain unchanged; the target association equals the new value. The empty case is immediate. In an unequal case, the inserted key lies inside the chosen child's narrower interval, allowing the induction hypothesis. The untouched subtree retains its bounds. Refresh restores the size equation. In the equal case the key set and all order relations remain unchanged.

An absent key whose final node depth is $d$ requires $d$ comparisons with existing keys. Sorted insertion of $n$ distinct keys requires $0+1+\cdots+(n-1)=n(n-1)/2$ comparisons. Replacing an existing root value takes one comparison; an insertion upper bound alone must not imply that every insertion traverses the full height.

<!-- SIM: insert -->

## 6. Extrema, floor and ceiling

The minimum is the first actual node on the left spine with a null left child. It can have a right child. Any other node either lies to its right along that spine or in a right subtree, so its key is larger. The maximum follows the right spine. On an empty tree return explicit absence rather than a legal key used as a sentinel.

The floor of $q$ is the largest stored key at most $q$; the ceiling is the smallest stored key at least $q$. During a floor search, if $v.key>q$ descend left without changing the current candidate. If $v.key<q$, this key is a better floor candidate and descend right; the left subtree is smaller than this candidate. Equality finishes immediately. At null return the last candidate. Ceiling is symmetric.

The candidate invariant is that the floor is either the retained candidate or in the current subtree, and all previously discarded feasible keys are at most the candidate. This proves a missing query's neighbors occur on its search path. Strict predecessor and successor of a stored key exclude the key itself; floor and ceiling do not.

<!-- SIM: neighbors -->

## 7. Successor and predecessor with parent links

If a node $x$ has a right subtree, its successor is that subtree's minimum. If it has no right subtree, climb parent links while the current node is a right child. The first ancestor reached from its left child is the successor. If no such ancestor exists, $x$ is the maximum and has no successor.

Why must the stopping rule mention the side? Every ancestor reached from a right child has smaller key than $x$, so it cannot be its successor even when it has a nonempty right subtree. An ancestor reached from the left is larger; the first such ancestor is the smallest larger key because every node between it and $x$ lies below it in its left subtree. The predecessor is the mirror statement. Neither operation is generally “just the parent.”

A successor with a right child remains valid: only a minimum's left child must be null. Pointer identity also matters. A node reference lets the parent-link method begin immediately; searching for its key first adds another path, though the asymptotic bound stays $O(h+1)$.

<!-- SIM: successor -->

## 8. Deletion with zero or one child

First search for the target. If absent, preserve the tree. A leaf can be detached. A node with one child is replaced in its parent's link by that child, or the dictionary root becomes that child when deleting the root. Its whole subtree moves with it; reconnecting only the child's key loses descendants.

**Order proof.** The child's entire subtree previously satisfied every ancestor bound inherited by the deleted node. Removing the intermediate node cannot create a new violated comparison. The returned subtree still lies in the same allowed interval. In a parent-pointer implementation the replacement child's parent must be updated to the deleted node's former parent, including null at the root. Size fields are recomputed on the path back to the dictionary root.

Memory deletion is separate from mathematical deletion. Preserve required child pointers before releasing the old allocation, never dereference the released node afterward, and do not release descendants that remain in the tree. A recursive C++ call taking the root pointer by value cannot update its caller's link; use a returned root, a pointer-to-pointer or a reference to the pointer.

<!-- SIM: simple-delete -->

## 9. Two-child deletion and the successor's surviving child

Let the target have key $k$ and two children. Let $s$ be the minimum key of its right subtree. Then every left-subtree key is less than $k<s$, and every remaining right-subtree key is greater than $s$ under unique keys. Replacing the target association by $s$ and removing the old occurrence of $s$ therefore preserves strict order and removes exactly $k$.

The successor has no left child, but may have a right child. The latter replaces the successor at its old location. If the successor is the immediate right child, that replacement updates the target's right link; if deeper, it updates its former parent's left link. Both cases belong to the same returned-subtree algorithm.

```python
def erase_min(v):               # requires v is not None
    if v.left is None:
        return v.right
    v.left = erase_min(v.left)
    return refresh(v)

def erase(v, key):
    if v is None:
        return None
    if key < v.key:
        v.left = erase(v.left, key)
    elif v.key < key:
        v.right = erase(v.right, key)
    else:
        if v.left is None:
            return v.right
        if v.right is None:
            return v.left
        successor = v.right
        while successor.left is not None:
            successor = successor.left
        v.key, v.value = successor.key, successor.value
        v.right = erase_min(v.right)
    return refresh(v)
```

The code assumes managed memory and omits parent pointers. It is complete for unique-key dictionaries with correctly initialized size fields. The found target and right-subtree descent lie on one overall downward route, so search plus successor removal remains $O(h+1)$, not $O(h^2)$. The recursive stack uses $O(h+1)$.

Predecessor replacement is equally valid when used consistently. Deleting a specific node object by copying a successor's association leaves the target object alive and removes the successor object. Physically transplanting the successor can instead remove the target object; that variant must repair all parent links and both child links. Its immediate-right-child case requires care to avoid making the successor its own child. Order correctness does not by itself establish iterator or reference validity.

<!-- SIM: deep-delete -->
<!-- SIM: immediate-delete -->

## 10. Traversals and the sorted-order equivalence

Preorder visits root, left subtree, right subtree. Inorder visits left subtree, root, right subtree. Postorder visits left subtree, right subtree, root. Level order visits increasing depth from left to right, implemented with a queue. These definitions apply to arbitrary binary trees; only the BST invariant guarantees that inorder produces strictly increasing distinct keys.

**Inductive sortedness proof.** Each child's inorder is increasing by induction. Every left output is below the root and every right output is above it, so concatenation is increasing. Conversely, if the complete inorder of a finite binary tree with distinct keys is strictly increasing, each node follows every key of its left subtree and precedes every key of its right subtree. The required strict inequalities follow. Thus inorder can validate order, but it does not validate pointers, size fields or comparator stability.

Each actual node is visited once, giving $\Theta(n)$ time for a full traversal regardless of balance. A recursive traversal calls null subtrees too: exactly $2n+1$ calls occur if each nonnull call makes two child calls. Streaming inorder uses $O(h+1)$ stack; storing the complete output costs $\Theta(n)$ additional space. A breadth-first queue uses $O(w)$ space where $w$ is the maximum level width, potentially linear even when height is logarithmic.

```python
def inorder(root):
    stack, v = [], root
    while stack or v is not None:
        while v is not None:
            stack.append(v)
            v = v.left
        v = stack.pop()
        yield v.key
        v = v.right
```

The stack holds unfinished ancestors, not all stored nodes. Every node is pushed and popped once; a single next call can traverse a long spine, but an entire scan is linear. A postorder deallocator releases children before their parent. Releasing a parent first is possible only after saving safe child references and ensuring the ownership design permits it.

<!-- SIM: traversal -->

## 11. Reconstructing a tree from traversals

For arbitrary distinct-key binary trees, inorder plus preorder determines the tree: preorder's first key is the root, its inorder position splits the two key sets, and corresponding preorder blocks recursively determine the children. Inorder plus postorder works similarly with the last postorder key as root. Preorder alone does not determine an arbitrary binary tree: a root followed by one child does not identify the child's side.

For a strict BST, inorder is already known: it is the sorted key list. Therefore a valid distinct-key preorder alone determines the tree. A linear parser consumes the next key only when it lies inside the current interval, then recursively parses left and right. After parsing the root, all input must be consumed; an unconsumed key diagnoses an invalid preorder rather than an extra tree.

```python
def parse_preorder(a):
    i = 0
    def parse(lo, hi):
        nonlocal i
        if i == len(a):
            return None
        k = a[i]
        if (lo is not None and not lo < k) or (hi is not None and not k < hi):
            return None
        i += 1
        v = Node(k, None)
        v.left = parse(lo, k)
        v.right = parse(k, hi)
        return refresh(v)
    root = parse(None, None)
    if i != len(a):
        raise ValueError('Invalid strict BST preorder')
    return root
```

Each key is consumed once, and each of the linear number of empty child attempts costs constant time. Repeatedly scanning for split boundaries without index bookkeeping can instead become quadratic. Postorder can be parsed backward, processing root then right then left. A preorder such as 20,10,25,5 is invalid: after entering root 20's right subtree, 5 cannot legally return to its left subtree. Merely comparing each adjacent pair cannot detect the ancestor violation.

A valid BST level-order sequence also identifies a unique tree. To validate it in linear time, maintain a queue of available child slots carrying their allowed intervals. For each next key, discard preceding slots whose interval excludes it, fill the first fitting slot, and enqueue its left then right slots. Empty skipped slots remain empty. The queue respects breadth-first order; every slot is processed once, and every created node generates two slots. Ordinary repeated insertion reconstructs a valid supplied level order too, but can take quadratic time and is not by itself a validation of the claimed traversal order.

<!-- SIM: reconstruct -->

## 12. Rank and select through subtree augmentation

Define strict rank $r(q)$ to be the number of stored keys less than $q$, whether or not $q$ is present. Select uses zero-based rank: $select(j)$ is the key with exactly $j$ smaller keys, requiring $0\le j<n$. Store subtree size at each node and let $t=s(v.left)$.

If $q<v.key$, rank descends left. If equal, return $t$. If larger, all left keys and the root are smaller, so add $t+1$ and descend right. Select descends left when $j<t$, returns the root when $j=t$, and descends right with residual $j-t-1$ when $j>t$. The discarded rank block is a complete consecutive block, which proves the recursion by induction.

| Condition | Strict-rank result |
|---|---|
| The subtree is empty. | $r_v(q)=0$ |
| The query is smaller than the root key. | $r_v(q)=r_{v.left}(q)$ |
| The query equals the root key. | $r_v(q)=s(v.left)$ |
| The query is greater than the root key. | $r_v(q)=s(v.left)+1+r_{v.right}(q)$ |

Inclusive rank is $r(q)+\mathbf{1}_{q\in T}$. Mixing these definitions changes an exact count at every present endpoint. For unique keys, $r(select(j))=j$; for a present key $k$, $select(r(k))=k$. For an absent key, select at its insertion rank gives its ceiling only if that rank is below $n$.

Without stored sizes, recomputing size while descending can scan large subtrees and lose the path-time bound. With correct augmentation both queries cost $O(h+1)$. Refresh every changed ancestor after insertion and deletion. A rotation will need to refresh its lower node before its new upper node, because the upper size depends on the new lower size.

<!-- SIM: rank -->

## 13. Range reporting, counting and sum augmentation

For an inclusive interval $[a,b]$, reject a reversed interval or define its result explicitly as empty. At a node of key $k$, recurse left only if $a<k$, emit $k$ only if $a\le k\le b$, and recurse right only if $k<b$. An equality endpoint prevents descending toward keys strictly beyond it.

The visited nodes outside the answer lie on at most two boundary-search routes. Other visited actual nodes are output nodes, because their keys lie between the endpoints. Thus reporting $m$ matching keys costs $O(h+m+1)$, with $O(h+1)$ stack plus any saved output. The answer can be empty yet the boundary route still have linear length in a chain. “Output-sensitive” does not mean cost equals output alone.

Counting uses augmentation without emitting entries:

$$N[a,b]=r(b)-r(a)+\mathbf{1}_{b\in T}\qquad(a\le b).$$

If each key carries a numeric weight, store subtree sum $S(v)=S(v.left)+v.weight+S(v.right)$ alongside size. A strict prefix sum $P(q)$ adds complete left-subtree sums and root weights exactly when descending right. Then interval sum is $P(b)-P(a)+\mathbf{1}_{b\in T}weight(b)$. These operations also follow a path. Negative weights do not invalidate order or prefix subtraction, but arithmetic overflow or numerical rounding requires its own policy. A weight update preserves keys yet must refresh sums on the search path.

<!-- SIM: range -->

## 14. Counted multisets and duplicate policy

Represent each distinct key once with a positive multiplicity $c(v)$. Store mass $M(v)=M(v.left)+c(v)+M(v.right)$. Strict order remains on distinct node keys, while rank counts occurrences. When descending right add $M(v.left)+c(v)$; select returns the root for every residual index in the interval from $M(v.left)$ through $M(v.left)+c(v)-1$.

Inserting an equal key increments its count. Removing one occurrence decrements a count above one; structural deletion occurs only when the count becomes zero. In two-child structural deletion, copy the successor's complete key, value and count, then remove its old node completely, not merely one occurrence. Otherwise that key appears in two nodes or its total multiplicity changes incorrectly. Refresh mass throughout the route.

Storing duplicates in separate nodes is a different design. Always-left equal insertion with weak left and strict right bounds can create a chain of equal keys, and rotations may move an equal key to the disallowed side. Counted nodes preserve strict distinct-node order under later rotations and avoid that structural ambiguity. Exact formulas must specify whether $n$ is the number of distinct nodes or total occurrences.

<!-- SIM: multiplicity -->

## 15. Exact internal and external path lengths

Let $I(T)$ sum depths of actual nodes and $E(T)$ sum depths of null gaps. Every actual node, including a stored leaf, is internal in this extended-tree accounting. This terminology differs from calling only nonleaf actual nodes “internal.” For a tree with left and right node counts $l,r$,

$$I(T)=I(L)+I(R)+l+r.$$

$$E(T)=E(L)+E(R)+(l+1)+(r+1).$$

The empty tree has $I=E=0$ and one gap at depth zero. Subtracting the recurrences and applying induction yields $E=I+2n$. A singleton confirms it: $I=0$ and its two null gaps have depth one, so $E=2$.

If successful queries are uniform over the $n$ actual keys, average comparisons are $(I+n)/n$. If unsuccessful queries are uniform over the $n+1$ gaps, the average is $E/(n+1)$. Uniform gaps do not follow from uniform numeric queries when gaps have unequal lengths. For general successful probabilities $p_v$ and gap probabilities $q_g$, the unconditional comparator cost is $\sum_v p_v(d_v+1)+\sum_g q_g d_g$, with the probabilities jointly summing to one. Do not normalize each family independently unless asking conditional averages.

<!-- SIM: path-cost -->

## 16. How many insertion orders produce one fixed tree?

For distinct fixed sorted keys, a tree shape uniquely determines its labeling: assign keys in increasing inorder. To produce that labeled tree without rotations or deletion, every ancestor must be inserted before its descendants. This condition is also sufficient. Once a root appears first, left and right sequences never interfere with each other's comparisons, so any interleaving of valid child sequences works.

Let $W(T)$ count insertion permutations that produce $T$. With $n=1+l+r$,

$$W(T)=\binom{n-1}{l}W(L)W(R),\qquad W(\varnothing)=1.$$

The binomial chooses positions of the left sequence among the positions after the root. Expanding inductively gives the hook product $W(T)=n!/\prod_{v\in T}s(v)$. This is an exact integer. A perfect seven-node tree has counts 7 at the root, 3 at each internal child and 1 at each leaf, so $W=7!/(7\cdot3\cdot3)=80$.

Under a uniformly random insertion permutation its probability is $W(T)/n!=1/\prod_v s(v)$. Thus tree shapes are not uniform. For three keys, the balanced shape has two producing permutations, while each of the four chain shapes has one. Their probabilities are one third and one sixth respectively.

<!-- SIM: orders -->

## 17. Catalan shapes, chain probabilities and model distinctions

The number $C_n$ of ordered binary tree shapes with $n$ nodes satisfies $C_0=1$ and $C_n=\sum_{l=0}^{n-1}C_lC_{n-1-l}$: choose the left size and independently choose the children. Hence $C_n=\binom{2n}{n}/(n+1)$. BSTs on one fixed distinct key set have exactly these shapes, with unique inorder labeling. Counting all insertion permutations instead gives $n!$; multiple permutations can create the same shape.

A chain need not have all edges in the same direction. There are $2^{n-1}$ ordered chain shapes, and each requires exactly one insertion permutation: repeatedly insert an extreme of the remaining keys. The probability of any chain under uniform permutations is $2^{n-1}/n!$. Counting only increasing and decreasing orders misses mixed-direction chains. In contrast, a uniformly chosen shape has chain probability $2^{n-1}/C_n$. Neither formula implies a deterministic balance guarantee.

The distinction also affects “average height.” Uniform permutations create the random-BST model; uniform Catalan shapes are another model. We derive random-permutation depth next. Its exact depth result cannot be used as a proof of the maximum-depth result, and neither result applies automatically after a long Hibbard-deletion workload.

## 18. Expected depth under uniform distinct-key insertion

Number the sorted keys $1,\ldots,n$. A smaller key $j<i$ is an ancestor of rank $i$ exactly when $j$ is inserted before every key in the interval $j,\ldots,i$. If another interval key is inserted first, it separates $j$ from $i$; if $j$ is first, both remain in its right subtree until $i$ arrives. Under a uniform permutation every interval key is equally likely to be first, so this probability is $1/(i-j+1)$. For $j>i$ the analogous probability is $1/(j-i+1)$.

Summing ancestor indicators by linearity of expectation requires no independence between them. With $H_m=\sum_{k=1}^m1/k$,

$$\mathbb{E}[d_i]=H_i+H_{n+1-i}-2.$$

Summing over ranks and using $\sum_{i=1}^nH_i=(n+1)H_n-n$ gives

$$\mathbb{E}[I_n]=2(n+1)H_n-4n.$$

Consequently a uniformly selected successful key has expected comparator cost $2(n+1)H_n/n-3$. Conditional on a uniformly selected gap as well as a random permutation, the expected failed-search cost is $2H_n-2n/(n+1)$. Both are asymptotic to $2\ln n$; the logarithm here is natural. The fixed-rank formula distinguishes boundary and central ranks: the minimum has expected depth $H_n-1$, while central ranks are typically deeper.

The separate theorem that random-BST expected height is logarithmic concerns the maximum of correlated depths. Princeton's slides cite the sharper leading constant about 4.31107 times natural log. We do not derive that advanced probability theorem here or pretend the depth calculation proves it. Deterministic worst-case height remains $n-1$. Randomizing initial insertion also does not make subsequent adversarial queries or arbitrary update sequences independent random permutations.

## 19. Construction, tree sorting and iterator costs

Given sorted distinct keys in an array, recursively choose a midpoint as root and build its two halves. Directly assigning the resulting child pointers allocates each node once and costs $\Theta(n)$. Its height is the minimum $\lceil\log_2(n+1)\rceil-1$ because each split keeps child sizes within one. Inserting those midpoint-first keys through the ordinary dictionary interface can produce the same shape but uses $\Theta(n\log n)$ comparisons overall. Distinguish direct construction from repeated lookup-and-insert.

Tree sorting inserts each input into a BST and outputs inorder. Without balancing it takes quadratic worst-case time, even though the final traversal itself is linear. With uniform distinct insertion order its expected comparison count is the expected internal path length, $2(n+1)H_n-4n$, because a node's insertion path length equals its final depth. Keeping occurrences in counts emits each duplicate the declared number of times.

Calling a successor operation independently for each key gives the crude bound $O(n(h+1))$, but a continuous full parent-pointer scan is $O(n+h+1)$: each edge is traversed only a constant number of times. An isolated next step can still cost linear height. This is an aggregate statement about one scan, not proof that every step is worst-case constant. A stack iterator follows the same push-once/pop-once accounting.

## 20. Lowest common ancestors and range split points

For two present keys $a\le b$, descend from the root while both are less than the current key or both are greater. The first node whose key lies in $[a,b]$ is their lowest common ancestor. At that node the targets either split between children or one is the node itself. Earlier ancestors had both in the same child, proving that no earlier stopping point is lower. This costs $O(h+1)$.

If either key is absent, the same computation gives an interval split point, not necessarily an ancestor of two stored nodes. Validate membership when the requested interface promises an LCA of actual entries. A node's presence is a semantic precondition, not a consequence of the query values straddling a root.

## 21. Rotations as a boundary-preserving bridge

A left rotation at $x$ requires a right child $y$. Before it, $x$ has subtrees $A,B$ through $y$ and $y$ has right subtree $C$; their order is $A<x<B<y<C$. Move $y$ to the subtree root, set $x.right=B$, and set $y.left=x$. The inorder sequence is unchanged, proving preservation of strict BST order. Repair the old parent's link or the dictionary root, and every affected parent pointer. Recompute $x$'s fields before $y$'s fields.

A rotation uses constant pointer operations, but a single rotation is not a general balance strategy. It may decrease one subtree's height and increase another's. The next chapter proves AVL and red-black repair rules and their height guarantees. This chapter supplies the exact order and augmentation contracts those rules must preserve.

<!-- SIM: rotation -->

## 22. Threading, memory layout and implementation hazards

Morris inorder traversal uses temporary threads from a subtree's rightmost predecessor to its current ancestor. A first encounter installs the thread and descends left; a second encounter removes it and visits the ancestor before descending right. With a valid finite binary tree it has linear aggregate time and constant auxiliary memory, but it temporarily changes child links. It is inappropriate for a concurrent read-only traversal unless that mutation is coordinated, and early termination must clean every installed thread. A maintained parent pointer provides another constant-workspace scan without temporary threading.

Storage calculations need explicit assumptions. On an ABI with 4-byte integer keys, 8-byte aligned pointers, and field order key, left, right, there may be 4 padding bytes after the key, so a node occupies 24 rather than 20 bytes. A third pointer, a value, size metadata and allocator headers add space. Contiguous sorted arrays can have better locality even when update costs are worse. Asymptotic pointer counts do not measure cache performance or exact allocation bytes.

Common correctness failures have precise witnesses: a missing null base case crashes a one-child height recursion; an extreme-key absence sentinel collides with a real key; key-copy deletion without copying its value changes the map; deleting a successor's right subtree loses entries; stale subtree sizes make rank wrong even though inorder still looks sorted; an unassigned returned root makes empty insertion disappear. Each witness tests a different contract and deserves a separate diagnosis.

## 23. Complete summary

A strict BST is a finite owned tree with stable ordered keys and ancestor-wide inequalities. Search correctness rests on excluding entire impossible subtrees. Insertion preserves inherited intervals and must reconnect the returned subtree root. Deletion must remove exactly the target association while preserving every surviving descendant; a successor has no left child but may have a right child. Parent-link, augmentation and node-identity contracts are independent of sortedness and require their own repair.

Path operations cost $O(h+1)$, while a full traversal costs $\Theta(n)$. The sharp nonempty height interval is from $\lceil\log_2(n+1)\rceil-1$ through $n-1$. Stored subtree sizes enable strict rank and zero-based select along one path; count and sum queries must treat inclusive endpoints explicitly. A counted multiset stores total occurrence mass rather than distinct-node size.

Exact comparator costs distinguish stored-node depth plus one from null-gap depth. The external identity is $E=I+2n$. Uniform successful keys and uniform failed gaps are separate query distributions. A fixed tree has $n!/\prod_vs(v)$ producing insertion permutations, whereas all possible shapes are Catalan-counted. Random insertion permutations weight shapes unequally. Under that precise model, expected rank depth is $H_i+H_{n+1-i}-2$ and expected internal path length is $2(n+1)H_n-4n$.

For reconstruction, distinguish arbitrary binary trees from strict BSTs, and verify complete input consumption. Direct midpoint construction is linear; midpoint-first ordinary insertion is not. Full iterator scans have linear aggregate work even when one next operation is expensive. A rotation preserves inorder but needs a separate balance policy. Use these distinctions before applying a remembered formula: the question's duplicate policy, cost unit, height convention, query probability model and endpoint inclusivity determine the correct answer.

## 24. Worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 25. Final reasoning rules and examination traps

<!-- INCLUDE: review -->

## 26. Exact tree laboratory

<!-- LAB: bst -->

## 27. References and provenance

- Carnegie Mellon University, 15-122 Principles of Imperative Computation, Frank Pfenning, André Platzer, Rob Simmons and Iliano Cervesato: [Lecture 15, Binary Search Trees, Fall 2026 PDF, pages 1–22](https://www.cs.cmu.edu/~15122/handouts/lectures/15-bst.pdf). Source emphasis: contracts, interval validation and complete lookup/insertion implementation.
- Princeton University, COS226 Algorithms and Data Structures, Spring 2024 course archive; Robert Sedgewick and Kevin Wayne: [Binary Search Trees, 31 written slides](https://www.cs.princeton.edu/courses/archive/spring24/cos226/lectures/32BinarySearchTrees.pdf), and [Algorithms, Fourth Edition, §3.2](https://algs4.cs.princeton.edu/32bst/). Source emphasis: ordered operations, comparisons, rank/select, deletion and random-order models.
- University of California, Berkeley, CS61B Data Structures, Jonathan Richard Shewchuk, Spring 2014: [Lecture 24, Trees and Traversals](https://people.eecs.berkeley.edu/~jrs/61b/lec/24) and [Lecture 26, Binary Search Trees](https://people.eecs.berkeley.edu/~jrs/61b/lec/26). Source emphasis: parent links, traversals, bracketing and deletion cases.
- Massachusetts Institute of Technology, 6.006 Introduction to Algorithms, Erik Demaine and Srini Devadas, Fall 2011: [Lecture 5, Scheduling and Binary Search Trees, pages 1–8](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/d9c745bbfb610e9e53f6aef4261f3805_MIT6_006F11_lec05.pdf). Source emphasis: scheduling, successor and augmented rank.
- Stanford University, CS106B Programming Abstractions, Sean Szumlanski, Summer 2025: [Lecture 22, More on Binary Trees](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1258/lectures/22-bst/). Additional source emphasis: predecessor deletion, C++ lifetime and diagnostic exercises. Original reconstructions here do not reproduce its copyrighted exercise collection.
- Original Iranian examination references are identified individually beside the authenticated questions, including exact repository revision, booklet page and independently derived solution. They are not represented as official answer keys.
- [Source-selection and reconciliation audit](../reviews/a_bst-sources.html) and [scientific and visual audit](../reviews/a_bst-quality.html) separate observed checks, proof scope, finite experiments and remaining limitations. No finite bank guarantees a score on every unseen question.
