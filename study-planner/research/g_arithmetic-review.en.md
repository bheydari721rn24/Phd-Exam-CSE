# Conditions, examination rules, and final reasoning checks

1. Specify the width and interpretation before calculating. The same n-bit vector has an unsigned value in $[0,2^n-1]$ and a signed two's-complement value in $[-2^{n-1},2^{n-1}-1]$; a bit pattern alone does not choose between them.

2. Index zero is the least significant bit throughout this chapter. A carry leaving column i enters column i+1 and has twice the weight of that column's sum bit. Translate other sources' indexing before using their formulas.

3. A half adder counts two equal-weight bits. Its XOR output has the original weight and its AND output has twice that weight. It has no independent carry-input terminal.

4. A full adder counts three equal-weight bits. Its sum is parity and its carry is majority, not a three-input AND. The integer identity $a+b+c=s+2d$ is the safest local verification rule.

5. Four full adders can count seven one-bit inputs by respecting column weights. A carry generated in the first compression stage must join other weight-two bits, never the remaining weight-one input.

6. The carry expression $ab\lor ac\lor bc$ is symmetric in the three inputs. The physical gate implementation and its path delays need not be symmetric, even when its Boolean function is.

7. XOR propagate is $p=a\oplus b$ and generate is $g=ab$. Their joint-one state is unreachable. This fact justifies using an OR instead of an XOR to merge mutually exclusive generated and propagated carries.

8. OR propagate is $a\lor b$. It gives a valid carry equation with AND generate, but does not preserve the exclusivity of generate and propagate. Never transfer an XOR-based exclusivity argument to this convention.

9. Sum formation requires parity: $s=(a\oplus b)\oplus c$. An OR-propagate signal cannot replace the first XOR, even if it is correct for carry formation.

10. The ripple word identity is $A+B+c_0=S+2^nc_n$. It follows by canceling internal carries after weighting each local full-adder identity. It remains valid for every input, independently of signed interpretation.

11. A generating column can initiate a long chain through many propagating columns. The number of generating columns is not the length of the carry dependency path.

12. A kill column has input pair 00 and forces its outgoing carry to zero. A generate column has pair 11 and forces it to one. A propagate column has unequal bits and copies its incoming carry under XOR propagate.

13. A circuit timing answer must state the gate library, gate delays, allowed fan-in, input arrivals and loading assumptions. The number of bits alone does not determine a numerical delay.

14. Arrival time at an acyclic gate is the maximum arrival among its inputs plus the relevant gate delay. Use this recurrence before selecting a critical path; adding every gate in the diagram overcounts parallel branches.

15. In the specified unit-delay factored ripple implementation, p and g arrive at one, $c_i$ at $2i+1$ for i≥1, and $s_i$ at $2i+2$ for i≥1. These are structural bounds with all primary inputs arriving at zero.

16. A late external carry can become the critical source. A bound derived for an operand arriving at zero cannot be reused unchanged for a carry arriving later.

17. The final carry and final sum have different paths. The overall settling bound is their maximum, but earlier sum bits generally have much shorter dependency paths.

18. Expanded CLA expressions contain one term for every possible generating position below the carry boundary, plus the term propagating the external carry. Missing a single position can be exposed by one generate followed by a propagate chain.

19. A flat two-level CLA assumes wide AND and OR gates. With two-input gates its products and output ORs require additional levels; “two-level” is not an implementation-independent speed guarantee.

20. Independently expanded carries use $n(n+1)/2$ nontrivial AND products and n final ORs under the stated counting convention. Product sharing changes this count and must be identified explicitly.

21. A group pair represents the function $f(c)=G\lor Pc$. Higher-after-lower composition is $(G_H\lor P_HG_L,P_HP_L)$. The lower group's carry must enter the higher group, not the reverse.

22. Group composition is associative because function composition is associative. It is not commutative: a higher kill and a lower generate behave differently from the same two groups exchanged.

23. The empty group's pair is (0,1), since it passes its input carry unchanged. Padding a prefix tree with (0,0) introduces a kill and changes the result.

24. A prefix node must name the contiguous interval it represents. A correct stage count cannot compensate for duplicated, omitted or reversed intervals in its wiring.

25. For a power-of-two n, a doubling prefix network reaches full coverage in $\log_2 n$ composition stages. This excludes p/g generation and final sum XOR gates, and does not model physical wire delay.

26. The dense doubling prefix topology has $n\log_2n-n+1$ combining nodes for a power-of-two width. Other topologies have different area, fan-out and depth; this is not a universal prefix-adder count.

27. Four-bit CLA blocks connected by rippling block carries retain an interblock chain. A second-level group lookahead network is needed to accelerate that chain itself.

28. Carry-select computes both possible results of a block before its actual carry arrives. Its selector must choose all sum bits and the outgoing carry, not just the sum word.

29. A two-block eight-bit carry-select design with a four-bit low ripple block and duplicated four-bit high blocks uses twelve full adders and five one-bit selectors under the unoptimized block convention.

30. The square-root block-size result applies to the explicit model $\alpha b+\beta(n/b-1)$. It does not automatically describe recursive carry-select designs or physical layouts with unequal wire delays.

31. Under XOR propagate, a block with every propagate one passes its incoming carry unchanged. Under OR propagate the block generate must also be zero before this exact bypass statement is valid.

32. Carry-increment derives the carry-one result by incrementing a carry-zero result. The incrementer's carry must be combined with any original block-generated carry under a proved convention.

33. A half subtractor obeys $a-b=d-2r$, with $d=a\oplus b$ and $r=\overline a b$. The minus sign on the borrow weight distinguishes it from addition.

34. A full subtractor's borrow is $\overline a b\lor\overline a r\lor br$. Equal operand bits propagate borrow, unlike the unequal-bit propagation of an adder's XOR carry.

35. Ordinary subtraction uses $A+\overline B+1$. Its final carry is a no-borrow predicate: one means A≥B for unsigned inputs of equal width.

36. Equality in unsigned subtraction gives carry one and borrow zero. Treating carry one as strict greater-than incorrectly includes equal operands.

37. Subtract-with-borrow $A-B-r$ requires adder carry-in $1-r$. Supplying one regardless of r silently omits the incoming borrow.

38. A shared add/subtract datapath complements B conditionally using XORs and sets carry-in to the subtraction mode. Changing only the XOR controls computes subtraction minus one.

39. Unsigned carry indicates that the exact sum exceeds the retained unsigned range. Signed overflow indicates that the signed exact result exceeds its signed range. Neither flag can replace the other.

40. Opposite-sign ordinary addition cannot overflow in two's complement. Equal-sign addition overflows exactly when the retained result sign differs from the operand sign.

41. Carry into the sign column XOR carry out detects signed addition overflow. This includes carry-in arithmetic when the intended exact sum explicitly contains that incoming carry.

42. Four-bit seven plus one has V=1 and C=0. Four-bit minus one plus one has C=1 and V=0. Keep both counterexamples available when rejecting a proposed flag equivalence.

43. Signed subtraction overflows when operand signs differ and the retained result sign differs from A. Derive it from addition to complemented B, but interpret the flags under the original subtraction contract.

44. Signed less-than from subtraction is N XOR V. N alone fails precisely in overflowing cases such as seven minus minus one at width four.

45. Unsigned less-than from the complemented-adder subtractor is NOT of final carry. Signed ordering must not use this borrow predicate.

46. Signed less-or-equal is $(N\oplus V)\lor Z$, where Z tests the complete retained difference. Equality itself is independent of signedness for equal-width bit vectors.

47. An unsigned comparator is decided by the most significant differing bit. Lower-bit differences cannot outweigh it; they matter only while all higher bits are equal.

48. Equality is the AND of per-bit XNORs. A balanced tree and a serial chain implement the same function but have different depth.

49. Comparator group greater-than is $G_H\lor E_HG_L$, and group equality is $E_HE_L$. This ordered composition supports hierarchical comparison for the same reason that group carry functions support prefix addition.

50. Flipping both operands' sign bits maps signed order monotonically onto unsigned order. It adds the same bias $2^{n-1}$ to their signed values; flipping only one operand does not.

51. Sign-extend signed operands before widening arithmetic. Extending an already wrapped narrow result cannot recover the lost exact value.

52. A widened signed result can be narrowed safely only when every discarded bit matches the retained sign. Zero discarded bits alone do not prove signed safety.

53. Unsigned saturation selects all ones on carry. Signed saturation uses overflow and the original operand sign to select the upper or lower signed bound; the wrapped result sign points in the opposite direction on overflow.

54. Fixed-point addition requires aligned binary-point scales. An otherwise correct integer adder gives a wrong real-value operation when its operands' bit positions represent different scales.

55. Valid BCD digits lie in zero through nine. A single-digit sum with a one-bit incoming decimal carry lies in zero through nineteen, which is the domain used to prove the correction predicate.

56. The BCD correction predicate is $q=k\lor z_3z_2\lor z_3z_1$. It distinguishes eight and nine from ten through fifteen and also catches totals sixteen through nineteen.

57. Correct BCD by adding six to the low binary nibble when q is one. Decimal carry is q; the carry of the correction adder alone misses initial totals sixteen through nineteen.

58. An invalid BCD input is outside the normal digit-adder contract. Either detect it or enforce the invariant upstream; a final valid-looking digit does not prove the input was valid.

59. Cascaded BCD digit carries have decimal place weight. Dropping the final carry computes modulo $10^d$ for d retained digits, rather than the binary modulo of an unstructured bit word.

60. Carry-save compression obeys $X+Y+Z=S+2C$ when C is stored without its left shift. If the stored row is already shifted, the identity is instead $X+Y+Z=S+C_{shifted}$.

61. Carry-save columns operate independently, giving constant local compression depth. A final carry-propagate addition is still required to produce an ordinary binary result.

62. Three maximum n-bit inputs can require n+2 result bits. Derive the maximum value rather than assuming every arithmetic stage needs only one extra bit.

63. A zero carry-save sum row does not establish a zero total. Under an exact nonnegative specification, both the sum row and unshifted carry row must be zero.

64. An unsigned n×n multiplier has $n^2$ AND partial products. Each product belongs in column i+j, with weight $2^{i+j}$; row alignment is arithmetic, not decoration.

65. Unsigned n×n multiplication fits a conventional 2n-bit output. The current input may need fewer significant bits, but a fixed-width datapath reserves the maximum specified range.

66. Carry-save multiplier trees reduce the number of rows without immediately propagating carry across the whole word. Their final two rows still need a carry-propagate adder.

67. A signed multiplier's sign bit has negative weight. An unsigned multiplier fed the same input patterns generally computes a different integer product; changing the output label cannot correct it.

68. The minimum negative n-bit signed value has no positive counterpart at the same signed width. Widen before forming its positive magnitude or use an explicitly unsigned magnitude representation.

69. Radix-two Booth digit $d_i=b_{i-1}-b_i$, with $b_{-1}=0$, belongs to −1, zero or one. Pair ordering must be stated before associating 01 or 10 with add/subtract operations.

70. Booth recoding compresses a run of ones into boundary operations. Inputs with frequent transitions may not reduce the number of nonzero rows; recoding is not an input-independent speed proof.

71. A signed n×n product fits 2n signed bits, but can require all of them. The minimum-negative times itself produces the largest positive product and is a useful narrowing boundary test.

72. Unsigned product narrowing checks that the high half is zero. Signed narrowing checks sign-extension consistency with the retained low-half sign; the two tests answer different questions.

73. Unsigned long division maintains processed prefix $P=DQ+R$ with $0\le R<D$. Updating with next bit x uses trial $U=2R+x$, which is below 2D and needs at most one subtraction.

74. The division trial remainder may need one more bit than the divisor. Keeping only k bits before comparing U with a k-bit divisor can discard the very overflow that determines the next quotient bit.

75. Division by zero is outside the ordinary invariant. Reject it before constructing a normal trace or specify a separate architectural exception; a visually produced quotient is not a mathematical answer.

76. Signed division must state its rounding and remainder convention. Under truncation toward zero, a nonzero remainder follows the dividend's sign, and minimum-negative divided by minus one is an overflow boundary.

77. Multiword addition propagates the low carry into the next limb. Complete-word zero requires every retained limb to be zero; low-limb zero alone cannot serve as the word zero flag.

78. Multiword subtraction propagates the borrow using the selected flag polarity. A no-borrow carry from the lower limb is the carry input of the next complemented-addition limb.

79. A stored carry flag and a combinational carry wire are different signals. Feeding the output directly back to the input creates a combinational cycle; instruction sequencing needs a register and an explicit update enable.

80. A teaching checkpoint certifies the exact mathematical state it shows, not electrical timing, glitch behavior or guaranteed unseen-examination success. Solve a new problem by restating its number representation, weights, widths, control convention and proof obligations before applying a remembered formula.
