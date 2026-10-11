# Final reasoning rules and examination traps

These rules supplement the derivations and worked problems. Read each condition before using its formula. A correct formula under the wrong probability model can produce an incorrect examination answer.

1. State whether the abstraction is a set, a map or a multimap. A map has one record per equality class, so putting an existing key updates its value and does not increase the live count. A multimap may intentionally retain several records with equal keys.

2. Hash equality is necessary for equal keys but insufficient to establish key equality. Two unequal keys can share a hash code or bucket; a successful lookup still requires the specified equality test.

3. Equality and hashing must refer to the same immutable key information. Changing that information after insertion can leave a record in a bucket that future lookups no longer visit. Rehashing after an authorized key change must repair the representation.

4. Normalize negative remainders explicitly. For positive capacity $m$, floor modulo produces a value in $\{0,\ldots,m-1\}$; a language remainder operation can instead produce a negative value and cannot directly index the array safely.

5. Charge for evaluating the hash function. Hashing an uncached string of length $L$ ordinarily requires $\Theta(L)$ character work even when the expected number of table probes is constant. Distinguish bit complexity from a fixed-word computational model.

6. Evaluate polynomial string hashes by Horner's rule: multiply the preceding residue by the base, add the next character code and reduce modulo $m$. This avoids storing large powers but does not make the function injective.

7. Arithmetic progressions can be pathological under modular hashing. Keys separated by a multiple of $m$ share a home, even when their original numeric values look widely separated. Calculate residues before assuming a uniform distribution.

8. Ordinary comparison lower bounds for ordered searching do not prohibit expected constant-time dictionary operations using hashing. They refer to different operation models and different information available from a key.

9. Separate chaining permits $n>m$ because a bucket stores a collection of records. Ordinary open addressing stores at most one live record per physical slot, so it requires $n\leq m$ and usually reserves substantial empty space.

10. Define $n$ as the number of live records and $m$ as the number of buckets or slots before computing $\alpha=n/m$. A duplicate-key update changes neither $n$ nor the live load.

11. A bucket with $b$ live records requires $b$ equality checks for an unsuccessful sequential search. Include the constant routing and bucket-access work if the question asks for total time rather than equality comparisons alone.

12. Head insertion reverses the insertion order within each separate chain. If a problem asks for the successful-search cost of a particular key, derive its actual chain position; its hash home alone does not give that cost.

13. A map insertion into a chain must normally check for an existing equal key. Concentrating $n$ distinct insertions in one bucket gives $n(n-1)/2$ failed equality checks. Constant-time linking does not remove this quadratic uniqueness-checking work.

14. For a fixed table and uniformly chosen live key, successful chain comparisons average $\sum_j b_j(b_j+1)/(2n)$. This expression depends on the actual bucket sizes, not merely the total load.

15. For a fixed table and a uniformly chosen home, unsuccessful chain equality checks average $n/m$. This exact conditional calculation does not assert that arbitrary queries choose their homes uniformly.

16. The bucket containing a uniformly chosen live key is size-biased. Its expected size is $\sum_j b_j^2/n$, whereas a uniformly chosen bucket has mean size $n/m$. Do not interchange these sampling procedures.

17. Under independent uniform placement, the expected number of occupied buckets is $m[1-(1-1/m)^n]$. It counts nonempty buckets, not pair collisions or equality checks.

18. Under independent uniform placement, one bucket's occupancy is binomial with mean $n/m$ and variance $(n/m)(1-1/m)$. The expected value alone does not prove every bucket is short.

19. Count unordered colliding pairs using one indicator for each pair of distinct keys. When pair collision probability is $1/m$, the expected count is $n(n-1)/(2m)$ by linearity of expectation; mutual independence of the indicators is unnecessary.

20. Distinguish a total pair count from collisions involving one selected key. The latter has expectation $(n-1)/m$ under the same pairwise assumptions. A factor of approximately $n/2$ separates the two quantities.

21. The birthday threshold concerns whether any pair collides. A table can have a low live load while the probability of at least one collision is already substantial; these are different events.

22. For $n\leq m$ independent uniform homes, the exact probability of no collision is $\prod_{i=0}^{n-1}(1-i/m)$. If $n>m$, that probability is zero by the pigeonhole principle.

23. The exponential birthday expression is an approximation, not an identity. Its accuracy requires control of the higher-order terms in the logarithm of the exact product. Use the finite product when the problem supplies small exact parameters.

24. The union bound gives $\Pr(\text{some collision})\leq n(n-1)/(2m)$. A bound larger than one is uninformative rather than a valid probability value; probabilities remain at most one.

25. A universal hash family bounds the collision probability for each fixed distinct pair when the function is chosen randomly. It does not say that every function in the family distributes every input set evenly.

26. For affine hashing modulo prime $p$, choose the multiplier from the nonzero field elements and the offset from the entire field. Restricting both parameters to the smaller input range can destroy the collision guarantee.

27. Distinct input keys must first have distinct encodings in the declared prime-field universe. Reducing arbitrary unbounded integer keys modulo a fixed small prime can merge them before the affine family is applied.

28. For distinct field inputs, the affine parameter map produces a uniform ordered pair of distinct field outputs. Count outputs that reduce to the same bucket; this counting proof supplies the universal bound without assuming independent final bucket values.

29. Pairwise collision control is weaker than full independence. Use linearity of expectation for collision counts, but do not automatically apply a binomial distribution or an independent birthday product to a merely universal family.

30. State whether keys and queries are fixed before the random function is sampled. An adversary that learns the function and then chooses colliding keys can invalidate a guarantee proved for a fixed input set.

31. Open addressing uses the same complete deterministic route for insertion, lookup and deletion of a particular key in one table context. A lookup using another route has no reason to find a displaced record.

32. A key is reachable only if no earlier slot on its insertion route is currently EMPTY. This is the invariant that justifies stopping a lookup at an empty slot.

33. An EMPTY slot certifies absence along a correctly maintained route; a DELETED marker does not. A tombstone preserves the possibility that an equal key is stored farther along that route.

34. Count a terminating EMPTY inspection as a probe even though it performs no equality comparison with a live key. Similarly, visiting a tombstone increases probe count but need not increase key-equality count.

35. For linear probing, compute $(h+i)\bmod m$ for successive offsets. Remember wraparound from $m-1$ to zero; writing an unbounded sequence of array indices loses the circular structure.

36. A contiguous circular run of $r$ occupied cells contributes $r(r+1)/2$ extra unsuccessful-search probes over uniformly chosen homes. Summing these terms yields the exact fixed-table miss average when at least one EMPTY slot exists.

37. Equal load factors do not imply equal linear-probing costs. A single long cluster and many isolated entries can have very different sums of squared run lengths. Use the actual arrangement if it is given.

38. Primary clustering attracts additional keys whose homes fall inside an existing run. This phenomenon follows from linear routing and should not be confused with unequal keys merely sharing their original home.

39. During insertion with tombstones, remember the first reusable marker and continue searching for an existing equal key. Committing at the marker immediately can create a duplicate map entry.

40. If an equal key is found beyond a tombstone, update its existing record. Neither a new live entry nor a tombstone reuse occurs; the marker remains available for another genuinely absent key.

41. If a full bounded route scan finds no duplicate but remembers a tombstone, insertion can reuse that marker. The absence of an EMPTY slot does not itself prove that no physical reusable slot exists.

42. Every probing loop needs a finite bound. A full table or a nonpermuting route can otherwise make an unsuccessful lookup loop forever. Report route exhaustion separately from successful insertion.

43. Tombstone occupancy affects search termination. A table with few live keys but many markers can have long misses; distinguish live load $n/m$ from nonempty routing occupancy $(n+d)/m$.

44. Backward shifting is a linear-probing repair rule. For home $h$, hole $u$ and current slot $v$, shift only when circular distance from $h$ to $u$ is strictly less than the distance from $h$ to $v$.

45. A record already at its home must remain there when the repair hole lies later on its circular route. Mechanically shifting every encountered record can break reachability for mixed-home clusters.

46. The repair hole is temporary until the scan reaches the cluster boundary. Client lookups during an incomplete repair need an additional concurrency protocol; the sequential proof assumes the repair operation is completed atomically from their perspective.

47. The route $h+i^2\bmod p$ visits exactly $(p+1)/2$ positions for odd prime $p$. It is not a permutation of all $p$ slots, even though the modulus is prime.

48. For square probing at odd prime capacity, fewer than $(p+1)/2$ nonempty positions guarantee an empty position on each route. Tombstones count as nonempty for this guarantee; low live load alone is insufficient after many deletions.

49. Quadratic probing generally retains secondary clustering: keys with the same home use the same offset sequence. Eliminating contiguous linear runs does not eliminate every correlation between probe routes.

50. Alternating positive and negative squares give full coverage at primes congruent to three modulo four. The proof relies on minus one being a nonsquare; it does not apply to primes congruent to one modulo four.

51. Triangular offsets $i(i+1)/2$ form a permutation modulo a power of two over one full capacity-length route. Preserve the exact offset formula and the power-of-two capacity condition when using this result.

52. Double hashing uses $h_1(k)+i\,s(k)$ modulo $m$. Its exact cycle length is $m/\gcd(s(k),m)$, so full coverage requires the step to be coprime with the capacity.

53. A step that does not divide the capacity need not be coprime with it. At capacity twelve, step eight does not divide twelve but visits only three slots; use the greatest common divisor test.

54. At prime capacity, every nonzero step modulo the capacity gives full coverage. At a power-of-two capacity, the valid full-cycle steps are precisely the odd residues.

55. Zero step revisits the home forever unless the loop has a finite bound. A negative step can give full coverage after modular normalization, but the same coprimality condition still applies.

56. Distinct homes or steps can produce distinct affine routes, yet double hashing samples far fewer routes than all $m!$ permutations. Do not identify its deterministic route family with ideal uniform permutation probing.

57. In ideal uniform permutation probing with $n<m$ occupied cells, an unsuccessful search has exact expectation $(m+1)/(m-n+1)$. This finite formula includes the terminating empty inspection.

58. The familiar $1/(1-\alpha)$ unsuccessful-search expression is an upper bound in the ideal model, not the exact finite expectation. For small capacities, the difference can be substantial.

59. The ideal successful-search average requires a stated insertion history and a uniformly chosen stored key. Average each key's insertion-time miss cost at its earlier occupancy; do not use the final-load miss cost for every key.

60. The logarithmic ideal successful-search bound and the classical linear-probing estimates come from different models. Always identify whether the question assumes random permutations or independent uniform linear-probing homes.

61. The classical linear-probing miss estimate grows approximately as half of $(1-\alpha)^{-2}$ near full load. The ideal permutation bound grows as $(1-\alpha)^{-1}$, illustrating why substituting one for the other can materially underestimate work.

62. An expected bound concerns randomness in a declared input or hashing model. It does not remove the deterministic linear worst case for one lookup or the possibility of a concentrated adversarial input.

63. Resizing changes the modulus and therefore the home of a key. Reinsert live records under the new context instead of copying physical old slots to equal array indices.

64. Preserve record identity, values and equality classes during rebuilding. Tombstones are discarded; live records must appear once each. A rebuild is not an ordinary insertion that creates additional user records.

65. Geometric capacity growth bounds the sum of allocation sizes by a geometric series. If rebuilding has expected linear cost under the stated model, this supports expected amortized constant update overhead.

66. One growth-triggering insertion can still take linear actual time. Expected, amortized and worst-case are separate qualifiers; an expected amortized bound does not prove a constant latency bound for every operation.

67. Use separated growth and shrink thresholds. Shrinking immediately after crossing the growth boundary can cause repeated expensive rebuilds on an alternating insert/delete sequence.

68. Cleanup decisions may depend on marker occupancy as well as live load. Rebuilding at the same capacity can remove tombstones and shorten routes without increasing the physical array size.

69. Perfect hashing is injective on a fixed known set, not necessarily on the whole universe. A candidate query still requires checking the stored key to reject an absent key mapped to the same position.

70. A universal one-level table with $n^2$ positions has expected pair-collision count below one-half for $n>1$. Markov's inequality gives at least one-half probability of no collision, but dense initialization can still require quadratic work.

71. The identity $\sum_j b_j^2=n+2C$ relates squared bucket sizes to the number $C$ of unordered colliding pairs. It is an exact identity for a fixed distribution, preceding any expectation calculation.

72. With approximately $n$ first-level buckets and universal hashing, expected squared allocation is below $2n$. Rejecting a first-level function when allocation exceeds $4n$ yields a constant acceptance probability by Markov's inequality.

73. Allocate $b_j^2$ second-level positions for a bucket containing $b_j$ fixed keys. Independently retry a universal second-level function until those keys are collision-free, and include bucket zero in the construction.

74. A constant expected number of trials requires fresh independent parameter choices and a lower-bounded success probability. A deterministic search in the compact laboratory illustrates valid placement but is not evidence for the randomized trial theorem.

75. A Bloom filter stores bits rather than key identities. All queried bits being set means possibly present; an unset bit certifies absence when insertions use the same functions and no unsafe bit clearing has occurred.

76. The common Bloom false-positive expression $(1-e^{-kn/m})^k$ is an approximation under a stated ideal hashing model. Choosing $k$ near $(m/n)\ln2$ minimizes that approximation; compare neighboring integer choices.

77. Cuckoo placement gives each key a small set of candidates. A set of keys with fewer total candidate positions than keys is impossible to place; a bounded failed relocation attempt does not itself prove impossibility for every candidate graph.

78. Robin Hood insertion prioritizes the more displaced record at a contested slot. Search and deletion rules must match that representation; importing tombstone or early-stopping rules from another policy requires a separate proof.

79. Hash tables support equality lookup rather than ordered statistics by themselves. Median, predecessor and range requests need additional order-maintaining structure or explicitly analyzed extra work.

80. Finish an examination solution by checking the exact event counted, load definition, route formula, marker policy, query distribution, computational model and complexity qualifier. A numeric answer without these conditions can conceal a different problem from the one stated.
