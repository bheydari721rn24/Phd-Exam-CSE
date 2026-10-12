from pathlib import Path
import re
B=Path(__file__).parent;E=B/'deep-library-revision';A={}
A[1]=r'''**Correct option: 4.** This is a four-bit hardware representation question, not an instruction to execute overflowing signed C arithmetic.

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

Opposite-sign operands sum between the two inputs, so cannot leave the signed range. Two nonnegative operands can exceed the upper endpoint; two negative operands can fall below the lower endpoint. Test the exact mathematical sum against both endpoints before interpreting low bits. For a C17 expression evaluated in a signed type, an unrepresentable result has undefined behavior; two's-complement storage does not authorize predicting a wrapped C output. This distinction prevents a correct hardware calculation from becoming an incorrect language answer.'''
A[2]=r'''**Correct option: 3.** The false description equates rounding with truncation. The formula itself performs rounding under the stated exact-real model.

### Start from the definition of CHOP

For an exact real $t$, truncation toward zero is
$$t\ge0\ \Rightarrow\ \operatorname{CHOP}(t)=\lfloor t\rfloor,\qquad t<0\ \Rightarrow\ \operatorname{CHOP}(t)=\lceil t\rceil.$$
Every integer therefore remains unchanged, establishing option 1. For a negative $x$, subtracting one half before truncation implements nearest-integer rounding, with ties away from zero: at $x=-2.49$ the intermediate is $-2.99$ and the result $-2$; at $x=-2.5$ the intermediate is $-3$ and the result $-3$. This is the tie convention implicit in option 2, rather than ties to even.

For nonnegative $x$, scaling by one hundred moves the hundredths digit into the integer position. At $x=1.239$ the two relevant calculations are
$$\frac{\operatorname{CHOP}(123.9)}{100}=1.23,\qquad
\frac{\operatorname{CHOP}(123.9+0.5)}{100}=1.24.$$
Adding one half decides which hundredth is nearest; it does not merely remove all digits beyond the hundredths place. Hence option 3's claim of truncation is false, while option 4 correctly describes truncation. At the halfway input $1.235$, the offset formula returns $1.24$, clarifying its upward tie rule for positive inputs. The extension to $x=0$ also works, although it is not needed to broaden the original source's domain.

### Keep the mathematical primitive separate from a C cast

CHOP is defined here for all exact real arguments. A C floating-to-integer conversion first discards the fraction but additionally requires the resulting integer to fit the destination. Binary approximation of $100x$ can move a intended decimal halfway value slightly to either side. Thus this proof neither authorizes an out-of-range C cast nor guarantees exact decimal rounding for every `double`. Identify the arithmetic and tie model before applying a memorized offset formula.'''
A[3]=r'''**Correct option: 1.** The difference is $0.01$, caused by two distinct intermediate-rounding paths.

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

The left branch introduces error $0.004$ at its first node and then rounds again; the right branch's first node is already exact. This makes the mechanism visible instead of merely asserting that floating arithmetic is inaccurate. Always draw or record the evaluation tree, propagate each rounded output into the next operation, and preserve the stated decimal format. Replacing this machine with binary64 would answer another question.'''
A[4]=r'''**Correct option: 1.** The intermediate expression has value $-16$ and type `int`; the separately converted unsigned character has value $240$.

### Trace a typed value through three stages

The eight-bit object stores $u=15$. Since every possible `unsigned char` value $0,\ldots,255$ fits the declared 32-bit `int`, integer promotion converts the operand to `int` before unary complement. The operator therefore complements the promoted pattern, not an isolated eight-bit byte. In the specified two's-complement representation,
$$\mathord{\sim}15=-15-1=-16.$$
Converting this integer to the eight-bit unsigned destination selects its nonnegative residue:
$$-16= (-1)256+240,\qquad (\text{unsigned char})(\mathord{\sim}u)=240.$$

| Stage | Type | Value |
|---|---|---:|
| Stored source | `unsigned char` | $15$ |
| Promoted operand | `int` | $15$ |
| Complemented expression | `int` | $-16$ |
| Explicit narrowing destination | `unsigned char` | $240$ |

The alternative $(240,240)$ incorrectly truncates the expression to eight bits before giving its first value. The pair $(-16,-16)$ gives an impossible negative value to an unsigned destination. The pair $(15,240)$ leaves the intermediate operand unchanged.

### Boundary and transfer

For this model, source $u=0$ produces intermediate $-1$ and final $255$; source $u=255$ produces intermediate $-256$ and final zero. These checks expose the difference between expression width and storage width. The identity $\mathord{\sim}v=-v-1$ uses the stipulated two's-complement representation, rather than all historically permitted C17 signed representations. The unsigned destination's modulo conversion is a language rule; the signed complement's numerical interpretation additionally uses this declared representation. Neither stage is signed arithmetic overflow.'''
A[5]=r'''**Correct option: 1.** The values are $2.0$ and two floating approximations to $7/3$. An outer cast cannot recover a discarded remainder.

### Compare the three expression trees

For integer operands $a=7,b=3$, C17 integer division yields quotient two and remainder one:
$$7=2\cdot3+1.$$
In `(double)(a/b)`, the division node receives two integers. It returns integer two; only the parent cast changes that value's type to `double`. The final value is exactly $2.0$ in the declared format.

In `(double)a/b`, the left leaf becomes `double` seven before the division. The usual arithmetic conversions change integer three to `double` three, so the division is floating. In `a/(double)b`, converting the right leaf triggers the same common type and the same floating operation. Under the chapter's binary64 nearest-even model, both produce the same stored approximation to $7/3$; the exact fraction is not representable in finite binary precision because its denominator includes a factor other than two.

| Expression | Division operand types | Division result before any outer action |
|---|---|---|
| `(double)(a/b)` | `int`, `int` | Integer $2$ |
| `(double)a/b` | `double`, `double` | Rounded approximation to $7/3$ |
| `a/(double)b` | `double`, `double` | The same approximation |

Option 2 wrongly makes the first division floating. Option 3 ignores the conversion of the left operand in the second expression. Option 4 ignores the conversion of the right operand in the third. Assigning `a/b` into a `double` destination has the same lost-remainder problem as the first expression. For a general integer pair, first verify a nonzero divisor and a representable integer quotient; only then compare cast placement. The destination declaration does not retroactively determine a child operation's type.'''
A[6]=r'''**Correct option: 2.** The comparison yields integer one. The selected source value is converted to an unsigned common type before comparison.

### Separate static typing from runtime selection

The alternatives `x` and `y` have equal-rank `int` and `unsigned int` types. Applying the usual arithmetic conversions gives the conditional expression type `unsigned int`. Both alternatives contribute their types to this decision; only the selected alternative is evaluated for its value. The selector is true, so the source is $x=-1$. Conversion to the common unsigned type gives
$$-1\bmod 2^{32}=2^{32}-1=4294967295.$$
The right operand `2u` already has unsigned type. Hence the actual comparison is
$$4294967295>2,$$
which is true, with C logical result type `int` and value one.

The zero option would be correct for a signed comparison $-1>2$ but skips the conditional's conversion. Undefined behavior is incorrect: converting a negative integer to unsigned is defined modulo the unsigned range. Runtime dependence on the branch is also incorrect for the stated constant selector; although a different selector can select a different value, it cannot remove the common-type step.

### Test the mechanism by changing one premise

If the selector were false, the conditional value would be unsigned one and the comparison would return zero. If both alternatives were signed `int`, selecting $-1$ would keep the signed type and return zero. If a higher-rank signed alternative could represent every unsigned alternative value, the common type could instead be signed. Thus neither the sign of the chosen source nor the syntax of the selector alone answers the question. Draw one lane for branch types and a second lane for selected values; merge them before evaluating the comparison.'''
A[7]=r'''**Correct option: 2.** The value is zero and the division is not evaluated. The proof depends on control of evaluation, not cancellation of arithmetic.

### Trace reachability

The first expression `x != 0` reads $x=0$ and produces integer zero. C17 logical AND evaluates that left operand first and sequences it before any evaluation of the right operand. Because it is false, the right operand is skipped. Consequently neither `10/x` nor its comparison with two executes, and the entire logical expression is `int` zero.

| Checkpoint | Executed? | Result |
|---|---|---|
| Read `x != 0` | Yes | False |
| Read `10/x` | No | No value is computed. |
| Read `10/x > 2` | No | No value is computed. |
| Complete `&&` | Yes | $0$ |

The division-by-zero alternative incorrectly assumes eager evaluation. The value-one alternative contradicts the false left operand. The implementation-defined alternative ignores a language-mandated short-circuit rule. A simulator must mark the skipped node as **not evaluated**, rather than invent zero as the division's output.

### Changes that remove the protection

Replacing `&&` with bitwise `&` evaluates both operands and reaches division by zero; the result is undefined, not a predicted bit pattern. Reversing the original logical operands also puts the division before its guard. For a nonzero $x$, the right operand becomes reachable, so its own domain must still be checked. In a general quotient `a/x`, protecting only $x\ne0$ does not exclude signed minimum divided by $-1$. A correct guard must cover every exceptional input, and it must be evaluated before the dangerous operation. Precedence fixes grouping; short-circuit semantics provide this particular order and reachability.'''
A[8]=r'''**Correct option: 2.** The unsigned expression yields zero; the signed expression has undefined behavior.

### Determine expression types first

In `UINT_MAX + 1u`, both operands have `unsigned int` type. Under the declared no-padding 32-bit model, the largest unsigned value is $2^{32}-1$. Unsigned addition implements residue arithmetic:
$$((2^{32}-1)+1)\bmod2^{32}=0.$$
This is a language-defined unsigned operation. The suffix on `1u` establishes its type before addition, rather than converting an already-overflowed signed result afterward.

In `INT_MAX + 1`, both operands are `int`. The mathematical result is $2^{31}$, outside the signed domain $[-2^{31},2^{31}-1]$. C17 does not specify a numeric result for this signed overflow. A processor might store a low-bit pattern associated with `INT_MIN`, but that observation is not the semantics of the C expression.

| Alternative | Why it fails |
|---|---|
| Both wrap to zero | Signed overflow is not defined as unsigned reduction, and even a hardware low-bit signed reading would be the negative endpoint. |
| Both are undefined | The unsigned operation is explicitly defined. |
| Signed is guaranteed `INT_MIN` | Two's-complement representation does not override signed arithmetic rules. |

### A safe signed guard

For a positive signed addend $b$, overflow is avoided by checking $a\le\mathrm{INT\_MAX}-b$ before computing $a+b$. With $a=\mathrm{INT\_MAX}$ and $b=1$, this test fails. The subtraction in the guard is itself safe for a positive representable $b$. For a negative addend, use $a\ge\mathrm{INT\_MIN}-b$. Never test whether the overflowed sum is negative: that executes the invalid operation first. A simulation should stop the signed lane at classification while letting the separate unsigned lane demonstrate the modular zero.'''
A[9]=r'''**Correct option: 2.** The equality is true under the explicitly required binary64 rounding of each operation.

### Locate the adjacent representable values

Binary64 has $p=53$ significant binary bits. At $a=2^{53}=9007199254740992$, the next binade has spacing
$$\Delta=2^{53-53+1}=2.$$
The two neighbors of the exact sum $a+1$ are therefore $a$ and $a+2$. The exact sum is their midpoint. Write the endpoint as a significand integer $2^{52}$ times two; that significand integer is even, while the next one's $2^{52}+1$ is odd. Nearest-even therefore returns $a$:
$$\operatorname{RN}(a+1)=a,\qquad \operatorname{RN}(a+1)=a\ \text{is true}.$$
The equality produces integer one. It is floating addition, so no signed-integer overflow classification applies.

The zero alternative assumes consecutive integers remain distinct forever in a finite-precision format. Undefined behavior is not involved in this finite addition under the stated machine. The sign-only alternative is irrelevant to the positive input and does not state a rounding rule.

### A second midpoint checks the explanation

The exact sum $a+3$ is midway between $a+2$ and $a+4$. This time the lower neighbor has an odd significand and the upper an even one, so nearest-even chooses $a+4$. Rounding is therefore not simply always downward at a tie. Immediately below $a$, spacing is one; immediately above it, spacing is two. A ruler must display this boundary correctly. The explicit exclusion of excess intermediate precision matters: an implementation retaining a wider intermediate could distinguish $a+1$ before a later conversion. The answer follows the specified format and rounding checkpoints, not an assumption that every C evaluation rounds exactly as stored binary64.'''
A[10]=r'''**Correct option: 2.** The requested rounded value is $-2.38$ under exact-real arithmetic and ties away from zero.

### Scale, offset in the correct direction, truncate, then scale back

The target decimal unit is one hundredth. Multiplying $x=-2.376$ by one hundred gives $-237.6$. For a negative value, shift one half toward the negative direction before truncating toward zero:
$$100x-0.5=-238.1,\quad \operatorname{CHOP}(-238.1)=-238,\quad -238/100=-2.38.$$
The integer truncation removes the remaining fractional magnitude toward zero, after the offset has selected the nearest hundredth.

Compute the other options rather than merely naming them wrong:
$$\operatorname{CHOP}(-237.6+0.5)/100=-237/100=-2.37,$$
$$\operatorname{CHOP}(-237.6)/100=-2.37,$$
$$\operatorname{CHOP}(-2.376-0.5)/100=-2/100=-0.02.$$
The first uses the positive-input offset; the third only truncates; the fourth rounds at the units position and then scales that unrelated integer down.

### Derive and test the halfway convention

For $x<0$, nearest hundredth with ties away from zero is $\operatorname{CHOP}(100x-1/2)/100$. At $x=-2.375$, the intermediate becomes exactly $-238$, returning $-2.38$. At $x=-2.374$, it becomes $-237.9$, truncating to $-237$ and returning $-2.37$. Both sides of the halfway boundary are consistent. For positive input the sign of the half-unit offset reverses. These expressions assume exact real scaling and an unbounded CHOP primitive. A finite C floating implementation must separately consider representation error in the scaled input and whether its truncated integer fits the cast destination. That separate engineering problem does not alter this source's mathematical model.'''
A[11]=r'''**Correct option: 2.** The macro expands to tokens that evaluate to five, not the square of three.

### Expand before parsing

The preprocessing directive is on its own source line:
```c
#define SQR(x) x*x
```
Calling `SQR(1+2)` substitutes the argument tokens for each occurrence of `x`:
```c
1+2*1+2
```
Multiplication binds more tightly than addition, so the arithmetic tree is $(1+(2\cdot1))+2$, yielding $1+2+2=5$. The macro never first evaluates the argument to a local value three; that would be function-call reasoning applied to token substitution.

The nine alternative assumes grouping absent from the replacement list. The seven alternative groups only one side as intended, again inventing parentheses. Undefined behavior is incorrect for this side-effect-free expression: every evaluated arithmetic result fits the declared integer model.

### Two different repairs solve two different problems

Replacing the macro body with `((x)*(x))` yields `((1+2)*(1+2))` and fixes grouping for this argument. It does not fix repeated evaluation. For `SQR(i++)`, the parenthesized macro still contains two increments without a sequencing relation; in C17 it has undefined behavior. An actual function taking a scalar parameter evaluates this single argument expression once, then squares a stored local value, provided that square is representable. An inline function can therefore fix duplication as well as grouping, but does not abolish arithmetic range checks.

Analyze macros in three stages: substitute tokens, construct the resulting syntax tree, then inspect side effects and arithmetic domains. A simulator may show the five for this original expression; its side-effect extension must stop at an undefined classification instead of choosing an imaginary left-to-right order.'''

families=[
(12,[4,3,2,1],r'''Let $w=n+3$ be the number of unsigned value bits. Bit position $j$ contributes $2^j$. Setting every bit gives the geometric sum
$$\sum_{j=0}^{w-1}2^j=2^w-1=2^{n+3}-1.$$
There are $2^w$ different patterns, but the represented values start at zero, so the maximum is one less than the count. This proves the endpoint rather than guessing it from a type name. The representation has no negative values and no padding under the explicit premise.

The competing $2^{n+3}$ is the number of patterns and needs one more value bit to store as an unsigned value. The expression $2^{n+2}-1$ uses the positive endpoint of a different signed-width interpretation. The expression $2^n$ ignores three declared positions and is not even the maximum for an $n$-bit unsigned word. These are structural errors, not small numerical rounding errors.

For an actual C type, `sizeof` measures storage bytes; `CHAR_BIT` and possible padding determine how many of those bits are value bits. C guarantees at least the mandated minimum ranges, not the same exact width for every integer name on every implementation. This question defines an abstract unsigned representation, not the existence of arbitrary-width built-in C types.''',
[r'''At $n=5$, $w=8$, the all-one pattern is `11111111` and $128+64+32+16+8+4+2+1=255$. Option 1's $256$ counts patterns including zero; option 2's $127$ omits the top value-bit weight; option 3's $32$ uses the wrong exponent.''',r'''At $n=8$, $w=11$, the sum is $1024+512+\cdots+1=2047$. The option $1023$ discards the highest contribution, $256$ uses $2^n$, and $2048$ is the pattern count. Only option 3 gives the endpoint.''',r'''The derivation holds for every positive integer $n$: the finite geometric sum proves option 2. Substitution at two widths corroborates it but is not the proof of the universal identity. Even the hypothetical $n=0$ extension would give seven; the stated question needs only positive parameters.''',r'''Option 1 is the scope statement. For eight value bits the maximum is $255$, while eight storage bytes describe a different amount of space. Types with the same storage can also differ in padding or representation. Options 2–4 respectively erase language/platform differences, invent negative unsigned values, and confuse cardinality with endpoint.''']),
(16,[1,4,3,2],r'''Let $M=2^{n+3}$ be the modulus. The largest register value is $M-1$. Addition of $n+1$ gives
$$s=(M-1)+(n+1)=M+n.$$
Low-width storage retains the nonnegative residue of $s$ modulo $M$. For every positive integer $n$, $2^n\ge n+1$, as proved by induction: it holds at one, and doubling $n+1$ is at least $n+2$. Hence $n<M$ and
$$s=1\cdot M+n,\qquad s\bmod M=n.$$
Exactly one modulus is discarded in this family. The carry is not a minus sign; the stored unsigned residue remains nonnegative.

The unreduced expression $2^{n+3}+n$ is the mathematical sum, not the register contents. The value $n+1$ fails to include the initial maximum's residue $-1$. The value $-n$ is a sign mistake with no basis in unsigned reduction. Always distinguish exact total, discarded carry and stored result.

A narrow C object can follow a different intermediate route. An eight-bit unsigned source $255$ can promote to 32-bit signed `int`; adding six yields the representable expression value $261$, and only assigning to an unsigned byte produces five. The hardware register and this typed C expression reach the same stored byte through different semantic checkpoints. A sufficiently large multiplication of promoted narrow unsigned sources can even overflow signed `int`, despite the source objects being unsigned.''',
[r'''At $n=5$, $M=256$ and $255+6=261=256+5$, so option 1 stores five. The displayed $261$ is the exact total; six is only the addend; negative five is outside the unsigned domain.''',r'''At $n=8$, $M=2048$ and $2047+9=2056=2048+8$, so option 4 stores eight. The other values are the addend nine, unreduced total $2056$, and an invalid negative residue.''',r'''For every positive $n$, the proof that $n<M$ makes $n$ the canonical residue, so option 3 is the general answer. Merely observing one wrap at two sample widths would not establish the claim without this bound.''',r'''Option 2 recognizes the expression/destination distinction. A declaration of a narrow unsigned result variable does not force the children of its initializing expression to use that narrow arithmetic. Promotions can widen and change signedness before an operator runs; narrowing occurs afterward. Hardware modular addition cannot silently replace the language trace.''']),
(20,[4,3,2,1],r'''In an $n$-bit two's-complement representation, assign weight $-2^{n-1}$ to the sign bit and positive weights $2^j$ to lower positions. A pattern has value
$$v=-b_{n-1}2^{n-1}+\sum_{j=0}^{n-2}b_j2^j.$$
To minimize it, set the sign bit and clear every positive contribution. Therefore $v_{\min}=-2^{n-1}$. To maximize it, clear the sign bit and set every lower position, giving $v_{\max}=2^{n-1}-1$. The range contains $2^n$ distinct integers and is asymmetric by one.

The competing $-2^n$ requires an extra sign-weight position. The expression $-(2^{n-1}-1)$ omits the actual most-negative pattern; it is merely the negative of the positive maximum. Zero ignores every negative pattern. These distinctions follow directly from positional weights.

Negating the minimum has mathematical result $2^{n-1}$, which exceeds the same-width signed maximum. If negation is evaluated in a signed type whose minimum is this value, as in `-INT_MIN`, it is undefined. A narrow signed source may first promote to a wider `int`; for signed char negative128 under int32, unary minus then yields representable int128. Converting that result back to signed char is a separate out-of-range signed conversion, with an implementation-defined result or signal. A cast afterward cannot repair an operation that already overflowed; an actual promotion or widening before the operator can change its domain. The two's-complement premise is essential to this endpoint pair, rather than a universal historical C17 representation guarantee.''',
[r'''For $n=5$, pattern `10000` has weight $-16$, while `01111` is $15$. Option 4 gives $-16$; the other numerical endpoints either use six bits, exclude the sign-only pattern, or omit negative values.''',r'''For $n=8$, pattern `10000000` represents $-128$ and `01111111` represents $127$. The negative endpoint is therefore option 3. Mathematical negation of $-128$ would require positive $128$, unavailable in this same range.''',r'''The sign-only pattern constructs the claimed lower endpoint for every positive abstract width, so option 2 follows. At width one the abstract set is $\{-1,0\}$; this checks the positional proof, without claiming standard C provides a one-bit signed arithmetic type.''',r'''Option 1 identifies the boundary failure: the negative minimum has no positive counterpart in the same signed range. A mathematical absolute-value result can exceed its argument's type. Opposite endpoints are not symmetric, and low-bit hardware negation is not a portable output prediction for undefined C arithmetic.''']),
(24,[4,3,2,1],r'''Use the explicitly repaired **minimum-layout policy**: the first member begins at offset zero, each following member occupies the earliest aligned offset, no extra discretionary padding is inserted, and final size is rounded to record alignment. Without this policy the stated widths and alignments alone do not force a unique C structure size.

After the first $n$ bytes, the next member must start at a multiple of four at least $n$. Its earliest offset is
$$o=4\left\lceil\frac n4\right\rceil.$$
It occupies bytes $o$ through $o+3$, so the end offset is $o+4$. This is already divisible by four, giving minimum size
$$S=4\left\lceil\frac n4\right\rceil+4.$$
Write $n=4q+r$, $0\le r<4$. Internal padding is zero if $r=0$ and $4-r$ otherwise; it varies from zero to three bytes. This residue proof explains the ceiling and rules out assuming a constant padding count.

The expression $n+4$ ignores required internal padding whenever $r\ne0$. The expression $4\lceil n/4\rceil$ stops at the second member's starting offset and omits its storage. The expression $n+8$ assumes four padding bytes, which minimum alignment never requires here. Alignment adds unused positions; it does not erase member bytes.

C permits extra unnamed internal or tail padding, so an ABI's precise policy, member alignment, packing directives and record alignment must be specified before a numerical `sizeof` claim. This solution computes the declared minimal model, not an implementation-independent size.''',
[r'''For $n=5$, occupied first-member offsets are $0\ldots4$, padding is $5\ldots7$, and the second member is $8\ldots11$. Size is twelve, option 4. A layout putting that member at offset twelve and ending at sixteen also satisfies alignment, showing why the new minimum-policy premise is necessary.''',r'''For $n=9$, first-member offsets are $0\ldots8$, padding is $9\ldots11$, and the second member is $12\ldots15$. Size is sixteen, option 3. The distractors $13,12,17$ respectively omit padding, omit the last member, or assume a constant four padding bytes.''',r'''The least aligned-offset construction proves option 2 for all positive parameters. At $n=8$, there is no internal padding and size twelve. At $n=9$, size jumps to sixteen; this stepwise behavior is the reason a linear formula $n+c$ cannot solve the family.''',r'''Option 1 correctly requires stated layout rules. Widths alone give a lower bound, not every offset. A three-member extension with widths $5,4,1$ and alignments $1,4,1$ has offsets $0,8,12$ and size sixteen under record alignment four; its final three bytes are tail padding. Reordering as $4,5,1$ gives offsets $0,4,9$ and size twelve.''']),
(28,[3,2,1,4],r'''An actual two-dimensional array has $n$ rows and $n+1$ elements per row. Arrays contain their elements contiguously; each row occupies $4(n+1)$ bytes and all rows occupy
$$N=n(n+1)\ \text{elements},\qquad S=4n(n+1)\ \text{bytes}.$$
At zero-based element $(i,j)$, the byte offset from the array start is $4(i(n+1)+j)$, for $0\le i<n$ and $0\le j<n+1$. The final element begins at $S-4$ and ends at $S-1$, independently checking the total.

The alternative $4n$ accounts for only one four-byte element per row. The expression $4(n+1)$ is one row's stride, not the complete array. The expression $n(n+1)$ counts elements and leaves out their four-byte unit. A correct dimensional calculation keeps counts and bytes distinct.

In most value contexts, an array expression converts to a pointer to its first element. `sizeof` on the actual array is an important exception. A function parameter declared with array syntax is adjusted to a pointer type at declaration time; its `sizeof` therefore measures that pointer object, not the pointed-to allocation. For a two-dimensional parameter, the pointed-to row type can still preserve its column count. `sizeof a[0]` can be a row size even when `sizeof a` is pointer size. Neither pointer width nor the number of rows alone recovers the allocated byte count. The positive dimensions here avoid zero-length standard-array declarations; real allocation arithmetic must separately guard against overflow.''',
[r'''For $n=5$, there are $5\cdot6=30$ elements; row stride is twenty-four bytes and full size $5\cdot24=120$, option 3. The last element $(4,5)$ begins at $4(4\cdot6+5)=116$ and occupies bytes $116\ldots119$.''',r'''For $n=8$, there are seventy-two elements; row stride is thirty-six bytes and full size $8\cdot36=288$, option 2. The last element $(7,8)$ begins at $4(7\cdot9+8)=284$ and ends at byte287.''',r'''The product counts every ordered row/column pair exactly once; multiplication by the element width proves option 1 throughout the positive domain. Shape $(n,n+1)$ is part of the object model and must not be replaced by a pointer-to-pointer structure, whose pointed-to rows may occupy separate allocations.''',r'''Option 4 is correct: the adjusted parameter's `sizeof` measures a pointer. Under a separately declared eight-byte-pointer ABI, an original five-by-six array has size120, its row size24, but its adjusted parameter size8. This change does not make every array expression a pointer under every operator, and the pointer's bytes never include all its target elements.''']),
(32,[4,3,2,1],r'''Divide the positive number of flags by eight:
$$n=8q+r,\qquad0\le r<8.$$
The first $q$ bytes are full. If $r=0$, they hold every flag and no further byte is required. If $r>0$, at least one more whole byte is needed and is sufficient. Thus
$$B=q+\mathbf1_{r>0}=\left\lceil\frac n8\right\rceil.$$
This is a minimality proof: $B-1$ bytes have fewer than $n$ positions whenever $B>0$. The unused final-bit count is $8B-n$, between zero and seven. A partial final byte cannot be omitted merely because some of its positions are unused.

The distractor $n$ stores one flag per whole byte, a different format. The quantity $8n$ is neither the required bytes nor the number of stored flags; it mixes a byte's capacity with the count. The expression $\lceil n/8\rceil+1$ always allocates a redundant extra byte, including at exact byte boundaries.

For a nonnegative integer `n` in a finite unsigned type, compute `n/8 + (n%8 != 0)` instead of blindly evaluating `(n+7)/8`: the latter addition can wrap near the unsigned maximum. The quotient form has room for its final possible increment when the divisor is eight. This is a serialization contract, not a C bit-field allocation guarantee. C bit-field units, order and padding require implementation information; an array of Boolean objects is also not this packed format.''',
[r'''For $n=9$, $q=1,r=1$. The first byte holds eight flags and the second holds one flag plus seven unused positions. Minimum size is two, option 4. Eight positions are insufficient; three bytes are unnecessary.''',r'''For $n=17$, $q=2,r=1$. Two full bytes hold sixteen flags, and the seventeenth needs a third byte with seven unused positions. Minimum size is three, option 3; four bytes adds an unjustified spare byte.''',r'''Option 2 follows from quotient and remainder in both cases. At $n=8$ the answer is one, at nine two, at sixteen two and at seventeen three. These boundary transitions explain why unconditional quotient-plus-one is wrong. The extension to zero returns zero without allocating a fictitious partial byte.''',r'''Option 1 correctly separates wire-format packing from in-memory bit fields. With nine serialized flags this specified format needs two bytes, but nine `_Bool` array elements occupy nine times `sizeof(_Bool)` and a bit-field record can use implementation-specific allocation units. Their counts cannot be substituted for each other.''']),
(36,[1,4,3,2],r'''Let $p=n$ significant binary bits include the leading bit, and assume adequate exponent range for every number under discussion. Any positive integer below $2^p$ has at most $p$ binary digits and can be represented exactly. The endpoint $2^p$ itself is a power of two, requiring only one nonzero significand digit, so it is also exact.

In binade $[2^e,2^{e+1})$, normal values have spacing
$$\Delta_e=2^{e-p+1}.$$
At $e=p$, the spacing is two. The integer $2^p+1$ lies halfway between $2^p$ and $2^p+2$ and is not a representable value. Therefore the last endpoint through which **every consecutive nonnegative integer** is exact is $2^p$. This proves both inclusion and maximality.

The competing $2^p-1$ excludes the exact endpoint. The quantity $2^{p+1}$ includes odd integers already missing from the preceding binade. The value $p$ mistakes a count of significand bits for a numeric endpoint. More exponent range permits larger magnitudes but does not fill the missing significand positions.

Some larger integers remain exact: $2^p+2$, $2^{p+1}$ and suitable larger powers of two within exponent range. Thus this is not the largest finite value or the largest exact integer. For nearest-even rounding at the midpoint, inspect significand parity; exactness and rounding of a nonrepresentable integer are different questions. Subnormal spacing near zero and finite exponent endpoints need their own premises; the present question explicitly supplies enough exponent range.''',
[r'''At $p=5$, integers zero through32 are exact. Just below32 the spacing is one; above32 the values are32,34,36 and so on. Thirty-three is missing, so option 1's32 is the endpoint. Thirty-one is too small; sixty-four is exact itself but not all intervening integers are exact.''',r'''At $p=8$, integers zero through256 are exact, while257 is missing between256 and258. Option 4 gives256. The powers still represent512 exactly within range; that does not validate512 as an endpoint of consecutive exactness.''',r'''Option 3's $2^n$ is established by counting significant digits below the power and showing the immediate next odd integer is missing. A symbolic endpoint proof needs both arguments; finding an exact power of two alone does not establish that all preceding integers are exact.''',r'''Option 2 is correct. For $p=5$,34 and64 are exact but33 is not. Increasing the exponent cannot represent every integer if precision stays fixed. Spacing doubles at successive binades, so a uniformly spaced real-line picture would misrepresent the format.''']),
(40,[2,1,4,3],r'''The exact mathematical dividend is $a=-(3n+1)$ and the divisor is positive three. Its real quotient is
$$\frac a3=-n-\frac13.$$
C17 signed integer division discards the fractional part toward zero, giving $q=-n$. The remainder is determined from reconstruction:
$$r=a-3q=-(3n+1)+3n=-1,\qquad a=3q+r.$$
The remainder's magnitude is smaller than three and its nonzero sign matches the dividend. Mathematical floor would instead choose $-n-1$, with a positive remainder two; that is a different division convention.

The wrong positive quotient $n$ loses the dividend's sign. The expression $-3n-1$ is the original dividend rather than its quotient. The expression $-n-1$ imports floor division into C's truncation rule. Python `//` is an example of a different language rule; it must not be used to compute this answer without adjustment.

The stated representability premise includes evaluated intermediates. Under the chapter's int32 model, evaluating `-(3*n+1)` for positive `n` safely requires $n\le715827882$, since the upper endpoint makes $3n+1=2147483647$. A nonzero divisor alone is not enough for all signed inputs: `INT_MIN/-1` has an unrepresentable quotient, and `INT_MIN%-1` is undefined as well, even though its mathematical remainder is zero. First prove the operation's domain; only then use quotient/remainder identities. No simulator should return a numeric C result for an undefined boundary.''',
[r'''At $n=5$, the dividend is $-16$ and $-16=(-5)3+(-1)$. Quotient $-5$ is option 2. The floor candidate $-6$ would reconstruct $-16$ using remainder2, revealing its different convention; the other candidates are positive5 and unchanged dividend $-16$.''',r'''At $n=8$, the dividend is $-25$ and $-25=(-8)3+(-1)$. Quotient $-8$ is option 1. The alternative $-9$ is floor; eight reverses the sign; $-25$ omits division. The exact real quotient $-8.333\ldots$ clarifies why truncation moves upward toward zero.''',r'''Option 4 gives $-n$ for every positive parameter satisfying the intermediate and quotient range conditions. The proof uses the exact interval $-n-1<a/3<-n$, so truncation picks its less-negative endpoint. The examples corroborate a universal interval argument rather than replacing it.''',r'''Option 3 is the valid reconstruction rule on its defined domain. A negative dividend can have a negative remainder, as $-16\bmod3=-1$ under C semantics. A zero divisor or unrepresentable quotient invalidates the calculation; signed division is not always floor. For comparison, $16/(-3)=-5$ with remainder1, while $(-16)/(-3)=5$ with remainder $-1$.'''])]

for start,keys,proof,endings in families:
 for j,key in enumerate(keys):
  A[start+j]=f'**Correct option: {key}.**\n\n### Construct the value and state its domain\n\n'+proof+'\n\n### Requested instance or boundary\n\n'+endings[j]
A[44]=r'''**Correct option: 2.** The pair is $(4294967167,127)$, and the two destinations receive different residues of one common signed intermediate.

### Follow expression type before following assignment

The declared `uint8_t` object stores128 and has range zero through255. Every value fits the declared 32-bit `int`, so integer promotion turns the operand of complement into signed `int`. In two's complement,
$$\mathord{\sim}128=-128-1=-129.$$
This is a valid `int` value. Assigning it to `unsigned int` performs a defined integer conversion modulo $2^{32}$:
$$-129\bmod2^{32}=4294967296-129=4294967167.$$
The separately requested conversion back to `uint8_t` uses modulus256:
$$-129\bmod256=127.$$
Both residues satisfy their destination ranges and congruences. In particular, $4294967167=16777215\cdot256+127$, independently confirming their low-byte agreement.

Option 1 prematurely performs complement at the source byte's width, incorrectly predicting the first destination as127. Option 3's255 does not match the low eight bits of $-129$. Option 4 keeps the source128 for the first value instead of complementing it.

### Why the source's unsigned type is insufficient information

An unsigned narrow operand can promote to signed arithmetic if its full range fits `int`. The destination type enters after complement, not before it. If one explicitly converted the operand to `unsigned int` before complement, the intermediate expression would itself be unsigned, although it happens to yield the same first numeric residue in this model. The changed type can alter later comparisons and overflow reasoning. Track $(\text{type},\text{value})$ at every node, and distinguish numerical coincidence from identical language semantics. The two's-complement premise is used for the signed complement identity; it is not silently assumed for every historical C17 platform.'''
A[45]=r'''**Correct option: 1.** The comparison is false and its C value is integer zero.

### Type determination includes both alternatives

The conditional alternatives are signed `int` value $-1$ and equal-rank `unsigned int` value one. Their common arithmetic type is `unsigned int`. A true selector evaluates the first alternative, but its value is then converted to that common type:
$$-1\bmod2^{32}=4294967295.$$
In the subsequent comparison with signed integer zero, the same equal-rank conversion makes the zero unsigned. The actual value comparison is therefore
$$4294967295<0,$$
which is false. Its result is `int` zero; the operand type does not make the Boolean result an unsigned maximum.

The alternative one retains $-1$ without the conditional's required conversion. Undefined behavior is incorrect because converting a negative integer to unsigned is defined. The branch-dependence alternative is not an answer for the explicitly true selector; static type selection does not wait to discover which branch ran.

### Check both selection paths and a changed type premise

If the selector were false, unsigned one would also compare false against unsigned zero. Thus this particular less-than-zero test is false on both paths, even though the selected numeric values differ. If both alternatives were signed, selecting $-1$ would make the test true. If a higher-rank signed type represented the entire unsigned range, the usual conversion could instead retain a signed common type. A source-level branch that is never executed can still affect the expression's type. Keep the compile-time common-type calculation separate from the runtime selection trace; neither is an optional implementation choice here.'''

assert set(A)==set(range(1,46))
out='# Complete mathematical solutions: Data Types, Conversions, and Operators\n\n'+'\n\n'.join('## Q'+str(i)+'\n\n'+A[i] for i in range(1,46))+'\n'
(E/'p_types-solutions.md').write_text(out,encoding='utf-8')
print({'answers':len(A),'words':sum(len(a.split()) for a in A.values()),'minimum':min(len(a.split()) for a in A.values())})
