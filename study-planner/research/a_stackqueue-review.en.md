# Examination rules and precise retrieval notes

1. Write a stack bottom-to-top and a queue front-to-rear before tracing. LIFO and FIFO describe which live identity leaves, rather than sorting values or using physical array order.

2. For an initially empty structure, occupancy after any prefix is insertions minus successful removals. Every prefix must be nonnegative; a valid final balance cannot repair early underflow.

3. The minimum capacity for a prescribed legal insertion/removal history is its maximum prefix occupancy. Capacity depends on the interleaving, even with the same total insertion and removal counts.

4. A bounded structure requires occupancy at most capacity at every prefix. Rejecting, overwriting, blocking, and dropping are different overflow contracts with different output histories.

5. A next-unused stack counter n places the live top at n−1. An occupied-top counter t places it at t. Translate using n=t+1 before adapting code or formulas.

6. Underflow checks must occur before decrementing an unsigned counter or indexing the top slot. An invalid operation must not partially mutate the structure under a reject-without-change contract.

7. Clearing a popped reference prevents unintended object retention. The number of payload writes, reference clears, metadata writes, and allocation operations should be counted separately when an exact cost is requested.

8. A linked stack needs its top at the head for constant-time removal with singly linked nodes. A cached tail does not reveal its predecessor, and one cached predecessor does not solve all future pops.

9. For a non-sentinel linked queue, empty means head and tail are both null. Dequeuing the singleton must clear tail as well as head before a future enqueue uses that handle.

10. A doubly linked deque gives constant-time endpoint updates when both endpoints are accessible. Its backward links solve the singly linked tail-predecessor problem.

11. For a circular deque sentinel s, empty means s.next=s and s.prev=s. A singleton removal must restore both fields; the sentinel is structural storage and remains alive.

12. Every doubly linked neighbor pair must satisfy forward/backward consistency. Updating only the forward link can preserve one traversal while breaking another operation's invariant.

13. Initialize a newly allocated node before linking it into the public representation. Allocation failure should leave the original links unchanged when the operation promises failure-safe behavior.

14. Two opposing stacks in C slots are full when $\ell+1=r$. Their free interval has $r-\ell-1$ slots, rather than a fixed half of C for each stack.

15. Independent shared-stack empty tests are leftTop=−1 and rightTop=C. Space shared by the two stacks does not permit one to pop the other's values.

16. In a count-based ring, front f is the next removal slot, and logical rank j maps to $(f+j)\bmod C$ for 0≤j<n. Count n and physical capacity C are separate quantities.

17. The next enqueue slot in that representation is $(f+n)\bmod C$. Enqueue leaves front unchanged; dequeue advances front and decreases count.

18. A count-based ring can use all C slots and distinguishes full from empty with n=C versus n=0. Equality of rear and front is possible in both states.

19. A reserved-slot ring has empty f=r and full $(r+1)\bmod C=f$. Its usable capacity is C−1, and occupancy is $(r-f+C)\bmod C$.

20. A capacity-one reserved-slot ring holds no data, whereas a count-based capacity-one ring holds one item. Always check which capacity convention a question uses.

21. With successful totals e enqueues and d dequeues, a forward count-based ring's final front is (initialFront+d) mod C and count is initialCount+e−d. These formulas alone do not prove prefix legality.

22. Modular queue conventions need semantic names. A backward-growing next-rear cursor is not interchangeable with a forward-growing front cursor, even if both are integers in the same range.

23. Mathematical modulo is nonnegative for positive modulus, while signed remainder in some programming languages can be negative. For a ring decrement, add C before taking remainder under a safe integer-range assumption.

24. Bit masking by C−1 implements modulo C for nonnegative integers only when C is a power of two. A visually circular buffer does not imply power-of-two capacity.

25. Ring resizing copies logical order from old slots (front+j) mod oldCapacity into new slots j. Copying physical slot order can rotate the queue incorrectly.

26. After logical-order relocation, front becomes zero and live count is retained. A separate next-insertion cursor becomes n modulo the new capacity, rather than the old physical rear.

27. Geometric growth gives a geometric sum of copies. For capacity-one doubling and m≥1 append-only updates, copy writes total $2^{\lceil\log_2 m\rceil}-1$; new-element writes add m.

28. One resize operation can be linear even when every operation type has constant amortized cost. A deadline or worst individual latency cannot be inferred from a sequence-average guarantee.

29. Amortized analysis applies to every allowed history under the stated initialization. It is not an average over randomly sampled inputs or operations.

30. Separate-buffer doubling temporarily holds old C and new 2C slots. Peak slot storage is 3C slots before metadata, while the final new array has 2C slots.

31. Growing when full and shrinking at half occupancy can thrash under alternating insertion and removal. Separated thresholds, such as quarter-full contraction, force enough ordinary operations between costly rebuilds.

32. The piecewise dynamic-array potential depends on count and capacity, not on the ring front. Its relocation proof still requires copying the logical order correctly.

33. Exact potential charges depend on the primitive cost model. Charging allocation zero-fill, read/write separately, or nonconstant payload copying changes constants and can change applicability.

34. For a two-stack queue with bottom-to-top lists I and O, logical order is reverse(O) concatenated with I. This equation determines which stack holds the oldest pending item.

35. Transfer I to O only when O is empty. Pushing newer input onto a nonempty output stack can place a late arrival before an older unremoved value.

36. For e enqueues, d successful dequeues, and t moved items, primitive push/pop work is $e+2t+d$. Each moved item needs one pop and one push, not one combined primitive.

37. Each inserted item transfers from input to output at most once in the ordinary destructive queue. Therefore $t\le e$ and total work is at most $3e+d$ from empty initialization.

38. The potential $2|I|$ charges enqueue three and dequeue one under unit stack primitives. A transfer of k items costs 2k+1 but releases 2k units of saved potential.

39. A front query may trigger one complete transfer but must not remove the observed oldest item. Repeated front queries after that transfer are cheap, and their observation cost can be counted separately.

40. A preloaded input stack contributes an initial potential term. Excluding its construction invalidates a constant-per-measured-operation bound that silently assumes empty initialization.

41. The simple two-stack amortization proof assumes a destructive history. Branching persistent versions can repeat transfers and require a different analysis or memoized scheduling mechanism.

42. A stack built with one queue makes push or pop linear through rotations. Summing an expensive operation across growing or shrinking sizes can give quadratic work; it does not inherit two-stack FIFO amortization.

43. Expensive-push stack construction costs 2j+1 queue primitives at old size j. Building n values therefore costs $n^2$ under that exact model.

44. Expensive-pop stack removal costs 2j−1 queue primitives at live size j. Removing n values costs $n^2$, before counting their earlier insertions.

45. Moving one stack to another reverses bottom-to-top order. Moving it back supplies a second reversal and restores the original sequence.

46. Interface-only iterative size with restoration uses 4n push/pop primitives with one temporary stack. A cached library size can be constant time because it uses additional representation metadata.

47. A preserving stack copy creates its copy on the restoration pass, not during the initial reversal. The standard two-pass copy uses 5n push/pop primitives and restores the source.

48. Recursive preserving size uses 2n data-stack primitives but n+1 simultaneous calls including the base case. Lack of an explicit temporary container does not imply constant auxiliary space.

49. A loop that removes one item while testing i<currentSize performs $\lceil n/2\rceil$ iterations from initial size n. Save the original bound or test emptiness according to the intended traversal.

50. Reenqueuing every removed item preserves positive queue size. A while-not-empty loop then cannot terminate without another exit condition or external intervention.

51. Independent container storage does not imply independent payload objects. Shallow reference copying can share objects while preserving separate membership and ordering.

52. A test that promises restoration must restore removed values before every return path, including an early failure. Correct Boolean output alone does not prove a nondestructive postcondition.

53. A pop-and-restore predicate writes memory and is not automatically a pure assertion. Debug checks that mutate or allocate can alter behavior even if they restore the abstract sequence on success.

54. Stack-output validation from increasing distinct inputs has forced greedy steps. If the next desired value is already pushed but covered by another top, no later push can expose it without a wrong output.

55. The successful greedy trace gives minimum required stack capacity because all its pending smaller values are forced by the fixed input order. Peak occupancy is a lower bound as well as a construction.

56. Fixed increasing input produces exactly 312-avoiding output permutations. The 231 pattern describes the inverse input-sorting convention; check orientation before using a named pattern.

57. Distinct-input complete push/pop histories correspond to Dyck paths: equal numbers of steps, nonnegative prefix height, and final zero. They are counted by Catalan numbers rather than n!.

58. Catalan $C_n$ equals $\binom{2n}{n}/(n+1)$. Reflection removes the balanced words that first reach height −1; balanced final counts without prefix constraints overcount legal histories.

59. The first-return Catalan recurrence partitions the path into a matched outer pair, its legal interior, and a legal suffix. Their sizes determine a unique decomposition.

60. Capacity h imposes a height bound on the path. Use a push/pop dynamic program with $0\le p-d\le h$ instead of substituting the unrestricted Catalan count.

61. Histories needing exactly h slots equal the count at height at most h minus the count at height at most h−1. These capacity classes are nested, so subtraction is justified.

62. Duplicated input values break a direct count of distinct-value output permutations. Track occurrence identities or explicitly deduplicate outputs before applying a permutation-count interpretation.

63. Mixed brackets require a typed stack of unmatched openings. Equal opening/closing counts and nonnegative height do not reject crossing types such as ([)].

64. Bracket space equals maximum nesting depth. Parsing actual source code first requires tokenizing strings and comments so that non-delimiter characters are not mistaken for syntax.

65. Postfix scanning is left to right; its first pop is the right operand and second pop the left. This order matters for subtraction and division even when commutative examples hide the error.

66. Prefix scanning is right to left; its first pop is the left operand and second the right. Adapting postfix code without reversing these roles changes the expression.

67. A binary postfix expression with n operands has n−1 operators, but every operator must also find two existing values and the final stack must contain exactly one result.

68. An arity-k operator changes value-stack height by 1−k and requires k prior values. Total height balance is a necessary condition, not a substitute for prefix arity checks.

69. Division by zero, unsupported tokens, overflow, and numeric type policy are additional expression validity checks. A syntactically balanced value stack does not prove arithmetic definedness.

70. Infix conversion pops higher-precedence operators and equal-precedence operators only for a left-associative incoming operator. Right-associative exponentiation retains equal precedence until its right side completes.

71. Unary minus needs its own arity and precedence rule. The meaning of -2^2 depends on the grammar; explicit parentheses determine the intended base or negation scope.

72. Linear token-stack actions do not guarantee linear immutable-string conversion or arbitrary-precision evaluation. Count character copying and bit arithmetic separately when their sizes grow.

73. Cached prefix minima/maxima expose the correct surviving aggregate after each pop. A single insert-updated global extremum cannot reconstruct a removed maximum from its old value alone.

74. A separate extrema stack must retain equal extrema or their multiplicity. Pushing only strict record values and popping on equality loses duplicate maxima after one copy is removed.

75. Associative queue aggregates require input caches in arrival order and output caches in removal order. Combine output before input; associativity does not authorize reversing factors.

76. Monotone stacks should store indices when distance, expiration, boundaries, or duplicate identity matters. A value-only representation may compute an extremum but lose the requested position information.

77. For next strictly greater, resolve pending values with a strict comparison. Greater-or-equal changes the equality rule and the pending-value invariant; test duplicates explicitly.

78. A monotone algorithm's nested pop loop is aggregate linear because each identity is inserted once and removed at most once. A costly individual iteration and a linear total can both be true.

79. Histogram area for a popped height uses width $i-k-1$. Sliding-window extrema additionally expire indices by age; equal-value domination affects argmax identity but need not change maximum values.

80. Josephus queue simulation rotates k−1 survivors before removal, while its zero-based survivor recurrence adds k modulo the new problem size. General weighted shortest paths, concurrent updates, persistent branching queues, and full parser grammars require additional invariants beyond the sequential endpoint structures proved here.
