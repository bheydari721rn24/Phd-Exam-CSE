## Deeper constructions connecting certificates, formulas and implementations

### 1. The least forward closure and the greatest safe closure answer different questions

For a finite state set $S$, initial set $I$, transition relation $T$ and permitted region $Q$, define $\operatorname{Post}(X)=\{v:\exists u\in X,(u,v)\in T\}$. Iterating $R_0=I$ and $R_{k+1}=R_k\cup\operatorname{Post}(R_k)$ adds precisely states reachable in at most $k+1$ transitions. A strict addition increases cardinality, so at most $|S\setminus I|$ strict additions occur. Stabilization gives the least closed set containing $I$.

For universal safety, start instead from $K_0=Q$ and remove every state that has any successor outside the current candidate:
$$K_{k+1}=\{u\in K_k:\operatorname{Post}(\{u\})\subseteq K_k\}.$$
This decreasing sequence also stabilizes. Its final $K$ is closed and contained in $Q$. Every closed subset $J$ of $Q$ remains inside each $K_k$: if $u\in J$, every successor stays in $J$ and hence in $K_k$, so $u$ cannot be removed. Thus $K$ is the greatest closed subset of $Q$. Universal safety from $I$ holds exactly when $I\subseteq K$. One implication applies closure to all prefixes; the other uses the safe reachable set itself as a closed subset of $Q$.

An edge entering a closed set does not threaten it. An edge leaving it does. Dead ends stay in the safe closure when they belong to $Q$, because a universal condition over no successors is true. This expresses safety, not successful completion. A cycle entirely inside $Q$ may remain in $K$ and still allow infinite execution. A diagram must distinguish the forward frontier from backward deletion rather than color both computations as the same process.

For finite termination, restrict to $R$. A reachable cycle produces an infinite execution by repeating the cycle. Conversely an infinite execution in a finite graph revisits a state and contains a directed cycle. If the reachable subgraph is acyclic, define $h(u)=0$ at a sink and $h(u)=1+\max_{u\to v}h(v)$ otherwise. Reverse topological evaluation constructs this natural rank. Every actual edge lowers it by at least one. Failure of another proposed rank does not invalidate this independently constructed certificate.

### 2. Solve additive and affine preservation equations from the transition itself

If a state vector changes by one of the allowed vectors $v_j$, a linear conserved expression $w^Tx$ must satisfy $w^Tv_j=0$ for every generator. A modular conserved expression requires $w^Tv_j\equiv0\pmod m$. These are equations to solve, not patterns to guess from a favorable trace. Guard restrictions can make some states irrelevant to actual reachability, but preservation must still be proved over the declared certificate domain.

For generators $(2,1)$ and $(-1,2)$, the real linear equations $2w_1+w_2=0$ and $-w_1+2w_2=0$ have only the zero solution, because the determinant is five. There is no nonzero exact linear conservation law of those two coordinates. Modulo five, however, $w=(1,3)$ solves both equations. This explains why a residue invariant succeeds where an exact weighted sum cannot.

Solving for signed generator counts gives $p=(2x+y)/5$, $q=(-x+2y)/5$. An unrestricted integer target is reachable exactly when these coefficients are integers. This yields the converse to the modular obstruction. If backward moves are forbidden, coefficients must additionally be nonnegative; if states must remain nonnegative, the order of the moves must also respect every intermediate guard. A lattice membership calculation alone no longer proves the guarded path exists.

For an affine update $x'=Mx+c$, a candidate affine quantity $F(x)=w^Tx+c_0$ is conserved when $w^TM=w^T$ and $w^Tc=0$. The constant $c_0$ does not cancel a nonzero additive drift. Other transformations can linearize the update: if $d'=2d+1$, then $u=d+1$ satisfies $u'=2u$. This is geometric growth, not conservation. Under $a'=2a+1,b'=2b$ with $b\ne0$, the ratio $(a+1)/b$ is conserved because both numerator and denominator double. Its denominator condition and arithmetic model are part of the theorem.

### 3. Integer ranks, lexicographic ranks and exact cost accounting

A nonnegative integer rank that strictly decreases gives an upper bound on ranked transitions. Exact unit decrease plus a zero final rank gives equality of execution length and initial rank, provided every positive-rank state has an enabled terminating step. Without that progress condition, an execution can deadlock while the rank is still positive.

For a reset process $j>0:(i,j)\to(i,j-1)$ and $j=0,i>0:(i,0)\to(i-1,B)$, the weight $B+1$ gives rank $(B+1)i+j$. Both transitions reduce it by exactly one. By contrast, if the reset value is arbitrary and unbounded, no fixed finite weight covers all resets. Lexicographic $(i,j)$ still decreases: primary reduction permits any finite secondary reset. The natural lexicographic order has no infinite descending chain, but paths from one fixed start may have no common finite length bound.

This distinction can be sharpened for finite branching. In a finitely branching execution tree, unbounded finite path lengths from one fixed root would give an infinite branch by the finite-branching tree principle. Thus universal termination there implies a finite maximum path length from that root. The arbitrary-reset example has infinitely many successors at a reset and escapes that implication. This observation does not give a computable global bound across all inputs; it concerns one rooted execution tree.

For a two-phase process $x>0:(x,y)\to(x-1,y+B)$ followed by $x=0,y>0:(0,y)\to(0,y-1)$, rank $(B+1)x+y$ gives the exact remaining cost. The primary decrement creates $B$ later decrements plus the primary step itself. Interpreting its weight as prepaid work makes the formula intuitive and avoids the false requirement that every coordinate decrease separately.

### 4. A loop-head equation and weakest-precondition substitution must use the same checkpoint

For assignment `x = E`, a desired postcondition $P(x)$ requires the old-state condition $P(E)$, including defined evaluation of $E$. For a sequence of assignments, substitute backwards through the sequence. For `x = y; y = x`, a final condition $x=y$ is valid, but the final pair is $(y_{old},y_{old})$, not an exchange. Parallel assignment has another transition.

Consider repeated `s += i; i += 1` starting at $(s,i)=(0,2)$. At the loop head after $t$ completed bodies, $i=t+2$ and $s=t(t+3)/2=i(i-1)/2-1$. Immediately after the addition but before the increment, the same old index has $s=i(i+1)/2-1$. These two valid equations refer to different program locations. Adding a control-location tag to the state makes both assertions precise.

For a sum over arbitrary integer array values, an exact prefix equation supplies correctness even when the sum rises and falls. The rank is remaining indices, not the accumulated value. For Horner evaluation with ascending coefficients, scan backwards and interpret the accumulated value as a shifted suffix polynomial. The exit index supplies the final shift. For merging, sortedness must be joined with multiset preservation and valid exhaustion guards. These specifications retain the relationship between changing state and original input instead of using unrelated numeric bounds.

### 5. Constructor counting and binary leaf mass are related but different identities

In a finite rooted tree, every vertex except the root has one parent, giving $E=V-1$. Counting edges at their parents gives $E=\sum_{v\text{ internal}}d(v)$. With $I$ internal vertices and $L$ ordinary leaves, subtraction yields
$$L=1+\sum_{v\text{ internal}}(d(v)-1).$$
Binary nodes contribute one net leaf, ternary nodes contribute two, and unary nodes contribute zero. A full $k$-ary tree therefore has $L=(k-1)I+1$. Mixed arities require the actual sum. A forest changes the constant to its component count; a graph with cycles does not satisfy the tree edge identity.

Binary leaf mass instead assigns weight $2^{-d}$ at depth $d$, with root depth zero. A node with two children distributes all its weight; a unary node sends half and loses half into the absent branch. Therefore the exact deficit is
$$1-\sum_{\ell\text{ leaf}}2^{-d(\ell)}=\sum_{u\text{ unary}}2^{-d(u)-1}.$$
One proof expands the root's unit mass through every internal node: all present-child transfers cancel internally, leaving only leaf allocations and missing-child losses. Finiteness ensures this expansion is a finite sum. Every loss is positive, so equality of leaf mass to one holds exactly when there are no unary nodes. This criterion needs neither equal leaf depths nor a perfect tree.

An empty tree requires a separate definition, because it has no root to receive unit mass. In Cambridge's empty-or-node representation, external empty positions are constructor bases, not ordinary data leaves. A single stored root has two external positions and one ordinary leaf. Height bounds must similarly state whether height zero means an empty tree or a data-bearing leaf.

### 6. Accumulator specifications determine both proof strength and sharing behavior

For finite linked lists, define append by its empty and cons cases. Prove totality on the first list, then right identity, length additivity and associativity. A reversed-accumulator helper satisfies $\operatorname{revAcc}(L,A)=\operatorname{rev}(L)\Vert A$ for every accumulator $A$. The quantifier belongs inside the induction predicate: the recursive call changes $A$, so an empty-only hypothesis is unusable.

At a cons case, apply the hypothesis to $[x]\Vert A$, then use proved associativity to regroup $\operatorname{rev}(L)\Vert ([x]\Vert A)$ as $(\operatorname{rev}(L)\Vert [x])\Vert A$. Reordering would require list commutativity, which is false. The suffix $A$ is shared by the linked-list construction; it need not be copied merely because its length contributes to the resulting list.

For leaf-tree flattening, the right helper is evaluated first to construct a suffix, then the left helper prepends its result. The specification $\operatorname{flatAcc}(T,A)=\operatorname{flatten}(T)\Vert A$ needs both subtree hypotheses at their actual accumulator arguments. Totality justifies that the intermediate suffix is a finite value.

Under the declared linked-list cost model, an append copies its first argument once. Naive reversal allocates $n(n+1)/2$ cons cells over its whole execution: one singleton and the copied reversed tail per element. Accumulator reversal allocates $n$ new cells. Total allocation is not peak live space. Python slicing copies arrays and changes these costs; tail recursion saves auxiliary stack only when the evaluator actually eliminates tail calls.

### 7. A finite residue state can answer a huge-index question rigorously

Reducing a recurrence modulo $m$ gives a deterministic map on a finite tuple of residues when enough consecutive terms are retained. A recurrence of order $r$ has at most $m^r$ residue states. Pigeonhole guarantees that a trajectory eventually repeats, giving a transient followed by a cycle. Pure periodicity from the initial state requires that the first repeated state is that initial state, or another independently justified invertibility argument.

For $a_k=3a_{k-1}+5a_{k-2}+4$ modulo two, the consecutive-pair transition is $F(u,v)=(v,u+v\bmod2)$. It is invertible: $F^{-1}(v,w)=(w-v\bmod2,v)$. The zero pair is a fixed state; the three nonzero pairs form a cycle. Starting from two odds follows $(1,1),(1,0),(0,1)$ and returns. The phase of the given initial indices determines which subsequent indices are even; it is not enough to remember that the period is three.

To count terms with a given residue in an inclusive interval, count complete periods and inspect both boundary fragments. If qualifying indices are multiples of $q$, the number from $L$ through $U$ is $\lfloor U/q\rfloor-\lfloor(L-1)/q\rfloor$. For a more general periodic residue set, sum this count over its disjoint qualifying phase classes. No large integer recurrence terms need be constructed.

### 8. Structural recursion can be terminating while an object-level definition is ambiguous

An inductive datatype with disjoint constructors supplies unique top-level decomposition; a function defined by matching those constructors is well defined once recursive calls are legitimate. A generated mathematical set can have multiple derivations. Assigning values along derivations then defines a function on derivation trees, but not necessarily on the resulting object.

If the empty string is a base with cost zero and concatenation adds one plus both costs, the derivation concatenating two empty strings gives the same empty string cost one. This is a contradiction for an object-level cost, even though every finite derivation is evaluated by a terminating routine. One repair records constructor tags and makes the derivation itself the input. Another chooses an object measure, such as length, whose defining equations agree across derivations.

Mutually recursive routines require a joint specification or a phase rank. Nested recursion requires the inner call to terminate and return an output in the outer call's domain. In the standard Ackermann equations, lexicographic argument order supports an outer call with a huge second coordinate because its first coordinate is smaller. Fixing the base equations is essential: MIT's alternative and the standard function have different values. A mathematical totality proof supplies neither a practical time bound nor a guarantee that a finite implementation stack can execute every natural input.
