## Q1

Correct option: 2.

**Translate membership before manipulating the expression.** Fix an arbitrary element of the common universe. Write $a=1$ when it belongs to $A$ and $b=1$ when it belongs to $B$. Difference is intersection with a complement, so the requested membership bit is
$$F=(\neg a)b+[(a\neg b)+\neg b](b\neg a).$$
Absorption reduces the bracket to $\neg b$, because $(a\neg b)+\neg b=\neg b$. Its product with the last factor is therefore $(\neg b)b\neg a=0$. Thus $F=b\neg a$, which is membership in $B\setminus A$.

**Check every region.** In order $(a,b)=00,01,10,11$, the output vector is $0,1,0,0$. The second union operand is zero in all four regions; no large distributive expansion is required. This proves equality element by element for arbitrary sets, including empty sets and equal sets.

**Options and transfer.** Option 1 has vector $0,0,1,1$ and fails on the $A$-only region; option 3 has $0,0,1,0$ and reverses the difference; option 4 has $0,1,0,1$ and improperly includes the intersection. A region used to refute an option must be possible for arbitrary sets; a special instance such as $A=B=\varnothing$ makes several expressions coincide without proving an identity. The shared universe is necessary when complementing either set.

## Q2

Correct option: 3.

**Canonical CNF is built from false rows.** The stated true indices, with $A$ most significant, are $6,4,3,1$. The complete index set is $\{0,1,2,3,4,5,6,7\}$, so the false indices are $0,2,5,7$. A maxterm is an OR clause that is false on exactly its named row: bit zero gives a positive literal, and bit one gives a negative literal.
$$F=(A+B+C)(A+\neg B+C)(\neg A+B+\neg C)(\neg A+\neg B+\neg C).$$
For row $000$, the first clause has three zero literals. For row $111$, the last has three zero literals. Neither row is in the true list, so both requested clauses must occur. This gives option 3.

**Independent functional check.** The true rows are precisely those with $A\ne C$, irrespective of $B$, so $F=A\oplus C$. That shorter formula describes the same function but is not its canonical CNF over all three named inputs. A canonical clause cannot omit $B$ just because the function is independent of $B$.

**Alternatives and boundary.** Option 1 wrongly removes the row-zero clause; option 2 removes the row-seven clause; option 4 removes both. These omissions leave their designated false rows accepted unless another noncanonical construction is introduced. Canonical CNF is unique up to clause/literal ordering, unlike an arbitrary equivalent CNF. Always distinguish the requested syntax from the simplified truth function.

## Q3

Correct option: 2.

**Count disjoint zero-count cases.** There are four labeled string positions and four symbols; once a position is declared nonzero it has three choices. An even zero count means exactly $0$, $2$, or $4$ zeros. Consequently
$$A=\binom40 3^4+\binom42 3^2+\binom44 3^0=81+54+1=136.$$
The all-zero string contributes one, not four. For the middle case choose the two zero positions in $\binom42=6$ ways and independently fill the other two positions in $3^2=9$ ways. The cases are disjoint, so addition does not overcount.
$$A/4=136/4=34\in(30,45].$$
This is option 2. The value exceeds the upper endpoints of options 1 and 3 and is not greater than 45 as required by option 4.

**A second derivation and its conceptual meaning.** The coefficient-generating polynomial is $(3+t)^4$: the coefficient of $t^j$ counts strings with $j$ zeros. Adding its values at $t=1$ and $t=-1$ cancels odd powers, giving $A=(4^4+2^4)/2=136$. The two parity classes are not equal: the odd count is $(256-16)/2=120$. The Boolean parity function on four *independent binary flags* has eight even and eight odd flag patterns, but those patterns correspond to unequal numbers of original strings. This is why blindly taking half of 256 fails.

## Q4

Correct option: 2.

**List false rows and build their clauses.** True rows are $111,110,101,011$. False rows are $000,001,010,100$. For each false row, choose the literal polarity that makes every literal in its OR clause zero on that row:

| False row | Required maxterm |
|---|---|
| 000 | $p+q+r$ |
| 001 | $p+q+\neg r$ |
| 010 | $p+\neg q+r$ |
| 100 | $\neg p+q+r$ |

Conjoining these four clauses gives option 2; their displayed order is immaterial. Any true row differs from each false row in at least one bit, making every clause true on that true row. This proves the construction in both directions.

**Diagnose the original alternatives exactly.** Option 1 is the canonical DNF of the same function, so it is semantically equivalent but does not have the requested CNF syntax. In the corrected original option 3, the first clause $\neg p+\neg q+\neg r$ is false on the required true row $111$; the other clauses exclude $010,101,110$. Option 4 is a DNF whose one rows are $001,000,010,100$: it is the complement of majority, accepting precisely the required false rows. This analysis uses the source PDF's options 3 and 4, replacing the older transcription.

**Transfer.** The function is majority, with short SOP $pq+pr+qr$ and short POS $(p+q)(p+r)(q+r)$. Neither is canonical over three inputs: every canonical clause must contain all three input names. A familiar equivalent expression is insufficient when the task specifies a normal form.

## Q5

Correct option: 4.

**Evaluate the two constraints together.** Material implication is $\neg p+r$, and equivalence is $pq+(\neg p)(\neg q)$. The equivalence requires $p=q$. If both are zero, the implication is true for either $r$, yielding rows $000,001$. If both are one, the implication requires $r=1$, yielding row $111$.
$$\operatorname{on}(F)=\{0,1,7\},\qquad \operatorname{off}(F)=\{2,3,4,5,6\}.$$
Here the numerical index is $4p+2q+r$. Canonical product notation uses the off-set, hence $F=\prod M(2,3,4,5,6)$, option 4. Each maxterm is zero at exactly its own index and true at every other index.

**Audit every alternative.** Option 1 is the correct canonical sum but the wrong requested form. Option 2 has zeros at $0,1,3,4,6$ and therefore rejects the true row $000$ while accepting the false row $010$. Option 3 asserts that $010,101,111$ are true; at $010$ the equivalence already fails. Option 4 retains precisely the correct three true rows.

**Conceptual and boundary checks.** Conjunction means that satisfying the implication alone is not enough. Row $101$ satisfies the implication but fails $p\Leftrightarrow q$. Conversely, $110$ satisfies the equivalence but fails the implication. A different bit significance would change the numerical indices, while the underlying input triples would remain the same. Preserve the stated source order before converting tuples into numbers.

## Q6

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

## Q7

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

## Q8

Correct option: 1.

**Derive the on-set in the stated order.** The equivalence permits $a=b=0$ or $a=b=1$. In the first case $a\Rightarrow c$ is true regardless of $c$; in the second it forces $c=1$. Thus the true triples are $000,001,111$, with indices $0,1,7$ because $a$ has weight four and $c$ weight one.
$$F=\neg a\neg b\neg c+\neg a\neg b c+abc=\sum m(0,1,7).$$
The two first minterms combine to $\neg a\neg b$, so a shorter equivalent formula is $\neg a\neg b+abc$. Combining is valid but not required to answer the canonical-sum question.

**Option-by-option check.** Option 1 is correct. Option 2 lists the five false indices and gives the complement of the requested function. Option 3 uses product notation at the true indices, making those rows zero rather than one. Option 4 includes index two, row $010$, where $a$ and $b$ disagree, and omits index one, row $001$, which satisfies both clauses. These are explicit counterexamples rather than a claim that the other formulas merely look wrong.

**Transfer.** Changing index order changes which number labels a row, not its truth value. Before reading any sum/product notation, write the index weight formula and state whether the requested set is the on-set or off-set. A canonical term fixes every input, even if a simplified expression can omit one input on some branch.

## Q9

Correct option: 1.

**Separate steady-state equivalence from the stated transition.** The original function is $F=ab+(\neg a)c$. Consensus permits the extra product $bc$ because
$$bc=bc(a+\neg a)=abc+(\neg a)bc.$$
The first added part is absorbed by $ab$, the second by $(\neg a)c$. Consequently $ab+(\neg a)c+bc=F$ on every input. With $b=c=1$, the added term is one independently of $a$, maintaining a continuously enabled path through its product gate.

**Explain the possible glitch.** In the specified two-level SOP implementation, when $a$ goes from one to zero the direct $ab$ path can fall before the inverter-dependent $(\neg a)c$ path rises. If their delays allow a nonempty interval with both terms zero, the output can temporarily fall even though both endpoint truth values are one. The consensus path remains asserted during that single-input transition. This requires stable $b,c$ and the declared implementation model; it is not a universal statement about all physical circuits or simultaneous input changes.

**Distractors.** Adding $ac$ changes the function at $a,b,c=101$, where the original is zero. Adding $(\neg b)c$ also changes that row. Adding $a\neg c$ changes $100$, where the original is zero. Thus all three alternatives violate functional equivalence as well as lacking the required stable bridging product. Option 1 alone satisfies both requirements. Do not remove a consensus term from a hazard-controlled design merely because it is algebraically redundant.

## Q10

Correct option: 2.

**Identify independent choices, not unknown cells.** For three input bits, full input complementation maps index $i$ to $7-i$. The unknown cells at $0,1,6,7$ form two pairs: $(0,7)$ and $(1,6)$. Self-duality requires $F(7-i)=1-F(i)$. Choosing $F(0)$ forces $F(7)$, and choosing $F(1)$ forces $F(6)$.

| $F(0)$ | $F(7)$ | $F(1)$ | $F(6)$ |
|---|---|---|---|
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |

The remaining pairs $(2,5)$ and $(3,4)$ are already fixed and consistent by hypothesis, so they add no choices. The count is $2^2=4$, option 2.

**Explain every alternative.** Two would impose an unjustified link between the two free pairs. Eight would introduce a third independent choice although only two unknown complementary pairs remain. Sixteen would treat all four unknown cells independently and include assignments with equal outputs on a complementary pair. If a fixed pair had equal outputs, there would be zero completions, regardless of the free pairs. If one member of an unknown pair were fixed, that pair would contribute one completion rather than two. Self-duality constraints are therefore handled pair by pair before multiplying the remaining independent choices.

## Q11

Correct option: 2.

**Restrict the selector before eliminating its control.** At $x=0$, the expression becomes $F_0=z$. At $x=1$, it becomes $F_1=y$. The existential quantifier asks whether at least one of these choices produces one, hence
$$\exists x\,F=F_0+F_1=z+y.$$
This is still a function of $y,z$, not a single constant. For contexts $00,01,10,11$, the cofactor pairs are $(0,0),(1,0),(0,1),(1,1)$ and the existential outputs are $0,1,1,1$.

**Witness interpretation.** At $(y,z)=01$, choose $x=0$; at $10$, choose $x=1$; at $11$, either choice works. At $00$, neither works. A witness is allowed to depend on the remaining input context, unless an additional outer quantifier imposes another dependency.

**Alternatives.** Option 1, $yz$, is the universal result and rejects both contexts with exactly one successful witness. Option 3, XOR, rejects $11$ even though it has two witnesses. Option 4, $\neg y+z$, accepts $00$ despite no witness and rejects $10$ despite a valid witness. Option 2 matches all contexts. Quantification is not substitution of a favorite input value: replacing $x$ by zero would lose $10$, and replacing it by one would lose $01$. Only the cofactor OR expresses the required choice over both values.

## Q12

Correct option: 1.

**Use weights to verify the complete function.** In the proposed ANF $ab\oplus ac\oplus bc$, a weight-zero or weight-one input activates no pair product and gives zero. A weight-two input activates exactly one pair and gives one. Weight three activates all three pairs, whose XOR is $1\oplus1\oplus1=1$. These four cases exhaust all eight input rows and match majority.

**Coefficient derivation.** Majority has $F(000)=0$ and all singleton outputs zero, so its constant and linear ANF coefficients vanish. Each two-input subset has output one, giving its pair coefficient one. The cubic coefficient is the XOR of all eight outputs; there are four true rows, so that coefficient is zero. Uniqueness of ANF then fixes exactly the displayed quadratic expression, option 1.

**Distractors.** Option 2 adds $abc$ and flips $111$ from one to zero. Option 3 is odd parity: at $100$ it is one while majority is zero, and at $110$ it is zero while majority is one. Option 4 accepts only $111$ and misses all three weight-two rows. The OR formula $ab+ac+bc$ and this three-term XOR happen to agree, but their pair products overlap at $111$. Replacing one pairwise OR by XOR would not preserve that overlap; the three-term agreement follows from its *odd* threefold multiplicity. This example does not license a general OR-to-XOR substitution.

## Q13

Correct option: 4.

**Calculate the derivative as a function of the other inputs.** The zero cofactor is $F_0=yz$, while the one cofactor is $F_1=1\oplus yz=\neg(yz)$. Therefore
$$D_xF=F_0\oplus F_1=yz\oplus(1\oplus yz)=1.$$
For each of the four $(y,z)$ contexts, changing $x$ changes the output. The question counts complete *starting assignments*, so both $x=0$ and $x=1$ contribute for each context. The answer is $2\cdot4=8$, option 4.

**Inspect the two possible context types.** If $yz=0$, the function is $x$, so toggling $x$ flips zero to one or one to zero. If $yz=1$, the function is $\neg x$, and the toggle still flips the output, with reversed direction. Sensitivity records whether a change occurs; it does not say that every change is increasing.

**Options and counting convention.** Four counts contexts or undirected edges, rather than starting rows. Two would count only the two values of $x$ and ignore all contexts. Six has no support in the cofactor table: none of the four contexts is insensitive. Under an alternate request for distinct *undirected* $x$-edges the answer would indeed be four, because each edge has two starting endpoints. State which object is being counted before applying the factor two. No assumption of uniformly random inputs is needed for this exact count.

## Q14

Correct option: 1.

**Use the dual consensus identity.** The first two factors expand to
$$ (a+b)(\neg a+c)=ac+(\neg a)b+bc.$$
The last term is consensus: $bc=abc+(\neg a)bc$, covered respectively by $ac$ and $(\neg a)b$. Therefore the first two factors already equal $G=ac+(\neg a)b$. Every assignment satisfying $ac$ has $c=1$, and every assignment satisfying $(\neg a)b$ has $b=1$; hence $G$ implies $b+c$. Multiplying by that final factor changes nothing, proving option 1.

**An independent cofactor derivation.** At $a=0$, the original product is $b\cdot1\cdot(b+c)=b$. At $a=1$, it is $1\cdot c\cdot(b+c)=c$. Shannon reconstruction is $(\neg a)b+ac$. This route avoids generating the redundant term at all.

**Exact counterexamples.** Option 2 swaps the branches: at $abc=101$, the actual output is one and that option gives zero. Option 3, $bc$, also gives zero on $101$ despite the actual one. Option 4 gives one on $100$, whereas the original has its second factor zero. Thus the wrong choices fail for different reasons: reversed selection, excessive restriction, and excessive acceptance. Cofactors are a useful independent check on a long algebraic simplification because they preserve the control polarity explicitly.

## Q15

Correct option: 3.

**Use the componentwise partial order.** The two-input cube has bottom $00$, top $11$, and two incomparable middle rows $01,10$. The endpoints are fixed to zero and one. Monotonicity requires the output at a lower row not exceed that at a higher row. Either Boolean value at either middle row lies between the fixed endpoint values, and neither middle row constrains the other.

| $F(01)$ | $F(10)$ | Resulting function |
|---|---|---|
| 0 | 0 | $ab$ |
| 0 | 1 | $a$ |
| 1 | 0 | $b$ |
| 1 | 1 | $a+b$ |

There are four independent middle-row assignments, giving option 3. Their distinct truth tables prove that no two choices name the same function.

**Distractors and boundaries.** Two could result from incorrectly forcing the incomparable middle rows equal and keeping only AND and OR. Three omits one valid choice without a monotonicity reason. Six is the count when the endpoint constraints are removed: the two constant functions are then additionally allowed. Monotone does not mean strictly increasing; for example AND remains zero along several increasing edges. Nor does monotone imply symmetric: $a$ and $b$ depend on which middle row is true. For higher input counts, arbitrary assignments to all intermediate rows are not valid, because many intermediate rows become comparable and impose additional inequalities.

## Q16

Correct option: 2.

**Build a bijection or recover the coefficients.** Each implication forbids only an adjacent $10$. Once a bit is one, every bit to its right must be one. Conversely, a block of zeros followed by ones satisfies every implication. A legal row therefore has a unique zero-block length $k\in\{0,1,\ldots,n\}$, establishing a bijection with $n+1$ choices. All-zero and all-one rows correspond to $k=n$ and $k=0$; neither may be dropped.

**Exact requested instance.**
$$5+1=6$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $16$, comes from $2^{n-1}$, which assumes a parity-style half split although no output-reversing bijection has been established. Option 2, $6$, equals the exact result. Option 3, $32$, comes from $2^n$, which counts every row, including a row with a forbidden10 adjacency. Option 4, $5$, comes from $n$, which drops one of the two valid constant-word endpoints.

**Worked small example and transfer.** For five bits the six accepted words are $00000,00001,00011,00111,01111,11111$. A word such as $01011$ fails where its one is followed by zero. This is not the same property as the output function being monotone in every input: the conjunction of implications can fall when an earlier bit changes from zero to one.

## Q17

Correct option: 1.

**Build a bijection or recover the coefficients.** Each implication forbids only an adjacent $10$. Once a bit is one, every bit to its right must be one. Conversely, a block of zeros followed by ones satisfies every implication. A legal row therefore has a unique zero-block length $k\in\{0,1,\ldots,n\}$, establishing a bijection with $n+1$ choices. All-zero and all-one rows correspond to $k=n$ and $k=0$; neither may be dropped.

**Exact requested instance.**
$$8+1=9$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $9$, equals the exact result. Option 2, $256$, comes from $2^n$, which counts every row, including a row with a forbidden10 adjacency. Option 3, $8$, comes from $n$, which drops one of the two valid constant-word endpoints. Option 4, $128$, comes from $2^{n-1}$, which assumes a parity-style half split although no output-reversing bijection has been established.

**Worked small example and transfer.** For five bits the six accepted words are $00000,00001,00011,00111,01111,11111$. A word such as $01011$ fails where its one is followed by zero. This is not the same property as the output function being monotone in every input: the conjunction of implications can fall when an earlier bit changes from zero to one.

## Q18

Correct option: 4.

**Build a bijection or recover the coefficients.** Each implication forbids only an adjacent $10$. Once a bit is one, every bit to its right must be one. Conversely, a block of zeros followed by ones satisfies every implication. A legal row therefore has a unique zero-block length $k\in\{0,1,\ldots,n\}$, establishing a bijection with $n+1$ choices. All-zero and all-one rows correspond to $k=n$ and $k=0$; neither may be dropped.

**General result.** The derivation gives $n+1$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $2^n$, counts every row, including a row with a forbidden10 adjacency. Option 2, $n$, drops one of the two valid constant-word endpoints. Option 3, $2^{n-1}$, assumes a parity-style half split although no output-reversing bijection has been established. Option 4, $n+1$, is the derived result.

**Worked small example and transfer.** For five bits the six accepted words are $00000,00001,00011,00111,01111,11111$. A word such as $01011$ fails where its one is followed by zero. This is not the same property as the output function being monotone in every input: the conjunction of implications can fall when an earlier bit changes from zero to one.

## Q19

Correct option: 3.

**Analyze the scope rather than guessing from the previous number.**

Option 1 is false because $0\Rightarrow0$ is true. Option 2 permits a forbidden $10$. Option 3 is true for $n\ge2$: an equivalence chain accepts only the two constant words, whereas $0^{n-1}1$ satisfies the implication chain and not the equivalence chain. Option 4 is refuted by that same word. For $n=1$, both empty chains accept both words, so “weaker” is not strict; the revised boundary stem specifies $n\ge2$.

**Underlying derivation.** Each implication forbids only an adjacent $10$. Once a bit is one, every bit to its right must be one. Conversely, a block of zeros followed by ones satisfies every implication. A legal row therefore has a unique zero-block length $k\in\{0,1,\ldots,n\}$, establishing a bijection with $n+1$ choices. All-zero and all-one rows correspond to $k=n$ and $k=0$; neither may be dropped.

**Concrete check.** For five bits the six accepted words are $00000,00001,00011,00111,01111,11111$. A word such as $01011$ fails where its one is followed by zero. This is not the same property as the output function being monotone in every input: the conjunction of implications can fall when an earlier bit changes from zero to one.

## Q20

Correct option: 1.

**Build a bijection or recover the coefficients.** Fix input position one and map each word to the word with only that bit flipped. Applying the map twice returns the starting word, so it is a bijection without fixed words. The XOR output changes because exactly one summand toggles. Each pair contains exactly one true and one false word. There are $2^n$ total words and thus $2^{n-1}$ true ones for $n\ge1$.

**Exact requested instance.**
$$2^{5-1}=16$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $16$, equals the exact result. Option 2, $32$, comes from $2^n$, which includes both members of every true/false pair. Option 3, $5$, comes from $n$, which counts singleton-one words but omits odd-weight words of higher weight. Option 4, $15$, comes from $2^{n-1}-1$, which removes a true word although no extra exclusion is present.

**Worked small example and transfer.** With three inputs the true words are $001,010,100,111$. Flipping the first input pairs them with $101,110,000,011$, respectively, all false. Equivalently, choose the last $n-1$ inputs arbitrarily: exactly one value of the first input makes the total parity odd.

## Q21

Correct option: 4.

**Build a bijection or recover the coefficients.** Fix input position one and map each word to the word with only that bit flipped. Applying the map twice returns the starting word, so it is a bijection without fixed words. The XOR output changes because exactly one summand toggles. Each pair contains exactly one true and one false word. There are $2^n$ total words and thus $2^{n-1}$ true ones for $n\ge1$.

**Exact requested instance.**
$$2^{8-1}=128$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $256$, comes from $2^n$, which includes both members of every true/false pair. Option 2, $8$, comes from $n$, which counts singleton-one words but omits odd-weight words of higher weight. Option 3, $127$, comes from $2^{n-1}-1$, which removes a true word although no extra exclusion is present. Option 4, $128$, equals the exact result.

**Worked small example and transfer.** With three inputs the true words are $001,010,100,111$. Flipping the first input pairs them with $101,110,000,011$, respectively, all false. Equivalently, choose the last $n-1$ inputs arbitrarily: exactly one value of the first input makes the total parity odd.

## Q22

Correct option: 3.

**Build a bijection or recover the coefficients.** Fix input position one and map each word to the word with only that bit flipped. Applying the map twice returns the starting word, so it is a bijection without fixed words. The XOR output changes because exactly one summand toggles. Each pair contains exactly one true and one false word. There are $2^n$ total words and thus $2^{n-1}$ true ones for $n\ge1$.

**General result.** The derivation gives $2^{n-1}$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $n$, counts singleton-one words but omits odd-weight words of higher weight. Option 2, $2^{n-1}-1$, removes a true word although no extra exclusion is present. Option 3, $2^{n-1}$, is the derived result. Option 4, $2^n$, includes both members of every true/false pair.

**Worked small example and transfer.** With three inputs the true words are $001,010,100,111$. Flipping the first input pairs them with $101,110,000,011$, respectively, all false. Equivalently, choose the last $n-1$ inputs arbitrarily: exactly one value of the first input makes the total parity odd.

## Q23

Correct option: 2.

**Analyze the scope rather than guessing from the previous number.**

Option 1 confuses parity with all-input equality: $001$ has odd parity although its bits are not all equal. Option 2 states the essential bijection requirement. Option 3 is refuted by the source symbol-count question, where the even and odd classes have136 and120 strings. Option 4 contradicts $0\oplus t=t$ and $1\oplus t=\neg t$. The half-count requires an actual predicate-reversing map on the objects being counted.

**Underlying derivation.** Fix input position one and map each word to the word with only that bit flipped. Applying the map twice returns the starting word, so it is a bijection without fixed words. The XOR output changes because exactly one summand toggles. Each pair contains exactly one true and one false word. There are $2^n$ total words and thus $2^{n-1}$ true ones for $n\ge1$.

**Concrete check.** With three inputs the true words are $001,010,100,111$. Flipping the first input pairs them with $101,110,000,011$, respectively, all false. Equivalently, choose the last $n-1$ inputs arbitrarily: exactly one value of the first input makes the total parity odd.

## Q24

Correct option: 2.

**Build a bijection or recover the coefficients.** For $n\ge1$, complementation pairs each input word with a distinct word. There are $2^{n-1}$ complementary pairs. In a self-dual truth table one output in each pair is freely chosen, and the other is forced to its complement. The pairs are independent, giving two choices per pair and $2^{2^{n-1}}$ functions. This counts functions, not accepted input rows of one function.

**Exact requested instance.**
$$2^{2^{3-1}}=2^{4}=16$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $8$, comes from $2^n$, which counts input words rather than functions. Option 2, $16$, equals the exact result. Option 3, $256$, comes from $2^{2^n}$, which counts unrestricted truth tables with two independently chosen outputs per complementary pair. Option 4, $4$, comes from $2^{n-1}$, which counts complementary input pairs rather than assignments of their output choices.

**Worked small example and transfer.** For three inputs the pairs are $(000,111),(001,110),(010,101),(011,100)$. Four independently chosen representative outputs give16 functions. Every such function has four true rows, one in each pair, yet there are balanced functions that are not self-dual: a balanced table with both000 and111 true fails self-duality.

## Q25

Correct option: 1.

**Build a bijection or recover the coefficients.** For $n\ge1$, complementation pairs each input word with a distinct word. There are $2^{n-1}$ complementary pairs. In a self-dual truth table one output in each pair is freely chosen, and the other is forced to its complement. The pairs are independent, giving two choices per pair and $2^{2^{n-1}}$ functions. This counts functions, not accepted input rows of one function.

**Exact requested instance.**
$$2^{2^{4-1}}=2^{8}=256$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $256$, equals the exact result. Option 2, $65536$, comes from $2^{2^n}$, which counts unrestricted truth tables with two independently chosen outputs per complementary pair. Option 3, $8$, comes from $2^{n-1}$, which counts complementary input pairs rather than assignments of their output choices. Option 4, $16$, comes from $2^n$, which counts input words rather than functions.

**Worked small example and transfer.** For three inputs the pairs are $(000,111),(001,110),(010,101),(011,100)$. Four independently chosen representative outputs give16 functions. Every such function has four true rows, one in each pair, yet there are balanced functions that are not self-dual: a balanced table with both000 and111 true fails self-duality.

## Q26

Correct option: 4.

**Build a bijection or recover the coefficients.** For $n\ge1$, complementation pairs each input word with a distinct word. There are $2^{n-1}$ complementary pairs. In a self-dual truth table one output in each pair is freely chosen, and the other is forced to its complement. The pairs are independent, giving two choices per pair and $2^{2^{n-1}}$ functions. This counts functions, not accepted input rows of one function.

**General result.** The derivation gives $2^{2^{n-1}}$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $2^{2^n}$, counts unrestricted truth tables with two independently chosen outputs per complementary pair. Option 2, $2^{n-1}$, counts complementary input pairs rather than assignments of their output choices. Option 3, $2^n$, counts input words rather than functions. Option 4, $2^{2^{n-1}}$, is the derived result.

**Worked small example and transfer.** For three inputs the pairs are $(000,111),(001,110),(010,101),(011,100)$. Four independently chosen representative outputs give16 functions. Every such function has four true rows, one in each pair, yet there are balanced functions that are not self-dual: a balanced table with both000 and111 true fails self-duality.

## Q27

Correct option: 3.

**Analyze the scope rather than guessing from the previous number.**

Option 1 ignores the forced opposition within each pair. Option 2 fails for the constant-zero function. Option 3 correctly compares the output at a word with the complement of the output at its complementary word. Option 4 would demand $F(x)=1-F(x)$ on the *same* word, impossible for binary values. At $n=0$ the only input word equals its complement, so there are no self-dual scalar functions; the formula is intentionally restricted to $n\ge1$.

**Underlying derivation.** For $n\ge1$, complementation pairs each input word with a distinct word. There are $2^{n-1}$ complementary pairs. In a self-dual truth table one output in each pair is freely chosen, and the other is forced to its complement. The pairs are independent, giving two choices per pair and $2^{2^{n-1}}$ functions. This counts functions, not accepted input rows of one function.

**Concrete check.** For three inputs the pairs are $(000,111),(001,110),(010,101),(011,100)$. Four independently chosen representative outputs give16 functions. Every such function has four true rows, one in each pair, yet there are balanced functions that are not self-dual: the three-input parity complement for even input dimension provides the analogous failure; directly on three inputs a balanced table with both000 and111 true fails self-duality.

## Q28

Correct option: 2.

**Build a bijection or recover the coefficients.** The inputs form $n$ disjoint variable pairs; their product *events* need not be disjoint. There are $4^n$ complete words. The OR is false exactly when every pair avoids11. Each pair then has the three allowed states00,01,10; because their input positions are distinct these choices combine independently into $3^n$ false words. Subtracting gives $4^n-3^n$ true words.

**Exact requested instance.**
$$4^5-3^5=1024-243=781$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $32$, comes from $2^n$, which treats the2n primary inputs as onlyn free input bits. Option 2, $781$, equals the exact result. Option 3, $1024$, comes from $4^n$, which includes words where no product is true. Option 4, $243$, comes from $3^n$, which is the false-row count, the complement of the requested set.

**Worked small example and transfer.** For two pairs the total is16, with9 false words and7 true words. Inclusion–exclusion gives the same result: the first true-product event contains4 rows, the second contains4, and their intersection contains the single row1111; hence $4+4-1=7$. Simply adding event sizes overcounts overlaps.

## Q29

Correct option: 1.

**Build a bijection or recover the coefficients.** The inputs form $n$ disjoint variable pairs; their product *events* need not be disjoint. There are $4^n$ complete words. The OR is false exactly when every pair avoids11. Each pair then has the three allowed states00,01,10; because their input positions are distinct these choices combine independently into $3^n$ false words. Subtracting gives $4^n-3^n$ true words.

**Exact requested instance.**
$$4^8-3^8=65536-6561=58975$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $58975$, equals the exact result. Option 2, $65536$, comes from $4^n$, which includes words where no product is true. Option 3, $6561$, comes from $3^n$, which is the false-row count, the complement of the requested set. Option 4, $256$, comes from $2^n$, which treats the2n primary inputs as onlyn free input bits.

**Worked small example and transfer.** For two pairs the total is16, with9 false words and7 true words. Inclusion–exclusion gives the same result: the first true-product event contains4 rows, the second contains4, and their intersection contains the single row1111; hence $4+4-1=7$. Simply adding event sizes overcounts overlaps.

## Q30

Correct option: 4.

**Build a bijection or recover the coefficients.** The inputs form $n$ disjoint variable pairs; their product *events* need not be disjoint. There are $4^n$ complete words. The OR is false exactly when every pair avoids11. Each pair then has the three allowed states00,01,10; because their input positions are distinct these choices combine independently into $3^n$ false words. Subtracting gives $4^n-3^n$ true words.

**General result.** The derivation gives $4^n-3^n$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $4^n$, includes words where no product is true. Option 2, $3^n$, is the false-row count, the complement of the requested set. Option 3, $2^n$, treats the2n primary inputs as onlyn free input bits. Option 4, $4^n-3^n$, is the derived result.

**Worked small example and transfer.** For two pairs the total is16, with9 false words and7 true words. Inclusion–exclusion gives the same result: the first true-product event contains4 rows, the second contains4, and their intersection contains the single row1111; hence $4+4-1=7$. Simply adding event sizes overcounts overlaps.

## Q31

Correct option: 3.

**Analyze the scope rather than guessing from the previous number.**

Option 1 is false because1111 satisfies both products for two pairs and has two witnesses. Option 2 falsely asserts independence after sharing an input: $ab+ac=a(b+c)$ has three satisfying three-bit rows:101,110,111. Condition on $a$ rather than use a fictitious four-bit table. Option 3 identifies why the independent-pair argument becomes invalid. Option 4 replaces OR by AND and accepts only the all-pairs-true word. Independence refers to input choices, not exclusive output events.

**Underlying derivation.** The inputs form $n$ disjoint variable pairs; their product *events* need not be disjoint. There are $4^n$ complete words. The OR is false exactly when every pair avoids11. Each pair then has the three allowed states00,01,10; because their input positions are distinct these choices combine independently into $3^n$ false words. Subtracting gives $4^n-3^n$ true words.

**Concrete check.** For two pairs the total is16, with9 false words and7 true words. Inclusion–exclusion gives the same result: the first true-product event contains4 rows, the second contains4, and their intersection contains the single row1111; hence $4+4-1=7$. Simply adding event sizes overcounts overlaps.

## Q32

Correct option: 1.

**Build a bijection or recover the coefficients.** An accepted row has precisely two distinct one positions and zero in every other position. Assigning an unordered two-element subset of the $n$ labeled positions uniquely specifies such a row, and every accepted row determines that subset. Thus the count is $\binom n2=n(n-1)/2$, with one canonical minterm per true row.

**Exact requested instance.**
$$\binom{5}{2}=5(5-1)/2=10$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $10$, equals the exact result. Option 2, $32$, comes from $2^n$, which counts all rows regardless of weight. Option 3, $20$, comes from $n(n-1)$, which counts each two-element set twice by ordering its elements. Option 4, $25$, comes from $n^2$, which allows the same position twice and additionally retains order.

**Worked small example and transfer.** At $n=4$ the accepted words are0011,0101,0110,1001,1010,1100. There are six, not twelve: selecting position1 then2 and selecting position2 then1 produce the same row. For $n=1$ the count is zero because no two-element subset exists; the convention $\binom12=0$ handles that boundary.

## Q33

Correct option: 4.

**Build a bijection or recover the coefficients.** An accepted row has precisely two distinct one positions and zero in every other position. Assigning an unordered two-element subset of the $n$ labeled positions uniquely specifies such a row, and every accepted row determines that subset. Thus the count is $\binom n2=n(n-1)/2$, with one canonical minterm per true row.

**Exact requested instance.**
$$\binom{8}{2}=8(8-1)/2=28$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $256$, comes from $2^n$, which counts all rows regardless of weight. Option 2, $56$, comes from $n(n-1)$, which counts each two-element set twice by ordering its elements. Option 3, $64$, comes from $n^2$, which allows the same position twice and additionally retains order. Option 4, $28$, equals the exact result.

**Worked small example and transfer.** At $n=4$ the accepted words are0011,0101,0110,1001,1010,1100. There are six, not twelve: selecting position1 then2 and selecting position2 then1 produce the same row. For $n=1$ the count is zero because no two-element subset exists; the convention $\binom12=0$ handles that boundary.

## Q34

Correct option: 3.

**Build a bijection or recover the coefficients.** An accepted row has precisely two distinct one positions and zero in every other position. Assigning an unordered two-element subset of the $n$ labeled positions uniquely specifies such a row, and every accepted row determines that subset. Thus the count is $\binom n2=n(n-1)/2$, with one canonical minterm per true row.

**General result.** The derivation gives $\binom n2$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $n(n-1)$, counts each two-element set twice by ordering its elements. Option 2, $n^2$, allows the same position twice and additionally retains order. Option 3, $\binom n2$, is the derived result. Option 4, $2^n$, counts all rows regardless of weight.

**Worked small example and transfer.** At $n=4$ the accepted words are0011,0101,0110,1001,1010,1100. There are six, not twelve: selecting position1 then2 and selecting position2 then1 produce the same row. For $n=1$ the count is zero because no two-element subset exists; the convention $\binom12=0$ handles that boundary.

## Q35

Correct option: 2.

**Analyze the scope rather than guessing from the previous number.**

Option 1 confuses a canonical table expansion with an optimized implementation. Option 2 correctly distinguishes these objectives. Option 3 describes a maxterm rather than a minterm. Option 4 counts ordered selections, but the word stores only the final set of selected positions. For two inputs, the exact-two function is one AND gate; for more inputs, canonical rows can sometimes be combined or implemented through shared intermediate logic, so row count is not a universal gate count.

**Underlying derivation.** An accepted row has precisely two distinct one positions and zero in every other position. Assigning an unordered two-element subset of the $n$ labeled positions uniquely specifies such a row, and every accepted row determines that subset. Thus the count is $\binom n2=n(n-1)/2$, with one canonical minterm per true row.

**Concrete check.** At $n=4$ the accepted words are0011,0101,0110,1001,1010,1100. There are six, not twelve: selecting position1 then2 and selecting position2 then1 produce the same row. For $n=1$ the count is zero because no two-element subset exists; the convention $\binom12=0$ handles that boundary.

## Q36

Correct option: 4.

**Build a bijection or recover the coefficients.** There is one binary constant coefficient and one binary coefficient for each of $n$ input variables. These $n+1$ decisions give $2^{n+1}$ expressions. To prove they give distinct functions, recover the constant as $c=F(0)$ and each linear coefficient as $a_i=F(e_i)\oplus F(0)$, where $e_i$ has a single one at position $i$. Identical truth tables therefore force identical coefficients.

**Exact requested instance.**
$$2^{3+1}=16$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $8$, comes from $2^n$, which omits the independent constant coefficient. Option 2, $256$, comes from $2^{2^n}$, which counts every Boolean truth table, including nonlinear functions. Option 3, $4$, comes from $n+1$, which counts coefficients instead of their binary assignments. Option 4, $16$, equals the exact result.

**Worked small example and transfer.** For example, $F=1\oplus x_1\oplus x_3$ has $F(0)=1$, $F(e_1)=0$, $F(e_2)=1$, $F(e_3)=0$, recovering coefficients1,0,1. Removing the constant gives the linear subclass, with $2^n$ functions, all zero at the origin. An affine function with a nonzero input coefficient has equally many true and false rows; the two constant functions are exceptions.

## Q37

Correct option: 3.

**Build a bijection or recover the coefficients.** There is one binary constant coefficient and one binary coefficient for each of $n$ input variables. These $n+1$ decisions give $2^{n+1}$ expressions. To prove they give distinct functions, recover the constant as $c=F(0)$ and each linear coefficient as $a_i=F(e_i)\oplus F(0)$, where $e_i$ has a single one at position $i$. Identical truth tables therefore force identical coefficients.

**Exact requested instance.**
$$2^{4+1}=32$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $65536$, comes from $2^{2^n}$, which counts every Boolean truth table, including nonlinear functions. Option 2, $5$, comes from $n+1$, which counts coefficients instead of their binary assignments. Option 3, $32$, equals the exact result. Option 4, $16$, comes from $2^n$, which omits the independent constant coefficient.

**Worked small example and transfer.** For example, $F=1\oplus x_1\oplus x_3$ has $F(0)=1$, $F(e_1)=0$, $F(e_2)=1$, $F(e_3)=0$, recovering coefficients1,0,1. Removing the constant gives the linear subclass, with $2^n$ functions, all zero at the origin. An affine function with a nonzero input coefficient has equally many true and false rows; the two constant functions are exceptions.

## Q38

Correct option: 2.

**Build a bijection or recover the coefficients.** There is one binary constant coefficient and one binary coefficient for each of $n$ input variables. These $n+1$ decisions give $2^{n+1}$ expressions. To prove they give distinct functions, recover the constant as $c=F(0)$ and each linear coefficient as $a_i=F(e_i)\oplus F(0)$, where $e_i$ has a single one at position $i$. Identical truth tables therefore force identical coefficients.

**General result.** The derivation gives $2^{n+1}$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $n+1$, counts coefficients instead of their binary assignments. Option 2, $2^{n+1}$, is the derived result. Option 3, $2^n$, omits the independent constant coefficient. Option 4, $2^{2^n}$, counts every Boolean truth table, including nonlinear functions.

**Worked small example and transfer.** For example, $F=1\oplus x_1\oplus x_3$ has $F(0)=1$, $F(e_1)=0$, $F(e_2)=1$, $F(e_3)=0$, recovering coefficients1,0,1. Removing the constant gives the linear subclass, with $2^n$ functions, all zero at the origin. An affine function with a nonzero input coefficient has equally many true and false rows; the two constant functions are exceptions.

## Q39

Correct option: 1.

**Analyze the scope rather than guessing from the previous number.**

Option 1 gives the correct arithmetic: coefficient addition is XOR in $\mathbb F_2$. Option 2 permits infinitely many ordinary-integer coefficient tuples unless a modulo-two equivalence is separately specified; that is not the stated binary parameter set. Option 3 is false for $x_1x_2$, whose pair ANF coefficient is one. Option 4 ignores the independent constant bit and therefore misses the factor two. A coefficient of0 removes an input, while a coefficient of1 includes it exactly once.

**Underlying derivation.** There is one binary constant coefficient and one binary coefficient for each of $n$ input variables. These $n+1$ decisions give $2^{n+1}$ expressions. To prove they give distinct functions, recover the constant as $c=F(0)$ and each linear coefficient as $a_i=F(e_i)\oplus F(0)$, where $e_i$ has a single one at position $i$. Identical truth tables therefore force identical coefficients.

**Concrete check.** For example, $F=1\oplus x_1\oplus x_3$ has $F(0)=1$, $F(e_1)=0$, $F(e_2)=1$, $F(e_3)=0$, recovering coefficients1,0,1. Removing the constant gives the linear subclass, with $2^n$ functions, all zero at the origin. An affine function with a nonzero input coefficient has equally many true and false rows; the two constant functions are exceptions.

## Q40

Correct option: 3.

**Build a bijection or recover the coefficients.** The true rows have weight zero or one. There is exactly one all-zero row and $n$ singleton-one rows, so the true-row count is $1+n$. The complete table has $2^n$ rows, leaving $2^n-n-1$ false rows. Canonical CNF has exactly one distinct maxterm for every false row; minimization is not part of the question.

**Exact requested instance.**
$$2^5-5-1=32-5-1=26$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $6$, comes from $n+1$, which counts true rows and therefore canonical DNF terms rather than CNF clauses. Option 2, $16$, comes from $2^{n-1}$, which assumes an unjustified half split. Option 3, $26$, equals the exact result. Option 4, $31$, comes from $2^n-1$, which removes only the all-zero true row and forgets the singleton-one rows.

**Worked small example and transfer.** For three inputs, the false words are011,101,110,111, giving four full three-literal maxterms. A shorter equivalent CNF is $(\neg x_1+\neg x_2)(\neg x_1+\neg x_3)(\neg x_2+\neg x_3)$, which has three clauses and forbids every pair of simultaneous ones. The reduced expression does not alter the four-clause canonical count.

## Q41

Correct option: 2.

**Build a bijection or recover the coefficients.** The true rows have weight zero or one. There is exactly one all-zero row and $n$ singleton-one rows, so the true-row count is $1+n$. The complete table has $2^n$ rows, leaving $2^n-n-1$ false rows. Canonical CNF has exactly one distinct maxterm for every false row; minimization is not part of the question.

**Exact requested instance.**
$$2^8-8-1=256-8-1=247$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $128$, comes from $2^{n-1}$, which assumes an unjustified half split. Option 2, $247$, equals the exact result. Option 3, $255$, comes from $2^n-1$, which removes only the all-zero true row and forgets the singleton-one rows. Option 4, $9$, comes from $n+1$, which counts true rows and therefore canonical DNF terms rather than CNF clauses.

**Worked small example and transfer.** For three inputs, the false words are011,101,110,111, giving four full three-literal maxterms. A shorter equivalent CNF is $(\neg x_1+\neg x_2)(\neg x_1+\neg x_3)(\neg x_2+\neg x_3)$, which has three clauses and forbids every pair of simultaneous ones. The reduced expression does not alter the four-clause canonical count.

## Q42

Correct option: 1.

**Build a bijection or recover the coefficients.** The true rows have weight zero or one. There is exactly one all-zero row and $n$ singleton-one rows, so the true-row count is $1+n$. The complete table has $2^n$ rows, leaving $2^n-n-1$ false rows. Canonical CNF has exactly one distinct maxterm for every false row; minimization is not part of the question.

**General result.** The derivation gives $2^n-n-1$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $2^n-n-1$, is the derived result. Option 2, $2^n-1$, removes only the all-zero true row and forgets the singleton-one rows. Option 3, $n+1$, counts true rows and therefore canonical DNF terms rather than CNF clauses. Option 4, $2^{n-1}$, assumes an unjustified half split.

**Worked small example and transfer.** For three inputs, the false words are011,101,110,111, giving four full three-literal maxterms. A shorter equivalent CNF is $(\neg x_1+\neg x_2)(\neg x_1+\neg x_3)(\neg x_2+\neg x_3)$, which has three clauses and forbids every pair of simultaneous ones. The reduced expression does not alter the four-clause canonical count.

## Q43

Correct option: 4.

**Analyze the scope rather than guessing from the previous number.**

Option 1 fails specifically at the all-zero word. Option 2 reverses the false-row indexing convention. Option 3 is false because fixing a row fixes every maxterm polarity; reordering literals does not create another maxterm. Option 4 correctly identifies the zero-word distinction. At $n=1$ every row is true, so canonical CNF has zero clauses; the empty conjunction equals1. This boundary is consistent with $2^1-1-1=0$.

**Underlying derivation.** The true rows have weight zero or one. There is exactly one all-zero row and $n$ singleton-one rows, so the true-row count is $1+n$. The complete table has $2^n$ rows, leaving $2^n-n-1$ false rows. Canonical CNF has exactly one distinct maxterm for every false row; minimization is not part of the question.

**Concrete check.** For three inputs, the false words are011,101,110,111, giving four full three-literal maxterms. A shorter equivalent CNF is $(\neg x_1+\neg x_2)(\neg x_1+\neg x_3)(\neg x_2+\neg x_3)$, which has three clauses and forbids every pair of simultaneous ones. The reduced expression does not alter the four-clause canonical count.

## Q44

Correct option: 3.

**Build a bijection or recover the coefficients.** The square-free monomials of degree at most two are the constant1, the $n$ single inputs, and the $\binom n2$ products of two distinct inputs. Every monomial receives a binary coefficient. Their total number is $1+n+\binom n2$, so binary coefficient assignments number $2^{1+n+\binom n2}$. ANF uniqueness proves these are distinct functions, rather than merely different written expressions.

**Exact requested instance.**
$$2^{1+3+\binom{3}{2}}=2^{7}=128$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $64$, comes from $2^{n+\binom n2}$, which omits the free constant coefficient. Option 2, $8$, comes from $2^n$, which counts onlyn binary choices and discards most ANF coefficients. Option 3, $128$, equals the exact result. Option 4, $256$, comes from $2^{2^n}$, which counts functions with higher-degree monomials as well whenn≥3.

**Worked small example and transfer.** Recover $c=F(0)$, $a_i=F(e_i)\oplus c$, and $a_{ij}=F(e_i+e_j)\oplus F(e_i)\oplus F(e_j)\oplus c$. Thus an alleged collision between two quadratic coefficient lists is impossible. At three inputs the missing cubic coefficient explains why only128 of the256 unrestricted functions qualify. At one or two inputs, every possible monomial already has degree at most two, so the restricted class coincides with all functions.

## Q45

Correct option: 2.

**Build a bijection or recover the coefficients.** The square-free monomials of degree at most two are the constant1, the $n$ single inputs, and the $\binom n2$ products of two distinct inputs. Every monomial receives a binary coefficient. Their total number is $1+n+\binom n2$, so binary coefficient assignments number $2^{1+n+\binom n2}$. ANF uniqueness proves these are distinct functions, rather than merely different written expressions.

**Exact requested instance.**
$$2^{1+4+\binom{4}{2}}=2^{11}=2048$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $16$, comes from $2^n$, which counts onlyn binary choices and discards most ANF coefficients. Option 2, $2048$, equals the exact result. Option 3, $65536$, comes from $2^{2^n}$, which counts functions with higher-degree monomials as well whenn≥3. Option 4, $1024$, comes from $2^{n+\binom n2}$, which omits the free constant coefficient.

**Worked small example and transfer.** Recover $c=F(0)$, $a_i=F(e_i)\oplus c$, and $a_{ij}=F(e_i+e_j)\oplus F(e_i)\oplus F(e_j)\oplus c$. Thus an alleged collision between two quadratic coefficient lists is impossible. At three inputs the missing cubic coefficient explains why only128 of the256 unrestricted functions qualify. At one or two inputs, every possible monomial already has degree at most two, so the restricted class coincides with all functions.

## Q46

Correct option: 1.

**Build a bijection or recover the coefficients.** The square-free monomials of degree at most two are the constant1, the $n$ single inputs, and the $\binom n2$ products of two distinct inputs. Every monomial receives a binary coefficient. Their total number is $1+n+\binom n2$, so binary coefficient assignments number $2^{1+n+\binom n2}$. ANF uniqueness proves these are distinct functions, rather than merely different written expressions.

**General result.** The derivation gives $2^{1+n+\binom n2}$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $2^{1+n+\binom n2}$, is the derived result. Option 2, $2^{2^n}$, counts functions with higher-degree monomials as well whenn≥3. Option 3, $2^{n+\binom n2}$, omits the free constant coefficient. Option 4, $2^n$, counts onlyn binary choices and discards most ANF coefficients.

**Worked small example and transfer.** Recover $c=F(0)$, $a_i=F(e_i)\oplus c$, and $a_{ij}=F(e_i+e_j)\oplus F(e_i)\oplus F(e_j)\oplus c$. Thus an alleged collision between two quadratic coefficient lists is impossible. At three inputs the missing cubic coefficient explains why only128 of the256 unrestricted functions qualify. At one or two inputs, every possible monomial already has degree at most two, so the restricted class coincides with all functions.

## Q47

Correct option: 4.

**Analyze the scope rather than guessing from the previous number.**

Option 1 is false because $x_i^2=x_i$ for either binary input value, not a new monomial. Option 2 uses OR where ANF requires XOR. Option 3 contradicts coefficient recovery; changing the constant alone flips the origin output. Option 4 is exactly the square-free reduction. “Degree at most two” includes affine and constant functions; the number of *exactly degree two* functions would subtract $2^{n+1}$, not use the same count.

**Underlying derivation.** The square-free monomials of degree at most two are the constant1, the $n$ single inputs, and the $\binom n2$ products of two distinct inputs. Every monomial receives a binary coefficient. Their total number is $1+n+\binom n2$, so binary coefficient assignments number $2^{1+n+\binom n2}$. ANF uniqueness proves these are distinct functions, rather than merely different written expressions.

**Concrete check.** Recover $c=F(0)$, $a_i=F(e_i)\oplus c$, and $a_{ij}=F(e_i+e_j)\oplus F(e_i)\oplus F(e_j)\oplus c$. Thus an alleged collision between two quadratic coefficient lists is impossible. At three inputs the missing cubic coefficient explains why only128 of the256 unrestricted functions qualify. At one or two inputs, every possible monomial already has degree at most two, so the restricted class coincides with all functions.

## Q48

Correct option: 4.

**Build a bijection or recover the coefficients.** The input cube has $n+1$ nonempty weight layers, indexed $k=0,1,\ldots,n$. A symmetric function is constant on each such layer, and each layer output is otherwise free. Choose these $n+1$ binary outputs independently to obtain $2^{n+1}$ functions. Different layer choices give different truth tables because every layer contains at least one word.

**Exact requested instance.**
$$2^{3+1}=16$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $8$, comes from $2^n$, which drops one of the two endpoint layers. Option 2, $256$, comes from $2^{2^n}$, which treats rows within a layer as independently adjustable. Option 3, $4$, comes from $n+1$, which counts layers rather than their binary output assignments. Option 4, $16$, equals the exact result.

**Worked small example and transfer.** For three inputs the layer sizes are1,3,3,1, but there are four output choices regardless of those unequal sizes. A layer-output vector $(0,1,0,1)$ specifies odd parity. A vector $(0,0,1,1)$ specifies majority. To count the true rows of either chosen function, sum the binomial layer sizes where its output is one; that is a different task from counting the class of all symmetric functions.

## Q49

Correct option: 3.

**Build a bijection or recover the coefficients.** The input cube has $n+1$ nonempty weight layers, indexed $k=0,1,\ldots,n$. A symmetric function is constant on each such layer, and each layer output is otherwise free. Choose these $n+1$ binary outputs independently to obtain $2^{n+1}$ functions. Different layer choices give different truth tables because every layer contains at least one word.

**Exact requested instance.**
$$2^{4+1}=32$$
The calculation counts the stated objects. A row count is not a function count, and the number of coefficients is not the number of their assignments.

**Inspect the alternatives.** Option 1, $65536$, comes from $2^{2^n}$, which treats rows within a layer as independently adjustable. Option 2, $5$, comes from $n+1$, which counts layers rather than their binary output assignments. Option 3, $32$, equals the exact result. Option 4, $16$, comes from $2^n$, which drops one of the two endpoint layers.

**Worked small example and transfer.** For three inputs the layer sizes are1,3,3,1, but there are four output choices regardless of those unequal sizes. A layer-output vector $(0,1,0,1)$ specifies odd parity. A vector $(0,0,1,1)$ specifies majority. To count the true rows of either chosen function, sum the binomial layer sizes where its output is one; that is a different task from counting the class of all symmetric functions.

## Q50

Correct option: 2.

**Build a bijection or recover the coefficients.** The input cube has $n+1$ nonempty weight layers, indexed $k=0,1,\ldots,n$. A symmetric function is constant on each such layer, and each layer output is otherwise free. Choose these $n+1$ binary outputs independently to obtain $2^{n+1}$ functions. Different layer choices give different truth tables because every layer contains at least one word.

**General result.** The derivation gives $2^{n+1}$ throughout the stated domain. An isolated parameter coincidence does not validate a competing expression.

**Inspect the alternatives.** Option 1, $n+1$, counts layers rather than their binary output assignments. Option 2, $2^{n+1}$, is the derived result. Option 3, $2^n$, drops one of the two endpoint layers. Option 4, $2^{2^n}$, treats rows within a layer as independently adjustable.

**Worked small example and transfer.** For three inputs the layer sizes are1,3,3,1, but there are four output choices regardless of those unequal sizes. A layer-output vector $(0,1,0,1)$ specifies odd parity. A vector $(0,0,1,1)$ specifies majority. To count the true rows of either chosen function, sum the binomial layer sizes where its output is one; that is a different task from counting the class of all symmetric functions.

## Q51

Correct option: 1.

**Analyze the scope rather than guessing from the previous number.**

Option 1 is true: the constant-zero function is symmetric but not self-dual. Option 2 fails for OR, which is zero at weight0 and one at weightn. Option 3 omits parity, majority and many other symmetric functions. Option 4 drops a nonempty layer whose output is independent unless another constraint is imposed. Symmetry relates words of equal weight; self-duality relates weights $k$ and $n-k$ by opposite outputs. Neither relation should be substituted for the other.

**Underlying derivation.** The input cube has $n+1$ nonempty weight layers, indexed $k=0,1,\ldots,n$. A symmetric function is constant on each such layer, and each layer output is otherwise free. Choose these $n+1$ binary outputs independently to obtain $2^{n+1}$ functions. Different layer choices give different truth tables because every layer contains at least one word.

**Concrete check.** For three inputs the layer sizes are1,3,3,1, but there are four output choices regardless of those unequal sizes. A layer-output vector $(0,1,0,1)$ specifies odd parity. A vector $(0,0,1,1)$ specifies majority. To count the true rows of either chosen function, sum the binomial layer sizes where its output is one; that is a different task from counting the class of all symmetric functions.

## Q52

Correct option: 3.

**A monotone function is fixed by its minimal true sets.** Identify a word with the set of its one positions. If the output is one on a set $S$, it must be one on every superset. Consequently the minimal true sets form an antichain: none contains another. Conversely, any antichain defines one monotone function by making a set true exactly when it contains a member of the antichain. The empty antichain gives constant zero; the antichain containing the empty set gives constant one.

**Enumerate antichains on three positions completely.** There is one empty antichain. There are eight singleton antichains, one for each subset. For a two-member antichain, both subsets must be incomparable. There are three pairs of singleton subsets, three pairs of two-element subsets, and three mixed pairs consisting of a singleton and the two-element subset excluding it. That gives nine. There are two three-member antichains: all three singleton subsets, or all three two-element subsets. No larger antichain exists: if a singleton occurs, every included pair must exclude it, leaving at most that one opposing pair; otherwise only the three pair subsets can form a nontrivial layer. Bottom and top subsets cannot coexist with any other member.
$$1+8+9+2=20.$$
Thus option 3 is correct. Eight counts individual cube rows, not antichains. Sixteen could confuse this class with all three-input symmetric functions. Two hundred fifty-six counts all unconstrained three-input functions, most of which violate monotonicity. The full eight-row check is a useful independent verification, but the antichain classification explains the count and why the classes are disjoint.

## Q53

Correct option: 2.

**Check the fixed complementary pair first.** The pair $000/111$ already has opposite outputs, zero and one, so it is consistent and adds no freedom. The remaining pairs are $001/110$, $010/101$, and $011/100$. Choose one representative output from each pair; its partner is forced to the opposite value.
$$N=2\cdot2\cdot2=8.$$
This is option 2. For example, choosing all three low-index representatives zero makes their partners one, giving table vector $0,0,0,0,1,1,1,1$. Choosing only representative $011$ to be one changes both011 and100, producing another valid table while retaining the fixed endpoints. These examples show that each free pair contributes a genuinely independent decision.

**Alternatives.** Four counts only two free pairs, omitting a valid decision. Sixteen is the unrestricted three-input self-dual count before the endpoint pair is fixed. Sixty-four treats the six remaining cells as independent and includes tables with equal outputs on a complementary pair. Every completion has exactly four true rows, one in each pair; that invariant alone does not determine how many different functions exist.

**Transfer.** With a partial self-dual specification, a pair with no fixed entries contributes two choices; a pair with one fixed entry contributes one; two opposite fixed entries also contribute one; two equal fixed entries make the entire specification inconsistent and give zero. Multiply the free-pair choices only after checking consistency of every constrained pair.
