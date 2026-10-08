# Uninformed Search: BFS, DFS, Uniform Cost, and Iterative Deepening

## 1. Sources, prerequisites, and the chapter contract

This chapter develops search as a precisely specified computation. The four core written courses are UC Berkeley CS188, CMU 15-281, MIT 6.034 and Edinburgh INF2D. Stanford CS221 supplies a supplementary application. The final references and linked source audit identify the actual documents, authors where verified, selection reasons and limits of access. Their common framework is compared critically; a convenient introductory statement is not accepted without its assumptions.

You need finite sums, geometric series, elementary asymptotic notation, queues, stacks, priority queues and the preceding chapter's distinction between physical states and search nodes. We begin with a known deterministic transition model and a goal predicate. An action sequence is the output. Uncertainty, adversarial choices and heuristic estimates are not silently inserted into that model. They require later algorithms.

The goal is to derive and apply BFS, DFS, depth-limited search, iterative deepening, uniform-cost search and bidirectional search. Worked examples include exact frontier traces, mathematical counting, correctness arguments, counterexamples and implementation decisions. A statement of completeness must name the search variant and assumptions. A cost claim must distinguish the number of examined nodes from the work needed to examine each node. The problem bank and final rules are part of the instruction, not a replacement for the proofs.

## 2. Search states, paths, and node records

A state represents the information needed to determine legal actions, their results, their costs and goal status. Let the start state be $s_0$, the action set at $s$ be $A(s)$, the transition be $T(s,a)$ and the edge cost be $c(s,a,T(s,a))$. A node represents a particular path to a state. Its record contains a state, a parent-node reference, the incoming action, depth and accumulated cost.

$$n=(s,\text{parent},a,d,g),\qquad d(n')=d(n)+1,\qquad g(n')=g(n)+c(s,a,s').$$

Two nodes can have the same state and different parents, depths or costs. In the graph $S\to A\to X$ and $S\to X$, the two copies of $X$ are distinct search nodes. When costs are $1,1,8$, respectively, their costs are $2$ and $8$. Discarding a duplicate without deciding what information is being compared can remove the better route.

The state-space graph contains one vertex per distinct state. The search tree unfolds possible action sequences. A two-state cycle can therefore generate an infinite tree. A parent pointer is not an edge of the physical world: it is the algorithm's explanation of how that particular node was reached. Reconstruct a solution by following parents to the root and reversing the collected actions. Its time is proportional to the returned depth.

## 3. Declare what is counted

We use these terms consistently. A node is **generated** when a successor candidate is constructed. It is **accepted** when inserted into the frontier. It is **selected** when a valid record is removed for examination. It is **expanded** only when its successors are enumerated. A selected goal is not expanded in this chapter. A stale heap entry is physically removed and discarded before logical selection, so it contributes to raw removals but not to the selected or expanded counters. Initial insertion is counted separately when needed.

A frontier is the set or ordered work list of unresolved candidate paths. A discovered set remembers states accepted at least once. A closed or settled set remembers states whose selected records have received a particular final treatment. The word visited is avoided unless explicitly defined: different courses use it for discovery or expansion, and an examination can exploit that ambiguity.

For a frontier that begins with the root, every accepted child adds one entry and every removal subtracts one. Thus, after any finite prefix,

$$|F|=1+I-R,$$

where $I$ counts accepted child insertions and $R$ counts all removals, including stale entries. This is an accounting identity, not a complexity theorem. Expanded-node count cannot replace $R$ if stale or goal entries are present.

## 4. One framework, several priorities

Search repeatedly selects a frontier node, decides whether to terminate, and otherwise generates successors. BFS selects the earliest inserted node; DFS selects the most recently scheduled node; UCS selects a node of minimum accumulated cost. DLS adds a depth constraint. IDS restarts a correct DLS computation with increasing limits. A priority rule alone does not specify duplicate handling, successor order, goal timing or tie breaking.

For all finite laboratory graphs, successors appear in the written edge-list order. DFS inserts them in reverse so that the first written successor is examined first. UCS breaks equal-cost ties by insertion time. The laboratory uses graph search for BFS, DFS and UCS; DLS and IDS use current-path cycle checking. All goal tests occur on selection, before expansion and before the depth boundary test. These details make traces reproducible.

```python
while frontier:
    node = select(frontier)
    if obsolete(node):
        continue
    if is_goal(node.state):
        return reconstruct(node)
    for child in successors(node):
        if admission_rule(child):
            insert(frontier, child)
return FAILURE
```

The functions in this skeleton are obligations, not magic. In particular, the UCS admission rule compares path costs, whereas BFS can safely reject a state already discovered at a smaller or equal depth.

## 5. Breadth-first search and its layer invariant

BFS stores its frontier in a FIFO queue. Insert the start, mark its state discovered, then repeatedly remove the front. After a non-goal removal, append each not-yet-discovered successor and mark it immediately. Marking on insertion prevents two same-layer parents from inserting the same child repeatedly.

**Layer invariant.** Immediately before a removal, the queue contains nodes at at most two consecutive depths. All nodes at the smaller depth precede all nodes at the larger depth. Initially the queue contains only depth zero. Removing a depth-$k$ node appends only depth-$k+1$ children behind the remaining depth-$k$ nodes. Once that layer is exhausted, the same argument applies to $k+1$. This inductive proof establishes nondecreasing selection depth.

The first discovered route to a state has minimum edge count. Suppose a shorter route existed. Its predecessor would have been selected in an earlier layer and would have discovered the state earlier, a contradiction. This is why a single discovery bit suffices for unweighted shortest paths. It is not a theorem about arbitrary costs.

<!-- SIM: bfs -->

## 6. A complete BFS trace

Use the directed edges $S\to A$, $S\to B$, $A\to C$, $A\to D$, $B\to D$, $B\to G$, and $D\to G$, in that order within each adjacency list. All costs are one. After expanding $S$, the queue is $[A,B]$. After $A$, it is $[B,C,D]$. Expanding $B$ rejects the already discovered $D$ and appends $G$, giving $[C,D,G]$. Expanding the leaf $C$ leaves $[D,G]$. Expanding $D$ rejects $G$. Selecting $G$ returns $S,B,G$.

The selected order is $S,A,B,C,D,G$, while the expanded order excludes $G$. The returned path has two edges, even though $D$ was discovered through $A$ before another path through $B$ was considered. BFS does not compare the costs of those routes because they have identical unit edge costs. With goal-on-generation, the algorithm could return while expanding $B$, before selecting $C$ or $D$; the solution depth is unchanged, but the operation counts are different.

## 7. BFS completeness and cost optimality

BFS is complete when every node has finitely many successors, successor generation terminates, and some goal has finite depth. There are finitely many nodes before that depth, so FIFO processing eventually reaches it. The entire graph need not be finite. An infinitely branching root breaks the argument: enumerating its children can prevent any child from being selected.

BFS minimizes edge count. It minimizes cost when every edge has the same nonnegative cost, or more generally when every deeper solution is no cheaper than every shallower solution and same-depth ties cannot hide different solution costs. Equal costs are a convenient sufficient condition, not a necessary condition for one particular graph. With $S\to G$ of cost $9$ and $S\to A\to G$ of costs $1,1$, BFS returns the one-edge path costing $9$, not the optimum $2$.

Zero equal costs make every reachable solution cost zero, so BFS remains cost-optimal although it still prefers fewer actions. Negative equal costs reverse the preference for depth; cycles can make the objective unbounded below. The slogan that equal weights make BFS optimal needs the nonnegative qualification if negative weights are allowed.

## 8. Exact BFS counts and the extra exponent

For a full $b$-ary tree, let $d$ denote shallowest goal depth, with the root at zero. For $b\ne1$ the number of nodes through depth $d$ is

$$N_b(d)=\sum_{i=0}^{d}b^i=\frac{b^{d+1}-1}{b-1}.$$

For $b=1$, it is $d+1$. If every depth-$d$ node is examined but none expanded, this gives $\Theta(b^d)$ for fixed $b>1$. With goal testing only on removal, however, earlier non-goal nodes at depth $d$ may generate depth-$d+1$ children before the last goal is removed. In the complete worst-case arrangement with that goal last,

$$G=N_b(d)+b(b^d-1).$$

Here $G$ includes the initial root and every generated child. The queue just before the last depth-$d$ goal is removed has $1+b(b^d-1)$ entries. This explains textbook bounds written as $O(b^{d+1})$ for generation or memory, compared with $O(b^d)$ when counting selections through the goal layer or using goal-on-generation. With fixed constant $b$, the two differ by a constant; when $b$ is itself an input parameter, retain that factor. An examination's convention must be read before choosing a formula.

## 9. Depth-first search, stack order, and backtracking

DFS continues one unresolved branch before its pending siblings. With an explicit stack whose top is the right end, push successors in reverse desired examination order. If $A,B,C$ are pushed in that written order, $C$ is removed first. Reversing the push order gives $A$ first. A statement such as alphabetical DFS is incomplete without distinguishing generation order from removal order.

On the graph of Section 6, discovery-on-insertion DFS selects $S,A,C,D,G$ and returns $S,A,D,G$. The pending $B$ remains in the stack. This path has three edges, even though a two-edge solution exists. Recursive DFS with discovery on recursive entry can differ from an implementation that discovers all siblings before descending; both can be valid DFS graph searches, but their parent trees need not match.

Backtracking is the return to an ancestor with an unexamined successor. A memory-efficient recursive implementation can generate one successor at a time, retaining only recursion frames and the current-path membership set. An explicit stack that eagerly inserts all siblings uses more frontier entries. State which version is being analysed before asserting linear space.

<!-- SIM: dfs -->

## 10. DFS completeness and memory qualifications

Tree DFS can follow an infinite branch forever while a goal waits in a sibling. Preventing repeated states on the current path removes cycles but does not remove an infinite acyclic chain. Finite graph DFS with a global discovered set is complete for reachability, because each state is accepted once and there are finitely many states and edges to examine.

For a finite-depth full tree of maximum depth $m$, eager sibling storage has maximum frontier size $1+(b-1)m$ and time $\Theta(b^m)$ for fixed $b>1$. Lazy recursive generation stores $O(m)$ frames plus successor-generation state; if each frame materializes $b$ children it uses $O(bm)$ instead. A global discovered set adds $O(V)$ memory on an explicit graph. Therefore “DFS uses linear space” usually refers to depth, a tree or path-checking variant, and a particular successor implementation; it does not make a global set of millions of states disappear.

For a known finite graph with adjacency lists, BFS and DFS each examine at most $V$ accepted states and $E$ edges: $O(V+E)$ time and $O(V)$ auxiliary storage. This graph-size result and exponential depth bounds describe different input measures, not contradictory analyses.

## 11. Depth-limited search must distinguish three outcomes

DLS examines only paths of depth at most a limit $L$. It can return a solution, **cutoff**, or **failure**. A goal at exactly $L$ is valid, so goal testing precedes the boundary test. Failure means no solution exists among the paths the call is responsible for and no potentially useful boundary was truncated. Cutoff means the limit prevented a deeper search; it is not evidence that the underlying problem has no solution.

The conservative implementation returns cutoff whenever a non-goal is reached with zero remaining depth, even if that state might be a leaf. This avoids generating successors at the boundary, but can cause one extra IDS iteration. A more precise implementation examines whether any eligible successor remains and returns failure at a genuine exhausted leaf. Both are sound if their conventions are explicit; their cutoff counts differ.

For finite branching and finite limit, DLS terminates. It is not globally complete for a fixed limit below the shallowest goal depth. When $L\ge d$, a correctly implemented exhaustive DLS will find a solution, but it can return a deeper or costlier goal than another accessible solution. A limit is a resource constraint, not an optimization rule.

<!-- SIM: dls -->

## 12. Why a Boolean visited set can break DLS

Consider $S\to A\to B\to X\to G$ and $S\to X$, with limit $L=3$ and the $A$ branch first. The first occurrence of $X$ has depth three and cannot expand. A global Boolean visited bit can then reject the depth-one occurrence reached directly from $S$. The two-edge solution is lost even though it is within the limit.

The missing information is remaining depth. A path reaching $X$ at depth one has two expansion levels available; the depth-three occurrence has zero. Dominance requires at least as much remaining budget, not mere state equality. The simplest safe implementation uses a current-path set and removes states when backtracking. It may revisit a state through another path, but it will not wrongly equate different budgets.

A transposition table can store the largest remaining budget for which a state has already been sufficiently searched and re-explore when a larger budget arrives. Its correctness depends on exactly what “sufficiently searched” means, especially with path-dependent forbidden ancestors. Do not transplant an unproved table optimization into DLS. The laboratory uses path checking so that its proof does not rely on that subtle optimization.

<!-- SIM: depth-alias -->

## 13. Iterative deepening and its correctness

IDS runs DLS with limits $0,1,2,\ldots$. Every iteration resets its path or duplicate data. If an iteration returns a solution, return it. If it returns genuine failure, no deeper iteration is needed. If it returns cutoff, increase the limit. Carrying the previous iteration's discovered set forward can reject the root or all previously seen children and destroy completeness.

Let $d$ be the shallowest solution depth. Finite branching makes each finite iteration terminate. For every limit below $d$, no goal is within range. At limit $d$, an exhaustive correct DLS must encounter a goal. Thus IDS is complete under these assumptions and returns a minimum-depth solution. With equal nonnegative edge costs it is cost-optimal. For varying costs, the shallowest goal can still be expensive.

IDS does not necessarily terminate on an unsolvable infinite space. Completeness promises to find an existing finite solution, not to decide every impossible problem. With finite state space and path-cycle checking, all simple paths have bounded length, and a genuine-failure iteration can eventually terminate the unsolvable search.

<!-- SIM: ids -->

## 14. Deriving the repeated-work formula

To compare exhaustive iterations fairly, suppose every DLS iteration visits every node through its limit and include the root in every iteration. A node at depth $i$ appears in the iterations $i,i+1,\ldots,d$, hence $d-i+1$ times. Therefore

$$I_b(d)=\sum_{i=0}^{d}(d-i+1)b^i.$$

Reordering counts also gives $I_b(d)=\sum_{L=0}^{d}N_b(L)$. For $b\ne1$, substituting the geometric sum and simplifying yields

$$I_b(d)=\frac{b^{d+2}-(d+2)b+(d+1)}{(b-1)^2}.$$

For $b=1$, $I_1(d)=(d+1)(d+2)/2$. For fixed $b>1$, the leading terms of $I_b(d)$ and $N_b(d)$ imply

$$\lim_{d\to\infty}\frac{I_b(d)}{N_b(d)}=\frac{b}{b-1}.$$

This is an exhaustive-iteration ratio under a specific count convention. It is not an average-case ratio over randomly positioned goals. On a chain, the repeated work is quadratic while a single traversal is linear. The usual small-overhead intuition depends on exponential layer growth. In an actual final iteration, IDS stops at its first goal, so use its actual partial traversal when an exact trace is requested.

<!-- SIM: counts -->

## 15. Uniform-cost search orders complete path costs

UCS selects minimum $g$, the cost accumulated from the start. It does not select the smallest last edge, the fewest actions, or the state that looks closest to the goal. Its frontier is a priority queue. A state may initially be reached expensively and later reached more cheaply; the new route must replace or supersede the old frontier entry.

Use $S\to A$ with cost $4$, $S\to B$ with cost $1$, $B\to A$ with cost $1$, $A\to G$ with cost $2$, and $B\to G$ with cost $8$. After $S$, the frontier contains $B:1,A:4$. Expanding $B$ improves $A$ to $2$ and creates $G:9$. Expanding the improved $A$ improves $G$ to $4$. The old $A:4$ record, if still physically present in a lazy heap, is stale. Selecting the valid $G:4$ returns $S,B,A,G$.

A discovered-once rule would discard the improvement to $A$ and also reject the later improvement of the already discovered goal, returning cost $9$ rather than $4$. A hybrid that permits improving the goal but still blocks the improvement to $A$ would return $6$; it is incorrect too. A goal-on-generation rule could stop at $G:9$ while expanding $B$. These are separate errors. Correct UCS admits improved routes and accepts a goal only when a non-stale minimum-cost entry is selected.

<!-- SIM: ucs -->

## 16. The UCS frontier-cut proof

Assume nonnegative edge costs. Suppose a valid selected goal has cost $C$ but there exists a cheaper goal path of cost $C'<C$. Consider the first vertex on that cheaper path not yet settled. Its predecessor has been settled, or it is the start. When that predecessor was expanded, relaxation inserted or retained a frontier route to the vertex with cost at most the corresponding optimal-path prefix.

Because the remaining path costs are nonnegative, that prefix costs at most $C'$. Thus a valid frontier candidate of cost at most $C'<C$ exists, contradicting selection of the goal as a valid minimum-cost entry. The same cut argument proves that the first valid removal of any state settles its optimal cost. It depends on relaxation and on nonnegative suffix costs. A bare “priority queue” label does not supply either condition.

Strictly positive edge costs are not needed for this optimality proof. Zero-cost edges preserve nondecreasing path costs. They can, however, prevent termination in infinite spaces. Optimality conditional on returning and completeness are distinct properties and must be analysed separately.

## 17. A robust UCS implementation

Maintain `best[state]`, the least discovered cost, and immutable node records. On improvement, insert a new heap record with a monotonically increasing serial number. On removal, discard a record whose stored cost differs from `best[state]`. Then test the goal. Heap ties use the serial number rather than comparing state objects or paths. The node record's parent remains attached to that exact route, so an improvement does not corrupt an older path explanation.

```python
from heapq import heappush, heappop
from itertools import count

def uniform_cost(start, is_goal, successors):
    serial = count()
    # Node records are (state, parent_record, incoming_action, cost).
    root = (start, None, None, 0)
    heap = [(0, next(serial), root)]
    best = {start: 0}
    while heap:
        cost, _, node = heappop(heap)
        state = node[0]
        if cost != best[state]:
            continue
        if is_goal(state):
            actions = []
            while node[1] is not None:
                actions.append(node[2])
                node = node[1]
            return list(reversed(actions)), cost
        for action, target, step in successors(state):
            if step < 0:
                raise ValueError("UCS requires nonnegative edge costs")
            new_cost = cost + step
            if target not in best or new_cost < best[target]:
                best[target] = new_cost
                child = (target, node, action, new_cost)
                heappush(heap, (new_cost, next(serial), child))
    return None
```

Equal-cost alternatives are not inserted in this version. This both fixes a deterministic parent choice and prevents a zero-cost cycle from producing infinitely many equal-cost duplicate records on a finite graph. Floating-point equality can complicate stale checks; exact integer or rational costs avoid that issue in our models. An arbitrary epsilon comparison is not automatically safe for every shortest-path instance.

## 18. UCS completeness, zero costs, and shrinking positive costs

On a finite graph with nonnegative costs, correct UCS graph search terminates after finitely many useful relaxations and returns an optimal solution if one exists. A common sufficient condition for infinite, finitely branching search trees is a positive lower bound $\varepsilon$ on all edge costs and a goal of finite cost $C^*$. Every path of cost at most $C^*$ then has depth at most $\lfloor C^*/\varepsilon\rfloor$, so only finitely many competing prefixes exist.

Positive costs without a uniform lower bound are insufficient. Let a chain have successive costs $1/2,1/4,1/8,\ldots$ and let the root also connect directly to a goal at cost $1$. Every chain prefix costs $1-2^{-k}<1$. UCS follows the chain forever; the goal waits. A zero-cost infinite chain gives an even simpler example. Graph duplicate removal does not help because every chain state is different.

The more general useful condition is that only finitely many relevant candidate prefixes precede a finite-cost solution, with fair handling of any cost ties. A lower edge bound is one way to ensure this. Do not confuse a finite minimum cost in a finite graph with an infimum of zero in an infinite graph.

<!-- SIM: starvation -->

## 19. UCS complexity in tree and graph measures

Let $K=\lfloor C^*/\varepsilon\rfloor$. The nonnegative-cost tree search can select nodes with cost at most $C^*$, all at depth at most $K$. Expanding them can generate children one level deeper, so a conservative generated-node and frontier bound is $O(b^{K+1})$. A table that counts only selected sublevel nodes can report $O(b^K)$. Heap operations add a logarithmic factor to CPU work; node-count tables usually omit it intentionally.

For a finite explicit graph, binary-heap Dijkstra/UCS with decrease-key is commonly analysed as $O((V+E)\log V)$ and $O(V)$ auxiliary label/heap storage, besides adjacency lists. With lazy duplicate entries, there can be $O(E)$ physical heap entries and $O(E\log E)$ heap work. For simple graphs, $\log E=O(\log V)$, but the memory distinction still matters. State labels and the stored graph itself must not be omitted from a practical memory budget.

The number of states with true distance below $C^*$ controls necessary work before an optimal goal can be selected. Equal-distance states may or may not be examined first depending on tie breaking. Large edge costs beyond the optimal-cost contour do not by themselves force UCS to expand those expensive paths.

## 20. Negative edges and objective transformations

With $S\to G$ costing $2$, $S\to A$ costing $5$, and $A\to G$ costing $-10$, UCS returns cost $2$ before seeing the path costing $-5$. There is no cycle, yet the proof fails: the remaining negative suffix makes a costly prefix lead to a cheap solution. Negative cycles create another issue, potentially eliminating a finite optimum altogether. Bellman–Ford or topological dynamic programming may be appropriate under their own assumptions; neither is UCS with an unchanged stopping rule.

Multiplying all edge costs by a positive constant preserves complete-path rankings. Adding the same constant $k$ to every edge changes a path of depth $d$ from $g$ to $g+kd$. Routes with different action counts can change order. Therefore adding a constant to remove negative costs is generally unsound. If all feasible complete solutions have exactly the same length, their final rankings are preserved, but internal UCS correctness still requires appropriate transformed nonnegative edges and a correctly represented termination structure.

## 21. Bidirectional BFS and what backward search means

For a known goal state and reversible or explicitly enumerable predecessor transitions, run BFS forward from the start and backward from the goal. Backward search uses edges of the reversed directed graph. It does not assume that an original action can be executed backward in the physical world. A backward parent pointer must ultimately identify a legal forward continuation toward the goal.

If the search tree has comparable branching in both directions and the solution depth is $d$, balanced fronts can reduce the rough work from $b^d$ to $b^{d/2}$. This is an ideal estimate, not a universal property. A goal predicate with millions of satisfying states, expensive predecessor generation, asymmetric branching or a narrow one-directional chain can remove the benefit.

For a safe implementation, expand complete distance layers and maintain the best discovered connection length $\mu$, including crossing edges. If $a$ and $b$ are the next unsettled layer distances in the two directions, then no unaccounted shorter route exists once $a+b\ge\mu$, provided the distances and crossing updates follow the standard two-sided settled-front invariant. A simpler practical alternative is a correctly specified layer-synchronous algorithm with its own stopping proof. Arbitrarily switching directions and stopping at the first visual overlap is not a proof.

<!-- SIM: bidirectional -->

## 22. Bidirectional UCS and the first-contact trap

Weighted search must compare complete connection costs. Maintain forward and backward tentative distances, settled sets and a best complete route cost $\mu$. Whenever an edge joins known distances, update $\mu$ with $d_F(u)+c(u,v)+d_B(v)$. Also consider a state known on both sides. Continue valid minimum-cost removals until the minimum unsettled forward key plus the minimum unsettled backward key is at least $\mu$.

The lower-bound argument follows the same frontier-cut idea as ordinary UCS: any better unresolved route must cross the unsettled boundaries and cannot have cost below the sum of their minimum keys. This requires nonnegative costs, correct reverse edges, valid queue minima after stale removal, and all relevant connection updates. A meeting gives an upper bound, not immediate optimality.

For example, two fronts may first connect along a route costing $12$ while an unresolved route costs $8$. Returning the first contact confuses discovery with certification. The laboratory's bidirectional figure is a distance-layer illustration; it is not presented as an implementation of weighted bidirectional Dijkstra. The weighted stopping rule is taught and tested separately in the solved bank.

## 23. State keys, dominance, and path constraints

Duplicate pruning is valid only when the state key preserves every feature that affects legal continuations, goal status and future costs. If possession of a key enables opening a door, merging `(room, has_key)` into `room` can discard the only solvable route. If the task forbids visiting a location twice, the visited-location set becomes part of the state, or the search must explicitly treat it as a path constraint.

For unconstrained nonnegative shortest paths, reaching the same sufficient state more cheaply dominates a more expensive route: append the same legal suffix to both and the cheaper prefix stays cheaper. With both cost and remaining fuel, a single scalar may no longer dominate. A cheap route with no fuel and a costly route with enough fuel can both be necessary. Keep nondominated labels or augment the state.

Depth-limited search is the same principle in another form: remaining depth is a resource. The correct comparison depends on the question being solved. A graph-search optimization is not a universal permission to delete every repeated-looking symbol.

## 24. Applications: segmentation, grids, and joint planning

In dictionary segmentation of a string of length $n$, use the current character index as the state. An edge advances to the end of a matching dictionary word. Every edge costs one when minimizing word count, so BFS finds a segmentation with the fewest words. The graph is acyclic because the index strictly increases. DFS finds some segmentation but need not minimize word count.

If cost depends on the previous word, index alone is insufficient; augment the state with that word. If maximizing word count is represented by cost $-1$ per word, BFS minimizes the opposite objective and UCS's nonnegative-cost theorem no longer applies. A longest-path dynamic program on the acyclic index graph is a suitable alternative. This independent application is motivated by Stanford's Search assignment, with new examples and full solutions here.

Grid movement with unit costs is a BFS problem only after walls, permitted moves and state features have been specified. For labelled robots that cannot share a cell, the count of legal joint positions in $N$ cells is $N(N-1)\cdots(N-r+1)$, not $N^r$. Edge-swap collisions constrain joint transitions as well as states. A CMU activity uses the unconstrained product count; our exercises distinguish that upper bound from collision-free configurations.

<!-- SIM: segmentation -->

## 25. A decision table with explicit assumptions

| Method | Selection rule | Completeness | Cost optimality | Important storage qualification |
|---|---|---|---|---|
| BFS | FIFO / minimum depth | Finite branching, finite-depth solution | Equal nonnegative costs suffice | Frontier can be exponential in solution depth |
| DFS tree search | LIFO / one branch first | Not on arbitrary infinite trees | No general guarantee | Lazy frames can be linear in depth |
| DFS graph search | LIFO plus global discovery | Finite reachable graph | No general guarantee | Global discovery requires state storage |
| DLS | DFS with depth limit | Only for solutions within a sufficient limit | No general guarantee | Path checking avoids budget-insensitive pruning |
| IDS | DLS limits from zero upward | Finite branching, finite-depth solution | Minimum depth; equal nonnegative costs suffice | Restarts trade repeated work for bounded frontier |
| UCS | Minimum accumulated cost | Finite graph, or suitable finite cost sublevels | Nonnegative costs and correct relaxation | Lazy heaps can hold multiple records per state |
| Bidirectional BFS | Two distance layers | Searchable predecessors and correct stopping | Unit/equal nonnegative costs | Two frontiers plus intersection/distance data |

Read each row together with its qualification. In particular, a finite graph's $O(V)$ storage and a tree frontier's $O(bm)$ are different statements. Tie breaking changes a trace and can change work substantially without changing the applicable optimal-cost theorem.

## 26. Solve examination questions systematically

First identify whether the diagram is a physical state graph or an already unfolded search tree. Write the start, all goal states, edge directions, edge costs and successor order. Then name the algorithm variant, duplicate rule and goal-test timing. Make a frontier table after every expansion. For UCS, keep a separate best-cost table and cross out stale records without counting them as expansions.

For complexity questions, define $b$, $d$, $m$, $L$, $C^*$ and $\varepsilon$ before using them. Check whether the root, boundary nodes and generated children beyond the goal layer are counted. Separate exact finite sums from asymptotic approximations. If $b=1$, use the chain formula rather than dividing by $b-1$. If no positive lower cost bound exists, a depth bound derived from $C^*/\varepsilon$ is unavailable.

For true/false claims, seek the smallest counterexample. Two routes to one goal disprove weighted BFS optimality. Three vertices disprove UCS with a negative suffix. A converging deep and shallow path exposes DLS visited-bit errors. An infinite acyclic chain defeats the claim that cycle checking makes DFS complete. These are proof tools, not isolated facts to memorize.

## 27. Chapter summary

Search algorithms differ in frontier ordering and in what information makes one path dominate another. BFS establishes minimum depth by layer order. DFS controls the active frontier by committing to one branch, but must be qualified by graph size and duplicate policy. DLS must distinguish an exhausted search from a truncated one. IDS recovers minimum-depth completeness with repeated finite searches; its low overhead depends on rapidly growing layers.

UCS establishes optimal accumulated cost using relaxation, a valid minimum-cost goal removal and nonnegative suffixes. Its termination on infinite problems depends on cost-sublevel structure, not merely on every individual edge being positive. Bidirectional methods need real predecessor access and a certified stopping rule. Across all methods, a sufficient state key and declared counting conventions are essential. The final worked bank turns these principles into exact traces, formulas, proofs and counterexamples.

## 28. Worked mathematical and conceptual problems

All solutions explain the modelling choice, calculation and reason a tempting alternative fails. University-inspired problems are independently reconstructed and attributed. Authentic examination adaptations are distinguished from original problems and identify their original page. Answers are independently derived unless an official key has actually been verified.

<!-- INCLUDE: problems -->

## 29. Final examination rules and retrieval notes

These notes are complete conditional statements. Read the named assumption before applying the conclusion; use the linked solved problem to reconstruct the argument when a condition changes.

<!-- INCLUDE: review -->

## 30. Editable search laboratory

Change the directed graph, start, goal, algorithm and depth limit. Edge-list order specifies successor order. BFS and DFS use discovery on insertion; UCS uses improving costs and a stable priority tie. DLS and IDS use current-path cycle checking. The goal is tested on selection and is not counted as an expansion. The graph is intentionally small enough to keep every frontier change readable. A safety cap reports truncation rather than inventing failure or success.

<!-- LAB: search -->

## 31. References and scope of verification

- UC Berkeley, CS188 staff textbook, [Section 1.3: Uninformed Search](https://inst.eecs.berkeley.edu/~cs188/textbook/search/uninformed.html).
- Carnegie Mellon, 15-281, Spring 2023, Stephanie Rosenthal; staff [Search Notes](https://www.cs.cmu.edu/~15281/coursenotes/search/) and [Lecture 2 activity solutions](https://www.cs.cmu.edu/~15281-s23/activities/15281_S23_Lecture_2_Activity_Solutions.pdf).
- MIT, 6.034, Spring 2005, Leslie Kaelbling and Tomas Lozano-Perez; [Search I written notes, Sections 2.1–2.3](https://ocw.mit.edu/courses/6-034-artificial-intelligence-spring-2005/921a7a2eca07e1721e8c1cac1813f4c6_ch2_search1.pdf).
- University of Edinburgh, INF2D; [Lecture 3: Search Strategies](https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/inf2d/2025/inf2dlectureslides-03searchstrategies_0.pdf). The PDF does not identify an individual lecturer.
- Stanford, CS221, Summer 2012–2013, Chris Piech; [Search assignment by Chris Piech and Percy Liang](https://web.stanford.edu/~cpiech/cs221/homework/pset/search.html), supplementary application source.
- [Documented source comparison](../reviews/i_uninformed-sources.html) and [mathematical, visual and retention audit](../reviews/i_uninformed-quality.html).

The instruction, examples, diagrams and solutions are independently written. A bounded accessible source pool, checked examination pages and explicit finite-model tests provide inspectable evidence. They do not certify every course worldwide, literal universal coverage, or guaranteed performance on every unseen question. Informed search, games and advanced planning remain separate chapters rather than unexplained additions to this one.
