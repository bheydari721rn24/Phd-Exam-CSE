### 1. Formal division with a nonunit constant

Decide whether $2-x$ has an inverse over rational coefficients and over integer coefficients. Compute its first four rational inverse coefficients.

#### Solution

The constant equation in $(2-x)B=1$ requires $2b_0=1$, so $b_0=1/2$. At every later degree, $2b_n-b_{n-1}=0$, giving $b_n=1/2^{n+1}$. Thus the prefix is $1/2+x/4+x^2/8+x^3/16$. The rational inverse exists and is unique because the constant is invertible over the rationals. An integer-coefficient inverse cannot exist, since even an integer constant cannot multiply two to yield one. “Nonzero constant” is sufficient over a field, but the general ring criterion is “unit constant.” This distinction prevents an unjustified division in an integer or modular coefficient ring.

### 2. A reciprocal determined coefficient by coefficient

Find the coefficients through degree four of $1/(1-2x-x^2)$ without using its roots.

#### Solution

Let the unknown coefficients be $b_n$. Matching the constant gives $b_0=1$. The degree-one equation is $b_1-2b_0=0$, so $b_1=2$. Later coefficients obey $b_n=2b_{n-1}+b_{n-2}$. Consequently $b_2=5$, $b_3=12$, and $b_4=29$. The prefix is $1+2x+5x^2+12x^3+29x^4$. Multiply this prefix by the denominator: the constant remains one and every coefficient from degrees one through four cancels. Terms beyond degree four are unspecified, so the verification is modulo $x^5$, not an exact finite polynomial identity. The example demonstrates why a reciprocal can be computed without numerical root approximation.

### 3. A divergent series can still satisfy an identity

Let $A(x)=\sum_{n\ge0}n!x^n$. Prove a formal differential equation for $A$ and explain why it does not imply convergence at a positive numerical argument.

#### Solution

The factorial recurrence is $a_n=na_{n-1}$ for $n\ge1$, with $a_0=1$. Summing gives $A-1=x\sum_{m\ge0}(m+1)a_mx^m=x(A+xA')$. Thus $x^2A'+(x-1)A+1=0$. Every coefficient in this equation is a finite combination of factorials, so it is valid formally. For any nonzero numerical $x$, the ratio of consecutive absolute terms is $(n+1)|x|$, which eventually exceeds one and grows without bound. The terms do not tend to zero; the series diverges. A formal equation relates coefficients, while convergence concerns limits of numerical partial sums. Confusing these meanings would incorrectly permit evaluating the OGF at one.

### 4. Ordinary convolution versus a Hadamard product

For $A=1+2x+3x^2+4x^3$ and $B=1+3x+9x^2+27x^3$, find the degree-three coefficient of their ordinary product and their coefficientwise product.

#### Solution

Ordinary multiplication collects pairs of exponents summing to three: $1\cdot27+2\cdot9+3\cdot3+4\cdot1=58$. The coefficientwise, or Hadamard, product instead multiplies the two degree-three coefficients, giving $4\cdot27=108$. These operations describe different combinations of sequences. A product of independent choices with additive total size uses 58. A sequence deliberately defined by multiplying corresponding entries uses 108. The middle two cross terms are essential in ordinary multiplication; extracting coefficients separately before multiplying erases them. A direct expansion of the two finite polynomials provides an independent check of the ordinary answer.

### 5. The amount of a prefix needed after shifting

You know an OGF through degree six. Can you determine degree six of its square, its inverse when the constant is nonzero, and $(A-a_0-a_1x)/x^2$?

#### Solution

The square coefficient uses only pairs from degrees zero through six, so the known prefix suffices. The inverse recurrence also uses only denominator coefficients up to the target degree, so it suffices if the constant is nonzero over the chosen field. The left-shifted series has degree-six coefficient $a_8$, which is unknown. Two sequences can share every known coefficient and differ at degree eight, producing different shifted answers. Thus the first two questions are decidable and the last is not. A formal truncation should always carry a precision statement: left shifting by two reduces the known degree by two, whereas multiplying nonnegative-degree prefixes preserves the target precision.

### 6. A shifted rational coefficient with an impossible target

Find $[x^{12}]x^5/(1-3x)^3$, and explain the answer for target degree four.

#### Solution

The shift reduces the target to degree seven of $(1-3x)^{-3}$. The negative-binomial coefficient is $3^7\binom{9}{2}=2187\cdot36=78732$. For target four, the shifted target is minus one, so the coefficient is zero in an ordinary power series. The numerator shift must affect both the exponential and the binomial index: using $3^{12}\binom{14}{2}$ would count the unshifted expression. The product starts at degree five, which independently confirms the zero answer below five. This method works for any numerator monomial; a polynomial numerator is handled by summing its separate shifted contributions.

### 7. Removing an initial prefix before dividing

The OGF $A=1/(1-2x)$ has coefficients $2^n$. Find the OGF for $b_n=a_{n+3}$ and derive it through the left-shift formula.

#### Solution

Subtract the initial polynomial $1+2x+4x^2$ and divide the remainder by $x^3$. Multiplying that polynomial by $1-2x$ gives $1-8x^3$. Therefore $A-(1+2x+4x^2)=8x^3/(1-2x)$, and the shifted OGF is $8/(1-2x)$. Its degree-$n$ coefficient is $8\cdot2^n=2^{n+3}$, as required. Dividing the uncorrected $A$ by $x^3$ would introduce three negative powers and would not be the desired OGF. This boundary polynomial is the same type of correction that appears when a recurrence sum begins after several initial indices.

### 8. Even-degree filtering does not compress indices

Extract the even-degree part of $1/(1-3x)$ and then find the OGF of the compressed subsequence $b_n=3^{2n}$.

#### Solution

Average $1/(1-3x)$ and $1/(1+3x)$ to obtain $1/(1-9x^2)$. This series retains exponent $2n$ for the original term of index $2n$. The compressed subsequence instead has OGF $1/(1-9x)$, whose exponent is $n$. Both have coefficients drawn from powers of nine but at different positions. In the first series the coefficient of degree one is zero; in the second it is nine. This smallest nontrivial check already separates the two constructions. An exam question asking for “even coefficients” must be read carefully to determine whether it wants filtering or a new indexed subsequence.

### 9. A residue filter with a nontrivial offset

For $a_n=2^n$, find the series retaining only indices congruent to two modulo three, and give the compressed subsequence OGF.

#### Solution

The retained terms are $4x^2+32x^5+256x^8+\cdots$, so the filtered OGF is $4x^2/(1-8x^3)$. Equivalently, apply the root-of-unity filter with residue two. Its finite multiplier is one exactly at those indices and zero elsewhere. Compression defines $b_j=a_{3j+2}=4\cdot8^j$, so its OGF is $4/(1-8x)$. The factor four is the contribution of the offset two; omitting it would change even the first retained coefficient. The original size gap is three, whereas the compressed index gap is one.

### 10. Differentiation twice is not an index-square weight

If $A(x)=1/(1-x)$, find the OGF for $n^2$ in two ways and identify what $x^2A''$ represents.

#### Solution

First use the Euler operator twice: $xD(xA')=xA'+x^2A''$. Since $A'=1/(1-x)^2$ and $A''=2/(1-x)^3$, the sum simplifies to $x(1+x)/(1-x)^3$. Alternatively, the identity $n^2=n(n-1)+n$ combines the two falling-factorial weight series. The expression $x^2A''$ alone has coefficient $n(n-1)$, not $n^2$. At index one it gives zero while the target square is one, providing an immediate counterexample. The extra derivative of the intermediate factor $x$ is the reason the two operator expressions differ.

### 11. A cubic polynomial weight

Find the OGF of $n^3$ and explain how its numerator can be derived without memorizing a table.

#### Solution

Apply $xD$ to the square-weight series $x(1+x)/(1-x)^3$. The quotient derivative simplifies to $(1+4x+x^2)/(1-x)^4$ before multiplication by $x$. Therefore the cubic-weight OGF is $x(1+4x+x^2)/(1-x)^4$. A separate check uses $n^3=n(n-1)(n-2)+3n(n-1)+n$: the corresponding series are $6x^3/(1-x)^4$, $6x^2/(1-x)^3$, and $x/(1-x)^2$. Bringing them to a common denominator gives the same numerator. The first coefficients 0,1,8,27 verify both the boundary and the degree of the polynomial weight.

### 12. A harmonic convolution identity

Prove $\sum_{k=1}^{n}(n+1-k)/k=(n+1)H_n-n$ using generating functions.

#### Solution

The logarithmic series has coefficients $1/k$ for positive $k$ and zero at zero. Multiplying it by $(1-x)^{-2}$ gives degree-$n$ coefficient $\sum_{k=1}^{n}(n+1-k)/k$. Algebraically the sum also splits into $(n+1)\sum_{k=1}^{n}1/k-\sum_{k=1}^{n}1$, giving $(n+1)H_n-n$. This direct rearrangement is an independent check, not a replacement for the OGF interpretation. At zero both sides are zero by the empty-sum convention. The factor $(1-x)^{-2}$ supplies weight $n+1-k$, while a single inverse factor would produce only $H_n$.

### 13. Repeated prefix summation

Let $a_n=2^n$, and let $b_n$ be the prefix sum of the prefix sum of this sequence. Find $b_n$ exactly.

#### Solution

Two prefix operations give $B=1/((1-2x)(1-x)^2)$. Decompose it as $4/(1-2x)-2/(1-x)-1/(1-x)^2$. The coefficient is therefore $4\cdot2^n-2-(n+1)=2^{n+2}-n-3$. At zero it is one, as both prefix operations preserve the original constant one. At one, the first prefix is 1,3 and the second is 1,4; the formula gives four. The repeated pole at one contributes the linear subtraction, whereas the simple pole at one-half supplies the exponential term. Forgetting the second prefix factor would produce a different numerator and wrong initial values.

### 14. A binomial transform of a geometric sequence

Find the binomial transform of $a_n=3^n$, first by its OGF and then by a finite identity.

#### Solution

The source OGF is $A=1/(1-3x)$. Substitute $x/(1-x)$ and multiply by $1/(1-x)$ to obtain $B=1/(1-4x)$. Thus $b_n=4^n$. Directly, $b_n=\sum_{k=0}^{n}\binom{n}{k}3^k=(1+3)^n$, confirming the coefficient extraction. The prefactor in the transform formula is necessary; substitution alone would give $(1-x)/(1-4x)$ and would incorrectly change the coefficients after zero. This example also shows why the binomial transform is naturally a label-choice operation, even when expressed with an ordinary rather than exponential series.

### 15. Inverting a binomial transform

Suppose $b_n=5^n$ is the binomial transform of an unknown sequence. Recover that sequence and check the inversion for index two.

#### Solution

The inverse transform is $a_n=\sum_{k=0}^{n}(-1)^{n-k}\binom{n}{k}5^k=(5-1)^n=4^n$. At index two it gives $1-10+25=16$. Transforming the recovered sequence forward yields $1+8+16=25$, as required. The alternating sign depends on $n-k$, not merely $k$ unless the outside factor $(-1)^n$ is also included. The inverse identity follows by pairing two nested binomial coefficients and summing a signed binomial expansion, which vanishes for every index mismatch. Hence the reconstruction is unique, rather than just a sequence that happens to match the first few values.

### 16. A square-root coefficient with its sign

Compute $[x^4]\sqrt{1-4x}$ using generalized binomial coefficients and relate it to a Catalan number.

#### Solution

The coefficient is $\binom{1/2}{4}(-4)^4$. The descending product is $(1/2)(-1/2)(-3/2)(-5/2)/24=-5/128$, so the answer is minus ten. The Catalan identity $\sqrt{1-4x}=1-2xC(x)$ independently gives coefficient $-2C_3=-2\cdot5=-10$. The negative sign is not optional: generalized binomial coefficients are not ordinary nonnegative counting coefficients. The normalized square root has constant one, and its later negative coefficients combine with the leading one in the Catalan numerator to produce positive counts after division by the variable.

### 17. Distinct poles and a numerator shift

Find $[x^n]x^2/((1-x)(1-3x))$ for every nonnegative $n$.

#### Solution

For $m\ge0$, the unshifted inverse has coefficient $\sum_{i=0}^{m}3^i=(3^{m+1}-1)/2$, either by convolution or by partial fractions. Set $m=n-2$ when $n\ge2$, giving $(3^{n-1}-1)/2$. For $n=0,1$, the coefficient is zero because the numerator begins at degree two. The piecewise domain is essential: blindly inserting zero into the positive-index formula would introduce a fraction that is not a valid counting answer. At degree two the expression yields one, matching the constant of the unshifted inverse. A numerator monomial carries an actual delay in the sequence.

### 18. A repeated pole whose polynomial weight changes

Find the coefficient of $x^n$ in $(1+x)/(1-x)^3$ and simplify it.

#### Solution

The first numerator term contributes $\binom{n+2}{2}$ and the shifted term contributes $\binom{n+1}{2}$, with the latter zero at index zero. Their sum is $(n+1)^2$. Expanding the two products shows $(n+2)(n+1)/2+n(n+1)/2=(n+1)^2$. This OGF represents the squares 1,4,9,..., whereas $x(1+x)/(1-x)^3$ represents 0,1,4,... . The denominator multiplicity predicts quadratic index dependence, but the numerator and shift determine the exact polynomial and initial value. Testing the constant is a quick way to distinguish the two square sequences.

### 19. Cancellation invalidates an apparent resonance

Find the exact coefficients of $(1-2x)^2/((1-2x)^3(1+x))$, and explain why the apparent triple pole is misleading.

#### Solution

Cancel the two common factors first. The reduced OGF is $1/((1-2x)(1+x))$. Partial fractions give $(2/3)/(1-2x)+(1/3)/(1+x)$, so $a_n=(2^{n+1}+(-1)^n)/3$. The degree-zero coefficient is one and degree one is one, confirming the decomposition. Before cancellation the denominator has a third power, but two of those factors are removable. Therefore neither an index-square nor an index-linear factor is justified for the surviving base-two term. Pole multiplicity always means multiplicity in the reduced rational function.

### 20. Polynomial division creates an exact finite prefix

Find every coefficient of $(1+x^2)/(1-x)$, separating its polynomial and proper rational parts.

#### Solution

Polynomial division gives $-x-1+2/(1-x)$, because $(-x-1)(1-x)+2=1+x^2$. Thus $a_0=1$, $a_1=1$, and $a_n=2$ for every $n\ge2$. Direct convolution with the all-ones series gives the same answer: the constant numerator contributes one everywhere and its degree-two term contributes another one starting at index two. Keeping only the proper rational part would incorrectly produce two at the first two indices. A finite polynomial correction is negligible for eventual growth but indispensable in an exact formula, especially when an exam asks about a small index or an initial-value condition.

### 21. A simple pole coefficient determined at its root

Decompose $(2+x)/((1-2x)(1-3x))$ and obtain its exact sequence.

#### Solution

Write $A/(1-2x)+B/(1-3x)$ and clear the denominator. Then $2+x=A(1-3x)+B(1-2x)$. At $x=1/2$, the second term vanishes, giving $A=-5$. At $x=1/3$, the first term vanishes, giving $B=7$. Hence $a_n=-5\cdot2^n+7\cdot3^n$. The first coefficient is two, matching the numerator constant divided by the denominator constant. The next coefficient is eleven, also obtained by multiplying $(2+x)$ by the inverse denominator prefix $1+5x+\cdots$. Evaluation at a pole is performed only after clearing or removing its zero factor, never directly in the original singular quotient.

### 22. Complex poles produce exact periodic coefficients

Find the coefficients of $1/(1+x^2)$ and explain their relation to complex roots.

#### Solution

The geometric expansion in $-x^2$ gives $a_{2j}=(-1)^j$ and $a_{2j+1}=0$. The factors are $(1-ix)(1+ix)$, and the partial fractions average their geometric inverses, yielding $(i^n+(-i)^n)/2$. This expression is real and equals the same periodic sequence 1,0,-1,0,... . Its modulus does not stay bounded below by a positive constant on all indices, since every odd term vanishes. Equal-modulus poles can interfere; they do not support an automatic positive Theta claim at each index. Exact extraction is safer than inferring growth from a single factor in isolation.

### 23. A nonhomogeneous boundary polynomial

Let $a_0=2$, $a_1=3$, and $a_n=4a_{n-1}-4a_{n-2}+1$ for $n\ge2$. Derive its OGF, including the forcing domain.

#### Solution

Summing from two gives $A-2-3x=4x(A-2)-4x^2A+x^2/(1-x)$. Therefore $(1-2x)^2 A=2-5x+x^2/(1-x)$ and $A=(2-7x+6x^2)/((1-x)(1-2x)^2)$. Factor the numerator as $(1-2x)(2-3x)$, then cancel to get $(2-3x)/((1-x)(1-2x))=1/(1-x)+1/(1-2x)$. Thus $a_n=1+2^n$. The apparent double root cancels once because the specific initial data and forcing select a simpler solution. At index two, the recurrence gives $12-8+1=5$, matching the derived formula. Using an unshifted forcing inverse would already corrupt the constant equation.

### 24. Resonant exponential forcing

For $a_0=3$ and $a_n=2a_{n-1}+2^n$ from index one, find an exact coefficient formula and explain the polynomial factor.

#### Solution

The equation is $A-3=2xA+2x/(1-2x)$. Hence $A=3/(1-2x)+2x/(1-2x)^2$. The second term contributes $n2^n$ for positive indices and zero at zero, so $a_n=(n+3)2^n$ for all nonnegative indices. Division by $2^n$ provides an independent proof: the normalized recurrence increments by one, starting at three. The forced base two matches the homogeneous base, increasing the pole order and requiring the linear index factor. The numerator shift is what changes the ordinary coefficient $(n+1)2^n$ into $n2^n$.
