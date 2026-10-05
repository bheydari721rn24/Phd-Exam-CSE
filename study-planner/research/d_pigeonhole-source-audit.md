# Pigeonhole chapter: source selection and actual reading

## Bounded comparison

The search located nine written-course candidates across eight universities. Five primary courses from four universities were selected after comparison of the relevant written sections; a sixth Cornell text was read as a complementary theorem check. This is a documented comparison of accessible materials, not a claim to have evaluated every course worldwide. Merely finding a course URL is not counted as reading it.

| Candidate | Relevant written scope actually inspected | Selection and reason |
|---|---|---|
| MIT 6.042J, Spring 2015; Lehman, Leighton and Meyer | §14.8, physical pages 581–590 before §14.9; selected problems on pages 618–619 | Primary: finite maps, subset images, digit constructions, card channels, geometric and rectangle exercises |
| MIT 18.310, Fall 2013; Michel Goemans | September 2 pigeonhole lecture, all five pages | Primary: a different proof of monotone labels and the adaptive one-lie transcript argument |
| Oxford Discrete Mathematics, Michaelmas 2010; Andrew D. Ker | §6.5, physical pages 87–89; Exercises 6.7–6.8 on page 92 and solutions on page 94 | Primary: odd-part chains, modular images, compression and exact geometric endpoint handling |
| Stanford CS103, Winter 2026; Sean Szumlanski | Lecture 11, physical pages 12–74 and 83–135; zero-one multiple exercise on page 139 | Primary: degree restrictions, strict means, incidence saturation and the two Ramsey branches |
| Toronto MAT344, Summer 2019; Balazs Elek | Lecture 7 §4, physical pages 1–2, before §5 | Primary: an independently checked monotone proof with a different label convention and odd-core example |
| Cornell CS2800; Pass and Tseng | §4.5, physical page 77, Lemma 4.28 and Example 4.29 | Reviewed complementary: the integer-ceiling statement and its contradiction proof; too short to supply the advanced chapter alone |
| Cambridge CST 2016/17 Discrete Mathematics | Screened relevant basic principle near physical page 85 and generalized capacity statement near page 330 | Candidate only: relevant statements support discovery, but the whole course was not read or incorporated as a primary source |
| CMU 21-301, Fall 2018; Michael Tait | Searched the official text for the principle; screened multipartite graph use near page 37 and arithmetic-progression use near page 52 | Candidate only: no dedicated foundational treatment selected; not counted as a reviewed chapter course |
| Harvard freshman seminar, Fall 2023; Lauren Williams | Course catalogue entry scheduling pigeonhole and double counting on September 20 | Discovery only: no complete accessible lesson text was read there, so it is not counted as a reviewed source |

Official candidate links: [Cambridge notes](https://www.cl.cam.ac.uk/teaching/1617/DiscMath/DiscMathProofsNumbersSetsNotes.pdf), [CMU notes](https://www.math.cmu.edu/users/math/mtait/301/Notes.pdf), [Harvard course page](https://people.math.harvard.edu/~williams/Proofs-Fall23.html). The six adopted official references, instructors, dates and reading scopes are listed in the chapter and in the machine-readable course evidence.

## Reading and synthesis ledger

MIT 6.042J supplies the finite-function theorem, the equal-subset image comparison, the distinction between collision and decoding, and exercises. Its digit-sum exercise is recomputed with both inclusive endpoints. Its square exercise refers to interior points and strict distance; the chapter's closed-domain grid claims instead use a weak diameter bound. The card count is a necessary deck bound, whereas the standard-deck anchor construction is actually sufficient. The rectangle exercise's coarse repeated-row count is sharpened here by a proved pair-color certificate bound and an actual avoiding construction.

MIT 18.310 was read through the official web PDF text reader after a native fetch connection error. The whole five-page lecture was inspected. The one-lie transcript count is used only as a necessary packing bound; the lesson does not assert that its integer upper bound is achieved. An adaptive lie changes later questions and therefore need not produce a Hamming-distance-one word relative to a fixed truthful transcript. The chapter explicitly separates this from nonadaptive code geometry.

Oxford was read at the exact §6.5 and exercise boundaries. The nonempty equal-sum conclusion requires positive inputs after common-index cancellation. Modular product cancellation requires invertible common factors. The odd-prime square-image count does not cover prime two, which the chapter solves directly. Composite modulus eight provides an explicit failed extension. Geometric sufficiency is separated from minimum thresholds; the triangle has an actual four-point lower-bound witness.

Stanford's original cached slides were read over the stated ranges, including a second read of pages 66–73 where an earlier tool output was truncated. Graph and attendance diagrams on physical pages 102 and 133 were visually inspected. Instructor attribution was checked against the archived course page: Sean Szumlanski. Announcements and the informal topology sampler are excluded. The Ramsey star is retained as only the first proof step; the two triangle branches are proved separately.

Toronto's original §4 was read before its Fibonacci §5. Its monotone proof combines an increasing-starting label with a decreasing-ending label, which is valid when interpreted consistently. The synthesized chapter uses the equally valid pair of ending labels and proves their distinctness directly. Unrelated material and its initial-value conventions were not imported. Course attribution was checked against the official course page: Balazs Elek.

Cornell's complete relevant short section was read as a complementary sanity check, including the 800/366 birthday example. Its proof reinforces the weak ceiling inequality. It is not represented as a long advanced source.

## Source integrity and access

Original cached PDFs have SHA-256 records in the reviewed-course evidence: MIT textbook, Stanford slides and Toronto notes. MIT 18.310, Oxford and Cornell were read through the official web PDF text reader where native downloads failed or timed out; no local checksum or full-course offline reading is claimed for those documents. All course reconstructions use independently written statements and solutions rather than reproducing full exercise collections.

## Authentic archive boundary

The pinned archive commit is `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. Both chosen questions were visually checked against their original PDF pages. MSc CS 1405 question 116 on physical page 25 is a newly checked finite-search bridge: odd three-digit passwords over digits 1–9 give 405 candidates and 13.5 hours in the worst case. It is not mislabeled as a direct collision question. PhD CS 1404 question 25 on physical page 7 is a reviewed parity-counting question already present in the archive catalogue: 200 four-element subsets contain an opposite-parity pair. Its solution distinguishes counting successful subsets from universally forcing a pair. Answers are independent derivations, not official answer keys. Original PDFs remain private reference artifacts; only question adaptations, provenance and checksums are included here.

## Coverage boundary

The chapter covers finite assignments, generalized occupancy, strict averages, inventory feasibility, specified targets, heavy-bin bounds, collision pairs and higher tuples, residues and prefixes, decimal constructions, prime images, subset cancellation, complementary pairs, multiplicative cores, geometric partitions and approximation, monotone subsequences, degree labels, small Ramsey and rectangle theorems, truthful and one-lie information bounds, compression and constructive card decoding. Matching theory, general coding theory, advanced Ramsey numbers, arbitrary packing optima and infinite cardinal arithmetic remain separate topics. No assertion of universal future-examination success is made.
