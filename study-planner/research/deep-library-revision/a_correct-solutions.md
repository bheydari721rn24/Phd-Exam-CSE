# Correctness solution rewrite — complete answer manuscript

All 54 answer drafts are present. This is an answer manuscript, not a completed chapter audit: deeper instruction, final rules, subject-specific models and rendered checks still need integration and verification.

### Solution 1

**Correct option: 4. Prove the recursive contract and the joining order.** Assume distinct input values in a total order. The base inputs of size at most one are already descending. For a larger input, the pivot m separates a greater-value block R and a smaller-value block L. Strong induction gives descending outputs from both smaller recursive calls. Every value returned from R exceeds m, and every value returned from L is below m. Consequently, joining R's output, then m, then L's output establishes descending order both inside the blocks and across their boundaries.

With values {1,2,3,4,5} and pivot 3, the greater block returns [5,4] and the smaller block returns [2,1]. The joining operation produces [5,4,3,2,1]. The alternative claiming an ascending suffix changes one recursive contract without any corresponding change in the code. The random-order alternative ignores both comparisons. An ascending output would require joining the smaller block before the pivot before the greater block.

For the stronger claim that the output is a permutation, use a median that is an actual input order statistic, choosing an input middle value for even lengths. Strict partitioning then retains every nonpivot value exactly once and the singleton pivot retains the remaining value. An arithmetic-average median for an even input can insert a new value and violate conservation, even though joining order remains descending. Equal input keys would likewise require an explicit equality block to retain all copies. The source asks about distinct-key order; state extra premises when proving a stronger contract. Input sizes strictly decrease above the base region, proving recursive termination.

### Solution 2

**Correct option: 1. Relate each recursive call to a copied prefix.** At the kth active call, let k start at zero. The intended parameter relation is $n=N-1-2k$ and i=k. The previously copied output prefix then satisfies $b[t]=a[N-1-2t]$ for $0\le t<k$. If n≥0, writing b[i]=a[n] adds exactly the next required source entry at the next contiguous destination position. Calling store(n−2,i+1) restores the same relation with k increased by one.

For N=6, the write pairs are (source,destination)=(5,0),(3,1),(1,2). The next call has n=−1 and returns before reading. This constructs [a[5],a[3],a[1]], exactly every other element from the end in reverse stride. For N=5, the sources are 4,2,0; for N=0, the initial n=−1 immediately returns. The destination must have room for $\lceil N/2\rceil$ elements, and the arrays' intended separation must avoid overwriting unread source data.

Option 2 writes to b[i+1], leaving index zero unwritten and shifting the compact result. Option 3 advances i by two, leaving gaps. Option 4 combines both defects. The negative source guard must precede the read because −1 or −2 can occur in the base call, depending on parity. A natural measure counting remaining stride positions decreases at each active call, so exactly ceiling(N/2) writes occur and one additional base call terminates the recursion. A proof of output order must track both source and destination; decreasing only the source index does not establish compact storage.

### Solution 3

**Correct option: 2. Distribute a unit of mass and allow missing children.** Give the root mass 1. At each possible child edge, transfer half the parent's mass. A leaf at depth d then receives exactly $2^{-d}$. When both children exist, their two budgets sum to the parent's budget. When only one exists, half the budget is left unused. Leaves terminate their own budget without duplication. Therefore the total leaf mass cannot exceed the root's mass 1.

A structural induction makes the inequality precise for finite trees. A root leaf has mass 1. With two subtrees, each subtree's relative leaf mass is at most 1 by induction; scaling each by 1/2 gives a total at most 1. With one subtree, scaling its mass by 1/2 gives at most 1/2. This proves the bound, including all finite shapes, and does not assume that the tree is balanced or complete by levels.

Equality holds in a finite full binary tree, where every internal node has two children, including the single root leaf. A root with one leaf child has total mass 1/2. These witnesses refute both the always-equal and always-strict alternatives. A total greater than 1 contradicts the proved allocation bound. In a finite tree, a missing child at any internal node produces a positive deficit, so equality characterizes fullness. The simple conservation proof supplies a useful upper bound even when the actual leaf depths and tree balance are unknown; extra structural claims must follow from the equality premises rather than from intuition about tree size.

### Solution 4

**Correct option: 2. Count dependent iterations and then add initialization.** One increment occurs for each weakly ordered triple $1\le i\le j\le k\le15$. The map $(i,j,k)\mapsto(i,j+1,k+2)$ is a bijection to strictly increasing triples chosen from {1,…,17}. Its inverse subtracts one from the second coordinate and two from the third. Thus the number of increments is $\binom{17}{3}=17\cdot16\cdot15/6=680$. Cod starts at 10, so it ends at 690.

An independent count fixes j. There are j choices for i and 16−j choices for k. Summing gives $\sum_{j=1}^{15}j(16-j)=16\sum_{j=1}^{15}j-\sum_{j=1}^{15}j^2=16\cdot120-1240=680$. Both derivations preserve the equality cases in the loop bounds. The triple (1,1,1), for example, is a genuine execution and would be lost by counting only strictly increasing original indices.

The other numerical alternatives disagree with both exact counts. Counting 15³ ignores the dependent bounds; choosing three distinct numbers from 15 omits repetitions; returning only 680 omits initialization. An accumulator invariant can say that Cod equals 10 plus the number of completed innermost visits at the current checkpoint, making conservation of the count explicit. The granted wide-type premise must cover loop-index increments as well as Cod. A narrow implementation can overflow on a terminating update after the last useful body visit even when all useful indices were representable; the mathematical loop count does not by itself certify its machine translation.

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

### Solution 17

**Correct option: 1. Maintain a region, not a guessed match.** Initially lo=0 and hi=6. With the half-open loop, the first midpoint is 3. A[3]=3 is at least the target, so set hi=3; equality must not skip earlier duplicates. The second midpoint is 1, whose value is again 3, so hi=1. The third midpoint is 0, with A[0]=1 below the target, so lo=1. The boundaries meet at 1 and the loop returns index 1. The inspected midpoint sequence is therefore (3,1,0).

The invariant says every index below lo has value below 3, every index at or above hi has value at least 3, and $0\le lo\le hi\le6$. Initially the classified regions are empty. Sortedness justifies extending the appropriate region after each comparison. When lo=hi, no unclassified positions remain; index 1 is the first eligible index, not merely some occurrence of 3. The width hi−lo is a nonnegative integer and strictly decreases at every body execution.

An alternative starting with midpoint 2 uses a different midpoint or closed-interval convention. A result at 2 or 3 finds a matching duplicate but fails the first-occurrence specification. Returning zero treats the last inspected midpoint as the answer, even though that entry is below the target. Return the meeting boundary. The empty-array boundary and a target exceeding every element similarly return n, which is a legitimate insertion position but not an index to dereference.

### Solution 18

**Correct option: 2. Count body executions with the exact width recurrence.** Let L be the number of unclassified positions. A lower-bound iteration replaces L with at most $\lfloor L/2\rfloor$. Starting with 31, the worst surviving widths are 31,15,7,3,1,0. There are five transitions, hence five body executions and five inspected array entries. Initialisation and the final false guard evaluation are separate events.

More generally, the maximum number of iterations for length n is $\lceil\log_2(n+1)\rceil$ for n≥0. One way to see the precise threshold is that at most k iterations suffice for lengths at most $2^k-1$. The recurrence removes the midpoint and leaves no more than half of the previous width. For 31=$2^5-1$, five suffice, and a target outside the array's upper range realizes five steps. For n=0, the guard is false immediately, giving zero body executions.

Four iterations cannot resolve a length-31 worst path: after four maximal reductions, width 1 remains. Six usually comes from adding the final guard test to the body count, or using a loose logarithmic bound. Thirty-one would describe a linear scan. An asymptotic $O(\log n)$ statement is useful but does not determine which of nearby numeric options is correct. State the counted operation and the interval convention before using a formula.

### Solution 19

**Correct option: 1. Expose a nonshrinking singleton interval.** With array [2] and target 3, the initial boundaries are lo=0, hi=1. The midpoint is 0. Since A[0]=2 is less than 3, the faulty update sets lo=mid=0. Neither boundary changes. The next iteration has exactly the same state, makes the same comparison, and repeats forever. No out-of-bounds access is needed to demonstrate this failure.

The corrected update is lo=mid+1. In a half-open interval, the inspected midpoint has just been proved ineligible, so it belongs to the classified lower region and must be excluded from the remaining interval. Correct code changes [0,1) into [1,1), whose width is zero. The invariant may remain true under the defective update, but the strict-decrease obligation fails: a preserved relationship alone is not a total-correctness proof.

An input containing an exact match can conceal the fault because the other branch updates hi to mid and may shrink. Larger inputs may also shrink for a while before reaching a singleton. Thus successful traces are not evidence that this update terminates universally. A proposed counterexample that immediately takes the shrinking branch does not establish the stated infinite loop. The small explicit witness isolates the problematic transition and shows why adding a fixed iteration limit would merely mask the specification error rather than prove a correct result.

### Solution 20

**Correct option: 2. Verify the precondition used to eliminate a whole region.** The input is [4,1,3] with target 3. Starting at [0,3), midpoint 1 has value 1, so ordinary lower-bound code sets lo=2. Midpoint 2 then has value 3 and sets hi=2. The result is 2. Yet index 0 is already eligible because its value is 4≥3; therefore 2 is not the first index meeting the predicate.

The implementation has not suffered an indexing failure or an arithmetic failure. Its proof uses sortedness when it concludes from A[mid]<target that every earlier entry is also below target. That inference is false here: A[1]<3 but A[0]≥3. The first transition destroys the region invariant, even though lo and hi continue to satisfy the numeric bounds and the width still decreases. Termination survives while functional correctness fails.

The example does not show that binary search fails on every unsorted input. Some unsorted arrays happen to yield a correct result for a chosen target. It shows that the universal guarantee requires a monotone search predicate, typically established by sortedness. An alternative that calls the output a first occurrence also confuses lower bound with equality search; an eligible entry may exceed the target. Sort first only if changing array order is permitted by the application contract. Otherwise use a suitable scan or prove a different monotonicity premise for the searched sequence.

### Solution 21

**Correct option: 3. Use two distinct threshold predicates.** The array is [1,2,2,2,5]. Lower bound for 2 returns the first index with value at least 2, namely 1. Upper bound returns the first index with value strictly greater than 2, namely 4. Thus the requested pair is (1,4), and the half-open equal-key block is [1,4). Its width is three, the number of occurrences of 2.

For lower bound, move lo past mid only when A[mid]<2; equality moves hi left. For upper bound, move lo past mid when A[mid]≤2; equality is deliberately eliminated from the lower region. Their invariants use different comparison predicates even though their index mechanics are identical. At exit, each meeting boundary marks its own first qualifying position. Both algorithms terminate because their unresolved interval shrinks.

Returning the final occurrence index 3 as the upper bound is an inclusive-end convention, not the specified first strictly greater index. Returning zero or five fails the threshold definition for this concrete input. A pair (1,1) ignores the equality block. If the target is absent, the two boundaries coincide and the occurrence count is zero. If all values equal the target, they return 0 and n. These boundary positions are valid results even when n itself cannot be dereferenced. Convert interval conventions explicitly before extracting a count or checking a proposed answer.

### Solution 22

**Correct option: 2. Derive both branches before taking their maximum.** Let $L=hi-lo>0$ and $mid=lo+\lfloor L/2\rfloor$. The update hi=mid leaves length $\lfloor L/2\rfloor$. The update lo=mid+1 leaves length $L-\lfloor L/2\rfloor-1$. For odd length $L=2q+1$, both are q. For even length $L=2q$, the left remainder is q and the right remainder is q−1. Therefore the tight common upper bound is $\lfloor L/2\rfloor$.

The bound is attainable by the hi branch for even lengths and by either branch for odd lengths. It is a bound on the new interval's number of entries, not on the value of mid or on an inclusive endpoint difference. For L=1, both updates produce an empty interval and the bound is zero. For L=2, one branch can retain one entry; this small case rules out a universal zero-width claim.

A ceiling expression can be a valid looser estimate, but it is not the tight common bound asked for. A bound retaining the midpoint overcounts one branch and can obscure why the singleton case terminates. A statement that the length is always exactly half fails for odd lengths and for the unequal even branches. Use the floor and the removed midpoint explicitly; informal statements about halving are insufficient when an examination asks for an exact recurrence or worst-case step count.

### Solution 23

**Correct option: 3. Count shifts as strict inversions removed.** Starting from [4,2,3,1], insertion of 2 shifts 4 once and produces [2,4,3,1]. Insertion of 3 shifts 4 once and produces [2,3,4,1]. Insertion of 1 shifts 4, then 3, then 2, producing [1,2,3,4]. The total number of shifts is $1+1+3=5$. The three final placements of saved keys are writes, but they are not shifts under the stated count.

Each shift corresponds to an earlier value strictly greater than the current saved key. The original strict inversions are (4,2), (4,3), (4,1), (2,1), and (3,1), again five. An insertion moves each such greater prefix element one position right while retaining its value. This gives an independent combinatorial explanation rather than only a simulation.

Counting all writes would add key placements and obtain another quantity; counting comparisons also includes successful or failed loop conditions, depending on the model. These are not interchangeable operation counts. An answer based on the final sorted array alone misses the input-dependent work. With a strict greater-than shift condition, equal keys do not cross, which preserves their original relative order. Replacing it with greater-than-or-equal changes both the treatment of equal-key pairs and stability. Always identify the exact instruction being counted before importing an inversion formula.

### Solution 24

**Correct option: 2. Remove the logical hole before checking conservation.** When inserting saved key 2 into [1,4,2], shift 4 one position right. The physical array becomes [1,4,4], the saved key remains 2, and the hole is now index 1. The physical array temporarily contains two copies of 4 and no stored 2. Consequently, a claim that the whole physical array remains a permutation after every shift is false.

The correct invariant counts all physical positions except the hole and adds the separately saved key. Here that multiset is $\{1,4\}\uplus\{2\}$, exactly the original $\{1,4,2\}$. The value occupying the hole is ignored because it is a stale or duplicated value, not a logically retained record. Writing the saved key into index 1 closes the hole and yields the physical permutation [1,2,4]. The order proof and the conservation proof meet at that final placement.

Tracking the whole physical array plus the saved key would double-count a value; tracking only the physical array loses the saved record. A sorted-prefix condition alone cannot prove conservation. The logical-hole interpretation explains how an in-place algorithm can temporarily have duplicated physical data without discarding its logical input. This is an invariant at a specified checkpoint, with a precise representation of pending data. A different implementation using swaps needs a different intermediate conservation argument rather than this same hole annotation.

### Solution 25

**Correct option: 2. Test stability with identities, not just key values.** Take records (2,a) followed by (2,b), where a and b distinguish original positions. When the second record is inserted using a greater-than-or-equal shift condition, the first record's key 2 qualifies for shifting. Record a moves right, and saved record b is placed before it. The result is [(2,b),(2,a)]. The key sequence remains sorted, and the record multiset is preserved, but the original order of equal keys is reversed.

Stability requires equal-key records to appear in their original relative order. It cannot be checked on the unlabeled array [2,2], whose displayed values look unchanged after reversal. The strict comparison A[j]>key avoids shifting an equal predecessor, so the saved record is inserted after earlier equal records. A complete stable-sorting contract therefore includes order, conservation, and tie-order preservation as distinct obligations.

An alternative asserting that the result is unsorted confuses stability with nondecreasing key order. An alternative claiming data loss ignores that both labeled records still occur exactly once. An alternative claiming unchanged stability is refuted by this smallest pair. The defect is not that equality comparisons are intrinsically wrong; their direction must match the desired stable placement. This example also explains why a proof using only numerical keys cannot establish every property promised for records carrying associated data.

### Solution 26

**Correct option: 3. Stop comparing heads when a run is exhausted.** Merge [1,4,7] and [2,3,8]. Compare 1 with 2 and emit 1. Compare 4 with 2 and emit 2. Compare 4 with 3 and emit 3. Compare 4 with 8 and emit 4. Compare 7 with 8 and emit 7. The left run is now exhausted, and the remaining 8 is copied without another comparison between two valid heads. Thus there are five head comparisons.

After each comparison, the emitted prefix contains exactly the consumed entries and is sorted; every remaining entry is at least its last emitted key. Both input runs must themselves be sorted for this implication. Once either run is exhausted, the other is a sorted suffix and can be appended. Testing whether a pointer has reached the end is a boundary test, not the same operation as comparing two head values.

Counting six confuses the output length with head comparisons. Counting fewer misses one of the explicit pairs. Counting all guards and pointer checks would require a separately specified implementation. For two nonempty runs of lengths a and b, the maximum is a+b−1, attained here with a=b=3. A empty run needs zero head comparisons. For stability, choose the left head on equal keys when the left run precedes the right in the original array; the present distinct-key trace cannot alone demonstrate that tie rule.

### Solution 27

**Correct option: 1. A one-property checker cannot certify a two-property contract.** A sorting postcondition requires the output to be ordered and to preserve the complete input multiset. A routine that overwrites all entries with zero always produces a nondecreasing array. For input [3,1], however, its output [0,0] does not preserve either original value. A verifier that checks only sortedness accepts this invalid result.

The weakness is a missing specification obligation, not a counterexample to the sortedness check's implementation. Sortedness is a necessary property but insufficient for sorting correctness. Conversely, a checker that verifies only the multiset accepts an unsorted permutation, such as unchanged [3,1]. Both properties must be established. If stability is also promised, equal-key record order adds a third obligation; neither key sortedness nor multiset preservation implies it.

Zeroing can coincidentally be a correct result for an all-zero input. That exceptional input does not rescue the claim that the routine sorts every admitted input. To refute a universal guarantee, one explicit admitted failing input suffices. To certify a particular output, check every promised property for that particular input and result. If the application requires associated records rather than bare keys, compare whole records or a trustworthy original-index certificate, not just the key multiset. The lesson is to derive the checker from the full contract rather than from a visually pleasing output.

### Solution 28

**Correct option: 2. The base case must cover every minimal admitted input.** Suppose merge sort returns only when n=1. On an empty input, n=0 does not satisfy that condition. Splitting it yields empty children with size zero, and the recursive call repeats the same unresolved situation. Along that call path, the measure n does not strictly decrease. The function never reaches its sole base case.

The usual repair is a base condition n≤1, assuming the size is always a nonnegative integer. Both empty and singleton arrays are already sorted and preserve their own elements. For n≥2, proper halves are strictly smaller, so strong induction and the natural-valued termination measure apply. The two parts of the argument are inseparable: a decreasing measure above the base region does not compensate for a missing admitted boundary case.

Calling the failure a merge-comparison error misidentifies its location; no meaningful pair of nonempty runs is reached on this path. Claiming that the empty result is automatically returned assumes code that is absent. Claiming that a zero-length child eventually becomes length one reverses the split operation. A different contract explicitly excluding empty inputs could make n=1 a sufficient base case, provided every recursive call preserves that exclusion. The displayed routine is intended to accept empty input, so weakening the advertised domain is not a valid proof of its existing specification.

### Solution 29

**Correct option: 2. Trace the unknown region and the swaps it causes.** Use boundaries lt=i=0 and gt=5 for [3,1,2,3,0], with pivot 2. The regions are [0,lt) below the pivot, [lt,i) equal to it, [i,gt) unknown, and [gt,5) above it.

| Before the body | Action | Array afterward | New (lt,i,gt) |
|---|---|---|---|
| (0,0,5) | 3>2: decrement gt and swap indices 0,4 | [0,1,2,3,3] | (0,0,4) |
| (0,0,4) | 0<2: swap indices 0,0 and advance lt,i | [0,1,2,3,3] | (1,1,4) |
| (1,1,4) | 1<2: swap indices 1,1 and advance lt,i | [0,1,2,3,3] | (2,2,4) |
| (2,2,4) | 2=2: advance i | [0,1,2,3,3] | (2,3,4) |
| (2,3,4) | 3>2: decrement gt and swap indices 3,3 | [0,1,2,3,3] | (2,3,3) |

At exit i=gt=3. The below-pivot block ends at lt=2, and the equal block ends at gt=3, so the result is (2,3). Notice that i stays unchanged after a greater-key swap because its replacement came from the unknown region and still needs classification. Every action reduces gt−i by one, giving five body executions.

The final array happens to be fully sorted, but that is not the partition contract. In another input, either unequal-key region can remain internally unsorted. Alternatives using inclusive equal-block endpoints or confusing lt with a count of all processed entries give different numbers. Boundaries must be read from the stated half-open regions, not guessed from the final array's appearance.

### Solution 30

**Correct option: 3. The incoming key is unclassified, so it cannot be skipped.** With [3,1] and pivot 2, initially lt=0, i=0, gt=2. Key 3 is greater than the pivot. The branch decrements gt to 1 and swaps A[0] with A[1], producing [1,3]. Correct code leaves i=0 so that the incoming 1 is inspected next. The faulty code increments i to 1, ending the loop because i=gt.

The claimed equal region [lt,i) is then [0,1), containing key 1 rather than pivot 2. The values above gt are correctly greater, and the array is still a permutation; nevertheless, the partition boundary contract is false. In correct code, the next smaller-key branch moves lt and i to 1, leaving the equal region empty and returning boundaries (1,1).

Sorted-looking output [1,3] does not certify the faulty boundaries. A client can use those boundaries to omit or mishandle a key even when the displayed array looks orderly. The single failing region is enough to disprove the invariant-preservation obligation. An example in which the incoming unknown key already equals the pivot may hide the defect, so choose a witness with a strictly smaller incoming key. The repair follows directly from the representation: classifying the old key on the right does not classify the new key now occupying the current position.

### Solution 31

**Correct option: 1. Use a conserved progress count.** The unknown region has width $V=gt-i$. Initially its width is n. In the smaller-key branch, i increases by one while gt is unchanged. The equal-key branch also increases i by one. In the greater-key branch, gt decreases by one while i is unchanged. Therefore every body execution decreases V by exactly one, whatever the key distribution.

The invariant bounds ensure V is a nonnegative integer and the guard is true precisely when V>0. Exit occurs at V=0. Hence there are exactly n body executions, including n=0, where the loop executes zero times. An input with all greater keys still performs n shrinking-right steps; an input with all equal keys performs n advancing-left steps. These different traces have the same count because the measure, not the branch frequency, controls progress.

The result does not say that every physical array position is inspected exactly once. A right swap can bring a new entry to the same index, causing that index to be inspected again. It also does not give an exact comparison count when the branch structure sometimes performs two key comparisons. Swaps, writes, guards, and body executions are different quantities. A claim of quadratic work based on repeated inspection at one index ignores that each such inspection consumes a distinct position from the shrinking unknown region.

### Solution 32

**Correct option: 3. Preservation and stability are separate.** Label the two equal records 3a and 3b to expose their identities. Start with [3a,3b,1c] and pivot 2. The first greater-key branch swaps 3a with 1c, producing [1c,3b,3a]. The smaller-key branch advances lt and i past 1c. The final greater-key branch moves the right boundary over 3b. The output is [1c,3b,3a], with the equal-3 records in reversed original order.

All records remain present exactly once because each transformation is a swap. The below/above region contract also holds. The failure is solely stability: among records with the same key, b now precedes a even though a preceded b in the input. Without labels, the array [1,3,3] would conceal this reversal.

An option asserting element loss contradicts the swap-conservation property. An option asserting full sorting as a general guarantee extrapolates from this small witness; the algorithm promises partition regions rather than internal order. An option asserting stability is directly refuted by the labeled pair. To obtain a stable partition, one needs a different method or additional storage/rotation reasoning with a proven order-preservation contract. Adding a stable recursive sorter after an unstable partition does not automatically restore the original order of equal records already reversed during partitioning.

### Solution 33

**Correct option: 1. Retain the original dividend in the invariant.** For X=47 and positive Y=6, initialize q=0 and r=47. Each body replaces r by r−6 and q by q+1. The successive (q,r) pairs are (0,47), (1,41), (2,35), (3,29), (4,23), (5,17), (6,11), and (7,5). At that point r<6, so there have been seven iterations and the quotient–remainder pair is (7,5).

The invariant is $X=qY+r$, with q,r nonnegative integers and original X,Y unchanged. One step preserves it because $(q+1)Y+(r-Y)=qY+r$. The guard r≥Y makes the new remainder nonnegative. At exit, $0\le r<Y$ together with the invariant gives the Euclidean division specification. A natural-valued remainder strictly decreases by positive Y, proving termination.

The equality alone does not prove that r lies in the required range; the exit guard and lower bound are essential. A proposed pair (6,11) satisfies the equality but has a remainder at least the divisor. An iteration count including the initialization or final failed test changes the counted event. Uniqueness follows because two valid remainders in [0,Y) cannot differ by a nonzero multiple of Y. This proof uses exact nonnegative arithmetic and a positive divisor; those premises must be checked separately in an implementation.

### Solution 34

**Correct option: 3. A conserved equality does not imply progress.** With Y=0 and X≥0, initialize q=0 and r=X. The guard r≥Y is always true because r remains nonnegative. Each body changes q to q+1 but leaves r unchanged: r−0=r. The invariant $X=qY+r$ still holds, since qY is always zero. Thus the algebraic conservation argument survives while the termination argument collapses.

There is no quotient–remainder pair satisfying $0\le r<Y$ when Y=0, because the required interval is empty. A claim that r eventually becomes less than zero assumes subtraction of a positive value that is not present. A claim that increasing q establishes termination uses a measure moving in the wrong direction and lacking a finite upper bound under exact integer semantics. Finite-width overflow would introduce another safety defect rather than prove the mathematical loop terminates correctly.

This witness separates three obligations: preservation of a relation, attainability of the postcondition, and termination under a well-founded measure. To restore total division correctness, require Y>0 as part of the contract and ensure the arithmetic model supports the intended operations. Checking only Y≥0 is insufficient. A loop invariant can be perfectly preserved for an invalid input domain; the missing domain restriction is not repaired by asserting that same invariant more frequently.

### Solution 35

**Correct option: 1. The remainder must use the old first coordinate.** For initial (a,b)=(21,15), the defective sequential commands first execute a=b, giving (15,15). The next command b=a%b now evaluates 15%15=0. The loop exits with a=15, whereas the true gcd of 21 and 15 is 3. The first overwritten value 21 was required to compute the remainder 6 and has been lost.

Correct simultaneous execution gives (15,6), then (6,3), then (3,0), returning 3. A sequential implementation can preserve the intended transformer by computing `remainder=a%b` before overwriting a, then assigning a=b and b=remainder. The number-theoretic identity is $\gcd(a,b)=\gcd(b,a\bmod b)$ for b>0; it refers to the original values on the right-hand side.

The faulty transition can still terminate immediately and return a divisor of one original argument. Neither property proves that it returns the greatest common divisor of both. An input where b divides a could hide the mistake because the correct remainder is also zero. Choosing 21 and 15 makes the lost dependence visible. An alternative based on the final zero as the returned gcd confuses the loop's stopping coordinate with the returned coordinate. Proofs of assignments must fix their evaluation order before invoking an algebraic identity.

### Solution 36

**Correct option: 3. Count actual Euclidean transitions.** Starting with (34,21), the successive pairs are (21,13), (13,8), (8,5), (5,3), (3,2), (2,1), and (1,0). Each pair results from one remainder operation and one simultaneous coordinate update. There are seven body executions; the result is gcd(34,21)=1.

At every checkpoint, the gcd of the current pair equals that of the original pair. To justify the identity, write a=qb+r. A number divides a and b exactly when it divides b and r=a−qb, so the two pairs have the same common divisors. For nonnegative a and positive b, the new second coordinate r is in [0,b), making b a strictly decreasing natural-valued measure until it becomes zero.

Counting eight includes the initial pair as if it were a transition or includes the final false guard evaluation. Counting six omits the final remainder 2%1=0. Consecutive Fibonacci values make this trace relatively long because many quotients are one, but that observation does not change the explicit count. The algorithm must treat b=0 as a base condition before taking a remainder. Negative operands require a separately stated remainder convention and gcd sign convention; the nonnegative proof cannot be transferred silently to every language's signed `%` semantics.

### Solution 37

**Correct option: 1. State the checkpoint after a complete body.** Initialize r=1, b=3, e=13. In the first body, e is odd, so r becomes 3; b is squared to 9 and e becomes 6. In the second body, e=6 is even, so r stays 3; b becomes 81 and e becomes 3. Therefore the checkpoint after two complete bodies is (r,b,e)=(3,81,3).

The conservation relation is $r b^e=3^{13}$. After the first body it reads $3\cdot9^6=3^{13}$; after the second it reads $3\cdot81^3=3^{13}$. For an even old exponent e=2q, squaring the base and replacing e with q preserves the relation. For an odd exponent e=2q+1, first multiplying r by the old base and then squaring the base produces the same conservation.

An answer with r=27 after two bodies incorrectly performs an accumulator multiplication for the even exponent 6 or uses the updated squared base in the first odd branch. An answer with b=9 stops after the second accumulator decision rather than after the complete second body. A correct invariant must be associated with an exact program point; intermediate updates may not satisfy its checkpoint form individually. These values use exact integers. If multiplication is finite-width, every performed accumulator product and square needs its own range guarantee.

### Solution 38

**Correct option: 2. Separate set bits from processed bits.** The exponent 45 has binary expansion 101101, with six bits and four ones. Repeated integer halving processes exponents 45,22,11,5,2,1 before reaching zero. The odd cases are 45,11,5,1, so the accumulator is multiplied four times. The displayed body squares the base once in each of all six iterations, giving six squarings.

These counts assume the exact code whose square occurs even in the last body. A different implementation can avoid the final unused square after the exponent has become zero; that would have five base squarings, but it is not this program. At exponent zero initially, there are zero body executions and no products. For positive exponent B, this implementation has bitlength(B) squarings and popcount(B) accumulator multiplications.

An option giving six accumulator multiplications mistakes all bits for one bits. An option giving four squarings counts only odd branches. An option omitting the final square answers a modified routine. The last unused square can still overflow a machine type even when the final returned answer itself fits. Removing it may improve safety, but requires changing the code and rechecking its contract. An examination's operation count follows the written statements, including computations whose values will not subsequently be used.

### Solution 39

**Correct option: 3. Squaring before the odd multiplication changes the exponent.** For base 2 and exponent 1, begin with r=1, b=2, e=1. The faulty ordering squares b first, giving b=4. Because the old exponent is odd, it then multiplies r by this new base, producing r=4. Halving e gives zero and the routine returns 4 instead of $2^1=2$.

The correct odd transition is $r'=rb$, $b'=b^2$, and $e'=(e-1)/2$, with both products interpreted using the old b where specified. It preserves $r'b'^{e'}=rb^{1+2((e-1)/2)}=rb^e$. The reordered routine instead inserts an extra factor of the old base into this equality. A saved old base could repair the reordered code, but simply appealing to commutativity of multiplication cannot undo the overwritten operand.

An exponent-zero input hides the defect because no body executes. Some bases, such as one, can also yield an accidental correct value. The simple witness (2,1) requires one body and isolates the semantic problem. An alternative blaming the loop guard overlooks that the guard and halving terminate correctly here. This is a partial-correctness failure caused by assignment order. When translating simultaneous mathematical transitions into imperative code, either choose a safe order or explicitly retain every old value needed later.

### Solution 40

**Correct option: 2. Normalize the identity under the output representation.** Modular exponentiation with modulus M=1 has only one canonical residue, zero. At exponent e=0, the result is the residue of the multiplicative identity: $1\bmod1=0$. If the accumulator is initialized to literal 1 and the loop does not execute, it returns a value outside the required canonical interval [0,1).

Initializing r to $1\bmod M$ handles this boundary and gives zero when M=1. For general positive M, reduce the input base as well, and maintain the modular relation between the accumulator, remaining power, and original target. The exponent-zero convention here is the algebraic empty-product identity; it is independent of whether the unreduced numerical base is zero.

An option returning one confuses a representative of a congruence class with the specified normalized residue. One and zero are congruent modulo one, but the contract asks for the canonical representative. Modulus zero is not an admissible alternative because the remainder operation is undefined in this intended model. An option insisting on a multiplication to force reduction changes the exponent-zero control path unnecessarily. This example shows that numerical equivalence under a relation may be weaker than a representation contract; check the required range as well as the mathematical congruence.

### Solution 41

**Correct option: 2. A later modulus cannot reconstruct an earlier lost product.** Exact multiplication gives $200\cdot200=40000$. Dividing by 251 gives $40000=159\cdot251+91$, so the intended residue is 91. In the stipulated unsigned-eight-bit multiplication model, the stored product is $40000\bmod256=64$. Reducing that stored value modulo 251 still gives 64. The two residues differ.

The error is the premature reduction modulo 256, not the final `%251` operation. Modulo 256 and modulo 251 are different equivalence relations; preserving one does not preserve the other. The factors already lie below 251, so reducing them first modulo 251 does not fix this particular narrow-product failure. A wider exact product or a proven overflow-safe modular multiplication algorithm is needed.

This question explicitly stipulates an eight-bit product. In actual C, small unsigned operands can undergo integer promotions before multiplication, so their declaration alone does not establish this exact model. One must inspect the effective expression type and any subsequent narrowing conversion. Signed overflow has different semantics and must not be described as guaranteed wraparound. An alternative returning the exact 91 from the narrow stored 64 assumes information no longer available. Always separate abstract integer arithmetic, chosen wrap semantics, and the real language's evaluation rules before transferring a proof to code.

### Solution 42

**Correct option: 1. A stable index certificate records identity through the sort.** Input [5,1,5] has original indices 0,1,2. Output [1,5,5] is certified by [1,0,2]: the first output value comes from input index 1, the next from index 0, and the last from index 2. The indices occur exactly once, each output key matches its referenced input key, and the two equal keys preserve their original index order 0 before 2.

Check the three obligations separately. A permutation of indices establishes that no record is duplicated or lost. Matching referenced keys establishes consistency with the output. Increasing original indices among equal output keys establishes stability. Nondecreasing output keys still needs its own check; an index permutation by itself does not certify sorting order.

The alternative [1,2,0] matches the same numerical output and is a valid index permutation, but reverses the equal-key records and fails stability. An alternative beginning with index 0 or 2 assigns a key 5 to the first output value 1 and fails consistency. An alternative repeating an index fails conservation, even if the referenced key coincidentally matches both output positions. For records carrying other fields, the certificate should identify whole original records, not just bare key values. Labeled identities turn a visually invisible stability defect into a checkable mathematical statement.

### Solution 43

**Correct option: 3. Match an attaining witness to a universal bound.** In a minimization problem, suppose a feasible solution has cost 17 and a valid lower-bound proof establishes that every feasible solution has cost at least 17. Let OPT denote the optimal value. Feasibility gives OPT≤17 because the optimum cannot exceed the cost of an available candidate. The universal lower bound gives OPT≥17. Combining the two inequalities yields OPT=17, so the candidate is optimal.

Neither component is enough alone. A feasible cost-17 solution only provides an upper bound; there might be another solution costing 12. A lower bound of 17 alone does not establish that any feasible solution attains it. Their equality closes the proof. The bound must apply to the same instance, domain, and cost definition as the witness, and the witness's feasibility must be checked rather than assumed from its numerical cost.

An alternative claiming a unique optimum adds an unsupported conclusion: two different feasible solutions might both cost 17. An alternative treating 17 only as a possible value ignores the two-sided bound. An alternative reversing the inequalities confuses minimization with maximization. For maximization, a feasible witness is a lower bound and a universal bound is an upper bound; the same meeting-value argument then applies with reversed roles. Certificates prove a stated property, not every desirable property of a candidate.

### Solution 44

**Correct option: 3. Check every edge inequality.** The proposed distances are d(s)=0, d(a)=2, d(b)=5. Along s→a of weight 2, the inequality d(a)≤d(s)+2 holds with equality. Along a→b of weight 3, d(b)≤d(a)+3 also holds with equality. But the direct edge s→b has weight 4, and its inequality would require 5≤4, which is false. The proposed distance to b is therefore not certified.

The actual direct path gives distance at most 4, already contradicting the claimed shortest-path value 5. The longer path s→a→b has cost 5 and shows that 5 is a feasible path cost, but feasibility of a path does not make it shortest. This is the minimization distinction between an available upper bound and a matching universal lower bound.

In a valid certificate, edge inequalities telescope along every s-to-v path to give d(v) no greater than that path's cost. A rooted attaining path of cost d(v) supplies the reverse inequality, so the two bounds meet. Checking only the chosen parent edges can accept this false claim because the unchosen direct edge is exactly the missed shortcut. An alternative that rejects only the a→b edge has the wrong arithmetic. A certificate verifier must include all relevant graph edges, not merely the edges used to display an attractive candidate route.

### Solution 45

**Correct option: 2. Local equalities do not establish a rooted attaining path.** In the graph s→a with weight 5 and the zero-weight edges a→b and b→a, the proposed labels d(s)=d(a)=d(b)=0 pass all edge inequalities. The first is 0≤5; the other two are 0≤0. Choosing parent(a)=b and parent(b)=a also gives local parent equalities because both parent edges have zero weight.

Nevertheless, following either parent chain cycles between a and b and never reaches s. No s-to-a or s-to-b path of cost zero exists: every such path must first use s→a, paying 5, and the subsequent zero-weight moves cannot reduce that cost. The actual shortest distances to a and b are 5. The local equations define a consistent cycle of labels without providing an attaining witness rooted at the source.

The missing certificate condition is that every relevant parent chain reaches s, or an equivalent verified acyclic/rooted structure. A depth label decreasing toward the root can help certify that property if checked correctly. A claim that nonnegative edges alone exclude a parent cycle is false because zero-weight cycles are possible. A claim that passing edge inequalities proves exact distances supplies only one direction of the optimality argument. The path witness is the independent second direction and must not be replaced by unrooted local equalities.

### Solution 46

**Correct option: 2. A valid certificate can include a negative edge.** For s→a of weight 4, s→b of weight 5, and a→b of weight −3, proposed labels are d(s)=0, d(a)=4, d(b)=1. The edge checks are 4≤4, 1≤5, and $1\le4-3=1$. All hold. The path s→a attains 4, and the path s→a→b attains 1, so both vertex labels have rooted attaining witnesses.

To prove the certificate's lower-bound direction, sum each checked inequality along any s-to-v path. Intermediate distance labels cancel, leaving d(v)≤the path cost because d(s)=0. Negative individual edge weights do not invalidate that algebra. The attaining paths establish that the minimum path cost is at most d(v), closing equality for a and b.

An alternative rejecting the certificate merely because −3 is negative confuses a particular algorithm's operational preconditions with this proof framework. Standard Dijkstra reasoning requires a nonnegative-weight condition; a distance certificate verified independently uses different obligations. An alternative selecting direct cost 5 ignores the cheaper two-edge path. The example has no directed cycle, so no negative cycle issue arises. Certificates must still restrict claims to vertices with verified reachability and account for infinity labels if used; those additional representations are not present in this three-vertex finite-label problem.

### Solution 47

**Correct option: 1. Sum the local inequalities around the cycle.** A directed cycle with edge weights 2,−5,1 has total weight −2. Suppose finite distance labels satisfy every edge inequality on this cycle. Writing the three inequalities and adding them cancels all distance labels on both sides, leaving $0\le2-5+1=-2$, an impossibility. Therefore no finite label assignment can satisfy every required edge inequality on that cycle.

If the cycle is reachable from the source and walks may repeat vertices, traversing it an additional time decreases the cost by 2. There is no finite minimum walk cost for the affected reachable destinations: costs can decrease without bound. This operational explanation agrees with the algebraic obstruction. It is not necessary to guess which one edge will fail for a particular tentative labeling; at least one must fail by the summed contradiction.

The conclusion concerns a negative total cycle, not a single negative edge. Question 46 supplies a valid negative-edge example with no negative cycle. A zero-total cycle does not produce this strict contradiction, though it can still expose an unrooted-parent defect as in Question 45. Reachability matters when interpreting source distances; an isolated unreachable negative cycle does not imply that every reachable distance is unbounded. A certificate's selected domain and infinity conventions therefore must be specified when moving beyond the finite reachable cycle considered here.

### Solution 48

**Correct option: 2. Feasibility of a greedy output does not prove optimality.** An earliest-start rule chooses the long interval [0,10) first. Each of [1,2), [2,3), and [3,4) then conflicts with it, so the rule selects only one interval. The three short intervals are mutually compatible under the half-open endpoint convention: the end of one can equal the start of the next. Choosing them yields three intervals.

The greedy output is feasible but not maximum-cardinality. In this instance, three is also optimal: the long interval excludes all three short ones, and without the long interval there are only those three candidates. The example gives a concrete strict improvement and an exact optimum, not just a suspicion that another rule might perform better.

An alternative claiming that earliest start is universally optimal confuses a plausible priority with an exchange argument. Earliest finishing time supports a different standard greedy proof for unweighted interval scheduling; it is not interchangeable with earliest start. An alternative rejecting touching short intervals uses a closed-interval conflict convention rather than the stated half-open one. An alternative calling the one-interval result infeasible also misidentifies the problem: it satisfies compatibility but fails optimality. Before proving a method, fix the objective, endpoint rules, and admissible schedules; otherwise even a correct proof can address the wrong problem.

### Solution 49

**Correct option: 1. Compute the mass and interpret the equality condition.** The complete listed leaf set has depths 1,2,3, so its mass is $2^{-1}+2^{-2}+2^{-3}=1/2+1/4+1/8=7/8$. The result is below one and therefore cannot prove that the finite binary tree is full. In fact, it refutes fullness under the complete-leaf-set premise, because every finite full binary tree has total leaf mass exactly one.

One realizing tree has a root with a left leaf and a right internal child. That child has one leaf at depth 2 and another internal child whose single child is the depth-3 leaf. The unoccupied sibling at depth 3 accounts for the missing mass 1/8. This explicit structure shows both that the depth list is realizable and where the conservation deficit occurs.

An option giving one assumes a second depth-3 leaf that is not listed. An option declaring fullness from the existence of three leaf levels confuses depth variety with each internal node having two children. A greater-than-one result contradicts the root mass bound. The equality characterization needs a finite tree and the complete set of leaves; a partial leaf sample can have mass below one even within a full tree. State those premises before applying a structural conclusion from a numerical sum.

### Solution 50

**Correct option: 3. Count the weakly ordered triples and retain the offset.** Each increment corresponds to one triple $1\le i\le j\le k\le n$. Map it to the strictly increasing triple $(i,j+1,k+2)$ in {1,…,n+2}. Conversely, a strict triple (u,v,w) maps to (u,v−1,w−2), satisfying the original weak inequalities. The map is a bijection, so the increment count is $\binom{n+2}{3}$ and the final accumulator is $c_0+\binom{n+2}{3}$.

For n=2, the four triples are (1,1,1), (1,1,2), (1,2,2), and (2,2,2), matching $\binom43=4$. This small case exposes why repeated indices must count. Selecting three distinct original indices would instead count $\binom n3$, which is wrong. Multiplying n³ ignores the order constraints and includes many forbidden triples. Omitting c₀ counts work but does not give the requested final value.

An independent sum groups by j: there are j possible i-values and n−j+1 possible k-values, giving $\sum_{j=1}^n j(n-j+1)=n(n+1)(n+2)/6$. At n=0, no body executes and the accumulator remains c₀; the polynomial also gives zero increments. The exact arithmetic model must support every loop-index update as well as the accumulator. The bijection proves a formula for dependent loops without assuming their bounds are independent.

### Solution 51

**Correct option: 2. Derive the indices from the recursive parameters.** With N=10 and initial call store(9,0), the source–destination pairs are (9,0), (7,1), (5,2), (3,3), and (1,4). The next call has source index −1 and returns before accessing either array. There are five copied elements, and the last copied source index is 1.

At the kth active call, starting with k=0, the parameters satisfy $n=N-1-2k$ and i=k. An access occurs precisely while n≥0. For N=10, that allows k=0,…,4. The caller must allocate at least $\lceil N/2\rceil=5$ destination positions. The source indices lie in [0,N), and the negative termination call has no read because the guard is checked first.

An option ending at source index zero uses the even-index sequence rather than every other index starting at the odd last index 9. Counting six includes the base call as if it wrote an element. A destination increment of two leaves gaps and does not implement compact copying. For an odd N, the last copied source index is zero; for an even positive N, it is one. For N=0, the initial source index is already −1 and no element is copied. Safety and the index relation explain all these cases together.

### Solution 52

**Correct option: 2. Match the sum to the next unprocessed index.** With s=0 and k=1, the invariant is $s=(k-1)^2$. It holds initially because both sides are zero. One body adds 2k−1 and then increments k. The new sum is $(k-1)^2+(2k-1)=k^2$, which equals $(k'-1)^2$ because k'=k+1. Thus the equality is preserved.

To derive the final result, also keep the bounds $1\le k\le n+1$ for an integer n≥0. The guard k≤n implies that advancing k preserves the upper bound. On exit k>n, the integer bounds force k=n+1, and the equality gives s=n². The variant n−k+1 is nonnegative at every guard checkpoint and decreases by one in each body. At n=0, initialization gives k=1, the guard is false, and s=0=n².

An invariant s=k² fails at initialization. An expression involving (k+1)² is offset in the wrong direction. A claim about the target n² alone is not the useful intermediate relation because it normally holds only at completion. The equality without bounds is insufficient to infer the exit value of k, and it says nothing by itself about termination. This example shows how a functional relation, range information, guard, and progress measure cooperate in a complete proof.

### Solution 53

**Correct option: 2. Strengthen the recursive contract before composing it.** A child routine that merely returns sorted data could replace every input value with zero and satisfy that weak condition. A parent that merges those sorted results would then return a sorted array containing the wrong values. Therefore sortedness of each child result is insufficient to prove that the whole recursion sorts the original input.

The required child contract includes preservation of the child's complete input multiset. For a split into left and right parts, their original multisets combine to the parent's multiset. By strong induction, both child outputs are sorted and preserve their own inputs. A correct merge then returns a sorted output whose multiset is the union of those child outputs, hence exactly the original parent's multiset. If stability is promised, the split order and merge's tie policy require additional proof.

Termination needs strictly smaller recursive inputs above a complete base region; none of these content properties alone proves it. An alternative adding only a runtime bound does not recover lost values. An alternative requiring both children to return identical arrays would be unjustified for different inputs. An alternative claiming sortedness alone is enough is refuted by the all-zero implementation. Strengthening an induction hypothesis is legitimate when one also proves that strengthened statement at the base and induction steps; it cannot simply be assumed because the parent needs it.

### Solution 54

**Correct option: 1. The initialization introduces an extra candidate.** A maximum routine initialized with best=0 and updated only by larger encountered values returns zero on the nonempty input [−2]. The true maximum is −2, which is the only input element. The routine's actual invariant is that best equals the maximum of zero and the processed values, not necessarily the maximum of the processed values alone.

The faulty method works for inputs containing a nonnegative maximum, which can conceal the defect in ordinary positive examples. Its failure on one admitted all-negative input refutes universal correctness. Returning zero also fails the witness property that a maximum of a nonempty finite input must be one of that input's values.

For a contract admitting arbitrary nonempty numeric arrays, initialize best to A[0] and begin scanning at index 1. Then the processed prefix is nonempty, best is one of its values, and no processed value exceeds best. Each comparison preserves those properties, and at the final index the prefix is the whole input. An alternative repair using a negative-infinity sentinel requires a type and comparator that support that sentinel, plus appropriate handling of NaN or other non-total values. An empty-input contract needs a separately defined result; neither A[0] initialization nor an unexplained zero return defines a maximum of an empty set.
