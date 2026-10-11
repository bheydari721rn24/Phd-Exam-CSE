## From membership semantics to exact counting

The preceding definitions and proof tutorials describe when an individual object belongs to a set. Counting problems use those same definitions to describe which complete configurations are possible. A formula such as $3^n$ is the end of a construction, not a substitute for identifying what its three alternatives mean. This section develops the constructions used in the question bank.

### 1. Encode a pair by disjoint membership regions

For $A,B\subseteq U$, every object has exactly one state: 00,10,01 or 11. These represent outside both, $A$ only, $B$ only and both. An assignment of states to all labelled objects determines the sets. Conversely, the sets determine every state. This correspondence is a bijection, so it neither omits nor duplicates pairs.

If the restriction merely permits a fixed set of $r$ local states and places no further requirement on their populations, the count on an $n$-object universe is $r^n$. The multiplication rule applies because choosing a permitted state for one object does not change the alternatives for another. For example, containment forbids 10, whereas full union forbids 00. Both leave three states, although they describe different pairs. If the restriction requires a particular state to occur, choices cease to be unrestricted: the all-other-states words must be excluded.

| Pair condition | Permitted states | Count |
|---|---|---|
| None | 00,10,01,11 | $4^n$ |
| $A\subseteq B$ | 00,01,11 | $3^n$ |
| $A\cup B=U$ | 10,01,11 | $3^n$ |
| $A\cap B=\varnothing$ | 00,10,01 | $3^n$ |
| Disjoint cover | 10,01 | $2^n$ |

For a prescribed intersection $I$, objects inside and outside $I$ have different alternatives. Inside objects are forced into 11; outside objects have three alternatives. The count is $3^{n-|I|}$. If only $|I|=j$ is specified, first choose its members and obtain $\binom nj3^{n-j}$. The binomial factor is present only in the second problem.

### 2. Require witnesses by inclusion-exclusion

Consider contained pairs with $\varnothing\ne A\subsetneq B\subsetneq U$. The three regions $A$, $B\setminus A$ and $U\setminus B$ must all be nonempty. Without that requirement there are $3^n$ assignments. Let an event mean that one of the three regions is empty. Each event leaves two choices per object, and an intersection of two events leaves one. On a nonempty universe, all three events cannot occur together. Hence

$$3^n-3\cdot2^n+3,\qquad n\ge1.$$

At $n=0$ the answer is directly zero; extending this displayed expression would give one because its omitted three-event intersection is no longer empty. This illustrates why a parameter domain belongs to the derivation.

A strict nested triple $A\subsetneq B\subsetneq C$ has four possible regions, but only $B\setminus A$ and $C\setminus B$ must be nonempty. Excluding the two missing-witness events gives $4^n-2\cdot3^n+2^n$, valid even at zero. Do not require $A$ to be nonempty unless the stem does. Strict containment asserts the existence of a difference witness, not the existence of an element of the smaller set.

### 3. Fixed populations require multinomial counting

Suppose a universe of size $n$ is assigned to labelled disjoint regions of sizes $r_1,\ldots,r_k$, with nonnegative integer sizes summing to $n$. Choose the first region, then the second from the remaining objects, and continue. The binomial factors telescope to

$$\binom n{r_1}\binom{n-r_1}{r_2}\cdots\binom{r_k}{r_k}=\frac{n!}{r_1!\cdots r_k!}.$$

The factorial denominator removes the order of objects *within* each region. It does not identify different region labels. For sizes 2,1,1,2 on six objects the count is $6!/(2!1!1!2!)=180$. The two regions of size two remain distinct; exchanging them changes membership. Summing multinomial counts over all permitted populations produces the corresponding unrestricted state count. This links the region method to the binomial and multinomial theorems rather than leaving them as unrelated shortcuts.

### 4. Recover all atoms before using cardinalities

For three sets, the eight disjoint atoms are their membership states 000 through 111. If $t=|A\cap B\cap C|$, the $A,B$-only population is $|A\cap B|-t$. The $A$-only population is

$$|A|-|A\cap B|-|A\cap C|+t.$$

The triple intersection is added back because the two pair subtractions removed it twice although it occurred once in $|A|$. The analogous formulas recover the other exclusive atoms. The outside atom is $|U|-|A\cup B\cup C|$. Each atom must be a nonnegative integer. These conditions, together with the population sum, are both necessary and sufficient for a finite realization: allocate that many distinct labelled objects to each atom and reconstruct the sets.

If exactly-two membership is asked, add the three pair-only atoms:

$$|A\cap B|+|A\cap C|+|B\cap C|-3t.$$

If at-least-two is asked, add $t$ to this quantity instead. If exactly-one is asked, sum the three singleton atoms, giving the sum of single-set sizes minus twice the sum of pair sizes plus $3t$. A diagram should display the recovered atom populations; an attractive overlap picture without those data cannot verify the calculation.

### 5. Count the objects, rather than their possible witnesses

A four-element subset of $\{1,\ldots,10\}$ contains an odd pair sum exactly when it contains at least one odd and one even number. A subset with two of each parity has four possible odd-even witness pairs. Choosing a witness pair first therefore counts this subset repeatedly, while a subset with one odd and three even elements has three witnesses. A single division factor cannot repair that unequal multiplicity.

Instead, count the failing objects: they contain only odd numbers or only even numbers. Each failure class contains $\binom54=5$ subsets and the classes are disjoint. The result is $\binom{10}4-2\binom54=200$. Alternatively, classify by the number of odd elements:

$$\binom51\binom53+\binom52\binom52+\binom53\binom51=50+100+50=200.$$

This positive enumeration independently checks the complement count. A witness-first method becomes valid only if witness multiplicities are controlled or the witness itself is part of the requested object.

### 6. Separate ordered pairs from exchange classes

For a family invariant under exchanging $A,B$, each pair with unequal coordinates belongs to a two-element exchange class. A pair with equal coordinates is fixed and belongs to a one-element class. If $N$ is the ordered count and $F$ the fixed count, the unordered count is $F+(N-F)/2=(N+F)/2$.

Covering pairs have $N=3^n$ and $F=1$, because equality and coverage force $A=B=U$. Complementary pairs on a nonempty universe have $N=2^n$ and $F=0$. Pairs with prescribed symmetric difference $D$ have $N=2^n$; they have no fixed points when $D$ is nonempty and all pairs fixed when $D$ is empty. Thus “divide by two” has different answers even when the ordered counts agree. A family not preserved by exchange, such as prescribed unequal exclusive-region sizes, cannot use this argument at all.

### 7. Keep the types of objects visible

In $A\in\mathcal P(B)$, the left object is itself a set, and the statement means $A\subseteq B$. In $\mathcal P(A)\subseteq\mathcal P(B)$, arbitrary *subsets* of $A$ must also be subsets of $B$. These statements are equivalent to $A\subseteq B$, but the quantification is over different objects.

For a transitive set $S$, every member of every member lies in $S$. Equivalently, $\bigcup S\subseteq S$; equivalently, every member of $S$ is a subset of $S$, so $S\subseteq\mathcal P(S)$. This does not mean that all subsets of $S$ belong to $S$. For $S=\{\varnothing,\{\varnothing\}\}$, the subset $\{\{\varnothing\}\}$ is missing as a member. Writing one row per brace level prevents replacing membership by containment or confusing transitivity with full downward closure. The question bank uses both elementwise proofs and explicit small families to make this distinction checkable.
