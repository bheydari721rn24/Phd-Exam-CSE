# Gaussian elimination: expanded solution manuscript

Status: individual-review manuscript in progress. These thirteen expansions correspond to existing tasks LG13–LG25. They do not create thirteen new questions or constitute completion of the whole chapter review. The published chapter retains its own versioned edition until integration and presentation checks are complete.

## LG13

**Choose operations whose validity does not depend on the parameter.** Subtract twice the first equation from the second, and add the first equation to the third. These additions are invertible for every real value of the external parameter. They produce

$$x+z=-5,\qquad \alpha y+z=1,\qquad -\alpha y+(\alpha+1)z=\alpha^2-5.$$

Now add the new second equation to the new third. The final equation is

$$(\alpha+2)z=\alpha^2-4.$$

The coefficient block is triangular with diagonal entries $1,\alpha,\alpha+2$. Thus a generic solve can divide only when $\alpha\ne0,-2$. On that branch, factor the numerator to obtain $z=\alpha-2$. The second equation then gives $\alpha y=3-\alpha$, and the first gives $x=-\alpha-3$. All three coordinates are forced, so the solution is unique. Substituting into the three reduced equations verifies the result; reversibility verifies the original equations as well.

**Return to the undivided equations for each exceptional value.** At $\alpha=0$, the second reduced equation is $z=1$, whereas the last is $2z=-4$. Subtracting twice the former from the latter gives $0=-6$. Therefore no solution exists. The contradiction is exact and does not depend on a limiting argument.

At $\alpha=-2$, the last equation is $0=0$. Put $z=t$. Then $-2y+t=1$ gives $y=(t-1)/2$, and $x+t=-5$ gives $x=-5-t$. Every real $t$ works. Conversely every solution has some last coordinate $t$ and the first two equations force exactly those remaining coordinates; the family is complete.

**Examination decision.** Cancelling $\alpha+2$ in the generic calculation is legitimate only after excluding $-2$. Extending $z=\alpha-2$ to that value returns just $t=-4$ from an entire affine line. At $0$, that same generic expression would even conflict with a retained equation. A determinant identifies the two singular values; the transformed loads determine their different outcomes.

## LG14

Subtract the first equation from the second and third. Since these operations use no parameter division, the resulting system is equivalent for every real $\lambda$:

$$x+y+z=1,\qquad (\lambda-1)y=1,\qquad (\lambda-1)z=1.$$

For $\lambda\ne1$, the last two equations give $y=z=1/(\lambda-1)$. Substitution into the first gives $x=1-2/(\lambda-1)$. Each coordinate is forced, so there is exactly one solution. The reduced coefficient determinant is $(\lambda-1)^2$, agreeing with the determinant of the original coefficient matrix because row additions preserve determinants.

At $\lambda=1$, both later rows read $0=1$. One contradiction already suffices; two displayed contradiction rows do not raise the augmented rank by two. Here the coefficient matrix has three identical rows and rank one. The augmented matrix has rank two because its rows $(1,1,1,1)$ and $(1,1,1,2)$ are independent. Hence this branch is inconsistent.

**A repeated root is one parameter value.** The squared factor does not mean that there are two distinct exceptional values or that two free variables must exist. If the two later original loads were changed from two to one, the same singular coefficient matrix would instead yield $x+y+z=1$ and the complete family $(1-s-t,s,t)$. This comparison isolates the role of the load: the determinant is unchanged while compatibility changes.

## LG15

Subtract the first equation from the second to obtain $(\lambda-1)y=\lambda-1$. For $\lambda\ne1$, division gives $y=1$ and then $x=0$. Substitution yields $0+1=1$ and $0+\lambda=\lambda$, verifying the generic point.

For $\lambda=1$, substitute into the original equations before dividing. Both are $x+y=1$. Write $y=t$ and obtain $x=1-t$. Every real $t$ gives a solution, and the first equation forces this form for every solution. The null direction is $(-1,1)$; the difference between any two solutions is a multiple of that direction.

The generic vector $(0,1)$ has a perfectly well-defined limit as $\lambda$ approaches one, and it remains a valid solution at one. What fails is the assertion that this selected point describes every solution. For example $(1,0)$ also satisfies both exceptional equations but is never the generic solution. No continuity argument about one chosen vector can replace a rank and compatibility calculation.

**Examination decision.** The expression $(\lambda-1)/(\lambda-1)$ equals one on its stated nonzero domain. Its continuous extension is a numerical value, not a proof that an equation with zero coefficient still constrains its unknown. Always distinguish a formula's domain from the solution set of the original parameterized system.

## LG16

The first coefficient can vanish before any row operation. Keep that possibility visible. Subtracting the first equation from the second gives

$$\lambda x+y=1,\qquad (\lambda-1)y=\lambda-1.$$

When $\lambda\ne0,1$, the second equation forces $y=1$, and the first forces $x=0$. The determinant of the original coefficient matrix is $\lambda(\lambda-1)$, so these are precisely the nonsingular values.

At $\lambda=0$, the original system is $y=1$ and $0=0$. Thus $(x,y)=(s,1)$ for arbitrary real $s$. The first coefficient column is entirely zero, while the second contains a pivot. A solver must skip the first column rather than declare the whole system inconsistent or divide by its first entry.

At $\lambda=1$, both original equations are $x+y=1$, so $(x,y)=(1-t,t)$. The pivot now lies in the first column, and the second coordinate is free. Both exceptional systems have rank one and one free coordinate, but their pivot positions and affine directions differ.

Check the two families directly: at zero the first equation is always $1=1$ and the second is $0=0$; at one each equation reduces to $1-t+t=1$. Conversely those retained nonzero equations force exactly the stated forms.

**Examination decision.** Branching only on the last pivot's factor $\lambda-1$ misses the early zero coefficient at $\lambda=0$. Track every parameter-dependent division, including substitutions back into earlier rows. Counting the same number of free coordinates does not make two differently oriented solution families identical.

## LG17

Treat the three displayed equations as a triangular dependency structure, while checking both possible zero divisors. For $\lambda\ne1,-1$, the second equation gives $y=(\lambda^2-1)/(\lambda-1)=\lambda+1$, the third gives $z=(\lambda-1)/(\lambda+1)$, and the first gives $x=2-y=1-\lambda$. Inserting these expressions into the three equations verifies every generic value.

At $\lambda=1$, the second equation becomes $0=0$, so it imposes no condition on $y$. The third becomes $2z=0$, so $z=0$. Hence all solutions are

$$(x,y,z)=(2-t,t,0)=(2,0,0)+t(-1,1,0).$$

The retained first equation forces $x$ once $y$ is chosen, so no solutions are omitted. The coefficient and augmented ranks are both two.

At $\lambda=-1$, the second equation is $-2y=0$ and the third is $0=-2$. The latter proves inconsistency regardless of the first equation or any attempted choice of $y$. The coefficient rank is two and the augmented rank is three.

**Examination decision.** The two exceptional values arise in different rows and have different loads. Cancelling the numerator's factor in the second equation conceals its lost constraint at one; treating the third equation as a rational formula conceals its contradiction at minus one. The same instruction applies in larger systems: specialize the undivided rows, test contradictions, and only then count free coordinates.

## LG18

Use the visible row dependencies rather than solving three equations independently. The second coefficient row is twice the first and the third is three times the first. Applying those same combinations to the loads gives

$$x_1+2x_2-x_3=b_1,\qquad 0=b_2-2b_1,\qquad 0=b_3-3b_1.$$

Thus consistency is equivalent to both $b_2=2b_1$ and $b_3=3b_1$. Necessity follows from the two zero-coefficient rows. To prove sufficiency, choose arbitrary real $s,t$ and set

$$x=(b_1-2s+t,s,t)=(b_1,0,0)+s(-2,1,0)+t(1,0,1).$$

The first coefficient row applied to this vector equals $b_1$; the other rows then give $2b_1$ and $3b_1$, which equal the required loads. Conversely every solution has some coordinates $s=x_2,t=x_3$, and the first equation forces the displayed $x_1$. The two homogeneous directions are independent because their second and third coordinates are the two standard basis vectors. This establishes completeness with exactly two independent parameters.

The compatible loads form the line $\operatorname{span}\{(1,2,3)^T\}$. Two independent left-null vectors are $(-2,1,0)^T$ and $(-3,0,1)^T$; their products with $b$ are precisely the two compatibility residuals. Either nonzero residual is a complete impossibility certificate.

**Examination decision.** Checking only one row dependence is insufficient. For example $(1,2,4)^T$ passes the second-row check but fails the third. The one-dimensional set of attainable loads and the two-dimensional family of solutions to a fixed compatible load are different spaces in different roles.

## LG19

Write $A$ with rows $(1,2,-1)$ and $(2,4,-2)$ and write $b=(1,3)^T$. The coefficient rows have the exact dependence $-2A_{1,:}+A_{2,:}=0$. Apply this same dependence to the loads: $-2\cdot1+3=1$. Therefore the single row operation $R_2\leftarrow R_2-2R_1$ produces the impossible equation $0=1$.

The requested vector is $w=(-2,1)^T$. Its certificate has two separately checkable parts:

$$w^TA=(0,0,0),\qquad w^Tb=1.$$

Suppose a solution $x$ existed. Associativity gives $w^T(Ax)=(w^TA)x=0$, whereas $Ax=b$ would give $w^T(Ax)=w^Tb=1$. This contradiction proves impossibility without determining any unknown coordinate.

Neither equation is individually impossible. For example $(1,0,0)$ satisfies the first and $(3/2,0,0)$ satisfies the second. The failure is that their coefficient dependence is not matched by their loads. The coefficient matrix has rank one, while the augmented matrix has rank two.

**Examination decision.** A certificate must annihilate every coefficient column and leave a nonzero load. A vector that merely makes the load large, or nearly annihilates a coefficient in floating-point arithmetic, is not this exact proof. Any nonzero scalar multiple of $w$ is also a valid certificate; it need not have a prescribed normalization.

## LG20

The product $Ax$ is $(x_1,x_2,x_1+x_2)^T$. Therefore the first two coordinates of an alleged load immediately force $x_1=b_1,x_2=b_2$. Substituting them into the third equation gives the necessary condition $b_3=b_1+b_2$. It is also sufficient: the forced vector $(b_1,b_2)^T$ produces exactly that load.

Consequently the set of attainable loads is the plane

$$\{(u,v,u+v)^T:u,v\in\mathbb R\}\subset\mathbb R^3.$$

Every compatible load has a unique solution because the first two equations force both unknowns. Equivalently the two coefficient columns are independent and the nullspace is zero. There are nevertheless unattainable loads; $(0,0,1)^T$ is one explicit example.

For a failing load, use $w=(-1,-1,1)^T$. Direct multiplication gives $w^TA=(0,0)$ and $w^Tb=b_3-b_1-b_2\ne0$. This is an original-coordinate contradiction certificate, valid before any complete RREF calculation. For a compatible load the same functional vanishes, so it cannot then prove inconsistency.

**Examination decision.** A pivot in every coefficient column proves at most one solution for any load, and exactly one when compatible. It does not prove that every vector in the larger three-dimensional load space is attainable. A pivot in every row would address that existence question; this three-by-two matrix cannot have three coefficient pivots.

## LG21

Assume two distinct real solutions $u$ and $v$ exist. Subtracting their equations gives $A(v-u)=b-b=0$. Define $d=v-u$, which is nonzero, and for every real $t$ form $x(t)=u+td$. Linearity gives

$$Ax(t)=Au+tAd=b.$$

This verifies that the entire affine line consists of solutions. To prove that there are infinitely many distinct solutions, check injectivity: if $x(t)=x(s)$, then $(t-s)d=0$. Choose a nonzero coordinate of $d$; over the reals this forces $t=s$. Infinitely many real parameter values therefore give infinitely many different vectors. The possibilities are zero, one, or infinitely many solutions, with no finite count greater than one.

Over a finite field the same argument constructs a line, but the parameter has only finitely many values. For a consistent system of rank $r$ with $n$ unknowns, the standard free-coordinate map is a bijection from $\mathbb F_q^{n-r}$ to the solution set. There are exactly $q^{n-r}$ solutions, not automatically infinitely many.

For a concrete two-solution example, over $\mathbb F_2$ take $x_1+x_2=0$. Its solutions are exactly $(0,0)$ and $(1,1)$. Both satisfy the equation modulo two, and the other two possible pairs do not. Over the reals, the identical printed equation has the infinite line $(t,-t)$ instead.

**Examination decision.** The field hypothesis controls the cardinality conclusion. It is essential to the phrase “exactly two is impossible”; neither linearity nor a count of free coordinates by itself justifies the word “infinite.”

## LG22

The complete original solution set is $x=x_p+tv$, because the problem states that the entire nullspace is spanned by the nonzero vector $v$. Hence

$$x=(2+t,-1+2t,-t)^T.$$

Add the coordinates carefully. The constant sum is $2-1+0=1$ and the direction sum is $1+2-1=2$. The supplementary condition therefore becomes $1+2t=0$, giving the unique parameter $t=-1/2$. The selected vector is $(3/2,-2,1/2)^T$. Its coordinate sum is $3/2-2+1/2=0$.

No original coefficient matrix needs to be invented. Membership in the stated affine family already proves the original equations: $A(x_p+tv)=Ax_p+tAv=b$. Uniqueness under the additional condition follows because its coefficient two on $t$ is nonzero; two different parameters cannot both solve $1+2t=0$.

More generally, a new condition $c^Tx=d$ restricts this line by

$$(c^Tv)t=d-c^Tx_p.$$

If $c^Tv\ne0$, exactly one point survives. If $c^Tv=0$ and $d=c^Tx_p$, every point survives. If $c^Tv=0$ and the constants differ, no point survives. These alternatives explain why simply appending one more equation does not always reduce the number of free coordinates by one.

**Examination decision.** Apply extra restrictions after deriving the full field solution set. A valid additional condition selects a member of that family; it cannot turn a vector outside the family into a solution of the original system.

## LG23

The standard free coordinates are $x_3=s,x_4=t$, since columns one and two contain pivots. Solving their equations gives

$$x=(3-2s+t,-1+s-4t,s,t).$$

The proposed alternative uses $a=x_1$ and $s=x_3$. The map from the old parameters is $a=3-2s+t$. For every pair of real values $(a,s)$, there is exactly one inverse value $t=a-3+2s$. Thus the alternative parametrization is valid, and substitution gives

$$x=(a,11-4a-7s,s,a-3+2s).$$

Verify each original RREF equation. The first left side is $a+2s-(a-3+2s)=3$. The second is $11-4a-7s-s+4(a-3+2s)=-1$. Conversely a solution with coordinates $x_1=a,x_3=s$ must have the displayed $x_4$ from the first equation and then the displayed $x_2$ from the second, proving completeness and unique representation.

The linear part of the parameter change from $(s,t)$ to $(a,s)$ is the matrix with rows $(-2,1)$ and $(1,0)$. Its determinant is minus one, so the change is invertible. This is the relevant test, rather than whether a named coordinate happens to be called a pivot variable in the standard representation.

**Examination decision.** Two coordinate names do not necessarily give two independent parameters. If the first equation were $x_1+2x_3=3$ with no $x_4$ term, then $a$ and $s$ would have to satisfy $a+2s=3$ and could not both be chosen arbitrarily. Check the map and its inverse, not merely the number of labels.

## LG24

Apply $R_2\leftarrow R_2-R_1$ to the supplied matrix. The result is

$$E_1=\begin{bmatrix}1&1\\0&1\end{bmatrix}.$$

It is in REF because its nonzero leading entries occur in columns one and two in increasing order, and the entry below the first pivot is zero. Now apply the legal scaling $R_2\leftarrow2R_2$. This gives

$$E_2=\begin{bmatrix}1&1\\0&2\end{bmatrix}.$$

It also satisfies every REF condition, yet it is different from $E_1$. Both are row-equivalent to the original matrix: the first was obtained by an invertible row addition, and the second by that addition followed by an invertible scaling.

Neither displayed matrix is RREF. In $E_1$ the second pivot column has a nonzero entry above its pivot. In $E_2$ that same obstruction remains and the second leading entry is not one. Normalize the second row of $E_2$ by one half to obtain $E_1$, then apply $R_1\leftarrow R_1-R_2$ to obtain $I_2$. Starting directly from $E_1$ requires only that last operation. Their common RREF is therefore $I_2$.

**Examination decision.** A uniqueness theorem for RREF does not make REF, raw pivot values or operation traces unique. The exact two matrices above refute such claims constructively. The distinction depends on the definition: some authors additionally normalize REF pivots, so state the convention when presenting a counterexample based on scaling.

## LG25

Let the two row-equivalent RREF matrices have common row space $W$. For $j$ from zero through the number of columns, define $\pi_j$ to retain only the first $j$ coordinates of a row vector. The subspace $\pi_j(W)$ depends on $W$, not on which matrix represents it.

Suppose the nonzero rows of one RREF matrix have pivot columns $p_1<\cdots<p_r$. A row with pivot after $j$ is zero in every coordinate retained by $\pi_j$, so its projection vanishes. The projections of the rows with pivots at or before $j$ are independent: each retains a one at its own pivot coordinate and zeros at the other such pivot coordinates. They also span $\pi_j(W)$ because all original rows span $W$. Consequently

$$\dim\pi_j(W)=\#\{i:p_i\le j\}.$$

The difference between consecutive dimensions is one exactly when column $j$ is a pivot, and zero otherwise. Both RREF matrices have the same prefix dimensions and hence the same pivot columns. This proves the requested conclusion without determinants and applies to rectangular matrices as well.

To finish the stronger uniqueness statement, map a vector in $W$ to its coordinates at those $r$ pivot positions. The RREF nonzero rows map to the standard basis of $\mathbb R^r$, so this map is both onto and one-to-one: a linear combination with all pivot coordinates zero must have every coefficient zero. There is therefore exactly one vector in $W$ whose selected coordinates are a given standard basis vector. The corresponding nonzero rows of the two matrices must coincide. With the same total number of rows, their trailing zero rows coincide too.

**Examination decision.** The proof uses equality of row spaces, not just equal ranks. Two matrices with the same rank can have different row spaces and different pivot columns. The identity pattern at pivot coordinates is what supplies both the independent prefix counts and the unique normalized row representatives.
