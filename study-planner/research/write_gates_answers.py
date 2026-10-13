from pathlib import Path
from fractions import Fraction
import re
from read_gates_bank import rows
E=Path(__file__).parent/'deep-library-revision';A={}
def put(i,s):A[i]=f"Correct option: {rows[i-1]['answer']}.\n\n"+s.strip()
parts=re.split(r'^## Q(\d+)\s*$',(E/'g_boolean-solutions.md').read_text(),flags=re.M);boolean={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
for i,j in[(1,6),(2,7)]:put(i,re.sub(r'^Correct option:\s*\d+\.\s*','',boolean[j]))
put(3,r'''
**One loop traversal reverses the observed logic level.** An odd number of inverters returns the opposite level to a chosen node after the sum of their transition delays. In the stated symmetric fixed-delay model, five stages at $5\,\mathrm{ns}$ give one half-period of $5\cdot5=25\,\mathrm{ns}$. The opposite edge must traverse the loop again before the starting node returns to its original level, so
$$T=2\cdot5\cdot5\,\mathrm{ns}=50\,\mathrm{ns}.$$
Frequency is the reciprocal of the full period, not the reciprocal of one traversal:
$$f=\frac{1}{50\cdot10^{-9}\,\mathrm{s}}=20\cdot10^6\,\mathrm{Hz}=20\,\mathrm{MHz}.$$
This selects option 3. A dimensional shortcut is $f_{\mathrm{MHz}}=1000/T_{\mathrm{ns}}$; using 50 directly as seconds would lose nine orders of magnitude.

**Alternatives and model boundary.** Forty megahertz uses the25 ns half-period as a full period. Ten megahertz would double the correct full period once more to100 ns. Five megahertz would use200 ns, an unjustified further factor of four. The ordinary ring formula requires odd inversion count and assumes an established oscillating regime with the specified transition delays. It does not prove startup, amplitude, edge rate, or a measured physical frequency. If rise/fall delays differ, sum both directional traversals; there is no justification for using one common delay unless the question supplies it.
''')
put(4,r'''
**Separate the Elmore contributions that scale differently.** For a fixed RC topology, an Elmore moment is a sum of terms $R_{\mathrm{shared},j}C_j$, where the resistance is the portion shared by the source-to-output and source-to-capacitor paths. Uniformly doubling this gate's transistor widths halves each relevant on-resistance. Its width-dependent diffusion/internal capacitances double, while the explicitly specified next-stage load remains fixed.

For an internal term, $(R/2)(2C)=RC$. For a fixed-load term, $(R/2)C_L=RC_L/2$. For each modeled switching case, group the initial positive contributions as $I$ and $L$:
$$D=I+L,\qquad D'=I+L/2.$$
Consequently
$$D'/D=\frac12+\frac{I}{2(I+L)},\qquad 1-D'/D=\frac{L}{2(I+L)}.$$
With positive internal capacitance and positive load, both fractions establish $1/2<D'/D<1$ for that case. To handle the requested maximum, the case maximizing old delay supplies a new delay strictly greater than half the old maximum; the maximum new delay is at least that large. Conversely, every new case is strictly smaller than its own old delay and therefore smaller than the old maximum; finitely many cases preserve that strict upper bound. The worst-case input pattern need not remain the same. Thus the maximum decreases but remains greater than half, option 2. The original NAND and fixed-load statement were rechecked against the source page.

**Reject each distractor using the model.** Option 1 suggests the ratio can cross below one half, impossible with nonnegative contributions. Option 3 also contradicts that lower bound. Option 4 would require the load contribution to vanish or scale with the driver, neither matching the stated loaded gate. Exactly half is a limiting case with zero internal contribution; unchanged delay is the zero-fixed-load limit. These boundaries explain why treating all capacitances as fixed, or all as scaled, loses a condition. This is an Elmore/scaling result under the stated abstractions, not a promise for input slew, wire effects or a manufactured gate.
''')
put(5,r'''
**Substitute the requested valuation through the named nets.** At $x=0,y=1$, $t=\neg(xy)=1$, $u=\neg(xt)=1$, and $v=\neg(yt)=0$. Therefore $D=\neg(uv)=1$ and $B=\neg(vv)=1$. These computations use the same shared $t$ at both consumers; duplicating its value inconsistently would change the circuit.

**Identify the complete two-output function.** Algebraically,
$$D=xt+yt=\neg(xy)(x+y)=x\oplus y,\qquad B=yt=(\neg x)y.$$
In ordinary integer one-bit subtraction, $x-y=D-2B$. The requested row gives $0-1=1-2=-1$, exactly the borrow case of a half-subtractor. Option 1 has both the correct output pair and the correct interpretation.

**Alternatives.** Option 2 replaces borrow by half-adder carry. A half-adder at01 produces sum1 and carry0, but the actual second NAND output is1. Option 3 incorrectly makes the XOR output zero and calls it equality; equal inputs, not the current unequal inputs, would make XNOR one. Option 4 names the right circuit class but gives the wrong01 output pair, so the label alone does not make it correct. At11 the actual pair is00, while an adder would have carry1; that second row provides a useful cross-check beyond the requested valuation.
''')
put(6,r'''
**Build the complements of the three POS factors.** Name
$$u=\neg(x+y),\quad v=\neg(x+z),\quad w=\neg(y+z).$$
Each is a two-input NOR. A three-input NOR then gives
$$F=\neg(u+v+w)=(x+y)(x+z)(y+z).$$
The POS is majority: with two or three ones, no input pair is00, so every sum is one; with at most one one, a pair of zeros makes one factor zero. Thus three two-input NOR gates followed by one three-input NOR directly implement it, option 1. No literal complement is needed for this particular POS, even though the statement allows complemented input sources.

**Check the other constructions.** One three-input NOR outputs one at000 and zero at111, the opposite behavior at both endpoints. “Three NANDs only” does not specify this required NOR-NOR mapping or provide its three complemented factors and final combination. Two two-input NORs have at most one previous gate available to the output and cannot implement the stated direct three-factor construction. This question asks which listed fan-in combination realizes the *given direct POS mapping*, not a universal minimum over every alternative network and free source resource. If only two-input cells were allowed, the final three-input NOR would require a polarity-correct decomposition; treating its three pins as a free binary gate would change the cost model.
''')
put(7,r'''
**Trace the given event times before adding the output delay.** With $b=c=1$, the settled function $ab+(\neg a)c$ is one on both sides of the$a$ transition. The statement supplies the actual arrivals at the two OR inputs: the old asserted product falls at2 ns, and the new product rises at7 ns. Thus the Boolean OR-input result is zero on $[2,7)$ and one outside that interval.

An equal one-nanosecond transport delay translates each edge independently:
$$t_{\mathrm{fall}}=2+1=3\,\mathrm{ns},\qquad t_{\mathrm{rise}}=7+1=8\,\mathrm{ns}.$$
The output low interval is $[3,8)$ ns, option 2, and its width remains five nanoseconds. This is a possible static-one hazard, not a contradiction of the steady-state truth table.

**Alternatives and repair.** Option 1 gives the internal gap without translating it through the OR. Option 3 shifts the edges earlier, whereas the positive transport delay moves them later. Option 4 would require overlapping asserted paths, a stable bridging term, or a pulse-rejection model not supplied here. Adding consensus $bc$ gives an already settled one path during this specified stable-context transition, while preserving every settled output. A stated inertial rule could filter a pulse, but an ordinary propagation number alone does not establish such a rule.
''')
put(8,r'''
**Add delays along a path and take the maximum across parallel paths.** The first incoming path has late arrival3 ns. The second has serial components2 and4 ns, so its arrival is $2+4=6$ ns. The final AND must accommodate the later relevant input and then its own one-nanosecond delay:
$$L(F)=\max(3,2+4)+1=6+1=7\,\mathrm{ns}.$$
Option 3 follows. The two incoming paths run concurrently; their complete delays must not be added as though the signal traversed both.

**Alternative diagnoses.** Four nanoseconds accounts only for the fast three-nanosecond path plus the final gate. Six gives the slow incoming arrival but omits the final AND. Ten adds all gate delays across both parallel paths, $3+2+4+1$, treating a branching graph as a serial chain. The critical incoming path is the2+4 branch, but that statement identifies a structural settling bound under the supplied model; it does not assert that every input pattern sensitizes a transition along that path.

**Transfer.** When primary inputs arrive at different times, add each arrival to its own path before comparing the paths. With pin-specific final delays, compare $L_1+p_1$ and $L_2+p_2$, rather than use a common delay that the problem did not provide. Earliest-disturbance analysis would use the lower bounds and a minimum recurrence, which is a separate question from this latest arrival.
''')
put(9,r'''
**The second NAND has tied, not independent, inputs.** Let $A=\neg(xy)$. Because both pins of the output gate receive that same net, $F=\neg(AA)=\neg A=xy$ by AND idempotence and double complement. At10 the product is zero, hence the required pair is $xy$ and0, option 1.

**Inspect every candidate at more than a mnemonic level.** Option 2 describes OR, which is one on10; it disagrees with the circuit's output and truth function. Option 3 describes only the first gate's value and omits the output inversion. Option 4 gives XOR, also one on10, and differs from AND at01 as well. The complete AND output vector is0001 for rows00,01,10,11. No gates are duplicated by writing the same net on two pins; electrically, however, the output of the first gate drives two receiving pin capacitances.

**Cost boundary.** The drawing uses two NAND instances. One NAND with only$x,y$ available could compute only $\neg x$, $\neg y$ or $\neg(xy)$, and none is positive AND. Thus two gates are also a minimum under the no-free-complements/no-external-constants model, allowing tied inputs and fanout. A free positive AND cell or a different allowed library would invalidate that specific lower-bound argument.
''')
put(10,r'''
**Form a dimensionless ratio with the same activity convention.** In $P=\alpha CV^2f$, use the same definition of$\alpha$ before and after the change. Capacitance is unchanged, activity scales by1/2, frequency by2, and voltage by0.8. Therefore
$$\frac{P'}P=\frac12\cdot1\cdot(0.8)^2\cdot2=0.64.$$
The activity and frequency factors cancel; voltage contributes its square rather than its first power. This gives option 2.

**Alternatives.** Option 1,0.32, squares the voltage correctly but forgets the doubled frequency. Option 3,0.8, uses linear voltage scaling. Option 4,1.28, includes doubled frequency and the squared voltage but forgets that activity halves. Identifying the missing factor is more useful than comparing the candidates numerically.

**Model limits and transfer.** The formula concerns the declared switching-power term. Leakage and short-circuit components are not assumed to obey this same scaling. If the activity factor counts zero-to-one events per clock interval, the capacitor energy supplied per such event is $CV^2$; using a convention that counts all edges requires a corresponding coefficient adjustment. A before/after ratio remains valid only when the convention is held fixed. Frequency is events per time, so changing it multiplies power, not the energy of a single charging event.
''')
put(11,r'''
**Solve the first-order charging equation at the actual threshold.** Charging from zero toward$V$ through$R$ gives $v(t)=V(1-e^{-t/(RC)})$. At $v=3V/4$, divide by the nonzero supply and rearrange:
$$3/4=1-e^{-t/(RC)},\qquad e^{-t/(RC)}=1/4.$$
Taking natural logarithms gives $-t/(RC)=\ln(1/4)=-\ln4$, hence $t=RC\ln4$, option 2. Since $RC$ has time units and the logarithm's argument is dimensionless, the result has the correct units.

**Distractors.** $RC\ln2$ is the half-supply crossing, not the three-quarter crossing. $3RC/4$ assumes voltage rises linearly in time; substituting it into the actual exponential gives $V(1-e^{-3/4})$, approximately0.528V rather than0.75V. $4RC$ reaches approximately0.982V, overshooting the requested threshold. The approach slows as the capacitor voltage nears the supply.

**Generalization.** Reaching a fraction$r$ of the supply, with $0<r<1$, takes $-RC\ln(1-r)$. Discharging *to* that same fraction uses $-RC\ln r$, a different formula because the initial state and direction differ. The ideal charging time to exactly$V$ is unbounded; practical logic thresholds stay below the final asymptote.
''')
put(12,r'''
**Use the correct guarantee/requirement difference at each level.** A high noise margin is the driver's guaranteed minimum high output minus the receiver's required minimum high input. A low noise margin is the receiver's accepted maximum low input minus the driver's maximum low output:
$$NM_H=4.2-3.0=1.2\,\mathrm{V},\qquad NM_L=0.9-0.3=0.6\,\mathrm{V}.$$
The low side is smaller, so option 1 is correct. A symmetric disturbance magnitude must fit both adverse directions; its guaranteed threshold budget is the minimum,0.6 V, under these static bounds.

**Alternatives.** Option 2 uses the low-input threshold itself, forgetting to subtract the nonzero low-output guarantee. Option 3 swaps the high and low differences and therefore misidentifies the limiting side. Option 4 adds4.2 and3.0 instead of subtracting two bounds on the same high-level voltage. At the low boundary, adding0.6 V to a worst-case0.3 V output reaches the0.9 V receiver limit; this is the physical interpretation of the computed margin.

**Transfer.** When the driver and receiver belong to different families, keep the driver's output guarantees and the receiver's input requirements in their respective positions. Positive static margins do not by themselves prove adequate output current, acceptable input capacitance, timing compatibility or analog transient integrity. A negative difference means that even the undisturbed connection is not guaranteed by the supplied specifications.
''')
F={
'and-tree':(r'2^n-1',r'''Put $N=2^n$. A full binary reduction tree starts with$N$ separate input results. Each two-input gate combines two subresults into one, reducing the number of live components by exactly one. Reaching one output requires$N-1$ gates. Equivalently, count tree edges: if$G$ internal nodes each have two children, there are$2G$ edges, while a tree on$N+G$ vertices has$N+G-1$ edges; solving gives$G=N-1$.''',r'''A balanced$N=8$ realization has layers4,2,1, totaling7 gates and depth3. A chain also has7 gates but depth7. The count follows binary branching and distinct leaves, not a particular balancing shape. At$N=1$ the output is the input wire and zero gates suffice.''',{
r'2^n':'counts the leaves rather than the internal combining gates',r'n':'is balanced depth for this power-of-two leaf count, not gate count',r'n-1':'mistakenly subtracts one from the logarithmic depth instead of from the leaf count'},
r'''Option 1 is false: balancing a full binary tree preserves its$N-1$ internal nodes. Option 2 confuses seven gates with three levels in the eight-input example. Option 3 changes the allowed library: one unbounded-fan-in AND could replace the whole tree, but that is not a binary-input construction. Option 4 correctly separates gate count from critical-path depth. No sharing or absorption of distinct input requirements is allowed in this stipulated tree.'''),
'nand-and':(r'2n',r'''Each output product$xy$ is formed by a NAND giving$\neg(xy)$ and a tied-input NAND restoring the polarity. Thus each independent two-input AND construction has exactly two instances. With$n$ separate outputs and no sharing between them, sum the instance counts to obtain$2n$. Counting an inner net twice in a symbolic expression does not duplicate its gate.''',r'''For two products, name$t_1=\neg(a_1b_1)$,$F_1=\neg(t_1t_1)$ and$t_2=\neg(a_2b_2)$,$F_2=\neg(t_2t_2)$. Four gates give both positive products. Each path has two stages. Each$t_i$ drives two pins of its restoration gate, so load count is not identical to gate-instance count.''',{
r'n':'keeps only the first complemented product and misses every output-polarity restoration',r'3n':'adds an unnecessary third gate to each two-gate construction',r'n+1':'assumes one output inverter can restore several distinct product nets independently'},
r'''Option 1 contradicts$\neg(tt)=\neg t$. Option 2 violates the independent-output/no-sharing construction contract; one wire cannot carry two different product values at the same time. Option 3 is true: changing available complemented signals or the required output polarity can change the mapping. Option 4 mistakes NAND for positive AND, contradicted at11. The stated count is a construction count under explicit resources, not a minimum claim for every conceivable library.'''),
'xor-chain':(r'4n',r'''Combining$n+1$ independent inputs serially requires$n$ binary XOR operations: the first joins two inputs, and each further operation incorporates one new input. Every stipulated XOR unit has four NAND instances, with its own shared internal net but no sharing with other XOR units. The total is therefore$4n$ NAND gates.''',r'''For three inputs, first compute$x_1\oplus x_2$ with four NANDs and combine that result with$x_3$ using four more. The total is eight. Within each unit the auxiliary NAND result feeds two middle NANDs; it is one shared gate, not two. Replacing XOR by a primitive one-cell XOR changes the pricing model rather than disproves the substituted count.''',{
r'n':'counts abstract XOR units rather than their four-NAND implementations',r'2n':'charges only two NANDs per XOR and omits necessary internal operations',r'3n':'misses one of the four gates in each specified XOR realization'},
r'''Option 1 changes the stipulated primitive cost. Option 2 ignores the explicit no-sharing condition; a different optimized network requires its own derivation. Option 3 is correct: a balanced tree over the same leaves still has$n$ binary XOR nodes, so substitution still uses$4n$ NANDs, while the dependency depth can fall from linear to logarithmic. Option 4 ignores the increasing number of dependent units in a serial chain. Gate-count invariance under balancing does not prove identical load or detailed NAND path delay.'''),
'mux-tree':(r'2^n-1',r'''With$N=2^n$ independent leaves, each two-to-one selector is one binary internal tree node. A full tree has$N-1$ such nodes, obtained either from the binary edge count or the level sum$2^{n-1}+\cdots+2+1=2^n-1$. The$n$ address bits choose a path; they are control signals, not$n$ mux instances.''',r'''An eight-to-one balanced tree uses four muxes at its leaf level, two next and one final: seven muxes. Three address bits suffice. Label the first level with its least-significant selection decision and the later levels consistently with the input numbering, or explicitly declare another address convention. The same block count can implement a permuted data selection if the pin labels change.''',{
r'2^n':'counts data leaves rather than mux instances',r'n':'counts select bits or balanced levels instead of nodes',r'2^n-2':'omits the final selector that combines the last two subtree outputs'},
r'''Option 1 is correct because swapping$I_0/I_1$ on a mux reverses that select decision while preserving the number of blocks. Option 2 ignores this change in the selected data. Option 3 confuses$n$ control bits with$2^n-1$ selectors. Option 4 removes half the independent address choices unless the data or specification is additionally constrained. At$n=0$, one data input can connect directly with zero muxes, but the bank's numerical parameter domain is positive.'''),
'ripple-delay':(r'2n+1',r'''The carry entering the last, bit$n-1$, sum output traverses$n-1$ carry stages. Its arrival is$2(n-1)$. The sum then takes three more units, giving$2(n-1)+3=2n+1$. The final carry traverses$n$ stages and arrives after$2n$ units. Compare both candidate outputs: the last sum is one unit later, so the overall maximum is$2n+1$.''',r'''For three bits, the carry arrivals are$c_1=2$,$c_2=4$,$c_3=6$. The last sum follows$c_2$ at$4+3=7$, later than final carry6. At one bit there are no preceding carry stages; the sum takes3 and carry2. This boundary confirms$2n+1$ without inventing a negative stage count.''',{
r'2n':'counts only the final carry path and omits the slower sum',r'n+3':'charges one unit rather than two for each preceding carry stage and additionally miscounts its endpoints',r'n+1':'uses the wrong per-stage delay and omits the final three-unit sum contract'},
r'''Option 1 is false under the supplied delays: the final sum exceeds final carry by one. Option 2 adds parallel paths instead of taking their maximum. Option 3 discards the actual delay contract; changing the carry/sum costs changes which output is critical. Option 4 states the correct procedure: compare every candidate output path. This is a specified abstract path model, not a general physical timing result for all ripple-adder implementations.'''),
'rc-scaling':(r'1+1/n',r'''The initial internal term is one unit and the initial external-load term another. Scaling widths by$n$ divides resistance by$n$ and multiplies internal capacitance by$n$. Their product remains one. The externally fixed capacitance does not scale, so its contribution becomes$1/n$. The new total is therefore$1+1/n$, not$2/n$.''',r'''At$n=2$, the initial delay2 becomes$1+1/2=1.5$, a ratio3/4. At$n=1$ there is no change and the expression returns2. As$n$ grows, the internal term approaches the nonzero limit1 while the fixed-load term tends to zero. This is a delay in the stated time units; dividing it by the old2 would instead produce the new/old ratio.''',{
r'2/n':'incorrectly treats the width-dependent internal capacitance as fixed',r'2':'incorrectly scales the externally fixed load with the driver as well',r'1':'drops the positive fixed-load term at a finite width scale'},
r'''Option 1 is true: the internal$RC$ product sets a nonzero floor in this model. Option 2 ignores that retained product. Option 3 contradicts the explicit fixed-load assumption. Option 4 contradicts the stated internal-capacitance scaling. Input slew, unscaled interconnect and device nonlinearities can require a more detailed model; they must not be silently inserted into or omitted from the exercise's specified contract.'''),
'ring-frequency':(r'250/n',r'''Each stage has delay2 ns and$n$ is odd. One traversal reverses the observed node after$2n$ ns; a second traversal restores the original level. The modeled full period is$T=4n$ ns. Convert its reciprocal to megahertz: $f_{\mathrm{MHz}}=1000/(4n)=250/n$. A period and its reciprocal have different scaling directions.''',r'''For five inverters, one traversal takes10 ns and the full period20 ns, giving50 MHz. For seven, the full period28 ns gives$1000/28=250/7$ MHz. Both rising and falling transitions must be included. The formula describes an established ordinary ring regime with the supplied equal transition delays, not guaranteed startup or every possible feedback network.''',{
r'500/n':'uses the half-period rather than the full cycle',r'1000/n':'counts only one nanosecond per stage and one traversal instead of the supplied two and two',r'250n':'multiplies by stage count even though increasing loop delay reduces frequency'},
r'''Option 1 correctly states the odd-inversion assumption for this ordinary ring model. Option 2 treats an even-inversion loop as having the same oscillation mechanism; it can instead have consistent stable binary states. Option 3 confuses an opposite-level return with a complete cycle. Option 4 violates$f=1/T$: increasing a positive period decreases frequency. The formula is not a physical certification of oscillation for arbitrary gate models or initial conditions.'''),
'consensus-cost':(r'6n',r'''Each stipulated output has$ab+(\neg a)c+bc$. The first and second products each contain two literal occurrences, and the consensus bridge has two more. Thus a completed SOP contains six occurrences. Summing across$n$ independent, separately counted outputs yields$6n$. A complemented literal is one occurrence, not an extra algebraic variable or a second occurrence.''',r'''For one output the bridge adds two occurrences to the original four. Its functional redundancy follows$bc=abc+(\neg a)bc$, covered by the original two products. With$b=c=1$ the bridge is independent of changing$a$ and remains asserted, explaining its timing purpose. Literal occurrence count is not a count of gates, inverters or physical transistor controls.''',{
r'4n':'counts only the original two products and leaves out every bridge',r'3n':'counts product terms rather than their two literals each',r'2n':'counts only the added literals, not the completed SOPs'},
r'''Option 1 is correct: a truth-table-redundant term can protect a specified transition in a delay-aware implementation. Option 2 confuses settled function with waveform behavior. Option 3 contradicts the consensus identity. Option 4 ignores which variable hands responsibility between paths. The protection requires the stable side inputs and appropriate two-level/single-input model; it is not a cure for every multi-input or multilevel hazard.''')}
for i in range(13,45):
 q=rows[i-1]['canonical'];form,proof,example,wrong,bound=F[q['family']];mode=(i-13)%4
 if mode==3:put(i,'**Check the modeling condition.** '+bound+'\n\n**Derive the construction or timing result.** '+proof+'\n\n**Concrete check.** '+example);continue
 calc='**General answer.** The result is $'+form+'$ throughout the stated parameter domain; special numerical coincidences do not prove competing formulas valid.'
 n=q.get('audit',{}).get('n')if q.get('audit')else None
 if n:
  expressions={'and-tree':rf'2^{n}-1={2**n}-1={2**n-1}','nand-and':rf'2\cdot{n}={2*n}','xor-chain':rf'4\cdot{n}={4*n}','mux-tree':rf'2^{n}-1={2**n-1}','ripple-delay':rf'\max(2({n}-1)+3,2\cdot{n})={2*n+1}','rc-scaling':rf'1+1/{n}={n+1}/{n}','ring-frequency':rf'1000/(4\cdot{n})=250/{n}','consensus-cost':rf'6\cdot{n}={6*n}'}
  calc='**Exact requested calculation.**\n$$'+expressions[q['family']]+'$$\nRetain the declared unit and distinguish a count, depth, delay, ratio and frequency before comparing options.'
 diagnoses=[]
 for j,opt in enumerate(rows[i-1]['options'],1):
  if j==rows[i-1]['answer']:diagnoses.append(f'Option {j}, {opt}, is the derived result.');continue
  key=opt.strip('$');why=wrong.get(key)
  if n:
   numeric={'2^n':Fraction(2**n),'n':Fraction(n),'n-1':Fraction(n-1),'2^n-2':Fraction(2**n-2),'2n':Fraction(2*n),'3n':Fraction(3*n),'n+1':Fraction(n+1),'n+3':Fraction(n+3),'2/n':Fraction(2,n),'2':Fraction(2),'1':Fraction(1),'500/n':Fraction(500,n),'1000/n':Fraction(1000,n),'250n':Fraction(250*n),'4n':Fraction(4*n)}
   def value(s):
    s=s.strip('$');m=re.fullmatch(r'\\frac\{(\d+)\}\{(\d+)\}',s);return Fraction(int(m[1]),int(m[2]))if m else Fraction(s)
   v=value(opt);matches=[(k,w)for k,w in wrong.items()if numeric.get(k)==v]
   if matches:key,why=matches[0]
  assert why,(i,opt,wrong)
  diagnoses.append(f'Option {j}, {opt}, comes from ${key}$, which {why}.')
 put(i,'**Derive the actual construction or timed path.** '+proof+'\n\n'+calc+'\n\n**Diagnose each alternative.** '+' '.join(diagnoses)+'\n\n**Concrete example and boundary.** '+example)
put(45,r'''
**Translate both gap edges through the same transport delay.** The stable side inputs give $F=a+\neg a=1$. During the stated falling$a$ transition, the old$ab$ product drops at2 ns and the new$(\neg a)c$ product rises at5 ns. Their OR-input result is zero on $[2,5)$, a three-nanosecond gap. Equal one-nanosecond output transport delay gives a falling output at3 ns and a rising output at6 ns.
$$w=(5+1)-(2+1)=3\,\mathrm{ns}.$$
Option 3 is correct. The equal delay translates the interval without changing its width. One nanosecond is the gate's transport delay, not the pulse width; two and four have no support in the supplied event times. Subtracting the delay from only one edge would invent asymmetric timing and incorrectly change the width.

**Transfer and repair.** The same interval mechanism appears in Question 7, with different input-event times and a different select edge. Always identify the old falling product and new rising product from the specified transition rather than swapping them by visual habit. A stable consensus$bc$ term holds the output high without changing the truth function under the appropriate settled-side-input SOP model. An inertial model with an explicit rejection rule could give another waveform; a one-nanosecond propagation number alone does not imply that rule.
''')
put(46,r'''
**Compute the adverse disturbance budget on each level.** The driver guarantees low no greater than0.2 V, while the receiver accepts low through0.7 V, giving
$$NM_L=0.7-0.2=0.5\,\mathrm{V}.$$
For a high level, subtract the receiver's2.0 V requirement from the driver's2.4 V minimum guarantee:
$$NM_H=2.4-2.0=0.4\,\mathrm{V}.$$
The smaller margin is0.4 V, option 2. It bounds a symmetric static adverse disturbance that must fit both sides; the high side is the bottleneck.

**Options.**0.2 V is the maximum low output level itself, not a gap between a guarantee and requirement.0.5 V is the valid low margin but ignores the smaller high margin.0.7 V is the low-input threshold itself. Checking the limiting high case directly, subtracting0.4 V from a worst-case2.4 V high reaches the2.0 V acceptance boundary; this explains what the answer measures.

**Boundary.** If a voltage margin were negative, the undisturbed connection would not be guaranteed by the supplied bounds. A positive margin does not certify output-current capability, loading, pulse response or timing. These are receiving/driver static specifications, not probabilities of an error or claims about arbitrary noise waveforms.
''')
assert len(A)==46
(E/'g_gates-solutions.md').write_text('\n\n'.join('## Q'+str(i)+'\n\n'+A[i]for i in range(1,47))+'\n',encoding='utf-8')
print({'answers':len(A),'words':sum(len(v.split())for v in A.values())})
