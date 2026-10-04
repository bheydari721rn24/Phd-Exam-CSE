# Complete summary and examination rules

1. A combinational specification assigns permitted output vectors to present input vectors. Write the input width, output width, bit order and polarity before deriving equations; these conventions determine the meaning of every indexed row.

2. A completely specified n-input, m-output block has 2^n input rows and m times 2^n output-bit entries. The number of possible functions is 2 raised to that entry count, not merely the number of rows.

3. A truth table is a functional reference rather than a physical circuit. Many netlists can implement the same table while differing in gate count, timing, fan-out, hazards and power.

4. A partial contract is a relation describing permitted output vectors. Treat output bits as independent don't-cares only when every combination of their permitted values is legal; cross-output restrictions need explicit relational checks.

5. Validity and payload are separate obligations. An invalid payload may be unrestricted while its validity bit remains fixed; freeing the payload never authorizes changing the validity signal.

6. A care-set equivalence proof requires the candidate to match the reference on every care row. Disagreement elsewhere is permitted only if the environment actually guarantees that those rows cannot matter.

7. Unspecified behavior is not the same as contradictory behavior. A legal input with no permitted output makes the specification unsatisfiable, whereas a row admitting several outputs permits implementation choice.

8. Complete the specification before minimizing. Priority, simultaneous requests, disabled behavior and invalid encodings are semantic choices that Boolean simplification cannot resolve on your behalf.

9. Keep binary index order separate from table presentation order. In order A,B,C, the index is 4A+2B+C even when B and C are selected by a mux or rows are rearranged geometrically.

10. A multi-output truth-table row specifies an ordered word. Reversing the word bits exchanges output meanings even if the same decimal input addresses remain in the same sequence.

11. Combinational history independence applies after settling. A finite propagation interval does not make a circuit sequential, but indefinitely retained dependence on previous inputs does.

12. To refute combinational behavior, exhibit two histories reaching identical present inputs with different settled outputs. Merely showing that output changes sometime after an input is not such a counterexample.

13. A directed acyclic composition of verified total Boolean blocks is combinational. Prove it by substituting predecessor functions in topological order, starting at the primary inputs.

14. The topological proof assumes one well-defined driver per net. Connecting two ordinary gate outputs requires an electrical resolution model and cannot silently be interpreted as an OR function.

15. Fan-in counts a gate's input pins; fan-out counts receiving pins driven by a net. Count repeated tied pins according to the problem's stated convention rather than inventing a universal pin-count rule.

16. Logical gate levels follow dependency paths, not the order in which equations appear on a page. Two independent intermediate equations can operate in parallel even when written on separate lines.

17. Feedback defeats the general DAG evaluation guarantee, but not every algebraic feedback equation has two stable Boolean solutions. Check fixed points before making a specific claim about state or oscillation.

18. The equation q equals NOT q has no stable Boolean solution; q equals q has two; q equals q AND zero has one. These examples distinguish existence, uniqueness and structural acyclicity.

19. Label each internal net and derive all observed outputs. Recognizing one XOR subnetwork does not distinguish a half-adder from a half-subtractor when their second outputs differ.

20. Shared logic is a single physical computation used by several outputs. Count its gates once, but count any required fan-out buffers and their delay under the specified library.

21. Minimum SOP means minimum under a declared two-level algebraic cost. It is not automatically minimum mapped area, transistor count, delay or total gate count in a different implementation space.

22. A construction supplies an upper cost bound. To claim a global minimum, provide a valid lower bound or complete search over the same allowed gate types, input polarities and fan-in restrictions.

23. Factoring PQ plus PR into P times Q plus R can reduce gate duplication. Verify all specified rows afterward and distinguish the factored network's depth from its literal count.

24. A common primary wire is not itself a shared gate. Physical savings arise when an actual internal operation is reused; several uses of A alone do not prove eliminated computation.

25. Multi-output optimization can prefer a shared term that independent output minimization would not select. The objective concerns the union of physical gates, not the sum of isolated cover costs.

26. A source allowed to drive at most two loads gains only one net leaf slot per added two-load buffer. Seven final loads therefore require at least five such buffers when logic duplication is forbidden.

27. An n-input associative operation can be built by a binary tree with n minus one gates. This count follows from tree structure and does not apply to arbitrary nonassociative operations.

28. A fan-in-two formula depending on all n independent inputs has depth at least the ceiling of log base two n. A balanced AND, OR or XOR tree attains this depth for simultaneous arrivals.

29. A chain's maximum depth is n minus one, but an input attached at its final gate traverses only one gate. Late-input delay must use actual connectivity rather than the longest depth assigned to another input.

30. A balanced tree is not always fastest when inputs arrive at different times. Compare latest output bounds using the maximum predecessor arrival plus gate delay at each vertex.

31. NAND and NOR are not associative. A cascade of NAND gates is not automatically a wide NAND; restore the intermediate polarity or derive the truth function explicitly.

32. Shannon expansion partitions by the selected variable: F equals NOT S times F restricted to S=0, plus S times F restricted to S=1. The two selector cases prove the identity exhaustively.

33. Mux data inputs are cofactors and may be functions of remaining variables. A truth-table lookup using only constants is one special construction rather than the only way to use a mux.

34. Equal cofactors mean that the output is independent of that selected variable. Removing the unnecessary selector preserves the function and may reduce implementation cost.

35. Complementary cofactors often expose XOR or XNOR structure. Determine their ordering before choosing the polarity; exchanging zero and one branches complements the relationship.

36. For a one-bit residual, output pairs 00,01,10,11 correspond respectively to zero, the residual variable, its complement, and one. The pair order must always be residual zero then residual one.

37. Swapping two mux select bits exchanges addresses 01 and 10. Leaving data wiring unchanged is valid only when the exchanged cofactors are identical functions on their full residual domains.

38. Count distinct shared residual inversions rather than one inversion per mux pin. Nevertheless, the mux component itself remains part of total cost when the objective includes it.

39. Choose select variables by the resulting data-function complexity and available sharing. The most significant input is not automatically the best selector merely because it is visually first in the table.

40. An active-high decoder produces exactly one selected minterm when enabled under a stable legal binary input. Enable conditions must be included before using the one-hot claim.

41. A shared decoder supports several output functions by combining different subsets of minterms. Sharing its row generation does not make the output functions equal or remove their separate combining logic.

42. An active-low decoder's selected output is zero. A NAND of selected active-low lines implements their active-high minterm union through De Morgan's law; an OR usually does not.

43. An n-address-bit, m-output-bit logical ROM stores m times 2^n bits. This is a capacity formula, not a proof of the smallest circuit that realizes that particular truth table.

44. A fixed asynchronous lookup behaves combinationally after access delay. A clocked-read memory interface retains sampled address or output state and must not be classified by the same present-address rule.

45. ROM outputs can glitch while the address changes because internal decoder paths do not settle simultaneously. Table correctness alone supplies no hazard-free waveform certificate.

46. SOP maps naturally to NAND–NAND when each first-stage product is complemented and the final NAND restores their OR. Keep the algebraic polarity of every intermediate net explicit.

47. POS maps naturally to NOR–NOR by the dual argument. Do not exchange NAND and NOR solely by drawing bubbles without also changing the AND/OR operation under De Morgan's law.

48. Complemented primary inputs are free only when the stated problem gives them. Otherwise count their generating inverters and include those paths in depth and delay analysis.

49. A tied-input NAND or NOR acts as an inverter. The tied pins do not make the component disappear, and a cost convention may still classify it by its physical fan-in.

50. Active-low input conversion changes the arguments of the function; active-low output conversion complements its result. Transform both sides of the interface contract separately.

51. Disabled active-low grants normally read as one when no request is asserted. Checking only the enabled case can conceal a polarity error that violates the disabled contract.

52. Bitwise complement flips every bit in the stated width. Logical negation returns a Boolean zero/nonzero test, and signed arithmetic negation represents an additive inverse; the three operations are not interchangeable.

53. Zero-extension preserves unsigned numerical value. Sign-extension preserves signed two's-complement value, while changing the unsigned interpretation of a negative extended pattern.

54. Signedness is part of a comparator specification. The same visible bit pattern can be a large unsigned number or a negative signed number and consequently yield a different less-than result.

55. Truncation keeps selected bits rather than necessarily preserving the mathematical value. Separate the low-word arithmetic result from carry and from signed overflow.

56. Unsigned carry reports a sum beyond the unsigned range. Signed overflow reports a signed result beyond its signed range; opposite-sign operands can produce carry without signed overflow.

57. Continuous HDL assignments describe concurrent connectivity. Their textual order does not insert a serial execution dependence between independent gates.

58. Gate primitives place the output pin first in the shown structural Verilog syntax. Prefer named ports for hierarchical modules to reduce accidental swaps between similarly sized signals.

59. A combinational procedural block must assign every output on every legal path. A default assignment followed by deliberate overrides is a useful way to make completeness visible.

60. A missing disabled branch can retain an earlier value and infer storage or trigger a diagnostic. An always_comb declaration states intent but does not mathematically supply an unspecified output value.

61. Blocking assignments provide explicit local evaluation order in a combinational procedural example. Avoid assuming that a source-line ordering of continuous assignments has the same semantics.

62. X in simulation is an unknown value, not a Boolean minimization don't-care. Zero AND X can resolve to zero, whereas one AND X remains unknown under four-state logic.

63. Z denotes a high-impedance driver state in a resolution model. It is not a freely selectable ordinary third Boolean value for the two-valued gates studied in this chapter.

64. Wildcard case constructs can hide unknown-input faults by matching too broadly. State legal-input assumptions and use complete ordinary cases where the contract requires deterministic outputs.

65. A multi-output equivalence miter ORs the XOR discrepancies of every corresponding output. A zero discrepancy for one familiar output does not certify the rest of the block.

66. Care equivalence checks care AND the miter. Every discrepancy row surviving that conjunction is a valid counterexample; eliminating one witness alone does not prove the remaining rows safe.

67. A small exhaustive table is a proof in the declared finite model. Random tests without a failure give evidence but not a universal equivalence certificate.

68. An independent reference should express the original requirement rather than repeat the candidate netlist. A shared transcription error can make two wrong implementations agree perfectly.

69. A stuck-at fault must first be activated by a correct opposite value. It must also propagate through nonmasking side inputs to an observed output; activation alone is insufficient.

70. An OR side input fixed at one masks a discrepancy on its other input. An AND side input fixed at zero has the dual masking effect; use noncontrolling values when constructing a detecting test.

71. Test-set minimization is a set-cover problem whose elements are fault obligations. An irredundant chosen cover need not be globally minimum, just as an irredundant prime cover need not minimize terms.

72. Propagation bounds use the maximum predecessor latest arrival plus the gate's upper delay. Contamination bounds use the minimum predecessor earliest change plus its lower delay; compute these independently.

73. A structural timing interval does not say that an output transition necessarily occurs. A controlling side value may suppress it entirely, so sensitization needs separate Boolean analysis.

74. A longest structural path may be a false path because correlated reconvergent inputs cannot satisfy all necessary side conditions simultaneously. Do not independently assign signals derived from the same primary input.

75. Stable functional constancy does not prove glitch freedom. A times NOT A is zero after settling but unequal direct and inverted path delays can temporarily change its physical output.

76. Functional equivalence, structural delay bounds, sensitizable transitions and hazard freedom are distinct claims. Each requires an argument under its own assumptions rather than one interchangeable truth-table check.

77. A transport-delay trace and an inertial-delay trace can differ for short pulses. State the delay convention before reporting a pulse width or claiming that a glitch is filtered.

78. Saturating and modular arithmetic are different contracts. A two-bit saturating increment sends three to three; modulo-four increment sends three to zero, producing different output equations.

79. Prove priority grants' mutual exclusion, service completeness and disabled suppression separately. Then prove the selected payload follows the grant; correct one-hot control alone does not guarantee correctly routed data.

80. Final review should reconnect the specification, equations, netlist, output convention, cost and verification witness. Finite checked models support the chapter's conclusions under stated assumptions and cannot guarantee every conceivable unseen examination answer.
