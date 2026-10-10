### 49. Derangements from two reversible cycle cases

Compute $D_8$ using a recurrence, and explain both combinatorial terms in that recurrence.

#### Solution

Choose the image $j\ne1$ of element one. If $j$ maps to one, delete their two-cycle and derange the other $n-2$ elements. Otherwise delete one from its longer cycle and splice its predecessor to $j$, leaving a derangement on $n-1$ elements. Both operations are reversible for the chosen $j$, so $D_n=(n-1)(D_{n-1}+D_{n-2})$. Starting at $D_0=1,D_1=0$ gives $1,0,1,2,9,44,265,1854,14833$. Therefore $D_8=14833$. The coefficient $n-1$ multiplies both cases because the image choice precedes the split; multiplying only the two-cycle case would miss longer cycles.

### 50. Two derangement recurrences are equivalent

Starting from $D_n=(n-1)(D_{n-1}+D_{n-2})$, prove $D_n=nD_{n-1}+(-1)^n$.

#### Solution

Define $e_n=D_n-nD_{n-1}$. Rearranging the given equation yields $e_n=(n-1)D_{n-2}-D_{n-1}=-e_{n-1}$. At one, $e_1=D_1-D_0=-1$. Therefore $e_n=(-1)^n$ by induction. The first-order inhomogeneous form follows. Conversely, substitute $D_{n-1}=(n-1)D_{n-2}+(-1)^{n-1}$ into $nD_{n-1}+(-1)^n$ and rearrange to obtain $(n-1)(D_{n-1}+D_{n-2})$. The boundary data are needed for the sign pattern. This reduction does not turn the equation into a constant-coefficient recurrence; its multiplier is still the index.

### 51. Why the empty permutation contributes one

If the derangement recurrence is required at $n=2$, determine $D_0$ from $D_1=0,D_2=1$. Explain why setting every zero-size count to zero is incorrect.

#### Solution

At two, the recurrence reads $1=1(0+D_0)$, so $D_0=1$. Combinatorially, the empty set has one bijection to itself, the empty function. It has no fixed point because there is no element violating the condition. Thus one is the correct number of empty derangements. Setting it to zero would predict $D_2=0$, contradicting the unique swap on two elements. The same empty-object convention supports tilings and set partitions, but not every problem automatically accepts an empty object: acceptance is part of the definition and must be checked.

### 52. Stirling count by insertion

Compute $S(6,3)$ and explain why the insertion multiplier is three despite the blocks being unlabeled.

#### Solution

The recurrence is $S(n,k)=S(n-1,k-1)+kS(n-1,k)$. Values built from $S(0,0)=1$ give $S(4,2)=7,S(4,3)=6,S(5,2)=15,S(5,3)=25$, hence $S(6,3)=15+3\cdot25=90$. For any particular partition into three blocks, its three subsets have different members. Adding the new element to each produces three different partitions, so there are three insertion choices without assigning external labels to the blocks. Multiplying by $3!$ would overcount. The other term creates a singleton new block and is disjoint from all insertion cases.

### 53. An exact formula for three-block set partitions

Derive $S(n,3)$ for positive $n$ from surjections, and compute $S(7,3)$.

#### Solution

Assign each element to one of three labeled boxes. There are $3^n$ assignments. Excluding assignments missing at least one box by inclusion-exclusion gives $3^n-3\cdot2^n+3$ for positive $n$; the all-empty intersection contributes zero because a positive-size domain cannot map into zero boxes. Every unlabeled three-block partition corresponds to six labelings of its blocks. Therefore $S(n,3)=(3^n-3\cdot2^n+3)/6$, giving $(2187-384+3)/6=301$ at seven. At zero this formula would give one sixth, so the positive-index qualification is essential. The true $S(0,3)$ is zero.

### 54. Bell numbers through the distinguished block

Compute $B_6$ using $B_{n+1}=\sum_{j=0}^n\binom nj B_j$, and identify the meaning of $j$.

#### Solution

The first values are $B_0=1,B_1=1,B_2=2,B_3=5,B_4=15,B_5=52$. At six the recurrence gives $1+5+10\cdot2+10\cdot5+5\cdot15+52=203$. The index $j$ is the number of old elements outside the block containing the newly added element. Choose them in $\binom nj$ ways and partition them in $B_j$ ways; the remaining old elements join the new distinguished block. This interpretation makes the construction unique. A source list ending $1,1,2,5,13$ is rejected because applying the recurrence at four gives fifteen, and that error would contaminate later values.

### 55. Exactly one singleton block

Count set partitions of five labeled elements with exactly one singleton block.

#### Solution

Choose the singleton element in five ways. Partition the remaining four elements with no singleton blocks. Those remaining blocks can be one block of size four, or two blocks of size two. The first case has one partition; the second has $\binom42/2=3$, because choosing one pair also chooses its complementary pair and otherwise counts each pair-pair partition twice. Thus the answer is $5(1+3)=20$. Multiplying five by all $B_4=15$ partitions would allow additional singleton blocks and overcount. A recurrence with an extra singleton-count state could solve larger instances, but the small block-size classification here is complete and reversible.

### 56. Marking a block changes the count

Let $M_n$ count a partition of an $n$-element labeled set together with one marked block. Show that $M_n=B_{n+1}-B_n$ for positive $n$.

#### Solution

Insert a new element into the marked block and then erase the mark. This gives a partition of $n+1$ elements in which the new element is not a singleton. Conversely, remove the new element from its nonsingleton block and mark the remaining block. The operations are inverses. There are $B_{n+1}$ partitions in total, and $B_n$ with the new element as a singleton, so $M_n=B_{n+1}-B_n$. At four, this is $52-15=37$. Equivalently $M_n=\sum_k kS(n,k)$, because each partition with $k$ blocks offers $k$ marks. The bijection independently proves the weighted Stirling identity.

### 57. Exactly three positive integer parts

Compute $p(7,3)$ using the exact-part recurrence and list every partition to verify the answer.

#### Solution

The recurrence gives $p(7,3)=p(6,2)+p(4,3)$. The two-part partitions of six are $5+1,4+2,3+3$, giving three. The only partition of four into three positive parts is $2+1+1$, giving one. Thus the result is four. The complete original list is $5+1+1,4+2+1,3+3+1,3+2+2$. The first three have a one to remove; the last has every part at least two, and subtracting one from each produces the single partition of four. Treating reordered versions of a partition as new objects would instead count compositions.

### 58. Parts bounded above by three

How many partitions of six have no part greater than three? Use both a recurrence interpretation and an independent equation count.

#### Solution

The recurrence is $P(6,3)=P(6,2)+P(3,3)$, separating partitions with no three from those with at least one three. Independently let $x,y,z$ be the multiplicities of parts one, two, and three. Solve $x+2y+3z=6$ in nonnegative integers. For $z=0$, $y=0,1,2,3$ gives four choices; for $z=1$, $y=0,1$ gives two; for $z=2$, only $y=0$ works. Total seven. This verifies $P(6,2)=4$ and $P(3,3)=3$. The parameter three is a maximum part, not an exact number of parts, so the exact-part recurrence would count a different set.

### 59. A Ferrers conjugation identity

Prove that partitions of $n$ into at most $k$ positive parts are equinumerous with partitions of $n$ whose largest part is at most $k$.

#### Solution

Draw each partition as left-aligned rows of cells in nonincreasing order. Transpose the Ferrers diagram, interchanging rows and columns. A diagram with at most $k$ rows becomes one with at most $k$ cells in its longest row, so its largest part is at most $k$. The number of cells remains $n$, and transposing twice restores the original diagram. This is a bijection, proving the identity. It does not directly equate exactly $k$ parts with largest part at most $k$; exactly $k$ rows instead correspond to largest part exactly $k$. The difference between at most and exactly cannot be dropped.

### 60. Exactly two integer parts and an endpoint

Derive $p(n,2)$ for positive $n$, and determine $p(11,2)$.

#### Solution

Write the two parts as $a\le b$ with $a+b=n$. Positivity gives $a\ge1$, and ordering gives $a\le\lfloor n/2\rfloor$. Every such $a$ determines exactly one $b=n-a$, so $p(n,2)=\lfloor n/2\rfloor$, giving five at eleven. The recurrence $p(n,2)=p(n-1,1)+p(n-2,2)$ also yields one plus the value two indices earlier, consistent with the formula. At $n=1$ no pair exists, so the floor correctly gives zero. Counting all $n-1$ positive ordered pairs would count both orders separately and, for even $n$, would also need to treat the equal pair differently.

### 61. Catalan count by first return

Compute $C_5$ from the nonlinear recurrence and explain each product in the sum.

#### Solution

With $C_0=1$, the first values are $1,1,2,5,14$. Thus $C_5=C_0C_4+C_1C_3+C_2C_2+C_3C_1+C_4C_0=14+5+4+5+14=42$. In a balanced parenthesis string, the first matched pair encloses $j$ pairs and is followed by $4-j$ pairs. Choose the enclosed and following balanced strings independently; this gives each product. The position of the first matching close makes the cases disjoint. The product of sequence values prevents a homogeneous linear characteristic method from applying. A recurrence can have a clean closed form without belonging to the linear family.

### 62. A reflection proof counts forbidden paths

Among paths with six up and six down steps, how many never go below height zero? Give a bijective subtraction argument.

#### Solution

All unrestricted paths number $\binom{12}{6}=924$. For a bad path, reflect the prefix through its first visit to height negative one, swapping up and down steps in that prefix. The transformed path has seven up and five down steps, since the reflected prefix gains one up and loses one down. Conversely, a path ending at height two has a first visit to height one; reflecting that prefix gives the unique bad balanced path. Thus bad paths number $\binom{12}{7}=792$. The valid count is $924-792=132=C_6$. Reflecting toward the opposite endpoint gives the symmetric seven-down formulation; consistency of the inverse, rather than a memorized sign, establishes the bijection.

### 63. Binary-tree sizes must distinguish internal nodes

If $T_n$ counts ordered full binary trees with $n$ internal nodes, derive its recurrence. What changes if a problem indexes by total nodes?

#### Solution

A tree with no internal node is a single leaf, so $T_0=1$. A nontrivial root is internal; if the left subtree has $j$ internal nodes, the right has $n-1-j$. Ordered children are distinct choices, giving $T_n=\sum_{j=0}^{n-1}T_jT_{n-1-j}=C_n$. A full binary tree with $n$ internal nodes has $n+1$ leaves and $2n+1$ total nodes, proved by counting child edges or induction. Therefore a total-node index $N$ has zero count when even, and count $C_{(N-1)/2}$ when odd and positive. Confusing the index conventions changes both bases and allowable sizes.

### 64. Catalan convolution with a colored root

Let $A_0=1$ and $A_n=2\sum_{j=0}^{n-1}A_jA_{n-1-j}$. Find $A_n$ and $A_4$.

#### Solution

The factor two assigns one of two colors to each internal root. A tree with $n$ internal nodes has $2^n$ independent colorings, suggesting $A_n=2^nC_n$. Substitute this form: each product contributes $2^j2^{n-1-j}=2^{n-1}$, and the outside two restores $2^n$ times the Catalan convolution. The zero base is correct, so induction proves the formula. At four, $A_4=16\cdot14=224$. Multiplying only the final Catalan answer by two would color a single distinguished root rather than every internal node, missing a factor exponential in the node count.

### 65. The generating numerator records the boundary

Derive the generating function for $a_n=5a_{n-1}-6a_{n-2}$ with $a_0=2,a_1=5$.

#### Solution

Set $A(x)=\sum_{n\ge0}a_nx^n$. Multiplying by $1-5x+6x^2$, the coefficient at zero is two and at one is $a_1-5a_0=5-10=-5$. Every coefficient from two onward vanishes by the recurrence. Hence $A(x)=(2-5x)/(1-5x+6x^2)$. Factor the denominator and split: $A(x)=1/(1-2x)+1/(1-3x)$, recovering $a_n=2^n+3^n$. The numerator is not an arbitrary constant and cannot be omitted. Formal coefficient arithmetic is valid without choosing a real interval of convergence.

### 66. A prefix recurrence leaves a numerator correction

Let $a_0=2,a_n=3\sum_{j=0}^{n-1}a_j+1$ for $n\ge1$. Derive its rational generating function.

#### Solution

The separately verified values are $a_0=2,a_n=7\cdot4^{n-1}$ for positive $n$. Thus $A(x)=2+7x/(1-4x)=(2-x)/(1-4x)$. The numerator coefficient negative one measures $a_1-4a_0=7-8$, because the simplified geometric recurrence begins only at two. Multiplying by the denominator gives two at zero, negative one at one, and zero afterward, exactly the correct early correction. A guess $2/(1-4x)$ would produce eight at one and would solve a falsely extended recurrence. Boundary corrections can be detected before any partial-fraction algebra.

### 67. Repeated poles recover index factors

Find the coefficient of $x^n$ in $(1-3x)^{-2}$ and explain the connection with a repeated characteristic root.

#### Solution

Multiply two geometric series: the coefficient is $\sum_{j=0}^n3^j3^{n-j}=(n+1)3^n$. There are $n+1$ splits of the exponent. The denominator expands as $1-6x+9x^2$, so its coefficients satisfy $a_n=6a_{n-1}-9a_{n-2}$ from two onward, with $a_0=1,a_1=6$. The polynomial is $(r-3)^2$, and the coefficient formula is a linear polynomial times $3^n$, matching the repeated-root recipe. A single pole would supply only $3^n$; multiplicity counts the additional index degree.

### 68. A forced generating-function calculation

For $a_n=2a_{n-1}+3^n$, $a_0=0$, derive $A(x)$ and recover the exact sequence.

#### Solution

For positive indices, $(1-2x)A(x)=\sum_{n\ge1}3^nx^n=3x/(1-3x)$. Hence $A(x)=3x/((1-2x)(1-3x))$. Partial fractions give $A(x)=3/(1-3x)-3/(1-2x)$, so $a_n=3^{n+1}-3\cdot2^n$. At zero the two constants cancel, as required. At one the result is three, the first forced update. Starting the forcing sum at zero would insert an extra one and violate the boundary. The algebra illustrates why a forcing series must use the recurrence's actual valid indices.

### 69. A companion matrix is a state update

For $a_n=5a_{n-1}-6a_{n-2}$, specify a matrix computing $(a_{n+1},a_n)$ from $(a_n,a_{n-1})$, and recover the scalar recurrence from its polynomial.

#### Solution

The state matrix is $M=\begin{bmatrix}5&-6\\1&0\end{bmatrix}$. Its characteristic polynomial is $z^2-5z+6$. Direct multiplication verifies $M^2-5M+6I=0$, so multiplying any state by this identity gives the same order-two recurrence in each coordinate. Starting at $(a_1,a_0)=(5,2)$, one update produces $(13,5)$ and the next $(35,13)$. The state must contain both recent terms; a one-dimensional update cannot determine the next value from $a_n$ alone. Matrix exponentiation preserves the exact boundary vector and is an alternative representation of the same recurrence.

### 70. Constant forcing as an extra coordinate

Represent $a_n=2a_{n-1}+3$ as a homogeneous matrix update in an augmented state. Use it to explain the fixed-point shift.

#### Solution

Store $(a_n,1)$. Then $\begin{bmatrix}a_{n+1}\\1\end{bmatrix}=\begin{bmatrix}2&3\\0&1\end{bmatrix}\begin{bmatrix}a_n\\1\end{bmatrix}$. The extra coordinate remains one, injecting the constant forcing on every update. The matrix has eigenvalues two and one. The constant particular solution is negative three, since $-3=2(-3)+3$, and the deviation $a_n+3$ follows the root-two mode. Thus $a_n=(a_0+3)2^n-3$. Calling the original scalar equation homogeneous would be wrong; it becomes homogeneous only after augmenting the state, with its last coordinate constrained to one.

### 71. Fast doubling with an exact pair invariant

Given $F_5=5,F_6=8$, use doubling identities to compute $F_{10},F_{11},F_{21}$ without listing every intermediate Fibonacci term.

#### Solution

The identities give $F_{10}=F_5(2F_6-F_5)=5(16-5)=55$ and $F_{11}=F_5^2+F_6^2=25+64=89$. Apply the odd doubling identity at $m=10$: $F_{21}=F_{10}^2+F_{11}^2=3025+7921=10946$. The pair invariant supplies two adjacent terms at each recursive stage, so both even and odd target branches can be formed. Knowing only $F_5$ would be insufficient for the first operation. Every calculation is exact integer arithmetic; using Binet's approximation is unnecessary for these values and introduces a separate rounding obligation.

### 72. Arithmetic count is not bit complexity

An exact matrix method uses $O(\log n)$ multiplications to compute $F_n$. Does this mean it takes $O(\log n)$ bit operations? Explain using the output size.

#### Solution

No. Binet's formula implies $F_n$ has a number of binary digits proportional to $n$ for large $n$, because $\log_2 F_n=n\log_2\phi+O(1)$. Merely writing the exact output therefore requires order $n$ bit operations. The logarithmic claim counts arithmetic stages on growing integers, treating each multiplication as one operation. A precise bit analysis must include the cost of multiplying integers of the sizes encountered. If only $F_n$ modulo a fixed small modulus is required, intermediate words can remain bounded in size, and the arithmetic-stage bound has a much closer relationship to machine time. The requested output representation changes the computational claim.

### 73. A modular transient is not a pure cycle

Track $a_{n+1}=2a_n$ modulo four from $a_0=1$. Give the transient length and eventual period, and explain why invertibility fails.

#### Solution

The states are one, two, zero, zero, and so on. The first repeated state is zero, so two initial updates lead into a fixed cycle of period one. The sequence is eventually periodic but not periodic from index zero. Multiplication by two is not invertible modulo four: both zero and two map to zero. A noninjective finite-state map can collapse several histories into a common future, which permits a transient. A pigeonhole argument guarantees some eventual repetition, not a return to the starting state. An invertible map would put every state on a cycle immediately.

### 74. A modular pair cycle gives a distant Fibonacci residue

Find $F_{1000}$ modulo three using a complete pair state and its cycle.

#### Solution

Start at $(F_0,F_1)=(0,1)$ modulo three. Updating $(u,v)$ to $(v,u+v)$ gives pairs $(0,1),(1,1),(1,2),(2,0),(0,2),(2,2),(2,1),(1,0),(0,1)$. The first return occurs after eight updates, establishing a cycle of length eight. Since 1000 is divisible by eight, the residue is $F_0=0$. The update is invertible, with inverse $(u,v)\mapsto(v-u,u)$, so there is no transient. Observing a repeated single residue would not establish the full cycle because a second-order recurrence needs the adjacent pair to determine its future.

### 75. A parity condition on a distant interval

Let $a_n=7a_{n-1}+9a_{n-2}+6$, and suppose $a_{10},a_{11}$ are odd. How many even terms occur among indices fifty through seventy, inclusive?

#### Solution

Modulo two, the recurrence becomes $a_n=a_{n-1}+a_{n-2}$. Starting with odd, odd at ten and eleven yields even at twelve, then odd, odd, and repeats. Therefore even indices in this phase are those divisible by three. In fifty through seventy they are fifty-one, fifty-four, fifty-seven, sixty, sixty-three, sixty-six, and sixty-nine, giving seven. The count can also be written $\lfloor70/3\rfloor-\lfloor49/3\rfloor=23-16=7$. The inclusive lower endpoint requires subtracting the count through forty-nine, not fifty. Large actual values and the even constant forcing do not affect this parity projection.

### 76. A periodic forcing needs a phase state

Consider $a_{n+1}=a_n+q_n$ modulo five, with $q_n$ alternating between one and two and starting at one. Why is the residue $a_n$ alone not an autonomous state? Find the state period from $a_0=0$.

#### Solution

The same residue can be followed by an addition of one or two depending on the phase. Store $(a_n,n\bmod2)$ so the update is deterministic. Over two steps the phase returns and the residue increases by three modulo five. Five such pairs are needed to return the residue to zero, giving a state period of ten. No odd number of steps can return the phase, and no smaller even number returns the residue because three is invertible modulo five. Thus the extended state, not the scalar residue alone, establishes the period. Arbitrary nonperiodic forcing would not admit this fixed finite phase extension.

### 77. Resonance can be detected by an impossible coefficient equation

A student tries $p_n=K2^n$ for $a_n-4a_{n-1}+4a_{n-2}=2^n$ and obtains zero equal to one. Diagnose the calculation and repair the trial.

#### Solution

The substitution is correct: $K2^n-4K2^{n-1}+4K2^{n-2}=0$ for every $K$, because two is a double characteristic root. The impossible matching equation means the trial lies in the homogeneous null space, not that the recurrence has no solution. Multiplicity two requires a factor $n^2$. Substituting $p_n=Kn^22^n$ gives the residual $2K2^n$, hence $K=1/2$. The complete family is $(A+Bn+n^2/2)2^n$. Two boundary values then fix $A,B$. Trying only an extra factor $n$ would still lie in the null space and would fail for the same reason.

### 78. Parameter collision changes the solution basis

Solve $a_n=(1+t)a_{n-1}-t a_{n-2}$ with $a_0=0,a_1=1$, distinguishing $t=1$ from $t\ne1$.

#### Solution

The polynomial factors as $(r-1)(r-t)$. For $t\ne1$, solve the two starting equations to get $a_n=(t^n-1)/(t-1)$. This includes $t=0$ for positive indices with the explicit zero boundary, or can be interpreted as the finite geometric sum $1+t+\cdots+t^{n-1}$, which avoids zero-power ambiguity. At $t=1$, the roots collide and the basis becomes $1,n$; the data select $a_n=n$. The finite geometric-sum identity also gives this value directly. Substituting one into a formula with denominator $t-1$ without taking the correct limit is invalid; the separate repeated-root case is essential.

### 79. Distinguish orders of counting from orders of recursion

The number of ordered compositions of $n$ into parts one and two satisfies a Fibonacci recurrence. Does the number of unordered partitions into those parts satisfy the same recurrence? Derive the latter count.

#### Solution

For an unordered partition, let $j$ be the number of twos. It may range from zero through $\lfloor n/2\rfloor$, and the remaining $n-2j$ ones are forced. Thus the count is $\lfloor n/2\rfloor+1$. It satisfies $P_n=P_{n-2}+1$ for $n\ge2$ with $P_0=P_1=1$, rather than the Fibonacci equation. Removing a last part is valid for ordered compositions because the last position is distinguished; an unordered multiset has no uniquely selected last part. At four, unordered partitions number three, while ordered compositions number five. This explicit counterexample rejects the imported recurrence.

### 80. Diagnose a wrong recurrence from its complete contract

A model claims to count binary strings avoiding the substring 11, but reports $a_0=0,a_1=1$ and $a_n=a_{n-1}+a_{n-2}$. Identify every boundary error, repair the model, and give its generating function.

#### Solution

The empty string is valid, so its count is one rather than zero. Both one-bit strings are valid, so the first positive count is two rather than one. The recurrence itself is appropriate from index two, once the last-bit decomposition has been justified. With corrected values, $a_n=F_{n+2}$ and $A(x)=(1+x)/(1-x-x^2)$, since the numerator coefficients are $a_0=1$ and $a_1-a_0=1$. The original values instead generate ordinary $F_n$ and undercount the language. Correcting only the formula's title or attaching a plausible animation would not repair its mathematical state definition; boundaries, transitions, and object meaning must agree.
