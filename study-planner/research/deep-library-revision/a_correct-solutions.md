# Correctness solution rewrite — working manuscript

This file is an unfinished answer manuscript. The university-source and original-examination audits remain in progress. It is not the new published chapter edition. Numbering refers to the existing 54-question bank.

### Solution 5

**Correct option: 2. Derive the set of all admitted initial states.** Let $u$ denote the initial x-value and $v$ the final one. The assignment establishes $v=u+3$. The requested postcondition is $v^2=25$, so the exact precondition is $(u+3)^2=25$. Factoring gives $(u-2)(u+8)=0$, and over the integers this is equivalent to $u=2$ or $u=-8$. The forward checks are $2\mapsto5\mapsto25$ after squaring and $-8\mapsto-5\mapsto25$.

Weakest means that every admitted initial state which achieves the postcondition is included, and no failing state is included. Option 4, initial x=2 alone, is sufficient but stronger: it excludes the valid state −8. Option 1 lists final x-values rather than their preimages. Initial 5 produces final 8, whose square is 64; initial −5 produces final −2, whose square is 4. Option 3 reverses the shift: initial 8 produces 11, and initial −2 produces 1, so neither achieves square 25.

The assignment rule substitutes the old expression into the desired final predicate. It does not assert that the final value was already true before execution. This derivation assumes exact integer addition and squaring; a machine-overflow model would require separately defined expression semantics and safety. Here the necessary-and-sufficient initial-state set is established algebraically, while the two forward traces verify its particular witnesses.

### Solution 6

**Correct option: 1. Reverse the statements' order when propagating requirements.** Label initial values $x_0,y_0$. The first command produces $x_1=x_0+1$. The second overwrites y with $y_1=2x_1$. The last overwrites x with $x_2=y_1-3$. Therefore the entire sequence satisfies $x_2=2(x_0+1)-3=2x_0-1$. Final x=7 requires $2x_0-1=7$, giving $x_0=4$. The initial y-value is unconstrained because it is overwritten before any use relevant to the result.

Backward substitution obtains the same result in three proof steps. The last statement requires y−3=7, hence y=10 immediately before it. The middle statement requires 2x=10 immediately before that statement. The first then requires $2(x+1)=10$ in the original state. Substituting in forward order would mix these different checkpoints rather than implement the sequencing rule.

For initial x=4, the state trace is x=5, then y=10, then x=7. Option 2's x=5 produces final x=9, so it is false. Option 3 constrains initial y=10 but permits, for instance, initial x=0, which yields final −1; the overwritten initial y cannot ensure the target. Option 4 confuses the intermediate y=10 with initial x: initial x=10 returns 19. Since the equation has one integer solution and initial y is irrelevant, x=4 is the weakest condition, not merely a sufficient example. Expression evaluation and arithmetic are exact under the question's model.

### Solution 7

**Correct option: 3. Keep an explicit old-state snapshot.** Simultaneous assignment evaluates both right-hand expressions before changing either coordinate. With old $(x_0,y_0)=(5,8)$, it computes $x_1=y_0=8$ and $y_1=x_0+y_0=13$, so the result is $(8,13)$.

Sequential execution instead completes the first assignment before evaluating the second expression. After `x=y`, the state is $(8,8)$. The next command `y=x+y` now uses x=8 and y=8, giving $(8,16)$. Both programs terminate safely in this exact integer example; their disagreement is a functional-semantic difference, not a termination failure.

Option 1 treats the second sequential right-hand side as if it could still read the overwritten 5. Option 2 swaps the two assignment semantics. Option 4 leaves the first simultaneous coordinate at 5 even though its right-hand expression is old y=8. The needed repair for sequential code is a saved old x-value: store `old_x=x`, execute `x=y`, then `y=old_x+y`. That realizes the same state transformer as simultaneous assignment, provided old y has not also been overwritten prematurely.

In a general state, the two transformers are $(x,y)\mapsto(y,x+y)$ and $(x,y)\mapsto(y,2y)$. They agree exactly when old x equals old y, so agreement on such a test input would conceal the semantic difference. The concrete unequal input makes the lost dependence visible. A proof should name which expressions use old values and which use the updated state; unindexed variable names alone can hide an incorrect substitution.

### Solution 8

**Correct option: 4. Combine the guarded preimages of the postcondition.** In the true branch, old x<0 and the new value is −x. To obtain new x at least 3 requires $-x\ge3$, equivalent to $x\le-3$. This already implies the true-branch guard. In the false branch, old x is nonnegative and the new value is x+2. Its requirement $x+2\ge3$ reduces to $x\ge1$, which already implies the false-branch guard.

The complete weakest condition is the union of these admitted branch-specific regions: $x\le-3$ or $x\ge1$. Equivalently, the conditional rule requires both implications, from x<0 to −x≥3 and from x≥0 to x+2≥3. Every integer satisfying the union follows its appropriate branch and achieves the target. The excluded integers −2, −1 and 0 produce final values 2, 1 and 2, respectively, so no excluded state can be added while preserving correctness.

Option 1, x nonzero, admits −1 and −2 and is therefore insufficient. Option 2 includes only the nonnegative successful branch and unnecessarily excludes −3. Option 3 includes only the negative successful branch and unnecessarily excludes 1. These last two are individually sufficient but not weakest. Values −3 and 1 both produce final 3 and confirm that the boundary inequalities are inclusive. This is exact integer reasoning. In a finite signed type, negating the minimum value would additionally require a safety premise, even though it satisfies the abstract negative-branch inequality.

### Solution 9

**Correct option: 2. Restrict assumptions and relax conclusions in the sound directions.** The consequence rule takes a known triple $\{P\}C\{Q\}$ and justifies $\{P'\}C\{Q'\}$ when $P'\Rightarrow P$ and $Q\Rightarrow Q'$. Here initial x≥2 implies initial x≥0. The established postcondition r=x² implies r≥0 over exact integers regardless of the final x-value. Therefore the option's stronger precondition and weaker postcondition are both justified.

Option 1 expands the admitted initial domain to include negative x-values. The old contract makes no guarantee there. A program returning a correct square on nonnegative inputs and an arbitrary value on negative ones would satisfy the known triple while violating the proposed stronger claim. Option 4 similarly replaces the admitted domain by x<0, which does not imply the known precondition.

Option 3 demands r>x, which does not follow from r=x² in general: final x=0 gives r=0 and final x=1 gives r=1, so strict inequality fails. Even if some particular implementation avoids those final states, consequence alone cannot infer that additional fact from the stated postcondition. No runtime or termination assertion is added by this logical rule; it transforms the functional triple under its original interpretation.

The word always is decisive. One is not allowed to inspect an unspecified implementation and invent stronger guarantees. The two implication obligations are sufficient for every command satisfying the original triple. A changed domain or a stronger result may be true for a special command, but it needs another proof rather than this consequence application.

### Solution 10

**Correct option: 3. Treat array writes as updates to one shared map.** The first write establishes A[i]=1. The second writes 2 at index j. If i and j differ, the second update leaves A[i] unchanged and establishes A[j]=2, satisfying both final equalities. If i=j, the second write overwrites the very cell just set to 1, leaving its final value 2. The simultaneous final requirements A[i]=1 and A[j]=2 then demand one integer cell equal two distinct constants, which is impossible.

Thus inequality of the indices is both necessary and sufficient under the already stated valid-index premise. Option 1, i<j, is sufficient but excludes valid states with i>j. Option 2 is similarly sufficient but excludes valid states with i<j. Option 4 admits i=j and fails. This explains why the weakest condition is inequality rather than an ordering of positions.

Formally, the final array $A_2$ is the update of $A_1$ at j, and $A_2[i]$ equals 2 if i=j and equals $A_1[i]=1$ otherwise. This piecewise evaluation is the array-assignment analogue of backward substitution. Initial array values are irrelevant because the two required cells are overwritten, but the shared identity of a cell remains relevant. Validity only ensures the accesses are defined; it does not establish that they refer to different locations. For object references or memory pointers, the corresponding proof obligation is nonaliasing of the modified locations, which must be justified separately from address validity.

### Solution 11

**Correct option: 2. Separate inductiveness from sufficient strength.** At the initial state (0,0), x≥0 holds. In any state satisfying x≥0, the simultaneous transition produces $x'=x+1\ge1$, so it preserves the predicate. This preservation reasoning quantifies over every state allowed by the predicate, regardless of y. Consequently x≥0 is inductive for the specified transition.

However, x≥0 alone does not imply x=y. The state (1,0) satisfies it and violates equality. Even if that state is unreachable from the specific initial pair, it is admitted by the chosen annotation, so the annotation cannot establish the desired postcondition by a simple exit implication. The actual reachable states are $(k,k)$ for nonnegative integer k. Their equality needs the additional invariant x=y, which holds initially and is preserved because both coordinates increase by the same amount.

The conjunction $x=y\land x\ge0$ therefore describes the required relation and the useful bound. Options 1 and 3 incorrectly assert that the weak predicate suffices. Options 3 and 4 incorrectly deny preservation, since adding one cannot make a nonnegative integer negative. The old question title mentioning failure at an unreachable state is misleading for this particular predicate; the replacement title will distinguish an inductive but insufficient invariant.

No loop guard or stopping condition is specified in the state-machine question. Equality is established at every reachable checkpoint, but the invariant alone cannot prove that a final checkpoint is eventually reached. Correctness of a relation, sufficiency for a postcondition and termination are distinct obligations.

### Solution 12

**Correct option: 2. Reachable-state truth is weaker than inductiveness.** Starting from zero, the transition returns zero. Every subsequent reachable state is therefore zero, so x≥0 is true at every reachable checkpoint. This conclusion follows by induction on the number of transitions: the base is zero and the only reachable successor is again zero.

To test whether the predicate is inductive, however, consider all states satisfying it, not only reachable ones. The positive state x=1 satisfies x≥0 and is mapped to −1, which violates it. Hence the predicate is not preserved on its full annotated domain. The transition on negative inputs is irrelevant to this counterexample because both the initial counterexample state and the reachable states lie in the explicitly defined nonnegative part of the transition system.

Option 1 is false because no negative state is reachable from zero. Option 3 is false twice: initialization is true and preservation is false. Option 4 confuses an invariant assertion with a reachability characterization; this machine actually reaches only zero, not every integer. A stronger invariant x=0 excludes the positive spurious states, is true initially and is preserved by the transition. It therefore supplies an inductive proof of the reachable-state property.

The example shows why a verification-condition failure does not always exhibit a bad actual execution. Its x=1 counterexample refutes the proposed preservation condition but is not reachable from the stipulated initial state. Strengthening the annotation can eliminate that proof failure without changing the command. In contrast, a reachable counterexample would refute the claimed execution property itself.

### Solution 13

**Correct option: 3. Identify the failed proof obligation before judging the code.** The loop guard is the Boolean constant False, so the body never executes. The program behaves as skip: it terminates immediately and leaves the state unchanged. Under initial assertion True and final assertion True, the actual command is correct for every state.

The chosen invariant False nevertheless fails initialization. That verification condition is $\text{True}\Rightarrow\text{False}$, which is invalid in every state. Preservation is vacuously valid because its premise contains the conjunction of invariant False and guard False. The exit implication is also vacuous because its premise contains invariant False. Two vacuous obligations cannot compensate for the failed initialization condition.

Choose invariant True instead. Initialization becomes True⇒True. Preservation still has an impossible true-guard premise, and exit reduces to True⇒True. There is no body transition needing a decreasing variant; the fixed false guard directly proves termination. This repaired annotation proves the same unchanged program.

Option 1 incorrectly predicts divergence despite the never-entered guard. Option 2 contradicts the stipulated tautological final assertion. Option 4 treats an annotation as an arbitrary magic proof rather than a predicate that must satisfy concrete obligations. The correct diagnosis is a failed annotation, not a counterexample execution. This distinction matters in larger proofs: a noninductive or initially false predicate can cause verification to fail even when a different, more suitable predicate would establish the command's real contract. One must inspect initialization, preservation and exit separately before concluding that the implementation is wrong.

### Solution 14

**Correct option: 2. Derive the complete state formula.** After k executed bodies, the value is $x_k=\max(0,n-3k)$. The base k=0 gives the initialized n. If the current positive value is n−3k, the next body subtracts three and clamps at zero, giving precisely $\max(0,n-3(k+1))$. Once zero is reached the guard is false, so no further body occurs.

The stopping index is the least integer k with $n-3k\le0$, namely $\lceil n/3\rceil$. Write n=3q+r with r in {0,1,2}. If r=0, q bodies reach zero exactly. If r=1 or 2, q bodies leave that positive remainder and one additional body clamps it to zero. Thus the exact count is q for r=0 and q+1 otherwise.

Option 1 omits that final partial subtraction when n is not divisible by three. Option 3 counts one decrement per body instead of up to three and fails at n=3, where there is one body. Option 4 fails at n=1, predicting zero even though the initial guard is true and one body is required. The question counts body executions; the final false guard adds one more guard evaluation in a straightforward while implementation. The positive-n premise excludes zero, though extending the same code to n=0 would correctly yield zero bodies. The state formula explains exact work, while nonnegative integer descent independently certifies termination.

### Solution 15

**Correct option: 3. The arithmetic domain changes the termination argument.** In exact real arithmetic, after k bodies the value is $x_k=2^{-k}$. This is strictly positive for every finite integer k. The guard x>0 therefore remains true after every finite number of bodies, and the loop never terminates.

At the same time the sequence is strictly decreasing and nonnegative. The problem is not failure of those properties; it is failure of well-foundedness of the proposed order on nonnegative reals. Infinite strictly descending real chains exist. Convergence to zero as k tends to infinity is a limiting statement, not attainment of zero at a finite program step.

Option 1 predicts a zero after one body, but the first result is one-half. Option 2 applies a rule valid for a nonnegative integer measure decreasing by at least one to a real measure with ever smaller drops. Option 4 denies the genuine nonnegativity property; every finite state is positive. The correct answer identifies precisely which termination hypothesis is missing.

A finite floating-point implementation can eventually underflow or round to zero under some formats and modes. Integer division would also behave differently, giving zero from integer one divided by two. Neither observation answers the exact-real question. A valid general repair is to use a guard x>epsilon for a fixed positive threshold, or to specify a well-founded discrete progress measure tied to an appropriate finite stopping condition. Merely relabeling the unchanged real x-value as a variant does not establish the missing finite descent property.

### Solution 16

**Correct option: 1. Quantifier order distinguishes two different bounds.** The first step lowers the first coordinate from one to zero and may raise the second from zero to any chosen finite B. This is a strict lexicographic decrease because the first coordinate decreased. With first coordinate now fixed at zero, subsequent decrements strictly lower the nonnegative integer second coordinate until it reaches zero. Each execution therefore has one reset step followed by finitely many decrements.

If decrementing means subtracting one each time, its exact length is B+1 transitions, including the reset. For every proposed finite uniform bound K depending only on the initial pair (1,0), choose finite B>K. The resulting admitted execution exceeds K. Thus every execution has a finite length, but no single finite K bounds all executions from that initial state. Formally, for every chosen finite B there exists a finite run length; one cannot interchange that with existence of a uniform bound for all B.

Option 2 incorrectly turns an arbitrarily large finite B into an infinite integer value. No permitted reset chooses infinity. Option 3 ignores the subsequent B decrements and fails already at B=1. Option 4 denies lexicographic decrease because it inspects only the increasing second component; lexicographic order first compares the first component.

A potential x+y is not monotonically decreasing at the reset and cannot supply the asserted initial-sum bound. A uniform bound could be restored by a specified upper bound on allowed B, which would yield that bound plus one transitions. The stated well-founded lexicographic proof establishes termination without inventing such an additional restriction.
