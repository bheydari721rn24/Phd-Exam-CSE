## 1. Scope, prerequisites, and university sources

A Boolean equation specifies the final answer for each input pattern. A circuit must produce that answer using available gates, legal signal connections, and finite time. This chapter teaches how to move between these descriptions without losing complement scope, input polarity, or timing assumptions.

Prerequisites are the approved chapters on number representation and Boolean algebra. You should recognize truth tables, De Morgan laws, SOP and POS forms, and Shannon decomposition. The derivations below restate the particular identities needed for gate construction, so that every implementation can be followed locally.

The chapter boundary includes primitive gates, multi-input behavior, schematic interpretation, functional completeness, restricted gate libraries, static complementary CMOS, cost and loading, combinational delay bounds, and introductory hazard analysis. Karnaugh-map minimization, full arithmetic-block design, sequential state, flip-flop timing, and transistor device equations belong to later chapters. The material here provides their prerequisites; it does not silently treat them as already mastered.

### Sources selected for this chapter

The candidate search covered eight universities: MIT, Cambridge, Stanford, UC San Diego, Berkeley, Carnegie Mellon, Cornell, and ETH Zurich. Selection considered usable written teaching, relevance to this chapter, derivation depth, exercises, and complementary coverage. The four core courses below were actually read and compared; Berkeley supplies a fifth written cross-check. An accessible course page alone was not counted as a reviewed course.

| University and course | Instructor or author | Written material actually reviewed | Main contribution and limitation |
| --- | --- | --- | --- |
| MIT, 6.004 Computation Structures, Spring 2017 | Chris Terman | Chapter 3 annotated teaching text: complementary switches, inverter, NAND, compound gates, delay specifications, path bounds, and lenience | Strong link between Boolean behavior and physical contracts. Its restricted static-CMOS model must not be generalized to all logic technologies. |
| Cambridge, Digital Electronics, 2020–21 | Ian J. Wassell | Introduction; Multilevel Logic and Hazards, PDF pages 1–9; device slides, PDF pages 10–17; Examples Paper, questions 1–5 and 10 screened | Explicit implementation tradeoffs and glitch diagrams. Some formulas need visual inspection because extracted text loses overbars. |
| Stanford, EE108A Digital Systems I, Winter 2008 course reader | William J. Dally; course taught with Philip Levis | Reader pages 39–42, 58–65, 67–76, 79, 83–85, 100–101; relevant exercise descriptions on pages 45 and 66 | Detailed bubbles, CMOS, load, and acyclic composition. Several informal or erroneous statements are qualified rather than copied. |
| UC San Diego, CSE 140, Spring 2022 | C. K. Cheng | Lecture 6, Universal Gates, PDF pages 1–25; Lecture 1, relevant gate, equation, and circuit-cost material on pages 46–62 | Strong restricted-library and universality exercises. Availability of constants is essential in several claims. |
| Berkeley, CS 61C course notes, Combinational Logic | CS 61C teaching staff | Entire Logic Gates teaching body, including multi-input XOR and universal subsets | Clear basic semantics and parity convention. Transistor and timing depth require the core courses. |

Source references are linked at the end. The research register records access failures and exact reading ranges. This is a bounded, evidence-based selection; no finite search establishes that every course in the world was examined. All explanations, circuits, diagrams, and solutions here are independently written. Course-derived exercises are identified as exercise types with new data or presentation; they are not reproductions of entire copyrighted exercise collections.

## 2. The digital abstraction and its electrical contract

### A bit is an interpretation of a physical signal

An ideal Boolean variable has exactly two values. A wire has a voltage that varies continuously. A receiving gate treats a sufficiently low voltage as logic zero and a sufficiently high voltage as logic one. An intermediate voltage has no guaranteed Boolean interpretation. Calling it unknown does not turn the physical system into a third-valued Boolean algebra.

For a specified logic family, write the input thresholds as <span class="math-inline">V<sub>IL</sub></span> and <span class="math-inline">V<sub>IH</sub></span>. An input at or below the former is valid low; one at or above the latter is valid high, within the permitted electrical operating range. The output guarantees are <span class="math-inline">V<sub>OL</sub></span>, an upper bound for a driven low output, and <span class="math-inline">V<sub>OH</sub></span>, a lower bound for a driven high output. The thresholds depend on supply, load, temperature, and the particular device. They are not universal numerical constants.

For a driver connected to a receiver, the static noise margins are

<div class="formula-block"><math display="block"><mrow><msub><mi>NM</mi><mi>L</mi></msub><mo>=</mo><msub><mi>V</mi><mi>IL</mi></msub><mo>−</mo><msub><mi>V</mi><mi>OL</mi></msub><mo>,</mo><mspace width="1em"/><msub><mi>NM</mi><mi>H</mi></msub><mo>=</mo><msub><mi>V</mi><mi>OH</mi></msub><mo>−</mo><msub><mi>V</mi><mi>IH</mi></msub><mo>.</mo></mrow></math></div>

Use the receiver thresholds and driver output guarantees even when they come from different families. A positive low margin means a low output can acquire that much positive disturbance before reaching the receiving low threshold. A positive high margin similarly bounds a negative disturbance on a high output. A negative margin means compatibility is not guaranteed even before extra noise is added. Adequate voltage margins do not by themselves prove current-drive capacity, transient integrity, or timing compatibility.

### Restoration and valid operating conditions

A restoring gate maps valid input regions into narrower, well-defined output regions. This prevents small disturbances from accumulating indefinitely along a chain, provided every stage meets its electrical contract. An ideal wire or a passive switch does not restore a degraded voltage. A buffer may preserve the logical value while actively restoring the voltage and increasing drive capability.

The static discipline can be stated precisely: after the inputs have been valid and stable for the specified settling interval, the device must produce valid output levels implementing the stated Boolean function. During a transition, a Boolean truth table alone gives no guarantee about the waveform. This distinction is the reason a circuit can be logically correct and still produce a dangerous transient.

### Positive and negative logic

In positive logic, high voltage denotes one. In negative logic, high voltage denotes zero. Changing this convention for every input and output of a physical device with positive-logic function f gives the negative-logic function

<div class="formula-block">g(x₁, …, xₙ) = [f(x₁′, …, xₙ′)]′.</div>

For a physical positive-logic AND gate, substitution and De Morgan give a negative-logic OR gate. Similarly, NAND becomes NOR under a complete convention change. This does not mean the device internally changes. Its voltage behavior is identical; the interpretation changes. If only some pins change interpretation, complement only those pin variables and, if needed, the output. Never apply a blanket duality rule to mixed conventions.

## 3. Primitive gates, symbols, and multi-input behavior

### Complete two-input truth table

We use juxtaposition or a centered dot for AND, plus for inclusive OR, prime for complement, and the circled plus for XOR. A prime complements the immediately preceding variable or parenthesized expression. Gate functions are defined by the entire truth table, not by a name inferred from one row.

| x | y | AND xy | OR x + y | NAND (xy)′ | NOR (x + y)′ | XOR x ⊕ y | XNOR (x ⊕ y)′ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

A buffer outputs its input; an inverter outputs its complement. A buffer is logically redundant in a zero-delay equation, but may be physically necessary. Two cascaded inverters also preserve the Boolean value. They introduce two stages of delay and do not act like a delay-free wire.

The diagram below uses the rectangular functional-symbol convention: an AND block is labeled with an ampersand, an OR block with “at least one,” and an XOR block with parity. A small circle on a pin means inversion at that pin. The familiar shaped AND, curved OR, and triangle inverter symbols express the same functions. Always read the legend: a rectangular block label is more reliable than guessing from an unfamiliar outline.

<figure class="gates-diagram"><svg viewBox="0 0 780 285" role="img" aria-labelledby="gate-symbol-title"><title id="gate-symbol-title">Six functional gate symbols with exact equations</title><g class="wire" fill="none" stroke="currentColor" stroke-width="2"><path d="M30 55H65 M30 85H65 M135 70H165 M285 55H320 M285 85H320 M390 70H420 M540 55H575 M540 85H575 M655 70H685 M30 200H65 M30 230H65 M145 215H165 M285 200H320 M285 230H320 M390 215H420 M540 200H575 M540 230H575 M655 215H685"/><rect x="65" y="40" width="70" height="60" rx="5"/><rect x="320" y="40" width="70" height="60" rx="5"/><rect x="575" y="40" width="70" height="60" rx="5"/><circle cx="650" cy="70" r="5"/><rect x="65" y="185" width="70" height="60" rx="5"/><circle cx="140" cy="215" r="5"/><rect x="320" y="185" width="70" height="60" rx="5"/><rect x="575" y="185" width="70" height="60" rx="5"/><circle cx="650" cy="215" r="5"/></g><g class="math-label" text-anchor="middle"><text x="100" y="77">&amp;</text><text x="355" y="77">≥1</text><text x="610" y="77">≥1</text><text x="100" y="222">&amp;</text><text x="355" y="222">⊕</text><text x="610" y="222">⊕</text><text x="100" y="125">xy</text><text x="355" y="125">x + y</text><text x="610" y="125">(x + y)′</text><text x="100" y="270">(xy)′</text><text x="355" y="270">x ⊕ y</text><text x="610" y="270">(x ⊕ y)′</text></g><g class="diagram-label"><text x="78" y="22">AND</text><text x="333" y="22">OR</text><text x="583" y="22">NOR</text><text x="78" y="167">NAND</text><text x="333" y="167">XOR</text><text x="583" y="167">XNOR</text></g></svg><figcaption>Each output bubble complements the block result. The parity block is explicitly labeled; a multi-input “exactly one” block would implement a different function.</figcaption></figure>

### Controlling and neutral inputs

For AND, zero is controlling: if one input is zero, the output is zero regardless of the others. One is neutral: tying an AND input high removes that input from the function. For OR, one is controlling and zero is neutral. For NAND, zero forces the output high; tying one input high leaves the complemented AND of the remaining inputs. For NOR, one forces the output low; tying one input low leaves the complemented OR of the remaining inputs.

For XOR, neither Boolean input value controls the output independently of the other input. Zero passes the other input, and one complements it. Thus tying a gate input to a constant can change the apparent function. Leaving a CMOS input electrically floating is not a legitimate way to tie it to a constant.

Repeated input connections are also meaningful. Idempotence gives AND(x, x) = x and OR(x, x) = x. NAND(x, x) and NOR(x, x) both equal x′. XOR(x, x) is zero; XNOR(x, x) is one. Count these as one physical gate with two input pins tied together, not two gate instances. Electrically, both pin capacitances still load the source.

### Multi-input gates: where the shortcuts fail

AND and OR are associative, so a multi-input function equals any parenthesization of the corresponding binary operation. A multi-input NAND is the complement of one AND over all its inputs. It is not a left-fold of binary NAND. A multi-input NOR is the complement of one OR over all inputs, not a left-fold of binary NOR.

For example,

<div class="formula-block">NAND(NAND(x, y), z) = xy + z′.</div>

This is plainly different from the three-input NAND (xyz)′: at the all-one input, the nested circuit is one while the true three-input NAND is zero. Because NAND and NOR are not associative, replacing a large gate with a tree requires polarity correction at intermediate stages.

An n-input XOR is odd parity: it outputs one exactly when an odd number of its inputs are one. It does not mean “exactly one input is one.” With three inputs, the all-one row makes that error visible. Pairwise XOR trees work because XOR is associative and commutative. Complementing one input complements parity; complementing two inputs restores it.

An n-input XNOR usually means the complement of n-input XOR, hence even parity. Cascading binary XNOR gates does not always implement this convention. If XNOR(a, b) = 1 ⊕ a ⊕ b, a tree with n leaves has n − 1 binary gates and therefore outputs

<div class="formula-block">x₁ ⊕ ⋯ ⊕ xₙ ⊕ [(n − 1) mod 2].</div>

For odd n this is odd parity, not the multi-input XNOR convention. For even n it is even parity. The result is independent of binary tree shape because the constant contributions combine modulo two. Document the convention rather than relying on the word “exclusive.”

## 4. Reading circuits and writing exact netlists

### Wires, fanout, and graph structure

A circuit net is a signal connection with one permitted driver and possibly many receivers. A branch of one wire copies the same signal; it does not perform OR. A dot at a crossing indicates a connection under the stated schematic convention. A crossing without a dot normally means independent wires. Two ordinary push-pull outputs must not be tied together to invent an OR gate. They may fight electrically when their driven values differ.

Fan-in is the number of input pins of a gate. Fanout can mean the number of driven pins, but a physical calculation requires their total capacitance or current requirements. One large receiving gate can load a driver more than several small ones. A signal may branch and later reconverge; that is valid acyclic composition and is also a common source of unequal-delay hazards.

A combinational netlist is a directed acyclic graph of combinational gates. Assign each internal net a unique name and list the gate producing it. Evaluate in topological order. Since every predecessor is already known, each new output is a function of primary inputs. Induction over this order proves that the final outputs are functions of primary inputs and that no state is required.

This is a sufficient structural criterion, not a claim that every physical feedback network necessarily stores a useful bit. A loop can have multiple equilibria, no stable equilibrium, or a stable constant under additional constraints. The ordinary acyclic-combinational proof and delay algorithm do not apply to it. Cross-coupled latches and oscillators require a different analysis.

### A disciplined conversion method

When converting a schematic into an equation, label each gate output before simplifying. Apply input bubbles first, the block operation second, and the output bubble last. Keep parentheses around a complemented expression. Then substitute internal nets into the final equation. Verify several rows that expose complements, including all-zero and all-one inputs, before testing the full table.

Conversely, to turn an expression into a circuit, start with its outermost operation as the output gate. Recursively implement the operand expressions. Share repeated subexpressions when the chosen cost model allows sharing. A formula is an expression tree; a circuit can be a DAG because one internal result can drive several places. Expanding a shared circuit back into a formula can duplicate its written literals without adding physical gates.

For example, take two outputs f = xy + xz and g = xy + yz. A direct unshared drawing has four AND gates and two OR gates. Sharing the product xy leaves three AND gates and two OR gates. Both implement the same truth tables. The shared signal has increased fanout; a smaller gate count does not automatically mean lower delay or power.

### Netlist for a NAND-only selector

The selector function is f = s′d₀ + sd₁. Label the circuit as follows:

```text
sn = NAND(s, s)
p  = NAND(sn, d0)
q  = NAND(s, d1)
f  = NAND(p, q)
```

Substituting the internal equations gives <span class="math-inline">f = [(s′d₀)′(sd₁)′]′ = s′d₀ + sd₁</span>. The algebra proves static functional correctness. It does not prove freedom from a pulse when the select input changes while both data inputs are one.

<figure class="gates-diagram"><svg viewBox="0 0 800 325" role="img" aria-labelledby="mux-net-title"><title id="mux-net-title">Four NAND gates implementing a two-way selector</title><g fill="none" stroke="currentColor" stroke-width="2"><path d="M40 62H110 M90 62V87H110 M180 75H220V145H300 M40 165H300 M40 255H300 M90 62V225H300 M375 160H520V190H580 M375 240H540V225H580 M655 207H740"/><rect x="110" y="50" width="60" height="50" rx="4"/><circle cx="175" cy="75" r="5"/><rect x="300" y="130" width="65" height="60" rx="4"/><circle cx="370" cy="160" r="5"/><rect x="300" y="210" width="65" height="60" rx="4"/><circle cx="370" cy="240" r="5"/><rect x="580" y="177" width="65" height="60" rx="4"/><circle cx="650" cy="207" r="5"/><circle cx="90" cy="62" r="3" fill="currentColor"/></g><g class="math-label"><text x="20" y="67">s</text><text x="20" y="170">d<tspan baseline-shift="sub" font-size="14">0</tspan></text><text x="20" y="260">d<tspan baseline-shift="sub" font-size="14">1</tspan></text><text x="130" y="83">&amp;</text><text x="323" y="167">&amp;</text><text x="323" y="247">&amp;</text><text x="603" y="214">&amp;</text><text x="220" y="65">s′</text><text x="440" y="150">p</text><text x="440" y="263">q</text><text x="745" y="214">f</text></g><g class="diagram-label"><text x="110" y="30">Select inverter</text><text x="300" y="110">Zero branch</text><text x="300" y="298">One branch</text><text x="580" y="157">Output combine</text></g></svg><figcaption>The select wire branches at the marked dot. Each named internal signal has exactly one driver. All four blocks are two-input NAND gates.</figcaption></figure>

## 5. Bubbles, signal polarity, and De Morgan transformations

### What a bubble actually means

A bubble is a local complement in the Boolean interpretation of a pin. A NAND drawn as an AND with an output bubble is equivalent to an OR with a bubble on every input:

<div class="formula-block">(xy)′ = x′ + y′.</div>

Likewise, an OR with an output bubble becomes an AND with every input inverted. The rule applies to every input of the transformed gate. Moving one output bubble to only one input generally changes the function.

Bubble pushing is therefore an algebraic rewrite: change AND to OR or OR to AND, move the output complement to complements on all inputs, and preserve the meaning of the external wires. Inverting a wire twice cancels in the zero-delay Boolean model. Redrawing the symbol of the same physical gate does not add a real inverter or delay. Adding a physical inverter does.

Two connected bubbles indicate that the receiving operation complements the complemented driving result. Their logical cancellation is valid on that connection. If the net branches, cancellation along one branch does not authorize removal of an inverter used by every other branch. Either preserve the net value or compensate each consumer. This is why a named-net method is safer than erasing circles visually.

### Active-low interfaces

An active-low signal is asserted when its wire is low. A signal called <code>enable_n</code> is not “false enable”; it is a wire whose assertion predicate is its complement. If an output must be low whenever either of two active-low requests is asserted, then the output wire is the AND of the two request wires. Derive this by naming the assertion predicates first. Names ending in <code>_n</code> communicate a convention but do not apply a mathematical NOT operation automatically.

Changing the desired output polarity can remove a last inverter. A NAND-NAND realization of a SOP yields the positive SOP output; stopping before the final polarity recovery may produce its complement instead. An active-low specification might want that complement. Count the gate needed for the actual required wire level, not for the name of a logical event.

## 6. Functional completeness and its hidden assumptions

### Constructive proof of universality

A library is functionally complete if finite networks of its gates can implement every Boolean function of finitely many inputs under the stated rules for constants and fanout. A truth-table SOP proves that AND, OR, and NOT form a complete library: build a product selecting each one row and OR those products. Constant-zero and constant-one functions must also be available or constructible. When an input is available, x x′ and x + x′ construct the constants. A completely input-free constant output requires an allowed constant source.

To prove another library complete, construct NOT, AND, and OR from it. NAND alone suffices:

<div class="formula-block">x′ = NAND(x, x)<br>xy = NAND(NAND(x, y), NAND(x, y))<br>x + y = NAND(NAND(x, x), NAND(y, y)).</div>

The repeated inner NAND in the AND equation is one shared physical gate. Thus the three constructions use one, two, and three two-input NAND gates respectively, assuming tied inputs and fanout are allowed. NOR gives the dual constructions: one gate for NOT, two for OR, and three for AND. These are usable upper bounds. Minimum gate counts require a separate lower-bound argument under a specified library.

### Proving that a library is insufficient

The fastest rigorous counterargument is an invariant preserved by composition. AND and OR, even with constants, are monotone nondecreasing in each input. Inductively, their composition remains monotone. NOT is decreasing, so it cannot be built from those gates. XOR, NOT, and constants produce only affine functions over the two-element field; the algebraic normal form contains no product of two distinct variables. AND is non-affine and cannot be built from that library.

XOR and AND **without a constant-one source** both preserve the all-zero input. Every network made only from them must output zero at the all-zero primary-input vector. It cannot realize NOT or constant one. Adding constant one makes NOT available as x ⊕ 1, after which AND and NOT form a complete library. A course statement declaring XOR and AND universal must be read with this constant assumption.

The gate f(x, y) = xy′ also preserves zero, so it is not universal by itself without constants. With constant one, f(1, x) produces x′, and f(x, y′) produces xy, establishing completeness. The source of the one is part of the answer, not an invisible convenience.

### A complete two-input-gate classification

There are sixteen binary truth tables. Under ordinary acyclic composition with unrestricted fanout and tied inputs, the only single two-input gates that are universal by themselves, without externally supplied constants, are NAND and NOR. Here is a proof that does not require memorizing a classification theorem.

If f(0, 0) is zero, the gate preserves the all-zero vector and cannot realize NOT. If f(1, 1) is one, it preserves the all-one vector and cannot realize NOT. To escape both obstructions, its corner values must be f(0, 0) = 1 and f(1, 1) = 0. Four possible tables remain. When the off-diagonal entries are both one, the table is NAND. When both are zero, it is NOR. The two mixed cases are simply complemented projections x′ or y′. Networks of such projections depend on at most one primary input and cannot compute AND of two independent inputs. This eliminates every other case. Supplying constants changes some library arguments, so this theorem must be stated with its no-external-constants condition.

### Selector-based completeness

A two-way selector with independently programmable data inputs and constants is also universal. It realizes NOT by choosing data one for select zero and data zero for select one. It realizes AND by selecting zero on one branch and the second variable on the other. More generally, Shannon decomposition implements any function recursively as a selector between its two cofactors. This gives a construction, not a guarantee that the construction has the lowest area or delay.

## 7. Mapping functions into restricted gate libraries

### Two-level NAND mapping of SOP

Suppose f = P₁ + ⋯ + Pₖ where each product Pᵢ is a conjunction of literals. Make the complemented products with first-layer NAND gates. Then NAND those outputs:

<div class="formula-block">f = [P₁′ · P₂′ · ⋯ · Pₖ′]′.</div>

De Morgan proves the result equals the desired SOP. A negated literal may require an input inverter unless it is already supplied. Share that inverter wherever possible. A one-literal product can use its existing complemented signal directly at the final NAND; do not add a redundant gate merely to match the drawing template. If there is only one product, the output needs an AND, requiring polarity recovery after its NAND realization.

### Two-level NOR mapping of POS

For f = S₁ ⋯ Sₖ, each Sᵢ is an OR of literals. Compute each complemented sum by NOR, then NOR those complemented sums. The final equation is the complement of their OR, hence the product of the uncomplemented sums. As before, literal availability, single-term exceptions, and output polarity affect the count.

The term “two-level” usually counts the product and combine layers while excluding input inversions. If a timing question includes all physical gates, count the input inversions too. An SOP with large products and many terms is not automatically feasible in a two-input library. Large gates must be decomposed, increasing depth.

### Correctly decomposing large inverting gates

To implement a three-input NAND with two-input NANDs, first create xy with two NAND gates, then NAND that product with z. This uses three gates. Naively connecting NAND(x, y) into NAND with z yields xy + z′, a different function. A three-input NOR can similarly build x + y with two NORs, then NOR with z.

For a four-input AND using two-input AND gates, a balanced tree has three gates and depth two; a chain has three gates and depth three. For a four-input NAND built with two-input NANDs using pair products, generate xy and zw using two gates each, then combine them with one NAND: five gates and depth three. This is a construction, not a universal minimum claim. An alternative library with three-input gates, complemented primary inputs, or mixed NAND/NOR can change both cost and depth.

### XOR with four NAND gates

Let t = (xy)′, u = (xt)′, and v = (yt)′. Then the final NAND produces

<div class="formula-block">[u v]′ = xt + yt = (x + y)(xy)′ = xy′ + x′y.</div>

Therefore four two-input NANDs realize XOR with no external complemented input. The internal signal t is shared, so its fanout matters. In the unit-delay model, there are paths of two and three NAND gates. XNOR can be obtained by an added tied-input NAND inverter. This five-gate construction is not a proof that every constrained XNOR implementation needs five.

### Library-aware optimization

Do not minimize an expression before stating the cost objective. Possible objectives include total gates, total input pins, CMOS transistor count, depth, worst-case delay, energy, and hazard coverage. They can conflict. A repeated product may be shared to save area, but the added capacitance may slow its driver. Factoring may save gates while adding a level. A redundant term may be necessary for hazard protection. Always verify functional equivalence first; then compare costs under a common model.

## 8. Static complementary CMOS from switch networks

### The abstraction used here

Treat an n-channel MOS device as conducting for a high gate-control input and a p-channel device as conducting for a low one. Use nMOS switches for a pulldown network to ground and pMOS switches for a pullup network to the positive supply. This is the ideal switch abstraction for static complementary gates; real voltage thresholds, body effects, leakage, and transitional currents require device-level analysis.

Let D be the Boolean predicate that the pulldown conducts, and U the predicate that the pullup conducts. A valid complementary design satisfies U = D′ for every stable input vector. If only the pulldown conducts, the output is low; if only the pullup conducts, it is high. Thus the output function is D′. If both conduct, there is contention through a supply-to-ground path. If neither conducts, the output is floating and may retain charge temporarily; it is not a guaranteed zero or one.

Series switches conduct only when every component conducts; parallel switches conduct when at least one branch does. To construct the complementary pullup of a series-parallel nMOS network, replace each nMOS device with a pMOS controlled by the same signal and interchange series and parallel recursively. De Morgan proves that the resulting conduction predicate is the complement. Check actual connectivity, not the superficial visual arrangement of a drawing.

### Inverter, NAND, and NOR

An inverter has one pMOS pullup and one nMOS pulldown controlled by the same input. A two-input NAND has two series nMOS devices and two parallel pMOS devices: D = xy and U = x′ + y′. A two-input NOR reverses the series/parallel roles: D = x + y and U = x′y′. Each has four transistors in this standard static topology. An n-input NAND or NOR has 2n devices, excluding input inversion and buffering. AND and OR ordinarily append an inverter to their corresponding inverting topology.

<figure class="gates-diagram"><svg viewBox="0 0 760 360" role="img" aria-labelledby="cmos-title"><title id="cmos-title">Ideal-switch topology of a complementary two-input NAND</title><g fill="none" stroke="currentColor" stroke-width="2"><path d="M200 40V65H140V92 M200 65H260V92 M140 127V160H200 M260 127V160H200 M200 160V190 M200 225V250 M200 285V315 M200 160H380"/><rect x="122" y="92" width="36" height="35"/><rect x="242" y="92" width="36" height="35"/><rect x="182" y="190" width="36" height="35"/><rect x="182" y="250" width="36" height="35"/><circle cx="200" cy="160" r="3" fill="currentColor"/></g><g class="math-label"><text x="170" y="30">V<tspan baseline-shift="sub" font-size="14">DD</tspan></text><text x="102" y="114">x</text><text x="280" y="114">y</text><text x="155" y="213">x</text><text x="155" y="273">y</text><text x="300" y="184">f = (xy)′</text><text x="182" y="340">GND</text><text x="440" y="215">D = xy</text><text x="440" y="250">U = x′ + y′</text><text x="440" y="285">U = D′</text></g><g class="diagram-label"><text x="425" y="62">Parallel pMOS pullup</text><text x="425" y="93">Each conducts for low control.</text><text x="425" y="130">Series nMOS pulldown</text><text x="425" y="160">Each conducts for high control.</text></g></svg><figcaption>Rectangles denote ideal controlled switches, not detailed transistor symbols. For each stable input pattern, exactly one complete network conducts.</figcaption></figure>

### Compound inverting gates

An AOI21 gate computes (xy + z)′. Its pulldown is the series pair x and y in parallel with z. The pullup is the parallel pair of pMOS x and y in series with pMOS z. The six devices replace a separate AND, OR, and inverter in the standard topology. An OAI21 computes [(x + y)z]′ and uses the dual connection pattern. The digits describe grouping of inputs; verify the function rather than assuming every library names groups identically.

If only uncomplemented inputs control the network, its pulldown predicate is monotone nondecreasing, so the output is monotone nonincreasing in each input. A rising input can enable pulldown and disable pullup; it cannot make the stable output rise. Therefore one such static stage cannot realize AND, OR, or XOR directly. Adding a following inverter realizes a noninverting monotone function. Providing complemented input wires permits different original-variable polarities; the one-stage limitation must be stated relative to the actual transistor-control signals. Pass-transistor, transmission-gate, dynamic, and other families are outside this restricted proof.

### Why “both off” and “both on” matter

A circuit whose output is occasionally disconnected may depend on previous stored charge, leakage, or coupling. Its truth table is incomplete as an ordinary static restoring gate. A circuit that shorts two incompatible drivers or activates pullup and pulldown together cannot be analyzed as a valid Boolean node merely by writing an OR equation. Brief simultaneous conduction during a real transition is different from a stable input condition with sustained contention; the ideal steady-state proof concerns the latter.

## 9. Cost, loading, and physical tradeoffs

### Define the model before counting

Gate count counts instances, not appearances of a subexpression in the final expanded equation. Input-pin count sums fan-ins, including tied and constant pins when they physically exist. Depth counts the largest number of gate stages on an input-to-output path. Inverter counting must be explicit. A two-input CMOS NAND has four transistors in the standard topology; an inverter has two; an AND realized as NAND plus inverter has six. These counts do not compare drive strengths or wiring area.

Pin fanout and capacitive load are distinct. The load capacitance is the sum of receiving pin capacitances and relevant wire capacitance. Driving three identical pins triples the pin-capacitance contribution, but does not necessarily triple total load if wire and output capacitance are significant. A larger transistor may reduce resistance while increasing the capacitance seen by its predecessor.

### A useful RC model, with its derivation

In a lumped first-order model, a charged load discharging through resistance R obeys C dV/dt = −V/R. Separating variables and using initial voltage <span class="math-inline">V<sub>DD</sub></span> gives V(t) = <span class="math-inline">V<sub>DD</sub></span> exp(−t/RC). Charging from zero gives V(t) = <span class="math-inline">V<sub>DD</sub></span>[1 − exp(−t/RC)]. At half-supply, either process takes RC ln 2, approximately 0.693RC. This is an estimated midpoint transition time in the specified model, not a valid-output worst-case guarantee. Real characterized delay includes input slew, pin-specific arcs, internal capacitance, nonlinear current, and operating corners.

For equal device widths, a series stack increases effective resistance. Widening every device in an m-device series stack by a factor m approximately restores its total resistance in the simple inverse-width model, but also increases input capacitance. In a NAND the nMOS stack is the slow pulldown concern; in a NOR the pMOS stack is the pullup concern. Saying “NAND is always faster” ignores process, sizing, load, and actual library characterization.

### Energy and activity

In the ideal charging model, the supply provides C V² energy for one zero-to-one charging event; half becomes stored capacitor energy and half is dissipated in the charging resistance. The stored half is dissipated when the capacitor later discharges. Thus a full zero-to-one-to-zero cycle dissipates C V². If α counts zero-to-one events per clock interval, the corresponding switching-power approximation is α C V² times clock frequency. If an activity factor instead counts all edges, its coefficient differs. Leakage and short-circuit currents add power even when this switching formula is insufficient. Static CMOS has no ideal steady-state supply-to-ground path, but real static power is not literally zero.

Hazards can add internal charging events without changing the final truth-table output. A design optimized for literals alone can therefore lose on switching energy. This chapter derives the mechanism without making a numerical power prediction for an uncharacterized real circuit.

## 10. Propagation, contamination, and arrival-time reasoning

### Two bounds with different meanings

Propagation delay is an upper bound on the interval from stable valid input conditions to the required valid stable output. Contamination delay is a lower bound on how soon the previous output may stop being valid after an input starts to change. In the ideal digital-event model, we mark that input event at time zero and use these bounds as its early and late effects. If no contamination guarantee is supplied, zero is the conservative choice.

Between the bounds, do not assume the output remains old, has become new, or makes only one transition. This interval can contain multiple digital changes or invalid physical voltage. A datasheet midpoint propagation measurement is not automatically the same contract as MIT's valid-level bound. Use the definition supplied in the problem consistently; do not combine unmatched measurement conventions.

### Path sums and dynamic programming

For a finite acyclic circuit with fixed nonnegative per-gate bounds, sum propagation delays along each primary-input-to-output path and take the maximum. Sum contamination delays and take the minimum for a conservative earliest possible disturbance. These are structural bounds; a path may be unsensitizable for a particular input pattern, making the bound pessimistic rather than incorrect.

With arrival times at input pins, a gate output has the recursive upper bound

<div class="formula-block">L(out) = maxᵢ[L(inputᵢ) + pᵢ]<br>E(out) = minᵢ[E(inputᵢ) + cᵢ].</div>

Here pᵢ and cᵢ are the relevant pin-to-output upper and lower delay bounds. The late recurrence waits for every relevant input; the early recurrence allows the first possible influence. For a gate specified with one common upper and lower bound, pull those constants outside the max or min. Wire-delay bounds can be added as edge contributions. Topological evaluation computes these bounds efficiently without enumerating every path.

When several primary inputs change at different times, the output settling time must incorporate their arrival times. Measuring from the first input transition while ignoring a later transition is unsafe. If a particular primary input does not change, do not fabricate a disturbance arrival on it; use a pattern-specific analysis or keep the stated general structural bound.

### Rise/fall direction and sensitization

An inverter swaps edge direction: a rising input uses the output-falling delay, and a falling input uses the output-rising delay. Two inverters restore polarity but require one delay of each direction. For AND and NAND, the other inputs must be high to sensitize a tested pin transition; a low side input controls the output. For OR and NOR, side inputs must be low. A reconvergent path can impose incompatible conditions on shared side signals, so the structurally longest path is not always a realizable transition path.

Timing analysis with exact sensitization can be much harder than graph longest paths. State which method the question asks for. In an exercise supplying only abstract gate bounds, the maximum path sum is a safe delay budget. It does not promise that a simulation will exhibit that exact delay on every transition.

### Exact transport events versus inertial filtering

A fixed transport-delay model schedules every Boolean output change after a fixed interval, including short pulses. An inertial model rejects sufficiently brief disturbances according to its pulse-rejection rule. Neither is the same as an interval-valued physical specification. A pulse may exist in a structural delay explanation yet be filtered by a particular real gate; conversely an unmodeled analog effect may appear in hardware. State the model before drawing a precise waveform.

## 11. Hazards, consensus, and limits of logical equivalence

### A derivation of the classic static-one hazard

Take f = s′x + sy, with stable data inputs x = y = 1. The stable function is one for either select value. Implement the select complement through an inverter and the two products through separate AND gates. On a falling select transition, the direct product sy may fall before the complemented product s′x rises. During that gap, both products are zero and the OR output can fall temporarily.

Let the direct product gate have exact transport delay b, the select inverter delay a, the complemented product delay c, and the final OR delay d. For the falling select transition, the direct product falls at b and the complemented product rises at a + c. If b is less than a + c, the OR input gap has width a + c − b; the output pulse is translated by d without changing its width under this model. If b is greater, the two product highs overlap and there is no such static-one pulse. A truth table cannot express either result because it contains only settled input rows.

Add the consensus product xy:

<div class="formula-block">s′x + sy + xy = s′x + sy.</div>

The equation is unchanged because xy is already covered by the select branches. During the specified transition, however, xy stays one and holds the output high. The product is logically redundant but temporally protective.

### Static-zero and dynamic hazards

A static-zero hazard is a zero-to-one-to-zero transient when the stable output should stay zero. For the POS function (s + x)(s′ + y), with x = y = 0, the output should remain zero. Unequal paths can let both sum terms be one temporarily. Adding the consensus sum (x + y) holds the final AND output at zero. The redundant-sum identity is the dual of the redundant-product identity.

A dynamic hazard has more than one output transition where the settled function requires one. Reconvergent multilevel logic can create alternating intermediate events that survive downstream delays. Eliminating one static hazard in one SOP implementation does not prove that every multilevel remapping is hazard-free.

### Exact scope of the consensus guarantee

For a two-level AND-OR SOP with properly implemented literals, and one changing primary input at a time while the others remain stable, a static-one hazard can arise when adjacent one rows lack a product term covering both endpoints. A shared product independent of the changing input remains one throughout that transition. Covering every adjacent one pair by such a term gives the standard static-one hazard protection under this model. The POS dual protects adjacent zero pairs against static-zero hazards.

This guarantee assumes the covering term has settled before the transition and that the gate model preserves a stable controlling input. It does not cover simultaneous multi-input changes, unmodeled glitches in supposed stable inputs, arbitrary multilevel implementations, analog coupling, or asynchronous protocol correctness. A minimal cover is not necessarily a hazard-protected cover. Adding arbitrary redundant terms is not a universal cure; add a term that actually bridges the relevant adjacency.

### Functional hazards cannot always be removed by algebra

Suppose XOR inputs change from 00 to 11. The settled endpoints both produce zero, but input skew may make the intermediate vector 01 or 10, where the specified function is one. A circuit that correctly responds to that stable intermediate vector must allow the corresponding change. No static equivalent algebraic expression can make the Boolean function ignore every such intermediate vector while preserving its full truth table. Solutions require an input-transition protocol, a permitted Gray-coded transition, stable sampling, or a different specification. Register design and asynchronous protocols are later topics; the limitation already matters here.

## 12. Interactive gate and hazard laboratory

The laboratory has two separate models. The first enumerates stable truth tables of primitive gates and compares a true multi-input gate with its binary cascade. The second computes exact transport events for the selector hazard just derived. It is an instructional model, not SPICE, and does not model voltage, transistor physics, leakage, or inertial pulse rejection.

For the timing model, both data inputs stay one and the select falls once at time zero after the circuit has settled. Change the four gate delays and compare the two-product circuit with the consensus-protected circuit. The final OR translates each gap boundary by its delay. When two internal events have the same time, they are applied as one batch before evaluating the OR; this prevents an artificial zero-width glitch caused by arbitrary event ordering.

<section class="gates-lab" aria-label="Gate semantics and hazard laboratory"><h3>Stable gate semantics</h3><div class="lab-controls"><label>Gate<select id="gate-kind"><option>AND</option><option>OR</option><option>NAND</option><option>NOR</option><option>XOR</option><option>XNOR</option></select></label><label>Input count<select id="gate-count"><option>2</option><option selected>3</option><option>4</option></select></label></div><p id="gate-status" role="status"></p><div class="table-scroll"><table id="gate-table"><thead></thead><tbody></tbody></table></div><h3>Selector hazard under exact transport delay</h3><div class="lab-controls"><label>Inverter delay (ns)<input id="haz-inv" type="number" min="0" max="20" step="0.5" value="3"></label><label>Direct AND delay (ns)<input id="haz-direct" type="number" min="0" max="20" step="0.5" value="1"></label><label>Complemented AND delay (ns)<input id="haz-comp" type="number" min="0" max="20" step="0.5" value="1"></label><label>Final OR delay (ns)<input id="haz-or" type="number" min="0" max="20" step="0.5" value="2"></label></div><p id="haz-status" role="status"></p><figure class="gates-diagram"><svg id="haz-wave" viewBox="0 0 800 320" role="img" aria-label="Transport timing waveforms"></svg><figcaption>Each trace shows logic levels, not analog voltage. The protected output includes the stable consensus product.</figcaption></figure><div class="table-scroll"><table id="haz-events"><thead><tr><th>Time (ns)</th><th>Event</th><th>Interpretation</th></tr></thead><tbody></tbody></table></div></section>

Use the model after reading the worked derivation. A matching steady truth table is necessary for a correct mapping; a matching truth table alone says nothing about unequal-delay transients. Conversely, a pulse in this fixed-delay model is not a universal claim about every manufactured gate with those names.
