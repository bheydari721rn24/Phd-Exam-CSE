# Matrices and Matrix Operations

**Approved English chapter · Linear Algebra, Chapter 2 · Prerequisite: Vectors and Inner Products.**

## 1. Scope, learning route, and source synthesis

A matrix is simultaneously an array, a collection of column vectors, and a rule for transforming coordinates. Learning only the array viewpoint makes multiplication look arbitrary. Learning only the transformation viewpoint can leave you unable to calculate a particular entry. This chapter develops both viewpoints and connects them through proofs, examples, and a laboratory.

Start with shapes and indexing, then learn matrix-vector multiplication. Derive matrix multiplication from composition before studying its algebraic rules. Finally connect transposes, structured matrices, inverse rules, block operations, powers, and exact computational costs. The worked bank and final review consolidate these connections with complete solutions and explicit failure cases.

The boundary is **matrix algebra**. Gaussian elimination, general solution classification, rank theorems, determinant expansion, eigendecomposition, and general singular-value theory have their own later chapters. Here an inverse is defined, its elementary identities are proved, and structured inverses are derived directly. Those later subjects are identified wherever they become relevant; they are not assumed silently.

### 1.1 Reviewed written courses

Four core courses were selected by comparing a documented pool of seven university offerings. A fifth course supplies useful applications. The survey and its reading limits are recorded in the accompanying source audit. Selection is based on this chapter's needs and accessible written evidence; it is not a claim to have read every course worldwide.

| Role | University and course | Written sections actually reviewed | Instructional contribution |
|---|---|---|---|
| Core | Stanford — Stephen Boyd, archival EE263 | Matrix Operations, Lecture 2, all 15 slides | Shapes, products, powers, transpose, inverse identities, and the two-by-two inverse |
| Core | Oxford — M1 Linear Algebra I, Michaelmas 2022; instructor Andrew Wathen | Printed pages 8–13 and 21–24 | Definitions, finite-sum proofs, structural matrix classes, and operation counts |
| Core | UC Berkeley — Alexander Paulin, Math 54, Spring 2018 | Matrix Algebra, all four handwritten pages | Addition and composition of linear transformations, basis images, and failures of cancellation |
| Core | MIT — Gilbert Strang, 18.06SC, Fall 2011 | Multiplication/inverse and transpose/permutation summaries; multiplication recitation and solutions | Four views of multiplication, block structure, and two attributed problem types |
| Supplement | CMU — William Gunther, 21-241, Summer I 2014 | Summary of Day 7, all four pages | Quantities-times-prices interpretation, coordinate selectors, and graph-walk connections |

This is an independently written synthesis, with new proofs, numerical examples, diagrams, and solutions. Source notation is reconciled to **column vectors** throughout. Actual slips in strict triangularity, identity dimensions, and row-operation labels are corrected rather than propagated. References identify the precise written materials at the end.

### 1.2 Conventions and expected outcomes

Unless a section says otherwise, entries are real and all dimensions are positive integers. Complex extensions are marked explicitly. A vector is a column vector, so a real inner product is x<sup>T</sup>y. A transpose changes shape; it is never merely a decorative superscript. For complex entries the adjoint A<sup>*</sup> means conjugate transpose, not ordinary transpose.

After studying the chapter, you should be able to determine whether an expression is defined before calculating it; compute a product through any of four equivalent views; derive the matrix of a composition in the correct order; prove algebraic identities with compatible dimensions; detect invalid scalar-algebra shortcuts; and solve structured matrix problems without unnecessary full multiplication.

## 2. Matrices as shaped arrays

### 2.1 Dimensions are part of the object

An m-by-n matrix has m rows and n columns. Its entry a<sub>ij</sub> is in row i and column j. The first index selects the row; the second selects the column. The ranges are 1 ≤ i ≤ m and 1 ≤ j ≤ n. A matrix with three rows and two columns is not interchangeable with a matrix with two rows and three columns, even though both have six entries.

<div class="formula-block">A = @M{1,−2,4;0,3,5}, &nbsp; A ∈ ℝ<sup>2×3</sup>, &nbsp; a<sub>12</sub> = −2, &nbsp; a<sub>23</sub> = 5.</div>

The second row is the one-by-three matrix @M{0,3,5}; the second column is the **two-by-one** matrix @M{−2;3}. Its two entries correspond to the two rows of A. This simple distinction prevents many later product errors.

Two matrices are equal exactly when their shapes agree and all corresponding entries agree. To prove a matrix identity entrywise, first show both sides have the same shape, then fix arbitrary valid indices and prove equality of that entry. Equality of one entry or equality of row sums is insufficient.

A row vector in ℝ<sup>n</sup> is represented by a one-by-n matrix; a column vector by an n-by-one matrix. They contain the same number of coordinates, but their multiplication behavior differs. Converting between them requires a transpose.

### 2.2 Zero, identity, and matrix units

The zero matrix 0<sub>m×n</sub> has every entry zero. Different shapes give different zero matrices. Writing a bare zero is safe only when the surrounding expression fixes its shape.

The identity I<sub>n</sub> is square. Its entries are given by the Kronecker delta: δ<sub>ij</sub> is one when i = j and zero otherwise. Multiplication by an identity therefore selects the one term with a matching index.

<div class="formula-block">I<sub>3</sub> = @M{1,0,0;0,1,0;0,0,1}, &nbsp; I<sub>m</sub>A = A = AI<sub>n</sub> for A ∈ ℝ<sup>m×n</sup>.</div>

The two identities may have different sizes. An identity on the left must match the number of rows; an identity on the right must match the number of columns. This is a useful example of a correct-looking symbolic statement whose missing dimensions can conceal an error.

Let e<sub>i</sub> denote the appropriate standard column vector. The matrix unit E<sub>ij</sub> = e<sub>i</sub>e<sub>j</sub><sup>T</sup> has one at entry (i,j) and zeros elsewhere. Every m-by-n matrix can be assembled from its units:

<div class="formula-block">A = ∑<sub>i=1</sub><sup>m</sup> ∑<sub>j=1</sub><sup>n</sup> a<sub>ij</sub>E<sub>ij</sub>.</div>

At a fixed entry (r,s), every term vanishes except a<sub>rs</sub>E<sub>rs</sub>. That proves the expansion. It also proves that the mn matrix units are linearly independent: a zero linear combination forces every coefficient to vanish by inspecting its own entry. Thus matrices of fixed shape behave like vectors with mn coordinates under addition and scaling. Multiplication introduces additional structure and different compatibility rules.

For compatible matrix units, E<sub>ij</sub>E<sub>kl</sub> = δ<sub>jk</sub>E<sub>il</sub>. The middle index must match. This compact rule can produce counterexamples and select individual rows or columns without multiplying entire arrays.

### 2.3 Addition, scaling, and linear combinations

Addition is defined only for matrices of the same shape. It adds corresponding entries. Scalar multiplication multiplies every entry by the scalar. A linear combination of matrices requires every summand to have the same shape.

<div class="formula-block">(A+B)<sub>ij</sub> = a<sub>ij</sub> + b<sub>ij</sub>, &nbsp; (αA)<sub>ij</sub> = αa<sub>ij</sub>.</div>

The usual vector-space laws follow from scalar arithmetic at each entry. For example, the (i,j) entry of α(A+B) is α(a<sub>ij</sub>+b<sub>ij</sub>), which equals αa<sub>ij</sub>+αb<sub>ij</sub>. Therefore α(A+B) = αA+αB. The same argument proves commutativity and associativity of addition, additive inverses, and compatibility of repeated scaling.

These facts justify collecting terms such as 3A−2A = A. They do not justify exchanging factors in AB. Addition and multiplication must be learned as separate operations with separate hypotheses.

## 3. Matrix-vector multiplication and coordinate meaning

### 3.1 The column-combination definition

Write A = [a<sub>1</sub> … a<sub>n</sub>], with each a<sub>j</sub> a column in ℝ<sup>m</sup>. For a vector x with n coordinates, define:

<div class="formula-block">Ax = x<sub>1</sub>a<sub>1</sub> + ⋯ + x<sub>n</sub>a<sub>n</sub>, &nbsp; (Ax)<sub>i</sub> = ∑<sub>j=1</sub><sup>n</sup> a<sub>ij</sub>x<sub>j</sub>.</div>

The output has m coordinates. Each input coordinate weights one column. The row viewpoint gives the same output: each row of A computes one weighted sum of the input coordinates. The column viewpoint explains where outputs can lie; the row viewpoint computes individual outputs.

For the earlier matrix and x = (2,1,−1)<sup>T</sup>, the first output is 2−2−4 = −4 and the second is 0+3−5 = −2. From columns, the same calculation is twice (1,0)<sup>T</sup>, plus (−2,3)<sup>T</sup>, minus (4,5)<sup>T</sup>.

### 3.2 Columns are images of basis vectors

Because e<sub>j</sub> has only one nonzero coordinate, Ae<sub>j</sub> = a<sub>j</sub>. A column tells you what the matrix does to the corresponding input basis direction. For a linear map T, every vector is a combination of basis vectors, and linearity gives:

<div class="formula-block">T(x) = ∑<sub>j=1</sub><sup>n</sup> x<sub>j</sub>T(e<sub>j</sub>).</div>

Consequently the unique standard matrix of T has columns T(e<sub>j</sub>). To construct a two-dimensional transformation matrix, calculate the images of the horizontal and vertical unit vectors and place them in columns. Placing them in rows creates the transpose and generally the wrong map.

For a horizontal shear, the horizontal basis vector stays fixed while the vertical basis vector moves to (s,1)<sup>T</sup>. Thus:

<div class="formula-block">S(s) = @M{1,s;0,1}, &nbsp; S(s)@M{x;y} = @M{x+sy;y}.</div>

The map adds a multiple of the vertical coordinate to the horizontal coordinate. It fixes every point on the horizontal axis, but it generally changes lengths and angles. The zero vector remains zero, as it must for a linear map. A translation by a nonzero constant vector fails this property and is affine rather than linear in these coordinates.

### 3.3 Coordinate selectors and entry recovery

Right multiplication by e<sub>j</sub> selects column j. Left multiplication by e<sub>i</sub><sup>T</sup> selects row i. Using both selects one entry:

<div class="formula-block">Ae<sub>j</sub> = column j of A, &nbsp; e<sub>i</sub><sup>T</sup>A = row i of A, &nbsp; e<sub>i</sub><sup>T</sup>Ae<sub>j</sub> = a<sub>ij</sub>.</div>

The dimensions of the selectors differ when the matrix is rectangular. The left selector has m coordinates, the right selector n coordinates. Entry recovery proves a valuable criterion: if Ax = Bx for every vector x of the input dimension, then A = B, because you can choose each basis vector in turn. Equality for one arbitrary-looking vector does not establish matrix equality.

## 4. Matrix multiplication through four equivalent views

### 4.1 Derive the definition from composition

Suppose B maps ℝ<sup>p</sup> into ℝ<sup>n</sup> and A maps ℝ<sup>n</sup> into ℝ<sup>m</sup>. To apply B and then A, the intermediate dimensions must agree. The composition's column j is A(Be<sub>j</sub>), which is A applied to column j of B. Therefore:

<div class="formula-block">A ∈ ℝ<sup>m×n</sup>, &nbsp; B ∈ ℝ<sup>n×p</sup> ⇒ AB ∈ ℝ<sup>m×p</sup>, &nbsp; (AB)x = A(Bx).</div>

This explains both the compatibility condition and the multiplication order. The rightmost factor acts first on a column vector. It also explains why multiplication does not multiply corresponding entries: composition sums over all intermediate coordinates.

### 4.2 View 1: one output entry

Let C = AB. Its entry is a row of A paired with a column of B:

<div class="formula-block">c<sub>ij</sub> = ∑<sub>k=1</sub><sup>n</sup> a<sub>ik</sub>b<sub>kj</sub>.</div>

The summation index k is a dummy index: changing its name consistently does not change the sum. The free indices i and j identify the output entry and must not disappear. The first factor contributes a fixed row, the second a fixed column. Their shared index is contracted.

For real entries this is a row-column dot product. For complex entries ordinary matrix multiplication still uses the same sum **without complex conjugation**. Calling it the Hermitian inner product would incorrectly conjugate one factor. Complex inner products are handled separately by the adjoint.

### 4.3 One rectangular example used throughout

Use the following compatible matrices:

<div class="formula-block">A = @M{1,−1,2;0,3,1}, &nbsp; B = @M{2,0;1,4;−1,2}, &nbsp; AB = @M{−1,0;2,14}.</div>

The top-left entry is 1·2+(−1)·1+2·(−1) = −1. The top-right is 1·0+(−1)·4+2·2 = 0. The bottom-left is 0·2+3·1+1·(−1) = 2; the bottom-right is 0·0+3·4+1·2 = 14. Note that an output entry can be zero although both its row and its column contain nonzero values. Cancellation occurs inside the sum.

<figure class="matrix-figure"><svg viewBox="0 0 720 210" role="img" aria-label="Row-column contraction and surviving output dimensions"><rect x="15" y="25" width="205" height="150" rx="12" fill="#edf4fb"/><rect x="258" y="25" width="205" height="150" rx="12" fill="#eef7f1"/><rect x="505" y="25" width="195" height="150" rx="12" fill="#fff4e5"/><text x="117" y="65" text-anchor="middle" class="diagram-math">A: m × n</text><text x="360" y="65" text-anchor="middle" class="diagram-math">B: n × p</text><text x="602" y="65" text-anchor="middle" class="diagram-math">AB: m × p</text><path d="M40 105H195" stroke="#39779d" stroke-width="15" opacity=".35"/><path d="M360 85V150" stroke="#438660" stroke-width="15" opacity=".35"/><circle cx="580" cy="105" r="9" fill="#bb7927"/><text x="117" y="145" text-anchor="middle" class="diagram-math">aᵢ₁ … aᵢₙ</text><text x="360" y="190" text-anchor="middle">Sum over the shared index</text><text x="602" y="145" text-anchor="middle" class="diagram-math">cᵢⱼ = Σₖ aᵢₖbₖⱼ</text><path d="M220 105H247M463 105H494" stroke="#6a7c8d" stroke-width="2"/><text x="235" y="95" text-anchor="middle" class="diagram-math">×</text><text x="479" y="95" text-anchor="middle" class="diagram-math">=</text></svg><figcaption>The shared coordinate index is summed out. The output retains the row index of the first factor and the column index of the second.</figcaption></figure>

### 4.4 View 2: entire columns

Column j of AB is A times column j of B. Thus each output column is a linear combination of A's columns, using the corresponding B column as coefficients. In the example, the first output column is twice the first A column plus the second A column minus the third A column, giving (−1,2)<sup>T</sup>. The second is zero times the first plus four times the second plus twice the third, giving (0,14)<sup>T</sup>.

This viewpoint is especially effective when B contains many zeros or when several right-hand sides are processed together. It also explains the meaning of AX = Y: each column of X is a separate input vector, and each column of Y its corresponding output.

### 4.5 View 3: entire rows

Row i of AB is row i of A multiplied by B. It is a linear combination of B's rows with coefficients from that A row. The first output row is row 1 of B minus row 2 plus twice row 3, giving (−1,0). The second is three times row 2 plus row 3, giving (2,14).

The row and column views are not competing definitions. They reorganize the same finite sums. The rows of AB lie in the span of B's rows, and the columns of AB lie in the span of A's columns. General rank inequalities follow later from this observation; no rank calculation is needed here.

### 4.6 View 4: a sum of outer products

Pair column k of A with row k of B. Their outer product is m-by-p. Sum these products over the shared index:

<div class="formula-block">AB = ∑<sub>k=1</sub><sup>n</sup> (column k of A)(row k of B).</div>

For the example, the three terms are:

<div class="formula-block">@M{2,0;0,0} + @M{−1,−4;3,12} + @M{−2,4;−1,2} = @M{−1,0;2,14}.</div>

Each individual term has all columns proportional to one vector, unless it is zero. Combining such simple maps produces the full product. At entry (i,j), the kth outer product contributes a<sub>ik</sub>b<sub>kj</sub>, so its sum exactly reproduces View 1. This is a proof of the equivalence, not merely an example.

For column vectors u and v, the real outer product uv<sup>T</sup> is a matrix, while v<sup>T</sup>u is a scalar. Their roles cannot be exchanged. Applied to x, the outer product gives u(v<sup>T</sup>x): first extract a scalar from x, then scale u by it. Problem 8 develops the consequence for products of two outer-product maps.

## 5. Composition, geometric order, and algebraic proofs

### 5.1 A composition diagram

<figure class="matrix-figure"><svg viewBox="0 0 720 190" role="img" aria-label="A product applies B first and A second"><rect x="20" y="35" width="160" height="100" rx="14" fill="#edf4fb"/><rect x="278" y="35" width="160" height="100" rx="14" fill="#eef7f1"/><rect x="540" y="35" width="160" height="100" rx="14" fill="#fff4e5"/><text x="100" y="75" text-anchor="middle" class="diagram-math">x ∈ ℝᵖ</text><text x="358" y="75" text-anchor="middle" class="diagram-math">Bx ∈ ℝⁿ</text><text x="620" y="75" text-anchor="middle" class="diagram-math">A(Bx) ∈ ℝᵐ</text><text x="100" y="110" text-anchor="middle">Input</text><text x="358" y="110" text-anchor="middle">Intermediate</text><text x="620" y="110" text-anchor="middle">Output</text><path d="M185 85H265M443 85H527" stroke="#487a92" stroke-width="3"/><path d="m255 79 10 6-10 6m262-12 10 6-10 6" fill="none" stroke="#487a92" stroke-width="3"/><text x="226" y="65" text-anchor="middle" class="diagram-math">B</text><text x="485" y="65" text-anchor="middle" class="diagram-math">A</text><text x="360" y="172" text-anchor="middle">The written product is AB; the first action is B.</text></svg><figcaption>Compatibility checks the intermediate coordinate space. Reversing the action order changes the product to BA, which may have another shape or be undefined.</figcaption></figure>

Consider a counterclockwise quarter-turn R = @M{0,−1;1,0} and S = @M{1,1;0,1}. Applying S and then R gives RS. Applying R and then S gives SR. On e<sub>2</sub>, RS produces (−1,1)<sup>T</sup>, while SR produces (−1,0)<sup>T</sup>. Both actions are valid; their outcomes differ. The laboratory later lets you inspect this continuously.

### 5.2 Associativity proved entrywise

Let A, B, C have shapes m-by-n, n-by-p, and p-by-q. Both parenthesizations have shape m-by-q. For arbitrary valid i and j:

<div class="formula-block">((AB)C)<sub>ij</sub> = ∑<sub>r=1</sub><sup>p</sup> ∑<sub>k=1</sub><sup>n</sup> a<sub>ik</sub>b<sub>kr</sub>c<sub>rj</sub>.</div>

Expanding A(BC) gives exactly the same scalar terms, with the finite summations performed in the other order. Finite sums can be reordered, and scalar multiplication is associative, so the two entries agree. Therefore (AB)C = A(BC).

Associativity changes grouping while keeping factor order. It permits ABC without ambiguity. It does not permit ACB or BAC. In exact arithmetic the parenthesizations agree, but floating-point rounding can make their computed entries differ slightly, and their operation counts can differ greatly. These are separate issues addressed in Section 10.

### 5.3 Distributivity and scalar compatibility

If B and C have the same shape compatible with A, expand the entry of A(B+C):

<div class="formula-block">(A(B+C))<sub>ij</sub> = ∑<sub>k=1</sub><sup>n</sup> a<sub>ik</sub>(b<sub>kj</sub>+c<sub>kj</sub>) = (AB)<sub>ij</sub>+(AC)<sub>ij</sub>.</div>

This proves left distributivity. Right distributivity is proved by expanding (A+B)C. A scalar can be factored from either factor, so α(AB) = (αA)B = A(αB). A scalar commutes with every scalar entry; a matrix does not generally commute with another matrix.

### 5.4 Noncommutativity and zero divisors

For square matrices let N = @M{0,1;0,0} and D = @M{1,0;0,0}. Then DN = N but ND = 0. This shows AB and BA can differ even when they have exactly the same shape. It also shows that a product can vanish with neither factor zero.

Even more strikingly, N² = 0 although N is nonzero. The first application maps (x,y)<sup>T</sup> to (y,0)<sup>T</sup>; the second kills that result. A map can destroy all information after two applications without being the zero map on the first application.

The correct interpretation of AB = 0 is that **every column of B is sent to zero by A**. It need not mean that A is zero or that B is zero. This interpretation is stronger than memorizing a single counterexample and connects naturally to the nullspace chapter.

### 5.5 Cancellation has a direction and a hypothesis

From AB = AC, one gets A(B−C) = 0. To infer B = C, it is enough that A have a left inverse L satisfying LA = I. Multiplying on the left gives B = C. A nonzero A is not enough. Similarly, BA = CA permits right cancellation if A has a right inverse R with AR = I.

For a square invertible A both directions are allowed. The side matters: to solve AX = B use X = A<sup>−1</sup>B; to solve XA = B use X = BA<sup>−1</sup>. Writing “divide by A” hides the order and should be avoided.

If AXB = C with square invertible A and B, the correct solution is A<sup>−1</sup>CB<sup>−1</sup>. Multiply in the positions that bring inverse pairs together. Never move an inverse across a factor merely to obtain a familiar-looking expression.

## 6. Transpose, adjoint, symmetry, and Gram matrices

### 6.1 Ordinary transpose and its product rule

For an m-by-n matrix A, the transpose A<sup>T</sup> is n-by-m and has entry a<sub>ji</sub>. Its rows are A's columns. Transposing twice returns A. Addition and real scaling commute with transposition because they operate entrywise.

The product rule reverses factor order:

<div class="formula-block">(AB)<sup>T</sup> = B<sup>T</sup>A<sup>T</sup>.</div>

To prove it, the (i,j) entry of the left side is (AB)<sub>ji</sub>, equal to the sum of a<sub>jk</sub>b<sub>ki</sub>. The right side has the sum of b<sub>ki</sub>a<sub>jk</sub>. Corresponding scalar terms agree. The shapes also agree: if A is m-by-n and B n-by-p, both transposed products are p-by-m. The same reasoning gives (ABC)<sup>T</sup> = C<sup>T</sup>B<sup>T</sup>A<sup>T</sup>.

This reversal reflects composition order. It is not optional even when all factors are square. A transposed product with the original order is generally wrong.

### 6.2 Complex conjugate transpose

For complex matrices define A<sup>*</sup> by transposing and conjugating every entry. Conjugation changes the sign of the imaginary part. The adjoint satisfies the same reversed product law, but scalar multiplication is conjugated:

<div class="formula-block">(AB)<sup>*</sup> = B<sup>*</sup>A<sup>*</sup>, &nbsp; (αA)<sup>*</sup> = <span class="overline">α</span>A<sup>*</sup>.</div>

For complex column vectors, x<sup>*</sup>y is the inner product used here, conjugate-linear in the first argument and linear in the second. Ordinary x<sup>T</sup>y may be complex or even zero for a nonzero x when y = x. For x = (1,i)<sup>T</sup>, x<sup>T</sup>x = 0 while x<sup>*</sup>x = 2. A norm calculation must therefore use the adjoint.

### 6.3 Symmetric and skew-symmetric parts

A real square matrix is symmetric when A<sup>T</sup> = A and skew-symmetric when A<sup>T</sup> = −A. Skew-symmetry forces each diagonal entry to be zero, because a<sub>ii</sub> = −a<sub>ii</sub> over the real numbers. The zero matrix belongs to both classes.

Every real square matrix has a unique decomposition:

<div class="formula-block">A = H+K, &nbsp; H = @F{A+A<sup>T</sup>;2}, &nbsp; K = @F{A−A<sup>T</sup>;2}, &nbsp; H<sup>T</sup> = H, &nbsp; K<sup>T</sup> = −K.</div>

Transposing the two definitions verifies their structural properties; adding them gives A. For uniqueness, if A = H′+K′ too, then H−H′ = −(K−K′) is both symmetric and skew-symmetric, and hence equals zero. Symmetric and skew-symmetric parts cannot compensate ambiguously.

For a real skew-symmetric K and a real vector x, the scalar x<sup>T</sup>Kx equals its own transpose, which equals x<sup>T</sup>K<sup>T</sup>x = −x<sup>T</sup>Kx. Thus it is zero. Consequently a real quadratic expression x<sup>T</sup>Ax depends only on the symmetric part of A. For complex matrices the corresponding decomposition uses the adjoint: Hermitian means H<sup>*</sup> = H, and skew-Hermitian means K<sup>*</sup> = −K. A skew-Hermitian quadratic value is purely imaginary and need not be zero.

Products of symmetric matrices need not be symmetric. For symmetric A and B, the product AB is symmetric exactly when AB = BA, since (AB)<sup>T</sup> = BA. Addition preserves symmetry; multiplication requires a commutation condition.

### 6.4 Gram matrices and what they measure

For a real m-by-n matrix A, its column Gram matrix is G = A<sup>T</sup>A, of shape n-by-n. Its entry g<sub>ij</sub> is the dot product of columns i and j. It is symmetric, and:

<div class="formula-block">x<sup>T</sup>Gx = (Ax)<sup>T</sup>(Ax) = ‖Ax‖² ≥ 0.</div>

This property is called positive semidefiniteness. It concerns every quadratic value, not the signs of individual entries. Off-diagonal Gram entries can be negative because columns may point in opposite directions. Equality holds exactly when Ax = 0. Strict positivity for every nonzero x holds exactly when no nonzero input is sent to zero; later rank theory characterizes this condition.

The row Gram matrix AA<sup>T</sup> has shape m-by-m and contains dot products of rows. Both constructions are valid, but they answer different questions and may have different sizes. For complex A, replace the transpose by the adjoint: A<sup>*</sup>A is Hermitian and x<sup>*</sup>A<sup>*</sup>Ax = ‖Ax‖².

### 6.5 Orthogonal matrices and rectangular isometries

A real square matrix Q is orthogonal when Q<sup>T</sup>Q = I. Its columns are an orthonormal family because the product's entries are their dot products. For any vectors x and y, (Qx)<sup>T</sup>(Qy) = x<sup>T</sup>y, so it preserves inner products, lengths, and angles.

The columns are linearly independent: Qx = 0 implies x<sup>T</sup>Q<sup>T</sup>Qx = ‖x‖² = 0, hence x = 0. To see directly why n independent vectors in ℝ<sup>n</sup> form a basis, start with its n standard coordinate vectors as a spanning list. Insert the independent columns one at a time. Express the next column using the current list, which consists of previously inserted columns and unreplaced coordinate vectors. At least one unreplaced coordinate vector must have a nonzero coefficient; otherwise the next column would be a combination of the earlier columns, contradicting independence. Solve that relation for one such coordinate vector and replace it by the new column. The list still spans, retains n vectors, and contains one more column. After n replacements all columns form a spanning list. This exchange argument supplies the needed finite-dimensional fact without assuming that an independent family automatically spans in arbitrary dimensions. Consequently Q is onto. For any y = Qx, QQ<sup>T</sup>y = QQ<sup>T</sup>Qx = Qx = y. Therefore QQ<sup>T</sup> = I and Q<sup>−1</sup> = Q<sup>T</sup>.

A rectangular m-by-n matrix with Q<sup>T</sup>Q = I<sub>n</sub> also preserves input lengths. It is an isometric embedding. When m > n, QQ<sup>T</sup> is not I<sub>m</sub>; it is the identity on the column span and zero on its orthogonal complement. The distinction between an embedding and a square orthogonal matrix is a frequent examination trap. For complex square matrices the analogous condition is unitary: Q<sup>*</sup>Q = I.

## 7. Inverses, triangular structure, and matrix powers

### 7.1 Definition and uniqueness

A square matrix A is invertible if a matrix B satisfies AB = BA = I. The matrix B is its inverse. If B and C both satisfy this definition, then B = B(AC) = (BA)C = C. Thus the inverse is unique.

An inverse undoes a transformation. If Ax = y, multiplying on the left gives x = A<sup>−1</sup>y. A singular matrix cannot have an inverse: if it sends a nonzero z to zero, an inverse would imply z = A<sup>−1</sup>Az = 0, a contradiction. General methods for deciding invertibility are deferred to Gaussian elimination and rank chapters.

For square matrices over ℝ or ℂ, one inverse equation already implies the other. Suppose BA = I. Then Ax = 0 implies <span class="math-inline">x = BAx = 0</span>, so A's n columns are independent and form a basis. Every y can be written Ax. Therefore <span class="math-inline">ABy = ABAx = Ax = y</span>, proving AB = I. This uses finite-dimensional basis theory. It does not apply to rectangular matrices or arbitrary infinite-dimensional operators.

### 7.2 Product, scalar, and transpose inverse rules

If A and B are square invertible matrices of the same size, the candidate B<sup>−1</sup>A<sup>−1</sup> satisfies both inverse equations:

<div class="formula-block">(AB)(B<sup>−1</sup>A<sup>−1</sup>) = I, &nbsp; (B<sup>−1</sup>A<sup>−1</sup>)(AB) = I.</div>

Associativity groups the adjacent inverse pairs. Uniqueness then gives (AB)<sup>−1</sup> = B<sup>−1</sup>A<sup>−1</sup>. Undo the last action first, which reverses the written product order. Also (A<sup>T</sup>)<sup>−1</sup> = (A<sup>−1</sup>)<sup>T</sup> by transposing both inverse equations. The adjoint satisfies the analogous rule.

For a nonzero scalar α, (αA)<sup>−1</sup> = α<sup>−1</sup>A<sup>−1</sup>. Neither inverse distribution over addition nor a scalar-like fraction rule is available: (A+B)<sup>−1</sup> usually differs from A<sup>−1</sup>+B<sup>−1</sup>, and A+B might be singular even when both summands are invertible.

### 7.3 The two-by-two inverse derived by verification

For A = @M{a,b;c,d}, form C = @M{d,−b;−c,a}. Direct multiplication on either side gives AC = CA = (ad−bc)I. If the denominator is nonzero:

<div class="formula-block">A<sup>−1</sup> = @F{1;ad−bc} @M{d,−b;−c,a}.</div>

If ad−bc = 0 and (a,b) is nonzero, the nonzero vector (b,−a)<sup>T</sup> is sent to zero: its first output is ab−ba, its second cb−da. If (a,b) is zero but (c,d) is not, use (d,−c)<sup>T</sup>; if every entry is zero, any nonzero vector works. In every case the matrix is singular. Thus the denominator condition is necessary as well as sufficient, without assuming a general determinant theorem.

The denominator becomes the two-by-two determinant in a later chapter. Here the formula is justified directly by multiplication. In numerical computation, a denominator close to zero can magnify small data errors; a nonzero exact denominator does not alone promise numerical stability.

### 7.4 Diagonal and triangular matrices

A diagonal matrix D = diag(d<sub>1</sub>,…,d<sub>n</sub>) has zero off-diagonal entries. Left multiplication DA scales row i by d<sub>i</sub>; right multiplication AD scales column j by d<sub>j</sub>. These actions differ unless the relevant scaling factors agree. If every d<sub>i</sub> is nonzero, the inverse diagonal entries are their reciprocals.

An upper-triangular matrix has zeros below the diagonal. A **strictly** upper-triangular matrix also has zeros on the diagonal. Products of upper-triangular matrices remain upper triangular: when i > j, a potentially nonzero term a<sub>ik</sub>b<sub>kj</sub> would need i ≤ k ≤ j, which is impossible. On the diagonal, only k = i contributes, so (AB)<sub>ii</sub> = a<sub>ii</sub>b<sub>ii</sub>. The lower-triangular version follows by transposition.

For an n-by-n strictly upper-triangular N, a nonzero term of N<sup>r</sup> needs an increasing index chain of r steps. No such chain has n steps among n indices, so N<sup>n</sup> = 0. This proof explains nilpotence instead of treating it as a memorized pattern.

### 7.5 Powers, polynomials, and finite inverse series

For a square A, define A⁰ = I and A<sup>k</sup> as k repeated copies for positive integer k. Associativity gives A<sup>r</sup>A<sup>s</sup> = A<sup>r+s</sup> and (A<sup>r</sup>)<sup>s</sup> = A<sup>rs</sup> for nonnegative integers. If A is invertible, negative integer powers are defined using its inverse. Noninteger powers need additional theory and are not determined by these rules.

A matrix polynomial p(A) replaces a constant term by a multiple of I. Any two polynomials in the same A commute, because their expanded terms are powers of the same matrix. Arbitrary matrices do not inherit that property.

If N<sup>r</sup> = 0, then:

<div class="formula-block">(I−N)<sup>−1</sup> = I+N+⋯+N<sup>r−1</sup>.</div>

Multiplying by I−N on either side cancels all interior terms and leaves I−N<sup>r</sup> = I. This finite algebraic identity needs no convergence assumption. For I+N, alternating signs give I−N+N²−⋯ up to the last nonzero power.

The square expansion is (A+B)² = A²+AB+BA+B². It reduces to A²+2AB+B² exactly when AB = BA. The ordinary binomial theorem holds for commuting square matrices, because words with the same counts can then be reordered. Without commutation, preserve each word's order.

## 8. Blocks, permutations, and elementary operations

### 8.1 Partitioned multiplication

A block matrix groups contiguous entries into rectangular submatrices. The block entries may themselves be nonsquare. Treating them like scalars is safe only when every product and sum has compatible shape and factor order is preserved.

<div class="formula-block">@M{A_11,A_12;A_21,A_22} @M{B_11,B_12;B_21,B_22} = @M{A_11B_11+A_12B_21,A_11B_12+A_12B_22;A_21B_11+A_22B_21,A_21B_12+A_22B_22}.</div>

Suppose the A row partition has sizes r and s, and its column partition sizes u and v. The B row partition must have those same sizes u and v. If B's column partition has sizes t and w, then A<sub>12</sub> is r-by-v, B<sub>21</sub> is v-by-t, and both terms in the top-left sum are r-by-t. Matching only the number of blocks is insufficient; the intermediate block widths and heights must match too.

The block rule follows by splitting the shared-index sum into ranges. There is no new multiplication operation. It is the usual operation reorganized around structural groups. A block diagonal product multiplies corresponding diagonal blocks, while zero off-diagonal blocks remove other terms.

For compatible blocks a useful inverse identity is:

<div class="formula-block">@M{I,X;0,I}<sup>−1</sup> = @M{I,−X;0,I}.</div>

The identities can have different sizes and X can be rectangular. Both products give the appropriate block identity. More general block inverse formulas require additional invertibility assumptions and will be studied with elimination; inverses of individual blocks cannot simply be taken entrywise.

### 8.2 Permutations act on a particular side

A permutation matrix has exactly one one in each row and column and zeros elsewhere. Its columns are permuted standard basis vectors, so they are orthonormal and P<sup>−1</sup> = P<sup>T</sup>. Left multiplication PA reorders rows. Right multiplication AP reorders columns according to P's columns. The two reorderings need not have the same index convention.

For a simple swap of two coordinates the same matrix performs its own inverse, but a three-cycle does not. If P maps e<sub>1</sub> to e<sub>2</sub>, e<sub>2</sub> to e<sub>3</sub>, and e<sub>3</sub> to e<sub>1</sub>, then AP has columns a<sub>2</sub>, a<sub>3</sub>, a<sub>1</sub>, whereas PA has rows row 3, row 1, row 2. Derive the side-specific effect instead of transferring a verbal permutation blindly.

### 8.3 Row additions as matrix multiplication

For i ≠ j, E = I+αe<sub>i</sub>e<sub>j</sub><sup>T</sup> adds α times row j to row i when it multiplies on the left. The outer product selects row j and places it into row i. Because (e<sub>i</sub>e<sub>j</sub><sup>T</sup>)² = 0, the inverse is I−αe<sub>i</sub>e<sub>j</sub><sup>T</sup>. On the right, the same matrix adds α times column i to column j. The input and output roles reverse across the side.

This is the algebraic basis of elementary row operations. The next chapter organizes these operations into Gaussian elimination; here the emphasis is knowing exactly which coordinates a multiplication changes and how the operation is undone.

## 9. Trace, Frobenius geometry, and useful extensions

### 9.1 Trace and cyclic order

The trace of a square matrix is the sum of its diagonal entries. It is linear and unchanged by transposition. If A is m-by-n and B is n-by-m, both AB and BA are square, possibly of different sizes, and:

<div class="formula-block">tr(AB) = ∑<sub>i=1</sub><sup>m</sup> ∑<sub>k=1</sub><sup>n</sup> a<sub>ik</sub>b<sub>ki</sub> = tr(BA).</div>

Interchange the two finite sums to prove the last equality. This does **not** say AB = BA. It says one scalar statistic agrees. For a compatible cyclic product, trace is unchanged by rotating the entire factor sequence, for example tr(ABC) = tr(BCA) = tr(CAB). Arbitrarily swapping two adjacent factors is not a cyclic rotation and can change the trace.

If S is invertible, tr(S<sup>−1</sup>AS) = tr(A), by one cyclic rotation and cancellation. This is a useful bridge to later similarity theory, but no eigenvalue claim is needed to prove it.

### 9.2 Frobenius norm and orthogonal invariance

The Frobenius norm treats the matrix entries as a vector:

<div class="formula-block">‖A‖<sub>F</sub>² = ∑<sub>i=1</sub><sup>m</sup> ∑<sub>j=1</sub><sup>n</sup> a<sub>ij</sub>² = tr(A<sup>T</sup>A).</div>

It also equals the sum of squared column lengths and the sum of squared row lengths. For complex matrices replace squared entries by squared moduli and use tr(A<sup>*</sup>A). The Frobenius inner product is tr(A<sup>T</sup>B) over the real field; expanding the trace gives the sum of a<sub>ij</sub>b<sub>ij</sub>.

Left multiplication by an orthogonal Q preserves each column length, so ‖QA‖<sub>F</sub> = ‖A‖<sub>F</sub>. Right multiplication by an orthogonal R preserves each row length, yielding ‖AR‖<sub>F</sub> = ‖A‖<sub>F</sub>. Alternatively substitute into the trace formula and use the cyclic law. Symmetric and skew-symmetric parts are orthogonal under this matrix inner product: paired off-diagonal terms cancel, and the skew part's diagonal is zero. Hence ‖A‖<sub>F</sub>² = ‖H‖<sub>F</sub>²+‖K‖<sub>F</sub>².

For compatible A and B, scalar Cauchy–Schwarz on each output entry gives |(AB)<sub>ij</sub>|² ≤ (sum of squares in row i of A)(sum of squares in column j of B). Summing over i and j separates the factors and proves ‖AB‖<sub>F</sub> ≤ ‖A‖<sub>F</sub>‖B‖<sub>F</sub>. This bound is valid but can be loose; it is not a claim that every factor changes all lengths by its Frobenius norm.

### 9.3 Hadamard and Kronecker products

The Hadamard product A ⊙ B multiplies corresponding entries and requires identical shapes. It is commutative over ℝ or ℂ, unlike ordinary multiplication. For a fixed same-shape pair, the Hadamard product and AB can both exist yet be different. An examination problem must identify which product it means.

The Kronecker product A ⊗ B replaces entry a<sub>ij</sub> by the block a<sub>ij</sub>B. If A is m-by-n and B p-by-q, its shape is mp-by-nq. For compatible pairs A,C and B,D:

<div class="formula-block">(A⊗B)(C⊗D) = (AC)⊗(BD).</div>

To verify it, label a row by (i,r) and a column by (j,s). The product entry sums a<sub>ik</sub>b<sub>rt</sub>c<sub>kj</sub>d<sub>ts</sub> over k and t. Scalar commutation separates this into (sum over k of a<sub>ik</sub>c<sub>kj</sub>)(sum over t of b<sub>rt</sub>d<sub>ts</sub>), giving the stated block entry. The rule preserves the order within AC and within BD.

These products are included to remove notation ambiguity, not to assume advanced tensor theory. Ordinary multiplication remains the default everywhere else in the chapter.

## 10. Computation, operation counts, and perturbations

### 10.1 An exact reference algorithm

The following pseudocode uses zero-based array positions but computes the same mathematical product. Explicitly initializing the accumulator prevents old values from contaminating entries.

```text
multiply(A, B):
    m, n = shape(A)
    r, p = shape(B)
    require n == r
    C = zero_matrix(m, p)
    for i in 0 .. m-1:
        for j in 0 .. p-1:
            total = 0
            for k in 0 .. n-1:
                total = total + A[i,k] * B[k,j]
            C[i,j] = total
    return C
```

For each output entry the algorithm multiplies n pairs and performs n additions if adding the first product to an initial zero is counted. A minimal scalar arithmetic count uses n−1 additions by assigning the first product to the accumulator. Therefore dense multiplication costs mnp multiplications and mp(n−1) minimal additions. When counting multiply-and-add pairs or machine instructions, state the convention separately. Dense square multiplication by this algorithm has cubic time and quadratic output storage; the full storage also includes the inputs.

This count applies to the classical algorithm. It is not a lower bound for all matrix multiplication algorithms. Sparsity, special structure, and faster general algorithms change the cost. Exact rational arithmetic also has bit costs that this scalar-operation count does not capture.

### 10.2 Parenthesization changes cost, not factor order

Let A be 10-by-100, B 100-by-5, and C 5-by-50. Computing (AB)C costs 5,000+2,500 = 7,500 scalar multiplications. Computing A(BC) costs 25,000+50,000 = 75,000. Both results are 10-by-50 and equal in exact arithmetic. The first route makes a small intermediate matrix; the second a large one. Associativity allows the cheaper route but does not allow reordering A, B, C.

For a longer chain with dimensions d<sub>0</sub>,…,d<sub>r</sub>, the matrix-chain dynamic-programming recurrence is:

<div class="formula-block">M(i,j) = min<sub>i≤k&lt;j</sub> {M(i,k)+M(k+1,j)+d<sub>i−1</sub>d<sub>k</sub>d<sub>j</sub>}, &nbsp; M(i,i) = 0.</div>

Every final split divides the chain into a left and right subchain; after their products are computed, the final multiplication has the displayed dimension cost. Enumerating all splits and solving shorter chains first proves the recurrence finds the smallest classical multiplication count. This is an algebra–algorithms connection; it does not require implementing the optimizer during this study session.

### 10.3 Exact identities and floating-point behavior

Mathematical associativity does not guarantee bit-identical floating-point results. Scalar additions are rounded, and regrouping changes which intermediate numbers are rounded. For example, with finite precision, adding a tiny value to a huge one can discard the tiny value, while subtracting the huge values first can preserve it. Avoid interpreting a small computed discrepancy as a failure of the algebraic theorem.

For perturbed inputs A+E and B+F, exact distributivity gives:

<div class="formula-block">(A+E)(B+F)−AB = AF+EB+EF.</div>

The Frobenius product bound and triangle inequality imply a quantitative error bound:

<div class="formula-block">‖(A+E)(B+F)−AB‖<sub>F</sub> ≤ ‖A‖<sub>F</sub>‖F‖<sub>F</sub> + ‖E‖<sub>F</sub>‖B‖<sub>F</sub> + ‖E‖<sub>F</sub>‖F‖<sub>F</sub>.</div>

For small perturbations the first two terms dominate, but the quadratic term is present in the exact identity. Dropping it requires declaring an approximation. This is a useful habit for every later numerical method: distinguish a mathematical identity, a computational approximation, and an empirical observation.

## 11. Interactive laboratory: order of transformations

Choose a shear and a rotation, then compare their two composition orders on the same input vector. The blue result applies the shear first and the rotation second. The amber result applies the rotation first and the shear second. The dashed outline is the original unit square; the colored outlines are its images. The grid uses the same scale on both axes.

<div class="matrix-lab">
<div class="matrix-controls"><label for="matrix-angle">Counterclockwise rotation angle <output id="matrix-angle-value" class="lab-math"></output><input id="matrix-angle" type="range" min="−180" max="180" value="90"></label><label for="matrix-shear">Horizontal shear parameter <output id="matrix-shear-value" class="lab-math"></output><input id="matrix-shear" type="range" min="−200" max="200" value="100"></label><label for="matrix-x">Input horizontal coordinate <output id="matrix-x-value" class="lab-math"></output><input id="matrix-x" type="range" min="−150" max="150" value="100"></label><label for="matrix-y">Input vertical coordinate <output id="matrix-y-value" class="lab-math"></output><input id="matrix-y" type="range" min="−150" max="150" value="100"></label></div>
<svg id="matrix-canvas" viewBox="0 0 640 640" role="img" aria-label="Equal-scale plot comparing rotation after shear with shear after rotation"></svg>
<div id="matrix-result" aria-live="polite"></div>
<noscript>The laboratory needs JavaScript. At a quarter-turn with shear parameter one and input (1,1), rotation after shear gives (−1,2), while shear after rotation gives (0,1). All theoretical explanations and worked solutions remain readable without JavaScript.</noscript>
</div>

### 11.1 What to inspect

First set the shear to zero: both orders reduce to the same rotation. Next set the rotation to zero: both reduce to the same shear. With a half-turn, the rotation is −I, which commutes with every matrix, so the orders agree again. With a quarter-turn and nonzero shear they differ. Changing the input can reveal whether two different matrices happen to agree on that particular vector.

The displayed matrix difference is the commutator RS−SR. For s ≠ 0 and sin(θ) ≠ 0 it has nonzero diagonal entries of opposite sign, so these two particular maps disagree on every nonzero input. For other matrix pairs a nonzero commutator can still annihilate some nonzero vectors; the laboratory's conclusion should not be generalized without a proof. The squared difference of output coordinates is computed directly, not inferred from picture overlap.

The shapes of transformed squares reveal why a shear is not generally length-preserving. A pure rotation preserves side lengths and angles; a shear changes the square into a parallelogram. Both preserve the origin and linear combinations. A picture illustrates these facts; the formulas establish them.
