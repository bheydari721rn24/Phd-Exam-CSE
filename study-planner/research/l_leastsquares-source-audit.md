# Least squares: bounded course comparison and actual reading

Edition: 17 October 2026. Four primary written courses from four universities were selected for complementary coverage. This is a documented accessible comparison, not an enumeration of every course worldwide or a guarantee of a globally best set.

## Selection criteria

Preference was given to explicit existence and rank hypotheses, a proof linking projection to the normal equations, actual computable examples, QR and numerical distinctions, and useful estimation extensions. Reputation or a recent date alone is not a scientific quality score. A written syllabus is not counted as a read mathematical lecture. Previously read ranges are distinguished from fresh reading.

| Candidate course | What was actually inspected | Decision and limitation |
| --- | --- | --- |
| MIT 18.06SC, Gilbert Strang, Fall 2011 | All three Session 2.3 teaching pages freshly read; fourth page is license material | Primary. Concrete line fit, residual directions and Gram invertibility. Its use of distance in the data plot is translated explicitly as vertical error rather than perpendicular regression. |
| Stanford EE263, Stephen Boyd, Autumn 2007–08 | Lecture 5 teaching pages 1–14 freshly returned and read; pages 15–23 were read for the preceding projection chapter and remain historical contextual reading | Primary. Thin/full QR, residual split and left-inverse estimation. Statistical BLUE wording is qualified with zero-mean spherical-covariance assumptions and a full covariance proof. |
| Berkeley Math 54, Alexander Paulin, Spring 2018 | All four original scanned Least-Squares Problems pages downloaded, rendered and actually viewed | Primary. Independent normal-equation and triangular examples. The handwritten coefficient-space and observation-space notation is translated consistently; short answers receive full calculations. |
| ETH Zurich Linear Algebra for Computer Scientists, Afonso S. Bandeira and Robert Weismantel, Part II 2025 | Section 6.1, PDF/native pages 12–15 freshly read; QR consequences on page 23 and minimum-norm development on pages 24–25 freshly read | Primary. General-rank existence, centered line fits, polynomial features, QR and distinct row-rank versus column-rank inverse formulas. Its quadratic-feature prompt is developed into a proof and a repeated-input problem. |
| Oxford A7 Numerical Analysis, 2026–27 | Official written course outline and list of numerical-linear-algebra lectures screened | Candidate only. Its outline is directly relevant, but no mathematical lecture notes were read in this comparison; it is not counted as a fifth reviewed course. |
| ETH Numerical Methods for CSE, Ralf Hiptmair, 2020 | Official document search result and scope screened | Candidate only. Promising computational depth; the large text was not read in this chapter run and is not counted as another reviewed text or university. |
| CMU 21-241 and Harvard Math 55a | Historical inner-product reading from the earlier orthogonality audit considered for prerequisite overlap | Supporting historical candidates. Not freshly read least-squares lectures and not advertised as additional primary courses. |

The Berkeley PDF had no machine-extracted text and the research browser's screenshot requests failed. A direct verified HTTPS download was therefore rendered locally, and every original page was inspected. The source is retained as a local reference, not redistributed as a copied course packet. The other primary readings were read through the official PDF research browser; no local download fingerprint is invented for those browser readings.

## Synchronization and chapter coverage

| Scope | Source contribution | Independently developed teaching and exercises |
| --- | --- | --- |
| Existence, normal equations, uniqueness | MIT; Berkeley; ETH 6.1 | Algebraic necessity/sufficiency, nullspace solution set, zero design, inverse data construction and dimension obstructions |
| Vertical line fitting and centered coordinates | MIT worked example; ETH line example | Complete residual/error certificate, repeated inputs, through-origin contrast, added-feature gain and parameter changes |
| QR and stable computation | Stanford pages 8–10; Berkeley pages 3–4; ETH page 23 | Triangular solutions, Householder construction, sign and transformed-data obligations, condition-number warning |
| Rank deficiency and minimum norm | ETH pages 24–25; preceding projection foundations | Full geometric construction, common incorrect inverse formulas, coordinate-dependent norm convention |
| Weighted models | Stanford estimation context plus explicit independent extension | Positive definite whitening, off-diagonal metric, semidefinite and negative-weight counterexamples |
| Constrained and regularized models | Projection/prerequisite foundations plus independent extension | Feasible nullspace reduction, common-kernel uniqueness, ridge stationarity, unpenalized intercept and ridge limits |
| Statistical estimation | Stanford pages 11–14 | Explicit covariance assumptions, full BLUE difference proof, GLS, bias–variance comparison, degrees of freedom and non-Gaussian dependence counterexample |

The advanced extensions are independently derived; they are not falsely attributed as all appearing in every selected course. Detailed nonlinear least squares, robust-loss algorithms, SVD algorithms, asymptotic inference and Bayesian regression are outside this chapter. Their mention supplies a boundary, not a claim to teach them fully here.

## Exercise accounting

Problem 1 reconstructs the MIT worked line fit. Problems 2 and 3 independently reconstruct both Berkeley numerical examples, including the complete triangular solution. Problem 15 addresses the ETH quadratic-feature prompt and proves why raw constant/square columns cannot be perpendicular in a full-rank real design. The remaining 46 entries are original mathematical/conceptual problems, rather than copied source exercises. Every entry has a complete solution. The bank does not claim to reproduce every exercise in every course.

One authentic doctoral question is explicitly revisited: PhD CS 1404 Q31, original PDF page 8. The retained original page image was opened and read again; option order and contraction direction were checked. Its previous archive fingerprint remains historical evidence. It is a projection prerequisite and an exact least-squares certificate, not a newly discovered direct regression question. No unavailable official answer key is claimed.

## References

- MIT — Gilbert Strang — [18.06SC Session 2.3 summary](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/198bde3a6536b62989b6cc09495575c1_MIT18_06SCF11_Ses2.3sum.pdf).
- Stanford University — Stephen Boyd — [EE263 Lecture 5](https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/ls.pdf).
- University of California, Berkeley — Alexander Paulin — [Math 54 Least-Squares Problems](https://math.berkeley.edu/~apaulin/Least-Squares%20Problems.pdf).
- ETH Zurich — Afonso S. Bandeira, Robert Weismantel — [Linear Algebra Part II](https://ti.inf.ethz.ch/ew/courses/LA25/notes_part_II.pdf).
- University of Oxford — [A7 Numerical Analysis, official course materials outline](https://courses.maths.ox.ac.uk/course/section.php?id=13417), screened candidate only.
- Iranian examination archive — [pinned original booklets](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams), PhD CS 1404 Q31.
