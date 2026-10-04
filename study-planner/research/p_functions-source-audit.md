# Functions chapter: source selection and reconciliation

## Discovery and selection boundary

Six distinct accessible written courses from Cambridge, Berkeley, Harvard, CMU, Stanford and MIT were compared on written access, exact chapter coverage, semantic depth and exercise value, each scored from one to five. The scored register includes reasons and exact reading ranges. Four primary sources jointly cover C interfaces and effects, lexical environments, concrete caller/target tracing, and modular mathematical contracts. Stanford adds actual C++ reference semantics and MIT adds an independent Python scope/return comparison, so all six contribute. This is a bounded evaluated pool, not an unverifiable assertion that every worldwide course was found.

Cambridge Lecture 2 was read in full, 19 pages. Stanford's two-page handout was read in full. MIT Lecture 4 slides 3–35 were read. Berkeley §1.3, §1.6.3–1.6.4 and the sequence-object sharing/mutation material of §2.4.2 were read; material on classes, dispatch dictionaries and advanced mutable closures was outside this boundary. Harvard Lecture 1's function section and Lecture 4's value/pointer swapping section were read. CMU Contracts pp. 19–39 were read with introductory context on pp. 1–10; intermediate source pages not inspected are not counted as read.

## Retrieval identity check

The first cached responses for three PDF URLs had the wrong document content: Cambridge returned an old discrete-mathematics text, Stanford returned mathematical-functions slides, and MIT returned relations notes. Document titles and page counts exposed the mismatch. Fresh URL retrievals with a chapter-specific query retrieved the actual 19-page Cambridge, two-page Stanford, and 35-slide MIT documents. Those corrected documents and their hashes are the counted evidence; the first incorrect responses are not counted or cited as reviewed. Private original files remain outside the published app.

The CMU live notes identify Fall 2026, even though the search index described Fall 2025. The acquisition text, not the stale indexed date, determines the citation.

## Reconciliation of language rules

- Harvard describes pointer swapping as passing “by reference.” In this C17 chapter that phrase is refined to copied pointer values enabling writes through targets. It does not create C++ reference parameters.
- Cambridge's static-scope explanation is separated into identifier scope, object duration and internal linkage. Its physical 32-bit address layout is not elevated to a portable C rule.
- Stanford's absolute-value illustration omits the most-negative signed integer boundary. The chapter requires representability rather than claiming -INT_MIN is safe.
- MIT's historical print statements are expressed in Python 3. Python None is a returned object, not a printed numerical result; output events are separated from return values.
- CMU C0 modular integer arithmetic is not copied into signed C arithmetic. Its printed termination argument on p. 24 should establish floor(e/2) >= 0, not > 0 at e=1.
- C17 empty-list declarations are distinguished from void prototypes, C23, and C++.
- Separate C function bodies can be indeterminately sequenced while direct conflicting argument modifications remain unsequenced. WG14 N1570 §6.5.2.2 paragraph 10 and §6.5 paragraph 2 supply the precise distinction.
- Python binding, defaults and free-variable lookup are checked against the official tutorial and execution model. Ordinary function blocks are distinguished from advanced annotation/class-scope exceptions, which are not included here.

## Accessible exercise families and delivery disposition

Cambridge p. 19 lists lowercase counting, merge-sort memory and swap macros. Array/string implementation and advanced recursion are deferred to their dedicated chapters; macro repeated evaluation and alias-safe swapping receive original fully worked cases here. Stanford's set-to-zero examples motivate independently written mixed-reference/value cases. MIT's scope, return/print and function-argument examples motivate original binding and exception cases. Berkeley's square/sum-square and composition examples motivate distinct original environment and callback traces; the text has no claim here of an exhaustive all-course problem corpus. CMU Exercises 2 and 3 receive independently formulated geometric-sum and specification-strength tasks. The chapter's 89 original/course-inspired tasks plus two authentic bridge revisits are a curated bank, not a reproduction of all external exercise sets.

## Archive evidence

MSc CS 1393 Q167, original PDF page 34, and PhD CE 1405 Q9, page 3, were rendered and visually reread at the pinned archive revision bdadf6e2c9cadc4772ae137a96a3da753c7cfd08. Their source hashes are in the question records. Both are openly labeled revisits and bridge questions about call/return semantics; neither is falsely described as a new functions-specific unique item. Q167's English options describe the decisive correct stride and three option defects rather than pretending the printed pseudocode is strictly typed C17.

## Coverage limit

Arrays, strings, detailed recursive recurrences, pointer arithmetic, dynamic allocation, object-oriented methods and concurrency have separate plan chapters. Function-related distinctions needed before those chapters are introduced here, with their boundaries explicit. Mathematical proofs and exact finite checks establish the included models; literal universal completeness or guaranteed unseen-exam performance is not claimed.
