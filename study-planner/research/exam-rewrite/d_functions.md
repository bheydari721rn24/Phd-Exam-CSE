## Teaching through formulas and conceptual decisions

### Count fibers before assigning inverse choices

A function from an$n$-element domain to an$m$-element codomain selects one of$m$ outputs independently for every input, giving$m^n$. Injectivity requires distinct outputs and gives$m!/(m-n)!$ if$n\le m$. Surjectivity requires nonempty fibers and is counted by inclusion-exclusion: $\sum_{j=0}^m(-1)^j\binom mj(m-j)^n$. A codomain label outside the image is a failure of surjectivity even if every domain element has a legal output.

For an onto function with fiber sizes$s_1,\ldots,s_m$, a right inverse chooses one representative in every fiber, giving$\prod s_i$ choices. A left inverse of an injection must undo its image points, while its values outside the image are free choices in the original domain. These counts require careful empty-set cases; a nonempty set has no function into the empty set.

### Composition preserves some facts in only one direction

If$g\circ f$ is injective, $f$ is injective; $g$ need only be injective on the image of$f$. If$g\circ f$ is surjective, $g$ is surjective; $f$ need not fill the whole intermediate set. Full injectivity of both factors is sufficient for injective composition, and full surjectivity of both is sufficient for surjective composition. The converse does not follow in the unused part of the intermediate space.

### Images merge fibers; preimages do not

Preimages preserve unions, intersections and relative complements under the stated total-function types. Images preserve unions but can merge intersections: two disjoint domain subsets may share an output. The round trip$f^{-1}(f(S))$ contains$S$ and adds every other domain point in fibers touched by$S$. Equality means$S$ is a union of whole fibers. Global equality for every$S$ is equivalent to injectivity.

### Infinite counting needs explicit maps

Finite equality of domain and codomain sizes makes injectivity equivalent to surjectivity, but infinite examples break that equivalence. On the nonnegative integers, $n\mapsto n+1$ is injective and not onto. Cantor’s diagonal set$D=\{x:x\notin f(x)\}$ cannot equal$f(d)$ for any$d$ and proves no surjection from a set onto its power set. This is a structural argument, not a finite truth-table count.

## Formula and conceptual problem bank

### Question 1. Unrestricted functions

How many functions map a four-element labeled domain to a three-element labeled codomain?

**A.** 12

**B.** 24

**C.** 36

**D.** 81

**Answer: D.**

Each of four domain elements selects one of three outputs independently, giving$3^4=81$. Functions may repeat outputs.36 would count onto functions, and24 suggests a permutation rule without matching domain and codomain sizes. Every domain point must have one output, not an optional output.

### Question 2. Injections

How many injections map a three-element domain into a five-element codomain?

**A.** 15

**B.** 60

**C.** 125

**D.** 243

**Answer: B.**

Select distinct output choices successively:5 choices, then4, then3, giving60. Equivalently choose an image subset in$\binom53=10$ ways and biject the three inputs to it in$3!=6$ ways.125 permits collisions and counts all functions.

### Question 3. Surjections onto two values

How many surjections map a five-element domain onto a two-element codomain?

**A.** 16

**B.** 30

**C.** 31

**D.** 32

**Answer: B.**

All maps number$2^5=32$. Exactly two are not onto: the constant map to either codomain element. Subtract both to obtain30. Removing only one constant gives31 and violates the symmetry between codomain labels.

### Question 4. Exactly three image values

How many functions from four labeled inputs to five labeled outputs have image size exactly3?

**A.** 120

**B.** 240

**C.** 360

**D.** 625

**Answer: C.**

Choose the three used outputs in$\binom53=10$ ways. Onto maps from four inputs to those three number36 by inclusion-exclusion. Their product is360. Each function has one uniquely determined image set, so this multiplication does not overcount.

### Question 5. Right inverse choices

An onto function has three fibers of sizes2,3,4. How many right inverses does it have?

**A.** 9

**B.** 12

**C.** 24

**D.** 29

**Answer: C.**

A right inverse selects one preimage for each codomain element. The independent choices are2,3,4, giving24. The sum9 counts total domain points but not complete representative selections.29 counts ordered pairs within fibers and belongs to an equivalence-relation question instead.

### Question 6. Left inverse choices

An injection maps a three-element domain into a five-element codomain. How many left inverses from the codomain back to the domain exist?

**A.** 3

**B.** 6

**C.** 9

**D.** 15

**Answer: C.**

On the three image points the left inverse is forced to return their original inputs. On each of the two remaining codomain points, any of three domain values can be chosen. The count is$3^2=9$. The unused points are not constrained by$h\circ f=\mathrm{id}$.

### Question 7. Injective composition

If$g\circ f$ is injective, which conclusion must follow?

**A.** $f$ is injective.

**B.** $g$ is injective on its whole domain.

**C.** $f$ is onto.

**D.** $g$ is onto.

**Answer: A.**

If$f(x)=f(y)$, applying$g$ gives equal composite outputs. Composite injectivity forces$x=y$, proving$f$ injective. The behavior of$g$ away from$f$’s image is unconstrained. A one-point image inside a larger intermediate set can hide collisions of$g$ outside that image.

### Question 8. Surjective composition

If$g\circ f$ is onto its codomain, which conclusion must follow?

**A.** $f$ is onto its codomain.

**B.** $g$ is onto its codomain.

**C.** $f$ is injective.

**D.** $g$ is injective.

**Answer: B.**

Every final output is$g(f(x))$ for some input$x$, so it has a preimage under$g$. Thus$g$ is onto. The subset$f$ reaches may already contain one witness for every final output, so$f$ need not fill the intermediate codomain. Neither condition prohibits collisions.

### Question 9. Preimage algebra

Which equality holds for every total function$f$ and codomain subsets$B,C$?

**A.** $f^{-1}(B\cap C)=f^{-1}(B)\cap f^{-1}(C)$

**B.** $f(S\cap T)=f(S)\cap f(T)$ for all$S,T$

**C.** $f^{-1}(f(S))=S$ for every$S$

**D.** $f(f^{-1}(B))=B$ for every$B$

**Answer: A.**

An input belongs to the left side exactly when its one output belongs to both$B$ and$C$, so it belongs to both preimages. Images can merge separate points, refutingB andC without injectivity. The final round trip equals$B\cap\operatorname{im}f$, not all$B$ unless those outputs are reached.

### Question 10. Fiber saturation

$f(1)=f(2)=a$ and$f(3)=b$. What is$f^{-1}(f(\{1\}))$?

**A.** $\{1\}$

**B.** $\{1,2\}$

**C.** $\{a\}$

**D.** $\{1,2,3\}$

**Answer: B.**

The image of$\{1\}$ is$\{a\}$. Its preimage contains every input with output$a$, namely1 and2. The round trip fills the entire touched fiber. A tests injectivity where it fails; C is in the codomain rather than the required domain; D adds a point with a different output.

### Question 11. Involutions on four objects

How many permutations$f$ on four labeled objects satisfy$f\circ f=\mathrm{id}$?

**A.** 4

**B.** 8

**C.** 10

**D.** 24

**Answer: C.**

Every cycle must have length1 or2. There is one identity, six choices of a single transposition, and three ways to pair all four objects into two disjoint transpositions. Total$1+6+3=10$. All24 permutations include3-cycles and4-cycles, which do not square to identity.

### Question 12. Idempotent maps with two fixed points

On a four-element labeled set, how many functions satisfy$f\circ f=f$ and have image size2?

**A.** 12

**B.** 24

**C.** 36

**D.** 48

**Answer: B.**

Every image point of an idempotent map is fixed: if$y=f(x)$, then$f(y)=f(f(x))=f(x)=y$. Choose the two image/fixed points in6 ways. Each of the other two points independently maps to either one, giving4 choices. Total24. The image points themselves are not free assignments.

### Question 13. Empty-set typing

For nonempty$A$, which function set contains exactly one member?

**A.** Functions$A\to\varnothing$.

**B.** Functions$\varnothing\to A$.

**C.** Bijections$A\to\varnothing$.

**D.** Surjections$\varnothing\to A$.

**Answer: B.**

The empty function has no input obligations and is the unique function from the empty domain to any codomain. No total function maps a nonempty domain into an empty codomain because an input would lack an output. The empty function cannot be onto nonempty$A$.

### Question 14. Infinite injection without surjection

On$\mathbb N_0$, which description applies to$f(n)=n+1$?

**A.** Bijective.

**B.** Injective but not surjective.

**C.** Surjective but not injective.

**D.** Neither.

**Answer: B.**

Equality of outputs$n+1=m+1$ forces$n=m$, so injectivity holds. The codomain element0 has no preimage, so surjectivity fails. Equal infinite domain and codomain sets do not supply the finite pigeonhole equivalence between these properties.

### Question 15. Function-space size

For finite$A,B,C$ with sizes2,3,4, how many functions$(A\times B)\to C$ exist?

**A.** 24

**B.** 64

**C.** 729

**D.** 4096

**Answer: D.**

The product domain has six elements, and each chooses one of four outputs, so the count is$4^6=4096$. Currying gives a bijection with maps$A\to C^B$, whose codomain has$4^3=64$ members and count$64^2=4096$. The count24 multiplies sizes rather than counting function tables.

### Question 16. Cantor’s diagonal contradiction

For$f:A\to\mathcal P(A)$, define$D=\{x\in A:x\notin f(x)\}$. Why can$D$ not be$f(d)$ for any$d\in A$?

**A.** It would force$d\in D\Leftrightarrow d\notin D$.

**B.** Every subset of$A$ is empty.

**C.** $f$ must be injective.

**D.** $A$ must be finite.

**Answer: A.**

If$D=f(d)$, substituting$d$ into the defining membership rule gives$d\in D$ exactly when$d\notin f(d)$, hence exactly when$d\notin D$. Either truth value contradicts itself. No finiteness assumption or injectivity is used. This proves the diagonal subset is missing from every proposed image.

<!-- CHALLENGE-BANK -->

### Question 17. Challenge: All idempotent maps on four points

How many functions on a four-element labeled set satisfy$f\circ f=f$?

**A.** 24

**B.** 36

**C.** 41

**D.** 64

**Answer: C.**

Classify by nonempty image size$r$. Image points must be fixed, and each other point may map to any image point. Counts are$\binom4r r^{4-r}$. For$r=1,2,3,4$ they are4,24,12,1, totaling41. A nonempty domain cannot have empty image. All functions number256, while permutations satisfying this idempotent condition include only the identity.

### Question 18. Challenge: Count split inverse pairs

$A$ has two labeled elements and$B$ has three. How many ordered function pairs$f:A\to B,g:B\to A$ satisfy$g\circ f=\mathrm{id}_A$?

**A.** 6

**B.** 8

**C.** 12

**D.** 18

**Answer: C.**

The identity composite forces$f$ injective, giving3 times2=6 choices. For each chosen$f$, the values of$g$ on its two image points are forced. The remaining point of$B$ may map to either of the two$A$ values, giving two choices. Total12. This counts the pair jointly; selecting arbitrary$f,g$ independently would include pairs violating the identity.

## Applicable formulas and examination notes

### 1. Function counts

Total maps give$m^n$; injections give$m!/(m-n)!$ for$n\le m$; bijections of equal finite size give$n!$. State whether maps are total, partial or onto. Partial maps add a distinguished “undefined” option and number$(m+1)^n$.

### 2. Onto and image size

Count onto maps by missing-output inclusion-exclusion. For image size$r$, choose$r$ outputs and multiply by the onto count into them. Four inputs and five outputs with image size3 give$\binom53\cdot36=360$.

### 3. Right inverses

For an onto finite map, right inverse count is the product of fiber sizes. Fibers2,3,4 give24 choices. A missing fiber gives no right inverse, because its output has no representative.

### 4. Left inverses

For an injection from$n>0$ points into$m$, the image values of a left inverse are forced and the$m-n$ others each have$n$ choices: $n^{m-n}$. Empty-domain cases require direct typing rather than casual use of$0^0$.

### 5. Composition implications

Composite injective implies first map injective; composite onto implies second map onto. The reverse component conclusions fail on unused intermediate points. Restrict the second map to the first image before making a stronger assertion.

### 6. Cancellation sides

An injective postcomposition permits canceling the post-map from$g\circ f_1=g\circ f_2$. An onto precomposition permits canceling the pre-map. Swapping these hypotheses changes which values the equality actually tests.

### 7. Preimage preservation

Preimages preserve unions, intersections and codomain-relative complements for total functions. This uses one output per input, not invertibility. The notation$f^{-1}(B)$ is a set operation even when no inverse function exists.

### 8. Image loss

Images preserve unions but can enlarge intersections through collisions. For$1,2$ in one fiber, images of the disjoint singletons intersect. Images preserve all intersections exactly when the function is injective.

### 9. Saturation round trip

$f^{-1}(f(S))$ is the union of fibers touched by$S$ and equals$S$ precisely when$S$ is already fiber-saturated. The codomain round trip is$f(f^{-1}(B))=B\cap\operatorname{im}f$.

### 10. Involution versus idempotence

An involution has$f^2=\mathrm{id}$ and consists of fixed points and swaps. An idempotent has$f^2=f$ and fixes every image point. With a chosen$r$-point image on$n$ points, idempotent count is$\binom nr r^{n-r}$ for$r\ge1$.

### 11. Empty function

There is one map from the empty domain to any codomain. There is no map from a nonempty domain to the empty codomain. A map is onto an empty codomain only when the domain is empty as well.

### 12. Infinite finite-rule failure

On nonnegative integers,$n\mapsto n+1$ is an injection missing0. A surjection can likewise merge points in an infinite domain. Use explicit fibers or missing outputs rather than finite cardinality cancellation.

### 13. Currying

Maps$(A\times B)\to C$ correspond to maps$A\to C^B$. Finite size becomes$|C|^{|A||B|}=(|C|^{|B|})^{|A|}$. This rearranges a function representation, not an ordinary Cartesian product of codomains.

### 14. Diagonal exclusion

For$D=\{x:x\notin f(x)\}$, assume$D=f(d)$ and test membership of$d$. The contradiction proves no surjection onto the power set. It does not assume every proper subset is smaller in cardinality.

<!-- BOUNDARY-NOTES -->

### 15. Floor and ceiling fibers

For integer $k$, $\lfloor x\rfloor=k$ iff $k\le x<k+1$, while $\lceil x\rceil=k$ iff $k-1<x\le k$. Negative inputs use the same intervals, not truncation toward zero. Endpoint inclusion changes the fiber.

### 16. Restricted codomain

Replacing a codomain by the exact image makes the same total graph surjective onto that new codomain. It does not repair collisions or create an inverse on the original codomain. Domain and codomain are part of a function's type.

### 17. Kernel factorization

Inputs are equivalent when they have the same output. The quotient by this kernel maps bijectively to the image, while the original function may be neither injective nor onto its declared codomain. Representative choice must not change the quotient map.

### 18. Two injections and cardinality

Injections both ways imply a bijection by Schröder–Bernstein, even for infinite sets. Two one-sided injections need not already be inverses of each other. The theorem proves existence of a new matching, not cancellation of arbitrary given maps.
