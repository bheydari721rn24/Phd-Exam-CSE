# Exact row traces: individually interpreted conclusions

These conclusions replace generic post-trace text for LG01–LG12. The existing exact row-operation arrays remain part of each answer.

## LG01

The final three rows state $x_1=2/3$, $x_2=-1/9$ and $x_3=11/9$. Each coefficient column contains a pivot. Thus every coordinate is forced: there are no free coordinates, and the displayed point is the unique solution.

Check the original equations explicitly. The first gives $2(-1/9)+11/9=1$. The second gives $2/3+1/9+11/9=2$. The third gives $4/3-1/9-11/9=0$. Hence the point satisfies all three original equations, including the equation initially moved by the swap.

The initial entry zero did not establish singularity. Row two supplied a legal first pivot when the complete equations, including their loads, were exchanged. The final coefficient identity proves uniqueness; an arbitrary later row order or a different sequence of nonzero scalings would give the same RREF. Swapping coefficient entries without their loads would solve a different problem. The tracked invertible transformation also certifies that none of these operations removed or added solutions.

## LG02

The final equations are $x_2=1$, $x_3=1$ and $0=0$. The first coefficient column contains only zeros, so $x_1$ never appears in an equation. The complete family is $(t,1,1)$ for arbitrary real $t$.

Substitution verifies all original loads: $1+2=3$, $2+4=6$, and $1=1$. Conversely any solution must have $x_3=1$ from the third original equation and then $x_2=1$ from the first; there is no remaining condition on $x_1$. This proves completeness rather than merely exhibiting a family of valid vectors.

The direction $(1,0,0)$ is a null vector, and its nonzero first coordinate proves that changing the parameter changes the solution. Rank is two and nullity is one, despite the array having three rows. A free coordinate may occur before the first pivot. Skipping an all-zero eligible coefficient column must advance the column index without consuming the next pivot row; treating the diagonal position as a compulsory pivot would incorrectly divide by zero.

## LG03

The coefficient pivots lie in columns one and two. The last two coefficient coordinates are free. Put $x_3=s$ and $x_4=t$. The final two nonzero equations then give $x_1=2+t$ and $x_2=s+4t$. Thus

$$x=(2,0,0,0)+s(0,1,1,0)+t(1,4,0,1).$$

Verify the original loads directly. The first left side is $(2+t)-(s+4t)+s+3t=2$. The second is $2(2+t)-(s+4t)+s+2t=4$. The third is $4(2+t)-3(s+4t)+3s+8t=8$. Every pair $(s,t)$ works. Conversely the free coordinates of any solution uniquely determine $s,t$, and the pivot equations force the two remaining coordinates. The two directions are independent because their third and fourth coordinates form an identity matrix.

The vanished third equation represents redundancy, not an additional restriction. Its coefficient row and its load equal twice the first original row plus the second. This dependence explains why three equations leave a two-dimensional family in four unknowns. The final zero row cannot be counted as a pivot or as a contradiction.

## LG04

The decisive final row is $[0,0,0,0\mid-10]$, which demands $0=-10$. No choice of the otherwise nonpivot coordinates can change this statement. Therefore the solution set is empty, not a two-parameter family.

The contradiction can be checked without trusting an elimination display. Let $w=(-3,1,1)^T$, using the original equation order. The weighted coefficient rows sum to

$$-3(1,1,1,1)+(2,3,-2,-3)+(1,0,5,6)=(0,0,0,0).$$

Their loads sum to $-3\cdot4+1+1=-10$. If $Ax=b$ held, multiplication by $w^T$ would give $0=-10$, which is impossible. This is a short certificate expressed in the original coordinates.

The coefficient rank is two and the augmented rank is three. The displayed array reduces only coefficient columns, so it need not be full augmented RREF: a full reduction would normalize and clear the load-column pivot as well. That extra work would not change the inconsistency conclusion. Always check this conclusion before assigning free variables or interpreting the coefficient rank as a solution-family dimension.

## LG05

The final identity coefficient block gives $x=(1,-1,2)^T$. Substituting into the original equations yields $3-1-4=-2$, $1-1+2=2$ and $2-4+2=0$, respectively. Thus existence is established by direct substitution. Since there are three coefficient pivots for three unknowns, all coordinates are forced and the solution is unique.

The displayed route begins by dividing row one by three, then normalizes the later current pivots $2/3$ and $-6$. These are all nonzero exact rational scalars, so every normalization is legal. A different route could exchange the original first two equations to obtain an initial unit pivot, but that is not the route shown here. The title and explanation must describe the actual trace rather than an alternative trace.

Fractions in intermediate arrays are not evidence of numerical error; they are exact field elements. In particular the final pivot minus six comes from the updated row after prior elimination, not the original bottom-right coefficient. Computing a later multiplier from the original array would silently invalidate the sequence even if the first operation were correct.

## LG06

The final equations are $x_1+8x_3=5/2$ and $x_2-x_3=-1/2$. Set the only free coordinate to $x_3=t$. The entire solution line is

$$x=(5/2,-1/2,0)+t(-8,1,1).$$

For the first original equation, substitution gives $5/2-8t+3(-1/2+t)+5t=1$. The second gives $5/2-8t-1/2+t+7t=2$. Conversely any solution has some third coordinate $t$, and the two reduced equations force exactly the displayed first and second coordinates. The nonzero direction establishes that distinct parameters give distinct solutions.

Geometrically, the two coefficient rows $(1,3,5)$ and $(1,1,7)$ are independent plane normals: proportionality would force the multiplier one from the first coordinate but then incorrectly require three to equal one. Their common solution set has one free coordinate, so the intersection is a line. Neither two equations nor three unknowns alone proves this conclusion; independence and consistency are the essential checks. The particular point corresponds to $t=0$ and is only one point on the intersection.

## LG07

Read the six-column augmented array as five unknowns and one load. The coefficient pivots are in columns one, three and five. Columns two and four are free. Set $x_2=s,x_4=t$ and obtain

$$x=(-9+s+5t,s,4-4t,t,3).$$

Equivalently this is $(-9,0,4,0,3)+s(1,1,0,0,0)+t(5,0,-4,1,0)$. The two directions are independent because the second and fourth coordinates recover their coefficients directly.

Substitution into the original first equation gives $(4-4t)+4t-3=1$. Into the second it gives $-18+2s+10t-2s+16-16t+6t+9=7$. Into the third it gives $-9+s+5t-s+4-4t-t+6=1$. These identities hold for every pair of parameters. Conversely the final pivot equations force $x_1,x_3,x_5$ after $s,t$ are selected, proving completeness.

The load in column six is never a sixth unknown or a free coordinate. The pivot count three gives nullity $5-3=2$, not $6-3$. Nonconsecutive pivots are entirely normal; searching only the diagonal would misclassify this system.

## LG08

The final point is $(3,-3/5,-9/5)^T$. Check it with exact fractions in the original equations. The first left side is $3/2-1/5-3/10=1$. The second is $3+3/5-18/5=0$. The third is $9/2-2/5-21/10=2$. Each coefficient column has a pivot, so these verified coordinates form the unique solution.

The rational operations in the trace preserve exact equalities. For example the lower residual coefficient $1/3$ is nonzero and supplies the last pivot; it is not a redundant equation. Normalizing that row forces $x_3=-9/5$, after which clearing its column yields the first two coordinates. A decimal threshold that discarded this nonzero coefficient would manufacture a free coordinate and change the problem.

An exact examination calculation may clear original denominators by multiplying whole rows by nonzero common denominators, including their loads. That produces a different valid elimination trace with the same final result. Approximating individual coefficients before classifying rank is a separate numerical model and requires its own scale and error analysis; it cannot be substituted silently for the rational model used here.

## LG09

The final coefficient rows give $x_1=1$ and $x_2=1$, followed by two identities. Original substitution gives loads $1+2=3$, $2-1=1$, $3+1=4$ and $4+3=7$. Therefore every original equation is satisfied. The two pivot columns force both unknowns, so no other solution is possible.

The third original coefficient row is the sum of the first two, and its load is also $3+1=4$. The fourth row is twice the first plus the second, with load $2\cdot3+1=7$. These matched dependences explain why the extra equations are compatible rather than contradictory. If either dependent load were changed independently while the first two equations remained fixed, the same row cancellation would expose a nonzero residual load and destroy consistency.

This example has four equations and two unknowns. The inequality alone does not determine compatibility. Both coefficient and augmented ranks equal two here, giving a unique solution. Distinguish redundant data, which are consistent checks, from inconsistent data, which impose an impossible condition after the independent equations have been solved.

## LG10

The reduced equations are $x_2+x_4=0$ and $x_3-x_4=0$. Coordinates one and four are free. Taking $x_1=s,x_4=t$ gives

$$x=(s,-t,t,t)=s(1,0,0,0)+t(0,-1,1,1).$$

Substitution into the first original equation gives $-t-2t+3t=0$; the second is twice that identity; the third gives $t-t=0$. Conversely the reduced equations force the second and third coordinates after $s,t$ are chosen. The two directions are independent because their first and fourth coordinates form the standard basis of the parameter plane. This establishes a two-dimensional nullspace.

The zero vector is obtained at $s=t=0$ and is always present in a homogeneous system. It is not the whole solution set because there are nonpivot coefficient columns. A completely zero augmented row is the identity $0=0$, so it cannot establish inconsistency. The leading positions are columns two and three, rather than the first two diagonal positions; a diagonal-only algorithm would miss the free early coordinate and misread the later pivot.

## LG11

The first two columns are coefficients and the last column is a load. Both rows therefore say $0x_1+0x_2=0$. Every pair $(s,t)\in\mathbb R^2$ satisfies them. Conversely every possible two-coordinate vector has exactly such a pair of coordinates, so the solution set is the whole plane.

There are no coefficient pivots and no contradictions. Rank is zero, and nullity is the number of unknowns, namely two. A basis of the homogeneous solution space is $(1,0),(0,1)$. These vectors are independent, and their linear combinations produce all coordinate pairs. Setting all free coordinates to zero selects the particular point $(0,0)$ but supplies no reason to exclude the other points.

There is no legal nonzero pivot to normalize, and none is needed. Skipping both coefficient columns is the correct finite outcome of the algorithm. The number of printed equations does not equal the number of independent restrictions: both printed equations are identities. This extreme boundary case is useful for detecting formulas that incorrectly subtract the row count from the number of unknowns.

## LG12

The two equations are $0x_1+0x_2=0$ and $0x_1+0x_2=1$. The first is an identity; the second is false for every coordinate vector. Consequently no solution exists, even though neither coefficient column has a pivot.

An original-coordinate impossibility certificate is $w=(0,1)^T$. Direct multiplication gives $w^TA=(0,0)$ and $w^Tb=1$. If $Ax=b$ held, applying $w^T$ would assert $0=1$. This proves the empty solution set without any division, row exchange or parameter assignment.

The coefficient rank is zero and the augmented rank is one. A full augmented RREF would move the nonzero load row above the zero row, but that row order cannot repair the contradiction. The coefficient-only display simply leaves the detected contradiction in its original position. Its two nonpivot coefficient coordinates do not yield a two-parameter solution family: the formula $n-r$ describes nullspace dimension, and describes an affine solution-family dimension only when the loaded system is consistent. Check consistency first.
