# Generating Functions: Formal Algebra, Exact Coefficients, and Counting Structures

## 1. Written sources, prerequisites, and chapter scope

This chapter synthesizes four complementary written courses: MIT 6.042J, Berkeley Math 172, CMU 15-251, and Princeton's Analysis of Algorithms lecture on generating functions. Their exact reading scopes, authors, selection rationale, and source corrections appear in the [source audit](../reviews/d_generating-sources.html). We use their mathematical ideas to build independent derivations and original worked problems, rather than concatenate lecture summaries.

You need algebraic manipulation, finite sums, binomial coefficients, elementary counting, and recurrence relations. Formal differentiation is introduced here; numerical calculus is not required for the main coefficient arguments. The advanced extensions prove formal coefficient inversion and distinguish exact extraction from analytic growth. The lesson addresses the complete declared scope of ordinary and exponential generating functions, bounded and weighted counting, rational recurrences, recursive structures, parameter marking, and probability bridges. Full complex-analysis singularity theory is outside this chapter.

The four core written references are listed at the end. The problem bank includes original examination bridges checked against source PDFs, original mathematical problems, and explicitly identified course-pattern reconstructions. Every displayed answer has a derivation. A completed quality audit documents finite checks and remaining limits; it cannot guarantee performance on every future question.

## 2. What a generating function represents

A sequence is an indexed assignment of coefficients. An ordinary generating function, abbreviated OGF, packages that assignment into a formal expression:

$$A(x)=\sum_{n\ge0}a_nx^n,\qquad [x^n]A(x)=a_n.$$

The bracket operator returns a coefficient, not the term containing the variable. Thus extracting a coefficient removes the bookkeeping variable. Coefficients with negative indices are defined to be zero unless a Laurent series is explicitly introduced. For example, the sequence 3,0,5,0,0,... has OGF $3+5x^2$. The coefficient of the third power is zero, while the coefficient of the second power is five.

Size and coefficient are different data. In a counting application, an exponent records size and its coefficient records the number or total weight of objects of that size. Two distinguishable objects of size four contribute two copies of the same monomial. Combining those copies yields $2x^4$; it does not mean one object of size eight. This distinction underlies every product and composition argument later.

A finite list through degree $N$ represents a truncated series, not an infinite claim that all later coefficients vanish. Write equality modulo the next power when only a prefix is known. A prefix determines a target coefficient only if all operations used to obtain it require no unknown higher coefficients.

## 3. Formal power series and why convergence is unnecessary

Work first over the rational numbers. A formal series is the infinite coefficient list, with addition defined coordinatewise and multiplication defined by finite convolution:

$$[x^n](A+B)=a_n+b_n,\qquad [x^n](AB)=\sum_{i=0}^{n}a_i b_{n-i}.$$

Only finitely many pairs contribute to one coefficient. Consequently this product exists even if neither series converges at any nonzero numerical value. Associativity follows by collecting the finite triples of indices whose sum is the requested degree. The zero series has all coefficients zero; the multiplicative identity has coefficients 1,0,0,... . Multiplication is not coordinatewise multiplication. Coordinatewise multiplication is called a Hadamard product and has a different coefficient rule.

For a series $A$ with nonzero constant coefficient, solve $AB=1$ one coefficient at a time. The constant equation gives $b_0=1/a_0$. The equation at degree $n$ then gives

$$b_n=-\frac{1}{a_0}\sum_{i=1}^{n}a_i b_{n-i}\qquad(n\ge1).$$

This proves both existence and uniqueness of an inverse. Conversely, the constant coefficient of a product is the product of the constant coefficients, so a series with zero constant cannot have an inverse. Over a general commutative coefficient ring, replace “nonzero” with “invertible in that ring.” For example, a constant two is invertible over the rationals but not over the integers. The variable itself has zero constant coefficient and is not invertible as a power series.

One may still divide a series with zero initial coefficients by a matching power of the variable: all exponents remain nonnegative. That is a shift of a divisible series, not a claim that the variable has an inverse in the power-series ring.

<!-- SIM: inverse -->

## 4. Coefficient extraction, products, and safe truncation

Expand a product by choosing one term from each factor. A term $a_i x^i$ and a term $b_j x^j$ produce $a_i b_j x^{i+j}$. To extract degree $n$, retain exactly the diagonal with $i+j=n$. This proves the convolution rule directly and gives a useful visual method for avoiding wrong indices.

$$[x^n](AB)=a_0b_n+a_1b_{n-1}+\cdots+a_nb_0.$$

For the first $N+1$ coefficients, replace both factors by their prefixes through degree $N$. Higher terms cannot enter a nonnegative-degree convolution target at most $N$. A reciprocal prefix likewise depends only on the denominator prefix through $N$ when its constant coefficient is nonzero. These statements fail after a left shift that exposes unknown higher coefficients: extracting degree $N$ from a series divided by a power $x^m$ may require degree $N+m$ of its numerator.

As a concrete calculation, multiply $A(x)=1+2x+3x^2+4x^3$ by $B(x)=1+x+x^2+x^3$. The degree-three coefficient is $1+2+3+4=10$. The coefficientwise product would give only four, so it cannot represent this ordinary product.

<!-- SIM: convolution -->

## 5. Shifts, scaling, parity, and index changes

A right shift inserts zeros. A left shift removes initial terms before dividing:

$$[x^n]x^m A(x)=a_{n-m},\qquad \sum_{n\ge0}a_{n+m}x^n=\frac{A(x)-\sum_{j=0}^{m-1}a_jx^j}{x^m}.$$

The removed polynomial is essential: without it, negative powers appear. Scaling the variable multiplies a coefficient by the corresponding power:

$$[x^n]A(cx)=c^n a_n.$$

Replacing the variable by its negative alternates signs. Therefore the even-degree and odd-degree parts are respectively $(A(x)+A(-x))/2$ and $(A(x)-A(-x))/2$. Those parts still use the original exponents. They are not the compressed subsequence OGFs $\sum_{n\ge0}a_{2n}x^n$ and $\sum_{n\ge0}a_{2n+1}x^n$. Compression changes the index scale and must be handled separately.

For a primitive complex $m$th root of unity $\omega$, the residue filter is

$$\frac{1}{m}\sum_{j=0}^{m-1}\omega^{-rj}A(\omega^j x)=\sum_{n\equiv r\pmod m}a_nx^n.$$

To prove it, the multiplier of a coefficient is a finite geometric sum of powers of $\omega^{n-r}$. It is one after division by $m$ when the exponent is a multiple of $m$, and zero otherwise. This uses complex scalars and an invertible integer $m$; it is not automatically valid in modular arithmetic of characteristic dividing $m$.

<!-- SIM: filtering -->

## 6. Differentiation, integration, and polynomial weights

Define formal differentiation term by term. Its meaning is algebraic and its product rule follows from convolution:

$$A'(x)=\sum_{n\ge0}(n+1)a_{n+1}x^n,\qquad xA'(x)=\sum_{n\ge0}n a_nx^n.$$

The operator $xD$, where $D$ means differentiation, weights an unchanged index by that index. Repeating $xD$ twice gives the weights $n^2$, whereas $x^2D^2$ gives $n(n-1)$. These operators are different because differentiation also acts on the first multiplier $x$:

$$(xD)^2A=xA'+x^2A''.$$

More generally, $x^kD^k$ weights by the falling factorial $n(n-1)\cdots(n-k+1)$. Polynomial weights can be expanded in the falling-factorial basis, which makes rational OGFs particularly easy to differentiate. Starting from $1/(1-x)$ gives

$$\sum_{n\ge0}nx^n=\frac{x}{(1-x)^2},\qquad \sum_{n\ge0}n^2x^n=\frac{x(1+x)}{(1-x)^3}.$$

The formal integral with constant zero is $\sum a_nx^{n+1}/(n+1)$. This requires that the relevant integers are invertible, as they are over the rationals. It is not a general operation over a field of positive characteristic. Formal differentiation can lose information there; for instance the derivative of the $p$th power of the variable is zero in characteristic $p$.

## 7. Prefix sums, finite differences, and binomial transforms

The all-ones series is the inverse of $1-x$, since its product with that polynomial has constant one and all later coefficients zero. Convolution therefore gives the prefix-sum rule:

$$\sum_{n\ge0}\left(\sum_{i=0}^{n}a_i\right)x^n=\frac{A(x)}{1-x}.$$

Multiplication by $1-x$ produces the backward difference $a_n-a_{n-1}$, with the boundary $a_{-1}=0$. This boundary is part of the transformation. Repeated prefix summation multiplies by repeated inverse factors; the resulting coefficient weights are binomial coefficients.

For the binomial transform $b_n=\sum_{k=0}^{n}\binom{n}{k}a_k$, derive its OGF by reversing a coefficientwise finite double sum. The inner identity comes from differentiating a geometric series $k$ times:

$$\sum_{n\ge k}\binom{n}{k}x^n=\frac{x^k}{(1-x)^{k+1}},\qquad B(x)=\frac{1}{1-x}A\left(\frac{x}{1-x}\right).$$

The inner substitution has zero constant coefficient, so composition is formally defined. Inverting the transform gives $a_n=\sum_{k=0}^{n}(-1)^{n-k}\binom{n}{k}b_k$. This can be verified by substituting the forward transform and using the binomial theorem to annihilate every nonmatching index.

## 8. A coefficient dictionary with proofs and conditions

For an integer $k\ge1$, the negative-binomial expansion is

$$[x^n]\frac{1}{(1-cx)^k}=c^n\binom{n+k-1}{k-1}\qquad(n\ge0).$$

One proof multiplies $k$ geometric series. Each coefficient counts nonnegative integer $k$-tuples summing to $n$, which are counted by stars and bars; scaling adds the factor $c^n$. A second proof differentiates $(1-cx)^{-1}$ repeatedly and adjusts the index. Both proofs show exactly why the exponent in the denominator is one more than the degree of the polynomial factor in $n$.

For any rational or complex scalar $\alpha$, define generalized binomial coefficients by the finite product

$$\binom{\alpha}{n}=\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!},\qquad \binom{\alpha}{0}=1.$$

Then $(1+x)^\alpha$ means the unique normalized formal solution of $(1+x)Y'=\alpha Y$, whose coefficient recurrence gives exactly these coefficients. This supplies an algebraic definition even when the exponent is not an integer. The exponential and logarithmic series are defined by their coefficients and normalized differential equations:

$$e^x=\sum_{n\ge0}\frac{x^n}{n!},\qquad -\log(1-x)=\sum_{n\ge1}\frac{x^n}{n}.$$

The logarithm has zero constant. Harmonic numbers arise by dividing this logarithmic series by $1-x$, so its degree-$n$ coefficient is $H_n=\sum_{j=1}^{n}1/j$. Rational, algebraic, exponential, and logarithmic OGFs need different extraction techniques; not every useful OGF has a partial-fraction decomposition.

## 9. Rational functions, repeated poles, and finite prefixes

For a rational OGF, first ensure that the denominator has nonzero constant coefficient. Cancel common factors before discussing its poles. If the numerator degree is at least the denominator degree, polynomial division separates a finite polynomial prefix from a proper rational part. A polynomial quotient affects only finitely many coefficients and cannot simply be discarded in an exact answer.

Factor the proper denominator over a suitable field. Each nonzero pole $\rho$ corresponds to the factor $1-x/\rho$. For simple poles, multiplying by this factor and then setting the variable to the pole determines the corresponding coefficient. For a repeated pole of multiplicity $m$, include every denominator power from one through $m$. Coefficient extraction gives terms that are polynomial in the index times $\rho^{-n}$.

$$A(x)=P(x)+\sum_{i}\sum_{j=1}^{m_i}\frac{c_{ij}}{(1-\lambda_i x)^j},\qquad a_n=[x^n]P(x)+\sum_i\sum_{j=1}^{m_i}c_{ij}\lambda_i^n\binom{n+j-1}{j-1}.$$

For example, $1/((1-x)(1-2x))=-1/(1-x)+2/(1-2x)$ has coefficient $2^{n+1}-1$. In contrast, cancellation in $(1-2x)/(1-2x)^2$ leaves a simple pole and coefficients $2^n$, not an index times that power. The reduced denominator controls the answer.

### Why the complete repeated-pole basis is necessary

After polynomial division, write the denominator as a product of relatively prime powers of distinct linear factors over the complex numbers. The Chinese remainder decomposition of the numerator modulo that denominator separates one residue polynomial of degree below each factor's multiplicity. Dividing those residue polynomials by their factor powers, then expressing each numerator in powers of its own linear factor, yields exactly the displayed family of inverse powers. Uniqueness follows after clearing denominators: reduce at each pole modulo its factor power to force the corresponding residue polynomial to zero. Thus partial fractions are a basis decomposition, not a guess based on how many constants look convenient.

For a pole of multiplicity $m$, the coefficient of the highest inverse power is the value at that pole of the rational function after multiplying by the factor to the power $m$. Subtract that highest term before finding the lower powers. Repeating this step, or expanding the remaining numerator locally at the pole, determines all of them. A surviving highest-order coefficient is nonzero in the reduced expression; a numerator cancellation lowers the order before this calculation begins. The polynomial quotient remains a separate finite-prefix contribution.

<!-- SIM: poles -->

## 10. Recurrences with all initial terms retained

Suppose a fixed-lag recurrence begins at index $k$:

$$a_n=\sum_{j=1}^{k}c_j a_{n-j}+h_n\qquad(n\ge k).$$

Multiply by $x^n$ and sum only over the stated domain. For the left side subtract all $k$ known initial terms from $A$. For a lag-$j$ sum, shift the index and subtract the first $k-j$ known terms from the inner series. The complete identity is

$$\left(1-\sum_{j=1}^{k}c_jx^j\right)A(x)=\sum_{i=0}^{k-1}a_i x^i-\sum_{j=1}^{k}c_jx^j\sum_{i=0}^{k-j-1}a_i x^i+\sum_{n\ge k}h_nx^n.$$

An empty inner sum is zero. This formula makes every boundary correction visible. For $a_0=2$, $a_1=5$, and $a_n=5a_{n-1}-6a_{n-2}$ from index two onward, the numerator is $2-5x$ and the denominator is $(1-2x)(1-3x)$. Thus $A=1/(1-2x)+1/(1-3x)$ and $a_n=2^n+3^n$.

An equivalent technique extends negative indices by zero and inserts finite impulses to repair the initial equations. Both methods are valid if the repairs are written explicitly. A constant forcing that starts only after the initial indices contributes a shifted geometric series, not the whole geometric series.

## 11. Inhomogeneous recurrences and resonance in the denominator

For $a_n=2a_{n-1}+n$ from index one onward with $a_0=0$, the equation is $(1-2x)A=x/(1-x)^2$. Partial fractions give

$$A(x)=\frac{2}{1-2x}-\frac{1}{(1-x)^2}-\frac{1}{1-x},\qquad a_n=2^{n+1}-n-2.$$

The first values 0,1,4,11 confirm the boundary and forcing. A forcing term $\lambda^n$ introduces a factor $1-\lambda x$; if that factor already occurs in the recurrence denominator, its multiplicity may increase. The added polynomial degree is the generating-function expression of resonance. Always cancel the numerator before claiming that every potential pole survives.

As a resonant example, $a_n=2a_{n-1}+2^n$ with $a_0=0$ gives $A=2x/(1-2x)^2$, so $a_n=n2^n$. The numerator shift changes the binomial coefficient; directly reading $(n+1)2^n$ would ignore that shift. Nonconstant-coefficient recurrences may lead to differential equations for an OGF, while binomial-sum recurrences often become simpler with EGFs.

## 12. Combinatorial translation: independent choices and bijections

A counting construction is justified by a unique decoding of every counted object. A disjoint union corresponds to a sum. A Cartesian product with additive size corresponds to a product. Multiplying OGFs for two inventory categories counts one independent choice from each, with total size constrained only when the coefficient is extracted. It does not count an arbitrary union of overlapping categories.

For indistinguishable items of one type, unrestricted multiplicity has factor $1/(1-x)$. Multiplicity from $L$ through $U$ has factor $x^L(1-x^{U-L+1})/(1-x)$. Multiplicity congruent to $r$ modulo $m$, with $0\le r<m$, has factor $x^r/(1-x^m)$. If one item has size or price $w$, replace the variable by $x^w$. If there are $q$ genuinely different choices for one component of size $w$, its component polynomial is $qx^w$.

These rules encode counts, not probabilities, unless coefficients are deliberately assigned probability weights. Dependence between categories must be represented explicitly rather than erased by multiplying factors for choices that are not independent.

## 13. Upper and lower bounds through generating functions

For $k$ distinguishable boxes containing indistinguishable units, each constrained to contain between zero and $u$, the OGF is $(1+x+\cdots+x^u)^k$. Rewriting its numerator and denominator gives the exact count

$$[x^n]\frac{(1-x^{u+1})^k}{(1-x)^k}=\sum_{j=0}^{k}(-1)^j\binom{k}{j}\binom{n-j(u+1)+k-1}{k-1}.$$

Here a binomial term is zero when its top integer is less than its nonnegative bottom integer. This is the combinatorial zero convention, not the generalized-binomial convention at negative top indices. The proof selects the $j$ factors supplying the negative numerator monomial and then extracts the remaining nonnegative distribution coefficient.

Lower bounds are removed first: subtract their total from the target and reduce every upper bound accordingly. Unequal upper bounds produce a subset sum of shifts rather than a single binomial coefficient counting equal-bound violations. Before expanding, check that the target lies between the total minimum and total maximum; an impossible target has zero answers immediately.

<!-- SIM: bounded -->

## 14. Coin change, sequences, and exact dynamic programming

For coin denominations in a finite positive set $S$, unordered selections with unlimited multiplicity have OGF $\prod_{w\in S}(1-x^w)^{-1}$. Each multiplicity vector gives exactly one selection. Ordered coin strings instead have OGF $1/(1-\sum_{w\in S}x^w)$, because a string chooses a number of components and then an ordered component at every position. These are different models even with the same denominations.

For denominations 1 and 2, unordered selections of total four are (4,0), (2,1), and (0,2), so there are three. Ordered strings of total four are 1111,112,121,211,22, so there are five. The difference is visible in the two OGFs, and should be diagnosed before doing algebra.

An exact truncated product can be computed with integer dynamic programming. Process denominations outside and target sums in increasing order to allow unlimited use of the current denomination. Reverse the target loop for zero-or-one use. For ordered strings, process the target first and sum contributions from every possible last denomination. The loop order is a mathematical choice about object identity.

```python
def unordered_change(target, denominations):
    ways = [1] + [0] * target
    for weight in sorted(set(denominations)):
        if weight <= 0:
            raise ValueError("Every denomination must be positive.")
        for total in range(weight, target + 1):
            ways[total] += ways[total - weight]
    return ways[target]
```

The code treats repeated denomination entries as the same type. If different colored types of equal price are intended to remain distinguishable, merge-by-value would change the problem and should be removed. Counts are arbitrary-precision integers, not floating-point approximations.

<!-- SIM: coins -->

## 15. Ordered sequences, compositions, and zero-size obstructions

If a component class has OGF $B(x)$ and no zero-size component, ordered finite sequences have OGF $1/(1-B(x))$. Its geometric expansion counts every sequence length once. The condition $B(0)=0$ ensures that any fixed-size coefficient receives contributions from only finitely many lengths. A component of size zero would allow arbitrarily many padded sequences of unchanged size, destroying local finiteness.

For compositions of a positive integer into positive parts, the component OGF is $x/(1-x)$. Thus all compositions, including the unique empty composition of zero, have OGF $(1-x)/(1-2x)$. There are $2^{n-1}$ compositions for positive $n$, while the empty count is one. For exactly $k\ge1$ parts, use the $k$th power of the component series to obtain $\binom{n-1}{k-1}$ when $n\ge k$.

Introducing a marker $u$ for the number of parts gives $1/(1-uB(x))$. Weak compositions with zero parts are safely represented in a two-variable series, since each component contributes positive marker degree even if its size is zero. Setting that marker to one before fixing the number of parts would erase the restriction that made the coefficients finite.

<!-- SIM: composition -->

## 16. Integer partitions, infinite products, and classical identities

An integer partition is an unordered multiset of positive parts. Independent multiplicities give

$$P(x)=\prod_{j\ge1}\frac{1}{1-x^j},\qquad P(x,u)=\prod_{j\ge1}\frac{1}{1-ux^j}.$$

The exponent of $u$ counts parts. The infinite product is formally valid: only factors with $j\le n$ can affect degree $n$. Distinct parts replace each inverse factor by $1+x^j$. Odd parts retain only odd-index factors. The factor identity $1+x^j=(1-x^{2j})/(1-x^j)$ proves that distinct-part and odd-part partitions have identical OGFs: cancellation is justified coefficientwise by truncation, not by uncontrolled numerical products.

Ferrers conjugation exchanges number of parts and largest part. Consequently partitions into exactly $k$ positive parts have OGF $x^k/\prod_{j=1}^{k}(1-x^j)$. Distinct positive $k$-part partitions remove a staircase of $k(k-1)/2$ cells and therefore have numerator $x^{k(k+1)/2}$ over the same denominator. The staircase offset preserves positivity of the reduced rows.

The largest square in a Ferrers diagram has a unique size $d$. Its right arm has at most $d$ rows and its lower leg has largest part at most $d$. Their independent OGFs produce the Durfee-square decomposition

$$P(x)=\sum_{d\ge0}\frac{x^{d^2}}{\prod_{j=1}^{d}(1-x^j)^2}.$$

For any target degree only $d^2\le n$ contributes. This identity includes the empty partition at $d=0$, with the empty product defined as one. Self-conjugate diagrams decompose into distinct odd-length diagonal hooks, so their OGF is the product of $1+x^j$ over odd positive $j$.

### Reconstructing a self-conjugate diagram from its hooks

Number the diagonal cells from the top left. In a self-conjugate diagram, the arm and leg of the $i$th diagonal cell have equal length $a_i$, so its diagonal hook has length $2a_i+1$. Successive arm lengths are strictly decreasing: the row length cannot increase, while the diagonal index increases by one. The hook lengths are therefore distinct odd positive integers. Every cell belongs to exactly one diagonal hook: a cell weakly above the diagonal belongs to its row's diagonal hook, and a cell below it belongs to its column's diagonal hook. The total hook length equals the total number of cells.

Conversely, sort a finite collection of distinct odd hook lengths in decreasing order and write them as $2a_i+1$. Put $a_i$ cells to the right and $a_i$ cells below diagonal cell $i$. Strict decrease ensures that the resulting row lengths are nonincreasing and that the diagonal cells and their hooks form one Ferrers diagram. Transposition preserves the construction. Extracting the diagonal hooks recovers the original lengths, so the two constructions are inverse bijections. This proves the product over distinct odd lengths and explains why ordinary odd parts with unrestricted repetition represent a different class.

<!-- SIM: partitions -->

## 17. Catalan structures, branch selection, and a removable quotient

A nonempty balanced-parenthesis word decomposes uniquely as a left parenthesis, a balanced interior, a right parenthesis, and a balanced suffix. Count pairs, not individual characters. If $C$ includes the empty word, this construction gives

$$C(x)=1+xC(x)^2,\qquad C(x)=\frac{1-\sqrt{1-4x}}{2x}.$$

The square root is the normalized formal root with constant one. The negative branch is required because its numerator has zero constant coefficient and is divisible by $x$; the positive branch would have a negative power. The resulting quotient has constant one even though direct numerical substitution gives an apparent zero divided by zero. Formal division after cancellation resolves it.

Expand the normalized square root using generalized binomial coefficients. Comparing degree $n+1$ in the numerator gives $C_n=-(1/2)\binom{1/2}{n+1}(-4)^{n+1}$. Multiplying out the finite descending product reduces this to $\binom{2n}{n}/(n+1)$. The result counts ordered binary trees with $n$ internal vertices, balanced strings with $n$ pairs, and polygon triangulations with $n+2$ vertices, under the corresponding precise conventions.

An ordered rooted tree with all its vertices counted satisfies $T=x/(1-T)$, since its children form an ordered sequence of nonempty rooted trees. Thus $T=xC$, and its size-$n$ count is $C_{n-1}$ for positive $n$. The empty tree is absent in this latter class, so its constant coefficient is zero.

<!-- SIM: catalan -->

## 18. Formal composition and coefficient inversion

For an infinite outer series $F$ and inner series $G$ with zero constant coefficient, composition is well-defined: to compute degree $n$, only finitely many powers of $G$ contribute. A polynomial outer expression can be composed with any inner series. These are sufficient standard conditions; claims about more general rings require separate hypotheses.

The equation $T=x\phi(T)$ with $\phi(0)\ne0$ has a unique zero-constant formal solution: degree $n$ on the right depends only on previously determined coefficients. For positive integers $n,k$, coefficient inversion gives

$$[x^n]T(x)^k=\frac{k}{n}[t^{n-k}]\phi(t)^n.$$

Here is a formal proof, not an appeal to a numerical inverse function. Define the residue of a Laurent series to be its coefficient of exponent minus one. Residues of derivatives vanish. Under a change $x=g(t)$ with nonzero linear coefficient, the residue of $F(x)$ equals the residue of $F(g(t))g'(t)$. It suffices to check monomials: for an exponent other than minus one the transformed expression is a constant multiple of the derivative of a power of $g$; for exponent minus one, write $g=t h(t)$ with $h(0)\ne0$, and $g'/g=1/t+h'/h$ has residue one.

Now take $g(t)=t/\phi(t)$ so that $T(g(t))=t$. The target is the residue of $t^k g(t)^{-n-1}g'(t)$. Since $(g^{-n})'=-n g^{-n-1}g'$, the zero-residue product derivative gives this target as $(k/n)$ times the residue of $t^{k-1}g^{-n}$. Substituting $g=t/\phi(t)$ proves the displayed formula. All products have finite negative tails and all substitutions used here are legitimate formal Laurent substitutions.

For $\phi(t)=(1+t)^m$, one obtains $[x^n]T=\binom{mn}{n-1}/n$. For rooted labelled trees, $\phi(t)=e^t$ gives coefficient $n^{n-1}/n!$. Multiply by $n!$ to recover the number of labelled structures. These statements use different combinatorial classes even though the same algebraic theorem extracts both.

## 19. Exponential generating functions and labelled products

For a count $a_n$ on a fixed set of $n$ distinct labels, define the EGF

$$\widehat A(x)=\sum_{n\ge0}a_n\frac{x^n}{n!},\qquad a_n=n![x^n]\widehat A(x).$$

To combine an $A$ structure and a $B$ structure on disjoint subsets of the label set, first choose which $i$ labels belong to the first structure, then choose both structures. Therefore the product count is

$$c_n=\sum_{i=0}^{n}\binom{n}{i}a_i b_{n-i}.$$

Multiplying the two EGFs yields precisely $c_n/n!$, proving the labelled product rule. This binomial coefficient records label allocation and is absent from ordinary convolution. The same algebraic expression $1/(1-x)$ is an OGF for the all-ones sequence but an EGF for factorial counts; its interpretation must always be stated.

The EGF for arbitrary label sets with one trivial structure each is $e^x$. A nonempty set has EGF $e^x-1$; exactly $j$ labels have EGF $x^j/j!$. Distinct recipients receiving labelled items independently correspond to a product of such recipient EGFs. Identical recipients require an unordered set-of-components construction, not the same product with recipient names silently erased.

<!-- SIM: labelled -->

## 20. Surjections, Stirling numbers, and Bell structures

Distributing $n$ labels onto $k$ distinct nonempty recipients has EGF $(e^x-1)^k$. Expanding by the ordinary binomial theorem gives the inclusion-exclusion count

$$k!S(n,k)=\sum_{j=0}^{k}(-1)^{k-j}\binom{k}{j}j^n.$$

The convention $0^0=1$ here represents the unique function from an empty domain to an empty codomain; it is a combinatorial convention for this formula. Dividing by $k!$ forgets the recipient ordering because every partition into $k$ nonempty blocks has exactly $k!$ recipient assignments. Empty blocks would destroy this free permutation action, so the nonempty condition is essential.

Summing over the number of blocks gives the Bell EGF $\exp(e^x-1)$. Marking blocks by $u$ gives $\exp(u(e^x-1))$. Restricting block sizes to a positive set $S$ replaces the inner expression by $\sum_{j\in S}x^j/j!$. For blocks of size exactly two, the EGF $\exp(x^2/2)$ counts perfect pairings: on $2m$ labels its count is $(2m)!/(2^m m!)$, and on an odd number it is zero.

## 21. Labelled composition, cycles, derangements, and ordered blocks

To make a set of nonempty component structures with EGF $B$, partition the labels into component blocks and independently structure each block. Ordering $k$ components gives $B^k$; every unordered set has $k!$ orderings because blocks are nonempty and disjoint. Summing $B^k/k!$ gives $\exp(B)$. More generally, imposing an outer structure with count $a_k$ on the set of blocks gives $\widehat A(B)$.

A cycle on $j\ge1$ labels has $(j-1)!$ arrangements, since rotations of a list describe the same directed cycle. Its EGF contribution is $x^j/j$, so all positive cycles have series $-\log(1-x)$. A permutation is an unordered set of cycles; exponentiation recovers $1/(1-x)$ as an EGF for $n!$. Excluding one-cycles gives the derangement EGF $e^{-x}/(1-x)$ and count

$$D_n=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}.$$

Restricting cycles to lengths one and two gives $\exp(x+x^2/2)$ for involutions. Ordered nonempty blocks instead give $1/(2-e^x)$, because the outer EGF for linear orders is $1/(1-t)$. The interpretation is an ordered set partition, not an ordinary sequence of unlabelled subsets.

## 22. Derivatives, distinguished labels, and recursive EGFs

Differentiating an EGF shifts the count without an index multiplier: $\widehat A'=\sum a_{n+1}x^n/n!$. This counts structures on the existing labels plus one new distinguished label. Multiplication by $x$ after differentiating instead counts an existing label distinguished among the $n$ labels, with count $n a_n$. These two meanings are often conflated.

For rooted unordered labelled trees, the root is a single label and its branches form an unordered set of nonempty rooted trees, so $T=xe^T$. The coefficient-inversion proof yields the rooted count $n^{n-1}$. For an unrooted labelled tree with positive $n$, each has $n$ choices of root; dividing gives Cayley's $n^{n-2}$ for $n\ge2$, with a separately defined one-vertex count one.

For odd alternating permutations with the up-down pattern, separating the largest label divides the remaining labels into two nonempty alternating sides, except for the singleton boundary. Its EGF satisfies $A'=1+A^2$, $A(0)=0$. Coefficients recursively determine the tangent series. This argument uses the intrinsic order of the labels; it is not a relabelling-invariant species on arbitrary named sets. That distinction is noted in Berkeley's course correction and retained here.

## 23. Two-variable marking, averages, and distinct leaf definitions

Let $F(x,u)=\sum f_{n,k}x^n u^k$ count size and a parameter. After differentiating in $u$ and setting $u=1$, the coefficient of $x^n$ is the total parameter across all size-$n$ objects. Divide by $[x^n]F(x,1)$ to get the mean when size-$n$ objects are uniformly distributed and that denominator is positive. A second derivative gives the total falling factorial $k(k-1)$, not the second moment $k^2$.

For all binary strings, $F=1/(1-x(1+u))$ when $u$ marks ones. Its parameter derivative at one is $x/(1-2x)^2$, giving total ones $n2^{n-1}$ and mean $n/2$.

For ordered binary trees, call an internal vertex with two empty children an internal leaf. The empty tree has zero internal leaves. The bivariate equation is $T(x,u)=1+x(T(x,u)^2-1+u)$: replace the one root-with-both-children-empty term by a marked root. Differentiating and setting $u=1$ gives

$$L(x)=x+2xC(x)L(x)=\frac{x}{\sqrt{1-4x}}.$$

For $n\ge1$, the total internal-leaf count is $\binom{2n-2}{n-1}$; dividing by $C_n$ gives $n(n+1)/(2(2n-1))$. This is not the number of external null leaves, which is exactly $n+1$ in every size-$n$ tree. Different leaf definitions produce different answers.

<!-- SIM: marking -->

## 24. Probability generating functions and analytic hypotheses

For a nonnegative integer-valued random variable $X$, its PGF is $G(s)=\sum p_n s^n$ with probabilities as coefficients. It is an OGF with nonnegative coefficients summing to one. Unlike an arbitrary formal counting OGF, it converges absolutely for complex modulus at most one. Then $G(0)$ is the probability of zero, $G(1)=1$, and independent sums have PGF products. Independence is the reason products encode probability convolution.

With finite moments, derivatives approaching one from below give $G'(1)=E[X]$ and $G''(1)=E[X(X-1)]$. Hence $\operatorname{Var}(X)=G''(1)+G'(1)-G'(1)^2$. If a moment is infinite, the corresponding boundary derivative can diverge; the finite formula must not be asserted without its hypotheses.

For a binomial variable, $G=(1-p+ps)^n$. For the number of failures before a geometric success, $G=p/(1-(1-p)s)$. For a Poisson variable, $G=\exp(\lambda(s-1))$. A geometric variable counting trials includes one extra factor of $s$ and has a different mean. The support convention must be stated before differentiating.

## 25. Exact coefficients versus asymptotic growth

A rational OGF's partial fractions give an exact finite sum of exponential-polynomial terms, plus a finite prefix. Growth depends on the surviving terms, including their coefficients. A pole at $\rho$ yields exponential base $\rho^{-1}$. Repeated poles add polynomial factors. Several equal-modulus poles can create oscillation or periodic zero coefficients; the modulus alone cannot justify a positive Theta bound on every index.

For example, $1/(1-x^2)$ has coefficients one on even indices and zero on odd indices. Its two poles have equal modulus. For $1/((1-x)(1-2x))$, the surviving base two dominates and coefficients are asymptotic to $2^{n+1}$. Cancellation of the base-two factor would change that conclusion completely.

Catalan coefficients have growth asymptotic to $4^n/(\sqrt{\pi}n^{3/2})$, obtained from their exact binomial formula and Stirling's factorial approximation. This conclusion uses an asymptotic factorial theorem; it is distinct from the purely formal branch-selection proof. General singularity-transfer theorems require complex analytic conditions and are not presented here as automatic rules for every formal expression.

## 26. An exact verification workflow for exam problems

First identify the counted objects, distinguishability, size variable, lower bounds, and ordering. Write one factor for each independent choice and justify unique reconstruction. For a recurrence, write its starting index and every initial value before forming the series equation. For an EGF, show where label allocations or factorial divisions enter.

Next simplify the expression while retaining finite prefixes and excluded terms. Extract coefficients using the appropriate dictionary, convolution, recurrence, or formal inversion theorem. Check the smallest admissible case and at least one nontrivial case by a second method, such as enumeration, integer dynamic programming, or a direct recurrence. A correct-looking rational expression with a wrong constant term is already falsified.

Finally state the exact answer's domain, separate analytic conclusions from formal ones, and report whether an official exam answer key was used. Our authentic bridges use independently derived answers checked against the original problem statement; they are not labelled official answer keys.

## 27. Complete chapter summary

An OGF is a formal coefficient sequence. Its product is ordinary convolution, and its reciprocal is uniquely determined by a nonzero constant coefficient over a field. Coefficient extraction is linear but does not turn products into products of equal-index coefficients. Shifts must retain or remove the appropriate initial terms; differentiation, prefix summation, and substitution transform index weights in precise ways.

Independent additive-size choices produce products; disjoint alternatives produce sums. Ordered positive-size sequences produce a geometric inverse. Bounded distributions produce finite numerator corrections; unordered coin selections and integer partitions produce products of multiplicity factors. Their ordered counterparts instead require sequence constructions. Infinite products are legitimate when only finitely many factors affect a target coefficient.

Reduced rational denominators determine exact exponential-polynomial coefficients, while finite polynomial parts determine initial exceptions. Recurrence OGFs require all boundary corrections. Catalan functional equations choose the branch that belongs to the power-series ring. Formal inversion extracts coefficients from recursive equations under explicit zero-constant and nonzero-linear conditions.

EGFs normalize by factorials so that multiplication automatically accounts for allocating distinct labels. Nonempty labelled blocks justify factorial division, composition, Bell counts, cycle decomposition, derangements, involutions, and rooted trees. Parameter derivatives yield total statistics, from which means are computed with a declared probability model. PGFs are OGFs with normalized nonnegative coefficients and separate moment hypotheses. These distinctions, together with the worked problems and the full final-rule section, form the method-selection framework for new formula and concept questions.

## 28. Worked formula and concept problems

<!-- INCLUDE: problems -->

## 29. Final reasoning rules and examination traps

<!-- INCLUDE: review -->

## 30. Editable exact generating-function laboratory

<!-- LAB: generating -->

## 31. References

1. Eric Lehman, F. Thomson Leighton, Albert R. Meyer. MIT 6.042J, Mathematics for Computer Science, Spring 2015, Chapter 15, one-based PDF pages 636–670. [Official textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf).
2. Mark Haiman. UC Berkeley Math 172, Combinatorics, Spring 2010. [Course](https://math.berkeley.edu/~mhaiman/math172-spring10/), [Ordinary Generating Functions](https://math.berkeley.edu/~mhaiman/math172-spring10/ordinary.pdf), [Exponential Generating Functions and Structures](https://math.berkeley.edu/~mhaiman/math172-spring10/exponential.pdf), [Partitions and Their Generating Functions](https://math.berkeley.edu/~mhaiman/math172-spring10/partitions.pdf).
3. Carnegie Mellon 15-251. Generating Functions, Lecture 8, 20 September 2012, handout originally written by John Lafferty in 2008, all 9 pages. [Official handout](https://www.andrew.cmu.edu/course/15-251/Notes/gen-functions.pdf).
4. Robert Sedgewick. Princeton Analysis of Algorithms / Analytic Combinatorics Part One, Lecture 3, Generating Functions, all 52 written slides; companion text with Philippe Flajolet. [Course listing](https://aofa.cs.princeton.edu/online/), [author's official slide mirror](https://sedgewick.io/wp-content/uploads/2022/04/AA03-GFs.pdf).
5. Iranian MSc and doctoral examination originals. Exact repository paths, source commit, question number, PDF page, and checked adaptation are provided beside each authentic bridge. The solution is independently derived unless a different provenance is explicitly stated.
