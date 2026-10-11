## Complete operation-counting rules and examination traps

### 1. Name the operation being counted

Body calls, key comparisons, guard predicates, assignments and output writes are different quantities. Give the requested ledger first; add other ledgers only when translating that count into full runtime under an explicit cost model.

### 2. State the domain and arithmetic semantics

Declare nonnegative or positive integer sizes, independent parameters and enough counter capacity. A terminating mathematical-integer loop may wrap or overflow in a concrete language. Its iteration theorem does not automatically transfer to the changed semantics.

### 3. Count the final false guard

A normal pretest invocation with $q$ bodies has $q+1$ header evaluations. In a nested loop, add one such final test per inner invocation, including empty rows. A break from inside a body removes the normal final false header test for that invocation.

### 4. Charge initialization per invocation

An inner loop initialized on every outer row incurs one initialization per row, not per inner body. At zero-size input, setup and a false outer guard can remain even when the chosen body count vanishes.

### 5. Inspect continue and update placement

A conventional C-style for-loop continues to its update expression after `continue`. A while-loop update placed later in the body can be bypassed, creating a repeated state and nontermination. The fragments' control flow determines the count.

### 6. Count short-circuit predicates separately

In `P and Q`, the right predicate is evaluated only when the left is true. Its final failed evaluation depends on which predicate ends the loop. A composite condition is not necessarily one constant-cost operation.

### 7. Write the index region

Independent bounds create a rectangular region; dependent bounds require row sums or another exact partition. Replacing all rows by their maximum supplies an upper estimate, not generally an exact count or a matching lower bound.

### 8. Retain inclusive and strict endpoints

Starting at zero with fixed positive step $d$, the guard `j<M` gives $\lceil M/d\rceil$ visits, while `j<=M` gives $\lfloor M/d\rfloor+1$. Changing one endpoint can affect every row in a nested program.

### 9. Distinguish weak and strict order

Strict triples count $\binom n3$, weak triples count $\binom{n+2}{3}$, and $i\le j<k$ counts $\binom{n+1}{3}$. Shift to strict positions and construct the inverse map to justify each formula rather than guessing a factorial division.

### 10. Check equality cases explicitly

Weak triples split into all-distinct, exactly-two-equal and all-equal cases. Their counts are $\binom n3$, $2\binom n2$ and $n$. Equality cases contribute $n^2$ additional triples and cannot be discarded in an exact question.

### 11. Use row increments as an independent check

A candidate finite count should gain exactly the newly admitted row when the size increases. For squared rows, the increment is $n^2$; for weak triples, it is the number of weak pairs at the new last index.

### 12. Derive power sums with uniform hypotheses

For fixed $p\ge0$, the last half of the terms proves $\sum_{i=1}^ni^p\in\Theta(n^{p+1})$. The witness constant depends on fixed $p$. If $p$ grows with input, that proof is not uniform and may conceal superpolynomial work.

### 13. Distinguish geometric stages from their work

The values $1,2,4,\ldots,2^h$ give $h+1$ visits. Charging the current value per visit gives $2^{h+1}-1$ operations. A logarithmic stage count alone does not determine total work.

### 14. Define the size parameter for exponent schedules

Work $2^{n+1}-1$ is exponential in maximum exponent $n$ but linear in final numerical scale $N=2^n$. Neither description is meaningful without naming the input measure and representation.

### 15. Solve multiplicative guards algebraically

With positive start $a$ and fixed multiplier $b>1$, inclusive bound $M$ gives $\lfloor\log_b(M/a)\rfloor+1$ visits when $a\le M$. If the start already exceeds the bound, the count is zero; logarithmic formulas must respect this case.

### 16. Treat zero-start multiplication as a progress defect

Doubling zero does not leave zero. A positive-bound loop started there can run forever. Establish termination before assigning any logarithmic runtime class.

### 17. Recheck squaring endpoints

Starting at two and squaring visits $2^{2^r}$. Inclusive bound $N\ge2$ gives $\lfloor\log_2\log_2N\rfloor+1$ visits; strict bound gives $\lceil\log_2\log_2N\rceil$. Big-integer multiplication cost is separate from this visit count.

### 18. Count divisibility by multiples

For fixed divisor $j$, exactly $\lfloor n/j\rfloor$ positive targets up to $n$ are multiples. Summing those rows counts successful branches; summing divisor counts by target counts the same finite set differently.

### 19. Preserve floors in exact answers

The successful divisor count is $D(n)=\sum_{j=1}^n\lfloor n/j\rfloor$. Fractional row lengths are not body visits. The uniform sandwich $(n/2)H_n\le D(n)\le nH_n$ proves growth without asserting an exact harmonic value.

### 20. A rare body does not remove its tests

An all-pairs divisibility implementation makes $n^2$ condition checks even though its successful body count is tight $n\log n$. Direct multiple stepping changes the implementation ledger while preserving the successful set.

### 21. Reverse a finite double count when useful

Starting from each positive index and doubling yields $\sum_{t\ge0}\lfloor n/2^t\rfloor$, not a tight $n\log n$ count. The exact identity is $2n-s_2(n)$, where $s_2(n)$ counts one-bits in the binary expansion.

### 22. A filtered triangle need not split equally

For $1\le j\le i\le n$ with even $i+j$, kept rows have $\lceil i/2\rceil$ positions and total $\lfloor(n+1)^2/4\rfloor$. The diagonal is entirely kept, so halving the unfiltered triangle gives the wrong exact count.

### 23. Count residues with the endpoint included

Skipping multiples of fixed positive $d$ through $M$ leaves $M-\lfloor M/d\rfloor$ bodies. A density approximation may hide the last partial block. With $d=1$, every index is skipped, so a positive linear success lower bound fails.

### 24. Expand a variable body into a weighted sum

If each visit $(i,j)$ costs $j$ unit actions, total work is $\sum_i\sum_jj$, not the number of visits. Integer weights can be interpreted as an extra counting index; otherwise bound the weighted sum directly.

### 25. Require uniform constants when summing costs

Summing a stated $\Theta(f(i))$ body cost requires uniform positive witnesses over the relevant calls. An $O(f(i))$ promise alone supplies only an upper bound and does not justify a tight total.

### 26. Separate input-specific counts from worst cases

A supplied merge array has one exact trace; alternating inputs attain a maximum. A worst-case upper bound need not equal the given instance's count. A maximum claim needs both an upper theorem and an attainable input family.

### 27. Monotone merge pointers give linear comparisons

For two nonempty inputs of lengths $p,q$, the maximum head-key comparisons are $p+q-1$. Appending a leftover sorted suffix needs no head comparison, but output materialization still writes $p+q$ keys.

### 28. Accumulated lengths determine sequential merging

With $k$ equal lists of length $m=n/k$, stage $j$ processes $jm$ keys. Summing gives tight $nk$ work for $k\ge2$. Balanced merging has a different schedule and tight $n\log k$ work; do not substitute its theorem for sequential code.

### 29. Distinguish a branch expectation from scan length

A random-permutation running minimum has expected update count $H_n$, derived by indicators and linearity. Every element is still compared. A fixed-array trace or a biased distribution does not automatically have that expectation.

### 30. Restrict a feasible region for lower bounds

For $ijk\le n$, enlarging a range proves an upper bound, while a square of small outer factors proves a lower bound. The resulting tight $n(\log n)^2$ count needs both arguments; counting a full cube ignores feasibility.

### 31. Retain independent size parameters and overhead

Initializing lengths $m,n$ and traversing all pairs has modeled work proportional to $1+m+n+mn$, including constant setup if the origin is part of the claim. Replace dimensions by one parameter only after establishing their relation.

### 32. Use finite checks to challenge, not certify, proofs

Check zero and one, endpoint powers and adjacent values, actual row increments and independently enumerated small regions. A successful finite trace illustrates its contract. General correctness and growth still require the explicit identities, invariant arguments or uniform bounds written in the solutions.
