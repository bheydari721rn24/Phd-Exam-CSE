# Worked arithmetic-circuit problems

### 1. A full adder is a weighted population counter

Prove the full-adder equations without assuming a memorized truth table, and decide whether its carry can mean “all three inputs are one.”

#### Solution

Let $k=a+b+c$ as an integer, so $k\in\{0,1,2,3\}$. The units bit of $k$ is its parity: $s=a\oplus b\oplus c$. The twos bit is one precisely when $k\ge2$, hence $d=ab\lor ac\lor bc$. For the four possible counts, $(s,d)$ is $(0,0),(1,0),(0,1),(1,1)$. Thus $a+b+c=s+2d$. An AND of all three inputs misses the three cases containing exactly two ones; it cannot serve as carry. This weight argument will remain valid when every input has weight $2^i$.

### 2. Construct and simplify the complete full-adder table

Write all eight input/output rows in order $abc=000$ through $111$. Derive minimal sum-of-products expressions for both outputs.

#### Solution

The output pairs $(s,d)$ are $00,10,10,01,10,01,01,11$. Sum is one at minterms 1, 2, 4 and 7; no two of these cells are adjacent in a three-variable K-map. Consequently its two-level SOP requires four three-literal products. Carry is one at minterms 3, 5, 6 and 7. Pair each of 3, 5 and 6 with 7 to obtain $bc$, $ac$ and $ab$. Every product is essential because its corresponding exactly-two-ones row is covered by no other pair. XOR structure is much more compact than the minimal two-level SOP for sum; “minimal SOP” does not mean “best implementation in every gate library.”

### 3. Why the final OR is legal in a two-half-adder design

Use $p=a\oplus b$, $g=ab$ and $h=pc$. Explain why $g\lor h$ equals $g\oplus h$, and whether this remains true for $p=a\lor b$.

#### Solution

Under XOR propagate, $g=1$ forces $a=b=1$, which forces $p=0$. Thus $gh=0$ for every input and the OR and XOR truth tables differ only on an unreachable joint-one case. Under OR propagate, $a=b=c=1$ gives $g=h=1$. OR then gives the required carry one, whereas XOR gives zero. Therefore the substitution depends on the definition of propagate. Sum must also use XOR propagate; replacing its first XOR by OR makes the all-ones row incorrect.

### 4. Unequal bit weights cannot feed one ordinary full adder

A designer connects two weight-eight bits and one weight-four bit to an ordinary full adder, then labels its outputs weight eight and sixteen. Give a counterexample and a correct reconstruction.

#### Solution

Set only the weight-four input to one. The input value is four, but the proposed sum output has value eight. No Boolean relabeling of the two outputs can represent all possible totals under those weights. Put the weight-four input in column two and the other two in column three. If column two has other operands, compress them there and send its carry to column three. Only equal-weight bits may be locally counted by a full adder. The error is a positional-weight violation, not an overflow problem.

### 5. Population count of seven inputs

Construct a three-bit population counter for seven one-bit inputs using exactly four full adders. Prove its weighted result.

#### Solution

Compress the first three inputs into $(s_0,c_0)$ and the next three into $(s_1,c_1)$. A third full adder counts $s_0,s_1,x_6$, producing result bit $r_0$ and carry $c_2$. All three carries now have weight two. A fourth full adder counts $c_0,c_1,c_2$, producing $r_1$ of weight two and $r_2$ of weight four. Adding the four local identities gives $\sum_{i=0}^{6}x_i=r_0+2r_1+4r_2$. The maximum is seven, so three result bits suffice. This is an independently reconstructed extension of Stanford Exercise 10–5.

### 6. Prove ripple addition by telescoping weights

For n full adders satisfying $a_i+b_i+c_i=s_i+2c_{i+1}$, prove the word-level identity and explain why every internal carry cancels.

#### Solution

Multiply the bit-i identity by $2^i$ and sum for $i=0$ through $n-1$. The left side contains $A+B+c_0+\sum_{i=1}^{n-1}c_i2^i$. The right side contains $S+\sum_{i=1}^{n-1}c_i2^i+c_n2^n$. Subtract the identical internal-carry sum from both sides. The result is $A+B+c_0=S+2^nc_n$. Cancellation is possible because a carry generated in column i has precisely the weight of an input to column i+1. A diagram that connects it to column i+2 changes the arithmetic.

### 7. An entire carry chain with only one generating column

Trace four-bit $1111+0001$ with $c_0=0$. Classify each column as generate, propagate or kill and find the retained sum.

#### Solution

Column zero has $(a_0,b_0)=(1,1)$: it generates $c_1=1$ and gives $s_0=0$. Columns one, two and three have input pair $(1,0)$: they propagate incoming carry, giving sums zero and carries one. Hence $S=0000$ and $c_4=1$, consistent with $15+1=16$. Only one column generates a carry; a long path arises because the following columns propagate it. A count of generating columns cannot determine the chain length.

### 8. A local kill blocks a distant carry

Evaluate four-bit $1111+0001$ with $c_0=0$, then replace $a_2$ by zero. Identify where the incoming carry is killed in the modified circuit.

#### Solution

Originally fifteen plus one produces $0000$ with carry one: column zero generates and all higher columns propagate. With $a_2=0$, A becomes $1011$, or eleven. Columns zero and one still generate/propagate, but column two now has input pair $(0,0)$ and kills $c_3$. Column three outputs one without an outgoing carry. The result is twelve, $1100$, with carry zero. A local kill breaks the dependency from lower carries to every higher column, even when the higher columns would otherwise propagate.

### 9. Arrival times with unit XOR, AND and OR delays

All input bits and $c_0$ arrive at time zero. The implementation computes $p_i=a_i\oplus b_i$, $g_i=a_ib_i$, $c_{i+1}=g_i\lor p_ic_i$, and $s_i=p_i\oplus c_i$. Find structural arrival bounds for an eight-bit ripple adder.

#### Solution

Both p and g arrive at time one. Carry one arrives at $\max(1,\max(1,0)+1)+1=3$. Subsequently each carry adds an AND and an OR delay, so $T(c_i)=2i+1$ for $i\ge1$. Sum zero arrives at two; sum i for $i\ge1$ arrives at $T(c_i)+1=2i+2$. Therefore the last sum arrives at sixteen and final carry at seventeen. These are structural bounds under the stated gates; reconvergent sensitization and technology-specific complex gates require separate analysis. They are not measured nanoseconds.

### 10. A late external carry changes the critical source

Use the preceding gate model with input p/g ready at time one, but $c_0$ ready at time ten. Find $T(c_4)$ and $T(s_3)$.

#### Solution

Carry one now arrives at $\max(1,\max(1,10)+1)+1=12$. The succeeding carries arrive at fourteen, sixteen and eighteen. Sum three arrives at seventeen. The latest source is the external carry, not either word input. The old formula $2i+1$ assumes the carry arrives at zero and cannot be reused after this change. Writing the max recurrence first prevents mixing an operand-to-result path with a carry-to-result path.

### 11. Explain two valid definitions of propagate

Prove $ab\lor(a\oplus b)c=ab\lor(a\lor b)c$. Give the one input pair on which the two propagate signals differ and explain why carry is unaffected.

#### Solution

For $a=b=0$, both propagate definitions are zero. For unequal inputs both are one. For $a=b=1$, XOR propagate is zero and OR propagate is one, but generate $ab$ is already one. Thus both complete carry expressions are one in that case. Equivalently the extra OR-propagate contribution is absorbed by generate. The signals differ precisely on $(1,1)$. That redundancy is harmless in carry logic but not in a sum expression: $s=(a\oplus b)\oplus c$ still requires parity.

### 12. Recover a missing CLA term

A proposed four-bit carry equation omits $p_3p_2p_1g_0$. Give input values that distinguish it from the correct equation.

#### Solution

Choose column zero to generate: $a_0=b_0=1$. Choose columns one through three to propagate: their input pairs are $(1,0)$. Set $c_0=0$. Then A is fifteen, B is one, all higher generates are zero, and only the omitted term produces $c_4=1$. The defective equation gives zero. The correct expansion is $g_3\lor p_3g_2\lor p_3p_2g_1\lor p_3p_2p_1g_0\lor p_3p_2p_1p_0c_0$. Testing only all-zero and all-one input words would not isolate this omission.

### 13. Flat CLA gate count versus fan-in

For XOR propagate, count the nontrivial AND products needed to compute all carries $c_1$ through $c_n$ using fully expanded independent equations. Explain why “two gate levels” is a conditional claim.

#### Solution

Carry k contains k nontrivial products plus the single literal $g_{k-1}$. Summing yields $n(n+1)/2$ AND products, followed by n OR gates. The longest product has n+1 inputs and the final OR has n+1 terms. Calling this two levels assumes gates with those fan-ins and excludes p/g generation. With bounded two-input gates, those wide products and ORs require trees. Sharing products can reduce area but changes the stated independent-equation count. Counting literals, gates and logic depth are different tasks.

### 14. Ordered generate/propagate composition

Let a higher group H and lower group L have carry functions $f_H(c)=G_H\lor P_Hc$ and $f_L(c)=G_L\lor P_Lc$. Derive their combined pair and prove associativity.

#### Solution

Carry enters L first, so substitute $f_L(c)$ into $f_H$. The result is $G_H\lor P_HG_L\lor P_HP_Lc$, giving $(G_H\lor P_HG_L,P_HP_L)$. Function composition is associative, so three adjacent groups can be parenthesized either way without changing any carry. Expanding both sides yields $G_H\lor P_HG_M\lor P_HP_MG_L$ and propagate $P_HP_MP_L$. Adjacency and high/low order are essential; associativity permits regrouping, not exchanging groups.

### 15. Noncommutativity and the empty group

Find two group pairs whose ordered composition changes when their order is exchanged. Then determine the identity pair.

#### Solution

Take H=(0,0), a kill group, and L=(1,0), a generate group. H after L yields (0,0), because the high kill blocks the lower generated carry. L after H yields (1,0), because the high generate overrides the lower kill. They differ. The identity function is $f(c)=c$, represented by (0,1). Combining it on either side preserves any pair. This identity is useful for padding prefix trees; a padding pair (0,0) would incorrectly destroy carries.

### 16. Prefix stage count and a missing edge

An eight-bit parallel-prefix network combines intervals of length 1, 2, 4 and 8. How many combination stages are required? Why cannot its diagram connect an arbitrary nearby pair instead of the required lower interval?

#### Solution

The maximum interval doubles at every combination stage, so three stages cover eight bits. This count excludes initial p/g gates and the final sum XOR. Each node represents a specific contiguous ordered interval. A missing lower interval omits its generated carry; a repeated interval can count it twice; a reversed interval changes the carry function. The network must track both endpoints, not just stage number. Logarithmic logical depth also says nothing by itself about long-wire delay or physical fan-out.

### 17. Count a dense prefix network

For n=8, a dense doubling network creates a combination node at each bit i with $i\ge2^k$ at stage k. Count nodes and compare its depth with ripple.

#### Solution

The stages contain 7, 6 and 4 nodes, totaling seventeen. More generally for n a power of two, the count is $\sum_{k=0}^{\log_2n-1}(n-2^k)=n\log_2n-n+1$. Its three combination stages contrast with eight serial ripple carry steps, but a prefix node may itself contain more than one primitive gate. The comparison is at the architecture level. Other prefix topologies exchange node count, depth and fan-out; seventeen is not a universal minimum.

### 18. Hierarchical CLA is not automatically global lookahead

Four four-bit CLA blocks are connected by rippling their block carries. Compare this with a second-level group CLA.

#### Solution

Each block exposes its G and P pair. In the first design, block $j+1$ waits for the carry leaving block j; accelerating internal carries does not remove this interblock chain. In the second design, all block pairs feed a group network that computes every block-entry carry from the external carry. If pairs are ready at time $T_P$ and each block carry composition costs d, the ripple bound includes roughly four d contributions. A balanced group tree needs two combination stages for the final four-block carry, plus local carry/sum formation. Exact numerical delays require the chosen gate implementation.

### 19. Carry-select resource accounting

Build an eight-bit carry-select adder split into two four-bit blocks. The low block is ordinary ripple; the high block computes both possible incoming carries. Count full adders and one-bit output multiplexers.

#### Solution

The low block uses four full adders. Each speculative high block uses four more, giving twelve total. Selection must choose four sum bits and the final carry, so five one-bit multiplexers are required. Selecting only the sum leaves the carry flag incorrect. This count assumes duplicated complete ripple blocks; constant-input simplification may optimize particular gates but does not change the stated block-level construction. It is an independent reconstruction of the carry-select design pattern in MIT and Berkeley.

### 20. Optimize a simple block carry-select timing model

Suppose an n-bit equal-block carry-select chain has delay $D(b)=\alpha b+\beta(n/b-1)$, with continuous block size b for optimization. Find its minimum and explain the integer restriction.

#### Solution

Differentiate: $D'(b)=\alpha-\beta n/b^2$. The stationary point is $b=\sqrt{\beta n/\alpha}$ and $D''(b)=2\beta n/b^3>0$ for positive parameters. Actual blocks have integer widths and must partition n, so compare legal sizes around this point and possibly an unequal final block. This model describes serial block selection after speculative ripple computation. It does not describe a recursively selected architecture and does not prove every carry-select adder has square-root delay.

### 21. Carry skip uses an exact condition

A four-bit block's XOR propagates are all one. Show that its output carry equals input carry. Explain why observing only three propagates does not justify bypassing the block.

#### Solution

If every p is one, each corresponding g is zero because the two input bits differ. Repeatedly applying $c_{i+1}=g_i\lor p_ic_i$ gives $c_4=c_0$. If one untested column is a kill, it forces the outgoing carry to zero; if it generates, it forces it to one. The bypass predicate is the AND of all block propagates. With OR propagate the input-to-output equality additionally needs the group's generate to be zero; “all p are one” alone is insufficient.

### 22. Carry increment from a speculative zero-carry result

A block computed $S_0$ assuming carry zero. Derive the corrected result for actual carry x and find the incrementer's carry propagation condition.

#### Solution

The actual word is $(S_0+x)\bmod2^b$. If x=0 nothing changes. If x=1, the increment flips the trailing run of ones to zeros and flips the following zero to one. It carries out precisely when $S_0=2^b-1$. The complete block carry includes any carry already generated by the original zero-carry addition; it cannot be reconstructed from the incrementer carry alone. The design trades a second full adder block for increment logic and appropriate carry merging.

### 23. Derive the half-subtractor by weights

For one-bit A−B, derive difference and borrow and explain the sign in $a-b=d-2r$.

#### Solution

The four input cases produce $(d,r)=(0,0),(1,1),(1,0),(0,0)$ in order 00,01,10,11. Hence $d=a\oplus b$ and $r=\overline a b$. When a=0,b=1, retaining difference one needs a borrowed weight-two unit: $-1=1-2$. The carry of an adder and the borrow of a subtractor have different signs in their weighted identities. A circuit with difference XOR and borrow $a\overline b$ subtracts in the opposite direction.

### 24. Full-subtractor borrow recurrence

Derive a borrow predicate for $a-b-r_{in}=d-2r_{out}$ and compare it with adder carry.

#### Solution

Difference is $a\oplus b\oplus r_{in}$. Borrow occurs when $b+r_{in}>a$, giving $r_{out}=\overline a b\lor\overline a r_{in}\lor br_{in}$. Factoring gives $\overline a b\lor\overline{a\oplus b}r_{in}$. In equal-bit cases the incoming borrow propagates, whereas adder XOR carry propagates in unequal-bit cases. At a=b=1,r=1 the difference is one and borrow is one; this row is a useful guard against an incorrectly reused carry equation.

### 25. Complemented addition proves no-borrow polarity

For n-bit unsigned inputs, compute $A+\overline B+1$. Show that its carry is one exactly when A is at least B.

#### Solution

As unsigned values, $\overline B=2^n-1-B$, so the total is $A-B+2^n$. Its low word is $(A-B)\bmod2^n$. Its carry is one precisely when the total reaches $2^n$, equivalently A≥B. Thus borrow is the complement of carry. Equality gives carry one, not zero. A processor may store either carry or borrow as its status bit; instruction semantics must specify the polarity before multiword subtraction is designed.

### 26. A subtract-with-borrow input is not the same as carry one

Implement $A-B-r$ using one adder. Determine its incoming carry and demonstrate with A=B=3, r=1, n=4.

#### Solution

Use $A+\overline B+(1-r)$. With r=1 the incoming carry is zero. The example gives $3+12+0=15$, retained as $1111$, with carry zero and borrow one. Setting carry one would produce zero, computing A−B rather than A−B−1. The arithmetic identity is $A-B-r=S-2^n\overline{c_n}$ for the selected input carry. State the convention explicitly when chaining subtractors.

### 27. One XOR-controlled adder for addition and subtraction

Let each effective B bit be $b_i\oplus m$ and $c_0=m$. Prove the operations for m=0 and m=1, then explain what happens if only the XOR controls change.

#### Solution

For m=0, effective B is B and input carry is zero, so the circuit adds. For m=1, effective B is the bitwise complement and input carry is one, so the circuit subtracts modulo $2^n$. If m=1 but input carry remains zero, the circuit computes $A-B-1$. All XORs must receive the same operation control, and the carry input must follow it. A visually plausible bank of complement gates is not sufficient unless this final plus-one is accounted for.

### 28. Unsigned carry without signed overflow

Interpret four-bit $1111+0001$ both unsigned and signed. Give C, V, N and Z.

#### Solution

Unsigned, fifteen plus one is sixteen and exceeds the range 0–15, so C=1. Signed, −1+1=0 fits −8–7, so V=0. The retained word is $0000$, giving N=0 and Z=1. Opposite-sign addition cannot overflow in two's complement. The pair C=1,V=0 is therefore perfectly valid; it does not mean that one flag implementation is wrong.

### 29. Signed overflow without unsigned carry

Analyze four-bit $0111+0001$ and prove that C alone cannot detect signed overflow.

#### Solution

The unsigned total is eight, which fits four bits, so C=0. The signed operands are seven and one, but signed eight is outside −8–7. The retained word $1000$ represents −8, so V=1,N=1,Z=0. Carry into the sign column is one and carry out is zero; their XOR detects the overflow. This counterexample refutes the assertion V=C. The correct signed result is eight in a wider word, not −8.

### 30. Negative overflow and saturation

Compute four-bit $1010+1011$, interpret it signed, and give both wrapped and saturated signed outputs.

#### Solution

The unsigned total is twenty-one, so retained output is $0101$ and carry one. Signed, the inputs are −6 and −5; their mathematical sum is −11, outside −8–7. The wrapped signed result is +5 and V=1. Saturation must choose the lower bound $1000$ (−8), since the overflowed operands were both negative. Choosing $1111$ merely because carry is one would saturate to −1 and be incorrect.

### 31. Prove the sign-form overflow predicate

For ordinary addition with $c_0=0$, justify $V=\overline{a_{n-1}\oplus b_{n-1}}(a_{n-1}\oplus s_{n-1})$ from ranges.

#### Solution

Opposite-sign inputs have a sum between the two inputs and cannot exceed either signed bound. Two nonnegative inputs can exceed the upper bound only by reaching or crossing $2^{n-1}$, causing the retained sign to become one. Two negative inputs can cross the lower bound only when the wrapped sign becomes zero. Thus equal operand signs together with a different result sign are necessary and sufficient. The predicate does not say that every negative result indicates overflow; mixed signs are excluded.

### 32. Prove the carry-XOR overflow predicate

Using the sign-column full-adder equation, prove $V=c_{n-1}\oplus c_n$.

#### Solution

When the sign inputs differ, sign-column propagate is one and generate zero. Hence $c_n=c_{n-1}$ and overflow is zero. When both sign inputs are zero, $c_n=0$ and the result sign equals $c_{n-1}$, so overflow equals that incoming carry. When both are one, $c_n=1$ and the result sign again equals $c_{n-1}$; overflow occurs exactly when that result sign is zero. In all three cases the sign predicate equals carry XOR. The derivation also accommodates an additional input carry when the mathematical specification includes it.

### 33. A signed comparison that fails on the result sign

Use four-bit A=7 and B=−1. Evaluate A−B, and show why N alone gives the wrong less-than answer.

#### Solution

The exact difference is eight. The retained four-bit word is $1000$, so N=1. A naive test N=1 would claim 7<−1. Subtraction overflow is one because operands have different signs and the result sign differs from A. Therefore $N\oplus V=0$, correctly rejecting less-than. The zero flag is zero. For signed less-or-equal use $(N\oplus V)\lor Z$, not a carry test.

### 34. Same bit vectors, opposite comparison answers

Compare four-bit $1110$ and $0011$ as unsigned and signed values. Identify which interpretation uses borrow and which uses N XOR V.

#### Solution

Unsigned, fourteen is greater than three. The subtractor computes eleven, carry one and no borrow. Signed, −2 is less than three. The retained difference $1011$ represents −5 without overflow, so N XOR V is one. Both hardware interpretations use the same word subtraction but read different predicates. An unspecified comparison type makes the problem ambiguous; signedness belongs in the circuit contract.

### 35. Sign extension before versus after addition

Compare adding four-bit signed 7 and 3 after extending to five bits with extending their four-bit sum afterward.

#### Solution

Extending operands gives $00111+00011=01010$, the exact signed ten. Adding first at width four gives $1010$, a wrapped value of −6. Sign-extending that result yields $11010$, still −6. Extension preserves the interpreted input value; it does not recover bits already lost by a narrower overflowing operation. The order of width conversion is part of the algorithm, not merely formatting.

### 36. Unsigned and signed saturation selectors

Give formulas for n-bit unsigned saturation and signed saturation, and specify the control needed for the signed bound.

#### Solution

Unsigned saturation selects the ordinary sum when C=0 and all ones when C=1. Signed saturation selects the ordinary sum when V=0. When V=1, use the original common operand sign: sign zero selects a zero sign bit followed by n−1 ones, while sign one selects a one sign bit followed by n−1 zeros. N after overflow has the opposite direction and must not be used without inversion. The bounds follow from two's-complement encoding; for n=4 they are seven and −8.

### 37. Fixed-point addition and a scale mismatch

Two four-bit signed integers encode real values at scale $2^{-2}$. Compute $0101+0010$. Why is adding a value encoded at scale $2^{-1}$ directly invalid?

#### Solution

The inputs represent 1.25 and 0.5. Integer addition gives $0111$, representing 1.75 at the same scale and within the signed range. A second encoding scale changes the positional weight of every bit; equal bit positions would no longer represent equal real increments. Align binary points before addition, retaining enough fractional and integer bits. Shifting may introduce rounding or lose range. The adder cannot infer the intended physical scale from the bit vectors.

### 38. Derive a two-bit unsigned comparator

For A=$a_1a_0$ and B=$b_1b_0$, derive equality and strict less-than using the first differing bit.

#### Solution

Equality is $\overline{a_1\oplus b_1}\,\overline{a_0\oplus b_0}$. Less-than is $\overline a_1b_1\lor\overline{a_1\oplus b_1}\,\overline a_0b_0$. The first term decides when the high bits differ; the second is enabled only when they match. Since a differing high bit has weight two and the lower bit can change the value by at most one, the high difference dominates. This is the comparator argument underlying ETH's K-map exercise, reconstructed in consistent indexed notation.

### 39. A comparator composition resembles a carry composition

A higher group supplies equality E_H and greater-than G_H; a lower group supplies E_L and G_L. Derive the combined pair and prove that both greater and less cannot be true.

#### Solution

Combined equality is $E_HE_L$. Combined greater-than is $G_H\lor E_HG_L$. Higher unequal bits decide immediately; lower bits matter only under equality of the high group. This ordered composition is associative for the same functional reason as carry composition. For any fully specified binary words exactly one of less, equal and greater holds. A circuit yielding greater and less simultaneously violates its specification, although indeterminate HDL values require a separately stated four-state policy.

### 40. Equality detector size and depth

Construct an n-bit equality detector from two-input gates. State a simple component count and a balanced depth bound.

#### Solution

Form n XNOR terms and AND all of them. This uses n XNOR gates and n−1 two-input AND gates for n≥1. A balanced AND tree has depth $\lceil\log_2 n\rceil$ after the XNOR layer. A serial AND chain instead has n−1 AND levels. The output can also be NOT of the OR of all XOR differences; gate-library choices may change area and delay. For n=1 the AND stage is absent, a useful boundary case.

### 41. BCD addition with no binary carry but decimal carry

Add valid BCD digits 7 and 5 with no incoming decimal carry. Compute the initial binary sum, correction predicate, final digit and decimal carry.

#### Solution

The initial sum is twelve, represented by k=0 and z=$1100$. Because $z_3z_2=1$, correction q is one. Add $0110$ to z: eighteen gives low digit $0010$, which is two. The decimal carry is q=1, so the result is decimal twelve. The initial binary carry k was zero. A detector that corrects only when k=1 fails for every total ten through fifteen.

### 42. BCD totals sixteen through nineteen

Evaluate 9+9+1 and explain why the carry from the correction adder alone is not the decimal carry.

#### Solution

The total is nineteen, so the first adder outputs k=1,z=$0011$. q=1 because k=1. Adding six to z gives $1001$ with correction-adder carry zero. The correct decimal result is carry one and digit nine. Therefore decimal carry must be q, or an equivalent properly merged condition, rather than only the second adder's carry. The first addition already supplied the carry in this range.

### 43. Derive the BCD correction detector

Prove $q=k\lor z_3z_2\lor z_3z_1$ for valid input digits and a binary carry input. Why is $z_3$ alone insufficient?

#### Solution

Valid total range is 0–19. For totals sixteen through nineteen, k=1. Among totals zero through fifteen, invalid digits ten through fifteen have z3=1 and at least one of z2,z1 equal to one; eight and nine have both these bits zero. Thus the predicate identifies precisely total≥10. A detector z3 would incorrectly correct eight and nine. z0 is irrelevant to this threshold because adjacent even/odd codes cross no new threshold inside either accepted or rejected pair.

### 44. Invalid BCD inputs defeat the decimal assumption

Feed $1111$ and $1111$ into a digit adder designed for valid BCD. Apply the correction formula and explain why the output is not a specification for decimal addition.

#### Solution

Binary total thirty has k=1,z=$1110$. Correction gives low output $0100$ and q=1. Reading this as decimal fourteen does not correspond to the binary total thirty or to addition of valid single decimal digits; fifteen is not a decimal digit. The formula's proof assumed inputs at most nine. A circuit may specify invalid-code detection, a fail-safe output, or don't-cares under an enforced input contract. It may not infer validity merely because the final nibble looks valid.

### 45. Two-digit BCD addition with a chain of corrections

Add decimal 59 and 73 using two BCD digit adders. Show the carries and state whether two digits suffice.

#### Solution

Units: 9+3=12, so output digit is two and carry one. Tens: 5+7+1=13, so output digit is three and carry one. The retained two-digit result is 32, with a hundreds carry one: exact result 132. Dropping the final carry computes decimal modulo one hundred. Each decimal carry is one bit, but its place weight is ten times the preceding digit, not twice it.

### 46. Carry-save arithmetic with a width trap

Compress four-bit X=15,Y=15,Z=15 into an unshifted sum row S and carry row C. Find both and the required width of the final result.

#### Solution

Every column has three ones, so S=$1111$ and C=$1111$. The integer identity is $15+15+15=15+2\cdot15=45$. C shifted left occupies five bits; adding it to S requires a six-bit exact result because three maximum four-bit operands can exceed thirty-one. Truncating shifted C to four bits would give fifteen plus fourteen, losing sixteen. A compressor stage is local arithmetic; output width must still be derived globally.

### 47. Count compressor stages correctly

Why is a carry-save stage independent of n in logical depth, while a complete sum of three n-bit operands is not?

#### Solution

Each bit column receives only its three equal-weight operand bits; no carry generated by another column is needed to compute its sum or carry. Therefore columns operate in parallel with constant full-adder depth. The two output rows still require a carry-propagate adder to produce one ordinary binary word. Its depth depends on the selected ripple or prefix architecture. Calling the whole operation constant-time confuses compression with final addition.

### 48. Three operands versus two serial adders

Compare a three-operand sum using two ripple adders with a carry-save stage followed by one ripple adder, under explicit delays $D_R(n)$ and $D_F$.

#### Solution

Two serial ripple additions require approximately $2D_R(n)$, with proper extra widths included. The compressor alternative requires $D_F+D_R(n+1)$ if the second row needs n+1 positions; the exact final width may be n+2. For large n the removed first carry chain is the main benefit. Area and routing are separate costs; compression does not prove fewer gates. Numerical conclusions require the width-aware gate timing model rather than reusing one nominal n-bit delay twice.

### 49. Partial-product count and maximum product width

For an unsigned n×n multiplier, count AND partial products and prove that 2n bits always suffice. Does every product actually need all 2n bits?

#### Solution

Each pair $(a_i,b_j)$ contributes one AND product of weight $2^{i+j}$, giving $n^2$ products. The maximum result is $(2^n-1)^2<2^{2n}$, so 2n bits suffice. Some products need fewer bits: zero needs only a zero encoding, and one times one needs one significant bit. A fixed-width multiplier reserves the maximum output width regardless of the current values. For n=1 the maximum is one, so the top of its conventional two-bit output is always zero.

### 50. Exact rows for a four-bit multiplication

Multiply unsigned $1011$ by $1101$ using shifted rows and give the eight-bit result.

#### Solution

The multiplier bits from low to high are 1,0,1,1. The rows are eleven, zero, forty-four and eighty-eight. Their sum is 143, or $10001111$. The row shifts encode weights; writing all nonzero rows without shifting would give thirty-three. A carry-save tree may add these rows in a different order, but its final integer total must remain 143. The corresponding lesson model displays each row's contribution and the accumulated exact value.

### 51. Signed multiplication is not an unsigned reinterpretation

Multiply four-bit $1101$ by $0101$ as signed values. Compare the correct eight-bit output with the unsigned multiplication of the same vectors.

#### Solution

Signed inputs are −3 and five, so their product is −15. Eight-bit two's complement is $11110001$, obtained by adding 256 to −15. Unsigned multiplication interprets thirteen times five, giving 65 or $01000001$. Merely labeling the unsigned output “signed” does not fix the partial products. The sign bit contributes a negative positional weight and must be treated accordingly, or operands must be converted to correctly widened magnitudes.

### 52. The minimum negative magnitude needs special care

Explain why negating four-bit signed $1000$ at width four cannot produce a positive magnitude. Give a safe magnitude width for a signed multiplier implementation.

#### Solution

The input is −8. Bitwise complement plus one wraps back to $1000$ because positive eight is outside the four-bit signed range. Widening to five bits gives $11000$; negation yields $01000$, the positive magnitude eight. Alternatively treat the n-bit magnitude as unsigned, with a carefully specified conditional negation. A signed temporary that must represent both $-2^{n-1}$ and its positive magnitude needs n+1 bits. This boundary affects Booth subtraction and division preprocessing too.

### 53. Derive radix-two Booth recoding

Let $b_{-1}=0$ and define $d_i=b_{i-1}-b_i$. Prove that the signed multiplier equals $\sum_{i=0}^{n-1}d_i2^i$.

#### Solution

Expand the sum into $\sum b_{i-1}2^i-\sum b_i2^i$, where both sums run from i=0 to n−1. Reindex the first sum as $\sum_{j=0}^{n-2}b_j2^{j+1}$. Subtracting gives $\sum_{j=0}^{n-2}b_j2^j-b_{n-1}2^{n-1}$, exactly the two's-complement value. Pairs 01 produce +1, pairs 10 produce −1, and equal pairs produce zero when the pair is written $(b_i,b_{i-1})$. State this ordering: reversing the pair silently reverses the operation sign.

### 54. Booth recoding of a run of ones

Recode six-bit positive $011110$ and explain the reduction in nonzero partial rows.

#### Solution

Its value is thirty. The low zero gives d0=0; at i=1 the transition from zero to one gives d1=−1. Equal ones give zero until i=5, where the transition from one to the top zero gives d5=+1. Thus $30=2^5-2^1$. Ordinary unsigned rows have four nonzero contributions; Booth has two. A bit pattern with frequent transitions need not gain this reduction. Sparse recoding lowers additions for this input but does not by itself guarantee faster fixed hardware.

### 55. Signed product range and overflow narrowing

Why does a product of two n-bit signed inputs fit 2n bits? Determine whether four-bit −8 times −8 fits an eight-bit signed word and a seven-bit signed word.

#### Solution

The largest positive product is $2^{2n-2}$, from both minimum negative inputs. The most negative attainable product has magnitude at most $2^{n-1}(2^{n-1}-1)$. Both fit the 2n-bit signed range. For n=4, −8 times −8 is 64, which fits −128–127 but exceeds the seven-bit upper bound 63. Discarding a leading zero would change the sign. To narrow a signed result safely, all discarded bits must match the retained sign bit, not merely be zero.

### 56. Derive the prefix division invariant

In unsigned restoring-style long division, let the processed dividend prefix be P=DQ+R with $0\le R<D$. Derive the update for next bit x.

#### Solution

The new prefix is $2P+x=D(2Q)+(2R+x)$. Put U=$2R+x$. Since R<D and x≤1, U<2D. Therefore the next quotient bit q is one exactly when U≥D. Set $Q'=2Q+q$ and $R'=U-qD$. These equations preserve $P'=DQ'+R'$ and ensure $0\le R'<D$. One subtraction suffices precisely because U is below 2D. This derivation supplies both the algorithm and its proof.

### 57. Trace a division with leading zeros

Divide six-bit $101101$ by unsigned $0101$. List the trial remainders, quotient bits and final result.

#### Solution

Process bits 1,0,1,1,0,1. Starting R=0, trial values U are 1,2,5,1,2,5. Subtract five only on trials three and six. Quotient bits are 0,0,1,0,0,1, giving nine. Final R=0, so $45=5\cdot9+0$. Quotient leading zeros are part of the fixed-width trace. A model that skips them must still state its equivalent initialization rather than changing the invariant.

### 58. Trial remainder width and division by zero

For a k-bit positive divisor, derive the trial-remainder width. Explain why the same algorithm cannot simply run with D=0.

#### Solution

R is at most D−1 and D at most $2^k-1$, so U=$2R+x$ can approach $2^{k+1}-3$. Thus k+1 bits may be required for the trial and subtraction comparison, even though the final remainder fits k bits. With D=0 the invariant $0\le R<D$ is impossible and the quotient has no ordinary mathematical definition. A divider must reject zero or expose an explicitly specified exception status before starting its normal trace.

### 59. Signed division overflow at a unique boundary

Under truncation toward zero, analyze n-bit minimum negative divided by −1, and describe the sign of a nonzero remainder for other inputs.

#### Solution

The exact quotient is $2^{n-1}$, outside the n-bit signed range, so this case overflows. It cannot be repaired by merely changing the quotient sign bit. For ordinary nonexceptional inputs, divide magnitudes, apply the XOR of operand signs to the quotient, and apply the dividend sign to the remainder. Then A=DQ+R holds with $|R|<|D|$. Rounding toward negative infinity is a different specification and has a different remainder convention. The laboratory implements unsigned division only, to avoid conflating these policies.

### 60. A two-limb addition and its flags

Add hexadecimal 0x7FFF and 0x0001 using two eight-bit limbs. Show the low carry, high result and final 16-bit signed overflow.

#### Solution

Low limb: 0xFF+0x01=0x100, producing zero and carry one. High limb: 0x7F+0x00+1=0x80, with final unsigned carry zero. Combined output is 0x8000. Signed total 32768 exceeds the 16-bit upper bound, so V=1. The high-limb overflow computation must include the propagated carry. Zero for the complete word is the AND of both limb-zero predicates; the low zero alone does not mean that the result is zero.

### 61. A two-limb subtract-with-borrow chain

Compute 0x1000−0x0001 with eight-bit limbs using the no-borrow carry convention.

#### Solution

Low subtraction 0x00−0x01 gives 0xFF with carry zero, indicating a borrow. High computation is 0x10−0x00−1=0x0F. It can be implemented as $0x10+\overline{0x00}+0$, because the low no-borrow carry is zero. Final word is 0x0FFF and final carry one, meaning no whole-word unsigned borrow. Supplying a constant plus-one to every limb would ignore the low borrow and yield 0x10FF, which is wrong by 256.

### 62. Control signals versus live status signals

A combinational ALU's mode selects add or subtract; a stored carry flag participates in add-with-carry. Explain why connecting the ALU's carry output directly back to its input is generally invalid.

#### Solution

The flag must be the previously stored architectural state, sampled before the new operation. Direct output feedback creates a combinational cycle, violating the acyclic timing model and potentially producing ambiguous or unstable values. A register breaks the cycle and updates only when the instruction enables flag writing. Different instructions may preserve flags or alter only selected flags. The arithmetic chapter defines the datapath; controller timing and register update belong to the sequential chapter. Berkeley's processor exercise motivates this reconstruction.

### 63. Width-safe HDL addition

Explain why an explicit widened sum is preferable to relying on an implicit language expression width when exposing carry. Give the arithmetic specification for the widened result.

#### Solution

Use an n+1-bit temporary and explicitly zero-extend both unsigned operands before adding the input carry. Its integer value is $A+B+c_0$, bounded by $2^{n+1}-1$. Retain low n bits as sum and the top bit as carry. HDL expression sizing and signedness rules can cause a narrower intermediate even when the destination is wider, depending on context and language constructs. Explicit extensions make intent reviewable. Functional algebra does not replace compilation and synthesis checks for a particular toolchain.

### 64. Overflow detection by widening

For signed n-bit addition, explain an independent overflow check using an n+1-bit exact sum and show why merely checking its top bit is wrong.

#### Solution

Sign-extend both operands to n+1 bits and add there. The exact result fits this width. Narrowing back to n bits is safe precisely when the two top bits of the widened result match, because discarded sign extension must agree with the retained sign. Their XOR is the overflow predicate. The top bit alone is just the sign of the exact result: a negative but valid result has top bit one without overflow. This supplies an independent reference check for a carry-based implementation.

### 65. End-around carry is a different number system

For four-bit one's-complement arithmetic, compute the raw addition $1110+0010$ and apply end-around carry. Contrast with two's complement.

#### Solution

Raw unsigned total is sixteen: low word zero and carry one. One's-complement arithmetic adds that carry back into the low word, producing $0001$. In one's complement, $1110$ is −1 and $0010$ is +2, so +1 is correct. In two's complement, $1110$ is −2 and the exact result is zero; adding the carry back would be wrong. End-around carry implements modulo $2^n-1$ with two zero encodings, not the usual modulo $2^n$ word arithmetic.

### 66. A sign-magnitude adder requires comparison

Derive the two cases for adding sign-magnitude numbers. Why does an ordinary two's-complement adder not implement them directly?

#### Solution

Equal signs require adding magnitudes and retaining the common sign, with a magnitude-overflow policy. Opposite signs require subtracting the smaller magnitude from the larger and taking the larger magnitude's sign; equal magnitudes require a canonical zero policy. A sign bit in this encoding is not a negative positional weight of $2^{n-1}$, so ordinary two's-complement arithmetic interprets it incorrectly. The opposite-sign case needs magnitude comparison or equivalent borrow information and conditional magnitude/sign selection. This reconstructs Stanford's sign-magnitude design exercise with its representation made explicit.

### 67. All sums are not simultaneously on the longest path

In the unit-gate ripple model, why is $s_0$ ready much earlier than $s_{n-1}$? Can the latest carry bound be assigned to every output?

#### Solution

Sum zero depends only on p0 and external c0, so it has two gate delays when all inputs arrive at zero. A higher sum depends on a carry formed by preceding columns. Each output has its own dependency graph and arrival bound. The final carry may be the latest output, but assigning its arrival time to every sum overstates their paths and conceals opportunities for pipelining or early local use. A circuit's overall settling bound is the maximum of the individual output bounds, not an assertion that every output settles then.

### 68. Carry pair validity with XOR versus OR propagate

Under XOR propagate, which (G,P) pair is impossible for a single bit? Can an ordered group of such bits produce that pair? What changes under OR propagate?

#### Solution

The pair (1,1) is impossible at one bit because generate requires both bits one, while XOR propagate requires them unequal. A group with P=1 has every bit propagating, hence no generate in any column and G=0. Thus the pair remains impossible for groups. Under OR propagate, a column with both bits one has (1,1), and groups may too. Both encodings still represent the same carry function in that state, constant one, but signal exclusivity arguments must use the actual convention.

### 69. Complementing a signed comparison's sign bits

Prove that signed order can be converted to unsigned order by XORing the most significant bit of both operands with one.

#### Solution

Let unsigned encoding A have sign bit a. Its signed value is $A-a2^n$. Flipping its sign bit yields unsigned $A+(1-2a)2^{n-1}=A_s+2^{n-1}$. This adds the same constant to every signed value, mapping the signed interval monotonically onto 0 through $2^n-1$. Comparing transformed unsigned words therefore gives exactly signed order. The transformation is on both operands before comparison; flipping only the subtraction result does not implement the same mapping.

### 70. Is a prefix carry tree a timing simulation?

A teaching model reveals group nodes level by level. Can its visible order establish propagation time, glitches or metastability? State what it does establish.

#### Solution

The stored sequence establishes algebraic dependencies and the exact Boolean carry functions after each selected composition. It does not include inertial/transport delays, load capacitance, rise/fall asymmetry or asynchronous sampling. Consequently it cannot certify nanosecond delay, hazard freedom or metastability behavior. A separate delay model can annotate path bounds, and a transistor or event-driven simulator can address additional physical questions. Animation accuracy means consistency with its stated mathematical model, not silently extending that model's scope.

### 71. Recover an unknown input from sum and carry

A one-bit full adder has a=1, sum=0 and outgoing carry=1. Find every possible pair (b,c). Explain the information loss.

#### Solution

The weighted identity gives $1+b+c=0+2$, hence b+c=1. The possible pairs are (0,1) and (1,0). The adder records population count but does not preserve input order, so it cannot distinguish which of those inputs was one. If sum=1 and carry=1, the count would be three and b=c=1 uniquely. Solving the weighted equation is often simpler than reverse-searching a memorized truth table.

### 72. Unknown operand constraints in an overflow question

For four-bit signed addition A=5, find every signed B that causes positive overflow, and determine whether any negative overflow is possible.

#### Solution

The exact sum exceeds seven when B>2. Since B lies in −8 through seven, the overflowing values are 3,4,5,6,7. All are nonnegative, matching the equal-sign condition. The minimum possible sum is 5−8=−3, so negative overflow cannot occur. The interval method proves completeness; checking a handful of binary examples would not establish all values. Unsigned carry depends on B's encoding and answers a different question.

### 73. Minimum output width of a sum of many words

Find the exact unsigned output width for k independent n-bit operands, including k=1. Give a simple sufficient bound and explain when it is loose.

#### Solution

The maximum total is $M=k(2^n-1)$. For M>0 the exact width is $\lfloor\log_2M\rfloor+1$, equivalently $\lceil\log_2(M+1)\rceil$. The sufficient bound $n+\lceil\log_2k\rceil$ follows from $M<k2^n$. It can be loose, for example n=1,k=3 needs two bits, whereas the sufficient bound gives three. For k=1 the exact width is n. Compressor trees do not alter this numerical range requirement.

### 74. A safe zero detector for a multioperand compressor

Can an all-zero sum row S establish that X+Y+Z is zero? Give a counterexample and an exact zero test.

#### Solution

At one column take two ones and a zero. Parity gives S=0 but carry gives C=1, representing value two. Thus S=0 alone is insufficient. With nonnegative operands, the complete compressed integer is $S+2C$; it is zero precisely when both S and C are zero. If the specification instead observes a truncated modulo word, a nonzero high carry may be discarded and zero has a different condition. Flags must be derived for the final represented result and its width.

### 75. Multiplication overflow from high-half tests

State the correct test for narrowing a 2n-bit unsigned product to n bits, then show why the same test is wrong for signed multiplication.

#### Solution

Unsigned narrowing is safe exactly when every discarded high bit is zero. Signed narrowing is safe exactly when every discarded bit equals the retained sign bit. For four-bit −2 times one, the eight-bit product is $11111110$. Its high half is nonzero but its low four bits $1110$ correctly represent −2; sign-extension equality proves no signed overflow. Conversely the positive product eight has a zero high half but low word $1000$ is negative, so it overflows the signed four-bit range.

### 76. Compare equality from subtraction versus XNOR

Prove that the retained difference is zero exactly when equal-width unsigned bit vectors A and B are equal. Does signed overflow change this conclusion?

#### Solution

The retained difference is $(A-B)\bmod2^n$. Since A−B lies between $-(2^n-1)$ and $2^n-1$, the only multiple of $2^n$ in that interval is zero. Thus zero difference implies A=B and the converse is immediate. The same encodings are equal as signed values exactly when their bit vectors are equal. Signed overflow can corrupt ordering predicates but cannot produce a false zero difference within this equal-width operand range.

### 77. Correct a flawed BCD carry connection

A digit circuit outputs corrected low nibble but defines its decimal carry as the second adder's carry. Find two input totals that expose the flaw and derive a repair.

#### Solution

For total twelve, z=12 and adding six gives eighteen; the second carry is one, so the flawed circuit appears correct. For total nineteen, the initial carry is one and z=3; adding six gives nine with second carry zero, so it fails. Decimal carry q from the threshold detector is correct throughout 0–19. Equivalently OR the initial carry with the correction carry under this valid-input contract. The repair must be accompanied by a proof over both ranges rather than one successful example.

### 78. Reconstruct an arithmetic black box from its identities

A circuit satisfies $F_1=x\oplus y$ and $F_2=\overline xy$. Decide whether it is a half adder, half subtractor, or unsigned comparator, and state the qualification.

#### Solution

It implements a half subtractor with difference F1 and borrow F2, since $x-y=F_1-2F_2$. F2 alone also represents one-bit x<y, but F1 is inequality, not equality. A half adder would use xy as carry. The output functions, their assigned weights and the operation contract together identify the circuit. This original problem prepares the NAND-network reasoning of the authenticated doctoral bridge without relying on the shape of the schematic alone.

### 79. Prove the final ripple carry from a threshold

For n-bit addition with input carry c, show that outgoing carry is one exactly when $A\ge2^n-B-c$. Discuss the threshold when B=c=0.

#### Solution

Outgoing carry is the high bit of A+B+c, hence is one precisely when that total is at least $2^n$. Rearranging gives the stated threshold. When B=c=0 the threshold is $2^n$, which no valid A reaches, so carry is always zero. When B=$2^n-1$ and c=1 the threshold is zero, so carry is always one. Treating the threshold modulo $2^n$ would turn the first boundary into zero and reverse its answer; threshold algebra uses exact integers.

### 80. An integrated width, flags and comparison audit

For four-bit A=$1000$, B=$0001$, compute addition and subtraction. Give signed exact values, retained values, C/V/N/Z, and signed versus unsigned less-than.

#### Solution

Addition: unsigned total nine gives S=$1001$, C=0,N=1,Z=0. Signed −8+1=−7 fits, so V=0. Subtraction: unsigned eight minus one gives S=$0111$, C=1 (no borrow), N=0,Z=0. Signed −8−1=−9 overflows, so V=1. Signed less-than from subtraction is N XOR V=1, correctly −8<1. Unsigned less-than is borrow=0, correctly eight is not less than one. The same four-bit datapath supports both interpretations only when its output predicates are selected consistently.
