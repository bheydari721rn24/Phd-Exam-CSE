# Discrete random variables: delivery and quality audit

## Deliverable and approval boundary

Only `s_discrete`, the Week 3 chapter *Discrete Random Variables and Common Distributions*, is delivered as a complete English review draft. The student explicitly approved `s_descriptive` before this chapter began. No following chapter has started; the next chapter requires explicit approval.

The chapter contains 26 lesson sections, 80 independently authored or reconstructed course-inspired worked problems, three authentic examination adaptations, a complete synthesis, 80 fully stated final examination rules, 37 distinct subject-specific models with 208 stored checkpoints, and eight editable laboratory modes. Thirty-three worked questions contain matching visual models; the comparison problem on replacement also includes a second model. Mounted instances are not counted as distinct models.

## Coverage and depth

| Chapter scope | Derivations and conceptual checks | Problems and diagrams |
|---|---|---|
| Measurements and atom laws | Measurability, fiber partitions, nonuniform weights, normalization, parameter positivity, countable concentration versus closure | Problems 1–10; weighted mapping and empirical-law contrasts |
| CDF and endpoints | Monotonicity, endpoint limits, right continuity, left limits, jump recovery, four interval contracts, real bounds on integer support | Problems 11–20; jump endpoints and exact interval membership |
| Inverse selection and transformations | Generalized inverse versus digital half-open sampling; all supported preimages; negative affine order; zero-scale case | Problems 17–25 and 71–76; inverse pointer, square, affine, cyclic and quadratic fiber diagrams |
| Independence and binary counts | Same marginals versus same variables; mutual versus pairwise independence; binomial sequence proof, tails, ratios, modes, thinning, dynamic recurrence | Problems 24–40 and 74–80; exact count rows, unequal trials and shared-regime mixture |
| Without-replacement sampling | Both capacity bounds, subset proof, Vandermonde normalization, ordered histories, observed-state update and depletion recurrence | Problems 41–50; marked/unmarked pools and independent sequential propagation |
| Waiting and stopping | Two geometric conventions, real-threshold CDF, memorylessness and characterization, varying hazards, forced terminal success, cap versus truncation | Problems 51–64; survival prefixes, censored terminal mass and r-th-success slots |
| Poisson counts | Exponential normalization, window units, recurrence, modes, zero truncation, finite prefix tail, rare-event pointwise limit | Problems 65–70; recurrence and finite-binomial versus limit comparison |
| Conditional and combined laws | Positive denominator, likelihood reweighting, joint-product condition, weighted convolution, maxima/minima and conditional ties | Problems 69 and 73–80; joint-grid fibers, nested maximum classes and family-size posterior |
| Computational reasoning | Exact rational dynamic code, induction proof, arithmetic and storage cost, bit-cost qualification, underflow and rounding | Section 20 and final rules; independent implementation comparisons |

Expectation is introduced only as a boundary bridge where a proper law can have an infinite first moment. General expectation, covariance, continuous laws, full joint theory, generating-function theory and approximation error bounds have their own scheduled units. Named-law probabilities are taught here; their moments return in the later scheduled chapters.

## Sources and authentic questions

Four core written courses from four universities were actually reviewed: Oxford, MIT, UC Berkeley and Stanford. Harvard contributes a bounded additional review of three exercise families and their solutions. The source audit records the seven-candidate pool, ranking rationale, definitions reconciled, retrieval failures and scopes. A course index or syllabus does not count as a read lecture.

Original PDF pages were visually rechecked for MSc CE 1405 Q35 and PhD CS 1404 Q68–69, preserving the printed options. Answers are independently derived. The n=3 model attached to the symbolic Q68 is explicitly a specialization, not a proof for all n.

## Independent mathematical verification

Seventy named exact checks use rational arithmetic and independent finite outcome enumeration. They include PMF reconstruction, real endpoint events, colliding transformations, maximum fibers, weighted convolution, reliability tails, parity, unequal trials, a shared latent regime, two-stage eligibility, support-constrained urns, observed composition, geometric and capped probabilities, forced last-success events, conditional allocations and the three authentic answers. The symbolic authentic count formula is additionally checked for n=2 through 8.

The actual JavaScript generators were compared with separate reference enumerations in 616 groups. Full binary sequences establish reference binomial and unequal-trial laws. Uniform subsets establish without-replacement laws, and a separately implemented sequential depletion generator agrees across every population, marked count and sample size through population eight. Checks include empty and degenerate experiments. General proofs in the text remain necessary; finite enumeration does not prove every symbolic statement.

All 80 original solutions and 80 rules were read in the final semantic review. The question-30 convolution initially had a differently parameterized visualization; its actual inputs were corrected to match the worked problem. Additional exact diagrams were added for affine reversal, indicators, conditional urn composition, negative-binomial stopping, count capping and quadratic transformations. Displayed decimals are rounded; underlying laboratory arithmetic uses double precision, separately compared with rational reference examples.

## Typography, geometry and controls

The real chapter was rendered in Edge with opened solutions. Formulae use native MathML with structured fractions, sums and subscripts/superscripts, and STIX Two Math separate from Source Sans 3 prose, Newsreader headings and JetBrains Mono code. Font loading succeeds; no unresolved TeX delimiter, Persian line, underlined link or invisible math block remains in the chapter.

Every mounted stored model checkpoint is checked for real rendered text overlap and clipping. Plot coordinates retain actual numerical meaning: PMF bars use a common probability scale, CDF jump endpoints distinguish included values from left limits, uniform cell lengths are probabilities, and joint-grid cells carry their own product masses. Mapping connectors terminate at the drawn box boundaries. Success/failure pools are color-coded and explained in words, not by color alone. Infinite-law prefixes explicitly disclose omitted tails without renormalizing them.

Actual controls are checked for play, pause/resume, previous, seek, restart, reduced motion and explanatory print checkpoints. All eight editable modes return independently checked results. Six invalid-input cases preserve the preceding valid model. A 390-pixel viewport has no page-level horizontal overflow. Runtime errors are absent. Screenshots of mapping, CDF, transformation, urn, stopping, maximum, title and mobile layout were inspected for legibility and mathematical placement. Finite screenshots cannot certify every possible user-entered layout.

## Prior library and evidence

All 39 preceding chapter HTML files retain their opening SHA-256 values and all 2,428 preceding complete problem bodies. The resulting library has 40 chapter pages and 2,511 complete problems. Only previous approval metadata, the current chapter, evidence and delivery state are updated. Synced project sources remain read-only.

Detailed machine-readable evidence is retained in `research/s_discrete-evidence/reading.json`, `mathematics.json`, `models.json`, `browser.json`, `prior-library.json` and `lesson-and-retention.json`. The public-facing source and quality audits are available beside the chapter. GitHub mirroring and private Site deployment are recorded after verification in the separate publication receipt. No literal 100-percent correctness or universal examination-performance guarantee is claimed.
