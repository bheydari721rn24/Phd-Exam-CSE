# Independent mathematical audit: l_matrices

Date: 12 October 2026. All **47 existing placements** were read individually from the current HTML using `read_deep_revision.py`, which loads only the AST helper definitions from `deep_revision_inventory.py` and does not run that module's inventory-writing main. Read ranges were 1–16, 17–32 and 33–47. This report owns no shared lesson, answer manuscript, gate or publication file. It is an independent mathematical audit, not a completed chapter or an assurance of universal examination performance.

## 1. Fresh original-page inspection

The original PDFs were independently hashed, freshly rendered and their complete page images actually viewed during this audit:

| Canonical item | Booklet PDF page | Original SHA-256 |
|---|---:|---|
| MS_CS_1405_Q41 | 9 | `198f75f9f9d195adc5c09ab14d17029e63a3cd11030d62cffcdfcb5df7627527` |
| MS_CS_1405_Q113 | 25 | same MSc booklet hash |
| Phd_CS_1404_Q30 | 8 | `928e51b55059b3094583f9c190e260b405ec775da05f6c7679675e332a8a6f40` |
| Phd_CS_1404_Q31 | 8 | same PhD booklet hash |
| Phd_CS_1404_Q32 | 8 | same PhD booklet hash |

Rendered evidence is in `C:/Users/bheydari/AppData/Local/Temp/deep-matrix-audit-sources/`: `MS_CS_1405_Q41.png`, `MS_CS_1405_Q113.png`, `Phd_CS_1404_Q30.png`. The last image contains all three named PhD questions.

### Newly identified authentic transcription error

**MSc CS 1405 Q113, chapter placement Q2: original option 1 is 37, not 32.** The original Persian digits are ۳۷. The key remains option 4, 336. This explains the intended additive distractor: the independent counts are 21 and 16, whose sum is 37. Correct the canonical option and every authentic placement using that canonical item, while treating changes to other chapters as source-only corrections rather than full chapter revision. The two other distractors are \(\binom{24}{4}+\binom72=10647\) and \(\binom{24}{4}\binom72=223146\).

### Authentic orthogonal-basis ambiguity preserved

Chapter Q4 is original PhD Q31, whose literal source says orthogonal, not explicitly unit length. It already carries the corrected ambiguity annotation. Preserve `answer=null`, `intendedAnswer=3`: a nonunit orthogonal basis invalidates both the general idempotence assertion and the reversed universal norm inequality. Under the added orthonormal interpretation, option 3 is the intended false general theorem, but the full-space case \(n=m\) makes all four statements true for that configuration. Do not restore an unqualified unique key or silently normalize the authentic wording.

## 2. Required authored wording improvements

1. **Q9 option 1 is false as a necessary-condition claim.** It says multiplying diagonal entries works directly *only* for triangular matrices. Triangular structure guarantees the rule, but some nontriangular matrices also satisfy the equality. For example

   \[
   M=\begin{pmatrix}1&1&1\\0&1&1\\1&0&2\end{pmatrix},\qquad \det M=2=\prod_iM_{ii}.
   \]

   Replace the option with: **“Triangular structure guarantees the diagonal-product determinant; arbitrary matrices have no such guarantee.”** Under the literal current wording there is no strictly correct scope option: the other three options are also false as universal claims. Keep intended answer 1 only after fixing the authored sentence.

2. **Q33 option 4 must specify the same new ordered basis in domain and codomain.** Independently changing the input and output bases gives \(Q^{-1}AP\), which is not generally similarity. Replace “Changing both input and output basis” by “Using the same new ordered basis for both input and output of an endomorphism.” The question's own single specified ordered basis already permits the intended calculation.

3. **Q14–17 must explicitly use \(n\ge2\).** A cyclic shift with no fixed coordinate does not exist at \(n=1\). The present generic positive-integer domain is qualified by the no-fixed-coordinate premise, so the correct calculation is not wrong, but the excluded parameter deserves an explicit statement.

4. **Q26–29 must explicitly use \(n\ge2\).** Both factors having rank two forces this domain. At \(n=2\), UV actually is invertible; at \(n>2\), it is singular. Therefore say the larger square product need not be invertible, not that it is always singular.

5. **Q25's commutation statement is a guarantee for the usual universally valid binomial grouping.** Do not claim that a numerical coincidence for one exponent is logically impossible for noncommuting matrices. For the standard square identity \((A+B)^2=A^2+2AB+B^2\), commutation is exactly required, because the difference is BA−AB.

6. Pattern citations such as symmetric-dimension Q41 or integer-counting Q113 do not by themselves establish a substantive mathematical relationship to every matrix family. Their provenance is an author comparison, not evidence that nilpotent-power or inverse-order questions occur in those specific items. Avoid presenting a generic pattern label as an authentic source for the calculation.

## 3. Full answer ledger

Option order is the current authored order. Q4 remains ambiguous; Q9 needs the wording correction above. No other numerical or symbolic wrong key was identified.

| Placement | Option | Independently derived answer |
|---|---:|---|
| 1 | 2 | Symmetric trace-zero dimension 9 |
| 2 | 4 | 336; original option 1 must be 37 |
| 3 | 2 | Positive definiteness does not follow from the norm lower bound |
| 4 | null | Intended normalized general-theorem answer 3; literal source is ambiguous |
| 5 | 2 | \(-1/2<a<1\) |
| 6 | 4 | \(\det(I+J)=6\) at n=5 |
| 7 | 3 | \(\det(I+J)=9\) at n=8 |
| 8 | 2 | \(n+1\) |
| 9 | Correct wording first | Intended option 1 after replacing “only” by the guaranteed-rule statement |
| 10 | 1 | Inverse entry -5 |
| 11 | 4 | Inverse entry -8 |
| 12 | 3 | Inverse entry \(-n\) |
| 13 | 2 | Matrix inversion is not entrywise reciprocation |
| 14 | 3 | Product trace 0 at n=5 |
| 15 | 2 | Product trace 0 at n=8 |
| 16 | 1 | 0, for n≥2 and the specified no-fixed-coordinate shift |
| 17 | 4 | Cyclic trace identity is distinct from trace multiplicativity |
| 18 | 2 | \(6^5=7776\) |
| 19 | 1 | \(6^8=1679616\) |
| 20 | 4 | \(6^n\) |
| 21 | 3 | Scaling every row supplies a dimension-dependent determinant power |
| 22 | 3 | \((I+N)^5_{13}=10\) |
| 23 | 2 | \((I+N)^8_{13}=28\) |
| 24 | 1 | \(\binom n2\) |
| 25 | 4 | Commutation justifies the ordinary binomial grouping |
| 26 | 1 | Product rank 2 |
| 27 | 4 | Product rank 2 |
| 28 | 3 | Product rank 2, with n≥2 |
| 29 | 2 | The generic smaller-rank upper bound does not prove equality |
| 30 | 3 | New-basis entry \(-3/2\) |
| 31 | 2 | New-basis entry -3 |
| 32 | 1 | \((2-n)/2\) |
| 33 | 4 | Similarity when the same ordered basis is used on both sides |
| 34 | 1 | Block determinant \(2^5=32\) |
| 35 | 4 | Block determinant \(2^8=256\) |
| 36 | 3 | \(2^n\) |
| 37 | 2 | Off-diagonal block invertibility is unnecessary |
| 38 | 3 | Dimension 13 |
| 39 | 4 | New-basis columns (2,1) and (1,0) |
| 40 | 3 | Nilpotent power entry 21 |
| 41 | 1 | \((ABA^{-1})^{-1}=AB^{-1}A^{-1}\) |
| 42 | 1 | \(\ker(A^TA)=\ker A\), for real A |
| 43 | 2 | \(-1/3<a<1\) |
| 44 | 2 | \(\operatorname{tr}(AB)=\operatorname{tr}(BA)\) |
| 45 | 2 | Inverse upper-right block \(-C\) |
| 46 | 3 | Nilpotent power entry 45 |
| 47 | 2 | Inverse upper-right block \(-B\) |

## 4. Complete transferable family derivations

### Authentic Q1 and integrated Q38: independent matrix constraints

A real symmetric matrix of size four has four diagonal and six upper off-diagonal coordinates. The lower off-diagonal entries are determined copies. Trace is a nonzero linear functional, because it maps \(E_{11}\) to 1. Removing its rank one leaves dimension 9. A basis is the six matrices \(E_{ij}+E_{ji}\), i<j, plus three \(E_{ii}-E_{44}\), i=1,2,3. Inspection of entries proves independence and unique spanning.

For Q38, the symmetric size-five space has dimension 15. The trace functional and the (1,2) entry functional are independent: evaluating a proposed relation between them on \(E_{11}\) first forces the trace coefficient to zero, then evaluating it on \(E_{12}+E_{21}\) forces the other coefficient to zero. Rank two therefore leaves dimension 13. Symmetry has already identified (1,2) with (2,1); they are not two independent restrictions. Sizes zero and one have special domains: the off-diagonal condition does not exist there. Counting written equations instead of independent functional rank is the specific error behind over-subtraction.

### Authentic Q2: real dimension is not lattice cardinality

Subtracting the first equation from the second gives \(x_4+x_5=15\). For each \(x_1\in\{0,\ldots,5\}\), the pair (x2,x3) has 6−x1 choices. Thus the first group has \(6+5+4+3+2+1=21\) points. The second group has choices x4=0 through 15, exactly 16. Combining any first-group point with any second-group point gives one admissible five-tuple and vice versa, so the product is 336. The original option 37 adds these independent choice counts. The binomial \(\binom{24}{4}\) ignores the first equation and counts every nonnegative five-tuple summing to 20; adding or multiplying it by 21 does not enforce intersection of the equations. The real linear system has rank two and affine dimension three, which is not its number of nonnegative integer solutions.

### Authentic Q3: lower norm bound

Trivial kernel follows from \(Ax=0\Rightarrow0\ge\theta\|x\|\). A square map then has an inverse. Substituting \(x=A^{-1}y\) gives \(\|A^{-1}y\|\le\theta^{-1}\|y\|\), hence the induced inverse norm bound. Positive definiteness fails for A=−I with θ=1 under every vector norm.

For an arbitrary finite-dimensional real norm, nonreal eigenvalues can be handled without silently assuming a complex norm: set B=A^{-1}, use \(\|B^k\|\le\theta^{-k}\), and norm equivalence \(c\|x\|_2\le\|x\|\le C\|x\|_2\). It follows that \(\|B^kx\|_2\le(C/c)\theta^{-k}\|x\|_2\) for real vectors. Squaring and adding the bounds for real and imaginary parts extends that Euclidean estimate to complex vectors. On a complex eigenvector for μ, \(|\mu|^k\le(C/c)\theta^{-k}\); kth roots and a limit yield \(|\mu|\le\theta^{-1}\), hence \(|\lambda|\ge\theta\) for A. Keep the equivalence constant outside the kth power.

### Authentic Q4: preserve both interpretations

For a nonunit orthogonal basis, \(P_s=\sum u_ku_k^T\) has eigenvalue \(\|u_k\|^2\) on the kth basis direction. It is idempotent only when all basis lengths are one. For u=(2,0), Ps=diag(4,0), whose square is diag(16,0); for x=(0,1), the reversed inequality reads 1≤0. Options 2 and 4 remain true because outputs are combinations of the basis vectors and coefficient functionals are linear. Normalizing or inserting squared-length denominators gives the true orthogonal projection; Pythagoras proves contraction. With a full orthonormal basis P=I, so the reverse inequality is equality. This source requires ambiguity handling, not a manufactured unique literal key.

### Authentic Q5 and integrated Q43: structured definiteness

In dimension d≥2, write the matrix as \(A=(1-a)I+aJ\). Decompose x=s*1+z with sum z=0. Then

\[
x^TAx=d[1+(d-1)a]s^2+(1-a)\|z\|_2^2.
\]

The two perpendicular spaces exhaust all directions, proving positive definiteness iff both coefficients are positive. The ranges are (-1/2,1) for d=3 and (-1/3,1) for d=4. At the endpoints a nonzero subspace is null, so the matrices are semidefinite rather than definite. At d=1 the unused off-diagonal parameter has no restriction. Negative off-diagonal entries can yield positive-definite matrices; positive entries alone do not prove definiteness. Determinant positivity alone is inadequate: for d=3, \((1-a)^2(1+2a)>0\) when a>1, while two quadratic directions are negative.

### Q6–9: identity plus all ones

Let q=1=(1,...,1). For every x, Jx=(sum x_i)q, so Jq=nq and Jz=0 when sum z_i=0. Over the real field these are complementary spaces. I+J therefore acts by n+1 on the line and 1 on the (n−1)-dimensional complement, giving determinant n+1: 6 and 9 in the required instances. This is a diagonal product after a justified basis change, not the product of the displayed diagonal entries, which are all 2 and give the wrong 2^n.

The inverse can be verified without an eigenvalue theorem: J²=nJ, so \((I+J)(I-J/(n+1))=I\), and the reverse multiplication is identical. More generally \(\det(\alpha I+\beta J)=\alpha^{n-1}(\alpha+n\beta)\) for n≥2, with an inverse when both displayed factors are nonzero. At n=1 the matrix is the scalar α+β; α need not separately be nonzero. A singular addend J for n>1 does not force the sum singular. At n=0 the conventional empty determinant is 1, but there is no all-equal direction.

### Q10–13: inverse shear by square-zero cancellation

\[
S=\begin{pmatrix}1&n\\0&1\end{pmatrix}=I+N,\quad N^2=0,\qquad S^{-1}=I-N=\begin{pmatrix}1&-n\\0&1\end{pmatrix}.
\]

Both orders of multiplication give I. The upper-right result is −5 or −8. Entrywise reciprocation would propose 1/n and does not cancel the shear; copying n would double the upper-right entry; setting it to zero leaves the shear unchanged. The determinant is 1 for every real n, including zero. The reciprocal distractor is undefined at zero even though S remains perfectly invertible. For general nilpotent N with N^r=0, the finite geometric inverse is \(I-N+N^2-\cdots+(-1)^{r-1}N^{r-1}\), proved by multiplying and canceling adjacent powers.

### Q14–17: trace sees fixed coordinates

For diagonal D, \((DP)_{ii}=D_{ii}P_{ii}\). A permutation matrix has Pii=1 exactly at a fixed coordinate, otherwise zero. Therefore trace(DP) is the sum of diagonal weights on the permutation's fixed coordinates. A single nontrivial n-cycle has none, so the answer is zero for n≥2. At n=1 its only permutation is identity and trace(DP)=1, violating the premise of a no-fixed-coordinate shift. The sum n(n+1)/2 is trace D, not trace DP; n and n² have no appropriate coordinate-sum derivation.

The cyclic identity follows from \(\operatorname{tr}(AB)=\sum_i\sum_jA_{ij}B_{ji}=\operatorname{tr}(BA)\), including conformable rectangular factors. Trace is not multiplicative: taking A=B=I2 gives trace(AB)=2 but trace(A)trace(B)=4. For three or more factors the permitted operation is cyclic rotation, not arbitrary factor permutation. General permutations with fixed coordinates produce a nonzero weighted sum, so merely saying permutation does not suffice.

### Q18–21: determinant versus trace under scaling

The product of 2I and 3I is 6I. Its determinant is the product of n diagonal entries, \(6^n\): 7776 or 1679616. The addition distractors are 275 or 6817; the trace distractors 6n give 30 or 48; the final distractor 3^n omits one factor. Multilinearity in rows gives \(\det(cA)=c^n\det A\), while trace scales by c. Multiplicativity \(\det(AB)=\det A\det B\) does not require AB=BA. Determinants are not generally additive: det(I2+I2)=4, whereas det(I2)+det(I2)=2. In dimension one some wrong general formulas may accidentally coincide with the correct result; the stated exact instances avoid those coincidences.

### Q22–25, Q40, Q46: nilpotent paths and matrix powers

For N with N12=N23=1, N² has only entry (1,3)=1 and N³=0. Thus

\[
(I+N)^k=\begin{pmatrix}1&k&\binom k2\\0&1&k\\0&0&1\end{pmatrix}
\]

for nonnegative integer k, using binomial coefficients with out-of-range terms zero. The second-superdiagonal results are 10 at 5, 28 at 8, 21 at 7 and 45 at 10. The exponent counts k possible first-superdiagonal steps, while the (1,3) term requires two distinct time slots in increasing order, hence choose(k,2). Choosing slots with replacement would give k²; allowing equal ordered endpoints in a cumulative sum would give choose(k+1,2). Neither applies because one factor can contribute only one N step. The recurrence t(k+1)=t(k)+k with t(0)=0 independently gives the same coefficient. At k=0 and 1 it is zero; at 2 it is one.

The binomial grouping is valid because I and N commute. A counterexample for arbitrary matrices uses A=diag(1,0), B=E12: AB=B but BA=0, and (A+B)² differs from A²+2AB+B² by −B. Nilpotent means some power vanishes, not that N itself vanishes. The same finite polynomial holds for integer negative k with the generalized falling-factorial coefficient k(k−1)/2, because the inverse is I−N+N²; this is not ordinary combinatorial choose notation at negative k unless explicitly defined.

### Q26–29: the product rank requires a composition argument

V maps Rn onto R2 and U maps R2 injectively into Rn. Therefore image(UV)=U(image V)=U(R2), dimension two. Equivalently kernel(UV)=kernel V, so rank-nullity gives 2. An upper bound rank(UV)≤min(rank U,rank V) alone does not prove equality. The generic smaller-rank equality fails for diag(1,0) times diag(0,1): both factors have rank one and the product is zero.

At n=2 both factors are invertible square maps and UV is invertible. At n>2, nullity is n−2 and determinant zero. The reverse product VU is a different map and need not have rank two. For n≥4, choose U to embed the first two coordinate axes, and V to extract the third and fourth coordinates. Both factor ranks are two; UV has rank two and square zero, whereas VU=0. Thus a product of maximum-rank rectangular factors can be nilpotent and has no automatic inverse. This example was checked at n=5 and 8.

### Q30–33 and Q39: similarity by actual coordinate columns

Let \(B=\begin{pmatrix}1&1\\1&-1\end{pmatrix}\). Its inverse is B/2. For T=diag(2,n),

\[
[T]_B=B^{-1}TB=\frac12\begin{pmatrix}n+2&2-n\\2-n&n+2\end{pmatrix}.
\]

The requested first-row second-column entry is (2−n)/2, giving −3/2 and −3. It is the first basis coordinate of T(b2)=(2,−n). The distractor (2+n)/2 is the diagonal entry, 2−n omits the conversion factor, and n−2 reverses the sign and omits the factor. At n=2, the off-diagonal coefficient becomes zero because T=2I, invariant under every basis change. Similarity preserves trace 2+n, determinant 2n and eigenvalues, but not arbitrary individual entries.

For Q39, the old standard matrix is \(\begin{pmatrix}2&1\\1&0\end{pmatrix}\). The images are (3,1) and (1,1); solving (c1+c2,c1−c2) for each gives coordinate columns (2,1) and (1,0). The new matrix here happens to equal the old matrix, but this is a specific algebraic coincidence, not basis independence of entries. The actual coordinate conversion B inverse times T times B verifies it. Option 2 uses the unconverted standard-coordinate images.

### Q34–37, Q45, Q47: block structure

For \(M=\begin{pmatrix}I_n&C\\0&2I_n\end{pmatrix}\), the determinant is 2^n. Block elimination can verify it: multiply on the right by \(\begin{pmatrix}I_n&-C\\0&I_n\end{pmatrix}\), whose determinant is one, to obtain diag(In,2In). The inverse is \(\begin{pmatrix}I_n&-C/2\\0&I_n/2\end{pmatrix}\), verified in both orders. C can be zero, singular or nonsingular. The values 1, 2n and 4^n respectively ignore the second block, confuse determinant with a scalar count, or incorrectly assign a factor 2 to all 2n rows.

Adding a lower-left block destroys the automatic rule: at scalar block size one, \(\begin{pmatrix}1&1\\1&2\end{pmatrix}\) has determinant 1, not 2. For identity diagonal blocks and arbitrary conformable C, the inverse upper-right block is −C. If identity block sizes are p and q, C is p×q and need not even have an ordinary inverse. Multiplying \(\begin{pmatrix}I_p&C\\0&I_q\end{pmatrix}\) by \(\begin{pmatrix}I_p&-C\\0&I_q\end{pmatrix}\) gives identity in both orders. The two integrated questions Q45 and Q47 are duplicate mechanisms; useful extensions should differ, e.g. unequal block sizes for one and nonidentity invertible diagonals for the other, without pretending the existing statements are wrong.

### Q41: inverse order and explicit option rejection

Invert a product by reversing factors: \((ABA^{-1})^{-1}=AB^{-1}A^{-1}\). Both products simplify using adjacent inverse pairs. For a concrete audit, choose

\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad B=\begin{pmatrix}2&0\\0&3\end{pmatrix},\quad ABA^{-1}=\begin{pmatrix}2&1\\0&3\end{pmatrix}.
\]

The correct inverse has upper-right entry −1/6. The other three expressions in the existing option order have respectively +1/6, −5/6 and +5/6, so none cancels the original. In special commuting or identity-factor examples wrong expressions can coincide; they are rejected as formulas for arbitrary invertible factors, not as impossible numerical matrices under every choice.

### Q42: Gram kernels

The inclusion kernel A ⊆ kernel(AᵀA) follows directly. Conversely, AᵀAx=0 gives \(x^TA^TAx=\|Ax\|_2^2=0\), forcing Ax=0. Rank-nullity then gives rank(AᵀA)=rank A, not universally m. Invertibility of AᵀA is equivalent to full column rank; A=0 is an immediate counterexample to unconditional invertibility. AAᵀ and AᵀA have different shapes when m≠n. Even for square A they can differ: A=[[1,1],[0,0]] gives AAᵀ=diag(2,0) and AᵀA=[[1,1],[1,1]]. Over complex matrices use A*, not Aᵀ: the complex column (1,i) has AᵀA=0 while A is injective, refuting the transpose-based kernel identity outside its real hypothesis.

### Q44: rectangular trace versus determinant

For A of shape 2×3 and B of shape 3×2,

\[
\operatorname{tr}(AB)=\sum_{i=1}^2\sum_{j=1}^3A_{ij}B_{ji}=\operatorname{tr}(BA).
\]

Both products are square, but their sizes differ. Set A=[I2 0] and B to its transpose: AB=I2 while BA=diag(1,1,0). Their traces both equal 2, whereas determinants are 1 and 0. Product equality is not a well-typed matrix assertion because the dimensions differ. This exact example rejects three distractors simultaneously without relying on vague language about commutation.

## 5. Actual symbolic and numeric corroboration

SymPy computations independently verified:

- N², N³ and (1,3) entries of powers at k=0,1,2,5,7,8,10.
- det(I+J)=3,6,9 at sizes 2,5,8 and the exact inverse I−J/(n+1).
- The nontriangular Q9 counterexample has determinant 2 and diagonal product 2.
- The symbolic basis-conjugation matrix for diag(2,n), and the Q39 coordinate-column matrix.
- The four Q41 candidate matrices, with exactly option 1 multiplying to identity in the explicit noncommuting example.
- The Q44 rectangular products, traces and unequal determinants.
- Exact 6^5, 6^8 and additive determinant distractors.
- Rank-two square-zero UV and zero VU at n=5 and n=8.
- Q113 independent counts 21 and 16; unrestricted binomial 10626; additive/multiplicative unrestricted distractors 10647 and 223146.

These checks corroborate the audited models. They do not validate course completeness, visual appearance, browser controls, student mastery, or an unseen-question guarantee.

## 6. Dedicated visual proposals by mathematical mechanism

1. **Symmetric constraint grid:** link mirrored cells so they share one variable; separately remove one diagonal degree of freedom using trace. Q38 adds the independent (1,2) zero constraint. Include the rank of the constraint map, not simply the number of marked cells.
2. **Coupled integer equations:** show the triangular lattice of 21 first-group points and line of 16 second-group points, then the Cartesian-product count. Label this as discrete counting and contrast it with the real affine dimension three.
3. **All-ones rank-one map:** project a vector onto its all-equal and sum-zero components, show J annihilating the latter and multiplying the former by n. Adding identity then supplies the actual n+1 versus 1 scalings. A compact matrix/eigenspace ledger is appropriate for n=5,8, rather than a false literal 3D drawing of an n-dimensional space.
4. **Shear and inverse:** transform a unit grid by (x,y)→(x+ny,y), then apply the inverse shear. Preserve signed area one; show the actual product cancellation. Do not merely change matrix-cell colors.
5. **Permutation trace:** route each coordinate to its cyclic destination and highlight diagonal positions only at fixed coordinates. Display the weighted fixed-point sum. Turning a no-fixed shift into a permutation with a fixed point must update the trace.
6. **Scalar determinant scaling:** show one dimension representative with lengths scaled by 2 then 3 and the dimension-dependent volume factor 6^n in a ledger. Label area/volume examples as examples, not literal drawings of n=8-dimensional volume.
7. **Nilpotent power paths:** show three coordinates with arrows 3→2→1 under N and hold arrows under I. Two distinct ordered time slots produce the 1←2←3 contribution. A cumulative exact counter adds k to choose(k,2) at each power. The endpoint (1,3) coefficient must change with time, not just the current highlighted cell.
8. **Full-rank rectangular composition:** show Rn→R2→Rn with the first map onto and the second injective. Add a separate counterexample checkpoint with both factors maximum rank but VU=0, distinguishing UV from VU. Display domain dimensions and kernel dimensions.
9. **Basis-conjugation diagram:** show basis coordinates→standard coordinates→linear transformation→new basis coordinates. The second basis vector's image should reconstruct from the new-basis matrix column. Trace/determinant stay fixed while entries change.
10. **Block triangular map:** draw (x,y)→(x+Cy,2y), then apply the exact inverse. The upper coupling changes the shape, but diagonal-block volume factors remain fixed. In the identity-diagonal case show −C cancellation with unequal p,q blocks to make the absence of C inverse clear.
11. **Inverse-order chain:** display the three actual transformation stages and their inverse stages in reverse order. Adjacent cancellation markers must connect the correct factors; the four candidate products can be checked in a numeric table.
12. **Gram kernel:** show Ax and the nonnegative squared-norm identity; kernel-input motion leaves both Ax and AᵀAx zero. Include an explicit full-column-rank versus deficient-rank switch; real transpose and complex adjoint should never share an unlabeled formula.
13. **Rectangular trace pairing:** display the six Aij*Bji terms in a 2×3 grid, then regroup the same six values by columns to show both traces. Pair with AB=I2 and BA=diag(1,1,0) so differing shapes and determinants are visible.
14. **Structured definiteness:** vary a while displaying the all-equal coefficient and sum-zero coefficient. At an endpoint show the actual null direction; outside the valid interval show a negative quadratic direction. Distinguish determinant sign from definiteness.

## 7. Handoff and limits

The authentic option-37 correction, authored Q9 rule wording and Q33 same-basis qualification should be resolved before publishing the rewritten bank. Q4's ambiguity must remain. All other listed exact and symbolic answers agree with independent derivation. Remaining full-chapter work includes course reconciliation, deep lesson writing, individual explanatory answers, appropriate simulations, mathematical notation audit and browser/print/mobile inspection. This report alone does not complete those tasks.
