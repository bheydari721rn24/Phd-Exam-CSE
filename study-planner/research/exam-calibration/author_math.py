"""Original counting/probability and linear algebra examination analogues."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parent
questions=[]
def q(topic,title,stem,options,answer,solution,pattern,difficulty='Medium'):
 questions.append(dict(topic=topic,title=title,stem=stem,options=options,answer=answer,solution=solution,pattern=pattern,difficulty=difficulty,kind='Original examination analogue'))

q('s_axioms','Feasibility of a three-event table',r'$P(A)=0.6$, $P(B)=0.5$, $P(C)=0.4$; the pair intersections are 0.3, 0.2, and 0.1 respectively. Which range of $t=P(A\cap B\cap C)$ is feasible?', [r'$0\le t\le0.1$',r'$0\le t\le0.2$',r'$0.1\le t\le0.3$',r'$t=0.1$ only.'],1,r'''The pair-only cells are $0.3-t,0.2-t,0.1-t$, so $0\le t\le0.1$. The single-only cells are $0.1+t,0.1+t,0.1+t$, all nonnegative in that interval.

The union is $0.6+0.5+0.4-0.3-0.2-0.1+t=0.9+t$, so the outside cell is $0.1-t$, providing the same upper bound. These eight nonnegative cells sum to one, proving every point of the stated range is attainable. Marginal bounds alone would miss a negative atom.''','Phd_CS_1405_Q21','Hard')
q('s_axioms','Two events: exactly one and independence',r'$P(A)=0.4$, $P(B)=0.5$, and $P(A\cup B)=0.7$. Find the probability of exactly one event and decide whether $A,B$ are independent.', ['0.5 and independent.','0.7 and independent.','0.5 and dependent.','0.3 and dependent.'],1,r'''Inclusion-exclusion gives $P(A\cap B)=0.4+0.5-0.7=0.2$. Exactly one has probability $0.4+0.5-2\cdot0.2=0.5$.

The intersection equals the product $0.4\cdot0.5$, so the two events are independent. The union is not the exactly-one event because it includes both; independence does not mean disjointness. These distinctions must be checked separately.''','Phd_CS_1405_Q21; Phd_CS_1404_Q68')
q('s_axioms','Conditional sampling in the correct sample space',r'A five-ball urn has three red and two blue balls. Draw two without replacement. Given that at least one is red, what is the probability both are red?', ['3/10','1/3','3/5','1/2'],2,r'''Among $\binom52=10$ equally likely pairs, three are red-red and one is blue-blue. Conditioning on at least one red removes only the blue-blue pair, leaving nine pairs.

The desired ratio is $3/9=1/3$. Three tenths is the unconditional probability; three fifths is a one-draw proportion. Conditioning restricts and renormalizes the outcome set rather than simply deleting a term from the numerator.''','Phd_CS_1404_Q69; Phd_CS_1404_Q70')
q('s_axioms','Pairwise is not mutual independence',r'Two fair independent bits $X,Y$ determine events $A=\{X=1\}$, $B=\{Y=1\}$, and $C=\{X\oplus Y=1\}$. Which statement is correct?',['All three events are mutually independent.','Every pair is independent, but the triple is not.','No pair is independent.','Only A and B are independent.'],2,r'''Each event has probability one half. Each pair intersection has probability one quarter, verified from the four equally likely bit pairs, so every pair is independent.

The triple intersection is empty: when both bits are one, their XOR is zero. Its probability is zero rather than the product one eighth. Mutual independence includes all subset products, not just pairwise checks. The full table gives a finite counterexample to the stronger implication.''','Phd_CS_1404_Q68; MS_CS_1405_Q99','Hard')
q('s_axioms','Nonuniform elementary outcomes',r'Toss a fair coin three times. Record only the number of heads $K$. What is $P(K\ge2)$, and are the four possible values of $K$ equally likely?', ['1/2 and no.','1/2 and yes.','2/3 and no.','3/4 and yes.'],1,r'''There are eight equally likely ordered toss sequences. Head counts 0,1,2,3 occur in 1,3,3,1 sequences respectively. Thus $P(K\ge2)=(3+1)/8=1/2$.

The recorded values are not uniform, although the underlying ordered sequences are. Counting two acceptable recorded values out of four accidentally gives the right probability here, but the method is invalid and fails for other events. The second part detects that conceptual error.''','Phd_CS_1404_Q70; Phd_CS_1404_Q68')
q('s_axioms','A normalized infinite law and a tail',r'$P(N=k)=c/3^k$ for $k=1,2,\ldots$. Find $c$ and $P(N\ge4)$.',['2 and 1/27.','1 and 1/81.','2 and 1/81.','3 and 1/27.'],1,r'''The geometric series $\sum_{k\ge1}3^{-k}=1/2$ forces $c=2$. The tail from four sums to $2\cdot3^{-4}/(1-1/3)=1/27$.

Keeping only the first tail mass gives $2/81$, not the full tail; using the wrong starting index changes normalization. Infinite discrete laws must first have total mass one, and an at-least event includes every later outcome.''','Phd_CS_1404_Q69')
q('s_axioms','A collision bound and an exact calculation',r'Draw three independent uniform labels from a four-element set. What is the probability of a repeated label, and what does a union bound over the three pair-equality events give?', ['5/8 and at most 3/4.','3/4 and exactly 3/4.','5/8 and at most 1/4.','3/8 and at most 3/4.'],1,r'''There are $4^3$ ordered draws. The all-distinct count is $4\cdot3\cdot2=24$, so repetition has probability $1-24/64=5/8$.

Each of the three pair-equality events has probability one quarter, so their union is bounded above by three quarters. The events overlap when all three labels agree, making the bound loose. Three eighths is the complement probability, and the union bound is an inequality rather than an independence formula.''','Phd_CS_1404_Q67; Phd_CS_1404_Q68')
q('s_axioms','Expectation without indicator independence',r'In a uniformly random permutation of five distinct values, how many running-minimum updates are expected with initial minimum infinity?', ['5/2','137/60','2','5'],2,r'''Position $i$ is the smallest in its prefix with probability $1/i$. By linearity of expectation the expected update count is $1+1/2+1/3+1/4+1/5=137/60$.

No independence assumption about the update indicators is needed. Five is the number of tested elements, not the mean number of successful updates. A logarithm gives a growth approximation rather than this exact finite answer.''','Phd_CS_1404_Q72','Hard')

q('s_counting','Integer solutions with parity and two bounds',r'Count nonnegative integer solutions of $a+b+c=18$ with $a$ even, $b\le3$, and $c\ge2$.',['32','33','34','36'],1,r'''Set $a=2j$ and $c=c'+2$. Then $2j+b+c'=16$. For $b=0,1,2,3$, the numbers of allowed $j$ are 9,8,8,7, respectively.

Each determines exactly one $c'$, so add to obtain 32. The even endpoint at sixteen makes the four cases unequal. Ordinary stars and bars ignores parity and the upper bound; dividing an unrestricted count by two is unjustified at a finite boundary.''','MS_CS_1405_Q129','Hard')
q('s_counting','An onto map with a fiber lower bound',r'Count surjections from a five-element labeled set to three labeled outputs when the first output has at least two preimages.',['90','100','120','150'],1,r'''If its fiber size is two, choose that fiber in $\binom52=10$ ways and map the remaining three inputs onto the other two outputs in $2^3-2=6$ ways, giving sixty.

If its fiber size is three, choose it in ten ways; the remaining two inputs must use the other two outputs bijectively, giving twenty. If its fiber size is four or five, surjectivity fails. The total is eighty, so the authored options are corrected below to reflect this calculation.''','MS_CS_1405_Q124','Hard')
questions[-1]['options']=['80','100','120','150']
questions[-1]['solution']=r'''The distinguished fiber has size two or three; larger sizes leave too few inputs to hit both remaining outputs. At size two, choose the fiber in ten ways and use one of six onto maps from the remaining three inputs to two outputs, giving sixty.

At size three, choose the fiber in ten ways and biject the other two inputs in two ways, giving twenty. The total is eighty. One hundred includes a missing-output case; 150 counts every surjection without the fiber restriction. Fiber-size cases are disjoint, so their counts must be added.'''
q('s_counting','Parity-filtered strings with no fixed composition',r'How many length-five strings over $\{0,1,2\}$ have an even number of zeros?', ['121','122','123','81'],2,r'''The even zero counts are zero, two, and four, giving $2^5+\binom52 2^3+\binom54 2=32+80+10=122$.

Equivalently the parity filter is $(3^5+1^5)/2$. The total 243 is odd, so the parity classes cannot have exactly equal sizes. One hundred twenty-one is the odd-zero class; eighty-one counts a different fixed-length unrestricted alphabet.''','MS_CS_1405_Q123')
q('s_counting','Equal unlabeled groups with distinct objects',r'Partition eight distinct students into four unlabeled pairs. How many partitions are there?', ['105','210','2520','1680'],1,r'''Temporarily order the eight students and group consecutive positions into pairs. Each partition appears $2^4$ times from internal pair orders and $4!$ times from pair order.

Divide to get $8!/(2^4 4!)=105$. These symmetry factors are justified because all objects are distinct and each pair has exactly two members. The larger options leave some group or internal ordering labeled.''','MS_CS_1405_Q120')
q('s_counting','A weighted binomial coefficient identity',r'Compute $\sum_{k=3}^{9}\binom9k\binom k3$.',['5376','2688','84','10752'],1,r'''Choose the three marked members first in $\binom93=84$ ways, then independently choose any subset of the other six in $2^6=64$ ways.

The product is 5376. This double count equals the displayed sum, in which total subset size is chosen first. Eighty-four omits optional members; halving or doubling inserts an absent restriction. A bijection or two-order count explains why the formula applies.''','MS_CS_1405_Q121','Hard')
q('s_counting','Selections with two category constraints',r'Ten questions consist of five algebra and five programming questions. Select six, with at least three algebra and at least two programming. How many selections?', ['150','175','200','210'],2,r'''The possible algebra counts are three or four; five would leave only one programming question. Thus count $\binom53\binom53+\binom54\binom52=100+50=150$.

The correct option is therefore 150; the initial answer index is corrected below. Two simultaneous lower bounds restrict the case range. The unrestricted count $\binom{10}6=210$ includes forbidden category balances.''','MS_CS_1405_Q115')
questions[-1]['answer']=1
q('s_counting','Equal head counts by Vandermonde',r'Two independent fair-coin experiments have eight and five tosses. What is the probability of equal head counts?', [r'$\binom{13}{5}/2^{13}$',r'$\binom{13}{8}/2^8$',r'$\binom85/2^{13}$',r'$1/2$'],1,r'''Sum over the common head count: $2^{-13}\sum_{k=0}^5\binom8k\binom5k$. Replace the second coefficient by $\binom5{5-k}$; Vandermonde gives $\binom{13}5$.

All thirteen tosses contribute to the denominator. The combination $\binom85$ omits possible successes in the second experiment. Complementing the second experiment's heads gives an equivalent single-binomial event, but does not imply probability one half.''','Phd_CS_1404_Q70','Hard')
q('s_counting','Weakly increasing maps with a required used value',r'Count weakly increasing length-four sequences from $\{1,2,3\}$ that use value 2 at least once.',['5','8','10','15'],3,r'''All weakly increasing sequences number $\binom{4+3-1}{3-1}=15$. Those avoiding value two are weakly increasing sequences over two values, numbering $\binom51=5$.

Subtract to get ten. This uses the multiplicity encoding and complement counting. Avoidance does not require deleting sequence positions; it removes one available value. The final option ignores the use requirement.''','MS_CS_1405_Q122')

q('l_vectors','Projection onto a nonorthogonal span',r'Let $u=(1,0,1)$, $v=(1,1,0)$, and $w=(1,2,3)$. What is the orthogonal projection of $w$ onto their span?', ['(7/3,2/3,5/3).','(1,2,3).','(4,3,4).','(2,1,1).'],1,r'''Write the projection as $au+bv$. Orthogonality of the residual to both basis vectors gives $2a+b=4$ and $a+2b=3$.

Solving gives $a=5/3,b=2/3$, hence projected vector $(7/3,2/3,5/3)$. The original vector is not in the span; independently projecting onto two nonorthogonal vectors and adding ignores their interaction. The Gram system accounts for the nonzero dot product between $u$ and $v$.''','Phd_CS_1404_Q31','Hard')
q('l_vectors','Distance to a plane with a scaled normal',r'Find the distance of $(1,2,3)$ from plane $2x-y+2z=4$.',['1','2','3','1/3'],1,r'''Evaluate the plane residual: $2-2+6-4=2$. The normal has norm three, so the distance is $2/3$, not one. The correct option is corrected below.

The projection correction is residual divided by squared normal norm times the normal. A raw residual is not a Euclidean distance unless the normal is a unit vector.''','Phd_CS_1404_Q31')
questions[-1]['options']=['2/3','2','3','1/3']
questions[-1]['solution']=r'''The residual in the plane equation is $2\cdot1-2+2\cdot3-4=2$. Divide its absolute value by the normal length $\sqrt{2^2+(-1)^2+2^2}=3$, giving $2/3$.

Subtracting $(2/9)(2,-1,2)$ gives a point on the plane and a correction of length $2/3$, checking the formula. The distractors use the unnormalized residual, the normal length alone, or an extra division.'''
q('l_vectors','Parameter-dependent independence',r'Vectors $(1,1,0)$, $(1,0,1)$, and $(0,1,a)$ in $\mathbb R^3$ are independent exactly when which condition holds?', [r'$a\ne1$',r'$a\ne-1$',r'$a>0$',r'$a\ne0$'],2,r'''For coefficients $r,s,t$ in a zero linear combination, the coordinates give $r+s=0$, $r+t=0$, and $s+at=0$. Substituting $s=t=-r$ gives $-(1+a)r=0$.

Only the zero combination is possible when $a\ne-1$. At $a=-1$, choose $r=1,s=t=-1$ to exhibit dependence. Positivity is unnecessary, and zero itself is a valid independent parameter. Solving the coefficient equations also supplies the exceptional witness.''','MS_CS_1405_Q41; Phd_CS_1404_Q32')
q('l_vectors','An affine minimum norm problem',r'Among real vectors $(x,y,z)$ satisfying $x+y+z=6$, what is the minimum squared Euclidean norm and where is it attained?', ['12 at (2,2,2).','36 at (6,0,0).','6 at (1,2,3).','0 at (0,0,0).'],1,r'''Cauchy–Schwarz gives $(x+y+z)^2\le3(x^2+y^2+z^2)$, so the squared norm is at least twelve.

Equality holds precisely when the vector is proportional to $(1,1,1)$; the constraint fixes the proportionality at two. The point $(6,0,0)$ is feasible but not minimal, while the zero vector is infeasible. An optimization answer must include a lower bound and a feasible attaining vector.''','Phd_CS_1404_Q31; Phd_CS_1404_Q32','Hard')
q('l_vectors','Coordinates are not dot products in a general basis',r'In the basis $b_1=(1,1)$, $b_2=(1,-1)$, find coordinates of $(3,1)$ and its squared Euclidean norm.', ['(2,1) and 10.','(4,2) and 20.','(2,1) and 5.','(3,1) and 10.'],1,r'''Solve $c_1+c_2=3$ and $c_1-c_2=1$, obtaining $(c_1,c_2)=(2,1)$. The actual vector norm squared is $3^2+1^2=10$.

The basis is orthogonal but not normalized; its squared basis lengths are two, so the coordinate norm uses Gram matrix $2I$. The sum $2^2+1^2=5$ would be valid only in an orthonormal basis. Coordinate labels depend on the ordered basis.''','MS_CS_1405_Q41; Phd_CS_1404_Q31')
q('l_vectors','A complex inner product uses conjugation',r'Using $\langle u,v\rangle=\sum\overline{u_i}v_i$, let $u=(1,i)$ and $v=(i,1)$. Find $\langle u,v\rangle$ and $\Vert u\Vert^2$.',['0 and 2.','2i and 0.','2i and 2.','0 and 0.'],1,r'''Conjugate the first vector: $\langle u,v\rangle=1\cdot i+(-i)\cdot1=0$. Its squared norm is $1\cdot1+(-i)i=2$.

Without conjugation the apparent self-dot-product would be zero for a nonzero vector, violating positive definiteness. The convention is explicitly supplied because some texts conjugate the second argument instead; norm positivity and orthogonality remain consistent.''','Phd_CS_1404_Q31; Phd_CS_1404_Q32')
q('l_vectors','Equality versus inequality in a projection',r'$P$ is orthogonal projection onto a plane through zero in $\mathbb R^3$. For a nonzero $x$ perpendicular to that plane, what is $\Vert x-Px\Vert/\Vert x\Vert$?', ['0','1/2','1','It depends on the plane.'],3,r'''Orthogonal projection of a perpendicular vector is zero. Thus $x-Px=x$ and the ratio is one.

Nonzero is required so division by its norm is defined. The result expresses the full residual rather than the projected fraction. If $x$ belonged to the plane, the ratio would be zero, showing why the domain condition changes the answer.''','Phd_CS_1404_Q31')
q('l_vectors','Gram geometry and dependence',r'Two real vectors have squared lengths 9 and 16 and dot product 12. Which conclusion follows?', ['They are independent.','They are perpendicular.','They are dependent and point in the same direction.','Their sum has squared length 25.'],3,r'''Their Gram determinant is $9\cdot16-12^2=0$. Equality in Cauchy–Schwarz implies dependence, and the positive dot product gives the same direction.

Their lengths are three and four, so one is a positive $4/3$ multiple of the other. The squared norm of their sum is $9+16+2\cdot12=49$, not twenty-five. Zero Gram determinant is a dependency test; positive individual norms alone do not establish independence.''','Phd_CS_1404_Q31; Phd_CS_1404_Q32')

q('l_matrices','Dimension with a second independent constraint',r'Real symmetric $5\times5$ matrices have trace zero and entry $(1,2)$ equal to zero. What is the dimension of this space?', ['15','14','13','12'],3,r'''A symmetric matrix has fifteen independent coordinates. Trace is one nonzero linear constraint on diagonal coordinates. The $(1,2)$ constraint is a separate nonzero constraint on an off-diagonal coordinate.

Their constraint functionals are independent, so dimension is $15-2=13$. Symmetry already determines entry $(2,1)$ from $(1,2)$; setting both to zero does not impose two additional independent conditions. Count independent equations, not repeated written entries.''','MS_CS_1405_Q41')
q('l_matrices','A basis change by coordinate columns',r'$T(x,y)=(2x+y,x)$. In ordered basis $b_1=(1,1),b_2=(1,-1)$, what are the columns of its matrix?', ['(2,1) and (0,1).','(3,1) and (1,1).','(2,0) and (1,1).','(2,1) and (1,0).'],4,r'''The basis images are $T(b_1)=(3,1)$ and $T(b_2)=(1,1)$. Coordinates in the specified basis solve $(a+b,a-b)$ equal to each image.

The first image has coordinates $(2,1)$; the second has coordinates $(1,0)$. These become matrix columns, not rows. The second option uses standard-coordinate images without converting; the other options swap or alter coordinate roles.''','MS_CS_1405_Q41; Phd_CS_1404_Q31','Hard')
q('l_matrices','A triangular nilpotent power',r'Let $N$ be a $3\times3$ matrix with ones at positions $(1,2),(2,3)$ and zeros elsewhere. What is entry $(1,3)$ of $(I+N)^7$?', ['7','14','21','49'],3,r'''Here $N^2$ has one at $(1,3)$ and $N^3=0$. Expand the commuting binomial: $(I+N)^7=I+7N+\binom72N^2$.

Only the squared term contributes to entry $(1,3)$, giving twenty-one. A scalar geometric shortcut would miss the nilpotent structure. The binomial is valid because the identity commutes with $N$, not because arbitrary matrix factors commute.''','MS_CS_1405_Q41; Phd_CS_1404_Q30')
q('l_matrices','An inverse-product order trap',r'$A,B$ are invertible square matrices. Which expression is the inverse of $ABA^{-1}$?', [r'$AB^{-1}A^{-1}$',r'$A^{-1}B^{-1}A$',r'$A^{-1}B^{-1}A^{-1}$',r'$AB^{-1}A$'],1,r'''Reverse the three factors and invert each: $(A^{-1})^{-1}B^{-1}A^{-1}=AB^{-1}A^{-1}$.

Multiplying by the original on either side cancels the adjacent $A^{-1}A$ and $BB^{-1}$ pairs to the identity. The other alternatives do not have those cancellation pairs for general noncommuting matrices. A scalar-inspired rearrangement is not permitted without a commutativity hypothesis.''','Phd_CS_1404_Q30')
q('l_matrices','A Gram matrix and a nullspace',r'$A$ is a real $m\times n$ matrix. Which statement is always correct?', [r'$\ker(A^TA)=\ker A$',r'$A^TA$ is always invertible.',r'$\operatorname{rank}(A^TA)=m$',r'$AA^T=A^TA$'],1,r'''If $Ax=0$, then $A^TAx=0$. Conversely, if $A^TAx=0$, take the quadratic form to obtain $x^TA^TAx=\Vert Ax\Vert^2=0$, hence $Ax=0$.

Invertibility requires full column rank and was not assumed. The rank equals that of $A$, not always $m$. The two Gram products can even have different dimensions. The nonnegative squared norm is the decisive identity.''','Phd_CS_1404_Q30; Phd_CS_1404_Q31')
q('l_matrices','A structured positive-definiteness interval',r'A symmetric $4\times4$ matrix has diagonal entries 1 and off-diagonal entries $a$. What is the positive-definiteness range?', [r'$-1<a<1$',r'$-1/3<a<1$',r'$0<a<1$',r'$-1/4<a<1/4$'],2,r'''The matrix is $(1-a)I+aJ$, where $J$ is all ones. On the three-dimensional sum-zero subspace the coefficient is $1-a$; on the all-equal line it is $1+3a$.

Both must be positive, giving $-1/3<a<1$. The perpendicular decomposition proves sufficiency as well as necessity. At either endpoint a nonzero vector has zero quadratic form, so endpoints are excluded. Positivity of entries is not the criterion for positive definiteness.''','Phd_CS_1404_Q32','Hard')
q('l_matrices','Trace of rectangular products',r'$A$ has shape $2\times3$ and $B$ shape $3\times2$. Which statement is always correct?', [r'$AB=BA$',r'$\operatorname{tr}(AB)=\operatorname{tr}(BA)$',r'$\det(AB)=\det(BA)$',r'$AB$ and $BA$ have identical dimensions.'],2,r'''Expand the first trace as $\sum_{i=1}^2\sum_{j=1}^3 A_{ij}B_{ji}$. Reversing the finite sums gives the trace of $BA$.

The products have shapes two-by-two and three-by-three, so equality as matrices is not even typed. Determinant equality fails, for example when $AB=I_2$ but $BA$ has rank at most two and zero determinant. Trace cycling needs compatible factors, not identical product shapes.''','MS_CS_1405_Q41; Phd_CS_1404_Q30')
q('l_matrices','Block triangular inverse by equations',r'A block matrix has diagonal identity blocks and upper-right block $C$, with lower-left block zero. Which upper-right block appears in its inverse?', ['$C$','$-C$','$C^{-1}$','Zero.'],2,r'''Write the candidate inverse with upper-right block $D$. Multiplying the two block matrices produces upper-right block $C+D$, which must be zero, so $D=-C$.

No invertibility of $C$ is required; it may be rectangular as long as block dimensions conform. The whole matrix is invertible because its diagonal blocks are identities. Treating an off-diagonal block as an independent diagonal inverse gives the wrong answer.''','Phd_CS_1404_Q30; MS_CS_1405_Q41')

(BASE/'original-math.json').write_text(json.dumps(questions,indent=2)+'\n')
print('Authored',len(questions),'original math questions.')
