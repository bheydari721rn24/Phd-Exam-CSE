## Twenty further circuit decisions with derivations

These decisions complement the retained sixty-rule summary and sixteen examination notes. Each identifies a mathematical object, a valid calculation and the condition that changes the answer.

### 17. Preserve the polarity of each named wire

A NAND output is the complement of its entire input product. For $t=\neg(xy)$, the next NAND with inputs $t,z$ gives $\neg(tz)=xy+\neg z$, not $\neg(xyz)$. To build the latter with binary NANDs, restore $u=\neg(tt)=xy$ before computing $\neg(uz)$. Explicit net names prevent silently treating inverting gates as associative.

### 18. A tied input saves a source, not a gate instance

The two pins of $\operatorname{NAND}(t,t)$ receive one shared signal, but there is still one NAND cell. It produces $\neg t$. Thus a positive two-input AND constructed from a NAND followed by this inverter uses two cells, not one or three. Counts of cells, pins, distinct wires and transistor devices answer different questions.

### 19. A primitive must essentially depend on each requested input

One binary cell cannot realize a genuinely three-input function. A lower-bound argument must also exclude the remaining smaller networks. For a three-input NAND with no supplied constants, every two-cell attempt using the first NAND output produces one at the all-one assignment, whereas the required result is zero. Three cells attain the target, so this is a proved minimum in that precise library. Merely exhibiting three gates would only establish an upper bound.

### 20. Independent modules do not inherit shared-subexpression savings

For $n$ separate positive AND outputs using two NANDs each, the stipulated construction costs $2n$. For a chain with $n$ XOR operations using four NANDs per operation, it costs $4n$. Do not multiply the number of input bits $n+1$ by the module price: the number of binary combining operations is one less than the number of leaves. A different shared implementation requires a new netlist and a new count.

### 21. The binary-tree equation counts total internal vertices

With $L$ leaves and $G$ internal binary vertices, the tree has $2G$ incoming edges and $L+G-1$ edges in total. Hence $G=L-1$. If $L=2^n$, a balanced tree has depth $n$ but $2^n-1$ cells. A skew tree retains the cell count while increasing depth. Shared directed graphs and arbitrary-fan-in cells are outside this tree proof.

### 22. Multiplexer count is not address width

A full selector for $2^n$ independent values uses $2^n-1$ binary multiplexers and $n$ address bits in its regular balanced organization. Each bit controls a layer of many cells. Swapping a cell's zero and one data pins changes the selected function even when the total count is identical. Read the data pin labels before substituting Shannon's expression.

### 23. An XNOR tree contributes one constant per internal vertex

Since $\operatorname{XNOR}(a,b)=1\oplus a\oplus b$, a binary tree on $L$ leaves gives the XOR of those leaves, further XORed with $(L-1)\bmod2$. For five leaves it is odd parity; for four leaves it is even parity. The binary XNOR cell name alone does not identify the parity of a larger composition.

### 24. Price both literal polarities in SOP/POS mapping

In NAND-NAND SOP mapping, each first-layer complement is intentional because the final NAND restores the OR of products. In NOR-NOR POS mapping, the first layer complements each sum and the final NOR forms their product. If a required complemented primary input is unavailable, its generator adds cells and possibly another stage. Do not call those complements free unless the resource statement does.

### 25. Complementary CMOS requires complementary conduction predicates

For a pulldown with $D=xy+z$, the correct pullup predicate is $U=(\neg x+\neg y)\neg z$. Verify $D+U=1$ on every stable input. Replacing all nMOS devices by pMOS without dualizing the series/parallel graph gives the wrong predicate and can permit both networks to conduct. The Boolean proof concerns stable ideal switches; leakage and transient current remain physical effects.

### 26. Elmore weighting follows shared paths

For a two-resistor chain with capacitances $C_1$ at the intermediate node and $C_2$ at the output, the output moment is $R_1(C_1+C_2)+R_2C_2$. Only $C_2$ shares $R_2$ with the observation path. Multiplying total resistance by total capacitance incorrectly charges the intermediate capacitor through a resistor outside its path. Establish topology before arithmetic.

### 27. Width scaling preserves a modeled internal contribution

Under $R\mapsto R/s$, internal $C\mapsto sC$ and fixed external load, each case has $D(s)=I+L/s$. Internal resistance-capacitance products cancel the scale; external-load products shrink. For $s>1$ and positive $I,L$, $D(1)/s<D(s)<D(1)$. Zero contributions turn some strict inequalities into equalities. This result uses the stated linear scaling approximation, not an unrestricted device law.

### 28. Recompute the maximum after changing widths

Different switching cases can have different $I_j,L_j$. The correct result is $\max_j(I_j+L_j/s)$, which need not be achieved by the old maximizer. With $D_1=0.5+4/s$ and $D_2=3+1/s$, case one is slower at scale one and case two at scale two. To meet a target, impose the inequality on every allowed case, rather than sizing against one originally worst pattern.

### 29. Compare final sum and final carry separately

If each carry step costs two units and the last sum costs three after its carry input, the last sum arrives at $2(n-1)+3=2n+1$. The final carry arrives at $2n$. The last sum therefore dominates by one unit in this declared model. The sum uses the penultimate carry, not the final carry; appending three to $2n$ double-counts a carry stage.

### 30. A reconvergence takes a maximum, not a sum of branches

For branches with delays $3$ and $2+4$, followed by a one-unit final gate, the structural late bound is $\max(3,6)+1=7$. Adding both branches gives ten and incorrectly treats parallel work as serial. A sensitization argument is still necessary if the problem asks whether this structural bound is attained by a particular transition.

### 31. Early change and latest settling are different promises

For independent pin contracts, a conservative earliest disturbance uses a minimum plus contamination delay; latest validity uses a maximum plus propagation delay. Neither implies exactly one transition between those limits. Correlated reconvergent signals can eliminate a structural early transition or a particular late path; report that boundary when deriving bounds.

### 32. Derive an RC logarithm from the correct initial condition

Charging from zero gives $v/V=1-e^{-t/(RC)}$ and crossing fraction $q$ at $-RC\ln(1-q)$. Discharging from $V$ gives $v/V=e^{-t/(RC)}$ and crossing at $-RC\ln q$. At $q=3/4$, the answers are $RC\ln4$ and $RC\ln(4/3)$ respectively. The threshold fraction is dimensionless and strictly between zero and one for a finite positive crossing time.

### 33. Compute power ratios factor by factor

For a fixed convention $P=\alpha CV^2f$, the ratio is the product of activity ratio, capacitance ratio, squared voltage ratio and frequency ratio. Activity one half, fixed capacitance, voltage $0.8$ and frequency two yield $0.5\cdot1\cdot0.64\cdot2=0.64$. Squaring the frequency or forgetting to square voltage changes the model. Supply energy per charging event and stored capacitor energy differ by a factor of two.

### 34. Use the receiver's bound on the appropriate side

$NM_L=V_{IL}-V_{OL}$ compares the receiver's highest accepted low with the driver's worst high low-output voltage. $NM_H=V_{OH}-V_{IH}$ compares the driver's lowest guaranteed high with the receiver's minimum accepted high. For $4.2,3.0,0.9,0.3$ volts in that order, they are $1.2$ and $0.6$ volts, limited by the low side. A negative margin identifies incompatibility under those guarantees, not a negative delay.

### 35. Translate edges before subtracting pulse times

If a Boolean OR-input result is low from time two to five and both output arcs delay one, the output is low from three to six and has width three. If the rise arc instead delays two, its output rise is at seven and the width becomes four. An independently specified inertial rule may reject the original input-result pulse. A steady-state truth table or delay upper bound alone does not specify that filtering behavior.

### 36. One trip around an odd ring changes level

In an established equal-delay $n$-inverter ring with odd $n$, one trip takes $n\tau$ and returns the opposite edge. The next trip completes the full cycle, so $T=2n\tau$ and $f=1/T$. With five stages of five nanoseconds, $T=50$ ns and $f=20$ MHz. With unequal rise/fall delays, a full cycle contains every stage's rise and fall arc once. These are declared steady-regime delay-model results, not guarantees of physical startup or valid voltage amplitude.
