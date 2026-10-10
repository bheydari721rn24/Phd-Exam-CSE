# Final reasoning rules

1. Write the bit order before converting an address into an integer. With MSB-first order, the leftmost bit has the largest weight.

2. A 2:1 multiplexer returns its zero port when select is zero and its one port when select is one; derive every cascade from this rule.

3. A select pin controls a route rather than serving as an additional data operand. Substitute its two cases before recognizing a gate function.

4. The two-input selector equation is $\overline s d_0+sd_1$. The sum in this equation is Boolean OR.

5. Equal data cofactors remove dependence on the select in the truth function. They do not guarantee absence of physical glitches in every implementation.

6. Exchanging a selector's two data ports complements the select interpretation. It does not generally complement the output function.

7. A word selector applies one address to every bit slice. Count word-level blocks separately from one-bit selector cells.

8. Shannon expansion is proved by the two values of the chosen variable. It applies even when the remaining data cofactors are complicated functions.

9. Complete constant-leaf realization of an $n$-variable function uses $2^n$ data entries and $n$ selectors. These two quantities are not interchangeable.

10. Complete Shannon expansion supplies an upper construction bound. Cofactor sharing and constant reduction can make the actual circuit smaller.

11. For one residual variable, pairs 00, 01, 10, and 11 correspond respectively to zero, the variable, its complement, and one.

12. Construct each residual pair in increasing residual-variable order. Reversing that order exchanges the variable and its complement.

13. Two residual variables can produce sixteen different cofactors. The four-entry single-variable table is insufficient for that case.

14. Select variables should be chosen by cofactor complexity, sharing, and arrival time. Merely counting selected variables does not identify a uniquely best circuit.

15. Exchanging two selector bits permutes the truth-table addresses. Compensate by the corresponding data permutation if the function must remain unchanged.

16. In a four-input selector, swapping the two select wires exchanges data indices one and two while fixing zero and three.

17. An output inversion complements each cofactor. A select inversion instead permutes which cofactor is used.

18. A balanced $2^k$-input binary selector tree has $k$ levels and $2^k-1$ cells under a one-bit cell metric.

19. The tree's first stage normally consumes the least significant address bit when adjacent leaves are paired. A different pairing requires a correspondingly different address assignment.

20. For an $r$-ary complete tree with $N=r^h$ leaves, the cell count is $(N-1)/(r-1)$. The depth is $h$.

21. Mixed-radix trees require a level-by-level count. A formula for a uniform tree cannot be applied to arbitrary mixed blocks without checking its assumptions.

22. An incomplete input count produces unused binary address codes. Give those codes a defined response or explicitly declare them unconstrained.

23. A constant connection to an unused port implements a default value. It does not remove the port's address code from the input domain.

24. Gate count is not path delay. A tree's data arcs and select arcs can have different delays and different arrival times.

25. A selector applied at level $j$ traverses one select arc and all later data arcs. Include every remaining stage when calculating its arrival contribution.

26. Place a late selector near the output only after preserving the data permutation. Timing optimization must not silently change the logic function.

27. A static-one hazard is possible when unequal path delays interrupt two products that should collectively keep an output high.

28. The selector consensus term $d_0d_1$ can protect the single-select static-one transition without changing the truth mapping. Its scope does not include arbitrary simultaneous changes.

29. A decoder generates address predicates, not arbitrary source data. Its output index is determined by the address contract.

30. An enabled complete active-high decoder is one-hot. A disabled one is all zero, so “exactly one output” needs the enable assumption.

31. Distinct decoder minterms have zero product because at least one address literal conflicts. This is the algebraic reason for exclusivity.

32. The Boolean OR of all active-high decoder outputs equals enable. It is not always one.

33. An active-low output is asserted at numerical zero. Describe assertion and voltage polarity separately.

34. An active-low enable and active-low outputs introduce inversions at different circuit locations. They cannot be canceled merely by counting minus signs.

35. Active-low minterms realize a positive sum by a NAND of the selected output pins. ORing those negative pins generally gives a different function.

36. Derive the disabled value of the combining gate as well as its enabled truth rows. A correct active mapping can still violate the inactive interface.

37. Hierarchical expansion uses high address bits for bank enables and low bits for local addresses. The global index is the bank index times the local capacity plus the local index.

38. Predecoded predicates are shared signals. Their count does not include the final combining gates or the internal implementation of the predecoders.

39. Sharing predecodes trades repeated literals for fanout and an extra combination stage. Whether that is beneficial depends on the specified metric.

40. Several output functions may share one decoder while requiring different output-combination networks. Decoder sharing does not make their outputs identical.

41. Complementing a selected minterm set works as a complement function only when the decoder partitions the complete enabled domain.

42. A demultiplexer gates a decoded predicate by data. Zero data makes every active-high output zero even though one route is selected.

43. A decoder enable can serve as demultiplexer data under a matching polarity and inactive-state contract. Check those contracts before substituting the block.

44. The OR of all complete active-high demultiplexer outputs recovers the input data. An additional enable changes that result to enabled data.

45. An ordinary encoder assumes a legal one-hot input domain. Multi-request behavior of its equations is not automatically priority behavior.

46. Valid distinguishes no request from request zero. It does not prove that a nonempty request vector is one-hot.

47. A multiple-request input can create a phantom ordinary-encoder code that corresponds to no requested index. Use a legality detector or a priority resolver.

48. The bitwise nonzero power-of-two test detects one-hot words. Its arithmetic proof clears the least significant asserted bit and checks whether any other asserted bit remains.

49. Highest-index and lowest-index priority are different specifications. State which wins whenever more than one request is possible.

50. A priority grant is the request AND the absence of every outranking request. Encoding raw requests skips this essential suppression operation.

51. The priority endpoint has an empty suppression product equal to one. This ensures the highest-priority request can actually win.

52. Prove both at-most-one grant and existence for nonempty requests. Together they establish exactly one winner on the valid domain.

53. Group validity chooses the winning group. A selector must then choose that group's local code; ORing all local codes can generate a phantom global index.

54. A group tree can reduce logical dependency depth, but an actual delay claim needs gate fan-in, loading, and cell-arc assumptions.

55. A leading-zero counter must represent the full word width for a zero word. Its range can need an extra bit compared with a nonzero priority index.

56. Rotating priority is a circular order defined by a supplied pointer. Numeric highest or lowest priority is not equivalent after wraparound.

57. Round-robin fairness requires sequential pointer updates and service-progress assumptions. A combinational winner alone supplies no long-term service guarantee.

58. A complete ROM with $n$ address bits and $w$ output bits stores $2^nw$ truth bits. Peripheral circuitry is not included in that count.

59. A ROM's output columns are separate Boolean functions sharing one address. Word width and address width count different dimensions.

60. A row-column organization preserves capacity. Use quotient for the row and remainder for the column under the stated low-column-bit convention.

61. A physically square bit array need not split its address bits equally. Each word contributes multiple adjacent bit columns.

62. Legal entries and physical address rows are separate counts. Ten legal words in a complete sixteen-row table still require sixteen stored defaults or data words.

63. ROM lookup and synthesized logic may have the same truth mapping without the same area, delay, programmability, or inactive electrical behavior.

64. A PLA shares selected product terms between outputs. A product omitting an input variable is a cube that covers both values of that variable.

65. A conventional PAL fixes output product groups and can require duplicated products. Specialized device feedback must be stated before altering this architecture-based count.

66. NAND-NAND equivalence follows from De Morgan's law with explicit internal complements. A visually similar two-level NOR circuit needs its own polarity derivation.

67. Seven-segment words need a declared segment order and active polarity. The displayed digit alone does not specify an external bit pattern.

68. A specified blank output on invalid BCD inputs is a real constraint. Those rows cannot also be marked don't-care during minimization.

69. Compare segment geometry with an independently stated reference. A checker sharing the implementation's erroneous constants can pass every case incorrectly.

70. Z denotes a disconnected tri-state driver, not a zero-valued driver. An undriven unpulled bus has no guaranteed binary value.

71. Opposing active push-pull drivers create contention. Boolean OR of their data is not an electrical explanation of the shared bus.

72. Check enable ownership independently from data agreement. Two equal-value drivers can still violate a single-owner contract.

73. A crossbar selects values for destinations and permits source replication. Exclusive resource allocation requires an additional arbitration rule.

74. Complete combinational HDL assigns every output on every path. A default before priority or case logic makes inactive behavior explicit.

75. Independent HDL if statements let later assignments overwrite earlier ones. An if/else-if chain gives priority to the first true branch instead.

76. Unknown-valued HDL semantics require a separate verification contract. Wildcard matching can conceal an unknown rather than prove the underlying hardware correct.

77. A selector wiring test needs distinguishable data patterns. All-zero and all-one patterns cannot expose port permutations.

78. Test a decoder's output index and exclusivity together. Population count alone does not catch exchanged output wires.

79. Derive each intermediate signal in a mixed arithmetic-selector circuit before enumerating final minterms. Carry, parity, and an XOR of those signals are different functions.

80. Use symbolic proofs, independent finite-domain oracles, source checks, and visual inspection together. Report remaining boundaries honestly rather than converting finite evidence into a guarantee about every unseen examination question.
