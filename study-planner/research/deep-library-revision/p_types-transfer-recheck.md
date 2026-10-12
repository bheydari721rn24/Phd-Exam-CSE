# Independent transfer-challenge, rule and model recheck

Date: 12 October 2026. Scope: the complete `p_types-method-instruction.md`, its ten authored transfer challenges, all new examination rules16–40 in `p_types-exam-rules.md`, `build_types_question_models.py`, generated typed-model data, and the complete `typesQuestion` renderer in `semantic-diagrams.js`. No shared manuscript, model, renderer or publication file was edited by this audit. No undefined C expression was executed.

## 1. Ten challenge conclusions

All ten challenge calculations agree with independent derivation under their declared contracts.

| Challenge | Independently checked conclusion |
|---|---|
| A | uint16 value65535 promotes to int32; its square4294836225 exceeds INT_MAX. Cast before multiplication to unsigned32 makes this exact product representable. A uint64 destination alone cannot repair the original operation. |
| B | Integer -1 converts to unsigned32 maximum; floating -1.0 has an unrepresentable truncated unsigned result; floating -0.75 truncates to representable zero. |
| C | LP64 long64 contains every unsigned-int32 value, so -1<1 is true in long. LLP64 long32 does not contain that unsigned range, so the common unsigned-long32 comparison is false. |
| D | `i++ + i++` is unsequenced UB; comma returns2 and leaves3; logical AND returns1 and leaves3, starting independently at1. |
| E | Parenthesized repeated-argument macro with i++ remains UB; an actual one-argument square function captures old value1 once, increments to2 and returns1 for this instance. |
| F | `-(2*n)` at int32 n=1073741824 overflows in the intermediate product despite a representable final mathematical value. Widening must precede multiplication. |
| G | `1u<<31` gives2147483648; `1u<<32` and `1<<31` are UB in the stated C17 model; negative signed right shift is implementation-defined. |
| H | Binary64 nearest-even maps a+1 to a and a+3 to a+4 at a=2^53, using opposite retained-parity decisions. |
| I | Minimum-layout widths5,4,1 have offsets0,8,12 and size16; reorder4,5,1 gives0,4,9 and size12. Member bytes remain10; padding changes6→2. |
| J | Reject n=M, guard c=n+1 by M/4, then guard n by M/(4c), with positive divisors. All subsequent products are representable; allocation success remains separate. |

The named exact-width typedefs are covered by the chapter's explicit availability premise. LP64 and LLP64 are declared comparison models, not inferred host facts. In Challenge F the final signed conversion is valid because the exact final value is within int32 range; it is not an appeal to implementation-defined narrowing.

### Signed-shift rule checked against the primary issue record

The C17 signed-left-shift conclusion must not be replaced by C++14's corresponding-unsigned-type rule. The official [WG14 issue0463](https://open-std.org/JTC1/SC22/WG14/issues/c11c17/issue0463.html) was freshly consulted: its proposed C++-style change was treated as a feature request, not an accepted defect correction. Thus the existing `1<<31` classification is appropriate for this chapter's C17 scope. N1570 remains identified as a C11 committee draft, not a published C17 standard.

## 2. Examination-rule recheck

Rules16–40 contain no newly identified mathematical error under the stated contracts. Particular boundary checks:

- Rule21 preserves the essential distinction between integer-source modular conversion and floating-source range requirements.
- Rule23 correctly tests range after rank when mixing signed and unsigned operands; long's greater rank alone does not settle the result.
- Rule27 is a representation warning; combine it with the master promotion procedure before classifying unary minus. The corrected Q20–23 answers now explain narrow-source promotion explicitly.
- Rule29's quotient/remainder ceiling expression also fits its type: for d=1 there is no increment; for d≥2 the quotient is at most half a nonnegative type maximum, leaving room for the optional1. The operands must belong to the stated same compatible integer model.
- Rule38 correctly uses the promoted left width and separately classifies invalid count, signed left-shift range and negative signed right-shift behavior. An eight-bit unsigned source promoted to int32 can be left-shifted by8 because its maximum255 times256 fits int32; its evaluated result is not an eight-bit modular result.
- Rule39 distinguishes numeric scalar truth from representation bits. IEEE negative zero compares equal to zero; NaN does not. A null pointer representation is a different portability fact from its truth value.
- The array, packed-flag and ABI rules identify actual objects, row stride, adjusted parameter, serialization and minimum-padding assumptions separately.

The source-course roles in method section7 were read as declared provenance, but this subtask did not re-open those university texts and does not independently confirm their reading inventory.

## 3. Model-data scientific checks actually executed

The builder was executed through its AST **with all top-level output-write and print calls removed**, so only an in-memory model reconstruction was created. It produced **21 model records and86 checkpoints**. Assertions checked each record's consistent mechanism kind and exactly one initial checkpoint. Additional independent assertions verified:

- For all four authentic adder instances, `carryin != carryout` agrees with the signed-range overflow result and stored low bits equal the mathematical total modulo16.
- Layout offsets are multiples of4, internal minimum padding is0–3 bytes, and the last member end equals the stated total size.
- Each packed count supplies enough flag positions and one fewer byte does not.

The other data were read individually: signed and unsigned residues, exact-real CHOP stages, decimal rounding nodes, selected conditional values, row offsets and stride, binary midpoint locations and negative quotient/remainder all match the manuscript. No source data assign a numeric result to an undefined C operation.

The actual renderer function was also run with read-only drawing stubs recording its raw drawing calls for every generated checkpoint. This checks that a checkpoint changes mathematical labels/objects rather than merely claiming that it did. It is not a browser-layout, font, animation-timing or accessibility test.

## 4. Renderer corrections already applied and independently re-read

The integrating agent applied the first reported progression fixes during this audit. The current function and builder were re-read afterward:

- **wrap:** type-only checkpoint, then unsigned residue, then signed-domain failure; pending expressions are distinct from computed results.
- **width:** unknown bit slots, then selected extremal pattern, then positional sum.
- **macro:** token-substitution card, parse tree, evaluated tree nodes, then a different-expression UB board.
- **register:** input card, exact total/carry, residue, then a separately labeled promoted C lane.
- **division:** exact quotient location, truncation choice, reconstruction equation, then a dedicated minimum/-1 UB board.
- **macro/division terminal formulas:** their changed-expression UB frames now use a dedicated classification formula rather than leaving the prior safe numerical formula under an unrelated changed expression.

The two earlier answer corrections were separately rechecked in the regenerated manuscript: Q1 now names option3 for unsigned carry; Q20–23 classify negation after promotion. Their original numeric keys remain unchanged.

## 5. Checkpoint/label findings from the intermediate inspection

These are concrete rendering-state findings, not claims that the scientific challenge answers are wrong. The integrating agent was notified of them.

### Short-circuit input, guard and completion are drawn identically

`types-question-short` checkpoints0,1,2 produce identical raw diagrams. Already at the initial input-read checkpoint, the guard reads false, the right operand is not evaluated and the final logical result is0. Gate those facts by stage: input known/guard pending; guard evaluated/right skipped; whole expression completed. The bitwise-change UB board is distinct and its classification is correct.

### Floating midpoint inspection does not show its selection

`types-question-precision` checkpoints0–2 produce the same raw diagram with midpoint33 already marked. Checkpoints0–1 of `types-question-binary64` are likewise identical. At the selection stage the renderer shows no selected-neighbor marker or parity label; only the caption explains which neighbor wins. Show representable neighbors first, then the exact missing midpoint, then an explicit arrow/marker to the even-significand selected neighbor. For the35 or a+3 example, visibly change the selected target to36 or a+4. The number-line coordinates and the asymmetric1/2 spacing themselves are correct.

### Signed checkpoint3 retains the positive-maximum pattern

In `types-question-signed`, checkpoint2 constructs maximum `01111` and checkpoint3 retains that pattern while its caption discusses negating the minimum. The raw diagrams at2 and3 are identical. For a minimum-negation domain check, show the original `10000` representation, its mathematical positive magnitude16, and distinguish the unavailable positive16 in the same five-bit representation from a possible wider promoted arithmetic domain. Do not depict15 as the subject of the minimum-negation check.

### Layout interval labels should follow the data

The n=8 caption describes `padding8..7 if nonempty`, although the actual padding set is empty. Render “no internal padding” when n=offset. The first/second member labels currently have fixed centers180 and535 even though interval positions change with n. Place them at centers calculated from the occupied member intervals, or draw explicit connected interval brackets. Actual byte-index cells and sizes are scientifically correct.

### Static reference maps versus execution steps

The pipeline/CHOP/decimal/cast diagrams reveal all future values at the initial checkpoint and then change mainly a highlight. Their values and arrows are correct, but they are complete reference maps rather than demonstrations of values becoming available. Either explicitly label them “complete trace; active step highlighted” or show pending future values until the relevant operation executes. A stated model should make this teaching choice clear; it must never imply that an unselected conditional branch was evaluated.

## 6. Limits and handoff

All ten challenge conclusions and the new rules agree with the declared mathematical and C contracts. The model data are correct; the remaining issues concern meaningful step revelation and truthful association of labels with the currently taught operation. The script-level audit does not replace human inspection of final SVG layout, text-to-card clearance, connected arrows, controls, print or mobile rendering. No shared file was modified, and no student pretest was requested.

## 7. Final closure recheck of the later patches

The complete current renderer was re-read after the integrating agent applied the final changes. The generated model data were again rendered through recording drawing stubs for all86 checkpoints.

- Short circuit now distinguishes input/guard pending, false guard with bypass, completed logical zero, and the changed bitwise undefined case.
- Floating checkpoints first show neighbors without a midpoint, then the missing odd midpoint, then a visible selected-neighbor ring with the correct even-significand label. The second midpoint selects36 or a+4 correctly. The binary64 final equality revisits its first selected-neighbor geometry after demonstrating the other tie; this is a valid closing reuse, not an unexecuted calculation.
- The signed-domain terminal board now explicitly shows the narrow-source promotion comparison with int32 unary minus rather than retaining the positive-maximum five-bit pattern.
- The aligned n=8 layout says no internal padding, and the member label positions are computed from their actual intervals.
- All previously identical adjacent checkpoint draws were eliminated. Pipeline and decimal diagrams remain complete reference maps with an active checkpoint highlight; their type/value data are correct.

The final signed-terminal formula association was identified and then **corrected and freshly rechecked after regeneration**. The actual generated checkpoint now stores `\text{Promoted int32: }-(-128)=128`, and its caption explicitly identifies the changed eight-bit signed-char source context, its int32 promotion and the contrasting undefined `-INT_MIN` case. The preceding checkpoints retain their five-bit positional model. The formula, board and caption therefore teach the same operation.

**Closure:** no unresolved concrete scientific or checkpoint-association correction remains from this independent subtask. The ten transfer challenges, new examination rules and21 model mechanisms agree with their stated contracts after the recorded fixes. Final browser, glyph and layout inspection remains the integrating agent's separate gate; this closure does not claim those checks were performed here.
