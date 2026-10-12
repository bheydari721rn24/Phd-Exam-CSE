## Detailed decisions at the end of the chapter

The fifteen foundational notes remain above. These twenty additional rules connect the mathematical methods to precise execution paths and their boundaries.

**16. Count the requested event.** In the original triple loop, there are680 accumulator writes,815 header updates and951 guard evaluations. Each number is correct for a different event. Specify whether the question asks for entries, completed useful work, updates, tests, total calls or active frames before selecting a formula.

**17. Convert weak inequalities by a bijection.** The transformation $(i,j,k)\mapsto(i,j+1,k+2)$ takes weakly ordered indices through15 to distinct indices through17, proving $\binom{17}{3}$. Strict combination $\binom{15}{3}$ omits equality cases. Add the accumulator's initial value separately.

**18. A failed guard can still update state.** Postfix `x++<3` compares old three on its fourth test but leaves stored four, while its body ran only three times. A skipped short-circuit right operand has no side effect. These are different reasons why guard count and update count can differ.

**19. Give an invariant a checkpoint.** In add-before-increment, $s=i(i-1)/2$ holds before the guard and after the complete body, not between the addition and index update. A continue inserted before restoration can break that proof. A general assertion that the sum is correct does not identify its processed interval.

**20. Do not confuse a ranking with the output.** The odd-subtract/even-halve process decreases n at every step, although population count can stay unchanged during halving. For $n>0$, its exact transition count is $\lfloor\log_2n\rfloor+\operatorname{popcount}(n)$; at zero the guard fails and the count is zero, without evaluating a logarithm of zero. An increasing accumulator can coexist with a decreasing separate ranking.

**21. Check every continuation edge.** In a for-loop, continue reaches the header update; in a while-loop, it reaches the guard. Moving the update below continue can leave the index unchanged at the first skipped value. An equivalence proof must preserve these edges, variable scope and inner-loop targets.

**22. A break is not a normal false guard.** Q44 at break8 has eight entries, seven header updates and no final false guard. Its exit index stays eight. A postcondition derived from the negation of the loop guard does not apply to this exit without a separate argument.

**23. Test overlap before claiming priority changes output.** The original continue-at-multiples3 and break-at8 predicates cannot both hold at the terminating index. Reordering those pure tests leaves $(19,8)$ unchanged. Break9 creates overlap and distinguishes $(37,11)$ from $(27,9)$. Side-effectful predicates need an additional evaluation-order analysis.

**24. Switch labels select an entry, not independent branches.** Control value2 enters case2 and can then execute case3 before a break. Changing the control variable inside the body does not redispatch. A default label in the middle can also fall through later statements; give the chosen entry and every actual transfer in the trace.

**25. Name the nearest transfer target.** An inner-loop break leaves the outer body active. A switch nested inside a loop intercepts a break, while continue targets the enclosing loop. An if adds no break target. Replacing break with return can leave the function and produce a different total.

**26. Preserve source and destination strides independently.** The original recursive-copy options all decrement source by two; their destination positions are t, t+1,2t,2t+1. Only the first writes the required dense prefix from zero. A one-element trial can fail to distinguish destination-stride errors; test two or more writes and prove the index invariant.

**27. A length is not a last index.** Initial source index10 admits six sources10,8,6,4,2,0 and one additional returning call. A length10 instead starts at nine and admits five copies. Include zero endpoints, negative guards and destination capacity before applying a ceiling formula.

**28. Total recursion work is not current stack occupancy.** Two children per non-base call give $2^{n+1}-1$ total invocations, including leaves, but an ordinary sequential active path has at most n+1 frames. A compiler's tail-call optimization or a parallel implementation needs its own resource model.

**29. One recursive child does not imply linear work.** Local toll k along arguments n through one sums to $n(n+1)/2$. Tail position may reduce retained frames without erasing that toll. Count local body operations separately from the n+1 invocations.

**30. Every intermediate and last update needs range.** A valid last useful body index is insufficient when the header increments afterward. A powers-of-two loop can emit $2^{30}$ then overflow its signed32 update. The filtered loop needs $3n+1$ to fit. An arithmetic swap can overflow its first sum even when the swapped final values fit.

**31. Distinguish first threshold crossing from feasible-budget prefix.** After k positive additions, $S_k=k(k+1)/2$ increases strictly. Reaching threshold H uses $S_k\ge H$ with preceding failure, whereas maximal budget prefix m uses $S_m\le B<S_{m+1}$. Check which side owns equality and whether the test runs before or after the addition.

**32. A modular target needs a gcd test and a first-hit calculation.** Step six modulo256 reaches only even residues. Target64 first occurs at96 updates; target zero has first positive return128 but already occurs at update zero. Period and hitting time are different quantities.

**33. A signed terminal value can disappear after a type change.** Starting from a representable signed $n\ge0$, the do-decrement loop ends at negative one after n+1 entries. A negative starting value needs a separate one-entry analysis, and decrementing the signed minimum is undefined. An unsigned object never becomes negative; its nonnegative guard cannot fail through that route. Preserve the desired processed positions when designing a safe unsigned reverse traversal.

**34. Course-language and numerical hypotheses are part of the proof.** Python range supplies iterator values even if the body rebinds its target name. C updates an object through its header expression; Java signed overflow differs from C17. Newton's first step can increase root-distance, and NaNs invalidate an ordered argmin without a policy. Do not export informal course statements beyond their domains.

**35. Separate proof, finite corroboration and resources.** Exact traces check their stated inputs; invariants and well-founded variants justify a wider declared domain. Mathematical termination does not guarantee available stack memory or eventual valid external input. No diagram or finite test set proves anticipation of every unseen examination question.

### Closing synthesis in complete statements

Control flow determines the next location, and data state determines what that location reads. Parse statement ownership and labels, identify every transfer target, and establish initialization, sequencing and arithmetic safety before predicting output. Record guard input and guard output separately when the guard changes state. An invariant describes processed work at a named checkpoint; a ranking establishes progress on every edge returning to that checkpoint. Count the requested event from the resulting domain or recurrence. Source language, representation, rounding, ordinary-entry assumptions and environmental conditions remain explicit. The full lesson and its proofs provide the instruction; these final decisions support retrieval and application.
