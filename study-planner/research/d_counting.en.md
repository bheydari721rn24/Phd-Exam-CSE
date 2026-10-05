# Permutations, Combinations, and Counting

## Scope, reading route, and university sources

This chapter teaches how to construct and verify a finite counting model. The objective is to solve numerical, symbolic, and conceptual examination problems by proving what each formula counts. The treatment begins with sets and sequences, develops permutations, subsets, multisets, constrained arrangements, and integer allocations, and finishes with identities, coefficient arguments, monotone indices, and exact enumeration. Read the lesson in order before using the examination rules as a review tool. The worked bank supplies detailed solutions, not a diagnostic test that you must take before learning.

Four primary written courses were genuinely reviewed for this chapter: **MIT 6.042J**, **UC Berkeley CS70**, **Stanford CS109**, and **Carnegie Mellon 15-251**. The [source audit](../reviews/d_counting-sources.html) records their precise reading boundaries, a comparison with other accessible candidates, and corrections to notation or conventions. University reputation alone does not determine the selection: MIT supplies rigorous mapping proofs; Berkeley explains when order and replacement change the sample space; Stanford contributes constrained selections and allocations; CMU supplies double-counting and polynomial-choice arguments. A course title on a candidate list is not evidence that its whole course was read.

| University and course | Written material actually used | Contribution |
|---|---|---|
| MIT, 6.042J, Lehman–Leighton–Meyer | Mathematics for Computer Science, Chapter 14, Sections 14.1–14.7 and 14.10 | Bijections, constant fibers, labeled splits, multinomials, proof discipline |
| UC Berkeley, CS70 Summer 2019 | Note 12 and Note 12.5; teaching staff James Hulett and Elizabeth Yang | The four selection models, complement, casework, symmetry, combinatorial identities |
| Stanford, CS109 Spring 2020, Lisa Yan; based on Sahami and Piech | Lecture Notes 1 and 2 | Sequential choices, nonuniform representations, constrained book selections, allocation transformations |
| Carnegie Mellon, 15-251 Fall 2010, Anupam Gupta and Danny Sleator | Lectures 7 and 8 | Choice trees, overcounting, repeated letters, binomial and multinomial expansions, lattice paths |

The next chapters separately teach inclusion–exclusion, the pigeonhole principle, recurrences, and generating functions. Here a complement removes one forbidden family, a short case sum handles a small bound, and polynomial expansion explains coefficients; this is not a replacement for those later methods. Circular symmetry is treated far enough to expose invalid division and solve small repeated-color examples, with the required proof supplied below. The declared chapter coverage is auditable; neither an exhaustive survey of every course worldwide nor perfect performance on every unseen question can honestly be certified.

## Finite models and the fundamental counting rules

### Define the object before choosing a formula

A set has no order and no repeated elements. A sequence has labeled positions and may repeat values. A multiset records multiplicities but forgets order. A partition divides a set into disjoint nonempty blocks; a collection of labeled boxes has additional identities even when two boxes hold equally many objects. These distinctions change cardinalities. Selecting two people for a committee is different from selecting a president and secretary. Placing indistinguishable tokens in labeled boxes records an occupancy vector; placing distinct tokens records the recipient of each token.

Write a model contract containing the available objects, the permitted length, which identities survive, whether repetition is allowed, the constraints, and the equivalence relation. For a four-digit integer, the first digit cannot be zero. For a four-character code, it can be zero unless prohibited. A circular arrangement usually identifies rotations; a necklace may also identify reflection. A formula cannot repair a model chosen incorrectly.

Let $\Omega$ be the finite set of valid objects. Every counting construction should establish **validity**, **coverage**, and **multiplicity**: each constructed object belongs to $\Omega$; every member of $\Omega$ is constructed; and the number of constructions producing each member is known. The last condition is the source of most factorial corrections. Being able to generate some valid examples is not enough to prove the answer.

### Disjoint addition and sequential multiplication

If $A_1,\ldots,A_t$ are pairwise disjoint finite sets, then

$$|A_1\cup\cdots\cup A_t|=\sum_{i=1}^{t}|A_i|.$$

Each object belongs to exactly one case, so it contributes once to the right side. Partitioning a committee by its exact number of engineers is valid; partitioning it into “contains engineer A” and “contains engineer B” is not disjoint. For an at-least constraint, sum all feasible exact counts, with their actual lower and upper endpoints.

For a Cartesian product, each coordinate can be chosen from its own set:

$$|A_1\times\cdots\times A_t|=\prod_{i=1}^{t}|A_i|.$$

More generally, suppose every valid prefix of length $i-1$ has exactly $b_i$ possible next entries. The identities of these choices may depend on the prefix, but their **number** must be the same at that depth. Induction on the depth of the choice tree gives $\prod_{i=1}^{t}b_i$ leaves. This is a combinatorial condition, not a requirement of probabilistic independence. Choosing distinct names successively has branch counts $n,n-1,\ldots$ even though later choices depend on earlier names.

If the second-stage branch count is $b(a)$ after first choice $a$, the correct count is $\sum_{a\in A}b(a)$. There is no product $|A|b$ unless all those values equal $b$. For pairs $1\le i\le j\le n$, the prefix $i$ has $n-i+1$ completions. Summing gives $n(n+1)/2$, whereas $n^2$ would count illegal pairs with $j<i$.

<!-- SIM:tree -->

### Bijections and the constant-fiber division rule

A bijection $f:A\to B$ has an inverse defined on every element of $B$. Consequently $|A|=|B|$. The inverse is a useful proof device: an encoding that cannot reconstruct the original object has lost information, and an encoding with two reconstructions has retained too little information.

For a surjection $f:A\to B$, the sets $f^{-1}(b)$ partition $A$. Therefore

$$|A|=\sum_{b\in B}|f^{-1}(b)|.$$

If every fiber has the same positive size $r$, this becomes $|B|=|A|/r$. The constant-fiber premise is essential. When ordered pairs over two symbols are mapped to multisets, AA and BB each have one preimage, while AB has two. Dividing four ordered pairs by $2!$ gives two, but there are three multisets. Count by multiplicities or use a different bijection instead.

The same issue occurs when permutations are mapped to binary-search-tree shapes: different insertion orders can generate the same tree with different multiplicities. A quotient is legitimate only after proving the multiplicity, not because two pictures look equivalent. MIT's division proof, Berkeley's replacement counterexample, and Stanford's tree example reinforce this same requirement in different settings.

<!-- SIM:fibers -->

## Ordered selections, subsets, and roles

### Permutations and partial permutations

An ordering of all $n$ distinct objects has $n!$ possibilities: choose each next object from those remaining. An ordered selection of $k$ distinct objects from $n$ has

$$P(n,k)=n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.$$

This formula requires integer $0\le k\le n$. There is one empty ordering, so $P(n,0)=1$ and $0!=1$. If $k>n$, there are zero injective selections; a negative factorial expression is not the way to express that fact. An unrestricted length-$k$ sequence over $n$ symbols has $n^k$ possibilities for positive $n$, because each position admits all symbols again.

An injection from a labeled $k$-element domain to an $n$-element codomain is exactly an ordered selection indexed by the domain. By contrast, selecting $k$ distinct outputs without attaching them to domain elements produces a subset. Role names count as labels even when the selected people form the same underlying set.

### Derive the binomial coefficient instead of memorizing a division

Forget the order of an ordered selection of $k$ distinct elements. Each resulting subset has precisely $k!$ preimages, one per ordering of its members. The division rule proves

$$\binom nk=\frac{n!}{k!(n-k)!}.$$

For nonnegative integer $n$, this chapter uses $\binom nk=0$ when $k<0$ or $k>n$. This convention is particularly convenient in finite sums, but it does not license negative upper arguments without a separate definition. Complementation gives $\binom nk=\binom n{n-k}$ because choosing members is equivalent to choosing excluded members.

Suppose a committee of $k$ people from $n$ has one chair and one distinct secretary. Select the committee, then assign its two roles, giving $\binom nk k(k-1)$. Alternatively select the two officers first, then the other $k-2$ members, giving $n(n-1)\binom{n-2}{k-2}$. Both expressions count the same object. Multiplying $\binom nk$ by $n(n-1)$ would let the officers lie outside the committee and therefore count a different model.

### Category constraints and safe complements

From $a$ engineers and $b$ scientists, committees of size $k$ with exactly $j$ engineers number $\binom aj\binom b{k-j}$. Valid indices satisfy $\max(0,k-b)\le j\le\min(a,k)$. “At least $r$ engineers” requires summing those products from the larger of $r$ and the feasible lower endpoint. Each committee has a unique engineer count, so these cases are disjoint.

If two specific people may not both serve, count all $k$-committees and subtract those containing both:

$$\binom nk-\binom{n-2}{k-2}.$$

The forbidden family is a subset of the declared universe. If neither person is allowed, select from $n-2$ instead. If exactly one must serve, use $2\binom{n-2}{k-1}$. These three English conditions are mathematically different. For several overlapping forbidden events, do not keep subtracting them blindly; the next inclusion–exclusion chapter supplies the general correction.

<!-- SIM:selection -->

## Repeated symbols and finite inventories

### Fixed-content words and the multinomial coefficient

Consider words of length $n$ with exactly $n_i$ occurrences of symbol $i$, where $n_1+\cdots+n_t=n$. Temporarily label the individual copies. There are $n!$ arrangements of the labeled copies. Erasing labels maps exactly $\prod_i n_i!$ arrangements to each fixed-content word, because only copies of the same symbol may exchange positions without changing the word. Thus

$$\binom{n}{n_1,\ldots,n_t}=\frac{n!}{\prod_{i=1}^{t}n_i!}.$$

Equivalently, select the positions of symbol 1, then the positions of symbol 2 from those left, and continue. The binomial factors telescope to the same multinomial. A zero multiplicity contributes $0!=1$. If the proposed multiplicities do not sum to the length, the specified word does not exist.

For AABBC, there are $5!/(2!2!)=30$ different words. If the first symbol must be A, consume one A before counting the remaining four positions: $4!/(1!2!)=12$. Multiplying the unrestricted count by a guessed fraction is unnecessary; consuming the fixed inventory gives a direct model. If the first and last symbols must be equal, split by the repeated symbol and reduce its inventory by two in each case.

<!-- SIM:word -->

### Partial words are not full permutations

Suppose an inventory contains at most $a_i$ copies of symbol $i$, but only a word of length $r$ is formed. The used multiplicities are not predetermined. First choose a feasible vector $c_1+\cdots+c_t=r$ with $0\le c_i\le a_i$, then count its words. The disjoint-case formula is

$$\sum_{c_1+\cdots+c_t=r}\frac{r!}{c_1!\cdots c_t!},\qquad 0\le c_i\le a_i.$$

Each word belongs to one multiplicity vector. Using the factorial of the entire inventory incorrectly forces unused objects into the word. For inventory AAB and length two, the feasible words are AA, AB, BA: three, not $3!/(2!1!)$ for an unrelated reason and not $P(3,2)$ with labeled A copies. The accidental equality of two numerical answers does not validate a wrong model.

The product $n^r$ assumes unlimited reuse of every symbol. The full-inventory multinomial assumes all copies are used. The bounded sum sits between these assumptions and handles the actual available stock. This distinction also matters for passwords with a prescribed number of distinct symbols, where the symbols must first be selected and then every selected symbol must actually occur.

## Adjacency, separation, and circular equivalence

### Blocks and gaps in a line

If a specified set of $r$ distinct people must occupy consecutive seats in a line with $n$ distinct people, contract that set into a single block. Arrange $n-r+1$ units and then arrange the $r$ people inside their block: $(n-r+1)!r!$. The contraction and expansion are inverse operations. If their internal order is fixed, omit $r!$. If several disjoint specified groups must each be consecutive, contract each separately; overlapping blocks need separate analysis because the simple contraction may not be unique.

For two specified distinct people, adjacency gives $2(n-1)!$. Nonadjacency gives $n!-2(n-1)!$. An “at least one adjacent pair among several pairs” condition is not counted by adding these values without checking overlap.

To arrange $q$ identical A symbols and $p$ distinct other symbols with no adjacent As, first arrange the other symbols in $p!$ ways. They create $p+1$ gaps, including both ends. Select $q$ different gaps and put one A in each, giving $p!\binom{p+1}{q}$. If the As are distinct, also multiply by $q!$. If the other symbols repeat, replace $p!$ by their own multinomial, since the gap positions still retain their left-to-right identities.

For binary strings of length $n$ with exactly $k$ ones and no adjacent ones, list the selected positions as $a_1<\cdots<a_k$ with $a_{i+1}\ge a_i+2$. Set $b_i=a_i-(i-1)$. Then $1\le b_1<\cdots<b_k\le n-k+1$, and the inverse $a_i=b_i+(i-1)$ preserves separation. Therefore the count is $\binom{n-k+1}{k}$. Feasibility requires $n\ge2k-1$ for positive $k$; the empty selection has one representation.

More generally, requiring at least $s$ zeros between successive ones compresses positions by $s(i-1)$ and gives $\binom{n-s(k-1)}{k}$ when the parameters are feasible. No zeros are automatically required at the two ends; imposing endpoint conditions consumes additional positions first.

<!-- SIM:gaps -->

### Distinct people around a circle

With $n\ge1$ distinct people and rotations identified but clockwise orientation preserved, each circular arrangement corresponds to exactly $n$ linear sequences, one per starting person. The answer is $(n-1)!$. Fixing a distinguished person at the top gives the same count by a bijection.

If reflection is also identified and $n\ge3$, each orientation-preserving circular arrangement pairs with a different reflected arrangement, so the count is $(n-1)!/2$. For one or two people this division is invalid: reflection does not create a second circular order. Numbered seats do not identify rotations at all, so they give $n!$.

Circular adjacency includes the edge connecting the last seat to the first. For two specified people with $n\ge3$ distinct people, contracting their clockwise or counterclockwise block gives $2(n-2)!$ rotation classes. For circular separation, a gap argument around the arranged unmarked people has $p$ gaps rather than $p+1$; endpoint gaps in a line become the same circular gap.

### Why repeated-color necklaces require more care

A binary circular word can have a short period. AABB has four distinct rotations; ABAB has only two. Among the six labeled-seat words with two As and two Bs, four belong to the AABB orbit and two to the ABAB orbit, so there are two orbits, not $6/4$. A uniform division by the number of rotations is invalid.

For a finite group $G$ acting on a finite set $X$, count the pairs $(g,x)$ satisfying $gx=x$. Counting first by $g$ gives $\sum_{g\in G}|\operatorname{Fix}(g)|$. In an orbit of size $r$, each of its $r$ objects has $|G|/r$ stabilizing group elements: the elements carrying a fixed representative to one target form a coset of its stabilizer. Hence each orbit contributes $|G|$ fixing pairs. Dividing proves the orbit-counting identity

$$\text{number of orbits}=\frac{1}{|G|}\sum_{g\in G}|\operatorname{Fix}(g)|.$$

For rotations of a length-$n$ word over $q$ colors, rotation by $r$ places has $\gcd(n,r)$ cycles. A fixed word is constant on each cycle, so its count is $q^{\gcd(n,r)}$. If the number of each color is fixed, each cycle must contribute its full length to a color inventory; some rotations therefore fix no words. Use explicit cycle assignments rather than the unrestricted-color expression. This extension is independently derived here; it is not claimed to be fully covered in all four selected lectures.

<!-- SIM:circle -->

## Integer allocations, inequalities, and box identities

### Stars and bars is a bijection

For $N\ge0$ and $m\ge1$, a nonnegative solution of $x_1+\cdots+x_m=N$ is encoded by $N$ stars and $m-1$ bars, with $x_i$ stars between the corresponding consecutive bars. Empty boxes produce consecutive bars or bars at an endpoint; both are allowed. Conversely every such star–bar string reconstructs one solution. Selecting the bar positions proves

$$\#\{x_i\ge0:\sum_i x_i=N\}=\binom{N+m-1}{m-1}.$$

The boxes are labeled by their order. Stars are identical, not individually labeled tokens. A multiset of size $N$ selected from $m$ types is the same multiplicity vector and has this count. It is not $m^N/N!$, because ordered words with different multiplicities have different permutation fibers.

<!-- SIM:stars -->

### Lower bounds and unused capacity

For integer bounds $x_i\ge\ell_i$, define new variables $y_i=x_i-\ell_i$. They are nonnegative, their sum is $N-L$ where $L=\sum_i\ell_i$, and the inverse is $x_i=y_i+\ell_i$. The count is zero if $N<L$ and otherwise $\binom{N-L+m-1}{m-1}$. Use new variable names: saying that the old $x_i$ now sum to a smaller number obscures the bijection. For positive variables, all lower bounds equal one, giving $\binom{N-1}{m-1}$ when $N\ge m$.

For $x_1+\cdots+x_m\le N$, introduce the uniquely determined slack $s=N-\sum_i x_i\ge0$. Counting nonnegative solutions in $m+1$ variables gives $\binom{N+m}{m}$. This extra variable represents unused capacity, not an additional arbitrary choice. If the total must lie between $L$ and $U$, subtract the count with total at most $L-1$ from the count with total at most $U$, with the zero case handled correctly.

### Upper bounds, parity, and coupled equations

If only $x_1\le u$ is imposed on a nonnegative total-$N$ solution, subtract those with $x_1\ge u+1$. Translating that bad family gives

$$\binom{N+m-1}{m-1}-\binom{N-u-1+m-1}{m-1},$$

where the second term is zero if its residual total is negative. Several upper bounds usually produce overlapping violations; sum over a short bounded variable or use the later inclusion–exclusion chapter. With $0\le x_1\le u$ and $0\le x_2\le v$, an exact alternative is $\sum_{a=0}^{u}\sum_{b=0}^{v}\binom{N-a-b+m-3}{m-3}$ for $m\ge3$, treating negative residual totals as zero rather than assigning generalized negative-upper binomial values.

If $x_1$ must be even, write $x_1=2j$ and sum over feasible $j$. Stars and bars no longer applies to a weighted sum as though its coefficients were all one. For $a+b+c=17$, $a$ even, $b\le3$, and $c\ge1$, translating $c$ gives $2j+b+c'=16$. For each fixed $b$, there are $\lfloor(16-b)/2\rfloor+1$ possible $j$, each forcing $c'$. The four disjoint counts are 9, 8, 8, and 7, totaling 32.

For coupled equations, eliminate a shared sum before multiplying independent blocks. If $x_1+x_2=4$ and $x_1+x_2+x_3+x_4=11$, then $x_3+x_4=7$. There are $5\cdot8=40$ solutions. Multiplying the unrestricted counts of the original two equations would not enforce their simultaneous compatibility.

### Distinct balls, unlabeled groups, and the empty-box exception

Assigning $N$ distinct objects to $m$ labeled boxes with no occupancy restriction gives $m^N$. Prescribing occupancies $n_1,\ldots,n_m$ gives $N!/\prod_i n_i!$. Making the boxes unlabeled does not universally mean dividing by $m!$: empty boxes or equal contents can introduce stabilizers. If all boxes are nonempty and contain disjoint sets of distinct objects, their contents are different sets, so each unlabeled partition has exactly $m!$ labelings.

For prescribed **unlabeled nonempty block sizes**, let $a_j$ be the number of blocks of size $j$. Then

$$\frac{N!}{\left(\prod_j(j!)^{a_j}\right)\left(\prod_j a_j!\right)}$$

counts partitions of the $N$ distinct elements. Divide internally by $j!$ for each block, and externally by $a_j!$ for the interchangeable blocks of equal size. Do not divide by the factorial of the total number of blocks if their different sizes already distinguish them. For sizes 2,2,3, the external correction is $2!$, not $3!$.

The Stirling number $S(N,m)$ counts partitions into $m$ nonempty unlabeled blocks. Placing a new distinct element either into one of $m$ existing blocks or alone in a new block proves $S(N,m)=mS(N-1,m)+S(N-1,m-1)$, with $S(0,0)=1$ and impossible parameters giving zero. This small recurrence is explained as a partition identity; systematic recurrence-solving remains a later chapter. Assignments to $m$ labeled nonempty boxes number $m!S(N,m)$. Identical objects in unlabeled boxes instead form integer partitions, a different model.

<!-- SIM:groups -->

## Binomial identities, coefficients, and parity

### Pascal, Vandermonde, and marked subsets

For $0\le k\le n$, separate $k$-subsets according to whether they contain a particular element. This gives Pascal's identity $\binom nk=\binom{n-1}{k}+\binom{n-1}{k-1}$, with boundary terms interpreted as zero. Every subset belongs to exactly one case. Repeated use constructs Pascal's triangle, but the proof comes from the set partition rather than from the visual pattern.

From disjoint sets of sizes $a$ and $b$, classify a $k$-subset by how many members come from the first set. This proves Vandermonde's identity

$$\sum_j\binom aj\binom b{k-j}=\binom{a+b}{k}.$$

Only feasible terms contribute. Taking $a=b=n$ and $k=n$, then using symmetry, gives $\sum_{j=0}^{n}\binom nj^2=\binom{2n}{n}$. A product of coefficients does not automatically collapse; the complementary indices and shared total must match the identity.

Count a subset of size $i$ together with $r$ marked members. Choosing the subset first gives $\binom ni\binom ir$; choosing the marked members first gives $\binom nr\binom{n-r}{i-r}$. Summing over $i$ gives

$$\sum_{i=r}^{n}\binom ni\binom ir=\binom nr2^{n-r}.$$

The free remaining subset explains the power of two. For $r=1$ this yields $\sum_i i\binom ni=n2^{n-1}$. Since $i^2=i(i-1)+i$, the second moment is $n(n-1)2^{n-2}+n2^{n-1}$ for $n\ge2$. Counting two **distinct ordered** marked members uses $i(i-1)$, not $i^2$.

Partition $(r+1)$-subsets of $\{1,\ldots,n+1\}$ by their largest element $j+1$. The remaining $r$ members lie among $j$ smaller elements, proving the hockey-stick identity $\sum_{j=r}^{n}\binom jr=\binom{n+1}{r+1}$. Specifying the smallest element gives a reverse-indexed equivalent proof. It is the unique extreme member that makes the cases disjoint.

<!-- SIM:pascal -->

### Polynomial expansion as labeled choices

To expand $(a+b)^n$, select either $a$ or $b$ from each of $n$ labeled factors. Exactly $k$ choices of $b$ can be made in $\binom nk$ ways. Thus

$$ (a+b)^n=\sum_{k=0}^{n}\binom nk a^{n-k}b^k.$$

The theorem holds for commuting variables or numbers; arbitrary noncommuting matrices do not allow the same collection of terms into a scalar binomial coefficient. The coefficient of $x^s$ in $(\alpha x^p+\beta x^q)^n$ comes from integers $k$ satisfying $p(n-k)+qk=s$ and $0\le k\le n$. For $p\ne q$ there is at most one such integer $k$, and its contribution is $\binom nk\alpha^{n-k}\beta^k$. A noninteger or out-of-range $k$ means coefficient zero. If $p=q$, combine like terms before using that reasoning.

With more summands, the exponent equations may have several feasible multiplicity vectors. For $(1+x+x^2)^4$, the coefficient of $x^4$ receives contributions from vectors $(c_0,c_1,c_2)$ with $c_1+2c_2=4$ and $c_0+c_1+c_2=4$. These are $(0,4,0)$, $(1,2,1)$, and $(2,0,2)$; their multinomial counts are 1, 12, and 6, totaling 19. Counting only one vector omits valid terms. Generating functions later generalize this idea to richer and unbounded structures.

### Even and odd symbol counts

Suppose a length-$n$ word uses $u$ unmarked symbols and $v$ marked symbols. The count with exactly $k$ marked positions is $\binom nk v^ku^{n-k}$. Adding the expansions of $(u+v)^n$ and $(u-v)^n$ cancels odd $k$, while subtracting cancels even $k$. Therefore

$$E_n=\frac{(u+v)^n+(u-v)^n}{2},\qquad O_n=\frac{(u+v)^n-(u-v)^n}{2}.$$

For positive length and $u=v$, the classes are equal. Otherwise they need not be equal. With three unmarked symbols and one marked symbol, the difference is $2^n$. For length zero, the empty word has even marked count, so $E_0=1$ and $O_0=0$; handle that case explicitly when a zero base appears. Symmetry arguments must exhibit an actual parity-flipping bijection before claiming “half.”

## Monotone indices, paths, and exact algorithms

### Weakly increasing sequences

A weakly increasing sequence $1\le a_1\le\cdots\le a_k\le n$ is determined by the multiplicities of its $n$ values. This gives $\binom{n+k-1}{k}$. Alternatively define $b_i=a_i+i-1$; then $1\le b_1<\cdots<b_k\le n+k-1$. The inverse subtracts the same offsets and restores weak monotonicity. Strictly increasing sequences instead count $\binom nk$. Weak monotonicity does not mean that all outputs are distinct.

For three nested inclusive loops with $1\le i\le j\le k\le n$, the body executes $\binom{n+2}{3}$ times. If a counter starts at $c$ and increments by one, its final value is $c+\binom{n+2}{3}$. Starting the innermost loop at $j+1$ changes one inequality to strict and therefore changes the count. Asymptotic order alone cannot distinguish exact multiple-choice answers.

### Lattice paths and obstacles

A path from $(0,0)$ to $(a,b)$ using only unit right and up steps has exactly $a$ R symbols and $b$ U symbols. The word–path mapping is bijective, so there are $\binom{a+b}{a}$ paths. If it must pass through $(r,s)$ within the rectangle, split uniquely at that point and multiply $\binom{r+s}{r}\binom{a+b-r-s}{a-r}$. Subtract this from the total to avoid one point. For two required points, coordinatewise ordering is necessary; incomparable points cannot both lie on a monotone path.

For paths from $(0,0)$ to $(n,n)$ that never go above $y=x$, reflect the prefix up to and including the first step reaching $y=x+1$ by exchanging U and R. A bad path originally has $n$ of each step; the reflected prefix has one more R than before, giving $n+1$ R and $n-1$ U overall. Conversely a word with those totals must first reach $x=y+1$; reflecting that prefix reconstructs a unique bad path. Thus bad paths number $\binom{2n}{n-1}$, and valid paths number

$$\binom{2n}{n}-\binom{2n}{n-1}=\frac{1}{n+1}\binom{2n}{n}.$$

The endpoint is changed by the reflection; retaining $(n,n)$ after the transformation would hide the essential bijection. The resulting Catalan count is included as a proved advanced application, not as a complete chapter on Catalan structures.

<!-- SIM:path -->

### Implement exact counts without silently changing the model

For numerical evaluation, compute binomial coefficients by a multiplicative recurrence using exact integers. The quotient at each iteration is integral because the partial value equals a binomial coefficient, not because arbitrary integer division is harmless.

```python
def choose(n, k):
    if n < 0:
        raise ValueError("The upper argument must be nonnegative")
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for j in range(1, k + 1):
        result = result * (n - k + j) // j
    return result
```

Before iteration $j$, the value is $\binom{n-k+j-1}{j-1}$. Multiplying by $(n-k+j)/j$ gives $\binom{n-k+j}{j}$, proving the loop invariant and exact divisibility. The loop has $k$ arithmetic iterations, but integer operands grow; this is not automatically $O(k)$ bit complexity. Fixed-width implementations can overflow even when the final result fits, because the multiplication occurs before division.

Brute-force enumeration is valuable as an independent check for small parameters. Generate every ordered tuple, filter the actual constraints, and canonicalize only if the declared equivalence requires it. For a circular word, the lexicographically smallest rotation is a canonical representative; add reversed rotations only when reflection is identified. Enumeration checks finite cases, not a theorem for all sizes. The chapter laboratory exposes both the formula and its small-instance enumeration so that a mismatch identifies a model or implementation error.

## Fully worked mathematical and conceptual problems

The bank contains eight authentic archive revisits and eighty original or independently worded course-inspired problems. Authentic entries retain booklet, question number, PDF page, and original-file fingerprint in the audit. Their answers are independently derived, not represented as official answer keys. The new problems span formula construction, integer bounds, symmetry, identities, coefficient conditions, exact loops, and counterexamples. Their difficulty labels are author assessments rather than measured examination statistics.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

### A decision procedure for a new problem

First define one outcome precisely. Determine whether identities and positions survive, whether copies repeat, whether boxes are labeled, and whether rotations or reflections are identified. Then construct a bijection or a disjoint decomposition. If the construction overcounts, compute the fiber for every type of outcome before dividing. Translate lower bounds with new variables; encode parity or weighted contributions explicitly. Evaluate the final expression only after checking feasibility and the endpoints of every sum. Finally test a small case that preserves the same constraint pattern.

The four unrestricted selection models are $n^k$ for ordered selections with unlimited repetition, $n!/(n-k)!$ for ordered selections without repetition, $\binom nk$ for unordered selections without repetition, and $\binom{n+k-1}{k}$ for unordered selections with unlimited repetition. Their hypotheses matter as much as their values. Fixed-content words, bounded stock, labeled allocations, nonempty unlabeled partitions, and cyclic patterns require additional structure.

An examination solution should state a construction, a reason it is complete, and a multiplicity argument. A compact final formula can represent a deep proof; a long factorial expression without those checks can represent a wrong sample space. The following eighty rules give complete statements with the conditions that make them usable.

<!-- INCLUDE:review -->

## Interactive counting laboratory

Use the embedded traces at the relevant lesson sections to inspect specific bijections, gaps, rotation orbits, and path prefixes. They have pause, reset, and forward/backward controls. The independent laboratory below enumerates small cases you choose; it does not require you to answer a test. Labeled sequences, separated subsets, weak compositions, and rotation classes use different displays because they represent different objects.

<!-- LAB:counting -->

## References and provenance

1. Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. **Mathematics for Computer Science**, revision May 18, 2015. MIT 6.042J, Chapter 14, Sections 14.1–14.7 and 14.10. [Official text](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). These sections were read in the cached original PDF text, with the counting proof boundaries recorded in the source audit.
2. UC Berkeley CS70, Summer 2019. **Note 12: Counting**, and **Note 12.5: More Counting**. Course instructors James Hulett and Elizabeth Yang; the notes themselves do not identify an individual author. [Note 12](https://www.su19.eecs70.org/static/notes/n12.pdf), [Note 12.5](https://www.su19.eecs70.org/static/notes/n12.5.pdf). Both notes were read; their inclusion–exclusion preview informs the boundary with the next chapter.
3. Lisa Yan. Stanford CS109, Spring 2020. **Lecture Notes 1: Counting**, April 6, 2020, and **Lecture Notes 2: Combinatorics**, April 8, 2020. Based on handouts by Mehran Sahami and Chris Piech. [Notes 1](https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN01_counting.pdf), [Notes 2](https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN02_combinatorics.pdf). Both complete handouts were reviewed.
4. Anupam Gupta and Danny Sleator. Carnegie Mellon University, **15-251: Great Theoretical Ideas in Computer Science**, Fall 2010. **Lecture 7: Counting I** and **Lecture 8: Counting II: Pascal, Binomials, and Other Tricks**. [Lecture 7](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15251-f10/Site/Materials/Lectures/Lecture07/lecture07.pdf), [Lecture 8](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15251-f10/Site/Materials/Lectures/Lecture08/lecture08.pdf). Original PDF page text was read through the web PDF reader; the native downloader failed and no successful local download is claimed.
5. **Iranian MSc Computer Science examination, 1405**, booklet 257A, Questions 113, 115, 120–123, and 129; **Iranian doctoral Computer Science examination, 1405**, booklet 693A, Question 20. [Project examination archive](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/main/Exams). Exact pinned links occur beside each worked revisit. Pages 25, 26, 28, and 8 were rendered and visually checked against the English adaptations in this delivery.

The lesson is independently written. Standard mathematical results are proved with explicit assumptions; course connections acknowledge their instructional influence. Selected course patterns are adapted with new wording and parameters rather than reproducing complete protected question banks. [Quality and uncertainty audit](../reviews/d_counting-quality.html) documents the numerical checks, visual checks, limits of coverage, and draft approval status.
