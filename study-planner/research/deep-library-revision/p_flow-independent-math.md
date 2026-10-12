# Independent mathematical and execution audit: p_flow

Date: 12 October 2026. All45 current bank placements were individually read in ranges1–16,17–32,33–45. The complete retained instructional text in `p_flow.en.md`, all36 retained tutorial problems in `p_flow-problems.en.md`, and the complete60-rule summary in `p_flow-review.en.md` were read. SVG markup was omitted from these textual reads; no browser-layout or visual-rendering inspection is claimed. Only this independent report was written. No chapter, canonical metadata, gate or publication state was edited by this subtask. No unsafe C expression was executed.

## 1. Fresh authentic-page inspection

Original cached PDFs were freshly hashed, rendered, and the actual page images viewed. Detail images were additionally viewed for the recursive copying options and SplitSort's base condition.

| Item | PDF page | Source SHA-256 |
|---|---:|---|
| Phd_CS_1405_Q20 | 8 | `a1d82a81df56f660353ff05077755d4af44095ffeeb398c4d2afbee31162fcfa` |
| Phd_CE_1405_Q9 | 3 | `34d7e4f8f1d347be2ede1be4ff027efc2e17680c3aedf633a13857f27955b75a` |
| MS_CS_1393_Q167 | 34 | `7ed89fae8eb601a964355fde5e5d297cbb30844e5240b9e3908b798fb86e349d` |

The recomputed hashes match the canonical declarations. Rendered pages/details are in `C:/Users/bheydari/AppData/Local/Temp/deep-flow-audit-sources/`. The SplitSort source explicitly uses length(A)≤1, distinct input elements, greater block before the median and smaller block afterward. The ordered-triple code and its four numeric options match their transcriptions.

### Source correction required for authentic bank Q3

**MSc CS1393 Q167 option4 uses `store(n-2,i+2)`, not canonical `store(n-1,i+2)`.** The printed fourth option is:

```text
if(n<0)return;
b[i+1]=a[n];
store(n-2,i+2);
```

All four options actually decrease their source index by2. Their distinctions form a two-by-two destination model:

| Option | Destination at copy t | Source at copy t |
|---|---|---|
| 1 | t | N−1−2t |
| 2 | t+1 | N−1−2t |
| 3 | 2t | N−1−2t |
| 4 | 2t+1 | N−1−2t |

Option1 remains the general correct algorithm. Option4's defect is destination offset and destination stride, **not** source stride1. Correct the canonical option and all authentic placements, including d_invariants, as source-only reconciliation. The earlier claim that this fourth source stride had already been visually corrected is not sufficient evidence against the freshly observed original page.

The source uses integer pseudocode with global arrays, not a complete modern C17 declaration. A real implementation needs destination capacity and an index model that can safely represent the negative guard boundary, or a prechecked length-based design.

## 2. Other concrete corrections and qualifications

1. **Historical archive-exclusion wording is stale.** The retained lesson says no Iranian exam paper is used and cites a final-month reservation. The current bank contains three authentic items, so the new revision must replace that sentence with an accurate current description. Historical student approval belongs to the earlier edition; do not reuse its approved status as approval of this revision.
2. **Q44's tests are disjoint at the actual break index8.** Reversing its two pure tests does not change final(s,i)=(19,8). It changes which guard expressions are evaluated on some paths, not the final numerical pair. Distinguish those claims rather than imply a different final output. A break-at9 extension produces an actual priority difference: continue-first returns(37,11), break-first returns(27,9).
3. **Original exact keys are otherwise consistent.** No numeric wrong key was found in the45 placements. The current weaknesses are short general answers with repeated abstract option-analysis prose; replace those passages with the equations, invariants, source-specific traces and concrete failed models listed below.
4. **Code and proof arithmetic need separate domains.** Closed-form products in a mathematical invariant do not mean the program computes those products. A direct C formula can overflow before division even when an incremental loop's final result is representable.
5. **An abstract modular orbit is not a portable runtime timing promise.** The current instructional discussion correctly identifies the nonobservable-loop optimization boundary. Preserve it when adding cyclic-model questions or animations, and identify their mathematical state model explicitly.

## 3. Complete exact-answer ledger

| Q | Option | Independently derived result |
|---|---:|---|
| 1 | 2 | Cod=10+choose(17,3)=690 |
| 2 | 4 | Descending output |
| 3 | 1 | Correct copy destination t and source N−1−2t; fix option4 transcription |
| 4 | 1 | x=0 |
| 5 | 1 | s=9 |
| 6 | 3 | x=6 |
| 7 | 3 | Target1 unreachable; even orbit of period128 |
| 8 | 2 | Six copies; last source index0 |
| 9 | 2 | (x,c)=(4,3) |
| 10 | 1 | Nonnegative integer n strictly decreases |
| 11 | 2 | Six counter increments |
| 12 | 3 | Sum10 |
| 13 | 2 | Sum28 |
| 14 | 1 | n(n−1)/2 |
| 15 | 4 | Moving increment changes the accumulated sequence |
| 16 | 3 | j=5 |
| 17 | 2 | j=8 |
| 18 | 1 | j=n |
| 19 | 4 | Bitwise replacement can change side-effect/value behavior |
| 20 | 2 | Counter10 |
| 21 | 1 | Counter16 |
| 22 | 4 | Counter2n |
| 23 | 3 | Moving update below a while-continue can remove progress |
| 24 | 1 | Five additions |
| 25 | 4 | Eight additions |
| 26 | 3 | n additions |
| 27 | 2 | Threshold checkpoint determines which operations occurred |
| 28 | 2 | Total63 calls |
| 29 | 1 | Total511 calls |
| 30 | 4 | 2^(n+1)−1 calls |
| 31 | 3 | Exponential total calls with linear active depth |
| 32 | 3 | Fifteen local body operations |
| 33 | 2 | Thirty-six local body operations |
| 34 | 1 | n(n+1)/2 body operations |
| 35 | 4 | Tail position does not erase local work |
| 36 | 4 | Final a=2, b=5 |
| 37 | 3 | Final a=2, b=8 |
| 38 | 2 | Final a=2, b=n |
| 39 | 1 | Intermediate representability is required |
| 40 | 2 | Six body executions |
| 41 | 1 | Nine body executions |
| 42 | 4 | n+1 body executions |
| 43 | 3 | The unsigned nonnegative guard is always true |
| 44 | 1 | (s,i)=(19,8) |
| 45 | 3 | First64 target hit at t=96 |

## 4. Authentic and integrated proofs

### Q1: count the actual nested index domain

Each Cod increment corresponds to a unique weakly increasing triple1≤i≤j≤k≤15. Map it to the strictly increasing triple(i,j+1,k+2) in1 through17; the inverse subtracts0,1,2. This is a bijection and yields choose(17,3)=680, not a memorized analogy. Initial Cod10 gives690.

A second proof fixes i. There are15−i+1 possible values for j through k; their weakly ordered pairs number choose(17−i,2). Summing these for i=1 through15 gives choose(17,3). The strict-order count choose(15,3)=455 would discard equal indices; the independent15³ count includes forbidden orderings. Do not assign either mechanism to a listed numeric distractor unless its number actually matches.

This code also distinguishes operation counts: outer body entries15; middle body entries choose(16,2)=120; inner body entries680. Outer guards16, middle guards135, inner guards800. Their total is951, whereas for updates total15+120+680=815. All three loop variables finish at16. These facts require ordinary entry and no abrupt transfer. For a general positive upper bound n, Cod is10+choose(n+2,3), and each variable's final update must safely reach n+1. At n=0 the increment count is0, but unentered middle/inner variables cannot be assigned invented final values.

### Q2: descending recursion semantics

For the conventional median-as-input-order-statistic interpretation on distinct totally ordered values, partition the input into a disjoint greater block R, singleton median and smaller block L. Both recursive inputs are smaller. The length0/1 bases are descending and preserve their inputs. Strong induction gives descending recursive outputs, preserving both blocks; every first-block element exceeds m and every last-block element is below m, so concatenation is descending and preserves the input multiset.

For example input[5,1,4,2,3] with median3 gives descending greater block[5,4], then3, then descending smaller block[2,1]. The result is[5,4,3,2,1]. Reversing the top-level concatenation alone is not enough to prove ascending output unless the recursive calls also follow the revised order. Median affects balance, whereas the output order follows the concatenation and induction.

In an implementation, specify an actual lower/upper order statistic for even lengths if multiset preservation is part of the claim. An arithmetic average median need not belong to the array. The authentic order answer remains descending; a stronger sorting-permutation claim additionally needs the pivot-membership convention. Duplicate inputs are outside the stated source domain because strict R/L partitioning with one median would otherwise lose copies equal to the pivot.

### Q3 and Q8: copy invariant, endpoint and call count

At recursive entry after t completed copies, n=N−1−2t and i=t; b[0] through b[t−1] contain the corresponding original selected elements. The correct write extends this prefix, and the recursive edge reestablishes the equations at t+1. A nonnegative source is copied; the first negative source is tested before any read. Thus copied count is ceil(N/2), base-inclusive call count ceil(N/2)+1, and destination capacity must be at least ceil(N/2). Ordinary unoptimized recursion has that same maximum active depth.

N=5 copies source4,2,0 into destination0,1,2 and then calls(-2,3). N=4 copies3,1 and then calls(-1,2). N=0's mathematical call(-1,0) immediately returns. If N is an unsigned C length, do not first evaluate N−1 at zero and expect a negative guard; check emptiness or use a carefully range-checked signed index. Disjoint arrays, or an explicit proof that overlap cannot overwrite a future source element, are needed by a concrete C copy implementation.

In Q8 the initial **index**10 corresponds to an eleven-element source segment. Indices10,8,6,4,2,0 give six copies and a seventh base call at(-2,6). Option5-and2 omits the final endpoint; six-and1 confuses even and odd starting index; eleven-and0 ignores the stride. Generally, start m≥0 gives floor(m/2)+1 copies and last source m mod2.

Option3 of the authentic source agrees with option1 when at most one element is copied, but fails for general N≥3 by skipping destination slots. This coincidence explains why a one-element trial is not a proof of an algorithm's full-domain correctness.

### Q4–6: ownership and switch entry

Q4 parses as an outer if whose substatement is the entire inner if/else. With a=0, that substatement is skipped and initialized x0 remains0. There is no undefined read. Attaching else to the outer if would define a different statement tree.

Q5's six entries have i=1..6; odd1,3,5 add9. Even entries still reach the for-update. Sum12 is the even-index sum,21 ignores the filter, and nontermination assumes a skipped header update that C does not skip.

Q6 dispatches once to case2, executes x+=2, falls through x+=4, then break exits switch. The trace is0→2→6. Case1 and default do not execute on this path. For the retained middle-default example, dispatch/fallthrough gives tags1,2,3,4 results100,90,70,40; for retained tutorial8's different switch it gives13,8,12,16. Keep each switch's own arithmetic instead of recycling one generic table.

### Q7 and Q45: solve the orbit, then the target congruence

The state after t updates is6t mod256. Period is the least positive t with256 dividing6t, hence128 because gcd(6,256)=2. The orbit contains exactly the even residues. One is unreachable, so Q7 cannot terminate through equality to1 in the specified modular state model. Having a finite state space proves eventual repetition, not eventual target reachability.

For Q45 solve6t≡64(mod256). Divide by2:3t≡32(mod128). Since3*43=129≡1, t≡43*32=1376≡96(mod128). The least positive solution is96. Checks at the distractor counts give t32→192, t64→128, t128→0. Reachability and first positive hitting time are different obligations. A count0 target hit at the initial state also differs from the first positive return at the period.

### Q9: the failed guard still increments

| Old x compared | x after postfix side effect | Guard | c after possible body |
|---:|---:|---|---:|
| 0 | 1 | true | 1 |
| 1 | 2 | true | 2 |
| 2 | 3 | true | 3 |
| 3 | 4 | false | 3 |

This establishes(4,3). The guard is evaluated four times and the body three. In a general signed `while(x++<n)` starting at0, the final increment needs n+1 representable; n=INT_MAX produces overflow even though the final comparison's old value would fail. This is distinct from a short-circuit test that never evaluates the final increment.

### Q10: a branch-valid ranking and a harder exact count

For odd positive n, subtracting1 gives a strictly smaller nonnegative integer. For even positive n, halving gives a strictly smaller positive integer. Therefore n is a ranking. Parity and n mod3 can repeat or rise; population count stays unchanged under halving an even value, so it is not alone a strict ranking at every step.

A precise extension counts transitions as floor(log2 n)+popcount(n) for n>0. Halving removes a trailing zero and decreases bit length by1; there are exactly initial-bit-length−1 such removals before reaching1. Each odd subtraction clears its trailing1 without borrow, reducing population count by1; halving leaves that count unchanged, and all initial one bits must eventually be cleared. Thus the number of odd subtractions is the initial population count. Both n5(101) and n8(1000) take four transitions, with different branch compositions. A lexicographic pair(bit length,popcount) is another valid decreasing measure.

### Q11 and Q44: target each transfer precisely

Q11 increments at j1 and2, then breaks at3 before the counter write. Three outer entries give3*2=6. The outer body remains active after every inner break.

Q44's exact trace:

| i | Path | s afterward | Next control |
|---:|---|---:|---|
| 1 | add1 | 1 | update→2 |
| 2 | add2 | 3 | update→3 |
| 3 | continue | 3 | update→4 |
| 4 | add4 | 7 | update→5 |
| 5 | add5 | 12 | update→6 |
| 6 | continue | 12 | update→7 |
| 7 | add7 | 19 | update→8 |
| 8 | break before addition | 19 | exit, no update |

There are eight body entries, eight true outer guards and seven header updates; no final false guard. The break and continue predicates cannot both hold at i8, so swapping those pure tests leaves the final(19,8) unchanged. With break9, continue-first skips the break and finishes(37,11), while break-first ends(27,9). This extension demonstrates actual priority overlap.

## 5. Complete family constructions for Q12–43

### Q12–15: sum before increment

At the guard, invariant0≤i≤n and s=sum of0 through i−1=i(i−1)/2. Initialization i=s=0 satisfies the empty sum. Adding i then incrementing preserves the invariant. Ranking n−i decreases; false guard and upper bound give i=n. Final sum n(n−1)/2 gives10 and28. Increment-before-add instead sums1..n and differs by n. The n² distractor assigns constant n work to each entry; n confuses entry count with accumulated value.

For an int32 implementation of the incremental loop, n=65536 still has representable final sum2147450880; larger n does not. Directly computing n*(n−1) in int can overflow at a smaller n even though division by2 would make the mathematical formula fit. The proof identity does not require that unsafe intermediate product in the actual incremental code.

### Q16–19: stateful short circuit

At each guard, i=j=t for0≤t≤n. When t<n, the left operand is true, ++j gives t+1>0, and ++i restores i=j=t+1. At t=n the left operand is false and ++j is skipped. Thus final pair(n,n), including(0,0). The requested final j is5 or8.

Reversing logical operands makes the final increment execute, giving(n,n+1) when representable. It overflows j at an int32 n=INT_MAX; the original need not. Bitwise replacement has a more dramatic exact trace: first1&1 succeeds, second1&2 is zero for n≥2 (or0&2 for n1), so every positive start n in this example ends(i,j)=(1,2). At n0 it ends(0,1). These operands use different objects, so this particular bitwise example does not introduce same-object unsequenced UB; it changes evaluation and integer-bit semantics. A proof should not merely say both operands run.

### Q20–23: filtered entries and continue

For i1 through3n, there are n disjoint blocks(3r+1,3r+2,3r+3), r0..n−1. Exactly two entries per block reach ++s. Final s=2n, giving10 and16. However the loop body is entered3n times, its update executes3n times and its guard executes3n+1 times. The distractor3n counts entries, n counts skipped multiples, and2n−1 removes an accepted endpoint without justification.

A minimum-safe finite signed contract must include3n, final update to3n+1, and accumulator2n. In a general signed type with maximum M, require3n+1≤M, not just3n≤M. Under int32 this gives positive n≤715827882. Moving the update below continue in a while body stops progress at the first multiple3 and repeats the same index; no arithmetic-count formula can replace that control-edge analysis.

### Q24–27: first triangular threshold

After k completed additions, s=k(k+1)/2. Each next added value k+1 is positive, so these checkpoints increase strictly. At k=n the sum is exactly n(n+1)/2; all earlier values are smaller. Therefore n additions,5 or8, first qualify. A before/after test must identify which addition and update has already run; break skips all subsequent body/header work.

For an arbitrary budget B≥0, the first k reaching or exceeding B is the least nonnegative k with k(k+1)/2≥B, but a mandatory first body addition changes the B=0 boundary. An implementation should avoid blindly computing a floating inverse-triangular formula near rounding boundaries: prove the integer inequality around the chosen candidate. Similarly, n*(n+1)/2 as a C expression can overflow its product before division; its mathematical threshold is not a language safety proof.

### Q28–31: total calls versus active path

C(0)=1, because the base invocation still occurs. For n>0, C(n)=1+2C(n−1). Induction gives C(n)=2^(n+1)−1, yielding63 and511. By level count, depth d has2^d calls, including2^n zero-parameter leaves. Internal non-base calls number2^n−1. Ordinary sequential depth-first evaluation holds at most n+1 active frames, including the base, while all earlier calls remain part of total work. The distractor2^n counts only leaves,2^(n+1) omits the finite-series minus1, and n+1 measures maximum path length rather than total calls. Tail-call or memoization transformations require their own specified semantics; none is implicit in this question.

### Q32–35: one child but growing local toll

W(0)=0 and W(n)=n+W(n−1). Expanding gives n+(n−1)+...+1=n(n+1)/2, hence15 and36. Calls number n+1 including the base, but the local toll is not constant. The n distractor ignores growing loops; n² treats every call's toll as n;2^n invents binary branching. If an implementation eliminates tail-call stack growth, the local operations still occurred. A recurrence must state what its counted event is before comparing its asymptotic or exact result.

### Q36–39: sequential arithmetic swap

The state after each full expression is(n,2)→(n+2,2)→(n+2,n)→(2,n). Each assignment reads the updated previous state. The correct requested a is2; n leaves the original a unchanged, n+2 stops after one statement, and n−2 applies subtraction to old values. Positive int32 n≤INT_MAX−2 ensures all these intermediate values fit. A temporary-variable swap needs no intermediate sum beyond the two original values. Aliased references would be another specification; the present a and b are distinct scalar objects. Unsigned modular arithmetic can prove a different same-width arithmetic swap using residues, but it must not be used to justify signed overflow.

### Q40–43: posttest descent

At body execution t=1..n+1, i=n−t. The guard is true through i0 and false at i−1. Therefore n+1 body entries and n+1 guard tests, giving6 and9. There is no preliminary guard. At mathematical n0 the body still executes once and exits at−1. Negative starting values also need a separate one-entry analysis, rather than the positive-domain n+1 formula. An unsigned source cannot make i>=0 false; a narrow source may promote for that comparison, but its promoted value is still nonnegative. Unsigned decrementation has a cycle; signed decrementation beyond its minimum would instead be undefined. Preserve the distinct machine and control models.

## 6. Retained instructional proof review

The retained explanation is substantially more concrete than the old bank templates and should be preserved where valid. Its examples and proof obligations were checked as follows:

- All36 tutorial outputs agree with independent tracing; the switch/continue tutorial10 yields46, inner-break tutorial18 yields33, Euclid84/30 yields6 and its mistaken sequential replacement yields30.
- The summation construction's checkpoint invariant and ranking are valid, and its incremental updates are bounded by the assumed final sum. It correctly notes that the proof product need not be computed in C.
- Odd-sum tutorial23 at n≤100 finishes n² and keeps all shown arithmetic within every conforming int; odd's final value2n+1 is included in the safety check.
- Budget tutorial25's speculative sum is bounded by5050; its separate normal/break postconditions are valid. Its maximal feasible prefix length is min(n,floor((sqrt(8b+1)−1)/2)) as an exact mathematical statement, requiring integer validation if implemented numerically.
- Decimal digit tutorial27's partial digit sum is bounded by original unsigned input N, so its additions do not wrap. The zero digit-count versus zero digit-sum distinction is correct.
- The capstone odd-prefix invariant handles both continue and break correctly. It is a prefix optimum, not an arbitrary subset optimum. A useful exact strengthening is accepted count m=min(floor(n/2),floor(sqrt(budget))), sum=m², with normal exit i=n if every candidate fits, otherwise break index2m+1. For n12,budget18 this gives m4,sum16,i9.
- Integer progression ceiling/floor counts, normal/break guard-update counts, comma-guard behavior and Python range distinctions are correct under their stated entry and arithmetic premises.
- The modular-cycle and floating-stagnation proofs separate their state models from a universal runtime claim. The retained optimizer warning is necessary and correct.

The [public N1570 C11 committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf) was freshly consulted for continue/break targets and loop assumptions, especially6.8.6.2,6.8.6.3 and6.8.5 p6. It is not labeled the published C17 standard. No fresh university-course reading is claimed by this mathematical subtask; the listed course reading evidence remains the source-review task's responsibility.

## 7. Finite corroboration actually executed

Read-only mathematical Python models independently checked:

- Triple counts for n0..20 against choose(n+2,3); the actual n15 count680.
- SplitSort with an actual upper-median input element on all874 distinct permutations of lengths0..6 against descending sorted output.
- Copy traces at lengths0,1,4,5,11, including the base call and exact index lists.
- Logical versus bitwise stateful-guard traces at n0,1,5,8.
- Every arithmetic count family at n5 and8; the complete postfix-guard trace ending(4,3).
- The128-state unsigned orbit against all even residues, first64 hit96, and the retained four-bit cycle0,6,12,2,8,14,4,10.
- The exact odd-subtract/even-halve step identity for every start1..10000.
- Q44's original break8 under either test order, and the break9 overlapping-priority extension.

These models use mathematical integers with explicit control steps, not host C output experiments or Python floor division substituted for C signed division. They corroborate specified cases and formulas; proofs above establish the broader declared-domain conclusions.

## 8. Appropriate dedicated diagrams and state models

1. **Ordered triples:** a layered lattice of i,j,k with inequalities visible; show the bijection to distinct shifted coordinates and separate counts for Cod writes, tests and updates.
2. **SplitSort:** an actual recursion tree with greater/median/smaller partitions, sorted child outputs and ordered concatenation. Preserve element identities and distinguish tree call count from stack depth.
3. **Reverse-stride copy:** two arrays with source positions N−1−2t and dense destinations t; animate the actual read/write, then the negative guard base without an invalid read. Show all four destination-offset/stride alternatives using the corrected original option4.
4. **Dangling else:** a statement-ownership tree plus a guard path; indentation alone is not the model.
5. **Filtered for and continue:** a program-counter graph whose continue edge reaches update; distinguish body-entry count from accumulator writes and display the corresponding while-rewrite cycle separately.
6. **Switch:** one dispatch arrow to the selected label, followed by actual sequential fallthrough and the precise break target. A switch inside a loop must have visibly different continue and break destinations.
7. **Modular orbit:**128 reachable even residues or a readable small-modulus representative, plus the exact congruence proof. Unreachable odd targets and first-hit even targets are different checkpoints.
8. **Postfix guard:** a four-row state trace including the failed test; show old compared value, updated x and possible c increment separately.
9. **Ranking:** branch-specific integer transitions with decreasing n and unchanged/decreased population count, plus an exact step-count ledger. Do not show population count as if it strictly decreases under every half step.
10. **Nested break:** nesting frames and the actual innermost exit arrow; the outer loop remains active.
11. **Accumulator checkpoint:** prefix0..i−1 with s=i(i−1)/2, followed by add then increment. The increment-first comparison must display its different invariant.
12. **Stateful guard:** a static parse tree plus runtime short-circuit gates; the final false left guard visibly skips ++j. Separate reversed-logical and bitwise traces.
13. **Threshold:** sum checkpoints with the first qualifying index and break before any later update. If generalized, show the candidate integer inequality rather than trusting rounded inverse roots.
14. **Recursion tree/stack:** a complete small binary tree beside the active single root-to-leaf stack; each base invocation counts even though it returns immediately.
15. **Growing local recursion toll:** one-child call chain with k local operations at each node; sum the toll independently of the active-depth count.
16. **Arithmetic swap:** three full-expression state tables, including the intermediate n+2 range check. Do not animate simultaneous assignments or an undefined signed overflow.
17. **Posttest descent:** first body before any guard, then states n−1..−1 with the final failed test. A separate unsigned lane cycles rather than supplying a fake negative terminal value.
18. **Continue/break overlap:** original break8 paths plus break9 extension; count evaluated guards separately from final(s,i) so a pure-test reorder is not portrayed as a changed numeric answer when it is not.

## 9. Handoff

The45 keys are mathematically consistent. The authentic Q167 option4 and its analysis require source correction; stale archive/status text requires revision; Q44 test-order commentary needs the final-value/guard-trace distinction. Every source and proof claim above is bounded to the materials actually inspected. No student quiz, chapter promotion, publication, visual-layout pass or universal correctness guarantee was performed by this independent audit.
