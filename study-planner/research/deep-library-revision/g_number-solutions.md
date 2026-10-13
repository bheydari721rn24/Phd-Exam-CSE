# Number bases and encoding: individual answer-revision manuscript

Status: draft pending full source, model and rendered review. These are complete written solutions, not a claim that the entire chapter revision is finished.

## Q1

**Correct option: 4.** This is a four-bit hardware representation question, not an instruction to execute overflowing signed C arithmetic.

### Decode, add mathematically, then test the range

A four-bit two's-complement pattern has weights $-8,4,2,1$. Its signed domain is $[-8,7]$. For example, $1100=-8+4=-4$ and $1011=-8+2+1=-5$. Checking all four alternatives gives:

| Option | Decoded operands | Mathematical sum | Low four bits | Signed overflow? |
|---|---|---:|---|---|
| 1 | $5,-8$ | $-3$ | `1101` | No |
| 2 | $2,5$ | $7$ | `0111` | No: the endpoint is included. |
| 3 | $4,-2$ | $2$ | `0010` | No |
| 4 | $-4,-5$ | $-9$ | `0111` | Yes: $-9<-8$. |

In the last addition, low-bit storage computes $12+11=23=16+7$. Discarding the fifth bit leaves the pattern for positive seven. That bit pattern cannot represent the correct signed answer. Both negative operands produced a nonnegative stored result, the characteristic signed-overflow condition. Equivalently, the carry into the sign bit differs from the carry out. Unsigned carry and signed overflow answer different questions: option 3 has an unsigned carry although its signed result is valid; option 2 can overflow neither interpretation.

### Derive the general test

Opposite-sign operands sum between the two inputs, so cannot leave the signed range. Two nonnegative operands can exceed the upper endpoint; two negative operands can fall below the lower endpoint. Test the exact mathematical sum against both endpoints before interpreting low bits. For a C17 expression evaluated in a signed type, an unrepresentable result has undefined behavior; two's-complement storage does not authorize predicting a wrapped C output. This distinction prevents a correct hardware calculation from becoming an incorrect language answer.

## Q2

**Correct option: 3.** The false description equates rounding with truncation. The formula itself performs rounding under the stated exact-real model.

### Start from the definition of CHOP

For an exact real $t$, truncation toward zero is
$$t\ge0\ \Rightarrow\ \operatorname{CHOP}(t)=\lfloor t\rfloor,\qquad t<0\ \Rightarrow\ \operatorname{CHOP}(t)=\lceil t\rceil.$$
Every integer therefore remains unchanged, establishing option 1. For a negative $x$, subtracting one half before truncation implements nearest-integer rounding, with ties away from zero: at $x=-2.49$ the intermediate is $-2.99$ and the result $-2$; at $x=-2.5$ the intermediate is $-3$ and the result $-3$. This is the tie convention implicit in option 2, rather than ties to even.

For nonnegative $x$, scaling by one hundred moves the hundredths digit into the integer position. At $x=1.239$ the two relevant calculations are
$$\frac{\operatorname{CHOP}(123.9)}{100}=1.23,\qquad
\frac{\operatorname{CHOP}(123.9+0.5)}{100}=1.24.$$
Adding one half decides which hundredth is nearest; it does not merely remove all digits beyond the hundredths place. Hence option 3's claim of truncation is false, while option 4 correctly describes truncation. At the halfway input $1.235$, the offset formula returns $1.24$, clarifying its upward tie rule for positive inputs. The extension to $x=0$ also works, although it is not needed to broaden the original source's domain.

### Keep the mathematical primitive separate from a C cast

CHOP is defined here for all exact real arguments. A C floating-to-integer conversion first discards the fraction but additionally requires the resulting integer to fit the destination. Binary approximation of $100x$ can move a intended decimal halfway value slightly to either side. Thus this proof neither authorizes an out-of-range C cast nor guarantees exact decimal rounding for every `double`. Identify the arithmetic and tie model before applying a memorized offset formula.

## Q3

**Correct option: 1.** The difference is $0.01$, caused by two distinct intermediate-rounding paths.

### Determine the actual precision

One digit before the normalized mantissa's decimal point plus four after it gives five significant decimal digits. Convert the inputs to ordinary notation:
$$a=341.27,\quad b=81.316,\quad c=12.417.$$
Write $R(t)$ for rounding $t$ to five significant decimal digits. The calculator evaluates $A=R(R(a+b)+c)$ and $B=R(a+R(b+c))$, not one common exact sum followed by one final round.

| Node | Exact operation on its current inputs | Rounded output |
|---|---|---|
| Left branch, first addition | $341.27+81.316=422.586$ | $422.59$ |
| Left branch, second addition | $422.59+12.417=435.007$ | $435.01$ |
| Right branch, first addition | $81.316+12.417=93.733$ | $93.733$ |
| Right branch, second addition | $341.27+93.733=435.003$ | $435.00$ |

The final subtraction is exact at the available precision:
$$A-B=435.01-435.00=0.01.$$
None of these rounding decisions is a halfway case, so differences between nearest-even and nearest-away tie handling do not change this item.

### Explain every competing result

Zero comes from importing the associativity of exact real addition into a machine that rounds after each operation. The value $0.003$ is the exact total's discarded tail, not the difference of the two rounded expression trees. The value $-0.01$ reverses the requested subtraction. Counting only four significant digits also defines a different calculator from the source's normalized mantissa.

The left branch introduces error $0.004$ at its first node and then rounds again; the right branch's first node is already exact. This makes the mechanism visible instead of merely asserting that floating arithmetic is inaccurate. Always draw or record the evaluation tree, propagate each rounded output into the next operation, and preserve the stated decimal format. Replacing this machine with binary64 would answer another question.

## Q4

**Correct option: 1.** The requested triple is the stored word `10000000`, unsigned carry zero, signed overflow one.

### Derive the two numerical interpretations separately

The operands have unsigned and signed values 127 and 1, since their top bits are zero. An eight-bit unsigned format allows $0\le U\le255$, while an eight-bit two's-complement format allows $-128\le T\le127$. The exact sum is 128. Therefore the unsigned sum fits, but the signed sum does not. Reduction modulo 256 leaves 128, so its stored word is `10000000`; signed decoding then gives $128-256=-128$. This negative stored value is a consequence of overflow, not the exact mathematical sum.

| Bit positions | Local addition | Result | Outgoing carry |
|---|---|---|---|
| 0 | $1+1+0$ | 0 | 1 |
| 1 through 6 | $1+0+1$ at each position | 0 | 1 |
| 7, the sign position | $0+0+1$ | 1 | 0 |

The carry into the sign position is one and the final carry is zero, so $V=c_7\oplus c_8=1$. Equivalently, two nonnegative inputs produced a negative decoded result.

### Exclude the alternatives and transfer the method

Option 2 invents a final carry, although 128 is below 256. Option 3 belongs to a different sum such as unsigned $255+1$. Option 4 denies the signed range violation. Compute the exact sum, derive its low bits, and evaluate each flag under its own interpretation. In this hardware model a residue always exists. That does not establish defined wrap for a C17 expression evaluated in an overflowing signed type; the evaluation type and its range are separate questions.

## Q5

**Correct option: 2.** The output integer code is 38, so the stored real value is $38/16=2.375$.

### Track scale as a unit attached to each integer

The inputs are $I=25$ and $J=24$. Four fractional bits mean that they represent $25/16=1.5625$ and $24/16=1.5$. Their exact real product is
$$xy=\frac{25\cdot24}{16^2}=\frac{600}{256}=2.34375.$$
The wide integer product is 600 with eight fractional bits. Returning to four fractional bits requires division of that integer by 16, rather than division of the already decoded real product again:
$$600=16\cdot37+8,\qquad 600/16=37.5.$$

### Make the tie decision from quotient and remainder

For nearest-even rounding, compare twice the remainder to the divisor. Here $2\cdot8=16$, an exact tie. The lower index 37 is odd and the upper index 38 is even, so choose 38. Its unsigned eight-bit encoding is `00100110`; it fits the interval from zero through 255. The output error is $2.375-2.34375=1/32$, exactly half the target spacing $1/16$.

Option 1 applies truncation instead of nearest-even. Option 3 moves beyond both nearest candidates. Option 4 reports the unrescaled product code, whose unit is $1/256$, as if it already had unit $1/16$. At least ten unsigned intermediate bits are needed for 600. If the product were wrapped to eight bits first, it would become 88 and subsequent rescaling would answer a different problem. Retain a wide exact product, declare the target scale and tie rule, round once at the required conversion, then check the target range.

## Q6

**Correct option: 1.** The format represents 3.25; it is the declared normal format, not an inferred IEEE interchange format.

### Split fields before assigning place weights

The word has sign field 0, stored exponent field `100`, and fraction field `1010`. The three-bit exponent field has unsigned value 4, so bias subtraction gives $e=4-3=1$. The exponent is neither reserved pattern `000` nor `111`; the question's normal decoding rule therefore applies.

The four explicit fraction bits have weights $2^{-1},2^{-2},2^{-3},2^{-4}$. Normalization contributes an implicit leading one:
$$m=1+1\cdot2^{-1}+0\cdot2^{-2}+1\cdot2^{-3}+0\cdot2^{-4}=\frac{13}{8}.$$
Combine all three fields:
$$x=(-1)^0m2^e=\frac{13}{8}\cdot2=\frac{13}{4}=3.25.$$

### Locate each plausible mistake

Option 2, 1.625, decodes the significand but omits exponent scaling. Option 3, 6.5, multiplies that significand by four instead of two. Option 4, 2.625, is not the result of the stated fraction weights and exponent; reconstruction of the field value excludes it. Writing `1010` as decimal ten or treating the entire eight-bit word as an unsigned integer also changes the decoder.

The formula is only justified for normal exponent fields. A reserved field requires a separately specified zero, subnormal, infinity or other convention; the labels alone do not define such a convention. The sign bit controls the final sign and is not part of the exponent's bias. First state field widths, ordering, bias, leading-bit rule and special patterns. The calculation then follows from exact rational weights, avoiding dependence on a language's host floating type.

## Q7

**Correct option: 2.** Nearest-even stores 6; the exact midpoint 5.5 is not itself representable at the stated precision.

### Construct the local grid instead of guessing a decimal rule

Three significant binary bits mean one implicit leading bit and two fraction bits. In the binade $[4,8)$, the exponent is two. The representable values are
$$1.00_2\cdot2^2=4,\quad1.01_2\cdot2^2=5,\quad1.10_2\cdot2^2=6,\quad1.11_2\cdot2^2=7.$$
The spacing is $2^{2-(3-1)}=1$. Both candidates 5 and 6 are at distance $1/2$ from 5.5, so the nearest-distance test alone cannot choose an answer.

In integer-significand units, the candidates have codes `101` and `110`, respectively 5 and 6. The low retained bit of `101` is one, while that of `110` is zero. Ties to even selects the even retained significand, so the stored result is 6. Its signed error is $+0.5$, consistent with the half-spacing bound.

Option 1 chooses the lower endpoint without applying the tie rule. Option 3 requires one more significant bit because $5.5=1.011_2\cdot2^2$. Option 4 is farther away, at distance 1.5. Ties to even does not mean always rounding upward or always choosing an even decimal integer: at another exponent the real grid values can be fractional even when their integer significand indices have defined parity. For example, with this same precision in $[1,2)$, the midpoint 1.125 rounds to 1.0 because its lower index is even. Establish the local spacing, compute both adjacent retained indices, and apply parity only in the actual grid-index units.

## Q8

**Correct option: 2.** The eight-bit word is `11101101`, preserving the mathematical value $-19$.

### Decode at the original width

The six-bit word `101101` has unsigned value $32+8+4+1=45$. Its top bit is one, so its two's-complement value is $45-64=-19$. Equivalently, direct signed weights give $-32+8+4+1=-19$. Width six is essential to both calculations.

### Derive the extension rather than copy a familiar prefix

Two new leading ones add unsigned weight $128+64=192$. The resulting unsigned value is $45+192=237$, encoded `11101101`. At width eight its signed decoder subtracts 256:
$$237-256=-19.$$
In general, adding $k$ leading ones contributes $2^{n+k}-2^n$. The widened code for a negative value becomes $(x+2^n)+(2^{n+k}-2^n)=x+2^{n+k}$, so its widened signed decoder recovers $x$.

### Check the other words under the same decoder

Option 1 zero-extends to 45, changing the signed value. Option 3 has the correct bits but incorrectly reports $-45$; unsigned magnitude is not obtained by placing a minus sign before 237 or 45. Option 4 has unsigned value 173 and signed value $173-256=-83$, so it does not preserve the original integer. Extension does not perform arithmetic negation. The rule also depends on the representation: sign-magnitude widening moves the sign to the new top position and zero-pads the magnitude, while complement formats replicate the sign. Identify the original width and decoder, establish the required mathematical value, then verify the new word at its new width.

## Q9

**Correct option: 1.** Truncation returns 2.37; the offset rounding formula returns 2.38.

### Follow each exact intermediate

The premise specifies exact real arithmetic and $x=2.376\ge0$, so CHOP equals floor on both intermediate arguments. Scaling yields $100x=237.6$. Therefore
$$T(x)=\frac{\lfloor237.6\rfloor}{100}=\frac{237}{100}=2.37,$$
$$R(x)=\frac{\lfloor237.6+0.5\rfloor}{100}=\frac{\lfloor238.1\rfloor}{100}=2.38.$$
The truncation error is $-0.006$ and the nearest-rounding error is $+0.004$. The former is strictly less than one hundredth in magnitude; the latter is below half a hundredth.

### Derive the threshold and tie convention

Write $100x=q+r$ with integer $q$ and $0\le r<1$. Truncation selects $q$. Adding one half then taking floor selects $q$ for $r<1/2$ and $q+1$ for $r\ge1/2$. Its positive tie policy is therefore upward, not nearest-even. At $x=2.365$, this formula returns 2.37 even though a nearest-even decimal grid would select 2.36.

Option 2 incorrectly rounds the truncation branch. Option 3 omits the threshold crossing in the offset branch. Option 4 interchanges the operations. For negative arguments CHOP is ceiling, so reusing the positive offset formula does not provide symmetric nearest rounding; the sign must be considered. Finally, an exact-real premise is doing real work: in software, a binary approximation of a decimal midpoint can fall to either side of the intended threshold, and an integer conversion has a range condition. This numerical derivation isolates the stated quantization rules and makes no claim that every implementation of `double` reproduces them.

## Q10

**Correct option: 3.** Only $13/32$ has a terminating binary expansion, namely $0.01101_2$.

### Prove the criterion from the representation

A finite binary fraction with $f$ positions is an integer $K$ divided by $2^f$. If a reduced rational $p/q$ equals $K/2^f$, then $p2^f=qK$. Since $p$ and $q$ are coprime, $q$ divides $2^f$. Its only possible prime factor is therefore two. Conversely, if $q=2^r$, choosing $f=r$ directly gives a finite positional expansion. This establishes necessity and sufficiency rather than just recognizing an example.

| Option | Reduced denominator | Obstruction or result |
|---|---|---|
| 1 | $20=2^2\cdot5$ | Factor 5 cannot divide a power of two. |
| 2 | $24=2^3\cdot3$ | Factor 3 cannot divide a power of two. |
| 3 | $32=2^5$ | Five fractional positions suffice. |
| 4 | $18=2\cdot3^2$ | Factor 3 prevents binary termination. |

For the selected fraction, 13 is binary `01101` at width five. Its fractional weights are $1/4+1/8+1/32=13/32$. Five positions are also necessary because the fraction is reduced and 32 does not divide any smaller power of two.

Reduce before applying the test: $15/20=3/4$ terminates despite the unreduced denominator's factor five. A finite decimal expansion need not terminate in binary, as $3/20$ shows. Nontermination does not imply irrationality; a rational remainder process has finitely many states and consequently becomes periodic. The criterion concerns an exact finite expansion, not a rounded computer approximation with a fixed number of available positions.

## Q11

**Correct option: 1.** The smallest address contains `0x78` in little-endian storage; switching to matching big-endian storage changes byte order, not the abstract word.

### Split the stated word into byte-sized place values

An eight-bit byte groups two hexadecimal digits. The unsigned word has the exact decomposition
$$W=0x12\cdot256^3+0x34\cdot256^2+0x56\cdot256+0x78.$$
In decimal its value is $18\cdot16777216+52\cdot65536+86\cdot256+120=305419896$.

| Address offset | Little-endian byte | Big-endian byte |
|---|---|---|
| 0, smallest address | `78` | `12` |
| 1 | `56` | `34` |
| 2 | `34` | `56` |
| 3 | `12` | `78` |

Each decoder assigns its own byte weights, so either matching layout reconstructs the same $W$. A little-endian decoder reading the big-endian byte sequence instead returns `0x78563412`; that is a layout/decoder mismatch, not a consequence that the value must change whenever a correct system uses another layout.

Option 2 chooses the big-endian first byte and incorrectly changes the mathematical word. Option 3 introduces bit reversal, which endianness does not request. Option 4 exchanges the two nibbles of the least-significant byte; `0x87` differs from `0x78` and is not a byte-order operation. Keep significance, address order and bit order as separate axes. The premise includes byte addressability and a 32-bit unsigned word; it is not a universal claim about every C implementation's byte width. This retained cross-topic question is explicitly taught here as a place-value and storage-contract extension, although complete language object-representation semantics belong to the later programming chapter.

## Q12

**Correct option: 1.**

### Derive the exponent decoder with its domain

Let $E$ be the unsigned value of the stored exponent field and $K$ its declared bias. Normal decoding is $e=E-K$, not $e=E$. Here
$$e=(n-3)-(2^{n-1}-1)=n-2-2^{n-1}.$$
The outer minus changes both terms of the bias; forgetting its internal minus one produces an answer too small by one. For the requested width $n=5$, $E=2$ and $K=15$, so $e=2-(15)=-13$.

For every integer $n\ge4$, $E=n-3\ge1$. Also $n-3<2^n-1$, so this exponent is neither zero nor all ones. If those patterns are reserved, the stated normal rule is applicable. This explicit domain argument matters more than testing a few sample widths. The sign of the significand is a separate field and does not modify the bias.

### Compare the alternatives by reconstructing their rules

The candidate $n-3$ leaves the bias unapplied. The candidate $n-4+2^{n-1}$ adds the bias instead of subtracting it. The candidate $n-3-2^{n-1}$ omits the positive one from opening the bias subtraction. Thus only $n-2-2^{n-1}$ decodes the declared normal field. For the boundary question the valid statement is that reserved exponent patterns require separate decoding rules. This is not permission to apply a normal formula to zeros or subnormals: those objects need their stated leading-bit and exponent conventions. Nor can one infer an infinity or NaN convention solely from a bit count. A biased normal exponent is an integer code with explicitly limited applicability; inspect the field before multiplying a significand by its decoded power of two.

## Q13

**Correct option: 4.**

### Derive the exponent decoder with its domain

Let $E$ be the unsigned value of the stored exponent field and $K$ its declared bias. Normal decoding is $e=E-K$, not $e=E$. Here
$$e=(n-3)-(2^{n-1}-1)=n-2-2^{n-1}.$$
The outer minus changes both terms of the bias; forgetting its internal minus one produces an answer too small by one. For the requested width $n=8$, $E=5$ and $K=127$, so $e=5-(127)=-122$.

For every integer $n\ge4$, $E=n-3\ge1$. Also $n-3<2^n-1$, so this exponent is neither zero nor all ones. If those patterns are reserved, the stated normal rule is applicable. This explicit domain argument matters more than testing a few sample widths. The sign of the significand is a separate field and does not modify the bias.

### Compare the alternatives by reconstructing their rules

The candidate $n-3$ leaves the bias unapplied. The candidate $n-4+2^{n-1}$ adds the bias instead of subtracting it. The candidate $n-3-2^{n-1}$ omits the positive one from opening the bias subtraction. Thus only $n-2-2^{n-1}$ decodes the declared normal field. For the boundary question the valid statement is that reserved exponent patterns require separate decoding rules. This is not permission to apply a normal formula to zeros or subnormals: those objects need their stated leading-bit and exponent conventions. Nor can one infer an infinity or NaN convention solely from a bit count. A biased normal exponent is an integer code with explicitly limited applicability; inspect the field before multiplying a significand by its decoded power of two.

## Q14

**Correct option: 3.**

### Derive the exponent decoder with its domain

Let $E$ be the unsigned value of the stored exponent field and $K$ its declared bias. Normal decoding is $e=E-K$, not $e=E$. Here
$$e=(n-3)-(2^{n-1}-1)=n-2-2^{n-1}.$$
The outer minus changes both terms of the bias; forgetting its internal minus one produces an answer too small by one. At $n=5$ the result is $2-15=-13$; at $n=8$ it is $5-127=-122$. These illustrate the identity, while the algebra below proves it throughout the domain.

For every integer $n\ge4$, $E=n-3\ge1$. Also $n-3<2^n-1$, so this exponent is neither zero nor all ones. If those patterns are reserved, the stated normal rule is applicable. This explicit domain argument matters more than testing a few sample widths. The sign of the significand is a separate field and does not modify the bias.

### Compare the alternatives by reconstructing their rules

The candidate $n-3$ leaves the bias unapplied. The candidate $n-4+2^{n-1}$ adds the bias instead of subtracting it. The candidate $n-3-2^{n-1}$ omits the positive one from opening the bias subtraction. Thus only $n-2-2^{n-1}$ decodes the declared normal field. For the boundary question the valid statement is that reserved exponent patterns require separate decoding rules. This is not permission to apply a normal formula to zeros or subnormals: those objects need their stated leading-bit and exponent conventions. Nor can one infer an infinity or NaN convention solely from a bit count. A biased normal exponent is an integer code with explicitly limited applicability; inspect the field before multiplying a significand by its decoded power of two.

## Q15

**Correct option: 2.**

### Derive the exponent decoder with its domain

Let $E$ be the unsigned value of the stored exponent field and $K$ its declared bias. Normal decoding is $e=E-K$, not $e=E$. Here
$$e=(n-3)-(2^{n-1}-1)=n-2-2^{n-1}.$$
The outer minus changes both terms of the bias; forgetting its internal minus one produces an answer too small by one. At $n=5$ the result is $2-15=-13$; at $n=8$ it is $5-127=-122$. These illustrate the identity, while the algebra below proves it throughout the domain.

For every integer $n\ge4$, $E=n-3\ge1$. Also $n-3<2^n-1$, so this exponent is neither zero nor all ones. If those patterns are reserved, the stated normal rule is applicable. This explicit domain argument matters more than testing a few sample widths. The sign of the significand is a separate field and does not modify the bias.

### Compare the alternatives by reconstructing their rules

The candidate $n-3$ leaves the bias unapplied. The candidate $n-4+2^{n-1}$ adds the bias instead of subtracting it. The candidate $n-3-2^{n-1}$ omits the positive one from opening the bias subtraction. Thus only $n-2-2^{n-1}$ decodes the declared normal field. For the boundary question the valid statement is that reserved exponent patterns require separate decoding rules. This is not permission to apply a normal formula to zeros or subnormals: those objects need their stated leading-bit and exponent conventions. Nor can one infer an infinity or NaN convention solely from a bit count. A biased normal exponent is an integer code with explicitly limited applicability; inspect the field before multiplying a significand by its decoded power of two.

## Q16

**Correct option: 4.**

### Identify the unit represented by one raw integer count

With $n$ fractional bits, raw unsigned code $I$ represents $I2^{-n}$. Substitution gives
$$x=(3\cdot2^n+1)2^{-n}=3+2^{-n}.$$
The factor is a power of two, not the count $n$ itself. The stated code requires enough total bits; $n+2$ unsigned bits suffice because $3\cdot2^n+1<2^{n+2}$ for positive $n$. No overflow or clipping is stipulated. At $n=5$ the raw integer is $97$ and the exact real value is $97/32$. The adjacent lower code represents exactly 3, and this code is one grid step above it.

For consecutive valid integer codes $I$ and $I+1$, subtract their decoded values:
$$[(I+1)-I]2^{-n}=2^{-n}.$$
The spacing is uniform over the format, including values near powers of two. Increasing the fractional count by one halves this spacing if the total-width/range choice still allows the codes.

### Audit the options and prevent a scale mismatch

The expression $3+1/n$ treats a bit count as a numerical scale divisor. The raw code $3\cdot2^n+1$ omits decoding. The value $3-2^{-n}$ moves one step below three instead of above it. In the conceptual question the valid statement is uniform fixed-point spacing. A floating format's local spacing depends on its exponent, whereas this fixed-point format uses one common unit. This is an exact decoding problem: no rounding takes place because the code already belongs to the grid. If the total width were too small, one would first have to specify rejection, saturation or wrapping; silently wrapping would produce another code and another value. Write raw units beside each intermediate before comparing a code to a represented real number.

## Q17

**Correct option: 3.**

### Identify the unit represented by one raw integer count

With $n$ fractional bits, raw unsigned code $I$ represents $I2^{-n}$. Substitution gives
$$x=(3\cdot2^n+1)2^{-n}=3+2^{-n}.$$
The factor is a power of two, not the count $n$ itself. The stated code requires enough total bits; $n+2$ unsigned bits suffice because $3\cdot2^n+1<2^{n+2}$ for positive $n$. No overflow or clipping is stipulated. At $n=8$ the raw integer is $769$ and the exact real value is $769/256$. The adjacent lower code represents exactly 3, and this code is one grid step above it.

For consecutive valid integer codes $I$ and $I+1$, subtract their decoded values:
$$[(I+1)-I]2^{-n}=2^{-n}.$$
The spacing is uniform over the format, including values near powers of two. Increasing the fractional count by one halves this spacing if the total-width/range choice still allows the codes.

### Audit the options and prevent a scale mismatch

The expression $3+1/n$ treats a bit count as a numerical scale divisor. The raw code $3\cdot2^n+1$ omits decoding. The value $3-2^{-n}$ moves one step below three instead of above it. In the conceptual question the valid statement is uniform fixed-point spacing. A floating format's local spacing depends on its exponent, whereas this fixed-point format uses one common unit. This is an exact decoding problem: no rounding takes place because the code already belongs to the grid. If the total width were too small, one would first have to specify rejection, saturation or wrapping; silently wrapping would produce another code and another value. Write raw units beside each intermediate before comparing a code to a represented real number.

## Q18

**Correct option: 2.**

### Identify the unit represented by one raw integer count

With $n$ fractional bits, raw unsigned code $I$ represents $I2^{-n}$. Substitution gives
$$x=(3\cdot2^n+1)2^{-n}=3+2^{-n}.$$
The factor is a power of two, not the count $n$ itself. The stated code requires enough total bits; $n+2$ unsigned bits suffice because $3\cdot2^n+1<2^{n+2}$ for positive $n$. No overflow or clipping is stipulated. For five fractional bits the value is $97/32=3.03125$; for eight it is $769/256=3.00390625$. The decreasing increment is caused by a smaller grid step, not a change in the high integer part.

For consecutive valid integer codes $I$ and $I+1$, subtract their decoded values:
$$[(I+1)-I]2^{-n}=2^{-n}.$$
The spacing is uniform over the format, including values near powers of two. Increasing the fractional count by one halves this spacing if the total-width/range choice still allows the codes.

### Audit the options and prevent a scale mismatch

The expression $3+1/n$ treats a bit count as a numerical scale divisor. The raw code $3\cdot2^n+1$ omits decoding. The value $3-2^{-n}$ moves one step below three instead of above it. In the conceptual question the valid statement is uniform fixed-point spacing. A floating format's local spacing depends on its exponent, whereas this fixed-point format uses one common unit. This is an exact decoding problem: no rounding takes place because the code already belongs to the grid. If the total width were too small, one would first have to specify rejection, saturation or wrapping; silently wrapping would produce another code and another value. Write raw units beside each intermediate before comparing a code to a represented real number.

## Q19

**Correct option: 1.**

### Identify the unit represented by one raw integer count

With $n$ fractional bits, raw unsigned code $I$ represents $I2^{-n}$. Substitution gives
$$x=(3\cdot2^n+1)2^{-n}=3+2^{-n}.$$
The factor is a power of two, not the count $n$ itself. The stated code requires enough total bits; $n+2$ unsigned bits suffice because $3\cdot2^n+1<2^{n+2}$ for positive $n$. No overflow or clipping is stipulated. For five fractional bits the value is $97/32=3.03125$; for eight it is $769/256=3.00390625$. The decreasing increment is caused by a smaller grid step, not a change in the high integer part.

For consecutive valid integer codes $I$ and $I+1$, subtract their decoded values:
$$[(I+1)-I]2^{-n}=2^{-n}.$$
The spacing is uniform over the format, including values near powers of two. Increasing the fractional count by one halves this spacing if the total-width/range choice still allows the codes.

### Audit the options and prevent a scale mismatch

The expression $3+1/n$ treats a bit count as a numerical scale divisor. The raw code $3\cdot2^n+1$ omits decoding. The value $3-2^{-n}$ moves one step below three instead of above it. In the conceptual question the valid statement is uniform fixed-point spacing. A floating format's local spacing depends on its exponent, whereas this fixed-point format uses one common unit. This is an exact decoding problem: no rounding takes place because the code already belongs to the grid. If the total width were too small, one would first have to specify rejection, saturation or wrapping; silently wrapping would produce another code and another value. Write raw units beside each intermediate before comparing a code to a represented real number.

## Q20

**Correct option: 3.**

### Establish which branch of the decoder applies

For an $n$-bit two's-complement word, signed decoding is $T=U-s2^n$, where $s$ is the top bit. We must prove $s=1$ rather than subtract a modulus from every word. For $n\ge3$,
$$2^n-3\ge2^{n-1}\quad\Longleftrightarrow\quad2^{n-1}\ge3,$$
which holds. Thus the word lies in the upper unsigned half and
$$T=(2^n-3)-2^n=-3.$$
At width $5$, the word has unsigned value $29$ and bits `11101`. Its signed decoder gives $29-32=-3$.

A second check complements the bits and adds one at the same width. Their unsigned magnitude is three, the positive opposite of the decoded value. Because $-3$ lies within the signed range for every width in the domain, this is exact negation, unlike the minimum-value exception.

### Explain the competing interpretations

The candidate $2^n-3$ is the unsigned interpretation, not the requested signed value. The candidate $+3$ forgets the negative sign after computing the magnitude. The candidate $-2^{n-1}$ is the signed value of `100...0`, not of the actual word with additional lower ones. The correct boundary statement is that signedness changes the decoder rather than the stored bits. One may hold one physical word and calculate both values without writing new bits. Conversely, converting a numerical value between representations can require new bits; conversion and reinterpretation are different operations. State width first: even an unchanged short bit string can acquire a different value if its width or top-bit convention is changed.

## Q21

**Correct option: 2.**

### Establish which branch of the decoder applies

For an $n$-bit two's-complement word, signed decoding is $T=U-s2^n$, where $s$ is the top bit. We must prove $s=1$ rather than subtract a modulus from every word. For $n\ge3$,
$$2^n-3\ge2^{n-1}\quad\Longleftrightarrow\quad2^{n-1}\ge3,$$
which holds. Thus the word lies in the upper unsigned half and
$$T=(2^n-3)-2^n=-3.$$
At width $8$, the word has unsigned value $253$ and bits `11111101`. Its signed decoder gives $253-256=-3$.

A second check complements the bits and adds one at the same width. Their unsigned magnitude is three, the positive opposite of the decoded value. Because $-3$ lies within the signed range for every width in the domain, this is exact negation, unlike the minimum-value exception.

### Explain the competing interpretations

The candidate $2^n-3$ is the unsigned interpretation, not the requested signed value. The candidate $+3$ forgets the negative sign after computing the magnitude. The candidate $-2^{n-1}$ is the signed value of `100...0`, not of the actual word with additional lower ones. The correct boundary statement is that signedness changes the decoder rather than the stored bits. One may hold one physical word and calculate both values without writing new bits. Conversely, converting a numerical value between representations can require new bits; conversion and reinterpretation are different operations. State width first: even an unchanged short bit string can acquire a different value if its width or top-bit convention is changed.

## Q22

**Correct option: 1.**

### Establish which branch of the decoder applies

For an $n$-bit two's-complement word, signed decoding is $T=U-s2^n$, where $s$ is the top bit. We must prove $s=1$ rather than subtract a modulus from every word. For $n\ge3$,
$$2^n-3\ge2^{n-1}\quad\Longleftrightarrow\quad2^{n-1}\ge3,$$
which holds. Thus the word lies in the upper unsigned half and
$$T=(2^n-3)-2^n=-3.$$
For example, `11101` at width five is unsigned 29 and signed $29-32=-3$; `11111101` at width eight is unsigned 253 and signed $253-256=-3$.

A second check complements the bits and adds one at the same width. Their unsigned magnitude is three, the positive opposite of the decoded value. Because $-3$ lies within the signed range for every width in the domain, this is exact negation, unlike the minimum-value exception.

### Explain the competing interpretations

The candidate $2^n-3$ is the unsigned interpretation, not the requested signed value. The candidate $+3$ forgets the negative sign after computing the magnitude. The candidate $-2^{n-1}$ is the signed value of `100...0`, not of the actual word with additional lower ones. The correct boundary statement is that signedness changes the decoder rather than the stored bits. One may hold one physical word and calculate both values without writing new bits. Conversely, converting a numerical value between representations can require new bits; conversion and reinterpretation are different operations. State width first: even an unchanged short bit string can acquire a different value if its width or top-bit convention is changed.

## Q23

**Correct option: 4.**

### Establish which branch of the decoder applies

For an $n$-bit two's-complement word, signed decoding is $T=U-s2^n$, where $s$ is the top bit. We must prove $s=1$ rather than subtract a modulus from every word. For $n\ge3$,
$$2^n-3\ge2^{n-1}\quad\Longleftrightarrow\quad2^{n-1}\ge3,$$
which holds. Thus the word lies in the upper unsigned half and
$$T=(2^n-3)-2^n=-3.$$
For example, `11101` at width five is unsigned 29 and signed $29-32=-3$; `11111101` at width eight is unsigned 253 and signed $253-256=-3$.

A second check complements the bits and adds one at the same width. Their unsigned magnitude is three, the positive opposite of the decoded value. Because $-3$ lies within the signed range for every width in the domain, this is exact negation, unlike the minimum-value exception.

### Explain the competing interpretations

The candidate $2^n-3$ is the unsigned interpretation, not the requested signed value. The candidate $+3$ forgets the negative sign after computing the magnitude. The candidate $-2^{n-1}$ is the signed value of `100...0`, not of the actual word with additional lower ones. The correct boundary statement is that signedness changes the decoder rather than the stored bits. One may hold one physical word and calculate both values without writing new bits. Conversely, converting a numerical value between representations can require new bits; conversion and reinterpretation are different operations. State width first: even an unchanged short bit string can acquire a different value if its width or top-bit convention is changed.

## Q24

**Correct option: 2.**

### Separate the exact signed total from the hardware output

The maximum nonnegative signed value is $M=2^{n-1}-1$. Both operands have top bit zero, yet their mathematical sum is
$$2M=2^n-2.$$
For $n\ge2$, this exceeds the signed upper bound $2^{n-1}-1$, so signed overflow occurs. It is nevertheless below the unsigned modulus $2^n$, giving final unsigned carry zero. The stored word has value $U=2^n-2$ without requiring another subtraction during low-bit reduction. Its top bit is one, so
$$T=U-2^n=-2.$$
At $n=5$ each operand is $15$. The exact positive sum is $30$ and its output word is `11110`. Signed decoding gives $30-32=-2$.

This is a particularly useful example of overflow without carry. In the bit trace, adding the low one-bits establishes a carry into the sign position. At that sign position $0+0+1$ stores one and produces no outgoing carry; their XOR is one.

### Reject answers that measure another layer

The expression $2^n-2$ is the exact mathematical sum and the unsigned interpretation of the output, but not its signed decoded value. The expression $2^{n-1}-1$ is one operand rather than the sum. Zero would require residue zero, whereas the actual sum is two counts below the modulus. The correct scope statement is that hardware wrap does not establish language signed-overflow behavior. In particular an overflowing C17 signed expression is undefined; no subsequent cast or claim of two's-complement storage repairs that expression. A language with expressly modular arithmetic would have another contract. Identify the question's layer—exact integer, retained word, decoded output or language evaluation—before choosing a formula.

## Q25

**Correct option: 1.**

### Separate the exact signed total from the hardware output

The maximum nonnegative signed value is $M=2^{n-1}-1$. Both operands have top bit zero, yet their mathematical sum is
$$2M=2^n-2.$$
For $n\ge2$, this exceeds the signed upper bound $2^{n-1}-1$, so signed overflow occurs. It is nevertheless below the unsigned modulus $2^n$, giving final unsigned carry zero. The stored word has value $U=2^n-2$ without requiring another subtraction during low-bit reduction. Its top bit is one, so
$$T=U-2^n=-2.$$
At $n=8$ each operand is $127$. The exact positive sum is $254$ and its output word is `11111110`. Signed decoding gives $254-256=-2$.

This is a particularly useful example of overflow without carry. In the bit trace, adding the low one-bits establishes a carry into the sign position. At that sign position $0+0+1$ stores one and produces no outgoing carry; their XOR is one.

### Reject answers that measure another layer

The expression $2^n-2$ is the exact mathematical sum and the unsigned interpretation of the output, but not its signed decoded value. The expression $2^{n-1}-1$ is one operand rather than the sum. Zero would require residue zero, whereas the actual sum is two counts below the modulus. The correct scope statement is that hardware wrap does not establish language signed-overflow behavior. In particular an overflowing C17 signed expression is undefined; no subsequent cast or claim of two's-complement storage repairs that expression. A language with expressly modular arithmetic would have another contract. Identify the question's layer—exact integer, retained word, decoded output or language evaluation—before choosing a formula.

## Q26

**Correct option: 4.**

### Separate the exact signed total from the hardware output

The maximum nonnegative signed value is $M=2^{n-1}-1$. Both operands have top bit zero, yet their mathematical sum is
$$2M=2^n-2.$$
For $n\ge2$, this exceeds the signed upper bound $2^{n-1}-1$, so signed overflow occurs. It is nevertheless below the unsigned modulus $2^n$, giving final unsigned carry zero. The stored word has value $U=2^n-2$ without requiring another subtraction during low-bit reduction. Its top bit is one, so
$$T=U-2^n=-2.$$
For five bits, $15+15=30$ stores `11110`, decoded as $-2$. For eight bits, $127+127=254$ stores `11111110`, also decoded as $-2$.

This is a particularly useful example of overflow without carry. In the bit trace, adding the low one-bits establishes a carry into the sign position. At that sign position $0+0+1$ stores one and produces no outgoing carry; their XOR is one.

### Reject answers that measure another layer

The expression $2^n-2$ is the exact mathematical sum and the unsigned interpretation of the output, but not its signed decoded value. The expression $2^{n-1}-1$ is one operand rather than the sum. Zero would require residue zero, whereas the actual sum is two counts below the modulus. The correct scope statement is that hardware wrap does not establish language signed-overflow behavior. In particular an overflowing C17 signed expression is undefined; no subsequent cast or claim of two's-complement storage repairs that expression. A language with expressly modular arithmetic would have another contract. Identify the question's layer—exact integer, retained word, decoded output or language evaluation—before choosing a formula.

## Q27

**Correct option: 3.**

### Separate the exact signed total from the hardware output

The maximum nonnegative signed value is $M=2^{n-1}-1$. Both operands have top bit zero, yet their mathematical sum is
$$2M=2^n-2.$$
For $n\ge2$, this exceeds the signed upper bound $2^{n-1}-1$, so signed overflow occurs. It is nevertheless below the unsigned modulus $2^n$, giving final unsigned carry zero. The stored word has value $U=2^n-2$ without requiring another subtraction during low-bit reduction. Its top bit is one, so
$$T=U-2^n=-2.$$
For five bits, $15+15=30$ stores `11110`, decoded as $-2$. For eight bits, $127+127=254$ stores `11111110`, also decoded as $-2$.

This is a particularly useful example of overflow without carry. In the bit trace, adding the low one-bits establishes a carry into the sign position. At that sign position $0+0+1$ stores one and produces no outgoing carry; their XOR is one.

### Reject answers that measure another layer

The expression $2^n-2$ is the exact mathematical sum and the unsigned interpretation of the output, but not its signed decoded value. The expression $2^{n-1}-1$ is one operand rather than the sum. Zero would require residue zero, whereas the actual sum is two counts below the modulus. The correct scope statement is that hardware wrap does not establish language signed-overflow behavior. In particular an overflowing C17 signed expression is undefined; no subsequent cast or claim of two's-complement storage repairs that expression. A language with expressly modular arithmetic would have another contract. Identify the question's layer—exact integer, retained word, decoded output or language evaluation—before choosing a formula.

## Q28

**Correct option: 1.**

### Solve both branches of the ones'-complement decoder

Let $U$ be the unsigned value and $s$ its top bit. The decoder is $T=U-s(2^n-1)$. In the top-zero half, $T=0$ forces $U=0$, the all-zero word. In the top-one half, $T=0$ forces $U=2^n-1$, the all-one word. These are the only solutions, because each branch's decoder is injective on its own unsigned half. For every positive width they are distinct patterns, giving exactly two encodings.

At width $5$ the two words are `00000` and `11111`. Their unsigned values are 0 and $31$, but their ones-complement numerical values are both zero.

Neither sign convention changes the integer identity $-0=0$. The labels positive zero and negative zero record different words, not two different mathematical integers. An $n$-bit ones'-complement format consequently has $2^n$ words but only $2^n-1$ distinct numerical values. For $n=1$ both available words encode zero, and the same count of two words still holds.

### Diagnose each alternative and comparison format

The candidate one confuses numerical zero with its number of representations or imports two's complement. The candidate $n$ counts bit positions without solving the decoder. The candidate $2^n$ counts all words, most of which are nonzero for wider formats. The correct conceptual statement distinguishes counting encodings from counting values. Sign-magnitude also has two zeros, but its second zero is a top one followed by zeros; two's complement has only the all-zero zero. Thus shared counts do not imply identical codewords or arithmetic rules. Counting strictly negative values must exclude the all-one ones'-complement word even though its top bit is one. Use the actual decoder and its zero set instead of a visual sign-bit shortcut.

## Q29

**Correct option: 4.**

### Solve both branches of the ones'-complement decoder

Let $U$ be the unsigned value and $s$ its top bit. The decoder is $T=U-s(2^n-1)$. In the top-zero half, $T=0$ forces $U=0$, the all-zero word. In the top-one half, $T=0$ forces $U=2^n-1$, the all-one word. These are the only solutions, because each branch's decoder is injective on its own unsigned half. For every positive width they are distinct patterns, giving exactly two encodings.

At width $8$ the two words are `00000000` and `11111111`. Their unsigned values are 0 and $255$, but their ones-complement numerical values are both zero.

Neither sign convention changes the integer identity $-0=0$. The labels positive zero and negative zero record different words, not two different mathematical integers. An $n$-bit ones'-complement format consequently has $2^n$ words but only $2^n-1$ distinct numerical values. For $n=1$ both available words encode zero, and the same count of two words still holds.

### Diagnose each alternative and comparison format

The candidate one confuses numerical zero with its number of representations or imports two's complement. The candidate $n$ counts bit positions without solving the decoder. The candidate $2^n$ counts all words, most of which are nonzero for wider formats. The correct conceptual statement distinguishes counting encodings from counting values. Sign-magnitude also has two zeros, but its second zero is a top one followed by zeros; two's complement has only the all-zero zero. Thus shared counts do not imply identical codewords or arithmetic rules. Counting strictly negative values must exclude the all-one ones'-complement word even though its top bit is one. Use the actual decoder and its zero set instead of a visual sign-bit shortcut.

## Q30

**Correct option: 3.**

### Solve both branches of the ones'-complement decoder

Let $U$ be the unsigned value and $s$ its top bit. The decoder is $T=U-s(2^n-1)$. In the top-zero half, $T=0$ forces $U=0$, the all-zero word. In the top-one half, $T=0$ forces $U=2^n-1$, the all-one word. These are the only solutions, because each branch's decoder is injective on its own unsigned half. For every positive width they are distinct patterns, giving exactly two encodings.

At five bits, `00000` and `11111` both denote zero; at eight bits the corresponding words are `00000000` and `11111111`.

Neither sign convention changes the integer identity $-0=0$. The labels positive zero and negative zero record different words, not two different mathematical integers. An $n$-bit ones'-complement format consequently has $2^n$ words but only $2^n-1$ distinct numerical values. For $n=1$ both available words encode zero, and the same count of two words still holds.

### Diagnose each alternative and comparison format

The candidate one confuses numerical zero with its number of representations or imports two's complement. The candidate $n$ counts bit positions without solving the decoder. The candidate $2^n$ counts all words, most of which are nonzero for wider formats. The correct conceptual statement distinguishes counting encodings from counting values. Sign-magnitude also has two zeros, but its second zero is a top one followed by zeros; two's complement has only the all-zero zero. Thus shared counts do not imply identical codewords or arithmetic rules. Counting strictly negative values must exclude the all-one ones'-complement word even though its top bit is one. Use the actual decoder and its zero set instead of a visual sign-bit shortcut.

## Q31

**Correct option: 2.**

### Solve both branches of the ones'-complement decoder

Let $U$ be the unsigned value and $s$ its top bit. The decoder is $T=U-s(2^n-1)$. In the top-zero half, $T=0$ forces $U=0$, the all-zero word. In the top-one half, $T=0$ forces $U=2^n-1$, the all-one word. These are the only solutions, because each branch's decoder is injective on its own unsigned half. For every positive width they are distinct patterns, giving exactly two encodings.

At five bits, `00000` and `11111` both denote zero; at eight bits the corresponding words are `00000000` and `11111111`.

Neither sign convention changes the integer identity $-0=0$. The labels positive zero and negative zero record different words, not two different mathematical integers. An $n$-bit ones'-complement format consequently has $2^n$ words but only $2^n-1$ distinct numerical values. For $n=1$ both available words encode zero, and the same count of two words still holds.

### Diagnose each alternative and comparison format

The candidate one confuses numerical zero with its number of representations or imports two's complement. The candidate $n$ counts bit positions without solving the decoder. The candidate $2^n$ counts all words, most of which are nonzero for wider formats. The correct conceptual statement distinguishes counting encodings from counting values. Sign-magnitude also has two zeros, but its second zero is a top one followed by zeros; two's complement has only the all-zero zero. Thus shared counts do not imply identical codewords or arithmetic rules. Counting strictly negative values must exclude the all-one ones'-complement word even though its top bit is one. Use the actual decoder and its zero set instead of a visual sign-bit shortcut.

## Q32

**Correct option: 1.**

### Derive the finite geometric sum with a stated endpoint

The word is a finite positional fraction, so its value is
$$x_n=\sum_{j=1}^{n}2^{-j}.$$
Multiplying by two shifts the terms: $2x_n=1+\sum_{j=1}^{n-1}2^{-j}$. Subtracting $x_n$ cancels the shared terms and leaves
$$x_n=1-2^{-n}=\frac{2^n-1}{2^n}.$$
The final position is included. The term that survives with a minus sign is precisely that least-position weight. For exactly $5$ positions the integer numerator is $31$ and the denominator $32$, so the value is $31/32$. The missing tail has exact value $1/32$.

An infinite all-one tail has value one because $2^{-n}$ tends to zero as $n$ tends to infinity. But for every finite $n$, $2^{-n}>0$, so the finite fraction is not equal to one. The infinite continuation adds
$$\sum_{j=n+1}^{\infty}2^{-j}=2^{-n},$$
one unit of the last retained position.

### Interpret the distractors as endpoint mistakes

The candidate one replaces a finite sum with its infinite limit. The candidate $2^{-n}$ gives the omitted tail rather than the retained prefix. The candidate $1-2^{1-n}$ is the value of only $n-1$ ones and drops the final specified bit. The conceptual statement about a least-position difference is valid specifically for the compared finite all-one prefix and its infinite all-one continuation; arbitrary infinite extensions need not differ by exactly one such unit. Each position has a different power-of-two weight. Count positions and preserve the terminal condition before using a geometric identity: a visually repeated string is not evidence of an infinite repetition contract.

## Q33

**Correct option: 4.**

### Derive the finite geometric sum with a stated endpoint

The word is a finite positional fraction, so its value is
$$x_n=\sum_{j=1}^{n}2^{-j}.$$
Multiplying by two shifts the terms: $2x_n=1+\sum_{j=1}^{n-1}2^{-j}$. Subtracting $x_n$ cancels the shared terms and leaves
$$x_n=1-2^{-n}=\frac{2^n-1}{2^n}.$$
The final position is included. The term that survives with a minus sign is precisely that least-position weight. For exactly $8$ positions the integer numerator is $255$ and the denominator $256$, so the value is $255/256$. The missing tail has exact value $1/256$.

An infinite all-one tail has value one because $2^{-n}$ tends to zero as $n$ tends to infinity. But for every finite $n$, $2^{-n}>0$, so the finite fraction is not equal to one. The infinite continuation adds
$$\sum_{j=n+1}^{\infty}2^{-j}=2^{-n},$$
one unit of the last retained position.

### Interpret the distractors as endpoint mistakes

The candidate one replaces a finite sum with its infinite limit. The candidate $2^{-n}$ gives the omitted tail rather than the retained prefix. The candidate $1-2^{1-n}$ is the value of only $n-1$ ones and drops the final specified bit. The conceptual statement about a least-position difference is valid specifically for the compared finite all-one prefix and its infinite all-one continuation; arbitrary infinite extensions need not differ by exactly one such unit. Each position has a different power-of-two weight. Count positions and preserve the terminal condition before using a geometric identity: a visually repeated string is not evidence of an infinite repetition contract.

## Q34

**Correct option: 3.**

### Derive the finite geometric sum with a stated endpoint

The word is a finite positional fraction, so its value is
$$x_n=\sum_{j=1}^{n}2^{-j}.$$
Multiplying by two shifts the terms: $2x_n=1+\sum_{j=1}^{n-1}2^{-j}$. Subtracting $x_n$ cancels the shared terms and leaves
$$x_n=1-2^{-n}=\frac{2^n-1}{2^n}.$$
The final position is included. The term that survives with a minus sign is precisely that least-position weight. Five ones give $31/32$; eight give $255/256$. Both are below one, with differences $1/32$ and $1/256$, respectively.

An infinite all-one tail has value one because $2^{-n}$ tends to zero as $n$ tends to infinity. But for every finite $n$, $2^{-n}>0$, so the finite fraction is not equal to one. The infinite continuation adds
$$\sum_{j=n+1}^{\infty}2^{-j}=2^{-n},$$
one unit of the last retained position.

### Interpret the distractors as endpoint mistakes

The candidate one replaces a finite sum with its infinite limit. The candidate $2^{-n}$ gives the omitted tail rather than the retained prefix. The candidate $1-2^{1-n}$ is the value of only $n-1$ ones and drops the final specified bit. The conceptual statement about a least-position difference is valid specifically for the compared finite all-one prefix and its infinite all-one continuation; arbitrary infinite extensions need not differ by exactly one such unit. Each position has a different power-of-two weight. Count positions and preserve the terminal condition before using a geometric identity: a visually repeated string is not evidence of an infinite repetition contract.

## Q35

**Correct option: 2.**

### Derive the finite geometric sum with a stated endpoint

The word is a finite positional fraction, so its value is
$$x_n=\sum_{j=1}^{n}2^{-j}.$$
Multiplying by two shifts the terms: $2x_n=1+\sum_{j=1}^{n-1}2^{-j}$. Subtracting $x_n$ cancels the shared terms and leaves
$$x_n=1-2^{-n}=\frac{2^n-1}{2^n}.$$
The final position is included. The term that survives with a minus sign is precisely that least-position weight. Five ones give $31/32$; eight give $255/256$. Both are below one, with differences $1/32$ and $1/256$, respectively.

An infinite all-one tail has value one because $2^{-n}$ tends to zero as $n$ tends to infinity. But for every finite $n$, $2^{-n}>0$, so the finite fraction is not equal to one. The infinite continuation adds
$$\sum_{j=n+1}^{\infty}2^{-j}=2^{-n},$$
one unit of the last retained position.

### Interpret the distractors as endpoint mistakes

The candidate one replaces a finite sum with its infinite limit. The candidate $2^{-n}$ gives the omitted tail rather than the retained prefix. The candidate $1-2^{1-n}$ is the value of only $n-1$ ones and drops the final specified bit. The conceptual statement about a least-position difference is valid specifically for the compared finite all-one prefix and its infinite all-one continuation; arbitrary infinite extensions need not differ by exactly one such unit. Each position has a different power-of-two weight. Count positions and preserve the terminal condition before using a geometric identity: a visually repeated string is not evidence of an infinite repetition contract.

## Q36

**Correct option: 1.**

### Count explicit fraction positions, not total significant bits twice

Five significant bits include the leading one. Thus four bits remain after the binary point. Inside the stated normal binade, each significand has the form $1+j/16$ with $j=0,1,\ldots,15$. With exponent $n$,
$$x_j=(1+j/16)2^n=2^n+j2^{n-4}.$$
Subtract adjacent grid values to derive
$$x_{j+1}-x_j=2^{n-4}.$$
The derivation applies when both compared values use this normal precision and the exponent range covers the binade. At $n=5$ the first value is $32$ and the next is $34$, a difference of $2$. The last value inside this binade is $62$.

The gap from the last value below $2^{n+1}$ to that boundary is also $2^{n-4}$. Immediately above the boundary the local gap doubles to $2^{n-3}$. This distinction avoids saying that an ambiguous boundary point has one symmetric spacing on both sides. At the lower boundary, its predecessor in the previous binade lies only $2^{n-5}$ below it.

### Explain the incorrect scaling choices

The candidate $2^{-n}$ confuses the magnitude exponent with a fractional-place count. The candidate $2^n$ reports the binade's starting value, omitting fraction precision. The candidate $2^{n-5}$ counts five explicit fraction bits even though the leading bit is already included. In the boundary question, spacing changes at a binade transition; exponent range determines whether values exist, while significant-bit count determines their precision. Subnormal formats can have another leading-bit and exponent rule, and overflow at the highest exponent removes an otherwise expected neighbor. The question expressly grants adequate exponent range and normal values, so those exceptions do not invalidate the stated local-grid result.

## Q37

**Correct option: 4.**

### Count explicit fraction positions, not total significant bits twice

Five significant bits include the leading one. Thus four bits remain after the binary point. Inside the stated normal binade, each significand has the form $1+j/16$ with $j=0,1,\ldots,15$. With exponent $n$,
$$x_j=(1+j/16)2^n=2^n+j2^{n-4}.$$
Subtract adjacent grid values to derive
$$x_{j+1}-x_j=2^{n-4}.$$
The derivation applies when both compared values use this normal precision and the exponent range covers the binade. At $n=8$ the first value is $256$ and the next is $272$, a difference of $16$. The last value inside this binade is $496$.

The gap from the last value below $2^{n+1}$ to that boundary is also $2^{n-4}$. Immediately above the boundary the local gap doubles to $2^{n-3}$. This distinction avoids saying that an ambiguous boundary point has one symmetric spacing on both sides. At the lower boundary, its predecessor in the previous binade lies only $2^{n-5}$ below it.

### Explain the incorrect scaling choices

The candidate $2^{-n}$ confuses the magnitude exponent with a fractional-place count. The candidate $2^n$ reports the binade's starting value, omitting fraction precision. The candidate $2^{n-5}$ counts five explicit fraction bits even though the leading bit is already included. In the boundary question, spacing changes at a binade transition; exponent range determines whether values exist, while significant-bit count determines their precision. Subnormal formats can have another leading-bit and exponent rule, and overflow at the highest exponent removes an otherwise expected neighbor. The question expressly grants adequate exponent range and normal values, so those exceptions do not invalidate the stated local-grid result.

## Q38

**Correct option: 3.**

### Count explicit fraction positions, not total significant bits twice

Five significant bits include the leading one. Thus four bits remain after the binary point. Inside the stated normal binade, each significand has the form $1+j/16$ with $j=0,1,\ldots,15$. With exponent $n$,
$$x_j=(1+j/16)2^n=2^n+j2^{n-4}.$$
Subtract adjacent grid values to derive
$$x_{j+1}-x_j=2^{n-4}.$$
The derivation applies when both compared values use this normal precision and the exponent range covers the binade. At exponent five the adjacent values are 32 and 34, giving spacing two. At exponent eight they are 256 and 272, giving spacing sixteen.

The gap from the last value below $2^{n+1}$ to that boundary is also $2^{n-4}$. Immediately above the boundary the local gap doubles to $2^{n-3}$. This distinction avoids saying that an ambiguous boundary point has one symmetric spacing on both sides. At the lower boundary, its predecessor in the previous binade lies only $2^{n-5}$ below it.

### Explain the incorrect scaling choices

The candidate $2^{-n}$ confuses the magnitude exponent with a fractional-place count. The candidate $2^n$ reports the binade's starting value, omitting fraction precision. The candidate $2^{n-5}$ counts five explicit fraction bits even though the leading bit is already included. In the boundary question, spacing changes at a binade transition; exponent range determines whether values exist, while significant-bit count determines their precision. Subnormal formats can have another leading-bit and exponent rule, and overflow at the highest exponent removes an otherwise expected neighbor. The question expressly grants adequate exponent range and normal values, so those exceptions do not invalidate the stated local-grid result.

## Q39

**Correct option: 2.**

### Count explicit fraction positions, not total significant bits twice

Five significant bits include the leading one. Thus four bits remain after the binary point. Inside the stated normal binade, each significand has the form $1+j/16$ with $j=0,1,\ldots,15$. With exponent $n$,
$$x_j=(1+j/16)2^n=2^n+j2^{n-4}.$$
Subtract adjacent grid values to derive
$$x_{j+1}-x_j=2^{n-4}.$$
The derivation applies when both compared values use this normal precision and the exponent range covers the binade. At exponent five the adjacent values are 32 and 34, giving spacing two. At exponent eight they are 256 and 272, giving spacing sixteen.

The gap from the last value below $2^{n+1}$ to that boundary is also $2^{n-4}$. Immediately above the boundary the local gap doubles to $2^{n-3}$. This distinction avoids saying that an ambiguous boundary point has one symmetric spacing on both sides. At the lower boundary, its predecessor in the previous binade lies only $2^{n-5}$ below it.

### Explain the incorrect scaling choices

The candidate $2^{-n}$ confuses the magnitude exponent with a fractional-place count. The candidate $2^n$ reports the binade's starting value, omitting fraction precision. The candidate $2^{n-5}$ counts five explicit fraction bits even though the leading bit is already included. In the boundary question, spacing changes at a binade transition; exponent range determines whether values exist, while significant-bit count determines their precision. Subnormal formats can have another leading-bit and exponent rule, and overflow at the highest exponent removes an otherwise expected neighbor. The question expressly grants adequate exponent range and normal values, so those exceptions do not invalidate the stated local-grid result.

## Q40

**Correct option: 1.**

### Prove capacity and place-value preservation independently

Each hexadecimal position has sixteen possible digit values. For $n$ positions there are $16^n=(2^4)^n=2^{4n}$ distinct strings, including leading zeros. An injective fixed-length binary representation therefore needs at least $4n$ bits. Grouping exactly four bits per hexadecimal position attains that bound, establishing both necessity and sufficiency.

The same grouping preserves numerical value: digit $d_j$ at hexadecimal position $j$ has weight $16^j=2^{4j}$. Its four-bit expansion contributes binary weights at positions $4j$ through $4j+3$, whose sum is $d_j2^{4j}$. Concatenating the groups is consequently an exact representation transformation. For $n=5$ hexadecimal positions the complete format contains $16^5=2^{20}$ words, requiring $20$ binary bits. Its largest unsigned value is $2^{20}-1$, while the all-zero word is also included.

### Separate format width, a value's minimal length and maximum label

The candidate $n$ gives one binary position per hexadecimal digit and cannot represent sixteen digit choices. The candidate $16n$ treats the number of digit choices as a bit count; four bits already distinguish sixteen choices. The candidate $2^n$ has no consistent fixed-width radix-capacity role. In the conceptual question the valid statement is that a particular value's minimal numeral may be shorter than the format width. Leading zeros preserve its positional value but still belong to the specified stored word. The number of words is $2^{4n}$, while their largest unsigned label is $2^{4n}-1$ because labels begin at zero. Hex notation alone does not establish signedness: a declared two's-complement decoder can interpret the same $4n$ bits as negative. Determine the requested capacity or interpretation before reporting a bit count or a value.

## Q41

**Correct option: 4.**

### Prove capacity and place-value preservation independently

Each hexadecimal position has sixteen possible digit values. For $n$ positions there are $16^n=(2^4)^n=2^{4n}$ distinct strings, including leading zeros. An injective fixed-length binary representation therefore needs at least $4n$ bits. Grouping exactly four bits per hexadecimal position attains that bound, establishing both necessity and sufficiency.

The same grouping preserves numerical value: digit $d_j$ at hexadecimal position $j$ has weight $16^j=2^{4j}$. Its four-bit expansion contributes binary weights at positions $4j$ through $4j+3$, whose sum is $d_j2^{4j}$. Concatenating the groups is consequently an exact representation transformation. For $n=8$ hexadecimal positions the complete format contains $16^8=2^{32}$ words, requiring $32$ binary bits. Its largest unsigned value is $2^{32}-1$, while the all-zero word is also included.

### Separate format width, a value's minimal length and maximum label

The candidate $n$ gives one binary position per hexadecimal digit and cannot represent sixteen digit choices. The candidate $16n$ treats the number of digit choices as a bit count; four bits already distinguish sixteen choices. The candidate $2^n$ has no consistent fixed-width radix-capacity role. In the conceptual question the valid statement is that a particular value's minimal numeral may be shorter than the format width. Leading zeros preserve its positional value but still belong to the specified stored word. The number of words is $2^{4n}$, while their largest unsigned label is $2^{4n}-1$ because labels begin at zero. Hex notation alone does not establish signedness: a declared two's-complement decoder can interpret the same $4n$ bits as negative. Determine the requested capacity or interpretation before reporting a bit count or a value.

## Q42

**Correct option: 3.**

### Prove capacity and place-value preservation independently

Each hexadecimal position has sixteen possible digit values. For $n$ positions there are $16^n=(2^4)^n=2^{4n}$ distinct strings, including leading zeros. An injective fixed-length binary representation therefore needs at least $4n$ bits. Grouping exactly four bits per hexadecimal position attains that bound, establishing both necessity and sufficiency.

The same grouping preserves numerical value: digit $d_j$ at hexadecimal position $j$ has weight $16^j=2^{4j}$. Its four-bit expansion contributes binary weights at positions $4j$ through $4j+3$, whose sum is $d_j2^{4j}$. Concatenating the groups is consequently an exact representation transformation. Five hexadecimal positions correspond to twenty binary bits; eight correspond to thirty-two. A particular value such as one can have a shorter minimal numeral while still occupying that fixed format.

### Separate format width, a value's minimal length and maximum label

The candidate $n$ gives one binary position per hexadecimal digit and cannot represent sixteen digit choices. The candidate $16n$ treats the number of digit choices as a bit count; four bits already distinguish sixteen choices. The candidate $2^n$ has no consistent fixed-width radix-capacity role. In the conceptual question the valid statement is that a particular value's minimal numeral may be shorter than the format width. Leading zeros preserve its positional value but still belong to the specified stored word. The number of words is $2^{4n}$, while their largest unsigned label is $2^{4n}-1$ because labels begin at zero. Hex notation alone does not establish signedness: a declared two's-complement decoder can interpret the same $4n$ bits as negative. Determine the requested capacity or interpretation before reporting a bit count or a value.

## Q43

**Correct option: 2.**

### Prove capacity and place-value preservation independently

Each hexadecimal position has sixteen possible digit values. For $n$ positions there are $16^n=(2^4)^n=2^{4n}$ distinct strings, including leading zeros. An injective fixed-length binary representation therefore needs at least $4n$ bits. Grouping exactly four bits per hexadecimal position attains that bound, establishing both necessity and sufficiency.

The same grouping preserves numerical value: digit $d_j$ at hexadecimal position $j$ has weight $16^j=2^{4j}$. Its four-bit expansion contributes binary weights at positions $4j$ through $4j+3$, whose sum is $d_j2^{4j}$. Concatenating the groups is consequently an exact representation transformation. Five hexadecimal positions correspond to twenty binary bits; eight correspond to thirty-two. A particular value such as one can have a shorter minimal numeral while still occupying that fixed format.

### Separate format width, a value's minimal length and maximum label

The candidate $n$ gives one binary position per hexadecimal digit and cannot represent sixteen digit choices. The candidate $16n$ treats the number of digit choices as a bit count; four bits already distinguish sixteen choices. The candidate $2^n$ has no consistent fixed-width radix-capacity role. In the conceptual question the valid statement is that a particular value's minimal numeral may be shorter than the format width. Leading zeros preserve its positional value but still belong to the specified stored word. The number of words is $2^{4n}$, while their largest unsigned label is $2^{4n}-1$ because labels begin at zero. Hex notation alone does not establish signedness: a declared two's-complement decoder can interpret the same $4n$ bits as negative. Determine the requested capacity or interpretation before reporting a bit count or a value.

## Q44

**Correct option: 3.** The stored real value is $-2.0$ after nearest-even rescaling.

### Decode the raw inputs before multiplying

Two fractional bits give scale $1/4$. Signed raw integers $-6$ and $5$ represent $-6/4=-1.5$ and $5/4=1.25$, respectively. Their exact real product is $-30/16=-1.875$. The raw integer product $-30$ has four fractional bits; it must be converted back to a grid with two fractional bits. Thus the ideal target raw code is
$$-30/4=-7.5.$$
Its nearest integer neighbors are $-8$ and $-7$, equidistant by one half. The index $-8$ is even, whereas $-7$ is odd, so nearest-even selects $-8$. Eight-bit two's-complement storage is `11111000`, whose real decoder gives $-8/4=-2.0$.

### Check signed error, range and the alternatives

The stored error is $-2-(-1.875)=-0.125$, exactly half the target grid spacing $1/4$. The chosen raw integer fits the eight-bit signed range $[-128,127]$. A general implementation should form a wide product before rounding even though this particular product also fits eight signed bits.

Option 1, $-1.75$, would select index $-7$, as truncation toward zero would do. Option 2 is the exact real product but is not on the two-fractional-bit target grid. Option 4 interprets raw product $-30$ with scale $1/4$ instead of the product scale $1/16$. Negative nearest-even rounding is not implemented by always adding a positive one half and truncating. Locate both integer grid neighbors and use their parity at a tie. This distinguishes rounding a signed real from applying an arithmetic shift, which instead rounds the raw division downward.

## Q45

**Correct option: 2.** Quantization stores 1.5, selecting the even lower raw index at an exact midpoint.

### Convert the target to raw grid units

An unsigned fixed-point format with two fractional bits has spacing $\Delta=1/4$. Its legal real values are integer multiples $I/4$, subject to the declared sufficient range. Scaling the exact target gives
$$1.625\cdot4=6.5.$$
The adjacent integer codes are 6 and 7, representing $6/4=1.5$ and $7/4=1.75$. Each is distance $0.125=\Delta/2$ from the target. Nearest-distance comparison establishes a tie; it does not determine a direction.

Ties to even applies to the retained integer code: 6 is even and 7 is odd. Thus the result is code 6, real value 1.5. Its signed error is $1.5-1.625=-0.125$. The phrase even does not mean that the real stored number must be an even integer; the index is the relevant unit.

### Analyze the rejected answers and a contrasting tie

Option 1, 1.25, is two grid indices away from the upper neighbor and has error 0.375, so it is not nearest. Option 3 retains the exact input, but 1.625 requires three fractional binary positions because it equals $1.101_2$. Option 4 chooses the odd upper index and would correspond to another tie rule. For comparison, 1.875 scales to 7.5 and rounds upward to index 8, real value 2, because that upper index is even. Nearest-even can move either way depending on parity. The sufficient-range premise excludes clipping; without it, endpoint handling must be declared and the half-spacing error statement may fail. Decode, scale, find neighbors, decide distance and parity, then check range in that order.
