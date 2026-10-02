# p_types quality audit

Date: 2026-10-02. Status: approved English chapter. Student approval on 2026-10-02 permits ready status and work on p_flow; the validation evidence below was completed before that approval.

## Deliverable

- Full lesson, problem bank, and final review are separate editable English manuscripts, rendered into dist/chapters/p_types.html.
- Approximately 13,600 whitespace-separated manuscript words, including code/markup; this is an approximate size measure, not a claimed prose-only word count.
- Twelve sections; 36 numbered problems with complete tasks and explanatory solutions; fifty complete-sentence examination rules; a seven-step unfamiliar-expression procedure; failure/repair map.
- Two original SVG teaching diagrams; an interactive typed conversion/division laboratory with five modes, accessible labels, live output and explicit model limits.
- Four selected core written courses from four universities plus a genuinely reviewed fifth-university supplement. Selection, exact read depth, rejected candidates, correction ledger and exercise-pattern inventory are in p_types-source-audit.md.
- C17 is the primary language; 32-bit example integer assumptions, LP64/LLP64 differences, binary64 example assumptions and Java/Python comparisons are explicitly separated.

## Scientific and instructional checks

- The conversion tree was checked against WG14 N1570 §§6.3.1.1–6.3.1.8. Promotion, operand common type, expression result type and final storage conversion are kept distinct.
- Literal lists, character constants, sizeof result/operand evaluation, increment/assignment/comma sequencing, conditionals, signed overflow and shifts were checked against the named draft clauses. It is correctly labelled as a public C11 committee draft for relevant rules retained in C17.
- Source errors in signed range, int-width guarantee, signed representation, signed narrowing, printf type matching, sizeof, Python version and macro repeated evaluation were resolved in original instruction rather than copied.
- Quotient/remainder, residue uniqueness, ceiling quotient, unsigned wrap detection, signed addition/subtraction thresholds and finite-binary rational termination have explicit proofs and domain assumptions.
- The worked solutions were reread for grouping, intermediate type and range, state changes, result type and behavior classification. Undefined examples have no invented numeric outputs.
- Independent verify_types_semantics.py passed **453,032** exact/model and manuscript assertions. This includes exhaustive eight-bit signed addition/subtraction guard checks, valid division/remainder checks, all pairs of byte-residue arithmetic, ceiling quotients and nonnegative-remainder correction. Specific 32-bit boundary answers and binary64 examples were checked separately.
- Finite checks supplement the general proofs; they are not a proof of all C executions, all source coverage or unseen-question performance.

## Browser, typography, and print

- check_site_en.py passed for seventeen local HTML pages: local links, English-only assets, approved previous chapters, new draft URL, mathematical symbols and semantic indices. No Arabic-script characters or replacement characters were found in the manuscripts.
- All mathematical displays and inline mathematical runs use the separate STIX Two Math styling; two native MathML fractions were inspected for legibility. The typography audit finds no unstyled mathematical runs by its documented detector, with more than 270 styled runs.
- A locally bundled JetBrains Mono regular WOFF2 and its official SIL OFL license provide the new chapter's consistent code typography. Newsreader headings and Source Sans 3 prose remain in the established presentation.
- Headless Edge at 390 CSS pixels: page width 390, document width 390, mathematical display overflow zero, fonts loaded. Code blocks and wide diagram/table containers can scroll internally; they do not widen the page.
- Eleven laboratory states passed: byte promotion/storage, invalid byte inputs, signed C versus Python quotient, zero-divisor rejection, cast timing, mixed unsigned comparison, short-circuit zero-divisor skip, minimum/-1 rejection, and valid negative quotient. No arbitrary code evaluation is used.
- Laboratory state is reset to its documented initial byte-storage example before print capture, avoiding a misleading QA-mutated printout.
- Browser A4 print output has **39 pages**. Mobile code, MathML fraction, final-review and laboratory screenshots were inspected. Print pages 2, 8, 13, 29 and 34 were rendered and visually inspected for source table continuity, conversion diagram, equations, worked problems and the final review. No visible clipping or corrupted glyphs appeared in the inspected areas.
- Print font resources include embedded JetBrains Mono and STIX Two Math, with browser math fallback resources. Computed browser math and code families match the declared separate fonts; no assertion that every glyph uses only one PDF font resource is made.
- The chapter-library card has its complete title, verified in the browser. The application now derives missing older card titles from the existing schedule instead of displaying empty labels.
- node --check passed for p_types-lab.js and app.en.js. git diff --check passed; line-ending notices do not indicate whitespace errors.

## Actual limitations

- No C compiler was available in the inspected Windows PATH or Ubuntu WSL environment; Docker's local daemon was unavailable. **C code was not compiled or executed.** The audit uses specification reasoning and independent numeric models; it does not pretend these are compiler tests. Undefined snippets must never be empirically run to invent an answer.
- The selected materials were reviewed for this boundary. Whole-course transcription, a complete global source inventory and every literal question in every offering are not claimed. The exercise-pattern map distinguishes represented patterns from deferred applications.
- The public specification draft is not the published ISO C17 text. Other language versions, implementation-dependent choices, floating modes and unknown future questions remain explicit scope limits.
- Archived Iranian master's/doctoral papers were not inspected; their joint study remains deferred to the final month.
- The temporary print PDF, source PDFs/HTML and screenshots remain outside the deploy archive and GitHub mirror. The published deliverable is the fully formatted chapter and its laboratory.

## Approval handoff

The student approved l_matrices on 2026-10-02; it is promoted to ready. p_types was delivered as a draft with its completed audit. The subsequent explicit approval on 2026-10-02 promoted it to ready and authorized p_flow.
