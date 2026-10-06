# Searching, Selection, and Order Statistics

## Written sources and how to use this chapter

This chapter combines the complementary strengths of five reviewed university courses. MIT supplies a finite-size deterministic proof; Stanford supplies selection correctness and group-size analysis; Carnegie Mellon supplies the probability and cost-model distinctions; Princeton supplies searching contracts and partition implementation; Berkeley's assigned text supplies duplicate-aware three-way selection. Exact reading scopes and rejected candidates are recorded in the [source audit](../reviews/a_select-sources.html).

Read Sections 2–5 before using binary-search laboratories, and Sections 8–13 before using selection laboratories. The worked bank teaches derivations; the examination rules consolidate them. Neither an algorithm's successful demonstrations nor a finite question bank establishes correctness on every unseen examination question. The proofs apply to their stated contracts, and the audit distinguishes proof from finite testing.

Prerequisites are loop invariants, induction, elementary summation, logarithms, conditional expectation and comparison-based sorting. This chapter re-explains each tool at its point of use. Tree search, hashing, string matching and full priority-queue implementation belong to their own chapters; here they appear only when needed to compare search or top-k strategies.

## Order, rank, duplicates and the output contract

A **key** determines order; a **record** also has an identity or payload. Two records can have equal keys without being the same record. Assume a consistent total order on keys. A comparator must be transitive and must treat equivalence consistently. IEEE NaN, changing keys, and inconsistent comparators break these assumptions unless a deliberate total-order policy is supplied.

Let the sorted keys, including repeated occurrences, be $x_{(1)}\le\cdots\le x_{(n)}$. The one-based $k$th order statistic is $x_{(k)}$, for $1\le k\le n$. Its zero-based sorted-array index is $k-1$. A value $v$ is a correct answer exactly when

$$|\{x:x<v\}|<k\le|\{x:x\le v\}|.$$

To prove this certificate, put all strictly smaller occurrences first, then all occurrences equal to $v$. Their occupied rank interval is from $|L|+1$ through $|L|+|E|$. This proof permits equal keys; the distinct-key shortcut “exactly $k-1$ smaller elements” does not. For $[8,3,3,9,3,1]$, value 3 occupies ranks 2, 3 and 4. A stable choice of a specific record among those three requires an additional identity tie-breaker; key selection alone promises no stability.

For even length, “median” needs a definition. The lower median has rank $\lfloor(n+1)/2\rfloor$ and the upper median has rank $\lceil(n+1)/2\rceil$. A numerical statistical median averages the two middle values. It may not be an input key and is meaningless for keys supporting only order, such as filenames. For $[2,5,8,40]$, these outputs are 5, 8 and 6.5. Always state the contract before deriving a recurrence or choosing an option.

Selection returns a value or a record; **partition selection** additionally arranges a selected index so that all earlier keys are no larger and all later keys are no smaller. The earlier and later regions need not be internally sorted. Full sorting solves all rank queries at once and is a stronger output requirement.

<!-- SIM:rank -->

## Linear searching and the information supplied by a test

Unsorted membership search inspects occurrences until it finds the target or exhausts the input. If exactly one matching occurrence is uniformly located among $n$ positions, the expected number of equality tests is $(n+1)/2$. An unsuccessful query costs $n$. If success has probability $p$, and its conditional position is uniform, the expected cost is

$$p\frac{n+1}{2}+(1-p)n.$$

For arbitrary conditional position probabilities $p_i$, the successful expected cost is $\sum_{i=1}^n i p_i$. If successful key frequencies are known, ordering records by decreasing frequency minimizes this cost: swapping adjacent probabilities $p_i<p_{i+1}$ changes their contribution by $p_i-p_{i+1}<0$. This is an exchange argument, not an assumption that the original data are uniformly random. Unsuccessful probability adds the same $n$ term for every order.

An equality-only failure eliminates one candidate. An ordered comparison can eliminate a whole interval. This difference explains why a password lock that says only “wrong” cannot generally be searched by numerical bisection even if candidate passwords can be sorted. Sorting candidate names does not create comparison feedback from the lock.

A sentinel appends the target so that an inner loop need not check the end condition each time. It does not reduce the worst-case number of inspected keys asymptotically. It also requires writable extra space or saving and restoring an overwritten position, and a final check distinguishing a real occurrence from the sentinel.

The unsorted minimum needs $n-1$ comparisons: every nonminimum must lose a comparison establishing a smaller key. A scan achieves that bound. Likewise, an adversary can keep an unseen occurrence as a possible target or minimum, so general unsorted search/selection has a linear worst-case information requirement. This is a model-specific lower bound; a supplied index or bounded integer universe changes the available operations.

<!-- SIM:linear -->

## Binary search through a half-open boundary invariant

Sorted random-access arrays allow cheap elimination. We teach **lower bound** first because it handles membership, duplicates and insertion positions with one invariant. Define $\operatorname{lb}(x)$ as the first index with $A[i]\ge x$, or $n$ if none exists.

Maintain integer bounds $0\le lo\le hi\le n$ with all indices below $lo$ known to satisfy $A[i]<x$ and all indices at or above $hi$ known to satisfy $A[i]\ge x$. The unknown region is $[lo,hi)$; the possible boundary lies in the inclusive index interval $[lo,hi]$. These two intervals are different objects.

```python
def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

Initialization makes both known regions empty. If $A[mid]<x$, sortedness proves that every index at or below $mid$ is too small, so moving $lo$ to $mid+1$ preserves the invariant. Otherwise every index at or above $mid$ is large enough, so $hi=mid$ is valid. The integer measure $hi-lo$ decreases strictly. At termination $lo=hi$; every earlier key is too small and every key from that position onward is large enough, which is exactly the lower-bound contract.

For $[1,3,3,3,7,9,12,18]$ and target 3, the tested indices are 4, 2, 1 and 0; the returned index is 1. A membership routine must then test `i < len(a) and a[i] == x`. Accessing `a[n]` after a failed search is a separate boundary error, even if the search loop is correct.

For this loop, count **one key predicate** per iteration; do not silently count an equality check afterward as part of the same counter. Its exact worst-case predicate count for $n\ge1$ is $\lfloor\log_2 n\rfloor+1=\lceil\log_2(n+1)\rceil$. The largest remaining length after an iteration is $\lfloor n/2\rfloor$, so $W(n)=1+W(\lfloor n/2\rfloor)$ with $W(0)=0$. Targets before the minimum attain that chain. An ordinary membership routine that exits on equality has different best-case and exact path counts.

Computing `(lo+hi)//2` may overflow a fixed-width signed integer even when both bounds fit. `lo+(hi-lo)//2` avoids that sum for nonnegative valid bounds. Python integers do not overflow this way, but the invariant is still useful when translating to C++ or Java.

<!-- SIM:binary -->

## Upper bounds, equal ranges and searching by answer

The upper bound is the first index with $A[i]>x$. Replace `< x` by `<= x` in the loop. The equal-occurrence interval is $[\operatorname{lb}(x),\operatorname{ub}(x))$, and its length is the frequency of $x$. The strict predecessor index is $\operatorname{lb}(x)-1$; the strict successor index is $\operatorname{ub}(x)$. Check the corresponding range before accessing either one. A closed numeric range $[u,v]$ contains $\operatorname{ub}(v)-\operatorname{lb}(u)$ occurrences when $u\le v$.

Binary search actually needs a monotone Boolean predicate, not necessarily a stored array. For integer candidates $[0,N)$ with false values followed by true values, find the first true candidate by using `if predicate(mid): hi=mid; else: lo=mid+1`. Returning $N$ denotes “no true candidate.” Invariant: every discarded lower candidate is false, every discarded upper candidate is true. A predicate that returns true, false, true cannot support this elimination proof.

For example, a shipping capacity $C$ is feasible if a greedy left-to-right packing of nonnegative item weights uses at most $D$ days, with order preserved. Increasing capacity cannot increase the required days: every packing possible at $C$ is still possible at a larger capacity. Hence the minimum feasible integer capacity can be searched between the maximum weight and the total weight. Each feasibility test costs $\Theta(n)$; the full cost is $O(n\log(U-L+1))$, not merely logarithmic. The greedy test minimizes days because it puts the longest feasible prefix into each day; an exchange of a shorter first-day prefix cannot let a later day start farther right.

If a first true index $t$ exists but no upper bound is known, test 1, 2, 4, 8, and so on until a true candidate appears; then bisect the bracket. This costs $O(\log(t+1))$ tests, including the doubling phase. Check index zero separately. If no true candidate exists, unrestricted doubling need not terminate; a finite cap, termination assumption or timeout belongs to the contract.

Real bisection maintains an interval bracketing a monotone crossing. After $s$ exact halves its width is $(b-a)/2^s$, so at most $\lceil\log_2((b-a)/\varepsilon)\rceil$ halvings reach width $\varepsilon$. Floating-point stagnation can produce `mid == lo` or `mid == hi`; detect it. A small interval alone is not a bound on residual function error without assumptions on the function.

<!-- SIM:boundary -->

## Search variants, representation costs and lower bounds

**Exponential search** is the unknown-bound method just described applied to a sorted sequence. **Jump search** probes block ends separated by $b$ positions, then scans inside the first possible block. Its worst-case key probes are bounded by $\lceil n/b\rceil+b$ up to endpoint details. Treating $b$ as a positive real gives a minimum near $\sqrt n$, then nearby integers are checked. This tradeoff assumes direct access to block ends; counting only comparisons conceals pointer traversal in a linked list.

**Interpolation search** estimates position from numerical key values. For sorted numeric data with $A[lo]<A[hi]$, an estimate is $lo+\lfloor(x-A[lo])(hi-lo)/(A[hi]-A[lo])\rfloor$. Clamp or reject out-of-range estimates and handle a zero denominator. Its familiar expected $O(\log\log n)$ behavior needs suitable distribution and independence assumptions. Highly skewed keys can make it advance one position per probe and cost $\Theta(n)$. Numerical arithmetic, rounding and overflow are extra requirements absent from pure comparison search.

A sorted singly linked list has no constant-time midpoint access. A boundary search retaining interval length and a left cursor can spend $n/2+n/4+\cdots=O(n)$ pointer steps despite only $O(\log n)$ key comparisons. Repeatedly restarting each midpoint traversal from the global head can cost $\Theta(n\log n)$ pointer steps on a rightward path. State whether the requested complexity counts comparisons, traversal, or all operations.

For locating one of $n+1$ insertion gaps through Boolean ordered tests, a decision tree needs at least $\lceil\log_2(n+1)\rceil$ tests in its worst case: a depth-$d$ binary tree has at most $2^d$ leaves. This exact gap bound does not automatically apply to a primitive three-outcome comparison with equality, or to equality-only guessing. A lower bound must match the allowed observation and output contract.

For a distinct sorted array rotated at an unknown position, at least one half of an interval is sorted. Test whether the target lies in that half's key interval; keep it if so, otherwise keep the other half. Duplicate keys can make both ends and the midpoint equal, hiding the rotation and forcing a linear worst case. In a strictly bitonic array, comparing adjacent middle keys locates the peak, then binary-searching the increasing and decreasing sides solves membership in $O(\log n)$. Plateaus need an explicit policy and may destroy a naive strict-slope proof.

## Minimum, maximum and tournament certificates

Scanning separately for minimum and maximum uses $2n-2$ comparisons. Pairing improves this. First compare the two keys in each pair; only the smaller can update the minimum, and only the larger can update the maximum. For even $n$, initialize from the first pair (one comparison), then use three comparisons per remaining pair. For odd $n$, initialize both extrema from one unpaired key and use three per pair. For $n\ge2$, the exact count is

$$\left\lceil\frac{3n}{2}\right\rceil-2.$$

An adversary explains optimality on distinct-key inputs. Label a key fresh until its first comparison, then classify its remaining eligibility as maximum-only, minimum-only, or neither. When two fresh keys meet, the larger loses minimum eligibility and the smaller loses maximum eligibility, eliminating two candidacies. There can be at most $\lfloor n/2\rfloor$ such comparisons because each consumes two fresh keys. In every other comparison the adversary can eliminate at most one new candidacy: a fresh key loses to a maximum-only key, beats a minimum-only key, or is placed above/below an ineligible key so that it retains one eligibility; two maximum-only keys eliminate one maximum candidate; two minimum-only keys eliminate one minimum candidate; a maximum-only key beats a minimum-only key without a new elimination. Ineligible keys are placed consistently between the surviving minimum and maximum classes. These outcomes can be extended to distinct numeric values satisfying all comparison results.

At termination, only the actual minimum and maximum retain their respective eligibility, so $2n-2$ candidacies must have been removed. If $C$ comparisons occurred, they remove at most $C+\lfloor n/2\rfloor$ candidacies. Thus $C\ge2n-2-\lfloor n/2\rfloor=\lceil3n/2\rceil-2$, matching the paired algorithm. This counts key comparisons, not loop conditions.

To find the largest and second largest **distinct-ranked records**, organize a knockout tournament. Every loser has a witness larger than it. Only keys that lost directly to the champion can be second largest: a key losing elsewhere also has its defeater below the champion, so cannot be runner-up. The tournament uses $n-1$ comparisons, then finding the largest direct loser uses $d-1$, where $d$ is the number of matches played by the champion. A balanced bracket with byes gives $d\le\lceil\log_2 n\rceil$, hence at most $n+\lceil\log_2 n\rceil-2$. For a power of two the champion plays exactly $\log_2 n$ matches. This is a worst-case bound; a champion with a bye can require fewer comparisons. Equal keys demand a distinction between the second occurrence and the second **distinct value**.

<!-- SIM:extrema -->

## Three-way partitioning: a constructive correctness proof

Save a pivot **value** before exchanges. Maintain four regions in $[lo,hi)$: keys less than the pivot in $[lo,lt)$; equal keys in $[lt,i)$; unknown keys in $[i,gt)$; and greater keys in $[gt,hi)$. Initially `lt=i=lo` and `gt=hi`.

```python
def partition3(a, lo, hi, pivot):
    lt = i = lo
    gt = hi
    while i < gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            gt -= 1
            a[i], a[gt] = a[gt], a[i]
        else:
            i += 1
    return lt, gt
```

In the less case, the element previously at `lt` belongs to the equal region when `lt<i`; exchanging it with the unknown smaller key and incrementing both cursors preserves all three classified regions. If `lt==i`, the exchange is harmless. In the greater case, decreasing `gt` exposes a previously unknown key at that position. The exchange classifies the greater key on the right, but the replacement at `i` is still unknown. Therefore `i` must not increment. In the equal case, increasing `i` extends the equal region. Each branch decreases `gt-i` by exactly one, so there are exactly $hi-lo$ classification iterations.

An iteration may execute two Boolean key comparisons (`<`, then `>`) rather than one abstract three-way comparator. Report the intended convention. A pivot copied from the range guarantees a nonempty equal block at completion. A pivot outside the input can give an empty equal block, so selection must not assume that such a value was found in the array.

<!-- SIM:partition -->

## Quickselect: keep one region and translate the rank

For a local one-based rank $k$, let $l=|L|$ and $e=|E|$ after partitioning. If $k\le l$, continue in $L$ with the same rank. If $l<k\le l+e$, return the pivot value. Otherwise continue in $G$ with rank $k-l-e$. The equal block, rather than one arbitrarily removed pivot record, determines the translation for repeated keys.

```python
def select_value(a, k, choose_pivot):
    if not 1 <= k <= len(a):
        raise ValueError("rank must be in 1..n")
    lo, hi = 0, len(a)
    target = k - 1                 # fixed global array index
    while True:
        pivot = choose_pivot(a, lo, hi)
        lt, gt = partition3(a, lo, hi, pivot)
        if target < lt:
            hi = lt
        elif target >= gt:
            lo = gt
        else:
            return pivot
```

The implementation keeps a fixed global target index; the mathematical recursive explanation uses a local rank. They are equivalent because each rightward move accounts for the discarded lower positions in `lo`. Do not subtract discarded counts from `target` while also keeping global array indices.

Correctness follows by strong induction on the active length. Partitioning establishes the rank interval of the equal block. If the target lies outside it, exactly one strict region can contain the desired value, and the proper rank translation preserves the specification. Because the equal block contains at least the chosen pivot occurrence, any continuation is smaller. If all keys are equal, one partition finishes all possible rank queries on that input.

Correctness does not imply a good split. For distinct keys, always choosing the smallest pivot when seeking the maximum makes active lengths $n,n-1,\ldots,1$. With one pivot comparison against every other key, the total is $n(n-1)/2$. Selecting the median on the same pivot policy still visits linearly many nearly full suffixes and has quadratic cost. Sorting recurses on both strict regions; selection follows only the region containing the rank.

<!-- SIM:select -->

## Randomized selection: expectation without circular reasoning

Choose a uniformly random **occurrence** from the current range independently conditional on the previous history. For distinct keys, its sorted rank is uniform. For duplicates, assign an arbitrary fixed identity order inside each equal-key class solely for analysis. An occurrence in the central rank region has a pivot value whose strict sides are no larger than the bounds obtained from its identity rank; equal occurrences are removed together, which can only help.

For every active length $m\ge8$, at least half the identity ranks lie between $\lceil m/4\rceil$ and $\lfloor3m/4\rfloor+1$. Any such pivot leaves either strict side with length at most $3m/4+1\le7m/8$. Thus a “good” pivot has conditional probability at least $1/2$ and shrinks the range by at least a fixed factor. The conservative $7/8$ factor keeps rounding explicit; it is not a tight comparison constant.

In a phase starting with at most $M$ elements, wait until the active size is at most $7M/8$ or below eight. While the phase persists, a good pivot of the current active set finishes the phase, because its next size is at most $7M/8$. If $N$ is its number of partitions, conditional success probability at least $1/2$ implies $\Pr(N>t)\le2^{-t}$ and $E[N]\le2$. Each partition in that phase costs at most $cM$, so expected phase cost is at most $2cM$. Summing phase sizes gives

$$E[T(n)]\le2cn\sum_{j\ge0}(7/8)^j+O(1)=16cn+O(1).$$

The first incomplete phase and the finite base range can be absorbed into a fixed constant. This proves expected $O(n)$ work for every fixed input; a general linear lower bound gives $\Theta(n)$ for worst-input expected cost. The bound is conservative and does not equal the exact number of comparisons in a trace. It averages over the algorithm's random choices, not over a supposedly random input. A particular unlucky sequence can still cost $\Theta(n^2)$.

It is invalid to replace $E[T(X)]$ by $T(E[X])$ before proving linearity. For $X$ equally likely to be 1 or 3 and $T(x)=x^2$, these values are 5 and 4. Using a property one is trying to prove is circular. The phase proof bounds actual conditional work without that substitution.

For distinct keys and an abstract partition cost of exactly $n-1$ pivot comparisons, exact expected counts can instead be computed by conditioning on pivot rank:

$$C(n,k)=n-1+\frac1n\left(\sum_{r=1}^{k-1}C(n-r,k-r)+\sum_{r=k+1}^{n}C(r-1,k)\right).$$

Set $C(1,1)=0$. If $r<k$, continue on the right; if $r>k$, continue on the left; if $r=k$, no child is visited. This recurrence supports small exact exam calculations. Its counter is different from the Boolean-comparison count in our three-way implementation.

<!-- SIM:random -->

## Deterministic median-of-medians selection

The goal is a pivot guaranteed to discard a constant fraction without first sorting the entire input. Divide the input into groups of at most five, sort each constant-size group, and take its lower median. Let $g=\lceil n/5\rceil$ and let $M$ contain those $g$ medians. Recursively select the lower median of $M$, using rank $\lfloor(g+1)/2\rfloor$. Then partition the original input three ways and recursively select only the necessary strict side.

```python
def deterministic_select(a, k):
    if not 1 <= k <= len(a):
        raise ValueError("rank must be in 1..n")
    if len(a) <= 140:
        return sorted(a)[k - 1]  # fixed-size base, asymptotically constant
    groups = [sorted(a[i:i+5]) for i in range(0, len(a), 5)]
    medians = [g[(len(g)-1)//2] for g in groups]
    p = deterministic_select(medians, (len(medians)+1)//2)
    less = [x for x in a if x < p]
    equal = [x for x in a if x == p]
    greater = [x for x in a if x > p]
    if k <= len(less):
        return deterministic_select(less, k)
    if k <= len(less) + len(equal):
        return p
    return deterministic_select(greater, k-len(less)-len(equal))
```

This readable version allocates lists. Linear time is not a claim of constant auxiliary space: the live input/group/partition arrays can occupy $O(n)$ total additional space and recursion depth is $O(\log n)$. An in-place implementation needs explicit group storage and partition management. A small lab may use a lower base threshold for demonstration; that is a different executable trace, not the finite proof's implementation.

### Why the pivot discards enough elements

At least $\lfloor g/2\rfloor$ medians are no smaller than the lower median $p$, and at least that many are no larger. Every qualifying **full** five-element group certifies three keys on its corresponding weak side of $p$. To get one convenient symmetric bound, discard a possible partial group and the pivot-containing group. Each weak side still has at least

$$3(\lceil n/10\rceil-2)$$

certified occurrences, with a negative small-$n$ expression interpreted as the trivial bound zero. For distinct keys the retained groups certify strict sides. For duplicates, weak-side certificates suffice: the strict greater side excludes every occurrence certified $\le p$, and the strict less side excludes every occurrence certified $\ge p$. Therefore either selected strict child has size at most $7n/10+6$. Do not count three disjoint groups merely because three medians have been compared: each certificate comes from a separate original group.

For an ideal complete-group illustration, medians of $[1,2,3,10,11]$, $[4,5,6,12,13]$, and $[7,8,9,14,15]$ are 3, 6 and 9, so $p=6$. The global median is 8. The approximate pivot is useful even though it is not the exact median. In the model, the separate representative row is a copied list of median keys; the original records remain in their columns. Purple identifies the chosen pivot value, while green and blue identify actual smaller and greater occurrences after pivot selection.

<!-- SIM:groups -->

### The recurrence, including the work of choosing the pivot

There are two recursive computations: selection in the median array and selection in at most one strict partition. Sorting fixed-size groups and partitioning cost at most $an$ for a constant $a$. Thus

$$T(n)\le T(\lceil n/5\rceil)+T(\lfloor7n/10+6\rfloor)+an.$$

The ordinary equal-size Master theorem does not apply to two unequal child sizes. For $n>140$, their summed upper bound is at most $0.9n+7\le0.95n$. Choose $c\ge20a$ and large enough that $T(t)\le ct$ for every integer $1\le t\le140$. Strong induction gives $T(n)\le c(0.9n+7)+an\le cn$. The finite base is what justifies the ceiling and additive constant. Dropping them in a formal proof without a threshold leaves a gap.

The familiar ideal recurrence has child fractions summing to $1/5+7/10=9/10$. Its level costs form $an(1+0.9+0.9^2+\cdots)$. This is useful intuition, but the finite induction is the precise argument. Selection has a comparison-model $\Omega(n)$ worst-case lower bound, so the deterministic algorithm is asymptotically optimal for a single rank. That statement concerns order of growth; it does not claim the smallest possible exact constant.

## General group sizes and recurrence traps

Let an odd fixed group size be $b=2t+1$. A full group contributes $t+1$ certified keys when its median lies on the corresponding weak side. Ignoring only additive boundary terms, the discard fraction is $(b+1)/(4b)$ and the selected child fraction is $(3b-1)/(4b)$. The ideal recurrence is

$$T(n)\le T(n/b)+T(((3b-1)/(4b))n)+O(n).$$

The sum of fractions is $3(b+1)/(4b)$. It is below one exactly when $b>3$. Hence every fixed odd $b\ge5$ gives the same linear asymptotic upper bound, with different constants. For groups of seven, the second fraction is $5/7$ and the sum is $6/7$; with ideal toll exactly $n$, linear substitution needs $c\ge7$. For groups of five it needs $c\ge10$. Real implementations also have group-sorting cost and finite boundary effects.

Groups of three give the **bound** $T(n)\le T(n/3)+T(2n/3)+O(n)$, which yields an $O(n\log n)$ upper bound. The equality recurrence with a positive linear toll is $\Theta(n\log n)$. This does not by itself prove that every implementation of the selection algorithm attains both worst child sizes recursively on a single adversarial input. Distinguish analysis of a recurrence from a matching algorithmic lower bound.

A repeated grouping technique illustrates how the same group size can lead to a different guarantee. Take medians of triples, then medians of triples of those medians. The second-level representative certifies four original occurrences on either side. Select the median among about $n/9$ representatives; approximately half contribute, so roughly $2n/9$ originals are certified on either side. The resulting ideal bound is $T(n/9)+T(7n/9)+O(n)$, with fraction sum $8/9<1$. It is linear after boundary constants are handled. “Groups of three cannot support linear selection” is therefore an overstatement about one particular construction.

## Selection from two sorted arrays

Let arrays $A$ and $B$ have lengths $m$ and $n$, with $m\le n$. To obtain one-based rank $k$ in their multiset union, put exactly $k$ elements on the combined left side. Choose $i$ from $A$ and $j=k-i$ from $B$, with

$$\max(0,k-n)\le i\le\min(k,m).$$

Define the left and right boundary keys using conceptual sentinels $-\infty$ and $+\infty$ for empty sides. A valid cut satisfies $A_L\le B_R$ and $B_L\le A_R$. Both arrays are internally sorted, so these cross inequalities imply that every combined left key is no larger than every combined right key. The desired value is $\max(A_L,B_L)$.

If $A_L>B_R$, too many large $A$ keys are on the left; decrease $i$. If $B_L>A_R$, too few $A$ keys are on the left; increase $i$. As $i$ increases, $A_L$ cannot decrease while $B_R$ cannot increase, establishing the elimination direction. Equal keys are allowed by the weak inequalities. Empty arrays work if the rank is valid; both empty arrays have no valid rank.

```python
def kth_two_sorted(a, b, k):
    if len(a) > len(b):
        return kth_two_sorted(b, a, k)
    if not 1 <= k <= len(a) + len(b):
        raise ValueError("rank outside union")
    lo, hi = max(0, k-len(b)), min(k, len(a))
    while lo <= hi:
        i = (lo + hi) // 2
        j = k - i
        al = a[i-1] if i else float('-inf')
        ar = a[i] if i < len(a) else float('inf')
        bl = b[j-1] if j else float('-inf')
        br = b[j] if j < len(b) else float('inf')
        if al > br:
            hi = i - 1
        elif bl > ar:
            lo = i + 1
        else:
            return max(al, bl)
```

This numeric code uses infinities; for general comparable records, represent missing boundaries symbolically rather than mixing incomparable sentinel objects with records. Its cost is $O(\log(m+1))$ boundary iterations with constant-time access. If both arrays have equal length $n$, the lower median is the union's rank $n$. A comparison decision tree has at least $2n$ possible output locations realizable in suitable interleavings, so it needs $\Omega(\log n)$ comparisons; this gives a tight asymptotic bound, not an exact optimal constant for the displayed implementation.

For an even-length numerical median, select ranks $(m+n)/2$ and $(m+n)/2+1$ or use both boundary values at one median cut. Do not average the two input medians: relative interleaving, not only the two middle keys, determines the union's median.

<!-- SIM:two -->

## Top-k, rank intervals and multiple quantiles

To output the smallest $k$ occurrences without sorting them, select the $k$th value $v$, retain every key smaller than $v$, and add enough equal occurrences to reach exactly $k$. This takes $O(n+k)$ output-inclusive time. Taking all keys $\le v$ may output too many if the threshold is repeated. If the output must be sorted, sort just those $k$ selected records, for total $O(n+k\log k)$ with deterministic selection.

For streaming top-k largest values, retain a min-heap of at most $k$ records. Its root is the weakest retained record. A new record replaces the root only when it is better under the requested tie policy. The total is $O(n\log(k+1))$ time and $O(k)$ memory; sorting the final retained records adds $O(k\log k)$. This supports one pass and small space but is not the same cost as offline linear selection.

For a rank interval $[i,j]$, select its boundary values and output all strictly interior keys plus the appropriate boundary occurrences. With distinct keys, selecting rank $i$, filtering the greater side, then selecting the desired endpoint in that side is enough. With duplicates, use occurrence counts or a consistent identity tie-breaker so exactly $j-i+1$ records are output. Unsorted interval output costs $O(n+j-i+1)$; sorted interval output adds the interval's sorting cost.

For $q$ requested ranks, choose the middle requested rank, select it in linear time, then recurse only in the relevant left and right ranges. In one level, active ranges are disjoint, so their total size is at most $n$. The tree over requested ranks has $O(\log(q+1))$ levels, yielding $O(n\log(q+1))$ time. A shared equal block answers all requested ranks it covers. Asking for all distinct input ranks recovers sorted order and the comparison sorting lower bound $\Omega(n\log n)$. A single rank does not have $n!$ distinguishable output permutations.

## Weighted medians and absolute-error minimization

Each key $x_i$ may have a nonnegative weight $w_i$, with positive total weight $W$. A weighted median has total weight strictly below it at most $W/2$ and strictly above it at most $W/2$. Equal-key occurrences must have their weights aggregated when testing a threshold. The lower weighted median is the first sorted key whose cumulative weight reaches $W/2$. For an exact-half gap, multiple real minimizers exist, and this convention chooses its lower endpoint.

Consider $F(y)=\sum_i w_i|y-x_i|$. Between adjacent distinct keys, increasing $y$ by a small $\delta$ changes $F$ by $\delta(W_{left}-W_{right})$. To the left of a weighted median this slope is nonpositive; to its right it is nonnegative. At a key, the subgradient spans the contribution of its equality mass, so zero belongs to that interval exactly when both strict-side masses are at most half the total. Thus weighted medians minimize weighted absolute deviation. If exactly half the weight is on each side of a gap, the slope in the gap is zero and every point there minimizes $F$. The mean instead minimizes squared error, so substituting it changes the objective.

Linear weighted selection can use a cardinality-balanced deterministic pivot while computing weight sums during partition. Maintain a fixed threshold $W/2$ and the discarded-lower mass, or equivalently a local remaining threshold. If the threshold lies inside the pivot's cumulative mass interval, return it; otherwise keep one strict region and update the mass offset. The pivot need not bisect **weight**: balancing record count still bounds the running time because only one count-balanced region survives. Using the unweighted median directly as the final weighted answer is incorrect.

```python
def lower_weighted_median(records):  # pairs (key, nonnegative weight)
    if not records or any(w < 0 for _, w in records):
        raise ValueError("nonempty data and nonnegative weights required")
    threshold2 = sum(w for _, w in records)  # twice the desired local mass
    if threshold2 <= 0:
        raise ValueError("total weight must be positive")
    active = list(records)
    while True:
        keys = [x for x, _ in active]
        p = deterministic_select(keys, (len(keys)+1)//2)
        lower = [(x, w) for x, w in active if x < p]
        equal = [(x, w) for x, w in active if x == p]
        higher = [(x, w) for x, w in active if x > p]
        wl = sum(w for _, w in lower)
        we = sum(w for _, w in equal)
        if threshold2 <= 2 * wl:
            active = lower
        elif threshold2 <= 2 * (wl + we):
            return p
        else:
            threshold2 -= 2 * (wl + we)
            active = higher
```

This version computes a true lower count median as pivot using the preceding worst-case linear selector. Each retained strict side has at most half the active occurrences, so the selector calls and partition scans form a geometric linear sum. The local threshold is kept in doubled-mass units, avoiding division and remaining exact for arbitrary-size Python integer weights. The equality case `threshold2 == 2*wl` continues left, preserving the lower weighted-median convention at an exact-half gap. Zero-weight records do not count toward the mass threshold. Exact rational weights also work with exact arithmetic; approximate floating-point weights require a deliberate policy near half-mass ties.

<!-- SIM:weighted -->

## Implementation obligations and adversarial cases

The mathematical specification is the interface. State whether inputs are mutated, whether returned output is sorted, whether ties are stable, and whether comparisons or total RAM work are counted. Never use a stale pointer to a pivot record that moves during exchanges; save the pivot key or maintain its identity deliberately. Iterative quickselect controls its main stack use, but a recursive pivot chooser still requires its own recursion analysis.

A logarithmic-depth stopping rule followed by sorting a large residual range does not by itself prove worst-case linear selection. The preceding unbalanced scans can already cost $\Theta(n\log n)$. A true worst-case linear hybrid needs a bounded **cumulative work budget** of $Bn$ before switching to a proven linear fallback. Then prefix cost is at most $Bn$ and fallback cost is $O(n)$. Particular library implementations require inspection of their actual contracts; the word “introselect” alone does not identify a proof.

For bounded integer keys in $[0,U)$, a histogram and cumulative count can answer a single rank in $O(n+U)$ time and $O(U)$ memory. This is not a contradiction of comparison lower bounds; direct addressing is an extra permitted operation. If $U$ is huge or negative keys need shifting, the model and resource bounds change. A histogram loses original identities unless separate buckets or payload references are stored.

For sorted range sums, precompute $P[0]=0$ and $P[i+1]=P[i]+w_i$. A closed key interval query finds $l=\operatorname{lb}(u)$ and $r=\operatorname{ub}(v)$, then returns $P[r]-P[l]$. The prefix construction costs $O(n)$ after sorting; each query costs $O(\log n)$ plus constant arithmetic. Sorting anew before each query defeats this reuse.

## Complete summary and method choice

Start with the output contract and the feedback model. Equality-only unsorted search has linear worst-case work. Sorted random-access boundary search has logarithmic key probes and precise insertion-gap semantics. Selection needs one order statistic, whereas sorting establishes every rank. A three-way partition handles ties through a complete equal interval, and only one strict region survives a single-rank query.

Random pivots give expected linear selection for any fixed input under the stated conditional-uniform choice; a unlucky run can be quadratic. Median-of-medians gives deterministic worst-case linear time by spending linear work to certify a sufficiently central pivot. Its recursive pivot selection must be included in the recurrence. Two already sorted arrays permit logarithmic rank selection because a feasible cut can be searched without scanning all records.

Use offline selection for one rank or an unsorted top-k output. Use selection followed by sorting only the retained records for sorted top-k. Use a bounded heap for streaming top-k when memory and a single pass matter. Use multiselection for several known ranks, and full sorting when essentially every ordered output is needed. For weighted absolute deviation, use cumulative **weight**, not occurrence rank, to identify the answer.

| Task and assumptions | Suitable method | Time guarantee | Important output detail |
|---|---|---|---|
| Unsorted equality-only lookup | Linear scan | Worst-case $\Theta(n)$ | A failure requires exhaustion |
| Sorted random-access insertion boundary | Lower/upper bound | Worst-case $\Theta(\log(n+1))$ | Return $n$ if no qualifying key exists |
| One unsorted order statistic | Randomized three-way quickselect | Expected $\Theta(n)$, worst-case $\Theta(n^2)$ | Side regions need not be sorted |
| One rank with deterministic bound | Median of medians | Worst-case $\Theta(n)$ | Pivot is only approximately central |
| Rank in two sorted arrays | Cross-boundary cut search | $O(\log(\min(m,n)+1))$ | Weak cross inequalities permit ties |
| Offline sorted smallest $k$ | Select, extract, then sort | $O(n+k\log k)$ | Take only enough equal thresholds |
| Streaming largest $k$ | Bounded min-heap | $O(n\log(k+1))$ | Explicit tie policy and $O(k)$ space |
| Weighted absolute-error optimum | Weighted median | Worst-case $O(n)$ with count-balanced pivots | Equal values aggregate mass |

## Worked mathematical, conceptual and examination problems

The authentic items preserve their original options and independently derived answers. Two are explicit revisits comparing sorting with selection, and one is a searching-information bridge. The remaining problems are original or independently reconstructed course tasks. Their stated comparison conventions are part of each question, and every solution explains the elimination or counting argument rather than just naming a complexity class.

<!-- INCLUDE:problems -->

## Examination rules and diagnostic traps

<!-- INCLUDE:review -->

## Editable exact-state laboratories

Each laboratory computes its trace from the submitted data. The animation follows the mathematical model of that algorithm: boundary elimination, moving record identities across three-way regions, grouped-median certificates, feasible cross-array cuts, or cumulative weight. Indices stay attached to positions while records can move. Step backward, seek, pause and restart allow inspection of every decision; reduced-motion mode preserves all states without animated travel. Invalid data leave the last valid trace intact.

<!-- LAB:selection -->

## References and chapter boundary

1. **MIT.** Erik Demaine, Srini Devadas, Nancy Lynch. *6.046J Design and Analysis of Algorithms*, Spring 2015, Lecture 2, PDF pp. 4–5. [Written lecture notes](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/7463c413c944ed72b46a3c3d02b49448_MIT6_046JS15_lec02.pdf).
2. **Stanford University.** Moses Charikar and Nima Anari. *CS161 Design and Analysis of Algorithms*, Winter 2023, Lecture 4, PDF pp. 1–9, notes adapted from Virginia Vassilevska Williams and Mary Wootters. [Lecture notes](https://stanford-cs161.github.io/winter2023/assets/files/lecture4-notes.pdf). [Selection concept checks](https://stanford-cs161.github.io/winter2023-bank/select.pdf).
3. **Carnegie Mellon University.** *15-451 Algorithm Design and Analysis*, Fall 2024, Lecture 1, *Introduction and Linear-time Selection*, PDF pp. 7–14. [Written lecture](https://www.cs.cmu.edu/~15451-f24/lectures/lecture01-selection.pdf). Fall 2005, Homework 2, problem 1. [Two sorted arrays assignment](https://www.cs.cmu.edu/afs/cs/academic/class/15451-f05/www/assignments/hwk2.pdf).
4. **Princeton University.** Robert Sedgewick and Kevin Wayne. *COS226 Algorithms and Data Structures*, Spring 2025, Quicksort lecture slides, PDF pp. 28–31 and 34–39. [Written slides](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/23Quicksort.pdf). *Introduction to Programming*, §4.2, searching exposition and exercises. [Written searching chapter](https://introcs.cs.princeton.edu/java/42sort/).
5. **University of California, Berkeley.** CS170 assigned text: Sanjoy Dasgupta, Christos Papadimitriou and Umesh Vazirani, *Algorithms*, Chapter 2, §2.4, printed pp. 64–66 / PDF pp. 10–12. [Written textbook chapter](https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf).
6. **Original examination archive.** Iranian MSc Computer Science 1405 Q116; PhD Computer Engineering 1405 Q9; MSc Computer Engineering 1405 Q59. PDF paths, page numbers and immutable archive commit are attached to each authentic item. [Project examination archive](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams).

The chapter covers array searching and comparison-based order statistics, including repeated keys, weighted extensions and two sorted inputs. It does not claim an exhaustive survey of every specialized selection algorithm, every library implementation, or every historical examination. Formal proofs, source scope, independent finite checks and visual evidence are reported in the [quality audit](../reviews/a_select-quality.html). The chapter remains a review draft until explicit student approval.
