# Independent mathematical and language audit: p_types

Date: 12 October 2026. All **45 current question placements**, their stems, options and previous answers were individually read using `read_deep_revision.py` in ranges 1–14, 15–32 and 33–45. No shared chapter, gate, solution manuscript or publication file was changed. No undefined C expression was executed to infer its result. This report is not a completed chapter or an assurance of universal coverage.

## 1. Source inspection and language-reference scope

Three original exam pages were freshly rendered and actually viewed:

| Authentic item | PDF page | Original SHA-256 |
|---|---:|---|
| Phd_CE_1405_Q31 | 8 | `34d7e4f8f1d347be2ede1be4ff027efc2e17680c3aedf633a13857f27955b75a` |
| MS_CS_1393_Q165 | 33 | `7ed89fae8eb601a964355fde5e5d297cbb30844e5240b9e3908b798fb86e349d` |
| MS_CS_1404_Q51 | 11 | `53719e256f35b9acb43bfa87062a7c0fb20f1e4b3f9e0fa9c688e74e4a0ec26f` |

These hashes were independently recomputed from the cached repository PDFs and matched canonical metadata. Images are in `C:/Users/bheydari/AppData/Local/Temp/deep-types-audit-sources/`. No numerical source-transcription error was identified in these three items. Q2's wording must make clear that its false option claims **truncation**, although the offset formula performs rounding. The source's positive-x conditions need not be silently broadened when quoting it; extending the formula to x=0 is a separate valid observation.

The official [WG14 N1570 document](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf) was freshly consulted through the web tool. It is the **12 April 2011 C11 committee draft**, not the published C17 standard. It supplies clause references for the stable rules used in this C17-oriented audit. The attempted local download failed DNS resolution; no local downloaded N1570 hash or local-PDF inspection is claimed.

Freshly read clause locations:

| N1570 clause | Rule location used |
|---|---|
| 6.2.5 p9; 6.2.6.2 | Unsigned arithmetic and integer representation |
| 6.3.1.1 p2 | Integer promotions |
| 6.3.1.3; 6.3.1.4 | Integer conversions; floating/integer conversions |
| 6.3.1.8 | Usual arithmetic conversions |
| 6.3.2.1 p3 | Array conversion |
| 6.5 p2,p5 | Unsequenced effects and exceptional arithmetic |
| 6.5.3.3 p4 | Complement after promotion |
| 6.5.3.4 | Sizeof and variable-length operands |
| 6.5.5 p5,p6 | Division/remainder |
| 6.5.7 | Shift constraints |
| 6.5.13; 6.5.15 p4,p5 | Short circuit; conditional evaluation/type |
| 6.7.2.1 p11,p14–17 | Bit-field allocation; structure alignment and permitted padding |
| 6.7.6.3 p7 | Array-parameter adjustment |
| 6.10.3.1 | Macro argument substitution |

The clauses were read at the relevant portions of PDF pages 57, 62–63, 67–71, 93, 106–109, 111–117, 131–132, 150 and 185. No complete reading of the 701-page document is claimed.

## 2. Explicit models and required repairs

### Distinguish the five models

1. **Hardware representation:** mathematical fixed-width bit patterns and low-bit modular storage, independent of C expression semantics.
2. **C17 integer-expression model:** when numerical 32-bit results are requested, state CHAR_BIT=8, no padding in int/unsigned int, signed range [-2^31,2^31−1], unsigned range [0,2^32−1], two's-complement int, and availability of named exact-width types.
3. **Exact-real CHOP model:** truncation toward zero without binary floating error or conversion range limitations.
4. **Decimal floating model:** normalized significand with one integer digit and four fractional digits, rounded after every operation.
5. **Binary floating model:** p significant bits and adequate exponent range; binary64 questions additionally specify p=53, nearest-even and each operation rounded to binary64.

LP64 is not required by any existing numerical answer. If introduced for extensions, declare 64-bit long and pointers, 32-bit int, eight-bit bytes and the relevant no-padding ranges explicitly. Windows LLP64 is a different model; do not infer LP64 from the current host.

### Q24–27 layout is under-specified unless minimum padding is stated

Member widths and alignment requirements do not force one unique C structure size. A conforming implementation can insert extra unnamed padding. The intended formula uses **each member at the earliest aligned offset, no discretionary padding, then final size rounded up to record alignment**. Add those words to the authored model. At n=5, second-member offset 8 and total size 12 are the minimum; offset 12 and total size 16 also respect the stated alignments without the minimum-layout requirement. The current key is an intended minimum-layout answer, not an unconditional portable-C sizeof fact.

### Q40–43 arithmetic domains

The statement “all values fit” should explicitly include evaluated intermediates. For this particular family with int32 and positive n, the safe range is 1≤n≤715827882; at its upper endpoint 3n+1=2147483647. No counterexample to the given family arises by claiming a valid final dividend at n=715827883: the mathematical dividend would already be -2147483650, outside the range. A separate valid illustration of hidden intermediate overflow is `-(2*n)` at n=1073741824: the mathematical final value is INT_MIN, but evaluating `2*n` as signed int exceeds INT_MAX before negation.

### Other clarification points

- Q5 options' 7/3 must denote the mathematical target approximated in double, not an exact representability promise.
- Q9 already excludes excess precision by demanding binary64 rounding of every operation; retain that premise.
- Q11's macro directive must be displayed on its own source line; the explanatory prose is not part of the replacement list.
- Q28–31 describe an **actual array object**, not an adjusted parameter or a pointer object. Row count and allocation size must remain distinct from pointer representation size.
- Pattern citations to hardware overflow or CHOP do not make C macro, padding or conditional-conversion questions authentic exam transcriptions. Preserve the original-problem labels.

## 3. Answer ledger for all placements

The keys agree with independent deductions under the stated models, except the layout family's unique result requires the explicit minimum-padding assumption.

| Q | Option | Exact answer or classification |
|---|---:|---|
| 1 | 4 | -4 + -5 = -9 is outside four-bit signed range |
| 2 | 3 | Offset formula rounds rather than truncates |
| 3 | 1 | Decimal rounded A−B=0.01 |
| 4 | 1 | ~u=-16 as int; converted unsigned char=240 |
| 5 | 1 | 2.0; double approximation to 7/3; same approximation to 7/3 |
| 6 | 2 | Comparison result 1 |
| 7 | 2 | Result 0; right operand not evaluated |
| 8 | 2 | Unsigned result 0; signed counterpart undefined |
| 9 | 2 | Equality result 1 under the explicit binary64 model |
| 10 | 2 | CHOP(100x−0.5)/100 gives -2.38 |
| 11 | 2 | Unparenthesized macro result 5 |
| 12 | 4 | Unsigned maximum 255 |
| 13 | 3 | Unsigned maximum 2047 |
| 14 | 2 | 2^(n+3)−1 |
| 15 | 1 | Representation width must be stated |
| 16 | 1 | Modular register result 5 |
| 17 | 4 | Modular register result 8 |
| 18 | 3 | Modular register result n |
| 19 | 2 | Expression promotions precede destination conversion |
| 20 | 4 | Signed five-bit minimum -16 |
| 21 | 3 | Signed eight-bit minimum -128 |
| 22 | 2 | -2^(n−1) |
| 23 | 1 | Minimum has no positive same-range counterpart |
| 24 | 4, after clarification | Minimum-layout record size 12 at n=5 |
| 25 | 3, after clarification | Minimum-layout record size 16 at n=9 |
| 26 | 2, after clarification | 4*ceil(n/4)+4 |
| 27 | 1 | Layout assumptions are necessary |
| 28 | 3 | Actual-array size 120 bytes |
| 29 | 2 | Actual-array size 288 bytes |
| 30 | 1 | 4n(n+1) bytes |
| 31 | 4 | Adjusted array parameter has pointer sizeof |
| 32 | 4 | 9 packed bits occupy 2 bytes |
| 33 | 3 | 17 packed bits occupy 3 bytes |
| 34 | 2 | ceil(n/8) bytes |
| 35 | 1 | Serialization does not determine portable C bit-field layout |
| 36 | 1 | All consecutive integers through 32 exact at p=5 |
| 37 | 4 | All consecutive integers through 256 exact at p=8 |
| 38 | 3 | Consecutive-exactness endpoint 2^n |
| 39 | 2 | Some larger integers exact, but not every consecutive integer |
| 40 | 2 | Quotient -5 |
| 41 | 1 | Quotient -8 |
| 42 | 4 | Quotient -n |
| 43 | 3 | Truncated quotient/remainder reconstruct the dividend |
| 44 | 2 | (4294967167,127) |
| 45 | 1 | Comparison result 0 |

## 4. Independent derivations and precise distractor failures

### Authentic Q1: signed overflow is not unsigned carry

Decode the four additions as (5,-8), (2,5), (4,-2), (-4,-5). Their mathematical sums are -3, 7, 2, -9. Only the last is outside [-8,7]. The stored low-bit sums are respectively 1101, 0111, 0010 and 0111. Thus the overflowed last result misleadingly decodes to +7. A fixed-width adder can detect signed overflow when the carry into the sign position differs from the carry out; equivalently, equal-sign operands produce a result of the opposite sign. Opposite-sign operands cannot exceed either signed endpoint. Carry out alone tests a different unsigned condition.

The hardware item does not ask a C expression's signed result. A solution should stop at “undefined” for overflowing signed C arithmetic and may illustrate low bits only as a separate hardware model.

### Authentic Q2 and authored Q10: CHOP and decimal places

For exact real x, truncation is floor(x) when x≥0 and ceil(x) when x<0. An integer is unchanged. For a negative x, truncating x−1/2 implements nearest-integer rounding with ties away from zero; for a positive scaled x, truncating 100x+1/2 implements nearest hundredth with ties upward. This is rounding, not discarding all digits after the hundredth.

At x=1.239, plain hundredth truncation is 1.23 while the offset expression gives 1.24. For x=-2.376, scale gives -237.6. The correct negative offset gives -238.1, whose CHOP is -238, producing -2.38. Positive offset and no offset both give -2.37. Applying CHOP to x−0.5 before scaling gives -2/100=-0.02, an entirely different decimal place. At the tie x=-2.375, the correct expression also yields -2.38. All these are exact-real calculations, not guarantees about multiplying an arbitrary double by 100.

### Authentic Q3: operation-by-operation decimal rounding

The calculator retains five significant decimal digits. Compute two distinct rounding trees:

| Branch | Exact intermediate | Rounded value |
|---|---:|---:|
| a+b | 422.586 | 422.59 |
| rounded(a+b)+c | 435.007 | 435.01 |
| b+c | 93.733 | 93.733 |
| a+rounded(b+c) | 435.003 | 435.00 |

Subtracting gives 0.01. The final exact total without intermediate rounding is 435.003; pretending both branches use it would produce zero. Treating precision as four total significant digits rather than four digits after the normalized mantissa's decimal point would define another machine. None of these intermediate rounds is a tie, so the result is independent of tie-breaking distinctions between common nearest rules.

### Q4 and Q44: narrow object, promoted expression, destination conversion

For u=15, promotion to the stipulated signed int occurs before complement. In two's-complement int, ~15=-16, whose eight-bit unsigned residue is 240. The proposed 240 as the intermediate value prematurely truncates the expression to its original storage width. A negative unsigned-char result is outside that type's range, and 15 fails to perform complement.

For uint8_t x=128, all original values fit int, so ~x is int -129. Assignment to unsigned int yields -129 mod 2^32 = 4294967167; conversion to uint8_t yields -129 mod 256 =127. The first integrated distractor applies an eight-bit complement too early, the third has the wrong low-byte residue, and the fourth retains the input instead of complementing. The numeric identity ~v=-v−1 is tied to the declared two's-complement model, not every C17 signed representation.

### Q5: cast placement cannot recover a remainder

Integer 7/3 first produces quotient 2 and remainder 1. Casting the quotient produces 2.0 and cannot restore 1/3. Casting either operand before division gives double operands 7.0 and 3.0. Under binary64 nearest-even, the result is the same stored approximation in both cases; it is not the exact real fraction. The three wrong options each incorrectly assign a floating target to a post-division cast or an integer target to one of the pre-division casts. Assignment to a double after `a/b` has the same information-loss issue as an outer cast.

### Q6 and Q45: selected value and common type are different questions

The two arithmetic alternatives are int and unsigned int of equal rank. The common type is unsigned int, regardless of the selected value path. The selected -1 becomes 2^32−1. It is greater than 2u, giving Q6 result 1. For Q45, comparison with zero converts zero to the same unsigned type, so the result is 0. The unselected branch contributes its type without executing its value expression. This is a defined value conversion, not overflowing signed arithmetic. Changing the selector changes the selected value but does not remove the common-type step.

### Q7: a control-flow proof, not algebraic simplification

Evaluate x!=0 first; at x=0 it is false. The && expression therefore yields int zero and never evaluates 10/x. The division-by-zero distractor assumes eager evaluation. Value 1 contradicts the left operand, and implementation dependence has no role in this stated case. Replacing && with & evaluates the dangerous right operand and introduces undefined behavior. The absence of evaluation is the reason the original is safe; cancellation or an assumed order for bitwise operands would not repair the eager variant.

### Q8: range checks before output prediction

UINT_MAX+1u is evaluated as unsigned int and has residue zero modulo 2^32. INT_MAX+1 has an unrepresentable signed mathematical result; no portable result, including INT_MIN, follows. Saying both wrap imports hardware low-bit behavior into a different language model. Saying both are undefined discards the explicit unsigned operation. The suffix on 1u establishes the unsigned operand type before addition.

### Q9 and Q36–39: binades and consecutive exactness

A binary format with p significant bits has spacing 2^(e−p+1) in the binade [2^e,2^(e+1)). Every integer through 2^p is exact: smaller integers require at most p significant bits, and the endpoint is an exact power of two. At the endpoint binade the spacing is 2, so the next odd integer 2^p+1 is missing. This proves answers 32 at p=5 and 256 at p=8, while 2^p−1 excludes a valid endpoint and 2^(p+1) crosses many missing odd integers. It does not mean 2^p is the largest finite or largest exactly represented integer.

For binary64, p=53 and a=2^53. Exact a+1 lies halfway between a and a+2. The endpoint's significand integer 2^52 is even, so nearest-even chooses a and equality is true. Exact a+3 lies halfway between a+2 and a+4; the lower significand is odd and the upper even, so that separate extension rounds to a+4. Just below a, the spacing is 1; just above it, 2. A simulation should show this asymmetric local spacing rather than a uniform decimal ruler. Excess evaluation precision or a different rounding mode changes the premise, so the current explicit round-after-each-operation model must stay visible.

### Q11: expand tokens and parse the resulting expression

`SQR(1+2)` replaces x twice in `x*x`, giving `1+2*1+2`. Multiplication binds before either addition, yielding 1+2+2=5. A fully parenthesized macro `((x)*(x))` fixes this input but still repeats an argument expression. It is not a function, and parenthesization alone does not make repeated side effects safe. There are no side effects in the original expression, so its result is defined rather than undefined.

### Q12–15: unsigned range

With w=n+3 value bits and no padding, the maximal pattern has positional sum 1+2+...+2^(w−1)=2^w−1. There are 2^w patterns, including zero. At n=5, w=8 and max=255; at n=8, w=11 and max=2047. The distractor 2^w counts values, 2^(w−1)−1 assumes a different signed range, and 2^n uses the wrong width. A storage size in bytes alone does not identify the number of value bits without CHAR_BIT and padding assumptions. The width is a representation model, not a declaration that arbitrary-width C integer types exist.

### Q16–19: explicit modular register

Let M=2^(n+3). Maximum M−1 plus n+1 gives M+n, whose residue is n because 0≤n<M. For every positive n, the exponential M exceeds n; an induction or the stronger bound 2^n≥n+1 suffices. Exactly one carry is discarded for this family. The results are 5 from 255+6=261 and 8 from 2047+9=2056. The unreduced mathematical totals are distractors, as are the unchanged addend n+1 and negative -n. A narrow C object may first promote to int and compute 261 without overflow, then narrow to 5 upon assignment; that differs from saying the expression itself was an eight-bit addition.

### Q20–23: two's-complement endpoints

For n total sign-and-value bits, the sign bit has weight -2^(n−1) and lower bits have weights 1 through 2^(n−2). Setting only the sign bit gives minimum -2^(n−1), hence -16 and -128. Setting all lower bits with sign zero gives maximum 2^(n−1)−1. The range is asymmetric by one. The distractor -2^n uses an extra bit; -(2^(n−1)−1) excludes the true endpoint, and zero ignores negative encodings. At n=1 the abstract representation contains -1 and 0; this does not assert that a standard C signed type may have only one bit. Negating the minimum in the same signed arithmetic type cannot produce a representable positive value.

### Q24–27: minimum-layout padding after clarification

If the first member starts at offset zero and occupies n bytes, the earliest valid second-member offset is 4*ceil(n/4). The four-byte second member ends at 4*ceil(n/4)+4, already a multiple of four; no additional minimum tail padding is needed. At n=5, bytes 5–7 are internal padding and the second member occupies bytes 8–11, size12. At n=9, bytes9–11 are padding and the second occupies12–15, size16. At n=8, no internal padding is needed and size12.

The n+4 distractor ignores internal padding; the rounded first-member size omits the second member; n+8 assumes a constant padding amount rather than 0–3 bytes. Extra permissible C padding is why the minimum-layout rule must be explicit. No member bytes disappear under alignment, and the object cannot end before the last member's storage ends.

### Q28–31: array-object size, row stride and pointer size

An actual n by (n+1) array contains n(n+1) elements, each four bytes, so size is 4n(n+1): 120 and 288. A row stride is only 4(n+1), giving 24 and 36; 4n counts one four-byte item per row; n(n+1) is the element count, not the byte count. Under a separately declared eight-byte-pointer ABI, `sizeof a` inside a function whose array parameter was adjusted to a pointer gives 8, whereas `sizeof a[0]` can still describe a whole row. The parameter adjustment is not a loss of the pointed-to row type. A pointer object never includes the target allocation in its own sizeof. Zero-size standard array declarations and oversized actual allocations require separate domain checks; the mathematical expression alone cannot guarantee an object exists.

### Q32–35: packed serialization

Write n=8q+r with 0≤r<8. Minimum bytes are q if r=0 and q+1 otherwise: ceil(n/8). Thus n=9 gives2, n=17 gives3, n=8 gives1, n=16 gives2, and a zero-flag serialization needs zero bytes. The extra-one distractor wastes a byte on every exact multiple; n treats each bit as a byte; 8n reverses the conversion. An overflow-safe implementation of the count for a nonnegative size_t is `n/8 + (n%8 != 0)`, unlike `(n+7)/8` at a near-maximum n. This explicit serialization is not an inference about C bit-field allocation order or an array of byte-valued booleans.

### Q40–43: truncated quotient and negative remainder

For positive n, the exact quotient of -(3n+1) by 3 is -n−1/3. Truncation toward zero gives -n. Reconstructing the dividend yields remainder -1:

\[
-(3n+1)=(-n)\,3+(-1).
\]

Thus -16/3 gives -5 remainder -1, and -25/3 gives -8 remainder -1. Floor gives the wrong -6 and -9; the positive n distractor loses the sign; the original negative dividend is not the quotient. A nonzero remainder follows the dividend's sign, not the divisor's. Before applying a universal remainder identity, exclude zero divisor and a quotient outside the type's range: int32 INT_MIN/-1 and INT_MIN%-1 both have undefined behavior under the stipulated model even though the mathematical remainder in the latter would be zero.

## 5. Concrete medium/hard extensions with complete target conclusions

These are suggestions for independently authored extensions, not claims that new question placements were added or officially calibrated.

1. **Narrow unsigned multiplication:** for uint16_t u=65535 and int32, `u*u` promotes both operands to int; exact product 4294836225 exceeds INT_MAX. Assigning afterward to uint64_t does not repair the intermediate. `(uint32_t)u*u` is a defined unsigned product equal to 4294836225 in the declared model.
2. **Integer versus floating unsigned conversion:** `(unsigned int)-1` gives UINT_MAX, while `(unsigned int)-1.0` has an unrepresentable truncated integer and is undefined. A finite double -0.75 truncates to zero and does fit unsigned. These cases cannot be classified from a blanket “all conversions wrap” rule.
3. **LP64 versus LLP64:** with long s=-1 and unsigned int u=1, LP64 long64 can represent all unsigned-int32 values, so s<u is true in signed long. Under a declared long32 LLP64 model, the common type is unsigned long and the negative value converts to its maximum, so the comparison is false. Do not run on the host to establish portability.
4. **Sequencing:** with int i=1, `i++ + i++` is undefined from unsequenced modifications; `(i++, i++)` is defined, evaluates to2 and leaves i=3; `i++ && i++` is also defined for these values, evaluates to1 and leaves i=3. Trace sequence relations, not only arithmetic precedence.
5. **Macro side effects:** `#define SQR(x) ((x)*(x))` with `SQR(i++)` still creates unsequenced modifications. An actual function receiving i++ once evaluates that argument once; its body then uses a local value. Parentheses repair grouping, not repeated evaluation.
6. **Intermediate negation:** int n=1073741824 in `-(2*n)` overflows at multiplication, despite the mathematical final value being INT_MIN. Using a sufficiently wide signed type before multiplication changes the evaluated model and makes the later range-checked conversion possible.
7. **Shift boundaries:** under int32, `1u<<31` gives2147483648, `1<<31` is undefined, `1u<<32` is undefined, and a right shift of a negative signed operand is implementation-defined. Unsigned modular arithmetic does not legalize an out-of-width shift count.
8. **Fractional rounding tie:** at a=2^53 in binary64 nearest-even, a+1 rounds to a and a+3 rounds to a+4. Give the adjacent significand parity rather than simply claiming rounding always goes down at a midpoint.
9. **Record reordering:** for a minimum-layout char[5], int32, char record with respective alignments1,4,1 and record alignment4, offsets are0,8,12; final size16 includes three tail bytes. Reordering to int32,char[5],char yields offsets0,4,9 and size12. Show both interior and tail padding; neither follows merely from summing widths.
10. **Allocation-size arithmetic:** for a declared size_t, computing 4*n*(n+1) must avoid overflow before allocating. Validate n+1 first, then divide an allowed maximum by factors before multiplication; a modularly wrapped positive count is not evidence that the full mathematical array fits.

## 6. Computations actually executed

Python exact integer arithmetic independently checked the four signed sums and low four-bit residues, narrow/wide complement residues, minimum-layout sizes at n=5,8,9, actual-array sizes at n=5,8, packed counts at n=0,8,9,16,17, quotient/remainder identities, the int32 safe upper parameter and the uint16 square. Decimal arithmetic at precision five recomputed both authentic rounding paths as435.01 and435.00. A safe binary64 host observation corroborated a+1==a and a+3=a+4; the mathematical neighbor/parity derivation remains the justification for the specified format. Python integer division was not used as if it were C signed truncation. No C undefined expression was executed.

## 7. Question-specific models and diagrams

1. **Four-bit adder:** four actual additions, bit weights, carry into/out of sign bit, mathematical result versus low-bit decoding. Separate signed-overflow and unsigned-carry indicators.
2. **CHOP ruler:** scaled real value, signed half-unit offset, truncation arrow toward zero and final scale-back. Show negative tie and non-tie examples explicitly.
3. **Decimal rounding trees:** two operation trees with exact intermediate and rounded value at each node; final difference0.01. Do not use binary64 as a replacement machine.
4. **Promotion pipeline:** eight-bit storage →32-bit promoted int →complemented signed value →selected destination residue. Label type and numeric value at every checkpoint; show 15 and128 examples.
5. **Cast placement trees:** group integer division first versus convert an operand first. Preserve lost remainder as a struck-through unavailable branch after division.
6. **Conditional type and value:** separate a static common-type lane containing both branches from a runtime lane selecting exactly one branch. A comparison then applies its own conversions.
7. **Short-circuit control:** reachability trace with the dangerous division marked not evaluated, not a fake computed zero. The bitwise variant enters an undefined-state checkpoint without predicting an output.
8. **Unsigned register:** number-circle or carry-chain showing total M+n, discarded carry and stored n. A second lane shows a promoted C expression and later narrowing to avoid mixing models.
9. **Signed endpoints:** bit weights and asymmetric number interval; negation of minimum leaves the representable range. No simulated C wrap for undefined negation.
10. **Record byte map:** first member, explicit padding, second member and tail rounding. A movable member length updates offsets and size; display the minimum-layout assumption.
11. **Two-dimensional array map:** row blocks, element offsets, row stride and whole-array bytes. Parameter adjustment shows a pointer box while retaining the pointed-to row type.
12. **Packed flags:** exact count of full bytes and final partially used byte, with n=8,9,16,17 boundary checkpoints. Unused bits are visible rather than omitted.
13. **Floating binade ruler:** adjacent representable values with asymmetric spacing around2^p and a midpoint parity decision. The p=5 representative should expose actual integer gaps; binary64 can use labeled large integers without implying ordinary screen spacing is linear across all magnitudes.
14. **Division reconstruction:** a number line distinguishing truncate from floor plus exact q*d+r ledger, including dividend-negative/divisor-negative cases. An invalid quotient is classified before any remainder output.
15. **Macro token expansion:** replacement tokens, parse tree, then value. An optional side-effect lane stops at unsequenced UB rather than inventing an evaluation order.

## 8. Handoff

All45 placements have independently checked keys under explicit models. Q24–27 need a minimum-padding premise. The source originals have been freshly inspected and the relevant N1570 rules actually read. Remaining work includes the full lesson/course synthesis, detailed individual answers, source integration, simulation implementation and real browser/font/mobile checks. This audit alone does not complete those gates.
