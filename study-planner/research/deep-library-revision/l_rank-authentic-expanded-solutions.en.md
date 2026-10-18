# Complete derivations for the two authentic revisits

## MS_CS_1405_Q41

**1. Define the ambient coordinates before counting restrictions.** A real symmetric four-by-four matrix is uniquely specified by its four diagonal entries and six entries strictly above the diagonal. Its reflected entries are already fixed by symmetry and are not six further unknowns. Thus the ambient vector space has dimension $4+\binom42=10$.

**2. Prove that trace contributes exactly one independent equation.** The map $T:S_4\to\mathbb R$, $T(M)=m_{11}+m_{22}+m_{33}+m_{44}$, is linear and onto, since $T(tE_{44})=t$. Its rank is one. The requested space is exactly its kernel, so rank–nullity gives $\dim W=10-1=9$.

**3. Construct all the matrices, not only their dimension.** Choose arbitrary real $a,b,c,p,q,r,s,t,u$. Every matrix in the space is uniquely

$$M=\begin{bmatrix}a&p&q&r\\p&b&s&t\\q&s&c&u\\r&t&u&-a-b-c\end{bmatrix}.$$

The nine displayed parameters vary independently. Six basis matrices are $E_{ij}+E_{ji}$ with $i<j$; the other three are $E_{11}-E_{44}$, $E_{22}-E_{44}$ and $E_{33}-E_{44}$. Off-diagonal entry comparison first kills the six pair coefficients in a zero combination; diagonal comparison then kills the remaining three. They therefore form an independent spanning list, independently confirming the count.

**4. Decide among the options.** The answer is **option 2, dimension nine**. Ten omits the trace restriction. Eight and seven subtract equations that the problem never imposes. A matrix and its transpose are not separate choices after symmetry has been imposed.

**Examination transfer.** First identify the independent ambient coordinates. Then prove the rank of the linear constraint map, using witnesses or an explicit parameterization. Subtract that rank, not the number of words or repeated equalities in the statement. This is a rechecked authentic revisit with an independently derived answer, not a claimed official key.

## Phd_CS_1404_Q30

**1. A positive lower bound rules out every nonzero kernel vector.** If $Ax=0$, the hypothesis gives $0\ge\theta\Vert x\Vert $. Because $\theta>0$ and a norm is positive on nonzero vectors, $x=0$. The real square finite-dimensional map is injective and hence invertible. Thus the nonsingularity assertion is true.

**2. Derive the inverse bound with the same induced norm.** For arbitrary output $y$, put $x=A^{-1}y$ in the hypothesis. It gives $\Vert y\Vert \ge\theta\Vert A^{-1}y\Vert $. Taking the supremum over nonzero $y$ yields $\Vert A^{-1}\Vert \le\theta^{-1}$. The substitution is justified only after invertibility has been established. This proves the first assertion.

**3. Handle complex eigenvalues without silently restricting them to real eigenvectors.** Under the Euclidean norm, write $z=u+iv$. The squared real inequality gives

$$\Vert Az\Vert _2^2=\Vert Au\Vert _2^2+\Vert Av\Vert _2^2\ge\theta^2(\Vert u\Vert _2^2+\Vert v\Vert _2^2)=\theta^2\Vert z\Vert _2^2.$$

If $Az=\lambda z$ and $z\ne0$, complex homogeneity gives $|\lambda|\Vert z\Vert _2\ge\theta\Vert z\Vert _2$, so $|\lambda|\ge\theta$.

**A stronger norm clarification.** The original page does not explicitly name its norm. The conclusion also follows for any real vector norm without assuming that an arbitrary complexification preserves the bound. Define $N(z)=\max_{0\le\phi\le2\pi}\Vert \operatorname{Re}(e^{i\phi}z)\Vert $. The maximum exists by continuity. This is a norm on the complexified space: the triangle inequality follows before taking the maximum; positivity follows by testing real and imaginary parts; multiplication by a complex scalar rotates $\phi$ and scales the maximum by its modulus. For real $x$, $N(x)=\Vert x\Vert $. Since $A$ is real, it commutes with taking these real parts, and the original lower bound gives $N(Az)\ge\theta N(z)$. Apply this to a nonzero complex eigenvector to obtain the same modulus conclusion for the original arbitrary real norm. No unproved equivalence between different induced norms is needed.

**4. Refute positivity by a complete admissible counterexample.** Take $A=-I$ and $\theta=1$. Every norm satisfies $\Vert Ax\Vert =\Vert -x\Vert =\Vert x\Vert $, so the hypothesis holds. Yet $x^TAx=-x^Tx<0$ for every nonzero real $x$. This matrix is negative definite, not positive definite. Hence **option 2 is false**. A magnitude lower bound prevents collapse of directions; it does not determine the sign of a quadratic form.

The source wording and options were rechecked against the original PDF image. This is an independently proved answer, not a claimed official key.
