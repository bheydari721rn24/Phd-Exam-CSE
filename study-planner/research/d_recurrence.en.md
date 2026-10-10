# Recurrence Relations: Exact Solutions, Counting Models, and Boundary Conditions

## 1. Sources, purpose, and prerequisite map

The four core written courses are MIT 6.042J, Oxford Discrete Mathematics, Cornell CS2800, and Berkeley Math 55. The separate source audit records the candidate pool, actual reading scopes, selection reasons, and source discrepancies. These are complementary selections from a documented accessible pool, rather than a claim to have reviewed every course worldwide. The exposition and proofs below are newly written. Reconstructed exercise patterns are labeled separately from original examination items.

This chapter develops exact sequence recurrences. Its prerequisites are induction, basic polynomial algebra, finite sums, counting bijections, and the elementary matrix operations already taught in the linear algebra track. It connects to the algorithmic recurrence chapter without repeating its divide-and-conquer toolbox. Full generating-function methods belong to the next discrete mathematics chapter; here we derive their boundary-aware interface. A recurrence is useful only after its index range, starting values, and objects being counted are specified.

Read the lesson before the questions. The question bank then trains four different actions: derive a recurrence from a model, solve it exactly, reject a tempting invalid solution, and extract only the quantity a problem requests. The final reasoning rules are complete statements with assumptions and exceptions. Neither a large question bank nor a checked chapter guarantees performance on every unseen examination problem.

## 2. A recurrence is a definition with a domain

A sequence is a function from an index set, usually the nonnegative integers, into a specified value set. Writing $a_n$ hides the function argument; it does not change the definition. For example, $a_0=3$ and $a_n=2a_{n-1}+1$ for $n\ge1$ define $3,7,15,31,\ldots$. The same equation with $a_0=0$ defines a different sequence. An equation without enough starting information describes a family of sequences.

A recurrence is well founded when every value used to compute a new term has already been defined. In $a_n=a_{\lfloor n/2\rfloor}+1$, the inequality $\lfloor n/2\rfloor<n$ holds for positive $n$, but not for zero; hence a separate value $a_0$ is essential. In $a_n=a_{n+1}+1$, forward evaluation is unavailable unless further boundary information or another argument is provided. A recurrence need not have constant coefficients, fixed lag, or a closed form.

For a normalized order-$k$ recurrence,

$$a_n=\sum_{j=1}^{k}c_j a_{n-j}+b_n,\qquad n\ge k,$$

the values $a_0,\ldots,a_{k-1}$ determine every later term by induction. No division is needed in this forward construction. If some last coefficients vanish, the effective lag may be smaller, but a late starting index can still leave an exceptional initial prefix. Do not remove that prefix merely because a polynomial factor is zero.

## 3. Classify before selecting a method

Linearity means that unknown sequence values occur to the first power and are not multiplied by one another. Thus $a_n=3a_{n-1}+n a_{n-2}+n^2$ is linear with variable coefficients, whereas $a_n=a_{n-1}a_{n-2}+1$ is nonlinear. A fixed nonzero forcing term makes a linear equation nonhomogeneous. Its homogeneous companion is obtained by setting the forcing to zero, while leaving the coefficients and valid index range unchanged.

The equation $T(n)=2T(n/2)+n$ is linear as an equation in the unknown function $T$, but it is not a fixed-order consecutive-index recurrence. The usual characteristic polynomial in $a_n,a_{n-1},\ldots$ cannot be applied to it without a justified change of variable. Conversely, a convolution such as the Catalan recurrence is genuinely nonlinear. Method selection should follow the actual equation, not the appearance of the word recursion.

| Equation structure | First useful method | Main condition |
| --- | --- | --- |
| One previous value with known coefficients | Unrolling or a product formula | State exactly where the equation begins. |
| Fixed lag and constant coefficients | Characteristic roots and forcing | Normalize the coefficient of the newest term. |
| Variable coefficients with combinatorial meaning | A bijection, normalization, or dynamic programming | Prove the transformed equation. |
| Finite coupled states | A transfer matrix | Define what every state counts. |
| Prefix sums | Subtract adjacent equations | Preserve the earliest exceptional terms. |
| Products or nonlinear convolutions | Logarithms, structural counting, or generating functions | Check positivity or formal algebra assumptions. |

## 4. Unrolling gives an exact first-order formula

Consider $a_n=p a_{n-1}+q_n$ for $n\ge1$. After two substitutions,

$$a_n=p^2a_{n-2}+p q_{n-1}+q_n.$$

After $r$ substitutions, induction gives $a_n=p^r a_{n-r}+\sum_{j=0}^{r-1}p^j q_{n-j}$. Set $r=n$ only when the recurrence really reaches the specified value at index zero:

$$a_n=p^n a_0+\sum_{j=1}^{n}p^{n-j}q_j.$$

The summand is the contribution injected at time $j$, multiplied once for every subsequent update. This interpretation explains the exponent $n-j$ and prevents the common shift to $n-j+1$. An empty sum is zero. The formula also works at $p=0$ if the empty product is one: the last forcing survives and all earlier contributions disappear. Dividing by $p^n$ would incorrectly exclude this case.

For constant $q$ and $p\ne1$, the geometric sum yields $a_n=p^n a_0+q(p^n-1)/(p-1)$. For $p=1$, it yields $a_n=a_0+nq$. These are separate formulas with a removable limiting singularity, not permission to divide by zero. With $p=2,q_n=n,a_0=0$, direct summation or substitution gives $a_n=2^{n+1}-n-2$; checking $n=0,1,2$ verifies the boundary and the first transitions.

<!-- SIM: unrolling -->

## 5. Variable coefficients and reset events

For $a_n=p_n a_{n-1}+q_n$, repeated substitution gives

$$a_n=a_0\prod_{i=1}^{n}p_i+\sum_{j=1}^{n}q_j\prod_{i=j+1}^{n}p_i.$$

Prove it by inserting the formula for $a_{n-1}$: multiplying each old contribution by $p_n$ extends its product, and the new term $q_n$ receives an empty product. This proof never divides by a coefficient, so zero coefficients are valid. If $p_r=0$, all information from times before $r$ is erased at that update; later values depend on the reset value $q_r$ and subsequent forcing.

When every $p_i$ is nonzero, define $P_n=\prod_{i=1}^n p_i$ and $u_n=a_n/P_n$. Then $u_n-u_{n-1}=q_n/P_n$ telescopes. This integrating-factor method is efficient, but its nonzero condition must be checked before use. For $a_n=n a_{n-1}+n!$ with $a_0=0$, division by $n!$ gives $u_n=u_{n-1}+1$, hence $a_n=n\,n!$. A multiplicative recurrence $a_n=2^n a_{n-1},a_0=1$ instead gives $a_n=2^{n(n+1)/2}$ by adding exponents; it has variable coefficients and cannot be solved by a constant characteristic root.

## 6. Existence, uniqueness, and the solution space

For a homogeneous order-$k$ equation with constant coefficients, addition and scalar multiplication preserve solutions. The map taking a solution to its initial tuple $(a_0,\ldots,a_{k-1})$ is linear. It is injective because identical initial tuples generate identical later terms, and surjective because every tuple can be propagated forward. Therefore the solution space has dimension $k$ over the chosen scalar field.

This dimension argument is more than a formality. If you propose only two modes for an order-three equation, you cannot represent every possible initial triple. If you propose three expressions but two are proportional, you still do not have a basis. The homogeneous solution space is a vector space; the solution set for one fixed nonzero forcing is an affine translate of it. The sum of two particular solutions normally doubles the forcing, rather than solving the same equation.

A zero initial tuple gives the zero homogeneous solution, regardless of how large the coefficients are. A dominant characteristic root can be present in the polynomial yet absent from the actual sequence because its coefficient is zero. Determine the constants before making a growth claim.

## 7. Derive the characteristic polynomial

Assume $c_k\ne0$ for the moment, and try the mode $a_n=r^n$. Substitution gives $r^n=\sum_{j=1}^k c_j r^{n-j}$. Since the nonzero constant term of the characteristic polynomial excludes $r=0$, divide by $r^{n-k}$:

$$P(r)=r^k-c_1r^{k-1}-c_2r^{k-2}-\cdots-c_k=0.$$

The signs come from moving the entire right side to the left. For $a_n=4a_{n-1}-3a_{n-2}$, the polynomial is $r^2-4r+3$, not $r^2-4r-3$. Its roots are one and three. Thus $a_n=A+B3^n$. Initial values $a_0=1,a_1=1$ imply $B=0,A=1$; initial values $a_0=1,a_1=3$ imply $A=0,B=1$.

For distinct roots $r_1,\ldots,r_k$, superposition gives $a_n=\sum_j A_j r_j^n$. The initial equations form a Vandermonde system. Its determinant is $\prod_{i<j}(r_j-r_i)$, which is nonzero precisely when the roots are distinct. The modes therefore represent every initial tuple exactly once. Repeated roots require a different basis, not repeated copies of the same equation.

## 8. Two distinct roots: solve the constants transparently

For $a_n=c_1a_{n-1}+c_2a_{n-2}$ with distinct roots $r,s$, write $a_n=A r^n+B s^n$. The equations $A+B=a_0$ and $rA+sB=a_1$ give

$$A=\frac{a_1-sa_0}{r-s},\qquad B=\frac{ra_0-a_1}{r-s}.$$

These constants should be computed with the same indexing as the recurrence. If the data are $a_1,a_2$, solve at one and two, or first define a shifted sequence; do not insert them as though they were $a_0,a_1$. For $a_n=5a_{n-1}-6a_{n-2}$ with $a_0=2,a_1=5$, roots two and three give $A=B=1$, so $a_n=2^n+3^n$. The term at index two is thirteen both from the formula and from $5\cdot5-6\cdot2$.

An exact formula is established by two checks: it satisfies the recurrence throughout the valid domain, and it satisfies every required starting value. Matching the first few computed terms is useful error detection, but is not a proof without the recurrence identity and uniqueness argument.

## 9. Repeated roots come from finite differences

Let $E$ shift a sequence forward: $(Ea)_n=a_{n+1}$. For a nonzero $r$ and a polynomial $q$,

$$((E-r)a)_n=r^{n+1}\bigl(q(n+1)-q(n)\bigr),\qquad a_n=r^nq(n).$$

Define $\Delta q(n)=q(n+1)-q(n)$. If $q$ has degree $d>0$ and leading coefficient $u$, then $\Delta q$ has degree $d-1$ and leading coefficient $du$; a constant has zero difference. Applying $(E-r)$ $m$ times annihilates $r^nq(n)$ whenever the degree of $q$ is less than $m$. Thus a root of multiplicity $m$ contributes

$$r^n,\quad nr^n,\quad n^2r^n,\quad\ldots,\quad n^{m-1}r^n.$$

For $a_n=4a_{n-1}-4a_{n-2}$, the polynomial is $(r-2)^2$. With $a_0=1,a_1=6$, the solution $(A+Bn)2^n$ has $A=1,B=2$. Writing $A2^n+B2^n$ would provide only one independent mode and could not satisfy the two data. A triple root contributes a quadratic polynomial times the exponential, not three unrelated exponentials with the same base.

<!-- SIM: differences -->

## 10. Why the complete root recipe really is complete

Factor $P(z)=\prod_j(z-r_j)^{m_j}$ over the complex numbers, with distinct nonzero roots and $\sum_jm_j=k$. Every proposed mode is annihilated by its own repeated factor, and the shift factors commute, so every mode satisfies $P(E)a=0$.

To prove independence, suppose $\sum_j r_j^n q_j(n)=0$ with each $q_j$ of degree below $m_j$. Fix one root $r_j$ and apply all factors associated with other roots. They annihilate all other terms. On the remaining term, a factor $E-s$ with $s\ne r_j$ acts as

$$((E-s)a)_n=r_j^n\bigl((r_j-s)q(n)+r_j\Delta q(n)\bigr).$$

If $q$ is nonzero, this operation preserves its degree and multiplies its leading coefficient by the nonzero number $r_j-s$. Repeating the operation cannot turn it into the zero polynomial. Yet the isolated expression must vanish for every nonnegative integer $n$, and $r_j^n\ne0$. A nonzero polynomial cannot have infinitely many roots, so $q_j=0$. The same reasoning applies to every root. We have $k$ independent modes in a space of dimension $k$, hence a basis.

This proof supplies the missing logical step between a useful recipe and an exhaustive solution. The scalar field matters: real coefficients may have complex roots; paired complex modes can be rewritten as real sequences. Zero roots require the separate treatment below because division and exponential-polynomial independence used nonzero bases.

## 11. Zero roots and exceptional initial prefixes

If $c_k=0$, the naive root recipe needs care. Consider $a_n=2a_{n-1}$ only for $n\ge2$, with $a_0=5,a_1=3$. The tail is $a_n=3\cdot2^{n-1}$ for $n\ge1$, but index zero remains five. The equation was not imposed at one. Reducing the order and silently extending it to one would demand $a_1=10$, contradicting the actual data.

An especially clear case is $a_n=0$ for $n\ge2$, with arbitrary $a_0,a_1$. Its formal order-two polynomial is $z^2$. The expressions $0^n$ and $n0^n$ do not form a complete two-dimensional basis, even if $0^0=1$ is adopted: the second expression is identically zero. The correct basis is two impulses, $\delta_{n,0}$ and $\delta_{n,1}$, each equal to one at its named index and zero elsewhere.

More generally, write $P(z)=z^sQ(z)$ with $Q(0)\ne0$. The equation $P(E)a=0$ says that $Q(E)$ annihilates the tail starting at index $s$. Solve that tail with its own boundary tuple, and retain the first $s$ terms as independent finite-prefix data. This gives $s$ impulse modes plus the nonzero-root tail modes, with total dimension $k$. It is often clearer in an examination to state the prefix and tail separately than to introduce special conventions for zero powers.

<!-- SIM: boundary -->

## 12. Negative and complex roots explain oscillation

A negative real root contributes an alternating sign. Two conjugate roots $\rho e^{i\theta}$ and $\rho e^{-i\theta}$ combine into the real form

$$a_n=\rho^n\bigl(A\cos(n\theta)+B\sin(n\theta)\bigr).$$

Euler's identity and conjugate coefficients justify this conversion. For the recurrence $a_n=-a_{n-2}$, the roots are $i,-i$. With $a_0=1,a_1=0$, the sequence is $1,0,-1,0,\ldots$, or $\cos(n\pi/2)$. A repeated conjugate pair contributes polynomial factors multiplying both sine and cosine. Real initial data still produce real values because the recurrence itself has real coefficients.

Absolute root size alone does not prove a positive lower bound. The sequence $1+(-1)^n$ is zero at every odd index; it is bounded above by two but is not bounded below by a positive constant for all sufficiently large indices. Likewise, a coefficient can cancel a dominant root entirely. Growth estimates must refer to the actual nonzero modes and the requested domain, sometimes a subsequence or absolute value.

## 13. Fibonacci, tilings, and initial-value conventions

In this chapter $F_0=0,F_1=1$, and $F_n=F_{n-1}+F_{n-2}$ for $n\ge2$. The characteristic roots are $\phi=(1+\sqrt5)/2$ and $\psi=(1-\sqrt5)/2$. Solving the two initial equations gives

$$F_n=\frac{\phi^n-\psi^n}{\sqrt5}.$$

This expression is an integer because it is the unique solution of an integer recurrence with integer starting values. Since $|\psi|<1$, the difference between $F_n$ and $\phi^n/\sqrt5$ has absolute value less than one half for every nonnegative $n$. Therefore exact real arithmetic followed by nearest-integer rounding recovers $F_n$. Ordinary floating-point computation at large $n$ is a different matter: accumulated numerical error can exceed one half, so the formula is not a reliable arbitrary-size integer algorithm.

Let $T_n$ count domino tilings of a $2\times n$ board. An empty board has one tiling, so $T_0=1$; a one-column board has one vertical tiling, so $T_1=1$. The leftmost column is either one vertical domino or the left halves of two horizontal dominoes. Removing those placements leaves a board of width $n-1$ or $n-2$, and replacement reconstructs the original tiling uniquely. Thus $T_n=T_{n-1}+T_{n-2}$ and $T_n=F_{n+1}$. A staircase using steps of sizes one and two has the same shifted sequence, not $F_n$ with the convention above.

<!-- SIM: tiling -->

## 14. Nonhomogeneous equations are affine translates

Let $L$ denote the linear recurrence operator. If $L(h)=0$ and $L(p)=b$, then $L(h+p)=b$. Conversely, the difference between any two solutions with forcing $b$ is homogeneous. Once one particular solution is known, every solution is that particular sequence plus a homogeneous solution.

The safe procedure is: solve the homogeneous companion; choose and verify one particular solution; add them; then fit the initial values of the complete expression. A particular solution need not satisfy any initial conditions. Imposing the initial values on the particular term alone can incorrectly eliminate a valid trial, or leave no freedom to correct its boundary values.

For $a_n=3a_{n-1}+2^n$, substituting $p_n=K2^n$ gives $K=3K/2+1$, hence $K=-2$. The general solution is $A3^n-2^{n+1}$. If $a_0=1$, then $A=3$, so $a_n=3^{n+1}-2^{n+1}$. The negative particular coefficient is not a contradiction: the full sequence, rather than one arbitrarily chosen component, is the object being modeled.

## 15. Resonance changes the trial space

Suppose the forcing is $r^nR_d(n)$, where $r\ne0$ and $R_d$ is a polynomial of fixed degree $d$. If $r$ is not a characteristic root, try $r^nQ_d(n)$. If $r$ is a root of multiplicity $m$, try

$$p_n=n^m r^nQ_d(n).$$

The multiplier $n^m$ moves the trial out of the homogeneous null space. It is not determined by the degree of the forcing. For $a_n=2a_{n-1}+2^n$, a trial $K2^n$ has zero residual and cannot generate the forcing. A trial $Kn2^n$ has residual $K2^n$, so $K=1$. With $a_0=3$, the full answer is $(n+3)2^n$.

For $a_n-2a_{n-1}+a_{n-2}=1$, the root one has multiplicity two. A constant or a linear polynomial is annihilated. The trial $Kn^2$ has residual $2K$, so $K=1/2$. The complete solution is $A+Bn+n^2/2$. If $a_0=0,a_1=1$, then $A=0,B=1/2$, giving $n(n+1)/2$. Omitting the resonance multiplier makes the coefficient equations inconsistent; that inconsistency is diagnostic evidence, not a reason to discard the forcing.

<!-- SIM: resonance -->

## 16. Justify undetermined coefficients and mixed forcing

The repeated-root difference identity proves the trial rule. The factor $(E-r)^m$ reduces the polynomial degree by $m$ after stripping the exponential. Other factors $E-s$ with $s\ne r$ preserve the resulting degree with nonzero leading coefficient. On the space spanned by $r^n n^m,\ldots,r^n n^{m+d}$, the recurrence operator maps to exponential polynomials of degrees zero through $d$ with a triangular coefficient matrix and nonzero diagonal. Therefore every forcing polynomial of degree at most $d$ has exactly one particular solution in this chosen trial space. The identity $P(E)a_n=b_{n+k}$ includes an index shift in the forcing; substituting into the original recurrence avoids losing that shift.

For a sum of distinct forcing components, construct one particular term per component and add them. For example, solve $a_n=2a_{n-1}+3^n+5n,a_0=0$. The exponential component has particular term $3^{n+1}$. For the linear component, substitute $Bn+C$: the residual is $-Bn+2B-C$, so $B=-5,C=-10$. Add $D2^n$ and use $0=D+3-10$, obtaining

$$a_n=7\cdot2^n+3^{n+1}-5n-10.$$

For polynomial forcing, root one is the relevant resonance test because a polynomial is $1^n$ times a polynomial. For trigonometric forcing, complex exponential decomposition provides the corresponding root test. Step functions, factorials, and arbitrary forcing may require unrolling or a generating function rather than a finite undetermined-coefficient trial. State the method's domain instead of forcing every right side into the same template.

## 17. Build counting recurrences from reversible cases

A counting recurrence requires disjoint exhaustive cases and a reversible reduction for each case. Removing a feature without recording information needed to reconstruct it may undercount. Splitting into overlapping cases may overcount. The empty object often contributes one because it is a single valid completion, not because a positive-size object exists.

For binary strings avoiding adjacent ones, classify by the final bit. Strings ending in zero arise by appending zero to any valid length-$n-1$ string. Strings ending in one must end in zero-one when $n\ge2$, and removing that pair gives a valid length-$n-2$ string. Thus $B_n=B_{n-1}+B_{n-2}$, with $B_0=1,B_1=2$. Consequently $B_n=F_{n+2}$. The same recurrence with tiling starting values counts a different set.

For ordered payments using two distinguishable one-unit tokens and one five-unit token, let $W_n$ count sequences totaling $n$. The last token is one of the two unit types or the five-unit type, so $W_n=2W_{n-1}+W_{n-5}$ for positive $n$, with $W_0=1$ and $W_n=0$ for negative $n$. If token order is irrelevant, this recurrence is wrong because removing the last token is not a uniquely defined operation on a multiset. Semantic words such as ordered, labeled, distinguishable, and unlimited are part of the mathematics.

## 18. State recurrences handle forbidden patterns

Sometimes total counts do not record enough history. For ternary strings with no consecutive zeroes and no consecutive ones, but unrestricted repetitions of two, distinguish a count $u_n$ of strings ending in one specified restricted symbol, and $v_n$ of strings ending in two. Symmetry makes the counts ending in zero and one equal. For $n\ge2$,

$$u_n=u_{n-1}+v_{n-1},\qquad v_n=2u_{n-1}+v_{n-1}.$$

At length one, $u_1=v_1=1$, and the total is $T_n=2u_n+v_n$. The transition matrix is

$$M=\begin{bmatrix}1&1\\2&1\end{bmatrix}.$$

Its polynomial is $z^2-2z-1$, so each component and the total satisfy $T_n=2T_{n-1}+T_{n-2}$ after valid initialization. Extending the total to the empty string gives $T_0=1,T_1=3$, then $1,3,7,17,41,99,239$. The matrix state at length zero cannot simply be $(1,1)$: there is no last symbol in an empty string. Introduce an empty-start state or begin the two-state calculation at length one.

For more complicated forbidden words, a state records the longest relevant suffix that is also a prefix of a forbidden word. A transition completing a forbidden word is omitted. Counts propagate along labeled allowed edges. This finite-state method generalizes the recurrence without pretending that every restriction is determined by only the last bit.

<!-- SIM: automaton -->

## 19. Derangements: prove the two cases by cycles

A derangement is a permutation with no fixed point. Write $D_0=1$ for the empty permutation and $D_1=0$. For $n\ge2$, choose the image $j$ of element one; there are $n-1$ possible choices. If $j$ maps back to one, the two form a two-cycle, and the remaining elements can be deranged in $D_{n-2}$ ways.

Otherwise, let $h$ be the element whose image is one. Delete one from its cycle by redirecting $h$ to $j$. The remaining permutation has no fixed point: $h\ne j$ in this case, so the new edge cannot fix $h$. Conversely, from a derangement on the remaining elements, find the predecessor of $j$ and insert one immediately before $j$. This is a bijection, giving $D_{n-1}$ possibilities for each chosen $j$. Therefore

$$D_n=(n-1)(D_{n-1}+D_{n-2}).$$

The factor $n-1$ belongs to both cases because $j$ was chosen before the split. The coefficient varies with $n$, so the constant-root method is inapplicable. For direct computation, $D_2=1,D_3=2,D_4=9,D_5=44$. An alternative recurrence follows from inclusion-exclusion or an induction identity: $D_n=nD_{n-1}+(-1)^n$. Proving their equivalence requires the specified bases; a recurrence that also generates factorials with different bases does not make the sequences equal.

<!-- SIM: derangements -->

## 20. Set partitions: Stirling and Bell recurrences

Let $S(n,k)$ count partitions of $n$ distinct elements into $k$ nonempty unlabeled blocks. The new element either forms a singleton, leaving $S(n-1,k-1)$ possibilities, or joins one of the $k$ existing blocks of a partition counted by $S(n-1,k)$. Thus

$$S(n,k)=S(n-1,k-1)+kS(n-1,k).$$

The blocks are unlabeled, but a particular partition still contains $k$ distinguishable subsets to which the new element can be added. That is why the multiplier is $k$, not $k!$. Boundary values are $S(0,0)=1$, $S(n,0)=0$ for positive $n$, and $S(n,k)=0$ for $k<0$ or $k>n$. These conventions make the recurrence safe along its edges.

The Bell number $B_n=\sum_{k=0}^n S(n,k)$ counts all set partitions. To obtain $B_{n+1}$, choose the $j$ old elements that lie outside the block containing the new element, and partition those $j$ freely. The new block is then forced. This reversible construction gives

$$B_{n+1}=\sum_{j=0}^{n}\binom{n}{j}B_j,\qquad B_0=1.$$

The first Bell numbers are $1,1,2,5,15,52$. Counting one block containing the new element makes the cases disjoint. Counting each arbitrary block as special would count a partition several times. Infinite-series expressions for Bell numbers require convergence arguments; the finite recurrence already gives an exact computational and combinatorial foundation.

<!-- SIM: partitions -->

## 21. Integer partitions require a second parameter

Let $p(n,k)$ count partitions of the integer $n$ into exactly $k$ positive parts, without regard to order. Split into partitions having a part equal to one and those having every part at least two. Removing one part equal to one gives $p(n-1,k-1)$. Subtracting one from every part in the second case gives $p(n-k,k)$. Both maps are reversible, so

$$p(n,k)=p(n-1,k-1)+p(n-k,k).$$

Take $p(0,0)=1$ and zero for negative arguments, for $k>n$, or for $k=0<n$. A Ferrers diagram displays the second operation as removing a full column of $k$ cells, not one cell from an arbitrary row. For $p(7,3)$, the partitions are $5+1+1$, $4+2+1$, $3+3+1$, and $3+2+2$, so the answer is four.

A different state $P(n,m)$ counts partitions with every part at most $m$. Classifying by whether a part $m$ appears gives $P(n,m)=P(n,m-1)+P(n-m,m)$. Its boundary is $P(0,m)=1$ for nonnegative $m$ and $P(n,0)=0$ for positive $n$. The two recurrences look similar, but their second parameters mean different things. Swapping the formulas without translating the state definition changes the problem.

<!-- SIM: conjugate -->

## 22. Catalan recurrence: a nonlinear decomposition

Let $C_n$ count balanced parenthesis strings with $n$ pairs, equivalently Dyck paths of semilength $n$. The empty string gives $C_0=1$. A nonempty balanced string has a uniquely matched closing parenthesis for its first opening parenthesis. If the enclosed string has $j$ pairs, the suffix has $n-1-j$ pairs. Each can be chosen independently, giving

$$C_n=\sum_{j=0}^{n-1}C_jC_{n-1-j}.$$

The first-return position makes these cases disjoint and reconstructible. The product appears because two independent objects are combined, making this recurrence nonlinear in the sequence. Characteristic roots for fixed-order linear equations cannot solve it. The standard formula $C_n=\binom{2n}{n}/(n+1)$ can be proved by reflecting a bad path: among all $\binom{2n}{n}$ paths with $n$ up and $n$ down steps, paths that first cross below zero correspond bijectively to paths with $n+1$ down steps and $n-1$ up steps, counted by $\binom{2n}{n+1}$. Their difference is the stated formula. The algebraic generating-function derivation is developed in the next chapter.

<!-- SIM: catalan -->

<!-- SIM: reflection -->

## 23. Prefix sums and differencing: preserve the first exception

Suppose $c_0=1$ and $c_{n+1}=\sum_{i=0}^n c_i$ for $n\ge0$. The first update gives $c_1=1$. Only for $n\ge1$ do two adjacent prefix equations exist, so subtracting them gives $c_{n+1}=2c_n$. Hence $c_n=2^{n-1}$ for positive $n$, together with the separate value $c_0=1$. The incorrect extension $c_n=2^n$ satisfies neither the actual first transition nor the original prefix sum.

If $a_n=\lambda\sum_{i=0}^{n-1}a_i+f(n)$ for $n\ge1$, subtracting equations at $n$ and $n-1$ gives $a_n=(1+\lambda)a_{n-1}+f(n)-f(n-1)$ only for $n\ge2$. The value $a_1$ must still be obtained from the original equation. Conversely, a sequence satisfying the simplified recurrence and this correct first value satisfies the prefix definition by induction. That converse check proves that no information was lost in differencing.

Finite differences are useful for partial sums too. If $s_n=\sum_{j=1}^n q_j$, then $s_n-s_{n-1}=q_n$ with $s_0=0$. A polynomial $q_n$ of degree $d$ leads to a polynomial sum of degree $d+1$, because taking one finite difference lowers the degree. The constant term is fitted by the empty-sum condition, rather than guessed from positive indices alone.

## 24. Generating-function bridge with every boundary correction

Let $A(x)=\sum_{n\ge0}a_nx^n$ be a formal power series and define $D(x)=1-c_1x-\cdots-c_kx^k$. For the order-$k$ recurrence starting at $n=k$, multiplication and coefficient comparison give

$$D(x)A(x)=\sum_{n=0}^{k-1}\left(a_n-\sum_{j=1}^{n}c_ja_{n-j}\right)x^n+\sum_{n\ge k}b_nx^n.$$

For $n<k$, the coefficient on the left is an initial correction because the recurrence has not yet been imposed there. For $n\ge k$, it is exactly the prescribed forcing. This proves the identity without an assumption about convergence: each coefficient uses only finitely many products. Since $D(0)=1$, it has a unique inverse in the ring of formal power series.

For Fibonacci, $A(x)=x/(1-x-x^2)$. For domino tilings, $A(x)=1/(1-x-x^2)$. The denominator records the shared recurrence; the numerator records different bases. For the prefix-sum example, $A(x)=(1-x)/(1-2x)$, so the numerator cancels the falsely extended first step. Root one with multiplicity $m$ corresponds to a factor $(1-x)^m$ in a rational denominator; partial fractions will reconnect poles to polynomial-exponential modes in the next chapter.

## 25. Matrix states and efficient exact evaluation

For an order-$k$ recurrence, store a state vector containing the latest $k$ terms. A companion matrix maps that vector to the next state. In order two,

$$\begin{bmatrix}a_{n+1}\\a_n\end{bmatrix}=\begin{bmatrix}c_1&c_2\\1&0\end{bmatrix}\begin{bmatrix}a_n\\a_{n-1}\end{bmatrix}.$$

Matrix exponentiation computes a distant state in $O(k^3\log n)$ scalar arithmetic operations with ordinary dense multiplication. This is an arithmetic-operation count; exact integers grow in bit length, so it is not a constant-bit running-time claim. A finite-state counting matrix works similarly. A constant forcing can be represented by appending a state coordinate equal to one; polynomial forcing can be represented by further difference-state coordinates.

For Fibonacci, a practical alternative is fast doubling. From the addition identities, $F_{2m}=F_m(2F_{m+1}-F_m)$ and $F_{2m+1}=F_m^2+F_{m+1}^2$. To justify the identities, prove $F_{u+v}=F_{u-1}F_v+F_uF_{v+1}$ by induction on $v$ for positive $u$, then specialize and use $F_{m-1}=F_{m+1}-F_m$; the $m=0$ boundary is checked directly. Recursing on $\lfloor n/2\rfloor$ obtains the pair $(F_n,F_{n+1})$ using logarithmically many doubling stages.

```python
def fibonacci_pair(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if n == 0:
        return 0, 1
    a, b = fibonacci_pair(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    return (d, c + d) if n % 2 else (c, d)
```

The code uses integer operations, avoiding rounding error. A modular version reduces every arithmetic result modulo the requested modulus. The base tuple, output order, and odd-index branch are part of its correctness proof.

<!-- SIM: matrix -->

## 26. Modular recurrences: cycles, transients, and parity

Modulo $m$, an order-$k$ recurrence with constant forcing has at most $m^k$ possible states. A deterministic update must eventually revisit a state; from that point its future is periodic. It need not be periodic from the start. For $a_{n+1}=2a_n$ modulo four with $a_0=1$, the residues are $1,2,0,0,\ldots$: there is a transient before the fixed cycle.

For a homogeneous companion update, the determinant is a sign times $c_k$. If $c_k$ is invertible modulo $m$, the state map is a bijection, so every trajectory is periodic from its initial state, without a transient. With constant forcing, the same conclusion holds for the corresponding affine bijection. For time-dependent forcing, include its phase in the state if it is periodic; arbitrary forcing does not give a fixed autonomous finite-state update.

In the authenticated parity example, $a_n=3a_{n-1}+5a_{n-2}+4$ reduces modulo two to $a_n=a_{n-1}+a_{n-2}$. The odd pair at indices sixteen and seventeen leads to the repeating parity block odd, odd, even. Thus indices divisible by three in the inclusive interval one hundred through one hundred thirteen are even: one hundred two, one hundred five, one hundred eight, and one hundred eleven. No enormous integer term needs to be calculated. Track the pair state, not just one residue, because one residue alone does not determine the next term.

<!-- SIM: modular -->

## 27. Verification, stability, and what an examination actually asks

Use a systematic verification order. First confirm the recurrence class and the allowed indices. Next substitute the proposed formula into the equation symbolically. Then check every initial value. Finally, compare a few independently computed values and handle special parameter cases. A proof by uniqueness completes an exact solution; a finite numerical check alone does not.

An asymptotic answer, a residue, a requested coefficient, and a closed form are different targets. For a positive stable averaging recurrence such as $L_n=(L_{n-1}+L_{n-2})/2$, the roots one and negative one half reveal a constant limit plus a decaying alternating transient. With $L_1=u,L_2=v$, the limit is $(u+2v)/3$, not the simple average of the two starting values. The weights emerge from fitting the two modes.

For inhomogeneous models, a small residual can accumulate through unstable roots; verify exact algebra when possible instead of interpreting visually close curves as proof. The interactive traces use small exact integers and declared finite domains. Their smooth playback is explanatory, not a claim about continuous time or numerical convergence. When a problem supplies incomplete boundary data, an honest parameterized family is the correct conclusion; inventing a starting value is not.

## 28. Complete summary and method selection

A well-defined recurrence includes a value set, a valid index range, and sufficient boundary information. Forward induction establishes uniqueness. First-order equations unroll into weighted forcing contributions, including zero-coefficient reset cases. A fixed-order constant-coefficient homogeneous equation is solved by its characteristic modes; multiplicity introduces powers of the index. The nonzero-root basis theorem follows from finite differences, independence, and the dimension of the initial-data space. Zero roots instead require finite-prefix handling.

Forcing adds a particular solution to the homogeneous family. Polynomial-exponential forcing uses a resonance multiplier determined by root multiplicity, and the initial values are fitted only after all components are combined. Counting recurrences require reversible disjoint cases; forbidden patterns may need multiple states. Derangements, set partitions, integer partitions, and Catalan objects each have a different state meaning and a different algebraic structure. Prefix subtraction and generating functions expose boundary corrections that cannot be discarded.

For a distant term, exact matrix exponentiation or a proved doubling identity can replace a long linear computation. For a distant parity or residue, use a complete finite state and distinguish cycles from transients. The strongest examination habit is to preserve the assumptions while changing representation: a generating function, root expansion, matrix state, and counting bijection should describe the same sequence, including its earliest terms.

## 29. Worked mathematical, conceptual, and examination questions

<!-- INCLUDE: problems -->

## 30. Final reasoning rules and examination pitfalls

<!-- INCLUDE: review -->

## 31. Interactive laboratory and scope

<!-- LAB: recurrence -->

The companion figures in solutions state their sample parameters. They support the written derivation and do not replace a proof for a different input. Small exhaustive checks validate the models over their declared domains; the general mathematical claims are justified in the lesson. No exact physical time, analog behavior, or guaranteed result on unseen examinations is inferred from playback.

## 32. References and actual reading scopes

1. **MIT — 6.042J, Mathematics for Computer Science, Spring 2015.** Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, *Mathematics for Computer Science*, Chapter 21, PDF pages 876–891. [Official course textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). The relevant written chapter was read; this is not a claim to have read every page of the textbook.

2. **University of Oxford — Discrete Mathematics, Michaelmas Term 2010.** Andrew D. Ker, *Discrete Mathematics*, Chapter 5, PDF pages 67–80, printed pages 57–70. [Official lecture notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf). The sequence definitions, counting recurrences, linear recurrence section, and practice answers were read through the accessible web PDF text. Source discrepancies are recorded in the audit rather than silently inherited.

3. **Cornell University — CS2800, Spring 2017 course reader.** Rafael Pass and Wei-Lung Dustin Tseng, *A Course in Discrete Structures*, recurrence material in PDF pages 31–35, including Theorems 2.20 and 2.21. [Official course-hosted reader](https://www.cs.cornell.edu/courses/cs2800/2017sp/handouts/pass_tseng_discmath.pdf). Reader authors are identified here; an unverified lecturer attribution is not supplied.

4. **University of California, Berkeley — Math 55, Summer 2017.** Ritvik Ramkumar, Week 5 Thursday worksheet, both PDF pages, and Friday worksheet, both PDF pages. [Official course page](https://math.berkeley.edu/~ritvik/math55.html), [Thursday worksheet](https://math.berkeley.edu/~ritvik/Worksheet_5Th.pdf), [Friday worksheet](https://math.berkeley.edu/~ritvik/Worksheet_5F.pdf). Written exercise patterns were inspected and independently solved; exercises in the new bank are labeled as reconstructions when their parameters or presentation differ.

5. **Examination provenance.** Authenticated Iranian MSc and doctoral bridges identify the repository commit, booklet, original PDF page, question number, source hash, and independently derived answer in their own entries. They revisit original questions for this chapter and are not represented as newly discovered official answer keys.
