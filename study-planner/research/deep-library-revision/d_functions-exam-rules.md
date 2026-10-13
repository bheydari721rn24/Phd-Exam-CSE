## Chapter summary and detailed examination decisions

Throughout this section, m is the finite domain size and n the finite codomain size. These meanings do not change between formulas. A summary supports the full proofs; it does not replace them. The rules describe mathematical applicability rather than an unmeasured frequency of examination appearances.

### 1. Validate a prescription before classifying it

A total declaration $f:A\to B$ requires exactly one B-output for every A-input. The rule $x\mapsto1/x$ on all reals fails at zero; the square-root rule on a real domain fails at negative inputs. Calling either declaration noninjective does not address this validity failure. Repair the domain or rule explicitly before discussing its image.

### 2. Include all empty-type cases

An empty-domain function into each fixed B is unique and injective. It is onto only when B is empty. A nonempty A has no total map into an empty B. Thus total-map counts use the combinatorial convention $0^0=1$, reflecting the unique empty graph. A left inverse of $\varnothing\to\{b\}$ would have an impossible reverse type.

### 3. Domain and codomain belong to the function

The square rule on reals to reals has collisions and misses negative targets. Restricted to nonnegative reals and corestricted to nonnegative reals it is bijective. Changing the codomain affects onto-ness, while changing the domain may eliminate collisions or outputs. The formula alone does not determine the answer. Equal typed functions must also have matching declared types.

### 4. Use fibers as certificates

The fibers $F_b=\{a:f(a)=b\}$ are disjoint and cover A. An oversized fiber certifies a collision; an empty target fiber certifies a missed target. Injection means sizes at most one, surjection sizes at least one. For output tuple (a,a,b,c) into {a,b,c,d}, the a-fiber has two members and the d-fiber none, certifying both failures.

### 5. State the finite-size hypothesis

For finite sets, injection implies m≤n and surjection m≥n. At m=n either property implies bijectivity. On infinite naturals, the shift n↦n+1 is injective and not onto, so the reverse implication fails. Equality of cardinalities asserts existence of some bijection; a specified constant map between equal finite carriers can still fail both properties.

### 6. Count total maps before imposing extra conditions

For labelled inputs and outputs, each of m inputs independently chooses one of n targets, giving $n^m$. Four inputs and three targets give $3^4=81$. No division by input or target permutations is justified because labels distinguish functions. This count includes collisions and missed targets; onto or injective conditions require separate counting.

### 7. Count injections with distinct choices

For m≤n, successive outputs have n,n−1,…,n−m+1 possibilities, giving $n!/(n-m)!$. If m>n the count is zero. Three inputs into eight targets give $8\cdot7\cdot6=336$. Choosing their image gives only $\binom{8}{3}=56$ sets; each admits 3!=6 assignments to the input labels. Equal-size bijections number m!.

### 8. Onto counts restore overlap

For positive m,n, onto maps number $\sum_{j=0}^n(-1)^j\binom nj(n-j)^m$. Omission events overlap at tuples missing several targets; subtracting them without restoration is wrong. Six inputs onto four targets give $4096-2916+384-4=1560$. Divide by 30 only if that is the requested transformed quantity; here the quotient is 52.

### 9. Image size is a two-stage choice

Exactly k attained targets give $\binom nk k!S(m,k)$. Choose the labelled image set and then require a surjection to it. Five inputs with three attained labels among four give $4(243-96+3)=600$. Choosing the image alone leaves outputs unspecified. Multiplying again by k! after an onto count already using labels would count those labels twice.

### 10. A prescribed fiber is selected and then excluded elsewhere

If one named target has exactly r antecedents, choose those inputs and keep that target unavailable at every remaining input: $\binom mr(n-1)^{m-r}$. With m=7,n=3,r=3 the result is $35\cdot16=560$. This does not require the other targets nonempty. Additional onto-ness changes the residual output count.

### 11. Fiber-size vectors carry target labels

For prescribed labelled sizes summing to m, the count is $m!/\prod r_j!$. A profile without assigned target labels needs a separate profile-assignment factor. For onto six-to-four maps, profiles (3,1,1,1) and (2,2,1,1) contribute 480 and 1080. Equal profile sizes do not make the input assignments unlabelled; never divide their multinomial count by n!.

### 12. Partial functions add a fresh undefined choice

An m-input, n-output partial function independently selects n outputs or undefinedness at each input, giving $(n+1)^m$. Exactly k defined inputs give $\binom mk n^k$. If n=0 the only partial map is everywhere undefined. A sentinel must lie outside the ordinary target, or a defined sentinel-valued output would be confused with undefinedness.

### 13. Monotone maps are multiplicity vectors

Weakly increasing maps from m ordered inputs into n ordered values correspond to n nonnegative counts summing to m. They number $\binom{m+n-1}{n-1}$ for n>0. With m=n=5 the result is $\binom94=126$. Repeated values and unused targets are permitted. Treating the outputs as distinct would solve a strict-increase problem instead.

### 14. Endpoint conditions consume only their own compulsory occurrences

For m,n≥2, first output 1 and last output n require positive multiplicities for those two labels, giving $\binom{m+n-3}{n-1}$. With m=6,n=4 this is $\binom73=35$. Interior values need not occur. If all outputs are required, positive counts for every label give $\binom{m-1}{n-1}$ when m≥n.

### 15. Strict monotonicity has different finite and infinite consequences

Strictly increasing finite-chain maps choose distinct targets and number $\binom nm$. A strict self-map of a finite chain must be the identity. On integers, x↦x+1 preserves strict order and is not the identity. It still is injective. Retain the source statement's distinction between identity and injection and its absence of a finite-carrier hypothesis.

### 16. Follow the inside map first

For $f:A\to B$ and $g:B\to C$, the rule is $(g\circ f)(a)=g(f(a))$. Its source is A and target C. With f(x)=x+1 and g(x)=2x the two orders give 2x+2 and 2x+1. The inverse of a composite of bijections reverses this order. Composition is associative with compatible types, generally not commutative.

### 17. A rule composite must preserve the outer domain

For f(x)=x²−1 and g(t)=1/t, the composite excludes x=−1 and x=1. Simplification does not create a value at either point. More generally its allowable inputs satisfy f(x) in the domain of g. If declared intermediate types do not match but the inner image lies in the outer domain, insert the required restriction or corestriction explicitly.

### 18. A composite sees only the attained middle values

Composite injection forces f injective; composite onto-ness forces g onto. The stronger exact tests are injection of f and of g on f[A], or $g[f[A]]=C$ respectively. An unused middle point can participate in a g-collision without spoiling the composite. Thus a bijective composite does not automatically make both factors bijective on their full types.

### 19. Extra composition hypotheses recover the missing implication

If the composite is bijective and f is onto, g's potential collisions can all be lifted to A and are excluded by composite injection. Both factors become bijective. If the composite is bijective and g injective, its onto-ness forces every B-point into f[A], again giving both bijections. Name the additional hypothesis instead of applying either theorem to arbitrary maps.

### 20. Cancellation is universally quantified

An injective outer g can be cancelled from $g\circ f=g\circ h$. An onto inner f can be cancelled from $g\circ f=h\circ f$. Converse characterizations compare all appropriately typed maps. A missed middle point hides a difference between outer maps; a collision hides a difference between inner maps. Equality for one pair of maps does not itself prove the cancelling function has the required property.

### 21. A true inverse requires both identities

An inverse $h:B\to A$ satisfies $h\circ f=\operatorname{id}_A$ and $f\circ h=\operatorname{id}_B$. Solving y=f(x) supplies a candidate, which still needs correct types and both verifications. For x≤2 and f(x)=(x−2)²+3, the valid inverse branch is $2-\sqrt{y-3}$ on y≥3. A reciprocal and a preimage set are different operations.

### 22. Left inverses have unused-target freedom

For an injection with m>0, a left inverse is forced on f[A] but has m choices on each unused target. Thus its count is $m^{n-m}$. A three-to-five injection has nine left inverses. These reverse maps are onto A, but generally not inverse to f in the other direction. For an empty domain and nonempty target no reverse total map exists.

### 23. Right inverses select one input from each fiber

A section of a fixed finite surjection has count $\prod_b|F_b|$. Fibers 2,3,4 give 24 sections. Each section is injective because different targets have disjoint fibers. A section does not make the original f injective or recover unchosen antecedents. A missing fiber gives zero choices and forbids a right inverse.

### 24. Count split pairs with both factors present

For m>0 and n≥m, pairs with $g\circ f=\operatorname{id}_A$ number $n!/(n-m)!\,m^{n-m}$. Two inputs and four middle targets give 48 pairs. The first factor chooses the injection and the second its free reverse values. Reversing the identity reverses the finite size condition. Requiring both identities gives only bijective pairs with a unique reverse map.

### 25. Idempotence fixes precisely the image

If $f^2=f$ and y=f(x), then f(y)=y. Conversely a fixed y belongs to the image. For exactly k image points on n nonempty labelled points, choose them and map every other input to one of them: $\binom nk k^{n-k}$. Two fixed points on five labels give $10\cdot8=80$. Two image values without idempotence need not be fixed.

### 26. Count all idempotents by disjoint image sizes

Sum $\binom nk k^{n-k}$ for k=1,…,n on a nonempty carrier. For n=4 the contributions are 4,24,12,1, totalling 41. An empty image is impossible for a nonempty total domain. The empty carrier instead has one empty idempotent map. An idempotent injection or an idempotent surjection must be the identity, but idempotence alone gives neither property.

### 27. Involutions allow only cycles of lengths one and two

The squared identity makes every orbit length divide two. With j transpositions on n labels, the count is $n!/[2^j j!(n-2j)!]$. Two transpositions on eight labels give 210; exactly two fixed points there instead means three transpositions and gives 420. Within-pair order and pair order are immaterial, while all labels remain distinguished.

### 28. Cyclic rotations are displays of the same function

A single cycle on n≥1 labelled points has (n−1)! arrangements: fix one start and order the remaining labels. For n=5 this is 24. Dividing n! by n removes redundant starting positions. Reversing a cycle of length at least three changes its successor function, so another universal division by two would be wrong. Length one and two are the reversal exceptions.

### 29. Specified fixed points are not exactly fixed points

Fixing two named points on n≥2 labels leaves (n−2)! residual permutations, with further fixed points permitted. Exactly two named fixed points instead requires a derangement on the residual labels. Exactly two unspecified fixed points adds the choice factor $\binom n2$. On five labels the first task gives six maps; the identity is among them and demonstrates why further fixed points cannot be excluded.

### 30. Direct images can merge different witnesses

Images preserve unions always. They satisfy $f[X\cap Y]\subseteq f[X]\cap f[Y]$ and $f[X]\setminus f[Y]\subseteq f[X\setminus Y]$ unconditionally. Distinct inputs u,v with f(u)=f(v) make both inclusions strict for disjoint singleton sets. Injection restores equality for all such set pairs. The direction of the difference inclusion must not be reversed.

### 31. Preimages preserve Boolean operations for every total function

For T,U⊆B, preimages preserve union, intersection, difference and complement relative to B and A. They test the single value f(a), so no competing witnesses are needed. Even a many-to-one function has these laws. A preimage exists without a true inverse and may have several inputs; f(x)=x² gives preimage {−2,2} for target singleton {4}.

### 32. Round trips measure saturation and unattained targets

The input round trip $f^{-1}[f[S]]$ fills entire touched fibers; equality with S holds exactly for saturated S. The target round trip is $f[f^{-1}[T]]=T\cap f[A]$. A two-input a-fiber expands either of its singleton subsets; an unused target disappears from the target round trip. Universal recovery on the two sides characterizes injection and surjection respectively.

### 33. Power-set operators interchange one classification

The direct-image operator is injective exactly when f is injective, and onto exactly when f is onto. The preimage operator is injective exactly when f is onto, and onto exactly when f is injective. An unused target gives two distinct target subsets with the same preimage; a collision makes an individual colliding input impossible as an entire preimage. These statements classify the operators, not an inverse of f.

### 34. Quotient descent must respect every representative

A rule $[a]_R\mapsto[f(a)]_S$ is well-defined exactly when aRa′ implies f(a)Sf(a′). Literal output equality is stronger and unnecessary if the target is a quotient. For $[x]_4\mapsto[ax+b]_6$, the condition is $6\mid4a$, equivalent to 3 dividing a. Testing only the four selected representatives would overlook the equivalent pair 0,4 and cannot prove the condition.

### 35. Function spaces are constructed, not formally exponent-reassociated

Currying gives a bijection between $C^{A\times B}$ and $(C^B)^A$ by v(a)(b)=u(a,b). A map on a tagged union corresponds to a pair of component maps. But $C^{B^A}$ generally differs: for |A|=3 and |B|=|C|=2 its size is 256, while $(C^B)^A$ has size 64. Preserve the parentheses and actual input type.

### 36. Powers depend on cycle lengths and entry distances

For a nonempty finite endofunction let H be maximal cycle-entry distance and L the cycle-length least common multiple. A positive power f^k is idempotent exactly when k≥H and L divides k. In the tuple (1,2,2,4,3,4,5), H=L=2, so the square is idempotent; the third power still swaps a two-cycle. Reaching a cycle and fixing its phase are separate requirements.

### 37. Infinite encodings must be injective or surjective by proof

Decode $2^x(2y+1)-1$ by factoring z+1 into a power of two and an odd factor. This proves a bijection on zero-based natural pairs; replacing the exponent by multiplication destroys it. Schröder–Bernstein uses two injections to construct a new bijection, without making either original map onto. Finite examples of the layers illustrate its construction, while the general proof handles every input.

### 38. Distinguish a chosen enumeration from a given order

A bijective natural-number listing transports a well-order to any countably infinite set. The usual order on the integers still has no least element; countability does not make every existing order well-founded. Cantor's diagonal argument prohibits a surjection from A onto its power set, so no natural-number listing enumerates all binary sequences. These are existence and nonexistence statements with different quantifiers.
