### Solution 1

**Pass a bounded mass down the actual tree.** Assume a finite nonempty rooted binary tree; an internal node may have one or two children, and the root has depth zero. Give the root mass one. Each existing child receives half its parent's mass. An absent child receives nothing. A leaf at depth $d$ receives exactly $2^{-d}$ because its root-to-leaf path contains $d$ halvings.

Let $W(T)$ be the sum of the leaf weights measured relative to the root of $T$. A single leaf has $W(T)=1$. With two subtrees, $W(T)=(W(T_1)+W(T_2))/2\le1$ by structural induction. With just one subtree, $W(T)=W(T_1)/2\le1/2$. These cases cover every finite binary-tree constructor and prove $\alpha\le1$.

Equality is possible: a single root leaf has weight one, and a full finite binary tree preserves all its mass at every branching. Equality is not universal: a root with one leaf child has weight one half. Thus option 1 and the always-strict option 4 each fail on a concrete allowed tree. Option 3 contradicts the proved upper bound; option 2 is correct. In fact equality holds exactly when no internal node is unary: any discarded positive mass remains a strict loss at the root. This is a mass bound on all leaves, not a claim that every leaf has the same depth.

### Solution 2

**Prove the ordering and the returned contents together.** For a finite input of distinct values, choose an actual input order statistic as the median pivot, using a lower or upper median for even size. Empty and singleton inputs are already descending. For a larger input, the greater and smaller partitions are disjoint, together contain all nonpivot values, and are each shorter than the original.

Use strong induction on input length. The hypotheses give descending permutations of both partitions. Every value of the first returned block exceeds the pivot; every value of the last block is below it. Therefore
$$\operatorname{SplitSort}(R)\;\Vert\;[m]\;\Vert\;\operatorname{SplitSort}(L)$$
is descending internally and across both boundaries, and contains exactly the original values. Smaller child lengths also prove termination. For input values $1,2,3,4,5$, the blocks are $[5,4]$, $[3]$, and $[2,1]$, giving $[5,4,3,2,1]$.

Option 4 is correct. The first option invents an ascending branch that the recursion never uses. The random alternative ignores deterministic block inequalities. Ascending order would require joining the smaller block first. Evaluation order of pure recursive calls does not change the prescribed concatenation order. An arithmetic-average median that is not an input value could preserve descending order but would spoil the stronger permutation theorem. With duplicates, strict partitioning discards extra pivot copies unless an equality block is included.

### Solution 3

**Name the call checkpoint before reading the indices.** After $t$ completed copies, the required next call has
$$n_t=N-1-2t,\qquad i_t=t,$$
and its completed output prefix satisfies $b[r]=a[N-1-2r]$ for every $0\le r<t$. At the initial call $t=0$, the prefix is empty and both parameter equations hold.

Option 1 tests the negative-source guard before accessing an array. When the guard does not return, it writes the next required source into destination $t$, then decreases the source by two and increases the destination by one. These updates establish the same equations at $t+1$. For $N>0$, legal writes have $2t\le N-1$, so there are $\lfloor(N-1)/2\rfloor+1=\lceil N/2\rceil$ writes. At $N=0$, the initial source is negative and no write occurs. Source sequences are $5,3,1$ for six elements and $6,4,2,0$ for seven; destinations are consecutive from zero.

Option 2 starts writing at one, leaving destination zero unwritten. Option 3 writes at destinations $0,2,4,\ldots$, leaving gaps. The original option 4 also has the correct source decrement of two, but writes at $1,3,5,\ldots$, combining the shift and gaps. It must not be rejected for an invented source stride. Signed integer bounds and a destination with at least $\lceil N/2\rceil$ slots are part of a valid implementation; an unsigned negative test would require another guard.

### Solution 4

**Project the recurrence into the requested residue system.** Modulo two, the odd coefficients three and five become one, and the constant four becomes zero. Hence $a_k\equiv a_{k-1}+a_{k-2}\pmod2$. Both specified values are odd. Track consecutive parities rather than constructing enormous integer values:
$$ (1,1)\longmapsto(1,0)\longmapsto(0,1)\longmapsto(1,1). $$
The deterministic pair transition returns to its initial state after three steps, so this entire cycle repeats by induction. The indices $16,17,18$ are odd, odd, even. Since 18 is divisible by three, the even terms in this forward sequence are precisely the indices divisible by three.

For an inclusive interval, count multiples by subtracting two floors:
$$\left\lfloor\frac{113}{3}\right\rfloor-\left\lfloor\frac{99}{3}\right\rfloor=37-33=4.$$
They are $102,105,108,111$, so option 1 is correct. A half-and-half rule would incorrectly predict seven; this recurrence has a three-state phase, not balanced parity. Five adds an out-of-range multiple such as 99 or 114. Ten counts the odd terms among the fourteen requested terms. A few matching examples alone would not prove periodicity; the return of the full consecutive-pair state under a fixed transition provides the proof.

### Solution 5

**Solve for a modular linear conserved quantity.** Let $F(x,y)=x+3y\pmod5$. The two generating moves change its integer expression by $2+3=5$ and $-1+6=5$. Their negatives change it by minus five. Thus every allowed move preserves $F$, and the origin has residue zero. Target $(1,0)$ has residue one and is impossible, so option 4 is correct.

The other targets are actually reachable, which verifies that the obstruction is discriminating. Let $u=(2,1)$ and $v=(-1,2)$. Then $2u-v=(5,0)$, $u+2v=(0,5)$, and $u=(2,1)$. Negative coefficients are legal because reverse moves are permitted and the domain is all integer pairs.

For the general converse, solve $pu+qv=(x,y)$ over the rationals:
$$p=\frac{2x+y}{5},\qquad q=\frac{-x+2y}{5}.$$
If $x+3y\equiv0\pmod5$, then $x\equiv2y\pmod5$, making both numerators divisible by five. The resulting integers provide a valid signed-move construction. Thus this specific conserved residue also characterizes reachability. That sufficiency was derived from the move matrix and the unrestricted domain; it must not be inferred from preservation alone in a guarded or directed system.

### Solution 6

**Use an exact prefix equation at the loop head.** With immutable input length $n$, the productive invariant is
$$s=\sum_{r=0}^{k-1}a_r,\qquad0\le k\le n.$$
Initially $k=0,s=0$ satisfy the empty sum. Under the guard $k<n$, the bounds justify access to $a_k$. Adding that element and then incrementing $k$ extends precisely the prefix in the equation. At exit, the false guard gives $k\ge n$, while the invariant gives $k\le n$; therefore $k=n$ and the equation becomes the required full sum. Option 2 is correct.

The rank $n-k$ is nonnegative and decreases by one on each enabled body execution, proving termination separately. Exact integer arithmetic is assumed; machine overflow would require a bounded-arithmetic or modular specification.

Option 1 is not even preserved for arbitrary arrays: input $[-1]$ gives a negative sum. With nonnegative entries it still says nothing about which entries were accumulated. Option 3 falsely asserts completion at initialization when the array sum is nonzero. Option 4 is the guard and fails at the final loop head; it supplies no output equation. Empty arrays produce zero iterations and the same empty-sum result, without a special unproved convention.

### Solution 7

**Count executed operators in this implementation.** The positive exponents at successive loop heads are $13,6,3,1$, followed by zero. There are four positive iterations, each executing an unconditional base square. The odd exponents 13, 3 and 1 also execute an accumulator multiplication. Consequently the total is $4+3=7$, so option 2 is correct.

For $a=2$, the complete after-iteration states $(r,b,e)$ are $(2,4,6)$, $(2,16,3)$, $(32,256,1)$ and $(8192,65536,0)$. At every loop head, $r b^e=2^{13}$; the last squared base is unused by the answer but its multiplication still executed.

In general, positive $n$ has $\lfloor\log_2n\rfloor+1$ positive halving iterations and $\operatorname{popcount}(n)$ accumulator multiplications. This routine therefore costs their sum. Zero has zero iterations and zero multiplications. Option 1 would fit a version skipping the final unused square, but that is a different program. Eight treats every exponent as odd; six is even. Thirteen follows repeated ordinary multiplication rather than the written binary routine. An operation count requires fixing the base case, final-square convention and counted operation before applying a formula.

### Solution 8

**Choose a weight that absorbs the reset exactly.** Write $\rho(i,j)=i(n+1)+j$ for the fixed nonnegative bound $n$. If $j>0$, its decrement changes the rank by minus one. If $j=0$ and $i>0$, the next state is $(i-1,n)$, whose rank is
$$ (i-1)(n+1)+n=i(n+1)-1=\rho(i,0)-1.$$
Thus option 2 decreases by exactly one on every permitted transition and remains a nonnegative integer. The only terminal state is $(0,0)$, with rank zero. Since every other allowed state has an enabled step, a maximal execution from $(i,j)$ has exactly $i(n+1)+j$ transitions, not merely at most that many.

The raw sum in option 1 changes by $n-1$ at a reset; for $n\ge1$ that is not a strict decrease. The product in option 3 is zero at $(i,0)$ and may become positive after a reset. The expression $i-j$ in option 4 increases when $j$ decreases and need not be nonnegative. Lexicographic order with $i$ primary also proves termination, but the question asks for an integer rank with an exact unit change. When $n=0$, the same formula reduces to $i$ and covers the reset-only boundary.

### Solution 9

**Track the exponent residue and its attainable range.** Suppose $k$ of the ten selected terms are $x^3$ and the other $10-k$ are $x^{-1}$. Their product is
$$x^{3k-(10-k)}=x^{4k-10},\qquad 0\le k\le10.$$
Every attainable exponent is congruent to two modulo four, and conversely every value $4k-10$ in the stated range occurs by selecting any $k$ factors for their positive term. This is a Laurent polynomial; negative exponents such as minus ten are legitimate under the formal interpretation, or for numerical evaluation with $x\ne0$.

The options minus ten, minus two and six correspond respectively to $k=0,2,4$. Exponent eight would require $k=18/4$, which is not an integer. Therefore option 4 is impossible. Parity alone is insufficient: all four options are even, but only three have the correct residue modulo four.

If the factors are $(x^3+x^{-1})$, the coefficient of $x^{4k-10}$ is $\binom{10}{k}$, because distinct choices of the positive-term factors give the same exponent. Existence of an exponent and multiplicity of its coefficient are different requested objects. The invariant gives a zero coefficient outside its residue class; counting subsets supplies the nonzero coefficient inside it.

### Solution 10

**Count each edge by its unique parent.** For a finite full binary tree, let $I$ count internal nodes and $L$ count leaves. Each internal node has exactly two children, giving $E=2I$. Every finite connected tree has one fewer edge than vertices, so $E=I+L-1$. Combining these equations gives $I=L-1$ and $E=2L-2$.

At $L=19$, the internal count is 18, the total vertex count is 37, and the edge count is 36. Option 1 is correct. Option 2 uses the leaf count as an internal count and then doubles it. Option 3 gives the correct internal count but mistakes the 37 vertices for edges. Option 4 supplies no valid count for this tree and violates $L=I+1$.

Structural induction supplies an independent verification: a leaf has $(I,L)=(0,1)$; joining two full trees adds one internal root and adds their leaf counts, preserving $L=I+1$. No assumption that all leaves have equal depth is needed. Fullness is essential: a unary root with a leaf child has $I=L=1$ and would violate this formula. Ordinary leaves, internal nodes and external empty positions are distinct quantities; their names must follow the declared representation.

### Solution 11

**Separate actual reachability from the global closure test.** Assume the candidate is checked over all integer states. Starting at zero and repeatedly adding two reaches exactly $\{0,2,4,\ldots\}$. Every such state differs from one, so $x\ne1$ is a true reachable-state property. Initialization also succeeds.

For inductive preservation, however, the hypothesis is merely $x\ne1$, not that $x$ was reached from zero. State minus one satisfies that hypothesis and has successor one. This is a failing closure edge. It is unreachable from the stated start, so it does not refute safety of actual executions. Option 3 is correct.

An initialized closed strengthening is $x\ge0$ together with $x\equiv0\pmod2$. Adding two preserves both clauses and they imply $x\ne1$. Option 1 ignores that zero satisfies the candidate. Option 2 misses the minus-one predecessor. Option 4 confuses safety with progress: the actual sequence $0,2,4,\ldots$ is infinite. If the state domain were explicitly restricted to nonnegative integers, the minus-one counterexample would be unavailable and $x\ne1$ would be closed. Therefore the revised question states the integer domain explicitly rather than leaving the answer dependent on an unstated modeling choice.

### Solution 12

**A sorting specification needs occurrence preservation and order.** Use induction on input length. The empty and singleton bases already satisfy both clauses. For a pivot input, assume each smaller recursive block returns a descending permutation of exactly its own original occurrences. The greater block lies entirely above the pivot, and the smaller block entirely below it. Their internal order and the two cross-block inequalities make their concatenation descending; partition coverage and uniqueness preserve the entire input. Thus option 3 gives the required proof ingredients.

Sum preservation in option 1 cannot recover order or contents: $[2,2]$ and $[1,3]$ have equal sums but different multisets. Length preservation in option 2 cannot even prevent replacing all entries by zero. Pivot occurrence in option 4 allows arbitrary disorder or loss in the remaining output. Each is at most a weak necessary condition for some inputs, never the stated sufficient specification.

For input $[4,1,3,2,5]$ with pivot three, induction returns $[5,4]$ and $[2,1]$, giving $[5,4,3,2,1]$. A pure routine may evaluate the smaller call first without changing this joined order. The correctness proof assumes a pivot taken from the input; distinct values permit singleton pivot coverage. Duplicate input values require retaining an equality block, and recursive termination still requires strictly shorter child inputs.

### Solution 13

**Use conservation and a separate rank.** At transition count $t$, induction gives $a_t=n-t$ and $b_t=n+1+2t$. Equivalently, $2a+b=3n+1$ is conserved: the change is $2(-1)+2=0$. The guard $a>0$ preserves nonnegativity and decreases natural rank $a$ by exactly one, so exit occurs after exactly $n$ steps. At $a=0$, the conserved equation yields $b=3n+1$. Conservation alone would identify the exit value only if exit happened; the rank and the enabled-step condition justify that event.

**Apply the exact parameter.** For $n=5$, the requested quantity is $3(5)+1=16$. Option 2 reports $11$, which differs from the derived 16. Option 3 reports $6$, which differs from the derived 16. Option 4 reports $15$, which differs from the derived 16. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

The exit condition is the missing link between an equation on arbitrary intermediate states and the final answer. At step $t<n$, $b=n+1+2t$ is generally smaller than its final value. A preserved quantity is not required to decrease; here $2a+b$ stays constant while rank $a$ decreases. This distinguishes the roles of an invariant and a termination measure. At $n=0$, the initial state is already terminal and $b=1$ agrees with the same formula.

### Solution 14

**Use conservation and a separate rank.** At transition count $t$, induction gives $a_t=n-t$ and $b_t=n+1+2t$. Equivalently, $2a+b=3n+1$ is conserved: the change is $2(-1)+2=0$. The guard $a>0$ preserves nonnegativity and decreases natural rank $a$ by exactly one, so exit occurs after exactly $n$ steps. At $a=0$, the conserved equation yields $b=3n+1$. Conservation alone would identify the exit value only if exit happened; the rank and the enabled-step condition justify that event.

**Apply the exact parameter.** For $n=8$, the requested quantity is $3(8)+1=25$. Option 1 reports $17$, which differs from the derived 25. Option 2 reports $9$, which differs from the derived 25. Option 3 reports $24$, which differs from the derived 25. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

The exit condition is the missing link between an equation on arbitrary intermediate states and the final answer. At step $t<n$, $b=n+1+2t$ is generally smaller than its final value. A preserved quantity is not required to decrease; here $2a+b$ stays constant while rank $a$ decreases. This distinguishes the roles of an invariant and a termination measure. At $n=0$, the initial state is already terminal and $b=1$ agrees with the same formula.

### Solution 15

**Use conservation and a separate rank.** At transition count $t$, induction gives $a_t=n-t$ and $b_t=n+1+2t$. Equivalently, $2a+b=3n+1$ is conserved: the change is $2(-1)+2=0$. The guard $a>0$ preserves nonnegativity and decreases natural rank $a$ by exactly one, so exit occurs after exactly $n$ steps. At $a=0$, the conserved equation yields $b=3n+1$. Conservation alone would identify the exit value only if exit happened; the rank and the enabled-step condition justify that event.

**Check the symbolic alternatives.** The proved expression is $3n+1$. At $n=5$ it gives $16$, and at $n=8$ it gives $25$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 3.

The exit condition is the missing link between an equation on arbitrary intermediate states and the final answer. At step $t<n$, $b=n+1+2t$ is generally smaller than its final value. A preserved quantity is not required to decrease; here $2a+b$ stays constant while rank $a$ decreases. This distinguishes the roles of an invariant and a termination measure. At $n=0$, the initial state is already terminal and $b=1$ agrees with the same formula.

### Solution 16

**Use conservation and a separate rank.** At transition count $t$, induction gives $a_t=n-t$ and $b_t=n+1+2t$. Equivalently, $2a+b=3n+1$ is conserved: the change is $2(-1)+2=0$. The guard $a>0$ preserves nonnegativity and decreases natural rank $a$ by exactly one, so exit occurs after exactly $n$ steps. At $a=0$, the conserved equation yields $b=3n+1$. Conservation alone would identify the exit value only if exit happened; the rank and the enabled-step condition justify that event.

**Identify the proof obligation in this version.** The exit condition is the missing link between an equation on arbitrary intermediate states and the final answer. At step $t<n$, $b=n+1+2t$ is generally smaller than its final value. A preserved quantity is not required to decrease; here $2a+b$ stays constant while rank $a$ decreases. This distinguishes the roles of an invariant and a termination measure. At $n=0$, the initial state is already terminal and $b=1$ agrees with the same formula.

The correct conceptual option is 2. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 17

**Preserve divisors; decrease the second argument.** For a guarded step with $b>0$, write $a=qb+r$ with $0\le r<b$. A positive integer divides both $a,b$ exactly when it divides both $b,r$, since $r=a-qb$ and $a=qb+r$. Thus the simultaneous transition $(a,b)\leftarrow(b,r)$ preserves their greatest common divisor. Its new second argument is strictly smaller, giving a nonnegative ranking. At $b=0$, the retained first argument equals the original gcd. From $(30n,18n)$ the successive pairs are $(18n,12n),(12n,6n),(6n,0)$ for positive $n$, so the result is $6n$.

**Apply the exact parameter.** For $n=5$, the requested quantity is $6(5)=30$. Option 1 reports $150$, which differs from the derived 30. Option 3 reports $60$, which differs from the derived 30. Option 4 reports $90$, which differs from the derived 30. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

Using sequential `a=b; b=a%b` without saving the old first value changes the second expression to old $b\bmod b=0$. For example, $(150,90)$ wrongly becomes $(90,0)$ instead of $(90,60)$. The gcd is conserved, not decreasing; the first argument need not strictly decrease, since starting $(3,5)$ makes it increase to five. The promised positive parameter excludes $(0,0)$, whose gcd requires a separately declared convention and whose division step is disabled.

### Solution 18

**Preserve divisors; decrease the second argument.** For a guarded step with $b>0$, write $a=qb+r$ with $0\le r<b$. A positive integer divides both $a,b$ exactly when it divides both $b,r$, since $r=a-qb$ and $a=qb+r$. Thus the simultaneous transition $(a,b)\leftarrow(b,r)$ preserves their greatest common divisor. Its new second argument is strictly smaller, giving a nonnegative ranking. At $b=0$, the retained first argument equals the original gcd. From $(30n,18n)$ the successive pairs are $(18n,12n),(12n,6n),(6n,0)$ for positive $n$, so the result is $6n$.

**Apply the exact parameter.** For $n=8$, the requested quantity is $6(8)=48$. Option 2 reports $96$, which differs from the derived 48. Option 3 reports $144$, which differs from the derived 48. Option 4 reports $240$, which differs from the derived 48. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

Using sequential `a=b; b=a%b` without saving the old first value changes the second expression to old $b\bmod b=0$. For example, $(150,90)$ wrongly becomes $(90,0)$ instead of $(90,60)$. The gcd is conserved, not decreasing; the first argument need not strictly decrease, since starting $(3,5)$ makes it increase to five. The promised positive parameter excludes $(0,0)$, whose gcd requires a separately declared convention and whose division step is disabled.

### Solution 19

**Preserve divisors; decrease the second argument.** For a guarded step with $b>0$, write $a=qb+r$ with $0\le r<b$. A positive integer divides both $a,b$ exactly when it divides both $b,r$, since $r=a-qb$ and $a=qb+r$. Thus the simultaneous transition $(a,b)\leftarrow(b,r)$ preserves their greatest common divisor. Its new second argument is strictly smaller, giving a nonnegative ranking. At $b=0$, the retained first argument equals the original gcd. From $(30n,18n)$ the successive pairs are $(18n,12n),(12n,6n),(6n,0)$ for positive $n$, so the result is $6n$.

**Check the symbolic alternatives.** The proved expression is $6n$. At $n=5$ it gives $30$, and at $n=8$ it gives $48$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 4.

Using sequential `a=b; b=a%b` without saving the old first value changes the second expression to old $b\bmod b=0$. For example, $(150,90)$ wrongly becomes $(90,0)$ instead of $(90,60)$. The gcd is conserved, not decreasing; the first argument need not strictly decrease, since starting $(3,5)$ makes it increase to five. The promised positive parameter excludes $(0,0)$, whose gcd requires a separately declared convention and whose division step is disabled.

### Solution 20

**Preserve divisors; decrease the second argument.** For a guarded step with $b>0$, write $a=qb+r$ with $0\le r<b$. A positive integer divides both $a,b$ exactly when it divides both $b,r$, since $r=a-qb$ and $a=qb+r$. Thus the simultaneous transition $(a,b)\leftarrow(b,r)$ preserves their greatest common divisor. Its new second argument is strictly smaller, giving a nonnegative ranking. At $b=0$, the retained first argument equals the original gcd. From $(30n,18n)$ the successive pairs are $(18n,12n),(12n,6n),(6n,0)$ for positive $n$, so the result is $6n$.

**Identify the proof obligation in this version.** Using sequential `a=b; b=a%b` without saving the old first value changes the second expression to old $b\bmod b=0$. For example, $(150,90)$ wrongly becomes $(90,0)$ instead of $(90,60)$. The gcd is conserved, not decreasing; the first argument need not strictly decrease, since starting $(3,5)$ makes it increase to five. The promised positive parameter excludes $(0,0)$, whose gcd requires a separately declared convention and whose division step is disabled.

The correct conceptual option is 3. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 21

**Price one unit of primary work at its full future cost.** During an $x>0$ step, the change is $\Delta x=-1,\Delta y=n$; later $y>0$ steps have $\Delta x=0,\Delta y=-1$. Define $\rho=(n+1)x+y$. Its changes are respectively $-(n+1)+n=-1$ and minus one. It stays nonnegative on the natural state domain and equals zero exactly at the terminal pair. Every positive-rank state has a legal move, so the transition count is exactly the initial rank $(n+1)n+n=n^2+2n$. An independent accounting has $n$ primary steps followed by $n+n^2$ secondary decrements.

**Apply the exact parameter.** For $n=5$, the requested quantity is $(5)^2+2(5)=35$. Option 2 reports $25$, which differs from the derived 35. Option 3 reports $30$, which differs from the derived 35. Option 4 reports $15$, which differs from the derived 35. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

A growing coordinate does not prevent termination: its future decrements are already accounted for in the primary coordinate's weight. Raw sum $x+y$ changes by $n-1$ in the first phase, so it is not a strict ranking for positive $n$. A preserved assertion or a bounded state description does not count steps; even a finite graph may contain a self-loop. This exact count needs a unit-decreasing rank, a zero terminal rank and availability of a move at every positive rank. For $n=0$, there are zero steps.

### Solution 22

**Price one unit of primary work at its full future cost.** During an $x>0$ step, the change is $\Delta x=-1,\Delta y=n$; later $y>0$ steps have $\Delta x=0,\Delta y=-1$. Define $\rho=(n+1)x+y$. Its changes are respectively $-(n+1)+n=-1$ and minus one. It stays nonnegative on the natural state domain and equals zero exactly at the terminal pair. Every positive-rank state has a legal move, so the transition count is exactly the initial rank $(n+1)n+n=n^2+2n$. An independent accounting has $n$ primary steps followed by $n+n^2$ secondary decrements.

**Apply the exact parameter.** For $n=8$, the requested quantity is $(8)^2+2(8)=80$. Option 1 reports $64$, which differs from the derived 80. Option 2 reports $72$, which differs from the derived 80. Option 3 reports $24$, which differs from the derived 80. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

A growing coordinate does not prevent termination: its future decrements are already accounted for in the primary coordinate's weight. Raw sum $x+y$ changes by $n-1$ in the first phase, so it is not a strict ranking for positive $n$. A preserved assertion or a bounded state description does not count steps; even a finite graph may contain a self-loop. This exact count needs a unit-decreasing rank, a zero terminal rank and availability of a move at every positive rank. For $n=0$, there are zero steps.

### Solution 23

**Price one unit of primary work at its full future cost.** During an $x>0$ step, the change is $\Delta x=-1,\Delta y=n$; later $y>0$ steps have $\Delta x=0,\Delta y=-1$. Define $\rho=(n+1)x+y$. Its changes are respectively $-(n+1)+n=-1$ and minus one. It stays nonnegative on the natural state domain and equals zero exactly at the terminal pair. Every positive-rank state has a legal move, so the transition count is exactly the initial rank $(n+1)n+n=n^2+2n$. An independent accounting has $n$ primary steps followed by $n+n^2$ secondary decrements.

**Check the symbolic alternatives.** The proved expression is $n^2+2n$. At $n=5$ it gives $35$, and at $n=8$ it gives $80$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 3.

A growing coordinate does not prevent termination: its future decrements are already accounted for in the primary coordinate's weight. Raw sum $x+y$ changes by $n-1$ in the first phase, so it is not a strict ranking for positive $n$. A preserved assertion or a bounded state description does not count steps; even a finite graph may contain a self-loop. This exact count needs a unit-decreasing rank, a zero terminal rank and availability of a move at every positive rank. For $n=0$, there are zero steps.

### Solution 24

**Price one unit of primary work at its full future cost.** During an $x>0$ step, the change is $\Delta x=-1,\Delta y=n$; later $y>0$ steps have $\Delta x=0,\Delta y=-1$. Define $\rho=(n+1)x+y$. Its changes are respectively $-(n+1)+n=-1$ and minus one. It stays nonnegative on the natural state domain and equals zero exactly at the terminal pair. Every positive-rank state has a legal move, so the transition count is exactly the initial rank $(n+1)n+n=n^2+2n$. An independent accounting has $n$ primary steps followed by $n+n^2$ secondary decrements.

**Identify the proof obligation in this version.** A growing coordinate does not prevent termination: its future decrements are already accounted for in the primary coordinate's weight. Raw sum $x+y$ changes by $n-1$ in the first phase, so it is not a strict ranking for positive $n$. A preserved assertion or a bounded state description does not count steps; even a finite graph may contain a self-loop. This exact count needs a unit-decreasing rank, a zero terminal rank and availability of a move at every positive rank. For $n=0$, there are zero steps.

The correct conceptual option is 2. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 25

**Count all parent-child edges using the actual arities.** There are $n$ binary internal nodes and $n$ ternary internal nodes, so parent degrees give $E=2n+3n=5n$. If $L$ is the leaf count, the vertex count is $2n+L$. The tree equation $E=V-1$ therefore gives $5n=2n+L-1$, or $L=3n+1$. This counts ordinary terminal vertices, not missing children. Structural induction gives the general identity $L=1+\sum_{v\text{ internal}}(d(v)-1)$; each constructor of arity $d$ adds $d-1$ net leaves.

**Apply the exact parameter.** For $n=5$, the requested quantity is $3(5)+1=16$. Option 1 reports $21$, which differs from the derived 16. Option 2 reports $25$, which differs from the derived 16. Option 4 reports $11$, which differs from the derived 16. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

The edge equation requires a finite connected acyclic tree. A directed cycle does not have one fewer edge than vertices, and a forest would use $E=V-c$ with its component count $c$. Binary and ternary nodes contribute two and three edges, respectively. Height alone does not determine leaves: one can keep a fixed maximum depth while removing or adding lower branches. The all-empty internal-node boundary $n=0$ gives a single root leaf under the nonempty-tree convention.

### Solution 26

**Count all parent-child edges using the actual arities.** There are $n$ binary internal nodes and $n$ ternary internal nodes, so parent degrees give $E=2n+3n=5n$. If $L$ is the leaf count, the vertex count is $2n+L$. The tree equation $E=V-1$ therefore gives $5n=2n+L-1$, or $L=3n+1$. This counts ordinary terminal vertices, not missing children. Structural induction gives the general identity $L=1+\sum_{v\text{ internal}}(d(v)-1)$; each constructor of arity $d$ adds $d-1$ net leaves.

**Apply the exact parameter.** For $n=8$, the requested quantity is $3(8)+1=25$. Option 1 reports $40$, which differs from the derived 25. Option 3 reports $17$, which differs from the derived 25. Option 4 reports $33$, which differs from the derived 25. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

The edge equation requires a finite connected acyclic tree. A directed cycle does not have one fewer edge than vertices, and a forest would use $E=V-c$ with its component count $c$. Binary and ternary nodes contribute two and three edges, respectively. Height alone does not determine leaves: one can keep a fixed maximum depth while removing or adding lower branches. The all-empty internal-node boundary $n=0$ gives a single root leaf under the nonempty-tree convention.

### Solution 27

**Count all parent-child edges using the actual arities.** There are $n$ binary internal nodes and $n$ ternary internal nodes, so parent degrees give $E=2n+3n=5n$. If $L$ is the leaf count, the vertex count is $2n+L$. The tree equation $E=V-1$ therefore gives $5n=2n+L-1$, or $L=3n+1$. This counts ordinary terminal vertices, not missing children. Structural induction gives the general identity $L=1+\sum_{v\text{ internal}}(d(v)-1)$; each constructor of arity $d$ adds $d-1$ net leaves.

**Check the symbolic alternatives.** The proved expression is $3n+1$. At $n=5$ it gives $16$, and at $n=8$ it gives $25$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 1.

The edge equation requires a finite connected acyclic tree. A directed cycle does not have one fewer edge than vertices, and a forest would use $E=V-c$ with its component count $c$. Binary and ternary nodes contribute two and three edges, respectively. Height alone does not determine leaves: one can keep a fixed maximum depth while removing or adding lower branches. The all-empty internal-node boundary $n=0$ gives a single root leaf under the nonempty-tree convention.

### Solution 28

**Count all parent-child edges using the actual arities.** There are $n$ binary internal nodes and $n$ ternary internal nodes, so parent degrees give $E=2n+3n=5n$. If $L$ is the leaf count, the vertex count is $2n+L$. The tree equation $E=V-1$ therefore gives $5n=2n+L-1$, or $L=3n+1$. This counts ordinary terminal vertices, not missing children. Structural induction gives the general identity $L=1+\sum_{v\text{ internal}}(d(v)-1)$; each constructor of arity $d$ adds $d-1$ net leaves.

**Identify the proof obligation in this version.** The edge equation requires a finite connected acyclic tree. A directed cycle does not have one fewer edge than vertices, and a forest would use $E=V-c$ with its component count $c$. Binary and ternary nodes contribute two and three edges, respectively. Height alone does not determine leaves: one can keep a fixed maximum depth while removing or adding lower branches. The all-empty internal-node boundary $n=0$ gives a single root leaf under the nonempty-tree convention.

The correct conceptual option is 4. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 29

**Index the loop head by completed iterations.** After $t$ iterations, $i=t+2$ and $s=2+3+\cdots+(t+1)=t(t+3)/2$. At $t=0$ the sum is empty. If the formulas hold before a step, adding the old index $t+2$ gives $t(t+3)/2+t+2=(t+1)(t+4)/2$; incrementing the index restores its formula at $t+1$. Exactly $n$ iterations therefore give $s=n(n+3)/2$ and final $i=n+2$. Equivalently the loop-head equation is $s=i(i-1)/2-1$, which includes initial $i=2,s=0$.

**Apply the exact parameter.** For $n=5$, the requested quantity is $\frac{(5)((5)+3)}2=20$. Option 1 reports $25$, which differs from the derived 20. Option 3 reports $15$, which differs from the derived 20. Option 4 reports $\frac{35}{2}$, which differs from the derived 20. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

Incrementing before addition changes the accumulated terms from $2,\ldots,n+1$ to $3,\ldots,n+2$. The new sum is $n(n+5)/2$, larger by $n$. A loop-head invariant must be rederived at a different checkpoint; the same equality need not hold halfway through the body. The growing sum is an output quantity, not a decreasing termination rank. An explicit remaining-iteration count $n-t$ establishes termination, including zero iterations.

### Solution 30

**Index the loop head by completed iterations.** After $t$ iterations, $i=t+2$ and $s=2+3+\cdots+(t+1)=t(t+3)/2$. At $t=0$ the sum is empty. If the formulas hold before a step, adding the old index $t+2$ gives $t(t+3)/2+t+2=(t+1)(t+4)/2$; incrementing the index restores its formula at $t+1$. Exactly $n$ iterations therefore give $s=n(n+3)/2$ and final $i=n+2$. Equivalently the loop-head equation is $s=i(i-1)/2-1$, which includes initial $i=2,s=0$.

**Apply the exact parameter.** For $n=8$, the requested quantity is $\frac{(8)((8)+3)}2=44$. Option 2 reports $36$, which differs from the derived 44. Option 3 reports $40$, which differs from the derived 44. Option 4 reports $64$, which differs from the derived 44. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

Incrementing before addition changes the accumulated terms from $2,\ldots,n+1$ to $3,\ldots,n+2$. The new sum is $n(n+5)/2$, larger by $n$. A loop-head invariant must be rederived at a different checkpoint; the same equality need not hold halfway through the body. The growing sum is an output quantity, not a decreasing termination rank. An explicit remaining-iteration count $n-t$ establishes termination, including zero iterations.

### Solution 31

**Index the loop head by completed iterations.** After $t$ iterations, $i=t+2$ and $s=2+3+\cdots+(t+1)=t(t+3)/2$. At $t=0$ the sum is empty. If the formulas hold before a step, adding the old index $t+2$ gives $t(t+3)/2+t+2=(t+1)(t+4)/2$; incrementing the index restores its formula at $t+1$. Exactly $n$ iterations therefore give $s=n(n+3)/2$ and final $i=n+2$. Equivalently the loop-head equation is $s=i(i-1)/2-1$, which includes initial $i=2,s=0$.

**Check the symbolic alternatives.** The proved expression is $\frac{n(n+3)}2$. At $n=5$ it gives $20$, and at $n=8$ it gives $44$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 4.

Incrementing before addition changes the accumulated terms from $2,\ldots,n+1$ to $3,\ldots,n+2$. The new sum is $n(n+5)/2$, larger by $n$. A loop-head invariant must be rederived at a different checkpoint; the same equality need not hold halfway through the body. The growing sum is an output quantity, not a decreasing termination rank. An explicit remaining-iteration count $n-t$ establishes termination, including zero iterations.

### Solution 32

**Index the loop head by completed iterations.** After $t$ iterations, $i=t+2$ and $s=2+3+\cdots+(t+1)=t(t+3)/2$. At $t=0$ the sum is empty. If the formulas hold before a step, adding the old index $t+2$ gives $t(t+3)/2+t+2=(t+1)(t+4)/2$; incrementing the index restores its formula at $t+1$. Exactly $n$ iterations therefore give $s=n(n+3)/2$ and final $i=n+2$. Equivalently the loop-head equation is $s=i(i-1)/2-1$, which includes initial $i=2,s=0$.

**Identify the proof obligation in this version.** Incrementing before addition changes the accumulated terms from $2,\ldots,n+1$ to $3,\ldots,n+2$. The new sum is $n(n+5)/2$, larger by $n$. A loop-head invariant must be rederived at a different checkpoint; the same equality need not hold halfway through the body. The growing sum is an output quantity, not a decreasing termination rank. An explicit remaining-iteration count $n-t$ establishes termination, including zero iterations.

The correct conceptual option is 3. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 33

**Count calls by level, not by simultaneous stack occupancy.** A complete three-branch call tree of depth $n$ has $3^k$ calls at level $k$, by induction from its single root. Therefore the total including all bases is $C_n=\sum_{k=0}^{n}3^k=(3^{n+1}-1)/2$. Multiply the sum by three and subtract the original sum to obtain $2C_n=3^{n+1}-1$. The recursive alternative is $C_0=1$ and $C_n=1+3C_{n-1}$, producing the same result. The leaf-only count is $3^n$, while the internal-only count is $(3^n-1)/2$.

**Apply the exact parameter.** For $n=5$, the requested quantity is $\frac{3^{(5)+1}-1}2=364$. Option 1 reports $729$, which differs from the derived 364. Option 2 reports $121$, which differs from the derived 364. Option 4 reports $243$, which differs from the derived 364. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

Maximum depth counts edges on one root-to-leaf path; maximum ordinary recursion-stack occupancy is $n+1$ active calls when children are evaluated sequentially. Neither quantity equals the total calls made across all branches. Three calls per nonbase node produce exponentially many nodes over several levels, not just three overall. The assumed equal leaf depth makes the complete-level sum applicable; an irregular recursion tree would require its actual constructor counts. At depth zero, there is one root/base call, not zero.

### Solution 34

**Count calls by level, not by simultaneous stack occupancy.** A complete three-branch call tree of depth $n$ has $3^k$ calls at level $k$, by induction from its single root. Therefore the total including all bases is $C_n=\sum_{k=0}^{n}3^k=(3^{n+1}-1)/2$. Multiply the sum by three and subtract the original sum to obtain $2C_n=3^{n+1}-1$. The recursive alternative is $C_0=1$ and $C_n=1+3C_{n-1}$, producing the same result. The leaf-only count is $3^n$, while the internal-only count is $(3^n-1)/2$.

**Apply the exact parameter.** For $n=8$, the requested quantity is $\frac{3^{(8)+1}-1}2=9841$. Option 1 reports $3280$, which differs from the derived 9841. Option 3 reports $6561$, which differs from the derived 9841. Option 4 reports $19683$, which differs from the derived 9841. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

Maximum depth counts edges on one root-to-leaf path; maximum ordinary recursion-stack occupancy is $n+1$ active calls when children are evaluated sequentially. Neither quantity equals the total calls made across all branches. Three calls per nonbase node produce exponentially many nodes over several levels, not just three overall. The assumed equal leaf depth makes the complete-level sum applicable; an irregular recursion tree would require its actual constructor counts. At depth zero, there is one root/base call, not zero.

### Solution 35

**Count calls by level, not by simultaneous stack occupancy.** A complete three-branch call tree of depth $n$ has $3^k$ calls at level $k$, by induction from its single root. Therefore the total including all bases is $C_n=\sum_{k=0}^{n}3^k=(3^{n+1}-1)/2$. Multiply the sum by three and subtract the original sum to obtain $2C_n=3^{n+1}-1$. The recursive alternative is $C_0=1$ and $C_n=1+3C_{n-1}$, producing the same result. The leaf-only count is $3^n$, while the internal-only count is $(3^n-1)/2$.

**Check the symbolic alternatives.** The proved expression is $\frac{3^{n+1}-1}2$. At $n=5$ it gives $364$, and at $n=8$ it gives $9841$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 1.

Maximum depth counts edges on one root-to-leaf path; maximum ordinary recursion-stack occupancy is $n+1$ active calls when children are evaluated sequentially. Neither quantity equals the total calls made across all branches. Three calls per nonbase node produce exponentially many nodes over several levels, not just three overall. The assumed equal leaf depth makes the complete-level sum applicable; an irregular recursion tree would require its actual constructor counts. At depth zero, there is one root/base call, not zero.

### Solution 36

**Count calls by level, not by simultaneous stack occupancy.** A complete three-branch call tree of depth $n$ has $3^k$ calls at level $k$, by induction from its single root. Therefore the total including all bases is $C_n=\sum_{k=0}^{n}3^k=(3^{n+1}-1)/2$. Multiply the sum by three and subtract the original sum to obtain $2C_n=3^{n+1}-1$. The recursive alternative is $C_0=1$ and $C_n=1+3C_{n-1}$, producing the same result. The leaf-only count is $3^n$, while the internal-only count is $(3^n-1)/2$.

**Identify the proof obligation in this version.** Maximum depth counts edges on one root-to-leaf path; maximum ordinary recursion-stack occupancy is $n+1$ active calls when children are evaluated sequentially. Neither quantity equals the total calls made across all branches. Three calls per nonbase node produce exponentially many nodes over several levels, not just three overall. The assumed equal leaf depth makes the complete-level sum applicable; an irregular recursion tree would require its actual constructor counts. At depth zero, there is one root/base call, not zero.

The correct conceptual option is 4. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 37

**Account for the unfinished last period explicitly.** The specified parity cycle has two odd positions followed by one even position. The range $1,\ldots,3n-1$ consists of $n-1$ full blocks and the first two positions of the next block. Thus it contains $2(n-1)+2=2n$ odd terms and $n-1$ even terms. As a second calculation, even positions are exactly the multiples of three, numbering $\lfloor(3n-1)/3\rfloor=n-1$; subtract from the $3n-1$ total to obtain $2n$. Positive $n$ is needed for the stated nonempty interval.

**Apply the exact parameter.** For $n=5$, the requested quantity is $2(5)=10$. Option 1 reports $14$, which differs from the derived 10. Option 3 reports $9$, which differs from the derived 10. Option 4 reports $5$, which differs from the derived 10. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

A deterministic recurrence should be projected to a full residue state, such as a consecutive pair, before asserting a cycle. Observing a few terms is not a proof that later terms repeat. Once the state returns and the transition is fixed, induction proves the repeated state sequence and permits distant interval counts without huge integer evaluations. The unfinished two-entry block is all odd here and cannot be discarded. Equal odd/even counts are not universal recurrence behavior; they fail already in the given three-term period.

### Solution 38

**Account for the unfinished last period explicitly.** The specified parity cycle has two odd positions followed by one even position. The range $1,\ldots,3n-1$ consists of $n-1$ full blocks and the first two positions of the next block. Thus it contains $2(n-1)+2=2n$ odd terms and $n-1$ even terms. As a second calculation, even positions are exactly the multiples of three, numbering $\lfloor(3n-1)/3\rfloor=n-1$; subtract from the $3n-1$ total to obtain $2n$. Positive $n$ is needed for the stated nonempty interval.

**Apply the exact parameter.** For $n=8$, the requested quantity is $2(8)=16$. Option 2 reports $15$, which differs from the derived 16. Option 3 reports $8$, which differs from the derived 16. Option 4 reports $23$, which differs from the derived 16. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

A deterministic recurrence should be projected to a full residue state, such as a consecutive pair, before asserting a cycle. Observing a few terms is not a proof that later terms repeat. Once the state returns and the transition is fixed, induction proves the repeated state sequence and permits distant interval counts without huge integer evaluations. The unfinished two-entry block is all odd here and cannot be discarded. Equal odd/even counts are not universal recurrence behavior; they fail already in the given three-term period.

### Solution 39

**Account for the unfinished last period explicitly.** The specified parity cycle has two odd positions followed by one even position. The range $1,\ldots,3n-1$ consists of $n-1$ full blocks and the first two positions of the next block. Thus it contains $2(n-1)+2=2n$ odd terms and $n-1$ even terms. As a second calculation, even positions are exactly the multiples of three, numbering $\lfloor(3n-1)/3\rfloor=n-1$; subtract from the $3n-1$ total to obtain $2n$. Positive $n$ is needed for the stated nonempty interval.

**Check the symbolic alternatives.** The proved expression is $2n$. At $n=5$ it gives $10$, and at $n=8$ it gives $16$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 4.

A deterministic recurrence should be projected to a full residue state, such as a consecutive pair, before asserting a cycle. Observing a few terms is not a proof that later terms repeat. Once the state returns and the transition is fixed, induction proves the repeated state sequence and permits distant interval counts without huge integer evaluations. The unfinished two-entry block is all odd here and cannot be discarded. Equal odd/even counts are not universal recurrence behavior; they fail already in the given three-term period.

### Solution 40

**Account for the unfinished last period explicitly.** The specified parity cycle has two odd positions followed by one even position. The range $1,\ldots,3n-1$ consists of $n-1$ full blocks and the first two positions of the next block. Thus it contains $2(n-1)+2=2n$ odd terms and $n-1$ even terms. As a second calculation, even positions are exactly the multiples of three, numbering $\lfloor(3n-1)/3\rfloor=n-1$; subtract from the $3n-1$ total to obtain $2n$. Positive $n$ is needed for the stated nonempty interval.

**Identify the proof obligation in this version.** A deterministic recurrence should be projected to a full residue state, such as a consecutive pair, before asserting a cycle. Observing a few terms is not a proof that later terms repeat. Once the state returns and the transition is fixed, induction proves the repeated state sequence and permits distant interval counts without huge integer evaluations. The unfinished two-entry block is all odd here and cannot be discarded. Equal odd/even counts are not universal recurrence behavior; they fail already in the given three-term period.

The correct conceptual option is 3. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 41

**Compute the affine change instead of assuming conservation.** The simultaneous next state is $a'=2n+1,b'=2$, so its difference is $a'-b'=2n-1$. For an arbitrary state let $d=a-b$. The general transition gives $d'=2d+1$, hence $d'-d=d+1$; the difference is not conserved. Setting $u=d+1$ absorbs the affine constant and gives $u'=2u$. After $t$ iterations from $(n,1)$, induction yields $d_t=2^t n-1$, because $u_0=n$. This broader formula recovers the required single-step value at $t=1$.

**Apply the exact parameter.** For $n=5$, the requested quantity is $2(5)-1=9$. Option 1 reports $4$, which differs from the derived 9. Option 2 reports $11$, which differs from the derived 9. Option 3 reports $10$, which differs from the derived 9. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

An affine potential may simplify a recurrence even when it is not constant or a termination rank. Here $d+1$ doubles; the time-indexed relation $(d_t+1)/2^t=n$ is constant only when transition count is included in the extended state. Dropping the added one changes the actual answer. The title is corrected to describe an affine difference, since calling the raw difference conserved is false. No stopping rule is supplied, so this one-step arithmetic calculation is not a termination theorem.

### Solution 42

**Compute the affine change instead of assuming conservation.** The simultaneous next state is $a'=2n+1,b'=2$, so its difference is $a'-b'=2n-1$. For an arbitrary state let $d=a-b$. The general transition gives $d'=2d+1$, hence $d'-d=d+1$; the difference is not conserved. Setting $u=d+1$ absorbs the affine constant and gives $u'=2u$. After $t$ iterations from $(n,1)$, induction yields $d_t=2^t n-1$, because $u_0=n$. This broader formula recovers the required single-step value at $t=1$.

**Apply the exact parameter.** For $n=8$, the requested quantity is $2(8)-1=15$. Option 1 reports $17$, which differs from the derived 15. Option 2 reports $16$, which differs from the derived 15. Option 4 reports $7$, which differs from the derived 15. The intermediate state, a related count, and the actual requested endpoint cannot be interchanged.

An affine potential may simplify a recurrence even when it is not constant or a termination rank. Here $d+1$ doubles; the time-indexed relation $(d_t+1)/2^t=n$ is constant only when transition count is included in the extended state. Dropping the added one changes the actual answer. The title is corrected to describe an affine difference, since calling the raw difference conserved is false. No stopping rule is supplied, so this one-step arithmetic calculation is not a termination theorem.

### Solution 43

**Compute the affine change instead of assuming conservation.** The simultaneous next state is $a'=2n+1,b'=2$, so its difference is $a'-b'=2n-1$. For an arbitrary state let $d=a-b$. The general transition gives $d'=2d+1$, hence $d'-d=d+1$; the difference is not conserved. Setting $u=d+1$ absorbs the affine constant and gives $u'=2u$. After $t$ iterations from $(n,1)$, induction yields $d_t=2^t n-1$, because $u_0=n$. This broader formula recovers the required single-step value at $t=1$.

**Check the symbolic alternatives.** The proved expression is $2n-1$. At $n=5$ it gives $9$, and at $n=8$ it gives $15$. These checks expose the other listed expressions; the proof establishes the general formula rather than inferring it from two instances. The selected option is 2.

An affine potential may simplify a recurrence even when it is not constant or a termination rank. Here $d+1$ doubles; the time-indexed relation $(d_t+1)/2^t=n$ is constant only when transition count is included in the extended state. Dropping the added one changes the actual answer. The title is corrected to describe an affine difference, since calling the raw difference conserved is false. No stopping rule is supplied, so this one-step arithmetic calculation is not a termination theorem.

### Solution 44

**Compute the affine change instead of assuming conservation.** The simultaneous next state is $a'=2n+1,b'=2$, so its difference is $a'-b'=2n-1$. For an arbitrary state let $d=a-b$. The general transition gives $d'=2d+1$, hence $d'-d=d+1$; the difference is not conserved. Setting $u=d+1$ absorbs the affine constant and gives $u'=2u$. After $t$ iterations from $(n,1)$, induction yields $d_t=2^t n-1$, because $u_0=n$. This broader formula recovers the required single-step value at $t=1$.

**Identify the proof obligation in this version.** An affine potential may simplify a recurrence even when it is not constant or a termination rank. Here $d+1$ doubles; the time-indexed relation $(d_t+1)/2^t=n$ is constant only when transition count is included in the extended state. Dropping the added one changes the actual answer. The title is corrected to describe an affine difference, since calling the raw difference conserved is false. No stopping rule is supplied, so this one-step arithmetic calculation is not a termination theorem.

The correct conceptual option is 1. The other options omit a stated hypothesis, replace the measured object, or assert a change incompatible with the explicit transition calculation above. Use the preserved relation and the actual guard together; no unsupported inference about unreachable states, rank descent or constructor structure is needed.

### Solution 45

**The final unused square is still an executed multiplication.** Positive exponents in the stated loop are $13,6,3,1$. Every one of these four iterations squares the base; exactly the three odd exponents multiply the accumulator. The total is $4+3=7$, so option 3 is correct. The algorithm starts from exponent thirteen but does not perform thirteen ordinary repeated multiplications.

The invariant at the loop head is $y b^e=a^{13}$. With $e=2q$, updating $(b,e)$ to $(b^2,q)$ preserves it. With $e=2q+1$, multiplying the old $b$ into $y$ first gives $(yb)(b^2)^q=yb^{2q+1}$, again preserving it. Exponent zero makes the invariant identify the returned accumulator with the requested power. Halving a positive natural exponent proves termination.

Five matches a common recursive version with a direct exponent-one base and no accumulator multiplication by the initial identity. Six matches this iterative version after removing the final unused square. Eight treats all four heads as odd. Each distractor changes a convention that the given pseudocode fixed explicitly. The final base may be irrelevant to the answer and nevertheless contribute to the cost. Zero input exponent executes none of these operators.

### Solution 46

**Enumerate the complete modular orbit and certify its complement.** After $t$ moves from the origin, the state is $(t,2t)\pmod5$. Its five distinct residue states are $(0,0),(1,2),(2,4),(3,1),(4,3)$, after which the state repeats. This follows directly by adding the same vector at each transition. The conserved quantity $y-2x\pmod5$ is zero at initialization and changes by $2-2=0$ in a move.

Target $(3,4)$ has residue $4-2\cdot3\equiv3\pmod5$, so it lies outside the orbit and is unreachable. Option 3 is correct. Options 1, 2 and 4 occur respectively after one, two and four moves; the explicit trace verifies their attainability rather than assuming matching invariant values are automatically sufficient.

The pair domain is the twenty-five residue pairs, but the actual orbit has five states. A cyclic reachable graph supplies an infinite execution when moves remain allowed, so this conservation argument does not prove termination. In this particular cyclic group, every pair with $y\equiv2x$ is reached by selecting the representative $t=x\in\{0,1,2,3,4\}$, proving sufficiency as well as necessity. Removing moves or imposing guards would require rechecking that converse.
