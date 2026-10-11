## Applicable formulas, conceptual checks and examination rules

These rules condense the proved methods, rather than replace them. For a new question, identify the given universe and counted objects, translate every condition, and only then apply a formula whose hypotheses match. Every finite counting formula below assumes labelled universe objects unless stated otherwise.

### 1. Membership and containment have different meanings

$x\in A$ says that $x$ is one member. $X\subseteq A$ says that every member of the set $X$ is a member of $A$. Expand a containment as a universal implication. The empty set is a subset of every set because it supplies no violating element; it need not be a member. $\varnothing$, $\{\varnothing\}$ and $\{\{\varnothing\}\}$ are three distinct sets.

### 2. Proper containment needs a missing-region witness

$A\subsetneq B$ means $A\subseteq B$ and there exists an element of $B\setminus A$. It does not require $A$ to be nonempty. An $n$-object universe has $3^n$ contained ordered pairs and $3^n-2^n$ proper-contained pairs. The subtracted term counts equal pairs. By contrast, a size inequality $|A|<|B|$ alone does not establish containment.

### 3. Equality proofs must control both directions

To prove $A=B$, prove both inclusions or show equivalent membership tests for every object. One inclusion and equal finite cardinalities also suffice, but equal cardinalities alone do not: two distinct singletons are a counterexample. To refute equality, exhibit a member of exactly one side and verify all premises of the proposed identity.

### 4. Complement is relative to one declared universe

$A^c=U\setminus A$. De Morgan gives $(A\cup B)^c=A^c\cap B^c$ and $(A\cap B)^c=A^c\cup B^c$. Each can be derived by negating the membership condition. Changing the universe changes the complements, so do not compare expressions that silently use different universes. Difference satisfies $A\setminus B=A\cap B^c$ under this common-universe convention.

### 5. Difference is directional and does not associate like subtraction

Expand all parentheses before simplifying. For example, $A\setminus(B\setminus C)=(A\setminus B)\cup(A\cap C)$, whereas $(A\setminus B)\setminus C=A\setminus(B\cup C)$. Taking $A=B=C=\{u\}$ gives different results, so those parenthesizations cannot be interchanged. Equal results after deleting the same set do not imply equal original sets: the deleted region conceals information.

### 6. Symmetric difference is cancellable XOR

$A\triangle B=(A\setminus B)\cup(B\setminus A)$, and $A\triangle B\triangle B=A$. Thus $A\triangle B=D$ forces $B=A\triangle D$ and has $2^n$ ordered solutions. Membership toggles twice and returns to its original value. This involution is not idempotence; a nonempty fixed toggle changes some membership bit. Union and intersection do not have the same cancellation property.

### 7. Check feasibility through every disjoint atom

For two finite subsets of an $n$-object universe with sizes $a,b$ and intersection $t$, require $\max(0,a+b-n)\le t\le\min(a,b)$. The four atom sizes are $t,a-t,b-t,n-a-b+t$. For three sets, recover all eight atoms, not just pairwise bounds. Nonnegative integer atom sizes are necessary and sufficient for a finite set realization.

### 8. Distinguish exactly two from at least two

Write $s_1=|A|+|B|+|C|$, $s_2=|A\cap B|+|A\cap C|+|B\cap C|$ and $t=|A\cap B\cap C|$. Union has size $s_1-s_2+t$; exactly two has size $s_2-3t$; at least two has size $s_2-2t$; exactly one has size $s_1-2s_2+3t$. Derive each coefficient by asking how many times a triple-region object was counted. Outside has size $|U|-(s_1-s_2+t)$.

### 9. Select permitted local states before choosing an exponent

An unrestricted pair has four states; containment, coverage alone and disjointness alone each have three different states; a complementary pair has two. With no population restrictions, $r$ permitted states yield $r^n$. A state that is required to occur needs a missing-witness subtraction, and a prescribed population needs binomial or multinomial selection. Similar-looking exponents do not imply equivalent conditions.

### 10. A nested chain has entry positions

A chain of $k$ labelled sets permits $k+1$ membership states per object, hence $(k+1)^n$ non-strict chains. A proper three-set chain requires two difference regions nonempty and gives $4^n-2\cdot3^n+2^n$. If the smallest set must also be nonempty, introduce another required region. If the largest must be proper in $U$, introduce the outside witness too. Do not add those assumptions without the stem.

### 11. Disjointness does not imply coverage

Three pairwise-disjoint subsets have four local states including outside-all, so their count is $4^n$. Adding coverage gives $3^n$. Empty triple intersection alone forbids only 111 and gives $7^n$; it permits pair overlaps and is weaker than pairwise disjointness. The example $A=B=\{u\},C=\varnothing$ exposes that distinction immediately.

### 12. Fixed subset and fixed cardinality are different inputs

For a fixed $I$ in an $n$-object universe, $A\cap B=I$ gives $3^{n-|I|}$. If only $|A\cap B|=j$ is specified, the count is $\binom nj3^{n-j}$. For fixed $B$, requiring $A\cup B=U$ forces every object outside $B$ into $A$, leaving $2^{|B|}$ choices inside $B$. Requiring a nonempty intersection reduces the last count to $2^{|B|}-1$.

### 13. Nonempty and proper exclude different extremes

For $n\ge1$, there are $2^n-1$ nonempty subsets, $2^n-1$ proper subsets, and $2^n-2$ subsets satisfying both. At $n=0$, all three counts are zero. The full and empty subsets coincide there, so blindly subtracting two fails. A formula with an existential witness often has this type of degenerate-domain exception.

### 14. Power-set intersection works; a union analogue generally fails

$\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B)$, because a set is a subset of both exactly when it is a subset of their intersection. Although $\mathcal P(A)\cup\mathcal P(B)\subseteq\mathcal P(A\cup B)$, equality holds precisely when $A,B$ are comparable by containment. Otherwise choose $a\in A\setminus B$ and $b\in B\setminus A$; the mixed subset $\{a,b\}$ witnesses failure. For finite $A,B$, the power-set difference has size $2^{|A|}-2^{|A\cap B|}$, not $2^{|A\setminus B|}$.

### 15. Nested union and transitivity require a brace-level audit

A union exposes members of members: $x\in\bigcup S$ exactly when some $Y\in S$ contains $x$. Transitivity is equivalent to $\bigcup S\subseteq S$ and to $S\subseteq\mathcal P(S)$. It does not imply $S=\mathcal P(S)$ or closure under every subset. Rename nested empty sets and enumerate each level before testing an inclusion. Cardinality alone cannot determine these memberships.

### 16. Product proofs must retain both coordinates

Membership in $A\times C$ requires a first coordinate in $A$ and a second in $C$. Thus $(A\setminus B)\times C=(A\times C)\setminus(B\times C)$ for every $C$, including empty $C$. Cancellation from $A\times C=B\times C$ requires $C\ne\varnothing$: select one $c\in C$ to test every first coordinate. Without it both products can be empty even when $A\ne B$. Finite product size is $|A||C|$.

### 17. Indexed operations conceal quantifier order

$x\in\bigcup_{i\in I}A_i$ means that at least one index works; $x\in\bigcap_{i\in I}A_i$ means that every index works. With an explicitly fixed universe, the empty-index union is empty and the empty-index intersection is that universe. Without a common universe, a universal set cannot be silently introduced. A claim of the form “for every object there is an index” does not entail “there is one index for every object.”

### 18. A witness-first count can overcount unequally

When a desired set needs at least one witness pair, different valid sets may have different numbers of witnesses. For the odd-pair-sum question, mixed four-element sets have three or four odd-even pairs, so a fixed divisor cannot repair a witness-first product. Count failure classes or classify by parity population instead. Always state whether a witness is part of the requested object or merely certifies it.

### 19. Symmetry needs fixed-point analysis

For an exchange-invariant ordered-pair family with count $N$ and $F$ equal pairs, the unordered count is $(N+F)/2$. Covers have one equal pair. Complementary pairs have none on a nonempty universe but one on an empty universe. A prescribed nonempty symmetric difference has no equal pairs; an empty one makes every pair equal. A family with unequal prescribed region roles may not even be preserved by exchange.

### 20. Validate a solution by a different construction

Check a state-product count with a binomial sum, an inclusion-exclusion count with a positive size partition, and an identity with an elementwise proof plus a small countermodel search for false alternatives. Enumerations of small finite universes are checks of those instances, not replacements for the general proof. For numerical data, verify every atom is nonnegative and their sum is the universe size. For a final answer, state the counted object and parameter domain explicitly.
