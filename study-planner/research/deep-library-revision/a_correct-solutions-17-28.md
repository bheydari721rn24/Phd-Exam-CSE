### Solution 17

**Correct option: 1. Maintain a region, not a guessed match.** Initially lo=0 and hi=6. With the half-open loop, the first midpoint is 3. A[3]=3 is at least the target, so set hi=3; equality must not skip earlier duplicates. The second midpoint is 1, whose value is again 3, so hi=1. The third midpoint is 0, with A[0]=1 below the target, so lo=1. The boundaries meet at 1 and the loop returns index 1. The inspected midpoint sequence is therefore (3,1,0).

The invariant says every index below lo has value below 3, every index at or above hi has value at least 3, and $0\le lo\le hi\le6$. Initially the classified regions are empty. Sortedness justifies extending the appropriate region after each comparison. When lo=hi, no unclassified positions remain; index 1 is the first eligible index, not merely some occurrence of 3. The width hi−lo is a nonnegative integer and strictly decreases at every body execution.

An alternative starting with midpoint 2 uses a different midpoint or closed-interval convention. A result at 2 or 3 finds a matching duplicate but fails the first-occurrence specification. Returning zero treats the last inspected midpoint as the answer, even though that entry is below the target. Return the meeting boundary. The empty-array boundary and a target exceeding every element similarly return n, which is a legitimate insertion position but not an index to dereference.

### Solution 18

**Correct option: 2. Count body executions with the exact width recurrence.** Let L be the number of unclassified positions. A lower-bound iteration replaces L with at most $\lfloor L/2\rfloor$. Starting with 31, the worst surviving widths are 31,15,7,3,1,0. There are five transitions, hence five body executions and five inspected array entries. Initialisation and the final false guard evaluation are separate events.

More generally, the maximum number of iterations for length n is $\lceil\log_2(n+1)\rceil$ for n≥0. One way to see the precise threshold is that at most k iterations suffice for lengths at most $2^k-1$. The recurrence removes the midpoint and leaves no more than half of the previous width. For 31=$2^5-1$, five suffice, and a target outside the array's upper range realizes five steps. For n=0, the guard is false immediately, giving zero body executions.

Four iterations cannot resolve a length-31 worst path: after four maximal reductions, width 1 remains. Six usually comes from adding the final guard test to the body count, or using a loose logarithmic bound. Thirty-one would describe a linear scan. An asymptotic $O(\log n)$ statement is useful but does not determine which of nearby numeric options is correct. State the counted operation and the interval convention before using a formula.

### Solution 19

**Correct option: 1. Expose a nonshrinking singleton interval.** With array [2] and target 3, the initial boundaries are lo=0, hi=1. The midpoint is 0. Since A[0]=2 is less than 3, the faulty update sets lo=mid=0. Neither boundary changes. The next iteration has exactly the same state, makes the same comparison, and repeats forever. No out-of-bounds access is needed to demonstrate this failure.

The corrected update is lo=mid+1. In a half-open interval, the inspected midpoint has just been proved ineligible, so it belongs to the classified lower region and must be excluded from the remaining interval. Correct code changes [0,1) into [1,1), whose width is zero. The invariant may remain true under the defective update, but the strict-decrease obligation fails: a preserved relationship alone is not a total-correctness proof.

An input containing an exact match can conceal the fault because the other branch updates hi to mid and may shrink. Larger inputs may also shrink for a while before reaching a singleton. Thus successful traces are not evidence that this update terminates universally. A proposed counterexample that immediately takes the shrinking branch does not establish the stated infinite loop. The small explicit witness isolates the problematic transition and shows why adding a fixed iteration limit would merely mask the specification error rather than prove a correct result.

### Solution 20

**Correct option: 2. Verify the precondition used to eliminate a whole region.** The input is [4,1,3] with target 3. Starting at [0,3), midpoint 1 has value 1, so ordinary lower-bound code sets lo=2. Midpoint 2 then has value 3 and sets hi=2. The result is 2. Yet index 0 is already eligible because its value is 4≥3; therefore 2 is not the first index meeting the predicate.

The implementation has not suffered an indexing failure or an arithmetic failure. Its proof uses sortedness when it concludes from A[mid]<target that every earlier entry is also below target. That inference is false here: A[1]<3 but A[0]≥3. The first transition destroys the region invariant, even though lo and hi continue to satisfy the numeric bounds and the width still decreases. Termination survives while functional correctness fails.

The example does not show that binary search fails on every unsorted input. Some unsorted arrays happen to yield a correct result for a chosen target. It shows that the universal guarantee requires a monotone search predicate, typically established by sortedness. An alternative that calls the output a first occurrence also confuses lower bound with equality search; an eligible entry may exceed the target. Sort first only if changing array order is permitted by the application contract. Otherwise use a suitable scan or prove a different monotonicity premise for the searched sequence.

### Solution 21

**Correct option: 3. Use two distinct threshold predicates.** The array is [1,2,2,2,5]. Lower bound for 2 returns the first index with value at least 2, namely 1. Upper bound returns the first index with value strictly greater than 2, namely 4. Thus the requested pair is (1,4), and the half-open equal-key block is [1,4). Its width is three, the number of occurrences of 2.

For lower bound, move lo past mid only when A[mid]<2; equality moves hi left. For upper bound, move lo past mid when A[mid]≤2; equality is deliberately eliminated from the lower region. Their invariants use different comparison predicates even though their index mechanics are identical. At exit, each meeting boundary marks its own first qualifying position. Both algorithms terminate because their unresolved interval shrinks.

Returning the final occurrence index 3 as the upper bound is an inclusive-end convention, not the specified first strictly greater index. Returning zero or five fails the threshold definition for this concrete input. A pair (1,1) ignores the equality block. If the target is absent, the two boundaries coincide and the occurrence count is zero. If all values equal the target, they return 0 and n. These boundary positions are valid results even when n itself cannot be dereferenced. Convert interval conventions explicitly before extracting a count or checking a proposed answer.

### Solution 22

**Correct option: 2. Derive both branches before taking their maximum.** Let $L=hi-lo>0$ and $mid=lo+\lfloor L/2\rfloor$. The update hi=mid leaves length $\lfloor L/2\rfloor$. The update lo=mid+1 leaves length $L-\lfloor L/2\rfloor-1$. For odd length $L=2q+1$, both are q. For even length $L=2q$, the left remainder is q and the right remainder is q−1. Therefore the tight common upper bound is $\lfloor L/2\rfloor$.

The bound is attainable by the hi branch for even lengths and by either branch for odd lengths. It is a bound on the new interval's number of entries, not on the value of mid or on an inclusive endpoint difference. For L=1, both updates produce an empty interval and the bound is zero. For L=2, one branch can retain one entry; this small case rules out a universal zero-width claim.

A ceiling expression can be a valid looser estimate, but it is not the tight common bound asked for. A bound retaining the midpoint overcounts one branch and can obscure why the singleton case terminates. A statement that the length is always exactly half fails for odd lengths and for the unequal even branches. Use the floor and the removed midpoint explicitly; informal statements about halving are insufficient when an examination asks for an exact recurrence or worst-case step count.

### Solution 23

**Correct option: 3. Count shifts as strict inversions removed.** Starting from [4,2,3,1], insertion of 2 shifts 4 once and produces [2,4,3,1]. Insertion of 3 shifts 4 once and produces [2,3,4,1]. Insertion of 1 shifts 4, then 3, then 2, producing [1,2,3,4]. The total number of shifts is $1+1+3=5$. The three final placements of saved keys are writes, but they are not shifts under the stated count.

Each shift corresponds to an earlier value strictly greater than the current saved key. The original strict inversions are (4,2), (4,3), (4,1), (2,1), and (3,1), again five. An insertion moves each such greater prefix element one position right while retaining its value. This gives an independent combinatorial explanation rather than only a simulation.

Counting all writes would add key placements and obtain another quantity; counting comparisons also includes successful or failed loop conditions, depending on the model. These are not interchangeable operation counts. An answer based on the final sorted array alone misses the input-dependent work. With a strict greater-than shift condition, equal keys do not cross, which preserves their original relative order. Replacing it with greater-than-or-equal changes both the treatment of equal-key pairs and stability. Always identify the exact instruction being counted before importing an inversion formula.

### Solution 24

**Correct option: 2. Remove the logical hole before checking conservation.** When inserting saved key 2 into [1,4,2], shift 4 one position right. The physical array becomes [1,4,4], the saved key remains 2, and the hole is now index 1. The physical array temporarily contains two copies of 4 and no stored 2. Consequently, a claim that the whole physical array remains a permutation after every shift is false.

The correct invariant counts all physical positions except the hole and adds the separately saved key. Here that multiset is $\{1,4\}\uplus\{2\}$, exactly the original $\{1,4,2\}$. The value occupying the hole is ignored because it is a stale or duplicated value, not a logically retained record. Writing the saved key into index 1 closes the hole and yields the physical permutation [1,2,4]. The order proof and the conservation proof meet at that final placement.

Tracking the whole physical array plus the saved key would double-count a value; tracking only the physical array loses the saved record. A sorted-prefix condition alone cannot prove conservation. The logical-hole interpretation explains how an in-place algorithm can temporarily have duplicated physical data without discarding its logical input. This is an invariant at a specified checkpoint, with a precise representation of pending data. A different implementation using swaps needs a different intermediate conservation argument rather than this same hole annotation.

### Solution 25

**Correct option: 2. Test stability with identities, not just key values.** Take records (2,a) followed by (2,b), where a and b distinguish original positions. When the second record is inserted using a greater-than-or-equal shift condition, the first record's key 2 qualifies for shifting. Record a moves right, and saved record b is placed before it. The result is [(2,b),(2,a)]. The key sequence remains sorted, and the record multiset is preserved, but the original order of equal keys is reversed.

Stability requires equal-key records to appear in their original relative order. It cannot be checked on the unlabeled array [2,2], whose displayed values look unchanged after reversal. The strict comparison A[j]>key avoids shifting an equal predecessor, so the saved record is inserted after earlier equal records. A complete stable-sorting contract therefore includes order, conservation, and tie-order preservation as distinct obligations.

An alternative asserting that the result is unsorted confuses stability with nondecreasing key order. An alternative claiming data loss ignores that both labeled records still occur exactly once. An alternative claiming unchanged stability is refuted by this smallest pair. The defect is not that equality comparisons are intrinsically wrong; their direction must match the desired stable placement. This example also explains why a proof using only numerical keys cannot establish every property promised for records carrying associated data.

### Solution 26

**Correct option: 3. Stop comparing heads when a run is exhausted.** Merge [1,4,7] and [2,3,8]. Compare 1 with 2 and emit 1. Compare 4 with 2 and emit 2. Compare 4 with 3 and emit 3. Compare 4 with 8 and emit 4. Compare 7 with 8 and emit 7. The left run is now exhausted, and the remaining 8 is copied without another comparison between two valid heads. Thus there are five head comparisons.

After each comparison, the emitted prefix contains exactly the consumed entries and is sorted; every remaining entry is at least its last emitted key. Both input runs must themselves be sorted for this implication. Once either run is exhausted, the other is a sorted suffix and can be appended. Testing whether a pointer has reached the end is a boundary test, not the same operation as comparing two head values.

Counting six confuses the output length with head comparisons. Counting fewer misses one of the explicit pairs. Counting all guards and pointer checks would require a separately specified implementation. For two nonempty runs of lengths a and b, the maximum is a+b−1, attained here with a=b=3. A empty run needs zero head comparisons. For stability, choose the left head on equal keys when the left run precedes the right in the original array; the present distinct-key trace cannot alone demonstrate that tie rule.

### Solution 27

**Correct option: 1. A one-property checker cannot certify a two-property contract.** A sorting postcondition requires the output to be ordered and to preserve the complete input multiset. A routine that overwrites all entries with zero always produces a nondecreasing array. For input [3,1], however, its output [0,0] does not preserve either original value. A verifier that checks only sortedness accepts this invalid result.

The weakness is a missing specification obligation, not a counterexample to the sortedness check's implementation. Sortedness is a necessary property but insufficient for sorting correctness. Conversely, a checker that verifies only the multiset accepts an unsorted permutation, such as unchanged [3,1]. Both properties must be established. If stability is also promised, equal-key record order adds a third obligation; neither key sortedness nor multiset preservation implies it.

Zeroing can coincidentally be a correct result for an all-zero input. That exceptional input does not rescue the claim that the routine sorts every admitted input. To refute a universal guarantee, one explicit admitted failing input suffices. To certify a particular output, check every promised property for that particular input and result. If the application requires associated records rather than bare keys, compare whole records or a trustworthy original-index certificate, not just the key multiset. The lesson is to derive the checker from the full contract rather than from a visually pleasing output.

### Solution 28

**Correct option: 2. The base case must cover every minimal admitted input.** Suppose merge sort returns only when n=1. On an empty input, n=0 does not satisfy that condition. Splitting it yields empty children with size zero, and the recursive call repeats the same unresolved situation. Along that call path, the measure n does not strictly decrease. The function never reaches its sole base case.

The usual repair is a base condition n≤1, assuming the size is always a nonnegative integer. Both empty and singleton arrays are already sorted and preserve their own elements. For n≥2, proper halves are strictly smaller, so strong induction and the natural-valued termination measure apply. The two parts of the argument are inseparable: a decreasing measure above the base region does not compensate for a missing admitted boundary case.

Calling the failure a merge-comparison error misidentifies its location; no meaningful pair of nonempty runs is reached on this path. Claiming that the empty result is automatically returned assumes code that is absent. Claiming that a zero-length child eventually becomes length one reverses the split operation. A different contract explicitly excluding empty inputs could make n=1 a sufficient base case, provided every recursive call preserves that exclusion. The displayed routine is intended to accept empty input, so weakening the advertised domain is not a valid proof of its existing specification.
