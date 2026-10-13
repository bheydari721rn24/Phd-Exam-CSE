## Detailed final decisions for combined examination questions

These decisions supplement the retained end-of-chapter notes. They state what to calculate, why the rule applies, and where it fails.

### 16. An interval-capacity question has two different proofs

An arbitrary injective code needs $\lceil\log_2(H-L+1)\rceil$ bits for inclusive labels. A mandated signed representation additionally requires both endpoints to fit its weighted range. The interval 0 through 127 needs 7 arbitrary bits and 8 two's-complement bits. Counting labels does not establish that the specified numerical decoder can use every code.

### 17. Largest-fitting weight includes equality

Greedy conversion uses a weight at most the residual, including equality. At residual 8, choose 8 instead of 4. If the residual reaches zero, explicitly fill remaining lower positions with zeros. An early stop with unassigned cells is not a complete fixed-width numeral.

### 18. A reduced denominator decides exact termination

For base $b$ and reduced denominator $q$, exact termination is equivalent to $q\mid b^f$ for some nonnegative integer $f$. Factor comparisons determine the minimum length, not just existence. For $7/48$ in base 12 the minimum is 2; in base 2 termination is impossible because of denominator factor 3.

### 19. Distinguish a stored count from its real unit

With $f$ fractional positions, code $I$ represents $I2^{-f}$. Multiplying two codes adds their fractional-position counts. Returning to a smaller fractional count rounds a wide code product at the new unit. A final value that fits does not prove that a prematurely narrowed intermediate retained its information.

### 20. An even tie concerns the grid index

Nearest-even selects an even retained integer index, not an even real number or an even bit-population count. At spacing 1/4,1.625 lies between indices 6 and 7 and rounds to 1.5. A neighboring tie at 1.875 lies between 7 and 8 and rounds to 2.0. The direction can change without changing the rounding mode.

### 21. Use Euclidean remainder to round negative rescaling

Write $P=qD+r$ with floor quotient and $0\le r<D$. Compare $2r$ to $D$, then choose by parity if equal. For $P=-30,D=4$, $q=-8,r=2$ is a tie and selects $-8$. A source language's negative remainder convention must be converted or analyzed before this rule is used.

### 22. A normal exponent formula is a conditional decoder

Subtract the declared bias only after checking that the stored field is normal. Reserved fields may change the leading bit, exponent or value class. A sign field is not part of that bias. For $E=n-3$, $K=2^{n-1}-1$, careful subtraction gives $n-2-2^{n-1}$, including the positive one contributed by the bias's internal minus sign.

### 23. A binade boundary has unequal neighboring gaps

Normal precision $p$ gives local spacing $2^{e-p+1}$ at exponent $e$. With five significant bits around 32, the predecessor is 31 and the successor is 34. One label such as spacing at 32 must therefore specify the side or local binade being measured. Full exponent-range and special-field assumptions remain necessary.

### 24. Hardware carry and signed overflow are independent

Two maximum positive signed words sum to $2^w-2$, with final unsigned carry 0 but signed overflow 1. Their signed stored result is $-2$, not the exact positive sum. Conversely unsigned all-ones plus 1 carries while signed $-1+1$ is valid. State which range each flag is testing.

### 25. A signed zero must be removed from strictly negative counts

Ones' complement and sign-magnitude each have two word encodings for one numerical zero. A top-one word can therefore decode to zero in those formats. Two's complement has only one zero. Counting words, distinct integer values, positive values and negative values are four different tasks.

### 26. Widening protects operations performed afterward

Sign extension preserves the signed value of its input word. It cannot recover a mathematical result that was already reduced at an insufficient width. Eight-bit 100 plus 60 stores signed $-96$; extending that word preserves $-96$. Widening the operands before adding instead represents 160 exactly.

### 27. Byte order does not reverse bit significance inside a byte

Little-endian stores the least-significant byte at the smallest address. Big-endian stores the most-significant byte there. Matching decoders recover the same word; reading with the wrong decoder can change its value. Hexadecimal groups identify significance, while the memory convention identifies addresses.

### 28. A finite all-one fraction is below its infinite limit

Exactly $n$ fractional ones represent $1-2^{-n}$, not 1. The infinite all-one continuation adds $2^{-n}$, exactly one last-retained-position unit in this special comparison. Omitting the final bit instead loses $2^{-n}$ from the finite prefix. Specify both the repetition and terminal conditions.

### 29. BCD correction preserves a decimal carry

Correct when the original binary carry is 1 or the retained nibble exceeds 9. At subtotal 17, low nibble 1 looks legal but still requires correction to digit 7 with carry 1. Binary and decimal moduli differ; adding 6 reconciles 16 with 10. Decode each packed nibble separately.

### 30. Weighted value does not define a unique Aiken codeword

The repeated 2421 weights let more than one word have the same sum. The designated codebook selects 1011 for digit 5 even though 0101 also has weight 5. Validate membership and complement closure under the named table. Weight sum 9 alone does not establish that an arbitrary chosen codebook is self-complementing.

### 31. Gray arithmetic starts with prefix-XOR decoding

Gray 11010 decodes to binary 10011, index 19. Increment its decoded index to 20 and re-encode 11110. Raw Gray-word increment produces 11011, which decodes to 18. One-track adjacency is a property of neighboring indices in a specified cycle, not ordinary numerical addition on labels.

### 32. Minimum distance measures the entire valid codebook

The distance between one chosen pair is not automatically the minimum. Guaranteed detection of up to $e$ flips needs $d_{\min}\ge e+1$; guaranteed correction of up to $t$ flips needs $d_{\min}\ge 2t+1$. A reflected Gray code contains every word and has minimum distance 1 despite its useful adjacency property.

### 33. A syndrome requires an error-model interpretation

In Hamming(7,4), a single error at position 6 produces syndrome 110. Two errors at 1 and 2 instead produce syndrome 011 and can fool a single-error corrector into flipping 3. The resulting zero syndrome does not prove that the original message was recovered. Declare position order, check-bit order and the error bound before correcting.

### 34. SECDED uses syndrome and overall parity together

Under an at-most-two-error bound, nonzero syndrome with odd overall parity identifies a single error in the Hamming part. Nonzero syndrome with even overall parity detects a double error and prohibits single-bit correction. Zero syndrome with odd parity identifies the extra parity-bit error. Remove the bound and these observations no longer identify every error pattern uniquely.

### 35. Count parity-bit errors in the syndrome-capacity bound

For $k$ data bits and $r$ Hamming parity bits, $2^r\ge k+r+1$ counts errors in all transmitted positions plus the no-error state. For $k=9$, $r=3$ fails and $r=4$ succeeds. SECDED adds one overall parity bit beyond this count. Numerical data width and coding redundancy solve different design constraints.

### Closing synthesis

A correct representation solution begins with width, decoder, scale and the operation's domain. It then performs exact arithmetic, checks representability, applies the stated quantizer or code transformation, and decodes the result again. Flags and syndrome observations answer specified questions under specified assumptions. These steps transfer across unfamiliar combinations because each derives a mathematical contract rather than guessing a familiar-looking bit string.
