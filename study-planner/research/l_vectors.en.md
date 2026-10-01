# Vectors, Inner Products, and Linear Geometry

**Approved English chapter · Linear Algebra, Chapter 1 · Read the full lesson before using the problem bank as practice.**

## 1. Scope, prerequisites, and reviewed sources

This chapter builds the language of vectors and then develops the geometry needed for exact calculations and proofs: span, independence, coordinates, norms, inner products, angles, orthogonal projection, orthonormal coordinates, Gram–Schmidt, and affine distances. A final section treats cross products, area, and volume in three-dimensional real space. Weighted, polynomial, and complex examples show which conclusions depend on the underlying geometry.

You need arithmetic, algebraic equations, sums, square roots, and elementary trigonometry. Integration is used only in the clearly identified polynomial extension; that extension explains the required integrals. Complex examples introduce conjugation explicitly. General matrix elimination, determinant theory, rank–nullity, eigenvalues, full least-squares algorithms, and infinite-dimensional convergence are reserved for later chapters. We introduce span and basis here because projection needs them; their general structural theory will be developed later.

Four university offerings were selected after a bounded comparison of eight candidates. The actual reading was of relevant written sections, not entire courses. The source audit records rejected candidates, access limits, and corrected slips. The explanations and problems below are independently written; a source attribution identifies the mathematical teaching pattern, not copied wording.

| University / course | Instructor | Written material genuinely reviewed | Role in this chapter |
|---|---|---|---|
| Stanford EE263, Autumn 2007–08 | Stephen Boyd | Linear Algebra Review, 31 slides; Orthonormal Sets and QR Factorization, 23 slides | Coordinates, norms, orthonormal expansions, computational geometry |
| Oxford M1 Linear Algebra I, Michaelmas 2022 | Andrew Wathen, course instructor; note authorship not stated on the title page | Printed pp. 25–43 and 69–77 | Definitions, independence, proof assumptions, real/complex inner products |
| UC Berkeley Math 54, Spring 2018 | Alexander Paulin | Four handwritten notes, four pages each: vectors; inner products/length; projections; inner-product spaces | Geometric reasoning, nonunit orthogonal bases, polynomial examples |
| MIT 18.02SC, Fall 2010 | Denis Auroux | Dot Product pp. 1–2; Components and Projection p. 1; Cross Product pp. 1–2 | Signed components, vectors in physical space, oriented area |

**How to read.** Work through Sections 2–9 in order. Use the laboratory to compare a correct projection with a nearby candidate. Read the worked solutions as lessons; their explanations deliberately include why tempting alternatives fail. Section 12 is a complete-sentence review for later revision. This chapter supplies a broad set of in-scope reasoning tools, but no finite text can establish a guarantee about every unseen examination problem.

## 2. Vectors, points, and coordinates

### 2.1 A vector is an object; coordinates describe it

A real coordinate vector of length n is an ordered list of n real numbers. Order matters: (1,2) and (2,1) generally represent different vectors. All vectors in a calculation must lie in the same ambient space unless an embedding or other map has been specified. A two-component vector cannot be added directly to a three-component vector.

We write tuples horizontally to save space, but interpret them as column-coordinate vectors when a transpose is used. The ith coordinate is xᵢ. The zero vector has every coordinate zero; its number of coordinates is determined by the space.

<div class="formula-block">ℝⁿ = { (x₁,…,xₙ) : xᵢ ∈ ℝ for each i }; 0 = (0,…,0).</div>

Addition and scalar multiplication are componentwise. For example, (2,−1,3)+(−4,5,0)=(−2,4,3), and −2(2,−1,3)=(−4,2,−6). A negative scalar reverses a nonzero vector's direction. The vector's length scales by the scalar's absolute value, not its signed value.

<div class="formula-block formula-steps"><div>(x+y)ᵢ = xᵢ+yᵢ; (αx)ᵢ = αxᵢ.</div><div>x−y = x+(−1)y; α(x+y) = αx+αy.</div></div>

A point is a location; a displacement is a vector. If points have coordinates P and Q, the displacement from P to Q is Q−P. Changing the origin changes both point-coordinate lists but leaves their difference unchanged. Adding a displacement to a point gives another point. Treating a location as a vector requires an identified origin; this matters when finding distances to a line that does not pass through zero.

In the plane, vector addition follows the parallelogram rule. Moving by x and then by y has the same total displacement as moving by x+y. The order of these two translations does not matter because coordinate addition is commutative. This geometric picture extends algebraically to any dimension even when an n-dimensional drawing is unavailable.

<figure class="logic-diagram"><svg viewBox="0 0 620 270" role="img" aria-label="Head to tail addition of vectors u and v gives u plus v"><defs><marker id="add-arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6" fill="none" stroke="context-stroke"/></marker></defs><path d="M70 220 L310 220 L440 80 L200 80 Z" fill="#eef6f8" stroke="#b7d2db" stroke-dasharray="5 5"/><g fill="none" stroke-width="3" marker-end="url(#add-arrow)"><path d="M70 220 L310 220" stroke="#286c91"/><path d="M310 220 L440 80" stroke="#a0612e"/><path d="M70 220 L440 80" stroke="#487962"/></g><g font-size="23" fill="#233142"><text x="65" y="250">0</text><text x="175" y="245">u</text><text x="380" y="170">v</text><text x="245" y="125">u + v</text></g></svg><figcaption>Translate the second arrow without changing it. The diagonal is the total displacement.</figcaption></figure>

### 2.2 The standard basis and the role of a chosen basis

The standard vector eᵢ has coordinate 1 in position i and 0 everywhere else. Every vector has the expansion below. Comparing coordinates proves uniqueness: the ith coordinate of the expansion is exactly xᵢ.

<div class="formula-block">x = ∑<sub>i=1</sub><sup>n</sup> xᵢeᵢ.</div>

Coordinates relative to another basis can be different. With b₁=(1,1) and b₂=(1,−1), the vector (4,2) equals 3b₁+b₂. Its coordinates in that ordered basis are (3,1), while its standard coordinates are (4,2). Never take a dot product of arbitrary coordinate lists and assume that it equals a geometrical inner product. That shortcut works for an orthonormal basis; it does not hold for every basis.

### 2.3 Why vector-space rules matter beyond arrows

A vector space supports addition and scalar multiplication satisfying eight rules: commutativity and associativity of addition; a zero vector; additive inverses; distributivity over vector addition; distributivity over scalar addition; compatibility of consecutive scalar multiplications; and multiplication by scalar 1 acting as the identity. Closure means these operations stay within the space. The rules hold in real coordinate space because they hold separately in each coordinate.

They also hold for polynomials under ordinary addition and scaling, and for functions under pointwise operations. A polynomial is a vector in this sense even though it is not itself an arrow. The zero vector is then the zero polynomial or zero function. A vector space alone does not provide angles or lengths: an inner product or a norm is additional structure.

The identities 0x=0 and α0=0 follow from distributivity. For instance, 0x=(0+0)x=0x+0x; subtracting 0x gives 0=0x. If αx=0 and α is nonzero, multiplication by its scalar inverse gives x=0. This inference relies on working over a field such as the real or complex numbers.

## 3. Span, independence, bases, and affine sets

### 3.1 Span describes every reachable linear combination

The span of a finite list consists of all its linear combinations with arbitrary scalars from the specified field. It contains zero, because every coefficient may be zero. It is closed under addition and scaling because coefficients can be added or scaled. Thus it is a subspace. Any subspace containing the original list must contain every such combination, so span is the smallest containing subspace.

<div class="formula-block">span(v₁,…,vₖ) = {∑<sub>j=1</sub><sup>k</sup> cⱼvⱼ : cⱼ ∈ ℝ}.</div>

One nonzero vector spans a line through the origin. Two nonparallel vectors span a plane through the origin. Two parallel vectors still span only a line; adding a redundant vector does not create a dimension. A zero-only list spans the zero subspace. By convention, the empty list also spans the zero subspace, through its empty combination.

The subspace test is efficient: a subset W of a known vector space is a subspace if it contains zero and is closed under arbitrary linear combinations of two members. Necessity follows from vector-space closure. For sufficiency, taking both coefficients 1 gives addition, and taking the second vector zero gives scalar closure. The remaining axioms are inherited from the ambient space.

The set of solutions to a homogeneous equation x₁+2x₂−x₃=0 is a subspace. The equation with right side 1 describes an affine plane, not a subspace: it excludes zero. The unit circle contains no zero and is not closed under scaling. Even a set that contains zero may fail closure; the union of the two coordinate axes fails addition because (1,0)+(0,1) is on neither axis.

### 3.2 Independence means no nontrivial cancellation

A list is linearly independent if its only combination equal to zero has all coefficients zero. A list containing a zero vector is dependent. A repeated vector is dependent, and a nonzero scalar multiple of another vector introduces dependence. Dependence does not mean that every pair is parallel: three planar directions can have every pair nonparallel yet still be dependent.

<div class="formula-block">∑<sub>j=1</sub><sup>k</sup> cⱼvⱼ = 0 ⇒ c₁ = ⋯ = cₖ = 0.</div>

**Uniqueness theorem.** For an independent list, a vector in its span has exactly one coefficient list. If two representations exist, subtract them. The resulting zero combination has coefficients equal to the differences; independence makes each difference zero. Conversely, unique representations make the representation of zero unique, so a nontrivial zero combination cannot occur.

Adding a vector to an independent list preserves independence exactly when the new vector lies outside the existing span. If it lies inside, moving its representation to one side gives a nontrivial relation. If it lies outside and a zero combination uses it with a nonzero coefficient, division expresses it in the old span, a contradiction. Its coefficient must therefore be zero, after which the old independence finishes the proof.

### 3.3 Bases separate existence from uniqueness

A basis of W is a list that both spans W and is independent. Spanning guarantees existence of a representation; independence guarantees uniqueness. An ordered basis gives ordered coordinates. A nonspanning independent list is a basis only for its own span, not automatically for the entire ambient space.

In a finite-dimensional space, every basis has the same number of members, its dimension. Here we use this terminology for coordinate spaces and their subspaces; the general exchange-lemma proof belongs to the later vector-space chapter. A nonzero orthogonal list is independent by the argument in Section 7, so it is automatically a basis for its span. The zero subspace has the empty basis and dimension zero, not the single-vector list containing zero.

The field matters. The numbers 1 and i form an independent pair over the reals: a+bi=0 with real coefficients forces both zero. Over the complex numbers the same pair is dependent because i·1−1·i=0. Questions about dimension or dependence are incomplete without specifying allowed scalars.

### 3.4 Affine geometry is a translated subspace

An affine set P+W consists of P+w for w in W. It is a translate of a subspace. It is itself a subspace precisely when P belongs to W, in which case the translate is W. To see necessity, if zero lies in P+W, then −P lies in W, so P lies in W. A line P+tb has a base point and direction; a plane P+su+tv has a base point and two independent directions. Distance calculations must subtract P first.

## 4. Dot products, norms, and angles

### 4.1 The real dot product is scalar-valued

The standard dot product multiplies matching real coordinates and adds. It produces a scalar, not a vector. It is symmetric and linear in each argument. The product of a vector with itself is a sum of squares, so it is nonnegative, and zero only for the zero vector. These observations supply the standard Euclidean norm.

<div class="formula-block formula-steps"><div>x·y = ∑<sub>i=1</sub><sup>n</sup> xᵢyᵢ; ‖x‖² = x·x.</div><div>‖x‖ = <math><msqrt><mrow><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></munderover><msubsup><mi>x</mi><mi>i</mi><mn>2</mn></msubsup></mrow></msqrt></math>.</div></div>

Distance is ‖x−y‖. It is the length of the displacement between the points, and it is symmetric because negation does not change norm. A unit vector has norm 1. Normalizing a nonzero vector means dividing it by its norm. The zero vector cannot be normalized because division by zero is undefined.

Expanding componentwise gives several useful identities. The middle term in a squared norm is twice the dot product; forgetting it falsely treats every pair as orthogonal.

<div class="formula-block formula-steps"><div>‖x+y‖² = ‖x‖²+2x·y+‖y‖².</div><div>‖x−y‖² = ‖x‖²−2x·y+‖y‖².</div><div>‖x+y‖²+‖x−y‖² = 2‖x‖²+2‖y‖².</div><div>x·y = (‖x+y‖²−‖x−y‖²)/4.</div></div>

The third identity is the parallelogram law. The fourth is real polarization: it recovers the dot product from norm data without knowing coordinates. If x·y=0, the first formula becomes Pythagoras. Conversely, in a real inner-product space, the displayed Pythagorean equality implies x·y=0.

### 4.2 Cauchy–Schwarz, with its equality condition

For any real vectors, |x·y|≤‖x‖‖y‖. This is not just a bound to memorize: it follows from the nonnegativity of a carefully chosen squared residual. If y=0 the assertion is immediate. Otherwise put c=(x·y)/‖y‖² and expand:

<div class="formula-block formula-steps"><div>0 ≤ ‖x−cy‖²</div><div>= ‖x‖²−2c(x·y)+c²‖y‖²</div><div>= ‖x‖²−(x·y)²/‖y‖².</div></div>

Multiplying by the positive denominator gives the squared inequality; taking nonnegative square roots gives the stated form. Equality holds exactly when the residual is zero, meaning x is a scalar multiple of y. Including the zero case, equality holds exactly when the pair is linearly dependent. The scalar may be negative; Cauchy–Schwarz equality does not require the same direction.

An alternative real proof uses the quadratic ‖x+ty‖², which is nonnegative for every real t. Its discriminant must be nonpositive. This also yields the inequality and proves dependence at equality. The residual proof extends naturally to complex vectors once conjugation is handled correctly.

### 4.3 Triangle and reverse-triangle inequalities

Using the norm expansion and Cauchy–Schwarz gives ‖x+y‖²≤(‖x‖+‖y‖)². Both sides are nonnegative, so taking square roots is valid. For nonzero real vectors, equality requires x·y=‖x‖‖y‖, which means positive proportionality. Opposite directions satisfy Cauchy–Schwarz equality but usually make the triangle inequality strict. If either vector is zero, triangle equality also holds.

Apply triangle inequality to x=(x−y)+y to obtain ‖x‖−‖y‖≤‖x−y‖. Exchanging x and y gives the reverse bound:

<div class="formula-block">|‖x‖−‖y‖| ≤ ‖x−y‖ ≤ ‖x‖+‖y‖.</div>

These bounds reveal feasible distances. With fixed nonzero lengths, the maximum distance occurs in opposite directions and the minimum in the same direction. In one-dimensional real space only these sign configurations are possible; in at least two dimensions intermediate angles are available.

### 4.4 Angles need nonzero real vectors

For nonzero real vectors, Cauchy–Schwarz puts the ratio below in [−1,1], so arccos defines an unsigned angle in [0,π]. Its sign classification gives acute, right, and obtuse angles. The definition is algebraic in any real inner-product space, not restricted to visible two-dimensional arrows.

<div class="formula-block">cos θ = <math><mfrac><mrow><mi>x</mi><mo>·</mo><mi>y</mi></mrow><mrow><mo>‖</mo><mi>x</mi><mo>‖</mo><mo>‖</mo><mi>y</mi><mo>‖</mo></mrow></mfrac></math>; 0 ≤ θ ≤ π.</div>

Orthogonality is defined by zero inner product. The zero vector is therefore orthogonal to every vector, but an angle involving zero is undefined. A statement such as “orthogonal vectors always make a right angle” needs the nonzero qualification. An angle between vectors is also distinct from the smaller angle between two unoriented lines, which uses the absolute value of the dot product.

The algebraic definition agrees with the usual geometric angle in a Euclidean plane. The triangle formed by x, y, and their difference has side lengths ‖x‖, ‖y‖, and ‖x−y‖. The law of cosines gives ‖x−y‖²=‖x‖²+‖y‖²−2‖x‖‖y‖cosθ. Comparing with the dot-product expansion identifies x·y=‖x‖‖y‖cosθ. Thus the coordinate formula measures the familiar angle; it is not an unrelated definition imposed on the picture.

## 5. General and complex inner products

### 5.1 The geometry must be specified

A real inner product is a symmetric bilinear scalar-valued function ⟨x,y⟩ with ⟨x,x⟩≥0, equality only when x=0. Bilinearity means linearity in each argument. Its induced norm is √⟨x,x⟩. All the real residual, inequality, and projection proofs above remain valid because they used exactly these properties.

Positive weighted coordinates give a simple example. If every weight wᵢ is strictly positive, a sum of weighted squares vanishes only if every coordinate vanishes. A zero weight permits a nonzero vector of zero “length”; a negative weight permits negative self-products. Neither is an inner product on the full coordinate space.

<div class="formula-block">⟨x,y⟩<sub>w</sub> = ∑<sub>i=1</sub><sup>n</sup> wᵢxᵢyᵢ, wᵢ &gt; 0.</div>

Changing the weights changes angles and perpendicular directions while leaving vector addition and span unchanged. More generally, a real symmetric matrix G describes a bilinear form xᵀGy. It is an inner product exactly when xᵀGx is strictly positive for every nonzero x. This chapter uses small coordinate formulas, so no spectral theorem is assumed. For G with rows (1,a) and (a,1), completing squares yields (x₁+ax₂)²+(1−a²)x₂², which is strictly positive exactly when |a|&lt;1.

Not every norm comes from an inner product. The sum of absolute coordinates and the maximum absolute coordinate are norms, but in dimensions at least two they fail the parallelogram law. Their triangle inequalities can be established directly, but their nearest points need not be unique. This chapter's orthogonal-projection theorem applies to inner-product geometry, not to every possible notion of distance.

### 5.2 Polynomial vectors and sampling

For continuous real functions on [a,b] with a&lt;b, the integral of f(t)g(t) defines an inner product. Linearity of the integral proves bilinearity; multiplication proves symmetry. If a continuous nonzero f is nonzero at a point, continuity makes its square positive on a subinterval of positive length. Hence the integral of its square is strictly positive. The condition a&lt;b is necessary; an interval of zero length gives zero for every self-product.

<div class="formula-block">⟨f,g⟩ = <math><munderover><mo>∫</mo><mi>a</mi><mi>b</mi></munderover><mi>f</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi>g</mi><mo>(</mo><mi>t</mi><mo>)</mo><mi mathvariant="normal">dt</mi></math>.</div>

For polynomials of degree at most m, evaluations at m+1 distinct points also define an inner product by summing products of sampled values. A nonzero polynomial of degree at most m cannot vanish at m+1 distinct points; this proves definiteness. Fewer sample points can fail: a nonzero polynomial can vanish at all of them. These are different geometries; integrating products and taking a dot product of raw polynomial coefficients usually give different answers.

### 5.3 Complex vectors require conjugation

Write i²=−1. The conjugate of a+bi is a−bi, and the squared modulus is a²+b². The naive bilinear product of (1,i) with itself is 1+i²=0, so it cannot supply a positive-definite complex inner product. Our convention conjugates the **first** argument:

<div class="formula-block formula-steps"><div>⟨x,y⟩ = ∑<sub>j=1</sub><sup>n</sup> <span class="overline">x</span><sub>j</sub>yⱼ; ‖x‖² = ∑<sub>j=1</sub><sup>n</sup> |xⱼ|².</div><div>⟨αx,βy⟩ = <span class="overline">α</span>β⟨x,y⟩.</div><div>⟨y,x⟩ = <span class="overline">⟨x,y⟩</span>.</div></div>

Oxford's notes use the opposite convention, linear in the first argument. Either convention is valid if used consistently. Formulas that move a scalar or extract a projection coefficient must be translated when changing conventions. Under ours, the coefficient for projecting x along a nonzero b is ⟨b,x⟩/⟨b,b⟩, not ⟨x,b⟩/⟨b,b⟩.

With c=⟨b,x⟩/‖b‖², expansion gives ‖x−cb‖²=‖x‖²−|⟨b,x⟩|²/‖b‖². Thus complex Cauchy–Schwarz uses the modulus of the inner product. Equality means complex linear dependence. In a norm expansion the cross term is 2 Re⟨x,y⟩; a complex inner product need not itself be real.

To see every conjugation in that derivation, put z=⟨b,x⟩ and S=‖b‖²&gt;0. Expanding before substituting c gives the following steps. Conjugate symmetry supplies ⟨x,b⟩ equal to the conjugate of z. Both cross terms therefore become the same real number after c=z/S is substituted:

<div class="formula-block formula-steps"><div>‖x−cb‖² = ‖x‖²−c⟨x,b⟩−<span class="overline">c</span>⟨b,x⟩+|c|²S.</div><div>= ‖x‖²−|z|²/S−|z|²/S+|z|²/S.</div><div>= ‖x‖²−|z|²/S ≥ 0.</div></div>

Multiplication by S and taking square roots proves the complex inequality. Equality forces the residual to be zero by positive definiteness. If b is zero, handle it directly instead of assigning S a reciprocal. This proof explains why replacing a complex modulus by an ordinary square can produce a false bound.

Consequently, the naive real angle ratio is not a real cosine in general. One can define an angle using the real part after regarding the space as real, or an angle between complex lines using the modulus; they are different notions. We use the standard arccos formula only for real vectors. In particular, complex Pythagorean norm equality only forces the real part of the inner product to vanish; complex orthogonality is the stronger condition that the entire inner product is zero.

## 6. Projection: the residual explains the formula

### 6.1 Three quantities that must not be confused

Let b be nonzero, and first work over the reals. A unit direction is q=b/‖b‖. The signed scalar component of x along that unit direction is x·q. The coefficient multiplying the unnormalized b is (x·b)/‖b‖². The vector projection is that coefficient times b. Its length is the absolute value of the signed scalar component.

<div class="formula-block formula-steps"><div>s = x·b/‖b‖; c = x·b/‖b‖².</div><div>p = cb; r = x−p; r·b = 0.</div><div>‖p‖ = |s|; x = p+r.</div></div>

A negative component means the projection points opposite to b. Replacing b by any nonzero scalar multiple leaves p unchanged, though c and the signed component relative to an oriented unit direction can change. Orthogonality of the residual follows by substituting c: (x−cb)·b=x·b−c‖b‖²=0. In the complex convention use ⟨b,r⟩=0 and c=⟨b,x⟩/‖b‖².

<figure class="logic-diagram"><svg viewBox="0 0 640 300" role="img" aria-label="Projection decomposes x into its component p along a line and an orthogonal residual r"><defs><marker id="proj-arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6" fill="none" stroke="context-stroke"/></marker></defs><path d="M60 240 L570 240" stroke="#9cb8c7" stroke-width="2"/><g fill="none" stroke-width="3" marker-end="url(#proj-arrow)"><path d="M90 240 L390 70" stroke="#286c91"/><path d="M90 240 L390 240" stroke="#487962"/><path d="M390 240 L390 70" stroke="#a0612e"/></g><path d="M370 240 L370 220 L390 220" fill="none" stroke="#536f80"/><g font-size="23" fill="#233142"><text x="75" y="272">0</text><text x="220" y="145">x</text><text x="235" y="270">p</text><text x="410" y="150">r = x − p</text><text x="468" y="270">span(b)</text></g></svg><figcaption>Projection preserves the component along the line; subtraction leaves the orthogonal component.</figcaption></figure>

### 6.2 Why this is the unique nearest point

Every candidate on the line has the form tb. Write x−tb=r+(c−t)b. The two terms are orthogonal, so their squared lengths add. For real t:

<div class="formula-block">‖x−tb‖² = ‖r‖²+(t−c)²‖b‖².</div>

The second term is nonnegative and is zero only when t=c. Thus p is the unique nearest point. The same argument over complex scalars uses |t−c|². No calculus is needed. It also yields the squared distance ‖x‖²−|⟨b,x⟩|²/‖b‖². The denominator's nonzero assumption is essential.

If b=0, the line formula is undefined, but its span is the zero subspace, whose projection is well-defined as zero. Distinguish a failed coordinate formula from the underlying geometric object. If x=0 and b is nonzero, the formula gives projection zero without difficulty.

### 6.3 Projection onto an orthogonal span

Let b₁,…,bₖ be nonzero and pairwise orthogonal. Put W equal to their span. Taking an inner product with each bⱼ isolates one coefficient, because all other terms vanish. This yields:

<div class="formula-block">p = ∑<sub>j=1</sub><sup>k</sup> <math><mfrac><mrow><mo>⟨</mo><msub><mi>b</mi><mi>j</mi></msub><mo>,</mo><mi>x</mi><mo>⟩</mo></mrow><mrow><mo>⟨</mo><msub><mi>b</mi><mi>j</mi></msub><mo>,</mo><msub><mi>b</mi><mi>j</mi></msub><mo>⟩</mo></mrow></mfrac></math>bⱼ.</div>

For each j, ⟨bⱼ,x−p⟩=0. Linearity then makes the residual orthogonal to every member of W. For any w in W, x−w=(x−p)+(p−w), and Pythagoras gives ‖x−w‖²=‖x−p‖²+‖p−w‖². This proves both nearest-point optimality and uniqueness. The projection is determined by W, not by the particular orthogonal basis chosen.

**Nonorthogonal trap.** If the basis is not orthogonal, summing separate one-direction projections generally fails. Write p=∑cⱼbⱼ and enforce ⟨bᵢ,x−p⟩=0. The coefficients satisfy coupled equations:

<div class="formula-block">∑<sub>j=1</sub><sup>k</sup> ⟨bᵢ,bⱼ⟩cⱼ = ⟨bᵢ,x⟩, 1 ≤ i ≤ k.</div>

Their Gram matrix has entries ⟨bᵢ,bⱼ⟩. Independence makes its quadratic form strictly positive: the form equals the squared norm of ∑cⱼbⱼ, zero only for the zero coefficient vector. Thus the coefficients are unique. With dependent generators, coefficients can be nonunique even though the projected vector is unique. A worked problem derives the two-direction equations without assuming general inverse-matrix theory.

## 7. Orthonormal coordinates and Gram–Schmidt

### 7.1 Orthogonality supplies independence and coordinates

Suppose a combination of nonzero pairwise orthogonal vectors is zero. Taking the inner product with one vector gives its coefficient times that vector's positive squared norm equal to zero. Every coefficient is therefore zero. Nonzero is necessary: the zero vector is orthogonal to everything but cannot belong to an independent list.

An orthonormal list is orthogonal and every vector has norm 1. If it spans W, coefficients of any member x of W are ⟨qⱼ,x⟩. For an arbitrary x in a larger ambient space, the same sum is its projection, not necessarily x itself.

<div class="formula-block formula-steps"><div>p = ∑<sub>j=1</sub><sup>k</sup> ⟨qⱼ,x⟩qⱼ.</div><div>‖x‖² = ∑<sub>j=1</sub><sup>k</sup> |⟨qⱼ,x⟩|²+‖x−p‖².</div></div>

Dropping the nonnegative residual gives Bessel's inequality. Equality holds exactly when x lies in W. If the list is an orthonormal basis of the entire finite-dimensional space, the residual is zero for every x; the equality is Parseval's identity. An orthogonal nonunit basis needs division by each squared norm when extracting coefficients, and a factor of each squared norm when recomputing the norm from those coefficients.

### 7.2 Gram–Schmidt constructs the needed geometry

Start with v₁,…,vₘ. At each stage remove the component along every previously retained orthonormal direction. If the residual is nonzero, normalize it and retain the result. If it is exactly zero, the input belongs to the existing span; skip it. The first zero input is skipped too.

<div class="formula-block formula-steps"><div>w = vⱼ−∑<sub>i=1</sub><sup>k</sup> ⟨qᵢ,vⱼ⟩qᵢ.</div><div>If w ≠ 0, append q<sub>k+1</sub> = w/‖w‖.</div></div>

**Invariant and proof.** Before a step, the retained directions are orthonormal and span all earlier inputs. Subtracting their projection makes w orthogonal to every retained direction. Normalization gives a unit vector without changing that orthogonality. The new input equals its old-span projection plus w, so retaining w preserves the span of processed inputs. Conversely w is a combination of the new input and old-span vectors, so it introduces no extra span. If w is zero, the old span already contains the new input. Induction proves the algorithm produces an orthonormal basis for the full input span.

For an independent input list no residual vanishes. For dependent inputs the number of retained vectors is smaller than the number of inputs. Changing the input order can change the resulting basis while preserving the final span and its projection. Multiplying a retained direction by −1, or by a complex scalar of modulus 1, also changes the basis but not the span.

```python
def orthonormalize(vectors, inner):
    # Exact-arithmetic mathematical pseudocode; vectors share one space.
    basis = []
    for v in vectors:
        w = v.copy()
        for q in basis:
            coefficient = inner(q, w)  # First argument is conjugate-linear.
            w = w - coefficient * q
        squared_norm = inner(w, w).real
        if squared_norm == 0:
            continue
        basis.append(w / sqrt(squared_norm))
    return basis
```

This successive-subtraction form is mathematically equivalent to the displayed projection formula in exact arithmetic: later coefficient calculations are unchanged because retained directions are mutually orthogonal. Floating-point arithmetic is different. Near dependence can produce a tiny residual, so testing exact numerical equality to zero is unreliable. Production implementations need a scale-aware tolerance, possibly reorthogonalization, and an explicit rank decision. The pseudocode teaches the exact invariant; it is not a complete numerical linear-algebra library. Simply deleting every small residual using an unexplained fixed threshold can discard a genuinely independent direction.

### 7.3 Orthogonal complements and projection structure

The orthogonal complement W⊥ contains all vectors perpendicular to every member of W. It is a subspace: linear combinations preserve all zero inner products. Testing against a spanning list is sufficient by linearity. In a finite-dimensional inner-product space every x decomposes uniquely as p+r with p in W and r in W⊥. Existence follows from constructing an orthonormal basis for W and taking the residual. For uniqueness, the difference between two decompositions lies in both W and W⊥; its self-product is zero, so that difference is zero.

Thus W∩W⊥={0}, not the empty set. Extending an orthonormal basis by Gram–Schmidt supplies an orthonormal basis for the complement, so the two dimensions sum to the ambient dimension. It also proves (W⊥)⊥=W in finite dimensions. We do not apply these finite-dimensional conclusions to arbitrary infinite spaces without the extra closure assumptions required there.

The map P taking x to its projection is linear because each extracted coefficient is linear in x. Projecting twice has no further effect, so P²=P. The complementary map x−Px is projection onto W⊥. The identities ‖Px‖≤‖x‖ and ‖Px−Py‖≤‖x−y‖ follow from the orthogonal decomposition and linearity. Equality in the first requires x in W; equality in the second requires x−y in W. The map preserves inner products with directions in W, but usually loses the component in W⊥.

## 8. Distances to affine lines and planes

### 8.1 Translate, project, and translate back

For a line L={P+tb}, subtract P from the target point X to get x=X−P. Project x onto span(b), and add P back. The perpendicular residual gives the distance. This procedure is coordinate-independent in Euclidean geometry, and it avoids the mistake of projecting X directly onto a direction through the origin.

<div class="formula-block formula-steps"><div>c = (X−P)·b/‖b‖².</div><div>Q = P+cb; dist(X,L) = ‖X−Q‖.</div></div>

A hyperplane with nonzero normal n has equation n·Z=d. Its nearest point to X differs from X only along n. Substitute Q=X−tn into the plane equation: n·X−t‖n‖²=d. Solving gives the formulas below. The absolute value belongs in the distance, while the signed displacement retains the numerator's sign.

<div class="formula-block formula-steps"><div>Q = X−<math><mfrac><mrow><mi>n</mi><mo>·</mo><mi>X</mi><mo>−</mo><mi>d</mi></mrow><msup><mrow><mo>‖</mo><mi>n</mi><mo>‖</mo></mrow><mn>2</mn></msup></mfrac></math>n.</div><div>dist(X,H) = |n·X−d|/‖n‖.</div></div>

To prove optimality, any difference between two points in the plane is perpendicular to n. The proposed residual is parallel to n. Pythagoras therefore makes every alternative plane point at least as far away, with equality only at Q. Scaling both n and d by the same nonzero factor leaves the plane and distance unchanged.

If n=0 and d=0, the equation describes the whole space, distance zero. If n=0 and d≠0, there are no plane points; the formula is not applicable. A parametric plane P+su+tv requires independent directions. With dependent directions it is a line or point, so labeling it a plane would misidentify the problem.

## 9. Cross products, oriented area, and volume

### 9.1 A separate operation in three-dimensional real space

The usual cross product produces a vector perpendicular to two input vectors in oriented real three-space. It is not the dot product, and its standard coordinate formula is not an operation on arbitrary n-component lists. Define it in a right-handed orthonormal coordinate system:

<div class="formula-block">u×v = (u₂v₃−u₃v₂, u₃v₁−u₁v₃, u₁v₂−u₂v₁).</div>

Substituting into u·(u×v) makes all terms cancel in pairs; the same happens for v. Thus the result is perpendicular to both. Each coordinate is bilinear, and exchanging u and v negates it. The cyclic products of standard unit vectors obey e₁×e₂=e₃, e₂×e₃=e₁, and e₃×e₁=e₂. Reversing the order changes sign.

The determinant-shaped mnemonic with a top row of unit vectors is a memory device; the defining formula has ordinary scalar coordinates. Cross product is not associative. For example, (e₁×e₂)×e₂=−e₁ while e₁×(e₂×e₂)=0. One cannot move parentheses as with scalar multiplication.

### 9.2 The Lagrange identity proves the area formula

Expand ‖u‖²‖v‖²−(u·v)². Terms with identical indices cancel. Grouping the remaining terms by unordered pairs of indices gives a sum of squares:

<div class="formula-block formula-steps"><div>‖u‖²‖v‖²−(u·v)²</div><div>= ∑<sub>i&lt;j</sub> (uᵢvⱼ−uⱼvᵢ)².</div><div>= ‖u×v‖² in ℝ³.</div></div>

For nonzero inputs, the real angle formula turns the last equality into ‖u×v‖=‖u‖‖v‖sinθ. In [0,π], sine is nonnegative. This equals base times height, the parallelogram area. If either input is zero or they are parallel, the cross product and area vanish; the angle formula with zero remains undefined even though the area is perfectly defined.

The area of a triangle with points A,B,C is half ‖(B−A)×(C−A)‖. The differences are its side vectors; using raw point coordinates instead would generally depend on the arbitrary origin. Swapping two vertices reverses the oriented cross product but leaves the unsigned area unchanged.

### 9.3 Scalar triple product and coplanarity

The signed volume is u·(v×w). To understand it, take the area vector v×w: its length is the base-parallelogram area, and its direction is a unit normal times that area. Dotting with u multiplies area by the signed perpendicular height. The absolute value is the parallelepiped volume; dividing by six gives the tetrahedron volume with three edges from a common vertex.

<div class="formula-block">V = |u·(v×w)|.</div>

The scalar triple product is unchanged by cyclic permutations and negated by swapping two arguments, as coordinate expansion verifies. It is zero exactly when the three vectors are linearly dependent. If v and w are independent, their cross product is a nonzero normal, and zero dot product says u lies in their plane. If v and w are dependent, the triple is already zero and the three-vector list is necessarily dependent. Distinguish this zero-volume condition from the much stronger condition that every pair is parallel.

## 10. Interactive projection laboratory

The model below uses the real Euclidean plane and a fixed target x=(3,2). Change the direction angle, its length, and a candidate coefficient t. The green arrow is the exact projection p; the orange segment is the orthogonal residual. The purple point is the candidate tb. The reported squared distance separates the unavoidable residual from the extra error due to choosing the wrong coefficient. The laboratory models geometry; it does not simulate floating-point rank determination or general matrix least squares.

At zero direction length, span(b) is the zero subspace. Projection remains zero, while division-based coefficients and a direction angle for the zero vector are not defined. The display handles this case explicitly rather than dividing by zero. The slider's orientation then has no geometric effect.

<div class="lab vector-lab">
<div class="vector-controls"><label for="vector-angle">Direction orientation: <output id="angle-label">60°</output></label><input id="vector-angle" type="range" min="0" max="180" value="60" step="1"><label for="vector-length">Direction length: <output id="length-label">1.00</output></label><input id="vector-length" type="range" min="0" max="200" value="100" step="5"><label for="vector-candidate">Candidate coefficient: <output id="candidate-label">0.00</output></label><input id="vector-candidate" type="range" min="-500" max="500" value="0" step="5"></div>
<svg id="vector-canvas" viewBox="0 0 560 420" role="img" aria-label="Dynamic two dimensional projection and candidate distance"><defs><marker id="lab-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="none" stroke="context-stroke"/></marker></defs><g id="vector-drawing"></g></svg>
<div id="vector-result" aria-live="polite"></div>
<p>Diagram legend: blue target; green projection; orange residual; purple candidate. Large candidate points can lie outside the displayed window; their computed distances still appear below.</p>
</div>

For a guided observation, choose an orientation near 146 degrees, approximately perpendicular to the target: the green arrow becomes very short while almost the entire target becomes residual. Compare orientations 0 and 180 degrees: the coefficient changes sign, but the projected point stays on the same line. Decrease direction length without changing its orientation: the projected point stays fixed while the coefficient grows. These are different quantities, not a contradiction.
