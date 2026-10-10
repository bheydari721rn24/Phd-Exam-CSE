### 49. Catalan convolution from first return

Use the unique first-return decomposition of balanced words to compute the number with four pairs, retaining every convolution term.

#### Solution

The empty count is one. For a nonempty word of four pairs, its first enclosing pair contains $i$ pairs and its suffix contains $3-i$ pairs. Thus $C_4=C_0C_3+C_1C_2+C_2C_1+C_3C_0=5+2+2+5=14$. The cases are disjoint because the matching parenthesis for the first opening symbol is unique. The OGF equation $C=1+xC^2$ represents this same convolution over all sizes. It is not $1+xC$; both the interior and suffix are independently chosen balanced words. The closed binomial formula gives $\binom{8}{4}/5=14$ as an independent check.

### 50. Selecting a formal square-root branch

Solve $Y=1+xY^2$ as a formal power series and explain why its algebraic second root is inadmissible.

#### Solution

The quadratic formula gives $(1\pm\sqrt{1-4x})/(2x)$. Choose the normalized square root with constant one. The minus numerator has zero constant and begins with $2x$, so its quotient is a power series with constant one. The plus numerator has constant two and produces a term $1/x$, outside the ordinary power-series ring. Recursive coefficient comparison uniquely determines all nonnegative coefficients from the constant one, confirming that only the minus branch is admissible. No numeric choice of “smaller root” is needed; the branch is selected by the series domain and prescribed initial coefficient.

### 51. Ordered rooted trees count all vertices

Find the number of ordered rooted unlabelled trees on five vertices, and compare it with binary trees counted by internal vertices.

#### Solution

For an ordered rooted tree, each child contributes a nonempty rooted subtree and the children form an ordered sequence. Therefore $T=x/(1-T)$ with zero constant coefficient. Its solution is $T=xC$, so the five-vertex count is $C_4=14$. Ordered binary trees with five internal vertices have count $C_5=42$, under a different size convention and child-slot model. The shift in the first answer is not a harmless relabelling of the same index: a nonempty general rooted tree counts its root, while the Catalan series includes an empty binary tree at index zero. Always identify the object class and size before applying a Catalan number.

### 52. A ternary recursive structure through coefficient inversion

Let $T=x(1+T)^3$. Find $[x^5]T$ and derive the answer from the proved inversion theorem.

#### Solution

Take $\phi(t)=(1+t)^3$. For positive $n$, the theorem gives $[x^n]T=\binom{3n}{n-1}/n$. At five this is $\binom{15}{4}/5=1365/5=273$. The zero-constant solution is unique because each new coefficient depends on earlier ones; its first coefficients 1,3,12,55,273 can also be obtained by truncated substitution. The three positions encoded by $(1+T)^3$ are ordered optional subtree slots. An unordered set of three subtrees would not have the same expression. This illustrates how the algebraic theorem still requires a correct combinatorial specification.

### 53. Extracting a power of a recursive solution

For the same $T=x(1+T)^3$, find $[x^6]T^2$ and explain why a zero answer is forced below degree two.

#### Solution

Use coefficient inversion with $k=2$, $n=6$: the coefficient is $(2/6)[t^4](1+t)^{18}=\binom{18}{4}/3=3060/3=1020$. A direct check convolves the first five positive coefficients: the contributions at total six are $2\cdot273+2\cdot3\cdot55+12^2=546+330+144=1020$. Since $T$ has no constant and begins at degree one, its square begins at degree two. Negative-index extraction in the theorem likewise returns zero when $n<k$. The factor $k/n$ cannot be omitted; it is a consequence of the formal residue derivative in the proof.

### 54. Labelled rooted trees and factorial normalization

Use $T=xe^T$ to count rooted labelled trees on five labels.

#### Solution

The ordinary coefficient of this EGF is $(1/5)[t^4]e^{5t}=5^4/(5\cdot4!)=5^4/5!$. Multiply by $5!$ to obtain the labelled count $5^4=625$. The root is one distinguished label and the branches form an unordered set of nonempty rooted trees, which explains the exponential construction. If the problem asked for unrooted labelled trees on five labels, divide by five, giving 125, because every unrooted tree has exactly five choices of root. The EGF coefficient itself is a rational normalized value and is not the raw integer count.

### 55. The same formula has two different interpretations

Interpret $1/(1-x)$ as an OGF and as an EGF. Then interpret $e^{2x}$ in both ways.

#### Solution

The geometric expression has ordinary coefficients one, so as an OGF it counts one object at every size. As an EGF it represents counts $n!$, because normalized coefficients are the raw counts divided by factorials. The exponential expression has ordinary coefficients $2^n/n!$, which need not be integers; as an EGF its raw counts are $2^n$. An expression's analytic or formal shape does not determine its counting interpretation. At index three, the geometric raw count is one in the OGF interpretation and six in the EGF interpretation. Stating the generating-function type beside a coefficient query prevents this fundamental normalization error.

### 56. A labelled product allocates the labels

Split five distinct labels into an ordered pair of sets, allowing either to be empty. Count the structures by an EGF product and compare with indistinguishable units.

#### Solution

Each set has one trivial structure, with EGF $e^x$. The ordered pair has EGF $e^{2x}$ and raw size-five count $2^5=32$. Equivalently, choose which labels go to the first set; there are $\sum_{i=0}^{5}\binom{5}{i}=32$ choices. Five indistinguishable units split between two named recipients instead have six multiplicity vectors, with OGF $(1-x)^{-2}$. The difference is the binomial allocation of distinct labels. Multiplication is formally the same operation in both series types, but their coefficient normalizations implement different combinatorial products.

### 57. Surjections onto three recipients

Count surjections from six distinct labels onto three named recipients and obtain the number of partitions into three nonempty blocks.

#### Solution

The EGF for surjections is $(e^x-1)^3$. Expanding gives raw count $3^6-3\cdot2^6+3\cdot1^6=729-192+3=540$. The missing constant-codomain term is zero since the domain is nonempty. Each partition into three blocks has $3!$ assignments to the three named recipients, so $S(6,3)=540/6=90$. The division is valid because every block is nonempty and distinct as a subset of the labels. If empty recipients were allowed, multiple empty blocks would not have the same free ordering multiplicity. Direct Stirling insertion recurrence provides a second integer computation of 90.

### 58. Labelled distributions with unequal occupancy constraints

Distribute five distinct labels into three named boxes: the first has exactly two labels, the second is nonempty, and the third is unrestricted. Find the count.

#### Solution

The EGF is $(x^2/2)(e^x-1)e^x$. The residual degree three is that of $e^{2x}-e^x$, namely $(2^3-1)/3!=7/6$. Multiplying by the first factor and then by $5!$ gives $120\cdot7/12=70$. Directly choose the first two labels in ten ways, then assign the remaining three between the second and third boxes with the second nonempty, in $2^3-1=7$ ways. The factorial in the first factor is required to represent exactly one trivial set structure on two labels. Replacing it by $x^2$ would double the count.

### 59. Perfect pairings as an unordered set of pairs

Count perfect pairings of eight distinct labels and explain every divisor.

#### Solution

One pair has EGF $x^2/2!$; an unordered set of pairs has EGF $\exp(x^2/2)$. Its degree-eight coefficient is $1/(2^4 4!)$. Multiply by $8!$ to get $40320/(16\cdot24)=105$. Directly order the eight labels, divide by two for the internal order of each of four pairs, and divide by $4!$ for the order of the four pairs. The same divisors arise in the EGF expansion. An odd number of labels gives zero because all nonzero powers are even. The construction has no empty pair component, which is why the exponential set rule is legitimate.

### 60. Set partitions into blocks of size one or two

Count partitions of six labels whose blocks have size one or two.

#### Solution

The EGF is $\exp(x+x^2/2)$. If there are $j$ pairs, there are $6-2j$ singleton blocks, and the count is $6!/((6-2j)!2^j j!)$. Sum for $j=0,1,2,3$: the contributions are 1,15,45,15, totaling 76. These cases are disjoint by the number of pairs. This also counts involutions as permutations made only of one-cycles and two-cycles. Larger cycles are absent, not merely unmarked. A recurrence choosing whether a distinguished label is fixed or paired gives $I_n=I_{n-1}+(n-1)I_{n-2}$ and confirms the same value.

### 61. Bell EGF with an excluded singleton component

Count partitions of four labels with no singleton blocks.

#### Solution

Remove the singleton term from the nonempty-block EGF, giving $B(x)=e^x-1-x$. The set of such blocks has EGF $\exp(B)$. At degree four, possible block-size patterns are one block of size four or two blocks of size two. Their counts are one and three, giving four. In the series, the size-four block contributes $1/24$, while two pairs contribute $(x^2/2)^2/2!=x^4/8$; multiplying their sum by $4!$ gives four. Using $\exp(e^x-1)$ would include singleton-containing partitions, so removing the component term is required before exponentiating.

### 62. Exactly two even-size blocks

Count partitions of six labels into exactly two nonempty even-size blocks.

#### Solution

The component EGF is $\cosh x-1=x^2/2!+x^4/4!+\cdots$. Exactly two unordered components give its square divided by two. Degree six comes from block sizes two and four; the two factor orders cancel the outside divisor, leaving coefficient $1/(2!4!)$. Multiply by $6!$ to obtain 15. Directly choose the two-element block in $\binom{6}{2}=15$ ways; the other block is forced and has a different size, so no further division by two is needed in this direct count. Applying both the EGF division and a second direct division would undercount.

### 63. Ordered nonempty blocks

Count ordered set partitions of four labels and compare with ordinary Bell partitions.

#### Solution

Order the blocks of an ordinary partition. The count is $\sum_{k=0}^{4}k!S(4,k)=1+2!\cdot7+3!\cdot6+4!=1+14+36+24=75$, where the one-block contribution is one and the empty-block contribution is zero at positive size. The EGF is $1/(2-e^x)$, whose size-four normalized coefficient is $75/24$. Ordinary partitions have $B_4=15$. The ordered answer is not $4!B_4$, because the number of blocks varies and each partition has only $k!$ block orders. An EGF recurrence or direct enumeration by block count confirms 75.

### 64. Derangements via cycle exclusion

Find the number of derangements on six labels from an EGF and confirm it by the recurrence.

#### Solution

Exclude cycles of length one, giving $e^{-x}/(1-x)$. Multiply coefficients and remove normalization: $D_6=6!\sum_{j=0}^{6}(-1)^j/j!=265$. The integer recurrence has boundaries $D_0=1$, $D_1=0$, then gives 1,2,9,44,265 at sizes two through six. It follows from whether a distinguished label forms a two-cycle or belongs to a longer cycle. The EGF derivation and recurrence are independent descriptions of the same excluded-fixed-point class. Rounded values of $n!/e$ are a convenient derived approximation, but the finite alternating sum gives the exact result without numerical rounding uncertainty.

### 65. Permutations with exactly two cycles

Count permutations of five labels having exactly two directed cycles.

#### Solution

The cycle EGF is $L=-\log(1-x)$. Exactly two unordered cycles have EGF $L^2/2$. Degree five receives ordered size splits one/four and two/three. After the outside division, its coefficient is $1/4+1/6=5/12$. Multiply by $5!=120$ to obtain 50. Directly, the first cycle-size pattern contributes choosing the singleton in five ways and cycling the other four in six ways, giving 30. The two/three pattern contributes choosing the pair in ten ways and cycling the other three in two ways, giving 20. Their sum confirms 50 and explains the distinction between cycle order and within-cycle orientation.

### 66. Exactly one three-cycle and all other labels fixed

Count permutations on seven labels with exactly one three-cycle and no other nontrivial cycle.

#### Solution

The distinguished cycle component contributes $x^3/3$ and unrestricted singleton cycles contribute $e^x$. The EGF is $(x^3/3)e^x$. Its size-seven count is $7!/(3\cdot4!)=70$. Directly choose the three moving labels in $\binom{7}{3}=35$ ways and choose one of their two directed cycles. All other labels are fixed, so there is no additional ordering. A factor $e^{x^3/3}$ would allow several three-cycles, while a factor $1/(1-x)$ would allow arbitrary permutations on the remaining labels. Exact restrictions must be built into the component expression.

### 67. EGF differentiation introduces a new distinguished label

For $a_n=n!$, determine the counts represented by $\widehat A'$ and $x\widehat A'$ and explain their different meanings.

#### Solution

The EGF is $(1-x)^{-1}$. Its derivative is $(1-x)^{-2}$, with normalized coefficient $n+1$ and raw count $(n+1)!$. It counts permutations on the existing labels plus one new distinguished label. Multiplying that derivative by $x$ gives raw count $n\cdot n!$ for positive $n$, and zero at zero; it represents a permutation on the existing labels together with a marked existing label. At size two the counts are six and four respectively. The extra variable changes both the index and factorial normalization. Saying merely “differentiate to mark an item” leaves these two constructions ambiguous.

### 68. Odd alternating permutations from an EGF equation

Use $A'=1+A^2$, $A(0)=0$, to compute the number of odd up-down alternating permutations on five ordered labels.

#### Solution

Let $a_n$ be the raw EGF counts. The derivative equation gives $a_{n+1}=\sum_{k=0}^{n}\binom{n}{k}a_k a_{n-k}$ for positive $n$, with $a_1=1$ from the constant one and $a_0=0$. At $n=2$, only the split one/one survives, giving $a_3=2$. At $n=4$, splits one/three and three/one contribute $4\cdot1\cdot2$ each, so $a_5=16$. Even-sized counts in this odd-only class are zero. The usual order on the labels is part of the alternating definition; this class cannot be interpreted as an arbitrary relabelling-invariant species without additional order data.

### 69. Marking ones in binary words

Find the mean and variance of the number of ones in a uniformly selected length-six binary word by a two-variable OGF.

#### Solution

The marked OGF is $F=1/(1-x(1+u))$. Degree six is $(1+u)^6$. Its first derivative at one gives total ones $6\cdot2^5=192$, divided by 64 words to give mean three. Its second derivative gives total $k(k-1)$ equal to $6\cdot5\cdot2^4=480$, so the factorial second moment is $480/64=7.5$. Add the mean to obtain the ordinary second moment 10.5, then subtract the squared mean nine to get variance 1.5. The calculation independently matches a binomial variable with six trials and success probability one-half. Forgetting to add the mean would confuse a falling-factorial moment with a square moment.

### 70. Two meanings of a binary-tree leaf

For uniformly selected ordered binary trees with four internal vertices, compute the expected number of internal leaves and the number of external null leaves.

#### Solution

The Catalan total is $C_4=14$. The marked internal-leaf series is $L=x/\sqrt{1-4x}$, so the total internal leaves is $\binom{6}{3}=20$, giving mean $20/14=10/7$. Every tree with four internal vertices has five external null leaves, so that second statistic is deterministically five. The first formula counts internal vertices with two empty children; the second counts absent child slots. For the empty tree, there are zero internal leaves but one external null leaf under the extended-tree convention. This boundary and terminology must be explicit before using a leaf-generating function.

### 71. A finite inventory probability model

Choose uniformly a nonnegative pair summing to six. Let $X$ be its first entry. Find its PGF, mean, and variance.

#### Solution

There are seven equally likely pairs, so $G(s)=(1+s+\cdots+s^6)/7$. The mean is $(0+1+\cdots+6)/7=3$. The ordinary second moment is $(0^2+1^2+\cdots+6^2)/7=91/7=13$, giving variance four. PGF differentiation yields the same result: $G'(1)=3$ and $G''(1)=10$, hence $10+3-9=4$. A generating function for counts must be divided by the actual number of equiprobable outcomes before it becomes a probability generating function. The two coordinates are dependent because their sum is fixed; their marginal PGFs cannot be multiplied to recover the fixed-sum joint model.

### 72. Geometric support conventions

A success has probability one-quarter. Find the PGF and mean of failures before the first success, then of trials through that success.

#### Solution

Failures have probabilities $(1/4)(3/4)^n$ for nonnegative $n$. Their PGF is $(1/4)/(1-(3/4)s)$ and its derivative at one is three. The trials count is failures plus one, so its PGF is $sG(s)$ and its mean is four. The trial-count constant coefficient is zero, whereas the failures constant coefficient is one-quarter. That small-index difference fixes the support convention. Both derivatives are finite because these geometric distributions have exponentially decaying tails. Applying a remembered geometric mean without stating whether it counts failures or trials would risk a one-unit error.

### 73. Independent Poisson sums

For independent Poisson variables of means two and three, derive the distribution, mean, and variance of their sum using PGFs.

#### Solution

Their PGFs are $e^{2(s-1)}$ and $e^{3(s-1)}$. Independence gives the product $e^{5(s-1)}$, which is the PGF of a Poisson variable with mean five. Differentiate at one: the first derivative is five and the second is 25. Therefore variance is $25+5-25=5$. The coefficient formula is $e^{-5}5^n/n!$, so every probability is nonnegative and the coefficients sum to one. Without independence, the product rule is not valid and the marginal means alone do not determine the sum distribution or variance.

### 74. A distribution with an infinite mean

Let $p_n=1/((n+1)(n+2))$ for $n\ge0$. Show it is a probability distribution and determine whether its PGF derivative at one is finite.

#### Solution

Write $p_n=1/(n+1)-1/(n+2)$. The partial sums telescope to $1-1/(N+2)$ and tend to one, so the probabilities are normalized. The mean term is $n/((n+1)(n+2))$, which behaves like $1/n$ and produces a divergent harmonic-type sum. For example, for $n\ge2$ it is at least $1/(4n)$, proving divergence by comparison. Thus the left boundary derivative $G'(1)$ is infinite, although the PGF itself converges at one. Convergence of a probability series at its boundary does not imply finite derivative moments. A finite variance formula cannot be used here.

### 75. Dominant poles with periodic zero terms

Can coefficients of $1/(1-4x^2)$ be described as Theta of $2^n$ on every nonnegative index? Give the exact answer and a valid restricted growth statement.

#### Solution

Expansion gives $a_{2j}=4^j=2^{2j}$ and $a_{2j+1}=0$. A positive Theta lower bound by $2^n$ fails at every odd index, so the proposed statement is false for the complete sequence. On the even subsequence, the coefficients equal $2^n$ exactly. The two poles at plus and minus one-half have equal modulus and their contributions cancel on odd indices. One may give an upper bound $O(2^n)$ for all indices and an exact residue-class statement. Inspecting only the positive pole would discard a surviving term needed for exact and asymptotic behavior.

### 76. A numerator removes the largest exponential base

Determine the sequence and growth for $(1-3x)/((1-2x)(1-3x))$.

#### Solution

Cancel $1-3x$ to obtain $(1-2x)^{-1}$, with coefficients $2^n$. The sequence is exactly Theta of $2^n$, not Theta of $3^n$. The apparent pole at one-third is removable; no contribution with base three survives. In particular, the ratio of the actual coefficients to $3^n$ is $(2/3)^n$, which tends to zero and disproves a base-three lower bound. This example requires no complex analysis, only exact rational simplification. Growth statements must be made after reducing the function and checking the coefficients of every purported dominant term.

### 77. A repeated dominant pole with an exact shift

Find an exact and an asymptotic expression for $[x^n]x^3/(1-2x)^4$.

#### Solution

For $n\ge3$, shift the target to $n-3$, obtaining $2^{n-3}\binom{n}{3}$. For lower indices the coefficient is zero. Since $\binom{n}{3}=n(n-1)(n-2)/6$, the positive-index coefficients are asymptotic to $n^3 2^n/48$. The factor 48 combines the binomial leading coefficient six and the exponential shift eight. Merely identifying a fourth-order pole predicts a cubic polynomial multiplier but not this exact constant or the three zero initial coefficients. The exact formula also shows a valid Theta bound for sufficiently large indices, with no periodic cancellations.

### 78. A counting model with a nonuniform statistic

Choose uniformly a composition of five into positive parts. Compute the expected number of parts from a marker and verify it by the separator interpretation.

#### Solution

The marked OGF is $F=(1-x)/(1-x-ux)$. Differentiate in $u$ and set $u=1$ to get $x(1-x)/(1-2x)^2$. Degree five is $5\cdot2^4-4\cdot2^3=48$. There are $2^4=16$ compositions, so the mean is three. Alternatively, a composition of five chooses a subset of the four interior separators; each separator occurs in half the subsets. The number of parts is one plus the number of chosen separators, giving $1+4/2=3$. The empty composition has zero parts and a different boundary, so this positive-size formula must not be extended to zero without qualification.

### 79. A nonlinear recurrence that is not a rational OGF

For $c_0=1$ and $c_n=\sum_{i=0}^{n-1}c_i c_{n-1-i}$, derive its functional equation and explain why the finite-lag rational-recurrence recipe does not apply.

#### Solution

Multiply the convolution recurrence by $x^n$ and sum from one. The shifted double sum is $xC^2$, so $C=1+xC^2$. Its valid solution is the Catalan square-root expression, which is algebraic and not rational. The recurrence is nonlinear in its previous values and uses a growing number of lags, so it is outside the constant-coefficient finite-lag theorem. Formal generating functions still work because convolution is represented by a product, but “use a generating function” does not mean “expect partial fractions.” The first values 1,1,2,5,14 provide a direct coefficient check of the functional equation.

### 80. A complete method-selection synthesis

Compare three counts at total six: ordered strings of parts one or two; unordered selections of those weights; and partitions of six distinct labels into singleton or pair blocks. Derive all three answers with the correct generating-function type.

#### Solution

Ordered positive-size components give OGF $(1-x-x^2)^{-1}$ and coefficient 13 at six, by the Fibonacci-type last-component recurrence. Unordered multiplicities give OGF $((1-x)(1-x^2))^{-1}$ and coefficient four, according to zero through three copies of weight two. Distinct labels partitioned into unordered singleton and pair blocks give EGF $\exp(x+x^2/2)$ and raw count 76, as derived by label allocation and pair-order divisions. All three use the same possible component sizes, yet answer different object-identity questions. The correct workflow identifies labels, order, component multiplicity, and the target size before applying an algebraic dictionary. Each final count can be checked independently by a small enumeration or recurrence.
