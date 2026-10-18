# Independent layout review: PA01–PA12 and the arrays lesson

Date: 2026-10-18. All study-checkout access was read only. The first twelve current question records and the complete main arrays lesson were read. A second targeted read recovered the multidimensional-pointer, traversal and prefix-sum text omitted by the first output's truncation. No Sites tool was called. No C compiler or native pointer arithmetic was used.

## Corrections and qualifications required

### Main lesson: empty difference-array update

The lesson permits empty segments `[k:k)` for every boundary `0<=k<=n`, but later states that adding c on `[l:r)` changes `D[l]` by +c and optionally `D[r]` by -c. For the permitted `[n:n)` and an n-entry difference array, `D[n]` is outside the object. This is a genuine missing boundary case, not a different numerical convention. The initialization `D[0]=A[0]` also requires n>0.

State the algorithm as follows: an empty update is a no-op; otherwise `l<r<=n` proves `l<n`, so updating `D[l]` is legal, and update `D[r]` only when `r<n`. For n=0, the difference sequence is empty. An n+1 boundary representation is a different valid contract but must actually allocate that extra position and specify its sentinel semantics. The oracle includes the concrete n=3, `[3:3)` access counterexample. Its Python `IndexError` demonstrates the numerical index error; it is not labelled a C execution result.

### Main lesson: realloc size-zero qualification

“On failure the old allocation remains valid” needs a **nonzero requested size** qualification in the C17 contract. A zero-size `realloc` request has implementation-defined behavior, including whether the old allocation is deallocated and what is returned. Do not classify every null result of `realloc(p,0)` as a failed positive-size allocation with the original block necessarily retained. Prefer handling zero length explicitly before the call.

### PA12: unstated integer width

The original stem says only that the two allocations store integers. It does not state four-byte integers. Therefore the old solution's “Four-byte integers and the observed difference forty” needs to become **“If sizeof(int) is additionally stipulated to be four bytes...”**, or the stem must explicitly stipulate that width. The principal answer remains unchanged: separate allocations do not satisfy C's same-array relation for pointer subtraction. Numerically adjacent addresses and an integer-sized spacing cannot create that relation.

### PA05: coordinate normalization

The existing arithmetic assumes zero lower bounds on all three axes. Make those bounds explicit in the stem. An extent alone specifies a count, not necessarily a declared lower index in the chapter's language-independent layout model. The answers 48,2192 and `(2,1,2)` are correct under zero-based normalized coordinates.

### PA07: element starts versus occupied bytes

The question explicitly gives byte strides, shape and logical-origin address, but does not state element width. The requested minimum and maximum **element-start** addresses are fully determined. Do not silently infer element width from the -4-byte column stride, or claim a total occupied-byte span without another assumption. If width four is explicitly added, the selected bytes total72 but the smallest containing byte interval has length104, namely addresses1000 through1103. The logical origin remains1020, not the smallest selected address1000.

### PA02: layout wording

The title identifies row-major storage; repeat it in the stem for a self-contained problem statement. The normalized row/column division and all stated values are correct under that representation. The same shape and base under column-major storage would give a different coordinate for the same address.

## Exact first-twelve results

| Record | Verified result and model |
|---|---|
| PA01 |12 elements, index5 address1632,48 occupied bytes, last element start1644, last occupied byte1647, one-past byte boundary1648; declared indices -3 through8 inclusive, width4 |
| PA02 |Row-major5-by-7, declared lower indices `(2,-1)`, width8; address4312 maps to `(5,5)`, offset27;4313 is not an element start; total storage280 bytes |
| PA03 |Column count5 and base1000; at least4 rows, no unique total row count; both observations reproduced by independently enumerated coordinates |
| PA04 |4-by-6, width2, base800: `(2,3)` has row-major address830 and column-major address828; matching coordinates for this shape are precisely `(0,0)` and `(3,5)` |
| PA05 |3-by-4-by-5 zero-based row-major: `(2,1,3)` offset48/address2192; offset47 gives `(2,1,2)` |
| PA06 |2-by-5 source to5-by-2 copied transpose:7 maps to5,9 maps to9; full permutation `[0,2,4,6,8,1,3,5,7,9]` |
| PA07 |Address map1020+40i-4j,3-by-6; `(2,5)`1080, `(1,0)`1060; minimum start1000 at `(0,5)`, maximum start1100 at `(2,0)` |
| PA08 |Symmetric6-by-6 lower-row packing: `(1,4)` redirects to `(4,1)`, offset11, address3088;21 packed elements/168 bytes |
| PA09 |Upper5-by-5 row packing: `(2,4)` offset11; offset9 is `(2,2)`;15 packed elements |
| PA10 |Lengths `[2,0,3,1]`, boundaries `[0,2,2,5,6]`; offset2 is `(2,0)`,5 is `(3,0)`;6 has no coordinate |
| PA11 |n=5 diagonal offsets `[0,6,12,18,24]`, sum60, count5; n=0 is an empty abstract selection, not a valid fixed C zero-bound declaration |
| PA12 |No portable pointer subtraction between separate allocations; in one live int array, positions0 and10 yield difference10 if endpoints and ptrdiff_t range are legal. Position10 may be one-past in a10-element array, or a dereferenceable element in an array of at least11 elements. |

## Mathematical generalizations and their proofs

### Two layouts coincide only at solutions of an integer equation

For normalized coordinates, row-major offset is `iC+j` and column-major offset is `jR+i`. Equality is equivalent to `i(C-1)=j(R-1)`. For R,C>1, let g=gcd(R-1,C-1). Dividing the equation by g gives relatively prime coefficients, so every solution in bounds is

`i=t(R-1)/g`, `j=t(C-1)/g`, with t=0,...,g.

There are g+1 coincidences. A single-axis matrix also has identical row/column order for every element; the same count formula works, including the1-by-1 case. For PA04, g=gcd(3,5)=1, hence exactly the first and last positions coincide. A useful non-endpoint example is4-by-7, with g=3 and four coincidences; matching one address does not identify layout.

### Inversion is mixed-radix uniqueness

A valid offset in a positive-extent row-major matrix has a unique quotient and remainder by C. Repeated quotient/remainder by the final dimensions uniquely decodes higher dimensions. An empty extent produces no valid element offsets; do not divide by a zero extent. Inverting a byte address additionally requires an in-range byte difference divisible by the stated element width. Numeric alignment is necessary for the diagram model, not sufficient for C object validity.

### Transposition is a permutation between differently shaped domains

Decode source offset into `(i,j)` in R-by-C, then encode `(j,i)` in C-by-R. The target offset is `jR+i`. Its inverse decodes with the **new** column count R and swaps the recovered pair. It is not generally correct to apply the original fixed-shape flattening operation twice without changing the shape. The first and last elements are fixed but this does not make the whole mapping identity.

### Packed-triangle formulas derive from preceding row lengths

Lower row i is preceded by lengths1,...,i, totaling i(i+1)/2; add j for a legal `0<=j<=i<n`. Upper row i is preceded by lengths n,n-1,...,n-i+1, totaling `in-i(i-1)/2`; its within-row column offset is j-i. Only then encode `0<=i<=j<n`. Symmetric lookup canonicalizes to `(max(i,j),min(i,j))` first. Both packed lengths are n(n+1)/2. The equal capacity of upper/lower formats does not make their coordinate maps interchangeable. Machine products require separate overflow guards or widening.

### Jagged inversion must use the correct repeated-boundary interval

Require `0<=o<Q[R]` first. Then `upper_bound(Q,o)-1` gives the containing row and `o-Q[row]` gives its column. The *last* boundary no greater than o skips repeated boundaries of empty rows. With valid o, the selected row has a strictly larger right boundary and is nonempty. All-empty shapes have no valid o. This proof also handles initial and trailing empty rows; an equality-only search cannot do so reliably.

### General affine extrema need nonempty shape, and aliasing is separate

For positive axis extents R,C and byte strides sr,sc, the minimum selected start is `B+min(0,sr(R-1))+min(0,sc(C-1))`; the maximum replaces each min by max. The coordinate choices are independent, so choosing each extremizing endpoint attains the bound. Zero or colliding strides can select the same storage more than once. A valid shape alone does not prove injectivity, nonoverlap, sufficient backing storage, or pointer provenance. Empty shapes have no selected minimum or maximum.

## Oracle results

The standalone `oracle.py` constructs coordinate sequences independently and compares formulas against their positions. It passed19 grouped assertions:

-12 exact record checks.
-256 two-dimensional shapes,18496 positions: row/column encodings, inversion, coincidence criterion/count and transpose bijection.
-512 three-dimensional shapes,46656 positions, each extent1..8.
-343400 packed-triangle coordinates and338350 symmetric canonical lookups for n=1..100.
-3906 jagged shapes,37110 valid coordinates, row count0..5 and every row length0..4.
-101 diagonal cases n=0..100.
-4356 affine shape/stride cases with each axis1..6 and strides -5..5.
-The concrete lesson difference-array empty-update counterexample is recorded as an expected failure of the unqualified rule.

These are finite checks supporting the given proofs, not global accuracy guarantees. They establish no source-reading claims and do not certify later rewritten wording, typography, figures, simulation behavior, allocation metadata or C implementation layout.
