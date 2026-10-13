## Ten solved circuit and timing synthesis challenges

These independently authored problems combine the chapter's mechanisms. Every construction states its resources, and every time-dependent result states its event model. The solutions are teaching material, not a pre-study assessment.

### Challenge 1. Prove a minimum for a three-input NAND

**Task.** Only two-input NANDs, uncomplemented independent inputs$x,y,z$, tied inputs and fanout are available; no constants are supplied. Prove the minimum number of gates for$\neg(xyz)$ and provide a matching netlist.

**Solution.** Three gates suffice: $t=\neg(xy)$, $u=\neg(tt)=xy$, $F=\neg(uz)=\neg(xyz)$. The longest$x/y$ path has three gate stages. A one-gate output cannot depend essentially on all three inputs. For two gates, if the output gate does not use the first gate's result, it likewise has at most two primary inputs. If it does use that result, consider the all-one primary input. The first NAND necessarily gives zero; NANDing it with any available primary signal or with itself gives one. The desired three-input NAND is zero there. These cases exhaust a two-gate acyclic network with one prior result. Therefore no network with fewer than three gates works, and the construction is minimal in the declared model.

This argument does not transfer to a library that includes a three-input NAND or free complemented sources. Three standard two-input static-CMOS NAND cells have twelve transistors in the stipulated four-device-per-cell topology; that separate transistor count does not change the gate-count proof.

### Challenge 2. An Elmore chain with internal and fixed capacitance

**Task.** A driver-to-output RC chain has$R_1=2$ kΩ and$R_2=1$ kΩ. A5 fF internal capacitor is after$R_1$; after$R_2$ are a4 fF internal capacitor and6 fF fixed external load. Find the original Elmore moment and the moment after doubling driver widths under the chapter's scaling model.

**Solution.** The first capacitor shares only$R_1$ with the output path; the later two share$R_1+R_2$. Thus
$$D=2000\cdot5\cdot10^{-15}+3000\cdot(4+6)\cdot10^{-15}=40\,\mathrm{ps}.$$
Internal contributions are$2000\cdot5+3000\cdot4=22000$ in Ω·fF, or22 ps. The fixed load contributes18 ps. Scaling gives$D'=22+18/2=31$ ps. A direct recomputation checks it: new resistances are1000 and500 Ω, internal capacitances10 and8 fF, and fixed load remains6 fF. Therefore
$$D'=1000\cdot10\cdot10^{-15}+1500\cdot(8+6)\cdot10^{-15}=31\,\mathrm{ps}.$$
The ratio31/40 lies between one half and one. Multiplying a guessed total3 kΩ by total15 fF would give45 ps, not the correct40: the upstream5 fF capacitor does not load$R_2$.

### Challenge 3. The worst switching case can change after sizing

**Task.** Two allowed switching cases have modeled delays$D_1(s)=0.5+4/s$ and$D_2(s)=3+1/s$, for positive width scale$s$. Determine the worst case at$s=1$ and2, their crossing, and the smallest$s\ge1$ meeting worst-case delay3.2.

**Solution.** At1, the two delays are4.5 and4, so case1 is worse. At2, they are2.5 and3.5, so case2 is worse. Equating gives$3/s=2.5$, hence$s=1.2$. The maximum is$D_1$ below that scale and$D_2$ above it. Each case decreases, but their identity can change; propagating only the originally worst case would understate the new maximum.

Both must satisfy the target. Case1 requires$s\ge4/(3.2-0.5)=40/27$. Case2 requires$s\ge1/(3.2-3)=5$. Their simultaneous requirement is$s\ge5$; at5 the delays are1.3 and3.2. The worst-case ratio after doubling is$3.5/4.5=7/9$, still strictly between one half and one. The example uses abstract positive RC contributions, not measured parameters of a particular NAND.

### Challenge 4. Late and early arrival through two reconvergent paths

**Task.** Inputs$x,y$ have early/late arrivals$(0,3)$ and$(2,5)$ ns. Gate$u=\operatorname{NAND}(x,y)$ has lower/upper bounds1 and4 ns. Gate$v=\operatorname{NOT}(x)$ has bounds2 and6 ns. A final NOR of$u,v$ has bounds0.5 and2 ns. Find structural output bounds and explain what they do not assert.

**Solution.** For$u$, earliest possible disturbance is$\min(0,2)+1=1$ ns and latest validity is$\max(3,5)+4=9$ ns. For$v$, the corresponding values are$0+2=2$ and$3+6=9$ ns. Therefore
$$E_F=\min(1,2)+0.5=1.5\,\mathrm{ns},\qquad L_F=\max(9,9)+2=11\,\mathrm{ns}.$$
The two paths share$x$, so exact sensitization can impose correlated conditions not captured by these structural recurrences. The bounds are conservative under the supplied pin contracts; they do not promise a transition at1.5 ns, settling exactly at11 ns, or one clean edge in between. No timing rule for a feedback loop is being inferred from this finite DAG calculation.

### Challenge 5. Two threshold directions use different logarithms

**Task.** A load with$RC=20$ ns charges from zero toward$V$ or discharges from$V$ toward zero. Find the time to0.75V in each direction, then the time to a valid low at0.2V during discharge.

**Solution.** Charging uses$20\ln4$, approximately27.73 ns. Discharging to0.75V uses$-20\ln(0.75)=20\ln(4/3)$, approximately5.75 ns. Discharging to0.2V uses$20\ln5$, approximately32.19 ns. The same numerical threshold is reached quickly early in discharge but late during charging because their initial conditions differ.

Substituting20 ns into a generic “RC delay” rule would answer none of these exact crossing requests. Nor is a calculated voltage crossing automatically a worst-case characterized gate guarantee: the resistor/capacitor model must first apply to the circuit and its operating condition. All logarithm arguments are dimensionless; the20 ns time constant carries the unit.

### Challenge 6. Positive voter output under two different gate libraries

**Task.** Implement a four-input at-least-three voter with a positive output. Price one construction using arbitrary-fan-in NANDs and another using arbitrary-fan-in NORs, and explain the change when only binary cells exist.

**Solution.** The SOP$abc+abd+acd+bcd$ has four triple products. Four three-input NANDs form their complements; a four-input NAND ORs the positive products by De Morgan. This is five gates, with sixteen total input pins: twelve in the first layer and four in the last.

The POS is the product of the six pair sums$(a+b),(a+c),(a+d),(b+c),(b+d),(c+d)$. Each factor is one exactly when its pair is not00; all factors being one means at most one input is zero, which is at least three ones. Six binary NORs and a six-input NOR use seven gates and eighteen input pins. These are direct construction counts, not universal minima. A binary-only library lacks both large final gates and the NAND triple cells. Decomposing their underlying AND/OR operations with proper polarity recovery increases gate counts and levels. Reusing the original five/seven counts would silently change the library.

### Challenge 7. An XNOR tree's name does not determine parity

**Task.** Compare a binary XNOR tree over five independent inputs with the complement of their XOR. Use a four-NAND XOR implementation and an extra NAND inverter to price two explicit constructions for even parity.

**Solution.** A binary XNOR is$1\oplus a\oplus b$. A five-leaf tree has four internal gates, adding four ones to the XOR of its leaves. Those constants cancel, so the tree is odd parity, independent of its shape. At all-zero leaves it gives zero, whereas even parity must give one.

Building the five-input XOR uses four XOR modules at four NANDs each: sixteen NANDs. A final tied-input NAND inverts it, giving a seventeen-gate even-parity construction. Alternatively, replacing each abstract XNOR unit by a four-NAND XOR and one inverter uses five NANDs per unit. Four such units produce odd parity and consume twenty NANDs; one final inverter corrects them, giving twenty-one. These different construction counts do not prove a global minimum. They expose why substituting a name without deriving the constant contribution can waste gates and return the wrong function.

### Challenge 8. A ring with unequal directional delays

**Task.** Three inverters have output-rise delays2,3,4 ns and output-fall delays5,6,7 ns, in that order. Find the modeled period and frequency in an established ordinary ring regime.

**Solution.** A rising event at the observed input of stage1 makes its output fall after5 ns, stage2 rise after3 more, and stage3 fall after7 more. This opposite-level return takes15 ns. The returning fall makes stage1 rise after2 ns, stage2 fall after6, and stage3 rise after4, adding12 ns. Hence$T=15+12=27$ ns and$f=1000/27$ MHz, approximately37.04 MHz.

Equivalently the full cycle includes every stage's rising and falling arc once, totaling$(2+5)+(3+6)+(4+7)=27$ ns. Twice one selected traversal would give either30 or24 ns and ignore the direction difference. The result requires the supplied established-regime event model; odd inversion alone is not a physical startup or amplitude proof.

### Challenge 9. Unequal output arcs can change a pulse width

**Task.** The Boolean OR-input result falls at2 ns and rises at5 ns. A stated transport model delays falling output edges by1 ns and rising output edges by2 ns. Find the output pulse. Compare with a separate inertial rule rejecting input-result pulses shorter than4 ns.

**Solution.** The transport fall occurs at3 ns and rise at7 ns, making output low on$[3,7)$ with width4 ns. Its input-result pulse had width3 ns. Equal-delay translation preserves width, but unequal arcs add the difference$2-1=1$ ns. The scheduled edges have the correct temporal order here, so there is no ambiguous negative-width event case.

Under the separately specified inertial rule, the3 ns input-result pulse is shorter than4 ns and is rejected; the output stays high. Do not use the transport output width4 as the input pulse tested by that inertial contract. These models share a steady-state OR truth table but specify different waveform behavior. A propagation-delay bound alone is insufficient to choose between them.

### Challenge 10. Complementarity of a compound CMOS gate

**Task.** A three-device nMOS pulldown has series$x,y$ in parallel with$z$. A proposed pMOS pullup puts all three devices in parallel. Diagnose its failure, repair it, and count standard-topology devices for the inverting and positive functions.

**Solution.** The pulldown conducts when$D=xy+z$. All-parallel pMOS gives$U=\neg x+\neg y+\neg z$, which is not$\neg D$. At110, $D=1$ while the low$z$ turns on a pMOS, giving$U=1$ and a sustained supply-to-ground path in the ideal stable-state model. No valid Boolean output is guaranteed there.

The complementary pullup is parallel pMOS$x,y$ in series with pMOS$z$, producing$U=(\neg x+\neg y)\neg z=\neg(xy+z)$. For every stable input, exactly one of$D,U$ is one. The output is$F=\neg(xy+z)$, an AOI21 function. Three nMOS and three pMOS devices give six transistors in this topology. Appending a two-transistor inverter gives positive$xy+z$ with eight devices. This switch-level count excludes drive resizing, physical layout, internal capacitance and short-circuit/leakage details; it is not an area or power measurement.
