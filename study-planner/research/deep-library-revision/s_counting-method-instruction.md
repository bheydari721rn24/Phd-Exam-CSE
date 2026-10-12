## Mathematical constructions for the examination applications

The original instruction above and the complete tutorials below remain part of this chapter. This section develops the additional constructions used in the examination bank. A count is exact only after the objects, their equivalence relation, and any probability law have been specified.

### 1. Quotients, constant fibers, and induced probabilities

Let $f:X\to Y$ erase part of a detailed description. If every $y\in Y$ has exactly $c>0$ preimages, the disjoint fibers partition $X$, proving $|X|=c|Y|$. This is the entire justification for dividing a count by $c$. Listing distinct members of a $k$-subset has fiber $k!$. Ordering a pairing has fiber $2^n n!$. Naming three nonempty unnamed groups has fiber $3!$. These divisors remove different kinds of information.

For a uniform random detailed outcome, $P(f(X)=y)=|f^{-1}(y)|/|X|$. Thus uniform detailed outcomes give uniform summaries if and only if all fibers have equal size. Three fair bits have report fibers $1,3,3,1$, not four equal fibers. Sorting a word also has variable fibers $n!/\prod c_i!$. A multiset count and a multiset probability therefore require different calculations.

The repeated-letter circle illustrates a second failure: AABB has four distinct rotations, ABAB only two. Dividing six linear words by four cannot count their two rotational classes. For a finite group $G$ acting on $X$, a general remedy is

$$|X/G|=\frac{1}{|G|}\sum_{g\in G}|\{x:g(x)=x\}|.$$

To prove this orbit formula, count pairs $(g,x)$ with $g(x)=x$. An orbit of size $m$ has a stabilizer of size $|G|/m$ at each of its $m$ points, contributing exactly $|G|$ pairs. Summing over orbits and dividing proves the identity. In the four-letter example, the identity rotation fixes six words, the half-turn fixes two, and the quarter-turns fix none: $(6+2)/4=2$. The simple quotient is the special case where only the identity fixes outcomes.

### 2. A single ledger for bounds, parity, and total inequalities

For named integer coordinates $x_i\ge L_i$ with total $T$, set $y_i=x_i-L_i$. The residual $R=T-\sum L_i$ must be nonnegative; otherwise there are no solutions. If no upper bounds remain and there are $r\ge1$ coordinates, stars and bars gives $\binom{R+r-1}{r-1}$. A total inequality becomes an equality by adding its uniquely determined nonnegative slack coordinate.

An upper bound $y_i\le U_i$ is violated first at $U_i+1$. Inclusion–exclusion gives

$$N=\sum_{J\subseteq\{1,\ldots,r\}}(-1)^{|J|} H\left(R-\sum_{j\in J}(U_j+1)\right),$$

where $H(t)=\binom{t+r-1}{r-1}$ for $t\ge0$ and $H(t)=0$ otherwise. Each term comes from shifting exactly the coordinates in $J$ past their first forbidden values. The zero convention is a feasibility statement, not a factorial evaluation at a negative integer.

When a coordinate must be even, write it as twice a new nonnegative integer. Its coefficient remains two. For $2a+b+c=R$ with $0\le b\le u$, fixing $b$ leaves $\max(0,\lfloor(R-b)/2\rfloor+1)$ pairs $(a,c)$. This exact row ledger is preferable to halving an unrestricted count. For Question 68 the rows are $9,8,8,7$; their sum 32 retains every endpoint.

### 3. Surjections and exact fibers

For maps from $m$ distinct objects to $r$ named targets, exclude the events that targets are absent. A specified $j$-set of missing targets leaves $(r-j)^m$ maps. Hence, for $m\ge1$,

$$N_{m,r}=\sum_{j=0}^{r}(-1)^j\binom rj(r-j)^m.$$

If $m<r$, the answer is zero by feasibility. If $m=0<r$, count the empty map in each exclusion intersection before simplifying; the onto count is zero. Erasing target names after enforcing nonemptiness divides by $r!$, because all nonempty disjoint fibers are distinct. Stars and bars alone counts fiber-size vectors; each vector $(c_1,\ldots,c_r)$ contributes $m!/\prod c_i!$ assignments.

For a restriction on the first fiber, partition by its exact size $k$ and choose all its members. Then count an onto map on the remainder: $\binom mk N_{m-k,r-1}$. Question 69 uses $k=2,3$. Choosing only two witnesses for a larger fiber is not a unique description: a size-$k$ fiber has $\binom k2$ such witnesses. Overcounting cannot be repaired by an arbitrary common divisor.

### 4. Parity filters and coefficient feasibility

If a distinguished symbol has weight $t$ and each of $q-1$ other symbols weight one, the word-count polynomial is $F(t)=(q-1+t)^n$. Its coefficient of $t^k$ is $\binom nk(q-1)^{n-k}$. Substituting $t=1$ adds every coefficient; substituting $t=-1$ adds even coefficients and subtracts odd ones. Therefore

$$E_n=\frac{F(1)+F(-1)}2,\qquad O_n=\frac{F(1)-F(-1)}2.$$

This derivation explains why four symbols give correction $2^n$ while three symbols give correction one. The empty word is counted directly if a displayed power uses a zero base. Filters isolate counts; they do not establish random independence.

For $(x^a+x^b)^m$, choosing $j$ first terms gives exponent $bm+(a-b)j$. A requested exponent $s$ is reachable only if $j=(s-bm)/(a-b)$ is an integer in $[0,m]$ when $a\ne b$. Its coefficient is then $\binom mj$. Otherwise the coefficient is zero. If $a=b$, the entire expression is $2^m x^{am}$ and needs separate treatment. Negative exponents create a Laurent polynomial without invalidating the argument. Question 8 fails the integer test, even though its exponent lies in the range.

### 5. Nonadjacent positions and recursion with empty constructions

For $j$ nonadjacent selected positions $p_1<\cdots<p_j$ in a row of length $n$, remove one required gap before each selected position except the first: $q_i=p_i-(i-1)$. Then the $q_i$ form an ordinary $j$-subset of $\{1,\ldots,n-j+1\}$. Conversely restore $p_i=q_i+(i-1)$. This proves the fixed-weight count $\binom{n-j+1}j$, with feasibility $j\le\lfloor(n+1)/2\rfloor$.

Without fixing weight, prefix deletion proves $T_n=T_{n-1}+T_{n-2}$ for $n\ge2$. The seeds are $T_0=1,T_1=2$. The empty construction is necessary because prefix 10 may leave no suffix. These seeds and the recurrence produce $1,2,3,5,8,13,21,34,55$. Summing the fixed-weight counts gives the same total and verifies a second route. Cyclic adjacency requires a different endpoint treatment: the first and last positions are neighbors, so the linear formula cannot be transferred unchanged.

### 6. Dependence beyond pair tests and information loss

Mutual independence of events $A_1,\ldots,A_m$ requires factorization for every nonempty index subset, not merely pairs or the largest intersection. Complement preservation follows by subtracting intersections; iterating the argument yields every binary pattern mass. Conversely, summing factorized pattern masses over unconstrained coordinates establishes every intersection condition. This equivalence explains why a full pattern table is a constructive independence proof.

An economical pairwise-independent construction uses $b$ independent fair bits. For each distinct nonzero binary vector $v$, report the parity $v\cdot U$ modulo two. Each parity is fair because at least one input bit toggles it. For two distinct nonzero vectors $v,w$, they are linearly independent over the two-element field: the only nonzero scalar is one, and $v\ne w$. Two independent equations therefore have $2^{b-2}$ solutions for each pair of outputs, proving pairwise independence when $b\ge2$. Higher-order factorization need not hold: for $b=2$, the three nonzero parities satisfy a deterministic xor relation.

To provide $n\ge1$ such bits, choose $b=\lceil\log_2(n+1)\rceil$. There are $2^b-1\ge n$ nonzero vectors, and $n+1\le2^b<2(n+1)$. The enumeration cost is proportional to $n$, not exactly $n$. Oxford's “Bits for free” discussion writes the stronger equality $2^b=n$ at one point; the bound above is the corrected claim. A simulation can enumerate this law exactly but cannot promote pairwise independence to mutual independence.
