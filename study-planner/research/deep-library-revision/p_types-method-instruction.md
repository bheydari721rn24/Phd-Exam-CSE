## Mathematical constructions needed by the question bank

### 1. A semantic contract precedes every calculation

A bit pattern, an exact integer, a typed C value and a rounded floating value are different objects. In a hardware word, low-bit storage is a specified map from integers to residues. In a C expression, types, promotions, sequencing and exceptional cases determine whether an operation has a value at all. In an exact-real CHOP problem, truncation is defined independently of representability in a C destination. In a decimal calculator, rounding at each node uses decimal significance. In a binary format, spacing is controlled by binary significance. Do not join these models merely because all five may display similar numerals.

For the numerical C examples, the declared contract is eight-bit bytes, no padding in the named 32-bit integer types, signed range from negative two to the thirty-first power through one less than that positive power, unsigned range zero through one less than two to the thirty-second power, and two's-complement signed representation. Exact-width typedefs are assumed available when named. These are examples, not a claim about every C17 target or the computer rendering this page. The public N1570 document is a C11 committee draft; it supplies the cited scalar rules retained in the chapter's C17 scope, and is not mislabeled as the published C17 standard.

The following pipeline is a proof procedure. Parse the expression; identify each leaf's type; apply that operator's own promotion and conversion rules; establish sequencing and reachable operations; test each intermediate's domain; evaluate defined operations; apply destination conversion only when reached. A common type can be determined from an unselected conditional alternative, while a short-circuit operand can be skipped entirely. A complete trace therefore records both static type information and actual evaluation.

### 2. Range, residues and destination conversion

For a mathematical unsigned word with $w$ value bits, the represented domain is $0\le u<2^w$. Integer-to-unsigned conversion chooses the unique residue $r$ in this domain such that
$$x=q2^w+r,\qquad0\le r<2^w.$$
Euclidean division proves existence and uniqueness. At $x=-129$, an eight-bit destination gets127; a 32-bit destination gets4294967167. The same integer has different nonnegative residues under the two moduli. This does not mean a floating-to-unsigned conversion is permitted to wrap an arbitrary negative or large real value.

Two's-complement positional decoding uses a negative weight for the sign position and positive weights below it. It proves the asymmetric endpoints and explains why negating the minimum can fail. Hardware low-bit addition can always be depicted under its own modular contract; undefined signed C addition must instead stop at a range violation. An expression such as a multiplication of narrow unsigned operands may first promote to signed `int`, so source signedness alone is not an overflow proof.

### 3. Minimum record layout is an algorithm, not a universal sizeof fact

Assume a declared ABI places each member at the earliest permitted aligned offset with no discretionary padding. Let member $i$ have byte size $s_i$, alignment $a_i$, and let $e_{i-1}$ be the preceding end offset. Define
$$o_i=a_i\left\lceil\frac{e_{i-1}}{a_i}\right\rceil,\quad e_i=o_i+s_i,\quad e_0=0.$$
If record alignment is $A$, its minimum total size is
$$S=A\left\lceil\frac{e_k}{A}\right\rceil.$$
The gap $o_i-e_{i-1}$ is internal padding; $S-e_k$ is tail padding. Each formula follows by taking the least aligned position no earlier than the occupied end, then reserving every member byte. This also proves that the record cannot end before its last member.

For widths $5,4,1$, alignments $1,4,1$, and record alignment four, the offsets are zero, eight and twelve. There are three internal padding bytes, thirteen occupied-or-interior bytes through the final member, and three tail bytes, giving size sixteen. Reordering the members to widths $4,5,1$ puts them at zero, four and nine, ending at ten and rounding to twelve. Reordering can change ABI size but is not permission to reorder fields of an existing externally specified binary format. C permits additional unnamed padding, so alignment constraints alone do not force this minimal algorithm's result. Questions24–27 explicitly adopt this algorithm rather than pretending their original alignment-only wording was sufficient.

### 4. Arrays, row stride and packed-bit storage measure different things

An actual $r$-by-$c$ array with element width $b$ contains $rc$ elements and occupies $brc$ bytes. Row stride is $bc$, and element $(i,j)$ begins at byte offset $b(ic+j)$. These formulas describe a contiguous array of arrays; they do not describe separately allocated rows behind a pointer-to-pointer object. A declared array parameter is adjusted to a pointer, so its parameter `sizeof` measures a pointer while the pointed-to row type can still describe one full row.

A packed format placing one flag in each consecutive bit of eight-bit bytes needs $\lceil n/8\rceil$ bytes. Write $n=8q+r$ and use $q+\mathbf1_{r>0}$. This proof supplies a safe computational form without adding seven near an unsigned maximum. Serialization specifies the byte/bit contract independently of implementation-defined C bit-field allocation. Member padding, array stride, pointer width and packed-byte count are not interchangeable quantities.

### 5. Floating exactness and rounding are separate proofs

For normal binary precision $p$, binade $[2^e,2^{e+1})$ has spacing $2^{e-p+1}$. All integers through $2^p$ are exact, while $2^p+1$ is not; some larger powers of two remain exact within exponent range. At $2^p$, spacing below is one and spacing above is two. A nearest-even midpoint chooses the neighbor whose retained significand integer is even. Hence binary64 rounds $2^{53}+1$ down to $2^{53}$ but rounds $2^{53}+3$ up to $2^{53}+4$.

An expression tree can round different intermediate values depending on grouping. In the authentic decimal example, both exact expression trees have sum435.003, but rounding each operation yields435.01 and435.00. Show every exact intermediate and its rounded replacement. A display rounded to two decimal places does not change the stored value's precision, and a comparison tolerance requires an application-specific absolute/relative error model rather than a universal epsilon.

### 6. Ten fully worked transfer challenges

These are independently authored extensions of the reviewed mechanisms, not copied course or official exam questions. Each answer states the additional machine contract it uses.

**Challenge A — An unsigned source can overflow signed multiplication.** Under int32 and available `uint16_t` and `uint32_t`, let `uint16_t u=65535;`. Is `uint64_t r=u*u;` safe? Both operands promote to `int` because their full range fits. The exact product is
$$65535^2=4294836225>2147483647.$$
The signed multiplication is undefined before assignment; a wider destination does not repair it. Converting one operand first, `(uint32_t)u*u`, gives common unsigned32 arithmetic and the exact product4294836225, which fits its domain. That value can then widen safely. The cast's location is the repair.

**Challenge B — Integer and floating unsigned conversions disagree.** Compare `(unsigned int)-1`, `(unsigned int)-1.0` and `(unsigned int)-0.75`. Integer conversion gives4294967295 modulo the unsigned32 range. Floating conversion discards the fractional part and requires that integer to be representable: negative one is not, so the second conversion is undefined. The third truncates to zero, which is representable, so its result is zero. No blanket rule that every unsigned conversion wraps can solve all three.

**Challenge C — Rank needs a range test.** Let `long s=-1; unsigned int u=1;`. Under a declared LP64 model with signed long64 and unsigned int32, `long` has higher rank and represents every unsigned32 value, so the comparison `s<u` is signed and true. Under a declared LLP64 model with signed long32 and unsigned int32, long cannot represent that entire unsigned range, so the common type is unsigned long32. Negative one converts to4294967295 and the comparison is false. The host operating system is irrelevant to this two-model proof.

**Challenge D — Sequencing is a relation, not precedence.** Starting independently with `int i=1;`, classify `i++ + i++`, `(i++, i++)` and `i++ && i++`. The plus operands' modifications are unsequenced, so no numeric output is specified. The comma operator sequences its left increment before its right: the returned right old value is two and the final stored value is three. Logical AND sequences the first operand, which returns one and is true, then evaluates the second, which returns two and is true; the logical result is one and final `i` is three. All increments here fit. Commas separating function arguments are not this comma operator.

**Challenge E — Parentheses cannot repair repeated side effects.** For `#define SQR(x) ((x)*(x))`, expanding `SQR(i++)` produces two increments with no sequencing relation between multiplication operands. It is undefined even though grouping is correct. A function receiving `i++` once instead captures one old value; starting at one, the call's scalar argument is one and `i` becomes two. Squaring that local one returns one. For larger inputs, the function still needs a square-range check.

**Challenge F — A representable final mathematical result is insufficient.** In int32, take $n=1073741824$. The mathematical value $-(2n)=-2147483648$ fits, but `2*n` first tries to produce2147483648 in `int`, which does not fit. The original expression is undefined. With a declared signed type able to represent both intermediate magnitudes, converting `n` to that type before multiplication makes the path valid; conversion of the final value to int32 is then permitted. A cast around the already-computed product is too late.

**Challenge G — Unsigned shifts still have domains.** Under unsigned32/int32, `1u<<31` is2147483648; `1u<<32` is undefined because the count equals the promoted left width. `1<<31` is undefined in the C17 rule used here because the signed mathematical product does not fit `int`. Right-shifting a negative signed operand is implementation-defined. Each shift promotes its operands individually and retains the promoted left type; usual arithmetic conversions do not supply a common shift type.

**Challenge H — Two binary64 ties choose different directions.** Let $a=2^{53}$. The midpoint $a+1$ has neighbors $a,a+2$, whose significand integers are $2^{52}$ and $2^{52}+1$. The lower is even, so it is selected. The midpoint $a+3$ has neighbors $a+2,a+4$, with odd and even significands respectively, so the upper is selected. The resulting values are $a$ and $a+4$, under rounding of each operation to binary64. Midpoint parity explains both without executing potentially different host evaluation rules.

**Challenge I — Trace both internal and tail padding.** For the three-member minimum ABI in section3, member widths5,4,1 yield offsets0,8,12 and end13. Record alignment four rounds13 to16. Reordering as4,5,1 yields offsets0,4,9, end10 and size12. The saved four bytes are not a missing member: the total member widths remain ten, while total padding changes from six to two. Identify every padding interval, rather than guessing one fixed amount per record.

**Challenge J — Allocation arithmetic needs guards before multiplication.** Let unsigned `size_t` maximum be $M$, positive row count $n$ and four-byte elements. The desired mathematical size is $4n(n+1)$. First reject $n=M$ before adding one. Let $c=n+1$. Check $c\le\lfloor M/4\rfloor$, then form safe row size $r=4c$. Check $n\le\lfloor M/r\rfloor$, then form total $nr$. Both divisions have positive divisors. Every multiplication is now proved within range before it executes. A wrapped small count is not evidence that the intended large array fits; a successful representability check also does not guarantee allocation succeeds.

### 7. Four freshly reviewed university roles and exercise coverage

Harvard CS50x2025 provides declaration, expression and truncation examples. Berkeley CS61C's written scalar sections provide portability, initialization and macro issues. Princeton COS126 §1.2 provides value/operation structure, Java contrasts, IntOps/DoubleOps examples and all48 displayed exercise statements in the accessible inventory. MIT6.0001 Fall2016 Lecture1 pages23–34 and its three written in-class questions provide Python objects, conversions, output and assignment snapshots. The language boundaries and corrected course generalizations are incorporated in the original exposition above and the retained tutorials. Princeton's image-only tables were inaccessible; their contents are not claimed read. Stanford CS107's earlier reading remains historical evidence because its renewal was unavailable. These four fresh roles were reassessed within the recorded bounded seven-offering pool, not selected randomly or proclaimed a global optimum.

The original course exercise inventory is a source map, not a claim that every course's full exercise bank is reproduced here. Introductory expression/assignment exercises are represented by the retained tutorials; the authored challenges extend promotions, signed domains, sequencing, layout and floating error. Whole course syllabi extend beyond this chapter boundary. Advanced C claims are cross-checked against the language reference and independent derivations because an introductory course combination alone cannot establish them.
