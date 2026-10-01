## 12. Fully worked problems: calculation, proof, and diagnosis

**Reading instruction.** These are teaching examples with complete solutions, not a test of material you have not yet studied. Read the reasoning and the final lesson together. The progression moves from shape checks to structural proofs and advanced connections. Problems marked course-derived adapt a mathematical problem type with newly written explanations; they do not reproduce an entire source exercise collection. All remaining questions are original.

### Problem 1 — Diagnose dimensions before calculating

Let A be 2-by-3, B 3-by-4, C 4-by-2, and D 2-by-2. Determine the shapes of AB, BA, ABC, CAB, A+B, DA, and AD. Explain every undefined expression.

**Solution.** AB contracts the matching inner dimension three and leaves shape 2-by-4. BA would need four, the number of columns of B, to equal two, the number of rows of A; it is undefined. ABC is defined in either grouping: AB is 2-by-4 and can multiply C, giving 2-by-2; BC is 3-by-2 and can be premultiplied by A, with the same output shape. CAB is 4-by-4, because CA is 4-by-3 and then multiplies B. Addition A+B is undefined because both dimensions must match. DA is 2-by-3, while AD is undefined because three does not match two.

The cyclic order changed the final shape from 2-by-2 for ABC to 4-by-4 for CAB. That does not contradict trace cyclicity: their traces can agree even though their sizes differ. **Lesson:** compatible multiplication contracts an intermediate dimension; addition never contracts dimensions.

### Problem 2 — Recover a matrix from linear combinations

Suppose X+2Y = @M{5,0;1,4} and 3X−Y = @M{1,7;10,−2}. Find X and Y without solving four separate systems.

**Solution.** Call the right sides M and N. Multiplying the first equation by three and subtracting the second gives 7Y = 3M−N. Therefore Y = (3M−N)/7 = @F{1;7}@M{14,−7;−7,14} = @M{2,−1;−1,2}. Substitute into the first equation: X = M−2Y = @M{1,2;3,0}. Verification in the second equation gives 3X−Y = @M{1,7;10,−2}, as required.

This manipulation is valid because matrix addition and scalar multiplication obey vector-space laws. It does not divide by a matrix or commute any matrix factors. **Lesson:** scalar linear systems can be solved with matrix-valued unknowns when all unknowns have the same fixed shape.

### Problem 3 — Construct a transformation from basis images

A linear map T sends (1,0)<sup>T</sup> to (2,−1,0)<sup>T</sup> and (0,1)<sup>T</sup> to (1,3,4)<sup>T</sup>. Find its standard matrix and T(3,−2).

**Solution.** Place the two output vectors in columns, not rows. The matrix is A = @M{2,1;−1,3;0,4}, of shape 3-by-2. The input equals 3e<sub>1</sub>−2e<sub>2</sub>, so linearity yields three times the first column minus twice the second. This is (4,−9,−8)<sup>T</sup>. Row-column evaluation confirms the entries: 6−2, −3−6, and 0−8.

A two-by-three arrangement of the given images would act on three-dimensional inputs and could not represent this map. **Lesson:** the number of columns is the input dimension; the number of rows is the output dimension. Basis images completely determine a linear map once the input basis is fixed.

### Problem 4 — One product, four calculations

For A = @M{1,−1,2;0,3,1} and B = @M{2,0;1,4;−1,2}, compute AB and verify the second row and first column through the row and column views.

**Solution.** The output is 2-by-2. Its four row-column sums are 2−1−2 = −1, 0−4+4 = 0, 0+3−1 = 2, and 0+12+2 = 14. Thus AB = @M{−1,0;2,14}. The second row of A is (0,3,1), so the second output row is zero times row 1 of B, plus three times row 2, plus row 3: (3,12)+(−1,2) = (2,14). The first column of B supplies coefficients (2,1,−1); combining A's columns gives (2,0)+(−1,3)+(−2,−1) = (−1,2).

The outer-product terms are @M{2,0;0,0}, @M{−1,−4;3,12}, and @M{−2,4;−1,2}. Their sum confirms every output entry. **Lesson:** select the view that exposes sparsity or structure; all four views compute the same product.

### Problem 5 — Distributivity with a complete verification

**Course-derived type:** MIT 18.06SC multiplication recitation, Problem 3.1. The numerical data and explanation here are new. Let A = @M{2,−1;1,3}, B = @M{1,0;0,0}, and C = @M{0,0;4,−2}. Verify A(B+C) = AB+AC and explain why this example alone is not a universal proof.

**Solution.** B+C = @M{1,0;4,−2}. Multiplying gives A(B+C) = @M{−2,2;13,−6}. Separately, AB = @M{2,0;1,0} and AC = @M{−4,2;12,−6}; their sum is the same matrix. Each output entry has split the two contributions into separate sums.

The calculation establishes the identity for these particular matrices. The general identity requires the arbitrary-entry argument from Section 5, where distributivity of scalar multiplication is applied inside the shared-index sum. **Lesson:** an example illustrates a theorem; arbitrary-entry reasoning proves its universal scope.

### Problem 6 — Quantities, prices, and physical units

**Course-derived type:** CMU 21-241 Day 7 quantities-times-prices application. A laboratory buys three consumable types. Two teams request Q = @M{3,2,5;1,4,2} units, with teams as rows and consumables as columns. Two suppliers charge P = @M{2,3;5,4;1,2} dollars per unit, with consumables as rows and suppliers as columns. Compute the total costs and select the cheaper supplier for each team.

**Solution.** QP is 2-by-2: team-by-supplier. The first team's costs are 3·2+2·5+5·1 = 21 and 3·3+2·4+5·2 = 27. The second team's costs are 1·2+4·5+2·1 = 24 and 1·3+4·4+2·2 = 23. Thus QP = @M{21,27;24,23}. Team one chooses supplier one; team two chooses supplier two.

Every term has units of units purchased times dollars per unit, so the result is dollars. Multiplying corresponding entries would be undefined as a same-shape operation and would not sum over consumables. **Lesson:** semantic row and column labels can be as useful as numerical dimensions when modeling a problem.

### Problem 7 — Select rows, columns, and one entry

Let A = @M{7,−2,5;1,4,0}. Compute Ae<sub>2</sub>, e<sub>2</sub><sup>T</sup>A, and e<sub>1</sub><sup>T</sup>Ae<sub>3</sub>. Specify every selector's dimension.

**Solution.** On the right, e<sub>2</sub> is the three-coordinate vector (0,1,0)<sup>T</sup>, so Ae<sub>2</sub> = (−2,4)<sup>T</sup>, the second column. On the left, e<sub>2</sub> is the two-coordinate vector (0,1)<sup>T</sup>, so e<sub>2</sub><sup>T</sup>A = (1,4,0), the second row. The final left selector has two coordinates, the right selector three; their product extracts entry (1,3), equal to five.

The same notation e<sub>2</sub> has different ambient dimensions in different positions. That is legitimate when the context fixes the dimensions, but omitting this distinction in a proof can make an expression invalid. **Lesson:** coordinate selectors are shape-dependent objects.

### Problem 8 — Compose two outer-product maps

Let u,w be real m-coordinate columns and v,z real m-coordinate columns. Find (uv<sup>T</sup>)(wz<sup>T</sup>) and characterize when it vanishes if u and z are nonzero.

**Solution.** Associate the middle factors: the product equals u(v<sup>T</sup>w)z<sup>T</sup>. Since v<sup>T</sup>w is a scalar, this equals (v<sup>T</sup>w)uz<sup>T</sup>. When u and z are nonzero, their outer product is nonzero: choose nonzero coordinates u<sub>i</sub> and z<sub>j</sub>, and their product is a nonzero entry. Thus the matrix product vanishes exactly when v<sup>T</sup>w = 0.

Take u = z = (1,0)<sup>T</sup>, v = (0,1)<sup>T</sup>, and w = (1,0)<sup>T</sup>. Both outer-product matrices are nonzero, but their product is zero because the first map reads a coordinate that the second map's output does not contain. **Lesson:** zero products can reflect orthogonality of an internal scalar pairing, not zero factors.

### Problem 9 — Reverse a shear and a rotation

Use S = @M{1,1;0,1} and R = @M{0,−1;1,0}. Compute RS, SR, and both products on x = (1,1)<sup>T</sup>.

**Solution.** RS = @M{0,−1;1,1} while SR = @M{1,−1;1,0}. Applying RS to x gives (−1,2)<sup>T</sup>. Applying SR gives (0,1)<sup>T</sup>. To understand the first answer, shear x to (2,1), then rotate it to (−1,2). For the second, rotate x to (−1,1), then shear it to (0,1).

The commutator RS−SR = @M{−1,0;0,1} is nonzero and sends x to (−1,1), exactly the difference of the two outputs. **Lesson:** follow the action sequence on a vector before choosing the written matrix order; the rightmost factor acts first.

### Problem 10 — Nonzero factors, zero product, and failed cancellation

Let D = @M{1,0;0,0}, B = @M{0,0;1,0}, and C = 0. Show that DB = DC although B ≠ C. Explain exactly what information D loses.

**Solution.** Every column of B has zero first coordinate. D keeps a vector's first coordinate and sets its second to zero, so it kills every column of B. Thus DB = 0 = DC. Yet B has a one in its lower-left position and is not C. Premultiplication by D discards the entire second row of any matrix. Equality after applying D therefore cannot recover that discarded row.

No contradiction with cancellation for invertible matrices exists: D has no inverse, since D(0,1)<sup>T</sup> = 0. Merely being nonzero is not a cancellation hypothesis. **Lesson:** translate A(B−C) = 0 into a statement about each difference column before drawing conclusions.

### Problem 11 — Equality on a basis versus one vector

Suppose A and B are m-by-n. Prove that Ae<sub>j</sub> = Be<sub>j</sub> for every standard basis vector implies A = B. Give different two-by-two matrices that agree on (1,0)<sup>T</sup>.

**Solution.** Multiplication by e<sub>j</sub> extracts column j. The hypothesis therefore says every corresponding pair of columns agrees. Entrywise equality follows for every row and column, proving A = B. Choose A = I and B = @M{1,4;0,3}. Their first columns both equal (1,0)<sup>T</sup>, so they agree on the specified vector, but their second columns differ.

More generally, equality on any basis is enough because every input is a linear combination of basis vectors and the maps are linear. Equality on a set that does not span the input space can leave unconstrained directions. **Lesson:** the quantifier “for every input” or “for every basis vector” carries essential information.

### Problem 12 — Rectangular left and right inverses

Let A = @M{1,0;0,1;0,0} and L = @M{1,0,0;0,1,0}. Compute LA and AL. Explain which cancellation direction A permits and why A is not invertible in the square-matrix sense.

**Solution.** LA = I<sub>2</sub>, but AL = diag(1,1,0), not I<sub>3</sub>. The map A embeds a two-coordinate vector into three coordinates by appending zero, and L reads the first two coordinates. Therefore L undoes A on every input. However, applying L to (0,0,1)<sup>T</sup> loses its third coordinate and A cannot restore it.

If AX = AY, premultiply by L to obtain X = Y. A therefore permits left cancellation in this form. It has a left inverse but cannot have a two-sided inverse of the definition in Section 7 because it is rectangular. **Lesson:** one-sided inverse equations must retain the identity dimensions; LA = I does not imply AL = I for rectangular pairs.

### Problem 13 — Solve an equation with factors on both sides

Let A = @M{1,1;0,1}, B = diag(2,3), and C = @M{4,6;2,3}. Solve AXB = C and verify the solution.

**Solution.** Undo A on the left and B on the right. Their inverses are A<sup>−1</sup> = @M{1,−1;0,1} and B<sup>−1</sup> = diag(1/2,1/3). First A<sup>−1</sup>C = @M{2,3;2,3}. Right multiplication by B<sup>−1</sup> scales the first column by one half and the second by one third, so X = @M{1,1;1,1}. Verification gives AX = @M{2,2;1,1}, followed by AXB = @M{4,6;2,3}.

The tempting expression B<sup>−1</sup>CA<sup>−1</sup> uses the wrong sides and generally solves a different problem. **Lesson:** erase factors by multiplying inverses next to the factor being erased, and preserve all other order.

### Problem 14 — Transpose a rectangular product

Let A = @M{1,2,0;−1,3,4} and B = @M{2;1;−1}. Compute (AB)<sup>T</sup> directly and through the product rule.

**Solution.** AB is a two-coordinate column: its entries are 2+2+0 = 4 and −2+3−4 = −3. Thus (AB)<sup>T</sup> is the row (4,−3). The rule gives B<sup>T</sup>A<sup>T</sup>, a one-by-three matrix times a three-by-two matrix. Its first entry is 2·1+1·2+(−1)·0 = 4; its second is 2·(−1)+1·3+(−1)·4 = −3.

The incorrect order A<sup>T</sup>B<sup>T</sup> would be three-by-two times one-by-three and is not even defined. **Lesson:** rectangular examples reveal order errors that square dimensions might conceal.

### Problem 15 — Distinguish transpose from adjoint

Let z = (1,i)<sup>T</sup> and A = @M{1,i;2,1−i}. Find z<sup>T</sup>z, z<sup>*</sup>z, A<sup>T</sup>, and A<sup>*</sup>.

**Solution.** Ordinary transpose gives z<sup>T</sup>z = 1+i² = 0. Conjugate transpose gives z<sup>*</sup>z = 1+(−i)i = 2. The transpose is @M{1,2;i,1−i}. The adjoint is @M{1,2;−i,1+i}. Both swap rows and columns; only the adjoint conjugates entries.

The squared Euclidean length is two, not zero. Ordinary matrix multiplication remains bilinear and does not insert a conjugate, while the complex inner product does. **Lesson:** a nonzero complex vector can have zero bilinear self-product without having zero norm.

### Problem 16 — Symmetric/skew decomposition and its uniqueness

Decompose A = @M{2,5;−1,4} into symmetric H and skew-symmetric K. Evaluate x<sup>T</sup>Ax for x = (1,2)<sup>T</sup> through H and explain why K contributes nothing.

**Solution.** A<sup>T</sup> = @M{2,−1;5,4}. The half-sum gives H = @M{2,2;2,4}; the half-difference gives K = @M{0,3;−3,0}. Their sum is A. Hx = (6,10)<sup>T</sup>, so x<sup>T</sup>Hx = 6+20 = 26. Kx = (6,−3)<sup>T</sup>, and x<sup>T</sup>Kx = 6−6 = 0. Directly Ax = (12,7)<sup>T</sup>, giving 12+14 = 26.

If another decomposition existed, its symmetric difference would equal a skew-symmetric difference. Transposing would show that difference equals its own negative, hence is zero. **Lesson:** the decomposition is unique, and a real quadratic expression sees only its symmetric component.

### Problem 17 — Symmetric factors do not ensure a symmetric product

Let A = diag(1,2) and B = @M{0,1;1,0}. Are A, B, and AB symmetric? Prove the condition for a product of two symmetric matrices to be symmetric.

**Solution.** Both A and B equal their transposes. Their product is @M{0,1;2,0}, which is not symmetric because its off-diagonal entries differ. The reversed product is @M{0,2;1,0}, exactly the transpose of AB.

For any symmetric A and B of the same size, (AB)<sup>T</sup> = B<sup>T</sup>A<sup>T</sup> = BA. Thus AB is symmetric if and only if AB = BA. This establishes both necessity and sufficiency. **Lesson:** closure under addition does not imply closure under multiplication; a structural condition can impose a commutation requirement.

### Problem 18 — Gram matrix, negative entries, and strict positivity

Let A = @M{1,−1;0,2;1,0}. Find A<sup>T</sup>A, verify its quadratic value directly, and decide whether it is positive definite.

**Solution.** The columns are (1,0,1)<sup>T</sup> and (−1,2,0)<sup>T</sup>, with squared lengths two and five and mutual dot product −1. Hence G = @M{2,−1;−1,5}. For x = (u,v)<sup>T</sup>, Ax = (u−v,2v,u)<sup>T</sup>, giving x<sup>T</sup>Gx = (u−v)²+4v²+u² = 2u²−2uv+5v².

This sum of squares vanishes only when u = 0 and v = 0, so the matrix is positive definite. Its negative off-diagonal entries do not conflict with positivity: positivity refers to the quadratic value for every nonzero vector. **Lesson:** prove a Gram claim by expressing the quadratic value as a squared norm.

### Problem 19 — Rectangular orthonormal columns

Let Q = @M{1,0;0,0;0,1}. Compute Q<sup>T</sup>Q and QQ<sup>T</sup>. Does Q preserve lengths? Does it preserve every three-dimensional vector after Q<sup>T</sup> followed by Q?

**Solution.** The two columns are perpendicular unit vectors, so Q<sup>T</sup>Q = I<sub>2</sub>. The reverse product is diag(1,0,1). For input (a,b)<sup>T</sup>, Q outputs (a,0,b)<sup>T</sup>, preserving squared length a²+b². On a three-dimensional vector (r,s,t)<sup>T</sup>, QQ<sup>T</sup> returns (r,0,t)<sup>T</sup> and discards the middle coordinate.

Thus Q is a length-preserving embedding, while QQ<sup>T</sup> is a projection onto its column plane. It is not the three-dimensional identity. **Lesson:** orthonormal columns imply input-length preservation but not a two-sided identity unless the matrix is square.

### Problem 20 — Two-by-two inverse and a singular parameter

For A(t) = @M{1,t;2,3}, find the inverse when it exists. Exhibit a nonzero vector killed by A when it does not exist.

**Solution.** The denominator from direct multiplication is 3−2t. For t ≠ 3/2, the inverse is @F{1;3−2t}@M{3,−t;−2,1}. Multiplying the numerator matrix on either side of A yields (3−2t)I, which verifies the formula.

At t = 3/2 the vector (−3,2)<sup>T</sup> is nonzero and is mapped to (−3+3,−6+6)<sup>T</sup> = 0. An inverse would have to recover this vector from zero, impossible for a linear map. **Lesson:** identify exceptional parameter values before dividing; check both the existence condition and the claimed inverse.

### Problem 21 — Inverse of a product: reverse the order

Let A = @M{1,1;0,1} and B = diag(2,3). Compute (AB)<sup>−1</sup>, and show A<sup>−1</sup>B<sup>−1</sup> is incorrect.

**Solution.** AB = @M{2,3;0,3}. The correct inverse B<sup>−1</sup>A<sup>−1</sup> is @M{1/2,−1/2;0,1/3}. Multiplication by AB gives diagonal entries one and off-diagonal entry 2·(−1/2)+3·(1/3) = 0. The opposite-side check also gives I.

The wrong order yields @M{1/2,−1/3;0,1/3}. Multiplying AB by it gives top-right entry −2/3+1 = 1/3, so the product is not I. **Lesson:** transpose and inverse both reverse product order, for different but compatible algebraic reasons.

### Problem 22 — Diagonal scaling and a permutation cycle

For A = @M{1,2,3;4,5,6;7,8,9}, D = diag(2,−1,3), and P = @M{0,0,1;1,0,0;0,1,0}, describe DA, AD, PA, and AP.

**Solution.** DA scales rows: @M{2,4,6;−4,−5,−6;21,24,27}. AD scales columns: @M{2,−2,9;8,−5,18;14,−8,27}. The columns of P are e<sub>2</sub>, e<sub>3</sub>, e<sub>1</sub>, so AP has A's columns 2,3,1, giving @M{2,3,1;5,6,4;8,9,7}. On the left, P selects A's rows 3,1,2, giving @M{7,8,9;1,2,3;4,5,6}.

The row and column permutation orders differ because they are determined by P's rows and columns, respectively. P<sup>T</sup> is its inverse and P³ = I, but P² is not I. **Lesson:** a permutation matrix need not be a simple self-inverse swap.

### Problem 23 — Square expansion and a false difference of squares

Let A = @M{1,1;0,1} and B = diag(1,2). Compare (A+B)² with A²+2AB+B², and derive the correct expansion of (A−B)(A+B).

**Solution.** AB = @M{1,2;0,2} and BA = @M{1,1;0,2}. Their difference is @M{0,1;0,0}. The correct square expansion is A²+AB+BA+B². Replacing BA with AB changes the answer by AB−BA. Directly A+B = @M{2,1;0,3}, whose square is @M{4,5;0,9}. The false scalar-style formula gives @M{4,6;0,9}.

Distributing the other product gives (A−B)(A+B) = A²+AB−BA−B². It equals A²−B² exactly when AB = BA. **Lesson:** distribute first, preserving order, and only combine cross terms after establishing commutation.

### Problem 24 — A nilpotent three-by-three inverse

**Course-derived type:** MIT 18.06SC recitation Problem 3.2, also identified there as Strang, Section 2.5, Problem 24. Derive the upper-triangular inverse by multiplication rather than Gaussian elimination. Let U = @M{1,a,b;0,1,c;0,0,1}.

**Solution.** Write U = I+N, where N has entries a,b,c above the diagonal and zeros elsewhere. Direct multiplication gives N² = @M{0,0,ac;0,0,0;0,0,0}, while N³ = 0. The alternating finite series therefore gives U<sup>−1</sup> = I−N+N² = @M{1,−a,ac−b;0,1,−c;0,0,1}.

Check the top-right product entry: (ac−b)+a(−c)+b = 0. The adjacent upper entries also cancel, and all diagonal entries equal one. In the reverse product the top-right entry is b−ac+(ac−b) = 0. Both sides give I. **Lesson:** the ac term records a two-step path through the middle coordinate; simply negating all off-diagonal entries misses that interaction.

### Problem 25 — Powers of an idempotent matrix

Let P = @F{1;5}@M{1,2;2,4}. Prove P² = P. For positive integer k, derive (I+P)<sup>k</sup> without diagonalization.

**Solution.** Squaring the numerator matrix gives @M{5,10;10,20}, equal to five times that numerator. Including the factor 1/25 gives P again. Every positive power of P is consequently P. Since I commutes with P, the binomial theorem applies. Its constant term is I, and the coefficient multiplying P is the sum of all nonconstant binomial coefficients, 2<sup>k</sup>−1. Thus (I+P)<sup>k</sup> = I+(2<sup>k</sup>−1)P.

An alternative proof applies induction and uses P² = P at the multiplication step. **Lesson:** a low-degree polynomial relation can determine all higher powers; eigenvalue theory is not always necessary.

### Problem 26 — A nonzero matrix with no square root

**Course-derived type:** Oxford M1, printed p. 13, Example 29. Prove that N = @M{0,1;0,0} has no two-by-two square root over ℝ or ℂ.

**Solution.** Suppose X = @M{a,b;c,d} satisfies X² = N. Entrywise, a²+bc = 0, b(a+d) = 1, c(a+d) = 0, and d²+bc = 0. The second equation forces a+d ≠ 0 and b ≠ 0. The third therefore forces c = 0. The first now yields a² = 0 and hence a = 0; the fourth yields d = 0. But then b(a+d) = 0, contradicting its required value one.

The argument works over the real and complex fields because a scalar with square zero is zero in either field. **Lesson:** existence of matrix powers does not imply existence of matrix roots. Scalar intuitions about square roots cannot be imported automatically.

### Problem 27 — Block dimensions and a triangular block inverse

Let X be 2-by-3. Form M = @M{I_2,X;0,I_3}. State M's size, derive its inverse, and explain why the lower-left zero block is 3-by-2.

**Solution.** The row block sizes are two and three, and the column block sizes are two and three, so M is 5-by-5. The lower-left block must have three rows and two columns. Try N = @M{I_2,−X;0,I_3}. Multiplying compatible blocks gives top-left I<sub>2</sub>, bottom-right I<sub>3</sub>, lower-left zero, and top-right −X+X = 0. The reverse product has the same cancellation. Thus N is M's inverse.

The fact that X is rectangular causes no problem: the off-diagonal products are I<sub>2</sub>X and XI<sub>3</sub>, both 2-by-3. **Lesson:** identities and zeros in a block expression may have different shapes; write them from the row and column partitions.

### Problem 28 — A block commutator

For square X and Y of the same size, let M = @M{I,X;0,I} and N = @M{I,0;Y,I}. Compute MN and NM. When do they commute?

**Solution.** Block multiplication gives MN = @M{I+XY,X;Y,I} and NM = @M{I,X;Y,I+YX}. Their off-diagonal blocks agree. The top-left blocks agree exactly when XY = 0, and the bottom-right blocks agree exactly when YX = 0. Both conditions are necessary and together sufficient.

A claim that they commute whenever XY = YX would be false: taking X = Y = I makes the products unequal. A claim that XY = 0 alone suffices is also false for general matrices because YX may remain nonzero. **Lesson:** compare every block of the entire expression; equality of one internal product is not automatically equality of two larger block matrices.

### Problem 29 — Prove and use triangular closure

Let A = @M{2,1,4;0,3,−2;0,0,5} and B = @M{1,2,0;0,−1,3;0,0,2}. Compute their diagonal product entries without full multiplication and prove the product is upper triangular.

**Solution.** On a diagonal entry (i,i), a nonzero term requires i ≤ k from A and k ≤ i from B, so k = i is the only contributor. The diagonal of AB is therefore (2,−3,10). Below the diagonal, i > j, a nonzero contribution would require i ≤ k ≤ j, which is impossible; every term is zero.

If desired, the full product is @M{2,3,11;0,−3,5;0,0,10}: the top-right is 0+3+8 = 11 and the middle-right 9−4 = 5. **Lesson:** prove zero structure first; it can eliminate most arithmetic and expose impossible proposed answers immediately.

### Problem 30 — Trace of rectangular products

Let A = @M{1,2,0;0,−1,3} and B = @M{2,0;1,4;−2,1}. Compute AB, the diagonal of BA, and both traces. Does trace equality imply product equality?

**Solution.** AB = @M{4,8;−7,−1}, with trace three. BA is three-by-three; its diagonal entries come from row 1 of B paired with column 1 of A, row 2 paired with column 2, and row 3 paired with column 3. They are two, −2, and three, respectively, again summing to three. The shapes of the products differ, so the matrices cannot be equal.

The general equality follows by interchanging the two finite sums in the trace expansion, not by commuting the matrices. **Lesson:** a trace identity is a scalar equality; it must not be promoted to an equality of matrices.

### Problem 31 — Cyclic trace is not arbitrary swapping

Use square matrix units A = E<sub>12</sub>, B = E<sub>21</sub>, C = E<sub>11</sub> in dimension two. Find tr(ABC), tr(BCA), and tr(ACB).

**Solution.** The unit rule gives AB = E<sub>11</sub>, so ABC = E<sub>11</sub> and its trace is one. BC = E<sub>21</sub>, followed by A on the right, gives BCA = E<sub>22</sub>, also trace one. In contrast AC = E<sub>12</sub>E<sub>11</sub> = 0 because the middle indices do not match. Thus ACB = 0 and its trace is zero.

BCA is a cyclic rotation of ABC. ACB exchanges only the final two factors and is not such a rotation. **Lesson:** trace can rotate the full factor order; it cannot erase noncommutativity.

### Problem 32 — Frobenius norm and decomposition geometry

For A = @M{2,5;−1,4}, compute the Frobenius norms of A, its symmetric part H, and its skew part K from Problem 16. Verify the squared norm decomposition.

**Solution.** The squared norm of A is 4+25+1+16 = 46. For H = @M{2,2;2,4}, it is 4+4+4+16 = 28. For K = @M{0,3;−3,0}, it is 0+9+9+0 = 18. Hence 46 = 28+18. Their Frobenius inner product is 2·0+2·3+2·(−3)+4·0 = 0, which explains the Pythagorean relation.

The squared norms add, not the norms themselves. Also this is a matrix-entry geometry statement, distinct from whether A preserves vector lengths. **Lesson:** write the norm's subscript and square explicitly; several different norms and geometries coexist in linear algebra.

### Problem 33 — Two nonstandard products

For A = @M{1,2;0,3} and B = @M{4,0;−1,2}, compute A ⊙ B, AB, and A ⊗ B. State their shapes.

**Solution.** The Hadamard product is @M{4,0;0,6}, obtained by corresponding-entry multiplication. Ordinary multiplication gives @M{2,4;−3,6}, because each output entry sums two intermediate products. Both are 2-by-2 but differ. The Kronecker product is @M{4,0,8,0;−1,2,−2,4;0,0,12,0;0,0,−3,6}, of shape 4-by-4, consisting of blocks B, 2B, zero, and 3B.

The three products answer different mathematical questions. Identical shapes do not make the first two operations interchangeable, and the third deliberately enlarges the dimension. **Lesson:** determine the product symbol before applying a rule.

### Problem 34 — Exact operation counts and parenthesization

For A of shape 10-by-100, B 100-by-5, and C 5-by-50, compare both parenthesizations using classical multiplication. Count multiplications and minimal additions separately.

**Solution.** AB costs 10·100·5 = 5,000 multiplications and 10·5·99 = 4,950 additions. Then (AB)C costs 10·5·50 = 2,500 multiplications and 10·50·4 = 2,000 additions. Totals are 7,500 and 6,950.

For the other route, BC costs 100·5·50 = 25,000 multiplications and 100·50·4 = 20,000 additions. A(BC) costs 10·100·50 = 50,000 multiplications and 10·50·99 = 49,500 additions. Totals are 75,000 and 69,500. Both routes produce a 10-by-50 matrix. **Lesson:** associativity allows a tenfold reduction in this example's classical scalar counts, without changing the factor order or exact result.

### Problem 35 — A graph power counts walks

Let G = @M{0,1,0;1,0,1;0,1,0}, the adjacency matrix of an undirected three-vertex path. Compute G² and explain the meaning of its diagonal and off-diagonal entries. Prove the walk-count interpretation for all nonnegative integer powers.

**Solution.** Multiplication gives G² = @M{1,0,1;0,2,0;1,0,1}. Entry (1,3) is one because the sole two-edge walk is 1→2→3. Entry (2,2) is two because 2→1→2 and 2→3→2 both return to vertex two. These are walks; revisiting a vertex is allowed, so the diagonal is not necessarily zero.

For zero steps, I counts one empty walk from each vertex to itself. Inductively, (G<sup>k+1</sup>)<sub>ij</sub> sums (G<sup>k</sup>)<sub>ir</sub>G<sub>rj</sub> over the penultimate vertex r. Every length-(k+1) walk has exactly one such vertex and one final edge, so the sum counts each walk exactly once. **Lesson:** powers encode repeated composition; distinguish walks from simple paths.

### Problem 36 — Perturbation identity and an explicit bound

Let A = diag(2,1), B = I, E = @M{0,ε;0,0}, and F = @M{0,0;ε,0}, with real ε. Compute the exact product error and compare its Frobenius norm to the general bound.

**Solution.** AF = @M{0,0;ε,0}, EB = @M{0,ε;0,0}, and EF = @M{ε²,0;0,0}. Thus (A+E)(B+F)−AB = @M{ε²,ε;ε,0}. Its squared Frobenius norm is ε⁴+2ε², giving norm |ε|√(ε²+2).

The general bound gives √5|ε|+√2|ε|+ε² because ‖A‖<sub>F</sub> = √5, ‖B‖<sub>F</sub> = √2, and both perturbation norms equal |ε|. This bound is valid but conservative. Omitting EF gives a first-order approximation whose neglected norm is ε²; it is not the exact product. **Lesson:** retain the mixed perturbation term in an identity and state explicitly when you make an approximation.
