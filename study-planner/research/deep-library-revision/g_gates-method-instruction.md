## Exact construction, electrical and timing methods

The complete gate lesson and all thirty-six worked tutorials are retained. These constructions provide the additional mathematics used by the revised examination bank. A gate's truth function, the cost of its implementation, the voltage validity contract and its time-dependent output are separate descriptions. Every conclusion below names the description and assumptions it uses.

### 1. Gate count, depth and independent input information

Let a full binary tree combine $N$ independent leaves into one result. If it has $G$ internal two-input nodes, count its edges in two ways. Each internal node has two children, giving $2G$ edges. The connected acyclic tree has $N+G$ vertices and therefore $N+G-1$ edges. Thus
$$2G=N+G-1,\qquad G=N-1.$$
This proof is independent of balancing. A chain has depth $N-1$, while a balanced tree has depth $\lceil\log_2N\rceil$. For $N=2^n$, the balanced level counts are $2^{n-1},2^{n-2},\ldots,1$, totaling $2^n-1$ gates at depth $n$. At $N=1$, the input wire itself is the result and there are zero gates.

The depth lower bound also has a proof: an output at binary depth $d$ can depend on at most $2^d$ independent leaves, by induction over its two predecessor subtrees. Depending essentially on all $N$ leaves therefore requires $d\ge\lceil\log_2N\rceil$. This is a structural information bound under two-input composition, not a claim about every fan-in library. An unbounded-input primitive would change the assumption.

For a full mux tree, the same internal-node count applies, but the function additionally depends on select labeling. A tree of seven muxes can select any of eight inputs using three address bits; swapping data pins changes which address selects which input without changing the count. A circuit-count argument cannot verify that address map by itself.

### 2. Expand cost at the actual primitive-library level

A binary XOR unit can use four NANDs: $t=\neg(xy)$, $u=\neg(xt)$, $v=\neg(yt)$, $F=\neg(uv)$. The shared internal$t$ is one instance. Substitution gives
$$F=xt+yt=(x+y)\neg(xy)=x\neg y+(\neg x)y.$$
A chain combining $n+1$ independent inputs has$n$ XOR units. With the stipulated no-sharing four-NAND realization at every unit, the count is$4n$. A balanced XOR tree retains the same number of abstract units and the same substituted instance count, while reducing dependency depth. Individual NAND paths inside a unit can have different numbers of stages, so a detailed physical delay needs their arcs rather than only an abstract XOR count.

Positive AND uses two NANDs: generate$t=\neg(xy)$ and restore$F=\neg(tt)=xy$. Under the model with only primary$x,y$ available, no constants or complemented inputs, zero gates can only forward a primary wire; one NAND can produce only$\neg x$, $\neg y$ or$\neg(xy)$. None is$xy$, proving the two-gate construction minimal under that exact model. Presenting a network normally proves only an upper bound; this enumeration supplies the missing lower bound.

Complemented input availability, tied-input permission, reusable internal nets and required output polarity belong to a cost statement. A free complement source can change a mapping but has an arrival/load contract of its own. Multiple output expressions may share a real product gate, yet its increased receiving capacitance may worsen delay. Count physical instances, connected pins, logic depth and transistor assumptions independently.

### 3. Elmore delay and uniform width scaling

For an RC tree rooted at its driver, the Elmore first moment at output$o$ can be written
$$D_o=\sum_j C_jR_{\mathrm{shared}}(o,j).$$
Here $R_{\mathrm{shared}}(o,j)$ is the sum of resistances common to the source-to-output and source-to-capacitor$j$ paths. It accounts for a capacitor loading every upstream shared resistance, rather than multiplying an arbitrary total resistance by an arbitrary total capacitance. For a simple two-resistor chain, with$C_1$ after$R_1$ and$C_2$ after$R_2$,
$$D_2=R_1C_1+(R_1+R_2)C_2=R_1(C_1+C_2)+R_2C_2.$$
Every term is nonnegative for passive positive components. The quantity is a model moment; converting it to a particular voltage-crossing delay can require an approximation and must use a consistent convention.

In the examination's fixed-topology scaling model, multiplying driver widths by$s>0$ divides the relevant on-resistances by$s$. Width-dependent internal capacitances multiply by$s$, but an externally specified fixed load does not. Group original contributions as$D_I$ and$D_L$:
$$D(s)=D_I+D_L/s.$$
Internal products are unchanged because $(R/s)(sC)=RC$; fixed-load products reduce because $(R/s)C_L=RC_L/s$. With positive internal and fixed-load contributions and$s>1$,
$$\frac1s<\frac{D(s)}{D(1)}<1.$$
For doubled widths, the ratio lies strictly between one half and one. Algebraically, $D(2)-(D_I+D_L)/2=D_I/2>0$, while $D(1)-D(2)=D_L/2>0$.

The limits expose the hypotheses. With zero internal contribution, exactly$1/s$ is possible. With no fixed load, scaling leaves this model's delay unchanged. If the receiving gates also scale, their load capacitance is no longer fixed. If interconnect resistance remains unscaled, its terms need separate classification. If changed device widths also alter the incoming waveform, that requires an input-slew model. None of these effects should be silently substituted for the exercise's stated model.

For a maximum over several switching cases, write $D_{\max}(s)=\max_j(D_{I,j}+D_{L,j}/s)$. Do not silently assume that the maximizing input case remains the same after scaling. Nevertheless the same strict ratio bounds hold when every allowed case has positive internal and fixed-load contributions: the old maximizing case proves the lower bound, and each of finitely many new cases is smaller than the old maximum, proving the upper bound. An explicit worst-case-changing example is solved in the transfer challenges.

This also supplies a constrained sizing calculation. To meet delay target$D_T>D_I$, require $s\ge D_L/(D_T-D_I)$. A target at or below$D_I$ is unattainable by finite width scaling in this model. For$D_I=1$, $D_L=1$, target1.25 requires$s\ge4$. Width increase buys diminishing load-delay improvement while preserving a nonzero internal floor.

### 4. Solve a voltage crossing before naming a delay

For a capacitor charging from zero through resistance$R$ toward supply$V$, Kirchhoff's law gives $C\,dv/dt=(V-v)/R$. Rearrange using$u=V-v$: $du/dt=-u/(RC)$ with$u(0)=V$. The solution is
$$v(t)=V(1-e^{-t/(RC)}).$$
At a specified fraction$0<r<1$, set$v=rV$ and solve:
$$t_r=-RC\ln(1-r).$$
At$r=1/2$ this is$RC\ln2$; at$r=3/4$ it is$RC\ln4$. Discharge from$V$ instead has$v(t)=Ve^{-t/(RC)}$ and crossing time$-RC\ln r$. The same symbol$r$ therefore produces different charging and discharging expressions unless the threshold is the symmetric half-supply value.

A source that informally uses$RC$ as an estimated stage delay is not supplying an exact half-supply crossing of this differential equation. Stanford's simplified loading estimates and MIT's valid-level upper/lower contracts also refer to different timing descriptions. Keep a numerical RC estimate, midpoint delay, latest valid-output guarantee and earliest invalid-output guarantee explicitly distinct. The interval between the last two need not contain one clean digital edge.

Static noise margins compare a driver with its receiver:
$$NM_L=V_{IL,\mathrm{receiver}}-V_{OL,\mathrm{driver}},\qquad NM_H=V_{OH,\mathrm{driver}}-V_{IH,\mathrm{receiver}}.$$
A common adverse disturbance magnitude must fit both, so use their minimum. A negative margin means that the static level connection is not guaranteed even with no extra noise. Adequate voltage gaps do not establish current-drive, capacitive-load or timing compatibility.

### 5. Propagate arrival bounds through the actual dependency graph

For a gate with pin-specific late bounds$p_i$, its output late bound is $L_o=\max_i(L_i+p_i)$. The corresponding conservative earliest-disturbance bound uses $E_o=\min_i(E_i+c_i)$ for the pin-specific lower bounds$c_i$. With one common gate delay, these reduce to maximum or minimum input arrival plus that delay. Topological evaluation applies them to each node of a finite acyclic graph.

For incoming paths3 ns and$2+4=6$ ns followed by a common1 ns AND, the late result is$\max(3,6)+1=7$ ns. Adding3+2+4+1 treats the two parallel branches as one serial signal path. For a ripple carry chain with carry-stage delay2 and final sum delay3, compare the final carry path$2n$ with the last sum path$2(n-1)+3$; the sum is one unit later.

Output edge direction matters at an inverter: a rising input causes a falling output, so use that cell's output-fall arc. A second inverter reverses the direction again. Side inputs may block a structural path: an AND with a stable controlling zero has no settled-output change from its other input. A longest structural path is a conservative budget and not a promise that every input transition exhibits it. A guaranteed stable controlling input suppressing transient effects additionally requires the appropriate lenient gate contract.

### 6. Derive an exact hazard waveform from named events

For $F=ab+(\neg a)c$ with$b=c=1$, either endpoint value of$a$ gives one. During a specified transition, let the old asserted product fall at$t_f$ and the new product rise at$t_r$. If$t_r>t_f$, the OR-input result is zero on$[t_f,t_r)$. Under equal transport delay$d$ at the OR,
$$t_{Y\downarrow}=t_f+d,\quad t_{Y\uparrow}=t_r+d,\quad w=t_r-t_f.$$
The pulse moves but keeps its width. If the new product rises before the old product falls, the asserted paths overlap and there is no low gap. Equal-time events are processed as one batch; a zero-width event ordering artifact is not a real positive-width pulse.

With distinct falling and rising output delays$d_f,d_r$, candidate edges occur at$t_f+d_f$ and$t_r+d_r$. Whether they constitute a valid ordered output pulse additionally depends on the precise event/pulse rule. One must not assume equal-width translation after changing the timing model. An inertial rejection rule can eliminate short pulses, but a quoted propagation delay by itself supplies no such rule.

Adding$bc$ preserves the settled function because $bc=abc+(\neg a)bc$ is covered by the original terms. For this stable context, the bridge remains one during the handoff. The dual POS bridge protects a static-zero transition. This is a two-level, one-changing-input argument with already settled side inputs; it does not eliminate dynamic hazards in arbitrary remapped circuits or the function-required response of XOR to a skewed00-to11 input change.

### 7. A ring period includes both polarities of a returning edge

An ordinary odd-inverter ring in an established symmetric-delay regime returns the opposite value to a chosen node after one traversal. If$n$ stages each take$\tau$, the half-period is$n\tau$ and the full period is$2n\tau$. Therefore
$$f=1/(2n\tau).$$
When$\tau$ is in nanoseconds, $f_{\mathrm{MHz}}=1000/(2n\tau_{\mathrm{ns}})$. Five stages at5 ns yield$T=50$ ns and$f=20$ MHz. Five stages at2 ns yield$T=20$ ns and$f=50$ MHz. Mixing the two source instances' delay values would change the question.

If output-rise and output-fall delays differ, both traversals contribute their appropriate arcs. In a three-inverter ring with rise delays2,3,4 ns and fall delays5,6,7 ns, one observed rising-to-falling return can use5+3+7=15 ns, while its opposite uses2+6+4=12 ns; the full modeled period is27 ns. The reciprocal is approximately37.04 MHz. The odd-inversion and established-regime assumptions explain this event model; they do not certify startup, analog amplitude or fabricated-device performance.

**Written sources used here.** The freshly reread MIT, Cambridge, Stanford and Berkeley scopes are recorded in the course recheck; the historical UCSD restricted-library scope is distinguished from failed fresh DNS requests. Elmore scaling, threshold crossings, path maxima/minima and exact event-time calculations are independently derived. The recorded Stanford table multiplication error is corrected instead of propagated. Source references and the limits of each model remain explicit.
