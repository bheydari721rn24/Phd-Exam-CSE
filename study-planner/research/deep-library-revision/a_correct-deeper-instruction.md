## Construct a complete proof, not an annotation list

### Construction 1. Four obligations at one checkpoint

For a loop with precondition P, guard G, body B, invariant I, and postcondition Q, first choose the checkpoint immediately before each guard evaluation. Initialisation must establish I from P. The body must re-establish I from I together with G. Exit must establish Q from I together with the negation of G. Total correctness additionally requires a well-founded decreasing measure whenever G is true, and the model must ensure that every executed expression and access is defined.

For a scan counting a key in an n-element array, use a processed half-open prefix [0,i). Define c to be the number of matches in that prefix, and keep $0\le i\le n$. Initially i=c=0, and the empty prefix contains zero matches. If i<n, reading A[i] is safe. Increase c by one exactly when A[i] equals the key, then increase i by one. The newly processed prefix adds exactly that element, preserving the count and the bounds. Exit gives i=n, so c counts the whole array. The measure n−i decreases by one and remains nonnegative. The unmodified input array is part of the frame condition; without that condition, a concurrent or hidden mutation could invalidate the counted prefix.

An assertion checked only on one trace does not prove its preservation from every state admitted by I. Conversely, a true relation may be too weak to imply Q. These are different failures. Testing the scan on an empty array verifies a boundary witness; the general proof above quantifies over every nonnegative n and every possible key distribution under the stated array model. [Cornell Lecture 4; CMU Contracts; MIT state-machine invariant principle.]

### Construction 2. Backward substitution includes definedness

The assignment rule for exact, defined expressions is $wp(x:=E,Q)=Q[x\leftarrow E]$. The right-hand side refers to the pre-assignment state. For a sequence, propagate the desired condition backward through the last statement first. For a conditional, require the relevant branch precondition under each guard outcome. These rules construct admissible initial states; they do not assert that a final condition already held initially.

Suppose a program assigns y=10/x using exact real division and the desired result is y≥2. Definedness requires x≠0. If x>0, multiplying by x preserves the inequality and gives 10≥2x, hence 0<x≤5. If x<0, multiplying reverses the inequality and gives 10≤2x, which is incompatible with x<0. The weakest admissible condition is therefore 0<x≤5. Simply substituting and multiplying by x without a sign split can include invalid negative inputs or the undefined input zero.

For array writes, model the array as a map with a single updated cell. A final predicate about A[i] after writing A[j]=v must split the alias case i=j from i≠j. Valid indices do not imply distinct cells. Machine arithmetic adds further definedness or representation constraints; an abstract real or integer expression must not silently adopt finite-width behavior. [Cambridge historical assignment/array rules; CMU executable contract qualifications.]

### Construction 3. A maximum needs an attaining value

To find the maximum of a nonempty ordered array, initialise best=A[0] and i=1. Use an invariant stating that best is a value in the processed prefix and is at least every value in that prefix, together with $1\le i\le n$. When the next value exceeds best, replace best with that value; otherwise retain it. Either update preserves the witness and upper-bound properties. At exit i=n, best is an input value dominating the whole input, hence its maximum.

For argmin, retain an index loc in [0,i) with A[loc]≤A[t] for every processed t. Initialisation loc=0 and i=1 satisfies this on the one-element prefix. Replacing loc only on a strict improvement selects the earliest minimum when ties occur; replacing on equality too selects the latest. Both satisfy an unspecified minimum-index contract, but only one satisfies a particular tie policy.

The nonempty premise licenses A[0]. A zero initial sentinel for a general maximum changes the candidate set to the input plus zero and fails on all-negative arrays. A NaN value does not obey ordinary total-order comparisons; a floating-point application must either exclude it or define and implement a compatible order. A proof of argmin's value alone does not establish that its reported index is valid or corresponds to that value. [Cornell argmin; CMU preconditions.]

### Construction 4. Logical representation controls conservation

Sorting requires order and conservation; stable sorting additionally preserves equal-key record order. During insertion, a saved key leaves a logical hole in the array. Each right shift duplicates a physical entry, so the physical array is not necessarily a permutation at an intermediate checkpoint. Exclude the hole and add the saved record to obtain the correct conserved multiset. When the saved key is placed in the hole, logical conservation becomes physical conservation again.

For [1,4,2], saving 2 and shifting 4 gives physical [1,4,4]. Excluding index 1 yields records {1,4}; adding the saved 2 restores the original multiset. The prefix-order argument must also say where larger shifted keys lie relative to the hole. Stable insertion shifts only strictly greater predecessor keys, so earlier equal records stay before the new equal record. An inclusive greater-or-equal test can keep keys sorted while reversing identities.

A merge instead has two consumed prefixes and one emitted prefix. The emitted multiset is their union, and the two unconsumed suffixes plus output preserve all input records. Sortedness of each run establishes that selecting a smaller valid head emits the smallest remaining key. When one run is exhausted, append the other safely. A proof cannot compare an exhausted head or assume an undefined sentinel value. The particular program determines its intermediate representation; a generic “the array stays sorted and unchanged” annotation is insufficient. [Stanford insertion/merge; Cornell interval representations.]

### Construction 5. Well-founded progress is more than numerical decrease

A natural-valued measure V that is nonnegative at the loop checkpoints and strictly decreases on every guarded transition cannot support an infinite execution: each descent consumes at least one natural step. For a two-boundary partition, V=gt−i is ideal because every branch reduces it exactly once. A body may revisit the same physical index after a swap while still making one unit of logical progress.

A positive real measure can decrease forever. Starting at x=1 and repeatedly dividing by two gives $x_k=2^{-k}>0$ for every finite k. The guard x>0 never becomes false under exact real semantics, even though x decreases and approaches zero. Finite floating-point underflow changes the program model and cannot be imported into that exact proof.

A lexicographic pair of naturals can prove termination when a lower-priority coordinate resets. For example, from (1,0) choose any finite B and move to (0,B), then repeatedly decrement the second coordinate until (0,0). The first coordinate decreases at the reset, making the lexicographic pair smaller regardless of B; afterward the second decreases. Every chosen execution is finite, but there is no uniform bound independent of the unrestricted B. Termination, a per-input runtime bound, and a bound uniform over all nondeterministic choices are distinct claims. [MIT well-founded state-machine progress; Cambridge historical variants.]

### Construction 6. Certificates meet a bound with an actual witness

For minimisation, a feasible witness of cost U gives OPT≤U. A verified lower bound L applicable to every feasible solution gives L≤OPT. If L=U, the candidate is optimal. Neither direction establishes uniqueness. The witness and bound must refer to the same instance and objective.

For source distances, require d(s)=0, edge inequalities $d(v)\le d(u)+w(u,v)$, and an s-to-v path attaining d(v) for each claimed finite distance. Summing inequalities along any path telescopes to d(v)≤that path's cost, providing the universal lower bound. The attaining path supplies the opposite bound, proving equality. Parent equalities alone are not paths: a parent cycle can satisfy every local equation while failing to reach the source. A decreasing rooted-depth certificate or an independently checked root-reaching walk repairs that missing condition.

Negative edges do not invalidate telescoping. A negative-total cycle does: summing its inequalities would imply zero is at most a negative number. Reachability and the definition of allowed walks determine which source-distance claims are affected. The certificate framework is independently derived from the reviewed invariant and contract methods; it is not attributed to a graph course that was only listed rather than read. Question 43 proves the bound/witness argument numerically, and Questions 44–47 test all three graph obligations with concrete counterexamples.
