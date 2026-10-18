# Functions chapter: independent scoped source refresh

Date: 2026-10-18. Research-only assignment. The app checkout and synced sources were not edited.

## Files and reading distinction

`acquisition.json` records actual fresh bytes, final URLs, SHA-256 identities, page counts and failed requests. Retrieval did not automatically count as reading. The following scopes were subsequently actually read; no worldwide course-exhaustiveness claim is made.

### Stanford CS106B, Winter 2016

Official written handout: https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1164/handouts/1-PassbyReference.pdf

Both pages were reread in text and visually inspected as rendered PNGs. Fresh hash matches the original course register: `5dfbd2aa55697b52e6c43b84ec2c87ee491d236f82acaf37f91a2eaee5f29646`. Date and course identity match. A staff attribution is supported; a named individual author is not established.

The value-parameter and `int&` examples support PF60, PF61 and PF89. Three source simplifications need explicit qualifications: negating the most-negative signed integer can overflow; the value-parameter prose should describe the unchanged caller object rather than an expired parameter's supposed later value; the literal-binding restriction concerns the illustrated non-const lvalue reference, not every C++ reference type. No reference-return lifetime proof is supplied by this short handout, so PF86 requires separate language reasoning. The statement labeling `int` as the function's “return” is more precisely the return type.

### MIT 6.0001, Fall 2016

Official Lecture 4: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/6ba59859535f1566dd57a7279aeba5d1_MIT6_0001F16_Lec4.pdf

All 35 extracted slide texts were read across web-reader responses. Chapter-relevant scope is slides 3–35; introductory context 1–2 was also visible. Only slide images 28 and 31 were freshly visually inspected, including the actual indentation and nested-scope diagram. Other illustration pixels were not newly inspected. Fresh hash matches the register: `eac916af74cd039a9f1a85a611e1ef5776a14e1ae0f4a0e6b3fccbcb2e782530`.

The source supplies decomposition, scope, return/print, callback and nested-call comparisons. Historical print-statement examples require Python 3 syntax adaptation. An implicit return supplies `None`; it does not return a previous printed value. A return exits its current invocation; broader exceptions/finally behavior is outside this introductory simplification. Claims about inability to modify outside variables must distinguish rebinding from mutation, plus explicit global/nonlocal declarations. The nested example's `h` has its own local string binding while `g` retains its separate integer binding.

### Official Python documentation

The web reader returned Python 3.15.0 documentation updated 18 October 2026. The reviewed ordinary-function rules also apply to the printed chapter examples; execution below uses the locally installed interpreter recorded in `python-checks.json`. Direct byte retrieval timed out, so no fresh local Python-page hash is claimed.

- https://docs.python.org/3/tutorial/controlflow.html — actually read §4.8, §4.9.1, §4.9.2 and the parameter-kind explanation/examples of §4.9.3 through the combined-call failure examples. Definitions bind function objects; ordinary calls introduce local parameter bindings. Defaults are evaluated when the definition executes, including one shared mutable default. Explicit arguments do not replace a saved default. Missing/duplicate argument binding and positional-only/keyword-only markers support PF68–PF71 and PF80–PF82. This is not a claim to read the entire tutorial.
- https://docs.python.org/3/reference/executionmodel.html — actually read §§4.1, 4.2.1–4.2.2 and §4.2.6. Ordinary function binding classification spans the block; pre-binding reads can raise `UnboundLocalError`. Global and nonlocal choose namespaces/bindings, and free-variable lookup occurs at runtime. Class and annotation scope exceptions were noted but not adopted as ordinary-function rules. Runtime implementation/thread sections were not part of this assignment's substantive review.
- https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result — actually read the local/global explanation and complete late-binding/default-snapshot examples immediately surrounding this heading. This independently confirms PF77–PF78. It does not imply that every closure snapshots a value.
- https://docs.python.org/3/reference/expressions.html#evaluation-order — actually read §6.16 and adjacent ordinary-call return/binding paragraphs of §6.3.4. Left-to-right expression evaluation confirms PF79. Entire comprehensions and precedence chapters were not counted as comprehensively read.

## Exact C provisions freshly reread

The official WG14 N1570 PDF failed through the web reader, but fresh local HTTPS retrieval succeeded. The Dalhousie copy has the identical SHA-256 `208969fec021e4f4ce87a1873765298c73e7bbb5209b1c5868967c7adfc8492e`. This is a C11 committee draft used for corresponding retained C17 rules, not a freshly acquired final C17 standard. Only the listed provisions were substantively reread; all 701 pages were not read.

Official artifact: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf

| Provision | Physical PDF page | Verified use |
| --- | --- | --- |
| 6.2.1p7 | 54 | Ordinary identifier scope begins after completion of its declarator. |
| 6.2.4p2,p6 | 56 | Ended-lifetime access and pointer indeterminacy; separate recursive automatic instances. |
| 6.5p2,p5 | 94 | Conflicting unsequenced scalar effects and unrepresentable arithmetic. |
| 6.5.2.2p7,p10 | 100 | Parameter conversions/default promotions; noninterleaving, indeterminately sequenced called bodies. |
| 6.5.5p5–6 | 110 | Zero division, truncation and quotient-remainder representability. |
| 6.5.15p4 | 118 | Conditional guard precedes the one selected branch. |
| 6.5.17p2 | 123 | Comma operator sequencing differs from argument separators. |
| 6.7.6.3p7–10 | 151 | Array/function parameter adjustment and void-list interface. |
| 6.8p4 | 164 | Sequencing between full expressions. |
| 6.8.5p6 and continuation | 168–169 | Qualified permission to assume loop termination. |
| 6.9.1p9–12 | 175 | Automatic parameter objects, as-if-assignment entry, used missing return. |

Pages 100 and 118 were additionally visually inspected. `c-scopes.txt` and `c-additional-scopes.txt` retain the first set of extracted relevant pages; declaration scope and conditional/loop-continuation pages were read in a separate tool output. These are evidence excerpts, not an all-standard audit.

The exact C17 correction to loop paragraph 6 was also read in full at the official committee issue: https://www9.open-std.org/JTC1/SC22/WG14/issues/c11c17/issue0436.html . The fixed wording permits termination assumptions for nonconstant controlling expressions without I/O, volatile access, synchronization or atomics. A stipulated mathematical divergent branch, or `if (x<0) while(1){}`, avoids silently treating every side-effect-free nonconstant C loop as a portable divergence example.

## Question review PF37–PF89

All 53 stems and their current saved solutions were individually read. Their arithmetic results and major classifications agree with the declared models. This is an independent semantic review, not an approval or a claim of adequate final instructional depth.

### Changes or qualifications to make

1. **PF43:** make the mathematical divergence contract explicit. If executable C is supplied, use a constant-condition infinite loop for the negative branch, or explain the qualified loop rule above. The existing mathematical result is correct, but an unspecified concrete C loop can undermine its intended portability.
2. **PF64:** replace “creates integer 7” with “computes integer value 7 and rebinds the local name.” A distinct observable allocation of every integer result is not part of Python's value semantics.
3. **PF71:** prefer “`r1 is r2` is false” to “false identity equality”; identity and value equality are different operations. This task's two results happen to be unequal too.
4. **PF37, PF44, PF50:** the stems refer to the preceding task or lesson definitions. Preserve the exact referenced definitions or restate them for standalone question readability; do not silently change the state/reset assumptions when rewriting.
5. **PF57:** the 32-bit interval `[-1073741827,1073741820]` is correct. The general ceiling/floor expression is mathematical, not an instruction to evaluate `-INT_MIN` or overflow intermediate C products.
6. **PF58–PF59 and PF84:** distinguish mathematical general formulas from C implementations' intermediate representability constraints. The stated concrete small examples are safe; unrestricted signed-int polynomial identities cannot imply universally executable code.
7. **PF86:** its lifetime conclusion is sound, but Stanford's two-page handout alone does not prove it. Cite the appropriate C++ lifetime rule if expanding into a standards-level reference-return discussion; do not cite C pointer-indeterminacy text as if it defines C++ references.
8. **PF87:** the ordinary `a[10]` parameter has no copied-array object or automatic length. Do not generalize its lack of a mandatory ten-element access promise to the distinct C syntax `a[static 10]`, whose minimum-access requirement is explicit in 6.7.6.3p7.

### Independently executed printed examples

`check_python.py` extracts the exact fenced Python code for PF64–PF83 from the current question JSON and applies independently written assertions. All 20 passed, including the two expected exceptions. `python-checks.json` records interpreter identity and per-ID results. This does not compile C/C++, test the browser simulations, validate the authentic archive pages, or establish universal correctness of rewritten answers.

The reference-mode examples PF60/PF61/PF89, theoretical value-result/call-by-name PF62/PF63, contract proofs, integer bounds and sums were checked by semantic/mathematical reasoning; they are not described as compiled runs.
