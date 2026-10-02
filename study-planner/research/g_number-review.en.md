## 14. Complete-sentence summary and examination guidance

### Reconstruct the chapter from five ideas

**A word needs a decoding contract.** The same bits can represent an unsigned integer, a signed integer, a scaled fraction, a decimal digit sequence, or a Gray index. Record width, encoding, scale, and legal-word constraints before calculating. Hexadecimal notation does not supply these missing assumptions.

**Positional conversion follows division and remainder.** Integer repeated division extracts low digits first; fractional repeated multiplication extracts high fractional digits first. Grouping is exact when bases are powers of the same underlying base. Rational termination is equivalent to the reduced denominator dividing a power of the target radix, and repeated remainder states identify cycles.

**Word arithmetic is modular arithmetic plus interpretation.** Two's complement maps signed integers to residues modulo 2<sup>n</sup>, allowing the same low-bit adder as unsigned arithmetic. The retained bits are not proof that the exact integer answer fits. Carry, borrow, signed overflow, and discarded product bits answer different representability questions.

**Changing width or scale must preserve a declared value.** Sign extension works because the newly added leading ones exactly cancel the larger signed modulus. Narrowing preserves value only if its discarded bits satisfy the target decoder's condition. Fixed-point arithmetic separately tracks integer codes and fractional-bit counts; quantization and intermediate overflow each need explicit treatment.

**A code is designed for a particular property.** BCD preserves decimal digit boundaries; self-complementing decimal codes simplify nines' complement; Gray codes provide one-bit adjacency; parity and Hamming codes supply redundancy for bounded error detection or correction. These properties are not interchangeable and none grants unlimited immunity to errors.

### Sixty high-yield rules, with the reason and the exception

#### Notation, capacity, and conversion

1. **Write the base before evaluating a numeral.** A string containing only zeros and ones can be legal in many radices, so its appearance does not determine its value.
2. **Reject illegal digits before solving a base equation.** Every digit value must be strictly smaller than the radix; an algebraic root that violates this condition is inadmissible.
3. **Distinguish a count from a largest label.** An n-bit code has 2<sup>n</sup> patterns, while the maximum unsigned value is 2<sup>n</sup> − 1.
4. **Use the inclusive interval length for arbitrary-code capacity.** Labels from L through H require H − L + 1 distinct codes, but a prescribed signed format can demand extra bits.
5. **Treat zero as a special digit-count case.** Its minimal written representation contains one digit even though a logarithm-based positive-integer formula does not apply.
6. **Keep integer division remainders in reverse order.** Repeated division extracts the least significant digit first; reversing them constructs the written numeral.
7. **Keep fractional multiplication digits in extraction order.** Each extracted integer part supplies the next most significant fractional position; reversing them changes the value.
8. **Preserve internal zero digits.** A zero contributes no value but still fixes the positional weights of later digits.
9. **Group outward from the radix point.** Complete integer groups by padding on the far left and fractional groups by padding on the far right.
10. **Do not reuse unsigned padding as signed extension.** Adding leading zeros to a negative two's complement word changes its value; widening must preserve its signed decoder.

#### Fractions and numerical accuracy

11. **Reduce a rational fraction before deciding termination.** Only the reduced denominator matters; numerator cancellation can remove otherwise problematic prime factors.
12. **Test divisibility by a power of the radix.** Finite base-b representation exists exactly when the denominator divides b<sup>f</sup> for some integer f.
13. **Recognize binary-exact fractions by their reduced denominator.** A binary terminating fraction has a denominator that is a power of two; a finite decimal expansion does not imply binary termination.
14. **Track exact remainders to find a repeating block.** An approximate decimal residual can produce false termination or an unreliable cycle length.
15. **Count leading zeros inside a repeating block.** They determine the block length k and hence the denominator b<sup>k</sup> − 1.
16. **Scale a repeating tail by its prefix length.** A t-digit nonrepeating prefix moves the repeating fraction t positions to the right.
17. **Specify the tie rule for nearest rounding.** An exact midpoint can map to either adjacent grid point unless a policy such as ties-to-even is declared.
18. **Use the appropriate absolute-error bound.** Positive truncation error is below one grid step, while nearest rounding is at most half a step when a suitable in-range point exists.
19. **Do not infer a uniform relative-error bound near zero.** A small absolute quantization error can be large relative to a very small exact value.
20. **Check range after rounding.** A target near the highest endpoint may round beyond the representable interval even if it is close to a valid value.

#### Signed encodings and complements

21. **Apply the correct negative-value decoder.** Ones' complement subtracts 2<sup>n</sup> − 1 from a top-one word; two's complement subtracts 2<sup>n</sup>.
22. **Account for both zero words in symmetric encodings.** Sign-magnitude and ones' complement have two zero encodings, so their top-one zero is not strictly negative.
23. **Locate the two's complement minimum correctly.** One followed by zeros represents −2<sup>n−1</sup>; all ones represents −1.
24. **Negate two's complement words at a stated width.** Complement-plus-one depends on the number of bits being complemented and the modulus being retained.
25. **Handle the most negative value before exact negation.** Its positive opposite does not fit at the same signed width; widen first when an exact result is needed.
26. **Do not add sign-magnitude words as ordinary binary integers.** The numerical algorithm must inspect signs and add or subtract magnitudes accordingly.
27. **Include end-around carry in ones' complement addition.** Dropping the carry without adding it back can leave a representable sum wrong by one.
28. **State the actual bias in excess-K notation.** Biases at or near half the modulus are common but do not produce the same encoding.
29. **Correct one extra bias when adding biased words.** Two stored operands already contain two copies of K; the result should contain only one.
30. **Use the top-bit toggle shortcut only for excess-2<sup>n−1</sup>.** Other biases need additional value adjustment; the shortcut is not a generic biased-code conversion.

#### Arithmetic flags and widths

31. **Compute the exact answer before reducing it.** A valid low-word residue can coexist with an unrepresentable intended mathematical answer.
32. **Use carry-out for unsigned addition overflow.** Signed addition instead requires its signed range or a signed-overflow criterion.
33. **Opposite-sign signed addition cannot overflow without an extra unspecified operand.** The exact sum lies between the two operands; include any carry-in in the arithmetic contract.
34. **Equal-sign addition overflows when the retained sign changes.** Two nonnegative operands can wrap negative; two negative operands can wrap nonnegative.
35. **Distinguish carry into the sign bit from carry out.** Their XOR is signed adder overflow; final carry alone has a different meaning.
36. **Label subtraction's flag convention.** For A + complement(B) + 1, carry-out means no unsigned borrow, while a borrow flag is its complement.
37. **Use the subtraction-specific sign criterion.** Different operand signs plus a result sign different from the minuend indicates signed overflow.
38. **Do not implement a comparison by the sign of a truncated difference alone.** Overflow can reverse that sign; the subtractor's result sign XOR signed overflow supplies the signed less-than condition.
39. **Budget up to twice the operand width for an exact product.** The minimum-times-minimum signed case shows why 2n − 1 bits can fail.
40. **Check narrowing against the retained sign bit.** Every discarded two's complement bit must match that new sign bit; matching the old sign alone is insufficient.

#### Shifts and fixed-point calculations

41. **Widen before an operation that needs greater range.** Widening a result after overflow preserves its damaged value instead of recovering the lost mathematical answer.
42. **Extend sign-magnitude by moving the sign and padding the magnitude.** Repeating the top bit is appropriate to complement encodings, not this format.
43. **Differentiate logical right shift from arithmetic right shift.** The first fills with zeros; the second repeats the sign bit and implements signed floor division in the abstract model.
44. **Distinguish floor division from truncation toward zero.** Negative quotients differ when discarded remainder bits are nonzero.
45. **Do not transfer abstract shifts into a language without checking its rules.** C promotions, signed overflow, and implementation-defined negative shifts can change or invalidate a numerical shortcut.
46. **Define total width and fractional-bit count explicitly.** A bare Q-format name may use a different sign convention in another source.
47. **Keep scale metadata distinct from stored integer bits.** Decoding an integer correctly is only the first step; the power-of-two scale supplies its real value.
48. **Align scales before adding fixed-point values.** Adding raw codes with different fractional-bit counts combines incompatible units.
49. **Add fractional-bit counts when multiplying.** Rescale the full product deliberately before storing it in a target format with fewer fractional places.
50. **Audit intermediate range and cumulative error separately.** A safe final value does not prove a safe intermediate, and a one-step quantization bound does not apply unchanged to a whole computation.

#### Decimal, Gray, and error-control codes

51. **Validate every BCD nibble separately.** Six of the sixteen four-bit patterns are invalid decimal digits, and a packed digit sequence is not a pure binary integer.
52. **Correct BCD subtotals at ten, not sixteen.** Add six when the initial carry is set or the retained nibble exceeds nine, preserving the decimal carry.
53. **Use the declared weighted codebook.** Duplicate weights can give several words the same sum; only the designated table determines legal Aiken 2421 words.
54. **Interpret self-complementing decimal codes as digitwise nines' complements.** They do not make bitwise complement of an ordinary BCD word a valid decimal complement.
55. **Decode Gray words before ordinary arithmetic.** XOR-based Gray labeling preserves adjacency, not the numerical value of the raw word or ordinary binary addition.
56. **Limit Gray's one-change claim to adjacent positions.** Skipped positions, mechanical noise, and metastability are not eliminated by the labeling convention.
57. **Do not classify Gray code as a redundancy code.** Every n-bit word is legal and the minimum distance is one, so arbitrary single-bit errors are not generally detected.
58. **State distance thresholds precisely.** Guaranteed detection of e flips requires minimum distance at least e + 1; guaranteed correction of t flips requires at least 2t + 1.
59. **Interpret a passing parity check conservatively.** Even parity detects all odd-weight flips, while any even-weight corruption can pass the test.
60. **Apply syndrome correction only under its error bound.** Hamming (7,4) can miscorrect double errors; extended overall parity separates single errors from double errors only under the declared SECDED bound.

### An eight-step method for unfamiliar problems

1. **List the contracts.** Identify radix, word width, signed encoding, fractional scale, codebook, arithmetic operation, and overflow or rounding policy.
2. **Validate the given data.** Check legal digits, legal codewords, width, representable input range, and denominator or divisor restrictions.
3. **Decode to exact values.** Use positional weights, the proper signed formula, or the declared code conversion; keep exact rational arithmetic where possible.
4. **Perform the requested mathematical operation.** Include carry-in, scale alignment, decimal carries, and the intended quotient rounding rule.
5. **Test representability before presenting the result.** Compare the exact value with the target range and determine whether quantization or an explicit overflow policy is needed.
6. **Encode the target result and compute the requested flags.** Keep carry, no-borrow, signed overflow, parity, and syndrome labels distinct.
7. **Check independently.** Decode the final word again; verify a different formula or a boundary case, rather than repeating the same arithmetic unchanged.
8. **Explain any lost information.** State whether truncation, quantization, clipping, wraparound, ambiguous decoding, or an exceeded error bound prevents an exact conclusion.

### Readiness and remaining uncertainty

The chapter aims to teach the derivations needed to handle unfamiliar combinations of its topics, not just memorize the worked answers. The source comparison, independent finite arithmetic checks, browser tests, and visual review make specific errors less likely. They do not establish literal universal correctness or guarantee performance on every future examination question. The stated chapter boundary and deferred archive are explicit; questions involving a later circuit, programming-language, or floating-point topic need that additional instruction.

This chapter was explicitly approved by the student on 2026-10-02. It is now an approved chapter. No pre-study test is required.

## 15. References and exact reading locations

1. **Massachusetts Institute of Technology.** Chris Terman. *6.004 Computation Structures*, Spring 2017. [Chapter 1, Annotated Slides](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s1/). Reviewed in-scope fixed-length encoding, integer representation, complement, Hamming-distance, parity, and correction sections. The [worksheet landing page](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s3/) was screened; its linked worksheet was not used as a read exercise source.
2. **University of California, Berkeley.** CS61C course teaching team. *Number Representation*, living written course notes. [Binary, Decimal, Hex](https://notes.cs61c.org/content/number-rep/binary-decimal-hex/) and [Integer Representations](https://notes.cs61c.org/content/number-rep/integer-representations/). Reviewed the written teaching bodies and quick checks for unsigned, sign-magnitude, ones' complement, two's complement, and bias. A specific year or sole author is not assigned to these living notes.
3. **Stanford University.** Jerry Cain and Lisa Yan. *CS107*, Winter 2020, Lecture 2, Bits and Bytes; Integer Representations. [Official lecture PDF](https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/lectures/2/Lecture2.pdf). PDF pages 8–50, 53–84, and 109–114 reviewed; numeric-range and casting claims are restricted to their stated machine model. [Course archive](https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/).
4. **Cornell University.** Adrian Sampson and Giulia Guidi; CS3410 teaching team. *Computer System Organization and Programming*, Fall 2024. [Switches and Numbers](https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/numbers.html), specifically positional conversion and signed representation, and [Floating Point](https://www.cs.cornell.edu/courses/cs3410/2024fa/notes/float.html), specifically Real Numbers in Binary and Fixed-Point Numbers. [Offering overview](https://www.cs.cornell.edu/courses/cs3410/2024fa/) identifies both instructors. Full IEEE details are deferred.
5. **Carnegie Mellon University.** Course teaching team. *15-213/14-513/15-513: Introduction to Computer Systems*, Spring 2025. [From Bits through Integers, January 16](https://www.cs.cmu.edu/afs/cs/academic/class/15213-s25/www/lectures/02-bits-bytes-ints.pdf). PDF pages 7–10, 19, 21–35, 39–64 reviewed for positional notation, fixed-width arithmetic, extension, narrowing, product widths, and shift rounding. Individual authorship is not inferred from the slide template.
6. **Princeton University.** Robert Sedgewick and Kevin Wayne. *Algorithms*, Combinatorial Search lecture resources. [Official lecture PDF](https://algs4.cs.princeton.edu/lectures/keynote/67CombinatorialSearch.pdf), PDF pages 35–37: reflected Gray construction, enumeration, and applications. Original page images were checked because local text extraction damaged some glyphs. The edition year is not guessed from a search-engine crawl date.
7. **ISO/IEC JTC1/SC22/WG14.** *N1570, Committee Draft, 12 April 2011.* [Official committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), §§6.5 paragraph 5 and 6.5.7, checked for expression representability, integer promotions, shift counts, unsigned left shifts, and implementation-defined signed negative right shifts. This is a C11 committee draft used to check the relevant retained C17 rules, not the published C17 standard and not another university course.

The chapter's additional derivations, explicitly declared decimal code tables, Hamming construction, integrated design problems, and numerical checks are independently developed instructional material. The source audit explains which contribution each reviewed course supplied and which adjacent topics were excluded. References describe actual reading rather than implying complete inspection of every lecture in a course.
