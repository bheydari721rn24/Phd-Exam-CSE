# Bayes and base rates: source selection and reading audit

## Selection scope and criteria

Date: 2026-10-04. This is a bounded comparison of nine candidate course families across seven universities, not an assertion that every course worldwide has been enumerated. Four primary courses were selected after chapter-specific reading; a fifth university's course was retained as supplementary. Sources are judged by (1) explicit hypotheses and positive-denominator assumptions, (2) partition and posterior derivations, (3) odds/history and selection coverage, (4) mathematical exercise transfer, and (5) useful advanced depth without importing unrelated methods. Reputation alone does not establish chapter coverage. The source fingerprints and actual reading ranges are in `research/s_bayes-source-downloads.json`; downloaded originals stay in the private temporary cache.

| Candidate | Written material examined or acquisition outcome | Selection judgment |
| --- | --- | --- |
| MIT 6.1200J/18.062J, Abel / Chapman / Demaine | Lecture 19, all PDF pages 1–8 | Primary. Strong discrete derivation, odds and background-information cautions; continuous parameters need another source. |
| Stanford CS109, Chris Piech | Complete total-probability and Bayes reader instructional bodies | Primary. Clear partition normalization and base-rate interpretation; this chapter adds explicit null-stratum and dependence qualifications. |
| CMU Introduction to Probability for Computing, Mor Harchol-Balter | Chapter 2, PDF pages 11–21; Theorems 2.18–2.21 and screened exercise descriptions | Primary. Strong conditional total probability and diverse latent-source/report exercises; no wholesale distribution of source text. |
| Oxford SC7 Bayes Methods, Geoff K. Nicholls | MT25 notes, PDF pages 6–15; foundational density, generative, prior, risk, prediction and odds sections | Primary. Adds decision-theoretic and continuous-depth boundaries. Radiocarbon, Monte Carlo algorithms, Laplace asymptotics and later chapters are not included in the chapter coverage claim. |
| Berkeley STAT 134, David Aldous | Lecture 3, all PDF pages 1–10 | Supplementary fifth university. Particularly useful reporting and fixed-coin prompts. Results marked as board work are independently derived, not claimed to have appeared in the PDF. |
| MIT 6.041SC, John Tsitsiklis | Previously reviewed Lecture 2, pages 1–3, re-screened for relevant partition/Bayes scope | Alternative same-university course. Concise useful slide framework; the selected MIT MCS reading gives richer explicit odds/protocol discussion. This does not count as a second university. |
| Oxford Part B Applied Probability, Matthias Winkel | Previously reviewed PDF pages 15–20, re-screened for conditioning scope | Alternative same-university source. Useful density groundwork, but SC7 more directly addresses posterior inference, prior sensitivity and loss. |
| Harvard STAT 110, Joe Blitzstein | Strategic practice/homework 2 acquisition returned HTTP 403 | Not selected or counted as read. Access failure is not a scientific judgment on the course. |
| Cambridge Probability, Richard Weber | Candidate PDF acquisition failed certificate verification | Not selected or counted as read. TLS verification was not disabled. |

The original Stanford `total_prob` path and Oxford older `BLnotes23.pdf` path returned 404. They were recovered using the current `law_total` reader and `BLnotes25MT.pdf`. These failures and recoveries are retained in the acquisition ledger. No video, audio or transcript availability was assumed from a landing-page link alone.

## How the readings were synchronized

| Chapter content | Primary contribution | Added derivation or qualification |
| --- | --- | --- |
| Partition / total probability | CMU Theorems 2.18–2.19; Stanford total reader | Skip null strata and maintain one conditional background measure; derive countable-family example. |
| Bayes normalization | MIT p4; CMU 2.20–2.21; Stanford Bayes | Separate likelihood weights from evidence scale; positive evidence and common normalization proof. |
| Base rates / natural frequencies | Stanford; MIT p5; CMU Example 2.22 | Independently specified synthetic detector, complete four-cell interpretation, credibility thresholds. |
| Odds / history | MIT p4; Oxford 1.3.7 | Exact repeated-update rule, duplicate-report counterexample and pairwise/full-posterior distinction. |
| Latent-state prediction | CMU Exercise 2.17; Berkeley p10; Oxford 1.3.4 | Fixed-versus-redrawn state, explicit posterior predictive mixture and independent hidden-coin calculation. |
| Protocol / selection | Berkeley p4; CMU 2.12, 2.22, 2.23 | Explicit host tie-breaking, child sampling likelihood and family-size bias. |
| Prior sensitivity / decisions | Oxford 1.3.1, 1.3.3, 1.3.5 | Derive sharp binary thresholds, risk ties, abstention and distinction between inference and action. |
| Continuous bridge | Oxford 1.2.1 | Elementary uniform-rate posterior and integer beta-integral proof rather than unexplained named-distribution substitution. |

Five written university courses contribute to the synthesis; four are primary. The manuscript and every solution are independently written. Original diagrams and exact checkpoint simulations illustrate the chapter's proofs rather than reproduce university figures.

## Chapter-relevant exercise screening and bank coverage

CMU Chapter 2 exercise descriptions were screened individually on pages 14–21. Relevant families: 2.1 / 2.3 / 2.4 (inverse observation); 2.7 (conditioning direction); 2.11–2.14 (latent classes, report mechanisms, repeated checks); 2.17 (shared origin and predictive probability); 2.22 / 2.25 (informed-host selection); 2.23 (equal-weight pair selection); 2.27 (hidden die); 2.28 (history-dependent packets). Their structures are covered through the detector, sequential, latent-source, host, pair-selection and full-history problems. Some receive a changed-parameter original analogue rather than a copied exercise. Oxford Exercise 1.2 supplies the independently expanded rejection-sampling proof. Berkeley's p10 hidden-coin prompt receives an independently completed calculation. Stanford's examples motivate original base-rate and factory exercises with independently specified values.

CMU exercises 2.2 / 2.5 / 2.6 / 2.9 / 2.10 primarily revisit counting/event algebra; 2.8 / 2.15 / 2.16 / 2.18–2.21 primarily revisit independence proofs already taught in the prerequisite. CMU 2.24 concerns winning streaks and conditional arrangement counts; 2.26 requires a carefully specified money-value prior and is deferred to later expectation/modeling instruction. They are not silently counted as solved here. Oxford Exercise 1.3 and later posterior computation exercises require Monte Carlo/order-statistic prerequisites and are outside this elementary Bayes chapter. Screening an exercise and solving it are distinct states.

The delivered bank contains 65 entries: two authentic archive items and 63 independently written original/course-derived problems. All have complete derivations. Exact reused booklet questions are labeled intentional revisits, while posterior extensions receive new original identities. Author-assessed difficulty does not imply empirical psychometric calibration. No claim is made that every exercise from every source has been reproduced.

## Authentic examination control

Original PDF pages were rendered and visually read in this run. CS doctoral 1404 Q69, page 15, includes the zero-child case and gives prior mass `2^(-n-1)`; answer option 4 is independently derived as one quarter. CE master's 1405 Q35, page 8, states that only first-round heads are retossed; answer option 4 is independently derived as `27/128`. The original booklets are fingerprinted against the pinned archive revision `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. No official answer key is claimed. The original Iranian-language scans remain private; public instruction, translations and provenance are English.

## Limits of the evidence

Accessible written material and explicit scope determine this selection. Inaccessible courses are not deemed inferior. The source audit is a defensible chapter-specific comparison, not proof of a globally optimal course set. Exact finite/rational checks and editorial derivation review support correctness within recorded domains. They cannot guarantee every unseen examination outcome or literal universal completeness.
