# Divide-and-Conquer Mathematical and Visual Quality Audit

Date: 2026-10-02. Topic: a_divide. Status: delivered English review draft awaiting explicit student approval.

## Source evidence

Eight universities form the documented screened pool. MIT, Stanford, UC Berkeley and CMU are the four principal genuinely reviewed written courses. ETH is a genuinely reviewed fifth-university supplement for maximum subarrays. Princeton, Oxford and Cornell are screened candidates, not silently counted as read courses. Actual page scopes and source disagreements are in a_divide-source-audit.md; PDF fingerprints are in a_divide-source-downloads.json.

Original-source page images inspected: CMU page 3 for packing; Berkeley pages 3 and 25 for integer shifts and FFT block structure; ETH page 10 for the crossing decomposition and empty-interval policy. PDFs were used as read-only references, and no course deck was copied into the served chapter.

## Teaching and coverage

The chapter contains 14869 source-word tokens by the documented simple lexical count, including code identifiers and review headings; this is not a printed page-count claim. There are 48 independently authored worked problems, 88 full-sentence revision rules, five original vector diagrams, twelve native MathML displays, seven executable teaching-code blocks and an exact bounded summary laboratory. Lesson, problems and review counts: {"lesson": 6860, "-problems": 5305, "-review": 2704}.

The main lesson develops contracts, recursion, work/span/space, lower bound, stable merge and strict inversions, nonempty maximum subarrays and associative summaries, closest pair with tied coordinates and dense-ID membership, signed/odd-width Karatsuba, all four ordered Strassen block proofs, roots of unity, radix-two FFT, inverse orthogonality, norm scaling, zero padding and modular-recovery conditions.

Source issues addressed include unstable merge ties, exhausted runs, queue-run stability, nonempty versus empty subarrays, half-specific geometric separation, odd-width shifts, carry-bit qualifications, noncommuting blocks, unnormalized Fourier norms, numerical precision and spurious reduced-majority candidates. No national entrance-exam archive was opened or classified.

## Independent executable checks

Actual manuscript code is extracted and executed, rather than rewritten inside its verifier. Optimized results are compared against distinct direct methods. Actual served JavaScript is executed through Node and compared to Python interval enumeration.

{
  "mergeInversionAndLowerBoundArrays": 97656,
  "summaryArrays": 1089,
  "actualJavaScriptSplitWitnessChecks": 4923,
  "signedOddWidthKaratsubaProducts": 67073,
  "noncommutingMatrixBlockChecks": 300,
  "closestPairSetsAndMultisets": 1827,
  "floatingFFTDirectAndInverseChecks": 180,
  "floatingFFTMaxObservedError": 4.287648548987259e-13,
  "exactModularConvolutions": 729,
  "limits": "Finite independent checks supplement the stated proofs; they do not establish universal completeness, a floating-point error guarantee or performance on unseen questions."
}

The geometric packing, inductive correctness and algebraic identities remain mathematical proofs. These finite counts check implementation behavior and boundary cases; they are not a proof of arbitrary instances or all possible exam questions.

## Browser and visual evidence

The chapter was rendered locally in Edge at desktop width 1280 and mobile width 390. All five SVGs have zero out-of-view labels and zero label overlaps. The mobile document fits width 390 without page overflow, and native formula blocks have no overflow. Print-media width 794 confirms diagram fit; this does not claim paginated PDF inspection.

Screenshots of every diagram, all twelve MathML displays, the mobile laboratory, code, rules and opening were inspected. Mathematics, HTML indices and SVG index spans use STIX Two Math. Code uses JetBrains Mono; prose and headings use Source Sans 3 and Newsreader. Links have no underline. SVG indices use explicitly positioned spans rather than relying on small Unicode glyph fallback.

The four laboratory presets verify crossing, all-negative, left-only and tied answers. Invalid splits, malformed integer strings and out-of-bound values are rejected and do not present an old result as newly verified.

The site-wide English checker passes local links, chapter status, session data and index typography. The previously approved recurrence chapter verifier also passes after promotion.

## Limits and handoff

The manuscript is complete for its declared boundary, with no known failing mathematical or visual checks. Full quicksort, selection, randomized geometry, precision engineering and broader correctness theory retain their own chapter boundaries. Floating-point FFT remains educational, with no unrestricted integer-rounding guarantee. Course screening is bounded; neither worldwide optimality nor perfect performance on unseen questions is claimed.

a_recurrence is student-approved and ready. a_divide remains draft. The proposed next topic is a_correct and may begin only after explicit approval.
