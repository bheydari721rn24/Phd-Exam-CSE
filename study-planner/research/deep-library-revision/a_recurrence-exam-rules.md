## Complete summary and examination decisions

### Summary of the mathematical structure

1. A recurrence problem consists of a measured quantity, input domain, child map, local toll, stopping rule and terminal cost. Changing any of these can change an exact answer, a tight order or termination itself.
2. A positive equal-split recurrence on $N=b^h$ has the exact decomposition $a^hT(1)+\sum_{j=0}^{h-1}a^jf(b^{h-j})$. Its classification comes from summing aggregate level costs, including the terminal contribution.
3. For polynomial toll $N^d$, comparing $a$ with $b^d$ separates increasing, constant and decreasing aggregate level work. A tight conclusion requires a matching lower bound, not only an upper envelope.
4. At critical exponent $p=\log_ba$, toll $N^p(\log N)^k$ reduces to a sum of $r^k$. The three thresholds are $k>-1$, $k=-1$ and $k<-1$; the middle case produces a double logarithm.
5. A halving chain, a full binary tree and a reused dependency graph can have the same depth but different executed work. Count actual computed states and actual repeated calls separately.
6. A square root halves the logarithm. A subtract-one step decrements the input. A subtract-square-root step decreases its square-root potential by a bounded amount. These maps require different analyses.
7. Unequal fixed-ratio branches have a critical exponent determined by $\sum_i a_ib_i^p=1$. A directly justified level sum or induction envelope often proves the answer without invoking a more general theorem.
8. Exact finite sums retain bases and endpoint corrections. Replacing a finite geometric sum by its limit or replacing merge toll $n-1$ by $n$ preserves some broad orders but changes exact values.
9. Multiplicative recurrences expand into products. Positive logarithmic normalization can turn them into additive equations, but constant-factor changes inside an unbounded exponent can destroy a claimed $\Theta$ equivalence.
10. For random child sizes, condition on the size distribution and apply a pointwise bound before averaging. Expected cost is not generally cost evaluated at expected size.

### Forty detailed examination decisions

#### Decision 1. Identify the original variable before doing arithmetic

Write down whether $n$ denotes original input size, logarithmic input, recursion depth or a sequence index. If $N=2^n$, the expression $n2^n$ means $N\log_2N$. If $N=2^{2^n}$, it means $\log_2N\log_2\log_2N$. A correct algebraic answer in the transformed index can still be a wrong answer to the original-size question. Record both substitution identities before comparing options.

#### Decision 2. Verify the stopping region before solving the recurrence

Every child must eventually enter a declared base. The map $n\mapsto\sqrt n$ fixes one, so a rule that recursively processes one does not terminate. The map $n\mapsto\lfloor n/2\rfloor$ can reach zero, so a singleton-only base may be insufficient if zero is not handled. A fixed positive base cost affects exact totals through the number of leaves. The solution starts by verifying the mathematical domain, rather than treating bases as decoration.

#### Decision 3. Distinguish an equality from an algorithmic upper inequality

If an algorithm only proves $T(n)\le2T(n/2)+O(n)$, solving the envelope gives an upper bound. It does not prove that the algorithm always executes two children or pays a linear toll. A tight answer needs compulsory work on a relevant input family or an explicitly positive exact recurrence. Preserve the meaning of the source's $O$ notation; changing it silently into $\Theta$ invents evidence.

#### Decision 4. Test exact candidates against the seed and the step

A candidate for a one-step sequence is fully verified by its seed and its defining recurrence. For a second-order sequence, check both initial values and the recurrence. Failing a seed refutes an exact expression immediately, even if its asymptotic order is right. For example, $3\cdot2^n$ and $3(2^n-1)$ differ by a constant but only the latter satisfies the zero seed in the affine family.

#### Decision 5. Compute node multiplicity and local cost separately

For $a$ equal children shrinking by $b$, depth $j$ has $a^j$ nodes and per-node size $N/b^j$. The aggregate toll is their product with the stated cost function. One child with linear toll yields a geometric series; two half-size children yield constant linear work per level; four yield increasing linear work per level. A diagram that shows only changing input size omits half of the cost model.

#### Decision 6. Include leaves in exact tree totals

At input $N=2^h$ with two children, there are $N$ singleton leaves. If each costs three, they contribute $3N$, as in the exact value 256 at input 32. Ignoring them produces 160, which counts only internal work. Leaves may be lower order, of the same order, or the source of the dominant lower bound. Their relevance must be determined, not assumed away.

#### Decision 7. Separate depth from total work

Halving gives logarithmic depth, but a binary tree has exponentially many nodes in that depth. A linear-toll binary recurrence costs $\Theta(N\log N)$, while a linear-toll chain costs $\Theta(N)$. A subtract-one chain with squared toll costs cubic work despite having only one child. Depth measures one path; work sums every executed call and its local operations.

#### Decision 8. Apply the polynomial Master cases only to their stated shape

The usual theorem requires fixed $a\ge1$, fixed $b>1$, children of equal ratio and an appropriate nonnegative toll. A subtract-one, square-root or unequal-ratio recurrence is not in that form. The expression $T(n/4)+T(3n/4)$ cannot be replaced by $2T(n/2)$ just because both split total size $n$. First prove a valid transformation or use a different method.

#### Decision 9. Calculate the branching exponent in the correct base

The exponent is $p=\log_ba$, where $a$ is multiplicity and $b$ is size reduction. Two children of one-third size give $p=\log_32$, not $\log_23$. Four half-size children give exponent two. The exponent need not be an integer. To compare a toll $n^d$, evaluate $a/b^d$ or compare $d$ directly with $p$; no approximate decimal is required in many questions.

#### Decision 10. Use polynomial gaps where the theorem requires them

A leaf-case hypothesis often asks for $f(n)=O(n^{p-\varepsilon})$ for some fixed $\varepsilon>0$. Being smaller than $n^p$ by one logarithm is not a polynomial gap. The critical reciprocal-logarithm cases must be handled by the exact level sum or a theorem that explicitly covers them. An argument that simply calls $n^p/\log n$ a lower-order polynomial toll misclassifies its extra double logarithm.

#### Decision 11. Remember the negative-one logarithmic threshold

At the critical exponent, the normalized sum is $\sum r^k$. For $k>-1$, it grows as $h^{k+1}$; for $k=-1$, it grows as $\log h$; for $k<-1$, it stays bounded. With $h=\Theta(\log n)$ these become the three stated original-size classes. Defining the toll only beyond a fixed threshold avoids singular values for negative powers. This rule follows from an actual finite sum, not a memorized extension without conditions.

#### Decision 12. Check regularity in the root-dominated case

Polynomially large toll alone is insufficient. The condition $af(n/b)\le cf(n)$ for fixed $c<1$ prevents child tolls from repeatedly overwhelming the root. In the alternating quadratic/cubic example, the ratio at odd depths is $n/4$, so the condition fails. The actual total is cubic although the root toll is quadratic on half the inputs. Test the inequality algebraically instead of assuming every polynomial-looking toll is smooth.

#### Decision 13. Prove a lower bound explicitly

The root toll often proves a root-dominated lower bound. Positive leaves can prove a leaf-dominated lower bound. A critical case needs many comparable levels, or an equivalent exact sum. An upper induction on $Cn^d$ cannot by itself establish $\Theta(n^d)$. In the polylogarithmic chain, keeping its first half of levels gives the missing cubic-logarithm lower bound directly.

#### Decision 14. Repair an induction hypothesis when the leading term cancels

For $T(n)=2T(n/2)+n$, a guess $T(n)\le Cn$ gives $Cn+n$, which never closes. This failure is mathematical: the true answer needs a logarithmic factor. For a correct but delicate order, strengthen the envelope with lower-order slack, cover bases and recheck the recurrence. Do not increase a fixed constant to absorb an unbounded number of additive contributions.

#### Decision 15. Choose the induction constant from the slack

If the child squared-size coefficient is $q<1$, an upper envelope $Cn^2$ requires $Cq+1\le C$, or $C\ge1/(1-q)$. The one-quarter/three-quarter example has $q=5/8$ and threshold $8/3$. The two-half/three-third weighted example has $q=5/6$ and threshold six. Increase the constant further to cover bases; its algebraic threshold does not replace that initial check.

#### Decision 16. Conserve the correct quantity in unequal trees

Children whose sizes sum to their parent conserve linear mass at complete levels. They generally do not conserve squared size: the one-quarter/three-quarter split contracts squared mass by $5/8$. Linear toll can therefore accumulate a depth factor while quadratic toll forms a bounded geometric sum. The exponent on the toll determines which level quantity must be added. A mass diagram must label whether its numbers are sizes, squares or costs.

#### Decision 17. Distinguish complete from partly terminated levels

In an unequal tree, short branches terminate before long ones. Counting every depth as a full size-$n$ level overestimates the later internal work and can corrupt an exact expression. For a tight linear-toll argument, use an initial range of guaranteed complete levels for the lower bound and the maximum branch depth for the upper bound. Leaf sizes and base costs are then handled separately. This proves the order without asserting equal-depth leaves.

#### Decision 18. Keep fixed ratios fixed in the asymptotic claim

The constants in the unequal-tree proof depend on $\min(\alpha,\beta)$ and $\max(\alpha,\beta)$. If one ratio tends to zero with input size, the complete-level count and maximum-depth estimates may cease to be uniform. A recurrence with variable proportions requires its own analysis. A hypothesis described as a fixed positive constant must not later be selected as $1/n$ to justify an answer.

#### Decision 19. Bound rounding errors rather than merely dismissing them

For floor-square-root recursion, the transformed error per child is at most one and its cumulative effect is less than two. This proves enough comparable levels for the tight order. For balanced integer splitting, exact floor/ceiling recurrences produce different finite totals away from powers of two. Bounded perturbation theorems have hypotheses; arbitrary child maps are not justified by saying rounding never matters.

#### Decision 20. Do not apply a power-of-two exact formula to every integer

The identity $T(n)=n(3+\log_2n)$ in the balanced exact problem is specified on powers of two. At other sizes, a rounded split must be provided before an exact evaluation is meaningful. For balanced merge comparisons on all integers, use $n\lceil\log_2n\rceil-2^{\lceil\log_2n\rceil}+1$ with zero singleton cost. Exact domains and asymptotic classifications are different pieces of information.

#### Decision 21. Change variables in the argument, toll and base together

For $T(n)=4T(\sqrt n)+\log n$, using $m=\log_2n$ produces $S(m)=4S(m/2)+m$ and transforms the base $n\le4$ into $m\le2$. Forgetting the toll transformation or the new stopping region gives a different recurrence. After solving for $S$, substitute back to obtain a squared logarithm, not a quadratic polynomial in the original input.

#### Decision 22. Distinguish square-root shrink from subtract-square-root shrink

The maps $n\mapsto\sqrt n$ and $n\mapsto n-\sqrt n$ have very different rates of progress. The first becomes halving after taking a logarithm; the second has $\Theta(\sqrt n)$ depth by a square-root potential. Parentheses and subtraction signs determine the recurrence class. Read the exact child expression before selecting a familiar formula from the options.

#### Decision 23. Keep logarithm bases in exact numerical answers

Changing a fixed log base preserves asymptotic order but multiplies exact tolls by constants. The problem $T(16)=T(8)+\log_2^316$ evaluates to 101 only with the stated base-two toll and seed. A natural-log computation would have a different numerical total. Use base conversion when necessary, and distinguish $\log^3n=(\log n)^3$ from $\log(n^3)=3\log n$.

#### Decision 24. Subtract prefix equations with the correct starting index

For $a_{n+1}=c\sum_{i=0}^{n}a_i$, subtraction gives $a_{n+1}=(c+1)a_n$ only for $n\ge1$, while $a_1=ca_0$. The first transition is exceptional. With $c=3$ and $a_0=1$, the fifth term is $3\cdot4^4=768$, not $4^5$ or a power of three. State the index range of every derived equation.

#### Decision 25. Separate a term from its prefix sum

If $P_n=\sum_{i=0}^{n}a_i$ and $a_{n+1}=3P_n$, then $P_{n+1}=4P_n$. The prefix and the individual term have different initial values and formulas. For the multiplier-one authentic problem, $c_0=c_1=1$ while subsequent terms double. The generating function's first coefficient therefore detects a mistaken extension of the geometric formula at index zero.

#### Decision 26. Treat a generating function as an exact coefficient identity

Formal power series allow algebraic coefficient comparison without an analytic convergence claim. For $(1-x)/(1-\alpha x)$, the coefficient of $x$ is $\alpha-1$, so the seed determines $\alpha=2$ immediately. If the derivation also interprets the series as an analytic function, state its convergence region. A denominator root or growth factor alone does not excuse checking the numerator and initial coefficients.

#### Decision 27. Repeated characteristic roots require polynomial factors

The recurrence with characteristic polynomial $(r-2)^2$ has solution $(A+Bn)2^n$. A single geometric term cannot satisfy arbitrary two seeds. Normalizing by $2^n$ turns the recurrence into constant successive differences and independently derives that linear factor. Both $A$ and $B$ must be fixed from the two supplied values. A characteristic-root calculation without initial conditions is incomplete.

#### Decision 28. Use products for changing multiplicative coefficients

When $T_n=a_nT_{n-1}$, the exact solution is $T_0\prod_{j=1}^{n}a_j$. It is not a sum of the coefficients or a fixed power of the last coefficient. With $a_j=2^j$, the exponent is the triangular sum $n(n+1)/2$. Logarithms convert this product to an additive recurrence only when the values are positive; a zero seed produces the zero sequence instead.

#### Decision 29. Preserve finite corrections in geometric and weighted sums

The identity $\sum_{j=1}^n j/2^j=2-(n+2)/2^n$ has a nonzero tail correction. Multiplying by $2^n$ yields $2^{n+1}-n-2$, not $2^{n+1}$. Similarly, four-child linear-toll work is $2\cdot4^n-2^n$. Infinite limits classify growth but do not supply exact finite answers. The requested output determines whether a correction can be omitted.

#### Decision 30. Normalize only by nonzero products

For $T_n=a_nT_{n-1}+b_n$, dividing by $P_n=\prod a_j$ is valid only if none of the included multipliers is zero. A zero multiplier resets the recurrence to its toll at that index; restart afterward. Signed coefficients can create cancellation and invalidate positive-work lower bounds. The method's algebraic conditions are part of the solution, not optional qualifications.

#### Decision 31. Compare exponential candidates by ratios

If the exact answer is $2^{n(n+1)/2}$, neither $2^{n^2}$ nor $2^{n^2/2}$ is tightly equivalent. Their exponent differences are unbounded, causing the corresponding ratios to diverge or vanish. A leading polynomial term in an exponent cannot be dropped as if it were an ordinary additive lower-order term outside the exponential. Taking logarithms helps compare, but returning to the original ratio decides $\Theta$ equivalence.

#### Decision 32. Reduce modular recurrences before generating huge values

For a parity question, work in residues modulo two. The authentic second-order recurrence becomes $p_n=p_{n-1}+p_{n-2}$ modulo two. Its pair state cycles through three configurations. Anchor the cycle at the supplied indices, then count matching residues in the requested closed interval. A period without a phase is not enough to identify which distant terms are even.

#### Decision 33. Respect inclusive interval endpoints

Counting even recurrence terms from index 100 through 113 includes fourteen positions, not thirteen. The even indices are $102,105,108,111$, while 114 is excluded. A floor-difference formula should use the integer just before the lower endpoint: $\lfloor113/3\rfloor-\lfloor99/3\rfloor$. Writing down the actual selected indices is a useful finite check against endpoint errors.

#### Decision 34. Model a sampled pivot by its rank guarantee

A median of $2\sqrt n+1$ sampled distinct keys guarantees roughly $\sqrt n$ keys on each side of the global partition. It does not guarantee two equally sized global partitions. Sorting the sample and scanning the partition has linear-order toll, while the possible extreme branches have orders $\sqrt n$ and $n-\sqrt n$. A faithful worst-case model maximizes over allowed ranks before adopting an extreme-split shorthand.

#### Decision 35. Do not infer simultaneous worst cases without justification

An upper recurrence may add the separate worst costs of both children. That bounds the parent, but equality requires an input arrangement that can realize those child cases together. Pivot, partition and merge models need this distinction. The authentic quicksort variant asks for the permitted worst-split abstraction, not a proof that every input realizes it. Declare when a displayed tree is a mathematical recurrence model or an illustrative input.

#### Decision 36. Reuse requires identity of state, not equality of size

Two half-size subproblems may be different arrays or states and cannot automatically share a result. When the entire requested state and output are identical, memoization can replace one executed call by a lookup. This changes a two-child recurrence to a one-child recurrence in the repeated-state example. Include lookup and copying costs if they are not bounded, and distinguish executed edges from reference edges in the diagram.

#### Decision 37. State the arithmetic model for Fibonacci

Naive call count is $2F_{n+1}-1$, so its unit-cost work is $\Theta(\phi^n)$. Memoization computes each state once and uses $\Theta(n)$ unit additions. If additions are charged by bit length, the integer at index $k$ has $\Theta(k)$ bits, and straightforward memoization takes $\Theta(n^2)$ bit work. Neither arithmetic model changes merely because the program is written recursively.

#### Decision 38. Condition on random child sizes before taking expectations

The expected recurrence includes $\mathbb E[T(J)]$. Generally it differs from $T(\mathbb E[J])$, as a quadratic-cost example demonstrates. A valid induction first bounds every possible smaller-state cost, then averages those bounds with the actual probabilities. Uniform-pivot expected shrink and adversarial worst-case shrink are separate hypotheses. The distribution, base cases and source of the lower work must all be stated.

#### Decision 39. Preserve ambiguity in authentic upper-bound options

The original square-root question prints three valid $O$ upper bounds. Its tight answer is $\Theta(\log n\log\log n)$, and option 1 is the smallest listed upper bound. Options 2 and 3 are looser but mathematically true. The final option $O(\log\log n)$ is false. A worked solution must explain this wording limitation instead of inventing mutually exclusive truth values or silently replacing the printed options.

#### Decision 40. Reconcile sources and state remaining scope

Read the actual formula, hypotheses, base region and edition header before borrowing a result. A printed division by $\log\log x$ in the reviewed Akra–Bazzi example conflicts with its own integral and is corrected to multiplication. Exact merge size-toll work is separated from comparison work. This chapter covers its declared recurrence families; it does not claim an exhaustive global course census, every nonlinear recurrence or a guaranteed outcome on unseen examinations. The evidence ledger states actual reading and independently checked cases.
