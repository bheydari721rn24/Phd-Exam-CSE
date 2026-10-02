### Problem 1. A recurrence does not yet specify a function

**Original · Domains and base cases.** An author writes $T(n)=T(⌈2n/3⌉)+1$ for every integer $n>1$, with $T(1)=1$. Diagnose the model and repair it.

**Solution.** At two the child size is $⌈4/3⌉=2$, so the definition demands $T(2)=T(2)+1$, impossible for a finite value. The recurrence has a familiar constant reduction only at sufficiently large inputs. Set a base cost at two as well, and apply the recursive rule only for $n ≥ 3$. For those inputs the ceiling is at most $n−1$, so strong induction gives a unique finite sequence. A constant-size base range does not change its logarithmic asymptotic depth, but the original self-reference was mathematically invalid. Check small inputs before applying any solution theorem.

### Problem 2. One branch, two calls, or a cached result

**Original · Model derivation.** Compare a half-size recursion called twice sequentially, a conditional selecting one half-size call, and one computed half-size result reused twice. Assume a unit local toll and constant positive bases.

**Solution.** The first model is $T(n)=2T(n/2)+1$, yielding linear work from its binary tree. The conditional executes one child, so its model is $T(n)=T(n/2)+1$ and its work is logarithmic. Reusing an already computed result also executes one recursive call, with only constant local reuse work, so it follows the second model. A source expression containing the child function twice may or may not execute it twice, depending on whether the result is stored. Derive the execution structure before selecting a branching coefficient. The number of distinct subproblem sizes does not equal the number of uncached calls.

### Problem 3. Why an upper toll does not give a tight bound

**Course-derived · Stanford's explicit upper-bound formulation; original counterexample.** Does $T(n)=2T(n/2)+O(n)$ force $T(n)=Θ(n log n)$?

**Solution.** No. Set the actual toll to one and the base at one to one. This is a permitted $O(n)$ toll, but the exact recurrence has solution $2n−1$ on powers of two: its binary tree has $n$ leaves and $n−1$ internal nodes. The standard linear envelope gives an $O(n log n)$ upper bound, but no matching lower bound follows from that information. If the actual toll is bounded below by a positive multiple of $n$ at each sufficiently large call and bases are positive, level sums give the tight result. The missing lower assumption changes the logical strength of the conclusion.

### Problem 4. Binary search with a costly representation

**Course-derived · MIT Recitation 3 binary-search exercise, extended cost model.** Compare index-based binary search with an implementation that copies the chosen half of the input array before each recursive call.

**Solution.** Index boundaries take constant local work, giving $T(n)=T(⌊n/2⌋)+Θ(1)$ and $Θ(log n)$ time. Copying a half costs $Θ(n)$ at a size-$n$ node, so the second model is $U(n)=U(⌊n/2⌋)+Θ(n)$. Its copied sizes form a geometric sequence $n,n/2,n/4,…$, summing to linear time. The second implementation still makes logarithmically many comparisons, but its total time is linear in this representation. Naming the algorithm is insufficient to determine all resource costs; identify the operation being counted and whether the data are copied or viewed.

### Problem 5. An exact additive chain

**Course-derived · MIT additive recurrence exercise, exact toll and base.** Solve $T(0)=4$ and $T(n)=T(n−1)+3n+2$.

**Solution.** Expand through the base: $T(n)=4+∑_{j=1}^{n}(3j+2)=4+3n(n+1)/2+2n$. Thus the exact answer is $(3n^2+7n+8)/2$. Its value at zero is four. Subtracting its value at $n−1$ gives exactly $3n+2$, proving it satisfies every recurrence step; uniqueness supplies completeness. The quadratic leading term gives $Θ(n^2)$, while omitting the initial four would produce a different exact sequence. An asymptotic answer and an exact answer have different obligations.

### Problem 6. Additive power thresholds

**Original · Integral bounds.** For $T(n)=T(n−1)+n^r$, $T(0)=1$, classify the growth for fixed real $r$.

**Solution.** The exact expression is $1+∑_{j=1}^{n}j^r$. If $r>−1$, upper and lower rectangle comparisons with $x^r$ give order $n^{r+1}$; for nonnegative $r$, the last-half lower bound is an alternative proof. At $r=−1$, the sum is harmonic and grows logarithmically. If $r<−1$, its infinite positive sum converges, while the initial one keeps a positive lower bound, giving constant order. The often-used exponent-plus-one rule has a domain restriction. Fractional tolls here define a mathematical cost model; they need not be literal integer operation counts.

### Problem 7. Exponential size from a linear-depth tree

**Course-derived · MIT's double-call decrement exercise; exact base.** Solve $T(0)=1$ and $T(n)=2T(n−1)+1$.

**Solution.** Divide the normalized expression by $2^n$, or expand all calls. The result is $T(n)=2^n+∑_{j=1}^{n}2^{n−j}=2^{n+1}−1$. At depth $j$ there are $2^j$ nodes, and the depth is $n$. The longest path is linear, but the node population is exponential. Substitution verifies $2(2^n−1)+1=2^{n+1}−1$. A linear call-stack bound is therefore compatible with exponential total work. The exact leading coefficient also depends on the specified base value.

### Problem 8. A summation factor with variable coefficients

**Course-derived · Princeton Exercise 2.13, independently derived.** Solve $A_0=1$ and $A_n=(n/(n+1))A_{n−1}+1$.

**Solution.** The product of multipliers through $n$ telescopes to $1/(n+1)$. Set $B_n=(n+1)A_n$. Multiplying the recurrence by $n+1$ gives $B_n=B_{n−1}+n+1$, with $B_0=1$. Hence $B_n=1+n(n+3)/2=(n+1)(n+2)/2$, so $A_n=(n+2)/2$. The initial value checks, and direct substitution gives the same formula at every step. Using a constant-coefficient characteristic equation would be inappropriate because the multiplier depends on $n$; normalization restores a simple additive recurrence.

### Problem 9. A zero multiplier resets a chain

**Original · Summation-factor boundary.** Suppose $A_0=10$, $A_1=2A_0+3$, $A_2=0A_1+5$, and $A_n=2A_{n−1}+1$ for $n ≥ 3$. Find an exact expression from index two onward.

**Solution.** The first value is twenty-three, but the zero multiplier makes $A_2=5$, independent of everything before it. Restart at index two. Expansion of the later recurrence gives $A_n=2^{n−2}·5+(2^{n−2}−1)=6·2^{n−2}−1$. At two this is five, and its subsequent difference equation checks directly. Dividing by the product of multipliers from zero would divide by zero, so the summation-factor formula cannot cross that step. A reset is part of the recurrence's exact structure, not a negligible asymptotic adjustment.

### Problem 10. Distinct characteristic roots and cancellation

**Original · Linear recurrence.** Solve $A_n=3A_{n−1}−2A_{n−2}$ with $A_0=4$, $A_1=6$. Then change the initial pair to $(4,4)$.

**Solution.** The characteristic polynomial factors as $(λ−1)(λ−2)$. Thus $A_n=u+v2^n$. The initial equations are $u+v=4$ and $u+2v=6$, giving $u=v=2$ and $A_n=2+2^{n+1}$. For the alternative pair, the equations give $v=0$, so the sequence is the constant four. The largest root is two in both recurrences, but its coefficient vanishes in the second solution. Initial values can remove a dominant mode. Check both base equations and the recurrence instead of assigning exponential growth from the characteristic polynomial alone.

### Problem 11. A repeated root needs another factor

**Original · Repeated-root equation.** Solve $A_n=4A_{n−1}−4A_{n−2}$, with $A_0=1$ and $A_1=4$.

**Solution.** The characteristic polynomial is $(λ−2)^2$. The independent solutions are $2^n$ and $n2^n$, so use $(u+vn)2^n$. The bases yield $u=1$ and $2(1+v)=4$, giving $v=1$. The answer is $(n+1)2^n$. Substituting verifies that $4n2^{n−1}−4(n−1)2^{n−2}=(n+1)2^n$. The second solution's linear factor is necessary to accommodate arbitrary two base values. Treating a repeated root as two identical exponentials would collapse the two-dimensional solution family to one dimension.

### Problem 12. Resonance in a forced equation

**Original · Nonhomogeneous recurrence.** Solve $A_n=2A_{n−1}+2^n$, $A_0=3$.

**Solution.** Let $B_n=A_n/2^n$. The recurrence becomes $B_n=B_{n−1}+1$, with $B_0=3$. Therefore $B_n=n+3$ and $A_n=(n+3)2^n$. A particular solution of the form $c2^n$ cannot work: subtracting twice its predecessor gives zero, while the forcing is nonzero. Multiplication by $n$ provides the needed independent shape. This is the elementary resonance rule in a form whose normalization and exact initial coefficient are completely visible.

### Problem 13. Count a complete recursion level

**Course-derived · Stanford solved concept-check tree, independently explained.** For $T(n)=5T(n/4)+2n$, determine node count at depth four, size at depth five, and internal cost at depth $j$.

**Solution.** Each node creates five children, so depth four contains $5^4=625$ nodes. Each step divides size by four, so every depth-five node has size $n/4^5=n/1024$. At depth $j$, multiply node count by each node's toll: $5^j·2(n/4^j)=2n(5/4)^j$. The total increases geometrically down the internal levels. Positive leaves contribute order $n^{log_4 5}$, consistent with the leaf-dominated master result. The reciprocal ratio $(4/5)^j$ would incorrectly combine branching and shrinking in reverse. These statements concern existing internal levels; a level below the stopping depth does not exist.

### Problem 14. Exact balanced level costs

**Original · Tree identity.** Solve $T(1)=2$ and $T(n)=2T(n/2)+n$ on powers of two.

**Solution.** Let $h=log_2 n$. Each of the $h$ internal levels contributes exactly $n$; there are $n$ leaves at cost two each. Thus $T(n)=n log_2 n+2n$. At one the log term is zero and the value is two. Substitution gives $2[(n/2)(log_2 n−1)+n]+n=n log_2 n+2n$. This proves both the exact identity and its order $Θ(n log n)$. Counting the leaves as another linear toll level would give the wrong coefficient because their base cost is two, not the internal toll convention.

### Problem 15. The root dominates a geometric tree

**Course-derived · Cornell's quadratic binary-tree example; exact base.** Solve $T(1)=1$ and $T(n)=2T(n/2)+n^2$ for powers of two.

**Solution.** Internal levels cost $n^2, n^2/2,…,n^2/2^{h−1}$. Their sum is $2n^2(1−1/n)=2n^2−2n$. The leaves contribute $n$, giving $T(n)=2n^2−n$. The exact value satisfies both the base and recurrence. The ratio one half makes the total a constant multiple of the root contribution, so the depth is not another multiplicative log factor. Adding a logarithm merely because recursion has logarithmic depth would overestimate the tight answer.

### Problem 16. Leaves dominate despite cheap internal calls

**Course-derived · MIT four-way half-size exercise, positive exact toll.** Classify $T(n)=4T(n/2)+3n$, with positive constant bases.

**Solution.** The critical exponent is $log_2 4=2$, while the toll exponent is one. The gap is a full power, satisfying leaf dominance with $ε=1$. At depth $j$, internal contribution is $3n·2^j$, which grows to order $n^2$ near the bottom. There are $n^2$ leaves with constant positive cost, establishing a matching lower bound. Thus $T(n)=Θ(n^2)$. Reducing the internal linear toll to a constant cannot beat that leaf population; changing the branching pattern is necessary for a smaller exponent in this model.

### Problem 17. Fractional tolls and exact exponents

**Course-derived · Stanford's fractional-power concept check.** Classify $T(n)=3T(n/81)+10n^{1/4}$ on an ideal admissible grid.

**Solution.** The critical exponent is $log_{81}3=1/4$, because $81^{1/4}=3$. The toll is exactly balanced, so $T(n)=Θ(n^{1/4}log n)$. The regularity ratio is one, not less than one, which is consistent with balanced work rather than root dominance. A quarter-power toll is not a linear toll, and rounding its exponent to a decimal approximation is unnecessary. For a mathematical real-size grid, fractional local weights are legitimate; a literal machine operation count would need an appropriate integer-cost interpretation.

### Problem 18. A parameter phase transition

**Course-derived · Cornell's variable-shrink-factor discussion; changed branching count.** Classify $T(n)=9T(n/b)+n^2$ for fixed $b>1$.

**Solution.** Compare $p=log_b 9$ with two. Equality occurs at $b=3$. If $1<b<3$, the critical exponent exceeds two and leaves dominate, giving $Θ(n^{log_b 9})$. At three, every internal level contributes order $n^2$, giving $Θ(n^2 log n)$. If $b>3$, the regularity ratio is $9/b^2<1$, so the answer is $Θ(n^2)$. State the threshold and valid parameter domain; a shrink factor of one would not reduce the problem. The answer changes by a logarithm at equality rather than jumping directly between pure powers.

### Problem 19. A correct order with a failed induction

**Course-derived · Cornell's slack technique; changed recursive argument.** Prove a linear upper bound for $T(n)=2T(n/2)+1$, $T(1)=1$.

**Solution.** A bare hypothesis $T(k) ≤ Ck$ yields $T(n) ≤ Cn+1$, which does not close for any fixed $C$. Strengthen the claim to $T(k) ≤ Ck−1$. Then the parent is at most $2(Cn/2−1)+1=Cn−1$. The base requires $1 ≤ C−1$, so choose $C=2$. This yields $T(n) ≤ 2n−1$, in fact an equality for the exact recurrence. The asymptotic guess was correct; the failed proof lacked a constant amount of slack. This pattern is different from a recurrence whose balanced linear toll truly requires an extra logarithm.

### Problem 20. A wrong order exposed by constants

**Course-derived · CMU's seven-way balanced example; independent proof diagnosis.** Why cannot $T(n)=7T(n/7)+n$, $T(1)=0$, be proved linear by substituting $Cn$?

**Solution.** The attempted parent bound becomes $7(Cn/7)+n=(C+1)n$. The coefficient increases at each expansion, so it is not a fixed constant. At depth $log_7 n$, each internal level contributes $n$, giving the exact result $n log_7 n$ on powers of seven. The zero leaves do not contribute here, but the internal levels alone prove the logarithmic factor. This exception to the default positive-base convention is stated explicitly. Induction with $n log_7 n$ closes exactly, showing how a failed linear guess can suggest the missing factor.

### Problem 21. A logarithmic critical toll

**Course-derived · MIT's extended balanced case.** Classify $T(n)=2T(n/2)+n log_2 n$, with a constant base at one.

**Solution.** Let $n=2^h$. The cost at depth $j$ is $n(h−j)$, so internal work is $n(h+(h−1)+…+1)=nh(h+1)/2$. Add the linear leaf contribution. The total is $Θ(n(log n)^2)$. The classical balanced case with toll $Θ(n)$ alone does not cover this toll, but the extended case with log exponent one does. The explicit arithmetic sum proves the added logarithm and prevents treating the toll as a polynomially larger function.

### Problem 22. A reciprocal-log boundary

**Course-derived · Cornell's uncovered recurrence, tightened independently.** Solve the order of $T(n)=2T(n/2)+n/log_2 n$, with bases through two and inputs powers of two.

**Solution.** Normalize at $n=2^h$ by dividing by $n$. The relation becomes $U(h)=U(h−1)+1/h$, starting at $h=1$. Therefore $U(h)=U(1)+H_h−1$, giving $T(n)=Θ(n log log n)$. The classical leaf case cannot be used: $n/log n$ is not polynomially below $n$. Comparing to a larger linear-toll envelope does give $O(n log n)$, but that is not tight. The harmonic depth sum provides the missing precision.

### Problem 23. Negative logarithmic exponents have a threshold

**Original · Complete critical table.** Classify $T(n)=4T(n/2)+n^2/(log_2 n)^{3/2}$, with a base range through two.

**Solution.** The critical exponent is two and the log exponent is negative three halves, below negative one. Reversing the depth index gives normalized total $1+∑_{r=1}^{h}r^{−3/2}$. That sum converges to a finite positive limit, so the total is $Θ(n^2)$. The leaves alone already force this order. Blindly adding one to the log exponent would predict $n^2/√log n$, smaller than the compulsory leaf cost. The finite base threshold prevents evaluating the reciprocal logarithm at one.

### Problem 24. A noninteger logarithmic exponent above the boundary

**Original · Integral power sum.** Classify $T(n)=2T(n/2)+n/√log_2 n$, with bases through two.

**Solution.** The normalized depth sum is $1+∑ r^{−1/2}$. An integral comparison with $1/√x$ puts it between positive constant multiples of $√h$. Hence the answer is $Θ(n√log n)$. This is a critical exponent with log exponent negative one half, which lies above negative one. It is neither a classical leaf case nor the harmonic boundary. Comparing only the sign of the log exponent would miss the distinction between this recurrence and the previous one.

### Problem 25. Growth alone does not imply regularity

**Original · Oscillating toll counterexample.** On $n=2^h$, let $T(1)=1$, $T(n)=2T(n/2)+f(n)$, and let $f(n)$ be $n^2$ at even $h$ and $n^3$ at odd $h$. Can root dominance be inferred from $f(n) ≥ n^2$?

**Solution.** For even $h ≥ 2$, the child exponent index is odd, so the two immediate child tolls already total $2(n/2)^3=n^3/4$. The parent's toll is only $n^2$, yielding $T(n)/f(n) ≥ n/4$. The ratio is unbounded along those inputs; $T(n)=Θ(f(n))$ is false. Regularity would require $2f(n/2)/f(n)$ bounded by one fixed number below one, while here it equals $n/4$. A polynomial lower estimate for the toll verifies only one of the root-case hypotheses and cannot replace the other.

### Problem 26. A theorem can fail while its conclusion remains true

**Original · Comparison envelopes.** Suppose an equal-size recurrence has nonnegative toll $f(n)$ with $n^2 ≤ f(n) ≤ 10n^2$, but the ratio $2f(n/2)/f(n)$ sometimes exceeds one. Determine the order for $T(n)=2T(n/2)+f(n)$.

**Solution.** Use two exact envelope recurrences with tolls $n^2$ and $10n^2$, and base costs bounding the actual bases. Comparison induction sandwiches the actual cost between them. Each envelope has order $n^2$, as shown by its geometric level sum, so the actual cost has the same order. The displayed regularity condition may fail for the oscillating toll, preventing that direct theorem application. Nevertheless, its bounded monomial envelopes give an independent proof. Failure of a sufficient hypothesis does not imply failure of the conclusion itself.

### Problem 27. Exact rounding changes lower terms

**Course-derived · Princeton's exact split-count theme; actual comparison toll.** Compute the balanced merge worst-case comparison counts at $n=5$ and $n=8$, and give the exact general formula.

**Solution.** For five, split into two and three. The values at two and three are one and three, so $C(5)=1+3+4=8$. For eight, the formula with $h=3$ gives $C(8)=8·3−8+1=17$. Generally, the balanced tree's leaf depths sum to $nh−2^h+n$; subtracting one for each of its $n−1$ internal nodes gives $C(n)=nh−2^h+1$, where $h=⌈log_2 n⌉$. A reference formula using toll $n$ instead gives a larger answer by $n−1$. Exact rounding and the primitive being counted must both match before transferring a formula.

### Problem 28. A ceiling with an additive offset

**Original · Termination and rounding.** Analyze $T(n)=T(⌈n/2⌉+1)+1$ with bases for $n ≤ 4$.

**Solution.** For $n>4$, the child is smaller than the parent. Write the child as at most $n/2+3/2$. Subtract three from the current size: the child's shifted size is at most half the parent's shifted size. Thus after $O(log n)$ calls the input reaches the constant base region. Conversely, each step's argument is at least $n/2$, so a fixed number fewer than a constant multiple of $log n$ calls cannot reduce a large input to four. With unit local cost and positive bases, the answer is $Θ(log n)$. The additive offset changes a stopping threshold, not the order, and its harmlessness has been proved rather than assumed.

### Problem 29. Unequal ratios with total mass below one

**Course-derived · CMU selection recurrence; independent complete cost bound.** Classify an exact positive-toll model $T(n)=T(n/5)+T(7n/10)+n$ with fixed positive bases.

**Solution.** Total child size is nine tenths of the parent. Internal linear work at depth $j$ is at most $n(9/10)^j$, so all internal levels total at most $10n$. Leaf costs are also $O(n)$ because each stopping leaf has size bounded below by a positive constant and splitting does not increase total mass. The root alone costs $n$, proving the lower bound. Hence the answer is $Θ(n)$. For an upper inequality with only an $O(n)$ toll, this argument supplies $O(n)$; the actual algorithm's mandatory scan must establish its linear lower bound separately.

### Problem 30. Rounding the unequal recurrence

**Original · Explicit substitution margin.** Prove an upper linear bound when $T(n) ≤ T(⌈n/5⌉)+T(⌈7n/10⌉)+n$ above a sufficiently large fixed base threshold.

**Solution.** The two child sizes sum to at most $0.9n+2$. A naive linear hypothesis then gives at most $0.9Cn+2C+n$, which is bounded by $Cn$ once $(0.1C−1)n ≥ 2C$. Choosing $C ≥ 20$ makes the coefficient at least $0.05C$, so the condition holds for $n ≥ 40$. Choose a constant base threshold of forty, ensuring smaller children, and enlarge $C$ if needed to dominate every positive base ratio $T(k)/k$ for $1 ≤ k ≤ 40$. The same $C$ then closes every larger step. This is a complete finite-threshold proof; the ceiling terms have been retained in the inequality.

### Problem 31. Unequal conserved mass

**Course-derived · Cornell's intended unequal-tree example, corrected notation.** Classify $T(n)=T(n/3)+T(2n/3)+n$ with fixed positive bases in the ideal model.

**Solution.** The two fractions sum to one. Akra–Bazzi gives critical exponent one because $(1/3)^1+(2/3)^1=1$. The normalized toll integrand is $u/u^2=1/u$; its integral grows as $log n$. Thus $T(n)=Θ(n log n)$. This conclusion also follows by counting conserved mass across full live levels and charging the remaining levels carefully, but a longest-path estimate alone gives only an upper bound. The expression $T(n/3)+2T(n/3)$ has three equal one-third calls and describes a different tree, even though its asymptotic order happens to agree for a linear toll.

### Problem 32. A root below one for unequal branches

**Course-derived · Princeton Exercise 2.73, independently justified.** Classify $T(n)=T(n/2)+T(n/4)+n$.

**Solution.** The critical equation is $2^{−p}+4^{−p}=1$. Set $z=2^{−p}$ to get $z+z^2=1$, whose positive solution is $(√5−1)/2$. Thus $p=log_2((1+√5)/2)<1$. The linear toll exponent is larger than the critical exponent, and the Akra–Bazzi integral grows as $n^{1−p}$; multiplying by $n^p$ gives $Θ(n)$. The total child mass is three quarters, giving an independent geometric-mass proof. Computing $p$ is not required for that simpler proof, but it verifies the generalized theorem's prediction.

### Problem 33. A nontrivial critical weighted equation

**Course-derived · MIT Akra–Bazzi example, explicit evaluation.** Solve the order of $T(n)=2T(n/4)+3T(n/6)+n log n$.

**Solution.** At exponent one, $2/4+3/6=1$, so uniqueness of the decreasing characteristic expression gives $p=1$. The integrand is $(u log u)/u^2=(log u)/u$. Its integral from a fixed positive cutoff to $n$ is one half of $(log n)^2$ plus a constant. The full answer is therefore $Θ(n(log n)^2)$. Choosing one average child size would lose both multiplicities and could produce the wrong critical exponent. The integral's extra one accounts for base work even when the normalized toll integral converges in other examples.

### Problem 34. Prove an unequal quadratic envelope

**Course-derived · Stanford solved substitution concept check.** Prove $T(n) ≤ 6n^2$ for $T(n)=2T(n/2)+3T(n/3)+n^2$, assuming the fixed base interval already satisfies this bound.

**Solution.** The weighted quadratic child factor is $2/4+3/9=5/6$. Substituting the induction hypothesis gives $2·6(n/2)^2+3·6(n/3)^2+n^2=6n^2$. Thus the bound closes with equality in its envelope. The positive quadratic root toll also gives an $Ω(n^2)$ lower bound for the exact recurrence, so its order is quadratic. A guessed upper coefficient two would fail the inequality because $2(5/6)+1>2$. The constant six is an algebraic threshold, not a value chosen from numerical fitting.

### Problem 35. A nonlinear reduction becomes linear after taking logs

**Original · Change of variables.** Classify $T(n)=2T(√n)+log_2 n$ on $n=2^{2^h}$ with a fixed positive base region.

**Solution.** Set $m=log_2 n$ and $S(m)=T(2^m)$. A square-root child has new argument $m/2$, and the toll is $m$. Thus $S(m)=2S(m/2)+m$, a balanced recurrence with $Θ(m log m)$ growth. Return to the original variable: $T(n)=Θ(log n log log n)$. The admissible grid makes the transformed sequence reach its fixed base exactly. An answer expressed in $m$ is unfinished until the original variable is restored.

### Problem 36. An exponential toll is outside the integral theorem

**Course-derived · Princeton Exercise 2.71 theme; fixed branching.** Classify $T(n)=2T(n/2)+2^n$ on powers of two.

**Solution.** The root gives $T(n) ≥ 2^n$. For sufficiently large $n$, a proposed upper bound $C2^n$ gives $2C2^{n/2}+2^n ≤ C2^n$; choose $C ≥ 2$ and a fixed threshold where $2^{1−n/2} ≤ 1/2$, then enlarge $C$ for the finite base band. Thus $T(n)=Θ(2^n)$. The exponential toll fails multiplicative-interval comparability, so the stated Akra–Bazzi integral formula is not the justification. Direct substitution verifies root dominance under an appropriate condition instead of applying a theorem outside its domain.

### Problem 37. Work and span have different branching

**Original · Parallel model.** Two half-size children can execute in parallel, and combining has linear work but logarithmic span. Determine work and span.

**Solution.** Work sums all executed operations, giving $W(n)=2W(n/2)+Θ(n)=Θ(n log n)$. Span follows the slower of the concurrent children and then the combine span: $S(n)=S(n/2)+Θ(log n)$. On $n=2^h$, its tolls are $h,h−1,…,1$, whose arithmetic sum is $Θ(h^2)$, so span is $Θ((log n)^2)$. This requires a real combine algorithm with logarithmic span and sufficient available parallelism. Using the work recurrence for span would incorrectly count simultaneous children sequentially.

### Problem 38. Time does not determine live space

**Original · Storage liveness.** A sequential recursive routine makes two half-size calls. Compare constant-size frames with frames retaining local arrays proportional to their input size.

**Solution.** With constant frames, only one active root-to-leaf chain needs stack storage at a time, so the recurrence uses a maximum child rather than the sum: $M(n)=M(n/2)+Θ(1)=Θ(log n)$. If every active frame retains a local size-proportional array while recursing, the storage along a halving chain sums $n+n/2+n/4+…$, giving $Θ(n)$. Counting all nodes in the execution tree would count memory from calls that are no longer live. The result also changes if arrays are freed before recursion or shared through an explicit workspace; specify allocation lifetime before writing a storage recurrence.

### Problem 39. Memoization replaces a tree with a dependency graph

**Original · Repeated Fibonacci states.** Compare naive Fibonacci calls and a memoized implementation under unit-cost arithmetic.

**Solution.** The naive call count satisfies $N(n)=N(n−1)+N(n−2)+1$, with one call at each base. Setting $B(n)=N(n)+1$ gives the homogeneous Fibonacci relation, so $N(n)=2F_{n+1}−1$ and its order is exponential in the golden-ratio power. Memoization computes each index once: there are only $n+1$ distinct states and a constant number of dependency edges per state, giving linear arithmetic work. Recursive depth can still be linear. This distinction is about the actual execution graph. For bit complexity, additions act on growing Fibonacci integers and need a separate size-sensitive analysis.

### Problem 40. Expected size is not expected cost

**Original · Random-size boundary.** A child size is zero or two with equal probability. If its cost is squared size, compare expected cost with the cost at the expected size.

**Solution.** The expected child size is $(0+2)/2=1$. The expected cost is $(0^2+2^2)/2=2$, whereas cost at the expected size is $1^2=1$. Thus replacing $E[T(X)]$ by $T(E[X])$ loses information about the distribution. An expected algorithm recurrence must condition on the child's actual size, multiply each conditional cost by its probability, and sum. Linearity of expectation applies to sums of random costs without requiring independence, but it does not move expectation through a nonlinear function. This is the precise modeling error behind many apparently plausible average-size recurrences.
