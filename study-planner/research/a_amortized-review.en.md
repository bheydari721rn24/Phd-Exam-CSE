# Final reasoning rules

1. Distinguish the number of public operations from the current number of stored records; they are different parameters in a sequence theorem.

2. State the initial structure explicitly, because an arbitrarily preloaded structure can contain unpaid cleanup work.

3. Identify the charged primitive before computing an exact answer; copied records, comparisons, writes and allocation are different units.

4. A deterministic amortized theorem applies to every legal sequence and does not require random input order.

5. Expected time requires an explicit random experiment or distribution; it is not another name for amortized time.

6. Constant amortized cost permits expensive individual calls, so it does not establish constant latency.

7. Aggregate analysis counts total real work directly; dividing independent maximum call costs is often unnecessarily pessimistic.

8. A resource consumed at most once provides a lifetime counting argument only if the operation never recreates that resource without paying again.

9. Accounting must maintain solvency at every permitted prefix, rather than merely matching totals at the final endpoint.

10. Credits attached to initial records need an initial allowance; those records were not inserted by the analyzed sequence.

11. The exact potential identity is actual total equals charge total plus initial potential minus final potential.

12. Nonnegative potential by itself does not remove a positive initial potential term.

13. A relative lower bound at least equal to initial potential suffices even if the displayed potential values are negative.

14. A known global lower bound gives an additive allowance equal to initial potential minus that lower bound.

15. Negative amortized charges are legal releases of stored credit and must never be interpreted as negative execution time.

16. Adding a constant to potential changes neither charges nor the difference between its endpoints.

17. Scaling potential changes the charges and can be necessary when cleanup primitives have higher costs.

18. Derive a potential coefficient from an exact expensive transition before checking all ordinary transitions.

19. Big-O and Theta expressions cannot be canceled without bounding their hidden coefficients in the required direction.

20. A complete case analysis checks both sides of a piecewise potential boundary and the smallest reachable capacity.

21. A bounded multipop removes the minimum of its requested count and the current size; use actual removals in a cost formula.

22. Empty multipop has zero element work but still has constant dispatch or check work in a fuller model.

23. A stack with unit push and unit removal can charge two per push when it starts empty.

24. A stack with initial size s and final size t has exact element work twice its analyzed pushes plus s minus t.

25. Multipush changes the input unit: a call creating k records cannot have constant cost independently of k.

26. An unbounded binary increment flips its trailing ones plus the next zero, and popcount potential gives charge two.

27. From zero, unbounded binary flips after N increments are exactly twice N minus popcount of N.

28. The exact counter floor sum includes only bits that exist in the selected representation.

29. A finite-width all-ones wrap has no new one bit; its bit-flip charge is zero under popcount potential.

30. A counter beginning nonzero retains its initial popcount in the telescoping formula.

31. Alternating increment and decrement across a carry boundary defeats the increment-only constant amortized theorem.

32. A reset that scans every bit can be expensive repeatedly even when the counter is already zero.

33. Sparse resetting requires maintained metadata or another valid way to reach set positions; it is not a free primitive.

34. Base-b digit-change potential can use digit sum divided by b minus one, with a fractional charge bound.

35. Weighted high-bit costs can change constant digit-change amortization to logarithmic average work.

36. A capacity-one doubling array grows on the append after becoming full, not on the append that fills its last slot.

37. For positive N, final doubling capacity is the smallest power of two at least N; handle zero separately.

38. Exact copied records from initial capacity one are final capacity minus one.

39. Exact copy-plus-write work is N plus final capacity minus one; a linear upper bound is not the exact count.

40. An initially larger capacity changes the starting term of the geometric copy sum.

41. Front insertion has shift work that resizing amortization does not remove.

42. Clipping insert-only potential at zero covers sparse initial states without an artificial negative starting balance.

43. The doubling growth transition ends after the new record is appended, so its completed potential is two in unit scaling.

44. A growth factor r gives charge at most one plus r divided by r minus one in the reduced copy/write model.

45. Integer ceiling preserves the general upper bound but can change the exact growth charge.

46. A growth factor approaching one with input size does not produce a uniform constant hidden in big-O notation.

47. Fixed additive capacity growth copies an arithmetic series and yields quadratic total copying.

48. Allocation or zero-filling a new buffer changes the rebuild coefficient and must be included when the contract charges it.

49. Nonconstant record constructors or string copies require a cost parameter beyond the number of records.

50. Pointer invalidation and exception safety are correctness obligations separate from favorable operation counts.

51. Shrinking at half occupancy after doubling can alternate full-buffer rebuilds on successive insert/delete calls.

52. Hysteresis requires a strict gap between the occupancy after resize and the opposing trigger.

53. For growth and shrink factors r, a fixed shrink threshold beta must lie strictly between zero and one divided by r.

54. A threshold gap that tends to zero with input size can make amortized constants grow with that input.

55. State whether the quarter-full test occurs before or after removal; exact copies and endpoint potential depend on that timing.

56. The main post-removal quarter policy uses dense potential twice size minus capacity and sparse potential half capacity minus size.

57. Crossing from half occupancy into the sparse branch gives a different deletion charge from remaining wholly in the dense branch.

58. Minimum capacity prevents repeated shrinking below the declared representation boundary and fixes the empty-state contract.

59. The main minimum-capacity-two policy begins with potential one; retain that one-unit allowance.

60. Completed-state capacity and peak simultaneous old/new allocation are different space measurements.

61. A two-stack queue's FIFO order is output from top to bottom followed by input from bottom to top.

62. Transfer input only when output is empty; moving new records ahead of old output can violate FIFO order.

63. Twice input size pays for one input pop and one output push per transferred record in the unit stack model.

64. A transfer-triggered dequeue and a normal output dequeue both have charge one in the primitive-only model.

65. Total queue size is a poor transfer potential because transferring records hardly changes that size.

66. A front query can trigger one transfer without removing a record; repeated fronts do not need repeated transfers.

67. A preloaded input stack supplies initial pending-transfer potential and prevents a from-empty bound from applying unchanged.

68. In a monotonic stack, each index is pushed once and popped at most once, which bounds total inner-loop iterations.

69. Failed value comparisons and empty-stack checks are different events and must be counted in the declared model.

70. Strict-smaller and smaller-or-equal pop rules encode different tie behavior even though both are linear in total.

71. Sliding-window expiration and dominance remove an index by alternative routes; they do not remove the same stored index twice.

72. Sorted-block merging costs proportional to output length, whereas a binomial-tree link costs constant primitive work.

73. Binary-level rebuilding contributes linear work per level across an insertion prefix and therefore logarithmic amortized insertion.

74. Searching every occupied sorted block can require a quadratic sum in the number of bit levels.

75. Root-count potential proves a binomial insertion bound only under its specified constant-cost link model.

76. A competitive move-to-front theorem compares with another algorithm and does not make arbitrary list accesses constant time.

77. Sparse initialization needs a valid readable-memory contract, round-trip membership checks and an explicit epoch-wrap policy when epochs are used.

78. Persistent branches can repeat deferred work from the same state; a linear-history potential cannot be spent independently on every branch.

79. Incremental rebuilding needs an authoritative read/write routing invariant and a deadline before the next capacity exhaustion, plus an allocation assumption.

80. Transfer learning to unfamiliar questions requires checking representation, costs, initial state, legal operations and triggers; a verified chapter does not imply a guaranteed answer to every unseen question.
