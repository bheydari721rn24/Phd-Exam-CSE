# Control Flow: independent answer-manuscript recheck

Review date: 2026-10-12. Scope: all 45 answers in `p_flow-solutions.md` and the generating content in `research/write_flow_answers.py`. This report does not change chapter HTML, metadata, gates, source PDFs or publication.

## Result

No unresolved concrete mathematical or C-semantics error was found in the reviewed manuscript. All 45 stated option numbers agree with the independent ledger derived from the question stems and options. This is a bounded audit of the present text; it is not a guarantee about all possible questions, all implementations or the final rendered chapter.

Read-only AST reconstruction removed the writer's final file-write and print expressions before evaluating its content construction. The reconstructed 45-answer text matches the saved manuscript exactly after ordinary text-file newline normalization. No generator output was overwritten during this recheck.

- Manuscript normalized UTF-8 SHA-256: `10f65738e91f4b3451e9d5193b0e262b82f37ae94e2471c64856b7d55116939c`.
- Writer file SHA-256: `f77d9aaab5580c38757fafa6f85a02468b4486e5a23bd4e56e2e2780a9429082`.
- Answer ledger, Q1–Q45: `2,4,1,1,1,3,3,2,2,1,2,3,2,1,4,3,2,1,4,2,1,4,3,1,4,3,2,2,1,4,3,3,2,1,4,4,3,2,1,2,1,4,3,1,3`.

## Eight-family mathematical checks

Each family proof was read in every placement, including the individual instance/distractor explanation rather than only its shared derivation.

| Questions | General result under the stated domain | n = 5 | n = 8 | Important boundary checked |
|---|---|---:|---:|---|
| 12–15 | Sum before index increment: n(n−1)/2 | 10 | 28 | Empty input gives zero; a mathematical product in a proof is not automatically a safe C expression. |
| 16–19 | Logical guard final state: i = j = n | j = 5 | j = 8 | Reversed operands require an extra j increment. Bitwise replacement gives (1,2) for positive safe n, rather than simply adding one to the original j. |
| 20–23 | Filtering multiples of three from 1…3n gives 2n contributions | 10 | 16 | Last header update needs 3n+1 representable, not merely 3n. A manual while update skipped by continue changes progress. |
| 24–27 | After-addition threshold S_n first reached after n additions | 5 | 8 | Positive terms establish strict prefix growth. The zero-threshold extension needs a separately chosen test location. |
| 28–31 | Complete binary call tree: 2^(n+1)−1 calls | 63 | 511 | Base calls count; maximum ordinary sequential active depth is n+1, not total calls. |
| 32–35 | Single-chain local work: n(n+1)/2 | 15 | 36 | Zero base contributes no local work but is still a call. Tail-call optimization does not delete the defined local-operation count. |
| 36–39 | Sequential arithmetic swap: (a,b) = (2,n) | (2,5) | (2,8) | For positive int32 inputs, n≤INT_MAX−2 is needed for the first sum. Final representability alone does not repair signed overflow. Distinct objects are required. |
| 40–43 | Signed post-test decrements: n+1 body entries, final i=−1 | 6 | 9 | n=0 gives one entry. The formula is not extended indiscriminately to negative inputs. Unsigned nonnegative comparison cannot supply the same stopping condition. |

Independent finite mathematical models checked these eight results for n=0…64 (the positive-threshold claim only when n>0): 519 evaluated family assertions. These finite checks corroborate the symbolic proofs; they do not replace the proofs or infer C behavior by executing undefined operations.

## Standalone answers and source reconciliation

- **Q1:** The weakly ordered triple count is C(17,3)=680, so the initialized accumulator is 690. The reversible shift to a strictly increasing triple and the independent sum of j(16−j) agree. Exhaustive mathematical counts for upper bounds 0…20 agree with C(n+2,3).
- **Q2:** The current text explicitly uses an actual input order statistic for the stronger permutation claim, allows lower or upper median for even lengths, and separately describes the arithmetic-average caveat. Strict descending order, value preservation and termination are established as distinct obligations. This resolves the previously identified missing convention.
- **Q3:** The corrected authentic fourth option decrements the source by two and advances destination by two from destination one. The solution attributes its failure to destination shift/gaps, not an erroneous source stride. Copy count ceil(N/2), source/destination indices and the empty-input guard agree with the original pseudocode model. The concrete-C discussion is explicitly conditional on suitable bounds and allocations.
- **Q4–Q6:** Nearest-unmatched-if binding, continued for-header updates, and single switch dispatch with subsequent fallthrough give 0, 9 and 6 respectively. Skipped inner decisions and executed-false decisions are distinguished.
- **Q7:** The modulo-256 orbit comprises the 128 even residues; target one is unreachable. The text distinguishes this abstract model from a claim about host unsigned-int width and from the qualified C rule permitting termination assumptions in certain nonobservable loops.
- **Q8:** Source indices 10,8,6,4,2,0 produce six writes and a seventh negative-source base call. Index ten is not treated as length ten.
- **Q9:** Four evaluated postfix guards produce final (x,c)=(4,3). The prefix variant gives (3,2). The failed guard's increment is included, with its representability condition.
- **Q10:** Every enabled transition strictly decreases a nonnegative ranking; parity, population count and residue modulo three fail as strictly decreasing candidates by the supplied witnesses. Initial 13 has six transitions to zero.
- **Q11:** Three outer entries each produce two increments before inner break, giving six increments, nine inner entries and six inner updates. Break is correctly scoped.
- **Q44:** The original pure predicates are disjoint before exit. Either predicate order ends at (19,8). The trace includes eight reached bodies and omits both the break-index addition and update. At break target nine, continue-first gives (37,11), while break-first gives (27,9); both extensions were independently traced.
- **Q45:** Solving 6t≡64 (mod 256) gives t≡96 (mod 128); 96 is the first positive visit. Listed alternatives 32,64,96,128 produce residues 192,128,64,0. Reachability and period are correctly separated.

The original PDF-page/hash inspection supporting Q1–Q3 is documented in the earlier `p_flow-independent-math.md` audit. This manuscript recheck reuses that verified source reconciliation and does not falsely claim a second new visual inspection.

## Integration limits

No answer correction is requested from this recheck. The Q19 mathematical ampersand notation is already assigned to native-renderer normalization by the integrating agent. Final formula rendering, diagram associations, browser geometry and publication consistency are separate pending integration checks; this report cannot certify those from Markdown alone. Abstract counts and defined machine execution remain separate throughout the reviewed explanations.
