# Individually derived computation-model solutions

## Q1

**Correct option: 2.** Give the root an available mass of one. A node at depth $d$ receives $2^{-d}$; each existing child receives half of that mass. Two children use all of their parent's mass, while a single child uses only half. Thus no split creates mass. Distinct leaves lie in disjoint descendant branches, so the masses finally assigned to them cannot exceed the original unit.

For a formal finite-tree proof, normalize the weight of each subtree root to one and denote its leaf sum by $M(T)$. A root leaf has $M(T)=1$. Otherwise, with existing child subtrees $T_j$, structural induction gives

$$M(T)=\frac12\sum_jM(T_j)\le\frac12\cdot2=1.$$

With one child the bound is at most one half; with two children equality requires equality in both subtrees. Therefore, for a finite nonempty tree, equality holds exactly when every internal node has two children. This condition is fullness, not balance: highly unequal branch depths can still conserve the entire mass.

The root alone gives equality, so option 4's universal strict inequality is false. A root with one leaf child gives $\alpha=1/2$, refuting option 1. Option 3 contradicts the proved conservation inequality. The inequality remains valid if an infinite binary tree is allowed: every finite collection of leaves has disjoint mass at most one, and the nonnegative series is the supremum of those finite sums. However, the finite equality characterization must not be transferred without a finiteness hypothesis: an infinite full tree can have no leaves and hence leaf sum zero.

**Model lesson.** Distinguish a universal upper bound from its equality condition, and state whether the counted structure is finite. Leaf depth is an edge count starting at zero, so including internal-node weights or starting the root at depth one would solve a different question.

## Q2

**Correct option: 1.** Count only comparisons between current front keys during ordinary merging. Copying a remaining tail after the other list is empty makes no further key comparison. The four singleton merges sort $[12,7]$, $[5,9]$, $[3,8]$, and $[2,6]$, using one comparison each.

| Merge | Compared front pairs, in order | Comparisons | Sorted result |
| --- | --- | ---: | --- |
| First left pair | $(12,7)$ | 1 | $[7,12]$ |
| Second left pair | $(5,9)$ | 1 | $[5,9]$ |
| First right pair | $(3,8)$ | 1 | $[3,8]$ |
| Second right pair | $(2,6)$ | 1 | $[2,6]$ |
| Left half | $(7,5),(7,9),(12,9)$ | 3 | $[5,7,9,12]$ |
| Right half | $(3,2),(3,6),(8,6)$ | 3 | $[2,3,6,8]$ |
| Whole array | $(5,2),(5,3),(5,6),(7,6),(7,8),(9,8)$ | 6 | $[2,3,5,6,7,8,9,12]$ |

After the sixth comparison of the final merge, the right list is exhausted; $9,12$ are copied without comparing keys. The total is

$$4\cdot1+2\cdot3+6=16.$$

The value 10 in option 4 counts all lower merges but omits the final merge. Twelve would require only two final comparisons, impossible because both lists contain four keys. Fourteen also disagrees with the explicit six-pair trace. A generic worst-case calculation would instead give $4+6+7=17$ comparisons for eight keys; this supplied array needs one fewer. Neither the worst-case bound nor counting emitted keys is a substitute for the actual front-pair trace.

**Boundary.** Comparisons for testing loop indices or whether a list is empty are not the charged key comparisons here. The distinction must remain consistent throughout all recursion levels.

## Q3

**Correct option: 2.** Define $I_i=1$ if position $i$ replaces the current minimum, and zero otherwise. Since the initial minimum is positive infinity, $I_1=1$. For $i>1$, replacement occurs exactly when the key at position $i$ is smaller than all preceding keys. Every position among the first $i$ is equally likely to contain their minimum under the uniform random-permutation hypothesis; consequently $\operatorname{Pr}(I_i=1)=1/i$.

The total number of replacements is $Y=\sum_{i=1}^n I_i$. Using linearity of expectation,

$$\mathbb E[Y]=\sum_{i=1}^n\mathbb E[I_i]=\sum_{i=1}^n\frac1i=H_n.$$

This computation needs no independence assumption. For example, at $n=3$ the six update counts for permutations $123,132,213,231,312,321$ are $1,1,2,2,2,3$. Their mean is $11/6=1+1/2+1/3$, illustrating the indicator calculation exactly.

Because $1/x$ decreases on positive inputs, bounding each harmonic summand by neighboring integrals gives

$$\ln(n+1)\le H_n\le1+\ln n.$$

Thus the large-$n$ scale is logarithmic; option 2 is the listed approximation. It is not an assertion that $H_n$ equals $\ln n$. One ignores all later record minima; $n$ counts every position as a successful update; $n\ln n$ incorrectly multiplies the scan length by the update expectation.

**Cost distinction.** The loop performs exactly $n$ comparisons against the current minimum regardless of permutation. Its expected successful assignments are harmonic. Increasing input gives one assignment and decreasing input gives $n$, so the expected count must not be reported as either a worst-case count or the scan's total running time. Initializing the minimum from the first element instead would reduce the replacement-assignment count by one.

## Q4

**Correct option: 4.** Write $m=n/k$ and assume nonempty equally sized lists, so $2\le k\le n$ and $k$ divides $n$. When list $j$ is incorporated, the previous merged list contains $(j-1)m$ keys and the incoming list contains $m$. Ordinary merge writes a list of $jm$ keys. Its key comparisons are at most $jm-1$; its total ordinary merge work is proportional to $jm$.

$$\sum_{j=2}^k jm=\frac nk\left(\frac{k(k+1)}2-1\right).$$

For $k\ge2$, this is bounded above and below by fixed positive constant multiples of $nk$, giving $\Theta(nk)$ in the standard model. For example, with $n=12,k=4,m=3$, the three output lengths are $6,9,12$, totaling 27 emitted keys. The exact worst-case comparison total is $5+8+11=24$. Both illustrate increasing accumulated size.

This comparison maximum can be achieved simultaneously. Choose list maxima that strictly increase with the list number, and place every other key below the smallest of these maxima. At stage $j$, the largest key belongs to incoming list $j$ and the second-largest to the accumulated list, whose largest key is the maximum of list $j-1$. The last two keys therefore belong to opposite merge inputs; neither side empties before $jm-1$ comparisons. Hence the bound is not merely the sum of unattainable separate maxima.

Option 3 describes a balanced merge schedule or a suitable heap approach: that changes the algorithm. Option 2 treats $k$ as fixed or ignores repeated processing of the growing list. Option 1 cannot even account for writing the supplied $n$ keys in general. At $k=1$ no merge is performed, so the nontrivial merge analysis explicitly starts at $k=2$; any required initial input read is a separate cost.

## Q5

**Correct option: 3.** Under ordinary binary notation without leading zeros, exactly $b$ bits means

$$2^{b-1}\le N\le2^b-1.$$

The algorithm's charged cost is $T(N)=N$, because one charged unit is specified per iteration. Both endpoints are constant multiples of $2^b$, and the largest cost among all $b$-bit inputs is $2^b-1$. Therefore the tight worst-case order in $b$ is $\Theta(2^b)$.

For $b=4$, the actual iteration counts range from 8 through 15, although the input occupies only four bits. Polynomial alternatives $b$ and $b^2$ fail on growing $b$: dividing $2^b$ by either polynomial grows without bound. The $2^{2b}$ alternative is a loose upper bound but not a tight one, since $N/2^{2b}\le2^{-b}$ tends to zero.

**Model boundary.** This question explicitly charges iterations at unit cost. A real binary counter might also incur nonconstant individual updates under a different representation; that cost cannot be introduced or discarded silently. If unary encoding were used, its length would be $N$ and this same iteration count would be linear in that length. Padding with leading zeros likewise changes the meaning of an input of exactly $b$ bits.

## Q6

**Correct option: 3.** The required output identifies a four-position subset of the eight positions, namely those containing zero. There are

$$q=\binom84=\frac{8\cdot7\cdot6\cdot5}{4\cdot3\cdot2\cdot1}=70$$

such possible outputs. Equal keys do not erase the positions, but permuting same-key records without changing zero positions does not create another requested output. Thus $8!=40320$ would overcount the output distinctions.

| Binary-test depth $d$ | Maximum leaves $2^d$ | Can distinguish 70 outputs? |
| ---: | ---: | --- |
| 5 | 32 | No |
| 6 | 64 | No |
| 7 | 128 | Capacity is sufficient |
| 8 | 256 | More capacity than the minimum bound |

A tree with maximum depth $d$ has at most $2^d$ leaves, even if some branches terminate early. Two different required zero-position subsets cannot share a terminal leaf of a correct deterministic procedure. Hence $2^d\ge70$ and $d\ge\lceil\log_2 70\rceil=7$. Options 1 and 2 lack sufficient information capacity. Eight would be a stronger lower bound requiring a separate argument; it does not follow as the minimum required by this counting calculation.

**Limit of the result.** Seven is an information lower bound, not a construction of a seven-comparison algorithm. Restrictions on which binary comparisons may be asked can force a larger depth. Allowing a genuinely ternary observation would give a different capacity bound, $\lceil\log_3 70\rceil=4$; allowing direct inspection of stored bits also changes the observation model.

## Q7

**Correct option: 3.** Before the $k$th doubling, the exact value is $2^{k-1}$, whose ordinary binary representation is a one followed by $k-1$ zeros. Its operand length is therefore $k$, not $2^{k-1}$. The stipulated charge for that doubling is $k$.

| Doubling number | Operand | Operand bits | Result bits |
| ---: | --- | ---: | ---: |
| 1 | $1$ | 1 | 2 |
| 2 | $2$ | 2 | 3 |
| 3 | $4$ | 3 | 4 |
| $k$ | $2^{k-1}$ | $k$ | $k+1$ |

Summing the actual charged lengths yields $1+2+\cdots+n=n(n+1)/2=\Theta(n^2)$. This is why option 3 is tight. Option 1 counts arithmetic statements in a unit-cost unbounded model rather than the supplied charges. Option 2 uses a logarithm of the loop index, although the current operand length is the index itself. Option 4 substitutes final numerical magnitude $2^n$ for the total charged bit lengths.

**Representation boundary.** Quadratic cost is a conclusion about the explicitly supplied charging convention. Doubling a sparse power-of-two representation could merely increment an exponent; a mutable bit string could append a zero; copying a dense operand charges differently. These alternatives do not invalidate the result because they replace its model. The zero-iteration case has no doubling charge and retains the one-bit integer 1.

## Q8

**Correct option: 3.** An unordered triple is a three-element subset. Choosing ordered distinct elements gives $n(n-1)(n-2)$ sequences; each triple appears in $3!=6$ orders. Therefore the number of triples is $\binom n3=n(n-1)(n-2)/6$.

The requested interface writes all three references of each triple. The output length in charged reference units is exactly $3\binom n3=n(n-1)(n-2)/2$. For fixed triple size and growing $n$, this is $\Theta(n^3)$, imposing $\Omega(n^3)$ writing time. A three-index routine restricted to $i<j<k$ attains this output order with constant work per triple.

The linear and quadratic choices are true weaker lower bounds for sufficiently large $n$, but they miss the tight output-imposed order sought here. The exponential choice confuses all subsets, numbering $2^n$, with subsets of fixed size three; cubic output is not exponential. Computing only the number $\binom n3$ or returning a description such as “all triples” is a different output contract.

**Boundary and units.** At $n<3$ there are no triples; the cubic asymptotic statement concerns the growing family, not positive work on every tiny input. If references are charged in bits instead of constant-size words, include their encoding lengths. Three references per output is not automatically three bit writes.

## Q9

**Correct option: 1.** In each row, form the $c$ scalar products $a_{i1}x_1,\ldots,a_{ic}x_c$ and add those already formed values together. Combining $c$ values by a left-to-right chain uses $c-1$ additions when $c\ge1$.

$$y_i=\sum_{j=1}^c a_{ij}x_j,\qquad M=rc,\qquad A=r(c-1).$$

For $r=2,c=3$, each output has three products and two additions; the totals are six and four. The alternative $c(r-1)$ would be the sum count for $c$ column reductions of length $r$, not the requested $r$ row reductions. The expressions $r+c$ and $rc$ confuse counting entries with adding dimensions. The square counts $r^2,c^2$ discard the rectangular row-column structure.

**Exact convention.** At $c=1$, every output is one product and there are no additions, confirming $r(c-1)=0$. An implementation that initializes an accumulator to zero and then executes `sum += product` for every column performs $rc$ source additions instead. Both implementations compute the same mathematical vector; their exact statement counts differ. The question uses the chain-combination convention, not an implicit zero addition. Scalar counts also do not establish bit costs for arbitrary-precision entries.

## Q10

**Correct option: 2.** Every key comparison removes one front key from one of the two nonempty lists. With lengths three and five, neither can be exhausted before at least three keys have been removed. This lower count is achievable: merge $[1,2,3]$ with $[4,5,6,7,8]$. After three comparisons the first list empties, and the five remaining keys are copied.

Before a comparison both lists must contain a key. Consequently the last possible comparison occurs when two keys remain overall and removes one of them. The maximum is therefore $3+5-1=7$, attained, for example, by $[1,4,7]$ and $[2,3,5,6,8]$. Their final two keys are 7 and 8, from different lists.

Thus the minimum/maximum pair is $(3,7)$. Option 1 adds a nonexistent eighth comparison after one side has emptied. Option 3 overlooks that the shorter list can empty first. Option 4 would remove only one key, insufficient to empty either nonempty list.

**General rule.** For nonempty lengths $p,q$, ordinary front-key merge uses between $\min(p,q)$ and $p+q-1$ comparisons. If either input is initially empty, the comparison count is zero. Copies and bound checks must be charged separately if the requested resource is total instructions rather than comparisons alone.

## Q11

**Correct option: 1.** Let $n=2^h$ for a clean level count and let every combine phase have linear cost. At recursion depth $j$, there are $2^j$ subproblems of size $n/2^j$, so that level's combine work is $\Theta(n)$. There are $h$ nonleaf levels and $n$ constant-cost leaves. Hence

$$W(n)=2W(n/2)+\Theta(n)=\Theta(nh+n)=\Theta(n\log n).$$

The two recursive calls are executed sequentially. During a child call, its parent's frame stays active, but a previously completed sibling no longer occupies the stack. At maximum depth, the live frames form one root-to-leaf chain, containing $h+1$ frames. With constant local storage per frame, peak auxiliary stack space is $\Theta(\log n)$.

| Resource | Objects being counted | Growth |
| --- | --- | --- |
| Total calls | All $2n-1$ tree nodes over the execution | $\Theta(n)$ |
| Total combine work | Linear work at every nonleaf level | $\Theta(n\log n)$ |
| Peak live frames | One active path | $\Theta(\log n)$ |

Option 2 counts all calls as concurrently resident. Option 3 omits repeated combine work across levels. Option 4 substitutes tree height for total execution and total nodes for live storage. Non-power-of-two sizes change rounding but not these orders under balanced halving.

**Storage boundary.** These are recursion-stack cells only. A linear output buffer, copied subarrays, parallel sibling execution or nonconstant frame objects would require another peak-space analysis. The stipulated constant local storage cannot silently include a fresh size-$n$ buffer.

## Q12

**Correct option: 1.** Evaluate the four leaf weights exactly:

$$2^{-1}+2^{-2}+2^{-3}+2^{-3}=\frac12+\frac14+\frac18+\frac18=1.$$

To prove realizability, construct a root with a leaf left child at depth one and an internal right child. That internal node has a leaf at depth two and another internal child; the latter has two leaf children at depth three. Every internal node has exactly two children. The required depth list therefore occurs in a finite full tree, even though this tree is not perfect.

The “one and no” alternative ignores the explicit construction. The $7/8$ alternative loses one of the two depth-three leaves. The $9/8$ alternative counts an additional eighth not present in the given list; it would also violate the universal binary leaf-mass bound.

**Logical distinction.** The mass inequality is a necessary condition on a depth list. Stating a necessary condition alone does not constitute a construction. Here, the explicit shape proves sufficiency for this particular list. Finiteness permits the equality characterization; equality of total mass does not mean every leaf is at the same depth. Root depth is zero and only leaves are summed.

## Q13

**Correct option: 4.** Five labeled distinct keys admit $5!=5\cdot4\cdot3\cdot2\cdot1=120$ possible relative orders. In a comparison-only sorting tree each terminal path must identify an order that can be returned correctly. Since equality never occurs for comparisons of distinct keys, there are at most two relevant outcomes per comparison.

At depth six a binary tree can distinguish at most $2^6=64$ orders, too few. Depth seven allows $2^7=128$ leaves. The minimum integer permitted by this information inequality is therefore seven. This proves that at least one five-key input needs seven or more comparisons for any such sorting algorithm; it does not say every input needs seven.

Option 1 floors the logarithm and would leave at least 56 orders indistinguishable. Option 2 counts the entries of a five-by-five array, unrelated to comparison outcomes. Option 3 prices five separate length-five searches, obtaining 15, but that computation is not the leaf-capacity lower bound. The information inequality alone does not construct a sorting tree of depth seven: legally available key comparisons constrain possible partitions.

**Boundary.** Counting distinct orders assumes distinct keys and no observations beyond key comparisons. A numerical key used as an address or inspected by its bits supplies different information and escapes this specific model.

## Q14

**Correct option: 3.** Eight distinct keys have $8!=40320$ relative orders. The critical capacities are $2^{15}=32768$ and $2^{16}=65536$. Fifteen yes/no comparisons cannot distinguish all required orders in the worst case; sixteen is the smallest integer compatible with the capacity inequality.

$$32768<40320\le65536,\qquad d\ge16.$$

Option 4 uses the floor rather than the ceiling and is insufficient. Sixty-four counts an eight-by-eight set of pairs; 24 equals $8\lceil\log_2 8\rceil$ and could arise from charging eight separate searches, but neither is the requested capacity minimum. An algorithm may use more than sixteen comparisons, and some inputs can use fewer: the result concerns the largest depth and necessary distinguishable leaves.

**Attainability caution.** The model cannot ask arbitrary balanced questions about the permutation; it may ask only legal comparisons of keys. Thus the number sixteen is not, by itself, a proved exact optimum for sorting eight keys. Converting a numerical lower bound into an equality would need an algorithm and a matching upper-bound proof, neither supplied by leaf counting.

## Q15

**Correct option: 2.** For $n$ distinct labeled keys, choose the least key in $n$ ways, the next in $n-1$ ways, and continue, giving $n!$ possible orders. A correct sorting leaf cannot combine two incompatible relative orders into the same returned permutation. A binary tree of maximum depth $d$ has at most $2^d$ leaves, so

$$2^d\ge n!,\qquad d\ge\lceil\log_2(n!)\rceil.$$

The ceiling is necessary because depth is integral. For example, $n=5$ gives a logarithm strictly between six and seven, making the floor option false. The alternatives $n^2$ and $n\lceil\log_2 n\rceil$ are not solutions of the capacity inequality; at $n=5$ they give 25 and 15 instead of seven. At $n=1$, the single order requires zero distinguishing tests, correctly giving $\lceil\log_2 1\rceil=0$.

To recover the asymptotic lower order without assuming Stirling's formula, note that at least $n/2$ factors of $n!$ are at least $n/2$. Thus $\log_2(n!)\ge(n/2)\log_2(n/2)$, while $n!\le n^n$ gives the upper logarithmic bound $n\log_2 n$. These inequalities place the information lower bound in $\Theta(n\log n)$ for growing $n$. They still do not prove exact attainability of the ceiling by legal sorting comparisons.

## Q16

**Correct option: 1.** The proof has two essential premises: $n!$ distinguishable relative orders of distinct keys, and at most two relevant branches per charged comparison. From these it derives $d\ge\lceil\log_2(n!)\rceil$ for the worst-case depth of a comparison-only sorting tree.

Option 2 reverses a lower bound into an upper bound on every algorithm. A deliberately redundant algorithm could repeat each comparison many times without becoming incorrect. Option 3 transfers the lower bound to another observation model: bounded integer keys can be used as addresses or digit-indexed values, so their information is not restricted to two comparison outcomes. Option 4 overcounts when keys repeat. With multiplicities $m_1,\ldots,m_r$ totaling $n$, the number of distinct key-order assignments is $n!/(m_1!\cdots m_r!)$ when equal-key permutations are not distinguished by the output contract.

For eight keys consisting of four zeros and four ones, that count is 70, rather than $8!$. A stable sorting task may additionally prescribe order within equal-key records, but that order is determined by their initial positions rather than creating arbitrary independent key orders. The correct lower-bound argument must count only genuinely different required outcomes under the declared task.

## Q17

**Correct option: 3.** Each of the five elements has an independent include/exclude bit, giving $2^5=32$ subsets. The interface does not output one subset identifier or one changing position: it writes a complete five-bit vector for each subset. Hence the exact number of emitted bits is $32\cdot5=160$.

A small analogous case makes the distinction visible: for two elements the vectors are `00`, `01`, `10`, `11`; four objects occupy eight emitted bits, not four. Five elements follow the same multiplication rule. Option 4 counts objects alone. Option 1 squares the number of input elements despite there being 32 outputs. Option 2 uses $2^{25}$, as if the object were a freely chosen five-by-five bit matrix rather than a five-bit subset.

**Resource interpretation.** This is an exact output-length count. In a bit-output model it gives at least 160 writes; it does not count loop tests, memory reads or separators. A word-output model can emit several bits per word, but then word width and packing must be stated. Replacing each vector by an incremental change notification changes the contract and cannot reduce the stipulated full-vector bit count.

## Q18

**Correct option: 2.** The eight independent membership bits identify $2^8=256$ distinct subsets. Every output is a full eight-bit vector, so the emitted payload is $8\cdot256=2048$ bits.

The first and last vectors might be `00000000` and `11111111`, but their order does not affect total length: all 256 vectors have the same eight-bit width. Option 3 counts vectors without their lengths. Sixty-four prices only an eight-by-eight grid. Option 1 counts $2^{64}$ objects, corresponding to arbitrary 64-bit configurations rather than the declared eight-bit membership choices.

If one primitive output instruction handles one bit, 2048 output instructions are necessary. If it writes one aligned eight-bit word and the vectors occupy individual words, exactly 256 payload word writes suffice, illustrating why the units matter. This does not change the 2048-bit answer. A descriptor “all subsets” or a borrowed pointer to a precomputed collection is an implicit result, unlike explicit enumeration. Precomputing those vectors elsewhere moves their materialization cost; it does not make that earlier work disappear.

## Q19

**Correct option: 1.** Establish a bijection between subsets and membership vectors: the $i$th bit is one exactly when element $i$ belongs to the subset. There are $2^n$ vectors and each contains $n$ bits. Therefore the full-vector interface emits exactly

$$B(n)=\sum_{S\subseteq U}|\operatorname{vector}(S)|=n2^n.$$

The factor $n$ is a representation length, not an extra independent choice. That is why $2^{n^2}$ is incorrect; it would describe choosing $n^2$ independent bits. The expression $2^n$ counts outputs but not emitted bits, and $n^2$ ignores the exponential number of subsets. At $n=1$ some wrong expressions coincide, which is not evidence of a general identity; $n=3$ gives 24 bits versus 8, 9 and 512 for the alternatives.

For $n=0$, a single empty subset has a zero-bit payload, consistent with $n2^n=0$. A representation with a delimiter per output would still write framing information even at that boundary, so payload length and total serialized length must be separated. Under a packed word-output model, concatenate the payload and charge at least $\lceil n2^n/w\rceil$ word writes, rather than silently treating a bit as a word.

## Q20

**Correct option: 4.** The equality $n2^n$ comes from the stipulated requirement to emit every full $n$-bit membership vector. A changed output interface produces a changed count. For example, a Gray-code traversal can describe each next subset by a changed coordinate, using an index of about $\log_2 n$ bits per change, but reconstructing each entire vector still requires the receiver to maintain state. Those messages are not the original full-vector outputs.

Option 1 contradicts this explicit comparison. Option 2 treats a finite word of $w$ bits as an unbounded information container; it has only $2^w$ patterns. If a vector is longer than $w$, it spans multiple words. Option 3 replaces output count by the number of bits needed to name that count: a short description of how many outputs exist is not the act of emitting them.

**Lower-bound test.** Ask whether the requested result is a full materialized list, an iterator, an implicit description or a pointer to already stored data. Only then divide by the number of bits or references one charged operation can emit. Compression does not refute a lower bound for uncompressed materialization; it solves a different interface problem.

## Q21

**Correct option: 1.** For $n=5$, the number is $2^5-1=31$, whose binary expansion is `11111`. The five positions carry weights 16, 8, 4, 2 and 1, totaling 31. Thus the representation length is five bits.

The count 31 in option 2 is the numerical value, not the number of digits. Four bits can encode at most $2^4-1=15$, so option 3 cannot hold this value. Six bits could hold 31 with a leading zero, but ordinary unpadded binary excludes that extra position. Option 4 instead resembles the length of 32, namely `100000`.

The proof generalizes from the positional sum $1+2+\cdots+2^{n-1}=2^n-1$: its highest nonzero position is $n-1$, so there are $n$ positions from zero through $n-1$. This is precisely the off-by-one distinction between a bit's index and a representation's length. No computation of the large integer's decimal digits is needed to establish its binary length.

## Q22

**Correct option: 4.** For $n=8$, $2^8-1=255$, written as `11111111`. Its highest place value is $2^7=128$; counting that position and the seven lower positions gives eight bits.

The value 255 counts units of numerical magnitude. Seven bits permit at most 127 and cannot represent 255. Nine bits are needed for 256, written as `100000000`, but that is the next integer. The adjacent pair 255/256 demonstrates the length jump at a power of two rather than a continuous relationship between magnitude and digit count.

**Input-size consequence.** An algorithm executing once for each integer from 1 through 255 takes 255 iterations on this eight-bit input. Scaling the pattern to $b$ bits gives $2^b-1$ iterations. A fixed numerical example is finite, but the growing family establishes exponential dependence on the binary length. This claim is about a value-dependent loop, not about the cost of merely reading the eight bits or computing the formula for their maximum value.

## Q23

**Correct option: 3.** For every integer $n\ge1$,

$$2^{n-1}\le2^n-1<2^n.$$

An ordinary positive binary integer in that interval has exactly $n$ bits. Equivalently, $\lfloor\log_2(2^n-1)\rfloor=n-1$, and adding one yields the length $n$.

The expression $n-1$ is the highest bit index rather than the number of occupied positions. The expression $n+1$ is the length of the next integer $2^n$. The numerical value $2^n-1$ grows exponentially and cannot stand for its digit count. At $n=1$ it happens to equal the correct length, but at $n=3$ the value seven needs only three bits, demonstrating the general failure.

**Boundary.** Extending the formula blindly to $n=0$ would give the number zero and a claimed length of zero. This chapter encodes zero as the one-bit string `0`; therefore the positive-index condition is essential. A fixed-width machine representation may include leading zeros and hence have a supplied width different from this minimal ordinary representation length.

## Q24

**Correct option: 2.** A loop with one iteration for each unit of $N=2^n-1$ performs that many iterations. Since the input length is $n$, the iteration count is exponential in the encoded length, even though it is linear in $N$.

Option 1 confuses the length of a padded representation with the minimal representation length: adding zeros can increase supplied length but does not change $N$. Option 3 asserts value equals length; $31$ represented as five bits is already a counterexample. Option 4 declares every value-linear method polynomial in binary length, contradicted by the same growing family.

For a precise pseudo-polynomial classification, both item count and numeric parameters should be named. A cost $\Theta(mN)$ is polynomial in $m,N$, but an input with fixed $m$ and $n$ capacity bits can still require $\Theta(2^n)$ iterations. Conversely, if an independently stated restriction guarantees $N\le m^c$ for a fixed constant $c$, that restricted family can have a polynomial bound in structural size. Thus “may be exponential” is a possibility over the admitted input family, not a claim that every numerical instance forces an exponential cost.

## Q25

**Correct option: 4.** The value is $2^5-1=31$. Unary encoding uses one mark for each unit of value, so it contains 31 marks. A grouping such as six blocks of five marks plus one remaining mark can make that count easy to check; those visual groups are not additional encoding symbols.

Five is the length of the binary string `11111`, not the unary string. Thirty-two is the unary length of the next value $2^5$, and sixteen uses only the highest positional bit's weight. The correct unary length comes directly from its one-mark-per-unit definition, without logarithms.

**Conversion cost.** Writing this unary output from a binary input needs at least 31 mark writes in a one-symbol-output model. For the general $n$-bit all-ones value, the conversion writes $2^n-1$ marks. Thus converting to unary cannot be treated as free preprocessing when comparing end-to-end algorithms. Once that longer input has actually been supplied, a subsequent one-step-per-mark scan is linear in its unary length.

## Q26

**Correct option: 3.** With $n=8$, the integer is $2^8-1=255$, so unary notation requires 255 marks. The eight-bit binary representation conveys the same value much more compactly, but the question explicitly changes the representation.

Option 4 retains the binary digit count eight after switching to unary. Two hundred fifty-six represents $2^8$ rather than $2^8-1$. One hundred twenty-eight is $2^7$, the weight of the highest binary bit, and omits all lower place values. The subtraction of one is numerically significant here; an asymptotic replacement by $2^8$ cannot answer an exact count question.

The length ratio for this instance is $255/8$. In the growing family it is $(2^n-1)/n$, which is unbounded and certainly not a fixed additive or multiplicative change. Therefore statements about complexity in the input's length need the encoding to be identified. This result concerns unary payload marks; separators, sign symbols or framing would need separate accounting if included in the format.

## Q27

**Correct option: 2.** Let the unary encoder map positive integer $N$ to $N$ copies of the mark `1`. Its length is exactly $N$. Substituting $N=2^n-1$ yields the general expression $2^n-1$.

Option 3 gives the length of the unpadded binary encoder. Option 4 includes one extra mark and would encode $2^n$. Option 1 counts only the leading binary place value, ignoring the sum $2^{n-2}+\cdots+1$. At $n=1$, the exact unary length is one, so several expressions accidentally coincide; $n=3$ distinguishes seven from three, eight and four.

If an algorithm uses exactly $N$ charged iterations, then with unary input length $L=N$ its cost is $\Theta(L)$. With binary length $b=n$, the same iteration count is $\Theta(2^b)$. These are compatible statements about one numerical computation viewed against different input encodings. In particular, the unary form does not make construction of that input from a short binary description free.

## Q28

**Correct option: 1.** Polynomial time is measured against the length of a specified encoding, not an abstract numerical value. For the example, binary length is $n$ while unary length is $2^n-1$. A value-linear loop is exponential in the first length and linear in the second.

Option 2 incorrectly assumes a polynomial in a numeric value remains polynomial after taking the value's logarithmic encoding length. Option 3 would require the difference $2^n-1-n$ to be constant, but it already equals 26 at $n=5$ and 247 at $n=8$. Option 4 ignores both the changed size measure and the conversion work.

**What comparisons are legitimate?** Encodings related by polynomial-time conversions with polynomially bounded lengths preserve broad polynomial classifications under appropriate models. Binary and unary conversion in the direction that materializes unary can create an exponentially long output, so they are not such a freely interchangeable pair. A correct exam argument identifies the representation, defines its length and substitutes it into the resource function before classifying growth.

## Q29

**Correct option: 4.** The direct product $C=AB$ of two five-by-five dense matrices has 25 output entries. For each fixed $(i,j)$,

$$C_{ij}=\sum_{k=1}^5 A_{ik}B_{kj}$$

contains five scalar products. Therefore 25 dot products require $25\cdot5=125$ scalar multiplications.

Option 1 counts output entries but loses the five products inside each. Option 2 equals $25\cdot4=100$, which is the chain-addition count if the five products are combined using four additions per entry. Option 3 doubles the multiplication count, treating another operation type as an additional multiplication. Under the chain convention, the separate scalar-operation subtotal would be $125+100=225$, not 250.

**Convention.** A multiply-accumulate machine instruction might perform a product and addition together, but that instruction count is another metric. This question counts mathematical scalar multiplications in the stated direct row-column algorithm. Zero entries, sparsity shortcuts or a faster algebraic matrix algorithm would alter the declared computation and need their own count.

## Q30

**Correct option: 3.** With eight rows and eight columns, the output contains $8^2=64$ entries. Every direct dot product has eight terms, so $64\cdot8=512$ multiplications are executed.

The 64 alternative counts only outputs. The 448 alternative is $64\cdot7$, the additions required to combine eight already formed products by a chain. The 1024 alternative is $2\cdot512$; it is not the multiplication count, and even the chain-convention combined count is $512+448=960$, not 1024.

For an index-based derivation, the multiplication instructions correspond bijectively to triples $(i,j,k)$ with each coordinate in $\{1,\ldots,8\}$. There are $8^3$ such triples. This establishes the count from the iteration region rather than guessing from the number of nested loops. Operand bit lengths can make one scalar multiplication expensive in another model; 512 source multiplications do not automatically mean 512 bit operations. At $n=1$ the direct method has one multiplication and zero chain additions, confirming the distinction.

## Q31

**Correct option: 2.** For each output pair $(i,j)$ in the $n$-by-$n$ output, the algorithm executes one multiplication for each $k$ from 1 through $n$. Hence its multiplication events are the full Cartesian product of the three index ranges, numbering $n^3$.

$$M(n)=\sum_{i=1}^n\sum_{j=1}^n\sum_{k=1}^n1=n^3.$$

The expression $n^2$ counts dot products, not their constituent scalar products. The expression $n^2(n-1)$ counts chain additions. The expression $2n^3$ would combine different operation types under a different exact convention, and it is not an exact multiplication count. These distinctions survive asymptotically even though the multiplication and addition totals both have cubic order for growing $n$.

The identity proves the cost of this direct algorithm, not a cubic lower bound for every matrix multiplication method. A different algorithm may combine blocks and reorganize products. Likewise, in a bit model each event needs an operand-size charge. For rectangular multiplication of an $r\times s$ matrix by an $s\times c$ matrix, the same index accounting gives $rsc$ products and $rc(s-1)$ chain additions for $s\ge1$.

## Q32

**Correct option: 1.** A scalar-operation count assigns one event to each mathematically performed multiplication, regardless of precision. A bit-operation analysis instead depends on how many bits those operands carry and on the multiplication algorithm. For example, grade-school multiplication of two $b$-bit operands forms $b^2$ one-bit partial products; treating the entire operation as one bit event would lose those internal computations.

Option 2 makes precisely that mistake for unbounded integers. Option 3 mistakes output entries for additions: a direct $n$-by-$n$ product has $n^2$ outputs but $n^2(n-1)$ chain additions. At $n=1$ those counts are one and zero, already different. Option 4 mistakes an algorithm's upper-cost analysis for a problem lower bound. Reorganizing products with a faster algebraic algorithm is not prohibited by the direct algorithm's cubic count.

**Exam discipline.** State whether multiplication is a scalar event, a word instruction or a multiword subroutine. Exact integer accumulation can also increase intermediate widths: summing $n$ products of $b$-bit unsigned inputs can need up to approximately $2b+\log_2 n$ bits. A faithful bit analysis therefore needs bounds on intermediate values as well as the number of source statements.

## Q33

**Correct option: 1.** A permutation of five distinct labels chooses its first label in five ways, its second in four remaining ways, and so on, giving $5!=120$ complete orders. The output interface writes all five labels for every one of those orders.

$$\text{emitted labels}=5\cdot120=600.$$

Option 2 counts the number of lists without their lengths. Option 3 counts $5^5=3125$ arbitrary assignments of labels to five positions, permitting repeated labels and omitting others; those are functions, not permutations. Option 4 counts a five-by-five grid and has no correspondence to either permutation count or explicit list length.

Even if the internal next-permutation operation sometimes changes only a few positions, emitting a complete new length-five list writes five labels each time. An interface emitting only changes would require an initial state and reconstruction protocol and would be another problem. Constant-time label writes assume each label/reference occupies a bounded number of words; bit-encoded labels would require their widths to be included in the output measure.

## Q34

**Correct option: 4.** The exact number of eight-label permutations is

$$8!=8\cdot7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1=40320.$$

Each output writes eight labels, making the payload count $8\cdot40320=322560$. The choice 40320 counts outputs alone. The choice $8^8=16777216$ counts all length-eight strings over eight labels, including strings such as eight copies of one label that are not permutations. Sixty-four is unrelated to the factorial enumeration.

The unavoidable explicit-output cost is already factorial in the number of labels. This conclusion does not say that naming a permutation or representing a generator requires factorial storage; a generator can use limited live state. It says that completing the full materialized output stream requires writing all its labels. Peak working memory and total output volume are different resources, just as recursion height and total recursive work are different.

**Boundary.** Distinctness matters. If repeated label values are treated as indistinguishable, unique permutations number $n!/(m_1!\cdots m_r!)$, and the requested output count changes.

## Q35

**Correct option: 3.** The multiplication principle gives $n!$ permutations because there are $n,n-1,\ldots,1$ remaining choices for consecutive positions. The full-list interface emits $n$ labels per permutation, so its exact output count is $n\,n!$.

An arbitrary self-map has $n$ independent choices at each of $n$ domain positions and therefore $n^n$ possibilities; independence is absent in a permutation because used labels cannot be repeated. The alternative $n!$ omits the labels per output. The alternative $n^2$ replaces factorially many ordered outcomes by a polynomial grid. With $n=3$, the six length-three permutations emit 18 labels, while the alternatives give 27, 6 and 9.

Under one-reference-per-output-step accounting, time is at least $n\,n!$ such steps. This is a lower bound from the output contract, not an exact total runtime that ignores generation and bookkeeping. At $n=0$ there is one empty permutation but zero payload labels; a delimiter or notification could still have nonzero serialization cost. An output-count theorem must therefore distinguish mathematical outcomes from the actual symbols sent to the receiver.

## Q36

**Correct option: 2.** A permutation is bijective: each of the $n$ labels occurs once, and order matters. An arbitrary function from an $n$-element set to itself can repeat images. For $n=2$, the functions are the four image lists $[1,1],[1,2],[2,1],[2,2]$, whereas only the two middle lists are permutations.

This explicit example disproves option 3's equality of counts. It also disproves option 1: $[1,2]$ and $[2,1]$ are distinct ordered outputs. Option 4 ignores the required materialization; two different next-permutation states do not become fully emitted lists merely because an internal pointer can identify them.

For the stated interface, multiplying $n!$ admitted orders by $n$ labels per order gives $n\,n!$. This is the unavoidable output length before charging any generation overhead. Reusing one mutable buffer for an iterator is possible, but if the receiver expects independently retained copies, mutating that buffer would change earlier outputs and violate the contract. Ownership, copying and aliasing assumptions can therefore matter as much as the numerical count.

## Q37

**Correct option: 3.** At position 1 there is no earlier key; positions 2, 3, 4 and 5 compare with one, two, three and four earlier keys respectively. The total is $0+1+2+3+4=10$.

| Position $i$ | Earlier indices compared | Count |
| ---: | --- | ---: |
| 1 | None | 0 |
| 2 | 1 | 1 |
| 3 | 1, 2 | 2 |
| 4 | 1, 2, 3 | 3 |
| 5 | 1, 2, 3, 4 | 4 |

The 15 alternative counts $1+2+3+4+5$ and includes a self-comparison at every position. Twenty-five compares every position with all five positions, including later positions and duplicate orientations. Four counts only the comparisons performed at the last position, omitting earlier work.

Every unordered pair appears exactly once, at its later endpoint, so an independent counting check is $\binom52=10$. Because the routine is required to perform every stipulated comparison, this count does not depend on the key values. Adding an early return on equality would change that input independence and require separate best- and worst-case analyses.

## Q38

**Correct option: 2.** The eight comparison counts are $0,1,2,3,4,5,6,7$. Pairing the first and last, second and next-to-last, and so on gives four pairs each summing to seven, for a total of 28.

Equivalently, there are $\binom82=8\cdot7/2=28$ unordered distinct position pairs. Each is visited when its later position is processed. This second derivation verifies that no self-pair and no repeated orientation is included.

Option 1 counts only the seven comparisons at the final position. The 36 alternative is $8\cdot9/2$ and adds eight self-comparisons. Sixty-four counts a full eight-by-eight Cartesian product rather than its strict triangular region. Thus identifying the actual eligible index pairs, rather than counting the number of loops in the source, determines the exact cost.

**Control-flow boundary.** The present routine has no data-dependent exit. If it returned on the first duplicate, a duplicate-free array would still force all 28 comparisons, while equal first and second keys could terminate after one key comparison. Allocating a record array beforehand might also add initialization work without changing the key-comparison count.

## Q39

**Correct option: 1.** The eligible events are ordered index pairs $(j,i)$ satisfying $1\le j<i\le n$. Each unordered pair of distinct positions has exactly one such orientation. Therefore

$$C(n)=\binom n2=\sum_{i=1}^n(i-1)=\frac{n(n-1)}2.$$

The expression $n(n+1)/2$ includes the $n$ diagonal pairs. The expression $n^2$ includes all ordered pairs, counting both orientations and self-pairs. The expression $n-1$ counts just the final row. At $n=1$, the actual count is zero, correctly reproduced by $n(n-1)/2$; at $n=2$ it is one.

For $n\ge2$, this grows quadratically even though the exact leading coefficient is one half. A Big-Theta answer may discard that coefficient; an exact-count question may not. If each comparison acts on opaque strings rather than one-word keys, its internal character cost must also be charged in a model that counts characters. An exact number of key-comparison calls is not automatically the same as their execution time.

## Q40

**Correct option: 4.** The fixed routine visits the strict triangular region $j<i$, so its count is $n(n-1)/2$. A modification that returns when equal keys are found may visit only a prefix of that region. With the first two keys equal, only one key comparison is needed; with all keys distinct, every eligible pair is tested.

Hence for $n\ge2$ this early-exit version has a best-case key-comparison count of one and a worst-case count of $n(n-1)/2$, assuming the task is duplicate detection and no other preliminary comparisons are charged. The pair of actual witness inputs justifies these extrema rather than deriving them from syntax alone.

Option 1 replaces a triangular region by a rectangle. Option 2 includes self-pairs that the strict condition excludes. Option 3 assumes two nested loops always execute a fixed number of iterations without looking at their limits or exits. These errors alter the set of executed events, which is the object being counted.

**Average case.** A mean for the early-exit count would require a probability distribution over key arrays and a specified comparison order. Neither can be inferred from the presence of an early return. Best, worst and expected costs are separate quantified questions.

## Q41

**Correct option: 3.** A perfect tree with five nonempty levels has level sizes $1,2,4,8,16$, totaling 31 keys. A deepest successful search visits one key at each of those five levels. With one charged three-way comparison against each visited key, it performs five key comparisons.

The deepest key has edge depth four, which explains option 1's off-by-one error: edge count excludes the root's comparison. Six would charge an additional step after equality has already ended the search. Thirty-one counts every stored key, while a successful search follows one path and does not scan the entire tree.

**Primitive definition.** A language implementation may use separate equality and less-than tests at a node. Then the source Boolean-test count can be different. This question charges one comparison capable of reporting the key's order relative to the node key. Under that convention, deepest successful cost equals visited nodes. A null-pointer check is not another key comparison because no key is stored at a null child.

## Q42

**Correct option: 2.** Since $255=2^8-1=1+2+4+\cdots+128$, the perfect tree has eight nonempty levels. The deepest successful path has seven edges but eight visited keys. The matching last node is compared before success is known, so the count is eight.

Option 4 counts only the seven edges. Option 1 adds a comparison at a nonexistent empty successor after a successful match. Option 3 counts all 255 keys as though the routine performed a traversal. The path property of search is the reason the full tree size is not the comparison count.

For an unsuccessful query below the deepest leaf, the routine can visit an empty child afterward, but there is still no ninth key to compare. An implementation may charge that null check as an instruction, which is a different metric. Also, storing 255 keys does not by itself guarantee eight levels: a skewed search tree of the same size could have a path of 255 keys. The perfect-height premise is essential.

## Q43

**Correct option: 1.** A perfect tree with $ℓ$ nonempty levels has $1+2+\cdots+2^{ℓ-1}=2^ℓ-1$ nodes. The given size $2^n-1$ therefore makes $ℓ=n$. A deepest successful search visits all $n$ nodes along one path and charges one key comparison at each, giving exactly $n$.

The $n-1$ alternative is height measured in edges. The $n+1$ alternative adds an empty-child event after a match. The $2^n-1$ alternative scans the whole tree. At $n=1$, the root alone requires one successful key comparison, so the edge count zero cannot be the answer.

In terms of the stored-key count $N=2^n-1$, this exact cost is $\log_2(N+1)$. The answer is logarithmic in $N$ but linear in the exponent parameter $n$. The same symbol cannot silently denote both input measures. Separate less-than/equality Boolean instructions or multiword-key comparisons would need an explicit revised charging model.

## Q44

**Correct option: 4.** Perfection fixes the node count by levels and gives a deepest path containing $n=\log_2(N+1)$ keys when $N=2^n-1$. Without a height restriction, a valid binary search tree can store its $N$ sorted keys as a one-child chain; searching for the final key then makes $N$ comparisons.

That chain refutes options 1 and 2: the same total size does not force perfection or the same height. Option 3 charges an empty structural position after a successful search, although success stops at the matching key. Even for an unsuccessful search, reaching null does not compare against another key.

**General formula.** For any fixed search tree, a successful query at edge depth $d$ costs $d+1$ charged node-key comparisons. The deepest successful cost is therefore $h+1$, where $h$ is that tree's edge height. The logarithmic conclusion requires a height theorem or a balancing invariant; it is not supplied by the word “binary.” This explains why structural assumptions belong in the computational contract before a complexity claim is made.

## Q45

**Correct option: 4.** Let $x_0=2$ and $x_{k+1}=x_k^2$. Induction on $k$ gives $x_k=2^{2^k}$: the base is $2^{2^0}=2$, and squaring doubles the exponent $2^k$ to $2^{k+1}$. A power $2^e$ needs $e+1$ ordinary binary bits.

| Completed squarings $k$ | Exact value | Bit length |
| ---: | --- | ---: |
| 0 | $2$ | 2 |
| 1 | $2^2$ | 3 |
| 2 | $2^4$ | 5 |
| 3 | $2^8$ | 9 |
| 4 | $2^{16}$ | 17 |
| 5 | $2^{32}$ | 33 |
| 6 | $2^{64}$ | 65 |

Thus the requested final length is 65. Six counts squaring statements, 32 is the exponent before the last squaring, and 64 is the final highest bit index rather than its length.

**Model distinction.** An unsigned 64-bit word holds at most $2^{64}-1$, so the exact final answer no longer fits. Performing modular 64-bit squaring would instead give zero at the last step. A representation storing only the exponent could manipulate this special family compactly, but returning a materialized exact integer still requires its 65-bit output. Repeated squaring of general values must be charged by their growing operand lengths, not merely by six source operators.

## Q46

**Correct option: 3.** Under ordinary unpadded binary notation, a positive capacity with exactly 20 bits satisfies $2^{19}\le W\le2^{20}-1$. The largest capacity is $1048575$, not $2^{20}$. With 100 cells per capacity unit, the largest count is

$$100(2^{20}-1)=100\cdot1048575=104857500.$$

Two thousand substitutes the bit length 20 for the value $W$. The value 1048575 omits the factor 100. The value 104857600 uses $2^{20}$, which requires 21 bits and is excluded by the input domain. The exact subtraction must be retained before multiplication.

**Storage versus initialization.** The result counts cells, not bytes, bits or primitive instructions. If each cell contains $s$ payload bits, their payload requires $s\cdot104857500$ bits; if cells are eagerly initialized one per write, that many writes are necessary. Virtual allocation without immediate writes has another runtime model, although the declared table size is unchanged.

For a general $b$-bit capacity with the same fixed factor 100, the maximum count is $100(2^b-1)=\Theta(2^b)$. It is linear in numeric capacity but exponential in its binary description length. The statement classifies this table construction; it does not prove every algorithm for the underlying problem needs the same table.
