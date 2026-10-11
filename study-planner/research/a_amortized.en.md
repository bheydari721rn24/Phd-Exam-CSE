# Amortized Analysis and Dynamic Resizing

## 1. Sources, prerequisites, and chapter scope

The four core written courses are MIT 6.046J, CMU 15-451/651, Princeton COS423 and Stanford CS166. ETH Zurich supplies an additional reviewed comparison. The linked source audit records complete reading ranges, instructor verification, inaccessible candidates and corrections. Sources agree on the central idea but sometimes use different primitive costs or resize timing; those differences matter when a question asks for an exact number.

Prerequisites are geometric series, binary representation, asymptotic notation, stacks, queues, arrays and elementary induction. This chapter develops a method for every legal operation sequence, including adversarial sequences. It extends earlier array and heap chapters by deriving proof coefficients, endpoint terms, hysteresis conditions and failure examples. It does not certify every unseen examination question.

## 2. What is being bounded?

Let $D_0$ be the initial data-structure state. Operation $i$ transforms $D_{i-1}$ into $D_i$ and costs $c_i\geq0$ measured in specified primitives. The sequence length $N$ counts public operations, not the number of elements currently stored. A statement that total cost is at most $aN+b$ means the same constants work for every legal sequence from the permitted initial state. The expensive operation can occur anywhere that the state permits it.

In the laboratory, $T$ denotes cumulative real work and $A$ denotes cumulative amortized charges. The displayed endpoint formula $T=A+\Phi_0-\Phi_N$ is evaluated only when the current public operation is complete. Storage positions are numbered; labels beginning with K identify records and labels beginning with I identify original input indices. These identifiers follow objects even when their storage positions change.

Worst-case time for one operation maximizes that operation's cost over reachable states. Amortized time bounds a complete sequence by relating its operations. Average-case time averages over a distribution on inputs. Expected time averages over specified random choices. These are different quantifiers. A deterministic two-stack queue has constant amortized time without any assumption that inputs are random; a randomized hash table can instead have expected amortized time.

The phrase constant amortized cost does not mean constant response time. If an append copies a million records, that particular append remains expensive even when earlier cheap appends pay for it in a proof. Throughput and latency answer different questions.

## 3. Aggregate analysis and prefix validity

Aggregate analysis directly bounds the sum of real costs. If each of $P$ inserted records can be removed at most once, total removals are at most $P$ even when one call removes many records. Charging every call its largest individually possible cost loses this dependency.

The bound must hold for every prefix that the theorem allows. A future operation cannot retrospectively rescue an earlier prefix whose required upper bound has already failed. For an initially empty stack with push cost one and removal cost one, total element work is at most $2P\leq2N$. If every public call also costs one for dispatch/checking, add $N$. Empty multipop calls then have cost one rather than zero. State the chosen model before quoting an exact charge.

## 4. Accounting: where credits live

Assign a charge $a_i$ to each operation and maintain balance $B_i=B_{i-1}+a_i-c_i$. If $B_0=0$ and every prefix has $B_i\geq0$, then actual total is no larger than total charges. A proof must specify what carries the credits and which event consumes them. For a stack, charge two for a push: one pays for insertion and one stays with that record until removal. A record cannot spend the same credit twice.

For a structure that starts nonempty, unused removal credits must be supplied initially or the final bound must include the starting workload. Saying that the credits are on the records is insufficient if those records were never charged in the analyzed sequence. When comparing different operations, different charges are allowed; a queue need not charge enqueue and dequeue equally.

## 5. Potential: the full telescoping theorem

Choose a real-valued state function $\Phi$. Define the amortized charge by

$$\widehat c_i=c_i+\Phi(D_i)-\Phi(D_{i-1}).$$

Summing cancels every internal endpoint, leaving the exact identity

$$\sum_{i=1}^{N}c_i=\sum_{i=1}^{N}\widehat c_i+\Phi(D_0)-\Phi(D_N).$$

If every reachable endpoint satisfies $\Phi(D_N)\geq\Phi(D_0)$, the charge sum directly upper-bounds actual work. The common sufficient condition $\Phi(D_0)=0$ and $\Phi\geq0$ is convenient but not logically necessary. If only $\Phi\geq0$ is known and the initial potential is positive, keep the additive $\Phi(D_0)$ term. More generally, a known lower bound $L$ gives total work at most the charge sum plus $\Phi(D_0)-L$.

An individual charge can be negative: that means an operation releases more stored credit than its actual cost. It is not a negative running time. Adding the same constant to all potentials does not change any charge or endpoint difference. Multiplying a potential by a constant changes charges and is useful when one move costs several primitive units.

## 6. Deriving a potential rather than guessing

A useful potential increases during cheap preparation and drops during expensive cleanup. Begin with the exact expensive transition. Suppose cleanup costs $qm$ and changes a candidate state measure by $-m$. Multiply that measure by at least $q$ to pay for the cleanup. Then check every cheap transition and every reachable boundary.

For doubling arrays, free slots alone point in the wrong direction: a full array has zero free slots, then growth creates many free slots while also costing much. The potential rises when it should pay out. The expression $2n-C$ instead accumulates as a capacity-$C$ array fills. Clipping it at zero handles the initially sparse states.

Never cancel $O(m)$ against $-O(m)$ without choosing a concrete coefficient or a known upper-bound coefficient. The two hidden constants need not match. Potential design is an inequality problem with a cost contract, not symbolic cancellation of asymptotic labels.

## 7. Multipop stacks and initial workload

Our stack supports push, pop-if-nonempty, and multipop($k$), which removes $\min(k,n)$ elements for nonnegative integer $k$. In the element-only model, push costs one and a multipop that removes $r$ elements costs $r$. Take $\Phi=n$. A push has charge two; each removal has charge zero because $r$ units of potential pay $r$ units of work. With a constant call overhead, add that overhead to each charge.

A stack starting with $s$ records has initial potential $s$. Total element work is at most $2P+s$ for the analyzed pushes and removals. The additive term cannot be discarded when $s$ is an independent input parameter: one multipop can consume all $s$ initial records. A multipush($k$) that creates $k$ records must cost and be charged proportional to $k$; a constant bound per public call would be false.

<!-- SIM: stack -->

## 8. Binary counters: exact counts and overflow

For an unbounded nonnegative binary counter, increment clears its $t$ trailing one bits and sets the next zero. Actual bit flips are $t+1$. The potential is the number of one bits, so its change is $1-t$ and every increment has charge two. Starting from zero after $N$ increments, the exact total is

$$F(N)=\sum_{j\geq0}\left\lfloor\frac{N}{2^j}\right\rfloor=2N-\operatorname{popcount}(N).$$

To prove the second equality, write $N=\sum_j b_j2^j$. Each set bit contributes $2^{j+1}-1$ to the floor sum; summing gives twice the value minus the number of set bits. The first increment has one flip, not two; the unused one unit is the final potential.

For a width-$w$ counter that wraps modulo $2^w$, only bits $0$ through $w-1$ exist. Starting at zero, the exact count for any $N$ is $\sum_{j=0}^{w-1}\lfloor N/2^j\rfloor$. On an all-ones wrap, cost is $w$, potential drops by $w$, and charge is zero. For a nonzero initial state, retain its popcount as an additive term. If increment and decrement alternate around a carry boundary, every operation can flip $w$ bits; increment-only amortization does not prove constant cost for this enlarged operation set.

<!-- SIM: counter -->

## 9. Dynamic arrays: exact geometric copying

Consider an initially empty array of capacity one. Append doubles capacity only when the old array is full, copies all live records, then writes the new record. One record copy and one new-record write each cost one; allocation and index checks are excluded from this exact model. After $N\geq1$ appends, let $C=2^{\lceil\log_2 N\rceil}$, with $C=1$ for $N=1$. Copied capacities are $1,2,\ldots,C/2$, totaling $C-1$. Hence exact work is

$$T(N)=N+C-1<3N.$$

At $N=8$, no capacity-eight copy occurs: the array only becomes full. At $N=9$, that copy occurs and capacity becomes sixteen. This strict boundary is a frequent source of off-by-one answers. The number of expansions is $\lceil\log_2 N\rceil$ for positive $N$, and zero for $N=0$.

The theorem covers appending, not arbitrary position insertion. Front insertion shifts all existing elements; $N$ such operations cause $N(N-1)/2$ shifts regardless of how well resizing is amortized. The real operation cost includes both shifting and rebuilding.

## 10. Insert-only potential and general growth factors

Use $\Phi(n,C)=\max(0,2n-C)$. Initially it is zero. Without growth, the potential increase is at most two and actual cost is one, giving charge at most three. When old $n=C$ and the new state is $(C+1,2C)$, potential changes from $C$ to two. Actual work is $C+1$, so the charge is exactly three, including the capacity-one boundary.

For ideal exact capacity multiplication by fixed $r>1$, use

$$\Phi(n,C)=\max\left(0,\frac{rn-C}{r-1}\right).$$

A full table has potential $C$; after copying into capacity $rC$ and appending, potential is $r/(r-1)$. Both growing and ordinary appends have charge at most $1+r/(r-1)$. If integer capacities use $C'=\lceil rC\rceil$, the growth potential decreases at least as much when the new-state expression stays positive; if clipping occurs, the old $C$ potential still pays all copies, leaving charge one. Therefore the same upper bound works. It is an upper bound, not an exact identical charge after rounding.

As $r$ approaches one, the constant grows. Constant additive growth $C'=C+d$ instead copies an arithmetic series and produces quadratic total work for fixed $d$. Choosing $r=1+1/N$ for a workload of length $N$ does not give a uniform constant bound; the parameter itself changes with the input.

<!-- SIM: growth -->

## 11. Weighted primitives and allocation

If an ordinary append costs $u$ and moving an old record costs $v$, scale the insert-only potential by $v$. Charges are at most $u+vr/(r-1)$ under the reduced model. If allocating or clearing a new capacity-$rC$ buffer costs $arC$, the rebuild coefficient becomes $v+ar$ per old record. A potential scaled by that coefficient proves constant amortized cost for fixed $a,v,r$, but the numerical charge is larger.

Record moves can themselves be nonconstant. Copying a string of length $L$ is not a unit record move unless the array stores fixed-size handles. User-defined constructors, destructors, allocation failure and exception rollback require separate contracts. Pointer/reference invalidation affects correctness even when operation counts remain favorable. A time theorem does not automatically imply a safe client API.

## 12. Why naive halving thrashes

Starting from $n=C/2+1$ in a capacity-$C$ table, a deletion to $C/2$ followed by immediate halving leaves the smaller table full. The next insertion doubles it again. Alternate these operations near the boundary and pay proportional to $C$ almost every time. The cheap preparatory work that growth requires has been undone by shrinking too early.

The remedy is hysteresis: use distinct grow and shrink thresholds. Doubling at full occupancy and halving at one-quarter occupancy leaves the resized array near half occupancy. Reaching either trigger again requires a linear number of intervening operations in the current capacity. A picture of spare space is not enough; derive the number of required inserts or deletions.

## 13. Quarter-full shrinking: complete case analysis

The main policy uses capacity powers of two with minimum capacity two. Append grows before writing if full. Pop removes the last record first, then halves when $C>2$ and the new size is at most $C/4$. Empty pop returns no record and costs a constant check. In legal states reached from the empty minimum-capacity table, a shrink event crosses the threshold from $C/4+1$ to exactly $C/4$.

For completed states choose

For dense states with $n\geq C/2$, define $\Phi(n,C)=2n-C$. For sparse states with $n<C/2$, define $\Phi(n,C)=C/2-n$. At the shared boundary both expressions equal zero, so the definition is continuous there.

It is nonnegative. Initially $\Phi(0,2)=1$, so keep a plus-one endpoint allowance. A normal append in the high branch has charge three; in the low branch it has charge zero, with the crossing into exact half occupancy also costing zero. A growth has charge three. A normal nonempty pop in the high branch has charge minus one, except crossing from half occupancy into the low branch has charge two. A low-branch pop without shrink has charge two.

For a shrink with old capacity $C\geq8$, old size $C/4+1$ has potential $C/4-1$. The new size is $C/4$, new capacity $C/2$ and final potential zero. Cost is $1+C/4$, so charge is two. At $C=4$, the crossing begins at half occupancy and old potential zero; the new state $(1,2)$ also has potential zero, so charge is two again. Empty pops have charge one in the check-only model. Thus every append has charge at most three and every pop at most two, and total work is at most $3P+2Q+1$ for $P$ appends and $Q$ pops.

```python
def pop_last(a, size, capacity):
    if size == 0:
        return a, size, capacity, None
    value = a[size - 1]
    size -= 1
    if capacity > 2 and size <= capacity // 4:
        capacity //= 2
        a = copy_live_records(a, size, capacity)
    return a, size, capacity, value
```

If a course checks occupancy before deletion, compute that transition separately. At old size $C/4$, it copies $C/4$ records first and then removes one. Its endpoint has size $C/4-1$ and capacity $C/2$, giving potential one rather than zero. The asymptotic theorem survives, but an exact charge copied from the post-delete proof does not.

<!-- SIM: shrinking -->

## 14. General hysteresis and space bounds

Suppose growth multiplies capacity by $r>1$ at full occupancy and shrink divides capacity by $r$ when occupancy reaches $\beta$. Immediately after growth, occupancy is approximately $1/r$; immediately after shrink, it is approximately $r\beta$. A fixed strict condition $0<\beta<1/r$ separates both new states from the opposite trigger. The distances $1/r-\beta$ and $1-r\beta$ must be bounded away from zero independently of input size for uniform constants.

In the doubling/quarter policy, a nonempty completed table has capacity at most $\max(2,4n)$ and at least $n$. Empty storage is bounded by the minimum capacity. During rebuilding, old and new buffers coexist; peak storage is larger than the capacity of either one alone. A spatial theorem must distinguish steady-state and transient storage.

## 15. Two-stack queues: order and exact charge

Maintain an input stack and output stack. Enqueue pushes onto input. Dequeue pops output if it is nonempty; otherwise it transfers every input record by one input pop and one output push, then pops output. The logical FIFO order is output from top to bottom followed by input from bottom to top. This order invariant remains true after a complete transfer.

Count each primitive push or pop as one. Set $\Phi=2|\mathrm{input}|$. Enqueue costs one and adds two potential units, so charge is three. Dequeue without transfer costs one and does not change potential, so charge is one. Transferring $k$ records and then removing one costs $2k+1$, drops potential by $2k$, and also has charge one. Empty checks can be added explicitly. Starting from empty, total primitive work is at most three times enqueues plus nonempty dequeues.

A front/peek operation can trigger a transfer but omit the final output pop; its transfer charge is zero under the primitive-only model. Repeated peeks do not repeatedly transfer. If an implementation transfers when output is already nonempty, newer items can be put ahead of older ones and break FIFO correctness.

<!-- SIM: queue -->

## 16. Monotonic stacks and nested loops

For each incoming value, remove stack-top values that are smaller than it, then push its index. Although an inner loop can run many times for one input, every index is pushed once and popped at most once. Total stack modifications are at most $2N$. Each successful comparison causes a pop; at most one final failed comparison occurs per incoming element. Hence comparisons are at most $2N-1$ for a nonempty input when only comparisons between actual values are counted.

Equality is part of the specification. Pop while top is strictly smaller when equal values must remain; pop while top is smaller or equal when a later equal value supersedes an earlier candidate. Nearest greater, nearest greater-or-equal and sliding-window maximum are different queries. For window algorithms, expired indices are removed separately and still at most once. State the invariant during processing and the final answer direction before drawing the stack.

<!-- SIM: monotonic -->

## 17. Binary carries, sorted blocks and binomial links

Represent a growing collection by at most one sorted block of each size $2^j$. Insert a singleton and merge equal-sized blocks exactly as a binary increment carries. A merge producing a block of size $2^j$ costs proportional to $2^j$. During $N$ insertions, that level is built $\lfloor N/2^j\rfloor$ times, so each level contributes at most $N$ work and all levels together give $O(N\log N)$ total. The amortized insertion is logarithmic, despite a linear worst-case carry.

To search, binary-search every occupied block. At size $N$, search cost is $O(\sum_{j:b_j=1}(j+1))$, which can be quadratic in $\log N$ when every low bit is set. This is not the same cost as linking binomial trees: an equal-rank tree link is constant work, so root-count potential can give constant amortized insertion for a maintained forest. Treating a sorted-array merge as a constant link silently changes the algorithm.

<!-- SIM: blocks -->

## 18. Advanced extensions and honest boundaries

For sorted insertion into a B-tree, a pointer to the rightmost leaf avoids repeated root-to-leaf searches. Expensive splits occur after enough keys accumulated at that level. Summing split counts across levels gives linear construction work for fixed branching rules and constant-size primitive metadata. If the branching factor is an input parameter, charge key moves and pointer updates explicitly; a right-spine key potential needs root-boundary terms. The source shorthand about nodes and keys is not used as a complete proof here.

Move-to-front illustrates a different use of potential: comparing one algorithm with a competing algorithm. Count inversions between their list orders. Accessing an item at position $p$ removes inversions involving items after it in the competitor and creates inversions involving preceding items. Under the specified list-update model, this yields a competitive bound proportional to the competitor's total cost. It does not make every list access constant time; repeatedly accessing the current last item can remain linear per access. Competitiveness is a relative guarantee, amortized complexity is an absolute sequence bound.

Sparse-set initialization stores active indices in a dense list and checks a reverse pointer before trusting a cell. A reset can clear the logical active length without clearing every possible cell. In a word-RAM model with arbitrary readable words, initialization work can be independent of the universe size; in a language that prohibits reading uninitialized memory, use initialized metadata, epochs or a different memory contract. Epoch counters require a wrap policy. This technique is a representation argument, not permission to invoke undefined behavior.

## 19. Expected amortization, persistence and deamortization

If rebuilding a hash table scans every old record, geometric resizing bounds the number of rebuild record visits deterministically. If each reinsertion has expected constant collision cost under a stated hash family and load bound, expected total rebuild work is linear. A deterministic geometric-series proof alone does not prove deterministic constant dictionary operations. Adaptive adversaries and reused randomness may invalidate a probabilistic assumption; state the model.

In a persistent structure, two branches can both request the same deferred cleanup from a shared old state. A potential that pays for one cleanup cannot be spent on both branches without recharging or memoizing shared work. A linear history proof does not automatically prove a tree of histories.

Deamortization spreads cleanup over subsequent operations. To grow capacity $C$ to $2C$, begin copying at the overflow event and copy at least one old record per following append, with a schedule that finishes before the new buffer fills. Reads must route to the old or new location according to a migration boundary, and writes must update the authoritative location. Constant allocation of the new buffer is a separate assumption. Concurrent mutations, deletions, iterator validity and copy failures are additional requirements; merely limiting copy count does not prove an entire production API has constant worst-case latency.

<!-- SIM: migration -->

## 20. A procedure for formula and conceptual examination questions

First identify the sequence length, the current number of records and the initial state separately. Second identify the exact charged primitive and the permitted operations. Third compute the expensive transition, including whether resize occurs before or after the update. Fourth choose aggregate, accounting or potential reasoning that captures a resource consumed only once. Fifth retain the initial and final potential terms. Finally test the smallest capacity, an exact power-of-two endpoint, an empty operation and an adversarial alternating sequence.

For multiple-choice questions, eliminate statements whose quantifiers differ: amortized is not expected, per-operation worst case is not sequence worst case, a bound for appends is not a bound for shifts, and a result from empty is not a result from an arbitrarily full initial buffer. The problem bank develops these distinctions through complete algebra, numerical traces and counterexamples.

## 21. Complete-sentence chapter summary

Amortized analysis bounds every permitted operation sequence by tracking preparation and cleanup across time. Aggregate analysis sums work directly; accounting keeps a prefix-solvent balance; potential analysis expresses the same resource through a state function and an exact telescoping identity. Initial workload and the endpoint potential determine whether a charge sum alone bounds real work.

Increment-only counters, bounded multipop stacks and correctly implemented two-stack queues admit constant amortized operation costs in their declared primitive models. Geometric array growth copies a geometric series, while additive growth copies an arithmetic series. Growth and shrinking require distinct thresholds to avoid repeated rebuilds. Weighted moves, allocation, arbitrary-position shifts, enlarged operation sets and persistent branching can change the guarantee. Deamortization adds scheduling and representation obligations that amortization alone does not satisfy.

## 22. Worked mathematical and conceptual problems

<!-- QUESTIONS -->

## 23. Final reasoning rules and examination traps

<!-- RULES -->

## 24. Editable exact-cost laboratory

<!-- LAB -->

## 25. References

The complete reading and correction ledger is available in the source audit. This chapter's worked problems are original or independently reconstructed exercise families with new numerical data; they are not presented as copied university examination questions. Authentic Iranian examination bridges, when included, are separately labeled and linked to the original booklet.

- MIT. Dana Moshkovitz and Bruce Tidor. 6.046J Design and Analysis of Algorithms, Spring 2012, Lecture 11. https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/83b82d45beb3776da72b7f3e1b3f42df_MIT6_046JS12_lec11.pdf
- Carnegie Mellon University. Daniel Anderson and David Woodruff. 15-451/651 Algorithm Design and Analysis, Spring 2024, Lecture 6. https://www.cs.cmu.edu/~15451-s24/lectures/lecture06-amortized.pdf
- Princeton University. Kevin Wayne. COS423, Spring 2013, Amortized Analysis. https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/AmortizedAnalysis.pdf
- Stanford University. Keith Schwarz. CS166 Advanced Data Structures, Spring 2026, Lecture 9. https://web.stanford.edu/class/archive/cs/cs166/cs166.1266/lectures/09/Condensed%20Slides.pdf
- ETH Zurich. Felix Friedrich. Data Structures and Algorithms, Spring 2022, Lecture 8, English handout. https://lec.inf.ethz.ch/DA/2022/slides/daLecture8.en.handout.pdf
