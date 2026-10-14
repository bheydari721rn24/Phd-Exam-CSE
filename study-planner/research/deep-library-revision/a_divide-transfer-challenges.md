## Solved transfer challenges

These ten additional problems are independently authored and are not attributed to an unrelated examination booklet. Each problem changes a hypothesis or representation, so its solution must justify the mechanism rather than substitute into a memorized formula.

### Challenge 1. A strict inversion count with duplicate boundary keys

**Problem.** Merge $L=[2,4,4,7]$ and $R=[1,4,6]$. Count cross inversions, head comparisons and output writes under stable left-first equality handling. Identify the step at which a non-strict inversion test first becomes wrong.

**Solution.** Compare 2 with 1: select 1 and charge four left keys. Compare 2 with 4: select 2 and charge nothing. Compare the first left 4 with the right 4: select left and charge nothing. Repeat for the second left 4. Compare 7 with 4: select right 4 and charge one. Compare 7 with 6: select 6 and charge one. The right side is now exhausted; copy 7 without another head comparison. There are six comparisons, seven writes and $4+1+1=6$ cross inversions.

The pairs are $(2,1)$, both identity-distinct $(4,1)$ pairs, $(7,1)$, $(7,4)$ and $(7,6)$. Identity distinguishes the two left fours without changing their equality relation. A test charging when $R_j\le L_i$ would charge the two equal left fours on the right 4 and overcount by two. Stability also fails if the right equal key is emitted first. Output writes are not a replacement for key-comparison counts: the final 7 must still be written, even though no opposite head remains. The exact worst bound $p+q-1=6$ happens to be attained for this input, while its inversion count is below the possible cross maximum $pq=12$.

### Challenge 2. Prove why summaries cannot be reversed

**Problem.** Compute the four-component nonempty summaries of $L=[3,-6,5,-5,1]$, $R=[6,-2]$, their concatenation and the reversed concatenation. Return earliest-start/earliest-end best witnesses using zero-based half-open intervals.

**Solution.** The left total is $-2$, prefix candidates are 3, −3, 2, −3 and −2, so its prefix is 3. Its suffix candidates from the right are 1, −4, 1, −5 and −2, so its suffix is 1. Its best sum is 5 from the singleton at $[2,3)$. The right summary is $(4,6,4,6)$. Thus $L\star R=(2,4,5,7)$: prefix $\max(3,-2+6)=4$, suffix $\max(4,4+1)=5$, and best $\max(5,6,1+6)=7$.

For the crossing witness, left suffix sum 1 has two possible intervals, $[2,5)$ and $[4,5)$. The earlier-start tie rule selects $[2,5)$; the right best prefix is its first element, so the global answer is $[2,6)$, namely $[5,-5,1,6]$. The shorter interval $[1,6]$ also totals 7 but loses the specified tie rule. Reversing the intervals gives $R\star L=(2,7,2,7)$, with earliest best witness $[0,3)$ in $[6,-2,3,-6,5,-5,1]$. Its best suffix is the entire reversed concatenation, with sum 2. Best values happen to tie, but prefix and suffix differ. Equality of one component cannot establish commutativity. The retained laboratory independently enumerates the nonempty intervals and verifies these witness policies.

### Challenge 3. An odd-width signed Karatsuba product

**Problem.** Multiply $-123$ by 45 using low width one decimal digit. Compute both the sum and difference variants on magnitudes and explain how the final sign is restored.

**Solution.** Magnitudes split as $123=12\cdot10+3$ and $45=4\cdot10+5$. The outer products are $z_2=48$, $z_0=15$. The sum product is $(12+3)(4+5)=15\cdot9=135$, so the mixed coefficient is $135-48-15=72$. The magnitude is $48\cdot100+72\cdot10+15=5535$.

For the difference variant, $d=(12-3)(4-5)=9(-1)=-9$. Consequently $z_1=48+15-(-9)=72$, agreeing with the sum formulation. Treating $d$ as positive 9 would produce 54 and the incorrect magnitude 5355. Exactly one original operand is negative, so restore the negative sign and obtain −5535. The width choice, not a fractional half of three digits, supplies shifts of 10 and 100. A sum may gain a digit; the difference may become negative. These are representation obligations of the identity, not exceptions that can be ignored by its recurrence. Direct multiplication verifies the particular result; expansion of the radix representation proves the method for arbitrary admissible inputs.

### Challenge 4. Audit all four Strassen outputs

**Problem.** Multiply $X=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ and $Y=\begin{pmatrix}5&6\\7&8\end{pmatrix}$ using the seven-product convention in Construction 5. Explain which algebraic property permits cancellation.

**Solution.** Products are $M_1=5\cdot13=65$, $M_2=7\cdot5=35$, $M_3=1\cdot(-2)=-2$, $M_4=4\cdot2=8$, $M_5=3\cdot8=24$, $M_6=2\cdot11=22$ and $M_7=(-2)\cdot15=-30$. Therefore $C_{11}=65+8-24-30=19$, $C_{12}=-2+24=22$, $C_{21}=35+8=43$, and $C_{22}=65-35-2+22=50$.

Direct dot products give $(5+14,6+16,15+28,18+32)$, independently agreeing with $(19,22,43,50)$. This check covers all outputs rather than inspecting only the top-left block. In a recursive block application, distributivity expands products of sums, and additive inverses cancel the unwanted terms. Block multiplication itself need not commute. For example, replacing $DE$ by $ED$ would generally invalidate the cancellation even though this scalar instance would not expose the error. Over Boolean OR/AND, subtraction has no direct meaning, so these formulas are not immediately a seven-product Boolean semiring algorithm. State the arithmetic domain before transferring the identity.

### Challenge 5. Find the closest cross pair without re-sorting

**Problem.** Rank-divide points $(-2,0),(-1,3),(0,1),(0,2),(1,4),(2,0)$ into two halves of three, preserving the listed order for tied x-coordinates. Determine the two child distances, strip order and global closest pair. Work with squared distances.

**Solution.** In the left child the pairwise squared distances are 10, 5 and 5; its minimum is 5. In the right child they are 5, 8 and 17; its minimum is also 5. Thus the initial $\delta^2=5$. A divider at zero admits all six points because their absolute x-offsets are at most 2, less than $\sqrt5$. The y-order, with the stated identity tie rule, is $(-2,0),(2,0),(0,1),(0,2),(-1,3),(1,4)$.

The two points at x=0 have different child identities. They form a cross pair with squared distance 1, so the current bound decreases to one. No smaller squared distance is possible among distinct integer-coordinate points: the sum of two integer squares is either zero or at least one, and this input has no duplicate point. Hence the global minimum distance is one. Once that pair is found, y-separation at least one cannot improve the bound and may terminate a local forward scan. Filtering a maintained y-order is linear; independently sorting these strip points in every recursive call would change the recurrence. An x-only test assigning all x=0 points to one side would contradict the declared rank partition and break this trace.

### Challenge 6. An exact modular butterfly and its inverse

**Problem.** Transform $[1,2,0,0]$ modulo 17 with positive-exponent root 4. Recover coefficient 1 from the inverse formula. Diagnose what happens if the inverse normalization is omitted.

**Solution.** Even coefficients $[1,0]$ have transform $E=[1,1]$ at root $4^2=16$. Odd coefficients $[2,0]$ have $O=[2,2]$. Butterfly k=0 gives $Y_0=1+2=3$ and $Y_2=1-2=-1\equiv16$. Butterfly k=1 gives $Y_1=1+4\cdot2=9$ and $Y_3=1-4\cdot2=-7\equiv10$. Outputs must be placed at indices 0,2 and 1,3 respectively, not in the order in which a casual drawing lists them.

The inverse root 13 has successive powers $1,13,16,4$. For coefficient $a_1$, the unnormalized inverse sum is $3+9\cdot13+16\cdot16+10\cdot4=416\equiv8$. Multiplying by the inverse length $4^{-1}=13$ gives $8\cdot13=104\equiv2$, recovering the original coefficient. Without normalization the result is 8, which is four times 2 modulo 17. The root must be primitive: using 1 would give the same sum 3 at every output and discard positional information. All operations in this example are exact residues; no floating rounding rule is involved.

### Challenge 7. Distinguish circular aliasing from modular ambiguity

**Problem.** Multiply coefficient arrays $[1,2,3]$ and $[4,5]$. Compare length-two circular convolution, length-four convolution modulo 17 and exact integer recovery under a coefficient bound of 30.

**Solution.** Direct multiplication gives $c_0=4$, $c_1=5+8=13$, $c_2=10+12=22$, $c_3=15$. Length two wraps exponents modulo two, returning $c_0+c_2=26$ and $c_1+c_3=28$. This is an index collision, so increasing only the arithmetic modulus cannot recover all four positions.

Length four meets the padding requirement and preserves every position, but modulo 17 yields $[4,13,5,15]$. At index two, residue 5 can represent either 5 or 22 within $[0,30]$. Padding alone cannot choose the correct integer. For signed coefficients in $[-30,30]$, a modulus product above 60 ensures uniqueness. A single NTT prime 97 supports length four because four divides 96; root 22 has $22^2\equiv-1$ and hence exact order four. Modulus 97 also exceeds 60, so centered recovery is unambiguous for this bound. These two certificates—sufficient transform length and sufficient residue range—must both be checked. The actual coefficient 22 is safely recovered in the 97 transform, while 17 deliberately demonstrates the missing information.

### Challenge 8. A tight five-group pivot certificate

**Problem.** There are 25 distinct keys in five full groups of five. The pivot is the median of the five group medians. Find a guaranteed strict-smaller count and an input attaining it. Bound the larger strict partition.

**Solution.** Here $t=2$. Two group medians below the pivot certify three smaller keys per group, and the pivot's own group certifies two, giving $3t+2=8$. Construct groups $[-30,-29,-28,1,2]$, $[-27,-26,-25,3,4]$, $[-2,-1,0,5,6]$, $[7,8,9,10,11]$, $[12,13,14,15,16]$. Their medians are −28, −25, 0, 9 and 14, so the selected pivot is 0. Exactly the first groups' six negative keys and the pivot group's two negative keys are below it: eight keys.

There are sixteen strictly larger keys, meeting the maximum $25-1-8=16$. Thus the guarantee eight is tight under these conditions, rather than merely an estimate of 30 percent. The pivot itself is excluded from both strict sides. Counting its whole three-key lower half would overstate the strict guarantee by one. Full groups and distinctness are stated premises; incomplete groups or equal medians need different floor and equality handling. The construction proves attainability of the certificate, not the worst running-time realization of every level of a selection algorithm.

### Challenge 9. Stability requires identity-aware run order

**Problem.** Four equal-key records have original identities 0,1,2,3. One child contains identities $[0,2]$, another $[1,3]$. Each child is internally stable. Does an equality-left-first merge produce a globally stable result? Repair the design.

**Solution.** With equal keys, left-first selection emits 0, then 2, followed by the remaining right records 1,3. The sequence $[0,2,1,3]$ reverses original identities 1 and 2, so global stability fails. Internal child stability alone says only that 0 precedes 2 and 1 precedes 3; it says nothing about the interleaving between children.

Two repairs are valid. First, divide into adjacent original intervals, in which every original identity in the left child precedes every identity in the right. Then left-first equality plus inductively stable children proves the desired global order. Second, retain original indices and compare the pair $(\text{key},\text{original index})$ lexicographically. Then merging the two arbitrary runs emits 0,1,2,3 even if their original positions interleaved. The second repair changes the effective comparison key, so distinguish its identity tie comparison from the number of primary-key comparisons in an examination question. Sorted primary keys alone cannot detect the bug; record identities must appear in the specification and in the simulation.

### Challenge 10. A decision-tree endpoint is not an inspected key

**Problem.** A perfect BST stores keys 1 through 7. Search unsuccessfully for 8, then implement equivalent half-open array search over $[0,7)$. Count stored-key inspections, calls including the empty base, and primitive tests under a declared two-test interface.

**Solution.** The tree path inspects 4, then 6, then 7, then reaches the empty right child. There are three key inspections and four calls. The half-open array implementation computes midpoints 3,5,6 and advances its lower bound to 4,6,7. The interval finally becomes $[7,7)$ and the next call returns without reading any array cell.

If each nonempty call first tests equality and then tests less-than when equality fails, unsuccessful target 8 incurs two tests at each of the three inspected keys: six primitive key tests. A three-way comparator would incur three comparator calls instead. The final base condition incurs a control test but no key test; whether it is included depends on the problem's measured quantity. Eight possible unsuccessful gaps require at least $\lceil\log_2 8\rceil=3$ binary yes/no decisions in the ideal gap-classification tree. The two-test implementation is correct but is not automatically optimal for that interface. Finally, updating the lower bound to mid instead of mid+1 leaves $[6,7)$ unchanged and causes nontermination. The concrete endpoint trace exposes this error more clearly than quoting logarithmic complexity.
