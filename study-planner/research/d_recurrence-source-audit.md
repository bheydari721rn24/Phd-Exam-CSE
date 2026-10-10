# Discrete recurrence relations: source selection and reading audit

## Scope and selection contract

This is a documented comparison of accessible written candidates for exact discrete sequence recurrences. It is not an exhaustive enumeration of every university course worldwide. Selection considers mathematical derivation, coverage of initial conditions and multiplicity, forcing, combinatorial models, and problem quality. A course catalogue, search snippet, or topic list does not count as a genuinely reviewed teaching text. Four core courses from four universities were read in the scopes below. Broader fields covered in earlier algorithm chapters and the next generating-function chapter are kept distinct.

## Candidate comparison

| Candidate | Written evidence actually inspected | Chapter fit and decision |
| --- | --- | --- |
| MIT 6.042J, Spring 2015; Lehman, Leighton, Meyer textbook | Chapter 21, PDF 876–891, all sixteen pages | Core: unrolling, constant-coefficient methods, particular solutions, and verification. |
| Oxford Discrete Mathematics, Michaelmas 2010; Andrew D. Ker | Chapter 5, web PDF text covering printed 57–70, PDF 67–80; the intervening printed page 69 contains no additional problem text | Core: sequence domains, counting recurrences, characteristic methods, mixed forcing, practice and boundary cases. |
| Cornell CS2800, Spring 2017 hosted reader; Rafael Pass and Wei-Lung Dustin Tseng | PDF 31–35, inductive definitions through Theorems 2.20 and 2.21 and their proofs | Core: initial-data counterexample, distinct-root proof, repeated-root recipe, Fibonacci derivation. |
| Berkeley Math 55, Summer 2017; Ritvik Ramkumar | Entire two-page Thursday and two-page Friday Week 5 worksheets; Thursday page 2 rendered and visually inspected | Core: independently reconstructed counting, higher-order, and forced-recurrence exercises. Friday informs the boundary-aware generating-function bridge. |
| Stanford Math 108 | Entire two-page final-review document | Screened: a useful boundary checklist, but a review list without actual derivations does not meet the core teaching-text requirement. The PDF's course year and instructor were not independently established. |
| CMU 15-251, Spring 2012; Lecture 9, Adam Blank | Official course page and accessible written slide text, including early domino prompt and subsequent algorithm-cost sections | Screened: most inspected content concerns algorithmic divide-and-conquer costs already taught; it is weaker for this chapter's exact constant-lag proof and forcing coverage. The colored-domino prompt is not used without its defining figure. |
| Cambridge Discrete Mathematics | Course-scope screening only | Not counted as read: the inspected scope emphasized foundational proof and sets, without a confirmed recurrence treatment meeting this chapter's requirements. |
| Harvard CS20 | Catalogue/search screening only | Not counted as read: an accessible substantive recurrence text was not acquired in this search. |
| ETH Zurich | Search screening only | Not counted as read: no specific recurrence teaching text was acquired for this chapter. |

The last three are acquisition boundaries, not evidence that these universities lack strong courses. Additional sources should be added when a concrete gap requires them. There is no assertion that exactly four sources will always suffice for later chapters.

## Source-specific contributions and reconciliation

MIT supplies the first-order expansion and forcing workflow. The chapter distinguishes the textbook's staircase initial convention from the zero-one Fibonacci convention. Its use of “linear” in contrasting a halving-index cost equation is interpreted narrowly as constant-lag applicability; a halving-index equation can still be linear in the unknown function. The new lesson proves its own claims and does not reproduce the textbook's narrative.

Oxford supplies a broader discrete modeling boundary and worked-method comparison. Text extraction reports Bell values ending in thirteen, although the stated finite recurrence gives fifteen. Practice answer 5.1(ii) reports an increment that produces two instead of four at the first transition; with index zero equal to one, the correct increment for consecutive squares is twice the index plus three. Practice answer 5.8 reports a formula inconsistent with the stated values at indices one and two; the independently fitted result is two to the index minus one. These are text-level discrepancies, not claims about visually inspected source glyphs. The lesson independently checks every imported mathematical pattern.

Cornell supplies the distinct-root proof and an example showing why one missing base case invalidates induction. Its reader does include the repeated-root recipe; the new chapter adds a full independence proof using finite differences, rather than falsely claiming the source omits multiplicity. Reader authors are distinguished from unverified course lecturers. The general nonzero-root recipe is qualified by a separate zero-root prefix treatment.

Berkeley supplies exercise patterns requiring a model before a formula. A rendered page confirmed exponential forcing and its negative particular solution. Ordered payment tokens remain distinguishable; forbidden ternary symbols require explicit states; the averaging recurrence's starting indices remain one and two. Problems here are original or reconstructed, with fresh derivations and labeled provenance, rather than a wholesale copied worksheet.

## Reading access and evidence limits

The MIT PDF was read from an existing local official-source cache. The Berkeley PDFs were downloaded successfully and have recorded SHA-256 hashes. Cornell and Oxford native downloads timed out, while their official PDFs remained accessible through web text; the actual relevant passages were read there. No local hash is invented for unavailable downloads. Stanford's two-page checklist and CMU's scoped slides do not replace any of the four core readings.

Lecture videos and transcripts without verified text are not counted. The independent exact calculations, proof checks, original exam page rereads, models, and browser evidence are reported separately in the scientific and visual audit.

## Official source links

- [MIT 6.042J textbook](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf)
- [Oxford Discrete Mathematics notes](https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf)
- [Cornell CS2800 reader](https://www.cs.cornell.edu/courses/cs2800/2017sp/handouts/pass_tseng_discmath.pdf)
- [Berkeley Math 55 course](https://math.berkeley.edu/~ritvik/math55.html)
- [Berkeley Thursday worksheet](https://math.berkeley.edu/~ritvik/Worksheet_5Th.pdf)
- [Berkeley Friday worksheet](https://math.berkeley.edu/~ritvik/Worksheet_5F.pdf)
- [Stanford Math 108 review](https://web.stanford.edu/class/math108/files/final_review.pdf)
- [CMU 15-251 course](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15251-s12/www/)
- [CMU Lecture 9](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15251-s12/www/lectures/lecture09/lecture09.pdf)
