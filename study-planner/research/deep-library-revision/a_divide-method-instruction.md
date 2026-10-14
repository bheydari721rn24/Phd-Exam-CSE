## Deeper constructions: why the combination step is sufficient

The following constructions supplement the complete preceding lesson. They connect executable invariants to proofs, representations and exact counts. Their worked examples are independently authored. The selected MIT, Berkeley, CMU and ETH written scopes are recorded at the end of this chapter; an inherited Stanford reference is retained as historical reading, not counted as a fresh review.

### Construction 1. A merge invariant proves order, stability and inversion charges

Let sorted runs occupy two adjacent intervals of the original sequence. Keep pointers $i,j$ to their first unconsumed elements and an output pointer $k$. Before every iteration, the output contains exactly the consumed elements in sorted order; every unconsumed element is at least its own run's current head. Selecting the smaller head therefore appends a smallest remaining element. The invariant is initialized by an empty output, maintained by advancing exactly the selected pointer, and terminated by exhausting one side and copying the remainder. This proves the sorted multiset contract rather than merely asserting that the recurrence has the correct order.

For stable sorting, records have a key and an identity. When heads tie, select the left record, because the left adjacent run originated earlier. Stability inside each child and this cross-run tie policy imply stability of the parent. Adjacency is essential: if arbitrary runs interleave original positions, choosing the left run on ties no longer certifies original-record order. A comparison expression using strict less-than and an unconditional right-side alternative is an instability bug, even if the resulting keys are sorted.

The same invariant counts strict cross inversions. If $R_j<L_i$, every remaining left element is at least $L_i$ and is consequently strictly greater than $R_j$. Charge exactly $|L|-i$ pairs, advance $j$, and charge none when equal heads are resolved left first. Each charged pair is unique because its right member is consumed once. Every cross inversion is charged when its right member is selected. Thus neither missed pairs nor double counting can occur.

For $L=[1,3,3]$ and $R=[2,3,4]$, consume 1 first. Selecting 2 charges the two remaining threes. Equality at 3 charges nothing, so the cross count is 2. The left and right internal inversion counts must still be added if they came from recursively sorted, originally unsorted halves. For an original sequence of length $N$, the maximum strict inversion count is $N(N-1)/2$; this can exceed a narrow integer counter even when an array index fits.

Separate key comparisons from output writes. A merge of nonempty lengths $p,q$ performs at most $p+q-1$ head comparisons and exactly $p+q$ writes into a fresh output. The last unconsumed tail needs writes but no cross-head comparisons. On a fully expanded equal-halves merge sort with $N=2^h$, the worst comparison sum is

$$M(N)=\sum_{j=0}^{h-1}(N-2^j)=hN-N+1.$$

At each depth there are $2^j$ merges with aggregate input length $N$, each saving one final comparison. Sorted input in the ordinary merge implementation instead consumes each left half immediately, giving $hN/2$ comparisons. An adaptive boundary test can skip a merge altogether, but its counts belong to a different implementation.

### Construction 2. Four values form an ordered summary algebra

For a nonempty interval $A$, define its total $S(A)$, maximum nonempty prefix $P(A)$, maximum nonempty suffix $U(A)$ and maximum nonempty subarray $B(A)$. For adjacent intervals $L,R$, every prefix is either a prefix of $L$ or all of $L$ followed by a prefix of $R$. Every suffix has the symmetric decomposition. A best interval is wholly left, wholly right, or crosses the boundary. Therefore the combination $L\star R$ is

$$S=S_L+S_R,$$
$$P=\max(P_L,S_L+P_R),$$
$$U=\max(U_R,S_R+U_L),$$
$$B=\max(B_L,B_R,U_L+P_R).$$

These equations are a correctness proof: the cases exhaust all feasible nonempty intervals, and each candidate is feasible. A scalar best value alone loses the boundary information needed for future combinations. For example, $[-1,5,-1]$ and $[5,-20,5]$ both have best value 5 but have different suffixes and totals, so appending the same interval can yield different results.

Associativity follows from semantics. Both $(L\star R)\star Q$ and $L\star(R\star Q)$ summarize the identical ordered concatenation $LRQ$, and each component is uniquely defined by that sequence. Commutativity does not follow: $[2,-3]\star[4]$ has best value 4, while $[4]\star[2,-3]$ has best value 6. A segment-tree range query may change parentheses but must preserve interval order. Store separate left and right accumulators if query fragments are encountered in different traversal orders.

An empty identity is possible using $e=(0,-\infty,-\infty,-\infty)$, with symbolic rules $a+(-\infty)=-\infty$ and $\max(a,-\infty)=a$. Do not simulate negative infinity by a finite integer without a justified bound; overflow or a sufficiently negative input can break the identity. A singleton $[x]$ has $(x,x,x,x)$ under the nonempty policy. Under an empty-allowed policy, its last three values become $\max(0,x)$, so changing only the output convention does not repair a nonempty implementation.

Store each candidate's endpoints together with its value. To return the earliest start and then earliest end among tied maxima, compare records lexicographically by value descending, start ascending and end ascending. Prefixes have a fixed start, suffixes a fixed end, and the crossing witness concatenates the chosen left suffix and right prefix. Consistent local tie decisions reconstruct a valid globally ordered witness. The tree uses $N-1$ combinations, $\Theta(N)$ work and $\Theta(\log N)$ balanced parallel span when each summary combine has constant cost.

### Construction 3. The geometric strip proof requires recursive membership

Sort points by $(x,y,\text{id})$ and divide by rank, not by an ambiguous test against a repeated x-coordinate. The left child is a specific set of identities and the right child is its complement. Partition the y-sorted list by those identities in linear time, preserving y-order. This is why tied coordinates do not unbalance the recursion or lose points.

Let $\delta$ be the smaller distance returned by the two children. If it is zero, a duplicate pair is already globally optimal and can be returned immediately. Otherwise, a cross pair with distance less than $\delta$ must place both endpoints within $\delta$ of the divider, and their y-coordinates differ by less than $\delta$. Filter this strip in y-order. Only points in a $2\delta$ by $\delta$ rectangle ahead of the current point can improve the answer.

The separation premise is within each child, not between all strip points. Subdivide each child's half of that rectangle into four half-open cells of side $\delta/2$. Two points of the same child in one cell would be less than $\delta$ apart because the cell diameter is $\delta/\sqrt2$. Thus each of the eight child-specific cells contains at most one point. Boundary ownership must be consistent; points on the divider retain their recursive identity. This yields at most seven other points after counting the current point in the rectangle. An uncolored grid crossing the divider can contain a close left-right pair in one geometric cell and cannot support the same one-point claim.

The scan is therefore linear. Combined with two balanced recursive calls, the recurrence is $T(N)=2T(N/2)+\Theta(N)$, producing $\Theta(N\log N)$ after the initial sorts. Sorting the strip at every recursive node instead introduces a $\Theta(N\log N)$ toll and yields $\Theta(N\log^2N)$. The geometry alone does not guarantee the faster bound; maintaining the representation supplies it.

For bounded integer coordinates, compare squared distances to avoid square roots, but widen before subtraction and multiplication. If each coordinate lies in $[-K,K]$, a squared distance can reach $8K^2$. Floating coordinates require a separately stated numerical policy. A drawing indicates which candidates are inspected; the cell proof establishes the bound for all admissible inputs.

### Construction 4. Karatsuba is an algebraic identity with a width contract

Choose a low-part width $m$ in radix $b$ and write $x=x_Hb^m+x_L$, $y=y_Hb^m+y_L$, with $0\le x_L,y_L<b^m$ for nonnegative operands. Define $z_2=x_Hy_H$, $z_0=x_Ly_L$ and $z_s=(x_H+x_L)(y_H+y_L)$. Expansion gives

$$z_1=z_s-z_2-z_0=x_Hy_L+x_Ly_H,$$
$$xy=z_2b^{2m}+z_1b^m+z_0.$$

The actual low width determines the shifts, including for odd input length. For 123 and 45 in decimal with $m=1$, the parts are $(12,3)$ and $(4,5)$. The three products are 48, 15 and 135; the mixed coefficient is 72, giving $4800+720+15=5535$. Replacing the shift by half of a rounded total length can silently change the represented numbers.

In the sum formulation, each sum can have one extra digit or bit. Thus the bit-cost recurrence needs a bound such as $T(n)\le3T(\lceil n/2\rceil+1)+cn$, not a literal identity involving three exact half-width products. A fixed base threshold and a shifted-size analysis preserve the familiar $O(n^{\log_2 3})$ upper bound. The ideal fixed-width complete recursion has exactly $3^h$ leaves at depth $h$, but data-dependent zero pruning or unequal operand lengths change the literal leaf count.

A difference variant computes $d=(x_H-x_L)(y_H-y_L)$ and uses $z_1=z_2+z_0-d$. The differences can be negative. Either use signed recursive multiplication correctly or separate sign and magnitude before recursion. The radix-shift identity still holds, while pretending every intermediate is unsigned can invalidate it. The faster exponent counts bit operations with linear additions and shifts; a unit-cost model that treats arbitrary-length multiplication as one operation would answer a different question.

### Construction 5. Strassen preserves product order

Let $A,B,C,D$ be the blocks of the left matrix and $E,F,G,H$ those of the right. The product blocks are $AE+BG$, $AF+BH$, $CE+DG$, and $CF+DH$. Strassen's seven products can be chosen as

$$M_1=(A+D)(E+H),\quad M_2=(C+D)E,$$
$$M_3=A(F-H),\quad M_4=D(G-E),$$
$$M_5=(A+B)H,\quad M_6=(C-A)(E+F),$$
$$M_7=(B-D)(G+H).$$

Recombine with $C_{11}=M_1+M_4-M_5+M_7$, $C_{12}=M_3+M_5$, $C_{21}=M_2+M_4$ and $C_{22}=M_1-M_2+M_3+M_6$. For example, the first expands to $AE+AH+DE+DH+DG-DE-AH-BH+BG+BH-DG-DH=AE+BG$. Every product keeps a left-input block on the left and a right-input block on the right. No commuting of blocks is used, which matters because matrix multiplication is noncommutative.

Additive inverses and distributivity are essential. Ordinary arithmetic matrices over a ring support the identities; an arbitrary semiring without subtraction does not directly support these seven-product formulas. Padding a non-power-of-two square matrix to the next power of two increases dimension by less than a factor of two; crop the final product to the original shape. This preserves asymptotic work, though it increases constants and storage.

For side $N=2^h$, the complete ideal recursion has $7^h$ scalar-product leaves and $\Theta(N^2)$ additions at each recursive node. Level $j$ contributes $N^2(7/4)^j$ additions up to a fixed factor, so lower levels dominate and total work is $\Theta(N^{\log_2 7})$. Seven multiplications at only the top level, followed by classical child multiplication, do not produce this exponent. Arithmetic operation counts also do not guarantee numerical stability or practical speed on small inputs.

### Construction 6. Fourier correctness comes from paired roots and orthogonality

For even transform length $N$, split coefficient positions into even and odd subsequences. With a primitive root $\omega$ of order $N$, write $A(x)=A_e(x^2)+xA_o(x^2)$. Since $\omega^{k+N/2}=-\omega^k$, the two evaluations are

$$Y_k=E_k+\omega^kO_k,$$
$$Y_{k+N/2}=E_k-\omega^kO_k.$$

The smaller transforms use $\omega^2$, whose order is $N/2$. This proves both the recursion and the butterfly wiring: the same even value and twiddle-scaled odd value feed two outputs with opposite signs. A root merely satisfying $\omega^N=1$ is insufficient; $\omega=1$ would repeat the same evaluation point and destroy invertibility.

Use the declared forward convention $Y_k=\sum_{j=0}^{N-1}a_j\omega^{jk}$. For a complex primitive root, the finite geometric sum $\sum_{k=0}^{N-1}\omega^{k(j-r)}$ is $N$ if $j=r$ modulo $N$ and zero otherwise. Substituting it into the inverse proves

$$a_r=\frac1N\sum_{k=0}^{N-1}Y_k\omega^{-rk}.$$

Changing the root direction without the factor $1/N$ returns a scaled result. The unnormalized Fourier matrix satisfies $F^*F=NI$, so it scales Euclidean norm by $\sqrt N$; only $F/\sqrt N$ is unitary. Do not interpret the unnormalized transform as a norm-preserving rotation.

For $N=4$ modulo prime 17, the root 4 has powers $1,4,16,13$ and order four. Coefficients $[1,2,0,0]$ transform to $[3,9,16,10]$. The even child gives $[1,1]$ and the odd child $[2,2]$. The first butterfly gives 3 and 16; the second gives 9 and 10. The inverse root is 13 and the inverse length is also 13 modulo 17. This finite-field example uses exactly defined integer operations rather than a floating approximation.

### Construction 7. Convolution requires both index and value recovery

For coefficient lengths $r,s$, the product has length at most $r+s-1$. A length-$N$ transform computes convolution modulo $x^N-1$; its coefficient at index $k$ is the sum of linear coefficients whose indices are congruent to $k$ modulo $N$. Therefore padding to $N\ge r+s-1$ prevents index wraparound. Radix-two implementations also require a power-of-two length. These are independent constraints.

Consider $[1,2,3]$ and $[4,5]$. Their linear convolution is $[4,13,22,15]$. A length-two circular convolution instead returns $[26,28]$ because coefficients 0 and 2 collide, as do 1 and 3. A modulus large enough for coefficient values cannot repair this index aliasing.

For integer inputs with $|a_i|\le A$, $|b_j|\le B$, each coefficient is bounded by $C=\min(r,s)AB$. To reconstruct signed coefficients uniquely from residues, a sufficient CRT modulus product is $M>2C$. First reconstruct in $[0,M)$, then subtract $M$ when the residue exceeds $M/2$. If $M\le2C$, distinct admissible integers can share a residue. Over an NTT prime, transform length must divide $p-1$ and the chosen root must have exactly that order; a large arbitrary modulus need not satisfy these conditions.

The bound is sufficient, not always minimal for a particular input. For the preceding nonnegative example, modulus 17 returns $[4,13,5,15]$ and cannot distinguish coefficient 22 from 5. Knowledge that the coefficient lies in $[0,30]$ still leaves both values possible. A floating FFT needs an explicit rounding-error bound below one-half per integer coefficient; small successful tests cannot establish this for arbitrary lengths and magnitudes.

### Construction 8. Pivot certificates and decision trees count different objects

Suppose $5g$ distinct keys are divided into $g=2t+1$ full groups of five. Sort each group, select its median, then select the median of those medians as pivot. At least $t$ group medians are strictly below the pivot, certifying three below-pivot keys in each such group. The pivot's own group certifies two additional below-pivot keys. Hence at least $3t+2$ keys are strictly smaller, and the same number are strictly larger. The pivot belongs to neither strict partition.

Since $5g=10t+5$, the larger strict partition is at most $(10t+5)-1-(3t+2)=7t+2$. Incomplete groups, even group counts and duplicate keys require adjusted certificates. With duplicates, a three-way partition retains the equal block and permits immediate termination when the target rank lies there. This is the certificate used here; full deterministic-selection implementation and expected-pivot analysis are treated in their dedicated chapters.

For binary search, distinguish visited calls, inspected keys and elementary comparisons. In a perfect binary search tree with $2^h-1$ stored keys, an unsuccessful path visits $h$ nonempty nodes and then one empty child: $h+1$ calls, $h$ inspected keys. A three-way key comparison costs one operation at each nonempty node; a less-than test followed by equality can cost more. The empty base call does not inspect a stored key.

For any ordered set of $N$ distinct keys, there are $N+1$ possible gaps for an unsuccessful target. A binary yes/no comparison decision tree distinguishing those gaps needs worst depth at least $\lceil\log_2(N+1)\rceil$. This lower bound concerns the comparison interface, not a promise that every recursive implementation attains it. Inclusive or half-open interval updates must shrink strictly; an unchanged endpoint can create nontermination despite an intended logarithmic recurrence.
