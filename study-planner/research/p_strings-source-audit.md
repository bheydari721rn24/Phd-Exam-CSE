# Strings and terminators: source selection and reconciliation

## Selection scope

Review date: 8 October 2026. The candidate pool is finite and chapter-specific. Four university courses with accessible written teaching were selected; Stanford adds a reference checklist. This does not establish that every university course worldwide has been inspected. Selection follows complementary coverage, scientific precision after reconciliation, accessible text, and useful exercise patterns, rather than a numerical world-ranking claim.

| Candidate | Actual reading | Decision and contribution |
| --- | --- | --- |
| Harvard CS50x 2025, David J. Malan | Week 2 notes, arrays through string length/case conversion/arguments; Week 4 string, pointer, comparison and copy sections | Core: gradual representation and aliasing explanations. Translate the CS50 string typedef into actual C17 types. |
| Cambridge Programming in C 2017–18, Neel Krishnaswami | All extracted text of Lectures 2 and 3, 19 and 25 slides respectively | Core: pointer views, parameters, traversal, reversal and substring-search exercise patterns. |
| MIT 6.087, January IAP 2010, Daniel Weller and Sharat Chikkerur | Lecture 5 review page 5 and relevant lifetime/array/pointer/string pages 16–26 | Core: lifetime and string-library families. Historical architecture numbers and old interfaces need explicit qualifications. |
| Princeton COS 217, Fall 2026 | Complete extracted text of the 32-page Pointers, Arrays, and Strings slide deck | Core: arrays versus pointers, parameter size, string-library composition and a halving-index debugging pattern. The slide marker is not independently verified individual authorship. |
| Stanford CS107 | Complete accessible C reference sheet | Supplementary: checklist for copying, concatenation, spans, search, conversion and input. Restricted table and question wording are not reproduced. Archived Lecture 6 PDF text could not be reliably fetched, so it is not claimed as read. |
| CMU 15-122 | String-buffer assignment PDF metadata found; repeated body retrieval failed | Not selected as a read course. A catalog or PDF title does not establish content review. |
| Princeton Spring 2024 short strings handout | Search metadata found; direct access returned 403 | Not claimed as read. The accessible Fall 2026 teaching deck is selected instead. |

## Scientific reconciliation

The lesson uses C17 consistently. Harvard's convenience typedef is not a built-in string type. Its scalar case examples need explicit encoding and classification-domain assumptions. Cambridge's reversal pattern involving a signed index derived from `strlen(s)-1` is replaced by a `size_t` half-length loop that does not evaluate a negative index for empty input. The substring interface uses unambiguous text and pattern names.

MIT's old `strlen` slide uses `int`; the C library returns `size_t`. Its brief `strncpy` description is expanded into copying plus zero padding and possible missing termination. Historical memory-size examples are not portable constants. `gets` is excluded because C11 removed it. Neither MIT's “array implemented using a pointer” shorthand nor an address diagram changes the distinction between an array object and a pointer variable.

Princeton's deck contains introductory and historical simplifications: C99 and C17 allow loop-local declarations; automatic arrays can have variable length where supported; an array is not merely an address; and forming an out-of-range pointer is not valid just because it is not immediately dereferenced. Java-like `int[]` spellings in comparison slides are not valid C declarations. Eight-byte pointer examples remain explicitly implementation-specific. The final exercise's pointer-size check, null-check ordering, uninitialized output index and signed narrowing motivate an independently written problem, not copied erroneous code.

Stanford's sheet is a compact aid rather than a complete semantics specification. The lesson supplies `strncpy` padding and exact append-capacity requirements. `strdup` and `strndup` are not assumed ISO C17. The primary WG14 N1570 string sections were read to reconcile zero-count pointer validity, overlap, unsigned comparison, bounded termination and search return conventions. N1570 is accurately identified as the C11 draft, not a C17 publication.

## Coverage and problem construction

Twenty-eight teaching sections cover representation, literals/escapes, object bounds, suffixes, invariant-based scanning, copying, bounded copying, concatenation, arithmetic overflow, aliasing/lifetime, overlapping moves, comparison, spans, matching, reversal, compaction, tokens, stream input, formatting, character classes, conversion, Unicode distinctions, string tables, arguments, dynamic capacity, exact cost and combinatorial counting.

The 80 original or independently reconstructed problems address those contracts, exact sums, invariant proofs, counterexamples and combined mutations. Cambridge reversal/lowercase/search patterns, Harvard alias/copy patterns, MIT lifetime patterns and Princeton debugging patterns receive explicitly transformed independent tasks. This is not a claim to reproduce all exercises from all courses. One authentic MSc CS 1405 Q123 counting bridge is rechecked against original PDF page 26; it is already present in a previous chapter and is not counted as a new unique archive question. It concerns abstract strings, not C sentinel bytes. No original C-string-specific archive question was verified in this pass: a full local PDF text search found no usable `strlen`/copy/compare identifiers in the image-heavy archive, and that is not proof that none exists.

## Honest boundaries

Advanced pattern matching, Unicode grapheme algorithms, wide strings, locale collation, full dynamic-array interfaces and allocator design are separate topics. Testing supports the stated algorithms and examples under explicit contracts, not a literal guarantee of universal completeness or future examination performance. Full lecture decks and restricted reference tables are linked rather than republished. Source wording is not copied into the independently authored instruction.

Exact source links and instructor/course credits appear in the chapter's final References section.
