# Arrays: Harvard and Berkeley written-source revalidation

Review date: 2026-10-20. This report was prepared outside the study-planner checkout. No chapter, source register, synced source, Site state, or deployment was modified.

## Fresh acquisition and exact reading scopes

The three official HTML resources were freshly acquired with HTTP 200. Their SHA-256 digests match the current p_arrays reviewed-course register. `acquisition.json` records byte sizes, acquisition timestamps, and final URLs; the adjacent HTML files preserve the freshly obtained bytes. Extracted `*-read-scope.txt` files contain the actual reading scopes. Scope extraction used UTF-8 explicitly; the first general-purpose full-page extraction used a guessed encoding and was replaced for actual reading. Importing the extraction helper caused one repeat acquisition; the acquisition register contains the final identical-byte fetch.

| University | Course / author as identified in the existing course register | Actually read now | Fresh SHA-256 |
|---|---|---|---|
| Harvard | CS50x 2025, David J. Malan | Lecture 2 written notes, complete bodies of Arrays, Strings, String Length, and Command-Line Arguments; from the Arrays heading through the end of the argv printing example, stopping before Exit Status | `56ab89cca73e293ecb09c52bcd9caa13cd068f964a1543fac4bdbdcdd4a338b4` |
| UC Berkeley | CS61A / Composing Programs, John DeNero | Complete §§2.3.1 Lists, 2.3.2 Sequence Iteration, 2.3.3 Sequence Processing, 2.3.4 Sequence Abstraction, 2.3.5 Strings; stopping before Trees | `f7b6cb1bde1edf7235e14f6e2931ddbf19517373726414b585f77ecb4e498df3` |
| UC Berkeley | Same course, supplementary chapter | Complete §2.4.2 Sequence Objects, including sharing, identity, comprehensions, tuples, and tuple-contained mutable elements; stopping before Dictionaries | `7a66af669941b362b4201e5c516206942311edd36abd3b93e0b02c211210cfc8` |

Official written URLs:

- [Harvard Lecture 2](https://cs50.harvard.edu/x/2025/notes/2/)
- [Berkeley sequence sections](https://composingprograms.com/pages/23-sequences.html)
- [Berkeley mutable sequence objects](https://composingprograms.com/pages/24-mutable-data.html#sequence-objects)

No video or transcript was needed. Stanford and MIT were not freshly reacquired or reread in this bounded refresh, so their historical complete-reading claims should not be promoted to fresh-reading claims. The existing Cambridge/CMU source audit was inspected for selection context; their documents were not independently reread by this agent.

## Harvard synthesis and reconciliation

The written progression moves from three separate scores to an indexed array, an input loop, and a length-parameter average; it then develops terminated character storage and argv traversal. This is the strongest practical starting point among the two refreshed universities. Its simplicity requires explicit qualifications in an advanced chapter: listed numeric type sizes are platform examples; an array parameter adjusts to a pointer rather than copying the array; and a valid average requires positive length, accessible initialized elements, and representable intermediate arithmetic. The text’s broad string explanation should distinguish CS50’s `string` pointer alias from a character-array object. `strlen` measures bytes before the first NUL, not capacity, and its result has type `size_t`. argv is an array of pointers, not one flat character array. Conversion by subtracting 32 presupposes the illustrated encoding; generic ctype calls require an unsigned-char-representable argument or EOF. These qualifications are already mostly present in the chapter and should remain explicit in worked answers. The selected notes contain examples, not a complete formal treatment of C pointer bounds. [Source](https://cs50.harvard.edu/x/2025/notes/2/)

## Berkeley §2.3 synthesis and a discovered source error

The selected sections develop indexing, list concatenation/repetition, nested selection, iteration, unpacking, ranges, map/filter/reduce, basic slicing, and strings. This supplies the chapter’s mathematical sequence interface and Python comparison. Slicing here expressly covers basic positive-step cases; it does not substantiate advanced negative-stop normalization or extended-slice assignment. Those require the separate Python reference already cited by the chapter. String membership tests substrings, whereas list membership tests elements.

A genuine boundary error occurs in §2.3.3: its `divisors(1)` implementation returns `[1]`, despite describing proper divisors as positive integers smaller than the argument. Consequently its displayed exclusion of 1 from the first perfect-number computation does not match that code; the later higher-order example includes 1. The prose also incorrectly describes 1 as ordinarily perfect. Under the stated proper-divisor definition, the correct empty divisor list has sum zero, so 1 is not perfect. The independently checked positive examples below 1000 are 6, 28, and 496. This error does not affect the chapter’s present mapped/filter bank, which does not reproduce that example. [Source](https://composingprograms.com/pages/23-sequences.html)

## Berkeley §2.4.2 synthesis

The playing-card example distinguishes shared names, in-place changes, a new outer list, and nested sharing. Its identity comparisons and tuple example are relevant to PA46, PA47, and PA49. A new list comprehension does not generally imply recursively independent contents: an identity mapping can preserve every inner list. A tuple prevents replacement of its own slots but can still refer to a mutable list. The source’s nonsharing statement concerns its particular Unicode-name transformation, not all comprehensions. Explain diagrams with separate outer slots and inner object identities rather than copying the displayed nested values into unrelated boxes. Equality and identity should be evaluated separately. The current PA46–PA50 numerical outcomes were rechecked and are correct; their forthcoming expanded solutions should preserve these distinctions. [Source](https://composingprograms.com/pages/24-mutable-data.html#sequence-objects)

## Comparative selection judgment

Retain Harvard and Berkeley as complementary members of the existing four-university core: Harvard provides concrete C traversals and termination; Berkeley provides the Python sequence/object distinction. Neither replaces Cambridge’s typed pointer-boundary work or CMU’s proof-oriented segment work. This is a judgment about the documented accessible candidate pool, not a worldwide ranking or a claim to have evaluated every course. The current Stanford/MIT supplements remain historically selected for backing-storage growth and iteration mutation; this refresh does not add an independent fresh review of either.

## Exact local editorial corrections / risks

1. PA52 currently contains literal escaped `\\x27` strings where C apostrophes should appear. Present a proper fenced C declaration: `char s[8]={'a','b',0,'c'};`. This is a question-rendering defect, not an uncertain numerical answer.
2. PA51 asks for a “number of stored characters” while crossing code-point and byte models. Ask instead for the number of `char` elements in the specified eight-bit-byte UTF-8 array, including its final NUL. The result is four elements; Python code-point count is two and encoded byte count is three. Its existing solution already identifies the encoding assumption correctly.
3. PA42–PA45 require independent formal sequence rules beyond Berkeley’s expressly basic slice scope. Keep separate citations to Python’s Common/Mutable Sequence Operations.
4. Do not represent the university examples as verbatim reproduced examination questions. The current independently written PA46, PA50, and PA81 transformations have suitable course-inspired labels. Exact course assignment inventories were not read in this refresh, so no claim to include every course exercise is justified.

## Independently authored teaching and exercise proposals

These are original extensions, not quoted university exercises.

- **Average contract and arithmetic:** for `[7,8,10]`, draw the three read positions, accumulate 25, and show why integer division gives 8 whereas floating division approximates 25/3. Then separate zero length, invalid storage, uninitialized entries, and accumulator overflow into distinct failed preconditions. Casting the truncated integer result afterward cannot restore the fraction. This expands PA81 without adding unrelated mechanics.
- **Two-level alias diagram:** start with `a=[[2],[5]]`, create `b=a[:]`, append 7 through `b[0]`, and replace `b[1]` with `[9]`. The graph should initially have two outer objects sharing both inner objects. The first operation mutates one shared node; the second redirects only one outer edge. End states are `a=[[2,7],[5]]` and `b=[[2,7],[9]]`.
- **Slice index proof:** use `range(*slice_spec.indices(n))` only as an audit tool after explaining normalization. For each selected index prove `0 <= i < n`, then distinguish reading an absent element from choosing an empty boundary interval. A diagram should place boundary markers between slots, including the before-first sentinel for a negative omitted stop.
- **Pointer versus character termination:** with arguments `"prog", "x", "yz"`, draw three argument pointers and the null pointer sentinel, then separate each string’s character terminator. `argv[2][1]` is `z`, `argv[2][2]` is NUL, `argv[3]` is null, and `argv[3][0]` is invalid. A flat diagram cannot show this distinction faithfully.
- **Comprehension independence counterexample:** an identity comprehension over `[[3]]` creates a new outer object sharing the inner list. Append through the result and demonstrate the original also changes. Compare it to a row-copy comprehension, and add a third nested level to show why one row copy is still not a universal deep copy.
- **Correct proper-divisor boundary:** if extending the sequence-processing example, define the domain `n >= 1`; use all `d` with `1 <= d < n` and `n % d == 0`. The empty case at 1 must be taught explicitly. This is an optional corrective example, not a needed expansion of the current array chapter.

## Independent executable evidence

`check_written_examples.py` passed **63 checks**, saved in `python-checks.json`. They include every current question certificate marked `python`, each executed in a fresh namespace, plus independently constructed identity/sharing cases, Unicode units, slice-index normalization for lengths 0–9, and reproduction/correction of the source’s perfect-number error. These are finite exact-example checks; they do not establish universal source completeness. No C/C++ compilation or execution is claimed.
