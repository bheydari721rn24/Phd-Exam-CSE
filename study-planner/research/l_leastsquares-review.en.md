# Complete summary and examination decisions

## The argument in one coherent sequence

A least-squares problem begins with a feasible observation subspace and a declared metric. Orthogonal projection gives a unique closest fitted vector. A coefficient vector produces that fit exactly when its residual is perpendicular to every design column, equivalently when it solves the normal equations. The full coefficient solution set is one minimizer plus the design nullspace; unique coefficients therefore require full column rank. Independent columns make the Gram matrix positive definite, but QR gives a more reliable floating-point computational route than explicitly forming its inverse. Rank deficiency requires a separate minimum-norm convention if one coefficient answer is requested. Weights, constraints and penalties each modify a different part of the problem and require their own orthogonality or stationarity conditions. Statistical interpretation additionally requires an explicit noise model. The following decisions state those conditions and the errors they prevent.

## Modeling, dimensions and rank

1. A system with $m>n$ is overdetermined, not automatically inconsistent. Test $b\in\operatorname{col}(A)$ to decide exact consistency; for example repeated copies of a compatible equation remain consistent.
2. The coefficient vector has $n$ coordinates, while the fitted and residual vectors have $m$. Check every matrix product against these spaces before selecting an inverse formula.
3. In this chapter $r=b-Ax$. Changing to the opposite sign preserves its norm and zero-orthogonality equations, but changes expressions such as the signed residual vector and its coordinate interpretation.
4. Minimizing $\|r\|_2$ and $\|r\|_2^2$ gives the same minimizers because both are nonnegative and squaring preserves their order. This argument does not permit replacing squared error by absolute error.
5. The normal equations $A^TAx=A^Tb$ are necessary and sufficient for an unrestricted real Euclidean least-squares minimum. They remain valid when the Gram matrix is singular.
6. The identity $F(x_*+z)=F(x_*)+\|Az\|_2^2$ proves global minimality once $A^Tr_*=0$. It also shows exactly which directions leave the objective unchanged.
7. Every real finite-dimensional least-squares problem has a minimizer, including a zero design. Inverting a Gram matrix is one solution method with additional hypotheses, not the existence theorem.
8. All minimizers produce the same fitted vector $Pb$. They differ by exactly $\ker A$; their coefficient values need not be unique even when their observed predictions are.
9. Coefficient uniqueness for one response already implies full column rank, and hence uniqueness for every response with the same design. A special response cannot remove a nonzero design nullspace.
10. The identity $z^TA^TAz=\|Az\|_2^2$ proves equality of the two kernels. Therefore $A^TA$ is invertible exactly when the columns of $A$ are independent.
11. A $3\times4$ matrix can never have unique unrestricted least-squares coefficients because rank is at most three. A unique minimum-norm answer is an additional convention and remains possible.
12. For full column rank, $(A^TA)^{-1}A^T$ maps observations to coefficients; $A(A^TA)^{-1}A^T$ maps observations to fitted observations. Only the latter is the observation-space orthogonal projector.

## Fitting and observation geometry

13. A line fit with fixed input coordinates minimizes vertical data-plot errors. The residual vector is perpendicular to the column space in observation space; the plotted vertical segments generally are not perpendicular to the line.
14. With a constant feature in the design span, $\sum_i r_i=0$. Without that feature the identity need not hold; the through-origin fit in Problem 5 is an explicit counterexample.
15. A line with intercept passes through the sample centroid because its first normal equation gives $c+d\bar t=\bar b$. This is a statement about the declared vertical least-squares model.
16. Centered inputs make the constant and linear columns perpendicular. The slope denominator is $\sum_i(t_i-\bar t)^2$, positive exactly when not all inputs coincide.
17. Repeated input values are permitted and contribute repeated error costs. Identical input values cannot separately identify slope and intercept, no matter how many responses were collected there.
18. Polynomial regression is linear in the coefficients. Its design rank depends on sampled feature columns; nonlinear input functions do not invalidate linear least squares.
19. A degree-at-most-$k$ polynomial sampled at at least $k+1$ distinct real inputs has independent feature columns. Repeated observations increase weights but do not supply additional distinct roots.
20. Centering does not make raw quadratic features $1,t,t^2$ mutually perpendicular. Their constant-square product is $\sum_i t_i^2$, which is positive in every nontrivial full-rank design.
21. An invertible change $A'=AT$ preserves fitted values and transforms coefficients by $T^{-1}$. A coordinate penalty or minimum-norm convention generally changes unless its metric is transformed too.
22. Multiplying one noisy equation by a nonzero factor squares that factor in its residual weight. Exact row-equivalence of equations does not imply invariance of an inconsistent least-squares optimum.

## Computation and geometric certificates

23. Orthogonal but unnormalized columns give $x_j=(a_j^Tb)/(a_j^Ta_j)$. Using $A^Tb$ directly requires unit column lengths as well as perpendicularity.
24. Thin QR gives the triangular system $Rx=Q^Tb$. Solve it by backward substitution; an inverse in a theoretical formula is not a requirement to compute that inverse numerically.
25. A tall thin $Q$ satisfies $Q^TQ=I$, but generally $QQ^T\ne I_m$. The latter is the projector onto its column space, and the omitted directions account for residual error.
26. Full QR splits squared error into a variable triangular part and $\|Q_\perp^Tb\|_2^2$. The second term is irreducible; a transformed zero design row cannot be fitted by changing coefficients.
27. A Householder step must transform the response as well as the design. Orthogonal multiplication preserves a joint residual norm; changing just one side solves a different problem.
28. The stable Householder sign avoids cancellation in constructing its normal vector. Its mathematical correctness follows from the reflector formula, while the sign choice also protects finite-precision accuracy.
29. For full column rank, $\kappa_2(A^TA)=\kappa_2(A)^2$. This explains a numerical weakness of forming normal equations, without contradicting their exact algebraic characterization.
30. A small floating-point diagonal can indicate numerical rank loss but does not prove exact symbolic dependence. State the tolerance and scaling before interpreting a solver's rank report.
31. The correct certificate is residual perpendicularity to every design column. Perpendicularity to the data vector, one unrelated direction, or only a zero fitted vector is insufficient.
32. A rank-deficient minimum-norm solution lies in the row space and is perpendicular to the design nullspace. Arbitrary solutions of the normal equations need not satisfy this extra property.
33. The full-row-rank formula $A^T(AA^T)^{-1}b$ gives the minimum-norm exact solution. It must not be substituted into a tall design whose row Gram matrix is singular.
34. A solver can return an empty optional residual array for deficient rank even when its true error is nonzero. Explicitly compute $b-Ax$ before drawing an error conclusion.

## Weights, constraints and penalties

35. Positive definite weights give $A^TWr=0$. Ordinary $A^Tr=0$ can fail, and an ordinary Euclidean right-angle marker may misrepresent the weighted geometry.
36. A weighted projector is idempotent and $W$-self-adjoint: $P_W^TW=WP_W$. It need not be symmetric in ordinary coordinates; Problem 18 gives a concrete nonsymmetric example.
37. Semidefinite weights can ignore observations. Uniqueness requires the whitened design $CA$ to have independent columns, where $W=C^TC$; independent columns of $A$ alone no longer suffice.
38. Negative weights are not a norm and can make the loss unbounded below. The positive-remainder proof of normal-equation sufficiency does not apply to an arbitrary indefinite quadratic form.
39. Constrained least squares begins with feasibility of $Bx=d$. No objective can produce an exact constrained minimizer from an empty feasible set.
40. Feasible coordinates $x=x_0+Zy$ reduce a constrained problem to ordinary least squares with design $AZ$. Uniqueness requires $\ker A\cap\ker B=\{0\}$ on those feasible directions.
41. A finite constraint penalty is a relaxation, not literal enforcement of the equality. A large number does not repair inconsistent exact constraints or guarantee zero violation.
42. Identity ridge with positive $\lambda$ is unique because $A^TA+\lambda I$ is positive definite. This remains true when the original unpenalized design is rank deficient.
43. Ridge satisfies $A^Tr=\lambda x$, not the unpenalized zero-residual-product equation. Its fitted map generally is not idempotent and therefore is not an ordinary orthogonal projector.
44. Increasing an identity ridge parameter decreases coefficient norm and increases or preserves unpenalized residual norm. The complete penalized objective changes with the parameter, so compare like quantities.
45. A general penalty $\lambda\|Lx\|_2^2$ gives unique coefficients exactly when $\ker A\cap\ker L=\{0\}$. A positive parameter by itself does not identify a direction ignored by both operators.
46. Leaving the intercept unpenalized changes the penalty matrix. Claims that every coefficient is shrunk or that the penalty is invariant under arbitrary basis changes need separate justification.

## Sensitivity, added features and statistical interpretation

47. Leverage is $h_i=P_{ii}$ and depends on the design. It lies in $[0,1]$ and sums to the design rank; it is not a direct measure of whether the observed response is an outlier.
48. Deleted-observation residuals equal $r_i/(1-h_i)$ only when deletion preserves full column rank. At leverage one, the zero denominator signals loss of identifiability and must not be canceled against a zero residual.
49. Nested column spaces cannot have increasing minimum training error as features are added. The gain is the squared projection onto new perpendicular model directions; it is not proof of improved future prediction.
50. For one added feature residualize first: $u=(I-P)z$. If $u\ne0$, gain is $(u^Tb)^2/(u^Tu)$; if $u=0$, the feature is redundant and gain is zero without using a zero denominator.
51. A fixed-design response perturbation changes the fit by $P\delta b$ and residual by $(I-P)\delta b$, both contractions. Coefficients change by $A^+\delta b$ and can be highly sensitive to nearly dependent columns.
52. Perturbing the matrix adds the first-order term $(dA)^Tr$ to the differentiated normal equations. Omitting it assumes away an effect that can dominate when the original fit is inconsistent.
53. Statistical unbiasedness requires a declared zero-mean error model and $LA=I$ for every true coefficient vector. Exact zero-noise recovery alone does not specify a full error distribution.
54. Under spherical covariance, every unbiased linear competitor is $L_0+D$ with $DA=0$, and its covariance excess is $\sigma^2DD^T$. This proves BLUE for that competitor class without assuming Gaussianity.
55. Known unequal or correlated error covariance generally calls for GLS with $W=\Sigma^{-1}$. Ordinary least squares remains an algebraic optimizer but need not have the corresponding best-variance interpretation.
56. BLUE does not rule out a biased estimator having smaller mean squared error for some parameter values. Bias, variance, loss and the class of competitors must be stated before comparing estimators.
57. Expected residual sum of squares is $\sigma^2(m-\operatorname{rank}A)$ under the spherical model. Dependent named columns do not each consume a separate degree of freedom.
58. Zero covariance between coefficient errors and residuals does not prove independence. The four-outcome discrete construction in Problem 40 supplies an explicit counterexample; Gaussianity provides an additional theorem.
59. Complex least squares uses the adjoint $A^*$, and multiple response columns use a sum of column losses through the Frobenius norm. A plain complex transpose or a mistaken coupling of response columns changes the mathematics.
60. A final answer should state the metric, rank, requested coefficient convention, residual, optimality certificate, boundary cases and interpretation. A finite set of notes or checks supports these methods but cannot guarantee perfect performance on every unseen examination question.
