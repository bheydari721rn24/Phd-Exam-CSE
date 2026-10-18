## From a language model to an examination proof

### Separate four stages before tracing a call

A reliable solution first evaluates argument expressions, then determines their parameter bindings, then executes body statements, and finally resumes the caller's pending continuation. These stages answer different questions. An argument can have a side effect before the callee body begins; a duplicate Python binding can prevent the body from beginning at all; a valid body can return a value that the caller subsequently discards.

For C17, an ordinary scalar parameter is a new object initialized from the argument value. For a pointer parameter, the newly created object holds a pointer value, and that value may designate an existing caller object. For a C++ reference parameter, the parameter designates its referent. For Python, the invocation's local parameter name binds to the supplied object. These are language-specific rules. One sentence saying that a function changes an argument cannot replace them.

Use a trace with an identity column as well as a value column. If p and q both designate A, write one row for A rather than two falsely independent rows named *p and *q. If a Python name is rebound, change its link; if its list is mutated, change the contents at the link's target. If a closure retains a cell, keep that cell after the factory returns. Identity is the structure on which numerical substitution operates.

### Derive an alias transformation instead of guessing its output

For the two complete statements `*p += 2; *q *= 3;`, distinct targets with initial coordinates u and v undergo

$$F(u,v)=(u+2,3v).$$

An aliased target has only one independent coordinate. The second statement reads the result of the first, so its transformation is

$$G(u)=3(u+2)=3u+6.$$

Reversing these full statements gives a different map, $H(u)=3u+2$. Their outputs differ by four for every mathematical u. In a machine implementation, all additions and products must also be representable. Equal initial numerical contents in two distinct objects do not make the arguments aliased; identity, rather than equality, chooses between F and G.

A repeated caller assignment composes the returned or mutated map. For $u_{k+1}=3u_k+6$, induction gives

$$u_k=3^k u_0+6\sum_{j=0}^{k-1}3^j=3^k(u_0+3)-3.$$

This formula applies to the stipulated sequential aliased update. It is not valid for a call that merely changes a scalar parameter and discards its result. At zero calls it returns the original state, and at one call it agrees with the direct trace. Those boundary checks catch many incorrect recurrence translations.

### Prove maximality, preservation and termination separately

Suppose positive inputs a and b are searched for their greatest common divisor by testing candidates from min(a,b) downwards. A successful divisibility test proves that the returned candidate is a common divisor. It does not by itself prove greatestness. The required invariant says that every larger candidate up to min(a,b) has already been rejected.

At initialization the excluded range is empty. On a failed test, rejecting the current d and decrementing it expands the excluded range by exactly that rejected value. At a successful test, the invariant rules out every larger candidate. Termination follows because the candidate decreases through positive integers and one divides both positive inputs. An early return must satisfy the same postcondition as a final return; proving only the loop's normal exit is insufficient.

The contract must also state preserved state and allowed effects. A helper can always return the correct gcd while incrementing a global counter. Its numeric postcondition would hold, but a caller cannot infer purity. Total correctness additionally requires termination. In mathematical pseudocode a divergent branch can be stipulated; a concrete C17 example requires attention to the language's qualified permission to assume termination of certain nonconstant, side-effect-free loops. A constant-condition `while (1) {}` has a different relevant contract. See the [WG14 correction to loop paragraph 6](https://www9.open-std.org/JTC1/SC22/WG14/issues/c11c17/issue0436.html).

### Check executed products, including discarded ones

To compute an integer power by repeated squaring, maintain the mathematical invariant

$$r b^e=x^y.$$

For an even e, replace b by its square and e by e/2. For an odd e, first multiply r by b, then perform the corresponding halving and squaring transition. At exponent zero, the invariant yields the returned result r. The complete implementation and step-by-step even/odd proof are in PF52.

The mathematical invariant is not a signed-machine safety proof. With an explicitly assumed int32 and input x = 50000, y = 1, the desired result fits, but an unconditional unused final square computes 2500000000 and overflows. Skip that unused square and verify every product that remains. Similarly, a geometric sum can fit at $2^{31}-1$ while an unnecessarily computed next power $2^{31}$ does not. Formula values, operation order and declared representation must all agree.

### Close the proof with an observation table

Report the returned value, output events, surviving caller bindings and persistent state separately. For a helper that prints five, prints eight and returns eight, an assignment receives eight while the two printed events remain distinct. For a function that evaluates a square but has no Python return statement, the call returns None even though the multiplication was evaluated.

Finally classify the result: one defined value; several permitted outcomes under a stated language rule; an exception or constraint failure; undefined behavior; or a deliberately underspecified theoretical model. A numeric-looking answer to undefined code is not an additional legal outcome. Conversely, an unspecified choice need not change the final numeric answer if both permitted paths agree. This classification, followed by explicit state and domain reasoning, is the reusable method for unfamiliar problems.
