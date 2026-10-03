## Teaching through formulas and conceptual decisions

### Type the operands before evaluating the expression

The language for the following questions is C17. Machine widths are specified whenever needed. Integer promotions occur before the usual arithmetic conversions. With32-bit `int` and `unsigned int`, comparing `-1` to `1u` first converts the negative integer to the corresponding unsigned value, making the comparison false. This rule is not shared by every programming language and cannot be replaced by mathematical integer ordering.

For division of two integer operands, compute the truncated integer quotient before assigning to a floating object. `double z = 3/2;` stores1.0, while `double z = (double)3/2;` stores1.5. Casting the already computed quotient cannot restore its discarded fractional part. C17 signed division truncates toward zero and its remainder satisfies `a == (a/b)*b + a%b` for defined operands.

### Distinguish storage width, promotion width and assignment conversion

On an8-bit unsigned-character model, `unsigned char x = 250; x += 10;` computes the promoted sum260 in an `int` that can represent it, then converts the assignment back modulo256 to4. Unsigned arithmetic has modular semantics, but a narrow unsigned operand may be promoted to a signed `int` first. Therefore not every intermediate expression inherits the storage width of its variable.

### Classify behavior before predicting an output

Unsigned wraparound is defined. Overflow of a signed arithmetic result is undefined, so an exam answer must not invent a wrapped numeric result. A C17 expression with unsequenced modification and access to the same scalar, such as `i++ + i`, is undefined. Precedence determines parsing, while sequencing determines which evaluations may legally interact. Short-circuit logical operators specify evaluation order and can suppress an otherwise invalid operation.

For an IEEE binary64 exercise, exact integer representation extends through $2^{53}$. At larger magnitudes, neighboring integers need not be distinct after conversion. This is a specified numeric model for those questions, not a guarantee that every C implementation uses binary64 for `double`.

## Formula and conceptual problem bank

### Question 1. Integer division before assignment

In C17, what value is stored by `double z = 3 / 2;`?

**A.** 1.0

**B.** 1.5

**C.** 2.0

**D.** Undefined behavior.

**Answer: A.**

Both operands have integer type, so integer division computes1. Assignment then converts that integer to the floating value1.0. The destination type does not retroactively change evaluation of the right-hand expression. To obtain1.5, convert an operand before division or use a floating literal.

### Question 2. Cast location

In C17, which expression has value1.5?

**A.** `(double)(3/2)`

**B.** `(double)3/2`

**C.** `3/(int)2.0`

**D.** `(int)(3.0/2)`

**Answer: B.**

InB, one operand is converted before division and the other is converted by the arithmetic rules, producing a floating quotient. A converts an integer quotient already truncated to1. C has integer operands after its cast, andD explicitly converts a floating quotient back to an integer. Trace the typed intermediate result at each operator.

### Question 3. Signed and unsigned comparison

Assume32-bit `int` and `unsigned int`. What is the value of `-1 < 1u` in C17?

**A.** 0

**B.** 1

**C.** Implementation-defined under these assumptions.

**D.** Undefined behavior.

**Answer: A.**

The equal-rank unsigned operand forces conversion of$-1$ to unsigned, yielding $2^{32}-1$. This is greater than1, so the comparison is false and has integer value0. The conversion itself is defined. A mathematical comparison of the original values ignores the type conversion step.

### Question 4. Narrow assignment wrap

Assume8-bit `unsigned char` and an `int` that represents0 through260. After `unsigned char x=250; x+=10;`, what is$x$?

**A.** 4

**B.** 10

**C.** 250

**D.** 260

**Answer: A.**

The compound assignment performs the addition after promotion, yielding260, then converts to the unsigned-character range modulo256. The stored result is4. The intermediate need not wrap at8 bits, but the final conversion does.260 cannot be stored in the specified8-bit destination.

### Question 5. Negative remainder

In C17, what is `-7 % 3`?

**A.** -1

**B.** 1

**C.** 2

**D.** Undefined behavior.

**Answer: A.**

The quotient `-7/3` truncates toward zero to-2. Use the defining identity: remainder is `-7 - (-2)*3 = -1`. A nonnegative Euclidean remainder would be2, but C signed remainder follows truncating division. Neither division by a nonzero3 nor this quotient overflows.

### Question 6. Parsing a bitwise test

In C17, how is `x & 1 == 0` parsed?

**A.** `(x & 1) == 0`

**B.** `x & (1 == 0)`

**C.** `(x == 1) & 0`

**D.** It is syntactically invalid.

**Answer: B.**

Equality binds more tightly than bitwise AND, so the comparison `1 == 0` is evaluated as a subexpression and yields0. The whole value is therefore `x & 0`, zero for an integer$x$. To test whether the low bit is zero, write explicit parentheses around `x & 1`. Parsing and the intended English condition are separate.

### Question 7. A signed shift boundary

Assume a32-bit signed `int` with maximum2147483647. What is the C17 classification of `1 << 31`?

**A.** Defined and equal to-2147483648.

**B.** Defined and equal to2147483648.

**C.** Undefined behavior.

**D.** Always zero.

**Answer: C.**

The left operand is a signed nonnegative `int`. Its multiplication by $2^{31}$ is not representable in that signed type, so the signed-left-shift rule does not define this expression. The shift count itself is within the width, but representability still fails. Using `1u` would ask a different, defined unsigned question.

### Question 8. Unsequenced access

In C17, with initially `int i=1`, what is the classification of `i++ + i`?

**A.** Always2.

**B.** Always3.

**C.** Unspecified but always2 or3.

**D.** Undefined behavior.

**Answer: D.**

The modification from the postfix increment is unsequenced relative to the other read of the same scalar used to compute the sum. This violates the C17 sequencing rule and produces undefined behavior. Evaluating the left operand first by intuition does not supply a sequencing guarantee for the addition operator.

### Question 9. Short-circuit suppression

Initially `int x=0, y=2;`. Evaluate `x && ++y` in C17. What are the expression value and final$y$?

**A.** (0,2)

**B.** (0,3)

**C.** (1,2)

**D.** (1,3)

**Answer: A.**

Logical AND first evaluates$x$. Since it is zero, the result is already false and the right operand is not evaluated. Thus$y$ remains2 and the expression value is0. This is a specified sequencing and suppression rule; replacing logical AND with bitwise AND would evaluate both operands.

### Question 10. Array storage

Assume `sizeof(int)==4` and `sizeof(int*)==8`. For a local `int a[10];`, what is `sizeof a`?

**A.** 4

**B.** 8

**C.** 10

**D.** 40

**Answer: D.**

The operand of `sizeof` retains the array type in this case instead of undergoing ordinary array-to-pointer conversion. Ten elements of four bytes give40 bytes. Eight would be the size of a pointer variable, including an array parameter after its type adjustment, which is not this local declaration.

### Question 11. An unparenthesized macro

For `#define SQ(x) x*x`, what is the C value of `SQ(1+2)`?

**A.** 5

**B.** 6

**C.** 9

**D.** Undefined behavior.

**Answer: A.**

Text substitution yields `1+2*1+2`. Multiplication binds before addition, so the value is5. The macro should parenthesize each substituted operand and the full expression. Even a parenthesized square macro can repeat evaluation when its argument has side effects, so syntactic repair alone does not make every argument safe.

### Question 12. Binary64 spacing

Assume IEEE754 binary64 rounding to nearest, ties to even. Let$x=2^{53}$ exactly. What is the result of comparing the floating sum$x+1$ with$x$?

**A.** The sum is greater.

**B.** The sum equals$x$.

**C.** The sum is smaller.

**D.** Every implementation must raise an exception.

**Answer: B.**

At this magnitude adjacent representable values differ by2. The exact integer $2^{53}+1$ is halfway between$x$ and$x+2$. Ties-to-even rounds it to$x$, so the equality comparison is true. This is a rounding effect on a defined specified format, not signed integer overflow and not a universal rule for all floating formats.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: Complement after integer promotion

Assume8-bit `uint8_t`,32-bit two’s-complement `int` and32-bit `unsigned int`. For `uint8_t x=128; unsigned int y=~x;`, what are$y$ and `(uint8_t)~x`?

**A.** (127,127)

**B.** (4294967167,127)

**C.** (4294967167,255)

**D.** (128,127)

**Answer: B.**

The narrow unsigned$x$ is promoted to signed `int` because all its values fit. Bitwise complement of128 in that specified representation is$-129$. Assignment to unsigned converts it modulo$2^{32}$, giving4294967167. The separate conversion to8-bit unsigned gives$-129\bmod256=127$. Complement is performed at the promoted width; applying an8-bit complement first would incorrectly predict$y=127$.

### Question 14. Challenge: Conditional type changes an unselected value

Assume32-bit `int` and `unsigned int`. For `int a=-1; unsigned int b=1;`, what is the value of `(1 ? a : b) < 0` in C17?

**A.** 0

**B.** 1

**C.** Undefined behavior.

**D.** It depends on which branch is selected at runtime.

**Answer: A.**

The conditional operator’s common result type is unsigned because its arithmetic branches have equal-rank signed and unsigned types. The selected value$a$ is converted to unsigned even though the$b$ branch is not evaluated, producing the unsigned maximum. In the comparison, zero is converted to unsigned and the result is false. Short-circuit selection controls evaluation, but it does not remove the unselected branch from type determination.

## Applicable formulas and examination notes

### 1. Promotion before conversion

Determine literal types, apply integer promotions, then apply usual arithmetic conversions. Under32-bit equal-rank signed/unsigned comparison, $-1$ becomes $2^{32}-1$. A destination type does not control intermediate operators.

### 2. Cast timing

`(double)(a/b)` preserves integer-division truncation already performed; `(double)a/b` requests floating division. For3 and2, the results are1.0 and1.5. Place the cast before the operator whose semantics must change.

### 3. Unsigned assignment modulus

Converting an integer to an unsigned destination of$b$ bits gives its residue modulo$2^b$. For8 bits,260 becomes4 and$-1$ becomes255. Intermediate promotion can occur at a wider signed width; distinguish calculation from final storage.

### 4. C remainder identity

For defined signed C17 division, quotient truncates toward zero and remainder satisfies `a == (a/b)*b + a%b`. Thus `-7%3` is-1. A nonnegative modular representative belongs to a different arithmetic convention.

### 5. Bit-test parentheses

Write `(x & mask) == 0` when testing masked bits. `x & mask == 0` parses the equality first. Also distinguish bitwise operators, which operate on bit patterns, from logical operators, which produce0 or1 and may short-circuit.

### 6. Shift legality

Check the promoted left operand, count range and signed representability separately. For32-bit `int`, `1 << 31` is undefined inC17 while `1u << 31` is defined. Right-shifting a negative signed value has implementation-defined semantics in this language version.

### 7. Undefined is not unspecified

Signed overflow and unsequenced modification/access cannot be assigned a finite set of predicted outputs by the language. Unspecified evaluation order can still be defined when operands do not conflict. Classify before tracing.

### 8. Short-circuit protection

For `a && b`, a false left operand suppresses$b$; for `a || b`, a true left operand suppresses$b$. This can guard a pointer access or division. Swapping operand order can remove the protection even if a pure Boolean identity holds mathematically.

### 9. Array versus pointer sizeof

A local fixed array preserves its complete type under `sizeof`; an adjusted array parameter is a pointer. Ten four-byte integers occupy40 bytes, while the pointer size is separately specified. Storage size is independent of the displayed numeric values.

### 10. Macro expansion

Expand replacement text before parsing. `SQ(1+2)` under an unparenthesized macro yields5, not9. Parenthesizing parameters repairs precedence but does not prevent an argument like `i++` from appearing twice.

### 11. Floating integer precision

Binary64 represents every integer through$2^{53}$ exactly, but not every larger integer. Under nearest-even, $2^{53}+1$ rounds to$2^{53}$. Equality tests at this boundary need a format and rounding assumption.

### 12. Defined overflow checks

For signed positive$b$, ensure `a <= MAX-b` before evaluating `a+b`. Checking overflow after the signed operation is too late. Division also requires a nonzero divisor and must exclude the minimum-signed divided by-1 overflow case.

<!-- BOUNDARY-NOTES -->

### 13. Conditional operator type

The conditional expression selects one evaluated branch, but its result type is determined by both branch types under the language rules. A signed value can be converted to unsigned even when the unsigned branch is not selected. Determine the expression type before predicting its stored value.

### 14. Format argument types

A variadic output function requires the argument type expected by its conversion specification. Printing an integer with a floating conversion is not an implicit conversion and can be undefined behavior. Convert the supplied expression to the required type instead.

### 15. Floating tolerance

An absolute tolerance controls error near zero while a relative tolerance scales with magnitude. A combined rule must specify both scales and special-value behavior. One fixed relative test can fail near zero; approximate equality need not be transitive.
