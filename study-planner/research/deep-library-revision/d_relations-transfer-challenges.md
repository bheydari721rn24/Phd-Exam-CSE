## Ten solved synthesis challenges for relations and orders

These original problems combine the selected university methods. They supplement all forty-six retained tutorials and the forty-five rewritten bank answers. The mathematical objects, carriers and target counts are specified before each derivation.

### Challenge 1. A difference subgroup with a finite carrier restriction

**Task.** On the integers, define $x\sim y$ when the residue of $x-y$ modulo ten belongs to $\{0,5\}$. Prove equivalence, identify the infinite classes, and count the related ordered pairs after restricting the carrier to $\{0,\ldots,29\}$.

**Solution.** A difference has allowed residue if and only if it is divisible by five. Differences zero, negatives and sums therefore remain allowed, proving the three equivalence axioms. The integer classes are the five residue classes modulo five. This is not a ten-class relation merely because its initial description uses modulo ten: the allowed two-element subgroup coarsens those residues.

The finite restriction contains six numbers in each class. Explicitly, class r contains $r,r+5,r+10,r+15,r+20,r+25$, for $0\le r<5$. A block contributes six choices for each endpoint, including its six loops. Consequently there are $5\cdot6^2=180$ ordered related pairs. This is different from the thirty carrier elements and from the universal carrier square of nine hundred pairs. All five finite classes are nonempty, so the quotient still has five elements.

The restriction is induced: both endpoints must belong to the finite interval. Equivalence survives induced restriction, but an infinite pair-count formula would not be a finite numerical answer. Derive the restricted block sizes before counting them.

### Challenge 2. Equal partition counts do not determine relation sizes

**Task.** Count partitions of a labelled seven-element carrier into blocks of sizes three and four. Then count partitions of a labelled eight-element carrier into two size-four blocks. Compare both partition counts and their relation pair counts.

**Solution.** In the seven-element problem, choosing the three-element block uniquely determines its complement, so $\binom73=35$. Do not divide by two: the unequal sizes distinguish which selected subset plays that role. Each such equivalence has $3^2+4^2=25$ pairs.

For eight elements, choosing one four-element block gives $\binom84=70$, but either of the two equal-sized blocks can be selected first. Every partition is counted twice, so $70/2=35$. Each resulting equivalence has $4^2+4^2=32$ pairs. Thus the number of possible relations is thirty-five in both cases, while the size of one relation differs.

The factorial formulas confirm the distinction: $7!/(3!4!)=35$ and $8!/((4!)^2 2!)=35$. The block-order symmetry factor applies exactly when the equal-size blocks are interchangeable. It does not remove the labels of the carrier elements.

### Challenge 3. Symmetric serial relations require inclusion–exclusion

**Task.** On a labelled three-element carrier, count relations that are symmetric and serial, with loops allowed. How many remain if transitivity is additionally required?

**Solution.** A symmetric matrix has three diagonal bits and three unordered-pair bits, hence sixty-four possibilities. Seriality says no row is empty. Let $E_i$ be the event that vertex i has no outgoing edge. Symmetry also removes every incoming edge to that vertex. Fixing one empty row leaves a symmetric relation on two vertices, giving $2^3=8$ possibilities. Fixing two empty rows leaves one optional loop, giving two possibilities. Fixing all three leaves only the empty relation. Inclusion–exclusion therefore gives
$$64-3\cdot8+3\cdot2-1=45.$$
This is not the arbitrary directed serial count $7^3=343$: symmetry ties off-diagonal entries and prevents independent row choices.

If a symmetric transitive relation is serial, choose an outgoing witness $aRb$ for each a. Symmetry supplies $bRa$, and transitivity forces $aRa$. Thus it becomes reflexive and is an equivalence. Conversely, an equivalence is symmetric, transitive and serial. There are five partitions of three labelled elements: one three-element block, three choices for a two-element block plus singleton, and the all-singleton partition. Hence exactly five of the forty-five relations meet the added condition.

### Challenge 4. Transitive closure can destroy intersection equality

**Task.** On $\{a,b,c,d\}$, take $R=\{(a,b),(b,c)\}$ and $S=\{(a,d),(d,c)\}$. Compare $(R\cap S)^+$ with $R^+\cap S^+$ and prove the inclusion direction valid for every input pair.

**Solution.** The original edge sets are disjoint, so their intersection and its positive closure are empty. Closing R adds $(a,c)$ via b; closing S adds the same endpoint pair via d. Their closures have exactly that pair in common. Thus $R^+\cap S^+=\{(a,c)\}$ and equality fails.

For any relations, a path whose every edge belongs to their intersection is simultaneously a path in each operand. Its endpoint pair therefore lies in both closures, proving $(R\cap S)^+\subseteq R^+\cap S^+$. The converse can fail because the two witnesses need not share any intermediate edges. The output closure need not preserve intersections even though the property “is transitive” is preserved under intersections. Those are different assertions about different objects.

### Challenge 5. Symmetric and transitive closure order changes the pair count

**Task.** On four vertices, let $R=\{(a,b),(a,c),(c,d)\}$. Let s add reversed edges and t take positive transitive closure. Compute sizes of $s(t(R))$, $t(s(R))$, and the least equivalence containing R.

**Solution.** Positive closure of R contains its three edges and shortcut $(a,d)$; there is no other outgoing continuation and no cycle. Symmetrizing those four edges adds four distinct reverses, giving eight pairs. No loop is included at this step.

Symmetrizing first makes the undirected connection tree a–b, a–c, c–d traversable in both directions. Any vertex can reach any other, and every vertex has a neighboring edge along which it can travel out and back. Positive closure therefore contains all sixteen pairs, including four loops. The least equivalence is also the universal relation, because these original connections force one class containing all four vertices.

The noncommuting results are eight versus sixteen. A transitivity witness missing from the smaller relation is $bRaRc$ without $bRc$. Adding only reflexive loops to that eight-pair relation would still leave this missing shortcut. The order of operations has mathematical consequences beyond the diagonal convention.

### Challenge 6. Linear extensions of the twelve-divisor grid

**Task.** For divisors of $72=2^3 3^2$ under divisibility, find height, width and the number of linear extensions. Derive a finite recurrence for the last count rather than interpreting a single Hasse path as a total listing.

**Solution.** Exponent coordinates form a four-by-three grid. Rank i+j increases along each strict comparison, so height is six, attained by $1,2,4,8,24,72$. Keeping j fixed partitions the grid into three chains, so width is at most three. The three vertices with coordinates $(2,0),(1,1),(0,2)$ are mutually incomparable, attaining width three.

A prefix of a linear extension must be an order ideal: if a divisor has been listed, every strictly smaller divisor has already been listed. Describe the occupied lengths of the j=0,1,2 rows by $(a,b,c)$, where $0\le c\le b\le a\le4$. Each row is a prefix because comparison along that row is a chain; the inequalities express the downward comparisons between rows.

Let F(a,b,c) count legal prefix listings of exactly that ideal. The empty listing has F(0,0,0)=1. Remove the last listed vertex. It must be maximal in the ideal and can be the last vertex of row zero when a>b, of row one when b>c, or of row two when c>0. Thus
$$F(a,b,c)=\mathbf1_{a>b}F(a-1,b,c)+\mathbf1_{b>c}F(a,b-1,c)+\mathbf1_{c>0}F(a,b,c-1),$$
with omitted terms treated as zero. The final-vertex choices are disjoint and exhaustive, proving the recurrence rather than guessing it from a pattern.

Evaluating states by increasing a+b+c gives F(1,1,1)=1, F(2,2,2)=5, F(3,3,3)=42 and F(4,4,4)=462. Therefore there are 462 linear extensions. By contrast, a saturated path from the least to greatest divisor contains only six of the twelve vertices and has ten possible increment orderings. The counts 462 and ten concern different objects: a total legal listing of all tasks versus one longest chain.

### Challenge 7. Intersect partitions, then close their union

**Task.** On $\{1,\ldots,6\}$, equivalence E has blocks $\{1,2,3\},\{4,5,6\}$ and equivalence F has blocks $\{1,4\},\{2,5\},\{3,6\}$. Find the pair counts of E, F, their intersection, their union and the union's equivalence closure.

**Solution.** E has $2\cdot3^2=18$ pairs, while F has $3\cdot2^2=12$. An E-block intersects each F-block in exactly one element. The common refinement is therefore six singleton blocks; $|E\cap F|=6$. Inclusion–exclusion gives $|E\cup F|=18+12-6=24$.

Each F-block provides a bridge between the two E-blocks. Since an equivalence already relates all elements inside an E-block, one bridge forces both blocks to merge in any equivalence extension. The closure thus has a single six-element block and thirty-six pairs, adding twelve pairs to the unclosed union.

A direct missing-pair witness is 1 related to 2 by E and 2 related to 5 by F, while 1 and 5 are in neither a common E-block nor a common F-block. Transitivity fails before closing. Sum-of-squares counts apply to the equivalence operands and their equivalence closure; they cannot be applied to the union as if its overlapping original blocks were a partition.

### Challenge 8. Boolean composition and numerical witness counts

**Task.** Source A and middle B each have three elements, and target C has two. In the specified orders, matrices are
$$M_R=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix},\qquad M_S=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}.$$
Compute $S\circ R$ and distinguish its number of pairs from the number of two-edge witnesses.

**Solution.** Numerical multiplication gives
$$M_RM_S=\begin{pmatrix}2&1\\1&2\\1&1\end{pmatrix}.$$
The first row's first entry is two because middle vertices one and two both reach the first target. The second row's second entry is two because its middle vertices two and three both reach the second target. Each other entry has exactly one witness.

Boolean multiplication replaces addition by OR and multiplication by AND. Every numerical entry is positive, so the Boolean result is the three-by-two all-one matrix. Hence all six endpoint pairs belong to $S\circ R$, while summing numerical entries counts eight two-edge witnesses. Repeated witnesses do not duplicate membership in a set of pairs.

The symbol order of $S\circ R$ does not reverse the source-row matrix order: it is $M_R$ followed by $M_S$. A two-by-three matrix cannot be substituted for the given second matrix without changing the typed carriers. Establish dimensions and the witness definition before doing arithmetic.

### Challenge 9. Lexicographic descent without a fixed positive linear rank

**Task.** A procedure on natural pairs may call $(m,n-2)$ when $n\ge2$, or $(m-1,n^2+1)$ when $m>0$. Each call returns before a fixed finite amount of subsequent work finishes, and each invocation makes at most these two calls. Prove termination. Can a rank am+bn with fixed positive a,b certify every allowed call?

**Solution.** The first call preserves m and reduces n. The second strictly reduces m, so its possibly much larger second coordinate does not prevent lexicographic descent. Natural-number order is well-founded; choosing a least occurring first coordinate and then least occurring second coordinate proves the lexicographic order well-founded.

Use well-founded induction on argument pairs. Assuming all smaller invocations terminate, both guarded recursive calls terminate; only finitely many calls and subsequent steps occur, so this invocation terminates. Guards preserve nonnegative coordinates. This proves completion of the recursion tree, not merely termination of one arbitrarily chosen branch.

For the second call, the linear rank change is $-a+b(n^2+1-n)$. With fixed positive a,b, choose n sufficiently large to make this positive. Taking m=1 still permits that call. Thus no such fixed positive linear rank certifies all transitions. The absence of this particular rank does not refute termination; the lexicographic relation supplies the actual proof.

### Challenge 10. Changing the carrier changes a join and distributivity

**Task.** Delete divisor six from the divisor lattice of twelve, leaving $\{1,2,3,4,12\}$ under divisibility. Is the resulting poset a lattice? Find the join of two and three, and test one distributive identity.

**Solution.** The remaining shape is a chain $1<2<4<12$, plus vertex three strictly between bottom one and top twelve and incomparable with two and four. Every comparable pair has its smaller member as meet and larger member as join. The only incomparable pairs are (2,3) and (4,3); both have meet one and join twelve. This exhaustive pair classification proves it is a lattice.

The join of two and three is twelve, not their numerical lcm six, because six is absent from the carrier. Twelve is the only common upper bound still available, so it satisfies both the upper-bound and leastness obligations. A formula from a larger ambient lattice must not silently insert a missing object.

Now take a=4,b=2,c=3. Then $b\vee c=12$, giving $a\wedge(b\vee c)=4$. But $a\wedge b=2$ and $a\wedge c=1$, so $(a\wedge b)\vee(a\wedge c)=2\vee1=2$. The unequal outputs four and two disprove distributivity. This five-element pentagon lattice is finite and therefore complete under the chapter's nonempty-lattice convention; completeness does not imply distributivity.
