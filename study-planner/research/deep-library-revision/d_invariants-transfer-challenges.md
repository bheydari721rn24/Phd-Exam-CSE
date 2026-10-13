## Ten solved synthesis challenges

### Challenge 1. Compare forward reachability, backward safety and two ranks

**Question.** States are $0,1,2,3,4,5$. The initial state is zero. Edges are $0\to1,1\to2,2\to3,4\to2,5\to5$. Let $Q=\{0,1,2,4,5\}$. Compute the reachable set, the greatest safe closed subset, and a rank proving termination from zero. Explain what changes when state five becomes an additional initial state.

**Solution.** Forward layers are $\{0\}$, $\{0,1\}$, $\{0,1,2\}$ and $\{0,1,2,3\}$, which then stabilize. The shortest safety violation is the three-edge path $0,1,2,3$. Backward removal starts from $Q$: remove two because it points to excluded three, then remove one and four because they point to two, then remove zero because it points to one. State five remains, so the greatest safe closed subset is $\{5\}$.

The reachable chain admits ranks $3,2,1,0$ on states zero through three. They decrease by one at every reachable edge, proving every execution from zero terminates despite eventual safety failure. A constant proposed rank would fail without changing that conclusion. If five becomes initial, its self-loop is a reachable cycle and creates an infinite execution. That state is safe under $Q$ but nonterminating. Thus neither safety nor termination implies the other; forward and backward algorithms certify different quantified claims.

### Challenge 2. Prove an additive residue criterion and audit its domain

**Question.** Moves add or subtract $(2,1)$ and $(-1,2)$ on integer pairs. Characterize targets from the origin, and decide $(7,1)$, $(1,0)$ and $(0,5)$. What additional proof would be needed if all intermediate coordinates had to be nonnegative?

**Solution.** The residue $x+3y\pmod5$ changes by plus or minus five and stays zero. Solving $p(2,1)+q(-1,2)=(x,y)$ gives $p=(2x+y)/5$, $q=(-x+2y)/5$. A zero residue makes both integers, supplying a signed-move witness and establishing sufficiency on the unrestricted domain.

For $(7,1)$, the coefficients are $p=3,q=-1$; three first moves and one reverse second move reach it. For $(0,5)$, $p=1,q=2$. For $(1,0)$, $p=2/5,q=-1/5$, so it fails the residue obstruction. Under nonnegative guards, an integer linear combination still proves lattice membership, but a legal order must be exhibited. For $(7,1)$, the path $(0,0),(2,1),(4,2),(6,3),(7,1)$ obeys the guards. For $(0,5)$, the path $(0,0),(2,1),(1,3),(0,5)$ does too. These witnesses solve the particular guarded examples; they do not establish a general guarded converse without further construction.

### Challenge 3. Linearize an affine update and identify a true conservation law

**Question.** Starting from $(a_0,b_0)=(5,1)$, apply $(a,b)\leftarrow(2a+1,2b)$ repeatedly. Find $a_t,b_t,a_t-b_t$. Which of $a-b$, $a+1$, and $(a+1)/b$ is conserved? Compute step four.

**Solution.** Define $c=a+1$. Then $c'=2a+2=2c$ and $b'=2b$. By induction, $c_t=6\cdot2^t$ and $b_t=2^t$, yielding $a_t=6\cdot2^t-1$ and $a_t-b_t=5\cdot2^t-1$. At four, the state is $(95,16)$ and the difference is 79.

The raw difference obeys $d'=2d+1$ and is not conserved. The shifted numerator doubles and is also not conserved. The ratio equals six at every step because $b$ is initially positive and remains so. Exact rational arithmetic makes this statement literal; a machine implementation needs its own overflow or numerical specification. There is no supplied halt guard, and the trace is infinite. A conserved ratio identifies the orbit's algebraic relation without proving termination. The general start $(n,1)$ gives ratio $n+1$ and difference $n2^t-1$.

### Challenge 4. Compare three powering counts under explicit base conventions

**Question.** Compute the multiplication counts at $n=13$ and $n=32$ for: an iterative binary routine always squaring in each positive iteration; the same routine skipping its final unused square; and a recursive routine returning directly at exponents zero and one, with one reused half-result at other calls.

**Solution.** For positive $n$, let $\ell=\lfloor\log_2n\rfloor+1$ and $p=\operatorname{popcount}(n)$. The always-square iteration has $\ell$ squares and $p$ accumulator multiplications, totaling $\ell+p$. Skipping its final square subtracts one, giving $\ell+p-1$. The recursive exponent-one base omits the last square and the last identity-accumulator multiplication: it has $\ell-1$ squares and $p-1$ odd-branch multiplications, totaling $\ell+p-2$.

For thirteen, $\ell=4,p=3$, so the counts are seven, six and five. For thirty-two, $\ell=6,p=1$, so they are seven, six and five again, although their traces have different lengths and bit patterns. At one, the counts are two, one and zero. At zero all three return one with zero multiplications; the positive-input formulas are not substituted into $\log_2 0$. These routines share a value specification and logarithmic call or loop depth, but their exact operator counts differ. Duplicating a recursive half-call would change the work tree and require another count.

### Challenge 5. Derive the exact missing-child mass of an irregular binary tree

**Question.** A binary root has two children. The left child is a leaf; the right child is unary and its only child has two leaf children. Compute the leaf-weight sum, its deficit and the ordinary leaf/internal counts. Explain why the full-binary formula cannot be applied.

**Solution.** The leaf depths are one, three and three. Their total weight is $1/2+1/8+1/8=3/4$. The single unary vertex has depth one, so its missing child discards mass $2^{-2}=1/4$, exactly the deficit. Mass transferred to the existing child then splits into its two depth-three leaves; no other mass is lost.

There are three internal vertices: the root, the unary right child and its binary child. There are three leaves and six total vertices, hence five edges. Parent arities give $2+1+2=5$ edges independently. The full-binary identity would predict four leaves from three internal vertices and is inapplicable because one internal vertex is unary. The general arity identity gives $1+(2-1)+(1-1)+(2-1)=3$ leaves. Unequal depths alone do not imply strict mass loss; a full irregular binary tree still has total leaf mass one. Here the missing child, rather than irregular depth, causes the strict inequality.

### Challenge 6. Count a mixed-arity tree without mistaking edges for leaves

**Question.** A finite nonempty rooted tree has four binary internal vertices, three ternary internal vertices and two unary internal vertices. Find leaves, vertices and edges. Does this determine height?

**Solution.** Parent degrees give $E=4\cdot2+3\cdot3+2\cdot1=19$. The internal count is nine. Since $E=I+L-1$, the leaf count is $L=19-9+1=11$, and total vertices are twenty. The constructor identity independently gives $L=1+4\cdot1+3\cdot2+2\cdot0=11$.

Unary vertices add one internal vertex and one edge without changing the number of leaves. Dropping them would preserve the computed leaf count but reduce total vertices and edges, which are different requested objects. Height is not determined: placing internal vertices on one long branch yields a larger height than distributing branching vertices across several branches. Any claimed height bound must state allowed arity and the root/leaf depth convention. The counts apply to a tree, not a cyclic graph with the same outdegrees; unique parents and acyclicity supplied $E=V-1$.

### Challenge 7. Separate flattening order, helper calls and allocation cost

**Question.** For $T=Node(Leaf(2),Node(Leaf(5),Leaf(7)))$, evaluate the right-first accumulator helper with suffix $[9,10]$. Under immutable linked-list cons and append-by-copying-the-first-argument, count cons allocations for naive flattening and accumulator flattening. Generalize the naive cost to perfect trees with $L=2^h$ leaves.

**Solution.** Evaluate the rightmost leaf first, obtaining $[7,9,10]$; the next leaf prepends five, then the leftmost leaf prepends two. The result is $[2,5,7,9,10]$, with left-to-right tree order followed by the original suffix. There are five helper calls, one for each tree vertex, and three new cons cells, one per leaf. The existing two-cell suffix is shared.

Naive flattening allocates three singleton leaf cells. Its right internal append copies the one-cell list $[5]$, and the root append copies $[2]$, adding two more allocations for five total. It has the same tree-call count but different list-copy work. In a perfect tree of leaf height $h$, each of the $h$ internal levels copies $L/2$ leaf-list cells in aggregate, so total cons allocations are $L+hL/2$. Inductively, $C(1)=1$ and $C(L)=2C(L/2)+L/2$ give this expression. A left-heavy full comb instead copies lists of lengths one through $L-1$, giving $L+L(L-1)/2$ allocations. The accumulator version still allocates $L$ cells for either shape. Shape controls copying; equal returned values and tail-recursive syntax alone do not establish equal costs.

### Challenge 8. Prove totality before comparing two Ackermann conventions

**Question.** Use $A(0,n)=n+1$, $A(m+1,0)=A(m,1)$ and $A(m+1,n+1)=A(m,A(m+1,n))$. Compare $A(1,5)$ with MIT's alternative $B(m,n)=2n$ when $m=0$ or $n\le1$, and $B(m,n)=B(m-1,B(m,n-1))$ otherwise. Why can neither proof require both coordinates to decrease at every call?

**Solution.** Prove termination and natural output jointly by lexicographic induction with the first coordinate primary. An inner call at fixed first coordinate lowers the second; its natural result is a legal outer argument. The outer call lowers the first coordinate, so its second may be arbitrarily larger without invalidating the ordering. Base equations return naturals directly. This argument covers both definitions but does not make their values equal.

For the standard definition, $A(1,0)=A(0,1)=2$ and $A(1,n+1)=A(1,n)+1$, so induction gives $A(1,n)=n+2$ and $A(1,5)=7$. For the alternative, $B(1,1)=2$ and, for $n>1$, $B(1,n)=2B(1,n-1)$; hence $B(1,n)=2^n$ for $n\ge1$, giving $B(1,5)=32$. Its zero boundary is $B(1,0)=0$, not the positive-input formula. The secondary argument in an outer nested call can grow dramatically, defeating an unproved sum rank. Lexicographic totality is a mathematical theorem, not a practical resource guarantee.

### Challenge 9. State Horner's invariant at every backwards checkpoint

**Question.** Evaluate coefficients $[1,-2,3,4]$ in ascending degree order at $x=2$ by `value=0`, scanning indices three through zero and assigning `value=value*x+a[i]`. Give every state, a loop-head invariant and exact operator counts.

**Solution.** The loop-head pairs $(i,value)$ are $(3,0),(2,4),(1,11),(0,20),(-1,41)$. At a head, the value represents the already processed coefficient suffix shifted to degree zero:
$$value=\sum_{j=i+1}^{3}a_jx^{j-i-1}.$$
The initial sum is empty. Multiplication by $x$ raises every processed suffix degree by one; adding $a_i$ inserts its new degree-zero term. Decreasing the index restores the same formula. At exit minus one, it is the whole polynomial. Direct evaluation checks $1-2\cdot2+3\cdot4+4\cdot8=41$.

The index rank $i+1$ decreases from four to zero and justifies valid indices under the guard. The written loop executes four multiplications and four additions, including its initial $0\cdot2+4$. An optimized implementation initializing from the final coefficient would execute three of each but needs a separate empty-input case. Empty coefficients yield zero iterations and result zero. Counting the optimized routine's operators against the given routine would misread the implementation even though both return the same polynomial value.

### Challenge 10. Obtain exact minimum and maximum population from a guarded rank

**Question.** Start with twelve blue and seven red tokens. While blue exceeds red, choose one of $(0,1),(-1,0),(1,2),(-2,-1)$ as the change to $(b,r)$, with removal guards. Find the exact maximal-execution length and the smallest and largest achievable final populations.

**Solution.** Every move lowers $d=b-r$ by one. Initially $d=5$, and an enabled move has $d\ge1$, so the new difference remains nonnegative. Adding one red is always possible while $d>0$, preventing early deadlock. Thus every maximal execution has exactly five steps and ends at equal counts.

Total population starts at nineteen. The four move changes are $+1,-1,+3,-3$, so after five steps it lies between $19-15=4$ and $19+15=34$. Five additions $(1,2)$ give $(17,17)$ and attain the maximum. Five removals $(-2,-1)$ give $(2,2)$ and attain the minimum: before the last removal the pair is $(4,3)$, so every removal guard is satisfied. Earlier states also have enough tokens. This proves both bounds tight.

For this particular five-step start, every combination of the four choices is legal: before step $t+1$ with $0\le t<5$, blue is at least $12-2t\ge4$, red at least $7-t\ge3$, and difference is $5-t>0$. There are therefore $4^5=1024$ legal choice sequences. All sixteen even final populations from four through thirty-four occur; sums of five choices from $\{-3,-1,1,3\}$ attain every odd integer between minus fifteen and fifteen. Final populations are not equally frequent, and a path count is distinct from a state count. The animation must display an actual guarded trace or declared aggregate, rather than infer endpoints from a generic decreasing bar.
