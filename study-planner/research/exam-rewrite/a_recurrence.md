## Teaching through formulas and conceptual decisions

### Account for a whole level before summing the tree

For$T(n)=aT(n/b)+f(n)$ on$n=b^h$, depth$i$ has$a^i$ nodes, each of size$n/b^i$. Its toll is$a^if(n/b^i)$. The leaf contribution is$a^hT(1)=n^{\log_ba}T(1)$. Every proposed total must include both internal work and leaves. If$f$ is stated only as an upper bound, the equation may not determine a tight internal-work rate, although a leaf lower bound can remain decisive.

For the balanced critical recurrence with$a=b$, toll$n(\log n)^q$ and a positive constant base cutoff, reindex levels by distance from the leaves. Total internal work has order$n\sum_{j=1}^{h}j^q$. This yields$n\log^{q+1}n$ when$q>-1$, $n\log\log n$ when$q=-1$, and$n$ when$q<-1$, after adding the linear leaves. The logarithmic denominator must be defined only above the stated cutoff; evaluating a toll$n/\log n$ at1 is invalid.

### Change variables when arguments are not linear fractions

For$T(n)=T(\sqrt n)+1$, let$n=2^{2^k}$ and set$U(k)=T(2^{2^k})$. Then$U(k)=U(k-1)+1$, so$T(n)$ is order$\log\log n$. For$T(n)=2T(\sqrt n)+\log_2n$, instead set$m=\log_2n$ and$U(m)=T(2^m)$; the equation becomes$U(m)=2U(m/2)+m$. Its solution is$\Theta(m\log m)$, giving$\Theta(\log n\log\log n)$. Translate back to the original variable at the end.

### Unequal split exponents and resources

For$T(n)=T(n/3)+T(2n/3)+n$ with admissible rounding and positive base cost, the Akra–Bazzi exponent$p$ satisfies $(1/3)^p+(2/3)^p=1$, giving$p=1$. The integral correction from the linear toll is logarithmic, so the result is$n\log n$. Work sums child costs; parallel span can instead take their maximum. Storage of a depth-first implementation counts simultaneously live data, not every node ever created.

## Formula and conceptual problem bank

### Question 1. Leaf-dominated recurrence

For$n=2^k$, $T(n)=4T(n/2)+n$ with$T(1)=1$. What is its tight order?

**A.** $\Theta(n)$

**B.** $\Theta(n\log n)$

**C.** $\Theta(n^2)$

**D.** $\Theta(n^3)$

**Answer: C.**

The leaf exponent is$\log_24=2$. At depth$i$, toll is$4^i(n/2^i)=n2^i$, which grows geometrically toward the leaves. Its sum is quadratic and the$n^2$ leaves give a matching lower bound. Comparing only the root’s linear toll misses most of the work.

### Question 2. Balanced critical toll

$T(n)=2T(n/2)+n\log_2n$ on powers of two, with$T(1)=1$. What is the tight order?

**A.** $\Theta(n\log n)$

**B.** $\Theta(n\log^2n)$

**C.** $\Theta(n^2)$

**D.** $\Theta(\log^2n)$

**Answer: B.**

Write$h=\log_2n$. Level$i$ contributes$n(h-i)$. Sum$i=0$ through$h-1$ to obtain$n h(h+1)/2$, then add$n$ leaf work. The result is order$n\log^2n$. The logarithm is not a polynomial gap allowing classical case3.

### Question 3. Critical reciprocal log

For powers of two above cutoff2, $T(n)=2T(n/2)+n/\log_2n$, with positive constant base cost at2. What is the order?

**A.** $\Theta(n)$

**B.** $\Theta(n\log\log n)$

**C.** $\Theta(n\log n)$

**D.** $\Theta(n/\log n)$

**Answer: B.**

Let$h=\log_2n$. Level tolls are$n/(h-i)$ until the cutoff. Their sum is a linear factor times a harmonic sum of order$\log h$. Leaves add linear work, so total is$\Theta(n\log\log n)$. The cutoff makes every denominator nonzero.

### Question 4. Convergent critical tail

With the same cutoff convention, $T(n)=2T(n/2)+n/(\log_2n)^2$. What is the order?

**A.** $\Theta(n)$

**B.** $\Theta(n\log\log n)$

**C.** $\Theta(n\log n)$

**D.** $\Theta(n^2)$

**Answer: A.**

After reindexing, the level sum is$n\sum_{j=2}^{h}1/j^2$, bounded above and below by positive constants times$n$. The leaf contribution is also linear. A logarithmic saving in the toll does not reduce below the cost of the linear number of leaves.

### Question 5. A decreasing-by-one chain

$T(n)=T(n-1)+n$ with$T(0)=0$. What is$T(10)$?

**A.** 45

**B.** 50

**C.** 55

**D.** 100

**Answer: C.**

Unroll to the exact sum$10+9+\cdots+1=55$. The base contributes zero. Applying a divide-and-conquer master formula to$n-1$ is invalid because the shrink factor is not a fixed$b>1$. The sum determines both the exact value and quadratic asymptotic order.

### Question 6. Unequal mass-conserving split

$T(n)=T(n/3)+T(2n/3)+n$ with conventional rounding and constant positive base costs. What is the tight order?

**A.** $\Theta(n)$

**B.** $\Theta(n\log n)$

**C.** $\Theta(n^{\log_32})$

**D.** $\Theta(n^2)$

**Answer: B.**

The exponent equation $(1/3)^p+(2/3)^p=1$ has$p=1$. The integral term is$\int_1^n u/u^2\,du=\log n$, so Akra–Bazzi gives$n(1+\log n)$. Ordinary equal-subproblem master parameters do not describe the unequal split. Rounding must meet the theorem’s admissible perturbation conditions.

### Question 7. Shrinking total mass

$T(n)=T(n/3)+T(n/4)+n$ with constant positive bases and admissible rounding. What is the tight order?

**A.** $\Theta(n)$

**B.** $\Theta(n\log n)$

**C.** $\Theta(n^2)$

**D.** $\Theta(\log n)$

**Answer: A.**

The total child size is$(7/12)n$, so successive total linear tolls decrease geometrically up to rounding effects. The root already costs$n$, giving a linear lower bound. A substitution with sufficient constant slack proves the matching upper bound. Two recursive calls alone do not imply$n\log n$ work.

### Question 8. Square-root recursion

$T(n)=T(\sqrt n)+1$, with a fixed base for$n\le2$ and idealized arguments$n=2^{2^k}$. What is the tight order?

**A.** $\Theta(\log n)$

**B.** $\Theta(\log\log n)$

**C.** $\Theta(\sqrt n)$

**D.** $\Theta(1)$

**Answer: B.**

Each square root halves$\log_2n$, so$k$ successive roots reach the cutoff when$n=2^{2^k}$. Since$k=\log_2\log_2n$, the one-per-level cost is doubly logarithmic. Treating the root as division by a constant applies the wrong recurrence family.

### Question 9. Transformed critical recurrence

$T(n)=2T(\sqrt n)+\log_2n$ with fixed small bases on a compatible domain. What is the tight order?

**A.** $\Theta(\log n)$

**B.** $\Theta(\log n\log\log n)$

**C.** $\Theta(n\log n)$

**D.** $\Theta(\log^2n)$

**Answer: B.**

Let$m=\log_2n$ and$U(m)=T(2^m)$. The equation becomes$U(m)=2U(m/2)+m$, giving$\Theta(m\log m)$. Substituting back yields the listed expression. Leaving the answer in$m$ or writing$n\log n$ without reversing the variable change loses the original input scale.

### Question 10. Exact balanced count

$T(n)=2T(n/2)+n$ on powers of two with$T(1)=1$. What is$T(8)$?

**A.** 16

**B.** 24

**C.** 32

**D.** 64

**Answer: C.**

There are three internal levels, each costing8, plus eight unit-cost leaves. Thus$T(8)=8\cdot3+8=32$. Equivalently values are$T(2)=4,T(4)=12,T(8)=32$.24 omits the leaf cost. Exact counts retain bases that asymptotic notation may hide.

### Question 11. Repeated characteristic root

$a_n=2a_{n-1}-a_{n-2}$ with$a_0=1,a_1=3$. What is$a_n$?

**A.** $2^n$

**B.** $1+2n$

**C.** $n^2+1$

**D.** $3^n$

**Answer: B.**

The characteristic polynomial is$(r-1)^2$, so the general form is$A+Bn$. The first base gives$A=1$ and the second$B=2$. Another direct proof observes that first differences satisfy$a_n-a_{n-1}=a_{n-1}-a_{n-2}$ and remain2. A repeated root requires the polynomial factor$n$.

### Question 12. Resonant forcing

$a_n=2a_{n-1}+2^n$ with$a_0=0$. What is$a_n$?

**A.** $2^n$

**B.** $n2^n$

**C.** $2^{n+1}$

**D.** $n^2$

**Answer: B.**

Divide by$2^n$ and set$b_n=a_n/2^n$. Then$b_n=b_{n-1}+1$ with$b_0=0$, giving$b_n=n$. Multiply back to get$n2^n$. The forcing term resonates with the homogeneous factor2, so a constant multiple of$2^n$ alone cannot satisfy the equation.

### Question 13. Memoized overlapping states

A recursive program computes$F_n$ from$F_{n-1},F_{n-2}$ with constant local work. Memoization stores each$F_k$ once. What is total arithmetic work through$F_n$ under unit-cost arithmetic?

**A.** $\Theta(2^n)$

**B.** $\Theta(n)$

**C.** $\Theta(\log n)$

**D.** $\Theta(n^2)$

**Answer: B.**

There are$n+1$ distinct indexed states and each nonbase state requires a constant number of table lookups and arithmetic operations. Memoization counts the state DAG, not every occurrence in the expanded recursion tree. With bit-cost arithmetic on growing Fibonacci integers, the unit-cost conclusion would need revision.

### Question 14. Work versus span

A parallel algorithm has$W(n)=2W(n/2)+n$ and$S(n)=S(n/2)+n$, with constant positive bases. What are their orders?

**A.** Both$\Theta(n\log n)$.

**B.** $W=\Theta(n\log n),S=\Theta(n)$.

**C.** $W=\Theta(n),S=\Theta(\log n)$.

**D.** Both$\Theta(\log n)$.

**Answer: B.**

Work adds both child subcomputations and has a linear toll at every level, giving$n\log n$. Span takes one longest child chain; its tolls are$n+n/2+n/4+\cdots$, summing to linear$n$. Parallelism does not make a serial linear combine constant time.

### Question 15. Insufficient toll information

$T(n)=2T(n/2)+f(n)$ with$f(n)\in O(n^2)$, $f(n)\ge0$, positive constant bases. Which is guaranteed without a lower bound on$f$?

**A.** $T\in\Theta(n^2)$

**B.** $T\in O(n^2)$ and$T\in\Omega(n)$.

**C.** $T\in\Theta(n\log n)$

**D.** $T\in O(\log n)$

**Answer: B.**

Using the maximum permitted quadratic toll gives a quadratic upper bound, while the$n$ positive-cost leaves give a linear lower bound. The choice$f=0$ gives linear cost, whereas$f=n^2$ gives quadratic cost, so no single tight rate is forced. Replacing an$O$ statement by a$\Theta$ toll changes the assumptions.

### Question 16. Depth-first auxiliary storage

A balanced depth-first recursive algorithm allocates$c n$ temporary words at size$n$, retains them during both child calls, and frees them on return. Child sizes halve. What is peak extra storage?

**A.** $\Theta(\log n)$

**B.** $\Theta(n)$

**C.** $\Theta(n\log n)$

**D.** $\Theta(n^2)$

**Answer: B.**

Only one child path is active at a time, with simultaneously live arrays totaling$cn+cn/2+cn/4+\cdots<2cn$, plus logarithmic stack metadata. The root allocation gives a linear lower bound. Summing allocations across every tree node counts lifetime allocation volume rather than peak storage.

<!-- CHALLENGE-BANK -->

### Question 17. Challenge: A slowly shrinking argument

For integer$n>1$, $T(n)=T(n-\lceil\sqrt n\rceil)+1$, with constant base cost for$n\le1$. What is its tight order?

**A.** $\Theta(\log n)$

**B.** $\Theta(\sqrt n)$

**C.** $\Theta(n)$

**D.** $\Theta(n\log n)$

**Answer: B.**

Each step removes order$\sqrt n$ items, and the potential$\sqrt n$ decreases by a positive constant order: rationalize $\sqrt n-\sqrt{n-\lceil\sqrt n\rceil}$ as the decrement divided by the sum of roots. Away from the fixed small cutoff this difference is bounded above and below by constants. Hence order$\sqrt n$ steps are necessary and sufficient. The final small states add only a constant. Neither subtract-one unrolling nor equal-fraction master cases model this shrink rule.

### Question 18. Challenge: Work with a repeated state

A program recursively calls the identical size-$n/2$ subproblem twice, then does$n$ work. If the second call reuses the first result instead of recomputing, what is the resulting work order?

**A.** $\Theta(\log n)$

**B.** $\Theta(n)$

**C.** $\Theta(n\log n)$

**D.** $\Theta(n^2)$

**Answer: B.**

Without reuse the execution tree follows$2T(n/2)+n$ and costs$n\log n$. With one actual child computation per size, the recurrence is$T(n/2)+n$ and its tolls form$n+n/2+n/4+\cdots=\Theta(n)$. The specification requires identical subproblems and reusable results; equal sizes alone do not prove that the child instances are identical.

## Applicable formulas and examination notes

### 1. Whole-level toll

For$aT(n/b)+f(n)$, level$i$ costs$a^if(n/b^i)$ and leaves cost$n^{\log_ba}T(1)$. Count both. A root-only comparison misses leaf-dominated and critical cases.

### 2. Master comparison

For $T(n)=aT(n/b)+f(n)$ with $a\ge1$, $b>1$, nonnegative toll and positive constant bases, put $p=\log_ba$. If $f(n)=O(n^{p-\epsilon})$ for some fixed $\epsilon>0$, the answer is $\Theta(n^p)$. If $f(n)=\Theta(n^p)$, the answer is $\Theta(n^p\log n)$. If $f(n)=\Omega(n^{p+\epsilon})$ and $af(n/b)\le cf(n)$ for some fixed $c<1$ eventually, the answer is $\Theta(f(n))$. A logarithmic gap is not the polynomial gap required in the strict cases. For $a=b=2$ and quadratic toll, the regularity ratio is one half; the result is $\Theta(n^2)$.

### 3. Critical positive log powers

For $T(n)=aT(n/b)+\Theta(n^p\log^q n)$ with $p=\log_ba$ and $q>-1$, the answer is $\Theta(n^p\log^{q+1}n)$ under the standard balanced cutoff model. Reindex levels from the leaves to derive the power sum. In particular, $2T(n/2)+n\log n$ has order $\Theta(n\log^2n)$; comparing only the root toll misses one logarithmic factor.

### 4. Critical negative powers

For the same critical recurrence, $q=-1$ gives $\Theta(n^p\log\log n)$; for $q<-1$, the level series converges and positive-cost leaves give $\Theta(n^p)$. Thus $2T(n/2)+n/\log n$ and $2T(n/2)+n/\log^2n$ have different orders. Use a fixed base cutoff above one, avoiding division by $\log1=0$. These are tight growth rates, not exact identities for the count.

### 5. Additive chains

$T(n)=T(n-1)+n$ unrolls to$n(n+1)/2$ with zero base. A step$n-d$ stays in residue classes modulo$d$ and needs bases covering them. The equal-split master theorem does not apply.

### 6. Unequal splitting

For $T(x)=\sum_i a_iT(b_ix+h_i(x))+g(x)$, first solve $\sum_i a_i b_i^p=1$, with positive $a_i$ and fractions $0<b_i<1$. Subject to the theorem’s regularity and perturbation conditions, the bound is $\Theta(x^p(1+\int_1^x g(u)/u^{p+1}\,du))$. For thirds and two-thirds, $p=1$; a linear toll gives the integral $\log x$ and therefore $\Theta(x\log x)$. Floor and ceiling errors are bounded perturbations, but the subproblem sizes must still decrease beyond a fixed base cutoff. Averaging the fractions before applying an equal-split theorem changes the recurrence.

### 7. Shrinking mass

If total child fraction is less than1 and local work is linear, a geometric mass bound often gives linear total work. For fractions1/3 and1/4, the ratio is7/12. Rounding slack must still be handled in a proof.

### 8. Square-root transform

For a one-child square-root recursion, log size halves and depth is$\Theta(\log\log n)$. For two children with log toll, transform to$m=\log n$ and solve$U(m)=2U(m/2)+m$. Substitute$m$ back in the final result.

### 9. Exact bases

For$T(n)=2T(n/2)+n,T(1)=1$, exact cost is$n\log_2n+n$ on powers of two. Dropping leaf work changes exact values such as$T(8)=32$, even though asymptotic order remains unchanged.

### 10. Repeated roots

A characteristic root$r$ of multiplicity$s$ contributes$(A_0+\cdots+A_{s-1}n^{s-1})r^n$. For a double root1, use$A+Bn$. Bases determine coefficients and cannot be replaced by a growth-rate guess.

### 11. Resonant forcing

For$a_n=2a_{n-1}+2^n$, normalization by$2^n$ yields an arithmetic sequence and gives$n2^n$ with zero base. A forcing term sharing a homogeneous root requires additional polynomial factors.

### 12. Tree versus state DAG

Memoized recursion pays once per distinct state, plus dependency-processing work. Fibonacci has linear states under unit arithmetic. Repeated appearances in an expanded tree are not separate executions after cache hits.

### 13. Work versus span

Work sums parallel children; span follows the maximum child path plus the actual combine span. With a serial linear combine, balanced work is$n\log n$ while span is$n$. Speedup assumptions cannot remove a serial dependency.

### 14. Peak live storage

Depth-first retained allocations$n,n/2,n/4,...$ yield linear peak storage. Parallel children or different allocation lifetimes can change the recurrence. Total allocations over time are not peak memory.

### 15. Upper toll uncertainty

An$O(n^2)$ nonnegative toll supplies a quadratic upper bound, not necessarily quadratic tight order. Positive leaves supply a separate lower bound. Give the strongest justified interval of growth rates rather than silently strengthening the toll.

### 16. Substitution slack

When substituting an upper-bound guess, leave enough constant or lower-order slack to absorb the toll and rounding. Prove bases separately. Writing$T(n)\le cn\log n$ on both sides without closing the remaining inequality is not an induction proof.

<!-- BOUNDARY-NOTES -->

### 17. Roundings need a domain proof

Floor and ceiling subproblem sizes must be strictly smaller above a chosen cutoff and must satisfy the comparison theorem used. Exact node counts can change even when the tight order survives. Do not substitute fractional subproblem sizes into an integer program and claim exact equality.

### 18. Nonconstant arithmetic costs

A recurrence counting Fibonacci additions as unit operations is a word-cost abstraction. Fibonacci values gain linearly many bits, so ordinary bit additions over all states can require quadratic total bit work. Translate the primitive cost before using a state-count recurrence.
