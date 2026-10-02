### Integrated summary

A function first passes a validity test: every declared input must receive exactly one output inside the declared target. Its nonempty fibers partition the domain. Injection limits fiber size, surjection prohibits empty target fibers, and bijection combines those conditions. A true inverse exists exactly for a bijection and reverses both the graph and the order of a composite. A one-sided inverse enforces only the property relevant to its side, with an explicit empty-domain exception for left inverses and a choice qualification for arbitrary onto maps.

Composition sees only the middle values attained by its inner factor. This explains why a composite can be bijective even when neither factor is. A function factors canonically through its fiber quotient, a bijection to its image, and an inclusion into its codomain. Images can merge information; preimages transfer target conditions back to inputs and preserve Boolean set operations. An image/preimage round trip either fills touched fibers or removes unattained targets.

Finite counts follow from independent output choices, distinct-output choices, or nonempty labeled fibers. Inclusion–exclusion counts onto maps by excluding missed targets. For infinite sets, explicit encodings replace finite-size subtraction, and injective maps in both directions imply a bijection by the Schröder–Bernstein construction. Cantor's diagonal argument prohibits an exhaustive indexing of a power set by its underlying set.

### A decision table for examination problems

| What the question asks | First action | Required evidence | Frequent failure |
|---|---|---|---|
| Is the prescription a function? | Check domain coverage, agreement on overlapping branches, and target membership. | A unique valid output for every declared input. | Classifying an invalid square-root or reciprocal declaration. |
| Is it injective? | Assume equal outputs or seek a collision. | A universal equality argument or two distinct colliding inputs. | Confusing one output per input with one input per output. |
| Is it onto? | Start with an arbitrary target. | An antecedent in the domain for every target, or a missed-target witness. | Solving an equation but ignoring its input restrictions. |
| Does a true inverse exist? | Prove both injection and onto-ness. | Both identity compositions and correct reversed types. | Accepting a single identity or taking a reciprocal. |
| What follows from a composite property? | Examine the inner image. | Collision persistence or $g[f[A]]=C$. | Inferring both factors have every property of the composite. |
| Is a quotient formula well-defined? | Change the representative within one class. | Equal output classes for equivalent input representatives. | Giving a formula without testing representative independence. |
| Is an image set identity valid? | Translate membership with explicit witnesses. | Equal witnesses under injectivity, where required. | Assuming all image laws behave like preimage laws. |
| How many maps exist? | Identify labeled domain, labeled target, and all constraints. | Independent choices, fiber partitions, or inclusion–exclusion. | Dividing by permutations even when target labels matter. |
| Is an infinite family countable? | Build an injection into naturals or encode an uncountable subfamily. | A fully specified encoding with injectivity proof. | Treating an infinite set like a finite-size equation. |

### Seventy-two complete high-yield rules

These are mathematical examination rules, not frequency claims based on deferred Iranian archives. Each rule states its needed scope; the lesson and worked bank explain the proofs.

1. A total function must assign exactly one codomain member to every declared input, so a missing value or an out-of-target value makes the declaration invalid.
2. Two different inputs may share one output without violating the function axiom; that sharing concerns injectivity instead.
3. The same formula can have different injection, onto, and inverse properties after its domain or codomain changes.
4. Equality of typed functions requires matching domains, matching codomains, and matching outputs at every input.
5. An empty-domain function exists uniquely into each fixed target and is injective even when that target is nonempty.
6. A total function from a nonempty domain into an empty target does not exist.
7. The empty map from the empty set to itself is a bijection, an identity, and its own inverse.
8. The image consists of attained targets and must be distinguished from the entire declared codomain.
9. A domain restriction preserves injectivity if it was present, but may remove targets needed for onto-ness.
10. Corestricting to the image makes the map onto and preserves all collisions; it is not a repair for noninjectivity.
11. A piecewise definition is valid only when its branches cover the domain and agree wherever their input conditions overlap.
12. Simplification of an expression does not retroactively define values excluded by its original denominator or radical.
13. A partial function becomes total by mapping undefined inputs to a fresh sentinel outside the original target.
14. Strict monotonicity on a totally ordered domain proves injectivity, while ordinary monotonicity can allow constant stretches.
15. The defining floor inequality is $⌊x⌋≤x<⌊x⌋+1$, including for negative inputs.
16. The defining ceiling inequality is $⌈x⌉−1<x≤⌈x⌉$, so its integer fibers have the opposite endpoint convention from floor fibers.
17. To prove injectivity algebraically, start with two arbitrary domain inputs having equal outputs and use only justified operations to obtain equal inputs.
18. To disprove injectivity, name two distinct permitted inputs and calculate their common output explicitly.
19. To prove onto-ness, construct an input for an arbitrary codomain target and verify that the input respects every domain restriction.
20. To disprove onto-ness, name an actual codomain target and prove that no permitted input reaches it.
21. A fiber over an unused target is empty, while the nonempty fibers partition the entire domain.
22. Injection means every target fiber has at most one element; onto-ness means every target fiber has at least one element.
23. For finite carriers, injection implies $m≤n$ and onto-ness implies $m≥n$, but neither inequality classifies every assignment.
24. When finite domain and target have equal size, injectivity, onto-ness, and bijectivity are equivalent.
25. For an infinite endofunction, injection need not imply onto-ness, and onto-ness need not imply injection.
26. In $g∘f$, the inner map $f$ acts first, and the composite has the inner domain and outer codomain.
27. A formula composite is defined exactly where its inner value lies in the domain of the outer rule, not merely where both written expressions look familiar.
28. Composition is associative with compatible types; it is generally noncommutative and the reverse order may be ill-typed.
29. Two injections compose to an injection, and two onto maps compose to an onto map.
30. If a composite is injective, its inner factor must be injective because an inner collision cannot be undone.
31. If a composite is onto, its outer factor must be onto because every composite output is an outer output.
32. A composite is injective precisely when its inner factor is injective and its outer factor is injective on the attained middle subset.
33. A composite is onto precisely when its inner image meets enough outer fibers to attain every final target.
34. A bijective composite need not make either factor bijective on its full declared sets; unused middle points supply counterexamples.
35. If a composite is bijective and its inner factor is onto, both factors are bijective.
36. If a composite is bijective and its outer factor is injective, both factors are bijective.
37. An injective outer map can be cancelled from the left of a composition equality by applying its defining property pointwise.
38. An onto inner map can be cancelled from the right because every middle input is tested by at least one original input.
39. The converse cancellation characterizations quantify over all suitably typed maps; a fixed singleton target cannot distinguish differing maps.
40. A reversed graph is a total inverse function exactly when the original function is bijective.
41. A true inverse must satisfy both identity compositions with the correctly named source and target identities.
42. Solving $y=f(x)$ is only a candidate inverse construction until the resulting input type and both identities have been checked.
43. The inverse of a composite of bijections reverses the order: $(g∘f)^{-1}=f^{-1}∘g^{-1}$.
44. A true inverse is unique, whereas one-sided inverses may vary at unused targets or among alternate fiber representatives.
45. A left inverse forces injection and is itself onto; it need not undo every target value in the right-hand identity.
46. A right inverse forces onto-ness and is itself injective; it need not recover every original input in the left-hand identity.
47. An injection with a nonempty domain has a left inverse, but the injection from an empty domain to a nonempty target does not.
48. A finite onto map has a right inverse by choosing one representative in each fiber; the arbitrary-set universal version uses the axiom of choice.
49. If a left inverse and a right inverse both exist, they coincide and give the unique true inverse.
50. An involution is bijective because its own composition with itself is the identity; its finite cycles have length one or two.
51. An idempotent map fixes exactly its image, and injectivity or onto-ness of an idempotent endofunction forces it to be the identity.
52. Preimage notation applies even when no inverse function exists, and the preimage of one target value may contain several inputs.
53. Preimages preserve unions, intersections, differences, and complements relative to the declared domain and codomain without a bijection hypothesis.
54. Direct images preserve unions, but equal-image witnesses in different subsets need not be the same input.
55. For intersections, the universal inclusion is $f[S∩T]⊆f[S]∩f[T]$, and equality for every pair of subsets characterizes injectivity.
56. For differences, the universal inclusion is $f[S]∖f[T]⊆f[S∖T]$, and injectivity restores equality.
57. The input round trip $f^{-1}[f[S]]$ fills every fiber touched by $S$ and equals $S$ exactly when $S$ is saturated.
58. Every input subset is recovered by its round trip exactly when the function is injective.
59. The target round trip satisfies $f[f^{-1}[T]]=T∩f[A]$, so it removes precisely the unused targets of $T$.
60. Every target subset is recovered by its round trip exactly when the function is onto.
61. The equivalence $f[S]⊆T⇔S⊆f^{-1}[T]$ is a direct membership translation and often shortens subset proofs.
62. A quotient formula must preserve the chosen input equivalence into the chosen output equivalence; literal equality is required only when the target has no quotient.
63. A function's kernel classes correspond bijectively to its attained outputs, and a finite image with $k$ points gives exactly $2^k$ saturated input subsets.
64. Currying reorganizes a function on a product into a function with function-valued outputs; it does not justify arbitrary reassociation of exponential expressions.
65. Maps on a tagged union correspond to pairs of maps on its components, and the tags must be retained when the underlying sets overlap.
66. There are $n^m$ total maps and $(n+1)^m$ partial maps between finite carriers of sizes $m,n$, using the empty-map convention $0^0=1$.
67. The injection count is the falling product of $m$ distinct target choices when $m≤n$, and is zero otherwise; the equal-size bijection count is $m!$.
68. Onto counts require every target fiber nonempty, so inclusion–exclusion or $n!S(m,n)$ is appropriate rather than the unrestricted power count.
69. To count exactly $k$ attained targets, first choose their labels and then count onto maps to that selected image.
70. Left-inverse counts depend on free unused-target values, while right-inverse counts are products of independent nonempty fiber sizes.
71. For infinite cardinality, construct an explicit injection or bijection; injections in both directions guarantee a bijection by Schröder–Bernstein without making either original map onto.
72. Cantor's diagonal set differs from every proposed indexed subset at its own index, proving that no map from a set onto its power set can exist.

### Reading the evidence correctly

The course ledger records the actual texts used; a discovered course is not silently counted as a reviewed course. The worked-bank ledger maps the relevant listed exercises to complete solutions. The general proofs establish the stated mathematical results; finite enumeration checks catch boundary or implementation errors but are not substitutes for those proofs. The rules above are examination-oriented mathematical guidance. Claims about the distribution of actual Iranian exam questions await the final-month analysis requested by the student.
