# Individually rewritten proof solutions

These answers retain the original examination meanings and option order. Each proof explicitly records its domain, assumptions, justification and conclusion. Existing course readings are reused within the recorded source audit; this file does not claim a new exhaustive survey.

## Q1

**Correct option: 4.** Cardinal comparison $|A|\le |B|$ means that an injection from $A$ into $B$ exists. If the specified $f$ is injective, it is itself the required witness. This proves (a) without having to construct another map.

For (b), suppose $f$ is onto. Every fiber $f^{-1}(\{b\})$ is nonempty. Under the stated choice convention, select one element $s(b)$ from each fiber. Then $f(s(b))=b$. If $s(b_1)=s(b_2)$, apply $f$ to get $b_1=b_2$, proving that $s:B\to A$ is injective. Hence $|B|\le|A|$. For finite sets these selections require only finitely many choices; the infinite version is why the convention was stated.

For (c), a bijection is the witness that defines equal cardinality. Its inverse is also a function and gives the reverse comparison. However, equality of cardinalities asserts the existence of a bijection, not that the particular map named $f$ is that bijection. Let $A=B=\{0,1\}$ and $f(0)=f(1)=0$. The identity map witnesses equal cardinality, whereas $f$ is neither injective nor onto. This refutes (d).

Option 1 omits the true surjection implication. Option 2 includes the false converse (d) and omits (a),(c). Option 3 also includes (d) and omits (a),(b). Only option 4 lists precisely the three valid assertions. If $A=\varnothing$ and $B\ne\varnothing$, the empty function is injective but not onto; this boundary is consistent with (a) and does not make (d) true.

## Q2

**Correct option: 3.** The next-to-last line is universal introduction. Its justification includes a side condition: the parameter $u$ is arbitrary and is not fixed by any undischarged assumption. The complete derivation makes this visible.

| Line | Formula | Justification |
|---|---|---|
| 1 | $\forall xP(x,x)$ | Assumption for implication introduction |
| 2 | $P(u,u)$ | Universal elimination at arbitrary $u$ |
| 3 | $\exists zP(u,z)$ | Existential introduction with witness $z=u$ |
| 4 | $\forall y\exists zP(y,z)$ | Universal introduction, since $u$ was arbitrary |
| 5 | $\forall xP(x,x)\Rightarrow\forall y\exists zP(y,z)$ | Discharge line 1 by implication introduction |

The witness in line 3 may depend on the arbitrary input: for each $y$, choose $z=y$. The conclusion therefore has order $\forall y\exists z$, not $\exists z\forall y$.

Option 1, existential elimination, would start from an existential premise and temporarily use a fresh witness to derive a conclusion independent of its name. No such elimination occurs at line 4. Option 2 specializes a universal statement and cannot introduce the displayed leading universal quantifier. Option 4 creates an existential quantifier, as at line 3, but not the universal quantifier at line 4.

The freshness condition is essential. From the special assumption $u=0$ and fact $u\ge0$, one cannot infer that every real number is nonnegative. Here line 1 contains no free $u$, so it grants no special property to the parameter and the generalization is legitimate.

## Q3

**Correct option: 3.** Write transitivity without compressed chain notation:

$$\forall y\in A\;\forall x\in y\;(x\in A).$$

If $x\in\bigcup A$, the definition of union gives some $y\in A$ with $x\in y$. Transitivity then places $x$ in $A$, proving $\bigcup A\subseteq A$. Conversely, this containment puts every such $x$ in $A$, so it implies transitivity. This proves equivalence of condition (a), not just necessity.

For condition (b), $A\subseteq\mathcal P(A)$ means that every $y\in A$ belongs to the power set, hence is a subset of $A$. Expanding that subset condition says exactly that every $x\in y$ lies in $A$. Conversely, the transitivity assumption proves $y\subseteq A$ for each arbitrary $y\in A$, and therefore $y\in\mathcal P(A)$. This proves the second equivalence.

Both conditions are equivalent to the stated property, so selecting only one would discard an equivalent reformulation and selecting neither would discard both. The levels of objects matter: $y$ is a member of $A$, but its own members $x$ are the objects controlled by transitivity.

For a failure example, take $e=\varnothing$ and $A=\{\{e\}\}$. Its member $\{e\}$ contains $e$, which is not a member of $A$. Thus transitivity fails. The union is $\{e\}$ and is not a subset of $A$, refuting (a). The member $\{e\}$ is not a subset of $A$, so it does not belong to $\mathcal P(A)$; this refutes (b). For $A=\varnothing$, all three conditions hold vacuously. The proof handles that case without requiring an existential witness.

## Q4

**Correct option: 3.** Let $H(x),I(x),T(x)$ mean human, ignorant and thinker. The first argument has premises $\exists x(H(x)\land I(x))$ and $\forall x(H(x)\Rightarrow T(x))$. Choose a witness $u$ for the first premise. It has both $H(u)$ and $I(u)$. Applying the universal implication to that same $u$ gives $T(u)$, and hence $T(u)\land I(u)$. Existential introduction proves $\exists x(T(x)\land I(x))$.

The second argument has premises $\forall x(I(x)\Rightarrow\neg T(x))$ and $\forall x(H(x)\Rightarrow T(x))$. Fix an arbitrary $u$ and assume $H(u)$. This gives $T(u)$. If additionally $I(u)$ held, the first premise would give $\neg T(u)$, a contradiction. Thus $\neg I(u)$, and the arbitrary choice proves $\forall x(H(x)\Rightarrow\neg I(x))$.

The first argument needs an existing human witness and receives one explicitly. The second needs no human to exist: a universal prohibition holds when the human set is empty. In set form, its premises say $I\cap T=\varnothing$ and $H\subseteq T$, implying $H\cap I=\varnothing$.

Options 1 and 2 falsely reject one of these derivations; option 4 rejects both. A universal premise alone cannot introduce a witness, but an existential witness can be carried through a universal implication. Keeping the same individual in every step is what makes the first argument valid.

## Q5

**Correct option: 3.** Name the nested objects $e=\varnothing$, $s=\{e\}$ and $t=\{e,s\}$. Then $S_1=\{e,s\}$ and $S_2=\{e,s,t\}$. To evaluate a union, expose the members of each family member.

| Family member | Members exposed |
|---|---|
| $e$ | None |
| $s$ | $e$ |
| $t$ | $e,s$ |

Therefore $\bigcup S_1=\{e\}$ and $\bigcup S_2=\{e,s\}$. Every exposed object belongs to the respective original family, so both inclusions hold. Their unions are not equal to the families: $s$ is missing from the first union and $t$ from the second. Equality was not required.

Option 1 overlooks the valid second inclusion; option 2 overlooks the valid first inclusion; option 4 incorrectly rejects both. One can instead test the transitivity definition from the preceding question. In $S_1$, its member $s$ is a subset of $S_1$; in $S_2$, both $s$ and $t$ are subsets of $S_2$. The empty member is a subset in either case. Thus both families satisfy $S_i\subseteq\mathcal P(S_i)$, independently confirming the union test.

Removing $e$ from $S_1$ leaves $\{s\}$, whose union contains $e$ even though the family does not. This small modification illustrates the actual role of the membership witness and prevents treating every nested empty-set family as automatically acceptable.

## Q6

**Correct option: 2.** The source booklet's Persian phrase means **the identity function**, not an injective function. Assertion (a) is false. On $A=\mathbb Z$ with its usual strict order, define $f(k)=k+1$. For any $i<j$, addition of one gives $f(i)<f(j)$, so the map preserves the order. It is a self-map of $\mathbb Z$, yet $f(0)=1\ne0$, proving that it is not the identity.

<figure class="logic-diagram question-specific-diagram"><svg viewBox="0 0 720 200" role="img" aria-label="Three values of the order-preserving shift on the integers; each output is one greater than its input"><defs><marker id="q19-shift-tip" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#47768a"/></marker></defs><g fill="#28495b" style="font-family: Source Sans 3,sans-serif; font-size:17px"><text x="16" y="52">Input</text><text x="16" y="164">Output</text></g><g fill="#f2f8fa" stroke="#a2bac6"><circle cx="190" cy="48" r="25"/><circle cx="390" cy="48" r="25"/><circle cx="590" cy="48" r="25"/><circle cx="190" cy="160" r="25"/><circle cx="390" cy="160" r="25"/><circle cx="590" cy="160" r="25"/></g><g style="font-family: STIX Two Math,serif; font-size:21px" text-anchor="middle" fill="#28495b"><text x="190" y="55">−1</text><text x="390" y="55">0</text><text x="590" y="55">1</text><text x="190" y="167">0</text><text x="390" y="167">1</text><text x="590" y="167">2</text></g><g fill="none" stroke="#47768a" stroke-width="2" marker-end="url(#q19-shift-tip)"><path d="M190 73V135"/><path d="M390 73V135"/><path d="M590 73V135"/></g></svg><figcaption>Three values of the shift on the full integer domain. Left-to-right order is retained, but no displayed output equals its own input. The diagram is a finite excerpt of the map on all integers, not a self-map of these three inputs alone.</figcaption></figure>

Strict order preservation does imply the weaker claim of injectivity: if $x\ne y$, linear comparability gives $x<y$ or $y<x$, and the corresponding strict output inequality excludes equality of outputs. That correct theorem does not prove the source's stronger identity claim. On a **finite** linearly ordered set, an injective self-map is bijective and an order-preserving bijection must fix each successive element, so identity does follow there. The source places no finiteness hypothesis on $A$; the infinite counterexample decides its universal statement.

For (b), a finite set can be enumerated and ordered by its finite index. A countably infinite set has a bijective listing $g:\mathbb N\to B$. Define $g(i)\prec g(j)$ exactly when $i<j$. For any nonempty subset $C\subseteq B$, its index set $\{i:g(i)\in C\}$ is a nonempty subset of the natural numbers and has a least member. The element at that index is the least element of $C$. This constructs a well-order. The empty set is well-ordered vacuously.

This is existence of a suitable order, not a claim that every order already placed on a countable set is a well-order. The integers with their usual order have no least element, but a listing such as $0,1,-1,2,-2,\ldots$ induces a different well-order. Thus only (b) is true. Option 1 wrongly accepts (a) and rejects (b); option 3 wrongly accepts both; option 4 wrongly rejects the constructed well-order. The correct choice is 2. This revision corrects the earlier translation and answer, while retaining the source's four-option order.

## Q7

**Correct option: 3.** For the forward implication, write $n=6k$ for an integer $k$. Then $n^2=36k^2=6(6k^2)$, with an integer witness $6k^2$. This proves $6\mid n^2$ directly, including $n=0$ and negative $n$.

For the converse, if $6\mid n^2$, both 2 and 3 divide $n^2$. An odd integer has odd square, so $n$ is even. Squares modulo three are 0 or 1, and only inputs congruent to zero produce zero; therefore $3\mid n$. Write $n=3t$. Since $n$ is even and 3 is odd, $t$ is even, so $t=2k$ and $n=6k$.

One exhaustive residue table also proves the converse without assuming it:

| $n\bmod6$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| $n^2\bmod6$ | 0 | 1 | 4 | 3 | 4 | 1 |

Only residue zero satisfies the square condition. Options 1 and 2 omit a proved implication and option 4 omits both. This converse depends on the squarefree modulus six; for modulus four, $4\mid2^2$ but $4\nmid2$. The general condition is controlled by prime exponents, not by a universal rule allowing one to remove a square.

## Q8

**Correct option: 3.** Let $c=a^2-1$ and $d=a-1$. A real linear equation $cx=d$ has one solution when $c\ne0$, none when $c=0,d\ne0$, and all real numbers as solutions when both vanish.

| Parameter | Coefficient $c$ | Right side $d$ | Solution set |
|---|---:|---:|---|
| $a=1$ | 0 | 0 | All real numbers |
| $a=-1$ | 0 | $-2$ | Empty |
| $a\notin\{-1,1\}$ | Nonzero | $a-1$ | $\{1/(a+1)\}$ |

For the last row, division is legal and gives $x=(a-1)/[(a-1)(a+1)]=1/(a+1)$. Substitution verifies existence, and if two solutions $x_1,x_2$ existed, subtracting their equations gives $(a^2-1)(x_1-x_2)=0$; the nonzero coefficient forces $x_1=x_2$, proving uniqueness.

Option 1 permits $a=-1$, the no-solution case. Option 2 permits $a=1$, the infinitely-many-solutions case. Option 4 permits both. Cancelling $a-1$ without first checking whether it is zero erases the $a=1$ case. The classification precedes simplification; a unique-looking expression produced by illegal division is not a valid proof of uniqueness.

## Q9

**Correct option: 3.** A counterexample to a universally quantified implication must satisfy the domain, satisfy its antecedent and falsify its consequent. Here both inputs must be positive integers, their sum must be even, and they must fail to be both even.

| Pair | In domain? | Even sum? | Both even? | Refutes the claim? |
|---|---|---|---|---|
| $(2,4)$ | Yes | Yes, 6 | Yes | No |
| $(1,2)$ | Yes | No, 3 | No | No |
| $(3,5)$ | Yes | Yes, 8 | No | Yes |
| $(0,2)$ | No | Yes, 2 | Yes | No |

Thus only option 3 passes all counterexample requirements. The second pair falsifies the conclusion but also falsifies the premise, so its implication is true rather than false. The fourth is inadmissible independently of its arithmetic.

In fact, an even sum says that the two parities agree. Its possibilities are even-even and odd-odd, not only the former. Every pair of positive odd integers is therefore a counterexample. A single such pair is enough to refute the universal statement; it does not establish that all positive pairs violate it. The correct replacement statement is that an even sum occurs exactly when the two integers have the same parity.

## Q10

**Correct option: 2.** The verified range supplies the base fact $P(1)$. If the proposed universal successor implication is proved, induction gives $P(2)$ from $P(1)$, then $P(3)$ from $P(2)$, and, through the induction principle, $P(k)$ for every positive integer $k$. The step must be justified for arbitrary $n\ge1$, rather than checked at finitely many samples.

Option 1 leaves untested inputs beginning at $10^6+2$. To demonstrate its insufficiency, define $P(n)$ to mean $n\ne10^6+2$: all given tests and its extra test pass, yet the universal claim fails. For option 3, choose any tested additional integer $r$ and let $P(n)$ fail at another larger integer; a successful random sample still supplies no universal implication. Option 4 describes the search history rather than the truth of unsearched instances and cannot rule out that same kind of counterexample.

The exact role of the two induction obligations is different. A base fact alone does not propagate. A successor implication alone does not start: the property that is false at every positive integer has a vacuously true successor implication. Their conjunction proves the target. The next chapter develops induction systematically; this question distinguishes a completed proof obligation from merely increased numerical evidence.

## Q11

**Correct option: 2.** In statement I, the universal input $x$ is chosen first. Set $y=x+1$. This is an integer and $y>x$ for every integer $x$, so it is a permitted input-dependent witness and proves $\forall x\exists y(y>x)$.

Statement II requires a single integer $y$ chosen before $x$ varies. For any candidate $y$, take $x=y$. The desired strict inequality becomes $y>y$, which is false. This proves the negation

$$\forall y\exists x\;(y\le x),$$

with witness $x=y$. Thus II is false. Option 1 incorrectly reuses an input-dependent witness for the reversed quantifier order; option 3 reverses the two outcomes; option 4 ignores the valid construction for I.

If the condition were $y\ge x$, taking $x=y$ would not refute II, because equality now satisfies the relation. One must instead choose $x=y+1$. This boundary shows that a counterexample must be adapted to the exact predicate. On a finite nonempty ordered domain, I with strict $>$ fails at its maximum input. The proof above uses the unbounded integer domain explicitly.

## Q12

**Correct option: 2.** The identity $(x-y)^2=(x+y)^2-4xy$ and the sum condition give $(x-y)^2=100-4xy$. Since a real square is nonnegative, $100-4xy\ge0$ and hence $xy\le25$.

Equality holds precisely when $(x-y)^2=0$, so $x=y$. Combining with $x+y=10$ gives $x=y=5$. This pair is positive and attains the bound, proving that 25 is the maximum, not merely an upper bound. One may also set $y=10-x$ and complete the square:

$$xy=x(10-x)=25-(x-5)^2,\qquad0<x<10.$$

Option 1 reverses the bound and is refuted by $(1,9)$, whose product is 9. Option 3 is refuted by the attaining pair $(5,5)$. Option 4 is refuted by $(1,9)$ as well. Positivity restricts the admissible interval but the upper-square bound itself holds for every real pair with sum ten. The minimum is not attained in the positive domain: products approach zero as $x$ approaches zero or ten. That fact does not alter the attained maximum or justify a strict upper bound.

## Q13

**Correct option: 2.** Classical inference permits explosion from contradictory premises. A short derivation is:

| Line | Formula | Reason |
|---|---|---|
| 1 | $p$ | Premise |
| 2 | $\neg p$ | Premise |
| 3 | $p\lor q$ | Disjunction introduction from line 1 |
| 4 | $q$ | Disjunctive syllogism using lines 2 and 3 |

Semantically, entailment from premises means that every assignment satisfying them satisfies the conclusion. There are no assignments satisfying both $p$ and $\neg p$, so there is no premise-true, conclusion-false assignment, regardless of the chosen formula $q$.

Option 1 is false because the derivation applies to a noncontradictory conclusion such as an unrelated atom $q$. Option 3 confuses entailment under impossible premises with tautologicity without premises: an assignment giving $q$ false still shows that $q$ is not a tautology. Option 4 contradicts the classical two-valued definition of an assignment, which gives an atom exactly one value.

The premises remain part of the proof statement. One cannot erase them from a derivation and claim an arbitrary mathematical theorem. In particular, an algebraic argument that quietly obtains an impossible assumption and then continues may derive anything while establishing no useful conclusion about admissible inputs. This answer concerns classical logic; other logical systems require their own explicitly stated inference rules.

## Q14

**Correct option: 3.** The assumption $x=y\ne0$ implies $x-y=0$. Hence both sides of the displayed equation $(x-y)(x+y)=y(x-y)$ are zero. The equation itself is true and the factorization of $x^2-y^2$ is valid.

The invalid step divides by $x-y$, which is zero. A correct cancellation theorem says that $cz=cw$ implies $z=w$ when $c\ne0$ in a field. When $c=0$, it says only $0=0$ and conveys no equality between $z,w$. Here $x+y$ need not equal $y$: with $x=y=1$, those expressions are 2 and 1 even though their products by $x-y$ both vanish.

Option 1 wrongly rejects a valid factorization. Option 2 rejects a possible assumption witnessed by $x=y=1$. Option 4 does not repair the argument: zero cancellation fails over the rationals and reals as well as the integers. The stated nonzero hypothesis concerns $x$ and $y$, not their difference. Every division step must verify the precise divisor's nonzeroness, and later division by a nonzero $y$ cannot repair an earlier division by zero.

## Q15

**Correct option: 4.** Divide the interval 1 through 30 into the five blocks $\{6k+1,\ldots,6k+6\}$ for $k=0,\ldots,4$. The square residues modulo six for the input residues 1,2,3,4,5,0 are 1,4,3,4,1,0. Thus each block contains exactly one successful input, its last element. The complete list is 6,12,18,24,30, giving five.

This enumeration rests on the general equivalence $6\mid x^2$ if and only if $6\mid x$, proved through the prime factors two and three in Question 7. Option 1, ten, counts multiples of three, including 3 whose square is not divisible by six. Option 2, fifteen, counts even inputs, including 2 whose square is not divisible by six. Option 3 counts all thirty inputs. The square condition requires both prime divisibilities, so neither individual list suffices.

For an arbitrary interval 1 through $M$, the same equivalence gives $\lfloor M/6\rfloor$ inputs. The exact-block expression $n$ arises because $M=6n$ leaves no partial block. The result would not extend unchanged to modulus four: its square condition admits every even input, not only multiples of four. A converse proof must track the required prime exponents.

## Q16

**Correct option: 3.** For $n=8$, the interval ends at 48. Successful inputs are the eight multiples

$$6,12,18,24,30,36,42,48.$$

Every listed input has a square divisible by six. No other input qualifies: a residue 1 or 5 has square residue 1, a residue 2 or 4 has square residue 4, and a residue 3 has square residue 3. These cases exhaust the six input residues.

Option 1, 24, counts even inputs and overlooks divisibility by three. Option 2, 48, admits all inputs. Option 4, sixteen, counts multiples of three and overlooks evenness. In particular, $x=2$ and $x=3$ show why satisfying one factor does not satisfy the product condition.

The endpoint 48 is included and contributes the eighth successful value; replacing a closed endpoint by a strict upper bound would remove it. The proof also distinguishes integers *whose squares satisfy the condition* from distinct square residues: there is just one qualifying residue class, but eight inputs in the specified interval. Counting residue classes alone would answer a different question.

## Q17

**Correct option: 2.** By the equivalence $6\mid x^2\Leftrightarrow6\mid x$, every successful input has the unique form $x=6k$. The bounds $1\le x\le6n$ translate to $1\le k\le n$. The map $k\mapsto6k$ is a bijection between these $n$ indices and successful inputs, proving the count for every positive integer $n$.

Option 1, $6n$, is the full interval size. Option 3, $2n$, counts multiples of three, while option 4, $3n$, counts even inputs. Their failure is semantic rather than a rounding error: the former includes odd multiples of three and the latter includes even nonmultiples of three. On the smallest case $n=1$, only 6 succeeds, whereas those alternatives give six, two and three.

For a general positive modulus $m=\prod p_i^{e_i}$, the condition $m\mid x^2$ is equivalent to $\prod p_i^{\lceil e_i/2\rceil}\mid x$. Twice the exponent of each prime in $x$ must reach its required exponent in $m$. The squarefree modulus six has $e_i=1$, so its required divisor of $x$ is again six. This prime-exponent argument explains the converse's exact scope rather than treating a successful small residue table as a universal composite-modulus theorem.

## Q18

**Correct option: 1.** Write $m=\prod p_i^{e_i}$ and let $v_{p_i}(x)$ be the exponent of $p_i$ in a nonzero integer $x$. Then

$$m\mid x^2\quad\Longleftrightarrow\quad2v_{p_i}(x)\ge e_i\ \text{for every }i.$$

Equivalently, $v_{p_i}(x)\ge\lceil e_i/2\rceil$. These exponents are not generally $e_i$. For $m=12=2^2\cdot3$, the square condition requires $6\mid x$, not $12\mid x$: $x=6$ has square 36 divisible by twelve. Zero can be treated directly, since every positive modulus divides zero.

Options 2 and 3 both fail at $m=4,x=2$: the square is divisible by four but its root is not. Option 4 reverses a valid implication: if $x=mk$, then $x^2=m(mk^2)$, so root divisibility always implies square divisibility for integer $m,x$.

For a squarefree positive modulus all $e_i=1$, so the square condition does force root divisibility. Conversely, if some $e_i\ge2$, the number $\prod p_i^{\lceil e_i/2\rceil}$ satisfies square divisibility but has too few copies of at least that prime to be divisible by $m$. Hence squarefreeness exactly characterizes when the converse holds for all integer inputs.

## Q19

**Correct option: 3.** Five boxes can hold fifteen objects while every box has at most three: the occupancy vector $(3,3,3,3,3)$ is an explicit nonforcing arrangement. Sixteen objects cannot be distributed under that cap, because the sum of five occupancies each at most three would be at most fifteen. Therefore sixteen forces a box with at least four objects and is the smallest forcing count.

Option 4, fifteen, fails at the displayed vector. Option 2, nine, fails at $(3,3,3,0,0)$. Option 1, twenty, does force the conclusion, but is not the smallest forcing count, since sixteen already does. A sufficient answer can therefore still be an incorrect answer to a minimum-threshold question.

The average at sixteen objects is $16/5=3.2$, not four. Because occupancy is integer, an average above three implies some occupancy at least four. Requiring the average itself to reach four would unnecessarily increase the threshold. The object labels affect which distributions exist but not this worst-case capacity proof; empty boxes are permitted and cause no difficulty.

## Q20

**Correct option: 2.** With eight boxes, the largest nonforcing total is $8\cdot3=24$, attained by $(3,3,3,3,3,3,3,3)$. A total of twenty-five contradicts the sum bound if all occupancies are at most three. The construction at twenty-four and impossibility at twenty-five together prove minimality.

Option 3, twenty-four, is precisely the attainable nonforcing total. Option 1, twelve, can be distributed as $(3,3,3,3,0,0,0,0)$ and does not force four in any box. Option 4, thirty-two, is sufficient but unnecessarily large. The mean at twenty-five is $25/8=3.125$; integral occupancies, rather than equality of the mean to four, give the conclusion.

More generally, for arbitrary nonnegative integer occupancies $a_1,\ldots,a_8$ with sum twenty-five, assuming all $a_i\le3$ yields $25=\sum a_i\le24$, an actual numerical contradiction. This proof uses no assumption of equal distribution and does not construct a specific forced box in advance. The conclusion is existence of some box, whose identity may depend on the distribution.

## Q21

**Correct option: 1.** Let $a_i$ be the occupancy of box $i$. If no box reaches four, then $a_i\le3$ for every $i$, so $\sum_{i=1}^n a_i\le3n$. Thus $3n+1$ objects force at least one occupancy of four or more. Conversely, putting exactly three in every box gives a nonforcing distribution of $3n$ objects. Both directions prove the sharp threshold $3n+1$.

Option 2 is refuted by that construction. Option 3, $4n$, is a sufficient total but larger than $3n+1$ for $n>1$; agreement at $n=1$ does not make it a general minimum formula. Option 4, $n+4$, fails for example at $n=3$, where seven objects can have occupancies $(3,3,1)$; the correct threshold is ten.

The same argument for a target occupancy $k\ge1$ gives $(k-1)n+1$. A heterogeneous version with allowed occupancies $c_1,\ldots,c_n$ gives forcing total $1+\sum c_i$, provided those capacities are jointly attainable. This proof is a capacity inequality followed by a construction, not a claim that the objects actually distribute evenly. The question assumes at least one box; distributing positive objects into zero boxes is undefined in this model.

## Q22

**Correct option: 4.** A forcing proof establishes sufficiency of a total, but sharpness additionally requires a nonforcing arrangement at the preceding total. Here the capacity bound shows that $3n+1$ is sufficient and the vector $(3,\ldots,3)$ shows that $3n$ is not. For a smaller total, remove objects from that vector; this produces another nonforcing arrangement. Thus no smaller count forces the conclusion.

Option 1 is false: applying the same contradiction argument at $4n$ proves that $4n$ forces the conclusion, yet generally does not prove that $4n$ is minimal. Option 2 is false at five boxes and sixteen objects; the average is 3.2 and a box with at least four is already forced. Option 3 is false because an empty box has occupancy zero, which still obeys the upper bound three and is included correctly in the sum estimate.

The quantifier is “for every distribution, some box exceeds the cap.” Refuting a proposed threshold needs only one distribution with no such box. Proving it needs to rule out every distribution under the cap. The extremal vector supplies the first obligation, while the sum inequality supplies the second. This distinction between construction and universal impossibility is useful well beyond pigeonhole problems.

## Q23

**Correct option: 2.** Partition the ten available integers into the five disjoint pairs

$$\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}.$$

Every pair sums to eleven. A six-element chosen set places six distinct integers into five pairs, so one pair contributes both endpoints. This supplies the desired sum. Conversely, the five-element set $\{1,2,3,4,5\}$ chooses one endpoint per pair and has no sum eleven. Hence the smallest forcing size is six.

Option 3, five, is refuted by that set. Options 1 and 4, seven and ten, force the property but are not minimal. Distinctness of chosen values is necessary: six copies of 1 do not contain two values summing to eleven. The chosen object is a subset, so repetitions are excluded.

The complementary pairs are genuine disjoint classes: each number's partner is unique and taking the partner twice returns the original number. Because eleven is odd, no integer can be its own partner. These facts justify the partition used by the pigeonhole step; an arbitrary list of overlapping pairs would not support the same count.

## Q24

**Correct option: 1.** The sixteen integers partition into eight pairs $\{i,17-i\}$ for $i=1,\ldots,8$. The endpoints in a given pair sum to seventeen, and no endpoint appears in a different pair. A nine-element subset must select both endpoints of some pair.

The eight-element subset $\{1,\ldots,8\}$ contains no sum seventeen, since its two largest distinct values sum to fifteen. Thus nine is both sufficient and necessary as a threshold. Option 2, eight, fails at this concrete subset. Options 3 and 4, sixteen and ten, give larger sufficient values and therefore fail the “smallest” requirement.

There are $2^8=256$ nonforcing subsets of maximum size eight: choose one endpoint from each complementary pair. This characterizes the entire extremal family and explains why the exhibited lower half is only one counterexample, rather than an assumption about how every nonforcing subset looks. At sizes above eight, the choice-per-pair construction cannot avoid selecting two endpoints somewhere.

## Q25

**Correct option: 4.** The $2n$ integers are partitioned by the involution $i\mapsto2n+1-i$. There are no fixed points, since $2i=2n+1$ has no integer solution. The resulting $n$ disjoint two-element classes each contain exactly one complementary pair.

A subset of size $n+1$ must use both endpoints of at least one class, proving sufficiency. A subset choosing one endpoint from every class has size $n$ and avoids every complete pair, proving necessity. Hence the threshold is $n+1$.

Option 1 is refuted by $\{1,\ldots,n\}$. Option 2, $2n$, is larger than necessary for $n>1$. Option 3, $n+2$, is also unnecessarily large, and at $n=1$ is not even an available subset size. The smallest case has universe $\{1,2\}$ and threshold two, agreeing with the formula.

Every maximum nonforcing subset has exactly one endpoint per class; if it omitted a class, it would need a doubled class to reach size $n$, which would violate the nonforcing condition. Thus there are exactly $2^n$ such maximum subsets. This structural result independently identifies the obstruction behind the threshold.

## Q26

**Correct option: 3.** The original argument counts distinct selected integers, assigning each to its unique complementary pair. With repetition allowed, several selections might represent the same endpoint; two visits to a pair would no longer guarantee its two different endpoints. Repeating the number 1 any number of times yields only pair sums two, never the required odd sum $2n+1$. Therefore no finite selection threshold of the original kind is forced in that repeated-value model.

Option 1 imposes a nonexistent constraint on which endpoint is chosen. For $n=2$, both $\{1,2\}$ and $\{1,3\}$ are nonforcing maximum subsets, choosing different endpoint patterns. Option 2 is false because the partner map is an involution with no fixed points, so its classes are disjoint. Option 4 is refuted by $\{1,\ldots,n\}$, which has size $n$ but contains no complementary pair.

The proof requires both values in a pair, not merely two objects assigned to a common class. This distinction explains precisely where a multiset interpretation breaks the pigeonhole step. State whether “choose” means a subset, an ordered sample without replacement or a repeated sample before transferring a threshold formula.

## Q27

**Correct option: 1.** In the interval 1 through thirty, there are fifteen multiples of two and ten multiples of three. Their intersection consists of five multiples of six. To keep elements belonging to exactly one divisibility class, subtract that common class twice:

$$15+10-2\cdot5=15.$$

Equivalently, every six-object block has successful residue classes 2,3,4 and no others. The five blocks contribute $5\cdot3=15$. Option 2, twenty, counts the inclusive union and retains the multiples of six. Option 3, ten, counts the multiples of three alone, omitting even nonmultiples of three and including forbidden multiples of six. Option 4, twenty-five, adds the two divisibility counts without removing double-counting or the excluded intersection.

The words “or, but not by six” enforce an exclusive union here because the intersection of the two divisibility classes is exactly the multiples of six. Inclusion-exclusion first counts the union as twenty; deleting its five intersection members gives fifteen. The factor two in the direct expression accounts for their original double occurrence.

## Q28

**Correct option: 4.** In the interval 1 through forty-eight, the divisibility classes have sizes twenty-four and sixteen, with intersection size eight. The requested exclusive union therefore has size

$$24+16-2\cdot8=24.$$

Partitioning into eight consecutive blocks of six verifies it independently: the qualifying values in each block have residues 2,3,4. A residue zero is divisible by both and is excluded; residues 1 and 5 are divisible by neither.

Option 1, thirty-two, is the inclusive-union count $24+16-8$ and includes all eight multiples of six. Option 2, sixteen, counts the multiples of three without enforcing the full condition. Option 3, forty, is the unreconciled sum $24+16$, counting the eight forbidden intersection objects twice. The requested size equals the even-input count numerically in this interval, but the sets are different: 6 is even and excluded, whereas 3 is odd and included. Equal cardinality cannot replace the required membership predicate.

## Q29

**Correct option: 3.** Let $E$ be the multiples of two in the stated interval and $T$ its multiples of three. Their sizes are $3n$ and $2n$, and $|E\cap T|=n$. The required set is $E\triangle T$, whose size is

$$|E|+|T|-2|E\cap T|=3n+2n-2n=3n.$$

One can instead partition the interval into $n$ complete blocks of six; each has three qualifying residues, proving the result for every positive integer $n$. Option 1 counts only the multiples of three. Option 2 adds both class sizes without subtracting their common elements. Option 4 counts the inclusive union and retains the forbidden intersection.

For an arbitrary endpoint $M$, the corresponding formula is $\lfloor M/2\rfloor+\lfloor M/3\rfloor-2\lfloor M/6\rfloor$. The simpler $3n$ expression follows specifically from a complete number of six-element blocks. This generalization shows which divisibility hypotheses justify replacing floor functions by exact multiples of $n$.

## Q30

**Correct option: 2.** The integers 2 and 3 each lie in the union of the multiples-of-two and multiples-of-three classes, but their sum 5 lies in neither. All three values are within the stated interval when $n\ge1$. Thus the union is not closed under addition.

Option 1 reverses the overlap correction: adding class sizes counts a common object twice, so an inclusive union subtracts the intersection once. Option 3 is refuted even on the full integers by the additive subgroups $2\mathbb Z$ and $3\mathbb Z$. Their union contains 2 and 3 but not 5. Option 4 is refuted by 2, which is divisible by two but not by six; the product condition requires both coprime factors, not just one.

The finite interval classes are not themselves asserted to be additive subgroups: a finite bound also obstructs general addition closure. The subgroup counterexample uses the unbounded classes and keeps that distinction explicit. A counting identity about the union's size cannot prove an algebraic closure statement. The failure is a specific admissible pair whose sum leaves the set, rather than a vague claim that closure “usually” fails.

## Q31

**Correct option: 4.** A counterexample to the claim $x\le y$ has $x>y$, not $x\ge y$. For each first coordinate $x$, the eligible second coordinates are $1,\ldots,x-1$. On the five-object domain the row counts are explicit:

| $x$ | Possible $y$ | Count |
|---:|---|---:|
| 1 | None | 0 |
| 2 | 1 | 1 |
| 3 | 1,2 | 2 |
| 4 | 1,2,3 | 3 |
| 5 | 1,2,3,4 | 4 |

Their sum is ten. Option 1, fifteen, includes the five diagonal pairs by using $x\ge y$. Option 2 counts all twenty-five pairs. Option 3, four, counts only the final row with $x=5$ and omits the earlier six witnesses.

Each unordered pair of distinct values has exactly one orientation with $x>y$, so $\binom52=10$ provides a second construction. This question counts all counterexamples in a finite domain; just one of them, such as $(2,1)$, would already refute the universal claim. Enumerating ten failures does not show that all twenty-five pairs fail: the fifteen remaining pairs satisfy the inequality.

## Q32

**Correct option: 3.** For first coordinate $x=1,\ldots,8$, there are $x-1$ counterexample targets. The count is therefore $0+1+2+3+4+5+6+7=28$.

Among the sixty-four total ordered pairs, eight are diagonal. The remaining fifty-six split into two equal classes under coordinate exchange: one has $x>y$ and the other $x<y$. No off-diagonal pair is fixed by exchange, so half of fifty-six, namely twenty-eight, is the required count. This independently verifies the row sum.

Option 1, sixty-four, ignores the predicate. Option 2, seven, counts only the row $x=8$. Option 4, thirty-six, includes the eight diagonal pairs and counts $x\ge y$ instead. Equality satisfies the original non-strict inequality, so it cannot be a counterexample.

The exchange argument works because the two coordinates range over the same set. For domains of different sizes, the two strict-inequality classes need not be equinumerous. A row-count derivation remains valid after such a change, provided the permitted targets are counted in the actual second-coordinate domain. State this symmetry assumption before halving an off-diagonal count.

## Q33

**Correct option: 2.** Negating $x\le y$ in a total order gives $x>y$. The row with first coordinate $x$ contains $x-1$ such targets, and hence

$$\sum_{x=1}^{n}(x-1)=\frac{n(n-1)}2.$$

The sum identity follows by pairing terms from opposite ends: each pair totals $n-1$. Equivalently, there are $n^2-n$ off-diagonal ordered pairs, split equally between the two strict orientations, giving the same formula.

Option 1 counts only the $n-1$ witnesses with $x=n$. Option 3 includes equality and gives the larger count of pairs with $x\ge y$. Option 4 counts every ordered pair. At $n=1$ there is only $(1,1)$, which satisfies the claim, so the count is zero. At $n=2$ the unique counterexample is $(2,1)$, giving one.

The global universal claim has no counterexample when $n=1$ and fails for every $n\ge2$. The formula counts its failures, but the proof of failure for $n\ge2$ can simply exhibit $(2,1)$. These are distinct tasks: the existence of a counterexample and enumeration of all counterexamples should not be conflated.

## Q34

**Correct option: 1.** In a total order, exactly one of $x<y$, $x=y$ and $x>y$ holds. The condition $x\le y$ combines the first two alternatives; its negation is the third. Therefore equality is excluded from counterexamples.

Option 2 is refuted by $x=y=1$: it satisfies $x\le y$, so it cannot simultaneously witness its negation. Option 3 is refuted by any satisfying pair, such as $(1,2)$, which supports rather than refutes the inequality. Option 4 confuses two quantified claims. The failure at $(2,1)$ disproves “every pair satisfies the inequality,” but $(1,1)$ still satisfies it and disproves “every pair violates the inequality.”

This distinction is written logically as $\neg\forall x\forall y,P(x,y)\Leftrightarrow\exists x\exists y\,\neg P(x,y)$; it is not equivalent to $\forall x\forall y\,\neg P(x,y)$. The counterexample domain must also remain unchanged. A pair with a coordinate outside $\{1,\ldots,n\}$ cannot refute a bounded claim about that domain, even if its inequality is false. The derivation uses total order; negation on a partial order must separately account for incomparable elements.

## Q35

**Correct option: 4.** Use the complete representative list $0,1,\ldots,9$ modulo ten. An even input has even square, and an odd input has odd square. Thus the successful representatives are 1,3,5,7,9, giving five.

Parity is well-defined on residue classes modulo ten: replacing $r$ by $r+10k$ adds an even integer and preserves its parity. Squaring also preserves that parity. The count concerns input classes, not distinct output residues; for example 1 and 9 have the same square residue modulo ten but are different input classes and both must be counted.

Option 1, ten, admits the even classes as well. Option 2, four, omits one successful odd class. Option 3, six, includes an extra unsuccessful class. Neither endpoint zero nor the residue-nine class is a special exception: zero has even square and nine has odd square. Pairing consecutive representatives $(0,1),(2,3),\ldots,(8,9)$ gives exactly one odd input in each of five pairs and independently verifies the result.

## Q36

**Correct option: 3.** Modulo sixteen, take representatives 0 through fifteen. The successful inputs are $1,3,5,7,9,11,13,15$. They are exactly the eight odd classes, so the answer is eight.

For an even integer $r=2k$, $r^2=4k^2$ is even. For an odd integer $r=2k+1$, $r^2=2(2k^2+2k)+1$ is odd. These two exhaustive parity cases prove the criterion without testing large individual squares. The modulus is even, so representatives of the same residue class cannot have different parity.

Option 1, seven, removes one valid odd class. Option 2, nine, counts an extra even class. Option 4, sixteen, ignores the square-parity restriction. The square map is not injective on these inputs: for example, 1 and 15 both square to residue one modulo sixteen. That collapse does not reduce the requested count, which asks for input residues satisfying the predicate rather than the size of the image of the square map.

## Q37

**Correct option: 2.** The identity $r^2-r=r(r-1)$ shows that $r^2$ and $r$ have the same parity: two consecutive integers have an even product. Among $0,\ldots,2n-1$, exactly the $n$ representatives $2k+1$, with $k=0,\ldots,n-1$, are odd. Each qualifies and no even representative qualifies. Hence the count is $n$.

Option 1 adds an extra successful class, option 3 admits all $2n$ classes, and option 4 omits one odd class. The pairing $(2k,2k+1)$ partitions the representative list into $n$ pairs, each contributing one successful input, so no endpoint adjustment is needed. For $n=1$, residue zero fails and residue one succeeds, verifying the smallest case.

The parameter must satisfy $n\ge1$ because a modulus must be positive. “Modulo zero” is not a continuation of this residue-class model. With an odd modulus, representatives of one class can differ in parity, so parity of an integer representative is no longer an invariant of that class. The even-modulus hypothesis is therefore more than a convenience for counting half the representatives.

## Q38

**Correct option: 1.** A necessary residue condition can rule out an integer equation but need not establish that a solution exists. Every integer square is congruent to zero or one modulo four. The number 17 is congruent to one, so it passes that necessary test, yet it is not a square: $4^2=16<17<25=5^2$, and no integer lies strictly between four and five.

Option 2 is refuted by this compatible nonsquare. Option 3 is refuted algebraically: the square of $2k$ is $4k^2$, which is even. Option 4 is refuted by $x^2=3$ over the integers, since its right side is residue three modulo four while every square has residue zero or one. That congruence contradiction proves impossibility for every integer $x$.

For the specific predicate “$r^2$ is odd,” oddness of $r$ is both necessary and sufficient, as the two parity formulas prove. It is legitimate to count exactly $n$ input classes in that case. The caution is against promoting an arbitrary necessary residue check to a sufficient theorem for a different equation. A successful screening test and a constructed solution perform different logical jobs.

## Q39

**Correct option: 3.** Each distinct atom pair $(p_i,q_i)$ must avoid 10, the sole falsifying state of $p_i\Rightarrow q_i$. Its allowed states are 00,01,11, giving $3^5=243$ complete assignments making every implication true.

If all antecedents are true, every pair must have state 11, so exactly one assignment lacks a false antecedent. Excluding it leaves $243-1=242$. Option 4 retains that forbidden all-true assignment. Option 1, 32, counts only assignments with every antecedent false: each consequent is then free, but this omits models with a mixture of true and false antecedents. Option 2, 1023, starts from all $4^5$ pair assignments and removes only one; it therefore admits implication-falsifying state 10.

An independent classification by the number $j$ of false antecedents gives

$$\sum_{j=1}^{5}\binom5j2^j=10+40+80+80+32=242.$$

Choose which $j$ antecedents are false; their consequents are free, while every remaining true antecedent forces its consequent true. No implication is required to fail in this question. The extra property is vacuous truth of at least one implication, not a counterexample to an implication.

## Q40

**Correct option: 2.** Eight independent atom pairs each have three implication-satisfying states, so there are $3^8=6561$ complete models. Exactly one has every antecedent true, namely all eight pairs in state 11. Removing it gives 6560 models with at least one false antecedent.

Option 3 forgets that exclusion. Option 4, 256, counts the narrower family in which every antecedent is false; it uses the two states 00,01 at every pair. Option 1, 65535, subtracts one from the unrestricted $4^8$ total but leaves models containing a false implication, such as a first pair in state 10 and all remaining pairs in state 11.

To see a valid model missed by the all-false-antecedents count, put the first pair in state 00 and the other seven in state 11. Every implication is true and a false antecedent exists, so the model qualifies. By contrast, state 10 has a true antecedent and a false consequent, so it violates the implication. Recording both bits prevents these two states from being confused.

## Q41

**Correct option: 1.** There are $3^n$ models of the conjunction of the independent implications. The additional requirement is $\exists i\,\neg p_i$. Its failure is $\forall i,p_i$, which forces $q_i$ true at every position as well. Thus precisely one conjunction model is excluded and the count is $3^n-1$.

The binomial identity

$$\sum_{j=1}^{n}\binom nj2^j=(1+2)^n-1$$

proves the count by a disjoint partition according to which antecedents are false. Option 2 fails to require any false antecedent. Option 3 requires all antecedents false, rather than at least one. Option 4 fails to enforce the implications before subtracting.

The $2n$ atoms must be distinct for the independent product. If two implications are $p\Rightarrow q$ and $p\Rightarrow r$, requiring at least one of their antecedents false is simply requiring $p$ false; that gives four assignments of $q,r$, not $3^2-1=8$. On an empty index family, the conjunction is vacuously true but the existential false-antecedent requirement is false; the count is zero, agreeing with $3^0-1$. This boundary counts the empty valuation as a candidate and then excludes it.

## Q42

**Correct option: 4.** Material implication $p\Rightarrow q$ is equivalent to $\neg p\lor q$. When $p$ is false, this disjunction is true regardless of $q$. Thus truth of the implication alone does not establish its consequent. Modus ponens needs the additional premise $p$.

| $p$ | $q$ | $p\Rightarrow q$ | $\neg p\Rightarrow\neg q$ |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Option 1 is refuted by either false-antecedent row. Option 2 is refuted by $p=q=0$, which makes the implication true but the consequent false. Option 3 asserts equivalence to the inverse; the middle rows of the table refute it. The logically equivalent transformed implication is the contrapositive $\neg q\Rightarrow\neg p$, not the inverse.

In the counting problem, a false antecedent gives two consequent choices, whereas a true antecedent gives only one. This is the mathematical reason for the three local states. Vacuous truth is a truth-condition calculation, not a proof that the asserted implication's consequent holds in the real situation.

## Q43

**Correct option: 1.** For $n=5$, the positive triple has total nine. Fix its first coordinate $a$, which can range from one through seven. Then $b+c=9-a$, and positive choices of $b$ number $8-a$; $c$ is determined. The row counts are 7,6,5,4,3,2,1, summing to twenty-eight.

Equivalently, place two separators in the eight interior gaps of a row of nine objects. Their three positive block sizes are $a,b,c$, giving $\binom82=28$. The order of these coordinates matters, so $(1,2,6)$ and $(2,1,6)$ are different triples.

Option 2, 36, equals $\binom92$ and counts positive triples of total ten, rather than nine. Option 3, 21, equals $\binom72$ and counts positive triples of total eight. Option 4, 81, chooses two coordinates independently in a nine-value range but leaves the third potentially zero or negative and violates the total constraint. For example, $a=b=9$ would force $c=-9$.

An exhaustive search over these twenty-eight triples can prove a claim about this fixed total if every evaluation is correct. It cannot prove a claim over all positive totals unless an additional general argument connects those cases.

## Q44

**Correct option: 4.** For $n=8$, the total is twelve. Fix $a=1,\ldots,10$. The positive choices of $b$ range from one through $11-a$, with $c=12-a-b$ then positive. Hence the count is

$$10+9+\cdots+1=\frac{10\cdot11}{2}=55.$$

The separator construction independently chooses two gaps among the eleven interior gaps of twelve objects, giving $\binom{11}2=55$. Option 1, 66, counts positive triples of total thirteen, using twelve interior gaps. Option 2, 45, counts positive triples of total eleven, using ten gaps. Option 3, 144, chooses two coordinates from 1 through twelve without imposing the positivity of the residual third coordinate.

For each fixed $a$, both positive coordinates $b,c$ have an exact allowed range; “let the third coordinate be whatever remains” is incomplete unless that range is checked. A triple such as $(1,1,10)$ belongs to the family, whereas $(1,11,0)$ does not. These boundary cases distinguish positive from nonnegative stars-and-bars models and explain why changing the domain changes the separator count.

## Q45

**Correct option: 3.** Put $u=a-1,v=b-1,w=c-1$. This is a bijection between positive triples of total $n+4$ and nonnegative triples with $u+v+w=n+1$. Arrange $n+1$ stars and two bars, whose positions determine the three nonnegative blocks. There are $n+3$ total symbol positions, so choosing the two bar positions gives $\binom{n+3}2$.

Alternatively, fix $a=1,\ldots,n+2$. For each, there are $n+3-a$ positive pairs $(b,c)$, giving

$$\sum_{a=1}^{n+2}(n+3-a)=\frac{(n+2)(n+3)}2.$$

This equals the separator formula. Option 1 counts positive triples of total $n+3$, while option 4 counts those of total $n+5$. Option 2 chooses two coordinates independently from 1 through $n+4$ and ignores the residual positivity restriction. At $n=1$, the total is five and the six positive triples are the permutations of $(1,1,3)$ and $(1,2,2)$, agreeing with $\binom42=6$.

If the original variables were nonnegative instead, the count would be $\binom{n+6}2$, because their total would remain $n+4$ and two bars would add two symbol positions. The positivity shift is therefore a necessary step, not an arbitrary convention of notation.

## Q46

**Correct option: 2.** For a fixed total $N=n+4$, the positive triples form a finite, exactly enumerated domain. Checking a predicate $P(a,b,c)$ for every one of those triples establishes the bounded statement $\forall a,b,c>0\,(a+b+c=N\Rightarrow P(a,b,c))$. The proof must justify that every eligible triple was included and each evaluation is valid.

Option 1 is false because a triple outside that positive fixed-total domain does not satisfy the theorem's premise. Option 3 is false: define a property that holds for all triples with total $N$ but fails at $(1,1,N)$, whose total is $N+2$. A complete search at total $N$ would still pass. Option 4 is false because allowing zeros adds triples such as $(0,1,N-1)$ that the positive model excludes. The positive count $\binom{N-1}2$ and nonnegative count $\binom{N+2}2$ differ.

The search is a proof for its exact finite scope, rather than merely numerical evidence within that scope. It becomes insufficient only when its bounded conclusion is promoted to an unbounded one. This distinction is why a verification report should state its enumerated domains explicitly and why a general theorem still needs the symbolic derivation supplied in the preceding solution.

## Q47

**Correct option: 4.** At $n=40$, compute

$$n^2+n+41=1600+40+41=1681=41^2.$$

The input is a permitted nonnegative integer, and the output is composite because it has the proper divisor 41 between one and 1681. This single admissible failure disproves the universal prime claim.

For options 1,2,3, the outputs are 41,43,47. Each is prime: its square root is less than seven, so it suffices to test primes 2,3,5. None divides any of those three odd outputs; their digit sums are 5,7,11 and their last digits exclude a factor five. Those inputs therefore do not refute the claim.

The construction is systematic. For a positive constant $c$, substituting $n=c-1$ into $n^2+n+c$ gives $c^2$. Taking $c=41$ yields the shown failure rather than relying on a search guess. At $n=41$ there is another composite, $41\cdot43$. No claim about every intermediate output is needed; testing many earlier successes cannot remove this explicitly factored counterexample.

## Q48

**Correct option: 2.** For $x>0$,

$$x+\frac1x-2=\frac{x^2-2x+1}{x}=\frac{(x-1)^2}{x}\ge0.$$

The numerator is a nonnegative real square and the denominator is positive. Thus two is a lower bound. Equality holds exactly when $x=1$, which is admissible and gives $1+1=2$, proving that the lower bound is attained and is the minimum.

Option 1 is inconsistent with the bound. Option 3 incorrectly makes it strict and is refuted at $x=1$. Option 4 drops the positive-domain hypothesis: $x=-1$ gives $-2$, already below the asserted bound. On $x<0$, use $x+1/x+2=(x+1)^2/x\le0$, which proves $x+1/x\le-2$, with equality at $x=-1$. This uses a different square identity from the positive-domain proof. As $x$ approaches zero from below, the expression tends to negative infinity. Therefore it has no finite lower bound on all nonzero reals.

An independent proof uses AM-GM for the positive numbers $x$ and $1/x$, whose product is one. Their sum is at least two, with equality when $x=1/x$; positivity then selects $x=1$. Every method must retain the sign hypothesis and verify the equality witness. The excluded value zero makes the expression undefined and cannot be used as a counterexample or equality case.
