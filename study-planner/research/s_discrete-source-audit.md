# Discrete random variables: source selection and synthesis audit

## Selection boundary

Seven located university candidates were compared for this chapter. Four accessible written courses were selected as the core synthesis: Oxford, MIT, UC Berkeley and Stanford. Harvard supplies an additional, explicitly bounded exercise review. CMU's syllabus and ETH's course index were screened but are not counted as reviewed lecture sources. This is a documented search pool, not a claim to have examined every course in existence.

Selection prioritized precise mathematical definitions and conditions; relevance to the chapter's event-to-law boundary; useful derivations, counterexamples and computing applications; and accessible written evidence that could actually be inspected. Prestige alone or the presence of a course link did not qualify a source. The ranking below concerns this chapter, not the overall quality of a university.

| Priority | Course | Actual reading and contribution | Limitation / decision |
|---|---|---|---|
| 1, core | Oxford Prelims Probability, James Martin, Michaelmas 2019 | PDF pages 18–21, Chapter 2 definitions through Exercise 2.5: random-variable maps, concentrated support, classical-law contracts and normalization | Expectation begins at the boundary; its full treatment belongs to the next chapter |
| 2, core | MIT 18.05, Jeremy Orloff and Jonathan Bloom, Spring 2022 | Entire Class 4 reading, combined PDF pages 28–39: PMF/CDF, Bernoulli/binomial, zero-based geometric, finite uniform and weighted sums | MIT's failures-before-success convention is translated explicitly, not mixed with total-trial waiting |
| 3, core | UC Berkeley CS70, Rao and Walrand, Spring 2016, Note 16 in the Fall archive | PDF pages 1–5: fixed maps, many-to-one fibers, permutation examples and binomial packet models | The expectation remainder was not incorporated as if it belonged to this chapter; guessed unavailable URLs were excluded |
| 4, core | Stanford CS109, Chris Piech and teaching team, Winter 2025, Lecture 6 | All 124 textual slides; progressive duplicates recognized and mathematical figures checked: counts, binomial applications, sequence grouping and series-winning contracts | Empirical frequencies do not establish a population law; stopped-series probability is distinguished from stopping-time distribution |
| Additional reviewed material | Harvard Statistics 110, Joe Blitzstein, Strategic Practice 4, Fall 2011 | Section 1 problems 1–3 and corresponding page 4 solutions via the web PDF reader: same law versus equality, cyclic labels and positive-based geometric CDF | Direct PDF acquisition returned 403. Only this bounded web scope is counted; no complete downloaded-file review or hash is claimed |
| Screened, excluded from the four-source requirement | CMU 36-225, Jing Lei, Fall 2012 syllabus | Four-page syllabus establishes course context but does not supply the needed chapter-level lesson | A syllabus is not evidence of reading the lectures |
| Screened, excluded from the four-source requirement | ETH Zurich 401-2604-00L, Fadoua Balabdaoui, Spring 2019 course index | Located official probability/statistics course index | An index is not a reviewed English lecture text; no inaccessible lecture content was invented |

## Actual primary written materials

1. James Martin. *Prelims Probability*. University of Oxford, Michaelmas 2019, version of 20 October 2019. [Official lecture notes](https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553).
2. Jeremy Orloff and Jonathan Bloom. *18.05 Introduction to Probability and Statistics*. MIT, Spring 2022. [Combined probability readings](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf), Class 4.
3. Rao and Walrand. *CS70 Discrete Mathematics and Probability Theory*, Note 16. UC Berkeley, Spring 2016 material in the Fall archive. [Written note](https://fa16.eecs70.org/static/notes/n16.pdf).
4. Chris Piech and teaching team. *CS109 Probability for Computer Scientists*, Lecture 6. Stanford, Winter 2025. [Written lecture slides](https://web.stanford.edu/class/archive/cs/cs109/cs109.1254/lectures/6-RandomVariables/6-RandomVariables.pdf).
5. Joe Blitzstein. *Statistics 110*, Strategic Practice 4. Harvard, Fall 2011. [Practice and solutions](https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_4.pdf), bounded scope as above.
6. Jing Lei. *36-225 Introduction to Probability Theory*, Fall 2012. CMU. [Screened syllabus](https://stat.cmu.edu/~jinglei/syllabus_f12.pdf).
7. Fadoua Balabdaoui. *Probability and Statistics*, Spring 2019. ETH Zurich. [Screened course index](https://metaphor.ethz.ch/x/2019/fs/401-2604-00L/).

## Reconciled definitions and independent synthesis

The lesson first distinguishes elementary outcomes, fixed measurable maps, value events, formal ranges and positive-mass atoms. This prevents a uniform-label assumption from replacing a supplied nonuniform experiment. PMFs are derived by partitioning fibers, while CDF properties are proved from probability-measure continuity rather than a memorized graph shape.

Geometric laws use both conventions explicitly: MIT's failures before first success begin at zero; Oxford/Harvard's total trials through success begin at one. Negative-binomial offsets use r rather than one. The lesson separately treats capping, truncation and a no-success code, whose terminal masses differ.

Stanford's fixed-sequence grouping is reconciled with stopped series by pre-generating an imagined full horizon. This proves a series-winning event without asserting that the actual stopping index has a binomial law. Independent unequal trials and a shared hidden parameter receive distinct constructions. A per-trial marginal probability cannot replace mutual independence.

Hypergeometric support is derived from both pool capacities, and exact subset enumeration is checked against sequential depletion. Convolution adds joint masses along fibers; extrema use nested conjunctions. Poisson normalization, parameter units, adjacent ratios and a fixed-count rare-event limit are derived with explicit finite-versus-limit qualifications. Infinite prefixes always retain their omitted tails.

The prose, diagrams, algorithms and problem wording are independently authored. Reconstructed course families are labelled, use their own data or extensions, and do not claim to reproduce every copyrighted exercise. All 80 original/reconstructed problems and the 80 final rules were read during the final semantic audit.

## Original examination evidence

Three English adaptations use original PDFs from the project archive at commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. The actual page images were rendered and visually inspected in this turn:

| Archive item | PDF page | Pattern | Independently derived option |
|---|---|---|---|
| MSc Computer Engineering 1405, Q35 | 8 | Eligibility followed by a second success; binomial thinning | 4, probability 27/128 |
| PhD Computer Science 1404, Q68 | 15 | At most one success among n independent indicators with success probability 1/n | 1, symbolic formula and a labelled n=3 specialization |
| PhD Computer Science 1404, Q69 | 15 | Countable family-size prior reweighted by the no-boy likelihood | 4, conditional positive-size probability 1/4 |

Printed option order is preserved. These are independent answers, not official keys. Source paths, immutable source commit, translation scope, page numbers and SHA-256 values are retained in the authentic-question records. Scanned archive pages were not represented as an exhaustive classification of every examination.

## Evidence and remaining uncertainty

`research/s_discrete-evidence/acquisition.json` records successful and failed retrievals; `reading.json` records bounded scopes and four core PDF hashes. The four downloaded core files and the two original examination PDFs were hash-checked again before delivery. Third-party PDF caches remain outside the repository; synced project sources remain untouched.

The selected sources support the declared chapter, but neither a finite bibliography nor a test suite establishes literal universal correctness or success on every unseen examination question. Full expectation theory, joint distributions, generating functions, covariance, continuous distributions and quantitative approximation bounds belong to later scheduled chapters.
