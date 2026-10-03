## Teaching through formulas and conceptual decisions

### Decode the representation before doing arithmetic

For an unsigned$b$-bit word, the value is$\sum_{i=0}^{b-1}x_i2^i$. For two's complement, the most significant bit has weight$-2^{b-1}$ instead. Thus an8-bit word11110110 has unsigned value246 and signed two's-complement value$246-256=-10$. The same physical word can represent different values under different encoding contracts.

Signed addition overflow is detected when equal-sign operands produce an opposite-sign result in a fixed-width two's-complement adder. A carry out alone detects unsigned overflow, not signed overflow. For8 bits,127+1 produces10000000 with no final unsigned carry but with signed overflow;255+1 produces00000000 with unsigned carry but does not represent addition of two positive signed operands.

### Treat binary fractions and fixed point as scaled integers

A binary fraction$0.x_1x_2\ldots$ has weights$2^{-1},2^{-2},\ldots$. A rational$p/q$ in lowest terms terminates in binary exactly when$q$ is a power of two. For a fixed-point word with$f$ fractional bits, the represented value is the decoded integer divided by$2^f$. Addition preserves the scale; multiplication of raw integers doubles the fractional-bit scale and must be rescaled with a specified rounding rule.

### Floating encodings have several regimes

For a specified binary floating format, normal values use an implicit leading1 and exponent field minus bias. Subnormals use no implicit1 and the minimum normal exponent. All-zero exponent and fraction represent signed zero; all-one exponent selects infinities or NaNs depending on the fraction. A decoded bit pattern is therefore not always a finite number. Endianness determines byte order in memory, while bit significance in the value remains unchanged.

## Formula and conceptual problem bank

### Question 1. Base conversion

What is the decimal value of hexadecimal$2D$?

**A.** 29

**B.** 35

**C.** 45

**D.** 52

**Answer: C.**

The digitD represents13. Positional evaluation gives $2\cdot16+13=45$. Reading the letter as a decimal digit or interpreting the string as two decimal characters does not respect the base. A check is binary0010 1101, which has weights32+8+4+1=45.

### Question 2. A binary fraction

What is the decimal value of binary$101.101$?

**A.** 5.125

**B.** 5.5

**C.** 5.625

**D.** 5.75

**Answer: C.**

The integer part is4+1=5. The fractional positions contribute1/2,0/4 and1/8, totaling5/8. Thus the value is5.625. Treating the fractional digits as101/1000 would incorrectly use decimal rather than binary place values.

### Question 3. Minimum unsigned width

What minimum unsigned width can represent every integer from0 through300?

**A.** 8

**B.** 9

**C.** 10

**D.** 300

**Answer: B.**

Eight bits provide256 values and maximum255, insufficient. Nine bits provide512 values and maximum511, sufficient. The exact formula is $\lceil\log_2(301)\rceil=9$. The plus-one counts zero as one of the required values.

### Question 4. Decode two’s complement

Interpret the8-bit word `11110110` as two’s complement. What is its value?

**A.** -9

**B.** -10

**C.** -118

**D.** 246

**Answer: B.**

The unsigned value is246. Since the sign bit is1, subtract256 to obtain$-10$. Alternatively invert to00001001 and add1 to obtain magnitude10. The answer246 uses the unsigned interpretation; sign-magnitude and ones-complement use different negative encodings.

### Question 5. Signed overflow versus carry

In an8-bit two’s-complement adder, add `01111111` and `00000001`. Which flags apply?

**A.** No signed overflow and no carry out.

**B.** Signed overflow but no carry out.

**C.** Carry out but no signed overflow.

**D.** Both flags.

**Answer: B.**

The bit sum is10000000, with no ninth-bit carry. Interpreted signed, the mathematical sum128 is outside the range-128 through127, and two positive inputs produced a negative decoded result. Thus signed overflow occurs. Carry-out is an unsigned-range flag and does not detect this signed case.

### Question 6. Sign extension

What16-bit word preserves the value of the8-bit two’s-complement word `11110110`?

**A.** `0000000011110110`

**B.** `1111111111110110`

**C.** `0000000000001010`

**D.** `1000000011110110`

**Answer: B.**

Copy the sign bit into all eight new leading positions. The resulting unsigned value is65526, which decodes as65526-65536=-10. Zero extension instead gives positive246 and changes the signed value. Sign extension follows from the negative leading weight in two’s complement.

### Question 7. Fixed-point scale

An unsigned8-bit fixed-point format has four fractional bits. What real value is represented by raw integer40?

**A.** 2.5

**B.** 4

**C.** 10

**D.** 40

**Answer: A.**

The scale is$2^4=16$. Divide the raw integer by16, giving40/16=2.5. Four fractional bits means sixteen representable steps per unit, not a division by4 or by ten. The spacing is1/16 and the largest value is255/16.

### Question 8. Binary termination

Which reduced rational number has a finite binary expansion?

**A.** 1/10

**B.** 3/20

**C.** 7/16

**D.** 2/15

**Answer: C.**

The reduced denominator16 is a power of two, so7/16 has a terminating expansion, namely0.0111. Denominators10,20 and15 retain an odd prime factor after reduction and cannot divide a power of two. Termination in decimal does not imply termination in binary.

### Question 9. Reflected Gray encoding

For the4-bit binary word `1011`, what is its reflected Gray code?

**A.** `1110`

**B.** `1010`

**C.** `0111`

**D.** `1101`

**Answer: A.**

Gray encoding is the XOR of the binary word and its one-bit right shift:1011 XOR0101 gives1110. The leading bit is copied; each later Gray bit XORs neighboring binary bits. Gray code minimizes neighboring-code changes but is not a positional arithmetic representation.

### Question 10. BCD validity

Which4-bit word is invalid as one8421 BCD digit?

**A.** `0011`

**B.** `1001`

**C.** `1010`

**D.** `0000`

**Answer: C.**

BCD digit codes represent decimal0 through9.1010 has ordinary binary value10 and lies among the six unused4-bit patterns.1001 represents9 and is valid. A whole decimal number uses one nibble per decimal digit, which differs from encoding the whole number directly in base2.

### Question 11. Little-endian bytes

A32-bit word has hexadecimal value `12345678`. What bytes appear at increasing addresses in little-endian storage?

**A.** `12 34 56 78`

**B.** `78 56 34 12`

**C.** `87 65 43 21`

**D.** `21 43 65 87`

**Answer: B.**

Little-endian places the least significant byte78 first, followed by56,34,12. It reverses byte order relative to the written most-significant-first hexadecimal word, not the order of bits within each byte and not the digits within a byte. The numeric value remains the same once the representation is interpreted correctly.

### Question 12. A small normal floating format

A toy binary format has one sign bit, three exponent bits with bias3 and four fraction bits. A normal code has sign0, exponent100 and fraction0100. What is its value?

**A.** 1.25

**B.** 2.5

**C.** 4.25

**D.** 10

**Answer: B.**

The exponent field is4, so the unbiased exponent is1. The significand is$1.0100_2=1.25$. The value is$1.25\cdot2^1=2.5$. Forgetting the hidden leading1 or using the raw exponent without bias produces a different result. The question explicitly says normal, so subnormal decoding does not apply.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: A fixed-point multiplication with rounding

A signed8-bit two’s-complement fixed-point format has two fractional bits. Raw inputs are$-6$ and5. Multiply their values and round the stored result to nearest, ties to even. What real value is stored?

**A.** -1.75

**B.** -1.875

**C.** -2.0

**D.** -7.5

**Answer: C.**

The inputs mean$-6/4=-1.5$ and$5/4=1.25$, whose exact product is$-1.875$. At the target scale4, the desired raw result is$-7.5$. It is halfway between$-7$ and$-8$; ties-to-even selects$-8$, yielding$-2.0$. The exact product is not representable at quarter-unit spacing. Truncation toward zero would yield$-1.75$, a different rounding rule.

### Question 14. Challenge: Nearest-even binary quantization

Quantize1.625 to an unsigned fixed-point format with two fractional bits, nearest-even rounding and enough integer range. What is the result?

**A.** 1.25

**B.** 1.5

**C.** 1.625

**D.** 1.75

**Answer: B.**

Scale by4 to get raw target6.5, halfway between6 and7. The even raw integer is6, so the stored value is6/4=1.5. Rounding ties upward would choose1.75 instead. The tie rule applies to the retained integer significand or raw field, not to the parity of the decimal printed value.

## Applicable formulas and examination notes

### 1. Position weights

In base$r$, multiply each digit by its power of$r$, with negative powers after the point. Hexadecimal2D is45 and binary101.101 is5.625. Digit validity must be checked before evaluation.

### 2. Width bounds

Unsigned$b$ bits cover0 through$2^b-1$; two’s complement covers$-2^{b-1}$ through$2^{b-1}-1$. To include unsigned maximum$M$, require $b\ge\lceil\log_2(M+1)\rceil$. The signed interval is asymmetric.

### 3. Signed decoding

For a two’s-complement word with sign1, subtract$2^b$ from its unsigned value.11110110 is246 unsigned but-10 signed. Do not decode the same word by a sign-magnitude rule unless the format explicitly changes.

### 4. Negation boundary

Invert bits and add1 to negate a two’s-complement value modulo$2^b$. The minimum signed value negates to the same bit pattern and has no positive counterpart in that width. This is a representability boundary, not an ordinary equality of mathematical integers.

### 5. Two overflow flags

Signed overflow occurs when same-sign inputs yield an opposite-sign result. Unsigned overflow is a carry beyond the width.127+1 in8 bits illustrates signed overflow without carry. The flags answer different questions.

### 6. Extension rules

Sign-extend two’s complement by copying its sign bit; zero-extend unsigned words. Extending11110110 with zeros changes its signed interpretation from-10 to246. A representation-preserving conversion must follow the original value contract.

### 7. Fixed-point scaling

With$f$ fractional bits, divide the raw decoded integer by$2^f$. Multiplying two such words produces a raw product with$2f$ fractional bits; rescale before storing back and specify rounding and overflow. Integer multiplication alone does not preserve the original scale.

### 8. Terminating fractions

A reduced denominator gives a finite binary expansion exactly when it divides a power of two.7/16 terminates;1/10 repeats. Always reduce the fraction first, because removable odd factors do not obstruct termination.

### 9. Gray transformations

Encode reflected Gray as `b XOR (b >> 1)`. Decode by cumulative XOR from the leading bit. Adjacent reflected Gray codes differ in one bit, but adding codewords as ordinary binary does not preserve represented numeric addition.

### 10. BCD correction

8421 BCD has valid digit codes0000 through1001. A digit sum exceeding9 requires decimal correction, not just ordinary4-bit truncation. Distinguish a BCD carry between decimal digits from a binary carry between bit positions.

### 11. Endianness

Little-endian changes byte placement, not bit significance inside a byte.12345678 appears as78 56 34 12 at increasing addresses. Byte swapping and reversing every bit are different operations.

### 12. Floating regimes

For a normal field use$(-1)^s(1.f)2^{E-\mathrm{bias}}$. An all-zero exponent uses subnormal or zero rules; an all-one exponent selects infinity or NaN. A decoder must classify the regime before applying the normal formula.

<!-- BOUNDARY-NOTES -->

### 13. Two zero encodings

Sign-magnitude and ones-complement formats can encode both positive and negative zero; two's complement has one zero and one extra negative endpoint. Decoding or counting representable distinct values must distinguish bit patterns from numeric values.

### 14. Narrowing and representability

Dropping high bits preserves an unsigned or two's-complement value only when the original value fits the target range under the intended conversion rule. Matching a low-bit pattern does not prove the original mathematical value was retained.

### 15. Subnormal spacing

Subnormals use the minimum normal exponent without the hidden leading one and have uniform spacing down to zero. They extend range while sacrificing relative precision. Applying the normal hidden-one formula to an all-zero exponent invents the wrong value.

### 16. Rounding carry into exponent

Rounding a significand can turn an all-ones fractional tail into a leading carry, requiring exponent adjustment. Overflow and underflow classification follow that adjustment. A guard, round and sticky-bit rule must state the rounding mode.
