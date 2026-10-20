# Arrays: replacement derivations, PA49–PA81

## PA49 | Value equality does not determine the sharing graph

Initially a and its outer slice b contain equal lists, so a==b is true. Their outer objects are distinct, making a is b false. The outer slice copies the references to the inner lists, so a[0] is b[0] is true.

The row-copy comprehension for c executes a separate slice for each row. Thus a[0] is c[0] is false, even though their contents initially compare equal. Appending nine to a[0] changes the shared first inner list observed through b too, but c[0] remains [1]. Its other inner row is similarly independent in this particular two-level example.

The results therefore concern four different questions: equal values, identical outer objects, shared inner objects, and the depth to which copying was performed. They should not be condensed to a statement that b is a copy while c is a deep copy without defining the reachable structure.

If a row itself contained another mutable list, row[:] would copy only that row's outer slots and still share deeper targets. The construction supplies the independence required by this exact example, not a universal recursive-copy guarantee. Identity-sensitive diagrams should draw the actual inner edges rather than duplicating every displayed bracketed value.

## PA50 | A comprehension's output expression is not its predicate

In `[x*x for x in a if x>0]`, the predicate first selects original values three and five. The output expression squares each selected value, producing [9,25], whose sum is thirty-four.

In `[x for x in a if x*x>0]`, the predicate accepts minus two, three and five because their squares are positive. The output expression is x, so it returns those original values, producing [-2,3,5]. Zero fails that predicate. The presence of a square in the filter does not make the output a square.

For the first sum, explicitly compute $3^2+5^2=9+25=34$. Summing the second output instead gives six. These are different mathematical reductions as well as different lists.

Neither comprehension mutates the input here: integer comparisons and products provide values for a newly constructed outer list. That argument depends on the particular expressions and immutable integer elements. It does not establish that arbitrary predicates are pure, or that a comprehension returning mutable elements automatically duplicates those elements. Read the filter and output expression as separate parts of the contract.

## PA51 | Count code points, encoded bytes and char elements separately

Python's s contains the code points for A and the precomposed character é, so len(s) is two. UTF-8 encodes A with one octet and this é with two, so len(s.encode('utf-8')) is three. Encoding changes the representation being counted, not the original string's code-point length.

Under the explicitly stipulated C environment with eight-bit char bytes and UTF-8 execution encoding, an array holding these encoded bytes plus its terminating zero needs four char elements. Its C string byte length is three, excluding that zero. The four storage elements do not mean four displayed characters.

An ordinary C source literal with non-ASCII text is not guaranteed to use UTF-8 on every implementation. The stipulated encoding and byte width make the requested char-element count unambiguous; a C type name is not itself a count of human-readable character units.

For more complex Unicode text, code points need not coincide with grapheme clusters either. The stated precomposed é makes this example unambiguous, but a combining sequence could display similarly with another code-point count. Byte and code-point indices cannot be exchanged in a bounds proof without an explicit decoding map.

## PA52 | The first zero ends a string, not its array object

The intended C declaration is:

```c
char s[8] = {'a', 'b', 0, 'c'};
```

The declaration creates eight char elements, and sizeof(char) is one C byte. Thus sizeof s is eight. Its explicit values occupy indices zero through three; the omitted initializer entries four through seven are zero-initialized.

The first zero starting at s is at index two, so strlen(s) is two. Index three still exists and contains the initialized character 'c'. A direct in-bounds read of s[3] is valid even though it is beyond the end of the string beginning at s.

No later character extends that first string past its terminator. Starting a different string operation at s+3 would instead see 'c' followed by the zero at index four and have length one. The array's capacity, the selected starting pointer and the first accessible zero jointly determine which string is observed.

The declaration's character literals denote actual initialized elements; the numeric zero denotes the first terminator. Keep those roles separate when locating any later string starting elsewhere in the same array.

## PA53 | C permits a character array with no spare terminator slot

In C17, char a[3]="cat" is permitted: the three available elements receive 'c', 'a' and 't', and the terminating zero is omitted because the declared bound leaves no room. The declaration itself is not the same as a valid zero-terminated string.

The inferred array b from char b[]="cat" has four elements, including the zero at index three. Therefore sizeof b is four and strlen(b) is three. In contrast, strlen(a) lacks an accessible terminator within a's object and cannot be assigned a portable result. An unrelated zero in conveniently adjacent storage does not repair the interface precondition.

The distinction is specifically the stated C initialization rule; a C++ question needs its own language analysis. Replacing a's bound by four would provide the missing terminator, while simply casting a to another pointer type would not.

If the intent is to store exactly three nonterminated character elements, a is a valid buffer representation, but use operations with an explicit length rather than unbounded string scanning. Capacity and initialization establish real elements; the additional zero-termination contract determines whether a C string function may consume them.

## PA54 | Equal initial contents can have different modification contracts

The declaration char a[]="cat" creates a writable four-element character array initialized from the literal's characters and terminating zero. Assigning a[0]='b' changes that array's first element and gives the string "bat". Its last zero remains intact.

The pointer p instead designates a string-literal array containing "cat". It does not designate a merely because the initial displayed characters matched. It still observes "cat" after a is changed. C string literals are not valid modification targets; casting away the written const qualification does not make their storage writable under the language rules.

The result depends on object origin and access contract, not only the pointer's apparent type. A cast can alter which type an expression presents, but cannot create a different backing object or extend its lifetime.

sizeof a counts four char elements; sizeof p measures a pointer object and depends on the implementation. strlen(a) and strlen(p) both return three after the assignment because each first string still has three nonzero character bytes. Those equal lengths do not establish shared identity or permission to perform the same writes.

## PA55 | The bound test must precede every read

Use a loop whose guard checks the capacity first:

```c
size_t k = 0;
while (k < capacity && a[k] != 0) ++k;
bool found_zero = k < capacity;
```

Assume a names capacity readable initialized char elements, or capacity is zero and no element access is required. Short-circuit evaluation means a[k] is read only after k<capacity succeeds. At every boundary, all earlier tested positions are nonzero and $0\le k\le\operatorname{capacity}$.

For [65,66,67,0,88], the first three tests advance k, and the test at index three finds zero. The result is k=3 with found_zero true. For [65,66,67,88,89], all five values are nonzero; k reaches five and the bound stops the loop before a[5] is read. The status is false.

The latter k is a scanned buffer extent, not a verified zero-terminated string length. Returning it without status could incorrectly authorize an unbounded string function. Swapping the guard operands would lose the boundary protection and attempt an invalid endpoint access in the unterminated case.

## PA56 | Charge matching characters as well as mismatches

The text length is six and the pattern length four, giving candidate starts zero, one and two. At start zero, the first three 'a' comparisons succeed, and the fourth compares text 'a' with pattern 'b', failing. That candidate costs four comparisons.

At start one, the same three successes precede another fourth-position mismatch, for four more comparisons. At start two, all four characters match "aaab" and the search returns index two. The total is $4+4+4=12$ character comparisons.

The usual naive upper bound $(n-m+1)m$ equals twelve here and is attained. Counting only the two mismatch events omits ten successful equality tests. Counting loop guards as character comparisons would instead charge a different operation and must be stated separately.

No later candidate is explored after the first match. An explicit trace should identify the candidate start and current pattern position together, because the same text character can be compared during different candidates. More efficient search algorithms reduce this repeated work, but they are a different implementation; their costs cannot be silently substituted for the specified left-to-right naive search.

## PA57 | Resolve empty and too-long patterns before subtraction

Under the stated first-match convention, the empty pattern matches the text at boundary zero and requires zero character comparisons. This is a boundary match; it does not demand an element from an empty pattern.

The pattern "abcd" has length four while text "abc" has length three. No nonnegative candidate start can leave room for all four pattern characters, so the search reports no match immediately, without comparing any character.

When n and m are size_t, compute n-m only after establishing m<=n. Otherwise its unsigned interpretation or later conversion can produce a large apparent range instead of the intended negative mathematical difference. A safe control structure first handles m=0, then m>n, and only then visits starts from zero through n-m inclusive.

For each remaining candidate and each pattern position j<m, those conditions establish start+j<n. The proof must also choose machine arithmetic that cannot overflow while constructing the index. A return convention for failure must be explicit, for example a separate success flag and index or a defined sentinel. The problem's length rejection does not itself choose a universal C return type.

## PA58 | Reserve one real element for the terminating zero

The old string length is four and the suffix length four. The required resulting storage is $4+4+1=9$ char elements: eight visible bytes plus one zero. With capacity nine, copy suffix characters into indices four through seven and store zero at index eight. The final string is "abcdwxyz".

Capacity eight has no element at index eight. It can hold those eight nonzero bytes as a buffer but not that complete terminated string. Treating the one-past boundary as a spare terminator slot is precisely the off-by-one error.

The argument assumes both source and destination strings have already been validated to their respective accessible zeros. It must also respect any overlap restrictions of the selected copying operation. Sufficient destination capacity does not make overlapping strcpy-style use valid.

For a general overflow-safe capacity check, first establish old_length<capacity, reserving its current terminator, then require append_length<=capacity-old_length-1. This avoids forming an unchecked old_length+append_length+1. The numerical nine-byte example fits easily, but the subtraction-based contract transfers safely to large machine sizes.

## PA59 | Pointer sentinels and character terminators are different levels

With argc equal to three, argv[0], argv[1] and argv[2] point to the three argument strings. The third is "yz", so argv[2][1] is 'z', and argv[2][2] is its terminating zero character. The second access remains within that string's actual storage.

argv[3], at the boundary argc, is a null pointer sentinel. It is not a pointer to an empty string. Attempting argv[3][0] would perform indirection through that null pointer and is invalid.

A faithful diagram therefore has an outer array of pointers ending in a null pointer, and separate inner character arrays each ending in a zero character. The outer null is not another argument, while an inner zero is an actual element of its string storage.

This distinction also explains why argv is not a contiguous rectangular character matrix. Argument lengths differ and the outer elements are pointers, so advancing one outer position and one inner position use different types. Report the character values rather than assuming their numeric encoding, since no ASCII code table is needed for the requested identity of 'z'.

## PA60 | Repair the ctype argument domain before interpreting text

Under an implementation where the stored non-ASCII byte promotes to a negative int distinct from EOF, passing it directly to toupper violates that function's domain. Its valid inputs are EOF and values representable as unsigned char. Plain signed char values do not automatically meet that contract.

For a byte obtained from the char array, use `toupper((unsigned char)s[i])`. Converting before the function call produces the corresponding unsigned-byte value, which integer promotion then presents in the valid domain. Casting the returned value afterwards would be too late to repair the argument.

This is distinct from preserving the EOF result of an input function, which must be tested as int rather than prematurely narrowed to char. The example's value is a stored byte, not an EOF-bearing input result.

The conversion solves the library precondition, not Unicode uppercasing. A byte can be part of a multibyte UTF-8 sequence, and locale-sensitive byte conversion need not map a whole code point. An ASCII-only arithmetic exercise has a narrower explicit domain and cannot justify feeding arbitrary negative char values to ctype functions.

## PA61 | An interior search result is borrowed storage

A successful search returning an interior pointer identifies an element of the caller-supplied text object. It allocates no new character array and does not automatically transfer ownership. To read the result later, the original object must remain alive, the selected access must stay within its object domain, and the characters being read must have usable initialized values.

If the owner frees or successfully reallocates the backing allocation, a saved interior pointer is not preserved as a valid access handle. Mutating the text without ending its lifetime can also change what a still-valid pointer observes; stable location is not a promise of stable contents.

An interior pointer is not generally the owning pointer returned by an allocator and cannot simply be passed to free. Ownership must remain with the interface that owns the complete allocation. A returned pointer into a callee's ordinary automatic buffer is worse: that buffer ends its lifetime on return, so subsequent access has no valid referent.

Returning a position plus explicit success status can make borrowing clearer, but using that position still requires a live compatible text object. Observed unchanged bytes or a plausible numeric address cannot extend an expired object's lifetime.

## PA62 | Count copying, insertion writes and peak storage separately

Starting at capacity one, appends that exceed capacities one, two, four and eight allocate capacities two, four, eight and sixteen. They copy respectively one, two, four and eight live elements. Thirteen successful appends therefore finish at logical length thirteen and capacity sixteen.

Total copied elements are $1+2+4+8=15$. The thirteen new values each require another write, giving twenty-eight element writes in the specified model. Initial reservation does not copy an element, and no extra growth occurs merely because an append exactly fills the current capacity.

During the final allocate-copy-release expansion, the old capacity-eight block and new capacity-sixteen block coexist, giving peak backing storage twenty-four slots. This differs from both the final capacity sixteen and final logical length thirteen.

The ninth append alone copies eight old elements before storing its new value, so it has linear cost in the previous length. A constant amortized cost distributes expansion work across a whole sequence of operations; it is not a constant upper bound on that single append. The count assumes successful allocations, unit-cost element assignments and explicit coexistence, rather than an allocator that can extend a block in place.

## PA63 | A geometric total bounds a sequence, not each operation

If final capacity c is a power of two, the expansion copies are one, two, four and so on through c/2. Their sum is c-1. At c equal to one there are no expansions and the empty sum is zero, also c-1.

For positive final length n, c is the least power of two at least n. Thus $n\le c<2n$. The copied-element work c-1 is less than 2n, and including n stores of new elements gives less than 3n. Dividing that sequence cost by n establishes a constant amortized bound under the unit-copy model.

When n itself is a power of two, c=n and the exact copy total is n-1. Just after a threshold, for example n=9, capacity jumps to sixteen and copying totals fifteen, illustrating why copy work is not always n-1.

The proof assumes no deletions, failed operations, or costly nested copy behavior. Counting initial allocation, allocation latency or constructor work would require an enlarged cost model. A uniform bound on total assignments does not establish a physical time bound independent of element type, nor eliminate an individual expansion's linear copying cost.

## PA64 | Fixed additive growth gives an arithmetic series

With initial capacity three, the fourth, seventh and tenth appends trigger expansions to six, nine and twelve. They copy three, six and nine existing elements. After twelve appends, final capacity is twelve and total copied elements are eighteen. New-value stores contribute another twelve, for thirty assignments in this model.

For n=3m appends, expansions copy $3,6,\ldots,3(m-1)$. Their total is

$$3\sum_{j=1}^{m-1}j=\frac{3m(m-1)}{2}=\frac{n^2}{6}-\frac{n}{2}.$$

Adding n new-value stores retains quadratic growth of total work and gives a linear, rather than constant, average cost per append as n grows.

The exact endpoints matter: reaching length three uses the initial block without expansion, and reaching length twelve exactly does not allocate fifteen. An implementation that expands proactively on becoming full would have a different count. The stated policy expands only before an append that would exceed capacity. Fixed additive increments cannot use the geometric-series argument for doubling because successive copied sizes differ by a constant rather than a fixed ratio.

## PA65 | A growth factor trades copying against reservation

Tripling from capacity one copies one live element to capacity three, three to capacity nine, and nine to capacity twenty-seven. The tenth append needs that final expansion, so copy work is thirteen. Adding ten stores of new values yields twenty-three element writes, with seventeen spare slots at completion.

Doubling for the same length reaches capacity sixteen and copies $1+2+4+8=15$ elements, giving twenty-five total writes and six spare slots. Under these exact conventions, tripling performs two fewer copied-element writes but reserves eleven more final slots.

Neither comparison ranks a growth factor universally. Peak simultaneous storage, allocation costs, future append count, element-copy expense and memory limits can change the preferred objective. For instance, allocate-copy-release tripling from nine to twenty-seven temporarily holds thirty-six slots, versus twenty-four at doubling's last expansion here.

Every fixed multiplicative factor greater than one yields a geometric copied-work series and therefore linear total copying under the simple model. Its constants and unused-capacity bounds differ. A claimed efficiency result must name which quantity is minimized; an asymptotic equivalence does not imply equal practical costs or equal memory use.

## PA66 | Identify the evaluated type before locating overflow

The mathematical request is representable in the stipulated size_t exactly when $8n\le65535$, giving $n\le8191$. The maximum valid count requests 65528 bytes. At n=8192 the mathematical request is 65536, which cannot be represented by that size_t.

It is not sufficient to assert that multiplication necessarily wraps merely because SIZE_MAX is 65535. If size_t is a narrower unsigned type and int can represent its full range, integer promotions can evaluate the product in a wider int and obtain 65536 exactly. Conversion of that value to the stipulated size_t, for example for an allocation argument, then reduces it to zero. An explicitly sixteen-bit unsigned evaluated product can instead wrap during the multiplication itself.

Once the invalid result has been stored as size_t, comparing it with SIZE_MAX cannot recover the lost high bits; every such stored value already lies within the type's range. A genuinely wider untruncated product can be checked, but that is a different computation.

Use the precondition n<=SIZE_MAX/sizeof *p before constructing the allocation count. This proves representability of that count, not allocation success, object initialization or lifetime. These remain separate obligations.

## PA67 | Preserve the owning pointer until positive-size success

Assume new_bytes is positive. On allocation failure, realloc returns null and the original allocation remains available. If p is its only saved owning pointer, assigning `p = realloc(p,new_bytes)` overwrites that pointer with null and can lose the ability to release or use the still-live block.

Use a temporary result:

```c
void *next = realloc(p, new_bytes);  /* new_bytes > 0 */
if (next != NULL) {
    p = next;
    /* Recompute any required interior pointers from the new allocation. */
} else {
    /* p still owns the original allocation. */
}
```

On success, use the returned allocation pointer. The prior allocation's lifetime has ended; old owning and interior pointer values are not preserved as valid handles even if the observed numeric address happens to be unchanged. Reestablish positions from saved offsets under the new size bounds.

On positive-size failure, previously valid interior pointers remain tied to the original live allocation. The guarantee must not be generalized to every null result of a zero-size request. Handle that C17 corner separately, and validate byte-count arithmetic before the call rather than treating allocation failure handling as an overflow repair.

## PA68 | The declared implementation copies some elements twice

The full sequence has eight live elements and no spare slot. Its expansion allocates sixteen slots and copies all eight old values. The old eight-slot block coexists until release, giving a peak of twenty-four backing slots.

Insertion at index two then shifts the six old elements at indices two through seven one position right, in descending order. A final store writes the inserted value. The declared expand-then-shift strategy therefore performs $8+6+1=15$ element writes and ends at logical length nine.

The descending suffix movement protects unread values, while expansion itself preserves the entire old logical prefix in separate storage. These are two different preservation arguments, even though some elements participate in both sets of writes.

A different implementation can allocate the new block and copy each old element directly to its final side of the insertion gap, reducing repeated assignments. That possibility does not change the requested fifteen, because the question explicitly selects the first strategy. Exact operation counts must follow the stated execution rather than silently substituting a more efficient algorithm with the same final sequence.

## PA69 | Avoid immediate growth-shrink oscillation

Begin with five values in capacity eight. Deleting the fifth value leaves four and immediately triggers the stipulated shrink: four remaining elements are copied to capacity four. Re-appending a fifth value finds that block full, copies those same four elements to capacity eight, then stores the new value.

Each delete/append pair therefore copies eight elements and writes one new value, repeatedly allocating and releasing blocks even though logical length changes by only one. In a scaled version with thresholds c/2 and c, one such opposing pair can copy a quantity proportional to c without many intervening operations to pay for it.

A smaller shrink threshold supplies hysteresis. For example, after shrinking from c to c/2 at length c/4, the new block is half full and many appends can occur before expansion. The exact amortized proof must state the growth/shrink factors and minimum capacity, rather than merely suggesting a threshold informally.

The example concerns resize copies, separate from the cost of deleting a middle element. Its fifth-item deletion can remove the last logical element without shifts, yet the resize policy still creates the repeated copying overhead.

## PA70 | Equal element counts can have different line-fill counts

Each row contains eight four-byte elements, exactly thirty-two bytes, and the first row starts on a line boundary. Therefore each complete row occupies one cache line. A cold row-major traversal fills that line once and reuses it for the remaining seven elements, giving eight fills across the eight rows.

Column-major traversal reads one element from each of eight different row lines before returning to the next column. Each next row access requests a line different from the sole resident line and therefore misses. Returning to the first row at the next column also misses, so all sixty-four element reads cause fills.

Both loops perform sixty-four element accesses. The counts eight and sixty-four describe misses under the explicitly cold, one-line, no-retention model, not different arithmetic complexity.

Alignment, capacity and replacement assumptions are essential. A cache able to retain all eight row lines can reuse them across columns; a different starting alignment can make a row cross a line boundary. Real hardware may also prefetch. None of those alternative models should be silently added to this exact counting exercise.

## PA71 | Include the initial partial cache line

Eleven consecutive four-byte elements cover forty-four bytes. Beginning eight bytes into a sixteen-byte line, they occupy the inclusive byte interval eight through $8+44-1=51$ relative to that line's start.

The first line index is floor(8/16)=0 and the last is floor(51/16)=3, so four distinct lines are touched: intervals 0–15, 16–31, 32–47 and 48–63. The first and final selected portions are partial lines.

Rounding forty-four divided by sixteen upward gives three, which would suffice only for a suitably aligned starting interval. It ignores the eight-byte starting displacement. For positive length n, the general count is

$$\left\lfloor\frac{B+nw-1}{L}\right\rfloor-\left\lfloor\frac{B}{L}\right\rfloor+1.$$

Handle n=0 first: no byte is accessed and no line is touched. In machine code the positive-case endpoint expression also requires nonoverflowing address arithmetic. The count concerns distinct lines for the contiguous read interval under the stipulated model; cache conflict behavior of a different noncontiguous traversal requires another analysis.

## PA72 | Logical order wraps while physical slots remain fixed

With head five and capacity seven, logical offsets zero, one, two and three map to physical indices $(5+t)\bmod7$, namely [5,6,0,1]. Their logical adjacency crosses the physical end without moving any slot. The next append position is $(5+4)\bmod7=2$.

If a separate length is stored, empty means length zero and full means length seven. In both cases the tail boundary can equal the head, so head=tail alone cannot distinguish them. A reserved-empty-slot representation resolves ambiguity differently and reduces the usable capacity; it must not be mixed with the present length-counted representation.

The general proof requires positive capacity, a head in zero through capacity-1, and a logical length between zero and capacity. Every valid logical offset then maps into a physical slot, and offsets within one capacity are distinct modulo it.

In fixed-width code, the mathematical formula does not automatically justify an overflowing head+length intermediate. Use a safe conditional wrap or a sufficiently wide representation. The small values here are safe, but modulo after overflow is not a universal repair for arbitrary capacities.

## PA73 | A rectangular transpose can contain a long cycle

Decode source offset as (i,j) in a two-by-three shape and encode its transpose as (j,i) in a three-by-two shape. The original-to-destination map is [0,2,4,1,3,5]. In particular, one goes to two, two to four, four to three and three back to one.

The nontrivial cycle is therefore 1,2,4,3,1. Positions zero and five are fixed. For original values [a,b,c,d,e,f], a separate destination becomes [a,d,b,e,c,f]. An in-place cycle algorithm can save b, place it at destination two while saving the displaced c, then continue through four, three and one.

A square transpose's pairwise swaps rely on the source and destination having the same row extent. Here the row width changes from three to two; the physical permutation has a four-cycle rather than only two-cycles. Treating every coordinate pair as one symmetric swap can therefore revisit or misplace values.

The inverse transpose uses the swapped shape, not the same original flattening map a second time. This distinction separates a mathematical coordinate involution from the physical permutations expressed in different source and destination layouts.

## PA74 | Invert the triangular prefix with exact inequalities

Lower row i begins at triangular offset $T_i=i(i+1)/2$ and contains i+1 values. Find the unique i satisfying $T_i\le17<T_{i+1}$. The starts are 0,1,3,6,10,15,21, so row five owns seventeen. Its column offset is $17-15=2$, giving (5,2).

The containing matrix needs at least six rows, and the recovered column satisfies zero<=2<=5. If a finite matrix order were supplied, its total packed length would also need to exceed seventeen; inversion does not independently prove that the allocation exists.

An exact binary search over triangular starts locates the row without floating rounding. Alternatively, arbitrary-precision integer square-root arithmetic can supply a candidate that is verified against both inequalities. An unchecked floating square-root formula can round incorrectly near a large triangular boundary.

Even an integer search must avoid overflowing i(i+1) before dividing by two. Use suitable width or divide an even factor before multiplication with a remaining range check. The final packed offset fitting in a type does not prove every candidate product evaluated during inversion fits that same type.

## PA75 | Sum the triangular region's row lengths

For a fixed i from zero through n-1, the indices strictly above it are i+1 through n-1, giving n-i-1 possibilities. Summing these row lengths yields

$$\sum_{i=0}^{n-1}(n-i-1)=\frac{n(n-1)}{2}.$$

Including i=j adds one pair for each of the n rows, giving n(n+1)/2. At n=5 the respective counts are ten and fifteen. At n=0 both are zero, and at n=1 only the included-diagonal region has one pair.

The full n-by-n rectangle instead has n squared ordered positions: it includes both orientations of off-diagonal pairs as well as the diagonal. For a square transpose, selecting only i<j visits each unordered off-diagonal pair once, giving exactly the required swap count rather than swapping each pair twice.

These are mathematical products. To implement the count in a finite type, divide the even factor before multiplying or use an appropriate wider checked representation, and establish that the resulting count itself fits. If n is an unsigned zero, blindly forming n-1 can underflow before a later multiplication by zero; handle that empty case explicitly.

## PA76 | A missing length argument does not imply missing information

For an arbitrary array that may be empty, an unconditional A[0] access is not proved safe merely because an array parameter exists. If ordinary C0 code has no accessible length information and the interface gives no other promise, it cannot justify even its first read.

A stronger precondition can change the answer. If the caller guarantees at least one accessible initialized element, a function returning A[0] is useful and safe without receiving a separate numeric length parameter. A guaranteed sentinel within accessible storage can similarly justify a particular scan; a sentinel that might be absent cannot.

The negative conclusion in the course exercise must therefore be read under its unconstrained interface. It is not a universal impossibility theorem for every array-related function lacking a length argument. Nor does a contract magically expose hidden allocation metadata: it supplies an assumption the caller must establish.

For C, ordinary pointer/array parameters likewise carry no automatic runtime extent. The intended domain can be conveyed through a length, a stronger fixed-bound contract, a validated container, or a valid terminator convention. Each option needs an explicit proof of safe access and termination under its actual promises.

## PA77 | Final cancellation does not excuse an earlier signed overflow

The mathematical partial sums in the specified order are 2147483647, then 2147483648, then 2147483647. The second exceeds the maximum signed thirty-two-bit value. Thus straightforward C int accumulation is not safe even though the final mathematical total fits.

Signed overflow is not a promised wraparound result. A convenient numerical output from a particular compilation cannot validate this execution. The loop invariant needs both equality to the mathematical processed-prefix sum and representability of the next addition.

A wider accumulator whose range covers every partial sum can compute this example safely. Alternatively, before adding a positive x require current<=INT_MAX-x, and before a negative x require current>=INT_MIN-x, with correctly typed bounds and operations. Merely checking the completed total after overflow is too late.

Reordering this particular input to cancel one with minus one first avoids its overflow, but arbitrary reordering is not a general safety proof and can change other algorithms' semantics. An absolute-sum bound supplies a sufficient wider-range argument, although it may be conservative. Distinguish mathematical addition identities from the evaluation order and representation of a concrete implementation.

## PA78 | Skip the empty case before forming a high index

An executed iteration has $0\le i<\lfloor n/2\rfloor$, so n is at least two. The low index i is below n. For the high index, i>=0 implies n-1-i<=n-1, and i<=n-1 implies n-1-i>=0. Both selected positions therefore exist.

They are distinct: the loop bound gives $2i<n-1$ for every executed pair, so i lies strictly below its reflected partner. For odd n, the center (n-1)/2 is excluded; pairing it with itself would not contribute a reversal swap.

For n=0 or n=1, the iteration range is empty. A concrete implementation must preserve this evaluation order: test the loop guard before calculating n-1-i for an access. Precomputing an unsigned n-1 before checking the empty case is a different program and needs another argument.

There are exactly floor(n/2) pairs. Their low positions are distinct, their high positions are distinct, and no low position equals a high one. Consequently every off-center element participates once, providing the disjoint-pair structure used by a reversal invariant.

## PA79 | The largest required square occurs at the final filled index

At boundary i, maintain $0\le i\le n$ and the relation $B[k]=(k+1)^2$ for every k<i. Initially the filled prefix is empty. If i<n, index i exists and storing (i+1) squared extends the relation through that index. Incrementing i restores the invariant; n-i proves termination. At i=n, all required positions are correct.

The positive values increase with k, so the largest stored value is n squared for n>0. For signed thirty-two-bit multiplication,

$$46340^2=2147395600\le2147483647<2147488281=46341^2.$$

Thus n may be at most 46340 under that implementation model. This also keeps i+1 representable for each executed body, but the array's allocation size and success remain separate checks. On an implementation whose int is narrower, the explicitly thirty-two-bit assumption cannot be dropped.

For n=0 the abstract fill performs no access and needs no value square. A standard C fixed or evaluated variable-length array declaration still needs a positive bound; use another empty-sequence representation. The proof establishes the filled logical prefix, not permission to inspect uninitialized spare storage.

## PA80 | Translate a relative offset into an absolute array position

Let p correspond to position r of the same live n-element array, allowing r=n only as its one-past boundary. The subscript p[k] selects position r+k, so its element-access domain is

$$0\le r+k<n\quad\Longleftrightarrow\quad-r\le k\le n-1-r.$$

Pointer formation without evaluated element indirection also permits position n, extending the upper bound to n-r. The lower bound does not change. Both inequalities describe mathematical index displacements; the actual C operands must also have suitable representable integer values.

If r=0, only nonnegative element offsets through n-1 are accessible. At an interior position, some negative offsets are valid. If r=n, offsets from minus n through minus one can reach elements, but k=0 cannot be dereferenced. These cases explain why the sign of a written subscript alone does not decide validity.

The same-array and lifetime premises are essential. A numerically convenient address into another allocation does not acquire this domain, and an expired object's old pointer cannot be justified by substituting a former r. This gives the complete condition behind isolated negative-index examples rather than a memorized special case.

## PA81 | Convert before division, and prove accumulation safety

The three integer scores sum to twenty-five. Dividing this integer numerator by integer three gives eight. Dividing by the floating operand 3.0 converts the operation to floating arithmetic and produces an approximation to 25/3, about 8.3333333333 in ordinary double arithmetic.

Casting the integer result eight to double afterwards gives 8.0; it cannot recover the discarded fraction. A cast on the numerator before division or a floating divisor changes the division itself, which is the relevant operation.

A general average requires positive logical length to avoid division by zero, accessible initialized elements for the whole scan, and a safely represented accumulator. A correct final average does not prove that a preceding signed integer sum avoided overflow. A floating accumulator has its own precision and range limits, while a wider integer accumulator needs a bound covering every partial sum.

The supplied three values are small, so the concrete sum is safe. The interface argument must not silently generalize that convenience to arbitrary scores or lengths. An array-shaped parameter supplies neither a runtime length nor proof that the caller passed a nonempty initialized sequence.
