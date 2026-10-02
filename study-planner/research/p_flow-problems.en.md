## Worked problems with complete reasoning

Every problem includes its assumptions, the reasoning path, and a reusable lesson. These are study examples with answers already provided. Read them after the teaching sections; there is no request to take a test before learning. Most problems are original. Where a university exercise family supplied a pattern, the attribution identifies that family, while parameters, formulation, explanation, and boundary analysis here are independently developed. The set covers this chapter's scalar control-flow boundary; array sorting, partitioning, merging, and reference-course exercises outside that boundary remain assigned to their later chapters.

### Problem 1. Separate conditions can both execute

**Original problem.** Find the final value for initial `x = 3`, then give the result for initial `x = 1`.

```c
if (x < 5) x += 4;
if (x > 5) x -= 2;
```

**Solution.** For 3, the first guard is true and changes `x` to 7. The second guard is evaluated afterwards against 7, so it too is true and leaves 5. For 1, the first assignment gives 5; `5 > 5` is false, leaving 5. There is no implicit exclusivity between the conditions. Replacing the second `if` by `else if` changes the result for initial 3 to 7, because its guard is skipped after the first branch executes. This example separates a syntactic priority chain from two sequential decisions about evolving state.

### Problem 2. A threshold classifier and its domain

**Course-pattern attribution:** Harvard CS50's mutually exclusive branch examples motivate interval classification; this specification and solution are original. Classify an integer `score` into invalid outside 0–100, low below 40, middle from 40 through 74, and high from 75 through 100.

```c
int category;
if (score < 0 || score > 100) category = -1;
else if (score < 40) category = 0;
else if (score < 75) category = 1;
else category = 2;
```

**Solution.** The first branch removes values outside the domain. On the next branch, previous falsity establishes 0 ≤ score ≤ 100, and `score < 40` identifies [0, 40). On the third branch, previous falsity adds score ≥ 40, giving [40, 75). The residual branch has score ≥ 75 and at most 100. Boundary checks −1, 0, 39, 40, 74, 75, 100, and 101 each select exactly the intended outcome. Writing a chain testing `score >= 40` before `score >= 75` would wrongly classify all high scores as middle. The correctness argument uses the accumulated path conditions, not only each guard in isolation.

### Problem 3. The nearest unmatched if

**Original problem.** Start with `r = 9`. Evaluate this fragment for pairs `(a,b)` equal to `(1,-1)`, `(-1,1)`, and `(1,1)`.

```c
if (a > 0)
    if (b > 0)
        r = 1;
    else
        r = 2;
```

**Solution.** The else belongs to the inner if. For `(1,-1)` the outer guard admits entry, the inner guard fails, and `r` becomes 2. For `(-1,1)` the outer guard fails; no inner statement executes, so `r` remains 9. For `(1,1)` both guards succeed and `r` becomes 1. A common incorrect answer gives 2 for the second pair by attaching the else to the outer if according to indentation. Add braces around the inner conditional if that is the intended grammar. Notice that the initial value matters on the path with no assignment; omitting its initialization would introduce an indeterminate-value issue when the result is later read.

### Problem 4. A null statement defeats apparent indentation

**Course-pattern attribution:** Princeton §1.3's spurious-semicolon exercise family. This fragment and reasoning use different values and C17 semantics.

```c
int x = 1, y = 8;
if (x > y);
{
    x = 6;
    y = 2;
}
```

**Solution.** The controlled statement is `;`, so the condition has no useful side effect here. The following block is a separate statement and executes unconditionally. Final values are `x = 6` and `y = 2`. Removing the semicolon changes the grammar: now the block is controlled, and because the original condition is false, values stay 1 and 8. To diagnose such a question, identify the immediate substatement before calculating any branch result. Whitespace can mislead a human, but C syntax is determined by tokens.

### Problem 5. Chained comparisons do not form an interval

**Original problem.** Determine whether `if (2 < x < 8)` distinguishes the interval 3 through 7 for integer `x`.

**Solution.** Relational operators group left to right. `2 < x` yields integer 0 or 1. Both 0 and 1 are below 8, so the complete guard is always true, even for −100 or 100. The correct C interval test is `2 < x && x < 8`. The latter admits precisely integers 3, 4, 5, 6, and 7. This is not a defect in precedence; it is an incorrect transfer of mathematical chained-inequality syntax into C. In Python, `2 < x < 8` has dedicated chained-comparison semantics, so the language must be established first.

### Problem 6. Sequenced short-circuit state changes

**Original problem.** Evaluate the final `i` and `r`.

```c
int i = 1, r = 0;
if (i++ == 0 || ++i == 3) r = i;
```

**Solution.** The first comparison uses old value 1, fails, and leaves `i = 2`. A false first operand of `||` allows the second operand to execute. Prefix increment leaves 3 and compares 3 to 3, true. The body reads that completed state and assigns 3 to `r`. Final values are `(3,3)`. If initial `i` were 0, the first operand would be true and leave 1, the second increment would be skipped, and the body would assign 1. These are defined evaluations because short-circuit operators sequence their operands. Replacing `||` by bitwise `|` would create unsequenced modifications and invalidate numerical output reasoning.

### Problem 7. Build a division guard that actually protects

**Original problem.** For a declared 32-bit two's-complement signed `int`, construct a guard before evaluating `a / b`, rejecting precisely zero divisor and the unrepresentable minimum divided by −1.

```c
if (b == 0 || (a == INT_MIN && b == -1)) {
    valid = 0;
} else {
    quotient = a / b;
    valid = 1;
}
```

**Solution.** On the else path, `b != 0` is known and the special pair is excluded. All other signed-int quotients in this declared model are representable. The guard itself uses only comparisons and logical operations, so it cannot divide first. Cases `(8,0)` and `(INT_MIN,-1)` are rejected; `(INT_MIN,1)` and `(17,-3)` are accepted, with quotients INT_MIN and −5 respectively. Checking `a / b` before checking `b` defeats the protection. The minimum-overflow pair depends on the specified signed range; the chapter does not silently substitute this asymmetric model for every C17 implementation.

### Problem 8. Default is an entry label in the middle

**Original problem.** Find `r` for tags 1, 2, 3, and 4.

```c
int r = 0;
switch (tag) {
case 1: r += 1;
default: r += 4;
case 2: r += 8; break;
case 4: r += 16;
}
```

**Solution.** Tag 1 enters at the first label and falls through two additions, producing 13. Tag 2 enters at its label and yields 8. Tag 3 has no matching case, so it enters at default and yields 12. Tag 4 yields 16 and reaches the end. The values of unselected cases do not prevent their statements from executing after fallthrough. Moving default to the bottom would change the results unless transfers are also changed. Treat dispatch and subsequent sequential execution as two distinct phases.

### Problem 9. Case constants and converted duplicates

**Original problem.** Explain the problems with these two independent switch sketches in C17.

```c
const int limit = 3;
switch (x) { case limit: break; }
```

```c
switch (u) { case -1: break; case UINT_MAX: break; }
```

**Solution.** In the first, an ordinary `const int` object is not an integer constant expression, so it does not provide a valid case label. An enumeration constant such as `enum { limit = 3 };` can supply the intended constant. In the second, assume `u` has type `unsigned int`. Its promoted controlling type is still unsigned int. Converting −1 to that type produces UINT_MAX, duplicating the second converted case value. Duplicate case values violate a constraint even if the source tokens look different. Labels must be compared after the standard's required conversion, not by textual spelling or mathematical signed value.

### Problem 10. Continue crosses a switch, break does not

**Original problem.** Determine final `sum` and the body values that reach the last assignment.

```c
int sum = 0;
for (int i = 0; i < 5; ++i) {
    switch (i) {
    case 1: continue;
    case 3: break;
    default: sum += i;
    }
    sum += 10;
}
```

**Solution.** At `i = 0`, default adds zero, then 10. At 1, continue targets the enclosing for, bypassing the bottom assignment but still executing the header increment. At 2, default adds 2 and the bottom adds 10. At 3, break exits only the switch, so the bottom adds 10. At 4, default adds 4 and the bottom adds 10. Total is 46. The bottom is reached for indices 0, 2, 3, and 4. A trace that stops the entire loop at 3 confuses the target of break; a trace that skips the update at 1 confuses continue with break.

### Problem 11. A visible declaration can have a skipped initializer

**Original problem.** Diagnose this fragment instead of inventing an output.

```c
int result = 0;
switch (tag) {
    int temporary = 7;
case 1:
    result = temporary;
    break;
default:
    result = 0;
}
```

**Solution.** Dispatch to case 1 bypasses the initializer. The automatic local is in scope, but no executed statement established its value. Reading it as if it contained 7 is unjustified and can cause undefined behavior through an indeterminate value. The default route does not read it, so this defect is path-dependent. Move the declaration inside a block after the label, as shown in the teaching section. Initialization is an executed operation. Scope alone does not prove it happened, and assigning a different variable named `temporary` outside this block would not initialize this inner object.

### Problem 12. Three loop forms at an empty boundary

**Original problem.** Begin each independent fragment with `i = 0`, `sum = 0`, and `n = 0`.

```c
while (i < n) { sum += i; ++i; }
```

```c
do { sum += i; ++i; } while (i < n);
```

```c
for (i = 0; i < n; ++i) { sum += i; }
```

**Solution.** The while and for guards fail immediately. Their bodies execute zero times; both finish with `(i,sum) = (0,0)`. The do-loop executes once, adding zero and increasing `i` to 1 before its false test; it finishes `(1,0)`. Equal sums conceal different state and execution counts. With start `i = 2`, the do-loop instead finishes `(3,2)`, while the while-loop leaves `(2,0)`. Choose a posttest loop for a required initial attempt, not merely because its layout seems shorter.

### Problem 13. A false postfix guard still changes state

**Original problem.** Trace this loop and count guard evaluations.

```c
int i = 0, sum = 0;
while (i++ < 3) sum += i;
```

| Guard uses old `i` | Guard result | `i` after guard | `sum` after possible body |
|---|---|---|---|
| 0 | True | 1 | 1 |
| 1 | True | 2 | 3 |
| 2 | True | 3 | 6 |
| 3 | False | 4 | 6 |

**Solution.** Final values are `i = 4` and `sum = 6`. There are three body entries but four guard evaluations. Replacing postfix by prefix gives only two entries, accumulating 1 + 2 = 3 and exiting with `i = 3`. The table explicitly includes the failed guard because it performs a side effect. Recording only successful iterations loses necessary information about the exit state.

### Problem 14. A for-continue preserves the update

**Original problem.** Determine the sum and exit index.

```c
int i, sum = 0;
for (i = 0; i < 6; ++i) {
    if (i % 2 == 0) continue;
    sum += i;
}
```

**Solution.** Body entries occur at indices 0 through 5. Even entries go directly to `++i`; odd entries add 1, 3, and 5, then also execute the update. The sum is 9, and final `i` is 6. Six updates and seven tests occur. The continuation guard does not remove an iteration from the execution count; it removes only selected work within that entry. Thus the number of accumulator updates is three while the number of loop updates is six. Specify which operation is being counted.

### Problem 15. A tempting while rewrite creates a cycle

**Original problem.** Explain the behavior of this rewrite of Problem 14.

```c
int i = 0, sum = 0;
while (i < 6) {
    if (i % 2 == 0) continue;
    sum += i;
    ++i;
}
```

**Solution.** At the first guard, `i = 0`, so the body is entered. The even test succeeds and continue returns directly to the while guard. The manual increment is skipped; state remains `(0,0)`. The same deterministic source state repeats. The intended progression never occurs. For source-level semantics this is a cycle; for an otherwise nonobservable loop, the separate optimizer termination permission must also be remembered before claiming portable runtime behavior. A repair places `++i` on every continuing path, or keeps the original for-loop. Copying the for-update to the bottom is not an equivalence proof.

### Problem 16. Break removes the last update and last failed test

**Original problem.** Count body entries, guard tests, and updates.

```c
int i, sum = 0;
for (i = 0; i < 8; ++i) {
    if (i == 3) break;
    sum += i;
}
```

**Solution.** Entries occur at 0, 1, 2, and 3. The last entry breaks before accumulation. The sum is 3, and `i` remains 3. Guard tests occur four times, all true; the for-update occurs only three times. There is no later false guard. The invariant “sum contains all processed earlier indices” at the break point yields 0 + 1 + 2, not a sum including 3. The body-entry count is four even though only three entries reach the accumulator. Off-by-one errors often come from conflating entry, completed body, and processed element.

### Problem 17. Continue in a do-loop still reaches its test

**Original problem.** Find the result.

```c
int i = 0, sum = 0;
do {
    ++i;
    if (i % 2 == 0) continue;
    sum += i;
} while (i < 5);
```

**Solution.** After each initial increment the body sees 1 through 5. Even values skip accumulation but still reach `i < 5`. Odd values 1, 3, and 5 accumulate, so sum is 9 and final `i` is 5. There are five body entries and five tests. If the increment were below the continue, an even entry could repeat unchanged. The posttest form does not grant an implicit increment; its continuation target is merely the trailing test.

### Problem 18. Inner break does not stop the outer body

**Original problem.** Evaluate the total.

```c
int total = 0;
for (int i = 1; i <= 3; ++i) {
    for (int j = 1; j <= 4; ++j) {
        if (j == i) break;
        ++total;
    }
    total += 10;
}
```

**Solution.** At outer index 1, the inner loop breaks on its first entry and adds zero. At 2 it adds once for `j = 1`. At 3 it adds twice for `j = 1,2`. The outer bottom assignment executes after every inner break and contributes 30. Final total is 33. Inner body entries count 1 + 2 + 3 = 6, while inner increments of total count 0 + 1 + 2 = 3. If the intended task were to exit both loops at the first equality, a single unlabeled break would be insufficient in C17.

### Problem 19. Prove an exact nested count

**Original problem.** For mathematical nonnegative `n`, with C updates and `count` representable, count this operation.

```c
int count = 0;
for (int i = 0; i < n; ++i)
    for (int j = 0; j < i; ++j)
        ++count;
```

**Solution.** Fix the outer index `i`. The inner body sees precisely 0 through `i - 1`, giving `i` increments. Outer indices range from 0 through `n - 1`. Therefore:

<div class="formula-block"><math display="block"><mrow><mi>count</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></munderover><mi>i</mi><mo>=</mo><mfrac><mrow><mi>n</mi><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac></mrow></math></div>

For zero or one the count is zero; for four it is six. The empty inner loop at `i = 0` still evaluates its guard once. If counting inner guard evaluations, add one per outer entry, producing n(n + 1)/2. This demonstrates why a count must name its operation and why a nested structure does not automatically imply exactly n squared executions.

### Problem 20. A loop-local variable starts fresh

**Original problem.** Predict the total and explain the scope of `i`.

```c
int i = 99, total = 0;
for (int i = 0; i < 3; ++i) {
    int x = 2;
    total += x++;
}
```

**Solution.** The header introduces an inner `i` hiding the outer one. Its values 0, 1, and 2 control three entries. Each body creates and initializes `x` to 2. Postfix increment contributes 2, then changes the local to 3, whose lifetime ends with the iteration. Total is 6; after the loop the visible outer `i` is still 99. A model that carries `x` as 2, 3, then 4 across iterations would require a different declaration placement or storage duration. The identity of each object is part of the state, not just its name.

### Problem 21. Positive-step count with an exclusive endpoint

**Original problem.** How many times does the body execute, and what is the final `i`?

```c
int i;
for (i = 4; i < 23; i += 5) {
    /* body does not alter i */
}
```

**Solution.** Body indices are 4, 9, 14, and 19. The next update yields 24, whose guard fails. Count is ceiling((23 − 4)/5) = ceiling(19/5) = 4. Final `i` is 24, not 23. With guard `i <= 24`, one extra body entry occurs at 24, then final index becomes 29. Under a mathematical progression proof all values are safe here for every conforming `int`. In general, use the formula only after checking that the last update is representable and that no body path changes the progression.

### Problem 22. Inclusive descent and overshoot

**Original problem.** Count `for (i = 20; i >= 3; i -= 4)` under signed integer arithmetic where all shown values fit.

**Solution.** The body sees 20, 16, 12, 8, and 4. The next update yields 0, which fails the guard. Count is floor((20 − 3)/4) + 1 = 5. Final index is 0. A variant such as ceiling((i − 2)/4) on true-guard states is a positive integer that decreases each iteration. Simply using `i - 3` as a nonnegative variant at every checkpoint fails at the final false checkpoint, although nonnegativity is needed only on the appropriate continuation domain for the termination argument. Be precise about where the variant claim is required.

### Problem 23. Construct and prove summation

**Original problem.** Derive a loop that computes the sum of odd integers from 1 through `2*n - 1` for `0 <= n <= 100`, using no multiplication in its body.

```c
int i = 0, odd = 1, sum = 0;
while (i < n) {
    sum += odd;
    odd += 2;
    ++i;
}
```

**Solution.** At each guard use invariant 0 ≤ i ≤ n, `odd = 2*i + 1`, and `sum = i*i`, interpreted as mathematical relationships. Initialization satisfies all three. Under `i < n`, adding the next odd value gives i² + 2i + 1 = (i + 1)². Updating odd by two and index by one restores the relationships for the next checkpoint. Variant n − i decreases strictly and is nonnegative. Exit gives i = n and sum n². With the bound 100, sum is at most 10000, odd is at most 201, and all body arithmetic fits every C17 `int`. The proof relationships need not be computed as multiplications in the program.

### Problem 24. An invariant that is true but insufficient

**Course-pattern attribution:** Cornell CS2110's emphasis on explicit processed-region invariants. The scalar counterexample and proof below are original.

Consider `i = 0; sum = 0; while (i < n) { sum += 2; ++i; }` for `0 <= n <= 100`. Does invariant `0 <= i && i <= n` prove the final sum is n?

**Solution.** The bound is initialized and preserved, and it proves `i = n` at normal exit. It says nothing about sum. The actual stronger invariant is `sum = 2*i`, which follows from the update and gives sum 2n. For n = 3 the result is 6, so the desired postcondition is false. A valid invariant cannot imply a false result when combined with valid termination facts; the missing relationship is the diagnostic. An invariant should connect the output accumulator to the processed work rather than only state index bounds.

### Problem 25. Break needs a separate proof exit

**Original problem.** For `0 <= n <= 100`, compute the largest prefix sum not exceeding budget `b`, where `0 <= b <= 10000`.

```c
int i = 0, sum = 0;
while (i < n) {
    if (sum + (i + 1) > b) break;
    ++i;
    sum += i;
}
```

**Solution.** At the guard, sum is the sum of 1 through i and does not exceed b. The maximum speculative sum is at most 5050 under the bounds, so the guard arithmetic fits a conforming int. If a break occurs, adding the next value would exceed b, so the current feasible prefix is maximal. If normal guard exit occurs, i = n and all available values fit the budget. Variant n − i decreases on every continuing iteration. For n = 10 and b = 12, successive accepted sums are 1, 3, 6, 10; the next candidate 15 fails, leaving i = 4 and sum = 10. The postcondition is a disjunction: exhausted input or next prefix is infeasible. It is wrong to infer i = n merely because the loop ended.

### Problem 26. Euclid's old values must survive

**Original problem.** Trace the Euclid loop for initial A = 84, B = 30, and diagnose a two-assignment replacement.

| Guard pair `(a,b)` | Remainder | Next pair |
|---|---|---|
| (84,30) | 24 | (30,24) |
| (30,24) | 6 | (24,6) |
| (24,6) | 0 | (6,0) |

**Solution.** The false guard at `(6,0)` stops before any remainder with divisor zero. The invariant gcd preservation gives result 6; the second component decreases 30, 24, 6, 0, proving termination. Replacing the body by `a = b; b = a % b;` changes the first pair to `(30,0)` immediately and returns 30, because the second assignment sees the new `a`. A temporary is needed for the original remainder. Simultaneous mathematical assignment and sequential C assignment have different semantics unless old values are explicitly preserved.

### Problem 27. Decimal digit accumulation, including zero

**Original problem.** For an unsigned input N, compute its decimal digit sum. Explain whether a while-loop and a do-loop differ at N = 0.

```c
unsigned int rest = N, sum = 0;
while (rest != 0u) {
    sum += rest % 10u;
    rest /= 10u;
}
```

**Solution.** The remainder extracts the least significant digit, and quotient removes it. For 5072 the successive `(rest,sum)` checkpoints are `(5072,0)`, `(507,2)`, `(50,9)`, `(5,9)`, `(0,14)`. The invariant says sum contains the removed digits' sum and rest contains the unprocessed prefix. A positive rest strictly decreases when divided by ten; no zero divisor is involved. The sum is bounded by N for positive N, so its accumulation fits unsigned int without wrap. For zero, the body executes zero times and the digit sum is zero. A do-loop also yields zero but makes one entry. If the task is digit **count**, zero conventionally has one decimal digit, so the entry-count difference matters and must be handled explicitly.

### Problem 28. Signed overflow is not another loop iteration

**Original problem.** Does this loop have a defined final `i` on a 32-bit two's-complement signed-int machine?

```c
for (int i = 0; i <= INT_MAX; ++i) {
    /* no early exit */
}
```

**Solution.** The index reaches INT_MAX, and that guard is true. After the body the update attempts INT_MAX + 1, which is outside the type's range. Signed overflow is undefined; no defined wrapped negative value or normal final state follows. If the requirement is to process every value through INT_MAX, a safe structure processes the current value, checks `i == INT_MAX` and breaks, then increments only otherwise. An exclusive bound `i < INT_MAX` avoids overflow but omits the last value, so it repairs a different specification. Safety and task coverage must both be checked.

### Problem 29. Unsigned reverse counting has a false stopping idea

**Original problem.** Compare `for (unsigned int i = 3; i >= 0u; --i)` with a safe reverse traversal of three positions.

**Solution.** Every value of unsigned int is at least zero, so the guard can never fail. The abstract sequence is 3, 2, 1, 0, UINT_MAX, and so on; decrementation is defined modulo the unsigned range. If the loop has no observable actions, optimizer assumptions add another reason not to use it as a runtime timing experiment. A safe version initializes `i = 3`, loops while `i > 0u`, and decrements at the start of the body. Its processed positions are 2, 1, 0 and its exit value is zero. Merely changing `>=` to `>` in the original loop would process 3, 2, 1, a different set of positions.

### Problem 30. Equality exit can be unreachable in a modular cycle

**Original problem.** In a declared abstract four-bit unsigned model, start at zero and add six modulo 16 on each iteration. Can an equality guard ever reach target 5? What about target 10?

**Solution.** gcd(16,6) = 2. Every reachable residue is even, so 5 is unreachable. The complete cycle is 0, 6, 12, 2, 8, 14, 4, 10, then 0. Target 10 is reached after seven updates. The cycle length is 16/2 = 8. This is a deliberately small mathematical model, not a claim that C17 offers a four-bit unsigned int. The congruence analysis transfers to an actual specified unsigned modulus. A source loop stopping only on target 5 lacks a termination argument even though its update is defined.

### Problem 31. Fractional updates to an integer can stagnate

**Course-pattern attribution:** Princeton §1.3's fractional compound-update trap. Parameters and C reasoning are independently developed.

```c
int x = 0;
while (x < 4) {
    x += 0.25;
}
```

**Solution.** The addition uses a floating operand; the compound assignment converts the result back to int. Starting at zero, 0.25 is representable in the floating model and truncates to integer zero on assignment. The same state recurs, so the source progression does not advance. This is not signed overflow and is not a compiler syntax error. Use an integer iteration counter when counting quarters, or use a suitable floating variable with an explicit numerical termination argument. Java's compound-assignment rule is similar in this example, but that similarity does not establish identical language semantics for every update or arithmetic boundary.

### Problem 32. A floating step can disappear

**Original problem.** In binary64 with round-to-nearest ties-to-even and stored binary64 results after each assignment, consider `x = 2^53` and repeatedly execute `x = x + 1`. Does a guard `x < 2^53 + 4` guarantee progress?

**Solution.** Adjacent representable values at this magnitude are spaced by 2. The exact sum 2^53 + 1 is halfway between 2^53 and 2^53 + 2. Ties-to-even selects 2^53, so the stored value does not change. The guard remains true and the same state repeats in this declared model. Extra intermediate precision, a different rounding mode, or different storage rules could change the analysis, so the assumptions are part of the problem. A real-number proof that adding one strictly increases x does not apply automatically to floating state. Count iterations with an integer when the task is discrete, and separately analyze the numerical value being generated.

### Problem 33. Python range binds successive iterator values

**Course-pattern attribution:** MIT 6.0001 Lecture 2's range-and-accumulator examples. This mutation experiment and explanation are original.

```python
total = 0
for i in range(2, 8, 2):
    total += i
    i = 100
```

**Solution.** The iterator supplies 2, 4, and 6 on successive entries. Assigning 100 to the loop variable does not mutate the range iterator. Total becomes 12, and after the final body `i` is 100. A C loop `for (i = 2; i < 8; i += 2)` whose body sets `i = 100` would instead update to 102 and end after one body entry, giving total 2. Python's range excludes its stop and can use a negative step; it is not generally described by “stop minus one” when the step is not one. Establish iterator semantics before transferring a counting formula.

### Problem 34. A comma guard discards its first truth value

**Course-pattern attribution:** Cambridge Programming in C Lecture 1's comma-controlled loop question. This repaired specification uses initialized int variables and safe bounds.

```c
int i = 0, j = 0, count = 0;
for (; i < 2, j != 5; ++i, ++j) {
    ++count;
}
```

**Solution.** The comma operator evaluates `i < 2` then discards its value; the guard's value is `j != 5`. Thus the loop executes five times and exits with `i = j = count = 5`. The update's comma sequences both increments. Replacing the guard comma with `&&` yields only two entries and final values 2. Leaving `j` uninitialized would invalidate the trace before any useful count. Cambridge's original uses a character-type setting that also raises signedness and narrowing issues; this version isolates the control rule before introducing those representation boundaries later.

### Problem 35. Ordinary entry is an assumption

**Original problem.** Explain why this fragment enters a while body whose guard would initially be false.

```c
int i = 0, visits = 0;
goto work;
while (i < 0) {
work:
    ++visits;
    ++i;
}
```

**Solution.** The jump reaches the labeled statement directly and bypasses the initial test. It increments visits to 1 and i to 1. On normal body completion, control returns to the guard, which now fails. These values are the defined result in this fragment. No variably modified declaration is entered illegally. The familiar pretest-loop body count of zero for an initially false guard assumes control reaches the loop through its standard entry. An invariant established only on that entry would need an additional proof at this jump edge. Avoiding such entry paths makes structured code easier to reason about.

### Problem 36. Integrated trace and proof under continue and break

**Original capstone.** For `0 <= n <= 100` and `0 <= budget <= 10000`, sum positive odd values below n without exceeding budget. Prove the result is the maximal accepted prefix of those odd values.

```c
int i, sum = 0;
for (i = 0; i < n; ++i) {
    if (i % 2 == 0) continue;
    if (sum + i > budget) break;
    sum += i;
}
```

**Solution.** At each guard, `sum` equals the sum of all odd nonnegative indices already encountered below `i`, and `sum <= budget`. Initialization holds because the processed interval is empty. On an even entry, continue adds nothing and the header increment moves the boundary; the same sum correctly covers the enlarged interval because the added index is even. On an odd accepted entry, adding `i` extends the sum by precisely the newly processed odd value, and the header increment restores the checkpoint relationship. The bound on inputs ensures every speculative sum and update is safely representable.

If an odd entry breaks, its addition would exceed budget; all later candidate odd values are positive, so a longer prefix cannot fit. If the guard fails, every candidate below n has been considered. Variant n − i decreases on every edge returning to the guard, including continue, while break ends immediately. For n = 12 and budget = 18, accepted values are 1, 3, 5, 7, giving 16; the attempt at 9 would give 25, so exit has `i = 9`. This proves a prefix optimum, not an arbitrary subset optimum: skipping an unaffordable odd value and choosing a different subset is a different specification.
