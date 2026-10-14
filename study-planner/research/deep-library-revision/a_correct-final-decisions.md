## Complete examination decisions and mathematical summary

### 1. Fix the mathematical and implementation models first

Specify exact integers, exact reals, a chosen wrap model, or a concrete language expression type. The same source statement can have different behavior under those models. The exact-halving loop is infinite over positive reals, while a floating implementation may reach zero by underflow. Neither outcome licenses changing the model halfway through a proof.

### 2. Write the full contract before choosing a proof method

Order, multiset preservation, stability, valid indices, and output range are separate properties. A program satisfying one can violate another. A sorted array of invented zeros refutes a sorting checker that tests order alone. A canonical modular residue has a stronger representation condition than mere congruence.

### 3. Associate each relation with a program checkpoint

State whether the annotation applies before the guard, after an assignment, or after the complete body. Fast-power conservation is a relation across complete transitions; the partially updated registers may not satisfy that same form. A trace lacking checkpoint labels can silently mix old and new values.

### 4. Distinguish sufficient preconditions from the weakest one

A sufficient condition can exclude successful inputs. For $(x+3)^2=25$, initial x=2 is sufficient, but the weakest exact integer condition also includes x=−8. To claim weakest, show that every admitted state succeeds and every excluded state fails or is outside the defined model.

### 5. Propagate sequential requirements backward

The last assignment is substituted first when calculating a precondition for a sequence. For x+=1, y=2x, x=y−3 and final x=7, backward reasoning gives original x=4. Original y is unconstrained because it is overwritten before relevant use. An intermediate value is not automatically an initial condition.

### 6. Preserve old values in simultaneous updates

Mathematical tuple assignment evaluates right-hand expressions in the old state. Sequential code needs an ordering or saved values that implements that transformer. In Euclid, compute the old remainder before replacing the first operand. In fast power, the odd accumulator multiplication needs the old base.

### 7. Include expression-definedness in the precondition

Division requires a nonzero divisor in the intended model. Array access requires a valid index at the actual read checkpoint. A signed overflow is not a harmless algebraic value under C semantics. A formal substitution that admits an undefined expression is not a safety proof.

### 8. Split conditionals by their guards

Each branch contributes its own guarded admissible region. For negation below zero and addition of two otherwise, final x≥3 admits x≤−3 or x≥1. Combining only one branch gives a stronger condition; accepting x merely nonzero admits failures. Equality boundaries must follow the actual guard.

### 9. Strengthen preconditions and weaken postconditions in consequence

From a proved triple, a stronger input restriction and a weaker output promise remain justified when the corresponding implications hold. Reversing either implication invents a new guarantee. The rule applies to the stated correctness interpretation and does not add termination to a partial-correctness triple.

### 10. Distinguish valid addresses from nonaliasing

Two valid indices may denote the same cell. Writing A[i]=1 and then A[j]=2 can satisfy both desired final equalities only if i≠j. Ordering i<j is sufficient but unnecessarily strong. Array updates must explicitly describe which cells change and which retain their values.

### 11. Separate reachable truth from inductiveness

A predicate can hold on all reachable states but fail preservation from an unreachable state it admits. Conversely, x≥0 can be inductive but too weak to imply x=y. Check initialisation, preservation over all invariant states, and the exit implication independently; do not conflate their failure modes.

### 12. An invalid annotation does not automatically refute the program

A loop with a false guard can terminate correctly even when its proposed invariant is false initially. That annotation is unusable, but the program may have another valid proof. Report which obligation fails instead of labeling every failed assertion a functional bug.

### 13. A preserved relation does not prove termination

With divisor zero, X=qY+r is preserved while the remainder never decreases and the guard remains true. Supply a well-founded progress measure under the required input restrictions. Repeating a conservation equation cannot supply the missing strict descent.

### 14. A decreasing real value can support an infinite run

The sequence $2^{-k}$ strictly decreases but stays positive for every finite k. A limit is not a reached state. Use a well-founded range, usually naturals or a lexicographic product of naturals, and prove strict decrease on every guarded transition.

### 15. Termination need not imply a uniform nondeterministic bound

A transition can choose any finite reset B and then terminate after B decrements. Every chosen run is finite, but no single bound covers all unrestricted B. A lexicographic proof establishes termination; a runtime claim needs additional quantitative restrictions.

### 16. Fix half-open or closed intervals before updating endpoints

The lower-bound loop here uses [lo,hi). Midpoint elimination is lo=mid+1 on a below-target key and hi=mid otherwise. Replacing lo by mid can leave a singleton unchanged. Closed-interval formulas cannot be mixed with these updates without a new invariant.

### 17. Lower bound and equality search answer different questions

Lower bound returns the first position with value at least the target, even if no equal value exists. Returning n is a valid insertion-position result. Dereference only after checking that the position is inside the array and, when needed, that its value equals the target.

### 18. Sortedness supplies the regional implication

From A[mid]<target, the loop eliminates earlier entries only because the predicate is monotone. Numeric endpoint bounds and termination can still hold on an unsorted input while the result is wrong. Check the premise used for each inference, not just the mechanics of the loop.

### 19. Handle duplicate thresholds deliberately

Lower bound moves equality into the upper classified region; upper bound moves equality into the lower one. Their difference counts occurrences. In [1,2,2,2,5], the two boundaries for 2 are 1 and 4, so the count is three, not the final matching index.

### 20. Derive exact widths rather than saying “half”

For length L, the two remainders are floor(L/2) and L−floor(L/2)−1. Their maximum is floor(L/2). This gives a worst body count ceiling(log₂(n+1)) for the stated lower-bound routine. The final false guard evaluation is not another body execution.

### 21. Name the operation being counted

Insertion shifts, key comparisons, final saved-key writes, merge head comparisons, recursive calls, and guards are different quantities. For [4,2,3,1], five shifts equal five strict inversions; that does not mean every implementation has only five comparisons or writes. Derive the counter from the written instruction.

### 22. A logical hole is excluded from the conserved array multiset

After shifting 4 in [1,4,2], physical [1,4,4] is not a permutation. Excluding the hole and adding the saved 2 restores logical conservation. Include the saved record once, not twice. The final placement closes the representation gap.

### 23. Test stability using record identities

Equal keys can appear numerically unchanged while their records reverse. Strict greater-than insertion preserves earlier equal records; greater-than-or-equal insertion can reverse them. A key-only sortedness proof does not establish the stronger stable-record contract.

### 24. Exhausted merge inputs require a separate path

Compare two heads only while both are valid. Once a run is exhausted, copy the remaining sorted suffix without another head comparison. Two nonempty lengths a,b have at most a+b−1 such comparisons; an empty run has zero. Stability requires the correct equal-head priority.

### 25. Recursive hypotheses must cover all promised properties

For sorting, each child must return an ordered permutation, not merely an ordered array. Prove that stronger child contract at the bases and induction step. A runtime bound or an order-only hypothesis cannot recover values that the children discarded.

### 26. The base region must cover every admitted boundary

Returning only at size one leaves empty merge sort recursing on size zero forever. A size-at-most-one base and proper smaller splits support the natural termination proof. Excluding empty input is an alternative contract, but it is not a repair of a routine advertised to admit it.

### 27. Partition regions specify boundaries, not complete sorting

In three-way partition, [0,lt) is smaller, [lt,i) equal, [i,gt) unknown, and [gt,n) greater. The returned pair describes the final equal block. Internally unsorted unequal regions can satisfy the contract, so do not add an unproved full-order or stability guarantee.

### 28. Do not skip a key swapped in from the unknown region

The greater-key branch decreases gt and swaps a new unknown entry into index i. Leave i unchanged until that incoming entry is classified. For [3,1] and pivot 2, advancing i too soon yields a false equal region even though the displayed array is sorted.

### 29. Count logical consumption, not distinct physical indices

Each three-way body reduces gt−i by exactly one, giving n executions. Repeated inspection of index i does not make the algorithm quadratic because the unknown width still decreases. The number of comparisons inside a body depends on its branch structure.

### 30. Division needs conservation and a remainder range

X=qY+r alone allows many invalid quotient–remainder pairs. With Y>0, nonnegative r and the false exit guard give 0≤r<Y, establishing Euclidean division. At (47,6), seven subtractions yield (7,5); the pair (6,11) preserves conservation but is not a valid final division result.

### 31. Euclid's proof uses old operands and a smaller remainder

The common-divisor sets of (a,b) and (b,a mod b) are equal. The new remainder lies below positive old b, establishing progress. Replacing a first and then computing a%b destroys that identity. Count the final transition to a zero second coordinate.

### 32. Fast-power counts follow bits and the exact code

For a positive exponent, bitlength counts processed iterations and popcount counts odd-branch accumulator multiplications. A square written in the final body still counts and still needs safety, even if its result is unused. For exponent 45, these counts are six and four, respectively.

### 33. Normalize modular output even on the zero-exponent path

For modulus one, the canonical residue of one is zero. Initializing the accumulator to literal one returns an out-of-range result when no body executes. Use 1 mod M under M>0, and define the exponent-zero convention explicitly.

### 34. Reduction after a lost product cannot repair overflow

Under the stipulated eight-bit product, 200×200 wraps to 64; exact reduction modulo 251 gives 91 instead. A later modulus sees only the stored 64. Real expression promotions and signed semantics need their own audit; small variable declarations alone do not prove a small product type.

### 35. A sorting index certificate needs three checks

Check an index permutation, output-value consistency, and increasing original indices within equal-key blocks for stability. For [5,1,5], [1,0,2] certifies the stable output [1,5,5], while [1,2,0] does not. Verify output order separately rather than assuming it from index uniqueness.

### 36. A feasible optimum candidate needs a matching universal bound

For minimisation, a feasible cost 17 supplies an upper bound, and a proof that every feasible cost is at least 17 supplies a lower bound. Equality establishes optimal value 17, but not uniqueness. Confirm that the witness and bound use the same objective and domain.

### 37. Graph certificates must check all edges and rooted witnesses

Edge inequalities telescope to a lower bound on each path cost. A path attaining the label supplies the opposite bound. Checking only parent edges misses shortcuts, and local parent equalities can hide a zero-weight cycle disconnected from the source in the parent structure. Root reachability is a separate obligation.

### 38. Negative edges and negative cycles have different implications

A negative edge can coexist with valid finite distances and a sound certificate. A negative-total cycle makes the sum of its edge inequalities impossible for finite labels. Reachability determines the source-distance effect; do not reject every negative edge by importing a different algorithm's precondition.

### 39. Structural mass has a premise-dependent equality case

For all leaves of a finite binary tree, the mass sum is at most one, with equality exactly for a full tree. Depths 1,2,3 give 7/8 and refute fullness when that is the complete leaf set. An incomplete sample of leaves cannot support the same structural conclusion.

### 40. Complete a sum invariant with index bounds

The odd-sum relation s=(k−1)² is preserved by adding 2k−1 and increasing k. Bounds 1≤k≤n+1 plus the false guard force final k=n+1 and s=n². The equality alone cannot establish the final index or termination. Check n=0 before claiming a formula for every admitted input.

### Final method selection

Use backward substitution for exact preimages of assignments; induction on checkpoints for loops and state machines; strong induction plus a complete child contract for recursion; a well-founded measure for termination; a representation invariant for pending or moved data; and a bound plus an attaining witness for optimality. Combine these methods when the contract has several obligations. A counterexample refutes a universal claim, while a finite successful test suite only checks its sampled domain. The explicit proofs and their declared premises remain the general argument.
