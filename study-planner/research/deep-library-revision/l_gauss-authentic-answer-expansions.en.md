# Authentic examination solutions: expanded derivations

## Phd_CS_1404_Q33

**Use the triangular structure before attempting a full factorization.** The first column of an upper triangular matrix is $(u_{11},0,0)^T$. Thus multiplying by $L$ gives

$$A_{:,1}=u_{11}L_{:,1}=(3,0,6)^T.$$

The entry $u_{11}$ cannot be zero because the given first column is nonzero. Every possible first column of $L$ must therefore have second coordinate zero and third coordinate twice its first. Options one and two have the opposite ratio, while option four has a nonzero second coordinate. Option three, $(-1,0,-2)^T$, satisfies the necessary ratio with $u_{11}=-3$.

**Prove that the candidate can actually occur.** Necessity alone would not establish that some complete lower and upper triangular factors exist with the chosen column. Direct elimination of the given matrix yields

$$L_0=\begin{bmatrix}1&0&0\\0&1&0\\2&6/5&1\end{bmatrix},\qquad U_0=\begin{bmatrix}3&-2&4\\0&5&1\\0&0&-31/5\end{bmatrix}.$$

Multiply their rows and columns to check the least immediate third row. It is $2(3,-2,4)+(6/5)(0,5,1)+(0,0,-31/5)=(6,2,3)$. The other two rows reproduce the given first two rows, so $L_0U_0=A$.

Let $D=\operatorname{diag}(-1,1,1)$ and put $L=L_0D$, $U=D^{-1}U_0$. These matrices remain lower and upper triangular. Their product is $L_0DD^{-1}U_0=A$, and the first column of $L$ is exactly $(-1,0,-2)^T$. Hence option three is sufficient as well as necessary.

**Examination decision.** The source does not impose a unit diagonal on the lower factor. Imposing that additional normalization would change the problem and incorrectly eliminate the valid negative scaling. The selected answer is independently derived; no official answer-key status is inferred.

## MS_CS_1405_Q113

**Eliminate the common sum before counting.** The first equation fixes $x_1+x_2+x_3=5$. Subtracting it from the second gives $x_4+x_5=15$. These operations are equivalent to the original two equations: combining the two new equations recovers the original second equation.

For the first group, nonnegative triples summing to five are counted by $\binom72=21$. One derivation arranges five identical units and two separators; choosing the separator positions among seven positions is a bijection with the triples, including cases with a zero coordinate. An independent direct sum fixes $x_1=k$ for $k=0,1,\ldots,5$. Then $x_2$ has $6-k$ allowed choices and $x_3$ is forced. Their total is $6+5+4+3+2+1=21$.

For the second group, choose $x_4$ among the sixteen integers zero through fifteen. Then $x_5=15-x_4$ is forced and nonnegative. Therefore the second group has sixteen choices.

Every allowable first-group triple can be combined with every allowable second-group pair. Conversely every original solution splits uniquely into such a triple and pair. This Cartesian-product bijection proves the count

$$21\cdot16=336.$$

Thus option four is correct. Option one is **37**, as verified on the original booklet page: it adds $21+16$ instead of multiplying the independent choices. The two options involving $\binom{24}{4}$ count all nonnegative five-tuples summing to twenty, including tuples whose first three coordinates do not sum to five, so they do not enforce both original equations.

**Examination decision.** The real coefficient matrix has rank two and a three-dimensional affine family when constraints are interpreted over the reals. That dimension is not the requested number of nonnegative integer points. Eliminate the shared block, respect the domain and prove the counting correspondence before applying a formula.
