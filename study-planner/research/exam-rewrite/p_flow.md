## Teaching through formulas and conceptual decisions

### Expand execution into control checkpoints

A for-loop executes initialization once, then alternates guard, body and update. A `continue` in its body jumps to the update, whereas a `continue` in an equivalent-looking while-loop jumps directly to the guard. To preserve semantics in a for-to-while translation, every continue path must still execute the intended update. A `break` exits the nearest loop or switch; it does not automatically exit an enclosing loop.

A switch performs one initial dispatch to a matching label and then ordinary sequential execution. Encountering `default` later through fallthrough does not mean the original value failed every case. Case labels do not create automatic jumps after each statement. Compute the exact entered point and follow the statements until a transfer exits.

### Trace side effects in guards at the correct time

For `while (i++ < 3)` starting at0, successful tests compare0,1,2; the failing test compares3, but still increments$i$ to4. The body runs three times while the final state is4. Distinguish the value used in the comparison from the new value stored by postfix increment. A posttest loop runs its body at least once if control enters it, even when its first guard is false.

### Machine arithmetic changes termination

An unsigned$b$-bit update adding$d$ follows residues modulo$2^b$. Its cycle length is $2^b/\gcd(d,2^b)$, and only residues congruent to the start modulo that gcd are reachable. A mathematical increasing sequence can therefore become a finite modular cycle. A signed overflow path is instead undefined; it must not be treated as the same wrapped state graph.

For total correctness, supply an invariant giving the output property and a decreasing nonnegative integer or other well-founded ranking giving termination. A constant invariant such as “the variables are integers” may be preserved but does not explain the result or why execution stops.

## Formula and conceptual problem bank

### Question 1. Independent conditionals

Initially `int x=1;`. Execute `if(x==1) x=2; if(x==2) x=3;`. What is final$x$?

**A.** 1

**B.** 2

**C.** 3

**D.** Undefined behavior.

**Answer: C.**

The first condition is true and changes$x$ to2. The second statement is independent and tests the updated value, so it changes$x$ to3. Replacing the second `if` with `else if` would make the statements one selection chain and change the outcome. Read the actual syntax, not an imagined priority chain.

### Question 2. Dangling else

Initially `int a=0,b=0,x=0;`. Execute `if(a) if(b) x=1; else x=2;`. What is final$x$?

**A.** 0

**B.** 1

**C.** 2

**D.** Undefined behavior.

**Answer: A.**

The else binds to the nearest unmatched if, namely `if(b)`. Because the outer condition$a$ is false, its entire nested statement is skipped. No assignment to$x$ occurs. Formatting without braces does not change the binding rule; pairing the else with the outer if would incorrectly predict2.

### Question 3. Switch fallthrough

Initially `int x=2,y=0;`. Execute `switch(x){case 1:y+=1; case 2:y+=2; default:y+=4;}`. What is$y$?

**A.** 2

**B.** 4

**C.** 6

**D.** 7

**Answer: C.**

Dispatch enters case2, adds2, then falls through to the default-labeled statement and adds4. The result is6. Case1 is before the entry point and is not executed. Default is a label, not an implicit else branch that prevents fallthrough. A break after case2 would give a different result.

### Question 4. Continue in a for-loop

Compute$s$ after `int s=0; for(int i=0;i<5;i++){if(i==2) continue; s+=i;}`.

**A.** 7

**B.** 8

**C.** 10

**D.** The loop never terminates.

**Answer: B.**

The accumulated indices are0,1,3,4, totaling8. At$i=2$, continue skips the remaining body but still executes the for update, moving$i$ to3. The sum10 includes the skipped index. An incorrect while translation that puts its update after the continue path could stall.

### Question 5. A modifying guard

Initially `int i=0,c=0;`. Execute `while(i++<3) c++;`. What are final$(i,c)$?

**A.** (3,3)

**B.** (4,3)

**C.** (4,4)

**D.** (3,4)

**Answer: B.**

The tests use old$i$ values0,1,2,3. The first three succeed and increment$c$; the fourth fails, but its postfix increment still changes$i$ from3 to4. Thus final$i$ is4 and$c$ is3. A failed comparison does not undo side effects performed while evaluating its operand.

### Question 6. Posttest minimum execution

Initially `int i=5,c=0;`. Execute `do {c++;} while(i<3);`. What is$c$?

**A.** 0

**B.** 1

**C.** 3

**D.** 5

**Answer: B.**

Control enters the body before evaluating the condition, so$c$ becomes1. The first test is false and ends the loop. A while-loop with the same condition would execute zero times. The initial numeric value5 affects the guard but does not specify a number of body repetitions.

### Question 7. Break scope

Execute `int c=0; for(int i=0;i<3;i++){for(int j=0;j<4;j++){if(j==2) break; c++;}}`. What is$c$?

**A.** 2

**B.** 3

**C.** 6

**D.** 12

**Answer: C.**

For each outer$i$, the inner iterations$j=0,1$ increment$c$, then$j=2$ breaks only the inner loop. The outer loop continues for all three indices. Total increments are$3\cdot2=6$. An outer-loop exit would need another transfer or condition; the inner break does not imply it.

### Question 8. Return exits the function

A function loops through indices0 through9, increments$c$, and immediately returns$c$ when the index equals3. Starting$c=0$, what value is returned?

**A.** 3

**B.** 4

**C.** 9

**D.** 10

**Answer: B.**

Indices0,1,2,3 each execute the increment before the return check. Thus$c$ is4 when the function exits. Return ends the whole function and no later iterations execute. The answer3 would correspond to checking before the increment or using different index endpoints.

### Question 9. Unsigned cycle reachability

Assume8-bit unsigned storage and defined promoted additions. Starting$x=0$, repeatedly assign$x=x+64$ back to that storage. Which value is never reached?

**A.** 0

**B.** 64

**C.** 128

**D.** 1

**Answer: D.**

The reachable cycle is0,64,128,192,0. Equivalently $\gcd(64,256)=64$, so only residues congruent to0 modulo64 can appear.1 is outside that class. A loop waiting for$x=1$ never terminates under this model; “the counter increases” is not a valid unsigned termination proof.

### Question 10. A sum invariant

A loop begins with$i=0,s=0$ and repeats `s+=i; i++;` while$i<n$. Which invariant holds at each guard checkpoint?

**A.** $s=i(i-1)/2$

**B.** $s=i(i+1)/2$

**C.** $s=n(n-1)/2$

**D.** $s=i^2$

**Answer: A.**

Before the iteration with index$i$, exactly the values0 through$i-1$ have been accumulated, so $s=i(i-1)/2$. Adding$i$ gives $i(i+1)/2$, which equals the same invariant expression after incrementing the index to$i+1$. At termination$i=n$, it yields the final sum. The other formulas use the wrong checkpoint or assume the postcondition throughout.

### Question 11. Euclid trace

Starting positive$a=48,b=18$, repeatedly replace$(a,b)$ by$(b,a%b)$ while$b!=0$. How many updates occur?

**A.** 2

**B.** 3

**C.** 4

**D.** 18

**Answer: B.**

The states are(48,18), then(18,12), then(12,6), then(6,0). There are three updates before the guard fails. The second component strictly decreases while positive and the gcd is invariant, so termination and the answer6 are independently explained. Counting the initial state as an update gives the wrong endpoint count.

### Question 12. A correct ranking

For a loop with invariant$0\le i\le n$ and update$i=i+1$ whenever$i<n$, which integer ranking proves termination?

**A.** $i$

**B.** $n-i$

**C.** $n+i$

**D.** $0$

**Answer: B.**

$n-i$ is nonnegative at the checkpoint and decreases by exactly1 per iteration. It cannot descend infinitely through nonnegative integers. The counter$i$ increases and is not a decreasing ranking; the constant0 provides no progress. The invariant supplies the ranking domain needed by the proof.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Continue and break priorities

Compute final$(s,i)$ for `int s=0,i; for(i=1;i<=10;i++){if(i%3==0)continue; if(i==8)break; s+=i;}`.

**A.** (19,8)

**B.** (27,9)

**C.** (19,9)

**D.** (55,11)

**Answer: A.**

Indices3 and6 are skipped by continue. Indices1,2,4,5,7 add to19. At8, the continue condition is false, then break exits before adding8 and before the for update, so final$i$ remains8. Values9 and10 are never reached. Reversing the order of tests or moving the addition changes the state trace; exact execution checkpoints decide both components.

### Question 14. Challenge: Reach a target in an unsigned orbit

An8-bit unsigned variable starts at0 and repeatedly adds6 modulo256. What is the first positive update count at which it reaches64?

**A.** 32

**B.** 64

**C.** 96

**D.** 128

**Answer: C.**

Solve$6t\equiv64\pmod{256}$. Divide by the gcd2 to obtain$3t\equiv32\pmod{128}$. The inverse of3 modulo128 is43, so$t\equiv1376\equiv96\pmod{128}$. This residue is the least positive solution. The orbit period is128, while32 and64 updates give residues192 and128. A target test can terminate even though the counter does not increase monotonically.

## Applicable formulas and examination notes

### 1. If chains are syntax

Independent if statements test the latest state; an else-if chain chooses at most one branch. In the update1 to2 to3 example, independent statements yield3, while a chain can yield2. Do not infer the grouping from indentation.

### 2. Else binding

An else attaches to the nearest unmatched if. For a false outer guard, an inner else is skipped with its enclosing statement. Braces make the intended binding explicit and remove this common parsing distractor.

### 3. Switch dispatch and fallthrough

Switch selects an entry label once; later labels do not redispatch. Starting at case2 and falling into default executes both bodies. Count until a break, return or other actual transfer occurs.

### 4. Continue destination

In a for-loop, continue goes to the update and then guard. In a while-loop, it goes directly to the guard. A semantics-preserving translation must route all continue paths through the equivalent update.

### 5. Guard side effects

A failed guard still evaluates its operands. `while(i++<3)` starting0 ends with$i=4$ after three bodies. The old value determines the comparison; the new value remains stored after failure.

### 6. Do-while entry

A do-while body executes once before its first guard if entered normally. For initial$i=5$ and test$i<3$, it still executes once. A pretest loop with the same condition executes zero times.

### 7. Break and return

Break exits the nearest enclosing loop or switch. Return exits the entire function. A break inside a switch nested in a loop need not end the loop, and a break inside an inner loop need not end the outer one.

### 8. Half-open count

For$i=a,a+d,\ldots<b$ with$d>0$, exact body count is $\max(0,\lceil(b-a)/d\rceil)$. Inclusive upper bounds use a floor formula with one added. A count formula assumes arithmetic progresses without overflow.

### 9. Unsigned orbit

An unsigned$b$-bit increment$d$ has period $2^b/\gcd(d,2^b)$. Reachable residues share the starting residue modulo the gcd. For8 bits and step64, the period is4 and the target1 from start0 is unreachable.

### 10. Invariant checkpoint

Before adding$i$, the prefix sum of0 through$i-1$ is$i(i-1)/2$. After adding$i$ but before incrementing, it is$i(i+1)/2$. Locate the assertion exactly; a correct formula at one checkpoint can be wrong at another.

### 11. Euclid progress

For nonnegative remainder arithmetic and positive$b$, the next second operand is strictly smaller than$b$. The gcd remains invariant. Together these properties establish termination and the returned gcd; neither alone proves total correctness.

### 12. Partial versus total correctness

An invariant plus a false exit guard can establish the postcondition if the loop terminates. A nonnegative decreasing ranking establishes termination. A preserved weak property such as “all variables are integers” supplies neither the intended result nor progress.

<!-- BOUNDARY-NOTES -->

### 13. Switch initialization bypass

Jumping to a later case can bypass initialization of an automatic scalar declared earlier in the switch body. Scope determines where the name is visible, not whether its initializer executed. Reading an indeterminate value is not a deterministic trace question.

### 14. Loop equivalence boundaries

Replacing a do-while with a while requires explicitly preserving its initial body execution. Replacing a for with a while requires preserving update behavior on continue paths. Similar syntax is insufficient to prove equal reachable states.

### 15. Unsigned exit condition

A loop using an unsigned counter and guard $i\ge0$ never fails that comparison by becoming negative. Modular wrap can revisit its starting state. A signed counter reaching overflow instead has undefined behavior, not a defined negative-wrap termination.
