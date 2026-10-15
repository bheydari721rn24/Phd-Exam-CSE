## 21. Reflection is reversible; projection discards information

Let $P$ be the Euclidean orthogonal projector onto $S$. Define the reflection that fixes $S$ by $H=2P-I$. If $x=s+n$ is its perpendicular decomposition, then $Hx=s-n$. Therefore $H$ preserves the component parallel to the reflecting subspace and reverses the perpendicular component. Applying it twice returns $x$. Algebraically,

$$H^T=H,\qquad H^2=4P^2-4P+I=I,\qquad H^TH=I.$$

Thus this reflection is both symmetric and orthogonal, although $P$ is usually not an orthogonal **matrix**. An orthogonal projection is a closest-point map; an orthogonal matrix preserves every norm. A matrix can have the former description without the latter. Only the full-space orthogonal projector $P=I$ is also an invertible orthogonal matrix.

For a nonzero normal $n$, projection onto $n^\perp$ gives $P=I-nn^T/(n^Tn)$. Its reflection is

$$H=I-2\frac{nn^T}{n^Tn}.$$

The normal direction has eigenvalue minus one, and each direction in the hyperplane has eigenvalue one. More generally, the reflection fixing a rank-$k$ subspace in $\mathbb R^m$ has determinant $(-1)^{m-k}$ and trace $2k-m$. Conversely, if a real matrix is symmetric and orthogonal, then $H^2=I$, and $(I+H)/2$ is its orthogonal projector onto the fixed space. Orthogonality without symmetry is insufficient: a general rotation need not give an idempotent average with the identity.

## 22. Change of coordinates also changes the metric

Let $B$ be an invertible matrix whose columns are a coordinate basis, with physical vector $x=Bz$. If the physical projector is $P$, its coordinate matrix is $E=B^{-1}PB$. Similarity preserves idempotence, rank and eigenvalues. Ordinary symmetry need not survive because the new basis need not be orthonormal.

The Euclidean physical squared length becomes $z^TB^TBz$. Set $G=B^TB$. A correct coordinate representation satisfies

$$E^2=E,\qquad E^TG=GE.$$

To verify the second identity, substitute $E=B^{-1}PB$ and $G=B^TB$. Both sides reduce to $B^TPB$, using $P^T=P$. Conversely, these identities make $BEB^{-1}$ a physical Euclidean orthogonal projector. The metric carries the geometry that a nonorthonormal coordinate chart hides.

For $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and physical horizontal projector $P=\operatorname{diag}(1,0)$, the coordinate matrix is $E=\begin{pmatrix}1&1\\0&0\end{pmatrix}$. Its nonsymmetry does not imply that the physical map is oblique: coordinates use $G=\begin{pmatrix}1&1\\1&2\end{pmatrix}$. In the *ordinary coordinate dot product*, however, the same numerical matrix is an oblique projector. An examination must specify which metric is being used.

## 23. Alternating projections: derive the finite iterate first

Take the horizontal line and a line with unit direction $u=(\cos\theta,\sin\theta)^T$. Write $c=\cos\theta$ and $s=\sin\theta$, with $0<\theta<\pi/2$. Project first onto the sloping line by $Q=uu^T$, then onto the horizontal line by $P$. One full cycle is

$$M=PQ=\begin{pmatrix}c^2&cs\\0&0\end{pmatrix}.$$

Multiplication gives $M^2=c^2M$, and induction gives

$$M^j=c^{2j-2}M\quad(j\ge1).$$

The lines have zero intersection, so their intersection projector is zero. Since $0<c^2<1$, the finite iterates converge to zero. They are generally nonzero at every finite cycle. In particular, starting at $e_1$, the output after $j$ full cycles is $c^{2j}e_1$. The error target $c^{2j}\le\varepsilon$, for $0<\varepsilon<1$, requires

$$j\ge\frac{\log\varepsilon}{2\log c}.$$

Both logarithms are negative, so dividing by $2\log c$ reverses the preceding logarithmic inequality. The least integer is the ceiling of the displayed quantity. At perpendicular lines, $c=0$ and one cycle is exact; at coincident lines, $c=1$ and the intersection is the whole line instead of zero. Neither endpoint belongs in the logarithmic formula. Nearly parallel distinct lines converge slowly, although every individual projection is norm nonincreasing.

For general finite-dimensional subspaces, the convergence statement also holds. One proof avoids assuming simultaneous diagonalization. Put $T=S\cap U$. Both projectors fix $T$ and preserve $T^\perp$, since for $t\in T$ and $x\perp T$, $\langle Px,t\rangle=\langle x,Pt\rangle=0$. On $T^\perp$, a nonzero vector cannot retain its norm through both projections: equality in each contraction would place it in both subspaces and hence in $T$. The continuous function $x\mapsto\Vert PQx\Vert$ has a maximum $\rho<1$ on the unit sphere of $T^\perp$, which is compact. Thus the error after $j$ cycles is at most $\rho^j$ times the initial perpendicular component. If $T^\perp$ has dimension zero, both projections are the identity and the assertion is immediate. This proof uses finite dimension; infinite-dimensional analogues require different arguments and may lack a uniform rate.

## 24. Computing without constructing a dense projector

Suppose an $m\times k$ thin orthonormal basis $Q$ is already available. Computing $y=Q^Tb$ uses $mk$ scalar products and computing $p=Qy$ uses another $mk$ products, with comparable additions. Storage for $Q$ is $mk$ numbers. Building an $m\times m$ matrix $QQ^T$ uses much more storage when $k\ll m$ and is unnecessary for a single target.

The following pseudocode emphasizes the dimensions and the required input contract. It assumes a previously verified orthonormal basis; it does not turn arbitrary generators into one.

```text
project_with_basis(Q[m,k], b[m]):
    require transpose(Q) * Q = identity(k)
    y[k] = transpose(Q) * b
    p[m] = Q * y
    r[m] = b - p
    return p, r, dot(r,r)
```

For full-column-rank generators $C=QR$, coefficient recovery solves $Rc=Q^Tb$ by back substitution. The physical projection is $Q(Q^Tb)$ regardless of the conditioning of that coefficient recovery. If $\sigma_{\max}$ and $\sigma_{\min}$ are the largest and smallest positive singular values of $C$, then the eigenvalues of $C^TC$ are their squares. Therefore

$$\kappa_2(C^TC)=\frac{\sigma_{\max}^2}{\sigma_{\min}^2}={\kappa_2(C)}^2.$$

This exact identity explains why forming normal equations can amplify sensitivity in numerical coefficient calculations. It does not mean that every coefficient error is squared, that QR cures an intrinsically ill-conditioned problem, or that a dependent matrix has a finite full-column-rank condition number. Householder QR is a standard stable route for independent columns; rank-deficient numerical problems need a declared rank threshold, rank-revealing factorization or SVD. Exact arithmetic in the laboratory avoids rounding and does not certify arbitrary floating-point implementations.

## 25. Coverage map and boundaries

The core objectives are membership and perpendicularity certificates; basis construction and invariance; dependent coordinates; recognition by symmetry and idempotence; contraction; range, kernel, trace and diagonal constraints; weighted and complex geometry; affine feasibility; sums, products, containment and differences; trace overlap; reflection; coordinate change; finite iteration; and computational qualifications. The worked bank revisits these objectives through calculations, proofs and counterexamples. Basic checkpoints are deliberately interleaved with medium and hard synthesis so that a wrong hypothesis can be identified before a long calculation.

Detailed regression, random-noise estimation, pseudoinverse/SVD construction and statistical model selection belong to later chapters. This chapter uses or derives only the pseudoinverse examples needed to distinguish coefficient nonuniqueness from physical uniqueness. The sources were selected from a documented seven-university pool, not from an exhaustively searchable universe of all courses. Neither a finite source review nor a mathematical audit can guarantee perfect performance on every unseen examination question. The audit names what was checked and what remains uncertain.
