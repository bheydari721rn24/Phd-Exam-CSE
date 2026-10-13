## Q1

Correct option: 4.

**Trace actual connected nets.** The first NAND gives $t=\neg(xy)$. Because $u=\neg(xt)$ and $v=\neg(yt)$, De Morgan at the fourth NAND gives
$$F_1=\neg(uv)=xt+yt=t(x+y)=\neg(xy)(x+y).$$
Using $\neg(xy)=\neg x+\neg y$, expand and eliminate $x\neg x$ and $y\neg y$ to obtain $F_1=x\neg y+(\neg x)y=x\oplus y$. The final NAND has its two inputs tied to $v$, so it is an inverter:
$$F_2=\neg(vv)=\neg v=yt=y\neg(xy)=y\neg x.$$

| $xy$ | $t$ | $u$ | $v$ | $F_1$ | $F_2$ |
|---|---|---|---|---|---|
| 00 | 1 | 1 | 1 | 0 | 0 |
| 01 | 1 | 1 | 0 | 1 | 1 |
| 10 | 1 | 0 | 1 | 1 | 0 |
| 11 | 0 | 1 | 1 | 0 | 0 |

**Interpret both outputs.** One-bit subtraction obeys the ordinary integer relation $x-y=F_1-2F_2$: the borrowed case $01$ gives $-1=1-2$. Thus these are difference and borrow, option 4. Options 1 and 2 require equality as the first output; equality is XNOR and disagrees at $00$. A half-adder has carry $xy$, which is one at $11$ and zero at $01$, opposite to the relevant borrow cases. Identifying only the XOR subnetwork is not sufficient; the second output distinguishes addition from subtraction. This is a binary steady-state analysis, not a propagation-delay model.

## Q2

Correct option: 4.

**Apply the declared select convention at each stage.** A two-to-one multiplexer computes $\operatorname{MUX}(s,I_0,I_1)=(\neg s)I_0+sI_1$. The first stage has $I_0=1$, $I_1=0$, $s=b$, hence $t=\neg b$. The second has $I_0=t$, $I_1=0$, $s=a$, giving
$$F=(\neg a)t+a\cdot0=(\neg a)(\neg b)=\neg(a+b).$$
Both select bits must be zero to maintain a connected path to the constant one. If either select becomes one, its selected data branch is the constant zero.

| $ab$ | First output $t$ | Second selected input | $F$ |
|---|---|---|---|
| 00 | 1 | $I_0=t$ | 1 |
| 01 | 0 | $I_0=t$ | 0 |
| 10 | 1 | $I_1=0$ | 0 |
| 11 | 0 | $I_1=0$ | 0 |

**Compare all candidate functions.** NOR has vector $1,0,0,0$, exactly the table, so option 4 is correct. XNOR has $1,0,0,1$ and wrongly accepts $11$. XOR has $0,1,1,0$ and fails at $00$ as well as both mixed rows. NAND has $1,1,1,0$ and wrongly accepts the mixed rows. Digits inside a mux identify the select *value*; they are not constants injected into the output algebra. Digits on the incoming data wires are constants. Keeping these roles separate prevents a wrong inversion or a false NAND recognition.

## Q3

Correct option: 3.

**One loop traversal reverses the observed logic level.** An odd number of inverters returns the opposite level to a chosen node after the sum of their transition delays. In the stated symmetric fixed-delay model, five stages at $5\,\mathrm{ns}$ give one half-period of $5\cdot5=25\,\mathrm{ns}$. The opposite edge must traverse the loop again before the starting node returns to its original level, so
$$T=2\cdot5\cdot5\,\mathrm{ns}=50\,\mathrm{ns}.$$
Frequency is the reciprocal of the full period, not the reciprocal of one traversal:
$$f=\frac{1}{50\cdot10^{-9}\,\mathrm{s}}=20\cdot10^6\,\mathrm{Hz}=20\,\mathrm{MHz}.$$
This selects option 3. A dimensional shortcut is $f_{\mathrm{MHz}}=1000/T_{\mathrm{ns}}$; using 50 directly as seconds would lose nine orders of magnitude.

**Alternatives and model boundary.** Forty megahertz uses the25 ns half-period as a full period. Ten megahertz would double the correct full period once more to100 ns. Five megahertz would use200 ns, an unjustified further factor of four. The ordinary ring formula requires odd inversion count and assumes an established oscillating regime with the specified transition delays. It does not prove startup, amplitude, edge rate, or a measured physical frequency. If rise/fall delays differ, sum both directional traversals; there is no justification for using one common delay unless the question supplies it.

## Q4

Correct option: 2.

**Separate the Elmore contributions that scale differently.** For a fixed RC topology, an Elmore moment is a sum of terms $R_{\mathrm{shared},j}C_j$, where the resistance is the portion shared by the source-to-output and source-to-capacitor paths. Uniformly doubling this gate's transistor widths halves each relevant on-resistance. Its width-dependent diffusion/internal capacitances double, while the explicitly specified next-stage load remains fixed.

For an internal term, $(R/2)(2C)=RC$. For a fixed-load term, $(R/2)C_L=RC_L/2$. For each modeled switching case, group the initial positive contributions as $I$ and $L$:
$$D=I+L,\qquad D'=I+L/2.$$
Consequently
$$D'/D=\frac12+\frac{I}{2(I+L)},\qquad 1-D'/D=\frac{L}{2(I+L)}.$$
With positive internal capacitance and positive load, both fractions establish $1/2<D'/D<1$ for that case. To handle the requested maximum, the case maximizing old delay supplies a new delay strictly greater than half the old maximum; the maximum new delay is at least that large. Conversely, every new case is strictly smaller than its own old delay and therefore smaller than the old maximum; finitely many cases preserve that strict upper bound. The worst-case input pattern need not remain the same. Thus the maximum decreases but remains greater than half, option 2. The original NAND and fixed-load statement were rechecked against the source page.

**Reject each distractor using the model.** Option 1 suggests the ratio can cross below one half, impossible with nonnegative contributions. Option 3 also contradicts that lower bound. Option 4 would require the load contribution to vanish or scale with the driver, neither matching the stated loaded gate. Exactly half is a limiting case with zero internal contribution; unchanged delay is the zero-fixed-load limit. These boundaries explain why treating all capacitances as fixed, or all as scaled, loses a condition. This is an Elmore/scaling result under the stated abstractions, not a promise for input slew, wire effects or a manufactured gate.

## Q5

Correct option: 1.

**Substitute the requested valuation through the named nets.** At $x=0,y=1$, $t=\neg(xy)=1$, $u=\neg(xt)=1$, and $v=\neg(yt)=0$. Therefore $D=\neg(uv)=1$ and $B=\neg(vv)=1$. These computations use the same shared $t$ at both consumers; duplicating its value inconsistently would change the circuit.

**Identify the complete two-output function.** Algebraically,
$$D=xt+yt=\neg(xy)(x+y)=x\oplus y,\qquad B=yt=(\neg x)y.$$
In ordinary integer one-bit subtraction, $x-y=D-2B$. The requested row gives $0-1=1-2=-1$, exactly the borrow case of a half-subtractor. Option 1 has both the correct output pair and the correct interpretation.

**Alternatives.** Option 2 replaces borrow by half-adder carry. A half-adder at01 produces sum1 and carry0, but the actual second NAND output is1. Option 3 incorrectly makes the XOR output zero and calls it equality; equal inputs, not the current unequal inputs, would make XNOR one. Option 4 names the right circuit class but gives the wrong01 output pair, so the label alone does not make it correct. At11 the actual pair is00, while an adder would have carry1; that second row provides a useful cross-check beyond the requested valuation.

## Q6

Correct option: 1.

**Build the complements of the three POS factors.** Name
$$u=\neg(x+y),\quad v=\neg(x+z),\quad w=\neg(y+z).$$
Each is a two-input NOR. A three-input NOR then gives
$$F=\neg(u+v+w)=(x+y)(x+z)(y+z).$$
The POS is majority: with two or three ones, no input pair is00, so every sum is one; with at most one one, a pair of zeros makes one factor zero. Thus three two-input NOR gates followed by one three-input NOR directly implement it, option 1. No literal complement is needed for this particular POS, even though the statement allows complemented input sources.

**Check the other constructions.** One three-input NOR outputs one at000 and zero at111, the opposite behavior at both endpoints. “Three NANDs only” does not specify this required NOR-NOR mapping or provide its three complemented factors and final combination. Two two-input NORs have at most one previous gate available to the output and cannot implement the stated direct three-factor construction. This question asks which listed fan-in combination realizes the *given direct POS mapping*, not a universal minimum over every alternative network and free source resource. If only two-input cells were allowed, the final three-input NOR would require a polarity-correct decomposition; treating its three pins as a free binary gate would change the cost model.

## Q7

Correct option: 2.

**Trace the given event times before adding the output delay.** With $b=c=1$, the settled function $ab+(\neg a)c$ is one on both sides of the$a$ transition. The statement supplies the actual arrivals at the two OR inputs: the old asserted product falls at2 ns, and the new product rises at7 ns. Thus the Boolean OR-input result is zero on $[2,7)$ and one outside that interval.

An equal one-nanosecond transport delay translates each edge independently:
$$t_{\mathrm{fall}}=2+1=3\,\mathrm{ns},\qquad t_{\mathrm{rise}}=7+1=8\,\mathrm{ns}.$$
The output low interval is $[3,8)$ ns, option 2, and its width remains five nanoseconds. This is a possible static-one hazard, not a contradiction of the steady-state truth table.

**Alternatives and repair.** Option 1 gives the internal gap without translating it through the OR. Option 3 shifts the edges earlier, whereas the positive transport delay moves them later. Option 4 would require overlapping asserted paths, a stable bridging term, or a pulse-rejection model not supplied here. Adding consensus $bc$ gives an already settled one path during this specified stable-context transition, while preserving every settled output. A stated inertial rule could filter a pulse, but an ordinary propagation number alone does not establish such a rule.

## Q8

Correct option: 3.

**Add delays along a path and take the maximum across parallel paths.** The first incoming path has late arrival3 ns. The second has serial components2 and4 ns, so its arrival is $2+4=6$ ns. The final AND must accommodate the later relevant input and then its own one-nanosecond delay:
$$L(F)=\max(3,2+4)+1=6+1=7\,\mathrm{ns}.$$
Option 3 follows. The two incoming paths run concurrently; their complete delays must not be added as though the signal traversed both.

**Alternative diagnoses.** Four nanoseconds accounts only for the fast three-nanosecond path plus the final gate. Six gives the slow incoming arrival but omits the final AND. Ten adds all gate delays across both parallel paths, $3+2+4+1$, treating a branching graph as a serial chain. The critical incoming path is the2+4 branch, but that statement identifies a structural settling bound under the supplied model; it does not assert that every input pattern sensitizes a transition along that path.

**Transfer.** When primary inputs arrive at different times, add each arrival to its own path before comparing the paths. With pin-specific final delays, compare $L_1+p_1$ and $L_2+p_2$, rather than use a common delay that the problem did not provide. Earliest-disturbance analysis would use the lower bounds and a minimum recurrence, which is a separate question from this latest arrival.

## Q9

Correct option: 1.

**The second NAND has tied, not independent, inputs.** Let $A=\neg(xy)$. Because both pins of the output gate receive that same net, $F=\neg(AA)=\neg A=xy$ by AND idempotence and double complement. At10 the product is zero, hence the required pair is $xy$ and0, option 1.

**Inspect every candidate at more than a mnemonic level.** Option 2 describes OR, which is one on10; it disagrees with the circuit's output and truth function. Option 3 describes only the first gate's value and omits the output inversion. Option 4 gives XOR, also one on10, and differs from AND at01 as well. The complete AND output vector is0001 for rows00,01,10,11. No gates are duplicated by writing the same net on two pins; electrically, however, the output of the first gate drives two receiving pin capacitances.

**Cost boundary.** The drawing uses two NAND instances. One NAND with only$x,y$ available could compute only $\neg x$, $\neg y$ or $\neg(xy)$, and none is positive AND. Thus two gates are also a minimum under the no-free-complements/no-external-constants model, allowing tied inputs and fanout. A free positive AND cell or a different allowed library would invalidate that specific lower-bound argument.

## Q10

Correct option: 2.

**Form a dimensionless ratio with the same activity convention.** In $P=\alpha CV^2f$, use the same definition of$\alpha$ before and after the change. Capacitance is unchanged, activity scales by1/2, frequency by2, and voltage by0.8. Therefore
$$\frac{P'}P=\frac12\cdot1\cdot(0.8)^2\cdot2=0.64.$$
The activity and frequency factors cancel; voltage contributes its square rather than its first power. This gives option 2.

**Alternatives.** Option 1,0.32, squares the voltage correctly but forgets the doubled frequency. Option 3,0.8, uses linear voltage scaling. Option 4,1.28, includes doubled frequency and the squared voltage but forgets that activity halves. Identifying the missing factor is more useful than comparing the candidates numerically.

**Model limits and transfer.** The formula concerns the declared switching-power term. Leakage and short-circuit components are not assumed to obey this same scaling. If the activity factor counts zero-to-one events per clock interval, the capacitor energy supplied per such event is $CV^2$; using a convention that counts all edges requires a corresponding coefficient adjustment. A before/after ratio remains valid only when the convention is held fixed. Frequency is events per time, so changing it multiplies power, not the energy of a single charging event.

## Q11

Correct option: 2.

**Solve the first-order charging equation at the actual threshold.** Charging from zero toward$V$ through$R$ gives $v(t)=V(1-e^{-t/(RC)})$. At $v=3V/4$, divide by the nonzero supply and rearrange:
$$3/4=1-e^{-t/(RC)},\qquad e^{-t/(RC)}=1/4.$$
Taking natural logarithms gives $-t/(RC)=\ln(1/4)=-\ln4$, hence $t=RC\ln4$, option 2. Since $RC$ has time units and the logarithm's argument is dimensionless, the result has the correct units.

**Distractors.** $RC\ln2$ is the half-supply crossing, not the three-quarter crossing. $3RC/4$ assumes voltage rises linearly in time; substituting it into the actual exponential gives $V(1-e^{-3/4})$, approximately0.528V rather than0.75V. $4RC$ reaches approximately0.982V, overshooting the requested threshold. The approach slows as the capacitor voltage nears the supply.

**Generalization.** Reaching a fraction$r$ of the supply, with $0<r<1$, takes $-RC\ln(1-r)$. Discharging *to* that same fraction uses $-RC\ln r$, a different formula because the initial state and direction differ. The ideal charging time to exactly$V$ is unbounded; practical logic thresholds stay below the final asymptote.

## Q12

Correct option: 1.

**Use the correct guarantee/requirement difference at each level.** A high noise margin is the driver's guaranteed minimum high output minus the receiver's required minimum high input. A low noise margin is the receiver's accepted maximum low input minus the driver's maximum low output:
$$NM_H=4.2-3.0=1.2\,\mathrm{V},\qquad NM_L=0.9-0.3=0.6\,\mathrm{V}.$$
The low side is smaller, so option 1 is correct. A symmetric disturbance magnitude must fit both adverse directions; its guaranteed threshold budget is the minimum,0.6 V, under these static bounds.

**Alternatives.** Option 2 uses the low-input threshold itself, forgetting to subtract the nonzero low-output guarantee. Option 3 swaps the high and low differences and therefore misidentifies the limiting side. Option 4 adds4.2 and3.0 instead of subtracting two bounds on the same high-level voltage. At the low boundary, adding0.6 V to a worst-case0.3 V output reaches the0.9 V receiver limit; this is the physical interpretation of the computed margin.

**Transfer.** When the driver and receiver belong to different families, keep the driver's output guarantees and the receiver's input requirements in their respective positions. Positive static margins do not by themselves prove adequate output current, acceptable input capacitance, timing compatibility or analog transient integrity. A negative difference means that even the undisturbed connection is not guaranteed by the supplied specifications.

## Q13

Correct option: 3.

**Derive the actual construction or timed path.** Put $N=2^n$. A full binary reduction tree starts with$N$ separate input results. Each two-input gate combines two subresults into one, reducing the number of live components by exactly one. Reaching one output requires$N-1$ gates. Equivalently, count tree edges: if$G$ internal nodes each have two children, there are$2G$ edges, while a tree on$N+G$ vertices has$N+G-1$ edges; solving gives$G=N-1$.

**Exact requested calculation.**
$$2^5-1=32-1=31$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $5$, comes from $n$, which is balanced depth for this power-of-two leaf count, not gate count. Option 2, $4$, comes from $n-1$, which mistakenly subtracts one from the logarithmic depth instead of from the leaf count. Option 3, $31$, is the derived result. Option 4, $32$, comes from $2^n$, which counts the leaves rather than the internal combining gates.

**Concrete example and boundary.** A balanced$N=8$ realization has layers4,2,1, totaling7 gates and depth3. A chain also has7 gates but depth7. The count follows binary branching and distinct leaves, not a particular balancing shape. At$N=1$ the output is the input wire and zero gates suffice.

## Q14

Correct option: 2.

**Derive the actual construction or timed path.** Put $N=2^n$. A full binary reduction tree starts with$N$ separate input results. Each two-input gate combines two subresults into one, reducing the number of live components by exactly one. Reaching one output requires$N-1$ gates. Equivalently, count tree edges: if$G$ internal nodes each have two children, there are$2G$ edges, while a tree on$N+G$ vertices has$N+G-1$ edges; solving gives$G=N-1$.

**Exact requested calculation.**
$$2^8-1=256-1=255$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $7$, comes from $n-1$, which mistakenly subtracts one from the logarithmic depth instead of from the leaf count. Option 2, $255$, is the derived result. Option 3, $256$, comes from $2^n$, which counts the leaves rather than the internal combining gates. Option 4, $8$, comes from $n$, which is balanced depth for this power-of-two leaf count, not gate count.

**Concrete example and boundary.** A balanced$N=8$ realization has layers4,2,1, totaling7 gates and depth3. A chain also has7 gates but depth7. The count follows binary branching and distinct leaves, not a particular balancing shape. At$N=1$ the output is the input wire and zero gates suffice.

## Q15

Correct option: 1.

**Derive the actual construction or timed path.** Put $N=2^n$. A full binary reduction tree starts with$N$ separate input results. Each two-input gate combines two subresults into one, reducing the number of live components by exactly one. Reaching one output requires$N-1$ gates. Equivalently, count tree edges: if$G$ internal nodes each have two children, there are$2G$ edges, while a tree on$N+G$ vertices has$N+G-1$ edges; solving gives$G=N-1$.

**General answer.** The result is $2^n-1$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $2^n-1$, is the derived result. Option 2, $2^n$, comes from $2^n$, which counts the leaves rather than the internal combining gates. Option 3, $n$, comes from $n$, which is balanced depth for this power-of-two leaf count, not gate count. Option 4, $n-1$, comes from $n-1$, which mistakenly subtracts one from the logarithmic depth instead of from the leaf count.

**Concrete example and boundary.** A balanced$N=8$ realization has layers4,2,1, totaling7 gates and depth3. A chain also has7 gates but depth7. The count follows binary branching and distinct leaves, not a particular balancing shape. At$N=1$ the output is the input wire and zero gates suffice.

## Q16

Correct option: 4.

**Check the modeling condition.** Option 1 is false: balancing a full binary tree preserves its$N-1$ internal nodes. Option 2 confuses seven gates with three levels in the eight-input example. Option 3 changes the allowed library: one unbounded-fan-in AND could replace the whole tree, but that is not a binary-input construction. Option 4 correctly separates gate count from critical-path depth. No sharing or absorption of distinct input requirements is allowed in this stipulated tree.

**Derive the construction or timing result.** Put $N=2^n$. A full binary reduction tree starts with$N$ separate input results. Each two-input gate combines two subresults into one, reducing the number of live components by exactly one. Reaching one output requires$N-1$ gates. Equivalently, count tree edges: if$G$ internal nodes each have two children, there are$2G$ edges, while a tree on$N+G$ vertices has$N+G-1$ edges; solving gives$G=N-1$.

**Concrete check.** A balanced$N=8$ realization has layers4,2,1, totaling7 gates and depth3. A chain also has7 gates but depth7. The count follows binary branching and distinct leaves, not a particular balancing shape. At$N=1$ the output is the input wire and zero gates suffice.

## Q17

Correct option: 2.

**Derive the actual construction or timed path.** Each output product$xy$ is formed by a NAND giving$\neg(xy)$ and a tied-input NAND restoring the polarity. Thus each independent two-input AND construction has exactly two instances. With$n$ separate outputs and no sharing between them, sum the instance counts to obtain$2n$. Counting an inner net twice in a symbolic expression does not duplicate its gate.

**Exact requested calculation.**
$$2\cdot5=10$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $6$, comes from $n+1$, which assumes one output inverter can restore several distinct product nets independently. Option 2, $10$, is the derived result. Option 3, $5$, comes from $n$, which keeps only the first complemented product and misses every output-polarity restoration. Option 4, $15$, comes from $3n$, which adds an unnecessary third gate to each two-gate construction.

**Concrete example and boundary.** For two products, name$t_1=\neg(a_1b_1)$,$F_1=\neg(t_1t_1)$ and$t_2=\neg(a_2b_2)$,$F_2=\neg(t_2t_2)$. Four gates give both positive products. Each path has two stages. Each$t_i$ drives two pins of its restoration gate, so load count is not identical to gate-instance count.

## Q18

Correct option: 1.

**Derive the actual construction or timed path.** Each output product$xy$ is formed by a NAND giving$\neg(xy)$ and a tied-input NAND restoring the polarity. Thus each independent two-input AND construction has exactly two instances. With$n$ separate outputs and no sharing between them, sum the instance counts to obtain$2n$. Counting an inner net twice in a symbolic expression does not duplicate its gate.

**Exact requested calculation.**
$$2\cdot8=16$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $16$, is the derived result. Option 2, $8$, comes from $n$, which keeps only the first complemented product and misses every output-polarity restoration. Option 3, $24$, comes from $3n$, which adds an unnecessary third gate to each two-gate construction. Option 4, $9$, comes from $n+1$, which assumes one output inverter can restore several distinct product nets independently.

**Concrete example and boundary.** For two products, name$t_1=\neg(a_1b_1)$,$F_1=\neg(t_1t_1)$ and$t_2=\neg(a_2b_2)$,$F_2=\neg(t_2t_2)$. Four gates give both positive products. Each path has two stages. Each$t_i$ drives two pins of its restoration gate, so load count is not identical to gate-instance count.

## Q19

Correct option: 4.

**Derive the actual construction or timed path.** Each output product$xy$ is formed by a NAND giving$\neg(xy)$ and a tied-input NAND restoring the polarity. Thus each independent two-input AND construction has exactly two instances. With$n$ separate outputs and no sharing between them, sum the instance counts to obtain$2n$. Counting an inner net twice in a symbolic expression does not duplicate its gate.

**General answer.** The result is $2n$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $n$, comes from $n$, which keeps only the first complemented product and misses every output-polarity restoration. Option 2, $3n$, comes from $3n$, which adds an unnecessary third gate to each two-gate construction. Option 3, $n+1$, comes from $n+1$, which assumes one output inverter can restore several distinct product nets independently. Option 4, $2n$, is the derived result.

**Concrete example and boundary.** For two products, name$t_1=\neg(a_1b_1)$,$F_1=\neg(t_1t_1)$ and$t_2=\neg(a_2b_2)$,$F_2=\neg(t_2t_2)$. Four gates give both positive products. Each path has two stages. Each$t_i$ drives two pins of its restoration gate, so load count is not identical to gate-instance count.

## Q20

Correct option: 3.

**Check the modeling condition.** Option 1 contradicts$\neg(tt)=\neg t$. Option 2 violates the independent-output/no-sharing construction contract; one wire cannot carry two different product values at the same time. Option 3 is true: changing available complemented signals or the required output polarity can change the mapping. Option 4 mistakes NAND for positive AND, contradicted at11. The stated count is a construction count under explicit resources, not a minimum claim for every conceivable library.

**Derive the construction or timing result.** Each output product$xy$ is formed by a NAND giving$\neg(xy)$ and a tied-input NAND restoring the polarity. Thus each independent two-input AND construction has exactly two instances. With$n$ separate outputs and no sharing between them, sum the instance counts to obtain$2n$. Counting an inner net twice in a symbolic expression does not duplicate its gate.

**Concrete check.** For two products, name$t_1=\neg(a_1b_1)$,$F_1=\neg(t_1t_1)$ and$t_2=\neg(a_2b_2)$,$F_2=\neg(t_2t_2)$. Four gates give both positive products. Each path has two stages. Each$t_i$ drives two pins of its restoration gate, so load count is not identical to gate-instance count.

## Q21

Correct option: 2.

**Derive the actual construction or timed path.** Combining$n+1$ independent inputs serially requires$n$ binary XOR operations: the first joins two inputs, and each further operation incorporates one new input. Every stipulated XOR unit has four NAND instances, with its own shared internal net but no sharing with other XOR units. The total is therefore$4n$ NAND gates.

**Exact requested calculation.**
$$4\cdot5=20$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $10$, comes from $2n$, which charges only two NANDs per XOR and omits necessary internal operations. Option 2, $20$, is the derived result. Option 3, $5$, comes from $n$, which counts abstract XOR units rather than their four-NAND implementations. Option 4, $15$, comes from $3n$, which misses one of the four gates in each specified XOR realization.

**Concrete example and boundary.** For three inputs, first compute$x_1\oplus x_2$ with four NANDs and combine that result with$x_3$ using four more. The total is eight. Within each unit the auxiliary NAND result feeds two middle NANDs; it is one shared gate, not two. Replacing XOR by a primitive one-cell XOR changes the pricing model rather than disproves the substituted count.

## Q22

Correct option: 1.

**Derive the actual construction or timed path.** Combining$n+1$ independent inputs serially requires$n$ binary XOR operations: the first joins two inputs, and each further operation incorporates one new input. Every stipulated XOR unit has four NAND instances, with its own shared internal net but no sharing with other XOR units. The total is therefore$4n$ NAND gates.

**Exact requested calculation.**
$$4\cdot8=32$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $32$, is the derived result. Option 2, $8$, comes from $n$, which counts abstract XOR units rather than their four-NAND implementations. Option 3, $24$, comes from $3n$, which misses one of the four gates in each specified XOR realization. Option 4, $16$, comes from $2n$, which charges only two NANDs per XOR and omits necessary internal operations.

**Concrete example and boundary.** For three inputs, first compute$x_1\oplus x_2$ with four NANDs and combine that result with$x_3$ using four more. The total is eight. Within each unit the auxiliary NAND result feeds two middle NANDs; it is one shared gate, not two. Replacing XOR by a primitive one-cell XOR changes the pricing model rather than disproves the substituted count.

## Q23

Correct option: 4.

**Derive the actual construction or timed path.** Combining$n+1$ independent inputs serially requires$n$ binary XOR operations: the first joins two inputs, and each further operation incorporates one new input. Every stipulated XOR unit has four NAND instances, with its own shared internal net but no sharing with other XOR units. The total is therefore$4n$ NAND gates.

**General answer.** The result is $4n$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $n$, comes from $n$, which counts abstract XOR units rather than their four-NAND implementations. Option 2, $3n$, comes from $3n$, which misses one of the four gates in each specified XOR realization. Option 3, $2n$, comes from $2n$, which charges only two NANDs per XOR and omits necessary internal operations. Option 4, $4n$, is the derived result.

**Concrete example and boundary.** For three inputs, first compute$x_1\oplus x_2$ with four NANDs and combine that result with$x_3$ using four more. The total is eight. Within each unit the auxiliary NAND result feeds two middle NANDs; it is one shared gate, not two. Replacing XOR by a primitive one-cell XOR changes the pricing model rather than disproves the substituted count.

## Q24

Correct option: 3.

**Check the modeling condition.** Option 1 changes the stipulated primitive cost. Option 2 ignores the explicit no-sharing condition; a different optimized network requires its own derivation. Option 3 is correct: a balanced tree over the same leaves still has$n$ binary XOR nodes, so substitution still uses$4n$ NANDs, while the dependency depth can fall from linear to logarithmic. Option 4 ignores the increasing number of dependent units in a serial chain. Gate-count invariance under balancing does not prove identical load or detailed NAND path delay.

**Derive the construction or timing result.** Combining$n+1$ independent inputs serially requires$n$ binary XOR operations: the first joins two inputs, and each further operation incorporates one new input. Every stipulated XOR unit has four NAND instances, with its own shared internal net but no sharing with other XOR units. The total is therefore$4n$ NAND gates.

**Concrete check.** For three inputs, first compute$x_1\oplus x_2$ with four NANDs and combine that result with$x_3$ using four more. The total is eight. Within each unit the auxiliary NAND result feeds two middle NANDs; it is one shared gate, not two. Replacing XOR by a primitive one-cell XOR changes the pricing model rather than disproves the substituted count.

## Q25

Correct option: 4.

**Derive the actual construction or timed path.** With$N=2^n$ independent leaves, each two-to-one selector is one binary internal tree node. A full tree has$N-1$ such nodes, obtained either from the binary edge count or the level sum$2^{n-1}+\cdots+2+1=2^n-1$. The$n$ address bits choose a path; they are control signals, not$n$ mux instances.

**Exact requested calculation.**
$$2^5-1=31$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $32$, comes from $2^n$, which counts data leaves rather than mux instances. Option 2, $5$, comes from $n$, which counts select bits or balanced levels instead of nodes. Option 3, $30$, comes from $2^n-2$, which omits the final selector that combines the last two subtree outputs. Option 4, $31$, is the derived result.

**Concrete example and boundary.** An eight-to-one balanced tree uses four muxes at its leaf level, two next and one final: seven muxes. Three address bits suffice. Label the first level with its least-significant selection decision and the later levels consistently with the input numbering, or explicitly declare another address convention. The same block count can implement a permuted data selection if the pin labels change.

## Q26

Correct option: 3.

**Derive the actual construction or timed path.** With$N=2^n$ independent leaves, each two-to-one selector is one binary internal tree node. A full tree has$N-1$ such nodes, obtained either from the binary edge count or the level sum$2^{n-1}+\cdots+2+1=2^n-1$. The$n$ address bits choose a path; they are control signals, not$n$ mux instances.

**Exact requested calculation.**
$$2^8-1=255$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $8$, comes from $n$, which counts select bits or balanced levels instead of nodes. Option 2, $254$, comes from $2^n-2$, which omits the final selector that combines the last two subtree outputs. Option 3, $255$, is the derived result. Option 4, $256$, comes from $2^n$, which counts data leaves rather than mux instances.

**Concrete example and boundary.** An eight-to-one balanced tree uses four muxes at its leaf level, two next and one final: seven muxes. Three address bits suffice. Label the first level with its least-significant selection decision and the later levels consistently with the input numbering, or explicitly declare another address convention. The same block count can implement a permuted data selection if the pin labels change.

## Q27

Correct option: 2.

**Derive the actual construction or timed path.** With$N=2^n$ independent leaves, each two-to-one selector is one binary internal tree node. A full tree has$N-1$ such nodes, obtained either from the binary edge count or the level sum$2^{n-1}+\cdots+2+1=2^n-1$. The$n$ address bits choose a path; they are control signals, not$n$ mux instances.

**General answer.** The result is $2^n-1$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $2^n-2$, comes from $2^n-2$, which omits the final selector that combines the last two subtree outputs. Option 2, $2^n-1$, is the derived result. Option 3, $2^n$, comes from $2^n$, which counts data leaves rather than mux instances. Option 4, $n$, comes from $n$, which counts select bits or balanced levels instead of nodes.

**Concrete example and boundary.** An eight-to-one balanced tree uses four muxes at its leaf level, two next and one final: seven muxes. Three address bits suffice. Label the first level with its least-significant selection decision and the later levels consistently with the input numbering, or explicitly declare another address convention. The same block count can implement a permuted data selection if the pin labels change.

## Q28

Correct option: 1.

**Check the modeling condition.** Option 1 is correct because swapping$I_0/I_1$ on a mux reverses that select decision while preserving the number of blocks. Option 2 ignores this change in the selected data. Option 3 confuses$n$ control bits with$2^n-1$ selectors. Option 4 removes half the independent address choices unless the data or specification is additionally constrained. At$n=0$, one data input can connect directly with zero muxes, but the bank's numerical parameter domain is positive.

**Derive the construction or timing result.** With$N=2^n$ independent leaves, each two-to-one selector is one binary internal tree node. A full tree has$N-1$ such nodes, obtained either from the binary edge count or the level sum$2^{n-1}+\cdots+2+1=2^n-1$. The$n$ address bits choose a path; they are control signals, not$n$ mux instances.

**Concrete check.** An eight-to-one balanced tree uses four muxes at its leaf level, two next and one final: seven muxes. Three address bits suffice. Label the first level with its least-significant selection decision and the later levels consistently with the input numbering, or explicitly declare another address convention. The same block count can implement a permuted data selection if the pin labels change.

## Q29

Correct option: 3.

**Derive the actual construction or timed path.** The carry entering the last, bit$n-1$, sum output traverses$n-1$ carry stages. Its arrival is$2(n-1)$. The sum then takes three more units, giving$2(n-1)+3=2n+1$. The final carry traverses$n$ stages and arrives after$2n$ units. Compare both candidate outputs: the last sum is one unit later, so the overall maximum is$2n+1$.

**Exact requested calculation.**
$$\max(2(5-1)+3,2\cdot5)=11$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $8$, comes from $n+3$, which charges one unit rather than two for each preceding carry stage and additionally miscounts its endpoints. Option 2, $6$, comes from $n+1$, which uses the wrong per-stage delay and omits the final three-unit sum contract. Option 3, $11$, is the derived result. Option 4, $10$, comes from $2n$, which counts only the final carry path and omits the slower sum.

**Concrete example and boundary.** For three bits, the carry arrivals are$c_1=2$,$c_2=4$,$c_3=6$. The last sum follows$c_2$ at$4+3=7$, later than final carry6. At one bit there are no preceding carry stages; the sum takes3 and carry2. This boundary confirms$2n+1$ without inventing a negative stage count.

## Q30

Correct option: 2.

**Derive the actual construction or timed path.** The carry entering the last, bit$n-1$, sum output traverses$n-1$ carry stages. Its arrival is$2(n-1)$. The sum then takes three more units, giving$2(n-1)+3=2n+1$. The final carry traverses$n$ stages and arrives after$2n$ units. Compare both candidate outputs: the last sum is one unit later, so the overall maximum is$2n+1$.

**Exact requested calculation.**
$$\max(2(8-1)+3,2\cdot8)=17$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $9$, comes from $n+1$, which uses the wrong per-stage delay and omits the final three-unit sum contract. Option 2, $17$, is the derived result. Option 3, $16$, comes from $2n$, which counts only the final carry path and omits the slower sum. Option 4, $11$, comes from $n+3$, which charges one unit rather than two for each preceding carry stage and additionally miscounts its endpoints.

**Concrete example and boundary.** For three bits, the carry arrivals are$c_1=2$,$c_2=4$,$c_3=6$. The last sum follows$c_2$ at$4+3=7$, later than final carry6. At one bit there are no preceding carry stages; the sum takes3 and carry2. This boundary confirms$2n+1$ without inventing a negative stage count.

## Q31

Correct option: 1.

**Derive the actual construction or timed path.** The carry entering the last, bit$n-1$, sum output traverses$n-1$ carry stages. Its arrival is$2(n-1)$. The sum then takes three more units, giving$2(n-1)+3=2n+1$. The final carry traverses$n$ stages and arrives after$2n$ units. Compare both candidate outputs: the last sum is one unit later, so the overall maximum is$2n+1$.

**General answer.** The result is $2n+1$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $2n+1$, is the derived result. Option 2, $2n$, comes from $2n$, which counts only the final carry path and omits the slower sum. Option 3, $n+3$, comes from $n+3$, which charges one unit rather than two for each preceding carry stage and additionally miscounts its endpoints. Option 4, $n+1$, comes from $n+1$, which uses the wrong per-stage delay and omits the final three-unit sum contract.

**Concrete example and boundary.** For three bits, the carry arrivals are$c_1=2$,$c_2=4$,$c_3=6$. The last sum follows$c_2$ at$4+3=7$, later than final carry6. At one bit there are no preceding carry stages; the sum takes3 and carry2. This boundary confirms$2n+1$ without inventing a negative stage count.

## Q32

Correct option: 4.

**Check the modeling condition.** Option 1 is false under the supplied delays: the final sum exceeds final carry by one. Option 2 adds parallel paths instead of taking their maximum. Option 3 discards the actual delay contract; changing the carry/sum costs changes which output is critical. Option 4 states the correct procedure: compare every candidate output path. This is a specified abstract path model, not a general physical timing result for all ripple-adder implementations.

**Derive the construction or timing result.** The carry entering the last, bit$n-1$, sum output traverses$n-1$ carry stages. Its arrival is$2(n-1)$. The sum then takes three more units, giving$2(n-1)+3=2n+1$. The final carry traverses$n$ stages and arrives after$2n$ units. Compare both candidate outputs: the last sum is one unit later, so the overall maximum is$2n+1$.

**Concrete check.** For three bits, the carry arrivals are$c_1=2$,$c_2=4$,$c_3=6$. The last sum follows$c_2$ at$4+3=7$, later than final carry6. At one bit there are no preceding carry stages; the sum takes3 and carry2. This boundary confirms$2n+1$ without inventing a negative stage count.

## Q33

Correct option: 4.

**Derive the actual construction or timed path.** The initial internal term is one unit and the initial external-load term another. Scaling widths by$n$ divides resistance by$n$ and multiplies internal capacitance by$n$. Their product remains one. The externally fixed capacitance does not scale, so its contribution becomes$1/n$. The new total is therefore$1+1/n$, not$2/n$.

**Exact requested calculation.**
$$1+1/5=6/5$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $\frac{2}{5}$, comes from $2/n$, which incorrectly treats the width-dependent internal capacitance as fixed. Option 2, $2$, comes from $2$, which incorrectly scales the externally fixed load with the driver as well. Option 3, $1$, comes from $1$, which drops the positive fixed-load term at a finite width scale. Option 4, $\frac{6}{5}$, is the derived result.

**Concrete example and boundary.** At$n=2$, the initial delay2 becomes$1+1/2=1.5$, a ratio3/4. At$n=1$ there is no change and the expression returns2. As$n$ grows, the internal term approaches the nonzero limit1 while the fixed-load term tends to zero. This is a delay in the stated time units; dividing it by the old2 would instead produce the new/old ratio.

## Q34

Correct option: 3.

**Derive the actual construction or timed path.** The initial internal term is one unit and the initial external-load term another. Scaling widths by$n$ divides resistance by$n$ and multiplies internal capacitance by$n$. Their product remains one. The externally fixed capacitance does not scale, so its contribution becomes$1/n$. The new total is therefore$1+1/n$, not$2/n$.

**Exact requested calculation.**
$$1+1/8=9/8$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $2$, comes from $2$, which incorrectly scales the externally fixed load with the driver as well. Option 2, $1$, comes from $1$, which drops the positive fixed-load term at a finite width scale. Option 3, $\frac{9}{8}$, is the derived result. Option 4, $\frac{1}{4}$, comes from $2/n$, which incorrectly treats the width-dependent internal capacitance as fixed.

**Concrete example and boundary.** At$n=2$, the initial delay2 becomes$1+1/2=1.5$, a ratio3/4. At$n=1$ there is no change and the expression returns2. As$n$ grows, the internal term approaches the nonzero limit1 while the fixed-load term tends to zero. This is a delay in the stated time units; dividing it by the old2 would instead produce the new/old ratio.

## Q35

Correct option: 2.

**Derive the actual construction or timed path.** The initial internal term is one unit and the initial external-load term another. Scaling widths by$n$ divides resistance by$n$ and multiplies internal capacitance by$n$. Their product remains one. The externally fixed capacitance does not scale, so its contribution becomes$1/n$. The new total is therefore$1+1/n$, not$2/n$.

**General answer.** The result is $1+1/n$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $1$, comes from $1$, which drops the positive fixed-load term at a finite width scale. Option 2, $1+1/n$, is the derived result. Option 3, $2/n$, comes from $2/n$, which incorrectly treats the width-dependent internal capacitance as fixed. Option 4, $2$, comes from $2$, which incorrectly scales the externally fixed load with the driver as well.

**Concrete example and boundary.** At$n=2$, the initial delay2 becomes$1+1/2=1.5$, a ratio3/4. At$n=1$ there is no change and the expression returns2. As$n$ grows, the internal term approaches the nonzero limit1 while the fixed-load term tends to zero. This is a delay in the stated time units; dividing it by the old2 would instead produce the new/old ratio.

## Q36

Correct option: 1.

**Check the modeling condition.** Option 1 is true: the internal$RC$ product sets a nonzero floor in this model. Option 2 ignores that retained product. Option 3 contradicts the explicit fixed-load assumption. Option 4 contradicts the stated internal-capacitance scaling. Input slew, unscaled interconnect and device nonlinearities can require a more detailed model; they must not be silently inserted into or omitted from the exercise's specified contract.

**Derive the construction or timing result.** The initial internal term is one unit and the initial external-load term another. Scaling widths by$n$ divides resistance by$n$ and multiplies internal capacitance by$n$. Their product remains one. The externally fixed capacitance does not scale, so its contribution becomes$1/n$. The new total is therefore$1+1/n$, not$2/n$.

**Concrete check.** At$n=2$, the initial delay2 becomes$1+1/2=1.5$, a ratio3/4. At$n=1$ there is no change and the expression returns2. As$n$ grows, the internal term approaches the nonzero limit1 while the fixed-load term tends to zero. This is a delay in the stated time units; dividing it by the old2 would instead produce the new/old ratio.

## Q37

Correct option: 4.

**Derive the actual construction or timed path.** Each stage has delay2 ns and$n$ is odd. One traversal reverses the observed node after$2n$ ns; a second traversal restores the original level. The modeled full period is$T=4n$ ns. Convert its reciprocal to megahertz: $f_{\mathrm{MHz}}=1000/(4n)=250/n$. A period and its reciprocal have different scaling directions.

**Exact requested calculation.**
$$1000/(4\cdot5)=250/5$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $100$, comes from $500/n$, which uses the half-period rather than the full cycle. Option 2, $200$, comes from $1000/n$, which counts only one nanosecond per stage and one traversal instead of the supplied two and two. Option 3, $1250$, comes from $250n$, which multiplies by stage count even though increasing loop delay reduces frequency. Option 4, $50$, is the derived result.

**Concrete example and boundary.** For five inverters, one traversal takes10 ns and the full period20 ns, giving50 MHz. For seven, the full period28 ns gives$1000/28=250/7$ MHz. Both rising and falling transitions must be included. The formula describes an established ordinary ring regime with the supplied equal transition delays, not guaranteed startup or every possible feedback network.

## Q38

Correct option: 3.

**Derive the actual construction or timed path.** Each stage has delay2 ns and$n$ is odd. One traversal reverses the observed node after$2n$ ns; a second traversal restores the original level. The modeled full period is$T=4n$ ns. Convert its reciprocal to megahertz: $f_{\mathrm{MHz}}=1000/(4n)=250/n$. A period and its reciprocal have different scaling directions.

**Exact requested calculation.**
$$1000/(4\cdot7)=250/7$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $\frac{1000}{7}$, comes from $1000/n$, which counts only one nanosecond per stage and one traversal instead of the supplied two and two. Option 2, $1750$, comes from $250n$, which multiplies by stage count even though increasing loop delay reduces frequency. Option 3, $\frac{250}{7}$, is the derived result. Option 4, $\frac{500}{7}$, comes from $500/n$, which uses the half-period rather than the full cycle.

**Concrete example and boundary.** For five inverters, one traversal takes10 ns and the full period20 ns, giving50 MHz. For seven, the full period28 ns gives$1000/28=250/7$ MHz. Both rising and falling transitions must be included. The formula describes an established ordinary ring regime with the supplied equal transition delays, not guaranteed startup or every possible feedback network.

## Q39

Correct option: 2.

**Derive the actual construction or timed path.** Each stage has delay2 ns and$n$ is odd. One traversal reverses the observed node after$2n$ ns; a second traversal restores the original level. The modeled full period is$T=4n$ ns. Convert its reciprocal to megahertz: $f_{\mathrm{MHz}}=1000/(4n)=250/n$. A period and its reciprocal have different scaling directions.

**General answer.** The result is $250/n$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $250n$, comes from $250n$, which multiplies by stage count even though increasing loop delay reduces frequency. Option 2, $250/n$, is the derived result. Option 3, $500/n$, comes from $500/n$, which uses the half-period rather than the full cycle. Option 4, $1000/n$, comes from $1000/n$, which counts only one nanosecond per stage and one traversal instead of the supplied two and two.

**Concrete example and boundary.** For five inverters, one traversal takes10 ns and the full period20 ns, giving50 MHz. For seven, the full period28 ns gives$1000/28=250/7$ MHz. Both rising and falling transitions must be included. The formula describes an established ordinary ring regime with the supplied equal transition delays, not guaranteed startup or every possible feedback network.

## Q40

Correct option: 1.

**Check the modeling condition.** Option 1 correctly states the odd-inversion assumption for this ordinary ring model. Option 2 treats an even-inversion loop as having the same oscillation mechanism; it can instead have consistent stable binary states. Option 3 confuses an opposite-level return with a complete cycle. Option 4 violates$f=1/T$: increasing a positive period decreases frequency. The formula is not a physical certification of oscillation for arbitrary gate models or initial conditions.

**Derive the construction or timing result.** Each stage has delay2 ns and$n$ is odd. One traversal reverses the observed node after$2n$ ns; a second traversal restores the original level. The modeled full period is$T=4n$ ns. Convert its reciprocal to megahertz: $f_{\mathrm{MHz}}=1000/(4n)=250/n$. A period and its reciprocal have different scaling directions.

**Concrete check.** For five inverters, one traversal takes10 ns and the full period20 ns, giving50 MHz. For seven, the full period28 ns gives$1000/28=250/7$ MHz. Both rising and falling transitions must be included. The formula describes an established ordinary ring regime with the supplied equal transition delays, not guaranteed startup or every possible feedback network.

## Q41

Correct option: 4.

**Derive the actual construction or timed path.** Each stipulated output has$ab+(\neg a)c+bc$. The first and second products each contain two literal occurrences, and the consensus bridge has two more. Thus a completed SOP contains six occurrences. Summing across$n$ independent, separately counted outputs yields$6n$. A complemented literal is one occurrence, not an extra algebraic variable or a second occurrence.

**Exact requested calculation.**
$$6\cdot5=30$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $20$, comes from $4n$, which counts only the original two products and leaves out every bridge. Option 2, $10$, comes from $2n$, which counts only the added literals, not the completed SOPs. Option 3, $15$, comes from $3n$, which counts product terms rather than their two literals each. Option 4, $30$, is the derived result.

**Concrete example and boundary.** For one output the bridge adds two occurrences to the original four. Its functional redundancy follows$bc=abc+(\neg a)bc$, covered by the original two products. With$b=c=1$ the bridge is independent of changing$a$ and remains asserted, explaining its timing purpose. Literal occurrence count is not a count of gates, inverters or physical transistor controls.

## Q42

Correct option: 3.

**Derive the actual construction or timed path.** Each stipulated output has$ab+(\neg a)c+bc$. The first and second products each contain two literal occurrences, and the consensus bridge has two more. Thus a completed SOP contains six occurrences. Summing across$n$ independent, separately counted outputs yields$6n$. A complemented literal is one occurrence, not an extra algebraic variable or a second occurrence.

**Exact requested calculation.**
$$6\cdot8=48$$
Retain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.

**Diagnose each alternative.** Option 1, $16$, comes from $2n$, which counts only the added literals, not the completed SOPs. Option 2, $24$, comes from $3n$, which counts product terms rather than their two literals each. Option 3, $48$, is the derived result. Option 4, $32$, comes from $4n$, which counts only the original two products and leaves out every bridge.

**Concrete example and boundary.** For one output the bridge adds two occurrences to the original four. Its functional redundancy follows$bc=abc+(\neg a)bc$, covered by the original two products. With$b=c=1$ the bridge is independent of changing$a$ and remains asserted, explaining its timing purpose. Literal occurrence count is not a count of gates, inverters or physical transistor controls.

## Q43

Correct option: 2.

**Derive the actual construction or timed path.** Each stipulated output has$ab+(\neg a)c+bc$. The first and second products each contain two literal occurrences, and the consensus bridge has two more. Thus a completed SOP contains six occurrences. Summing across$n$ independent, separately counted outputs yields$6n$. A complemented literal is one occurrence, not an extra algebraic variable or a second occurrence.

**General answer.** The result is $6n$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.

**Diagnose each alternative.** Option 1, $3n$, comes from $3n$, which counts product terms rather than their two literals each. Option 2, $6n$, is the derived result. Option 3, $4n$, comes from $4n$, which counts only the original two products and leaves out every bridge. Option 4, $2n$, comes from $2n$, which counts only the added literals, not the completed SOPs.

**Concrete example and boundary.** For one output the bridge adds two occurrences to the original four. Its functional redundancy follows$bc=abc+(\neg a)bc$, covered by the original two products. With$b=c=1$ the bridge is independent of changing$a$ and remains asserted, explaining its timing purpose. Literal occurrence count is not a count of gates, inverters or physical transistor controls.

## Q44

Correct option: 1.

**Check the modeling condition.** Option 1 is correct: a truth-table-redundant term can protect a specified transition in a delay-aware implementation. Option 2 confuses settled function with waveform behavior. Option 3 contradicts the consensus identity. Option 4 ignores which variable hands responsibility between paths. The protection requires the stable side inputs and appropriate two-level/single-input model; it is not a cure for every multi-input or multilevel hazard.

**Derive the construction or timing result.** Each stipulated output has$ab+(\neg a)c+bc$. The first and second products each contain two literal occurrences, and the consensus bridge has two more. Thus a completed SOP contains six occurrences. Summing across$n$ independent, separately counted outputs yields$6n$. A complemented literal is one occurrence, not an extra algebraic variable or a second occurrence.

**Concrete check.** For one output the bridge adds two occurrences to the original four. Its functional redundancy follows$bc=abc+(\neg a)bc$, covered by the original two products. With$b=c=1$ the bridge is independent of changing$a$ and remains asserted, explaining its timing purpose. Literal occurrence count is not a count of gates, inverters or physical transistor controls.

## Q45

Correct option: 3.

**Translate both gap edges through the same transport delay.** The stable side inputs give $F=a+\neg a=1$. During the stated falling$a$ transition, the old$ab$ product drops at2 ns and the new$(\neg a)c$ product rises at5 ns. Their OR-input result is zero on $[2,5)$, a three-nanosecond gap. Equal one-nanosecond output transport delay gives a falling output at3 ns and a rising output at6 ns.
$$w=(5+1)-(2+1)=3\,\mathrm{ns}.$$
Option 3 is correct. The equal delay translates the interval without changing its width. One nanosecond is the gate's transport delay, not the pulse width; two and four have no support in the supplied event times. Subtracting the delay from only one edge would invent asymmetric timing and incorrectly change the width.

**Transfer and repair.** The same interval mechanism appears in Question 7, with different input-event times and a different select edge. Always identify the old falling product and new rising product from the specified transition rather than swapping them by visual habit. A stable consensus$bc$ term holds the output high without changing the truth function under the appropriate settled-side-input SOP model. An inertial model with an explicit rejection rule could give another waveform; a one-nanosecond propagation number alone does not imply that rule.

## Q46

Correct option: 2.

**Compute the adverse disturbance budget on each level.** The driver guarantees low no greater than0.2 V, while the receiver accepts low through0.7 V, giving
$$NM_L=0.7-0.2=0.5\,\mathrm{V}.$$
For a high level, subtract the receiver's2.0 V requirement from the driver's2.4 V minimum guarantee:
$$NM_H=2.4-2.0=0.4\,\mathrm{V}.$$
The smaller margin is0.4 V, option 2. It bounds a symmetric static adverse disturbance that must fit both sides; the high side is the bottleneck.

**Options.**0.2 V is the maximum low output level itself, not a gap between a guarantee and requirement.0.5 V is the valid low margin but ignores the smaller high margin.0.7 V is the low-input threshold itself. Checking the limiting high case directly, subtracting0.4 V from a worst-case2.4 V high reaches the2.0 V acceptance boundary; this explains what the answer measures.

**Boundary.** If a voltage margin were negative, the undisturbed connection would not be guaranteed by the supplied bounds. A positive margin does not certify output-current capability, loading, pulse response or timing. These are receiving/driver static specifications, not probabilities of an error or claims about arbitrary noise waveforms.
