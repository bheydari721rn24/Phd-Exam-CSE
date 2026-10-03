## Teaching through formulas and conceptual decisions

### Solve a cardinality question by recovering disjoint atoms

For two finite sets, the disjoint pieces are the intersection, the part only in the first set, the part only in the second, and the outside. If their sizes are respectively $t,a-t,b-t,N-a-b+t$, every one must be nonnegative. Thus a proposed intersection must satisfy $\max(0,a+b-N)\le t\le\min(a,b)$. This feasibility check comes before substitution into a formula.

For three sets, start with the triple intersection, subtract it from the pair intersections, and only then obtain the single-only regions. A pair intersection includes the triple intersection unless explicitly stated otherwise. The union is

$$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.$$

Exactly one membership has size the sum of singleton sizes minus twice the sum of pair intersections plus three times the triple intersection. Exactly two memberships has size the sum of pair intersections minus three times the triple intersection. These coefficients follow by charging an object that occurs in one, two or three sets; they are not independent formulas to memorize without a region model.

### Count sets of sets by translating the constraint

If $A\subseteq S\subseteq B$ and $A\subseteq B$, each element of $B\setminus A$ is independently optional: there are $2^{|B|-|A|}$ choices. A size restriction $|S|=k$ instead gives $\binom{|B|-|A|}{k-|A|}$. If the premise $A\subseteq B$ fails, the answer is zero; negative exponents cannot repair an inconsistent constraint.

For a fixed ordered pair $(A,B)$ of subsets of an $n$-element universe, each element has four membership states. A local rule eliminates forbidden states: $A\subseteq B$ leaves three, $A\cap B=\varnothing$ leaves three, and both together leave two. A rule requiring at least one element in a particular state needs subtraction of the configurations avoiding that state. Thus a proper inclusion has $3^n-2^n$ pairs, not $3^n-1$.

### Algebraic identities are truth-table identities

Set $a=[x\in A]$, $b=[x\in B]$, $c=[x\in C]$. Union, intersection, complement and symmetric difference become OR, AND, NOT and XOR. Equality of sets means equality on all admissible membership patterns. An implication between containments restricts which patterns are admissible; cancellation of a common union or intersection is generally invalid. A single legal pattern falsifying an identity is sufficient.

## Formula and conceptual problem bank

### Question 1. Three overlapping groups

In a universe of 100 objects, $|A|=50$, $|B|=45$, $|C|=40$, pair intersections are 20, 18 and 15, and the triple intersection is 8. How many objects belong to exactly one set?

**A.** 40

**B.** 45

**C.** 53

**D.** 61

**Answer: C.**

The sum of singleton counts is 135 and the sum of pair intersections is 53. Exactly-one membership therefore counts $135-2(53)+3(8)=53$. Alternatively the exclusive regions are $50-20-18+8=20$, $45-20-15+8=18$ and $40-18-15+8=15$; their sum is 53. The union is 90 and exactly-two membership is 29, so $53+29+8=90$ checks the partition. The choices 40, 45 and 61 do not satisfy these disjoint-region equations.

### Question 2. Exactly two memberships

Use the data in Question 1. How many objects belong to exactly two sets?

**A.** 21

**B.** 29

**C.** 37

**D.** 53

**Answer: B.**

The pair-only regions are $20-8=12$, $18-8=10$ and $15-8=7$. Their sum is 29. Summing the inclusive pair intersections produces 53 and counts each triple member three times; subtracting the triple count only once produces 45, also wrong. Exactly-two means three disjoint pair-only regions, not the union of inclusive intersections.

### Question 3. Choose an intermediate set

$A\subseteq B$, $|A|=3$, $|B|=8$. How many $S$ satisfy $A\subseteq S\subseteq B$ and $|S|=5$?

**A.** 10

**B.** 20

**C.** 32

**D.** 56

**Answer: A.**

The three compulsory elements are already in $A$. Select exactly two of the five elements in $B\setminus A$, giving $\binom52=10$. The answer 32 counts all intermediate sizes. The answer 56 chooses five elements from eight without making the three elements of $A$ compulsory. Ordered selection of the optional two would overcount each resulting set twice.

### Question 4. Strict inclusion pairs

How many ordered pairs of subsets $(A,B)$ of a four-element labeled universe satisfy $A\subset B$?

**A.** 65

**B.** 80

**C.** 81

**D.** 256

**Answer: A.**

For nonstrict inclusion each element is in neither set, only $B$, or both; hence $3^4=81$. Equality allows only neither or both, giving $2^4=16$. Subtract all equal pairs, not just the empty pair: $81-16=65$. The unrestricted pair count 256 allows the forbidden only-$A$ state. Strict inclusion does not mean that either individual set is nonempty.

### Question 5. Disjoint pairs covering everything

For an $n$-element universe $U$, how many ordered pairs satisfy $A\cap B=\varnothing$ and $A\cup B=U$?

**A.** $2^n$

**B.** $3^n$

**C.** $4^n$

**D.** $2^{n-1}$

**Answer: A.**

Every element must belong to exactly one of $A$ and $B$. Its two independent choices give $2^n$. The three-choice formula allows an element in neither and fails the coverage rule. Dividing by two would forget that the pair is ordered; exchanging the two sets generally changes the counted object. For the empty universe the one pair $(\varnothing,\varnothing)$ confirms the formula.

### Question 6. Power-set intersection

If $|A|=5$, $|B|=6$ and $|A\cap B|=3$, what is $|\mathcal P(A)\cap\mathcal P(B)|$?

**A.** 3

**B.** 8

**C.** 32

**D.** 64

**Answer: B.**

A set belongs to both power sets exactly when it is a subset of both underlying sets, equivalently a subset of $A\cap B$. There are $2^3=8$ such sets. The number 3 counts shared elements, not shared subsets; 32 and 64 count the full power sets. The empty subset is one of the eight and must not be excluded.

### Question 7. Nested empty objects

What is $|\mathcal P(\mathcal P(\varnothing))|$?

**A.** 0

**B.** 1

**C.** 2

**D.** 4

**Answer: C.**

The empty set has no elements. Its power set is the singleton whose only element is the empty set. Taking a power set again produces exactly the empty subset and that singleton itself, so the size is $2^1=2$. The distinction between zero elements and one element that happens to be empty controls both stages.

### Question 8. A conditional cancellation

Which hypothesis guarantees that $A\cup C=B\cup C$ implies $A=B$?

**A.** $A\subseteq C$

**B.** $A\cap C=B\cap C=\varnothing$

**C.** $C\ne\varnothing$

**D.** $A\cap B=\varnothing$

**Answer: B.**

Outside $C$, union equality already forces equal membership in $A$ and $B$. Under the disjointness hypothesis neither set has members inside $C$, so their membership agrees everywhere. If $A\subseteq C$, different subsets of $C$ have the same union with $C$. Nonemptiness is irrelevant; even disjoint $A$ and $B$ can be hidden inside $C$. Cancellation is justified by recovering the hidden region, not by ordinary arithmetic.

### Question 9. Symmetric-difference size

$|A|=17$, $|B|=12$ and $|A\cup B|=22$. Find $|A\oplus B|$, where $\oplus$ denotes symmetric difference.

**A.** 5

**B.** 15

**C.** 22

**D.** 29

**Answer: B.**

Inclusion-exclusion first gives $|A\cap B|=17+12-22=7$. Symmetric difference discards the intersection from both sets: $17+12-2(7)=15$. The answer 5 is a difference of sizes and loses overlap information. The answer 22 is the union, which still contains the seven shared elements. The answer 29 counts each shared element twice.

### Question 10. Product difference

Which identity holds for arbitrary sets $A,B,C,D$?

**A.** $(A\times B)\setminus(C\times D)=(A\setminus C)\times(B\setminus D)$

**B.** $(A\times B)\setminus(C\times D)=((A\setminus C)\times B)\cup(A\times(B\setminus D))$

**C.** $\mathcal P(A\cup B)=\mathcal P(A)\cup\mathcal P(B)$

**D.** $A\setminus(B\cup C)=(A\setminus B)\cup(A\setminus C)$

**Answer: B.**

An ordered pair is excluded from $C\times D$ when its first coordinate is outside $C$ OR its second is outside $D$. Intersect that condition with membership in $A\times B$ to obtain option B. Option A requires both failures and loses pairs with only one failing coordinate. A subset can mix elements from $A$ and $B$, refuting C. De Morgan changes the union in option D to an intersection.

<!-- CHALLENGE-BANK -->

### Question 11. Challenge: Two strict inclusions

For a four-element universe, how many ordered triples satisfy$A\subset B\subset C$?

**A.** 65

**B.** 81

**C.** 110

**D.** 256

**Answer: C.**

For nonstrict chains, each element is in none, only$C$, in$B,C$, or in all three: four choices, hence256 triples. The failure$A=B$ removes one membership state and has$3^4=81$ triples; so does$B=C$. Their intersection has all three sets equal and$2^4=16$ triples. Subtract failures and restore their overlap:256-81-81+16=110. Properness is a global requirement that at least one element occupies each of two distinct difference states.

### Question 12. Challenge: Nonempty disjoint subsets

How many ordered pairs of disjoint nonempty subsets of a five-element universe exist?

**A.** 120

**B.** 180

**C.** 211

**D.** 243

**Answer: B.**

With disjointness, each element lies in neither set, only$A$, or only$B$, so there are$3^5=243$ pairs before nonemptiness. Pairs with$A$ empty number$2^5=32$, and the same is true for$B$. The pair with both empty was subtracted twice and must be restored. Total243-32-32+1=180. Division by two is inappropriate because the pair is ordered.

## Applicable formulas and examination notes

### 1. Intersection feasibility

For sizes $a,b$ in a universe of size $N$, require $\max(0,a+b-N)\le t\le\min(a,b)$ before using $t=|A\cap B|$. For $a=8,b=7,N=10$, the intersection is at least 5; a proposed value 4 makes the outside region negative. Bounds on an intersection are simultaneous constraints.

### 2. Exactly-one versus exactly-two

For three sets with pair-sum $s_2$ and triple size $t$, exactly-one is $s_1-2s_2+3t$ and exactly-two is $s_2-3t$. An element in all three contributes three to each sum of pairs. If a question supplies pair-only counts instead, do not subtract the triple again.

### 3. Union and outside

Compute the union by inclusion-exclusion and subtract it from the specified universe for “none.” For Question 1, the union is 90 and none is 10. Summing complements independently counts the same outside object repeatedly; the complement of a union is an intersection of complements.

### 4. Optional elements

$A\subseteq S\subseteq B$ gives $2^{|B|-|A|}$ only if $A\subseteq B$. A required size $k$ changes it to $\binom{|B|-|A|}{k-|A|}$. Interpret an out-of-range binomial choice as zero. Compulsory elements must be removed before selecting optional ones.

### 5. Local membership states

Ordered subset pairs use four states per element. Inclusion or disjointness removes one state and gives $3^n$; coverage together with disjointness leaves two and gives $2^n$. Proper inclusion subtracts $2^n$ equal pairs from $3^n$. Pair order is part of the sample object.

### 6. Power-set operators

$\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B)$ because a subset must satisfy both containments. The union counterpart fails for mixed subsets. With $A=\{1\},B=\{2\}$, the subset $\{1,2\}$ exposes that failure.

### 7. Nested size growth

If $|A|=n$, then $|\mathcal P(A)|=2^n$ and $|\mathcal P(\mathcal P(A))|=2^{2^n}$. Distinguish membership from inclusion: $\varnothing\subseteq A$ always, but $\varnothing\in A$ requires an empty object actually listed as an element.

### 8. Symmetric difference

$|A\oplus B|=|A|+|B|-2|A\cap B|$. For multiple sets, membership means an odd number of occurrences. Associativity follows from parity, while union is not parity. Two identical copies cancel under symmetric difference and do not cancel under union.

### 9. Products and empty factors

$|A\times B|=|A||B|$ for finite sets. A product is empty if either factor is empty; therefore equality of products does not let you cancel an arbitrary empty factor. Coordinate order remains significant even when the cardinalities agree.

### 10. A counterexample is a membership pattern

To refute $A\setminus(B\cup C)=(A\setminus B)\cup(A\setminus C)$, choose an element in $A\cap B$ but outside $C$. It belongs to the right side and not the left. This one pattern is a complete disproof and identifies the correct intersection replacement.

<!-- BOUNDARY-NOTES -->

### 11. Indexed and empty families

For complements relative to $U$, the union of an empty family is empty and the intersection of an empty family is $U$. For a decreasing tail $A_n=\{n,n+1,\ldots\}$, every finite intersection is a nonempty tail, but the intersection over all positive $n$ is empty. Finite-stage nonemptiness does not imply infinite-intersection nonemptiness.

### 12. Power-set containment reverses no direction

$\mathcal P(A)\subseteq\mathcal P(B)$ holds exactly when $A\subseteq B$: the singleton of each element tests the reverse implication. In contrast, $A\in\mathcal P(B)$ means $A\subseteq B$, whereas $A\subseteq\mathcal P(B)$ means every element of $A$ is itself a subset of $B$. These are different types of statements.

### 13. Set recovery and hidden regions

$A\cup C=B\cup C$ determines membership outside $C$ only; $A\cap C=B\cap C$ determines membership inside $C$ only. Both equalities together imply $A=B$. One equation alone allows differences hidden in its unobserved region.
