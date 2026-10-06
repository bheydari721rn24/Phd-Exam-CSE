# Examination rules: conditions, formulas, and failure modes

1. State the object being sorted before choosing a theorem. A record contains a key and a payload; ordering its key does not authorize losing, duplicating, or reconstructing its payload. Sortedness and multiset preservation are separate obligations.

2. Stability concerns the order of distinct records with equal keys. The output keys alone cannot establish it. Label equal occurrences by original positions and compare their output positions.

3. A comparator must define a consistent order. With a strict comparator, irreflexivity and transitivity are essential, and the induced equivalence must be transitive. A cyclic comparator can invalidate partition and merge proofs even when every individual comparison terminates.

4. Do not assume that a tie-breaking rule makes an unstable implementation stable. Decorating each key with its original index makes all composite keys distinct and forces the desired order, but requires index storage and a comparator that actually reads the index.

5. For secondary and primary keys, a stable secondary-key sort followed by a stable primary-key sort gives lexicographic order. Reversing the pass order reverses the priority. This same principle underlies LSD radix sorting.

6. Distinguish a key comparison from a loop-bound test, an assignment, a swap, and a comparator call. One ternary comparator call can correspond to two Boolean key tests. Exact operation questions require the code and the counting convention.

7. A strict inversion is a pair $i<j$ with $A_i>A_j$. Equal keys contribute no strict inversion. A swap of an inverted adjacent pair removes exactly one inversion; an arbitrary long-distance swap need not do so.

8. For the stated selection sort, the comparison count is exactly $n(n-1)/2$ on every input. This is an exact count, whereas $\Theta(n^2)$ conceals constants and lower-order terms.

9. Selection sort has at most $n-1$ nontrivial swaps, but its comparisons remain quadratic. When record writes dominate comparisons, this tradeoff can matter. Do not infer a linear running time from a linear swap count.

10. Ordinary selection sort is unstable: moving a distant minimum can carry an earlier equal-key record past a later one. Replacing the final swap with a block shift can preserve stability, but can require quadratic writes.

11. For a known target permutation with $c$ cycles, the minimum number of unrestricted swaps is $n-c$. The theorem assumes distinct identities and a fixed target; repeated keys may admit several valid targets.

12. In insertion sort with shifts, the number of predecessor shifts is exactly the initial inversion count $I$. Placing the saved key adds another write for each of the $n-1$ outer iterations in the stated implementation, even if its position does not change.

13. Let $r$ count positions after the first that are strict new prefix minima. With short-circuit testing of the boundary before comparing keys, insertion comparisons equal $I+(n-1)-r$. Counting a sentinel comparison instead changes this formula.

14. Insertion sort is stable when it shifts only keys strictly greater than the saved key. Shifting equal keys changes their relative order. The distinction is between $>$ and $\geq$, not between ascending and descending sorting.

15. For a uniformly random permutation of distinct keys, $\mathbb{E}[I]=n(n-1)/4$. For a multiset with multiplicities $m_j$, the expectation is $(n^2-\sum_j m_j^2)/4$. The distribution over labeled arrangements must be stated.

16. Binary insertion reduces the search comparisons but does not eliminate array shifts. Its worst-case movement remains quadratic. To preserve stability, insert after existing equal keys, using the upper-bound position.

17. A left rotation of a sorted distinct array by $k$ positions has $k(n-k)$ inversions. Its insertion cost can therefore be quadratic even though the array consists of only two increasing runs.

18. With a shrinking upper bound and an early-exit flag, bubble sort uses $n-1$ comparisons on an already sorted nonempty array. Without the flag, it still executes the triangular comparison count.

19. Bubble sort's number of strict adjacent swaps equals $I$. Its number of comparisons need not be $\Theta(n+I)$: a small key at the right end can travel left only one position per pass, producing quadratic comparisons with only $n-1$ inversions.

20. A large key at the left end can travel to the right end in one left-to-right pass. This direction asymmetry explains why two inputs with the same inversion count can have different bubble comparison counts.

21. An $h$-sort sorts each residue class modulo $h$. It need not sort the whole array when $h>1$. A final gap of one is required by ordinary Shell sort to establish total order.

22. If $n=qh+r$ with $0\leq r<h$, the maximum comparisons for separate insertion sorts of the $h$ chains are $r\binom{q+1}{2}+(h-r)\binom q2$. This is a single-gap bound, not automatically a tight total bound for a gap sequence.

23. Earlier Shell passes alter the inputs of later passes. Summing the independent worst cases of all gaps gives an upper bound, but one input may not attain every term. Never present that sum as an exact worst case without a construction.

24. Shell sort can be unstable even though each individual chain is sorted stably. Records in different residue classes can cross before they share a chain. Its running-time guarantee depends on the complete gap sequence.

25. Merging two nonempty sorted runs of lengths $p,q$ uses at most $p+q-1$ ordinary head comparisons and at least $\min(p,q)$. If one run is empty, the count is zero. Copying leftover records performs writes but no head comparisons.

26. A stable merge chooses the left run when head keys are equal. Choosing the right run reverses cross-run ties even if both input runs were individually stable. Stability must hold at every merge.

27. In a merge, a selected right key smaller than the current left head contributes the number of remaining left keys to the strict cross-inversion count. Equality contributes zero. Within-run inversions must also be counted recursively.

28. For balanced top-down mergesort with $n=2^k$, the best head-comparison count is $(n/2)\log_2n$ and the worst is $n\log_2n-n+1$. These formulas describe ordinary merging without a pre-merge boundary shortcut.

29. For arbitrary $n\geq1$, balanced mergesort's worst count is $n\lceil\log_2n\rceil-2^{\lceil\log_2n\rceil}+1$. Unequal leaf depths matter. Do not round the power-of-two formula by replacing the logarithm alone.

30. Testing whether the last left key is at most the first right key allows a merge to be skipped. On sorted input, one test per internal node gives $n-1$ comparisons. On unsorted input, these tests add overhead to the ordinary merge count.

31. A reusable auxiliary array gives linear peak auxiliary storage. Repeatedly allocating temporary arrays can still have linear peak live storage but $\Theta(n\log n)$ cumulative allocated volume. Peak space and total allocation are different metrics.

32. Bottom-up mergesort doubles the run width each pass. A final incomplete run must be bounded by the array length; it is not padded with genuine records. Its output contract includes exact preservation of all records.

33. Merging runs one at a time into an ever-growing prefix can be quadratic. A balanced merge schedule has logarithmic participation depth per record. Natural mergesort's advantage depends on both the number of initial runs and the scheduling policy.

34. Reversing a nonincreasing run can reverse equal-key identities. Stable natural merging either detects strictly decreasing runs or handles equal-key groups separately. A sorted-key picture does not reveal this defect.

35. If every record is displaced by at most $k$ positions, a min-heap of at most $k+1$ candidates supports $O(n\log(k+1))$ sorting. The displacement promise is stronger than a vague statement that the input is nearly sorted.

36. A partition routine's return value must be interpreted from its contract. Lomuto returns a final pivot index; classic Hoare returns a split boundary that need not contain the pivot. Their recursive child intervals are consequently different.

37. For the stated strict Lomuto partition on $[lo,hi)$, each nonpivot key is compared once and the pivot ends at $b$. The children are $[lo,b)$ and $[b+1,hi)$. Reincluding $b$ can prevent termination.

38. Strict Lomuto with all equal keys puts the pivot at the left edge on every call. It makes $n(n-1)/2$ comparisons. Randomizing which equal record is chosen does not repair this key-value imbalance.

39. Classic Hoare scans must stop on equality and advance after exchanges. Otherwise equal keys can cause a stalled scan. After the split $j$, recurse on the ranges specified by that implementation, not the final-pivot ranges of Lomuto.

40. CMU's middle-position pivot is a deterministic position choice, not a median-key oracle. Carefully arranged input can repeatedly make that position contain an extreme value. The lecture's partition variant must be traced with its own $\leq$ rule.

41. In randomized quicksort on distinct keys, ranks $i<j$ are directly compared exactly when one endpoint is the first pivot from ranks $i$ through $j$. Their comparison probability is $2/(j-i+1)$.

42. Summing the pair indicators gives expected comparisons $2(n+1)H_n-4n$. This is an expectation over pivot randomness for a fixed distinct-key input. It is not an exact count for one observed trace.

43. Do not substitute the mean child size into a nonlinear recurrence. The correct expectation averages the costs for all possible pivot ranks. A distribution concentrated on extreme splits can have mean balanced child size and still quadratic expected work.

44. A random shuffle makes every distinct-key permutation equally likely when implemented correctly. It gives an expected guarantee, while a worst execution can still make quadratic comparisons. Probability and worst-case statements must remain separate.

45. Choosing the median of three distinct sampled keys excludes the sampled extremes, but does not ensure a constant-fraction split of the full array. The global pivot rank can still be close to an endpoint.

46. The median of a distinct sample of $2s+1$ guarantees at least $s$ smaller and $s$ larger sampled keys. Thus both full children have at most $n-s-1$ keys. The sample-selection cost must be included in the recurrence.

47. A sample of $2\sqrt n+1$ keys sorted by insertion sort costs $\Theta(n)$ in its worst case. The most unbalanced allowed split yields $T(n)=T(n-\sqrt n)+T(\sqrt n)+\Theta(n)$ up to rounding, with order $\Theta(n^{3/2})$ under that worst-split model.

48. Recursing on the smaller quicksort child bounds stack space only if the larger child is handled by iteration or tail-call elimination. Making two ordinary recursive calls in a different order does not itself bound the maximum live recursion chain.

49. A Dutch-national-flag partition maintains less, equal, unknown, and greater regions. After swapping an unknown key with the right boundary, inspect the new key at the current index before advancing it.

50. Three-way quicksort omits the equal block from recursion. With a first-key pivot and one ternary comparison per remaining key, an all-equal input costs $n-1$ comparisons in one partition. Count Boolean tests separately if that is the requested operation.

51. A constant number $r$ of distinct key values gives an $O(nr)$ bound for the simple three-way recursion. A single frequent value does not force linear total work when the remaining records have many distinct keys.

52. Neither ordinary Lomuto nor ordinary three-way swapping is stable. Equal keys can move through swaps with unrelated keys. Adding an equal region improves duplicate handling, but does not automatically preserve original equal-key order.

53. In a zero-based binary heap, children are $2i+1,2i+2$ and a nonroot parent is $\lfloor(i-1)/2\rfloor$. The last internal node is $\lfloor n/2\rfloor-1$. For $n\leq1$, there is no internal node to sink.

54. Floyd construction processes internal nodes from bottom to top. Each child's subtree is already a heap when its parent is sunk. This direction is the inductive reason that one downward repair suffices.

55. Summing node heights proves Floyd construction linear: most nodes have small height. Multiplying $n$ nodes by the root's height gives only an unnecessarily loose $O(n\log n)$ bound.

56. Building a heap by repeated insertion is a different algorithm from Floyd construction. It can require $\Theta(n\log n)$ comparisons even though bottom-up construction is $\Theta(n)$. State which construction the question specifies.

57. During heapsort, the live heap occupies a prefix and the final sorted records occupy a suffix. After exchanging the root with the last live record, decrease the heap size before sinking. The sorted suffix must never be included in later repairs.

58. Heapsort is generally unstable because a root exchange can reverse equal identities. Its worst-case comparison cost is $\Theta(n\log n)$, but the stated early-stop sink can make all-equal input linear. Do not turn a worst-case bound into an every-input bound.

59. In a binary comparison decision tree for distinct keys, there are at least $n!$ distinguishable orderings. Worst depth is at least $\lceil\log_2(n!)\rceil$. A node with a three-outcome oracle requires a separately stated branching model.

60. A comparison lower bound does not prohibit linear best-case behavior. It says some distinct-key input requires the large depth for a correct general sorter. It also does not apply to a counting algorithm that exploits a restricted integer universe.

61. For known multiplicities $m_1,\ldots,m_r$, the number of key-order arrangements is $n!/\prod_j m_j!$. The binary information bound is its base-two logarithm. State whether labels must also be stably preserved and what information is given in advance.

62. Merging already sorted distinct runs needs only $\binom{p+q}{p}$ possible interleavings, not $(p+q)!$. Its information lower bound is therefore $\lceil\log_2\binom{p+q}{p}\rceil$. Ordinary head merging need not attain this bound on unequal run lengths.

63. Randomization cannot evade the general comparison information bound on expected comparisons averaged over uniformly distributed distinct-key permutations. Conditioning on the random choices yields deterministic trees; averaging preserves the lower bound.

64. Counting sort with key interval $[L,H]$ uses $K=H-L+1$ counters. Its usual cost is $\Theta(n+K)$ and stable auxiliary storage is $\Theta(n+K)$. A large sparse key interval can dominate both even if only a few key values occur.

65. Frequency counts alone suffice to reconstruct sorted integer keys, but not arbitrary records with payloads. Stable counting sort scatters original records into an output array. The two versions solve different output contracts.

66. Prefix counts represent exclusive ends of key blocks. Scanning input from right to left, decrement the appropriate end and place the record there. This direction preserves original tie order.

67. With cumulative ends, a left-to-right scatter reverses ties. A left-to-right stable scatter instead uses starting positions and increments them. Direction and pointer meaning must be paired consistently.

68. A monotone shift $k\mapsto k-L$ preserves signed integer order and makes keys nonnegative. Sorting unsigned encodings of negative values without a corresponding monotone transformation can put negative keys after positive ones.

69. LSD radix sorting requires a stable sort at each digit. After $t$ passes, records are ordered by the low $t$ digits. An unstable later pass can destroy the lower-digit ordering established by earlier passes.

70. Sorting all records globally by the most significant digit and then globally by a less significant digit makes the later digit primary. MSD radix instead recurses within earlier digit buckets. These are different procedures.

71. If keys satisfy $0\leq k<U$, the digit count is $\lceil\log_B U\rceil$ for $U>1$. If the maximum key is inclusively $M$, it is $\lfloor\log_B M\rfloor+1$ for $M>0$. The difference matters exactly at powers of the base.

72. Compute digit counts by exact repeated integer division when implementation correctness matters. Dividing bit lengths is not a valid replacement for logarithms in an arbitrary base. For $U=3^{10}$, the maximum $U-1$ needs ten base-three digits.

73. Radix cost is $\Theta(d(n+B))$ for $d$ digit passes with counting-based digit sorting. A larger base reduces passes but increases counter initialization and storage. The best base depends on both the word width and the input size.

74. The word-RAM assumption must include digit extraction and integer arithmetic costs. If keys contain $\Theta(n)$ bits, reading all keys already requires quadratic bit volume. A constant-time unbounded-integer assumption cannot silently justify a bit-complexity claim.

75. FIFO distribution into digit buckets followed by concatenation is stable. Prepending to each bucket reverses local order unless it is reversed back appropriately. Check identity order at every pass, not only the final keys.

76. Bucket sorting is expected linear under suitable distribution and independence assumptions; its worst case can be quadratic with insertion-sorted buckets. Uniformity is an assumption about input generation, not a property obtained by drawing equal-width buckets.

77. With independent uniform assignment to $B$ buckets, $\mathbb{E}[\sum_j N_j^2]=n+n(n-1)/B$. This second-moment calculation explains the expected local quadratic work. Dependence or concentration can invalidate the conclusion.

78. For variable-length strings in MSD sorting, the end-of-string symbol precedes every real character. Otherwise a proper prefix can be put after its extension. Complexity must account for inspected characters and the representation of the alphabet.

79. Introsort uses a depth budget to replace pathological quicksort subproblems with heapsort. Small-subproblem insertion sorting adds a controlled cutoff cost. Its guarantee comes from the fallback and budget, rather than from a promise that all pivots are good.

80. For external merging, distinguish comparisons from block transfers. With memory $M$, block size $B$, and a feasible fan-in of approximately $M/B-1$, each full read/write pass costs about $2n/B$ transfers, subject to rounding and buffering overhead. Always state the memory reserved for output and metadata before fixing the exact fan-in.
