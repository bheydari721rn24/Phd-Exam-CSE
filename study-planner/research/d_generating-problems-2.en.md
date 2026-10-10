### 25. A reconstructed forcing pattern from CMU

For $a_0=a_1=1$ and $a_n=a_{n-1}+2a_{n-2}+(-1)^n$ for $n\ge2$, derive the complete OGF and exact sequence. This is a reconstructed algebraic pattern from the CMU handout.

#### Solution

Sum only from two. The forcing series is $1/(1+x)-1+x=x^2/(1+x)$. Thus $A-1-x=x(A-1)+2x^2A+x^2/(1+x)$, so $A=(1+x+x^2)/((1+x)^2(1-2x))$. Partial fractions give $7/(9(1-2x))-1/(9(1+x))+1/(3(1+x)^2)$. Consequently $a_n=(7/9)2^n+(n/3+2/9)(-1)^n$. The first two values are one; at index two the answer is four, matching $1+2+1$. The repeated factor at minus one arises from a forcing exponential already present in the homogeneous recurrence. The index-dependent alternating term must survive unless canceled by the numerator.

### 26. A recurrence reconstructed from a written MIT exam pattern

Let $r_0=1$ and $r_n=5r_{n-1}+n+1$ for $n\ge1$. Find its OGF and its exact coefficients. This changes the parameters of MIT Chapter 15's forced-recurrence exercise pattern.

#### Solution

The forcing OGF beginning at one is $(1-x)^{-2}-1$. Therefore $(1-5x)R=1+(1-x)^{-2}-1=(1-x)^{-2}$, giving $R=1/((1-5x)(1-x)^2)$. Decompose it as $(25/16)/(1-5x)-(5/16)/(1-x)-(1/4)/(1-x)^2$. The coefficient is $(25\cdot5^n-4n-9)/16$. At zero it is one, and at one it is seven, matching $5+2$. The forcing starts at one, so its constant must be subtracted; this cancellation explains the particularly simple numerator. A direct first-order unrolling sums $(j+1)5^{n-j}$ and gives the same closed form.

### 27. A coupled system without guessing roots

Suppose $u_0=1$, $v_0=0$, and $u_n=u_{n-1}+v_{n-1}$, $v_n=2u_{n-1}$ for $n\ge1$. Derive $U$ and $V$ and find $u_n$.

#### Solution

The summed equations are $U-1=xU+xV$ and $V=2xU$. Substitute the second into the first to obtain $U=1/(1-x-2x^2)=1/((1-2x)(1+x))$. Thus $u_n=(2^{n+1}+(-1)^n)/3$ and $V=2x/((1-2x)(1+x))$. Its coefficient at positive $n$ is $2u_{n-1}$, while the constant is zero. Eliminating a state introduces a second-order recurrence for $u$, but the initial value $u_1=1$ must still be retained. The system derivation determines that value automatically and avoids choosing an unsupported second boundary.

### 28. A binomial recurrence best handled by an EGF

Let $f_0=1$ and $f_n=\sum_{k=0}^{n}\binom{n}{k}f_k/2^k$ for $n\ge1$. Prove $f_n=2^n$ and explain how to remove its apparent self-reference.

#### Solution

The term $k=n$ is $f_n/2^n$. For positive $n$, moving it to the left leaves a nonzero multiplier $1-2^{-n}$, so each value is uniquely determined by earlier values. If $f_k=2^k$ for all lower indices, the remaining sum is $2^n-1$; division by $1-2^{-n}$ gives $2^n$. Equivalently, the EGF equation is $F(x)=e^xF(x/2)$ with constant one. The candidate $e^{2x}$ satisfies it exactly. Coefficient uniqueness proves the candidate; there is no need to justify an infinite numerical iteration of substitutions. The equation at zero is redundant, so the separately supplied constant is essential.

### 29. A variable-coefficient recurrence producing a differential equation

Let $a_0=1$ and $a_{n+1}=(n+2)a_n$ for $n\ge0$. Find the formal OGF equation and an EGF that is simpler.

#### Solution

The sequence is $a_n=(n+1)!$ by induction. The left-shifted OGF satisfies $(A-1)/x=xA'+2A$, or $x^2A'+(2x-1)A+1=0$. Its radius of numerical convergence is zero. The EGF is $\widehat A=\sum(n+1)x^n=1/(1-x)^2$, which has positive convergence radius and the same unnormalized counts. Changing generating-function type changes the coefficient interpretation, not the sequence itself. A rational EGF does not imply a rational OGF. This example shows why choosing a representation before attempting algebra can greatly simplify a recurrence.

### 30. A delayed recurrence with one untouched prefix value

Let $a_0=7$, $a_1=2$, and $a_n=3a_{n-1}$ for $n\ge2$. Find the OGF and explain its finite correction.

#### Solution

The tail is $a_n=2\cdot3^{n-1}$ for positive $n$, so $A=7+2x/(1-3x)=(7-19x)/(1-3x)$. The numerator records the independent initial value seven, rather than forcing $a_1=3a_0$. Polynomial division gives $19/3+(2/3)/(1-3x)$. It gives constant seven and positive-index coefficients $(2/3)3^n$. Multiplying this decomposition by $1-3x$ recovers $7-19x$, independently checking the sign of both terms. Showing the finite correction explicitly explains why an eventual recurrence can leave a prefix outside its exponential tail formula.

### 31. Bounded identical units in distinguishable boxes

Count solutions of $x_1+x_2+x_3+x_4=9$ with every variable an integer from zero through three.

#### Solution

The OGF is $(1+x+x^2+x^3)^4=(1-x^4)^4/(1-x)^4$. Extract degree nine using inclusion-exclusion: $\binom{12}{3}-4\binom{8}{3}+6\binom{4}{3}=220-224+24=20$. Terms with three or four violated bounds have negative shifted targets and contribute zero under the combinatorial convention. Complementing every variable to $3-x_i$ changes total nine to total three. At total three no upper bound can be exceeded, so stars and bars gives $\binom{6}{3}=20$, an independent check. This symmetry is particularly useful when the target is near the total upper limit.

### 32. Unequal bounds require subset-dependent shifts

Count nonnegative solutions of $a+b+c=7$ with $a\le2$, $b\le3$, and $c\le4$.

#### Solution

The product is $(1-x^3)(1-x^4)(1-x^5)/(1-x)^3$. The unrestricted count is $\binom{9}{2}=36$. Single upper-bound violations subtract $\binom{6}{2}+\binom{5}{2}+\binom{4}{2}=15+10+6$. The pair of shifts three and four adds $\binom{2}{2}=1$; all other pairs exceed the target. Thus the count is six. Complementation to total maximum nine changes the target to two, where bounds are irrelevant, giving $\binom{4}{2}=6$. Treating the three unequal bounds as one common shift would lose the individual numerator exponents and produce the wrong inclusion-exclusion formula.

### 33. Lower bounds must be removed before upper-bound correction

Count integer solutions of $a+b+c=10$ with $1\le a\le4$, $2\le b\le5$, and $3\le c\le6$.

#### Solution

Subtract the lower bounds to define $a'=a-1$, $b'=b-2$, $c'=c-3$. Their total is four and each lies from zero through three. The OGF for the shifted variables is $(1-x^4)^3/(1-x)^3$. Degree four is $\binom{6}{2}-3\binom{2}{2}=15-3=12$. The original OGF carries an additional factor $x^6$, so extracting original degree ten gives the same shifted target four. The three excluded cases are exactly those with one shifted variable equal to four and the other two zero. Applying the original upper limits directly after shifting would accidentally enlarge the allowed intervals.

### 34. Congruence and a finite cap in the same model

Count solutions of $a+b+c=12$ with $a\ge0$ even, $b\ge1$ odd, and $0\le c\le3$.

#### Solution

The product is $x(1+x+x^2+x^3)/(1-x^2)^2$. To reach even total twelve, $c$ must be odd, hence one or three. With $c=1$, write $a=2u$, $b=2v+1$; then $u+v=5$, giving six solutions. With $c=3$, the equation is $u+v=4$, giving five. The answer is eleven. Coefficient extraction from the product selects degree ten or eight of the inverse squared even-step factor, yielding six and five respectively. The odd minimum in $b$ is encoded by its leading $x$; dropping it would reverse the parity condition.

### 35. An exact mixed-inventory cancellation

An inventory has type A in multiples of three, type B in quantities zero, one, or two, and type C in any nonnegative quantity. Find the number of selections of total $n$.

#### Solution

The product is $(1-x^3)^{-1}(1+x+x^2)(1-x)^{-1}=(1-x)^{-2}$. Thus the count is $n+1$. A direct explanation uses Euclidean division: every nonnegative combined quantity of A and B has a unique representation $3q+r$ with $r\in\{0,1,2\}$. That combined quantity can be any number from zero through $n$, after which C is forced. The cancellation is therefore supported by a bijection, not a formal coincidence. If B could also take quantity three, the representation would cease to be unique and this count would no longer apply.

### 36. Unordered change with three denominations

Count unordered coin selections of total ten using denominations one, two, and five.

#### Solution

Use $1/((1-x)(1-x^2)(1-x^5))$. Fix the number of five-unit coins: it can be zero, one, or two. The remaining totals are ten, five, and zero. With denominations one and two, the numbers of selections are six, three, and one, respectively, because the number of two-unit coins can range from zero to the floor of half the remaining total. Thus the answer is ten. A denomination-first dynamic program gives the same coefficient. Multiplying by permutations of the coins would change the model to ordered strings; identical copies and the empty residual selection already have the correct multiplicities in the product.

### 37. The same coins counted as ordered strings

Count ordered strings of total five using denominations one and two, and compare with unordered selections.

#### Solution

The sequence construction gives $1/(1-x-x^2)$. Its coefficients from size zero are 1,1,2,3,5,8, so the ordered answer is eight. Equivalently, a valid nonempty string ends in one or two, yielding the sum of counts for totals four and three. Unordered selections have OGF $1/((1-x)(1-x^2))$ and answer three, according to zero, one, or two copies of denomination two. The two OGFs agree only at the earliest sizes. Their size-three coefficients already differ: ordered count three versus unordered count two. Establishing whether order matters must precede any algebraic simplification.

### 38. Limited copies and the direction of the update loop

There is one available item of each weight one, two, three, and four. Count subsets of total five, then explain why an increasing-sum update would be wrong.

#### Solution

The OGF is $(1+x)(1+x^2)(1+x^3)(1+x^4)$. The only total-five subsets are weights one and four, or weights two and three, so the coefficient is two. A zero-or-one dynamic program updates sums in decreasing order for each item: this ensures that a new coefficient cannot immediately reuse the same current item. Increasing order would reuse a newly updated lower sum and create illegal multiple copies. This is not a numerical implementation detail; it changes each factor from $1+x^w$ toward its geometric inverse. Direct subset enumeration provides a small independent reference for the loop invariant.

### 39. Colored items with equal weights

There are two distinguishable types of unit-weight items, both with unlimited identical copies within type. Find the count of total $n$ and explain why merging the types is incorrect.

#### Solution

The two independent multiplicities give $(1-x)^{-2}$, with coefficient $n+1$. The choices are the possible quantity of the first type from zero through $n$, with the second forced. Merging equal numeric weights would leave only $(1-x)^{-1}$ and count one, erasing the type distinction. Conversely, ordered strings of red and blue items have OGF $1/(1-2x)$ and count $2^n$, since positions distinguish choices. Unlimited inventory multiplicity, colored type identity, and sequence order are three separate assumptions. A weight-only data structure must not silently identify objects whose types the problem treats as distinct.

### 40. Exactly four positive parts with a lower part size

Count ordered compositions of sixteen into exactly four parts, each at least two.

#### Solution

The component OGF is $x^2/(1-x)$, and exactly four components give $x^8/(1-x)^4$. Extract degree sixteen by shifting to degree eight, yielding $\binom{11}{3}=165$. Directly subtract two from each part to obtain four nonnegative variables summing to eight; stars and bars gives the same answer. The part positions are distinguishable, so no division by $4!$ is permitted. Equal-valued parts can occur and do not create fewer ordered positions. For target below eight the answer is zero, which the numerator shift makes immediate.

### 41. Restricted compositions and number-of-parts marking

Count compositions of nine with parts one or three and exactly five parts.

#### Solution

The bivariate sequence OGF is $1/(1-u(x+x^3))$. Extracting the fifth marker power gives $(x+x^3)^5=x^5(1+x^2)^5$. Degree nine therefore requires two of the five factors to contribute their extra square, giving $\binom{5}{2}=10$. Directly, two parts must be threes and the other three must be ones; their locations choose the same ten compositions. The marker counts components, not total size. Using $(1-x-x^3)^{-1}$ without the marker would include compositions with several different lengths and would answer a different question.

### 42. Zero-size components and infinite coefficients

A component may have size zero or one. Why does the ordinary sequence construction fail when only total size is counted? How can exactly $k$ components be counted instead?

#### Solution

There are infinitely many size-zero sequences: any number of zero components yields a different sequence of the same total size. Thus local finiteness already fails at the constant coefficient. The formal geometric expansion $\sum_{j\ge0}(1+x)^j$ does not define coefficients by finite sums. The algebraic expression $1/(1-(1+x))=-1/x$ is a Laurent expression and not an OGF for these counts. If the length is fixed at $k$, use $(1+x)^k$, whose degree-$n$ coefficient is $\binom{k}{n}$. Alternatively retain a length marker $u$ in $1/(1-u(1+x))$ and extract its $k$th coefficient before setting $u$ to one.

### 43. Prefix-coded binary words

Find the OGF for binary words with no adjacent ones, and compute the count at length six using a unique block decomposition.

#### Solution

Every such word is a sequence of blocks 0 or 10, followed by an optional terminal 1. The decomposition is unique: scan left to right and pair any nonterminal 1 with its forced following zero. The block sequence has OGF $1/(1-x-x^2)$; the terminal choice contributes $1+x$. Hence $G=(1+x)/(1-x-x^2)$. Its coefficients are 1,2,3,5,8,13,21, so length six gives 21. This is $F_8$ under the standard Fibonacci convention $F_0=0,F_1=1$. A recurrence with boundaries one and two provides a second proof. Leaving off the optional terminal block misses words that end in one.

### 44. Partitions into exactly three parts

Count integer partitions of ten into exactly three positive parts and derive the corresponding OGF.

#### Solution

Ferrers conjugation converts three parts into largest part exactly three. Thus the OGF is $x^3/((1-x)(1-x^2)(1-x^3))$. Degree ten reduces to unordered selections of total seven with denominations one, two, and three. Fixing the number of threes at zero, one, or two gives four, three, and one choices respectively, for total eight. The partitions are (8,1,1), (7,2,1), (6,3,1), (6,2,2), (5,4,1), (5,3,2), (4,4,2), and (4,3,3). This explicit list confirms both the count and the unordered interpretation; counting ordered compositions would greatly overcount them.

### 45. Distinct parts and the staircase shift

Count partitions of twelve into exactly three distinct positive parts.

#### Solution

Subtract the staircase (2,1,0) from the descending three parts. This yields a positive nonincreasing partition of nine into three parts, bijectively. The OGF is $x^6/((1-x)(1-x^2)(1-x^3))$, so extract residual total six. Fixing the number of threes at zero, one, or two yields four, two, and one choices, giving seven. The seven original partitions are (9,2,1), (8,3,1), (7,4,1), (7,3,2), (6,5,1), (6,4,2), and (5,4,3). The minimum sum is six, represented by (3,2,1). Using a numerator $x^3$ would forget distinctness and count ordinary three-part partitions instead.

### 46. Odd parts versus distinct parts

Prove that the number of odd-part partitions of seven equals the number of distinct-part partitions, and calculate their common value.

#### Solution

Multiply the distinct factors $1+x^j=(1-x^{2j})/(1-x^j)$ for positive $j$. The even-index numerator cancels even-index denominator factors, leaving inverses only for odd parts. For a target of seven, this can be justified by finite truncation; no infinite numerical cancellation is required. The distinct partitions are (7), (6,1), (5,2), (4,3), and (4,2,1), so there are five. The odd partitions are (7), (5,1,1), (3,3,1), (3,1,1,1,1), and seven ones, also five. The identity matches total counts; it does not preserve the number of parts, so a marker for that statistic cannot be carried through this cancellation unchanged.

### 47. A Durfee-square decomposition at a fixed size

Compute the number of partitions of seven by separating Durfee-square sizes.

#### Solution

Only sizes one and two can occur for nonempty size seven. For size one, the OGF is $x/(1-x)^2$, whose degree-seven coefficient is seven. For size two, the OGF is $x^4/((1-x)^2(1-x^2)^2)$. The remaining degree three receives four from zero degree in the even factor and degree three in the first squared inverse, plus $2\cdot2=4$ from degree two in the even factor and degree one in the other. Its contribution is eight. Thus the total is fifteen. The empty Durfee case contributes only at size zero. The decomposition is disjoint because each Ferrers diagram has a unique largest top-left square.

### 48. Self-conjugate diagrams and odd hooks

Count self-conjugate partitions of nine using their diagonal-hook generating function.

#### Solution

Diagonal hooks are distinct odd positive lengths, giving the product over odd $j$ of $1+x^j$. Distinct odd parts summing to nine are (9) and (5,3,1), so the answer is two. Their corresponding self-conjugate partitions are (5,1,1,1,1) and (3,3,3), as can be checked by transposing each Ferrers diagram. An odd-part partition with repeated odd parts does not necessarily correspond to a self-conjugate diagram by this hook construction; distinctness is essential. The hook lengths partition the cells, and their nested positions determine the original diagram uniquely, proving the count rather than merely suggesting it.
