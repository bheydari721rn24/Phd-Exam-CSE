## Mathematical constructions, transfer proofs and source reconciliation

### 1. Count a named event at a named checkpoint

A loop's body entry, accumulator write, index update and guard evaluation are different events. For a normally entered pretest for-loop with $T$ entries and normal false-guard exit, the counts are $T$ entries, $T$ updates and $T+1$ guards. If its $T$-th entry breaks before the header update, there are $T$ entries, $T-1$ updates and $T$ guards. A continued for-entry still performs the update; a continued while-entry can skip a manual update. A posttest loop normally performs $T$ tests for $T$ entries, but a break before its trailing test removes that test. These counts follow the actual graph, rather than a universal rule that every loop has one extra comparison.

In the authentic weakly ordered triple loop, outer, middle and inner body-entry counts are respectively
$$15,\quad\sum_{i=1}^{15}(16-i)=120,\quad\binom{17}{3}=680.$$
Each middle loop invocation contributes one additional final false test, giving $120+15=135$ middle tests. Each inner invocation similarly gives $680+120=800$ inner tests. Adding the outer16 tests gives951 total guard evaluations. Total header updates are $15+120+680=815$. The requested accumulator still ends at690 because only the680 innermost entries increment its initial ten. One program can therefore support several correct numerical counts, but only one answers a specified event.

### 2. Invariants must survive every returning edge

At an accumulator's guard-input checkpoint, state its processed-prefix meaning. For add-before-increment, use $s=i(i-1)/2$; for increment-before-add, use $s=i(i+1)/2$. The invariant can temporarily fail between body statements and still be correct at its declared location. A continue inserted before restoration creates a new proof obligation, not merely a shorter path.

For `while(i<n && ++j){++i;}` with initialized zero counters, the invariant is $i=j=t$ before the left test. A successful guard changes only $j$; the body then changes $i$ and restores equality. On the final failed left test, the right increment is skipped, so equality survives into exit. For `while(x++<n){++c;}`, the false guard **does** change its index, so a guard-input equality $x=c$ need not hold afterward. Model the guard as a state transformation plus a Boolean result; do not use the negated guard as if state had not changed.

Termination additionally requires a well-founded ranking and terminating body execution. For the odd-subtract/even-halve process, $n$ decreases on every enabled branch. Its exact number of transitions for $n>0$ is
$$T(n)=\lfloor\log_2n\rfloor+\operatorname{popcount}(n).$$
Each halving removes a trailing zero and reduces bit length by one; exactly initial bit-length minus one such reductions are required to reach the final leading one. Each odd subtraction clears a trailing one without borrow and decreases population count by one. Halving preserves population count, so all initial one bits must be cleared by exactly that many odd subtractions. For13, three halving steps and three subtractions give six transitions. Population count alone is not a strict ranking on each halving, even though it participates in this exact total.

### 3. Ordered loops, filtered loops and first threshold crossing

For weak triples $1\le i\le j\le k\le m$, adding shifts zero, one and two maps them bijectively to distinct triples in one through $m+2$. Hence the count is $\binom{m+2}{3}$. Equal indices are admitted; a strict-triple count omits them. In a filtered range one through $3n$, disjoint three-element blocks each admit two counter writes but still make three body entries. At a guard-input index $i$, the count of preceding accepted entries is
$$s=i-1-\left\lfloor\frac{i-1}{3}\right\rfloor.$$
The invariant explicitly describes skipped multiples, rather than an abstract claim that the counter is correct.

For positive accumulation, after $k$ additions the sum is $S_k=k(k+1)/2$. Since $S_{k+1}-S_k=k+1>0$, threshold $S_n$ is first reached at $k=n$. For an arbitrary positive threshold $H$, choose the least integer $k\ge0$ satisfying $k(k+1)/2\ge H$. A computed inverse-square-root expression is only a candidate in finite arithmetic; validate both that inequality and the preceding index's strict failure. For a budget problem that accepts only sums **not exceeding** $B$, the maximal feasible prefix length instead obeys
$$S_m\le B<S_{m+1}.$$
Reaching or exceeding a threshold and accepting a prefix within a budget are opposite boundary decisions and require different inequalities.

### 4. Modular reachability supplies a termination proof or a counterexample

An abstract modular progression $u_t=a+st\pmod M$ reaches target $b$ if and only if $d=\gcd(s,M)$ divides $b-a$. Necessity follows because $st-Mq$ is always divisible by $d$. For sufficiency, divide by $d$; the reduced step is coprime to $M/d$ and has an inverse, which constructs all solutions. A first positive hit needs the least positive representative, not just existence of one solution.

For step six and modulus256, the period is128 and reachable values from zero are exactly the even residues. Target one is excluded. Target64 gives $3t\equiv32\pmod{128}$ and $t\equiv96\pmod{128}$, so its first positive hit is96. Target zero already matches at time zero; its first positive return is128. Stored values need not increase monotonically, and a finite state space implies repetition rather than visitation of every target.

These are explicit mathematical state models. An actual C unsigned expression needs its type and conversion checkpoints identified. A loop with a qualifying nonconstant guard and no observable or synchronization operations can also fall under the standard's termination-assumption permission; its abstract cycle is not a portable timing guarantee. Signed overflowing arithmetic is a different invalid domain and must never be shown as an unsigned-style predicted cycle.

### 5. Recursion semantics, total calls and active depth

A binary two-child recursion at parameter $k$ with base zero has total-call recurrence $C(0)=1$, $C(k)=1+2C(k-1)$, yielding $C(n)=2^{n+1}-1$. Ordinary sequential execution holds a root-to-current-node path, at most $n+1$ active frames without eliminating calls; it does not hold the complete historical tree at once. A one-child recursion with local toll $k$ instead has $W(0)=0$, $W(k)=k+W(k-1)$, yielding $W(n)=n(n+1)/2$ body operations. Tail position can permit frame reuse without deleting local work.

For reverse-stride copying, the checkpoint equations are $n_t=N-1-2t$ and $i_t=t$. There are $\lceil N/2\rceil$ writes and one additional returning base call. The original fourth option also uses source stride two; it fails through its odd destination positions one, three, five. Separate source stride, destination stride, destination offset, array capacity and base-inclusive call count.

The copying proof describes separate mathematical source and destination arrays. A concrete overlapping-memory implementation needs an additional proof that no write replaces a future source. For example, using the same five-element array for both names can write source position four into destination zero before later reading source zero, altering the intended original value. Avoid deriving an overlap guarantee from the index guard alone.

### 6. Eight fully solved conceptual and mathematical extensions

**A — Distinguish all event counts in a nested program.** In the authentic bound15 triple loop, inner writes680 do not equal middle entries120, total updates815 or total guard tests951. Derive each using invocation count plus one final false test per normally completed pretest invocation. All loop variables reach16 under the source's sufficient-type premise. With an empty outer range, unentered inner variables do not receive an invented terminal value.

**B — A finite proof counterexample to arithmetic swap.** Under int32 take `a=INT_MAX,b=2`. Both desired final swapped values fit, but `a=a+b` cannot produce2147483649 in signed int. The original sequence is undefined at its first arithmetic node. A temporary-variable swap stays within the source domains. Symbolic cancellation of the later two subtractions does not repair an already invalid execution.

**C — Distinguish logical AND from bitwise AND exactly.** Starting zero counters, `i<n && ++j` ends at $(n,n)$ for safe nonnegative $n$. Reversing its logical operands ends at $(n,n+1)$ when the additional final increment fits. For any safe positive $n$, replacing it with `(i<n) & (++j)` instead ends at $(1,2)$: first $1\mathbin{\&}1$ is one; second $1\mathbin{\&}2$ or $0\mathbin{\&}2$ is zero. The operands affect distinct objects, so this particular case is not same-object unsequenced undefined behavior. It demonstrates both eager evaluation and bit semantics.

**D — A real condition-priority difference.** With continue at multiples of three and break at eight, either order of the two pure tests yields $(19,8)$. Break target nine overlaps the continue predicate. Continue-first bypasses the break, accepts ten and normally exits with $(37,11)$. Break-first ends with $(27,9)$. A model must display this changed predicate instead of falsely changing the original question's output.

**E — Exact odd-prefix budget.** In the retained capstone, positive odd values below $n$ are $1,3,\ldots,2r-1$ where $r=\lfloor n/2\rfloor$, and the first $m$ sum to $m^2$. Under nonnegative budget $B$, accepted count is $m=\min(r,\lfloor\sqrt B\rfloor)$, interpreted as an exact integer inequality. If $m=r$, every candidate fits and normal exit has $i=n$; otherwise the break index is $2m+1$. At $n=12,B=18$, $r=6,m=4$, sum16 and break index nine. This proves maximal prefix length; it is not an arbitrary-subset selection problem.

**F — Newton's first step need not move closer.** Princeton's root-loop pedagogy requires a more precise claim than every initial step reduces root-distance. For $c=0.01$, start $t=c=0.01$ and update $t'=(t+c/t)/2=0.505$. The target is $\sqrt c=0.1$: absolute error rises from0.09 to0.405. For positive exact $t$, the arithmetic-geometric mean inequality gives $t'\ge\sqrt c$, and once $t\ge\sqrt c$, $\sqrt c\le t'\le t$. Thus the monotone-above-root argument applies after the first update, not necessarily from an arbitrary initial side. Finite rounding, zero division and termination tolerance need additional domains.

**G — A last update can fail after the last valid output.** Under int32, a loop emitting powers of two through exponent30 can print $2^{30}$ validly, then overflow if its unconditional final update multiplies by two before testing exponent31. Every emitted value fitting is insufficient. Move or guard that update according to the exact desired output sequence; Java wrap semantics from the source listing must not be silently applied to C17.

**H — NaNs invalidate a casual minimum postcondition.** An array argmin invariant based on ordinary ordered comparisons needs non-NaN values or an explicit NaN policy. If the first candidate is NaN and later candidate is finite, comparing the latter less than the stored NaN is false, so the original first candidate can persist without being an ordered minimum. State a non-NaN domain, reject NaNs or explicitly define how they are handled. Infinite values can be compared in IEEE order, while NaNs require this separate decision. The full array algorithm remains in its later chapter; this example tests the proof's domain.

### 7. Course synthesis and precise reading limits

Harvard CS50x2025's conditionals, loops, input validation and Mario sections were freshly read. MIT6.0001 Fall2016 Lecture2 pages7–23 and all five written in-class questions were freshly read, with relevant slide images checked. Princeton's accessible §1.3 body, 37 freshly accessible exercise statements and two complete linked program listings were read; its unavailable remaining inventory is historical evidence only. Cornell CS2110 Spring2026 Lecture4's complete written body and exercise4.1–4.12 statements were freshly read. Cambridge's scoped nine pages provide supplemental C-specific statement and comma-guard perspectives, with five images actually inspected. These recorded roles come from the existing bounded eight-offering evaluation; no complete worldwide course census or indiscriminate four-course selection is asserted.

MIT's final break example places its accumulator increment **inside** the same branch after `break`. It is unreachable on a taken branch and skipped on a false branch; silently moving it outside the branch would teach another program. Its range endpoint shorthand applies to unit step, while the general iterator excludes stop without necessarily visiting stop minus one. Cornell's invariant construction gains explicit guard-side-effect checkpoints and a continuation-edge qualification for loop rewrites. Princeton's numeric examples are kept under Java or independently declared C models, and the Newton and final-update corrections above prevent informal source claims from becoming false universal rules. Whole course exercise banks extend beyond this scalar chapter and are not reproduced or claimed completely solved here.
