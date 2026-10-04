### Interfaces and call execution

1. A function declaration supplies a type interface; its definition supplies executable behavior. Do not treat a prototype as code that runs or as a complete input-value contract.

2. Parameter names in compatible prototypes and definitions may differ. Compatibility is about return and parameter types, while names inside an invocation bind its own objects.

3. Use an explicit void parameter list for a zero-argument C17 prototype. An empty list in a C17 declaration lacks a parameter-type specification; C23 and C++ use different rules.

4. A visible prototype requires compatible argument types and an appropriate count. A constraint violation requires a diagnostic; it is not a normal arithmetic-output question.

5. Evaluate an argument expression before binding its resulting value to the parameter. The parameter receives the expression value, not the caller's source-text identifier.

6. With a prototype, argument conversion occurs as if by assignment to the unqualified parameter type. A narrow type or floating conversion can change the value before the body begins.

7. A float trailing variadic argument is promoted to double, and narrow integers undergo integer promotions. A variadic interface still requires correctly retrieved promoted types.

8. The type of a returned expression's arithmetic is determined before return conversion. A double return type cannot recover the fraction already lost by int/int division.

9. Save a return continuation for every genuinely active call. The continuation records what the caller still needs to do after the callee supplies its result.

10. Count total invocations and maximum simultaneously active invocations separately. Sequential repeated helpers increase the first count without accumulating live frames.

11. Nested argument syntax does not automatically imply nested active helper bodies. In f(g(x)), g completes before f's body begins; a call inside f's body is different.

12. A return transfers control out of the current invocation. A print operation records an output event and normally continues; the two observables must be reported separately.

13. A void C call cannot supply an integer result. A Python function that falls through returns None; these are different language concepts despite informal “no result” descriptions.

14. An ordinary non-void C function reaching its closing brace has undefined behavior if the caller uses its result. The zero result for falling through initial main is a specific exception.

15. A called externally linked function needs an appropriate definition in the program. Missing implementation is a translation/linking issue, not a license to invent runtime values.

### Values, identities, and lifetimes

16. In C, scalar parameters are separate objects initialized with argument values. Assigning such a parameter does not assign the caller's scalar object.

17. Distinguish the old caller value, the current parameter value, and the returned value in every trace. Equal numerical values do not establish shared object identity.

18. Discarding a pure helper's returned value leaves caller state unchanged. Assigning that returned value to the caller produces a recurrence that must be traced separately.

19. For repeated assignments of an affine result T(x)=ax+b, use $T^k(x)=a^kx+b\sum_{j=0}^{k-1}a^j$. Handle a=1 separately when replacing the sum by a quotient.

20. A mathematical composition may have a stricter domain than its simplified formula. Preserve the preconditions of every inner and outer call even when cancellation removes a denominator.

21. A parameter object is recreated for each invocation. A recursive call with the same parameter name still owns another object, not the parent's mutable slot.

22. Scope is visibility of an identifier; storage duration is existence of an object; linkage is identity across declarations. Never use one of these words as a substitute for all three.

23. Ordinary local variables have block scope. In technical C terminology, function scope belongs to labels, while parameter names in a prototype have prototype scope.

24. Lexical scope resolves a name using its definition context. An active caller's unrelated local declaration does not become visible in a separately defined C function.

25. Shadowing introduces a distinct declaration and hides a spelling in a region. It does not delete, overwrite, or merge the outer object.

26. The scope of a local C declaration begins before its initializer expression. In int x=x, the initializer selects the new uninitialized local, not a hidden outer x.

27. A new automatic scalar without an initializer is not guaranteed to contain zero. Do not derive an output from guessed previous stack contents.

28. A block-scope static object is initialized once and persists across calls. Its name remains limited to its block; persistent storage does not imply global visibility.

29. Distinct static declarations create distinct objects even if their names and initial values match. Conversely, recursive invocations share the single object of one static declaration.

30. Static-duration objects without explicit initializers receive zero initialization. That guarantee does not extend to ordinary uninitialized automatic objects.

31. File-scope static gives internal linkage to a function or object. Block-scope static gives static storage duration to an object; it does not define a reference passing mode.

32. Returning an integer value and returning a pointer to its local object are different operations. The copied value can survive after the automatic object ends.

33. A returned pointer or C++ reference to an expired automatic local cannot safely access that object. Pointer/reference syntax does not extend its lifetime.

34. A pointer to a live static object remains usable after return, but later calls can change that shared object. A stable address does not promise a stable value.

35. Conceptual call-stack diagrams specify identities and continuations. They do not prove a physical stack direction, exact frame size, address, or absence of optimization.

### Pointer parameters and aliases

36. A C pointer parameter receives a copied pointer value. The local pointer object is distinct from the caller's pointer object, although both can designate the same target.

37. Assignment p=q redirects only the local copied pointer p. Assignment *p=value writes the live designated target, which may be a caller object.

38. To redirect a caller pointer variable through a parameter, pass the address of that pointer object and write through a compatible pointer-to-pointer.

39. A pointer's target must exist, be appropriately typed/aligned, and permit the requested access. A non-null value alone does not establish these conditions.

40. Identify aliases before performing sequential mutations. If p and q designate one object, the second full statement reads the state produced by the first.

41. The map *p+=2; *q*=3 gives separate outputs (u+2,3v) for distinct targets and the single output 3u+6 for an aliased target. These are different state spaces.

42. Reversing aliased operations changes their composition unless they commute. Increment-then-scale and scale-then-increment cannot be exchanged without proof.

43. Temporary-based swapping supports identical valid targets and avoids arithmetic overflow. An arithmetic or XOR replacement needs separate alias and machine-safety analysis.

44. Multiple output pointers require an explicit alias contract. If two promised final scalar values differ, one scalar object cannot simultaneously retain both.

45. An output may safely designate an original caller input object when the callee already received the input value by scalar copy. This differs from two outputs aliasing each other.

46. A pointer member in a copied structure remains a pointer to the original target unless a deep-copy algorithm is explicitly performed. Structure value passing alone does not duplicate reachable objects.

47. An array-shaped parameter declaration adjusts to a pointer parameter. It neither copies the array nor automatically communicates its runtime length.

48. sizeof of an adjusted array parameter measures a pointer object, not the caller array. Use an explicit length interface rather than guessing from that expression.

49. const int * prevents target writes through that pointer access path. It does not establish that no other alias can change the original non-const object.

50. int *const prevents reassignment of the local pointer but allows valid target writes. const int *const combines two distinct restrictions.

### Order, macros, and behavior classification

51. Commas separating C17 arguments are not comma operators. They do not impose a left-to-right argument evaluation order.

52. Direct conflicting modifications such as f(i++,i++) are unsequenced in C17 and yield undefined behavior. Do not turn undefined behavior into a small set of plausible answers.

53. Separate function body executions that are not otherwise ordered are indeterminately sequenced in C17. Two next() calls can complete in either order without interleaving their bodies.

54. With a counter starting at zero, sub(next(),next()) can return -1 or 1, while add(next(),next()) returns 3 in either permitted order. Unique output does not imply unique internal order.

55. Separate full expressions can force an order and preserve saved values. When rewriting for clarity, retain which expression value is saved before each side effect.

56. The actual comma operator sequences its left operand before its right operand and yields the right operand's value. Parentheses can distinguish it from argument punctuation.

57. C && and || sequence and conditionally evaluate operands. Their control effects can skip a call entirely, so call counts must include short-circuit conditions.

58. Signed arithmetic outside the representable range is undefined in C. Do not import C0's modular integer interpretation from a contracts example into signed C code.

59. Mathematical representability of the final result is insufficient. Check every executed intermediate, including an unnecessary final square whose value is later discarded.

60. A function-like macro substitutes tokens rather than creating parameter objects. Expand it before analyzing value, side effects, precedence, or scope.

61. Parentheses around macro parameters fix many precedence errors but do not guarantee one evaluation. TWICE(i++) still performs two unsequenced modifications under addition.

62. A conditional macro can evaluate an argument twice with defined sequencing. MAX(i++,2) at i=3 produces result 4 and final i=5; “repeated” is not automatically “unsequenced.”

63. Classify language constraints, undefined behavior, unspecified outcomes, implementation-defined choices, and ordinary defined execution before deriving an output. These classifications are not interchangeable.

64. C++17 argument sequencing rules differ from C17. A similar-looking C++ expression must receive its own language label and analysis.

### Contracts, callbacks, and cross-language distinctions

65. A precondition is an obligation at the call site. A postcondition may be used after a safe normal return; total correctness additionally requires termination.

66. A frame condition limits which external objects may change. A numerical postcondition alone does not prove that a helper is pure.

67. A specification promising “a positive common divisor” does not promise “the greatest common divisor.” The constant-one implementation refutes that inference.

68. Every reachable return site must establish the postcondition, including early returns inside a loop. A proof only for the closing return is incomplete.

69. To compose helpers, establish each next call's precondition from previous postconditions and preserved state. Safe individual helpers do not make all caller arithmetic safe.

70. Quotient/remainder contracts require a defined division domain, a remainder convention, and valid distinct outputs when both values must survive. In C, negative division truncates toward zero.

71. A callback's callable type must match its implementation. An incompatible cast does not turn one function signature into another valid calling convention.

72. Pure callback composition permits algebraic substitution; stateful callback composition must include changing state. A callback called twice can use two different persistent counter values.

73. A C++ reference parameter aliases its referent; a value parameter copies its value. Passing the same argument twice can therefore produce one alias and one copy.

74. C++ assignment through a reference changes its referent; it does not reseat the reference. Binding restrictions and referent lifetime still apply.

75. Value-result and call-by-name are theoretical passing models unless the question supplies a language supporting them. Value-result aliases need a copy-out order to define a unique final state.

76. Python parameters bind to supplied objects. Rebinding a local name does not rebind a caller name, while mutating a shared mutable object can be visible through both.

77. Python free variables follow lexical parents, not the current caller. Returned closures can retain their enclosing bindings after the factory call finishes.

78. Python defaults are evaluated when the definition executes. A mutable default is shared across calls using it; an explicit argument does not reset that stored default.

79. Loop-created Python closures can share a late-read binding; per-definition defaults can instead save each current value. Explain binding identity and evaluation time rather than saying merely “captured.”

80. A Python binding operation can make a name local throughout its function block, causing an earlier read to raise UnboundLocalError. State session/error outcomes accurately; a failed call does not supply a normal numeric return.
