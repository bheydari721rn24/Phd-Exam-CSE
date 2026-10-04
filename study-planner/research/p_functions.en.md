# Functions, Variable Scope, and Parameter Passing

## Scope, prerequisites, and selected written courses

Read the approved [types and expressions](p_types.html) and [control flow](p_flow.html) chapters first. You must distinguish a stored value, an expression value, an object, and an identifier. This chapter explains how a function call creates local state, how identifiers select objects, how parameters receive arguments, how results return, and how effects cross a call boundary. It also develops mathematical specifications and a reliable examination tracing procedure.

**Language contract.** Unmarked code is C17, not C++, C23, or historical implicit-int C. Python blocks use ordinary Python 3 semantics; C++ blocks are explicitly marked C++17. Numerical examples stay within the stated type's representable range. A fragment is inside an enclosing function unless a complete definition or file-scope declaration is displayed. Library declarations require their standard headers. Pointer examples assume live, correctly aligned objects of the indicated type; the only aliasing considered is between compatible integer objects. A variable named “stack” in a drawing is a conceptual activation stack, not an assertion about an actual processor's addresses. Array indexing, dynamic allocation, advanced recursion recurrences, object-oriented methods, concurrency, and ABI layout receive dedicated later chapters.

The six-course discovery pool was evaluated for written accessibility, relevance to this exact boundary, precision of the semantic model, explanatory depth, and useful problem families. Four complementary courses are primary; two add useful cross-language checks. This bounded pool is documented, rather than presented as every university course worldwide.

| University and course | Written material actually examined | Selection and role |
|---|---|---|
| Cambridge, Programming in C, 2017–18; Neel Krishnaswami | [Lecture 2, Functions and the Preprocessor](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture2.pdf), all 19 slides | Primary C interface, copying, static storage, linkage, macros, and compilation source. Simplified terminology is refined using the language rules below. |
| UC Berkeley, CS61A; John DeNero's Composing Programs | [§1.3](https://composingprograms.com/pages/13-defining-new-functions.html), [§1.6.3–1.6.4](https://composingprograms.com/pages/16-higher-order-functions.html), and the mutation/sharing portions of [§2.4](https://composingprograms.com/pages/24-mutable-data.html) | Primary environment, lexical-parent, closure, and object-sharing source. Python binding does not imply C++ reference parameters. |
| Harvard, CS50x 2025; David J. Malan | [Lecture 1, Functions](https://cs50.harvard.edu/x/2025/notes/1/) and [Lecture 4, Swapping](https://cs50.harvard.edu/x/2025/notes/4/) | Primary concrete C examples and pointer-mediated effects. “By reference” in the teaching notes is interpreted as passing a pointer value; C still passes parameters by value. |
| CMU, 15-122, Fall 2026; Frank Pfenning and Iliano Cervesato | [Lecture 1, Contracts](https://www.cs.cmu.edu/~15122/handouts/lectures/01-contracts.pdf), pp. 19–39, with introductory example context | Primary modular proof source. C0's modular integer arithmetic must not be imported into signed C arithmetic. |
| Stanford, CS106B, Winter 2016; course teaching staff | [Functions and Pass by Reference](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1164/handouts/1-PassbyReference.pdf), both pages | Selected comparison: genuine C++ reference binding and interface readability. The handout does not identify an individual author, so none is guessed. |
| MIT, 6.0001, Fall 2016; Ana Bell, Eric Grimson, John Guttag | [Lecture 4 slides](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/6ba59859535f1566dd57a7279aeba5d1_MIT6_0001F16_Lec4.pdf), slides 3–35 | Selected independent Python comparison: decomposition, return versus print, and scope. Historical print syntax is rewritten for Python 3; integer parameters and mutable objects are treated separately. |

The public [WG14 N1570 committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), §§6.2.1–6.2.4, 6.5.2.2, 6.7.6.3, 6.8.6.4, 6.9.1, and 6.10.3, checks the C rules used here. It is a C11 draft, not the published C17 standard; this chapter uses the relevant rules retained in C17. The [Python tutorial, §§4.8–4.9](https://docs.python.org/3/tutorial/controlflow.html), checks default arguments and parameter binding. References supply concepts and checks; the derivations, numerical tasks, figures, and simulation models here are independently written. The complete exercise lists of the external courses are not reproduced.

**Learning route.** Learn the call interface, then copy semantics, then scope and lifetime. Add pointer effects and aliases only after these distinctions are clear. Study unspecified order and undefined behavior before numerical tracing. Complete contracts, callbacks, and the explicitly marked Python comparisons, then use the worked bank and final rules. The two authentic archive questions are disclosed bridge revisits: they use elementary recursive call semantics, while their full array/recursive-algorithm treatment belongs to later chapters.

## Functions as interfaces and state transformations

A mathematical function assigns one output to each input in its domain. A program function can also read external state, modify objects, produce output, fail, or not terminate. Therefore a parameter list alone need not describe its complete input. A stateful function is more accurately modeled as a transition:

$$F:(a,\sigma)\mapsto(r,\sigma').$$

Here $a$ is the argument tuple, $\sigma$ is the relevant state before the call, $r$ is its returned value if it returns, and $\sigma'$ is the state afterward. Output events can be included in the state. A pure, deterministic, terminating function whose result depends only on its explicit arguments reduces to $f:a\mapsto r$. A static counter does not: its returned value depends on its call history. A function that prints a number and returns zero has a printed event and a returned result; these are different observables.

An interface has four obligations: acceptable input values, acceptable input objects and aliases, the result relationship, and allowed effects. The type system checks only part of this. Two integer parameters cannot express “the second is nonzero”; two pointers cannot alone express “both point to initialized writable objects.” A useful function contract includes those requirements in words or assertions.

### Declaration, definition, prototype, and call

~~~c
int shifted_square(int value, int shift);  /* prototype */

int shifted_square(int value, int shift) {
    int adjusted = value + shift;
    return adjusted * adjusted;
}
~~~

The prototype declares a function taking two integers and returning an integer. The definition supplies its body. Parameter names in separate prototypes need not match those in the definition; their types must be compatible. The call supplies argument expressions:

~~~c
int result = shifted_square(2 + 1, 4);
~~~

First evaluate argument expressions under C's sequencing rules; their values are 3 and 4. Convert each to its parameter type, create the call's local parameter objects, and run the body. The local object named value contains 3; shift contains 4; adjusted becomes 7; the returned value is 49. The caller then initializes result with 49. The body is not executed merely because its definition was encountered during translation.

The expression return type is determined by the declaration, not by the destination:

~~~c
double ratio(int a, int b) { return a / b; }
double answer = ratio(7, 2);  /* 3.0, not 3.5 */
~~~

Both operands of division are integers, so integer division produces 3 first. Return conversion then produces 3.0. Changing the destination type cannot undo the lost fraction. Use a floating operand before dividing, with a nonzero denominator.

### Empty parameter lists and compatibility

In C17, int sample(void); is a prototype for zero parameters. A declaration int sample(); does not provide a parameter-type list; it is not the same type-checking interface. In a C17 definition, int sample() { return 1; } defines a zero-parameter function, but its empty-list form still does not provide a prototype. Use the explicit void form. The meaning changed in C23, which is outside this chapter. In C++, an empty list means no arguments.

With a prototype, a wrong argument count or an incompatible argument type violates a constraint and requires a diagnostic. A declaration alone does not provide executable code: a called function with external linkage needs an appropriate definition in the program. A header normally contains the shared prototype, not duplicate external definitions. These failures concern translation/linkage, and should not be answered by inventing runtime output.

## Call frames, continuations, and returned values

A call frame is a model of one active invocation: parameter bindings, local objects, saved intermediate results, and a continuation saying where the caller resumes. It is not the function's source code. One function definition can produce many distinct frames. The caller pauses while the callee executes; a nested call pauses that callee in turn.

~~~c
int affine(int x) { return 3 * x + 1; }
int combine(int x) {
    int first = affine(x);
    int second = affine(first);
    return first + second;
}
~~~

For combine(2), the first nested call returns 7; the second receives 7 and returns 22; combine returns 29. The two affine calls are sequential, not simultaneously active: their frames do not coexist in this example. Peak active depth, including combine but excluding its caller, is two. The total number of calls is three. Distinguishing cumulative calls from peak depth matters when a question asks for memory.

<!-- FIGURE:frames -->

Returning means evaluating the selected return expression, converting it to the declared return type, ending that invocation, and resuming its continuation. Statements later on the same executed path are skipped. An earlier print statement does not end a function. A void function can return with no expression and communicate through effects; its call has no value that can initialize an integer. Python returns None for a bare return or for reaching the end, rather than silently returning the last expression.

A non-void C function should return a value on every reachable normal exit. If it reaches the closing brace and the caller uses the result, behavior is undefined. Returning from main has special rules; reaching the closing brace of the initial main call returns zero. Do not generalize this exception to ordinary functions.

### Elementary recursive calls

Recursion is permitted, but each invocation still follows the same call rules. Consider:

~~~c
int sum_down(int n) {   /* 0 <= n <= 100 */
    if (n == 0) return 0;
    int tail = sum_down(n - 1);
    return n + tail;
}
~~~

The frame at depth $d$ has parameter $n-d$; it does not share the parameter object of its parent. Descent creates pending additions; ascent supplies their missing values. Strong induction proves $S(n)=n(n+1)/2$. There are $n+1$ invocations including the base case, and $n+1$ simultaneously active frames at the deepest point, excluding an external caller. These are semantic counts, not a guarantee that an optimized implementation allocates that many physical frames. The dedicated recursion chapter develops branching calls, recurrences, tail transformations, and deeper stack analysis.

## Pass by value and the mathematics of local updates

In C, each parameter receives a value. A scalar parameter becomes a separate object initialized from the corresponding argument. Assigning it does not assign the caller's object.

~~~c
int revise(int x) {
    x = 2 * x + 3;
    return x - 1;
}
int a = 4;
int b = revise(a);
~~~

The caller's a remains 4, the parameter becomes 11, and b receives 10. A correct trace uses three separate quantities: original caller value, current parameter value, and returned value.

If the initial argument is $u$, the local update is $x'=2u+3$ and the result is $2u+2$. The caller's transition is $(a,b)\mapsto(a,2a+2)$. Writing $a'=2a+3$ falsely merges two objects. This is why “the function doubled its input” must be qualified: did it compute a doubled result, modify a parameter copy, or modify an object through an address?

Calling the same pure function repeatedly with the same argument does not accumulate its local changes. Assignment of the result does:

~~~c
a = revise(a);
a = revise(a);
~~~

Now a goes from 4 to 10 to 22. For an affine returned map $T(x)=\alpha x+\beta$, repeated result assignment gives

$$T^k(x)=\alpha^k x+\beta\sum_{j=0}^{k-1}\alpha^j.$$

For $\alpha\ne1$, the geometric sum is $(\alpha^k-1)/(\alpha-1)$; for $\alpha=1$, it is $k$. This formula requires all intermediate C values to be representable. Calls that discard the result instead leave a unchanged.

<!-- FIGURE:copy -->

A structure passed by value copies its member values into a distinct parameter object. If a member is itself a pointer, the pointer value is copied, not the object it points to. Thus “copied structure” is not equivalent to “deeply duplicated reachable storage.” Arrays as function parameters are a different rule: a declaration such as void edit(int a[]) adjusts that parameter to int *a. No array object is copied by that declaration. Length must be communicated separately unless the interface supplies it another way. These distinctions are developed in the arrays and structures chapters.

## Scope, storage duration, linkage, and shadowing

**Scope** answers where an identifier can be used to designate an entity. **Storage duration** answers how long an object exists. **Linkage** answers whether declarations in different scopes or translation units designate the same entity. These three questions must be answered separately.

| Declaration in C17 | Identifier scope | Object duration / identity |
|---|---|---|
| An ordinary local variable inside a block | From its declaration to the end of that block, excluding inner hiding | Automatic duration for that execution of the block |
| A parameter in a function definition | Function body block scope | A new parameter object for each invocation |
| A block-scope static variable | Block scope | Static storage duration; one object across calls |
| A file-scope variable | File scope from its declaration | Static storage duration; linkage depends on declarations |
| A file-scope static function | File scope | Function has internal linkage; this is not a “persistent local parameter” |

Function scope in C is the technical scope of labels, not the ordinary scope of a local integer. Prototype parameter names have function-prototype scope and need not remain visible after the declaration. The storage category is about objects; a function is not a block-scope automatic object.

### Lexical name lookup and declaration points

~~~c
int x = 10;
int read_x(void) { return x; }
int caller(void) {
    int x = 3;
    return read_x() + x;
}
~~~

read_x uses its file-scope x, not its caller's local x. The result is 13. C has lexical scoping: an active caller's declarations do not suddenly become visible in a separately defined callee. Shadowing creates another declaration; it does not delete the outer object.

~~~c
int x = 8;
/* inside a function */
{
    int x = x;  /* deliberately invalid value reasoning */
}
~~~

The local declaration's scope begins just after its declarator, before its initializer. The initializer reads the new uninitialized local x, not the outer 8. This example must not be assigned a reliable numeric result. Do not interpret it as a convenient “copy the outer x” idiom.

<!-- FIGURE:scope -->

### Automatic and static locals

~~~c
int next_value(void) {
    int fresh = 0;
    static int saved = 0;
    ++fresh;
    ++saved;
    return 10 * fresh + saved;
}
~~~

Separate statements calling this function three times return 11, 12, 13. fresh starts again on every call; saved is initialized once and retains its changes. The static local name is still usable only within its block. Static duration does not make a variable globally visible. Recursive calls share that static object even though their ordinary parameters and automatic locals are distinct.

A C static-duration object is zero-initialized when no explicit initializer is supplied. An ordinary uninitialized automatic scalar is not guaranteed to be zero. Initialization of a block-scope static object is not rerun at each call. C's initializer restrictions differ from C++'s dynamic local-static initialization; do not silently transfer them.

When an automatic local object's lifetime ends, returning its address does not keep it alive. A caller may not dereference a pointer to that expired local. Returning the value itself is different: the value can initialize a live caller object after the callee's local object has ended. A pointer to a static local remains attached to a live object, although future calls can modify that shared object.

## Pointer parameters, aliases, and output objects

Passing a pointer copies an address value. The parameter pointer is a new object; its target can be the caller's live object. Distinguish assigning the pointer from assigning through it.

~~~c
void revise_object(int *p) {
    *p = 2 * *p + 3;
}
int a = 4;
revise_object(&a);  /* a becomes 11 */
~~~

The expression &a produces a pointer to a. The parameter p contains that pointer value. The expression *p designates a; assigning *p changes a. By contrast, p = &some_other_live_object changes only the parameter pointer. To change the caller's pointer object, pass its address and use a pointer-to-pointer:

~~~c
void redirect(int **slot, int *target) {
    *slot = target;
}
~~~

This requires slot to point to a live writable pointer object; target must have a compatible pointer type. redirect(&p,&b) changes p to point at b. Neither scalar b nor p's previous target is changed by this assignment.

### Swap and aliases

~~~c
void swap_int(int *a, int *b) {
    int saved = *a;
    *a = *b;
    *b = saved;
}
~~~

For distinct valid targets with initial values $u,v$, the result is $(v,u)$. If both parameters point to the same valid integer object, the temporary-based swap safely leaves it unchanged. There is no general “all aliases are invalid” rule. A contract must state whether aliases are allowed and whether the implementation works under them.

<!-- FIGURE:alias -->

Compare:

~~~c
void update_pair(int *p, int *q) {
    *p += 2;
    *q *= 3;
}
~~~

With distinct targets, $(u,v)\mapsto(u+2,3v)$. With p == q and initial value $u$, the single object becomes $3(u+2)$. Each full statement completes before the next. Applying the distinct-target formula to aliases misses the updated value. Reversing the statements would instead yield $3u+2$; these transformations do not commute.

An output pointer interface can provide several results, but aliases can destroy an assumed relationship. A quotient/remainder function that writes *q first and *r second cannot preserve two different values when q == r. Either forbid aliasing explicitly or use a returned structure. “Computes both outputs” is incomplete without output-object requirements.

### const and access permissions

A const int *p parameter prevents modification of its target through that access path, but does not prove the object cannot change through some other non-const alias. An int *const p parameter prevents reassignment of the local pointer object but permits a write through *p to a valid non-const target. A const int *const p combines both restrictions. These are type constraints, not automatic claims about global immutability or thread safety.

## Evaluation order and behavior classification

First classify the code; only then compute an output. For C17, the commas separating arguments are not comma operators. There is no universal left-to-right argument evaluation rule.

~~~c
int difference(int a, int b) { return a - b; }
int counter = 0;
int next(void) { return ++counter; }
/* counter is reset to zero before this expression */
int r = difference(next(), next());
~~~

The two next function executions are indeterminately sequenced: one completes before the other, but either order is allowed. The final counter is 2, and r can be -1 or 1. This is not the same as directly evaluating difference(counter++, counter++): those conflicting modifications in the argument expressions are unsequenced in C17, giving undefined behavior. The program with two separate next executions is an important distinction often lost in simplified notes.

<!-- FIGURE:orders -->

An unspecified permitted order can nevertheless produce a unique result. With add(next(),next()), the sum is 3 in either order, provided add has no additional effects. Deterministic final output does not imply deterministic internal order. Conversely, undefined behavior is not “choose either plausible output”; the language imposes no such restricted set of results.

Use separate full expressions to impose order:

~~~c
int left = next();
int right = next();
int r = difference(left, right);  /* -1 */
~~~

Within an actual comma operator (e1,e2), e1 is evaluated before e2; its value is discarded and the expression yields e2's value. C's && and || also sequence the first operand before a conditionally evaluated second operand. Function arguments, arithmetic operands, and assignment side effects each need their own rules. A C++17 example involving two argument increments has different sequencing rules and must be labeled separately.

Macro arguments are tokens substituted into an expansion, not fresh parameter objects:

~~~c
#define TWICE(x) ((x) + (x))
int twice(int x) { return x + x; }
~~~

twice(i++) evaluates the increment once before the body; TWICE(i++) expands to two unsequenced modifications and is undefined in C17. Parentheses fix precedence, not repeated evaluation. A MAX macro with a comparison followed by a conditional selected operand can evaluate a selected argument twice even when its operations are properly sequenced. Expand before tracing.

## Contracts, composition, and exact mathematical results

A precondition is the caller's obligation; a postcondition is the callee's promise if its precondition holds and it returns. Total correctness additionally requires termination. A frame condition names state that the function may modify, and thereby state that must remain unchanged. Without a frame condition, a postcondition about the result does not justify claiming that external state was preserved.

For a pure C helper increment_bound(x) returning x+3, a correct safety precondition is $x\le\operatorname{INT\_MAX}-3$; a lower bound is unnecessary for this addition. The postcondition is $r=x+3$, and the frame condition is “no caller object is changed.” If a caller then doubles r, it must prove the doubled value fits too. Safe helper calls do not automatically make the whole expression safe.

### Weakest preconditions through pure helpers

Let f(x)=2x+1 and g(y)=3y-4 over mathematical integers. To obtain $g(f(x))=11$, substitute the postcondition of f into g:

$$g(f(x))=6x-1.$$

Thus x must equal 2. For $g(f(x))\ge17$, require $x\ge3$. In C, additionally verify that both helper bodies and the caller expression avoid overflow. Replacing a pure helper with a stateful implementation breaks this substitution unless its relevant state effects are tracked.

### A contract for quotient and remainder

For nonnegative integer n and positive integer d, define q and r by

$$n=qd+r,\qquad 0\le r<d.$$

Existence follows from integer division; uniqueness follows because two decompositions imply $(q-q')d=r'-r$, whose right side has magnitude less than d, so the multiple of d must be zero. An interface:

~~~c
void divide_nonnegative(int n, int d, int *q, int *r) {
    *q = n / d;
    *r = n % d;
}
~~~

requires nonnegative n, positive d, initialized input values, two live writable integer output objects, and q != r if both results must survive. The input arguments are scalar copies, so they remain fixed even if an output object is also the original caller's n object. The two output pointers aliasing each other is a different issue. For signed general inputs, C17 division truncates toward zero and the remainder has the numerator's sign when nonzero; the mathematical nonnegative-remainder contract would need adjustment. INT_MIN divided by -1 is invalid when the quotient is not representable.

### Complete proof for a summation helper

For $0\le n\le100$, the following C17 implementation computes the triangular sum safely on every conforming C17 implementation:

~~~c
int triangular(int n) {
    int total = 0;
    for (int k = 1; k <= n; ++k)
        total += k;
    return total;
}
~~~

At the guard, use $1\le k\le n+1$ and $\operatorname{total}=(k-1)k/2$. Initialization holds for k=1. One body adds k, making total $k(k+1)/2$; the increment makes the same invariant true for the next k. The guard eventually fails because k strictly increases toward n+1. At exit k=n+1, giving $n(n+1)/2$. The maximum result is 5050, and k never exceeds 101, both inside every C17 int's guaranteed range. This is an actual machine safety proof; the formula alone does not certify an unrestricted implementation.

<!-- FIGURE:contracts -->

## Callback interfaces and alternative parameter models

A C function pointer can select behavior:

~~~c
int apply_twice(int (*step)(int), int x) {
    int once = step(x);
    return step(once);
}
~~~

With a pure step(x)=2x+1, the result is 4x+3. A pointer to a function has a callable type; calling through an incompatible function-pointer type is not a valid way to change its signature. If step has effects, apply_twice still performs two calls in the order established by its statements, but its result cannot be computed by pure algebra unless those effects are modeled. Parentheses in int (*step)(int) distinguish a function pointer from a function returning a pointer.

### Genuine C++ references

~~~cpp
void change(int &x, int y) {
    x += y;
    y = 0;
}
~~~

For change(a,b), x refers to a while y is a separate copy of b. If a=4 and b=7, the caller ends with a=11,b=7. A reference cannot later be reseated by assignment: assigning x assigns its referent. A non-const int& cannot bind to the temporary integer literal 3. A const int& can bind to a temporary under the appropriate lifetime rules. Reference binding and a copied pointer value are distinct models even when both can let a callee modify a caller object.

### Explicit theoretical comparison

In call by value-result, a parameter is copied in and copied out on return; this is not C's rule. If two such parameters share one actual variable and end with different values, the final caller result depends on the specified copy-out order. Call by name reevaluates an argument expression using the caller environment when the parameter is used; it is not a stored copy or a C macro in general. A question specifying either theoretical model overrides the ordinary language default and must supply enough order rules to determine a unique result. Do not guess these rules from a function's name.

## Python binding, lexical parents, and persistent environments

Python calls bind local parameter names to the supplied objects. Rebinding a parameter name does not rebind the caller's name. Mutating a shared object can be visible to the caller. “Everything is copied” and “every parameter is a C++ reference” are both wrong models.

~~~python
def alter(values):
    values.append(7)
    values = [99]
    return values

data = [2]
result = alter(data)
~~~

data now refers to [2,7]; result refers to [99]. The append mutated the shared original list. The later assignment rebound the local name to a different list. The caller's binding was not redirected. With integer parameters, x += 1 produces a new integer and rebinds the local name; integers themselves are immutable.

<!-- FIGURE:sharing -->

Python determines ordinary local names for a function block from binding operations in that block. Reading x before a later local assignment can raise UnboundLocalError even if a global x exists. global directs binding to the module namespace; nonlocal directs binding to an existing enclosing function binding. The global statement does not mean “use the calling function's locals.” Closures follow the environment of definition.

~~~python
def make_shift(k):
    def shift(x):
        return x + k
    return shift

f = make_shift(4)
g = make_shift(9)
~~~

The two factory calls create separate enclosing bindings for k. Later f(3)=7 and g(3)=12. Returning from the factory does not make a retained closure's environment inaccessible; this is unlike returning a C pointer to an expired automatic local. The model tracks lexical parents, not active caller parents.

### Definition-time defaults and call-time lookup

~~~python
base = 4
def frozen(x=base):
    return x
def live():
    return base
base = 9
~~~

frozen() returns 4 because its default expression was evaluated when the definition executed; live() returns 9 because its global lookup occurs at the call. A mutable default such as values=[] creates one list at definition time, shared across calls using that default. A None sentinel can create a fresh list per call. Passing an explicit list bypasses the default for that call; it does not clear the saved default list.

Loop-created closures generally share the enclosing variable binding, so three lambdas returning a loop variable can all later read its final value. Using a default argument in each lambda can snapshot the current value instead. The word “capture” is ambiguous unless one states whether a binding or a value is retained.

Python arguments are evaluated from left to right. A call with side effects can therefore have a unique Python trace that the similar-looking C17 call does not. Positional-only parameters precede /; keyword-only parameters follow *; remaining parameters can be bound positionally or by keyword. Supplying a parameter twice or omitting a required argument raises TypeError. None is a real singleton object, not an undeclared missing value or C void expression.

## Worked mathematical, conceptual, and archive problems

Every task includes a complete derivation. Begin with behavior classification and object identity, then compute. The authentic questions below are checked against original PDF pages; their options are expressed in English by their decisive algorithmic properties where source pseudocode is not strictly C17. The archive solutions are independently derived, not labeled official answer keys. Revisited questions are not claimed as newly discovered unique items.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

**Summary.** A function definition supplies behavior; a declaration supplies an interface. Each invocation owns distinct parameter objects and automatic locals, while designated static state persists. A call evaluates arguments, initializes parameters, executes its body, and returns to a saved continuation. Scope selects declarations; lifetime determines whether objects still exist; linkage identifies declarations across boundaries. Scalar assignment, pointer reassignment, and target mutation are three different operations. Aliases make sequential mutations share state. Pure functions permit algebraic composition; stateful functions require state composition. Language rules decide whether an output is unique, one of several permitted outcomes, or not defined at all. Contracts connect safe inputs to guaranteed outputs and explicit effects. Python adds object-sharing, lexical closure environments, and definition-time defaults; C++ adds genuine reference parameters.

**Examination procedure.** (1) State the language and parameter model. (2) Check declarations, call types, initialization, arithmetic range, and pointer lifetime. (3) Give every distinct object an identity, including shared static objects and aliased targets. (4) Separate argument evaluation from parameter initialization. (5) Record pending return continuations. (6) Follow the specified sequencing; branch the trace if order is unspecified. (7) Perform copy-out only if the question explicitly defines such a model. (8) Report the returned result, printed events, and final caller state separately. (9) Verify formulas at zero, one, a boundary, and an alias case. (10) Justify the general relation with contracts or induction; finite runs do not replace a proof.

<!-- INCLUDE:review -->

## Exact call-state laboratory

The laboratory replays curated, defined models with an adjustable integer input. It does not execute arbitrary submitted code or assign outputs to undefined expressions. Each checkpoint records the caller state, active local state, shared-object state, returned result, and pending continuation. Argument tokens move into a callee and returned tokens move back to the caller; the original caller object remains in place. Choose scalar copying, pointer mutation, aliased updates, static persistence, or nested calls and compare their exact formulas. Playback begins paused. The conceptual stack does not impose any physical address layout or promise that a compiler allocates visible frames.

<!-- LAB:functions -->

## References and scope of the evidence

1. Neel Krishnaswami. Programming in C, Michaelmas 2017–18, Lecture 2: Functions and the Preprocessor. University of Cambridge. [Written slides](https://www.cl.cam.ac.uk/teaching/1718/ProgC/lectures/lecture2.pdf). Function interfaces, copied arguments, storage/linkage, and macro distinctions.
2. John DeNero. Composing Programs, CS61A teaching text, UC Berkeley. [Defining New Functions](https://composingprograms.com/pages/13-defining-new-functions.html), [Higher-Order Functions](https://composingprograms.com/pages/16-higher-order-functions.html), and [Mutable Data](https://composingprograms.com/pages/24-mutable-data.html). Environments, lexical parents, closures, and sharing. Original exposition here does not reproduce the textbook's exercise corpus.
3. David J. Malan. CS50x 2025, Harvard University. [Lecture 1 notes](https://cs50.harvard.edu/x/2025/notes/1/) and [Lecture 4 notes](https://cs50.harvard.edu/x/2025/notes/4/). Function decomposition and pointer-mediated swapping.
4. Frank Pfenning and Iliano Cervesato. 15-122 Principles of Imperative Computation, Fall 2026, Lecture 1: Contracts. Carnegie Mellon University. [Written notes](https://www.cs.cmu.edu/~15122/handouts/lectures/01-contracts.pdf). Modular reasoning and specification strength. C0 arithmetic is distinguished from C17 arithmetic.
5. Stanford CS106B course teaching staff. Winter 2016, Functions and Pass by Reference, dated 6 February 2016. [Written handout](https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1164/handouts/1-PassbyReference.pdf). No unverified individual instructor attribution is made.
6. Ana Bell, Eric Grimson, and John Guttag. MIT 6.0001, Fall 2016, Lecture 4: Decomposition, Abstraction, Functions. [Written slides](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/6ba59859535f1566dd57a7279aeba5d1_MIT6_0001F16_Lec4.pdf).
7. ISO/IEC JTC1/SC22/WG14. N1570, public C11 committee draft, April 2011. [Draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf). Relevant retained C17 rules cited in the source audit.
8. Python Software Foundation. The Python Tutorial, [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html), and the [execution model](https://docs.python.org/3/reference/executionmodel.html). Parameter binding, defaults, name resolution, global and nonlocal.
9. Iranian MSc Computer Science 1393, Q167, PDF page 34, and PhD Computer Engineering 1405, Q9, PDF page 3. [Pinned project archive](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/bdadf6e2c9cadc4772ae137a96a3da753c7cfd08/Exams). Original page hashes and English adaptation details accompany the question records.

**Audit boundary.** This chapter covers the defined functions/scope/parameter-passing boundary and explicitly marks later array, recursion, pointer-arithmetic, and allocation topics. Its source audit names all six reviewed candidates and the exact written portions; it does not certify an exhaustive global course search. Independent exact-model checks, executable Python checks, and browser checks support the delivered examples. No local C/C++ compiler was available during this revision, so compiled execution is not claimed; language-rule proofs and separate reference models check those cases. No study text can guarantee performance on every unseen examination problem.
