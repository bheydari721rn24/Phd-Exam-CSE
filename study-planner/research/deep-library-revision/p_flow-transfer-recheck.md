# Control Flow: independent transfer-construction recheck

Date: 2026-10-12. Reviewed the full `p_flow-method-instruction.md`, all eight extensions A–H, and all twenty added rules 16–35 in `p_flow-exam-rules.md`. This report owns no chapter, gate, metadata or publication edits.

## Concrete corrections requested

### 1. Rule 20 must state the positive domain of its logarithm

The exact step formula currently appears as `floor(log2 n) + popcount(n)` without a local restriction on n. At n=0 the terminating process has zero transitions, but log2(0) is undefined. The method section already correctly says n>0; the independently retrievable rule should preserve that premise.

Suggested replacement sentence:

> For a positive integer initial n, the exact transition count is floor(log2 n) + popcount(n); initial n=0 takes zero transitions without evaluating a logarithm.

The existing ranking claim is correct on enabled positive transitions. Also change the grammatical phrase “A increasing accumulator” to “An increasing accumulator” when incorporating the replacement.

### 2. Rule 33 must state the nonnegative signed initial domain

The statement that a signed do-decrement loop ends at −1 after n+1 entries is correct for a representable initial signed n≥0, with this specific body and trailing `i>=0` test. It is not a universal consequence of signedness. Starting at −2 performs one decrement and exits at −3; starting at INT_MIN has undefined signed arithmetic on the first decrement. No invalid C expression was executed to derive these boundaries.

Suggested replacement sentence:

> With a representable initial signed n≥0, `do { --i; } while (i>=0);` makes n+1 body entries and exits at i=−1. Negative initial inputs require separate analysis: a value above INT_MIN decrements once and exits, while INT_MIN makes the first decrement undefined.

The following unsigned-domain explanation is correct. If the chapter keeps only its nonnegative input domain, the first replacement sentence alone is sufficient; the negative counterexamples can remain in audit evidence.

## Verified constructions and extensions

| Construction | Independent mathematical or semantic result |
|---|---|
| Event counts and extension A | At bound 15, the authentic triple loop has 15 outer entries, 120 middle entries, 680 inner writes, 951 total guard evaluations and 815 header updates. All three final indices are 16 under the sufficient-type premise. Empty outer input does not assign unentered inner indices. |
| Checkpoint invariants | Sum-before-increment and increment-before-sum formulas apply at their stated checkpoints. A stateful false guard and a skipped short-circuit operand are correctly distinguished. Continue introduces its own restoration/progress edge. |
| Bit-count identity | For positive n, exactly bit_length(n)−1 halvings remove zero suffix positions, and popcount(n) subtractions clear the one bits; T(n)=floor(log2 n)+popcount(n). Initial 13 has three halvings and three subtractions. |
| Ordered and filtered counts | Weak triples map reversibly to strict triples with shifts (0,1,2). Each three-element filter block gives two counter increments and three entries. Prefix count i−1−floor((i−1)/3) is correct at the guard. |
| First crossing versus budget | Positive triangular prefixes increase strictly. First crossing requires S_k≥H with the preceding failure; maximal feasible prefix requires S_m≤B<S_(m+1). Finite inverse-square-root computations must be checked against these integer inequalities. |
| Modular reachability | gcd(s,M) dividing b−a is the correct reachable-target condition for the declared positive-modulus integer model. Step 6 modulo 256 has period 128; target 64 first appears at 96, and target zero distinguishes initial matching from first positive return. C-language qualification is retained. |
| Recursion and copy | Binary calls 2^(n+1)−1 and sequential active depth n+1 count different objects. Single-chain local toll sums to n(n+1)/2. Dense reverse-stride copying has ceil(N/2) writes plus a base call. The same-array five-element counterexample correctly shows a write can clobber a future original source. |
| Extension B | Signed int32 INT_MAX+2 is unrepresentable at the first arithmetic-swap sum. Later cancellation cannot make that execution defined. A temporary swap avoids this arithmetic restriction. |
| Extension C | Logical guard gives (n,n) for safe nonnegative n. Reversal requires representable n+1. The bitwise replacement gives (1,2) for safe positive n and uses distinct objects, so the cited same-object sequencing violation is absent. |
| Extension D | Pure predicates at break 8 are disjoint and give (19,8) in either order. Moving the target to 9 creates the overlap: continue-first gives (37,11), break-first (27,9). |
| Extension E | Under the retained capstone's 0≤n≤100 and 0≤B≤10000 contract, r=floor(n/2), m=min(r,floor(sqrt B)), sum=m². Normal exit gives i=n; budget break gives i=2m+1. For n=12,B=18 this is sum 16, i=9. This is a prefix result, not subset optimization. |
| Extension F | With c=0.01 and t=0.01, Newton gives t'=0.505, increasing absolute root error from 0.09 to 0.405. For c>0,t>0 and r=sqrt(c), t'−r=(t−r)²/(2t)≥0. Once t≥r, t'−t=(c−t²)/(2t)≤0, proving the bounded nonincreasing sequence only after the first update. The text correctly requires additional finite-rounding and tolerance analysis. |
| Extension G | In signed int32, 2^30 fits but an unconditional following multiply by 2 requires 2^31 and is undefined. Valid emitted values do not establish safe subsequent updates. Java source behavior is not transferred to C17. |
| Extension H | A NaN candidate persists under an ordinary finite-candidate `<` comparison because the comparison is unordered/false. Thus an ordered argmin postcondition needs a non-NaN domain or explicit policy. Infinite values are ordered under the specified IEEE model. |

## Corroboration actually performed

- Instrumented a safe mathematical model of the authentic triple loop: guards 951, updates 815, innermost writes 680.
- Checked the exact bit-count identity for all initial integers 1–10000 using arbitrary-precision integer transitions.
- Checked the odd-prefix count, sum and terminal index for all n=0–100 against eighteen boundary-focused budgets, totaling 1818 cases, including square-adjacent budgets and the upper budget bound.
- Checked the Newton counterexample and the above-root difference identity using exact rational arithmetic, avoiding a floating approximation as proof.

No source-reading completeness or final renderer claim is made by this audit. The recorded course-access statements require the integrating agent's research evidence; browser layout and diagram checkpoint associations remain separate checks. Except for the two local rule-domain omissions above, no concrete mathematical or C-domain error was found in the reviewed constructions and extensions.
