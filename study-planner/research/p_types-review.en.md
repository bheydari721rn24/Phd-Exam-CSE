## Final review: decision procedures and examination rules

### A seven-step method for an unfamiliar expression

1. **Fix the language and model.** Identify the language version, integer widths and ranges, plain-character signedness, and any floating assumptions the question supplies. If a result depends on omitted implementation choices, state that dependency.
2. **Check validity and initialization.** Confirm that every evaluated variable has a usable value, operator operands satisfy the constraints, and assignment targets are modifiable lvalues.
3. **Parse the expression.** Insert conceptual parentheses using precedence and associativity. Separate the syntax tree from evaluation order; mark short-circuit, conditional, and comma sequencing boundaries.
4. **Annotate every intermediate type.** Type literals first. Apply promotions where required, then the common-type decision tree for applicable operators. For shifts, promote the operands separately.
5. **Establish execution preconditions.** Reject invalid division, signed overflow, invalid shift counts, and unsequenced conflicts before predicting a numeric value. Determine which guarded branches actually execute.
6. **Compute and convert stage by stage.** Apply the correct quotient rule, unsigned residue rule, floating model, and final storage conversion. A receiving type cannot repair an invalid earlier stage.
7. **Report the full conclusion.** State the value, expression type, final stored state, and behavior classification. When printing is involved, verify the promoted argument types against the format requirements.

### Fifty complete examination rules

1. A variable's name, declared type, stored value, and representation are different concepts; identify which one a question is asking about.
2. Assignment stores the current result of an expression, so later changes to its former inputs do not recompute that stored result.
3. C requires a modifiable lvalue as an assignment target; an arithmetic result, cast result, or assignment result cannot serve as that target.
4. Right-associative assignment permits `a=b=c`, but the receiving objects can have different stored values when their conversions differ.
5. An uninitialized automatic scalar must not be treated as a random usable value; static-storage objects follow a different zero-initialization rule.
6. `const` prevents ordinary modification of its object but does not generally create an integer constant expression in C17.
7. `typedef` gives an existing type an additional name; it does not by itself create a different arithmetic conversion rank.
8. One C byte is the size of `char`; it need not be eight bits unless the implementation or question fixes `CHAR_BIT` to eight.
9. C17 `int` represents at least −32767 through 32767; a claim that the only guarantee is eight bits is incorrect.
10. A 64-bit platform label does not determine the width of `int` or `long`; distinguish LP64 from LLP64 when those types interact.
11. Plain `char` has implementation-defined signedness and is a distinct type from both `signed char` and `unsigned char`.
12. Exact-width aliases such as `uint8_t` exist only when the implementation provides a suitable type; state their availability in a machine-specific problem.
13. An ordinary C character constant such as `'7'` has type `int`, while a string literal and a numeric constant have different meanings.
14. The codes for decimal digits are contiguous, so subtracting `'0'` from a known digit works without assuming that all characters use ASCII.
15. An unsuffixed decimal integer literal selects the first fitting signed candidate; an octal or hexadecimal literal can select an unsigned candidate sooner.
16. The leading minus sign is an operator applied to a positive literal, so determine the positive literal's type before analysing the negation.
17. A leading zero denotes an octal integer constant in C17, and binary `0b` spelling requires an extension outside this version's standard grammar.
18. A floating literal normally has type `double`; the `f` and `L` suffixes request `float` and `long double` respectively.
19. `sizeof` returns `size_t` and measures bytes of storage; it does not report a numeric maximum or normally evaluate a fixed-size operand.
20. A variable-length-array size is a relevant exception to the ordinary unevaluated-operand rule for `sizeof`.
21. Integer promotions preserve the value, selecting `int` if it contains the source range and `unsigned int` otherwise.
22. An eight-bit unsigned character usually promotes to signed `int`, so small unsigned storage does not imply unsigned intermediate arithmetic.
23. A small target can reduce an already computed integer during storage even when the intermediate addition itself did not wrap.
24. A representable integer-to-integer conversion preserves value; an integer-to-unsigned conversion outside the destination range selects its modulo representative.
25. An out-of-range integer-to-signed conversion is implementation-defined or signals in C17, whereas signed arithmetic overflow is undefined.
26. A cast performs the applicable conversion rule; it does not generally reinterpret unchanged bits or make an invalid operation safe.
27. Integer conversion rank and storage width are separate properties, so equal-width `int` and `long` still have different ranks.
28. Mixed signed and unsigned arithmetic requires both a rank comparison and, when applicable, a full-range containment test.
29. Arithmetic comparisons may use an unsigned common operand type while still returning `int` zero or one.
30. A cast before division can select floating division; a cast after integer division preserves the already truncated integer quotient.
31. A wider receiving variable or outer cast cannot repair signed overflow in a narrower intermediate product.
32. A finite floating-to-integer conversion truncates toward zero and requires its integral result to fit; the unsigned integer modulo rule does not rescue an out-of-range floating source.
33. Integer division truncates toward zero in C17, so a nonzero remainder follows the dividend's sign rather than the divisor's sign.
34. Division and remainder both reject a zero divisor and a nonrepresentable quotient, including the two's-complement minimum divided by negative one.
35. A ceiling quotient for nonnegative input can use quotient plus a nonzero-remainder indicator, avoiding a potentially overflowing preliminary addition.
36. A nonnegative modular representative can be obtained by adding a positive modulus only when the signed remainder is negative.
37. Precedence and associativity define grouping, while separate sequencing rules determine which side effects precede other evaluations.
38. Parentheses clarify grouping but do not order independent arithmetic operands or repair conflicting unsequenced changes to one object.
39. Postfix increment yields the old value and prefix increment yields the new one; both still require representable arithmetic and valid sequencing.
40. A comma operator sequences its operands, but a comma separating function arguments does not provide that operator's guarantee.
41. `&&` and `||` normalize truth and short-circuit; bitwise `&` and `\|` combine bits without those evaluation guarantees.
42. A guard must precede the dangerous operation and establish every precondition; a later test cannot undo an earlier invalid evaluation.
43. Both arithmetic branches of `?:` contribute to result type even though only one branch is evaluated.
44. A chained comparison in C compares the first comparison's zero-or-one result with the next operand; use two comparisons connected by a logical operator for an interval.
45. Bitwise XOR is not exponentiation, and bitwise complement is not logical negation; normalize truth when computing exclusive truth difference.
46. Shift counts must lie below the promoted left operand's width; signed left-shift representability and negative-right-shift implementation choices require separate checks.
47. A well-parenthesized macro can still evaluate an effectful argument twice, so parsing correctness and evaluation count must be audited independently.
48. A finite binary expansion requires a reduced denominator that is a power of two, and floating range does not imply exact representation of every integer.
49. Finite-precision regrouping can change a result, and a chosen approximate-equality tolerance is generally not a transitive equality relation.
50. A `printf` format describes the required promoted argument type and textual output; it is not a substitute for a numeric conversion.

### Compact failure-to-repair map

| Symptom | Correct diagnosis | Repair with its condition |
|---|---|---|
| A fraction unexpectedly becomes an integer | Integer division occurred before assignment or casting | Convert an operand before `/`; require a nonzero divisor and suitable floating accuracy |
| A supposedly unsigned product is undefined | Small unsigned operands promoted to signed `int` | Choose a suitable unsigned or sufficiently wide expression type before multiplication |
| A negative value appears larger than a positive one | Mixed signed/unsigned conversion changed the operand interpretation | Apply the full common-type tree; avoid unsafe casts used solely to silence a warning |
| A comparison chain always passes | The first comparison yielded zero or one | Express interval membership with two comparisons and `&&` |
| A guard did not prevent a failure | Evaluation occurred before the guard or used a bitwise operator | Place a complete precondition first in a short-circuiting expression |
| An output puzzle has different observed answers | The execution may be undefined or depend on an implementation choice | Classify the behavior before computing output; do not choose a guessed evaluation order |
| A formula differs from its mathematics | Parsing, operand types, overflow, or rounding changed a stage | Draw its expression tree and annotate types and valid ranges at every node |

## References and audit limits

1. Stanford University, CS107, Winter 2020. Jerry Cain and Lisa Yan. *Lecture 2: Bits and Bytes; Integer Representations*, slides 78–101 and 109–115, with earlier representation context consulted. [Lecture PDF](https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/lectures/2/Lecture2.pdf). [Course archive](https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/).
2. Harvard University, CS50x, 2025. David J. Malan. *Lecture 1 notes*: Types, Operators, Variables, logical-operator examples, More About Operators, and Truncation. [Written notes](https://cs50.harvard.edu/x/2025/notes/1/).
3. University of California, Berkeley, CS61C. Course teaching-team notes. *C Variables* and relevant sections of *C Syntax*: aliases, constants/enums, and macros. [C Variables](https://notes.cs61c.org/content/c-basics/c-variables/). [C Syntax](https://notes.cs61c.org/content/c-basics/c-syntax/). Embedded 2020 videos were not needed for the written review; the current notes are not attributed to a sole lecturer without evidence.
4. Princeton University, COS126 course-resource family. Robert Sedgewick and Kevin Wayne. *Introduction to Programming in Java*, §1.2, Built-in Types of Data, including the exercise inventory. [Written chapter](https://introcs.cs.princeton.edu/java/12types/). [Fall 2017 lecture-resource index](https://www.cs.princeton.edu/courses/archive/fall17/cos126/lectures.html).
5. Massachusetts Institute of Technology, 6.0001, Fall 2016. Ana Bell, Eric Grimson, and John Guttag. *Lecture 1*, particularly slides 23–34 and its three written in-class questions. [Course](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/). [Slides](https://live.ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/e921a690079369751bcce3e34da6c6ee_MIT6_0001F16_Lec1.pdf). [Questions](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/pages/in-class-questions-and-video-solutions/lecture-1/).
6. ISO/IEC JTC1/SC22/WG14. *N1570: Committee Draft, April 12, 2011*. Specification cross-check for the scalar rules retained in C17: §§5.2.4.2.1, 6.2.5–6.2.6, 6.3.1.1–6.3.1.8, 6.4.4, 6.5–6.5.17, 6.7.9, and 7.21.6.1. [Public draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).

**Review scope.** These are reviewed in-scope written sections, not claims of full-course transcription. The bounded source survey and corrected source statements are recorded in the project's source audit. The problem bank covers the chapter's reasoning patterns; it does not claim to contain every question in all university offerings. In-scope reasoning from the selected exercises is represented, while whole applications requiring later algorithms, strings, input processing, or advanced mathematics are deferred with their chapter boundaries.

**Accuracy limits.** The mathematical arguments establish their conclusions under the stated domains and model. Numerical and presentation checks supplement those arguments; they do not prove that an unknown future question has been anticipated or that studying alone guarantees an examination result. Language-version changes, implementation choices, and unexplored course material remain explicit limits. The student approved this chapter on 2026-10-02; it is promoted to the finished library.


Student approved this chapter on 2026-10-02 and authorized p_flow.
