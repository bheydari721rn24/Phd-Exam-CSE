# Algorithmic Recurrences and Solution Theorems

## Sources, prerequisites, and scope

This Week 2 Algorithms chapter assumes asymptotic notation, finite sums, logarithms, induction, and the approved chapters on algorithm cost models and invariants. It teaches how to derive, solve, and justify a recurrence; a formula without its domain and base cases is not a complete specification.

The principal written sources actually read are MIT 6.006 Recitation 3 (Erik Demaine, Jason Ku, Justin Solomon, Spring 2020); Stanford CS 161 Lecture 3 (the retrieved file identifies Winter 2026, Moses Charikar and Ellen Vitercik, adapted from Virginia Williams); CMU 15-451, Avrim Blum's Fall 2011 Lectures 2 and selected Lecture 4 passages, taught by Avrim and Manuel Blum; and Princeton's *Analysis of Algorithms*, Robert Sedgewick and Philippe Flajolet, Chapter 2 web notes. Cornell CS 3110's recursion-tree lecture and substitution recitation were also read. Tom Leighton's MIT notes supply the explicitly stated, unperturbed Akra–Bazzi theorem and its proof. The [candidate comparison and reading ledger](../reviews/a_recurrence-sources.html) records exact scopes and distinguishes a read text from a syllabus.

The chapter covers exact and asymptotic recurrence models, additive and multiplicative first-order equations, elementary constant-coefficient linear equations, summation, substitution, recursion trees, the three-case master theorem, all real logarithmic powers at the critical exponent, rounding and base-case effects, unequal fixed-ratio recurrences, an unperturbed Akra–Bazzi proof, changes of variables, and the distinction between work, stack space, and expected cost. Full divide-and-conquer algorithm designs belong to the next chapter. General generating-function theory, arbitrary nonlinear equations, and the full proof of every perturbation version of Akra–Bazzi are outside this bounded chapter. Iranian examination archives remain deferred.

Unless specified otherwise, costs are nonnegative, base costs are bounded above and below by positive constants, and logarithms in asymptotic expressions have a fixed base greater than one. An exact solution may require a particular log base; changing it inside an exact identity changes constants. Toll means the nonrecursive work at one call, excluding all recursive descendants.

## Build the recurrence before solving it

### Domain, progress, and the quantity being measured

A recurrence defines a function using previously defined values. For an integer-size cost, specify a threshold $n_0$ and base values for every $0 ≤ n ≤ n_0$. Every recursive argument above the threshold must be a nonnegative integer smaller than its parent. These conditions make strong induction applicable and give a unique value for each integer input. A ceiling can violate progress at small sizes: $⌈2n/3⌉=n$ at two, so a recurrence using that argument needs a base case through two. Termination is part of the model, even when an informal asymptotic formula looks familiar.

For a particular input $x$, the running cost is the local cost plus the sum of costs of all recursive calls actually executed. A conditional choosing one of two branches contributes one branch, not their sum. Sequential calls contribute a sum; perfectly parallel execution with enough processors contributes a maximum to span. Repeated calls to the same subproblem still count repeatedly unless an implementation really caches the result.

If $W(n)$ is the worst cost over size-$n$ inputs, replacing each child cost by its own worst value yields an upper inequality. Equality requires an input or structural reason that simultaneously realizes those worst costs. The equation $W(n)=W(k)+W(n−k)+n$ for one chosen split does not automatically describe the worst case over all possible splits. That worst case may need a maximum over the admissible split values. Conversely, a lower bound needs actual compulsory work or a realizable family of inputs, not merely an upper recurrence.

### Equality, inequalities, and asymptotic tolls

An exact model $T(n)=2T(n/2)+n$ on powers of two specifies one mathematical sequence. A model with a $Θ(n)$ toll represents any sequence whose actual toll lies between two positive constant multiples of $n$ eventually. Monotone comparison of recurrences supplies matching bounds when the child structure is fixed and coefficients are nonnegative. A model with only an $O(n)$ toll supplies an upper bound; its toll could be one instead of linear. For example, $2T(n/2)+1$ has linear cost, so an $O(n)$ toll alone cannot force $Θ(n log n)$.

Comparison is a strong-induction argument. Suppose $T$ and an envelope $U$ have the same smaller-child structure, $T$'s base values are no larger, and its local toll is no larger. Assuming $T(k) ≤ U(k)$ for all smaller arguments, nonnegative coefficients preserve the inequality at the parent. Prove the corresponding reverse comparison separately if a tight bound is requested. An envelope must recurse on itself; merely replacing the toll while retaining the original unknown children does not define an independently solvable comparison recurrence.

Derive costs in a fixed computational model. A search that recurses on an index interval may have constant local cost; slicing and copying the chosen half of a Python list introduces linear local work. Multiplication of unbounded integers is not a unit-cost operation merely because the program uses one multiplication symbol. The input size, primitive costs, branch rules, and base threshold all belong in the derivation.

## Unrolling, summation factors, and linear equations

### Additive chains and sum estimates

If $T(n)=T(n−1)+g(n)$ for $n ≥ 1$, with specified $T(0)$, repeated expansion gives $T(n)=T(0)+g(1)+…+g(n)$. Every summand corresponds to an actual enabled step; including or excluding a base toll changes an exact constant. For $g(n)=n$, the sum is $n(n+1)/2$. Pairing the first and last terms proves the arithmetic sum, while induction checks the closed form against the recurrence.

For a fixed $r>−1$, the sum of positive powers $j^r$ is $Θ(n^{r+1})$. For nonnegative $r$, an upper bound comes from at most $n$ terms bounded by $n^r$, and a lower bound comes from the last half of the terms. For $−1<r<0$, compare the decreasing function with its integral; the finite initial portion is harmless. At $r=−1$, harmonic numbers satisfy $ln(n+1) ≤ H_n ≤ 1+ln n$, using rectangles under and above $1/x$. For $r<−1$, the positive infinite series converges by the integral bound, so the finite sum is bounded above and below by constants. These thresholds prevent the false rule that every additive recurrence increases an exponent by one.

For a constant integer decrement $d>0$, expand only along that residue class: $T(n)=T(r)+g(n)+g(n−d)+…$, where the final base argument $r$ lies in the specified base interval. A fixed decrement changes constants for ordinary power tolls; a decrement that depends on $n$ can change the order and needs a new step-count argument.

### Multiplicative and variable-coefficient chains

For $T(n)=cT(n−1)+g(n)$ with a fixed positive $c$, expansion yields $c^nT(0)+∑ c^{n−j}g(j)$ over $j=1,…,n$. Dividing by $c^n$ turns the equation into a telescoping sum. In particular, $T(n)=2T(n−1)+1$, $T(0)=1$, gives $T(n)=2^{n+1}−1$. The tree has exponential size even though its longest chain is only linear in $n$.

More generally, suppose $A_n=r_nA_{n−1}+s_n$. On an interval where all $r_n$ are nonzero, set $P_0=1$ and $P_n=r_1…r_n$. Dividing by $P_n$ gives $A_n/P_n=A_{n−1}/P_{n−1}+s_n/P_n$, so $A_n=P_n(A_0+∑ s_j/P_j)$. If a multiplier vanishes, solve that step directly and restart the product afterward; division by a zero summation factor is not allowed.

For example, $A_n=(n/(n+1))A_{n−1}+1$, $A_0=1$, has $P_n=1/(n+1)$. The normalized increment is $n+1$, giving $A_n=(1+∑_{j=1}^{n}(j+1))/(n+1)=(n+2)/2$. The normalization, the initial value, and the telescoping sum are all necessary: computing several early values is evidence for a guess, not its proof.

### Constant-coefficient equations and resonance

For a homogeneous second-order equation $A_n=c_1A_{n−1}+c_2A_{n−2}$, substitute a nonzero trial $λ^n$ to obtain the characteristic equation $λ^2−c_1λ−c_2=0$. Two distinct roots give solutions $uλ_1^n+vλ_2^n$; solve the two initial-value equations for $u,v$. Their independence follows because their first two values form a matrix with nonzero determinant $λ_2−λ_1$. A second-order recurrence has a unique solution for two initial values, so the constructed solution is complete.

If a nonzero root is repeated, both $λ^n$ and $nλ^n$ satisfy the recurrence by direct substitution and have independent initial vectors. Thus $A_n=(u+vn)λ^n$. This is not permission to reuse the two-identical-roots expression and forget the new polynomial factor. For Fibonacci's equation the roots are $(1+√5)/2$ and $(1−√5)/2$; the usual initial values give the difference of their powers divided by $√5$. A leading term can disappear when its coefficient is zero, so the largest root's magnitude alone does not establish a lower bound for every initial condition.

For a nonhomogeneous equation, find one particular solution and add the general homogeneous solution. A forcing term shaped like an existing homogeneous solution requires a new factor of $n$. For $A_n=2A_{n−1}+2^n$, divide by $2^n$ to get a normalized increment one; the result is $(A_0+n)2^n$. For $A_n−2A_{n−1}+A_{n−2}=1$, a quadratic particular solution works because the second difference of $n(n−1)/2$ is one. Direct substitution is the final check. Higher-order characteristic and generating-function machinery is a separate topic; these derivations cover the elementary algorithmic equations used below.

The nonzero-root qualification matters. If $c_2=0$, the equation for $n ≥ 2$ is already first order: $A_n=A_1c_1^{n−1}$ for $n ≥ 1$ when $c_1 ≠ 0$, while the separately specified $A_0$ need not fit that expression. If both coefficients vanish, every term from index two onward is zero. Do not divide by a zero root or use $nλ^n$ as an independent solution at $λ=0$. Negative or complex roots also require signed or complex sequences; an oscillating expression is not automatically a nonnegative algorithmic cost. When a homogeneous formula is used for a cost, check the initial coefficients, eventual nonnegativity, and the lower bound separately.

## Recursion trees as exact sums

### Count nodes and tolls separately

Consider $T(n)=aT(n/b)+f(n)$, with an integer $a ≥ 1$, fixed $b>1$, and input $n=b^h$ so the ideal tree reaches one exactly. At depth $j$, there are $a^j$ nodes, each of size $n/b^j$. Its nonrecursive contribution is $a^jf(n/b^j)$. The internal depths are zero through $h−1$; the $a^h$ leaves contribute their base costs. Summing these quantities is an identity, not merely a picture-based guess.

<!-- MATH:tree -->

The identity $a^{log_b n}=n^{log_b a}$ follows by writing both sides as $exp((ln a)(ln n)/(ln b))$. Define the critical exponent $p=log_b a$. It measures the leaf population, not the toll's exponent. Even if the internal toll vanishes, positive leaf costs force a contribution of order $n^p$.

For $f(n)=n^q$, each internal level costs $n^q(a/b^q)^j$. Let $ρ=a/b^q$. A finite geometric sum is $(1−ρ^h)/(1−ρ)$ when $ρ ≠ 1$ and is $h$ when $ρ=1$. For $ρ<1$, its first term gives a lower bound and its infinite sum a constant upper bound. For $ρ>1$, factor out the last term and sum powers of $1/ρ$. For $ρ=1$, every internal level contributes the same amount. Account for the leaves separately in all three cases.

<!-- FIGURE:levels -->

An uneven tree requires care: different branches can stop at different depths, so multiplying the root toll by the longest path length need not give a matching lower bound. Either count the live contribution at each level, charge cost to leaves or mass, use substitution, or use a theorem whose hypotheses cover the unequal sizes. A fully specified tree with a justified sum is a proof; a sketch with unexplained dots is only intuition.

## Substitution with constants, slack, and base cases

Substitution means strong induction on a proposed explicit bound. Choose a constant once, verify every required base value, substitute the same constant for all smaller children, and prove the parent inequality. Writing $T(n)=O(n)$ on both sides of a recurrence and dropping hidden constants is not an inductive proof: a multiplier can grow at each level.

For $T(n)=2T(n/2)+n$, a proposed upper bound $Cn$ produces $Cn+n$ and cannot close. Trying $Cn log_2 n+Dn$ instead gives $Cn log_2 n−Cn+Dn+n$. The new expression is at most the target if $C ≥ 1$. Choose $D$ to cover the base at one, where the logarithmic term vanishes. A corresponding small positive coefficient on $n log_2 n$ proves a lower bound. The missing logarithm pays for work repeated at every level.

For $T(n)=2T(n/2)+1$, even the correct asymptotic guess $Cn$ does not close directly: it produces $Cn+1$. Strengthen it to $Cn−D$. The children produce $Cn−2D+1$, which is at most $Cn−D$ when $D ≥ 1$. Choose $C$ large enough that the base fits the strengthened expression. A failed proof can therefore mean the proposed order is wrong, or merely that the inductive statement lacks lower-order slack. Distinguish these two diagnoses.

If a bound is asserted only for $n ≥ N$, its children may lie below $N$. Cover the finite transition band explicitly, or state an induction beginning at a base range large enough to include all such child sizes. Increasing a constant can cover finitely many positive denominators, but cannot make $Cn log n$ positive at one. Do not divide by a function that vanishes at a base input.

For an upper inequality, substitution proves an upper bound. It cannot manufacture a lower bound. For instance, a nonnegative constant function satisfies $T(n) ≤ 2T(n/2)+n$ but does not grow as $n log n$. Keep inequality directions and the claimed conclusion aligned.

## The master theorem and its limitations

### The three classical cases

Take a fixed-size recurrence $T(n)=aT(n/b)+f(n)$ with $a ≥ 1$, $b>1$, positive constant base costs, and an eventually nonnegative toll. On powers of $b$, let $p=log_b a$. The following are separate sufficient conditions, not an exhaustive decision tree for every possible $f$.

| Case | Required condition | Tight conclusion |
| --- | --- | --- |
| Leaf dominated | $f(n)=O(n^{p−ε})$ for a fixed $ε>0$ | $T(n)=Θ(n^p)$ |
| Balanced | $f(n)=Θ(n^p)$ | $T(n)=Θ(n^p log n)$ |
| Root dominated | $f(n)=Ω(n^{p+ε})$ for a fixed $ε>0$ and $af(n/b) ≤ cf(n)$ eventually for a fixed $0<c<1$ | $T(n)=Θ(f(n))$ |

For the first case, each level is bounded by a constant times $n^{p−ε}b^{εj}$. Summing this geometrically through depth $h−1$ gives an upper bound of order $n^p$; the positive leaves give the lower bound. For the balanced case, each internal level is between fixed multiples of $n^p$, and there are $Θ(log n)$ such levels. For the third case, repeatedly applying regularity bounds level $j$ by $c^jf(n)$. The root itself gives a lower bound; the leaves are smaller than $f(n)$ by the polynomial gap. This proves all three cases from the tree identity.

For a pure-power toll $Θ(n^q)$, compare $q$ with $p$. If $q<p$, leaves dominate; if $q=p$, add one log; if $q>p$, the ratio $a(n/b)^q/n^q=a/b^q<1$ verifies regularity for the exact monomial model. When the actual toll is merely bounded by constant multiples of that monomial, comparison with two exact monomial envelopes yields the same conclusion even if the toll itself oscillates enough to fail the displayed regularity ratio.

### A logarithmic difference is not a polynomial gap

The toll $n^p/log n$ is smaller than $n^p$, but it is not $O(n^{p−ε})$ for any fixed positive $ε$: the ratio is $n^ε/log n$, which grows without bound. Likewise $n^p log n$ is larger than $n^p$ without being $Ω(n^{p+ε})$. The three-case theorem's balanced condition applies only when the ratio stays between positive constants. Such boundary tolls require the next section, summation, or Akra–Bazzi; declaring them “slightly smaller” or “slightly bigger” is not a case check.

Regularity is not decorative. On the dyadic grid $n=2^h$, let the toll be $n^2$ for even $h$ and $n^3$ for odd $h$, in the recurrence $T(n)=2T(n/2)+f(n)$. This toll is always at least quadratic, giving a polynomial gap above the critical exponent one. For even $h$, however, the immediate child has cubic toll, so the child contribution alone is $2(n/2)^3=n^3/4$. The solution-to-root-toll ratio is therefore at least $n/4$, unbounded along those even levels. The claimed $Θ(f(n))$ conclusion fails. The regularity ratio also grows without bound there, exposing the missing condition.

When a theorem does not apply, report that fact and choose another method. The recurrence can still have a precise answer. Failure of sufficient hypotheses is not failure of the algorithm or proof that the conclusion is false; the same conclusion may have an independent proof.

## Critical logarithmic tolls: all real powers

Choose a fixed base threshold $n_0>1$ so that negative log powers are defined safely. Consider $T(n)=aT(n/b)+Θ(n^p(log_b n)^k)$ with $p=log_b a$ and any fixed real $k$. For an ideal input $n=n_0b^h$, reverse the level index: a node with remaining depth $r$ has log size $log_b n_0+r$. Its level contribution is between fixed multiples of $n^p(log_b n_0+r)^k$. Summing and adding leaves yields $Θ(n^p(1+∑_{r=1}^{h}r^k))$; the fixed shift changes only constant factors.

The power-sum thresholds now give a complete boundary classification:

| Logarithmic exponent | Solution |
| --- | --- |
| $k>−1$ | $Θ(n^p(log n)^{k+1})$ |
| $k=−1$ | $Θ(n^p log log n)$ |
| $k<−1$ | $Θ(n^p)$ |

For $k=−1$, the sum is harmonic, so another log appears in the already logarithmic depth. For $k<−1$, the total normalized internal contribution converges, and leaves still contribute $Θ(n^p)$. The tempting formula that adds one to every log exponent fails below the threshold because it would predict less than the compulsory positive leaf cost.

<!-- FIGURE:critical -->

The table includes the common extended master case with nonnegative $k$, but its negative-power portion has just been derived independently rather than silently attributed to a weaker statement. For $a=1$, the critical exponent is zero; the same sum classification describes a single shrinking chain. Base thresholds must still prevent evaluating a singular log toll at one.

## Rounding, exact counts, and stopping rules

### Prove what survives rounding

For a monotone cost function and a nonnegative fixed-ratio model, comparison with adjacent powers can transfer a bound when the comparison hypotheses are established. If $b^h ≤ n<b^{h+1}$, the two neighboring ideal inputs differ by a constant factor. Standard polynomial/logarithmic bounds therefore differ by a constant factor as well. Without monotonicity or another valid envelope, this sandwich cannot simply be assumed.

For $T(n)=aT(⌊n/b⌋)+g(n)$ with integer $b ≥ 2$, the size at depth $j$ is $⌊n/b^j⌋$; prove that identity by writing integer division twice. With the fixed base range zero through $b−1$, stopping occurs after $h=⌊log_b n⌋$ steps for $n ≥ 1$. For a pure power toll with $q ≥ 0$ and positive bounded bases, the internal sizes and adjacent-power envelopes give the same asymptotic three cases. For ceilings and additive offsets, first choose a base threshold that forces each child smaller, then establish a suitable induction or perturbation theorem; “rounding never matters” is too broad.

### Exact balanced split costs

Let $C(0)=C(1)=0$ and, for $n ≥ 2$, let $C(n)=C(⌊n/2⌋)+C(⌈n/2⌉)+n−1$. This is the worst-case comparison count for ordinary merging of two nonempty sorted halves when each merge can require size minus one comparisons. Let $h=⌈log_2 n⌉$. A balanced split tree has $n$ singleton leaves, at depths $h−1$ or $h$; their numbers are $2^h−n$ and $2n−2^h$. If these counts are $u,v$, then $u+v=n$ and $2u+v=2^h$: each shallower leaf occupies two slots at depth $h$, while each deeper leaf occupies one. Solving these equations gives the stated counts. To justify the depth statement, at depth $j$ every live split size is a floor or ceiling of $n/2^j$; sizes are at least two before depth $h−1$, and at most one at depth $h$.

Every original item is counted once at each ancestor's size toll, so the sum of internal size tolls equals the sum of leaf depths. A full binary tree with $n$ leaves has $n−1$ internal nodes; prove this by counting its edges as twice the internal count and also as total nodes minus one. Subtracting the one-per-internal-node term gives the exact expression $C(n)=nh−2^h+1$. At powers of two it is $n log_2 n−n+1$. Between neighboring powers, the correction to the leading term is generally proportional to $n$, with a bounded periodic coefficient depending on the fractional part of $log_2 n$, plus the final constant one. The unnormalized correction is not bounded by a constant.

The upper comparison count is realizable simultaneously, which is necessary for a worst-case equality. At a merge of two nonempty halves, choose the sorted global rank order so its last two keys belong to opposite halves. The merge cannot exhaust either half before comparing all but the final key, so it uses exactly $n−1$ comparisons. Distribute the earlier ranks in any order respecting the two required half sizes. Inductively choose a worst-case input permutation within each half; this does not change the half's assigned set of ranks or their relative order after sorting. The top merge remains worst case and both recursive sorts attain their own maxima. Starting with singleton halves proves realizability at every size. Thus the recurrence is more than a sum of upper bounds from mutually incompatible inputs.

<!-- FIGURE:rounded -->

An abstract recurrence with toll $n$ and zero singleton base costs instead has value $C(n)+n−1=nh−2^h+n$. Princeton's notes discuss this latter recurrence. They share a $Θ(n log n)$ growth rate but have different exact counts. Always match the cost being measured before transferring a closed form from a reference.

## Unequal subproblems and Akra–Bazzi

### Linear work from shrinking total mass

For $T(n)=T(αn)+T(βn)+cn$ in an ideal real-size model with $0<α,β<1$ and $α+β<1$, the total active size at depth $j$ is at most $n(α+β)^j$. Terminated nodes can only reduce that mass. Summing the internal work gives at most $cn/(1−α−β)$. At the fixed positive stopping threshold, base leaves also cost only $O(n)$: their masses are bounded below by a positive constant, and splitting never increases total mass. The root's positive linear toll gives an $Ω(n)$ lower bound. Thus this exact positive-toll recurrence has $Θ(n)$ cost.

For a corresponding upper inequality alone, the reasoning proves $O(n)$; a compulsory linear scan in the actual algorithm establishes tightness separately. With additive rounding error, substitution makes the margin explicit. If child sizes sum to at most $γn+D$ with $γ<1$, then a linear upper guess produces $Cγn+CD+cn$, which is at most $Cn$ once $n$ is large and $C$ exceeds $c/(1−γ)$. Cover the finite smaller band by a suitable base bound. This proof applies to the median-of-medians size bound without pretending the ideal fractions are exact integers.

If $α+β=1$, the lost margin disappears; with linear tolls the solution is typically $Θ(n log n)$. A longest-path upper estimate alone does not prove a matching lower estimate. If the total child ratio exceeds one, mass grows, and the leaf exponent is determined by a weighted equation rather than a fake average subproblem size.

<!-- FIGURE:mass -->

### A precise unperturbed theorem

Consider a real-size equation $T(x)=∑ a_iT(b_ix)+g(x)$ above a fixed threshold, with a fixed finite number of terms, $a_i>0$, and $0<b_i<1$. After a fixed rescaling of input units, use a base interval $[1,x_0]$ with $x_0 ≥ 1/min_i b_i$; every child of a nonbase call then has argument at least one. Base values throughout that interval are bounded above and below by positive constants. Assume the toll is nonnegative, locally integrable, and bounded on each finite interval; extend it over the base interval as a bounded nonnegative integrable function. Assume its multiplicative-interval comparability: there are fixed $A,B>0$ with $Ag(x) ≤ g(u) ≤ Bg(x)$ for every relevant $u$ between $b_ix$ and $x$ and all sufficiently large $x$. This is a substantive smoothness hypothesis, not merely the statement that a derivative happens to have a polynomial bound.

There is a unique real $p$ with $∑ a_ib_i^p=1$: the left side is continuous and strictly decreasing in $p$, approaches infinity as $p$ tends to negative infinity, and approaches zero at positive infinity. Under the stated assumptions,

<!-- MATH:akra -->

For actual recursive call counts, the $a_i$ are positive integers; then $p ≥ 0$. Fractional positive coefficients define weighted mathematical recurrences and can give a negative exponent, but do not mean that a program executes a fraction of a call. The theorem concerns an unperturbed real-size model. Its full perturbation extension has additional conditions and is not assumed for arbitrary variable child arguments.

### Why the integral formula works

Define $F(x)=x^p(1+∫_1^x g(u)/u^{p+1}du)$. Positive weights $w_i=a_ib_i^p$ sum to one. Expand the child expressions and subtract them from the parent. The constant terms cancel, leaving

<!-- MATH:gap -->

On each interval $[b_ix,x]$, comparability bounds $g(u)$ by fixed multiples of $g(x)$, and $u^{p+1}$ by fixed multiples of $x^{p+1}$. Its length is $(1−b_i)x$. Therefore each displayed weighted integral, after multiplying by $x^p$, is between fixed positive multiples of $g(x)$. Summing finitely many positive weights gives constants $d,D>0$ with $dg(x) ≤ F(x)−∑ a_iF(b_ix) ≤ Dg(x)$.

For the upper bound, choose $C ≥ 1/d$ and large enough for the bounded base interval. Induction gives $T(x) ≤ C∑ a_iF(b_ix)+g(x) ≤ CF(x)$. For the lower bound choose $0<c ≤ 1/D$ and small enough for all base values, giving $T(x) ≥ c∑ a_iF(b_ix)+g(x) ≥ cF(x)$. Both choices are made once. To make induction on real inputs precise, choose a threshold large enough that every $b_ix$ lies at least one unit below $x$ above the threshold, and induct over consecutive unit intervals. The finite transition interval is absorbed into the base constants. This proves the unperturbed formula without requiring equal-depth leaves.

For $g(x)=Θ(x^q(log x)^k)$, the integral is comparable to integrating $u^{q−p−1}(log u)^k$, away from a fixed initial cutoff. When $q<p$ it converges for any fixed real $k$; when $q>p$ it grows as $x^{q−p}(log x)^k$; when $q=p$, substitute $v=log u$ and use the three log-power thresholds. The resulting classification agrees with the equal-size master analysis and extends it to unequal constant ratios.

Do not apply this integral theorem to exponential tolls merely because the recurrence has shrinking children. For a regular exponential toll such as $2^n$, direct comparison or unrolling can show root dominance, but the polynomial-interval comparability required here fails.

## Changes of variables and resource models

### Transform the argument, not the answer

For $T(n)=2T(√n)+log_2 n$ on $n=2^{2^h}$, first set $m=log_2 n$ and $S(m)=T(2^m)$. The equation becomes $S(m)=2S(m/2)+m$, so $S(m)=Θ(m log m)$. Returning to the original variable gives $T(n)=Θ(log n log log n)$. Reporting $Θ(n log n)$ would forget the transformation and solve the wrong problem.

For $T(n)=T(√n)+1$ with a constant threshold greater than one, log size halves on each call. There are $Θ(log log n)$ calls. But $T(n)=T(n/2)+1$ has $Θ(log n)$ calls. A square root, a constant-factor reduction, and a constant decrement are three different progress rates; visually similar short formulas do not imply similar depths.

For $T(n)=2T(n/2)+n/log_2 n$, the substitution $n=2^h$ and $U(h)=T(2^h)/2^h$ yields $U(h)=U(h−1)+1/h$, with a base at $h=1$. Thus $U(h)$ is harmonic and the original answer is $Θ(n log log n)$. Normalizing by the leaf exponent often reveals the sum responsible for a difficult boundary case.

### Work, span, storage, and repeated states

Two independent half-size calls with a linear combine step have sequential work $W(n)=2W(n/2)+Θ(n)$. If the calls run in parallel but combining is sequential, span satisfies $S(n)=S(n/2)+Θ(n)$, which is linear. A parallel combine step with logarithmic span instead gives $S(n)=S(n/2)+Θ(log n)$, producing $Θ((log n)^2)$. Processor scheduling and actual parallel primitives must support the claimed span model.

Stack space follows the maximum simultaneously live chain and per-frame storage. With constant-size frames and sequential half-size recursion, stack use is $Θ(log n)$, even when total work is $Θ(n log n)$. If each live frame retains an array proportional to its local size, the maximum sum along a halving path is linear. If temporary memory is released before the child calls, that storage recurrence changes. Space is a liveness question, not a copy of the time equation.

Naive Fibonacci recursion has repeated states and exponentially many calls. Memoizing it changes the execution graph: only linearly many distinct arguments are computed, and each performs constant work in a unit-cost arithmetic model. The recursion depth can still be linear. Fibonacci outputs have growing bit lengths, so treating arithmetic as unit cost and treating bit complexity are different analyses. A memoized implementation cannot be analyzed as if both subtrees were independently recomputed.

Expected cost must average actual conditional subproblem costs. In general $E[T(X)] ≠ T(E[X])$. For example, a child size equally likely to be zero or two has expected size one, but for squared cost its expected cost is two instead of one. Use conditioning and linearity of expectation to derive an expected recurrence; do not feed the average size into a nonlinear running-time function. Full probabilistic algorithm analysis is taught later.

## Fully explained problem bank

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Interactive recurrence-level laboratory

The laboratory uses an exact ideal tree on inputs $n=b^h$, with integer branching factor and polynomial toll exponent. It computes the same total in two ways: bottom-up recurrence evaluation and a separately accumulated level table with terminal leaf costs. Three presets show leaves dominating, equal internal levels, and the root dominating. Additional presets expose a single shrinking chain and how changing only the base cost changes an exact answer. It is a finite calculation, not a proof of an asymptotic statement or a simulator of arbitrary uneven recurrences.

<!-- LAB:recurrence -->

### Executable finite accounting

The following original Python function evaluates the ideal recurrence using integer arithmetic. Its loop invariant is that after iteration $r$, the stored cost equals the cost at input $b^r$, including the original terminal base value. At iteration zero this is the specified base; multiplying the previous cost by the branching factor and adding the current size toll establishes the next step. Python integers retain exactness even when a large polynomial toll exceeds floating-point precision. The function analyzes one finite input; it does not establish an asymptotic theorem.

```python
def ideal_cost(a, b, q, h, base=1):
    """Exact cost for n=b**h, toll n**q, and terminal cost base."""
    limits = ((a, 1, 6), (b, 2, 6), (q, 0, 4),
              (h, 0, 8), (base, 1, 20))
    if any(type(value) is not int or not low <= value <= high
           for value, low, high in limits):
        raise ValueError("Use integer parameters within the laboratory limits.")
    cost = base
    size = 1
    for remaining_height in range(1, h + 1):
        size *= b
        cost = a * cost + size ** q
    return cost
```

For parameters $(a,b,q,h,base)=(2,2,1,4,1)$, the function returns eighty. Independently, four internal levels each contribute sixteen and the sixteen leaves each cost one, giving $4·16+16=80$. With zero height the loop executes no steps and returns the base cost. This last case checks that a singleton root is a terminal node, rather than an internal call whose toll is charged again.

## References and limits

- Erik Demaine, Jason Ku, Justin Solomon. MIT 6.006, Spring 2020, [Recitation 3](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/1869dbf640ded6b31f1bd369d2001ef5_MIT6_006S20_r03.pdf), all seven pages, with recurrence material on pages 4–6.
- Moses Charikar, Ellen Vitercik; adapted from Virginia Williams and credited contributors. Stanford CS 161, retrieved Lecture 3 notes identifying Winter 2026, [Solving Recurrences and the Selection Problem](https://stanford-cs161.github.io/winter2025/assets/files/lecture3-notes.pdf), all six pages. [Solved concept checks](https://stanford-cs161.github.io/winter2025-bank/recurrence.pdf), one page. The URL's older year is not treated as the document's date.
- Avrim Blum. CMU 15-451, Fall 2011, taught by Avrim and Manuel Blum, [Lectures 1–10](https://www.cs.cmu.edu/afs/cs/academic/class/15451-f11/www/lectures/lects1-10.pdf), PDF pages 10–15 and 24–26, corresponding to printed Lecture 2 pages 7–12 and selected Lecture 4 pages 21–23.
- Robert Sedgewick, Philippe Flajolet. Princeton *Analysis of Algorithms*, [Chapter 2: Recurrence Relations](https://aofa.cs.princeton.edu/20recurrence/), complete available web text and selected exercise statements; [course materials](https://aofa.cs.princeton.edu/online/). Empty section headings are not counted as full underlying textbook sections.
- Cornell CS 3110. [Lecture 20, Spring 2009](https://www.cs.cornell.edu/courses/cs3110/2009sp/lectures/lec20.html) and [Recitation 19, Spring 2011](https://www.cs.cornell.edu/courses/cs3110/2011sp/Recitations/rec19.htm), complete available text. Individual authors are not named on these read pages.
- Tom Leighton. *Notes on Better Master Theorems for Divide-and-Conquer Recurrences*, October 9, 1996, [MIT course-hosted notes](https://courses.csail.mit.edu/6.046/spring04/handouts/akrabazzi.pdf), pages 1–5; the unperturbed theorem and proof on pages 2–4 are used, while the later perturbation proof is outside this lesson.

These are newly written explanations and independently worded exercises. The source audit records a bounded candidate pool and actual reading scopes; it does not certify an exhaustive search of every worldwide course or reproduce all exercise collections. General conclusions rest on their stated proofs; finite independent checks detect additional mistakes. No lesson can certify success on every possible unseen question. The student explicitly approved this chapter; it is now part of the finished library.
