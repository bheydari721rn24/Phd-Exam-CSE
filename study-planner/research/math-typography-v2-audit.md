# Library-wide mathematical typography audit

Date: 2026-09-30. The student approved `a_model` and asked for a distinct professional mathematical face in every existing chapter, including inline symbols and indices. This revision covers `d_logic`, `d_sets`, `d_proof`, `d_induction`, and `a_model`.

## Implementation

The shared rendering pass in `math_typography.py` identifies mathematical runs in lesson text, wraps them in `math-inline`, and converts Unicode small indices to semantic subscript or superscript markup. It leaves code, SVG, MathML, scripts, styles, and existing mathematical markup alone. Displayed formulas, inline formulas, and diagram labels use the self-hosted STIX Two Math font; Source Sans 3 remains the prose face. A unicode-range fallback routes any remaining mathematical characters to the math font. SVG subscript labels in the logic dependency diagram use explicit baseline shifts.

The renderer uses a bounded pattern grammar, not mathematical parsing. Its purpose is typography; it does not establish correctness of the formulas or a literal guarantee about every possible text form. Formula semantics and instructional claims were not revised in this pass.

## Verification

| Chapter | Styled inline runs | Mobile width / scroll | Formula overflow | A4 pages | Blank pages | Replacement characters |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| `d_logic` | 467 | 390 / 390 px | 0 | 22 | 0 | 0 |
| `d_sets` | 1,013 | 390 / 390 px | 0 | 20 | 0 | 0 |
| `d_proof` | 715 | 390 / 390 px | 0 | 19 | 0 | 0 |
| `d_induction` | 691 | 390 / 390 px | 0 | 20 | 0 | 0 |
| `a_model` | 242 | 390 / 390 px | 0 | 15 | 0 | 0 |

Each rendered page was compared with the preceding committed version using extracted HTML text. After normalizing Unicode script glyphs to their semantic digits or letters, text was identical for all five. The site audit found zero unstyled mathematical Unicode symbols in article text and verified the bundled math font assets. All chapter verifiers and the local Edge mobile/print checks passed. The browser loaded the three required font files with HTTP 200 responses. The available screenshot samples for logic, model, and the model diagram were visually inspected.
