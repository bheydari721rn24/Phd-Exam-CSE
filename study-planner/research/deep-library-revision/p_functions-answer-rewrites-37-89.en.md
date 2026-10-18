# Functions: remaining individually rewritten teaching solutions

Working review manuscript. These blocks replace the matching answers after integration and complete chapter checks. Mathematical arithmetic and stipulated theoretical passing models are explicitly separated from C17, C++17 and Python3 behavior.

## PF37 | The same order ambiguity can disappear from the result

**Full replacement solution.** Restate the inherited setup: counter starts at zero, next increments it and returns the new value, and the call supplies two next results to an addition helper. If the left call executes first, add receives (1,2). If the right call executes first, add receives (2,1). Each next body completes before the other under the C17 function-execution rule. Both orders leave counter equal to two.

The returned sum is $1+2=2+1=3$. Thus this particular final observation is invariant even though the argument evaluation order is unspecified. A unique observed sum does not establish a unique internal execution order. Addition hides the permutation because it is commutative on these representable integer inputs.

The preceding subtraction task exposed the same uncertainty because $1-2\ne2-1$. Other side effects or state observations could expose ordering too. The reliable method is therefore to enumerate the permitted executions first and compare their observations; it is unsafe to infer left-to-right evaluation from one result or one compiler run. These separate function calls also must not be replaced silently by conflicting direct increment expressions, which have a different sequencing classification in C17.

## PF38 | Direct increments are not separate function bodies

**Full replacement solution.** Here the arguments themselves are `i++` and `i++`. Each directly modifies the same scalar i. The comma separating function arguments is punctuation, not the sequencing comma operator. C17 does not sequence one of these argument evaluations before the other, so the two modifications are unsequenced relative to each other.

The language rule forbids this conflict; the expression has undefined behavior. It is therefore incorrect to assign it a portable two-value result set by pretending that one whole increment must finish before the other. The indeterminate sequencing of separate called function bodies used in PF36 does not apply to these direct increments.

Neither a small initial value nor absence of arithmetic overflow removes that sequencing violation. One observed output from one compiler also does not define the standard's permitted result. A repair performs the increments in separate full expressions, saves the results and then calls difference with those saved values. The caller must decide the intended order when writing that repair; the original undefined expression did not specify it. PF39 shows the left-increment-first version and computes its one defined result.

## PF39 | Separate statements impose an order

**Full replacement solution.** The initializer of a evaluates postfix `i++`: its expression value is the old zero, so a is initialized to zero, while the increment changes i to one. That full expression finishes before the next declaration's initializer begins. The initializer of b therefore obtains old i equal to one and completes the increment to two.

The last statement reads the two saved objects a and b and computes $r=0-1=-1$. Final values are $(a,b,i,r)=(0,1,2,-1)$. The expression values obtained by postfix increment and the new stored value of i are different records, and both must be tracked.

There is no conflicting unsequenced modification here: the full-expression boundaries provide the required order. The later subtraction performs only reads. Replacing these two initializers by two direct increment arguments would remove that guarantee in C17, rather than preserve the trace as a compact spelling. Conversely reversing the two saved-result statements would change which named argument receives the first old value. Safe rewriting needs both valid sequencing and preservation of the intended value-to-argument mapping.

## PF40 | Comma operator inside one argument

**Full replacement solution.** The inner parentheses contain one comma-operator expression. Its left operand evaluates `i++`, producing the old zero as an expression value and changing i to one. The comma operator sequences that entire left evaluation before the right operand, then discards the left value.

The right operand `i+3` now reads one and evaluates to four. The value of the comma expression is this right-hand result, so twice receives a single argument four. Its body returns $2\cdot4=8$. Final caller i is one and r is eight.

The outer call has one argument, not two: the comma inside the nested parentheses is an operator, while a top-level comma between arguments would be a separator. Confusing the two would change both the call interface and sequencing. In this example no uncertainty remains in the arithmetic because the increment is completed before the read on its right, and all argument work completes before the helper body executes. The discarded zero is not an additional return, argument or hidden caller-side assignment.

## PF41 | Return conversion follows expression evaluation

**Full replacement solution.** The parameters a and b are int objects. Consequently the expression `a/b` uses integer division before the function's double return conversion. At inputs nine and four, it produces quotient two, truncating the positive fractional part. Converting that already computed integer to double gives2.0. The return type cannot recover the fraction that was lost earlier.

A corrected body can use `return (double)a / b;`. The cast supplies a floating operand before division, so the other operand is converted for floating division. For these small exactly representable inputs, the result is2.25. By contrast `return (double)(a/b);` casts only after the integer quotient was formed and still returns2.0.

The interface also needs a nonzero denominator. Integer division has additional representability obligations at signed extremes, while a general floating result has its own range and rounding limits. None causes a problem for the stated nine/four example. Follow the conversion chain in order: argument conversion, expression-operand conversion and evaluation, return conversion, then caller-destination conversion. A later wider type does not retroactively change an earlier operation.

## PF42 | A missing return value

**Full replacement solution.** At x=0, the condition `x>0` is false, so the only displayed return statement is skipped. Execution reaches the ordinary non-void function's closing brace without returning a value. The caller then uses that missing result to initialize y. Under C17 this use gives undefined behavior; no portable numeric value for y follows.

Zero is merely the argument and the false condition's interpretation, not an implicit returned integer. The last expression evaluated inside a function also does not become an automatic result. An explicit value must be supplied on every normally returning path whose result the caller uses.

One possible repair is to return zero after the conditional, if that is the intended specification. Another is a different interface whose remaining path has an explicit effect/error contract. The choice must follow the desired meaning rather than arbitrary compiler output. Falling through the initial invocation of main has a special zero-result rule, but f is not main. The current classification concerns normal fallthrough and a used result; it should not be confused with a path that deliberately never returns.

## PF43 | A non-returning branch is not a numeric result

**Full replacement solution.** The problem stipulates an algorithmic negative-input branch that does not terminate. Under that stipulation, there is no returned integer for x<0. On mathematical integers the nonnegative branch terminates with $x^2$, including result zero at x=0. Restricting inputs to $x\ge0$ therefore makes this a total mathematical function on its stated domain.

For a signed C17 implementation, termination alone is insufficient: the multiplication must also be representable. With maximum int value U, a sufficient exact nonnegative-input range for the square expression is $0\le x\le\lfloor\sqrt U\rfloor$. The lower signed bound is irrelevant to its nonnegative result, but the actual multiplication cannot be evaluated outside that range and then retrospectively declared safe.

The divergence stipulation must be respected in real code. A constant `while (1) { }` is a straightforward C loop expressing an endless branch. C17 permits assuming termination for certain nonconstant controlling expressions whose loops have no specified observable effects; an arbitrary side-effect-free loop cannot be cited without examining that rule. This question's mathematical classification is not a universal claim about every optimized C spelling of a negative-input loop. Failure to return is distinct from returning an unspecified number.

## PF44 | Function versus repeated-evaluation macro

**Full replacement solution.** Use the explicit definitions: the function twice returns twice its one int parameter; the macro is `#define TWICE(x) ((x)+(x))`. With initial i=3, calling `twice(i++)` evaluates the argument once. The argument's expression value is three, and its increment to four completes before the helper body executes. The function therefore returns six and the caller i ends at four.

Textual substitution instead makes `TWICE(i++)` into `((i++)+(i++))`. The two additions' operands both modify i and the addition operator does not sequence one operand before the other in C17. This is undefined behavior, not a legitimate sum of two predictably consecutive old values.

Parenthesizing operands protects syntactic grouping, but does not add sequencing to `+`. Nor does a function-like macro create a parameter object containing one evaluated input value. The difference is repeated expression substitution versus one argument evaluation followed by use of a parameter. A safely evaluated numeric operand such as an initialized constant can work in both forms, but that limited case does not validate side-effecting arguments. The stated small function computation has no signed-overflow issue.

## PF45 | A macro can be defined but surprising

**Full replacement solution.** Expand the macro before tracing: the expression becomes `((i++)>(2)?(i++):(2))`. Its comparison reads old i=3, schedules the postfix increment and determines that three exceeds two. The conditional operator sequences its first operand before whichever branch is selected, so i has become four before the true branch runs.

The selected `i++` now produces the old four as the conditional expression's value and changes i to five. The false branch is not evaluated. Thus r is four and final i is five. Unlike the addition macro in PF44, the relevant repeated evaluations here are sequenced; the problem is surprising repeated evaluation, not this particular unsequenced-write violation.

The number of evaluations is path-dependent. If initial i were one, the comparison would make it two, the false branch would supply constant two, and no second increment would occur. Balanced parentheses therefore do not establish an evaluate-once interface. Correct macro reasoning expands the tokens, identifies the selected branch and applies that operator's sequencing rules. It should not blindly classify every repeated occurrence of a side-effecting argument in the same way.

## PF46 | Default promotions versus prototype conversion

**Full replacement solution.** A visible prototype with a float parameter specifies the type of that corresponding parameter. Its argument is converted as if assigned to that parameter, producing a float parameter object. It is not automatically promoted into a double parameter merely because a call boundary is crossed.

A trailing variadic argument is different: no corresponding declared parameter type supplies that conversion. Default argument promotions apply, including float to double and integer promotions for narrow integer types. A variadic implementation must retrieve a value using the type appropriate to those promotions. Fetching a passed double as though it were an unpromoted float is not a harmless representation choice.

Separate the declared fixed arguments before the ellipsis from the trailing arguments after it; one call can contain both conversion regimes. A function without a prototype in historical C17 syntax has further old-style rules and should not be confused with a properly prototyped fixed float parameter. The chapter excludes C23's changed empty-list meaning. Casting the returned result later does not alter the argument conversion or retrieval that has already occurred. The ellipsis also supplies no automatic guarantee that a format string agrees with the promoted values.

## PF47 | Printing and returning are separate observations

**Full replacement solution.** Calling f with four first executes its internal print of $4+1=5$, so the first output line is5. That print does not terminate f. The following return computes $4\cdot2=8$ and supplies the integer eight as the call's result. The outer print receives that result and writes8 on the second output line.

The observation is therefore the two-line sequence five, then eight; f's returned value is eight. These are different facts: the first belongs to an output effect, the second to result flow into the caller. The return value of Python's print operation itself is None, but that does not replace f's later explicit return.

If the explicit return were omitted, f would still print five and then fall through, returning None. The outer print would then write None. If the caller merely evaluated f(4) in a script without printing the returned result, the internal five would still appear but a bare returned eight would not automatically be printed as another script output. Recording output events separately from return values prevents all three behaviors from being collapsed into one number.

## PF48 | A postcondition too weak for substitution

**Full replacement solution.** The given postcondition states that the returned r is positive and divides both positive inputs. It does not state that no larger positive common divisor exists. Consider the implementation that always returns one. Since one divides every positive integer, it satisfies exactly that stated guarantee for every permitted pair.

At a=12,b=18, however, the greatest common divisor is six while that implementation returns one. This counterexample proves that the weak contract does not entail a gcd result. It is a logical countermodel to the proposed substitution, not a claim that every implementation with a gcd-like name actually returns one.

A stronger postcondition can state equality to a defined mathematical gcd, or combine common divisibility with a maximality property over other common divisors. The caller may use that stronger statement only after the implementation has been proved to satisfy it. The helper's name and an informal glance into its body do not enlarge a modular specification. Positivity is also essential to the simple always-one example's given domain and to the downward-search proof in PF49; changing the input domain requires revisiting its boundary cases.

## PF49 | An early return still needs the postcondition

**Full replacement solution.** Assume positive integer inputs and initialize d to $m=\min(a,b)$. Maintain $1\le d\le m$ and the invariant that every integer c with $d<c\le m$ has already been shown not to divide both inputs. Initially that interval is empty, so the exclusion statement holds without any test.

If the current d divides both, the return branch establishes common divisibility. The invariant excludes every larger candidate up to m, and no positive common divisor can exceed the smaller positive input m. Thus this early return is the greatest common divisor, not merely some divisor.

If d fails and d>1, decrementing it preserves the exclusion invariant: the old d joins the previously excluded interval because its failed test has just ruled it out. The new d remains at least one. When d reaches one, it divides both positive inputs and all larger candidates are excluded, so the final return also satisfies greatestness. The nonnegative variant d−1 decreases on each unsuccessful iteration, proving termination.

The weaker invariant d≥1 proves neither exclusions nor maximality. Likewise decrementing without the failed divisibility test would not preserve the stronger invariant. A caller needs this stronger property stated in the interface if it is to rely on greatestness modularly.

## PF50 | Summation precondition and a complete invariant

**Full replacement solution.** Restate the lesson algorithm: for nonnegative n, initialize total=0,k=1; while k≤n, add k to total and increment k; return total. At every guard use $1\le k\le n+1$ and $\mathrm{total}=(k-1)k/2$. The initial zero and one satisfy both statements.

If the guard is true at some k, adding k gives $(k-1)k/2+k=k(k+1)/2$. Incrementing to $k'=k+1$ therefore restores the formula $\mathrm{total}=(k'-1)k'/2$. At exit, k>n together with k≤n+1 gives k=n+1, hence the returned value is $n(n+1)/2$.

For n=100, final k is101 and total is5050. In fact every input from zero through100 keeps k between one and101 and total between zero and5050, safely within the minimum guaranteed C17 int range. The proof's products describe mathematical values; the loop actually executes small additions and increments. Replacing it with the machine expression `n*(n+1)/2` introduces a multiplication that can overflow at larger inputs even when the final mathematical quotient fits. Operation-level safety follows the executed code, not just the final algebraic result.

## PF51 | Geometric summation as a helper specification

**Full replacement solution.** Require an integer $n\ge0$ and specify the mathematical result $r=\sum_{i=0}^{n-1}2^i$. The empty sum at zero is zero. To prove a closed form, use an accumulator p and index k with $0\le k\le n$ and $p=2^k-1$ at every loop guard.

Initially k=0,p=0, so $p=2^0-1=0$. An iteration adds the next term $2^k$, producing $(2^k-1)+2^k=2^{k+1}-1$. Incrementing k preserves the invariant. On exit k=n, giving the promised result $r=2^n-1$. The remaining-term count n−k decreases, establishing termination for the mathematical loop.

For example, n=4 adds1,2,4,8 and returns15. This check illustrates the proof but does not replace its induction. A machine implementation must separately keep every computed power, accumulation and counter update representable. Even evaluation of an asserted closed form such as a machine `pow(2,n)` can have different bounds from accumulation of powers only through n−1. CMU's C0 modular demonstration and an exact-integer specification must not be transferred unchanged into signed C17 overflow reasoning.

## PF52 | Zero exponent is a specification boundary

**Full replacement solution.** At y=0, the original guard e>1 is false immediately. Initial r=1,b=x therefore leads its final `r*b` expression to return x. The adopted nonnegative-exponent specification instead requires $x^0=1$, including the algorithm's explicit convention $0^0=1$. Except at x=1, the original boundary result is wrong.

A complete mathematical repair is the following exact-integer algorithm; its input exponent is nonnegative:

```python
def power_exact(x, y):
    assert y >= 0
    r, b, e = 1, x, y
    while e > 0:
        if e % 2 == 1:
            r *= b
        e //= 2
        if e > 0:
            b *= b
    return r
```

At each guard use $r b^e=x^y$ and e≥0. For old e=2t>0, the new exponent is t and squaring b preserves the product. For old e=2t+1, multiplying r by b before reducing/squaring gives $(rb)(b^2)^t=rb^e$. If t=0, no future base is needed; the returned r already equals the required power. At initial y=0 the body is skipped and r=1 is returned correctly. Each positive e is reduced by integer halving, so termination follows. Translating this mathematical algorithm into fixed-width C still requires safety of each executed multiplication.

## PF53 | Unused arithmetic can still overflow

**Full replacement solution.** The question explicitly assumes a32-bit signed int with maximum2147483647. At x=50000,y=1, the mathematical answer50000 is representable. A loop iteration may correctly multiply r by b once, yet an unconditional final `b*b` then computes2500000000, exceeding that maximum.

The program has executed a signed overflow even if the new base is never subsequently read. A valid final numeric postcondition cannot erase an earlier undefined operation. Safety must cover the whole executed path, including work whose result later becomes dead.

One repair first reduces the exponent and squares only when another exponent bit remains, as in the complete exact-integer algorithm in PF52. For this example, exponent one becomes zero, the square is skipped and the result50000 is returned. Another approach checks representability before every multiplication or uses an appropriate checked/wider arithmetic contract. Merely widening the final destination after the int multiplication does not help.

The32-bit assumption belongs to this example;50000 need not itself fit every conforming C17 int. Negative bases, exponent zero and signed-range endpoints also need explicit contracts rather than a claim that all representable final powers automatically validate any repeated-squaring implementation.

## PF54 | Quotient-remainder uniqueness

**Full replacement solution.** For47 and positive divisor six, $47=7\cdot6+5$, and five is in the required interval from zero through five. Thus q=7,r=5 satisfies both the identity and the remainder bounds.

Suppose two pairs q,r and $q_2,r_2$ satisfied $n=qd+r=q_2d+r_2$ with positive d and both remainders in $[0,d)$. Subtracting the identities gives $(q-q_2)d=r_2-r$. Because the two remainders differ by strictly less than d in magnitude, the right side lies strictly between −d and d. The only multiple of d in that interval is zero. Hence q=q2 and then r=r2.

This proves uniqueness for the mathematical Euclidean specification, including negative n when the specified nonnegative remainder is used. Plain C division on a negative numerator follows a different truncation convention, as PF55 shows. The stated47/six case has no such difference.

A two-output implementation must also leave the unique results in the promised distinct output objects. Computing q and r correctly internally does not prove their simultaneous final storage if output aliases overwrite one another. The arithmetic theorem and the program's state/effect contract are separate obligations.

## PF55 | Signed division needs a different remainder statement

**Full replacement solution.** C17 integer division truncates toward zero. For numerator−23 and divisor five, the quotient is−4. The remainder identity then gives $r=-23-(-4)\cdot5=-3$. Thus q=−4,r=−3 and $-23=(-4)\cdot5+(-3)$.

The Euclidean condition r≥0 fails for this C result. For defined signed division, a nonzero C remainder has the numerator's sign and magnitude smaller than the divisor's magnitude. Denominator zero and an unrepresentable signed quotient, such as the relevant minimum divided by−1, must be excluded before using this result rule.

With positive divisor d, a negative remainder can be converted to Euclidean form by replacing r by r+d and q by q−1. Here the adjusted pair is q=−5,r=2, and $-23=(-5)\cdot5+2$. The adjustment preserves the identity and puts the remainder in $[0,d)$; an actual implementation must also justify its arithmetic safety.

Python's `//` uses floor division and would directly produce−5 for these inputs, so copying its output into a C trace changes the language semantics. Always state whether the contract concerns C truncation or mathematical Euclidean division instead of mixing the quotient from one with the remainder bounds from the other.

## PF56 | A frame condition makes replacement reasoning possible

**Full replacement solution.** Regard each helper as a transition from an argument and external state to a result and new state. The pure helper maps $(x,s)$ to $(x^2,s)$. The stateful one maps $(x,s)$ to $(x^2,s+1)$, under their respective termination/arithmetic contracts. Their first components agree, but their second components differ.

If the caller later reads s, the helpers are distinguishable. For example, starting at s=0 and calling once leaves zero or one respectively, despite the same numerical result. A specification stating only result=$x^2$ permits both implementations and therefore cannot support substitution in every state-observing caller.

A frame condition states which external objects may change, or that none relevant to the caller is changed. Together with valid input, termination and the returned relation, it can justify the intended pure abstraction. A name such as square does not supply that condition. Nor does using only the returned value immediately after the call establish that no later observation can reveal an effect. If observations are intentionally restricted to the result, say so explicitly; that is a weaker equivalence claim than interchangeability in arbitrary program contexts.

## PF57 | Composing two arithmetic safety conditions

**Full replacement solution.** Let L and U be the C17 int limits. The actual input x must lie in $[L,U]$. The first call computes y=x+3; the second doubles that y. Defined doubling requires $L\le2y\le U$, hence $\lceil L/2\rceil\le y\le\lfloor U/2\rfloor$.

Substitute y=x+3 to obtain the exact interval

$$x\in[L,U]\cap\left[\left\lceil\frac L2\right\rceil-3,\left\lfloor\frac U2\right\rfloor-3\right].$$

The half-range lies within the full int range, so satisfying this doubled-result bound also keeps the intermediate y representable. The input-range intersection prevents treating an out-of-type mathematical integer as a possible caller int.

As an explicitly illustrative32-bit two's-complement assumption, use L=−2147483648 and U=2147483647. The bounds become−1073741827 through1073741820. At the lower endpoint, f returns−1073741824 and g returns L. At the upper endpoint, f returns1073741823 and g returns2147483646. The neighboring input on either side makes the doubled result exceed its respective bound.

These inequalities are mathematical reasoning about machine operations, not a request to evaluate a potentially overflowing expression while testing it. The illustrative32-bit limits are an added example, not an unstated universal assumption about every C17 int.

## PF58 | Two callback applications are not one doubled argument

**Full replacement solution.** apply first calls the supplied function on four. step computes $3\cdot4-2=10$, which is stored in apply's local y. That call has ended before the return expression invokes the callback again, now on ten. The second result is $3\cdot10-2=28$, which apply returns.

For general x, the map is $T(T(x))=3(3x-2)-2=9x-8$. Calling step on twice the original argument instead gives $T(2x)=6x-2$; at four that is22, not28. Repetition of a transformation and transformation of a multiplied input are distinct operations.

The function-pointer parameter contains a copied compatible function-designation value. Copying it does not clone the function's code or make its parameters share caller storage. Each invocation still creates its own ordinary parameter object. The first local assignment and later return expression fix the callback order, so this is not an unspecified-argument-order case. Including apply, there are three helper invocations and at most two simultaneously active helper bodies. Machine use also needs each multiplication/subtraction representable; the displayed input and results are safely within the guaranteed int range.

## PF59 | A stateful callback changes the composition

**Full replacement solution.** Begin with the one persistent counter s=0. The first callback increments it to one, adds that value to its argument five and returns six. The second callback begins with s=1, increments to two, adds two to its argument six and returns eight. The complete apply call therefore returns eight and leaves s=2.

For a general starting counter c and input x, the two sequential returned values are $x+c+1$ and $x+c+1+c+2=x+2c+3$. The final counter is c+2. This state-transition formula explains why a later apply on the same input five, starting at c=2, returns12 and leaves four.

Replacing step globally by the pure function x+1 would predict seven from two applications, which already fails in the first actual call. The callback's history is a hidden input unless the contract exposes it as state. The first result is deliberately fed into the second callback, but the persistent counter is also carried between them; tracking only one of those flows is insufficient. The explicit sequential interface removes call-order ambiguity, and the small stated values avoid signed overflow.

## PF60 | Reference and value in the same C++ interface

**Full replacement solution.** This is C++17, not C17. The reference parameter x binds to the caller's a object, while y is a separate int parameter initialized with the value of b, seven. The statement x+=y reads a=4 and local y=7, then writes11 into a itself.

Assigning zero to y next changes only that copied parameter object. It does not assign zero to caller b. The final caller values are therefore a=11,b=7; y contains zero just before its invocation ends. Passing an expression as an argument does not by itself determine whether its caller storage is shared: the parameter's declared mode does.

A C pointer interface can achieve access to a caller object too, but requires a pointer declaration, an address argument and an explicit dereference for the write. Its copied pointer parameter is not a C++ reference object that can be explained by silently using this syntax in C. Reference binding also does not imply a fresh copy of a; x is a name designating that caller object throughout its valid binding. No lifetime or overflow issue arises for the given live objects and small values.

## PF61 | Two C++ references can designate one object

**Full replacement solution.** Both arguments are the same live caller object a, and both parameters are references. Thus x and y designate that one object rather than two independent int copies. The first statement adds two to a=4, producing six. The next reads the same updated six through y and triples it, producing18.

The final result is a=18. Reporting distinct outputs six and12 would incorrectly let y read an independent old four. The common mathematical transition is $a\mapsto3(a+2)$, just as for the sequenced aliased-pointer target case, though the C++ reference syntax is different.

The full statements sequence the two writes, so shared designation is permitted here and is not itself an unsequenced-modification error. A non-aliasing assumption would have to be stated separately; ordinary reference parameters do not guarantee it.

Once x is bound, an assignment such as x=y assigns a value to x's current referent; it does not reseat x to a new object. In this exact alias case such a later assignment would simply copy the same target value to itself. References also need a valid lifetime for their referents, a separate requirement examined in PF86.

## PF62 | A value-result alias requires a copy-out rule

**Full replacement solution.** The problem stipulates theoretical value-result semantics. Entry copies caller x=4 into two distinct local parameter objects p and q. The body then gives them values10 and20. The caller's x is not updated by those local body assignments; effects are copied back at return.

If p is copied out first, x becomes10, then q's copy-out overwrites it with20. If q is copied out first, x becomes20 and p's later copy-out leaves10. Thus the final value is20 for p-then-q and10 for q-then-p. Without an order or a prohibition on this alias, there is no unique final-state answer under the stipulated model.

This is neither C value passing nor ordinary immediate C++ reference writes. A reference version would change x while its body ran; an observer at that point could distinguish it from the delayed copy-out model, even if one chosen copy-out order happened to yield the same final integer. Matching one final number does not make the semantics equivalent. The two local parameter identities and the shared copy-out destination must both be represented to explain the ambiguity.

## PF63 | Call by name re-evaluates an expression

**Full replacement solution.** Under the explicitly stipulated mathematical call-by-name model, p is a recipe for evaluating the caller expression i+1 in its caller environment. It is not a stored snapshot of the first numerical result. With i initially three, the first read evaluates that recipe to four.

The body then performs the stipulated mutation of the caller's i, making it four. A second read of p evaluates the same expression again in that updated environment, obtaining five. The returned/read pair is therefore (4,5), with caller i finally four.

For call by value, entry evaluates i+1 once to four and stores that value for p. If the body retains its separately stipulated ability to mutate caller i, that mutation still makes i four, but the saved parameter value remains four on both reads. The comparison pair is then (4,4).

This example depends on a theoretical environment-access rule that the question states explicitly. It is not an inference that an ordinary C callee can access any caller local. Nor is the expression i+1 automatically a writable object suitable for a normal non-const C++ int reference. Re-evaluation of an expression, shared access to an object and copied parameter values are three different passing models.

## PF64 | An immutable argument and two separate bindings

**Full replacement solution.** At module level, x binds to the integer value four. Calling f(x) evaluates that binding and initializes the invocation's local parameter binding x with the supplied object. The two names initially refer to the same immutable integer value, but they belong to different namespaces.

Inside this ordinary Python function, x += 3 computes the integer value seven and rebinds the local name x. It does not mutate the integer four and does not assign the module's x. This argument does not require a freshly allocated integer object: implementations may reuse integer objects, and allocation identity is irrelevant here.

The return expression is evaluated using the local value seven, so 7 times 2 is fourteen. Returning that result terminates the invocation; the caller assigns it to y. Thus the final module bindings are x = 4 and y = 14. There is no printed output in the supplied program.

For an arbitrary integer argument u, this function's returned map is 2(u+3), while the caller's original binding is preserved. Replacing the call statement by x = f(x) would explicitly rebind the caller's x to fourteen. That different caller assignment, rather than a different parameter-passing rule, would explain the changed state.

## PF65 | Mutation survives a later local rebinding

**Full replacement solution.** Give the initial list the identity A. Before the call, module x refers to A = [2]. At entry the local parameter a also refers to A. The statement a.append(7) changes the contents of that one list to [2,7]. Because x still refers to A, that change is observable through x.

The next statement a = [99] constructs a different list, B, and changes only the local binding a to refer to B. It does not redirect module x. The return therefore supplies B, and the caller's y refers to B. Final observations are x = [2,7], y = [99], and x is y is false.

The two effects must be followed in statement order. Describing the function as either simply modifying its argument or simply copying it hides the essential distinction: its first statement mutates a shared object; its second statement rebinds a local name. The rebinding does not reverse the earlier append.

For comparison, assigning a = [99] before performing a.append(7) would mutate B instead, leaving A equal to [2]. An object-identity diagram therefore predicts more than a final-value table: it tells exactly which later mutations each caller name can observe.

## PF66 | A returned alias exposes subsequent mutations

**Full replacement solution.** Initially x refers to a list A containing [1]. The parameter a receives a binding to the same A. Appending five changes A to [1,5], and return a supplies a reference to that very list, not a fresh copy. The assignment to y gives the caller a second name for A.

The later statement y.append(9) mutates A again. Both x and y consequently display [1,5,9], and the identity test x is y is true. There are two caller bindings but only one list object involved in these operations.

Returning from f ends its local parameter binding; it does not end the returned list's lifetime while caller references still keep that object reachable. Do not transfer the C rule about returning a pointer to an automatic local integer to this managed-object example.

If f instead returned list(a), its append would still have changed the original to [1,5], but y would refer to a distinct outer list. Appending nine through y would then leave x unchanged. This comparison separates the mutation performed before return from the alias relationship created by the returned value.

## PF67 | An outer copy is not a recursive copy

**Full replacement solution.** The original list A contains [2,3]. At entry a refers to A. The expression list(a) creates a new outer list B with the same two element references, so b refers to B while a and caller x continue to refer to A. The append of eight changes B alone.

The returned B becomes y. Final values are x = [2,3] and y = [2,3,8]; x is y is false. This is a shallow copy. Its outer-list independence suffices for the particular append in this question, and the integer elements are immutable.

The distinction matters if the elements are mutable. With an input [[2],[3]], copying the outer list still leaves its inner lists shared. Appending a new element to the copied outer list remains independent, but b[0].append(8) would mutate a shared inner list and be observable through the original outer list too.

Therefore a correct copying argument identifies both the operation's target and the copied graph depth. The word copy alone cannot establish isolation of every reachable object. For the actual code, only a new outer container is needed to explain why the caller's two-element list does not acquire the appended eight.

## PF68 | A default is evaluated at definition time

**Full replacement solution.** Executing def f(x=k) while module k is four evaluates the default expression immediately and saves its resulting value in the function's defaults. It does not save the expression k as a recipe to reevaluate at each omitted-argument call.

The later assignment k = 9 changes the module binding, but it does not replace the saved default. Consequently a = f() binds the parameter x to the saved four and returns four. The explicit call b = f(k) evaluates the current module k, supplies nine, and returns nine. The final pair is therefore (a,b) = (4,9).

No body statement in this example modifies either value. The difference is established entirely by the times when the two argument values are obtained: definition time for an omitted argument's default, and call time for the explicit argument expression.

If the same def statement were executed again after k became nine, it would create a new function with a newly evaluated default of nine. That is different from merely calling the existing function again. This timing rule also explains mutable-default accumulation, although an immutable integer default cannot itself be appended to or changed in place.

## PF69 | Persistent default, independent returned snapshots

**Full replacement solution.** When the definition executes, its default [] creates one list D. The first call f(2) omits a, so a refers to D. Appending two makes D = [2]. The expression list(a) then creates a separate outer snapshot R1 containing [2], which is assigned to r1.

The second call f(5) again omits a and therefore reuses D, now already containing two. Its append produces D = [2,5]. Returning list(a) creates another snapshot R2 containing [2,5]. Thus r1 remains [2], r2 is [2,5], and r1 is r2 is false.

Three list identities matter: the persistent default and the two returned snapshots. The later mutation of D does not append to R1. Omitting this distinction would lead to the incorrect prediction that both returned values end as [2,5].

If the return statement were return a instead, both caller names would refer to D and both would display [2,5] after the second call. Conversely, constructing a fresh list in the body for every omitted argument would eliminate accumulation itself. Copying the return and replacing the default are two different repairs with different observable contracts.

## PF70 | An explicit list does not reset the saved default

**Full replacement solution.** Label the definition-time default list D and the explicitly supplied [9] list E. The first call f(1) uses D, appends one, and returns a snapshot [1] for r1. D now contains [1].

The middle call f(7,[9]) binds a to E. It appends seven to E, giving [9,7], and returns a separate snapshot for r2. Nothing in this call assigns to or clears D; supplying an explicit argument temporarily chooses a different object for that invocation.

The final call f(2) omits a and selects D again. Its earlier one is still present, so D becomes [1,2], and r3 receives that snapshot. The final values are r1 = [1], r2 = [9,7], and r3 = [1,2]. The three returned outer lists are distinct.

A useful trace records a selected-object column before each append: D, E, D. A trace recording only parameter spelling a loses the identity information and can wrongly treat the explicit argument as a new default. Definition-time storage belongs to the function object; per-call argument binding decides whether a particular call uses that storage.

## PF71 | A sentinel creates fresh omitted-argument storage

**Full replacement solution.** The saved default is None. On the first omitted-argument call, a is None is true, so the body executes a = [] and obtains a fresh list A. After appending one, it returns A = [1] to r1.

The second omitted-argument call starts with None again. The body creates a different list B, appends two, and returns B = [2] to r2. Thus r1 = [1], r2 = [2], and r1 is r2 is false. Identity is tested by is; it should not be confused with the separate value-equality operator ==.

The test specifically asks whether the supplied value is the sentinel None. A condition such as if not a would also replace an explicitly supplied empty list, changing the interface's intended behavior. With the identity test, an explicit empty list is used and mutated as provided.

This idiom guarantees a fresh outer list for each call that chooses the omitted/None path. It does not automatically copy explicitly supplied lists or recursively duplicate their elements. Those are additional contract decisions. The repair removes shared omitted-argument accumulation without claiming that every call is isolated from every caller-owned mutable object.

## PF72 | A local classification precedes the first read

**Full replacement solution.** The assignment x = 3 anywhere in this ordinary function body makes x local to the entire function block, because the body has no global or nonlocal declaration for that name. This classification is determined from the function's binding operations, not by waiting until execution reaches the assignment.

At the earlier print(x), the local x has not yet received a value. Python raises UnboundLocalError while evaluating the print argument. The global x = 8 is not selected as a fallback, and no eight is printed by this statement. The subsequent assignment is not reached, and the call does not return a normal numeric result.

This is not the C declaration-point rule. In a C block, an outer name can remain visible before a later inner declaration begins its scope. Python's ordinary function-block classification makes the earlier read local too.

If reading and changing the module binding is intended, an explicit global x declaration changes the binding rule. If a separate local is intended, giving it a distinct name avoids the collision. Neither repair should be silently applied when answering the original code: the required outcome is the exception before output.

## PF73 | An explicit global assignment selects the module binding

**Full replacement solution.** The global x declaration tells this function that uses and assignments of x address the module namespace binding. It does not create a new invocation-local x and does not search arbitrary active callers for a variable with that spelling.

With module x initially eight, evaluating x += 3 obtains eleven and rebinds that module name to the integer value eleven. The return reads the same updated binding, so r is eleven and module x is eleven after the call. There is no printed output in the supplied body.

The immutable integer itself has not been modified. What changes is the chosen namespace binding. This distinction is compatible with PF64: both examples compute a new integer value, but PF64 assigns a local parameter name whereas this explicit global declaration targets the module name.

If an unrelated caller had a local x equal to one hundred, that local would remain one hundred. Global means the defining module namespace under the ordinary Python rules, not dynamic access to whichever caller happens to be active. The declaration therefore changes name resolution, rather than changing integers into mutable objects or turning all argument passing into reference passing.

## PF74 | Separate factory invocations retain separate environments

**Full replacement solution.** Calling make(4) creates an enclosing binding k with value four and returns a function whose free name k resolves to that retained environment. Calling make(9) creates another invocation environment, with a different k binding containing nine.

Accordingly a(3) computes 3 + 4 = 7 and b(3) computes 3 + 9 = 12. The same nested source definition is executed by both factory calls, but the returned functions retain different environments. Equality of source text does not merge their bindings.

The environment can remain reachable after the factory's ordinary execution has finished. That managed lifetime is why the returned function can still read k. It is not analogous to safely dereferencing a C pointer to an expired automatic local; the two languages provide different lifetime mechanisms.

An environment diagram should draw one returned function pointing to each retained k cell. Drawing both functions toward a single cell containing the most recent nine would incorrectly predict twelve for both calls. Conversely, closure creation does not mean every captured value is forever a snapshot: a shared retained binding can later change through nonlocal, as the counter example demonstrates.

## PF75 | Lexical lookup does not use a caller's shadowing local

**Full replacement solution.** The function f is defined at module level and reads the module x = 10. The function g creates its own local x = 3, but that invocation environment is not f's lexical parent merely because g calls f.

Inside g, f() therefore returns ten. Only after this return does g evaluate the addition using its own local three. The result is 10 + 3 = 13. Module x remains ten and g's local binding ends with that invocation.

A correct trace has two different x identities. The helper's read follows the lexical chain from f to the module; the pending addition follows g's local binding. Merging these identities gives the tempting but incorrect answer six.

The call tree answers which invocation is waiting for another. The environment chain answers where a name is resolved. They often overlap in simple examples but are not the same data structure. Passing three explicitly as an argument to a suitably defined helper would change its input; merely choosing the same local name in the caller does not.

## PF76 | A nonlocal counter updates a retained cell

**Full replacement solution.** One call to make creates an enclosing n initialized to zero. Its returned next_value function declares nonlocal n, so reads and assignments of n use that enclosing binding rather than a new local binding or a module variable.

The first call adds two to zero and returns two. The second starts with the retained two, stores four, and returns four. The third stores and returns six. Thus the observed sequence is (2,4,6), and the retained cell ends at six.

For call number j starting from the factory's zero, induction gives n = 2j after the call: the base j = 0 is zero, and each transition adds exactly two. This reasoning counts calls to the same returned closure. Calling the factory again creates a separate cell initialized to zero and a separate sequence.

Without nonlocal, an assignment to n in the nested function would classify n as local there; a preceding n read in n += 2 would then fail with UnboundLocalError. The declaration is therefore essential to this program's state contract. It identifies a binding to update; it is not a claim that all nested functions automatically share one process-wide counter.

## PF77 | Loop-created functions can share one late-read cell

**Full replacement solution.** During one invocation of the builder, the loop repeatedly updates the same local binding i. Each lambda reads that free binding when it is later called; its body does not evaluate i while the lambda is being appended.

After range(3) finishes, that shared binding holds two. Calling the three saved functions afterwards therefore gives [2,2,2]. They are distinct function objects, but their free-name lookups reach the same retained cell. Three function identities do not imply three independent stored values of i.

A step table separates creation from evaluation: the first, second and third functions are created while i is zero, one and two respectively; all three later evaluations occur after i is two. The creation-time values explain why a snapshot intuition is attractive, but they are not what this code saves.

If each lambda were called immediately during its own iteration, the observed timing would differ. The stated program saves them and calls them after the loop. Likewise, a default-argument snapshot is an explicit different definition, not an alternative interpretation of this one. The answer depends jointly on shared binding identity and time of lookup.

## PF78 | A default parameter records each iteration's value

**Full replacement solution.** In lambda i=i: i, the i on the right of the equals sign is evaluated when that lambda expression executes. It reads the enclosing loop's current value and saves it as that new function's default. The i on the left declares the lambda's parameter; its body reads that parameter.

Across the three iterations, the saved defaults are zero, one and two. Calling each lambda with no argument uses its own default and produces [0,1,2]. These bodies do not need to read the loop variable as a free name, so the previous shared-late-binding argument does not apply.

The repair changes the function's interface: callers can explicitly override the parameter. For example, any of these particular lambdas called with nine returns nine. It is therefore precise to describe the values as saved defaults, rather than claiming an inaccessible immutable capture mechanism.

For mutable objects, saving a default saves a reference to the current object, not a deep snapshot of its entire future state. The integer iteration values here are immutable, making the value result straightforward. This qualification prevents transferring the integer example into an incorrect claim about independent nested lists.

## PF79 | Python fixes the order of these argument evaluations

**Full replacement solution.** Python evaluates the left argument expression first. With the counter initially zero, the first next_value call returns one and leaves the counter at one. The right argument is then evaluated; its next_value call returns two and leaves the counter at two.

The subtraction helper receives the ordered pair (1,2), so its result is 1 - 2 = -1. The final counter is two. A compact trace is counter zero, left result one, counter one, right result two, counter two, subtraction result minus one.

This is a single specified evaluation order for the printed Python code. It must not be answered using the C17 rule for two separately completed next function bodies, where either argument call may occur first. Conversely, the C17 distinction between direct unsequenced increments and called-body executions does not create additional Python outcomes here.

Changing subtraction to addition would make both possible C17 argument orders agree numerically, but would not make C17's order specified. This Python example demonstrates why the language label must precede arithmetic: the same apparent composition of stateful helpers can have a different set of permitted results under different language contracts.

## PF80 | Duplicate binding fails before the body executes

**Full replacement solution.** The positional argument one first binds the ordinary parameter a. The keyword a=3 then attempts to supply a second value for that same parameter in the same invocation. Python's argument-binding rules reject the call with TypeError.

There is no ordinary returned sum. In particular, the keyword does not overwrite the positional value to produce five, and the positional value does not silently win to produce three. The default b=2 matters only for a valid call whose b is omitted; it cannot repair a duplicate a.

The argument expressions in this simple example are constants, so they introduce no separate side effects to report. The function body is not entered, and its addition is not evaluated. With more elaborate argument expressions, argument evaluation and binding failure would need separate consideration rather than a blanket claim that nothing at all can happen before TypeError.

Valid comparisons clarify the interface: f(1) returns three, f(a=3) returns five, and f(1,b=3) returns four. These are distinct calls, not permissible reinterpretations of f(1,a=3). Always finish parameter binding before attempting to trace body arithmetic.

## PF81 | Parameter kinds constrain the binding map

**Full replacement solution.** In def f(a, /, b=2, *, c=3), the slash makes a positional-only. The star makes c keyword-only. The intervening b is an ordinary positional-or-keyword parameter with default two.

The supplied call f(1,c=7) is valid. Its binding map is a = 1 from the positional argument, b = 2 from its default, and c = 7 from the keyword argument. Substituting into the body gives 100 times 1 plus 10 times 2 plus 7, which is 127.

The punctuation is interface syntax, not division or multiplication performed on the parameter values. It does not introduce extra parameters named slash or star. Reading it as a binding table avoids confusing the eventual arithmetic with declaration syntax.

For comparison, f(a=1,c=7) is invalid because a must be supplied positionally, while f(1,2,7) is invalid because c cannot receive a third positional argument. A valid alternative f(1,b=4,c=7) returns 147. State whether a call binds successfully before deriving a numerical result; a binding error never produces the body result as a fallback.

## PF82 | Evaluating an expression does not return it

**Full replacement solution.** The call f(5) binds x to five and evaluates the expression statement x*x. That computation obtains twenty-five, but the statement does not assign, print or explicitly return its result. Its temporary result is discarded.

Execution then reaches the end of the ordinary Python function, which implicitly returns None. Thus r is None. The program does not print twenty-five, and r is neither twenty-five nor zero.

An interactive shell may display a bare expression typed directly at its prompt, but that display convention does not turn expression statements inside an ordinary function into implicit returns. The body must say return x*x to supply the square to its caller, or print(x*x) to produce output while still normally returning None.

This case distinguishes three observables: an internally evaluated value, an output event, and the call's returned object. A solution reporting only that the function computes twenty-five leaves the requested caller value unanswered. Conversely, reporting None should not imply that the multiplication was skipped; the multiplication ran, and its value simply was not used by a return.

## PF83 | Composition retains the supplied function bindings

**Full replacement solution.** compose receives two function objects in local parameter bindings f and g, then returns a lambda whose body calls the saved g first and passes that result to the saved f. In the stated call, g is plus2 and f is square.

Applying the returned function to three first obtains plus2(3) = 5, then square(5) = 25. The result is twenty-five, not eleven: eleven would come from adding two after squaring three, which reverses the composition.

The module assignment f = compose(square,plus2) does not make the lambda recursively call the module's new f. Its free f resolves to the retained compose-parameter binding containing square. The module f and the enclosing parameter f are different bindings despite their identical spelling.

For any integer u in Python's ordinary integer model, the returned map is (u+2) squared. The lambda invocation remains active while its two helpers are called sequentially; plus2 completes before square begins. A composition diagram should therefore show both the lexical links to retained function objects and the data path three to five to twenty-five, rather than drawing the helper bodies as simultaneously executing.

## PF84 | Sum of persistent triangular returns

**Full replacement solution.** Let s start at zero and make the sequential helper calls with increments 1,2,...,n. After the kth call, persistent state is the sum of the first k integers, so its returned value is k(k+1)/2. Induction proves this: the previous state (k-1)k/2 plus k equals k(k+1)/2.

The caller sums these returned states, rather than summing only the supplied increments. Its total is

$$\sum_{k=1}^{n}\frac{k(k+1)}2=\frac12\left(\frac{n(n+1)(2n+1)}6+\frac{n(n+1)}2\right)=\frac{n(n+1)(n+2)}6.$$

At n = 4 the helper returns 1,3,6,10 and the caller total is twenty. The persistent state itself ends at ten, not twenty. State and accumulated returned output are different quantities.

The formulas are mathematical identities. On an explicitly assumed signed int32 implementation, the triangular state fits through n = 65535, but the sequential sum of returns fits only through n = 2343. The latter gives 2146453540; n = 2344 gives 2149201880, beyond INT_MAX. Evaluating the literal int product n*(n+1)*(n+2) before dividing by six has yet another limit: its numerator already exceeds INT_MAX at n = 1290. Safe final mathematical output does not justify unsafe evaluated intermediates. Later calls also require accounting for any nonzero initial persistent state.

## PF85 | Two counters retain two independent cells

**Full replacement solution.** Each factory invocation initializes its own n to zero and returns a function that increments and returns that retained binding. Let A be the cell retained by counter a and B the cell retained by counter b. Both begin at zero, but they are distinct cells.

In the stated sequence a(), a(), b(), a(), the first call changes A to one; the second changes A to two; the third changes B to one without changing A; the fourth changes A to three. The returned sequence is therefore [1,2,1,3]. Final retained state is A = 3 and B = 1.

Resetting n on every counter call would instead produce repeated ones, while using one module-wide n would produce [1,2,3,4]. Neither model matches separate factory-created environments. The counter source is shared, but the enclosing state identities are not.

The stem describes the factory in prose, so a test reconstruction must be labelled as a reconstruction rather than the exact printed program. The semantic answer follows directly from the stipulated per-factory binding and increment rule; a diagram should distinguish the two retained cells and highlight only the cell selected by each call.

## PF86 | Returning a reference does not preserve an automatic local

**Full replacement solution.** The ordinary automatic local exists only during its block's lifetime. An int& return can bind a caller reference to that local, but returning from the function ends the local object's lifetime. The caller is then left with a dangling reference and cannot safely read the former integer through it.

The former stored number is not a guaranteed returned value. A particular run appearing to read that number does not establish defined behavior; later storage reuse is only one possible symptom, not the reason the program lacks a valid referent.

This is not C++ lifetime extension for selected temporary-binding contexts. Binding a reference to an ordinary automatic local and returning that reference does not extend the local's lifetime. Nor should the C rule about an indeterminate pointer value be quoted as the definition of every C++ reference rule.

Returning int by value copies the result into the caller's value flow and avoids this dangling-local problem. Returning a reference to a caller-owned object can be valid if that object outlives all uses. Returning a reference to static storage can also preserve lifetime, but introduces shared-state behavior across calls. Each alternative needs its own lifetime and effect contract; changing only the return type spelling cannot supply one.

## PF87 | An array-shaped parameter is adjusted to a pointer

**Full replacement solution.** In the C17 parameter declaration void f(int a[10]), a is adjusted to a pointer parameter. The function does not receive a new ten-element array object, and the written ten is not an automatically passed runtime length.

Consequently sizeof a inside the function measures its pointer parameter's type, not ten times sizeof(int). Its numerical size depends on the implementation; neither four nor eight bytes is universally implied. The caller's array object remains where the caller created it, and valid element writes through a can affect that original object.

A length-aware interface must communicate the usable length separately, for example with a size_t parameter and a matching access precondition. The ordinary a[10] syntax should not be confused with the distinct C parameter syntax a[static 10], which explicitly imposes a minimum-access requirement on arguments to calls of that function.

The rule is about parameter adjustment. sizeof on an actual ten-element array object in a scope where its array type is retained is a different expression and does yield ten times its element size. Establish the declaration context before applying a memorized array-size formula.

## PF88 | Equal returns do not establish observational equivalence

**Full replacement solution.** Starting from saved state zero, a pure helper returning seven twice produces returned sequence [7,7] and leaves state zero. A stateful helper that increments saved state before returning the same seven also produces [7,7], but ends at saved state two.

The result sequence is equal while the state transition is different. If callers can later observe that state, replace the helper, or invoke another operation that depends on it, the two implementations are distinguishable. A value-only postcondition is therefore insufficient to justify treating the stateful helper as pure.

Represent the contracts as transformations of both value and state: the pure helper maps state s to returned seven with unchanged s; the other maps s to returned seven with state s+1. Composing two calls gives final s versus s+2. This simple algebra exposes the difference without depending on an implementation's stack layout.

An equivalence argument must first state its observables: return values, permitted external effects, exceptions or failures, and termination as appropriate. If a deliberately restricted observer cannot access the state, a narrower equivalence may be proved under that restriction. It cannot be silently promoted to an unrestricted claim that the helpers behave identically.

## PF89 | The same argument can initialize an alias and a copy

**Full replacement solution.** C++ parameter a is an int reference, so f(x,x) makes a designate the caller's x. Parameter b is passed by value and becomes a separate int initialized to the same original three. Both argument evaluations merely read x, so there is no conflicting argument-side modification to resolve.

The first body statement a += b reads three through a and three from b, then writes six into the caller's x. The second statement b += a reads the updated six through a and adds it to b's still-original three, obtaining local b = 9.

After return, caller x is six. The local b value nine is not copied back and is not a returned result because the function returns void. A correct final report distinguishes the surviving caller value six from the final pre-exit local value nine.

If both parameters were references to x, the second update would instead double the shared six to twelve. If both were values, x would remain three. These comparisons show why argument spelling alone cannot identify the passing model: the declaration determines whether each parameter is a new object or an alias to an existing one.
