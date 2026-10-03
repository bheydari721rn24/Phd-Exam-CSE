# Conditional Probability: Source Selection and Reading Audit

Review date: 3 October 2026. Scope: the event-level conditional probability chapter, not every probability syllabus or every later stochastic-process topic.

## Candidate pool and availability

The candidate pool contains seven university course families. Each was evaluated individually for accessible written material and relevance. Five supplied usable readings. Two acquisition failures are recorded rather than counted as reviewed courses. A global exhaustive search over every university course cannot be established from this bounded pool; the selection below is the strongest complementary set among the candidates actually inspected.

| Course family | Written access | Relevance decision |
| --- | --- | --- |
| MIT 6.041SC; John N. Tsitsiklis | Lecture 2 PDF acquired and reviewed; separate Lecture 3 request failed TLS | Primary: conditional universe, complete-history tree, partition framework. Slides are concise, so CMU supplies detailed proofs and counterexamples. |
| Stanford CS109; Chris Piech | Three complete reader sections acquired and reviewed | Primary: conditional-measure interpretation, complement laws, generalized independence, chain factorization. Explicit denominator qualifications are added in the synthesis. |
| CMU Introduction to Probability for Computing; Mor Harchol-Balter | Chapter 2 PDF acquired | Primary: Sections 2.3–2.6 and the relevant exercise collection give the broadest event-level coverage and the most useful conceptual counterexamples. |
| Berkeley STAT 134; David Aldous | Lecture 2 and 3 PDFs acquired | Primary: observation protocols, unequal selection weights, aggregation, reliability. Source refers to unavailable board work; it is not treated as a reviewed proof. |
| Oxford Part B Applied Probability; Matthias Winkel | Complete PDF acquired; only the stated chapter-relevant range reviewed | Supplementary fifth university: modeling assumptions, density conditioning, null-event boundaries. Most stochastic-process material is outside this chapter. |
| Harvard STAT 110; Joe Blitzstein | Course context screened; the requested strategic practice 2 PDF returned HTTP 403 | Not counted as a reviewed written course. Its reputation does not compensate for inaccessible evidence. |
| Cambridge Probability; Richard Weber | PDF acquisition failed certificate verification | Not counted as a reviewed course. TLS verification was retained. |

## Selection rubric

The rubric uses editorial 0–5 ratings for four distinct criteria: event-level coverage, explicit mathematical assumptions, instructional complementarity, and accessible written verification. These are author judgments, not an objective ranking of university quality.

| Reviewed candidate | Coverage | Assumptions | Complementarity | Written verification | Role |
| --- | --- | --- | --- | --- | --- |
| CMU | 5 | 5 | 5 | 5 | Formal backbone and counterexample/problem structures |
| Stanford | 4 | 3 | 4 | 5 | Conditional paradigm and computing applications |
| MIT | 4 | 4 | 4 | 5 | Concise tree and partition organization |
| Berkeley | 4 | 3 | 5 | 4 | Protocol ambiguity, sampling and aggregation |
| Oxford | 2 | 4 | 4 | 5 | Supplementary boundary material rather than a replacement for elementary coverage |

The four primary courses are selected together for complementary coverage. Oxford is used in addition where its continuous-observation discussion adds a necessary qualification. None is asserted to be individually complete. Harvard and Cambridge receive no numerical content rating because the intended text was not accessible.

## Exact reading ledger

- **MIT:** Lecture 2 PDF pages 1–3 extracted. Pages 1–2 visually inspected to verify the displayed condition, multiplication tree, and partition diagrams. Page 3 is attribution rather than theory.
- **Stanford:** Complete instructional bodies of Conditional Probability, Independence, and Probability of And read after removing menus and scripts. Reviewed the weighted rather than equiprobable interpretation, nested conditioning, complement proof, all-subfamily definition, chain, and parallel network example.
- **CMU:** PDF pages 4–14 read for Sections 2.3–2.6; PDF pages 14–21 read for the exercise inventory. Pages 1–3 concern prior axioms, and page 22 is a footer, not additional reviewed theory. Relevant exercise structures used or adapted: 2.8, 2.9, 2.10, 2.15–2.22, and 2.24(a). Other exercises were screened for overlap or later Bayes/counting coverage; they were not all reproduced.
- **Berkeley:** Lecture 2 pages 1–12 and Lecture 3 pages 1–10 extracted and reviewed. Lecture 2 pages 11–12 and Lecture 3 page 4 visually checked because extracted character encodings were damaged. Numerical examples in the manuscript use separately specified original models instead of trusting garbled digits. Board-only network calculations are unavailable.
- **Oxford:** Title, synopsis, and Lecture 2, Sections 2.1–2.3, PDF pages 15–20 reviewed. PDF page 20 contains a set-letter typo in a displayed independence equality; the synthesis uses the correct event factorization. Smoothness/positivity qualifications are explicit for the density example. General regular conditional probability is outside the proof scope.

The machine acquisition ledger records URLs, byte sizes, SHA-256 fingerprints, and failures. The course files stay in a private temporary research cache; they are not distributed with the Site. The reading status is separate from successful downloading.

## Concept-to-source crosswalk

| Chapter concept | Primary written support | Additional contribution |
| --- | --- | --- |
| Reduced weighted universe and conditional axioms | MIT Lecture 2; Stanford Conditional Probability; CMU Section 2.3 | Original proof of the conditioned probability measure |
| Complete-history multiplication | MIT Lecture 2; Stanford Probability of And; CMU Theorem 2.10 and Exercise 2.9 | Positive-prefix versus positive-final distinction; original XOR counterexample |
| Joint-table feasibility and reversed direction | CMU Sections 2.3–2.6; Stanford Conditional Probability | Original sharp bounds, cell reconstruction, determinant and exact laboratory |
| Sequential counts and eligibility | CMU Exercise 2.10; Berkeley Lecture 2 sampling examples | Original urn derivations; authentic MSc 1405 question 35 |
| Weighted and conditional partitions | MIT Lecture 2; CMU Section 2.5; Berkeley Lecture 2 | Original Simpson model; authentic PhD 1404 question 69 |
| Pairwise/mutual/complement independence | Stanford Independence; CMU Section 2.4 and Exercises 2.15–2.18 | Original triple-only construction and feasible triple-mass interval |
| Conditional independence and hidden types | CMU Section 2.4 and Exercises 2.19–2.21; Stanford Independence | Original two-stratum covariance derivation and selection simulations |
| Reporting protocol | Berkeley Lecture 2 pages 11–12 and Lecture 3 page 4; CMU Exercise 2.22 | Explicit likelihood-weighted sensor and host models |
| Reliability | Stanford parallel-network reading; CMU Section 2.4; Berkeley Lecture 3 pages 5–7 | Original shared-edge proof and explicit five-edge bridge enumeration |
| Continuous conditioning boundary | Oxford Section 2.2 | Original triangle and positive-strip examples with stated interior assumptions |

## Examination provenance and limits

The repository source revision is `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. Four relevant existing translations were rechecked against newly rendered original pages: PhD CS 1404 Q68 and Q69 on PDF page 15; Q70 on page 16; MSc CE 1405 Q35 on page 8. Q70 is a cross-topic independence/counting application, not an explicitly conditional question. PhD Q67 was excluded because the problematic source wording cannot safely be repaired into an authenticated item.

This is a selected examination-pattern review, not a claim to have classified every question in every archive booklet for this chapter. Authentic options retain source numbering. Solutions are independently derived. The remaining 56 questions are original or explicitly attributed adaptations, with qualitative medium/hard labels rather than measured psychometric difficulty.
