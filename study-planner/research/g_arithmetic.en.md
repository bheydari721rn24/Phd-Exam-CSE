# Adders, Comparators, and Arithmetic Circuits

## 1. Boundary, prerequisites, and sources

This chapter develops exact fixed-width integer arithmetic from single-bit gates to complete combinational datapaths. You should already understand truth tables, Boolean algebra, binary weights, two's-complement encoding, and acyclic circuit timing. The main progression is addition, carry acceleration, subtraction, comparison, decimal correction, multioperand compression, multiplication, and division. Sequential controllers, floating-point rounding standards, transistor sizing, and implementation-specific chip pinouts belong to later or separate boundaries. Their existence is identified where it changes an assumption.

The four principal written courses are MIT 6.004 (Chris Terman, Spring 2017), Stanford EE108A (Philip Levis, Winter 2008; reader by William J. Dally), Berkeley CS150 (Randy H. Katz, Fall 2000), and ETH Zurich Digital Design and Computer Architecture (Onur Mutlu, Spring 2020). The exact passages actually read, comparisons, accessible alternatives, and limits are recorded in the [source audit](../reviews/g_arithmetic-sources.html). Written material was selected for this boundary rather than university name alone. Original explanations and problems below reconcile differing index conventions and identify erroneous or incomplete source examples.

The visual models use exact Boolean states. Their operation-by-operation order is a teaching dependency order, not measured electrical time. A timing bound is valid only under its stated gate model. A visible unknown value means that the teaching model has not yet established that value; it is not an IEEE four-state HDL value.

## 2. Specify the number before specifying the circuit

Let the unsigned values of two bit vectors be $A=\sum_{i=0}^{n-1}a_i2^i$ and $B=\sum_{i=0}^{n-1}b_i2^i$. Index zero is the least significant bit. Addition with a single incoming carry obeys the integer identity

$$A+B+c_0=S+2^nc_n.$$

Here $0\le S<2^n$ is the retained word and $c_n$ is the extra carry. Since the largest input total is $2^{n+1}-1$, exactly one extra bit suffices. Dropping that bit deliberately changes the specification to arithmetic modulo $2^n$.

The same input wires may instead represent signed values $A_s=A-a_{n-1}2^n$ and $B_s=B-b_{n-1}2^n$. The low result bits are identical for signed and unsigned addition because subtracting a multiple of $2^n$ does not change a residue. The interpretation of overflow differs. Thus a single hardware adder can serve both interpretations while its status flags answer different questions. Decide the operand interpretation, output width, incoming carry, and flag meanings before calculating.

## 3. Half adder: derive both outputs

Two equal-weight bits total zero, one, or two. The sum bit is the parity of the inputs, while the carry is one precisely when both are one:

$$s=a\oplus b,\qquad c=ab.$$

| a | b | s | c |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

An XOR gate and an AND gate implement this contract. The carry output has twice the positional weight of the sum. Two inputs do not make the half adder a replacement for every bit of a multiword adder: an interior position must also accept the carry produced below it. If the overall input carry is permanently zero, the least significant position can be a half adder; otherwise it must be a full adder.

<!-- SIM: full -->

## 4. Full adder and the weighted conservation law

A full adder totals $a+b+c$ for three bits of equal weight. Its outputs satisfy $a+b+c=s+2d$. Parity gives the sum, and majority gives the carry:

$$s=a\oplus b\oplus c,\qquad d=ab\lor ac\lor bc.$$

The carry formula follows by dividing the eight valuations into totals zero, one, two, and three. Both total two and total three need a carry; exactly these valuations contain at least one pair of ones. Equivalently, compute $p=a\oplus b$ and $g=ab$, then use

$$s=p\oplus c,\qquad d=g\lor pc.$$

Two half adders and one OR gate realize this second form. The intermediate carries $g$ and $pc$ cannot both be one because $g=1$ forces $p=0$. An XOR could therefore combine these particular carry terms, although this is not permission to replace arbitrary OR gates by XOR gates.

The conservation law is more useful than memorizing a picture. Multiplying it by $2^i$ proves that an output carry must enter column $i+1$. It also explains why a full adder is a three-to-two compressor, not an adder that emits a three-bit result.

## 5. Ripple addition: local correctness implies word correctness

Connect each carry output to the carry input of the next more significant position. For each bit,

$$a_i+b_i+c_i=s_i+2c_{i+1}.$$

Multiply by $2^i$ and sum over all positions. The interior carry terms appear once on each side and cancel, leaving the word identity from Section 2. This proves correctness for every width and every input, including a nonzero incoming carry.

For `1011 + 0110`, begin at the right: the four local totals are one, two, two, and two. The sum bits from low to high are one, zero, zero, zero, and the outgoing carry is one. Therefore the exact result is `10001`, not merely `0001`. Interpret the same operands as signed four-bit integers and the arithmetic becomes negative five plus six equals one; the outgoing carry does not indicate a signed error.

<!-- SIM: ripple -->

## 6. Timing requires a specified implementation

For the factored full adder, define XOR delay $t_X$, AND delay $t_A$, and OR delay $t_O$. Let $T(x)$ be the latest arrival time assigned to signal $x$. Conservative structural bounds are

$$T(p_i)=\max(T(a_i),T(b_i))+t_X.$$
$$T(g_i)=\max(T(a_i),T(b_i))+t_A.$$
$$T(c_{i+1})=\max(T(g_i),\max(T(p_i),T(c_i))+t_A)+t_O.$$
$$T(s_i)=\max(T(p_i),T(c_i))+t_X.$$

The longest structural bound does not automatically prove that a Boolean transition can sensitize that complete path. Conversely, observing an early answer for one input does not establish the worst-case bound. Under simultaneous arrivals and unit delay for the three stated gate types, $T(c_i)=2i+1$ for positive $i$, $T(s_0)=2$, and $T(s_i)=2i+2$ for positive $i$. Thus both the last sum and outgoing carry have conservative bounds $2n$ and $2n+1$, respectively. A question giving precomputed propagate/generate signals or a different full-adder carry delay has a different result.

A ripple adder has linear carry depth and linear area in the width, under bounded-size gate assumptions. Include an output flag or result-selection gate only when that output is requested. Never append an arbitrary XOR delay to a carry-only answer.

## 7. Generate, propagate, and kill

At one position, define XOR propagation $p_i=a_i\oplus b_i$ and generation $g_i=a_ib_i$. There are three disjoint behaviors: `00` kills any incoming carry; `01` or `10` propagates it; `11` generates an outgoing carry independently of the input. Therefore $c_{i+1}=g_i\lor p_ic_i$.

Some courses define an OR propagate $q_i=a_i\lor b_i$. The carry equation $c_{i+1}=g_i\lor q_ic_i$ remains valid because when $p_i$ and $q_i$ differ, generation already forces carry one. However, $s_i=q_i\oplus c_i$ is false. For $a_i=b_i=1,c_i=0$, it predicts one instead of zero. Use XOR propagation for the sum and for the disjoint three-state interpretation; explicitly identify another convention if encountered.

## 8. Expand the carry recurrence without changing bit order

Successive substitution gives

$$c_1=g_0\lor p_0c_0.$$
$$c_2=g_1\lor p_1g_0\lor p_1p_0c_0.$$
$$c_3=g_2\lor p_2g_1\lor p_2p_1g_0\lor p_2p_1p_0c_0.$$
$$c_4=g_3\lor p_3g_2\lor p_3p_2g_1\lor p_3p_2p_1g_0\lor p_3p_2p_1p_0c_0.$$

Every generation term travels through all more significant propagate terms between its position and the requested carry. The final term represents the external input traveling through the whole range. Omitting one intermediate propagate creates a circuit that can carry across a killing bit. Reversing the significance order makes a generating low bit override a killing high bit, which is equally wrong.

A flat sum-of-products realization can have two carry-logic levels only if large fan-in gates are admitted and propagation/generation are already available. As width increases, the product terms and fan-in increase. With bounded fan-in, realizing each wide product and OR requires trees; the flat formula is not a constant-delay asymptotic implementation.

## 9. Group carry and an associative composition

For adjacent high and low groups, represent each group by the Boolean carry function $f(c)=G\lor Pc$. Compose high after low:

$$G=G_H\lor P_HG_L,\qquad P=P_HP_L.$$

This pair is associative because function composition is associative. It is generally not commutative: high kill after low generate kills the final carry, while high generate after low kill generates it. Associativity allows regrouping; it does not allow reordering.

For bits three through zero, $P=p_3p_2p_1p_0$ and $G=g_3\lor p_3g_2\lor p_3p_2g_1\lor p_3p_2p_1g_0$. Then $c_4=G\lor Pc_0$. With XOR propagation, the identity pair for an empty interval is $(G,P)=(0,1)$: it passes carry unchanged. This makes recursive and prefix constructions work even when the width is not a power of two.

<!-- SIM: prefix -->

## 10. Prefix and hierarchical lookahead architectures

A balanced group tree computes the carry behavior of a complete range using $n-1$ binary combine cells. It can establish the final carry in logarithmic combine depth. Establishing every interior carry requires additional distribution or prefix work. Do not count one reduction tree as a complete all-prefix network.

In a two-tree design, propagate/generate information travels upward, and incoming carry information travels downward. In a parallel-prefix design, each bit obtains the prefix covering positions zero through that bit. Kogge–Stone favors short depth and bounded fan-out but uses many interconnects; Brent–Kung reduces cell count and wiring at additional stages. For power-of-two widths, a standard full Kogge–Stone prefix graph has $\log_2n$ prefix stages and $n\log_2n-n+1$ combine cells. This count excludes initial bit propagation/generation and final sums. A textbook tree diagram with $n-1$ cells may instead produce only the full-group reduction.

If four-bit lookahead blocks are cascaded by their block carries, block-to-block ripple remains. A second level must combine block propagate/generate pairs to accelerate that dependency. Internal lookahead alone does not guarantee whole-word logarithmic delay. All these claims refer to bounded logical cells; physical wire delay and buffering may alter actual performance.

## 11. Carry select: compute alternatives, then resolve the choice

A block can precompute two candidate results using incoming carries zero and one. The real incoming carry selects the correct sum and outgoing carry. For an eight-bit adder split into two four-bit blocks, the low block is computed once and the high block twice: twelve full-adder bit slices plus five one-bit result/carry selectors in a straightforward implementation. The extra hardware avoids waiting before starting the high arithmetic.

If low and candidate blocks arrive at time $D$, the selected high result arrives at $D+t_M$. More generally use $\max(T_{candidate},T_{select})+t_M$. Equal-width block carry select has a delay proportional to the block ripple cost plus the number of selectors crossed. Balancing $k$-bit ripple blocks against $n/k$ selector stages gives a square-root-width optimum under the simple equal-block model, not logarithmic depth. Recursively duplicating complete carry-select subcircuits is a different architecture with a different area recurrence.

<!-- SIM: select -->

## 12. Carry skip and increment/decrement

A block whose XOR group propagate equals one passes its incoming carry to the outgoing carry. A skip structure therefore selects between the block's ripple output and the incoming carry. Its delay depends on skip condition generation, selector delay, and end-block ripple; a claim about one path must not ignore the arrival time of the group condition. The bypass is semantically safe because when every bit propagates, generation is zero everywhere in that block.

An incrementer toggles bit zero and toggles bit $i$ precisely if all lower original bits are one. A decrementer toggles bit $i$ precisely if all lower original bits are zero. These are prefix conditions. Incrementing the largest unsigned word gives zero and a carry; decrementing zero gives the largest word and a borrow. A negator performs complement plus one, but negating the most negative signed value cannot produce its positive counterpart at the same width.

## 13. Subtractors and the meaning of borrow

A half subtractor computes $a-b=d-2r$: $d=a\oplus b$, and $r=\overline a b$. A full subtractor includes incoming borrow $r_i$:

$$d_i=a_i\oplus b_i\oplus r_i.$$
$$r_{i+1}=\overline a_i b_i\lor\overline{a_i\oplus b_i}\,r_i.$$

Derive the second expression by considering $a_i=b_i$ versus unequal bits. Equal bits pass an incoming borrow. The valuation zero minus one produces a borrow even without an incoming one. The valuation one minus zero kills it. Weighted telescoping yields $A-B-r_0=D-2^nr_n$.

The two's-complement adder realization computes $A+\overline B+1=A-B+2^n$. Therefore its outgoing carry is one when unsigned $A\ge B$, and zero when a borrow is needed. Carry is the complement of borrow in this implementation. Architecture manuals may label a subtraction flag either carry/no-borrow or borrow; the signal name alone is insufficient.

<!-- SIM: subtract -->

## 14. One shared add/subtract circuit

Let mode $m=0$ select addition and $m=1$ select subtraction. Feed $b'_i=b_i\oplus m$ and $c_0=m$ to the adder. This computes $A+B$ in add mode and $A+\overline B+1$ in subtract mode. Inverting only the operand without setting the initial carry subtracts one too much. Setting only the carry adds one without negating the operand.

The overflow calculation uses the carries into and out of the sign position of this actual operation. For subtraction, do not apply the addition equal-input-sign test to the original uncomplemented operands. The subtraction-specific sign formula is $(a_{n-1}\oplus b_{n-1})(a_{n-1}\oplus s_{n-1})$.

## 15. Signed overflow: prove the flag

For ordinary addition with zero incoming carry, signed overflow is

$$V=\overline{a_{n-1}\oplus b_{n-1}}\,(a_{n-1}\oplus s_{n-1}).$$

Opposite-sign operands sum inside the representable interval. Two nonnegative operands can only overflow upward; their retained result then has sign one. Two negative operands can only overflow downward; their retained result then has sign zero. This proves the sign criterion.

The gate equivalent is $V=c_{n-1}\oplus c_n$. To prove it, separate the sign-bit operands into `00`, mixed, and `11`. For `00`, outgoing carry is zero and incoming carry one is exactly positive overflow. Mixed inputs propagate the incoming carry, so the carries agree and there is no overflow. For `11`, outgoing carry is one, and incoming carry zero gives negative overflow. This argument also handles a legitimate incoming carry to the whole addition: it describes the exact signed total including that input. For add/subtract hardware, use the effective complemented second sign bit.

For four bits, seven plus one has carry zero and signed overflow one. Negative one plus one has carry one and signed overflow zero. Negative eight plus negative eight has both flags one. Zero plus zero has both zero. All four combinations are possible, so no implication between these two flags is generally valid.

## 16. Signed extension, saturation, and fixed-point alignment

Extending an unsigned word fills new high bits with zero. Extending a two's-complement word repeats its sign bit. The latter preserves value because the additional positive weights of repeated ones cancel the changed negative sign weight. Perform extension before addition if an exact wider result is required; extending a wrapped narrow result cannot recover the discarded information.

A signed saturating adder returns the exact result if it is representable, otherwise the closest endpoint. For an $n$-bit word those endpoints are $-2^{n-1}$ and $2^{n-1}-1$. On signed addition overflow, the original operand sign identifies the direction: nonnegative inputs saturate high, negative inputs saturate low. An unsigned saturating adder returns all ones when carry is one. These are different circuits.

Fixed-point addition uses the same integer datapath only after aligning binary points. If an integer encoding $X$ represents $X2^{-f}$, equal fractional widths can be added directly. Different widths require scaling the coarser encoding by a power of two and retaining enough range. Multiplication adds the two fractional widths. Reducing a result's fractional width requires an explicit rounding rule; arithmetic right shift rounds a negative exact encoding toward negative infinity, not necessarily toward zero.

## 17. Equality and unsigned magnitude comparison

Equality is the AND of bitwise XNORs. Under two-input combining gates, a balanced tree has logarithmic depth rather than the linear depth of a chain. For magnitude, the most significant differing position decides. A high bit's weight exceeds the sum of every lower weight, so no lower pattern can reverse that decision.

Define $e_i=\overline{a_i\oplus b_i}$ and $h_i=a_i\overline b_i$. A low-to-high recurrence is $H_0=0$, $H_{i+1}=h_i\lor e_iH_i$. Each higher bit overrides the accumulated lower decision when unequal, or preserves it when equal. Alternatively, scan high to low, preserving both an equality-so-far and a decision. The output pair $(E,H)$ for a high/low group obeys the same ordered composition $H=H_H\lor E_HH_L$, $E=E_HE_L$. Hence comparison also admits prefix acceleration.

<!-- SIM: compare -->

## 18. Signed comparison from a subtractor

For signed two's-complement subtraction, define $N$ as the result sign, $Z$ as the zero-result flag, and $V$ as signed overflow. Then signed less-than is $N\oplus V$, equality is $Z$, and signed greater-than is $\overline Z\,\overline{N\oplus V}$. Overflow reverses the sign indication, so correction is essential.

For four-bit seven minus negative one, the mathematical answer is eight, but the retained bits are `1000`: $N=1,V=1$, so signed less-than is zero. Looking only at $N$ would incorrectly claim seven is smaller. For unsigned comparison through the complement-and-add subtractor, use the no-borrow carry instead. Applying that unsigned flag to a signed ordering is wrong whenever the sign interpretations differ.

## 19. BCD correction: a decimal carry is not every binary carry

Each valid BCD operand digit lies between zero and nine, so two digits and a decimal carry total at most nineteen. First compute the five-bit binary total $T=16k+z$, where $z$ has bits $z_3,z_2,z_1,z_0$. A decimal correction is needed iff $T>9$:

$$q=k\lor z_3z_2\lor z_3z_1.$$

If $k=0$, the invalid low results ten through fifteen have bit three one and at least one of bits two and one one. If $k=1$, totals sixteen through nineteen require correction even though their low four bits look like valid digits. Add $6q$ to $z$ and keep the low four bits. The outgoing decimal carry is $q$.

Why six? Binary wraps at sixteen, decimal wraps at ten, and the difference is six. For totals ten through fifteen, the correction addition itself produces a binary carry. For sixteen through nineteen, it may not; the first addition already produced one. Therefore the second adder's carry alone is not the decimal carry. The procedure assumes valid input digits. Invalid BCD inputs require a separate validity contract and detector.

<!-- SIM: bcd -->

## 20. Carry-save compression and a width proof

Three same-width unsigned words can be compressed column by column with full adders. Let $S$ collect the sum outputs and let $C$ collect the carry outputs before shifting. Then

$$X+Y+Z=S+2C.$$

No carry crosses between columns during this compression layer; all columns operate independently. A final carry-propagating adder adds $S$ and the shifted carries to obtain conventional binary representation. Omitting that shift halves every carry weight. If an $n$-bit layer is used, retain the most significant carry when forming the $n+1$-bit shifted vector. The exact sum of three $n$-bit inputs may need $n+2$ output bits.

Repeated three-to-two compression reduces the number of operand rows, which differs from reducing word width. Wallace or Dadda scheduling preserves the sum of all column weights and eventually leaves two rows. A reduction tree followed by a final adder can achieve logarithmic logical depth under bounded-size cell assumptions, with quadratic area for a square unsigned multiplier's partial products. Exact compressor counts depend on the column heights and schedule.

<!-- SIM: csa -->

## 21. Unsigned multiplication and partial-product weights

An unsigned $n$-by-$m$ multiplication generates $nm$ AND partial products. The partial product $a_ib_j$ belongs to weight $2^{i+j}$, so

$$AB=\sum_{i=0}^{n-1}\sum_{j=0}^{m-1}(a_ib_j)2^{i+j}.$$

The maximum product is below $2^{n+m}$, making $n+m$ bits sufficient. In column accumulation, each sum stays in its column and each carry moves exactly one column left. An array diagram is correct only if every connection preserves these weights. For four-bit thirteen times eleven, rows are thirteen, twenty-six, zero, and one hundred four; their sum is one hundred forty-three, or `10001111`.

Rows may be accumulated with successive full-width additions, with a regular array, or with a compressor tree. These circuits share arithmetic but not necessarily depth. A naive chain of $m-1$ independent $n+m$-bit ripple adders has a different structural bound from a diagonal carry-save array. State the actual topology before asserting its asymptotic delay.

<!-- SIM: multiply -->

## 22. Signed multiplication and Booth recoding

The most significant two's-complement bit has negative weight. Sign-extend the multiplicand partial products, and subtract the row associated with the multiplier's sign bit. For four bits, negative three has encoding thirteen and negative two has encoding fourteen. Unsigned multiplication of those encodings gives one hundred eighty-two, while their signed product is six. The low four product bits coincide modulo sixteen, but the full eight-bit results do not.

An exact weighted expression uses positive lower-bit products, negative cross terms involving exactly one sign bit, and a positive term involving both sign bits. Baugh–Wooley reorganizes those negative terms using complemented partial products and correction constants; the constants depend on widths and layout and must be derived rather than copied from a different-width diagram.

For n-bit A and m-bit B, write the signed product explicitly:

$$A_sB_s=\sum_{i=0}^{n-2}\sum_{j=0}^{m-2}a_ib_j2^{i+j}-\sum_{i=0}^{n-2}a_ib_{m-1}2^{i+m-1}-\sum_{j=0}^{m-2}a_{n-1}b_j2^{n-1+j}+a_{n-1}b_{m-1}2^{n+m-2}.$$

Each negative-weight Boolean product x can be replaced by its complement: $-x2^k=(1-x)2^k-2^k$. The weights subtracted across the two cross-term rows sum to $2^{n+m-1}-2^{m-1}-2^{n-1}$. Therefore the complemented array needs correction constant $2^{n+m-1}+2^{m-1}+2^{n-1}$ modulo $2^{n+m}$. For equal widths, combine the duplicated $2^{n-1}$ terms into $2^n$. These constants describe this exact two's-complement weighted arrangement, not every diagram labeled Baugh–Wooley.

For four-bit negative three times negative two, lower unsigned portions are five and six. Their product contributes thirty; complemented negative rows contribute sixteen and eight; the double-sign term contributes sixty-four; the correction constant is one hundred forty-four. Their total is 262, whose low eight bits represent six. This calculation checks the array's constants against the exact signed product without requiring a memorized circuit layout.

Radix-two Booth recoding sets an implicit lower bit $b_{-1}=0$. At position $i$, the ordered pair $(b_i,b_{i-1})$ `01` selects addition of the multiplicand shifted by $i$, `10` selects subtraction, and `00` or `11` selects zero. This follows from the identity $B_s=\sum_{i=0}^{n-1}(b_{i-1}-b_i)2^i$. A run of consecutive ones becomes a difference of two powers of two, reducing the number of nonzero rows. Recoding does not by itself promise faster execution when a sequential machine performs a fixed number of iterations. Extra internal width is needed when negating the most negative multiplicand.

<!-- SIM: booth -->

## 23. Binary division: invariant before implementation

For unsigned divisor $D>0$, process the dividend bits from most to least significant. Suppose the already processed prefix satisfies $P=DQ+R$ with $0\le R<D$. On receiving next bit $x$, set $U=2R+x$. Since $U<2D$, the next quotient bit is $q=1$ iff $U\ge D$. Set $R'=U-qD$ and $Q'=2Q+q$. Then $2P+x=DQ'+R'$ and the remainder stays in range. Induction proves the complete division.

The compare/subtract decision can use the no-borrow carry of a sufficiently wide subtractor. Since $U$ may need one more bit than $D$, discarding that bit before the comparison is unsafe. A restoring implementation re-adds the divisor after an unsuccessful trial subtraction, while a conditional-subtract implementation simply selects the previous candidate. An unrolled combinational divider and a reused iterative divider have distinct hardware cost, latency, and throughput. Division by zero has no valid quotient/remainder contract; signed minimum divided by negative one overflows at the original width.

<!-- SIM: division -->

## 24. ALU controls, multiple-word arithmetic, and flags

A combinational ALU selects among specified arithmetic and Boolean functions. A shared adder can supply addition, subtraction, increment, decrement, negation, and comparison. Bitwise operations do not have a mathematical carry chain, although a particular architecture may clear, retain, or redefine flags. Never infer flag updates from the value operation alone.

To add multiple words, send the low word's carry into the next word's addition; this conserves positional weight. For subtraction through direct borrow units, send the borrow. Through complement-and-add units, the equivalent incoming carry is one minus the borrow. If an intermediate instruction overwrites the carry flag before it is consumed, the program no longer implements the intended multiword arithmetic.

The historical Berkeley processor exercise provides an important design pattern: define each instruction's result and carry-register update separately. Here its arithmetic idea is reconstructed with new operands; the surrounding processor/controller is outside this chapter. A comparison flag consumed after a delayed instruction must still refer to the operands intended by the contract.

## 25. Width-safe hardware description and verification

This original parameterized SystemVerilog example states unsigned wire widths explicitly. Signed interpretation is handled by flag equations, rather than relying on implicit expression extension. Its parameter must satisfy $N\ge2$.

```systemverilog
module addsub #(parameter int N = 4) (
  input  logic [N-1:0] a, b,
  input  logic sub,
  output logic [N-1:0] result,
  output logic carry_no_borrow, overflow
);
  logic [N-1:0] effective_b;
  logic [N:0] wide;
  assign effective_b = b ^ {N{sub}};
  assign wide = {1'b0, a} + {1'b0, effective_b}
              + {{N{1'b0}}, sub};
  assign result = wide[N-1:0];
  assign carry_no_borrow = wide[N];
  assign overflow = (~(a[N-1] ^ effective_b[N-1]))
                  & (a[N-1] ^ result[N-1]);
endmodule
```

The explicit extra bit prevents accidental loss of carry due to intermediate sizing. A behavioral `+` does not uniquely specify ripple, lookahead, or a library-mapped implementation. Exact mathematical checks in this chapter verify the Boolean/arithmetic contract; they do not constitute HDL compilation, gate-level timing signoff, or physical electrical simulation.

Test both interpretations, all flag combinations, zero, all ones, sign endpoints, mixed signs, carry entering the sign position, no-borrow equality, and BCD totals on either side of nine and fifteen. Check identities and invariants at intermediate checkpoints, not only the final answer.

## 26. Summary: an ordered solution procedure

Read a problem in this order. First specify bit widths, encoding, retained outputs, and flag conventions. Second derive the local gate or column equations. Third apply weighted conservation, the carry/borrow recurrence, or the comparison invariant. Fourth compute the mathematical result independently and reconcile the retained residue with its interpretation. Fifth, for timing, name the actual critical output and its implementation model. Finally test one boundary or counterexample capable of refuting the chosen answer.

The central distinction is between an exact integer, its low fixed-width residue, and the semantic flags attached to that residue. Carry acceleration reorganizes dependencies without changing this arithmetic identity. Compression preserves total weight while leaving a redundant representation. Comparison preserves significance order. Decimal correction changes the wrapping base. These are the principles that make unfamiliar circuits solvable.

## 27. Fully worked problem bank

Each solution explains its derivation, conditions, and a transferable decision rule. Original problem families use new data and independently written reasoning. Reconstructed course patterns are attributed; authentic archive bridges identify their original PDF page and do not pretend to supply an official answer key. Open solutions after reading the corresponding teaching section. No test response is requested from the student during this first reading.

<!-- INCLUDE: problems -->

## 28. Final examination notes and boundary rules

<!-- INCLUDE: review -->

## 29. Editable arithmetic laboratory

<!-- LAB: arithmetic -->

## 30. References and verified limits

1. [MIT, 6.004 Computation Structures, Chris Terman, Spring 2017: Lecture 8 written annotations, adder and multiplier tradeoffs](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c8/c8s1/).
2. [Stanford, EE108A Winter 2008, Philip Levis; William J. Dally, EE108 Class Notes: comparator pages 147–149, arithmetic pages 191–211, lookahead pages 229–232](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf).
3. [University of California, Berkeley, CS150 Fall 2000, Randy H. Katz: Arithmetic Circuits, all nine PDF pages](https://people.eecs.berkeley.edu/~randy/Courses/CS150.F00/Lectures/09-Arith.pdf).
4. [ETH Zurich, Digital Design and Computer Architecture, Onur Mutlu, Spring 2020: Lecture 5, Combinational Logic II, arithmetic and comparator passages](https://safari.ethz.ch/digitaltechnik/spring2020/lib/exe/fetch.php?media=onur-digitaldesign-2020-lecture5-combinational-logic-ii-afterlecture.pdf).
5. [Berkeley CS150, Randy H. Katz, Fall 2000, Problem Set 10/11: arithmetic and carry-register specification](https://people.eecs.berkeley.edu/~randy/Courses/CS150.F00/HWs/HW10_11.pdf).

Course references support the scope and terminology; this lesson's proofs, reconciliations, circuits and original problem data are independently constructed. The accessible candidate pool is documented and bounded, not every course worldwide. The verified domain is finite-width binary arithmetic, the stated gate models, and the saved/default laboratory traces. Physical analog behavior, all possible implementation toolchains, and guaranteed performance on every unseen examination question are outside that verification. Known in-scope errors must be corrected before this review draft is marked complete.
