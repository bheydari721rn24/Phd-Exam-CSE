## Teaching through formulas and conceptual decisions

### Separate Boolean equivalence from circuit cost

A NAND-only realization derives NOT as NAND of a signal with itself, AND as NAND followed by inversion, and OR by De Morgan using inverted inputs. Tying two inputs together is one two-input gate under this library convention; it is not free unless the cost model says so. A NAND implementation of XOR uses four shared gates; realizing separate expanded SOP terms without sharing can cost more.

For a two-level SOP, map product terms into first-level NANDs and combine their inverted outputs with a final NAND. A two-level POS maps dually into NORs. Gate fan-in constraints can add intermediate gates. Inverting gates are not associative: a cascade of NAND gates generally does not implement a larger NAND without a polarity correction.

### Derive timing from actual sensitized paths

Latest stable arrival through a gate is bounded by its maximum input arrival plus propagation delay. Earliest possible output contamination uses the earliest relevant input change plus contamination delay, with controlling-value and sensitization conditions checked. A topological timing calculation is not a proof that every longest graph path is sensitizable.

For$F=ab\lor\neg a c$ with$b=c=1$, a transition in$a$ exchanges the two product terms. Unequal path delays can temporarily make both zero even though the steady-state output is1. The consensus term$bc$ keeps a continuous1 coverage under the standard single-input, two-level static-hazard assumptions. This guarantee does not cover arbitrary simultaneous input changes or every multilevel dynamic hazard.

### Physical formulas require their activity convention

In the elementary RC model, charging a load$C$ through resistance$R$ toward a step voltage reaches fraction$1-e^{-t/(RC)}$. Reaching half the final value takes$RC\ln2$. Charging from an ideal supply uses$CV^2$ energy, half stored in the capacitor and half dissipated in the resistor. Average dynamic supply power is$\alpha CV^2f$ when$\alpha$ counts zero-to-one charging events per clock cycle; a different activity definition changes the prefactor.

## Formula and conceptual problem bank

### Question 1. NAND truth condition

When is a three-input NAND output zero?

**A.** Whenever any input is zero.

**B.** Only when all three inputs are one.

**C.** Whenever an odd number of inputs are one.

**D.** Only when all inputs are zero.

**Answer: B.**

NAND negates the AND of all its inputs. The underlying AND equals1 only on111, so the NAND is0 only there. A zero input is a controlling input for AND and forces the NAND output to1. The odd-parity rule describes a different gate.

### Question 2. NAND-only OR

Two-input NAND gates are allowed and inputs may be tied. How many gates does the direct De Morgan construction of$a\lor b$ use?

**A.** 1

**B.** 2

**C.** 3

**D.** 4

**Answer: C.**

Invert$a$ with NAND$(a,a)$ and invert$b$ with NAND$(b,b)$. A third NAND of these inverted signals yields$\neg(\neg a\land\neg b)=a\lor b$. This counts the stated construction, not a minimum over an enriched library with free input complements. Omitting an inverter changes one literal polarity.

### Question 3. A NAND cascade error

Let$u=\neg(ab)$ and$y=\neg(uc)$. Which expression is$y$?

**A.** $\neg(abc)$

**B.** $ab\lor\neg c$

**C.** $ab\lor c$

**D.** $a\oplus b\oplus c$

**Answer: B.**

Apply De Morgan to the final NAND: $y=\neg u\lor\neg c=ab\lor\neg c$. Setting$c=0$ makes the output1, and setting$c=1$ yields$ab$. A simple cascade therefore does not implement a three-input NAND; a missing polarity-restoring inversion explains the difference.

### Question 4. XOR shared NAND network

The standard shared implementation computes$t=\operatorname{NAND}(a,b)$,$u=\operatorname{NAND}(a,t)$,$v=\operatorname{NAND}(b,t)$,$y=\operatorname{NAND}(u,v)$. What is$y$?

**A.** $a\land b$

**B.** $a\lor b$

**C.** $a\oplus b$

**D.** $\neg(a\oplus b)$

**Answer: C.**

For00, the intermediate values are$t=u=v=1$, giving$y=0$. For01 or10, exactly one of$u,v$ is0, giving$y=1$. For11,$t=0$ and$u=v=1$, giving0. These four values identify XOR. The intermediate$t$ is shared, and duplicating its computation changes the gate count.

### Question 5. Functional completeness

With no external constants or complemented inputs, which two-input gate alone is functionally complete?

**A.** AND

**B.** OR

**C.** XOR

**D.** NOR

**Answer: D.**

NOR constructs NOT by tied inputs. It then constructs OR by following a NOR with inversion and AND through De Morgan with inverted inputs, giving a complete basis of AND, OR and NOT. AND and OR cannot express negation; XOR alone generates affine parity functions and cannot express arbitrary conjunction.

### Question 6. Static CMOS transistor count

In the ideal complementary static-CMOS model, how many transistors implement a three-input NAND without extra buffers?

**A.** 3

**B.** 4

**C.** 6

**D.** 8

**Answer: C.**

The pull-down network has three series nMOS devices, conducting only when every input is high. The dual pull-up network has three parallel pMOS devices, conducting when any input is low. Total count is six. The answer counts one complementary gate, not a cascade of two-input gates or a buffered cell.

### Question 7. Latest arrival calculation

A two-input gate has propagation delay3ns. Its input stable-arrival times are2ns and7ns. Using the conservative max-input timing rule, what is the latest output stable time?

**A.** 5ns

**B.** 7ns

**C.** 10ns

**D.** 12ns

**Answer: C.**

The output cannot be guaranteed stable until the last relevant input is stable and the gate’s propagation bound has elapsed. Compute$\max(2,7)+3=10$ns. Summing the two input arrival times counts parallel histories as serial work. Sensitization can tighten a particular case, but the stated conservative rule gives10.

### Question 8. Serial contamination delay

Two gates on a sensitized serial path have contamination delays1ns and2ns. What path lower bound follows for an output change after the initiating input change?

**A.** 1ns

**B.** 2ns

**C.** 3ns

**D.** 0ns

**Answer: C.**

An input change must traverse the first gate before it can initiate a change in the second. The two lower bounds add to3ns on the stated sensitized serial path. Parallel alternatives could give earlier changes, so the question restricts the path being analyzed. Contamination delay is an earliest-change lower bound, not a latest-stability guarantee.

### Question 9. A static-one hazard repair

For$F=ab\lor\neg a c$, what extra product term removes the classic single-$a$ static-one hazard in the two-level model?

**A.** $ac$

**B.** $\neg b\neg c$

**C.** $bc$

**D.** $a\neg a$

**Answer: C.**

The hazard case has$b=c=1$ while$a$ changes. The consensus term$bc$ stays1 throughout the transition and prevents a temporary output fall. It adds no new steady-state true rows because each such row was already covered by$ab$ or$\neg a c$. The other candidate terms do not provide constant coverage during both polarities of$a$.

### Question 10. RC half-voltage time

A first-order node charges with time constant$RC=10$ns. When does it reach half its final voltage?

**A.** 5ns

**B.** $10\ln2$ns

**C.** 10ns

**D.** 20ns

**Answer: B.**

Solve$1-e^{-t/(RC)}=1/2$. Then$e^{-t/(RC)}=1/2$, so$t=RC\ln2=10\ln2$ns, about6.93ns. Half voltage is not reached at half a time constant because the charging trajectory is exponential.

### Question 11. Dynamic power ratio

In$P=\alpha CV^2f$, voltage doubles and frequency halves while$\alpha,C$ stay fixed. What is the power ratio?

**A.** 1/2

**B.** 1

**C.** 2

**D.** 4

**Answer: C.**

Voltage contributes a factor$2^2=4$, and frequency contributes1/2. Their product is2. A linear voltage assumption would incorrectly predict no change. This compares dynamic charging power under a fixed activity convention; leakage and short-circuit power are not included by this elementary formula.

### Question 12. Stored versus supplied energy

An initially uncharged capacitor$C$ is charged to$V$ through a resistor from an ideal constant supply. What energy remains stored?

**A.** $CV^2$

**B.** $CV^2/2$

**C.** $2CV^2$

**D.** $CV/2$

**Answer: B.**

Stored energy is$\int_0^{CV}(q/C)\,dq=CV^2/2$. The supply delivers$V\int i\,dt=CV^2$; the other half is dissipated during ideal resistive charging. Confusing stored energy with supply energy introduces the factor-two error. The answer$CV/2$ has the wrong physical dimension for energy.

<!-- CHALLENGE-BANK -->

### Question 13. Challenge: A quantified static hazard window

$F=ab\lor\neg a c$ has$b=c=1$ and$a$ falls at0ns. The$ab$ output falls at2ns and$\neg a c$ rises at5ns. An OR with equal1ns transport delay follows them. What is its low-pulse width?

**A.** 1ns

**B.** 2ns

**C.** 3ns

**D.** 4ns

**Answer: C.**

The OR inputs are both zero from2ns to5ns, a three-nanosecond interval. Equal transport delay shifts the falling output event to3ns and the rising event to6ns without changing pulse width. A steady-state truth table predicts output1 before and after but misses the transient. An inertial model rejecting pulses shorter than4ns could suppress it, which is a different stated timing model.

### Question 14. Challenge: Noise-margin bottleneck

A driver guarantees$V_{OL}\le0.2$V and$V_{OH}\ge2.4$V. A receiver accepts lows through0.7V and highs from2.0V. What is the smaller guaranteed noise margin?

**A.** 0.2V

**B.** 0.4V

**C.** 0.5V

**D.** 0.7V

**Answer: B.**

Low margin is$0.7-0.2=0.5$V and high margin is$2.4-2.0=0.4$V. The smaller is0.4V. The driver output bounds and receiver thresholds have different roles; subtracting two driver levels would not give either noise margin. Both margins are positive, so the idealized voltage-level compatibility check passes.

## Applicable formulas and examination notes

### 1. Controlling inputs

For AND and NAND, any0 fixes the underlying AND to0; the NAND output is therefore1. For OR and NOR, any1 fixes the OR to1; the NOR output is0. Parity gates have no single controlling input in the same sense.

### 2. Mapping polarity

SOP naturally maps into NAND-NAND; POS into NOR-NOR. Write the inversion at each intermediate wire before counting gates. Complemented inputs are free only if the specified library provides them at no extra cost.

### 3. Inverting gates are not associative

$\operatorname{NAND}(\operatorname{NAND}(a,b),c)=ab\lor\neg c$. It is not a three-input NAND. Cascaded decompositions must restore the internal polarity where required.

### 4. Shared XOR cost

The standard four-NAND XOR reuses the first NAND output twice. Fanout is not an extra logical gate under this count, but buffering may add physical cost in a different model. Count unique instances, not repeated occurrences of a shared subexpression.

### 5. Completeness assumptions

NAND and NOR construct negation with tied inputs and form complete libraries. XOR alone generates affine functions. Constants, complemented external inputs and fan-in restrictions are part of the library and can change the completeness question.

### 6. Static CMOS dual networks

An$n$-input NAND uses$n$ series nMOS and$n$ parallel pMOS devices, total$2n$, in the ideal unbuffered model. NOR reverses series and parallel roles. Compound gates need the dual pull-up graph, not merely the same graph with device names changed.

### 7. Arrival recurrence

Conservative latest output arrival is$\max_i a_i+t_{pd}$. Serial path delays add; parallel input arrival times take a maximum. A longest graph path may be unsensitizable, so distinguish structural bounds from attainable transition timings.

### 8. Contamination versus propagation

Contamination bounds the earliest possible change; propagation bounds latest guaranteed stabilization. Summing contamination delays is a path-specific lower bound under a sensitized serial model. It does not guarantee the output has settled at that time.

### 9. Static hazard consensus

For$ab\lor\neg a c$, add$bc$ to maintain coverage while$a$ changes and$b=c=1$. This is a single-input static-one guarantee in a two-level model. It does not eliminate every functional hazard from multiple changing inputs.

### 10. RC threshold

At voltage fraction$q$, first-order charging takes$-RC\ln(1-q)$. Half voltage takes$RC\ln2$. A specified threshold and model are needed before using an RC delay as a gate timing number.

### 11. Activity convention

$P=\alpha CV^2f$ assumes$\alpha$ counts charging events per cycle. Doubling voltage and halving frequency doubles this power. If activity counts every edge instead, a factor-of-two convention change may be necessary.

### 12. Energy distinction

Charging from0 to$V$ supplies$CV^2$, stores$CV^2/2$ and dissipates$CV^2/2$ in the simple resistive model. During discharge the stored half is dissipated. A full charging/discharging cycle therefore uses the full supply-energy expression.

<!-- BOUNDARY-NOTES -->

### 13. Active-low interface

A bubble labels inversion or an active-low signal convention; trace which interpretation is used at each pin. Two matched inversions can cancel logically, while an unmatched bubble changes the function. Signal name and asserted voltage level are separate data.

### 14. Noise margin arithmetic

Low noise margin is $V_{IL}-V_{OL}$ and high noise margin is $V_{OH}-V_{IH}$ under the stated guaranteed voltage bounds. Positive margins are needed for compatible logic levels. Propagation delay does not measure a noise margin.

### 15. Load versus logical fanout

A shared wire may avoid duplicate gates but increases input capacitance. In an elementary RC model the delay grows with load. A minimum gate-count design need not minimize physical delay or energy.

### 16. Rise, fall and inertial filtering

A transition may use a rise-specific or fall-specific delay depending on each gate's inversion. Transport models propagate every pulse; inertial models can suppress pulses shorter than their specified rejection interval. Truth-table equivalence does not decide which waveform model applies.
