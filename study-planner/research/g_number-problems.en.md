## 13. Thirty-six fully worked problems

These problems progress from interpreting notation to combining representation, arithmetic, and coding constraints. Every solution states its contract before computing. Course-pattern adaptations are identified without claiming that these are verbatim university examination questions. The remaining problems are original constructions. None uses the deferred Iranian examination archive.

### Problem 1. Interpret rather than recognize a familiar digit string

**Task.** Evaluate 1010<sub>2</sub>, 1010<sub>8</sub>, and 1010<sub>16</sub>. Explain why the digit string alone is insufficient. **Pattern:** Stanford Lecture 2 base-conversion checks, with additional bases.

**Solution.** In binary the nonzero positions have weights eight and two, giving ten. In octal they have weights 8<sup>3</sup> and 8, giving 512 + 8 = 520. In hexadecimal they have weights 16<sup>3</sup> and 16, giving 4096 + 16 = 4112. Each digit is legal in all three bases, so no syntax error chooses one interpretation for us. The base must be stated.

**Lesson.** A numeral is a sequence of digit values plus a radix. Recognizing a binary-looking sequence is not evidence that it was intended as binary.

### Problem 2. Convert an integer with internal zero digits

**Task.** Convert decimal 1029 to binary, octal, and hexadecimal, retaining exactly twelve binary positions. **Pattern:** Cornell and Stanford integer-conversion instruction.

**Solution.** The largest binary weight is 1024, leaving five; five is four plus one. Thus the twelve-bit word is 0100 0000 0101. Grouping from the right into three-bit blocks gives 010 000 000 101, hence octal 2005. Grouping into four-bit blocks gives 0100 0000 0101, hence hexadecimal 405. Check: 4 × 256 + 5 = 1029, and 2 × 512 + 5 = 1029.

The leading zero is required by the requested twelve-bit width, while zeros inside the word preserve place values. Four hexadecimal digits would imply up to sixteen displayed bits if every hex digit were fully expanded; here three digits suffice for twelve bits.

**Lesson.** Conversion preserves value; a separate width requirement determines padding.

### Problem 3. Solve an unknown-radix equation and reject an apparent answer

**Task.** Find the radix in 34<sub>b</sub> = 25<sub>10</sub>. Then decide whether 45<sub>b</sub> = 17<sub>10</sub> has a legal solution.

**Solution.** The first equation is 3b + 4 = 25, yielding b = 7. Since four is the largest digit and 7 > 4, the answer is legal. The second equation gives 4b + 5 = 17, or b = 3. But digit five is not legal in radix three. Therefore the second written equation has no admissible radix despite having an algebraic root.

**Lesson.** Solve the numerical equation and the digit constraints together. A root alone is not a valid encoding.

### Problem 4. An unknown-base equation that does not determine the base

**Task.** Determine all bases for which (12<sub>b</sub>)<sup>2</sup> = 144<sub>b</sub>.

**Solution.** The left side is (b + 2)<sup>2</sup> = b<sup>2</sup> + 4b + 4. That is exactly the right side's positional value. Thus the equation is an identity, not a constraint fixing b. Digit four requires b ≥ 5, so every integer radix at least five is a solution.

**Lesson.** An unfamiliar-base puzzle may have no solution, one solution, or many. Expanding the numerals reveals which case occurs.

### Problem 5. Count states and then respect the required encoding

**Task.** A device needs to distinguish 500 statuses. How many freely assigned fixed-length binary bits suffice? How many standard two's complement bits are needed if the statuses are labeled numerically from zero through 499? **Pattern:** MIT fixed-length encoding and capacity.

**Solution.** Since 2<sup>8</sup> = 256 < 500 ≤ 512 = 2<sup>9</sup>, nine bits suffice for freely assigned codes. Nine-bit two's complement instead has maximum 255, so it cannot store numeric label 499. Ten-bit two's complement has range −512 through +511 and is sufficient. Nine-bit unsigned is also sufficient.

**Lesson.** Information capacity and the range of a specified numerical encoding answer different questions.

### Problem 6. Convert a mixed fraction by grouping around the point

**Task.** Convert 110101.1011<sub>2</sub> to octal and hexadecimal and verify the decimal value.

**Solution.** Integer octal groups are 110 and 101, yielding 65. Fractional groups are 101 and 100 after adding two trailing zeros, yielding .54. Therefore the octal result is 65.54. Hexadecimal grouping gives 0011 0101 . 1011, hence 35.B. Decimal verification is 32 + 16 + 4 + 1 + 1/2 + 1/8 + 1/16 = 53.6875. Octal verification is 6 × 8 + 5 + 5/8 + 4/64 = 53.6875.

Padding zeros on the wrong fractional side would change the value; .1011 and .001011 do not describe the same fraction.

**Lesson.** Group outward from the radix point. Integer and fractional padding go on opposite outer ends.

### Problem 7. Exact repeated multiplication

**Task.** Convert 0.6875 to binary with a trace and recover the original fraction.

**Solution.** Write 0.6875 = 11/16. Multiplying successive residual fractions by two gives 11/8 = 1 + 3/8; 3/4 = 0 + 3/4; 3/2 = 1 + 1/2; and 1 = 1 + 0. The digits arrive in order 1011. Thus 0.1011<sub>2</sub> = 1/2 + 1/8 + 1/16 = 11/16. The zero second digit must be recorded even though it contributes no numerical amount.

**Lesson.** Fractional conversion emits most significant fractional digits first, unlike integer division's least significant digits first.

### Problem 8. Determine termination and minimum length

**Task.** Does 7/48 terminate in base twelve? In binary? If it terminates, what is the shortest fractional length?

**Solution.** The denominator is 48 = 2<sup>4</sup> × 3, and the fraction is reduced. Base twelve is 2<sup>2</sup> × 3. Two fractional places supply denominator 12<sup>2</sup> = 144, divisible by 48; one place does not. Hence the shortest length is two. Scaling gives (7/48) × 144 = 21 = 19<sub>12</sub>, so the fraction is 0.19<sub>12</sub>. Binary never supplies the prime three, so its expansion repeats.

Check the base-twelve value: 1/12 + 9/144 = 12/144 + 9/144 = 21/144 = 7/48.

**Lesson.** A terminating length is a divisibility question, and the exponent comparison gives its exact minimum.

### Problem 9. Convert a repeating binary block back to a rational

**Task.** Find the rational value of 0.<span class="repeat">101</span><sub>2</sub> and of 0.01<span class="repeat">101</span><sub>2</sub>.

**Solution.** The three-bit block 101 has integer value five. For the first expansion, 8x − x = 5, so x = 5/7. For the second, the two-digit prefix 01 has value one and contributes 1/4. The repeating tail contributes (1/4)(5/7) = 5/28. The total is 7/28 + 5/28 = 12/28 = 3/7.

The prefix and repeated block occupy different positional scales. Treating the combined five characters as one repeating block would compute a different fraction.

**Lesson.** Mark the exact start of a cycle and preserve leading zeros in its length.

### Problem 10. Compare truncation and nearest rounding

**Task.** Approximate 0.1 with eight fractional binary bits by truncation and by nearest rounding. Compare errors and bounds.

**Solution.** Scaling by 256 gives 25.6. Truncation chooses code 25, so the stored value is 25/256 = 0.09765625 and absolute error is 0.00234375. Nearest rounding chooses code 26, giving 0.1015625 and error 0.0015625. The truncation bound is less than 1/256 = 0.00390625, while the nearest-rounding bound is at most 1/512 = 0.001953125. Both actual errors obey their respective bounds.

The nearest result is above the target, so its signed error is positive; the truncation error is negative. An error bound does not specify the error's sign.

**Lesson.** Compute the scaled exact value first, then state the quantizer. Do not equate truncation with rounding.

### Problem 11. Decode one word in five ways

**Task.** Decode eight-bit 1110 1001 as unsigned, sign-magnitude, ones' complement, two's complement, and excess-127. **Pattern:** Berkeley's comparison of integer encodings.

**Solution.** Unsigned weighting gives 233. Sign-magnitude has sign one and low-seven-bit magnitude 105, so the value is −105. Ones' complement subtracts 255 from the unsigned value, giving −22; complementing the word gives 0001 0110, magnitude 22. Two's complement subtracts 256, giving −23. Excess-127 subtracts the declared bias, giving 106.

These answers need not have the same sign because different decoders were requested. Excess-127 is not two's complement with an informal adjustment; it is an independently defined code.

**Lesson.** Decode from the stated representation, not from a guess that a leading one always means a negative value.

### Problem 12. Encode the same negative integer in three signed forms

**Task.** Encode −37 using eight-bit sign-magnitude, ones' complement, and two's complement; verify all results.

**Solution.** The positive magnitude 37 is 0010 0101. Sign-magnitude puts one in the top position while keeping the lower magnitude, yielding 1010 0101. Ones' complement flips all bits to 1101 1010, unsigned 218; 218 − 255 = −37. Two's complement adds one, yielding 1101 1011, unsigned 219; 219 − 256 = −37. All three have sufficient magnitude range at eight bits.

**Lesson.** Ones' complement and two's complement differ by one in the encoded negative word, but the corresponding decoders also differ by one.

### Problem 13. Find the two exceptional self-negating words

**Task.** Solve for every eight-bit word that is unchanged by complement-plus-one. Explain the numerical meanings. **Pattern:** Stanford and CMU negation boundary exercises.

**Solution.** Let its unsigned value be U. Unchanged negation means U ≡ −U modulo 256, or 2U divisible by 256. Among 0 ≤ U < 256, the possibilities are U = 0 and U = 128. The first is numerical zero; the second is two's complement −128. Its true positive opposite +128 is outside the eight-bit signed range, so the second fixed point is modularly valid but not an exact signed negation result.

**Lesson.** Algebra modulo the word modulus can have a different meaning from algebra over representable signed integers.

### Problem 14. Ones' complement addition requires end-around carry

**Task.** Add −5 and +3 using four-bit ones' complement. Show why retaining only four bits is insufficient.

**Solution.** +5 is 0101, so −5 is 1010. +3 is 0011. Their ordinary sum is 1101, with no carry; it decodes as 13 − 15 = −2, the desired answer. Now add −3 and −2 to expose the carry case: their words are 1100 and 1101, whose sum is 11001. The retained 1001 decodes as −6. Add the carry one to obtain 1010, which decodes as −5.

Both mathematical results lie in the four-bit ones' complement range −7 through +7. End-around carry makes these representable sums work; it does not expand that range.

**Lesson.** A correct algorithm must handle both the no-carry case and the carry case. A single easy example cannot justify omitting the correction.

### Problem 15. Signed and unsigned overflow are independent

**Task.** Analyze four-bit additions 0111 + 0001, 1111 + 0001, 1000 + 1000, and 0010 + 0011. Give carry-out and signed overflow.

**Solution.** The first gives 1000, carry zero. Unsigned 7 + 1 = 8 fits; signed +8 does not, so signed overflow is one. The second gives 0000, carry one. Unsigned 15 + 1 overflows, while signed −1 + +1 = 0 fits, so signed overflow is zero. The third gives 0000, carry one. Unsigned 8 + 8 exceeds fifteen and signed −8 + −8 is below −8, so both overflow. The fourth gives 0101, carry zero; both interpretations sum to five and fit, so neither overflows.

The four cases realize every combination of the two flags. Carry cannot be used as a signed-overflow substitute.

**Lesson.** Always label the interpretation whose representability is being checked.

### Problem 16. Derive overflow from a bit-by-bit trace

**Task.** Add four-bit 0101 and 0011, recording every carry. Verify both overflow criteria.

**Solution.** At bit zero, 1 + 1 + 0 gives result zero and carry one. At bit one, 0 + 1 + 1 gives result zero and carry one. At bit two, 1 + 0 + 1 gives result zero and carry one. At the sign bit, 0 + 0 + 1 gives result one and carry zero. The word is 1000. The carry into the sign bit is one and carry out is zero, so their XOR is one. Both operands are nonnegative and the stored result is negative, confirming signed overflow. Unsigned five plus three is eight and fits.

**Lesson.** The sign-bit carry is an internal carry, not the final carry. Distinguish their positions explicitly.

### Problem 17. Subtraction with a minimum operand

**Task.** Compute +7 − (−8) in four-bit two's complement using a unified subtractor. Report the retained word, unsigned borrow, and signed overflow.

**Solution.** Operand words are 0111 and 1000. Complement the second word to 0111 and add initial carry one: 0111 + 0111 + 1 = 01111 as a five-bit computation. The retained result is 1111, signed −1. There is no final carry, hence unsigned borrow one because unsigned 7 − 8 is negative. The true signed answer is fifteen, so signed overflow is one. Operand signs differ and result sign differs from the minuend, matching the subtraction sign criterion.

Trying to negate signed −8 separately would encounter its unrepresentable positive opposite. The subtractor computes a modular difference directly and evaluates subtraction's own overflow condition.

**Lesson.** A staged signed negation and a unified bit subtractor have different intermediate contracts.

### Problem 18. Decimal radix-complement subtraction

**Task.** Compute 289 − 475 using three-digit tens' complements. Recover the negative magnitude.

**Solution.** The three-digit tens' complement of 475 is 1000 − 475 = 525. Adding to 289 yields 814 without a thousands carry. Therefore the low three digits encode a negative modular result. Its magnitude is the tens' complement of 814, namely 186; the answer is −186. Check directly: 475 − 289 = 186.

814 is not the positive answer and must not be presented as such. If binary hardware stores the digit string as BCD, encode each of its digits separately after performing the decimal complement logic.

**Lesson.** A radix-complement word is a modular representation. Interpret the carry and the required signed result before reporting its digits.

### Problem 19. Biased arithmetic and top-bit conversion

**Task.** In five-bit excess-15, encode −7 and +11 and add them. Then explain how excess-16 differs.

**Solution.** The codes are −7 + 15 = 8, word 01000, and 11 + 15 = 26, word 11010. Raw code addition gives 34. Correct one extra bias: 34 − 15 = 19, word 10011. Decoding gives 19 − 15 = 4, the correct sum. The exact answer four lies in range −15 through +16.

In excess-16, the code for the same answer is 20, not 19. That bias permits direct conversion from a five-bit two's complement word by toggling its top bit. With excess-15, the conversion additionally differs by one; the top-bit shortcut alone is wrong.

**Lesson.** A bias is part of the format. Do not replace it with a familiar “approximately half the modulus” value.

### Problem 20. Widening depends on the signed encoding

**Task.** Widen a representation of −3 from five bits to eight bits in two's complement, ones' complement, and sign-magnitude. **Pattern:** Stanford and CMU width-conversion examples, extended to compare formats.

**Solution.** Five-bit two's complement −3 is 11101 and sign-extends to 1111 1101, unsigned 253; 253 − 256 = −3. Five-bit ones' complement −3 is 11100 and extends to 1111 1100, unsigned 252; 252 − 255 = −3. Five-bit sign-magnitude −3 is 10011; move the sign to the new top position and zero-extend magnitude three, giving 1000 0011.

Repeating the original top bit for sign-magnitude would give 1111 0011, magnitude 115 and value −115. A familiar widening rule is valid only for its specified encoding.

**Lesson.** State which decoder must preserve the value, then derive the added bits from that decoder.

### Problem 21. Narrowing without changing the sign can still lose value

**Task.** Narrow eight-bit two's complement 0001 0011 and 1111 0011 to four bits. Does retaining the original sign guarantee value preservation?

**Solution.** The first word is +19; its low four bits 0011 are +3. Both signs are zero, yet value was lost because a discarded bit was one. The second word is −13; its low four bits also are 0011, giving +3 and changing sign. Neither value fits in the four-bit signed interval −8 through +7.

The correct preservation test is that every discarded bit equals the retained sign bit. For +19, discarded bits 0001 are not all zero; for −13, discarded bits 1111 differ from the new retained sign zero. A sign-only check would miss the first failure.

**Lesson.** Sign preservation is necessary but not sufficient for signed narrowing.

### Problem 22. Widen before operating, not afterward

**Task.** Compare “add eight-bit +100 and +60, then sign-extend to sixteen bits” with “sign-extend each operand first, then add.”

**Solution.** Eight-bit low-word addition yields unsigned 160, word 1010 0000, which decodes as −96. Sign-extending that word yields sixteen-bit −96. It preserves the already wrong interpretation; it cannot recreate +160. If operands are extended first, their sixteen-bit codes are 0000 0000 0110 0100 and 0000 0000 0011 1100. Their exact sum is 0000 0000 1010 0000, correctly +160 and within the sixteen-bit range.

**Lesson.** Wider storage only protects operations performed at the wider width. It does not repair an answer already reduced modulo a narrower width.

### Problem 23. Shift rounding for negative values

**Task.** In eight-bit two's complement, compare logical right shift, arithmetic right shift, and truncation-toward-zero division for −11 shifted or divided by four. **Pattern:** CMU shift-rounding comparison.

**Solution.** The stored word is 1111 0101. Logical right shift by two gives 0011 1101, unsigned and signed +61. Arithmetic right shift gives 1111 1101, signed −3, equal to floor(−11/4). Truncation toward zero gives −2. For the latter using arithmetic-shift semantics, add bias three in a sufficiently wide domain: −11 + 3 = −8 and −8/4 = −2 exactly.

The logical shift reinterprets the low bits as part of a nonnegative quotient of unsigned 245. It is not a signed division algorithm.

**Lesson.** “Shift right divides by two” requires both a decoder and a rounding convention.

### Problem 24. Low products agree while full products differ

**Task.** Multiply four-bit words 1110 and 0011 under unsigned and two's complement interpretations. Compare the four low bits and required exact products.

**Solution.** Unsigned multiplication is 14 × 3 = 42, binary 0010 1010 in eight bits. Signed multiplication is −2 × +3 = −6, binary 1111 1010 in eight-bit two's complement. The low four bits are 1010 in both cases. Decoded as four-bit signed they are −6, which is exact; decoded as four-bit unsigned they are ten, which is not the exact unsigned product 42.

The low-bit agreement follows from congruence modulo sixteen. The full high bits differ because the signed inputs differ by a modulus from their unsigned interpretations.

**Lesson.** Agreement of truncated bits does not imply agreement of mathematical products or overflow conditions.

### Problem 25. Choose a format from range and resolution requirements

**Task.** Choose the smallest total two's complement fixed-point width that covers at least −12 through +12 and has spacing no greater than 1/32.

**Solution.** Spacing no greater than 1/32 requires f ≥ 5. With f = 5, the maximum is 2<sup>n−6</sup> − 1/32. At n = 9 this is 8 − 1/32, too small. At n = 10 it is 16 − 1/32, which covers +12, and the minimum is −16, covering −12. Thus ten bits with five fractional bits suffice. A larger f at nine total bits only shrinks the range, so it cannot make nine bits sufficient.

**Lesson.** Satisfy the positive endpoint as well as the negative endpoint. The asymmetric signed maximum includes a one-step subtraction.

### Problem 26. Midpoint rounding in a signed fixed-point format

**Task.** With eight-bit two's complement and three fractional bits, encode +2.3125, +2.4375, and −2.3125 using nearest ties-to-even.

**Solution.** Scale by eight. The values become +18.5, +19.5, and −18.5. The nearest even integers are +18, +20, and −18. Their eight-bit codes are 0001 0010, 0001 0100, and 1110 1110. Dividing the decoded integers by eight gives +2.25, +2.5, and −2.25. Each error magnitude is 1/16, half the spacing.

The parity determining a tie is the parity of the retained integer grid index, not the sign bit or the number of ones in the whole word.

**Lesson.** A tie rule must work consistently on both sides of zero and adjacent retained indices.

### Problem 27. Product scaling and rescaling loss

**Task.** Represent 1.5 and 1.25 with three fractional bits, multiply their integer codes exactly, and return to three fractional bits using nearest ties-to-even.

**Solution.** The codes are twelve and ten. Their product is 120 and initially has six fractional bits, representing 120/64 = 1.875. Returning to three fractional bits requires dividing the code by eight, yielding exactly fifteen, so no quantization loss occurs. The result is code fifteen with value 15/8 = 1.875. An eight-bit signed output can store fifteen easily.

If one kept product code 120 but interpreted it with three fractional bits, the reported value would be fifteen, eight times too large. If the product were formed in an insufficiently wide intermediate, even a small final value could be corrupted before rescaling.

**Lesson.** Track fractional-bit counts through each operation; a product carries the sum of its operands' fractional counts.

### Problem 28. BCD is not hexadecimal and correction is not optional

**Task.** Encode decimal 98 and 76 as BCD, then compute 98 + 76 + 1 using digit correction. Determine the packed result's value if misread as pure binary.

**Solution.** The operands are 1001 1000 and 0111 0110. Units: 8 + 6 + 1 = 15; adding six gives 21, low nibble five and decimal carry one. Tens: 9 + 7 + 1 = 17; its original binary carry is already one, so correction is necessary even though the low nibble is 0001. Adding six to the subtotal gives 23, low nibble seven with decimal carry one. The result is BCD 0001 0111 0101, decimal 175.

As a twelve-bit pure binary word it is hexadecimal 175, which equals 1 × 256 + 7 × 16 + 5 = 373. That is a different decoder, not a contradictory addition result.

**Lesson.** Keep the original carry in the correction decision. Digit legality and binary carry test complementary subtotal cases.

### Problem 29. Compare decimal complements across codebooks

**Task.** Find the digitwise nines' complement of decimal 26 in excess-three and Aiken 2421, and explain why bitwise complement of its BCD code is unsuitable.

**Solution.** The nines' complement is 73. Excess-three 26 is 0101 1001; bitwise complement gives 1010 0110, which decodes as excess-three 73. Aiken 2421 26 is 0010 1100; complement gives 1101 0011, also the designated 73 code. Ordinary BCD 26 is 0010 0110; complement gives 1101 1001, whose first nibble is invalid BCD.

For a two-digit tens' complement, add one decimal unit after obtaining the nines' complement, producing 74, with decimal-digit carry rules. A binary increment of a packed code is not universally a valid digitwise decimal increment.

**Lesson.** Self-complementing decimal codes encode 9 − d by bit complement. They do not turn all decimal arithmetic into ordinary binary arithmetic.

### Problem 30. Weighted validity versus membership in a designated code

**Task.** In weights 2, 4, 2, 1, both 0101 and 1011 sum to five. Are both legal Aiken codewords under this chapter's table?

**Solution.** 0101 contributes zero plus four plus zero plus one, totaling five. 1011 contributes two plus zero plus two plus one, also totaling five. However the designated Aiken table selects 1011 for digit five; 0101 is not a legal designated codeword. Its complement 1010 has weighted value four but is likewise not the selected word for four. The designated pair 0100 and 1011 preserves both weighted values and complement closure.

**Lesson.** A weighted sum is not by itself a complete codebook definition when weights repeat. Validate membership in the specified table.

### Problem 31. Convert and decode Gray words

**Task.** Convert binary index 10110 to reflected Gray code. Decode Gray word 11010. **Pattern:** Princeton reflected Gray instruction, independently chosen conversion data.

**Solution.** For encoding, XOR 10110 with its logical right shift 01011, giving 11101. For decoding 11010, the cumulative XORs from the top are one; 1 XOR 1 = 0; 0 XOR 0 = 0; 0 XOR 1 = 1; and 1 XOR 0 = 1. Thus the binary index is 10011, decimal nineteen. Directly reading Gray 11010 as unsigned gives 26, which is not its index.

**Lesson.** Gray decoding accumulates prefix XORs. The word's ordinary unsigned value is not the physical position index.

### Problem 32. Prove adjacency at a troublesome counter boundary

**Task.** Compare the transition from index seven to index eight in a four-bit natural binary counter and a reflected Gray counter. What about the closing transition from fifteen to zero?

**Solution.** Binary seven is 0111 and eight is 1000; XOR is 1111, so four bits change. Gray seven is 0111 XOR 0011 = 0100. Gray eight is 1000 XOR 0100 = 1100. Their XOR is 1000, so exactly one bit changes. Gray fifteen is 1111 XOR 0111 = 1000; Gray zero is 0000, so the closing edge also changes one bit.

This verifies the specified examples, while the reflected-construction proof earlier establishes adjacency for every width. It does not imply that several nonadjacent skipped positions would still differ once.

**Lesson.** Gray's guarantee concerns neighboring positions in the declared cycle, including its wrap edge.

### Problem 33. Parity and minimum-distance capability

**Task.** Append even parity to data 1011010. Show one detected and one undetected corruption, then classify the two-word code {00000, 11111}. **Pattern:** MIT parity and Hamming-distance teaching.

**Solution.** Four ones already have even parity, so append zero, yielding 10110100. Flip the fourth bit to obtain 10100100; there are now three ones and the check fails. Also flip the first bit, giving 00100100; two flips restore even parity and corruption is undetected.

The separate five-bit repetition code has minimum distance five because its only two valid words differ everywhere. It detects every pattern of up to four flips if used as a validity checker and corrects every pattern of up to two flips by nearest valid word. It cannot guarantee correction of three flips; such a received word can be closer to the wrong codeword.

**Lesson.** Detection and correction use different distance inequalities. State the error bound accompanying a decoder.

### Problem 34. Build and correct a Hamming word

**Task.** Encode data 1011 into Hamming (7,4), placing data from left to right at positions three, five, six, seven. Flip position six and correct it.

**Solution.** Set d<sub>3</sub> = 1, d<sub>5</sub> = 0, d<sub>6</sub> = 1, d<sub>7</sub> = 1. Check bits are p<sub>1</sub> = 1 XOR 0 XOR 1 = 0; p<sub>2</sub> = 1 XOR 1 XOR 1 = 1; p<sub>4</sub> = 0 XOR 1 XOR 1 = 0. In position order one through seven the code is 0110011.

Flipping position six gives 0110001. The low-index check over positions 1, 3, 5, 7 gives zero; the middle-index check over 2, 3, 6, 7 gives one; the high-index check over 4, 5, 6, 7 gives one. Syndrome high-to-low is 110, decimal six. Flipping position six again restores 0110011 and extracting the data positions recovers 1011.

**Lesson.** A syndrome denotes a position only under the assumed single-error model. Position numbering and syndrome bit order must be declared.

### Problem 35. Show why an unextended Hamming decoder can miscorrect

**Task.** Starting from the all-zero Hamming (7,4) codeword, flip positions one and two. What does a naive single-error corrector do? What does added overall parity change?

**Solution.** The syndrome is binary 001 XOR 010 = 011, position three. A naive decoder flips bit three and returns a word with ones at positions one, two, three. That word has zero syndrome and is another valid Hamming codeword, but its data bit at position three changed. The attempted correction therefore produces the wrong message.

With extended overall parity, two flips leave overall parity even while the Hamming syndrome remains nonzero. The SECDED table identifies a detected double error and refuses single-bit correction. This conclusion assumes at most two flips; three or more need a different guarantee.

**Lesson.** Correcting an observed syndrome without validating the decoder's error assumptions can turn detected corruption into a plausible wrong message.

### Problem 36. An integrated design with capacity, precision, and protection

**Task.** A sensor must store values from −10 to +10 inclusive with spacing at most 1/16, using two's complement fixed point. Choose the smallest data width, determine single-error Hamming parity count, and identify the cost of SECDED. Encode sensor value −2.375 in the chosen numerical format.

**Solution.** Spacing requires f ≥ 4. At f = 4, eight total bits give signed range −8 through 7.9375, too small. Nine bits give −16 through 15.9375, sufficient, so choose n = 9 and f = 4. Choosing more fractional bits cannot improve the range at eight bits.

For k = 9 data bits, test parity counts in 2<sup>r</sup> ≥ 9 + r + 1. Three parity bits provide eight syndromes but need thirteen, so fail. Four provide sixteen and need fourteen, so suffice. A shortened single-error Hamming construction therefore uses thirteen total bits. SECDED adds one overall parity bit, for fourteen total bits.

The scaled integer for −2.375 is −38. In nine-bit two's complement its unsigned code is 512 − 38 = 474, word 111011010. Decoding gives (474 − 512)/16 = −38/16 = −2.375. The Hamming layer protects those nine stored data bits; it does not alter the fixed-point decoding or guarantee protection against arbitrary numbers of errors.

**Lesson.** Numerical resolution, representable range, and transmission reliability are separate design constraints. Solve them in that order and record each contract.
