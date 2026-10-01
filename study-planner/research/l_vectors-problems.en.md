## 11. Worked problem bank: explanations, checks, and traps

The following 34 problems are independently written. A course attribution names the exercise type that informed the problem, not a reproduced statement. “Original synthesis” indicates a new combination, diagnostic example, or independently derived extension. No archived Iranian entrance-exam question was used. Read each solution before attempting parallel examples; you are not being asked to sit a test now.

### Problem 1 — Points are not displacements

**Task.** Points A=(2,−1,3) and B=(−1,4,5) are given. Find the displacement from A to B, the midpoint, and the distance. Explain what changes when the origin is translated by h=(7,0,−2). **Pattern:** Oxford vectors and coordinate choice; original data.

**Solution.** The directed displacement is B−A=(−3,5,2); reversing endpoints negates it. The midpoint is A+(B−A)/2=(1/2,3/2,4). The squared distance is 9+25+4=38, so the distance is √38. Under the translated origin, coordinates become A−h and B−h. Their difference is still B−A, and therefore the distance is unchanged. The midpoint coordinates change by subtracting h, because a midpoint is a point. This distinguishes an invariant displacement from a coordinate-dependent point description.

### Problem 2 — Recover coordinates in a nonstandard basis

**Task.** For b₁=(1,2) and b₂=(2,−1), represent x=(7,4) and determine whether the coefficient list is unique. **Pattern:** Stanford coordinate extraction; independently worded.

**Solution.** Write x=ab₁+bb₂. Comparing coordinates gives a+2b=7 and 2a−b=4. From the second equation b=2a−4. Substitute into the first: 5a−8=7, so a=3 and b=2. Reconstructing gives 3(1,2)+2(2,−1)=(7,4). For uniqueness, the homogeneous equations a+2b=0 and 2a−b=0 imply 5a=0, then b=0. The two vectors are independent and span the plane, hence form a basis. The basis coordinates (3,2) are not the standard coordinates (7,4).

### Problem 3 — A redundant generator and a membership constraint

**Task.** Let u=(1,0,1), v=(0,1,1), and w=(1,1,2). Characterize their span and all representations of (2,3,5). **Pattern:** Oxford span and dependence; original data.

**Solution.** Since w=u+v, adding w does not enlarge span(u,v). A combination au+bv has coordinates (a,b,a+b), so the span is exactly the plane z=x+y. The target satisfies 5=2+3, hence belongs. In au+bv+cw the first two coordinates are a+c and b+c. Thus a=2−c and b=3−c; the third is then automatically 5. Every real c gives a representation. The projected or represented vector can be unique while coefficients in a dependent generating list are not. Removing w restores unique coordinates (2,3).

### Problem 4 — Classify subspaces instead of trusting their shape

**Task.** Decide whether each subset of the real plane is a subspace: x+2y=0; x+2y=1; xy=0; and y≥0. **Pattern:** Oxford subspace test; original diagnostic set.

**Solution.** The first contains zero and is closed: if two points satisfy the equation, every linear combination does too by distributing its left side. It is a line subspace. The second excludes zero, so it fails immediately; it is an affine line. The third is the union of coordinate axes. It contains zero, but (1,0)+(0,1)=(1,1) violates xy=0. The fourth contains zero and is closed under addition, yet scalar multiplication by −1 sends (0,1) outside. A single failed requirement settles rejection; several satisfied requirements cannot compensate for it.

### Problem 5 — Norm, distance, and RMS are different quantities

**Task.** For x=(1,−2,2) and y=(−1,1,2), find the norm of x, its RMS value, and its distance from y. **Pattern:** Stanford norm and RMS; original data.

**Solution.** Squared norm is 1+4+4=9, so ‖x‖=3. RMS divides the sum of squares by the number of coordinates before taking the root: √(9/3)=√3. The displacement x−y=(2,−3,0) has squared norm 4+9=13, so the distance is √13. Norm measures distance from zero; distance from y requires subtraction; RMS incorporates dimension-dependent averaging. None of these computations uses the sum of the coordinates, which here would misleadingly give 1.

### Problem 6 — An angle and its zero-vector exception

**Task.** Find the angle between u=(1,1,0) and v=(1,0,1). Then explain the meaning of orthogonality between u and zero. **Pattern:** MIT dot-product geometry; independently worded.

**Solution.** The dot product is 1. Both norms are √2, so the cosine is 1/2 and the angle is π/3. The zero vector has dot product zero with u and is therefore orthogonal by definition. However, its norm is zero, so the angle ratio would divide by zero. There is no angle involving that vector. These two statements coexist because orthogonality is an algebraic condition and the angle formula has an additional domain restriction.

### Problem 7 — Recover a dot product from norm data

**Task.** Real vectors satisfy ‖u‖=3, ‖v‖=4, and ‖u−v‖=5. Find their dot product and the norm of u+v. **Pattern:** Berkeley norm expansions; original data.

**Solution.** Expanding the difference gives 25=9+16−2u·v, so u·v=0. The sum expansion then gives ‖u+v‖²=9+16=25, so its norm is 5. This is Pythagoras inferred from lengths, not a assumption that any two vectors with these lengths are orthogonal. It is valid here for real inner-product geometry. In a complex space the same calculation identifies only the real part of the inner product; Problem 15 explains the difference.

### Problem 8 — Distinguish equality in two inequalities

**Task.** Let u=(1,−2) and v=−3u. Compare equality in Cauchy–Schwarz and triangle inequality. **Pattern:** Oxford inequality equality cases; original diagnostic.

**Solution.** The lengths are √5 and 3√5. Their dot product is −15, whose absolute value equals √5·3√5=15, so Cauchy–Schwarz is an equality. Their sum is −2u, with norm 2√5, while the sum of their norms is 4√5. Triangle inequality is strict because the directions oppose one another. Linear dependence is enough for absolute Cauchy–Schwarz equality; nonzero triangle equality requires proportionality with a positive scalar. Replacing v by 3u makes both equalities hold.

### Problem 9 — Optimize a linear functional without calculus

**Task.** Maximize and minimize 2x−y+2z subject to x²+y²+z²=9. **Pattern:** Original synthesis of Stanford inner products and Oxford equality conditions.

**Solution.** Put a=(2,−1,2) and h=(x,y,z). Both have norm 3 under the constraint. Cauchy–Schwarz gives |a·h|≤9. Equality occurs when h is parallel to a, and the prescribed norm fixes h to a or −a. The maximum 9 occurs at (2,−1,2), and the minimum −9 at (−2,1,−2). Checking the constraint confirms both points are feasible. The equality condition supplies the optimizer; a bare inequality would supply only a bound, not its attainability.

### Problem 10 — Determine feasibility before inventing coordinates

**Task.** Real vectors have lengths 2 and 3. Is dot product 7 possible? Is distance 1 possible? Find all equality requirements. **Pattern:** Original synthesis.

**Solution.** The dot-product magnitude cannot exceed 6, so 7 is impossible. Reverse triangle inequality says distance is at least |3−2|=1. This minimum is attainable when both vectors point in the same direction: take u=(2,0), v=(3,0). Their dot product is 6. Equality at the minimum requires same-direction proportionality for these positive lengths. The maximum distance is 5, attained with opposite directions. In at least two real dimensions distances between 1 and 5 can be obtained by changing the angle; in one dimension only 1 and 5 occur.

### Problem 11 — Find the exact parameter range for an inner product

**Task.** Analyze B(x,y)=x₁y₁+a(x₁y₂+x₂y₁)+x₂y₂ on the real plane. **Pattern:** Berkeley general inner products; original parameterization.

**Solution.** Bilinearity and symmetry hold for every real a. The missing requirement is definiteness. On the diagonal, B(x,x)=(x₁+ax₂)²+(1−a²)x₂². When |a|&lt;1, the two terms force x₂=0 and then x₁=0 if their sum vanishes, so the form is positive definite. At a=1, the nonzero vector (1,−1) has zero self-product; at a=−1, use (1,1). For |a|&gt;1, take x=(−a,1), giving 1−a²&lt;0. The exact answer is −1&lt;a&lt;1; checking symmetry alone would miss the essential condition.

### Problem 12 — Test whether a familiar norm is Euclidean geometry

**Task.** Could ‖(x,y)‖₁=|x|+|y| be induced by any inner product on the plane? **Pattern:** Original boundary example.

**Solution.** Every inner-product norm satisfies the parallelogram identity. For u=(1,0) and v=(0,1), both individual norms are 1. The sum and difference each have norm 2. The left side of the identity would be 2²+2²=8, while the right side is 2·1²+2·1²=4. Thus no inner product induces this norm. It is still a genuine norm: positivity and homogeneity are immediate, and triangle inequality follows by applying |a+b|≤|a|+|b| separately to each coordinate. Being a norm is weaker than being an inner-product norm.

### Problem 13 — Sampling can create a zero-length nonzero polynomial

**Task.** On real polynomials of degree at most two, decide whether B(f,g)=f(−1)g(−1)+f(1)g(1) is an inner product. Repair it. **Pattern:** Berkeley sampled polynomial geometry; original data.

**Solution.** It is symmetric and bilinear, with nonnegative self-products. But f(t)=t²−1 is nonzero and vanishes at both samples, so B(f,f)=0. Definiteness fails. Add the distinct sample t=0 with a strictly positive weight, for example B̃(f,g)=B(f,g)+f(0)g(0). If B̃(f,f)=0, all three sampled values vanish. A nonzero polynomial of degree at most two has at most two distinct roots, so f must be zero. Three distinct samples repair the form on this particular degree-bounded space; they do not repair it on polynomials of arbitrary degree.

### Problem 14 — Verify the complex convention numerically

**Task.** For u=(1,i) and v=(i,1), calculate both ordered inner products and the norm of u. **Pattern:** Oxford complex extension; independent convention translation.

**Solution.** Under first-argument conjugation, ⟨u,v⟩=1·i+(−i)·1=0. The reverse product is (−i)·1+1·i=0 as conjugate symmetry requires. The squared norm is |1|²+|i|²=2, so the norm is √2. The naive nonconjugated self-product would be 1+i²=0 and is invalid as a squared norm. To see that ordered products need not be equal, take a=(1) and b=(i): ⟨a,b⟩=i while ⟨b,a⟩=−i. Conjugate symmetry, not ordinary symmetry, is the rule.

### Problem 15 — Complex Pythagoras does not imply orthogonality

**Task.** Use one-dimensional complex vectors x=1 and y=i to test the converse of Pythagoras. **Pattern:** Original boundary example.

**Solution.** Their squared norms are both 1, and |1+i|²=2, so the norm equality ‖x+y‖²=‖x‖²+‖y‖² holds. Yet ⟨x,y⟩=i, which is nonzero. The correct expansion is ‖x+y‖²=‖x‖²+2 Re⟨x,y⟩+‖y‖². Here the real part vanishes, but the imaginary part does not. Complex orthogonality implies Pythagoras; its converse requires more than this single equality. In the corresponding real two-dimensional interpretation, those two directions are orthogonal because that geometry uses the real part.

### Problem 16 — Compute every projection quantity and verify it

**Task.** Project x=(2,−1,3) onto b=(1,2,2). Give the coefficient, signed scalar component, projected vector, residual, and distance. **Pattern:** MIT components and Berkeley projection; original data.

**Solution.** The dot product is 2−2+6=6 and ‖b‖²=9. Thus c=2/3, the signed scalar component is 6/3=2, and p=(2/3,4/3,4/3). Subtracting gives r=(4/3,−7/3,5/3). Check orthogonality: r·b=(4−14+10)/3=0. Its squared norm is (16+49+25)/9=10, so the distance is √10. Finally ‖x‖²=14, ‖p‖²=4, and 14=4+10 verifies the decomposition. The coefficient 2/3, component 2, and vector p answer different questions.

### Problem 17 — Solve the coupled equations for a nonorthogonal basis

**Task.** Project x=(0,1) onto W=span((1,0),(1,1)). Explain why the sum of separate one-direction projections fails. **Pattern:** Original diagnostic of Berkeley's orthogonal-basis condition.

**Solution.** The two directions form a basis of the whole plane, so the correct projection is x itself. The separate projection sum would be (0,0)+(1/2,1/2), which is wrong. Derive the coefficients instead: p=c₁(1,0)+c₂(1,1), and force the residual perpendicular to both directions. This gives c₁+c₂=0 and c₁+2c₂=1. Solving gives c₂=1 and c₁=−1, so p=(0,1). The cross inner product is 1, so the two coefficients are coupled; the separate-projection shortcut wrongly discards this interaction.

### Problem 18 — A two-dimensional span inside three-space

**Task.** Project x=(1,2,3) onto the span of b₁=(1,−1,0) and b₂=(1,1,−2). **Pattern:** Berkeley orthogonal projections; independently written data.

**Solution.** First check b₁·b₂=1−1+0=0. The squared lengths are 2 and 6, while inner products with x are −1 and −3. Thus both expansion coefficients are −1/2, giving p=(−1,0,1). The residual is (2,2,2), perpendicular to both directions; its squared length is 12. This makes distance 2√3. The span is the plane of coordinate sum zero, consistent with the projected vector. We used an orthogonal but nonunit basis, so the denominators 2 and 6 were essential.

### Problem 19 — The same span has a different weighted projection

**Task.** Use ⟨x,y⟩=4x₁y₁+x₂y₂ to project x=(1,0) onto b=(1,1). Compare ordinary Euclidean projection. **Pattern:** Original synthesis of general geometry and projection.

**Solution.** The weighted inner product ⟨b,x⟩ is 4 and ⟨b,b⟩ is 5. Thus p=(4/5,4/5), and r=(1/5,−4/5). Weighted orthogonality is 4·(1/5)+(−4/5)=0. Weighted squared distance is 4/25+16/25=4/5. Ordinary Euclidean projection would be (1/2,1/2); its residual is perpendicular under the ordinary dot product, but not under the weighted one. The vector space and line have not changed; the definition of distance has changed, and so has its minimizing point.

### Problem 20 — An imaginary projection coefficient must have the right sign

**Task.** Project x=(i,0) onto the complex line generated by b=(1,i), using the chapter's convention. **Pattern:** Original complex projection diagnostic.

**Solution.** Compute ⟨b,x⟩=i and ⟨b,b⟩=2. The coefficient is i/2, so p=(i/2,−1/2). The residual r=(i/2,1/2) satisfies ⟨b,r⟩=i/2−i/2=0. Both residual and projection have squared norm 1/2, adding to ‖x‖²=1. If one mistakenly uses ⟨x,b⟩=−i, the proposed coefficient changes sign. Its residual has inner product 2i with b, so it is not orthogonal and not optimal. The residual check detects a convention error more reliably than memorizing a numerator order.

### Problem 21 — Carry Gram–Schmidt through three directions

**Task.** Orthonormalize v₁=(1,1,0), v₂=(1,0,1), and v₃=(0,1,1), in that order. **Pattern:** Stanford Gram–Schmidt; independent data and calculations.

**Solution.** Normalize v₁ to q₁=(1,1,0)/√2. The coefficient of v₂ along q₁ is 1/√2. Subtracting gives w₂=(1/2,−1/2,1), hence q₂=(1,−1,2)/√6. For v₃ the coefficients are 1/√2 and 1/√6. Subtracting both components gives w₃=(−2/3,2/3,2/3), whose normalization is q₃=(−1,1,1)/√3. Pairwise dot products vanish: the numerators are 1−1, −1+1, and −1−1+2. Each numerator vector has squared length equal to its denominator squared, so the list is orthonormal. It spans all three inputs by the algorithm's invariant.

### Problem 22 — Dependent and zero inputs are skipped, not normalized

**Task.** Apply Gram–Schmidt to (1,1), (2,2), (0,0), and (1,−1). **Pattern:** Stanford dependent-input extension; independent data.

**Solution.** The first retained direction is (1,1)/√2. The second is twice the first original vector, so subtracting its projection leaves exactly zero. Skip it. The zero input also leaves zero and is skipped. The last input is already perpendicular to the retained direction because 1−1=0; normalize it to (1,−1)/√2. The final list has two members, a basis of the plane. Trying to produce four unit vectors would divide by zero at the second step. The number of original entries is not necessarily the dimension of their span.

### Problem 23 — Gram–Schmidt changes when the metric changes

**Task.** Orthonormalize v₁=(1,1), v₂=(1,0) under ⟨x,y⟩=4x₁y₁+x₂y₂. **Pattern:** Original weighted extension.

**Solution.** The first norm is √5, so q₁=(1,1)/√5. The first coefficient for v₂ is 4/√5. Thus w₂=(1,0)−(4/5)(1,1)=(1/5,−4/5). Its weighted squared norm is 4/5, hence q₂=(1,−4)/(2√5). Weighted orthogonality has numerator 4−4=0. Its norm check gives (4+16)/(4·5)=1. Under the ordinary dot product the two vectors are not orthogonal. The algorithm does not prescribe one universal geometry; every projection and normalization must use the same chosen inner product.

### Problem 24 — Projection onto a shifted line

**Task.** Find the nearest point to X=(4,0) on L=(1,2)+t(2,1). **Pattern:** MIT geometry plus affine translation; original data.

**Solution.** Subtract the base point: x=X−(1,2)=(3,−2). Its dot product with b=(2,1) is 4, and ‖b‖²=5, so t=4/5. Translate back to Q=(1,2)+(4/5)(2,1)=(13/5,14/5). The residual X−Q=(7/5,−14/5) is perpendicular to b because 14/5−14/5=0. Its squared norm is 49/5, so distance is 7/√5. Directly projecting X onto b would find a nearest point on a different line through zero and would fail the required geometry.

### Problem 25 — Plane foot and signed distance

**Task.** Find the nearest point to X=(3,1,2) on x+2y+2z=3. **Pattern:** Original affine-plane synthesis.

**Solution.** The normal is n=(1,2,2), with squared norm 9. Its dot product with X is 9, so the signed equation residual is 9−3=6. Subtract (6/9)n to obtain Q=(7/3,−1/3,2/3). Substitution gives 7/3−2/3+4/3=3, verifying plane membership. The displacement X−Q=(2/3,4/3,4/3) is parallel to n, proving perpendicularity to the plane directions. Its length is 2. The signed distance along the oriented unit normal is +2; reversing both normal and equation orientation reverses that sign while leaving the unsigned distance unchanged.

### Problem 26 — Recover the orthogonal complement and its dimensions

**Task.** For W=span((1,0,1),(0,1,1)), find W⊥ and decompose x=(1,2,0). **Pattern:** Berkeley complement geometry; original data.

**Solution.** A vector (a,b,c) in the complement must satisfy a+c=0 and b+c=0. Thus W⊥=span((1,1,−1)). Its dimension is one, while W has dimension two. The normal component of x is r=((x·n)/(n·n))n=(3/3)n=(1,1,−1). The W component is p=x−r=(0,1,1), which belongs to W. The squared norms are 5=2+3, verifying Pythagoras. The intersection contains exactly zero because a vector in both spaces is perpendicular to itself. It is not empty.

### Problem 27 — Triangle area with a coordinate-origin check

**Task.** For A=(1,0,0), B=(2,1,0), and C=(1,1,2), find the triangle's area and an oriented normal. **Pattern:** MIT cross-product area; original data.

**Solution.** Form sides u=B−A=(1,1,0) and v=C−A=(0,1,2). Their cross product is (2,−2,1), with squared length 9. Thus the parallelogram area is 3 and the triangle area is 3/2. A unit normal is (2,−2,1)/3. Dotting the normal numerator with either side gives zero. Reversing B and C changes the normal sign but not the area. Translating every point by the same vector preserves both side differences; this confirms that the area calculation does not depend on the chosen origin.

### Problem 28 — Signed volume, unsigned volume, and degeneracy

**Task.** Compute the parallelepiped and tetrahedron volumes for u=(1,0,1), v=(0,2,0), w=(1,1,0). **Pattern:** Original scalar-triple extension of MIT area.

**Solution.** Compute v×w=(0,0,−2). Dotting with u gives −2, a signed volume. The parallelepiped volume is its absolute value 2; a tetrahedron with these three edge vectors from one vertex has volume 2/6=1/3. The negative sign expresses orientation, not a negative physical volume. Replacing w by u+v would make the triple product zero because the third edge lies in the plane of the first two. That degeneracy does not require the first two directions themselves to be parallel.

### Problem 29 — Verify that cross product is not associative

**Task.** Compare (u×v)×v and u×(v×v), where u=(1,0,0) and v=(0,1,0). **Pattern:** MIT nonassociativity; independently explained canonical example.

**Solution.** The first product u×v is (0,0,1). Crossing it with v gives (−1,0,0). The other expression begins with v×v=0, so its final result is zero. They differ. Bilinearity lets us distribute a cross product across addition, but does not permit reassociation. For instance, u×(v+w) can be expanded as u×v+u×w, whereas parentheses in a repeated cross product must be retained. This distinction prevents transferring scalar algebra rules to a different operation.

### Problem 30 — A polynomial projection and a source-slip diagnostic

**Task.** Under ⟨f,g⟩=∫<sub>−1</sub><sup>1</sup>f(t)g(t)dt, project t³ onto span(1,t²). **Pattern:** Berkeley Inner Product Spaces p. 4; independently recomputed correction.

**Solution.** First orthogonalize: the constant has squared norm 2, and ⟨1,t²⟩=2/3, so the second orthogonal vector is t²−1/3. Its squared norm is ∫(t⁴−(2/3)t²+1/9)dt=2/5−4/9+2/9=8/45. But both coefficients for t³ vanish. Its product with 1 is odd, and its product with t²−1/3 is t⁵−t³/3, also odd. Integrating over the symmetric interval therefore gives zero in both cases. The projection is the zero polynomial, with squared residual norm ∫t⁶dt=2/7. A claimed nonzero coefficient fails parity before any lengthy integration is attempted.

### Problem 31 — The best affine approximation to a quadratic

**Task.** Find the polynomial a+bt closest to t² in the same integral geometry on [−1,1]. **Pattern:** Original companion to Berkeley polynomial projection.

**Solution.** The basis 1,t is orthogonal because the integral of t is zero. Its squared lengths are 2 and 2/3. The target inner products are 2/3 and 0, giving a=1/3 and b=0. The residual t²−1/3 is perpendicular to both basis functions. Its squared norm is 8/45, as computed directly in Problem 30. For any other affine polynomial a+bt, the error separates into 8/45+2(a−1/3)²+(2/3)b². The nonnegative extra terms prove unique optimality, turning the approximation formula into a complete minimization argument.

### Problem 32 — Finite trigonometric orthogonality with frequency restrictions

**Task.** On [−π,π], compute ⟨sin t,cos 2t⟩, ⟨cos t,cos 2t⟩, and the norms of 1 and cos t. Explain the negative-frequency exception. **Pattern:** Oxford Example 208, with explicit assumptions and independent explanation.

**Solution.** The first integrand is odd, so its integral is zero. Product-to-sum gives <span class="math-inline">cos t cos 2t=(cos 3t+cos t)/2</span>; each cosine integrates to zero on this interval, so the second inner product is zero. The squared constant norm is 2π. Using <span class="math-inline">cos²t=(1+cos 2t)/2</span> gives squared cosine norm π. Distinct positive integer frequencies are orthogonal. Distinct signed integers are insufficient: <span class="math-inline">cos(−t)=cos t</span>, so their inner product is π, not zero. This is a finite calculation and makes no assertion about convergence of an infinite Fourier expansion.

### Problem 33 — Bessel's inequality distinguishes projection from reconstruction

**Task.** Let q₁=(1,1,0)/√2 and q₂=(1,−1,0)/√2. For x=(2,1,3), extract coefficients, project, and test Parseval. **Pattern:** Stanford orthonormal coordinates; original data.

**Solution.** Coefficients are 3/√2 and 1/√2. Their expansion gives p=(2,1,0), leaving r=(0,0,3). The sum of coefficient squares is 9/2+1/2=5, while ‖x‖²=14. Bessel's inequality holds, and the difference 9 is precisely ‖r‖². Parseval equality does not hold for this two-vector list because it is only a basis of the xy-plane. Appending q₃=(0,0,1) gives a basis of the whole space and coefficient 3; now the total is 14. Orthonormality alone does not guarantee complete reconstruction.

### Problem 34 — Projection structure and near dependence

**Task.** Explain why an orthogonal projection cannot increase distances. Then orthogonalize v₁=(1,0) and v₂=(1,ε) and discuss the limit ε→0. **Pattern:** Original synthesis of Stanford projection and numerical cautions.

**Solution.** Projection is linear, so Px−Py=P(x−y). Orthogonal decomposition yields ‖z‖²=‖Pz‖²+‖z−Pz‖², hence ‖Px−Py‖≤‖x−y‖. Equality occurs exactly when x−y lies in the target span. For the two inputs, q₁=(1,0) and the second residual is (0,ε). If ε is exactly zero it is skipped; otherwise normalization gives (0,sign ε). Thus every nonzero ε produces the full plane, while ε=0 produces a line. Small magnitude alone is not mathematical dependence. In finite precision, whether that tiny residual represents a meaningful direction depends on error scale and data uncertainty; an implementation must state its tolerance rather than silently substitute a numerical threshold for an exact theorem.
