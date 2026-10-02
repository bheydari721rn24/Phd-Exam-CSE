## 13. Thirty-six fully worked problems

Each solution separates the model, the derivation, the result, and the transferable reasoning. Problems marked **course-derived type** use a teaching pattern from the cited course with independently written data and solutions. All other problems are original chapter exercises. Read them as demonstrations; no pre-study test or timed response is required.

### Problem 1. Identify a gate from all four rows

An unknown two-input block has outputs 1, 0, 0, 0 in input order 00, 01, 10, 11. Identify it and find the result when both input pins are driven by x.

**Solution.** The block outputs one only when neither input is one. Therefore its function is (x + y)′, the NOR function. To evaluate tied pins, substitute y = x into the entire equation, rather than guessing that one input has disappeared: (x + x)′ = x′ by OR idempotence. Thus the tied-input block is an inverter. For input zero its output is one; for input one its output is zero, confirming the substitution.

**Transfer lesson.** A gate with tied inputs can have a different effective unary function. The electrical load still includes both input pins.

### Problem 2. Distinguish cascaded NAND from three-input NAND

Compare u = NAND(NAND(x, y), z) with v = NAND(x, y, z). Give the complete output columns and the number of differing rows.

**Solution.** De Morgan gives u = xy + z′; the other function is v = (xyz)′. In binary row order 000 through 111, u has column 1, 0, 1, 0, 1, 0, 1, 1. The column for v is 1, 1, 1, 1, 1, 1, 1, 0. They differ on rows 001, 011, 101, and 111: four rows. The internal NAND complement is applied before the second NAND, so it changes the combining operation after simplification.

**Transfer lesson.** NAND is commutative but not associative. Checking just the all-zero row misses this failure.

### Problem 3. Distinguish parity from exactly-one detection

For three input bits, compare odd parity, even parity, and a detector that outputs one only when exactly one input is one.

**Solution.** Odd parity is x ⊕ y ⊕ z, with one rows 001, 010, 100, 111. Even parity is its complement, with one rows 000, 011, 101, 110. Exactly-one detection is x′y′z + x′yz′ + xy′z′, with one rows only 001, 010, 100. The all-one input is the distinguishing counterexample between odd parity and exactly-one detection. Parity records the weight modulo two, whereas exactly-one detection uses an integer equality test on the weight.

**Transfer lesson.** Two-input XOR suggests an “exactly one” mnemonic that becomes false when generalized to three or more inputs.

### Problem 4. A binary XNOR tree with five leaves

Does any tree of four binary XNOR gates over five independent inputs compute even parity?

**Solution.** Each binary XNOR contributes a constant-one term to the XOR expansion of its output. Substituting through a tree combines all leaf inputs and four such constants. Four copies of one XOR to zero. Therefore the output is the XOR of the five inputs, which is odd parity. At all-zero inputs, the tree outputs zero while a true five-input even-parity XNOR outputs one. Adding one final inverter restores even parity. A different parenthesization cannot change the number of internal gates or the constant contribution.

**Transfer lesson.** Specify whether “multi-input XNOR” means complement of parity or a cascade of binary XNOR cells.

### Problem 5. Read a mixed gate netlist

Let p = NAND(x, y), q = NOR(y, z), and f = OR(p, q). Derive and simplify the output.

**Solution.** First keep each local complement: p = (xy)′ = x′ + y′ and q = (y + z)′ = y′z′. The OR gives f = x′ + y′ + y′z′. Absorption removes y′z′ because every row satisfying it already satisfies y′. Hence f = x′ + y′ = (xy)′. The third input z has no influence on the final stable function, although a physical implementation may still contain a z-driven internal gate and unnecessary switching.

**Transfer lesson.** An input connected somewhere in the drawing need not be in the semantic support of the output function.

### Problem 6. Track bubbles without deleting a branch

A NAND output t = (xy)′ drives two consumers. One consumer computes f = t′z, and the other computes g = t + w. Can the output bubble of the NAND be removed globally because the first consumer has an input bubble?

**Solution.** The first branch does cancel the two complements, giving f = xyz. The other branch requires g = (xy)′ + w. Changing the driver from NAND to AND changes t to xy; then the second consumer would compute xy + w, which is generally wrong. For x = y = 0 and w = 0, the original g is one while the changed g is zero. A redraw of the NAND as an input-bubbled OR preserves both branches. A physical change of the driver requires compensation on the g branch.

**Transfer lesson.** Preserve the value of a shared net when transforming only one of its uses.

### Problem 7. Active-low requests and an active-low alarm

Two request wires <code>r0_n</code> and <code>r1_n</code> are asserted low. An alarm output <code>alarm_n</code> must be low when either request is asserted and high otherwise. Find the simplest Boolean relation between the wires.

**Solution.** Define assertion predicates R₀ = r₀′ and R₁ = r₁′. The alarm assertion predicate is A = R₀ + R₁. Since the alarm wire is active-low, its electrical Boolean level is A′. Substitution gives A′ = (r₀′ + r₁′)′ = r₀r₁. Thus a positive-logic AND of the request wire levels produces the specified alarm wire. The row where either wire is zero yields a low alarm, and the row with both wires high yields a high alarm.

**Transfer lesson.** Derive assertion predicates separately from wire levels; signal names do not perform negation by themselves.

### Problem 8. Change the logic convention of a NAND

A physical block is a NAND under positive logic. All its input and output wires are now interpreted in negative logic. What function does it implement in the new variables?

**Solution.** Let the new interpreted input bits be a and b. Their positive-logic levels are a′ and b′. The physical positive-logic output is (a′b′)′ = a + b. Negative-logic output interpretation complements this level, giving (a + b)′, a NOR. No transistor or wire was changed; only the assignment of logical meaning to voltage levels changed.

If just the output interpretation changed while the inputs remained positive logic, the result would instead be AND. This shows why the complete-convention duality must not be used for a partially changed interface.

**Transfer lesson.** Write the substitution for every changed pin before naming the resulting gate.

### Problem 9. Build an OR using only two-input NAND gates

Use no complemented input sources and no explicit NOT cells.

**Solution.** Generate u = NAND(x, x) = x′ and v = NAND(y, y) = y′. A final NAND gives f = NAND(u, v) = (x′y′)′ = x + y. The construction has three gate instances. The first two can evaluate in parallel, so its depth is two. Under a common NAND propagation bound p, the largest path bound is 2p. Each primary input drives two pins of its tied-input inverter.

**Transfer lesson.** Gate count, depth, and driven-pin count are different quantities even in a very small implementation.

### Problem 10. Prove an AND/OR library incomplete

Assume constants zero and one are available. Can AND and OR alone implement NOT?

**Solution.** Each constant is a monotone function of every primary input, and each primary input is monotone. AND and OR preserve coordinatewise order: replacing an input vector by a larger vector cannot make their outputs decrease. Induction over the acyclic gate order proves every constructed output is monotone. NOT violates this property because its output decreases from one to zero when its input increases from zero to one. Therefore NOT is impossible even with constants.

**Transfer lesson.** A preserved invariant proves impossibility for networks of every size; a failed search of a few small circuits does not.

### Problem 11. Explain the constant-one exception for XOR and AND

Determine whether XOR and AND form a complete library with, and without, an external constant-one wire. **Course-derived type: UCSD Lecture 6, universality examples, pages 6–9.**

**Solution.** Without one, every primary input is zero at the all-zero vector. XOR and AND both output zero on zero inputs. Induction therefore gives zero at every internal net, so no network realizes NOT at that vector. A constant-zero source does not break this invariant.

With one available, x ⊕ 1 supplies NOT. Having AND and NOT supplies OR through (x′y′)′. These operations implement every SOP truth-table construction, so the augmented library is complete. This constructive proof also identifies exactly where the extra resource enters.

**Transfer lesson.** Always include constant availability in a completeness claim.

### Problem 12. Why XOR, NOT, and constants are insufficient

Show that no network of these elements realizes xy.

**Solution.** Every primary input and constant has an affine algebraic normal form. XOR adds affine forms, possibly canceling coefficients. NOT adds the constant one, preserving affineness. By induction, any output is a constant XOR a subset of the primary inputs. With two inputs, testing the AND rows 00, 01, and 10 forces the constant and both linear coefficients to zero. The resulting affine function is zero at 11, while AND is one there. Thus no such network realizes AND.

**Transfer lesson.** “Many combinations are possible” is not the same as universality. Algebraic structure can forbid an entire class of functions.

### Problem 13. Classify a candidate single universal binary gate

A gate outputs one at 00 and zero at 11. Does that alone prove it universal?

**Solution.** Those corner values are necessary to escape zero-preservation and one-preservation, but they leave four possibilities. If the middle rows are 1, 1, the gate is NAND. If they are 0, 0, it is NOR. If they are 0, 1, the output is y′; if they are 1, 0, it is x′. A complemented projection has only one effective input. Cascading such gates still cannot combine two independent primary signals into AND. Therefore only the first two possibilities are universal under the specified no-constant, tied-input, unrestricted-fanout model.

**Transfer lesson.** Necessary conditions are not sufficient; finish the remaining-case analysis.

### Problem 14. A four-input strict-majority voter

Design a positive output for at least three asserted inputs. Derive both SOP and POS, then give NAND and NOR mappings. **Course-derived type: Cambridge Examples Paper, questions 4–5, page 2.**

**Solution.** Each possible triple of asserted inputs gives a product: f = xyz + xyw + xzw + yzw. Any three ones satisfy one product, and four ones satisfy all four. Fewer than three satisfy none.

The dual POS is f = (x + y)(x + z)(x + w)(y + z)(y + w)(z + w). Every pair-sum is one exactly when no pair of inputs is simultaneously zero. That condition is equivalent to having at most one zero, hence at least three ones.

A NAND mapping uses four three-input NANDs followed by a four-input NAND: five gates. A NOR mapping uses six two-input NORs followed by a six-input NOR: seven gates. These counts assume the large gates exist in the library, positive output is required, and no input inversion is needed. They are construction counts, not minimum proofs under a two-input-only constraint.

**Transfer lesson.** Translate the specification before minimizing, and attach the fan-in assumptions to every gate count.

### Problem 15. A two-input NAND-only selector

Implement f = s′x + sy and prove its function. **Course-derived type: Stanford reader, exercise 3–6 on page 45, selector implementation and verification.**

**Solution.** Generate sn = NAND(s, s). Next form p = NAND(sn, x) and q = NAND(s, y). Their outputs are the complements of the two selected products. The last NAND gives (pq)′ = s′x + sy. With s = 0, the first product becomes x and the second zero; with s = 1, they become zero and y. This two-case proof verifies all eight stable input rows because x and y remain arbitrary in each case.

There are four gates. The select-complement branch has three NAND stages; the direct select and either data input have shorter paths. If s′ is already provided, the construction uses three new gates, but its incoming timing must still be specified.

**Transfer lesson.** A cofactor proof can verify a circuit more efficiently than enumerating every row, while timing remains a separate obligation.

### Problem 16. NOR mapping of a POS with a complemented literal

Implement f = (x + y′)(z + w) using NOR gates only, assuming only uncomplemented primary inputs are supplied.

**Solution.** First generate <span class="math-inline">yn = NOR(y, y)</span>. Then use <span class="math-inline">p = NOR(x, yn) = (x + y′)′</span> and <span class="math-inline">q = NOR(z, w) = (z + w)′</span>. Finally <span class="math-inline">f = NOR(p, q) = [(x + y′)′ + (z + w)′]′ = (x + y′)(z + w)</span>. The construction uses four gates, not three, because the complemented literal is not free. Its longest path from y has three stages; paths from x, z, or w have two.

**Transfer lesson.** “Two-level POS mapping” may exclude input inversions in a textbook diagram, whereas a physical delay calculation cannot exclude them.

### Problem 17. Correct a three-input NAND decomposition

Only two-input NAND cells are available. Build (xyz)′ and verify why the naive two-gate chain fails.

**Solution.** Form t = NAND(x, y), u = NAND(t, t), and f = NAND(u, z). The middle tied-input gate restores u = xy, so f = (xyz)′. This is three cells and depth three on the x/y paths. The naive chain produces NAND(t, z) = xy + z′. At x = y = z = 1, that expression equals one while the required function equals zero.

The correction is not merely adding a delay element: it restores the missing polarity at the intermediate product. An available AND cell would change the mapping to two gates.

**Transfer lesson.** Decompose the underlying associative operation, then recover the desired final complement.

### Problem 18. Prove the four-NAND XOR construction

Take t = (xy)′, u = (xt)′, v = (yt)′, and f = (uv)′. Derive the output and its pin load at the shared node.

**Solution.** The final De Morgan expansion yields f = xt + yt = (x + y)(xy)′. Expanding the complement gives (x + y)(x′ + y′) = xy′ + x′y after the contradictory products vanish. That is XOR. Equivalently, if exactly one input is high, t is high and one of u/v is low; if both inputs agree, u/v are both high.

The node t drives one pin of u and one pin of v. Thus its logical fanout is two pins; its capacitance is the sum of those pin capacitances plus wire contributions. Counting t twice in the expanded equation must not turn it into two physical gates.

**Transfer lesson.** Shared subexpressions save gates but carry a real fanout cost.

### Problem 19. Compare area and depth without mixing models

Compare two implementations of f = x(y + z). Use a library of two-input AND and OR cells, count instances and pins, and assume every cell has delay p.

**Solution.** The factored form uses one OR for y + z and one AND with x: two gates, four input pins, maximum depth two, and path bound 2p. The expanded form xy + xz uses two ANDs and one OR: three gates, six input pins, maximum depth two, and the same structural bound 2p under this artificial equal-delay model.

The factored drawing is smaller in this model. It is not automatically faster because the model assigns equal delays despite changed loads, transistor sizing, and gate type. The direct x path in the factored circuit has one stage while the expanded x paths have two.

**Transfer lesson.** Compare several metrics and label every conclusion with the assumptions supporting it.

### Problem 20. Two-output sharing with exact gate count

Let f = xy + xz and g = xy + yz. Compare shared and unshared two-input AND/OR realizations, and explain a possible timing penalty.

**Solution.** Unshared products require four AND instances, plus two ORs, for six gates. Sharing the product xy requires three AND instances and two ORs, for five. Both graphs have maximum depth two. The shared product drives two OR pins rather than one. Under a capacitive-load delay model, that driver may become slower. A larger shared AND may restore speed at a cost in area and primary-input load, or duplicating the product may be preferable on a critical path.

**Transfer lesson.** Common-subexpression elimination is an area option, not an unconditional timing improvement.

### Problem 21. Derive complementary CMOS for AOI21

Design the switch networks for f = (xy + z)′ and count standard-topology transistors.

**Solution.** The pulldown conduction predicate is D = xy + z. Implement x and y as series nMOS devices and put that branch in parallel with an nMOS controlled by z. The pullup predicate is D′ = (x′ + y′)z′. Thus pMOS x and y are parallel, and their combined network is in series with pMOS z. Three nMOS and three pMOS devices give six transistors.

At 000, the pulldown is off and the pullup on, so f = 1. At 110, the xy pulldown branch conducts and f = 0. At any input with z = 1, the z pulldown is on and its series pMOS counterpart is off, again giving f = 0. Remaining rows satisfy the same complementary predicates.

**Transfer lesson.** Design the pulldown for the complement of the desired output, then derive the pullup by De Morgan.

### Problem 22. Detect an invalid CMOS topology

A proposed block has parallel nMOS x/y pulldown switches and parallel pMOS x/y pullup switches. Is it a valid static complementary gate?

**Solution.** The pulldown predicate is D = x + y. The pullup predicate is U = x′ + y′. At 00, U is one and D zero, giving a high output. At 11, D is one and U zero, giving a low output. Those two rows may look plausible. At 01 or 10, however, one nMOS and the opposite pMOS both conduct, making D = U = 1. The output has sustained contention in the ideal stable-input model, so there is no valid Boolean truth table for those rows.

The correct complementary pullup for this pulldown is series pMOS, yielding U = x′y′ and a NOR gate.

**Transfer lesson.** Checking only extreme input patterns cannot establish complementarity.

### Problem 23. Why a single restricted static stage cannot be XOR

Assume only uncomplemented primary inputs directly control a series-parallel complementary CMOS stage. Can it compute XOR?

**Solution.** A rising control can turn an nMOS on and a pMOS off. Therefore its stable output is nonincreasing in each primary input: it may fall or remain unchanged. XOR violates this condition. With y = 0, increasing x changes XOR from zero to one; with y = 1, increasing x changes it from one to zero. No single restricted stage can realize both directions.

The conclusion changes if complemented control signals are supplied, or if a transmission-gate or other topology is allowed. The proof is about this specific gate abstraction, not about all transistor circuits bearing the name CMOS.

**Transfer lesson.** Match an impossibility proof to the exact permitted topology and control resources.

### Problem 24. Verify mixed-family noise margins

A driver guarantees low at most 0.35 V and high at least 2.7 V. A receiver accepts low at most 0.8 V and requires high at least 2.0 V. Find margins and test a 0.5 V disturbance in either adverse direction.

**Solution.** The low margin is 0.8 − 0.35 = 0.45 V. The high margin is 2.7 − 2.0 = 0.7 V. A positive 0.5 V disturbance can raise the worst low output to 0.85 V, exceeding the receiving low threshold; low interpretation is not guaranteed. A negative 0.5 V disturbance lowers the worst high to 2.2 V, still above its threshold; high interpretation remains guaranteed under these static bounds.

The conclusion says nothing about output current, absolute maximum ratings, or edge timing. Those are separate compatibility checks.

**Transfer lesson.** Use driver guarantees and receiver requirements in their respective directions; the smaller margin limits symmetric disturbance tolerance.

### Problem 25. Derive a midpoint RC delay

Under a lumped discharge model, R = 2 kΩ and C = 30 fF. Find the time to half the initial supply voltage.

**Solution.** The time constant is RC = 2000 × 30 × 10⁻¹⁵ seconds = 60 ps. From V(t)/V(0) = exp(−t/RC), setting the ratio to one half yields t = RC ln 2, approximately 41.59 ps. The dimensions are resistance times capacitance, hence time. A fourfold capacitive load with unchanged R gives approximately 166.36 ps in the same model.

This is a midpoint estimate; it is neither an upper bound guaranteed for an actual device nor the time to a different validity threshold. To reach a ratio r, use −RC ln r for discharge.

**Transfer lesson.** Derive the threshold crossing instead of treating RC itself as the exact delay for every definition.

### Problem 26. Compute arrival bounds through a DAG

At primary inputs, late arrivals are L(x) = 2 ns, L(y) = 0 ns, L(z) = 1 ns, and all earliest disturbance times are zero. Gates form u = AND(x, y), v = OR(y, z), f = NAND(u, v). Their upper/lower delays are respectively (3, 1), (5, 2), and (2, 0.5) ns. Find conservative bounds at f.

**Solution.** Late propagation gives L(u) = max(2, 0) + 3 = 5 ns and L(v) = max(0, 1) + 5 = 6 ns. Then L(f) = max(5, 6) + 2 = 8 ns. Early propagation gives E(u) = 1 ns, E(v) = 2 ns, and E(f) = min(1, 2) + 0.5 = 1.5 ns.

Thus the general structural output may first be disturbed after 1.5 ns and is guaranteed settled by 8 ns under the supplied contracts. Sensitization may make a particular transition slower to begin or earlier to finish. The unequal primary late arrivals must not be dropped.

**Transfer lesson.** Use max for late validity and min for earliest possible disturbance; do not interchange them.

### Problem 27. Unequal rise and fall delays in an inverter chain

Two inverters in series have output-rise/output-fall delays (4, 2) ns and (3, 5) ns. Find exact modeled delays for a rising and a falling primary input.

**Solution.** A rising input makes the first output fall, using its 2 ns falling-output delay. That falling intermediate event makes the second output rise, using 3 ns. Total rising-output delay is 5 ns. A falling input makes the first output rise after 4 ns; then the second output falls after another 5 ns, giving 9 ns.

The output has the same final polarity as the input, but the two directional delays differ. Selecting the larger number independently at both gates would give a conservative 9 ns general bound here, yet would not describe the rising case exactly.

**Transfer lesson.** Delay subscripts refer to the edge at the gate output unless the problem explicitly says otherwise.

### Problem 28. A structurally long but blocked path

In f = (xu) + y, let u be fixed zero and y fixed one while x changes. A netlist analyzer reports a path from x through two gates. Must the output transition after that path delay?

**Solution.** With u = 0, the product xu is always zero. With y = 1, the OR output is always one. There is no output Boolean transition caused by x in this setup. The structural path exists, and its delay may be part of a general bound when side inputs are arbitrary; it is not sensitized in this input condition.

If a gate is known to be lenient with a stable controlling input, the output can remain valid throughout. A generic static-discipline contract alone need not promise the same absence of a transient before its upper bound. The exact question must state which physical or gate model is used.

**Transfer lesson.** Path existence, Boolean sensitivity, and guaranteed transient behavior are three different statements.

### Problem 29. Calculate and repair a static-one hazard

For f = s′x + sy with x = y = 1, let s fall at time zero. Exact transport delays are inverter 3 ns, direct AND 1 ns, complemented AND 1 ns, and OR 2 ns. Find the waveform and repair the circuit. **Course-derived type: Cambridge hazard slides pages 8–9; Stanford reader pages 100–101, with independently chosen delays.**

**Solution.** Initially the direct product sy is one and s′x zero. The direct product falls at 1 ns. The inverted select rises at 3 ns, and the complemented product rises at 4 ns. Thus both OR inputs are zero from 1 to 4 ns. Transport through the OR translates those edges to a falling output at 3 ns and rising output at 6 ns: a three-nanosecond low pulse.

Add a third product xy. It is already one before time zero and does not change, so a lenient final OR stays high. The consensus identity proves the settled function is unchanged. This protection assumes that the data signals remain stable and that the added branch has already settled.

**Transfer lesson.** Logical redundancy can be exactly the temporal protection a circuit needs.

### Problem 30. Repair the dual static-zero hazard

Consider f = (s + x)(s′ + y) with x = y = 0. On a rising s transition, the first sum rises before the second sum falls. What redundant factor prevents an output pulse?

**Solution.** The stable function is ss′ = 0. During unequal path delays, both sum terms may temporarily be one, allowing the final AND to rise. Add the consensus factor x + y. For the specified stable data inputs, this factor is continuously zero and therefore controls the final AND low.

The identity (s + x)(s′ + y)(x + y) = (s + x)(s′ + y) follows from the dual of the SOP consensus theorem. It preserves every stable input row. The added term must actually be implemented as the stable controlling factor; an arbitrary equivalent remapping does not inherit a hazard guarantee without analysis.

**Transfer lesson.** Use the SOP/POS dual with the appropriate static hazard type and controlling output condition.

### Problem 31. Explain a multiple-input functional hazard

For XOR, both inputs are supposed to change from 00 to 11, but y rises 5 ns after x. Can an equivalent static circuit eliminate the intermediate one for every possible skew without changing the function?

**Solution.** During the skew interval the actual primary vector is 10, whose specified XOR value is one. If that vector lasts long enough for any correct combinational realization to settle, the output must become one. Eliminating this response for arbitrary long skew would violate the truth table. The endpoints alone do not define the whole physical input trajectory.

The proper remedy is a protocol or sampling rule ensuring that the intermediate result is not consumed, or a restricted encoding in which permitted successive states change one bit with an appropriate function. A consensus product cannot redefine XOR at 10.

**Transfer lesson.** Distinguish a removable implementation hazard from a function-required response to an intermediate input vector.

### Problem 32. Transport versus inertial pulse filtering

The two product inputs of an OR are both zero from 10 to 11 ns and at least one is high otherwise. The OR has a 3 ns transport delay. Compare its output with a specified inertial model rejecting all input-result pulses shorter than 2 ns.

**Solution.** Under transport delay, the low interval is shifted intact to 13–14 ns, with width 1 ns. The propagation interval changes event times, not pulse width. Under the specified inertial rule, the one-nanosecond low disturbance is rejected, so the output remains high. The two models agree on the stable truth table but differ on the transient response.

Real gates require characterized pulse behavior; “delay 3 ns” alone does not specify a pulse rejection threshold. Do not assume every pulse shorter than a quoted propagation upper bound disappears.

**Transfer lesson.** A delay number without a model is insufficient to determine a precise glitch waveform.

### Problem 33. Distinguish four-valued simulation from Boolean logic

In a conservative digital simulation, a wire may be 0, 1, unknown, or high impedance. Find AND(0, unknown), OR(1, unknown), and XOR(1, unknown). Does high impedance mean logical zero?

**Solution.** Treat unknown as the set of possibilities {0, 1}. AND with controlling zero produces zero for either possibility, so its abstract result is known zero. OR with controlling one is known one. XOR with one could be zero or one, so its result remains unknown. High impedance means the wire is not actively driven by that source; it is not a Boolean zero. Without a specified pull device or other driver, its voltage cannot be inferred.

This abstraction is useful for detecting incomplete initialization or disconnected outputs. It does not model actual contention current, capacitively retained charge, or analog noise.

**Transfer lesson.** A simulation uncertainty marker is information about knowledge or drive state, not an additional valid Boolean value.

### Problem 34. Diagnose a stuck-at fault with sensitization

The circuit is f = xy + z. The internal product net is stuck at zero. Choose an input that detects the fault and prove why each chosen side input matters.

**Solution.** To make the correct internal product one, set x = y = 1. To propagate a difference through the OR, set its other input z = 0. The fault-free output is then one, while the faulty output is zero. If z were one, it would mask the fault and both outputs would be one. If either x or y were zero, the fault-free product would already equal the stuck value.

This is a deterministic Boolean fault model; it does not claim coverage of bridging, delay, transistor, or analog defects. The method nevertheless connects controllability of an internal difference with observability at a primary output.

**Transfer lesson.** Excite the fault, then remove controlling side-input values that would hide it.

### Problem 35. Write unambiguous combinational HDL

Write a selector in Verilog and explain why a partial procedural assignment changes the intended kind of circuit.

**Solution.** A scalar continuous assignment expresses the intended equation directly:

```verilog
module mux2(input wire s, d0, d1, output wire y);
  assign y = (~s & d0) | (s & d1);
endmodule
```

The expression is a parallel combinational relation, not an instruction sequence that waits for one assignment to finish before the next. For one-bit signals, bitwise operators implement the listed gates. With vectors, logical and bitwise operators have different width semantics, so keep explicit types and parentheses.

A procedural block that assigns y only when s is one does not say what new value y receives when s is zero. Retaining the old y can infer a latch, introducing state. An exhaustive <code>if/else</code> or default assignment avoids that omission. The compiler may choose a different gate mapping than the written SOP; functional HDL alone does not preserve a manually added hazard-cover term.

**Transfer lesson.** Complete assignment and stable Boolean equivalence do not automatically establish timing or hazard behavior of a synthesized netlist.

### Problem 36. Minimum gate count needs a lower bound

With only two-input NAND gates, no free complements or external constants, tied inputs and fanout allowed, prove that a positive AND of two independent inputs needs at least two gates and give a matching construction.

**Solution.** With no gates, an output can only be an existing primary wire, so it cannot be xy for independent x and y. With one NAND, the only available input sources are x and y. The possible results are NAND(x, x) = x′, NAND(y, y) = y′, or NAND(x, y) = (xy)′. None is xy; the last already disagrees at 11 and 00. Therefore at least two gates are necessary.

Use t = NAND(x, y) and f = NAND(t, t). Double complement gives f = xy, matching the lower bound. This is a true minimum proof for the stated model, unlike merely presenting a convenient two-gate drawing.

**Transfer lesson.** A construction proves an upper bound. Proving optimality also requires excluding every cheaper permitted implementation.
