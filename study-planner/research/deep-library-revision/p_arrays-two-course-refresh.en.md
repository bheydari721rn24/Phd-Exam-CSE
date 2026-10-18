# Arrays: bounded independent source refresh

Date: 2026-10-18. Read-only research assignment. No app checkout, synced source or Site publication changes were made.

## Acquisition and actual reading

### University of Cambridge

Neel Krishnaswami, Programming in C, Michaelmas 2017–18, Lecture 3, Pointers and Structures. Official URL: https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture3.pdf .

Fresh download: 25 pages, SHA-256 `11a25cb24b7ebcb62d226c7fd90ed44fbcb5941d379e1bab5f005eead040f1b4`, matching the existing register. All extracted slide text was actually read. Physical slides 3,12,13,25 were also visually inspected: endian/address illustration, argv pointer graph, multidimensional parameter declarations, and complete exercise prompts. Other slide pixels were not newly inspected.

Chapter contributions: pointer-target identity, array indexing/strides, adjusted pointer parameters, pointer arrays versus rectangular arrays, and negative-index legality. Reconciliation: array-to-pointer conversion has exceptions; the illustrated numeric addresses and word sizes are platform examples. Its `%p` example needs `(void*)` argument casts in strictly typed C. The substring-search exercise searches `s` inside `f`, so implementations must state argument roles; a const-preserving returned type is preferable for const input. Struct/union summaries require additional qualifications and are outside this arrays refresh's adopted teaching boundary.

### Carnegie Mellon University

Frank Pfenning and André Platzer, 15-122 Principles of Imperative Computation, Fall 2026, Lecture 3, Arrays. Official URL: https://www.cs.cmu.edu/~15122/handouts/lectures/03-arrays.pdf .

All 19 pages of written text were actually read across overlapping web-reader responses, including Exercises 1–4 and sample proofs/solutions on pages12–19. Both local HTTPS host variants refused connections, so the historical register hash was not relabeled as a fresh hash. Web screenshot requests yielded references without visible image pixels; the source's memory diagrams therefore remain unverified visually in this pass. Their surrounding prose and code were read.

The source provides C0 allocation, zero initialization, checked indexing, aliasing, copying and invariants. These are C0 rules, not C17 automatic-array rules. Exercise 3's negative conclusion presumes no useful additional length guarantee; a suitable nonempty-array precondition changes what can be implemented. Its copy proofs contain naming slips and substantive overlap/arithmetic issues explained below. Allocation lifetime is managed, and an unreachable array is eligible for collection; that does not establish exactly when collection occurs.

### Additional scoped language rules

Official C draft: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf . The fresh official artifact acquired during the immediately preceding functions refresh was reused read-only: SHA-256 `208969fec021e4f4ce87a1873765298c73e7bbb5209b1c5868967c7adfc8492e`. Only the following additional provisions were reread, not all701pages:

- 6.3.2.1p3, physical page72: array conversion and exceptions.
- 6.5.6p7–9, physical page111: object-domain limits of pointer arithmetic/subtraction and `ptrdiff_t` representability.
- 6.7.9p10, physical page158: indeterminate uninitialized automatic objects versus recursive initialization of static aggregates.
- Annex J.2, physical page578: explicit out-of-range multidimensional index example despite apparently accessible adjacent storage.

N1570 is a public C11 draft supplying corresponding retained C17 rules, not a newly acquired final C17 edition. The array-rule excerpts are in `c-array-rules.txt`.

Official CMU integer support: https://cs.cmu.edu/~15122/handouts/slides/review/02-ints.pdf . Only the relevant overflow/comparison scopes were read: numbered slide30 (physical31), and numbered slides50–51 (physical51–52). They confirm modular32 arithmetic and the distinction between ring identities and signed ordering. The rest of this88-page deck is not counted as read. No fresh byte hash or diagram inspection is claimed.

## Source issues requiring explicit repairs

### Object boundaries are stricter than numerical contiguity

For `int a[4][5]`, `a` converts to a pointer to its first five-integer row. `a+1` advances one row, and `a[1][2]` designates a valid scalar. In contrast, `int *p=&a[0][0]` points into the first row array: `p+5` is its one-past pointer; evaluating `*(p+5)` does not become a legal second-row access merely because the numerical location coincides with the next row's start. `p+6` already exceeds the permitted arithmetic range. Use a row-pointer expression or a genuinely flat array representation for cross-row indexing. The draft's Annex J.2 explicitly reinforces the same distinction with `a[1][7]` for `int a[4][5]`.

For Cambridge's exercise `p[-2]`, the equivalent expression is `*(p-2)`. If `p` designates element k of a live array, this read requires k>=2 and a valid initialized target element; one-past p at k=n is also usable when n>=2. Negative relative indexing does not create negative C declaration indices. Separate numeric-address arithmetic cannot establish pointer-object membership or lifetime.

### C0 initialization is not C17 initialization

CMU's allocated C0 integer array starts with zero-valued elements and invalid indexing raises a defined runtime error. An ordinary uninitialized C17 automatic `int a[10];` has indeterminate element values; it does not acquire zeros because another language's allocator provides them. Static C integer arrays are zero-initialized, and `int a[10]={0};` explicitly initializes the first element and initializes omitted elements to zero. Numeric layout exercises must not imply that a read from an indeterminate cell is safe.

### CMU copy_into overlap and overflow counterexamples

The source's Exercise2 specification compares final source and destination segments without a no-alias premise. With one shared array `[1,2,3,4]`, leftward forward copying source index1 to target index0 for3elements yields `[2,3,4,4]`: final source `[3,4,4]` differs from destination `[2,3,4]`, contradicting that postcondition. Rightward copying source0 to target1 yields `[1,1,1,1]`, which can satisfy final-source equality while failing the intended original-input copy. Both demonstrate why a snapshot-based contract and an alias-aware direction or temporary copy are needed.

There is also an arithmetic gap: under C0 modular32 arithmetic, source length1, i=2147483647, n=1 satisfies `0<=i` and wrapped `i+n<=1`, but the segment is invalid. With checks enabled, the specification helper's own segment precondition may fail before the body; otherwise the first source access is out of bounds. A safe premise states `0<=i && i<=length(source) && 0<=n && n<=length(source)-i`, and similarly for target index j. The subtractions are safe under their preceding inequalities. Do not transport these modular comparisons into a signed-C proof.

CMU's Exercise4 identity trace can be independently reconstructed from its printed code: first A and B share `[1,2,2]`; C is a fresh copy. After B[2]=-1 and C[2]=1, A=C redirects A to C's `[1,2,1]`; assigning B a new two-element C0 array makes B designate `[0,0]`. The old `[1,2,-1]` array becomes unreachable. This is a code-derived trace, not a claim to have visually matched the original final diagram.

## Individual review of PA01–PA12

All twelve current stems and solutions were read. No incorrect concrete numeric answer or behavior classification was found in this bounded set.

| ID | Checked result | Teaching emphasis |
| --- | --- | --- |
| PA01 | address1632;48bytes; last byte1647 | Distinguish declared lower bound, final start, occupied byte and one-past boundary. |
| PA02 | declared coordinate(5,5) | Apply divisibility, extent and normalized mixed-radix inversion. |
| PA03 | five columns; base1000 | Two observations do not determine total row count. |
| PA04 | row830; column828 | Equal addresses at selected indices do not identify the entire layout. |
| PA05 | offset48/address2192; inverse47=(2,1,2) | Use full strides rather than an index sum. |
| PA06 | source offsets7,9 map to5,9 | Transpose changes destination stride and shape. |
| PA07 | requested1080,1060; extrema1000,1100 | Negative stride defines a numerical view, not C provenance. |
| PA08 | symmetric lookup offset11/address3088 | Apply symmetry before the lower-triangle map. |
| PA09 | (2,4) offset11; offset9=(2,2) | Upper-row lengths decrease. |
| PA10 | offset2=(2,0); offset5=(3,0) | Repeated boundaries represent empty rows; use half-open intervals. |
| PA11 | offsets0,6,12,18,24; sum60 | Offset sums are distinct from stored-value sums; abstract n=0 is not a valid fixed C array. |
| PA12 | no portable difference for separate allocations | Same-object membership and representability precede arithmetic. |

These first eleven problems heavily emphasize address/layout mathematics; PA12 begins the pointer-object boundary. That is coherent as a section, but those twelve alone do not cover initialization, alias/copy proofs, C0/C distinctions, or safe loop contracts. The remaining question bank needs its own review before chapter completion is claimed. No review of PA13 onward is asserted here.

`check_models.py` independently verifies the printed numbers, packed-coordinate enumeration, jagged reconstruction, transpose/inverse bijections across144positive shapes, and the two copy/overflow counterexamples. All14check groups pass; `mathematical-checks.json` records the results. These are finite mathematical/reference-model checks, not execution of C/C0 or the app simulations, and do not replace the general proofs.

## Remaining verification boundaries

This refresh covers two selected university texts plus named language rules. It neither ranks all worldwide courses nor claims a new six-university refresh. CMU original diagram pixels and new byte identity remain unverified; Cambridge visual inspection is restricted to the four named slides. No examination PDF reread, app browser audit, compiler execution or publication was performed by this assignment.
