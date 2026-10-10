# Arithmetic circuits: scientific, problem and visual audit

## Review outcome

The new chapter is a completed review draft, not a student-approved chapter. It contains thirty teaching sections, eighty original or independently reconstructed worked problems, two authenticated doctoral-examination bridges, eighty final condition-bearing reasoning rules, and fifteen subject-specific circuit/process models with seventy-one stored checkpoints. Every solution is complete English prose, and every final rule states the representation or implementation assumptions needed for its use.

## Scientific checks

The executable models were compared against independently generated exact-integer references for 16,648 cases, covering every operand pair at widths one through five for the principal binary operations, all three four-bit compressor operands, all valid BCD input pairs with both carry inputs, all one-bit gate inputs and selected eight-bit carry-select boundaries. A total of 84,808 intermediate checkpoints were checked, including local full-adder weight conservation, connected adjacent carries, carry-save weighted totals and the division prefix/remainder invariant. Six invalid-input classes were rejected.

The chapter contains 510 native MathML expressions before interactive rendering. Their XML, mathematical delimiter balance and closing-script bases passed the audit. The browser also checked real rendered fence bounds, math fonts and the absence of underlined links. These checks do not prove that no possible editorial or mathematical error remains; they provide specific reproducible evidence.

The independent exact-value audit corrects source errors in overflow annotations, signed comparison, saturation endpoints and carry indexing. The final lesson additionally derives signed partial-product correction constants rather than quoting an unqualified Baugh–Wooley diagram. The Booth pair order is explicitly current bit followed by lower bit.

## Coverage and instructional figures

| Scope | Teaching / problems | Visual or proof method |
| --- | --- | --- |
| Half/full adders and population counting | Sections 3–4; problems 1–5, 71 | Actual XOR/AND/OR schematic, weighted identity and complete truth-table reasoning |
| Ripple, timing and carry boundaries | Sections 5–6; problems 6–10, 67, 79 | Adjacent full-adder ports, exact carry sequence, independent max-arrival derivations |
| CLA and ordered prefix composition | Sections 7–10; problems 11–18, 68 | Interval-labeled prefix graph with connected boundary ports; associativity proof and order counterexample |
| Carry-select, skip and increment | Sections 11–12; problems 19–22 | Duplicated high-block datapath and real selection port; bypass and increment proofs |
| Borrow, add/subtract and semantic flags | Sections 13–18; problems 23–40, 64, 69, 72, 76, 80 | Complemented ripple, original NAND topology, significance comparison trace and overflow counterexamples |
| BCD | Section 19; problems 41–45, 77 | Two-adder/threshold schematic; both initial-carry and correction-carry contrast models |
| Carry-save and multiplication | Sections 20–22; problems 46–55, 73–75 | Independent equal-weight columns, shifted partial-product matrix and signed Booth row accumulation |
| Division | Section 23; problems 56–59 | Per-prefix long-division table with trial, quotient decision and invariant |
| ALU, multiword state and HDL widths | Sections 24–25; problems 60–66 | Width-explicit SystemVerilog, complete limb calculations, status-register scope and representation counterexamples |

Companion models appear in worked solutions where a changing circuit state or weighted layout aids understanding. A model's title and qualification state its sample parameters when they differ from the general problem; its drawing is not falsely presented as a trace of a different operand instance. Pure range proofs and algebraic derivations use native mathematical notation and explicit counterexamples rather than decorative animation.

## Browser and geometry checks

All fifteen distinct saved models and seventy-one stored checkpoints passed real SVG glyph-bound and label-padding checks in Edge. Forty-six embedded players were mounted across the lesson and worked solutions. All core fonts loaded: Source Sans 3, Newsreader, STIX Two Math and JetBrains Mono. SVG variable indices use separate subscript spans. The visual inspection found and corrected two wire/explanation crossings in the NAND and BCD figures and insufficient cell padding in the multiplier table.

Play/pause, restart, previous-step and checkpoint controls, reduced motion, printable checkpoint traces, eight editable operation samples and six invalid-input preservation cases passed. The chapter and library links work in the weekly plan. A 390-pixel viewport produced no page overflow; wide circuit details remain available through local scrolling and zoom. The new chapter does not modify any of the forty-seven preceding chapter bodies, whose saved SHA-256 hashes were all retained.

## Verified limits

This is exact logical dependency instruction, not analog gate simulation, transient hazard analysis, physical timing signoff or compiled/synthesized HDL verification. Architectural and numerical explanations are deep within the stated chapter boundary; sequential controllers and floating-point standards are outside it. The source audit reports a bounded accessible pool and four genuinely read written courses; it does not claim exhaustive discovery of every worldwide course. Neither a finite audit nor a textbook can guarantee success on every unseen examination question.

## Evidence and reproduction

The source audit links precise original course texts and reading scopes. Local evidence includes the download/reading manifests, `mathematics.json`, `browser.json`, the prior-library retention snapshot and rendered circuit screenshots. The reproducible preparation, rendering, exact-integer verification and browser-review tools are saved with this chapter's source. The two archive question answers are independently derived after checking the original PDF pages; they are not represented as official answer keys.
