## Mathematical constructions connecting induction to the questions

### 1. Certify an exact sum by its initial value and first difference

For a finite sum $S_n=\sum_{k=a}^{n}f(k)$, the defining successor is $S_{n+1}-S_n=f(n+1)$. A candidate $F(n)$ is proved by checking the same successor difference and one initial value. Indeed, $D_n=S_n-F(n)$ then has $D_{n+1}=D_n$; a zero initial difference forces every later difference to be zero by induction. Equal increments alone leave an undetermined additive constant.

For $F(n)=(n-1)2^n+1$, subtraction gives $(n+1)2^n$, matching the weighted summand. For $G(n)=n(n+1)(2n+1)/6$, it gives $(n+1)^2$. For $T(n)=n/(n+1)$, it gives $1/[(n+1)(n+2)]$. These are three different successor calculations; a generic statement that “the next case follows” supplies none of them. Once the exact identity is established, a sum from $m$ through $n$ is obtained by subtracting the prefix through $m-1$. Retain both resulting endpoints.

### 2. Marked subset identities and their inductive coefficient transition

For a universe of size $N$ and $0\le r\le N$, count a subset with an unordered marked $r$-subset. By total subset size, the count is $\sum_{k=r}^{N}\binom Nk\binom kr$. By selecting the marks first, it is $\binom Nr2^{N-r}$: the marked elements must be present and each of the others is optional. Algebraically, factorial cancellation proves $\binom Nk\binom kr=\binom Nr\binom{N-r}{k-r}$. This is a bijective double count, not an approximation or a rule permitting random coefficient multiplication.

For ordered distinct marks, use falling-factor weights instead. The one-mark count is $\sum_k k\binom Nk=N2^{N-1}$ for $N\ge1$. The two-distinct-ordered-mark count is $\sum_k k(k-1)\binom Nk=N(N-1)2^{N-2}$ for $N\ge2$. Splitting $k^2=k(k-1)+k$ therefore gives the square-weight count $N(N+1)2^{N-2}$ on $N\ge2$. Evaluate the smaller universes directly; do not interpret an optional subset of negative size.

Pascal's identity connects these constructions to induction. Partition subsets by whether a newly added element belongs to them, giving $\binom{N+1}{k}=\binom Nk+\binom N{k-1}$. With out-of-range coefficients zero, the one-mark weighted sum satisfies $T_{N+1}=2T_N+2^N$. A base and that coefficient-derived transition prove its formula inductively. When an exact power weight is decomposed into falling factors, each factor counts a distinct marking pattern; repeated marks need their own contribution.

### 3. A prefix recurrence retains a separate first step

Let $a_0=c$ and $a_n=b+\sum_{j=0}^{n-1}a_j$ for $n\ge1$. The original equation gives $a_1=b+c$. Subtracting equations at positive neighboring indices gives $a_{n+1}=2a_n$ for $n\ge1$, because their forcing constants and shared prefix terms cancel. Consequently

$$a_n=(b+c)2^{n-1}\quad(n\ge1),\qquad a_0=c.$$

The formula is piecewise in its domain even when its positive part looks simple. Setting $n=0$ in that part gives $(b+c)/2$, which need not equal $c$. The full generating series is

$$A(x)=c+\frac{(b+c)x}{1-2x}=\frac{c+(b-c)x}{1-2x}.$$

As a formal series, $1/(1-2x)$ is defined by its geometric coefficients and no analytic convergence assertion is needed. As an analytic series with nonzero geometric tail, use $|x|<1/2$. The authentic recurrence has $(b,c)=(0,1)$; the original positive-prefix question has $(b,c)=(2,1)$. The shared multiplier two does not make their seeds or numerators equal.

### 4. Step size, predecessor range and proof reachability

With a transition $P(k)\Rightarrow P(k+d)$ for every $k\ge n_0$ and positive integer $d$, the index residue modulo $d$ is invariant. The consecutive bases $n_0,\ldots,n_0+d-1$ suffice: each target has a unique representation $n=n_0+r+qd$ with $0\le r<d$ and $q\ge0$. Induction on $q$ reaches it from its corresponding base. If a residue class has no base and no additional connecting rule, define $P$ true exactly on the represented residues. This makes every provided rule and base true while leaving the missing class false, proving the logical insufficiency.

A two-predecessor recurrence differs from a step of size two. The relation $a_n=2a_{n-1}-a_{n-2}$ uses consecutive previous values and needs two seeds. The rule $P(k)\Rightarrow P(k+2)$ propagates independent parity chains. Strong induction may conveniently collect predecessors, but it cannot establish an unavailable starting assertion or use an index outside the theorem's domain.

### 5. Recurrence residues form a deterministic state machine

If only parity is requested for an integer recurrence, project each coefficient and constant modulo two before calculating large terms. For $a_n=3a_{n-1}+5a_{n-2}+4$, the projected rule is $a_n\equiv a_{n-1}+a_{n-2}\pmod2$. The sufficient state is the adjacent pair, not one isolated parity. Its transition is $(u,v)\mapsto(v,u+v\bmod2)$.

| Current pair | Next pair | Behaviour |
|---|---|---|
| $(0,0)$ | $(0,0)$ | Fixed even state |
| $(1,1)$ | $(1,0)$ | First nonzero-cycle state |
| $(1,0)$ | $(0,1)$ | Second nonzero-cycle state |
| $(0,1)$ | $(1,1)$ | Return to the same state |

Once a complete state returns, the deterministic transition forces every future state to repeat, proved by induction on the number of advances. A finite-state recurrence need not repeat from its initial state immediately: in general it can have a transient prefix before its eventual cycle. Here the displayed transition proves the exact cycle without a transient for the stated seed. The actual initial indices locate the phase; a period without a phase cannot answer which positions are even.

### 6. Structural induction tracks distinct tree quantities

For a finite rooted tree, every nonroot node has one parent, so $E=N-1$. If every internal node has exactly $m$ children, also $E=mI$. With $N=I+L$, derive $L=(m-1)I+1$ and $N=mI+1$. Each symbol counts a different object; substituting the leaf count for the total or the edge count for the leaves is a semantic error, even when some small instances coincide.

The root-leaf base has $(I,L,N,E)=(0,1,1,0)$. Expanding a leaf into an internal node with $m$ leaf children adds one to $I$, $m-1$ to $L$, $m$ to $N$ and $m$ to $E$, preserving both identities. Alternatively, combine $m$ smaller subtree hypotheses with a new root. Fullness specifies child counts; it does not enforce balance or equal leaf depths. For variable child counts, the exact repair is $L=1+\sum_{v\ \mathrm{internal}}(d(v)-1)$.

For binary leaf weights $2^{-d}$, structural induction tracks mass instead of vertices. A root leaf has mass one. One child gives half its subtree mass; two children give half the sum of their masses. Thus every finite binary tree has leaf-weight sum at most one, with equality exactly for full trees. This is an allocation argument and can also express the Kraft bound for finite prefix-free binary words. The equality characterization needs its finite-tree hypothesis.

### 7. A solved recurrence is distinct from a proved optimal model

The supplied recurrence $H_0=0,H_n=2H_{n-1}+1$ is solved by the shift $B_n=H_n+1$, yielding $B_n=2B_{n-1}$ and hence $H_n=2^n-1$. For the standard three-peg Hanoi puzzle, the construction moves the smaller stack to the auxiliary peg, moves the largest disk once, then moves the smaller stack to target. Induction on the disk count must cover all distinct peg assignments so both recursive calls are within the hypothesis.

To prove minimality, analyze an arbitrary legal successful procedure. Before its first largest-disk move, the smaller stack has been transferred to the only third peg, costing at least $H_{n-1}$. After its last largest-disk move to target, the smaller stack must be transferred from the remaining peg to target, costing at least another $H_{n-1}$. These separate time intervals and at least one largest-disk move give $2H_{n-1}+1$ as a lower bound. The construction achieves that bound. Counting one specific procedure supplies only an upper bound until this arbitrary-procedure argument is established. Four pegs or different movement rules require a different lower-bound and recurrence analysis.
