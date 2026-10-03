## Teaching through formulas and conceptual decisions

### Make shape and factor order part of every calculation

If$A$ is$m\times k$ and$B$ is$k\times n$, then $(AB)_{ij}=\sum_{r=1}^kA_{ir}B_{rj}$ and the output has shape$m\times n$. Row-column pairing fixes the answer. Composition applies the rightmost factor first to column vectors. Associativity permits changing parentheses, not changing factor order. A transpose or inverse reverses product order: $(AB)^T=B^TA^T$ and $(AB)^{-1}=B^{-1}A^{-1}$ when both square factors are invertible.

### Calculate operation counts from shapes

The ordinary product of$m\times k$ and$k\times n$ matrices uses$mkn$ scalar multiplications and$mn(k-1)$ additions if each dot product starts from its first product. Parenthesizing a chain changes intermediate shapes and work. For shapes$10\times100$, $100\times5$, $5\times50$, the left association uses5000+2500=7500 multiplications; the right uses25000+50000=75000. Both yield the same exact mathematical matrix while their computational cost differs by a factor10.

### Exploit structure without assuming cancellation

For $A=I+N$ with$N^2=0$, the inverse is$I-N$ because their product is$I-N^2=I$. For a nilpotent$N$ of index$r$, the finite geometric inverse has alternating powers through$r-1$. A scalar cancellation rule cannot justify matrix cancellation: nonzero matrices can multiply to zero. Left cancellation requires an injective left action, while right cancellation requires a suitable right-side condition. Square invertibility supplies both.

The Gram matrix$A^TA$ satisfies $x^TA^TAx=\|Ax\|^2\ge0$. It is positive definite precisely when$A$ has independent columns. Orthonormal columns imply$A^TA=I$, but a tall rectangular$A$ cannot also satisfy$AA^T=I$ on the larger space. The latter product is a projection onto its column space.

## Formula and conceptual problem bank

### Question 1. Shape of a product

$A$ is$3\times2$ and$B$ is$2\times4$. What is the shape of$AB$?

**A.** 2 by2

**B.** 3 by4

**C.** 4 by3

**D.** The product is undefined.

**Answer: B.**

The shared inner dimension is2, so multiplication is defined. The surviving outer dimensions are3 and4. Each of the twelve output entries is a length-two dot product. Shape matching concerns inner dimensions, not equality of the complete input shapes.

### Question 2. Compute a rectangular entry

$A$ has first row$(1,2)$ and$B$ has second column$(3,4)^T$. What is$(AB)_{12}$?

**A.** 7

**B.** 8

**C.** 11

**D.** 14

**Answer: C.**

The requested entry pairs row1 of$A$ with column2 of$B$: $1\cdot3+2\cdot4=11$. Adding entries gives neither a matrix product nor a dot product. Matching rows instead of row and column can silently compute the wrong entry when matrices are square.

### Question 3. Composition order

With column vectors, $S$ doubles the first coordinate and$R$ swaps the two coordinates. Which product maps$(1,3)^T$ to$(6,1)^T$?

**A.** $RS$

**B.** $SR$

**C.** $R+S$

**D.** $S^2$

**Answer: B.**

Apply$R$ first to get$(3,1)$ and then$S$ to get$(6,1)$. Composition therefore corresponds to$SR$, with the rightmost factor acting first. Reversing the order gives$(3,2)$, showing that factor order matters. Matrix addition describes a sum of outputs, not sequential transformations.

### Question 4. Inverse order

For invertible square$A,B$, which expression equals$(AB)^{-1}$?

**A.** $A^{-1}B^{-1}$

**B.** $B^{-1}A^{-1}$

**C.** $(A+B)^{-1}$

**D.** $A^TB^T$

**Answer: B.**

Multiply $(AB)(B^{-1}A^{-1})$ and reassociate to obtain $A(BB^{-1})A^{-1}=I$. The opposite-side product also equals$I$. Reversing neither factor would require commuting matrices, which is not assumed. Transpose and inverse coincide only under additional orthogonality conditions.

### Question 5. A two-by-two inverse entry

For$A$ with rows$(2,1)$ and$(3,2)$, what is$(A^{-1})_{12}$?

**A.** -3

**B.** -1

**C.** 1

**D.** 2

**Answer: B.**

The determinant is$2\cdot2-1\cdot3=1$. The inverse has rows$(2,-1)$ and$(-3,2)$ after dividing by that determinant. Its row1,column2 entry is$-1$. Option$-3$ selects the wrong off-diagonal position. Swapping the diagonal and negating both off-diagonal entries must preserve their positions.

### Question 6. Nilpotent inverse

$N\ne0$ is square and$N^2=0$. Which matrix is the inverse of$I+N$?

**A.** $I+N$

**B.** $I-N$

**C.** $-N$

**D.** $N^{-1}$

**Answer: B.**

Compute $(I+N)(I-N)=I-N^2=I$ and likewise in the other order. The finite geometric series terminates because the square vanishes. A nonzero square-zero matrix is not invertible: otherwise multiplying$N^2=0$ by an inverse would force$N=0$. ThusD is not available.

### Question 7. Matrix-chain cost

Ordinary multiplication is used for shapes$10\times100$, $100\times5$, $5\times50$. Which association uses fewer scalar multiplications and how many?

**A.** Left,7500

**B.** Right,7500

**C.** Left,75000

**D.** Both,5000

**Answer: A.**

The left product costs$10\cdot100\cdot5=5000$ and produces$10\times5$; multiplying by the third costs$10\cdot5\cdot50=2500$. Total7500. The right product costs25000, then the first-times-result costs50000, total75000. Both outputs have shape$10\times50$, but associativity does not imply equal operation counts.

### Question 8. Rectangular orthonormal columns

$A$ is a real$5\times2$ matrix with orthonormal columns. Which assertion must hold?

**A.** $A^TA=I_2$

**B.** $AA^T=I_5$

**C.** $A$ is square.

**D.** $A^T=A$

**Answer: A.**

The entries of$A^TA$ are column dot products, yielding the two-dimensional identity. The product$AA^T$ has rank at most2 and cannot be the rank-five identity; it projects onto the column span. Equality with a transpose is not even shape-compatible here. Orthonormal columns give an isometry from a smaller domain, not a bijection on the larger space.

### Question 9. Gram positivity

For a real$m\times n$ matrix$A$, when is$A^TA$ positive definite?

**A.** Whenever$A$ has no zero entries.

**B.** Exactly when the columns of$A$ are linearly independent.

**C.** Whenever$m<n$.

**D.** Only when$A$ is symmetric.

**Answer: B.**

$x^TA^TAx=\|Ax\|^2$. This is strictly positive for every nonzero$x$ exactly when$Ax=0$ has only the zero solution, which is column independence. With$m<n$, dependence is unavoidable. Nonzero entries or symmetry alone do not decide whether a null vector exists.

### Question 10. Trace with rectangular factors

$A$ is$2\times3$ and$B$ is$3\times2$. Which identity always holds?

**A.** $AB=BA$

**B.** $\operatorname{tr}(AB)=\operatorname{tr}(BA)$

**C.** $\det(AB)=\det(BA)$

**D.** $A^TB=B^TA$

**Answer: B.**

Expand the two traces as $\sum_i\sum_j A_{ij}B_{ji}$ and reverse the finite summation order. Both traces are defined even though the product shapes differ. The products cannot be equal as shaped arrays, and determinant equality need not hold for different-size square products. The transpose products inD may not even be defined.

### Question 11. Outer product

For$u=(1,2)^T$ and$v=(3,4,5)^T$, what are the shape and$(2,3)$ entry of$uv^T$?

**A.** 2 by3,10

**B.** 3 by2,10

**C.** 2 by3,7

**D.** 1 by1,11

**Answer: A.**

A column of length2 times a row of length3 produces a$2\times3$ array. Entry$(i,j)$ is$u_iv_j$, so the requested entry is$2\cdot5=10$. An outer product uses no summation across shared entries. The reversed product$v u^T$ has the swapped shape but is a different matrix.

### Question 12. Kronecker structure

$A$ is$2\times3$ and$B$ is$4\times5$. What is the shape of$A\otimes B$?

**A.** 6 by9

**B.** 8 by15

**C.** 4 by5

**D.** 2 by3

**Answer: B.**

The Kronecker product replaces each scalar of$A$ by a scaled copy of$B$. Two block rows each have four rows, and three block columns each have five columns, giving$8\times15$. Shape addition6 by8 is not the rule; an elementwise Hadamard product would require equal input shapes instead.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Powers of a triangular nilpotent perturbation

$A=I+N$ is3 by3, where$N_{12}=N_{23}=1$ and all other entries of$N$ are zero. What is$(A^{10})_{13}$?

**A.** 10

**B.** 20

**C.** 45

**D.** 100

**Answer: C.**

$N^2$ has its only nonzero entry1 at(1,3), and$N^3=0$. Since$I$ commutes with$N$, the binomial expansion terminates: $A^{10}=I+10N+\binom{10}2N^2$. The requested entry is45. Ordinary entrywise exponentiation would miss the path through the intermediate coordinate. This binomial use is legal because the factors here commute, not because arbitrary matrices do.

### Question 14. Challenge: Inverse of a triangular block

A block matrix has rows of blocks$(I,B)$ and$(0,I)$ with compatible square identity blocks. What is the top-right block of its inverse?

**A.** $B$

**B.** $-B$

**C.** $B^{-1}$

**D.** $0$

**Answer: B.**

Multiply the proposed inverse with blocks$(I,-B),(0,I)$ in both orders. The top-right product is$-B+B=0$, while diagonal blocks remain identities. No inverse of$B$ is needed; it may even be singular or rectangular under compatible block sizes. This is the square-zero perturbation identity applied to a block matrix and avoids an unjustified cancellation of$B$.

## Applicable formulas and examination notes

### 1. Shape before arithmetic

$A_{m\times k}B_{k\times n}$ has shape$m\times n$. Entry$(i,j)$ pairs row$i$ with column$j$. If the inner dimensions do not match, the product is undefined rather than zero.

### 2. Column-vector order

In$ABx$, apply$B$ first, then$A$. Associativity changes parentheses but does not exchange factors. A shear or coordinate swap combined with a scaling gives a concrete test of a proposed commutation.

### 3. Transpose and inverse reversal

$(AB)^T=B^TA^T$ and, for invertible square factors, $(AB)^{-1}=B^{-1}A^{-1}$. The complex counterpart uses the adjoint. Reversal follows from the entry formula or the identity-product check, not from a visual mnemonic alone.

### 4. Two-by-two inverse

For rows$(a,b),(c,d)$ with$ad-bc\ne0$, the inverse has rows$(d,-b),(-c,a)$ divided by$ad-bc$. A zero determinant prohibits this formula. The off-diagonal entries are negated without being swapped.

### 5. Nonzero zero divisors

Nonzero matrices may satisfy$AB=0$. For example, complementary coordinate projections have zero product. Therefore$AB=AC$ permits cancellation of$A$ only under an injectivity or invertibility hypothesis, not just$A\ne0$.

### 6. Finite inverse series

If$N^r=0$, $(I+N)^{-1}=I-N+N^2-\cdots+(-1)^{r-1}N^{r-1}$. Multiply and telescope to verify both sides. The result uses nilpotence; convergence of an infinite series is unnecessary.

### 7. Ordinary product operations

Multiplying$m\times k$ by$k\times n$ costs$mkn$ multiplications and$mn(k-1)$ additions under first-product initialization. Initializing an accumulator to zero can change the addition count by$mn$. State which exact implementation is counted.

### 8. Chain parenthesization

For10 by100,100 by5,5 by50, left association costs7500 multiplications versus75000 on the right. Track intermediate shapes separately. Changing factor order is not a permitted optimization.

### 9. Gram condition

$A^TA$ is always positive semidefinite over real inputs and is positive definite exactly for independent columns. This follows from$\|Ax\|^2$. Having every entry nonzero does not rule out dependence.

### 10. Tall isometry

Orthonormal columns give$A^TA=I$ on the domain. For a tall matrix,$AA^T$ is a projection, not the full codomain identity. Its fixed vectors are exactly those in the column span.

### 11. Trace cycling

$\operatorname{tr}(AB)=\operatorname{tr}(BA)$ for compatible rectangular factors making both products square. With three factors, cyclic rotations preserve trace; arbitrary swaps need not. Product equality is much stronger and usually false.

### 12. Outer versus elementwise versus Kronecker

An outer product of column lengths$m,n$ has shape$m\times n$. A Hadamard product requires matching shapes. A Kronecker product multiplies dimensions, so2 by3 with4 by5 gives8 by15. None is interchangeable with ordinary matrix multiplication.

<!-- BOUNDARY-NOTES -->

### 13. Permutation side

Left multiplication by a permutation matrix reorders rows; right multiplication reorders columns. These are different actions even for a square matrix. Check one basis row or column to establish the indexing convention before applying a long permutation.

### 14. Symmetric and skew parts

Over real scalars, $A=(A+A^T)/2+(A-A^T)/2$ decomposes a square matrix uniquely into symmetric and skew-symmetric parts. A skew-symmetric real matrix has zero diagonal. This division-by-two argument does not transfer unchanged to a field of characteristic two.

### 15. Frobenius norm

$\|A\|_F^2=\operatorname{tr}(A^TA)$ for real matrices, the sum of all squared entries. Compatible orthogonal multiplication preserves this norm. Ordinary trace $\operatorname{tr}(A)$ alone is not a matrix norm and can vanish for a nonzero matrix.

### 16. Block compatibility

Block multiplication uses the ordinary sum-of-products rule with matched block dimensions. The scalar identity $ab=ba$ cannot be used to swap blocks. Triangular block formulas require invertibility of the blocks actually canceled.

### 17. Floating association

Matrix products associate exactly over exact arithmetic, but floating implementations can round at different intermediate stages. A lower multiplication count is an arithmetic-cost result, not automatically a stability guarantee. Separate symbolic correctness from numerical error bounds.
