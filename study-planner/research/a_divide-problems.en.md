### Problem 1 — State a complete sorting contract

**Question.** A routine returns a nondecreasing list after recursively sorting two halves. What else must its correctness proof establish?

**Solution.** First require the output length and multiplicities to match the input: returning an empty list would otherwise satisfy nondecreasing order. Next distinguish ordinary sorting from stable sorting. If records carry equal keys and different identities, stability preserves their input order. In the induction, assume both child contracts, prove merge emits exactly their consumed records, and prove the next emitted head is a minimum of the remaining records. Taking the left head on equality establishes the cross-half part of stability. Base cases of length zero and one satisfy all three properties directly.

### Problem 2 — Repair a nonterminating search

**Question.** A lower-bound implementation sets the lower boundary to the midpoint when the middle value is too small. Give a counterexample and the repair.

**Solution.** Take one item equal to two and target three. The interval is initially from zero to one, and its midpoint is zero. Setting the lower boundary to zero changes nothing, so the loop repeats forever. The middle position has already been proved too small and must be excluded. Set the lower boundary to the midpoint plus one. The new interval is strictly shorter; after this update it is empty, and returning length one correctly signals that no array position meets the target.

### Problem 3 — Duplicate-aware lower bound

**Question.** Find lower bounds in $(1,3,3,3,7)$ for targets three, four and eight.

**Solution.** For three, move the upper boundary left whenever the middle value is at least three. The final boundary is index one, the first three. For four, the three-valued positions are too small and are excluded; the final boundary is index four, whose value is seven. For eight, every position is too small, so the final boundary is five. That last result is a valid insertion position but cannot be indexed. A membership routine checks both that the result is less than five and that its value equals the target.

### Problem 4 — A fixed point needs distinct integers

**Question.** Given sorted distinct integers at one-based positions, design a logarithmic test for a position whose value equals its index. Why is distinctness important? This is an independently authored variant of Berkeley exercise 2.17.

**Solution.** Define the middle discrepancy as its value minus its index. Distinct sorted integers increase by at least one, so discrepancies are nondecreasing. A negative middle discrepancy excludes every earlier position; a positive discrepancy excludes every later position. Zero is a witness. Binary search therefore suffices. With duplicates, discrepancies can decrease: values $(2,2)$ give discrepancies one and zero. A positive discrepancy at the first position would incorrectly discard the second fixed point. The monotonicity proof, rather than sortedness alone, justifies the search.

### Problem 5 — Unknown sorted-array length

**Question.** A read outside a sorted array returns positive infinity. Find a target without knowing the length. Source family: Berkeley exercise 2.16.

**Solution.** Inspect positions growing as one, two, four, eight and so on until a value is at least the target or the out-of-range marker is observed. The last two inspected positions bracket any first occurrence, because all positions up to the smaller bracket were too small. Perform lower-bound search inside the bracket, using the same marker policy. Doubling reaches the bracket in logarithmically many probes in its position, and the bracket search is also logarithmic. Finally verify the returned value equals the target. The marker must be distinguishable from a legal data value if that value could itself be infinite.

### Problem 6 — Stable equality has a visible consequence

**Question.** The left run contains equal-key records tagged A and B, and the right run contains a record tagged C with the same key. What happens under strict versus nonstrict left comparison?

**Solution.** A strict comparison rejects the left head when the keys tie, so C is emitted before A and B. The result is sorted, but the original cross-half order is lost. A nonstrict left comparison emits A, then B, then C. Child stability preserves A before B, while the parent equality rule preserves both before C. Thus changing one comparison repairs a specific contract, not merely presentation. Source family: MIT's merge stability exercise.

### Problem 7 — Locally stable merges can compose badly

**Question.** Put three equal tagged items A, B and C into a queue. Repeatedly remove two runs, merge them stably and append the result. Is the final order guaranteed stable?

**Solution.** The first merge makes run AB and appends it after C, leaving queue C, AB. The next merge treats C as its left run; left-on-equality emits CAB. Every individual merge was stable with respect to its supplied run order, but that run order no longer matches the original sequence. Repair the overall algorithm by merging adjacent contiguous original runs, as in bottom-up merge sort, or attach original indices and compare them as secondary keys. Do not infer a global invariant from a local rule without checking composition.

### Problem 8 — Compute strict inversions

**Question.** Count inversions in $(3,1,2,1)$, including duplicate handling.

**Solution.** The first three forms three inversions, with the later one, two and one. The middle two forms one inversion with the final one. The earlier one forms none with the equal final one. Therefore the count is four. A recursive split into $(3,1)$ and $(2,1)$ contributes one inversion in each child. Merging sorted runs $(1,3)$ and $(1,2)$ takes the left one on equality, then the right one adds one remaining left item, and the right two adds one more. The total is $1+1+2=4$.

### Problem 9 — Count the diagram's cross inversions

**Question.** Merge left run $(2,4,7)$ and right run $(1,4,6)$ and count only crossing inversions.

**Solution.** The right one is smaller than all three remaining left items, contributing three. The left two is then emitted. On the two fours, emit the left four without adding a strict inversion. The right four is smaller than the remaining seven and contributes one. The right six is also smaller than that seven and contributes one. The total is five, and the merged run is $(1,2,4,4,6,7)$. This step-by-step count also checks the diagram: both right four and right six must be charged; omitting the former is a common duplicate-related mistake.

### Problem 10 — Maximum count and counter width

**Question.** What is the largest possible strict inversion count for a length-$n$ array? When is it attained?

**Solution.** There are $n(n−1)/2$ index pairs with the earlier index smaller. No inversion count can exceed that number. A strictly decreasing sequence makes every such pair an inversion and attains the bound. Equal values prevent their pair from being a strict inversion, so a merely nonincreasing sequence with duplicates need not attain it. This quadratic-sized result explains why a counter needs more range than a single index; determine the largest supported array length before selecting a fixed-width integer type.

### Problem 11 — Balanced multiway merge

**Question.** Merge $k$ sorted runs, each of length $n$. Compare sequential accumulation with a balanced merge tree. Source family: Berkeley exercise 2.19.

**Solution.** Sequential accumulation merges lengths two runs, three runs, and so on. Output work is proportional to $n(2+3+⋯+k)=Θ(nk^2)$ for $k≥2$. In a balanced tree, each item is processed at most logarithmically many levels, and total work per level is at most $kn$. The cost is $Θ(kn log k)$ for balanced nonempty runs. Odd run counts can carry one run forward unchanged. Stability is retained if adjacent original runs are merged in their original order. A heap-based merge is another logarithmic-per-item strategy, but is a different representation.

### Problem 12 — Why sorting deduplicates efficiently

**Question.** Remove duplicate numeric values in linear-logarithmic time. Source family: Berkeley exercise 2.14.

**Solution.** Sort the values first. Equal values become contiguous because no distinct intermediate ordered value can lie between two equal values. Scan once, emit the first item of each equal-value block and skip the rest. Sorting costs linear-logarithmic work and the scan is linear. If the required output preserves first occurrence order, this simple sorted output violates the contract. Retain original indices, identify the earliest record in each equal block and then restore index order, or use a suitable dictionary with its stated computational assumptions.

### Problem 13 — All-negative maximum subarray

**Question.** Find the nonempty maximum subarray of $(-7,-2,-5)$ and explain the zero-initialization error.

**Solution.** Singleton sums are negative seven, negative two and negative five; longer intervals are even smaller than their largest included singleton. The best interval is the second item, with sum negative two. An algorithm initialized to zero and updated only on a larger sum never changes its answer, implicitly returning an empty interval. For the nonempty specification, initialize from the first item or use negative infinity before evaluating actual candidates. The recursive singleton summary is the value in all four components, so this policy is preserved throughout combination.

### Problem 14 — A crossing interval

**Question.** Split $(4,-6,8,-2,3,-9,5)$ after its first three items. Compute the four-component summaries and the best interval.

**Solution.** The left total is six, its best prefix is six, its best suffix is eight, and its best internal interval is eight. The right total is negative three, its best prefix is one, its best suffix is five, and its best interval is five. The crossing candidate is $8+1=9$, produced by $(8,-2,3)$. The parent summary is $(3,7,5,9)$: the prefix uses all left plus the best right prefix; the suffix stays in the right half. The best half-open interval is from index two to index five.

### Problem 15 — Show that the best value is insufficient

**Question.** Give two left segments with the same best internal sum but different effects when followed by $(3)$.

**Solution.** Choose $(5,-100)$ and $(-100,5)$. Both have best internal sum five. Their best suffix sums are negative ninety-five and five respectively. Appending three gives a best value of five in the first concatenation and eight in the second. An algorithm receiving only the child's best value sees indistinguishable child answers but must produce different parent answers. Therefore no combination rule based solely on those values can solve this specification. Returning the suffix, prefix and total restores the missing information.

### Problem 16 — Associativity is not commutativity

**Question.** Why can a summary tree regroup consecutive segments but not reorder them?

**Solution.** Both groupings of three consecutive segments summarize exactly the same concatenated sequence. Each summary component is uniquely defined by that sequence, so the results coincide. Reordering changes the sequence. For instance, $(5,-100)$ has best prefix five and best suffix negative ninety-five, whereas $(-100,5)$ has those values reversed. These are different summaries. A range query may regroup ordered pieces to obtain balanced evaluation but must preserve their left-to-right order. This gives a proof of associativity without claiming that arbitrary permutations are legal.

### Problem 17 — Count summary combinations exactly

**Question.** A summary recursion stops at singletons and always splits into two nonempty pieces. How many combinations are executed for eleven items?

**Solution.** There are eleven leaf calls. In a full binary tree, if there are $I$ internal nodes, there are $2I$ parent-child edges. Any finite tree with $I+11$ nodes has $I+10$ edges, so $2I=I+10$ and $I=10$. Each internal call performs one constant-size summary combination. The result holds for unequal leaf depths and does not require eleven to be a power of two. Copying slices at every call would introduce extra work beyond those ten combinations.

### Problem 18 — Recover witnesses under ties

**Question.** For $(2,-2,2)$, choose a maximum interval by greater sum, earlier start and then earlier end.

**Solution.** Maximum sum two is attained by the first singleton, the last singleton and the full array. The earliest start is zero, leaving the first singleton and full array. The earlier end is one, so the selected half-open interval is $[0,1)$. Store these same endpoints in every candidate and use the same comparison order at every combine. Comparing only sums at one level and preferring a shorter interval at another can produce inconsistent results. The laboratory's independent enumeration follows the declared start-then-end policy.

### Problem 19 — Derive Kadane for nonempty intervals

**Question.** Derive the update for the best interval ending at each position.

**Solution.** Any nonempty interval ending at the current item either consists only of that item or extends an interval ending at the previous item. Among extensions, the best uses the previous best ending sum. Therefore update that sum to the maximum of the current value and the previous ending sum plus the current value. Track the maximum ending sum seen so far. Initialize both quantities to the first value, which correctly handles an all-negative array. This derivation uses an exhaustive two-case classification and explains why the familiar reset-to-zero version solves a different policy.

### Problem 20 — Rank splitting with equal x-coordinates

**Question.** Six points all have x-coordinate zero and different y-coordinates. What goes wrong with sending points left only when their x-coordinate is below the median x-coordinate?

**Solution.** The median x-coordinate is zero. No point satisfies a strict less-than test, so the left child is empty and the right child receives all six points. Recursing on that right child does not reduce the instance. Instead, split the sorted x-order by rank into two groups of three, using IDs to define membership. The geometric divider still weakly separates their x-coordinates. Partition the y-order by membership, not by a new numeric coordinate test, so each child receives exactly its assigned records.

### Problem 21 — Why one point per uncolored cell is false

**Question.** The closest distance inside each half is ten. Can opposite-half points be only one tenth apart?

**Solution.** Yes. Place one left point at $(-0.05,0)$ and one right point at $(0.05,0)$, with other same-half points far away. Their distance is one tenth, while both child closest distances can be ten or larger. Therefore the strip's complete set is not ten-separated. The packing argument instead permits at most one left point per left cell and at most one right point per right cell of sufficiently small diameter. Keeping these two guarantees separate yields the eight-point window bound and seven-successor scan.

### Problem 22 — Prove the strip restriction

**Question.** A cross-half pair has distance smaller than the current child minimum. Why do both endpoints lie in the strip?

**Solution.** Let the dividing x-coordinate be $c$, with the left endpoint at or left of it and the right endpoint at or right of it. If the left endpoint is at least the child minimum away from $c$, its horizontal distance from every right endpoint is at least that minimum. Euclidean distance is at least horizontal distance, contradicting an improvement. The same reasoning applies to the right endpoint. Thus both horizontal offsets are strictly smaller than the current child minimum. Ties need not be newly found because a child witness already attains the existing value.

### Problem 23 — Presorting changes the recurrence

**Question.** Compare sorting the strip by y at every call with maintaining y-order from preprocessing. Source family: Berkeley exercise 2.32.

**Solution.** Sorting at each call incurs an upper toll proportional to input size times its logarithm, leading to a linear-times-log-squared upper bound across the recursion tree. Presort all points once by y and filter into child memberships; filtering preserves the order in linear time. Building the parent strip from that same ordered list is also linear. The recursive toll then becomes linear, giving a linear-logarithmic bound overall, including the initial sorts. The improvement comes from eliminating repeated representation construction, not from changing the seven geometric candidates.

### Problem 24 — Duplicate coordinates and output IDs

**Question.** Point records numbered zero and three share coordinates $(2,5)$. What should the closest-pair routine return?

**Solution.** They are distinct records and form a legal pair with squared distance zero. Euclidean squared distances are nonnegative, so this result is globally optimal without recursion. Sorting by coordinates places duplicates adjacent and lets preprocessing detect them. Return the two distinct record IDs, not two copies of a coordinate tuple that obscure record identity. If a different problem instead asks for distinct coordinate locations, duplicates must be removed under that explicit specification; silently doing so changes the input problem.

### Problem 25 — Shrinking the strip distance during scanning

**Question.** Can finding a better pair during strip scanning invalidate the original seven-successor limit?

**Solution.** No. The original child minimum provides a window with at most eight eligible points, including the current point. A smaller current best distance makes the potentially improving vertical window a subset of that original window. It cannot introduce more candidates. Keeping the strip built using the original distance is harmless because it is a superset; the updated vertical stopping check filters out unnecessary work. The algorithm may retain its fixed seven-successor limit, although the implementation must not make a larger distance replace a smaller one.

### Problem 26 — Account for squared-distance overflow

**Question.** Why does using squared distances remove one numerical issue but not every arithmetic issue?

**Solution.** For exact integer coordinates, comparing squared distances avoids square-root approximation and preserves distance order because squaring is strictly increasing on nonnegative numbers. However, coordinate differences, their squares and their sum can exceed a fixed-width type. For example, two individually representable coordinates near opposite extremes can have an unrepresentable difference. Use a sufficiently wide exact type or arbitrary-precision arithmetic. That choice affects bit complexity; the real-RAM or bounded-integer constant-cost analysis must be stated separately.

### Problem 27 — Reconstruct an odd-width product

**Question.** Use a one-digit decimal split to multiply 123 by 45.

**Solution.** The high/low pairs are $(12,3)$ and $(4,5)$. Compute high-high forty-eight, low-low fifteen and the difference product $(12−3)(4−5)=−9$. The middle coefficient is seventy-two. With low width one, the high coefficient is shifted by two decimal digits and the middle by one, yielding $4800+720+15=5535$. Shifting the high coefficient by three because one operand originally had three digits would be wrong. This directly checks that the radix shift follows the low width, not an assumed even total width.

### Problem 28 — A signed difference product

**Question.** Multiply 37 by 25 using the difference variant, then obtain negative 37 times 25.

**Solution.** With one decimal low digit, the parts are $(3,7)$ and $(2,5)$. The products are six, thirty-five and $(-4)(-3)=12$. The mixed coefficient is $6+35−12=29$. Recombining gives $600+290+35=925$. The outer input signs differ for the signed problem, so negate the unsigned result to obtain negative nine hundred twenty-five. The difference signs belong to the internal identity; they are separate from the outer input sign.

### Problem 29 — Why difference operands stay small

**Question.** High and low parts each fit in at most $r$ binary bits. Prove their absolute difference also fits, and compare their sum.

**Solution.** Both values lie between zero and $2^r−1$. Their absolute difference is at most $2^r−1$, so it has at most $r$ bits. Their sum may reach $2^{r+1}−2$, requiring $r+1$ bits. Thus a sum-based Karatsuba recurrence cannot literally assign every third call width $r$ without qualification. Difference-based recursion avoids this extra operand bit, while subtraction and sign handling remain linear-size overhead. The two valid variants have the same standard exponent after appropriate rounding analysis.

### Problem 30 — Why three products change the exponent

**Question.** Explain the asymptotic improvement from four to three half-width recursive products.

**Solution.** A regular four-branch recursion has about four to the depth leaves. At depth logarithmic base two in the width, this is quadratic in the width. Three branches instead produce width to the power logarithm base two of three leaves. Linear internal tolls are dominated by this larger-than-one but smaller-than-two exponent, giving the standard subquadratic bound. The algebraic identity is what permits deleting one product; simply deciding to omit a needed term would make the algorithm incorrect. The statement counts bit work with linear additions, not unit-cost arbitrary-length multiplication.

### Problem 31 — Multiplication and squaring reductions

**Question.** Could general integer multiplication have a strictly larger asymptotic exponent than exact integer squaring? Source family: Berkeley exercise 2.26.

**Solution.** Use the identity $2xy=(x+y)^2−x^2−y^2$. Three squarings of at most a constant additive increase in input bit width, plus linear-size arithmetic and exact division by two, compute a product. Conversely, multiplication computes a square by supplying the same operand twice. Under regular bit-cost bounds these reductions show that squaring and multiplication cannot have different polynomial exponents solely because the two operands coincide. Particular implementations can still have different constants and practical thresholds.

### Problem 32 — Convert a decimal number recursively

**Question.** A decimal digit string is split into high and low substrings of low length $m$. What exact recombination is required? Source family: Berkeley exercise 2.25.

**Solution.** Convert both substrings recursively into binary integers, then form the high integer times $10^m$ plus the low integer. The power may be computed by repeated squaring or shared preprocessing. The low length, including leading zero digits, controls the exponent. To claim a running-time bound, charge both the large multiplication and the construction of the power; treating conversion's arithmetic as constant time would hide the expensive work. The equation is exact even when the high and low substrings have different lengths.

### Problem 33 — Calculate all Strassen products

**Question.** Multiply the two matrices in the main lesson using its fixed seven-product convention.

**Solution.** Substitute $A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8$. The products are $P_1=−2$, $P_2=24$, $P_3=35$, $P_4=8$, $P_5=65$, $P_6=−30$ and $P_7=−22$. Then the output entries are $65+8−24−30=19$, $−2+24=22$, $35+8=43$ and $−2+65−35+22=50$. Ordinary row-column multiplication gives the same four values. This verifies the convention; importing a recombination formula from a differently numbered presentation could produce errors even though both presentations are individually correct.

### Problem 34 — Exhibit noncommuting blocks

**Question.** Why may a scalar shortcut fail on matrix blocks? Give exact two-by-two witnesses.

**Solution.** Let $U$ have rows $(0,1),(0,0)$ and $V$ have rows $(0,0),(1,0)$. Their product $UV$ has rows $(1,0),(0,0)$, while $VU$ has rows $(0,0),(0,1)$. Therefore they differ. Any block derivation replacing one ordered product by its reversal is invalid on these blocks. Strassen's proof avoids this: distributivity expands each ordered product, and additive cancellation removes exactly matching terms without swapping factors.

### Problem 35 — Padding a dimension of ten

**Question.** How does recursive square-matrix multiplication handle dimension ten, and how much can power-of-two padding increase the dimension?

**Solution.** Pad both inputs to dimension sixteen with zero rows and columns. The upper-left ten-by-ten block of the product is the required result because padded positions contribute zero to every relevant dot product. The next power of two is less than twice any positive original dimension that is not already a power of two. Therefore raising the dimension to a fixed exponent changes work by at most a constant factor. This reasoning does not justify padding a very skinny rectangular matrix to an enormous square without comparing dimensions.

### Problem 36 — Matrix squaring without commutativity

**Question.** A five-product scalar formula for squaring a two-by-two matrix is recursively applied to matrix blocks. Why is its scalar proof insufficient? Give a safe reduction showing multiplication can be obtained from squaring. Source family: Berkeley exercise 2.27.

**Solution.** Scalar derivations can combine terms using commuting off-diagonal products. Matrix blocks need not commute, so the recursive step lacks its necessary identity. For a safe reduction, form the block matrix with top row blocks $(0,X)$ and bottom row blocks $(Y,0)$. Squaring it gives diagonal blocks $XY$ and $YX$, with zero off-diagonal blocks. Thus one square of twice the dimension contains the desired product. A fixed dimension doubling preserves a regular polynomial exponent. The reduction uses ordered block multiplication and introduces no commutativity assumption.

### Problem 37 — An invalid semiring transfer

**Question.** Can Strassen's additions and subtractions be used unchanged for shortest-path min-plus products?

**Solution.** In min-plus arithmetic, the operation corresponding to addition is minimum and multiplication is ordinary addition. There is no additive inverse for minimum that supplies the required subtraction identities. Consequently the cancellation proof fails before any recurrence is considered. Ordinary block decomposition still has an appropriate semiring meaning, but the seven-product ring identity does not automatically carry over. The allowed algebraic operations are part of the algorithm's precondition, just as sortedness is part of binary search's precondition.

### Problem 38 — Distinguish degree from coefficient count

**Question.** Multiply coefficient arrays of lengths three and four. What output length and radix-two transform size suffice?

**Solution.** The degrees are at most two and three, so the product degree is at most five and the coefficient count is at most six. Choose the next power of two at least six, which is eight. Pad both inputs to length eight, multiply their transforms pointwise and invert. Using a transform size based only on the larger input length, four, would permit high-degree coefficients to wrap modulo $x^4−1$. Leading zero coefficients can lower the actual degree but do not invalidate the safe length-based bound.

### Problem 39 — Primitive versus nonprimitive roots

**Question.** Why is using one as a fourth root of unity invalid for a length-four transform?

**Solution.** One does satisfy its fourth power equals one, but its order is one. Every evaluation point would then be the same point one. Each output is the sum of the four coefficients, so distinct polynomials with equal coefficient sums become indistinguishable. The resulting matrix has identical rows and is not invertible. Choose a primitive fourth root, such as the imaginary unit, whose powers are one, the imaginary unit, negative one and negative imaginary unit. Distinctness is necessary for interpolation and the inverse proof.

### Problem 40 — A four-point transform by hand

**Question.** Compute the positive-exponent transform of coefficients $(1,2,3,4)$.

**Solution.** Use the primitive root equal to the imaginary unit. At one, evaluation is ten. At the imaginary unit, the value is $1+2i−3−4i=−2−2i$. At negative one it is $1−2+3−4=−2$. At negative imaginary unit it is $1−2i−3+4i=−2+2i$. Thus the output is $(10,-2-2i,-2,-2+2i)$. For real coefficients, the two nonreal outputs are conjugates. Applying the opposite-exponent transform and dividing by four returns the original coefficients.

### Problem 41 — Circular convolution is a different answer

**Question.** Explain exactly why a length-two transform of $(1,1)$ times itself yields $(2,2)$.

**Solution.** Ordinary multiplication yields coefficients $(1,2,1)$. At second roots of unity, the relation $x^2=1$ holds. Therefore the highest coefficient folds into the constant coefficient: one plus one becomes two, and the linear coefficient remains two. The inverse transform is correctly recovering a circular convolution for its chosen length. The error is choosing a representation incapable of distinguishing the required product, not a failure of the transform identities. Padding to length four prevents this fold.

### Problem 42 — Prove the orthogonality sum

**Question.** For a primitive root of order $N$, evaluate the sum of its powers weighted by a nonzero exponent modulo $N$.

**Solution.** Let the ratio be $r=ω^q$, where $q$ is not zero modulo $N$. Primitivity ensures $r≠1$, while $r^N=1$. The finite geometric identity gives $(1+r+⋯+r^{N−1})(1−r)=1−r^N=0$. Over the complex numbers, the nonzero factor $1−r$ can be divided out, so the sum is zero. For exponent zero modulo $N$, every term is one and the sum is $N$. These two cases give the inverse transform and its single normalization factor.

### Problem 43 — Exact transform modulo seventeen

**Question.** Justify an eight-point number-theoretic transform using root two modulo seventeen.

**Solution.** The successive power facts needed are $2^2=4$, $2^4=16≡−1$ and $2^8≡1$. The only proper divisors of eight are one, two and four, none of which gives one. Hence the order is eight. Eight is invertible modulo seventeen because $8⋅15=120≡1$. The inverse uses the inverse root, nine, and normalization fifteen. All operations are exact in the field, but the recovered coefficients are residues modulo seventeen. Integer recovery needs an independent magnitude bound or additional moduli.

### Problem 44 — Prove the coefficient recovery bound

**Question.** Both input coefficient magnitudes are at most $C$, and their lengths are $m$ and $k$. Give a sufficient modular-reconstruction bound.

**Solution.** Any output coefficient sums at most the smaller of the two lengths many products. Each product has absolute value at most $C^2$. Thus every coefficient has magnitude at most $D=min(m,k)C^2$. Choose an odd combined modulus larger than $2D$. Each true signed coefficient then has a unique representative in the centered interval of that modulus, so Chinese remainder reconstruction identifies it. The chosen transform lengths and primitive roots must still exist for every modulus. The size bound alone does not supply a valid transform.

### Problem 45 — A fast Hadamard transform

**Question.** A recursively defined matrix has block rows $(H,H)$ and $(H,-H)$. Multiply it by a vector in linear-logarithmic arithmetic work. Source family: Berkeley exercise 2.28.

**Solution.** Split the vector into two halves $u$ and $v$. Recursively compute $Hu$ and $Hv$. The upper output is their sum and the lower output their difference. There are two half-size matrix-vector calls and linear entrywise combination, with a scalar base case. The recurrence therefore gives linear-logarithmic work. The butterfly resembles the Fourier combine without nontrivial twiddle factors. The derivation uses the particular recursive matrix structure; a generic dense matrix-vector product does not acquire this bound simply by being split.

### Problem 46 — Bit-reversal indices

**Question.** Derive the length-eight bit-reversal permutation from the parity recursion.

**Solution.** Write indices with three binary bits. Recursively separating even and odd indices chooses the low bit first, then the next bit, then the high bit. Reading those choices in root-to-leaf order reverses the original bit significance. The original three-bit indices map to the sequence zero, four, two, six, one, five, three, seven. Applying the reversal twice returns the original index, because reversing a bit string is an involution. The permutation depends on index width; omit leading zero bits and the mapping becomes wrong.

### Problem 47 — A majority candidate must be verified

**Question.** Pair equal values and retain one representative; discard unequal pairs. Does a majority in the reduced list prove a majority in the original list? Source family: Berkeley exercise 2.23, with an explicit qualification.

**Solution.** No. Pair the original sequence $(a,a,b,c)$ as $(a,a)$ and $(b,c)$. The reduced list contains only $a$, which is a strict majority there, while $a$ occurs only twice out of four originally and is not a strict majority. The safe direction is that a true original majority survives suitable pair elimination as a candidate, with an appropriate policy for odd leftover items. Count the candidate in the original sequence before returning it. This is an example of a necessary condition being mistaken for an equivalence.

### Problem 48 — Work and span can differ

**Question.** Two half-size merge-sort calls run in parallel, but their merge remains sequential. Give work and span bounds.

**Solution.** Work sums both children and the linear merge, so it remains linear-logarithmic. Span follows only the longer child chain plus the sequential linear merge: its recurrence is $S(n)=S(n/2)+Θ(n)$. The geometric sum of decreasing merge sizes is linear, so span is linear under this parallel model. Two child calls running simultaneously do not make the parent merge constant time. A different parallel merge could improve span, but needs a separate algorithm, proof and model.
