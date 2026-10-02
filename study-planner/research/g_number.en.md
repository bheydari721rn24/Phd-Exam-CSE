# Number Bases and Binary Encoding

## 1. Scope, prerequisites, and reviewed sources

This chapter develops the mathematical meaning of finite binary representations. You will learn to convert integer and fractional numerals, select a sufficient word width, interpret signed encodings, prove complement identities, diagnose arithmetic overflow, change widths safely, and reason about decimal, Gray, and error-control codes. The central habit is to separate **the stored word**, **its interpretation**, and **the operation performed on it**. A calculation can produce the correct low bits while failing to represent the intended mathematical answer.

Prerequisites are integer division with remainder, powers, finite sums, elementary inequalities, and the exclusive-or operation. For single bits, exclusive-or returns one when its inputs differ. We use it before studying Boolean circuit synthesis; no knowledge of gate minimization is assumed. A bit is an abstract value zero or one. Actual voltage thresholds and timing belong to later circuit chapters.

### Source selection and how the courses fit together

Four complementary core courses were selected from a documented pool of eight university offerings. Two further written courses supply advanced arithmetic and Gray-code perspectives. Selection is based on accessible written instruction, relevance to the declared scope, derivational quality, useful problem patterns, and identifiable assumptions. It is a bounded comparison of the sources inspected, not a claim to have reviewed every course that exists.

| Role | University and course | Written material actually reviewed | Contribution and necessary qualification |
|---|---|---|---|
| Core | MIT, 6.004 Computation Structures, Spring 2017; Chris Terman | Chapter 1 annotated slides: fixed-length encodings, unsigned and signed integers, complement arithmetic, Hamming distance, parity, correction | Connects representation to coding capacity and reliability. Arithmetic is qualified by width and representability; variable-length compression is outside this chapter. |
| Core | UC Berkeley, CS61C; course teaching team | Binary, Decimal, Hex; Integer Representations, including sign-magnitude, ones' complement, two's complement, and bias | Compares alternative encodings and their tradeoffs. Ones' complement addition needs end-around carry; signed zero is not a negative value. |
| Core | Stanford, CS107, Winter 2020; Jerry Cain and Lisa Yan | Lecture 2: PDF pages 8–50, 53–84, and 109–114 | Develops positional notation, complement construction, overflow boundaries, extension, and truncation. Machine-specific sizes and C conversion shortcuts are not universal language rules. |
| Core | Cornell, CS3410, Fall 2024; Adrian Sampson and Giulia Guidi, course notes | Switches and Numbers; Real Numbers in Binary and Fixed-Point Numbers within Floating Point | Adds explicit conversion algorithms and the distinction between scale metadata and stored bits. Floating-point format claims must be restricted to a stated format. |
| Supplement | Carnegie Mellon, 15-213/14-513/15-513, Spring 2025; course teaching team | From Bits through Integers, January 16: PDF pages 7–10, 19, 21–35, 39–64 | Supplies modular arithmetic, narrowing, product width, and shift-rounding comparisons. Abstract word operations are separated from C signed overflow and integer promotions. |
| Supplement | Princeton, Algorithms course resources; Robert Sedgewick and Kevin Wayne | Combinatorial Search, PDF pages 35–37, visually checked against the original slides | Supplies the reflected Gray construction, subset transitions, and rotary encoders. Gray values must be decoded before ordinary arithmetic. |

The source and quality audits record exact links, access limitations, coverage decisions, and finite checks. All exposition, proofs, numerical examples, diagrams, and solutions below are independently written. Problems identified as course-pattern adaptations teach the corresponding idea with original wording or data; the chapter does not reproduce complete copyrighted exercise collections.

### Boundaries that prevent hidden gaps

The scope includes positional bases, rational expansions, unsigned and three signed integer encodings, biased encoding, radix complements, word arithmetic and flags, widening and narrowing, shifts, fixed-point quantization, BCD and self-complementing decimal codes, reflected Gray code, and introductory error-control coding. We also derive a small Hamming code so that parity and correction are not merely slogans.

Full IEEE floating-point formats, NaNs, byte order, and character encodings are developed in the programming representation chapter. Gate-level adders, code converters, and sequential counters are developed in the corresponding logic-circuit chapters. We explain their numerical contracts here, but do not pretend that a proof about numbers is a transistor implementation. Archived Iranian entrance-exam questions remain reserved for the final month. The examination guidance here is mathematical problem-solving guidance, not a statistical analysis of those deferred papers.

## 2. Positional notation and the meaning of a word

### Digits, radix, and place values

A radix is an integer b ≥ 2. A legal digit has a value from zero through b − 1. The digit characters A through F denote values ten through fifteen in hexadecimal; they are not variables when used inside a hexadecimal numeral. The subscript on a numeral declares its base. Thus 101<sub>2</sub> and 101<sub>10</sub> name different values.

For digits d<sub>m−1</sub> through d<sub>0</sub>, the rightmost integer digit has weight one. Moving one place left multiplies the weight by b. Fractional places instead have weights b<sup>−1</sup>, b<sup>−2</sup>, and so forth.

<div class="formula-block"><math display="block"><mrow><mi>x</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mo>−</mo><mi>f</mi></mrow><mrow><mi>m</mi><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>d</mi><mi>i</mi></msub><msup><mi>b</mi><mi>i</mi></msup></mrow></math></div>

Here m is the number of integer places and f is the number of fractional places. For example, 2B.6<sub>16</sub> means 2 × 16 + 11 + 6/16 = 43.375. The radix point separates weights one and 1/b. It is not physically stored in a fixed-point word; a decoding convention supplies its position.

A nonnegative integer has a unique finite base-b expansion once unnecessary leading zeros are removed. To prove uniqueness, suppose two different legal expansions describe the same integer. Reducing their values modulo b forces their last digits to be equal because both remainders lie between zero and b − 1. Subtract that common last digit and divide by b. The same reasoning forces the next digits to agree. Repetition contradicts the assumption that the expansions differ. This proof will also explain the repeated-division algorithm.

### Capacity and digit count

A word of n binary positions has 2<sup>n</sup> distinct patterns. If M distinct states must have distinct fixed-length codes, at least n = ⌈log<sub>2</sub> M⌉ bits are necessary. The result is a capacity statement, not an unsigned maximum. There are 2<sup>n</sup> patterns, but the greatest n-bit unsigned value is 2<sup>n</sup> − 1 because counting begins at zero.

For a positive integer N, the minimum number of base-b digits is ⌊log<sub>b</sub> N⌋ + 1. Zero still needs one written digit by convention. In exact computations, repeated division or integer bit length is safer than a floating logarithm near powers of the base. To encode every integer in an inclusive interval from L to H, a freely chosen injective code needs ⌈log<sub>2</sub>(H − L + 1)⌉ bits. A mandated representation may need more. For example, sixteen states fit in four bits, but standard two's complement cannot encode the interval from zero through fifteen in four bits.

### Bits have no inherent signedness

The eight-bit word 1110 1001 is unsigned 233, two's complement −23, ones' complement −22, or sign-magnitude −105. With unsigned fixed-point scaling by 2<sup>−4</sup>, it is 14.5625. With signed scaling by the same factor, it is −1.4375. The bits alone do not choose an answer.

<figure class="number-diagram"><svg viewBox="0 0 720 260" role="img" aria-labelledby="interpret-title interpret-desc"><title id="interpret-title">One word, several decoding contracts</title><desc id="interpret-desc">The word 11101001 branches to unsigned 233, two's complement minus 23, sign-magnitude minus 105, and signed fixed-point minus 23 divided by 16.</desc><rect x="228" y="14" width="264" height="52" rx="10" fill="#edf5fa" stroke="#89aec4"/><text x="360" y="47" text-anchor="middle" class="math-label">1110 1001</text><path d="M360 66V96M85 96H635M85 96V128M270 96V128M450 96V128M635 96V128" stroke="#6997ac" fill="none" stroke-width="2"/><g fill="#f5f8fa" stroke="#c3d6df"><rect x="10" y="128" width="150" height="86" rx="8"/><rect x="195" y="128" width="150" height="86" rx="8"/><rect x="375" y="128" width="150" height="86" rx="8"/><rect x="560" y="128" width="150" height="86" rx="8"/></g><g text-anchor="middle"><text x="85" y="154">Unsigned</text><text x="85" y="185" class="math-label">233</text><text x="270" y="154">Two's complement</text><text x="270" y="185" class="math-label">−23</text><text x="450" y="154">Sign-magnitude</text><text x="450" y="185" class="math-label">−105</text><text x="635" y="154">Signed fixed-point</text><text x="635" y="185" class="math-label">−23 / 16</text></g></svg><figcaption>The decoder supplies width, signed encoding, and scale. No single decimal value follows from an unlabeled word.</figcaption></figure>

## 3. Converting integer numerals correctly

### Conversion to a numerical value: expansion and Horner's rule

Expanding place values always works. For long integers, Horner's rule reduces arithmetic: begin with zero, then for each digit from left to right multiply the accumulated value by b and add the next digit. For 3A7<sub>16</sub>, the successive values are 3, 3 × 16 + 10 = 58, and 58 × 16 + 7 = 935.

The invariant is that the accumulated value equals the value of the prefix already processed. Appending a digit shifts the entire prefix one place left, multiplying it by b, then adds the digit. This proves the algorithm and explains why illegal digits must be rejected before evaluation. A hexadecimal character F is valid in base sixteen and invalid in base twelve.

### Conversion from a nonnegative integer: repeated division

The division theorem writes N = bq + r with 0 ≤ r < b. The remainder is exactly the least significant digit; the quotient is the value of the remaining prefix. Apply the theorem to each quotient until it becomes zero. Record remainders in discovery order, then reverse them to obtain the written numeral.

Convert 347 to base seven. The divisions are 347 = 7 × 49 + 4, 49 = 7 × 7 + 0, 7 = 7 × 1 + 0, and 1 = 7 × 0 + 1. The remainders are 4, 0, 0, 1, so the result is 1004<sub>7</sub>. The internal zeros must be retained: 1 × 343 + 4 = 347. Dropping them would change the positions and the value.

After k divisions, the original value equals the remaining quotient times b<sup>k</sup> plus the already extracted weighted digits. Each positive quotient strictly decreases when b ≥ 2, so the algorithm terminates. For input zero, return the numeral zero explicitly; a loop that only executes while the quotient is positive otherwise returns an empty string.

### Grouping for power-of-two bases

If b = 2<sup>k</sup>, one base-b digit represents exactly k consecutive binary bits. This works because a block beginning at bit position kj contributes its internal binary value multiplied by 2<sup>kj</sup> = b<sup>j</sup>. Octal therefore groups three bits and hexadecimal groups four. This is a proof of place-value preservation, not just a memorization trick.

Start grouping integer bits at the radix point and move left. Add zero padding on the left only to complete the outermost group. Start grouping fractional bits at the radix point and move right; pad the last group on the right. Thus 110101.1011<sub>2</sub> becomes 0011 0101 . 1011, or 35.B<sub>16</sub>; in octal it becomes 110 101 . 101 100, or 65.54<sub>8</sub>. Both describe 53.6875.

Leading zero padding preserves the value of an **unsigned positional numeral**. Extending a signed word is a different operation: changing four-bit two's complement 1111 to eight-bit 0000 1111 changes −1 to +15. Use the extension rules later in this chapter. Similarly, hexadecimal notation compresses bits but does not specify signedness or width. A hex digit F can be a four-bit word or the low nibble of a much wider positive integer.

### Unknown-base equations

An equation involving an unknown radix is a polynomial equation plus digit-validity constraints. For example, 23<sub>b</sub> = 17<sub>10</sub> gives 2b + 3 = 17, so b = 7, which is legal because the largest digit is three. A numerical root smaller than or equal to a digit is inadmissible. For multi-digit unknown-base equations, inspect whether there are several legal integer roots; do not assume uniqueness from the notation alone.

## 4. Fractional expansions, repetition, and accuracy

### Repeated multiplication and its invariant

For 0 ≤ x < 1, multiply by b. The integer part is the next fractional digit; the remaining fraction becomes the input to the next iteration. For x = 13/16 in binary, the successive products are 13/8 = 1 + 5/8, 5/4 = 1 + 1/4, 1/2 = 0 + 1/2, and 1 = 1 + 0. The extracted digits are 1101 in that order, so x = 0.1101<sub>2</sub>. Fractional digits are not reversed.

After k steps, let r<sub>k</sub> be the remaining fraction. The invariant is:

<div class="formula-block"><math display="block"><mrow><mi>x</mi><mo>=</mo><munderover><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>k</mi></munderover><msub><mi>d</mi><mi>j</mi></msub><msup><mi>b</mi><mrow><mo>−</mo><mi>j</mi></mrow></msup><mo>+</mo><msub><mi>r</mi><mi>k</mi></msub><msup><mi>b</mi><mrow><mo>−</mo><mi>k</mi></mrow></msup></mrow></math></div>

Because 0 ≤ r<sub>k</sub> < 1, truncating after k digits has error below b<sup>−k</sup>. For a negative number, apply the positional conversion to its absolute value and retain a mathematical minus sign. Encoding a negative fixed-point value requires a separate signed-word decision.

### When does a rational expansion terminate?

Write a rational number in lowest terms as p/q with q positive. A finite base-b expansion with f fractional places represents an integer divided by b<sup>f</sup>. Hence p/q can terminate only if q divides b<sup>f</sup>: coprimality prevents the numerator from cancelling any missing denominator factor. Conversely, if q divides b<sup>f</sup>, multiplying p/q by b<sup>f</sup> gives an integer, so an exact finite expansion exists. This proves both directions.

Equivalently, every prime factor of q must divide b. In binary, q must be a power of two. The fraction 3/40 terminates in decimal because 40 = 2<sup>3</sup> × 5, but repeats in binary because the factor five never divides a power of two. The fraction 1/6 does not terminate in either binary or decimal; its denominator contains the missing prime three.

If q and b have the same prime factors, the minimum f is obtained by comparing exponents. If q contains prime p to exponent α and b contains it to exponent β, then fβ ≥ α. Take the maximum required ceiling over the denominator's primes. This computes the shortest terminating length exactly.

### Repeating blocks and eventually repeating expansions

For exact rational conversion, track integer remainders rather than approximate decimal fractions. If the current remainder is r, divide br by q to obtain the next digit and next remainder. There are only q possible remainders. Reaching zero ends the expansion; otherwise a remainder eventually repeats and the subsequent digit sequence repeats. The first repeated remainder marks the start of the repeating block, which may follow a nonrepeating prefix.

For 1/10 in binary, the remainders after extracting successive digits are 2, 4, 8, 6, 2, … . The digits are 0, 0, 0, 1, 1, then the cycle repeats from remainder two. Thus 1/10 = 0.0<span class="repeat">0011</span><sub>2</sub>, where the overbar applies to the four digits 0011. Equivalently its expansion begins 0.0001100110011… . The first zero is a nonrepeating prefix; the following four-bit block repeats.

If a block of k base-b digits has integer value A, then 0.<span class="repeat">block</span><sub>b</sub> = A/(b<sup>k</sup> − 1). To prove it, multiply the repeating value by b<sup>k</sup> and subtract the original; all trailing copies cancel, leaving A. With a prefix of length t and value P, followed by the repeating block, the value is P/b<sup>t</sup> + A/[b<sup>t</sup>(b<sup>k</sup> − 1)]. Leading zeros in the block still count toward k.

Finite expansions also have an alternative infinite tail of digits b − 1. For instance, 0.1000…<sub>2</sub> = 0.0111…<sub>2</sub>. The tail sums to 1/2. This does not violate the uniqueness proof for **finite integer** expansions; the representation class has changed. Use terminating expansions as the canonical choice when possible.

### Truncation, rounding, and a stopping rule

For nonnegative x, truncation after f binary fractional bits discards a remainder strictly smaller than Δ = 2<sup>−f</sup>. Rounding to the nearest representable grid point has error at most Δ/2 when the chosen point lies in range. At exact midpoints, a tie rule is necessary: ties to even, ties away from zero, or another declared policy can give different bits. A guard bit alone does not decide ties; lower discarded bits distinguish an exact midpoint from a value beyond it.

To guarantee absolute truncation error below ε, choose f so that 2<sup>−f</sup> ≤ ε. To guarantee nearest-rounding error at most ε, choose 2<sup>−f−1</sup> ≤ ε and check the endpoint range. These are absolute-error statements. Relative error can become arbitrarily large near zero, so do not infer a universal percentage accuracy from the number of fractional bits.

## 5. Signed encodings and complements

### Unsigned interpretation

For an n-bit word, let U be its ordinary unsigned value and let s be its most significant bit. The unsigned range is 0 through 2<sup>n</sup> − 1. Every pattern has a unique unsigned value. Arithmetic on stored low n bits uses residues modulo 2<sup>n</sup>; exact mathematical arithmetic is a separate layer.

### Sign-magnitude

Reserve the top bit as a sign and interpret the remaining n − 1 bits as magnitude m. The value is (−1)<sup>s</sup>m. The range is −(2<sup>n−1</sup> − 1) through +(2<sup>n−1</sup> − 1). Both 000…0 and 100…0 represent numerical zero.

Negation toggles the sign bit while preserving the magnitude. Addition must inspect signs: equal signs require adding magnitudes and retaining the sign; opposite signs require subtracting the smaller magnitude from the larger and keeping the larger magnitude's sign. For five-bit sign-magnitude, +9 is 01001 and −6 is 10110. Their sum is +3, encoded 00011. Adding the entire stored words as ordinary binary would instead produce 11111, which means −15: the encoding does not preserve ordinary binary addition.

### Ones' complement

For a nonnegative magnitude m, encode +m normally and −m by complementing every bit of that positive word. Since an n-bit complement has unsigned value 2<sup>n</sup> − 1 − U, decoding is U when s = 0 and U − (2<sup>n</sup> − 1) when s = 1. The range is the same symmetric range as sign-magnitude. All zeros encode +0; all ones encode −0.

Negation complements the entire word. For addition, retain the low n bits and add any carry-out back into the least significant position: **end-around carry**. This reflects residue arithmetic modulo 2<sup>n</sup> − 1. In four bits, −3 is 1100 and −2 is 1101. Their unsigned sum is 11001; taking only 1001 gives −6, which is wrong. Adding the discarded carry yields 1010, which represents −5. End-around carry fixes the off-by-one result. A representability check is still required: +6 + +3 is outside the four-bit range and cannot become a valid exact signed answer merely by applying this rule.

Positive and negative zero are alternative encodings of the same integer value. A leading one in ones' complement does not by itself prove that the value is strictly negative; all ones is zero. Similarly sign-magnitude 100…0 is zero. This exception matters when counting strictly positive and strictly negative values.

### Two's complement: definition and modular proof

Replace the unsigned top-bit weight +2<sup>n−1</sup> by −2<sup>n−1</sup>. The lower weights stay positive. Equivalently:

<div class="formula-block"><math display="block"><mrow><mi>T</mi><mo>=</mo><mo>−</mo><msub><mi>b</mi><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msub><msup><mn>2</mn><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup><mo>+</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>−</mo><mn>2</mn></mrow></munderover><msub><mi>b</mi><mi>i</mi></msub><msup><mn>2</mn><mi>i</mi></msup></mrow></math></div>

<div class="formula-block formula-steps"><div>T = U − s·2<sup>n</sup>.</div><div>Range: −2<sup>n−1</sup> ≤ T ≤ 2<sup>n−1</sup> − 1.</div><div>Encode a representable integer x as U = x mod 2<sup>n</sup>.</div></div>

For example, eight-bit 1010 1101 has unsigned value 173 and signed value 173 − 256 = −83. Direct weighting gives −128 + 32 + 8 + 4 + 1 = −83. These are two equivalent checks.

To negate the word, complement all n bits and add one, discarding any extra carry. The unsigned complement is 2<sup>n</sup> − 1 − U, so complement-plus-one is congruent to −U modulo 2<sup>n</sup>. That is exactly the encoded additive inverse. The formula is a statement about a fixed-width bit operation; it is not permission to ignore language evaluation rules.

Only zero and the most negative word negate to themselves. The latter has unsigned value 2<sup>n−1</sup>; its additive inverse is the same residue because 2 × 2<sup>n−1</sup> = 2<sup>n</sup>. Its mathematical positive opposite is outside the signed range. For eight bits, negating −128 produces word 1000 0000 again and signals signed overflow if exact negation was intended. Widening to nine bits first permits the exact opposite +128.

There are 2<sup>n−1</sup> negative values, 2<sup>n−1</sup> − 1 strictly positive values, and one zero. All ones represent −1, not the most negative value. The most negative word is one followed by zeros.

### A comparison table that includes the exceptions

| Encoding | Decoder from an unsigned word U | Range | Zero patterns | Negation |
|---|---|---|---|---|
| Unsigned | U | 0 to 2<sup>n</sup> − 1 | All zeros | Modular inverse exists, but usually is not a nonnegative mathematical opposite. |
| Sign-magnitude | (−1)<sup>s</sup>(U − s2<sup>n−1</sup>) | −(2<sup>n−1</sup> − 1) to 2<sup>n−1</sup> − 1 | All zeros; top bit only | Toggle the sign bit. |
| Ones' complement | U − s(2<sup>n</sup> − 1) | −(2<sup>n−1</sup> − 1) to 2<sup>n−1</sup> − 1 | All zeros; all ones | Complement all bits. |
| Two's complement | U − s2<sup>n</sup> | −2<sup>n−1</sup> to 2<sup>n−1</sup> − 1 | All zeros | Complement and add one; the minimum is exceptional as an exact integer operation. |
| Excess-K | U − K | −K to 2<sup>n</sup> − 1 − K | Unsigned word K, if K is in range | Encode the opposite value, checking range. |

### Biased encoding and why its order is convenient

An excess-K code stores x + K as an unsigned word. Decoding subtracts K. For a fixed bias, unsigned ordering of code words agrees with numerical ordering of decoded values. In five-bit excess-15, the range is −15 through +16, zero is 01111, and −7 is 01000. The bias need not be 2<sup>n−1</sup> − 1; it must be specified.

Biased arithmetic needs bias correction. If words A and B encode x and y, their ordinary sum encodes x + y + 2K, so an encoded result for x + y is A + B − K, subject to range and width. Subtraction uses A − B + K. Adding raw biased words without this correction produces the wrong decoded value.

For bias 2<sup>n−1</sup>, converting a two's complement word to excess-bias form toggles the top bit. Proof: adding that bias to the signed value shifts the lower half of the signed range to unsigned codes zero through 2<sup>n−1</sup> − 1 and the upper half to the remaining codes. This shortcut does not apply unchanged to bias 2<sup>n−1</sup> − 1.

### Complements in any radix

For a nonnegative n-digit base-b integer A, the diminished-radix complement is b<sup>n</sup> − 1 − A; compute it by replacing each digit d with b − 1 − d. The radix complement is (b<sup>n</sup> − A) mod b<sup>n</sup>; compute it by adding one to the diminished complement and retaining n digits. Binary gives ones' and two's complements. Decimal gives nines' and tens' complements.

For A − B, add A to the radix complement of B and retain n digits. A carry-out generally marks A ≥ B when B is nonzero; B = 0 is an important convention exception because its stored radix complement is zero. Adding A + (b<sup>n</sup> − 1 − B) + 1 as an n+1-digit computation retains a consistent no-borrow flag even at B = 0. If the mathematical result is negative, the low digits are its modular encoding, not its unsigned magnitude. Complement them again to recover the magnitude.

## 6. Word arithmetic, carry, borrow, and overflow

### The exact answer and the stored answer

Let M = 2<sup>n</sup>. For unsigned words A and B, the low-word sum is R = (A + B) mod M. The carry-out is one exactly when A + B ≥ M. Since each operand is at most M − 1, their sum needs at most n + 1 bits and can wrap at most once. The same low-word adder computes the residues of two's complement addition because the encoded operands are congruent to their signed values modulo M.

**Unsigned overflow** means the exact unsigned result is outside zero through M − 1. For addition it agrees with carry-out. **Signed overflow** means the exact signed result is outside −M/2 through M/2 − 1. It does not generally agree with carry-out. Four-bit 0111 + 0001 produces 1000 with no final carry, but +7 + +1 = +8 is not representable. Conversely 1111 + 0001 produces 0000 with a final carry, but −1 + +1 = 0 is a valid signed answer.

### Sign criterion for signed addition

Adding operands of different signs cannot overflow: the exact sum lies between the operands. Adding two nonnegative operands overflows exactly when the stored result has a negative sign. Adding two negative operands overflows exactly when the stored result has a nonnegative sign. Thus if operand signs are s<sub>A</sub>, s<sub>B</sub> and the result sign is s<sub>R</sub>, then:

<div class="formula-block">V = (s<sub>A</sub> = s<sub>B</sub>) and (s<sub>R</sub> ≠ s<sub>A</sub>).</div>

The criterion applies to **addition without a separate carry-in**, or to an explicitly analyzed adder contract. When arithmetic is part of a chained multiword operation, compute the full exact sum including the carry-in before deciding signed representability.

### Carry into and out of the sign position

Let c<sub>i</sub> be the carry into bit i, so c<sub>0</sub> is zero for ordinary addition and c<sub>n</sub> is the final carry. At each bit, a<sub>i</sub> + b<sub>i</sub> + c<sub>i</sub> = r<sub>i</sub> + 2c<sub>i+1</sub>. Multiplying these equations by positional weights and telescoping proves the low-word sum and carry formula.

At the top position, signed overflow is c<sub>n−1</sub> ⊕ c<sub>n</sub>. An instructive derivation avoids blindly memorizing an XOR rule. The lower n − 1 bits contribute a carry into the sign position. Substituting negative weights for the top bits gives the exact signed sum equal to the decoded stored result plus (c<sub>n−1</sub> − c<sub>n</sub>)M. If the carries match, that correction is zero. If they differ, the decoded stored result is displaced by one full modulus and cannot be the exact representable answer. This also works with a specified carry-in when the exact total includes that carry-in.

### Subtraction and the no-borrow convention

Compute A − B as A + complement(B) + 1 in an n+1-bit adder. Its exact unsigned intermediate is A + M − 1 − B + 1 = A − B + M. Therefore final carry is one exactly when A ≥ B. In this convention, carry means **no borrow**; an unsigned borrow flag is its complement. Some processors expose different flag conventions, so state the convention rather than giving an unlabeled carry value.

For two's complement subtraction, overflow requires different operand signs and a stored result sign different from the minuend's sign:

<div class="formula-block">V = (s<sub>A</sub> ≠ s<sub>B</sub>) and (s<sub>R</sub> ≠ s<sub>A</sub>).</div>

Why? Subtracting a nonnegative value from a negative value can go below the minimum; subtracting a negative value from a nonnegative value can exceed the maximum. Same-sign subtraction cannot exceed either signed bound. The direct criterion remains valid even when B is the most negative word. Negating B as a separate signed integer operation first would itself overflow; a unified complement-plus-one subtractor operates on bits and must be assessed as subtraction.

### Multiplication and division boundaries

Two n-bit unsigned operands may need 2n product bits because (2<sup>n</sup> − 1)<sup>2</sup> fits in 2n bits. Two n-bit two's complement operands also need up to 2n signed bits: minimum times minimum is 2<sup>2n−2</sup>, which exceeds the maximum of a signed 2n − 1-bit format. The low n product bits agree for unsigned and signed interpretations of the same operand words; the full products generally do not.

For truncated multiplication, unsigned overflow means the discarded upper bits are nonzero. Signed overflow means the full product does not fit the target signed interval; equivalently the discarded upper bits must all equal the retained result's sign bit for value preservation. Do not use the addition carry criterion for multiplication.

Division by zero is undefined as integer arithmetic. Minimum divided by −1 gives a quotient outside the n-bit signed range. The usual remainder equation x = qy + r must include a rounding convention for q. Truncation toward zero and floor division differ for negative inputs. These distinctions will reappear in fixed-point rescaling.

### Ordering and modular differences

Unsigned comparison orders unsigned values. For two's complement words with different sign bits, the negative operand is smaller. Within the same sign half, unsigned ordering agrees with signed ordering. Sorting all raw words as unsigned therefore places the negative signed values after the nonnegative values.

The sign of a truncated difference is not a universally correct signed comparison. If subtraction overflows, its sign can be opposite to the true mathematical difference. Use the operand signs first or use the result sign together with the signed-overflow flag; for a two's complement subtractor, signed less-than is s<sub>R</sub> ⊕ V. This formula assumes the specified operands are signed words of the same width.

## 7. Changing widths and shifting bits

### Widening with a value-preservation proof

Unsigned widening adds zero bits on the left. Two's complement widening repeats the sign bit. If x is negative, its n-bit unsigned code is x + 2<sup>n</sup>. Adding k leading ones increases that unsigned code by 2<sup>n+k</sup> − 2<sup>n</sup>. Decoding at the wider width subtracts 2<sup>n+k</sup>, recovering x. This proves sign extension rather than merely illustrating it.

Ones' complement also repeats the sign bit; its decoder subtracts 2<sup>n+k</sup> − 1, and the same added leading-ones contribution preserves the value. Sign-magnitude instead relocates the original sign to the new top position and zero-extends the magnitude. Five-bit sign-magnitude −3 is 10011; widening to eight bits yields 1000 0011, not 1111 0011. The latter would represent −115 in sign-magnitude.

### Narrowing and recoverability

Keeping the low m bits computes U mod 2<sup>m</sup>. An unsigned value is preserved exactly when every discarded high bit is zero. A two's complement value is preserved exactly when every discarded bit equals the **new retained sign bit**. That qualification is crucial: merely discarding bits equal to the old sign bit is insufficient if the new sign changes.

For example, eight-bit +15 is 0000 1111. Discarded bits are zeros, but the new four-bit sign is one; the retained word decodes as −1. In contrast eight-bit −3 is 1111 1101 and narrowing to four-bit 1101 preserves −3 because the discarded ones match its retained sign.

Widening after narrowing cannot recover information that was discarded. It returns the original value only if the narrowing preserved the value. Widening before addition can prevent arithmetic overflow; widening an already truncated answer only reinterprets the damaged result at a greater width.

### Logical and arithmetic shifts

A logical right shift introduces zeros at the top. For unsigned x, shifting right by k gives ⌊x/2<sup>k</sup>⌋. An arithmetic right shift repeats the sign bit. For two's complement x, its abstract word result represents ⌊x/2<sup>k</sup>⌋, including for negative values. Thus arithmetic shifting −11 right by two gives −3, whereas division with truncation toward zero gives −2.

For negative x, truncation toward zero can be computed mathematically as ⌊(x + 2<sup>k</sup> − 1)/2<sup>k</sup>⌋. Proof: write x = q2<sup>k</sup> + r with 0 ≤ r < 2<sup>k</sup>. When r is zero, the bias still floors to q; when r is positive, it floors to q + 1, which moves the negative quotient toward zero. The bias formula must be evaluated in a sufficiently wide domain; it is not a blanket guarantee about a language expression.

An abstract n-bit left shift keeps the low bits of x2<sup>k</sup>. Its unsigned value is (U2<sup>k</sup>) mod 2<sup>n</sup>. As exact signed multiplication it is valid only if the product is in range. For six-bit x = −5, multiplying by four gives −20, which is representable; multiplying by eight gives −40, which is not. The low-bit operation still produces a word, but the exact signed operation fails.

An abstract right shift and rotate are different operations. A rotate wraps discarded bits into the vacated positions; it generally is not division. A negative or out-of-width shift count has no meaning under the word-operation contract used here. Programming languages may reject it or define separate masking behavior. C17 signed overflow is undefined, signed negative right shift is implementation-defined, and integer promotions can change the operand width before shifting. The numerical laboratory models declared abstract words, not C expressions.

## 8. Fixed-point representation and quantization

### Declare the format before placing the point

We specify total width n, signed encoding, and number f of fractional bits. The decoded value is x = I·2<sup>−f</sup>, where I is the decoded integer. This convention avoids ambiguity in names such as Q3.4, whose sign-bit convention varies between sources. A negative f is also mathematically possible and gives a grid spacing greater than one; here ordinary examples use 0 ≤ f < n.

<div class="formula-block"><math display="block"><mrow><mi>x</mi><mo>=</mo><mfrac><mi>I</mi><msup><mn>2</mn><mi>f</mi></msup></mfrac><mo>,</mo><mspace width="0.8em"/><mi>Δ</mi><mo>=</mo><mfrac><mn>1</mn><msup><mn>2</mn><mi>f</mi></msup></mfrac></mrow></math></div>

For unsigned words the range is zero through (2<sup>n</sup> − 1)2<sup>−f</sup>. For two's complement it is −2<sup>n−1−f</sup> through 2<sup>n−1−f</sup> − 2<sup>−f</sup>. The spacing is Δ = 2<sup>−f</sup>. More fractional bits at fixed width give finer resolution but less magnitude range. Resolution is the grid spacing, not the error of every possible arithmetic computation.

Eight-bit two's complement with f = 3 represents −16 through 15.875 in steps of 0.125. The word 1110 1101 decodes first as integer −19, then as −19/8 = −2.375. Treating the top bit as an ordinary positive digit before inserting a point would give a different format and the wrong signed answer.

### Encoding, midpoint ties, and saturation

To encode a real x, multiply by 2<sup>f</sup>, choose an integer quantization rule, check the integer range, then encode that integer. Under nearest ties-to-even, x = 2.3125 with f = 3 becomes 18.5 and rounds to 18, so the stored value is 2.25. The adjacent midpoint x = 2.4375 becomes 19.5 and rounds to 20, so it stores 2.5. Both errors have magnitude 0.0625, half a grid step; tie direction differs because the retained integer parity differs.

Clipping or saturation replaces out-of-range values with an endpoint. Wrapping uses a modular word and can radically change sign. Neither policy should be silently substituted for an exact representable conversion. The Δ/2 nearest-rounding bound applies when a suitable grid point is available; clipping arbitrary inputs beyond the range can produce much larger error.

For negative x, floor quantization and truncation toward zero differ. With f = 2, x = −1.3 gives scaled value −5.2. Flooring stores −6/4 = −1.5; truncating toward zero stores −5/4 = −1.25. The phrase “discard the fractional bits” must therefore say whether it refers to magnitude truncation or an arithmetic right shift of a signed integer.

### Arithmetic with scales

Addition of equally scaled values adds the encoded integers, then checks the width. Differently scaled operands must first be aligned to a common scale, possibly using a wider word to avoid overflow. A fixed-point product of integer codes I and J with fractional counts f and g has integer product IJ and fractional count f + g. Retaining the original fractional count requires rescaling with a declared rounding policy.

For two inputs each having f fractional bits, simply multiplying their codes and interpreting the product with f bits makes the value too large by a factor 2<sup>f</sup>. Compute the wide product first, divide by 2<sup>f</sup> with the selected rounding rule, then check the target range. Conversely, division often needs scaling the numerator upward before integer division; that intermediate may overflow even when the final quotient is small.

### Accumulated quantization error

If k independently quantized inputs each have absolute error at most Δ/2 and their sum is performed exactly in a sufficiently wide accumulator, the total absolute error is at most kΔ/2 by the triangle inequality. Independence is unnecessary for this deterministic bound; statistical assumptions would only be needed for a smaller probabilistic estimate.

If x and y are perturbed by errors e and h, then (x + e)(y + h) − xy = xh + ye + eh. Thus a product-error bound depends on operand magnitude as well as resolution. It is misleading to promise the same Δ/2 error for an entire sequence of products and rescalings. Check each quantization step, intermediate width, and overflow policy separately.

## 9. Decimal codes and self-complementing encodings

### 8421 BCD versus pure binary

Binary-coded decimal encodes each decimal digit separately. Standard 8421 BCD uses the ordinary four-bit unsigned word for each digit zero through nine. Patterns 1010 through 1111 are invalid as individual BCD digits. The decimal integer 59 is BCD 0101 1001 but pure binary 0011 1011. Interpreting the BCD word as one unsigned binary integer instead yields 89. The encoding contract matters again.

An unsigned decimal quantity with d digits, including optional leading zeros, requires 4d BCD bits and has 10<sup>d</sup> legal digit combinations. A freely packed binary representation of the same combinations requires ⌈log<sub>2</sub>10<sup>d</sup>⌉ bits. BCD trades storage efficiency for direct decimal digits. Packed decimal may also reserve a sign nibble under a separate convention; ordinary unsigned BCD here has no sign nibble.

### Why BCD addition adds six

Add two valid digit codes and an optional incoming decimal carry. The exact subtotal t is between zero and nineteen. If t ≤ 9, its binary code is already a valid BCD digit and no decimal carry occurs. If t ≥ 10, the desired decimal digit is t − 10 with decimal carry one. Ordinary four-bit modular arithmetic works modulo sixteen, so adding six changes t to t + 6 = 16 + (t − 10). The low four bits become the correct digit and the carry becomes the decimal carry. This proves the correction rather than presenting it as an arbitrary recipe.

For subtotals ten through fifteen there is no initial binary carry, but the low nibble is invalid and correction creates the decimal carry. For sixteen through nineteen the initial binary addition carries and the low nibble may look valid. Therefore correction is required when the original binary carry is one **or** the low nibble exceeds nine. After correction, the decimal carry is one for either case; do not discard the original carry just because adding six to its low nibble did not generate another carry.

To add multi-digit BCD numbers, process digits right to left, including each decimal carry in the next subtotal. For 58 + 67, the units subtotal fifteen corrects to five with carry one, and the tens subtotal twelve corrects to two with carry one. The final result is 0001 0010 0101, or decimal 125.

### Excess-three and the Aiken 2421 code

Excess-three encodes a decimal digit d as the four-bit unsigned value d + 3. Its valid words run from 0011 through 1100. Complementing the four bits produces 15 − (d + 3) = (9 − d) + 3, the code for the digit's nines' complement. This is the **self-complementing** property. It is a digit property, not two's complement negation of the entire integer.

The Aiken 2421 code is a particular weighted decimal code. Its weights are two, four, two, and one from left to right. Weight duplication means that several words can have the same weighted sum; the designated codebook chooses one word per decimal digit. The following table declares the convention used throughout this chapter.

| Decimal digit | 8421 BCD | Excess-three | Aiken 2421 |
|---|---|---|---|
| 0 | 0000 | 0011 | 0000 |
| 1 | 0001 | 0100 | 0001 |
| 2 | 0010 | 0101 | 0010 |
| 3 | 0011 | 0110 | 0011 |
| 4 | 0100 | 0111 | 0100 |
| 5 | 0101 | 1000 | 1011 |
| 6 | 0110 | 1001 | 1100 |
| 7 | 0111 | 1010 | 1101 |
| 8 | 1000 | 1011 | 1110 |
| 9 | 1001 | 1100 | 1111 |

The Aiken weights sum to nine, so complementing a word changes its weighted value from d to 9 − d. The chosen table is closed under bitwise complement, making the code self-complementing. Weights summing to nine are necessary for this complement transformation in a weighted code, but the chosen codebook must also contain the complemented words. Weight sums alone do not prove that an arbitrary designated code is self-complementing.

BCD subtraction can use decimal nines' or tens' complements applied to the **digit sequence**, not binary complement of the packed word. For a d-digit decimal quantity, its tens' complement is (10<sup>d</sup> − value) mod 10<sup>d</sup>, then each resulting digit is BCD-encoded. Complementing every packed BCD bit generally produces invalid digit codes and is not the required operation.

## 10. Gray code: conversion, proof, and applications

### Reflected construction and cyclic adjacency

A Gray ordering visits every n-bit word so that consecutive words differ in exactly one bit. The standard binary reflected Gray code is built recursively: prefix zero to the previous code in its existing order, then prefix one to the previous code in reverse order. Starting with the one-bit sequence 0, 1 gives the two-bit sequence 00, 01, 11, 10 and the three-bit sequence 000, 001, 011, 010, 110, 111, 101, 100.

Induction proves three properties. Each half visits all previous words exactly once, and their different leading bits make the halves disjoint. Within a half, neighboring words still differ in one lower bit. Across the middle boundary, the lower words match because of reversal, so only the leading bit changes. The final and first words also have matching lower words and different leading bits. Therefore the reflected construction is cyclic for n ≥ 1.

<figure class="number-diagram"><svg viewBox="0 0 720 340" role="img" aria-labelledby="gray-title gray-desc"><title id="gray-title">A cyclic three-bit reflected Gray ordering</title><desc id="gray-desc">Eight nodes contain 000, 001, 011, 010, 110, 111, 101, 100 in cyclic order. Every edge changes exactly one bit, including the closing edge.</desc><path d="M180 55H360L535 105V230L360 285H180L65 230V105Z" fill="#f7fafc" stroke="#82a8bc" stroke-width="3"/><g fill="#e8f2f8" stroke="#8dabbf"><circle cx="180" cy="55" r="33"/><circle cx="360" cy="55" r="33"/><circle cx="535" cy="105" r="33"/><circle cx="535" cy="230" r="33"/><circle cx="360" cy="285" r="33"/><circle cx="180" cy="285" r="33"/><circle cx="65" cy="230" r="33"/><circle cx="65" cy="105" r="33"/></g><g text-anchor="middle" class="math-label"><text x="180" y="61">000</text><text x="360" y="61">001</text><text x="535" y="111">011</text><text x="535" y="236">010</text><text x="360" y="291">110</text><text x="180" y="291">111</text><text x="65" y="236">101</text><text x="65" y="111">100</text></g><text x="300" y="164" text-anchor="middle">Each edge changes one bit</text><text x="300" y="192" text-anchor="middle">All eight words appear once</text></svg><figcaption>Adjacency refers to this ordering, not to adding one to the raw Gray word as an unsigned number.</figcaption></figure>

### Binary-to-Gray and Gray-to-binary

For a binary index B with bits b<sub>n−1</sub> through b<sub>0</sub>, the reflected Gray word G has top bit g<sub>n−1</sub> = b<sub>n−1</sub> and lower bits g<sub>i</sub> = b<sub>i+1</sub> ⊕ b<sub>i</sub>. At word level:

<div class="formula-block">G = B ⊕ (B logically shifted right by one).</div>

Decode by cumulative XOR from the top: b<sub>n−1</sub> = g<sub>n−1</sub> and b<sub>i</sub> = b<sub>i+1</sub> ⊕ g<sub>i</sub>. Equivalently each binary bit is the XOR of all Gray bits from that position through the top. This uniquely determines B from G, proving that conversion is bijective.

The formula's adjacency can also be proved directly. When B increases by one, a suffix of ones becomes zeros and the zero immediately above becomes one. In G, neighboring binary differences within that changing suffix cancel in pairs; only the Gray bit at the top of the suffix's change survives. Thus consecutive reflected Gray words differ in exactly one position. At wraparound, the final Gray word is a top one followed by zeros and the first is all zeros, again differing once.

For binary 10110, Gray is 10110 XOR 01011 = 11101. To decode 11101, the prefix XORs are 1, 0, 1, 1, 0, recovering 10110. These operations involve bitwise XOR, not ordinary addition. Gray word 11101 has unsigned value 29, but its reflected Gray index is 22.

### What Gray code guarantees and what it does not

In a rotary encoder, natural binary transition 0111 to 1000 changes four tracks. If track transitions are read at different moments, a transient mixture may describe a distant position. Gray ordering changes only one track at an adjacent boundary, reducing that particular ambiguity. It does not remove mechanical noise, guarantee analog signal validity, or make metastability impossible. Practical synchronization and timing still matter.

All n-bit reflected Gray words are legal, so the code has minimum Hamming distance one. It is not an error-detecting redundancy code. Its virtue is one-change adjacency, which is a different design goal from separating valid words to detect arbitrary bit flips. Gray labeling is also useful in Karnaugh maps because adjacent cells differ in one Boolean variable; the geometric map arrangement and wrap adjacency are developed in the minimization chapter.

For arithmetic, decode the Gray words, perform the intended numerical operation, check the required width, and re-encode. Incrementing the raw Gray word as binary generally gives the wrong next index. Reversing or rotating a valid cyclic Gray ordering preserves adjacency but changes the index convention; the standard conversion formula presumes the declared reflected ordering.

## 11. Error detection, correction, and Hamming codes

### Distance separates valid words

The Hamming distance of equal-width binary words is the number of positions in which they differ. It equals the number of ones in their XOR. The minimum distance d<sub>min</sub> of a code is the smallest distance between distinct valid words; it is a property of the entire codebook, not one chosen pair.

Every pattern of at most e bit flips is detectable by validity checking if d<sub>min</sub> ≥ e + 1. If fewer than d<sub>min</sub> positions change, a valid word cannot become another valid word. Conversely, if two valid words differ in at most e positions, flipping those positions makes an undetectable error. This proves the condition is necessary and sufficient for guaranteed detection of all such patterns.

Correction of every pattern of at most t bit flips requires d<sub>min</sub> ≥ 2t + 1. Radius-t balls around valid words must be disjoint: otherwise one received word could plausibly come from two messages. The triangle inequality proves disjointness at the stated distance, and splitting a shortest differing-position path proves overlap when the distance is at most 2t. These are worst-case guarantees under a bit-substitution model; they do not describe burst duration or analog noise directly.

### Parity is a test, not a repair

An even-parity bit is chosen so that the XOR of all transmitted bits is zero. It detects every error pattern with an odd number of flipped bits, because each flip toggles the XOR. Any even number of flips leaves parity unchanged. With at least one data bit, the even-parity code has minimum distance two: it detects a single error but cannot identify its position. Odd parity changes the expected XOR to one; its detection capability is the same.

For data 1011010, there are four ones, so an appended even-parity bit is zero. Receiving 10100100 changes one data bit and fails parity. Receiving 00100100 changes two data bits and passes parity despite corruption. A passing parity check therefore means “no odd-weight error detected,” not “the message is certainly correct.”

### Constructing Hamming (7,4) from positional checks

Number seven transmitted bit positions from one through seven. Put parity bits at powers of two: positions one, two, and four. Put four data bits at positions three, five, six, and seven. Write each position number in three-bit binary; parity check j includes exactly those positions whose jth binary index bit is one. Use even parity throughout.

| Check | Included positions | Computed parity bit |
|---|---|---|
| Low index bit | 1, 3, 5, 7 | p<sub>1</sub> = d<sub>3</sub> ⊕ d<sub>5</sub> ⊕ d<sub>7</sub> |
| Middle index bit | 2, 3, 6, 7 | p<sub>2</sub> = d<sub>3</sub> ⊕ d<sub>6</sub> ⊕ d<sub>7</sub> |
| High index bit | 4, 5, 6, 7 | p<sub>4</sub> = d<sub>5</sub> ⊕ d<sub>6</sub> ⊕ d<sub>7</sub> |

At the receiver, recompute the XOR of all positions in each check. The three results form a syndrome, written in order high, middle, low. A flip at position j toggles exactly the checks indicated by j's binary index. Consequently, under the assumption of at most one error, a nonzero syndrome is the erroneous position and zero means no error. Correct by flipping that position.

The Hamming (7,4) code has minimum distance three. No single flipped bit has zero syndrome because every position index is nonzero. No two distinct flips have zero syndrome because the XOR of two distinct indices is nonzero. A three-position pattern at positions one, two, and three has zero syndrome because 1 ⊕ 2 ⊕ 3 = 0; it changes a valid word to another valid word. Thus the minimum is exactly three, not merely at least three.

The code can detect all two-bit errors if used strictly as a validity checker, or correct all single-bit errors under the corresponding error bound. A naive single-error corrector cannot simultaneously identify arbitrary double errors: a two-error syndrome can point to a third position, and flipping that position may miscorrect the message.

### Extended parity and the SECDED decision table

Add an overall even-parity bit to the seven-bit Hamming word. The resulting eight-bit extended code has minimum distance four and supports single-error correction plus double-error detection, abbreviated SECDED. Let S be the three-bit Hamming syndrome and P the XOR of all eight received bits. Under the explicit assumption of at most two flipped bits:

| Syndrome | Overall parity result | Interpretation and action |
|---|---|---|
| Zero | P = 0 | No error under the assumed bound. |
| Nonzero | P = 1 | One error in the original seven positions; correct position S. |
| Zero | P = 1 | One error in the added overall parity bit; correct that bit. |
| Nonzero | P = 0 | Two errors detected; do not apply a single-bit correction. |

Without the two-error bound, the table is not a universal decoder. Three errors can masquerade as one and some four errors are undetected. Extra redundancy increases a particular guaranteed capability; it does not prove perfection against unlimited corruption.

For k data bits and r Hamming parity bits that identify a single error among k + r positions, the necessary counting condition is 2<sup>r</sup> ≥ k + r + 1: the r-bit syndrome must represent all error positions plus the no-error state. Hamming constructions attain the single-error capability with appropriate columns, including shortened variants. Add one more overall parity bit for SECDED. The condition must include r on the right; counting only k + 1 misses parity-bit errors.

## 12. Interactive word laboratory

The laboratory uses an explicit width between two and sixteen bits. Enter the **unsigned decimal values of the stored operand words**, not signed decimal values; the panel displays both interpretations. Choose addition or subtraction. It shows exact unsigned and signed answers, the retained word, carry or no-borrow, signed overflow, per-bit carries, and the reflected Gray encoding of the first operand. Change one input at a time to observe which quantities depend on interpretation and which depend only on the bits.

<section class="number-lab" aria-label="Fixed-width word laboratory"><div class="number-controls"><label>Word width <input id="number-width" type="number" min="2" max="16" value="4"></label><label>First stored word, unsigned decimal <input id="number-a" type="number" min="0" value="7"></label><label>Second stored word, unsigned decimal <input id="number-b" type="number" min="0" value="1"></label><label>Operation <select id="number-operation"><option value="add">Add words</option><option value="sub">Subtract second from first</option></select></label></div><div id="number-result" aria-live="polite"></div><div class="number-table-wrap"><table><caption>Per-bit adder trace, least significant bit first</caption><thead><tr><th>Position</th><th>First bit</th><th>Second adder bit</th><th>Carry in</th><th>Result</th><th>Carry out</th></tr></thead><tbody id="number-trace"></tbody></table></div><p class="lab-note">For subtraction, the second adder word is the width-limited complement of the second operand and the initial carry is one. A final carry then means no borrow. This is an abstract word model; it does not execute C signed arithmetic.</p></section>

The initial example is four-bit +7 + +1: the unsigned answer eight fits, while the signed answer eight does not. Try first word fifteen and second word one: the unsigned answer sixteen does not fit, but signed −1 + +1 = 0 does. For subtraction, try first word seven and second word fifteen: unsigned subtraction borrows, while signed +7 − (−1) overflows. These are guided demonstrations after instruction, not a test required before you can study.

### Transparent reference algorithms

The following Python functions operate on unbounded mathematical integers and apply width explicitly. They are not subject to C integer promotions. The checked examples and the browser laboratory use the same declared decoding contracts, with separately implemented arithmetic checks.

```python
def decode_twos(word, width):
    if width < 1 or not 0 <= word < (1 << width):
        raise ValueError("Invalid word or width")
    sign = (word >> (width - 1)) & 1
    return word - sign * (1 << width)

def encode_twos(value, width):
    if width < 1 or not -(1 << (width - 1)) <= value < (1 << (width - 1)):
        raise ValueError("Value does not fit")
    return value % (1 << width)

def gray_encode(index):
    if index < 0:
        raise ValueError("Index must be nonnegative")
    return index ^ (index >> 1)

def gray_decode(word):
    if word < 0:
        raise ValueError("Word must be nonnegative")
    result = 0
    while word:
        result ^= word
        word >>= 1
    return result
```

Gray decoding XORs the word with each of its successive right shifts, producing exactly the prefix XORs derived earlier. Replacing XOR by addition would be wrong. In an implementation language with bounded signed integers, choose suitable unsigned types, mask explicitly when needed, and recheck shifts and intermediate ranges; do not transfer these Python semantics without analysis.
