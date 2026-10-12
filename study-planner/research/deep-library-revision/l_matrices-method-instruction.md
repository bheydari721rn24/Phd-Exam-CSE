## Mathematical constructions needed by the examination bank

The full matrix-algebra lesson above establishes shapes, composition, transposes, inverse identities, blocks and computational counts. The bank also uses elementary determinant, dimension and coordinate arguments. The following constructions teach the exact additional results used here. Full elimination, general spectral theory and numerical factorization retain their later chapters. The four freshly rechecked core university texts supply the algebraic foundations; these proof expansions are independently written and are not attributed to unread course sections.

### 1. Determinant means an alternating volume function, not a diagonal shortcut

For a square matrix of positive size, define

$$\det A=\sum_{\pi\in S_n}\operatorname{sgn}(\pi)\prod_{i=1}^{n}a_{i,\pi(i)}.$$

The sum ranges over permutations, so every product chooses one entry from each row and each column. For a two-by-two matrix this gives $a_{11}a_{22}-a_{12}a_{21}$. The off-diagonal term is part of the definition. A general three-by-three matrix likewise involves six signed products; it cannot automatically use three diagonal entries alone.

The formula is linear in each column while the others are fixed. Swapping two columns changes the sign because it reindexes permutations with an odd swap. If two columns coincide, exchanging them leaves the array unchanged but negates its determinant, so the determinant is zero over the real or complex field. These facts prove the normalized alternating multilinear property, with $\det I_n=1$.

They also prove multiplicativity without assuming commutation. Write each column of $AB$ as a combination of columns of $A$, with coefficients supplied by the corresponding column of $B$. Multilinearly expand the determinant. Any term selecting one $A$ column twice vanishes. The surviving choices select all $n$ columns in a permutation order. The determinant of each such ordered selection is its permutation sign times $\det A$. Summing its scalar coefficients gives exactly the permutation formula for $\det B$. Therefore $\det(AB)=\det A\det B$. Only scalar coefficients were rearranged; no matrix factors were commuted.

If $A$ is upper triangular, a nonzero permutation term requires $\pi(i)\ge i$ for every $i$. Summing these inequalities and using $\sum_i\pi(i)=\sum_i i$ forces equality for every index. Only the identity permutation survives, giving $\det A=\prod_i a_{ii}$. This is a sufficient structural guarantee. A nontriangular matrix can coincidentally have the same determinant and diagonal product; that does not extend the shortcut to arbitrary matrices.

Multiplicativity implies similarity invariance: for invertible $B$, the identity $B^{-1}B=I$ gives $\det(B^{-1})=1/\det B$, and hence $\det(B^{-1}AB)=\det A$. Row multilinearity gives $\det(cA)=c^n\det A$, while trace scales only by $c$. These two scalar summaries measure different aspects of a transformation.

### 2. Constraints must be counted by independent functionals

Let $L:V\to W$ be a linear map on a finite-dimensional domain. Choose a basis $k_1,\ldots,k_r$ of its kernel and extend it to a basis $k_1,\ldots,k_r,v_1,\ldots,v_s$ of $V$. Every image is a combination of $L(v_j)$ because the kernel contributions vanish. If $\sum_j c_jL(v_j)=0$, then $\sum_jc_jv_j$ is a kernel vector and therefore a combination of the $k_i$. Independence of the extended basis forces every $c_j=0$. Thus $L(v_1),\ldots,L(v_s)$ form a basis of the image and

$$\dim V=\dim\ker L+\dim\operatorname{im}L.$$

On symmetric $n\times n$ matrices, the independent coordinates are the $n$ diagonal entries and $\binom n2$ upper off-diagonal entries. Mirrored lower cells are determined values. Trace is a nonzero functional: applying it to $E_{11}$ gives one. Trace zero therefore removes exactly one dimension. Adding a specified off-diagonal zero removes a second dimension when that coordinate exists, because evaluating the two proposed functionals on $E_{11}$ and $E_{ij}+E_{ji}$ proves their independence. Repeating the reflected equation does not remove a third dimension.

This theorem classifies real linear degrees of freedom. It does not count integer solutions. The authentic coupled nonnegative equations first require a reversible subtraction, then enumeration of lattice points in disjoint variable groups. Their affine dimension is three; their integer cardinality is 336. A correct matrix-rank statement can be an incorrect answer to a different counting question.

### 3. A rank bound becomes an equality only after information loss is excluded

For compatible maps $V$ then $U$, the product image is $U(\operatorname{im}V)$. Its dimension cannot exceed either the intermediate image dimension or the total image dimension of $U$. This proves the familiar upper bound. It does not prove equality, since $U$ may kill part of $\operatorname{im}V$.

For the bank's $n\times2$ full-column-rank $U$ and $2\times n$ full-row-rank $V$, the first action $V$ reaches every two-coordinate vector, and the second $U$ loses none of those vectors. Hence the product image is exactly $\operatorname{im}U$ and its rank is two. Injectivity also proves $\ker(UV)=\ker V$. The hypotheses require $n\ge2$; at $n=2$ the product is invertible, while at larger sizes it has nullity $n-2$.

The reverse action order can behave very differently. At $n=5$, take $U=[e_1\ e_2]$ and let $V$ read the third and fourth coordinates. The product $UV$ maps $(x_1,x_2,x_3,x_4,x_5)$ to $(x_3,x_4,0,0,0)$. It has rank two and square zero. In contrast $VU=0$. Both factors have their maximum possible rank, yet they are neither square inverses nor a guarantee of full rank in the reverse product. This is a concrete composition explanation, not a contradiction of the rank bound.

### 4. Nilpotent powers record chronological paths

For the three-coordinate shift, $N$ moves coordinate three to two and two to one. Two moves reach coordinate one, and three moves are impossible. Thus $N^2=E_{13}$ and $N^3=0$. Expanding $(I+N)^k$ is justified because its two summands commute. A term that contributes to the upper-right entry selects $N$ at two distinct time slots, with identity at all other slots. There are $\binom{k}{2}$ choices. One slot cannot perform both moves.

For weights $a,b,c$ above the diagonal,

$$N=\begin{pmatrix}0&a&b\\0&0&c\\0&0&0\end{pmatrix},\qquad (I+N)^k_{13}=kb+\frac{k(k-1)}2ac.$$

The first term is a direct move; the second passes through the middle coordinate. At nonnegative integer powers zero and one, the indirect contribution vanishes. At negative integer powers, derive the inverse $I-N+N^2$ first. The polynomial identity $I+kN+k(k-1)N^2/2$ continues to satisfy the integer group law because $N^3=0$, but the negative coefficient expression is a falling-factorial polynomial, not an ordinary count of choosing a negative number of slots.

For a strictly upper-triangular matrix of size $n$, any potentially nonzero product entry of $N^k$ follows a strictly increasing index chain of $k$ edges. No chain of $n$ edges exists among $n$ indices, so $N^n=0$. The actual Oxford definition correctly includes zero diagonal entries; this proof is an instructional expansion, not a correction of that definition.

### 5. Coordinate conversion has three separately justified stages

Let $B$ contain the new input basis vectors in standard coordinates. A coordinate list $c$ represents the physical vector $Bc$. A standard matrix $T$ maps that vector to $TBc$. If the same new basis is used on output, the output list is $B^{-1}TBc$, and the new array is $B^{-1}TB$. Each column can be checked by transforming one basis vector and solving for its coefficients.

For different input and output bases, with matrices $B,C$, the array is $C^{-1}TB$. Calling this a similarity would be incorrect unless the same ordered basis is used on both sides. Trace and determinant invariance concern similarity, not arbitrary independent coordinate changes. A rectangular transformation has separate input and output spaces and naturally uses two basis matrices.

For $B=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and $T=\operatorname{diag}(2,n)$, the second output image is $(2,-n)$. The equations $c_1+c_2=2$ and $c_1-c_2=-n$ give coefficients $(2-n)/2$ and $(2+n)/2$. This explicit coefficient solution explains the off-diagonal value and the common half-factor error before any compact conjugation formula is memorized.

### 6. Block inverse construction undoes the diagonal actions and their coupling

For compatible block coordinates $(x,y)$, the matrix $\begin{pmatrix}A&C\\0&D\end{pmatrix}$ sends them to $(Ax+Cy,Dy)$. If $A,D$ are invertible, solve backward: first $y=D^{-1}v$, then $x=A^{-1}u-A^{-1}CD^{-1}v$. Therefore

$$\begin{pmatrix}A&C\\0&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&-A^{-1}CD^{-1}\\0&D^{-1}\end{pmatrix}.$$

The coupling block can be rectangular or singular. Its inverse is never required. Both ordered products verify the formula, while changing factor order in its upper-right block generally fails. With identity diagonal blocks, the inverse coupling is simply negative $C$. With $A=I,D=2I$, it is $-C/2$ because the lower output must first be divided by two.

Two opposing block shears need not commute. Their products have diagonal blocks $I+XY,I$ in one order and $I,I+YX$ in the other. Equality requires both $XY=0$ and $YX=0$, not just $XY=YX$. Taking $X=Y=I$ gives equal internal products but unequal full block matrices. A new lower-left coupling also removes the automatic block-triangular determinant shortcut.

### 7. The Gram kernel theorem uses positivity and a declared field

For real $A$, the implication $Ax=0\Rightarrow A^TAx=0$ is immediate. For the reverse implication, the identity $x^TA^TAx=\sum_i(Ax)_i^2$ turns zero into a sum of nonnegative real terms. Every term must vanish. Thus the two kernels agree and rank–nullity makes their ranks agree.

For complex matrices the proof requires $A^*$ and squared absolute values. The column $(1,i)^T$ has ordinary bilinear self-product zero but Hermitian squared length two. Therefore using transpose in an unlabeled complex positivity argument is not a harmless typographical choice. Similarly, a positive-semidefinite weight can kill a nonzero output; a positive-definite weight is needed for $\ker(A^*HA)=\ker A$ without extra restrictions.

Positive definiteness of the equicorrelation matrix is proved by decomposing the full space into the all-equal line and its sum-zero complement. For dimension $d\ge2$, the two coefficients are $1+(d-1)a$ and $1-a$. Both must be strictly positive. Their positivity is sufficient because the decomposition exhausts every vector; testing a few random coordinates alone would not establish the theorem.
