# Multiplexers, Decoders, Encoders, and Function Realization

## 1. Sources, scope, and a reading method

This chapter combines four reviewed written university courses: Stanford EE108A, MIT 6.004, Cambridge Digital Electronics, and ETH Zurich Digital Design and Computer Architecture. Their exact chapters, instructors, accessible texts, selection reasons, and corrections appear in the source audit and References. The material below is an original synthesis with independent derivations, not a transcription of their notes. The candidate comparison is bounded to documented accessible courses; it does not claim that every course in the world has been inspected. Stanford supplies the broadest block-design treatment; MIT supplies cofactor reasoning and structured lookup; Cambridge supplies practical polarity, programmable arrays, and bus contracts; ETH supplies a second independent block-level derivation.

The prerequisite is Boolean algebra, including minterms, complements, and truth tables. Read the chapter in dependency order: select a value, decode an address, realize a function, encode a request, then combine blocks. A circuit symbol is meaningful only with its input ordering, enable polarity, inactive value, and validity rule. Each diagram and problem states these conventions. Logical checkpoints show exact dependencies; they are not transistor-level timing waveforms.

## 2. The signal contract comes before the drawing

Unless stated otherwise, a word is written most-significant bit first; $s_1s_0$ denotes the integer $2s_1+s_0$. Inputs $I_0,I_1,I_2,I_3$ are indexed by that integer. A positive-logic enable $e$ activates a block when $e=1$. An active-low enable $\overline{EN}$ activates it when the external pin is zero. The overbar describes the pin's polarity, not an instruction to silently invert every other signal.

We distinguish an **asserted** signal from a signal whose numerical value is one. An active-low decoded output is asserted when its value is zero. Similarly, a binary code needs a valid bit if the all-zero request could be confused with a request at index zero. Invalid address codes are not automatically don't-cares. A specified default, blank display, error flag, or inactive output must be implemented and tested. Unknown HDL values and a physically floating bus are outside the ordinary two-valued Boolean model unless explicitly included.

## 3. Derive the two-input multiplexer

A multiplexer chooses one data value. For select $s=0$, its output is $d_0$; for $s=1$, it is $d_1$. The mutually exclusive selection terms give

$$y=\overline{s}d_0+sd_1.$$

The plus sign here is Boolean OR, not integer addition. To prove the equation, substitute each select value: at zero the second product vanishes, and at one the first vanishes. Data can themselves be functions or entire words. A width-$w$ word multiplexer applies the same selector to $w$ independent bit slices; it has two $w$-bit inputs and one $w$-bit output, not $w$ different selectors.

Connecting $(d_0,d_1)=(0,1)$ produces $s$; $(1,0)$ produces $\overline{s}$. Connecting $(0,b)$ produces $sb$, and $(1,b)$ produces $\overline{s}+b$. These are consequences of selection, not new primitive gates. When cascading multiplexers, derive the first output as a named signal and substitute it into the next equation. This prevents a select pin from being mistaken for a data input.

<!-- SIM: mux -->

## 4. Shannon expansion proves universality

For any Boolean function $f(x,u)$, define its cofactors $f_0(u)=f(0,u)$ and $f_1(u)=f(1,u)$. Then

$$f(x,u)=\overline{x}f_0(u)+xf_1(u).$$

The proof is by the two possible values of $x$ and requires no assumption about the remaining variables. A 2:1 multiplexer therefore realizes one Shannon decomposition. Recursing on all $n$ variables yields a binary decision tree whose leaves are constants. Equivalently, one $2^n$:1 multiplexer with $n$ selectors implements any $n$-variable truth table. The exponential count refers to **data inputs**, whereas $n$ is the number of **select inputs**. Interchanging these counts is a serious design error.

An arbitrary four-variable function needs sixteen constant leaves under complete expansion, but simplification can merge identical cofactors or replace a pair of constant leaves by the remaining variable or its complement. Universality gives an upper construction bound; it is not a claim that every function needs that many physical cells.

## 5. Four-input selection and bit ordering

With address $s_1s_0$, the four-input equation is

$$y=\overline{s_1}\overline{s_0}I_0+\overline{s_1}s_0I_1+s_1\overline{s_0}I_2+s_1s_0I_3.$$

Exactly one minterm is one for every legal two-bit address. If the wires to $s_1$ and $s_0$ are exchanged, the address permutation exchanges positions one and two and leaves zero and three fixed. Reordering the data wires can compensate for the select swap. This is why visual location alone does not identify an input index: a figure must label its ports.

For a word multiplexer, the entire selected word is copied. If several sources must drive several destinations independently, use one selector per destination; this is a combinational crossbar. It does not itself enforce exclusive ownership of a source. Arbitration, if required, is a separate policy.

## 6. Use residual variables to reduce the data-input count

Suppose $a,b$ select a 4:1 multiplexer and $c$ remains as data. For each fixed $ab$, inspect the pair $(f(a,b,0),f(a,b,1))$. The four possible pairs map to data functions as follows.

| Pair at $c=0,1$ | Required data function |
|---|---|
| 00 | $0$ |
| 01 | $c$ |
| 10 | $\overline c$ |
| 11 | $1$ |

For $f(a,b,c)=\Sigma m(0,2,6,7)$, the pairs are 10, 10, 00, and 11. Thus the data inputs are $(\overline c,\overline c,0,1)$, with selectors $(a,b)$ in that order. Verify every address: $ab=10$ forces zero for either $c$, whereas $ab=11$ forces one for either $c$. The simplification does not erase the dependence on the select ordering.

For $n$ variables and $k$ selected variables, there are $2^k$ data cofactors, each a function of the other $n-k$ variables. A single remaining variable permits only the four entries in the table. Two remaining variables permit sixteen Boolean functions, some requiring additional logic. The best selector choice depends on cofactor complexity, sharing, fanout, and available cells, not merely the number of variables.

<!-- SIM: shannon -->

## 7. Build and count multiplexer trees

An eight-input selector can be built with seven 2:1 cells: four first-stage cells choose adjacent inputs using $s_0$, two second-stage cells choose pairs of groups using $s_1$, and the last chooses a half using $s_2$. The selected leaf is $4s_2+2s_1+s_0$. A balanced $2^k$-input binary tree has $k$ levels and $2^k-1$ internal cells. The internal-cell count follows either from the geometric sum or from the full binary-tree identity: leaves equal internal nodes plus one.

A balanced tree made solely of $r$:1 cells has $(N-1)/(r-1)$ cells when $N=r^h$, and $h$ levels. This follows because each internal node contributes $r$ child edges and a tree with $N+C$ nodes has $N+C-1$ edges: $rC=N+C-1$. Mixed-radix trees require counting each level separately. For twelve inputs, first use three 4:1 cells and then one 4:1 cell with the unused input given a documented default; invalid top-level code three must not accidentally select real data.

<!-- SIM: tree -->

## 8. Timing is a path calculation, not a cell count

Let a 2:1 cell have data-to-output delay $t_d$ and select-to-output delay $t_s$. A data leaf in a depth-$k$ tree traverses $k$ data arcs. A selector applied at stage $j$, numbering the first stage one, traverses one select arc and $k-j$ later data arcs. Its arrival contribution is therefore

$$T_j+t_s+(k-j)t_d.$$

The output bound is the maximum of all relevant data and selector contributions. If selectors arrive simultaneously, a late-stage selector often has a shorter remaining path; if the high selector arrives much later, it may dominate. Reassigning variables to levels trades off cofactor complexity and timing. Do not infer a nanosecond delay from a gate diagram unless the problem supplies an arc model and loading assumptions.

When $d_0=d_1=1$, the Boolean output stays one as the select changes. A particular AND-OR implementation can nevertheless have a static-one hazard if the two product paths briefly go low. Adding the consensus term $d_0d_1$ removes that single-select static-one hazard under the usual gate-delay model. It does not prove immunity to simultaneous data changes, analog noise, or metastability.

## 9. A decoder generates address predicates

An enabled active-high $n$:$(2^n)$ decoder produces

$$D_i=e\,[a=i],\qquad 0\leq i<2^n.$$

Here $[P]$ is one exactly when predicate $P$ is true. For two address bits, $D_0=e\overline{a_1}\overline{a_0}$ and $D_3=ea_1a_0$, with the mixed minterms in between. When $e=1$, exactly one output is asserted. When $e=0$, none is asserted. The outputs encode an index as a one-hot vector; a decoder does not choose an arbitrary data word.

The identity $D_iD_j=0$ for $i\ne j$ follows because distinct binary addresses differ in at least one bit, forcing a variable and its complement into the product. Also, $\sum_iD_i=e$ under Boolean OR. This partition property is central to function realization, address selection, and safe one-hot controls.

<!-- SIM: decoder -->

## 10. Enables and active-low outputs

For an active-low decoder output, define the external pin $L_i=\overline{e[a=i]}$. When enabled, exactly one $L_i$ is zero; when disabled, all are one. A negative enable input $g$ changes the logical enable to $e=\overline g$, so $L_i=\overline{\overline g[a=i]}$. These two inversions affect different aspects of the contract.

If an enabled active-high decoder realizes $f=\bigvee_{i\in M}D_i$, the corresponding active-low implementation is $f=\overline{\bigwedge_{i\in M}L_i}$, using a NAND of the selected negative outputs. An OR of the negative pins does not implement the same sum of minterms. When the decoder is disabled, this NAND arrangement returns zero, provided $M$ is nonempty. The empty-set function should be connected to zero directly.

## 11. Hierarchical decoder expansion

To construct a 3:8 active-high decoder from two enabled 2:4 decoders, feed $a_1a_0$ to both. Enable the lower bank by $e\overline{a_2}$ and the upper bank by $ea_2$. Lower bank output $j$ represents address $j$; upper bank output $j$ represents $4+j$. This construction uses the high bit to select a bank, not to modify the local address.

For an $n$-bit address split into a $p$-bit high group and $q$-bit low group, $p+q=n$. Predecode each group into $2^p$ and $2^q$ predicates, then combine one high predicate with one low predicate for every output. If $H_h$ and $L_l$ are enabled consistently, $D_{h2^q+l}=H_hL_l$. Sharing group predicates reduces repeated literals but adds a logic level and fanout. Counts must distinguish predecoder blocks, final gates, and primitive gate equivalents.

<!-- SIM: banks -->

## 12. Function realization with decoder outputs

With no don't-cares, a function's minterm set $M$ completely determines it: $f=\bigvee_{i\in M}D_i$ for enable one. Several functions may share the same decoder while using different output-combination networks. A three-input full adder is a useful example: sum uses minterms 1, 2, 4, and 7; carry uses 3, 5, 6, and 7. Sharing the decoder does not imply that the OR networks are also identical.

Compare implementation costs under an explicit metric. An 8-output decoder plus two OR gates is a block count of three, but not a three-primitive-gate circuit. A four-input OR built from two-input OR gates needs three cells. A direct simplified sum-of-products may be cheaper than a complete decoder when only a few terms are needed; a decoder can become attractive when many outputs share address predicates.

## 13. A demultiplexer distributes data

An active-high 1:$N$ demultiplexer has one data input $d$, select address $a$, and outputs $Y_i=d[a=i]$. When $d=1$, the output vector is one-hot; when $d=0$, it is all zero. Thus a decoder with its enable driven by data implements a demultiplexer under this contract. It is not meaningful to call a device with three select bits and eight output wires a three-data-input demultiplexer.

The selected route exists for either data value, but its output value may be zero. A visualization must distinguish the selected route from a wire carrying one. With active-low decoded outputs, the external values and inactive state change; always derive the pins before substituting one block for another.

<!-- SIM: demux -->

## 14. Ordinary encoding requires a legal input domain

An ordinary $N$:$\lceil\log_2N\rceil$ encoder maps a one-hot input request $r$ into its asserted index. For four inputs,

$$b_1=r_2+r_3,\qquad b_0=r_1+r_3,\qquad v=r_0+r_1+r_2+r_3.$$

These equations produce correct codes on the one-hot domain. For requests at indices one and two simultaneously, they produce code three even though index three is not requested. That output is a **phantom code**, not priority resolution. If multiple requests are possible, either detect illegality or replace the ordinary encoder with a priority encoder. A separate valid bit distinguishes no request, $(v,b)=(0,00)$, from request zero, $(1,00)$.

For an unsigned request word, the arithmetic test $r\ne0$ and $(r\mathbin{\&}(r-1))=0$ detects exactly one set bit. The proof is that subtracting one clears the least significant set bit and sets all lower zeros; AND with the original word clears that bit and retains any higher set bit. In mathematical statements use bitwise AND, not Boolean multiplication of entire integers.

## 15. Derive priority encoding from suppression

For highest-index priority, the granted one-hot vector is

$$g_i=r_i\prod_{j=i+1}^{N-1}\overline{r_j}.$$

The product over an empty set is one, so the highest request has grant $g_{N-1}=r_{N-1}$. If a request exists, let $h$ be its greatest asserted index. Every lower grant contains $\overline{r_h}=0$, every higher grant has request zero, and $g_h=1$. Therefore exactly one grant is asserted. The binary output is the ordinary encoding of **grants**, not raw requests.

For lowest-index priority, reverse the suppression direction: $g_i=r_i\prod_{j=0}^{i-1}\overline{r_j}$. An empty request has no grant and valid zero; choose a documented inactive code such as zero. Neither convention is universally implied by the name “priority encoder.” A problem must specify which request wins.

<!-- SIM: priority -->

## 16. Group priority and logarithmic depth

Split eight requests into high and low groups of four. Compute each group's valid bit and local priority index. If the high group is valid, choose its local code and set the global high code bit to one; otherwise choose the low group's code and set the high bit to zero. Global valid is the OR of both group-valid bits.

The critical operation is selection of the winning group's local code. ORing both local codes fails: if the high group requests global index four and the low group requests index three, the winning local code is 00, but ORing 00 with 11 reports index seven. Balanced hierarchy gives logarithmic levels of group summary and selection, while a literal serial suppression chain has linear depth under a fixed small-fan-in gate model. Delay depends on actual implementation; the mathematical group identity alone is not a timing guarantee.

## 17. Leading zeros, rotating order, and fairness

For a nonzero $N$-bit word with highest set-bit index $h$, its leading-zero count is $N-1-h$. For the zero word, the count is $N$. Hence an eight-bit leading-zero counter needs four output bits to represent eight, although a nonzero highest-bit index needs only three. The valid flag resolves the exceptional zero case.

A rotating-priority chooser receives a starting index $p$ and visits $p,p+1,\ldots$ modulo $N$, choosing the first requested index. This is a combinational decision for a supplied pointer. Round-robin fairness additionally requires sequential pointer updates and assumptions about completion and persistent requests. A static chooser cannot guarantee eventual service. Keep that distinction explicit when an animation displays different supplied pointers.

<!-- SIM: rotate -->

## 18. ROMs are truth tables with word outputs

A complete lookup for $n$ address bits and $w$ output bits contains $2^nw$ stored bits. Address $a$ selects the corresponding $w$-bit row. A ROM can realize any collection of $w$ Boolean functions on the same $n$ inputs. A masked implementation, a programmable memory, and a synthesized case statement can implement the same truth mapping while having very different area and electrical characteristics.

Split the address into $r$ row bits and $c$ column bits, $r+c=n$. The array has $2^r$ rows and $2^c$ words per row, each $w$ bits. Row index is $\lfloor a/2^c\rfloor$ and column index is $a\bmod2^c$. Capacity remains $2^r2^cw$, independent of this organizational choice. “Square” refers to a physical bit arrangement, not necessarily equal numbers of row and column **address** bits.

<!-- SIM: rom -->

## 19. PLA and PAL realization

A PLA generates selected product terms in a programmable AND plane and combines them in a programmable OR plane. Product terms can be shared among outputs. For $f=ab+ac$ and $g=ab+bc$, three product terms suffice in the shared plane: $ab$, $ac$, and $bc$. A complete decoder would generate all minterms; the PLA need not. A cube such as $ab$ covers both values of the omitted variable $c$, so a product term is not necessarily a minterm.

A conventional PAL has programmable products feeding fixed output OR groups. The same logical product may need duplication when two outputs use it and the architecture does not permit sharing. Device-specific feedback and macrocell features can change this accounting; use the architecture stated in the question. NAND-NAND can realize a sum of products by De Morgan's law, but an arbitrary NOR-NOR plane requires correct input and output polarities; do not infer equivalence merely from the number of levels.

## 20. Seven-segment decoding and explicit invalid codes

We label segments $a$ through $g$ conventionally: top, upper-right, lower-right, bottom, lower-left, upper-left, and middle. A segment word is written $abcdefg$ and is active-high. Digit zero is 1111110; digit one is 0110000; digit eight is 1111111. A common-anode active-low interface complements all seven output bits. The digit identity does not determine polarity or bit order.

For a BCD-to-display decoder, inputs ten through fifteen are invalid decimal digits. Our contract blanks them, so their output is 0000000. Those rows cannot also be treated as don't-cares in simplification. A decoder allowing arbitrary invalid outputs is a different specification. Test reference tables independently from the implementation: generating both from one erroneous constant can make every test pass while displaying the wrong digit.

<!-- SIM: display -->

## 21. Tri-state buses are not ordinary OR networks

A tri-state driver outputs its data when enabled and a high-impedance state, Z, otherwise. Z means disconnected, not logical zero. If all drivers are disabled, an unpulled bus has no defined binary value. If two active drivers demand different values, the bus is in contention; a Boolean OR of their data would conceal that physical conflict. Equal-value multiple drivers may avoid a Boolean disagreement but still violate the intended single-owner electrical contract.

For a deliberate push-pull shared bus, require at most one enabled driver and require exactly one when a valid binary value is needed. A multiplexer implements logical selection without externally tying push-pull outputs together. Open-drain wired logic is a different circuit requiring pull-ups and suitable device contracts. The model here classifies Z, selected data, and conflict; it does not predict voltage, current, or damage.

<!-- SIM: bus -->

## 22. Write complete combinational HDL

In SystemVerilog, `always_comb` communicates combinational intent, but every output must still be assigned on every path. A safe four-input selector has a default before a `case`, then explicit legal branches. For four binary selector codes, every two-valued code is legal; the default also defines the simulation response to unknown-valued selects under ordinary `case` semantics.

```systemverilog
module mux4 #(parameter int W = 8)
  (input logic [W-1:0] d0, d1, d2, d3,
   input logic [1:0] sel,
   output logic [W-1:0] y);
  always_comb begin
    y = '0;
    case (sel)
      2'b00: y = d0;
      2'b01: y = d1;
      2'b10: y = d2;
      2'b11: y = d3;
      default: y = '0;
    endcase
  end
endmodule
```

A priority encoder should default both code and valid, then use a documented priority chain. An ordinary independent sequence of `if` assignments gives later assignments precedence; an `if/else if` chain gives earlier branches precedence. Omitting a no-request assignment can infer storage. A broad wildcard case can treat unknowns as don't-cares and hide a defect; its use needs an explicit four-valued verification contract. The code examples are explanatory source; this chapter does not claim synthesis-tool or silicon timing verification.

## 23. Verification must distinguish nearby wrong designs

Begin with a reference defined independently from the gate equations: a multiplexer uses array indexing; a decoder uses equality; a priority encoder uses a search for an extreme asserted index; a ROM uses a separate word table. Then test all bounded inputs, legal and specified-invalid cases, and every control boundary. Include mutation witnesses: exchange selector bits, reverse priority, omit valid, OR the local priority codes, or invert an active-low output incorrectly. A test suite that cannot distinguish these designs is insufficient.

There are $2^{N+k}$ data/select combinations for an $N$:1 single-bit multiplexer with $k$ selectors and $N=2^k$. Testing only all selector codes with all data bits equal misses wiring permutations. A stronger compact wiring test can use one-hot data vectors and every selector: output should be one exactly where the selector equals the asserted data index. Exhaustive small-domain tests and symbolic derivations support the stated contract; they do not establish correctness of arbitrary imported hardware or every unseen examination question.

## 24. Integrated reasoning: derive before simplifying

Consider a full adder with $C_{in}=1$. Its carry is $c=a+b$ in Boolean algebra, and its sum is $s=\overline{a\oplus b}$. Let $t=s\oplus c$. A following 4:1 multiplexer receives $(\overline c,c,t,\overline t)$ and selectors $xy$. First derive these four data functions; then enumerate the select cases. For $(a,b)=(0,0)$, the data vector is $(1,0,1,0)$. For either mixed pair it is $(0,1,1,0)$; for $(1,1)$ it is $(0,1,0,1)$. In variable order $abxy$, the output minterms are 0, 2, 5, 6, 9, 10, 13, and 15.

This is a source-checked adaptation of an actual MSc circuit problem in the question bank. Its difficulty comes from combining arithmetic, complements, XOR, and select ordering. The circuit animation traces the genuine dependencies; it is not a generic sliding-block animation.

<!-- SIM: integrated -->

## 25. Complete summary and problem-solving workflow

Start every problem by writing the input word order, select mapping, enable polarity, inactive state, and priority rule. A multiplexer selects data by an address; a decoder turns an address into one-hot predicates; a demultiplexer gates those predicates with data; an encoder returns an index under a legal-input rule; a priority encoder resolves multiple requests before encoding. A ROM stores a multi-output truth mapping, while a PLA shares selected product terms.

Derive local equations before connecting blocks. Use Shannon cofactors to choose data inputs. Count internal cells separately from bit slices and logic levels. Calculate delay from supplied arcs and arrival times. Carry validity through every encoder hierarchy. Distinguish a disabled output from a floating electrical bus. Finally verify truth mappings and inspect a counterexample to each plausible wrong design. The following problems require these operations, and the final rules retain the reasoning in complete sentences.

## 26. Worked mathematical and conceptual problems

<!-- INCLUDE: problems -->

## 27. Final examination rules and conceptual checkpoints

<!-- INCLUDE: review -->

## 28. Editable exact-state laboratory

<!-- LAB: mux -->

## 29. References and source boundaries

1. Stanford University. Philip Levis, EE108A, Winter 2008; William J. Dally, *EE108 Class Notes*, Chapters 7–8. [Written reader](https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf). PDF pages 119–146 and 150–162 were inspected for code conversion, selectors, decoders, encoders, ROM organization, and programmable arrays. RAM state and comparator material are neighboring topics rather than the central chapter boundary.
2. Massachusetts Institute of Technology. Chris Terman, 6.004 *Computation Structures*, Spring 2017, Lecture 4, combinational-device written annotations. [Lecture text](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/). The multiplexer, function-lookup, and ROM passages were read; their concepts are independently derived here. No claim is made that the entire course was read for this chapter.
3. University of Cambridge. Ian J. Wassell, *Digital Electronics*, 2025–26, combinational-logic notes. [Course materials](https://www.cl.cam.ac.uk/teaching/2526/DigElec/materials.html), [written notes](https://www.cl.cam.ac.uk/teaching/2526/DigElec/combined_25.pdf), [Examples Paper 1](https://www.cl.cam.ac.uk/teaching/2526/DigElec/examples_25_1.pdf). PDF pages 64–76 and the three-page examples paper were inspected. The decoder address example is normalized to explicitly stated MSB-first indexing.
4. ETH Zurich. Onur Mutlu, *Digital Design and Computer Architecture*, Spring 2020, Lecture 5, Combinational Logic II. [Written slides](https://safari.ethz.ch/digitaltechnik/spring2020/lib/exe/fetch.php?media=onur-digitaldesign-2020-lecture5-combinational-logic-ii-afterlecture.pdf). PDF pages 37–43 were inspected for decoder and selector contracts and hierarchical construction. This introductory contribution does not supply the advanced priority or bus analysis.
5. Iranian MSc Computer Engineering examination, 1404, booklet 335C, PDF page 19, Questions 80 and 82. The original scanned page and source hash were checked. English adaptations preserve the circuit topology and choices; answers are independently derived, not represented as an official answer key. Links to the exact repository commit accompany the questions.

The lesson supplies rigorous derivations and tested finite circuit models. It does not guarantee an examination score, literal universal completeness, or physical timing correctness without electrical parameters. Source-specific corrections, untested boundaries, and verification evidence are recorded in the chapter audits.
