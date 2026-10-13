# Divide-and-conquer answers — unintegrated review draft

### Solution 1

**Use mass conservation to prove both bounds for the unequal tree.** Let $B>0$ be the fixed stopping size, $\delta=\min(\alpha,\beta)$ and $q=\max(\alpha,\beta)$. Because both constants are positive and sum to one, $0<\delta\le q<1$. First analyze the stated real-size recurrence, which keeps the exact identities visible.

At depth $j$, every node has size between $n\delta^j$ and $nq^j$. While the smaller bound exceeds $B$, the entire level remains internal. Its sizes sum to $n$: each split replaces size $s$ by $\alpha s+\beta s=s$. Therefore each of $\Theta(\log n)$ complete levels contributes exactly $n$ toll, proving $\Omega(n\log n)$.

Every branch stops after at most $\log_{1/q}(n/B)+O(1)$ levels. On any incomplete level, internal-node sizes total at most $n$, because terminated subtrees contribute no further internal work. All internal tolls are consequently $O(n\log n)$. Every nonroot leaf has size in $(\delta B,B]$; leaf sizes sum to $n$. There are $O(n)$ leaves, whose bounded base costs add only $O(n)$. This proves the matching upper bound and $T(n)\in\Theta(n\log n)$.

Option 2 is the stated valid upper bound. Options 1 and 4 have only linear order for fixed $\alpha,\beta$, which is too small. The ratio of option 3 to the derived order is $\beta n^{\alpha-1}\to0$, so that upper bound also fails. Fixed ratios matter: permitting $\alpha$ to approach zero with the input changes the constants and can invalidate this uniform argument. For an implementation with integer children, declare the rounding and verify progress; the exact real-size identities are not automatically exact integer identities.

### Solution 2

**Prove the actual concatenation order by induction.** The input contains distinct values. For length zero or one, the returned array is already descending and preserves the input records. For a larger input, an actual median $m$ separates the remaining values into $R$, whose members are greater than $m$, and $L$, whose members are smaller. Both children are smaller and the three groups partition the input.

Assume the recursive results for $R$ and $L$ are descending. Every value in the first result exceeds $m$, and $m$ exceeds every value in the last result. Therefore the concatenation of the right result, singleton median and left result is descending across both boundaries as well as inside each child. It also contains every input record exactly once. This establishes the contract for the parent and completes induction. Option 4 is correct.

On input $[4,1,3,2,5]$, the median is three. The two recursive outputs are $[5,4]$ and $[2,1]$, so the final output is $[5,4,3,2,1]$. The small example illustrates the invariant; the induction proves it for every permitted size, regardless of the original input order. With even length, choosing either central input key as the median preserves the same descending argument.

Option 1 incorrectly assigns different internal directions to the two children; the same algorithm recursively sorts both in descending order. Option 2 has no basis: deterministic comparison and concatenation enforce an ordered result. Option 3 reverses the two concatenation boundaries and would describe a different program. Distinctness is essential to the printed multiset-preservation specification: if equal keys existed, both strict child sets would exclude every occurrence equal to $m$, and the singleton median would retain only one. A duplicate-aware version must return the entire equal-key block.

### Solution 3

**Count comparisons only while both merge fronts exist.** The original array is $[12,7,5,9,3,8,2,6]$. Its four length-two merges compare $(12,7)$, $(5,9)$, $(3,8)$ and $(2,6)$ once each, contributing four comparisons. Their sorted outputs are $[7,12]$, $[5,9]$, $[3,8]$ and $[2,6]$.

The next left merge compares $7$ with $5$, $7$ with $9$, then $12$ with $9$. Its right run becomes empty, and appending twelve needs no key comparison. Its output is $[5,7,9,12]$ and its count is three. The next right merge compares $3$ with $2$, $3$ with $6$, then $8$ with $6$, also three; its output is $[2,3,6,8]$.

At the final merge the exact compared pairs are $(5,2),(5,3),(5,6),(7,6),(7,8),(9,8)$. After six comparisons the right run is exhausted. The remaining nine and twelve are appended without comparing two keys. Hence
$$C=4+3+3+6=16.$$
Option 1 is correct. This is a trace for the actual input, not the maximum over all eight-key permutations, whose value is seventeen.

Option 2, fourteen, misses two actual front comparisons; there is no early termination before the documented right fronts have been consumed. Option 3, twelve, is the count for an already sorted eight-key input under this merge policy, not for the given input. Option 4, ten, counts just the four initial and six final comparisons and omits the two intermediate merges. Comparisons with array lengths and pointer updates are excluded because the question measures element comparisons. Neither copying a remainder nor returning a singleton compares two keys.

### Solution 4

**Derive the branch sizes from the pivot guarantee, not from a preferred theorem.** For sufficiently large $n$, the sample size $m=2\sqrt n+1$ is at most $n$ after ordinary rounding. Insertion sort of these $\Theta(\sqrt n)$ sampled elements costs $O(m^2)=O(n)$, and the ordinary partition scan performs $\Theta(n)$ work. The combined toll is therefore $\Theta(n)$ even when the sample happened to be already sorted.

Assume distinct keys. The sample median has at least $\sqrt n$ sampled keys below it and at least that many above it, suppressing the integer corrections. The global pivot rank cannot be closer than roughly $\sqrt n$ to either endpoint. Nevertheless all unsampled keys can lie on one side, so the guarantee allows a small side of that order and a large side of order $n-\sqrt n$.

The faithful integer worst-case model is a maximization over the allowed ranks:
$$W(n)=\max_{r\in R_n}\bigl(W(r)+W(n-1-r)+\Theta(n)\bigr),$$
where $R_n$ excludes the forbidden endpoint ranks. The listed extreme-split abstraction suppresses the pivot, rounding and bounded corrections, yielding $T(n-\sqrt n)+T(\sqrt n)+n$, option 4. It describes the worst permitted imbalance, not the split of every input. A proof that the same extreme choices can be realized recursively needs an adversarial-input argument; the recurrence choice alone is not that proof.

Option 1 creates two almost full-size children and violates disjoint partition sizes. Option 2 accounts for only about $2\sqrt n$ elements and omits the large partition. Option 3 again counts two large children whose total size exceeds the parent's available keys. With duplicate keys, an equal-key partition policy must be specified; the distinct-rank guarantee cannot be imported unchanged. This is a modeling question, so applying the equal-ratio Master theorem would miss its central point.

### Solution 5

**The sorted input makes each left run exhaust first.** At the bottom depth there are four merges of two singleton runs, each needing one front comparison, for four comparisons. At the next depth there are two merges of length-two runs. Every key in the left run is smaller than every key in the right run, so each merge uses exactly two comparisons to exhaust the left run. Those merges contribute another four.

The final merge compares the four left keys with the unchanged first right key until the left side is exhausted, using exactly four comparisons. Therefore
$$C(8)=4+4+4=12,$$
and option 2 is correct. In general, at input $N=2^h$, each of the $h$ internal merge depths contributes $N/2$ front comparisons on this sorted input, giving $(N/2)h$.

This count is smaller than the maximum seventeen for eight keys, but it is still of order $N\log N$. The algorithm has not been specified to skip a merge when the boundary keys are already ordered. An explicit adaptive check could change its best case and must be charged as a different algorithm.

Option 1, seven, counts internal merge calls rather than the comparisons inside them. Option 3, sixteen, is the count for the different authentic array in Question 3. Option 4, seventeen, is the worst-case maximum over arrangements, which this sorted input does not attain. The lower-level count, intermediate count and final count must all use the same front-comparison convention. Copying the unused right remainder writes output records but does not compare two element keys.

### Solution 6

**Count strict inequalities and preserve the identities of equal records.** With left run $[1,3,3]$ and right run $[2,3,4]$, a cross inversion chooses one item from each run and requires the left key to be strictly larger. The left one contributes none. Each of the two separate left threes exceeds the right two, but neither exceeds the right three or four. Thus exactly two ordered index pairs are inversions, and option 1 is correct.

The merge computation gives an independent trace. First emit left one. The right two is now smaller than the two remaining left threes, so add two and emit it. On the next equal-key comparison, emit the left three and add zero; repeat for the other left three. The right three and four are then remainder items. No further strict cross inversion exists.

The two left threes are distinct index positions and each forms its own valid pair with the right two. Their equality to each other does not merge them into one record. Conversely, equality across runs is not an inversion. Using a greater-than-or-equal definition would add the two left-three/right-three pairs and produce four, explaining option 2's mistake. Options 3 and 4 add additional nonexistent inequalities, such as a left three exceeding the right four, or confuse the number of merge operations with the inversion count.

The linear merge counts several inversions with one addition because sortedness certifies that every unconsumed left key is larger than the current right key. It need not enumerate those pairs individually. This distinction becomes decisive when two runs generate quadratically many inversions but can still be merged in linear work.

### Solution 7

**Classify the optimal interval by its location relative to the split.** Every nonempty interval is inside the left segment, inside the right segment, or crosses the boundary. The first two best sums are five and six. A crossing interval consists of a nonempty left suffix followed by a nonempty right prefix, whose independent maxima are one and six. Therefore the crossing maximum is seven, and
$$B_{LR}=\max(5,6,1+6)=7.$$
Option 3 is correct. The full combined summary is $(2,4,5,7)$: total $-2+4=2$, prefix $\max(3,-2+6)=4$, suffix $\max(4,4+1)=5$, and best seven.

The supplied summaries are realizable, so this is not merely arithmetic on inconsistent hypothetical data. A left witness array is $[3,-6,5,-5,1]$, with total negative two, best prefix three, best suffix one and best interval five. A right witness is $[6,-2]$, with total four, best prefix six, best suffix four and best interval six. Their crossing interval $[1,6]$ attains seven in the concatenation.

Option 1 chooses only the left optimum and ignores both other locations. Option 2 chooses only the better child and omits the crossing candidate. Option 4 adds the left prefix to the right prefix, yielding $3+6=9$. Those two pieces generally do not concatenate into an interval crossing the split because the selected left prefix may end before the boundary. The necessary boundary quantity is the left suffix. The summary is ordered: swapping left and right changes the prefix, suffix and possible crossing value.

### Solution 8

**Derive the cross coefficient before recombining radix blocks.** Write $23=2\cdot10+3$ and $47=4\cdot10+7$. Their product expands to $z_2\cdot100+z_1\cdot10+z_0$, where $z_2=2\cdot4=8$ and $z_0=3\cdot7=21$. The third Karatsuba product is $(2+3)(4+7)=5\cdot11=55$. Distributivity gives the missing cross coefficient:
$$z_1=55-8-21=26.$$
Reconstruction then yields
$$23\cdot47=8\cdot100+26\cdot10+21=1081.$$
Option 1 is correct. A conventional multiplication check gives $23(40+7)=920+161=1081$.

Option 2 incorrectly treats the raw third product 55 as the cross coefficient, without subtracting the unmixed terms. That would reconstruct 1371, but it is not the given product. Option 3 uses an incorrect mixed coefficient 29, which reconstructs 1111 and fails direct multiplication. Option 4 keeps the correct mixed coefficient while giving the wrong reconstruction: 821 is only $800+21$, so it omits the middle contribution 260.

The shifts are determined by the low-block width, which is one decimal digit. The third product can use larger operands than the individual parts because sums may carry; that width must be included in a bit-complexity argument. The identity itself is exact even though the cross coefficient 26 exceeds a single decimal digit. No digit-wise carry is discarded: ordinary integer addition during reconstruction incorporates it correctly.

### Solution 9

**Charge the stated quadratic combine cost, rather than memorizing Karatsuba's linear toll.** The model is $T(n)=3T(n/2)+\Theta(n^2)$ with positive bounded bases and a regular fixed split. Its branching exponent is $\log_23<2$. At complete depth $j$, the total squared-size toll is a positive constant multiple of
$$3^j(n/2^j)^2=n^2(3/4)^j.$$
The internal sum is bounded above by a constant multiple of $n^2\sum_{j\ge0}(3/4)^j=4n^2$. The leaves add $O(n^{\log_23})$, a smaller order. A positive quadratic root toll supplies the matching lower bound. Thus $T(n)\in\Theta(n^2)$, option 2.

An induction envelope reaches the same conclusion: with upper toll $cn^2$, a guess $T(n)\le Cn^2$ closes when $3C/4+c\le C$, or $C\ge4c$, with the base covered by increasing $C$ if necessary. This gives a complete upper proof independently of the level diagram.

Option 1 counts the leaf exponent while ignoring the larger compulsory root work. Option 3 adds a logarithm as though every depth had equal quadratic aggregate cost; here the ratio is three-quarters, so the costs decrease geometrically. Option 4 treats the number of children as an exponential in the original size instead of in its logarithmic depth. The same child count can accompany different costs depending on the combine operation, so the algebraic product-reuse idea alone does not determine this recurrence's answer.

### Solution 10

**Add degrees, then convert degree to coefficient count.** The two input lengths are five and four, so their degrees are at most four and three. The product degree is at most seven, and complete ordinary convolution needs eight coefficient positions. A radix-two transform must therefore have length at least eight and be a power of two. The smallest such length is eight, option 2.

For a concrete boundary witness, take $A(x)=x^4$ and $B(x)=x^3$. Their product is $x^7$. Evaluation at fourth roots identifies $x^4$ with one, so length four would wrap the exponent seven to exponent three and return the wrong linear convolution. At length eight, exponents zero through seven are distinct modulo eight and no product coefficient wraps.

Option 1 is insufficient, as that witness shows. Options 3 and 4, sixteen and thirty-two, are sufficient padded lengths but are not the smallest. Choosing their larger sizes needlessly increases transform work; the question asks for minimal capacity, not for any possible safe transform. If the highest input coefficients vanished, an instance could have smaller actual degree, but the general guarantee for the given coefficient capacities still needs eight.

The transform also needs a valid primitive root and a consistent inverse. Over complex numbers, choose a primitive eighth root. Over a finite field, an order-eight root must exist and eight must be invertible. Sufficient padding settles index aliasing; it does not by itself prove numerical accuracy or exact recovery of unbounded integer coefficients.

### Solution 11

**Use only the information supplied by the sample.** Nine distinct sampled keys, sorted by value, have a fifth key as their median. Exactly four sampled keys are strictly smaller and four are strictly larger. These keys are also members of the entire input, so at least four full-input keys lie on each side. Option 1 is the guaranteed bound.

The bound is tight. Choose the sample values one through nine, so its median is five. Place all unsampled keys above nine. Then the full array has exactly four keys below the pivot, even if its length is arbitrarily larger than nine. Reversing the construction by placing all unsampled keys below one gives exactly four above it. These two witnesses show why the sample alone cannot guarantee a global half split.

Option 2 confuses a median of a sample with a median of the whole array; the first construction refutes it for sufficiently large arrays. Option 3 claims nine keys on each side, but the sample itself supplies only four and unsampled keys can all be on the other side. Option 4 ignores the eight actual sample neighbors and is weaker than what the supplied information proves.

For a distinct-key input of length $n\ge9$, the pivot's one-based global rank lies between five and $n-4$, inclusive. The two resulting partition sizes therefore lie between four and $n-5$. These exact bounds include the pivot exclusion. The symmetry gives a guarantee for each side, not a statement that one input simultaneously minimizes both sides. Duplicate keys would require defining strict versus nonstrict counts and a three-way equal-key partition.

### Solution 12

**Count the representation-building toll at every recursion level.** For an exact power-of-two size $N=2^h$, a complete level $j$ has $2^j$ nodes of size $N/2^j$. When each node re-sorts its information in $\Theta(s\log s)$ work, the level cost is of order $N(h-j)$. Summing over $j=0,\ldots,h-1$ gives
$$N\sum_{r=1}^h r=N\frac{h(h+1)}2,$$
up to fixed positive toll constants. Bounded leaf work adds only $\Theta(N)$. Thus the stated repeated-sorting recurrence has tight order $\Theta(N\log^2N)$.

Maintaining the presorted representations changes the recursive toll to $\Theta(s)$. Each complete internal depth then costs $\Theta(N)$, so its total is $\Theta(Nh)=\Theta(N\log N)$. The initial two coordinate sorts also have at most that order and do not introduce a second logarithm. Option 1 gives these two respective classes correctly.

Option 2 overstates the first as quadratic and understates the second as linear, ignoring its positive complete levels. Option 3 fails to sum the decreasing logarithmic toll across all levels and again omits the second model's depth factor. Option 4 assumes repeated sorting is free or can be charged only once, contrary to the first recurrence.

The geometric seven-successor proof is unchanged by this improvement; it is the maintained ordering that removes the extra factor. A statement that an actual implementation always pays a tight sorting toll must be justified separately. The question explicitly supplies positive $\Theta$ tolls, so matching level lower work is part of its mathematical model rather than inferred from an upper-only algorithm description.

### Solution 13

**Derive the mechanism and the exact measure.** Let $N=2^n$ and count only comparisons of two present front keys. At depth $j<n$, there are $2^j$ merges, each with worst cost $N/2^j-1$. The complete level contributes $N-2^j$. Unit-size leaves compare no keys. Summing all internal depths gives $nN-\sum_{j=0}^{n-1}2^j=nN-N+1$. The zero-depth seed is zero, and the recurrence $C(2N)=2C(N)+2N-1$ verifies the formula independently. The per-merge maximum can be attained by interleaving the sorted child outputs; recursively assigning their relative ranks permits child maxima as well. This is the maximum over suitable input arrangements, not the count on every array.

$$Q_n=n2^n-2^n+1.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $129$, so option 2 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $25$, rather than the derived value $129$. Option 3 gives $160$, rather than the derived value $129$. Option 4 gives $31$, rather than the derived value $129$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 14

**Derive the mechanism and the exact measure.** Let $N=2^n$ and count only comparisons of two present front keys. At depth $j<n$, there are $2^j$ merges, each with worst cost $N/2^j-1$. The complete level contributes $N-2^j$. Unit-size leaves compare no keys. Summing all internal depths gives $nN-\sum_{j=0}^{n-1}2^j=nN-N+1$. The zero-depth seed is zero, and the recurrence $C(2N)=2C(N)+2N-1$ verifies the formula independently. The per-merge maximum can be attained by interleaving the sorted child outputs; recursively assigning their relative ranks permits child maxima as well. This is the maximum over suitable input arrangements, not the count on every array.

$$Q_n=n2^n-2^n+1.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $1793$, so option 1 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 2 gives $2048$, rather than the derived value $1793$. Option 3 gives $255$, rather than the derived value $1793$. Option 4 gives $64$, rather than the derived value $1793$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 15

**Derive the mechanism and the exact measure.** Let $N=2^n$ and count only comparisons of two present front keys. At depth $j<n$, there are $2^j$ merges, each with worst cost $N/2^j-1$. The complete level contributes $N-2^j$. Unit-size leaves compare no keys. Summing all internal depths gives $nN-\sum_{j=0}^{n-1}2^j=nN-N+1$. The zero-depth seed is zero, and the recurrence $C(2N)=2C(N)+2N-1$ verifies the formula independently. The per-merge maximum can be attained by interleaving the sorted child outputs; recursively assigning their relative ranks permits child maxima as well. This is the maximum over suitable input arrangements, not the count on every array.

$$Q_n=n2^n-2^n+1.$$

**Check the symbolic alternatives.** Option 4 is the derived general expression. $n2^n$ uses size toll rather than size-minus-one comparisons; $2^n-1$ counts just internal merge nodes or the last maximum merge; $n^2$ treats depth as input length. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 16

**Derive the mechanism and the exact measure.** Let $N=2^n$ and count only comparisons of two present front keys. At depth $j<n$, there are $2^j$ merges, each with worst cost $N/2^j-1$. The complete level contributes $N-2^j$. Unit-size leaves compare no keys. Summing all internal depths gives $nN-\sum_{j=0}^{n-1}2^j=nN-N+1$. The zero-depth seed is zero, and the recurrence $C(2N)=2C(N)+2N-1$ verifies the formula independently. The per-merge maximum can be attained by interleaving the sorted child outputs; recursively assigning their relative ranks permits child maxima as well. This is the maximum over suitable input arrangements, not the count on every array.

$$Q_n=n2^n-2^n+1.$$

**Apply the boundary statement.** The correct statement says that charging combine work only once omits the other depths. A merge can append its last leftover key without a key comparison, so one comparison per output key is not its exact maximum. The dominant expression $n2^n$ omits the finite subtract-$2^n$ correction. The final merge's $2^n-1$ count excludes every recursive comparison. Exact answers require all depths and their endpoints. Thus option 3 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 17

**Derive the mechanism and the exact measure.** Each of the $n$ left records occurs before each of the $n$ right records in the original concatenation. By hypothesis its value also exceeds every right value. Thus every ordered choice of one left and one right position is a cross inversion. These choices form a Cartesian product of size $n\cdot n=n^2$. There are no within-block inversions because each block is sorted. During merge, each emitted right key sees all $n$ left keys still unconsumed and adds $n$ to the counter. There are $n$ such right keys, yielding the same total with just $n$ aggregate additions. The output writes $2n$ keys, while the inversion count is a separate numerical result.

$$Q_n=n^2.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $25$, so option 4 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $20$, rather than the derived value $25$. Option 2 gives $50$, rather than the derived value $25$. Option 3 gives $100$, rather than the derived value $25$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 18

**Derive the mechanism and the exact measure.** Each of the $n$ left records occurs before each of the $n$ right records in the original concatenation. By hypothesis its value also exceeds every right value. Thus every ordered choice of one left and one right position is a cross inversion. These choices form a Cartesian product of size $n\cdot n=n^2$. There are no within-block inversions because each block is sorted. During merge, each emitted right key sees all $n$ left keys still unconsumed and adds $n$ to the counter. There are $n$ such right keys, yielding the same total with just $n$ aggregate additions. The output writes $2n$ keys, while the inversion count is a separate numerical result.

$$Q_n=n^2.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $64$, so option 3 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $128$, rather than the derived value $64$. Option 2 gives $256$, rather than the derived value $64$. Option 4 gives $56$, rather than the derived value $64$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 19

**Derive the mechanism and the exact measure.** Each of the $n$ left records occurs before each of the $n$ right records in the original concatenation. By hypothesis its value also exceeds every right value. Thus every ordered choice of one left and one right position is a cross inversion. These choices form a Cartesian product of size $n\cdot n=n^2$. There are no within-block inversions because each block is sorted. During merge, each emitted right key sees all $n$ left keys still unconsumed and adds $n$ to the counter. There are $n$ such right keys, yielding the same total with just $n$ aggregate additions. The output writes $2n$ keys, while the inversion count is a separate numerical result.

$$Q_n=n^2.$$

**Check the symbolic alternatives.** Option 2 is the derived general expression. $4n^2$ counts all ordered pairs in the two-block universe rather than cross pairs; $n(n-1)$ incorrectly excludes matching cross-block index numbers; $2n^2$ counts each left/right choice twice. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 20

**Derive the mechanism and the exact measure.** Each of the $n$ left records occurs before each of the $n$ right records in the original concatenation. By hypothesis its value also exceeds every right value. Thus every ordered choice of one left and one right position is a cross inversion. These choices form a Cartesian product of size $n\cdot n=n^2$. There are no within-block inversions because each block is sorted. During merge, each emitted right key sees all $n$ left keys still unconsumed and adds $n$ to the counter. There are $n$ such right keys, yielding the same total with just $n$ aggregate additions. The output writes $2n$ keys, while the inversion count is a separate numerical result.

$$Q_n=n^2.$$

**Apply the boundary statement.** The correct statement permits counting quadratically many inversions in linear combine work without listing them. A count and an explicit list have different output-size obligations. Equal positions within different blocks are still different records and have no diagonal exclusion. The number of key comparisons can be $n$ when the right block exhausts first, whereas the inversion count is $n^2$. Internal sortedness does not prevent cross-block inversions. Thus option 1 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 21

**Derive the mechanism and the exact measure.** The question specifies a regular recursion with exactly three executed half-width multiplications at each nonbase call and a scalar base at width one. From width $N=2^n$, each root-to-leaf path has exactly $n$ halving steps. Depth zero has one call; multiplication by the branching count gives $3^j$ calls at depth $j$. Therefore the last depth contains $3^n$ scalar multiplication leaves. The same conclusion follows from $L_0=1$, $L_n=3L_{n-1}$. In the original width, this is $N^{\log_23}$. A complete three-child tree has $(3^n-1)/2$ internal nodes, which is a different count. The algebraic mixed-term identity is what makes three products sufficient; deleting a fourth necessary term without that identity would be incorrect.

$$Q_n=3^n.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $243$, so option 4 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $1024$, rather than the derived value $243$. Option 2 gives $32$, rather than the derived value $243$. Option 3 gives $1215$, rather than the derived value $243$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 22

**Derive the mechanism and the exact measure.** The question specifies a regular recursion with exactly three executed half-width multiplications at each nonbase call and a scalar base at width one. From width $N=2^n$, each root-to-leaf path has exactly $n$ halving steps. Depth zero has one call; multiplication by the branching count gives $3^j$ calls at depth $j$. Therefore the last depth contains $3^n$ scalar multiplication leaves. The same conclusion follows from $L_0=1$, $L_n=3L_{n-1}$. In the original width, this is $N^{\log_23}$. A complete three-child tree has $(3^n-1)/2$ internal nodes, which is a different count. The algebraic mixed-term identity is what makes three products sufficient; deleting a fourth necessary term without that identity would be incorrect.

$$Q_n=3^n.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $6561$, so option 3 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $256$, rather than the derived value $6561$. Option 2 gives $52488$, rather than the derived value $6561$. Option 4 gives $65536$, rather than the derived value $6561$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 23

**Derive the mechanism and the exact measure.** The question specifies a regular recursion with exactly three executed half-width multiplications at each nonbase call and a scalar base at width one. From width $N=2^n$, each root-to-leaf path has exactly $n$ halving steps. Depth zero has one call; multiplication by the branching count gives $3^j$ calls at depth $j$. Therefore the last depth contains $3^n$ scalar multiplication leaves. The same conclusion follows from $L_0=1$, $L_n=3L_{n-1}$. In the original width, this is $N^{\log_23}$. A complete three-child tree has $(3^n-1)/2$ internal nodes, which is a different count. The algebraic mixed-term identity is what makes three products sufficient; deleting a fourth necessary term without that identity would be incorrect.

$$Q_n=3^n.$$

**Check the symbolic alternatives.** Option 2 is the derived general expression. $n3^n$ multiplies the terminal count by depth unnecessarily; $4^n$ counts four children per call; $2^n$ confuses width shrink with the number of calls. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 24

**Derive the mechanism and the exact measure.** The question specifies a regular recursion with exactly three executed half-width multiplications at each nonbase call and a scalar base at width one. From width $N=2^n$, each root-to-leaf path has exactly $n$ halving steps. Depth zero has one call; multiplication by the branching count gives $3^j$ calls at depth $j$. Therefore the last depth contains $3^n$ scalar multiplication leaves. The same conclusion follows from $L_0=1$, $L_n=3L_{n-1}$. In the original width, this is $N^{\log_23}$. A complete three-child tree has $(3^n-1)/2$ internal nodes, which is a different count. The algebraic mixed-term identity is what makes three products sufficient; deleting a fourth necessary term without that identity would be incorrect.

$$Q_n=3^n.$$

**Apply the boundary statement.** The correct statement distinguishes leaf count from total bit complexity. Additions, subtraction, signs, shifts and growing representations also cost work in a bit model. A regular padded implementation obeys the stated count; a value-dependent implementation that shortens operands or skips zero products can have fewer calls on some inputs. Product reuse does not make every precision operation constant time. The specified child count is three, not four. Thus option 1 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 25

**Derive the mechanism and the exact measure.** Let the original square dimension be $N=2^n$. Each recursive stage halves the dimension, so the depth to scalar dimension one is $n$. The regular seven-product identity creates seven children at every nonbase call. Hence depth $j$ has $7^j$ subproducts and the terminal count is $7^n$. The recurrence $L_0=1$, $L_n=7L_{n-1}$ proves it exactly. Restoring the original dimension gives $N^{\log_27}$. The standard arithmetic recurrence also includes a quadratic combine toll; because $\log_27>2$, its order is governed by the leaf exponent. Nevertheless the exact scalar multiplication count is not the exact total number of arithmetic operations. Ordered block products cannot be commuted when applying the identity recursively.

$$Q_n=7^n.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $16807$, so option 3 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $1024$, rather than the derived value $16807$. Option 2 gives $32$, rather than the derived value $16807$. Option 4 gives $32768$, rather than the derived value $16807$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 26

**Derive the mechanism and the exact measure.** Let the original square dimension be $N=2^n$. Each recursive stage halves the dimension, so the depth to scalar dimension one is $n$. The regular seven-product identity creates seven children at every nonbase call. Hence depth $j$ has $7^j$ subproducts and the terminal count is $7^n$. The recurrence $L_0=1$, $L_n=7L_{n-1}$ proves it exactly. Restoring the original dimension gives $N^{\log_27}$. The standard arithmetic recurrence also includes a quadratic combine toll; because $\log_27>2$, its order is governed by the leaf exponent. Nevertheless the exact scalar multiplication count is not the exact total number of arithmetic operations. Ordered block products cannot be commuted when applying the identity recursively.

$$Q_n=7^n.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $5764801$, so option 2 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $256$, rather than the derived value $5764801$. Option 3 gives $16777216$, rather than the derived value $5764801$. Option 4 gives $65536$, rather than the derived value $5764801$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 27

**Derive the mechanism and the exact measure.** Let the original square dimension be $N=2^n$. Each recursive stage halves the dimension, so the depth to scalar dimension one is $n$. The regular seven-product identity creates seven children at every nonbase call. Hence depth $j$ has $7^j$ subproducts and the terminal count is $7^n$. The recurrence $L_0=1$, $L_n=7L_{n-1}$ proves it exactly. Restoring the original dimension gives $N^{\log_27}$. The standard arithmetic recurrence also includes a quadratic combine toll; because $\log_27>2$, its order is governed by the leaf exponent. Nevertheless the exact scalar multiplication count is not the exact total number of arithmetic operations. Ordered block products cannot be commuted when applying the identity recursively.

$$Q_n=7^n.$$

**Check the symbolic alternatives.** Option 1 is the derived general expression. $8^n$ uses the classical eight-product block algorithm; $4^n$ counts quadrant-sized entries rather than seven recursive products; $2^n$ is the original dimension, not the leaf multiplicity. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 28

**Derive the mechanism and the exact measure.** Let the original square dimension be $N=2^n$. Each recursive stage halves the dimension, so the depth to scalar dimension one is $n$. The regular seven-product identity creates seven children at every nonbase call. Hence depth $j$ has $7^j$ subproducts and the terminal count is $7^n$. The recurrence $L_0=1$, $L_n=7L_{n-1}$ proves it exactly. Restoring the original dimension gives $N^{\log_27}$. The standard arithmetic recurrence also includes a quadratic combine toll; because $\log_27>2$, its order is governed by the leaf exponent. Nevertheless the exact scalar multiplication count is not the exact total number of arithmetic operations. Ordered block products cannot be commuted when applying the identity recursively.

$$Q_n=7^n.$$

**Apply the boundary statement.** The correct statement retains nonproduct additions in the combine toll. Seven products at one node compound into $7^n$ scalar leaves after $n$ stages, rather than seven leaves total. Halving both dimensions still takes $n$ stages; dividing the number of entries by four does not divide recursion depth by four. The leaf count describes this regular algorithm and does not establish a lower bound for every matrix-multiplication method. Thus option 4 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 29

**Derive the mechanism and the exact measure.** An array of $n$ coefficients indexed zero through $n-1$ represents a polynomial of degree $n-1$ when its last coefficient is nonzero. Over the ordinary real, complex or finite-field coefficient domains used here, the two nonzero leading coefficients have a nonzero product. Thus the product degree is exactly $2n-2$, and its complete coefficient count is degree plus one, namely $2n-1$. The highest coefficient comes from the unique index pair $(n-1,n-1)$, so it cannot cancel with another contribution. Coefficient positions run from zero through $2n-2$ inclusively. A radix-two transform may need a larger padded length; coefficient count and chosen transform length are separate quantities. Rings with zero divisors need additional qualifications because nonzero leading factors could multiply to zero.

$$Q_n=2n-1.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $9$, so option 4 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $10$, rather than the derived value $9$. Option 2 gives $25$, rather than the derived value $9$. Option 3 gives $5$, rather than the derived value $9$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 30

**Derive the mechanism and the exact measure.** An array of $n$ coefficients indexed zero through $n-1$ represents a polynomial of degree $n-1$ when its last coefficient is nonzero. Over the ordinary real, complex or finite-field coefficient domains used here, the two nonzero leading coefficients have a nonzero product. Thus the product degree is exactly $2n-2$, and its complete coefficient count is degree plus one, namely $2n-1$. The highest coefficient comes from the unique index pair $(n-1,n-1)$, so it cannot cancel with another contribution. Coefficient positions run from zero through $2n-2$ inclusively. A radix-two transform may need a larger padded length; coefficient count and chosen transform length are separate quantities. Rings with zero divisors need additional qualifications because nonzero leading factors could multiply to zero.

$$Q_n=2n-1.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $15$, so option 3 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $64$, rather than the derived value $15$. Option 2 gives $8$, rather than the derived value $15$. Option 4 gives $16$, rather than the derived value $15$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 31

**Derive the mechanism and the exact measure.** An array of $n$ coefficients indexed zero through $n-1$ represents a polynomial of degree $n-1$ when its last coefficient is nonzero. Over the ordinary real, complex or finite-field coefficient domains used here, the two nonzero leading coefficients have a nonzero product. Thus the product degree is exactly $2n-2$, and its complete coefficient count is degree plus one, namely $2n-1$. The highest coefficient comes from the unique index pair $(n-1,n-1)$, so it cannot cancel with another contribution. Coefficient positions run from zero through $2n-2$ inclusively. A radix-two transform may need a larger padded length; coefficient count and chosen transform length are separate quantities. Rings with zero divisors need additional qualifications because nonzero leading factors could multiply to zero.

$$Q_n=2n-1.$$

**Check the symbolic alternatives.** Option 2 is the derived general expression. $n$ is an input length and does not include the new high-degree coefficients; $2n$ confuses the count with a convenient larger capacity; $n^2$ counts coefficient pair products rather than output positions. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 32

**Derive the mechanism and the exact measure.** An array of $n$ coefficients indexed zero through $n-1$ represents a polynomial of degree $n-1$ when its last coefficient is nonzero. Over the ordinary real, complex or finite-field coefficient domains used here, the two nonzero leading coefficients have a nonzero product. Thus the product degree is exactly $2n-2$, and its complete coefficient count is degree plus one, namely $2n-1$. The highest coefficient comes from the unique index pair $(n-1,n-1)$, so it cannot cancel with another contribution. Coefficient positions run from zero through $2n-2$ inclusively. A radix-two transform may need a larger padded length; coefficient count and chosen transform length are separate quantities. Rings with zero divisors need additional qualifications because nonzero leading factors could multiply to zero.

$$Q_n=2n-1.$$

**Apply the boundary statement.** The correct statement warns that a transform shorter than the linear length can alias coefficients. Evaluation at $M$th roots identifies powers differing by $M$, so inverse results sum contributions modulo $x^M-1$. Circular and linear convolution agree only when wrapping contributes nothing under suitable padding or special data. Degree is one less than coefficient count. For $n>1$, transform length $n$ is not a universal capacity guarantee for the full product. Thus option 1 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 33

**Derive the mechanism and the exact measure.** Write the transform length as $N=2^n$. A radix-two FFT has $n$ stages, and each stage partitions its $N$ values into $N/2$ disjoint pairs. Each pair produces two outputs by one butterfly. Consequently the complete count is $n(N/2)=n2^{n-1}$. Counting output nodes instead would give $nN$, twice as many. The zero-stage transform at $N=1$ requires zero butterflies; positive indices give the stated integer expression. In one ordinary butterfly, a twiddle product is used in both a sum and a difference. Therefore its arithmetic cost includes operations beyond a single multiplication. Some twiddle factors are special values such as one, but optimizing those products does not remove the pair's butterfly from the defined count.

$$Q_n=n2^{n-1}.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $80$, so option 1 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 2 gives $160$, rather than the derived value $80$. Option 3 gives $31$, rather than the derived value $80$. Option 4 gives $25$, rather than the derived value $80$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 34

**Derive the mechanism and the exact measure.** Write the transform length as $N=2^n$. A radix-two FFT has $n$ stages, and each stage partitions its $N$ values into $N/2$ disjoint pairs. Each pair produces two outputs by one butterfly. Consequently the complete count is $n(N/2)=n2^{n-1}$. Counting output nodes instead would give $nN$, twice as many. The zero-stage transform at $N=1$ requires zero butterflies; positive indices give the stated integer expression. In one ordinary butterfly, a twiddle product is used in both a sum and a difference. Therefore its arithmetic cost includes operations beyond a single multiplication. Some twiddle factors are special values such as one, but optimizing those products does not remove the pair's butterfly from the defined count.

$$Q_n=n2^{n-1}.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $1024$, so option 4 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $2048$, rather than the derived value $1024$. Option 2 gives $255$, rather than the derived value $1024$. Option 3 gives $64$, rather than the derived value $1024$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 35

**Derive the mechanism and the exact measure.** Write the transform length as $N=2^n$. A radix-two FFT has $n$ stages, and each stage partitions its $N$ values into $N/2$ disjoint pairs. Each pair produces two outputs by one butterfly. Consequently the complete count is $n(N/2)=n2^{n-1}$. Counting output nodes instead would give $nN$, twice as many. The zero-stage transform at $N=1$ requires zero butterflies; positive indices give the stated integer expression. In one ordinary butterfly, a twiddle product is used in both a sum and a difference. Therefore its arithmetic cost includes operations beyond a single multiplication. Some twiddle factors are special values such as one, but optimizing those products does not remove the pair's butterfly from the defined count.

$$Q_n=n2^{n-1}.$$

**Check the symbolic alternatives.** Option 3 is the derived general expression. $2^n-1$ counts binary recursion-tree internal nodes rather than every stage butterfly; $n^2$ confuses the logarithmic index with the full length; $n2^n$ counts the two butterfly outputs separately. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 36

**Derive the mechanism and the exact measure.** Write the transform length as $N=2^n$. A radix-two FFT has $n$ stages, and each stage partitions its $N$ values into $N/2$ disjoint pairs. Each pair produces two outputs by one butterfly. Consequently the complete count is $n(N/2)=n2^{n-1}$. Counting output nodes instead would give $nN$, twice as many. The zero-stage transform at $N=1$ requires zero butterflies; positive indices give the stated integer expression. In one ordinary butterfly, a twiddle product is used in both a sum and a difference. Therefore its arithmetic cost includes operations beyond a single multiplication. Some twiddle factors are special values such as one, but optimizing those products does not remove the pair's butterfly from the defined count.

$$Q_n=n2^{n-1}.$$

**Apply the boundary statement.** The correct statement makes normalization and sign conventions part of correctness. With forward positive exponents, the inverse uses negative exponents and a single division by $N$. Using the same sign without a correction reverses indices rather than generally recovering the input. Omitting normalization scales recovered coefficients by $N$. Butterfly counts are arithmetic counts; they are not automatically bit-operation counts when precision or coefficient width grows. Thus option 2 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 37

**Derive the mechanism and the exact measure.** There are $2n+1$ full groups of five and all keys are distinct. Order their group medians. The chosen median of medians has exactly $n$ smaller group medians. In each corresponding group, the median and its two smaller keys are all strictly below the pivot, certifying three keys per group. The pivot's own group contributes its two smaller keys. Hence at least $3n+2$ keys are strictly below it. These contributions come from disjoint groups and exclude the pivot itself. The same argument certifies $3n+2$ strictly larger keys. Tightness is possible by placing the two unguaranteed keys in every smaller-median group above the pivot, and every key of the larger-median groups above it, with distinct values maintaining each group order.

$$Q_n=3n+2.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $17$, so option 2 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $18$, rather than the derived value $17$. Option 3 gives $6$, rather than the derived value $17$. Option 4 gives $25$, rather than the derived value $17$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 38

**Derive the mechanism and the exact measure.** There are $2n+1$ full groups of five and all keys are distinct. Order their group medians. The chosen median of medians has exactly $n$ smaller group medians. In each corresponding group, the median and its two smaller keys are all strictly below the pivot, certifying three keys per group. The pivot's own group contributes its two smaller keys. Hence at least $3n+2$ keys are strictly below it. These contributions come from disjoint groups and exclude the pivot itself. The same argument certifies $3n+2$ strictly larger keys. Tightness is possible by placing the two unguaranteed keys in every smaller-median group above the pivot, and every key of the larger-median groups above it, with distinct values maintaining each group order.

$$Q_n=3n+2.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $26$, so option 1 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 2 gives $9$, rather than the derived value $26$. Option 3 gives $40$, rather than the derived value $26$. Option 4 gives $27$, rather than the derived value $26$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 39

**Derive the mechanism and the exact measure.** There are $2n+1$ full groups of five and all keys are distinct. Order their group medians. The chosen median of medians has exactly $n$ smaller group medians. In each corresponding group, the median and its two smaller keys are all strictly below the pivot, certifying three keys per group. The pivot's own group contributes its two smaller keys. Hence at least $3n+2$ keys are strictly below it. These contributions come from disjoint groups and exclude the pivot itself. The same argument certifies $3n+2$ strictly larger keys. Tightness is possible by placing the two unguaranteed keys in every smaller-median group above the pivot, and every key of the larger-median groups above it, with distinct values maintaining each group order.

$$Q_n=3n+2.$$

**Check the symbolic alternatives.** Option 4 is the derived general expression. $n+1$ counts group medians rather than all certified original keys; $5n$ assumes every member of a smaller-median group is smaller than the pivot; $3n+3$ mistakenly includes the pivot as a strictly smaller key. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 40

**Derive the mechanism and the exact measure.** There are $2n+1$ full groups of five and all keys are distinct. Order their group medians. The chosen median of medians has exactly $n$ smaller group medians. In each corresponding group, the median and its two smaller keys are all strictly below the pivot, certifying three keys per group. The pivot's own group contributes its two smaller keys. Hence at least $3n+2$ keys are strictly below it. These contributions come from disjoint groups and exclude the pivot itself. The same argument certifies $3n+2$ strictly larger keys. Tightness is possible by placing the two unguaranteed keys in every smaller-median group above the pivot, and every key of the larger-median groups above it, with distinct values maintaining each group order.

$$Q_n=3n+2.$$

**Apply the boundary statement.** The correct statement retains distinctness and full-group size. Incomplete groups may contribute fewer certified neighbors. A group median below the pivot has three guaranteed smaller keys, not all five. The pivot's own group contributes two strictly smaller keys, while a third would include the pivot illegally. Equal keys would require a three-way partition and separate strict-count reasoning. The guarantee is a lower count, not an assertion that every input has exactly that many below-pivot keys. Thus option 3 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 41

**Derive the mechanism and the exact measure.** A perfect binary search tree with $2^n-1$ stored keys has $n$ nonempty depths, numbered zero through $n-1$. An unsuccessful search follows exactly one child per visited nonempty node. It therefore visits one stored-key node at each of those $n$ depths, then enters an empty child at depth $n$. The requested measure includes that terminal invocation, so the total is $n+1$. Equivalently, visited-call count has $V_0=1$ for an empty tree and $V_n=1+V_{n-1}$ for one unsuccessful descent, giving the same expression. This is not a traversal of every stored node. At zero tree height, the empty base still contributes one call but performs no stored-key comparison.

$$Q_n=n+1.$$

**Evaluate the requested parameter.** At $n=5$, the exact count is $6$, so option 2 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 1 gives $25$, rather than the derived value $6$. Option 3 gives $5$, rather than the derived value $6$. Option 4 gives $32$, rather than the derived value $6$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 42

**Derive the mechanism and the exact measure.** A perfect binary search tree with $2^n-1$ stored keys has $n$ nonempty depths, numbered zero through $n-1$. An unsuccessful search follows exactly one child per visited nonempty node. It therefore visits one stored-key node at each of those $n$ depths, then enters an empty child at depth $n$. The requested measure includes that terminal invocation, so the total is $n+1$. Equivalently, visited-call count has $V_0=1$ for an empty tree and $V_n=1+V_{n-1}$ for one unsuccessful descent, giving the same expression. This is not a traversal of every stored node. At zero tree height, the empty base still contributes one call but performs no stored-key comparison.

$$Q_n=n+1.$$

**Evaluate the requested parameter.** At $n=8$, the exact count is $9$, so option 1 is correct. The original-size interpretation and endpoint conditions above remain part of this calculation.

Option 2 gives $8$, rather than the derived value $9$. Option 3 gives $256$, rather than the derived value $9$. Option 4 gives $64$, rather than the derived value $9$. These are numerical alternatives, so sharing a broad asymptotic class cannot make an incorrect integer acceptable. The constructive counting proof supplies the full requested domain rather than relying on this single illustration.

### Solution 43

**Derive the mechanism and the exact measure.** A perfect binary search tree with $2^n-1$ stored keys has $n$ nonempty depths, numbered zero through $n-1$. An unsuccessful search follows exactly one child per visited nonempty node. It therefore visits one stored-key node at each of those $n$ depths, then enters an empty child at depth $n$. The requested measure includes that terminal invocation, so the total is $n+1$. Equivalently, visited-call count has $V_0=1$ for an empty tree and $V_n=1+V_{n-1}$ for one unsuccessful descent, giving the same expression. This is not a traversal of every stored node. At zero tree height, the empty base still contributes one call but performs no stored-key comparison.

$$Q_n=n+1.$$

**Check the symbolic alternatives.** Option 4 is the derived general expression. $n$ omits the final empty-subtree invocation; $2^n$ counts a whole depth or all tree capacity instead of a single search path; $n^2$ multiplies path length by an unrequested extra factor. Every discarded expression changes the measured objects, omits a specified contribution, or uses the wrong index domain. The expression is proved by the stated combinatorial or recursive mechanism, rather than extrapolated from two evaluated instances. Always restore original input size before interpreting a logarithmic stage parameter as a running-time exponent.

### Solution 44

**Derive the mechanism and the exact measure.** A perfect binary search tree with $2^n-1$ stored keys has $n$ nonempty depths, numbered zero through $n-1$. An unsuccessful search follows exactly one child per visited nonempty node. It therefore visits one stored-key node at each of those $n$ depths, then enters an empty child at depth $n$. The requested measure includes that terminal invocation, so the total is $n+1$. Equivalently, visited-call count has $V_0=1$ for an empty tree and $V_n=1+V_{n-1}$ for one unsuccessful descent, giving the same expression. This is not a traversal of every stored node. At zero tree height, the empty base still contributes one call but performs no stored-key comparison.

$$Q_n=n+1.$$

**Apply the boundary statement.** The correct statement counts work in an empty-key base case. A successful search can terminate at a stored key and need not reach an empty subtree. Call count is different from the number of stored nodes and from the number of stored-key comparisons. An empty invocation can check its base condition and return absence without comparing a data key. These distinctions matter for exact counts even though all successful and unsuccessful path bounds are logarithmic in tree size. Thus option 3 is correct. A mathematical guarantee applies only under its explicitly stated contract. Changing the coefficient domain, execution policy, terminal count or equality convention requires checking the proof again instead of assuming the same exact expression.

### Solution 45

**Evaluate the polynomial at the actual powers of the root.** Work in the field modulo seventeen. The element $\omega=4$ has order four: its square is $16\equiv-1$, its fourth power is one, and neither its first nor its second power is one. Its successive powers at indices zero through three are $1,4,16,13$.

The coefficient array $[1,2,0,0]$ represents $A(x)=1+2x$. Under the positive-exponent forward convention, $Y_j=1+2\omega^j$ modulo seventeen. Therefore
$$Y=(3,9,16,10).$$
The third raw value is $1+2\cdot16=33\equiv16$, while the fourth is $1+2\cdot13=27\equiv10$. Option 1 is correct.

Option 2 swaps the second and fourth evaluations; it is the result of using the inverse root $4^{-1}\equiv13$ without changing the forward-sign specification. Option 3 simply returns the coefficient representation and never performs evaluation. Option 4 has numerical errors in every nonconstant evaluation; for example, at root four the value is nine, not eight.

An inverse check uses root thirteen and normalization by $4^{-1}\equiv13$. The orthogonality sum of the fourth roots is zero except for matching exponents, where it is four. Thus the negative-exponent transform multiplied by thirteen recovers the original four coefficients. The modulus is prime, four divides its multiplicative-group order sixteen, and four is invertible, satisfying the field conditions. This exact modular computation has no floating-point rounding, but its values remain residues rather than unrestricted signed integers.

### Solution 46

**Enumerate all integer lifts inside the stated range.** A residue of seven modulo seventeen means the exact coefficient has form $c=7+17t$ for integer $t$. Intersect it with the closed allowed range:
$$-10\le7+17t\le10,\qquad-17\le17t\le3.$$
Hence the only admitted integers are $t=-1$ and $t=0$, giving $c=-10$ and $c=7$. Both endpoints satisfy their congruence: $-10-7=-17$ is divisible by seventeen. Option 3 is correct; uniqueness fails.

Option 1 ignores the allowed negative representative. Option 2 ignores the allowed nonnegative representative. Option 4 is contradicted by either explicit lift. Choosing a preferred canonical residue does not establish which integer coefficient actually occurred. Both are compatible with all given information.

The general sufficient uniqueness rule follows from differences. If two candidate coefficients lie in $[-B,B]$, their difference has absolute value at most $2B$. If both agree modulo a reconstruction modulus $M>2B$, the difference is a multiple of $M$ with magnitude below $M$, so it must be zero. Here $M=17$ fails that inequality because $2B=20$. A modulus of twenty-one already separates every integer in this particular interval; modular-transform applicability may impose additional prime and root-order requirements.

For multiple coprime transform moduli, use their product as the reconstruction modulus and retain the proven absolute coefficient bound. Exact modular arithmetic alone is insufficient: it can return a perfectly accurate residue that admits multiple ordinary integer lifts. The question tests reconstruction information, not the accuracy of a modular FFT implementation.
