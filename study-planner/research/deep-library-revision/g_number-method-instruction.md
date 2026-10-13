## Constructing solutions when representation constraints are combined

This section joins the chapter's individual definitions into reusable derivations. It also supplies the small normal-floating and byte-order bridge required by the retained question bank. Full floating exception handling and language object representation remain separate later topics. These explanations and examples are independently authored, with the four complementary written course bodies identified in the source audit.

### Construction 1. Representability comes before a decoding shortcut

For an unsigned width $w$, the interval is $[0,2^w-1]$. For two's complement it is $[-2^{w-1},2^{w-1}-1]$. The endpoints determine whether an intended integer can be encoded exactly. A bit pattern always has a decoder value, but that does not imply that an attempted arithmetic result has that value.

To choose the smallest two's-complement width for an integer interval $[L,H]$, test both inequalities
$$-2^{w-1}\le L,\qquad H\le2^{w-1}-1.$$
For $[-128,128]$, eight bits satisfy the lower endpoint and fail the upper endpoint; nine bits are necessary. A freely assigned code for these257 labels needs nine bits as well, but the reason is capacity rather than the signed weighting rule. For $[0,127]$, freely assigned or unsigned encoding needs seven bits, while two's complement needs eight. Never replace a representation requirement by a count of labels without checking the declared decoder.

If a source informally says sign-magnitude loses a bit, quantify the intended comparison. It has $2^w$ stored words and $2^w-1$ distinct integers because two words decode as zero. Its nonnegative maximum is smaller than an unsigned format's maximum, but that is a redistribution of range, not the disappearance of half the available bit patterns.

### Construction 2. Conversion algorithms need equality and zero cases

In greedy integer conversion, select the largest place weight that is **less than or equal to** the current residual. At residual eight, weight eight must be used; a strict less-than rule would begin at four and can require an illegal coefficient two. After writing a digit, reduce the residual by its weighted contribution and continue through every lower place. If the residual becomes zero early, write zeros into all remaining positions. Otherwise a correct partial sum can leave the output representation incomplete.

For repeated division, the invariant after $k$ extracted digits is
$$N=q_kb^k+\sum_{j=0}^{k-1}r_jb^j,\qquad0\le r_j<b.$$
The quotient decreases when positive. Reverse the extracted remainders; do not omit zero remainders. The input zero is handled explicitly as numeral0. These details reconcile the intuitive place-weight method with a complete executable algorithm.

For a reduced fraction $p/q$, termination requires $q\mid b^f$. For repetition, track **integer** remainder states under $r\mapsto br\bmod q$. In base two, $1/10$ starts with a one-digit nonrepeating prefix and a four-digit repeating block. The fact that its denominator contains five predicts nontermination; the repeated remainder identifies the actual period. A floating residual that happens to become zero is not a proof of rational termination.

### Construction 3. Make quantization an integer quotient-and-remainder decision

Let $x$ be the exact real value and let the target spacing be $\Delta=2^{-f}$. The ideal raw index is $z=x/\Delta$. Write
$$z=q+r,\qquad q=\lfloor z\rfloor,\quad0\le r<1.$$
Nearest rounding chooses $q$ for $r<1/2$ and $q+1$ for $r>1/2$. At equality, nearest-even chooses whichever integer index is even. This works for negative $z$ too: $-7.5=-8+0.5$, so the even neighbor is $-8$. Truncation toward zero instead chooses $-7$.

When rescaling an exact integer product $P$ by a positive integer divisor $D$, use Euclidean division $P=qD+r$ with $0\le r<D$. Compare $2r$ to $D$ and apply parity only if equal. A signed programming language's remainder can be negative, so first convert to this declared floor/remainder convention or use a separately proved signed algorithm. This derivation avoids fragile offset formulas and identifies ties exactly.

### Construction 4. A normal floating grid has explicit scope

A declared normal format with $p$ significant binary bits, including the leading one, has significands $1+j2^{-(p-1)}$. At exponent $e$,
$$x_j=2^e+j2^{e-(p-1)},\qquad\Delta_e=2^{e-p+1}.$$
The bias decodes the exponent field; it does not supply the fraction precision. For $p=5$ and $e=5$, local spacing is2. The predecessor just below32 belongs to the previous binade and is31, while the successor is34. Distances on opposite sides of a power-of-two boundary need not match.

For a stored exponent $E$ with bias $K$, normal decoding is $e=E-K$. The leading-bit rule applies only to normal fields. Reserved fields, exponent overflow and subnormals need declared separate rules. The retained bank uses explicitly specified miniature formats or decimal normalized arithmetic, so it does not require assuming that a host `float` has any particular format.

In a decimal format with five significant digits, an addition node rounds at the exponent of its current result. To analyze an expression tree, carry each rounded node into the next operation. An exact final sum with one final rounding is a different computation. The authentic associativity example illustrates this with two branch-specific tables.

For a specifically declared IEEE-style binary format with minimum normal exponent $e_{\min}$ and $p$ significant bits, subnormals use significand $j2^{-(p-1)}$ instead of $1+j2^{-(p-1)}$, at the fixed exponent $e_{\min}$. Their spacing is $2^{e_{\min}-p+1}$. This convention is conditional; a custom format may assign reserved fields differently. Under nearest-even, if a retained significand's discarded tail has guard bit $G$, following round bit $R$, and sticky bit $S$ equal to the OR of all further discarded bits, increment the retained integer exactly when $G=1$ and either $R\lor S=1$ or its low retained bit is1. At $G=1,R=S=0$ the tail is an exact tie and retained parity decides. If incrementing carries past the leading significand position, renormalize and check the new exponent range. These rules explain the retained boundary notes without assuming that every custom format or C implementation adopts IEEE special-field semantics.

### Construction 5. Distinguish word significance from address order

For four eight-bit bytes, a word decomposes as $W=b_3 256^3+b_2 256^2+b_1 256+b_0$. Little-endian storage orders the bytes $b_0,b_1,b_2,b_3$ at increasing addresses; big-endian orders them oppositely. Matching decoders recover the same $W$. Neither rule reverses bits inside each byte. A hex numeral does not itself reveal a memory layout. A later programming chapter covers object-access and implementation requirements; this mathematical bridge supplies only the declared storage contract needed for the retained question.

### Construction 6. BCD and Gray need their own invariants

For BCD addition, each digit subtotal $t$ includes its incoming **decimal** carry and lies between0 and19. If $t\ge10$, adding6 produces $16+(t-10)$. Correction is required when the initial binary carry is one **or** the retained nibble exceeds9. Keep the decimal carry when correcting a subtotal16 through19; its retained low nibble can look legal before correction. The invariant across digit stages is that processed low decimal digits and the outgoing decimal carry represent the exact processed subtotal.

For reflected Gray decoding, the invariant is that each reconstructed binary bit is the XOR of the Gray prefix down to that position. Gray adjacency compares **consecutive indices** in the declared ordering. For example, indices7 and8 have Gray words0100 and1100, differing once even though their natural binary words differ four times. Skipping an index can change more than one Gray track. A Gray word's unsigned value is not its numerical index, and a one-bit-adjacency code is not an error-detecting codebook.

### Construction 7. Syndrome is an observation before it is a correction command

For the stated Hamming(7,4) placement, a single error at position $j$ contributes binary index $j$ to the syndrome. Two errors at distinct positions $i,j$ contribute $i\oplus j$, which can equal a third position. Thus a nonzero syndrome does not establish that a single error occurred. Extended overall parity adds another observation: with at most two errors, odd overall parity plus nonzero syndrome identifies a single error in the seven-position part; even overall parity plus nonzero syndrome identifies a double error and forbids single-bit correction. The error bound is part of the decoder's theorem.

## Ten solved transfer challenges across the chapter

These original medium-to-hard problems combine constraints, require explicit numerical derivations, and extend the retained tutorials. They are not verbatim university or entrance-examination questions.

### Transfer 1. Simultaneous radix equations can have no legal solution

**Question.** Find all integer radices $b$ satisfying both $23_b=19_{10}$ and $(13_b)^2=169_b$. Every written digit must be legal. Which condition prevents a solution?

**Solution.** The first equation expands to $2b+3=19$, forcing $b=8$. Its own digits are legal in that base. The second expands to $(b+3)^2=b^2+6b+9$, an algebraic identity; it does not force another numerical root. Its digit9 instead requires $b\ge10$. Consequently the legal solution sets are $\{8\}$ and the integers at least10, whose intersection is empty. Saying that the second equation is an identity and hence imposes no condition would miss digit legality. Conversely, attempting to find a unique root of that identity would add a condition the arithmetic does not contain. Solve each numerical relation and each notation constraint, then intersect the admissible sets. If the rightmost digit in the second equation were changed, both the polynomial identity and the legal-domain analysis would have to be repeated.

### Transfer 2. A shortest finite expansion and an exact repeating expansion

**Question.** Determine the shortest finite base-six expansion of $5/72$. Then find the preperiod and a repeating block in binary. Prove both results.

**Solution.** The fraction is reduced, $72=2^3\cdot3^2$, and $6=2\cdot3$. A finite base-six length $f$ must satisfy $f\ge3$ and $f\ge2$, so its minimum is3. Scaling gives $(5/72)6^3=15=23_6$; the three required fractional positions therefore give $0.023_6$. Check that $2/36+3/216=15/216=5/72$. Dropping the leading fractional zero would change the value.

In binary, remove the power-of-two factor by shifting three fractional positions: $8(5/72)=5/9$. The first three fractional digits are000, and the remaining fraction is $5/9$. The order of2 modulo9 is6: successive residues are2,4,8,7,5,1 and no earlier residue is1. Thus the repeating tail has period6. Its block value is $(5/9)(2^6-1)=35$, binary100011 at width6. Hence the expansion is a three-zero prefix followed by repeating100011. The exact reconstruction is $2^{-3}(35/63)=5/72$. The reduced denominator's factor $2^3$ forces a preperiod of at least3, while the coprime factor9 determines the eventual period. A finite decimal or base-six expansion does not imply a finite binary expansion.

### Transfer 3. End-around carry reaches a negative endpoint and a signed zero

**Question.** In five-bit ones' complement, add $-9$ and $-6$, then add $+15$ to the corrected result. Give every intermediate word and explain the zero convention.

**Solution.** The modulus for complement arithmetic is31. Codes for $-9$ and $-6$ are $31-9=22$, word10110, and $31-6=25$, word11001. Their unsigned sum47 is `1 01111`. The initial low word01111 would decode as $+15$, not the desired $-15$. Adding the outgoing carry back gives unsigned16, word10000; its ones'-complement decoder is $16-31=-15$, exactly the negative endpoint. This result fits the five-bit range $[-15,15]$.

Adding positive15, word01111, then gives10000+01111=11111 with no carry. That is the negative-zero word, decoded as $31-31=0$. The numerical sum is zero, but its bit pattern differs from positive zero00000. If a system requires canonical positive zero, an explicit postprocessing conversion can choose00000; it is a representation convention rather than another arithmetic value. The example exposes why merely dropping the first carry is wrong, why a leading one need not denote a strictly negative integer in ones' complement, and why mathematical cancellation alone does not specify a unique zero word in a redundant encoding.

### Transfer 4. Three width pipelines give three different results

**Question.** Starting with positive signed values90 and90, compare: add in sixteen bits; add in eight bits then sign-extend; narrow each operand to four low bits, add in four bits, then sign-extend. All operations here are explicitly modular hardware operations followed by two's-complement decoding.

**Solution.** The sixteen-bit path represents $90+90=180$ exactly. The eight-bit path stores unsigned180, word10110100, which decodes as $180-256=-76$; subsequent sign extension preserves $-76$. The four-bit input narrowing keeps $90\bmod16=10$, word1010, decoded as $-6$. Both inputs have therefore changed numerical value before addition. Their exact signed sum is $-12$, below the four-bit minimum $-8$. Modular addition stores $20\bmod16=4$, word0100, decoded as $+4$; later widening preserves4.

| Pipeline | Values actually added | Stored signed result |
|---|---|---|
| Widen inputs first | $90,90$ | 180 |
| Add at width8 | $90,90$ | $-76$ |
| Narrow inputs, then add at width4 | $-6,-6$ | 4 |

Widening preserves the decoder value it receives and cannot recover discarded information. Input narrowing and result narrowing are distinct losses. None of these hardware calculations predicts the behavior of an overflowing C17 signed expression, which has a different language contract.

### Transfer 5. Negative division, logical shift and arithmetic shift

**Question.** For eight-bit two's-complement $-29$, calculate logical right shift by3, arithmetic right shift by3, and division by8 truncated toward zero. Derive a bias conversion from floor division to truncation.

**Solution.** The stored unsigned code is $256-29=227$, word11100011. Logical shifting inserts zeros and gives00011100, unsigned28. Arithmetic shifting repeats the sign and gives11111100, unsigned252, signed $-4$. This equals $\lfloor-29/8\rfloor$ because $-29=8(-4)+3$ in Euclidean division. Truncation toward zero instead gives $-3$, with the usual truncating remainder $-5$ because $-29=8(-3)-5$.

Adding bias $2^3-1=7$ in a sufficiently wide domain gives $-22$; floor division $\lfloor-22/8\rfloor=-3$ reproduces truncation. In general, for a negative $x=qD+r$ with floor quotient and $0\le r<D$, adding $D-1$ leaves floor quotient $q$ if $r=0$ and changes it to $q+1$ otherwise. This matches negative truncation. The logical shift instead divides the unsigned code227 and has no signed-division meaning. A rotate would move discarded bits back into the word and is another operation altogether. The bias expression needs its own intermediate-range and language-shift analysis before implementation.

### Transfer 6. Range, resolution and shortened Hamming protection

**Question.** Cover the interval $[-20,20]$ with two's-complement fixed point at spacing at most $1/64$. Choose the smallest data width, single-error Hamming parity count and SECDED total width. Encode $-3.3125$.

**Solution.** At least6 fractional bits are needed. Eleven total bits with $f=6$ give range $[-16,1023/64]$, insufficient. Twelve give $[-32,2047/64]$, covering both endpoints. Increasing $f$ at width11 only shrinks the range, so twelve is minimal. For twelve data bits, $r=4$ gives16 syndrome states but needs $12+4+1=17$; it fails. At $r=5$,32 states cover $12+5+1=18$, so a shortened single-error Hamming code uses17 positions. One overall parity bit makes the SECDED total18.

The scaled integer is $-3.3125\cdot64=-212$. Its twelve-bit code is $4096-212=3884$, word111100101100. Re-decoding gives $(3884-4096)/64=-212/64=-3.3125$. A protected word's position ordering needs a separate parity-placement specification; the parity count alone does not give its transmitted bit string. Numerical width, resolution and bounded error correction are three distinct design constraints and must be solved in that order.

### Transfer 7. BCD correction and the count of corrected input cases

**Question.** Add BCD48 and57 with incoming units carry1. Then, among all200 ordered triples of digit inputs $a,b\in\{0,\ldots,9\}$ and incoming carry $c\in\{0,1\}$, how many require add-six correction? How many of those already have an initial binary carry?

**Solution.** Units subtotal $8+7+1=16$ gives an initial binary carry and low nibble0000. Correction adds6, leaving decimal digit6 and carry1. Tens subtotal $4+5+1=10$ has no initial binary carry but invalid low nibble1010; correction yields16, digit0 and carry1. The result is BCD000100000110, decimal106.

For the count, let $t=a+b+c$. Correction is required exactly when $t\ge10$. The involution $(a,b,c)\mapsto(9-a,9-b,1-c)$ maps $t$ to $19-t$, pairing each uncorrected case with a corrected case. There are200 triples and no self-pair at a half-integer threshold, so exactly100 require correction. Initial binary carry means $t\ge16$. At $c=0$, sums16,17,18 have3,2,1 ordered digit pairs, totaling6. At $c=1$, sums15,16,17,18 have4,3,2,1 pairs, totaling10. Thus16 corrected cases already carry, and84 have no initial carry but an invalid retained nibble. This proves why neither testing carry alone nor testing low-nibble legality alone implements the full rule.

### Transfer 8. Adding Gray-encoded indices at an insufficient width

**Question.** At five-bit reflected Gray width, add indices represented by labels11010 and11101. Compare an exact-result policy with index wrap modulo32. Explain why adding the raw Gray words fails.

**Solution.** Prefix XOR decodes11010 as10011, index19, and11101 as10110, index22. Their exact sum41 does not fit the unsigned five-bit index range $[0,31]$. An exact-result policy must reject that width or widen the index. With explicit modulo32 index arithmetic, the result is9, binary01001. Reflected Gray encoding is $01001\oplus00100=01101$.

Adding raw labels as binary instead computes $26+29=55$, low five-bit word10111. Prefix XOR decodes that word as11010, index26, not9. An exact widened index41 would be binary101001 at width6 and Gray $101001\oplus010100=111101$, a third result under a third width policy. State whether the intended operation is exact or modular, choose adequate index width, decode both inputs, operate on indices and re-encode. Gray adjacency does not turn the labeling function into a homomorphism for ordinary integer addition.

### Transfer 9. One error and two errors can share a syndrome

**Question.** Encode data0110 into extended even-parity Hamming, placing data at3,5,6,7 and overall parity at8. Compare flipping position7 alone with flipping positions7 and8. Calculate the transmitted word, syndrome and proper action under an at-most-two-error premise.

**Solution.** The data assignments are $d_3=0,d_5=1,d_6=1,d_7=0$. Parity equations give $p_1=0\oplus1\oplus0=1$, $p_2=0\oplus1\oplus0=1$, and $p_4=1\oplus1\oplus0=0$. The seven-position word is1100110, with four ones, so overall even parity is0 and the transmitted word is11001100.

| Corruption | Received word | Syndrome high-to-low | Overall XOR | Action |
|---|---|---|---|---|
| Position7 only | 11001110 | 111 | 1 | Correct position7. |
| Positions7 and8 | 11001111 | 111 | 0 | Detect double error; do not correct. |

The overall bit is not included in the three Hamming-position checks, so both cases have syndrome7. It changes the overall XOR and consequently the decoder action. Correcting the first case recovers the original word and data0110. Applying the same correction to the second would leave a wrong overall parity bit and would ignore the proper double-error decision. Observed syndrome alone is insufficient; error assumptions and both check layers supply the theorem.

### Transfer 10. Exceeding SECDED's bound can produce a valid wrong word

**Question.** Starting with the all-zero eight-bit extended Hamming word, flip positions1,2,4. What would a decoder that assumes at most two errors infer? Show the result of its inferred correction and explain the limit.

**Solution.** The received word in increasing position order is11010000. Its Hamming syndrome is $1\oplus2\oplus4=7$, binary111, and its overall XOR is1 because three bits changed. These observations mimic a single error at position7. A decoder using the at-most-two-error table would flip7, returning11010010. Its four one positions1,2,4,7 have syndrome $1\oplus2\oplus4\oplus7=0$ and even overall parity, so it is a different valid extended codeword. Data position7 is one instead of zero; the recovered message is wrong.

The code's minimum distance4 permits this exact four-position difference between valid words. Single-error correction and double-error detection do not guarantee detection or correction of every three-error pattern. The example does not contradict the SECDED theorem, because the actual corruption violates its premise. It instead demonstrates why a post-correction valid-codeword test cannot certify which original message was transmitted once more errors are allowed than the decoder's assumed bound.
