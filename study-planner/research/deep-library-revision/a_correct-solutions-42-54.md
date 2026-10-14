### Solution 42

**Correct option: 1. A stable index certificate records identity through the sort.** Input [5,1,5] has original indices 0,1,2. Output [1,5,5] is certified by [1,0,2]: the first output value comes from input index 1, the next from index 0, and the last from index 2. The indices occur exactly once, each output key matches its referenced input key, and the two equal keys preserve their original index order 0 before 2.

Check the three obligations separately. A permutation of indices establishes that no record is duplicated or lost. Matching referenced keys establishes consistency with the output. Increasing original indices among equal output keys establishes stability. Nondecreasing output keys still needs its own check; an index permutation by itself does not certify sorting order.

The alternative [1,2,0] matches the same numerical output and is a valid index permutation, but reverses the equal-key records and fails stability. An alternative beginning with index 0 or 2 assigns a key 5 to the first output value 1 and fails consistency. An alternative repeating an index fails conservation, even if the referenced key coincidentally matches both output positions. For records carrying other fields, the certificate should identify whole original records, not just bare key values. Labeled identities turn a visually invisible stability defect into a checkable mathematical statement.

### Solution 43

**Correct option: 3. Match an attaining witness to a universal bound.** In a minimization problem, suppose a feasible solution has cost 17 and a valid lower-bound proof establishes that every feasible solution has cost at least 17. Let OPT denote the optimal value. Feasibility gives OPT≤17 because the optimum cannot exceed the cost of an available candidate. The universal lower bound gives OPT≥17. Combining the two inequalities yields OPT=17, so the candidate is optimal.

Neither component is enough alone. A feasible cost-17 solution only provides an upper bound; there might be another solution costing 12. A lower bound of 17 alone does not establish that any feasible solution attains it. Their equality closes the proof. The bound must apply to the same instance, domain, and cost definition as the witness, and the witness's feasibility must be checked rather than assumed from its numerical cost.

An alternative claiming a unique optimum adds an unsupported conclusion: two different feasible solutions might both cost 17. An alternative treating 17 only as a possible value ignores the two-sided bound. An alternative reversing the inequalities confuses minimization with maximization. For maximization, a feasible witness is a lower bound and a universal bound is an upper bound; the same meeting-value argument then applies with reversed roles. Certificates prove a stated property, not every desirable property of a candidate.

### Solution 44

**Correct option: 3. Check every edge inequality.** The proposed distances are d(s)=0, d(a)=2, d(b)=5. Along s→a of weight 2, the inequality d(a)≤d(s)+2 holds with equality. Along a→b of weight 3, d(b)≤d(a)+3 also holds with equality. But the direct edge s→b has weight 4, and its inequality would require 5≤4, which is false. The proposed distance to b is therefore not certified.

The actual direct path gives distance at most 4, already contradicting the claimed shortest-path value 5. The longer path s→a→b has cost 5 and shows that 5 is a feasible path cost, but feasibility of a path does not make it shortest. This is the minimization distinction between an available upper bound and a matching universal lower bound.

In a valid certificate, edge inequalities telescope along every s-to-v path to give d(v) no greater than that path's cost. A rooted attaining path of cost d(v) supplies the reverse inequality, so the two bounds meet. Checking only the chosen parent edges can accept this false claim because the unchosen direct edge is exactly the missed shortcut. An alternative that rejects only the a→b edge has the wrong arithmetic. A certificate verifier must include all relevant graph edges, not merely the edges used to display an attractive candidate route.

### Solution 45

**Correct option: 2. Local equalities do not establish a rooted attaining path.** In the graph s→a with weight 5 and the zero-weight edges a→b and b→a, the proposed labels d(s)=d(a)=d(b)=0 pass all edge inequalities. The first is 0≤5; the other two are 0≤0. Choosing parent(a)=b and parent(b)=a also gives local parent equalities because both parent edges have zero weight.

Nevertheless, following either parent chain cycles between a and b and never reaches s. No s-to-a or s-to-b path of cost zero exists: every such path must first use s→a, paying 5, and the subsequent zero-weight moves cannot reduce that cost. The actual shortest distances to a and b are 5. The local equations define a consistent cycle of labels without providing an attaining witness rooted at the source.

The missing certificate condition is that every relevant parent chain reaches s, or an equivalent verified acyclic/rooted structure. A depth label decreasing toward the root can help certify that property if checked correctly. A claim that nonnegative edges alone exclude a parent cycle is false because zero-weight cycles are possible. A claim that passing edge inequalities proves exact distances supplies only one direction of the optimality argument. The path witness is the independent second direction and must not be replaced by unrooted local equalities.

### Solution 46

**Correct option: 2. A valid certificate can include a negative edge.** For s→a of weight 4, s→b of weight 5, and a→b of weight −3, proposed labels are d(s)=0, d(a)=4, d(b)=1. The edge checks are 4≤4, 1≤5, and $1\le4-3=1$. All hold. The path s→a attains 4, and the path s→a→b attains 1, so both vertex labels have rooted attaining witnesses.

To prove the certificate's lower-bound direction, sum each checked inequality along any s-to-v path. Intermediate distance labels cancel, leaving d(v)≤the path cost because d(s)=0. Negative individual edge weights do not invalidate that algebra. The attaining paths establish that the minimum path cost is at most d(v), closing equality for a and b.

An alternative rejecting the certificate merely because −3 is negative confuses a particular algorithm's operational preconditions with this proof framework. Standard Dijkstra reasoning requires a nonnegative-weight condition; a distance certificate verified independently uses different obligations. An alternative selecting direct cost 5 ignores the cheaper two-edge path. The example has no directed cycle, so no negative cycle issue arises. Certificates must still restrict claims to vertices with verified reachability and account for infinity labels if used; those additional representations are not present in this three-vertex finite-label problem.

### Solution 47

**Correct option: 1. Sum the local inequalities around the cycle.** A directed cycle with edge weights 2,−5,1 has total weight −2. Suppose finite distance labels satisfy every edge inequality on this cycle. Writing the three inequalities and adding them cancels all distance labels on both sides, leaving $0\le2-5+1=-2$, an impossibility. Therefore no finite label assignment can satisfy every required edge inequality on that cycle.

If the cycle is reachable from the source and walks may repeat vertices, traversing it an additional time decreases the cost by 2. There is no finite minimum walk cost for the affected reachable destinations: costs can decrease without bound. This operational explanation agrees with the algebraic obstruction. It is not necessary to guess which one edge will fail for a particular tentative labeling; at least one must fail by the summed contradiction.

The conclusion concerns a negative total cycle, not a single negative edge. Question 46 supplies a valid negative-edge example with no negative cycle. A zero-total cycle does not produce this strict contradiction, though it can still expose an unrooted-parent defect as in Question 45. Reachability matters when interpreting source distances; an isolated unreachable negative cycle does not imply that every reachable distance is unbounded. A certificate's selected domain and infinity conventions therefore must be specified when moving beyond the finite reachable cycle considered here.

### Solution 48

**Correct option: 2. Feasibility of a greedy output does not prove optimality.** An earliest-start rule chooses the long interval [0,10) first. Each of [1,2), [2,3), and [3,4) then conflicts with it, so the rule selects only one interval. The three short intervals are mutually compatible under the half-open endpoint convention: the end of one can equal the start of the next. Choosing them yields three intervals.

The greedy output is feasible but not maximum-cardinality. In this instance, three is also optimal: the long interval excludes all three short ones, and without the long interval there are only those three candidates. The example gives a concrete strict improvement and an exact optimum, not just a suspicion that another rule might perform better.

An alternative claiming that earliest start is universally optimal confuses a plausible priority with an exchange argument. Earliest finishing time supports a different standard greedy proof for unweighted interval scheduling; it is not interchangeable with earliest start. An alternative rejecting touching short intervals uses a closed-interval conflict convention rather than the stated half-open one. An alternative calling the one-interval result infeasible also misidentifies the problem: it satisfies compatibility but fails optimality. Before proving a method, fix the objective, endpoint rules, and admissible schedules; otherwise even a correct proof can address the wrong problem.

### Solution 49

**Correct option: 1. Compute the mass and interpret the equality condition.** The complete listed leaf set has depths 1,2,3, so its mass is $2^{-1}+2^{-2}+2^{-3}=1/2+1/4+1/8=7/8$. The result is below one and therefore cannot prove that the finite binary tree is full. In fact, it refutes fullness under the complete-leaf-set premise, because every finite full binary tree has total leaf mass exactly one.

One realizing tree has a root with a left leaf and a right internal child. That child has one leaf at depth 2 and another internal child whose single child is the depth-3 leaf. The unoccupied sibling at depth 3 accounts for the missing mass 1/8. This explicit structure shows both that the depth list is realizable and where the conservation deficit occurs.

An option giving one assumes a second depth-3 leaf that is not listed. An option declaring fullness from the existence of three leaf levels confuses depth variety with each internal node having two children. A greater-than-one result contradicts the root mass bound. The equality characterization needs a finite tree and the complete set of leaves; a partial leaf sample can have mass below one even within a full tree. State those premises before applying a structural conclusion from a numerical sum.

### Solution 50

**Correct option: 3. Count the weakly ordered triples and retain the offset.** Each increment corresponds to one triple $1\le i\le j\le k\le n$. Map it to the strictly increasing triple $(i,j+1,k+2)$ in {1,…,n+2}. Conversely, a strict triple (u,v,w) maps to (u,v−1,w−2), satisfying the original weak inequalities. The map is a bijection, so the increment count is $\binom{n+2}{3}$ and the final accumulator is $c_0+\binom{n+2}{3}$.

For n=2, the four triples are (1,1,1), (1,1,2), (1,2,2), and (2,2,2), matching $\binom43=4$. This small case exposes why repeated indices must count. Selecting three distinct original indices would instead count $\binom n3$, which is wrong. Multiplying n³ ignores the order constraints and includes many forbidden triples. Omitting c₀ counts work but does not give the requested final value.

An independent sum groups by j: there are j possible i-values and n−j+1 possible k-values, giving $\sum_{j=1}^n j(n-j+1)=n(n+1)(n+2)/6$. At n=0, no body executes and the accumulator remains c₀; the polynomial also gives zero increments. The exact arithmetic model must support every loop-index update as well as the accumulator. The bijection proves a formula for dependent loops without assuming their bounds are independent.

### Solution 51

**Correct option: 2. Derive the indices from the recursive parameters.** With N=10 and initial call store(9,0), the source–destination pairs are (9,0), (7,1), (5,2), (3,3), and (1,4). The next call has source index −1 and returns before accessing either array. There are five copied elements, and the last copied source index is 1.

At the kth active call, starting with k=0, the parameters satisfy $n=N-1-2k$ and i=k. An access occurs precisely while n≥0. For N=10, that allows k=0,…,4. The caller must allocate at least $\lceil N/2\rceil=5$ destination positions. The source indices lie in [0,N), and the negative termination call has no read because the guard is checked first.

An option ending at source index zero uses the even-index sequence rather than every other index starting at the odd last index 9. Counting six includes the base call as if it wrote an element. A destination increment of two leaves gaps and does not implement compact copying. For an odd N, the last copied source index is zero; for an even positive N, it is one. For N=0, the initial source index is already −1 and no element is copied. Safety and the index relation explain all these cases together.

### Solution 52

**Correct option: 2. Match the sum to the next unprocessed index.** With s=0 and k=1, the invariant is $s=(k-1)^2$. It holds initially because both sides are zero. One body adds 2k−1 and then increments k. The new sum is $(k-1)^2+(2k-1)=k^2$, which equals $(k'-1)^2$ because k'=k+1. Thus the equality is preserved.

To derive the final result, also keep the bounds $1\le k\le n+1$ for an integer n≥0. The guard k≤n implies that advancing k preserves the upper bound. On exit k>n, the integer bounds force k=n+1, and the equality gives s=n². The variant n−k+1 is nonnegative at every guard checkpoint and decreases by one in each body. At n=0, initialization gives k=1, the guard is false, and s=0=n².

An invariant s=k² fails at initialization. An expression involving (k+1)² is offset in the wrong direction. A claim about the target n² alone is not the useful intermediate relation because it normally holds only at completion. The equality without bounds is insufficient to infer the exit value of k, and it says nothing by itself about termination. This example shows how a functional relation, range information, guard, and progress measure cooperate in a complete proof.

### Solution 53

**Correct option: 2. Strengthen the recursive contract before composing it.** A child routine that merely returns sorted data could replace every input value with zero and satisfy that weak condition. A parent that merges those sorted results would then return a sorted array containing the wrong values. Therefore sortedness of each child result is insufficient to prove that the whole recursion sorts the original input.

The required child contract includes preservation of the child's complete input multiset. For a split into left and right parts, their original multisets combine to the parent's multiset. By strong induction, both child outputs are sorted and preserve their own inputs. A correct merge then returns a sorted output whose multiset is the union of those child outputs, hence exactly the original parent's multiset. If stability is promised, the split order and merge's tie policy require additional proof.

Termination needs strictly smaller recursive inputs above a complete base region; none of these content properties alone proves it. An alternative adding only a runtime bound does not recover lost values. An alternative requiring both children to return identical arrays would be unjustified for different inputs. An alternative claiming sortedness alone is enough is refuted by the all-zero implementation. Strengthening an induction hypothesis is legitimate when one also proves that strengthened statement at the base and induction steps; it cannot simply be assumed because the parent needs it.

### Solution 54

**Correct option: 1. The initialization introduces an extra candidate.** A maximum routine initialized with best=0 and updated only by larger encountered values returns zero on the nonempty input [−2]. The true maximum is −2, which is the only input element. The routine's actual invariant is that best equals the maximum of zero and the processed values, not necessarily the maximum of the processed values alone.

The faulty method works for inputs containing a nonnegative maximum, which can conceal the defect in ordinary positive examples. Its failure on one admitted all-negative input refutes universal correctness. Returning zero also fails the witness property that a maximum of a nonempty finite input must be one of that input's values.

For a contract admitting arbitrary nonempty numeric arrays, initialize best to A[0] and begin scanning at index 1. Then the processed prefix is nonempty, best is one of its values, and no processed value exceeds best. Each comparison preserves those properties, and at the final index the prefix is the whole input. An alternative repair using a negative-infinity sentinel requires a type and comparator that support that sentinel, plus appropriate handling of NaN or other non-total values. An empty-input contract needs a separately defined result; neither A[0] initialization nor an unexplained zero return defines a maximum of an empty set.
