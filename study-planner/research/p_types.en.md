# Data Types, Conversions, and Operators

## Scope, conventions, and reviewed sources

**Programming Fundamentals · Chapter 1 · English review draft.** This chapter teaches how to read an expression as a typed computation, determine its mathematical meaning, and identify the conditions under which that meaning is valid. Read the teaching sections before attempting the problem bank. The final review is a retrieval aid, not a substitute for the derivations.

The primary language is **ISO C17**. Python 3 and Java appear in explicitly labelled comparisons. A rule from one language must never be silently imported into another. Unless a problem states otherwise, numerical machine examples use an eight-bit byte, 32-bit `int` and `unsigned int`, 16-bit `short`, and a two's-complement signed representation. Examples involving `long` state its width separately. These are a declared example model, not universal C guarantees. Floating examples that require exact numerical rounding additionally assume IEEE binary64 `double`, round to nearest with ties to even, and no reassociation or excess intermediate precision.

Five written university course bodies were reviewed for this boundary. Their complementary roles were selected from a bounded seven-offering pool; this is not a claim to have examined every course worldwide. The source audit records access, selection, corrections, and exercise coverage. The original exposition, proofs, diagrams, and new problems below reconcile the course perspectives using the language specification.

| Reviewed university course | Written material and author or instructor | Role in this chapter |
|---|---|---|
| Stanford CS107, Winter 2020 | [Lecture 2](https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/lectures/2/Lecture2.pdf), Jerry Cain and Lisa Yan; relevant slides 78–101 and 109–115 | Signedness, range, conversions, and comparison pitfalls. Machine assumptions in the slides are made explicit here. |
| Harvard CS50x, 2025 | [Lecture 1 notes](https://cs50.harvard.edu/x/2025/notes/1/), David J. Malan; Types, Operators, Variables, More About Operators, and Truncation | A foundation for moving from declarations to numeric expressions. The signed range and overflow statements require corrections. |
| UC Berkeley CS61C course notes | [C Variables](https://notes.cs61c.org/content/c-basics/c-variables/) and [C Syntax](https://notes.cs61c.org/content/c-basics/c-syntax/); course notes maintained by the teaching team | Width portability, initialization, aliases, constants, and macro evaluation. Version-sensitive and inaccurate generalizations are corrected. |
| Princeton COS126 course resources | [Built-in Types of Data, §1.2](https://introcs.cs.princeton.edu/java/12types/), Robert Sedgewick and Kevin Wayne | A precise distinction between values, operations, and expressions, plus a Java comparison and exercise-pattern review. Java overflow and Boolean rules are kept separate. |
| MIT 6.0001, Fall 2016 | [Lecture 1 slides](https://live.ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/e921a690079369751bcce3e34da6c6ee_MIT6_0001F16_Lec1.pdf), Ana Bell; course instructors Ana Bell, Eric Grimson, and John Guttag; slides 23–34 and [three written in-class questions](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/in-class-questions-and-video-solutions/lecture-1/) | Python objects, conversions, expression values, and assignment snapshots. This supplemental course prevents inappropriate transfer of C rules. |

The specification cross-check uses [WG14 N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), the public C11 committee draft, for the cited scalar-expression rules retained in C17. It is a specification reference, not a sixth university course or the published ISO C17 document. Relevant clauses are named alongside the rules. C23 changes are outside the declared language version.

The boundary includes scalar types, names and objects, initialization, literals, arithmetic conversions, every basic scalar operator family, expression parsing, sequencing, integer safety, floating precision, and output-type matching. Detailed encodings belong to the later representation chapter; control-flow statements to the next chapter; functions, pointers, arrays, strings, storage management, and advanced mask algorithms each have their own later chapters. Those boundaries do not remove the prerequisite rules needed to understand an expression here. Archived Iranian examination papers remain deferred to the final month.

## Values, types, objects, and assignment

### A type specifies a domain and permitted operations

A mathematical integer has no fixed maximum. A machine integer type has a finite domain. A floating type represents a finite collection of approximations and special values on implementations that support them. A type therefore answers three questions: which values can exist, which operations are legal, and how the language interprets those operations. The same written operator may have different meanings depending on operand types.

An **object** in C is a region of storage whose contents can represent values. A variable identifier designates an object. A declaration associates that name with a type; a definition provides its object; an initializer supplies an initial value. In the ordinary local definitions used here, these actions occur together:

```c
int count = 12;
double rate = 0.75;
unsigned int flags = 0U;
```

`count` is a name, `int` is its declared type, and `12` is the current value. A value is not the same as its printed spelling or bit pattern. The characters `"12"` form a string literal; they do not constitute the numeric integer constant `12`. The ordinary character constant `'2'` is an integer code for a character, not the number two. In C, an ordinary character constant has type `int`, even when assigned into a `char` object.

An **expression** computes a value, designates an object, creates a side effect, or combines these purposes. A statement directs execution. The expression `count + 1` computes a value without changing `count`. The assignment expression `count = count + 1` computes a new value and stores it. Adding the semicolon makes it an expression statement.

### Assignment is a state transition

Let σ denote the current association between variable names and values. For a well-defined expression E, let value(E, σ) denote its result in that state. Assignment to a variable x has the conceptual effect:

<div class="formula-block formula-steps"><div>v = value(E, σ)</div><div>σ′ = σ[x ↦ convert(v, type(x))]</div></div>

This is a model for reasoning, not a replacement for C's rules about evaluation order or side effects inside E. The crucial point is that the right-hand expression is evaluated using the relevant current values; the result is then converted for storage. A previously assigned result does not update automatically when an input variable changes.

```c
int left = 7;
int right = 4;
int total = left + right;
left = 20;
```

The final values are `left = 20`, `right = 4`, and `total = 11`. The value eleven was stored earlier. There is no permanent algebraic equation linking the objects. In mathematics, x = x + 1 has no solution over ordinary integers. In programming, `x = x + 1` is a valid state transition when the addition is representable.

Python makes a name refer to an object and permits rebinding it to an object of another type. C does not change a variable's declared type after declaration. Both languages nevertheless have the same snapshot issue: assigning the current value of an expression does not install a spreadsheet-style dependency.

### Lvalues and modifiability

An **lvalue** is an expression designating an object. A **modifiable lvalue** may be the target of assignment. The variable `count` is one; `count + 1` is a computed result and cannot be assigned to. A `const`-qualified object's value cannot be modified through the ordinary assignment operators. In C, an assignment result and a cast result are not lvalues. Thus `a = b = 5` is valid, while `(a = b) = 5` violates the assignment constraint.

```c
int a = 0, b = 0;
a = b = 5;             // parsed as a = (b = 5)
const int limit = 100; // an initialized const-qualified object
// limit = 101;        // invalid: not a modifiable lvalue
```

`const` does not generally make an object an integer constant expression in C17. `const int n = 4;` is an object definition; an enumeration constant such as `enum { N = 4 };` is suitable for contexts requiring an integer constant expression. `typedef` provides an alias, not a new distinct integer type: `typedef unsigned int Counter;` gives a second name for the same type.

### Initialization is a semantic requirement

An automatic local scalar without an initializer has an indeterminate value. Evaluating an ordinary uninitialized automatic `int` is not a legitimate way to obtain a random number and can have undefined behavior. An object with static storage duration and no explicit initializer receives the language's zero initialization. The word “garbage” is inadequate because it conceals both the different storage-duration rules and the absence of a portable result.

```c
static int saved; // zero initialized
int main(void) {
    int local;   // indeterminate: do not evaluate its value
    int valid = 0;
    return saved + valid;
}
```

Scope and lifetime are developed later. For this chapter, trace a value only after a valid initialization or assignment; an earlier declaration by itself is not proof that the object contains a usable value.

## Scalar types, ranges, and literal typing

### The type families

C has integer types, real floating types, complex types, and pointer types among its scalar types. This chapter concentrates on integers and real floating arithmetic. `_Bool`, plain `char`, `signed char`, `unsigned char`, `short`, `int`, `long`, and `long long`, with the relevant unsigned variants, support integer reasoning. `float`, `double`, and `long double` support real floating arithmetic. `void` signifies absence of a value in relevant contexts; it is not a numeric storage type.

`bool`, `true`, and `false` in C17 normally come from `<stdbool.h>` and refer to `_Bool`, one, and zero. `string` in CS50 is a library alias, not an ISO C built-in type. Plain `char`, `signed char`, and `unsigned char` are distinct types; plain `char` has either the signed or unsigned range as an implementation choice. Never infer that choice from the English word “character.”

| Type or property | Portable guarantee | Declared example model |
|---|---|---|
| `char` | `sizeof(char)` is one byte; `CHAR_BIT` is at least eight | Eight-bit byte; the signedness of plain `char` must still be stated |
| `int` | It includes at least −32767 through 32767 | −2147483648 through 2147483647 |
| `unsigned int` | Zero through `UINT_MAX`, at least 65535 | Zero through 4294967295 |
| `short`, `int`, `long`, `long long` | Their storage sizes are nondecreasing in this order; equal sizes are possible | Usually 16, 32, 32 or 64, and 64 bits; `long` requires a model choice |
| `uint8_t`, `int32_t` | Exact-width aliases are supplied only when suitable types exist | Eight-bit unsigned and 32-bit two's-complement signed types |
| `size_t` | Unsigned integer type returned by `sizeof` | Width depends on the implementation; do not equate it with `unsigned int` |
| `float`, `double`, `long double` | The later type has at least the range and precision of the earlier type | Binary32 and binary64 are common examples, not universal requirements |

For an unsigned integer with w value bits, the domain is:

<div class="formula-block">0 ≤ u ≤ 2<sup>w</sup> − 1.</div>

For the declared two's-complement signed model with w total bits and no padding, the domain is:

<div class="formula-block">−2<sup>w−1</sup> ≤ s ≤ 2<sup>w−1</sup> − 1.</div>

There are 2<sup>w</sup> representations in both models. The unsigned domain allocates them to nonnegative values; the signed model allocates half to negative values. The asymmetry explains why negating the minimum signed value cannot produce a representable positive value. C17 also permits other signed representations; the formula for that signed example must not be presented as an unconditional C17 rule. Exact-width `intN_t` types, when supplied, carry stricter representation requirements.

The fact that a machine or operating system is described as 64-bit does not imply 64-bit `int`. The common LP64 model has 64-bit `long`; Windows LLP64 has 32-bit `long` and 64-bit pointers and `long long`. Verify the relevant limits with `<limits.h>` and precision with `<float.h>` instead of guessing from the platform label.

### Literals have types before assignment

For an unsuffixed decimal integer constant, C tries `int`, then `long`, then `long long`, selecting the first type that can hold the value. For an unsuffixed octal or hexadecimal constant, it interleaves signed and unsigned candidates: `int`, `unsigned int`, `long`, `unsigned long`, `long long`, `unsigned long long`. The base therefore can affect the type even when the mathematical value is the same. Suffixes such as `U`, `L`, and `ULL` select the applicable candidate list. See N1570 §6.4.4.1.

Under a 32-bit `int` model, `2147483648` is not an `int`; it becomes `long` on LP64 or typically `long long` on LLP64. In contrast, `0x80000000` fits `unsigned int`, so that is its type. The expression `-2147483648` consists of unary minus applied to the positive literal. The minus sign is not part of an integer literal token. Use `INT_MIN` when the purpose is the minimum of the actual implementation's `int` type.

An initial zero denotes octal in C17: `010` means eight. `0x10` means sixteen. A `0b` binary literal is not part of ISO C17, even though some compilers accept it as an extension. A floating constant such as `2.5` or `1e3` normally has type `double`; `2.5f` has type `float`, and `2.5L` has type `long double`. Hexadecimal floating constants such as `0x1.8p1` are allowed and mean three. The exponent marker is `p` because the exponent scales by powers of two.

Character codes require their own assumptions. C guarantees contiguous codes for the decimal digits, so `c - '0'` converts a character known to be a decimal digit to its value. It does not guarantee that letter codes are ASCII or that all alphabetic letters are contiguous. Strings, Unicode encodings, escape sequences, and representation layouts are taught later.

### `sizeof` measures storage, not numeric magnitude

`sizeof` is an operator whose result has type `size_t`; it reports a size in C bytes. It does not report a maximum value or evaluate an ordinary non-VLA operand. For `int i = 3;`, `sizeof(i++)` gives the size of `int` and leaves `i` at three. The operator still checks the expression's type and constraints. Variable-length-array types are an important exception: their size can depend on run-time evaluation. This chapter uses fixed-size operands; it does not pretend the exception is absent.

## Conversions: the complete reasoning pipeline

### Conversion changes a typed value

A conversion can preserve a mathematical value, change it by truncation or reduction, or lose information. It is not generally a reinterpretation of unchanged bytes. For instance, converting integer seven to `double` creates the floating value seven; its floating representation is different from the integer representation. An explicit cast and an implicit conversion invoke the same applicable numeric conversion rules. A cast documents a request; it does not grant immunity from undefined behavior.

The conceptual pipeline for a binary arithmetic expression followed by assignment is:

<figure class="type-diagram"><svg viewBox="0 0 780 230" role="img" aria-label="Four stages: obtain operand values, promote and choose a common type, perform the operation, and convert for storage"><g fill="#eef5f8" stroke="#7399b0"><rect x="15" y="25" width="350" height="70" rx="10"/><rect x="415" y="25" width="350" height="70" rx="10"/><rect x="415" y="145" width="350" height="70" rx="10"/><rect x="15" y="145" width="350" height="70" rx="10"/></g><g fill="#213c50" font-size="18" text-anchor="middle"><text x="190" y="54">1. Read values and declared types</text><text x="190" y="80">The destination does not decide the operation</text><text x="590" y="54">2. Promote; choose the common type</text><text x="590" y="80">Check rank, signedness, and range</text><text x="590" y="174">3. Compute in the expression type</text><text x="590" y="200">Check overflow and operator conditions</text><text x="190" y="174">4. Convert the result for storage</text><text x="190" y="200">Information may be lost here too</text></g><g stroke="#326d8c" stroke-width="3" fill="none"><path d="M365 60H400l-10 -6m10 6l-10 6"/><path d="M590 95V130l-6 -10m6 10l6 -10"/><path d="M415 180H380l10 -6m-10 6l10 6"/></g></svg><figcaption>Type the intermediate expression before consulting the receiving variable. Shifts and logical operators have their own conversion rules.</figcaption></figure>

### Integer conversion to unsigned: a congruence proof

For an integer value z converted to an unsigned type with modulus M = 2<sup>w</sup>, the unique resulting value u satisfies:

<div class="formula-block formula-steps"><div>u ≡ z (mod M),</div><div>0 ≤ u &lt; M.</div></div>

Existence follows from division with remainder: z = qM + u for some integer q and a remainder u in the stated interval. Uniqueness follows because two such remainders differ by a multiple of M but have absolute difference smaller than M, so their difference is zero. This proof works for negative z as well. In an eight-bit unsigned destination, converting −1 gives 255 because −1 = −1·256 + 255. Converting 300 gives 44 because 300 = 1·256 + 44.

This is a rule for **integer-to-unsigned conversion**. It must not be applied to an out-of-range floating-to-unsigned conversion. Converting the floating value −1.0 to an unsigned type is not made valid by a modulo argument.

For conversion to a signed destination, a representable value is preserved. If an integer value is outside the signed destination's range, C17 specifies an implementation-defined result or an implementation-defined signal. This differs from signed arithmetic overflow, which has undefined behavior. With two's-complement hardware, a common implementation discards upper bits when narrowing, but the language-level classification must still be stated.

### Integer promotions happen before many operators

`_Bool`, `char`, and integer types of rank below `int` are promoted when the operator requires it. If `int` represents every value of the original type, the promotion yields `int`; otherwise it yields `unsigned int`. This preserves the value. In the usual 32-bit `int`, eight-bit character model, both signed and unsigned characters promote to `int`.

```c
unsigned char a = 240;
unsigned char b = 20;
int total = a + b;            // int result: 260
unsigned char stored = a + b; // storage conversion: 4
```

The operands' small storage width does not force small-width arithmetic. The addition computes 260 in `int`; the destination conversion subsequently reduces it modulo 256. The difference matters for multiplication too: two promoted 16-bit unsigned shorts can multiply in 32-bit signed `int` and overflow it, even though their original storage types are unsigned.

Promotions apply to unary `+`, unary `-`, `~`, both shift operands, and the integer stages of usual arithmetic conversions. They also occur in default argument promotions. They do not mean that every stored `float` automatically becomes `double` in every expression: `float + float` has type `float` under the usual arithmetic conversions.

### Usual arithmetic conversions: use the decision tree

For the real arithmetic types considered here, most binary arithmetic, arithmetic comparison, equality, and bitwise binary operations choose a common type. The conditional operator also uses this rule to determine its arithmetic result type. N1570 §6.3.1.8 gives the following procedure:

1. If either operand is `long double`, convert the other to `long double`.
2. Otherwise, if either is `double`, use `double`.
3. Otherwise, if either is `float`, use `float`.
4. Otherwise, perform integer promotions.
5. If the promoted types agree, stop. If they have the same signedness, use the type with higher integer conversion rank.
6. If the unsigned type has rank at least that of the signed type, convert the signed operand to the unsigned type.
7. Otherwise, if the signed type represents all values of the unsigned type, use the signed type.
8. Otherwise, use the unsigned counterpart of the higher-rank signed type.

Rank is not merely storage size. The rank order is `signed char`, `short`, `int`, `long`, `long long`, even when adjacent types occupy the same number of bytes. An unsigned counterpart has the same rank as its signed type. The final range test is essential.

`-1 < 1U` is false in the declared model: the equal-rank signed operand becomes `unsigned int`, yielding 4294967295, and that is not less than one. `-1L < 1U` is true in LP64 because 64-bit signed `long` represents the entire unsigned 32-bit range. The same source expression is false in LLP64 because 32-bit signed `long` cannot do so, and the common type becomes `unsigned long`. The rule is deterministic once the model is known.

Comparisons have an important extra step: their operands may be converted to an unsigned or floating common type, but the **result** is `int` zero or one in C17. Calling a comparison's result “unsigned” because the comparison used unsigned operands confuses operand interpretation with result type.

### Floating conversions and the timing of casts

For a finite floating value converted to an integer, discard the fractional part toward zero. Both `3.9` and `-3.9` therefore convert to three and negative three respectively. The resulting integral value must be representable in the destination; otherwise the behavior is undefined. This includes a finite value outside the integer range. NaNs and infinities also do not provide a portable valid integer conversion.

For integer-to-floating conversion, an exactly representable value is preserved. If the value lies in range but is not exactly representable, the nearby result follows the implementation's specified conversion behavior; the declared binary64 examples use round-to-nearest-even. A larger range does not imply exact representation of every integer. In binary64 all integers through 2<sup>53</sup> are exactly representable, but the immediately following integer is not.

Compare these expressions for positive integers seven and four:

```c
double first = 7 / 4;          // int division, then conversion: 1.0
double second = (double)(7/4); // same loss before the cast: 1.0
double third = (double)7 / 4;  // double division: 1.75
```

The destination type cannot reach backward and change an operation already specified by operand types. A cast after an integer product likewise cannot repair overflow that happened in that product. If a wider type is sufficient, convert an operand before multiplication, and prove that the widened result fits.

## Operators, parsing, and mathematical translation

### Build a syntax tree before evaluating values

Precedence determines which operators bind their operands. Associativity determines grouping among operators at the same precedence. Neither, by itself, specifies when operands with side effects are evaluated. This distinction is developed in the sequencing section.

| Binding level, highest first | Operator family | Grouping |
|---|---|---|
| Postfix | Calls, indexing, member access, postfix `++` and `--` | Left |
| Unary and casts | Prefix `++` and `--`, unary `+ - ! ~`, address/indirection, `sizeof`, casts | Right |
| Multiplicative | `* / %` | Left |
| Additive | `+ -` | Left |
| Shift | `<< >>` | Left |
| Relational | `< <= > >=` | Left |
| Equality | `== !=` | Left |
| Bitwise AND | `&` | Left |
| Bitwise XOR | `^` | Left |
| Bitwise OR | `\|` | Left |
| Logical AND | `&&` | Left |
| Logical OR | `\|\|` | Left |
| Conditional | `?:` | Right; its middle expression is parsed with special grammar |
| Assignment | `= += -= *= /= %= <<= >>= &= ^= \|=` | Right |
| Comma operator | `,` | Left |

Use this table as a parsing aid; exact syntactic constraints still apply. For example, a left assignment operand must be suitable, and a conditional middle operand is treated as an expression, not simply restricted by the surrounding table. Parentheses make the intended tree explicit, but they do not create a sequencing guarantee for otherwise unsequenced arithmetic operands.

The expression `a + b * c` has an addition root with multiplication as its right child. For values two, three, and four, its result is fourteen. `(a + b) * c` has a multiplication root and produces twenty. The altered tree changes the operation dependencies.

<figure class="type-diagram"><svg viewBox="0 0 650 230" role="img" aria-label="Two expression trees compare a plus b times c with parenthesized a plus b times c"><g stroke="#7399b0" stroke-width="2"><path d="M155 45L75 115M155 45L235 115M235 115L195 195M235 115L285 195M495 45L415 115M495 45L575 115M415 115L365 195M415 115L455 195"/></g><g fill="#eef5f8" stroke="#7399b0"><circle cx="155" cy="45" r="23"/><circle cx="235" cy="115" r="23"/><circle cx="495" cy="45" r="23"/><circle cx="415" cy="115" r="23"/></g><g fill="#213c50" font-size="24" text-anchor="middle" font-family="STIX Two Math"><text x="155" y="53">+</text><text x="75" y="123">a</text><text x="235" y="123">×</text><text x="195" y="203">b</text><text x="285" y="203">c</text><text x="495" y="53">×</text><text x="415" y="123">+</text><text x="575" y="123">c</text><text x="365" y="203">a</text><text x="455" y="203">b</text></g></svg><figcaption>The left tree represents addition after forming the product. The right tree represents multiplication after forming the sum. The tree alone does not order independent side effects.</figcaption></figure>

### Arithmetic and remainder

After conversions, `+`, `-`, and `*` perform addition, subtraction, and multiplication subject to the result type's rules. `/` performs integer division if both converted operands are integers; otherwise it performs floating division. `%` requires integer operands in C. It is not a percent-of operator and does not accept `double` operands.

For integer division, let a be the dividend and b the nonzero divisor. If the quotient is representable, C17 computes q by truncating the rational a/b toward zero, and the remainder r satisfies:

<div class="formula-block formula-steps"><div>a = bq + r,</div><div>|r| &lt; |b|.</div></div>

A nonzero remainder has the dividend's sign. To derive this, first divide the magnitudes using nonnegative quotient and remainder. Reattach the quotient's sign according to the operand signs. The amount subtracted from the dividend then has magnitude no larger than the dividend, and the residual retains its sign. For −17 divided by five, q = −3 and r = −2 because −17 = 5(−3) − 2. For seventeen divided by negative five, q = −3 and r = 2.

Python `//` instead rounds downward, giving `-17 // 5 == -4` and `-17 % 5 == 3`. Both languages maintain their quotient–remainder identity, but with different quotient rules. C's `%` can be negative; a mathematical nonnegative residue for a positive modulus needs an explicit correction.

For nonnegative integer n and positive integer d, a ceiling quotient can be computed safely as:

<div class="formula-block"><math display="block"><mrow><mo>⌈</mo><mfrac><mi>n</mi><mi>d</mi></mfrac><mo>⌉</mo><mo>=</mo><mo>⌊</mo><mfrac><mi>n</mi><mi>d</mi></mfrac><mo>⌋</mo><mo>+</mo><mo>[</mo><mi>n</mi><mo>mod</mo><mi>d</mi><mo>≠</mo><mn>0</mn><mo>]</mo></mrow></math></div>

The brackets denote an indicator equal to one when the condition holds. Euclidean division gives n = dq + r with 0 ≤ r &lt; d. If r is zero, n/d is q; otherwise its ceiling is q + 1. This derivation avoids the overflow-prone expression `(n + d - 1) / d`. In C, `n/d + (n%d != 0)` realizes the indicator directly when its types and domain conditions are valid.

### Equality, comparisons, and truth

`=` stores a value; `==` compares two values. `!=` tests inequality. `<`, `<=`, `>`, and `>=` compare ordered real arithmetic values after the required conversions. A chain such as `2 < x < 8` means `(2 < x) < 8`, so its first comparison produces zero or one, both less than eight. Use `2 < x && x < 8` for the intended interval.

C conditions consider a scalar value false when it compares equal to zero, and true otherwise. Negative integers are true. `_Bool` conversion stores exactly zero or one. Logical `!` returns one for a false operand and zero for a true operand. `&&` and `||` similarly return an `int` zero or one; they do not return one of their original operands as Python's `and` and `or` can.

| Left truth | Right truth | `&&` | `\|\|` | Exclusive truth difference |
|---|---|---|---|---|
| False | False | 0 | 0 | 0 |
| False | True | 0 | 1 | 1 |
| True | False | 0 | 1 | 1 |
| True | True | 1 | 1 | 0 |

C has no distinct logical XOR token. For arbitrary scalar integers, compare normalized truth values: `!!a != !!b`. `a ^ b` computes a bitwise XOR and can differ from Boolean XOR unless the operands are already normalized. The negation `!a` normalizes truth, while `~a` complements bits after promotion; these are different operations.

### Bitwise operators and shifts

The integer operators `&`, `|`, and `^` combine corresponding bits as AND, inclusive OR, and exclusive OR. Unary `~` complements each bit of the promoted operand. Binary bitwise operators use usual arithmetic conversions; unary complement uses integer promotion. For unsigned u with modulus M, `~u` has value M − 1 − u. This follows because each complemented value bit adds the contribution missing from an all-one pattern.

For unsigned 32-bit values twelve and ten, the low patterns are `1100` and `1010`: AND gives eight (`1000`), OR gives fourteen (`1110`), and XOR gives six (`0110`). `^` never means exponentiation in C. Multiplying a value by itself or calling a mathematical power function is necessary for powers, subject to the applicable overflow or precision analysis.

Shifts promote each operand **individually**. The result has the promoted left operand's type. They do not choose a common type using the usual arithmetic conversions. If the promoted left width is w, the shift count k must satisfy 0 ≤ k &lt; w. A negative count or a count at least w gives undefined behavior, even for a zero left operand.

For unsigned u and a valid count, the left shift computes u·2<sup>k</sup> modulo 2<sup>w</sup>, and the right shift computes ⌊u/2<sup>k</sup>⌋. For a signed nonnegative value, left shift is valid only when the mathematical product fits the result type. Signed negative left shift is undefined in C17. Signed negative right shift is implementation-defined; arithmetic right shift is common, but must not be assumed as a universal language guarantee.

An eight-bit `unsigned char` promoted to 32-bit `int` can be shifted by eight; the relevant width is 32, not eight. Conversely, storing the result into an eight-bit destination can then discard its value modulo 256. Advanced masks and encodings belong to their later chapters, but these promotion and shift preconditions already apply here.

## Sequencing, short-circuiting, and state changes

### Precedence is not execution order

In `f() + g() * h()`, the multiplication groups more tightly than addition. C17 does not generally prescribe the order in which those independent calls are evaluated. A compiler may choose allowable orders. If there are no interacting side effects and all operations are valid, the grouping still determines the numeric result.

Three terms must be separated. **Sequenced before** establishes that one evaluation finishes before another. **Indeterminately sequenced** guarantees one precedes the other without specifying which. **Unsequenced** establishes neither ordering. The distinction becomes decisive when the same scalar object is modified or read in conflicting evaluations. N1570 §6.5 paragraph 2 makes an unsequenced modification relative to another modification or a value computation using the same object undefined.

```c
int i = 3;
int a = i++;   // a becomes 3; i becomes 4 before the next full expression
int b = ++i;   // i becomes 5; b becomes 5
// int c = i++ + i; // undefined: conflicting unsequenced evaluations
```

Postfix increment yields the old value and causes an update; prefix increment yields the new value. The value computation of a postfix increment precedes its update, but “postfix” does not mean “wait until the entire program line is finished before doing anything.” What matters is the language's sequencing relation. Separate full expressions, such as successive ordinary statements, provide the clear ordering used in the valid trace above.

`i = i + 1` is valid because the assignment update occurs after the value computations needed to determine it. `i = i++` is undefined in C17 because the postfix update and the assignment update are not ordered appropriately. Parentheses around the postfix expression do not repair the conflict. The same warning applies to `printf("%d %d", i++, i++)`: commas separating function arguments are not sequencing operators.

### Short-circuiting is a semantic protection

For `A && B`, evaluate A first. If it is false, do not evaluate B; the result is zero. Otherwise evaluate B after A's relevant effects and normalize its truth. For `A || B`, skip B when A is true. These rules allow a guard to establish the preconditions of a later operation.

```c
int divisor = 0;
int numerator = 12;
int allowed = divisor != 0 && numerator / divisor > 2;
```

The left operand is false, so the division is not evaluated and `allowed` is zero. Reversing the operands would evaluate division first. Replacing `&&` with `&` loses the short-circuit guarantee and requires both integer operands. A valid guard must establish every relevant condition: a nonzero divisor does not by itself protect the two's-complement minimum signed integer divided by negative one.

De Morgan's laws describe normalized logical values. With state-changing operands, algebraically reordering terms can change observable effects or remove a precondition guard. Preserve operand order and the intended guarded domain when transforming a Boolean expression. The truth table alone cannot justify every program rewrite.

### Conditional, assignment, and comma operators

In `condition ? yes : no`, evaluate the condition and then only the selected branch. The arithmetic result type is nevertheless determined from both branch types. In `1 ? -1 : 1U`, the selected value negative one is converted to `unsigned int`, giving `UINT_MAX`. The unselected branch contributes to type determination without being evaluated. A bad operation confined to an unselected branch is not executed, but both branches still must satisfy syntax and type constraints.

Simple assignment converts the right operand to the target's type. Compound assignment, such as `x += y`, computes the applicable operation and stores its converted result, evaluating the left target expression only once. It is therefore not universally interchangeable with a textual expansion that duplicates a complex left expression.

For `unsigned char x = 250; x += 10;`, the addition uses promoted `int` operands and computes 260; conversion back to the target stores four in the eight-bit byte model. For `int x = INT_MAX; x += 1;`, the signed operation overflows and is undefined. The shorthand does not alter overflow policy.

The comma **operator** evaluates its left operand, completes the required effects, then evaluates its right operand; the result has the right operand's type and value. `int answer = (i++, i);` is defined for a representable increment and stores the updated value. A comma between separate arguments or declarators is punctuation with a different grammatical role. Parse the code before assigning the comma operator's guarantee.

### Macros can repeat evaluation

A function-like preprocessor macro expands tokens. Parenthesizing arguments protects grouping but does not ensure one evaluation. Consider `#define MIN(a,b) ((a) < (b) ? (a) : (b))`. Passing expressions with effects can evaluate one argument in the comparison and again in the selected branch. If two effects occur unsequenced in the comparison, the result may already be undefined. With effect-free local variables, the expression behaves as the intended minimum.

There are two separate repairs: parenthesize each occurrence and the whole expansion to fix parsing; avoid effectful repeated arguments or use a properly typed function to fix repeated evaluation. The latter topic is developed in the functions chapter. A correct syntax tree does not prove a macro safe.

## Integer safety and behavior classification

### Four classifications before output prediction

| Classification | Meaning | Example within this chapter |
|---|---|---|
| Defined under stated assumptions | The rules and model determine the result | Unsigned wrap; representable signed addition |
| Implementation-defined | The implementation must document its chosen behavior | Out-of-range integer-to-signed conversion; negative signed right shift; plain `char` signedness |
| Unspecified | Several choices are permitted without requiring a documented choice for each occurrence | The order of independent arithmetic operands or independent call arguments |
| Undefined behavior | The language imposes no result requirement for the offending execution | Signed arithmetic overflow, integer division by zero, invalid shift count, conflicting unsequenced updates |

A constraint violation is an additional category: the implementation must issue a diagnostic for a syntax or constraint error in a translation unit, such as applying integer `%` to `double` operands. A diagnostic is not an output. If a compiler accepts such code as an extension, its extension behavior does not become an ISO C17 rule.

An observed output from an undefined program proves no portable result. Likewise, wrapping on two's-complement hardware does not make signed overflow valid C. The language's abstract machine determines which assumptions an optimizer may use. For example, `x + 1 > x` holds on every execution where a signed addition is representable; this does not license computing `INT_MAX + 1` to “test” the maximum.

### Unsigned arithmetic has a mathematical model

For unsigned type modulus M, addition, subtraction, and multiplication reduce the mathematical result to its unique residue in [0, M). Congruence is preserved by these operations, so an unsigned expression consisting of these operations can be analysed in the ring of residues modulo M. Its order comparisons do not inherit ordinary integer ordering across wrap.

For example, with an eight-bit unsigned arithmetic model, 250 + 10 gives four. Thus adding a positive value can produce a smaller stored residue. A wrap detector for an actual unsigned addition `sum = a + b` can use `sum < a`. To prove it, if a + b &lt; M then sum = a + b ≥ a. If a + b ≥ M, the inputs are each less than M, so sum = a + b − M &lt; a. This proof applies to the **type in which the addition occurs**, not automatically to a promoted `unsigned char` expression.

### Check signed addition before performing it

Let L and H denote the signed type's minimum and maximum. To compute a + b safely, the following conditions reject precisely the out-of-range sums:

<div class="formula-block formula-steps"><div>b &gt; 0 and a &gt; H − b: reject.</div><div>b &lt; 0 and a &lt; L − b: reject.</div><div>Otherwise L ≤ a + b ≤ H.</div></div>

When b is positive, H − b is representable; exceeding it is equivalent to exceeding the upper bound after addition. The lower bound cannot fail because adding a positive value increases a. When b is negative, L − b is representable; falling below it is equivalent to falling below the lower bound after addition. The upper bound cannot fail. The test itself does not calculate the dangerous sum.

```c
#include <limits.h>
int safe = !((b > 0 && a > INT_MAX - b)
          || (b < 0 && a < INT_MIN - b));
// Compute a + b only when safe is true.
```

For subtraction a − b, reject if positive b exceeds the available lower margin, `a < INT_MIN + b`, or if negative b makes `a > INT_MAX + b`. These threshold expressions are representable in the corresponding guarded cases. Do not turn subtraction into addition of `-b` without first checking that negation is representable.

For nonnegative a and b, multiplication is safe if b is zero or a ≤ ⌊H/b⌋. The corresponding expression `b == 0 || a <= INT_MAX / b` short-circuits the division. Mixed-sign multiplication requires careful sign cases and the minimum-value exception; a casual absolute-value reduction can overflow. Widening before the operation is sufficient only if the wider type's range provably contains the product.

### Division has a second exceptional boundary

Integer division and remainder require a nonzero divisor and a representable quotient. In the declared two's-complement signed model, `INT_MIN / -1` would produce the unavailable positive magnitude. Both that division and `INT_MIN % -1` are undefined, even though the mathematical remainder would be zero. The representable-quotient condition is part of the language rule, not an optional performance consideration.

The same asymmetry invalidates `-INT_MIN` and `abs(INT_MIN)` when the return type cannot represent the positive magnitude. Use a sufficiently wide representation before negation where available, or devise an unsigned-magnitude conversion with explicit reasoning. The question “what prints?” must first become “is this expression permitted to have a defined result?”

## Floating arithmetic and language boundaries

### Finite precision is not decimal accuracy by default

A binary floating type represents values using a finite significand and exponent range. A rational number has a terminating binary expansion only when its reduced denominator is a power of two. To prove the necessary direction, a finite binary expansion equals an integer divided by a power of two; cancelling common factors leaves no odd denominator factor. Conversely, a denominator that is a power of two can be represented by finitely many binary places. Consequently one eighth terminates; one tenth does not.

The familiar stored binary64 approximation to 0.1 therefore cannot generally equal the exact rational one tenth. Displaying fewer digits does not improve the stored value; it only rounds the textual display. Under the explicitly declared binary64 evaluation model, `0.1 + 0.2 == 0.3` is false. This is an example of approximation and rounding, not a universal rule that every sum of decimal-looking values fails equality.

An operation may round away a small contribution when magnitudes differ substantially. A nonassociativity demonstration under binary64 nearest-even uses a large positive a, its negative, and one:

```c
double a = 1e16;
double left = (a + -a) + 1.0; // 1.0 under the declared model
double right = a + (-a + 1.0); // 0.0 under the declared model
```

The first grouping cancels equal magnitudes before adding one. The second grouping loses the one while combining it with the large negative value, then cancels to zero. Regrouping an expression is therefore not an identity for finite-precision arithmetic even when it is an identity over real numbers. An optimizer mode that allows reassociation changes the assumptions of the example.

### Comparison tolerances need a model

If approximate results are expected, one useful criterion is:

<div class="formula-block">|x − y| ≤ τ<sub>abs</sub> + τ<sub>rel</sub> max(|x|, |y|).</div>

The absolute tolerance addresses values near zero; the relative tolerance scales with magnitude. Both tolerances must come from the problem's accuracy requirement or an error analysis, not an unexplained universal constant. This relation is generally not transitive: three progressively separated values can make adjacent pairs pass while the endpoints fail. It must not silently replace an equivalence relation in an algorithm.

If IEEE special values are supported, positive and negative zero compare equal but may differ in operations that inspect their signs. A NaN is unordered: equality with itself is false, inequality is true, and ordered comparisons are false. In C it converts to true under the scalar-to-`_Bool` rule because it does not compare equal to zero. Infinity and NaN handling for arithmetic depends on the applicable floating implementation rules; baseline C division-by-zero rules must not be replaced with Java's specified outcomes without stating a stronger floating model.

### Output formatting does not convert the supplied type

`printf` is variadic. In its variadic arguments, `float` is promoted to `double` and small integer types undergo integer promotions. The format string tells the function what type and textual representation to expect; it does not retroactively change an incompatible supplied argument to that type.

```c
#include <stdio.h>
#include <stddef.h>
int count = 12;
double ratio = 1.75;
printf("%d %.2f %zu\n", count, ratio, sizeof count);
```

Use `%d` for `int`, `%u` for `unsigned int`, `%ld` for `long`, `%lld` for `long long`, `%zu` for `size_t`, and `%f` for a `double` argument to `printf`. A `long double` requires `%Lf`. Exact-width integers have portable macros in `<inttypes.h>` because their underlying standard integer type may differ across implementations. A mismatched `printf("%d", 1.5)` has undefined behavior; it is not a truncating conversion. Input-format pointer requirements are a separate topic and must not be inferred from these output rules.

### A compact cross-language comparison

| Feature | C17 | Python 3 | Java |
|---|---|---|---|
| Integer size | Finite implementation-dependent types | Ordinary `int` has arbitrary precision subject to resources | `int` is 32-bit; `long` is 64-bit |
| Integer division | `/` truncates toward zero | `/` produces a floating result; `//` floors | Integer `/` truncates toward zero |
| Integer overflow | Signed overflow is undefined; unsigned arithmetic reduces modulo its range | Arbitrary-precision arithmetic avoids fixed-width integer overflow | Ordinary `int` and `long` arithmetic wrap within their widths |
| Truth operands | Scalar zero is false; logical results are `int` zero or one | Truth testing includes more object types; `and` and `or` can return operands | `&&` and `\|\|` require Boolean operands |
| Chained comparison | Repeated binary comparisons of zero/one results | `a < b < c` has comparison-chain semantics | A numeric comparison chain usually fails type checking |
| Exponentiation | `^` is integer XOR; multiply or use a power function | `**` is exponentiation | `^` is XOR; use multiplication or `Math.pow` |

For the Java comparison, this chapter follows the named Princeton material's ordinary primitive operations, not Java library methods designed to detect overflow. For Python, the stated major version matters; Python 2's integer division and old `int`/`long` distinction do not apply here. CMU's C0 arithmetic is also distinct from C17 and is not used as a C17 authority.

## Conversion and division laboratory

The laboratory shows **typed stages**. It uses exact integer arithmetic for the unsigned storage demonstration and explicitly truncates the division model toward zero for the C comparison. It does not compile arbitrary C, model pointers, simulate undefined executions, or reproduce every platform's floating rounding rules. Select a case, adjust the inputs, and read both the result and its explanation. The lesson remains readable without JavaScript; the worked problems contain the same reasoning.

<section class="lab types-lab" aria-label="Typed expression laboratory"><label for="type-case">Expression model</label><select id="type-case"><option value="store">unsigned char addition: promote, add, store</option><option value="divide">C integer division versus Python floor division</option><option value="cast">Cast before versus after integer division</option><option value="compare">int compared with unsigned int</option><option value="guard">Short-circuit division guard</option></select><div class="type-inputs"><label for="type-a">First integer<input id="type-a" type="number" min="-2147483648" max="2147483647" value="250" step="1"></label><label for="type-b">Second integer<input id="type-b" type="number" min="-2147483648" max="2147483647" value="10" step="1"></label></div><output id="type-result" aria-live="polite"></output><ol id="type-stages"></ol><p id="type-explanation"></p></section>

For the initial storage example, the intermediate sum is 260 in `int` and the stored byte is four. Switching to division with negative inputs shows why memorizing “discard the remainder” is insufficient: the direction of quotient rounding determines the remainder's sign. A zero divisor is reported as a rejected operation; no fabricated numeric output is produced.
