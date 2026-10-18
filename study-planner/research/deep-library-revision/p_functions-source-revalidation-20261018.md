# Functions: fresh scoped written-source revalidation

State: individual review in progress. The published previous edition has not yet been promoted as a newly complete review.

## Actual text reread in this continuation

- **Cambridge, Programming in C, 2017–18; Neel Krishnaswami.** Lecture2, all19PDF pages, text extracted by the web reader. First query-string attempt failed; the exact official base URL worked. The returned title, author, term and19-page length match the intended document. Source address-space illustration pixels were not newly inspected. [Official PDF](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture2.pdf).
- **UC Berkeley, Composing Programs; John DeNero.** Complete §1.3 text, including parameters, fresh frames, lookup, abstraction and operator discussion. Embedded environment diagrams were not newly visually inspected. §1.6 and mutation sections remain prior actual readings, not claimed as fresh rereads in this pass. [Official text](https://composingprograms.com/pages/13-defining-new-functions.html).
- **Harvard, CS50x2025; David J.Malan.** Lecture4 Swapping heading through the next Overflow heading; both complete C swap bodies and surrounding comparison prose. Lecture1 Functions and other Lecture4 sections remain prior readings, not fresh complete readings. [Official note](https://cs50.harvard.edu/x/2025/notes/4/#swapping).
- **CMU,15-122 Contracts.** Physical PDF pages19–39, including full argument repair, loop invariants, termination, bounded arithmetic, modular specifications, exercise statements and supplied sample solutions. Surrounding pages17–18 were also read. Earlier pages1–10 remain historical readings, not a fresh full-document claim. [Official PDF](https://www.cs.cmu.edu/~15122/handouts/lectures/01-contracts.pdf).

Local fresh byte hashes were not obtained by this web-reader pass. Historical fingerprints are retained in the original reviewed-course register and are not relabeled as current downloads. Stanford and MIT remain documented previous supplementary readings; no fresh reread is claimed yet.

## Reconciliations retained or strengthened

1. Cambridge's historical empty-list explanation applies to the chapter's C17 contract, not C23 or C++. Its static-scope wording is refined into visibility, storage duration and linkage. Its example x86 layout is not a portable address rule.
2. Cambridge's macro lecture is instructional simplification: replacement operates on preprocessing tokens, `##` pastes tokens, and replacement/argument expansion rules need the standard-level qualifications. A malformed displayed JOIN line is not adopted as an executable definition.
3. Harvard describes its pointer swap as passing by reference. In C, the pointer values are copied into distinct parameter objects; dereferencing them designates caller objects. True C++ references are a separate explicitly named language mechanism.
4. Berkeley's environment model separates each invocation's bindings from returned values. The model does not assert a machine ABI or a count of physically allocated frame bytes. Its ordinary Python scope is not silently generalized to every advanced class/annotation exception.
5. CMU physical page24's text ends with a strict `e/2 > 0` assertion, contradicted by e=1. Nonnegativity `floor(e/2) >= 0` is the needed termination bound. The preceding invariant/preservation calculation already supports the repaired statement.
6. CMU's C0 modular integer examples must not be imported into signed C17 arithmetic. Its sample GCD interface intentionally promises a common divisor, not maximality. A caller using only that weak postcondition may not silently assume greatest-common-divisor behavior from the function's name or body.

The thirty-six newly rewritten answer blocks are an unintegrated review manuscript. Other question answers, the two authentic bridge placements, simulations, final notes and complete browser gates still need individual review. Baseline completed-review count remains27of60.


Additional standard-level checks: WG14N1570 section6.2.1 paragraph7 confirms the declaration-point scope rule, and section6.2.4 paragraph2 confirms ended-lifetime pointer indeterminacy. These are named C11 draft provisions used for the corresponding unchanged C17 rules, not a claim to have freshly read all701pages. The original official PDF was checked through the web reader.


For PF36,WG14N1570 section6.5.2.2 paragraph10 was checked directly: separate called bodies are indeterminately sequenced. This supplies the required distinction from direct unsequenced argument modifications. Fresh standard reading is limited to these identified provisions.
