## Complete summary and examination decision rules

### Conceptual summary

Control flow selects the next execution location, and state records the values at that location. C statement grammar determines ownership of branches and loop bodies; indentation does not. A condition can change state and then select a path, so its value and its side effects must both appear in a trace. A priority chain chooses the first matching branch, whereas separate conditions can execute sequentially against changing values.

A switch evaluates one controlling expression and dispatches once to an entry label. Labels do not impose independent guards on later statements. Fallthrough continues until a transfer or the end of the switch. Break targets the nearest enclosing switch or loop; continue targets the nearest loop and reaches different checkpoints for while, do-while, and for. Normal loop exit, break exit, and function return do not establish the same postconditions.

For a correct loop, explain what its state means at a named checkpoint. Establish the invariant initially, prove it is restored on every returning path, and combine it with each exit condition. Prove termination separately using a well-founded measure and safe arithmetic. Exact counting formulas assume the path and progression actually described by the program. Machine integers, rounding, input behavior, and optimizer permissions can invalidate a casual mathematical termination claim.

### An eight-step solving procedure

1. **Fix the contract.** Identify the language/version, type ranges, initial state, allowed input domain, and any rounding or modular model.
2. **Parse the ownership.** Mark blocks, null statements, the matching if for every else, and each label's associated statement.
3. **Mark transfer targets.** Give every break, continue, return, and goto its actual destination in the nesting tree.
4. **Screen validity.** Check required constant expressions, scope, initialization on every read path, unsequenced effects, and arithmetic boundaries before predicting output.
5. **Choose checkpoints.** Record guard input, guard output when state changes, body entry, update, and final exit separately when needed.
6. **Derive the progression.** Determine which statements run on ordinary, continued, and broken paths. Count a specified operation, not an unnamed “iteration.”
7. **Prove the result.** State a meaningful invariant, establish preservation and all exit postconditions, and justify termination or its failure under the contract.
8. **Challenge boundaries.** Recheck empty input, one entry, first and last reachable break, equality at a threshold, extremal representable values, and unusual entry edges.

### Sixty high-yield rules with reasons and traps

#### Statement grammar and state

1. A semicolon can be a complete null statement. Locate it before assuming that the following visible block belongs to a condition.
2. An expression statement discards its computed value but retains side effects. `x + 1;` and `++x;` therefore have different effects on state.
3. A block occupies one statement position. Braces are the reliable way to control several statements with one if or loop.
4. A physical source line is not an execution unit. Trace complete expressions and control checkpoints even when several share one line.
5. Scope identifies an object; it does not prove that its initializer executed. Switch dispatch and goto can bypass initialization.
6. A body-local automatic variable with an initializer starts fresh on each entry. Move its declaration outside the loop when its state must persist.
7. A header declaration can hide an outer variable. The outer object can remain unchanged even though the same name appears in a loop.
8. An undefined execution has no required numerical output. Stop the output trace at the violated semantic condition.

#### Conditions and branch chains

9. A negative arithmetic scalar is true in a C condition when it is nonzero. Do not equate true with “positive.”
10. An assignment inside a condition can be valid C and can select the true branch. Check the operator token before reading a guard as equality.
11. Chained mathematical inequalities require explicit conjunction in C. Two relational operators do not create a range test.
12. Each independent if evaluates in the state left by earlier statements. Recompute later guards after earlier assignments.
13. An else-if chain stops at its first true guard. Put overlapping thresholds in the priority required by the specification.
14. The final else denotes the residual case under previous falsities and the input domain. It does not automatically mean mathematical equality for floating values with NaNs.
15. Every interval boundary must have a deliberate owner. Test both equality and neighboring allowed values at each threshold.
16. The else binds to the nearest unmatched if allowed by grammar. Visual alignment cannot override this rule.
17. Short-circuit conjunction can protect a right operand only after its left guard has safely evaluated. A dangerous left operand is already too early.
18. Bitwise operators do not replace logical short-circuit operators when safety or sequencing depends on skipping work.
19. Conditional-expression type formation can convert the chosen value using the types of both alternatives. Branch selection does not prevent all conversion effects.
20. Boolean algebra preserves truth for pure operands, not automatically the behavior of stateful code. Count and order evaluated operations when rewriting guards.

#### Switch dispatch

21. A C17 switch needs an integer controlling expression. A floating controlling expression is a constraint problem, not a different kind of switch trace.
22. Case values are compared after conversion to the promoted controlling type. Textually different cases can become forbidden duplicates.
23. An ordinary const-qualified object is not automatically an integer constant expression in C17. Enumeration constants provide a different mechanism.
24. A switch chooses one entry point and then executes sequentially. Do not retest the control value at every later case.
25. Default handles the absence of a matching case, wherever its label is placed. Its position still affects later fallthrough.
26. A switch without a match or default skips its body entirely. Result variables need an established value on that path if subsequently read.
27. A break inside a switch nested in a loop usually exits only that switch. Draw the smallest enclosing eligible construct.
28. A continue inside a switch targets an enclosing loop. It can skip code following the switch within the same body.
29. A case-local declaration should be placed in a block after the label for the C17 syntax used here. Do not rely on extensions from a different language version.
30. A declaration before the first case may have its initializer skipped. A visible initializer is not a path-independent assignment.

#### Loop ordering and transfers

31. An ordinarily entered while-loop can have zero body entries. Its guard is evaluated before the first body.
32. An ordinarily entered do-loop has an initial body entry. Break or return can still prevent that entry from reaching its trailing test.
33. A for-loop initializes once under ordinary entry. Its repeated order is guard, body, update, then guard again.
34. Continue in a for-loop reaches the header update. Moving that update to the bottom of a while body can change the behavior.
35. Continue in a while-loop reaches its guard. Manual updates below the continue are skipped and can cause a repeated state.
36. Continue in a do-loop reaches the trailing guard. The posttest syntax supplies a test, not an implicit index update.
37. Break skips the remaining body and the update of a departed for-loop. Count completed updates separately from body entries.
38. Break affects the nearest loop or switch, not an enclosing if. An if is a selection node without a break destination.
39. An inner-loop break leaves the outer body active. Statements after the inner loop still run unless another transfer intervenes.
40. Return leaves the current function invocation. It is stronger than break and can bypass all surrounding loops in that invocation.
41. An omitted for-guard is nonzero. Such a loop needs another exit or deliberately continues indefinitely under its contract.
42. A false guard can still have side effects. Include the terminating evaluation when predicting the final state.
43. Postfix tests compare the old value and then update. Prefix tests update first; body-entry values and counts can differ.
44. A comma expression's result is its right operand's value. A left comparison in a comma guard does not restrict iteration by itself.
45. A goto can bypass ordinary loop entry. Standard zero-entry and one-time-initialization statements need their entry assumptions stated.

#### Proofs, counts, and safety

46. An invariant needs a checkpoint and a precise relationship. “The answer is correct” does not identify what processed work it describes.
47. Invariants need not hold between every pair of body statements. They must be restored before all edges returning to their declared checkpoint.
48. A continue path needs both invariant preservation and progress. Restoring only on the bottom path leaves a proof gap.
49. A break path needs its own exit argument. The negation of the loop guard is not established merely because a break ended the loop.
50. Partial correctness and termination are separate obligations. A preserved relationship can coexist with an endless cycle.
51. A decreasing nonnegative integer variant proves finite repetition only when each body execution returns. An infinite inner loop invalidates that premise.
52. Exact progression counts assume the body leaves the index progression intact. Early exits, side effects, wraparound, and rounding must be analyzed first.
53. A normal pretest exit gives one more guard evaluation than body entries. A break can remove that final false guard.
54. A posttest loop normally has equal body-entry and test counts. A break before the trailing test creates a different count.
55. Unsigned reverse loops cannot end through an always-true comparison with zero. Check the intended processed values before choosing a repair.
56. Signed overflow is undefined rather than mandated wraparound. The final update can be unsafe even after every useful body operation completed safely.
57. Modular equality reachability is governed by a greatest-common-divisor condition. A nonzero step does not guarantee every target is visited.
58. Floating updates can stagnate or miss equality endpoints. A real-number increase is not automatically a stored-value increase.
59. Input-driven termination requires an environmental assumption or a bounded failure policy. Loop syntax cannot guarantee that a user supplies a valid response.
60. A finite collection of successful traces is evidence for those traces, not a universal proof. Combine boundary checks with invariants, safety arguments, and a declared coverage boundary.

### Boundary review table

| Situation | Required decision |
|---|---|
| Empty input interval | Decide whether zero attempts or one initial attempt is intended. |
| Final failed guard mutates index | Record its side effects in the post-loop state. |
| First entry breaks | Count one body entry, zero prior updates, and only the evaluated guards. |
| Continue occurs before manual update | Follow the actual continuation edge and test whether state changes. |
| Switch appears inside a loop | Give break and continue different target analyses. |
| Mathematical proof uses products | Check whether code computes those products or uses only safe incremental updates. |
| Counter can reach a type extremum | Audit the subsequent update before calling the progression defined. |
| Guard depends on external input | Separate source correctness from assumptions about future input. |

## References and chapter review boundary

The chapter is an original synthesis with independently developed explanations, proofs, diagrams, laboratory, and solutions. Course material is used selectively with attribution; entire lecture bodies and exercise inventories are not redistributed.

1. **Harvard University.** David J. Malan. *CS50x 2025, Lecture 1.* Written lecture notes: Conditionals, compare.c, agree.c, Loops and meow.c, input validation, and Mario. [Official notes](https://cs50.harvard.edu/x/2025/notes/1/).
2. **Massachusetts Institute of Technology.** Ana Bell, Eric Grimson, John Guttag. *6.0001 Introduction to Computer Science and Programming in Python, Fall 2016. Lecture 2: Branching, Iteration.* Slides, pages 7–23, including the range and break examples. [Official slides](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/ba2947b25b1580e4a84df0ec5dbe5cdd_MIT6_0001F16_Lec2.pdf); [offering and instructor metadata](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_lec2/).
3. **Princeton University.** Robert Sedgewick and Kevin Wayne. *Introduction to Programming in Java, §1.3: Conditionals and Loops*, the COS126 resource family. [Official section and exercises](https://introcs.cs.princeton.edu/java/13flow/). Language-specific assumptions are kept separate from C17.
4. **Cornell University.** CS2110 course teaching staff. *Spring 2026, Lecture 4: Loop Invariants.* Loop anatomy, diagram conventions, invariant construction, and exercise families. [Official written lecture](https://courses.cis.cornell.edu/courses/cs2110/2026sp/lectures/lec04/). No unverified individual authorship is assigned.
5. **University of Cambridge.** Neel Krishnaswami, with source-note credits to Anil Madhavapeddy, Alan Mycroft, Alastair Beresford, and Andrew Moore. *Programming in C, Michaelmas 2017–18, Lecture 1: Types, Variables, Expressions and Statements.* Pages 14–18 and 20–23. [Official slides](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture1.pdf); [official offering](https://www.cl.cam.ac.uk/teaching/1718/ProgC/).
6. **ISO/IEC JTC1/SC22/WG14.** *N1570, Committee Draft, 12 April 2011.* §§6.8–6.8.6 for statements and jumps; §§6.5, 6.5.13–6.5.17 for expressions and sequencing; §6.3 for conversions; §6.6 for constant expressions. [Public committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).

**Review boundary.** Five substantive course bodies were read in the stated scope. The chapter covers scalar statement sequencing, selection, dispatch, loop order, abrupt transfers, checkpoint invariants, exact basic counts, and termination boundaries. Functions, arrays, pointer lifetime, full input parsing, concurrent loops, complete numerical methods, and arbitrary-program verification require their own chapters. Course exercise patterns within scope are curated, not exhaustive. The numerical and state models can be checked exhaustively over specified finite domains; those checks do not certify all possible programs or future exam questions. C snippets were specification-reviewed and model-checked where documented, but were not compiled in this environment. No literal 100% correctness, global course completeness, or guaranteed performance on unseen examinations is asserted.

**Status:** Approved English chapter. The student explicitly approved promotion and continuation on 2026-10-02.
