## Fully worked problem bank

Each problem gives its assumptions before its solution. The bank includes original questions and independently worded applications of explicitly identified course exercise patterns. It does not reproduce an entire course assignment or any archived Iranian paper. An undefined expression is classified without running it to guess a result. All code uses C17 unless another language is named.

### Problem 1 — Assignment stores a snapshot

**Task.** Trace `int x = 6, y = 9; int z = x + y; x = 2; y = z - x;` and explain whether the final objects satisfy `z == x + y` by a lasting dependency.

**Solution.** First record x = 6 and y = 9. The addition computes fifteen and stores it in z. Reassigning x stores two without recomputing z. Finally `z - x` uses fifteen and two, so y becomes thirteen. The final tuple is (2, 13, 15). It happens to satisfy the equality because the last assignment was constructed from z and x, not because a permanent relationship was installed. Replacing the last statement with `y = 100` would immediately destroy that equality. This distinction prevents treating a program trace as simultaneous algebraic equations. **Pattern:** MIT Lecture 1, Bindings; all numbers and this explanation are original.

### Problem 2 — Copying is not swapping

**Task.** Starting with `int a = 4, b = 11;`, compare `a = b; b = a;` with `int t = a; a = b; b = t;`.

**Solution.** In the first sequence the first statement stores eleven in a, destroying a's old value. The second statement therefore copies eleven into b. Both end at eleven. In the second sequence t first preserves four. Reassigning a to eleven leaves t untouched; the last statement copies four into b. The final pair is (11, 4). The temporary object preserves information that would otherwise be lost. A swap expressed through arithmetic may overflow, while this version does not perform arithmetic. **Pattern:** Princeton §1.2, assignment and swap exercises.

### Problem 3 — Literal base changes type

**Task.** Assume LP64, 32-bit `int`, and 64-bit `long`. Determine the types and values of `010`, `0x10`, `2147483648`, `0x80000000`, and `1.0f + 1.0`.

**Solution.** An initial zero makes `010` octal, so its value is eight and its type is `int`. Hexadecimal `0x10` is sixteen and also fits `int`. The decimal value 2147483648 exceeds `INT_MAX`; the next decimal candidate is signed `long`, which fits it. The hexadecimal value with the same magnitude fits the earlier hexadecimal candidate `unsigned int`. The suffix on `1.0f` creates a `float`, while `1.0` is `double`; usual arithmetic conversions select `double`, and the result is the exact floating value two. Determine each literal's type before considering a destination.

### Problem 4 — Character code is not numeric value

**Task.** With ASCII for this example, find the values and types of `'7'`, `'7' - '0'`, and a `char c = '7';` promoted in `c + 1`.

**Solution.** The character constant `'7'` has type `int` and ASCII value 55. Subtracting the code for `'0'`, which is 48, gives seven in `int`. The `char` object stores 55; with the declared eight-bit character and 32-bit `int` model, its promotion preserves 55 and `c + 1` computes 56 in `int`. That is the code for `'8'` under ASCII, but the expression is still integer arithmetic. The digit subtraction remains valid for decimal digits without assuming ASCII because their codes are contiguous by the C requirements.

### Problem 5 — `sizeof` does not increment this operand

**Task.** For 32-bit `int`, `int i = 7; size_t n = sizeof(i++);`, determine n and i. Would replacing the operand with a variable-length-array type justify the same general rule?

**Solution.** With an eight-bit byte and 32-bit `int`, the fixed-size operand has storage size four bytes. `sizeof` does not evaluate this `i++`, so n is four and i remains seven. The result's type is `size_t`, not `int`. The VLA case requires separate analysis because the size can depend on run-time bounds and relevant evaluation. Therefore “sizeof never evaluates anything” is too broad. This problem illustrates both the ordinary rule and the boundary that prevents an invalid generalization.

### Problem 6 — Promotion before byte storage

**Task.** In the declared model, let `unsigned char a = 250, b = 10; int s = a + b; unsigned char t = a + b;`. Find both values and the expression type.

**Solution.** Every possible value of either byte fits in `int`, so both operands promote to `int`. The mathematical sum 260 is representable in that expression type. Storing into s preserves it. Storing into t converts the already computed integer 260 modulo 256, giving four. The different destinations do not change the intermediate sum's type. The stored tuple is (260, 4). Calling the addition itself “eight-bit wrap” would misidentify the stage at which the reduction occurs.

### Problem 7 — Unary minus of a promoted unsigned byte

**Task.** For `unsigned char c = 1;`, determine the type and value of `-c` and of `(unsigned char)-c` in the declared model.

**Solution.** Unary minus first promotes c to `int`. Its negation is therefore the signed `int` value negative one, which is representable. The outer cast in the second expression converts that integer to an eight-bit unsigned value. Its residue is 255, because −1 ≡ 255 modulo 256. Thus the first expression is `int` negative one; the second is `unsigned char` 255. The operand's stored unsigned type does not bypass promotion.

### Problem 8 — General unsigned conversion

**Task.** Find the residues of −513, −256, −1, 256, and 769 in an eight-bit unsigned destination. Prove one answer without appealing to a machine bit pattern.

**Solution.** The required interval is zero through 255. The residues are respectively 255, zero, 255, zero, and one. For the first value, −513 = (−3)·256 + 255, so 255 lies in the allowed interval and is congruent to the source. Uniqueness of the interval representative proves the result. This calculation is an integer conversion; attempting the same argument for a floating source outside the destination's allowed integral range would be invalid.

### Problem 9 — Equal-rank signed and unsigned comparison

**Task.** Under 32-bit `int`, evaluate `-3 < 2U`, `-3 == (unsigned int)-3`, and `-3 > -4`.

**Solution.** The first comparison has equal-rank signed and unsigned operands, so negative three converts to `unsigned int` 4294967293. That is not less than two, and the comparison returns `int` zero. In the equality, both sides compare as `unsigned int` with the same value, so its result is `int` one. The final comparison has two signed `int` operands; negative three is greater than negative four, giving one. Signedness changes operand interpretation; it does not change comparison results into unsigned values. **Pattern:** Stanford CS107 Lecture 2, mixed-type comparisons.

### Problem 10 — The higher-rank signed range test

**Task.** Evaluate `-1L < 1U` on LP64 and LLP64, both with 32-bit `int`. Explain why “unsigned always wins” is incorrect.

**Solution.** `long` outranks `unsigned int` in both models. On LP64 its 64-bit signed range contains all 32-bit unsigned values, so the common type is signed `long`; negative one is less than one. On LLP64, signed `long` is 32-bit and cannot contain the entire unsigned `int` range. The common type becomes `unsigned long`, and negative one converts to its maximum, making the comparison false. The answer is true on LP64 and false on LLP64. Rank decides which range question to ask; range decides whether the higher signed type can prevail.

### Problem 11 — Conditional branches determine type together

**Task.** With 32-bit `int`, determine the value and type of `1 ? -2 : 3U`. Is the unsigned branch evaluated?

**Solution.** The condition one is true, so only the middle branch's value is evaluated. However, the result type is chosen from both arithmetic branch types, `int` and `unsigned int`, yielding `unsigned int`. The selected negative two is converted to that type and becomes 4294967294. The unselected branch is not evaluated. Type determination and dynamic branch evaluation are different stages. Assigning this result to `long long` afterward preserves the large unsigned value rather than restoring negative two.

### Problem 12 — Cast placement in division

**Task.** Compare `double a = 9/4;`, `double b = (double)(9/4);`, and `double c = 9/(double)4;`.

**Solution.** The first two divisions use `int` operands and truncate to two. Conversion of that result yields 2.0, whether requested by assignment or by an explicit outer cast. The third division converts nine to `double` because the other operand is `double`; it computes 2.25. All three are defined, but only the third preserves the fractional quotient. The receiving type and an outer cast are too late to alter the division operator's operand types. **Pattern:** Harvard truncation example and Princeton §1.2 Web Exercise 5.

### Problem 13 — Four signs of quotient and remainder

**Task.** Find `(a/b, a%b)` for the pairs (17, 5), (−17, 5), (17, −5), and (−17, −5), then check the identity.

**Solution.** Truncation toward zero gives the tuples (3, 2), (−3, −2), (−3, 2), and (3, −2). For example, seventeen divided by negative five has quotient negative three; multiplying gives fifteen, leaving positive two. In every case bq + r equals a, and the remainder's absolute value is less than five. Its sign follows the dividend when nonzero, not the divisor. Python floor division for (−17, 5) instead gives (−4, 3), also satisfying its identity with a different quotient rule.

### Problem 14 — Ceiling without dangerous addition

**Task.** For nonnegative `int n` and positive `int d`, show how to compute the number of d-item groups needed, including at `n = INT_MAX`. Explain why `(n+d-1)/d` can fail.

**Solution.** Compute `n/d + (n%d != 0)`. Euclidean division gives n = dq + r. If r is zero, q groups suffice; otherwise one additional group is required. At `INT_MAX` and d = 2, q is 1073741823, r is one, and the result is 1073741824, which fits. The alternative expression would add one to `INT_MAX` before dividing, causing signed overflow. If d is one, the correction is zero, so the safe expression never increments the maximum. This proof addresses the intermediate expression, not merely the final mathematical result.

### Problem 15 — A nonnegative residue from a signed remainder

**Task.** For arbitrary representable integer a and positive representable integer m, compute the representative of a modulo m in zero through m−1 without risking an unnecessary large addition.

**Solution.** First calculate `int r = a % m;`. Positive m excludes the negative-one quotient exception and zero division. If r is negative, add m; otherwise leave it unchanged. In the negative case, −m &lt; r &lt; 0, so zero &lt; r + m &lt; m and the addition fits. For a = −17 and m = 5, the first remainder is −2 and the corrected result is three. `(a % m + m) % m` unnecessarily adds m when the remainder is already nonnegative and can overflow for large m. The conditional correction has a proved range.

### Problem 16 — A wider destination cannot repair multiplication

**Task.** Under 32-bit `int` and at least 64-bit `long long`, analyse `int x = 50000; long long y = x * x;` and give a correct repair.

**Solution.** Both operands are `int`, so the product is computed in `int`. Its mathematical value is 2500000000, greater than 2147483647, so the original execution has undefined behavior. Assignment to `long long` happens after that invalid operation and cannot repair it. Use `long long y = (long long)x * x;`. The common type is now `long long` before multiplication. Its required range contains 2500000000, so the operation and storage are valid. An outer cast `(long long)(x*x)` is still too late. **Pattern:** Princeton §1.2 Web Exercise 6, with C17 classification replacing Java wrapping.

### Problem 17 — Unsigned source operands can overflow signed arithmetic

**Task.** Under 16-bit `unsigned short` and 32-bit `int`, analyse `unsigned short a = 60000, b = 60000; unsigned int p = a*b;`.

**Solution.** `int` represents every value of a 16-bit unsigned short, so both operands promote to `int`. Their product 3600000000 does not fit 32-bit signed `int`. The execution is undefined before storage into the unsigned destination. To obtain a defined unsigned 32-bit product here, convert an operand first: `(unsigned int)a * b`. The other promoted operand then converts to unsigned by the usual conversions, and 3600000000 lies below `UINT_MAX`. Larger inputs in another type might still wrap; the repair's range proof is specific to these source ranges.

### Problem 18 — Derive an addition guard

**Task.** With a = 2147483640 and b = 20 in the 32-bit signed model, apply the chapter's overflow guard. Repeat with a = −2147483640 and b = −20.

**Solution.** For positive b, `INT_MAX - b` is 2147483627. Since a exceeds it, reject the first sum without evaluating the sum. For negative b, `INT_MIN - b` is −2147483628. The second a is smaller than that threshold, so reject the second sum. Both threshold computations are representable. The guards are obtained by solving the appropriate upper- or lower-bound inequality; they do not rely on observing a wrapped result. A post-operation test would already execute undefined arithmetic.

### Problem 19 — Negation, division, remainder, and narrowing are different

**Task.** Classify `-INT_MIN`, `INT_MIN/-1`, `INT_MIN%-1`, and conversion of `UINT_MAX` to `int` in the declared model.

**Solution.** The first three have undefined behavior. Negation and division require the unavailable positive magnitude 2147483648; remainder shares the division's representable-quotient precondition even though its mathematical residue would be zero. The final integer-to-signed conversion is instead implementation-defined or raises an implementation-defined signal in C17. A common implementation yields negative one, but that is not a portable C17 answer. These expressions must not be grouped under a single vague word such as “overflow.”

### Problem 20 — Precedence tree with mixed operations

**Task.** Evaluate `2 + 3 * 4 << 1` and `(2 + 3) * (4 << 1)` for `int` operands. Check every intermediate range.

**Solution.** Multiplication binds before addition, and addition before shifting. The first tree is `(2 + (3*4)) << 1`: multiply to twelve, add to fourteen, then shift the nonnegative representable value to 28. In the second tree the sum is five and the inner shift is eight, so multiplication gives forty. Each value and doubled value fits `int`, and each shift count is within range. Grouping determines the different results; no issue of conflicting side effects arises because the operands are constants.

### Problem 21 — Chained comparisons are not interval membership

**Task.** For `int x = 100;`, evaluate `10 <= x <= 20`, and write the intended test.

**Solution.** Left associativity parses the expression as `(10 <= x) <= 20`. The first comparison yields one, and one is at most twenty, so the expression is true despite x lying outside the intended interval. For any ordinary integer x, the first comparison yields zero or one and the final test still succeeds. The correct expression is `10 <= x && x <= 20`, which is false for one hundred. Both expressions have result type `int`. **Pattern:** Princeton §1.2 Web Exercise 2; C accepts a misleading chain while Java rejects its operand types.

### Problem 22 — Logical and bitwise operations disagree

**Task.** Compare `6 && 3`, `6 & 3`, `6 || 3`, `6 | 3`, `6 ^ 3`, and `!!6 != !!3`.

**Solution.** Six and three are both nonzero, so logical AND and logical OR each return one. Their low binary patterns are `110` and `011`. Bitwise AND gives `010`, which is two; bitwise OR gives `111`, which is seven; XOR gives `101`, which is five. Both normalized truths are one, so logical truth inequality gives zero. A nonzero bitwise XOR is not proof that exactly one operand was truthy. Distinguish numerical bit differences from Boolean differences.

### Problem 23 — A shift uses the promoted left width

**Task.** For `unsigned char c = 1;`, evaluate `c << 8`, `c << 31`, `1U << 31`, and `1U << 32` under the declared model.

**Solution.** c promotes to 32-bit `int`, so the first shift count is valid and its product 256 is representable. The second count is within 32, but the signed product 2147483648 is not representable, so that expression is undefined. The unsigned literal in the third expression has 32-bit unsigned type, and its shift yields 2147483648 with a valid count. The fourth has an invalid count equal to the width, so it is undefined even though the left operand is unsigned. Count validity and result representability are separate checks.

### Problem 24 — Short-circuiting protects a division

**Task.** With `int d = 0, n = 8;`, compare `d != 0 && n/d > 2` with `n/d > 2 && d != 0` and `(d != 0) & (n/d > 2)`.

**Solution.** The first expression evaluates the false left guard and skips the division; its result is zero. The second attempts division first and is undefined. The bitwise AND evaluates both required operands without a short-circuit guarantee, so division by zero is still attempted and undefined. Truth-table similarity cannot replace sequencing semantics. For arbitrary signed inputs, a complete safety guard must also exclude the minimum-integer divided by negative-one case.

### Problem 25 — Defined increment traces

**Task.** Trace `int i=2; int a=i++; int b=++i; int c=(i++,i);`.

**Solution.** The first initializer yields the old value two for a, then completes the update so i is three before the next full expression. Prefix increment raises i to four and yields four for b. In the comma expression, postfix increment's old result is discarded and its update completes before the right operand reads i. Therefore c is five and final i is five. The tuple (a, b, c, i) is (2, 4, 5, 5). All increments are representable, and the comma operator supplies the sequencing needed inside the final expression.

### Problem 26 — Reject a plausible output puzzle

**Task.** For a fresh `int i=2;`, classify separately `i++ + i`, `i = i++`, `printf("%d %d", i++, i++)`, and `(i++, i+1)`.

**Solution.** The first has an unsequenced update and a read of the same object; the second has conflicting unsequenced updates; the third has two unsequenced argument updates, since the separating comma is punctuation. All three are undefined in C17, and assigning an imagined evaluation order does not fix them. The final comma operator completes the update from two to three before computing the right operand, so it is defined and gives four, leaving i at three. These are separate experiments with a fresh initial state, not a combined trace.

### Problem 27 — Macro parentheses do not prevent duplicate effects

**Task.** Let `#define MIN(a,b) ((a)<(b)?(a):(b))`. Starting from `int i=3;`, analyse `int z=MIN(i++,10);` and separately `MIN(i++,i++)`.

**Solution.** The first expansion is `((i++)<(10)?(i++):(10))`. The comparison uses three and increments i to four. The conditional operator sequences that condition before the selected branch. Since three is less than ten, the branch yields four and increments i to five. Thus z is four and final i is five: the execution is defined but not the intended single evaluation. In the second expansion, the condition compares two unsequenced modifications of i and is already undefined. The remedy is to avoid effectful arguments or use a suitable function. **Pattern:** Berkeley C Syntax, macro evaluation; this analysis corrects the claim that a selected argument is always repeated.

### Problem 28 — Binary fractions and exactness

**Task.** Decide whether the reduced rational values 3/8, 1/10, and 7/20 have finite binary expansions. Explain why a `double` can still approximate all three.

**Solution.** Eight is a power of two, so three eighths terminates as binary `0.011`. Ten and twenty have a factor five remaining in their reduced denominators, so neither other fraction terminates in base two. A finite binary format rounds a nonterminating value to a nearby representable number; existence of such an approximation is different from exact equality. Precision and exponent-range conditions still determine whether a particular rational fits exactly in a given format. The argument proves termination, not unlimited storage precision.

### Problem 29 — A lost integer unit at binary64 precision

**Task.** Assume binary64 nearest-even conversions. For the exactly represented integer p = 2<sup>53</sup>, predict converting p + 1 and p + 2 to `double`. Is an integer equality necessarily preserved by conversion?

**Solution.** Around p on the higher-magnitude side, consecutive binary64 values are two units apart. The integer p + 1 is halfway between p and p + 2; ties-to-even chooses p, whose significand endpoint is even. The integer p + 2 is exactly representable and remains p + 2. Thus distinct integers p and p + 1 can become the same floating value. Converting before an equality can lose distinctions. This is a precision limitation within range, not overflow of a floating exponent.

### Problem 30 — Finite-precision associativity fails

**Task.** Under the declared binary64 evaluation model, compare `(a + b) + c` with `a + (b + c)` for a = 10<sup>16</sup>, b = −10<sup>16</sup>, and c = 1.

**Solution.** The first parenthesized sum cancels the equal opposite magnitudes exactly to zero, then adds one, giving one. In the second grouping, the unit is too small to change b after nearest-even rounding at its magnitude. The inner sum rounds to b, and adding a cancels it to zero. The different results arise from rounding at different intermediate nodes. The assumptions exclude excess precision and compiler reassociation; without them, a concrete C execution needs its own model. An exact-real algebra identity cannot justify this finite-precision rewrite.

### Problem 31 — Formatting is not a numeric cast

**Task.** Explain `printf("%d", 2.75)`, `printf("%f", 2.75f)`, and `printf("%zu", sizeof(int))`.

**Solution.** The first supplies `double` where the format requires an `int`, so it is undefined; `%d` does not truncate the argument. In the second, default variadic promotion changes the `float` argument to `double`, matching `%f`. In the third, the unsigned type `size_t` returned by `sizeof` matches `%zu`, regardless of whether its width equals that of an `int`. If the desired result is integer two, explicitly convert the representable finite value with `(int)2.75` and pass that to `%d`.

### Problem 32 — An integrated expression audit

**Task.** Under 32-bit `int`, evaluate `unsigned char c=250; int x=-1; unsigned int u=1U; int r=(c+10>255) && (x<u); unsigned char t=c+10;`.

**Solution.** Promote c to `int`, add ten to obtain 260, and compare it with 255; the first logical operand is one. Because it is true, evaluate the second comparison. The equal-rank unsigned common type converts x to 4294967295, which is not less than u, so the second logical operand is zero. The conjunction gives r = 0. The separate final addition again computes 260 in `int`, then unsigned byte storage gives t = 4. The trace combines promotions, comparison result types, short-circuit choice, and a later storage conversion without any undefined arithmetic.

### Problem 33 — Python file output and rebinding

**Task.** In a Python 3 script, consider `type(8)` followed by `print(4.0-1)`; then `x=4; y=x*3; x=9; print(y)`. Explain what is printed and whether x can later refer to a string.

**Solution.** The bare `type(8)` expression computes a type object but the file execution does not automatically display it. The explicit first print emits `3.0`. The next sequence computes and binds y to twelve before rebinding x to nine; its print emits `12`. Assigning `x="nine"` later is permitted in Python because the name can be rebound to an object of another type. The corresponding C object cannot acquire a new declared type. **Pattern:** MIT Lecture 1, all three written questions: file output, assignment legality, and binding snapshots. In either language, an assignment target must be valid; Python permits `xy=2` as an identifier assignment but not `x*y=2` as an equation-solving request.

### Problem 34 — Formula translation with explicit types

**Task.** A dimensionless ratio is <math><mfrac><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow><mi>d</mi></mfrac></math> for integers a = 5, b = 8, d = 4. Write C code preserving its fractional part. Then explain why `double value = a + b / d;` changes two aspects of the intended computation.

**Solution.** Use `double value = ((double)a + b) / d;`. The early conversion causes the sum and quotient to be computed in `double`; the result is 3.25. The proposed expression instead groups as `a + (b/d)`, because division binds before addition. That division is also integer division, giving two; adding five gives seven, then assignment yields 7.0. Correcting only grouping to `(a+b)/d` still leaves integer division and gives 3.0. Correcting only the destination type solves neither issue. This original problem consolidates the mathematical-translation patterns reviewed in Princeton §1.2.

### Problem 35 — Approximate equality need not be transitive

**Task.** For the rule |x − y| ≤ 0.1 with exact real numbers, use x = 0, y = 0.075, and z = 0.15 to test transitivity. Explain the consequence for replacing equality in a grouping algorithm.

**Solution.** The adjacent distances are both 0.075, which pass the tolerance. The endpoint distance is 0.15, which fails. Thus x can be approximately equal to y and y to z without x being approximately equal to z. Exact equality is transitive; this approximate relation is not. An algorithm that merges equality classes therefore needs a specified clustering policy or a genuine equivalence relation, rather than blindly substituting a tolerance check. The example uses exact reals to show that the issue is inherent in the criterion, not merely binary rounding.

### Problem 36 — A full safety precondition for signed division

**Task.** In the two's-complement `int` model, build a logical condition that permits evaluating `a/b`, including all boundary cases, and trace it for `(INT_MIN,-1)`, `(8,0)`, and `(8,-2)`.

**Solution.** Use `b != 0 && !(a == INT_MIN && b == -1)`. For the first pair, the divisor is nonzero but the inner conjunction is true, so its negation rejects the operation. For the second, the first guard is false and the rest need not establish permission. For the third, the divisor is nonzero and the exceptional pair is absent, so division is allowed and gives negative four. This condition must guard the actual evaluation, for example as the condition selecting an appropriate branch. Computing the quotient earlier and then examining the guard would not protect it.
