# Control Flow: independent question-model recheck

Date: 2026-10-12. Scope: complete `research/build_flow_question_models.py`, complete `research/flow-question-renderer.js`, and generated `flow-question-*` scene snapshots in `dist/chapters/concept-animations.json`. Only this report is edited.

## Transfer-report closure

The two rule-domain corrections identified in `p_flow-transfer-recheck.md` are present in the current rule manuscript:

- Rule 20 explicitly restricts the logarithmic transition formula to n>0 and states zero transitions at n=0 without evaluating log2(0).
- Rule 33 explicitly requires a representable signed initial n≥0 and separately identifies negative-input analysis and the undefined signed-minimum decrement.

Those two previously open scientific issues are closed.

## Concrete model corrections requested

### 1. Partial toll accounting must not reuse the chapter's W(k)

Current toll formulas read W_1=5, W_2=9, W_3=12, W_4=14, W_5=15. These are accumulated work along the root-first parameter sequence 5,4,3,2,1, not the chapter's function W(k)=k(k+1)/2. The first four formulas are false if interpreted using that defined function. The numerical running totals themselves are correct.

Use a separate partial-accounting sequence, for example A_0=0 and A_t=Σ[r=0…t−1](5−r), giving A_1=5, A_2=9, A_3=12, A_4=14, A_5=15=W(5). This separates number of accounted calls from the recursive parameter. A zero-accounted-work initial frame would also make the first transition explicit; no invented zero toll should be attributed to the root's already-performed work.

### 2. The target orbit's period frame must declare its post-stop status

The target-64 scene includes t=128 after the target was first reached at t=96. The residue formula at 128 is correct, but a target-stopping loop would already have terminated. Label this frame as a counterfactual continuation of the full mathematical orbit after the stopping event, or omit it from actual execution playback. Its caption/formula/display should not imply that the stopping loop continued to update normally.

This restriction does not affect the target-one unreachable scene, where the orbit can repeat in the declared abstract model.

### 3. Unentered nested-loop indices must be pending rather than zero

The initial nested scene says neither loop has entered yet, but supplies i=0 and j=0 and renders those as actual index values. The source loop initializes its indices to one on entry; it does not establish those zero values before the initializers execute. Show the initialized counter c=0 while marking index values as pending/not initialized, then expose the real values at the first entered checkpoint. Do not manufacture numeric values for unentered or out-of-scope loop indices.

## Verified associations

The generated set inspected contains 21 models and 142 frames. The following associations were independently checked from builder operations and renderer dispatch, rather than inferred from scene titles alone.

| Scene mechanism | Verified scientific association |
|---|---|
| Triples | Each bar corresponds to one middle-index group j·(16−j); total 680. The shift example (2,2,4)→(2,3,6) preserves the weak-to-strict bijection. Initial accumulator 10 and final 690 are kept separate. |
| SplitSort | Declared distinct five-element representative uses member pivot 3. Greater output precedes pivot and smaller output; original identities are preserved. This scene is not mislabeled as a different actual input. |
| Copy source alternatives | The N=7 representative reads indices 6,4,2,0. All variants retain source stride two; only destination offset/stride changes to t+1,2t,2t+1. Unwritten cells are dots, not invented zeros. Source-size 7 is declared rather than replacing the general source question silently. |
| Copy index ten | Source sequence 10,8,6,4,2,0 gives six writes; −2 base call gives seven calls without a source read. The model separates last index from array length. |
| Dangling else | Outer false bypasses the entire inner conditional, so b is not evaluated and initialized x stays zero. Diagram ownership matches the grammar. |
| Filtered and prefix traces | Body checkpoint updates the accumulator but not the current header index update. Completed-update counts lag body-entry count by one there. Final false-guard frames include the last header update. Continue rows skip only accumulator work. |
| Stateful logical guard | Initial counters are both zero. Right-guard frames show j advanced while i remains old; body-completed frames restore i=j. Final left-only false guard skips ++j. History headings i/j/operation agree with these temporary states. |
| Switch | Dispatch enters case 2 once. Its addition precedes case-3 fallthrough, then break prevents default. State x runs 0→2→6→6. |
| Modulo orbit | Residue equals 6t mod 256; the circle positions are update order, not ascending residue magnitude. Highlight uses t mod 128. Target 64 is hit at 96; target 1 is outside the even subgroup. The post-stop-frame scope correction above remains necessary. |
| Postfix guard | Each row distinguishes old compared x, stored x+1 and post-body count c. The fourth failed guard leaves x=4,c=3; initial frame precedes all guards. |
| Ranking | Actual trajectory 13,12,6,3,2,1,0 matches binary population count and bit length at each selected value. Halving does not incorrectly reduce population count. |
| Nested break | Entered checkpoints satisfy total=2(i−1)+min(j,2), with j=3 breaking before increment. Three outer entries contribute six increments. Pending initial indices need the correction above. |
| Threshold | Actual n=5 uses H=15. Prefixes 0,1,3,6,10,15 equal i(i+1)/2; the hit is exactly the fifth after-addition checkpoint. No extra update beyond break is depicted. |
| Binary tree | Depth-three representative has 15 total calls and four active frames. Labels explicitly distinguish it from original n=5 count 63. Level d nodes have parameter 3−d; base leaves are zero. The green path is one representative active stack, not simultaneous occupancy of the whole counted tree. |
| Toll | Parameters 5,4,3,2,1 and running totals 5,9,12,14,15 are numerically correct. Rename the partial sequence as requested above. |
| Swap | Four sequential states (5,2),(7,2),(7,5),(2,5) match full-expression dependencies. The separate invalid INT_MAX+2 example is described as undefined, not given a fabricated swapped result. |
| Signed post-test | Initial i=5 has no preliminary guard. After t decrements, i=5−t; six trailing tests end at −1. No unsigned wrap is substituted. |
| Condition priorities | Break 8 gives (19,8) under both pure-test orders. Changed break 9 gives (37,11) continue-first and (27,9) break-first. Scenario captions expose the changed target and order. |

The renderer's new HTML history table uses the supplied rows and matching headings; it does not change the state mathematics. Final font, clipping, geometry, playback usability and browser rendering are outside this read-only scientific audit and remain the integrating agent's visual verification.

## Status

Snapshot arithmetic checks passed for the inspected mechanisms. The three concrete notation/checkpoint-association issues above are open until patched and rechecked. This report makes no global guarantee about all future scenes or questions.

## Closure after regeneration

Fresh recheck on 2026-10-12 confirms all three requested model corrections in both source construction and generated snapshots:

1. Toll partial formulas now use A_1=5, A_2=9, A_3=12, A_4=14, A_5=15. The scene description defines A_t as the first t descending tolls and separately identifies W(5)=15 as total work. The notation collision is closed.
2. The target-64 frame at t=128 has `extension=true`, an explicit counterfactual post-stop caption, and a corresponding counterfactual renderer heading. Earlier actual checkpoints are not labeled as extensions. The residue zero is now clearly a full-orbit analysis beyond the already-completed target-stopping loop, closing the execution-scope ambiguity.
3. The nested initial snapshot and its teaching-state data use null for both i and j. The renderer maps these nulls to “not initialized yet,” while the counter remains initialized to zero. The caption states that neither loop initializer has established an index value. The fabricated numeric initial indices are removed.

The regenerated inventory remains 21 models and 142 frames. Exact snapshot/description checks for all three corrections passed. No unresolved scientific correction remains from this model audit; the earlier open-status paragraph is historical evidence preceding these fixes.

Source hashes at this closure:

- Builder SHA-256: `d0aa4d2b2fabaef291837be56a40a34ce7fdf70125b3ade535f51c3799a99fde`.
- Renderer SHA-256: `5d6b8671a5e0214808e609d6a93e4f74bb7b4bfa0cf090e44aa01c4023cd17bf`.

The HTML history-table geometry and final browser appearance are still separately evaluated by the integrating agent. This closure confirms data semantics and corresponding label logic, not unobserved pixel layout.
