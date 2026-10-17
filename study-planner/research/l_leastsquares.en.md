# Least Squares: Fitting, Identifiability, Computation, and Estimation

## 1. Sources, prerequisites, and the question being solved

This English author-review draft builds on Orthogonal Projections, Gaussian Elimination, Rank, and Orthogonality. Read those chapters first if a column space, nullspace, orthogonal decomposition or triangular solve is unfamiliar. Calculus is introduced only after an algebraic proof of the central theorem. Statistical extensions state their additional probability assumptions explicitly.

The four primary written courses are MIT 18.06SC, Gilbert Strang; Stanford EE263, Stephen Boyd; Berkeley Math 54, Alexander Paulin; and ETH Zurich Linear Algebra for Computer Scientists, Afonso S. Bandeira and Robert Weismantel. Their chapter-specific strengths and limitations were compared before selection. The source audit records actual reading, candidate alternatives and exercise coverage. These are four universities, rather than four pages from one course. Oxford's written numerical-analysis syllabus was screened as an alternative; it is not counted as a fully read fifth course.

Least squares answers a specific optimization question: among vectors produced by a declared linear model, which one is closest to the observed data in a declared norm? It does not establish that the model is scientifically correct, that the data contain no outliers, or that a fitted relation is causal. A model that is linear in unknown coefficients may be nonlinear in its input variable. The algebra below separates those issues so that examination shortcuts have explicit hypotheses.

## 2. Three spaces and a consistent residual convention

Let $A\in\mathbb R^{m\times n}$ and $b\in\mathbb R^m$. The coefficient vector $x$ belongs to $\mathbb R^n$, the fitted observation vector $p=Ax$ belongs to $\mathbb R^m$, and the residual is always $r=b-Ax$. Stanford uses the opposite residual sign in its slides; that convention has the same squared norm, but signs in intermediate equations must be translated consistently.

Define $F(x)=\|b-Ax\|_2^2$. Minimizing the norm or its square gives the same minimizers because squaring is strictly increasing on nonnegative numbers. Multiplying the whole objective by a positive constant also leaves the minimizers unchanged. None of these facts permits changing the relative weights of separate observations.

An overdetermined system has more equations than unknowns. It need not be inconsistent: consistency is exactly $b\in\operatorname{col}(A)$. An underdetermined system can also be inconsistent when its rows are dependent and $b$ violates those dependencies. Matrix shape alone establishes neither consistency nor uniqueness.

## 3. Deriving the normal equations without calculus

Suppose $x_*$ minimizes $F$ and consider the line $x_*+tz$ for any fixed $z\in\mathbb R^n$. Write $r_*=b-Ax_*$. Direct expansion gives

$$F(x_*+tz)=\|r_*\|_2^2-2t z^T A^Tr_*+t^2\|Az\|_2^2.$$

If $z^TA^Tr_*$ were nonzero, a sufficiently small $t$ with the same sign would decrease the objective: the linear decrease dominates the quadratic term. Therefore it must vanish for every $z$, which is equivalent to $A^Tr_*=0$. This gives the normal equations

$$A^TAx_*=A^Tb.$$

Conversely, if those equations hold, the cross term vanishes for every $z$ and

$$F(x_*+z)=F(x_*)+\|Az\|_2^2\ge F(x_*).$$

Thus the equations are necessary and sufficient, even when $A$ is rank deficient. This identity proves global minimality. Merely setting a derivative equal to zero without identifying convexity or this nonnegative remainder would leave the sufficiency argument unfinished.

## 4. Existence, fitted-value uniqueness, and coefficient uniqueness

The column space is a finite-dimensional subspace and therefore has an orthogonal projection. Project $b$ onto it to obtain a unique point $p$. Since $p$ belongs to the column space, at least one coefficient vector satisfies $Ax_*=p$. The perpendicular residual satisfies $A^T(b-p)=0$, establishing existence for every real matrix and data vector, including $A=0$.

Two minimizers have the same fitted value. Indeed, the identity in Section 3 applied to their difference gives $A(x_2-x_1)=0$. Hence the complete set of minimizers is

$$x_*+\ker A.$$

The coefficients are unique exactly when $\ker A=\{0\}$, equivalently when $A$ has full column rank. This condition is independent of the particular $b$. If one least-squares problem with this matrix has unique coefficients, every data vector does. A rank-deficient model can have a unique fitted curve on the observed inputs while having infinitely many coefficient descriptions or different predictions at new inputs.

The squared norm of a nullspace component does not affect the fit. Selecting the minimum coefficient norm is an additional optimization criterion, taught explicitly below rather than silently imposed by normal equations.

## 5. Gram matrices, positive definiteness, and dimensions

For every $z$,

$$z^TA^TAz=\|Az\|_2^2.$$

Consequently $\ker(A^TA)=\ker A$ and $\operatorname{rank}(A^TA)=\operatorname{rank}A$. The Gram matrix is symmetric positive semidefinite. It is positive definite, and therefore invertible, exactly when the columns of $A$ are independent. In that case

$$x_*=(A^TA)^{-1}A^Tb,\qquad P=A(A^TA)^{-1}A^T.$$

The inverse has size $n\times n$, the coefficient map has size $n\times m$, and the projector has size $m\times m$. Dimension checks catch illegal substitutions such as $AA^T$ into a formula that requires an invertible column Gram matrix. For a tall full-column-rank matrix, $AA^T$ is singular whenever $m>n$.

The matrix $P$ is symmetric and idempotent. Its range is the column space and its complementary range is the left nullspace. These identities describe observation vectors. They do not mean that $x_*$ and $b$ have the same dimension or that the coefficient map is itself an observation-space projector.

## 6. A complete line fit and two different geometries

Fit $b_i=c+dt_i$ to $(1,1),(2,2),(3,2)$. The design matrix has rows $(1,t_i)$, so

$$A^TA=\begin{bmatrix}3&6\\6&14\end{bmatrix},\qquad A^Tb=\begin{bmatrix}5\\11\end{bmatrix}.$$

Subtract twice the first equation from the second to get $2d=1$. Then $3c+3=5$, giving $c=2/3$, $d=1/2$. The fitted values are $(7/6,5/3,13/6)$ and residuals $(-1/6,1/3,-1/6)$. Their sum and their time-weighted sum are both zero, so both normal equations are checked. Their squared sum is $1/6$.

In the two-dimensional data plot the error segments are vertical: each time is held fixed. In the three-dimensional observation space, the entire vector $r$ is perpendicular to the plane spanned by the constant and time columns. A vertical segment in the data plot is generally not perpendicular to the fitted line. Orthogonal regression, which changes both input and output coordinates to minimize perpendicular plot distances, is a different optimization problem. The interactive figures keep these two geometries separate.

This example reconstructs MIT's published worked fitting example with an independent normal-equation and residual certificate; it is not labeled as an invented examination question.

## 7. Centering, repeated inputs, and intercept identities

For a line with intercept, let $\bar t=m^{-1}\sum_i t_i$, $\bar b=m^{-1}\sum_i b_i$, and $s_i=t_i-\bar t$. The design columns $\mathbf1$ and $s$ are orthogonal because $\sum_i s_i=0$. Provided not all inputs coincide,

$$d=\frac{\sum_i(t_i-\bar t)(b_i-\bar b)}{\sum_i(t_i-\bar t)^2},\qquad c=\bar b-d\bar t.$$

Derive this by writing the line as $a+ds_i$. The first centered normal equation gives $a=\bar b$; the second gives the displayed slope. Transforming back gives $c$. The denominator is positive exactly when at least two input values differ. Repeated inputs are allowed; complete equality of all inputs destroys separate identifiability of slope and intercept.

An intercept makes the residual sum zero and makes the fitted line pass through $(\bar t,\bar b)$. These statements require the constant column to be present in the design span. A through-origin model generally has neither property. Centering is an invertible change of coefficient coordinates when the intercept is retained, so fitted values remain unchanged; dropping the intercept after centering the data changes the question unless the transformation is handled explicitly.

## 8. Beyond lines: bases, polynomials, and identifiability

For chosen functions $\phi_1,\ldots,\phi_n$, set $A_{ij}=\phi_j(t_i)$. The model is $\sum_jx_j\phi_j(t)$, linear in $x$ even if the features contain squares, exponentials or trigonometric terms. Least squares fits the sampled feature vectors; it does not require the features to be linear functions of $t$.

A degree-at-most-$k$ polynomial has $k+1$ coefficients. Distinct inputs numbering at least $k+1$ guarantee full column rank: a nonzero polynomial of degree at most $k$ cannot vanish at all those distinct inputs. Repeated samples change weights but do not create new distinct roots. More coefficients than distinct inputs prevent uniqueness, even if the number of observations is large.

Changing basis to $A'=AT$ with invertible $T$ leaves the column space and fitted vector unchanged. Coefficients transform as $x'=T^{-1}x$. An invertible rescaling of columns therefore changes coefficient norms and numerical conditioning, but not the unpenalized fitted values. A ridge penalty on the new coordinates generally changes the problem because the Euclidean coefficient norm is not invariant under arbitrary basis changes.

For centered symmetric inputs, odd powers are orthogonal to even powers in the discrete sample inner product. The constant and squared-input columns need not be orthogonal: their inner product is $\sum_i t_i^2$, positive unless every input is zero. Centering alone does not diagonalize a polynomial Gram matrix. Construct an actually orthogonal polynomial basis if that property is wanted.

## 9. QR: solve a triangular system, not an inverse

For full column rank, write the thin factorization $A=QR$ where $Q^TQ=I_n$ and $R$ is invertible upper triangular. The normal equations become $R^TRx=R^TQ^Tb$. Cancel $R^T$ to obtain

$$Rx_*=Q^Tb.$$

Compute the right-hand side and use backward substitution. The displayed inverse formula $R^{-1}Q^Tb$ characterizes the result; a numerical implementation should solve rather than explicitly form that inverse. Complete $Q$ to an orthogonal matrix $[Q\ Q_\perp]$. Orthogonal norm preservation gives

$$\|b-Ax\|_2^2=\|Q^Tb-Rx\|_2^2+\|Q_\perp^Tb\|_2^2.$$

The first term can be made zero; the second is the irreducible error. Therefore the fitted values are $QQ^Tb$, the residual is $Q_\perp Q_\perp^Tb$, and the minimum squared error is $\|Q_\perp^Tb\|_2^2$. Thin $Q$ does not preserve the norm of every vector in the observation space: it extracts coordinates of the projection. The full orthogonal matrix does preserve the norm.

## 10. Householder reflection and numerical conditioning

Given a nonzero column segment $v$, choose $\alpha=-\operatorname{sign}(v_1)\|v\|_2$, with sign one when $v_1=0$, and put $u=v-\alpha e_1$. The reflector is $H=I-2uu^T/(u^Tu)$. Since $u^Tu=2(\|v\|_2^2-\alpha v_1)$, direct substitution gives $Hv=\alpha e_1$. Expanding $H^TH$ gives $I$, so norms are preserved. Apply the same reflectors to $b$ as to $A$; transforming the matrix alone loses the correct right-hand side. The sign choice avoids subtracting nearly equal large positive numbers in the first component.

For independent columns, the eigenvalues of $A^TA$ are the squares of the positive singular values of $A$. Hence its spectral condition number is $\kappa_2(A^TA)=\kappa_2(A)^2$. Forming the Gram matrix can therefore lose accuracy sooner than an orthogonal-factorization method. This is a numerical warning about finite precision, not a claim that exact normal equations are mathematically wrong.

Classical Gram-Schmidt can also lose orthogonality numerically for nearly dependent columns. Householder QR is the standard stable direct route; modified Gram-Schmidt with appropriate reorthogonalization can be useful. A tiny floating-point diagonal does not by itself prove exact rank deficiency. State the tolerance, scaling and data accuracy used in a numerical rank decision. Detailed SVD algorithms belong to the later singular-value chapter; the geometric facts needed here are proved or explicitly identified.

## 11. Rank deficiency and the minimum-norm convention

Every least-squares solution is $x_0+z$ with $z\in\ker A$. Decompose $x_0=x_R+x_N$ into the row space and nullspace. Because these spaces are perpendicular, every solution can be written as $x_R+w$ and has squared norm $\|x_R\|_2^2+\|w\|_2^2$. Thus the minimum-norm least-squares solution is uniquely the one in the row space.

This defines the Moore–Penrose solution $A^+b$ geometrically: first project the data into the column space, then invert the restriction of $A$ from its row space onto its column space. That restriction is injective because a vector both in the row space and nullspace is zero; its dimensions are both the rank, so it is onto. This construction proves existence, uniqueness and linearity without using an invalid inverse of a singular Gram matrix.

For full row rank, the exact minimum-norm solution is $A^Tb'$ with $AA^Tb'=b$, hence $A^+=A^T(AA^T)^{-1}$. For full column rank it is $(A^TA)^{-1}A^T$. The two formulas have different rank hypotheses. For arbitrary rank, choose orthonormal bases of the row and column spaces, or use the later SVD construction; do not force either full-rank inverse formula.

## 12. Weighted and correlated-error least squares

Let $W$ be symmetric positive definite and minimize $(b-Ax)^TW(b-Ax)$. If $W=C^TC$ with invertible $C$, this equals $\|Cb-CAx\|_2^2$. Ordinary least squares on the whitened system yields

$$A^TWAx_*=A^TWb.$$

For independent columns the coefficient solution is unique. The observation projector is $P_W=A(A^TWA)^{-1}A^TW$. It is idempotent and satisfies $P_W^TW=WP_W$; it generally is not symmetric under the ordinary Euclidean product. The residual is $W$-perpendicular to every design column. If $W$ is diagonal, it rescales individual residual costs. Off-diagonal entries couple residual coordinates, so the loss cannot generally be interpreted as separate independent row weights.

Positive semidefinite weights require another qualification. If $C^TC=W$ but $C$ is singular, some observation directions are ignored. Uniqueness requires $CA$ to have independent columns, equivalently $\ker(CA)=\{0\}$. Full column rank of $A$ alone is insufficient. Zero weights remove information and negative weights can destroy convexity or make the objective unbounded below.

## 13. Exact linear constraints and feasible nullspace coordinates

Suppose coefficients must satisfy $Bx=d$. First check feasibility. Choose one feasible $x_0$ and let the columns of $Z$ form a basis for $\ker B$. Then every feasible vector is $x_0+Zy$ and the problem becomes

$$\min_y\|(b-Ax_0)-AZy\|_2^2.$$

This reduces the constrained problem to a standard least-squares problem without changing the constraint. Coefficients are unique over the feasible set exactly when $\ker A\cap\ker B=\{0\}$. There can be redundant constraints; feasibility and independent constraint rows are different properties.

Alternatively stationarity for a feasible minimizer gives $A^TAx+B^T\lambda=A^Tb$, together with $Bx=d$, using the Lagrangian $F(x)/2+\lambda^T(Bx-d)$. When $B$ has independent rows and the objective is strictly positive along every nonzero feasible direction, the associated block system is nonsingular. Without those hypotheses, multipliers may be nonunique even when the fitted vector is unique. A penalty with a large finite weight approximates a hard constraint; it is not literally the same condition.

## 14. Ridge and general quadratic regularization

For $\lambda>0$, ridge minimizes $\|b-Ax\|_2^2+\lambda\|x\|_2^2$. Its normal equations are

$$ (A^TA+\lambda I)x_\lambda=A^Tb.$$

The matrix is positive definite even when $A$ is rank deficient because its quadratic form is $\|Az\|_2^2+\lambda\|z\|_2^2>0$ for nonzero $z$. Equivalently solve the augmented least-squares system with design $[A^T,\sqrt\lambda I]^T$ and data $[b^T,0^T]^T$. This avoids interpreting regularization as new measured observations.

The ridge residual generally does not satisfy $A^Tr=0$; instead $A^Tr=\lambda x_\lambda$. The fitted-value map is generally not idempotent. With fixed $A,b$, coefficient norm is nonincreasing as $\lambda$ increases while unpenalized residual norm is nondecreasing. To prove this, compare optimality inequalities for two positive penalty values and add them; the penalty difference times the coefficient-norm difference has the required sign. Substituting the resulting sign into either inequality controls residuals.

For a penalty $\lambda\|Lx\|_2^2$, uniqueness requires $\ker A\cap\ker L=\{0\}$. An unpenalized intercept is represented by a zero in the corresponding penalty coordinate; it is not covered by a claim that every coefficient is shrunk. As $\lambda$ tends to zero, ordinary ridge tends to the minimum-norm least-squares solution; this follows by orthogonally diagonalizing the symmetric Gram matrix and observing the factors $1/(s+\lambda)$ on positive eigenvalues, with zero right-hand-side components along its kernel.

## 15. Fitted values, leverage, and an omitted observation

For full column rank, $p=Pb$. The diagonal $h_i=P_{ii}=\|Q_{i,:}\|_2^2$ is a leverage score. Since $P$ is an orthogonal projector, $0\le h_i\le1$ and $\sum_i h_i=n$. Changing only $b_i$ by $\delta$ changes its own fitted value by $h_i\delta$, and changes the full fit by $\delta Pe_i$. This is sensitivity to the response at a fixed design; it is not a definition of an outlier.

If removing row $i$ retains full column rank, then $h_i<1$ and the deleted-observation residual at its original input is

$$b_i-a_i^Tx_{(-i)}=\frac{r_i}{1-h_i}.$$

Here $a_i^T$ is row $i$ of $A$. To derive it, let $G=A^TA$, $c=A^Tb$ and $x=G^{-1}c$. The deleted normal equations are $(G-a_ia_i^T)x_{(-i)}=c-a_ib_i$. Subtract the original equations and solve the rank-one correction to obtain $x_{(-i)}=x-G^{-1}a_ir_i/(1-h_i)$. Multiplication by $a_i^T$ gives the formula. The same rank-one identity shows that the deleted Gram matrix is nonsingular exactly when $1-h_i\ne0$. At $h_i=1$, deletion loses rank; a zero-over-zero expression is not a valid leave-one-out answer.

## 16. Nested models and exact reductions in error

If one model's column space is contained in another's, the larger model's minimum residual norm cannot increase because it offers every earlier fitted vector. If their orthogonal projectors are $P_1,P_2$ with nested ranges, $P_2-P_1$ is the projector onto the added perpendicular directions. Thus

$$\|(I-P_1)b\|_2^2-\|(I-P_2)b\|_2^2=\|(P_2-P_1)b\|_2^2.$$

For one additional feature $z$, first residualize it against the old model: $u=(I-P_1)z$. If $u=0$, the feature is redundant and adds no fitted directions. Otherwise the added projector is $uu^T/(u^Tu)$, and the exact error reduction is $(u^Tb)^2/(u^Tu)$. This gives a fast conceptual solution to many comparison questions without recomputing the complete inverse.

A smaller training residual alone does not prove better prediction on new data. Adding arbitrarily many features can interpolate the sample while making coefficients unstable. That is a limitation of what the optimization criterion measures, rather than a reason to change its mathematical solution.

## 17. Perturbing observations and nearly dependent features

For fixed full-column-rank $A$, an observation change $\delta b$ gives $\delta x=A^+\delta b$, $\delta p=P\delta b$ and $\delta r=(I-P)\delta b$. Orthogonal projection is a contraction, so the fitted observation vector and residual change by at most $\|\delta b\|_2$. The coefficients can be much more sensitive when columns are nearly dependent because $\|A^+\|_2$ can be large.

For example, $A_\varepsilon$ with rows $(1,1),(0,\varepsilon),(0,0)$ has full column rank for nonzero $\varepsilon$. At data $(1,0,1)$ its coefficients are $(1,0)$ and its residual is $(0,0,1)$. Perturb the second observation by $\delta$; coefficients become $(1-\delta/\varepsilon,\delta/\varepsilon)$ while the fitted-vector change is only $(0,\delta,0)$. Exact rank and numerical sensitivity are different questions.

If the matrix also changes, differentiating the normal equations gives, to first order,

$$A^TA\,dx=A^Tdb+(dA)^Tr-A^T(dA)x.$$

The term involving the nonzero residual must not be omitted. Bounds for perturbing both matrix and data need additional residual and scaling information; the simple fixed-design contraction does not justify a universal coefficient-relative-error bound based only on $\kappa(A)$. A zero true coefficient vector also makes a relative coefficient error undefined.

## 18. What the BLUE statement actually assumes

Suppose $b=Ax_0+\varepsilon$ with fixed full-column-rank $A$, deterministic unknown $x_0$, $E[\varepsilon]=0$ and covariance $\sigma^2I$. A linear estimator is $Lb$. It is unbiased for every $x_0$ exactly when $LA=I$. Ordinary least squares uses $L_0=(A^TA)^{-1}A^T$, so it is unbiased and has covariance $\sigma^2(A^TA)^{-1}$.

For any other unbiased linear estimator write $L=L_0+D$ with $DA=0$. The cross products vanish because $L_0D^T=(A^TA)^{-1}(DA)^T=0$. Therefore

$$\operatorname{Cov}(Lb)-\operatorname{Cov}(L_0b)=\sigma^2DD^T.$$

This is positive semidefinite: every linear combination of coefficient errors has no smaller variance under $L$ than under least squares. No Gaussian assumption is needed for this covariance comparison. The word best refers to the class of linear unbiased estimators under this covariance model; it does not cover every biased or nonlinear estimator, every noise covariance, or every realized sample error.

Stanford's deterministic left-inverse characterization is consistent with zero-noise recovery. The statistical interpretation additionally needs the displayed zero-mean and spherical-covariance hypotheses. With a known positive definite covariance $\Sigma$, generalized least squares uses $W=\Sigma^{-1}$ and applies the same proof after whitening. With Gaussian errors it also maximizes the corresponding likelihood; that likelihood claim requires the Gaussian model, whereas the unbiased covariance claim does not.

## 19. Residual degrees of freedom and explicit statistical boundaries

Under the spherical zero-mean noise model, $r=(I-P)\varepsilon$. Its expected squared norm is $\sigma^2\operatorname{tr}(I-P)=\sigma^2(m-n)$ for full column rank, because $I-P$ is symmetric idempotent and has rank $m-n$. This uses $E[\varepsilon^TM\varepsilon]=\operatorname{tr}(M\operatorname{Cov}\varepsilon)$ for zero-mean noise, obtained by expanding the double sum.

For arbitrary rank $r_A$, replace $n$ by $r_A$. Dividing residual sum of squares by $m-r_A$ gives an unbiased estimator of the common variance only when that denominator is positive and the stated model holds. A saturated fit with $r_A=m$ has zero residual but supplies no residual degrees of freedom to estimate noise. Independence of coefficient estimates and residuals requires additional distributional conditions such as joint Gaussianity; zero covariance alone does not prove independence.

With an intercept, the observed data decompose into their constant mean, the centered fitted part, and residual. The latter two are perpendicular, so total centered sum of squares equals explained centered sum plus residual sum. The usual $R^2$ ratio needs nonzero total centered variation. A constant response makes that ratio undefined; forcing a default numerical value would be a software convention rather than the algebraic formula.

## 20. Complex data and multiple right-hand sides

Over $\mathbb C$, use the Hermitian norm and replace transposes by adjoints: $A^*(b-Ax)=0$. Orthogonality and positivity involve $z^*A^*Az=\|Az\|_2^2$, a real nonnegative number. The full-column-rank solution is $(A^*A)^{-1}A^*b$. A plain transpose can cancel a nonzero complex column against itself and produce an entirely wrong Gram matrix.

For a data matrix $B$ with several right-hand-side columns, minimize the Frobenius norm $\|B-AX\|_F^2$. This is the sum of the independent column objectives. Solve each with the same factorization; the normal equations are $A^TAX=A^TB$ in the real case. Uniqueness again depends on the design rank, not on the number of data columns. Reusing QR saves computation without coupling statistically unrelated responses unless an additional joint model is imposed.

## 21. An implementation that states its contract

For exact rational exercises, elimination on normal equations is useful and transparent. For floating-point computation, use a reliable QR-based solver for independent columns and a rank-aware SVD or pivoted factorization for deficient or uncertain rank. Do not calculate an explicit matrix inverse merely because a theorem displays one.

```python
import numpy as np

def fit_linear_model(design, observations):
    A = np.asarray(design, dtype=float)
    b = np.asarray(observations, dtype=float)
    if A.ndim != 2 or b.ndim != 1 or A.shape[0] != b.size:
        raise ValueError("Use one response for every design row.")
    if not np.isfinite(A).all() or not np.isfinite(b).all():
        raise ValueError("The design and responses must be finite.")
    x, _, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)
    fitted = A @ x
    residual = b - fitted
    return {
        "coefficients": x,
        "fitted": fitted,
        "residual": residual,
        "squared_error": float(residual @ residual),
        "numerical_rank": int(rank),
        "singular_values": singular_values,
    }
```

The rank is numerical and depends on the solver tolerance; it is not an exact symbolic proof. This solver selects a minimum-norm solution when coefficients are nonunique. The returned residual is computed explicitly because a solver's optional residual array can be empty for rank-deficient or underdetermined inputs; an empty array does not certify zero error. Inspect scaled normal-equation residuals and the model assumptions as well as numerical output.

## 22. Study route and transfer to unfamiliar questions

First identify the feasible model space, residual sign and metric. Next classify rank and decide whether the requested object is a fitted observation, any minimizing coefficient vector, or the minimum-norm vector. Choose the shortest justified route: a perpendicular certificate, centered sums, a triangular solve, a nullspace parameterization or a precise weighted model. Finally compute the residual and verify the appropriate orthogonality equation and objective value.

The following bank deliberately mixes numerical calculation, proof, inverse construction, counterexamples and model selection. Its source-derived items identify their provenance. The final decisions provide complete mathematical statements and tempting-error diagnoses. Reading solutions supports understanding; timed performance on unseen questions must still be established through later practice. No finite chapter can establish literal universal correctness or guarantee a particular examination result.

## References

1. MIT — Gilbert Strang — *18.06SC Linear Algebra*, Fall 2011 — [Session 2.3 summary](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/198bde3a6536b62989b6cc09495575c1_MIT18_06SCF11_Ses2.3sum.pdf), teaching pages 1–3; worked line fit and Gram invertibility. The license page is not counted as teaching content.
2. Stanford University — Stephen Boyd — *EE263 Introduction to Linear Dynamical Systems*, Autumn 2007–08 — [Lecture 5: Least-squares](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/ls.pdf), teaching pages 1–14 freshly read; later application pages screened previously. This chapter qualifies the statistical assumptions behind the BLUE terminology.
3. University of California, Berkeley — Alexander Paulin — *Math 54*, Spring 2018 — [Least-Squares Problems](https://math.berkeley.edu/~apaulin/Least-Squares%20Problems.pdf), all four original handwritten pages viewed. Both numerical examples are independently reconstructed in the problem bank.
4. ETH Zurich — Afonso S. Bandeira, Robert Weismantel — *Linear Algebra for Computer Scientists*, Part II, 2025 — [Lecture notes](https://ti.inf.ethz.ch/ew/courses/LA25/notes_part_II.pdf), Section 6.1, pages 12–15, plus the QR consequences on page 23 and minimum-norm construction on pages 24–25. Teaching-page and PDF numbering coincide in this edition.
