# Arrays: replacement derivations, PA13–PA48

## PA13 | Relative indices belong to a pointer's array domain

The pointer p designates a[4], whose value is ten. Subscript syntax means pointer displacement followed by access: p[k] selects a[4+k] when that element exists. Consequently p[-3] selects a[1] and reads four, while p[2] selects a[6] and reads fourteen.

Solve the access constraint before interpreting any other displacement:

$$0\le4+k<7\quad\Longleftrightarrow\quad-4\le k\le2.$$

The lower endpoint selects a[0], and the upper selects a[6]. Pointer formation has a slightly larger range: k equal to three forms a+7, the one-past pointer. That endpoint is useful for a boundary comparison or legal same-array subtraction, but not for an evaluated element access. A displacement below minus four or above three exceeds even the pointer-formation domain.

The negative sign is therefore not inherently an error and does not invoke Python's indexing-from-the-end convention. Its legality follows from p's interior position in this same live initialized array. A pointer with the same numerical address but no established object relation would require a separate argument; numerical arithmetic alone is insufficient.

## PA14 | sizeof measures the declared operand type

Where a is the actual nine-int array object, its size is $9\cdot4=36$ bytes and an element's size is four. The quotient is therefore nine. The array operand of sizeof does not undergo the usual conversion to a pointer.

Inside the parameter declaration `void f(int a[9])`, the parameter is adjusted to `int *a`. No nine-element array parameter object is created. Under the stated pointer size, sizeof a is eight and sizeof a[0] is four, giving the quotient two. That two is a ratio of type sizes, not a discovered sequence length.

The two expressions have identical spelling but different operand types. Changing the caller's actual array length does not change the adjusted pointer type or its sizeof. Conversely, changing the implementation's pointer size can change the misleading parameter quotient without changing the caller's nine elements.

These fixed-type sizeof expressions do not read any element value. To process the actual sequence, pass a length and require that it matches accessible initialized storage; merely writing nine inside ordinary array-parameter brackets does not supply the length at runtime.

## PA15 | Whole-array and element strides differ

In a+1, ordinary expression conversion first gives a pointer to the first int. Adding one advances to the next int, a numerical displacement of four bytes under this problem's stated model. Its resulting type is int*.

Unary & instead preserves the array object as its operand. The type of &a is a pointer to an array of six ints, written `int (*)[6]`. Adding one advances by one whole pointed-to array, numerically $6\cdot4=24$ bytes. The result is one past that entire object and does not designate a second live six-int array.

Both original pointers correspond to the beginning of the same storage because the first element starts at the array's beginning. A common starting location does not erase the pointed-to type, which determines the arithmetic unit. The byte displacements are statements in the specified representation; C does not generally promise that casting pointers to integers produces a universally linear address encoding.

Formation of the whole-array one-past pointer is permitted. Evaluated access through it is not. Changing the array extent to seven would change the whole-array stride to twenty-eight while leaving the element stride four.

## PA16 | A rectangular row is an array, not a pointer slot

The compatible declaration is `int (*p)[5] = m`. Conversion of the outer array gives a pointer to its first five-int row. Each row occupies twenty bytes, so p+2 advances forty bytes and designates m[2].

The expression *(p+2) is that five-element row-array lvalue. In an ordinary value context it can convert to a pointer to m[2][0]; as the operand of sizeof it retains its array type. Therefore `sizeof *(p+2)` is twenty bytes, not the size of an int pointer.

An int** expects a pointer to an int* object. The rectangular matrix stores rows of integers and has no intervening array of row-pointer objects. A cast does not construct those missing objects, so using an int** interpretation is not a representation repair.

There are three separately valid row positions for p-relative row access: zero, one and two. After selecting a row, a column access must also be in zero through four. The two-dimensional numerical offset formula counts storage correctly only when the actual typed accesses respect those separate row and element domains.

## PA17 | An enclosing allocation does not remove a row boundary

The converted m[0] points into the first three-int row object. Relative element pointers p, p+1 and p+2 designate that row's elements, while p+3 is its one-past pointer. Forming p+4 already exceeds that row's permitted pointer-arithmetic domain. Thus p[4] is not justified by the fact that the enclosing rectangular matrix occupies contiguous storage.

The intended element can instead be selected as m[1][1]. The first subscript selects a valid row of the outer two-row array, and the second selects a valid element of that row. Its flat numerical offset is four, but numerical offset and legal typed evaluation are different propositions.

A genuine flat six-int array would have a different relevant element-array domain and could permit flat[4]. The distinction is not whether a processor could reach the bytes. The C object model sets the arithmetic boundary. The public C draft's Annex J.2 explicitly lists an out-of-range multidimensional index despite apparently accessible adjacent storage, reinforcing this point. No compiler observation of a convenient output would establish portable behavior for the invalid expression.

## PA18 | Bounds and initialization are separate obligations

The aggregate initializer supplies a[0] equal to nine and a[1] equal to two. Omitted elements of this initialized aggregate receive zero initialization, so a[2], a[3] and a[4] are zero. The requested a[4] is therefore zero even though only two values were explicitly written.

The block-scope static array c has static storage duration. With no explicit initializer, its integer elements are zero-initialized, so c[4] is also zero. This is a storage-duration initialization guarantee, not a claim that every block-local array starts cleared.

The ordinary automatic b has no initializer. Its element at index four has an indeterminate value; the declaration does not justify a portable numeric result from reading it. Index four is within the allocated five-element array, so the issue is initialization rather than bounds.

A correct access argument checks three facts: the object is alive, the selected index belongs to it, and the stored value can be used under the language rules. Zeroing b explicitly, initializing it with `{0}`, or giving it static storage would change the last fact. Changing arbitrary observed bytes or guessing previous stack contents is not a valid substitute.

## PA19 | Array conversion does not make an array assignable

The positive-bound declarations int a[3] and int b[3] are valid. The assignment a=b violates a constraint: the assignment's left operand must be a modifiable lvalue, and an array is not one. Usual expression conversion does not turn the original array object into a writable pointer variable.

The constant bound in int z[0] is zero, violating the positive-bound requirement for this standard fixed array declaration. A compiler may diagnose and then accept an extension; that does not change its standard-C classification. This differs from a runtime nonpositive variable-length bound, whose rule must be analyzed separately.

To copy initialized contents, use a bounded element loop:

```c
for (size_t i = 0; i < 3; ++i) a[i] = b[i];
```

Here the original uninitialized b must first receive valid values before this loop reads them. A suitable nonoverlapping byte copy can copy the representation of appropriate objects, but it is not array assignment syntax. Assigning a separate pointer p=b redirects p and copies no array contents. These are distinct operations with different effects.

## PA20 | A legal endpoint is not an accessible element

For this four-element array, a+4 is the permitted one-past pointer. Its formation does not read array contents. It can serve as an exclusive iteration boundary even though it designates no fifth element.

Evaluating *(a+4) as an element indirection is not a valid access. In contrast, a+5 is already outside the permitted pointer-formation range, so no dereference is needed to expose that arithmetic error. The initialized values of the four existing elements do not repair either violation.

The subtraction (a+4)-a uses the same array and its one-past boundary. It gives four in units of elements, subject to representability in ptrdiff_t. It does not need to read a value at the endpoint. Reversing its operands gives minus four under the same representability condition.

The classification concerns evaluated operations. Unevaluated fixed-type sizeof operands and the special cancellation rules for expressions such as &*p need their own analysis; they should not be used to justify an ordinary out-of-bounds read. Keep pointer formation, same-object distance and element access as three separate checks.

## PA21 | Terminate before unsigned wraparound

Because size_t is unsigned, its stored values are never below zero; i>=0 cannot terminate the proposed loop. At n equal to zero, initialization stores the converted value SIZE_MAX in i. For a nonempty array, reaching zero and decrementing similarly produces the maximum unsigned value instead of a negative stopping sentinel. The following access is not a valid reverse traversal.

Use a boundary and decrement before access:

```c
for (size_t i = n; i > 0; ) {
    --i;
    use(a[i]);
}
```

At every guard, $0\le i\le n$. A true guard establishes i positive, so decrement produces a valid index from zero through n-1. The first accessed index is n-1 when n is nonzero; subsequent iterations decrease it by one. After the final access at zero, the next guard sees zero and exits without another decrement.

The variant is the boundary i itself, which decreases on each executed iteration and cannot pass below zero. When n is zero, the body is skipped, including all array access. This proves both the order and the exact n-access count without treating wraparound as termination.

## PA22 | Count an arithmetic progression under a strict guard

Write a visited index as $i=3+4t$, where t is a nonnegative iteration number. The condition i<26 becomes $4t<23$, hence t can be zero through five. There are six visits: 3,7,11,15,19,23. The last visited index is twenty-three, and the next candidate twenty-seven fails the guard.

Equivalently, a positive stride s over a nonempty half-open interval [l,r) has $\lceil(r-l)/s\rceil$ visits. Here that is $\lceil23/4\rceil=6$. The strict inequality must be retained when converting from an endpoint to an integer count.

Changing the guard to i<=26 happens not to change this example because twenty-six is absent from the progression. At endpoint twenty-seven, the strict guard still excludes that candidate whereas the non-strict guard includes it. A numerical coincidence is therefore not an equivalence proof.

Finally, a zero-based array serving these accesses needs at least twenty-four elements, not merely six. Six counts visits, while twenty-three is the largest accessed coordinate. In actual machine code, the final increment and any arithmetic used to form indices need their own representability check.

## PA23 | Count comparisons and successful assignments separately

Initialize the minimum to the first five and scan the six later positions. The second five ties and does not replace a strict minimum; two at index two replaces five; the next two ties; seven is larger; one at index five replaces two; the final one ties. Thus there are six comparisons and two successful updates, with the first minimum occurrence retained at index five.

With a mathematical positive-infinity initialization, all seven elements are compared. The first five now causes an additional successful replacement. The subsequent strict decreases are the same two and one, giving seven comparisons and three updates. Positive infinity is a stated mathematical sentinel, not an arbitrary finite integer constant assumed above every possible input.

Using non-strict comparison would replace on ties too. For this data it would give five updates after first-element initialization, or six after infinity initialization, and retain the last one at index six. That is a different algorithmic policy.

The original strict algorithm's comparison count follows from its scan boundaries; its update count follows from record-low events in the actual data. Neither count alone identifies the other, and a correct final minimum value does not establish the tie index or number of assignments.

## PA24 | Prove the weighted prefix that is actually accumulated

The four products are $1\cdot2=2$, $2\cdot(-1)=-2$, $3\cdot4=12$ and $4\cdot3=12$. Their sum is twenty-four. The running totals after each access are two, zero, twelve and twenty-four.

At a loop boundary use

$$0\le i\le4,\qquad S=\sum_{k=0}^{i-1}(k+1)A[k].$$

Initially i is zero and S is the empty sum zero. A true guard i<4 proves the next element access valid. Adding (i+1)A[i] appends exactly the missing weighted term, and incrementing i restores the stated prefix relation. At exit i=4, the invariant gives the entire required sum. The variant 4-i proves termination.

Using i instead of i+1 changes the products and gives sixteen here, not twenty-four. The unweighted total is eight, another different reduction. The invariant must describe the implemented weighting, not merely mention a generic sum. The question uses mathematical integers; a C implementation would additionally need every multiplication and every partial addition to fit, not just its final result.

## PA25 | Prefix entries label boundaries

Set P[0] to zero and successively add the five data values. This constructs P = [0,3,1,6,7,3]. Entry P[t] is the sum of exactly the first t elements, so five elements require six boundary entries.

The sum on [1,4) is $P[4]-P[1]=7-3=4$, agreeing with the direct sum minus two plus five plus one. The whole-array sum is $P[5]-P[0]=3$. The empty query [3,3) subtracts P[3] from itself and gives zero without accessing a data element.

For general boundaries, subtracting the first l elements from the first r elements cancels precisely the unwanted prefix, leaving indices l through r-1. Replacing P[r] by P[r-1] would omit the last included element and break the empty-range convention.

The table summarizes a particular data state. After a point update at index j, every P[t] with t>j is affected. Reusing the old table without repair would answer queries about the previous array. Thus the constant-time query guarantee assumes valid preprocessing for the current values; it is not a constant-time arbitrary-update data structure.

## PA26 | A right boundary cancels a contribution

Use six boundary slots for five data elements and initialize all slots to zero. Adding four on [1,4) records plus four at boundary one and minus four at boundary four. Subtracting two on [2,5) records minus two at boundary two and plus two at boundary five. Their combined difference array is [0,4,-2,0,-4,2].

Accumulate the first five entries: the running values are zero, four, two, two and minus two. Hence the resulting data array is [0,4,2,2,-2]. Direct interval membership independently confirms it: index one receives only four, indices two and three receive four minus two, and index four receives only minus two.

The final sentinel two cancels the remaining minus-two contribution beyond the data range. Including that sixth accumulated boundary as a data value would incorrectly invent another element. It exists to express the exclusive endpoint, not to extend the logical array.

An empty update at identical boundaries adds and subtracts at the same boundary and has no effect under this six-slot contract. An n-slot implementation must instead treat an empty update as a no-op before attempting an endpoint access at n. The storage contract determines which boundary writes exist.

## PA27 | Rectangle subtraction restores a doubly removed overlap

The boundary prefix table is

$$P=\begin{bmatrix}0&0&0&0\\0&1&3&6\\0&5&12&21\end{bmatrix}.$$

P[i,j] contains rows before i and columns before j. The selected rectangle uses row boundaries zero and two and column boundaries one and three. Its sum is

$$P[2,3]-P[0,3]-P[2,1]+P[0,1]=21-0-5+0=16.$$

Directly adding the four selected entries 2,3,5,6 also gives sixteen. This independent check detects an indexing convention mismatch.

For an arbitrary rectangle, begin with the prefix ending at its lower-right boundary. Remove the prefixes above and left of it. Their intersection has then been removed twice, so add it back once. That explains the final plus sign rather than treating it as a mnemonic.

The zero boundary row and column handle top and left edges without negative subscripts. Equal row boundaries or equal column boundaries make the expression cancel to zero, as an empty rectangle requires. Each table entry itself needs a safe partial-sum representation in a machine implementation; a mathematically correct inclusion-exclusion identity alone does not guarantee absence of intermediate overflow.

## PA28 | Increasing updates consume an already accumulated predecessor

Starting with [1,2,3,4,5], the four writes produce [1,3,3,4,5], [1,3,6,4,5], [1,3,6,10,5] and [1,3,6,10,15]. The key observation is that the right-hand predecessor has already been updated when the next statement reads it.

Let A0 denote the original array. Before processing index i, every earlier position k holds its original prefix sum, while positions from i onward remain original. The update at i adds original A0[i] to the established prefix at i-1, yielding

$$A[i]=\sum_{k=0}^{i}A_0[k].$$

This extends the invariant by one position; index zero supplies the base prefix. After the final write the entire array contains inclusive prefix sums. All visited indices and their predecessors are within the five-element array.

The expression A0[i]+A0[i-1] describes a snapshot-neighbor transformation, not this execution, because it discards the dependency on the modified predecessor. The difference is algorithmic, not undefined behavior: these are sequential complete assignments. For length zero or one, a correctly guarded loop performs no writes. Fixed-width execution also requires every accumulating prefix to fit.

## PA29 | Decreasing updates preserve the source neighbor

Processing indices four, three, two and one produces [1,2,3,4,9], [1,2,3,7,9], [1,2,5,7,9] and [1,3,5,7,9]. Unlike the increasing traversal, each predecessor lies at a smaller index and has not yet been changed.

Thus for every processed i>0, both values read are still A0[i] and A0[i-1], giving the final relation $A[i]=A_0[i]+A_0[i-1]$. Index zero is never assigned and retains A0[0]. A descending invariant states that the already processed suffix has this neighbor-sum value, while the unprocessed prefix remains original.

The update decreases the suffix boundary by one and cannot change any still-unread lower predecessor. This proves preservation and explains why the same statement computes a different map when its direction changes. There is no need to invoke unspecified evaluation order: the two array reads in each assignment do not conflict with an unsequenced independent modification.

If a prefix sum is intended, use the increasing traversal. If original adjacent sums are intended, use this direction or an explicit snapshot. The required postcondition, rather than a preference for forward loops, determines the correct dependency order.

## PA30 | A valid access can still destroy an unread value

The requested forward loop writes A[1]=2 at t=0. At t=1, it reads that newly changed A[1], so A[2] becomes two. The same dependency repeats: A[3] and A[4] also become two. The final array is [2,2,2,2,2,12].

An original-value move would place the original source segment [2,4,6,8] into destinations one through four, producing [2,2,4,6,8,12]. Bounds alone do not distinguish these outcomes: every read and write index in the faulty forward loop is valid. The failed obligation is preservation of future source values.

After its first write, the loop has overwritten source position one before the next read. Induction then explains the repeated two: every next source equals the preceding write. Using a postcondition that compares only final source and final destination can hide precisely this corruption.

For this rightward overlap, copy relative indices three down to zero. Each original source is read before the higher destination can destroy it. A temporary source snapshot or a valid memmove provides another correct strategy. memcpy does not permit overlapping source and destination regions, so merely replacing the loop with memcpy is not a valid repair.

## PA31 | A descending suffix invariant preserves the snapshot

The four writes are A[4]=8, A[3]=6, A[2]=4 and A[1]=2, in that order. Each reads an original source value before its cell can be overwritten. Final state is [2,2,4,6,8,12]. Positions zero and five lie outside the destination region and retain their original values.

Before relative index t is processed, every destination 1+k with k>t already equals original A0[k], and the original source prefix from zero through t is unchanged. The initial t=3 checkpoint has an empty completed suffix, so the invariant holds.

At the next step, source t is still original by that prefix condition. Writing it to t+1 extends the correct destination suffix. Because t+1 exceeds every remaining source index below t, the write preserves the next unread source prefix. Decrementing t restores the invariant; after processing zero, the complete destination segment equals the original source segment.

This proof also states a frame condition: no position outside destinations one through four is written. The source's final values need not equal its original values because source and destination overlap. The desired relation must therefore refer to A0, not an imagined immutable final source segment.

## PA32 | Leftward overlap reverses the safe direction

For increasing relative indices, destinations zero through three receive original source values at one through four: four, six, eight and ten. The successive writes give final [4,6,8,10,10,12]. Each destination is below its current source and below every future, larger source, so unread source values survive.

Decreasing order starts by writing A[3]=A[4]=10. The next step reads A[3], now ten, and writes that into A[2]. Ten then propagates through A[1] and A[0], giving [10,10,10,10,10,12]. The operation is within bounds but violates the original-value move postcondition.

The ascending proof uses a correct copied target prefix and an unchanged unread source suffix. Writing the next lower destination cannot affect that suffix, which establishes preservation. This is the dual of the descending proof for rightward overlap.

The correct rule compares integer offsets in one known backing array: rightward overlap requires descending copying, leftward overlap permits ascending copying, and identical regions require no change. Disjoint regions can tolerate either direction. General ordering comparisons on unrelated C pointers are not a portable substitute for these known-array offset conditions.

## PA33 | A postcondition can be both too weak and false under aliasing

Use one backing array [1,2,3,4], with source zero, target one and length three. Forward copying produces [1,1,1,1]. Final source and final destination segments are equal, so a final-to-final equality may hold even though the intended original-value result [1,1,2,3] was not obtained. That specification is too weak to distinguish corruption.

For the opposite leftward move, forward copying gives [2,3,4,4]. The final source segment [3,4,4] differs from the correct target [2,3,4], so the same final-to-final equality can reject a correct move. Both examples satisfy the numerical bounds.

A useful specification refers to the source snapshot at entry: every final target position equals its corresponding original source value. Its proof additionally needs interference control, such as distinct arrays, disjoint ranges, a temporary snapshot, or the appropriate overlap-safe direction.

For bounded machine indices, validate ranges without a potentially overflowing sum: first establish start<=length, then count<=length-start. Even a bounds precondition can be defective if it tests a wrapped start+count. These repairs strengthen the reviewed CMU copying exercise rather than blindly importing a flawed alias or arithmetic assumption.

## PA34 | The source snapshot is preserved by distinct storage

Let m=r-l. Initialize t=0 and require a valid destination representation of length m. At each loop boundary use $0\le t\le m$ and, for every $0\le k<t$, $B[k]=A_0[l+k]$. Distinct destination storage ensures that A remains equal to its entry snapshot.

Initialization holds because the copied prefix is empty. A true guard t<m proves destination t valid and source $l+t<l+m=r\le n$. Writing B[t]=A[l+t] establishes the missing equality at k=t. Incrementing t extends the completed prefix and preserves the bound.

At exit, t=m, so all destination positions satisfy the required relation. The nonnegative variant m-t decreases by one per iteration, proving termination. No source location is written, and no destination outside the copied prefix is touched before its turn.

For l=r, m is zero and the body is skipped; use an appropriate empty-sequence representation rather than an illegal fixed C zero-bound declaration. In a C implementation, allocation-size multiplication, allocation success and live initialized source elements are additional obligations. The abstract invariant alone does not allocate memory or establish those machine-level facts.

## PA35 | Insert by moving the suffix away from its source

The old logical length is four and capacity is six, so a new length five is available. To insert at index two, first copy A[3]=12 into A[4], then A[2]=9 into A[3], and finally store seven into A[2]. The new logical sequence is [3,6,7,9,12].

The suffix has n-k=2 old elements, so there are two shifts and one new-value store. Descending movement preserves each old suffix value until it has been copied one position right. An increasing shift would overwrite nine with a previous value before all old values had been read.

Insertion at boundary four appends instead: the suffix is empty, so there are zero shifts and one store at A[4]. Boundary n is valid for insertion although it was not a valid old-element index. In general insertion permits $0\le k\le n$ and requires capacity at least n+1.

Only the first new-length positions belong to the logical container afterwards. Spare allocated slots need not previously contain meaningful initialized values when they are assigned before reading. Capacity and logical length are therefore separate parts of the correctness argument.

## PA36 | Stable deletion changes the logical extent

Deleting index one removes six. Copy A[2]=9 into A[1], then A[3]=12 into A[2], and A[4]=15 into A[3]. The resulting logical prefix is [3,9,12,15], with length four. Three elements were shifted, matching $n-k-1=5-1-1=3$.

Ascending copying is safe because each destination is below its source and cannot overwrite a later unread source. The copied prefix invariant preserves the original order of all elements after the removed one, which establishes stability.

The old final physical slot can still contain fifteen. It remains within the allocated array but is now outside the container's logical sequence. Clearing that slot is not required for this integer-sequence postcondition, although other element types or resource/security contracts could require additional cleanup. Reporting it as a fifth logical element would ignore the length update.

Deleting the final logical element requires no shifts, while deleting index zero requires n-1 shifts. A valid deletion requires a nonempty sequence and $0\le k<n$, unlike insertion's inclusive endpoint. These bounds should be checked before evaluating n-k-1 in unsigned arithmetic.

## PA37 | Reverse pairs around the segment's center

The half-open segment [1,6) contains indices one through five, so its length is five. Pair its first and last included positions, then move both boundaries inward. The swaps are (1,5) and (2,4), producing [0,5,4,3,2,1,6]. Positions zero and six remain outside the operation.

After t swaps, the first t and last t positions of the segment equal their reversed original partners; the intervening segment is still original. Another swap extends both correct ends while preserving the untouched middle. At t=2, only index three remains, and its reversed partner is itself.

The total swap count is $\lfloor5/2\rfloor=2$. In general, the reflected partner of included index k is l+r-1-k, not l+r-k; the minus one comes from r being excluded. Starting the high partner at six would reverse a different segment.

An empty or singleton segment needs no swap. An implementation should test the remaining segment length before forming an unsigned r-1 for the empty case. The mathematical empty case does not authorize an underflowing machine index, even when no eventual element write is intended.

## PA38 | Reverse the blocks, then reverse their order

Split the original sequence into X=[0,1,2] and Y=[3,4,5,6]. Reverse X to obtain [2,1,0,3,4,5,6], reverse Y to obtain [2,1,0,6,5,4,3], and reverse the whole to obtain [3,4,5,6,0,1,2].

For arbitrary blocks, reversing a concatenation reverses its block order as well as each block internally. Thus reversing reverse(X) followed by reverse(Y) yields Y followed by X, because each block's second reversal restores its internal order. This proves the rotation for all values, including duplicates; it is a position permutation rather than a comparison-based operation.

The first two reversals use one and two swaps respectively, and the final length-seven reversal uses three, for six swaps here. Each reversal uses a constant-size temporary element, so the complete operation uses constant auxiliary element storage and linear work.

For a positive length n, normalize a nonnegative left rotation k modulo n. Handle n equal to zero before taking a remainder. At k equal to zero, a direct no-op is valid; the algebraic reversal method also restores the original order but performs unnecessary work.

## PA39 | State which direction the cycle represents

The destination-to-source step map for a left rotation by eight is $f(i)=(i+8)\bmod12$. Starting at zero gives the cycle 0,8,4,0. Returning after t steps requires twelve to divide 8t. Dividing by their greatest common divisor four shows that the least positive t is three.

All cycles therefore have length three, and the twelve positions form four disjoint cycles. Representatives zero, one, two and three give cycles (0,8,4), (1,9,5), (2,10,6) and (3,11,7). This accounts for every position exactly once.

The orientation matters during implementation. The new value at destination i comes from old position f(i); following this source map with a saved element implements the left rotation. Mapping an old element to its new destination instead uses subtraction of eight modulo twelve, the inverse cycle orientation.

In general, repeated addition of k modulo positive n gives gcd(n,k) cycles of length n/gcd(n,k). Distinct values are unnecessary because the cycles concern positions. For normalized k equal to zero, every position is a one-element cycle and no movement is needed. Repeating a traversal from an already visited member would duplicate work.

## PA40 | The write boundary never overtakes the read boundary

Read the original sequence from left to right with write boundary w initially zero. Five is rejected. Two is copied to position zero; seven is rejected; four is copied to position one; six to position two; nine is rejected; eight to position three. The final logical prefix is [2,4,6,8] with length four.

At each boundary, $0\le w\le r\le7$, and positions before w are exactly the retained values from the processed original prefix before r, in encounter order. On rejection only r advances. On retention, write at w and advance both boundaries, extending the retained prefix by precisely the next qualifying value.

Because w never exceeds r, a write affects the current or an earlier position, never a larger unread one. The original value needed at r is read before that write. This proves interference safety as well as stability.

Spare positions beyond new length four can retain old or copied values; they are not part of the logical result. If no elements qualify the result is an empty prefix, and if all qualify the values remain in their original order. The predicate and capacity contract, not the physical contents of the spare suffix, determine correctness.

## PA41 | Difference extraction must preserve the original predecessor

Process indices three, two and one. The first subtraction is ten minus nine, storing one at index three. Then nine minus five stores four at index two, and five minus three stores two at index one. The result is [3,2,4,1].

At a descending checkpoint, completed suffix positions hold original adjacent differences and the remaining prefix is unchanged. The next predecessor lies inside that unchanged prefix, so each subtraction uses two original values. Retaining index zero provides the initial value needed to reconstruct the original sequence later.

Forward order instead first stores two at index one. The next subtraction uses that modified two and gives seven at index two; the last uses the modified seven and gives three. It produces [3,2,7,3], a different recurrence.

Forward prefix accumulation applied to [3,2,4,1] reconstructs [3,5,9,10], showing the inverse relation under exact arithmetic. A signed-machine implementation needs every subtraction and subsequent reconstruction sum to be representable. The algebraic inverse does not retroactively make an overflowing intermediate defined.

## PA42 | A clipped boundary does not imply a valid element

The list contains [0,1,2,3,4,5]. A single index minus two is normalized by adding length six, giving index four and result four. A single index still must satisfy the element domain after normalization.

For the positive-step slice [-8:20:3], start minus eight lies before the beginning and clips to zero; stop twenty clips to six. The normalized progression is range(0,6,3), selecting indices zero and three and producing [0,3]. For [8:20], both forward boundaries clip to six, so the resulting slice is empty.

In contrast, a[8] raises IndexError, and a[-8] also raises IndexError: adding six gives minus two, still outside the normalized element domain. Slice clipping does not repeatedly wrap indices or make these element accesses safe.

The slicing operation constructs a new outer list of selected references and leaves the original list unchanged. Here all elements are immutable integers; for nested mutable elements, an outer slice would not recursively duplicate them. Establish the normalized progression first, then count or copy its elements rather than treating the written start and stop as necessarily accessible positions.

## PA43 | An omitted negative stop is a distinct sentinel

For length seven and step minus one, an omitted start becomes six and an omitted stop is the before-first sentinel. The progression is 6,5,4,3,2,1,0, so a[::-1] yields that reversal.

In a[:-1:-1], the explicit minus-one stop is normalized as an ordinary negative boundary relative to the length, giving six. The omitted start is also six. A decreasing slice includes indices strictly greater than its stop; since six is not greater than six, the slice is empty.

For a[5:0:-2], the selected indices are five, three and one. Zero is excluded, and the next candidate minus one has passed the stop. The result is [5,3,1].

Python exposes the exact normalization through `slice(start,stop,step).indices(len(a))`; an omitted negative stop and a written -1 need not produce the same triple. Do not replace one with the other during algebraic simplification. A zero step is invalid and raises ValueError rather than representing an empty progression. These rules concern slicing, not C's pointer-relative negative subscripts.

## PA44 | An extended slice updates fixed selected positions

Normalize the slice [1:6:2] in a six-element list. Its progression selects indices one, three and five, exactly three positions. Matching them in order with [9,8,7] replaces those slots and yields [0,9,2,8,4,7]. Indices zero, two and four remain unchanged.

A non-unit-step extended slice assignment must supply exactly as many replacement values as selected positions. Replacing the three slots with [9,8] therefore raises ValueError; it is not a request to delete the remaining selected slot or to shift all later positions. If attempted separately on the original list with that concrete replacement, it does not produce a shortened result.

Ordinary step-one slice replacement follows a different contract and can resize a list. Consequently the statement that every slice assignment preserves length would be as incorrect as claiming every replacement may resize.

The selected count is obtained from the normalized progression, not simply stop minus start. Explicit clipping, negative steps and empty slices must be handled before matching replacement lengths. The successful assignment returns no new list value; it mutates the existing list's selected slots.

## PA45 | The second slice uses the updated sequence

The first slice [1:4] selects [2,3,4], three old values. Replacing them with [8,9] gives [1,8,9,5] of length $5-3+2=4$. The prefix before index one and suffix beginning at old index four are retained in order.

The next slice [2:2] has equal boundaries in this current four-element list. It selects no element, but step-one slice assignment inserts [6,7] at that boundary. The result is [1,8,6,7,9,5] of length $4-0+2=6$.

The second boundary is interpreted after the first mutation. It is before the current nine, not a saved reference to original index two's element. A trace based entirely on old coordinates would miss this shift.

An empty slice can therefore designate an insertion position without being a valid single-element access. Inserting at len(a) appends, although a[len(a)] itself raises IndexError. These are Python resizable-list operations; they should not be translated into C whole-array assignment, where storage capacity and explicit element movement require a separate implementation and proof.

## PA46 | Copying slots preserves the referenced inner objects

Name the initial inner lists X=[2] and Y=[5]. The outer list a has slots referring to X and Y. The slice b=a[:] creates a different outer list whose two slots initially refer to those same X and Y; it does not copy X and Y themselves.

Appending seven through b[0] mutates X to [2,7], so the first entry observed through either outer list changes. Assigning b[1]=[9] instead creates a new inner list Z and redirects only b's second slot. The corresponding slot in a still refers to Y.

The final values are a=[[2,7],[5]] and b=[[2,7],[9]]. The outer identity test a is b is false, while a[0] is b[0] is true. Their second entries are now distinct objects.

The two statements affect different levels of the object graph: append changes an inner object's contents, while slot assignment changes one edge in a particular outer container. Equal initial displayed values cannot identify which edges are shared. An accurate diagram must preserve those identities as it changes contents or redirects links.

## PA47 | List repetition repeats one row reference

The expression [0]*4 creates one row R=[0,0,0,0]. Repeating the outer list three times places three references to R into three distinct outer slots. The assignment bad[1][2]=9 selects R through the second slot and changes R itself to [0,0,9,0]. All three displayed rows therefore contain that nine.

In the comprehension, [0]*4 is executed once per iteration. It creates three distinct row objects, so assigning good[1][2]=9 changes only the second row. The first and third rows remain [0,0,0,0]. The relevant distinction is inner-list identity, not the identical initial zero values.

A shallow outer copy of bad still contains three references to the same R and does not repair independent-row behavior. Copying each row separately repairs this two-level example; deeper nested mutable elements would require another decision about how far copying must proceed.

Immutable integer zeros do not themselves cause the problem. Replacing one row slot with another integer is local to that row object. The cross-row visibility follows from sharing the mutable row container, which a correct environment diagram should show as one target with three incoming links.

## PA48 | Deletion shifts values under the advancing iterator

The list iterator first reads index zero, obtaining two. Removing that value leaves [4,6,7]. The iterator advances to index one, which now contains six, not the shifted four at index zero. Removing six leaves [4,7]. Its next index two is beyond the current length, so iteration stops. The final result is [4,7].

Four remains even because it was skipped after shifting, not because the predicate failed. A trace must record both the current sequence and the iterator's next positional index; tracking only the encountered values hides this dependency.

A separate filtered result `[x for x in a if x % 2 != 0]` reads the source without deleting positions under the iterator. If caller aliases must keep referring to the same outer list, assigning the filtered result to the full slice can replace its contents while preserving that outer identity. A read/write compaction loop is another approach with an explicit write<=read invariant.

These repairs have different identity and allocation contracts. Simply iterating the same mutating list again is not a proof that all rejected values will be removed, and replacing remove with an index deletion does not by itself cure positional skipping.
