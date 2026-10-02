# Quality audit — asymptotic notation and growth comparison

Date: 2026-09-30. Status: completed **review draft**, pending the student's explicit approval. The chapter is not promoted to `ready`.

- **Boundary:** formal one-variable and explicitly domain-qualified multivariable asymptotic comparison. Detailed loop counts and recurrence solutions remain in their scheduled chapters. Archived Iranian master's and doctoral exam booklets were not used.
- **Sources:** four directly read written course texts from MIT, Stanford, CMU, and Princeton, with exact PDF pages and complementary strengths recorded in `a_asym-source-audit.md`. Other candidate courses were screened within the documented boundary, not represented as reviewed.
- **Coverage:** O, Ω, Θ, o, ω, ∼; quantifier witnesses and negation; ratio classifications and oscillatory counterexamples; logarithm, polynomial, exponential, factorial, and variable-exponent comparisons; algebraic rules and their assumptions; rounding, cancellation, inversion, composition, finite crossovers, and two-parameter domains. Eighteen independent worked problems and a twenty-item high-yield sheet map these cases to solutions.
- **Mathematics:** proof assumptions and counterexamples were reviewed individually. Separate finite arithmetic checks passed the explicit polynomial witnesses for 10,000 sizes, rounding inequalities for 10,000 sizes, the factorial-product bound for 99 sizes, and the worked crossover examples. These checks support the calculations but do not replace the general proofs in the lesson.
- **Rendering:** the shared STIX Two Math renderer styles inline and displayed notation and SVG labels. `check_site_en.py` passed for every published and draft English chapter with no missing local link or unstyled detected mathematical character. Edge mobile QA passed at 390 px with zero horizontal overflow, and the print PDF contained 16 nonblank A4 pages, no replacement glyphs, and embedded STIX Two Math. The mobile first viewport and a print page were visually inspected.
- **Uncertainty:** the source survey is bounded, and no finite audit can prove global course optimality or guarantee every unseen exam question. The draft should be corrected if the student identifies an unclear derivation, missing in-scope case, or rendering defect.


## Final existing-library revision — 2026-10-02

The full authored manuscripts, every worked answer, final rules, and diagram context were reread during the sixteen-chapter revision. Findings: Corrected signed residual in asymptotic equivalence under the nonnegative little-oh convention. All identified findings were corrected before rebuilding. The rebuilt chapter passed the recorded finite checks, desktop/mobile geometry, font loading, and print-style diagram-width checks. This is evidence of the performed review, not a universal correctness guarantee or a new full reading of every source course. See `LIBRARY_FINAL_REVIEW.en.md` and `library-review.json`.
