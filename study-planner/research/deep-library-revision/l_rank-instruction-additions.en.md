# Targeted explanations added after individual review

## A complete rank-and-fiber examination decision sequence

Begin with the field and the shape $A\in F^{m\times n}$. Record two different coordinate spaces: the input has dimension $n$ and the output has dimension $m$. If a load is present, keep it separate from coefficient columns throughout reduction. A pivot in an augmented load column certifies inconsistency; it is not another solved input coordinate.

Next certify the rank with matching lower and upper bounds. An explicit independent column list or a nonzero minor proves a lower bound. A complete echelon reduction, a spanning dependency description, or vanishing of all larger minors proves an upper bound. One zero minor, many visible nonzero entries or the number of original equations alone cannot supply the complete certificate. For parameter families, retain branches where candidate pivots vanish before dividing.

Once $r$ is known, compute right nullity $n-r$ and left nullity $m-r$ separately. Extract an image basis from the original pivot columns, a row-space basis from nonzero reduced rows, and a right-kernel basis from independent free-coordinate patterns. Check matrix annihilation, independence and the expected number of basis vectors. A zero-dimensional space has an empty basis.

For an actual load, test $b\in\operatorname{Col}A$, equivalently coefficient/augmented rank equality. Over the reals, the left-kernel test $Y^Tb=0$ supplies explicit independent compatibility equations. If the test fails, stop: there is no fiber to parameterize. If it succeeds, construct one particular input and add every kernel direction. Substitute the resulting formula into the original equations, not only the reduced coefficients. Report both a load criterion and a full input family whenever the question requests all solutions.

Finally interpret the result. Full column rank means uniqueness for compatible loads and existence of a left inverse. Full row rank means existence for every load and existence of a right inverse. Only finite equal dimensions identify those two conditions. For a composition, restrict the next map to the actually reached intermediate image. For a sum, keep track of shared input coordinates as well as output subspaces. For constraints on matrices or polynomials, build the linear constraint map before subtracting dimensions.

## Which kernel tests which membership question?

For a real $m\times n$ matrix $A$, a column-space membership question concerns an $m$-coordinate output $b$. Every left-kernel vector $y\in\mathbb R^m$ obeys $y^TA=0$, so an attainable output must satisfy $y^Tb=0$. The left kernel provides output restrictions.

A row-space membership question instead concerns an $n$-coordinate row $x$. Every right-kernel vector $z\in\mathbb R^n$ obeys $Az=0$, so a row combination must satisfy $xz=0$. The right kernel provides restrictions on possible rows. In each case the annihilator condition is sufficient because the containing orthogonal complement has the same finite dimension as the requested space. This is a dimension argument after an obvious containment, not an assumption that all spaces with the same dimension are equal.

For example, the three independent rows in LR88 occupy a three-dimensional hyperplane in $\mathbb R^4$. Their right kernel is one-dimensional and supplies its single membership equation. Their left kernel is zero-dimensional and supplies no output-load restriction for the onto map $A:\mathbb R^4\to\mathbb R^3$. The two conclusions are consistent because they concern different ambient spaces. For complex inner-product statements use conjugate transpose. Over a general field use the natural dual-space annihilator pairing instead of assuming positivity.
