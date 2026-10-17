# Authentic examination placements: expanded teaching solutions

## Phd_CS_1404_Q33

**Read the assumptions before normalizing anything.** The question says that $L$ is lower triangular and $U$ is upper triangular. It does not prescribe a unit diagonal for either factor. We must therefore allow the diagonal scaling freedom of triangular factors.

The first column of $U$ is $(u_{11},0,0)^T$, so matrix multiplication gives

$$(LU)_{:,1}=u_{11}L_{:,1}=(3,0,6)^T.$$

The scalar $u_{11}$ cannot be zero because the product's first column is nonzero. Every possible first column of $L$ must consequently have middle coordinate zero and third coordinate exactly twice its first. Options one and two have the opposite sign ratio. Option four has a nonzero middle coordinate. Only option three, $(-1,0,-2)^T$, passes the necessary test; its scalar would be $u_{11}=-3$.

**Prove that the passing option is actually attainable.** A valid normalized factorization is

$$L_0=\begin{bmatrix}1&0&0\\0&1&0\\2&6/5&1\end{bmatrix},\qquad U_0=\begin{bmatrix}3&-2&4\\0&5&1\\0&0&-31/5\end{bmatrix}.$$

Their product has first two rows $(3,-2,4)$ and $(0,5,1)$. Its third row is $2(3,-2,4)+(6/5)(0,5,1)+(0,0,-31/5)=(6,2,3)$, which verifies every nontrivial entry. Set $D=\operatorname{diag}(-1,1,1)$ and define $L=L_0D$, $U=D^{-1}U_0$. The two inserted diagonal matrices cancel in the product, while multiplying $L_0$ on the right scales its first column by minus one. This gives exactly $(-1,0,-2)^T$ and proves existence.

**Answer: option 3.** Necessity eliminates the distractors; the constructed factors prove sufficiency. Imposing the unstated condition that $L$ has unit diagonal would incorrectly reject a legitimate answer. This answer is independently derived, rather than attributed to an official key.

## MS_CS_1405_Q113

**Eliminate the shared sum first.** Subtract the first equation from the second. Because subtraction is reversible while the first equation is retained, the system is equivalent to

$$x_1+x_2+x_3=5,\qquad x_4+x_5=15,$$

with every coordinate still a nonnegative integer. The variables now split into disjoint groups. Choosing any valid first-group triple and any valid second-group pair determines exactly one valid original five-tuple, and every valid original five-tuple yields exactly that pair of choices. This bijection justifies multiplication of counts.

For the triple, placing two separators among seven positions gives $\binom72=21$ solutions. The separator construction encodes five identical units split into three ordered boxes and permits empty boxes, as nonnegativity requires. An independent direct count fixes $x_1=k$ for each $k=0,\ldots,5$. Then there are $6-k$ choices for $x_2$ and $x_3$ is forced, giving $6+5+4+3+2+1=21$.

For the pair, choose $x_4=j$ for each $j=0,\ldots,15$ and then $x_5=15-j$. There are sixteen choices, all distinct and all nonnegative. Therefore the number of five-tuples is $21\cdot16=336$.

**Read every distractor against the actual constraints.** Option one is **37**, as verified in the original printed booklet; it adds $21+16$ instead of counting all pairs of independent choices. The quantity $\binom{24}{4}$ counts every nonnegative solution of the second equation alone, without requiring the first three coordinates to sum to five. Adding or multiplying that unrestricted count by $\binom72$ does not enforce the missing condition and does not count the required set.

**Answer: option 4.** The two independent real equations in five unknowns leave three real free coordinates, but that dimension is not an integer count. Nonnegativity and the fixed totals leave finitely many lattice points; the disjoint-group bijection counts precisely those points. The solution is independently derived and the original-source option transcription is now corrected.
