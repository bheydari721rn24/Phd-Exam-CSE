The problems below are complete teaching examples, arranged by technique. “Course-derived” identifies the mathematical exercise family and its source location; statements, numerical variants, notation, and solutions are independently written. “Original” identifies a newly constructed synthesis problem. The source ledger distinguishes selected exercises from material outside this chapter's boundary.

### Problem 1. Specify a bounded counter precisely

**Original · State modeling.** A counter starts at zero, increments until it reaches three, and then reports completion forever. Specify its states and transitions. Has it terminated as a transition system?

**Solution.** Take $S={0,1,2,3,done}$, initial set ${0}$, and transitions $0→1$, $1→2$, $2→3$, $3→done$, and $done→done$. The execution has an infinite suffix at `done`, so this transition system does not terminate. It does eventually report completion, which is a different property. If the last self-loop is removed, the only maximal execution has four transitions and ends at `done`. The modeling choice determines which theorem is appropriate. An invariant excluding numerical overflow can be valid in either model, but a strict ranking on every transition cannot coexist with the self-loop.

### Problem 2. Repair a true but noninductive assertion

**Original · Strengthening.** Let $S={0,1,2,3}$, $S_0={0}$, and transitions $0→1$ and $2→3$. Classify $P={0,1,2}$, and find a certificate proving that state three is unreachable.

**Solution.** Only zero and one are reachable, so $R={0,1}⊆P$. Initialization holds because zero belongs to $P$. Preservation fails on $2→3$. This edge is not a reachable counterexample path; it is a counterexample to the stronger closure obligation. Choose $J={0,1}$. Its only outgoing edge is $0→1$, which remains inside it. Thus $J$ is initialized and preserved, and $3∉J$ proves the requested impossibility. This example teaches how to interpret an unsuccessful certificate: a failed inductive check need not mean that the desired safety claim is false.

### Problem 3. Which operations preserve invariant certificates?

**Original · Logical closure.** Prove closure under intersection and union. Disprove closure under complement and under weakening.

**Solution.** If $s∈J∩K$ and $s→t$, preservation of each operand gives $t∈J$ and $t∈K$, hence $t∈J∩K$. If $s∈J∪K$, it belongs to an operand whose preservation places its successor back in that same operand. Initialization is retained when the operands are initialized. For complement, use $0→1$: the set ${1}$ is preserved, but ${0}$ is not. For weakening, use Problem 2: the preserved set ${0,1}$ implies membership in ${0,1,2}$, but the latter is not preserved. Thus proving an assertion implies another assertion does not transfer its one-step closure to the weaker assertion.

### Problem 4. Find the largest safe closed set

**Original · Forward and backward reasoning.** Let $Q⊆S$ be the permitted states of a finite graph. Construct the largest transition-closed subset of $Q$ and explain how it decides universal safety of initial states.

**Solution.** Start with $K_0=Q$. Repeatedly remove states having at least one successor outside the current set:

<div class="formula-block">$K_{i+1}={s∈K_i:Post({s})⊆K_i}$.</div>

The sequence only shrinks, so finiteness guarantees stabilization at a set $K$. At stabilization every successor of a member stays in $K$, and $K⊆Q$. If $J⊆Q$ is any transition-closed set, induction gives $J⊆K_i$: a member of $J$ cannot be removed because all its successors remain in $J$. Hence $J⊆K$, proving maximality. Universal safety holds exactly when $S_0⊆K$. For the forward direction, the reachable set is a closed subset of $Q$ and therefore lies in $K$. For the reverse direction, initialized closure of $K$ puts every reachable state inside $Q$. Dead ends are retained because having no successors satisfies the subset condition vacuously. This construction is a safety calculation, not a guarantee of reaching a goal.

### Problem 5. Check whether strengthening is actually necessary

**Original · Discovery.** Initialize $x=0$, $y=0$, then repeatedly execute the simultaneous update $(x,y)←(x+1,y+2)$. Prove $y≥x$. Explain why that assertion alone is a poor one-step certificate if the state space permits negative integers.

**Solution.** Under this update, $y≥x$ is actually preserved on all integer states: the new difference is $(y+2)−(x+1)=(y−x)+1≥1$. Thus negative integers do not invalidate this particular candidate. The stronger equality $y=2x$ is also preserved and initialized, and yields the goal only together with $x≥0$. Both clauses are true on reachable states. An equality without its sign condition would not imply the desired inequality at negative values. The deliberately tempting explanation in the question is false: a rigorous solution must check the change and reject an incorrect premise instead of automatically inventing a strengthening. The equality is useful for characterizing reachable pairs, but is not necessary to certify this goal.

### Problem 6. Derive a weighted conservation law

**Original · Linear invariants.** States have nonnegative coordinates. Moves add $(2,−1)$ or $(−2,1)$ when the new state remains nonnegative. Starting at $(4,3)$, characterize all reachable states.

**Solution.** Solving $2w_1−w_2=0$ gives the conserved quantity $x+2y$. Initially its value is ten. The possible nonnegative integer solutions of $x+2y=10$ are $(10,0),(8,1),(6,2),(4,3),(2,4),(0,5)$. All six are reachable: repeated first moves increase $x$ by two and decrease $y$ by one until zero; repeated second moves do the reverse until $x=0$. Every intermediate state obeys the nonnegative guard. Thus in this specific system conservation plus the domain is sufficient, and the displayed paths prove the converse. If only the first move were allowed, the same equality would remain conserved but the final two pairs would be unreachable. The converse depends on the moves, not just on the formula.

### Problem 7. A diagonal robot: necessity and sufficiency

**Course-derived · MIT Section 5.4.2.** A robot starts at the origin and independently changes each coordinate by either plus one or minus one. Determine exactly which lattice points it can reach.

**Solution.** Every step changes the coordinate sum by an even number, so an odd sum is excluded by an initialized modular invariant. For the converse, let $x+y$ be even. The coordinates have equal parity. Choose an integer $k≥max(|x|,|y|)$ with that parity. A length-$k$ sequence containing $(k+x)/2$ plus signs and $(k−x)/2$ minus signs sums to $x$; both counts are nonnegative integers. Construct another sequence with counts $(k+y)/2$ and $(k−y)/2$ for $y$. Pairing their steps gives exactly the permitted diagonal moves and ends at $(x,y)$. Consequently even sum is both necessary and sufficient. The construction also identifies admissible path lengths: they must be at least the maximum absolute coordinate and have the common coordinate parity.

### Problem 8. Water-jug divisibility is an invariant

**Course-derived · MIT Section 5.4.4, numerical extension.** Two jugs have integer capacities twelve and eight. Allowed operations completely fill a jug, completely empty it, or pour until the source is empty or the target is full. Can either jug contain six units if both start empty?

**Solution.** Use the predicate that both volumes are multiples of four. Initialization holds at $(0,0)$. Filling produces twelve or eight; emptying produces zero. During a pour from volumes $(a,b)$ into the eight-unit jug, the transferred amount is $min(a,8−b)$. If both volumes are multiples of four, both arguments of this minimum are multiples of four, so the transfer and both updated volumes are multiples of four. The reverse pour uses $min(b,12−a)$ and has the same property. Thus all move types preserve the predicate. Six is not divisible by four and is impossible. For general integer capacities the same proof uses their greatest common divisor. This proves an obstruction, not the unrestricted converse for arbitrary target volumes or altered pouring rules. Allowing an arbitrary partial pour would invalidate the preservation proof.

### Problem 9. An even-area board that cannot be tiled

**Original · Coloring.** Remove two diagonally opposite corner squares from an eight-by-eight board. Prove that dominoes cannot tile the remainder.

**Solution.** Color square $(i,j)$ by the parity of $i+j$. The two opposite corners have the same color because both coordinate sums are even. The intact board has thirty-two squares of each color. Removing those corners leaves thirty of one color and thirty-two of the other. Each horizontal or vertical domino covers exactly one square of each color, since moving by one along either coordinate flips parity. Removing covered pairs preserves the uncovered color difference, initially two. A complete covering would leave zero uncovered squares of either color and hence difference zero, a contradiction. The remaining sixty-two squares have even area, so area divisibility is a weaker test. All allowed orientations were included in the coloring argument.

### Problem 10. Flipping a fixed number of coins

**Original · Modular change.** A move flips exactly six coins. Prove that the parity of the number of heads is preserved, and show why total-head count is not conserved.

**Solution.** If $h$ of the chosen six coins initially show heads, those heads disappear and the other $6−h$ coins become heads. Thus the change is $6−2h$, always even. An initialized head-parity predicate is therefore preserved. The actual count can change by six when all selected coins are tails, by minus six when all are heads, or by zero when three of each are selected. Hence parity conservation does not imply numerical conservation or monotonicity. With five flipped coins, the change $5−2h$ is odd and parity flips at every move; parity would then constrain the number of moves instead of remaining a constant state property.

### Problem 11. Derive the sliding-puzzle invariant

**Course-derived · MIT Problem 5.38.** On a four-by-four sliding puzzle, list the fifteen numbered tiles row by row while omitting the blank. Let $p$ be their inversion count and $r$ the blank's row number counted from the top. Prove that the remainder of $p+r$ modulo two is conserved and use it to exclude a completely reversed numbered order with the blank remaining at bottom right.

**Solution.** A horizontal blank move does not change the relative order of numbered tiles in the flattened list: the moving tile crosses only the omitted blank. Neither inversion parity nor the blank's row parity changes. In a vertical move, the moving tile crosses exactly three other numbered tiles in the flattened list. Interchanging it past each distinct tile flips inversion parity, so three crossings flip it once. The blank's row changes by one and flips its parity too. Their sum modulo two is therefore unchanged in both move types.

Initially the tile list is increasing, so $p=0$ and $r=4$, giving parity zero. In the completely reversed list, every pair is inverted, giving $p=15⋅14/2=105$ and $r=4$, hence parity one. The target is excluded. On an odd-width board, a vertical move crosses an even number of numbered tiles, so inversion parity alone is conserved. Equal invariant values are not, by this calculation alone, a proof of mutual reachability; that converse needs a separate constructive argument.

### Problem 12. Triple rotation preserves parity but need not sort

**Course-derived · MIT Problem 5.43, smaller instance.** Rotate three consecutive distinct entries cyclically until their smallest entry is first. Show that inversion count never increases, inversion parity is preserved, and a reversed six-element list cannot become increasing through these moves.

**Solution.** Entries outside the triple retain the same total number of inversions with its three values, since its occupied positions remain a consecutive block. It suffices to inspect internal order. If the smallest entry is already first, the move is the identity. If the smallest is in the middle, the rotation either leaves the internal inversion count unchanged or reduces it by two, depending on the relative order of the other two entries. If the smallest is last, moving it to the front reduces the internal inversion count by two. Thus every change is zero or minus two, preserving parity and giving weak descent.

The reversed six-element list has $6⋅5/2=15$ inversions, an odd count, whereas the increasing list has zero. It is impossible to reach the target. Weak descent alone does not prove termination if identity moves are allowed. If only nonidentity rotations are permitted, the entire list decreases lexicographically because the first changed position acquires a smaller entry. There are only finitely many permutations, so such nonidentity executions terminate. Their terminal arrangement need not be sorted: $[1,3,2]$ permits no nonidentity rotation of its only triple.

### Problem 13. A growing coin system with a preserved head parity

**Course-derived · MIT Problem 5.40.** Start with ninety-eight heads and four tails. A move either flips ten coins or adds one more tail than the current head count. Prove that exactly one head is impossible, exhibit a route to exactly one tail, and classify the useful derived quantities.

**Solution.** Flipping ten coins changes the head count by $10−2h$ for some selected-head count $h$, hence by an even integer. Adding tails changes no heads. Head parity is initially even and remains even, excluding exactly one head.

To reach one tail, first flip nine heads and one tail. This gives ninety heads and twelve tails. Add ninety-one tails, producing ninety heads and one hundred three tails. Flip ten tails nine times, producing one hundred eighty heads and thirteen tails. Flip three heads and seven tails: the result is one hundred eighty-four heads and nine tails. Finally flip one head and nine tails: the result is one hundred ninety-two heads and one tail. Each flip chooses an available number of heads and tails, so the witness is valid.

Total-coin count is weakly increasing: flips leave it unchanged and additions increase it. It is not strictly increasing, since a flip is permitted. Head count and tail count are neither always increasing nor always decreasing. Their parities behave differently: head parity is constant; an addition changes total parity and tail parity because the added number is odd on every reachable state. Thus neither of those latter parities is constant. A statement about reachable states has been justified here using the already proved even-head invariant.

### Problem 14. A safe admission policy that eventually deadlocks

**Course-derived · MIT Problem 5.39, generalized capacity.** Let $A,B$ be money collected at entry and exit, and $C$ the number of occupants on a bridge. Entry changes $(A,B,C)$ by $(3,0,1)$; exit changes it by $(0,2,−1)$ and requires $C>0$. The allowed capacity is a positive integer $K$. Admit only when $D=A−B<T$, where $T=D_0+3(K−C_0)$ and $C_0≤K$. Prove safety and explain deadlock.

**Solution.** The quantity $D−3C$ changes by zero at entry and by one at exit. Therefore $D−3C≥D_0−3C_0$ is initialized and preserved. Just before admission, combine this inequality with the guard:

<div class="formula-block">$D_0+3(C−C_0)≤D<T=D_0+3(K−C_0)$.</div>

Canceling the initial terms yields $C<K$, so the integer occupancy is at most $K−1$ before entry and at most $K$ afterward. Exiting reduces occupancy. Consequently $0≤C≤K$ is preserved by both operations.

For a full change classification, entry and exit increments are respectively: $A$: three and zero; $B$: zero and two; $A+B$: three and two; $A−B$: three and minus two; $3C−A$: zero and minus three; $2A−3B$: six and minus six; $B+3C$: three and minus one; $2A−3B−6C$: zero and zero; $2A−2B−3C$: three and minus one. Hence the first two are weakly increasing, their sum is strictly increasing, $3C−A$ is weakly decreasing, the eighth expression is constant, and the remaining expressions have neither monotonic direction.

Safety does not imply continued admission. First let every initial occupant exit. The bridge is now empty and $D=D_0−2C_0$. At an empty bridge below threshold, admit one occupant and then let that occupant exit. Each completed trip increases $D$ by one while restoring $C=0$. Since $T−(D_0−2C_0)=3K−C_0$ is a positive integer, after that many trips the empty bridge has $D=T$. Entry is forbidden and exit is impossible because it is empty: a deadlock. This is a concrete maximal execution consistent with the safety invariant.

### Problem 15. Two-neighbor growth and perimeter

**Course-derived · MIT Problem 5.41.** Cells in an $n$-by-$n$ square become marked permanently when at least two edge-adjacent neighbors were already marked. Prove that fewer than $n$ initially marked cells cannot eventually mark the whole square.

**Solution.** Define the perimeter of the marked union as the number of unit edges between a marked cell and an unmarked cell or the exterior. Initially $k$ marked cells have perimeter at most $4k$, because shared edges reduce the naive sum of four per cell. Marking one new cell with $j≥2$ marked neighbors removes $j$ old boundary edges and creates $4−j$ new boundary edges. Thus the perimeter change is $4−2j≤0$.

If a round adds several cells simultaneously, process those additions in any sequential order. Each new cell already had at least two marked neighbors before the round, and still has them when processed; additional previously processed cells only increase that number. The same nonincrease bound applies to the total round. A fully marked square has exterior perimeter $4n$. Starting with $k<n$ gives perimeter at most $4k<4n$, and nonincrease makes the target impossible. The marked-cell count increases, but that quantity alone cannot exclude the target. The perimeter uses geometric information about the boundary that the count discards.

### Problem 16. Prove the normal-play Nim strategy

**Course-derived · MIT Problem 5.37(a–d).** A move removes a positive number of stones from one pile. The player unable to move loses. Prove the zero-XOR strategy and give a concrete response for piles of sizes two, two, and one.

**Solution.** Let $z$ be the bitwise XOR of all pile sizes, and write $⊕$ for XOR. If $z=0$, changing one pile from $a$ to a smaller $b$ changes the XOR to $a⊕b$, which is nonzero because the sizes differ. Thus a move from zero XOR never returns zero XOR.

If $z≠0$, locate the highest set bit of $z$. At least one pile $a$ has a one in that bit. Replace it by $b=a⊕z$. All more significant bits stay unchanged and the selected highest bit becomes zero, so $b<a$. The new XOR is $z⊕a⊕b=0$. For $(2,2,1)$, XOR is one; the usable pile is the size-one pile, which can be reduced to zero. The largest pile is not necessarily a usable pile.

The total number of stones strictly decreases at each move, so the game terminates. A player who can first move to zero XOR can restore zero XOR after every opponent move. A nonterminal zero-XOR position cannot have just one nonempty pile, so the opponent cannot remove the final stones directly from such a position. The strategy player eventually makes the final removal and wins. The maintained assertion is at a designated turn boundary, after the strategy player's moves; zero XOR is not preserved after every individual move by both players.

### Problem 17. Repair the strategy for misère Nim

**Course-derived · MIT Problem 5.37(e).** Now the player taking the last stone loses. Derive the adjustment to the normal-play strategy.

**Solution.** If all nonempty piles have size one, every move removes exactly one pile. With an odd number of such piles, the player to move takes the last stone and loses under perfect play; with an even number, that player can leave an odd number and win. This reverses the normal zero-XOR conclusion in the all-ones case.

If exactly one pile exceeds one, let $k$ be the number of one-stone piles. Reduce the large pile to one when $k$ is even, or to zero when $k$ is odd. Both are legal reductions, and both leave an odd number of one-stone piles to the opponent. Hence such a position is winning.

If at least two piles exceed one, use the ordinary XOR rule. A move to zero XOR cannot leave exactly one large pile, since XOR of the small piles is zero or one and cannot cancel a number greater than one. It also cannot eliminate all large piles with one move when at least two existed. Thus the zero-XOR response stays in the large-pile regime until an opponent eventually leaves exactly one large pile, at which point switch to the preceding odd-ones rule. From a zero-XOR position with large piles, every move leaves nonzero XOR; it either stays in that regime and admits a restoring response, or leaves exactly one large pile and admits the special response. This proves that such zero-XOR positions are losing and establishes the complete strategy, with the empty initial game interpreted separately according to the chosen terminal convention.

### Problem 18. A positive descending quantity can run forever

**Original · Ranking counterexample.** A state is a positive real number and its only step replaces it by half its value. Does strict decrease prove termination?

**Solution.** Starting from one gives $1,1/2,1/4,…$, an infinite execution of positive real states. Each new value is smaller, but the range is not well-founded under the usual order. It has infinite descending chains. A lower bound of zero does not imply that the process reaches zero. If the guard instead permits a step only when the value exceeds a fixed positive threshold, one can derive a finite halving bound; that is a different transition system. The domain, guard, and rank order must all be part of the proof.

### Problem 19. Two other incorrect termination arguments

**Original · Strictness and boundedness.** Give separate counterexamples to “a nonnegative integer quantity never increases, so the process terminates” and “an integer quantity strictly decreases, so the process terminates.”

**Solution.** A self-loop at a state of rank zero keeps a nonnegative integer quantity constant forever, refuting the first assertion. A system with states all integers and transitions $z→z−1$ has a strictly decreasing integer quantity but follows $0,−1,−2,…$ forever, refuting the second assertion. The natural-number theorem excludes both failures: it requires strict decrease and nonnegative values at every reached state. If a candidate rank becomes negative under an enabled move, its promised codomain has failed even if the formula is algebraically decreasing.

### Problem 20. Termination without a uniform length bound

**Course-derived · MIT Section 5.4.6, coordinate order changed.** A robot has state $(y,x)∈ℕ^2$. It may decrease positive $x$ by one, or decrease positive $y$ by one while resetting $x$ to any nonnegative integer. Prove termination from every state and show that lengths from $(1,0)$ have no common finite bound.

**Solution.** Every move decreases $(y,x)$ lexicographically. The first coordinate can drop only finitely many times; between drops, the second coordinate decreases through nonnegative integers. Hence there is no infinite execution. The only dead end is $(0,0)$, so every maximal execution reaches it. From $(1,0)$, choose the reset $(0,M)$ and then make $M$ decrements. This execution has $M+1$ transitions for any chosen natural $M$. A uniform bound would have to exceed every natural number, which is impossible. This does not contradict termination: each selected reset is finite, but the family of possible choices has unbounded size. The weighted sum $cy+x$ fails to decrease when the reset chooses $M$ larger than $c$.

### Problem 21. Turn bounded lexicographic progress into a scalar rank

**Original · Constructive ranking.** Repeat Problem 20 with every reset restricted to $0≤x≤B$. Construct a natural-valued rank and a length bound.

**Solution.** Use $ρ(y,x)=(B+1)y+x$. A secondary decrement lowers the rank by one. A primary decrement followed by a reset changes it by $−(B+1)+x'−x≤−(B+1)+B=−1$, since old $x≥0$. Thus the rank strictly decreases and remains nonnegative. Every execution from $(y_0,x_0)$ has at most $(B+1)y_0+x_0$ transitions. The initial $x_0$ need not be bounded by $B$ for this proof; only reset values need that bound. This sharper observation follows from the explicit change calculation rather than an unnecessary global restriction.

### Problem 22. Goal reachability does not imply inevitable arrival

**Original · Nondeterminism.** State zero has edges to itself and to a terminal goal. Is the goal reachable? Does every execution eventually reach it? What assumption would alter the answer?

**Solution.** The one-edge path reaches the goal, so existential reachability is true. Repeating the self-loop yields an infinite execution avoiding the goal, so universal eventual arrival is false. An invariant describing permitted states does not distinguish these two behaviors. A fairness requirement that an exit continuously enabled at zero is eventually taken excludes the infinite self-loop execution, but this is an added execution assumption. If the program itself removes the self-loop, termination follows directly from the revised graph. A proof must state which system and which class of executions it quantifies over.

### Problem 23. Prove prefix-sum correctness with negative entries

**Original · Loop proof.** Trace and verify `prefix_sum` on $[4,−7,5]$. Explain why “the running sum increases” cannot be its termination argument.

**Solution.** Loop-head states $(i,total)$ are $(0,0),(1,4),(2,−3),(3,2)$. At each head the index lies between zero and three and the total equals the sum of exactly the processed prefix. Under $i<3$, accessing the indexed element is valid, and the two assignments extend the prefix equality. The exit state has index three and total two, the full sum. The total decreases on the second iteration, so an increasing-total claim would be false. Termination follows from the remaining-index rank $3−i$, whose values are three, two, one, and zero. On an empty array, the same invariant uses an empty sum and the same rank is initially zero; the loop returns immediately.

### Problem 24. Horner's rule as a suffix invariant

**Original · Algebraic loop proof.** Coefficients $a_0,…,a_{n−1}$ define a polynomial in ascending power order. A loop scans from the final coefficient backward, repeatedly assigning `value = value*x + coefficient`. Prove its result, including the empty coefficient list.

**Solution.** At the loop head let $i$ be the next coefficient index, initially $n−1$, and let `value` initially be zero. The invariant states that the accumulated value is the polynomial formed by coefficients with indices above $i$, shifted so its first coefficient has degree zero:

<div class="formula-block">$value=a_{i+1}+a_{i+2}x+⋯+a_{n−1}x^{n−i−2}$.</div>

When no coefficient has been processed, the right side is the empty polynomial zero. Updating multiplies every existing power by $x$ and adds $a_i$, producing $a_i+a_{i+1}x+⋯+a_{n−1}x^{n−i−1}$. Decrementing the index makes this exactly the same invariant at the new head. At exit $i=−1$, it becomes the requested polynomial $a_0+a_1x+⋯+a_{n−1}x^{n−1}$. Rank $i+1$ is nonnegative at all loop heads and decreases by one. If $n=0$, the initial index is minus one, no iteration occurs, and the result is zero. The displayed term formula is interpreted as an empty sum when its coefficient range is empty, rather than inventing an out-of-range coefficient.

### Problem 25. Merge correctness, duplicates, and exhaustion

**Course-derived · Stanford CS161 Section 1 and Princeton COS226 slides 7–8.** Merge two sorted finite sequences while preserving every occurrence. Give safe code, prove correctness and stability, and derive the maximum comparison count when both inputs are nonempty.

```python
def merge(left, right):
    i = 0
    j = 0
    out = []
    while i < len(left) or j < len(right):
        if j == len(right) or (
            i < len(left) and left[i] <= right[j]
        ):
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    return out
```

**Solution.** At the loop head, $0≤i≤m$, $0≤j≤n$, and the output contains exactly the occurrences of the consumed prefixes of lengths $i,j$. It is sorted, and every output occurrence is no greater than every remaining occurrence. Initially the output is empty, so these conditions hold vacuously. When both sequences have an unconsumed head, their smaller head is a minimum among all remaining elements because each input is sorted. Appending it therefore preserves sortedness and the comparison with remaining elements. When one side is exhausted, the other head is the remaining minimum. Incrementing the chosen index accounts for exactly one additional occurrence.

The guard guarantees at least one side is not exhausted. The condition uses short-circuit evaluation: if the right side is exhausted, its element is not accessed; otherwise the left comparison is made only if the left side is not exhausted. In the `else` branch the right side is known nonempty. Thus every access is valid, including when either original input is empty. At exit both prefixes are complete, so the output is sorted and has the original multiset. Rank $m+n−i−j$ decreases by one and proves termination after $m+n$ output steps.

Equal heads are selected from the left. If each input already preserves the original order of equal-key records and every left record originally precedes every right record in the split, this tie rule preserves stable order. Stable merging has a stronger requirement than merely sorting numbers. Comparisons between two heads occur only while both sides remain nonempty; by the time $m+n−1$ elements have been output, at most one remains. Hence at most $m+n−1$ head comparisons occur, and alternating sorted inputs attain this bound. Output steps and comparisons are different counts.

For the equal-length Princeton comparison question, when each input has length $N/2$, at least $N/2$ head comparisons are needed to exhaust one side, and this minimum is attained when every entry of one side precedes every entry of the other. The worst case is $N−1$. Here $N$ is a positive even integer and the count excludes the boundary-condition checks.

### Problem 26. Exact exponent-halving counts

**Course-derived · MIT Section 5.4.5 and Problem 5.36.** The positive exponent is replaced by its integer quotient by two on each body iteration. Derive the exact number of such iterations and audit a claimed ceiling-logarithm formula.

**Solution.** After $k$ iterations the exponent is $⌊n/2^k⌋$. Induction establishes this because integer halving commutes with taking the quotient by an integer power of two. For $n>0$, the first zero occurs when $2^k>n$, so the exact count is $⌊log_2 n⌋+1$. For zero it is zero. A claim that the exact count is $⌈log_2 n⌉+1$ is false at nonpowers of two: $n=3$ follows three, one, zero in two body iterations, whereas that expression gives three. The ceiling expression is a valid upper bound, not the exact body count. If a terminal return action is itself counted as a separate transition, add that explicitly; guard checks are another distinct count. Counting conventions must be fixed before comparing results.

In the iterative power routine, at most two multiplications occur per positive iteration: one squaring and possibly an accumulator multiplication. Under that implementation, the exact accumulator-multiplication count is the number of one bits in $n$, and the squaring count is the bit length. An implementation that skips the unused final squaring has a different constant count while preserving the same result.

### Problem 27. Recursive power needs integer arguments

**Course-derived · Stanford CS161 Section 1, generalized base.** Prove the recursive `power` routine in the lesson and explain why real division breaks its termination proof.

**Solution.** Use the joint claim that for every scalar $a$ and natural $n$ the routine terminates and returns $a^n$. At zero it returns one. For positive $n$, the recursive argument $q=⌊n/2⌋$ is a smaller natural. Strong induction gives a returned value $a^q$. Even input satisfies $n=2q$, so squaring that value is correct. Odd input satisfies $n=2q+1$, so multiplying the square by $a$ is correct. Arithmetic completes in the mathematical model, establishing the joint claim.

If the odd branch instead passes $n/2$ as a real and stops only at exact zero, input one can produce $1/2,1/4,…$ rather than a base-case argument. The recursive-call domain is violated and the natural ranking no longer applies. Testing an even input would miss this issue. With negative exponents, a separate reciprocal specification and a nonzero-base precondition are needed; the current routine is not specified for them.

### Problem 28. Repeated subtraction and quotient-remainder correctness

**Original · Combined conservation and ranking.** Given integer $a≥0$ and $b>0$, initialize $q=0$, $r=a$. While $r≥b$, increment $q$ and subtract $b$ from $r$. Prove the final quotient-remainder relation.

**Solution.** Maintain $a=bq+r$, $q≥0$, and $r≥0$. Initialization establishes the equation. A body update gives $b(q+1)+(r−b)=bq+r=a$, and the guard ensures the new remainder is nonnegative. Rank $r$ strictly decreases by the positive integer $b$, so termination follows. At exit $0≤r<b$ and $a=bq+r$, which is the quotient-remainder specification. Uniqueness follows independently: if $bq+r=bq'+r'$ with both remainders in the interval from zero to $b−1$, then $b(q−q')=r'−r$. The right side has absolute value less than $b$, so the only possible multiple of $b$ is zero; thus both quotient and remainder agree. If $b=0$, the guard and update permit an infinite unchanged remainder, so the strict positive-divisor precondition is necessary.

### Problem 29. Euclid as invariant plus decreasing remainder

**Original · Recursive reasoning, number-theory preview.** For nonnegative integers $a,b$ not both zero, repeatedly replace $(a,b)$ by $(b,r)$ when $b>0$, where $r$ is the remainder of division of $a$ by $b$, and return $a$ at $b=0$. Prove the result is the greatest common divisor.

**Solution.** Use the unique remainder $r$ with $a=qb+r$ and $0≤r<b$. A positive integer divides both $a$ and $b$ exactly when it divides both $b$ and $r$: subtraction of $qb$ proves one direction, and addition proves the other. Thus the entire set of common positive divisors is conserved, so its greatest member is conserved. The new second coordinate is a smaller nonnegative integer, giving a ranking and termination. At $(a,0)$, the first coordinate is positive because the original pair was not both zero and the update cannot create that pair from a valid nonzero pair. The common positive divisors are precisely the positive divisors of $a$, whose greatest member is $a$. The returned value is therefore the original greatest common divisor. The same proof supports the recursive version with measure equal to the second argument. This proof uses remainder bounds rather than an unjustified assertion that both coordinates always decrease.

### Problem 30. Audit four recursive definitions

**Course-derived · MIT Section 6.3.2, independently chosen equations.** Determine what goes wrong with a recurrence lacking a base value, a routine moving toward larger positive arguments, conflicting cases, and a routine calling itself twice on smaller arguments.

**Solution.** The equations $f(n+1)=f(n)+2$ without $f(0)$ admit the whole family $f(n)=c+2n$, so they do not specify a unique function. A routine with `f(0)=0` and `f(n)=f(n+1)` for positive naturals has an increasing call chain and does not terminate there, even though many constant-on-positive-input mathematical assignments satisfy the equations. Clauses demanding value zero on every even input and value one on every multiple of three conflict at six unless interpreted with a specified priority; unordered mathematical equations are inconsistent there. Finally, making two calls on $n−1$ with a valid zero base is mathematically terminating: strong induction justifies both smaller calls, and finite branching makes the whole recursion tree finite. It may have exponential work, but inefficiency is not nontermination. Evaluate domain, consistency, totality, and cost separately.

### Problem 31. Prove the concatenation laws from the constructors

**Course-derived · MIT Problem 6.1; CMU structural notes, Lemmas 2–3; Cornell Lecture 21.** Prove totality, right identity, length additivity, and associativity for finite-list concatenation.

**Solution.** Concatenation recurses only on its first list. Induct on that list. At the empty list it returns its second argument immediately, proving totality. At $Cons(x,L)$, the induction hypothesis gives a finite returned tail for concatenating $L$ with any second list, and applying one constructor returns a finite list. Right identity has empty case $[]⧺[]=[]$ and step $Cons(x,L)⧺[]=Cons(x,L⧺[])=Cons(x,L)$ by the hypothesis.

For length additivity, the empty case is $len(M)=0+len(M)$. The step gives $len(Cons(x,L)⧺M)=1+len(L⧺M)=1+len(L)+len(M)$, which is the required expression. For associativity, the empty case reduces both expressions to $M⧺N$. The step reduces the left expression to $Cons(x,(L⧺M)⧺N)$, applies the associativity hypothesis to its tail, and reconstructs $Cons(x,L)⧺(M⧺N)$. Each theorem quantifies over arbitrary other lists, so recursive uses remain legal. Equality of outputs does not imply equality of allocation cost; associativity regroups copying operations.

### Problem 32. Reversal is an involution

**Course-derived · MIT Problem 6.2 and Cornell Lecture 21 review exercises.** Prove the reversal-of-concatenation identity and then prove $rev(rev(L))=L$.

**Solution.** First prove $rev(L⧺M)=rev(M)⧺rev(L)$ by induction on $L$ with arbitrary $M$. For the empty case, both sides reduce to $rev(M)$ using right identity. For $Cons(x,L)$, unfold concatenation and reversal to obtain $rev(L⧺M)⧺[x]$. The hypothesis changes this to $(rev(M)⧺rev(L))⧺[x]$. Associativity turns it into $rev(M)⧺(rev(L)⧺[x])$, the desired right side.

Now induct on $L$ for involution. The empty case is immediate. For a constructor, $rev(Cons(x,L))=rev(L)⧺[x]$. Apply the proved concatenation-reversal identity to reverse it again, obtaining $rev([x])⧺rev(rev(L))=[x]⧺L=Cons(x,L)$, using the induction hypothesis and the reversal of a singleton. This proof depends on an auxiliary lemma; simply writing that reversal “obviously cancels” would hide the recursive justification. Length preservation follows similarly from length additivity and the reversal equation.

### Problem 33. Accumulator reversal with a nonempty suffix

**Course-derived · CMU List Reversal, theorem and thought questions.** Prove the generalized helper specification and compute $revAcc([1,2,3],[8,9])$.

**Solution.** The appropriate statement is $revAcc(L,A)=rev(L)⧺A$ for every accumulator. For $L=[]$, both expressions give $A$. For $Cons(x,L)$, the function calls $revAcc(L,Cons(x,A))$. The hypothesis is universally quantified over accumulators, so apply it to that changed value, obtaining $rev(L)⧺Cons(x,A)$. By the concatenation definition, $Cons(x,A)=[x]⧺A$. Associativity gives $(rev(L)⧺[x])⧺A$, which is $rev(Cons(x,L))⧺A$.

The successive accumulators in the example are $[8,9]$, $[1,8,9]$, $[2,1,8,9]$, and $[3,2,1,8,9]$. The result agrees with the proved reversed-prefix-plus-suffix specification. A one-way evaluation step establishes output equality, and equality can subsequently be used in either direction; this explains why a constructor equation may be cited backward in an equational proof. Such symmetric equality does not mean that the evaluator runs backward. Restricting the hypothesis to an empty accumulator would fail at the first recursive step.

### Problem 34. An accumulator that traverses right before left

**Course-derived · CMU structural notes, Lemma 5 and Theorem 6.** Verify $flatAcc(T,A)=flatten(T)⧺A$ and trace it on $Node(Leaf(2),Node(Leaf(5),Leaf(7)))$ with accumulator $[9]$.

**Solution.** The leaf case returns $Cons(v,A)=[v]⧺A$. At a node, evaluate the right helper first. Its hypothesis gives $flatten(R)⧺A$, a finite list. The left hypothesis applies to this entire changed accumulator, giving $flatten(L)⧺(flatten(R)⧺A)$. Associativity changes this to $flatten(Node(L,R))⧺A$. Both subtree hypotheses are required; totality follows simultaneously from strict subtree descent and finite constructor work.

For the example, the rightmost leaf puts seven before nine, then the leaf five puts five before that suffix, and finally the left leaf two puts two before everything. The result is $[2,5,7,9]$. The traversal order of helper evaluation is seven, five, two, but the final order of data is two, five, seven. A wrapper with accumulator $[]$ therefore computes left-to-right leaf order. Claiming that right-first evaluation reverses the output would confuse evaluation sequence with list construction.

### Problem 35. Full binary-tree identities and missing-child traps

**Course-derived · MIT Problem 6.5(c) and Cambridge tree equations.** Derive internal-node, leaf, and total-node identities for leaf-labeled full trees. Explain why a general binary tree has a different interpretation.

**Solution.** At a leaf, internal count is zero, leaf count is one, and total count is one. At $Node(U,V)$, add one internal node to the sum of child internal counts and add the child leaf counts without another leaf. Assuming $L_f(U)=I(U)+1$ and $L_f(V)=I(V)+1$ gives $L_f(U)+L_f(V)=I(U)+I(V)+2=I(Node(U,V))+1$. Thus $L_f=I+1$, and total count $N=I+L_f=2L_f−1$. Since flattening lists exactly one value per leaf, $2len(flatten(T))=N+1$ follows, including the single-leaf case.

A general binary tree can have a unary node. A two-node chain has one internal node and one nonempty leaf, so the same equation would falsely demand two leaves. For the empty-or-node representation, however, counting **external empty children** restores a related identity: each added stored node adds one net external position, so external positions equal stored nodes plus one. The identity concerns the constructor representation, not whichever quantity has casually been called a leaf.

### Problem 36. Height bounds and equality cases

**Course-derived · Cambridge printed page 65.** With empty-tree height zero and node height one plus the maximum child height, prove $N≤2^h−1$ and characterize equality.

**Solution.** An empty tree has $N=0$ and $h=0$, so equality holds. For a nonempty tree of height $h$, both children have height at most $h−1$. Applying the induction bounds gives $N≤1+2(2^{h−1}−1)=2^h−1$. Equality requires both child node bounds to be equalities and both child heights to be exactly $h−1$, because the exponential bound strictly grows with height. Recursively this is a perfect binary tree with every level filled. A skew chain has $N=h$ and satisfies the bound without equality except in the smallest cases. With a data-bearing leaf assigned height zero instead, the total-node formula becomes $2^{h+1}−1$; using the wrong convention creates an off-by-one exponent, not a contradiction in the mathematics.

### Problem 37. A construction count that is not a function of the object

**Course-derived · MIT Section 6.2.** A generated string set contains the empty string and allows concatenation. Proposed cost is zero for the empty string and one plus both input costs for concatenation. Diagnose the definition and give two repairs.

**Solution.** The same empty string can be regarded as a base object or as the concatenation of two empty strings. The base equation assigns zero, while the concatenation equation assigns $1+0+0=1$. Consequently the proposed equations do not define a function on strings. One repair changes the domain to explicitly tagged derivation trees, keeping `BaseEmpty` distinct from `Concat(BaseEmpty,BaseEmpty)`; their different costs then refer to different inputs. Another repair defines an object-level measure such as string length and uses a concatenation equation without the extra one. That measure is independent of the derivation. General well-definedness requires checking that all representations of the same object produce the same value; a terminating recursive computation on derivations alone does not prove that independence.

### Problem 38. Mutual recursion and a phase rank

**Original · Joint induction.** Prove parity routines that call one another on $n−1$. Then justify the variant in which `even(n)` calls `odd(n)` without decrement, while `odd(n)` calls `even(n−1)` for positive $n$.

**Solution.** For the first pair, assume `even(0)=True`, `odd(0)=False`, and for $n>0$ each routine returns the other routine's answer on $n−1$. Joint induction asserts that both terminate and report their respective parity at every natural input. The two base values are correct. At a positive input, the opposite parity of $n−1$ is exactly the requested parity of $n$, and the induction hypothesis justifies both calls.

For the same-size variant, a consistent definition is `even(n)=not odd(n)` for $n>0$, and `odd(n)=even(n-1)` for $n>0$, with the same base values. Rank calls by $(n,phase)$, assigning phase one to `even` and zero to `odd`. The first call decreases the phase at fixed input; the second decreases input and may reset phase. Both edges therefore decrease lexicographically. Correctness follows from the same rank induction: `odd(n)` returns the evenness of $n−1$, and `even(n)` negates that result. Without the negation, the altered pair would terminate but give incorrect answers; a ranking proves totality, not the parity specification.

### Problem 39. Nested recursion can increase a secondary argument

**Course-derived · MIT Section 6.3.2, two explicitly distinguished variants.** Prove totality of the standard Ackermann equations in the lesson and of the MIT variant $B(m,n)=2n$ at $m=0$ or $n≤1$, otherwise $B(m−1,B(m,n−1))$.

**Solution.** Use lexicographic induction on the natural pair with first coordinate primary, and include natural-valued output in the proposition. For the standard variant, zero first coordinate returns a natural. At positive first coordinate and zero second coordinate, the recursive call has smaller first coordinate, even though its second coordinate is one. For positive second coordinate, the inner call has the same first coordinate and a smaller second coordinate. It terminates and produces a natural $u$. The outer call has smaller first coordinate and second coordinate $u$, so the hypothesis applies regardless of $u$'s size. Both computations and the surrounding finite work terminate.

For $B$, its base cases return a natural directly. Otherwise $m>0$ and $n>1$, so the inner call $(m,n−1)$ is smaller. Its natural result is a legal input to the outer call whose first coordinate is $m−1$. The same induction therefore proves totality. For a check on conventions, $B(1,2)=B(0,B(1,1))=B(0,2)=4$, while the standard variant has $A(1,2)=4$ but different other base-row values, since $A(0,n)=n+1$ and $B(0,n)=2n$. Agreement on a few inputs does not make these definitions identical.

### Problem 40. Prove substitution for every expression constructor

**Course-derived · MIT Theorem 6.4.4, argument order made explicit.** Prove $eval(subst(E,H),z)=eval(E,eval(H,z))$ for the pure expression type in the lesson.

**Solution.** Induct on $E$ with arbitrary $H,z$. For $Const(k)$, substitution leaves it unchanged and both sides give $k$. For $Var$, substitution returns $H$ and both sides give $eval(H,z)$. For $Add(U,V)$, the left side is the sum $eval(subst(U,H),z)+eval(subst(V,H),z)$. Apply the hypotheses for both children and recover evaluation of the addition at variable value $eval(H,z)$. For $Mul(U,V)$, the left side is the product of those substituted-child values; applying their hypotheses recovers evaluation of the multiplication at the new variable value. For $Neg(U)$, the left side is the negative of the substituted-child value; applying its hypothesis gives the negative of $eval(U,eval(H,z))$, which is evaluation of the negation. Every constructor is covered. All subexpressions are strictly smaller finite trees, so the recursive definitions terminate. The proof would need revision if evaluating $H$ had side effects, because substitution could duplicate that evaluation.

### Problem 41. Sum a list with an accumulator

**Course-derived · Cambridge Exercise 3.1 and CMU lecture-code accumulator pattern.** Give direct and accumulator definitions for summing integer lists, prove their equivalence, and explain the space qualification.

**Solution.** Define $sum([])=0$ and $sum(Cons(x,L))=x+sum(L)$. Define $sumAcc([],a)=a$ and $sumAcc(Cons(x,L),a)=sumAcc(L,a+x)$. Prove $sumAcc(L,a)=a+sum(L)$ for all integers $a$ by induction on $L$. The empty case is $a=a+0$. In the step, the hypothesis at the changed accumulator gives $(a+x)+sum(L)$, equal by associativity to $a+(x+sum(L))$, the claimed expression. The input length strictly decreases in both definitions and establishes termination.

Both visit each linked-list element once and use a linear number of additions. The direct routine has pending additions on its call stack; the accumulator routine is tail recursive. Constant auxiliary stack space requires a language/runtime that eliminates tail calls, or an explicit loop. Integer bit sizes and output storage still have their own costs. An implementation using Python slices copies suffixes and does not inherit the linked-list cost merely because its mathematical recurrence looks similar.

### Problem 42. The last element requires a nonempty domain

**Course-derived · Cambridge Exercise 3.2.** Define and verify a last-element routine for a nonempty finite list.

**Solution.** Use $last([x])=x$ and $last(Cons(x,Cons(y,L)))=last(Cons(y,L))$. The two cases cover every nonempty finite list; the recursive argument remains nonempty and has one fewer element. Induct on positive length. Length one returns its unique and final element. For a longer list, the hypothesis says the shorter tail's routine returns its last element, which is also the last element of the original list. Thus total correctness holds on the stated domain. A linked-list implementation takes one traversal and linear time, because there is no direct final-node index. The empty list has no final element, so either exclude it by the precondition or return an explicitly defined optional result; leaving the case unspecified and claiming totality on all lists is wrong.

### Problem 43. Select the even-numbered positions

**Course-derived · Cambridge Exercise 3.3.** Positions are counted from one. Define a routine returning the entries at positions two, four, six, and so on, and prove it on lists of both parities.

**Solution.** Define $evens([])=[]$, $evens([x])=[]$, and $evens(Cons(x,Cons(y,L)))=Cons(y,evens(L))$. The base cases cover zero and one element. The recursive case removes two elements, so the remaining list's even-numbered positions correspond exactly to original positions four, six, and onward. Under the induction hypothesis, the recursive answer contains precisely those entries in original order; adding $y$ first adds original position two and proves the full specification. Length decreases by two and cannot drop indefinitely below zero, establishing termination. For $[a,b,c,d,e]$ the result is $[b,d]$; for $[a,b,c,d,e,f]$ it is $[b,d,f]$. Using only an empty base would miss the singleton input reached from odd lengths.

### Problem 44. Generated sets need both inclusions

**Course-derived · MIT Problem 6.4(a–f), structural and numeric extension.** Give recursive generators for products $2^k3^m5^n$, products $2^k3^{2k+m}5^{m+n}$ with nonnegative exponents, and pairs of integers whose coordinate difference is divisible by three. Prove the claimed sets rather than only closure.

**Solution.** For the first set, start from one and allow multiplication by two, three, or five. Structural induction proves that each generated value has the required exponent form, since a move increments one exponent. Conversely, apply the corresponding move counts to generate any chosen exponent triple. Thus both inclusions hold.

For the second set, start from one and allow multiplication by eighteen, fifteen, or five. These moves increment $k,m,n$ respectively in the target expression. Structural induction proves soundness; repeating the first move $k$ times, the second $m$ times, and the third $n$ times proves completeness. Products can have several derivation orders, but membership does not require a unique derivation.

For the pair set, start at $(0,0)$ and allow addition or subtraction of $(1,1)$ and of $(3,0)$. Each move preserves a coordinate difference divisible by three. For any target $(a,b)$ with $a−b=3q$, take $b$ signed diagonal moves to reach $(b,b)$, then $q$ signed horizontal-three moves to reach $(a,b)$. Negative signed counts mean use the opposite generator. This proves completeness for all integers, not merely nonnegative coordinates.

An unambiguous alternative is a tagged representation `(Diag(b),Offset(q))` with two integers, interpreted as $(b+3q,b)$. Every permitted pair uniquely determines $b$ and $q=(a−b)/3$, so the coordinate representation is unique. Build each signed integer with a canonical sign and a unary natural magnitude; require positive magnitude for a negative tag to avoid two representations of zero. Arbitrary orderings of the original move sequence are not unique; the canonical pair representation repairs that issue explicitly.

One can also give unambiguous recursive rules directly on coordinates. Start at $(0,0)$. On the horizontal axis, allow $(a,0) → (a+3,0)$ only when $a ≥ 0$, and allow $(a,0) → (a−3,0)$ only when $a ≤ 0$. For diagonal moves, allow $(a,b) → (a+1,b+1)$ when $b ≥ 0$, and $(a,b) → (a−1,b−1)$ when $b ≤ 0$. Every rule moves away from the axis or from its origin; a diagonal move never returns to the axis, so horizontal moves necessarily precede diagonal moves. These restrictions preserve divisibility of $a−b$ by three. To generate any target, first reach $(3q,0)$ by the unique signed horizontal sequence, then take the unique signed diagonal sequence of length $|b|$. Completeness follows because $q=(a−b)/3$ is an integer. Uniqueness follows backwards: a target with positive $b$ has only predecessor $(a−1,b−1)$, one with negative $b$ has only predecessor $(a+1,b+1)$, and a nonzero axis target has only the horizontal predecessor closer to zero. The origin has no predecessor. Thus both membership and unique derivability are proved, rather than inferred from a drawing.

### Problem 45. Prove a pure expression simplifier

**Original · Structural synthesis.** Recursively simplify expression children and replace `Add(E,Const(0))` by the simplified child. Prove value preservation and explain why it does not establish optimal simplification.

**Solution.** Induct on the original finite expression. Constants and the variable are unchanged. For each addition, multiplication, or negation, induction preserves the values of the recursively simplified children. Reconstructing a constructor therefore preserves its evaluation. If an addition's simplified right child is zero, dropping it preserves value because integer addition has zero as a right identity. This includes every case of the routine and proves preservation for all integer variable assignments. The recursive calls inspect strict subtrees of the original input, so they terminate.

The routine need not eliminate `Add(Const(0),E)`, a product by zero, or other algebraic redundancies. Soundness means that whatever transformation it performs preserves value; completeness or optimality of simplification requires a separate goal and argument. If constructors had side effects, discarding a zero-valued expression could discard an effect and invalidate the proof. The pure-expression assumption is therefore substantive.

### Problem 46. A failed proposed rank can coexist with termination

**Original · Certificate versus decision.** On the chain $0→1→2→3$, a proposed rank assigns zero to every state. Explain the failure and construct a valid rank. Then add an unreachable self-loop at an extra state four.

**Solution.** The proposed rank is nonnegative but does not strictly decrease on any chain edge, so that certificate fails. The graph is nevertheless acyclic and every execution from zero has at most three transitions. Rank values three, two, one, zero on the four chain states decrease exactly by one. The extra self-loop prevents a globally decreasing rank covering every graph edge, but it is unreachable from zero. The same reachable-state rank still proves termination from the stated initial state. If four is added to the initial set, its infinite self-loop becomes an execution and universal termination fails. Rank scope and initial-state scope must be explicit.

### Problem 47. Strengthen a bound with quantitative slack

**Course-derived · Berkeley CS70 Note 4, pages 5–6.** Prove that the sum of reciprocal squares from one through $n$ is at most $2−1/n$ for every integer $n≥1$, and explain why the weaker bound two is difficult to induct on directly.

**Solution.** Let $S_n$ denote that finite sum. At one, $S_1=1=2−1$. Assume $S_k≤2−1/k$ for $k≥1$. Then $S_{k+1}≤2−1/k+1/(k+1)^2$. The amount needed to make this at most $2−1/(k+1)$ is exactly the inequality $1/(k+1)^2≤1/k−1/(k+1)=1/(k(k+1))$. Positive denominators and $k≤k+1$ prove it. Hence induction yields the claimed bound. The direct hypothesis $S_k≤2$ only gives $S_{k+1}≤2+1/(k+1)^2$, which does not imply the goal. The stronger statement supplies enough numerical slack to pay for the next positive term. The algebra is used for $k≥1$; inserting zero into the denominators would be invalid.

### Problem 48. Write an exact finite invariant checker

**Original · Implementation and witness reasoning.** Explain an algorithm that separates initialization failure, preservation failure, and reachable safety failure, and show why its witness is valid.

**Solution.** Represent the finite transition relation by adjacency lists. Check initialization directly by testing membership of every initial state in the proposed truth set. Check preservation by scanning each edge whose source belongs to that set and recording any target outside it. Independently run breadth-first search from the initial states, adding an unseen successor and recording its predecessor. Every discovered state has a path from an initial state by induction on discovery steps, and every reachable state is eventually discovered by induction on its shortest path length. Thus the computed set is exactly reachable.

If a reached state is outside the predicate, follow predecessor links back to an initial state and reverse the sequence to obtain a valid violating execution prefix. Breadth-first search supplies a shortest such prefix. If initialization fails, that prefix may have zero transitions. If only preservation fails, the recorded bad edge's source might be unreachable, as in Problem 2; it should not be mislabeled an execution witness. Cycle detection on the reachable subgraph separately decides universal termination in this finite model. These different reports explain **which obligation** failed and do not infer one failure from another.

### Problem 49. A guarded population process: exact bound and termination

**Course-derived · MIT Problem 5.42, independent starting counts.** Start with twelve blue and seven red tokens. As long as blue count exceeds red count, one may add one red, remove one blue, add two reds and one blue, or remove two blues and one red when available. Specify an invariant, derive the exact number of steps in a maximal execution, and find the largest possible total population.

**Solution.** The state is a nonnegative integer pair $(b,r)$, initially $(12,7)$. The four changes are $(0,1)$, $(−1,0)$, $(1,2)$, and $(−2,−1)$. Each requires $b>r$; removals additionally require sufficient tokens. In every case the difference $d=b−r$ decreases by exactly one. Because an enabled step has integer $d≥1$, its successor has $d≥0$. Thus the nonnegative-difference predicate is initialized and preserved, and $d$ is a strictly decreasing natural rank on enabled transitions.

Initially $d=5$. At every state with positive difference, adding one red is available, so a maximal execution cannot stop early. It therefore has exactly five transitions and finishes with equal counts. The initial population is nineteen; each step increases it by at most three, so no intermediate population exceeds $19+3⋅5=34$. Apply the two-reds-and-one-blue addition five times to attain $(17,17)$ and total thirty-four. This simultaneously proves the bound is tight and checks the guards on the witness. Ranking counts maximal transitions here because positive-rank states always have an enabled step; without that progress observation it would establish only an upper bound.
