# Source comparison: Descriptive Statistics and Exploratory Data Analysis

## Selection method and bounded candidate pool

Seven universities were screened through located accessible written course material or an index: MIT, Stanford, UC Berkeley, Carnegie Mellon, Harvard, Oxford and ETH Zurich. Selection considered relevance to this chapter, precise definitions, usable derivations, edge cases, graphical conventions and complementary coverage. Rank means suitability for this chapter within this located pool. It is not a global university ranking or a claim that every course in existence was found and read.

The selected core comprises four courses from four universities. A fifth university's assigned teaching text is included because its treatment of empirical distributions and Q–Q comparisons adds useful detail. Course acquisition, a page view and actual reading are distinguished in [the reading ledger](s_descriptive-reading.json). The student-facing chapter contains direct primary-source references and bounded reading scopes.

| Priority | University and course | Reviewed scope | Selection reason and qualification |
|---|---|---|---|
| 1 | UC Berkeley, SticiGui, Philip B. Stark | Histograms: frequency tables through percentiles; Location and Spread: location/loss, spread, affine maps, Markov and Chebyshev; full textual Computing Correlation chapter | Strongest explicit finite-list mathematical contracts, histogram area and inequalities. Its lower nearest-rank median is separated from midpoint median rather than silently blended. |
| 2 | MIT, 15.075J / ESD.07J, Statistical Thinking and Data Analysis, Cynthia Rudin; Allison Chang and Dimitrios Bisias | Chapter 4, PDF pages 1–7 | Compact coherent coverage of corrected variance, group mixtures, correlation and time summaries. Concise lecture formulas are expanded with original proofs and worked problems. |
| 3 | Stanford, STATS60 / STATS160 / PSYCH10, Michael Howes and Tselil Schramm, Spring 2026 | Relevant full textual teaching bodies of Lectures 5, 7 and 8 | Clear center/variability/robustness teaching, visual interpretation and counterexamples. Descriptive denominator n is retained as a separate convention; finite quantile percentages and strict-tail wording are independently corrected. |
| 4 | Carnegie Mellon, 36-309, Experimental Design and Analysis, Howard Seltman | Chapter 4, PDF pages 1–24 | Complementary boxplot and Q–Q conventions, measurement types and outlier interpretation. The chapter distinguishes whiskers from fences and fourth-moment kurtosis from a vague peakedness description. |
| 5, added complement | Harvard, Introduction to Data Science, Rafael Irizarry | Sections 12.1–12.8 and 12.9.1–12.9.2 | Strengthens ECDF, distribution visualization, stratification, normal-reference quantile plots and outlier effects. Later exercise and robust-MAD sections were not represented as fully reviewed. |
| Historical comparison; not core | Oxford, IAUL / Department of Statistics, Descriptive Statistics for Research, Hilary 2002; individual author attribution unconfirmed | Lecture 1, PDF pages 11–22 | Contains relevant descriptive topics, but audited numerical and mathematical defects prevent selection as one of the four core courses. |
| Index only; not selected | ETH Zurich, Mathematical Statistics, autumn 2022 course index | Located index screened | Inferential emphasis and the located index provide no additional fully reviewed descriptive unit. No full ETH lecture review is claimed. |

The guessed Stanford Lecture 6 URL was unavailable (HTTP 404) and contributes no claimed reading. A table of contents supplies discovery links; it is not counted as a reviewed chapter. Acquisition file hashes are retained in the ledger, while downloaded third-party files remain outside the repository.

## Synchronization rather than incompatible formula blending

| Topic | Reconciled treatment in this chapter |
|---|---|
| Variance | Define $M_2$ first. Describe $v=M_2/n$ separately from $s^2=M_2/(n-1)$. Prove the correction under iid finite-variance assumptions; no normality assumption is added. |
| Quantiles | Nearest rank, midpoint median, type 7 and median-of-halves receive distinct definitions. Negative affine transformations expose the lower-versus-upper middle-record issue. |
| Histogram | Use actual unequal widths, disjoint endpoint contracts and mass as area. Within-bin interpolation is explicitly an assumption. |
| Boxplot | Compute type-7 quartiles, strict fences and observed whiskers. A value on the fence is retained. |
| Shape | Define moment skewness and kurtosis; state the software-convention caveat. Zero third moment does not imply symmetry, and normality is not inferred from standardization. |
| Correlation | Preserve record pairing; prove the Cauchy–Schwarz bound, degenerate-column exclusion and scaling invariance. Distinguish empirical association from population independence. |
| Pooling and streaming | Derive within/between decomposition and Welford's recurrence rather than averaging unrelated variance estimates. |
| Time and Q–Q plots | State plotting probabilities, startup denominators, initial EWMA state and the absence of future observations from a valid one-step forecast. |

## Defects found in comparison material

Oxford PDF page 17 prints house/car coefficients of variation as 160 and 16 where the surrounding units and stated spreads require 1/60 and 1/6. Its moment-skewness and kurtosis displayed sums lack the averaging factors described in the text. Page 18 describes excess with an opposite sign from the usual kurtosis-minus-three convention. Page 19 gives inconsistent scores to the two naming orientations of a concordant pair; it also overstates the straight-line interpretation of perfect rank association. These statements are not propagated. Named-file image evidence is retained outside the repository and the exact source hash is in the ledger.

The Stanford quantile wording is qualified for ties and finite ranks. The CMU kurtosis description is replaced by the exact fourth-moment definition. Harvard's empirical threshold discussion is expressed consistently with $F_n(t)=\#\{x_i\le t\}/n$. These corrections were derived independently rather than settled by a vote among courses.

## Problems and original examination evidence

Eighty problems use original data, independent wording and complete solutions, including course-inspired concepts. They are not a verbatim compilation of copyrighted course exercise banks. Two authentic archive questions are checked English adaptations: PhD CS 1405 Q58, PDF page 15, and MS CE 1405 Q36, PDF page 8. Their source commit, hashes, original option order and independent answer status are stored in `s_descriptive-authentic.json`.

The archive's PDFs are predominantly image-based. The direct keyword scan did not read those images and is not evidence of archive-wide absence or exhaustive topic classification. Only inspected pages support the two included questions. The authentic questions are labelled population-moment and normal-standardization bridges; neither is misrepresented as a raw-data quantile question. No official answer key is claimed.

## Limits and next review

The lesson is independently authored from the reviewed concepts and derivations. It does not reproduce all source wording or promise to include every exercise from every course. Inferential estimation, tests and full regression theory belong to their scheduled chapters. This chapter remains a review draft, and finite checks cannot establish literal universal correctness or guarantee performance on every unseen examination question.
