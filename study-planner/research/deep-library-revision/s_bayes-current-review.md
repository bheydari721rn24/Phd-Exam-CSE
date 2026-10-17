# Bayes: individual review of the complete edition

Edition: 17 October 2026. State: revised and checked author-review draft. Earlier student approval applies to the earlier edition; it does not silently approve this revision.

## What was actually reviewed

The entire teaching manuscript, all 65 problem statements and answers, and all 80 final examination decisions were read. Sixty-three original/course-derived answers now have separately written constructions, intermediate equations, mathematical justification and checks, followed by the retained valid result and interpretation. The two authentic examination revisits have additional derivations. The answer bank contains about 10,935 words, excluding the full teaching chapter and final decisions. Length is recorded for accountability, not used as a correctness score.

The original and authentic questions are distinguished. The chapter does not represent every source exercise as reproduced, and does not classify invented questions as actual examinations. Source-specific exercise coverage and deliberate exclusions remain in the original source audit.

## Repaired assumptions and conceptual distinctions

1. **SB33, individual versus family sampling.** The statement now specifies exact finite population proportions with a family count divisible by six. The minimum admissible population has three size-one, two size-two and one size-three families, supplying ten children and probabilities 3/10, 2/5 and 3/10. The lesson and final decision now distinguish fixed proportions or limiting population laws from ratios involving small random populations. A separately enumerated two-family counterexample prevents replacing an expected ratio by a ratio of expectations.
2. **SB36, equal weights.** The statement now specifies one common heavy weight and one distinct common light weight. Thus exactly HH and LL satisfy the observation; their pair counts are one and twenty-eight.
3. **SB29, stopping versus count.** The exact TTH stopping event and the one-success count event have different probabilities. Their posteriors happen to agree in this fixed independent-trial model because of a common factor. The explanation now makes the coincidence explicit.
4. **SB54, observation versus intervention.** Two explicit structural models have the same observational joint distribution and different intervention results. The answer therefore demonstrates non-identification rather than merely warning about causality.
5. **SB55, numerical versus mathematical certainty.** Shifted log weights prevent underflow; a result rounded to one remains an approximation to a strictly interior posterior. The complementary probability can be retained separately.

## Sources: actual scope and current access

The original bounded comparison evaluated nine course families across seven universities. Four primary written courses are MIT Mathematics for Computer Science, Stanford CS109, CMU Introduction to Probability for Computing and Oxford SC7 Bayes Methods. Berkeley STAT 134 is an additional contribution. Different MIT or Oxford courses are not counted as different universities. This is a documented accessible candidate pool, not a claim to have enumerated every course worldwide.

On 17 October, MIT Lecture 19 pages 4–5 were freshly read and its downloaded bytes matched the previous SHA256. Stanford's complete Bayes instructional body was freshly read and both stored reader downloads matched their earlier fingerprints. Oxford PDF pages 10–15 were freshly read, covering prior interpretation, conditional loss, prediction, model uncertainty and odds; its download matched the earlier SHA256. CMU Theorems 2.18–2.21 and their proofs on PDF pages 11–13 were freshly read through the official PDF browser. Local CMU download failed with a connection refusal: no new local file or hash verification is claimed for that source. The earlier full reading ranges remain historical evidence and are not relabeled as all freshly read today. Berkeley is supplementary historical reading, not a fifth freshly re-read course in this revision.

## Authentic questions

The retained original page images were opened and read again: CS doctoral 1404 Q69, PDF page 15, and CE master's 1405 Q35, PDF page 8. The family question explicitly permits the zero-child case; the coin question retosses only first-round heads. The independent results remain option 4, respectively 1/4 and 27/128. These are intentional prerequisite revisits, not newly discovered distinct questions. The historical original-PDF fingerprints remain in the acquisition ledger; this review does not pretend a missing temporary original was freshly rehashed.

## Figures, mathematics and browser evidence

Thirty-one new question-specific vector figures use the actual priors, likelihoods, joint masses, posterior tables, exact finite populations, decision risks or posterior density in their question. The three-source, detector, duplicate-versus-independent and fixed-coin walkthroughs match the relevant question inputs. Unrelated generic question animations were removed. The ten distinct lesson mechanisms remain available; all selectable options were exercised, including options that are not initially selected.

The actual browser checked 13 players, 15 scene placements and 76 finite checkpoints, with next, previous, seek and restart controls. The exact posterior laboratory checked positive, independent, copied, impossible, zero-report and twenty-report inputs. All 65 solutions open for printing. Fonts loaded successfully, no links were underlined, no page overflow occurred at widths 390, 768 and 1360, and no script errors were recorded. New figure text was checked for bounding-box overflow, overlap and card padding, and representative screenshots were inspected.

The independent numerical oracle performs 6,586 exact checks; additional symbolic and statement-bound checks cover sensitivity derivatives, finite populations, coin weights, decision thresholds, structural-model distinctions, serialized scene values, and all 1,089 native MathML expressions. The current evidence is in `s_bayes-mathematics.json` and `s_bayes-evidence/browser.json` beside this record. General conceptual proofs are author reviewed; finite enumerations are not a machine proof of every possible input.

## Remaining limits

The notes are designed for deep mathematical and conceptual examination preparation. Neither course selection nor finite checks establish literal universal completeness, absolute correctness, or guaranteed answers to every unseen question. Student understanding and timed performance still need to be established after teaching. The library-wide review remains incomplete; this record covers only this chapter.

## References

- MIT — Zachary Abel, Ben Chapman, Erik Demaine — [6.1200J/18.062J, Lecture 19](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/mit6_1200j_s24_lec19.pdf), Spring 2024.
- Stanford University — Chris Piech — [CS109, Bayes' Theorem](https://chrispiech.github.io/probabilityForComputerScientists/en/part1/bayes_theorem/) and [Law of Total Probability](https://chrispiech.github.io/probabilityForComputerScientists/en/part1/law_total/).
- Carnegie Mellon University — Mor Harchol-Balter — [Introduction to Probability for Computing, Chapter 2](https://www.cs.cmu.edu/~harchol/Probability/chapters/chpt2.pdf), Theorems 2.18–2.21.
- University of Oxford — Geoff K. Nicholls — [SC7 Bayes Methods, MT2025](https://www.stats.ox.ac.uk/~nicholls/BayesMethods/BLnotes25MT.pdf), opening inference and decision sections.
- University of California, Berkeley — David Aldous — [STAT 134, Lecture 3](https://www.stat.berkeley.edu/~aldous/134/lecture3.pdf), supplementary historical reading.
