## Sources, scope, and prerequisites

This chapter synthesizes four principal written university courses: Oxford Discrete Mathematics (Andrew D. Ker), Stanford CS103 (Keith Schwarz), Cambridge Discrete Mathematics (Peter Robinson), and MIT 6.042J (Tom Leighton and Marten van Dijk; notes by Lehman, Leighton, and Meyer). CMU 21-127 exercises (Shaun Allison) and Cornell CS2800 notes (Michael George) supply focused additional material. The [source comparison and reading ledger](../reviews/d_functions-sources.html) records exact sections, candidate decisions, exercise coverage, and corrected qualifications.

You should already understand quantified statements, elementary proof methods, sets, Cartesian products, and equivalence relations. If needed, revisit [Sets](d_sets.html), [Proof Methods](d_proof.html), and [Relations](d_relations.html). Here $ℕ={0,1,2,…}$; positive naturals are $ℕ_+$. All functions are total unless explicitly called partial. Complements always name their ambient set. Composition is written in the standard right-to-left order. No archived Iranian entrance-examination question is used in this chapter.

The boundary extends from exact definitions to inverse and cancellation theorems, image/preimage calculus, quotient factorization, finite counting, function spaces, and cardinality constructions. Calculus, advanced set-theoretic independence, and the full theory of computable functions are separate subjects. The aim is transferable proof and problem-solving ability; a bounded chapter cannot guarantee success on every unseen question. Read the lesson before treating the worked bank as practice. Every problem has a complete solution, so no preliminary assessment is required.

## Functions as typed mathematical objects

### Domain, codomain, graph, and the uniqueness axiom

A function $f:A→B$ consists of a domain $A$, a codomain $B$, and a graph $Γ_f⊆A×B$ such that every element of $A$ appears as the first coordinate of exactly one graph pair. The precise condition is:

<div class="formula-block">∀a ∈ A, ∃!b ∈ B such that (a,b) ∈ Γ<sub>f</sub>.</div>

The symbol $∃!$ means existence and uniqueness together. Existence excludes a missing output; uniqueness excludes two different outputs for the same input. We write $f(a)=b$ for the unique partner. Equal outputs for different inputs are allowed: uniqueness concerns the output for one fixed input, not uniqueness of the input for an output. An arrow diagram must therefore have exactly one outgoing arrow from each domain vertex. No such requirement applies to incoming arrows at a codomain vertex.

The notation $f:A→B$ declares a type; $a↦f(a)$ declares an assignment. A formula alone may not specify a function completely. The rule $x↦x^2$ can define a function from reals to reals, from reals to nonnegative reals, or from nonnegative reals to nonnegative reals. These declarations produce different answers to inverse and surjectivity questions. An output outside the declared codomain invalidates the proposed function before classification begins.

The image is $f[A]={f(a):a∈A}⊆B$. The codomain is the declared target; the image is the target subset actually attained. Some texts call either of these the “range.” This chapter avoids that ambiguous word. Two typed functions are equal when their domains and codomains agree and their values agree at every input. A corestriction to a smaller target preserves all assignments but changes the typed function.

If $A=∅$, the empty graph defines exactly one function into each specified $B$. The universal uniqueness condition has no input to check. If $A≠∅$ and $B=∅$, no function exists, because existence fails at every input. If $A=B=∅$, the empty function is the identity and a bijection. A constant function into a nonempty target is valid for every domain, including the empty domain. The empty graph with different declared codomains is the same set of pairs but a different typed object.

### Restrictions, corestrictions, piecewise rules, and partial functions

For $S⊆A$, the restriction $f|_S:S→B$ keeps just the graph pairs whose first coordinate belongs to $S$. Restriction can eliminate collisions or lose outputs. For $T⊆B$ containing $f[A]$, a corestriction $A→T$ keeps the graph and the whole domain. Corestricting to $f[A]$ makes a function surjective; it does not remove collisions. Corestricting to a set that omits an attained value is invalid.

A piecewise rule is a function when every input is covered and overlapping branches agree wherever both apply. Disjoint, exhaustive branches make this straightforward. If the first branch applies for $x≥0$ and the second for $x≤0$, both prescribe the value at zero, so that value must coincide. Disjoint branches can still leave a gap: conditions $x<0$ and $x>0$ omit zero on a real domain.

A partial function $A⇀B$ has at most one output per input, but it may be undefined at some inputs. Its defined subset $D⊆A$ carries a total restriction $D→B$. Distinguish the declared input universe $A$ from this defined subset. Add a fresh symbol $⊥∉B$ and send every undefined input to it; this gives a total function $A→B∪{⊥}$. The word “fresh” matters: an ordinary output equal to the sentinel must not be confused with undefinedness. A program with hidden state or randomness is not necessarily a mathematical function of its visible argument; a suitable deterministic model includes the relevant state and random seed in its input.

### Intervals, floor, ceiling, and boundary values

For $a<b$, $(a,b)$ excludes both endpoints, $[a,b]$ includes both, and mixed brackets include exactly the indicated endpoint. Infinity is not a real number, so a real half-line is open at infinity. Domain restrictions must survive every algebraic manipulation: simplifying $x/x$ to $1$ does not make the original expression defined at zero.

For real $x$, the floor $⌊x⌋$ is the greatest integer at most $x$; the ceiling $⌈x⌉$ is the least integer at least $x$. Their defining inequalities are $⌊x⌋≤x<⌊x⌋+1$ and $⌈x⌉−1<x≤⌈x⌉$. Thus $⌊−1.2⌋=−2$ and $⌈−1.2⌉=−1$; truncation toward zero is a different operation. The fiber of integer $k$ under floor is $[k,k+1)$, while under ceiling it is $(k−1,k]$. Both maps from $ℝ$ to $ℤ$ are onto and fail to be injective. These fibers make the endpoint conventions visible.

## Injectivity, surjectivity, and fibers

### Exact definitions and negations

A function $f:A→B$ is injective when equality of outputs forces equality of inputs:

<div class="formula-block">∀a<sub>1</sub>,a<sub>2</sub> ∈ A, f(a<sub>1</sub>) = f(a<sub>2</sub>) ⇒ a<sub>1</sub> = a<sub>2</sub>.</div>

Equivalently, distinct inputs have distinct outputs. To disprove injectivity, exhibit two specific distinct domain elements with equal outputs. The fact that each input has only one output is already part of being a function and proves nothing about injectivity.

Surjectivity means that every declared target is attained:

<div class="formula-block">∀b ∈ B, ∃a ∈ A such that f(a) = b.</div>

To prove it, start with an arbitrary target $b$, construct an input possibly depending on $b$, check that the input belongs to $A$, and verify its output. To disprove it, give one target $b∈B$ for which every input fails. Reversing the quantifiers to “one input produces every output” usually asks for something completely different. A bijection is both injective and surjective; “one-to-one” means injective, not automatically bijective.

The fiber over $b$ is $F_b=f^{-1}[{b}]={a∈A:f(a)=b}$. This notation denotes a set even when no inverse function exists. The fibers are pairwise disjoint, since a shared input would have two different outputs. Their union over all $b∈B$ is $A$, because every input has an output. Nonempty fibers partition the domain. Injectivity says every fiber has size at most one; surjectivity says every fiber is nonempty; bijectivity says every fiber has exactly one element.

<!-- FIGURE:fibers -->

### Proof templates and finite bounds

For an algebraic injection, assume $f(u)=f(v)$ with $u,v∈A$ and deduce $u=v$ by valid operations. Division by a quantity that might be zero is not valid without a case split. Squaring an equality can lose sign information; when finding an inverse, confirm the permitted sign from the domain. A strictly increasing or strictly decreasing function on a totally ordered domain is injective: for $u≠v$, one is smaller, and strict monotonicity gives unequal outputs. Ordinary nondecreasing behavior is insufficient.

For finite sets, let $|A|=m$ and $|B|=n$. An injection gives $m≤n$ because distinct inputs occupy distinct targets. A surjection gives $m≥n$ because the $n$ nonempty disjoint fibers together contain $m$ elements. If $m=n$, either property implies the other: there is no capacity left for an empty fiber or an oversized fiber. If $m<n$, an injection need not be onto; if $m>n$, a surjection need not be injective. Size inequalities are necessary conditions, not properties of every particular assignment.

For an endofunction on a finite set, injective, surjective, and bijective are equivalent. This equivalence fails for infinite carriers: $n↦n+1$ on $ℕ$ is injective and misses zero, while $n↦⌊n/2⌋$ is onto and merges consecutive pairs. Infinite cardinal equality likewise does not imply that a specified map is a bijection. The empty function into a nonempty set is injective and not onto; its image is empty.

## Composition and cancellation

### Types, order, associativity, and image restrictions

For $f:A→B$ and $g:B→C$, define $(g∘f)(a)=g(f(a))$. The domain is $A$, the codomain is $C$, and the inner map acts first. If only formulas are supplied, first find the input set on which the inner rule is defined and its values lie in the outer rule's domain. With $f:A→B$ and $g:D→C$, the composite rule can be evaluated on all of $A$ when $f[A]⊆D$; a strict typed presentation inserts a corestriction to $D$ rather than silently identifying $B$ and $D$.

Composition is associative. If $h:C→D$, both $h∘(g∘f)$ and $(h∘g)∘f$ are maps $A→D$. At every $a∈A$, both evaluate to $h(g(f(a)))$. Equality of types and pointwise values proves equality of the functions. Identity maps satisfy $id_B∘f=f=f∘id_A$. Composition need not commute, and sometimes the reverse composition is not even typed. Even for real endofunctions, $f(x)=x+1$ and $g(x)=2x$ yield outputs $2x+2$ and $2x+1$ in the two orders.

### Preservation and reverse implications

If $f$ and $g$ are injections, equality $g(f(u))=g(f(v))$ first gives $f(u)=f(v)$ and then $u=v$. If both are onto, take any $c∈C$, choose $b∈B$ with $g(b)=c$, then choose $a∈A$ with $f(a)=b$; this $a$ maps to $c$. Two bijections therefore compose to a bijection.

The reverse implications are asymmetric. If $g∘f$ is injective, then $f$ must be injective: a collision for $f$ survives the outer map. If $g∘f$ is onto, then $g$ must be onto: every composite output is also an output of $g$. Neither conclusion alone says the other factor has the corresponding property.

The sharper statements are:

<div class="formula-block">g ∘ f is injective ⇔ f is injective and g restricted to f[A] is injective.<br>g ∘ f is surjective ⇔ g[f[A]] = C.</div>

For the first equivalence, necessity for the restricted map follows by writing two image elements as $f(u),f(v)$ and invoking injectivity of the composite and then equality of the resulting inputs. Sufficiency follows by applying restricted injectivity, then injectivity of $f$. The second equivalence is simply the composite image. A bijective composite gives a bijection from $A$ onto $f[A]$, then a bijection from $f[A]$ onto $C$, while unused elements of $B$ may destroy surjectivity of $f$ or injectivity of $g$ on the whole middle set.

<!-- FIGURE:composition -->

### Cancellation is a quantified property

If $g$ is injective and $g∘f=g∘h$ for maps $f,h:X→B$, then at each input, equality after $g$ forces $f(x)=h(x)$; thus $f=h$. If $g$ is not injective, choose distinct $b_1,b_2$ with equal $g$-values. The two constant maps from a singleton into these points are different and become equal after $g$. Therefore injectivity is equivalent to left cancellation against all suitably typed maps.

If $f$ is onto and $g∘f=h∘f$ for maps $g,h:B→C$, then for any $b∈B$ choose $a$ with $f(a)=b$; the equality at $a$ gives $g(b)=h(b)$. If $f$ misses $b_0$, two maps to ${0,1}$ can agree everywhere except at $b_0$, so they agree after $f$ but differ. Surjectivity is equivalent to right cancellation against all suitably typed maps. A fixed one-element target cannot distinguish two maps, so the phrase “all suitably typed maps” is essential in the converse.

## Inverses, sections, and retractions

### The converse relation and the true inverse

The converse graph reverses every pair of $Γ_f$. It is single-valued exactly when $f$ is injective, and total on $B$ exactly when $f$ is onto. Thus it is a total function $B→A$ precisely when $f$ is bijective. The true inverse $f^{-1}:B→A$ satisfies both $f^{-1}∘f=id_A$ and $f∘f^{-1}=id_B$. A reciprocal $1/f(x)$ is a numerical operation and has no general relationship to this inverse.

**Full inverse theorem.** If $k:B→A$ satisfies both identities, apply $k$ to any equality $f(u)=f(v)$ to obtain $u=v$, proving injectivity. For an arbitrary $b∈B$, the input $k(b)$ has output $b$, proving surjectivity. Conversely, if $f$ is bijective, each $b$ has exactly one antecedent. Define $k(b)$ to be that antecedent. Then $f(k(b))=b$, and the unique antecedent of $f(a)$ is $a$, giving $k(f(a))=a$. This definition involves uniqueness, not arbitrary choices among several candidates.

The inverse is unique. If $k$ and $ℓ$ are true inverses, associativity and the identities give $k=k∘id_B=k∘(f∘ℓ)=(k∘f)∘ℓ=id_A∘ℓ=ℓ$. Either missing identity prevents this argument. A bijection's inverse is a bijection, and $(f^{-1})^{-1}=f$.

For bijections $f:A→B$ and $g:B→C$, the inverse of $g∘f$ is $f^{-1}∘g^{-1}$. Check both compositions: reversing first undoes $g$ and then $f$. The identity at $A$ and the identity at $C$ result. The order reversal is forced by the types as well as by the algebra.

### One-sided inverses and all empty cases

A left inverse $ℓ:B→A$ satisfies $ℓ∘f=id_A$. It implies injectivity, but need not imply surjectivity. If an injection has $A≠∅$, define $ℓ$ by the unique antecedent on $f[A]$, and assign a fixed $a_0∈A$ at every target outside the image. This constructs a left inverse. If $A=∅$ and $B≠∅$, the injection has no total left inverse because no map $B→∅$ exists. If both sets are empty, its unique inverse is available.

A right inverse $r:B→A$ satisfies $f∘r=id_B$. It implies surjectivity and chooses one representative from each fiber. For finite carriers, every onto map has a right inverse by selecting one element in each nonempty fiber. For arbitrary sets, the general assertion that all onto maps admit such simultaneous selections is equivalent to the axiom of choice. An explicit selector, or well-ordered fibers with specified least elements, suffices for a particular map. Bijective inverses require no arbitrary selector.

For a finite nonempty-domain injection, each value of a left inverse outside the image is free. There are $m^{n−m}$ left inverses when $m=|A|>0$ and $n=|B|$. For a finite onto map, the number of right inverses is the product of its fiber sizes. The choices are independent across targets. A left inverse of a function is onto, since it attains every $a$ at $f(a)$; a right inverse is injective, since applying $f$ distinguishes its chosen representatives. If a left inverse and a right inverse both exist, they coincide: $ℓ=ℓ∘(f∘r)=(ℓ∘f)∘r=r$.

### Involutions and idempotent endofunctions

An involution $f:A→A$ satisfies $f∘f=id_A$, hence is its own true inverse and is bijective. Its finite cycles have length one or two. An idempotent endofunction satisfies $p∘p=p$. For any attained value $b=p(a)$, the identity gives $p(b)=b$; therefore its image is precisely its fixed-point set. It projects onto that image. If an idempotent map is injective, cancelling $p$ from $p∘p=p∘id_A$ yields $p=id_A$. If it is onto, every point is an attained value and hence fixed, with the same conclusion. Idempotence alone gives neither property on the whole carrier.

## Images, preimages, and the algebra of subsets

### Three operations that must not be conflated

For $S⊆A$ and $T⊆B$, define the direct image $f[S]={f(a):a∈S}$ and the preimage $f^{-1}[T]={a∈A:f(a)∈T}$. Image moves a subset forwards; preimage tests inputs against a target condition. A preimage exists for every function and target subset, including a noninjective or nonsurjective function. It is a set, not an inverse value. For example, if $f(x)=x^2$ on reals, $f^{-1}[{4}]={−2,2}$ although the declared real-to-real map has no inverse function.

Both operations preserve subset inclusion. The fundamental test connecting them is:

<div class="formula-block">f[S] ⊆ T ⇔ S ⊆ f<sup>−1</sup>[T].</div>

To prove it, translate the left side as “every value of an input in $S$ lies in $T$.” That is exactly the right side's assertion about membership of those inputs in the preimage. This equivalence is often a shorter route than separately manipulating both sides of a complicated set expression.

### Preimages preserve Boolean operations without bijectivity

For target subsets $T,U⊆B$, membership of an input in the preimage of a union means $f(a)∈T$ or $f(a)∈U$, which is membership in the union of their preimages. Replacing “or” by “and” proves the intersection identity. Negating membership proves the complement identity. The complete laws are:

<div class="formula-block">f<sup>−1</sup>[T ∪ U] = f<sup>−1</sup>[T] ∪ f<sup>−1</sup>[U]<br>f<sup>−1</sup>[T ∩ U] = f<sup>−1</sup>[T] ∩ f<sup>−1</sup>[U]<br>f<sup>−1</sup>[B ∖ T] = A ∖ f<sup>−1</sup>[T]<br>f<sup>−1</sup>[T ∖ U] = f<sup>−1</sup>[T] ∖ f<sup>−1</sup>[U].</div>

The same element argument handles arbitrary indexed unions and intersections. Empty indexed unions are empty, while empty indexed intersections mean the full declared ambient set; totality gives $f^{-1}[B]=A$ as required. No injection, surjection, or inverse-function hypothesis is used.

### Images preserve unions but can merge intersections and differences

Images preserve arbitrary unions: a value has an antecedent in a union precisely when it has an antecedent in at least one member. However $f[S∩U]⊆f[S]∩f[U]$ can be strict. On the right, one value may be reached by two different inputs, one in each set; neither input need belong to the intersection. If $f$ is injective, equal output witnesses must be the same input, so equality follows. Conversely, equality for every pair of subsets forces injectivity: singleton sets of distinct colliding inputs would make the right side nonempty and the left empty.

For differences, the unconditional inclusion runs as follows:

<div class="formula-block">f[S] ∖ f[U] ⊆ f[S ∖ U].</div>

If an output belongs to $f[S]$ but not $f[U]$, its witness in $S$ cannot lie in $U$. The reverse inclusion fails when an input outside $U$ shares its output with one inside $U$. Injectivity restores equality for all $S,U$ and is necessary for that universal equality. Images of complements satisfy $B∖f[S]⊆f[A∖S]$ when $f$ is onto, but equality for every $S$ requires bijectivity; the universally valid image formula is $f[A∖S]$ itself, without assuming it is a complement of $f[S]$.

### Round trips, saturation, and exact recovery

Every input in $S$ maps into $f[S]$, so $S⊆f^{-1}[f[S]]$. This round trip contains every fiber touched by $S$, not merely the chosen original inputs. It is the saturation of $S$. Equality holds precisely when $S$ is a union of entire fibers; equality for every subset holds precisely when $f$ is injective. For $T⊆B$, an output is attained by an input mapping into $T$ precisely when it is both in $T$ and in the image:

<div class="formula-block">f[f<sup>−1</sup>[T]] = T ∩ f[A].</div>

Consequently the other round trip recovers $T$ exactly when $T⊆f[A]$, and recovers every target subset exactly when $f$ is onto. Saturation is extensive, monotone, and idempotent: after whole fibers have been filled, another pass changes nothing. Subsets of $f[A]$ correspond bijectively to saturated subsets of $A$ by these two operations.

<!-- FIGURE:saturation -->

For composition, $(g∘f)[S]=g[f[S]]$, while $(g∘f)^{-1}[T]=f^{-1}[g^{-1}[T]]$. Direct images follow the evaluation order; preimages reverse the chain because a target condition is pulled backward through the outer map first. These identities use only the definitions and compatible types.

## Quotients, products, and function spaces

### Kernel equivalence and the canonical factorization

Define $a∼a'$ when $f(a)=f(a')$. Equality of values is reflexive, symmetric, and transitive, so this is an equivalence relation. Its classes are the nonempty fibers. Let $q:A→A/∼$ send each input to its class. Define $b:A/∼→f[A]$ by $b([a])=f(a)$. Representatives in the same class have equal outputs, so the definition is well-defined. If two classes have equal $b$-values, their representatives are equivalent and the classes coincide, proving injectivity. Every image value has an antecedent, proving surjectivity. Let $i:f[A]→B$ be inclusion. Then $f=i∘b∘q$.

This separates information loss, relabeling, and unused targets: $q$ merges indistinguishable inputs, $b$ is an exact correspondence, and $i$ embeds the attained outputs in the declared target. For finite carriers, the number of nonempty fibers is exactly the image size. This factorization works for an empty domain as well: the quotient and image are both empty.

For an equivalence relation $R$ on $A$, a rule $h([a]_R)=f(a)$ into $B$ is well-defined exactly when $aRa'$ implies $f(a)=f(a')$. Necessity follows because equal classes must get equal outputs; sufficiency follows because any two representatives of a class give the same prescribed output. In that case $h∘q=f$, and onto-ness of $q$ makes $h$ unique. If the target is also a quotient by $S$, the weaker condition $aRa'⇒f(a)Sf(a')$ suffices, since only target classes, not literal output representatives, must agree.

<!-- FIGURE:factorization -->

### Product, tagged union, indicator, and currying constructions

A two-input rule is formally a function on a Cartesian product. A binary operation on $A$ is a function $A×A→A$, so closure in the codomain is part of its definition. Associativity, commutativity, identity, and idempotence are separate properties. Function composition on the set of endofunctions of $A$ is an associative binary operation with identity $id_A$; bijections form its invertible part.

Write $B^A$ for the set of all functions from $A$ to $B$. The exponential notation is justified by finite counts, not by treating a function as a real power. A function $A→B×C$ is equivalent to a pair of functions $A→B$ and $A→C$: take its two coordinates, or pair the outputs. A function on a tagged union $A⊔B$ is equivalent to a pair of functions with the two component domains and the same target; the tags keep overlapping underlying sets distinct.

Currying gives a bijection between $C^{A×B}$ and $(C^B)^A$. Given $u:A×B→C$, set $v(a)(b)=u(a,b)$. For each fixed $a$, the result is a function $B→C$, so $v$ has the stated function-valued target. Conversely set $u(a,b)=v(a)(b)$. Both transformations undo each other pointwise, including empty-set cases. This is a reorganization of inputs, not a mysterious arithmetic identity.

Each subset $S⊆A$ has an indicator $χ_S:A→{0,1}$ equal to one on $S$ and zero outside it. Its set of one-valued inputs recovers $S$, so $𝒫(A)$ is in bijection with ${0,1}^A$. Pointwise multiplication corresponds to intersection; pointwise maximum corresponds to union; $1−χ_S$ corresponds to complement. On finite coordinate sets this also identifies a subset with a Boolean vector. The product order on those vectors corresponds to subset inclusion in both directions.

## Counting finite functions and inverse choices

### Unrestricted maps, injections, bijections, and partial maps

Let $m=|A|$ and $n=|B|$ be nonnegative integers. For each of the $m$ labeled inputs, there are $n$ choices, independent of all others. Thus the total number of functions is $n^m$. In this combinatorial expression $0^0=1$: there is one empty map from the empty set to itself. If $m>0,n=0$, the count is zero. A partial function gives each input $n+1$ possibilities, including undefinedness, so there are $(n+1)^m$ partial functions.

For an injection, successive inputs have $n,n−1,…,n−m+1$ choices when $m≤n$. The count is $n!/(n−m)!$, with the empty product equal to one. It is zero when $m>n$. For two finite sets of equal size $m$, the bijection count is $m!$. If their sizes differ, it is zero. This includes the unique empty bijection through $0!=1$.

If each input $a_i$ is independently restricted to an allowed subset $T_i⊆B$, the count is the product of the allowed-set sizes. Requiring distinct outputs breaks independence: multiply successively adjusted choices only when symmetry justifies it, or use a matching argument. A bound on the count of choices is not a guarantee that an assignment satisfying all coupled requirements exists.

### Surjections, image size, and inclusion–exclusion

For each target $b$, let $E_b$ be the event that the function misses $b$. If a chosen collection of $j$ targets is forbidden, there are $(n−j)^m$ remaining maps. Inclusion–exclusion therefore gives:

<!-- MATH:onto -->

The binomial coefficient chooses which targets are missing. The alternating sum removes maps missing one target, restores maps removed twice, and continues until each nonsurjective map has net coefficient zero. A surjective map has net coefficient one because it belongs to no missing-target event. This proof also handles empty carriers using the combinatorial exponent convention. For $m=0,n>0$, the alternating binomial sum is zero; for $m=n=0$, the sole term is one.

An alternative description partitions the domain into $n$ nonempty unlabeled fibers, then assigns the $n$ distinct target labels to the blocks. Thus the onto count is $n!S(m,n)$, where $S(m,n)$ is a Stirling number of the second kind, not a function permutation count. To derive its recurrence, inspect the last labeled input. It is either a singleton block, leaving $S(m−1,n−1)$ partitions, or joins one of $n$ blocks of a partition of the other inputs, giving $nS(m−1,n)$. Set $S(0,0)=1$, $S(m,0)=0$ for positive $m$, and $S(0,n)=0$ for positive $n$.

For exactly $k$ distinct attained targets, choose the image subset in $\binom{n}{k}$ ways, then count onto maps to it. Hence the count is $\binom{n}{k}k!S(m,k)$ for $0≤k≤min(m,n)$. For a specified list of fiber sizes $r_1,…,r_n$ summing to $m$, the count is $m!/(r_1!⋯r_n!)$: choose which labeled inputs occupy each labeled fiber. Empty fibers are permitted unless onto-ness is required.

### Finite function analysis as an algorithm

Represent a function from ${0,…,m−1}$ to ${0,…,n−1}$ by a length-$m$ sequence of target indices. The following routine checks validity before classifying it. It returns the fibers rather than just a Boolean answer, because they are certificates: a large fiber gives a collision, and an empty one gives a missed target.

```python
def analyze_function(values, target_size):
    if type(target_size) is not int or target_size < 0:
        raise ValueError("The target size must be a nonnegative integer.")
    fibers = [[] for _ in range(target_size)]
    for source, target in enumerate(values):
        if type(target) is not int or not 0 <= target < target_size:
            raise ValueError("Every input must have a valid target index.")
        fibers[target].append(source)
    injective = all(len(fiber) <= 1 for fiber in fibers)
    surjective = all(len(fiber) >= 1 for fiber in fibers)
    inverse = [fiber[0] for fiber in fibers] if injective and surjective else None
    return fibers, injective, surjective, inverse
```

The loop invariant states that after processing the first $k$ inputs, each fiber contains exactly those processed inputs with its target value. It holds initially because no input has been processed; one append preserves it; termination gives the exact fibers. The predicates implement the definitions, and a bijection has exactly one representative per target, so the returned inverse is correct. The running time and storage are both $O(m+n)$, counting target-list initialization. An invalid output raises an error and is not silently classified. For two empty carriers the inverse is an empty list, which is a legitimate inverse rather than the absence marker `None`.

## Infinite maps and cardinality constructions

### Cardinal comparisons and explicit enumeration

Two sets have equal cardinality when a bijection exists between them. An injection establishes a cardinal upper bound for its domain. A countable set is finite or admits a bijection with $ℕ$. Equivalently, it admits an injection into $ℕ$. A nonempty countable set also admits a surjection from $ℕ$; the empty set is an exception to this last formulation. For infinite sets, proper subsets can have the same cardinality as the whole set: shifting naturals supplies a direct example.

The piecewise map from $ℤ$ to $ℕ$ that sends a nonnegative integer $z$ to $2z$ and a negative integer $z$ to $−2z−1$ is a bijection. Even targets recover $z=k/2$ and odd targets recover $z=−(k+1)/2$. The parities separate the two branches. For pairs of nonnegative naturals, a particularly useful map is $p(x,y)=2^x(2y+1)−1$. Every target plus one has a unique factorization into a power of two and an odd factor, giving exactly one pair. This proves that a two-dimensional infinite grid can be enumerated by one natural-number coordinate without skipping or duplicating points.

Every rational has a unique reduced fraction with positive denominator. The numerator lies in $ℤ$ and the denominator in $ℕ_+$, so sending the fraction to that pair is injective. Encode both coordinates into naturals and use the pairing map. Thus rationals are countable. No enumeration may count different unreduced fractions as different rational numbers.

### Schröder–Bernstein with a complete construction

**Theorem.** If $u:A→B$ and $v:B→A$ are injective, there exists a bijection $A→B$. The theorem does not assert that either original injection is onto.

Define $A_0=A∖v[B]$, $A_{k+1}=v[u[A_k]]$, and let $H$ be the union of all these layers. On $H$, set $h(a)=u(a)$. Outside $H$, the input cannot lie in $A_0$, so it lies in $v[B]$ and has a unique antecedent under the injection $v$; set $h(a)=v^{-1}(a)$ there, where the inverse is restricted to $v[B]$.

Each branch is injective. They cannot collide: if $u(a)=v^{-1}(a')$ with $a∈H$ and $a'∉H$, then $a'=v(u(a))$ belongs to the next layer of $H$, a contradiction. To prove onto-ness, choose $b∈B$. If $b∈u[H]$, the first branch reaches it. Otherwise consider $a=v(b)$. If $a∈H$, it cannot lie in $A_0$; it would be $v(u(x))$ for some $x∈H$ in an earlier layer. Injectivity of $v$ would imply $b=u(x)∈u[H]$, contradicting the case assumption. Hence $a∉H$, and the second branch sends it to $b$. This proves both defining properties without a choice among multiple antecedents.

### Cantor's theorem and diagonalization

For any set $A$, the singleton map $a↦{a}$ injects $A$ into $𝒫(A)$. No function $F:A→𝒫(A)$ is onto. To see this, form $D={a∈A:a∉F(a)}$. If $F$ were onto, there would be $d$ with $F(d)=D$. Then $d∈D$ is equivalent to $d∉F(d)=D$, a contradiction. This argument also handles the empty set: its power set contains the empty subset, whereas the empty-domain map reaches nothing. A diagonal construction disproves a proposed exhaustive indexing, rather than merely showing that one attempted list was inconvenient.

The indicator correspondence transfers this result to binary sequences: ${0,1}^ℕ$ is uncountable. Given any proposed sequence list, change the $n$th bit of its $n$th entry to produce a binary sequence absent from that list. There is no decimal-expansion ambiguity in this binary-sequence argument. For real-number encodings, use an explicitly unique representation or a separated digit construction, as in Problem 31.

Countability of the union of a countable family of countable sets is used in the usual setting where enumerations for the members can be chosen. Encoding an element by the least enumerated member that contains it and its index inside that member proves the bound when those enumerations are given. Arbitrary simultaneous choices introduce foundational assumptions; the elementary explicit constructions in this chapter name their encodings instead of hiding them.

## Fully worked problem bank

<!-- INCLUDE:problems -->

## Chapter summary and examination decisions

<!-- INCLUDE:review -->

## Interactive fiber laboratory

The laboratory below analyzes finite total functions. Choose one output for each of four labeled inputs, then inspect the fibers, collision witnesses, missed targets, saturation, and inverse eligibility. Use the presets to compare a bijection, an onto map with collisions, and an injection with an unused target. The selected subset demonstrates why a direct-image/preimage round trip can add inputs. It does not administer an assessment or record a performance score.

<!-- LAB:functions -->

## References and chapter review status

1. Andrew D. Ker. University of Oxford, Discrete Mathematics, Michaelmas 2010. Chapter 2, pp. 17–30. [Lecture notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf).
2. Keith Schwarz. Stanford University, CS103, Spring 2017. [Lecture 08: Functions](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/08/Small08.pdf), instructional pp. 1–37 and 46–76; [Problem Set 3](https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/handouts/150%20Problem%20Set%203.pdf), Problems 6–8 and extra credit, pp. 5–6.
3. Peter Robinson. University of Cambridge, Discrete Mathematics, Michaelmas 2003 / Lent 2004 edition, printed pp. 44–49. [Functions, cardinality, and exercises](https://www.cl.cam.ac.uk/teaching/2003/DiscMaths/DiscMaths.pdf).
4. Eric Lehman, F. Thomson Leighton, and Albert R. Meyer. MIT 6.042J, Fall 2010; instructors Tom Leighton and Marten van Dijk. [Chapter 7](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/efac321fdc8d0b27586ca35b04aab808_MIT6_042JF10_chap07.pdf), §7.1.5 and §§7.2.1–7.2.2, pp. 217–220.
5. Shaun Allison. Carnegie Mellon University, 21-127 Concepts of Math, Summer I 2018. [Assignment 5](https://www.math.cmu.edu/~sallison/concepts18/assignment5.pdf), Questions 1–7.
6. Michael George. Cornell University, CS2800, Spring 2017. [Lecture 4: proofs and functions](https://www.cs.cornell.edu/courses/cs2800/2017sp/lectures/lec04-functions.html).

This chapter has been approved by the student. The source ledger distinguishes genuinely read texts from catalogue-only candidates. Mathematical checks include independent finite enumeration and worked-example calculations; presentation checks inspect equations, semantic indices, diagrams, mobile layout, and print styles. Finite tests supplement the general proofs and cannot establish a universal guarantee. Iranian exam calibration remains deferred to the final month.
