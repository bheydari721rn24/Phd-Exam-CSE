## Scope, prerequisites, and reviewed sources

This chapter teaches how to determine which statement executes next, how to construct correct branches and loops, and how to justify the result rather than guess it from a few runs. Read the approved [scalar types and expressions chapter](p_types.html) first. You need assignment, integer promotions, short-circuit evaluation, representable ranges, and the distinction between an expression's value and its side effects. The [loop-analysis chapter](a_loop.html) supplies the broader asymptotic counting methods; here we establish the execution paths that those counts assume.

**Language contract.** Unless a block is marked Python or pseudocode, code uses C17. Small numerical examples fit every conforming C17 `int` unless a different machine model is stated. `INT_MAX` and `UINT_MAX` denote the implementation's limits from `<limits.h>`; unsigned arithmetic is modular, while signed arithmetic outside its representable range is undefined. A fragment belongs inside a function with the displayed declarations. Complete input/output scaffolding is omitted when it does not affect the control-flow question. `emit(x)` in pseudocode means append a value to an output sequence; it is not an undeclared C library function.

The documented discovery pool contains eight offerings. Four complementary core courses were selected for this chapter, with a fifth university source used for C-specific scope, comma-expression, and jump details. Selection considered accessible written substance, coverage within this chapter's boundary, explicit assumptions, proof depth, and exercise value. This is an evaluated accessible pool, not a claim that every course in the world was discoverable or that these courses are globally optimal.

| Reviewed course | Exact written material | Role and reconciliation |
|---|---|---|
| Harvard University, CS50x 2025, David J. Malan | [Lecture 1 notes](https://cs50.harvard.edu/x/2025/notes/1/), Conditionals, compare.c, agree.c, Loops, input validation, and Mario | Core foundation. Branching and iteration are connected to explicit state tables; teaching examples do not establish universal termination or overflow safety. |
| Massachusetts Institute of Technology, 6.0001, Fall 2016, Ana Bell, Eric Grimson, John Guttag | [Lecture 2 slides](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/ba2947b25b1580e4a84df0ec5dbe5cdd_MIT6_0001F16_Lec2.pdf), pages 7–23 | Core cross-language comparison. Python iteration over a range is distinguished from a C three-clause loop. |
| Princeton University, COS126 resource family, Robert Sedgewick and Kevin Wayne | [§1.3 Conditionals and Loops](https://introcs.cs.princeton.edu/java/13flow/), instructional body and exercise inventory | Core tracing and numerical-loop perspective. Java typing, labeled jumps, and overflow behavior are not imported into C. |
| Cornell University, CS2110, Spring 2026, course teaching staff | [Lecture 4: Loop Invariants](https://courses.cis.cornell.edu/courses/cs2110/2026sp/lectures/lec04/), loop anatomy, invariant construction, and exercise families | Core proof method. Prefix and boundary diagrams motivate independently developed scalar examples; array partition algorithms belong to later chapters. Individual authorship is not guessed from an unavailable staff page. |
| University of Cambridge, Programming in C, 2017–18, Neel Krishnaswami | [Lecture 1](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture1.pdf), pages 14–18 and 20–23 | Supplement. The comma-controlled loop exercise and scope/jump distinctions receive explicit initialization and C17 assumptions. |

Stanford CS106A's written robot-control lecture and Berkeley CS61C's short control-flow reference were screened but provide less additional depth for this boundary. CMU 15-122 Spring 2024 was screened through its index; its linked contracts PDF returned 404 and is not counted as reviewed. Exact selection evidence and source hashes are retained in the research audit. The C rules below were checked against the public [WG14 N1570 draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), particularly §§6.8–6.8.6. This is a C11 committee draft used to check rules that carry into the stated C17 scope, not a falsely labeled copy of the published C17 standard.

**Study route.** First understand the state-and-control model. Then learn branch selection, each loop's execution order, and the targets of abrupt transfers. Next study proof obligations and machine boundaries. Finish with the worked problems, the decision procedure, and the final rules. The laboratory can replay execution while you read; it does not replace the proofs. No Iranian entrance-exam paper is used in this chapter, consistent with the final-month reservation. The problem set is a curated set of original and attributed, independently formulated course-inspired problems, not a reproduction of every exercise in the source courses.

## Statements, state, and execution checkpoints

### A program needs both data and a next location

A state maps each in-scope variable to its current value. Write σ for that mapping, and pc for the next execution location. A trace is a sequence of pairs (pc, σ). The location matters: the same values immediately before a loop test and immediately after a loop body can lead to different next actions. A final value alone hides the reasoning that established it.

For `x = x + 2; y = x * 3;`, with initial `x = 4`, the second statement reads the updated value 6. It assigns 18 to `y`. A trace should have one row after each full expression, not one row per physical source line. Multiple statements can share a line, and one statement can span several lines. Comments and visual indentation do not create execution steps in C.

| Checkpoint | `x` | `y` | Meaning |
|---|---|---|---|
| Before first assignment | 4 | Not yet assigned | Reading `y` here would need a valid earlier initialization. |
| After first assignment | 6 | Not yet assigned | The update is complete before the second full expression. |
| After second assignment | 6 | 18 | Both values are now established. |

An expression statement evaluates an optional expression and ends in a semicolon. Its value is discarded, but its side effects matter. `x + 1;` does not change `x`; `x += 1;` does. A null statement is simply `;`. It performs no operation and can legally be a branch or loop body. A block `{ ... }` groups declarations and statements so the block can occupy a single statement position.

```c
int x = 3;
if (x > 0)
    ;
{
    x = 7;
}
```

The `if` controls the null statement. The block following it executes independently, so `x` becomes 7. The braces do not retroactively attach themselves to the preceding condition. Draw a tree of statements when layout is misleading: an `if` owns its immediate substatement, which can be a block, another `if`, a loop, or a null statement.

### Scope is a name rule; execution is a path rule

An inner declaration can hide an outer variable without changing the outer object. Each iteration entering a body block can create a fresh automatic local object. Its initializer executes on that entry; it does not remember an earlier iteration's value unless its storage duration says otherwise. Scope determines which object a name denotes; it does not establish that an assignment actually executed.

```c
int total = 0;
for (int i = 0; i < 3; ++i) {
    int local = 2;
    total += local;
    ++local;
}
```

Each entry initializes `local` to 2. `total` receives 2 three times and finishes at 6. The increment of `local` is discarded when that iteration's object lifetime ends. The `i` declared in the header is in scope for the loop's remaining header and body, not after the loop. A preexisting outer `i` would be a different object if hidden by this declaration.

A control-flow graph represents execution locations as nodes and possible next steps as directed edges. A decision has outgoing edges marked by guard results. A loop has a backward edge. `break` and `continue` create edges that bypass some statements. A graph is more reliable than saying “go to the next line,” because the next executed statement often lies above or outside the current block.

### Trace only defined executions

Before calculating output, check syntax, scope, initialization, arithmetic safety, and sequencing. A convenient branch can prevent an unsafe expression from being evaluated, but an unsafe expression already evaluated in the guard is too late to prevent. `if (b != 0 && a / b > 2)` excludes zero division, yet a signed minimum divided by −1 can still be unrepresentable on the specified machine. A fully appropriate precondition or additional guard is required.

Undefined behavior is not a branch with an unusual numerical answer. The language imposes no requirements on that execution. Keep such cases classified as undefined instead of extending a trace with an invented wraparound. A missing compiler diagnostic does not establish defined behavior. Conversely, a constraint violation such as `continue` outside any loop requires a diagnostic; it is different from a valid program containing a possible undefined execution.

## Conditional selection and decision design

### Truth and evaluation order

In C17 an `if` controlling expression must have scalar type, including arithmetic and pointer types. It selects its first substatement when the expression compares unequal to zero. Negative values are true as well as positive values. A null pointer is false; “zero” here is a semantic comparison, not a claim about raw pointer bits. Java requires a boolean condition. Python uses its own truth-testing protocol. These rules are not interchangeable.

`if (x = 5)` is valid C when `x` is a suitable scalar: it assigns 5, and the assigned value is nonzero, so the branch is taken. `if (x == 5)` compares without assigning. Parentheses around an intentional assignment improve clarity, but they do not convert assignment to comparison. Similarly, `if (0 < x < 10)` parses as `(0 < x) < 10`; the first comparison yields 0 or 1, so the second comparison is true for every ordinary integer `x`. The intended interval test is `0 < x && x < 10`.

For `A && B`, evaluate `A` first; evaluate `B` only if `A` is nonzero. For `A || B`, evaluate `B` only if `A` is zero. The first operand is sequenced before the second when the second executes. Bitwise `&` and `|` do not supply those short-circuit guarantees. A guard therefore has both a Boolean function and an evaluation policy. Algebraically equivalent formulas can differ when operands have side effects or unsafe operations.

```c
int i = 0;
if (i++ == 0 && ++i == 2) {
    i += 10;
}
```

The first operand compares old value 0 and increments `i` to 1. Because that operand is true, the second increments it to 2 and compares 2 to 2. Both are true; the body makes `i` 12. The operations are sequenced by `&&`. Replacing `&&` by `&` introduces unsequenced modifications of the same scalar and gives undefined behavior; it is not merely a less efficient version.

### Independent conditions versus a priority chain

Several independent `if` statements can all execute. An `if`/`else if`/`else` chain selects the first true guard and skips all later guards. In the chain, the last `else` is the residual case under the domain assumptions. It is not an additional condition evaluated separately.

For integer scores restricted to 0 through 100, thresholds should be ordered so the first selected branch has the intended priority. To assign categories 3 for at least 80, 2 for at least 50, and 1 otherwise, test 80 before 50. Testing 50 first swallows all values at least 80. An ascending chain works when its predicates are upper bounds: below 50, then below 80, then the residual case.

Decision design has three obligations. **Coverage:** every allowed input reaches an intended outcome. **Exclusivity or priority:** either predicates are disjoint, or their order deliberately resolves overlap. **Boundary correctness:** equality belongs to the specified interval. Write categories as mathematical intervals before writing code. Include a separate invalid-input outcome when the contract admits inputs outside the classification range.

Independent conditions that assign to the same result implement “last true assignment wins.” They do not implement “first matching category.” Furthermore, an early assignment can change a later guard. For `if (x < 5) x += 4; if (x > 5) x -= 2;`, an initial 3 becomes 7, then 5. A trace must recompute the second guard from the new state.

### The dangling else and explicit blocks

An `else` binds to the nearest preceding unmatched `if` permitted by the grammar, regardless of indentation.

```c
if (a > 0)
    if (b > 0)
        result = 1;
    else
        result = 2;
```

The `else` belongs to `if (b > 0)`. If `a` is nonpositive, neither assignment executes. To give the `else` to the outer test, enclose the inner test in braces and put `else` after that block. The distinction is especially important when `result` would otherwise remain indeterminate. Initializing a default makes the no-assignment path explicit but does not repair a wrongly specified branch.

### Conditional expressions are expressions

`condition ? yes : no` chooses one operand after evaluating its condition. Only the selected operand executes. It produces a value whose type depends on both operand types, even when only one operand executes. Thus a ternary expression can have conversion consequences absent from an `if` with two independent assignments. Review the usual arithmetic conversions before assuming `-1` remains signed in `flag ? -1 : 1u`.

Avoid repeatedly evaluating stateful conditions while simplifying code. `if (read()) ...` and a rewritten expression that calls `read()` twice need not behave alike. A sound transformation preserves evaluated operations, their sequencing, chosen paths, relevant scope, and observable effects. “Same truth table for pure inputs” is a narrower statement than “same program behavior.”

## Switch dispatch, labels, and fallthrough

### Dispatch is one entry jump

A C17 `switch` controlling expression has integer type. Integer promotions apply. Each case is an integer constant expression converted to that promoted controlling type; converted case values must be distinct. There can be at most one `default` in a given switch. An ordinary `const int` variable is not, merely by being `const`, an integer constant expression in C17. An enumeration constant or appropriate constant expression can be used.

After evaluating the controlling expression, execution jumps to the matching label, or to `default` if no case matches. If neither exists, the body is skipped. A label is an entry location, not an automatically guarded independent branch. From the entry point, statements execute in ordinary order, including across later labels, until a jump or the end of the body intervenes. This is fallthrough. A `default` in the middle can fall through into a later case.

```c
int value = 2, sum = 0;
switch (value) {
case 1: sum += 10;
case 2: sum += 20;
default: sum += 30;
case 4: sum += 40; break;
}
```

Input 2 enters at `case 2`; additions 20, 30, and 40 execute, yielding 90. Input 3 enters at `default`, yielding 70. Input 4 yields 40. Input 1 yields 100. The controlling value is not retested at each label. Changing `value` in the body does not redirect the switch to a different case.

### Break targets the nearest eligible construct

`break` exits the smallest enclosing switch or loop. A switch inside a loop therefore intercepts a `break` located directly inside that switch. A loop inside a switch intercepts a `break` located inside the loop. `if` creates no break target. Trace the nesting tree before deciding which construct ends.

`continue` has a different rule: it targets the smallest enclosing loop, ignoring any intervening switch. In a switch inside a `for`, `continue` proceeds to that `for`'s update expression. It skips both the remaining switch statements and the remaining statements of that loop body. A switch with no enclosing loop cannot contain a valid `continue` merely because it resembles a selection among iterations.

### Scope does not force initialization to execute

Declarations placed before the first case are skipped by the dispatch jump. An automatic object can be in scope while its initializer was bypassed. Reading its indeterminate value is not justified by the declaration's visual position. Place case-local declarations inside an explicit block entered after the label.

```c
switch (tag) {
case 1: {
    int temporary = 7;
    result = temporary;
    break;
}
default:
    result = 0;
}
```

In C17 a label prefixes a statement, not a declaration. `case 1: int x = 7;` is not the portable form assumed here. A compound statement after the label provides the required statement and a useful local scope. C versions and compiler extensions can differ; the declared C17 contract decides the answer.

## While, do-while, and for execution order

### Pretest loops: while

`while (guard) body` tests first. If the guard is zero, it executes the body zero times. After a normally completed body, it returns to the guard. There is no implicit update unless code actually performs one. A loop can be syntactically valid yet never progress. `while (i < 4) total += i;` does not change `i` and may repeatedly accumulate until arithmetic itself becomes unsafe.

For `i = 0; while (i < 4) { sum += i; ++i; }`, the body sees 0, 1, 2, 3. The terminating guard sees 4. Body entries and guard evaluations are different counts: four entries, five guards. This rule presumes normal termination by a false guard, a pretest loop entered in the ordinary way, and no other transfer. An early `break` can remove the final guard. Guard expressions with side effects can change state even when false.

### Posttest loops: do-while

`do body while (guard);` enters the body before the first test. The trailing semicolon belongs to the syntax. Ordinary entry guarantees one body entry, but not that every statement of that body completes: an early `break`, `return`, or other jump can skip the trailing test. If termination occurs through a false guard after each completed body, the numbers of body entries and tests are equal.

Input validation often uses this structure because obtaining an input is necessary before deciding whether to repeat. The loop can still fail to terminate if an input source supplies invalid values forever. “A valid value will eventually be supplied” is an environmental assumption, not a mathematical fact implied by the syntax. Robust real input handling must also distinguish end-of-input and parse failure; advanced I/O belongs to its later chapter.

### Three-clause loops: for

For `for (init; guard; update) body`, the normal order is initialization once, guard, body, update, guard, body, update, and so on. The update follows each normally completed body and each `continue` targeting this loop. It does not follow `break` or `return` leaving this loop. The final guard evaluation can be false without another body entry.

The clauses are not function arguments. Initialization and update may be omitted. An omitted guard is treated as a nonzero constant, so `for (;;) { ... }` does not terminate by a false guard. A comma operator can sequence multiple expressions in a clause. However, a comma in a declaration separates declarators rather than forming the same comma operator. A declared header variable is local to the loop.

<figure class="flow-diagram"><svg viewBox="0 0 700 330" role="img" aria-labelledby="order-title"><title id="order-title">The execution graph of a for loop</title><defs><marker id="flow-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="#446c7b"/></marker></defs><g fill="#f0f7f8" stroke="#446c7b" stroke-width="1.5"><rect x="25" y="125" width="110" height="55" rx="8"/><path d="M240 100L310 152L240 204L170 152Z"/><rect x="355" y="125" width="115" height="55" rx="8"/><rect x="520" y="125" width="115" height="55" rx="8"/><rect x="185" y="265" width="110" height="45" rx="8"/></g><g stroke="#446c7b" stroke-width="1.8" fill="none" marker-end="url(#flow-arrow)"><path d="M135 152H170"/><path d="M310 152H355"/><path d="M470 152H520"/><path d="M578 125V45H240V100"/><path d="M240 204V265"/><path d="M412 180V288H295"/><path d="M412 125V85H578V125"/></g><g fill="#153448" text-anchor="middle" font-size="18"><text x="80" y="159">Initialize</text><text x="240" y="158">Guard</text><text x="412" y="159">Body</text><text x="578" y="159">Update</text><text x="240" y="293">After loop</text><text x="332" y="140" font-size="14">true</text><text x="267" y="239" font-size="14">false</text><text x="377" y="280" font-size="14">break</text><text x="484" y="76" font-size="14">continue</text><text x="410" y="32" font-size="14">Normal completion returns through update</text></g></svg><figcaption>Figure 1. In a for loop, continue reaches the update; break reaches the statement after the loop. The update is not an automatic effect of leaving the body by any route.</figcaption></figure>

### The for-to-while rewrite has a condition

The simple rewrite `init; while (guard) { body; update; }` preserves behavior only when relevant paths through `body` reach the update correctly. A `continue` in the original body reaches the for-update; a `continue` in the rewritten while skips the appended update. It can change termination, result, and safety. Scope also needs preserving when initialization declares a variable.

For a structural rewrite, use a dedicated update label inside an enclosing block, replace only `continue` statements targeting the original loop by jumps to that label, and preserve inner-loop continues. Alternatively, restructure the body so every continuation path explicitly performs the update. A mechanical text replacement of every `continue` is wrong in nested loops. A label must not introduce an invalid jump into the scope of a variably modified object.

### The guard can modify the exit state

With `int i = 0; while (i++ < 3) { ... }`, successful tests compare 0, 1, and 2 but body entries see 1, 2, and 3. The false test compares 3 and still increments `i` to 4. Therefore, the post-loop value is 4. With `++i < 3`, body entries see 1 and 2, and the exit value is 3. Treat postfix and prefix operations as state transitions, not decorative typography.

## Abrupt transfers, nesting, and reachability

### A destination table

| Transfer | Destination | Effects skipped |
|---|---|---|
| `break` | After nearest enclosing loop or switch | Remaining body and a departed for-update are skipped. |
| `continue` in while | That loop's next guard evaluation | Remaining body, including manual updates below it, is skipped. |
| `continue` in do-while | That loop's trailing guard | Remaining body is skipped; the test still executes. |
| `continue` in for | That loop's update, then guard | Remaining body is skipped; the header update still executes. |
| `return` | Caller of current function | All remaining local loops and statements in that invocation are skipped. |
| `goto label` | Named statement in same function | Intervening statements are skipped; scope restrictions still apply. |

Nested loops keep separate control states. Breaking the inner loop leaves the outer body active, so statements after the inner loop still run. An outer loop update then occurs if the outer body completes normally. To leave several loops, use a propagated flag, a function return when appropriate, or a carefully constrained label. C17 has no Java-style labeled `break` or labeled `continue`.

Reachability follows the graph, not the apparent intent. Statements after an unconditional `break` in the same path are unreachable on that path. A statement following the entire loop may be reachable through a false guard, a break, or a jump; each route can supply a different postcondition. A `return` inside a nested loop can make an otherwise visible final assignment unreachable for some inputs.

### A label can bypass the normal entry

Ordinary “while can run zero times” and “init runs once” statements assume entry through the loop statement. C permits certain jumps into a loop body; such a jump can skip the initial guard and a for-initialization. This is an advanced tracing boundary, not a recommended design. A valid loop proof must account for every reachable entry edge.

```c
int i = 0, visits = 0;
goto inside;
while (i < 0) {
inside:
    ++visits;
    ++i;
}
```

The jump enters the body once. Afterwards the guard tests `i < 0` with `i = 1` and ends the loop. Final `visits` is 1 despite the initially false ordinary guard. No forbidden scope is entered in this fragment. A jump from outside into the scope of an identifier with variably modified type would violate a separate constraint. Distinguish the syntax boundary from a valid but surprising control path.

## Invariants, termination, and constructing loops

### Four proof obligations

A useful invariant is a property required at a stated checkpoint, commonly just before each guard. It need not hold after every intermediate assignment. Let I denote that property and B the guard. For a side-effect-free guard and an ordinary while loop, establish:

<div class="formula-block">Precondition ⇒ I<br>I ∧ B ⇒ body is safe and re-establishes I<br>I ∧ ¬B ⇒ Postcondition</div>

These establish **partial correctness**: if the loop terminates through its normal guard, the specified result holds. Add a **termination** argument for total correctness. A common variant V maps each guard checkpoint satisfying the guard to a nonnegative integer and strictly decreases across every iteration that returns to the guard. A strictly decreasing sequence of nonnegative integers cannot continue forever. Also establish termination of each body execution; a variant at the outer guard cannot rescue an inner loop that never returns.

Break exits require a separate postcondition at the break edge. Continue paths require preservation and progress at their actual return checkpoint. A stateful guard requires modeling its state transformation; using I ∧ ¬B without accounting for the final guard's side effects can produce a false postcondition. Name the checkpoints before doing algebra.

### Derive an accumulator rather than memorize it

Suppose the task is to add all integers from 1 through `n`, where `n` is a nonnegative `int` and the final sum is representable. Choose `i` as the number already processed and `sum` as their sum. At the guard:

<div class="formula-block"><span class="math-inline">0 ≤ i ≤ n</span><br><math display="block"><mrow><mi>sum</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mi>i</mi></munderover><mi>k</mi><mo>=</mo><mfrac><mrow><mi>i</mi><mo>(</mo><mi>i</mi><mo>+</mo><mn>1</mn><mo>)</mo></mrow><mn>2</mn></mfrac></mrow></math></div>

The empty processed prefix at `i = 0` has sum zero, so initialize both to zero. The postcondition needs `i = n`, giving guard `i < n`. To extend the prefix, increment `i` and add that newly processed number. With `n = 0`, the guard is initially false and the correct result remains zero.

```c
int i = 0, sum = 0;
while (i < n) {
    ++i;
    sum += i;
}
```

Initialization follows from the empty sum. Preservation follows because the new sum is the old sum plus the new endpoint. The bounds become `i + 1 <= n` under the old guard. The variant is `n - i`, a nonnegative integer strictly reduced by one. Upon the false guard, the invariant supplies `i <= n` and the guard supplies `i >= n`, hence equality. All partial sums are nonnegative and at most the final sum, so the stated representability assumption covers the updates. The mathematical expression `i(i + 1)/2` in the proof does not require computing that product in C, where its intermediate value might overflow.

### A moving boundary picture

<figure class="flow-diagram"><svg viewBox="0 0 700 205" role="img" aria-labelledby="prefix-title"><title id="prefix-title">Processed and unprocessed prefixes in an accumulation invariant</title><defs><marker id="prefix-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="#446c7b"/></marker></defs><rect x="35" y="60" width="300" height="64" fill="#dbeee7" stroke="#446c7b"/><rect x="335" y="60" width="330" height="64" fill="#f0f3f8" stroke="#446c7b"/><g fill="#153448" text-anchor="middle" font-size="17"><text x="185" y="88">Processed values: 1 through <tspan class="math-label">i</tspan></text><text x="185" y="111">Their sum is stored</text><text x="500" y="88">Unprocessed values</text><text x="500" y="111"><tspan class="math-label">i + 1</tspan> through <tspan class="math-label">n</tspan></text><text x="35" y="43" class="math-label">0</text><text x="335" y="43" class="math-label">i</text><text x="665" y="43" class="math-label">n</text><text x="350" y="183">One update moves the boundary right by one</text></g><path d="M270 150H405" stroke="#446c7b" stroke-width="2" marker-end="url(#prefix-arrow)"/></svg><figcaption>Figure 2. The boundary is a count of processed values. It is not an array-cell address. At initialization the processed region is empty; at termination it covers the whole interval.</figcaption></figure>

### Weak invariants and circular reasoning

“The sum is correct” is too vague unless “correct for which prefix?” is answered. “The algorithm eventually produces the desired sum” is a goal, not an invariant. A true property such as `i >= 0` may be preserved but too weak to imply the desired sum at exit. Choose enough state relationships to connect progress to meaning.

An invariant can be temporarily false within a body. In the summation loop, immediately after `++i` and before `sum += i`, the sum still covers the previous prefix. The proof is valid because the declared checkpoint occurs after the entire body and before the next guard. A `continue` inserted between those two assignments would return to the checkpoint with the relationship broken.

### Euclid's algorithm and a non-counter loop

For nonnegative mathematical integers A and B, not both zero, maintain `gcd(a, b) = gcd(A, B)` while applying `(a, b) ← (b, a mod b)` whenever `b > 0`. The equality follows because an integer divides both `a` and `b` exactly when it divides both `b` and `a - qb`, where `q` is the quotient. The remainder lies between zero and `b - 1`. Thus `b` is a strictly decreasing nonnegative variant. At exit `b = 0`, and `gcd(a, 0) = a` gives the result.

```c
unsigned int a = A, b = B;
while (b != 0u) {
    unsigned int remainder = a % b;
    a = b;
    b = remainder;
}
```

Here `A` and `B` must fit `unsigned int`, and at least one is nonzero. No multiplication is needed, and remainder is evaluated only with a nonzero divisor. The temporary preserves the old pair. Replacing the three body statements by `a = b; b = a % b;` uses the changed `a` and destroys the invariant. The mathematical meaning determines the necessary sequencing.

## Exact counts and machine-level termination

### Arithmetic progression counts

For mathematical integers, start value a, positive step s, and guard `i < b`, body-entry values are a + ks for nonnegative k satisfying a + ks < b. The count is:

<div class="formula-block"><math display="block"><mrow><mi>T</mi><mo>=</mo><mi>max</mi><mo>(</mo><mn>0</mn><mo>,</mo><mo>⌈</mo><mfrac><mrow><mi>b</mi><mo>−</mo><mi>a</mi></mrow><mi>s</mi></mfrac><mo>⌉</mo><mo>)</mo></mrow></math></div>

For inclusive `i <= b`, when a ≤ b, the count is floor((b − a)/s) + 1; otherwise it is zero. A descending loop with positive decrement s and `i > b` has the analogous ceiling of (a − b)/s, clipped at zero. Derive these by solving the inequality for k, then count integer solutions. Do not apply them when the body changes the index, guard has side effects, an early exit intervenes, or finite arithmetic alters the progression.

For a normal terminating pretest loop with T entries and no early exit, the guard runs T + 1 times; the for-update runs T times. If the T-th body entry breaks, the guard has run T times and the update T − 1 times, assuming earlier entries completed normally and no other transfers. For a do-while with normal guard termination, tests run T times. A break in its T-th entry leaves only T − 1 tests. Initialization counts once under ordinary entry in every such for case.

### Unsigned cycles have number theory

An unsigned loop index updated by `i += step` follows modular arithmetic with modulus M = UINT_MAX + 1 as a mathematical integer. It can wrap instead of passing an expected bound. If it begins at zero, it reaches exactly M/gcd(M, step) distinct residues before returning to zero. A guard testing for equality to target t can be reached only if gcd(M, step) divides t. More generally from a start a, reachability requires gcd(M, step) to divide t − a.

Proof: after k updates the residue is a + k·step modulo M. Target reachability is a linear congruence. If d is the greatest common divisor, every reachable difference is divisible by d. Conversely, dividing by d leaves a step coprime to M/d, which has a multiplicative inverse modulo M/d, so a solution for k exists. This yields a precise termination argument for equality-based loops under a specified modular model. It does not make a guard like `i <= UINT_MAX` false: that comparison is always true for an unsigned variable of that type.

`for (unsigned int i = n; i >= 0u; --i)` never exits through its guard because every unsigned value is at least zero. At zero the decrement wraps. A safe reverse count is `for (unsigned int i = n; i > 0u; ) { --i; ... }`, whose body sees n − 1 through zero and whose decrement occurs only from a positive value. The postdecrement idiom `while (i-- > 0u)` has the same body-entry count but leaves `i` wrapped after its final false test; it has a different exit state.

### Signed and floating progression

For `for (int i = 0; i <= INT_MAX; ++i)`, the guard admits `i = INT_MAX`; the subsequent increment overflows. It is not a defined infinite wraparound. Even if every body access is safe, the update can violate the arithmetic contract. Prefer an exclusive guard when it expresses the desired interval, or explicitly stop before performing an unrepresentable final update.

Floating-point addition can stop changing a large counter when the step is smaller than the rounding resolution. Repeated addition of a decimal fraction can also miss an intended endpoint. Exact equality is therefore not a general termination argument for floating iteration. With a declared binary floating model, ask whether each update changes the stored value, whether values stay finite, and whether NaNs are possible. A NaN fails ordinary ordered comparisons, so “not less than” need not mean “greater than or equal to.” Counting discrete iterations with an integer and deriving the floating value from the index often separates progress from numerical approximation; it does not remove all numerical error.

### Optimizer and environmental boundaries

The C rule for certain loops with nonconstant controlling expressions and no I/O, volatile accesses, or atomic/synchronization operations permits an implementation to assume termination. Consequently, a source-level modular cycle in a nonobservable empty loop is not a portable timing device. A trace of the abstract progression remains useful for identifying a missing termination argument, but do not promise a particular optimized execution of such a loop. A constant guard such as `for (;;)` is a separate case under that rule.

Input loops depend on future inputs. Busy-wait loops for concurrently changing state require appropriate concurrency and memory rules; an ordinary local variable is not a synchronization mechanism. Such systems issues are deferred to their chapters. For this chapter, distinguish three claims: the guard and update mathematically lead to termination; the C operations remain defined; and the environment eventually permits an exit. All three may matter.

## Execution-order laboratory

The laboratory replays a declared, bounded integer model. It supports a normal for-loop, the corresponding while-loop, a posttest loop, a continue-skipping update bug, and early break. Choose a case, the nonnegative limit, and the starting index. Advance one checkpoint at a time. Read the active phase and state together. A repeated full state is reported as a cycle in this deterministic model; a trace cap is a separate stop condition, never a claim of proven nontermination. The model does not interpret arbitrary C or simulate undefined behavior.

<section class="flow-lab" aria-label="Execution order laboratory">
<label for="flow-case">Execution case</label>
<select id="flow-case"><option value="for">for: continue still reaches update</option><option value="while">while: ordinary accumulator</option><option value="do">do-while: body before first test</option><option value="bug">while: continue skips manual update</option><option value="break">for: break skips header update</option></select>
<div class="flow-inputs"><label>Limit, 0 through 12<input id="flow-limit" type="number" min="0" max="12" value="5"></label><label>Starting index, 0 through 12<input id="flow-start" type="number" min="0" max="12" value="0"></label></div>
<pre id="flow-code"></pre>
<div class="flow-actions"><button id="flow-prev" type="button">Previous checkpoint</button><button id="flow-next" type="button">Next checkpoint</button><button id="flow-end" type="button">Show full trace</button></div>
<output id="flow-state" aria-live="polite"></output><p id="flow-explanation"></p>
<div class="flow-track" aria-label="Execution phases"><span data-phase="init">Initialize</span><span data-phase="guard">Guard</span><span data-phase="body">Body</span><span data-phase="update">Update</span><span data-phase="exit">Exit</span></div>
<div class="flow-table"><table><thead><tr><th>Checkpoint</th><th>Phase</th><th>Index</th><th>Sum</th><th>Reason</th></tr></thead><tbody id="flow-trace"></tbody></table></div>
</section>

For limit 5 and start 0, the for-case skips accumulating even indices but updates on every completed or continued entry; its sum is 4 and exit index is 5. The bug-case reaches an even index, continues without changing it, and repeats the same state. The posttest case with limit zero still adds its initial index and increments once before its false guard. The break-case stops at index 3 when that index is entered and skips the header update. Vary the initial state to see why one path diagram must cover both ordinary and boundary inputs.
