# Arrays and Indexing

## Reviewed sources and the chapter contract

This chapter teaches array representation, safe indexing and exact array transformations from first principles. It assumes that you can trace assignments, loops and function calls. The main language is C17. Explicitly marked comparisons use C0, Python 3 or C++. Mathematical algorithms use unbounded integers unless a machine range is specified. Numerical memory diagrams use a stated flat byte-address model; they do not authorize otherwise invalid C pointer operations.

Four primary written courses contribute different parts of the explanation: Cambridge Programming in C (Neel Krishnaswami, 2017–18), CMU 15-122 (Frank Pfenning and André Platzer, Fall 2026), Harvard CS50x (David J. Malan, 2025), and UC Berkeley CS61A / Composing Programs (John DeNero). Stanford CS106B (Chris Gregg, Fall 2016) is a fifth reviewed comparison for dynamic backing arrays. MIT 6.0001 (Ana Bell, Eric Grimson and John Guttag, Fall 2016) is a sixth reviewed comparison for list cloning and mutation during iteration. The [source review](../reviews/p_arrays-sources.html) records exact reading ranges, evaluated alternatives, selection criteria and corrections. References at the end link to written materials.

The central skill is to distinguish four things: a logical sequence, its allocated storage, the references that select that storage, and the sequence of writes that changes it. Address arithmetic alone cannot establish correctness. Every problem needs a domain, an access proof, a value relation and an explanation of whether the relation uses original or already modified values.

After reading, you should be able to derive row/column strides, invert a flat index, classify C array expressions, prove loop and copy invariants, detect alias corruption, calculate dynamic-array costs and explain Python shallow sharing. The worked bank emphasizes these mathematical and conceptual tasks. Two authentic examination items are explicitly labeled bridge revisits rather than newly discovered unique items. No finite source pool or test suite can guarantee all future examination questions.

## Elements, boundaries and object representation

An abstract array of length $n$ maps each integer index in $0\le i<n$ to one element. An array can repeat values; positions remain distinct even when values are equal. A segment $A[l:r)$ contains indices $l,l+1,\ldots,r-1$, requires $0\le l\le r\le n$, and has length $r-l$. Its right boundary is not an element. The empty segment $A[k:k)$ is valid for every boundary $0\le k\le n$.

For a language with lower bound $L$ and upper bound $U$, the length is $U-L+1$. The normalized index is $i-L$. A zero-length abstract sequence is useful, but a standard fixed C declaration cannot use a zero array bound. An empty logical sequence may instead have reserved capacity, or be represented by a pointer and length zero. A variable-length C array evaluated with a nonpositive bound is also invalid; do not turn a mathematical empty case into such a declaration.

A C array is a contiguous object consisting of elements of one element type. There is no extra gap between successive elements beyond what is included in each element's own size. An array of structures therefore uses the structure's full size, including any structure padding, as its stride. A pointer object stores a pointer value; it does not contain the whole pointed-to array. A Python list is a mutable sequence of object references and can contain heterogeneous objects. Its language contract does not promise the same raw layout as a C integer array.

Write the following initialization before doing any arithmetic:

~~~c
int a[6] = {4, -2, 7};   /* Remaining elements are zero. */
int b[6];               /* Automatic elements are not initialized here. */
static int c[6];         /* Static-storage elements are zero-initialized. */
~~~

The first array has six elements, not three; the initializer leaves the final three equal to zero. Reading an uninitialized automatic integer element does not give a portable predictable value. An arbitrary external input array also needs an explicit validity and initialization assumption.

If the first element begins at byte address $B$ and each element occupies $w$ bytes, then the numerical storage model gives

$$\operatorname{addr}(A[i])=B+w(i-L).$$

For $A[-2:5]$ with inclusive declaration bounds, $B=1200$ and $w=4$, element 3 is at $1200+4(3+2)=1220$. This example uses a language-independent declaration; ordinary C indices still start at zero. The array's final occupied byte is $B+wn-1$, while its one-past boundary is $B+wn$. Neither an arbitrary byte address nor a numerically aligned address proves that a live typed C object exists there.

<!-- FIGURE:boundaries -->

## Multidimensional layouts and inverse indices

A rectangular two-dimensional array with $R$ rows and $C$ columns has $RC$ elements. Let row and column lower bounds be $L_r,L_c$, and normalize $u=i-L_r$, $v=j-L_c$. In row-major storage, all $C$ entries of each earlier row precede the selected row, then $v$ entries precede the selected column. Consequently,

$$o_{\mathrm{row}}=uC+v,\qquad \operatorname{addr}(A[i,j])=B+w(uC+v).$$

In column-major storage, each earlier column contains $R$ entries:

$$o_{\mathrm{col}}=vR+u,\qquad \operatorname{addr}(A[i,j])=B+w(vR+u).$$

These expressions count elements first and bytes second. For $R=3,C=4,w=8,B=2048$, index $(2,1)$ has row-major offset 9 and address 2120; its column-major offset is 5 and address 2088. C's real rectangular array declaration uses row-major storage. Column-major here is a separate stated representation, not a switch in how C interprets its declared array.

The inverse follows from quotient and remainder. Given a valid row-major element offset $0\le o<RC$, divide $o$ by $C$: $u=\lfloor o/C\rfloor$ and $v=o\bmod C$. For column-major, divide by $R$ to recover $v$ and $u$. For a byte address $X$, first check that $X-B$ is nonnegative, divisible by $w$, and less than $wRC$. A byte inside an element is not necessarily that element's starting address.

For three normalized indices $u,v,t$ in extents $D_1,D_2,D_3$, row-major offset is

$$o=(uD_2+v)D_3+t=uD_2D_3+vD_3+t.$$

This is mixed-radix notation. Its uniqueness follows by repeatedly taking remainder and quotient by the last extent. In $d$ dimensions, the stride of axis $k$ in row-major order is the product of all later extents. Changing one index by one changes the element offset by that stride. The same principle handles a general affine view with stated strides $s_k$: $o=\sum_k (i_k-L_k)s_k$. Such a view may include gaps or reversed axes; it need not be a standalone C multidimensional array.

<!-- FIGURE:layouts -->

A true C declaration and an array of row pointers are different:

~~~c
int grid[3][4];
int (*row)[4] = grid;  /* Pointer to a complete four-int row. */
int *rows[3];         /* Array of three int pointers: pointees need allocation. */
~~~

The first contains twelve integer objects. Its expression conversion gives a pointer to a row, so row + 1 advances by four integers. The last contains three pointer objects and makes no promise that the selected row allocations are adjacent, equally long or even valid. Casting grid to int ** cannot create the missing row-pointer objects. A numerical flattening formula also does not justify using pointer arithmetic beyond the first actual row subarray; for portable C, index grid[i][j] with valid row and column bounds.

Transposition of an $R\times C$ row-major logical matrix produces a $C\times R$ result. Original position $(i,j)$ maps from $iC+j$ to $jR+i$. A transpose view can swap strides without moving data; a copied transpose creates a different physical arrangement. Square in-place transposition swaps each pair $i<j$ once and leaves the diagonal unchanged. Rectangular in-place transposition requires permutation cycles or extra storage and cannot use the square-only loop unchanged.

## C arrays, pointers and legal accesses

In most expression contexts, a C array expression converts to a pointer to its first element. Important exceptions include an array operand of sizeof, an operand of unary &, and a string literal used to initialize an array. A real array's sizeof counts its full storage. A function parameter declared int a[] is adjusted to int *a, so sizeof a inside that function counts the pointer object. The function must receive an independent length or a stronger explicit contract.

~~~c
int a[5] = {2, 4, 6, 8, 10};
int *p = a + 2;
int x = p[-1];           /* Selects a[1], so x is 4. */
size_t n = sizeof a / sizeof a[0];  /* Five, in this actual-array scope. */
~~~

The subscript p[-1] does not mean “count from the end” as in Python. The identity $p[k]=*(p+k)$ applies only when the resulting access is legal. Here p points at a[2], so -1 moves back to a[1]. For a pointer at a[r], permitted element-access offsets satisfy $-r\le k<n-r$. Pointer formation additionally permits $k=n-r$, the one-past position; dereferencing that position does not.

Pointer addition and subtraction must stay within one array object or its one-past boundary. Subtraction counts elements, not bytes, and its result must be representable in ptrdiff_t. The valid numerical byte difference is therefore not a justification for subtracting pointers into unrelated allocations. Relational comparisons between unrelated array pointers likewise cannot be used as a portable general address ordering.

Unary & applied to the complete array yields a pointer to the whole array type. a and &a can describe the same beginning of storage, but their types and increments differ: a + 1 advances one int after conversion; &a + 1 advances one five-int array. Equality of beginning locations is not equality of type or stride.

For an array with nonzero length, a + n is a legal one-past pointer useful as an exclusive end. A reverse loop using size_t must not rely on i >= 0 to stop, because size_t is unsigned. Use a boundary that decreases before the access:

~~~c
for (size_t i = n; i > 0; ) {
    --i;
    use(a[i]);
}
~~~

The body runs n times and never computes n - 1 when n is zero. Check arithmetic used in allocation: before requesting n * sizeof *p bytes, establish $n\le\lfloor\mathrm{SIZE\_MAX}/\operatorname{sizeof}(*p)\rfloor$. A successful arithmetic check still needs successful allocation and a live valid object. realloc may move storage and invalidate earlier aliases; on failure the old allocation remains valid, so keep the old pointer until the result is known.

For a rectangular parameter, int a[][4] adjusts to int (*a)[4]. The column extent participates in the row stride. C variable-length parameter forms can express a run-time column count, with the relevant positive-bound and implementation-support conditions; int ** remains a different representation.

## Traversals, reductions and proof obligations

Before tracing a loop, describe the exact visited indices. For increasing stride $s>0$ over the half-open segment $[l,r)$, they are $l+ts$ for nonnegative integers $t$ with $l+ts<r$. The count is zero when $l\ge r$; otherwise it is $\lceil(r-l)/s\rceil$. For a reverse traversal starting at $r-1$ with decrement $s$, the count is the same. A separate stopping relation involving the destination index can prematurely terminate a copying procedure.

To sum a segment, define original values $A_0[k]$ and use the invariant

$$l\le i\le r,\qquad S=\sum_{k=l}^{i-1}A_0[k].$$

Initially $i=l$ and the empty sum is zero. The guard $i<r$ together with the invariant proves a valid read. Adding the current value and advancing i extends the sum by exactly one term. At exit, $i=r$, so the required segment sum is obtained. The variant $r-i$ decreases to zero. Machine integer addition separately needs representability of all partial sums.

Finding a minimum needs a nonempty input or an explicit optional-result convention. If the first element initializes the minimum, comparisons number $n-1$. If a mathematical positive-infinity sentinel initializes it, comparisons number n and the first value always causes an update. Strict comparison retains the first occurrence of a tied minimum; non-strict comparison retains the last. Do not assume independence when analyzing the random number of updates; the authentic PhD bridge below derives it with indicator expectations.

For prefix sums, reserve $n+1$ entries and define

$$P[0]=0,\quad P[i+1]=P[i]+A[i],\quad
\sum_{k=l}^{r-1}A[k]=P[r]-P[l].$$

The query formula follows by cancellation of the first l terms, and also works for an empty segment. A static array permits linear preprocessing and constant-time range-sum queries. A later element update invalidates every subsequent prefix value; do not claim unchanged query correctness after mutation.

The difference sequence satisfies $D[0]=A[0]$ and $D[i]=A[i]-A[i-1]$ for $i>0$. Adding c to $A[l:r)$ changes only D[l] by +c and, if r < n, D[r] by -c. An n+1 boundary array can retain a right-end sentinel. Reconstruct by a prefix accumulation. This inverse relation explains range updates; it is not merely a pair of memorized signs.

For a two-dimensional prefix table indexed by boundaries, P has shape $(R+1)\times(C+1)$ and zero top/left edges. The recurrence and rectangle query are

$$P[i+1,j+1]=A[i,j]+P[i,j+1]+P[i+1,j]-P[i,j],$$

$$S=P[r_2,c_2]-P[r_1,c_2]-P[r_2,c_1]+P[r_1,c_1].$$

The final plus sign restores the overlap that the two subtractions removed twice. Half-open row and column bounds make empty rectangles and edge rectangles work without case-specific index subtraction. Native formulas below use a separate mathematical font.

<!-- FIGURE:prefix -->

## Mutation order, copying and overlap

An in-place transformation reads the values currently stored, unless it explicitly snapshots the original input. For a=[1,2,3,4], the forward update a[i] += a[i-1] for i=1..3 produces [1,3,6,10], because each read uses a modified predecessor. Running the same statements in reverse produces [1,3,5,7], because the predecessor has not yet changed. Both are well-defined mathematical sequences of statements; they compute different maps.

For a copy between distinct arrays, let B receive A[l:r). After t iterations, the copy invariant states $B[k]=A_0[l+k]$ for $0\le k<t$ and $0\le t\le r-l$. Destination index t and source index l+t are valid under the segment contract. The result array must have capacity at least r-l; a new allocation gives a distinct result even when the values match.

For a move within the same array from [s,s+m) to [d,d+m), original values are the desired specification. If d > s and the segments overlap, increasing-index copying overwrites source values that have not yet been read. Copy from the high end. If d < s, increasing-index copying is safe; decreasing-index copying may corrupt the source. If d=s, no change is required.

<!-- FIGURE:overlap -->

A rigorous reverse-copy invariant fixes the already copied suffix to original values and states that the remaining source prefix is unmodified. At step t descending from m-1, destination d+t lies above source s+t, so it cannot overwrite any still unread smaller source index. This is the reason for the direction, not a convention to memorize.

For disjoint arrays, source and destination are different objects. For a C move within one known backing array, compare integer offsets to select the direction. Do not compare unrelated pointers with > as a general portable overlap test. The library memmove supports valid overlapping byte regions using an as-if temporary-copy contract. memcpy requires nonoverlap. A language-level element-copy loop is more appropriate for object types whose semantics are not simply raw byte copying.

The reviewed CMU copying proof omits an important alias restriction: its postcondition compares final source and final target segments. When overlapping writes modify the source, even the asserted copied-prefix relation can fail. This chapter uses original-input snapshots in its specification and either disjointness or an overlap-safe move. The correction is demonstrated in both the problem bank and an animation.

### A complete overlap-safe element implementation

The following function moves elements within one known integer array. Its caller supplies a live initialized backing array with n elements whenever a nonempty move is requested. The function validates offsets before subtraction, so its tests do not themselves overflow. A zero-length move performs no pointer arithmetic or access and may use a null backing pointer. No unrelated-pointer ordering is needed.

~~~c
#include <stdbool.h>
#include <stddef.h>

bool move_ints(int *a, size_t n, size_t s, size_t d, size_t m) {
    if (s > n || d > n) return false;
    if (m > n - s || m > n - d) return false;
    if (m == 0 || s == d) return true;
    if (d > s) {
        size_t k = m;
        while (k > 0) {
            --k;
            a[d + k] = a[s + k];
        }
    } else {
        for (size_t k = 0; k < m; ++k)
            a[d + k] = a[s + k];
    }
    return true;
}
~~~

For the descending branch, at boundary k the target suffix with relative indices k through m−1 equals the corresponding original source suffix. The original source prefix with relative indices below k remains unchanged. After decrement, the read occurs at s+k and the write at d+k. Since d>s, the write is strictly above that source position and therefore above every remaining unread source position. The access checks give s+k<n and d+k<n without requiring an unchecked sum s+m. At k=0, the target is the entire original segment. The ascending branch has the dual invariant: the completed target prefix is correct, and the unread source suffix remains original because d<s. Both branches decrease their number of unprocessed elements by one. For a disjoint rightward move, descending order remains correct even though forward order would also work.

These validations establish ranges, not allocation authenticity: a caller that lies about n or supplies an expired pointer violates the backing-object contract. Returning true means the stated move was performed under that contract; it cannot prove facts about memory that C does not expose as metadata.

To insert at index k in a logical sequence of length n with spare capacity, move original positions n-1 down to k into positions n down to k+1, then write the new element and increase the length. There are n-k shifts. Deletion at k uses forward moves from k+1 through n-1 and decreases the length, for n-k-1 shifts. Old bytes outside the shortened logical prefix need not vanish; capacity and logical length are different.

Reversal swaps $(l+t,r-1-t)$ for $0\le t<\lfloor(r-l)/2\rfloor$. Its invariant fixes both completed ends and preserves the original untouched middle. Three reversals rotate a nonempty sequence left by k: reverse [0:k), reverse [k:n), then reverse [0:n). Normalizing k modulo n requires n>0; handle the empty sequence before that division. A cycle method uses $\gcd(n,k)$ cycles and visits every index exactly once.

The boundary form below avoids unsigned n−1 when the segment is empty. The caller validates l≤r≤n and the backing array before entry. In each iteration r−l>1 guarantees two distinct live indices after decrementing r. An odd middle entry is left alone; there are exactly floor((r−l)/2) pair swaps relative to the original segment length.

~~~c
void reverse_segment(int *a, size_t l, size_t r) {
    while (r - l > 1) {
        --r;
        int saved = a[l];
        a[l] = a[r];
        a[r] = saved;
        ++l;
    }
}
~~~

## Python slices, sharing and nested rows

Python single indexing normalizes a negative integer i to n+i and then requires a valid element. Slicing instead normalizes and clips boundaries, then follows a nonzero step. Positive steps default to start zero and stop n; negative steps default to start n-1 and a special before-first stop. The special omitted stop is different from an explicit -1, which normalizes to the last index. Consequently a[::-1] reverses a sequence, while a[:-1:-1] is empty.

After normalization, positive-step selected indices are $a+ts<b$ and negative-step selected indices are $a+ts>b$. Counting them gives a ceiling divided by the step magnitude when the respective interval is nonempty. Use slice(...).indices(n) when auditing Python's exact boundary normalization. A zero step raises ValueError; an out-of-range single index raises IndexError, while a clipped ordinary slice can simply be empty.

~~~python
a = [[2], [5]]
b = a[:]             # New outer list, same inner lists.
b[0].append(7)       # Also visible through a[0].
b[1] = [9]           # Rebinds only b's second slot.
~~~

After the first mutation, both outer lists contain a first reference to [2,7]. After the second, a is [[2,7],[5]] and b is [[2,7],[9]]. A shallow copy does not copy recursively referenced objects. A row comprehension that creates a fresh row each time avoids the repeated-row problem:

~~~python
bad = [[0] * 3] * 2
good = [[0] * 3 for _ in range(2)]
bad[0][1] = 8         # Both displayed rows change.
good[0][1] = 8        # Only the first row changes.
~~~

<!-- FIGURE:sharing -->

An ordinary step-one slice assignment can change the list's length. An extended slice with a step other than one requires exactly as many replacement items as selected slots. Mutating a list while iterating can skip shifted elements: the iterator advances its position while deletion moves the next element left. A safe filtering construction makes a new output or uses a carefully proved read/write compaction loop.

Python string elements are Unicode code points, whereas C char-array bytes and UTF-8 encoding lengths describe different units. One displayed grapheme may contain several code points. Reversal by code points is not automatically a correct visual reversal of human text. These distinctions prevent importing a byte-address formula into Python string indexing.

## C strings, terminators and bounded searching

A C string is a sequence of character values ending at its first zero character within accessible storage. Capacity, initialized bytes and string length are separate quantities. char s[] = "cat" allocates four characters; strlen(s) is three and sizeof s is four in that actual-array scope. char t[3] = "cat" is allowed in C but lacks the terminator, so it is not a valid string for strlen or %s. An embedded zero ends the string earlier even if later bytes remain in the array.

The string literal used through const char *p = "cat" must not be modified. A writable array initialized from the literal can be modified within its bounds. p's sizeof measures the pointer. strlen requires a terminator and scans up to it; the return type is size_t, not int. The final zero is a real array element, unlike the one-past pointer.

Searching m pattern characters in a text of length n requires candidate starts $0\le s\le n-m$ when $m\le n$. Each comparison reads text[s+t] with $0\le t<m$, hence $s+t<n$. In the worst case, a direct search performs $(n-m+1)m$ character comparisons, but successful early matches and mismatches can reduce that count. For m=0, specify a match at the starting boundary. For m>n, return failure before subtracting unsigned lengths.

~~~python
def first_match(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    for start in range(n - m + 1):
        j = 0
        while j < m and text[start + j] == pattern[j]:
            j += 1
        if j == m:
            return start
    return -1
~~~

This code is a complete bounded-search model, not a C library replacement. Returning a C pointer into a caller-owned text additionally depends on that text's lifetime. Command-line argv is an array of pointers to strings, with argv[argc] null; that final pointer is different from each argument's final zero character. If argc is zero, argv[0] is the null sentinel and cannot be read as a program-name string.

Character conversion using a numeric difference assumes an encoding such as ASCII. C's ctype operations accept EOF or an unsigned-char-representable value; a negative signed char must first be converted to unsigned char. Do not assume that bytewise uppercase conversion handles arbitrary UTF-8 text.

## Capacity growth and exact operation costs

A dynamic array maintains $0\le n\le c$, where n is logical length and c is allocated capacity. Its occupied logical prefix is [0:n); allocated spare slots are [n:c). Insertion requires free capacity or expansion. Expansion allocates a new backing block, copies the n live elements, changes the owning reference and releases the old block under the appropriate ownership rules. Any earlier interior pointer into released storage becomes invalid.

<!-- FIGURE:growth -->

Under the simple doubling model with initial capacity 1, successful appends allocate capacities 1,2,4,8,... . Copy work through a final capacity c is

$$1+2+4+\cdots+\frac c2=c-1.$$

For n≥1, the smallest power-of-two c at least n satisfies $n\le c<2n$. Hence copied elements are less than 2n and total writes including the n new elements are less than 3n. This proves amortized constant append cost under unit-cost element copying, while one expansion append still has linear cost. It does not say that every individual append is constant-time.

Doubling is not uniquely optimal. A fixed factor g>1 also produces a geometric total; its time/space constants differ. An additive increment instead creates quadratic total copying when it is fixed as n grows. Allocation time, element-copy behavior, cache effects and peak memory are outside the simplest unit-copy model and must be stated if included.

When c live elements expand to 2c, both blocks can coexist during copying, so the peak backing capacity is 3c slots. The final capacity alone misses that peak. A container with owned nested allocations also requires correct copy/move semantics; copying pointer values alone may produce shared ownership bugs. Shrinking at exactly half-full can repeatedly grow/shrink under alternating operations. A separate lower shrink threshold supplies hysteresis.

Two-dimensional traversal order affects a stated locality model. For a row-major matrix, visiting successive columns in one row accesses adjacent elements. Visiting one column down the rows uses a stride of C elements. Arithmetic operation counts may be equal while cache-line accesses differ. A precise cache question must state line size, alignment, cache capacity, replacement assumptions and reuse; “row-major is always faster” is not a theorem.

## Packed representations and advanced index reasoning

For a lower-triangular $n\times n$ matrix storing its diagonal in row order, valid normalized indices satisfy $0\le j\le i<n$. Earlier row lengths are 1 through i, so

$$o=\frac{i(i+1)}2+j,\qquad N=\frac{n(n+1)}2.$$

For an upper triangle in row order, row i has n-i entries and earlier rows contain $in-i(i-1)/2$ entries:

$$o=in-\frac{i(i-1)}2+(j-i),\qquad 0\le i\le j<n.$$

These are representation-dependent formulas. For a symmetric matrix stored only in its lower triangle, replace $(i,j)$ by $(\max(i,j),\min(i,j))$ before applying the lower formula. Multiplication and division must be ordered or widened so that a finite implementation does not overflow its intermediate product. The final representability of a triangular count does not alone ensure that i(i+1) fits.

<!-- FIGURE:packed -->

A jagged matrix with row lengths $r_0,\ldots,r_{R-1}$ can be packed into one flat sequence using boundary offsets $Q[0]=0$ and $Q[i+1]=Q[i]+r_i$. Element $(i,j)$ lies at $Q[i]+j$ for $0\le j<r_i$. Repeated offsets represent empty rows. Recovering a row from a flat position must locate a nonempty interval containing it, rather than taking the first equal boundary blindly.

A circular buffer with positive capacity c maps logical offset t from head h to $(h+t)\bmod c$. Maintain the length separately to distinguish empty from full when head equals tail. For negative integer rotations, normalize with mathematical modulo in [0:c); C's signed remainder may be negative and requires an explicit correction. The empty-capacity case cannot use modulo at all.

An in-place read/write compaction has invariant $0\le w\le r\le n$, with A[0:w) equal to the retained original values from A[0:r) in their original order. Because w never exceeds r, writing A[w] cannot damage unread positions above r. This gives a stable filter with linear reads and at most n writes. It is a proof about dependency direction, closely related to safe leftward copying.

## Worked mathematical and conceptual problems

The first two items revisit original MSc/PhD scans. The remaining items are original examination-style questions or independently worded course-inspired extensions, with their origin stated. Solutions explain the model, derive the result and examine a relevant boundary or distractor. Some tasks ask for a proof or behavior classification because a numeric answer would conceal the main issue.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

<!-- INCLUDE:review -->

## Exact array laboratory

Choose a transformation and inspect its exact checkpoints. Input is a small integer sequence; controls start paused. Value tokens move between source and destination positions while array objects retain their identities. A deliberately unsafe copy is labeled a counterexample and is compared with the original-value specification. Use the scene selector to inspect every concept, then the adjustable lab to change the data.

<!-- LAB:arrays -->

## References

1. University of Cambridge — Neel Krishnaswami. Programming in C, Michaelmas 2017–18. [Lecture 3: Pointers and Structures](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture3.pdf), slides 2–13 and array/string exercise prompts on slide 25. Complete 25-slide file screened; unrelated structures/union material is outside this chapter.
2. Carnegie Mellon University — Frank Pfenning and André Platzer. 15-122: Principles of Imperative Computation, Fall 2026. [Lecture 3: Arrays](https://www.cs.cmu.edu/~15122/handouts/lectures/03-arrays.pdf), pages 1–19, including specifications, aliasing, exercises and proposed solutions. The chapter supplies an explicit overlap correction.
3. Harvard University — David J. Malan. CS50x 2025. [Lecture 2 written notes](https://cs50.harvard.edu/x/2025/notes/2/), Arrays, Strings, String Length and Command-Line Arguments. Platform-specific sizes and informal passing explanations are qualified here.
4. University of California, Berkeley — John DeNero. CS61A / Composing Programs. [Sections 2.3.1–2.3.5](https://composingprograms.com/pages/23-sequences.html) and [Section 2.4.2](https://composingprograms.com/pages/24-mutable-data.html). Sequence abstraction, iteration, slicing and sharing are reconciled with Python's formal sequence contract.
5. Stanford University — Chris Gregg. CS106B: Programming Abstractions, Fall 2016. [Lecture 17: Implementing Vector](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1172/lectures/17-ImplementingVector/17-ImplementingVector.pdf), slides 3–28. Unit-copy doubling analysis is derived independently; doubling is not presented as universally optimal.
6. Massachusetts Institute of Technology — Ana Bell, Eric Grimson and John Guttag. 6.0001, Fall 2016. [Lecture 5: Tuples, Lists, Aliasing, Mutability and Cloning](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/1776670e271578eeb99fc25975f20586_MIT6_0001F16_Lec5.pdf), all 24 slides, particularly slides 7–23. Older print syntax is normalized to Python 3 in new examples.
7. Python Software Foundation. [Built-in Types: Common and Mutable Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations), including slicing, repetition and extended slice assignment.
8. ISO/IEC JTC1/SC22/WG14. [N1570 public C11 committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), sections 6.3.2.1, 6.5.2.1, 6.5.6, 6.5.3.4, 6.7.6.2–3, 6.7.9 and 7.24.2. This public draft supports the selected rules retained in C17; it is not labeled a copy of the published C17 standard.
9. Original Iranian examination repository. MSc Computer Science 1393, question 167, PDF page 34; PhD Computer Science 1404, question 72, PDF page 16. Original PDF paths, pinned repository commit and SHA-256 values are recorded with the two explicitly labeled bridge revisits. English adaptations and answers were checked independently against the scans; no official answer-key claim is made.
