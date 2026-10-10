# Original and reconstructed problems

### 1. A selector implements implication
Derive the function of a 2:1 multiplexer with select $a$ and data $(1,b)$. State exactly when its output is zero.
#### Solution
1. Selection gives $f=\overline a+ab$. Apply absorption, $\overline a+ab=\overline a+b$.
2. This is implication $a\Rightarrow b$. Its only zero row is $a=1,b=0$.
3. At $a=0$ the output is the constant one, irrespective of $b$. At $a=1$ it copies $b$. These cases verify the algebra independently and distinguish implication from OR, which is zero at 00.

### 2. XOR from data cofactors
Implement $a\oplus b$ using one 2:1 multiplexer and, if necessary, an inverter. Explain why no second selector is required.
#### Solution
1. Set select to $a$. The cofactor at zero is $b$; the cofactor at one is $\overline b$.
2. Connect $(d_0,d_1)=(b,\overline b)$. The result is $\overline ab+a\overline b$.
3. One inverter supplies the complemented data. The select already expresses the two alternatives. Swapping the data ports produces XNOR, so the port labels are essential.

### 3. Gate realization with constant data
A designer claims a 2:1 selector with $(d_0,d_1)=(b,0)$ implements OR. Derive its true function and a distinguishing input.
#### Solution
1. The output is $\overline ab$, where $a$ is the select. It is one only at $(a,b)=(0,1)$.
2. At $(1,0)$, OR is one but this circuit is zero. At $(1,1)$ the same disagreement occurs.
3. A select is not an additional OR operand: it controls which data port reaches the output. To implement $a+b$, use data $(b,1)$ with select $a$.

### 4. Nested cofactor substitution
The first selector has select $b$ and data $(a,\overline a)$. The second has select $c$ and data $(t,a)$, where $t$ is the first output. Give the truth mapping as minterms in order $abc$.
#### Solution
1. The first signal is $t=a\oplus b$. The final signal is $\overline c(a\oplus b)+ca$.
2. For $a=0$, the only one row is $b=1,c=0$, giving minterm 2. For $a=1,b=0$, both values of $c$ give one, contributing 4 and 5. For $a=1,b=1$, only $c=1$ gives one, contributing 7.
3. Thus $f=\Sigma m(2,4,5,7)$. This enumeration checks substitution without assuming that XOR remains the final function.

### 5. Universal lookup count
How many constant data entries and select wires suffice for an arbitrary six-variable single-output function? How many distinct functions can that lookup represent?
#### Solution
1. Six selectors address $2^6=64$ data entries, one per truth row.
2. Each entry independently stores zero or one, so the number of possible tables is $2^{64}$.
3. Sixty-four is the number of data entries, not select wires. A 6:1 selector has only six data choices and cannot directly store a complete six-variable truth table.

### 6. Identify four residual data functions
For $f(a,b,c)=\Sigma m(1,2,3,4,7)$, derive the data for a 4:1 selector using $ab$.
#### Solution
1. Group consecutive rows by $ab$. The pairs at $c=0,1$ are 01, 11, 10, and 01.
2. Therefore data are $(c,1,\overline c,c)$ in port order zero through three.
3. Verify the less intuitive group $ab=10$: the function is one at row 4 and zero at row 5, which requires a complement. Treating every isolated one as $c$ would reverse that cofactor.

### 7. Change the selector variables
For the same function $\Sigma m(1,2,3,4,7)$, use $ac$ as selectors and leave $b$ as data. Compare the two choices.
#### Solution
1. Inspect $ac=00$: rows 0 and 2 give 01, hence data $b$. At 01, rows 1 and 3 give 11, hence one.
2. At 10, rows 4 and 6 give 10, hence $\overline b$. At 11, rows 5 and 7 give 01, hence $b$.
3. Data are $(b,1,\overline b,b)$. Both this implementation and the preceding one need one residual-variable inverter; neither is uniquely best without timing, fanout, or available-cell information.

### 8. A four-variable reduction
Implement $f(a,b,c,d)=\Sigma m(0,1,3,4,5,7,8,9,11,14)$ with selectors $ab$ and two-variable data functions.
#### Solution
1. For $ab=00,01,10$, the local $cd$ table is 1101: it is one except at $cd=10$.
2. That cofactor is $\overline c+d$. For $ab=11$, only $cd=10$ is one, giving $c\overline d$.
3. Thus the data vector is $(h,h,h,\overline h)$ with $h=\overline c+d$. One shared OR expression and its complement feed the selector. This is substantially smaller than four separately synthesized cofactors, although actual cost depends on the cell library.

### 9. Majority by cofactors
Realize three-input majority using a 4:1 selector addressed by $ab$ and prove the data assignments.
#### Solution
1. With no ones in $ab$, output is zero; with exactly one one, $c$ decides whether the total reaches two; with two ones, output is one.
2. Hence data are $(0,c,c,1)$.
3. The resulting function is $ab+ac+bc$. The proof counts asserted inputs and independently checks the cofactor construction rather than simply guessing a familiar gate formula.

### 10. Three-of-four threshold
Derive a 4:1 realization of the function that is one when at least three of $a,b,c,d$ are one. Use $ab$ as selectors.
#### Solution
1. At $ab=00$, two residual bits cannot reach a total of three, so data zero is required.
2. At either mixed $ab$ pair, both residual bits must be one, so data $cd$ is required. At $ab=11$, at least one residual bit must be one, so data $c+d$ is required.
3. Connect $(0,cd,cd,c+d)$. This reconstructs the threshold-design reasoning pattern in Cambridge Examples Paper 1 without reproducing its question text.

### 11. Address permutation
A 4:1 circuit has data $(0,1,0,1)$ and selectors $ab$. What does it implement, and what changes if the select wires are exchanged?
#### Solution
1. In normal order the values repeat 0,1 for each value of $a$, so output equals $b$.
2. Exchanging select wires makes the low selector $a$, so output equals $a$.
3. A distinguishing input is $a=0,b=1$. To retain the original function after exchange, permute data to $(0,0,1,1)$. Data indices one and two exchange places under the permutation.

### 12. Recover minterms from residual data
A 4:1 selector uses $ab$ and data $(c,\overline c,1,0)$. Find its minterm set and its complement's set.
#### Solution
1. Port zero contributes row 1. Port one contributes row 2. Port two contributes rows 4 and 5. Port three contributes none.
2. Thus $f=\Sigma m(1,2,4,5)$ and $\overline f=\Sigma m(0,3,6,7)$.
3. Both sets partition the eight legal truth rows. Complementing the output complements every cofactor, giving $(\overline c,c,0,1)$.

### 13. Minimize constant cofactors
For $f=ab+\overline a c$, use $a$ as the selector. Is an inverter on $a$ needed outside the multiplexer?
#### Solution
1. Cofactors are $f|_{a=0}=c$ and $f|_{a=1}=b$.
2. One selector with data $(c,b)$ implements the function. Its internal selection equation already includes the complemented select.
3. No external inverter is needed in the block-count model. A gate-level implementation might internally generate the complement, which is a different accounting convention.

### 14. Two residual variables are not four arbitrary constants
The cofactor for one address group is XOR of residual variables $c,d$. Can that port be connected to a constant or one raw residual variable?
#### Solution
1. Its four truth values are 0110. A constant gives 0000 or 1111; $c$ and its complement give 0011 or 1100; $d$ and its complement give 0101 or 1010.
2. None matches XOR. Additional logic, such as a 2:1 selector using $c$ with data $(d,\overline d)$, is required.
3. The four-entry residual table applies only when exactly one variable remains. Applying it to a two-variable cofactor silently changes the function.

### 15. Constant-leaf binary tree count
Construct an arbitrary five-variable Boolean function using only 2:1 multiplexers with constant leaves. State the upper cell count and depth.
#### Solution
1. Complete Shannon expansion has 32 leaves and 31 internal cells. A balanced expansion has five levels.
2. The level counts are 16, 8, 4, 2, and 1, whose sum is 31.
3. This is an upper construction, not a minimality theorem: identical cofactors and constants may collapse branches. The count excludes constant generators and buffering, as the stated metric counts selector cells only.

### 16. Word-wide selector area
How many one-bit 2:1 cells realize a balanced 16-input selector for 12-bit words? How many select wires are logically needed?
#### Solution
1. A single-bit tree needs $16-1=15$ cells. Twelve bit slices therefore need 180 one-bit cells.
2. Four shared select wires choose the same source word in every slice.
3. The word-level block count remains fifteen if a twelve-bit selector is treated as one block. State which metric is being used; otherwise 15 and 180 appear contradictory while both answer different questions.

### 17. Radix-four tree
Build a 64:1 selector using only 4:1 cells. Derive its cell count and depth.
#### Solution
1. The levels contain 16, 4, and 1 cells, totaling 21. There are three levels and six binary select wires.
2. The tree identity gives $(64-1)/(4-1)=21$, confirming the direct count.
3. Each level consumes two address bits. Counting six binary selectors as six tree levels would mistake wire count for cell depth.

### 18. Twelve sources and invalid addresses
Three 4:1 cells feed a final 4:1 cell to select twelve sources. Specify the addressing and behavior of the four unused addresses.
#### Solution
1. The low two bits select within each group of four; the high two bits select among the three groups. Addresses 0 through 11 select real inputs.
2. Connect the unused final data port to zero. Addresses 12 through 15 then return zero.
3. Four selector blocks suffice. Calling those addresses don't-cares would permit other outputs and violate the stated zero-default contract.

### 19. Data versus select arrival
An 8:1 binary tree has $t_d=2$ ns and $t_s=3$ ns per cell. Data arrive at 1 ns; $s_0,s_1,s_2$ arrive at 0, 4, and 8 ns. Find the bound.
#### Solution
1. The data path contributes $1+3(2)=7$ ns.
2. Selector paths contribute $0+3+2(2)=7$, $4+3+2=9$, and $8+3=11$ ns.
3. The maximum is 11 ns. This calculation assumes the supplied fixed arcs and neglects unspecified loading. Multiplying the largest cell delay by three would miss the actual selector arrival times.

### 20. Move a late variable to the last stage
In the preceding tree, what if the signal arriving at 8 ns is placed at the first stage instead, with the other selector arrivals unchanged as a set?
#### Solution
1. Its contribution becomes $8+3+4=15$ ns rather than 11 ns.
2. The other signals cannot dominate this value under the same arcs, so the new bound is 15 ns.
3. A selector arriving late benefits from fewer remaining data arcs. Reordering it also permutes the input assignment; moving the wire alone changes the selected function unless the data arrangement is adjusted.

### 21. Static-one hazard and consensus
For $y=\overline s d_0+sd_1$, explain the hazard when $d_0=d_1=1$ and derive a logically redundant protective term.
#### Solution
1. The output should stay one, but unequal select and inverter delays can momentarily disable both product terms.
2. Add $d_0d_1$, obtaining $y'=\overline s d_0+sd_1+d_0d_1$. Whenever the new term is one, both data are one and the original function is already one, so the truth mapping is unchanged.
3. The new term bridges the select transition. The guarantee is limited to that static-one hazard model; it does not establish immunity to multiple changing inputs.

### 22. Decoder partition proof
Prove that an enabled three-bit decoder has exactly one asserted output, and explain its disabled vector.
#### Solution
1. Every binary address is exactly one integer $i$ from zero through seven, so exactly one equality predicate $[a=i]$ is true.
2. With enable one, $D_i=[a=i]$ and the output vector is one-hot. With enable zero, every product $e[a=i]$ vanishes.
3. Pairwise products of distinct minterms contain a contradictory literal pair and are zero. The Boolean OR of all outputs equals enable, providing independent algebraic checks of exclusivity and completeness.

### 23. Decode an MSB-first address
For address bits $a_2a_1a_0=101$ and active-high enable one, which decoder output is asserted? What if $a_2$ and $a_0$ are exchanged?
#### Solution
1. Address value is $4+1=5$, so output five is asserted.
2. This particular pattern is symmetric under the exchange and remains five. It is therefore a poor test of wiring order.
3. Use 100 instead: the original output is four and the exchanged output is one. A test should distinguish the suspected defect rather than merely exercise a convenient pattern.

### 24. Active-low sum of minterms
An enabled active-low 3:8 decoder implements $f=\Sigma m(1,3,6)$. Derive the combining gate and disabled output.
#### Solution
1. With $L_i=\overline{e[a=i]}$, use $f=\overline{L_1L_3L_6}$, a three-input NAND.
2. On a selected minterm in the set, one selected pin is zero, so the NAND returns one. Outside the set, all three pins are one, so output is zero.
3. When disabled, all decoder pins are one and the output is zero. ORing the pins would incorrectly return one on many off-set addresses.

### 25. Two independent polarities
An active-low enable pin is $g$, and output pins are active-low. Find $L_2$ for a 2:4 decoder and evaluate $g=1$ and $g=0,a=2$.
#### Solution
1. Logical enable is $\overline g$, and address-two predicate is $a_1\overline{a_0}$. Thus $L_2=\overline{\overline g a_1\overline{a_0}}$.
2. At $g=1$, the internal product is zero, so every output pin is one. At $g=0,a=2$, the product is one and $L_2=0$.
3. Enable inversion and output inversion are separate operations. Removing both because there are “two negatives” is invalid: they act at different locations in the expression.

### 26. Expand to eight outputs
Using two enabled active-high 2:4 decoders, derive the 3:8 output $D_6$ and the two enables.
#### Solution
1. Feed $a_1a_0$ to both blocks. Their enables are $e\overline{a_2}$ and $ea_2$.
2. Output six is upper-bank local output two, so $D_6=ea_2a_1\overline{a_0}$.
3. Both blocks share the local address but never both have asserted enables under a stable binary high bit. Transient physical overlap requires a separate delay analysis.

### 27. Expansion with negative output banks
Repeat the expansion when each 2:4 block has active-low outputs but active-high enables. What are the eight output values when disabled?
#### Solution
1. Use the same bank enables, since enable polarity did not change. Each external output is the complement of its enabled local minterm.
2. With global enable zero, both banks are disabled and all eight external pins are one.
3. When enabled, exactly one pin is zero. Combining these pins as if they were active-high would reverse the meaning of assertion. A bank's output polarity does not by itself change its enable wiring.

### 28. Predecode a six-bit address
Split six address bits into two groups of three. Count predecoded predicates and final two-input combinations for all 64 outputs.
#### Solution
1. Each group generates eight predicates, so there are sixteen distinct predecoded signals.
2. Each output combines one high predicate and one low predicate; 64 final two-input AND gates produce all pairs.
3. These are signal and final-gate counts, not a complete primitive implementation count: the cost of the two predecoders, inversion, fanout, and enable distribution remains separate.

### 29. Address identity in a grouped decoder
With a two-bit high group and three-bit low group, write the output index and predicate for high address two and low address five.
#### Solution
1. The index is $2(8)+5=21$. The full binary word is 10101.
2. Its predicate is $H_2L_5$, or the corresponding five-literal minterm when expanded.
3. Multiplying the high group by four would incorrectly treat the low group as two bits. The group width, not the number of asserted high signals, determines the stride.

### 30. Two-output full-adder decoder
Use one 3:8 decoder to realize full-adder sum and carry. If only two-input OR gates are available, count the output-combination cells.
#### Solution
1. Sum uses outputs 1, 2, 4, and 7; carry uses 3, 5, 6, and 7.
2. Each four-way OR requires three two-input cells, so six output-combination cells are needed if no further sharing is introduced.
3. The shared decoder is additional hardware. Counting “one decoder and two ORs” is legitimate only if arbitrary-width OR blocks are the chosen unit. The shared minterm seven does not make both functions identical.

### 31. Decoder realization of a complemented function
With an always-enabled decoder, $f=D_0+D_2+D_5$. Express its complement using the remaining decoded outputs.
#### Solution
1. Exactly one of the eight outputs is one. Therefore the complement is $D_1+D_3+D_4+D_6+D_7$.
2. This equality depends on enable one. If the decoder is disabled, all $D_i$ vanish: both sums are zero, whereas a true complement of zero is one.
3. The disabled boundary is a counterexample to blindly complementing a minterm set without carrying the enable contract.

### 32. A demultiplexer's zero data
A 1:8 active-high demultiplexer has select five and data zero. Is output five asserted, and is the route selected?
#### Solution
1. All outputs equal zero because $Y_i=d[a=i]$ and $d=0$.
2. The route to output five is selected by the address, but its transmitted value is zero. No active-high output is asserted.
3. Conflating selected route with asserted value leads to a wrong one-hot claim. The animation distinguishes the selected route from the Boolean level on that route.

### 33. Recover a demultiplexed word
For an enabled demultiplexer with one-bit data, show how ORing every output recovers data, and state the effect of an additional enable.
#### Solution
1. Exactly one address predicate is true, so $\bigvee_i d[a=i]=d$.
2. With global enable $e$, the outputs are $ed[a=i]$ and their OR is $ed$.
3. Recovery is guaranteed only if all decoded routes exist and outputs follow the stated active-high contract. Missing or suppressed invalid address routes may force zero even when data is one.

### 34. Four-request encoder ambiguity
Derive the ordinary four-input code for requests at indices one and two together. Explain why adding valid is insufficient.
#### Solution
1. Raw encoder equations give $b_1=r_2+r_3=1$ and $b_0=r_1+r_3=1$, reporting index three.
2. Valid is one because requests exist, but index three is not requested. Thus valid detects emptiness, not one-hot legality.
3. A separate multiple-request flag or priority suppression is needed. Changing the code's inactive value does not repair an illegal simultaneous-request input.

### 35. One-hot legality test
Evaluate the bitwise test $r\ne0$ and $(r\mathbin{\&}(r-1))=0$ for four-bit words 0000, 0100, and 1010. Explain its proof.
#### Solution
1. Zero fails the nonzero condition. For 0100, subtracting one gives 0011, and AND is zero. For 1010, subtracting one gives 1001, and AND is 1000, so it fails.
2. Subtracting one removes the lowest set bit while leaving any higher set bits available to the AND.
3. Therefore the conjunction is true exactly for a nonempty word with one asserted bit. It is an arithmetic implementation of legality, not a priority encoder.

### 36. Minimum width for incomplete encoder domains
An ordinary encoder has ten legal one-hot inputs. What is its minimum binary output width, and how many codes are unused?
#### Solution
1. The width is $\lceil\log_2 10\rceil=4$. Four bits provide sixteen code words.
2. Six codes are unused for legal one-hot requests. A valid flag adds another output if emptiness must be represented distinctly.
3. Three bits provide only eight distinct values and cannot uniquely encode ten legal indices. Unused output codes do not automatically specify what happens on illegal input combinations.

### 37. Highest-index priority
For eight requests $r=01011010$ written MSB first, give the highest-priority grant, binary code, and valid bit.
#### Solution
1. The asserted indices are one, three, four, and six. Highest-index priority chooses six.
2. Grant is 01000000, code is 110, and valid is one.
3. The request word is not itself a one-hot grant. Applying an ordinary encoder directly to it can combine index bits from several requests and produce an incorrect code.

### 38. Lowest-index priority
For the same word, use lowest-index priority and derive the winning grant formula.
#### Solution
1. Index one is the smallest asserted request, so grant is 00000010 and code is 001.
2. Its grant is $g_1=r_1\overline{r_0}$. All higher grants contain $\overline{r_1}$ and are zero; index zero is not requested.
3. Highest and lowest priority are equally valid conventions. An encoder question with no priority specification is incomplete on multi-request inputs.

### 39. Empty product at the highest endpoint
For highest priority on four inputs, write all grant equations and explain why $g_3$ has no suppression factor.
#### Solution
1. Grants are $g_3=r_3$, $g_2=r_2\overline{r_3}$, $g_1=r_1\overline{r_2}\overline{r_3}$, and $g_0=r_0\overline{r_1}\overline{r_2}\overline{r_3}$.
2. No index outranks three. The product over no higher indices is defined as one, preserving $g_3=r_3$.
3. Defining the empty product as zero would suppress the highest request permanently. This boundary matters in both symbolic proofs and program loops.

### 40. Prove grant exclusivity
Prove that two different highest-priority grants cannot both be one, even if every request is one.
#### Solution
1. Suppose $i<j$. Grant $g_i$ contains the factor $\overline{r_j}$, while grant $g_j$ contains $r_j$.
2. Their product therefore contains $r_j\overline{r_j}=0$, so it vanishes.
3. If requests are nonempty, their highest asserted index has no higher asserted request and is granted. This proves both at-most-one and existence, yielding exactly one grant on valid inputs.

### 41. Derive a four-input priority code
For highest-index priority on four requests, derive simplified equations for $b_1,b_0$ and valid.
#### Solution
1. Code bit one is asserted for winning indices two or three, so $b_1=g_2+g_3=r_2+r_3$.
2. Code bit zero is asserted for winning indices one or three: $b_0=g_1+g_3=r_3+r_1\overline{r_2}$. The factor $\overline{r_3}$ is absorbed by the $r_3$ term.
3. Valid is the OR of all requests. The missing suppression factor on $r_1$ would turn the equation into an ordinary encoder and fail on simultaneous requests one and two.

### 42. Group-code OR counterexample
An eight-input highest-priority tree ORs the two local two-bit codes and uses high-group valid as the high bit. Give a failing request word.
#### Solution
1. Request indices four and three, so the word is 00011000. The high group is valid and its winning local index is zero; the low winning local index is three.
2. ORing local codes gives 11, and the high bit one yields global code 111, or seven, which is not requested.
3. Correct logic uses a multiplexer to choose the high group's local code, returning 100. Group validity determines which local code is relevant.

### 43. Three-group priority
Twelve requests form three groups of four, with the highest group winning. Only global indices two, seven, and nine request. Find the group, local code, and global code.
#### Solution
1. Group indices are zero, one, and two. Global index nine belongs to group two with local index one.
2. Select group two, then local code 01. Global index is $4(2)+1=9$, encoded as 1001.
3. Concatenating the two-bit group index and two-bit local index gives the correct four-bit code. Group three is unused and must not be selected by a legal request summary.

### 44. Leading zeros including zero
Give leading-zero counts for eight-bit words 00101000 and 00000000, and the output width needed for the complete domain.
#### Solution
1. The first word has highest asserted index five, giving $7-5=2$ leading zeros.
2. The zero word has eight leading zeros, not seven and not an arbitrary highest-index code.
3. Counts range from zero through eight, requiring four bits. A three-bit priority index can be reused only with a valid flag and special handling for zero.

### 45. Rotating order and wraparound
For eight inputs, starting priority pointer six, and requests at zero, three, and seven, find the winner. What if seven withdraws?
#### Solution
1. The order is 6,7,0,1,2,3,4,5. The first asserted request is seven.
2. If seven withdraws, the first asserted request becomes zero, after the wraparound.
3. Numeric highest or lowest priority alone cannot implement this order. A supplied starting pointer changes the ordering, but no pointer-update or long-term fairness guarantee follows from this combinational decision.

### 46. Stateful fairness is an extra assumption
A rotating chooser always receives pointer zero and all four requests persist. Can its combinational outputs prove round-robin fairness?
#### Solution
1. No. The static order always starts at zero, so index zero wins every invocation.
2. A round-robin protocol would update the pointer, typically to the successor of a completed grant, and would define when completion occurs.
3. Fairness needs those state transitions and assumptions about service progress. A circuit selecting the correct current winner can still participate in an unfair system if the pointer never advances.

### 47. ROM capacity and multiple functions
How much storage is needed for seven Boolean outputs of five address variables in a complete ROM? How many independent truth functions can the ROM represent?
#### Solution
1. There are 32 addresses and seven bits per address, so capacity is 224 bits.
2. Each output column stores a full five-variable truth function. The complete table has 224 independently programmable bits, yielding $2^{224}$ possible vector mappings.
3. The seven functions share address decoding. This count does not include decoders, output circuitry, or physical overhead, and it is not 32 bytes unless padded to eight-bit words.

### 48. Row-column organization
A 256-word, 16-bit ROM uses six row-address bits and two column-address bits. Find rows, bits per row, and the location of address 49.
#### Solution
1. There are 64 rows, each containing four 16-bit words, hence 64 bits per row and 4096 bits in total.
2. Address 49 decomposes as $49=4(12)+1$, selecting row twelve and column one. The row contains words 48 through 51.
3. The bit array is square, 64 by 64, even though the address split is six/two rather than four/four. This reconstructs Stanford's organization pattern using an independently checked address calculation.

### 49. A word count that is not a power of two
A table has ten 7-bit entries and a four-bit address. Under a complete physical 16-row implementation with invalid rows blank, how many stored bits are required?
#### Solution
1. Sixteen physical rows times seven bits require 112 bits. Ten meaningful entries alone contain 70 information bits.
2. Rows ten through fifteen store the specified blank value. A specialized ten-row circuit could have a different physical cost, but that is not the stated complete implementation.
3. Address width gives the available row domain; the legal-data count and physical-storage count must not be silently equated.

### 50. ROM versus simplified logic
A 12-input single-output function is one only when all inputs are one. Compare full truth-table storage with direct product logic under a two-input AND metric.
#### Solution
1. A complete lookup contains $2^{12}=4096$ stored bits. The function itself is a single twelve-literal product.
2. A tree of two-input AND gates requires eleven cells and can be balanced to depth four.
3. These are different resources, so no universal area ratio follows without a technology model. The example shows why a full ROM can be wasteful for a sparse structured function.

### 51. Shared PLA product terms
For $f=ab+ac$ and $g=ab+bc$, count distinct product terms in a shared PLA and in a PAL with disjoint product banks.
#### Solution
1. The PLA shares $ab$, so its distinct products are $ab,ac,bc$, totaling three.
2. A PAL with no inter-output product sharing needs two products per output, totaling four occurrences.
3. This assumes the stated conventional architecture. Feedback or specialized macrocells could alter the count. An omitted variable means the product covers both values of that variable, so these products are cubes rather than complete three-variable minterms.

### 52. NAND-NAND equivalence
Derive a two-level NAND realization of $f=ab+\overline ac$ without confusing the internal product polarity.
#### Solution
1. Let $u=\overline{ab}$ and $v=\overline{\overline ac}$, each generated by a NAND. Generate $\overline a$ with an inverter if not otherwise available.
2. The final NAND returns $\overline{uv}=ab+\overline ac$ by De Morgan's law.
3. ORing $u$ and $v$ instead returns a different function. The second inversion is what converts the complemented products back into a positive sum.

### 53. Segment polarity conversion
Our active-high segment word for digit two is 1101101 in $abcdefg$ order. Find the active-low word and explain what the digit identity alone does not specify.
#### Solution
1. Complement every bit to obtain 0010010. Segment names and positions remain unchanged.
2. Digit two does not specify pin order, common-anode versus common-cathode behavior, or whether a decimal-point bit is present.
3. A wiring diagram or interface contract must provide those details. Merely copying a seven-bit constant from another source can reverse the displayed shape even when the numerical digit is correct.

### 54. Invalid BCD is a specified value
A BCD-to-display circuit blanks inputs ten through fifteen. May those six rows be marked don't-care during minimization?
#### Solution
1. No. Blanking means every segment must be zero on those rows under an active-high contract.
2. A don't-care permits either value, so a simplified circuit may illuminate a segment for an invalid code and violate the blanking requirement.
3. Don't-cares belong only to genuinely unconstrained conditions. A later decision to blank invalid inputs changes the truth specification and requires rechecking the simplification.

### 55. A shared faulty reference table
Both a display implementation and its checker import the same erroneous digit-six constant. All tests pass. What independent evidence is missing?
#### Solution
1. The checker reproduces the same error, so agreement demonstrates consistency rather than correctness.
2. Define expected illuminated segment names independently from the constant table and compare the resulting bits, or inspect a separately sourced reference diagram with the stated polarity.
3. This is a correlated-oracle failure. Increasing the number of inputs tested cannot fix it unless the expected values come from an independent specification.

### 56. Empty tri-state bus
Two active-high tri-state drivers share an unpulled bus and both enables are zero. Can its value be treated as zero in Boolean proofs?
#### Solution
1. Both drivers are disconnected, so the bus is Z in the digital multi-valued model and has no guaranteed binary voltage in the physical circuit.
2. Treating Z as zero introduces an unstated pull-down or a simulation conversion rule.
3. A selected multiplexer with a zero default has a defined zero output; it is not electrically equivalent to a floating bus. The interface must state how an inactive bus is resolved.

### 57. Opposing drivers and false OR reasoning
Two push-pull drivers are enabled simultaneously with data zero and one. A designer predicts one by ORing the enabled data. Explain the fault.
#### Solution
1. One driver attempts low while the other attempts high, producing contention rather than a valid Boolean OR.
2. The exact voltage and current depend on electrical characteristics; the logical model can only flag the conflicting drive.
3. A proper single-owner bus requires mutually exclusive enables. Deliberate wired logic uses suitable output devices and pull components; it is a different circuit from tied push-pull outputs.

### 58. Equal drivers are not a single-owner proof
Two enabled drivers both output one. Does absence of a Boolean disagreement prove compliance with a single-owner bus contract?
#### Solution
1. No. The visible logical value may be one, but there are still two active owners.
2. The asserted-enable count is two, violating the at-most-one requirement. Electrical tolerances and switching behavior remain outside the two-valued conclusion.
3. Verification should check ownership separately from data consistency. Otherwise this input passes while a later data transition can introduce contention.

### 59. Crossbar source replication
Two independent destinations select among three source words. Must the destinations choose different sources, and how many selector blocks are required?
#### Solution
1. Two 3:1 word selectors suffice, one per destination, under a word-block metric. Both may choose the same source.
2. A combinational crossbar replicates values; it does not arbitrate ownership. If resource exclusivity is required, a separate grant policy must constrain the destination selects.
3. With binary selects, unused code three also needs a specified default. Its presence does not automatically provide an arbitration mechanism.

### 60. Complete assignment and inferred state
An HDL priority encoder assigns code only if at least one request is asserted. Explain the no-request behavior and repair the intent.
#### Solution
1. On no request, the unassigned output can retain a previous value, suggesting storage rather than a total combinational mapping.
2. Assign code zero and valid zero before the priority chain. On a winning request, overwrite both with its code and valid one.
3. A combinational process declaration communicates intent but does not replace complete assignments. Test the transition from a valid request to no request, not only isolated nonzero request cases.

### 61. Independent if statements reverse priority
An HDL block assigns code zero by default, then executes `if(r[0]) code=0; if(r[1]) code=1; if(r[2]) code=2; if(r[3]) code=3;`. What priority results?
#### Solution
1. Later executed assignments overwrite earlier assignments. Therefore the greatest asserted index wins.
2. An `if/else if` chain in the same ascending order instead gives lowest-index priority, since the first true branch prevents later branches.
3. These syntactic structures implement different policies on multiple requests. Their single-request behavior is identical, so one-hot-only tests cannot distinguish them.

### 62. Test count for a small multiplexer
How many exhaustive two-valued input cases exist for a 4:1 single-bit selector? Give a smaller wiring-permutation test family.
#### Solution
1. Four data bits and two selectors give $2^6=64$ cases.
2. Use each of four one-hot data vectors and all four selector values, totaling sixteen cases. Output must be one exactly when the selected index matches the asserted data bit.
3. This compact family catches data permutation defects under the basic selector contract, but does not replace exhaustive tests of enable, unknown values, or an implementation with additional control signals.

### 63. All-equal data hide wiring faults
Why do all-zero and all-one data tests fail to detect exchanged data ports in a selector?
#### Solution
1. Permuting identical values leaves the selected output unchanged for every select code.
2. Use differing data, such as a one-hot vector, to make the output sensitive to which port is selected.
3. Test coverage in terms of selector values alone is therefore misleading. A useful case must distinguish the correct mapping from the specific plausible wrong mapping.

### 64. Decoder-enable test count
How many binary input combinations exist for a 4:16 decoder with one enable? What properties should the checker verify?
#### Solution
1. Four address bits plus enable give 32 cases. Sixteen are enabled and sixteen disabled.
2. For enabled cases, verify that exactly the address-matched pin is asserted. For disabled cases, verify the complete inactive vector.
3. Checking only the population count misses an output permutation. Checking only the selected pin misses an extra incorrectly asserted pin. Both exclusivity and index correspondence are required.

### 65. A priority metamorphic property
Under highest-index priority, adding requests below the current winner should not change the code. Prove this and state a boundary.
#### Solution
1. If the current highest request is $h$, adding requests with indices below $h$ leaves the greatest asserted index unchanged.
2. The grant proof therefore still selects $h$. Adding a higher request can change the winner, and removing $h$ can expose another request.
3. The property applies only to a nonempty original word and the stated priority convention. It is a useful independent metamorphic check, but not a complete proof of every implementation branch.

### 66. Exactly-two-hot encoding
Six inputs have exactly two asserted bits. How many legal patterns are there and what minimum output width encodes each pattern uniquely?
#### Solution
1. There are $\binom{6}{2}=15$ unordered pairs. Four bits encode sixteen values and suffice; three encode only eight and do not.
2. An ordinary six-input one-hot encoder cannot recover the pair; ORing its index bits loses information.
3. A pair-ranking scheme or two separately resolved indices can represent the legal pattern. This reconstructs the coding-domain pattern in Stanford Chapter 8 exercises with independently chosen dimensions.

### 67. Decoder followed by a legal encoder
An enabled decoder feeds an ordinary encoder of matching index order. Derive code and valid, including the disabled case.
#### Solution
1. When enabled, the decoder produces exactly one request at the address index, so the encoder returns that address and valid one.
2. When disabled, every request is zero. Under a zero-default encoder, the output code is zero and valid zero.
3. Thus code alone does not equal the address on every disabled input, but the pair satisfies the identity on valid inputs. Carrying valid is necessary for a total interface specification.

### 68. Priority encoder followed by a decoder
Feed a highest-priority encoder code to a decoder whose enable is encoder valid. What does the final vector represent?
#### Solution
1. For a nonempty request, the encoder chooses the highest asserted index and valid enables exactly that decoded output.
2. For an empty request, valid zero disables all outputs. The final vector is therefore the highest-priority grant vector.
3. It is generally not the original request vector when multiple requests existed. The composition resolves information rather than preserving every asserted request.

### 69. How many functions fit one residual selector?
With fixed selectors $ab$ and one remaining variable $c$, each data port may independently be one of $0,1,c,\overline c$. How many three-variable functions are expressible?
#### Solution
1. Each of four ports has four choices, giving $4^4=256$ mappings.
2. There are $2^{2^3}=256$ total three-variable Boolean functions. The cofactor table is bijective, so every function is expressible.
3. The count agrees with Shannon expansion, and it explains why one residual variable is enough with a 4:1 block plus complements. Shared physical wiring may reduce hardware without reducing the mapping set.

### 70. A mux-only universal primitive
Show that 2:1 selectors plus binary constants can form NOT, AND, and OR, and hence arbitrary Boolean functions.
#### Solution
1. Select $a$ with data $(1,0)$ gives NOT. Select $a$ with data $(0,b)$ gives AND. Select $a$ with data $(b,1)$ gives OR.
2. These gates form a functionally complete basis. Alternatively, recursive Shannon decomposition directly constructs any truth table.
3. Constants are part of this construction. Removing available constants changes the assumptions and requires a separate universality argument.

### 71. Selector sensitivity
Prove that changing a 2:1 select affects the output exactly when its two fixed data values differ.
#### Solution
1. At select zero the output is $d_0$; at select one it is $d_1$.
2. Their Boolean difference is $d_0\oplus d_1$, which is one exactly when they differ.
3. Thus the select's Boolean sensitivity is independent of its current value when data are held fixed. This is a truth-function statement; equal data do not by themselves prevent a physical static hazard in every gate implementation.

### 72. Function composition under an output bubble
A 4:1 selector has active-low output and data $(0,c,1,\overline c)$ under select $ab$. Find the external output minterms.
#### Solution
1. The internal positive selector has minterms 3, 4, 5, and 6: port zero none, port one row 3, port two both rows, and port three row 6.
2. The external complement therefore has minterms 0, 1, 2, and 7.
3. Complementing only the select bits would instead permute the data choices; it would not generally complement the output. Output polarity must be applied at the actual pin location.

### 73. Enable location matters
Compare circuit A, $y=e\,\mathrm{MUX}(s,d_0,d_1)$, with circuit B, $y=\mathrm{MUX}(s,ed_0,d_1)$. Are they equivalent?
#### Solution
1. Circuit A suppresses either selected data value when enable is zero. Circuit B suppresses only its zero-select data port.
2. At $e=0,s=1,d_1=1$, A is zero and B is one, providing a counterexample.
3. Enable must gate both data cofactors or the final result to implement a global output enable with zero default. Moving a control through a selector is valid only after an algebraic derivation.

### 74. Gray-coded selector address
A 4:1 lookup is addressed by two-bit Gray code $g_1g_0$ representing binary index $b_1=g_1$, $b_0=g_1\oplus g_0$. Which data port corresponds to each Gray word?
#### Solution
1. Gray 00 maps to binary 00, selecting zero. Gray 01 maps to 01, selecting one. Gray 11 maps to 10, selecting two. Gray 10 maps to 11, selecting three.
2. In numerical Gray input order 00,01,10,11, the chosen binary indices are 0,1,3,2.
3. Either convert the address or permute the data table consistently. Treating a Gray code as an ordinary binary address silently exchanges two choices.

### 75. A correct ignored address bit
A 16-row ROM implements a function depending only on the low three address bits. State the relationship between its two eight-row halves.
#### Solution
1. For every low address $j$, rows $j$ and $j+8$ must contain the same output word.
2. Then changing the high address bit has no effect. Conversely, if the high bit has no effect on any input, each such row pair must match.
3. This gives a necessary and sufficient table test for an ignored address bit. It can also justify replacing the ROM by an eight-row table when the interface permits it.

### 76. Multi-output decoder versus separate lookups
Three functions share four input variables. Compare stored truth bits for one 16-by-3 ROM with three 16-by-1 ROMs and discuss decoder sharing.
#### Solution
1. Both store 48 truth bits. The information content is identical.
2. The multi-output implementation can share address decoding; three separate physical blocks may replicate it.
3. Equal stored-bit counts do not imply equal area or delay. Output loading, memory organization, and technology determine those properties. The problem distinguishes logical information from peripheral implementation overhead.

### 77. Nonempty decoder subset and disabling
For active-high enabled outputs, $f=D_2+D_3$. Can $f$ be expressed as $e a_1$ in a 2:4 decoder? Explain why enable cannot be dropped.
#### Solution
1. Outputs two and three share $a_1=1$ and cover both values of $a_0$, so $f=ea_1(\overline{a_0}+a_0)=ea_1$.
2. At enable zero and $a_1=1$, $f$ must be zero. Dropping enable would incorrectly return one.
3. Combining minterms can remove a fully covered address literal while retaining every global control literal. Simplification must respect the entire input domain.

### 78. One-hot selection outside its domain
A one-hot selector computes $y=r_0d_0+r_1d_1+r_2d_2$. What happens for no asserted selector and for two asserted selectors?
#### Solution
1. With no selectors, every product is zero and output is zero. With two selectors, output is the OR of those two data values.
2. That is a defined Boolean superposition, not unique source selection. If the two values differ, it returns one regardless of an unstated priority.
3. The same algebra cannot be used to justify tying push-pull drivers together; that would be an electrical bus with possible contention. Legal one-hot input constraints are part of the selector specification.

### 79. Integrated full-adder data extraction
A full adder receives $a,b,1$. Derive carry, sum, and their XOR for all four $ab$ pairs before using them as selector data.
#### Solution
1. Carry is $a+b$ and sum is $\overline{a\oplus b}$. For pairs 00,01,10,11, carry values are 0,1,1,1 and sum values are 1,0,0,1.
2. Their XOR is consequently 1,1,1,0, which equals $\overline{ab}$.
3. The integer input sum verifies the full-adder outputs independently. This intermediate derivation avoids treating a carry as parity or forgetting the fixed carry-in one.

### 80. An integrated selector with permuted select order
The data vector is $(\overline c,c,t,\overline t)$, where $c=a+b$ and $t=\overline{ab}$. A 4:1 selector uses $xy$, giving minterms $(0,2,5,6,9,10,13,15)$ in $abxy$ order. Find the minterms if the select wires are exchanged.
#### Solution
1. Swapping $x,y$ exchanges local addresses one and two. In each four-row group, apply this permutation to the original minterms.
2. Group 00 changes rows 0,2 to 0,1. The mixed groups retain both local indices one and two, giving 5,6 and 9,10. Group 11 changes local indices one and three to two and three, giving 14,15.
3. The new set is $(0,1,5,6,9,10,14,15)$. Independent enumeration confirms it. The original function is not preserved because its data ports one and two are not equivalent in every input group.
