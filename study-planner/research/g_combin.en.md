# Combinational Circuit Design

## Sources, objectives, and notation

This chapter develops a complete design argument: state an unambiguous contract, construct a circuit, prove its outputs, measure its cost under an explicit library, and identify where timing or an incomplete implementation invalidates the argument. The prerequisites are Boolean algebra, indexed truth tables, and the previous minimization chapter. You do not need prior HDL experience.

| Reviewed course | Contribution to this chapter |
|---|---|
| MIT 6.004, Chris Terman, Spring 2017 | Complete specifications, bounded-fan-in trees, input arrival times, multiplexers and ROM construction |
| Stanford EE108A, Philip Levis; William J. Dally reader | History independence and an inductive proof of closure under acyclic composition |
| Cambridge Digital Electronics, Ian J. Wassell, 2025–26 | Multilevel factoring, common expressions, implementation alternatives |
| Cornell ECE2300, Christopher Batten, Fall 2026 | Internal nets, multiple outputs, structural Verilog, propagation and contamination bounds |
| Berkeley CS150, Randy H. Katz, Fall 2005 | Multi-output design examples, declared cost models, NAND/NOR polarity transformations |

These five written courses were selected after a documented comparison with accessible alternatives. Exact reading ranges and source corrections are in the [source audit](../reviews/g_combin-sources.html). Historical sources are identified by date. Every figure and animation here is newly constructed rather than copied from a course PDF.

In Boolean equations, juxtaposition or a dot means AND, $+$ means OR, $\oplus$ means XOR, and an overbar means complement. Ordinary numerical addition is explicitly called arithmetic addition. Inputs $A,B,C,D$ are ordered from most to least significant unless stated otherwise. A vector $x_{w-1}\cdots x_0$ represents the unsigned integer $\sum_{i=0}^{w-1}2^i x_i$. A signal called `request_n` has active-low polarity only if its contract states that zero asserts the request; an identifier alone is not a proof of polarity.

## The functional contract: from words to obligations

### Boolean functions and relations

A completely specified combinational block with $n$ input bits and $m$ output bits implements a function

$$F:\mathrm{Bool}^n\to\mathrm{Bool}^m.$$

Here $\mathrm{Bool}=\{0,1\}$ is the set of binary values. The superscripts count the input and output coordinates, not exponentiation of a numerical signal.

The function assigns exactly one output vector to each input vector. It has $2^n$ input rows and $m2^n$ output-bit entries. There are $2^{m2^n}$ possible such functions: each of the $m2^n$ entries can independently be zero or one. This counts mathematical specifications, not physically distinct netlists; infinitely many redundant netlists may implement the same function.

A partial specification is better modeled as a relation $R(x,y)$ that describes allowed output vectors. Its implementation requirement is $R(x,F(x))=1$ for each legal input. If a contract says that output $Y$ is irrelevant when validity $V=0$, then either value of $Y$ is permitted on those rows, while $V$ itself is still specified. Do not change specified validity merely because associated data is unspecified. Independent per-bit don't-cares are appropriate only if every combination of the permitted output bits is allowed. A relational restriction such as “exactly one of $Y_0,Y_1$ is asserted” cannot be represented by making both bits independently X.

For a care predicate $C(x)$ and a fixed reference function $F$, a candidate $G$ is acceptable if

$$C(x)=1\Rightarrow G(x)=F(x).$$

This allows disagreement outside the care set. The environment must actually enforce $C$; an invalid-input behavior that is harmless in a mathematics exercise can be dangerous in a control interface. An implementable contract must admit at least one permitted output on every legal input. If two requirements force the same bit both high and low, the task is inconsistent rather than merely difficult to minimize.

### A disciplined specification procedure

Begin by listing inputs, outputs, widths, bit order, and polarity. Write each semantic requirement as a predicate over current inputs. Decide whether simultaneous requests are legal, and whether they are combined, rejected, or ordered by priority. State reset, validity, default, and invalid-code behavior where applicable. Enumerate the complete small truth table; for a large datapath use an arithmetic or bit-vector specification plus boundary cases. Only then simplify or select a circuit structure. This ordering prevents a plausible-looking circuit from silently selecting an interpretation that the original wording never justified.

**Worked example 1 — priority is part of the specification.** Two requests $R_1,R_0$ ask for mutually exclusive grants $G_1,G_0$. Enable $E=0$ suppresses both grants; when enabled, request 1 has priority. Derive the equations by conditions: grant 1 requires enable and request 1, so $G_1=ER_1$. Grant 0 additionally requires the absence of request 1, so $G_0=E\overline{R_1}R_0$. Validity is $V=E(R_1+R_0)$. For $E=1,R_1=R_0=1$, the output is $(G_1,G_0,V)=(1,0,1)$. The tempting expression $G_0=ER_0$ violates exclusivity on that row. Algebraically $G_1G_0=E^2R_1\overline{R_1}R_0=0$ proves that the chosen grants are never simultaneously asserted. Also $G_1+G_0=E(R_1+\overline{R_1}R_0)=E(R_1+R_0)=V$ proves that a valid request obtains exactly one grant.

<!-- FIGURE:contract -->

**Worked example 2 — count legal completions without corrupting validity.** A three-bit input is a binary number from zero to seven. Output $V$ must be one precisely for inputs zero through five. Output $P$ must indicate even parity on these six valid inputs and is unrestricted on six and seven. There are exactly $2^2=4$ permitted complete output functions: only the two invalid $P$ entries are free. There are not sixteen completions, because the corresponding $V$ entries are fixed at zero. A safe alternative contract requires $P=0$ whenever $V=0$; it has one completion and can be implemented as $P=V\overline{A\oplus B\oplus C}$. The two contracts have different obligations even if they happen to produce identical outputs on all valid inputs.

## History independence, netlists, and acyclic composition

### A settled output is not an instantaneous output

Combinational behavior means that after the modeled settling time, the output is determined by the present inputs and does not encode earlier input history. It does not mean that physical propagation takes zero time. Two different input histories reaching the same stable input vector must converge to the same specified stable output. If one history leaves $Y=0$ and another leaves $Y=1$ indefinitely under identical present inputs, $Y$ contains state.

A useful structural guarantee is a directed acyclic graph of combinational blocks. Each vertex is a gate or already verified combinational module. A directed edge connects a driving output to a receiving input. Primary inputs are external sources, and primary outputs are observed nets. Every internal net needs one well-defined driver in the simple Boolean model. Two ordinary output drivers connected together require an electrical resolution model; they are not automatically an OR gate. Fan-out is the number of receiving input pins, whereas fan-in is a gate's number of input pins.

### Proof of closure under acyclic composition

Assign primary inputs depth zero. A gate whose inputs already have depths receives depth one plus their maximum. A finite DAG has a topological ordering, so this assignment eventually reaches every gate. Induct on that order. A first-level gate computes a function of primary inputs. Assume each predecessor of gate $v$ computes a unique function of primary inputs. Substitution of those predecessor functions into the truth function of $v$ gives another unique function of primary inputs. Consequently every output of the DAG is history-independent after settling. The same induction proves the correctness of a topological evaluator, provided every primitive's truth function and every connection are correct.

The proof fails at an actual cycle because there is no first uncomputed gate on the cycle. A cycle is a structural warning, not an automatic classification of every algebraic equation. For $q=\overline q$, no stable Boolean assignment exists. For $q=q$, both stable Boolean assignments satisfy the equation. For $q=q\cdot0$, the only Boolean fixed point is zero, although electrical convergence still needs a physical model. Thus “has feedback” and “has exactly two stable states” are not equivalent statements. Design rules usually prohibit combinational cycles so that a general settling and evaluation guarantee is available.

<!-- FIGURE:dag -->

**Worked example 3 — evaluate a shared network.** Let $p=AB$, $q=C+D$, $r=pq$, $Y=r+E$, and $Z=r\oplus H$. The same $r$ drives two outputs. With $(A,B,C,D,E,H)=(1,1,0,1,0,1)$, compute $p=1$, $q=1$, $r=1$, $Y=1$, and $Z=0$ in topological order. The Boolean equations are $Y=AB(C+D)+E$ and $Z=AB(C+D)\oplus H$. If two-input AND, OR, and XOR gates cost one each, there are five gates. Duplicating the entire three-gate $p,q,r$ subnetwork separately for each output would need eight gates; duplicating only the final $r$ gate while still sharing $p,q$ would need six. Primary-input-to-output depth is three through $p$ or $q$, then $r$, then an output gate. It is not four simply because five equations were written sequentially on the page. HDL source-line order for continuous assignments likewise does not make these gates execute serially.

**Worked example 4 — a two-output examination network.** In the authentic PhD NAND circuit, define $t=\overline{xy}$, $u=\overline{xt}$, $v=\overline{yt}$, $D=\overline{uv}$, and $B=\overline{vv}$. The first four gates produce $D=x\oplus y$. Tied-input NAND is inversion, so $B=\overline v=yt=y\overline{xy}=\overline x y$. These are one-bit subtraction difference and borrow, not addition sum and carry. A complete derivation identifies both outputs; recognizing only the XOR subnetwork would not distinguish a half-adder from a half-subtractor. The authentic item and its option analysis appear in the problem bank.

## Multilevel structure, sharing, and explicit cost

### Why minimum SOP is not automatically the best circuit

A minimum two-level cover minimizes its declared algebraic objective, often term count followed by literal count. A mapped implementation has additional constraints: allowed gate types, fan-in, complemented-input availability, output polarity, fan-out, delay, wiring, and cell area. Two algebraically equivalent implementations can differ in all of these. State the objective before using the word minimum. Showing one compact circuit establishes an upper bound; proving global minimality needs a lower bound or exhaustive search in a specified implementation space.

Common subexpressions are computed once and reused. Algebraic factoring exploits $PQ+PR=P(Q+R)$. In a multi-output block, a product useful to more than one output can be physically shared even when independent minimization selects a different cover for each output. The benefit must be measured with internal gates counted once, and with any buffers required by the declared fan-out limit included. Sharing also couples faults and timing to several outputs, which may be undesirable under a reliability objective.

**Worked example 5 — fan-in changes a published gate count.** Expand

$$Z=(a+b+c)(d+e)f+g.$$

It contains six three-literal products plus $g$, so the expanded expression has nineteen literal occurrences. If three-input AND and a seven-input OR are allowed, the expanded two-level network uses seven gates. The factored network uses a three-input OR for $a+b+c$, a two-input OR for $d+e$, a three-input AND for their product with $f$, and a final two-input OR: four gates, nine gate-input incidences, and three physical levels. With only two-input gates, form $a+b+c$ using two OR gates and the three-way product using two AND gates. Together with $d+e$ and the final OR, this factored realization uses six gates and has a maximum depth of five for that left-associated topology. Reassociation can reduce the maximum to four by first computing $(a+b+c)$ and $(d+e)f$ in parallel, then ANDing and ORing. A truth table proves functional equality; it does not decide which library-specific realization is cheapest or fastest.

<!-- FIGURE:sharing -->

### Bounded fan-in trees and arrival-sensitive organization

An AND, OR, or XOR of $n$ operands can be constructed with $n-1$ two-input gates. A full binary tree with $n$ leaves has $n-1$ internal vertices, proving this count for that tree construction. A gate at depth $d$ can depend on at most $2^d$ leaves, so the depth of any fan-in-two formula depending on all $n$ inputs is at least $\lceil\log_2 n\rceil$. A balanced tree achieves that depth when all inputs arrive together. A chain instead has depth $n-1$. These formulas exclude input inversion and assume equal gate delays.

NAND and NOR are not associative. Cascading NAND as though it were AND generally changes the function. To build a wide NAND, first realize the conjunction with proper polarities, then complement the final result, or use a correctly polarity-mapped alternating network. Never infer the output by counting inversion bubbles alone without considering where the complemented signals enter other operations.

**Worked example 6 — the balanced tree loses with a late input.** Four AND inputs $a,b,c,d$ arrive at times $0,0,0,10$, and each two-input AND has delay one. A balanced arrangement $(ab)(cd)$ produces its output at $\max(\max(0,0)+1,\max(0,10)+1)+1=12$. The arrangement $((ab)c)d$ produces $ab$ at one, $(ab)c$ at two, and the final output at $\max(2,10)+1=11$. The second circuit has greater structural depth but an earlier output under these arrival assumptions. This is why “balanced means fastest” needs a simultaneous-arrival qualification.

## Cofactors and systematic construction

### Shannon expansion is a proof and a circuit recipe

Define $F_0(z)=F(0,z)$ and $F_1(z)=F(1,z)$ for one selected variable $S$ and all remaining variables $z$. For $S=0$, the expression $\overline S F_0+SF_1$ evaluates to $F_0$; for $S=1$, it evaluates to $F_1$. These exhaustive cases prove

$$F=\overline S F_0+SF_1.$$

A 2:1 multiplexer implements exactly this expansion when select zero chooses its input 0. The two data inputs may themselves be functions, not merely constants. If $F_0=F_1$, selection is unnecessary because $F$ is independent of $S$. If the two cofactors are complements, XOR or XNOR structure may emerge. Repeated expansion over $k$ selected variables yields $2^k$ data functions of the remaining variables. The usefulness of a select choice is measured by the complexity of those residual functions and by available shared logic, not by arbitrary attachment of variables to select pins.

**Worked example 7 — derive four data inputs without guessing.** Let $F(A,B,C)=\sum m(1,2,3,5,7)$. Choose $A,B$ as the select bits of a 4:1 mux, with $A$ most significant. Pair the truth rows by $AB$: at 00, the values for $C=0,1$ are 0,1, so $D_0=C$; at 01 they are 1,1, so $D_1=1$; at 10 they are 0,1, so $D_2=C$; at 11 they are 0,1, so $D_3=C$. Therefore $F=\overline A B+C$. The mux construction and the simplified equation agree on all eight rows. In contrast, swapping the select-bit order without permuting $D_1,D_2$ implements a different function. A one-variable residual has four possible truth pairs: 00 gives zero, 11 gives one, 01 gives the variable, and 10 gives its complement.

<!-- FIGURE:cofactor -->

### Decoder and ROM construction for several outputs

An enabled active-high $n$-to-$2^n$ decoder produces $d_i=1$ precisely when the input vector has index $i$. Its outputs are minterms; exactly one is high under a legal stable binary input and asserted enable. Any output function can be obtained by ORing the required decoder outputs. Multiple outputs reuse the decoder and select different row sets. With active-low decoder outputs, those selected minterms are complemented; a NAND, rather than an OR, recovers their active-high union through De Morgan's law. State the enable and output polarity before choosing the combining gate.

A logical ROM stores one $m$-bit word at each of $2^n$ addresses. Its capacity is $m2^n$ bits, and its table directly implements an $n$-input, $m$-output function. This proves existence but does not claim an area optimum. For an asynchronous fixed-content ROM, the stable output is a function of the current address after access delay. A synchronous-read memory instead has an output associated with a clocked address and belongs to a sequential interface. Address order, word-bit order, and physical polarity remain separate questions.

**Worked example 8 — one decoder, two predicates.** For a three-bit input $ABC$, let $P$ be odd parity and $M$ be majority. Their one-sets are $\{1,2,4,7\}$ and $\{3,5,6,7\}$. A shared decoder feeds two separate four-input OR functions. A ROM stores words $(P,M)$ in address order 000 through 111: `00,10,10,01,10,01,01,11`. The ROM needs sixteen bits. With only two-input output OR gates, each four-term union needs three gates and depth two beyond the decoder; there are six such output gates. A mistaken reversed word order produces the majority bit where parity was expected. The shared decoder does not make the two predicates equal.

<!-- FIGURE:rom -->

## Technology mapping and polarity contracts

### NAND/NOR transformations with internal signals labeled

For $Y=P+Q$, De Morgan gives $Y=\overline{\overline P\cdot\overline Q}$. Compute $\overline P$ and $\overline Q$ with first-stage NAND gates when $P,Q$ are products, then a final NAND recovers their OR. This works because each intermediate complement is explicitly present in the algebra. The dual construction for a product of sums uses first-stage NOR gates and a final NOR. Complemented primary inputs may need separate inverters; count them unless the problem says both polarities are already available. An output inversion can sometimes be absorbed into a consuming gate, but a change to an externally observed output's required polarity is not free.

**Worked example 9 — a factored NAND mapping.** For $Y=A(B+C)$ with only two-input NAND and no pre-supplied complements, compute $b_n=\overline{BB}$ and $c_n=\overline{CC}$, then $t=\overline{b_n c_n}=B+C$, $u=\overline{At}$, and $Y=\overline{uu}$. This is a valid five-NAND construction. Alternatively, compute $p=\overline{AB}$, $q=\overline{AC}$, and $Y=\overline{pq}$, giving the same function with three NANDs. The factored algebra is shorter but its particular NAND mapping is worse. These constructions establish costs five and three for the listed circuits, not a universal mapping theorem. At $A=0,B=C=1$, the correct output is zero; this row quickly rejects a circuit that inadvertently computes $A+(B+C)$.

<!-- FIGURE:polarity -->

### Interface transformations

Suppose enable is active-low `en_n`, both requests are active-high, and grants are active-low. The priority equations become $G_{1n}=\overline{\overline{E_n}R_1}$ and $G_{0n}=\overline{\overline{E_n}\overline{R_1}R_0}$. Disabled outputs are both one. Do not negate only the final truth table while leaving an active-low input interpreted as active-high. Input polarity transforms the argument; output polarity transforms the result.

Word-level complements are width-sensitive. Complementing the four-bit word `0011` gives `1100`, which represents twelve unsigned and minus four in four-bit two's complement. Logical negation of the same nonzero word gives the one-bit Boolean zero. Equality to zero, bitwise complement, and signed negation are distinct operations. Zero-extension preserves an unsigned numeric value; sign-extension preserves a two's-complement signed numeric value. Truncation preserves low bits, not necessarily the original number. An algorithmic predicate such as $x<y$ must specify signedness as well as width.

## Combinational HDL: connectivity and complete assignment

### Structural and dataflow descriptions

The following structural Verilog module describes a circuit, not a serial instruction list. Primitive pins place the output first; named module ports are preferable when an interface has several similarly sized signals.

```verilog
module shared_pair(input wire a, b, c, d, e, h,
                   output wire y, z);
  wire p, q, r;
  and (p, a, b);
  or  (q, c, d);
  and (r, p, q);
  or  (y, r, e);
  xor (z, r, h);
endmodule
```

The equivalent continuous assignments are `assign p = a & b;`, `assign q = c | d;`, `assign r = p & q;`, `assign y = r | e;`, and `assign z = r ^ h;`. Continuous assignments concurrently define drivers that react to input changes. The symbols `&`, `|`, `^`, and `~` are bitwise operations; `&&`, `||`, and `!` are logical operations producing a Boolean result. Parenthesize deliberately. A bus's range and every literal's size should be explicit.

### Complete behavioral assignments and hidden state

An original SystemVerilog implementation of the priority contract is:

```systemverilog
module priority_pair(input logic en, r1, r0,
                     output logic g1, g0, valid);
  always_comb begin
    g1 = 1'b0;
    g0 = 1'b0;
    valid = 1'b0;
    if (en) begin
      g1 = r1;
      g0 = (~r1) & r0;
      valid = r1 | r0;
    end
  end
endmodule
```

Every output is assigned for every execution path. Blocking assignments make the intended local evaluation order explicit inside the procedural block. An `always_comb` declaration expresses an intended combinational process and enables tool checks; it does not make a missing assignment mathematically harmless. With `if (en) y = d;` and no assignment when `en=0`, preserving the old $y$ value is state. A synthesis tool may reject the incomplete process or infer a latch according to its rules. The correction is a fully specified disabled behavior, such as `y = en ? d : 1'b0;`, if that matches the contract. If hold behavior is actually intended, the block is a storage element and must be treated as sequential.

**Worked example 10 — exhibit two histories that defeat a combinational claim.** Start with $y=0$, enable once with $d=0$, then disable. The current inputs are $(en,d)=(0,1)$ and $y$ remains zero. Starting from another history, enable with $d=1$, then disable with the same current inputs $(0,1)$; now $y$ remains one. Two settled outputs under the same current input prove history dependence. Testing the disabled branch only once would fail to reveal this.

Four-state simulation uses 0, 1, X, and Z. X means an unknown/unresolved simulation value, not permission to choose a convenient output in a specified row. For example, `1'b0 & 1'bx` evaluates to zero while `1'b1 & 1'bx` remains unknown. Z models a high-impedance driver state and is not an ordinary Boolean third value in this chapter's gate model. A `casez`/`casex` wildcard can mask unknowns in ways that hide real faults; use explicit legal-input assumptions and ordinary complete cases where possible. These code examples are verified against independent mathematical models, not presented as compiled or electrically simulated designs.

## Proving equivalence, finding counterexamples, and testing faults

### The equivalence miter

For reference outputs $F_j$ and candidate outputs $G_j$, construct a discrepancy bit

$$M(x)=\bigvee_{j=0}^{m-1}(F_j(x)\oplus G_j(x)).$$

The circuits are equivalent exactly when $M$ is zero on every input. Under care predicate $C$, the condition is $CM=0$ on every input. A satisfying input for $CM=1$ is a concrete counterexample. This check must use the same width, bit order, output polarity, and care assumptions for both implementations. Comparing only one output cannot prove a multi-output block. Comparing only valid rows cannot prove safe default behavior if the contract specifies invalid rows too.

Small truth tables can be exhausted. Larger blocks can be checked by symbolic reasoning, SAT/SMT with explicit bit-vector semantics, compositional lemmas, or carefully designed tests. Random testing may find errors but absence of a random counterexample is not an equivalence proof. A useful independent checker describes the reference from the original requirement, rather than mechanically duplicating the candidate's gate equations; the same wiring error in both models would otherwise agree.

**Worked example 11 — a fault hidden by one checked output.** A correct two-output block has $F_0=A(B+C)$ and $F_1=AB$. A candidate retains $G_0=F_0$ but sets $G_1=A(B+C)$. Its miter reduces to $AB\oplus A(B+C)=A\overline B C$. Thus exactly row 101 detects the error. Tests of 000, 111, and any row with $A=0$ all pass, and output zero is correct on every row. The counterexample follows from the relational difference, not from choosing an arbitrary “hard-looking” input.

### Stuck-at fault activation and propagation

A stuck-at-zero fault at net $t$ is activated by an input for which the correct $t=1$. It is detected only if the resulting discrepancy reaches an observed output. For $Y=AB+C$ and a stuck-at-zero fault at $t=AB$, activation requires $A=B=1$ and propagation through the OR requires $C=0$. Hence 110 is the unique detecting row. Setting $C=1$ masks the fault even though it is activated internally. A stuck-at-one fault at the same net needs $AB=0,C=0$, giving 000, 010, and 100. These finite functional fault models do not encompass bridging faults, analog delay faults, or every physical failure.

For several specified faults, each test detects a subset. Selecting a minimum test set is a set-cover problem over those fault obligations. Distinguish an irredundant chosen test set from a globally minimum set. Exhaustive enumeration is feasible for small exercise instances; heuristic test selection requires an explicit optimality limitation.

<!-- FIGURE:miter -->

## Timing foundations: structural bounds and false paths

### Latest and earliest arrival recurrences

Give primary input $i$ latest arrival $T_i$ and earliest possible change $t_i$. For gate $v$ with propagation upper bound $d_p(v)$ and contamination lower bound $d_c(v)$, conservative structural bounds are

$$T_v=\max_{u\in\mathrm{pred}(v)}T_u+d_p(v),$$

$$t_v=\min_{u\in\mathrm{pred}(v)}t_u+d_c(v).$$

The latest bound says that once all predecessor inputs have settled, the gate settles within its propagation bound. The earliest bound says no output change can arrive through an input path before that path's contamination bound. Compute them separately; minimum and maximum are not interchangeable. A bounded interval is not a promise that a transition occurs at every time in the interval. It may never occur if the input combination masks that path.

**Worked example 12 — interval bounds and sensitization.** Let $p=AB$, $q=p+C$, and $Y=qD$. The propagation delays are 3,4,2; the contamination delays are 1,2,1. Assume all primary inputs may change at time zero. The longest structural delay through $A$ or $B$ is $3+4+2=9$. The shortest structural path through $D$ has contamination delay one. A transition through $A$ is sensitized with $B=1,C=0,D=1$; otherwise a controlling value can block it. Thus the structural maximum can be attained in the stated independent-input model, but it is not the delay for every transition. If $D=0$, no input change at $A,B,C$ can alter $Y$ at all.

### False paths and reconvergence

Reconvergent fan-out occurs when one net branches and later influences a common receiving output through several paths. Such paths have correlated values. For $Y=A\overline A$, the stable Boolean function is zero, even though the schematic has input-to-output paths. A structural path search alone cannot prove a stable output transition exists. With unequal physical path delays the implementation may produce a transient pulse, so stable constancy is not the same as a hazard-free waveform.

For $Y=AB+\overline A C$ with $B=C=1$, both stable endpoints for an $A$ transition are one. Unequal product delays may briefly make both OR inputs zero. The prior minimization chapter treats the exact consensus repair; here the lesson is methodological: functional equivalence, structural timing bounds, sensitization, and hazard freedom are four different claims requiring different evidence. Transport and inertial delay models can predict different short-pulse behavior. Neither the laboratory's settled values nor a truth table alone establish analog glitch behavior.

<!-- FIGURE:timing -->

## Integrated design case studies

### A saturating two-bit incrementer with validity

Let unsigned input $x=2A+B$, enable $E$, and output $Y_1Y_0$. If disabled, output zero; if enabled, output $\min(x+1,3)$. Validity is $V=E$. First derive the enabled mapping: 00→01, 01→10, 10→11, 11→11. Therefore the enabled output bits are $A+B$ and $A+\overline B$. Adding the disabled obligation gives $Y_1=E(A+B)$ and $Y_0=E(A+\overline B)$. Both output OR expressions can reuse $A$, but this does not create a shared gate by itself. Under a NOT/AND/OR two-input library, the direct mapping uses one inverter, two OR gates, and two AND gates, totaling five. With E zero, both outputs are forced zero; with E one, all four enabled rows match the arithmetic specification. This design differs from modular increment, whose enabled mapping 11→00 would require XOR and complement equations instead.

### A BCD interface with explicit invalid behavior

For input $ABCD$ in binary order, decimal validity is $V=\overline A+\overline B\overline C$ because all codes 0–7 are valid when $A=0$, and only 8–9 remain valid when $A=1,B=C=0$. An enabled decimal successor maps 0–8 to their successor and 9 to 0. If invalid codes 10–15 are unspecified, minimizing each successor bit may exploit those rows. If the output must instead equal zero on invalid codes, mask a correct valid-domain successor with $V$ or derive the full table directly. Masking retains validity information but may increase depth and may produce transient invalid intermediate states while several inputs change. The functional contract must precede a claim that these are harmless.

### A request controller with assertions

For the priority block, prove three independent properties: grants are mutually exclusive; every enabled request gets one grant; and no grant appears when disabled. The earlier identities prove these properties for all eight input rows. Then separately prove the output code or associated data matches the granted requester. A one-hot grant proof alone cannot prove correct payload routing. In a practical module, preserve this separation using named output equations and assertion obligations. The adjustable laboratory below computes all rows, internal nets, exact gate costs, and a counterexample set for a deliberately faulty alternative; it makes these distinctions observable.

## Fully worked mathematical and conceptual problem bank

The two authentic questions are clearly marked as revisits, not new unique archive questions. The original problems span contract completion, select-choice analysis, multiple-output circuits, gate mapping, fault activation/propagation, structural timing, bit-vector interfaces, and proof counterexamples. Every solution states the convention that makes its numerical or logical conclusion meaningful. Difficulty is an author judgment rather than a measured examination score calibration.

<!-- INCLUDE:problems -->

## Complete summary and examination rules

Use the following full statements after studying the lesson. They summarize a reasoning method without replacing the derivations or the worked solutions. Read the cost, polarity, care, and timing assumptions before applying any formula.

<!-- INCLUDE:review -->

## Adjustable verification laboratory

Choose the input bits and a reference/candidate pair. The laboratory derives internal values, enumerates the complete truth table, reports all discrepancy rows, and animates topological evaluation. The correct shared network has $p=AB$, $q=C+D$, $r=pq$, $Y=r$, and $Z=AB+C$. Its deliberately faulty alternative changes $Z$ to $AB(C+D)+C$. A second mode compares the priority grants with the incorrect independent-grant implementation. A third mode compares factored $A(B+C)$ against its three-NAND implementation or an incorrect NAND cascade. Changing an input restarts the trace; it does not silently retain an old result.

The lab uses settled two-valued Boolean semantics. Its propagation times are structural upper bounds for the declared equal-delay gates, not an electrical waveform simulator. Default input values are demonstrations, not questions you are required to answer. Previous/next, seek, reset, play/pause, enlargement, and reduced-motion behavior are available in the animation controls.

<!-- LAB:combin -->

## References and scope of the evidence

1. **MIT — Chris Terman.** *6.004 Computation Structures*, Spring 2017, Lecture 4 written annotations, especially functional specifications, bounded-fan-in organization, muxes, decoders and ROMs. [Official text](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/).
2. **Stanford — Philip Levis; William J. Dally, reader author.** *EE108A*, Winter 2008 archived reader, Chapter 6, PDF pages 83–105; acyclic composition and design method. [Official reader](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf).
3. **Cambridge — Ian J. Wassell.** *Digital Electronics*, 2025–26, combined slides 55–70; multilevel factoring and implementation alternatives. [Official materials](https://www.cl.cam.ac.uk/teaching/2526/DigElec/materials.html).
4. **Cornell — Christopher Batten.** *ECE2300 / ENGRD2300*, Fall 2026, T02 Combinational Logic, all 34 PDF pages, revision 2026-09-03-23-48. [Official handout](https://www.csl.cornell.edu/courses/ece2300/handouts/ece2300-T02-comb-logic.pdf).
5. **Berkeley — Randy H. Katz.** *CS150*, Fall 2005, Lecture 2, 73 slides in 37 PDF pages; cost, multiple outputs and polarity mapping. [Official slides](https://people.eecs.berkeley.edu/~randy/Courses/CS150.F05/Lectures/02-CombLogic.pdf).
6. **Iranian examination archive.** PhD CE 1405 Q23 and MSc CE 1404 Q80, original PDF pages 6 and 19, pinned repository commit `bdadf6e2c9cadc4772ae137a96a3da753c7cfd08`. The bank records exact file paths and SHA-256 fingerprints. [Repository](https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/main/Exams).

The detailed [source audit](../reviews/g_combin-sources.html) records actual reading and reconciled conventions. The [quality audit](../reviews/g_combin-quality.html) records observed verification and remaining limits. Dedicated arithmetic blocks, detailed mux/encoder design, full timing analysis, and hazard theory continue in their respective chapters. This chapter is a review draft until explicitly approved. Its finite checks support the authored material; they cannot guarantee the answer to every conceivable unseen examination question.
