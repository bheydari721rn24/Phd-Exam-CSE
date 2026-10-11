## Complete induction rules, formulas and examination traps

### 1. Define the entire predicate and its first valid index

An assertion includes its integer domain, formula and quantification over relevant objects. “Every full binary tree with $n$ internal nodes” permits an arbitrary subtree in the step; a statement about one fixed tree does not. If a denominator is $n-1$, inspect whether $n=1$ is excluded before selecting a base. A convenient base outside the target domain does not automatically anchor the required interval.

### 2. The induction hypothesis is conditional and local

Fix arbitrary eligible $k$, temporarily assume $P(k)$ and derive exactly $P(k+1)$. This does not assume the global theorem or the next assertion. After a separately proved base and universal step, invoke induction for the global conclusion. A valid step with an everywhere-false antecedent supplies no true starting fact; a true base without a valid step supplies one case only.

### 3. Write the successor target before manipulating it

For $F(n)=n(n+1)(2n+1)/6$, the next target is $(n+1)(n+2)(2n+3)/6$. Matching only its leading term is insufficient. Separate the old prefix from the new summand, use the hypothesis on that prefix and verify the final factors. Backward algebra is valid only when every reversed operation is justified as an equivalence within the stated domain.

### 4. Initial value plus correct difference certifies an exact sum

If $F(a)$ equals the starting sum and $F(n+1)-F(n)=f(n+1)$ at every later index, induction proves $F(n)=\sum_{k=a}^{n}f(k)$. Adding a constant to $F$ preserves every difference but can violate the base. A proposed formula's constant and lower-order terms therefore matter in exact examination answers even when they do not change an asymptotic order.

### 5. Keep both endpoints when shifting a sum

For $1\le m\le n$, $\sum_{k=m}^{n}k2^{k-1}=(n-1)2^n-(m-2)2^{m-1}$. For reciprocal products, $\sum_{k=m}^{n}1/[k(k+1)]=1/m-1/(n+1)$. Removing the first term changes the starting boundary; moving the upper limit changes the final one. Count included terms before substituting a familiar identity.

### 6. Weighted and unweighted powers have different identities

$\sum_{k=1}^{n}2^{k-1}=2^n-1$, whereas $\sum_{k=1}^{n}k2^{k-1}=(n-1)2^n+1$. The first increment is $2^n$ and the second is $(n+1)2^n$. The extra index weight cannot be treated as a uniform multiplier on all summands. Derive the increment if a multiple-choice option resembles a familiar formula.

### 7. The square sum includes quadratic and linear terms

$\sum_{k=1}^{n}k^2=n(n+1)(2n+1)/6=n^3/3+n^2/2+n/6$. Its successor adds $(n+1)^2$. Neither $n^3$ nor its leading term $n^3/3$ is the exact sum. All common candidate expressions may agree at one small index; their factored differences distinguish the true universal identity.

### 8. Telescope finite sums before taking a limit

The positive term $1/[k(k+1)]$ is nonzero; its components $1/k-1/(k+1)$ cancel across adjacent terms. The finite result is $n/(n+1)$ and the infinite limit is one. The two component harmonic series diverge, so their unspecified infinite difference is not a legitimate calculation. Matched finite cutoffs preserve the endpoints and justify the limit.

### 9. Marked-subset double counts require exact object definitions

$\sum_{k=r}^{N}\binom Nk\binom kr=\binom Nr2^{N-r}$ counts an unordered marked $r$-subset inside a subset. Choose the marks first and force them present; only unmarked elements are optional. Ordering the marks would multiply by $r!$, and freeing their membership would count invalid objects. Check $r=0$ and $r=N$ against their actual constructions.

### 10. Square weights separate repeated and distinct marks

$k^2=k(k-1)+k$ splits two ordered markings into distinct and repeated members. Hence $\sum_k k^2\binom Nk=N(N-1)2^{N-2}+N2^{N-1}$ for $N\ge2$. The repeated case forces one member present; the distinct case forces two. Apply each free-membership factor to the appropriate object rather than using one uniform factor for both cases.

### 11. Pascal induction retains endpoint coefficients

Use $\binom nk=0$ outside $0\le k\le n$ when shifting sums. This makes $\binom{n+1}{k}=\binom nk+\binom n{k-1}$ valid at the boundaries and prevents losing the constant or highest-power term. The binomial theorem collects commuting variables; for noncommuting matrices, reordering mixed products can invalidate the usual coefficient grouping.

### 12. A prefix recurrence can double after an exceptional seed

If $a_0=c$ and $a_n=b+\sum_{j=0}^{n-1}a_j$ for $n\ge1$, compute $a_1=b+c$ first. The derived $a_{n+1}=2a_n$ starts at $n\ge1$, giving $a_n=(b+c)2^{n-1}$ there. It does not overwrite $a_0=c$. An incorrect seed propagates through every later doubling; extra algebra does not repair that boundary mistake.

### 13. Formal generating series and analytic sums have different requirements

The prefix recurrence yields $A(x)=[c+(b-c)x]/(1-2x)$ as a formal identity. Its coefficients determine the sequence without choosing a numerical $x$. An analytic geometric interpretation with nonzero tail requires $|x|<1/2$. Comparing the coefficient of $x$ can determine a proposed parameter immediately, but reconstructing the original recurrence verifies the entire sequence.

### 14. A step of size d preserves residues

The rule $P(k)\Rightarrow P(k+d)$ leaves $k\bmod d$ unchanged. Consecutive bases $n_0,\ldots,n_0+d-1$ reach every index at least $n_0$. Missing a class admits a countermodel with $P$ true only on supplied classes. A statement that the rule establishes only even indices is about proof reachability; it does not assert that the underlying property is false at odd indices.

### 15. Multiple predecessor terms need sufficient seeds

The recurrence $a_n=2a_{n-1}-a_{n-2}$ requires both $a_0$ and $a_1$. Strong induction provides earlier eligible assertions only after those base obligations are established. A candidate quadratic may match both seeds but still fail at the next term; verify its recurrence as well as its boundary data. A step of size two is a different dependency structure from a two-predecessor recurrence.

### 16. Strong induction checks every reduced index

In a theorem beginning at $n_0$, the hypothesis covers $n_0\le j<n$, not arbitrary smaller integers. A reduction to $n-4$ is usable only when $n-4\ge n_0$. For four-and-five-unit representations, this requires four separate starting amounts. In a composite-number proof, both nontrivial factors are between two and the current number, making them eligible for the prime-product hypothesis.

### 17. Strong and ordinary induction prove the same integer principles

Set $Q(k)=\bigwedge_{j=n_0}^{k}P(j)$. A valid strong step extends this conjunction by $P(k+1)$, so ordinary induction on $Q$ proves every $P$. This transformation explains the equivalence; the word “strong” does not authorize additional premises, omitted bases or future cases. It describes a more convenient hypothesis, not a guarantee of stronger conclusions.

### 18. Minimal counterexamples require a well-founded measure

A nonempty subset of nonnegative integers has a least member. A nonempty real interval such as $(0,1)$ does not. State why the hypothetical bad set is nonempty, why its measure is eligible and why the reduction strictly decreases that measure. For recursive algorithms, a merely nonincreasing measure can permit an infinite cycle; strict decrease is required to invoke the smaller-instance hypothesis.

### 19. Strengthen inequalities with proved slack

For $T_n=\sum_{k=1}^{n}1/k^2$, the weak hypothesis $T_n<2$ cannot absorb the next positive summand. Prove $T_n\le2-1/n$ instead. The remaining slack after the next term is $1/[n(n+1)^2]>0$, closing the step and then implying the desired strict bound. A stronger assertion is useful only if its own base and transition are actually proved.

### 20. Strict thresholds need a failing lower index

$2^n>n^2$ is true at one, fails or is equal at two through four, and holds on the entire tail from five. The inductive slack is $2n^2-(n+1)^2=n^2-2n-1>0$ on that tail. Failure at four establishes the smallest threshold. A larger sufficient threshold is an incorrect answer when the question asks for the smallest one.

### 21. Divisibility induction constructs an integer quotient

For $8\mid5^{2n}-1$, the successor is $25(5^{2n}-1)+24$. With the hypothesis $5^{2n}-1=8t$, it becomes $8(25t+3)$, whose quotient is integer. Replacing a congruence by equality or forgetting the added correction is invalid. The same expression fails divisibility by sixteen at $n=1$, so a proven modulus cannot be increased without a new argument.

### 22. Residue cycles use complete recurrence states and exact phase

For a second-order parity recurrence, retain the adjacent pair. The rule $(u,v)\mapsto(v,u+v\bmod2)$ cycles the three nonzero states and fixes $(0,0)$. Once a state repeats, determinism and induction prove the future cycle. The given initial indices fix the phase. Count multiples of a period in an inclusive range using $\lfloor R/d\rfloor-\lfloor(L-1)/d\rfloor$, adjusting for any phase shift.

### 23. Tree node, leaf and edge counts are distinct

In a finite full $m$-ary tree, $E=mI$, $N=E+1=mI+1$ and $L=N-I=(m-1)I+1$. The base is one root leaf, not an empty tree. A binary tree uses $m=2$; a ternary tree uses $m=3$. A candidate may count a different valid quantity and still be wrong for the requested one, so label each quantity before substituting numbers.

### 24. Fullness does not imply a balanced height

A full binary comb with $n$ internal nodes has height $n$, while a perfect full tree has equal leaf depth and much smaller height for the same comparable size. Both obey $N=2n+1$. For $n\ge1$, $\lceil\log_2(n+1)\rceil\le h\le n$. Node accounting supplies no logarithmic algorithmic bound without an additional balance or shape hypothesis.

### 25. Child-count changes have an exact accounting correction

For variable internal child counts $d(v)$, $L=1+\sum_v(d(v)-1)$. A one-child chain has every summand zero and only one leaf. For an at-most-three-child tree, $L\le2I+1$, with equality only when every internal child count is three. This bound follows by replacing each summand with its maximum, not by applying the full-tree equality unchanged.

### 26. Leaf weights are a mass invariant, not an unweighted count

The weight of a leaf at root-relative depth $d$ is $2^{-d}$. One child receives half the parent mass; two children receive the full mass in separate halves. Thus the leaf-weight sum is at most one. A finite full binary tree has equality even with unequal leaf depths; an infinite full tree need not. The root-only tree gives equality and refutes any universally strict bound.

### 27. A recursive cost recurrence still needs a model proof

The exact solution of $H_n=2H_{n-1}+1,H_0=0$ is $2^n-1$. For standard three-peg Hanoi, legal construction proves an upper bound; the transfers before the first and after the last largest-disk move prove the matching lower bound. Peg assignments must be universally covered by the recursive hypothesis. Four pegs or altered move rules invalidate an unexamined reuse of this optimality argument.

### 28. Structural induction quantifies over every child configuration

For deficient-board tiling, the hypothesis must permit any missing cell, because an arbitrary quadrant can contain the original gap. The central L creates one covered cell in each other quadrant, making four eligible smaller problems. Area divisibility by three is only necessary; the disjoint constructor proves sufficiency. For trees, include root-leaf children even when the main numerical parameter question starts at positive internal counts.

### 29. Test the earliest usable transition for hidden failures

In the horse-color argument, the two size-one subgroups of a two-horse group do not overlap, so the first transition fails despite a valid one-horse base. Later overlap cannot bridge that missing step. Check the first predecessor index, a zero denominator, an omitted parity chain and a missing base before accepting a superficially familiar induction format.

### 30. Coupled and descending inductions close every dependency

For linked assertions $P(n),Q(n)$, prove both bases and both successor conclusions by inducting on their conjunction. For a finite downward interval $L\le n\le U$, start at $U$ and prove $P(k+1)\Rightarrow P(k)$ through $L$. The substitution $m=U-n$ converts it to ordinary induction. One upper base cannot cover all arbitrarily large indices by downward steps.
