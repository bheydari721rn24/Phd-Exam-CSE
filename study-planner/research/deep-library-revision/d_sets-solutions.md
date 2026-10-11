# Sets: individually derived solutions

## Q1

**Correct option: 2.** Write $A\setminus B=A\cap B^c$ and $B\setminus A=B\cap A^c$. Any member of the second intersection would have to belong to $B\setminus A$ and to $(A\setminus B)\cup B^c$. The first requirement forces membership in $B$ and nonmembership in $A$. The union's two alternatives then both fail: such an object belongs neither to $A\setminus B$ nor to $B^c$. The second intersection is therefore empty. The first term is exactly $B\cap A^c=B\setminus A$, so union with the empty term leaves that set unchanged.

| Membership region | First term | Second intersection | Whole expression |
| --- | --- | --- | --- |
| Outside both | 0 | 0 | 0 |
| $A$ only | 0 | 0 | 0 |
| $B$ only | 1 | 0 | 1 |
| Both | 0 | 0 | 0 |

Option 1 includes the $A$-only region and excludes the $B$-only region. Option 3 selects the opposite exclusive region. Option 4 additionally includes the common region. For instance, $A=\{1\}$ and $B=\{1,2\}$ produce the result $\{2\}$, whereas options 1, 3 and 4 give $\{1\}$, the empty set and $\{1,2\}$. A short disjointness argument removes the complicated term without an unnecessary full distributive expansion.

## Q2

**Correct option: 3.** Expand transitivity rather than reasoning from the appearance of the symbols. If $x\in\bigcup A$, some $y\in A$ contains $x$. Thus $x\in y\in A$, and transitivity gives $x\in A$. This proves $\bigcup A\subseteq A$.

Now take an arbitrary $y\in A$. Every member $x$ of $y$ belongs to $A$, again by transitivity. Therefore $y\subseteq A$, meaning $y\in\mathcal P(A)$. Since the chosen member $y$ was arbitrary, $A\subseteq\mathcal P(A)$.

Conversely, if the union inclusion holds, any $x\in y\in A$ belongs to $\bigcup A$ and hence to $A$. If the power-set inclusion holds, any $y\in A$ is a subset of $A$, so every $x\in y$ belongs to $A$. Each condition individually characterizes transitivity, and both must hold. Options 1 and 2 omit an equivalent characterization; option 4 rejects both.

For a boundary check, the empty set is transitive and satisfies both inclusions. A useful counterexample to automatic transitivity is $A=\{\{\varnothing\}\}$: its union contains $\varnothing$, but $\varnothing\notin A$, and its sole member is not a subset of $A$. Membership, subset inclusion and power-set membership must be translated at their actual brace levels.

## Q3

**Correct option: 3.** Name the nested objects $e=\varnothing$, $s=\{e\}$ and $t=\{e,s\}$. Then $S_1=\{e,s\}$ and $S_2=\{e,s,t\}$. Taking a union gathers the members of these objects, not the objects themselves.

| Object in a family | Its members contributed to the union |
| --- | --- |
| $e$ | None |
| $s$ | $e$ |
| $t$ | $e$ and $s$ |

Consequently $\bigcup S_1=\{e\}$, a subset of $S_1$, and $\bigcup S_2=\{e,s\}=S_1$, a subset of $S_2$. Both families qualify. Neither equality $\bigcup S_i=S_i$ is required; in fact both displayed inclusions are proper.

Option 1 ignores the valid second inclusion. Option 2 ignores the valid first inclusion. Option 4 confuses the union's elements with one additional level of braces. To verify directly from the definition, inspect each member of each family: every member of those member-sets is already present as a member of the original family. This is exactly transitivity. The calculation also explains why adding $\{t\}$ without adding $t$ to a family could break the property: union would expose a missing member.

## Q4

**Correct option: 1.** Split the ten integers into five odd and five even objects. Two distinct selected elements have an odd sum exactly when their parities differ. Thus a four-element subset qualifies precisely when it contains at least one element of each parity.

There are $\binom{10}{4}=210$ unrestricted subsets. The failures are four odds, numbering $\binom54=5$, or four evens, also numbering 5. The failure classes are disjoint, so the answer is $210-5-5=200$.

A second calculation partitions by the exact number of selected odd elements:

$$\binom51\binom53+\binom52\binom52+\binom53\binom51=50+100+50=200.$$

Option 2 subtracts only one homogeneous parity class. Options 3 and 4 subtract respectively two and one subsets instead of the ten failures. Choosing a particular odd-even witness pair and then two other elements overcounts: a subset with two odds and two evens has four different witness pairs, whereas one with one odd and three evens has three. There is no uniform witness multiplicity by which to divide that naive count. Counting the property by its complement or by a disjoint parity partition avoids this issue.

## Q5

**Correct option: 1.** The given pairwise intersection counts include the triple intersection. Subtract its size once from each pair to obtain the exclusive pair regions: $10-4=6$, $9-4=5$ and $8-4=4$. Exactly-two membership is their disjoint sum, $6+5+4=15$.

| Three-set region | Population |
| --- | --- |
| $A$ only | $25-10-9+4=10$ |
| $B$ only | $22-10-8+4=8$ |
| $C$ only | $20-9-8+4=7$ |
| $A,B$ only | 6 |
| $A,C$ only | 5 |
| $B,C$ only | 4 |
| All three | 4 |
| Outside all three | $60-44=16$ |

Inclusion-exclusion gives union size $25+22+20-10-9-8+4=44$, so sixteen objects are outside. Every region population is nonnegative and the eight populations sum to sixty, checking feasibility as well as arithmetic.

Option 2 uses the raw sum 27 of pair intersections and counts each triple member three times as if it had exactly two memberships. Option 3 drops the final triple correction in the union formula, producing outside count 20. Option 4 subtracts only two copies of the triple population from the pair sum, yielding 19 and still retaining one count for each triple member. Exactly-two counting removes all three copies, while union counting restores one after the pair subtractions.

## Q6

**Correct option: 1.** The three disjoint labelled regions are $A$, $B\setminus A$ and $U\setminus B$. Each must be nonempty: these express, respectively, the nonempty smaller set and the two proper containments. Conversely, any assignment of the five labelled objects to three nonempty regions reconstructs a unique valid pair by taking $B$ to be the union of the first two regions.

Start with $3^5=243$ assignments. Excluding each of three empty-region events removes $3\cdot2^5=96$. Each intersection of two empty-region events puts all objects in the remaining region and contributes one; there are three such intersections. All three regions cannot be empty because the universe has five objects. Therefore $243-96+3=150$.

An independent size partition gives

$$\sum_{a=1}^{3}\binom5a(2^{5-a}-2)=5\cdot14+10\cdot6+10\cdot2=150.$$

After choosing $A$, select a nonempty proper part of its complement for $B\setminus A$. Option 3, 180, arises if the outside region is allowed to be empty while the first two are nonempty; it wrongly admits $B=U$. Options 2 and 4, 120 and 90, do not match the displayed nonempty-region partition. The labels matter: exchanging the first and last region changes the pair's roles, so dividing by a region-permutation factorial would count a different object.

## Q7

**Correct option: 3.** A subset belongs to both $\mathcal P(A)$ and $\mathcal P(B)$ precisely when every one of its elements belongs to both underlying sets. Hence

$$\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B).$$

There are $2^4=16$ subsets of $A$, of which $2^2=4$ are also subsets of $B$. Their difference therefore has twelve members. This subtraction operates on collections of subsets, not on the underlying objects directly.

For an explicit model, let $A=\{1,2,3,4\}$ and $B=\{1,2,5\}$. A subset of $A$ fails to be a subset of $B$ exactly when it contains 3 or 4. Choose a nonempty subset of $\{3,4\}$ in three ways and any subset of $\{1,2\}$ in four ways, giving $3\cdot4=12$.

Option 1 counts only $\mathcal P(A\setminus B)$ and wrongly excludes mixed subsets such as $\{1,3\}$; it also includes the empty subset, which is not in the requested difference. Option 2, eight, would fix one particular exclusive element as included and misses qualifying subsets using only the other exclusive element. Option 4 fails to subtract shared subsets. The correct factorization is $(2^{|A\setminus B|}-1)2^{|A\cap B|}$, not $2^{|A\setminus B|}$.

## Q8

**Correct option: 1.** Symmetric difference contains the exclusive regions and excludes the common region. Thus

$$12=11+9-2|A\cap B|,$$

giving $|A\cap B|=4$. The factor two comes from counting a common object once in each of $|A|$ and $|B|$ although symmetric difference must count it zero times.

Membership in symmetric difference is XOR. For an arbitrary object, let its membership bits in $A$ and $B$ be $a,b$. The bit in $(A\triangle B)\triangle B$ is $(a\oplus b)\oplus b=a$, because toggling twice restores a bit. Hence the entire set equals $A$ and has size eleven.

Option 2 forgets the factor two and gives an intersection size of eight. Option 3 retains the intermediate symmetric difference instead of applying the second toggle. Option 4 incorrectly returns $B$. This cancellation does not require disjointness. It does, however, require the same set $B$ in both positions; replacing one occurrence by a different set invalidates the cancellation. The two parts of the problem use different evidence: a cardinality equation for the first and an elementwise identity for the second.

## Q9

**Correct option: 1.** The union equation forces every element of $U\setminus B$ into $A$: otherwise that element belongs to neither set and the union misses it. These five objects contribute no choice. Inside $B$, at least one of the three objects must be chosen for $A$ to make the intersection nonempty. Therefore $A$ is uniquely of the form

$$A=(U\setminus B)\cup S,\qquad\varnothing\ne S\subseteq B.$$

There are $2^3-1=7$ possible sets $S$ and hence seven possible sets $A$. No multiplier is needed for the five forced objects.

Option 2 counts nonempty selections from the wrong five-object region. Option 3, 56, counts a different product of three- and five-object choices despite the fixed outside region. Option 4 uses six independent bits, although only three membership bits are free. If the intersection were required to have exactly two elements, the answer would be $\binom32=3$. If the intersection could be empty, all eight selections inside $B$ would be allowed. If disjointness were added, only $S=\varnothing$ would work, contradicting the nonempty intersection requirement and giving zero solutions.

## Q10

**Correct option: 2.** Again write $e=\varnothing$, $s=\{e\}$ and $t=\{e,s\}$. The given set is $S=\{e,s,t\}$. Union exposes $e$ from $s$ and exposes $e,s$ from $t$, so $\bigcup S=\{e,s\}$. This is a proper subset of $S$, since $t$ is absent from the union.

Every member of $S$ is a subset of $S$: $e$ has no members, $s$ contains only $e$, and $t$ contains $e,s$. Thus $S\subseteq\mathcal P(S)$. It is proper because $S$ has three members but its power set has eight. For an explicit missing member, $\{t\}$ belongs to $\mathcal P(S)$ but is not one of $e,s,t$.

Option 1 wrongly makes both inclusions equalities. Option 3 contradicts the direct union list. Option 4 contradicts the member-by-member subset check. Transitivity states that every member is a subset of the original set; it does not state that every subset of the original set is a member. The latter downward-closure condition is stronger and fails in the example at $\{t\}$. Distinguish the two directions before reading a power-set inclusion as a closure property.

## Q11

**Correct option: 2.** The four disjoint labelled regions are $A\setminus B$, $B\setminus A$, $A\cap B$ and $U\setminus(A\cup B)$. Their sizes are 2,1,1 and $6-2-1-1=2$. A pair is reconstructed uniquely from its assignment of labelled objects to these regions.

Choose the two $A$-only objects in $\binom62=15$ ways, the one $B$-only object from the remaining four in four ways, and the common object from the remaining three in three ways. The remaining two are forced outside. Thus $15\cdot4\cdot3=180$, equivalently

$$\frac{6!}{2!1!1!2!}=180.$$

Option 1, 360, misses one of the two factorial corrections for unordered elements within a size-two region. Option 3, 720, counts all element orderings without either correction. Option 4, 90, divides the correct count by an unjustified exchange of labelled roles. Equal region sizes do not make the regions interchangeable: $A$-only and outside-both encode different membership bits. Swapping $A$ and $B$ would also change the required exclusive sizes from (2,1) to (1,2), so it is not a symmetry of the stated family.

## Q12

**Correct option: 1.** An ordered pair $(a,c)$ belongs to $(A\setminus B)\times C$ exactly when $a\in A$, $a\notin B$ and $c\in C$. Membership in $(A\times C)\setminus(B\times C)$ requires $a\in A,c\in C$ and not $(a\in B\land c\in C)$. Since $c\in C$ already holds, the final condition reduces to $a\notin B$. The two sides have identical membership conditions for every ordered pair, proving equality even when $C$ is empty.

To reject option 2, take $A=\{0\}$, $B=\varnothing$ and $C=\{1\}$. Its left side contains $(0,1)$, while its right side is empty because $C\setminus C$ is empty. To reject option 3, let $C=\varnothing$ and choose unequal $A,B$: both products are empty, so product equality does not permit cancellation. To reject option 4, use the same one-object example with $B=\varnothing$; its left product is nonempty and the proposed intersection empty.

If $C$ is nonempty, product cancellation is valid: select one $c\in C$ and use pairs $(a,c)$ to prove both inclusions between $A$ and $B$. That proof explains exactly why the empty factor is the boundary, rather than treating it as a memorized exception.

## Q13

**Correct option: 2.** For each of the five labelled objects, record its membership in $A,B$ as a pair of bits. Containment forbids 10, because an object cannot be in $A$ and outside $B$. The remaining states are 00, 01 and 11. The assignment of states determines the pair uniquely, and every such assignment satisfies containment. Independent choices for the five distinct objects therefore give $3^5=243$.

One can verify the count by choosing $B$ first. If $|B|=b$, there are $\binom5b$ choices of $B$ and $2^b$ choices of its subset $A$. Thus

$$\sum_{b=0}^{5}\binom5b2^b=1+10+40+80+80+32=243.$$

The term $b=0$ is important: the pair $(\varnothing,\varnothing)$ is valid. Option 1, $5^3$, chooses a labelled object three times and does not assign a membership state to every object. Option 3, $4^5$, permits the forbidden state 10. Option 4, $2^5$, counts only equal pairs $A=B$, whose objects have states 00 or 11. There are $243-32=211$ proper-containment pairs, but proper containment was not required.

## Q14

**Correct option: 1.** With eight labelled objects, the permitted membership states for $A\subseteq B$ remain 00,01,11. For example, the first object can be outside both sets, the second in $B$ only, and the third in both; these choices impose no restriction on the fourth. A complete eight-state assignment is equivalent to one valid ordered pair. Consequently the count is $3^8=6561$.

The independent binomial calculation is

$$\sum_{b=0}^{8}\binom8b2^b=(1+2)^8=6561.$$

For a chosen $B$, containment leaves $2^{|B|}$ possibilities for $A$, not the same number for every $B$. This explains why multiplying the number of all sets $B$ by an arbitrary fixed number of subsets is invalid.

Option 2, $4^8=65536$, counts unrestricted ordered pairs and includes violations of containment. Option 3, $2^8=256$, counts equal pairs only. Option 4, 512, does not describe the three-state choices or their binomial expansion; it cannot be justified by treating the two sets as a single eight-bit selection with one extra binary choice. Equality is allowed, so subtracting 256 would incorrectly enforce proper containment.

## Q15

**Correct option: 4.** The map from a contained ordered pair to a word of length $n$ over $\{00,01,11\}$ is a bijection. Injectivity holds because the bits recover both sets. Surjectivity holds because absence of 10 guarantees that every member of $A$ is a member of $B$. Therefore there are $3^n$ pairs for every finite labelled universe, including $n=0$.

For a small check, let $U=\{u\}$. The three pairs are $(\varnothing,\varnothing)$, $(\varnothing,\{u\})$ and $(\{u\},\{u\})$. For $U=\varnothing$, there is the single empty pair, agreeing with $3^0=1$. The formula also follows from the binomial theorem:

$$\sum_{B\subseteq U}2^{|B|}=\sum_{b=0}^{n}\binom nb2^b=3^n.$$

Option 1 allows all four membership states. Option 2 restricts every object to 00 or 11 and therefore counts equality. Option 3, $n^3$, counts ordered triples of chosen objects rather than assignments to every object. Containment is an elementwise implication; a numerical condition such as $|A|\le |B|$ does not imply it. For example, $A=\{1\}$ and $B=\{2\}$ satisfy that size condition but violate containment.

## Q16

**Correct option: 3.** Proper containment removes exactly the pairs with $A=B$ from the $3^n$ contained pairs. An equal pair is determined by its common set, so there are $2^n$ equal pairs. Hence

$$\#\{(A,B):A\subsetneq B\}=3^n-2^n.$$

Equivalently, proper containment requires at least one object with state 01, in addition to excluding 10 everywhere. Excluding assignments with no 01 leaves only the two states 00,11, which is exactly the subtraction above.

Option 1 is false: on a one-object universe non-strict containment permits three pairs but proper containment only $(\varnothing,U)$. Option 2 is false: take $U=\{1,2\}$, $A=\{1\}$ and $B=U$; the smaller set is nonempty. Option 4 is false because state 10 directly contradicts containment. For $n=0$ the count is $1-1=0$, as the only two subsets coincide. Distinguish a local restriction, which forbids a state at every object, from a strictness requirement, which demands at least one witness in a particular region.

## Q17

**Correct option: 1.** The equation $A\cup B=U$ forbids state 00. Each of the five labelled objects must belong to $A$ only (10), to $B$ only (01), or to both (11). These three choices are independent, giving $3^5=243$ ordered covering pairs.

Another derivation chooses $A$. Every object outside $A$ is forced into $B$, while each object inside $A$ may or may not belong to $B$. For a chosen $A$ of size $a$, there are $2^a$ choices of $B$. Summing gives

$$\sum_{a=0}^{5}\binom5a2^a=243.$$

Option 2, 32, counts disjoint covering pairs by allowing only 10,01; disjointness is an additional restriction. Option 3, 1024, counts unrestricted pairs and includes 00. Option 4, 211, subtracts the 32 disjoint coverings and therefore counts only covering pairs with a nonempty intersection. A common object is permitted but not compulsory. Both pairs $(\varnothing,U)$ and $(U,U)$ are valid, demonstrating that neither nonemptiness of both sets nor disjointness follows from the union equation.

## Q18

**Correct option: 4.** The eight objects each have one of the states 10,01,11. Once those states are fixed, the two sets are recovered without further choices. Thus $3^8=6561$.

The number with empty intersection is $2^8=256$, because a disjoint cover allows only 10 and 01. The number with nonempty intersection is therefore

$$3^8-2^8=6561-256=6305.$$

This decomposition checks the requested count: every cover belongs to exactly one of those two classes, and $256+6305=6561$. Option 1 selects only the disjoint class. Option 2, $4^8$, admits objects in neither set and therefore fails the coverage requirement. Option 3 selects only the nonempty-intersection class. Nothing in the question chooses either class, so they must be added.

For example, assigning all eight objects to 11 produces $A=B=U$, and assigning all to 01 produces $A=\varnothing,B=U$. Both extremes are valid. The common-region size may be any integer from zero through eight, with the count for exactly $j$ common objects equal to $\binom8j2^{8-j}$; summing over $j$ again yields $3^8$.

## Q19

**Correct option: 3.** A covering ordered pair is a partition of the labelled objects into three labelled regions: $A\setminus B$, $B\setminus A$ and $A\cap B$. The regions may be empty. Conversely, each such region assignment reconstructs exactly one covering pair. Consequently the count is $3^n$.

The binomial decomposition by intersection size makes the reasoning explicit:

$$\sum_{j=0}^{n}\binom nj2^{n-j}=(1+2)^n=3^n.$$

Choose the $j$ common objects, then place each remaining object in exactly one of the two exclusive regions. Option 1 counts all four membership states, including uncovered objects. Option 2 excludes the $2^n$ disjoint covers, although the problem permits them. Option 4 counts only those disjoint covers. At $n=1$ there are three possibilities, of which two are disjoint and one has a common object. At $n=0$ the unique pair is $(\varnothing,\varnothing)$; the general formula still gives one. The labels $A$ and $B$ make ordered pairs the requested objects, so exchanging the sets is generally a different answer.

## Q20

**Correct option: 2.** Adding $A\cap B=\varnothing$ removes state 11 from the covering states 10,01,11. The remaining two states assign each labelled object to exactly one of the sets. Hence there are $2^n$ ordered pairs.

Option 1 incorrectly permits 00, which would leave an object outside the union. Option 3 confuses covering with disjoint covering: $A=B=U$ covers any nonempty universe but is not disjoint. Option 4 cannot obtain unordered coverings by always dividing $3^n$ by two, because the exchange map has a fixed point. Its only fixed covering pair is $(U,U)$. All other covering pairs come in distinct exchanged pairs, so the unordered count is

$$1+\frac{3^n-1}{2}=\frac{3^n+1}{2}.$$

For a one-object universe the three ordered coverings produce two unordered coverings, not one and a half. For disjoint coverings of a nonempty universe, there is no fixed point and division by two is valid, giving $2^{n-1}$. On the empty universe there is one fixed empty pair, so that special case must again be treated directly. Determine the family and its exchange-fixed objects before applying a symmetry divisor.

## Q21

**Correct option: 3.** Containment $A\subseteq B\subseteq C$ permits only the following membership triples:

| State in $A,B,C$ | Region |
|---|---|
| 000 | Outside $C$ |
| 001 | $C\setminus B$ |
| 011 | $B\setminus A$ |
| 111 | $A$ |

For instance, 101 is forbidden because membership in $A$ would require membership in $B$. Every assignment of the five labelled objects to these four regions reconstructs a unique nested triple. Thus $4^5=1024$.

Option 1, $3^5$, omits one permitted region. Option 2, $2^5$, counts triples with all three sets equal, permitting only 000 and 111. Option 4, $8^5$, permits all eight triples of bits and ignores both containment implications. Equalities and empty sets are allowed; the valid triple $(\varnothing,\varnothing,\varnothing)$ and the valid triple $(U,U,U)$ must not be excluded. If both containments were proper, the regions 001 and 011 would have to be nonempty and the count would instead be $4^5-2\cdot3^5+2^5=570$.

## Q22

**Correct option: 2.** Each of the eight labelled objects has four possible entry positions in the chain: it enters at $A$, at $B$ only onward, at $C$ only, or never. Their membership triples are respectively 111,011,001,000. The entry choices are independent, so the answer is $4^8=65536$.

Choosing the largest set first gives a separate verification. For a specified $C$ of size $c$, each of its objects has one of three states in the contained pair $A\subseteq B\subseteq C$, while objects outside $C$ are forced outside both smaller sets. Hence

$$\sum_{c=0}^{8}\binom8c3^c=(1+3)^8=65536.$$

Option 1, 256, counts the equal triples only. Option 3, $8^8=16777216$, counts unrestricted triples, including 100 and 010, which violate the chain. Option 4, $3^8=6561$, counts a three-region restriction such as requiring $C=U$; the question leaves the outside-$C$ region available. This distinction also explains why a nested triple is not counted by multiplying the unrestricted numbers of choices for the three sets.

## Q23

**Correct option: 1.** Under the chain condition, the membership bits of any object are nondecreasing when read from $A$ to $C$. The only length-three nondecreasing binary words are 000,001,011,111. Thus the complete triple is equivalent to a length-$n$ word over four states and its count is $4^n$.

On a one-object universe these words give exactly four nested triples; on an empty universe there is exactly one. Both checks agree with the formula. An alternative expression is

$$\sum_{c=0}^{n}\binom nc\sum_{b=0}^{c}\binom cb2^b=\sum_{c=0}^{n}\binom nc3^c=4^n.$$

Here the inner sum first selects $B$ within a fixed $C$, then selects $A$ within $B$. Option 2 permits all eight local states. Option 3 incorrectly leaves only three states, as though one of the four regions were forbidden. Option 4 retains only the two equal-membership states. For a chain of $k$ labelled sets the same argument gives $(k+1)^n$, because a membership word can switch from zero to one at just one entry position, or remain zero throughout.

## Q24

**Correct option: 4.** In a chain of $k$ sets, an object's membership can begin at any of the $k$ sets, or at none of them. Once the object enters, it belongs to all later sets. There are therefore $k+1$ states, not $2^k$ unrestricted bit patterns.

Option 1 ignores the forbidden patterns of a three-set chain; for example 100 violates $A\subseteq B$. Option 2 is refuted by $A=\varnothing$, $B=\{1\}$, $C=\{1,2\}$, a valid chain whose sets differ. Option 3 is refuted by comparing a one-set chain, with two entry states, to a two-set chain, with three states rather than four.

Strictness is a global witness condition. For $A\subsetneq B\subsetneq C$, one must use state 011 at least once and state 001 at least once. Inclusion-exclusion gives

$$4^n-2\cdot3^n+2^n.$$

The two subtracted terms correspond to a missing first or second difference region; their intersection leaves only 000 and 111 and is restored once. It is wrong to forbid 000 or 111, or to require each object to witness strictness. For $n=1$ the count is zero because two distinct nonempty difference regions cannot be formed from one object.

## Q25

**Correct option: 1.** The equation $A\triangle B=D$ determines $B$ uniquely once $A$ is selected:

$$B=A\triangle D.$$

Indeed, XORing both sides with $A$ cancels $A\triangle A=\varnothing$. Conversely, substituting this expression for $B$ gives $A\triangle(A\triangle D)=D$. Thus every one of the $2^5=32$ choices of $A$ produces exactly one valid ordered pair.

For an object outside $D$, the two membership bits must agree, giving choices 00 or 11. For an object in $D$, they must differ, giving choices 01 or 10. There are two choices in either case, so the size of $D$ does not change the count. Option 2 uses three states per object as though there were a containment or union restriction. Option 3 uses all four states and ignores the fixed XOR result. Option 4, 16, would count unordered pairs when $D$ is nonempty; the question asks for ordered pairs. If $D=\varnothing$, every solution has $A=B$ and even the unordered count remains 32.

## Q26

**Correct option: 4.** There are $2^8=256$ choices for $A$. For each, the only possible second set is $A\triangle D$, so the total is 256, regardless of how many of the eight objects are in the fixed set $D$.

For a concrete reconstruction, suppose $D=\{1,3\}$ and $A=\{1,2\}$ within an eight-object universe. Then $B=\{2,3\}$: object 1 is removed, object 3 added, and the membership of all other objects retained. The symmetric difference of these two sets is exactly $D$.

Option 1, $3^8=6561$, assigns an irrelevant three-state restriction. Option 2, $4^8=65536$, chooses the two sets independently even though one determines the other. Option 3, 128, identifies exchanged ordered pairs, which is not requested. If $D$ is nonempty, exchanging the sets pairs up all solutions without a fixed point, so 128 would be the corresponding unordered count. If $D$ is empty, exchange fixes all 256 equal pairs; division by two is then invalid. The distinction between a prescribed set $D$ and an unspecified XOR result is essential to the bijection.

## Q27

**Correct option: 3.** The function $A\mapsto(A,A\triangle D)$ maps the $2^n$ subsets of $U$ bijectively to the required ordered pairs. It is injective because its first coordinate is $A$. It is surjective because cancellation in $A\triangle B=D$ forces the second coordinate to be $A\triangle D$.

The local alternatives are explicit:

| Membership in $D$ | Allowed membership in $A,B$ |
|---|---|
| 0 | 00 or 11 |
| 1 | 01 or 10 |

Two choices per labelled object give $2^n$. Option 1 makes both bits free and permits the wrong XOR result. Option 2 applies an exchange divisor, although pairs are ordered; it also fails for an empty universe. Option 4 gives a third local choice that violates either equality or inequality of the bits. At $n=0$ the only possible $D$ is empty and the unique solution is the empty pair, agreeing with $2^0=1$. No assumption that $D$ is nonempty is needed for the ordered count.

## Q28

**Correct option: 2.** Define $T_D(A)=A\triangle D$. Applying it twice gives

$$T_D(T_D(A))=(A\triangle D)\triangle D=A.$$

Thus $T_D$ is an involution. It is injective because applying it again to an equality of outputs recovers equality of inputs. It is surjective because $T_D(T_D(B))=B$ supplies an input for every target $B$.

Option 1 is false: both empty and full $D$ give two choices per object, so the ordered-pair count stays $2^n$. Option 3 confuses an involution with an idempotent operation. Take $U=D=\{1\}$ and $A=\varnothing$. Then $T_D(A)=\{1\}$, whereas $T_D(T_D(A))=\varnothing$; the two outputs differ. The identity $T_D^2=T_D$ holds for every input only when $D=\varnothing$. Option 4 is false because the second set is uniquely determined by the first.

A fixed point would satisfy $A\triangle D=A$ and therefore $D=\varnothing$. Hence nonempty $D$ has no fixed points and the unordered solution count is $2^{n-1}$, while empty $D$ fixes every subset and gives $2^n$ unordered equal pairs. These are different counting problems from the ordered one.

## Q29

**Correct option: 1.** A five-object universe has $2^5=32$ subsets. Remove the empty set, which violates nonemptiness, and the full universe, which violates properness. They are distinct, so there are $32-2=30$ eligible subsets.

Grouping by size verifies the subtraction:

$$\binom51+\binom52+\binom53+\binom54=5+10+10+5=30.$$

Option 2, 31, removes only one extreme and therefore describes either all nonempty subsets or all proper subsets, rather than both conditions. Option 3, 16, is the number of subsets with a specified object included, or half the complete power set; neither restriction is the question's condition. Option 4, five, counts singleton subsets only and omits valid larger subsets such as $\{1,2\}$.

The conditions are logically independent on a nonempty universe: the empty set is proper but not nonempty, and the full universe is nonempty but not proper. Complementation exchanges the nonempty proper subsets in distinct pairs. Since $U$ is nonempty, no subset equals its own complement, so there are fifteen complementary pairs. That is a count of pairs of subsets, not the thirty individual subsets requested here.

## Q30

**Correct option: 4.** There are $2^8=256$ subsets, of which exactly two fail the combined condition: $\varnothing$ and $U$. Thus the answer is 254.

The explicit size expansion is

$$8+28+56+70+56+28+8=254.$$

These terms count subsets of sizes one through seven. This provides a check that subsets of all intermediate sizes, rather than just singletons or half-sized subsets, are included. Option 1, 255, permits one forbidden extreme. Option 2, 128, imposes an unrelated fixed-object membership condition or counts complementary pairs before excluding the boundary pair; neither gives the number of individual eligible subsets. Option 3, eight, counts only size-one subsets.

If one instead asked for eligible complementary pairs, the answer would be $254/2=127$. The full power set has 128 such pairs; the single pair $\{\varnothing,U\}$ is removed. This explains where a symmetry divisor can be used and why it must be applied to the correct family. The universe has eight objects, so the two excluded extremes are distinct; the empty-universe case needs a separate argument.

## Q31

**Correct option: 3.** For $n\ge1$, the power set has $2^n$ members and the empty and full subsets are distinct. Deleting both gives $2^n-2$.

The same formula follows by summing allowed sizes:

$$\sum_{j=1}^{n-1}\binom nj=2^n-\binom n0-\binom nn=2^n-2.$$

For $n=1$ the sum has no terms and the result is zero, as a singleton universe has no nonempty proper subset. For $n=2$ the two singleton subsets are precisely the two possibilities. Option 1, $2^{n-1}$, generally counts subsets containing a fixed object, rather than those excluding both extremes. Option 2, $n$, counts singletons; its occasional agreement at a small value does not prove a general formula. Option 4 removes only one extreme.

The hypothesis $n\ge1$ must accompany the formula. At $n=0$ the empty subset and full subset are the same set, so subtracting two counts the sole member twice. The correct direct count there is zero, not $2^0-2=-1$. Always check whether the objects removed by a subtraction are distinct throughout its stated parameter range.

## Q32

**Correct option: 2.** On the empty universe the only subset is $\varnothing=U$. It is neither nonempty nor proper, so the desired family is empty. The usual subtraction $2^n-2$ is not valid at $n=0$, because its two excluded subsets coincide.

Option 1 is false on every nonempty universe: $U$ itself is nonempty but not a proper subset of itself. Option 3 is false because the empty set is a subset of every set: there is no element of it that can violate containment. Option 4 is false on a nonempty universe because $\varnothing\subsetneq U$ although the smaller set is empty.

The distinction can be summarized precisely:

| Universe size | Nonempty subsets | Proper subsets | Nonempty proper subsets |
|---|---:|---:|---:|
| $n=0$ | 0 | 0 | 0 |
| $n\ge1$ | $2^n-1$ | $2^n-1$ | $2^n-2$ |

The two middle families have the same size but are different families on a nonempty universe. Their intersection is the last family. Equal counts do not justify replacing one semantic condition by another.

## Q33

**Correct option: 2.** Pairwise disjointness permits each object to occur in at most one of $A,B,C$. The possible states are 000,100,010,001: outside all sets, in $A$ only, in $B$ only, or in $C$ only. Coverage is not required. Assigning one of these four states to each of the five labelled objects gives $4^5=1024$ triples.

Option 1, $2^5$, allows only two categories and omits eligible triples. Option 3, $3^5$, omits the outside-all category and therefore counts disjoint triples that cover $U$. Option 4, $8^5$, permits all three bits independently and includes overlapping objects. In particular, 110 violates $A\cap B=\varnothing$.

The triple $(\varnothing,\varnothing,\varnothing)$ is valid because the sets need not cover the universe or be nonempty. The triple $A=B=\{1\},C=\varnothing$ is invalid despite its empty triple intersection. It violates pairwise disjointness in $A\cap B$. This counterexample prevents a common error: forbidding only state 111 leaves seven states, whereas pairwise disjointness leaves four.

## Q34

**Correct option: 1.** Each of the eight objects may be assigned to $A$ only, $B$ only, $C$ only, or none. Pairwise disjointness is satisfied by every such assignment, and a valid triple yields exactly that assignment. Thus $4^8=65536$.

Classifying by the number $j$ of objects assigned to at least one set gives an independent expansion:

$$\sum_{j=0}^{8}\binom8j3^j=(1+3)^8=65536.$$

Choose the $j$ used objects, then place each in one of three labelled sets; all remaining objects are outside. Option 2, 6561, requires all objects to be used and counts only covers. Option 3, 16777216, is $8^8$, the count of unrestricted triples with overlaps permitted. Option 4, 256, has only two choices per object and does not encode the four allowed regions.

The region labels matter. For example, moving object 1 from $A$ to $B$ changes the ordered triple. Dividing by $3!$ would not answer this question; moreover, empty or equal sets can create exchange-fixed configurations, so even an unordered version would need a careful orbit count. No such identification is part of the stated family.

## Q35

**Correct option: 4.** There is a bijection between pairwise-disjoint ordered triples and assignments of each universe object to four labelled regions: $A$, $B$, $C$ and $U\setminus(A\cup B\cup C)$. Hence the general count is $4^n$.

For $n=1$ the four triples put the sole object in one of the three sets or nowhere. For $n=0$ there is the unique all-empty triple, agreeing with $4^0=1$. Option 1, $3^n$, additionally requires coverage. Option 2, $8^n$, allows all possible membership patterns and ignores disjointness. Option 3, $2^n$, admits only two categories, rather than four.

If all three sets were also required to be nonempty, the count for $n\ge1$ would be

$$4^n-3\cdot3^n+3\cdot2^n-1.$$

There are three empty-set events, each leaving three local categories; their three pairwise intersections leave two; their triple intersection assigns every object outside all sets and contributes one. This additional restriction is absent from the present question. At $n=0$, the same expression is zero; all empty-set events coincide, but full inclusion-exclusion still handles their overlaps correctly.

## Q36

**Correct option: 3.** Coverage removes the 000 state from the four pairwise-disjoint states. Each object must then be assigned to exactly one of $A,B,C$, giving $3^n$ ordered triples.

Option 1 is refuted by $A=B=\{1\},C=\varnothing$: the triple intersection is empty but $A\cap B$ is not. Option 2 is refuted by taking $A=U$ and $B=C=\varnothing$; a disjoint cover can contain empty sets. Option 4 is refuted on a nonempty universe by the all-empty triple, which is pairwise disjoint but covers nothing.

Requiring all three covering sets to be nonempty is yet another condition. For $n\ge1$, inclusion-exclusion gives

$$3^n-3\cdot2^n+3.$$

At $n=1$ and $n=2$ the value is zero, since three nonempty disjoint sets require at least three objects. At $n=3$ it gives six labelled singleton allocations. At $n=0$ the count is directly zero; the final $+3$ formula assumed the intersection of all three empty-set events was impossible and is therefore not applicable there. State precisely which region is forbidden and which regions are required to have witnesses.

## Q37

**Correct option: 3.** The universe has ten objects, and a particular five-object set $I$ is prescribed as the intersection. Every object of $I$ is forced into both $A$ and $B$, giving state 11 with no choice. Each of the other five objects may have state 00,10 or 01, but not 11 because that would enlarge the intersection. Hence $3^5=243$.

Option 1, 32, imposes an extra coverage requirement on the five outside objects by allowing only 10 and 01. Option 2, 59049, is $3^{10}$ and wrongly grants free states to the five forced intersection objects. Option 4, 1024, allows state 11 outside $I$ and therefore admits intersections larger than the fixed set.

If only the *size* of the intersection were prescribed, one would also choose its members, giving $\binom{10}{5}3^5=252\cdot243=61236$. Here the set $I$ is already fixed, so that factor must not be added. Fixed objects contribute one choice, not a count of one for each object multiplied by a separate binomial factor. The distinction between a fixed subset and a subset of fixed size is central to this problem.

## Q38

**Correct option: 2.** The universe has sixteen objects; the eight objects of its prescribed intersection are forced into both sets. On the remaining eight, the three states 00,10,01 independently preserve exactly that intersection. Thus the count is $3^8=6561$.

For a concrete local check with two objects, let $U=\{u,v\}$ and $I=\{u\}$. The three permitted ordered pairs are $(\{u\},\{u\})$, $(\{u,v\},\{u\})$ and $(\{u\},\{u,v\})$. The forbidden fourth pair puts $v$ in both sets and changes the intersection to $U$. The eight-object free-region calculation repeats exactly this three-choice structure.

Option 1, 43046721, is $3^{16}$ and counts as though all sixteen objects were free. Option 3, $4^8=65536$, permits outside objects in both sets. Option 4, $2^8=256$, additionally forces every outside object to appear in the union. Since the union is unrestricted, outside-both state 00 must remain available. The prescribed intersection itself contributes no independent selection factor and no exponent beyond the outside-region size.

## Q39

**Correct option: 1.** There are $2n$ universe objects, of which the prescribed $n$ members of $I$ must have state 11. The other $n$ objects have states 00,10,01. The resulting bijection with three-state words of length $n$ proves the count $3^n$.

More generally, for a fixed intersection $I$ in an $m$-object universe,

$$\#\{(A,B):A\cap B=I\}=3^{m-|I|}.$$

Option 2 leaves the outside bits unrestricted and can produce additional common objects. Option 3 removes the outside-both state, adding the condition $A\cup B=U$. Option 4 counts the forced intersection objects as though they too had three choices. At $n=0$ there is just the empty pair; at $n=1$ the three pairs listed in the preceding solution verify the formula.

If the intersection were unspecified but required to have size $n$, its $n$ members could first be chosen in $\binom{2n}{n}$ ways. That variant gives $\binom{2n}{n}3^n$. The written word “fixed” determines whether this factor is present. A correct counting solution must identify which data are given before deciding which objects to choose.

## Q40

**Correct option: 4.** If $x\in I=A\cap B$, then by the definition of intersection both $x\in A$ and $x\in B$. Thus inside-$I$ objects are forced into state 11. Conversely, an object outside $I$ cannot be in both sets, leaving precisely 00,10,01.

Option 1 violates the intersection equality by permitting an inside object in only one set. On $I=\{u\}$, taking $A=\{u\}$ and $B=\varnothing$ demonstrates the failure. Option 2 wrongly forces all outside objects into neither set; with $U=\{u,v\}$ and $I=\{u\}$, the pair $(\{u,v\},\{u\})$ is a counterexample. Option 3 wrongly makes the pair unique: that same pair and $(\{u\},\{u\})$ have the same fixed intersection.

Even prescribing the intersection's size does not determine its members. On a two-object universe, either singleton can be the intersection, and each has three valid ordered pairs, giving six possibilities. A pointwise forced region and a numerical size constraint provide different information. Record the inside and outside regions separately before multiplying counts.

## Q41

**Correct option: 3.** The conjunction of empty intersection and full union says that every object belongs to exactly one of the two sets. Thus $B=U\setminus A$. Each of the $2^5=32$ subsets $A$ determines one valid $B$, giving 32 ordered pairs.

Option 1, 1024, counts all unrestricted pairs. Option 2, 31, removes a boundary choice of $A$ without permission; both $(\varnothing,U)$ and $(U,\varnothing)$ satisfy the requirements. Option 4, 243, counts three local states and enforces only one of the two required conditions. Empty intersection alone allows 00,10,01; full union alone allows 10,01,11. Their conjunction leaves just 10 and 01.

The count can also be expanded by the size of $A$:

$$\sum_{a=0}^{5}\binom5a=32.$$

There is no extra factor for choosing $B$, because it is the prescribed complement of the selected $A$. If both sets had to be nonempty, the two displayed boundary pairs would be removed and the answer would be 30. If pairs were unordered, exchange would halve this nonempty-universe count to sixteen. Neither additional instruction occurs here.

## Q42

**Correct option: 2.** Choose any of the $2^8=256$ subsets for $A$ and set $B=U\setminus A$. This construction satisfies the two equations and exhausts all solutions, so the answer is 256.

For example, if $A$ consists of the first three objects, the remaining five must form $B$. The second set has no freedom once the first is fixed. Grouping by $|A|$ gives

$$\sum_{a=0}^{8}\binom8a=256.$$

Option 1, 255, excludes one of the allowed extreme choices. Option 3, 6561, uses three states per object as though only coverage or only disjointness were required. Option 4, 65536, uses four states and omits both restrictions. The pair with empty $A$ and full $B$ is valid, as is its exchange; they are distinct because the universe is nonempty.

Every complementary pair in this universe has distinct coordinates. Identifying exchanges would therefore give 128 unordered pairs. Requiring both coordinates nonempty would give 254 ordered pairs. These nearby counts belong to different mathematical families and should not be substituted for the stated ordered complementary-pair count.

## Q43

**Correct option: 1.** Every subset $A$ has exactly one complementary partner $U\setminus A$. The map $A\mapsto(A,U\setminus A)$ is injective through its first coordinate and surjective because the two given equations force complementary membership at every object. Thus the count is $2^n$.

Option 2 retains three states and counts either disjoint pairs without coverage or covering pairs without disjointness. Option 3 counts unrestricted pairs. Option 4 deletes one permissible boundary pair without an additional condition. For $n=1$ the valid pairs are $(\varnothing,U)$ and $(U,\varnothing)$. For $n=0$ they coincide in the single pair $(\varnothing,\varnothing)$, agreeing with $2^0=1$.

The nonempty-universe unordered count is $2^{n-1}$ because exchange has no fixed point: $A=U\setminus A$ would require any universe object to be simultaneously in and outside $A$. At $n=0$ exchange does fix the unique empty pair, so the unordered count is one. Complementation depends on the specified universe; changing the universe changes the partner and can invalidate an identity written without that context.

## Q44

**Correct option: 4.** The union condition rules out state 00, while the intersection condition rules out state 11. Both are needed to leave exactly the complementary states 10 and 01.

Option 1 is false: on $U=\{u\}$ the pair $(\varnothing,\varnothing)$ is disjoint but not complementary, because it fails coverage. Option 2 is false: $(U,U)$ covers this universe but is not complementary, because its intersection is nonempty. Option 3 is false on the empty universe: the complement of its empty subset is the same empty subset. A no-fixed-point claim about complementation therefore requires a nonempty universe.

One can check the requirements separately before combining them:

| Requirement | Allowed states | Ordered-pair count |
|---|---|---|
| Disjointness only | 00,10,01 | $3^n$ |
| Coverage only | 10,01,11 | $3^n$ |
| Both | 10,01 | $2^n$ |
| Neither | 00,10,01,11 | $4^n$ |

Two different conditions can have equal counts without describing the same pairs. The membership-state table explains the semantic difference and prevents interpreting an exponent solely from its numerical value.

## Q45

**Correct option: 3.** The four regions of a nested triple are $A$, $B\setminus A$, $C\setminus B$ and $U\setminus C$. Both proper containments require the middle two regions to be nonempty; the first and last may be empty. Begin with $4^4=256$ assignments of the four labelled objects to these regions.

If $B\setminus A$ is empty, there are $3^4=81$ assignments. The same count applies when $C\setminus B$ is empty. If both are empty, only $A$ and outside-$C$ remain, giving $2^4=16$. Inclusion-exclusion therefore yields

$$256-81-81+16=110.$$

For an independent positive enumeration, choose the positive sizes $b,c$ of the two required difference regions. Choose their members in $\binom4b\binom{4-b}{c}$ ways and assign the remaining objects to the two optional regions in $2^{4-b-c}$ ways. The contributions for $(b,c)=(1,1),(1,2),(2,1),(1,3),(3,1),(2,2)$ are respectively 48,24,24,4,4,6, summing to 110.

Option 1, 65, equals $81-16$ and counts a different three-state family with one required witness. Option 2, 81, omits one region entirely instead of requiring both difference regions to be used. Option 4 permits equality at either containment. For a valid boundary example, take $A=\varnothing,B=\{1\},C=\{1,2\}$. Proper containment does not make $A$ nonempty or $C$ equal to the universe.

## Q46

**Correct option: 2.** Disjointness permits three regions: $A$, $B$ and outside both. Nonemptiness requires the first two to be used. There are $3^5=243$ unrestricted three-region assignments. Excluding $A=\varnothing$ removes $2^5=32$, and excluding $B=\varnothing$ removes another 32. The all-outside assignment was removed twice, so restore it once:

$$243-32-32+1=180.$$

Choosing $A$ first gives a second derivation:

$$\sum_{a=1}^{4}\binom5a(2^{5-a}-1)=5\cdot15+10\cdot7+10\cdot3+5\cdot1=180.$$

For each nonempty $A$, the partner $B$ is a nonempty subset of the complement. Size five is excluded because then no nonempty $B$ remains. Coverage is not required, so unused objects are permitted.

Option 4, 243, permits empty coordinates. Option 3, 211, removes only one empty-coordinate event and leaves pairs whose other coordinate is empty. Option 1, 120, disagrees with the exhaustive size partition displayed above; no condition in the question discards any of its terms. Dividing by two would yield ninety unordered pairs, since disjoint nonempty sets cannot coincide. The required pair is ordered, so its two labelled roles must remain distinct.
