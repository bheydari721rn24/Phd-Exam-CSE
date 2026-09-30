# Quality audit — a_model English review draft

Date: 2026-09-30. Manuscript: `research/a_model.en.md`; study page: `dist/chapters/a_model.html`. The student approved `d_induction` before this chapter began. The archived Iranian entrance-exam booklets remain deferred.

## Scope and source gate

- The boundary is computation models and input size. Asymptotic notation, loop-operation counting, hashing, sorting, and recurrences remain later chapters. The boundary prevents a superficial opening chapter from swallowing topics requiring their own proof and exercise banks.
- Five relevant **written** course texts from MIT, CMU, Princeton, Stanford, and Berkeley were read in the bounded portions listed in `a_model-source-audit.md`. The candidate pool also inspected ETH's index and handwritten PDF, which is **not** counted among the five because this review did not extract its text. The course register in `dist/course-audit-week1.en.json` names the actual reviewed documents and their limits.
- In-text pedagogical ideas and problems are independently worded. Problems 9–11 state their university reasoning-type provenance; the source list at the end gives exact direct links. No question from the deferred Iranian examination archive appears.

## Coverage matrix

| In-scope reasoning pattern | Full teaching | Worked problem or counterexample | Review rules |
| --- | --- | --- | --- |
| Problem relation, instance, deterministic algorithm, implementation, measurement | §2 | 1, 14 | 1–2, 19–20 |
| Binary length and exact power-of-two boundary | §3.1 | 2, 10 | 3, 14 |
| Element count versus bit size; variable-width arrays and framing | §§3.1–3.2 | 3, 5 | 4–5 |
| Graph/list/matrix representation | §3.2 | 5–6 | 5–6 |
| Address width versus storing the length | §4.1 | 4 | 7 |
| Static array access versus initialization and interface | §4.2 | 7 | 10–11 |
| Word arithmetic, overflow, multiword exact product | §§4.1, 4.3 | 8–9 | 8–9 |
| Comparison model, direct addressing, preprocessing, space | §5 | 11, 16 | 12–13, 23 |
| Binary versus unary encoding and pseudo-polynomial tables | §§3.4, 6 | 10, 15 | 14–15, 24 |
| Input-access adversary and output-writing lower bounds | §7 | 12–13 | 16–18 |
| Worst/best/average resource definitions | §4.1 | 14 | 19–21 |

## Mathematical checks

- Checked the distinct address and value thresholds: indexing `0..n-1` needs `(n-1).bit_length()` bits for `n≥2`, whereas representing `n` needs `n.bit_length()` bits. At `n=256`, the answers are eight and nine.
- Checked binary lengths for zero and the boundaries `1, 15, 16, 17, 2^m−1, 2^m` for `m=1..30` against Python integer bit length. Zero's one-bit encoding is stated as a convention.
- Checked Problem 3's `ceil(log2(n^3))` fixed-width claim for integer `n=2..512` using integer bit-length arithmetic.
- Checked the matrix arithmetic in Problem 5 (`30·40=1200`, `1200·16=19200`, `19200/64=300`) and the graph record counts in Problem 6.
- Checked the exact output bit length in Problem 9: `2^(n(w-1))` has `n(w-1)+1` bits for `2≤w≤32` and `1≤n≤200`.
- Checked the decision-tree capacities in Problem 16: `2^6=64<65≤128=2^7` and `3^3=27<65≤81=3^4`. The lower bound is explicitly not presented as an optimal construction.
- All input/output lower bounds state their access or output-contract hypotheses. The chapter avoids extrapolating a model-specific bound to a stronger model.

## Presentation checks

- `research/check_site_en.py` passes: local links resolve; all study-facing files are English; chapter statuses match the approval gate; raw fallback-prone Unicode indices are absent outside protected diagrams/MathML.
- Edge at 390 CSS pixels reports document width and scroll width both 390; all three self-hosted fonts loaded; formula blocks show zero internal overflow. The larger diagram scrolls within its own card rather than shrinking mathematical labels or widening the page.
- A4 browser print generated 15 pages; all pages extracted nonblank text; zero Unicode replacement characters. The 16th solved problem, final review, and full references appear in the print output.

## Delivery decision

No identified mathematical error, broken study link, or in-scope matrix gap remained after these checks. The chapter is a **review draft**, not a guaranteed solution to every unseen examination item. It remains at `draft` in `dist/lessons.json`; `research/chapter-gate.json` will be set to `awaiting_user_approval` after delivery. No later chapter begins until the student explicitly approves this one.
