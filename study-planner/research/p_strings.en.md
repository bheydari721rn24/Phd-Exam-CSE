# Strings and Terminators: Representation, Contracts, and Algorithms in C17

## 1. Sources, prerequisites, and the language contract

This chapter combines four written university courses: Harvard **CS50x 2025**, David J. Malan, Weeks 2 and 4; Cambridge **Programming in C 2017–18**, Neel Krishnaswami, Lectures 2 and 3; MIT **6.087 Practical Programming in C**, Daniel Weller and Sharat Chikkerur, Lecture 5; and Princeton **COS 217**, Fall 2026, *Pointers, Arrays, and Strings*, course slides marked `@rbw500` (individual slide authorship is not independently established). Stanford **CS107's C reference sheet** is an additional contract checklist. The [source comparison](../reviews/p_strings-sources.html) states exactly which materials were accessible and read. No finite search establishes that every course worldwide has been reviewed.

The prerequisite is the arrays chapter: zero-based indexing, object extent, pointer arithmetic, loops, and asymptotic sums. Main code is **ISO C17**, not C++, C0, Python, or CS50's convenience library. Every complete function below requires the displayed headers. A parameter described as a valid string must point into a live readable character array containing a terminating zero within its accessible extent. A writable destination must additionally designate enough writable storage. These are preconditions, not properties that an arbitrary pointer can reveal.

Diagrams use eight-bit ASCII bytes and flat illustrative indices. C guarantees `sizeof(char) == 1`, but a C byte need not contain eight bits; use `CHAR_BIT` for that fact. The language does not require eight-byte pointers or ASCII letters. Defined byte operations and the stated algorithms are taught here; full Unicode segmentation, advanced pattern matching, allocator implementation, locale collation, and wide-character programming require separate chapters. This scope is explicit rather than a claim of universal examination coverage.

## 2. The abstract string and its physical representation

An abstract string over an alphabet $\Sigma$ is a finite sequence. The empty string $\varepsilon$ has length zero. Concatenation joins sequences and adds their lengths. A C string represents a sequence by consecutive nonzero character bytes followed by the first zero byte. The terminator is stored but excluded from the length.

Let a readable array have capacity $C$, and let $b_i$ be the byte at index $i$. A string starting at index zero exists exactly when a first zero occurs within that array:

$$n=\min\{i:0\le i<C\text{ and }b_i=0\},\qquad 0\le n<C.$$

Only indices zero through $n-1$ contribute to its value; index $n$ is the terminator. The remaining bytes may hold zeros, previous data, or another deliberately represented object. They are outside this string view. With `char b[8] = {'c','a','t',0,'x','y',0,0};`, `strlen(b)` is 3, `strlen(b+4)` is 2, and `sizeof b` is 8. These three quantities answer different questions.

**Why the first zero?** A C string operation receives a starting address, not an accompanying length. A sentinel supplies a stopping rule. A byte sequence containing embedded zeros cannot be completely represented by one ordinary C string. Binary data instead needs an explicit byte count. A conceptual string length has no meaning until the representation's starting position is specified.

<!-- SIM: scan -->

## 3. Four things often called null

`'\0'` is the integer character constant with value zero. Assigning it to a `char` stores a zero character. `'0'` is the character digit zero; its encoding value is nonzero. `NULL` is an implementation-defined null pointer constant macro, used to construct a pointer that points to no object. `""` is a string literal whose array consists of one terminating zero. Consequently, an empty valid string and a null pointer are entirely different inputs.

`if (s && *s)` first checks that `s` is not null, then tests its first byte. It still cannot detect a dangling or otherwise invalid non-null pointer. `strlen(NULL)` violates the library contract. Neither a zero comparison limit nor a multiplication by zero generally legalizes invalid pointers: C's string-library conventions still require valid pointer arguments unless a particular function explicitly grants an exception.

Character constants such as `'a'` have type `int` in C. Ordinary string literals have array type `char[N]`, although attempting to modify their contents has undefined behavior. C++ uses different literal constness rules; do not transfer them silently.

## 4. Declarations, initialization, and embedded zeros

```c
char a[] = "cat";             /* four bytes, writable */
char b[8] = "cat";            /* c a t 0 0 0 0 0 */
char c[3] = "cat";            /* valid C declaration; no terminator */
const char *p = "cat";        /* pointer to a literal; do not modify */
char d[] = {'c','a','t','\0'}; /* four bytes, writable */
char e[] = "ab\0cd";          /* six bytes; string length two */
```

The special character-array initialization rule permits `c[3] = "cat"` to omit the final zero when there is no room for it. This does **not** make `c` a string. By contrast, `char c[3] = {'c','a','t',0};` has too many initializers and requires a diagnostic. Initializer syntax matters.

Unspecified elements of an initialized array are zero initialized. That rule does not apply to an uninitialized automatic array. `char b[8];` does not establish a terminating zero. A static-duration array without an explicit initializer is zero initialized. Storage duration and initialization must both be read before tracing.

Escape sequences are processed during translation. `"\n"` holds a newline character and a zero, not a backslash and `n`; `"\\n"` holds backslash, `n`, zero. Hexadecimal escapes consume all following hexadecimal digits within their token. To encode ASCII A followed by B, use `"\x41" "B"`; the adjacent literal tokens join, but the escape ends at the first token boundary. `"\x41B"` is one escape and can exceed the representable range. Octal escapes consume at most three octal digits. Never count source-code glyphs as stored bytes without processing escapes first.

## 5. Array extent, pointer size, and suffix views

For `char a[12] = "hello"; char *p = a;`, `sizeof a` is 12 and `sizeof *p` is 1; `sizeof p` is the size of a pointer on the implementation. `strlen(a)` and `strlen(p)` are both 5 because they inspect the same bytes. `sizeof` is an operator on a type or expression; `strlen` is a library function on an already valid string. `sizeof` usually does not evaluate its operand; variably modified types introduce important exceptions covered with arrays.

In `void f(char a[12])`, the parameter is adjusted to `char *a`. Inside `f`, `sizeof a` measures the pointer, not the caller's array. The notation `[12]` by itself does not pass a hidden capacity. Pass capacity explicitly. An array is not a pointer object even though most array expressions convert to a pointer to their first element.

If a string has length $n$, then for $0\le k\le n$, the view `s+k` is valid and has length $n-k$. At $k=n$ it is the empty string. If its complete array extent is $n+1$, `s+n+1` is a legal one-past pointer but is not dereferenceable and is not a valid string argument. Pointer formation, dereference, and library use are separate questions. Pointer subtraction is defined only within the same array object, including its one-past position, and returns `ptrdiff_t`.

## 6. Bounded scanning and a complete invariant

The ordinary conceptual implementation of `strlen` tests $n+1$ bytes: all $n$ nonzero bytes and the terminator. That is a count for this scalar algorithm; an optimized library may load words or vectors. ISO C specifies the result, not a fixed count of machine instructions.

```c
#include <stdbool.h>
#include <stddef.h>

bool bounded_length(const char *s, size_t cap, size_t *out) {
    size_t i = 0;
    while (i < cap && s[i] != '\0') ++i;
    if (i == cap) return false;
    *out = i;
    return true;
}
```

Contract: `out` is a writable `size_t` object disjoint from the character range; `s` designates `cap` readable initialized bytes, or may be null if `cap` is zero because this **custom function** never dereferences it in that case. On failure, `*out` is unchanged. On success, the result is the first zero index. This custom null policy does not override standard-library contracts.

At the loop head, $0\le i\le C$ and every previously inspected index $j<i$ is nonzero. Initially the inspected prefix is empty. If the body runs, short-circuit evaluation has established $i<C$, so `s[i]` is readable; incrementing preserves the prefix statement. At termination, either $i=C$, proving no zero in the accessible range, or `s[i]` is zero and the prefix statement proves it is the first zero. The variant $C-i$ decreases. Reversing the conditions to `s[i] != 0 && i < cap` reads before the bound check and is unsafe at the boundary.

## 7. Copying a string and proving capacity

`strcpy(dst, src)` copies all source bytes through the first terminator. If the source length is $n$, exactly $n+1$ character assignments occur in the conceptual scalar copy. The destination needs capacity at least $n+1$, both ranges must be valid, and they must not overlap. `strcpy` returns the original destination pointer. It does not allocate memory or inspect destination capacity.

```c
#include <stddef.h>
#include <string.h>
bool copy_checked(char *dst, size_t cap, const char *src) {
    size_t n = strlen(src);
    if (n >= cap) return false;
    memcpy(dst, src, n + 1);
    return true;
}
```

Include `<stdbool.h>` as in Section 6. The source must already be a valid string, and the destination must designate `cap` writable bytes disjoint from the source. The condition $n<C$ ensures $n+1\le C$ and ensures `n+1` is representable in `size_t`. Checking only $n\le C$ loses the terminator. A capacity failure causes no write; this is stronger than truncating and then reporting failure.

For the loop copying `src[i]` into `dst[i]`, the invariant is that the first $i$ destination bytes equal the original source prefix, and the unread source has not been modified. Disjointness is the reason the second statement remains true. It is a proof obligation, not a performance suggestion.

<!-- SIM: copy -->

## 8. Bounded copy is not necessarily string copy

`strncpy(dst, src, k)` writes exactly $k$ bytes when its preconditions hold. It copies nonzero source bytes up to the bound; if it encounters an earlier zero, it pads the remaining positions with zeros. If the first $k$ source bytes are nonzero, it writes no terminator. Thus it can write a terminated string, an unterminated prefix, or zero bytes, depending on the bound.

With source `"ab"` and bound 5, the written bytes are `a b 0 0 0`. With source `"abcdef"` and bound 3, the written bytes are `a b c`. If a larger destination previously had a zero at index 3, the resulting **array** may happen to remain a string; that does not mean `strncpy` wrote that zero. Untouched bytes and written bytes must be tracked separately.

The common truncation pattern `strncpy(dst, src, cap-1); dst[cap-1]=0;` requires `cap>0`, a sufficiently readable source prefix, a writable `cap`-byte destination, and no overlap. It silently loses information unless truncation is separately detected. For explicit nontruncating behavior, prefer the checked copy above. `strlcpy`, `strnlen`, `strdup`, and `strndup` are not ISO C17 functions; platform availability must be stated. Annex K interfaces are optional and must not be assumed universally present.

<!-- SIM: bounded-copy -->

## 9. Concatenation and overflow-safe arithmetic

Let destination length be $a$, source length be $b$, and destination capacity be $C$. `strcat` overwrites the old terminator at index $a$, copies $b$ content bytes, and writes the new terminator at $a+b$. It requires $a+b+1\le C$. A scalar implementation first scans $a+1$ destination bytes, then copies $b+1$ source bytes. The resulting length is $a+b$, not $a+b+1$.

`strncat(dst, src, k)` appends at most $k$ **content** bytes and then a terminator. If the source is a valid string of length $b$, the exact requirement is

$$C\ge a+\min(b,k)+1.$$

The bound is neither the destination capacity nor the total final length. Unlike `strncpy`, `strncat` appends a zero even when it copies exactly $k$ nonzero source bytes. The destination must already be a valid string; an uninitialized destination is not repaired by concatenation.

```c
bool append_checked(char *dst, size_t cap, const char *src) {
    size_t a;
    if (!bounded_length(dst, cap, &a)) return false;
    size_t b = strlen(src);
    if (b > cap - a - 1) return false;
    memcpy(dst + a, src, b + 1);
    return true;
}
```

The earlier bounded scan establishes $a<C$, so both subtractions are safe. Comparing available space avoids evaluating a possibly overflowing sum `a+b+1`. Source and destination ranges must be disjoint. The source must remain a valid string throughout the operation. An error return is a specified result; overrunning and hoping a neighboring zero exists is undefined behavior.

<!-- SIM: append -->

## 10. Aliasing, ownership, and lifetime

For `char a[]="cat"; char *p=a; char *q=p;`, assigning `q=p` copies an address. Both pointers designate the same array. Writing `q[0]='b'` changes what both pointers observe. A deep copy uses a distinct writable array or an allocation large enough for the content plus terminator.

An allocated copy requires four steps: obtain length, ensure the size addition is safe, allocate, and check allocation success before copying. For a valid representable character array containing the string, its length cannot equal `SIZE_MAX` because its terminator also occupies an element, but explicit size arithmetic is still important when lengths originate outside such a contract. A successful `malloc(n+1)` creates owned storage; the owner eventually calls `free` once. Losing the last owning pointer leaks storage; using or freeing it again after `free` violates the lifetime contract.

Returning a pointer to an automatic local array is invalid for later use after that function returns. Returning a pointer to a string literal has static lifetime but does not authorize modification. Returning a pointer into the caller's array borrows the caller's lifetime. `const char *` prevents mutation through that pointer; it does not prove that no other alias changes the underlying mutable object.

## 11. Overlap: byte movement and direction

`memcpy` and `strcpy` require nonoverlapping copy ranges. `memmove` provides the result as if the original bytes were first saved in an independent temporary array. It neither searches for nor adds a terminator. The caller chooses the byte count. To move an entire valid string, use `strlen(src)+1` when that count and the destination extent are valid.

Suppose `char a[10]="abcd";` and we want to move its five bytes, including zero, from index 0 to index 1. A forward handwritten loop would overwrite `b` before reading it and propagate `a`. A backward loop reads the terminator first, then `d`, `c`, `b`, `a`; all unread source bytes remain intact. Moving an overlapping range left instead admits forward copying. The simulator illustrates these chosen algorithms; it does not claim that a forbidden `strcpy` call has a predictable output.

```c
/* Preconditions: pos <= n, n is the valid current length,
   n < cap-1, and the writable array has capacity cap. */
void insert_byte(char *s, size_t n, size_t pos, char c) {
    memmove(s + pos + 1, s + pos, n - pos + 1);
    s[pos] = c; /* c must be nonzero to preserve the expected length */
}
```

The moved suffix length is $n-pos+1$, including the terminator. The final length becomes $n+1$ when `c` is nonzero. Capacity is at least $n+2$. Insertion at the end moves only the old terminator. Deletion at index `pos<n` uses `memmove(s+pos,s+pos+1,n-pos)`: that count includes the terminator and produces length $n-1$.

<!-- SIM: overlap -->

## 12. Comparing values rather than addresses

`p==q` compares pointer values. `strcmp(p,q)==0` compares string values. Two separately declared arrays containing identical text are distinct objects yet have equal string values. Identical string literals may be merged; therefore pointer equality between separately written equal literal expressions must not be used as a content test.

Lexicographic order examines the first unequal pair of bytes, interpreted as `unsigned char`. If one content sequence is a prefix of the other, its terminating zero is smaller than the other's next nonzero byte. The C library guarantees only whether the result is negative, zero, or positive. It does not promise exactly -1, 0, or 1, or the exact arithmetic difference.

For two strings with longest common prefix length $r$, a straightforward comparison examines $r+1$ byte pairs, including the final equal zero pair when the strings are identical. Its running time is $\Theta(r+1)$. `strncmp(p,q,k)` examines no more than $k$ pairs and stops at a mismatch or zero. Equality for a short prefix does not imply full-string equality. `memcmp` compares a fixed byte range, including bytes after embedded zeros; its notion of equality differs from string equality.

<!-- SIM: compare -->

## 13. Character search, spans, and return pointers

`strchr(s,c)` returns the first matching position or a null pointer. The terminator participates in this search, so `strchr(s,'\0')` returns `s+strlen(s)`. `strrchr` returns the last occurrence, also considering the terminator. Always test for null before subtracting the result from the starting pointer. The subtraction is valid for an actual returned position in that same array.

`strspn(s,accept)` measures the longest initial segment containing only accepted bytes. `strcspn(s,reject)` measures the longest initial segment containing none of the rejected bytes. Neither returns a pointer. `strpbrk(s,set)` returns the first pointer to a byte belonging to a set. For `"12ab34"`, `strspn(s,"0123456789")` is 2 and `strcspn(s,"ab")` is 2. Their direction is from the beginning, not a count of all qualifying bytes.

A direct membership loop may take $O(nk)$ for text length $n$ and set length $k$. A lookup table gives $O(n+U)$ for a fixed byte universe of size $U$, with extra space $O(U)$. Index such a table with an unsigned byte. If the implementation has more than eight bits per byte, a 256-entry table is not universally sufficient.

## 14. Substring matching with an exact bound

Let text length be $n$ and pattern length be $m$. A nonempty pattern can begin at positions zero through $n-m$, but only if $m\le n$. The empty pattern matches at position zero. `strstr` returns the first match or null. Repeated matching may count overlapping occurrences; whether it does so is an algorithm policy, not a property of the word “occurrence.”

```c
const char *find_first(const char *t, const char *p) {
    size_t n = strlen(t), m = strlen(p);
    if (m == 0) return t;
    if (m > n) return NULL;
    for (size_t i = 0; i <= n - m; ++i) {
        size_t j = 0;
        while (j < m && t[i+j] == p[j]) ++j;
        if (j == m) return t + i;
    }
    return NULL;
}
```

The outer invariant states that no smaller start position is a match. The inner invariant states that the first $j$ pattern bytes equal the corresponding text bytes. Since $i\le n-m$ and $j<m$, the read index $i+j<n$. The guard `m>n` is essential because unsigned `n-m` otherwise wraps. The algorithm checks at most $(n-m+1)m$ content pairs for $1\le m\le n$, plus the two length scans. Text consisting of $n$ copies of `a` and pattern consisting of $m-1$ copies of `a` followed by `b` attains that comparison count. Early success can be much cheaper. Optimized `strstr` implementations need not use this algorithm.

<!-- SIM: match -->

## 15. Reversal and palindrome reasoning

```c
void reverse_bytes(char *s) {
    size_t n = strlen(s);
    for (size_t i = 0; i < n / 2; ++i) {
        char tmp = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = tmp;
    }
}
```

At iteration $i$, the first and last $i$ content positions already contain their final reversed values; the middle interval remains to be reversed. The pair positions differ while $i<n/2$, and the terminator at index $n$ is never touched. Exactly $\lfloor n/2\rfloor$ swaps occur, using constant auxiliary space. The empty string executes no iterations, so the expression `n-1-i` is never evaluated when $n=0$.

A palindrome test compares those same mirrored pairs and returns false on the first mismatch. Its worst-case pair count is $\lfloor n/2\rfloor$, while computing length remains linear in this representation. A loop beginning `size_t i=n-1; i>=0; --i` is wrong: unsigned values are always nonnegative and the initial subtraction wraps for an empty string. Use a half-open interval or a forward half-length loop.

<!-- SIM: reverse -->

## 16. Stable filtering with two indices

To remove a chosen nonzero byte, maintain a read index `r` and a write index `w`. Before each read, the prefix `s[0..w)` is precisely the retained subsequence of the **original** prefix `s[0..r)`, in original order, and $0\le w\le r\le n$. If the next byte is kept, write it at `w`, then increment `w`. Always increment `r`. Finally write zero at index `w`.

```c
size_t remove_byte(char *s, unsigned char reject) {
    size_t r = 0, w = 0;
    while (s[r] != '\0') {
        unsigned char c = (unsigned char)s[r++];
        if (c != reject) s[w++] = (char)c;
    }
    s[w] = '\0';
    return w;
}
```

Writing never destroys an unread byte because $w\le r$; the value being classified has already been saved. The final terminator is within the original capacity. This algorithm makes one forward pass, takes $\Theta(n+1)$ time, and uses constant extra space. Repeatedly deleting each unwanted byte with a suffix shift can take quadratic time. The value of bytes after the new terminator is irrelevant to the new string but may still be sensitive data; logical deletion is not secure erasure.

<!-- SIM: compact -->

## 17. Tokens, delimiters, and preserving empty fields

`strtok` modifies a writable string by replacing selected delimiters with zeros and saves continuation state between calls. Consecutive delimiters are skipped, so empty fields are not returned. For `"a,,b,"` split on comma, the returned nonempty tokens are `a` and `b`. It is therefore unsuitable for a format in which the empty second and final fields matter. A literal is not a writable tokenization buffer.

A nonmutating parser can represent a field by a starting offset and a length. Scan delimiters once; every delimiter ends the preceding field, including a field of length zero. After the final byte, emit the remaining field. For a string of length $n$ containing $k$ delimiters, this policy yields $k+1$ fields. Do not pass a span directly to `%s` unless it actually has a terminator; print with a suitably checked precision or copy into a terminated buffer. Nested `strtok` sequences overwrite shared continuation state. Use an explicit parser state or a documented platform-specific reentrant API when needed.

<!-- SIM: tokens -->

## 18. Input is a contract with the stream

With a writable array of capacity at least two, `fgets(buf, cap, stream)` reads at most `cap-1` bytes, retains a newline if it reads one, and appends zero on success. Check its return before interpreting the buffer. A short result can mean newline or EOF; a result without newline can be a truncated line or a final line ending at EOF. If the input contains zero bytes, `strlen` cannot recover the number of bytes read. The stream and the C-string view have different representations.

For ordinary text known not to contain embedded zeros, find newline with `strchr` and replace it with zero when present. If no newline appears, decide whether to consume the rest of that line or process a long line incrementally. Never blindly remove the last byte: the last byte may be real data when the line has no newline.

`scanf("%7s",buf)` fits an eight-byte buffer for a successful single conversion: the width limits content bytes and a terminator is added. `%s` skips leading whitespace and stops at whitespace. `%c` does not add a terminator and normally does not skip whitespace. Check the conversion count. `gets` was removed from C11 and must not be used. In a `getchar` loop, store the result in `int` so that a valid unsigned character value is distinguishable from `EOF`; only convert after checking `EOF`.

## 19. Formatting, conversion, and character classes

`snprintf(dst, cap, format, ...)` reports the number of bytes that **would** have been written, excluding the terminator, when successful. A negative result indicates an encoding error. For positive capacity, the destination is terminated when the operation succeeds, but output is truncated if the nonnegative return is at least `cap`. For zero capacity it writes nothing; its destination may be null by this specific function's contract. Do not confuse that exception with all zero-count library operations.

Character classification and case conversion functions in `<ctype.h>` accept `EOF` or an `int` representable as `unsigned char`. A plain `char` may be negative. Use `isalpha((unsigned char)s[i])` and `toupper((unsigned char)s[i])` for an ordinary stored byte. These functions can depend on locale; subtracting 32 to uppercase a letter assumes ASCII and ignores nonletters. C guarantees that decimal digits have consecutive codes, not that letters have one universal encoding.

`strtol` provides an end pointer for conversion. Set `errno=0`, call it with a valid string, reject no conversion when `end==start`, inspect `ERANGE`, and define whether trailing characters are allowed. A numerical value of zero alone does not identify failure because the valid input `"0"` also converts to zero. This is another example of preserving a result together with its status.

## 20. Byte length is not human text length

In UTF-8, one Unicode code point may occupy several bytes. Precomposed `é` occupies two UTF-8 bytes but one code point. The decomposed sequence `e` followed by U+0301 occupies three bytes and two code points, while commonly forming one displayed grapheme cluster. An ordinary C `strlen` on these byte strings reports two and three respectively, provided UTF-8 encoding is explicitly used.

Reversing bytes can break UTF-8 encoding; reversing code points can detach combining marks from their base. A user-visible reversal needs a specified grapheme segmentation policy. Locale collation can differ from unsigned-byte lexicographic order. Our ASCII simulations make memory mechanics precise; they do not claim to implement general human-language text processing. The same discipline applies to examination questions: first identify the representation and the unit counted.

## 21. Arrays of strings and command-line arguments

`char rows[3][8]` is a contiguous array of three eight-byte rows: total size 24 bytes. Each row needs its own terminator to be a string. `char *names[3]` is an array of three pointers: total size `3*sizeof(char*)`, excluding pointed-to text. Rows cannot be reassigned as whole arrays; pointer elements can be reassigned. If the pointers designate literals, changing a pointer element is permitted but modifying that literal is not.

An `argv` convention supplies `argc` pointer entries followed by `argv[argc] == NULL`. Each argument is a separately terminated string; the final sentinel is a **null pointer**, not an extra empty argument. A pointer table and the bytes it references are distinct storage. `sizeof argv` in `main(int argc,char **argv)` measures a pointer, never the number of command-line arguments.

## 22. Dynamic buffers and repeated concatenation

A length-carrying buffer can maintain $0\le L<C$, `data[L]==0`, and no earlier zero when it represents ordinary text. Cached length makes appending avoid a repeated scan of the existing prefix. Capacity growth still needs allocation and overflow checks. After a successful `realloc`, the original pointer must no longer be used; on allocation failure, the original allocation remains valid. Assigning `realloc` directly into the sole owning pointer can leak the original block on failure.

Append $k$ pieces of length $r$ to an initially empty string using a scalar `strcat` each time. Existing-prefix lengths are $0,r,2r,\ldots,(k-1)r$. The content scan cost sums to $rk(k-1)/2$, while new-content copying is $kr$. Thus the total is $\Theta(rk^2+k)$ in that model. Knowing total capacity does not remove the repeated scans. A cached end pointer makes total copying $\Theta(kr+k)$, excluding allocation costs.

When capacities double, the sum of copied prior capacities is geometric and is less than twice the final capacity. This supports amortized constant growth cost per appended byte, although an individual growth can be linear. Distinguish logical length, reserved capacity, and allocation traffic. Full dynamic-array interfaces and allocator guarantees belong to their own chapters.

## 23. Mathematical counting and examination workflow

For an alphabet of $q$ allowed nonzero bytes, exactly $q^n$ strings have length $n$. A buffer of capacity $C\ge1$ can represent lengths zero through $C-1$. Its number of distinct string values is

$$V(C,q)=\sum_{j=0}^{C-1}q^j=\frac{q^C-1}{q-1}\quad(q\ne1).$$

For $q=1$, the count is $C$. This counts **values**, not complete array states: bytes after the first zero create multiple storage states for the same value. If every byte independently comes from zero plus $q$ nonzero values, the number of arrays whose first zero is at index $j$ is $q^j(q+1)^{C-j-1}$. Arrays with no zero number $q^C$. Therefore the number of terminated arrays is $(q+1)^C-q^C$. These formulas test whether the problem concerns abstract strings or memory configurations.

Before tracing a program, write the declared array sizes and pointer relationships. Expand literals into actual bytes. Mark the first zero for each starting view. Check bounds, mutability, lifetime, overlap, signedness, and sequencing **before** calculating output. If a precondition fails, classify the program rather than inventing a deterministic result. Next write the invariant and derive exact counts for the stated loop. Finally separate an exact result, an asymptotic order, and an implementation-dependent quantity.

## 24. Consolidated summary

A C string is a bounded object viewed from a particular starting position up to its first zero. Length excludes that zero, but every string copy or append must reserve storage for it. Arrays, pointers, string values, capacities, and allocated ownership are separate concepts. The standard library takes contracts, not magical pointers that carry their own bounds. Bounded functions differ: `strncpy` pads and may omit termination, whereas `strncat` limits appended content and writes a terminator.

Correct algorithms follow directly from preserved unread data. Scanning preserves a nonzero prefix; copying preserves an equal prefix; overlapping movement preserves original source bytes by a safe direction or temporary view; comparison resolves the first mismatch; matching excludes all smaller start positions; reversal fixes mirrored ends; stable filtering maintains a retained subsequence behind the read head. These invariants justify both the code and its complexity.

For examinations, the most productive habits are to count content and terminators separately, check unsigned subtraction before use, distinguish address equality from content equality, and state the representation counted by each formula. The worked problems and final rules below develop these habits through boundary cases and combined reasoning. Their solutions establish the stated results under explicit assumptions; no chapter can guarantee an individual's result on every unseen examination question.

## 25. Fully worked mathematical and conceptual problems

The bank separates original/reconstructed training from any original-PDF-checked examination item. Source inspiration is identified without passing new problems off as university or Iranian examination quotations. Every solution explains its contract, reasoning, and boundary cases. Open solutions as needed; the application does not require answering a quiz before reading.

<!-- INCLUDE: problems -->

## 26. Examination rules and advanced pitfalls

<!-- INCLUDE: review -->

## 27. Editable memory laboratory

The laboratory executes explicitly specified byte algorithms, not arbitrary C source. Enter printable ASCII strings; `\0` inserts a zero byte. Capacity is an actual displayed array extent. It rejects invalid inputs before replacing a valid trace. Cells remain at their indices while the read/write heads move. “Reject” is the model's checked outcome, not an attempt to simulate undefined behavior. Stored zero bytes beyond the first terminator remain visible.

<!-- LAB: strings -->

## 28. References and exact reading scope

1. Harvard University. David J. Malan. **CS50x 2025**, [Week 2 notes: Arrays and Strings](https://cs50.harvard.edu/x/2025/notes/2/), relevant array, string-length, case-conversion and command-line sections; [Week 4 notes: Memory](https://cs50.harvard.edu/x/2025/notes/4/), string pointers, comparison and copying sections. CS50's `string` typedef is explicitly translated into C17 `char *` here.
2. University of Cambridge. Neel Krishnaswami. **Programming in C, Michaelmas 2017–18**, [Lecture 2](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture2.pdf), all 19 slides as extracted text, especially string reversal and counting exercise; [Lecture 3](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture3.pdf), all 25 slides as extracted text, especially pointer views, array parameters and string-search exercise. Earlier material credits Anil Madhavapeddy, Alan Mycroft, Alastair Beresford and Andrew Moore.
3. Massachusetts Institute of Technology. Daniel Weller and Sharat Chikkerur. **6.087 Practical Programming in C, January IAP 2010**, [Lecture 5](https://ocw.mit.edu/courses/6-087-practical-programming-in-c-january-iap-2010/resources/mit6_087iap10_lec05/), relevant lifetime, array, pointer-arithmetic, string and string-utility slides (PDF pages 16–26, plus review page 5). Historical platform examples are not treated as portable C requirements.
4. Princeton University. **COS 217, Fall 2026**, [Pointers, Arrays, and Strings](https://www.cs.princeton.edu/courses/archive/fall26/cos217/lectures/06_PtrArrStr.pdf), complete 32-page extracted slide text, especially physical storage, parameters, string-library example and final debugging exercise. Instructor attribution is limited to what the material establishes; course-marker metadata is not a verified individual author credit.
5. Stanford University. **CS107**, [Exam C Reference Sheet](https://web.stanford.edu/class/cs107/exams/c_ref_sheet.html), complete accessible text. Supplementary function-contract checklist; no reproduction of its restricted table or question text.
6. ISO/IEC JTC1/SC22/WG14. [N1570 C11 Committee Draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), Sections 7.24.1–7.24.6, especially zero-count arguments, copying, concatenation, comparison, searching and length. Used as an accessible primary reference for the corresponding C17 string contracts, not falsely labelled a C17 publication. Other interfaces are labelled by their separate assumptions.

See the [quality audit](../reviews/p_strings-quality.html) for independent model checks, mathematical checks, preservation of previous chapters, and the remaining limits of this delivery.
