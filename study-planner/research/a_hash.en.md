# Hash Tables: Exact Probes, Collision Mathematics, and Correct Updates

## 1. Sources, objectives and prerequisites

This chapter combines four genuinely read core courses: MIT 6.006 Spring 2020 (Demaine, Ku and Solomon), CMU 15-122 Fall 2026 (Pfenning and Simmons), Princeton COS226 Spring 2025 (Sedgewick and Wayne), and ETH Zurich Data Structures and Algorithms Spring 2020 (Friedrich). Stanford's written CS106B lecture and Cambridge lecture 8 provide additional comparisons. The [source audit](../reviews/a_hash-sources.html) records the candidate evaluation, actual page ranges and corrections. References are repeated at the end. These courses contribute complementary mathematical models and contracts; a published claim is checked rather than adopted automatically.

Prerequisites are array and linked-list operations, modular arithmetic, greatest common divisors, summation, indicator random variables, conditional probability and geometric resizing. Each is restated where used. The objective is to derive exact tables, prove lookup and update correctness, distinguish probability models, and justify a cost using explicit assumptions. Hashing is not a synonym for guaranteed constant time.

## 2. The dictionary contract and the computational model

A map stores at most one value for each equality class of keys. `put(k,v)` inserts an absent key or replaces its existing value. `get(k)` distinguishes an absent key from a stored null-like value, for example by returning a presence flag together with the value. `delete(k)` removes a present key and explicitly reports whether removal occurred. A multimap is a different contract: several values may deliberately share a key. None of these contracts requires sorted iteration, predecessor, rank or minimum priority.

Let $n$ denote live entries, $m>0$ table capacity, and $U$ the key universe. A direct-address table allocates $|U|$ cells and achieves constant-time indexing for word-sized integer keys, but may waste enormous space. A hash table compresses this universe to $m$ home positions. Collisions are unavoidable somewhere when $|U|>m$, yet a particular stored subset can be collision-free. A pigeonhole statement concerns the entire domain; it does not assert that every subset of fewer than $m$ keys must collide.

A comparison-only lookup that distinguishes $n$ present keys and absence needs enough decision-tree leaves for those outputs. With binary tests and height $h$, there are at most $2^h$ leaves, giving $h\ge\lceil\log_2(n+1)\rceil$ for that model. Hashing adds arithmetic and indexed access on key representations; it does not violate a bound whose operation model it no longer obeys. Three-way comparisons alter constants, not the logarithmic order.

Cost statements assume word-sized arithmetic and constant-time equality unless stated otherwise. Computing a polynomial hash of a length-$L$ string costs $\Theta(L)$; comparing colliding strings may also inspect $\Theta(L)$ characters. A constant expected number of bucket or slot accesses is not a constant total character cost. Cached immutable fingerprints can reject many mismatches cheaply, but matching fingerprints still require equality verification.

## 3. Hash arithmetic and equality invariants

Separate key-to-code hashing from code-to-index reduction. Equal keys must have equal codes and equal probe routes. The converse is false: matching codes are only candidates for equality. The same table must use a fixed hash choice until rebuilding; a random family is sampled once, not freshly for each lookup. If equality-relevant fields mutate after insertion, the old entry can remain in a location unreachable from its new home. Either use immutable keys or remove and reinsert using the original representation.

For mathematical integers, the normalized index is

$$h(k)=k-m\lfloor k/m\rfloor\in\{0,\ldots,m-1\}.$$

At $m=7$, $h(-1)=6$ and $h(-15)=6$. Some languages' remainder operator returns a negative result for a negative dividend. Normalize a remainder with `r < 0 ? r + m : r`, assuming valid positive capacity and safe-width arithmetic. Taking the absolute value of the most negative signed integer can overflow. Taking absolute value after remainder stays in range but implements a different mapping from mathematical floor-modulo. Every exact trace must use one declared convention.

Division hashing $k\bmod m$ is a deterministic heuristic. A prime capacity avoids some stride patterns but cannot protect against keys $r,r+m,r+2m,\ldots$. For step-$s$ inputs, the number of reachable residues is $m/\gcd(s,m)$; a small greatest common divisor is useful, not a universal randomness certificate. Multiplication hashing extracts upper bits of a word product after reduction modulo $2^w$; fixed-word overflow must be intentional unsigned arithmetic rather than undefined signed overflow.

For a string with codes $c_0,\ldots,c_{L-1}$ and base $b$, Horner evaluation computes

$$H(s)=\left(\sum_{j=0}^{L-1}c_jb^{L-1-j}\right)\bmod m.$$

The update `v = (b*v + c) mod m` maintains the hash of the prefix already processed. Induction proves equivalence to the expanded polynomial. With $b=5,m=17$ and codes $[1,2,3]$, successive residues are $1,7,4$. Choosing $b\equiv1\pmod m$ reduces the code to a sum and loses order information; choosing $b\equiv0\pmod m$ retains only the last code. Even a good base permits collisions because the range is finite.

<!-- SIM: arithmetic -->

## 4. Separate chaining: representation and exact work

Bucket $j$ holds a chain of all records whose home is $j$. The representation invariant has three parts: every live record is in its correct bucket, every equality class occurs once, and the stored live count equals the number of records. Search scans only the target bucket, comparing keys until a match or the chain end. Correctness follows because no other bucket can contain an equal key and all possible matches in this bucket are inspected.

Head insertion is constant pointer work after absence has been established. A map insertion still searches for a duplicate; inserting a promised-new record and performing general `put` have different costs. Updating an existing value does not increase $n$. Deleting a found node takes constant unlink work with its predecessor, but finding that predecessor/key can require the entire chain. Sorted chains can terminate some misses early but remain linear in chain length. Sorted arrays permit logarithmic location search but require linear worst-case shifting for insertion. A balanced search tree inside a bucket changes its own cost and assumptions.

For $m=7$ and insertion sequence $[12,26,5,15,2,19,43]$ with head insertion, final bucket 5 is $19\to5\to26\to12$, bucket 1 is $43\to15$, and bucket 2 is $2$. The chain order depends on insertion policy. Search for 12 uses four equality tests; search for 33 uses four failed tests in bucket 5. Across all seven equally likely stored keys, exact successful comparisons total $10+3+1=14$, so the average is two. Across seven equally likely home buckets, a miss scans seven records in total and averages one record comparison. Neither result includes hash computation.

<!-- SIM: chaining -->

## 5. Load, occupancy and the difference between averages

The chaining load factor is $\alpha=n/m$ and may exceed one. Arithmetic alone gives the average bucket length $\alpha$. It does not bound the bucket selected by a query. If all records share one bucket, averaging over all buckets can still produce a small constant while every stored-key query scans that crowded bucket.

For fixed bucket lengths $\ell_0,\ldots,\ell_{m-1}$, equally likely successful searches inspect

$$C_{\mathrm{hit}}=\frac{1}{n}\sum_{j=0}^{m-1}\frac{\ell_j(\ell_j+1)}{2}.$$

Each position in a chain is reached by one successful query, so its contribution is $1+2+\cdots+\ell_j$. Equally likely miss home positions inspect $n/m$ entries. These are averages for a fixed table and stated query distributions. They are distinct from an expectation over randomly chosen hash functions.

Under independent uniform home positions, a specified bucket length is binomial, with expectation $n/m$ and variance $n(1/m)(1-1/m)$. Expected occupied buckets are

$$m\left(1-\left(1-\frac{1}{m}\right)^n\right).$$

Use one indicator for each bucket's nonempty event, then sum expectations. Expected empty buckets are $m(1-1/m)^n$. At $n=m$, a typical individual bucket need not be close to its mean with overwhelming probability: it can be empty. Maximum load, one bucket's expectation and all-bucket concentration are different claims.

## 6. Pair collisions and birthday probabilities

Define a collision pair as an unordered pair of distinct keys with equal homes. Under independent uniform hashing, each pair collides with probability $1/m$, so

$$E[P]=\binom{n}{2}\frac{1}{m}=\frac{n(n-1)}{2m}.$$

Linearity of expectation does not require the collision indicators themselves to be mutually independent. They are generally dependent. The exact pair count in a fixed table is $\sum_j\binom{\ell_j}{2}$. The number of overflow entries is $n-B$ where $B$ is the number of occupied buckets. These quantities differ: a bucket of length four contains six pairs but three overflow entries.

For $n\le m$, independent uniform choices give

$$\Pr(\text{no collision})=\prod_{i=0}^{n-1}\left(1-\frac{i}{m}\right)=\frac{m!}{(m-n)!m^n}.$$

The product comes from conditioning: after $i$ distinct positions have been occupied, the next key has $m-i$ safe positions. At $n>m$, collision-free placement is impossible. Since $1-x\le e^{-x}$, the no-collision probability is at most $e^{-n(n-1)/(2m)}$. The familiar exponential estimate is an approximation for suitable small ratios, not an exact identity. The 50% threshold is on the order of $\sqrt m$; low load does not imply an unlikely first collision. Conversely, many collisions need not imply poor chained-query performance if each chain remains short.

## 7. Universal hashing and its actual quantifiers

A universal family $\mathcal H$ satisfies, for every fixed pair $x\ne y$,

$$\Pr_{h\in\mathcal H}(h(x)=h(y))\le\frac{1}{m}.$$

Choose $h$ uniformly from the family and keep it fixed for a table lifetime. The key set is fixed independently of this choice in the standard argument. The guarantee does not promise perfect balance for every sampled function, mutual independence of all outputs, or resistance to an adaptive adversary that learns the chosen function.

For an absent fixed query $q$ against set $S$, define $I_x$ for its collision with each $x\in S$. Then $E[\sum_{x\in S}I_x]\le n/m$. For a present query, count its own entry separately to obtain expected bucket size at most $1+(n-1)/m$. Therefore searching the entire bucket gives $O(1+n/m)$ expected time with constant key costs. A precise successful rank expectation under a random insertion order is a stronger statement than this bucket-size upper bound.

Let $p$ be prime and larger than every allowed nonnegative key. Choose $a$ uniformly from $1,\ldots,p-1$ and $b$ from $0,\ldots,p-1$. The family

$$h_{a,b}(x)=((ax+b)\bmod p)\bmod m$$

is universal. Here is a counting proof. For $x\ne y$, the map $(a,b)\mapsto(r,s)$ with $r=ax+b\bmod p$ and $s=ay+b\bmod p$ is a bijection onto ordered distinct residues: solve $a=(r-s)(x-y)^{-1}\bmod p$ and then $b=r-ax\bmod p$. Each distinct output pair is equally likely. A residue class modulo $m$ contains at most $\lceil p/m\rceil$ residues, so for any first residue, at most $\lceil p/m\rceil-1$ possible distinct second residues collide. The conditional fraction is at most $(\lceil p/m\rceil-1)/(p-1)\le1/m$. Summing over first residues proves the bound. Modular inverses exist because $p$ is prime and $x-y$ is nonzero modulo $p$.

Do not restrict $a,b$ to a smaller key range while keeping a larger prime and quote the same theorem. That changes the probability distribution used in the bijection. The problem bank supplies an enumerated counterexample. Practical affine evaluation also needs enough arithmetic width to preserve modular multiplication.

## 8. Open addressing and the lookup invariant

Open addressing stores records directly in the $m$ slots. Every slot has a separate state: `EMPTY`, `LIVE` or `DELETED`. These markers must not be ordinary user keys. For each key, define a deterministic probe route $p(k,0),p(k,1),\ldots$. Search must use the same route as insertion and any subsequent rebuild.

The reachability invariant is: before a live key's current position along its route, no slot is `EMPTY`. A prior slot may be occupied by another record or marked `DELETED`. Thus a search can terminate at `EMPTY` but must continue through `DELETED`. Finding an equal live key is success. Exhausting the allowed route is a miss. All algorithms have explicit finite probe limits, including when there is no empty slot.

Live load $\alpha=n/m$ is at most one; most efficient implementations keep it bounded below one. Let $d$ be deleted markers. Nonempty occupancy $\beta=(n+d)/m$ governs where failed searches can stop. A nearly empty live table with many tombstones can still be slow. A quadratic route may fail to reach some empty slots, so low live load alone is insufficient without a coverage theorem for that exact policy.

## 9. Linear probing: exact insertion and clustering

Linear probing uses $p(k,i)=(h(k)+i)\bmod m$. Its first $m$ positions cover the entire table. Starting at a fixed home and walking forward is a circular route; crossing slot $m-1$ continues at zero. A probe is one examined slot. A collision comparison against a live unequal record is not necessarily the same counter as a probe that examines an empty/deleted slot.

With $m=11$ and keys $[10,21,32,43,9]$, homes are $[10,10,10,10,9]$. Insertion slots are $[10,0,1,2,9]$ and probe counts are $[1,2,3,4,1]$. The circular cluster runs from slot 9 through 2. Search for 54 starts at 10, visits $10,0,1,2,3$ and misses in five probes. Search for 9 succeeds in one probe. Averaging one observation across several keys is a descriptive calculation, not a proof for all future inputs.

A run of $r$ occupied slots followed by an empty slot receives insertions whose home lies at any of these $r+1$ positions. Under uniform home choices, the probability that this next empty slot receives the insertion is $(r+1)/m$. Larger clusters attract more new entries; clusters can merge. This is primary clustering. Uniform home positions do not imply uniform final insertion slots.

For a fixed table with at least one `EMPTY`, let its maximal circular nonempty runs have lengths $r_1,\ldots,r_t$, including tombstones when present. A uniformly distributed unsuccessful-query home costs exactly

$$C_{\mathrm{miss}}=1+\frac{1}{2m}\sum_{j=1}^{t}r_j(r_j+1).$$

Every home starts with one probe. In a run of length $r$, extra probes sum to $r+(r-1)+\cdots+1$. Empty homes add no extra work. This formula handles a run wrapping around the last index by treating it as one circular run. It is an exact fixed-table result and does not need independent random insertion assumptions.

<!-- SIM: linear -->

## 10. Tombstones, duplicate updates and safe insertion

Deleting a key by changing its slot to `EMPTY` can break reachability. In the preceding table, clearing slot zero after deleting 21 makes 32 and 43 unreachable from home 10. Marking zero `DELETED` preserves their routes. Searches skip the marker while new insertions can eventually reuse it.

A map insertion must not stop immediately at the first tombstone. Remember that position, then continue looking for an equal live key until `EMPTY` or the complete route limit. If the key is found, replace its value in place and leave counts unchanged. If absent, use the remembered tombstone if available; otherwise use the first empty slot. When reusing a tombstone, increment $n$ and decrement $d$. On deletion, decrement $n$ and increment $d$. A failed deletion changes neither.

For the running example after deleting 21, putting 32 with a new value must find slot 1 after skipping deleted slot zero. Reusing zero immediately would create a second 32 and violate uniqueness. Inserting a genuinely absent 54 can reuse zero only after the scan establishes absence. The invariant then remains true: its new route contains no earlier empty slot, and displaced survivors retain their previously reachable positions.

```text
put(key, value):
    first_deleted = none
    for attempt in 0 .. route_limit-1:
        j = probe(key, attempt)
        if state[j] == LIVE and equal(key, keys[j]):
            values[j] = value
            return UPDATED
        if state[j] == DELETED and first_deleted is none:
            first_deleted = j
        if state[j] == EMPTY:
            target = first_deleted if present else j
            place_new_record(target, key, value)
            return INSERTED
    if first_deleted is present:
        place_new_record(first_deleted, key, value)
        return INSERTED
    return ROUTE_EXHAUSTED
```

A nonpermuting quadratic route can revisit slots. The declared route limit is finite, and route exhaustion need not mean physical fullness. Rebuilding can clear markers and change the capacity or hashing policy; a rebuild changes every live record's routing context.

<!-- SIM: deletion -->

## 11. Removing tombstones by repairing a linear cluster

Linear probing admits deletion by removing the target and reinserting subsequent cluster entries until an empty slot is reached. Each removed survivor is reinserted under the same home rule, restoring reachability. During a full-table repair, avoid an unbounded loop: retain explicit limits or create a hole that terminates the traversal. Temporary gaps must not be treated as a completed map state in an animation.

Backward shifting is a more direct linear-probing variant. Let `hole` be a deleted position and `j` a later live slot in the same circular cluster. For home $h$, define circular distance $D(a,b)=(b-a)\bmod m$. Move the record at $j$ into `hole` exactly when $D(h,\mathrm{hole})<D(h,j)$. That condition says the hole lies on its original route before its current slot; if not, shifting would place the record before its own home and break search. After moving, the old $j$ becomes the new hole. Stop at the original empty boundary.

After deleting 21, slot zero is the temporary hole; slots 1, 2, 9 and 10 contain 32, 43, 9 and 10 respectively, and every other slot is empty. Record 32 at 1 has home 10 and distances one to zero versus two to 1, so it shifts to zero. Record 43 at 2 then shifts to 1. The hole at 2 can become empty once slot 3 is encountered. The inequality is essential for mixed homes. This repair is specific to linear-probing routes; applying it mechanically to double or quadratic hashing is unsound. One deletion can cost $\Theta(n)$ actual work.

## 12. Quadratic probing and coverage proofs

A common policy is $p(k,i)=(h(k)+i^2)\bmod m$. This does not generally permute the table. For odd prime $m$, offsets for $i=0,\ldots,(m-1)/2$ are distinct. If $i^2\equiv j^2\pmod m$, then $(i-j)(i+j)\equiv0$. Primality implies one factor is zero; within the chosen range, $i=j$ is the only possibility. Thus the route visits $(m+1)/2$ distinct positions. If fewer than half the slots are occupied and no tombstones obstruct the declared stop condition, an insertion must find an empty position in that range.

At $m=11$, square offsets are $[0,1,4,9,5,3]$ before repeats. At $m=8$, they are only $[0,1,4]$; empty slots elsewhere cannot help a key with home zero. At prime $m=11$ a half-full guarantee does not imply full-cycle coverage. Adding arbitrary coefficients changes the route and requires a separate theorem.

Two other policies illustrate why the precise formula matters. At primes $m\equiv3\pmod4$, alternating signed square offsets $0,+1,-1,+4,-4,\ldots$ visit every residue: positive nonzero squares and their negatives are disjoint because $-1$ is not a square in such a prime field, and together cover all nonzero residues. At capacities $m=2^r$, triangular offsets $i(i+1)/2$ for $0\le i<m$ form a permutation. If two offsets agree, $(i-j)(i+j+1)$ is divisible by $2^{r+1}$; the two factors have opposite parity, and the even factor would have to be divisible by $2^{r+1}$, impossible for distinct indices in that range. This proof concerns exact integer offsets before reduction.

Quadratic routes with the same home are identical, so they retain secondary clustering even when they avoid adjacent-home primary clustering. Do not transfer the half-load theorem between these different formulas.

<!-- SIM: quadratic -->

## 13. Double hashing and the exact cycle length

Double hashing uses $p(k,i)=(h_1(k)+i\,s(k))\bmod m$. The route returns to its starting point when $i\,s(k)$ is divisible by $m$. Let $g=\gcd(s(k),m)$, divide both by $g$, and use coprimality to conclude that the smallest positive return time is

$$L=\frac{m}{\gcd(s(k),m)}.$$

The route covers every slot exactly when $\gcd(s(k),m)=1$. A nonzero step alone is not enough. A step that does not divide $m$ is also not enough: step 8 at capacity 12 fails because the greatest common divisor is four, even though 8 does not divide 12. Prime capacity with step in $1,\ldots,m-1$ gives full coverage; power-of-two capacity requires an odd step. Step zero repeats one slot.

With $m=11$, $h_1(k)=k\bmod11$ and $s(k)=1+(k\bmod7)$, keys $[10,21,32,43]$ have steps $[4,1,5,2]$ and final slots $[10,0,4,1]$. Each key follows its own route, unlike linear probing. Two keys sharing both home and step share their entire route. There are only $m\varphi(m)$ distinct affine full-cycle routes, far fewer than $m!$ permutations for large $m$. Double hashing can approximate some behavior of uniform probing, but is not literally a uniform permutation sampler.

<!-- SIM: double -->

## 14. Uniform probing: exact and bounded expectations

In the ideal uniform-probing model, a fixed absent key's route is a uniformly random permutation independent of the occupied set. For $n<m$ occupied slots, let $X$ be probes until the first empty slot. Its tail for $1\le i\le n+1$ is

$$\Pr(X\ge i)=\prod_{j=0}^{i-2}\frac{n-j}{m-j}\le\alpha^{i-1}.$$

For $i>n+1$, the tail is zero. Summing tails gives $E[X]\le1/(1-\alpha)$. The exact finite expectation is $(m+1)/(m-n+1)$: the $m-n$ empty slots in a random ordering partition the occupied slots into $m-n+1$ exchangeable gaps, each with expected length $n/(m-n+1)$; the first gap plus the final empty probe gives the formula. At $m=10,n=9$, exact expectation is $11/2$, while the geometric upper bound is ten. Bounds are not exact answers.

For an equally likely successful key from a table built by independent uniform-permutation insertions without deletion, the $j$th insertion's expected probes are $(m+1)/(m-j+2)$. Its successful lookup follows the same route and stops at that inserted slot, so

$$C_{\mathrm{hit}}=\frac{m+1}{n}\sum_{j=1}^{n}\frac{1}{m-j+2}.$$

A customary upper bound is $\ln(1/(1-\alpha))/\alpha$; the limit at zero load is one. Its derivation sums the geometric miss bounds over the insertion history and bounds the harmonic sum by an integral. This successful-search formula assumes that uniformly chosen stored keys and insertion histories obey the stated model; updates, deletion and biased query popularity change the calculation.

## 15. Linear-probing estimates and model selection

Under independent uniform home positions and the standard large-table, fixed-load, insertion-only linear-probing model, classic estimates are

$$C_{\mathrm{hit}}\approx\frac{1}{2}\left(1+\frac{1}{1-\alpha}\right),\qquad C_{\mathrm{miss}}\approx\frac{1}{2}\left(1+\frac{1}{(1-\alpha)^2}\right).$$

At load one-half they estimate $1.5$ and $2.5$ probes. At load $0.9$ they estimate $5.5$ and $50.5$. The ideal permutation miss upper bound is ten at that latter load; substituting it for the linear-probing estimate erases clustering. The displayed table's exact run formula is preferable when the actual occupancy is given. Tombstones and deletion history also require care; substituting the live load into an insertion-only formula can be seriously misleading.

An examination calculation should start with a model label: exact specified table, independent uniform homes, universal family, or ideal random permutations. Then identify whether it asks for successful lookup, unsuccessful lookup, new insertion, duplicate update or a complete sequence. Without these conditions, a single universal numerical formula does not exist. The bank includes reverse calculations for allowed load and memory budgets, together with counterexamples to unjustified constant-time claims.

## 16. Resizing, cleanup and expected amortized cost

Resizing changes the index-reduction modulus; copying old physical slots is generally wrong. Allocate a new table, select an appropriate hash context, and reinsert every live entry. At capacity 7, keys 12 and 26 share home 5; at capacity 14, their homes become 12 and 12, while other records can split differently. Doubling is a capacity policy, not a proof of universally different homes.

If capacities grow geometrically, rebuilding costs sum as a geometric series. For capacities $m_0,2m_0,4m_0,\ldots$, the total allocated/scanned capacities before reaching $M$ are below $2M$. Under the appropriate bounded-load/randomness assumptions, rebuilding $n$ live entries takes expected linear time, so a sequence of updates costs expected linear total work. A single growth insertion can still take linear time. For chained tables, duplicate checks and reinsertions require their expected collision bounds; a deterministic adversarial hash can make rebuilding quadratic if implemented by general repeated bucket searches.

Use hysteresis: after growing near a chosen high-load threshold, shrink only at a substantially lower threshold. Growing at full capacity and shrinking whenever half empty can oscillate after alternating one insertion/deletion. A standard array policy grows when full and shrinks at one-quarter load, producing enough operations between rebuilds. Open-addressed tables often use lower thresholds and track nonempty occupancy to trigger same-capacity tombstone cleanup. State the exact thresholds before counting the rebuild sequence.

<!-- SIM: rebuild -->

## 17. Static perfect hashing from collision expectations

Perfect hashing is collision-free for a fixed known key set; it need not be injective on the entire universe. A one-level table of $n^2$ slots chosen from a universal family has expected collision-pair count below one-half. Markov's inequality yields collision-free probability at least one-half. Independent repeated choices therefore need at most two trials in expectation. Initializing $n^2$ physical slots can cost quadratic time, so an expected $O(n)$ testing statement does not automatically include dense-array initialization.

Two-level perfect hashing reduces space. First choose a universal hash into $n$ buckets. Let bucket lengths be $\ell_j$. The identity

$$\sum_j\ell_j^2=n+2\sum_j\binom{\ell_j}{2}$$

and universal collision bounds give expected squared-length sum at most $2n-1$. Reject a first-level choice when this sum exceeds $4n$. Markov ensures success probability at least one-half. Include bucket zero: all first-level buckets must be handled.

For each nonempty bucket, allocate $\ell_j^2$ slots and choose an independent universal second-level function until its stored keys do not collide. Each bucket trial succeeds with probability at least one-half and has $O(\ell_j^2)$ initialization/checking work. Since the accepted squared sum is at most $4n$, total expected construction work and final space are $O(n)$. Query computes the two indices and verifies the candidate's actual key, giving worst-case constant slot work after construction under word-key assumptions. An absent key can map to an occupied candidate; perfect placement of stored keys does not remove equality checking. Dynamic insertions can invalidate the fixed-set construction and need a different design.

<!-- SIM: perfect -->

## 18. Advanced comparisons with explicit limits

A Bloom filter represents membership approximately. It sets $k$ hashed bits per inserted key. With $b$ bits and $n$ keys, the probability a specified bit stays zero is $(1-1/b)^{kn}$ under independent draws. A common false-positive estimate is $(1-e^{-kn/b})^k$, using approximations and independence between queried bits. The ideal continuous optimum is $k\approx(b/n)\ln2$; implementation needs an integer choice. Standard insertion-only Bloom filters have no false negatives under their model, but clearing shared bits for deletion breaks that property. A counting filter needs counters and overflow care. A positive response is not proof of membership.

Two-table cuckoo hashing assigns each key two candidate slots. Lookup checks both, hence has a fixed worst-case slot count for a correctly built table. Insertion can displace a resident to its other candidate, potentially cycling. A bounded displacement limit and reseeding/rebuilding are essential. In a candidate graph, each key is an edge between its two slots; a connected component with more edges than vertices cannot place one key per slot. One cycle can be orientable; detecting a relocation cycle is not itself proof that every possible placement fails. Expected insertion claims need a stated load/randomness regime.

Robin Hood linear probing prefers the record with larger distance from its home when two records compete for a slot. This redistributes displacement; it is not the same as cuckoo's two-slot choice. Early unsuccessful-lookup termination needs the appropriate displacement invariant, and deletion must preserve it. No universal worst-case constant insertion claim follows. These comparisons identify useful mechanisms without presenting an unimplemented production library as a verified laboratory.

<!-- SIM: advanced -->

## 19. Applications and design reasoning

For two-sum, process records left to right. Before inserting $x$, query whether $t-x$ is already present. This permits using two distinct positions with equal values while preventing one entry from pairing with itself. Expected linear total time and linear space require the map's stated expected costs; comparison sorting with two pointers offers deterministic $O(n\log n)$ setup instead. Integer addition/subtraction needs an overflow policy.

For duplicate detection, stop when a key is already present; distinguish total input length from distinct live count. For frequency counts, `put` updates existing records, so many repetitions do not occupy new slots. Set intersection can build a table for one set and scan the other, giving expected linear total time with key costs stated. Prefix-sum maps solve zero-sum/subarray counting by matching equal accumulated sums; initialize the zero prefix before scanning and count prior occurrences before incrementing the current one.

Hashing alone does not support ordered rank or extrema efficiently. A balanced key-ordered tree can maintain subtree sizes and a priority winner aggregate; an identifier map helps locate records. Every mutation must update all affected structures. Median by key, maximum by priority and deletion by identifier are three different orders/access requirements. The authentic examination design problem and a worked companion make these distinctions explicit.

## 20. A precise procedure for examination problems

First write capacity, live count, deleted count, key domain, normalized modulo, probe formula and tie/update policy. For every insertion, list attempted positions in order, including the terminating empty cell if it is counted. Record successful destination, probes, live unequal comparisons and marker changes separately. For deletion, prove which later keys remain reachable. For a probability problem, identify the random object and fixed input before using a formula.

When a question says “collisions,” distinguish pair collisions, failed insertion encounters and entries beyond the first in a bucket. When it says “average,” distinguish an arithmetic bucket average, a uniform query average, an expectation over random functions and an amortized sequence average. When it says “constant,” identify load, key length, resizing and adversary assumptions. Each completed answer should include either a proof/invariant, an exact trace or a qualified probabilistic derivation. The final rules and fully worked questions consolidate these decisions without replacing the teaching above.

## 21. Complete-sentence summary

A hash table implements equality-based lookup by combining a deterministic table-lifetime hash context with a collision strategy. Chaining requires correct bucket membership and uniqueness; open addressing additionally requires a preserved reachability route. Live load, tombstone occupancy, chain order and probe coverage influence cost in different ways. Pairwise universal guarantees suffice for expected chained-query bounds, whereas ideal probe permutations and independent home choices support different formulas.

Exact tables are solved by exact routes and fixed-table sums. Statistical estimates are used only with their declared model and are labeled as estimates. Geometric resizing yields an expected amortized guarantee under appropriate collision assumptions while permitting expensive individual operations. Static two-level perfect hashing provides constant slot lookup and linear final space after a randomized construction; probabilistic filters and relocation schemes have separate contracts. Every result must retain its key-cost, randomness, load and operation assumptions.

## 22. Fully worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 23. Final reasoning rules and examination traps

<!-- INCLUDE: review -->

## 24. Editable specialized laboratory

<!-- LAB: hash -->

## 25. References and coverage boundaries

- Erik Demaine, Jason Ku and Justin Solomon, MIT 6.006 Spring 2020, [Lecture 4: Hashing](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ce9e94705b914598ce78a00a70a1f734_MIT6_006S20_lec4.pdf), pages 1–5.
- Frank Pfenning and Rob Simmons, CMU 15-122 Fall 2026, [Lecture 12: Hash Tables](https://www.cs.cmu.edu/~15122/handouts/lectures/12-hashing.pdf), pages 1–11.
- Robert Sedgewick and Kevin Wayne, Princeton COS226 Spring 2025, [Hash Tables slides](https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/34HashTables.pdf), pages 1–46; [Algorithms section 3.4](https://algs4.cs.princeton.edu/34hash/), teaching and selected exercise families.
- Felix Friedrich, ETH Zurich Data Structures and Algorithms Spring 2020, [English Lecture 9](https://lec.inf.ethz.ch/DA/2020/slides/daLecture9.en.pdf), all 98 PDF pages / printed slides 351–408, including repeated incremental diagrams.
- Stanford CS106B Summer 2025, [Written hashing lecture](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1258/lectures/24-hashing/), all teaching sections and exam-preparation discussion. Page credits identify Julie Zelenski and Sean Szumlanski; unverified instructor identity is not invented.
- Damon Wischik, Cambridge Algorithms 2023–24, [Lecture 8](https://www.cl.cam.ac.uk/teaching/2324/Algorithm1/content/slides08.pdf), dictionary and hashing content on pages 16–17; other pages inspected for selection.

The source audit identifies corrections, screened-but-unread candidates and exact acquisition evidence. The core scope is sequential examination-level hashing through static perfect hashing, with advanced comparison mechanisms qualified explicitly. Concurrent hashing, cryptographic internals and optimal probabilistic independence thresholds are outside that scope. Finite verification and proofs support the claims made here; they do not guarantee every unseen question or literal infallibility.
