# Functions: individually rewritten teaching solutions

State: review manuscript, not yet integrated into the study-facing edition. Each numbered block replaces the corresponding solution only after the full chapter review. Source-language assumptions belong to the original question and chapter contract. Mathematical equalities do not imply a caller-side assignment.

## PF01 | Two copies and one returned result

**Full replacement solution.** Keep three separate records: the caller's object a, a callee's parameter, and the value returned by that callee. Initially the caller has $a=4$. Evaluating the argument to f reads that four; the local parameter x then represents four and f computes $3\cdot4-2=10$. This invocation ends with result ten. No instruction assigns to the caller's a.

The next invocation binds g's parameter y to the returned ten. Its result is $2\cdot10+5=25$. Only now does the caller store that result in b. The final pair is therefore $(a,b)=(4,25)$. A value can flow through several parameter/result slots without making those slots the same mutable object.

For a general input u, substitution follows the inner-to-outer execution order:

$$g(f(u))=g(3u-2)=2(3u-2)+5=6u+1.$$

Checking the reverse gives $f(g(u))=3(2u+5)-2=6u+13$, so composition order matters. At four, that reversed expression is 37, not 25. A separate caller statement assigning the returned result back to a would change a; this question explicitly has no such statement. In finite C arithmetic, the products, subtraction and addition each need representability checks before the mathematical formula is used as a machine-output claim.

## PF02 | An output inequality through two helpers

**Full replacement solution.** First establish the exact composite, without changing the interface order. The inner helper returns $f(x)=2x+1$; the outer therefore returns

$$g(f(x))=3(2x+1)-4=6x-1.$$

“Between 17 and 41 inclusive” gives two simultaneous bounds, $17\le6x-1$ and $6x-1\le41$. Adding one to all three terms gives $18\le6x\le42$. Dividing by positive six preserves both inequality directions, yielding $3\le x\le7$. Restricting to the specified integer domain gives exactly $\{3,4,5,6,7\}$.

Check inclusion and exclusion explicitly. Inputs three and seven return 17 and 41 respectively, so both endpoints belong. Input two returns 11, below the interval; eight returns 47, above it. Because the affine output increases by six whenever x increases by one, no omitted integer between or beyond those boundaries can be another solution.

The order error is detectable algebraically: $f(g(x))=2(3x-4)+1=6x-7$. It is a different function and produces a different admissible input interval. The solution here concerns mathematical integers; a C version must additionally make every intermediate operation defined, rather than check only the final value's type.

## PF03 | Repeated returned assignment

**Full replacement solution.** The caller explicitly reassigns x after every invocation, so later arguments use the earlier returned values. Number the caller states with $x_0=1$ and $x_{k+1}=2x_k+3$. The first five updates are

$$1\longmapsto5\longmapsto13\longmapsto29\longmapsto61\longmapsto125.$$

To solve the recurrence, find its fixed-point shift. Adding three gives $x_{k+1}+3=2(x_k+3)$. Set $y_k=x_k+3$; then $y_{k+1}=2y_k$ and $y_0=4$. Repeated substitution yields $y_k=4\cdot2^k$, hence

$$x_k=4\cdot2^k-3.$$

The formula includes zero updates: $4-3=1$. It also passes an inductive check: assuming it at k, the next update is $2(4\cdot2^k-3)+3=4\cdot2^{k+1}-3$. At five the result is $128-3=125$, matching the complete trace.

The plus-three term is inserted once per assignment, not once for the entire loop, which is why $2^k x_0+3$ is wrong. If the same pure helper were called five times but all results discarded, the caller would stay at one and every call would receive one. Mathematical growth also warns that a fixed-width signed C implementation eventually needs a bounded input/update-count contract.

## PF04 | A shrinking returned recurrence

**Full replacement solution.** The nonnegative input domain makes division by two equal to mathematical floor division. Updating 83 gives 41, then 20,10,5,2,1 and 0. The seventh call returns zero; the loop then stops and must not make an eighth call just to confirm it.

For a positive initial integer n, after k updates the caller state is $x_k=\lfloor n/2^k\rfloor$. One useful proof of the nested-floor step writes $n=2^{k+1}q+r$ with $0\le r<2^{k+1}$. After division by $2^k$, the floor is $2q+\lfloor r/2^k\rfloor$, whose final term is zero or one. Dividing that integer by two and flooring gives q, exactly $\lfloor n/2^{k+1}\rfloor$.

The state first becomes zero when $2^k>n$. If $2^j\le n<2^{j+1}$, it remains positive after j updates and becomes zero after $j+1$. Thus the call count is $\lfloor\log_2 n\rfloor+1$ for positive n. For n=0, the original guard is already false and there are zero calls; logarithm of zero must not be substituted into the positive-input formula.

Every helper finishes before the next loop iteration invokes another one. Seven total invocations therefore do not create seven simultaneously live helper bodies. This is different from a recursive function that keeps a caller suspended while invoking itself.

## PF05 | Inverse composition with a negative coefficient

**Full replacement solution.** Compute g first, because it is inside f: $g(x)=3x-1$. Applying f to that result gives

$$f(g(x))=-2(3x-1)+7=-6x+2+7=-6x+9.$$

The equation $-6x+9=9$ becomes $-6x=0$, so the unique solution over the reals is zero and it is also an integer. A direct execution check uses $g(0)=-1$, followed by $f(-1)=2+7=9$. Both the intermediate and returned values have now been checked.

Do not reverse the composition: $g(f(x))=3(-2x+7)-1=-6x+20$. Setting that different expression to nine would produce $x=11/6$, which is not a solution to the stated integer problem. Do not reverse equality when dividing by minus six either. Equality remains equality; only the order relation in an inequality reverses under a negative divisor. For example, changing the original condition to $f(g(x))\ge9$ would give $-6x\ge0$, hence $x\le0$.

Finally, nine is a returned value, not evidence that a caller variable named x has changed to nine. Caller mutation depends on an actual assignment or an allowed side effect, neither of which follows from the mathematical notation alone.

## PF06 | A helper called inside a summation

**Full replacement solution.** For nonnegative integer n, the loop indices are $0,1,\ldots,n-1$, exactly n indices. One invocation per index therefore means n total calls, including zero calls when n=0. Returned values are the first n positive odd integers: $1,3,5,\ldots,2n-1$ when n is positive.

Using linearity of the finite sum,

$$S_n=\sum_{k=0}^{n-1}(2k+1)=2\sum_{k=0}^{n-1}k+\sum_{k=0}^{n-1}1=2\frac{n(n-1)}2+n=n^2.$$

There is also an inductive explanation of the square. The empty sum is zero. If the first n odd returns sum to $n^2$, appending the next return $2n+1$ gives $n^2+2n+1=(n+1)^2$. Thus the formula is valid at every nonnegative count, rather than inferred from a few numeric trials.

The proof uses purity: the result at index k is exactly $2k+1$ and does not depend on earlier calls. A persistent internal counter would change that interface and invalidate the same substitution unless its state were included in the specification. The loop's accumulator is another object; the sum appears there only if the caller actually adds the returned values. Total invocations n and maximum simultaneously active helper bodies one measure different resources.

## PF07 | Nested calls and live depth

**Full replacement solution.** Evaluate innermost argument values before starting the body that receives each one. The inner twice is applied to three and returns six. Its body has ended when inc receives six; inc then returns seven and ends. The outer twice now receives seven and returns 14. There are exactly three helper invocations.

Under the chapter's explicitly stated semantic body-activation model, the active helper-body sequence is: inner twice alone; no helper body between returns and the next invocation; inc alone; outer twice alone. The maximum is therefore one, excluding the enclosing caller. The expression's three pairs of call parentheses show dependency nesting, not three simultaneously executing or suspended callee bodies.

The enclosing caller still needs temporary evaluation state, and an implementation may reserve physical storage in other ways. The answer is not a claim about byte-level stack-pointer movement, a particular ABI or a compiler's chosen allocation. It answers the specified count of active helper bodies.

A genuinely different program defines an outer helper whose body calls another helper. The outer invocation has already begun and remains suspended while the inner body runs, so two body activations coexist in that case. That distinction is examined in PF08. Drawing all three argument-expression calls as a recursive activation stack would confuse when their bodies actually begin.

## PF08 | A genuinely nested helper body

**Full replacement solution.** Enter f with parameter three. Its first statement invokes g while f remains active. This first g computes $2\cdot3+1=7$, returns seven, and ends. The f invocation stores that seven in its own y object. Its return expression then invokes g again, now with argument seven, giving $2\cdot7+1=15$. After the second g returns and ends, f adds its stored seven to 15 and returns 22.

The semantic call tree has one f node and two sibling g nodes, for three total invocations. At either g node, f is an active suspended ancestor, so peak helper-body depth is two. The two g activations are sequential siblings and never coexist with each other. Counting the whole call tree as live storage would therefore overcount.

Algebraically, $y=2x+1$, and the second g result is $2(2x+1)+1=4x+3$. Therefore $f(x)=(2x+1)+(4x+3)=6x+4$. Substituting three gives 22, an independent check of the trace. At input zero it gives four, so the returned map is not merely the second g result.

The addition's operand evaluation order does not change this result: reading the local y has no conflicting effect with the pure g invocation. Finite signed C arithmetic still needs every multiplication/addition representable; the algebra alone supplies a mathematical relationship, not an overflow exemption.

## PF09 | The exact common domain of a composite

**Full replacement solution.** A composite is defined only where the inner function is defined and its result belongs to the outer function's domain. Here the inner denominator requires $x\ne2$. The outer call additionally requires $f(x)+1\ne0$. On the already permitted inner domain,

$$f(x)+1=\frac1{x-2}+1=\frac{x-1}{x-2}.$$

Because the denominator is nonzero there, this expression vanishes exactly at x=1. Exclude that point too. For every remaining real input, reciprocating gives

$$g(f(x))=\frac1{\frac{x-1}{x-2}}=\frac{x-2}{x-1},\qquad x\in\mathbb R\setminus\{1,2\}.$$

The rational expression on the right, viewed on its own, is defined at x=2 and equals zero. That does not make the original inner call valid at two: f was undefined before g could receive an argument. The correct answer is the formula together with its inherited domain, not the simplified formula's largest possible standalone domain.

Check a permitted point, x=3: f returns one and g returns one-half; the simplified formula also gives one-half. At x=1 the inner result is minus one, which lies outside g's domain. These two excluded inputs fail for different reasons and should remain separately identified. The question uses exact real functions, not C integer division or floating-point division-by-zero conventions.

## PF10 | A function that counts but does not accumulate caller changes

**Full replacement solution.** At the first call, the caller's a object contains seven. Its value is copied into a new local parameter object x. Executing `x += 4` changes that parameter to 11; it does not redirect the parameter name to a or assign through a pointer. On return, the ordinary parameter object's lifetime ends while a still contains seven.

The second invocation therefore also receives seven, creates another parameter object, changes that object to 11 and ends. Inductively, after every one of the 13 invocations the caller remains at seven. The final answer is a=7 with 13 executed local updates, one in each invocation. Counting those updates is valid work accounting, but adding their increments to a is not.

The incorrect value 59 comes from $7+13\cdot4$, which would describe a different caller-side recurrence. It becomes relevant if the helper returns $x+4$ and the caller repeatedly assigns that result back to a, or if a pointer parameter designates a and the body writes `*p += 4`. Those modifications add a real state-flow path that the original void scalar helper lacks.

The invocations are sequential. They may reuse physical storage in one implementation, but possible reuse does not turn separate abstract parameter objects into a persistent shared counter. The specified seven-to 11 local arithmetic is representable in every standard C int range.

## PF11 | Recursive return values and suspended additions

**Full replacement solution.** The lesson's function returns zero at n=0 and otherwise returns n plus the recursive result at n−1. With input six, the descending argument sequence is six,five,four,three,two,one,zero. Before the base returns, all seven semantic invocations are active: six ancestors wait for their own pending additions and the base invocation supplies the terminating value.

Trace the return direction explicitly. The base returns zero. The n=1 frame resumes and returns $1+0=1$; n=2 returns $2+1=3$; subsequent frames return six,ten,15 and 21. Thus the final result is 21, total invocations seven and peak semantic helper-body depth seven, excluding an external caller.

For general nonnegative n, let S(0)=0 and $S(n)=n+S(n-1)$. Induction gives $S(n)=n(n+1)/2$: the base is zero, and adding n to $(n-1)n/2$ gives $n(n+1)/2$. The invocation count satisfies $C(0)=1$ and $C(n)=1+C(n-1)$, hence n+1. The same chain gives depth n+1 under this semantic activation model.

Counting only the six positive arguments misses the base invocation. Listing return values in descending call order confuses entry with resumption. Physical stack bytes, optimization and machine overflow require separate assumptions; they are not determined merely by these semantic counts.

## PF12 | A machine-safe affine contract

**Full replacement solution.** C evaluates the signed-int multiplication before adding one. Let L and U denote the type's minimum and maximum. Defined multiplication requires $L\le2x\le U$. The subsequent addition additionally requires $L\le2x+1\le U$. Given the first lower bound, adding one cannot fall below L; the decisive strengthened upper bound is $2x\le U-1$. Together, the exact mathematical input interval is

$$\left\lceil\frac L2\right\rceil\le x\le\left\lfloor\frac{U-1}2\right\rfloor.$$

These bounds simultaneously ensure the intermediate product and the final sum are representable. They are inequalities over mathematical integers used to justify machine operations; calculating an already overflowing `2*x` to test whether it is safe would defeat the purpose.

For the explicitly specified two's-complement 32-bit interval $L=-2147483648$, $U=2147483647$, the allowed inputs are $-1073741824\le x\le1073741823$. At the lower endpoint, the product is exactly L and the final result is L+1. At the upper endpoint the product is 2147483646 and the sum is U. The neighboring input below the interval overflows multiplication; the neighboring input above it has product 2147483648 and also overflows multiplication.

Do not assume that every C17 int has that 32-bit representation; the symbolic L/U statement is the portable form. Likewise a wider destination or floating return conversion occurs after this signed expression's evaluation and cannot repair undefined signed overflow in the earlier multiplication.

## PF13 | Lexical scope defeats caller shadowing

**Full replacement solution.** Give the two objects distinct identities before evaluating either body. Let G be the file-scope x object, initialized to 12, and L the automatic x object created by g, initialized to four. The occurrence of x in f's definition is resolved in the lexical context of that definition. It therefore denotes G, not whichever object happens to have the same spelling in a calling function.

Calling f while g is active reads G=12 and returns 13. The other operand in g's return expression reads its own L=4. Thus g returns $13+4=17$. Neither expression writes either object; G stays 12 and L stays four until the latter's invocation ends.

The tempting answer nine uses the caller's local four inside f and would correspond to a dynamic-scope rule. Standard C does not resolve ordinary names by searching the runtime caller chain. A call-stack diagram may show that g is suspended, but that control relation is not a new lexical parent. The addition's operand order is immaterial here because both computations are free of conflicting side effects. This independence should be justified from the bodies, rather than assumed for arbitrary functions with the same call shape.

## PF14 | An inner block changes only its own object

**Full replacement solution.** Initially the outer x contains five. Entering the inner block declares a different automatic object, also spelled x, and initializes it to two. Its `x += 3` reads and writes that inner object, producing five. At this point the two x objects happen to contain the same number, but equal values do not merge their identities.

The assignment to result selects the enclosing result object because the block has no declaration hiding that name. It stores the inner value five into that object. Leaving the block ends the inner x's lifetime; result still contains its copied five, and the outer x is still its original five.

The final `x += result` occurs after the inner scope has ended, so its x again denotes the outer object. It computes $5+5=10$. The final requested values are therefore outer x=10 and result=5. Treating the inner update as a write to the outer x would accidentally give the right intermediate number here, but for the wrong reason; keeping object identities is necessary to transfer the reasoning to other constants. The code never reads result before assigning it, so its lack of an earlier initializer does not affect this trace.

## PF15 | Self-initialization is not an outer copy

**Full replacement solution.** A block-scope declaration's identifier comes into scope after completion of its declarator, before evaluation of its initializer. In `int x = x;`, the right-hand occurrence therefore resolves to the newly declared inner x, not the outer initialized eight. The initializer attempts to obtain a value from that inner object before a usable initialized value has been established.

Consequently eight is not a guaranteed result, and the fragment must not be answered with an invented numeric output. The exact language rules for indeterminate values and trap representations matter when classifying erroneous reads; the safe conclusion needed here is that the program has no portable guarantee that this inner value is an initialized copy of the outer one. No assumption about previous stack contents repairs that missing guarantee.

The outer object still exists and still has eight; the declaration merely hides its name in this scope. A valid repair saves the value before introducing the hiding declaration, for example `int saved = x;` followed by an inner `int x = saved;`, with saved remaining visible. Using a different inner identifier also avoids the issue. Scope resolution must happen before reasoning about arithmetic or random memory patterns.

## PF16 | Two functions have separate static objects

**Full replacement solution.** Label the objects $s_f$ and $s_g$. Each distinct block-scope static declaration creates its own object with static storage duration. Neither has an explicit initializer, so both are zero-initialized before these calls. Repeated invocations use the object belonging to that declaration; the shared spelling s does not unite the two declarations.

The first f changes $s_f$ from zero to one and returns one. The first g changes $s_g$ from zero to two and returns two. The second f changes only $s_f$ from one to two and returns two. Finally the second g changes only $s_g$ from two to four and returns four. The return sequence is therefore $(1,2,2,4)$ and the final stored pair is $(2,4)$.

The calls are in separate statements, so the question supplies the order; this is not a case of unspecified ordering among function arguments. A single shared file-scope counter would be another model with another sequence. Replacing static locals by ordinary zero-initialized automatic locals would also change the answer, because each new invocation would restart its own counter. The numerical trace is small enough that no signed-int overflow occurs.

## PF17 | Automatic reset versus static persistence

**Full replacement solution.** The automatic a is initialized to one whenever the body is entered. The static s is initialized to one only once and keeps its updated value between invocations. Use a two-column state record rather than treating both initializers as either persistent or repeated.

In f(2), local a becomes $1+2=3$ and s becomes $1+3=4$, which is returned. In f(3), a fresh a starts at one and becomes four; the retained s starts at four and becomes eight. In f(−1), the new a becomes zero, so adding it leaves s at eight. Returned values are therefore $(4,8,8)$, with local a values $(3,4,0)$ in the three different invocation objects.

For a supplied sequence of increments $d_1,\ldots,d_k$, provided every signed operation is representable, the persistent value after k calls is $s_k=1+\sum_{i=1}^k(1+d_i)$. This follows because each call contributes its newly computed local quantity, not the previous call's automatic a. Substituting 2,3,−1 gives $1+3+4+0=8$. A negative argument does not reset persistent storage, and the copied parameter d is not itself an assignment to any caller object.

## PF18 | Recursive locals and one shared static

**Full replacement solution.** Start with the single static s equal to zero. The n=3 frame increments it to one and calls n=2; that frame increments it to two and calls n=1; the next increments it to three and calls n=0. The base reads the same shared s and returns three. It has no local t initialization because it exits before that declaration is executed.

On resumption, the n=1 frame initializes its own t to three and returns four. The n=2 frame receives that four in its own t and returns six. The outer n=3 frame receives six and returns nine. Thus the final result is nine and the persistent s is three. There are separate n and t objects in each applicable invocation, but only one s object for the declaration.

More generally, if the static counter starts at c and a nonnegative argument n is supplied, descent performs n increments. The base returns c+n, and ascent adds $1+\cdots+n$. Hence the mathematical result is $c+n+n(n+1)/2$, under representable arithmetic. A second f(3) starts at c=3 and returns 12, not nine. The function's returned map depends on prior state as well as its explicit argument, so modeling it only as a pure function of n loses an essential input.

## PF19 | Returning a value versus returning a local address

**Full replacement solution.** With a value return, the return expression obtains the initialized nine while the local int object is still alive. The callee returns that integer value, which can initialize a distinct live caller object. Ending the callee's local-object lifetime does not invalidate a separately copied integer in the caller.

Returning `&x` instead attempts to communicate a designation of the local storage. It does not transfer ownership of that automatic object or extend its lifetime. When the invocation ends, the local lifetime ends; a caller cannot validly dereference that designation to recover a guaranteed nine. C's rules also make pointer values indeterminate when their pointed-to object reaches the end of its lifetime, so avoiding dereference alone is not a blanket promise that every other use of the dangling pointer is portable.

The diagnostic distinction is therefore copied result versus access to an expired object. A static local has different lifetime, and a caller-owned live target can remain accessible through a passed/returned pointer. Those alternatives need explicit contracts; they do not validate returning the address of an ordinary local. Possible compiler reuse of the same physical bytes is irrelevant to the ended abstract lifetime and must not supply a numeric answer.

## PF20 | Scope is not storage duration

**Full replacement solution.** The declaration is inside a function block, so its identifier saved is visible only in its lexical block scope after the declaration point. An unrelated function cannot refer to that object merely by writing the same spelling. A declaration of another saved there would normally name another object rather than reveal this one.

The static specifier gives this object static storage duration. It is initialized once, exists across invocations and is not recreated every time control enters the declaring function. Thus the two questions have different answers: no unrelated-name visibility, and no per-call re-creation.

Returning a pointer to this initialized static object illustrates why those concepts must remain separate. After return, the object is still alive, so a suitably typed pointer can designate it even though the caller cannot use its hidden identifier directly. Repeated calls can return pointers to that same object; changes through one then become observable through the others. A persistent address does not imply an unchanging value or independent per-call storage.

This reasoning concerns one declaration in one program context. It does not assume thread safety, independent translation-unit copies or an automatic reset policy. Those are additional properties that the word static alone does not provide.

## PF21 | Prototype names do not create caller variables

**Full replacement solution.** Compare the type interfaces: both declarations return int and take two int parameters in the same order. Changing the parameter names from left/right in the prototype to a/b in the definition does not change those types, so the displayed prototype and definition are compatible in this respect.

The names left and right have function-prototype scope in that declaration. They are not declarations of caller variables that remain available after the prototype. At an actual call, argument expressions are evaluated in the caller's environment, their values initialize the definition's separate parameter objects a and b, and the body evaluates `a-b` using those bindings.

For example, calling `mix(9,4)` returns five; declaring caller variables named left or right is unnecessary. Consistently renaming a and b inside the definition leaves this behavior unchanged, provided every reference is renamed consistently and no other binding is captured. Exchanging the parameter positions would instead alter which argument is subtracted from which, even if all types stayed compatible.

Type compatibility also does not promise absence of arithmetic overflow: a particular subtraction still needs a representable result. The question's naming compatibility and a call's value-level safety are distinct obligations. Matching identifier spellings proves neither of them.

## PF22 | File static versus block static

**Full replacement solution.** For a function declared at file scope, static specifies internal linkage. References to that function name within the translation unit designate its internally linked function; an independently compiled unit does not obtain that function as the same externally linked symbol merely by declaring the same spelling.

For an int object declared inside a block, static instead gives the object static storage duration. Its identifier remains block-scoped and the object persists between calls. It would be incorrect to describe this as making a block-local name globally visible. It is also incorrect to infer a parameter-passing mode from either use of the specifier.

A header containing a static helper definition can be included in two translation units, creating distinct internally linked functions. A block-static counter inside each such separately defined function can likewise be distinct. This differs from one externally linked definition with a shared declaration in a header. The distinction follows from identity across translation units, not the text happening to match.

Answer the three questions separately: where a spelling is visible is scope; which cross-declaration entity it identifies is linkage; how long an object exists is storage duration. Function linkage and object duration are related interface design issues, but they are not interchangeable definitions of static.

## PF23 | Two independent targets: case 1

**Full replacement solution.** Label the caller objects U and V, initially four and seven. The parameter p receives a copied pointer value designating U, while q receives a copied pointer value designating V. These parameter objects are separate from the caller targets, and the declared target identities are distinct.

The first full statement reads U=4 and stores $4+2=6$ into U. V is unaffected and still contains seven. The second statement reads V=7 and stores $7\cdot3=21$ into V. Final caller values are $(6,21)$, and the transition for general distinct-target values is $(u,v)\mapsto(u+2,3v)$ whenever the arithmetic is defined.

The second statement does not triple six because q designates V, not U. Nor does copying p prevent its dereference from modifying U: the copied address still designates the original live caller object. Copy semantics for the pointer parameter and shared access to its target are fully compatible facts.

Both six and 21 are representable in every standard C int range. If the objects were aliases, there would be only one current target value and the first write would affect what the second statement reads. That is explicitly the different input model in PF24; it must not be mixed into this distinct-target trace.

## PF24 | One aliased target: case 2

**Full replacement solution.** Both copied pointer values designate the same caller object U, initially four. The parameter objects p and q remain distinct; what is shared is their designated target. The first full statement reads U=4 and writes six. The next full statement reads the updated U=6 through q and writes 18. The final answer is one object containing 18, not a pair of independently surviving six and 12.

In mathematical form, the ordered transition is $u\mapsto u+2\mapsto3(u+2)=3u+6$, provided all signed operations are representable. Reversing the statements would give $u\mapsto3u\mapsto3u+2$, a result smaller by four whenever both traces are defined. This algebra makes the write/read dependency visible.

There is no unsequenced-modification violation in the displayed body: the two changes occur in separate full statements, so the first is completed before the second. A different expression combining conflicting modifications without sequencing could have different language status; aliasing alone does not imply that status.

Applying the distinct-target formula would incorrectly let q read the old four after U was already changed. The correct procedure groups pointer accesses by target identity, then follows the stated sequence of writes. Ordinary compatible int pointers permit this aliasing; no restrictive non-aliasing contract is declared here.

## PF25 | Two independent targets: case 3

**Full replacement solution.** There are two caller objects. The first contains minus two and is designated by p; the second contains five and is designated by q. After `*p += 2`, only the first becomes zero. The second has not been touched and still supplies five to `*q *= 3`, so the final pair is $(0,15)$.

The zero is an arithmetic cancellation in the first object, not a deletion of the second object or its value. Reading zero through q would require both pointers to designate the first object, contrary to the distinct-target premise. The general distinct-object transition $(u,v)\mapsto(u+2,3v)$ gives the same pair on substitution $u=-2,v=5$.

This negative-input example is useful because an incorrect shared-target drawing can make the zero appear to propagate everywhere. It must not: the two writes follow two different designation edges. Conversely the caller still observes both writes even though the pointer parameter objects are copied. What crosses the call boundary is access through those copied addresses, not an automatic mutation of every variable with a similar spelling. All displayed arithmetic remains representable in C17 int.

## PF26 | One aliased target: case 4

**Full replacement solution.** One caller object starts at minus two; p and q both designate it. The first statement replaces that object's value by $-2+2=0$. The second statement therefore reads zero, not the original minus two, and replaces it by $3\cdot0=0$. The one final object contains zero.

The ordered alias transition is $u\mapsto3(u+2)=3u+6$. At u=−2 it gives zero. Reversing the statements instead gives $u\mapsto3u+2$, which would produce minus four at this input. Thus multiplication by zero in the actual second step is the consequence of the first write; it is not a license to reorder the statements.

Do not report two outputs $(0,-6)$: that pair would arise from applying a distinct-target rule to two hypothetical objects initially holding minus two. This question has only one target identity. The sequential read/write trace is defined and contains no conflicting unsequenced modifications because the writes occur in different full statements. Their small intermediate values also avoid signed overflow, so no unspecified numeric outcome needs to be invented.

## PF27 | Local pointer redirection does not redirect the caller

**Full replacement solution.** Before the call, the caller's pointer object r stores the address of a, while a=2 and b=5. Entry creates a separate pointer parameter p with the same address value as r, and q with b's address. At that moment both r and p designate a, but they are different pointer objects.

The statement `p = q` writes only the callee's p object, changing its designation to b. It does not write r because the callee has not received an address designating r. The next `*p = 9` follows p's new value and changes b to nine. Neither statement writes a.

The final caller state is a=2,b=9 and r still designating a. Returning removes the ordinary p/q parameter objects; their disappearance does not undo the already completed write to the still-live b object. A diagram should move the callee p edge while leaving the caller r edge attached to a.

To redirect r through this style of interface, the function needs a way to designate the r pointer object itself, such as an int** parameter receiving `&r`. Copying the value currently stored in r is insufficient. PF28 makes precisely that change rather than relying on a different interpretation of the same code.

## PF28 | Redirecting the caller pointer object

**Full replacement solution.** Here the first argument is `&r`, the address of the live pointer object r. The parameter p therefore designates r, not the integer a directly. The second parameter q contains b's address. In `*p = q`, dereferencing p selects the caller's pointer object r and stores q's address value into it. After this assignment r designates b, while a remains two and b remains five.

The subsequent caller statement `*r += 4` follows that new designation. It reads b=5 and writes b=9. The final caller state is therefore a=2,b=9,r=&b. Pointer redirection and target mutation occur in different statements, and only the latter changes an integer object.

The types explain the two stages: p is int**, `*p` is the int* object r, and `**p` would be the selected int object. Confusing one dereference with two would change the operation being traced. The p parameter is itself still a copied pointer value; C's value passing remains intact. The address that was copied happens to provide access to a caller pointer object, which is why writing through it can redirect r. No lifetime or alignment violation occurs under the stated live-object contract.

## PF29 | A safe swap when both pointers alias

**Full replacement solution.** The temporary-based algorithm first copies `*a` into its independent local saved object. With a and b designating the same initialized caller int U=11, saved becomes 11. Next `*a = *b` reads the current eleven from U and writes eleven back to U. Finally `*b = saved` again writes eleven into U. The final target is unchanged, as a swap of an object with itself should be.

The reasoning extends to every initialized representable int value: only value copies occur, so no addition or multiplication can overflow. Reading U before the self-assignment's store is valid, and the following saved read does not depend on whatever earlier writes occurred to U because saved is another object.

This property is part of the implementation/contract combination, not an automatic property of every code fragment called swap. An XOR-based swap with identical targets normally zeros the object, and an arithmetic swap can both fail under aliasing and overflow. The temporary is useful because it preserves one original value in independent storage until both destination writes have been completed. Valid initialized writable targets are still required; alias safety does not validate null, expired or otherwise invalid designations.

## PF30 | Arithmetic swap is an unsafe general replacement

**Full replacement solution.** For distinct caller objects initially u and v, assuming every intermediate signed expression is representable, the three state pairs are $(u+v,v)$, then $(u+v,u)$, then $(v,u)$. The second statement obtains u by subtracting the still-old v from the saved sum; the third obtains v by subtracting the recovered u from that sum.

With one shared object initialized to six, the first statement instead stores 12 in that object. Both names in the second subtraction now read the same current 12, so the result is zero. Both reads in the third subtraction then read zero, leaving zero. The result is not a swapped six; the original value has been destroyed.

Distinct targets do not eliminate the arithmetic hazard either. For example, a target at INT_MAX and another at one have perfectly representable original values, but their first sum is outside signed-int range. The later mathematical cancellation cannot repair the undefined signed overflow that has already occurred. Therefore the algebraic identity under mathematical integers is a conditional proof, not a safe general C implementation. Temporary-based copying avoids both this overflow operation and the identical-target failure under its normal live-object contract.

## PF31 | Two outputs cannot occupy one scalar object

**Full replacement solution.** At function entry, n and d are independent scalar parameters holding 23 and five. Integer division produces quotient four, so the first output statement stores four into x through q. The remainder expression still uses the unchanged parameter values and produces three; the second output statement stores three into the same x through r. The final caller x is three.

The mathematical division identity is $23=4\cdot5+3$, with $0\le3<5$. That identity is correct, but it describes two different result values. A simultaneous final interface promise `*q == 4` and `*r == 3` cannot hold when q and r designate the same int: after return, both observations read the same final three.

Using a local quotient temporary does not solve this final-state impossibility. The function could correctly calculate both four and three and still overwrite one output with the other. A uniform two-output contract therefore needs distinct valid writable targets, or a different result representation such as two structure members. Exceptional inputs where quotient equals remainder may happen to tolerate aliasing, but they do not validate the unrestricted interface. Here the nonzero divisor and positive small values make both arithmetic operations defined.

## PF32 | An output may alias the original input object

**Full replacement solution.** Separate the caller's n object from the callee parameter also spelled n. Before the body begins, the first argument expression reads the caller's23 and that value initializes the callee parameter. Evaluating the address argument does not change the caller object. Thus regardless of permitted argument-evaluation order, the body starts with its own n=23 and d=5.

The q output designates the caller's n. Writing quotient four there changes that caller object to four, while the callee's copied n remains 23. The next remainder calculation is therefore $23\bmod5=3$, not $4\bmod5=4$. It stores three in the distinct caller rem object. Final caller values are n=4 and rem=3.

This demonstrates legal input/output overlap under the given live-object contract. It differs from PF31 because the two final output targets are distinct. The original input is preserved inside a scalar parameter before either output is written, so overwriting its caller storage does not retroactively change the value already copied. A function that repeatedly reread the input through a pointer could have another alias contract and would require another analysis. Identifier spelling alone cannot establish that such a read occurs here.

## PF33 | Sequential aliases yield an affine recurrence

**Full replacement solution.** Let x be the one shared target value at call entry. The first full statement computes $y=2x+1$ and stores it in that target. The second statement reads the same updated y through both q and p, then stores $y+y=2y$. One entire call therefore implements $T(x)=4x+2$, not a simultaneous-old-state update.

With $x_0=2$, the caller recurrence is $x_{k+1}=4x_k+2$. Repeated substitution yields

$$x_k=4^kx_0+2\sum_{j=0}^{k-1}4^j=4^kx_0+2\frac{4^k-1}{3}.$$

The geometric sum is zero at k=0, so the original state is included. An induction check multiplies the kth expression by four and adds two, giving the same formula at k+1. For the specified initial two, the first three results are 10,42 and 170. The quotient is an integer because $4^k-1$ is divisible by three; it is not an instruction to perform an early truncating division on an unrelated expression.

Both operations in each statement need representable intermediates in C. The formula describes the calls allowed by that safety contract and does not override signed-overflow rules for sufficiently large k. A distinct-target version would obey a two-dimensional state transformation and cannot be substituted for this one-object recurrence.

## PF34 | Const pointer versus pointer to const

**Full replacement solution.** Read the qualifiers from the object being qualified. In `const int *p`, the pointer parameter object p is assignable, but its dereferenced int is accessed through a const-qualified view. Assigning another compatible address to p is allowed; assigning through `*p` is not permitted through that view.

In `int *const q`, q itself is a const-qualified pointer parameter object. Assigning another address to q is prohibited inside the body, but its designated int is not const-qualified by this declaration, so `*q = value` is allowed when the original target is writable. Neither declaration redirects a caller pointer just because the parameter is named p or q.

The premise says the original targets are non-const live objects. Therefore another suitable non-const alias may still modify a target that p can only read. Pointer-to-const does not mean that the target is globally immutable or that no aliases exist. Conversely, casting away const from an actually const-defined object would not make writing that object valid.

Top-level qualification of a parameter object is also distinct from pointed-to qualification when comparing function interfaces. The local const on q controls the parameter object's assignments in its definition; it must not be mistaken for a blanket qualifier on all reachable integers.

## PF35 | Output contract for a maximum and minimum

**Full replacement solution.** First compute the mathematical results from the copied input values: $\ell=\min(u,v)$ and $h=\max(u,v)$. A two-output pointer interface promises that the low target contains the former and the high target contains the latter after return. Both targets must be live, writable, appropriately typed and aligned.

When $u\ne v$, the two desired result values differ. If the output pointers designate the same int, the simultaneous postcondition requires that one object equal two different integers, which is impossible. Computing both values into temporaries before writing ensures calculation correctness but cannot create two distinct final storage locations. The simplest uniform interface therefore requires distinct output targets.

When u=v, aliasing would happen to preserve the equal result, but allowing that exceptional case complicates the contract: it would need either distinct targets or equal requested results. Returning a structure with two ordinary int members provides a simpler value-result interface, with each result stored as its own member. A structure containing pointers instead would not automatically solve target aliasing.

Comparing and copying int inputs avoids the arithmetic overflow pitfalls of expressions such as `(u+v)/2` or subtracting to decide order. The interface should specify the mathematical selection relationship and effects directly, rather than depend on an unsafe arithmetic shortcut.

## PF36 | Two next calls inside a difference

**Full replacement solution.** The C17 question calls next twice, with its counter initially zero, before applying the pure difference body to the resulting argument values. Each next body increments the counter once and returns that new value. Their executions are indeterminately sequenced: one body completes before the other, but which argument's body runs first is unspecified.

If the left argument's next executes first, it returns one and the right returns two. Difference then receives $(a,b)=(1,2)$ and returns minus one. If the right argument's next executes first, it returns one and the left returns two. Argument positions remain fixed, so difference receives $(2,1)$ and returns one. Thus the permitted result set is $\{-1,1\}$ and the final counter is two in both cases.

Do not sort results by execution order and then always assign them left to right; each returned value belongs to its original argument expression. Do not describe these function-body increments as conflicting unsequenced direct argument updates either. Their function-execution sequencing rule is precisely the relevant distinction. Replacing the calls by direct `++counter` argument expressions would require a different C sequencing analysis. The chapter fixes C17; another language version's argument rules must not be substituted without explicitly changing that contract.
