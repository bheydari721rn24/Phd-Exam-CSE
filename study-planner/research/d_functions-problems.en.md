Problems marked **course-derived** are independently worded from the identified exercise family; numerical adaptations are stated where used. **Original** problems were designed for this chapter. Earlier proofs remain available, but the solutions here spell out the reasoning needed for the particular question.

### Problem 1. Interval endpoints and infinite set operations

**Course-derived: Oxford 2.1.** Decide whether the following hold: ${0,1}⊆(0,1)$; ${0,1}⊆[0,1]$; $(0,1)⊆[0,1)$; $(0,1)⊆ℚ$; the union of $(0,(n−1)/n)$ for positive integers $n$ equals $(0,1)$; and the intersection of $(−1/n,(n+1)/n)$ equals $(0,1)$.

**Solution.** The first assertion is false because neither endpoint belongs to the open interval. The second and third are true by their endpoint inequalities. The fourth is false: $√2/2$ is an irrational element strictly between zero and one. For the union, every member lies between zero and one. Conversely, if $0<x<1$, choose an integer $n>1/(1−x)$; then $x<1−1/n$, so $x$ lies in that member. The union is therefore correct. For the intersection, every $x∈[0,1]$ satisfies all the strict bounds, including both endpoints. If $x<0$, choose $n>1/(−x)$ to violate the lower bound; if $x>1$, choose $n>1/(x−1)$ to violate the upper bound. The intersection is $[0,1]$, not $(0,1)$. Strict inequalities inside each member do not force exclusion of limiting endpoints from an infinite intersection.

### Problem 2. Two opposite set differences cannot overlap

**Course-derived: Oxford 2.2.** Prove $(A∖B)∩(B∖A)=∅$.

**Solution.** Assume an element $x$ belongs to the intersection. Membership in the first difference says $x∈A$ and $x∉B$. Membership in the second says $x∈B$ and $x∉A$. In particular both $x∈B$ and $x∉B$ hold, a contradiction. Thus there is no member. Notice that the argument does not assume any special relation between $A$ and $B$, and also works if either is empty. This proof is a model for expanding definitions before guessing a set identity.

### Problem 3. Reciprocal rules and missing domain values

**Course-derived: Oxford 2.3.** Diagnose $f:ℝ→ℝ$ prescribed by $f(x)=1/x$, then repair it and find an inverse.

**Solution.** At zero there is no real value satisfying the prescription; the total-function existence axiom fails. Restrict the domain to $ℝ∖{0}$ and corestrict the codomain to the same set. The reciprocal of a nonzero real is nonzero, so the revised rule is valid. If $1/u=1/v$, multiplication by the nonzero product $uv$ gives $u=v$. For any nonzero target $y$, the nonzero input $1/y$ maps to it. Thus the repaired map is a bijection and its own inverse, since $1/(1/x)=x$. Merely changing the codomain would not repair the missing value at zero.

### Problem 4. Four real-function classifications

**Course-derived: Oxford 2.4.** Classify the rules $e^{−x}:ℝ→ℝ$, $e^{−x^2}:ℝ→(0,∞)$, $cos(x):ℝ→[−1,1]$, and the real endofunction sending a nonzero input to its reciprocal and zero to zero.

**Solution.** The first is strictly decreasing, hence injective. Its image is $(0,∞)$, so it misses zero and negative targets and is not onto the declared real codomain. Corestricting to positive targets gives inverse $y↦−ln(y)$. The second has image $(0,1]$: exponent $−x^2$ is nonpositive, and every value in this interval has an input $√{−ln(y)}$. The inputs $1$ and $−1$ collide, and target $2$ is missed, so it is neither property. Cosine is onto $[−1,1]$ because the restriction to $[0,π]$ takes each such value; it is not injective because $cos(0)=cos(2π)=1$. The last rule is an involution: zero stays zero, and every nonzero input is reciprocated twice. Both compositions with itself are the identity, so it is a bijection with itself as inverse. Handling the exceptional input separately prevents an invalid reciprocal calculation at zero.

### Problem 5. Constant maps including an empty domain

**Course-derived: Oxford 2.5.** For $c:A→ℕ$ defined by $c(a)=0$, characterize injectivity and surjectivity.

**Solution.** If $A$ contains two distinct elements, both have output zero, giving a collision. If $A$ has at most one element, no distinct pair exists, so the injection statement is true. Thus injectivity holds exactly for an empty or singleton domain. The target $1$ is missed regardless of $A$, so the map is never onto $ℕ$. If the declared target were instead ${0}$, onto-ness would hold exactly when $A$ is nonempty. This contrast isolates how the same assignment depends on its declared target.

### Problem 6. Powers and the zero-exponent exception

**Course-derived: Oxford 2.6, with the convention made explicit.** Classify $x↦x^k$ as a real endofunction for positive integer $k$.

**Solution.** For odd $k$, the rule is strictly increasing on all reals. Every real target has a unique real odd root, so the function is bijective. For even positive $k$, $1$ and $−1$ collide and no negative target is attained; its image is $[0,∞)$ and it is neither injective nor onto $ℝ$. If the exponent is zero and the rule is defined as the constant polynomial one, it is neither property on $ℝ$. If one instead treats numerical $0^0$ as undefined, the rule fails to define a total real-domain function at zero. State the convention before extending the odd/even classification to nonpositive exponents. Negative integer exponents require removing zero from the domain.

### Problem 7. Affine and cubic inverse algebra

**Course-derived: Oxford 2.8; original full derivation.** Let $f(x)=3x+1$ and $g(x)=(x−1)^3$, both real endofunctions. Find their composite and all relevant inverses.

**Solution.** Substitution gives $(g∘f)(x)=(3x+1−1)^3=27x^3$. Solving $y=3x+1$ gives $x=(y−1)/3$, which is a real input for every real $y$ and satisfies both inverse identities. Solving $y=(x−1)^3$ gives $x=1+∛y$, using the unique real cube root. The composite inverse is $y↦∛y/3$, since $27(∛y/3)^3=y$ and $∛(27x^3)/3=x$. Finally $(f^{-1}∘g^{-1})(y)=((1+∛y)−1)/3=∛y/3$. The reversed order $g^{-1}∘f^{-1}$ produces a different formula and is not the inverse of this composite.

### Problem 8. Fourteen proposed function types

**Course-derived: Stanford PS3 Problem 6.** Classify each declaration below, using $ℕ={0,1,…}$.

**Solution.** First check validity; only then test collisions and missing targets. Each row provides the necessary witness or argument.

| Declaration | Classification and complete reason |
|---|---|
| Square from $ℕ$ to $ℕ$ | It is injective because nonnegative equal squares have equal roots. It misses 2 and is not onto. |
| Square from $ℤ$ to $ℕ$ | It is a valid function but neither property: $1$ and $−1$ collide, and 2 is missed. |
| Square from $ℕ$ to $ℤ$ | It is injective, but negative integers are missed. |
| Square from $ℤ$ to $ℤ$ | It is neither property: signs collide and negative targets are missed. |
| Square from $ℝ$ to $ℕ$ | It is invalid, since the real input $1/2$ has output $1/4$, outside $ℕ$. |
| Square from $ℕ$ to $ℝ$ | It is injective but misses negative real values and many positive ones. |
| Principal square root from $ℕ$ to $ℕ$ | It is invalid, because input 2 has an irrational output. |
| Principal square root from $ℝ$ to $ℝ$ | It is invalid as a real-valued rule, because negative inputs have no real square root. |
| Principal square root from $ℝ$ to $[0,∞)$ | It is invalid for the same negative-input reason; changing the target does not repair the domain. |
| Principal square root from $[0,∞)$ to $[0,∞)$ | It is bijective: equality of roots gives equality of squares, and target $y≥0$ has input $y^2$. |
| Principal square root from $[0,∞)$ to $ℝ$ | It is injective but misses every negative target. |
| Any injection from $ℕ$ to $𝒫(ℕ)$ | It is not onto by Cantor's theorem, proved in the lesson; injectivity alone cannot reverse that cardinal comparison. |
| Any onto map from a three-element set to a two-element set | It is onto but cannot be injective, since three distinct inputs cannot occupy two distinct targets. |
| Any injection between two three-element sets | It is bijective: three distinct occupied targets fill the whole three-element codomain. |

### Problem 9. Multiple left inverses

**Course-derived: Stanford PS3 Problem 7(i–ii).** Construct a map with two different left inverses and prove why having a left inverse implies injectivity.

**Solution.** Let $A={0,1}$, $B={a,b,c}$, with $f(0)=a,f(1)=b$. Both maps $ℓ_0,ℓ_1:B→A$ send $a$ to 0 and $b$ to 1; let $ℓ_0(c)=0$ and $ℓ_1(c)=1$. At each input in $A$, either left inverse returns it after $f$, so both satisfy $ℓ_i∘f=id_A$. They differ at the unused target $c$. Generally, if $f(u)=f(v)$, applying a left inverse gives $u=ℓ(f(u))=ℓ(f(v))=v$. This proves injectivity while explaining why the inverse's unused-target values remain unconstrained. Here the count $2^{3−2}=2$ agrees with the construction.

### Problem 10. Multiple right inverses

**Course-derived: Stanford PS3 Problem 7(iii–iv).** Construct an onto map with two right inverses and prove the implication to onto-ness.

**Solution.** Let $A={0,1,2}$, $B={a,b}$, and $f(0)=f(1)=a,f(2)=b$. Define $r_0(a)=0,r_1(a)=1$, and $r_0(b)=r_1(b)=2$. Either choice has $f(r_i(a))=a$ and $f(r_i(b))=b$, hence is a right inverse. The choices differ in the two-element fiber over $a$. In general, for any $b∈B$, the element $r(b)∈A$ has output $b$, so every target is attained. The right inverse is an injection into selected representatives; it does not undo every original input.

### Problem 11. Uniqueness and why one-sided proofs fail

**Course-derived: Stanford PS3 Problem 7(v–vii).** Prove uniqueness of a true inverse and identify the exact failure for left-only and right-only inverses.

**Solution.** For inverse candidates $k,ℓ:B→A$, compute $k=k∘id_B=k∘(f∘ℓ)=(k∘f)∘ℓ=id_A∘ℓ=ℓ$. If both are only left inverses, the equality $f∘ℓ=id_B$ need not hold, so the second replacement is unjustified. If both are only right inverses, the equality $k∘f=id_A$ need not hold, so the penultimate replacement is unjustified. Problems 9 and 10 provide actual nonunique pairs, confirming that these are genuine logical gaps, not merely inconvenient proof choices. If one map is a left inverse and another a right inverse, the two identities needed in the displayed argument are both present; they must coincide.

### Problem 12. Composition implications and small counterexamples

**Course-derived: CMU Assignment 5(1), Cambridge Functions exercise 3, and Stanford PS3 Problem 8(i–ii).** Determine the implications involving injectivity, onto-ness, and a bijective composite.

**Solution.** Injections compose to an injection by applying the outer injection to equal composite outputs and then the inner injection. Onto maps compose to an onto map by selecting an antecedent in the middle set and then an antecedent in the first domain. An injective inner map alone does not suffice: take the identity on ${0,1}$ followed by a constant map to ${0}$. An onto outer map alone does not suffice: take the inclusion ${0}→{0,1}$ followed by the identity on ${0,1}$; target 1 is missed.

If $g∘f$ is bijective and $f$ is onto, then $f$ is also injective because the composite is. To prove $g$ injective, take $g(b_1)=g(b_2)$, use onto-ness of $f$ to write $b_i=f(a_i)$, then use composite injectivity to get $a_1=a_2$ and therefore $b_1=b_2$. The composite being onto already makes $g$ onto. Thus $g$ is bijective. This proves the contrapositive of Stanford's first assertion. If $g$ is injective and the composite is onto, take any $b∈B$; some $a$ satisfies $g(f(a))=g(b)$, so injectivity gives $f(a)=b$. The inner map is onto and, from composite injectivity, injective. This proves the second assertion's contrapositive. Each inference uses the appropriate additional hypothesis rather than assuming both factors inherit a composite property.

### Problem 13. A bijection assembled from two nonbijections

**Course-derived: Stanford PS3 Problem 8(iii).** Find nonbijective $f$ and $g$ with a bijective composite.

**Solution.** Use $A={0,1}$, $B={a,b,c}$, $C={u,v}$. Send 0 to $a$ and 1 to $b$ under $f$. Under $g$, send $a$ and $c$ to $u$, and $b$ to $v$. The inner map misses $c$ and is not onto. The outer map collides at $a,c$ and is not injective. Yet the composite sends 0 to $u$ and 1 to $v$, a bijection. The unused middle point is precisely where the outer collision occurs. Restricted to $f[A]={a,b}$, $g$ is bijective onto $C$. This is the mechanism shown in Figure 2.

### Problem 14. Domain-aware composite and a rational obstruction

**Original, using Oxford's domain emphasis and Claim 2.2.** Find the real domain of $g∘f$ for $f(x)=x^2−1$, $g(t)=1/t$. Then prove $h:ℚ→ℚ$ given by $h(x)=x^5+x^3$ is not onto.

**Solution.** The inner rule is defined for all reals, but the outer rule forbids zero. Solve $x^2−1=0$; exclude exactly $x=−1,1$. On the remaining domain the composite is $1/(x^2−1)$. For $h$, rational closure makes the rule valid. To show that target 1 is missed, suppose a reduced rational $m/n$ with $n>0$ satisfies the equation. Multiplying by $n^5$ gives $m^5+m^3n^2=n^5$. If $n$ is even, reducedness makes $m$ odd; the left side is odd and the right even. If $n$ is odd and $m$ even, the left side is even and the right odd. If both are odd, the left side is the sum of two odd numbers and is even, while the right remains odd. Both even is excluded by reducedness. Every possible parity combination fails. Thus 1 has no rational antecedent. Unbounded outputs alone do not prove onto-ness on a rational target.

### Problem 15. Exhaustive small function spaces

**Course-derived: Cambridge Functions exercise 1, with labels replaced by indices.** Describe and classify every map among $A_2={0,1}$ and $A_3={0,1,2}$.

**Solution.** A map from $A_i$ to $A_j$ is uniquely the tuple of its outputs in domain order. Thus the exact four spaces are ${0,1}^2$, ${0,1,2}^2$, ${0,1}^3$, and ${0,1,2}^3$; these Cartesian-power descriptions specify every tuple, not just counts. In the two-to-two space the tuples are $(0,0),(0,1),(1,0),(1,1)$; exactly the middle two are injections, onto maps, and bijections. In the two-to-three space the nine tuples are $(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)$; the six unequal-coordinate tuples are injections, and none is onto. In the three-to-two space the eight tuples are $(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)$; the six nonconstant tuples are onto, and none is injective. In the three-to-three space all 27 triples are classified by coordinate pattern: six triples using three distinct values are bijections, eighteen using exactly two distinct values are neither injection nor onto, and three constants are neither. This partitions all triples into disjoint complete classes. The exact enumerator below prints each tuple and its labels, including all 27, without an ellipsis standing in for unexplained classifications.

```python
from itertools import product
for domain_size, target_size in [(2, 2), (2, 3), (3, 2), (3, 3)]:
    for values in product(range(target_size), repeat=domain_size):
        injective = len(set(values)) == domain_size
        surjective = set(values) == set(range(target_size))
        print(domain_size, target_size, values, injective, surjective,
              injective and surjective)
```

### Problem 16. Cancellation with a missed target

**Original.** Show why an inner map can be cancelled only under an onto hypothesis when comparing arbitrary outer maps.

**Solution.** Let $f:{0}→{a,b}$ have output $a$. Let $g,h:{a,b}→{0,1}$ agree at $a$ with value zero, but let $g(b)=0$ and $h(b)=1$. Both composites with $f$ are the constant-zero map, yet $g≠h$. The missing target $b$ hides their difference. If $f$ is onto instead, every $b$ is $f(a)$ for some input, so equality of composite values there proves equality of the outer values at every $b$. The analogous left-cancellation property requires injectivity of the outer map because a collision can hide differing inner outputs. Cancellation is therefore a property with a precise quantified hypothesis, not an algebraic permission automatically granted by composition notation.

### Problem 17. An empty injection with no left inverse

**Original.** Analyze the injection $f:∅→{b}$ and compare it with $∅→∅$.

**Solution.** The first map exists and is injective because its domain contains no colliding inputs. A total left inverse would need type ${b}→∅$, which cannot exist: its input $b$ would have no available output. Thus “injective iff admits a left inverse” needs a nonempty-domain qualification or the special both-empty case. For $∅→∅$, the empty map exists in both directions, and both composition identities are the empty identity. It is therefore a bijection with its unique inverse. Checking types exposes the failure before any equation manipulation is attempted.

### Problem 18. Image of a difference under an injection

**Course-derived: CMU Assignment 5(2).** Prove $f[S∖T]=f[S]∖f[T]$ for an injection $f:A→B$ and $S,T⊆A$, then exhibit failure without injectivity.

**Solution.** If $y=f(x)$ with $x∈S∖T$, then $y∈f[S]$. If it also belonged to $f[T]$, some $t∈T$ would have $f(t)=f(x)$, and injectivity would force $t=x$, contradicting $x∉T$. This proves one inclusion. Conversely, if $y∈f[S]∖f[T]$, choose $x∈S$ with $f(x)=y$. This $x$ cannot be in $T$, so $y∈f[S∖T]$; this direction did not need injectivity. For a counterexample, let two distinct inputs $u,v$ both map to $b$, choose $S={u}$ and $T={v}$. The image of the difference is ${b}$, while the difference of images is empty. The direction that failed was exactly the direction using injectivity.

### Problem 19. A complete finite image and preimage calculation

**Original.** Let $A={0,1,2,3}$, $B={a,b,c}$, and output tuple $(a,b,a,b)$. Use $S={0,1}$ and $T={a,c}$ to compute both round trips.

**Solution.** The image of $S$ is ${a,b}$, and its preimage is all four inputs. Thus the input round trip expands $S$ to $A$. The fiber over $a$ is ${0,2}$, over $b$ is ${1,3}$, and over $c$ is empty. The preimage of $T$ is ${0,2}$; its image is ${a}$, precisely $T∩f[A]$. The unused target $c$ disappears in the target round trip, while omitted members of touched fibers appear in the input round trip. Repeating either operation stabilizes: all touched fibers are already filled, and all retained targets are already attained.

### Problem 20. Preimages of a quadratic target condition

**Original.** For $f:ℝ→ℝ$, $f(x)=x^2$, find the preimages of $[1,4]$, $(1,4]$, and $ℝ∖[1,4]$.

**Solution.** The condition $1≤x^2≤4$ means $1≤|x|≤2$, so the first preimage is $[−2,−1]∪[1,2]$. For the half-open target, the lower inequality is strict; the preimage is $[−2,−1)∪(1,2]$. The complement law gives the third preimage as the real complement of the first, namely $(−∞,−2)∪(−1,1)∪(2,∞)$. Directly testing $x^2<1$ or $x^2>4$ gives the same result. Negative target values are unattained but still cause no difficulty in preimage notation. An inverse function was never required.

### Problem 21. Exact equality conditions for set laws

**Original.** Prove that $f[S∩T]=f[S]∩f[T]$ for all input subsets iff $f$ is injective, and that $f[f^{-1}[U]]=U$ for all target subsets iff $f$ is onto.

**Solution.** With an injection, a value in both images has witnesses $s∈S,t∈T$ with equal outputs; injectivity makes them the same input, which belongs to the intersection. The opposite inclusion is unconditional. Conversely, distinct colliding inputs $s,t$ would violate the supposed equality for the disjoint singleton sets ${s},{t}$. For the second equivalence, the left side is always $U∩f[A]$, by tracing an antecedent into $U$. If $f$ is onto this is $U$ for every choice. If every choice gives equality, choose $U=B$ to obtain $f[A]=B$. These arguments show why an equality on one convenient subset is weaker than a universally quantified equality.

### Problem 22. A quotient that remembers an intersection

**Course-derived: Cambridge Functions exercise 2.** Fix $B⊆A$ and identify subsets $X,Y⊆A$ when $X∩B=Y∩B$. Construct a bijection from the quotient to $𝒫(B)$.

**Solution.** Equality of intersections is reflexive, symmetric, and transitive, so it defines an equivalence. Define $h([X])=X∩B$. Equal classes mean equal intersections, making the definition independent of representatives. If $h([X])=h([Y])$, the defining relation identifies the two representatives, so their classes agree and $h$ is injective. Every subset $T⊆B$ is itself a subset of $A$, and $h([T])=T$, proving onto-ness. The inverse sends $T$ to its class. Elements outside $B$ vary freely inside a class and carry no information in this quotient; this explains the bijection rather than merely counting both sides in the finite case.

### Problem 23. Product reassociation and currying

**Course-derived: Cambridge Functions exercise 4, first and fourth comparisons.** Establish explicit bijections between $A×(B×C)$ and $(A×B)×C$, and between $C^{A×B}$ and $(C^B)^A$.

**Solution.** Send $(a,(b,c))$ to $((a,b),c)$. The inverse removes the alternative parentheses, so both compositions are the identity. These are not literally equal sets of ordered pairs under standard pair encodings, but they are explicitly bijective. For currying, send $u$ to the map $v$ with $v(a)(b)=u(a,b)$. The reverse sends $v$ to $u(a,b)=v(a)(b)$. Substituting each into the other recovers every value, hence every function. If $A$ or $B$ is empty, the formulas still give the unique available input-free maps of the appropriate types; if $C$ is empty and the relevant domain is nonempty, both spaces have the matching absence of maps. Pointwise construction handles these cases more reliably than an unqualified exponent manipulation.

### Problem 24. Tagged unions and a false exponent identity

**Course-derived: Cambridge Functions exercise 4, fifth and sixth comparisons.** Show $C^{A⊔B}$ is bijective with $C^A×C^B$, but $C^{B^A}$ need not be bijective with $(C^B)^A$.

**Solution.** Restrict a map on the tagged union to its two tagged components. Conversely, given a pair of maps, apply the first to a left-tagged input and the second to a right-tagged input. The tags make the branches disjoint even if $A$ and $B$ overlap as underlying sets, and the constructions are inverses. For the proposed second identity, take all three sets to have two elements. Then $B^A$ has four elements, so $C^{B^A}$ has 16. The other space has $(2^2)^2=16$ as well in this particular case, which does not disprove it. Instead take $|A|=3,|B|=|C|=2$: the first size is $2^{2^3}=256$, while the second is $(2^2)^3=64$. No bijection exists for these finite sets. Degenerate choices such as a singleton $C$ do yield a singleton space on both sides. An accidental equality for one size triple is not a universal function-space identity.

### Problem 25. Squaring a set and doubling a set

**Course-derived: Cambridge Functions exercise 4, second and third comparisons.** Determine when finite $A×A$ can be bijective with $A$ or with $A⊔A$, and give infinite examples.

**Solution.** If $|A|=m$ is finite, the first requires $m^2=m$, so $m=0$ or $m=1$. These cases have explicit empty or singleton bijections. The second requires $m^2=2m$, so $m=0$ or $m=2$; for a two-element set, assign the four pairs to the two tagged copies in any fixed order. For $A=ℕ$, the pairing map in the lesson bijects $A×A$ with $A$. The tagged-union map sends $(left,n)$ to $2n$ and $(right,n)$ to $2n+1$, bijecting $A⊔A$ with $A$. Compose one bijection with the inverse of the other to compare $A×A$ and $A⊔A$. This proves the infinite example explicitly; no arithmetic subtraction of infinite cardinalities is used.

### Problem 26. Descent to two quotient sets

**Course-derived: Cambridge Functions exercise 5.** Let $R,S$ be equivalence relations on $A,B$, with quotient maps $p,q$. Characterize when a map $f:A→B$ induces $h:A/R→B/S$ satisfying $h∘p=q∘f$.

**Solution.** If such $h$ exists and $aRa'$, then $p(a)=p(a')$. Applying $h$ gives $q(f(a))=q(f(a'))$, hence $f(a)Sf(a')$. Conversely, assume this compatibility and define $h([a]_R)=[f(a)]_S$. Two representatives of the same source class have $S$-equivalent outputs, so the target classes coincide and the rule is well-defined. Evaluating at any $a$ proves the required commuting equation. Every source class has a representative, so this equation determines $h$ uniquely. For an example, let $f(x)=2x$ on integers and let both relations be congruence modulo 3; congruent inputs have congruent doubled outputs. For a failure, let the source relation identify integers by parity while the target is literal equality; doubling parity-equivalent 0 and 2 gives unequal values, so that quotient rule cannot land in literal integers without ambiguity.

### Problem 27. Subsets as ordered Boolean vectors

**Course-derived: Cambridge Functions exercise 6.** Prove that subsets of ${a,b,c}$ under inclusion form an order isomorphic to ${0,1}^3$ under coordinatewise order.

**Solution.** Send a subset to its three indicator values in the order $a,b,c$. Every Boolean vector uniquely determines the subset of coordinates equal to one, so the map is a bijection. If $S⊆T$, any coordinate equal to one for $S$ is one for $T$, and zeros never exceed either allowed coordinate; thus the vector inequality holds. Conversely, coordinatewise inequality prevents any member of $S$ from being absent in $T$, proving inclusion. The inverse therefore also preserves order. Bijection plus monotonicity in only one direction would not by itself prove order isomorphism for arbitrary partial orders; both directions have been checked here.

### Problem 28. Counting partial maps with prescribed defined size

**Course-derived: Cambridge Functions exercise 7, extended.** Count partial maps from an $m$-element input universe to an $n$-element target, and those defined at exactly $k$ inputs.

**Solution.** Every input independently chooses one of $n$ outputs or undefinedness, giving $(n+1)^m$. For exactly $k$ defined inputs, first select that subset in $C(m,k)$ ways, then assign one of $n$ outputs to each in $n^k$ ways. The count is $C(m,k)n^k$. Summing over $k$ recovers the binomial expansion of $(n+1)^m$. When $n=0$, the only partial map is everywhere undefined; the $k=0$ term is one and all positive-$k$ terms vanish. When $m=0$, the unique empty map is counted once. Domain-subset choice is separate from output choice.

### Problem 29. An explicit natural-pair bijection

**Course-derived: CMU Assignment 5(3).** Prove that $p(x,y)=2^x(2y+1)−1$ bijects $ℕ×ℕ$ with $ℕ$, and decode 39.

**Solution.** The expression is nonnegative because $2^x≥1$ and $2y+1≥1$. Given $z≥0$, factor the positive integer $z+1$ into $2^x u$ with $u$ odd and positive. Repeated division by two stops at exactly one odd part; then $y=(u−1)/2$ is a nonnegative integer. This constructs an antecedent and proves uniqueness, since the exponent of two and odd part are unique. For $z=39$, factor 40 as $2^3⋅5$, so the pair is $(3,2)$; substitution gives $8⋅5−1=39$. Reading $2^x$ as $2x$ would destroy both the definition and its proof, which is why the exponent must be rendered correctly.

### Problem 30. A closed-to-open interval bijection

**Course-derived: Stanford PS3 extra credit; explicit original construction.** Construct a bijection $[0,1]→(0,1)$ without assuming continuity.

**Solution.** Use two disjoint sequences: $a_n=1/(n+3)$ and $b_n=1−1/(n+3)$ for $n≥0$. All $a_n$ are at most $1/3$, and all $b_n$ at least $2/3$, so they do not overlap. Map endpoint 0 to $a_0$, endpoint 1 to $b_0$, each $a_n$ to $a_{n+1}$, each $b_n$ to $b_{n+1}$, and every other point to itself. The two shifted sequence branches are injective, their images are disjoint, and the unchanged points lie outside both images. Every target in a sequence has its predecessor or the appropriate endpoint as antecedent; every other target has itself. Thus the map is a bijection. It is not a continuous bijection, and no continuity requirement was imposed. This construction absorbs finitely many extra endpoints into infinite chains.

### Problem 31. Finite subsets versus all subsets of naturals

**Course-derived: Cambridge Functions exercises 8–9.** Show finite subsets of $ℕ$ are countable, while all subsets and all binary sequences are uncountable.

**Solution.** Encode a finite subset $S$ by the natural integer obtained by adding $2^i$ for its finitely many members $i$. Unique binary expansion makes this map injective, including the empty subset encoded by zero. Hence the finite-subset family is countable. For all subsets, suppose $F:ℕ→𝒫(ℕ)$ were onto and form $D={n:n∉F(n)}$. An index $d$ with $F(d)=D$ would satisfy $d∈D$ iff $d∉D$, impossible. Thus the power set is uncountable. Its indicator bijection with binary sequences transfers uncountability. To encode those sequences injectively as reals without ambiguous binary expansions, place their bits as ternary digits 0 or 2. If two sequences first differ at position $k≥1$, that digit creates difference $2/3^k$, while all later possible differences sum to at most $1/3^k$; a strictly positive gap remains. Hence the encoding is injective. The same counting intuition that enumerates finite subsets cannot enumerate unrestricted infinite ones.

### Problem 32. Three constrained binary-sequence families

**Course-derived: Cambridge Functions exercise 10, first three families.** Classify nondecreasing binary sequences, sequences whose positions $2n,2n+1$ differ for every $n$, and sequences whose consecutive bits always differ.

**Solution.** A nondecreasing binary sequence is either all zero, or has a first one at some index $k$, after which every bit is one. Index $k=0$ includes the all-one sequence. This is a countably infinite family: map all-zero to 0 and the first-one-at-$k$ sequence to $k+1$. For the paired constraint, the even-position bits are entirely free, and every odd-position bit is forced to be their complement. Reading the even bits and filling each complementary neighbor gives inverse bijections with all binary sequences, so the family is uncountable. For the consecutive constraint, choosing the first bit forces every later bit to alternate; there are exactly two sequences. Superficially similar “different neighbors” requirements have radically different numbers of free coordinates.

### Problem 33. Monotone natural-valued sequences

**Course-derived: Cambridge Functions exercise 10, last two families.** Classify nondecreasing and nonincreasing maps $ℕ→ℕ$ by cardinality.

**Solution.** Nondecreasing sequences are uncountable. Given arbitrary binary bits $b_i$, define $f(0)=b_0$ and $f(n+1)=f(n)+b_{n+1}$. The sequence is nondecreasing, and its initial value and successive increments recover every original bit, so this is an injection from an uncountable family. Nonincreasing natural-valued sequences are countably infinite. Starting at $k$, they can have at most $k$ strict drops, because each drop reduces a nonnegative integer by at least one. Thus they are eventually constant. Encode each sequence by a finite prefix through its final strict drop and its terminal value; finite sequences of naturals are countable by repeated pairing and a length code. There are infinitely many constant sequences, so the family is not finite. This reasoning depends on the natural target: a decreasing positive real sequence can have infinitely many strict drops.

### Problem 34. Rational pairs and disjoint discs

**Course-derived: Cambridge Functions exercise 11.** Prove $ℚ×ℚ$ is countable and any family of pairwise disjoint nonempty open discs in the plane is countable. Explain why circles differ.

**Solution.** Inject rationals into naturals using reduced numerator-denominator encodings, then pair the two natural indices; this injects rational pairs into naturals. Each nonempty open disc contains a point with both coordinates rational, since between two distinct real bounds there is a rational in each coordinate. Fix an enumeration of rational pairs and select the first such point in each disc. Different disjoint discs get different selected points, giving an injection into a countable set. No arbitrary choice is needed once the fixed enumeration supplies a least index. For circles meaning only perimeters, concentric circles centered at the origin with distinct positive radii are pairwise disjoint; there are uncountably many possible radii. An open-disc argument cannot apply because a circle does not contain an open rectangle or necessarily a rational-coordinate point. Here “disc” explicitly excludes an empty interior or radius zero.

### Problem 35. An affine conversion inverse

**Course-derived: CMU Assignment 5(4).** Invert the real function $F(C)=9C/5+32$ and verify both directions.

**Solution.** Solve $y=9x/5+32$: subtract 32, then multiply by $5/9$, obtaining $G(y)=5(y−32)/9$. Every real target produces a real input. Substitution gives $F(G(y))=9⋅5(y−32)/(5⋅9)+32=y$ and $G(F(x))=5(9x/5)/9=x$. Both types are real-to-real, so this proves a true inverse. A numerical check at $x=0$ yields $F(0)=32,G(32)=0$, but that example alone would not prove the two universal identities.

### Problem 36. Onto maps force a finite size inequality

**Course-derived: CMU Assignment 5(5).** Prove a surjection from an $m$-element set onto an $n$-element set requires $m≥n$.

**Solution.** Each target has a nonempty fiber, and fibers are pairwise disjoint. Choose one member in each of the finitely many fibers. These $n$ chosen inputs are distinct and belong to a domain with $m$ members, so $n≤m$. If the target is empty, existence of a total map forces the domain empty as well, and the inequality holds. This is a necessary condition: when $m≥n>0$, some onto map can be constructed, but a particular constant assignment may still miss targets. The conclusion is about the existence of the specified onto function, not about every rule between sets of those sizes.

### Problem 37. Finite deletion, insertion, and bijections

**Course-derived: CMU Assignment 5(6–7).** If $|X|=n>1$, $x∈X$, and $y∉X$, prove the deletion and insertion sizes. Then prove a bijection preserves finite size.

**Solution.** Enumerate $X$ by labels $1,…,n$. If the removed element has label $j$, keep labels below $j$ and subtract one from labels above $j$; this is a bijection from $X∖{x}$ to labels $1,…,n−1$. For insertion, keep the old labels and assign the fresh element $y$ label $n+1$, giving size $n+1$. If $h:X→Y$ is a bijection and $X$ has labels $1,…,n$, composing the labeling inverse with $h$ enumerates $Y$ with exactly those $n$ labels. Alternatively the injection and onto inequalities give both $|X|≤|Y|$ and $|X|≥|Y|$. The freshness condition $y∉X$ is essential: adding an existing element does not change a set.

### Problem 38. Onto counts, image size, and constrained outputs

**Original.** Count maps from four labeled inputs to three labeled targets; count the onto maps and those with image size two. Then fix $f(0)=a,f(1)=b$ and require onto-ness.

**Solution.** There are $3^4=81$ unrestricted maps. Inclusion–exclusion gives $3^4−3⋅2^4+3⋅1^4=81−48+3=36$ onto maps. For image size two, choose the two targets in three ways. Onto maps to those two targets number $2^4−2=14$, excluding their two constants. The result is $3⋅14=42$. The remaining image-size-one maps number 3, and $36+42+3=81$ checks the disjoint classification. Under the two fixed distinct outputs, the remaining two inputs have nine assignments. To be onto they must include $c$ at least once. Four assignments use only ${a,b}$, so the count is $9−4=5$. Applying the unrestricted onto formula to all four inputs would ignore the fixed-value constraints.

### Problem 39. Counting one-sided inverses from fibers

**Original.** An injection from three inputs into five targets has how many left inverses? An onto map has labeled fiber sizes $2,3,1$; how many right inverses does it have?

**Solution.** A left inverse's values at the three attained targets are forced by their unique antecedents. Each of the two unused targets can independently be sent to any of three inputs, so there are $3^2=9$ left inverses. For a right inverse, choose one representative from each of the three fibers, giving $2⋅3⋅1=6$. Every choice satisfies the right identity by construction, and different choices produce different functions. None is a true inverse of that second map, because its first two fibers contain collisions. The counts are counts of maps of the reverse type; they are not counts of inverse relations.

### Problem 40. Kernel factorization and the number of saturated subsets

**Original.** Let a function on a five-element domain have three nonempty fibers of sizes $2,2,1$ and one unused target. How many input subsets are saturated? Describe its quotient factorization.

**Solution.** A saturated subset must contain either all or none of each nonempty fiber. There are two independent choices for each of three fibers, so exactly $2^3=8$ saturated subsets. The original domain has $2^5=32$ subsets, most of which select only part of a fiber and therefore expand in a round trip. The quotient map merges inputs into three classes; the induced map from these classes to the three attained targets is bijective; the inclusion into the four-element codomain misses one point. This explains both the count and the failure of onto-ness in the original declaration. The unused target contributes an empty preimage, not a fourth nonempty domain class.

### Problem 41. Idempotent functions and permutation dynamics

**Original.** Count idempotent maps on a three-element set and find the order of a permutation with disjoint cycle lengths two and three.

**Solution.** An idempotent function's image is its fixed-point set. Choose a nonempty fixed subset of size $k$; every remaining input independently chooses one of those $k$ fixed points. Each resulting assignment is idempotent, and every idempotent assignment has exactly this construction. Thus the three-element count is $C(3,1)1^2+C(3,2)2^1+C(3,3)3^0=3+6+1=10$. An empty image cannot occur on a nonempty domain. For the permutation, an iterate returns every point precisely when its exponent is divisible by both cycle lengths. The smallest positive such exponent is $lcm(2,3)=6$. A permutation's inverse reverses its cycles; an idempotent function with a collision is a projection, not a permutation. These two compositional identities should not be confused.

### Problem 42. A concrete Schröder–Bernstein construction

**Original.** Apply the layer construction to injections $u,v:ℕ→ℕ$ with $u(n)=2n$ and $v(n)=n+1$.

**Solution.** The initial layer is $A_0=ℕ∖v[ℕ]={0}$. The next layer sends 0 through $u$ and then $v$, giving ${1}$; later layers are ${3},{7},{15},…$. By induction the $k$th layer is ${2^k−1}$: the recurrence transforms $2^k−1$ into $2^{k+1}−1$. Let $H$ be this sequence of inputs. On $H$, the constructed bijection gives $h(n)=2n$; outside $H$, it gives $h(n)=n−1$, the inverse of $v$ on its image. Outside $H$ there is no zero, so the second branch is valid. To inspect a target $b$, if $b=2^{k+1}−2$, it is reached from $2^k−1$ by the first branch. Otherwise $b+1$ is outside $H$ and the second branch reaches $b$. The branch images are disjoint by the same calculation. For example the outputs at inputs $0,1,2,3,4,5,6,7$ are $0,2,1,6,3,4,5,14$. A finite prefix can look nonmonotone or skip a value temporarily; the full branch proof establishes the bijection.
